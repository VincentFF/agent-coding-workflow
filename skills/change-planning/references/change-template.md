# Change Entry Outline

Use this outline for `change.md` within a delivery directory. Adapt the sections to meaningful content; the writing skills own the PRD/Spec/Design formats. Paths, states and approval scope follow the [document contract](document-contract.md). Preserve legacy single-file Changes in place.

```markdown
# <可判断是否完成的交付目标>

状态：draft
批准依据：<实际批准后记录指令或来源；草稿可省略>
依赖：<前置交付及其可用条件；无则写无>

## 目标与边界

<具体问题、本次交付结果、明确不做什么>

## 变更摘要

<相对现状的主要变化、必须保留的重要承诺；不复制完整契约>

本次批准材料：

- <本文件与实际需要的 spec.md、prd.md、design.md 链接及用途>
- <现有契约、产品决定、ADR 等来源的具体章节>

<重要未决事项放在其所属材料中，并在此概述对实施的影响>

## 实施计划

- [ ] <可验证的结果、依赖和完成条件；引用对应契约与验收>
- [ ] <必要的集成、文档合并和验证工作>

## 验收

<关键输入或前置条件、预期结果、检查方法与证明边界>
<实际验证入口或需要随任务交付的入口；沿用项目规定的检查>

## 文档合并

<目标材料要合并到哪些长期文档和章节、替换什么、何时可生效>

## 交付结论

<交付完成时简述实际结果、批准的例外、遗留项和证据位置；规划时可省略>
```

Approval applies to the listed material set. Omit unnecessary files; never create empty companions to fill a checklist. Keep tasks and final conclusions here, product requirements in PRD, target behavior in Spec and substantive technical mechanisms in Design. Execution history and full logs stay in runtime artifacts.
