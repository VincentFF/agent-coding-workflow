# agent-coding-workflow

一套面向 AI coding agent 的可组合技能与交付工作流：从需求澄清、行为契约、技术设计，到交付规划、实现、独立评审和验收归档。

工作流本身不绑定具体 coding agent。它通过 `adapters/` 接入 Codex、ZCode、pi 等运行环境，通过项目接入文件与目标项目的既有规则和文档约定合并。

## 它解决什么问题

AI 写代码时常见的问题不是不会写，而是：

- 需求、设计、当前行为被混在一份文档里，越写越乱。
- 计划批准了，实现却偏离或擅自缩小范围。
- 自己检查自己，缺陷和证据缺口被放过。
- 项目文档与代码不同步，旧方案长期残留在"现状"里。

这套工作流把职责拆开，并要求独立评审。

| 技能 | 负责 |
| --- | --- |
| `prd-writing` | 产品问题、范围、规则、验收与价值评估 |
| `spec-writing` | 行为契约：Change 的目标 Spec 与应用当前 Spec |
| `design-writing` | 技术结构；按需调用领域建模与代码结构设计 |
| `change-planning` | 组织一次交付：目标、材料集合、任务与验收 |
| `agent-workflow` | 实现、独立评审、文档合并、最终验证与归档 |
| `tdd` | 红绿行为切片 |
| `code-review` | 只读独立评审，契约与标准两轴 |
| `codebase-design` | 模块职责、接口、依赖与测试边界 |
| `domain-modeling` | 概念澄清、术语与 ADR |
| `grilling` | 单轮聚焦提问，收敛未决决定 |

## 使用方式

不需要手动复制文件。把这个仓库地址和版本交给 AI，让它按 [INSTALL.md](INSTALL.md) 安装：

> 按 `<repo>/INSTALL.md`，把 agent-coding-workflow `v0.1.0` 安装到当前项目。使用 Codex 和 ZCode，保留项目现有规则，完成后不要提交或推送。

安装会分发技能、写入运行环境适配、生成项目接入文件，并在 `AGENTS.md` 中合并一小段入口区块。

详细步骤见 [INSTALL.md](INSTALL.md)，工作原理见 [docs/workflow.md](docs/workflow.md)，项目定制边界见 [docs/customization.md](docs/customization.md)。

## 仓库结构

```text
agent-coding-workflow/
├── INSTALL.md                  # 给 AI 的安装、更新、卸载协议
├── distribution.json           # 分发清单：装什么、装到哪、怎么合并
├── skills/                     # 通用技能（唯一权威来源）
├── adapters/                   # 运行环境适配（角色模板与能力说明）
├── templates/                  # 项目接入文件模板
├── docs/                       # 工作流说明、采用与定制
└── examples/                   # 最小交付示例
```

## 版本与升级

发布使用语义化版本。项目通过 `.agents/coding-playbook.lock.json` 记录已安装版本、来源提交和受管文件摘要，升级时据此判断哪些文件可安全更新、哪些有本地改动需要比较。

## 许可证与来源

本项目包含对上游 MIT 技能的改编，来源与许可说明见 [NOTICE.md](NOTICE.md) 和各技能内的 `references/sources.md`。
