# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)；版本遵循语义化版本。

## [Unreleased]

## [0.2.0]

### Added

- 新增 7 个通用专项技能：
  - `golang-patterns`: Go 包组织、消费方接口、错误包装、goroutine 生命周期与退出条件、资源释放及性能分析。
  - `golang-testing`: 最小有效 Go 测试模式（子测试、测试隔离与清理、HTTP 测试、替身、golden、benchmark、fuzz 与覆盖率诊断）。
  - `postgres-patterns`: PostgreSQL 执行计划（EXPLAIN ANALYZE 隔离执行）、索引选择、约束不变量、锁顺序、SKIP LOCKED 队列与连接池分析。
  - `database-migrations`: PostgreSQL schema/数据迁移评估、锁与重写开销、批量回填、隔离验证与条件式 expand-contract 模式。
  - `error-handling`: 类型化错误分类、cause 保留、异步观察、取消清理与重试边界，拆分 Go 与 TypeScript 按需参考。
  - `cost-aware-llm-pipeline`: LLM 任务级别 token 计量、多轮重试花费、并发在途预算、缓存前置评估与模型选择权衡。
  - `prompt-caching-strategy`: Prompt 缓存稳定前缀设计、provider usage 归一化统计、完整计费比较公式与离线算术验证。
- 新增 5 个来自 ECC Agent 的按需审查与恢复规程：
  - `skills/code-review/references/go-review.md`: Go 专项代码审查视角。
  - `skills/code-review/references/silent-failures.md`: 防静默吞错审查视角。
  - `skills/code-review/references/postgres-review.md`: PostgreSQL 专项审查视角。
  - `skills/code-review/references/output-evaluation.md`: 5 维表达质量评估规程（明确不替代事实正确性与业务验收）。
  - `skills/tdd/references/go-build-recovery.md`: Go 编译与 linter 错误恢复操作规程。
- 新增统一任务导航：`skills/agent-workflow/references/task-methods.md`，按任务匹配专项技能与参考，避免全量载入上下文。
- 新增来源说明与许可：`skills/agent-workflow/references/ecc-sources.md` 与 `skills/agent-workflow/references/ECC-UPSTREAM-LICENSE`。
- `distribution.json` 分发清单由 10 个技能扩充至 17 个技能。

### Changed

- `skills/tdd/SKILL.md`: 增加任务级实现方法引导，按需引用 Go、错误处理及构建恢复规程。
- `skills/code-review/SKILL.md`: 增加任务级审查方法引导，按需引用 Go、防吞错、PostgreSQL 与输出质量评估参考。
- `skills/design-writing/SKILL.md`: 在结构设计阶段条件式引入 Go、错误处理、持久化/迁移与 LLM 成本/缓存方法。
- `skills/agent-workflow/references/execution.md`: 在技能交接中引入按任务选择技能与绝对路径交接要求。
- `INSTALL.md`、`README.md`、`NOTICE.md`、`templates/project-workflow.md`、`docs/workflow.md`、`docs/customization.md` 同步适配 17 个技能与专项导航。

### Upgrade Notes

- 本版本向后兼容。已有项目从 `0.1.0` 升级至 `0.2.0` 时，安装器会分发 7 个新技能并更新现有技能中的引用，项目已有的接入文件与定制约束默认保留。


## [0.1.0]

### Added

- 通用技能：`change-planning`、`agent-workflow`、`prd-writing`、`spec-writing`、`design-writing`、`codebase-design`、`domain-modeling`、`tdd`、`code-review`、`grilling`。
- 交付目录结构：`change.md` 为入口，按需配套目标 `spec.md`、`prd.md`、`design.md`。
- 目标 Spec 与当前 Spec 的区分，以及交付后的语义合并规则。
- 安装协议 `INSTALL.md`（识别、分发、接入、记录、升级、卸载、验证）。
- 分发清单 `distribution.json`，声明受管文件、安装位置与合并方式。
- 项目接入模板 `templates/project-workflow.md` 与入口区块模板。
- Codex、ZCode、pi 三个运行环境适配说明与角色模板（不含模型绑定）。
- 可选候选身份工具 `candidate.py`，不构成默认步骤或验收门槛。

### Notes

- 首个版本。尚需在至少两个不同类型的项目中验证安装与升级流程后才能视为稳定。
