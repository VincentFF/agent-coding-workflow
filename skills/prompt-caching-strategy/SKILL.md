---
name: prompt-caching-strategy
description: Structure LLM prompts for cache reuse, analyze stable prefix boundaries, and calculate full API cost differences across providers.
license: MIT
---

# Prompt Caching Strategy

Use this skill when analyzing prompt cache hit rates, latency, and API costs for repetitive LLM calls. This skill does not start agents or introduce new caching infrastructure without approval.

## Cache Conditions and Access Boundaries

Identify the provider, endpoint, model, SDK, service tier, and caching mechanics. Verify minimum prefix length requirements, cache eviction policies (TTL), read/write pricing, and usage reporting schemas. Caching reduces token processing costs and time-to-first-token, but cached tokens still occupy context window limits.

Authenticate and authorize access before retrieving or reusing cached context. Cache storage and keys must isolate across users, workspaces, provider accounts, and data classifications. Keys represent lookup hints, not authorization tokens. Invalidate application-level cache references when underlying content or permissions change. Never store unredacted secrets or credentials in reusable system prompts.

## Structuring Stable Prefixes

1. Arrange prompt elements according to the provider's serialization order: place unchanging tool schemas, core system instructions, and static reference documentation at the beginning (prefix). Place dynamic variables, current user queries, timestamps, and transient evidence at the end (suffix). Any modification in the prefix invalidates subsequent cache matches.
2. Keep only relevant context. Do not pad prompts with arbitrary filler tokens merely to meet minimum prefix thresholds. Verify that reordering content does not alter instruction precedence or degrade model adherence.
3. Normalize provider usage reporting into distinct, non-overlapping categories: standard uncached input tokens ($U$), cache write/creation tokens ($W$), cache read tokens ($R$), output tokens ($O$), and storage token-hours ($H$, if applicable).

| Provider | Key Verification Points |
| --- | --- |
| OpenAI | Review prompt caching documentation and pricing. Check `cached_tokens` in usage objects for Responses and Chat Completions; verify whether prompt tokens include or exclude cached tokens. |
| Anthropic Claude | Review prompt caching guide. Check `cache_creation_input_tokens` and `cache_read_input_tokens`. Note explicit `cache_control` breakpoints, minimum token thresholds, and TTL rules. |
| Google Gemini | Review context caching guide and pricing. Differentiate between automatic caching and explicit cache objects with hourly storage fees. |

Verify exact parameter names, token thresholds, and pricing from official provider documentation before deploying.

## Comparative Cost Formula

Using consistent currency and pricing per million tokens, where $U$ = uncached input, $W$ = cache write tokens, $R$ = cache read tokens, $O$ = output tokens, and $H$ = storage token-hours:

```text
baseline_cost = (U + W + R) * input_rate / 1e6 + O * output_rate / 1e6
actual_cost   = (U * input_rate + W * write_rate + R * read_rate + O * output_rate + H * storage_rate) / 1e6
savings       = baseline_cost - actual_cost
```

Only use non-negative token counts and current pricing rates. Include cache write premiums, cache expiration, cache misses, and retries in actual costs. A prompt cache write that is never read can cost more than an uncached call.

## Empirical Verification and Handoff

Measure real traffic performance across representative batches:
- Calculate token cache hit rate: $R / (U + W + R)$.
- Calculate request hit rate separately, noting sample size and measurement duration.
- Compare end-to-end latency, time-to-first-token, and output consistency between cached and uncached requests.
- When live requests have not been executed, label hit rates and savings as unmeasured estimates.

For budget and retry governance, see [cost-aware-llm-pipeline](../cost-aware-llm-pipeline/SKILL.md).

Adapted from ECC (MIT License), original author cyberspace-cs. See [ECC sources](../agent-workflow/references/ecc-sources.md).
