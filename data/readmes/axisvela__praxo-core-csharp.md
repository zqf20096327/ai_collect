# PRAXO-CORE for C#

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native .NET Core: an agent loop with tool registration and dispatch, policy hooks, typed events, memory, checkpoints, context budgets, middleware, JSON Schema validation, and plugin manifest parsing. It runs in-process and does not require a hosted service.

## At a glance

| Field | Value |
| --- | --- |
| Package | `Praxo.Core` |
| Registry | [NuGet](https://www.nuget.org/packages/Praxo.Core/0.11.1) |
| Install | `dotnet add package Praxo.Core --version 0.11.1` |
| Source version | `0.11.1` |
| Published version | `0.11.1` |
| Publication status | published |
| Canonical source tag | [`csharp/v0.11.1`](https://github.com/axisvela/praxo-core/tree/csharp/v0.11.1) |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/csharp/ |
| License | MIT |

## Highlights

- OpenAI-compatible model: native
- Anthropic model: native
- Gemini model: native
- MCP client: native
- Harmovela sink: native
- OpenTelemetry sink: native (transport seam)
- Subagent delegation: native
- Retriever: native

## Quick start

Install the published package:

```bash
dotnet add package Praxo.Core --version 0.11.1
```

```csharp
using Praxo.Core;

var model = new StaticModel("hello");
var agent = new Agent(new AgentOptions(model));
var result = agent.Run(new Session("demo"), "hello");
Console.WriteLine(result.Output);
```

See the [full C# README](language/csharp/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `Praxo.Core.OpenAiCompatible` |
| Anthropic model | native | `Praxo.Core.AnthropicModel`; SSE streaming reassembly |
| Gemini model | native | `Praxo.Core.GeminiModel`; SSE streaming |
| MCP client | native | `Praxo.Core.Adapters.McpClient`; stdio, plus `McpStreamableHttpTransport` for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `Praxo.Core.HarmovelaSink` |
| OpenTelemetry sink | native (transport seam) | `Praxo.Core.OtelSink`; caller supplies OTLP/HTTP transport |
| Subagent delegation | native | `Praxo.Core.Delegation.SubagentManager` |
| Retriever | native | `Praxo.Core.Retriever.Document` and `Retriever` |

## Examples

Runnable examples live under [`language/csharp/examples`](language/csharp/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/csharp/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern using published NuGet `Praxo.Core==0.11.1`. The parent agent may call a `delegate` tool but not the child's `r... |
| [checkpoint](language/csharp/examples/checkpoint) | This example uses published NuGet `Praxo.Core==0.11.1` to keep checkpoint storage application-owned while using the SDK allowlist for payload encoding. |
| [consumer](language/csharp/examples/consumer) | This starter installs the published NuGet package `Praxo.Core==0.11.1` and verifies an allow/deny governed tool path. |
| [event-sink](language/csharp/examples/event-sink) | This example uses published NuGet `Praxo.Core==0.11.1` to observe agent lifecycle and tool events without coupling the agent to a logging or telemetry backend. |
| [hitl](language/csharp/examples/hitl) | This example uses published NuGet `Praxo.Core==0.11.1` to demonstrate a write tool that requires human approval: |
| [identity-policy](language/csharp/examples/identity-policy) | This example uses published NuGet `Praxo.Core==0.11.1` to bind a trusted principal to Core policy authorization. The application owns authentication and principal storage; Core... |
| [live-model](language/csharp/examples/live-model) | This example uses published NuGet `Praxo.Core==0.11.1` to connect the C# Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/csharp/examples/mcp) | This example uses published NuGet `Praxo.Core==0.11.1` with an in-process MCP transport. It exercises the same `initialize`, `tools/list`, and `tools/call` flow as a stdio sessi... |
| [provider-fallback](language/csharp/examples/provider-fallback) | This example uses published NuGet `Praxo.Core==0.11.1` to fall back to a second model when the primary model call fails. |
| [retry](language/csharp/examples/retry) | This example uses published NuGet `Praxo.Core==0.11.1` to retry transient model failures without changing the agent loop. |
| [service](language/csharp/examples/service) | This example embeds published NuGet `Praxo.Core==0.11.1` in a standard-library TCP/HTTP service. The application supplies a principal and tenant, restricts tools, and returns JSON. |
| [session-checkpoint](language/csharp/examples/session-checkpoint) | This example uses published NuGet `Praxo.Core==0.11.1` to save and restore a multi-turn conversation across two agent runs. The checkpoint allowlist encodes the session message... |
| [streaming](language/csharp/examples/streaming) | This example uses published NuGet `Praxo.Core==0.11.1` to consume deltas while the agent loop keeps running normally. |
| [structured-output](language/csharp/examples/structured-output) | This example uses published NuGet `Praxo.Core==0.11.1` to turn free text into validated JSON with `StructuredOutput`. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/csharp/Tutorial`. Planning context: [Tutorial Plan](https://axisvela.github.io/praxo-core/getting-started/tutorial-plan/), [100 candidate agent scenarios](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), and [Tutorial Catalog](https://axisvela.github.io/praxo-core/getting-started/tutorial-catalog/).

| Path | What it shows |
| --- | --- |
| [Tutorial](language/csharp/Tutorial) | Application tutorials live in `Tutorial/`, alongside focused `language/go/examples/`. |
| [airport-recovery](language/csharp/Tutorial/airport-recovery) | A bounded first slice of [TL-07](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an airport operations system. It reads fixed gate/crew/connection constraints and drafts review-only recovery options. No operational scheduling, live disruption feed or latency guarantee. |
| [architecture-graph](language/csharp/Tutorial/architecture-graph) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [bom-review](language/csharp/Tutorial/bom-review) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [construction-safety](language/csharp/Tutorial/construction-safety) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [contract-review](language/csharp/Tutorial/contract-review) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [due-diligence](language/csharp/Tutorial/due-diligence) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [healthcare-scheduling](language/csharp/Tutorial/healthcare-scheduling) | A native C# Core tutorial for review-only appointment scheduling. It reads a fixed `appointment-100` clinic schedule, checks slot availability, and drafts a booking for human re... |
| [internal-service-desk](language/csharp/Tutorial/internal-service-desk) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [medical-coding](language/csharp/Tutorial/medical-coding) | A bounded first slice of [HC-04](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a billing or reimbursement system. It checks fixed record completeness and drafts review-only DRG/DIP-style codes. No false coding, reimbursement optimization or billing submission. |
| [order-review](language/csharp/Tutorial/order-review) | Embed the native C# Core in an ASP.NET Core minimal API. The Agent invokes a scoped order-review tool over the public synthetic business service. The same application also offer... |
| [phishing-awareness](language/csharp/Tutorial/phishing-awareness) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [public-approval](language/csharp/Tutorial/public-approval) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [rpa-reconciliation](language/csharp/Tutorial/rpa-reconciliation) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [sales-crm](language/csharp/Tutorial/sales-crm) | A native C# Core tutorial for a review-only sales workflow. The Agent has two fixed tools: `read_customer` reads synthetic customer `customer-100`, and `draft_followup` produces... |
| [test-generation](language/csharp/Tutorial/test-generation) | A bounded first slice of [SE-04](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a test-execution or load-testing service. It generates three bounded tests for a fixed local fixture and records zero executions. No load target, network traffic or runtime verification. |
| [trial-screening](language/csharp/Tutorial/trial-screening) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |
| [zero-trust-review](language/csharp/Tutorial/zero-trust-review) | A bounded tutorial slice over the native .NET Core. It reads one fixed fixture, enforces scope and drafts a review-only result. No production write or external system access. |

## Reference Applications

No accepted end-to-end reference application is recorded for this language yet. Candidate goals are tracked in the [Reference Application Portfolio](https://axisvela.github.io/praxo-core/project/roadmap/#reference-application-portfolio).

## Verify

Run the checks from `language/csharp`:

```bash
dotnet build language/csharp/Praxo.Core/Praxo.Core.csproj
dotnet run --project language/csharp/Praxo.Conformance
dotnet run --project language/csharp/Praxo.Tests
dotnet run --project language/csharp/Praxo.Conformance -- --check-api
dotnet run --project language/csharp/samples/VbSample
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/csharp/README.md`](language/csharp/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

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

- `language/csharp/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/csharp
- Registry introduction: `language/csharp/REGISTRY.md`
- Machine-readable entry: `language/csharp/llms.txt` and `language/csharp/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-csharp
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical C# source. The monorepo remains the source of truth and the release workflow source. The mirror's `main` branch tracks current source, not a release snapshot. Source tags refer to the canonical monorepo and are not necessarily present in this mirror; syncing the branch does not publish mirror tags or registry packages.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
