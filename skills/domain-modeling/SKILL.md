---
name: domain-modeling
description: Clarify project-specific concepts and consequential decisions with terminology and ADR methods for terminology conflicts, domain relationship discussions, or ADR creation and revision.
license: MIT
---

# Domain Modeling

Align concepts and record consequential decisions. A Glossary is not a container for Spec, Design, or tasks. Merely using existing terminology does not require starting a modeling process.

This is the domain/decision specialist selected by [design-writing](../design-writing/SKILL.md). That entry point owns design routing and document maintenance; this skill owns concept clarification and Glossary/ADR methods. Explicit standalone modeling or ADR requests may use this skill directly.

## Clarify Concepts

Read the relevant Glossary. If GLOSSARY-MAP exists, follow only the relevant context. Continue normally when files are absent; do not require directories or files in advance.

When user terminology conflicts with existing definitions, explain the different meanings. For vague names, propose precise candidates and test concepts, relationships, and ownership against concrete scenarios. Use code to verify current facts. If they disagree with the target, raise the conflict instead of automatically choosing either side.

After canonical names are confirmed, record them briefly using the [Glossary format](references/glossary-format.md). Include only project-specific concepts, not ordinary programming terms, implementation steps, or configuration inventories.

## ADR Candidates

By default, propose an ADR only for an actual decision with all these properties: difficult to reverse, confusing to future readers without context, and made after considering reasonable alternatives. Follow project rules for mandatory decision records; do not create ADRs for other implementation details merely to increase their number.

Context, decision, and rationale usually fit in one paragraph. Use the [ADR format](references/adr-format.md) to add genuinely useful alternatives, non-obvious consequences, or supersession relationships. When reopening an existing ADR, state the conflict and obtain approval for the replacement under the document contract; reuse a replacement decision already approved. Preserve the original rationale.

## Write Responsibilities

For discussion-only requests, return recommendations without automatically writing long-term documents. During change-planning, record confirmed terminology changes and ADR candidates in the Change. During agent-workflow closeout, the main agent persists delivered changes under the [document contract](../change-planning/references/document-contract.md).

When the user explicitly requests standalone Glossary/ADR creation or revision, the main agent may write within the authorized scope, recording only actual agreement. Approval of a technical decision does not mean its capability has been delivered; do not misrepresent it as implemented in the current Design.

Implementers/code-reviewers may read this reference without gaining permission to edit contracts or long-term documents. See [sources](../agent-workflow/references/sources.md).
