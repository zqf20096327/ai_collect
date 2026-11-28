# PRAXO-CORE for R

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native R Core: an in-process agent loop with tools, policy, events, memory, checkpoints, middleware, and JSON Schema validation, implemented in base R.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxocore` |
| Registry | [r-universe](https://axisvela.r-universe.dev/praxocore) |
| Install | `install.packages("praxocore", repos = "https://axisvela.r-universe.dev")` |
| Source version | `0.12.0` |
| Published version | `0.12.0` |
| Publication status | published on r-universe; CRAN not published |
| Canonical source tag | [`r/v0.12.0`](https://github.com/axisvela/praxo-core/tree/r/v0.12.0) |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/r/ |
| License | MIT |

## Highlights

- OpenAI-compatible model: native
- Anthropic model: native (transport seam)
- Gemini model: native (transport seam)
- MCP client: native (transport seam)
- Harmovela sink: native
- OpenTelemetry sink: native (transport seam)
- Subagent delegation: native (synchronous seam)
- Retriever: native

## Quick start

Install the published package:

```r
install.packages("praxocore", repos = "https://axisvela.r-universe.dev")
```

```r
model <- function(request) response(message(roles$assistant, "hello"))
result <- agent_run(model, "hi")
cat(result$output)
```

See the [full R README](language/r/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `openai_compatible` adapter; `openai_compatible_streaming_model` reassembles SSE content, tool calls, usage, and finish reason |
| Anthropic model | native (transport seam) | `anthropic`; caller may supply `transport`; `anthropic_streaming_model` reassembles SSE |
| Gemini model | native (transport seam) | `gemini`; caller may supply `transport`; SSE streaming |
| MCP client | native (transport seam) | `mcp_client`; base R needs caller-supplied transport for stdio |
| Harmovela sink | native | `harmovela_sink` |
| OpenTelemetry sink | native (transport seam) | `otel_sink`; caller supplies OTLP/HTTP transport |
| Subagent delegation | native (synchronous seam) | `subagent_run`; no asynchronous manager |
| Retriever | native | `document`, `func_retriever`, `retriever_retrieve` |

## Examples

Runnable examples live under [`language/r/examples`](language/r/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/r/examples/advanced-delegation) | This example adds application-level governed delegation checks for the R Core. |
| [checkpoint](language/r/examples/checkpoint) | This example uses the R Core checkpoint allowlist to encode and decode only registered payload types. |
| [consumer](language/r/examples/consumer) | This starter installs the published `praxocore` package from r-universe and verifies an allow/deny governed tool path. |
| [event-sink](language/r/examples/event-sink) | This example uses the R Core sink composition to fan out lifecycle and tool events and filter the tool-only stream. |
| [hitl](language/r/examples/hitl) | This example demonstrates a write tool that requires human approval: |
| [identity-policy](language/r/examples/identity-policy) | This example binds a trusted principal to policy decisions and rejects missing, inactive, role-mismatched, and tenant-mismatched actions. |
| [live-model](language/r/examples/live-model) | This example connects the R Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/r/examples/mcp) | This example uses a caller-owned in-process transport with the R MCP client. It covers initialize, `tools/list`, and `tools/call` without a server process. |
| [provider-fallback](language/r/examples/provider-fallback) | This example calls a fallback only after the primary fails and preserves the primary failure when both fail. |
| [representative-chain](language/r/examples/representative-chain) | This deterministic example exercises the same application seams as the Go representative chain without a live provider or network: |
| [retry](language/r/examples/retry) | This example retries a transient failure with a bounded attempt count and keeps the exhausted failure state. |
| [service](language/r/examples/service) | This example defines a transport-neutral request handler boundary with health, principal, and run cases. Wire it into any R HTTP server. |
| [session-checkpoint](language/r/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns using the Core checkpoint allowlist. |
| [streaming](language/r/examples/streaming) | This example forwards model deltas through the R Core and checks that the deltas reconstruct the final output. |
| [structured-output](language/r/examples/structured-output) | This example validates a final JSON answer against a schema and rejects invalid output. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/r/Tutorial`. Planning context: [Tutorial Plan](https://axisvela.github.io/praxo-core/getting-started/tutorial-plan/), [100 candidate agent scenarios](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), and [Tutorial Catalog](https://axisvela.github.io/praxo-core/getting-started/tutorial-catalog/).

| Path | What it shows |
| --- | --- |
| [Tutorial](language/r/Tutorial) | Application tutorials live in `Tutorial/`, alongside focused `language/go/examples/`. |
| [budget-review](language/r/Tutorial/budget-review) | A bounded first slice of CT-07, not an official audit. It computes budget execution for a fixed synthetic programme, explains a flagged variance and drafts a review-only perform... |
| [clinical-guidelines](language/r/Tutorial/clinical-guidelines) | Retrieves fixed guideline citations and abstains when evidence is missing. No diagnosis or treatment decision. |
| [compliance-tracking](language/r/Tutorial/compliance-tracking) | Compares fixed policy versions and drafts review-only remediation. No audit conclusion or submission. |
| [data-quality](language/r/Tutorial/data-quality) | A native R analytics tutorial. The Agent has one fixed tool, `summarize_dataset`, which computes statistics over a synthetic data frame. The deterministic model returns the comp... |
| [executive-brief](language/r/Tutorial/executive-brief) | Computes fixed metric deltas and cites them. No causal attribution or action. |
| [fire-spread](language/r/Tutorial/fire-spread) | A bounded first slice of AE-02, not a fire-warning or dispatch system. It computes fixed weather/fuel spread indicators in native R and drafts a review-only spread report. No op... |
| [hedge-plan](language/r/Tutorial/hedge-plan) | A bounded first slice of AE-04, not a trading or financial-advice system. It computes fixed farm exposure and scenario margins in native R and drafts a review-only hedging plan.... |
| [marketing-segmentation](language/r/Tutorial/marketing-segmentation) | A native R Core tutorial for campaign segmentation. It computes per-segment statistics over a fixed customer fixture, identifies the highest-value segment, and drafts a review-o... |
| [pollution-tracing](language/r/Tutorial/pollution-tracing) | Compares fixed sensor and wind records and drafts investigation hypotheses. No causal or enforcement finding. |
| [property-forecast](language/r/Tutorial/property-forecast) | A bounded first slice of BE-05, not a valuation or investment-advice system. It computes fixed site metrics in native R, shows forecast assumptions and drafts a review-only fore... |
| [wealth-analysis](language/r/Tutorial/wealth-analysis) | A native R Core tutorial for review-only portfolio analysis. It computes weighted risk and concentration over a fixed `acct-100` fixture, recommends a rebalance, and drafts a re... |
| [weather-anomaly](language/r/Tutorial/weather-anomaly) | A bounded first slice of SC-05, not an operational forecast or warning service. It computes fixed time-series anomalies in native R and drafts a review-only notice. No operation... |

## Reference Applications

No accepted end-to-end reference application is recorded for this language yet. Candidate goals are tracked in the [Reference Application Portfolio](https://axisvela.github.io/praxo-core/project/roadmap/#reference-application-portfolio).

## Verify

Run the checks from `language/r`:

```bat
Rscript r\conformance\run.R
Rscript r\api-snapshot.R --check
Rscript r\tests\run_tests.R
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/r/README.md`](language/r/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

## Community

- X: <https://x.com/axisvela>
- Weibo: <https://weibo.com/u/1936025761>
- LinkedIn: <https://www.linkedin.com/company/axisvela/>
- Facebook: <https://www.facebook.com/profile.php?id=61596905732406>
- YouTube: <https://www.youtube.com/@axisvela>
- Discord: <https://discord.com/channels/1575163993767809064/1575164343148875977>
- GitHub Discussions: <https://github.com/axisvela/praxo-core/discussions>
- GitHub Issues: <https://github.com/axisvela/praxo-core/issues>
- Documentation: <https://axisvela.github.io/praxo-core/>
- Architect: <https://axisvela.architect.pub>

## Repository layout

- `language/r/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/r
- Registry introduction: `language/r/REGISTRY.md`
- Machine-readable entry: `language/r/llms.txt` and `language/r/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-r
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical R source. The monorepo remains the source of truth and the release workflow source. The mirror's `main` branch tracks current source, not a release snapshot. Source tags refer to the canonical monorepo and are not necessarily present in this mirror; syncing the branch does not publish mirror tags or registry packages.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
