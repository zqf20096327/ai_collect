# Qwen4 Max Pricing — what a task actually costs

> Per-million-token pricing with real workload budgets and comparisons.

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**[👉 Use Qwen4 Max on APIMart](https://gola.apimart.ai/k-Sbsk0L)**

`https://gola.apimart.ai/k-Sbsk0L`

[💰 Pricing](https://gola.apimart.ai/k-ldlt5A) · [🔑 Get an API key](https://gola.apimart.ai/k-XXONHC)

---

## Price

| | Per 1M tokens | Per 1K tokens |
|---|---:|---:|
| Input | **$1.4286** | $0.00143 |
| Output | **$4.2857** | $0.00429 |

Reasoning tokens are billed at the **output** rate.

## What a task actually costs

| Task | Input tokens | Output tokens | Cost |
|---|---:|---:|---:|
| Classify 1,000 tickets | 120,000 | 20,000 | $0.257 |
| Summarise a 50-page PDF | 40,000 | 1,500 | $0.064 |
| Agent run (10 steps) | 60,000 | 12,000 | $0.137 |
| Code review of a 400-line diff | 8,000 | 2,000 | $0.020 |

## How it compares

| Model | Input /1M | Output /1M |
|---|---:|---:|
| **Qwen4 Max** | **$1.4286** | **$4.2857** |
| Qwen3.8 Max | $1.3714 | $4.1143 |
| DeepSeek V3.2 | $0.1400 | $0.2800 |
| GPT-class frontier | $2.50 | $10.00 |

## Where the bill grows

- **Reasoning tokens** — hard problems can triple output tokens
- **Long context re-sending** — cache the stable prefix
- **Agent loops** — each step re-sends history

## Practical budget

| Monthly volume | Est. cost |
|---|---:|
| 1M input + 200K output | $2.29 |
| 10M input + 2M output | $22.86 |
| 100M input + 20M output | $228.60 |

---

## Related

- All prompt collections: [fujc683 repositories](https://github.com/fujc683?tab=repositories)

## License

CC BY 4.0
