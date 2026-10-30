---
name: code-review
description: Review a stable candidate tree read-only, reporting contract compliance and project standards separately and checking test and validation evidence.
license: MIT
---

# Code Review

Read original contracts and current code; prioritize evidence. By default, one code-reviewer reports both axes separately without merging or reordering findings across axes. This skill neither starts other agents nor modifies project files. Within agent-workflow, the first review must use an independent code-reviewer with fresh context.

## 1. Define the Review Target

Confirm repo/cwd, a fixed comparison baseline, the current candidate tree, and the complete change list. Use a resolvable fixed ref/SHA for the baseline; do not silently switch to a moving branch tip during review. The main agent normally provides the starting baseline. Ask if it is unclear; do not assume working-tree differences from HEAD contain the entire delivery.

Inspect committed changes from baseline to candidate, staged and unstaged content, untracked new files, and deletions. Judge the net effect of the current tree. A commit or empty working-tree diff does not mean there are no changes. Without Git, use explicit original/candidate snapshots or file lists; report a blocker if no reliable comparison scope exists.

Read the Change entry and listed applicable material set, including the target Spec, necessary PRD/Design and original referenced sections. Compare against current contracts, ADRs and required approval sources; legacy single-file Changes remain valid. Judge implementation against the approved target and preserved existing guarantees, then check final long-term merge diffs for fidelity and conflicts. Read applicable project standards such as CODING_STANDARDS and CONTRIBUTING. Summaries are not substitutes for original requirements. In standalone review without contracts, report the Spec axis as indeterminate; team delivery cannot use that absence to bypass contract gates.

Establish expected behavior from original sources and the [acceptance basis](../change-planning/references/document-contract.md#acceptance-basis) before evaluating writer claims. For a changed PRD, use [prd-writing](../prd-writing/SKILL.md)'s review branch; for a changed Spec, use [spec-writing](../spec-writing/SKILL.md)'s review branch. For changed Design or assessment of consequential structural changes, use [design-writing](../design-writing/SKILL.md)'s review branch; it selects specialist analysis for actual doubts. Reading unchanged contracts alone does not require the writing skills. Check fixture/expected/runner diffs even when code and tests pass together. Use existing source records under [validation responsibilities](../agent-workflow/references/execution.md#validation-responsibilities); a separate candidate index is optional.

## 2. Spec Axis: Contract Compliance

- Check all consequential behavior, structural constraints and non-goals against original sources for omissions or unrequested changes; a coverage table is only an index.
- Check interfaces, errors, persistence, compatibility, and external interactions, prioritizing high-risk guarantees.
- Audit tests: the runner actually executes them, required awaits are present, key checks are not skipped, assertions are not swallowed, and expected values do not merely mirror implementation. Identify which check would fail if the target behavior were broken.
- Check red causes and chronology. Fixture or environment failures are not behavior evidence. For behavior-preservation checks, state the regression failure mode without requiring manufactured red.
- Distinguish implementation, behavior-test coverage, and verification at promised boundaries. Unit fakes do not prove real process, network, or storage guarantees; do not pass missing required evidence.
- Check for contradictions among requirements, tasks, and validation. List pending long-term synchronization and acceptance archival assigned to the main agent as closeout obligations, without claiming they are complete. Pending PRD/Spec/Design synchronization requires focused review of the final diff before team acceptance under the corresponding writing skill. Missing documents assigned to this round's writer remain implementation defects.

Findings need original requirements/standards or established behavior, reachable triggers, impact, code and reproduction/missing proof. A regression need not have an explicit Spec clause; missing proof must identify the promised boundary. Do not invent targets for gaps.

## 3. Standards Axis: Project Standards

Explicit project standards take precedence. Check evidence-backed naming, duplication, scattered responsibilities, unnecessary abstractions, and coupling. Read [quality heuristics](references/smells.md) when useful. Heuristics are judgments rather than hard rules; do not repeat style checks already enforced by tools.

Cite the standard for each finding or explicitly label it a judgment, explaining the actual impact. Do not block delivery on speculation unsupported by a contract, reproduction, or code.

## Task-specific Review Methods

Within this same review, read only the applicable methods: [Go review](references/go-review.md) for Go concurrency or resource changes, [silent failures](references/silent-failures.md) for error propagation or suspicious fallbacks, and [PostgreSQL review](references/postgres-review.md) for queries, schemas, transactions, or migrations. TypeScript error work uses only [error-handling](../error-handling/SKILL.md)'s TypeScript reference and silent-failure checks as needed; it does not trigger Go or unselected framework rules. For an explicitly requested output-quality assessment, use [output evaluation](references/output-evaluation.md); its five axes do not prove domain factual correctness or replace contract and boundary evidence. Actual LLM cost or cache questions use the conditional [task methods](../agent-workflow/references/task-methods.md).

These references are perspectives for the existing code-reviewer, not automatic agent dispatch, additional regular stages, or separate approval criteria. Findings retain the Spec and Standards axes and evidence/disposition rules of this skill; upstream style thresholds do not override project standards.

## 4. Output and Rereview

Report `Spec` and `Standards` separately as pass, blocked or indeterminate for this candidate. List main-agent closeout obligations separately. Each finding has a disposition:

- **Contract blocker**: a conflict, consequential gap, or need for a new product/architecture decision; the main agent refers it to the user.
- **Implementation defect**: violation of a settled requirement, a reachable regression, or missing evidence at a promised boundary for a required guarantee; the writer fixes and validates it.
- **Optional suggestion**: does not affect required contracts or acceptance and may be deferred.

Supply missing evidence when requested; the main agent adjudicates scope and disposition under agent-workflow. Keep its short rationale in the same record. In-scope gaps and evidence-backed defects remain blocking; outside-scope guarantees are extensions.

An axis cannot pass while relevant contract blockers or implementation defects remain unresolved. Passing with suggestions must not conceal missing required proof. Review approval does not replace main-agent synchronization, final mechanical checks, or publishing authorization.

Read artifacts and independently run focused checks for doubts under [validation responsibilities](../agent-workflow/references/execution.md#validation-responsibilities); explicit required checks apply. Generated-file checks go to the writer or isolation. Follow [context boundaries](../agent-workflow/references/execution.md#context-boundaries) for fresh first-review context and concise deltas. Source changes invalidate affected conclusions; retain old evidence labels and identify the new candidate before continuing.

For rereview by the same code-reviewer, read affected diffs, original findings, and new evidence, and assess related scope. For substantive contract changes, reread affected original text. Return concise findings or a pointer to a runtime-saved report; do not create a project report or second task ledger.

See [sources](../agent-workflow/references/sources.md).
