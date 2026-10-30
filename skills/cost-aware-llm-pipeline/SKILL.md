---
name: cost-aware-llm-pipeline
description: Track LLM token usage, calculate multi-attempt retry costs, evaluate prompt caching impact, and analyze model budget tradeoffs without unauthorized pipeline changes.
license: MIT
---

# LLM Cost Analysis Patterns

Use this skill when analyzing LLM API expenses, setting token budgets, or evaluating model invocation efficiency. Inspect the project's actual model configuration and client call chains before applying cost optimizations. This skill does not start agents or authorize unapproved model routing, layered retries, or circuit breakers.

## Complete Task Cost Accounting

1. Identify the provider, endpoint, model version, SDK, service tier, currency, pricing date, and existing retry policies. Consult current official provider documentation for exact token pricing and usage schema definitions.
2. Track input tokens, output tokens, cache creation/write tokens, cache read tokens, tool execution fees, and latency across all attempts for each task. Distinguish between verified provider usage reports and pre-call estimates; unreturned usage upon timeout does not imply zero cost.
3. Calculate costs by multiplying mutually exclusive token categories by their respective unit rates, adding output, tool, and storage costs. Account for all failed attempts, retries, and cache refresh overhead.
4. Compare total task cost, end-to-end latency, and success/fallback rates across comparable sample runs. Do not report average costs based solely on successful attempts while hiding the expense of failed attempts.

## Budgets and Recovery Contracts

- Define explicit budgets per task, per batch, and across concurrent in-flight executions. Establish clear policies for budget exhaustion (e.g., stop, degrade gracefully, or request human approval).
- Reserve estimated tokens for in-flight requests before dispatching calls, reconciling with actual usage upon completion; accumulating usage only after completion cannot prevent concurrent budget overruns.
- Review existing client and worker retry policies before adding new retry logic. Bound total attempts, elapsed time, and cumulative spending. Retry only retriable transient failures with cancelable backoff delays.

## Systematic Optimization Sequence

1. **Context Pruning:** Remove irrelevant context, redundant instructions, and duplicate retrieved passages before modifying pipelines.
2. **Prompt Caching:** Structure prompts with stable prefixes to maximize provider cache reuse according to [prompt-caching-strategy](../prompt-caching-strategy/SKILL.md). Ensure cache savings do not compromise necessary fresh evidence.
3. **Model Selection:** Evaluate cheaper models only when explicitly requested and supported by empirical quality benchmarks. Low character count or brief inputs do not prove a task is simple. Never hardcode unapproved model IDs or introduce automatic model fallback cascades without approval.
4. **Output Quality:** Assess generated outputs using [output-evaluation](../code-review/references/output-evaluation.md) across standard quality axes. Remember that high expression quality scores do not establish factual correctness; domain verification requires real evidence.

Adapted from ECC (MIT License). See [ECC sources](../agent-workflow/references/ecc-sources.md).
