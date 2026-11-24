# Ennyn
<img src=".claude-plugin/icon.svg" align="right" width="128" alt="">

**English** · [Türkçe](README.tr.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Node 22+](https://img.shields.io/badge/node-22%2B-brightgreen)](package.json) [![Runtime dependencies: 0](https://img.shields.io/badge/runtime%20dependencies-0-brightgreen)](package.json)

Ennyn is a Claude Code plugin and Node CLI. It gives the agent a working routine: impact analysis before code is written, a two-round review, and checks on every commit for recurring classes of bugs.

[Install](#install-claude-code) · [Try it without installing](#try-it-without-installing)

![Output of ennyn rework, ennyn doctor, and ennyn core on the Ennyn repository](docs/assets/terminal.png)

> Early days (0.1.x). Ennyn is built with Claude Code using its own cycle; its work graph, findings and metrics are in `.ennyn/`; the handoff notes between cycles are working notes and stay outside the repository. The config format may still change before 1.0.

## Why Ennyn

In a project where an agent writes the code, these problems show up over time:

- A review finds a bug, the agent fixes it, and the fix causes a regression nearby. The next review catches the regression, and the loop continues.
- The questions that would prevent these bugs can be asked before the code is written (what else reads this value? can this state be reached another way?), but they usually come up only in review.
- A bug leads to a new prose rule in CLAUDE.md, and a few weeks later a bug of the same class is back.
- CLAUDE.md keeps growing and takes up context in every session, with no way to measure which rules have any effect.

## What it does

- Before editing code, the agent fills in an impact table: five questions about what the change affects, each answered, where possible, by running git grep, git log, or the tests. For a task picked for its value, it first lists each new piece with the line of the task that asks for it, and what already does it.
- Review gets two rounds. The second round only looks at what the first round's fixes changed. After that, a failing test proves a fix, not another round.
- When a class of bug recurs, the next cycle (one pass of the loop described below) turns it into a gate: a test or a commit-hook rule. The prose rule for it in CLAUDE.md is then no longer needed.
- Each cycle closes with five metrics: bugs review found, regressions introduced by fixes, old bugs in code from before Ennyn, bugs a gate caught, and bugs that got past the commit and turned up later. It also measures whether the instruction text loaded in every session grew.
- Tasks live in a work graph, a JSON file. Ennyn picks four per cycle and always keeps a slot for the oldest high-value task.

Ennyn has no runtime dependencies and no install scripts. It makes network requests in only two cases. When a commit adds packages to a lock file, the commit hook looks them up on the npm registry (turn that off with `security.deps.online: false`). The `ennyn deps` command queries the OSV vulnerability database when you run it. More in [SECURITY.md](SECURITY.md).

The reasoning behind Ennyn's design is in [docs/evidence.md](docs/evidence.md).

## Try it without installing

Two commands work in any git repository without a config. Clone Ennyn next to your project, then run these from your project's root:

```sh
node ../ennyn/scripts/ennyn.mjs rework
node ../ennyn/scripts/ennyn.mjs budget
```

`rework` reports the share of commits whose lines a fix commit changed within 7 days. `budget` measures the size of the instruction text (CLAUDE.md, rules, and skill and agent descriptions) your agent loads in every session.

## Install (Claude Code)

```sh
claude plugin marketplace add boranb/ennyn
claude plugin install ennyn@ennyn
```

Then run `/ennyn:init` in your project. It scans the repository, asks a few questions, and sets up `.ennyn/`. In your other projects, the plugin's hooks do nothing except note the plugin's version in the plugin's own folder.

Install Ennyn only from `github.com/boranb/ennyn`, with the commands above or from a clone. The real thing has no binaries, no runtime dependencies and no install scripts. A copy that ships an executable, or asks you to run a setup program, is not Ennyn.

### Update

```sh
claude plugin marketplace update ennyn
claude plugin update ennyn@ennyn
```

Restart Claude Code afterwards. A commit-msg hook installed from the plugin follows the new version by itself; there is nothing to run again in your projects. With a clone, `git pull` is enough.

### Remove

First, in each project where you ran `/ennyn:init`, remove the commit-msg hook and Ennyn's state folder. In a Claude Code session, ask the agent to run `node "$ENNYN_PLUGIN_ROOT/scripts/ennyn.mjs" uninstall-hook`; with a clone, run `ennyn uninstall-hook`. It removes the hook only if `install-hook` wrote it and nobody has changed it since. A hook you edited, or one in a tracked hooks folder or husky's, stays: the command says which file and which lines to take out. It then removes `.git/ennyn` and lists what stays for you to decide: `.ennyn/config.json`, the work graph, the handoff, the metrics and findings logs, and the ask rules init added to `.claude/settings.json`. Delete those or keep them; they are ordinary files in your repository.

Then remove the plugin, and the marketplace it came from:

```sh
claude plugin uninstall ennyn@ennyn
claude plugin marketplace remove ennyn
```

Uninstalling the plugin also deletes its data folder, where the hook looks up the plugin's version. A hook left behind in some project then lets every commit through with a note; `uninstall-hook` from a clone still removes it. `--keep-data` keeps that folder, and with it a hook that points at a version Claude Code deletes after 14 days, after which every commit is refused, so remove the hooks first.

The cycle skill in `skills/cycle/` follows the [Agent Skills](https://agentskills.io) format, but it calls the CLI through `${CLAUDE_PLUGIN_ROOT}`, which only Claude Code sets. To use it with another agent, set `CLAUDE_PLUGIN_ROOT` to the path of an Ennyn clone. The CLI needs Node 22 or later and git 2.34 or later, and has no dependencies. From the Ennyn clone, `node scripts/ennyn.mjs --help` lists its commands. Elsewhere in this README, `ennyn` is short for that script, run from your project.

Ennyn runs on Linux and macOS, and on Windows through WSL, where the whole test suite last passed on 2026-11-09, at commit `c5d7b70` (Ubuntu 22.04, git 2.34.1). On macOS 27.2 (Node 22.23.4, git 2.56.0) the whole suite last passed on 2026-11-22, at `v0.1.1`, and on Linux the same day in containers at the floor (Node 22.0.0, git 2.34.1) and on Node 24.22.1 (git 2.39.5). On native Windows (Git for Windows 2.47.1, Git Bash, PowerShell 7) the push hook, the commit-msg hook, the gate-loosening check and the plugin's version record were last measured on 2026-11-05, at commit `41cfa37`, and hold, as [SECURITY.md](SECURITY.md) says; the test suite does not pass there, the compaction hook was only tried on a test project, and the other hooks were not measured.

## How a cycle runs

Before the first edit, the agent runs `ennyn impact`. This is its output for a change to Ennyn:

![Output of ennyn impact for a change to Ennyn](docs/assets/impact.png)

The steps of a cycle, and the settings that apply to them:

| Step | What happens | Commands |
|---|---|---|
| Setup | `/ennyn:init` looks at the repository before asking anything: how fixes are labeled, which files most commits rewrite (usually generated output), where the tests are, which paths are risky, and whether the project has a roadmap or issues. Then it asks up to six questions and writes the config, a starting work graph, and a handoff note for the next session. In a new project, one holding only a README, a licence, `.gitignore` and agent instruction files, it asks only what the config and a first graph need; outside a repository it proposes `git init`. It also reports how the agent handles secrets (bypass, the sandbox, Read rules for `.env` and SSH keys, tokens in `.mcp.json`) and offers to run without bypass; nothing changes unless you say yes. | `/ennyn:init`, `ennyn init-scan`, `ennyn doctor` |
| Picking work | Each cycle takes four tasks. One is always the oldest high-value task, so large tasks aren't starved (if it's too big, its first step goes in instead). The other three are the task with the best value for its cost, one that turns the most common kind of bug into a gate, and an audit of something already finished. Asked for one task by name, or for one fix (written as a task first), the cycle runs it alone with the same steps and the same end of cycle, without the gate task and the audit. | `ennyn core`, `ennyn mechanization` |
| Before writing | The impact table. Each of the five questions is answered by a command where possible (git grep, git log, or the tests), and a row no command can answer says so. If the change adds a heuristic, the agent first writes examples the heuristic should accept and reject, plus a failing test. A task picked for its value also answers a smallest-change row first: which line of the task asks for each new piece, and what the repository, the platform, git or an installed dependency already does for it. Input checks, data-loss handling, security and accessibility are never cut. | `ennyn impact` |
| Mutation testing | The agent picks a few mutants (small, deliberate bugs) for the changed lines, and the project's fast tests run once per mutant. A surviving mutant, one the tests miss, needs a new test or a written reason. Files are restored afterward, even if the run is interrupted. If someone edits a file while a mutant is in it, Ennyn leaves that file as it is and stops the run. | `ennyn mutate` |
| Heavy jobs | A whole test suite, a mutation run or a platform image waits its turn in one queue on your machine, shared by every session and project, and runs under a time limit. Its turn starts only when the machine has room: enough free memory and disk, and a load the CPUs can carry; until then it keeps its place, says what is short, and after its time limit starts anyway. A run that hangs is stopped along with everything it started, and a run that died gives the queue back. | `ennyn lock` |
| Review | Two rounds; a third only with a failing test or a measurement. Every finding quotes the code, names its source (new code, an earlier fix, or older code), and says how it was checked. | `agents/`, `skills/cycle/finding-schema.md` |
| Commit | A commit-msg hook checks every commit. It blocks patterns you've banned (`review.forbidden`) and secrets in known token formats, and warns when code changes but the docs tied to it don't (`review.cochange`). | `ennyn commit-check`, `ennyn install-hook` |
| Pushes | A hook refuses a `git push` in a command Claude Code's ask rule can't read for certain, and tells the agent how to write it. This catches habit, not a determined program. | Claude Code hook |
| Gate timing | How long the commit checks take and how often they fail, recorded on your machine. | `ennyn gate-record`, `ennyn gate-stats` |
| Tone | You choose how the agent talks to you (`focused` or `terse`) and how long commit messages are. Numbers, paths, and warnings are never cut. | `conversation.style`, `commitMsg.style` |
| Worktrees | When the agent works in a git worktree or a copy of the project, it still gets the project's path-specific rules. | Claude Code hook |
| Compaction | Claude Code doesn't summarize a session you left in the middle of a task with its turn ended: idle compaction waits for a commit. Compaction a session needs goes ahead as usual, and every summary is asked to name the task, its files and what comes next. After a compaction the agent is asked to re-read the files its task changed and its impact table before the next edit. `compaction.defer: false` turns all three off. | Claude Code hook, `compaction.defer` |
| End of cycle | You get the five metrics, and the most common kind of bug becomes the next cycle's gate task. The agent cleans up one lesson file (the project's written notes on past mistakes) and deletes the lessons a gate now covers. It also checks dependencies and CI files, and lists what the cycle left in the work tree (new untracked files, changes not committed) along with your project's own leftover tool if you name one, asking you about each and deleting nothing. It removes the worktrees the cycle made when nothing in them would be lost. Every few cycles there's a security audit. The agent asks before pushing, unless you set `push.mode` to `after-closing`. | `ennyn push-check`, `ennyn rework`, `ennyn bypass`, `ennyn budget`, `ennyn deps`, `ennyn leftovers`, `ennyn worktrees`, `ennyn audit` |

`ennyn rework` depends on how your project labels fixes. If most commit subjects start with "fix", it ends up measuring churn more than rework, and says so. Set `metrics.fixSubject` to match your real repair commits; that pattern also has to match `commitMsg.fixType` ([details](docs/evidence.md#speed-and-rework)).

## Configure

All settings live in one file, `.ennyn/config.json`, which `/ennyn:init` writes for you. You only set what differs from the defaults. Unknown keys and wrong types are reported all at once, so a typo can't quietly switch a check off. Paths in the config have to stay inside the project.

```json
{
  "language": "en",
  "paths": { "graph": ".ennyn/graph.json" },
  "commitMsg": { "types": ["feat", "fix", "docs", "test", "refactor", "chore"], "fixType": "fix" },
  "review": { "impactRequiredGlobs": ["src/auth/**", "migrations/**"] },
  "impact": { "twins": [["src/lib/engine", "server/src/lib"]] }
}
```

`language` (`en` or `tr`) sets the language of reports and of the agent's replies. Commit messages follow `commitMsg.language`, so you can talk in Turkish and commit in English. The hook accepts the commit types in `commitMsg.types`, and `commitMsg.fixType` is the type reserved for repairs of earlier commits, the ones `ennyn rework` counts. `/ennyn:init` sets the types and the fix type, and they override any commit rules in your own instructions. The full list of keys is in [DESIGN.md](DESIGN.md).

The work graph is a JSON file (or an ES module; the commands that read it import and run that module, so a cloned project's graph module is code to review) with two arrays, one for open tasks and one for done tasks. Field names can be configured, so you can point Ennyn at a graph you already have.

## When Ennyn does not fit

- It runs in Claude Code only for now.
- Rework is only as good as the fix label: `ennyn rework` counts commits whose subject carries the fix type, so a project that does not mark repairs gets a number that means little.
- It needs Node 22 and git 2.34 or newer for now.
- The config may change before 1.0.

## Glossary

- **Work graph**: the file of open and done tasks the cycle picks from.
- **Cycle**: one run of four tasks from the graph, ending in a report and a handoff.
- **Gate**: a check that refuses (the commit hook, a permission rule, a test the commit must pass), as opposed to advice the agent is told to follow.
- **Mechanization**: the cycle's task that turns a kind of bug that keeps coming back into a gate, a test, a type or a lint rule.
- **Legacy audit**: the cycle's task that re-checks a feature already finished, or the project's security.
- **Side copy**: a copy of the project in another directory (a scratch folder or a worktree) where an agent works; the project's rules follow it there.
- **Convergence**: the report at the end of a cycle that counts findings by where they came from, so you can see whether review is finding fewer new problems.
- **Impact table**: the short table written before a risky change, listing what else reads or depends on the thing being changed.

## Settings you may change

| Setting | What it changes |
|---|---|
| `language` | Language of reports, CLI output and the agent's replies (`en` or `tr`). |
| `conversation.style` | How the agent talks to you: `focused` or `terse` (`normal` is the default). Numbers, paths and warnings are never cut. |
| `commitMsg.language`, `commitMsg.style` | Language of commit text, and `terse` to keep the body to structured lines. |
| `push.mode` | Who says yes to the closing's push: `ask` (you, the default) or `after-closing`. |
| `compaction.defer` | Whether idle compaction waits while a task is half done (default on). |
| `review.agents` | The reviewer agents a cycle uses; empty means Ennyn's three. |

No setting turns a gate off. The full list of keys is in [DESIGN.md](DESIGN.md).

## Status and roadmap

- **0.1** (2026-11-18): the first public release, with the plugin, `/ennyn:init`, and the CLI.
- **0.2**: Codex support, `claude plugin eval` cases that compare a project with and without the plugin, published results from a second project, a terminal runner for unattended cycles, output masking for secrets, and a triage of the backlog.
- **1.0**: a stable config format.

## License

MIT. See [LICENSE](LICENSE).

## Name

*Ennyn* (pronounced *EN-nin*) means "gates" in Sindarin. It's the first word of the inscription on the Doors of Durin in *The Lord of the Rings*, which open only for the right word. In Ennyn, the checks your code has to pass are called gates.

The name has its own short policy in [TRADEMARK.md](TRADEMARK.md). Ennyn is not affiliated with, sponsored by, or endorsed by the Tolkien Estate, Middle-earth Enterprises, or any of their licensees.
