---
name: change-planning
description: Organize a delivery goal, coordinate necessary PRD/Spec/Design work, and produce a Change package with tasks and acceptance for approval.
disable-model-invocation: true
license: MIT
---

# Change Planning

The main agent coordinates one assessable delivery. Read the [document contract](references/document-contract.md) for authority, package layout, approval and merge/archival rules. Discussion-only requests produce recommendations; create or revise files only within the user's authorization. Planning does not start implementation, subagents or publishing.

## 1. Define the Delivery

Read the relevant discussions, effective requirements, current contracts and affected code/tests. Reuse unchanged sources already read. Explain a concrete current problem, the result this delivery should provide, its non-goals and actual prerequisites. Investigate facts directly; ask the user only about consequential choices the sources cannot resolve. Do not treat current code as authority to weaken an approved promise.

Split only when there are independently assessable delivery goals, not merely multiple files, layers, tasks or sessions. Prefer complete behavior slices over database/API/UI Changes. If the granularity is already agreed, proceed; otherwise present the proposed scope with the complete materials for approval rather than requiring a separate split-approval round. Follow explicit project delivery sequencing.

Complete when the user can judge what this delivery achieves and why it is needed.

## 2. Resolve Gaps with the Writing Skills

Choose work from actual gaps; do not run a fixed three-document pipeline. Read and apply each selected skill's original instructions:

| Gap | Skill and output |
| --- | --- |
| Product goal, scope, rule or acceptance objective needs clarification/change | [prd-writing](../prd-writing/SKILL.md); optional package `prd.md`, or an authorized update to existing product materials |
| Target behavior needs precise inputs, outcomes, state, failures or compatibility | [spec-writing](../spec-writing/SKILL.md); package `spec.md` for the complete target contract of affected capabilities |
| Responsibilities, ownership, dependencies or technical mechanisms need design | [design-writing](../design-writing/SKILL.md); package `design.md` when substantive, otherwise a brief design decision in `change.md` |
| Existing agreement already answers the question | Reference it; do not generate a duplicate |

For behavior changes, prepare a target Spec or explicitly adopt adequate existing target clauses through the package's materials list. A missing current baseline may need separate clarification under spec-writing; future behavior never enters the application Spec as already delivered. Behavior-preserving refactors can cite existing contracts without a new Spec.

The main agent coordinates these steps. A technical result may expose a product choice, but revisit only that affected decision; writing skills do not automatically dispatch one another. Preserve confirmed decisions and important open questions in the owning material. Drafts may expose unresolved decisions; affected implementation cannot proceed until they are settled.

Complete when implementers need not invent consequential product behavior, persisted meaning or structural boundaries.

## 3. Plan Work and Acceptance

In `change.md`, summarize differences and preserved promises, then arrange tasks by verifiable result with real dependencies and completion conditions. Refer to detailed contracts/design rather than restating them. One Change owns each shared target; dependent Changes cite its contract and availability gate.

Fix a few consequential input/precondition and expected-result scenarios from the effective sources. Explain the check and its proof boundary, including relevant failures, resource limits, cancellation and compatibility. Transactions, process recovery, network protocols and similar promises need evidence at those real boundaries; fake success cannot establish them. Assign a missing test runner as delivery work instead of inventing a runnable command. Record actual available validation entry points and required project checks; execution roles and detailed evidence handling remain with [agent-workflow](../agent-workflow/SKILL.md).

Name the destination sections for long-term document merging. A task checklist is the progress ledger; the package is not a debug log. Keep detailed commands/results and review iterations in existing runtime artifacts, with only final conclusions and necessary evidence pointers in the Change.

Complete when the tasks cover the delivery promises and acceptance can reveal the important violations.

## 4. Assemble and Request Approval

Create the delivery directory under the document contract and use the [change.md outline](references/change-template.md). Create only materials the delivery needs. List which package files and existing source sections define the approval scope; detailed requirements belong in those materials, not repeated in the entry document.

Read the package as a whole. Trace a normal interaction and consequential failures; ensure goal, target contract, design, tasks and acceptance agree. Remove unrelated capabilities, duplicate definitions and speculative mechanisms. Confirm cited local sources and available commands exist, and repair affected references when moving files. Use simple patch checks such as `git diff --check`; no document-check script or report is required, and formatting cannot establish semantic completeness.

Present the goal, boundaries, material list, necessary decisions, acceptance and remaining gaps. Record approval only from actual authorization for that scope. Approval covers the listed materials together, not hidden attachments. Existing approval remains valid for faithful restatement; consequential changes require confirmation of the affected content under the document contract. Return the entry path and readiness status. Approval does not independently authorize team execution or publishing.

Complete when the user can identify exactly what is being approved and the execution workflow can take over the package.
