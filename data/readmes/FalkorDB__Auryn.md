<div align="center">

# Auryn

**Turn any codebase into a queryable knowledge graph — so your AI agent answers from real
structure instead of grepping and guessing.**

[Quickstart](#quickstart) · [Agent setup](#give-your-agent-the-graph) · [Languages](#what-it-can-read) · [Docs](#documentation)

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue?style=flat-square)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-ready-5980a6?style=flat-square)](https://modelcontextprotocol.io/)
[![FalkorDB](https://img.shields.io/badge/graph-FalkorDB-5980a6?style=flat-square)](https://www.falkordb.com/)

Works with **Claude Code** · **Cursor** · **Windsurf** · any MCP client

</div>

---

Point it at a repo. It parses every file, builds a graph of functions, types, tables and
endpoints — plus the edges between them (`CALLS`, `EXTENDS`, `READS`/`WRITES`, `DEPENDS_ON`) —
and stores it in [FalkorDB](https://www.falkordb.com/). Your coding agent then traverses that
graph through MCP and **cites file and line** for every claim.

Sixteen languages. Live SQL and Oracle schemas too. No server, no Docker to get started.

## Quickstart

Two commands, zero infrastructure. You'll be looking at a real graph in about a second.

```bash
pip install falkordb-auryn
auryn quickstart
```

This boots FalkorDB **embedded** (in-process, no daemon), ingests a tiny payments API that
ships inside the package, and opens the viewer at <http://127.0.0.1:8080>.

![The quickstart viewer showing the sample app's call graph — endpoints, the charge_card billing path, and the Account class hierarchy.](docs/images/quickstart-viewer.png)

Your own project is the same command with a path:

```bash
auryn quickstart path/to/your/repo
```

The graph persists at `<path>/.auryn/graph.db`, so re-running reuses it. First pass parses
everything; after that, re-ingestion is a delta — unchanged files are a no-op.

> **Requirements** — Python ≥ 3.12. `falkordb-auryn` is batteries-included: every language plugin out
> of the box. The in-process database is fetched automatically on first `auryn quickstart` on macOS /
> Linux (recent glibc); on native Windows or older-glibc Linux, point at a remote FalkorDB via
> `auryn install --backend remote`. Add live-DB drivers with `"falkordb-auryn[all]"`. For an isolated
> tool install, include the DB up front: `uv tool install "falkordb-auryn[embedded]"`. From a clone?
> `uv sync` then `uv run auryn quickstart`.

## Give your agent the graph

The viewer is a one-shot look. The real payoff is your agent querying the graph itself.
Install once:

```bash
auryn install
```

That prompts for a FalkorDB backend — **local** (bundled server, starts on demand) or
**remote** (host/port/creds) — then registers the `auryn` MCP server and skill with every
agent it detects. It writes only to `~/.auryn` and the agent's own config. Never your repo.

From there it's just conversation:

> **You:** What breaks if I change the signature of `charge_card`?

```text
● auryn_status()          → no graph for this repo yet
● index_repository(path=".")   → indexed: functions, calls, endpoints, inheritance
● locate(name="charge_card")   → Function  app/billing.py:9  id: python://…charge_card(...)
● impact_of(id="python://…charge_card(...)", edge_types=["CALLS"])
    → create_charge (app/api.py) ──EXPOSES_ENDPOINT──▶ POST /charges
```

> **Agent:** A blast radius of one direct caller: `create_charge` in `app/api.py`, which
> handles **POST /charges** — so the endpoint's contract changes with it. `charge_card` itself
> calls `get_account`, `_guard_limit` and `Connection.execute`; none are affected by a
> signature change. Update `create_charge` and the `/charges` request shape together.
> *(cites `app/api.py:15`, `app/billing.py:9`)*

No raw Cypher, no file dumps, no guessing. One hop, id-backed. Each repo gets its own graph.

**Your code stays yours.** Everything runs on your machine or your own FalkorDB — self-hosted,
no hosted service in the path, no telemetry, no phoning home. Read tools issue only
`GRAPH.RO_QUERY`, so an agent is structurally incapable of writing to your graph, and `install`
touches nothing but `~/.auryn` and your agent's config.

<details>
<summary><b>The tools your agent gets</b></summary>

<br>

| Tool | | What it does |
|---|---|---|
| `auryn_status` | read | Is there a graph yet, and what's in it? **Called first.** |
| `index_repository` / `ingest_repository` | **write** | Build or update the graph for a local dir or git repo. |
| `locate` | read | Find symbols by name — the entry point; other tools take the `id` it returns. |
| `search_code` | read | Semantic (vector) search by meaning when you don't know the name — needs `auryn embed` first. |
| `get_context` | read | One node's properties, source, and 1-hop neighbours. |
| `who_calls` / `callees` | read | Inbound callers / outbound callees within N hops. |
| `find_path` | read | Shortest path between two nodes — "does X reach Y, and how." |
| `impact_of` | read | Blast radius over `CALLS`/`DEPENDS_ON`/`READS`/`WRITES`. |
| `trace_entrypoint` | read | Full call closure of an entry point, plus every table it touches. |
| `get_schema` / `run_cypher` | read | The meta-model; arbitrary **read-only** Cypher. |

`list_graphs` / `use_graph` switch between multiple graphs on one instance.

</details>

## Why a graph

| Question | grep | Auryn |
|---|---|---|
| Who calls this? | every textual match, no callers of callers | exact inbound edges, N hops deep |
| What breaks if I change it? | you read and hope | traversal with file:line citations |
| Does this endpoint touch that table? | unanswerable | one path query |
| Is the answer current? | always re-read | delta re-ingest; unchanged code is free |

## What it can read

Everything file-based is **auto-detected** by `auryn ingest` in a single pass. Live
databases are read via `auryn run <name>`. `pip install falkordb-auryn` includes every language by
default; for a lean, single-language install instead, `pip install auryn-python` (each plugin pulls
`auryn-core`).

<details>
<summary><b>All sources and engines</b></summary>

<br>

| Source | Extra | Engine |
|---|---|---|
| Python | `[python]` | tree-sitter → Jedi (deep) |
| TypeScript / JavaScript | `[typescript]` | tree-sitter |
| C# | `[csharp]` | Roslyn (deep), tree-sitter fallback |
| Java · C · C++ · CUDA | `[java]` `[c]` `[cpp]` `[cuda]` | tree-sitter |
| Go · Rust · PHP · Julia | `[go]` `[rust]` `[php]` `[julia]` | tree-sitter |
| Ruby · Kotlin · Swift · Bash | `[ruby]` `[kotlin]` `[swift]` `[bash]` | tree-sitter |
| PL/SQL files | `[oracle]` | vendored ANTLR |
| Oracle (live DB) | `[oracle-live]` | oracledb + ANTLR |
| SQL schema (live DB) | `[sql]` `[sql-all]` | SQLAlchemy, any dialect |

The deep C# engine needs the [.NET SDK](https://dotnet.microsoft.com/) on `PATH`; without it,
C# falls back to tree-sitter automatically.

</details>

## CLI

```bash
auryn ingest dir /path/to/repo --project-name MyApp   # auto-detect every language
auryn ingest repo https://github.com/you/repo.git --ref main
auryn view                    # open the viewer against the configured backend
auryn serve | stop            # run/stop the local FalkorDB daemon explicitly
auryn uninstall [--purge]     # reverse install
```

Omit `--host`/`--port` and it uses the backend from `auryn install`. Full reference:
[docs/cli.md](docs/cli.md), or `auryn <command> --help`. Runnable walkthroughs live in
[`demo/`](demo/).

## Documentation

| | |
|---|---|
| [Architecture](docs/architecture.md) | Plugin discovery, the ingest pipeline, delta-sync, backends. |
| [Graph model](docs/graph-model.md) | Labels, edges, ids, provenance — and what each ingestor extracts. |
| [CLI reference](docs/cli.md) | Every command and flag. |
| [Adding a language](docs/adding-a-language.md) | A worked, line-by-line new ingestor. |
| [Docs index](docs/README.md) | Everything, including the ADRs. |

## Contributing

```bash
uv sync --group dev
uv run pytest --cov=auryn --cov-report=term-missing
```

Tests run against embedded FalkorDB by default — no server, no Docker. Set
`AURYN_TEST_BACKEND=server` for a real one. New language ingestors are very welcome: start
at [CONTRIBUTING.md](CONTRIBUTING.md).

<div align="center">
<br>

Built by [FalkorDB](https://www.falkordb.com/)

</div>

