# PRAXO-CORE for Dart

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native Dart Core: an agent loop with tool registration and dispatch, policy hooks, typed events, memory, checkpoints, context budgets, middleware, OTel and Harmovela sinks, MCP, retriever and synchronous delegation seams, JSON Schema validation, and plugin manifest parsing. It runs in-process and does not require a hosted service.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo_core` |
| Registry | [pub.dev](https://pub.dev/packages/praxo_core/versions/0.8.0) |
| Install | `dart pub add praxo_core:0.8.0` |
| Source version | `0.8.0` |
| Published version | `0.8.0` |
| Publication status | published |
| Canonical source tag | [`dart/v0.8.0`](https://github.com/axisvela/praxo-core/tree/dart/v0.8.0) |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/dart/ |
| License | MIT |

## Highlights

- Publishing setup: [PUBLISHING.md](https://github.com/axisvela/praxo-core/blob/main/language/dart/PUBLISHING.md)

## Quick start

Install the published package:

```bash
dart pub add praxo_core:0.8.0
```

```dart
import 'package:praxo_core/praxo_core.dart';

void main() {
  final agent = Agent(AgentOptions(StaticModel('hello')));
  final result = agent.run(const Session(id: 'demo'), 'hello');
  print(result.output);
}
```

See the [full Dart README](language/dart/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `OpenAiCompatibleModel` with sync and async transport paths; `generateStream` reassembles SSE content, tool calls, usage, and finish reason |
| Anthropic model | native | `AnthropicModel` with sync and async transport paths; `generateStream` reassembles Anthropic SSE |
| Gemini model | native | `GeminiModel`; `generateStream` reassembles Gemini SSE |
| MCP client | native | `McpClient`; stdio, plus `McpStreamableHttpTransport` for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `HarmovelaSink` |
| OpenTelemetry sink | native (transport seam) | `OtelSink`; caller supplies `OtelTransport` |
| Subagent delegation | native (synchronous seam) | `SubagentManager.run`; no asynchronous manager |
| Retriever | native | `Document`, `FuncRetriever`, `retrieveDocuments` |

## Examples

Runnable examples live under [`language/dart/examples`](language/dart/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/dart/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern combined with six governance negative checks. |
| [checkpoint](language/dart/examples/checkpoint) | This example uses the Dart Core checkpoint allowlist for a registered payload round trip. |
| [consumer](language/dart/examples/consumer) | This example uses the source Dart Core with a deterministic model, one registered `record` tool, an explicit tool scope, and a policy that permits only the `public` target. It d... |
| [event-sink](language/dart/examples/event-sink) | This example uses Dart Core sink composition to fan out events and filter the tool-only stream. |
| [hitl](language/dart/examples/hitl) | This example demonstrates a write tool that requires human approval: |
| [identity-policy](language/dart/examples/identity-policy) | This example binds a trusted principal to policy decisions and rejects missing, role-mismatched, and tenant-mismatched actions. |
| [live-model](language/dart/examples/live-model) | This example connects the Dart Core to an OpenAI-compatible endpoint through `OpenAICompatibleModel` and registers one low-risk `get_time` tool with a small JSON Schema. The pol... |
| [mcp](language/dart/examples/mcp) | This example uses a caller-owned in-process transport with the Dart MCP client. |
| [provider-fallback](language/dart/examples/provider-fallback) | This example calls a fallback only after the primary fails and preserves the primary failure when both fail. |
| [representative-chain](language/dart/examples/representative-chain) | This deterministic example exercises the same application seams as the Go representative chain without a live provider: |
| [retry](language/dart/examples/retry) | This example retries a transient failure with a bounded attempt count and keeps the exhausted failure state. |
| [service](language/dart/examples/service) | This example defines a transport-neutral request handler with health, principal, and run cases. |
| [session-checkpoint](language/dart/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns. It uses the Core allowlist for payload encoding and a teaching in-memory payload. |
| [streaming](language/dart/examples/streaming) | This example accumulates streamed chunks and checks that they reconstruct the final output. |
| [structured-output](language/dart/examples/structured-output) | This example validates a final JSON answer against a schema and rejects invalid output. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/dart/Tutorial`. Planning context: [Tutorial Plan](https://axisvela.github.io/praxo-core/getting-started/tutorial-plan/), [100 candidate agent scenarios](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), and [Tutorial Catalog](https://axisvela.github.io/praxo-core/getting-started/tutorial-catalog/).

| Path | What it shows |
| --- | --- |
| [Tutorial](language/dart/Tutorial) | - [Meeting Coordination (OP-02)](https://github.com/axisvela/praxo-core/blob/main/language/dart/Tutorial/meeting-coordination/README.md): source Dart Core, fixed calendar evidence and a review-only minutes/task draft; no invites or calendar writes. - [Onboarding Plan (OP-06)](https://github.com/axisvela/praxo-core/blob/main/language/dart/Tutorial/onboarding-plan/README.md): source Dart Core, fixed employee profile and a review-only learning path; no permissions or provisioning. |
| [audiobook-production](language/dart/Tutorial/audiobook-production) | A bounded first slice of [MD-06](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an audio-production pipeline. It reads a fixed licensed book fixture and drafts a review-only production plan with character and mixing cues. No synthesized audio, voice cloning or rights guarantee. |
| [cbt-exercise](language/dart/Tutorial/cbt-exercise) | A bounded first slice of [HC-05](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a therapist or crisis service. It walks a fixed synthetic CBT exercise, keeps an explicit `human_review` escalation branch and drafts a review-only summary. No live session, diagnosis, therapist replacement or unsupervised crisis handling. |
| [chronic-care](language/dart/Tutorial/chronic-care) | A bounded first slice of [HC-02](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a clinical decision system. It summarizes fixed synthetic wearable trends and routes a review-only care alert. No dosage change, individualized treatment change or live device feed. |
| [digital-twin-memory](language/dart/Tutorial/digital-twin-memory) | A bounded first slice of [OG-06](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a personal memory hub. It stores one consent-scoped synthetic memory, recalls only that scope and confirms deletion. No real inbox, passwords, cross-app access or unrestricted recall. |
| [marketing-segments](language/dart/Tutorial/marketing-segments) | Fixed customer spend produces two high-value customers and a review-only campaign draft. No customer records, sends or live model. |
| [meeting-coordination](language/dart/Tutorial/meeting-coordination) | A bounded first slice of [OP-02](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not full multi-party scheduling or calendar control. It reads a fixed calendar fixture, checks conflicts, and drafts review-only minutes and tasks. This uses the source Dart Core with a relative import; no network, credentials or packages are required. |
| [onboarding-plan](language/dart/Tutorial/onboarding-plan) | A bounded first slice of [OP-06](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an HR or permissions system. It reads a fixed employee profile and drafts a review-only learning path. No account provisioning, permissions or live model are used. |
| [travel-booking](language/dart/Tutorial/travel-booking) | Fixed trip inventory produces a review-only fare hold. No payment, ticketing or inventory write. |
| [waste-collection](language/dart/Tutorial/waste-collection) | A bounded first slice of [CT-06](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a fleet-dispatch system. It reads a fixed collection queue and drafts a review-only schedule under vehicle limits. No vehicle commands, live telemetry or live model. |

## Reference Applications

No accepted end-to-end reference application is recorded for this language yet. Candidate goals are tracked in the [Reference Application Portfolio](https://axisvela.github.io/praxo-core/project/roadmap/#reference-application-portfolio).

## Verify

Run the checks from `language/dart`:

```bash
dart run conformance/run.dart
python api-snapshot.py --check
dart run test/run.dart
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/dart/README.md`](language/dart/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

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

- `language/dart/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/dart
- Registry introduction: `language/dart/REGISTRY.md`
- Machine-readable entry: `language/dart/llms.txt` and `language/dart/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-dart
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical Dart source. The monorepo remains the source of truth and the release workflow source. The mirror's `main` branch tracks current source, not a release snapshot. Source tags refer to the canonical monorepo and are not necessarily present in this mirror; syncing the branch does not publish mirror tags or registry packages.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
