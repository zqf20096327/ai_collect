# hstack

**Small models do the work. Frontier models direct it.**

hstack is a collection of agent skills that turns a frontier model into a senior engineer and a small, cheap model into the team that does the work.

The small model writes the spec, the plan and the tests, writes the code, and runs its own reviewer. The frontier model writes a short intake, approves the plan, answers a few checkpoints with terse directives, and signs off on the result. Most of the time it's just waiting, which costs nothing.

The goal: most of the tokens go to the cheap model, while code quality stays at the level a frontier model would hold it to.

> Status: early. hstack currently runs on **Muse Code**: Muse Wonder as the frontier and Muse Spark as the small model. Other harnesses come later.

---

## Why

Frontier tokens cost about 100× more than small-model tokens. Earlier experiments with hstack showed where they go:
- **The frontier writing text is the expensive part:** specs, briefs and fixes.
- **Small-model coding is almost free:** in one run, six small-model workers wrote six modules for 8 cents.
- **Every step moved from the frontier to the small model cut cost without hurting quality.**

So hstack takes that to its end. The small model does everything it can, and the frontier only decides **why** and **what**, checks the **how**, and corrects course in as few tokens as possible.

## How it works

![hstack workflow: the frontier writes the intake, a small-model lead plans and builds with sub-agents and an independent reviewer, and the frontier approves at the plan and done checkpoints](docs/hstack-flow.png)

<sub>Source: [`docs/hstack-flow.excalidraw`](docs/hstack-flow.excalidraw), editable at excalidraw.com.</sub>

- **Event-driven:** while the lead works, a script blocks and wakes the frontier only when a checkpoint arrives. There's no polling, and waiting costs no tokens.
- **Worker count follows the task:** the lead decides whether to do it alone or fan out to 2 or 100 sub-agents, and the frontier approves that choice in the plan.
- **Isolated:** the lead works in its own git worktree. Nothing reaches your code until the frontier approves and the patch is applied.
- **Skilled small models:** the `hstack-practice` skill gives the small model the engineering habits it usually lacks: exact specs, state tables, test-first development, real-environment facts and security basics. The frontier doesn't have to repeat them in every message.

## Risks and how hstack handles them

| Risk | Mitigation |
|---|---|
| Muse's spec drifts from what the user meant | The frontier's intake states acceptance criteria up front, and plan review checks the spec against them |
| Muse's tests only confirm its own mistakes | An independent Muse reviewer adds tests aimed at breaking the code, and the frontier spot-checks tests against the criteria |
| Lots of checkpoints add up | Wake on events only, keep digests short, and frontier context stays small |
| Tasks too vague for a small model | The frontier stays involved longer: more plan iterations, still terse |

## The skills

| Skill | Used by | Role |
|---|---|---|
| [`hstack`](skills/hstack/SKILL.md) | frontier (e.g. Muse Wonder) | Senior engineer: intake, plan review, checkpoint directives, final review, token discipline |
| [`hstack-lead`](skills/hstack-lead/SKILL.md) | small model (e.g. Muse Spark) | Owns the task end to end: spec, plan, fan-out, tests, build, independent review, checkpoints |
| [`hstack-practice`](skills/hstack-practice/SKILL.md) | small model (e.g. Muse Spark) | Engineering practice: exact specs, state tables, tests, real environment, security, honest reporting |
| [`hstack-activate`](skills/hstack-activate/SKILL.md) | frontier | `/hstack-activate`: turns hstack on for the session, or stays off if your model is already the smallest |

## Install

```bash
curl -fsSL https://hstack.shellhaki.dev/install | sh
```

The installer downloads the `hstack` CLI and walks you through setup:
1. **Agent:** Muse Code for now. Claude Code, Cursor and OpenCode come later.
2. **Frontier model:** the model you run sessions with, which directs.
3. **Small model:** the model that does the engineering. Pick `auto` (the best-ranked model below your frontier) or a specific one. Every lower-ranked model is kept as a fallback, so if a model isn't on your plan the next one starts automatically.

