---
name: spec-writing
description: Write behavior contracts. Use when drafting a Change target Spec, creating a missing current baseline, merging delivered targets into the application Spec, reorganizing a Spec, or reviewing contract changes; planning, execution and review coordinate these operations.
license: MIT
---

# Spec Writing

Write a coherent behavior contract by capability, distinguishing the Change's target Spec from the application's current Spec. Choose target drafting, baseline creation, delivered-target merge, reorganization or read-only review from the request. This skill owns Spec content and format; the [document contract](../change-planning/references/document-contract.md) owns location, approval, write ownership and lifecycle. Discussion and review requests produce findings only.

## 1. Establish the Effective Contract

Read project instructions, the affected Spec sections, effective requirements and Changes, and relevant implementation/tests. Locate the project's document owners before editing; reuse unchanged sources already read. Treat code as evidence of behavior, not authority to weaken an approved promise. Resolve consequential conflicts under the document contract.

Determine which branch applies:

- **Target:** In the Change's `spec.md`, write the complete target contract for affected capabilities: input/output, state, failures, limits and compatibility. Name the current baseline and affected application sections. Link unaffected capabilities instead of copying the whole main Spec. Summarize additions, replacements and removals in `change.md`; the target text is readable on its own, not a list of editing instructions. Approval makes it an implementation/acceptance contract, not delivered behavior.
- **Create:** A current behavior baseline is missing. Establish only the affected capability, supported by effective decisions and observed behavior. Keep unresolved choices in the planning discussion or target Spec; never promote future behavior into the current baseline.
- **Update or merge:** After implementation and appropriate validation, semantically merge delivered targets into the application Spec. A bug fix restoring an already documented promise usually needs no main Spec change; a newly exposed important boundary may need clarification. Internal refactors alone do not generate entries.
- **Reorganize:** Preserve every effective promise while merging duplicates, separating topics, and repairing inbound references. Do not infer new semantics from current code or discard compatibility limits as historical clutter.
- **Review:** For a target, assess decisions, completeness and consistency without claiming implementation; for a delivered merge, also compare implementation/evidence and preserved current rules. Keep the tree unchanged.

This step is complete when the affected capability, effective sources, and current versus proposed behavior are distinguishable. Report unknowns rather than turning them into assertions.

## 2. Select Content and Its Owner

Include a statement when a caller, user, operator, or future maintainer needs it to judge correct behavior, compatibility, or reliability.

| Content | Owning document |
| --- | --- |
| Input/output, API paths and schemas, errors, UI behavior, persisted meaning, retry and duplicate semantics | Application Spec for current behavior; Change Spec for the scoped target |
| Resource limits, configuration semantics, startup/readiness/shutdown/recovery and compatibility guarantees | Current or target Spec according to effect |
| Product purpose, scope decisions, value assessment, future requirements | PRD |
| Modules, dependencies, libraries, internal algorithms and implementation mechanisms | Design |
| Installation, command recipes, deployment steps and troubleshooting procedures | README or runbook |
| Delivery differences, approval history, tasks, executed checks and acceptance evidence | Change |
| Reasons, alternatives and consequences of consequential decisions | ADR |

Follow explicit project ownership where it differs; refer unresolved overlaps to the main agent rather than silently moving authority. Product documents may explain user intent and link to detailed effective behavior. Move an existing fact with its meaning and necessary inbound links, leaving a pointer instead of a second normative copy.

Keep observable guarantees even when they involve technical boundaries. For example, “reading and export must not exhaust reception capacity” belongs in Spec; the number and type of database pools belong in Design. A migration compatibility restriction belongs in Spec; Atlas invocation commands belong in README. Safety and data-integrity constraints remain even when they make the document longer.

This step is complete when each retained rule has a clear purpose and an owner. References to evidence need not become a per-sentence provenance table.

## 3. Write by Capability

Use this lightweight shape, adapted to the existing document. Omit irrelevant sections and keep small capabilities together; there is no required section count, word count, or separate file per interface.

```markdown
# <应用或能力> 行为契约

<说明当前或本次目标、受影响范围和基线；目标 Spec 链接 change.md 与合并目的章节。>

## <能力，例如通知接收>

### 输入与前置条件
<Interface, authentication, required/optional input and validation that affects behavior.>

### 结果与状态
<Success output, persisted effects, invariants, duplicates and retries as applicable.>

### 失败与限制
<Error outputs, state retained on failure, relevant resource and compatibility boundaries.>

### 关键场景
<Only the examples needed to explain interactions among the rules above.>

## 配置与生命周期
<Include when startup, readiness, shutdown or recovery has its own effective contract.>
```

Organize headings around the questions readers need to answer, not delivery dates, task IDs, or source packages. Split a paragraph when it mixes unrelated promises. Use tables for enumerable errors, configuration rules or state transitions; use prose for connected explanations. Express the condition, observable outcome and retained state precisely where they affect correctness.

Keep a few representative scenarios for complex behavior, reusing approved examples. For example: firing creates R1/J1; the same body received again creates R2/J2; a later pure resolved notification creates R3 without changing J1/J2. The scenario illustrates the rules rather than maintaining a second acceptance matrix. If no example adds meaning, omit it.

Write in the project's language with stable references. Make current versus target effect explicit, without chronological narratives; review results and history stay in Change. Current behavior must be understandable without archived Changes, and a target capability must be understandable without reconstructing a patch instruction list.

## 4. Merge the Current Contract

For a delivered merge, compare the approved target, latest application Spec and implementation/evidence. Recheck intervening Changes affecting the same capability; resolve semantic conflicts rather than overwriting newer guarantees. Replace superseded rules and merge additions with existing conditions. Remove obsolete claims and duplicates within scope; do not append the target file or blindly replace the whole application Spec. Undelivered clauses stay out of current behavior; incomplete approved scope needs an explicit decision before acceptance. Preserve the archived target as historical approval/acceptance evidence, not a second ongoing main Spec.

For ordinary updates, use the same replacement/merge method. A cancellation or deferral updates the application Spec only if it changes effective behavior or corrects a false delivery claim; update the owning target material for undelivered plans.

Read the complete affected capability after editing, including its errors, limits and lifecycle links. Verify preserved guarantees as well as new outcomes. Keep changes local unless nearby repetition or organization prevents a coherent contract. Match evidence to the claim: a fake Store cannot establish transaction durability, and one captured sample cannot establish the whole input protocol.

Complete the edit only when a reader can determine the behavior without guessing among conflicting paragraphs or duplicate authorities. Return the affected sections, semantic changes or preservation, source/evidence pointers and unresolved gaps concisely in the existing handoff or response. No new report, approval stage, keyword lint, or generated ledger is required.

## 5. Review the Final Spec Diff

For read-only review and author self-check, read the changed capability as a whole and check:

- Every added or changed promise follows an effective decision; current/delivered claims have appropriate evidence, and target claims remain identified as targets. Implementation detail has not silently become a contract.
- Old guarantees, important failures, data invariants and compatibility limits survive unless their change was approved; removed and replaced rules agree with the final text.
- Interfaces, state changes and representative scenarios agree; a delivered merge also agrees with implementation/evidence. Important gaps are identified without inventing extra requirements.
- Each fact has an owner; the text can be navigated by capability without delivery history or unnecessary cross-document round trips.

Use existing document/patch checks for links and formatting. These checks do not establish semantic correctness. In team execution, the existing independent code-reviewer inspects the final Spec diff; if synchronization follows implementation review, send that diff to the same code-reviewer for focused review. New semantics follow the document contract's approval rules; faithful synchronization does not require renewed product approval.
