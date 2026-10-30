# Output Quality Evaluation

Use this reference when the user explicitly requests an evaluation of response quality or when task deliverables require formal expression assessment. This is an analytical method for the existing `code-reviewer` or `oracle` role. It assesses output against the user's prompt without re-performing the task or judging developer effort.

Examine the original request, the deliverable, and supporting evidence. Do not accept claims of success without verifying actual command outputs and artifacts.

| Dimension | Executable Check | Scoring Rubric (1–5) |
| --- | --- | --- |
| **Accuracy** | Verify facts, API usages, and claimed results against source documents and tool outputs. | **5:** All verifiable claims supported by evidence.<br>**4:** Minor cosmetic inaccuracy that does not affect conclusions.<br>**3:** One substantial factual error or multiple minor errors.<br>**2:** Multiple substantial errors.<br>**1:** Core conclusion is factually incorrect. |
| **Completeness** | Check whether all explicit requirements, boundary conditions, and failure modes are addressed. | **5:** Complete scope addressed.<br>**4:** Only an unstated minor detail omitted.<br>**3:** One stated requirement or several boundary conditions missing.<br>**2:** Multiple required items missing.<br>**1:** Core task unaddressed. |
| **Clarity** | Assess whether conclusions, conditions, technical terms, and evidence are immediately understandable. | **5:** Clear, unambiguous, logical flow.<br>**4:** Minor awkward phrasing.<br>**3:** Several ambiguous passages requiring re-reading.<br>**2:** Key sections difficult to decipher.<br>**1:** Incoherent or self-contradictory. |
| **Actionability** | Determine whether the reader can execute next steps, run validation, or make decisions without missing links. | **5:** Clear verification paths and entry points provided.<br>**4:** Next steps clear but validation path slightly implicit.<br>**3:** Ambiguous next steps.<br>**2:** Requires reader to invent missing steps.<br>**1:** Completely non-actionable. |
| **Conciseness** | Check whether information density is high, avoiding repetition and filler while retaining necessary context. | **5:** Efficient, essential context preserved.<br>**4:** Minor redundancy.<br>**3:** Noticeable bloat or repeated points.<br>**2:** Substantial irrelevant filler.<br>**1:** Noise obscures core meaning. |

Score each dimension independently, citing specific evidence from the evaluated deliverable. Provide an actionable recommendation for any score below 5.

**Critical Distinction:** High expression quality scores **do not establish domain correctness or substitute for task acceptance**. Domain correctness requires code verification, passing test suites, and project specification conformance.

Adapted from ECC agent-evaluator and self-evaluation rubrics (MIT License). See [ECC sources](../../agent-workflow/references/ecc-sources.md).
