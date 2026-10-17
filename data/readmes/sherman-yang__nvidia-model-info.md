# NVIDIA Model Info Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A local web dashboard for browsing the free NVIDIA models listed on
[build.nvidia.com](https://build.nvidia.com), with sortable metadata, model-card
specs, live API probes, tool-calling detection, and copyable cURL examples.

The app is built for repeated model comparison work: dense table layout,
default `agent` filtering, pinned high-value columns, explicit rate limiting,
and refresh behavior that rebuilds local model-card data from NVIDIA sources.

## What It Shows

- Active and usable NVIDIA model IDs from `/v1/models`
- Flattened model metadata as sortable and searchable table columns
- Publisher labels from model cards, such as `agentic`, `coding`, `MoE`, and `Tool Use`
- Publisher-stated `Context (Card)` from `model_specs.json`
- Live-probed `Context (Deployed)` — the context window the hosted endpoint
  actually enforces, parsed from its own validation errors (it can be smaller
  than the model card claims)
- Live probe results for availability, latency, max output semantics, tool
  support, and how reasoning output is exposed in the default response
- Optional capability probes per model: reasoning support (default-on /
  toggleable / none observed), structured output
  (`response_format` json_schema and `nvext.guided_json`),
  `tool_choice: "required"`, parallel tool calls, and vision input
- Right-click popover per model: forced single-row actions (base re-test,
  capability probe, deep context probe) plus copyable cURL examples
- Duplicate model IDs removed before rendering

## Quick Start

Requirements:

- Node.js 18 or newer
- A NVIDIA API key from build.nvidia.com for live probes

```bash
git clone https://github.com/sherman-yang/nvidia-model-info.git
cd nvidia-model-info
export NVIDIA_API_KEY="nvapi-..."
./start.sh
```

The server listens on `http://localhost:4920` and attempts to open the
dashboard in your default browser.

If `model_specs.json` is missing or empty on first launch, the dashboard
automatically runs the same flow as `Force Refresh Data`: it clears local probe
state, loads the model catalog, fetches model-card specs, rebuilds
`model_specs.json`, reloads the table, and then applies the default `agent`
search filter.

## Main Controls

| Control | Behavior |
| --- | --- |
| Search | Defaults to `agent` after startup data loading. Space-separated terms use OR matching across displayed cells. |
| Exclude Inactive/Error | Hides rows whose live probe state is `Error` or `Inactive`. |
| Tool Support | Shows only rows confirmed to return tool calls. |
| Ping / Re-test | Runs a live probe for one row. Requires `NVIDIA_API_KEY`. |
| Test Displayed Models | Batch-tests displayed rows that are missing complete live probe data. Requires `NVIDIA_API_KEY`. |
| Shift + Click on Test Displayed Models | Forces a re-test of every displayed row (capability results are preserved). |
| Test Capabilities | Batch-runs the capability probes (reasoning support, structured output, `tool_choice: "required"`, parallel tool calls, vision) for displayed rows whose capabilities are untested. Requires `NVIDIA_API_KEY`. |
| Shift + Click on Test Capabilities | Forces capability re-probing of every displayed row. |
| Probe Deployed Ctx | Finds the deployed context window for displayed rows that completed a base test but whose `Context (Deployed)` is still blank — bisecting the `max_tokens` boundary, or probing from the input side when the server clamps silently. Requires `NVIDIA_API_KEY`. |
| Shift + Click on Probe Deployed Ctx | Forces re-probing of every displayed tested row — `Untestable`, `≥N`, and numeric values alike (`force=1`). |
| Force Refresh Data | Clears probe cache, reloads `/v1/models`, re-pulls model cards, rebuilds `model_specs.json`, and reloads table data. |

## Data Sources

The dashboard combines two NVIDIA sources:

| Source | Used For |
| --- | --- |
| `https://integrate.api.nvidia.com/v1/models` | Model IDs and basic model metadata |
| `https://api.ngc.nvidia.com/v2` catalog endpoints | Model-card labels, context limits, use cases, and model page links |

`model_specs.json` is generated from the public NGC catalog API and committed to
the repository so the table can show model-card specs immediately after startup.
Use `Force Refresh Data` or `npm run populate-specs` to rebuild it from current
NVIDIA model cards.

## Live Probe Behavior

`GET /api/test-model?model=<id>` performs up to three sequential checks (four
with `&caps=1`). Every probe request is streamed (`stream: true`): the response
is consumed chunk by chunk and the deltas are reassembled into a normal
completion before classification. As a result the per-attempt timeouts below
are **idle timeouts** (time-to-first-byte and the gap between chunks), not
total wall-clock budgets, so a slow-but-steadily-streaming reasoning model is
not falsely timed out. `PROBE_STREAM_HARD_TIMEOUT_MS` (300s default) caps the
total duration of any one streamed attempt.

1. Availability and latency using `chat/completions`. The first attempt sends
   no `max_tokens`; if that fails, one retry sends
   `AVAILABILITY_FALLBACK_MAX_TOKENS` (`4096` by default) to clear
   "max_tokens is required" rejections — the only failure a bigger budget can
   fix. Availability stores a hidden status such as `available`,
   `available_length_limited`, `available_async` (HTTP 202 async endpoints),
   `timeout`, `unavailable`, or `backend_error`, plus how reasoning output was
   exposed (`reasoning_content` field, `<think>` tags in content, or none).
2. Deployed-limits detection using an oversized `max_tokens` request. vLLM
   validates the request before inference, so the rejection is instant, costs
   no tokens, and its error text discloses the **deployed context window**
   (`max_model_len`) — the only machine-readable source of that value on the
   hosted endpoint. All observed error shapes are parsed
   (`max_model_len=max_total_tokens=N`, "maximum context length is N tokens",
   "context length is only N tokens", "exceeds maximum allowed token size N").
   Models that silently clamp the oversized value (HTTP 200) report
   `Max Output = Context-bound` — hosted models bound completion length by
   (deployed context − input tokens); there is no separate completion cap.
   Transient 5xx capacity errors stay retryable instead of caching a dead end.
   This probe can still run after an availability timeout or inconclusive
   availability error, but not after clear auth/model-unavailable failures.
3. Tool-calling detection using several OpenAI-compatible request shapes in
   order: `tools`, forced (named) `tool_choice`, `tool_choice: "auto"`, and
   legacy `functions` / `function_call`. The primary `tools` request steps
   through `128`, `2048`, and no `max_tokens`; forced/auto use `512` then no
   `max_tokens`; legacy gets one `512` attempt; the whole tool probe stops
   after 8 requests, sized so the forced variant always gets a turn. Budgets
   escalate only on `finish_reason="length"` — a completed text answer moves
   to the next variant instead. A model that answers in plain text despite a
   forced named `tool_choice` is recorded as `toolSupport=false`
   (`forced_tool_choice_ignored`); call text found in `content` with empty
   `tool_calls` is flagged as a suspected parser failure.
4. Capability probes (only with `caps=1`, after the model proved available):
   reasoning support (see below), structured output via
   `response_format: {type:"json_schema"}` and via `nvext: {guided_json}`
   (validated against the returned JSON, not just HTTP acceptance),
   `tool_choice: "required"`, parallel tool calls (two-city weather task
   expecting ≥2 `tool_calls`), and vision (`image_url` data URI, probed only
   for models whose card lists an image input modality).

`Reasoning (default)` records only how the DEFAULT availability response
looked — `none` there does not mean the model cannot reason (hybrid models
often keep thinking off by default or skip it on trivial prompts). The
`Reasoning Probe` capability column answers the capability question: it sends
a non-trivial prompt, then tries `chat_template_kwargs: {"thinking": true}`
and `{"enable_thinking": true}`, and reports `default_on`, `toggleable`, or
`none_observed`.

`Context (Card)` comes from model-card specs. `Context (Deployed)` comes from
the deployed-limits probe and is authoritative for what the endpoint actually
accepts — hosted deployments are sometimes smaller than the card claims (e.g.
cards stating 1M tokens while the deployment rejects above ~200K).

A separate `Probe Deployed Ctx` button (`GET /api/deep-context-probe`) targets
tested rows whose `Context (Deployed)` stayed blank. It re-sends the oversized
`max_tokens` request once: a parseable 400 fills the value directly; an
unparseable 400 proves a boundary exists, which the probe then bisects (up to
`DEEP_CONTEXT_PROBE_MAX_ATTEMPTS`, default 36, paced requests). After
convergence one padded-prompt request decides the boundary's meaning: if it
shifts with prompt size it is (context − input) and `Context (Deployed)` =
boundary + usage-reported prompt tokens; if it does not shift it is an
independent completion cap and fills `Max Output` instead.

HTTP 200 means the server clamps `max_tokens` silently, so the probe switches
to the **input side**: it sends a real filler prompt sized ~15% above the
card-stated context (capped by `DEEP_CONTEXT_INPUT_MAX_TOKENS`, default 1.2M
tokens ≈ a few MB of upload). An over-length input is rejected during request
validation — before any prefill runs — so the request costs no tokens and the
error text names the deployed limit (this is how card-says-1M models that
really run ~200K get their true value). HTTP 413 halves the payload and
retries; if the deployment unexpectedly accepts the largest payload, the cell
shows a verified `≥N` lower bound. `Untestable` remains only for endpoints
where the input side is unusable too (unparseable rejection, or 413 below the
card size).

## Rate Limiting

All outgoing NVIDIA model-invocation probe calls pass through one global pacing
gate. This applies to `/v1/chat/completions` calls used for availability,
deployed-limits, tool-support, and capability probes. Model-list and
model-metadata GET calls are not paced. The limiter intentionally uses fixed
minimum spacing between every outgoing probe call. Do not replace it with
token-bucket behavior; model probe calls must stay strictly below NVIDIA's
40 RPM free-tier cap.

| Variable | Default | Purpose |
| --- | --- | --- |
| `PROBE_RATE_LIMIT_RPM` | `39` | Main rate-limit knob, clamped below 40 RPM |
| `PROBE_MIN_INTERVAL_MS` | derived, minimum `1550` | Minimum delay between any two model probe calls |
| `PROBE_MAX_429_RETRIES` | `2` | Retries after `429 Too Many Requests` |
| `PROBE_429_BACKOFF_MS` | `10000` | Base exponential backoff when no `Retry-After` header exists |
| `PROBE_STREAM_HARD_TIMEOUT_MS` | `300000` | Absolute cap on a single streamed probe attempt (per-attempt timeouts are idle/inter-chunk timeouts) |
| `AVAILABILITY_FALLBACK_MAX_TOKENS` | `4096` | `max_tokens` used by the single availability retry |
| `AVAILABILITY_INITIAL_TIMEOUT_MS` | `30000` | Availability probe idle timeout |
| `OUTPUT_LIMIT_INITIAL_TIMEOUT_MS` | `30000` | First deployed-limits probe timeout |
| `OUTPUT_LIMIT_FALLBACK_TIMEOUT_MS` | `120000` | Fallback deployed-limits probe timeout |
| `DEEP_CONTEXT_PROBE_MAX_ATTEMPTS` | `36` | Request cap per model for the bisection probe |
| `DEEP_CONTEXT_INPUT_MAX_TOKENS` | `1200000` | Payload cap (in tokens) for the input-side deployed-context probe |

Rows that hit rate limits stay retryable instead of being cached as normal
failures, and every batch run finishes with deferred 429 retry rounds: rows
that came back rate-limited are re-tested after growing cool-down waits (60s,
120s, 240s, 480s — up to 4 rounds), so transient throttling clears itself
without manual re-testing.

## Configuration

The API key is read only from `NVIDIA_API_KEY`. The app intentionally does not
load `.env` files.

| Variable | Default | Notes |
| --- | --- | --- |
| `NVIDIA_API_KEY` | optional for catalog, required for live probes | Enables `Ping` and batch testing |
| `PORT` | `4920` | Server port |
| `MAX_CONCURRENCY` | `12` | Parallel metadata fetches |
| `REQUEST_TIMEOUT_MS` | `20000` | Generic HTTP timeout |
| `CACHE_TTL_MS` | `300000` | In-memory table cache TTL |
| `PROBE_STREAM_HARD_TIMEOUT_MS` | `300000` | Absolute cap per streamed probe attempt; per-attempt timeouts below are idle/inter-chunk timeouts |
| `AVAILABILITY_FALLBACK_MAX_TOKENS` | `4096` | `max_tokens` used by the single availability retry |
| `AVAILABILITY_INITIAL_TIMEOUT_MS` | `30000` | Availability probe idle timeout |
| `OUTPUT_LIMIT_MAX_TOKENS` | `99999999` | Oversized token budget used to trigger the deployed-limits validation error |
| `OUTPUT_LIMIT_INITIAL_TIMEOUT_MS` | `30000` | First deployed-limits probe timeout |
| `OUTPUT_LIMIT_FALLBACK_TIMEOUT_MS` | `120000` | Fallback deployed-limits probe timeout |
| `TOOL_SUPPORT_TOKEN_BUDGETS` | `128,2048` | Primary `tools` token ladder before no `max_tokens` |
| `TOOL_SUPPORT_SECONDARY_TOKEN_BUDGETS` | `512` | Forced/auto `tool_choice` token ladder before no `max_tokens` |
| `TOOL_SUPPORT_LEGACY_TOKEN_BUDGETS` | `512` | Legacy `functions` single-attempt budget |
| `TOOL_SUPPORT_MAX_ATTEMPTS` | `8` | Maximum tool-support probe requests per model |
| `TOOL_SUPPORT_INITIAL_TIMEOUT_MS` | `30000` | First tool support probe timeout |
| `TOOL_SUPPORT_FALLBACK_TIMEOUT_MS` | `120000` | Fallback tool support probe timeout |
| `CAPS_PROBE_MAX_TOKENS` | `2048` | Token budget for capability probes |
| `CAPS_PROBE_TIMEOUT_MS` | `60000` | Idle timeout for capability probes |
| `DEEP_CONTEXT_PROBE_MAX_ATTEMPTS` | `36` | Request cap per model for the deployed-context bisection |
| `DEEP_CONTEXT_INPUT_MAX_TOKENS` | `1200000` | Payload cap (tokens) for the input-side deployed-context probe |
| `POPULATE_CONCURRENCY` | `6` | Concurrent model-card fetches |
| `POPULATE_TIMEOUT_MS` | `20000` | Per model-card request timeout |
| `NGC_BASE` | `https://api.ngc.nvidia.com/v2` | NGC catalog API base |

## Commands

```bash
npm start               # start the server
npm run check           # syntax-check backend and frontend JavaScript
npm run populate-specs  # rebuild model_specs.json from NVIDIA model cards
```

## Repository Layout

| Path | Purpose |
| --- | --- |
| `nvidia-model-server-info.js` | Express server, NVIDIA API calls, live probes, cache handling |
| `public/app.js` | Browser UI, table rendering, filters, batch testing |
| `populate_specs.js` | CLI model-card fetcher for `model_specs.json` |
| `model_specs.json` | Persisted model-card specs used by the dashboard |
| `docs/MODEL_CARD_FETCH.md` | Details for the model-card fetch pipeline |

## Known Boundaries

- Claude Code commands are not shown because the hosted
  `integrate.api.nvidia.com` endpoint currently exposes `chat/completions`, not
  Anthropic-compatible `/v1/messages`.
- NVIDIA publishes no per-model limits or capability matrix for the hosted
  endpoint, and its `/v1/models` metadata carries no token-limit fields —
  the deployed context window is only discoverable by parsing the endpoint's
  own validation errors, and capabilities only by probing.
- Models that silently clamp an oversized `max_tokens` (HTTP 200 instead of a
  validation error) expose nothing on the output side; for those rows the
  regular limits probe leaves `Context (Deployed)` blank and `Max Output`
  shows `Context-bound`. `Probe Deployed Ctx` resolves them from the input
  side; only endpoints whose gateway also rejects large payloads (413) or
  emits unparseable input errors stay `Untestable`.
- Large batch tests can take time because model probe calls are paced to stay
  below NVIDIA's free-tier request limit.

## Documentation

- [USAGE.md](USAGE.md)
- [IMPLEMENTATION.md](IMPLEMENTATION.md)
- [REQUIREMENTS.md](REQUIREMENTS.md)
- [TESTING.md](TESTING.md)
- [docs/MODEL_CARD_FETCH.md](docs/MODEL_CARD_FETCH.md)

## License

MIT. See [LICENSE](LICENSE).
