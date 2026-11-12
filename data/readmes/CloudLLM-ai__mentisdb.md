<img src="logo.svg" alt="MentisDB logo" height="48" align="left" style="margin-right:12px" />

# MentisDB

MentisDB is a **durable semantic memory engine and versioned skill registry** for AI agents — a persistent, hash-chained brain that survives context resets, model swaps, and team turnover.

It stores semantically typed thoughts in an append-only, hash-chained memory log through a swappable storage adapter layer. The skill registry is a git-like immutable version store for agent instruction bundles — every upload is a new version, history is never overwritten, and every version is cryptographically signable.

---

## Why MentisDB

**Harness Swapping** — the same durable memory works across every AI coding environment. Connect Claude Code, OpenAI Codex, GitHub Copilot CLI, Qwen Code, Cursor, VS Code, or any MCP-capable host to the same `mentisdb` daemon and your agents share one brain, regardless of which tool you picked up today.

**Zero Knowledge Loss Across Context Boundaries** — when an agent's context window fills, it writes a `Summary` checkpoint to MentisDB, compacts, reloads `mentisdb_standing_context` (what is durably true, at any age) and `mentisdb_recent_context` (where it left off), and continues. Chat history is ephemeral. MentisDB is permanent.

**Fleet Orchestration at Scale** — one project manager agent decomposes work, dispatches a parallel fleet of specialists, each pre-warmed with shared memory, and synthesizes results wave by wave. MentisDB is the coordination substrate: every agent reads from the same chain and writes its lessons back. The fleet's collective intelligence compounds.

**Versioned Skill Registry** — skills are not just stored, they are versioned like a git repository. Every upload to an existing `skill_id` creates a new immutable version (stored as a unified diff). Any historical version is reconstructable. Skills can be deprecated or revoked while full audit history is preserved. Permanent delete is the explicit exception: it removes the skill and all versions so the same `skill_id` can be reused. Uploading agents with registered Ed25519 keys must cryptographically sign their uploads — provenance is verifiable, not assumed.

**Session Resurrection** — any agent can call `mentisdb_recent_context` and immediately know exactly where the project stands, what decisions were made, what traps were already hit, and what comes next — without re-reading code, re-running exploratory searches, or asking the human to re-explain context that was earned through hours of work.

**Self-Improving Agent Fleets** — agents upload updated skill files after learning something new. A skill checked in at the start of a project is better by the end of it. Agents with registered Ed25519 keys must sign their uploads, so each skill version records which agent authored it. (The skill registry is integrity-checked as a file; unlike thought chains, it is not hash-chained.)

**Multi-Agent Shared Brain** — multiple agents, multiple roles, multiple owners can write to the same chain key simultaneously. Every thought carries a stable `agent_id`. Queries filter by agent identity, thought type, role, tags, concepts, importance, and time windows. The chain represents the full collective intelligence of an entire orchestration system, not just one session.

**Lessons That Outlive Models** — architectural decisions, hard constraints, non-obvious failure modes, and retrospectives written to MentisDB survive chat loss, model upgrades, and team changes. The knowledge compounds instead of evaporating. A new engineer or a new agent boots up, loads the chain, and inherits everything the team learned.

---

## Installation

### Prerequisites

#### macOS

Install the Xcode Command Line Tools (required for native crates):

```bash
xcode-select --install
```

#### Ubuntu / Debian

On a fresh Ubuntu or Debian system you need a few development packages before `cargo install` will succeed (especially because the default build enables audio support for the TUI startup chime).

```bash
sudo apt update
sudo apt install -y \
    build-essential \
    pkg-config \
    libssl-dev \
    libasound2-dev \
    curl
```

