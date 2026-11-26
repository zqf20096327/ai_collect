# PRAXO-CORE for PowerShell

PRAXO-CORE is an embeddable, MIT-licensed agent framework. This package is its PowerShell Core: a shared-runtime wrapper over the C# Core for existing PowerShell automation that needs a model/tool loop, explicit policy and tool scope, events, memory, checkpoints, and human-in-the-loop decisions.

## At a glance

| Field | Value |
| --- | --- |
| Package | `praxo-core-ps` |
| Registry | [PowerShell Gallery](https://www.powershellgallery.com/packages/praxo-core-ps/0.8.1) |
| Install | `Install-Module praxo-core-ps` |
| Source version | `0.9.0` |
| Published version | `0.8.1` |
| Source tag | `powershell/v0.9.0` |
| Tier | Core (.NET) |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/powershell/ |
| License | MIT |

## Highlights

- OpenAI-compatible model: inherited
- Anthropic model: inherited
- Gemini model: inherited
- MCP client: native (C# shared runtime)
- Harmovela sink: inherited
- OpenTelemetry sink: inherited
- Subagent delegation: native (synchronous wrapper)
- Retriever: inherited (wrapper)

## Quick start

Install the published package:

```powershell
Install-Module praxo-core-ps
```

```powershell
$model = New-PraxoStaticModel -Content 'hello'
$options = New-PraxoAgentOptions -Model $model
$agent = New-PraxoAgent -Options $options
$session = New-PraxoSession -Id 'demo'
(Invoke-PraxoAgent -Agent $agent -Session $session -Prompt 'hello').Output
```

See the [full PowerShell README](language/powershell/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | inherited | Uses the C# Core |
| Anthropic model | inherited | Uses the C# Core |
| Gemini model | inherited | Uses the C# Core |
| MCP client | native (C# shared runtime) | `Connect-PraxoMcp`, `Get-PraxoMcpTools`, `Invoke-PraxoMcpTool`; wraps the C# MCP client and stdio/Streamable HTTP transports |
| Harmovela sink | inherited | Uses the C# Core |
| OpenTelemetry sink | inherited | Uses the C# Core |
| Subagent delegation | native (synchronous wrapper) | Reuses C# request/result/task types; no asynchronous manager |
| Retriever | inherited (wrapper) | Wraps C# `Retriever` |

## Examples

Runnable examples live under [`language/powershell/examples`](language/powershell/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/powershell/examples/advanced-delegation) | Application-level parent/child delegation plus six governance negative checks. |
| [checkpoint](language/powershell/examples/checkpoint) | This example uses the PowerShell Core checkpoint allowlist for a registered payload round trip. |
| [consumer](language/powershell/examples/consumer) | This starter is a thin PowerShell wrapper over the C# PRAXO-CORE runtime. The PowerShell module loads `Praxo.Core.dll`; the agent loop, tools, policy, and deterministic model be... |
| [event-sink](language/powershell/examples/event-sink) | This example demonstrates event fan-out and tool-only filtering with PowerShell-friendly sink collections. |
| [hitl](language/powershell/examples/hitl) | This example demonstrates a write tool that requires human approval: |
| [identity-policy](language/powershell/examples/identity-policy) | This example binds a trusted principal to policy decisions and rejects missing, role-mismatched, and tenant-mismatched actions. |
| [live-model](language/powershell/examples/live-model) | This example is a thin PowerShell wrapper over the C# PRAXO-CORE runtime. It uses the C# `OpenAiCompatibleModel` and registers one low-risk `get_time` tool with a small JSON Sch... |
| [mcp](language/powershell/examples/mcp) | The PowerShell Core does not bundle an MCP client. This example provides a transport-neutral MCP-shaped client boundary: initialize, `tools/list`, and `tools/call` over a caller... |
| [provider-fallback](language/powershell/examples/provider-fallback) | This example calls a fallback only after the primary fails and preserves the primary failure when both fail. |
| [representative-chain](language/powershell/examples/representative-chain) | Deterministic representative chain covering MCP record, final-argument authorization, governed child delegation, OTel/Harmovela events, and an edited denial with zero effects. |
| [retry](language/powershell/examples/retry) | This example retries a transient failure with a bounded attempt count and keeps the exhausted failure state. |
| [service](language/powershell/examples/service) | This example defines a transport-neutral request handler with health, principal, and run cases. |
| [session-checkpoint](language/powershell/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns. It uses the module's `New-PraxoSession` and `Invoke-PraxoAgent` over the C# Core runtime, plus the... |
| [streaming](language/powershell/examples/streaming) | This example accumulates streamed chunks and checks that they reconstruct the final output. |
| [structured-output](language/powershell/examples/structured-output) | This example validates a final JSON answer against a schema and rejects invalid output. |

## Scenario Tutorials

Scenario-oriented tutorials live under `language/powershell/Tutorial`.

| Path | What it shows |
| --- | --- |
| [Tutorial](language/powershell/Tutorial) | Application tutorials live in `Tutorial/`, alongside focused `language/go/examples/`. |
| [finops-review](language/powershell/Tutorial/finops-review) | A bounded cloud cost-review tutorial. It reads fixed resource costs, computes the highest-cost resource below a 5% utilization threshold, and drafts a review-only action. No clo... |
| [windows-diagnostics](language/powershell/Tutorial/windows-diagnostics) | A read-only Windows operations tutorial. PowerShell calls the shared C# Core through `praxo-core-ps`; the Agent has two fixed tools, `read_service` and `read_disk`. It produces... |

## Verify

Run the checks from `language/powershell`:

```bash
dotnet build language/csharp/Praxo.Core/Praxo.Core.csproj -c Release
dotnet run --project language/csharp/Praxo.Conformance -c Release
dotnet run --project language/csharp/Praxo.Tests -c Release
pwsh -NoProfile -File language/powershell/tests/run.ps1
pwsh -NoProfile -File language/powershell/api-snapshot.ps1 -Check
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/powershell/README.md`](language/powershell/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

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

- `language/powershell/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/powershell
- Registry introduction: `language/powershell/REGISTRY.md`
- Machine-readable entry: `language/powershell/llms.txt` and `language/powershell/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-powershell
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical PowerShell source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
