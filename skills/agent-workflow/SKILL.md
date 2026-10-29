---
name: agent-workflow
description: Execute approved Change materials through implementation, independent code-reviewer review, long-term document merging and final acceptance.
disable-model-invocation: true
license: MIT
---

# Agent Workflow

Execute the approved delivery without replanning settled decisions. The main agent owns coordination, user communication and acceptance; `implementer` owns assigned implementation and `code-reviewer` independently reviews it. Use those exact project role names. Discussion or editing this skill does not authorize team execution. Start subagents only when the user requests this team workflow/multiple agents or applicable project rules require delegation. Ordinary authorized small edits can proceed outside the team workflow; once entered, independent code-reviewer review is required.

## 1. Confirm the Execution Scope

Read the [document contract](../change-planning/references/document-contract.md), Change entry and applicable approved materials. Start with `change.md` for directory packages; legacy single-file Changes remain valid. Identify the target Spec or adopted target clauses, relevant PRD/Design, preserved current guarantees, actual approval and prerequisite availability. Read necessary original sources, not every document merely because it is in the directory.

The target Spec governs this delivery; the application Spec describes the current baseline. Their approved differences are intentional until delivered. Resolve consequential gaps through the response paths in [execution handoff](references/execution.md#issues-and-recovery); do not repeat a complete planning cycle or ask again about consistent existing approval.

Complete when scope, material authority, dependencies and authorized operations are clear.

## 2. Organize Implementation

Use [execution handoff](references/execution.md) for role handoffs, validation responsibility and recovery. Resolve original skill paths from the project collection; hand the implementer [tdd](../tdd/SKILL.md) and the code-reviewer [code-review](../code-review/SKILL.md). Each agent reads its rules and relevant contracts before work; unreadable required sources block the affected work. Preserve configured roles, models and permissions, using the runtime's supported agent controls.

Default to one implementer working through related tasks and one independent code-reviewer. Parallelize only when tasks can be independently implemented and verified within explicit write boundaries and there is a real benefit. Give parallel tasks exclusive ownership, isolate worktrees when needed, name an integration owner and honor dependencies. Each worktree has one writer at a time; explicitly hand back ownership before integration, main-agent edits or review. Use `oracle` only for a defined technical question, not as a routine stage.

The implementer completes approved tasks under TDD and returns task results, actual checks and unproven scope. Non-behavior tasks use appropriate fact checks. The main agent checks completeness and updates tasks in the Change entry from evidence; it does not duplicate the implementer's complete test run merely to screen the handoff. Continue the same agent with deltas where useful, using asynchronous notifications rather than repeated polling.

Complete when assigned results and required development evidence are available, integrated as needed, and write ownership has returned to the main agent. Unresolved gaps remain explicit.

## 3. Merge Affected Long-term Documents

Compare approved materials, current effective decisions and implementation/evidence. Apply [spec-writing](../spec-writing/SKILL.md), [design-writing](../design-writing/SKILL.md) and [prd-writing](../prd-writing/SKILL.md) only to documents actually affected. The document contract owns merge timing and archival; the writing skills own how content is merged. Update affected README operations where required.

Verify that the target, implementation, evidence and resulting current contract express the same delivery. Keep undelivered targets distinct and resolve overlap with intervening Changes. Partial delivery cannot become accepted by silently narrowing a contract. Ordinary implementation completion does not require a PRD completion entry.

This step normally precedes independent review so one review includes implementation and merged documents. Earlier implementation review is allowed when useful; send any subsequent document diffs to the same code-reviewer for focused review in §4. Do not edit a tree under active review.

Complete when required long-term content is faithfully merged and ready for review, or remaining merge obligations are explicitly assigned for the later focused review.

## 4. Independent Review and Repairs

Launch the `code-reviewer` with a stable candidate, fixed comparison baseline, complete delivery changes, approved target/current contracts and evidence as claims. Follow the handoff's [context boundaries](references/execution.md#context-boundaries) for fresh first-review context and read-only access. The code-review skill owns contract/standards judgments, finding evidence and disposition; this workflow owns routing and completion.

Send implementation defects to the implementer for repair and affected validation. The main agent resolves missing evidence and refers consequential product/contract/design changes under the document contract; local choices stay with the implementer. Reuse the code-reviewer for repair and later document diffs while retaining the original delivery scope. Recheck affected conclusions when inputs change, without restarting a full review solely for faithful document merging.

Continue while new evidence and a testable hypothesis support progress. When a dispute requires a user decision or repair has no viable next hypothesis, preserve the findings and report the specific blocker under execution handoff; no fixed round count decides this. Never downgrade a real defect because it is difficult to fix. If independent review cannot be established, report that gate unresolved rather than claiming it passed.

Complete when no relevant implementation defect, contract blocker or required evidence gap remains and the final long-term merge diffs have been reviewed. A code-reviewer conclusion is not acceptance or publishing authority.

## 5. Final Validation and Closeout

Run the delivery's required final validation under [validation responsibilities](references/execution.md#validation-responsibilities). Reuse adequate development/review evidence for what it proves; do not repeat full suites per role without a changed input, concrete doubt or explicit project requirement. Required checks retain their owner and scope; a failed or unavailable required check prevents acceptance.

Once delivered scope, review, required validation and document merging agree, complete the short delivery conclusion and archival under the document contract. Check affected references and final content, then report the final entry path, actual results, proof limits and remaining approved exceptions. Keep detailed logs and source identity in existing evidence, not new reports or the Change narrative.

Complete only after acceptance closeout succeeds. Local commits follow applicable policy; push, PR, deployment and destructive cleanup require their own authorization. Preserve evidence and in-progress work on failure; changing execution method after an agent/tool failure follows existing authorization, not an automatic fallback to self-implementation.

For optional maintenance walkthroughs and attribution, see [scenarios](references/scenarios.md) and [sources](references/sources.md); neither is a default execution prerequisite.
