# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)；版本遵循语义化版本。

## [Unreleased]

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
