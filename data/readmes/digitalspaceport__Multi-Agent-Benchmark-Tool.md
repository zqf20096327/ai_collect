# Multi Agent Benchmark Tool

A lightweight, asynchronous benchmark to emulate multiple autonomous Openclaw or “Hermes-style” agents sending requests to a single OpenAI-compatible endpoint (such as vLLM or llama.cpp). Here, “Hermes-style” refers to the prompting and interaction pattern used for the workload, not a formal compatibility claim with any specific Hermes framework or implementation. The tool measures request-level experience (TTFT), throughput (prefill and decode tokens per second), and realistic tool-calling flows with follow-up requests. If you want to run multiple local agents, this benchmark can help you tune your inference stack.

## Why this tool?

- Request-level metrics that matter for agents:
  - Time-To-First-Token (TTFT)
  - Time-Per-Output-Token (TPOT)
  - Request latency distributions (including $p95$)
- Realistic agent behaviors:
  - Tool calls with streamed aggregation and message reconstruction
  - Follow-up assistant requests after tool outputs (common agent pattern)
  - Multimodal user inputs (image URLs)
- Robustness:
  - Usage-based token counts during streaming when supported (tested with vLLM)
  - Fallback token estimation when streaming usage metadata is unavailable
  - Pacing controls with jitter to avoid synchronized spikes
  - Timeouts and SDK-level retries

## Key metrics

- Time to First Token (TTFT): Measured from request start to the first streamed response event. In most cases this closely tracks the first visible model output, though exact behavior may vary slightly by provider.
- Time per Output Token (TPOT): Calculated from total completion latency divided by completion tokens. This metric is most informative for text-generating responses and may be less representative for tool-call-heavy or non-text turns. Computed as `((T_total - T_TTFT) / completion_tokens)`.
- Prefill throughput: `prefill_tokens / T_wall`.
- Decode throughput: `completion_tokens / T_wall`.
- Requests per second (RPS): `completed_requests / T_wall`.

Note on pacing and achieved RPS:
- With `N` agents, per-agent pacing interval `Δ = 1/λ` and average service time `S`, achieved per-agent throughput is approximately `1 / (S + Δ)`, so aggregate RPS is approximately `N / (S + Δ)`.
- This benchmark reports achieved RPS. Use `--target-total-rps` and `--min-per-agent-rps` to guide pacing, understanding the service-time dependency.

## Installation

- Python 3.9+
- openai Python SDK

```bash
pip install --upgrade openai
```

## Streaming usage reporting (optional)

If your server supports streaming usage:
- Use `--include-usage` to obtain accurate token counts when your server emits usage metadata in streamed responses.
- If usage metadata is unavailable, the tool falls back to a rough estimator.

## Quick start

```bash
python mabt.py \
  --base-url http://localhost:9876/v1 \
  --model qwen35-27b \
  -n 4 \
```

## Tune it more

```bash
python mabt.py \
  --base-url http://localhost:9876/v1 \
  --model qwen35-27b \
  -n 16 \
  --max-turns 25 \
  --target-total-rps 3.0 \
  --min-per-agent-rps 0.35 \
  --enable-tools \
  --tool-followup \
  --include-usage
```

The quick start runs 4 concurrent agents against the endpoint, while the expanded example runs 16, enables tools on some turns, and issues a follow-up assistant request when tool calls appear (to emulate agent frameworks). The examples use port 9876 via `--base-url`

## CLI options

- `-n, --agents`: number of concurrent agents (default: 8)
- `--base-url`: API base URL (default: `http://localhost:9876/v1`)
- `--model`: model name to target; required (no default)
- `--max-turns`: number of user prompts per agent (default: 15)
- `--compaction-trigger`: naive compaction via context reset + tail retention (default: 20000)
- `--target-total-rps`: soft target for aggregate RPS (default: 3.0)
- `--min-per-agent-rps`: floor for per-agent RPS (default: 0.35)
- `--jitter-frac`: pacing jitter fraction (default: 0.2 → ±20%)
- `--temperature`: sampling temperature (default: 0.7)
- `--max-tokens`: max generated tokens (default: 512)
- `--timeout`: request timeout seconds (default: 120)
- `--api-key`: API key (default: `EMPTY`)
- `--enable-tools`: enable tool declarations and `tool_choice=auto` on some turns
- `--tool-followup`: after a tool-call, send a follow-up assistant request that consumes tool outputs
- `--enable-images`: occasionally include an image URL in user inputs
- `--include-usage`: ask the server to include token usage in the final streamed chunk

## Output

- Console summary:
  - Overall throughput and totals
  - Per-agent TTFT/TPOT/latency
  - “High Quality” agent counts vs. thresholds (configurable in code)
- JSON artifact:
  - `mabt_benchmark_results.json` with complete aggregates and per-agent stats

## Notes on tool-calling accuracy

- Tool calls are reconstructed from streamed deltas and preserved in the conversation history.
- When `--tool-followup` is set, synthetic tool outputs are inserted and a follow-up assistant request is issued. This mirrors how agent frameworks increase load after tools.
- If your endpoint does not support tool calls, omit `--enable-tools`.

## Caveats and future directions

- If `--include-usage` is not supported by your endpoint, token counts are estimated, and TPOT or throughput metrics may be less accurate.
- The default image URL format follows OpenAI-compatible Chat Completions multimodal conventions; omit `--enable-images` if your server/model is text‑only.
- The benchmark measures achieved RPS (completed requests per wall time); actual pacing depends on service times.
- "High Quality Agents" is a benchmark-specific label and “high quality” refers to agents that are responsive enough to reliably complete actions within acceptable latency bounds, reducing the likelihood of timeout-driven retries, stalled workflows, or degraded user experience. It is an operational latency/reliability label, not a measure of reasoning quality, correctness, or task intelligence.
- Tool simulation today, extensibility tomorrow: the current release includes a lightweight synthetic tool schema to exercise tool-calling paths, multi-turn follow-up behavior, and parser compatibility under load. Future versions may expand this simulator with richer tool sets or optionally connect to real tool backends for more realistic agent execution patterns, including deeper integration with Openclaw or Hermes-style tooling where appropriate.

## License

MIT — see `LICENSE`.