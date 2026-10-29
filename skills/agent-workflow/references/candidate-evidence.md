# Optional Candidate Helper

Use existing handoff/runner source records first under [validation responsibilities](execution.md#validation-responsibilities). A clean, stable tree can use a fixed SHA; an adequate dirty-tree fingerprint needs no extra index. Use [candidate.py](../scripts/candidate.py) only when actual content identity/comparison is missing. It does not run tests, manage tasks or approve evidence reuse.

## Capture and Compare

Requires Python 3.10+ and Git, with no third-party packages. Resolve the skill directory and retain the original delivery baseline:

```bash
python3 <agent-workflow-directory>/scripts/candidate.py capture \
  --repo <repository-root> --base <fixed-start-commit> \
  --output <run-directory>/candidate-a.json

python3 <agent-workflow-directory>/scripts/candidate.py compare \
  --before <run-directory>/candidate-a.json \
  --after <run-directory>/candidate-b.json \
  --output <run-directory>/candidate-delta.json
```

Capture only when a boundary needs an otherwise missing identity; do not add snapshots per role, poll or every check. Output JSON must be outside the repository or Git-ignored, and cannot overwrite tracked source or comparison inputs. Failures preserve previous output.

Capture hashes tracked and non-ignored untracked bytes, executable flags and missing-file markers. Symlinks use target text without reading external contents; ignored artifacts are excluded. Two passes detect instability but do not lock the tree. Unsupported kinds such as submodules fail explicitly.

Compare validates both indexes and requires the same root/baseline. It lists differing source entries; a HEAD-only change is metadata, not a content change.

Exit codes: capture `0` succeeds; compare `0` means indexed source unchanged and `1` means changed; `2` means invalid input, mismatch, unsupported source or unstable capture. Compare `1` is a change signal, not a failed test.

Checksums do not establish authenticity, correct expectations, external configuration/artifact equivalence or successful test execution. Keep results in existing records and assess reuse under execution handoff; no additional report or gate is created by this helper.

Behavior tests use disposable Git repositories:

```bash
python3 -m unittest discover -s <agent-workflow-directory>/tests -v
```
