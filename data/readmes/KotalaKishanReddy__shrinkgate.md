<div align="center">

# ShrinkGate

**A little less context. A little more breathing room.**

A local Rust gateway that removes repeated tool output from coding-agent requests.

[![Rust 1.85+](https://img.shields.io/badge/rust-1.85%2B-ea6344?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org) [![Crates.io](https://img.shields.io/crates/v/shrinkgate?style=flat-square&color=fc8d62&logo=rust)](https://crates.io/crates/shrinkgate) [![CI](https://github.com/KotalaKishanReddy/shrinkgate/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/KotalaKishanReddy/shrinkgate/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/KotalaKishanReddy/shrinkgate?style=flat-square&color=58a6ff&logo=github)](https://github.com/KotalaKishanReddy/shrinkgate/releases) [![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-blue?style=flat-square)](https://github.com/KotalaKishanReddy/shrinkgate) [![License](https://img.shields.io/badge/license-Apache--2.0-2ea44f?style=flat-square)](LICENSE)

[Get started](#get-started) · [See the demo](#see-it-work) · [Test results](#tested-not-assumed) · [Contribute](CONTRIBUTING.md)

<img src="docs/banner.svg" alt="Less repetition. More room to build. Earlier duplicate outputs become hash stubs; the latest identical copy stays verbatim." width="100%">

</div>

Read a file twice. Re-run the same compiler command. When identical output appears multiple times **inside one request**, ShrinkGate trims the earlier copies and keeps the latest identical copy intact.

| Small footprint | Conservative defaults | Yours to inspect |
| :--- | :--- | :--- |
| Stateless deduplication in a local Rust process. | Tool outputs only; instructions, reasoning and media stay protected. | No telemetry. Preview changes, inspect statistics, and undo the connection. |

## Get started

> [!IMPORTANT]
> The hardening and new commands on `main` are **unreleased**. Build from source to use the workflow below (requires **Rust 1.85+**). Published crates, binaries and containers still track their release tags.

```sh
git clone https://github.com/KotalaKishanReddy/shrinkgate.git
cd shrinkgate
cargo install --path . --locked

shrinkgate demo                     # Local fixture; no API keys
shrinkgate connect claude --dry-run  # Inspect the proposed settings
shrinkgate connect claude            # Or: codex / opencode
shrinkgate doctor
```

Start a new agent session after connecting. Keep using your agent's own authentication. To undo the change: `shrinkgate uninstall claude`.

<details>
<summary><strong>Install a published release instead</strong> — Cargo, verified binaries, Windows</summary>

Released commands may differ from the current source documentation. Read the matching [release notes](https://github.com/KotalaKishanReddy/shrinkgate/releases).

```sh
cargo install shrinkgate --locked
```

For a prebuilt binary without Rust or root access, download and inspect the installer, then run it:

```sh
curl --proto '=https' --tlsv1.2 -fsSLo install-shrinkgate.sh \
  https://raw.githubusercontent.com/KotalaKishanReddy/shrinkgate/main/scripts/install.sh
sh install-shrinkgate.sh
# Optional: SHRINKGATE_VERSION=v0.1.2 sh install-shrinkgate.sh
```

Windows x64 (PowerShell):

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/KotalaKishanReddy/shrinkgate/main/scripts/install.ps1 -OutFile install-shrinkgate.ps1
# Inspect the script, then:
./install-shrinkgate.ps1
```

Installers verify the matching archive's SHA-256 checksum **before extraction**. Checksums detect corrupt downloads; they are not independent publisher signatures. [Manual downloads](https://github.com/KotalaKishanReddy/shrinkgate/releases).

</details>

## See it work

![Recorded three-turn local demo: fresh output, repeated output, changed file](docs/demo.svg)

[Replay the recording](docs/demo.cast) with `asciinema play docs/demo.cast`. Playback is paced for readability; the fixture runs locally without provider credentials.

```text
Coding agent ──► ShrinkGate · 127.0.0.1:18793 ──► Your model provider
                       earlier duplicates → hash stubs
                       latest identical copy → unchanged
```

**History replay alone creates no savings.** If a payload appears only once in the current request, it stays intact. The shrink pass does not remove a sole copy because it was sent on a previous turn.

## Measure your workload

```sh
shrinkgate benchmark --iterations 500
shrinkgate benchmark --input private-request.json
shrinkgate stats --json
```

The built-in fixtures include repeated output, unique output, changed files and short messages. Local counters estimate tokens as candidate UTF-8 bytes ÷ 4; provider usage is reported separately.

**Smaller requests do not automatically mean a smaller bill.** Rewriting can invalidate provider prompt caches, change model interpretation, or affect latency. No universal savings percentage or unchanged-behavior guarantee is claimed.

[Benchmark results](docs/benchmark.json) · [How to measure real savings](docs/BENCHMARKS.md) · [Validation report](docs/VALIDATION.md)

## Tested, not assumed

The [follow-up audit fixes](docs/AUDIT-FIXES.md) cover provider routing, settings/service ownership, stream outcomes, diagnostics and bounded journaling.

| Check | Evidence and boundary |
| :--- | :--- |
| Linux · macOS · Windows | [CI](https://github.com/KotalaKishanReddy/shrinkgate/actions/workflows/ci.yml): build, lint, protocol and recovery tests |
| Installed Codex client | `0.167.0-alpha.4`: local Responses fixture, streaming, dummy-auth forwarding, 401 failure and config restoration verified |
| Extended gateway run | A bounded Linux soak covers three API formats, long request histories, errors, cancellation and restart; [recorded results](docs/VALIDATION.md) |
| Live ChatGPT authentication | Blocked: the available sign-in returns HTTP 401 even without ShrinkGate |
| Real billed savings | Blocked: no metered provider credentials; local byte estimates are not a substitute |

A client passing a local fixture does not certify its live provider or every agent feature. [Exact coverage and release gates →](docs/COMPATIBILITY.md)

## Bring your agent

| Agent | Connect | Notes |
| :--- | :--- | :--- |
| **Claude Code** | `shrinkgate connect claude` | Messages API; optional `--lean` and `--statusline`; live authentication unverified |
| **Codex** | `shrinkgate connect codex` | Responses API; `--env-key OPENAI_API_KEY` for API-key mode; live sign-in currently blocked |
| **OpenCode** | `shrinkgate connect opencode` | Adds providers; select a `shrinkgate/` model; explicit Meta/Zen routing |
| **Other HTTP clients** | `shrinkgate env` | Messages, Chat Completions and Responses; HTTP/SSE, no WebSockets |

Muse is an experimental helper, not a verified integration. It requires `default_upstream = "meta"`. See [compatibility notes](docs/COMPATIBILITY.md).

<details>
<summary><strong>CLI reference</strong></summary>

| Command | Purpose |
| :--- | :--- |
| `serve [--port N] [--no-shrink]` | Foreground gateway; bypass mode preserves request body bytes |
| `connect <agent> [--dry-run] [--no-service]` | Preview or connect, with a saved recovery snapshot |
| `uninstall <agent>` | Restore managed settings while preserving external edits |
| `doctor` | Check local identity, version, configuration and wiring |
| `status [agent]` / `stats [--json]` | Wiring, estimated reductions, provider usage and failed attempts |
| `demo` / `benchmark` | Offline proxy demo and transformation measurements |
| `lean on\|off\|status` | Optional Claude compaction setting |
| `env` / `config` / `statusline` | Manual routing, resolved options and terminal summary |

</details>

## Local by design

ShrinkGate binds loopback and forwards requests to your configured provider. It adds no telemetry or extra forwarding destination. It is intended for a trusted, single-user workstation.

Prompts and auth headers are not journaled. Usage metadata stays local. Observed usage from failed or cancelled requests remains visible separately from estimated reductions. Recovery snapshots can contain secrets already present in your agent settings; protect them and avoid sharing dry-run output.

[Configuration, limits & Docker](docs/OPERATIONS.md) · [Security & privacy](SECURITY.md) · [Audit findings](docs/AUDIT.md)

---

**Help make the next release dependable.** Share a sanitized compatibility report, contribute a realistic fixture, or pick a task from the [roadmap](docs/ROADMAP.md). If ShrinkGate helps your workflow, a star helps others find it.

<sub>Apache-2.0 · Not affiliated with Anthropic, OpenAI, Meta, or Context Shrink LLC.</sub>
