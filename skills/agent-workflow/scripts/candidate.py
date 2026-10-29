#!/usr/bin/env python3
"""Capture source identity or compare candidates; evidence reuse stays a review decision."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile


def git(repo, *args):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, errors="surrogateescape", timeout=15)
    if result.returncode:
        raise ValueError("Git command failed: " + " ".join(args[:2]))
    return result.stdout


def digest(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def source_files(repo):
    names = sorted(set(git(repo, "ls-files", "--cached", "--others", "--exclude-standard", "-z").split("\0")) - {""})
    result = {}
    for name in names:
        path = repo / name
        if not path.parent.resolve().is_relative_to(repo):
            raise ValueError("Source parent resolves outside the repository: " + name)
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            result[name] = {"kind": "missing"}
            continue
        if stat.S_ISLNK(mode):
            result[name] = {"kind": "symlink", "sha256": hashlib.sha256(os.fsencode(os.readlink(path))).hexdigest()}
        elif stat.S_ISREG(mode):
            sha = hashlib.sha256()
            # A symlink swapped in by an active writer must not redirect the read.
            fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            with os.fdopen(fd, "rb") as source:
                for block in iter(lambda: source.read(1024 * 1024), b""):
                    sha.update(block)
            result[name] = {"kind": "file", "sha256": sha.hexdigest(), "executable": bool(mode & 0o111)}
        else:
            raise ValueError("Unsupported source kind (for example submodule/directory): " + name)
    return result


def capture_source(repo, base):
    if Path(git(repo, "rev-parse", "--show-toplevel").strip()).resolve() != repo:
        raise ValueError("--repo must identify the repository root")
    base = git(repo, "rev-parse", "--verify", "--end-of-options", base + "^{commit}").strip()
    head = git(repo, "rev-parse", "HEAD").strip()
    files = source_files(repo)
    if files != source_files(repo) or head != git(repo, "rev-parse", "HEAD").strip():
        raise ValueError("Source changed while capturing; release write ownership and retry")
    return {"version": 1, "repo": str(repo), "base": base, "head": head,
            "source_sha256": digest(files), "files": files}


def output_path(path, repo):
    path = path.resolve()
    if path.suffix != ".json":
        raise ValueError("--output must be a JSON path")
    if path.is_relative_to(repo):
        ignored = subprocess.run(["git", "-C", str(repo), "check-ignore", "-q", "--", str(path)], capture_output=True)
        if ignored.returncode:
            raise ValueError("--output must be outside the repository or in an ignored run directory")
    return path


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Publish a complete index; a failed capture never replaces earlier evidence.
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            json.dump(data, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.replace(temporary, path)
        finally:
            if temporary.exists():
                temporary.unlink()


def load_candidate(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("version") != 1 or not isinstance(data.get("files"), dict):
        raise ValueError("Unsupported candidate index: " + str(path))
    if not all(isinstance(data.get(key), str) for key in ("repo", "base", "head", "source_sha256")):
        raise ValueError("Incomplete candidate identity: " + str(path))
    if not Path(data["repo"]).is_absolute():
        raise ValueError("Candidate repository must be absolute")
    for key in ("base", "head"):
        if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", data[key]):
            raise ValueError("Invalid candidate Git identity")
    for name, entry in data["files"].items():
        if not name or Path(name).is_absolute() or ".." in Path(name).parts or not isinstance(entry, dict):
            raise ValueError("Invalid candidate source entry")
        kind = entry.get("kind")
        fields = {"kind"} if kind == "missing" else {"kind", "sha256"}
        if kind == "file":
            fields.add("executable")
            if not isinstance(entry.get("executable"), bool):
                raise ValueError("Invalid source executable flag")
        if kind not in ("file", "symlink", "missing") or set(entry) != fields:
            raise ValueError("Unsupported candidate source entry")
        if kind != "missing" and not re.fullmatch(r"[0-9a-f]{64}", str(entry.get("sha256"))):
            raise ValueError("Invalid source digest")
    if data["source_sha256"] != digest(data["files"]):
        raise ValueError("Candidate index checksum mismatch: " + str(path))
    return data


def compare_candidates(before, after):
    if (before["repo"], before["base"]) != (after["repo"], after["base"]):
        raise ValueError("Candidate repository and fixed baseline must match")
    changed = sorted(name for name in before["files"].keys() | after["files"].keys()
                     if before["files"].get(name) != after["files"].get(name))
    return {"status": "changed" if changed else "unchanged", "changed": changed,
            "before_sha256": before["source_sha256"], "after_sha256": after["source_sha256"],
            "metadata_changed": ["head"] if before["head"] != after["head"] else []}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    capture = commands.add_parser("capture")
    capture.add_argument("--repo", type=Path, required=True)
    capture.add_argument("--base", required=True)
    capture.add_argument("--output", type=Path, required=True)
    compare = commands.add_parser("compare")
    compare.add_argument("--before", type=Path, required=True)
    compare.add_argument("--after", type=Path, required=True)
    compare.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            repo = args.repo.resolve()
            output = output_path(args.output, repo)
            result = capture_source(repo, args.base)
            write_json(output, result)
            print(f"{result['source_sha256']} {len(result['files'])} files; {output}")
            return 0
        if args.output.resolve() in (args.before.resolve(), args.after.resolve()):
            raise ValueError("Comparison output must not overwrite either candidate index")
        before, after = load_candidate(args.before), load_candidate(args.after)
        output = output_path(args.output, Path(after["repo"]))
        result = compare_candidates(before, after)
        write_json(output, result)
        print(f"{result['status']}: {len(result['changed'])} source changes; {output}")
        return 1 if result["changed"] else 0
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
