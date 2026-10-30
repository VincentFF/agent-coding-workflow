# Silent Failure Review Perspective

Use this reference when evaluating whether errors or failure states are obscured by success returns, default fallbacks, or unobserved logging. This is a review method for the existing `code-reviewer` role; findings are reported under [code-review](../SKILL.md).

1. **Locate Catch and Fallback Sites:** Identify `catch` blocks, discarded errors, blank identifier assignments (`_`), default return values, fallback handlers, background tasks, and transaction boundaries. Code matching is a starting point; read full execution branches to verify whether errors can occur and who observes them.
2. **Trace Error Observation:** For each failure path, ask: Is the root cause preserved? Does the return value or status code still indicate success? Can callers distinguish "no data found" from "dependency failed"? Has an error log become an unmonitored dead end?
3. **Asynchronous and Goroutine Failures:** Ensure Promise rejections are awaited, returned, or supervised. Verify that goroutine errors are returned to waiting coordinators. Issuing a cancellation signal or calling `void` does not prove work completed successfully.
4. **Audit Fallbacks:** Fallback logic must reflect approved specifications. Returning empty arrays, nulls, default models, or stale cache entries upon authentication failure, write failure, or missing required evidence obscures defects. Valid "not found" results or best-effort cleanup are not defects if their behavior matches contracts.
5. **Resource and Transaction Integrity:** Check timeouts and cleanup for I/O and database operations. In transactions, verify handling of rollback, commit errors, and ambiguous commit states. Cleanup operations must not overwrite the primary failure or misrepresent partial execution as untouched state.
6. **Logging Hygiene:** Verify logs include operation context, identifiers, and root causes without exposing sensitive credentials or unredacted tokens. Avoid logging identical errors repeatedly at every stack frame.

Validate doubts with targeted failure injection or concrete code paths. Report specific locations, violated contracts, observable false successes, and minimal fix suggestions.

Adapted from ECC (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
