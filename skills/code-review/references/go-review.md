# Go Review Perspective

This reference provides a review checklist for the existing `code-reviewer` role when inspecting Go code. It is not an independent agent role or a separate workflow stage. Evaluate code against the fixed baseline and complete candidate scope, including configuration and tests.

1. **Call Chains and State:** Trace critical inputs and failure paths from entry points through services to persistence and external dependencies. Verify interfaces and lifecycles against [golang-patterns](../../golang-patterns/SKILL.md) and test adequacy against [golang-testing](../../golang-testing/SKILL.md).
2. **Concurrency and Goroutine Lifecycle:** For every goroutine, verify creator, shared state ownership, cancellation propagation, blocking operations, error collection, and channel closure. Ensure worker pool limits and lock ordering are observed; passing the race detector does not prove deadlock or leak freedom.
3. **Resource and Error Lifecycles:** Verify cleanup for derived cancel contexts, HTTP response bodies, file descriptors, database rows, connections, and transactions. Check for `defer` inside loops, unchecked `rows.Err()`, unhandled commit ambiguity, and lost error causes. For swallowed errors, consult [silent-failures](silent-failures.md).
4. **Security and Trust Boundaries:** Verify parameterization in database queries, safe argument handling for external commands, real boundary checks for file paths, TLS certificate validation, and credential redaction. Issues must have reachable triggers and demonstrable impact.
5. **Pragmatic Performance:** Focus on meaningful bottlenecks, N+1 queries, excessive allocations in hot loops, and lock contention. Do not block delivery on line counts, lack of slice pre-allocation without proof, direct `return err` without wrapping where context is unneeded, or non-table-driven tests.

Report findings under the Spec and Standards axes of [code-review](../SKILL.md), citing concrete sources, reachable triggers, locations, impact, and missing proof.

Adapted from ECC (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
