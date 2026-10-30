# Go Build and Linter Diagnostics Recovery

Use this reference when an `implementer` encounters Go compilation, `go vet`, linter, or module dependency failures. This is a recovery procedure for the existing implementer role; it does not authorize expanding task scope or architectural redesign.

1. **Capture Exact Failure:** Run build/vet/lint commands from the relevant module root. Record the failing command, exit code, and first relevant error diagnostic. Distinguish between environment issues (missing tools, permissions) and source code errors; environment issues are not behavioral red tests.
2. **Identify Root Cause:** Read the error location, related type definitions, interface implementations, callers, build tags, and `go.mod`. Address root causes first, rather than suppressing cascading secondary errors.
3. **Apply Minimal Surgical Fixes:**
   - Undefined symbols: check spelling, package visibility, and imports.
   - Type mismatches: check pointer vs value receivers and interface method sets.
   - Missing returns: complete control flow branches cleanly.
   - Import cycles: evaluate dependency direction; if architectural changes are needed, refer them to the main agent.
   - Never use blank identifiers (`_`) to discard errors, apply blind type assertions, or insert empty stub implementations merely to satisfy the compiler.
4. **Re-verify:** Re-run the original failing command until clean. Run package tests to ensure no regressions were introduced. Format only the modified files using project-configured tools. Never run repository-wide reformatting or unsolicited `go mod tidy` unless authorized.
5. **Module Dependencies:** For dependency errors, use `go mod why -m` or `go mod verify`. Do not run automatic `go get -u`, wipe module caches, bypass checksums, or upgrade Go language versions without explicit authorization.

Do not remove assertions, skip tests, or add unjustified `//nolint` directives to eliminate warnings. If an interface or contract change is unavoidable and exceeds the approved Change boundary, stop and report the blocker to the main agent.

Adapted from ECC (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
