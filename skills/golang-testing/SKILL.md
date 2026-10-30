---
name: golang-testing
description: Select minimal effective Go testing methods: subtests, test cleanup, HTTP testing, fakes, golden files, fuzzing, benchmarks, and coverage diagnostics.
license: MIT
---

# Go Testing Patterns

Select the minimal effective test strategy for new behavior, regression fixes, or evidence gaps in Go projects. The red-green-refactor cycle, contract expectations, and handoff rules are governed by [tdd](../tdd/SKILL.md). This skill does not start agents or override project testing conventions.

## Deciding What Causes Test Failure

Identify publicly callable behavior interfaces based on the target specification. Enumerate expected outputs, invalid inputs, dependency failures, cancellations, and persistence boundaries. Expectations must derive from contracts or independent facts, not by duplicating implementation logic.

| Problem | Minimal Effective Method | Proof Boundary |
| --- | --- | --- |
| Multiple inputs through the same behavior | Named test cases or `t.Run` subtests; table-driven tests when structures are identical | Table-driven structure is not mandatory; avoid forcing disparate lifecycles into a single loop |
| HTTP status, headers, and body | `httptest.NewRequest` and `httptest.ResponseRecorder` | Proves handler logic; listener binding, connection handling, and network propagation require integration tests |
| External dependency failure modes | Controlled fakes implementing consumer interfaces | Proves caller error handling; does not prove third-party protocol compliance |
| Persistence, locking, commit ambiguity | Project-isolated real database integration fixtures | Unit fakes cannot prove database lock order, transaction isolation, or real constraints |
| Worker concurrency, cancellation, and exit | Channel/sync synchronization with bounded timeouts | Do not use fixed `time.Sleep` to guess timing; race detector pass does not prove leak freedom |
| Parser invariants and boundary inputs | Go fuzzing (`testing.F`) with representative seeds | Invariants must derive from contract properties, not round-tripping through the same implementation |
| Profiled performance concerns | Repeatable benchmarks (`testing.B`) recording allocations and input sizes | Report benchmark metrics separately from behavioral correctness |

## Isolation and Cleanup

- Mark test helper functions with `t.Helper()` to preserve accurate failure call sites.
- Use `t.TempDir()` for temporary filesystem fixtures. Register cleanup immediately after acquiring resources with `t.Cleanup()`. Cleanup must cancel running goroutines and wait for them to finish before closing shared pools.
- Use `t.Parallel()` only when tests are completely isolated from shared state (ports, environment variables, working directories, shared database records).
- Each subtest must be independently runnable and must not depend on side effects from preceding subtests.
- Async assertions must synchronize back to the main test goroutine; do not call `t.Fatal` from background goroutines.

## Assertions, Errors, and Fixtures

- Assert both return values and specific error categories using `errors.Is` or `errors.As` where appropriate; avoid asserting merely that an error is non-nil.
- Check HTTP body read errors, database rows iteration errors (`rows.Err()`), and resource close semantics.
- Cancellation tests must verify that workers actually exit and release resources, not just that `context.Canceled` was returned.
- Golden files must be reviewable and updated intentionally via explicit test flags; never auto-update golden files on test failure. Never store credentials or sensitive tokens in test fixtures.
- When fixing flaky tests, isolate shared mutable state or non-deterministic inputs; do not remove assertions or inflate sleep durations.

## Targeted Test Execution

Run tests from the target application module root. Focus on the affected package first:
```bash
go test ./path/to/package -run TestSpecificBehavior -count=1
```

Run with `-race` when evaluating concurrency changes. Use integration fixtures when persistence or process boundaries must be proven. Benchmarks use `-bench` and `-benchmem`. Fuzzing uses `-fuzz` with a bounded `-fuzztime`. Use coverage profiling (`-coverprofile`) as a diagnostic aid to locate untested branches; do not treat arbitrary percentage targets as behavioral proof.

Adapted from ECC (MIT License). See [ECC sources](../agent-workflow/references/ecc-sources.md).
