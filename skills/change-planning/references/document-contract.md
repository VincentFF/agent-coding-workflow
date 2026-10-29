# Document Contract

## Document Responsibilities

Use existing project locations. The writing skills own content and format; this contract owns authority, approval, lifecycle and delivery material relationships.

| Document | Owner and role |
| --- | --- |
| PRD | [prd-writing](../../prd-writing/SKILL.md): product goals, scope, rules and acceptance objectives, including explicitly undelivered requirements |
| Spec | [spec-writing](../../spec-writing/SKILL.md): application current behavior or a Change's target behavior, with scope and effect distinguished |
| Design | [design-writing](../../design-writing/SKILL.md): delivered structure or clearly identified target architecture and delivery design |
| ADR | Consequential rationale, alternatives and consequences under domain-modeling, reached through design-writing for design work |
| Change | change-planning: delivery goal, approved materials, tasks, acceptance, merge destinations and final conclusion |

Keep one normative definition for each fact at the relevant scope. Link existing effective materials rather than creating agent-only copies. Application Spec records delivered behavior; a target Spec is not a claim of delivery. Product agreement, implemented capability and demonstrated value remain distinct. Preserve historical approval evidence and ADR rationale.

## Sources and Authority

1. Identify project rules, effective decisions and current contracts. Names, dates, implementation and a file's status alone do not prove authority.
2. Explicit differences in an approved Change material set govern its delivery scope; unchanged current contracts remain effective. One Change owns an undelivered shared target, and dependent Changes reference that owner and its availability gate.
3. `change.md` lists applicable companion files and precise existing source sections. Approval covers that material set, including requirements, target behavior, necessary design constraints and acceptance, rather than the entry file alone. Do not hide decisions in unlisted attachments.
4. Ask the user to resolve consequential gaps/conflicts or approve changed product rules, behavior, structural constraints or validation commitments. Local implementation choices remain with the implementer. Faithful reorganization, synchronization and progress/evidence updates do not require renewed approval.
5. Writing a proposal, approving its contract, authorizing delegation and publishing are separate actions. Reuse actual existing authorization; do not invent evidence or repeat approvals already granted for the same scope.
6. Archived Changes preserve their approved delivery history; they do not override later current contracts. Read original material for consequential constraints; summaries and links are an index, not substitutes.

## Change States and Progress

| State | Meaning |
| --- | --- |
| draft | The material set is not approved for implementation, or consequential revisions remain unapproved |
| approved | Actual user authorization covers the listed materials and permits implementation within scope |
| accepted | Delivery, required review/validation, long-term merging and archival closeout are complete |

State and approval evidence live only in `change.md`, maintained by the main agent. Companion files share that lifecycle, not independent approval statuses. Identify unresolved choices and pause affected work; never silently shrink approved scope or describe partial delivery as completion. Explicitly cancelled legacy Changes retain their cancellation record; cancellation is not acceptance.

Tasks in the entry file are the authoritative progress ledger unless the project already has one elsewhere. The main agent updates them from evidence and write ownership. Keep detailed execution/review iterations in runtime artifacts; the entry retains a short final conclusion, exceptions and pointers. Preserve the project's management-facing progress summary without duplicating task truth. Dependent work starts only after its agreed availability gate.

## Change Naming and Archival

New nontrivial deliveries use `docs/changes/YYYY-MM-DD-<topic>/change.md`, with the local creation date and a short English hyphenated topic. Revisions, approval and acceptance retain that identity. Ordinary local mechanical edits need no Change. Existing `YYYY-MM-DD-<topic>.md` Changes remain valid and are not migrated solely for format consistency.

```text
docs/changes/YYYY-MM-DD-<topic>/
  change.md     # delivery entry
  spec.md       # target contract when behavior changes
  prd.md        # optional product requirements/change
  design.md     # optional substantial technical design
```

The entry may adopt already adequate target clauses from existing sources instead of generating a duplicate Spec; explicitly identify the adopted sections. Behavior-preserving refactors need no new Spec. Small technical choices can remain in the entry; substantive design belongs in its companion. No file is required merely to complete the tree.

