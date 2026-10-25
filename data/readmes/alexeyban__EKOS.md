# EKOS — Enterprise Knowledge Operating System

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=alexeyban_EKOS&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=alexeyban_EKOS)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=alexeyban_EKOS&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=alexeyban_EKOS)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=alexeyban_EKOS&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=alexeyban_EKOS)
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=alexeyban_EKOS)](https://sonarcloud.io/summary/new_code?id=alexeyban_EKOS)

EKOS is the open-source knowledge layer for AI agents: a compiler that turns source code, SQL,
documentation and Git history into evidence-backed knowledge that agents query over MCP. Project
site and documentation: **[ekos.dev](https://ekos.dev)**. Install: **[ekos.dev/docs/getting-started/installation](https://ekos.dev/docs/getting-started/installation.html)**
(a setup wizard in your browser on Linux, Windows 11 and macOS — see [Installation](#installation)).

Unlike traditional enterprise systems that manage data, documents or metadata independently, EKOS treats the entire enterprise as a living knowledge system — a permanently evolving semantic model that can be trusted by both humans and AI.

**First benchmark:** on a real 2,022-file open-source repo ([plausible/analytics](https://github.com/plausible/analytics)), cold ingestion takes 34 seconds, and answering real questions from the compiled ledger costs **67-93% fewer tokens** than raw grep-based search over the source — measured with a standard tokenizer (`tiktoken`), not a hand-rolled estimate, with the one case grep wins included rather than hidden. Full methodology, every command, and every raw output: [The First Benchmark Number](https://alexeyban.github.io/EKOS/presentations/token-benchmark.html).

## About

EKOS is a **compiler for enterprise knowledge**, not a database or document store. It observes an
enterprise's existing systems — source code, Git history, SQL schemas, GitHub issues/PRs,
Confluence, local PDF/DOCX documents — without interpreting them, compiles
those observations through deterministic passes into a Canonical Knowledge Model, and stores the
result in an append-only ledger where every conclusion carries the evidence it was derived from. AI
agents (Claude Code among them) read that ledger through a read-only Model Context Protocol server
(`ekos mcp serve`, RFC 0013) — they never touch raw enterprise systems directly.

The project follows an RFC-first workflow (`docs/rfcs/`): every capability is designed in writing
before it's implemented, and the `devlogs/devlog_*.md` files are the running record of
what shipped, why, and what was learned building it. It is written in Rust (2024 edition) as a
Cargo workspace, and is licensed under the [MIT License](LICENSE).

## The Problem

Modern enterprises contain enormous amounts of valuable knowledge distributed across disconnected systems: source code, databases, data warehouses, documentation, wikis, Git repositories, infrastructure-as-code, APIs, runtime logs, and monitoring systems. Every system contains only a partial description of reality. Documentation becomes outdated. Employees leave. Business logic remains hidden inside production code. AI assistants receive fragmented, inconsistent, and often contradictory information.

**Enterprises continuously lose knowledge.**

## The Insight

The enterprise already contains its own documentation — embedded inside source code, SQL, infrastructure definitions, APIs, logs, deployment history, schemas, and runtime behaviour. The problem is not missing information. The problem is the absence of a **compiler** capable of transforming enterprise reality into enterprise knowledge.

EKOS is that compiler.

## Architecture

```
          Enterprise Systems
 Git   SQL   APIs   Confluence   Logs   Cloud   Monitoring
                        |
                 Observation Layer        ← collects facts, no interpretation
                        |
               Knowledge Compiler         ← multi-pass: normalize → analyze → recover → verify
                        |
          ┌─────────────┴─────────────┐
   Knowledge Recovery          Identity Resolution
          └─────────────┬─────────────┘
                        |
          Canonical Knowledge Model (CKM)  ← language/storage/AI-provider independent
                        |
           Semantic Knowledge Ledger        ← append-only, every fact traceable to evidence
                        |
          ┌─────────────┴─────────────┐
    Knowledge Runtime          Knowledge Services
          └─────────────┬─────────────┘
                        |
            AI Agents & Enterprise Applications
```

### Semantic Primitives

The ledger stores four immutable primitives:

| Primitive | Description |
|-----------|-------------|
| **Object** | Identity of a concept: Customer, Product, Dataset, Service, Business Rule |
| **Relationship** | Semantic connection between objects (first-class, not just a foreign key) |
| **Event** | Immutable change — the only mechanism that mutates enterprise state |
| **Evidence** | Origin of knowledge: SQL query, source code, Git commit, log line, API spec |

Every semantic conclusion is supported by evidence. Every change is auditable.

### Key Invariants

- The **Observation Layer** collects facts only — it never interprets business meaning.
- The **ledger is append-only** — knowledge is never modified in place.
- The **Runtime is read-only** — it reconstructs and interprets state, never modifies it. This is enforced by the type system: the store API is split into a read-only `KnowledgeReader` and a `KnowledgeStore` that adds the writes, and the Runtime, EKL and graph export only ever hold a `KnowledgeReader`.
- **Human decisions stay human.** Confirming business definitions, settling conflicts, promoting session notes, approving migrations and confirming treasury payment authorizations are CLI / web console actions only; a test parses the MCP server and fails if any of them becomes reachable from it, even through a renamed import.
- **AI systems** consume reconstructed knowledge through the Runtime; they never touch raw enterprise systems directly. The one explicit, scoped, audited exception is the gated `ekos_clickhouse_query` MCP tool (RFC 0056, off by default) — see below.
- Every compiler pass is **deterministic** and **side-effect-free**. Evidence ids are derived from the evidence's content, so re-running a pass over unchanged sources writes no new ledger versions.
- Every artifact is **content-addressable** (id + checksum + metadata + dependencies + version).
- **Secrets and PII are never observed or stored** (RFC 0043) — a built-in baseline redacts known
  secret shapes (AWS/GitHub/Slack/Google/Stripe tokens, private keys, JWTs, generic
  key/password assignments) from all observed content, and excludes files like `.env`/`*.pem`/
  `id_rsa` entirely. The same rule covers every later re-read of a workspace file for a model or
  the ledger (symbol source, crate doc comments, view definitions: one shared `read_redacted`)
  and the `git blame` commit subjects recorded as rationale. `ekos.toml`'s `[security]` section
  can only extend this baseline, never disable it.

## Implementation

**Language:** Rust (2024 edition), Cargo workspace.

**Crates (`ekos/crates/`):** `compiler-core`, `compiler-sdk`, `observation-sdk`, `artifact`, `kir`,
`scheduler`, `sql-dialect-sdk`, `ledger`, `runtime`, `identity`, `recovery`, `ekl`, `semantic`,
`marketing`, `docs-gen`, `dbt-gen`, `common`, `cli`, `demo-server`, `segment-backend` / `cluster` /
`distributed` (RFC 0111/0113's partitioned + horizontally-distributed storage — see below),
`simulation` (RFC 0047-0055's opt-in World Engine — see below), `clickhouse-query` (RFC 0056's
opt-in live NL-to-SQL query engine — see below), `evals` (RFC 0138's answer-grading harness — see
below), `session` (RFC 0151 agent session memory), `plpgsql` (RFC 0163's PL/pgSQL parser and
procedural IR), `plsql` (RFC 0210's Oracle script scanner and PL/SQL front end), `ora-live` (RFC 0211's
read-only Oracle catalog reader), and EKOS Migrate's `migrate`, `migrate-dq`, `migrate-logic`, `migrate-validate`, `migrate-approval`,
`migrate-report`, `migrate-target-clickhouse` and `pg-live` (RFC 0154–0162 — see below). The same workspace also builds `ekos` with a generic extension seam (RFC 0149) that out-of-tree
builds plug extra connectors and MCP tools into.

**Connectors (`ekos/plugins/`):** File, Git, GitHub issues/PRs (live-verified against a real
repo, 1,600 real issues/PRs — RFC 0062), Confluence, local documents
(PDF/DOCX/text/Markdown/HTML/email — text, tables, image OCR), Pentaho Kettle (`.ktr`/`.kjb` —
RFC 0027), Python/PySpark source (real AST parsing, DataFrame chains recovered into the
Transformation IR — RFC 0038/0040), Rust source (real AST parsing, real function-call graph —
RFC 0041), Elixir and JavaScript/TypeScript source (real AST + `Calls` recovery — RFC 0081/0082),
Perl source (`.pl`/`.pm`/`.t`/`.psgi`, plus `.cgi` with a real `perl` shebang — packages, subs,
`use`/`require` dependencies, `use parent`/`use base`/`@ISA` inheritance, POD descriptions and
source spans; RFC 0147), Java source (`.java` — types, methods and constructors with spans,
signatures and Javadoc, imports and inheritance resolved inside the tree, SQL built in method
bodies folded and linked to the tables it reads and writes, `IDEMPIERE-NNNN` ticket anchors; for the
iDempiere/ADempiere family, the generated model classes become `ModelTable`s with every column's
business name, list values, mandatory flag, default and code-declared foreign key — RFC 0209),
**compiled .NET and JVM binaries with no source available**
(`.dll`/`.exe`/`.class`/`.jar`/`.war`/`.ear` — types, methods, signatures, fields, the real call
graph, branch structure, string/numeric constants and external I/O boundaries, read in-process
from CLI metadata and bytecode with no .NET SDK or JRE required; for .NET, per-method statement
recovery — `if`/loop/`switch`/`try` with the IL offset of every line, labelled with the fidelity actually
reached — plus a per-method migration spec, a Python-rewrite parity check and sandboxed characterization tests that
run the original and check the rewrite against what it did, RFC 0150; RFC 0148 — shipped
as a separately licensed extension build, not part of this open-source repository, RFC 0149), ClickHouse (real HTTP client, schema metadata plus an opt-in live query engine — RFC
0056), a live Oracle catalog connector (read-only sessions, catalog reconciled against the
database's own object counts, behind the `oracle` build feature — RFC 0211), plus scaffolded
proof-of-concept clients for Salesforce, SAP,
Microsoft Fabric, and Snowflake (real API shapes, mock-tested — none yet exercised against a live
account). SQL in the PostgreSQL, SQL Server (T-SQL), MySQL, Snowflake, Databricks and ClickHouse dialects is
parsed from files (RFC 0031); live PostgreSQL / SQL Server database connectors and a Jira connector remain planned.

## Installation

### With the web console: the setup wizard (Linux, Windows 11, macOS — RFC 0185)

The full package holds the `ekos` command, the web console and the Python that runs it; nothing
else is needed. Installing it opens a setup page in your browser:

```bash
curl -fsSL https://raw.githubusercontent.com/alexeyban/EKOS/main/install.sh | sh        # Linux, macOS
```
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/alexeyban/EKOS/main/install.ps1 | iex"   # Windows
```

Or download `ekos-<version>-<target>-full` from the releases page, unpack it and start
`setup.sh` (Linux), `setup.command` (macOS: right-click → Open the first time) or `setup.cmd`
(Windows: **More info → Run anyway** the first time; the program is not code-signed).

The wizard asks where EKOS goes, whether the console is for you alone (local mode: this machine
only, signed in with a one-time code) or for a team (OIDC), which port, a first project and its
source directories, which agents to register it with (Claude Code, Claude Desktop, VS Code —
their config files are backed up and other entries kept), and whether to start the console at
login. It shows the exact list of steps before doing anything. Afterwards:

```bash
ekos console open | status | stop | start | restart | logs
ekos setup                  # change any of it later
ekos uninstall              # the program, login entry, PATH line, agent entries; keeps projects
ekos uninstall --ui         # the same on a page in the browser: what goes, your projects, confirm
```

The console has the same: **Settings → Uninstall EKOS** (local mode, an install made by setup)
opens that page, which keeps working while it removes the console itself (RFC 0188). A project's
top bar has **Init & compile**: init (in-place workspaces), build, recover, resolve (conflicts
reported, not stopping), compile, commit and coverage as one run (RFC 0189).

`ekos setup --answers answers.toml` applies the same answers without a browser (servers,
scripts); `--dry-run` lists the steps. The release workflow builds the full package for Linux
x86_64 and aarch64, macOS on Apple silicon and Windows (Intel Macs: the command only); `scripts/package-full.sh` assembles one, and
`scripts/package-release.sh --full` builds an offline set for Linux x86_64. Releases from v1.1.0 on carry the full packages.

### Prebuilt binary, command only

```bash
curl -fsSL https://raw.githubusercontent.com/alexeyban/EKOS/main/install.sh | sh
```

Installs a single `ekos` binary into the EKOS home, `~/.ekos/bin` (RFC 0179), and creates
`~/.ekos/data`, where projects keep their config and compiled data. `EKOS_HOME` moves the home;
`EKOS_INSTALL_DIR` puts the binary somewhere else. An earlier install in `~/.local/bin` is
upgraded where it is. No Rust toolchain, no compiler, nothing else to install. The script resolves the latest release, verifies
the download against the release's `SHA256SUMS` **before** unpacking it, and never uses `sudo`.

Piping a script into a shell is a real supply-chain decision, so the script is short enough to
read first:

```bash
curl -fsSL https://raw.githubusercontent.com/alexeyban/EKOS/main/install.sh -o install.sh
less install.sh && sh install.sh
```

The script also takes `EKOS_VERSION` to pin a release (`EKOS_VERSION=v1.1.0 sh install.sh`) and
`EKOS_INSTALL_DIR` to change where it lands. To run EKOS as a shared service with the web
console, use the [container image](#container-image-rfc-0179) instead.

### Prebuilt binary, downloaded by hand

If you would rather not pipe a script into a shell, every release is a plain archive on the
[releases page](https://github.com/alexeyban/EKOS/releases). Pick the one for your machine:

| Your machine | Asset |
|---|---|
| Linux, Intel/AMD 64-bit | `ekos-<version>-x86_64-unknown-linux-gnu.tar.gz` |
| Linux, Intel/AMD, old or unusual distro | `ekos-<version>-x86_64-unknown-linux-musl.tar.gz` |
| Linux, ARM 64-bit (Raspberry Pi 4+, Graviton, Ampere) | `ekos-<version>-aarch64-unknown-linux-gnu.tar.gz` |
| macOS, Apple Silicon (M1 and later) | `ekos-<version>-aarch64-apple-darwin.tar.gz` |
| macOS, Intel | `ekos-<version>-x86_64-apple-darwin.tar.gz` |
| Windows, 64-bit | `ekos-<version>-x86_64-pc-windows-msvc.zip` |

`uname -sm` tells you which you are on if you are not sure: `Linux x86_64`, `Darwin arm64`, and
so on.

**glibc or musl?** Take the `gnu` build first — it is the faster of the two. If it refuses to
start with something like `version 'GLIBC_2.x' not found`, your distribution is older than the
one the release was built on: take the `musl` build instead, which is fully static and depends on
nothing. (`install.sh` does this fallback automatically.)

#### Linux and macOS

```bash
VERSION=v1.1.0
TARGET=x86_64-unknown-linux-gnu          # from the table above
ASSET="ekos-${VERSION#v}-$TARGET.tar.gz"
BASE="https://github.com/alexeyban/EKOS/releases/download/$VERSION"

curl -fsSLO "$BASE/$ASSET"
curl -fsSLO "$BASE/SHA256SUMS"

# Verify before unpacking. Feeding one line to -c keeps it quiet about the five assets
# you did not download, and works with both GNU sha256sum and macOS's shasum.
grep "$ASSET" SHA256SUMS | sha256sum -c -        # macOS: shasum -a 256 -c -

tar xzf "$ASSET"
mkdir -p ~/.local/bin                    # install(1) will not create it for you
install -m 755 "ekos-${VERSION#v}-$TARGET/ekos" ~/.local/bin/ekos
```

That prints `<asset>: OK` and exits 0. Anything else — `FAILED`, or nothing matched — means do
not unpack it; open an issue instead.

Worth being precise about what this proves: releases are checksummed but **not** signed — there
is no Sigstore/cosign signature or SLSA provenance yet. `SHA256SUMS` tells you the archive
arrived intact and matches what the release publishes; it does not, on its own, prove who built
it.

`~/.local/bin` needs to be on your `PATH`; add `export PATH="$HOME/.local/bin:$PATH"` to your
shell profile if `ekos --version` comes back "command not found". Any directory on `PATH` works —
`/usr/local/bin` needs `sudo`, which is the only reason it is not the default here.

**macOS, one extra step.** These binaries are not code-signed or notarised. A file downloaded
with a *browser* is quarantined by Gatekeeper and refuses to run ("cannot be opened because the
developer cannot be verified"). Clear the flag on the extracted binary:

```bash
xattr -d com.apple.quarantine ~/.local/bin/ekos
```

Downloading with `curl` — as above, and as `install.sh` does — does not set that flag, so this
step only applies if you clicked the link in a browser.

#### Windows

```powershell
$Version = "v1.1.0"
$Asset   = "ekos-$($Version -replace '^v','')-x86_64-pc-windows-msvc.zip"
$Base    = "https://github.com/alexeyban/EKOS/releases/download/$Version"

Invoke-WebRequest "$Base/$Asset" -OutFile $Asset
Invoke-WebRequest "$Base/SHA256SUMS" -OutFile SHA256SUMS

# Verify before unpacking.
$actual = (Get-FileHash $Asset -Algorithm SHA256).Hash.ToLower()
$line   = Select-String -Path SHA256SUMS -SimpleMatch $Asset
if (-not $line) { throw "$Asset is not listed in SHA256SUMS - do not use this file" }
$expected = $line.Line.Split()[0]
if ($actual -ne $expected) { throw "checksum mismatch - do not use this file" }

Expand-Archive $Asset -DestinationPath .
```

`ekos.exe` is inside the extracted folder. Move it somewhere on your `PATH`, or add that folder
to `PATH`. SmartScreen may warn the first time you run it, for the same reason as macOS: the
binary is unsigned.

(The Linux/macOS block above was run verbatim against the real v1.0.3 release. This PowerShell
one was not — no Windows machine was available — so treat it as carefully written rather than
proven, and please open an issue if it misbehaves.)

### Offline, from an install package

For a machine without internet access, or a build of a commit that is not released yet, build a
package on a Linux x86_64 machine with a checkout:

```bash
scripts/package-release.sh          # → dist/ekos-<version>-release.tar.gz
```

It builds `ekos` from the committed tree (uncommitted changes are left out) for glibc on the
host and fully static for musl in the pinned Rust image (needs Docker; `--no-musl` skips it),
packs both the way a release does with one `SHA256SUMS`, `install.sh` and an `INSTALL.md`, and
checks that the package installs. `<version>` is the tag on a tagged commit, otherwise
`<crate version>-dev.<commit>`. Copy that one file to the target machine, then:

```bash
tar xzf ekos-<version>-release.tar.gz && cd ekos-<version>-release
EKOS_VERSION=v<version> EKOS_BASE_URL="file://$PWD" sh install.sh
```

The installer verifies the archive and installs into `~/.ekos/bin` exactly as it does from a
release. `INSTALL.md` in the package covers installing by hand, the first run, agents, upgrading
and removing.

### First run

However you installed it:

```bash
ekos --version
cd /path/to/your/repo
ekos init --detect     # writes an ekos.toml that matches what's actually in this repository
ekos doctor
ekos build && ekos recover && ekos resolve && ekos compile && ekos commit
ekos coverage          # confirms every input kind actually produced objects
ekos ask "what does this system do?"
```

`ekos init --detect` is worth using rather than plain `ekos init`: it detects the SQL dialect your
schema is written in, excludes third-party and generated directories that would otherwise be
compiled as if they were your own code, and prints an inventory of what it found. See
[RFC 0152](ekos/docs/rfcs/0152-first-run-self-verification.md).

### Projects kept outside the sources (RFC 0178)

By default `ekos.toml` and the `.ekos/` state directory sit in the repository. A project in the
EKOS home keeps both elsewhere, so the sources are only read and one machine can hold many
projects, each with its own ledger:

```bash
ekos project add shop --source /path/to/your/repo --detect
ekos --project shop build && ekos --project shop recover && ekos --project shop resolve \
  && ekos --project shop compile && ekos --project shop commit
ekos --project shop ask "what does this system do?"
ekos project list
ekos mcp serve --project shop
```

```
~/.ekos/                          $EKOS_HOME, or --home
  data/<tenant>/<project>/
      ekos.toml                   [workspace] root = "/path/to/your/repo"
      state/                      what .ekos/ is for an in-place workspace
```

- `--project` works from any directory; `EKOS_PROJECT` and `EKOS_TENANT` do the same.
- The tenant is `default` unless `--tenant` names one. Two tenants may each have a project
  called `shop`; they share nothing.
- Nothing is written into the sources. Generated docs and dbt models default to the project's
  `out/` directory.
- `ekos project remove shop` moves the project's data to `~/.ekos/trash/`; `--purge --yes`
  deletes it.
- `ekos init` and `--config` are refused together with `--project`.

**Several repositories and folders in one project.** Name each input and they compile into one
ledger, so knowledge links across them and every object says where it is from:

```bash
ekos project add shop \
  --source api=/repos/payments-api --source web=/repos/storefront --source handbook=/srv/handbook
ekos --project shop source list
ekos --project shop build --source handbook      # re-observe one source only
ekos --project shop ekl "FIND Object WHERE source = 'handbook'"
```

- A file of the same name in two sources is two objects. Each object carries `source` (and
  `sources` when it was found in more than one).
- `ekos source add <name> --path <dir>` and `ekos source remove <name>` edit the project's
  `ekos.toml` and keep its comments. Removing a source does not remove compiled objects.
- A project already compiled without source names cannot gain them; create a new project.
- Sources are local directories and git repositories. Confluence and GitHub are still configured
  once per project.

Users, groups and roles are in the web console
([below](#tenants-users-and-roles-rfc-0180)). See
[RFC 0178](ekos/docs/rfcs/0178-ekos-home-projects-sources.md).

### Is the ledger still current? (RFC 0171)

The ledger describes the source as it was at the last `ekos commit`. `ekos build` records every
observed file's size and modification time, and a successful commit marks that list as "what the
ledger reflects". From then on EKOS compares it with the files on disk. It reads metadata only,
never file contents, and a file that was only touched also counts as changed. With `[freshness]
content-hash = true` (off by default) `ekos build` also records a content hash per file, and a file
whose time moved but whose bytes did not is no longer reported; files excluded as secrets are never
hashed.

```bash
ekos status            # … Source : fresh — ledger reflects the source as of 2026-10-09 12:35 UTC (git c4f01c7)
ekos freshness         # what changed since, and which compiled objects cite those files
```

```
Changed (1):
  schema.sql
    may be stale: File schema.sql, Table customers, Table orders
Removed (1):
  app.py
    may be stale: File app.py, PythonSymbol total
```

`ekos compile` and `ekos commit` warn `FRESH001` when the source moved after `ekos build`.
`ekos doctor` includes a "Source freshness" line. Over MCP, `ekos_status` carries a `freshness`
block, and when the source has changed every read tool's answer gets one extra note saying the
ledger may be behind, so an agent knows not to trust facts about those files. `[freshness] enabled
= false` turns all of this off; `ttl-seconds` (default 30) sets how long the MCP server reuses one
check.

### Upgrading and removing

Re-running the install command (or installing a newer package) replaces the binary in place with the latest release; there is no
package database and nothing else to update. To remove it, delete the binary
(`rm ~/.ekos/bin/ekos`, or `~/.local/bin/ekos` for an install made before RFC 0179). EKOS keeps
files in two places only: the `.ekos/` directory inside each workspace you compiled in place,
and the EKOS home (`~/.ekos`) for projects. Delete either separately.

### Container image (RFC 0179)

**Deploying for a team?** [docs/deployment.md](docs/deployment.md) is the step-by-step guide:
sign-in, tenants, roles, agents, model credentials, backups and upgrades.

One image holds the `ekos` binary, the console API and the built console UI, and serves both on
port 8000. All state is in one volume, the EKOS home. Sources are mounted read-only.

```bash
cp deploy/.env.example deploy/.env       # set EKOS_SOURCES and the two tokens
docker compose -f deploy/docker-compose.yml up -d --build
open http://127.0.0.1:8000
```

- `EKOS_SOURCES` is the host directory holding your repositories and document folders. It
  appears in the container as `/sources`.
- In the console, **Add a workspace → New project from a source directory** with a path such as
  `/sources/payments-api`. The project's config and compiled data go to the volume
  (`/var/lib/ekos/data/default/<project>/`); nothing is written into the source directory.
  Then run the pipeline from the project's Run tab.
- A project may only read directories under `/sources`, both when it is created and when its
  config is edited.
- The CLI is in the container too: `docker compose -f deploy/docker-compose.yml exec ekos ekos project list`.
  A project created that way appears in the console after a restart.
- The container runs as a non-root user and listens on loopback over plain HTTP. For access from
  other machines put a reverse proxy with TLS in front.
- A model server on the host (Ollama) is reachable from a project's `ekos.toml` as
  `http://host.docker.internal:11434`.

Tagged releases publish the image as `ghcr.io/alexeyban/ekos:<version>`; until the next tag,
build it from a checkout as above. See [RFC 0179](ekos/docs/rfcs/0179-installer-and-image.md).

### Tenants, users and roles (RFC 0180)

The console decides who may see and do what. The CLI is not affected: someone with a shell on
the machine already has the files.

- **Tenants.** Each tenant has its own projects and its own members. A project or tenant you
  have no role in answers 404, the same as one that does not exist.
- **Roles**, granted per tenant or per project in the console's **Admin** page:

  | Role | May |
  |---|---|
  | `viewer` | read everything in a project, including runs and logs |
  | `reviewer` | also decide business semantics and conflicts |
  | `operator` | also run commands, manage schedules, edit the project config |
  | `admin` | everything in the tenant: projects, members, groups, API tokens, audit log |

  A platform owner (named in `EKOS_CONSOLE_OWNERS`) can do everything, creates tenants, and sets
  which host directories each tenant's projects may read.
- **Sign-in** is OIDC. A role can be granted to an e-mail address before that person first signs
  in. A group can hold a role for its members, and can name a value of the provider's group
  claim so membership follows the provider.
- **API tokens** for agents and scripts (`Authorization: Bearer ekos_…`), created in the Admin
  page and shown once. A token can be `viewer` or `operator`. It can never review or administer:
  those need a signed-in person.
- **Audit log** per tenant: every request that changes something, and every refusal, with who
  and when.

```bash
# deploy/.env
EKOS_CONSOLE_OIDC_ISSUER=https://id.example.com/realms/main
EKOS_CONSOLE_OIDC_CLIENT_ID=ekos
EKOS_CONSOLE_OIDC_CLIENT_SECRET=...
EKOS_CONSOLE_OWNERS=you@example.com
EKOS_CONSOLE_SESSION_SECRET=...
EKOS_CONSOLE_PRODUCTION=true
```

With `EKOS_CONSOLE_PRODUCTION=true` the console refuses to start without OIDC, an owner and a
session secret, static tokens stop working, and access comes only from granted roles. Without it
the earlier behaviour remains for the `default` tenant: the two static tokens work (the write
token acts as a platform owner), and under OIDC every signed-in user can read `default`.

See [RFC 0180](ekos/docs/rfcs/0180-tenants-users-groups-roles.md).

### MCP for agents, through the console (RFC 0182)

An agent connects to a project through the console, with an API token:

```json
{"url": "https://ekos.example.com/mcp/default/shop",
 "headers": {"Authorization": "Bearer ekos_…"}}
```

`/mcp/<tenant>/<project>` speaks MCP Streamable HTTP, the same as `ekos mcp serve --http`. The
console sits in front of the project's own server and:

- lists only the tools the token's role allows. The two review tools need a signed-in reviewer,
  so no token ever sees them; `ekos_session_note` needs `operator`;
- attaches the token's read scope (RFC 0181) to every call. A scope the client sends itself is
  dropped;
- answers `404` for a project the token has no role in, the same as one that does not exist;
- records every call in the tenant's audit log: who, which tool, allowed or denied. Arguments
  are not recorded.

Projects' servers now start on first use. One unused for 15 minutes is stopped
(`EKOS_CONSOLE_MCP_IDLE_SECONDS`), and at most 8 run at once (`EKOS_CONSOLE_MCP_MAX_SERVERS`);
the first call after a stop waits for the server to start. Not built: OAuth for MCP clients and
rate limits. See [RFC 0182](ekos/docs/rfcs/0182-mcp-gateway.md).

### Backup, restore and model credentials (RFC 0183)

```bash
ekos home backup                       # every project, and the console's database
ekos --tenant acme home backup         # one tenant's projects
ekos home restore ekos-backup-20261013T101500Z.tar.zst
```

- A backup is one zstd-compressed tar under `<home>/backups/`. It holds each project's config
  and compiled data, not the sources (they are not in the home).
- A project is copied under its ledger's write lock: a pipeline stage that is writing makes the
  backup stop with that project's name, and no file is left. Readers are not affected.
- Restore replaces nothing that exists, and changes nothing if anything would be replaced. With
  `--force` each existing project is first moved to the home's trash. An archive with a path
  that would leave the home, or with a link in it, is refused.

In the console, a platform owner names for each tenant the environment variables holding its
model keys and switches metered calls on. A tenant's pipeline and MCP server then receive those
variables and no other tenant's, and none of the console's own settings. With the switch off
they receive none; a local model server still works. See
[RFC 0183](ekos/docs/rfcs/0183-operations.md).

### Console settings, local mode and the keychain (RFC 0184)

A platform owner changes the console's own settings on its **Settings** page: sign-in, owners,
MCP limits, ports. They are kept in `<EKOS_HOME>/control/console.toml`. An environment variable
wins over the file and shows on the page as read-only, so a container configured by
`deploy/.env` behaves as before. Changes apply at the next start (**Restart now** when a launcher
or a restart policy starts the console again).

Secrets typed on that page, and model keys for projects, go to the operating system's keychain
(Windows Credential Manager, macOS Keychain, Secret Service on Linux), never to a file or a
response. A key stored under a variable name (`ANTHROPIC_API_KEY`) reaches the commands of a
tenant granted that name while its metered calls are on, as an environment variable would. A
container has no keychain (`EKOS_CONSOLE_KEYCHAIN=off` in the image); keep secrets in its
environment.

**Local mode** (`mode = "local"`) is for one person on their own machine: no identity provider,
loopback only (a request from elsewhere, or naming another host, is refused), and the person who
can write the home's control directory signs in with a one-time code. That person is a platform
owner. The installer of RFC 0185 sets it up; see
[RFC 0184](ekos/docs/rfcs/0184-console-settings-local-mode-keychain.md).

### Every command and every setting from the console (RFC 0186)

A project's **Commands** tab lists every `ekos` command, read from the binary itself
(`ekos commands --json`), with a form built from its arguments and the exact command line shown
before it runs. Who may run what follows each command's class: reading needs a viewer, changing
the project an operator, a review decision a signed-in reviewer (recorded under their name, never
a token), and destructive commands or ones that reach a live system outside EKOS an admin who
types the command to confirm. Servers, the installer and the console's own commands are not run
from the web. The run's output lands in the run log like the pipeline's.

The project's config page has a **Settings** form for every section of `ekos.toml`, built from
the schema of the running binary (`ekos config schema --json`): types, defaults and the
documentation of each setting. Changes are applied to the file's text with its comments kept,
then validated and saved as before.

### Chat with a project (RFC 0187)

A project's **Chat** tab answers questions with a model that uses the project's EKOS tools: each
tool call is shown with its arguments and result, and the answer says which objects it rests
on. The model is set once by an owner (Settings → Chat, or in `ekos setup`): a local Ollama model,
any OpenAI-compatible server, or Anthropic. Its key is named by a variable whose value comes from
the environment or the OS keychain. A hosted model is paid per call, so it answers only in a
tenant whose metered calls an owner has turned on; a model on this machine always may.

The model is offered only tools that read, called with the person's own rights and read scope,
and every call is in the audit log. It never sees a review tool: review decisions stay with
people. Conversations are private to the person who started them.

### Access inside a project (RFC 0181)

A project is one ledger over several sources, so limits inside a project are applied when the
ledger is read. A viewer can be limited to part of one project, or have part of it hidden:

- **only** a source, or a path pattern in a source (`src/**`), or one object;
- **all except** a source, a path pattern (`secrets/**`), or an object.

In the Admin page, grant `viewer` on one workspace and choose "only…" or "all except…".

What a limited person gets:

- The graph, search, object pages, neighbourhoods and impact, filtered. A hidden object is not
  found, the same as one that does not exist. A relationship shows only when both its ends do.
  Counts cover only what is visible.
- Nothing else in that project: the dashboard, run history and logs, the configuration,
  semantics and conflicts answer 403. Those show more than the ledger (file names in a log, a
  freshness report), and nothing there could apply the limit.
- Anything the compiler could not attribute to a source is hidden from them: commit authors,
  crates, rollups, business-semantics items, conflicts.

Operators, admins and platform owners cannot be limited: running the pipeline shows every
source. A rule hides objects; it does not rewrite the text of a visible document that mentions
a hidden one.

The same filter is available from the command line, for `ekos mcp serve`, `ekos ekl` and
`ekos query`:

```bash
cat > scope.json <<'JSON'
{"default": "allow", "rules": [{"effect": "deny", "source": "payments-api", "path": "secrets/**"}]}
JSON
ekos --project shop --read-scope scope.json mcp serve
ekos --project shop --read-scope scope.json ekl "FIND Object WHERE kind = 'Table'"
```

Under a restricting scope the MCP server offers the tools that read only through the ledger
(`ekos_search`, `ekos_query`, `ekos_retrieve`, `ekos_ekl`, `ekos_neighborhood`, `ekos_state`,
`ekos_dependents`, `ekos_impact`, `ekos_diff`, `ekos_graph_export`) and refuses the rest. Any
other command refuses `--read-scope`. A local `ekos` run without a scope is unrestricted: that
user already has the files. See [RFC 0181](ekos/docs/rfcs/0181-read-scope.md).

### From source

**The Cargo workspace root is `ekos/`, not the repo root** — there is no top-level `Cargo.toml`,
so `cargo` commands must be run from inside `ekos/` (or with `--manifest-path ekos/Cargo.toml`).
The toolchain is pinned by `rust-toolchain.toml`; rustup installs the right version automatically.

Prerequisites on both platforms:
- **Rust**, stable channel, via [rustup](https://rustup.rs) — 2024 edition needs rustc 1.85+;
  installing the latest stable is fine.
- **A C/C++ toolchain** — `rusqlite`'s bundled SQLite and the `zstd` crate both compile native C
  source at build time, so a working `cc` is required even though the project itself is pure Rust.
- **Git**, to clone the repo.

#### macOS

```bash
# 1. C toolchain (skip if already installed)
xcode-select --install

# 2. Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

# 3. Clone and build (note: cd into ekos/, the actual workspace root)
git clone https://github.com/alexeyban/EKOS.git
cd EKOS/ekos
cargo build --release --workspace

# 4. Binary is at target/release/ekos — run it directly, or install onto PATH:
cargo install --path crates/cli
```

(Homebrew's `rustup-init` — `brew install rustup-init && rustup-init` — works the same way if you
prefer Homebrew-managed installs.)

#### Windows 11

Two supported paths — WSL2 is the path of least friction for a Unix-first Rust CLI project, since
it gives you a real Linux toolchain; native Windows works too and is fully supported by Rust.

**Option A — WSL2 (recommended):**

```powershell
wsl --install                       # if WSL2 isn't already set up; reboot if prompted
```

Then open the Ubuntu shell it installs and follow the **macOS/Linux steps above** (`xcode-select`
isn't applicable — `sudo apt install build-essential` gives you the C toolchain instead — then the
same `rustup.rs` install and `cargo build` commands).

**Option B — Native Windows:**

```powershell
# 1. C++ build tools (provides the MSVC linker rustc's default toolchain needs)
winget install Microsoft.VisualStudio.2022.BuildTools --override "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"

# 2. Rust (accept the default x86_64-pc-windows-msvc toolchain when prompted)
winget install Rustlang.Rustup

# 3. Git, if not already installed
winget install Git.Git

# 4. Clone and build (open a new terminal first, so the updated PATH takes effect)
git clone https://github.com/alexeyban/EKOS.git
cd EKOS\ekos
cargo build --release --workspace

# 5. Binary is at target\release\ekos.exe — run it directly, or install onto PATH:
cargo install --path crates\cli
```

#### Verify the install

```bash
ekos --help                # or: cargo run -p ekos -- --help, from ekos/
ekos init                  # creates .ekos/ in the current directory
cargo test --workspace     # optional: run the test suite (1,500+ tests)
```

See [`CLAUDE.md`](CLAUDE.md) for the full command reference and the mandatory development
workflow if you're planning to contribute.

### Legacy transformation recovery (RFC 0027/0028/0029)

A Pentaho step, a SQL `SELECT`, a `VIEW`, and a stored procedure are all the same underlying
concept — a transformation of data from sources to a sink through filter/join/aggregate/calculate
operations. `ekos recover` compiles all of them into one shared **Transformation IR**
(`Source`/`Filter`/`Join`/`Aggregate`/`Calculate`/`Sink`/`Unmapped`), so legacy ETL logic recovered
from a Pentaho `.ktr`/`.kjb` job can be diffed against a newly drafted SQL pipeline — no manual XML
reading required. `Unmapped` is deliberate, not a gap swept under the rug: anything that can't be
parsed is still recorded as evidenced fact ("something is here, not yet understood"), never
silently dropped.

### Oracle scripts, PL/SQL and schema history (RFC 0210)

An `oracle` SQL dialect reads Oracle schemas and SQL*Plus scripts: `SET`/`PROMPT`/`@file` lines and
whole PL/SQL units are set aside, Oracle-only clauses (`ENABLE NOVALIDATE`, `ADD (…)` column lists,
`MODIFY c DEFAULT x`, `VARCHAR2(10 BYTE)`, `FORCE` views, `(+)`, `MINUS`, physical attributes, …)
are rewritten — always keeping the file's line numbers. `ekos init --detect` adds one dialect rule
per engine-named directory, so a project shipping each migration for Oracle and for PostgreSQL reads
each copy with its own grammar, and the two copies are no longer reported as conflicting:
definitions are compared only within one dialect.

PL/SQL functions, procedures, triggers and packages are read into the same procedural IR as
PL/pgSQL and written as the same `Procedure` / `ProcedureStatement` objects, with a computed
fidelity label; an Oracle trigger's inline body is a `Procedure`, classified like any trigger
function. Migration scripts named `<yyyyMMddHHmm>_<description>.sql` become `SchemaChangeSet`s
(time, release, engine, tickets) holding one `SchemaChange` per operation — `add_column`,
`modify_column`, `add_constraint`, … — linked to their table at `ekos commit`.

On iDempiere `release-13`: Oracle migration statements rejected 5,317 → 9 (of 62,251); `db/oracle`
60 of 61 routines recovered completely (991 of 992 statements — the gap is a `GOTO`); 2,154 change
sets with 26,060 changes, none unrecognized; no model calls.

```bash
ekos recover   # … PL/SQL routines: …   Schema history: 2154 migration script(s), 26060 change(s) …
ekos ekl "FIND Object WHERE kind = 'SchemaChange' AND table = 'C_Invoice'"
```

### Live Oracle catalog and code ↔ database conflicts (RFC 0211)

A project can name an Oracle database next to its sources. `ekos build` reads its catalog through a
read-only session — `SET TRANSACTION READ ONLY`, a write probe that must be refused, settings pinned,
a call timeout — and checks that every kind it read matches the database's own object count, so a
user who cannot see some objects is an error, not a smaller answer. The password is never in the
file, only the name of the variable holding it:

```toml
[[databases]]
name = "erp-db"
kind = "oracle"
connect = "localhost:51521/XEPDB1"
user = "ekos_ro"
password-env = "EKOS_ORACLE_PASSWORD"
owners = ["ADEMPIERE"]
```

`ekos recover` turns the catalog into ordinary `Table`, `View` and `Procedure` objects marked
`origin: live` (routines go through the same PL/SQL reader as files); they never merge with tables
from scripts. `ekos commit` then compares the code's claims with the database and records each
disagreement as a conflict that cites both sides: a model table or column the database lacks, a
table no model describes, a mandatory model column that is nullable, a routine file whose text
differs from the installed one. When the source tree accounts for a difference — a migration newer
than the database, a translation table — the conflict carries that explanation.

`profile = "p0" | "p1" | "p2"` decides how much `ekos build` measures: optimizer statistics only
(the default), exact row counts, or one aggregate scan per table for exact null counts, number and
date bounds and text lengths. No tier stores a text value — a seeded marker row checks it — and
number and date bounds are withheld for columns named like personal data. A mandatory model column
that is nullable in the database then carries the count of rows that break the rule and the query
that re-counts them. The catalog also records the archive-log and supplemental-logging state.

On iDempiere (source `release-13`, the release 12 seed on Oracle XE): schema changes linked to their
table 11,748 → 28,916 of 31,620; 444 conflicts, 239 explained, every pending-migration explanation
confirmed against the database's own record of applied scripts. Among the rest: tables of modules
removed from the code but not the seed, a model column no script ever created, and an installed
procedure that builds `NVARCHAR2` columns where its file says `VARCHAR2`. At `profile = "p2"`
(903 tables in 6 s), of 116 mandatory-but-nullable columns 11 hold nulls and 105 none, each count
re-checked against the database. No model calls.

```bash
cargo build --release -p ekos --features oracle      # needs Oracle Instant Client at run time
ekos commit    # … Code ↔ database: 754 table(s) and 22 routine(s) compared … 239 of 444 explained …
ekos conflicts list --type model_column_missing
```

The testbed is `docker-compose.oracle.yml` + `deploy/fixtures/idempiere-oracle.sh`.


`ekos database add|list|test|remove` (RFC 0223) manage `[[databases]]` without editing `ekos.toml`; `ekos database
test <name>` connects read-only, checks a write is refused, and puts the census (tables, views, routines, triggers) next
to what was compiled. In the web console, a project's **Sources** tab does the same: add directories and databases (the
password goes to the server's keychain, never to `ekos.toml`), test, and analyse with Init & compile. On iDempiere,
from an empty project in a browser: census and compiled counts equal for every kind.
### Write behaviour: how each table is updated and deleted (RFC 0212)

Before copying a table incrementally you need to know whether every change moves its timestamp
column and whether rows ever disappear. `ekos commit` writes one `WriteBehaviour` per table with
both, each class citing where it came from:

- **update:** `po_only`, `raw_sql_sets_updated`, `raw_sql_skips_updated` (a raw `UPDATE` that leaves
  `Updated` alone — a watermark misses it), `no_updated_column`;
- **delete** (a set): `deleted_by_app` (a raw `DELETE` or a `PO` delete in code), `deleted_by_users`,
  `deleted_by_cascade`, `purged` (age-based or whole-table deletes), `soft_delete_only`,
  `never_deleted_in_code`;
- **change log:** whether the application records deletes of the table.

Users' deletes and change logging live in the application's dictionary, not its code; for
iDempiere-family schemas `[[databases]] dictionary = "idempiere"` reads those two flags of
`AD_Table` (opt-in). On iDempiere: 144 of 903 tables have a raw `UPDATE` that skips `Updated`, and
754 are deletable by users — something no source file says. No model calls.

```bash
ekos commit   # … Write behaviour: 903 table(s); update: po_only 737, raw_sql_skips_updated 144, …
ekos ekl "FIND Object WHERE kind = 'WriteBehaviour' AND update_class = 'raw_sql_skips_updated'"
```

### Tickets: commits, migrations and code joined by ticket key (RFC 0219)

Legacy estates cite their issue tracker in file names, comments and commit messages. With
`[tickets] keys = ["IDEMPIERE"]` (`ekos init --detect` proposes keys found in file names), every
ticket a commit names becomes a `Ticket` — its commits, dates, authors, a title taken from the first
commit's subject, and the files it touched — linked at `ekos commit` to the migration change sets
and code that cite it. A schema question then reaches when, why and who: on iDempiere,
`C_Country.ISOCountryCodeAlpha3` → change set `202412261358_IDEMPIERE-6349` → one commit,
2024-12-27, "Add M49 country codes to the C_Country table". Ticket ids are matched by exact key
only. `[observe] git-max-commits` raises the default of 500 commits read from history (the
iDempiere history has 16,260; read in full: 4,597 tickets).

```bash
ekos commit   # … Ticket links: 4597 ticket(s) from commits; linked to 272 JavaMethod, 154 JavaType, 3074 SchemaChangeSet …
ekos ekl "FIND Object WHERE kind = 'Ticket' AND name = 'IDEMPIERE-6349'"
```

### Run logs: every pipeline step as JSON lines (RFC 0220)

`build`, `recover`, `resolve`, `compile` and `commit` each write a JSON-lines run log next to their
usual output: one line per step with its counts (each connector scanned, each Oracle dictionary
query with rows and milliseconds, the reconciliation, a pass summary, analyzer stats, merges, facts
written), the warnings any part logged (redacted; the first 200, the rest counted), and two closing
lines — the model calls the command made, then its outcome. The file is `EKOS_RUN_LOG` when set,
otherwise `.ekos/runs/<timestamp>-<command>.jsonl`; the console sets it per run and shows the lines as
a steps table on the run page. On iDempiere every command logged zero model calls.

```
{"stage":"oracle.catalog","msg":"read DBA_TAB_COLUMNS","ms":687,"owner":"ADEMPIERE","query":"columns","rows":30457,"cmd":"build","t_ms":4889}
{"stage":"oracle.catalog","msg":"reconciled against DBA_OBJECTS","kinds":13,"mismatches":0,"objects":10613,"owner":"ADEMPIERE","cmd":"build","t_ms":8985}
{"stage":"llm","msg":"calls","count":0,"cache_hits":0,"embeddings":0,"cmd":"build","t_ms":19987}
{"stage":"run","msg":"finished","ok":true,"ms":19987,"warnings":0,"cmd":"build","t_ms":19987}
```

### Documentation repositories and wiki snapshots (RFC 0221)

A documentation site kept as Markdown (Docusaurus, MkDocs, a `docs/` folder) is a source like code: add it to a
project's `[[sources]]`. Front matter becomes the document's properties (`title`, `description`, and for a wiki
snapshot `source_url`, `source_revision`, `licence`) instead of the text of a section, and each section records the
tickets it names, so `ekos commit` links a ticket to the docs pages that describe it as well as to the commits,
migrations and code. On iDempiere (code + docs repository): 1,743 docs sections linked to tickets, e.g.
`C_Country.ISOCountryCodeAlpha3` → change set `202412261358_IDEMPIERE-6349` → `IDEMPIERE-6349` → the page "New
Fields in Country".

`scripts/wiki-snapshot.py` turns MediaWiki pages into such a directory — from a `Special:Export` file saved in a
browser, or from the API (one request a second; it stops at a 403 or a bot challenge rather than working around
it). Each page keeps its URL, revision id and licence. Snapshots are for analysis; check the licence before
republishing anything derived from them.

```bash
scripts/wiki-snapshot.py --xml export.xml --out ~/wiki-snapshot --licence "CC BY-SA 4.0"
ekos source add wiki --path ~/wiki-snapshot
```

### Review and sign-off (RFC 0213)

Before a lakehouse is built from a source estate, a person agrees to its source model. `ekos review list` shows six
subjects — the tables in scope (classed by name: `T_*` transient, `I_*` import, `*_Trl` translation, `*Log*` log,
`AD_*` config; `[review.scope]` adds rules), PII candidates, code ↔ database conflicts, identity matches, each table's
write behaviour, and the glossary — with what is decided and what still blocks. Decide items with `ekos review scope`,
`ekos review pii` and `ekos review write-behaviour` (conflicts, identity and glossary keep their own commands), then
sign a subject off on the digest you were shown:

```bash
ekos review show pii --undecided
ekos review pii C_BPARTNER.EMAIL --confirm --mask hash
ekos signoff show pii                      # prints the digest
ekos signoff approve pii --digest <digest>
```

A sign-off is valid only while the facts it covered are unchanged; after a compile that changes one, `signoff show`
says **stale** and names the items added, removed or changed. Row and null counts are shown but not signed, so a fresh
profile alone does not invalidate anything. Decisions and sign-offs are human-only: no MCP tool can make them.

`ekos workflow status [--json]` is the step bar of the seven-step operator workflow (analyse, documentation, review
and sign-off, requirements, extraction, bronze/silver, marts): step 1 from source freshness, step 3 from the six
subjects' sign-offs, the others from an extension such as ekos-lakehouse. Steps 4–7 show `blocked` until every subject
is validly signed, and an extension's step commands call the same gate before writing anything. Agents read the same
state, without being able to change it, through the `ekos_signoff_status` MCP tool. The subject summary is cached
beside the ledger under a key that every write moves (iDempiere: 24.5 s to compute, 1.8 s cached).

In the web console, every project page shows the step bar, and the **Review** tab has one tab per subject: a filterable
table of items (signed facts and shown-only measurements apart), decisions for selected items (scope, PII with a mask,
write behaviour, identity matches — `ekos review identity` on the CLI), and a sign-off box that shows the digest and
what changed since a stale sign-off and signs only after the subject's name is typed. Conflicts and the glossary are
decided on their own tabs. Deciding and signing need the reviewer role; no API token holds it.

### Source-estate documentation (RFC 0214)

`ekos docs generate --layout estate --output docs/estate` writes a database estate's documentation from the ledger:
functional areas with ER diagrams, one page per in-scope table (columns with business names, the database's foreign
keys next to the application model's references, check constraints, who reads and writes it, write behaviour, schema
history, open conflicts), a glossary of business terms, where each document type's `DocAction` methods start,
routines with their nested statements, schema history by release, and findings. The pages use the lakehouse-docs page
format, so `publish_github_wiki.py`, `publish_confluence.py` and `publish_azure_devops_wiki.py` publish them; manual
"notes" sections survive regeneration. Tables follow the review's scope (RFC 0213). Two gates are built in: a column
profile contributes counts only, never a value, and text is used only from sources with a known licence (detected from
a source's `LICENSE` file, or set in `[docs-estate] licences`; a database has none until you set one). On iDempiere:
1,060 pages in 26 s — published with a walkthrough of the first three workflow steps at
[alexeyban/ekos-lakehouse-oracle](https://github.com/alexeyban/ekos-lakehouse-oracle).

### iDempiere eval (RFC 0222)

`evals/idempiere/` holds 25 checked questions about iDempiere (code, schema, history, docs, write behaviour, and six
with no grounded answer), graded with `ekos eval run --datasets-dir evals/idempiere --dataset idempiere-25`. Add
`--evidence-only` to grade retrieval without calling a model. First results (code + docs, with and without the
Oracle database, answers by Claude Haiku 5.5): 14 and 15 of 25 passed, no hallucination, about 2 US cents a run;
the nine misses are retrieval, mostly documentation prose outranking the code that implements an answer.

### PL/pgSQL stored procedures (RFC 0163)

A stored procedure is also *imperative* — ordered statements, branches, loops, exception handlers —
which a dataflow IR cannot hold without losing the order. For every `.sql` file resolved to the
`postgres` dialect (or that names `plpgsql`), `ekos recover` parses each routine with a
deterministic, in-process PL/pgSQL parser (no database, no LLM) and writes:

- one `Procedure` object per routine — signature, language, and a **fidelity label computed from
  the parse**: `statements` (every statement recovered), `partial` (with the exact counts and the
  lines of what was missed), or `signature` (a `LANGUAGE sql`/`c` routine whose body is not parsed);
- one `ProcedureStatement` per statement at every depth, whose evidence is its own source text and
  line, linked by `Contains` edges that record which branch each child sits in (`then:0`, `else`,
  `handler:1`, …).

```bash
ekos recover   # … PL/pgSQL routines: 556 (254 plpgsql: 251 complete, 3 partial), 1556 statements
ekos commit    # … Procedure links: 1852 new (409 reads, 308 writes, 989 depends-on, 146 calls …)
ekos ekl "FIND Object WHERE kind = 'Procedure' AND name = 'payment_post'"
```

On LedgerSMB every routine its `LOADORDER` installs recovers completely (212/212); the three
`partial` routines above are in a module LedgerSMB itself does not load, and are invalid PL/pgSQL.

Each statement's embedded SQL (and each condition, assignment and loop bound) is parsed as real
PostgreSQL, so every `ProcedureStatement` and `Procedure` records the tables it **reads**, the tables
it **writes** and the functions it **calls** — `LANGUAGE sql` routines included. `ekos commit` then
links them across the whole workspace: `ReadsFrom`/`WritesTo` per statement, `DependsOn` from the
routine to each table (with `access: read | write | read_write`), and `Calls` between routines — so
"what breaks if I change `acc_trans`" now names the 50 LedgerSMB routines that touch it. A name links
only when it names exactly one object; an overloaded or redefined routine or view, a temp table or
a system catalog links nothing rather than something guessed.

### Triggers (RFC 0163)

Every `CREATE [CONSTRAINT] TRIGGER` becomes a `Trigger` object — timing, events (with `UPDATE OF`
columns), level, `WHEN` condition and function — linked to the table it fires on (`DependsOn`, so
impact analysis on a table finds its triggers) and to its function. Each is **classified from what
its function actually does**, read from the recovered IR, never from names: `Validation` (raises or
drops the row), `DerivedColumn` (sets `NEW` columns), `Audit` (only inserts elsewhere), `Cascade`
(updates/deletes elsewhere), `Mixed` (several of those, dynamic SQL, or calls whose effects are not
inlined — a human decides) or `Unknown` (the function body is not recovered). Every class carries its
reasons. A function redefined across migrations is classified per definition and only gets a class
when they all agree; `RETURN NEW` placeholders are set aside, and the reasons say so. Triggers are
never auto-translated.

```bash
ekos recover   # … Triggers: 42 (42 parsed, 0 read from tokens) — classified at compile
```

### Views (RFC 0169)

Every `CREATE [OR REPLACE] [MATERIALIZED] VIEW` in an observed `.sql` file is a `View` object — its
declared columns, whether it is materialized, its exact source text and line, and what its query
reads and calls, from a real parse. Each definition is parsed on its own, so a view using syntax the
parser lacks is still recorded (`footprint: unparsed`, with the reason) and never takes its file down.
Views are linked like routines: a view `DependsOn` the tables and views its query reads, routines and
transformations that read a view link to it, and impact analysis on a table now reaches the views
built on it.

Routines and views are documented like code: `docs generate --layout curated` writes a page for
each (the author's `COMMENT ON FUNCTION|VIEW` text as its description, its lines, what it reads,
writes and calls, and who uses it), lists views among the Data Stores with the routines that use
them, and lists routines in API.md under their file. `[llm-description]` describes them from their
real source like any other symbol, and a backticked routine or view name in a doc links to it.

```bash
ekos recover   # … Views: 17 (17 parsed, 0 unparsed — still recorded)
ekos ekl "FIND Object WHERE kind = 'View'"
```

### Business semantics → LinkML (RFC 0170, experimental, opt-in)

Business meaning that nobody wrote down survives as traces: `WHERE NOT p.obsolete`,
`entity_class = 2`, the lookup row `(2, 'Customer')`, `COMMENT ON COLUMN account.category IS
'A=asset,L=liability,…'`, the commit that last changed the line. Recovery records every
column-vs-literal predicate in views, routines and `CHECK` constraints — normalized, so
`status IN (1,3)` and `status = 1 OR 3 = status` are one predicate — plus `CHECK` constraints,
`NOT NULL`/key columns and lookup-table seed rows — plus PL/pgSQL `IF NEW.col …` conditions
(resolved to the trigger's table), Pentaho `FilterRows` conditions, standalone analyst `SELECT`s,
and dbt `schema.yml` (descriptions, `not_null`/`unique`/`accepted_values`/`relationships` tests)
and model SQL (Jinja rendered: `ref`/`source`/`var`; model columns traced back to their source
columns) — plus SQL in Perl strings, application constants (Perl `use constant EC_CUSTOMER => 2`,
Python `Enum` classes; matched to columns by label agreement or name) and marked glossaries (local
docs, Confluence; unmatched terms become gaps). Filters through CTEs and derived tables are
restated on the base table. `[semantics] ontology = "<file>"` adds exact/close
mapping suggestions from your own vocabulary, exported as annotations only. With `[semantics] enabled = true`, `ekos commit`
synthesizes **hypotheses** from them, deterministically and without an LLM:

| Kind | What |
|---|---|
| `BusinessConcept` | A filter that defines a view, or recurs in ≥ `min-sites` routines/views (`PartsNotObsolete`, `EntityCreditAccountCustomer`) |
| `EnumMeaning` | A coded value and its meaning, from a column comment legend, a lookup seed row via its foreign key, or a `CASE` label |
| `ConstraintCandidate` | A `CHECK` constraint, typed `range`/`enum`/`pattern`/`not_null`/`other` |
| `SemanticGap` | A coded value used in logic that no source explains; a concept nobody documented |
| (opt-in) AI summary | `[semantics] llm-definitions = true`: ≤2 sentences per undocumented concept, every sentence citing the concept's evidence (or the known code meanings) — uncited or hedging sentences are dropped; a reading aid, never the definition |
| `RationaleLink` | `git blame -w` on the evidence lines → the commit that last changed them |

Every item starts as `status: hypothesis` with its evidence (`path:line`). Only a human promotes
one — `ekos semantics confirm|reject|edit` is CLI-only and no MCP tool can reach it. A review holds
while what the item asserts and its evidence are unchanged (line moves don't count); otherwise the
item becomes `needs_review`, and a confirmed item whose traces disappear is flagged, not dropped.
Same-column threshold disagreements (`> 90` here, `> 60` there) become `ConceptConflict`s.
The web console's **Semantics** tab is the review UI: a queue with evidence and bulk
confirm/reject, and a LinkML viewer and YAML editor (with a side-by-side diff against the current
export) whose edits round-trip through `ekos import linkml` (see *Web console* below).

Agents read them over MCP — `ekos_semantics_lookup` (what a term, table, column or code means)
and `ekos_semantics_gaps` (what is not known), listed when `[semantics]` is on. Every result
states its status in words ("CONFIRMED by a human reviewer…", "HYPOTHESIS — … say so if you use
it"); rejected definitions are left out; an empty lookup says `no_semantics_found` so an agent
does not improvise. No MCP tool can confirm anything. The export is a **draft LinkML schema** — EKOS feeds LinkML, LinkML
generates everything else (JSON Schema, Pydantic, RDF/OWL/SHACL):

```bash
ekos semantics list [--kind concept|enum|constraint|gap|rationale]
ekos semantics show PartsNotObsolete        # definition, evidence lines, links, commits
ekos semantics gaps                         # open questions, conflicts, and the needs_review queue
ekos semantics confirm TransactionsNotApproved --note "drafts"     # human-only (--as, default $USER)
ekos semantics edit PartsWithInventoryAccnoId --name "Inventory part" --description "…"
ekos semantics reject UserPreferenceWithoutUserId --note "anti-join plumbing"
ekos export linkml --out model.yaml          # confirmed only; --status hypothesis|all for the draft
ekos import linkml model.yaml --dry-run      # an expert's YAML edits → the review decisions they mean
ekos import linkml model.yaml --as ann       # …recorded, all or nothing (renames, descriptions,
                                             # code labels, ekos_status: confirmed|rejected)
ekos semantics confirm PartsAssembly PartsNotObsolete --as ann   # many at once, all or nothing
ekos semantics gold-template --out gold.yaml   # blank, structure-only: for an expert, before any output
ekos semantics eval --gold gold.yaml        # concept recall, label accuracy, gap recall, evidence validity
```

A runnable end-to-end example — clone LedgerSMB, compile, review, export, then lint, generate
and validate with LinkML's own tools — is [`demo/ledgersmb-linkml/`](demo/ledgersmb-linkml/README.md).

On LedgerSMB (SQL + Perl + UI + git, no LLM): 649 predicate sites (458 resolved to a
table column), 47 concepts, 222 coded values (179 with a meaning), 0 identity conflicts in
`resolve`; an unchanged re-commit writes nothing. The LinkML file passes `linkml-lint` with 0 errors and
`gen-json-schema`/`gen-pydantic` run cleanly. Against a *starter* gold set (not expert-written —
see `ekos/docs/rfcs/0170-ledgersmb-starter-gold.yaml`): concept recall 0.68, enum label accuracy
0.95, evidence validity 1.0. Meaning defined only by comparisons between columns or against the
current date (overdue, unpaid) leaves no literal trace and is not recovered: no trace, no recovery.

### dbt metadata extraction (RFC 0117)

dbt can point at any warehouse, so `ekos recover` extracts real `Table` objects from a dbt
project's own checked-in metadata rather than a live database connection — never `manifest.json`/
`catalog.json` either, since both are `dbt/target/` build artifacts, gitignored in every real
project inspected while designing this. One `Table` per `models/**/*.sql` file (a model exists the
moment its `.sql` file does, regardless of whether any YAML documents it) and one per declared
`sources[].tables[]` entry (no `.sql` file backs a source — it's a pre-existing table dbt only
references). `ref()`/`source()` macro calls in each model's raw SQL become real `DependsOn`
relationships, resolved against the models/sources found in that same dbt project; an unresolvable
reference (e.g. into an installed, gitignored `dbt_packages/`) is honestly skipped, never
fabricated. Declared `schema.yml` columns are merged in as-is — explicitly partial, since dbt
projects typically only document tested/described columns, not every column a model produces.

The same real-world entity observed under different names across systems (Informix `cust_mstr`,
Postgres `customers`, Databricks `gold.dim_customer`) can be linked too: `ekos identity scan`
scores candidate cross-system matches (column overlap, naming-pattern similarity, type
compatibility) and writes them as `unconfirmed` relationships — never a silent auto-merge — for
review via the `ekos_identity_review` MCP tool (optional `reviewer` and `note`, recorded on the
decision's evidence). Treasury payment authorizations (`ekos treasury scan`, RFC 0032) are
different: a person confirms or rejects each with `ekos treasury confirm|reject <id>` (`reject`
needs `--note`); no MCP tool can.

Same-source duplicates (`ekos resolve`/`ekos
compile`, e.g. two `Table` objects both literally named `customers`) auto-merge only when the
match is an exact normalized name; anything fuzzy goes through that same `unconfirmed`/review
flow instead of an irreversible merge (RFC 0063) — no confidence threshold on the underlying
scoring formula reliably separates real correct fuzzy merges from real incorrect ones, so an
irreversible auto-merge isn't a safe default for that case.

A same-name group spread over separate namespaces is not a conflict: a Perl package
`LedgerSMB::GL` beside a table `gl`, or a JS and a Perl `initialize`. `resolve` accepts a group
spanning the database (`Table`/`View`/`Procedure`/`Trigger`) and the code of Perl, JS, Python,
Rust or Elixir when each namespace's share is unremarkable on its own; a `Table` beside a
same-named `View` still conflicts (RFC 0147 amendment b — LedgerSMB 16 → 0 conflicts).

**When sources disagree, both claims are kept (RFC 0172).** A table created in two files with
different columns, a column type an exact-name merge would have dropped, two labels for one code
from different sources — each becomes a `ConflictingEvidence` item instead of the last one silently
winning: every claim with its file and line, what EKOS kept, and a `Disputes` link to the object.
Values are normalized first (`INT`/`INTEGER`/`SERIAL` are one type), a fact only one side states is
unknown rather than a disagreement, and prose is never compared.

```bash
ekos conflicts list
#   [open] account.category = 'A'.label  — 2 source(s) disagree: "asset"  vs  "L"
#   [open] user_preference.columns  — 2 source(s) disagree: ["dateformat","id",…]  vs  ["id","name","user_id","value"]
ekos conflicts show "account.category = 'A'.label"   # each claim's path:line and source
ekos conflicts resolve user_preference.columns --both-valid --note "1.9 replaces the table"  # human-only
ekos conflicts resolve "account.category = 'A'.label" --pick 1 --as ann
```

A decision holds while the claims are unchanged; when one changes, the conflict reopens with the old
decision kept. Agents read conflicts over MCP (`ekos_conflicts`, and `open_conflicts` on
`ekos_state`) and are told to present an open one as a disagreement, never one side as fact; no MCP
tool can resolve one. Answers say so too (RFC 0173): an `ekos_query` / `ekos_retrieve` claim about an
attribute with an open conflict carries `disputed: true` and the conflict ids, since its value is
only the side EKOS kept, and `ekos ask` tells the model the same in the evidence it reads. A label
conflict is also linked to the table its column belongs to, so a question about the table surfaces
it. The web console's **Conflicts** tab lists every conflict with each claim's file and line, lets a
write-role user pick the right claim or mark both valid, and the graph rings objects with an open
conflict (RFC 0174). On LedgerSMB: 3 conflicts — `user_preference` (re-created by a 1.9 migration)
and 2 order-class labels where an API query names the counterparty (`customer`) rather than the
order type. The detector first surfaced a CASE that swaps `'A'`↔`'L'` misread as a label; the
extractor no longer reads a rewrite as a meaning. `[conflicts]
enabled = false` restores the old behaviour.

### Real schema and class structure from source (RFC 0091/0092)

**File-based SQL schema needs a dialect.** `.sql` files parse under the `generic` (ANSI) dialect
unless `ekos.toml` routes them somewhere real:

```toml
[recover.sql]
default-dialect = "generic"

[[recover.sql.dialect-rules]]           # first path-glob match wins
path-glob = "priv/repo/**"
dialect = "postgres"
[[recover.sql.dialect-rules]]
path-glob = "priv/ingest_repo/**"
dialect = "clickhouse"
```

This matters for any real schema **dump** — `pg_dump` output, a ClickHouse `structure.sql`, or
hand-written DDL past plain ANSI. The `postgres` / `clickhouse` dialects carry the preprocessing
(RFC 0057/0058/0059) that makes real dumps parse; `generic` does not.

A statement the dialect cannot parse costs that statement, not the file (RFC 0176). The rest of
the file is still recovered, and `ekos recover` says what was skipped:

- `SQL005` — `<file>: 2 of 61 statements were not parsed and skipped`, with the line, the first
  words and the parser's error for each. A skipped `CREATE TABLE` is called out as a lost table.
- `SQL001` — when a file states a `CREATE TABLE` and no table was recovered, the message names the
  dialect it was parsed under and the first error, and points at `[[recover.sql.dialect-rules]]`.
  A file with no `CREATE TABLE` keeps the plain `no tables found`.

If `ekos ekl "FIND Object WHERE kind = 'Table' COUNT"` returns 0 for a repo that clearly has a
schema, read those two warnings first. Foreign keys declared after the tables, as `pg_dump` writes
them (`ALTER TABLE … ADD CONSTRAINT … FOREIGN KEY`), become `ForeignKey` edges too.

**Hand-written schemas need more than the right dialect (RFC 0146).** Everything above was tuned
against `pg_dump`, which emits a narrow, mechanical subset of PostgreSQL. A human-maintained schema
does not: measured on LedgerSMB, a correctly-configured `dialect = "postgres"` still recovered
**0 of 158 tables**, because the file's first `COMMENT ON TABLE … IS $$…$$` failed the whole-file
parse and took every table with it. The `postgres` dialect now preprocesses `COMMENT ON`,
`INHERITS`, `SECURITY DEFINER`, `RETURNS SETOF`, `:=` named arguments, `DO` blocks, `CREATE RULE`,
psql meta-commands and `COPY … FROM stdin` payloads out of the way; the same file yields 158 tables
and 214 foreign keys.

`COMMENT ON TABLE` / `COMMENT ON COLUMN` text is no longer discarded either — it becomes an
evidence-backed `description` on the `Table` object (and on the matching column), with the source
line recorded. **Author-written text outranks the LLM's:** `description` is the schema's own words,
the model's version is kept alongside as `llm_description`, and `sql_comment` marks the provenance.

`[llm] max-tokens` caps compiler-pass LLM calls — distinct from `[ai] max-tokens`, which governs the
read-side `ekos ask` runtime. Leave it unset and each file's budget is computed from its own schema
size; a new `SQL004` diagnostic reports when enrichment named fewer tables than the file declares,
and says so explicitly when the response hit its ceiling.

Beyond raw SQL DDL, `ekos recover`'s Python analyzer recognizes a real SQLAlchemy declarative
model (`__tablename__` present on a class) and compiles it into the same `Table` object shape as a
`CREATE TABLE` statement — real column names, best-effort data-type hints, and `ForeignKey` edges
resolved against other models in the same file — so a project whose entire schema is ORM-declared
(the majority shape for a modern Python backend) still gets a real `## Data Architecture` and
entity-relationship diagram instead of an empty section. The same analyzer also compiles real
class inheritance (`class Document(Base):`) into `RelationshipKind::Extends` edges between the
real `PythonSymbol` objects involved — visible on each class's own generated page and in its
Mermaid diagram — resolved only when the base class is defined in the same file, never fabricated
against an imported base EKOS can't see the definition of.

### Document semantic memory (RFC 0025/0026)

Beyond structural parsing, an opt-in pass reads local documents through an LLM to extract real
entities (`Concept` objects) and the relationships between them — so the same concept mentioned
across different documents becomes one findable, linkable thing instead of isolated text hits.
Enable it in `ekos.toml`:

```toml
[llm]
provider = "ollama"   # or omit for Anthropic via ANTHROPIC_API_KEY; any LlmProvider works

[document-semantics]
enabled = true
```

Then `ekos recover` runs `DocumentSemanticsAnalyzerPass` alongside the structural document pass,
and the extracted `Concept` objects are queryable through the same MCP tools as everything else
— `ekos_search`, `ekos_neighborhood`, `ekos_dependents`, `ekos ask`. No new tool, no new query
surface — this is exactly the point: AI tools get real memory through the Runtime they already
talk to. `ekos ask` honors `[llm] provider = "ollama"` the same way `ekos recover` does — both
commands select the LLM provider through one shared function, so a workspace configured for local
Ollama works identically for recovery and for querying.

**Markdown is split by heading (RFC 0144).** Each heading becomes its own searchable `Section` named by
its heading path (`docs/rfcs/0013-mcp-server.md § RFC 0013 — MCP Server › Motivation`) with a real
line range, `doc_type` (`rfc`/`devlog`/`readme`/`claude_md`/`doc`) and, for RFCs, `rfc_number`/`rfc_status`.
`compile` also links docs deterministically: an `RFC NNNN` mention becomes a `References` edge to that RFC,
and a backticked identifier that names exactly one code symbol becomes an edge to it. `ekos ask "what does
RFC 0013 …"` resolves the RFC by number. These edges show up in neighbourhoods but never count as
dependents in `ekos_dependents`/`ekos_impact`.

**Using a hosted OpenAI-compatible model (RFC 0145).** Any Chat Completions host works — OpenCode Zen,
OpenRouter, DeepSeek, Groq, vLLM:

```toml
[llm]
provider = "openai"
base-url = "https://opencode.ai/zen/v1"
model = "deepseek-v4-flash"
api-key-env = "OPENCODE_API_KEY"

[ai]
max-tokens = 8192            # reasoning models spend hidden tokens; 1024/2048 truncate or empty answers
```

**A model per task (RFC 0197).** `provider = "zen"` reaches every OpenCode Zen model on its own wire
format (Claude and Qwen Flash on Messages, GPT/Grok on Responses, the rest on Chat Completions), and
`[llm.tasks.<task>]` routes one kind of call to its own model — tasks: `ask`, `doc-semantics`,
`description`, `semantics`, `sql-naming`, `session-capture`, `architecture`, `reconstruct`,
`nl-sql`, `docs-prose`, `marketing`. Measured on this repository (RFC 0197's tables):

```toml
[llm]
provider = "zen"
model = "claude-haiku-5-5"   # ask: 98/101 for $0.10 a full eval run
api-key-env = "OPENCODE_API_KEY"
budget-usd = 1.00            # refuse a call whose worst case could cross this, per command

[llm.tasks.doc-semantics]
model = "gpt-6-luna"         # 40/40 sections parsed; deepseek-v4.1-flash parsed 4/33 at the old cap
max-tokens = 4096
fallback = ["claude-haiku-5-5"]
```

Every call that reaches a host is priced and logged (metadata only) to `.ekos/llm-usage.jsonl`:
`ekos llm usage` totals it, `ekos llm routes` shows each task's model and price, `ekos llm probe`
sends a few-token request per model to show which ones a key can reach (access is per account on
Zen). Models whose provider may keep requests are refused unless `[llm] allow-data-collection = true`;
Zen's free models are not reachable outside OpenCode.

For local Ollama, `[llm] context-window = 8192` (the default; also `OLLAMA_NUM_CTX`) is sent as `num_ctx` —
without it Ollama silently truncated long prompts — and EKOS warns when a prompt fills the window.
`ekos doctor` shows the effective window or custom endpoint. Hosted models bill per token; a full
101-scenario `ekos eval run` on DeepSeek V4 Flash costs about $0.08. `ekos eval run --evidence-only`
calls no model: it reports Recall@10 and whether each scenario's expected facts reach the evidence. DeepSeek V4 Flash is a reasoning model whose
hidden reasoning counts against `max-tokens` — use `[ai] max-tokens = 8192` or some answers come back empty.

### Documentation generation (RFC 0035/0037/0042/0090/0094/0095)

`ekos docs generate` renders the compiled ledger straight into Markdown/HTML documentation —
zero LLM calls, every claim traceable to real compiled evidence. Three layouts:

```bash
ekos docs generate                              # --layout objects (default): one page per
                                                  # significant object, plus an index and ER diagram
ekos docs generate --layout curated --output doc # README.md/Architecture.md/API.md/
                                                  # SequenceDiagrams.md — the shape a developer
                                                  # actually expects, plus one detail page per
                                                  # crate/technology/pipeline/program-entity object
ekos docs generate --layout solution-architect --output doc-sa
                                                  # DependencyRiskReport.md/OnboardingGuide.md/
                                                  # FindingsMemo.md — a team-handoff bundle: real
                                                  # declared dependency versions and concentration
                                                  # risk, a first-day repository-layout guide, and
                                                  # an actionable findings list (unresolved
                                                  # dependencies, undeclared crate versions, missing
                                                  # doc-comment coverage). `--prose` layers an
                                                  # LLM-written executive summary on the findings
                                                  # list, never replacing the deterministic list
                                                  # underneath it.
```

`--layout curated`'s `Architecture.md` includes a real crate/workspace dependency graph (parsed
`Cargo.toml`, not guessed, annotated with a C4 mapping — crate → Container, external dependency →
External System, RFC 0065), external technology dependencies, an `## Open Questions` section
listing real knowledge gaps a deterministic pass couldn't resolve (e.g. an unresolvable workspace
dependency) rather than dropping them silently, CI/CD pipelines (parsed `.github/workflows/*.yml`),
and an entity-relationship diagram; `API.md` lists real functions/
structs/enums/traits (from `RustSymbol`/`PythonSymbol` objects, RFC 0038/0040/0041) grouped by
file, each linked to its own detail page; `SequenceDiagrams.md` covers both Transformation-IR
data-flow sequences and real function-call sequences (RFC 0041's `Calls` graph). Per-entity pages
nest under `entities/<kind>/<2-char shard>/` so a large codebase's page count never blows past
GitHub's per-directory file-listing cap — running `ekos docs generate --layout curated --output
doc` against this repo's own source is a ready example to try. Each entity page's Definition
section now shows the real human-written documentation from source when the analyzer found any
(`///` doc comments, Python docstrings, `@moduledoc`/`@doc`, JSDoc — RFC 0087), honestly stating
"Not documented in source" rather than fabricating one when it didn't. `--prose` (opt-in) layers an LLM-written overview onto each
object page, reusing `ekos ask`'s exact grounding+citation pipeline, with a token-cost estimate
shown before any call.

`Architecture.md`'s Executive Summary now surfaces two more real, deterministic signals instead of
placeholder text: **Major risks** lists real "Observed Concentration Risk" objects — any object
with 3 or more real compiled `DependsOn` dependents, a structural single-point-of-failure
candidate, never an LLM-guessed severity score (RFC 0094) — and **Architecture confidence** shows
the same real completeness/evidence-coverage score `ekos architecture investigate` computes (RFC
0065 Phase 3), now also run from the plain `docs generate` path instead of only the investigation
loop (RFC 0095). Both say so honestly when there's no real signal to compute from yet, rather than
showing a misleading 100%.

### Architecture reasoning + investigation loop (RFC 0065/0066/0067, opt-in)

Beyond deterministic extraction, `ekos architecture investigate` runs the RFC 0066 MVP agentic
loop: broad collection, deterministic crate-topology extraction, one batched LLM call classifying
each crate's architectural role (`ArchitectureReasoningPass`, RFC 0065 Phase 2), a deterministic
evaluator scoring completeness and evidence coverage (no LLM — RFC 0065 Phase 3), and — for any
crate the evaluator flags unclassified — a targeted second pass that reads that crate's own leading
doc comment for more context before trying again. Stops early once the quality threshold is met, or
after `--max-iterations`, always ending with a curated-docs `docs generate` run:

```bash
ekos architecture investigate                                 # RFC 0066 MVP defaults: 3 iterations,
                                                                # 0.90 quality threshold, --output doc
ekos architecture investigate --max-iterations 5 --quality-threshold 0.95 --output doc
```

Reuses the `[llm]` provider already configured in `ekos.toml` (local Ollama or a cloud provider) —
no separate `--llm` flag. See RFC 0067 for what's deliberately out of scope for this MVP
(persistent checkpointing/resume, concurrency-safety infrastructure, CI/CD exit codes, multi-format
output).

Because the LLM-classified crate role is a real judgment call, not a deterministic fact, two
follow-on commands treat it accordingly rather than silently trusting or silently re-deriving it:

```bash
ekos architecture diff --since <timestamp>   # real id-set comparison of technologies, crate role
                                              # classifications, risks, and open questions between
                                              # two points in time — not a fuzzy match (RFC 0108)
ekos architecture review                     # list/confirm/reject pending role classifications;
                                              # a confirmed-or-rejected review status survives the
                                              # next `ekos commit` even though the underlying claim
                                              # is content-signature-versioned and gets re-derived
                                              # on every run (RFC 0109)
```

`ekos_architecture_diff` and `ekos_architecture_review` expose both over MCP too — see the AI agent
access section below.

### LLM-backed compile-time descriptions (RFC 0088, opt-in)

Unlike `--prose` above (render-time, re-spent on every `docs generate` call), `[llm-description]`
in `ekos.toml` runs at `commit` time and persists real, evidence-grounded `ai_overview`/`ai_usage`
properties straight into the ledger — queryable through `ekos ekl`/`ekos ask`/MCP the same as any
other compiled knowledge, not just rendered once. Covers every `Module`/`Rollup`/`Crate`, and every
`Symbol` with a compiled `source_span` (Rust and Elixir today), regardless of whether RFC 0087
already found a real doc comment — a doc comment is real input to the prompt, not a skip condition.
When one exists, a new `ai_comment_check` property (`consistent`/`stale`/`incomplete`) flags a real
discrepancy between what the comment claims and what the code actually does, rendered as a visible
callout right on the entity page's Definition section — never silently trusted, never overwritten.
A single project-level call also fills `Architecture.md`'s `Purpose`/`Architecture style` fields
when real signal (a README, compiled subsystems, compiled technologies) exists to ground them.

```toml
[llm-description]
enabled = true
scope = "modules"   # "modules" (default, cheapest) | "symbols" | "all"
```

```bash
ekos commit          # shows a real call-count estimate, asks to confirm before any spend
ekos commit --yes    # skip the confirmation prompt
```

Opt-in and cost-gated like `[architecture-reasoning]` — a real, potentially large spend (~900 real
LLM calls at the default `scope = "modules"` against a real mid-size codebase, ~5x that at
`scope = "all"`), never defaulting to the more expensive tier just because it was turned on.

### Compiled-knowledge query engine (RFC 0118 — SEARCH → QUERY → REASON)

Traditional RAG searches documents; EKOS queries **compiled knowledge**. The retrieval stack is
three operations, built as RFCs 0119–0126 (`devlog_143`–`devlog_149`):

- **SEARCH** — one `KnowledgeStore::retrieve` seam behind every consumer, fusing a BM25 arm, an
  exact-name arm, and (opt-in) a vector arm with Reciprocal Rank Fusion (Cormack RRF, `k=60`). BM25
  indexes object names and content with English stemming, so a singular mention ("the customer
  table") resolves the same object a plural exact mention ("the Customers table") already did.
  `ekos query find "<text>" --mode lexical|vector|hybrid`; `--explain` prints the compiled plan
  and per-arm timings (populated on partitioned and distributed stores too, not just a single
  `FactLedger`). The same fused path runs on the single `FactLedger`, the partitioned
  store, and the distributed gateway.
- **QUERY** — direct, zero-LLM answers over the compiled graph: `fact(entity, attr)` for one
  attribute of one object, named ops (`dependents`, `callers`, `path`, …) for the graph. Exposed
  as MCP `ekos_query` (a typed list of source-cited claims) and `ekos_retrieve` ("show your
  work": the plan + evidence set + how the question was understood).
- **REASON** — `ekos ask "<question>"` now *compiles* the question: a rules planner routes it to
  fact lookups and graph traversals, executes them into a typed `EvidenceSet` where every item
  carries its provenance, and the model's job shrinks to "explain this evidence, cite each item."
  `--explain` prints the plan and evidence; `--classic` selects the pre-0123 retrieve-and-dump
  path. A citation not backed by a source id in the evidence set is a reported finding, not a
  formatting detail. Claims cite **a place in a file, not just a file** (RFC 0140): every
  Rust/Python/Elixir symbol with a `source_span` carries real evidence naming its path, its line,
  and the source text itself, rendered as `path:start-end` — so asking what a function does shows
  the model the function body, not only its name. Each Rust/Python/Elixir function or method also
  carries a real `signature` (RFC 0141) — the discriminating term for "what builds an
  `Arc<dyn LlmProvider>`" often lives in a return type, not the function's own name — and a Rust
  `Calls` edge carries `call_count`, `call_site_line`, and `caller_is_test`, so impact analysis can
  weigh 40 production call sites differently from 40 mostly-test ones instead of returning an
  undifferentiated list. For the top few entities in each answer's evidence set, `ekos ask` also
  reads the entity's real, on-demand source text straight from the artifact store — never the live
  filesystem, so it never bypasses redaction (RFC 0140 §3) — giving the model the actual code
  behind a claim, not just a name and a short excerpt. When the artifact store holds no file text
  for the entity, the source recorded with the symbol at recover time (up to 40 lines) is shown
  instead (RFC 0177). An opt-in `[retrieval] rerank = "llm"`
  (off by default) asks the model to reorder the top candidate evidence items by real relevance
  before it answers (RFC 0140 §4) — never on the deterministic retrieval-ranking path RFC 0126's
  CI gate checks, only inside the REASON answer pipeline itself.

EKL gains `FIND Object SEMANTIC 'text' [LIMIT k]` — the retriever as a candidate-set strategy.
Retrieval quality is CI-gated: `ekos_runtime::retrieval_eval` holds a checked-in graded query set
and a reference estate, and a workspace test fails the build if Recall@10 / MRR / nDCG@10 or
intent-classification accuracy drops more than 2% below the recorded baseline;
`cargo bench --bench retrieval_eval` prints the current scoreboard (RFC 0126).

What search reads and how it ranks (RFC 0177):

- An object is indexed by its name, kind, excerpt, and for a symbol its doc comment, signature and
  fields. An index built by an older version is rebuilt on the next command that writes to the
  ledger; `ekos ledger repair` does it at once.
- A hit that holds every word of the query ranks first. Hits that hold some of the words follow,
  ordered by BM25 rank fused with how many words each holds.
- A file is found by its name without directory or extension (`0043-secrets-and-pii-redaction`).
- The excerpt shown with a hit is the passage that matched the query.
- A question that asserts something the evidence does not support is answered
  `Premise not supported.`, followed by what the evidence does show. A question whose answer is
  not in the evidence is answered `Insufficient evidence.`, with what the evidence does show.

### The vector arm — semantic search (RFC 0125, opt-in)

A question phrased with none of the target object's words ("the thing that sends welcome emails" →
a function called `dispatch_signup_notification`) has no lexical hook. `[embeddings]` in
`ekos.toml` adds a vector retrieval arm: `ekos commit` embeds every compiled object (its name,
kind, and `ai_overview` prose if present) into a derived `<ledger-dir>/vectors/` index, and
retrieval fuses cosine-nearest hits with the BM25 + exact-name arms (Reciprocal Rank Fusion, the
same fuser as RFC 0120).

```toml
[embeddings]
enabled = true
provider = "ollama"          # "ollama" | "openai" | "mock"; falls back to [llm] provider
model = "nomic-embed-text"   # optional override
api-key-env = "OPENAI_API_KEY"
cache = true                 # content-addressed .ekos/embed-cache/, on by default
```

```bash
ekos query find "sends welcome emails" --mode vector   # semantic only
ekos query find "welcome email" --mode hybrid          # semantic + BM25, fused
```

Opt-in and off by default — with no `[embeddings]` table nothing is embedded and retrieval is the
pure BM25 + exact-name path. Embeddings are cheap and disk-cached, so unlike `[llm-description]`
there is no spend prompt. Single-node only this phase (a no-op on a SQLite or partitioned
workspace); a vector/hybrid search with no index built yet degrades to lexical with a visible
note. The MCP `ekos_search` tool takes the same `mode` and reports `arms_run`. Per-arm wall-clock
timings (`arm_timings`, RFC 0126) ride along on the `ekos_search` / `ekos_retrieve` results, into
`.ekos/query-log.jsonl`, and in `ekos query find --explain`.

### Eval harness (RFC 0138, on-demand)

`ekos eval run` grades whole `ekos ask` answers against a checked-in, 101-scenario suite spanning
seven categories — Architecture, Code, Dependencies, Lineage, History, Security, Adversarial
(`evals/datasets/*.yaml`) — not just retrieval ranking (that's RFC 0126's separate, narrower,
CI-gated `ekos_runtime::retrieval_eval`). Every score is deterministic keyword/id matching — no
LLM judge: did the answer state the expected facts, cite real (non-hallucinated) evidence, cover
what was asked, surface the right objects in the top-10, route to the right REASON planner query
type, and — for the Adversarial category — actually say **"Insufficient evidence"** for a question
with no grounded answer instead of inventing one. That last category is the harness's strictest:
every scenario in it expects a refusal, and an answer that invents a plausible-sounding detail
(a database name, a version number, a person) counts as a hallucination regardless of how
confidently it reads.

Recall@10 is graded against the exact keyword-only query `reason::plan()` actually searches with
(RFC 0139), not the raw natural-language question a `reason`/`ask` scenario asks — the two can rank
differently, so grading the wrong one could pass or fail a scenario for a reason unrelated to what
the model was shown. Lexical search itself also treats a bareword `and`/`or` as connector noise,
not a literal word a document must contain — the same two words this codebase already treats as
English stopwords everywhere else — so an "A or B" style query can match on either real term
without silently requiring the word "or" itself to appear.

```bash
cd ekos
cargo run -p ekos -- eval run --dataset ekos-full   # every category, "evals/" at the repo root
cargo run -p ekos -- eval run --dataset architecture --agent ollama
cargo run -p ekos -- eval run --dataset hallucination   # Category G only
cargo run -p ekos -- eval history                       # every past run, as a trend table
```

```
EKOS EVALUATION
─────────────────────────────

Dataset: architecture
Agent: ollama (llama3:latest)
Runtime: local

Scenarios:                    3
Passed:                       0
Failed:                       3

Answer correctness:       11.1%
Evidence groundedness:   100.0%
Completeness:             11.1%
Recall@10:                  n/a
Hallucination rate:        0.0%

Avg tokens:               1,221
P95 latency:              49.4s

Cache hits:                 0/3
Tokens saved:               n/a
Peak RSS:               69.7 MB
CPU time:                 14.7s

Status: FAIL
```

That example is a real run against this repo's own live self-analysis ledger with the local
`llama3:latest` model — not a simulated one. It is also the *floor*: a workstation-sized local model.

**Full-suite results — `ekos-full`, 101 scenarios, graded deterministically.** The answering model
went from a local llama3 8B on Ollama to **DeepSeek V4 Flash through [OpenCode Zen](https://opencode.ai/zen)**
(an OpenAI-compatible cloud endpoint), and the knowledge EKOS hands it was improved in two further steps. The same
checked-in suite, one change at a time:

| Step | Passed | What changed |
|---|---|---|
| Baseline, local `llama3:latest` (8B) — report `20260914T154459Z` | 42/101 | — |
| + evidence text kept, citation parsing, refusal wording (devlog_183) | 53/101 | Grader and evidence-rendering bugs, not the model |
| **+ DeepSeek V4 Flash** (model swap only) | **70/101** | A larger model, and the local one had been reading a **truncated prompt** — EKOS never sent `num_ctx`, so Ollama dropped the *start* of long prompts, where the instructions live (RFC 0145) |
| + document structure (RFC 0144) | **79/101** | Markdown cut by heading instead of blind 2,500-char chunks, fully indexed; docs link to code and to each other; output limit raised to 8,192 |
| + query-planner fixes (devlog_186) | **87/101** | A dependency phrase in a descriptive clause no longer triggers a graph walk; `crate::path` names resolve as one entity; generic words stop matching unrelated objects |

Seventeen points came from the model and seventeen from engineering; 53 → 87 is **+34**. Per category, before → after:

| Category | Before | After |
|---|---|---|
| Architecture | 9/20 | 18/20 |
| Code | 8/15 | 13/15 |
| Dependencies | 10/12 | 10/12 |
| Lineage | 5/12 | 10/12 |
| History | 3/12 | 11/12 |
| Security | 7/12 | 10/12 |
| Adversarial | 11/18 | 15/18 |
| **Total** | **53/101** | **87/101** |

| Metric | llama3 8B (53/101) | DeepSeek V4 Flash (87/101) |
|---|---|---|
| Answer correctness | 50.1% | **85.7%** |
| Evidence groundedness | 65.9% | **95.6%** |
| Hallucinated answers on adversarial questions | 7 | **3** |
| Recall@10 | 64.7% | 55.9% — *fell* |
| Latency | up to 79 s p95, killed three times for lack of memory on a 15 GB workstation | median 5 s per fresh call |
| Cost of a full 101-question run | free (local) | about **$0.05–0.08** |

Recall@10 fell because documents are now many heading-sections that outrank the crate or file a
retrieval-only scenario expects; answers improved anyway, and section-vs-document ranking is a tracked
follow-up. These numbers were re-verified against the per-category reports saved in
`evals/reports/zen-*/` (`zen-base` 70, `zen-final-8k` 79, `zen-planner2` 87). The full account, including the model-swap
run's 2,048-token output limit that cut off 17 answers (DeepSeek V4 Flash reasons, and its hidden reasoning
counts against the limit — so the model's own contribution is, if anything, understated), is in
[EKOS from 53 to 87](https://alexeyban.github.io/EKOS/presentations/deepseek-53-to-87.html) and
devlog_183 / 185 / 186.

**What still fails — 14 of 101, named rather than averaged away:**

| Cause | Scenarios |
|---|---|
| The model correctly rejects a false premise but not in refusal wording the grader accepts | adv-004, adv-011, adv-015 |
| The answer never reaches the top of the retrieved evidence | code-002, lin-008, dep-004 |
| The fact isn't recorded yet (a workspace-inherited Rust edition, struct fields as claims, no caller reached the evidence) | code-004, lin-007, dep-005 |
| Retrieval-only scenarios graded on recall@10 (see above) | arch-009, hist-007 |
| Right in substance, wrong keyword | arch-020, sec-002, sec-010 |

**Reproduce it, with your own model:**

```bash
export OPENCODE_API_KEY=...        # or any OpenAI-compatible endpoint: set base-url/model in the config
cargo run -p ekos -- --config ../ekos.zen.toml eval run --dataset ekos-full --save-answers
cargo run -p ekos -- eval history  # trend table across every saved run
```

```toml
# ekos.zen.toml — hosted, or a self-hosted OpenAI-compatible server (vLLM, llama.cpp) inside the network
[llm]
provider    = "openai"
base-url    = "https://opencode.ai/zen/v1"
model       = "deepseek-v4-flash"
api-key-env = "OPENCODE_API_KEY"

[ai]
max-tokens  = 8192   # a reasoning model: hidden reasoning counts against this

# local Ollama: set the window explicitly — a silent default truncation cost 17 points
# [llm]
# provider = "ollama"
# context-window = 32768
```

**Closed environments.** Compiling needs no GPU, no network and no model; answer quality tracks the model you
can serve. A workstation-sized local model lands near the llama3 column; reaching the DeepSeek column without a
cloud API means self-hosting a much larger open-weights model on dedicated GPU servers, with a context window of
at least 32k tokens and enough throughput to answer in seconds. Prompts contain real source excerpts — EKOS
redacts secrets and PII before anything reaches the ledger, but a hosted model still sees your code (Zen's paid
models are zero-retention; its free models may use prompts for training).

A local model is real and free to run, but it is not the reference: `ekos eval run` refuses outright rather than
silently grading against the stub `MockLlmProvider` when the configured provider's API key isn't set (there is no
`--agent mock` option). Grading is unchanged across every step above — keyword and id matching at temperature 0,
unchanged prompts replayed from the LLM cache — so a score that moved is attributable to a real change.

*Earlier history.* With llama3 held fixed the suite went 39 → 43 (RFC 0140/0141), then 42 → 53 against the
`20260914T154459Z` baseline (devlog_183), mostly because the harness found something unflattering: an adversarial-question fabrication count that got *worse* (3 → 6) once
third-party noise was gone and real objects made a wrong answer read more convincingly; a bit-identical re-run
after RFC 0139/0140/0141 that confirmed `temperature: 0` makes an unchanged prompt reproducible; and
recall@10 grading that had silently graded the wrong query (RFC 0139, devlog_182). Details: devlog_182, devlog_183.

Those numbers moved mostly because the harness found something unflattering: **94% of what this
repo was compiling wasn't its own code.** A Python virtualenv and two `.scannerwork/` directories
had never been excluded from the observation walk — `.gitignore