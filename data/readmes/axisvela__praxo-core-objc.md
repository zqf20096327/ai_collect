# PRAXO-CORE for Objective-C

Objective-C is a native Core implementation with source tag `objc/v0.8.0`. It passes all eleven shared vector groups and includes the native agent loop, context compaction, memory store, path policy, checkpoint allowlist, tool selection, tool-call parsing, argument-aware policy, and opt-in PII redaction, structured output validation, call limits, and human-in-the-loop interrupts. Vector coverage does not establish full Core parity or production readiness.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo-core-objc` |
| Registry | Source |
| Build | See README/SETUP.md |
| Source version | `0.8.0` |
| Published version | not published |
| Publication status | source-only |
| Canonical source tag | [`objc/v0.8.0`](https://github.com/axisvela/praxo-core/tree/objc/v0.8.0) |
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

No published package is available. Follow the source build instructions in [`language/objc/README.md`](language/objc/README.md).

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

## Scenario Tutorials

Scenario-oriented tutorials live under `language/objc/Tutorial`. Planning context: [Tutorial Plan](https://axisvela.github.io/praxo-core/getting-started/tutorial-plan/), [100 candidate agent scenarios](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), and [Tutorial Catalog](https://axisvela.github.io/praxo-core/getting-started/tutorial-catalog/).

| Path | What it shows |
| --- | --- |
| [Tutorial](language/objc/Tutorial) | - [Privacy Agent (PE-03)](https://github.com/axisvela/praxo-core/blob/main/language/objc/Tutorial/privacy-agent/README.md): source Objective-C Core, fixed message-exposure classification and a review-only deletion request; no password handling, account access or deletion execution. - [Chronic Care (HC-02)](https://github.com/axisvela/praxo-core/blob/main/language/objc/Tutorial/chronic-care/README.md): fixed wearable trends and a review-only alert; no dosage or individualized treatment change. - [DLP Redaction (CY-06)](https://github.com/axisvela/praxo-core/blob/main/language/objc/Tutorial/dlp-redaction/README.md): fixed export inspection and a review-only redaction draft; no encryption or DLP completeness claim. - [Digital Twin Memory (OG-06)](https://github.com/axisvela/praxo-core/blob/main/language/objc/Tutorial/digital-twin-memory/README.md): consent-scoped fixed memories with provenance and one deletion; no inbox or password access. |
| [chronic-care](language/objc/Tutorial/chronic-care) | Summarizes a fixed wearable trend and drafts a review-only care alert. No dosage or individualized treatment change. |
| [digital-twin-memory](language/objc/Tutorial/digital-twin-memory) | Recalls fixed consent-scoped memories with provenance, then deletes one scope. No real inbox, passwords or unrestricted recall. |
| [dlp-redaction](language/objc/Tutorial/dlp-redaction) | Inspects a fixed export for sensitive fields and drafts a review-only redaction. No encryption, DLP completeness or sharing claim. |
| [privacy-agent](language/objc/Tutorial/privacy-agent) | A bounded first slice of [PE-03](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a password manager or data-deletion service. It classifies a fixed message fixture for sensitive exposure and drafts a review-only deletion request. This uses the source Objective-C Core; no network, credentials or additional frameworks beyond Foundation are required. |

## Reference Applications

No accepted end-to-end reference application is recorded for this language yet. Candidate goals are tracked in the [Reference Application Portfolio](https://axisvela.github.io/praxo-core/project/roadmap/#reference-application-portfolio).

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
- LinkedIn: <https://www.linkedin.com/company/axisvela/>
- Facebook: <https://www.facebook.com/profile.php?id=61596905732406>
- YouTube: <https://www.youtube.com/@axisvela>
- Discord: <https://discord.com/channels/1575163993767809064/1575164343148875977>
- GitHub Discussions: <https://github.com/axisvela/praxo-core/discussions>
- GitHub Issues: <https://github.com/axisvela/praxo-core/issues>
- Documentation: <https://axisvela.github.io/praxo-core/>
- Architect: <https://axisvela.architect.pub>

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

This repository is a discovery mirror of the canonical Objective-C source. The monorepo remains the source of truth and the release workflow source. The mirror's `main` branch tracks current source, not a release snapshot. Source tags refer to the canonical monorepo and are not necessarily present in this mirror; syncing the branch does not publish mirror tags or registry packages.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
