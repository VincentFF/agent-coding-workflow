# Task-specific Methods

This guide coordinates which specialist skills and references to read for a specific technical task. Read only the methods matching the actual task, preserving approved contracts, project standards, and all authorization boundaries. These references are perspectives for existing `implementer`, `code-reviewer`, and `oracle` roles, not automatic agent dispatch or extra routine stages.

| Task | Methods to read when applicable |
| --- | --- |
| Go implementation / concurrency / resource fix | [golang-patterns](../../golang-patterns/SKILL.md); Go test work also uses [golang-testing](../../golang-testing/SKILL.md) under [tdd](../../tdd/SKILL.md); failure/cancellation work uses [error-handling](../../error-handling/SKILL.md)'s [Go reference](../../error-handling/references/go.md); review uses [go-review](../../code-review/references/go-review.md) and [silent-failures](../../code-review/references/silent-failures.md) for corresponding doubts. |
| SQL / schema / migration | [postgres-patterns](../../postgres-patterns/SKILL.md); migration changes additionally use [database-migrations](../../database-migrations/SKILL.md); review uses [postgres-review](../../code-review/references/postgres-review.md); existing project migration tools and deployment contracts remain effective. |
| TypeScript / JavaScript failure | [error-handling](../../error-handling/SKILL.md)'s [TypeScript reference](../../error-handling/references/typescript.md), selecting browser / Node.js / extension host semantics; [silent-failures](../../code-review/references/silent-failures.md) for swallowed-error doubts; do not load Go or unselected framework rules. |
| Concrete Go build / vet / lint failure | [go-build-recovery](../../tdd/references/go-build-recovery.md), preserving existing tooling and behavior contracts. |
| Actual LLM cost / budget question | [cost-aware-llm-pipeline](../../cost-aware-llm-pipeline/SKILL.md); no default cheap-model routing, layered retries, or circuit breakers without approved requirements. |
| Repeated prompt cache / measured reuse question | [prompt-caching-strategy](../../prompt-caching-strategy/SKILL.md); verify provider semantics, access boundaries, and actual usage. |
| Explicit output-quality assessment | [output-evaluation](../../code-review/references/output-evaluation.md); five expression-quality axes cannot establish factual correctness or substitute for domain acceptance. |

## Principles

1. **Load on demand, not in bulk.** Do not load the entire collection into conversation context. Match the task to the specific row above.
2. **Existing roles own execution.** `implementer` uses implementation, testing, and build recovery methods; `code-reviewer` uses review perspectives; `oracle` uses design and evaluation methods.
3. **Project contracts take precedence.** Project conventions (in `.agents/project-workflow.md`, `README.md`, or architecture documents) override generic skill suggestions.
4. **No unauthorized infrastructure.** Reading cost, caching, or migration skills does not authorize introducing new infrastructure, routing pipelines, or migration tools.
5. **Guidance, not runtime enforcement.** Shared Markdown files guide agent decision-making. They do not enforce filesystem sandboxing, network isolation, or automatic tool interception.

Skill origin, retained upstream licenses, and maintenance procedures are documented in [ECC sources](ecc-sources.md).
