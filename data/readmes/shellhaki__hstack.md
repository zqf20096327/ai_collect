# hstack

**Small models do the work. Frontier models direct it.**

hstack is a collection of agent skills for **Claude Code**, **Muse Code**, **Codex** and **Hermes Agent** that turns the model you're running (the frontier) into a senior engineer and a smaller, cheaper model into the engineer who does the work.

The worker explores the codebase, plans, writes the tests and the code, and reports. The frontier writes a short brief, approves the plan, reviews the result, and sends at most a few lines of correction. It never writes the code itself.

> **Measured:** on a production-grade waitlist backend, Claude Opus 5.5 directing a Claude Haiku 5.5 worker cost **53% less** than Opus alone, with the same hidden-test results (20/20) and Opus writing **90% fewer** output tokens. [Details](benchmarks/02-waitlist-backend/results.md).

> Status: early. hstack runs **inside Claude Code** (its sub-agents), **inside Muse Code** (its `muse.workflow` agents), **inside Codex** (its custom agents) and **inside Hermes Agent** (separate `hermes chat` worker processes). Others come later.

---

## Why

Frontier tokens cost far more than small-model tokens, and the expensive part of agentic coding is generating code, re-reading files and iterating. The model that makes the best engineering decisions doesn't need to be the one that types every line. So:
- **The frontier** decides why and what, checks how, and corrects.
- **The worker** does the execution at small-model prices.
- **Waiting costs nothing.** The frontier is only active at checkpoints.

## How it works

![hstack workflow: the frontier writes the brief, the worker plans and builds, optionally with parallel workers and an independent reviewer, and the frontier approves at the plan and done checkpoints](docs/hstack-flow.png)

<sub>Source: [`docs/hstack-flow.excalidraw`](docs/hstack-flow.excalidraw), editable at excalidraw.com.</sub>

1. **`/hstack`:** the session's model becomes the frontier and asks which smaller model should do the work. It keeps asking until you name a valid one; loose names like "haiku 5.5" are fine. If you're already on the smallest model, it stays off.
2. **Brief:** the frontier writes about 15 lines: why, acceptance criteria, constraints, the risks it will review, and the done commands.
3. **Plan:** an `hstack-worker` sub-agent on the worker model explores and returns a short plan. The frontier replies `APPROVE` or `REVISE` in a few lines.
4. **Build:** the same worker keeps its context. It writes tests first, implements, runs the checks until they pass, and returns a compact done report.
5. **Review:** the frontier runs the checks itself, spot-checks only its risk areas, and sends at most one correction round.
6. **`/hstack-swarm`** (optional): the worker plans a split, several workers build independent parts in parallel, and an `hstack-reviewer` tries to break the result.

## Risks and how hstack handles them

| Risk | Mitigation |
|---|---|
| The worker's plan drifts from what the user meant | The frontier's brief states acceptance criteria up front, and plan review checks against them |
| The worker's tests only confirm its own mistakes | The frontier runs the checks itself and spot-checks risk areas; in swarm mode an independent reviewer tries to break the work |
| Review rounds add up | One correction round by default, and short directives |
| The task is too vague for a small model | The frontier stays involved longer: more plan iterations, still terse |

## Skills and sub-agents

| | Type | Role |
|---|---|---|
| [`hstack`](skills/hstack/SKILL.md) | skill, `/hstack` (frontier) | Turns hstack on (asks for a valid, smaller worker model), then runs the senior-engineer loop: size gate, brief, plan review, build review, one correction round, token discipline |
| [`hstack-swarm`](skills/hstack-swarm/SKILL.md) | skill, `/hstack-swarm` | Parallel workers on independent parts, then an independent reviewer |
| [`hstack-ui`](skills/hstack-ui/SKILL.md) | skill, `/hstack-ui` | UI work from real references: a design system first, then pages built only from it, reviewed by screenshot |
| [`hstack-motion`](skills/hstack-motion/SKILL.md) | skill, `/hstack-motion` | Motion-graphics videos from a prompt or a codebase: storyboard first, scenes built in Remotion from a starter kit, voice and sound timed to words, reviewed as stills |
| [`hstack-update`](skills/hstack-update/SKILL.md) | skill, `/hstack-update` | Updates hstack to the latest skills and sub-agents in every harness it is installed in, and lists the skill versions that changed |
| [`hstack-research`](skills/hstack-research/SKILL.md) | skill, `/hstack-research` | Market and technical research: workers read the web and write sourced notes, the frontier writes one report with a recommendation |
| [`hstack` guides](skills/hstack/ROUTES.md) | worker guides | How the worker thinks, read one at a time from a routing table: understand, explore, plan, sources, focus, verify, escalate, plus practice, debug and refactor |
| [`hstack-worker`](agents/hstack-worker.md) | sub-agent | Plans, then builds and reports, in two phases |
| [`hstack-researcher`](agents/hstack-researcher.md) | sub-agent | Answers one research question from the web, with sourced notes |
| [`hstack-reviewer`](agents/hstack-reviewer.md) | sub-agent | Tries to break the work and reports defects without fixing them |

