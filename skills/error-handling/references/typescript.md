# TypeScript / JavaScript Error Handling

Use this reference when designing or reviewing TypeScript/JavaScript error handling. Check the target environment (browser, Node.js server, or extension host), runtime APIs, and existing conventions before introducing error patterns.

## Classification and Cause Preservation

- In `catch (err: unknown)` blocks, narrow the error type before accessing properties. Avoid relying solely on `instanceof` across realms (such as iframes or separate Node vm contexts).
- When defining custom errors, extend `Error` and preserve the underlying cause using `new CustomError("message", { cause: err })`. Verify target runtime compatibility for `Error.cause`.
- Provide structured error codes or discriminated unions when callers need to branch on specific failure modes. Map internal errors to user-safe messages at the application boundary; do not expose raw stack traces or internal SQL/API responses to end users.

## Asynchronous Code and Cancellation

- Every Promise must be awaited, returned, or explicitly handed off to an error-observing supervisor. Do not leave floating promises unhandled; synchronous `try/catch` blocks cannot intercept rejected asynchronous promises.
- When using `Promise.all`, remember that one rejection rejects the group immediately but does not cancel other in-flight promises. Handle in-flight side effects and cleanup.
- Pass `AbortSignal` to cancelable operations (`fetch`, timeouts, streams). In `finally` blocks, ensure timers, event listeners, and streams are cleaned up. Distinguish expected user cancellations (`AbortError`) from server failures; do not retry aborted operations.
- `fetch()` does not reject on HTTP 4xx or 5xx responses; check `response.ok` explicitly before parsing the body. Handle JSON parsing errors independently from network errors.

## Execution Environments

| Environment | Error Boundary Considerations |
| --- | --- |
| Browser | Reflect loading and error states in UI; clean up timers and subscriptions on component unmount; manage expired response race conditions; use UI error boundaries for rendering crashes without neglecting async promise errors. |
| Node.js Server | Map errors to standardized API responses at HTTP/RPC boundaries; ensure background workers log context and report failures; do not rely on global unhandled rejection handlers for normal error flow. |
| Extension Host / CLI | Consult installed host SDK APIs and lifecycle contracts; report errors through host-provided notification or logging mechanisms; do not assume browser DOM or Node.js server middleware exist. |

Verify rejection handling, cancellation, and error display using focused tests. See [silent-failures](../../code-review/references/silent-failures.md).

Adapted from ECC (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
