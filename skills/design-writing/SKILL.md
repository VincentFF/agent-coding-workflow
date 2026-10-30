---
name: design-writing
description: Design technical solutions and maintain Design documents. Use when forming or adjusting a technical design, synchronizing delivered structure, or reorganizing/reviewing a Design; planning, execution and review workflows call this entry point, which conditionally uses domain-modeling and codebase-design.
license: MIT
---

# Design Writing

Use this entry point to identify design work, invoke the necessary specialist skills, and record a coherent design. The [document contract](../change-planning/references/document-contract.md) owns approvals, write ownership and acceptance. Discussion and read-only review produce recommendations; writing a design does not authorize implementation or delegation.

## 1. Establish Scope and Document Purpose

Read the relevant project rules, PRD, Spec, Change, Design and ADRs, then inspect affected code, callers and evidence. Reuse unchanged sources already read. Start with a concrete problem or interaction; distinguish effective constraints, agreed targets, implementation facts and unresolved choices. Code does not automatically supersede an approved decision.

Choose the branch:

- **Form a solution:** Identify decisions needed to meet confirmed requirements; analyze only the affected capability.
- **Adjust a design:** Identify responsibilities, relationships, data or dependencies that change, and constraints that remain effective.
- **Synchronize or reorganize:** Record delivered structure or reorganize existing agreement, preserving semantics and repairing references. Documentation cleanup alone does not require redesign.
- **Review:** Inspect the design and its sources read-only using §5; analyze a specific doubt with the specialists below when needed.

Identify the document's purpose before editing:

| Purpose | Treatment |
| --- | --- |
| Current design | Describe delivered structure and implementation mechanisms |
| Target architecture | Describe the agreed direction; distinguish delivered and undelivered areas in sections or diagrams |
| Delivery-specific target | Use the Change's `design.md` for substantive technical design; brief choices can remain in `change.md`. Tasks and acceptance remain in the entry. |

A document may contain current and target architecture if readers can distinguish them. A short scope statement or clearly separated sections is enough; no per-sentence status labels or second progress ledger is needed. Existing target architecture is not permission to implement later capabilities. Merge confirmed direction into identified target architecture only within authorization, and delivered structure into current Design after implementation. The Change companion remains historical after archival rather than a second continuously maintained Design.

Complete this step when the problem, affected area, effective sources and current/target boundary are clear. If analysis exposes an unresolved product goal, scope or tradeoff, report it to the main agent rather than choosing product behavior through a technical shortcut. The main agent or calling workflow coordinates any separate product requirement work. For assigned feasibility analysis, return findings within that assignment; technical conclusions do not establish product approval. Resolve consequential conflicts under the document contract.

## 2. Invoke Specialists by Need

Read and apply the original skill at the following boundary; a link or skill name is not a substitute for its instructions. Keep findings within the selected branch and authorization.

| Design question | Specialist |
| --- | --- |
| Conflicting terminology, unclear objects, identity, relationships or lifecycle meaning | [domain-modeling](../domain-modeling/SKILL.md) |
| Module responsibilities, state ownership, interfaces, dependency direction or replacement/test boundaries need design | [codebase-design](../codebase-design/SKILL.md) |
| Both semantic and structural questions | Clarify domain meaning first, then design structure; revisit either only when new evidence requires it |
| A consequential decision needs rationale or supersedes an ADR | domain-modeling's ADR method |
| Existing terminology, established structure, faithful synchronization or diagram/link correction | Work directly; no specialist is required merely to restate an agreement |

For concrete implementation constraints, conditionally read [golang-patterns](../golang-patterns/SKILL.md) for Go interfaces, concurrency, and resources; [error-handling](../error-handling/SKILL.md)'s matching language reference for failure boundaries; and [postgres-patterns](../postgres-patterns/SKILL.md) plus [database-migrations](../database-migrations/SKILL.md) for persistence and migration questions, respecting the project's existing migration tools and deployment contracts. Only an actual LLM cost, budget, or prompt-cache question selects [cost-aware-llm-pipeline](../cost-aware-llm-pipeline/SKILL.md) or [prompt-caching-strategy](../prompt-caching-strategy/SKILL.md); reading them does not authorize unapproved model routing, layered retries, circuit breakers, or new infrastructure. These are analysis methods for the current role, not automatic delegation.

