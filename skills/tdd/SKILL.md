---
name: tdd
description: Behavior-driven red/green implementation rules for adding behavior, fixing bugs, or implementing approved Changes as an implementer.
license: MIT
---

# TDD

Test behavior through public interfaces, completing one red → green slice at a time. Use existing Glossary names and respect approved behavior and design contracts. This skill does not start other agents.

## Test Boundaries

Use the approved plan's test interfaces, explaining detectable errors and limits of proof. Existing approval does not require repeated questions for each test. Refer missing test-boundary decisions affecting the contract or required interface changes to the main agent first.

When a module interface itself needs design, use [design-writing](../design-writing/SKILL.md) to select the necessary analysis and return consequential choices to the main agent. Reading design references does not authorize changes to approved boundaries. Handle contract gaps, conflicts, and local implementation choices under the [document contract](../change-planning/references/document-contract.md).

Tests detect broken behavior and survive internal refactors. Use contract-derived expectations under the [acceptance basis](../change-planning/references/document-contract.md#acceptance-basis), not implementation-derived values. Read [test examples](tests.md) before tests and [mocking rules](mocking.md) for substitution. Keep runner/fixture repairs within scope and explain them; return changed expected semantics to the main agent.

## Each Behavior Slice

1. **red**: For new behavior or bug fixes, first run a test that detects the missing behavior or actual symptom. Fix fixture, runner, permission, or environment errors first; they are not red. Reuse an existing valid failing test. If a bug cannot be reproduced, establish a repeatable check for the actual symptom before guessing a fix.
2. **green**: Implement only what the current behavior requires, then run the corresponding complete check until it passes. Do not write all tests in one batch and then implement them in another, or implement future capabilities early. Restructure only as needed for implementation or approved review fixes; do not expand scope for refactoring every cycle.
3. **record**: Record commands, key failure/pass output, chronology, proven behavior, and scope in runtime artifacts. A post-implementation failure cannot retroactively count as pre-implementation red. Record the task identifier or name so the main agent can verify progress.

Tests preserving existing behavior may stay green throughout; explain the regression they would detect instead of deliberately breaking fixtures to manufacture red. One test focuses on one behavior and may contain multiple assertions jointly describing it. Prioritize approved important scenarios rather than splitting assertions to increase test count.

Documentation, configuration, and packaging tasks do not require red. Use mechanical validation or a short mapping of key facts to authoritative sources. Normative lists, versions, and identifiers need precise source locations; ordinary descriptions do not require sentence-by-sentence fact tables.

## Task-specific Implementation Methods

For Go implementation, read [golang-patterns](../golang-patterns/SKILL.md) and, when adding or changing Go tests, [golang-testing](../golang-testing/SKILL.md). Error propagation and cancellation work uses the matching language reference in [error-handling](../error-handling/SKILL.md); suspected swallowed failures use [silent-failures](../code-review/references/silent-failures.md). SQL/schema work uses [postgres-patterns](../postgres-patterns/SKILL.md), and migrations additionally use [database-migrations](../database-migrations/SKILL.md), preserving the application's existing deployment contract. A concrete Go build, vet, or lint failure uses [go-build-recovery](references/go-build-recovery.md). These are methods for the implementer, not new roles, automatic commands, or extra phases; they do not replace the slice order above. Load LLM cost or cache skills only for an actual cost or cache task via [task methods](../agent-workflow/references/task-methods.md).

## Validation and Handoff

Run focused tests/static checks and all checks assigned to the implementer. Follow [validation responsibilities](../agent-workflow/references/execution.md#validation-responsibilities) for final checks, source identity and reruns. Return task evidence and unproven scope concisely in the existing handoff; keep detailed logs in run artifacts. Neither reducing execution count nor filling a report justifies changing validation scope.

Distinguish implementation, behavior-test coverage, and verification at promised boundaries. Fakes prove only the logic they cover, not real process, network, or storage guarantees. Report a blocker if a required boundary cannot be verified; do not claim completion.

Modify only assigned implementation, tests, and non-contract deliverables. Assigned README, example, or configuration tasks may follow their corresponding evidence rules. The main agent owns Change contracts, approval state, and long-term Spec/Design/ADR. Do not edit other lanes' files. Return evidence for the main agent to update authoritative task status. Redact detailed output and preserve it through review and handoff.

See [sources](../agent-workflow/references/sources.md).
