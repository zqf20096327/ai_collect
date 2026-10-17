<p align="center">
  <img src="assets/millwright-mark.svg" alt="Millwright" width="104" height="104">
</p>

<h1 align="center">Millwright</h1>

<p align="center">
  <strong>The self-hosted LLM router for policy, cache affinity, and spend control in one Rust Binary.</strong>
</p>

<p align="center">
  <a href="https://github.com/Northwood-Systems/millwright/releases"><img alt="Release v0.1.0" src="https://img.shields.io/badge/release-v0.1.0-E66F2E?style=flat-square"></a>
  <a href="LICENSE"><img alt="Apache-2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-5B8C3A?style=flat-square"></a>
  <a href="https://github.com/Northwood-Systems/millwright/actions/workflows/ci.yml"><img alt="CI status" src="https://github.com/Northwood-Systems/millwright/actions/workflows/ci.yml/badge.svg"></a>
  <a href="rust-toolchain.toml"><img alt="Rust 1.97" src="https://img.shields.io/badge/rust-1.97-168BCC?style=flat-square&logo=rust"></a>
  <a href=".github/workflows/release.yml"><img alt="Linux and macOS" src="https://img.shields.io/badge/platforms-Linux%20%C2%B7%20macOS-168BCC?style=flat-square"></a>
</p>

## What is Millwright

Millwright is an open-source, self hosted LLM router that runs between your AI applications and the model providers you choose. It accepts OpenAI Chat Completions and Anthropic Messages, then routes each request to an OpenAI-compatible API, Anthropic, or Amazon Bedrock.

You define which models belong in the `cheap`, `mid`, and `frontier` roles. Millwright selects the lowest estimated-cost healthy route the resolved role permits and, when given a session ID, preserves provider/model affinity for prompt-cache reuse.

Millwright is a router, not an agent orchestrator. It does not spawn agents, schedule work, inspect prompts, or rewrite context.

## Why Millwright

LLM costs rise quickly when every request reaches the most expensive model and provider changes break prompt-cache reuse. Millwright makes the lower-cost path explicit:

- **Control model spend** — reserve frontier models for the work your policy says needs them.
- **Protect prompt caches** — role-scoped affinity keeps each session on a confirmed provider and model while its cache window is warm.
- **Keep concurrent agents moving** — one session can maintain independent `cheap`, `mid`, and `frontier` lanes without serializing requests.
- **Change providers without changing application code** — route compatible traffic across providers behind one endpoint.
- **Keep routing inspectable** — response headers identify the chosen route; traces and ledger entries retain the evidence when persistence is available.
- **Run the data plane yourself** — provider credentials stay on your infrastructure, with no required hosted control plane.

## Get Started

### Quick Start

Rust 1.97+ is required when building from source.

```bash
git clone https://github.com/Northwood-Systems/millwright.git
cd millwright
cargo install --path . --locked
millwright init
millwright serve
```

`millwright init` walks through provider endpoints, model roles, pricing, and separate workload and operator keys. It stores references to provider-secret environment variables, never the provider credentials themselves.

Connect [Claude Code, Codex, OpenCode, Pi, or another compatible client](docs/clients.md). Choose `millwright-fast`, `millwright-code`, or `millwright-plan` to request the cheap, mid, or frontier role.

### Optional Local Demo

The included Docker Compose setup starts Millwright with a mock provider and local demo key:

```bash
make compose-up
```

From another terminal:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H 'Authorization: Bearer sk-millwright-local-demo' \
  -H 'Content-Type: application/json' \
  -d '{"model":"millwright-fast","messages":[{"role":"user","content":"Hello from Millwright"}]}'
```

[Architecture](docs/architecture.md) · [Router API](docs/gateway-api.md) · [Policy & Catalog](docs/policy.md) · [Deployment](docs/deployment.md) · [Cost Analysis](docs/analyze.md) · [Security](SECURITY.md)

## Features

### Policy-controlled routing

Classify requests with explicit task and risk headers, the client's model selection, or documented defaults. Millwright resolves a `cheap`, `mid`, or `frontier` role, then selects the lowest estimated-cost healthy model that policy allows. High-risk and planning requests always use the frontier role.

Every decision includes the chosen model, provider, route reason, and rejected alternatives. Message content is never inspected to make the decision.

### Cache-aware concurrency

Naive per-request routing can erase provider prompt-cache savings by switching models mid-session. Millwright keeps independent `cheap`, `mid`, and `frontier` affinity lanes under one opaque session ID, each with its own cache TTL.

Traffic resolved to different roles no longer fights over one warm route. Same-role calls converge on the last confirmed provider/model, while all requests remain concurrent—Millwright does not serialize agent traffic or orchestrate agent lifecycles.

### See where the spend goes

Completed requests normally write usage evidence, cost provenance, provider attempts, and routing evidence to the ledger. SQLite is the local default; PostgreSQL is available for production deployments.

| Command | What it shows |
| --- | --- |
| `millwright spend` | Total spend, cache read rate, and per-team breakdown |
| `millwright models` | Model and provider mix |
| `millwright trace <id>` | One routing decision, including rejected alternatives |
| `millwright top` | Live spend and model activity in the terminal |

The same data is available through the authenticated `/v1/millwright/*` management APIs, with JSON output from `spend`, `models`, and `trace` for dashboards and automation.

### Analyze cost opportunities

`millwright analyze` reads a live Millwright ledger or local Millwright, OpenAI-compatible, or Anthropic JSONL. It produces a self-contained HTML or Markdown report plus schema-versioned JSON.

```bash
millwright analyze \
  --url http://127.0.0.1:8080 \
  --key "$MILLWRIGHT_OPERATOR_KEY" \
  --since 30d \
  --report analysis.html \
  --json-out analysis.json
```

Reports separate **measured** cost evidence from **modeled** candidate economics. Add an explicit catalog and candidate allowlist to compare full-swap costs and a price-floor economic scenario. Candidate results are cost hypotheses—not quality results or production routing recommendations. See [Cost Analysis](docs/analyze.md).

### Provider and protocol support

OpenAI Chat Completions and Anthropic Messages come in; OpenAI-compatible APIs, native Anthropic, and Amazon Bedrock go out. Same-protocol routes preserve fields Millwright does not model. Cross-protocol routes translate the supported text-and-tools subset and reject unsupported shapes instead of silently dropping data.

Retryable transport failures, timeouts, HTTP 408/429, and HTTP 5xx responses can trigger one bounded failover attempt. Circuit breakers stop unhealthy routes from receiving every request.

### Built for self-hosting

Millwright ships as one Rust binary with Docker and Docker Compose support. Provider credentials remain in environment variables, while separate workload and operator keys control inference and management access. Structured logs omit API keys and prompt payloads; request bodies, concurrency, timeouts, and upstream buffers are bounded.

## Enterprise

Need help deploying Millwright inside your infrastructure, integrating a provider, or designing a routing policy for your workload?

[Talk to the founder](https://northwoodsystems.ai/contact)

## Contributing

Bug fixes, features, tests, and documentation improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

### Quick Start for Contributors

The Rust toolchain is pinned in `rust-toolchain.toml`.

```bash
git clone https://github.com/Northwood-Systems/millwright.git
cd millwright
make build
make test
```

### Code Quality / Linting

Before opening a pull request, run:

```bash
make fmt
make lint
make test
make audit
```

The checks cover Rustfmt, Clippy with warnings denied, all Rust test targets, dependency advisories, approved licenses, and dependency sources. `make audit` requires [`cargo-deny`](https://embarkstudios.github.io/cargo-deny/). CI also builds the release binary and Docker image.

## License

Apache-2.0
