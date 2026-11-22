# PRAXO-CORE for C#

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its native .NET Core: an agent loop with tool registration and dispatch, policy hooks, typed events, memory, checkpoints, context budgets, middleware, JSON Schema validation, and plugin manifest parsing. It runs in-process and does not require a hosted service.

## At a glance

| Field | Value |
| --- | --- |
| Package | `Praxo.Core` |
| Registry | [NuGet](https://www.nuget.org/packages/Praxo.Core/0.10.0) |
| Install | `dotnet add package Praxo.Core --version 0.10.0` |
| Source version | `0.10.0` |
| Published version | `0.10.0` |
| Source tag | `csharp/v0.10.0` |
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
dotnet add package Praxo.Core --version 0.10.0
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
| [advanced-delegation](language/csharp/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern using published NuGet `Praxo.Core==0.10.0`. The parent agent may call a `delegate` tool but not the child's `r... |
| [checkpoint](language/csharp/examples/checkpoint) | This example uses published NuGet `Praxo.Core==0.10.0` to keep checkpoint storage application-owned while using the SDK allowlist for payload encoding. |
| [consumer](language/csharp/examples/consumer) | This starter installs the published NuGet package `Praxo.Core==0.10.0` and verifies an allow/deny governed tool path. |
| [event-sink](language/csharp/examples/event-sink) | This example uses published NuGet `Praxo.Core==0.10.0` to observe agent lifecycle and tool events without coupling the agent to a logging or telemetry backend. |
| [hitl](language/csharp/examples/hitl) | This example uses published NuGet `Praxo.Core==0.10.0` to demonstrate a write tool that requires human approval: |
| [identity-policy](language/csharp/examples/identity-policy) | This example uses published NuGet `Praxo.Core==0.10.0` to bind a trusted principal to Core policy authorization. The application owns authentication and principal storage; Core... |
| [live-model](language/csharp/examples/live-model) | This example uses published NuGet `Praxo.Core==0.10.0` to connect the C# Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/csharp/examples/mcp) | This example uses published NuGet `Praxo.Core==0.10.0` with an in-process MCP transport. It exercises the same `initialize`, `tools/list`, and `tools/call` flow as a stdio sessi... |
| [provider-fallback](language/csharp/examples/provider-fallback) | This example uses published NuGet `Praxo.Core==0.10.0` to fall back to a second model when the primary model call fails. |
| [retry](language/csharp/examples/retry) | This example uses published NuGet `Praxo.Core==0.10.0` to retry transient model failures without changing the agent loop. |
| [service](language/csharp/examples/service) | This example embeds published NuGet `Praxo.Core==0.10.0` in a standard-library TCP/HTTP service. The application supplies a principal and tenant, restricts tools, and returns JSON. |
| [session-checkpoint](language/csharp/examples/session-checkpoint) | This example uses published NuGet `Praxo.Core==0.10.0` to save and restore a multi-turn conversation across two agent runs. The checkpoint allowlist encodes the session message... |
| [streaming](language/csharp/examples/streaming) | This example uses published NuGet `Praxo.Core==0.10.0` to consume deltas while the agent loop keeps running normally. |
| [structured-output](language/csharp/examples/structured-output) | This example uses published NuGet `Praxo.Core==0.10.0` to turn free text into validated JSON with `StructuredOutput`. |

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

This repository is a discovery mirror of the canonical C# source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
