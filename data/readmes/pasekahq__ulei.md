# ulei

[![CI](https://github.com/pasekahq/ulei/actions/workflows/ci.yml/badge.svg)](https://github.com/pasekahq/ulei/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/pasekahq/ulei/badge)](https://scorecard.dev/viewer/?uri=github.com/pasekahq/ulei)
[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)

`ulei` is the home of a personal agent ecosystem: the pieces around an AI assistant that
should outlive any particular agent runtime. It is a Rust cargo workspace with strict module
boundaries, language-neutral contracts and resource budgets enforced in CI.

**Status:** pre-alpha, building the MVP (see [roadmap](docs/roadmap.md)). The agent loop
(`ulei-engine`, against qb's model gateway), the Telegram channel (`ulei-channels`) and the owner
inbox (`ulei-core`) are being built in sprints U1–U4; `ulei-memory` serves the archive store as a
daemon; `ulei-hive` and `ulei-glue` are still empty shells. Code moves in step by step from the existing Python system. No release
yet; not ready for use.

## Modules

| Crate | Purpose |
|---|---|
| `ulei-contracts` | Rust types generated from `contracts/` |
| `ulei-core` | owner inbox and events, module registry, config, notifications, MCP tools, `ulei` CLI, `ulei-connectors` runner of the source connectors |
| `ulei-hive` | task cards executed by agent "heads", acceptance, delivery |
| `ulei-garden` | garden of typed facts about the owner's life and their retrieval ([README](crates/garden/README.md)) |
| `ulei-memory` | archive of raw items of every source and the forest of session summaries made from it (C10) ([README](crates/memory/README.md)) |
| `ulei-runtime-adapters` | bridges to agent runtimes |
| `ulei-channels` | owner channels (Telegram first) |
| `ulei-glue` | bridges to standalone products (quota balancer, A2A gate) |
| `ulei-engine` | own agent loop: tools, sessions; models only through the qb gateway |
| `ulei-connector-test` | source connector over a synthetic source, the test subject of the connector runner (C11) |
| `ulei-connector-mcp-example` | source connector wrapping a ready MCP server's listing tool, the pattern for wrapping one; not released (C11) |
| `ulei-priv` | privileged helper: a root daemon that runs a fixed, audited list of root commands for the engine, which has no sudo (ADR-0073) |

Modules never depend on each other; they share only the generated contract types and talk
over the wire. Standalone products (for example [qb](https://github.com/pasekahq/quota-balancer))
live in their own repositories and are pinned in [`ecosystem.lock`](ecosystem.lock).
The current module graph: [docs/architecture/module-map.md](docs/architecture/module-map.md).
Decisions: [docs/architecture/adr/](docs/architecture/adr/).

## Python hive (`hive-py/`)

The task hive that runs today (cards, heads, gate, schedules and series, delivery of results) is
Python in [`hive-py/`](hive-py/) until the Rust hive of step P6 replaces it
([ADR-0068](docs/architecture/adr/0068-python-hive-in-hive-py.md)): the package `hive/`, its CLI and
scripts `scripts/hive*.py`, the tests `tests/hive/`, the neutral texts `texts/` and
`config.example.toml`. Every hive process reads its config from `--config` or `HIVE_CONFIG` and fails
without one; the deployment's own config and texts live outside the repository.

```sh
HIVE_CONFIG=/path/to/config.toml python3 hive-py/scripts/hive.py list
```

[`hive-py/AGENTS.md`](hive-py/AGENTS.md) gives the local test command, the same as the CI job `hive-py`.
The switch of the live hive to `hive-py/` and its rollback: [docs/runbooks/hive-cutover.md](docs/runbooks/hive-cutover.md).

## Contracts

| Id | Contract |
|---|---|
| C1 | event of the owner inbox |
| C2 | MCP tools of the core |
| C3 | card → head → report |
| C4 | qb API (vendored) |
| C4G | qb model gateway (vendored) |
| C5 | A2A gate, owner side |
| C6 | runtime adapter protocol |
| C7 | garden search and proposals |
| C8 | session journal of the engine |
| C9 | `ulei.toml`, the deployment config |
| C10 | archive of raw source items |
| C11 | source connector and its runner |

They are JSON Schema 2020-12 / OpenAPI 3.1 files in [`contracts/`](contracts/), with golden
fixtures and a changelog, so components in any language (including the existing Python
ones) can use them.

## Requirements

- Rust stable with `rustfmt` and `clippy` (MSRV 1.89), target `x86_64-unknown-linux-musl` for
  release binaries.
- Python 3.9+ only to run `ci/broad_check.py` (standard library); CPython 3.12 for `hive-py/`.

## Quick start

```sh
cargo build --workspace
cargo test --workspace
python3 -m ci.broad_check     # fmt, clippy, tests, architecture and contract checks
cargo run -p ulei-core --bin ulei -- contracts
```

Release build and budgets: `ci/budgets.sh` measures the static musl binaries `ulei`,
`ulei-inbox`, `ulei-engine`, `ulei-web` (and its `web-loopback-http` test build), `ulei-tg`,
`ulei-garden`, `ulei-memory` and `ulei-connectors`, and the glibc helper `ulei-garden-embed`. The builds and the call are the last
lines of [AGENTS.md, Commands](AGENTS.md#commands-all-must-pass-before-you-push).

## `ulei status`

```sh
ulei status [--config PATH]
```

It reads `inbox.socket`, `engine.c6_socket`, `engine.owner_session` and `qb.socket` from
`ulei.toml` (the file from `--config`, else `ULEI_CONFIG`, else `$XDG_CONFIG_HOME/ulei/ulei.toml`,
else `~/.config/ulei/ulei.toml`), probes the inbox, the engine and the qb gateway at once over
their sockets and prints one line per item within 10 s. It opens no database and writes
nothing. The engine's `ULEI_*` variables are not read, so a unit that sets them can serve other
sockets than the file names.

```text
inbox: up /run/ulei/inbox.sock (ulei-inbox 0.0.1)
queue: pending 0, leased 0, processing 0, deferred 0, uncertain 0
engine: up /run/ulei/engine.sock
channel: up
session: owner-session idle since 2026-01-01T09:00:00Z, queue 0, route main
last turn: turn-1 completed at 2026-01-01T09:00:00Z
qb: up /run/qb/gateway.sock (1.0.0)
route main: ready vendor-a/model-a
hive-mcp: up 127.0.0.1:8740
```

The last line is `ulei-hive-mcp` (ADR-0074): an unauthenticated request to `hive_mcp.listen`,
else to the engine's `engine.mcp.hive.url` (then ` (engine.mcp.hive.url)` follows the address),
answered `401`; `hive-mcp: not configured` when the file has neither. It never changes the exit
status.

A daemon that is down is its line with the reason, such as `inbox: down <socket>: connect:
Connection refused` or `engine: down <socket>: no answer within 5 s`; the other daemons are still
reported. Every line, its down forms and reasons are in ADR-0040 section 5. Exit 0 when `inbox`,
`engine`, `channel` and `qb` read `up`; 1 when one of them reads `down` or `unknown`; 2 for a
usage error or a config without one of the four keys, with nothing probed.

## `ulei-connectors`

```sh
ulei-connectors serve [--config PATH]
ulei-connectors list [--config PATH]
ulei-connectors run NAME [--config PATH]
ulei-connectors reset NAME [--config PATH]
ulei-connectors exec NAME DATA_DIR DIR [--key FILE] [--read PATH]... [--write PATH]...
                     [--landlock-off] [--direct [--port N]...] -- PROGRAM [ARG...]
```

The runner of the source connectors (ADR-0056, contract C11). It reads `connectors.dir`,
`connectors.enabled`, `connectors.state`, `connectors.log`, `connectors.run_dir`,
`connectors.sync_every`, `memory.socket` and the owner's `[connectors.<name>]` from `ulei.toml`.
`serve` reads them once at start, writes its ready line `ulei-connectors: ready: <n> connectors,
sync every <s> s` on stderr once its schedule is set, and runs each connected connector on its
schedule: due at `max(last start + every, not_before)`, at once for one never run or overdue after
downtime, and then once per period, never once per missed period. It calls C10 `sync` at start and
every `sync_every` seconds (default 900); a failed `sync` is one stderr line. Between due times it
sleeps without a wake-up. At most four runs are in flight; a due run without a free slot starts when
one frees. A connector due while its run is in flight, in `serve` or in a `run` of another process,
is recorded with outcome `busy` and no unit: a run holds the `flock` of
`<connectors.state>/<name>/lock`. A connector's `error` with `rate_limited` and `retry_after` puts
its next run off to the end of that run plus `retry_after`; `runner.json` keeps the last start and
that `not_before`, so a restart keeps the schedule. On SIGTERM or SIGINT `serve` stops the units of
its runs with `systemctl --user stop`, writes their records and exits 0; it exits 2 for a config
without its keys. Each enabled name without a valid manifest is one stderr line and is not
scheduled. `list` prints `name transport every Ns` for each enabled name whose directory holds a
valid `connector.json`, and one stderr line for each enabled name that does not (exit 1 then). `run`
starts one run of a connector now as a transient service of the user manager, `systemd-run --user
--wait --pipe --collect --unit=ulei-connector-<name>-<unix time>`, with the seccomp and limit
properties of ADR-0056 section 5.1 (no socket of any family, `MemoryMax=256M`, `TasksMax=64`,
`RuntimeMaxSec=` the manifest's `timeout`); the unit's stdio are the runner's pipes. Before it
starts the unit, the runner listens on its network broker `<connectors.run_dir>/<unit>.sock` (mode
0600, `run_dir` created 0700, at most 107 bytes and no colon) for one connection, which the manager
makes through `OpenFile=` and hands to the connector as fd 3 named `broker`; once connected the
runner unlinks the path. On it each C11 `BrokerRequest` line gets one `BrokerReply` line (ADR-0056
section 5.3): `{"ok": "ip:port"}` with the connected TCP socket attached by `SCM_RIGHTS`, or
`{"error": code}`. Only the `host:port` entries of the manifest's `source.addresses` and the owner's
`allow` are connected, resolved at each request and tried with a 10 s connect timeout per address;
an entry that resolves to a loopback, private, shared (`100.64.0.0/10`), link-local, unspecified
(`0.0.0.0/8`, `::`), multicast, broadcast, reserved (`240.0.0.0/4`) or local NAT64
(`64:ff9b:1::/48`) address, or to an IPv6 address embedding such an IPv4 one (mapped, compatible,
`64:ff9b::/96`, 6to4 `2002::/16`), is `not_allowed` unless the owner's `allow` names it; the 33rd
connection of a run is `limit`; a line that is not a `BrokerRequest`, or longer than 4 KiB, ends the
broker. The broker ends with its run on every outcome, a connect in flight included, and leaves no
file in `run_dir`. Under the owner's `network = "direct"` the unit gets
`RestrictAddressFamilies=AF_INET AF_INET6` instead, and the launcher its `--direct` ports, the ports
of `source.addresses` and `allow`; the broker is still passed. The run hands the connector its C11
`Request`: a `stdio` connector gets it as one stdin line and answers C11 `Line`s; an `mcp` connector
is an MCP server on the same pipes, which the runner initializes (protocol `2025-11-25`, client
`mcp` `0.1.0`, an answered version among ADR-0026's) and calls `tools/call` `ulei_pull` with the
`Request` as arguments, again with each page's `cursor` while `more` is true. An `isError` result is
the connector's `Error`; a server request is answered with JSON-RPC error `-32601`, a notification
ignored. A message that is not JSON-RPC 2.0 or not the answer to the pending id, a JSON-RPC error
answer, a result without a C11 `Page` (or with `isError` an `Error`) as `structuredContent`, another
protocol version or `more: true` with the cursor of the call ends the run `protocol`. After the last
page or an error the runner closes the server's stdin and stops its unit if it still runs 3 s later;
the run keeps its outcome. The run puts every item into the archive as C10 `put` with `source` = the
connector's name, as it reads it, stores the cursor in `<connectors.state>/<name>/runner.json` once
every item before it was answered, appends one C11 `RunRecord` line naming the unit, the Landlock
ABI and, under `direct`, the connect ports Landlock limited (`connect_ports`) to `connectors.log`
(mode 0600) and prints one stderr line ending in `landlock abi <n>` or `landlock off`, and under
`direct` in `direct connect ports [<ports>]` or `direct connect ports not limited`. A run whose unit
`systemd-run` reports with result `timeout` ends `timeout` with the cursors it stored kept; a
`systemd-run` that cannot start the unit ends the run `refused` with code `unit_start_failed`, and a
broker socket that cannot be bound with code `broker`; a run the runner ends early (`protocol`,
`archive`) has its unit stopped through `systemctl --user stop`. A stdout line or an item of an MCP
page over 1 MiB plus 4 KiB is not kept: an item whose top-level `external_id` is readable anywhere
in it counts as `too_large` with that id, and any other such line or item ends the run `protocol`;
an MCP result's `content` is skipped unread. The owner's `read`, `write` and `landlock = "off"` of
`[connectors.<name>]` reach the launcher in its argv; `read` and `write` must be absolute. Exit 0
for outcome `ok`, 1 for any other, 2 for a usage error, a config without its keys or a connector
that is not enabled or has no valid manifest. `reset` clears the stored cursor, so the next run
starts from the beginning of the source; it refuses, exit 1, while a run of the connector is in
flight.

`exec` is the launcher the unit runs, not a command for the owner. It refuses unless
`/proc/self/status` shows `NoNewPrivs: 1` and `Seccomp: 2` and `/proc/self/cgroup` ends in the unit
`ulei-connector-<NAME>-<unix time>.service`. Unless `--landlock-off`, it then restricts itself with
Landlock (ADR-0056 section 5.2): read and execute on `/usr`, `/etc`, `/lib`, `/lib64`, `/bin`,
`/sbin` and `DIR`, read on `/proc`, the random and zero devices and `--read` paths, read and write
on `/dev/null`, read on the `--key` file alone, and every right but execute on `DATA_DIR` and the
`--write` paths; it needs ABI 3 or later and sets the signal and abstract socket scopes from ABI 6.
With `--direct` on ABI 4 or later it also limits TCP connect to the `--port` values
(`LANDLOCK_ACCESS_NET_CONNECT_TCP`); UDP, DNS included, is not limited. A kernel without Landlock or
below ABI 3 refuses with code `landlock` and a reason naming `ENOSYS`, `EOPNOTSUPP` or the ABI seen.
It then writes `ulei-connectors: exec landlock abi <n>`, followed by ` connect <ports>`
(comma-separated, or `none`) when it limits connect ports, or `ulei-connectors: exec landlock off`
on stderr, clears the environment, sets `HOME` and `TMPDIR` to `DATA_DIR`, `PATH=/usr/bin:/bin` and
`LANG=C.UTF-8`, keeps `LISTEN_FDS`, `LISTEN_FDNAMES` and `LISTEN_PID`, and executes the connector in
`DATA_DIR`. A refusal is one stderr line `ulei-connectors: exec refused <code>: <reason>` and exit
125, which the run records as outcome `refused` with that code. A program that is missing, or a link
in `DIR` to one outside the execute paths, fails `execve` after the Landlock line; that refusal has
code `exec_failed`, and the run takes it only as the line right after the Landlock line.
## Release and install

The `release` job of every CI run builds the static `x86_64-unknown-linux-musl` binaries `ulei`,
`ulei-inbox`, `ulei-engine`, `ulei-web`, `ulei-tg`, `ulei-connectors`, `ulei-memory`, `ulei-hive-mcp`,
`ulei-priv` and `ulei-garden`, the garden's one glibc binary `ulei-garden-embed` (the embedder
helper, dynamic because it opens ONNX Runtime with `dlopen`, ADR-0075), and the test connector
`connectors/test/` (its binary `ulei-connector-test` and its `connector.json`, kept in
`deploy/connectors/test/`), twice, the second time from a clean target directory at another path,
and fails unless both builds give the same `SHA256SUMS`, which lists every file by its relative
path (ADR-0042 section 10, ADR-0056 section 6, ADR-0070, ADR-0075). Where to find a release of commit `<commit>`:

- the artifact `ulei-x86_64-unknown-linux-musl` on the run's summary page (Actions, the `CI` run
  of `<commit>`, Artifacts; the download needs a GitHub login): the eleven binaries, the
  `connectors/test/` tree and `SHA256SUMS`;
- the `SHA256SUMS` notice of the `release` job, readable without a login, beside the `toolchain`
  notice with the `rustc` and `cargo` versions the build used.

`ci/release.sh <out-dir>` in a checkout of `<commit>`, with that toolchain, its musl target and
`musl-tools`, builds the same files and `SHA256SUMS`.

Verify and install, as the account that owns the deployment, from a checkout of `<commit>`:

```sh
unzip ulei-x86_64-unknown-linux-musl.zip -d <release-dir>
cd <release-dir> && sha256sum -c SHA256SUMS && cd -   # compare with the run's notice too
<checkout>/deploy/install.sh <release-dir>
```

The script needs no root: it checks every file of `SHA256SUMS` before it copies anything, puts the
binaries into `$HOME/.local/bin` (mode 0755) and the units of `deploy/systemd` into
`$XDG_CONFIG_HOME/systemd/user` (default `$HOME/.config/systemd/user`, mode 0644), and leaves a
file with the same bytes as it is, so a second run changes nothing. It installs no connector and
not `ulei-priv`, whose sum it checks: the privileged helper is installed by the owner as root to
`/usr/local/lib/ulei/` with its system unit and policy (`docs/runbooks/mvp-pilot-cutover.md`
part 5.2, ADR-0073). It
never writes `ulei.toml` or a secret and never calls `systemctl`; it prints the `systemctl --user`
commands to run next. On a failure it exits 1 with one line `install.sh: <step>: <reason>`.

`<checkout>/deploy/install.sh --connector test --dir <connectors-dir> <release-dir>` checks the
same way and installs the one connector into `<connectors-dir>/test/` (`connector.json` mode 0644,
its binary 0755); a name the release does not hold is refused. Connecting it stays the owner's
`ulei.toml`: `connectors.dir`, `test` in `connectors.enabled`, and `memory.socket`. The runner
puts the items into the archive daemon `ulei-memory`, released and installed with the others.

## systemd user units

[`deploy/systemd/`](deploy/systemd) holds the user units `ulei-inbox.service`,
`ulei-engine.service`, `ulei-tg.service` (ADR-0042), `ulei-connectors.service`, the connector
runner's `ulei-connectors serve` (ADR-0056), `ulei-memory.service`, the archive's
`ulei-memory serve` (ADR-0070), `ulei-hive-mcp.service` (ADR-0071) and `ulei-garden.service`, the
garden's `ulei-garden serve` with its embedder helper (ADR-0075), and the oneshot
`ulei-night.service` with its timer `ulei-night.timer`, the night gardener `ulei-engine night`
(ADR-0078). They run as the account that owns the deployment,
start `ulei-engine` before the inbox and the channel, restart a daemon that exits non-zero, and
allow writes only to these directories, in the layout of ADR-0042 section 3:

| Directory | Holds |
|---|---|
| `<state>/ulei/inbox` | `inbox.root` |
| `<state>/ulei/engine` | `engine.journal`, `engine.terminal_output`, `engine.web_store`, `engine.no_ask_guard.log`, `engine.memory_file`, `engine.user_file`, `engine.skills_dir` |
| `<state>/ulei/telegram` | `telegram.attachments_dir` |
| `<state>/ulei/connectors` | `connectors.state`, `connectors.log` |
| `<state>/ulei/memory` | `memory.archive` |
| `<state>/ulei/garden` | `garden.store`, `garden.core_file` |
| `<state>/ulei/night` | `night.state` |
| `<runtime>/ulei` | `inbox.socket`, `engine.c6_socket`, `memory.socket`, `garden.socket` |
| `<runtime>/ulei-connectors` | `connectors.run_dir` |

`<state>` is `$XDG_STATE_HOME` (default `$HOME/.local/state`), `<runtime>` is `$XDG_RUNTIME_DIR`,
and each unit reads `$XDG_CONFIG_HOME/ulei/ulei.toml` (default `$HOME/.config/ulei/ulei.toml`)
through `ULEI_CONFIG`. `deploy/install.sh` (see [Release and install](#release-and-install))
puts the binaries into `$HOME/.local/bin` and the units into `$XDG_CONFIG_HOME/systemd/user/`
(default `$HOME/.config/systemd/user/`); then, as that account:

```sh
systemctl --user daemon-reload
systemctl --user enable --now ulei-engine.service ulei-inbox.service ulei-tg.service
~/.local/bin/ulei status
```

A written path outside the table needs its directory in a drop-in
(`systemctl --user edit <unit>`, `ReadWritePaths=<dir>`). The units' mount options need a host
that lets the user manager create unprivileged user namespaces.

`ulei-connectors.service` starts each run as a transient unit of the same manager through
`systemd-run --user`, so it allows `AF_UNIX`, `AF_INET` and `AF_INET6` (the user bus, C10 on
`memory.socket`, the broker's TCP connections). A stop sends SIGTERM to `serve` alone
(`KillMode=mixed`), which stops its runs' units, writes their records and exits 0 within
`TimeoutStopSec=30s`. Once `ulei.toml` has `[connectors]` and `memory.socket`:
`systemctl --user enable --now ulei-connectors.service`.

`ulei-memory.service` allows `AF_UNIX` only (its socket and the engine's C6 socket). It starts
after the engine when both start, and without it too: a failed pull is no failure to start, and
C10 `health` names it. Once `ulei.toml` has `[memory]`:
`systemctl --user enable --now ulei-memory.service`, then restart the engine so its archive tools
reach `memory.socket`. Setting it up and importing the old runtime's history:
[docs/runbooks/memory-archive.md](docs/runbooks/memory-archive.md).

`ulei-garden.service` allows `AF_UNIX` only (its socket and the inbox's) and starts the embedder
helper as its child, inside its limits. It starts without the embedder, its model and ONNX
Runtime: `health` then answers `dense: off` and `search` is lexical. Once `ulei.toml` has
`[garden]`: `systemctl --user enable --now ulei-garden.service`. Enabling it, adding the
embedder and moving from a hand-made unit:
[docs/runbooks/garden-service.md](docs/runbooks/garden-service.md).

`ulei-night.service` runs `ulei-engine night` once: it clears the garden's forget queue, sorts the
seedbed and the history of the archive sources `night.sources` into the garden through the model
on `night.route`, within `night.max_usd` a run, and exits. It allows `AF_UNIX` only (the gateway,
the garden and the archive) and has no `[Install]`; `ulei-night.timer` starts it each night. Once
`ulei.toml` has `[night]`, after a dry run: `systemctl --user enable --now ulei-night.timer`.
[docs/runbooks/night-gardener.md](docs/runbooks/night-gardener.md).

## Budgets

| | Limit |
|---|---|
| `ulei` CLI binary (static) | ≤ 512 KiB |
| `ulei --version` peak RSS / cold start / syscalls | ≤ 1 MiB / ≤ 3 ms / ≤ 40, no file opens |
| `ulei-inbox` daemon (static) | ≤ 2.5 MiB binary, ≤ 4 MiB peak RSS, ready ≤ 10 ms, 0 wake-ups when idle, publish p99 ≤ 50 ms, ≤ 128 KiB written per event |
| `ulei status` run | 1 file opened (`ulei.toml`), ≤ 4 MiB peak RSS |
| `ulei-engine` (static) | ≤ 4 MiB binary, ≤ 4 MiB peak RSS and 0 wake-ups while `run` waits for the gateway and while `serve` is idle, `session_search` p50 ≤ 20 ms over 100 sessions of 100 messages |
| `ulei-web` helper (static) | ≤ 2 MiB binary, ≤ 80 MiB peak RSS for a `web_extract` reply near the 16 MiB cap |
| `ulei-tg` channel (static) | ≤ 2.5 MiB binary, ≤ 4 MiB peak RSS and 0 wake-ups while blocked in `getUpdates` |
| `ulei-garden` daemon (static) | ≤ 2.5 MiB binary, ≤ 4 MiB peak RSS, ready ≤ 10 ms, 0 wake-ups when idle, `pointers` p50 ≤ 10 ms and `search` p50 ≤ 20 ms on 2,000 facts, ≤ 128 KiB written per seedbed write and per processed record |
| `ulei-garden-embed` helper (glibc) | ≤ 2 MiB binary, linked only to glibc's own libraries |
| `ulei-memory` daemon (static) | ≤ 2.5 MiB binary, ≤ 4 MiB peak RSS, ready ≤ 10 ms, 0 wake-ups when idle, `put` p50 ≤ 10 ms and `search` p50 ≤ 20 ms on 10,000 items, ≤ 128 KiB written per stored `put` |
| `ulei-connectors` daemon (static) | ≤ 2.5 MiB binary, ready ≤ 10 ms, 0 wake-ups with nothing due, ≤ 4 MiB peak RSS after 100 runs and after one MCP page of ten items of about 1 MB and one of 2 MiB over the cap, ≤ 16 KiB written per run |
| each future daemon | ≤ 2.5 MiB binary, ≤ 4 MiB RSS, 0 wake-ups when idle |

## Tooling

`cargo xtask <command>`:

- `arch` — crate-graph boundaries and source rules;
- `gen-contracts [--check]` — generate Rust types from `contracts/`;
- `contracts [--base REV]` — validate schemas and fixtures, compatibility against `REV`;
- `module-map [--check]` — regenerate the module map;
- `adr [--base REV]` — ADR format and "architecture changes need an ADR";
- `check` — all of the above in check mode.

## License

Copyright (C) 2026 the ulei contributors.

Licensed under the [GNU Affero General Public License v3.0 only](LICENSE) (SPDX: `AGPL-3.0-only`).
If you run a modified `ulei` for users over a network, section 13 asks you to offer them its source.
Third-party notices are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Contributions are accepted under the same license with a DCO sign-off; see [CONTRIBUTING.md](CONTRIBUTING.md).