Then install Rust 1.90 or newer (if you don't already have it; `rustup update` upgrades an older one):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

**Headless servers / minimal installs**

If you are installing on a server and do not want the startup sound (and the ALSA dependency), install without the default features:

```bash
cargo install mentisdb --no-default-features --features server
```

This produces a smaller binary with no audio dependencies.

### Prebuilt binaries

Every [GitHub release](https://github.com/CloudLLM-ai/mentisdb/releases) ships
ready-to-run `mentisdb` binaries for macOS (`mentisdb-macos-arm64`,
`mentisdb-macos-x86_64`), Windows (`mentisdb-windows-x86_64.exe`) and Linux.
Linux binaries come in two flavours (since 0.10.10, [#21](https://github.com/CloudLLM-ai/mentisdb/issues/21)):

| Asset | Local embeddings (FastEmbed) | Minimum glibc | Runs on |
| --- | --- | --- | --- |
| `mentisdb-linux-x86_64`, `mentisdb-linux-arm64` | yes | 2.39 | Ubuntu 24.04+, Debian 13+, Fedora 40+, RHEL 10, Arch |
| `mentisdb-linux-x86_64-compat`, `mentisdb-linux-arm64-compat` | no | 2.34 | Ubuntu 22.04 LTS, Debian 12, RHEL 9, and everything newer |

The full builds need a recent glibc because the prebuilt ONNX Runtime they link
for local embeddings is itself built against glibc 2.38+. The `-compat` builds are
compiled on Ubuntu 22.04 without the `local-embeddings` and `startup-sound`
features: lexical search and `local-text-v1` vectors work as usual, but there is no
`fastembed-minilm` semantic vector provider (the same trade-off as the Intel macOS
binary) and no startup chime, so they need no ALSA (`libasound.so.2`) on the host. Release
CI fails the build if a `-compat` binary ever needs a glibc newer than 2.35.

Check your glibc before picking one:

```bash
ldd --version | head -1     # e.g. "ldd (Ubuntu GLIBC 2.35-0ubuntu3) 2.35"
```

A full binary started on an older glibc fails immediately with
``version `GLIBC_2.39' not found``. If you are on an older distro and want local
embeddings, use the [Docker image](#docker): it is self-contained and has full
features regardless of the host's glibc. (Building from source with
`--features local-embeddings` does not avoid the floor, because the ONNX Runtime
library it downloads needs glibc 2.38+ too.)

```bash
# Example: Ubuntu 22.04 on x86_64
curl -fLo mentisdb https://github.com/CloudLLM-ai/mentisdb/releases/latest/download/mentisdb-linux-x86_64-compat
chmod +x mentisdb && ./mentisdb --help
```

### Docker

Release images are published to GitHub Container Registry for `linux/amd64` and
`linux/arm64` (first published with 0.10.10.55). Tags: the release tag (for example
`0.12.2.59`), the crate version (`0.12.2`, moves with each release of that version)
and `latest`. This is also the way to get full features, including local embeddings,
on Linux distros older than glibc 2.39 (see [Prebuilt binaries](#prebuilt-binaries)).

```bash
docker run -d --name mentisdb \
  -p 127.0.0.1:9471:9471 -p 127.0.0.1:9472:9472 -p 127.0.0.1:9475:9475 \
  -v mentisdb-data:/var/lib/mentisdb \
  ghcr.io/cloudllm-ai/mentisdb:latest
```

**Always publish the ports on loopback** (`-p 127.0.0.1:9471:9471`, as above). Inside the
container the daemon binds `0.0.0.0` (needed for published ports to work) with bearer tokens
and the dashboard PIN off, so a bare `-p 9471:9471` exposes an unauthenticated memory store to
every machine that can reach the host. The daemon does not refuse to start in that state, but
it says so: a `SECURITY:` warning in `docker logs` (stderr and the log), in the terminal UI
and as a red banner at the top of the dashboard, whenever a listener is bound to a
non-loopback address while `MENTISDB_BEARER_TOKEN_ACCESS` is off (MCP/REST) or no
`MENTISDB_DASHBOARD_PIN` is set (dashboard). Before exposing the container beyond the host,
set both (see the Compose example and the security notes below).

The entrypoint is `mentisdb --headless` under `tini`, so no TTY (`-t`) is needed
and `docker stop` (SIGTERM) drains the servers and exits cleanly. Check it with
`curl http://127.0.0.1:9472/health`; the image also has a Docker `HEALTHCHECK`.

Docker Compose:

```yaml
services:
  mentisdb:
    image: ghcr.io/cloudllm-ai/mentisdb:latest
    restart: unless-stopped
    ports:
      - "127.0.0.1:9471:9471"   # MCP (HTTP)
      - "127.0.0.1:9472:9472"   # REST (HTTP)
      - "127.0.0.1:9475:9475"   # dashboard (HTTPS, self-signed)
    volumes:
      - mentisdb-data:/var/lib/mentisdb
    environment:
      MENTISDB_BEARER_TOKEN_ACCESS: "true"
      MENTISDB_DASHBOARD_PIN: "change-me"
volumes:
  mentisdb-data:
```

| Item | Value |
| --- | --- |
| Data volume | `/var/lib/mentisdb` (`MENTISDB_DIR`). Chains, the skill registry, TLS certificates and the local-embedding model cache (`.fastembed_cache`, downloaded on first use) all live here. |
| User | non-root `mentisdb` (uid/gid `991`). Bind mounts must be writable by uid 991 (`chown 991:991 ./data`). |
| Ports | `9471` MCP (HTTP), `9472` REST (HTTP), `9475` dashboard (HTTPS). HTTPS MCP/REST (`9473`/`9474`) are off in the image; set `MENTISDB_HTTPS_MCP_PORT` / `MENTISDB_HTTPS_REST_PORT` to enable them. |
| Configuration | any variable from [Daemon Configuration](#daemon-configuration), passed with `-e` or `environment:`. |
| Base image | `debian:trixie-slim` (glibc 2.41). The ONNX Runtime used for local embeddings needs glibc 2.38+; the image is self-contained, so your host's glibc does not matter. |
| Features | server + local embeddings + LLM extraction; the startup-sound/audio feature is not compiled in. |

**Security notes.** Inside the container the daemon binds `0.0.0.0` (required for
published ports to work), and a fresh daemon has no authentication. Therefore:

- Publish ports on loopback (`-p 127.0.0.1:...`) unless you put a TLS reverse proxy
  or VPN in front. Never publish `9471`/`9472` to the open internet as-is.
- For any access beyond the host, set `MENTISDB_BEARER_TOKEN_ACCESS=true` and create
  tokens: `docker exec mentisdb mentisdb bearertoken create --global admin`.
- Set `MENTISDB_DASHBOARD_PIN`, and list the hostnames you reach the dashboard by in
  `MENTISDB_DASHBOARD_ALLOWED_HOSTS` (the dashboard rejects unknown `Host` headers, and
  browsers calling REST or MCP must name an allowed host too; see
  [Host allowlist](#host-allowlist)).
- Run one container per data volume. Since 0.11 a second daemon on a data directory that
  is already in use refuses to start.
- Back up the volume (`docker run --rm -v mentisdb-data:/d -v "$PWD":/b debian tar czf /b/mentisdb.tgz -C /d .`)
  after stopping the container.

Build locally with `make docker-build` (or `docker build -t mentisdb .`).


---

## Quick Start

Install the daemon (after completing the platform-specific prerequisites above):

```bash
cargo install mentisdb --features local-embeddings
```

The `local-embeddings` feature enables the built-in `fastembed-minilm` ONNX embedding provider for real semantic vector search. Without it, MentisDB falls back to `local-text-v1` (text hashing). The auto-updater also installs with `--features local-embeddings`.

The prebuilt Intel macOS (`x86_64-apple-darwin`) release binary is built **without** `local-embeddings`, because ONNX Runtime ships no prebuilt library for that target; it uses `local-text-v1` vectors. The same applies to the `mentisdb-linux-*-compat` binaries for older glibc (see [Prebuilt binaries](#prebuilt-binaries)). Every other release binary includes FastEmbed. Builds with `--no-default-features` (optionally re-adding `--features server` etc.) are supported.

Connect your local AI tools the fast way:

```bash
mentisdb wizard
```

Or target one integration explicitly:

```bash
mentisdb setup codex
mentisdb setup all --dry-run
mentisdb wizard
mentisdb add "The sky is blue"
mentisdb search "cache invalidation" --limit 5 --scope session
mentisdb agents
```

Then start the daemon:

```bash
mentisdb
```

When run in an interactive terminal, `mentisdb` launches a **full TUI** with
scrollable panes for configuration, chain/agent/skill tables, and a live event
log. On an interactive first run with no configured client integrations, it
offers to launch the setup wizard immediately after startup so you do not have
to guess the next command.

Run persistently after closing your SSH session:

```bash
nohup mentisdb &
```

**Headless mode.** The daemon now auto-promotes to headless HTTP mode
whenever stdin or stdout is not a TTY — so every common non-interactive
launch (Docker without `-t`, `nohup mentisdb &`, `systemd` without
`StandardInput=tty`, `cron`, an SSH session that was disconnected) gets
the right behavior automatically without you having to remember the
flag. To force the headless code path on a machine that does have a
TTY (for testing, or to suppress the dashboard), pass the explicit
flag:

```bash
mentisdb --headless               # HTTP/MCP/REST only, no TUI
mentisdb --mode http --headless   # equivalent; the stdio-proxy form
```

Both forms are accepted in either flag order. `mentisdb --help` lists the
flag in the Usage block and gives a full description under Flags.

Modern MCP clients bootstrap themselves from the MCP handshake:

- `initialize.instructions` tells the agent to read `mentisdb://skill/core`
- `resources/read(mentisdb://skill/core)` delivers the embedded operating skill
- `GET /mentisdb_skill_md` remains available only as a compatibility fallback

If you need to wire a tool manually, here are the raw MCP commands/configs:

```bash
# Claude Code
claude mcp add --transport http mentisdb http://127.0.0.1:9471

# OpenAI Codex
codex mcp add mentisdb --url http://127.0.0.1:9471

# Qwen Code
qwen mcp add --transport http mentisdb http://127.0.0.1:9471

# GitHub Copilot CLI — use /mcp add in interactive mode,
# or write ~/.copilot/mcp-config.json manually (see below)
```

---

## What Is In This Folder

`mentisdb/` contains:

- the standalone `mentisdb` library crate
- server support for HTTP MCP and REST, enabled by default
- the `mentisdb` daemon binary
- dedicated tests under `mentisdb/tests`

---

## Makefile

A `Makefile` is included at the repository root. All common workflows have a target:

```bash
make build          # fmt + release build
make build-mentisdb # build only the daemon binary
make release        # fmt, check, clippy, build, test, doc in sequence
make fmt            # cargo fmt
make check          # cargo check (lib + binary)
make clippy         # cargo fmt + clippy --all-targets -D warnings
make test           # cargo test
make bench          # Criterion benchmarks, output tee'd to /tmp/mentisdb_bench_results.txt
make doc            # cargo doc --all-features
make coverage       # tests under instrumentation: functions, branches, regions, lines (pinned nightly)
make install        # cargo install --path . --locked --features local-embeddings
make publish        # cargo publish
make publish-dry-run
make clean
make help           # list all targets with descriptions
```

---

## Build

```bash
make build
```

Or directly with Cargo:

```bash
cargo build --release
```

Build only the library without the default daemon/server stack:

```bash
cargo build --no-default-features
```

---

## Test

```bash
make test
```

Or directly:

```bash
cargo test
```

Run tests for the library-only build:

```bash
cargo test --no-default-features
```

Run rustdoc tests:

```bash
cargo test --doc
```

---

## Coverage

`.github/workflows/coverage.yml`, `scripts/coverage_gate.py`, `make coverage`.

Every CI run writes a coverage table into the run's job summary (the "Summary"
page of the `Coverage` workflow run), with **functions, branches, regions and
lines** as percentages with covered/total counts, a goal column (90%, with a
check mark or a cross per dimension) and the gate result. The HTML report and
`summary.json` are uploaded as the `coverage-report` artifact.

Run it locally, identically to CI:

```bash
cargo install cargo-llvm-cov --version 0.9.1 --locked
rustup toolchain install nightly-2026-10-01 --profile minimal --component llvm-tools-preview
make coverage          # table on stdout and in target/coverage/summary.md
make coverage-open     # same, then open target/coverage/html/index.html (macOS)
```

**One nightly run reports everything.** Branch coverage only exists on nightly
(`cargo +nightly llvm-cov --branch`, the unstable `-Z coverage-options=branch`),
and nightly's region and line numbers differ a little from stable's. Mixing a
stable run with a nightly run in one table would put numbers from two different
instrumentations side by side, so the whole suite runs once, on a nightly pinned
by date (`COVERAGE_NIGHTLY` in the `Makefile`, the same date in `coverage.yml`),
and all four dimensions come from that one profile. The table names the
toolchain. Pinning means a nightly that changes the flag cannot break CI; bump
the date deliberately, in its own commit, and re-measure. The run uses
`--all-features`, like the `Tests` workflow, and covers integration and unit
tests (not doctests). There is no `lcov.info`: this nightly's lcov exporter crashes on branch
data, so the artifact is the HTML report and `summary.json`.

**Nothing is excluded.** The measurement covers all of `src/`, including the
terminal UI and the daemon binary. The numbers below are low partly because
those are big and lightly tested; they are listed as gaps, not hidden.

**Goal and floor.** The goal is 90% on every dimension. Measured on
2026-11-08 (`nightly-2026-10-01`, `--all-features`), none meets it yet, so the
gate is a floor at each measured value rounded down, so coverage cannot regress:

| Dimension | Measured | Covered / total | Floor |
|---|---:|---:|---:|
| Functions | 73.54% | 3,689 / 5,016 | 73% |
| Branches | 64.30% | 4,007 / 6,232 | 64% |
| Regions | 72.07% | 33,505 / 46,490 | 72% |
| Lines | 74.24% | 33,933 / 45,710 | 74% |

The floors are `COVERAGE_FLOOR_*` in the `Makefile`. **They ratchet up toward
90 and are never lowered to land a change**: when a change raises a dimension,
raise its floor to the new value rounded down in the same commit; a dimension
that reaches 90 is gated at 90. A change that adds untested code fails the job;
the fix is a test, not a lower floor.

**Biggest uncovered areas** (uncovered regions, the roadmap to 90%):

| File | Uncovered regions | Regions covered |
|---|---:|---:|
| `src/dashboard.rs` | 2,524 | 9.5% |
| `src/bin/mentisdb.rs` | 2,083 | 14.7% |
| `src/lib.rs` | 1,878 | 78.8% |
| `src/tui.rs` | 1,165 | 2.2% |
| `src/server.rs` | 1,070 | 85.0% |
| `src/search/lemmas.rs` | 291 | 52.2% |
| `src/cli/mod.rs`, `src/cli/wizard.rs`, `src/cli/setup.rs`, `src/cli/args.rs` | 912 together | 35% to 65% |

The first four files hold about 7,650 of the 12,985 uncovered regions
(59%); testing the dashboard handlers, the daemon's `main` path as a process
and the terminal views against a test buffer is most of the way to 90%.

---

## Benchmarks

MentisDB ships a Criterion benchmark suite and a harness-free HTTP concurrency benchmark:

```bash
make bench
```

Or directly:

```bash
cargo bench
```

Results are also written to `/tmp/mentisdb_bench_results.txt` so numbers persist across terminal sessions.

Benchmark coverage:

- `benches/thought_chain.rs` — 10 benchmarks: append throughput, query latency, traversal patterns
- `benches/search_baseline.rs` — 4 benchmarks: lexical/filter-first search baseline over content, registry text, indexed+text intersections, and newest-tail limits
- `benches/search_ranked.rs` — 4 benchmarks: additive ranked retrieval over lexical content, filtered ranked queries, and heuristic fallback, plus a baseline append-order comparison
- `benches/skill_registry.rs` — 12 benchmarks: skill upload, search, delta reconstruction, lifecycle
- `benches/http_concurrency.rs` — starts `mentisdb` in-process on a random port; measures write and read throughput at 100 / 1k / 10k concurrent Tokio tasks with p50/p95/p99 latency reporting

Baseline numbers from the `DashMap` concurrent chain lookup refactor: **750–930 read req/s at 10k concurrent tasks**, compared to a sequential bottleneck on the previous `RwLock<HashMap>` implementation.

---

## Generate Docs

```bash
make doc
```

Or directly:

```bash
cargo doc --no-deps
```

Generate docs for the library-only build:

```bash
cargo doc --no-deps --no-default-features
```

---

## Run The Daemon

The standalone executable is `mentisdb`.

Run it from source:

```bash
cargo run --bin mentisdb
```

Install it from the crate directory:

```bash
make install
# or
cargo install --path . --locked
```

`mentisdb` now owns both daemon startup and local integration setup:

```bash
mentisdb setup codex
mentisdb setup all --dry-run
mentisdb wizard
mentisdb add "The sky is blue"
mentisdb search "cache invalidation" --limit 5 --scope session
mentisdb agents
mentisdb
```

When it starts, it serves:

- an MCP server
- a REST server
- an HTTPS web dashboard

Before serving traffic, it:

- refuses to start on a data directory written by a newer `mentisdb` (a downgrade), without touching it
- recovers any chain migration the previous process died in (a journal lookup per chain)
- migrates the skill registry from V1 to V2 format if needed (idempotent; safe to run repeatedly)

Chain format upgrades (legacy schemas, JSONL, the legacy hash algorithm) do **not** run before
serving: the daemon comes up in about a second and migrates those chains in the background, a few
at a time, while it serves every other chain. See [Upgrading and chain migrations](#upgrading-and-chain-migrations).

Once startup completes, it prints:

- the active chain directory, default chain key, and bound MCP/REST/dashboard addresses
- a catalog of all exposed HTTP endpoints with one-line descriptions
- a per-chain summary with version, adapter, thought count, and per-agent counts

---

## Command-Line Interface

The `mentisdb` binary is a complete command-line client for everything the MCP
tools, the REST API and the web dashboard can do. Commands are
`mentisdb <group> <command> [options]`; run `mentisdb --help` for the
overview, `mentisdb <group> --help` for a group, and
`mentisdb <group> <command> --help` for flags and copy-paste examples.
[`docs/CLI_PARITY.md`](docs/CLI_PARITY.md) maps every MCP tool, REST route and
dashboard action to its command.

| Group | What it covers |
|---|---|
| `thought` | `append`, `retro`, `get`, `genesis`, `traverse`, `recent`, `candidates` |
| `search` | ranked (default), `lexical`, `filter`, `federated`, `bundles` |
| `chain` | `list`, `head`, `bootstrap`, `branch`, `merge`, `info`, `delete`, `access show\|set\|allow\|deny\|verify` |
| `agent` | `list`, `get`, `registry`, `upsert`, `describe`, `alias`, `key add`, `key revoke`, `disable`, `activate`, `copy` |
| `entity-type` | `list`, `upsert` |
| `memory` | `export`, `import`, `extract` (MEMORY.md style Markdown) |
| `skill` | `guide`, `manifest`, `list`, `search`, `read`, `versions`, `upload`, `deprecate`, `revoke`, `delete`, `diff` |
| `webhook` | `list`, `register`, `delete` |
| `vectors` | `enable`, `disable`, `sync`, `rebuild` |
| `daemon` | `health`, `version`, `flush`, `restart`, `settings list`, `settings set` |
| local | `setup`, `wizard`, `add`, `backup`, `restore`, `bearertoken`, `cert`, `key generate\|show` (plus operator `agent key generate`) |

```bash
mentisdb chain bootstrap "Project Atlas memory" --chain atlas
mentisdb thought append "Use UTC everywhere" --chain atlas --type Decision --tag time
echo "deploy finished" | mentisdb thought append - --chain atlas --type Summary --role Checkpoint
mentisdb search "why UTC" --chain atlas --type Decision --limit 5
mentisdb memory export --chain atlas > MEMORY.md
mentisdb chain delete scratch --yes --pin 123456
```

Daemon commands talk to the running daemon so they share its chain cache and
locks: memory and registry commands use the REST API at `--url` (default
`http://127.0.0.1:9472`, bearer token from `--token` or `MENTISDB_BEARER_TOKEN`),
while the PIN-gated dashboard actions (`chain info/delete`, `vectors
enable/disable/sync`, `skill diff`, `agent copy`, `daemon version/restart/settings`)
use the dashboard API at `--dashboard-url` (default `https://127.0.0.1:9475`,
PIN from `--pin` or `MENTISDB_DASHBOARD_PIN`). `--json` prints compact JSON for
pipes; destructive commands require `--yes`. `backup`, `restore`, `bearertoken`
and `cert` work on the data directory directly and do not need the daemon.

## Daemon Configuration

`mentisdb` is configured with environment variables:

- `MENTISDB_DIR`
  Directory where MentisDB storage adapters store chain files.
- `MENTISDB_DEFAULT_CHAIN_KEY`
  Default `chain_key` used when requests omit one. Default: `borganism-brain`.
  `MENTISDB_DEFAULT_KEY` is accepted as a deprecated alias.
- `MENTISDB_STORAGE_ADAPTER`
  Default storage backend for newly created chains. Only `binary` is supported for
  new chains (JSONL is deprecated — existing JSONL chains remain readable).
  Default: `binary`
- `MENTISDB_VERBOSE`
  When unset, verbose interaction logging defaults to `true`. Supported explicit values:
  `1`, `0`, `true`, `false`.
- `MENTISDB_LOG_FILE`
  Optional path for interaction logs. When set, MentisDB writes interaction logs to that file
  even if console verbosity is disabled. If `MENTISDB_VERBOSE=true`, the same lines are also
  mirrored to the console logger.
- `MENTISDB_BIND_HOST`
  Bind host for both HTTP servers. Default: `127.0.0.1`. It is also one of the names the
  daemon answers to in the `Host` header (see "Host allowlist" below).
- `MENTISDB_MCP_PORT`
  MCP server port. Default: `9471`
- `MENTISDB_REST_PORT`
  REST server port. Default: `9472`
- `MENTISDB_KEY_DIR`
  Directory `mentisdb key generate` saves private keys in when `--out` is not given.
  Default: `~/.mentisdb/keys` (created `0700`, files `0600`). The seed is never printed.
- `MENTISDB_DASHBOARD_PORT`
  HTTPS dashboard port. Default: `9475`. Set to `0` to disable the web dashboard.
- `MENTISDB_DASHBOARD_PIN`
  Optional PIN required to access the dashboard. Leave unset only for trusted localhost use.
- `MENTISDB_DASHBOARD_ALLOWED_HOSTS`
  Comma-separated extra hostnames or IPs the dashboard accepts in the `Host` header (for
  example a public DNS name or the name a reverse proxy forwards). Set it in the environment
  or a `.env` file (`./.env` or `<MENTISDB_DIR>/.env`); it is not editable from the dashboard Settings
  tab. The MCP and REST listeners use the same list. See "Host allowlist" below for the
  built-in names and how each listener applies them. Set it before the daemon starts.
- `MENTISDB_WEBHOOK_ALLOWED_CIDRS`
  Private ranges webhooks may target despite the SSRF guard, for self-hosted consumers on a
  private network. One or more CIDRs or bare IPs separated by commas and/or whitespace, e.g.
  `100.64.0.0/10,fd7a:115c:a1e0::/48` (Tailscale). Unset (default) keeps every internal range
  blocked; an invalid value or an entry broader than `/8` (IPv4 or IPv6) stops the daemon
  from starting. Set it in the
  environment or a `.env` file (`./.env` or `<MENTISDB_DIR>/.env`). See "Webhook targets" below.
- `MENTISDB_MAX_BODY_BYTES`
  Largest body, in bytes, the import routes (`/v1/import-markdown`, `/v1/skills/upload`,
  `/v1/extract-memories`) accept from an authenticated caller. Default: `67108864` (64 MiB); must be
  `1048576` to `1073741824` (1 MiB to 1 GiB), otherwise the daemon refuses to start. Every other route
  takes at most 2 MiB; over the limit the answer is `413`. See [Large request bodies](#large-request-bodies).
- `MENTISDB_MAX_INFLIGHT_BODY_BYTES`
  Body bytes all *import* requests in flight may hold together. Default: four times `MENTISDB_MAX_BODY_BYTES`
  (one peer may hold twice the cap and four bodies); a smaller value is raised to one cap. Beyond it the answer is
  `503` with `Retry-After`. Ordinary requests have their own fixed 64 MiB pool and are never starved by imports.
- `MENTISDB_BODY_IDLE_TIMEOUT_SECS`
  A request body that delivers no data for this long fails. Default: `30`; `1` to `3600`.
- `MENTISDB_MIN_BODY_BYTES_PER_SEC`
  Slowest rate a request body may sustain, measured over each window of one idle timeout once a grace
  period (twice the idle timeout) is over; a slower body fails with `408`. Default: `65536` (64 KiB/s);
  `0` switches the rule off (the idle timeout and deadlines still apply). Lower it for imports over a
  slow link, or on a busy server that reads bodies late; `0` to `1073741824`.
- `MENTISDB_BEARER_TOKEN_ACCESS`
  Require bearer tokens for MCP requests. Default: `false`. Set `true` for remote
  or multi-user MCP servers. This can also be toggled live from the dashboard Settings screen.
- `MENTISDB_AUTO_FLUSH`
  Controls per-write durability of the `binary` storage adapter.
  - `true` (default): every `append_thought` returns only after its group commit has been
    written to the chain file. Survives a process crash; add `MENTISDB_FSYNC=1` to also
    survive power loss.
  - `false`: appends are queued to a background writer (queue capacity 128 records, then
    callers wait) and flushed every 16 appends (`FLUSH_THRESHOLD`). On a hard crash or power
    failure everything still queued is lost: up to 128 records, not 15, because the flush
    cadence is not the queue bound. Throughput rises significantly for multi-agent hubs with
    many concurrent writers.
  Supported values: `1`, `0`, `true`, `false`. Has no effect on the `jsonl` adapter.
- `MENTISDB_GROUP_COMMIT_MS`
  Group-commit window in milliseconds for the background binary writer.
  The writer batches appends that are already queued, waiting up to this window for
  more; when no other append is queued it flushes immediately, so a lone append never
  pays the window. Lower values = lower latency; higher values = better throughput.
  Default: `2`
- `MENTISDB_FSYNC`
  Set `1` (or `true`, `on`, `yes`) to `fsync` the chain file after every group commit,
  for power-loss durability. Default: off — each group commit is written to the OS
  (survives a process crash) but not forced to the device, because a per-commit fsync
  roughly quadruples append latency (`F_FULLFSYNC` on macOS). Explicit flushes
  (`POST /v1/admin/flush`), clean shutdown and dropping a chain handle always sync.
- `MENTISDB_MIGRATION_CONCURRENCY`
  How many chains the background migration manager rewrites at once. Default: `2`.
  See [Upgrading and chain migrations](#upgrading-and-chain-migrations).
- `MENTISDB_MIGRATION_BACKUP_RETENTION_DAYS`
  How long the preserved original of a migrated chain is kept under
  `<MENTISDB_DIR>/migrations/backup/`. Default: `14`; `0` keeps backups forever.
- `MENTISDB_EMBEDDINGS`
  Process-wide embeddings mode for managed vector sidecars: `off` (lexical/graph only),
  `local-text` (built-in hashing embeddings, never loads ONNX) or `fastembed`. Unset
  means FastEmbed when the `local-embeddings` feature is compiled in, `local-text`
  otherwise. Unknown values are logged and treated as unset.
- `MENTISDB_DF_SCOPE`
  How the lexical stop-word gate measures a term's document frequency: `global`
  (default, what every published benchmark used: a thought counts if the term is in
  *any* field, including agent registry text) or `field` (each field's own count).
  Experimental; see `WHITEPAPER.md` section 6.3.
- `MENTISDB_VECTOR_FUSION`
  How vector similarity is blended with the lexical score: `relative` (default; the
  decay depends on a hit's lexical score relative to the query's best, so paraphrased
  questions keep the vector channel) or `absolute` (the older raw-BM25 decay, which
  silences vectors for queries longer than a few words). On LoCoMo R@10 and
  LongMemEval R@5 `relative` scored 75.2% and 70.0% against 73.1% and 68.0%.
- `MENTISDB_COLLAPSE_DUPLICATES`
  Result-time collapse of exact and near-duplicate hits: a number in `(0, 1]` is the
  Jaccard threshold (default `0.9`), `off` disables it. Collapsed ids are listed in
  `collapsed_duplicates` on the surviving hit. Per request: `collapse_duplicates`
  (`0` disables). Text queries only.
- Per-request ranking knobs (REST/MCP fields and CLI flags, see `docs/CLI_PARITY.md`):
  `resolve_successors`, `collapse_duplicates`, `vector_fusion`, `synonym_weight`
  (automatic thesaurus expansion, default 0.3, `0` disables; the library applies it
  by default too), `df_scope` and `df_cutoffs`.
- `FASTEMBED_CACHE_DIR`
  Where the FastEmbed ONNX model is cached. Default: `<MENTISDB_DIR>/.fastembed_cache`.
- `MENTISDB_UPDATE_CHECK`
  Background GitHub release check for `mentisdb`. Enabled by default; set `0`, `false`, `no`,
  or `off` to disable update checks after startup. Default: `true`
- `MENTISDB_UPDATE_REPO`
  Optional GitHub `owner/repo` override used by the updater. Default: `CloudLLM-ai/mentisdb`
- `MENTISDB_HTTPS_MCP_PORT`
  HTTPS MCP server port. Default: `9473`. Set to `0` to disable HTTPS MCP.
- `MENTISDB_HTTPS_REST_PORT`
  HTTPS REST server port. Default: `9474`. Set to `0` to disable HTTPS REST.
- `MENTISDB_TLS_CERT`
  Path to a PEM-encoded TLS certificate for the HTTPS servers and dashboard.
  Default: `<MENTISDB_DIR>/tls/cert.pem`
- `MENTISDB_TLS_KEY`
  Path to a PEM-encoded TLS private key for the HTTPS servers and dashboard.
  Default: `<MENTISDB_DIR>/tls/key.pem`
- `MENTISDB_STARTUP_SOUND`
  Play the 4-note "men-tis-D-B" startup jingle. Default: `true`. Set `0`, `false`, `no`,
  or `off` to silence.
- `MENTISDB_THOUGHT_SOUNDS`
  Play unique short sounds for thought types on append (square-wave, 250–1,000 Hz) and
  for read operations (sine-wave, 2,500–4,500 Hz). Default: `false`. Set `1`, `true`,
  `yes`, or `on` to enable.
- `MENTISDB_DEDUP_THRESHOLD`
  Jaccard similarity threshold for automatic deduplication on append (0.0–1.0). When
  unset, auto-dedup is **disabled** (library and daemon default). When set, a new
  thought whose content is sufficiently similar to a recent thought gets an automatic
  `Supersedes` edge to that prior thought (the prior stays on disk for audit).
  **Recommended for multi-agent and long-lived chains:** `0.85`. Without this (or
  without agents writing `Supersedes` / `Corrects` / `Invalidates`), the invalidation
  set stays empty and search cannot hide near-duplicate noise.
- `MENTISDB_DEDUP_SCAN_WINDOW`
  Number of recent thoughts to scan for dedup comparison. Default: `64`. Only used
  when `MENTISDB_DEDUP_THRESHOLD` is set. Raise on chatty chains (e.g. `128`).

#### Invalidation and “current” memory

MentisDB never deletes corrected or superseded thoughts. Instead it maintains an
in-memory `invalidated_thought_ids` set for any thought that is the **target** of a
later `Supersedes`, `Corrects`, or `Invalidates` relation.

**Default retrieval** (`query`, ranked search, context bundles, recent context, memory
markdown export, REST/MCP search) **excludes** those IDs so agents see current memory.
Pass `include_invalidated=true` (crate: `ThoughtQuery::with_include_invalidated(true)` /
`RankedSearchQuery::with_include_invalidated(true)`) for audit archaeology.

Point-in-time `as_of` still returns thoughts that were valid at that timestamp, even
if they were superseded later.

How the set gets filled:

1. **Agents** write typed edges (`Supersedes` / `Corrects` / `Invalidates`) — the
   MentisDB skill’s search-before-write habit.
2. **Auto-dedup** when `MENTISDB_DEDUP_THRESHOLD` is set (see above).

Search filtering alone does not invent edges, and measured chains show agents rarely
type them (on one real installation 0 of 14 `Correction`/`AssumptionInvalidated`
thoughts and 0 of about 90 `Decision` thoughts carried one). So retrieval also reasons
about **lineage** (`mentisdb::lineage`):

- A superseded thought that would have ranked is **replaced by its live successor**
  (hit field `successor_of`), so hiding the old version never leaves the agent with
  nothing. Disable with `RankedSearchQuery::with_resolve_successors(false)`.
- An untyped link (`refs` / `References`) from a `Correction`, an
  `AssumptionInvalidated` or a new `Decision` over an older decision-like thought, or
  any `Contradicts`, does **not** hide the target (a reference is often background).
  The target is reported `version_status: "contested"` and the contesting thought is
  promoted above it.
- Every thought JSON carries `version_status`, `successors` and `current_version`
  when it is not plainly current, including `include_invalidated=true` results.
- Appending a replacement without a typed relation returns `warnings` naming the
  candidate `target_id`s; add `{"kind":"supersedes","target_id":"..."}`.
- Standing context substitutes a superseded constraint or decision with its successor,
  and the MEMORY.md export drops superseded thoughts.
- **Who may replace whose memory.** On an open chain any writer may replace any thought
  (corrections often come from another agent), so redirection is unchanged, but nothing is
  hidden about it: every successor note carries the replacement's `agent_id`, `trust`
  (`verified`, `unsigned` or `unverified`) and `cross_agent`, a hit that replaced another
  agent's thought sets `cross_agent: true`, and a standing entry shows `[REPLACES #n by
  agent: replaced by another agent, check it]`. On a governed chain (signing policy) a
  strong link replaces only when its writer is the same agent as the target or holds a key
  authorized on the chain; any other link is shown as `contested` (`authorized: false`) and
  replaces and promotes nothing. A chain of more than 64 versions of one thought
  (`MAX_LINEAGE_DEPTH`) is refused at write time.

Lineage is derived from the stored chain when it is opened, so existing chains benefit
with no migration. A `Supersedes`, `Corrects` or `Invalidates` relation that carries a
`chain_key` applies wherever one read sees both chains: branch search (a branch plus its
ancestors) and federated search replace the superseded hit with the live successor on the
other chain (`successor_of`, `successor_of_chain`), or annotate it `superseded` with
`current_version.chain_key` under `include_invalidated`. Only edges the caller's audience
may see count, so a public reader is never redirected to a private successor. A chain read
on its own is unchanged, and untyped links never apply across chains.

MentisDB loads environment variables at startup from a `.env` file in the current working
directory, then from `<MENTISDB_DIR>/.env` (where the dashboard Settings tab saves its
changes). Precedence is shell environment > `./.env` > `<MENTISDB_DIR>/.env`; a file never
overrides a variable that is already set. Missing files are silently ignored, so it is safe to commit a template `.env.example`
while keeping your actual `.env` in `.gitignore`.

Example — full durability (crash-safe default plus per-commit fsync):

```bash
MENTISDB_DIR=/tmp/mentisdb \
MENTISDB_DEFAULT_CHAIN_KEY=borganism-brain \
MENTISDB_STORAGE_ADAPTER=binary \
MENTISDB_VERBOSE=true \
MENTISDB_LOG_FILE=/tmp/mentisdb/mentisdb.log \
MENTISDB_BIND_HOST=127.0.0.1 \
MENTISDB_MCP_PORT=9471 \
MENTISDB_REST_PORT=9472 \
MENTISDB_DASHBOARD_PIN=change-me \
MENTISDB_AUTO_FLUSH=true \
MENTISDB_FSYNC=1 \
cargo run --bin mentisdb
```

#### What each durability setting really guarantees

| Setting | Survives process crash (kill -9) | Survives power loss / OS crash |
|---|---|---|
| `MENTISDB_AUTO_FLUSH=true` (default), `MENTISDB_FSYNC` unset | Yes: the append returns after the write reaches the OS | No: bytes may sit in the OS cache; a torn tail is truncated on open, but acknowledged records after the last device sync can be lost |
| `MENTISDB_AUTO_FLUSH=true`, `MENTISDB_FSYNC=1` | Yes | Yes (group commit is fsynced; roughly 4x append latency) |
| `MENTISDB_AUTO_FLUSH=false` | No: up to 128 queued records are lost | No |

`POST /v1/admin/flush`, clean shutdown and dropping a chain handle always fsync. Chain migrations
always fsync their journal, staged file and directory renames, regardless of these settings. The
default favours latency over power-loss durability; set `MENTISDB_FSYNC=1` on machines that can
lose power or on shared hosts where the memory is the system of record.

#### Durability and crash recovery (0.10.9)

- **Canonical record first.** An append returns `Ok` as soon as the hash-chained record is
  durable in the chain file. Derived state (lexical/vector sidecars, implicit-edge overlay,
  registries) is updated afterwards; if that fails it is logged and retried or rebuilt on
  the next append or open, instead of failing an append that already committed.
- **Torn-tail recovery.** If the daemon or machine died mid-write, opening a binary chain
  truncates a partial final record back to the last complete one and saves the dropped
  bytes beside the chain file as `<chain file>.torn-<unix-millis>` (mode `0600`) for
  inspection. Only a genuine partial record is truncated: if the bytes after a bad length
  prefix still decode as a complete record, the corruption is mid-file, so opening fails
  with an `InvalidData` error and the chain file is left untouched.
- **Single writer.** MentisDB assumes one writer process per chain directory; torn-tail
  repair takes no cross-process lock. Do not point two daemons (or a daemon and an embedded
  `MentisDb` writer) at the same `MENTISDB_DIR`.
- **Implicit-edge overlay catch-up.** The overlay records how many thoughts it covers and
  the chain head it was built against; after a crash it replays the missing tail on open
  (or rebuilds if the head does not match), so no implicit edges are lost.
- **Atomic registry writes.** The chain registry, agent registry, webhook list and other
  JSON registries are written to a temporary file and renamed into place, so a crash never
  leaves a half-written registry.

Example — multi-agent / long-lived chain (recommended: enable near-duplicate superseding):

```bash
MENTISDB_DIR=/var/lib/mentisdb \
MENTISDB_AUTO_FLUSH=true \
MENTISDB_DEDUP_THRESHOLD=0.85 \
MENTISDB_DEDUP_SCAN_WINDOW=64 \
MENTISDB_BIND_HOST=0.0.0.0 \
mentisdb
```

Example — high-throughput write mode (multi-agent hub):

```bash
MENTISDB_DIR=/var/lib/mentisdb \
MENTISDB_AUTO_FLUSH=false \
MENTISDB_BIND_HOST=0.0.0.0 \
mentisdb
```

### Upgrading and chain migrations

A release may need to rewrite chain files (a newer thought layout, a better hash algorithm,
JSONL to binary). `mentisdb` does that in the background, never blocks startup on it, tells you
what it is doing, and can always go back.

**What you will see**

- The daemon starts and serves immediately. Chains that need work are queued and migrated by a
  small worker pool (`MENTISDB_MIGRATION_CONCURRENCY`, default 2).
- A request for a chain that is still migrating gets **HTTP 503** with a `Retry-After` header and
  `{"retry_after_secs": 5, "migration": {"state": "migrating", "percent": 42, ...}}`; MCP clients get
  the same text as a tool error. Every other chain is served normally. A chain that is not
  migrating is never delayed by one that is.
- Progress is logged (`[migration] chain 'x': migrating ...`), shown in the TUI, and listed by
  `GET /v1/migrations`, the `mentisdb_migration_status` MCP tool, `mentisdb migrate status` and a
  banner on the dashboard.

**Why it is safe**

- *Backup first.* Before anything is replaced the original chain file is hard-linked (or copied)
  to `<MENTISDB_DIR>/migrations/backup/<chain>/`. It is kept `MENTISDB_MIGRATION_BACKUP_RETENTION_DAYS`
  days (default 14, `0` keeps it forever).
- *Journaled and resumable.* Each chain has a journal in `migrations/journal/`
  (planned, backed up, staged, committed, finalized). The upgraded chain is streamed into
  `migrations/staging/`, re-read and verified end to end, then swapped in with one atomic rename.
  Kill the daemon at any instant (the test suite does, at every step) and the next start resumes
  or discards the work. A chain interrupted three times is quarantined instead of crash-looping.
- *Never launders corruption.* Records from schemas that stored trustworthy hashes must verify;
  a chain whose stored hash is wrong (corruption or tampering), or whose migration would
  invalidate a v2 signature, is **refused and left byte-for-byte untouched**.
- *Failures are quarantined.* A failing chain is reported (state `failed`, with the error) and
  answers requests with a 503 naming the fix. The other chains and the daemon are unaffected.
- *Downgrades are refused.* A chain, or a data directory, written by a newer release is never
  opened by an older one that has this check; it says so and exits.

**Operator commands**

```bash
mentisdb migrate status                 # what needs, is in, or finished a migration
mentisdb migrate run --dry-run          # rehearse: check hashes and signatures, write nothing
mentisdb migrate run [--chain KEY]      # migrate now (resumes interrupted runs)
mentisdb migrate verify                 # re-check every hash link of the live chains
mentisdb migrate retry --chain KEY      # clear a quarantine; it is migrated on the next run
mentisdb migrate skip --chain KEY       # leave a chain alone and unavailable until retried
mentisdb migrate rollback --chain KEY   # restore the backup (stop the daemon first)
mentisdb migrate purge-backups          # delete preserved originals of finished migrations
```

`status --url http://127.0.0.1:9472` asks a running daemon. `rollback` refuses once new thoughts
were appended to the migrated chain unless you pass `--force`, which discards them; run it with the
daemon stopped, because a running daemon holds the chain in memory. Everything under
`migrations/` is plain files you can inspect.

**Derived data** (vector sidecars, HNSW graphs, the implicit-edge overlay, lexical indexes) is
never part of a migration's critical path: when a chain's hashes change they are deleted and
rebuilt lazily in the background; otherwise they are kept.

**Upgrade note (0.11).** Chains in the current layout with current hashes are not touched.
HNSW graph files gain a header (a magic and a SHA-256 digest of the embedding space and its
documents); existing graphs are rebuilt once in the background. Chains written by builds from
March and April 2026, which stamp `schema_version = 4` on schema-3 records, open again (0.11
accepts 4 as a historical alias and verifies those records under the rule that wrote them);
chains from schemas 0 to 2 are verified link by link before their hashes are rebuilt. Nothing else changes on
disk, so a chain that needed no migration is still readable by the previous release, except a
chain that holds an `AccessPolicy` record, which releases before the type cannot read.

### Automatic Update Check

`mentisdb` checks GitHub releases in the background after startup and can offer
to update itself with `cargo install`.

- checks are enabled by default
- version comparison uses only the first three numeric components, so a tag like
  `0.6.1.14` is treated as core version `0.6.1`
- interactive terminals get an ASCII prompt window with `Y` / `N`
- non-interactive terminals never block; they print the exact manual `cargo install` command instead

Disable the automatic check:

```bash
MENTISDB_UPDATE_CHECK=0 \
mentisdb
```

---

## Server Surfaces

MCP endpoints:

- `GET /health`
- `POST /`
- `GET /` (event stream; same `Host`, bearer and `Origin` checks as `POST /`)
- `POST /tools/list`
- `POST /tools/execute`

REST endpoints:

- `GET /health`
- `GET /mentisdb_skill_md`
- `GET /v1/skills`
- `GET /v1/skills/manifest`
- `GET /v1/chains`
- `POST /v1/chains/merge`
- `POST /v1/chains/branch`
- `POST /v1/vectors/rebuild`
- `POST /v1/bootstrap`
- `POST /v1/agents`
- `POST /v1/agent`
- `POST /v1/agent-registry`
- `POST /v1/agents/upsert`
- `POST /v1/agents/description`
- `POST /v1/agents/aliases`
- `POST /v1/agents/keys` (403: operator-only)
- `POST /v1/agents/keys/revoke` (403: operator-only)
- `POST /v1/agents/disable` (403: operator-only)
- `POST /v1/access/policy`
- `POST /v1/access/policy/set` (403: operator-only)
- `POST /v1/access/verify`
- `POST /v1/thought`
- `POST /v1/thoughts`
- `POST /v1/thoughts/genesis`
- `POST /v1/thoughts/traverse`
- `POST /v1/retrospectives`
- `POST /v1/search`
- `POST /v1/lexical-search`
- `POST /v1/ranked-search`
- `POST /v1/context-bundles`
- `POST /v1/recent-context`
- `POST /v1/standing-context`
- `POST /v1/memory-markdown`
- `POST /v1/import-markdown`
- `POST /v1/skills/upload`
- `POST /v1/skills/search`
- `POST /v1/skills/read`
- `POST /v1/skills/versions`
- `POST /v1/skills/deprecate`
- `POST /v1/skills/revoke`
- `POST /v1/skills/delete`
- `POST /v1/webhooks`
- `GET /v1/webhooks`
- `DELETE /v1/webhooks/{id}`
- `POST /v1/head`
- `POST /v1/federated-search`
- `POST /v1/summary-candidates`
- `POST /v1/entity-types`
- `POST /v1/entity-types/upsert`
- `POST /v1/extract-memories`
- `POST /v1/admin/flush`
- `GET /v1/migrations`
- `POST /v1/migrations/retry` (global token)
- `POST /v1/migrations/skip` (global token)

#### Chain listing and derived-state backlog

`GET /v1/chains` (global token; MCP `mentisdb_list_chains`) lists every chain with
`derived_backlog`, the work still pending on its derived state (0.12):

```json
{
  "chain_key": "project", "version": 3, "storage_adapter": "binary",
  "thought_count": 100000, "agent_count": 4, "storage_location": "...",
  "derived_backlog": {
    "embeddings_in_flight": 0, "embeddings_parked": 0,
    "embeddings_missing": 0, "implicit_edges": 312
  }
}
```

- `embeddings_in_flight`: thoughts whose embedding has been requested but not committed.
- `embeddings_parked`: vectors that are ready but wait for an earlier thought's vector, so
  they are applied in chain order.
- `embeddings_missing`: thoughts waiting to be embedded again after a failure.
- `implicit_edges`: applied vectors whose implicit `RelatedTo` edges have not reached the
  overlay yet.

All four are zero on a healthy, idle chain. A steadily growing `embeddings_missing` or
`embeddings_in_flight` points at a stalling embedding provider. A growing `implicit_edges`
means appends are outrunning the background edge scan: about 155 appends per second at
100,000 thoughts and 720 at 20,000 (4 threads, 384 dimensions). The backlog never blocks an
append or drops an edge. It only delays edges for recent thoughts, and it drains when
appends slow down. A chain that is not open, or whose private segments are hidden from the
caller, reports zeros. Library: `MentisDb::derived_backlog`.

#### Chain resolution and error statuses

Only operations that write a chain create it when its `chain_key` does not exist yet:
`POST /v1/bootstrap`, `POST /v1/thoughts`, `POST /v1/retrospectives`,
`POST /v1/import-markdown`, `POST /v1/agents/upsert`, `POST /v1/entity-types/upsert`,
and the target of `POST /v1/chains/merge`. Every other route
(search, head, agents, thought lookup, metadata updates, ...) returns **404** for an
unknown `chain_key` and persists nothing. The configured default chain
(`MENTISDB_DEFAULT_CHAIN_KEY`) is the one exception: it is created on demand so a fresh
daemon answers reads. Call `POST /v1/bootstrap` (or `mentisdb_bootstrap` over MCP)
before reading a new chain.

A `chain_key` must be non-empty, at most 256 bytes, and free of control characters;
anything else is rejected with **400**. The source, target and branch keys of
`POST /v1/chains/merge` and `POST /v1/chains/branch` (and the matching MCP tools) are
trimmed of surrounding whitespace and then validated by the same rule.

REST and MCP errors map to HTTP statuses as follows:

| Status | Meaning |
|---|---|
| `400` | Invalid input: malformed JSON, bad UUID, unknown thought type/role, invalid `chain_key`, a result window (`offset + limit`) above 10,000 or a standing-context `per_type_limit` above 100 |
| `401` | Missing/invalid bearer token, or a token whose scope does not cover the operation |
| `403` | Permission denied: missing or invalid signature on a signed skill upload, inactive agent, a write the chain's access policy refused, a `Host` outside the allowlist, or an operator-only route (`/v1/agents/keys`, `/v1/agents/keys/revoke`, `/v1/agents/disable`, `/v1/access/policy/set`) |
| `404` | Unknown chain (see above) or another missing resource |
| `408` | A request body stopped arriving for `MENTISDB_BODY_IDLE_TIMEOUT_SECS`, a small or anonymous body missed its total deadline (twice that), or any body fell below `MENTISDB_MIN_BODY_BYTES_PER_SEC` (64 KiB/s by default) in a window after its grace period (twice the idle timeout); on every route |
| `409` | Conflict, e.g. `POST /v1/chains/branch` into a chain key that already exists |
| `413` | Request body over the route's limit: 2 MiB, or `MENTISDB_MAX_BODY_BYTES` (default 64 MiB) on the import routes for an authenticated caller; over 1 MiB for a read proof (`X-Mentis-Auth`) that does not also send `X-Mentis-Content-Sha256` (see [Large request bodies](#large-request-bodies)). The `mentisdb` CLI and `pymentisdb` send it, so a large `memory import` works |
| `500` | Server fault; the body says only `"internal server error"` and details go to the daemon log |
| `501` | `POST /v1/extract-memories` on a build without the `llm-extraction` feature |
| `503` | The chain is being migrated or is quarantined; the body names the state, and a migrating chain adds `Retry-After` and `retry_after_secs` (see [Upgrading and chain migrations](#upgrading-and-chain-migrations)). Also, with `Retry-After`, when the in-flight body budget is exhausted (see [Large request bodies](#large-request-bodies)) |

### Large request bodies

Request bodies are limited per route. Ordinary routes take at most **2 MiB**. The import family
(`/v1/import-markdown`, `/v1/skills/upload`, `/v1/extract-memories`) takes up to
`MENTISDB_MAX_BODY_BYTES` (default 64 MiB), and with bearer-token access on only from a caller whose token
is valid: the token is checked from the headers before any of the body is read, so a request without one is
refused (`401`, or `413` for a declared length over 2 MiB) without the daemon pulling its body. Large
imports draw on their own budget (`MENTISDB_MAX_INFLIGHT_BODY_BYTES`, reserved from the declared length; beyond it
`503` with `Retry-After`); every other request is charged only for the bytes that actually arrive, from a separate
pool (64 MiB, at most 32 MiB per peer), so imports never starve appends and searches. A body that
stops arriving fails with `408` after `MENTISDB_BODY_IDLE_TIMEOUT_SECS`, small or anonymous bodies also get a
total deadline of twice that, and every body must sustain `MENTISDB_MIN_BODY_BYTES_PER_SEC` (64 KiB/s by default) in each window of one idle
timeout once its grace period (twice the idle timeout) is over. Anonymous bodies have a 16 MiB pool of their own (8 MiB per peer). MCP request bodies (including the `mentisdb_import_memory_markdown` tool) are always
limited to 2 MiB: send a large import to the REST route, or use the CLI. Two paths decide who is asking, and
they treat a large body differently:

- **Bearer token.** The daemon reads the body (up to the route's limit) to find the `chain_key` the token
  must cover, then hands it to the handler.
- **Read proof (`X-Mentis-Auth`).** The signature covers `SHA-256(body)`, so by itself the daemon must
  read the whole body to check it, which it only does up to **1 MiB**. A client that also sends
  `X-Mentis-Content-Sha256: <64 lowercase hex>` (the same digest the proof signed) lets the daemon verify
  the proof **before** reading the body and then hash the body as it streams. The signed body goes through;
  any other body fails at its end with `400` and no handler has run, so nothing is imported or changed. The
  proof format is unchanged: older clients (and a daemon that predates the header) work as before.

`mentisdb` (CLI) and `pymentisdb` send the digest header with every proof. If you sign requests yourself, add
the header and keep the body bytes you hash identical to the ones you send. Code on the daemon side that
streams a body must not act on it before the end: the digest is only confirmed there.

### Append Thought — `POST /v1/thoughts`

```json
{
  "chain_key":      "my-chain",
  "agent_id":       "my-agent",
  "agent_name":     "My Agent",
  "thought_type":   "LessonLearned",
  "role":           "Execution",
  "content":        "...",
  "scope":          "session",
  "tags":           ["tag1"],
  "concepts":       ["concept1"],
  "entity_type":    "incident",
  "source_episode": "triage-2026-04-17",
  "importance":     0.9,
  "confidence":     0.8,
  "refs":           [14, 22],
  "relations": [
    { "kind": "CausedBy",      "target_id": "<uuid>" },
    { "kind": "ContinuesFrom", "target_id": "<uuid>", "chain_key": "other-chain" },
    { "kind": "Supersedes",    "target_id": "<uuid>", "valid_at": "2025-01-01T00:00:00Z", "invalid_at": "2025-12-31T23:59:59Z" }
  ]
}
```

`chain_key`, `role`, `scope`, `tags`, `concepts`, `entity_type`, `source_episode`, `importance`, `confidence`, `refs`, and `relations` are optional.  
`relations[].kind` accepts: `References`, `Summarizes`, `Corrects`, `Invalidates`, `CausedBy`, `Supports`, `Contradicts`, `DerivedFrom`, `ContinuesFrom`, `BranchesFrom`, `RelatedTo`, `Supersedes`.  
`relations[].chain_key` is optional — omit for intra-chain edges, set for cross-chain references.  
`relations[].valid_at` and `relations[].invalid_at` are optional RFC 3339 timestamps that define when a relation edge is temporally valid, enabling point-in-time queries with `as_of`.  
`entity_type` is an optional per-chain ontology label (e.g. `"incident"`, `"customer"`, `"deploy"`) used by the dashboard explorer and by ranked-search filtering.  
`source_episode` is an optional free-form provenance string (e.g. a conversation id or batch name) that groups thoughts by the episode they were derived from; it is also filterable in ranked search.

---

## Search Semantics

MentisDB keeps its baseline thought search surface **filter-first and append-order**. Ranked, graph-aware, and vector retrieval are additive surfaces layered on top of that stable baseline.

**Ranked search now automatically expands queries** using the built-in static thesaurus (~900 headwords + 300+ irregular verb lemmas) for better recall on vocabulary mismatch and verb-form variation. No client changes or extra parameters are required — the expansion is applied transparently to every text-bearing ranked query (REST, MCP, dashboard, and CLI).

Today, the main search APIs are:

- `MentisDb::query(&ThoughtQuery)`
- `POST /v1/search`
- `mentisdb_search`

Current behavior:

- indexed filters narrow the candidate set for `thought_type`, `role`, `agent_id`, tags, and concepts
- `text` is a case-insensitive substring match over:
  - thought `content`
  - `agent_id`
  - tags
  - concepts
  - agent-registry display name, aliases, owner, and description
- results are returned in **append order**
- `limit` keeps the **newest matching tail** after filtering rather than applying a ranking score

That means plain `ThoughtQuery` / `/v1/search` behavior is deterministic and explainable, but that baseline path is **not** BM25, hybrid, or vector retrieval. Additive ranked and graph-aware retrieval now exist on separate crate, REST, and MCP surfaces.

Examples:

```rust,no_run
use mentisdb::{MentisDb, ThoughtQuery, ThoughtType};
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let chain = MentisDb::open(&PathBuf::from("/tmp/tc_query"), "agent1", "Agent", None, None)?;

let lexical = ThoughtQuery::new()
    .with_types(vec![ThoughtType::Decision])
    .with_tags_any(["search"])
    .with_text("latency");

let results = chain.query(&lexical);
# let _ = results;
# Ok(())
# }
```

```json
{
  "chain_key": "mentisdb",
  "thought_types": ["Decision"],
  "tags_any": ["search"],
  "text": "latency",
  "limit": 20
}
```

Design note:

- treat this lexical/filter-first behavior as the baseline
- keep ranked, vector, and hybrid retrieval as additive, explicitly documented surfaces on top of that baseline
- do not silently change the semantics of `ThoughtQuery` or `/v1/search` from append-order filtering to score-ranked retrieval

The dedicated benchmark `benches/search_baseline.rs` and evaluation tests in `tests/search_eval_tests.rs` are intended to preserve that baseline while world-class search evolves.

### Ranked Search

MentisDB now also exposes an additive ranked-search surface for direct crate use:

- `RankedSearchQuery`
- `RankedSearchGraph`
- `MentisDb::query_context_bundles(&RankedSearchQuery)`
- `MentisDb::query_ranked(&RankedSearchQuery)`
- `RankedSearchBackend::{Lexical, Hybrid, LexicalGraph, HybridGraph, Heuristic}`

This surface is intentionally separate from `ThoughtQuery`.

`ThoughtQuery` still decides **which** thoughts are eligible. Ranked search then decides **how those eligible thoughts are ordered**.

Current ranked-search behavior:

- `RankedSearchQuery.filter` uses the same deterministic semantics as `MentisDb::query`
- when `text` normalizes to a non-empty query, the backend is `lexical` or `hybrid` depending on whether a managed vector sidecar is active for the current handle
- lexical ranking scores indexed thought text plus agent metadata from the filtered candidate set
- when a managed vector sidecar is active for the current handle, ranked search blends lexical scoring with vector similarity and the backend becomes `hybrid`
- when `graph` is enabled alongside non-empty `text`, the backend becomes `lexical_graph` or `hybrid_graph` depending on whether vector scoring is available
- graph expansion starts from lexical seed hits, walks `refs` and typed `relations`, and can surface supporting context that did not lexically match
- `as_of` (RFC 3339 timestamp) filters to only relation edges that were valid at the given point in time, using each edge's `valid_at`/`invalid_at` temporal window — edges without temporal bounds are always included
- `scope` narrows results to thoughts tagged with a matching memory scope (`user`, `session`, or `agent`); omitted scope returns all
- when `text` is absent or blank, the backend falls back to `heuristic`
- heuristic ordering uses lightweight importance, confidence, and recency signals
- `total_candidates` counts the hits after filter application and ranked-signal gating, before final `limit` truncation
- each ranked hit includes `matched_terms` plus `match_sources` such as `content`, `tags`, `concepts`, `agent_id`, and `agent_registry`
- each ranked hit also includes a `vector` score component when semantic sidecars contribute to the ranking
- graph-expanded hits also expose `graph_distance`, `graph_seed_paths`, `graph_relation_kinds`, and `graph_path` provenance so callers can explain why a supporting thought surfaced
- grouped context delivery is available through `query_context_bundles`, which anchors supporting graph hits beneath lexical seeds in deterministic order
- `compact: true` (MCP `mentisdb_ranked_search` and `mentisdb_federated_search`, REST `/v1/ranked-search` and `/v1/federated-search`, CLI `mentisdb search --compact` and `mentisdb search federated --compact`) returns smaller hits for routine recall; see [Compact search results](#compact-search-results)

Lexical ranked example:

```rust,no_run
use mentisdb::{MentisDb, RankedSearchQuery, ThoughtQuery, ThoughtType};
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let chain = MentisDb::open(&PathBuf::from("/tmp/tc_ranked"), "agent1", "Agent", None, None)?;

let ranked = RankedSearchQuery::new()
    .with_filter(
        ThoughtQuery::new()
            .with_types(vec![ThoughtType::Decision])
            .with_tags_any(["search"]),
    )
    .with_text("latency ranking")
    .with_limit(10);

let results = chain.query_ranked(&ranked);
assert!(matches!(
    results.backend,
    mentisdb::RankedSearchBackend::Lexical | mentisdb::RankedSearchBackend::Hybrid
));
# let _ = results;
# Ok(())
# }
```

Lexical + graph ranked example:

```rust,no_run
use mentisdb::{MentisDb, RankedSearchGraph, RankedSearchQuery, ThoughtQuery, ThoughtType};
use mentisdb::search::GraphExpansionMode;
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let chain = MentisDb::open(&PathBuf::from("/tmp/tc_ranked"), "agent1", "Agent", None, None)?;

let ranked = RankedSearchQuery::new()
    .with_filter(
        ThoughtQuery::new()
            .with_types(vec![ThoughtType::Decision])
            .with_tags_any(["search"]),
    )
    .with_text("latency ranking")
    .with_graph(
        RankedSearchGraph::new()
            .with_max_depth(1)
            .with_mode(GraphExpansionMode::Bidirectional),
    )
    .with_limit(10);

let results = chain.query_ranked(&ranked);
# let _ = results;
# Ok(())
# }
```

Temporal and scoped ranked example:

```rust,no_run
use mentisdb::{MentisDb, MemoryScope, RankedSearchQuery, ThoughtQuery};
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let chain = MentisDb::open(&PathBuf::from("/tmp/tc_ranked"), "agent1", "Agent", None, None)?;

let ranked = RankedSearchQuery::new()
    .with_filter(ThoughtQuery::new())
    .with_text("cache invalidation")
    .with_as_of("2025-06-01T00:00:00Z")
    .with_scope(MemoryScope::Session)
    .with_limit(10);

let results = chain.query_ranked(&ranked);
# let _ = results;
# Ok(())
# }
```

Vector-backed ranked example:

```rust,no_run
use mentisdb::{MentisDb, RankedSearchBackend, RankedSearchQuery};
use mentisdb::search::LocalTextEmbeddingProvider;
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let mut chain = MentisDb::open_with_key(&PathBuf::from("/tmp/tc_ranked_vectors"), "semantic-ranked")?;
chain.append("planner", mentisdb::ThoughtType::Decision, "Tail latency ceiling for the Europe rollout.")?;

// Register the built-in local-text-v1 embedding sidecar so ranked search can
// blend lexical and semantic signals for the current chain handle.
chain.manage_vector_sidecar(LocalTextEmbeddingProvider::new())?;

let ranked = chain.query_ranked(&RankedSearchQuery::new().with_text("performance budget"));

assert_eq!(ranked.backend, RankedSearchBackend::Hybrid);
assert!(ranked.hits.iter().any(|hit| hit.score.vector > 0.0));
# Ok(())
# }
```

Grouped context example:

```rust,no_run
use mentisdb::{MentisDb, RankedSearchGraph, RankedSearchQuery, ThoughtQuery};
use mentisdb::search::GraphExpansionMode;
use std::path::PathBuf;

# fn main() -> std::io::Result<()> {
let chain = MentisDb::open(&PathBuf::from("/tmp/tc_ranked"), "agent1", "Agent", None, None)?;

let bundles = chain.query_context_bundles(
    &RankedSearchQuery::new()
        .with_filter(ThoughtQuery::new().with_tags_any(["search"]))
        .with_text("latency ranking")
        .with_graph(
            RankedSearchGraph::new()
                .with_mode(GraphExpansionMode::Bidirectional)
                .with_max_depth(2),
        )
        .with_limit(5),
);
# let _ = bundles;
# Ok(())
# }
```

Product rule:

- keep `ThoughtQuery` stable and explainable for append-order filtering
- evolve ranked search as a separate surface with its own benchmarks, tests, and transport layers
- treat registry-aware filtering and future transport exposure as additive work on top of the current crate API
- use `query_ranked` for flat ranked retrieval and `query_context_bundles` when the caller wants seed-anchored support context instead of one mixed list

The ranked-search benchmark `benches/search_ranked.rs` and evaluation tests in `tests/search_ranked_eval_tests.rs` are the guardrails for that additive surface.

### Compact search results

Ranked and federated search accept an opt-in `compact: true`. It cuts the tokens an agent spends reading results without removing any field the agent reasons with. The default response is unchanged. It is available on MCP (`mentisdb_ranked_search`, `mentisdb_federated_search`), REST (`POST /v1/ranked-search`, `POST /v1/federated-search`) and the CLI (`mentisdb search --compact`, `mentisdb search federated --compact`). It has no effect on `mentisdb_context_bundles` and `POST /v1/context-bundles`, which still return full thoughts.

A compact hit is `chain_key`, the total `score` as a plain number, and the thought, in the same order as the full form. Graph-expanded hits also keep `graph_distance`, `graph_seed_paths`, `graph_relation_kinds` and `graph_path`.

| | Full hit | Compact hit |
|---|---|---|
| `score` | object with `lexical`, `vector`, `graph`, `importance`, ... and `total` | the `total` number |
| `matched_terms`, `match_sources` | present | left out |
| thought `hash`, `prev_hash` | present | left out (chain integrity) |
| thought `thought_signature`, `signing_key_id` | present | left out (signing; `provenance` still carries the server's verdict) |
| thought `schema_version` | present | left out |
| thought `agent_name`, `agent_owner` | present | left out (they repeat the agent registry entry for `agent_id`; `mentisdb_get_agent` resolves it) |
| top-level thought fields that are `null`, `""`, `[]` or `{}` | present | left out |
| thought `provenance` (`segment`, `signed`, `signature`, `signature_version`, `verified_agent`, `trust`) | present | **always kept, whole** |
| `version_status`, `successors`, `current_version`, `successor_of`, `cross_agent`, `collapsed_duplicates` | present when set | **always kept** |
| `relations`, `concepts`, `refs`, `content`, `tags`, ids, importance, confidence, timestamps | present | kept (zero and `false` are values, not empty) |

Fields are dropped by name from a fixed list, so a field added to the thought later appears in compact hits by default. Visibility is decided before compaction: a public reader still gets only the public segment, and a reader with a valid `X-Mentis-Auth` proof still gets the private one, each hit with its `provenance`.

Full hit (`POST /v1/ranked-search`):

```json
{
  "backend": "hybrid",
  "total": 1,
  "results": [
    {
      "chain_key": "project",
      "score": {
        "confidence": 0.0, "graph": 0.0, "importance": 0.17541419, "lexical": 1.9490464,
        "recency": 0.05, "relation": 0.0, "rrf": 0.0, "seed_support": 0.0,
        "session_cohesion": 0.0, "total": 5.932654, "vector": 0.34079674
      },
      "matched_terms": ["job", "queue", "storag"],
      "match_sources": ["content", "tags", "concepts"],
      "graph_distance": null, "graph_path": null, "graph_relation_kinds": [], "graph_seed_paths": 0,
      "thought": {
        "agent_id": "builder", "agent_name": "Builder", "agent_owner": "platform",
        "concepts": ["job queue"], "confidence": null,
        "content": "Use Postgres for the job queue; revisit if throughput exceeds 5k jobs per second.",
        "entity_type": null,
        "hash": "31de8f264b1588a29be30a278a24e8623cf51b8f3ce8483a7e52f69ce80e21e1",
        "id": "1182d44f-3834-4ff0-9121-eab986b1a4f5", "importance": 0.800000011920929, "index": 0,
        "prev_hash": "",
        "provenance": {
          "segment": "public", "signature": "unsigned", "signature_version": null,
          "signed": false, "trust": "untrusted_data", "verified_agent": null
        },
        "refs": [], "relations": [], "role": "Memory", "schema_version": 3, "session_id": null,
        "signing_key_id": null, "source_episode": null, "tags": ["storage"],
        "thought_signature": null, "thought_type": "Decision",
        "timestamp": "2026-11-01T23:03:19.669167Z"
      }
    }
  ]
}
```

The same request with `"compact": true`:

```json
{
  "backend": "hybrid",
  "total": 1,
  "results": [
    {
      "chain_key": "project",
      "score": 5.932654,
      "thought": {
        "agent_id": "builder",
        "concepts": ["job queue"],
        "content": "Use Postgres for the job queue; revisit if throughput exceeds 5k jobs per second.",
        "id": "1182d44f-3834-4ff0-9121-eab986b1a4f5", "importance": 0.800000011920929, "index": 0,
        "provenance": {
          "segment": "public", "signature": "unsigned", "signature_version": null,
          "signed": false, "trust": "untrusted_data", "verified_agent": null
        },
        "role": "Memory", "tags": ["storage"], "thought_type": "Decision",
        "timestamp": "2026-11-01T23:03:19.669167Z"
      }
    }
  ]
}
```

When to use it: routine recall and scanning many hits, where the content, tags, relations, version status and provenance are what the agent reads. Leave it off when you need the hashes or signatures to verify a thought yourself, when you audit a provenance chain, or when you debug per-component scores or matched terms. `mentisdb_get_thought` (REST `POST /v1/thought`) returns the full record of any hit.

Measured on a copy of a working MentisDB with 11 chains (12 ranked, graph and federated searches, 10 hits each), responses were 23.7% smaller (353,071 B to 269,335 B); on a generated corpus of 66 queries they were 34.2% smaller. `cargo bench --bench search_compact` shows the same request time with and without `compact` (about 25% fewer bytes). Contributed by Austin Faulkner-Pearce.

### Lean MCP output

Agents read MCP tool results with their context window, so the streamable-HTTP MCP surface (JSON-RPC `tools/call`) is leaner than REST:

- Results are **minified JSON text**, with no indentation and no second `structuredContent` copy of the same object. (No tool declares an `outputSchema`, so clients read the text.) REST and `POST /tools/execute` still return the object.
- `mentisdb_ranked_search`, `mentisdb_federated_search`, `mentisdb_lexical_search` and `mentisdb_context_bundles` are **compact by default**; pass `"compact": false` for the full record. A lean thought leaves out what is default, so an absent field means its default: no `provenance` is a public, unsigned thought (a private segment, a signature or a `verified_agent` is always listed), no `role` is `Memory`, no `importance` is `0.5`, no `chain_key` is the chain you searched. Floats are rounded, timestamps keep full precision (so they round-trip through `as_of` and `since`), `successor_of` is an older version that matched the query and that the hit replaces, with a `superseded_versions` count that is a lower bound (not the whole lineage), and `version_status`, `successors` and `current_version` still say when a memory is contested or superseded.
- `mentisdb_standing_context` returns the rendered `prompt` once. Its `entries` array repeats the same memories, so it needs `include_entries: true`.

Measured with `cargo run --release --example token_diet` (a generated 3,500-thought chain with superseded lineages and weak-link corrections, 10 hits, characters of the text the model reads):

| Tool call | Before | After |
|---|---:|---:|
| `mentisdb_ranked_search` (default) | 23,657 | 5,948 |
| `mentisdb_ranked_search` `compact: true` | 12,699 | 5,948 |
| `mentisdb_ranked_search` `compact: false` | 23,657 | 16,696 |
| `mentisdb_lexical_search` | 18,743 | 6,341 |
| `mentisdb_federated_search` | 23,511 | 6,025 |
| `mentisdb_context_bundles` (5 bundles) | 9,993 | 3,562 |
| `mentisdb_standing_context` | 36,191 | 13,050 |
| `mentisdb_recent_context` (20 thoughts) | 6,936 | 6,931 |

The rules are in the `mentisdb::server_lean` rustdoc.

### Search Scoring (0.8.1)

Starting in 0.8.1, ranked search uses six key improvements:

- **Porter stemming** — the lexical tokenizer stems all tokens before indexing and querying so word variants share a common root (e.g. `prefers`/`preferred`/`preferences` → `prefer`).
- **Smooth exponential vector-lexical fusion** — replaces the 0.8.0 step-function boosts with a continuous decay curve: `vector × (1 + 35 × exp(-lexical / 3.0))`. Pure-semantic matches get ~36× amplification; by lexical=3.0 the boost has decayed to ~12×; at lexical=6.0 it's additive. This eliminates discontinuities between tiers. (Since the valid-version retrieval work the default is `MENTISDB_VECTOR_FUSION=relative`, which decays on the lexical score relative to the query's best so that long queries keep their vector signal; `absolute` restores this formula.)
- **Session cohesion scoring** — thoughts within ±8 positions of a high-scoring lexical seed (score ≥ 3.0) receive a proximity boost up to 0.8, decaying linearly with distance. This surfaces evidence turns adjacent to the matching turn but sharing no lexical terms.
- **BM25 document-frequency cutoff** — terms appearing in >30% of documents (corpus ≥ 20 docs) are skipped during scoring. This filters non-discriminative entity names without blanket stopword removal.
- **Importance-weighted scoring** — replaces flat multipliers with a differential boost proportional to lexical score: `lexical × (importance - 0.5) × 0.3`. User-originated thoughts (importance ≈ 0.8) outrank verbose assistant responses (importance ≈ 0.2) in close BM25 races.
- **Graph expansion limits and relation boosts** — `MAX_GRAPH_SEEDS=20` bounds BFS cost; `ContinuesFrom` boost raised to 0.30; graph proximity 1.0/depth.

These changes took LongMemEval R@5 from 57.2% to 67.6% and LoCoMo 2-persona R@10 from 55.8% to 88.7%.

### Search Scoring (0.8.2)

Starting in 0.8.2, ranked search adds temporal, scoped, and dedup-aware features:

- **Temporal `as_of` point-in-time filtering** — `RankedSearchQuery::with_as_of(rfc3339)` restricts graph expansion to only relation edges whose `valid_at`/`invalid_at` window covers the given timestamp. Edges without temporal bounds are always included. This enables queries like "what did the agent know at the start of the sprint?"
- **Memory scope filtering via `scope` tag** — thoughts carry a `scope` field (`user`, `session`, or `agent`) stored as `scope:<value>` tags. `RankedSearchQuery::with_scope(MemoryScope::Session)` narrows results to session-scoped memories only. Omitting scope returns thoughts from all scopes.
- **Auto-dedup with `Supersedes` relations** — when `MENTISDB_DEDUP_THRESHOLD` is set (recommended `0.85` for long-lived agent chains; **off** by default), appending a thought whose content is sufficiently similar (Jaccard ≥ threshold) to a recent thought automatically emits a `Supersedes` relation to that prior thought. The prior thought remains on disk for audit; its id enters the invalidation set for default search exclusion.
- **`invalidated_thought_ids` for O(1) superseded exclusion** — thoughts targeted by `Supersedes`, `Corrects`, or `Invalidates` are excluded from default `query`, ranked search, context bundles, recent context, and related retrieval. Pass `include_invalidated=true` (or `ThoughtQuery::with_include_invalidated(true)`) for audit. Point-in-time `as_of` still surfaces thoughts that were valid at that timestamp. The set only fills when those edges exist (agent-written and/or auto-dedup).

### Search Scoring (0.8.7)

Starting in 0.8.7, ranked search adds:

- **Entity type filtering** — thoughts can carry an optional `entity_type` label (e.g. "bug_report", "architecture_decision", "retrospective"). The `ThoughtQuery` accepts `entity_type` as a filter, and the dashboard exposes an entity_type text filter in the explorer. Entity types are auto-observed per chain and persisted in a `chain_key-entity-types.json` sidecar.

### Search Scoring (0.8.6)

Starting in 0.8.6, ranked search adds three features:

- **Irregular verb lemma expansion** — the query tokenizer maps irregular past-tense verbs to their base form (e.g. "went" → "go", "gave" → "give", "ran" → "run"). About 325 mappings onto 219 base forms. Indexed content is not modified — expansion is query-time only.
- **Reciprocal Rank Fusion (RRF)** — an opt-in reranking pass. When `enable_reranking=true` is set on a ranked search query, the engine produces separate lexical-only, vector-only, and graph-only rankings over the top `rerank_k` candidates (default 50), merges them via `1/(k + rank)` with `k=60`, and adds a scaled consensus bonus to the additive total. Use when lexical and vector signals disagree on top candidates. (Before 0.10.9 the RRF total replaced the additive total, which badly degraded results; see below.)
- **Per-field BM25 DF cutoffs** — `Bm25DfCutoffs` on `LexicalQuery` allows configuring separate document-frequency cutoff ratios per field (content, tags, concepts, agent_id, agent_registry). Terms whose global DF exceeds the cutoff for a given field are skipped for that field only. Default cutoffs match the original behavior (content=0.30, tags=0.30, concepts=0.30, agent_id=0.70, agent_registry=0.60).

### Search Scoring (after 0.9.9)

The post-0.9.9 ranked-search validation run used real embeddings plus automatic thesaurus expansion on the full LoCoMo-10P benchmark:

- **LoCoMo-10P overall R@10: 72.6%** (1436 / 1977 queries)
- **Single-hop R@10: 76.8%** (1193 / 1554 queries)
- **Multi-hop R@10: 57.4%** (243 / 423 queries)
- **Weak-vector smoke baseline: 44.9% R@10**, so the validated pipeline improved recall by 27.7 percentage points.
- **Evaluation throughput: 6 seconds for 1977 queries** (~317 queries/second).
- **Vector sidecar: `fastembed-all-minilm-l6-v2`**, about 28 MB with 5882 indexed thoughts.

The run applied the built-in thesaurus transparently on every `ranked_search` call and matches the whitepaper target of about 72% overall LoCoMo-10P R@10.

### Search Scoring (0.10.9)

- **RRF rerank fixed** — `enable_reranking=true` no longer replaces the additive score with the tiny raw RRF total (which collapsed rankings). RRF now adds a consensus bonus scaled by `RRF_SCORE_SCALE` (50): a rank-1 hit in all three lists is worth about +2.5, enough to break ties and reward agreement without overriding a clearly stronger lexical match. Only lists with a positive score for a candidate contribute.
- **Stemmed thesaurus keys** — synonyms now expand for inflected query terms (`debugging` expands like `debug`, `deploys` like `deploy`). Because stem keys make expansion fire more often, automatic synonyms are damped to weight 0.3 with at most 3 synonyms per term (the previous 0.7 / 5 displaced literal matches and cost about 2.4 points of LongMemEval R@5).
- **Federated search keyed by chain + id** — `POST /v1/federated-search` / `mentisdb_federated_search` fuse per-chain rankings with the same additive RRF bonus, keyed by `(chain_key, thought id)`, and deduplicate before paging, so `offset`/`limit` pages no longer repeat or drop results.
- **Faster ranked, lexical, vector and graph paths** — score-only top-k selection, dense lexical scans, cached vector norms and exact top-k, and a bounded graph-expansion arena. Filtered lexical and heuristic queries are roughly 10x faster in the criterion benches.
- **Filtered HNSW recall** — when filters are active, the HNSW backend switches to an exact scan over the filtered set or oversamples, so filtered vector searches no longer lose matches the approximate graph skipped.
- **Benchmarks (0.10.9.54 vs the 0.10.8 code line, `fastembed-minilm`)** — LoCoMo-10P default R@5/R@10 63.8/72.7% → 63.9/73.5%; LoCoMo rerank R@5/R@10 3.6/5.9% → 66.0/74.1%; LongMemEval default R@5/R@10/R@20 66.8/72.0/78.2% → 68.0/72.8/78.8%; LongMemEval rerank R@5 2.8% → 68.6%; query throughput about 206/159 → 384/385 queries/s (LoCoMo/LongMemEval).

### Search Scoring (0.11.0)

- **Valid-version retrieval** — a superseded hit is replaced by its live successor, a thought a newer correction or decision only references is shown as `contested` with the newer one ranked above it, and every hit carries `version_status`.
- **Relative vector fusion** (`MENTISDB_VECTOR_FUSION=relative`, decay 0.8) and **result-time duplicate collapse** (Jaccard 0.9).
- **Library and server share the defaults** — `RankedSearchQuery::new()` now applies relative fusion, duplicate collapse, successor redirection and thesaurus expansion at weight 0.3, like the daemon. Opt out per query (`with_vector_fusion(VectorFusion::Absolute)`, `with_collapse_duplicates(None)`, `with_resolve_successors(false)`, `with_thesaurus(false)`) or per request (`vector_fusion: "absolute"`, `collapse_duplicates: 0`, `resolve_successors: false`, `synonym_weight: 0`).
- **Deprecated** — `RankedSearchQuery::{llm_rerank, llm_model, llm_rerank_top_k, with_llm_reranking}`, `RankedSearchScore::llm_score` (LLM reranking was never implemented) and `search::ppr` (never called by ranked search) are no-ops marked `#[deprecated]`, to be removed in the next breaking release.
- **Full-protocol benchmarks (2026-11-01, `fastembed-minilm`, fresh ingest, same scripts as 0.10.9.54)** — LoCoMo-10P default R@5/R@10/R@20 67.9/76.7/83.4% (0.10.9.54: 63.9/73.5/–); LongMemEval default R@5/R@10/R@20 69.8/75.6/81.4% (0.10.9.54: 68.0/72.8/78.8%); about 428/371 queries/s. Raw outputs: `results/benchmarks/2026-11-01-full-protocol/`.

### Vector Sidecars

MentisDB now exposes an additive Phase 3 vector sidecar surface for direct crate use:

- `search::EmbeddingProvider`
- `search::EmbeddingMetadata`
- `search::VectorSidecar`
- `VectorSearchQuery`
- `MentisDb::vector_sidecar_path(&EmbeddingMetadata)`
- `MentisDb::load_vector_sidecar(&EmbeddingMetadata)`
- `MentisDb::vector_sidecar_freshness(&VectorSidecar, &EmbeddingMetadata)`
- `MentisDb::rebuild_vector_sidecar(&provider)`
- `MentisDb::manage_vector_sidecar(provider)`
- `MentisDb::unmanage_vector_sidecar(&EmbeddingMetadata)`
- `MentisDb::managed_vector_sidecars()`
- `MentisDb::apply_persisted_managed_vector_sidecars()`
- `MentisDb::managed_vector_sidecar_statuses()`
- `MentisDb::set_managed_vector_sidecar_enabled(kind, enabled)`
- `MentisDb::sync_managed_vector_sidecar_now(kind)`
- `MentisDb::rebuild_managed_vector_sidecar_from_scratch(kind)`
- `MentisDb::query_vector(&provider, &VectorSearchQuery)`

Contract:

- embeddings remain optional, and MentisDB still works with no vector dependencies at all
- vector state lives in a rebuildable sidecar, never in the canonical append-only chain
- vector sidecars are separated by `chain_key`, `thought_id`, `thought_hash`, `model_id`, embedding dimension, and embedding version
- changing the embedding model or version invalidates old vector state instead of silently mixing incompatible embeddings
- callers can opt one embedding space into append-time synchronization on a live handle by registering a managed vector sidecar provider
- vector hits surface whether they came from a `Fresh` or stale sidecar
- deleting or corrupting the sidecar degrades only vector retrieval; plain chain reads, appends, and lexical/graph search still work
- since 0.10.6, each append writes one integrity-chained WAL record beside the JSON snapshot (`*.json.wal`, magic `MDBVWAL1`). Load replays the WAL after verifying the snapshot digest. The snapshot is compacted and the WAL removed every 32 records. Older binaries that only read JSON treat a sidecar with a pending WAL as stale and rebuild.

Operational flow:

- rebuild a sidecar explicitly for one provider and chain
- or register that provider as a managed vector sidecar and keep it fresh on future appends for that open handle
- load or query that sidecar later with the same embedding metadata
- if the chain head changes, the sidecar becomes stale and results report that freshness state until the sidecar is rebuilt

### `mentisdb` Default Vector Sidecar

`mentisdb` now applies a persisted managed-vector setting every time it opens a chain.

- by default each chain gets the built-in FastEmbed MiniLM embedding provider (`fastembed-minilm`), which runs locally via ONNX with no cloud dependencies. The legacy `local-text-v1` provider is also available.
- the daemon keeps that sidecar synchronized on append unless the user disables auto-sync for that chain
- ranked search in the daemon and dashboard now uses that managed sidecar transparently, blending lexical, graph, and vector signals whenever it is enabled and available
- the web dashboard exposes per-chain controls to:
  - enable or disable append-time auto-sync
  - sync the sidecar to the latest chain state without changing the enable/disable setting
  - rebuild the sidecar from scratch after an explicit confirmation that the previous file will be deleted and recreated
- if auto-sync is disabled, new thoughts can make the sidecar stale until the user syncs or rebuilds it

Since 0.10.9 (issue #23, memory blow-up with many chains):

- one FastEmbed model is loaded per process and shared by every chain, and texts are embedded in small bounded batches, so memory no longer grows with the number of open chains
- the ONNX model cache lives in `<MENTISDB_DIR>/.fastembed_cache` instead of the daemon's working directory; set `FASTEMBED_CACHE_DIR` to put it elsewhere
- opening a chain never embeds its history on the request path: chains with more than 32 thoughts and no fresh sidecar are rebuilt by a single background worker. Until the rebuilt sidecar is adopted (on the next request or append once the worker finishes), ranked search on that chain returns lexical and graph results only
- opening a chain no longer rewrites its persisted vector provider configuration
- `MENTISDB_EMBEDDINGS` selects the embeddings mode process-wide: unset (default: FastEmbed when compiled in, local text otherwise), `off` (no managed sidecars, lexical only), `local-text` (built-in `local-text-v1` hashing, never loads ONNX), or `fastembed`

Upgrading from 0.10.1–0.10.8: the first start after upgrading may show lexical-only ranked results for large chains while their sidecars rebuild in the background. A stray `.fastembed_cache/` left in the directory you used to start the daemon from can be deleted; the model is re-downloaded into the new location once.

### HNSW approximate-nearest-neighbor vector backend

By default MentisDB uses an exact cosine scan over the managed vector sidecar.
Once the sidecar reaches `MENTISDB_HNSW_THRESHOLD` vectors (default 50,000) the
backend automatically switches to an **HNSW** approximate graph for that
sidecar. The same `VectorSearchBackend` trait powers both implementations, so
public APIs and hybrid/ranked search results stay the same:

- small corpora keep the deterministic exact backend
- large corpora get sub-linear approximate search with no query change
- `MENTISDB_HNSW_EF_CONSTRUCTION` and `MENTISDB_HNSW_EF_SEARCH` tune accuracy
  versus latency
- `MENTISDB_HNSW_BACKGROUND_BUILD` (default true) builds the graph off-thread
  while the daemon keeps answering queries

End users see lower latency transparently. The HNSW backend is always compiled
in since 0.10.4.49.

#### How vectors are stored (0.12)

Every vector of a managed sidecar lives once, in a flat store of 128-row chunks:
one 64-byte-aligned allocation per chunk, rows padded to whole 64-byte lines. The
sidecar entries, the exact index, the HNSW graph and the implicit-edge scanner all
hold handles to those rows, so there is no second copy of the corpus (about 150 MB
saved at 100,000 vectors of 384 dimensions per consumer). Exact search scores a
row with a 16-lane dot product written so the compiler emits NEON (aarch64) or
SSE2 (x86_64) instructions without `unsafe` intrinsics, a nightly toolchain or
runtime CPU probing; every platform computes the same bits. Scores equal a
sequential cosine within 1e-5. One limit: an HNSW graph loaded from disk keeps
its own copy of the vectors in the graph (the `hnsw` crate owns them); a graph
built in this process shares fully.

### REST Lexical Search

The daemon also exposes the Phase 1 ranked lexical surface over REST at `POST /v1/lexical-search`.

This is the right endpoint when you want lexicographical/lexical text ranking only, with simple score and match provenance fields.

Request shape:

```json
{
  "chain_key": "mentisdb",
  "text": "latency ranking",
  "agent_ids": ["planner"],
  "thought_types": ["Decision"],
  "offset": 0,
  "limit": 10
}
```

Example response:

```json
{
  "total": 1,
  "results": [
    {
      "thought": {
        "index": 42,
        "agent_id": "planner",
        "content": "Latency budget for the Europe rollout."
      },
      "score": 2.91,
      "matched_terms": ["latency", "ranking"],
      "match_sources": ["content", "tags", "agent_registry"]
    }
  ]
}
```

### Phase 4 Transport Contract (Ranked + Bundles)

Phase 4 transport work keeps plain `POST /v1/search` and `POST /v1/lexical-search`
compatibility and adds two additive endpoints:

- `POST /v1/ranked-search` for flat ranked retrieval
- `POST /v1/context-bundles` for seed-anchored grouped support context

Example `POST /v1/ranked-search` request:

```json
{
  "chain_key": "mentisdb",
  "text": "performance budget",
  "thought_types": ["Decision"],
  "limit": 10
}
```

**Result window.** A page is ranked from the top, so `offset + limit` may not exceed 10,000 on `/v1/ranked-search`, `/v1/lexical-search`, `/v1/federated-search`, `/v1/context-bundles`, their MCP tools and `mentisdb search`. A larger window is refused with `400` and a message naming the maximum (it is not clamped, which would return the wrong page); narrow the query with filters or `since`/`until` to read deeper. A standing-context `per_type_limit` above 100 is refused the same way.

When a managed vector sidecar such as the built-in `fastembed-minilm` provider is active for that chain, the ranked backend becomes `hybrid` or `hybrid_graph` and the response includes a non-zero `score.vector` component for semantic-only or semantic-boosted hits.

Ranked response contract fields:

- `backend`
- `results[].score.{lexical,vector,graph,relation,seed_support,importance,confidence,recency,session_cohesion,rrf,total}`
- `results[].matched_terms`
- `results[].match_sources`
- `results[].graph_distance`
- `results[].graph_seed_paths`
- `results[].graph_relation_kinds`
- `results[].graph_path`
- `results[].chain_key` (present when searching branch chains with ancestor results)

Context-bundle response contract fields:

- `total_bundles`
- `consumed_hits`
- `bundles[].seed.{locator,lexical_score,matched_terms,thought}`
- `bundles[].support[].{locator,thought,depth,seed_path_count,relation_kinds,path}`

MCP transport mirrors this split with additive tools:

- `mentisdb_ranked_search`
- `mentisdb_context_bundles`

Acceptance coverage for these transport contracts lives in:

- `tests/search_transport_contract_tests.rs`

Response shape:

```json
{
  "total": 2,
  "results": [
    {
      "thought": { "index": 42, "agent_id": "planner", "content": "..." },
      "score": {
        "lexical": 2.91,
        "vector": 0.27,
        "graph": 0.18,
        "relation": 0.05,
        "seed_support": 0.0,
        "importance": 0.0,
        "confidence": 0.0,
        "recency": 0.0,
        "total": 3.14
      },
      "matched_terms": ["latency", "ranking"],
      "match_sources": ["content", "tags", "agent_registry"]
    }
  ]
}
```

---

## Public and private chains

A chain is **public** (anyone with access writes unsigned and reads freely) or
**private** (writes need a signature by an authorized Ed25519 key, and what is
written while private can be read only by a reader who proves possession of an
authorized key). Mode changes are signed records in the chain that open
*segments*; every thought belongs to the segment its position falls in, so an
unauthorized reader sees only the public segments, on every read surface
(search, context, traversal, exports, listings, counts).

```bash
# operator (dashboard PIN, or --offline on the host that holds the data directory)
mentisdb chain access set private --chain vault --pin 123456
mentisdb agent key generate builder --key-id builder-1 --chain vault --pin 123456   # makes the pair, registers the public key
# (or register a key made elsewhere:)
# mentisdb agent key add builder --key-id builder-1 --public-key-hex <64 hex> --chain vault --pin 123456
mentisdb chain access allow builder builder-1 <64 hex> --chain vault --pin 123456

# an authorized client signs every request locally; the key never leaves it
mentisdb search "launch plan" --chain vault --read-key-file builder.key --read-agent builder --read-key-id builder-1
MENTISDB_READ_KEY_FILE=builder.key MENTISDB_READ_AGENT_ID=builder MENTISDB_READ_KEY_ID=builder-1 mentisdb --mode stdio
```

`agent key generate` creates the Ed25519 pair on the machine you run it on,
saves the private seed (64 hex characters) to an owner-only file (`--out FILE`,
else `$MENTISDB_KEY_DIR/<public key prefix>.key`, default `~/.mentisdb/keys`;
`--force` to overwrite), and registers only the public key. The private key is
never printed, logged or sent, and that file is its only copy: MentisDB cannot
recover it, so back it up, and never paste it into a chat or give it to an AI
agent. If the registration fails after the file was written the file is kept and
the error prints the `agent key add ... --public-key-hex` command that registers
it later. The dashboard offers the same on the agent page ("Generate key pair"),
generated in the browser with WebCrypto, so the private key never reaches the
server. Use the file with `--private-key-file` / `--read-key-file`.

Only the operator can add or remove keys; REST and MCP cannot. Every
returned thought carries a `provenance` object (segment, signature, verified
agent, `trust: untrusted_data`) and the operating skill tells agents to treat
memories as data, never as instructions. The prompt blocks loaded at session
start (standing, recent and restored context, the `MEMORY.md` export) render
every entry as one escaped line, so stored text cannot close a block or forge an
entry, and each standing entry shows `trust=verified|unsigned|unverified`. Serve private chains over HTTPS.
Details, wire formats and the threat model: [docs/CHAIN_ACCESS.md](docs/CHAIN_ACCESS.md).

## Web Dashboard

The daemon includes an embedded browser UI at:

```text
https://127.0.0.1:9475/dashboard
```

The dashboard is served over HTTPS with the same self-signed certificate used by
the HTTPS MCP and REST surfaces.

Dashboard capabilities:

- live chain listing with thought, agent, and storage-size counts
- thought exploration with grouped ThoughtType filters, refs, and typed relations
- chain-scoped ranked search with text and live-agent filters
- grouped context bundles for seed-anchored supporting search context
- ranked result inspection in the thought modal, including score breakdowns, matched terms, graph distance, relation kinds, and bundle support preview
- per-chain vector sidecar inspection plus enable/disable, sync, and rebuild controls
- agent detail management for display name, description, owner, status, and signing keys
- latest agent-thought browsing without restarting the daemon after new thoughts are appended
- chain import from `MEMORY.md`
- cross-chain agent-memory copy with agent metadata preserved on the target chain
- skill browsing, summary counts (total / active / revoked / deprecated), diffing, editing into new immutable versions, deprecation, revocation, and permanent delete of revoked skills
- Settings tab to view and edit all `MENTISDB_*` environment variables with live apply, reset-to-default, and `.env` persistence

Protect the dashboard with `MENTISDB_DASHBOARD_PIN` whenever the daemon is reachable
outside localhost.

### Host allowlist

One list of `Host` names serves the dashboard, REST and MCP: `localhost`, `127.0.0.1`,
`[::1]`, the configured `MENTISDB_BIND_HOST`, every entry of
`MENTISDB_DASHBOARD_ALLOWED_HOSTS` and, when `MENTISDB_BIND_HOST` is `0.0.0.0` or `::`, the
machine's own interface IPs. A VPS reached by its public IP or DNS name through a loopback
bind and a reverse proxy lists that name in `MENTISDB_DASHBOARD_ALLOWED_HOSTS`.

**The `my.mentisdb.com` alias is accepted on TLS listeners only** (HTTPS MCP, HTTPS REST and
the dashboard, whose certificate carries the name). It is a public DNS record that points at
`127.0.0.1`, but MentisDB does not control it: whoever controls that name (a lapsed domain, a
compromised registrar account) could serve a page and rebind the name to your loopback
daemon, and a plain-HTTP listener would take the page for "same-origin". So the plain HTTP
MCP and REST ports (`9471`, `9472`) answer `403` to `Host: my.mentisdb.com` unless you opt in
with `MENTISDB_DASHBOARD_ALLOWED_HOSTS=my.mentisdb.com`. Use `https://my.mentisdb.com:9473`
(MCP), `:9474` (REST) and `:9475` (dashboard), or `http://localhost:9471`.

The domain owner can still hold the name safely: enable the registrar's transfer/registry
lock and two-factor sign-in, and turn on DNSSEC for the zone. Keep bearer tokens
(`MENTISDB_BEARER_TOKEN_ACCESS=true`) and the dashboard PIN on whenever the daemon holds
data you care about: a rebinding page cannot present a token or the PIN.

- **MCP on a loopback bind (the default)** refuses any other `Host` with `403`, for every
  client, on `POST /`, the `GET /` event stream and the legacy `/tools/*` and
  `/resources/*` routes. This is the DNS-rebinding defence of `cloudllm_mcp` 0.4, fed with
  the list above so your configured names keep working (and `my.mentisdb.com` on the HTTPS
  listener). A proxy that
  forwards an unlisted `Host` gets `403 Forbidden host`: add the name to
  `MENTISDB_DASHBOARD_ALLOWED_HOSTS`.
- **MCP on a wildcard bind** (Docker, LAN) performs no `Host` check for non-browser
  clients, which reach the daemon by service name or DHCP address.
- **REST on a loopback bind (the default)** checks `Host` for every request, like MCP does:
  `curl`, the CLI, agents and browsers alike get `403` (`host 'X' is not allowed; set
  MENTISDB_DASHBOARD_ALLOWED_HOSTS ...`) unless the name is in the list. A request with no
  `Host` header at all (HTTP/1.0, in-process) passes. **Reverse proxy note:** an nginx or
  Caddy in front of a loopback daemon forwards the public name as `Host` by default; add
  that name to `MENTISDB_DASHBOARD_ALLOWED_HOSTS` (or have the proxy send `Host:
  127.0.0.1:9472`), or every proxied REST call is refused.
- **REST on a wildcard bind, and MCP with bearer tokens off**, refuse a request from a
  browser (it carries `Origin` or `Sec-Fetch-Site`) unless its `Host` and `Origin` host are
  in the list. `curl`, the CLI and agents send neither header and are unaffected.
- IPv6 entries match in canonical form (`2001:db8::7`, not `2001:0db8::7`).

Dashboard API rules (0.10.9):

- **Host allowlist (DNS-rebinding defence).** Every dashboard route, including `GET` pages
  and `/dashboard/login`, rejects a request with `403` unless its `Host` header names this
  daemon: `localhost`, `127.0.0.1`, `[::1]`, `my.mentisdb.com` (