Active draft/approved packages stay in `docs/changes/`; accepted packages move as a unit to `docs/changes/archive/`, retaining names, approval scope, target materials and concise results. Legacy files move individually under their established identity. On collision, stop; never overwrite or leave active/archive duplicates.

### Archival Closeout

After delivery gates and required human decisions pass, the main agent completes closeout without a separate archival permission request:

1. Confirm no implementer/code-reviewer still uses the location and the archive destination is absent. Complete the long-term merges below and obtain required review on their final diffs.
2. Record the final result and acceptance, move the whole package (or legacy original file), and repair internal relative links, inbound links and operational pointers. Historical commands may retain former paths when identified as historical.
3. Inspect the final material set for preserved content, unique active/archive location, correct state/date, usable references and patch formatting. Cancelled, deferred or replaced plans must also be corrected in the owning current/target descriptions and diagrams, without rewriting historical rationale.

If closeout fails, preserve all content and do not claim accepted. Restore the active approved location/state and references when possible; otherwise report the actual location and blocker. Do not move an already successfully archived Change again. There is no required document-check script or JSON report; semantic consistency and actual delivery evidence determine completion.

## Minimal Change Format

Use the [entry outline](change-template.md) for the delivery plan. Requirements and detailed behavior/design go in listed companions or effective existing sources rather than repeated in the entry. Make tasks verifiable outcomes with dependencies and completion conditions; acceptance connects consequential inputs, expected results and proof boundaries to those outcomes. Extra matrices, reports and numbering are not mandatory.

## Acceptance Basis

Before nontrivial implementation, fix key inputs/preconditions and expected observations from approved sources in the entry's acceptance section or referenced Spec scenarios/fixtures. Consider relevant failure, resource, cancellation, readiness and compatibility boundaries without inventing extra requirements. Main-agent coverage checks and code review inspect original sources, not just a mapping.

Separate expected meaning from runner setup. Assign missing runners to delivery tasks and prove they execute. Runner/fixture repair may preserve the approved expectation; changed semantics return to the main agent. Code-reviewers inspect expectations and actual proof boundaries even when code/tests pass together. Documentation-only work uses direct source/fact comparison and checks affected references; command success or an unchanged hash does not prove semantic completeness. Execution ownership and evidence procedures live in [execution handoff](../../agent-workflow/references/execution.md#validation-responsibilities).

## Main Agent Synchronization Rules

The entry names affected destination documents/sections and merge timing; update only actual changes. After writer ownership is released, coordinate applicable writing skills:

| Material | When and how it reaches long-term documents |
| --- | --- |
| Change PRD | Once product decisions are confirmed, merge within authorization into the owning PRD; retain undelivered status. Implementation completion alone does not require a PRD entry. |
| Change Design | Confirmed direction may enter clearly marked target architecture; delivered structure enters current Design after implementation. Preserve important rationale in ADR. |
| Change Spec | After implementation and appropriate validation, semantically merge delivered target clauses into the latest application Spec as part of acceptance closeout. Replace affected sections and preserve unrelated guarantees; do not append or blindly overwrite. |

Recheck overlapping concurrent Changes against the latest effective contract; synchronize serially and resolve consequential conflicts. Compare target Spec, approved decisions, implementation/evidence and the merged main Spec. In team execution, the existing independent code-reviewer reviews implementation against the approved target, then the final PRD/Spec/Design merge diffs; later synchronization receives focused review, not a repeated complete code review. New semantics require approval; never lower requirements to accept defects.

Run applicable final validation after integration/fixes/synchronization under the execution workflow. Documentation-only merging does not require unrelated implementation reruns, unless consumed build/test inputs or behavior changed. Check affected links and patch formatting directly; no mandated checker/report. Only after delivery, review, validation and merging pass may acceptance and archival complete. Archived companion documents remain historical targets rather than copies maintained alongside the application docs.