It installs the skills into `~/.config/hstack` (linked into your agent's skills folder) and saves your choices in `~/.config/hstack/config.json`.

From source: `go install github.com/shellhaki/hstack/cmd/hstack@latest && hstack`. Or clone the repo and run `./install.sh muse`.

### CLI

| Command | What it does |
|---|---|
| `hstack` | Interactive setup (same as `hstack init`) |
| `hstack init --agent muse --frontier <id> --small <id\|auto> --yes` | Non-interactive setup |
| `hstack models` | Model rankings, the benchmarks behind them, and credits |
| `hstack status` | Show your saved setup |
| `hstack uninstall` | Remove the skill links, and optionally `~/.config/hstack` |

## Use

1. Start your agent on the frontier model, e.g. `muse --model muse-wonder-1.0`.
2. Run **`/hstack-activate`**. If your session's model ranks above your small model, hstack turns on. If you're already on the smallest model, it says so and stays out of the way, because there is nothing cheaper to delegate to.
3. Give it a task:

   > Use hstack to add email sign-in with likes and comments to this app.

The frontier writes the intake, starts the small-model lead, and waits. One progress window shows the lead's checkpoints and the files it's writing. You get a single report at the end. Small tasks are done directly, without delegation.

### Model rankings

hstack picks and orders models using published benchmark results. These live in [`models/muse.json`](models/muse.json); run `hstack models` to see them.

| Model | Score | FrontierCode | Terminal-Bench | SWE-Atlas | Cost / task |
|---|---:|---:|---:|---:|---:|
| Muse Wonder Full | 54 | 35 | 60 | 69 | not published |
| Muse Wonder | 44 | 24 | 47 | 62 | $7.59 |
| Muse Ember | 40 | 21 | 43 | 55 | $0.22 |
| Muse Spark 1.3 | 37 | 22 | 30 | 59 | $4.34 |

Benchmarks:
- **FrontierCode-AA 2.0:** complex repository engineering
- **Terminal-Bench 4.1:** terminal and command-line execution
- **SWE-Atlas-QnA-AA:** software engineering knowledge and problem-solving

Credit goes to the maintainers of these benchmarks; hstack only reorders their published numbers. For other agents, hstack will use the same approach with benchmarks such as SWE-bench Pro, SWE-bench Verified, Terminal-Bench and FrontierCode, credited the same way.

### Scripts

| Script | Who runs it | What it does |
|---|---|---|
| `scripts/start.sh <repo> <orch> <name> <intake>` | frontier | Snapshot the repo into a worktree and start the Muse lead in the background |
| `scripts/wait.sh <worktree>` | frontier, in the background | Block until the lead posts a checkpoint (`EVENT <id> <file>`) or exits |
| `scripts/direct.sh <worktree> <id>` | frontier | Answer a checkpoint: `APPROVE`, `REVISE` or `ANSWER`, plus WHY / WHAT / HOW |
| `scripts/await.sh <id>` | lead | Block until the frontier answers |
| `scripts/progress.sh <worktree>` | you | Live view of checkpoints and files |
| `scripts/collect.sh`, `merge.sh`, `cleanup.sh` | frontier | Turn the worktree into a patch, apply it to your tree, clean up |

## Benchmarks

Every benchmark compares the same task done by the frontier alone against hstack. Both use exact token counts and are judged by a hidden acceptance suite that neither side sees. Results go in [`benchmarks/`](benchmarks/) whatever they show.

| Benchmark | Frontier alone | hstack | Hidden tests |
|---|---:|---:|---|
| [1: six engine modules](benchmarks/01-engine-modules/results.md) | $2.46 | **$1.59 (-35%)**: frontier $1.49 + small model $0.10 | 82/82 · 82/82 |

## History

hstack went through three designs. The first had the frontier write specs and briefs and came out 10% cheaper at best. The current design moves all writing to the small model and comes out 35% cheaper. [docs/HISTORY.md](docs/HISTORY.md) covers each version, its benchmarks, and every change that cut the cost.

## Roadmap

- **Skill bank (next):** a curated set of skills that make the small model better on its own (stack conventions, testing, security, framework and driver behavior), so the frontier corrects less.
- **Frontier optimizations:** a persistent frontier session, merge by script, a lighter base prompt, and fewer checkpoints for low-risk tasks. Estimated 75–85% cheaper than frontier alone; see [HISTORY](docs/HISTORY.md#where-the-cost-is-now-and-whats-next).
- More harnesses as frontier and small model: Claude Code, Cursor and OpenCode, starting from Muse.
- In-harness orchestration: harnesses that run several models themselves direct their own small models.

## License

See [LICENSE](LICENSE).
