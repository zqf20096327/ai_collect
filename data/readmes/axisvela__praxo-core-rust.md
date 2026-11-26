# PRAXO-CORE for Rust

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This crate is its native Rust Core: an agent loop with tool registration and dispatch, policy hooks, typed events, memory, checkpoints, context budgets, middleware, JSON Schema validation, and plugin manifest parsing. It runs in-process and does not require a hosted service.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo-core` |
| Registry | [crates.io](https://crates.io/crates/praxo-core/0.10.0) |
| Install | `cargo add praxo-core@0.10.0` |
| Source version | `0.11.0` |
| Published version | `0.10.0` |
| Source tag | `rust/v0.11.0` |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/rust/ |
| License | MIT |

## Highlights

- OpenAI-compatible model: native
- Anthropic model: native (transport seam)
- Gemini model: native (transport seam)
- MCP client: native
- Harmovela sink: native
- OpenTelemetry sink: native (transport seam)
- Subagent delegation: native
- Retriever: native

## Quick start

Install the published package:

```bash
cargo add praxo-core@0.10.0
```

```rust
use std::sync::Arc;
use praxo_core::agent::{Agent, AgentOptions, Session};
use praxo_core::model::{Message, Model, Request, Response};

struct EchoModel;

impl Model for EchoModel {
    fn generate(&self, _request: &Request) -> praxo_core::errors::Result<Response> {
        Ok(Response {
            message: Message::assistant("hello", Vec::new()),
            ..Response::default()
        })
    }
}

let agent = Agent::new(AgentOptions::new(Arc::new(EchoModel)))?;
let result = agent.run(&Session::new("session-1"), "hi")?;
println!("{} {}", result.output, result.steps);
```

See the [full Rust README](language/rust/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `openai_compat::OpenAICompatible` behind optional `http-ureq`; `parse_stream` always available |
| Anthropic model | native (transport seam) | `adapters::anthropic`; caller supplies transport; `StreamingModel` via `send_stream` |
| Gemini model | native (transport seam) | `adapters::gemini`; caller supplies transport; `StreamingModel` via `send_stream` |
| MCP client | native | `mcp::McpClient`; stdio, plus `McpClient::connect_http` over a caller-supplied `McpHttpTransport` seam for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `harmovela::Sink` |
| OpenTelemetry sink | native (transport seam) | `adapters::otel::Sink`; caller supplies OTLP/HTTP transport |
| Subagent delegation | native | `delegation::SubagentManager` |
| Retriever | native | `retriever::Document` and `Retriever` |

## Examples

Runnable examples live under [`language/rust/examples`](language/rust/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/rust/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern using published crates.io `praxo-core@0.10.0`. The parent agent may call a `delegate` tool but not the child's... |
| [checkpoint](language/rust/examples/checkpoint) | This example uses published crates.io `praxo-core@0.10.0` to keep checkpoint storage application-owned while using the SDK allowlist for payload encoding. |
| [consumer](language/rust/examples/consumer) | This starter installs the published crates.io package `praxo-core@0.10.0` and verifies an allow/deny governed tool path. |
| [event-sink](language/rust/examples/event-sink) | This example uses published crates.io `praxo-core@0.10.0` to observe agent lifecycle and tool events without coupling the agent to a logging or telemetry backend. |
| [hitl](language/rust/examples/hitl) | This example uses published crates.io `praxo-core@0.10.0` to demonstrate a write tool that requires human approval: |
| [identity-policy](language/rust/examples/identity-policy) | This example uses published crates.io `praxo-core@0.10.0` to bind a trusted principal to Core policy authorization. The application owns authentication and principal storage; Co... |
| [live-model](language/rust/examples/live-model) | This source-mode example connects the Rust Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/rust/examples/mcp) | This example uses published crates.io `praxo-core@0.10.0` with an in-process `McpHttpTransport`. It needs no server process and no network endpoint. |
| [provider-fallback](language/rust/examples/provider-fallback) | This example uses published crates.io `praxo-core@0.10.0` to fall back to a second model when the primary model call fails. |
| [representative-chain](language/rust/examples/representative-chain) | This deterministic example exercises the same application seams as the Go representative chain without a live provider or network: |
| [retry](language/rust/examples/retry) | This example uses published crates.io `praxo-core@0.10.0` to retry transient model failures without changing the agent loop. |
| [service](language/rust/examples/service) | This example embeds published crates.io `praxo-core@0.10.0` in a standard-library TCP/HTTP service. The application supplies a principal and tenant, restricts tools, and returns... |
| [session-checkpoint](language/rust/examples/session-checkpoint) | This example uses published crates.io `praxo-core@0.10.0` and saves and restores a conversation history across two agent turns. It uses the Core allowlist for payload encoding a... |
| [streaming](language/rust/examples/streaming) | This example uses published crates.io `praxo-core@0.10.0` to consume deltas while the agent loop keeps running normally. |
| [structured-output](language/rust/examples/structured-output) | This example uses published crates.io `praxo-core@0.10.0` to validate the final answer against a JSON Schema. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/rust/Tutorial`.

