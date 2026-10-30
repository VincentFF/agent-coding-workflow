---
name: golang-patterns
description: Idiomatic Go patterns for package structure, consumer interfaces, error propagation, goroutine lifecycle, resource cleanup, and profiling.
license: MIT
---

# Go Implementation Patterns

Use this skill for Go implementation, refactoring, or idiomatic design questions. Adhere to the project's existing architecture, module structure, and validation contracts before applying generic patterns. This skill does not start agents or authorize unrequested public API changes.

## Minimal Changes from Call Chains

1. Locate the symbol definition, callers, tests, configuration, and exports using code search. Trace both the success path and failure path to identify state owners, inputs, and side effects.
2. Respect existing package boundaries. Do not introduce speculative service or repository abstractions if the codebase does not already use them. Prefer standard library and installed dependencies over adding new external libraries.
3. Define interfaces on the consumer side, keeping them minimal. Returning concrete types is usually clearer, but existing interface contracts take precedence. Keep types usable in their zero value whenever possible. Perform and validate required initialization (maps, slices, pools) at creation boundaries.
4. Choose method receivers intentionally based on mutability, copy cost, method sets, and synchronization primitives. Never copy a type containing a sync primitive (`sync.Mutex`, `sync.WaitGroup`). Avoid package-level mutable state and hidden I/O in `init()`. Use functional options only when configuration complexity warrants them; embedding expands method sets and should reflect genuine capability inheritance.

## Error and Resource Lifecycles

Trace every file, HTTP, database, and channel operation: who acquires, who closes, when execution returns, and who observes failure.

- Return `error` for recoverable failures; reserve `panic` for unrecoverable programmer invariants. Wrap errors with `fmt.Errorf("...: %w", err)` to provide actionable operational context while preserving the root cause. Classify errors with `errors.Is` and `errors.As` instead of string matching. Avoid redundant repetitive wrapping.
- Never discard errors using the blank identifier (`_`). Evaluate whether cleanup failures affect correctness: closing, flushing, or committing may be success boundaries. If cleanup failure can be safely ignored, document why and ensure it does not overwrite the primary error.
- Schedule cleanup immediately after acquiring resources. Be mindful of `defer` inside loops, as deferred calls execute only when the enclosing function returns; wrap loop bodies in helper functions when necessary. Always close response bodies and database rows, checking `rows.Err()`.
- Pass `ctx context.Context` as the first parameter on request and I/O paths. Ensure every derived cancel function is called, and never replace an incoming context with `context.Background()` solely to bypass upstream cancellation.
- Place transaction boundaries strictly around atomic state changes. Avoid holding database transactions across external network or model calls. Handle ambiguous commit results without assuming failure implies rollback.

For domain error categorization, see [error-handling](../error-handling/SKILL.md). For detecting swallowed errors, see [silent-failures](../code-review/references/silent-failures.md).

## Concurrency with Definite Termination

Every goroutine must have an explicit creator, shared state owner, cancellation/exit signal, and waiting observer.

- Bound worker pool sizes, queue capacities, and connection usage. Account for peer disconnects and `ctx.Done()` on both channel sends and receives. Buffering a channel does not eliminate goroutine leaks.
- Close channels from the sender side, and ensure exactly one owner closes each channel after all writers finish. Observe worker errors explicitly rather than fire-and-forget logging.
- Protect shared memory with mutexes or channel ownership. Avoid performing I/O, holding foreign locks, or invoking arbitrary callbacks while holding a mutex. Keep lock acquisition order consistent.
- When shutting down services, stop accepting new work, cancel/drain in-flight tasks, and wait for background workers before releasing shared pools and listeners.

Verify cancellation, timeouts, concurrency limits, and clean termination using [golang-testing](../golang-testing/SKILL.md). Review concurrency code with [go-review](../code-review/references/go-review.md).

## Measure Before Optimizing

Profile real hot paths before introducing slice pre-allocation, batching, `strings.Builder`, or object pools. Do not pre-allocate huge slices without bounded input size evidence. Use `sync.Pool` only with allocation profiling evidence; never retain references or slice aliases to pooled objects after returning them.

Run formatters, linters, and package tests using the project's configured tooling from the appropriate module root. For compilation or linter errors, see [go-build-recovery](../tdd/references/go-build-recovery.md).

Adapted from ECC (MIT License). See [ECC sources](../agent-workflow/references/ecc-sources.md).
