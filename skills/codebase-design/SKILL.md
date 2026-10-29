---
name: codebase-design
description: Design module responsibilities, public interfaces, dependencies, and test boundaries for consequential structural changes or planning that needs explicit module and interface contracts.
license: MIT
---

# Codebase Design

Encapsulate useful behavior behind small, clear interfaces so knowledge, changes, and validation stay localized. Prefer the project's existing domain language and structural constraints; do not turn reference vocabulary into mandatory renaming rules.

This is the structural-analysis specialist selected by [design-writing](../design-writing/SKILL.md), which owns design routing, document format, synchronization and review. Explicit standalone structural-analysis requests may use this skill directly.

## Shared Vocabulary

| Concept | Meaning |
| --- | --- |
| Module | An encapsulated responsibility with an interface and implementation, such as a function, package, or complete behavior unit; not necessarily a file |
| Interface | The complete contract callers need to know: inputs, outputs, constraints, ordering, errors, configuration, and important performance properties, beyond type signatures |
| Implementation | Internal structure behind an interface |
| Seam | A place where behavior can be replaced or verified; identify the concrete test interface in the current plan to avoid ambiguity |
| Adapter | A concrete implementation satisfying the interface at that seam |
| Depth | Behavioral capability available after callers learn a small interface, rather than implementation line count |
| Locality | Related changes, problems, and validation concentrated within a clear responsibility |

## Reach Design Agreement

1. Read relevant current Design, ADRs, code, and callers. Identify responsibilities to change and constraints to retain. Inspect the affected area rather than auditing the entire repository's architecture by default.
2. State what each module owns and excludes, who owns data and state, and which dependencies are allowed or forbidden. Choose available static checks for mechanical dependency constraints; leave responsibility assessment to independent review.
3. Describe key interfaces, errors, ordering, and side effects. Test through existing interfaces that expose the complete target behavior. Do not expose private state or invent extensive abstractions for testing.
4. Record necessary key interactions and failure handling. Use brief input/output, state-machine, or type snippets when more precise than prose; do not copy demonstrations or full file trees.
5. Propose design differences and tradeoffs. Refer consequential new or changed boundaries under the [document contract](../change-planning/references/document-contract.md); reuse existing approval without asking again. Private functions and local algorithms remain implementation choices. Reading this reference does not authorize an implementer to redraw approved modules or shared interfaces.

## Structural Judgment

- Minimize callers' need to know internal details. Modules own complete behavior instead of scattering coordination complexity across callers.
- If removing a wrapper eliminates complexity, it may merely forward calls. If complexity spreads into callers, it provided real encapsulation. Do not delete layers automatically based on pattern names.
- Add abstractions only for real variants, necessary isolation, or explicit boundary constraints. Production and test adapters can establish a genuine need; do not add ports for imagined future capabilities.
- Inject dependencies at system boundaries; avoid constructing irreplaceable clients inside business logic. Prefer returning results from pure computation and concentrate necessary side effects under explicit owners.

For dependency isolation or merging shallow modules, read [dependencies and testing](references/dependencies.md). When the user needs comparison of substantially different interfaces, read [alternative comparison](references/alternatives.md); do not start multiple agents by default.

Return structural findings to the calling design-writing step without restarting it. For standalone work that needs document creation or synchronization, use [design-writing](../design-writing/SKILL.md)'s document steps under the document contract. See [sources](../agent-workflow/references/sources.md).
