# PRAXO-CORE for Delphi / Free Pascal

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native Delphi / Free Pascal Core: an in-process agent loop with tools, policy, memory, events, checkpoints, context, and middleware helpers. It is implemented in Object Pascal and does not call Go or another language Core.

## At a glance

| Field | Value |
| --- | --- |
| Package | `PRAXO-CORE` |
| Registry | [OPM / GitHub release](https://github.com/axisvela/praxo-core/releases/tag/delphi%2Fv0.7.0) |
| Install | `OPM package or release archive` |
| Source version | `0.9.0` |
| Published version | `0.2.1` |
| Source tag | `delphi/v0.9.0` |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/delphi/ |
| License | MIT |

## Highlights

- OpenAI-compatible model: native
- Anthropic model: native
- Gemini model: native
- MCP client: native
- Harmovela sink: native
- OpenTelemetry sink: native (transport seam)
- Subagent delegation: native (synchronous seam)
- Retriever: native

## Quick start

Install the published package:

```text
OPM package or release archive
```

See the [full Delphi / Free Pascal README](language/delphi/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `TPraxoOpenAIAdapter` with FPC HTTP transport; SSE streaming reassembly |
| Anthropic model | native | `TPraxoAnthropicAdapter`; FPC HTTP transport; `GenerateStream` reassembles Anthropic SSE |
| Gemini model | native | `TPraxoGeminiAdapter`; FPC HTTP transport; `GenerateStream` reassembles Gemini SSE |
| MCP client | native | `TPraxoMcpClient`; stdio and `TPraxoHttpMcpTransport` for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `TPraxoHarmovelaSink` |
| OpenTelemetry sink | native (transport seam) | `TPraxoOtelSink`; caller supplies `TPraxoOtelTransport` |
| Subagent delegation | native (synchronous seam) | `TPraxoSubagentManager.Run`; no asynchronous manager |
| Retriever | native | `TPraxoDocument`, `TPraxoRetriever`, `PraxoRetrieveDocuments` |

## Examples

Runnable examples live under [`language/delphi/examples`](language/delphi/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/delphi/examples/advanced-delegation) | Application-level parent/child delegation plus six governance negative checks. |
| [checkpoint](language/delphi/examples/checkpoint) | This example uses the Delphi Core checkpoint allowlist for a registered payload round trip. |
| [consumer](language/delphi/examples/consumer) | This example uses the source Delphi/Free Pascal Core with a deterministic host, one registered `record` tool, an explicit tool scope, and a policy that permits only the `public`... |
| [event-sink](language/delphi/examples/event-sink) | This example uses Delphi Core sink composition to fan out events and filter the tool-only stream. |
| [hitl](language/delphi/examples/hitl) | This example configures `TPraxoAgentOptions.InterruptOn` and `OnInterruptDecision` for approve, edit-with-reauthorization, and respond decisions. It is a deterministic self-chec... |
| [identity-policy](language/delphi/examples/identity-policy) | This example binds a trusted principal to policy decisions and rejects missing, role-mismatched, and tenant-mismatched actions. |
| [live-model](language/delphi/examples/live-model) | This example connects the Delphi/Free Pascal Core to an OpenAI-compatible endpoint through `TPraxoOpenAIAdapter` and registers one low-risk `get_time` tool with a small JSON Sch... |
| [mcp](language/delphi/examples/mcp) | This example uses a caller-owned in-process transport with the Delphi MCP client. |
| [provider-fallback](language/delphi/examples/provider-fallback) | This example calls a fallback only after the primary fails and preserves the primary failure when both fail. |
| [representative-chain](language/delphi/examples/representative-chain) | Deterministic representative chain covering MCP record, final-argument authorization, governed child delegation, OTel/Harmovela events, and an edited denial with zero effects. |
| [retry](language/delphi/examples/retry) | This example retries a transient failure with a bounded attempt count and keeps the exhausted failure state. |
| [service](language/delphi/examples/service) | This example defines a transport-neutral request handler with health, principal, and run cases. |
| [session-checkpoint](language/delphi/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns. It uses the checkpoint allowlist as a teaching in-memory store keyed by session id; production sto... |
| [streaming](language/delphi/examples/streaming) | This example accumulates streamed chunks and checks that they reconstruct the final output. |
| [structured-output](language/delphi/examples/structured-output) | This example validates a final JSON answer against a schema and rejects invalid output. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/delphi/Tutorial`.

| Path | What it shows |
| --- | --- |
| [Tutorial](language/delphi/Tutorial) | ﻿# Delphi / Free Pascal Tutorials |
| [hvac-settings](language/delphi/Tutorial/hvac-settings) | A bounded first slice of BE-02, not a building-management system. It reads a fixed building environment and drafts a review-only settings plan using the source Delphi/Free Pasca... |
| [legacy-migration](language/delphi/Tutorial/legacy-migration) | A bounded first slice of [SE-03](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an automatic production migration. It inventories fixed legacy modu... |
| [rpa-reconciliation](language/delphi/Tutorial/rpa-reconciliation) | A bounded first slice of [OP-04](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a production RPA platform. It reconciles a fixed purchase order and... |
| [tax-review](language/delphi/Tutorial/tax-review) | A bounded tax-planning tutorial. It reads a fixed ledger, computes taxable income and tax due, then drafts a review-only filing. No filing is submitted and no tax advice is given. |

## Verify

Run the checks from `language/delphi`:

```bash
python language/delphi/run-tests.py
python language/delphi/api-snapshot.py --check
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/delphi/README.md`](language/delphi/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

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

- `language/delphi/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/delphi
- Registry introduction: `language/delphi/REGISTRY.md`
- Machine-readable entry: `language/delphi/llms.txt` and `language/delphi/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-delphi
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical Delphi / Free Pascal source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
