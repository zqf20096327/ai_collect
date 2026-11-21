# hstack

**Small models do the work. Frontier models direct it.**

hstack is a collection of agent skills for **Claude Code** that turns the model you're running (the frontier) into a senior engineer and a smaller, cheaper model into the engineer who does the work.

The worker explores the codebase, plans, writes the tests and the code, and reports. The frontier writes a short brief, approves the plan, reviews the result, and sends at most a few lines of correction. It never writes the code itself.

> **Measured:** on a production-grade waitlist backend, Claude Opus 5.5 directing a Claude Haiku 5.5 worker cost **53% less** than Opus alone, with the same hidden-test results (20/20) and Opus writing **90% fewer** output tokens. [Details](benchmarks/02-waitlist-backend/results.md).

> Status: early. hstack runs **inside Claude Code**, using its sub-agents. Other agents come later.

---

## Why

Frontier tokens cost far more than small-model tokens, and the expensive part of agentic coding is generating code, re-reading files and iterating. The model that makes the best engineering decisions doesn't need to be the one that types every line. So:
- **The frontier** decides why and what, checks how, and corrects.
- **The worker** does the execution at small-model prices.
- **Waiting costs nothing.** The frontier is only active at checkpoints.

## How it works

![hstack workflow: the frontier writes the brief, the worker plans and builds, optionally with parallel workers and an independent reviewer, and the frontier approves at the plan and done checkpoints](docs/hstack-flow.png)

<sub>Source: [`docs/hstack-flow.excalidraw`](docs/hstack-flow.excalidraw), editable at excalidraw.com.</sub>

1. **`/hstack-activate`:** the session's model becomes the frontier and asks which smaller model should do the work. It keeps asking until you name a valid one; loose names like "haiku 5.5" are fine. If you're already on the smallest model, it stays off.
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
| [`hstack-activate`](skills/hstack-activate/SKILL.md) | skill, `/hstack-activate` | Turns hstack on and keeps asking for a valid, smaller worker model |
| [`hstack`](skills/hstack/SKILL.md) | skill (frontier) | Senior-engineer loop: size gate, brief, plan review, build review, one correction round, token discipline |
| [`hstack-swarm`](skills/hstack-swarm/SKILL.md) | skill, `/hstack-swarm` | Parallel workers on independent parts, then an independent reviewer |
| [`hstack-practice`](skills/hstack-practice/SKILL.md) | skill (worker) | Engineering habits small models lack: exact specs, state tables, tests first, real-environment facts, security, honest reports |
| [`hstack-worker`](agents/hstack-worker.md) | sub-agent | Plans, then builds and reports, in two phases |
| [`hstack-reviewer`](agents/hstack-reviewer.md) | sub-agent | Tries to break the work and reports defects without fixing them |

## Install

```bash
curl -fsSL https://hstack.shellhaki.dev/install | sh
```

The installer downloads the `hstack` CLI and sets everything up:
- it links the skills into `~/.claude/skills` and the sub-agents into `~/.claude/agents`
- it saves a default worker model, which `/hstack-activate` suggests, in `~/.config/hstack/config.json`

Other ways to install:
- **From source:** `go install github.com/shellhaki/hstack/cmd/hstack@latest && hstack`
- **From a clone:** `./install.sh`

| Command | What it does |
|---|---|
| `hstack` | Interactive setup (same as `hstack init`) |
| `hstack init --worker haiku --yes` | Non-interactive setup |
| `hstack models` | The Claude models used to validate workers, most to least capable |
| `hstack status` | Show your saved setup |
| `hstack uninstall` | Remove the links, and optionally `~/.config/hstack` |

## Use

1. Start Claude Code on your frontier model, e.g. `claude --model opus`.
2. Run **`/hstack-activate`** and name the worker, e.g. `haiku`.
3. Give it a real task:

   > Build the waitlist API from SPEC.md, with tests.

   For tasks that split into independent parts, run **`/hstack-swarm`** first.

Small tasks are done directly, without delegation, because delegating them costs more than it saves.

## Models

[`models/claude.json`](models/claude.json) lists the Claude models from most to least capable. `/hstack-activate` uses it to accept only workers smaller than the session's model:

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
