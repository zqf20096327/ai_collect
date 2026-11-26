<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
  <img alt="BrowserX: Next-generation AI/LLM-native browser pooling, session management, persistence, recovery and handoff for authorized security research." src="docs/assets/banner-light.svg" width="100%">
</picture>

**Next-generation AI/LLM-native browser pooling, session management, persistence, recovery and handoff for authorized security research.**

One Rust service supervises local Chromium processes, leases them to automation clients as sessions, keeps the state you ask it to keep, replaces browsers that die, and moves control of a live session from one client to another, with an explicit answer to the question every client has: what survived? A built-in [Model Context Protocol](docs/guides/mcp.md) server lets AI agents watch, drive and explain the pool within limits the operator sets, while leases, recovery and egress policy stay deterministic code.

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE) [![CI](https://github.com/noxred-research/browserx/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/noxred-research/browserx/actions/workflows/ci.yml) [![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-informational)](CHANGELOG.md) [![Rust 1.99.0](https://img.shields.io/badge/rust-1.99.0-orange?logo=rust)](rust-toolchain.toml) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md) [![Security policy](https://img.shields.io/badge/security-policy-informational?logo=github)](SECURITY.md)

[What it is](#what-is-browserx) · [Core idea](#the-core-idea-three-different-contracts) · [Features](#features) · [AI/LLM-native](#aillm-native) · [Architecture](#architecture) · [Quick start](#quick-start) · [API](#api-at-a-glance) · [Configuration](#configuration) · [Observability](#observability) · [Responsible use](#responsible-use-and-security) · [Docs](#documentation)

</div>

> [!IMPORTANT]
> **For authorized security research and authorized automation only.** BrowserX is for operating browsers and network egress that you own or are permitted to operate, against sites and services you are permitted to test or automate, within an engagement scope you can show. AI agents that drive it act under the same rule. It makes no promise about how a target site treats a browser it runs, and it is not a tool for evading protections, abusing third-party services or attacking anyone. See [Responsible use and security](#responsible-use-and-security).

> **Status:** pre-1.0 (`0.1.0`). Interfaces, configuration keys, on-disk formats and the HTTP API can still change between minor versions, and the [changelog](CHANGELOG.md) lists what changed. The distribution is this repository and tagged source releases; no prebuilt binaries, images or crates.io packages are published, so build from source (see [Quick start](#quick-start)) or with the provided Dockerfile.

## What is BrowserX

BrowserX is a single worker process, written in Rust, that turns a machine with Chromium installed into a managed browser service.

- **Pooling.** It launches and supervises Chromium processes, keeps a warm pool of shared browsers if you want one, and admits session requests through a bounded queue with per-owner quotas and a deadline.
- **Session management.** A session is a *lease*: an identity, an owner, a time-to-live, a fencing generation and a controller token. Leases are stored in SQLite by default (PostgreSQL or MariaDB when several workers share one registry) and every change is a compare-and-swap, so two writers can never both win.
- **Persistence.** You choose exactly what outlives the browser process: nothing (`ephemeral`), encrypted cookie and storage snapshots (`snapshot`) or a locked profile directory (`profile`). There is no boolean "persistent" flag, because each mode is a different engineering contract.
- **Recovery.** A health monitor notices a dead or unresponsive browser, launches a replacement, restores what the persistence mode kept and tells the next client exactly what happened.
- **Handoff.** Control of a live session moves to a new client with one call. The generation increments, the old token and any relay connection bound to it stop working, and the browser keeps running.
- **AI/LLM-native operation.** `browserx mcp` exposes the pool to MCP clients as scoped tools: monitoring, session control, read-only browsing and, if the operator enables them, interaction and script evaluation. See [AI/LLM-native](#aillm-native).

Any client that speaks the Chrome DevTools Protocol over a WebSocket attaches through the authenticated relay: automation libraries, crawlers, your own tooling.

## The core idea: three different contracts

"Resume my browser" can mean three different things. Treating them as one is how automation systems lose logins, replay the wrong state or silently start from nothing. BrowserX keeps them apart and reports which one you got, on **every attach**, as an `outcome`:

| `outcome` | What happened | What you can rely on |
| --- | --- | --- |
| `resumed_same_process` | You reconnected to the **live** browser process. | Everything: open pages, JavaScript heaps, sockets, in-flight requests. Only the controller changed. |
| `restored_from_profile` | A **new** process was launched on the **same profile directory**. | What Chromium keeps on disk: cookies, `localStorage`, IndexedDB, cache. Not open pages, JavaScript heaps or sockets. One worker, one browser at a time. |
| `restored_from_snapshot` | A **new** process was launched and an encrypted **snapshot was replayed** into it. | Cookies and the `localStorage` of the origins that were open, plus the page URLs, reopened. Portable across workers. Not heaps, sockets, service workers, cache or origins never opened. |
| `fresh_process` | A **new, empty** browser. | Nothing was restored. Treat the session as new. |

A client that sees anything other than `resumed_same_process` knows to re-establish page state before it continues. See [Persistence](docs/design/persistence.md) and [Recovery](docs/design/recovery.md) for the exact contracts.

## Features

| Capability | What you get |
| --- | --- |
| **Dedicated and shared isolation** | One Chromium process per session, or one browser context per session inside a warm shared browser. Shared sessions only ever receive a scoped relay that refuses cross-context commands. See [isolation and security](docs/design/isolation-and-security.md) |
| **Leases with fencing** | Time-to-live with renewal, an absolute lifetime cap, an idle timeout, per-owner quotas, and a generation counter that fences every ownership change: allocation, recovery, handoff |
| **Admission control** | Bounded FIFO queue with a deadline; `429 capacity` instead of unbounded waiting |
| **Persistence modes** | `ephemeral`, `snapshot` (AES-256-GCM sealed, versioned, pruned, key-rotatable) and `profile` (0700 directory under an exclusive lock) |
| **Recovery** | Health probes with strikes, relaunch with bounded attempts, startup reconciliation after a worker crash, `recovery = "none"` when you would rather lose the session than replace it |
| **Handoff** | Token rotation with generation fencing; the old controller is cut off |
| **Egress** | A loopback forwarder per dedicated session in front of the browser: direct dialing with a private-range block, or an upstream `http://`, `https://`, `socks5://` or `socks5h://` proxy with credentials kept out of browser flags and logs, and `{session}` / `{generation}` username templates for sticky exits. See [egress](docs/design/egress.md) |
| **Launch profiles** | Named launch configurations: your own Chromium executable, extra flags, headless or headed. See [launch profiles](docs/guides/launch-profiles.md) |
| **HTTP API and CLI** | JSON API with typed errors, and `browserx session create\|list\|get\|attach\|renew\|handoff\|snapshot\|release` |
| **MCP server** | `browserx mcp` serves the Model Context Protocol (revisions `2026-07-28`, `2025-06-18` and `2025-03-26`) over stdio or loopback HTTP: capability-gated tools, a scope-checked browsing loop, an action gate with human approvals, signed engagement manifests and scope grants, a hash-chained audit log. See [AI/LLM-native](#aillm-native) |
| **Backends** | SQLite and a snapshot directory by default, with no other service. Optionally: leases in PostgreSQL or MariaDB (`[database]`, a required `node` per worker), sealed snapshots in an S3-compatible object store (`[object_store]`), MCP rate limits and call budgets shared through Valkey or Redis (`[cache]`), and copies of the MCP audit log in ClickHouse, Kafka, RabbitMQ, OpenSearch or Elasticsearch. Several workers and products can share one service instance because each writes only inside its own namespace. See [backends](docs/guides/backends.md) |
| **Operations** | Separate ops listener with `/healthz`, `/readyz` and Prometheus `/metrics`; graceful drain on SIGINT/SIGTERM with final snapshots and confirmed browser shutdown. See [operations](docs/guides/operations.md) |

## AI/LLM-native

BrowserX is built so that AI agents can **watch, drive and explain** a browser pool, within limits an operator sets. The same guarantees apply to a human, a script or an agent:

- **Models advise and act through scoped tools. They never authorize.** What a session may do, which origins it may visit and which tools exist at all are decided by operator configuration, not by a prompt.
- **The data path is deterministic.** Leases, fencing, recovery, egress policy and the host-protection relay policy are ordinary code. No model sits between a client and its browser, and everything works with no model configured.
- **Read-only by default.** Monitoring tools are always on; everything else is a capability the operator turns on.

`browserx mcp` implements the [Model Context Protocol](https://modelcontextprotocol.io) itself and talks to a worker through its public HTTP API. A tool whose capability is not enabled is not listed.

| Area | Capability | Tools |
| --- | --- | --- |
| Monitoring | always on | `capabilities`, `health`, `pool_status`, `assess`, `list_sessions`, `get_session`, `explain_session`, `explain_error`, `list_launch_profiles`, `list_snapshots` |
| Sessions | `sessions`; `handoff` for `handoff_session` | `create_session`, `renew_session`, `snapshot_session`, `release_session` (needs `confirm: true`), `handoff_session` |
| Browsing | `browse` | `open_page`, `page_snapshot`, `find_in_snapshot`, `page_text`, `screenshot`, `list_tabs`, `switch_tab`, `close_tab`, `go_back`, `go_forward`, `wait_for`, `network_log`, `console_log` |
| Interaction | `interact` | `click`, `type_text`, `press_key`, `select_option`, `scroll`, `hover` |
| Script | `evaluate` (off by default) | `evaluate_js` |
| LLM-assisted | `[ai]` configured; advisory | `summarize_page`, `extract_data`, `diagnose` |
| Engagement | always on; `propose_scope_grant` with `browse` and `[operator]` | `engagement_status`, `reset_context`, `propose_scope_grant` |

The server also offers bundled documentation as resources (`browserx://docs/...`, `browserx://sessions/{id}`) and three prompts: `triage_session`, `capacity_review` and `explore_authorized_site`.

### MCP quick start

```sh
cp examples/mcp.toml mcp.toml      # set server.url and server.api_key_file
browserx mcp --config mcp.toml     # MCP over stdio: point your MCP client at this command
```

For a client that connects over HTTP, add `--http 127.0.0.1:7692`. The listener is loopback by default, requires a bearer token whose SHA-256 digest is `mcp.http.token_sha256`, compares it in constant time and checks the `Origin` header.

### Safety model

- **Scope is enforced in code.** Navigation must match `browse.allowed_origins` (exact origins) and an optional engagement window, and is re-checked after redirects; a page that ends outside scope is replaced by `about:blank` and the call fails. The operator and an authorization note are recorded in every audit entry.
- **Page content is untrusted.** Every tool that returns page-derived text wraps it in `<untrusted_page_content origin="..." nonce="...">` (a fresh nonce per call closes the block and prefixes every line), and the server instructions tell the model to treat it as data, never as instructions.
- **Secrets never reach the model.** Lease tokens, `cdp_url`, API keys and proxy credentials stay in the MCP server; proxies are chosen by name from configuration.
- **Everything is audited.** Each tool call is appended to a hash-chained JSONL audit log; `browserx mcp audit verify <path>` checks the chain.
- **Consequential actions need a human.** Fixed code classifies each action on an element (`destructive`, `credential_entry`, `payment`, ...) and a profile decides allow, approval or deny; an approval is bound to the exact action and works once. `confirm: true` is never an approval.
- **Rules of engagement are signed.** An operator-signed engagement manifest (hosts as `attack`, `visit` or `blocked`, protected requests, impact ceiling, limits, windows) and an optional signed scope grant narrow what an agent may do; unsigned or altered documents widen nothing. A session ledger (the Rule of Two: untrusted input, sensitive context, a tool that changes pages) can require an approval or refuse when all three meet.
- **Bounded.** Per-tool rate limits and output budgets, a 4 MiB message limit, and `confirm: true` for destructive tools. Browsing tools only operate on sessions the MCP server created or was told to adopt.

An agent that can click and type can still be misled by hostile page content. Enable `interact` and `evaluate` only for scopes you would let a junior colleague operate, and read [the MCP guide](docs/guides/mcp.md) and [the AI/LLM-native design](docs/design/ai-llm-native.md) before you do.

## Architecture

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/architecture-dark.svg">
    <img alt="BrowserX architecture: clients, HTTP API and CDP relay, scheduler, Chromium runtime, egress forwarder and state directory" src="docs/assets/architecture-light.svg" width="900">
  </picture>
</p>

The workspace is split by responsibility:

| Crate | Responsibility |
| --- | --- |
| `browserx-core` | Identifiers, session spec, lease record and state machine, snapshot format, storage and runtime traits, typed errors |
| `browserx-cdp` | Bounded Chrome DevTools Protocol client |
| `browserx-runtime` | Chromium process supervision, launch profiles, profile locks, state capture and restore |
| `browserx-egress` | Per-session loopback forwarder and destination policy |
| `browserx-store` | Lease registry (SQLite, PostgreSQL, MariaDB), sealed snapshots (directory or S3-compatible object store), the snapshot sealer |
| `browserx-pool` | Scheduler: admission, allocation, renewal, expiry, recovery, handoff |
| `browserx-server` | HTTP API, CDP relay, ops endpoints, metrics |
| `browserx-mcp` | Model Context Protocol server: tools, resources, prompts, scope checks, audit log and its optional export sinks |
| `browserx` | The binary: `serve`, `mcp`, `doctor`, key tools and the client commands |

Read the [architecture overview](docs/design/architecture.md) for how a request flows through them.

## Quick start

You need a Rust toolchain (the version in [`rust-toolchain.toml`](rust-toolchain.toml); `rustup` installs it) and a Chromium executable on `PATH` or named by `BROWSERX_CHROMIUM_PATH`. BrowserX is installed from source: clone the repository at a release tag (or `main`) and build it.

```sh
cargo build --release --locked -p browserx

# 1. Check that this machine can run browsers.
target/release/browserx doctor

# 2. Create an API key. The key is printed once, with the config snippet holding its digest.
target/release/browserx keys new dev

# 3. Create the snapshot encryption key (mode 0600, refuses to overwrite).
target/release/browserx snapshot-key new ./.browserx-keys/snapshot.key

# 4. Put the printed [[auth.api_keys]] snippet into browserx.toml, then start the worker.
target/release/browserx serve --config browserx.toml
```

Create a session and use it from any CDP client:

```sh
export BROWSERX_SERVER=http://127.0.0.1:7690
export BROWSERX_API_KEY=<the key printed by `keys new`>

browserx session create --persistence snapshot
# prints the session id, the lease token (once) and the cdp_url

browserx session attach <session-id> --token <lease token>
# { "outcome": "resumed_same_process", ... }
```

Connect your CDP client to the `cdp_url`. The [getting started guide](docs/guides/getting-started.md) walks through it end to end, including killing the browser and watching the outcome change.

## API at a glance

All routes are JSON and need `Authorization: Bearer <api key>`; session operations also need the lease token in `X-BrowserX-Token`.

| Route | Purpose |
| --- | --- |
| `POST /v1/sessions` | Create a session: returns the session, the token (once), the `cdp_url` and the `outcome` |
| `GET /v1/sessions`, `GET /v1/sessions/{id}` | List your sessions (`?status=`) or read one |
| `POST /v1/sessions/{id}/attach` | Attach and learn the `outcome` |
| `POST /v1/sessions/{id}/renew` | Extend the lease |
| `POST /v1/sessions/{id}/handoff` | Rotate the token and move control to a new client |
| `POST /v1/sessions/{id}/snapshot` | Write a snapshot now |
| `DELETE /v1/sessions/{id}` | Release the session |
| `GET /v1/profiles/{id}/snapshots`, `DELETE /v1/profiles/{id}` | List snapshots; erase a profile |
| `GET /v1/launch-profiles` | Launch profiles this worker offers |
| `GET /cdp/{session_id}/{token}` | WebSocket upgrade to the CDP relay |

The [API reference](docs/guides/api.md) has request and response bodies, error codes and status mapping.

## Configuration

One TOML file with `deny_unknown_fields`: a misspelled key is an error, not a silent default. The sections are `[server]`, `[[auth.api_keys]]`, `[pool]`, `[session]`, `[storage]`, `[health]`, `[egress]` and `[runtime]`, plus the optional `[database]` and `[object_store]` ([backends](docs/guides/backends.md)). A commented example lives in [`examples/browserx.toml`](examples/browserx.toml); every key, default and bound is in the [configuration reference](docs/guides/configuration.md). `browserx config check <path>` validates a file without starting anything.

## Observability

- `GET /healthz` on the ops listener: the process is alive.
- `GET /readyz`: the stores are reachable, the default launch profile can start, and the worker is not draining.
- `GET /metrics`: Prometheus text with `browserx_sessions{status}`, `browserx_browsers{isolation}`, `browserx_admissions_total{result}`, `browserx_queue_depth`, `browserx_recoveries_total{outcome}`, `browserx_launch_seconds`, `browserx_relay_connections`, `browserx_snapshots_total{result}` and `browserx_egress_refused_total`.
- Structured logs through `tracing` (`--log-format json|text`, `RUST_LOG`). Lease tokens, API keys, proxy credentials and the CDP relay path are never logged.

## Responsible use and security

BrowserX gives automation clients, including AI agents, real browsers and network egress. It is meant for authorized security research and for automation you are permitted to run. Use it only where you have the right to: your own sites and test environments, services whose terms and owners permit automation, and proxies you are entitled to use. The project does not help you hide from a site, does not promise that any site will treat the browser a particular way, and does not accept changes aimed at that or at attacking third parties. This is the project's intended-use policy; the [AGPL-3.0-only](LICENSE) license itself is unchanged.

Security properties worth knowing before you deploy:

- The relay speaks plaintext `ws://`. Keep it on loopback or a trusted network, or terminate TLS in front of it. The `cdp_url` contains the lease token.
- Snapshots are credentials. They are encrypted at rest with a key file that you must protect and back up separately.
- Shared-browser isolation separates browser contexts. It is not a boundary against a hostile tenant; use dedicated isolation for that.
- The default egress policy refuses private, loopback, link-local and metadata destinations.
- An AI agent with browsing or interaction tools acts with the reach of the session you gave it. Scope it with `browse.allowed_origins` and an engagement window, keep `evaluate` off unless you need it, and treat page content as untrusted input.

Report vulnerabilities privately, see [SECURITY.md](SECURITY.md).

## Documentation

The [documentation index](docs/README.md) lists everything. Start here:

| If you want to | Read |
| --- | --- |
| Run BrowserX for the first time | [Getting started](docs/guides/getting-started.md) |
| Understand the model | [Architecture](docs/design/architecture.md), [sessions and leases](docs/design/sessions-and-leases.md) |
| Choose what survives a crash | [Persistence](docs/design/persistence.md), [recovery](docs/design/recovery.md) |
| Move a session between clients | [Handoff](docs/design/handoff.md) |
| Let an AI agent monitor or drive it | [MCP guide](docs/guides/mcp.md), [AI/LLM-native design](docs/design/ai-llm-native.md) |
| Move state to PostgreSQL, MariaDB, S3 or share services | [Backends](docs/guides/backends.md), [backends design](docs/design/backends.md) |
| Connect a client | [Integrating CDP clients](docs/guides/cdp-clients.md) |
| Route browser traffic through a proxy | [Using an upstream proxy](docs/guides/upstream-proxy.md) |
| Run it in production | [Operations](docs/guides/operations.md), [configuration](docs/guides/configuration.md) |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Small fixes and documentation corrections can go straight to a pull request; open an issue first for larger changes. Dependency licenses are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

BrowserX is licensed under [AGPL-3.0-only](LICENSE). Maintained by NoxRed Security Research.

**Network use.** If you modify BrowserX and let other people interact with your modified version over a network (for example by offering it as a service), section 13 of the [license](LICENSE) requires you to offer those users the corresponding source code of your version. Running an unmodified build for your own use carries no such obligation. BrowserX itself exposes no source-location endpoint; an operator who modifies it is responsible for providing one. This summary is not legal advice; the license text governs.
