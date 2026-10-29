"""Public CLI tests using disposable Git repositories and actual source files."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "candidate.py"


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Fixture")
        self.write("main.py", "value = 1\n")
        self.write("removed.txt", "original\n")
        self.write(".gitignore", ".cache/\n")
        self.commit()
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True)

    def write(self, name, text):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def commit(self):
        self.git("add", "--all")
        self.git("commit", "-qm", "fixture")

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True, check=False, timeout=15)

    def capture(self, name="candidate.json"):
        output = Path(self.temp.name) / name
        result = self.run_cli("capture", "--repo", self.repo, "--base", self.base, "--output", output)
        self.assertEqual(0, result.returncode, result.stderr)
        return output, json.loads(output.read_text())

    def compare(self, before, after):
        output = Path(self.temp.name) / "comparison.json"
        result = self.run_cli("compare", "--before", before, "--after", after, "--output", output)
        self.assertTrue(output.is_file(), result.stderr)
        return result.returncode, json.loads(output.read_text())

    def test_capture_records_dirty_new_deleted_and_ignored_source_correctly(self):
        self.write("main.py", "value = 2\n")
        self.write("new test.py", "assert True\n")
        (self.repo / "removed.txt").unlink()
        self.write(".cache/log.txt", "runtime output\n")
        _, data = self.capture()
        self.assertEqual(hashlib.sha256(b"value = 2\n").hexdigest(), data["files"]["main.py"]["sha256"])
        self.assertIn("new test.py", data["files"])
        self.assertEqual("missing", data["files"]["removed.txt"]["kind"])
        self.assertNotIn(".cache/log.txt", data["files"])
        self.assertEqual(self.base, data["base"])
        self.assertEqual(self.base, data["head"])

    def test_same_source_is_stable_when_only_ignored_runtime_output_changes(self):
        _, first = self.capture("first.json")
        self.write(".cache/log.txt", "new runtime output\n")
        _, second = self.capture("second.json")
        self.assertEqual(first["source_sha256"], second["source_sha256"])
        self.assertTrue(first["source_sha256"])

    def test_compare_lists_source_changes_without_approving_evidence_reuse(self):
        before, _ = self.capture("before.json")
        self.write("main.py", "value = 3\n")
        self.write("new.py", "assert True\n")
        (self.repo / "removed.txt").unlink()
        after, _ = self.capture("after.json")
        code, data = self.compare(before, after)
        self.assertEqual(1, code, data)
        self.assertEqual(["main.py", "new.py", "removed.txt"], data["changed"])
        self.assertEqual("changed", data["status"])
        self.assertNotIn("reusable", data)

    def test_compare_preserves_source_identity_across_a_metadata_only_commit(self):
        before, _ = self.capture("before.json")
        self.git("commit", "--allow-empty", "-qm", "metadata only")
        after, _ = self.capture("after.json")
        code, data = self.compare(before, after)
        self.assertEqual(0, code, data)
        self.assertEqual([], data["changed"])
        self.assertEqual(["head"], data["metadata_changed"])

    def test_tampered_snapshot_is_rejected_and_prior_comparison_is_preserved(self):
        before, _ = self.capture("before.json")
        after, data = self.capture("after.json")
        data["files"]["main.py"]["sha256"] = "0" * 64
        after.write_text(json.dumps(data))
        output = Path(self.temp.name) / "comparison.json"
        output.write_text('{"previous":"preserve"}\n')
        result = self.run_cli("compare", "--before", before, "--after", after, "--output", output)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertEqual('{"previous":"preserve"}\n', output.read_text())

    def test_expected_results_changed_alongside_code_remain_visible(self):
        self.write("expected.json", '{"count":2}\n')
        before, _ = self.capture("before.json")
        self.write("main.py", "value = 1\n# changed behavior\n")
        self.write("expected.json", '{"count":1}\n')
        after, _ = self.capture("after.json")
        code, data = self.compare(before, after)
        self.assertEqual(1, code, data)
        self.assertEqual(["expected.json", "main.py"], data["changed"])

    def test_symlink_targets_are_recorded_without_reading_external_contents(self):
        outside = Path(self.temp.name) / "outside.txt"
        outside.write_text("original external contents\n")
        link = self.repo / "external-link"
        link.symlink_to(outside)
        before, data = self.capture("before.json")
        self.assertEqual("symlink", data["files"]["external-link"]["kind"])
        self.assertEqual(hashlib.sha256(os.fsencode(str(outside))).hexdigest(), data["files"]["external-link"]["sha256"])
        outside.write_text("new external contents\n")
        after, _ = self.capture("after.json")
        code, _ = self.compare(before, after)
        self.assertEqual(0, code)

    def test_executable_bit_change_is_detected(self):
        before, _ = self.capture("before.json")
        (self.repo / "main.py").chmod(0o755)
        after, _ = self.capture("after.json")
        code, data = self.compare(before, after)
        self.assertEqual(1, code, data)
        self.assertEqual(["main.py"], data["changed"])

    def test_different_baselines_cannot_be_used_to_hide_delivery_changes(self):
        before, _ = self.capture("before.json")
        self.write("main.py", "value = 4\n")
        self.commit()
        self.base = self.git("rev-parse", "HEAD").strip()
        after, _ = self.capture("after.json")
        result = self.run_cli("compare", "--before", before, "--after", after,
                              "--output", Path(self.temp.name) / "comparison.json")
        self.assertEqual(2, result.returncode, result.stderr)

    def test_source_and_snapshot_inputs_cannot_be_overwritten_by_output(self):
        source = self.write("source.json", '{"keep":true}\n')
        self.commit()
        self.write(".gitignore", ".cache/\nsource.json\n")
        result = self.run_cli("capture", "--repo", self.repo, "--base", self.base, "--output", source)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertEqual('{"keep":true}\n', source.read_text())
        before, _ = self.capture("before.json")
        saved = before.read_bytes()
        result = self.run_cli("compare", "--before", before, "--after", before, "--output", before)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertEqual(saved, before.read_bytes())

    def test_ignored_output_can_be_reused_and_source_files_remain_unchanged(self):
        output = self.repo / ".cache/candidate.json"
        saved = {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.iterdir() if p.is_file()}
        for _ in range(2):
            result = self.run_cli("capture", "--repo", self.repo, "--base", self.base, "--output", output)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertNotIn(".cache/candidate.json", json.loads(output.read_text())["files"])
        self.assertEqual(saved, {str(p.relative_to(self.repo)): p.read_bytes() for p in self.repo.iterdir() if p.is_file()})

    def test_invalid_baseline_does_not_replace_an_existing_index(self):
        output = Path(self.temp.name) / "candidate.json"
        output.write_text('{"old":"preserve"}\n')
        result = self.run_cli("capture", "--repo", self.repo, "--base", "missing-ref", "--output", output)
        self.assertEqual(2, result.returncode, result.stderr)
        self.assertEqual('{"old":"preserve"}\n', output.read_text())


if __name__ == "__main__":
    unittest.main()
