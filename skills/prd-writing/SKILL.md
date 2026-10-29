---
name: prd-writing
description: Form and maintain product requirements. Use when creating a PRD, changing product scope or rules, synchronizing/reorganizing requirements, or reviewing PRD changes; planning, design and review workflows call this entry point when product decisions need work.
license: MIT
---

# PRD Writing

Clarify whose problem the product solves, what outcomes and rules it should provide, and how to judge delivery and value. Choose formation, adjustment, synchronization/reorganization, or read-only review from the request. The [document contract](../change-planning/references/document-contract.md) owns approvals, write ownership and acceptance. Discussion and review return findings; creating a PRD does not authorize implementation or delegation.

## 1. Establish the Problem and Evidence

Read relevant discussions, project rules, PRDs, Specs and Changes, plus implementation or operating evidence needed to establish facts. Reuse unchanged sources already read. Distinguish observed facts, confirmed decisions, assumptions to validate and product choices still open. Code is evidence of current behavior, not proof that the behavior meets a product need.

Start with a concrete situation: who encounters what difficulty, under which conditions, and why it matters. For example, an on-call engineer receives a threshold alert but must open several metrics/log pages before choosing the next investigation step. Use sources actually available; do not invent interviews, adoption figures, benefits, research or target metrics to complete a template.

Identify the document's scope: long-term direction, the current agreed release, or a particular capability. A PRD may describe undelivered requirements. Requirement agreement, implementation and demonstrated value are different facts; identify them through appropriate evidence and links, not a second task-status ledger. Preserve the project's separately maintained management-facing progress tables.

Complete this step when the affected user/system participant, problem, impact and evidence are clear, or missing evidence is explicitly an assumption.

## 2. Define Goals, Scope and Product Rules

For formation, establish the smallest scope that addresses the problem. For adjustment, identify requirements added, narrowed, deferred, cancelled or replaced, and the scenarios and promises affected. For reorganization, preserve existing decisions and repair references without inventing product changes. For review, keep the tree unchanged and assess the affected requirements using §5.

Describe the intended outcome, in-scope capabilities and explicit non-goals, main participants and scenarios, important exceptional outcomes, real dependencies and unresolved decisions. Existing agreed requirements remain effective; do not reopen them or reduce them to match an implementation shortcut.

Retain concrete product choices when they determine the result. “Pure recovery does not start diagnosis” and “allow repeat delivery when receipt is uncertain” are meaningful product rules. Detailed database fields, HTTP error codes and internal components normally belong elsewhere. An explicitly mandated technical constraint can be cited as a requirement without expanding it into an architecture proposal.

For unresolved consequential product choices needing a focused interview, read and apply [grilling](../grilling/SKILL.md). Investigate verifiable facts directly and reuse settled answers; ordinary wording work does not trigger an interview.

Read existing Design and Spec documents as evidence and link to their authoritative detail. If a technical unknown affects whether a requirement can hold, identify the fact or design question for the main agent to investigate or arrange separately. Product meanings and tradeoffs remain product decisions. The main agent or calling workflow coordinates authorized Design/Spec work; PRD writing does not automatically invoke their writing skills or modify those documents. Requirement approval alone does not establish delivered behavior.

Complete this step when design can proceed without inventing consequential product behavior, or the draft explicitly identifies decisions preventing that part from proceeding. A valid draft may contain open choices; it is not implementation approval.

## 3. Define Acceptance and Value Assessment

Separate two questions:

| Question | What to record |
| --- | --- |
| Does delivery meet the agreed requirement? | Observable result for representative inputs/preconditions, including important failure or fallback cases |
| Does the product address the original problem? | Evidence and evaluation method for usefulness, quality, cost or effect; distinguish hypotheses from demonstrated outcomes |

For example, a failed diagnosis still producing a useful failure notice is a delivery condition; whether the notice helps an engineer choose the next step is value assessment. Use confirmed thresholds when available. Otherwise representative cases and explicit human assessment are valid; do not invent numeric targets or claim measurements already exist.

