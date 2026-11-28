# PRAXO-CORE for TypeScript

PRAXO-CORE is a dependency-free TypeScript framework for building tool-using AI agents. It provides the agent runtime, not a model or hosted service, so you keep control of your models, tools, storage, and sandboxing.

## At a glance

| Field | Value |
| --- | --- |
| Package | `@axisvela/praxo-core` |
| Registry | [npm](https://www.npmjs.com/package/@axisvela/praxo-core/v/0.10.1) |
| Install | `npm install @axisvela/praxo-core@0.10.1` |
| Source version | `0.10.1` |
| Published version | `0.10.1` |
| Publication status | published |
| Canonical source tag | [`typescript/v0.10.1`](https://github.com/axisvela/praxo-core/tree/typescript/v0.10.1) |
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
npm install @axisvela/praxo-core@0.10.1
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
| [consumer](language/typescript/examples/consumer) | This starter installs the published `@axisvela/praxo-core@0.10.1` package from npm in a separate application. It does not import the repository's TypeScript source. Node.js 20 o... |
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

## Scenario Tutorials

Scenario-oriented tutorials live under `language/typescript/Tutorial`. Planning context: [Tutorial Plan](https://axisvela.github.io/praxo-core/getting-started/tutorial-plan/), [100 candidate agent scenarios](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), and [Tutorial Catalog](https://axisvela.github.io/praxo-core/getting-started/tutorial-catalog/).

| Path | What it shows |
| --- | --- |
| [Tutorial](language/typescript/Tutorial) | Application-shaped tutorials live here, alongside `language/go/examples/`, which keeps mechanism checks and focused integration examples. Tutorial is intentionally capitalized i... |
| [api-orchestration](language/typescript/Tutorial/api-orchestration) | A bounded first slice of [SE-08](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an integration platform. It maps two fixed synthetic APIs, validates the order schema, and either drafts a review-only mapping or stops on a schema mismatch. No network, credentials or partner system is accessed. |
| [copyright-evidence](language/typescript/Tutorial/copyright-evidence) | Compares fixed authorized assets and drafts a review-only evidence packet. No broad crawl, DMCA notice or infringement verdict. |
| [customer-support](language/typescript/Tutorial/customer-support) | A native TypeScript Core tutorial for a customer-support reply streamed over SSE. The Agent has two fixed tools: `lookup_order` reads `order-100`, and `search_policy` reads a fi... |
| [education-tutoring](language/typescript/Tutorial/education-tutoring) | Tracks a fixed learner fixture and drafts a graded Socratic question for review. No adaptive model or issued grade. |
| [live-show](language/typescript/Tutorial/live-show) | Replays fixed engagement events and drafts a review-only running order. No audience profiling, coupon sends or stream control. |
| [localization-draft](language/typescript/Tutorial/localization-draft) | A bounded first slice of [CS-07](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a legal or tax compliance system. It compares fixed localization rules and drafts review-only localized product text. No legal/tax guarantee, live content system or publication. |
| [meeting-coordination](language/typescript/Tutorial/meeting-coordination) | Reconciles fixed calendar evidence and drafts review-only minutes. No invitations or live calendar writes. |
| [negotiation-interpretation](language/typescript/Tutorial/negotiation-interpretation) | A bounded first slice of [OG-03](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not an interpreter or cultural-profiling system. It compares a fixed bilingual transcript excerpt and drafts review-only negotiation notes. No micro-expression inference, mind reading or live interpretation guarantee. |
| [order-review](language/typescript/Tutorial/order-review) | First deterministic native TypeScript Core integration slice. It shares the synthetic order HTTP service with the Python example, not a remote Agent loop. The `review_order` too... |
| [phishing-awareness](language/typescript/Tutorial/phishing-awareness) | Classifies a fixed synthetic email and drafts an authorized review-only awareness exercise. No sends, links or infrastructure attacks. |
| [retail-replenishment](language/typescript/Tutorial/retail-replenishment) | A bounded first slice of [CS-05](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not live pricing or procurement. It checks a fixed SKU's stock and pricing fixture and drafts a review-only purchase order. No network, credentials or live model are used. |
| [sales-crm](language/typescript/Tutorial/sales-crm) | Extracts fixed objections from a transcript and drafts a review-only CRM update. No CRM write or customer message. |
| [storyboard-previs](language/typescript/Tutorial/storyboard-previs) | Turns a fixed script scene into a review-only shot plan. No rendering or virtual-production engine. |
| [travel-booking](language/typescript/Tutorial/travel-booking) | A native TypeScript Core tutorial for review-only flight booking. It checks fixed `trip-100` inventory and drafts a fare hold with no payment or booking write. The model package... |
| [workspace-plan](language/typescript/Tutorial/workspace-plan) | A bounded first slice of [SE-01](https://axisvela.github.io/praxo-core/getting-started/agent-scenarios/), not a code-generation or deployment product. It reads a fixed allowlisted workspace, applies one bounded edit to `app.js` and inspects synthetic diagnostics. In-process fixtures only; no host filesystem, compiler or deployment. |

## Reference Applications

No accepted end-to-end reference application is recorded for this language yet. Candidate goals are tracked in the [Reference Application Portfolio](https://axisvela.github.io/praxo-core/project/roadmap/#reference-application-portfolio).

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
- LinkedIn: <https://www.linkedin.com/company/axisvela/>
- Facebook: <https://www.facebook.com/profile.php?id=61596905732406>
- YouTube: <https://www.youtube.com/@axisvela>
- Discord: <https://discord.com/channels/1575163993767809064/1575164343148875977>
- GitHub Discussions: <https://github.com/axisvela/praxo-core/discussions>
- GitHub Issues: <https://github.com/axisvela/praxo-core/issues>
- Documentation: <https://axisvela.github.io/praxo-core/>
- Architect: <https://axisvela.architect.pub>

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

This repository is a discovery mirror of the canonical TypeScript source. The monorepo remains the source of truth and the release workflow source. The mirror's `main` branch tracks current source, not a release snapshot. Source tags refer to the canonical monorepo and are not necessarily present in this mirror; syncing the branch does not publish mirror tags or registry packages.

PRAXO-CORE is not a hosted model, workflow engine, identity provider, or safety controller. Do not infer exactly-once execution, complete sandbox isolation, production security certification, live-provider behavior, or physical safety from this package.

MIT licensed.
