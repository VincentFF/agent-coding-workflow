# 来源与许可

## 本项目的范围

`agent-coding-workflow` 由以下部分构成：

- 对上游 MIT 技能的改编，保留其方法与参考文件。
- 本地新增的工作流设计：PRD/Spec/Design 三类写作技能、交付材料集合与批准范围、目标 Spec 与当前 Spec 的区分及合并规则、目录式 Change、运行环境适配、安装协议。

## 上游来源

部分技能改编自 [mattpocock/skills](https://github.com/mattpocock/skills)，参考修订 `f3fc5632f401156837ee3872f14fe33ccf1024ea`，采用 MIT 许可。

| 本地技能 | 上游来源 |
| --- | --- |
| `change-planning` | `to-spec`, `to-tickets` |
| `agent-workflow` | `implement`, `implement-spec` |
| `tdd` | `tdd` 及其 tests/mocking 参考 |
| `code-review` | `code-review` |
| `codebase-design` | `codebase-design` 及其参考 |
| `domain-modeling` | `domain-modeling` 及 ADR/Glossary 格式 |
| `grilling` | `grilling` |

各技能内的 `references/sources.md` 记录该技能的具体保留方法与本地调整。上游 MIT 许可原文保存在 `skills/agent-workflow/references/UPSTREAM-LICENSE`。


### Everything Claude Code (ECC)

另有七个专项技能与五个评审/恢复规程改编自 [affaan-m/ECC](https://github.com/affaan-m/ECC)，参考修订 `b38be6a7f6350964d59328b52f0624e1d1d552d1`，采用 MIT 许可。

| 本地技能 / 参考 | 上游来源 |
| --- | --- |
| `golang-patterns` | `skills/golang-patterns/SKILL.md` |
| `golang-testing` | `skills/golang-testing/SKILL.md` |
| `postgres-patterns` | `skills/postgres-patterns/SKILL.md`（保留 Supabase team MIT 署名） |
| `database-migrations` | `skills/database-migrations/SKILL.md` |
| `error-handling` (含 Go & TypeScript 参考) | `skills/error-handling/SKILL.md` |
| `cost-aware-llm-pipeline` | `skills/cost-aware-llm-pipeline/SKILL.md` |
| `prompt-caching-strategy` | `skills/prompt-caching-strategy/SKILL.md`（保留 cyberspace-cs 署名） |
| `code-review/references/go-review.md` | `agents/go-reviewer.md` |
| `code-review/references/silent-failures.md` | `agents/silent-failure-hunter.md` |
| `code-review/references/postgres-review.md` | `agents/database-reviewer.md`（保留 Supabase team MIT 署名） |
| `code-review/references/output-evaluation.md` | `agents/agent-evaluator.md` 与 `skills/agent-self-evaluation/` |
| `tdd/references/go-build-recovery.md` | `agents/go-build-resolver.md` |

详细保留方法、本地改造与维护说明见 `skills/agent-workflow/references/ecc-sources.md`。上游 MIT 许可原文保存在 `skills/agent-workflow/references/ECC-UPSTREAM-LICENSE`。

## 本地设计

以下内容为本项目原创，不来自上游：

- `prd-writing`、`spec-writing`、`design-writing` 三个文档写作技能。
- 目标 Spec 与当前 Spec 的区分、交付后语义合并规则。
- 交付目录（`change.md` 及可选配套材料）与材料集合批准。
- 安装协议、分发清单、运行环境适配与项目接入模板。
- 候选身份工具的用途边界（可选，不构成验收门槛）。

## 使用注意

本项目描述的是**工作方法**，不包含任何业务项目的专属规则、模型选择或凭证。采用方应保留自己的安全、授权与验证要求；安装过程不降低既有约束。
