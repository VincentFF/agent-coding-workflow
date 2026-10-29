# agent-coding-workflow

本仓库维护通用 AI coding 工作流。它是**方法仓库**，不承载业务项目。

## 开始工作前

1. 读 [README.md](README.md) 了解项目定位与技能分工。
2. 修改技能或协议前，读 [docs/workflow.md](docs/workflow.md) 与 [docs/customization.md](docs/customization.md)。
3. 修改安装行为前，读 [INSTALL.md](INSTALL.md) 和 [distribution.json](distribution.json)。

## 本仓库的约束

- `skills/` 是通用技能的唯一权威来源。业务项目的定制不写回这里。
- 技能正文使用英文，以保持跨项目一致；说明类文档使用中文。
- 不把模型、供应商、凭证、业务领域术语或特定测试框架写进通用技能。
- 技能之间保持相对链接可用：移动或改名时同步修复引用。
- 新增或修改技能后，确认 `distribution.json` 的 `skills` 列表与实际目录一致。
- 角色模板不携带模型绑定；运行差异写进对应 `adapters/<env>/README.md`。

## 修改技能时的检查

无法用脚本证明的东西不要假装验证过。至少人工确认：

- 每个步骤仍有可判断的完成条件。
- 没有把项目专属假设写成通用要求。
- 修改后 `distribution.json`、`INSTALL.md`、`README.md` 的描述仍一致。
- 相对链接可达。

## 发布

版本记录在 [CHANGELOG.md](CHANGELOG.md)。采用方通过固定版本安装。改变安装布局、技能名称或交付状态语义时，需要在 CHANGELOG 中说明升级影响。

## 不做什么

不在本仓库引入业务实现、CI 流水线、部署配置或示例项目之外的应用代码。示例只用于说明工作流产物形态。