State material proof limits: production behavior, external channels or an observation period may need different evidence from a local demonstration. PRD holds product acceptance objectives; the owning Change holds delivery-level validation matrices, commands and executed results. Link existing sources instead of creating another test ledger.

Complete this step when each main goal has a way to judge it and the text distinguishes functional completion from demonstrated value.

## 4. Write the Product Document

Use the project's language and an adaptable shape. Omit irrelevant sections, combine small topics, and preserve useful existing identifiers and links. No fixed user-story format, requirement count, metric quota or new numbering scheme is required.

```markdown
# <产品或能力> 产品需求

<文档范围：长期方向、本期范围或某项能力；相关文档入口>

## 问题与目标
<谁遇到什么问题、依据是什么、希望改善什么>

## 用户与关键场景
<参与者、触发条件、主要过程和期望结果>

## 范围与非目标
<本期包含与排除什么；和长期方向的关系>

## 产品要求与规则
<必要能力、用户可见结果、重要异常处理和产品取舍>

## 验收与价值评估
<交付通过条件与实际效果的判断方法>

## 依赖与待定事项
<实际外部依赖、重要假设和尚待裁定的选择>
```

PRD retains goals and important product rules even after delivery. Link detailed effective inputs/outputs, API schemas, errors and interaction behavior to Spec; structure and mechanisms to Design; operations to README; delivery differences, tasks, approval history and execution evidence to Change. Important recorded rationale follows existing ADR ownership. A PRD should guide design, not become either an implementation manual or a directory containing only links.

A Change may contain an optional `prd.md` for new or adjusted product requirements. Follow the document contract's material-set approval and merge timing: after product decisions are confirmed, merge authorized changes into the owning long-term PRD while keeping undelivered requirements distinct. Preserve the archived companion as historical material, not another continuously maintained PRD.

Use the existing overall PRD for long-term direction and release PRD for agreed release scope. Keep scheduling and management progress in the project's development plan. Link actual delivery status instead of adding another status table to each PRD; completed implementation alone is not a reason to append a completion entry or rewrite the product goal.

Complete this step when the reader can understand the problem, scope, requirements and judgment criteria without reconstructing delivery history or choosing between duplicate normative copies.

## 5. Merge and Review

Replace affected requirements and merge related conditions in their owning sections. Scope reductions, deferrals and cancellations must reach the main flow, scenarios, exceptions and acceptance objectives that rely on them. Preserve valid guarantees, source links, important rationale and historical records. A note at the bottom does not supersede conflicting requirements above it.

For example, deferring deduplication requires reviewing repeat-alert scenarios, expected messages and acceptance goals, not merely adding “deduplication is deferred.” Update only affected material; keep unresolved product decisions out of claimed agreements.

Read the complete affected requirement area and check:

- Each requirement follows an actual problem, confirmed decision or explicitly identified hypothesis; claimed observations and benefits have evidence.
- Scope, scenarios, product rules, dependencies and acceptance objectives agree, including important failures and excluded cases.
- Proposed, agreed, implemented and evaluated claims are distinguishable; implementation facts have not silently become product approval.
- The document has enough substance to guide design, without duplicating detailed Spec/Design/operating content or adding unrequested capabilities.

Use existing link/patch checks; they do not establish requirement correctness. In team execution, the existing independent code-reviewer inspects changed PRD content; later PRD synchronization returns to the same code-reviewer for focused review. Ordinary PRD work does not automatically start a team. Approval and scope changes follow the document contract; faithful organization and synchronization do not add an approval stage.

Complete when the affected product requirements are coherent and consequential gaps are explicit. Return scope changes or preservation, sources, unresolved decisions and actual checks in the existing response/handoff. No extra report, generator, keyword lint or mandatory scoring is needed.
