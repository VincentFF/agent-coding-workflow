# Execution Handoff

This reference owns handoff, evidence and recovery details. The workflow owns progression; tdd, code-review and writing skills own their specialist methods. Use existing Change tasks and runtime handoffs rather than extra ledgers.

## Skill Paths

Resolve skill files from the actual project collection and supply readable absolute paths. An implementer receives tdd; a code-reviewer receives code-review and any writing-skill paths its assigned review requires. Agents read their role instructions and relevant original contracts. A name, summary or claim of loading is not a substitute for required text. On an unreadable source, report the path and block affected work; do not install tools or alter user role/model configuration as preflight.

## Context Boundaries

Continue the same implementer where useful and send incremental tasks/results. A new agent receives a focused handoff, with relevant prior investigation when it avoids rediscovery; scope and authorization remain unchanged.

The first `code-reviewer` starts without inherited parent conversation through the runtime's actual context controls and reads original contracts. Asking it to ignore inherited history is insufficient. Keep it read-only and the candidate stable; checks that write generated files belong to a writer or isolated environment. If required isolation is unavailable, report the review gate unresolved. Follow-up review retains the original baseline, scope and findings while receiving only new diffs/evidence.

## New Implementer

Provide only what the assigned task needs:

- Goal, completion conditions, dependencies and required validation.
- Repo/worktree, fixed delivery baseline, allowed write scope and current write owner.
- Change entry, applicable target Spec/PRD/Design and relevant current/source clauses, with approval basis.
- Absolute tdd path, necessary code pointers and existing evidence location.

Return implemented outcomes, changed scope, actual commands/results, proof limits and unresolved gaps. Detailed red/green evidence stays in runtime artifacts. Local choices are the implementer's; consequential contract changes return to the main agent.

## Code-reviewer

Provide the approved materials and preserved current guarantees, fixed comparison baseline, final candidate and complete changed scope (including commits, uncommitted changes and relevant untracked files). Include implementer evidence as claims, specific doubts and the absolute code-review path, plus conditional writing-skill paths. Identify target contracts versus final main-document merge diffs.

The code-reviewer returns findings with sources and evidence, separate Spec/Standards conclusions under code-review, and pending closeout obligations. Continuation sends affected diffs, original unresolved findings and new evidence; it does not erase the baseline-to-candidate review scope. Passing review does not establish main-agent acceptance.

## Validation Responsibilities

Assign required checks in the Change acceptance section and handoff. Explicit project and delivery commitments take precedence; each required check has an owner and result before acceptance.

| Role | Responsibility |
| --- | --- |
| implementer | TDD, affected-package/static checks and real-boundary proof required for task delivery |
| code-reviewer | Independently inspect contracts, complete changes and evidence; reproduce concrete doubts with focused checks rather than rerunning every suite by default |
| Main agent | Check handoff completeness and evidence applicability, perform the delivery's required final validation and closeout |

Evidence must answer: which candidate was checked, what actually ran and resulted, what it proves and what remains unproven. A fixed commit is adequate for a stable committed candidate; dirty trees need reliable content identity covering relevant untracked inputs. Reuse adequate existing runner/handoff records. Record dependent binaries, versions or external configuration when material; a source hash alone proves neither equivalent runtime inputs nor correct behavior. No snapshot per role or mandatory JSON report is required.

Changed implementation invalidates affected behavior checks and review. Changed tests/runners/dependencies/build/environment inputs require reassessing coverage and rerunning affected proof. Faithful document merging needs source/meaning comparison, affected-reference/patch inspection and focused review of final merge diffs; it does not require unrelated implementation reruns unless consumed inputs or semantics changed. With uncertain impact or doubtful evidence, expand validation to resolve the actual concern. Retained results keep their original candidate labels rather than pretending to be new runs.

Use an optional candidate-identity helper only if existing records cannot establish actual content identity/comparison; see [candidate evidence](candidate-evidence.md). This is not a default step or acceptance gate. No cap or quota reduces required checks, and no role repeats full validation solely to demonstrate activity.

## Issues and Recovery

| Issue | Main-agent action |
| --- | --- |
| Settled requirement violated | Send a defect to implementer; validate and review the repair |
| Product goal/scope/tradeoff is missing | Coordinate the necessary product clarification without reopening settled requirements |
| Target behavior is incomplete or conflicting | Coordinate the affected target Spec and required approval before dependent implementation |
| Consequential structure must change | Coordinate the affected design and required decision |
| Local implementation choice | Leave it with implementer |
| Delivery/acceptance scope changes | Revise the affected approved materials and confirm actual scope; never hide partial delivery |
| No useful next hypothesis, or a dispute needs a user decision | Preserve attempts/evidence and report the specific decision/blocker; new evidence may justify continuation |
| Agent, tool or isolation failure | Preserve work and partial results, report the failed action and use only recovery methods already authorized; no silent role/model/method substitution |

Do not infer failure from a healthy long-running check. Keep configured roles/models/permissions; publishing and destructive cleanup remain separately authorized. Preserve evidence through review, acceptance and recovery, and redact sensitive values.

A short recovery checkpoint is needed when replacing an agent, pausing, resuming interrupted work or integrating parallel work: record repo/worktree, ownership, completed/pending work, candidate/evidence, unresolved findings and next hypothesis/action. A replacement verifies the tree and ownership before writing. Normal continuation sends deltas, not a fresh full checkpoint each turn. Transfer write ownership explicitly; each worktree has one writer and no writer races a read-only review.