Each specialist owns its analysis methods; do not copy them here or routinely load both. Explicit standalone specialist requests remain valid. Respect confirmed decisions; ask only about consequential new or changed choices, not already approved boundaries or private implementation details.

Complete this step when concepts and structural choices necessary for the affected scope are settled, or remaining decisions are explicitly located in the proposal/Change.

## 3. Form the Smallest Complete Design

Describe the responsibilities and exclusions, data/state owners, allowed dependencies and key internal interactions needed for the current goal. Trace a normal path and consequential failures, assigning side effects, persistence, cancellation, timeouts and retries to owners where relevant. Explain migration, compatibility and rollback when existing users or data are affected.

Use the specialist results rather than repeating their full analysis. Compare alternatives only when a real tradeoff affects the decision. Match detail to the document purpose: target architecture may show future components, while delivery-level tables, interfaces and mechanisms belong to the current Change. Build abstractions, configuration and storage only for actual requirements or concrete isolation needs.

Complete this step when the main interaction and important failure paths have clear owners, without requiring an implementer to invent consequential structure. Unresolved decisions can remain in a discussion draft but prevent approval of the affected implementation.

## 4. Record in the Owning Document

Design owns structure and implementation mechanisms. Current external inputs/outputs, API paths/schemas, errors, UI behavior and compatibility promises belong to Spec under [spec-writing](../spec-writing/SKILL.md). Design may define internal responsibilities, call ordering, types and transaction boundaries, linking to the external contract it implements. Product goals remain in PRD, operational recipes in README, delivery differences in Change, and consequential rationale in ADR.

Domain conclusions go to their actual owner; use existing terminology locations rather than creating a Glossary solely for this skill. Preserve approved constraints when moving content and leave links instead of competing definitions. Follow explicit project ownership; surface unresolved conflicts instead of silently moving authority.

Use this adaptable shape; omit irrelevant sections, merge small topics and use diagrams only when they clarify interactions. No fixed section, diagram, alternative or ADR count is required.

```markdown
# <应用或能力> 设计

<文档范围、现状与目标边界、相关契约入口>

## 问题与设计依据
<具体问题、必要约束、已确认需求>

## 结构与职责
<模块职责与依赖方向；必要时配图>

## 数据与状态所有权
<对象关系、存储归属和状态修改责任>

## 关键交互
<主要调用链、内部接口和关键失败路径>

## 可靠性与兼容
<按需说明资源、取消、恢复、迁移和回退机制>

## 重要决定
<决定摘要和 ADR 链接>
```

Use the project's document language. Record the design, not a chronological account of how the team reached it. Return recommendations for discussion requests; write only the authorized documents. Completion means each conclusion has an owner and readers can distinguish implemented structure from agreed direction without reconstructing delivery history.

## 5. Merge and Review

For changes, identify structures added, replaced and removed; update the owning sections and diagrams together. Remove stale proposals from current descriptions, preserve original ADR rationale and historical Changes, and repair affected references. Cancellation or deferral must also reach target diagrams and descriptions; approval alone never marks a component delivered.

Read the complete affected area and check:

- Decisions follow effective requirements and preserved constraints; normal/failure paths have consistent responsibilities, state owners and dependencies.
- Text, diagrams, internal interfaces and data relationships agree; implementation claims have evidence, and undelivered targets are distinguishable.
- Alternatives and mechanisms serve the problem; no extra capability or externally visible promise has appeared through documentation.
- Removed/replaced structure is reflected throughout the affected area; Spec, Design, ADR and operational content each retain one owner.

Use existing link/patch checks, which do not establish semantic correctness. In team execution, include the final Design diff in the existing independent review; send later design synchronization to the same code-reviewer for focused review, without repeating the complete implementation review. Ordinary authorized document work does not start a team automatically. Approval of new semantics follows the document contract; faithful synchronization needs no renewed product approval.

Complete when the affected design is coherent and known gaps are explicit. Return changed sections, retained/current versus target scope, decisions needing resolution and actual checks in the existing response/handoff. No new script, report, approval stage or task ledger is required.