## Install

```bash
curl -fsSL https://hstack.shellhaki.dev/install | sh
```

The installer downloads the `hstack` CLI and sets everything up for the harness you pick:
- **Claude Code:** it links the skills into `~/.claude/skills` and the sub-agents into `~/.claude/agents`
- **Muse Code:** it links the skills into `~/.agents/skills`, which Muse reads
- **Codex:** it links the skills into `~/.agents/skills`, which Codex reads, and writes the sub-agents as TOML files into `~/.codex/agents` (or `$CODEX_HOME/agents`)
- **Hermes Agent:** it links the skills into `$HERMES_HOME/skills` (default `~/.hermes/skills`; set `HERMES_HOME` or use `hermes -p <profile>` to target a profile). The worker is a separate `hermes chat` process, so there are no sub-agent files to write
- nothing else: you choose the worker model inside a session, with `/hstack`

Other ways to install:
- **From source:** `go install github.com/shellhaki/hstack/cmd/hstack@latest && hstack`
- **From a clone:** `./install.sh` (Claude Code), `HSTACK_AGENT=muse ./install.sh` (Muse Code), `HSTACK_AGENT=codex ./install.sh` (Codex; the skills only, then run `hstack install --agent codex` for the sub-agents) or `HSTACK_AGENT=hermes ./install.sh` (Hermes Agent)

| Command | What it does |
|---|---|
| `hstack` | Install for Claude Code (same as `hstack install`) |
| `hstack install --agent muse` | Install for Muse Code |
| `hstack install --agent codex` | Install for Codex |
| `hstack install --agent hermes` | Install for Hermes Agent |
| `hstack models [--agent claude\|muse\|codex\|hermes] [--frontier <id>] [--json]` | The models used to validate workers, most to least capable, read live from the harness's local catalog when it has one |
| `hstack status` | Show your saved setup |
| `hstack uninstall` | Remove the links, and optionally `~/.config/hstack` |

## Use

1. Start your harness on its frontier model: `claude --model opus`, `muse --model muse-wonder-1.0`, or Hermes Agent on your frontier model.
2. Run **`/hstack`** and name the worker: e.g. `haiku` in Claude Code, `ember` or `spark-1.3` in Muse Code, `luna` in Codex, `spark-1.2` in Hermes Agent.
3. Give it a real task:

   > Build the waitlist API from SPEC.md, with tests.

   For tasks that split into independent parts, run **`/hstack-swarm`** first.

Small tasks are done directly, without delegation, because delegating them costs more than it saves.

## Models

[`models/claude.json`](models/claude.json), [`models/muse.json`](models/muse.json), [`models/codex.json`](models/codex.json) and [`models/hermes.json`](models/hermes.json) list each harness's models from most to least capable. `/hstack` uses them to accept only workers smaller than the session's model. Hermes's live list is read dynamically from every provider in `$HERMES_HOME/provider_models_cache.json`; inside Hermes always run `hstack models --agent hermes`, since its model ids overlap other harnesses.

| Model | Alias |
|---|---|
| Claude Fable 5.2 | `fable` |
| Claude Opus 5.5 | `opus` |
| Claude Sonnet 5.5 | `sonnet` |
| Claude Haiku 5.5 | `haiku` |

Benchmark scores (SWE-bench Pro, SWE-bench Verified, Terminal-Bench, FrontierCode) will be added from published results, with credit to their maintainers.

## Benchmarks

Every benchmark compares the same task done by the frontier alone against hstack. Both use exact per-model token counts and are judged by a hidden acceptance suite that neither side sees. Results are published in [`benchmarks/`](benchmarks/) whatever they show.

| Benchmark | Frontier alone | hstack | Hidden tests |
|---|---:|---:|---|
| [2: waitlist backend, Claude Code](benchmarks/02-waitlist-backend/results.md) | $1.59 (Opus) | **$0.75 (-53%)**: Opus $0.46 + Haiku $0.30 | 20/20 · 20/20 |
| [1: six engine modules, earlier Muse version](benchmarks/01-engine-modules/results.md) | $2.46 (Muse Wonder) | $1.59 (-35%) | 82/82 · 82/82 |

## History

hstack went through four designs:
1. The frontier wrote the specs and briefs, and the saving was 10% at best.
2. The small model took over the writing.
3. The small model led the whole task through an external CLI (Muse Code), for a 35% saving.
4. hstack now runs inside Claude Code, where the frontier keeps one cached session and directs a worker sub-agent, for a 53% saving.

[docs/HISTORY.md](docs/HISTORY.md) covers each version, its benchmarks, and every change that cut the cost.

## Roadmap

- **Skill bank (next):** a curated set of skills that make the worker better on its own (stack conventions, testing, security, frameworks, data, UI), so the frontier corrects less.
- **More optimizations:** skip the plan checkpoint for low-risk tasks, and a lighter brief.
- **Model scores:** published benchmark results for every supported model, credited.
- **More agents:** Cursor, OpenCode and others, using the same activation flow.

## License

See [LICENSE](LICENSE).
