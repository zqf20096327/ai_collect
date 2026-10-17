<p align="center">
  <img src="assets/etchplan-logo.svg" alt="etchplan logo" width="100">
</p>

<h1 align="center"><em>etchplan</em></h1>

**Your agent solves the same shape of task again and again. _etchplan_ turns the repeatable parts into validated routines that can replay without model calls, with fallback to the agent whenever a guard does not hold.**

*Built by [Egoist Machines, Inc.](https://egoistmachines.com/) - efficient full-stack infrastructure for reliable AI systems.*

_etchplan_ watches local agent traces, mines recurring workflows, and compiles the safe ones into deterministic `ExecutionPlan`s. A routine runs only after validation. If the input drifts, a guard fails, or a tool is unbound, the agent handles the request.

- Zero model calls on a fully compiled replay.
- Guards, static checks, validation, and mutation gates before any served result.
- Local capture for Claude Code, Codex, and opencode; traces write to `~/.etchplan/`.
- Shadow, approval, canary, and drift kill-switch before live serving.
- Append-only audit log for routine decisions, tool calls, and fallbacks.
- CLI, MCP server, and runnable [BYO](examples/byo/README.md), [MCP](examples/mcp/README.md), and [real-API](examples/real_traces/README.md) examples.

## What It Is

**etchplan** removes repeat model calls when a validated tool workflow can replay directly, with the agent still behind the fallback. This is _not_ prompt caching, response caching, observability, or a workflow builder you hand-author. Those are all valid techniques that one can use in combination with etchplan to make model calls cheaper, skip near-duplicates, or help you watch the agent. 

**etchplan** is built for structured tool-call workflows: API/MCP integrations, browser actions, and repeated multi-step work where arguments bind to inputs or earlier tool outputs. Free-text coding churn is mined and usually refused because the arguments are code, shell, or prose instead of stable parameters.

Reference points: [Agent JIT Compilation](https://arxiv.org/abs/2605.21470) and [Agent Workflow Optimization / meta-tools](https://arxiv.org/abs/2601.22037). The comparison notes are in [RELATED_WORK.md](RELATED_WORK.md).

## Install

Apache-2.0, local-first, Python >= 3.11.

```bash
pip install etchplan        # or: uv tool install etchplan, pipx install etchplan
etch demo                   # the whole offline loop: import, mine, compile, validate, run. No agent, no keys.
etch doctor                 # confirm capture wiring and that etch is on your PATH
```

Try it with no install at all: `uvx etchplan demo`. Extras for the parts that need them: `etchplan[mcp]` (MCP server), `etchplan[browser]` (Playwright replay), `etchplan[desktop]` (macOS GUI capture). From source: `git clone https://github.com/Egoist-Machines/etchplan && cd etchplan && uv run etch demo`.

## Use it on your agent

Install capture once and use your agent normally. `etch setup` runs the [Quickstart](#quickstart) discovery loop for you: an auto-pipeline captures, mines, and compiles draft routines on every session and turn end, so you never run those steps by hand.

```bash
uv run etch setup claude-code --write     # also: codex | opencode
# use your agent; sessions capture to ~/.etchplan/ and the auto-pipeline keeps routines fresh

uv run etch report                        # money and time saved, read from the store the pipeline fills
uv run etch report --format html --open
```

That auto-pipeline is Quickstart steps 1-3 (import, mine, compile drafts) on a schedule; `etch report` and `etch yield` just read what it found. `etch doctor` checks that capture is installed and events are flowing. `etch mcp install` registers the MCP server for Claude Code, Claude Desktop, Cursor, Codex, or all supported clients. The full command surface, dry-run behavior, serving modes, and MCP proxy details are in [docs/cli.md](docs/cli.md).

Only serving stays manual, by design (Quickstart steps 4-5): gather agreement with `etch run --shadow`, approve once the evidence clears your bar, then canary an approved routine. Guard failure, missing binding, runtime error, or drift routes back to the agent.

## Example results

Per recurring solve on AppWorld (gpt-5.5), after one agent solve to seed and one compile:

| | agent, every time | _etchplan_ |
|---|--:|--:|
| latency | ~116 s | ~0.2 s (~580x faster) |
| cost | ~$0.47 | $0 (zero model calls) |
| reuse economics | pays full price every time | break-even after ~1.07 reuses; ~9x cheaper by the 10th reuse |

The heavy live-agent harness behind those numbers is not in this repo. The compact benchmark artifacts are, and each number is labeled `measured`, `recorded`, `estimated`, or `assumed`. See [docs/results.md](docs/results.md) and [docs/benchmark-methodology.md](docs/benchmark-methodology.md).

The real-API corpora show the same shape on flows:

| domain | workflow | traces | result |
|---|---|---:|---|
| `weather_brief` | geocode(city) -> forecast -> air_quality | 30 | 3-node, 0 model |
| `ip_weather` | geoip(ip) -> forecast | 18 | 2-node, 0 model |
| `zip_weather` | postal(zip) -> forecast | 18 | 2-node, 0 model |
| `github_repo` | get_repo(slug) -> get_branch | 18 | 2-node, 0 model |
| `word_assoc` | related(word) -> related(top) | 18 | 2-node, 0 model |
| `pokemon` | get_pokemon(name) -> get_ability(url) | 18 | 2-node, 0 model |

All six compile in the local yield check: 120 traces, 6 recurring workflows, 6 compiled. The traces and scope notes are in [examples/real_traces](examples/real_traces/README.md).

## Quickstart

The real flow finds the workflows an agent repeats, compiles and validates the safe ones, then serves them behind the agent. Steps 1-3 run as-is on a real public-API corpus shipped in the repo; steps 4-5 bind your own tools and earn a routine the right to serve live.

**1. Get traces.** The traces can be your agent's (`etch setup <harness> --write` captures sessions to `~/.etchplan/`, see above). To run every step now, import a shipped real-API corpus into the same store:

```bash
db=.etchplan.sqlite
uv run etch import jsonl examples/real_traces/weather_brief/traces.jsonl --db $db
```

**2. See what recurs and compiles.** `etch yield` mines the recurring workflows and reports which compile and why the rest refuse. It measures only, it never serves:

```bash
uv run etch yield --db $db --min-support 5
#  recurring: 1  ->  compiled: 1   (weather_brief: geocode -> forecast -> air_quality, 0 model calls)
```

On captured agent traces, `etch report` turns the same store into money and time saved.

**3. Compile and validate a routine.** `--pattern-id top` takes the highest-support pattern that compiles; validation executes the routine over trace-derived cases (measured, not estimated):

```bash
uv run etch compile pattern --db $db --pattern-id top --out weather_brief.yaml
uv run etch validate plan weather_brief.yaml --db $db
```

**4. Run it behind your tools, with the agent as fallback.** `--registry` binds the plan's tool names to your callables; any guard failure, unbound tool, or runtime error routes to `--fallback`, and every call lands in the audit log:

```bash
uv run etch run weather_brief.yaml --input in.json \
  --registry your_tools:registry --fallback your_tools:agent --audit audit.jsonl
```

Runnable end to end with real bindings in [examples/byo](examples/byo/README.md) (plain callables) and [examples/mcp](examples/mcp/README.md) (MCP tools plus a policy-gated live mutation).

**5. Earn trust before serving live.** Nothing serves on day one. Accumulate agreement in shadow, approve once the evidence clears your bar, then canary in; the drift kill-switch pulls a routine whose fallback rate climbs:

```bash
uv run etch run weather_brief.yaml --input in.json --registry your_tools:registry --shadow   # serves the agent, records match/mismatch
uv run etch plans approve weather_brief.yaml --min-matches 20 --max-mismatch-rate 0.0
uv run etch run weather_brief.yaml --input in.json --registry your_tools:registry --require-approval --canary --canary-pct 10
```

Just want to watch the loop once? `uv run etch demo` runs all of it offline on a bundled example, no agent and no keys.

## How It Works

```
agent traces
    |
    v
 normalize      clean, redact, slot
    |
    v
   mine         find repeats, verify parameter flow, learn guards
    |
    v
  compile       synthesize a guarded ExecutionPlan
    |
    v
  validate      execute on trace-derived replay cases
    |
    v
   run ------>  guards hold: replay with zero model calls
    |
    +  ------>  guard fails: fall back to the agent
```

The trust loop is `draft -> shadow -> approved -> canary -> served`. Mutating steps stay behind idempotency and mutation gates, and a routine that fails validation is never run. The package map, guard implementation notes, and deeper diagrams are in [docs/architecture.md](docs/architecture.md) and [docs/security-model.md](docs/security-model.md).

## Workload Fit

| Workload | Fit | Why |
|---|---|---|
| Repeated API / MCP tool workflows | Excellent | bindable arguments, data flow between steps, learnable guards |
| Browser / desktop action loops | Preview | semantic actions can replay behind the same trust loop |
| Coding-agent edit loops | Refuses by design | free-text step arguments do not bind to deterministic routines |
| One-off tasks | No | one seed solve plus one compile does not amortize |

For natural compile-yield checks on your own traces, see [docs/measuring-yield.md](docs/measuring-yield.md). Active forward edges are tracked in [docs/roadmap.md](docs/roadmap.md).

## Docs

- Results: [docs/results.md](docs/results.md), [docs/benchmark-methodology.md](docs/benchmark-methodology.md)
- Build/run: [docs/cli.md](docs/cli.md), [docs/architecture.md](docs/architecture.md), [docs/security-model.md](docs/security-model.md)
- Project: [docs/development.md](docs/development.md), [docs/roadmap.md](docs/roadmap.md), [RELATED_WORK.md](RELATED_WORK.md), [CHANGELOG.md](CHANGELOG.md), [CITATION.cff](CITATION.cff)

## License & Security

Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). The open-source code is free to use, including commercially; the "Etchplan" name and logo are trademarks ([TRADEMARKS.md](TRADEMARKS.md)), and Apache-2.0 grants no trademark rights. _etchplan_ is local-first: nothing leaves your machine by default.

Enterprise licensing and commercial support are available from [Egoist Machines, Inc.](https://egoistmachines.com/): hosted/managed serving, SSO/RBAC, a multi-tenant plan registry, and on-prem / BYOC deployment. Contact [sales@egoistmachines.com](mailto:sales@egoistmachines.com).

PRs welcome; see [CONTRIBUTING.md](CONTRIBUTING.md) (commits need a DCO sign-off: `git commit -s`). Report security issues privately per [SECURITY.md](SECURITY.md), not in public issues. Other bugs and feature requests go to the [issue tracker](https://github.com/Egoist-Machines/etchplan/issues).