| Path | What it shows |
| --- | --- |
| [Tutorial](language/rust/Tutorial) | Bounded Rust examples built on the native Core. Each tutorial is a small, runnable slice with explicit non-goals and an application-owned boundary; none is a complete industry p... |
| [biodiversity-alerts](language/rust/Tutorial/biodiversity-alerts) | Classify fixed labeled observations and draft a ranger review. No production write or external system access. |
| [bug-repair](language/rust/Tutorial/bug-repair) | Reproduces a fixed bug, drafts a patch and reruns a fixture test. No PR creation or repository write. |
| [code-review](language/rust/Tutorial/code-review) | Reviews a fixed diff and dependency manifest, cites findings and uncertainty and drafts comments. No comments are posted. |
| [cold-chain](language/rust/Tutorial/cold-chain) | A bounded first slice of TL-04, not a refrigeration-control or clinical-cargo system. It computes fixed temperature excursions and drafts a review-only transfer review. No refri... |
| [construction-safety](language/rust/Tutorial/construction-safety) | A bounded first slice of BE-01, not a certified safety inspection. It reads fixed inspection labels for one site, drafts a review-only remediation checklist and records zero cer... |
| [copyright-evidence](language/rust/Tutorial/copyright-evidence) | Compare fixed authorized assets and draft an evidence packet. No production write or external system access. |
| [dlp-redaction](language/rust/Tutorial/dlp-redaction) | Inspect a fixed export and draft a review-only redaction. No production write or external system access. |
| [drone-fleet-plan](language/rust/Tutorial/drone-fleet-plan) | Simulate fixed waypoints and conflict checks, then draft a plan. No production write or external system access. |
| [fleet-map](language/rust/Tutorial/fleet-map) | Replay fixed road-topology changes and draft a reviewed map patch. No production write or external system access. |
| [household-robot](language/rust/Tutorial/household-robot) | A bounded first slice of PE-04, not a robot controller. It observes fixed robot state with freshness, drafts a bounded review-only action that requires cancel confirmation, and... |
| [iot-gateway](language/rust/Tutorial/iot-gateway) | A scoped edge tutorial over the published MIT `praxo-core` Rust crate. It reads one fixed gateway snapshot through an application-owned `GatewayAdapter` trait, asks a determinis... |
| [lab-loop](language/rust/Tutorial/lab-loop) | A bounded first slice of SC-03, not an autonomous laboratory. It replays a fixed parameter/result loop with deterministic limits and drafts review-only next parameters. No labor... |
| [leak-localization](language/rust/Tutorial/leak-localization) | A bounded first slice of CT-02, not a leak-detection or dispatch system. It ranks fixed synthetic pressure anomalies and drafts a review-only inspection list. No valve isolation... |
| [livestock-monitor](language/rust/Tutorial/livestock-monitor) | A bounded first slice of AE-01, not a veterinary or feeding-control system. It summarizes fixed animal observations and drafts a review-only veterinary request. No diagnosis, is... |
| [mining-slope](language/rust/Tutorial/mining-slope) | A bounded first slice of BE-03, not a collapse-prediction or dispatch system. It reads fixed slope displacement indicators and drafts a review-only alert. No collapse prediction... |
| [pentest-lab-review](language/rust/Tutorial/pentest-lab-review) | Inventory one allowlisted loopback lab and draft a review-only report. No production write or external system access. |
| [privacy-agent](language/rust/Tutorial/privacy-agent) | Classify fixed messages and draft a review-only deletion request. No production write or external system access. |
| [quant-risk](language/rust/Tutorial/quant-risk) | Replays fixed prices, enforces a deterministic exposure limit and drafts a review-only order. No trade or latency claim. |
| [supply-chain-review](language/rust/Tutorial/supply-chain-review) | Compare fixed manifests and draft a reviewed version pin. No production write or external system access. |
| [threat-hunting](language/rust/Tutorial/threat-hunting) | Search fixed logs and draft a cited synthetic TTP timeline. No production write or external system access. |

## Reference Applications

Complete AI-native reference applications live under `language/rust/application`.

| Path | What it shows |
| --- | --- |
| [application](language/rust/application) | A Rust edge CLI where the agent drives the primary gateway-diagnosis workflow: an operator submits an incident intent, the agent reads application-owned gateway telemetry, diagn... |

## Verify

Run the checks from `language/rust`:

```bash
cd language/rust
cargo test
cargo run --quiet --bin conformance
python api-snapshot.py --check
python -m unittest discover -s tests -p "test_*.py" -v
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/rust/README.md`](language/rust/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

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

- `language/rust/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/rust
- Registry introduction: `language/rust/REGISTRY.md`
- Machine-readable entry: `language/rust/llms.txt` and `language/rust/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-rust
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical Rust source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
