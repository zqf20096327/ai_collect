# PRAXO-CORE for Rust

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This crate is its native Rust Core: an agent loop with tool registration and dispatch, policy hooks, typed events, memory, checkpoints, context budgets, middleware, JSON Schema validation, and plugin manifest parsing. It runs in-process and does not require a hosted service.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo-core` |
| Registry | [crates.io](https://crates.io/crates/praxo-core/0.9.2) |
| Install | `cargo add praxo-core@0.9.2` |
| Source version | `0.9.2` |
| Published version | `0.9.2` |
| Source tag | `rust/v0.9.2` |
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
cargo add praxo-core@0.9.2
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
| Anthropic model | native (transport seam) | `adapters::anthropic`; caller supplies transport |
| Gemini model | native (transport seam) | `adapters::gemini`; caller supplies transport |
| MCP client | native | `mcp::McpClient`; stdio, plus `McpClient::connect_http` over a caller-supplied `McpHttpTransport` seam for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `harmovela::Sink` |
| OpenTelemetry sink | native (transport seam) | `adapters::otel::Sink`; caller supplies OTLP/HTTP transport |
| Subagent delegation | native | `delegation::SubagentManager` |
| Retriever | native | `retriever::Document` and `Retriever` |

## Examples

Runnable examples live under [`language/rust/examples`](language/rust/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/rust/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern using published crates.io `praxo-core@0.9.2`. The parent agent may call a `delegate` tool but not the child's... |
| [checkpoint](language/rust/examples/checkpoint) | This example uses published crates.io `praxo-core@0.9.2` to keep checkpoint storage application-owned while using the SDK allowlist for payload encoding. |
| [consumer](language/rust/examples/consumer) | This starter installs the published crates.io package `praxo-core@0.9.2` and verifies an allow/deny governed tool path. |
| [event-sink](language/rust/examples/event-sink) | This example uses published crates.io `praxo-core@0.9.2` to observe agent lifecycle and tool events without coupling the agent to a logging or telemetry backend. |
| [hitl](language/rust/examples/hitl) | This example uses published crates.io `praxo-core@0.9.2` to demonstrate a write tool that requires human approval: |
| [identity-policy](language/rust/examples/identity-policy) | This example uses published crates.io `praxo-core@0.9.2` to bind a trusted principal to Core policy authorization. The application owns authentication and principal storage; Cor... |
| [live-model](language/rust/examples/live-model) | This source-mode example connects the Rust Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/rust/examples/mcp) | This example uses published crates.io `praxo-core@0.9.2` with an in-process `McpHttpTransport`. It needs no server process and no network endpoint. |
| [provider-fallback](language/rust/examples/provider-fallback) | This example uses published crates.io `praxo-core@0.9.2` to fall back to a second model when the primary model call fails. |
| [representative-chain](language/rust/examples/representative-chain) | This deterministic example exercises the same application seams as the Go representative chain without a live provider or network: |
| [retry](language/rust/examples/retry) | This example uses published crates.io `praxo-core@0.9.2` to retry transient model failures without changing the agent loop. |
| [service](language/rust/examples/service) | This example embeds published crates.io `praxo-core@0.9.2` in a standard-library TCP/HTTP service. The application supplies a principal and tenant, restricts tools, and returns... |
| [session-checkpoint](language/rust/examples/session-checkpoint) | This example uses published crates.io `praxo-core@0.9.2` and saves and restores a conversation history across two agent turns. It uses the Core allowlist for payload encoding an... |
| [streaming](language/rust/examples/streaming) | This example uses published crates.io `praxo-core@0.9.2` to consume deltas while the agent loop keeps running normally. |
| [structured-output](language/rust/examples/structured-output) | This example uses published crates.io `praxo-core@0.9.2` to validate the final answer against a JSON Schema. |

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
