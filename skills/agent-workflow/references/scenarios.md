# Scenario Walkthroughs

Use when maintaining the skill or running its first trial. Rule and path checks establish only that document conventions are complete and readable; they do not replace observing actual subagent execution. A trial must also verify rules read, red/green evidence, independent review, and final-tree evidence.

| Scenario | Expected behavior |
| --- | --- |
| The user only discusses an approach or asks the AI to write a skill | Do not infer permission to delegate or implement project changes; file writes require the corresponding explicit request |
| Ordinary wording correction outside agent-workflow | Direct edits and focused checks are sufficient; do not manufacture a Change or team |
| Small change explicitly using agent-workflow | Still use an independent code-reviewer; do not manufacture red for non-behavior tasks |
| Related tasks share mutable files | Use one implementer sequentially; task count does not justify parallel writers |
| Tasks can be independently implemented/validated and parallelism has a real benefit | Assign exclusive write scope, isolated worktrees if needed and an integration owner; integrate only after prerequisite handoffs |
| Routine handoff needs candidate identity | Reuse adequate commit/runner records; no per-role snapshot or automatic candidate.py invocation |
| A repair attempt yields a new reproducible hypothesis | Continue affected repair/verification regardless of an arbitrary round count; pause when no viable hypothesis remains or a user decision is needed |
| Implementation was reviewed before long-term documents were merged | The main agent merges under the writing skills, then sends only later diffs for focused review by the same code-reviewer |
| Code-reviewer identifies a defect after document merging | Repair implementation, revise only affected merged content and rerun affected checks/review before final validation |
| The same full suite has already run during development | Code-reviewer focuses on independent doubts; main agent runs the approved final scope, with no automatic full rerun by every role |
| One login goal includes multiple tasks | One Change directory with tasks in change.md and only needed companions; task count alone does not require multiple Changes |
| Login and permissions are two delivery goals in the same discussion | Propose separately assessable Changes with actual dependencies; approve their complete material sets without an automatic separate split-approval round |
| An existing project has no long-term documents | Use spec-writing for the affected behavior baseline and design-writing for the affected structure; keep delivery-specific targets in the Change |
| A Change says approved without actual approval evidence | Verify sources; state alone does not establish implementation, delegation, or publishing authority |
| tdd/code-review or required original contracts are unreadable | Stop during main-agent preflight or child loading; do not proceed from summaries |
| Spec omits how duplicate requests affect data | Treat this as a data-semantics contract gap and complete the contract first; private function naming needs no approval |
| Red comes from a broken fixture or environment | Do not record it as behavior red; fix test conditions and confirm the actual symptom |
| Fake tests pass while a real-process persistence guarantee was promised | Do not claim the guarantee is verified; add evidence at the corresponding boundary or report a blocker |
| The implementer committed code and the working-tree diff is empty | The code-reviewer still checks baseline-to-candidate commits and current untracked new files |
| Unsynchronized long-term documents are explicitly assigned to the main agent | The code-reviewer lists pending closeout obligations; final PRD/Spec/Design synchronization uses the corresponding writing skill and returns to the same code-reviewer for focused review before acceptance |
| A PRD has no measured value baseline or agreed numeric target | Use prd-writing to distinguish delivery acceptance from value assessment; propose representative evidence or human assessment without inventing metrics |
| Deduplication is deferred from release scope | Use prd-writing to revise affected flows, repeat-alert scenarios and acceptance objectives together; preserve long-term intent and decision sources |
| A feature is delivered without changing its product goals | Keep the PRD goals effective, link detailed behavior to Spec and progress to the development plan/Change; no completion entry is required |
| PRD feasibility analysis needs a technical judgment | Identify the unknown for the main agent to investigate or arrange as separate design analysis; PRD writing does not automatically invoke design-writing or treat feasibility as product approval |
| A PRD refers to delivered detailed behavior | Read and link the existing Spec; any Spec edit is separately coordinated by the main agent within authorized scope, not triggered by PRD or requirement approval |
| Design uses familiar terms and only needs a diagram correction | Use design-writing's synchronization branch; preserve the decision without routinely loading domain-modeling or codebase-design |
| Task identity is unclear and module ownership must change | Use design-writing to clarify identity with domain-modeling, then structure with codebase-design; settle consequential choices before implementation |
| A target architecture contains an undelivered Worker | Distinguish that target from the delivered runtime; keep its delivery-specific interface contract in the owning Change |
| A deployment design is cancelled or replaced | Update affected text and diagrams together under design-writing; preserve ADR rationale and historical Change evidence |
| A bug fix restores an existing Spec promise | Apply spec-writing's update decision; retain the rule unless the fix reveals an important missing boundary, and avoid adding a repair history entry |
| A delivery changes page capacity and failure recovery | Write the full affected target capability in the Change spec.md, preserve current behavior in the main Spec until validated delivery, then semantically merge and review the affected capability |
| Another accepted Change modified the same main Spec during implementation | Compare the latest main contract, approved target and implementation; resolve semantic overlap instead of overwriting intervening guarantees |
| A behavior-preserving refactor has sufficient existing contracts | Reference them in change.md without creating empty spec.md/prd.md; separate substantive design only if needed |
| A legacy single-file approved Change is resumed | Keep its original location, structure and approval scope; no format-only migration is needed |
| Implementation satisfies only part of the target Spec | Report incomplete scope and retain unaccepted status unless the user explicitly approves a scope revision; never silently merge partial behavior as full delivery |
| An undelivered capability is cancelled | Correct any false current-capability claim in Spec under spec-writing; keep cancellation of future requirements with its owning PRD/Design/Change |
| Spec reorganization moves interface details out of Design | Preserve effective input/output/error/compatibility semantics, repair inbound references and leave one authoritative definition; invent no new behavior |
| A README assigned to this round's writer is missing | Report an implementation defect; do not skip it as a main-agent closeout obligation |
| Faithful synchronization or status/archive-only edits | Check consistency and affected document/patch checks without reapproval or unrelated implementation reruns; expand if build/test inputs consume the edited files |
| Synchronization introduces new behavioral or structural meaning | Reapprove and rereview; do not conceal defects by changing Spec |
| Implementation/tests change after checks passed | Reassess actual inputs, rerun affected checks/review and retain final main-agent validation; avoid automatic three-role full-suite repetition |
| Reading/export constraints span Change and Design (for example error/partial filtering, independent deadlines, staging budget, readiness and DTO validation) | Before writer handoff, map consequential constraints to original sources, owning tasks and boundary checks; code-reviewer still inspects original texts for omissions |
| Cleanup promises process groups and registered test resources; a finding demands all arbitrarily detached processes | Main agent verifies the original scope, treats the additional guarantee as an optional scope extension, and continues fixing actual registered-resource leaks |
| A code-reviewer reports a reachable regression without an explicit Spec clause | Cite the established behavior and triggering conditions; do not dismiss it merely because the mapping omitted it |
| A code-reviewer finding lacks a source, triggering case or concrete evidence | Main agent requests evidence before fix dispatch or user escalation; record its disposition in the existing review artifact |
| An affected reference targets an external repo or a moved document | Inspect the referenced material or report the unavailable source; reference reachability alone does not establish contract correctness |
| The approved error-view example contains one partial and one error request, but implementer code/test expect only one | Retain the original two-result expectation, flag the implementation/expectation drift and fix it; do not accept matching code/tests as proof |
| An acceptance runner does not yet exist | Fix input/expected semantics before implementation, assign runner delivery, then prove it actually executes; do not invent a runnable command |
| A repair changes source or expectations | Use existing source records to assess inputs and retain old evidence labels; a separate index/helper is optional |
| Source is unchanged but ignored binary, tool version or external input changes | Source identity alone cannot carry evidence; check dependent artifacts/environment and rerun affected proof |
| A new independent implementer task starts with a long/unrelated parent chat | Prefer a concise isolated handoff; provide original sources, scope and acceptance pointers |
| A implementer needs highly relevant investigation already in the parent context | Relevant inheritance is allowed; preserve decisions and prefer continuing the same implementer over rediscovery |
| The first code-reviewer is about to launch | Disable parent-history inheritance through actual runtime controls; retain mandatory sources and configured role/model/permissions |
| A repair continues the same code-reviewer | Send the incremental diff/evidence and unresolved findings while retaining the original fixed baseline and complete review obligation |
| Runtime cannot establish a fresh first-review context | Report the affected gate unresolved; do not claim full-history inheritance is independent context or silently change invocation methods |
| Two Changes modify the same long-term Design | The main agent synchronizes serially and checks subsequent assumptions without overwriting work |
| Required validation or human approval is incomplete | Keep delivery unaccepted and explain the blocker; optional suggestions may be deferred |
| A new Change is created | Use its local creation date in the directory, start with draft change.md, list applicable companion/source materials and avoid premature archival |
| Revision, approval, or acceptance occurs after the creation date | Retain the directory identity (or legacy filename); do not rename using the acceptance date |
| Required gates pass and acceptance closeout begins | Complete long-term merges and review, set accepted in the entry, move the whole package or legacy file, and repair references; no extra archival permission is required |
| An archive destination already has the same delivery identity | Do not overwrite or copy; keep approved and report a blocker |
| State updates, evidence pointers, or post-archival checks fail | Restore the active location and references and keep approved; if recovery fails, report the actual location without claiming acceptance or rerunning unrelated full checks |
| An already archived, successfully checked accepted Change is read again | Retain the unique historical file without moving or renaming it again |

For a real trial, choose a small change with clear public behavior, repeatable tests, and controllable dependencies. Observe the minimal complete loop before evaluating multiple Changes or parallel execution. If no trial project is specified, do not modify other repositories on your own initiative.
