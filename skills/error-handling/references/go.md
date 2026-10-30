# Go Error Handling, Cancellation, and Cleanup

Use this reference when designing or reviewing Go error handling. Adhere to the project's existing sentinel errors and error types before introducing new ones.

- Wrap errors with operation context using `fmt.Errorf("operation: %w", err)`. Use `errors.Is` to check sentinel errors across wrapped chains and `errors.As` to extract structured error types. Avoid string matching on error messages. Do not add redundant wrapper layers that repeat the function name without adding context.
- Distinguish between not-found, permission, validation, timeout, and storage errors. Preserve underlying driver or network errors in the error chain. Map errors to appropriate status codes and safe user messages at boundary layers.
- Check state mutations and side effects when an error occurs. Ambiguous commit errors mean the transaction outcome is uncertain; do not assume rollback occurred without verification. Always call `defer tx.Rollback()` after `db.BeginTx()`; a rollback after a successful commit is safely ignored by standard drivers.
- Propagate `ctx context.Context` through network, database, and background calls. Invoke cancel functions when derived contexts are created, and wait for controlled goroutines to terminate upon cancellation. Never use `context.Background()` to bypass upstream timeouts.
- Collect errors from goroutines through synchronized error channels or wait groups. Logging an error inside a goroutine and returning nil to the caller creates silent failures. Reserve `panic` for unrecoverable invariants; if recovering from panic at service boundaries, log stack traces and ensure resources are cleaned up.
- Always check `rows.Err()` after iterating database rows. Close response bodies, files, and connections promptly. Avoid accumulating `defer` statements inside long loops by extracting the loop body into a helper function. Combine cleanup errors with primary errors when cleanup affects data durability.

Verify error classification, propagation, and cancellation with targeted unit and integration tests. See [golang-testing](../../golang-testing/SKILL.md) and [silent-failures](../../code-review/references/silent-failures.md).

Adapted from ECC (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
