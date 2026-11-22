# PRAXO-CORE for Objective-C

Objective-C is a native Core implementation with source tag `objc/v0.7.0`. It passes all eleven shared vector groups and includes the native agent loop, context compaction, memory store, path policy, checkpoint allowlist, tool selection, tool-call parsing, argument-aware policy, and opt-in PII redaction, structured output validation, call limits, and human-in-the-loop interrupts. Vector coverage does not establish full Core parity or production readiness.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo-core-objc` |
| Registry | Source |
| Build | See README/SETUP.md |
| Source version | `0.7.0` |
| Published version | not published |
| Source tag | `objc/v0.7.0` |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/objc/ |
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

This implementation is source-only. Follow the build instructions in [`language/objc/README.md`](language/objc/README.md).

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `PXROpenAIGenerate` with injectable transport; SSE streaming reassembly |
| Anthropic model | native | `PXRAnthropicGenerate` with injectable transport; `PXRAnthropicGenerateStream` reassembles Anthropic SSE |
| Gemini model | native | `PXRGeminiGenerate` with injectable transport; `PXRGeminiGenerateStream` reassembles Gemini SSE |
| MCP client | native | `PXRMcpClient`; stdio and `PXRHttpMcpTransport` for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `PraxoHarmovela` |
| OpenTelemetry sink | native (transport seam) | `PXROtelSink`; caller supplies `PXROtelTransport` |
| Subagent delegation | native (synchronous seam) | `PXRSubagentRun`; no asynchronous manager |
| Retriever | native | `PXDocument`, `PXRetriever`, `PXRetrieveDocuments` |

## Examples

Runnable examples live under [`language/objc/examples`](language/objc/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/objc/examples/advanced-delegation) | Application-level parent/child delegation plus six governance negative checks. |
| [checkpoint](language/objc/examples/checkpoint) | This example uses the Objective-C Core checkpoint allowlist for a registered payload round trip. |
| [consumer](language/objc/examples/consumer) | This starter uses a deterministic model and an in-memory tool. It does not use the network or a model service. |
| [event-sink](language/objc/examples/event-sink) | This example uses Objective-C Core sink composition to fan out events and filter the tool-only stream. |
| [hitl](language/objc/examples/hitl) | This example demonstrates a write tool that requires human approval: |
| [identity-policy](language/objc/examples/identity-policy) | This example binds a trusted principal to policy decisions and rejects missing, role-mismatched, and tenant-mismatched actions. |
| [live-model](language/objc/examples/live-model) | This example connects the Objective-C Core to an OpenAI-compatible endpoint through `PXROpenAIModelCreate`, registers a `get_time(zone)` tool with a small JSON Schema, and restr... |
| [mcp](language/objc/examples/mcp) | This example uses a caller-owned in-process transport with the Objective-C MCP client. |
| [provider-fallback](language/objc/examples/provider-fallback) | This example calls a fallback only after the primary fails and preserves the primary failure when both fail. |
| [representative-chain](language/objc/examples/representative-chain) | Deterministic representative chain covering MCP record, final-argument authorization, governed child delegation, OTel/Harmovela events, and an edited denial with zero effects. |
| [retry](language/objc/examples/retry) | This example retries a transient failure with a bounded attempt count and keeps the exhausted failure state. |
| [service](language/objc/examples/service) | This example defines a transport-neutral request handler with health, principal, and run cases. |
| [session-checkpoint](language/objc/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns. It uses `PXRSessionCreate`, `PXRAgentRun`, `PXRMessageWire`, and the checkpoint allowlist with a t... |
| [streaming](language/objc/examples/streaming) | This example accumulates streamed chunks and checks that they reconstruct the final output. |
| [structured-output](language/objc/examples/structured-output) | This example validates a final JSON answer against a schema and rejects invalid output. |

## Verify

Run the checks from `language/objc`:

```bash
python language/objc/api-snapshot.py --check
python language/objc/run-tests.py
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/objc/README.md`](language/objc/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

## Community

- X: <https://x.com/axisvela>
- Weibo: <https://weibo.com/u/1936025761>

## Repository layout

- `language/objc/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/objc
- Registry introduction: `language/objc/REGISTRY.md`
- Machine-readable entry: `language/objc/llms.txt` and `language/objc/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-objc
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical Objective-C source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
