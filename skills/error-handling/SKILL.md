---
name: error-handling
description: Design and review error classification, propagation, cancellation, resource cleanup, and user-facing messages across Go and TypeScript.
license: MIT
---

# Error Handling Patterns

Use this skill for designing error boundaries, diagnosing failures, and reviewing error recovery or fallback logic. Identify the programming language and execution environment, then read the applicable reference:
- Go: [Go Error Handling](references/go.md)
- TypeScript/JavaScript: [TypeScript Error Handling](references/typescript.md)

Browser, Node.js server, and extension host environments have distinct lifecycles and error propagation models; do not mix them. This skill does not start agents or prescribe rigid API response envelopes.

## Tracing Failure Paths End-to-End

1. Identify all potential failure points: input validation, network requests, database calls, external model invocations, and async tasks. Trace the error from its origin to callers, persistent state, and user observation.
2. Categorize errors into clear domain categories: expected business failures, configuration/auth defects, transient dependency outages, timeouts/cancellations, and unhandled internal bugs. Preserve root causes rather than converting all errors into generic failure messages.
3. Explicitly assign responsibility for each failure: return to caller, execute defined fallback, record persistent failure, or terminate the operation. Merely logging an error and returning success is an unhandled failure.
4. Ensure cancellation signals propagate and resources close cleanly. Issuing a cancel signal does not prove work has stopped; wait for execution to terminate. Ensure cleanup failures do not mask the primary error.
5. Verify failure behavior with concrete inputs: assert return types, status codes, user-visible messages, and persisted state.

## Fallbacks, Retries, and Observability

Fallbacks must adhere to approved specifications. Never disguise missing data, authentication failures, or dependency crashes behind silent empty arrays or default objects unless explicitly specified. For auditing swallowed errors, see [silent-failures](../code-review/references/silent-failures.md).

Retries must be deliberate:
- Verify whether existing client libraries or worker queues already perform retries before adding retry logic.
- Retry only idempotent operations and transient network failures. Never retry authentication errors, validation errors, or non-idempotent mutations without deduplication keys.
- Ensure backoff delays are cancelable via context or abort signals. Do not stack multiple layers of retries.

Logs must contain actionable context (operation name, identifiers, error category, root cause) while strictly redacting credentials, tokens, and sensitive personal data. User-facing messages should provide clear guidance without leaking internal stack traces or database schema details.

Adapted from ECC (MIT License). See [ECC sources](../agent-workflow/references/ecc-sources.md).
