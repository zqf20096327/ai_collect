# PRAXO-CORE for TypeScript

PRAXO-CORE is a dependency-free TypeScript framework for building tool-using AI agents. It provides the agent runtime, not a model or hosted service, so you keep control of your models, tools, storage, and sandboxing.

## At a glance

| Field | Value |
| --- | --- |
| Package | `@axisvela/praxo-core` |
| Registry | [npm](https://www.npmjs.com/package/@axisvela/praxo-core/v/0.9.0) |
| Install | `npm install @axisvela/praxo-core@0.9.0` |
| Source version | `0.9.0` |
| Published version | `0.9.0` |
| Source tag | `typescript/v0.9.0` |
| Tier | Core |
| Contract | `SPEC_VERSION` `0.2.0` |
| Documentation | https://axisvela.github.io/praxo-core/languages/typescript/ |
| License | MIT |

## Highlights

- Typed models, tools, events, and sessions.
- Policy hooks, approvals, path checks, PII redaction, and call limits.
- Context budgets, checkpoints, middleware, and fallback models.
- Streaming, `AbortSignal` cancellation, and OpenAI-compatible, Anthropic, and Gemini adapters.
- No runtime dependencies; Node.js 20 or newer.

## Quick start

Install the published package:

```bash
npm install @axisvela/praxo-core@0.9.0
```

```ts
import {
  Agent,
  FuncTool,
  Registry,
  ROLE_ASSISTANT,
} from "@axisvela/praxo-core";

class EchoModel {
  async generate() {
    return {
      message: { role: ROLE_ASSISTANT, content: "hello" },
    };
  }
}

const tools = new Registry();
tools.register(new FuncTool("echo", "Echo", (args) => args));

const agent = new Agent({ model: new EchoModel(), tools });
const result = await agent.run({ id: "session-1" }, "hi");
console.log(result.output, result.steps, result.usage);
```

See the [full TypeScript README](language/typescript/README.md) for complete installation, build, and verification commands.

## What's included

| Capability | Status | Detail |
| --- | --- | --- |
| OpenAI-compatible model | native | `src/adapters/openaicompat.ts` |
| Anthropic model | native | `src/adapters/anthropic.ts`; SSE streaming reassembly |
| Gemini model | native | `src/adapters/gemini.ts`; SSE streaming |
| MCP client | native | `src/adapters/mcp.ts`; stdio, plus `src/adapters/mcp-http.ts` for Streamable HTTP 2025-03-26 |
| Harmovela sink | native | `src/adapters/harmovela.ts` |
| OpenTelemetry sink | native (transport seam) | `src/adapters/otel.ts`; caller supplies OTLP/HTTP transport |
| Subagent delegation | native | `src/delegation.ts` `SubagentManager` |
| Retriever | native | `src/retriever.ts` `Document` and `Retriever` |

## Examples

Runnable examples live under [`language/typescript/examples`](language/typescript/examples).

| Example | What it shows |
| --- | --- |
| [advanced-delegation](language/typescript/examples/advanced-delegation) | This example shows an application-level parent/child agent pattern. The parent agent may call a `delegate` tool but not the child's `record` tool. The delegate tool runs a child... |
| [checkpoint](language/typescript/examples/checkpoint) | This example uses published npm `@axisvela/praxo-core@0.9.0` to keep checkpoint storage application-owned while using the SDK allowlist for payload encoding. |
| [consumer](language/typescript/examples/consumer) | This starter installs the published `@axisvela/praxo-core@0.9.0` package from npm in a separate application. It does not import the repository's TypeScript source. Node.js 20 or... |
| [event-sink](language/typescript/examples/event-sink) | This example uses published npm `@axisvela/praxo-core@0.9.0` to observe agent lifecycle and tool events without coupling the agent to a logging or telemetry backend. |
| [hitl](language/typescript/examples/hitl) | This example demonstrates a write tool that requires human approval: |
| [identity-policy](language/typescript/examples/identity-policy) | This example uses published npm `@axisvela/praxo-core@0.9.0` to bind a trusted principal to Core policy authorization. The application owns authentication and principal storage;... |
| [live-model](language/typescript/examples/live-model) | This example uses published npm `@axisvela/praxo-core@0.9.0` to connect the TypeScript Core to an OpenAI-compatible endpoint and registers one low-risk `get_time` tool. |
| [mcp](language/typescript/examples/mcp) | This example uses published npm `@axisvela/praxo-core@0.9.0` to connect to a minimal stdio MCP server, list tools, register them in a Core registry, and call one tool. |
| [provider-fallback](language/typescript/examples/provider-fallback) | This example uses published npm `@axisvela/praxo-core@0.9.0` to fall back to a second model when the primary model call fails. |
| [representative-chain](language/typescript/examples/representative-chain) | This deterministic example exercises the same application seams as the Go and Python representative chains without a live provider: |
| [retry](language/typescript/examples/retry) | This example uses published npm `@axisvela/praxo-core@0.9.0` to retry transient model failures without changing the agent loop. |
| [service](language/typescript/examples/service) | This example embeds published npm `@axisvela/praxo-core@0.9.0` in a Node standard-library HTTP service. The application supplies a principal and tenant, restricts tools, and ret... |
| [service-auth](language/typescript/examples/service-auth) | This example embeds published npm `@axisvela/praxo-core@0.9.0` in a Node standard-library HTTP service with application-owned identity (local HMAC, OIDC/JWT, or token introspect... |
| [session-checkpoint](language/typescript/examples/session-checkpoint) | This example saves and restores a conversation history across two agent turns. It uses the Core allowlist for payload encoding and a teaching in-memory store. |
| [streaming](language/typescript/examples/streaming) | This example uses published npm `@axisvela/praxo-core@0.9.0` to consume deltas while the agent loop keeps running normally. |
| [structured-output](language/typescript/examples/structured-output) | This example uses published npm `@axisvela/praxo-core@0.9.0` to turn free text into validated JSON with `StructuredOutput`. |

## Verify

Run the checks from `language/typescript`:

```bash
cd language/typescript
npm ci
npm run build
npm run conformance
node --test tests
```

This mirror contains the language source and the shared `spec/` vectors, so the implementation can be built and tested here. See [`language/typescript/README.md`](language/typescript/README.md) for the exact commands. The monorepo CI runs conformance, API snapshot, and native tests for this implementation.

## Community

- X: <https://x.com/axisvela>
- Weibo: <https://weibo.com/u/1936025761>

## Repository layout

- `language/typescript/` — implementation source, tests, API snapshot, and examples
- `spec/` — shared contract, vectors, and parity inventories
- `LICENSE` — MIT license

## Canonical source

- Canonical source: https://github.com/axisvela/praxo-core/tree/main/language/typescript
- Registry introduction: `language/typescript/REGISTRY.md`
- Machine-readable entry: `language/typescript/llms.txt` and `language/typescript/llms.md`
- Mirror repository: https://github.com/axisvela/praxo-core-typescript
- Release index: https://axisvela.github.io/praxo-core/languages/registry-status/

This repository is a discovery mirror of the canonical TypeScript source. The monorepo remains the source of truth and the release workflow source.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
