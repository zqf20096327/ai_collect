# Cheap LLM API — price per million tokens, ranked

> Every LLM on APIMart ranked by cost, plus a two-tier routing pattern that cuts bills ~70%.

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**[👉 Use Qwen4 Max on APIMart](https://gola.apimart.ai/k-KvaHgX)**

`https://gola.apimart.ai/k-KvaHgX`

[💰 Pricing](https://gola.apimart.ai/k-5qbxtS) · [🔑 Get an API key](https://gola.apimart.ai/k-DTFTPv)

---

## Cheapest capable LLMs, ranked

| Model | Input /1M | Output /1M | Best for |
|---|---:|---:|---|
| DeepSeek V3.2 | $0.14 | $0.28 | bulk classification, extraction |
| Qwen3.7 Flash | $0.15 | $0.60 | cheap chat |
| Step 3.7 Flash | $0.15 | $0.93 | tool calling |
| Qwen3.8 Max | $1.37 | $4.11 | harder reasoning |
| **Qwen4 Max** | **$1.43** | **$4.29** | hardest reasoning, Chinese |

## How to cut LLM spend

1. **Route by difficulty** — cheap model first, escalate on low confidence
2. **Cache the stable prefix** — system prompts are re-billed every call
3. **Cap reasoning** — `max_tokens` limits the thinking budget too
4. **Batch** — 1,000 small calls cost more than 10 batched ones

## Two-tier routing pattern

```python
def answer(q):
    cheap = call("deepseek-v3.2", q)
    if cheap.confidence > 0.8:
        return cheap
    return call("qwen4-max", q)
```

Typical split: 80% cheap, 20% strong → **~70% lower bill** than always-strong.

## Cost of a real workload

| Workload | Model | Monthly cost |
|---|---|---:|
| 1M classify calls | DeepSeek | $42 |
| 100K support replies | Qwen4 Max | $98 |
| 10K agent runs | Qwen4 Max | $137 |

---

## Related

- All prompt collections: [fujc683 repositories](https://github.com/fujc683?tab=repositories)

## License

CC BY 4.0
