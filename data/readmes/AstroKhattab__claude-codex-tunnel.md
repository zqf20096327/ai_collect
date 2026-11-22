# claude-codex-tunnel

**Let Claude Code and OpenAI Codex hand work to each other, and watch them talk.**

Claude writes the code, and Codex reviews it. Or Codex builds, and Claude checks.
One model family checks the other's work. Each side asks the other in plain
language, and you watch the whole conversation live in a terminal window.

A real run, as the conversation window shows it (shortened):

```
── Claude → Codex · Review calc.py ─────────────────────────────────────────
  12:22:30 · role review · sandbox read-only
  Goal:
    Find real bugs in calc.py.
  Definition of done:
    1. Every bug is listed with file:line, severity and a concrete fix.
    2. Edge cases: empty list, zero whole.
  Codex:
    I'll inspect calc.py and check the empty-list and zero-total cases without changing files.
  Codex runs $ nl -ba calc.py
      exit 0
  Codex runs $ python3 -B -c 'import calc ...'
      exit 0
      average([],) -> ZeroDivisionError: division by zero
      average([2, 4],) -> 3.0
      percent(5, 0) -> ZeroDivisionError: division by zero

  Codex → Claude: REVISE   (35s, exit 0)
    Found two division-by-zero bugs in calc.py.
    Empty lists crash `average`; zero totals crash `percent`.
    Reproduced both failures and verified four ordinary cases.
  ❓ question: The brief does not specify the desired result for undefined averages ...
  report: .tunnel/reports/20261121-232213-review-calc.codex.report.md
```

- **Works both ways.** Claude → Codex, and Codex → Claude.
- **Real integration.** It starts the other CLI as a real process (`codex exec` or
  `claude -p`). No server, no API keys, no MCP setup. It uses the CLIs you already
  signed in to, and your existing plans.
- **Live conversation window.** A terminal pops up and shows each brief going out,
  every command the other AI runs, and the verdict coming back.
- **Safe by default.** Reviews run read-only. Writing runs are sandboxed. Nothing
  commits, pushes, deploys or deletes. Those go back to you as *Needs human approval*.
- **One file is the whole channel.** The task is a markdown brief, and the answer is
  a markdown report with a verdict. You can read exactly what was asked and answered.

## Install (1 minute)

You need [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and/or the
[Codex CLI](https://github.com/openai/codex), signed in, plus `git` and `python3`.

```bash
git clone https://github.com/AstroKhattab/claude-codex-tunnel.git
cd claude-codex-tunnel && ./install.sh
```

That installs:

| What | Where |
|---|---|
| the `tunnel` command | `~/.local/bin/tunnel` (a link into this folder, so `git pull` updates it) |
| a skill that teaches Claude to delegate to Codex | `~/.claude/skills/claude-codex-tunnel/` |
| two Claude subagents: `codex-builder`, `codex-reviewer` | `~/.claude/agents/` |
| a skill that teaches Codex to delegate to Claude | `~/.agents/skills/claude-codex-tunnel/` |

The installer asks whether Claude and Codex may run `tunnel` without asking each
time (`--trust` / `--no-trust` skip the question). Restart Claude Code and Codex,
then check:

```bash
tunnel doctor          # is everything installed?
tunnel doctor --live   # do both engines answer? (spends a few tokens)
```

**Let your AI install it.** Paste this into Claude Code or Codex:

> Clone https://github.com/AstroKhattab/claude-codex-tunnel, run its `install.sh --trust`,
> then run `tunnel doctor` and tell me the result.

**One project only, shared with your team:** `./install.sh --project /path/to/repo`
puts the skills inside that repo (`.claude/` and `.agents/skills/`) so they travel with git.

## Use it

Just ask, in your own words:

| In Claude Code | In Codex |
|---|---|
| "Ask Codex to review my last commit." | "Ask Claude to review my last commit." |
| "Have Codex implement the plan in PLAN.md." | "Have Claude write tests for parser.py." |
| "Get a second opinion from Codex on this bug." | "Get a second opinion from Claude on this design." |

The agent writes a brief, runs `tunnel`, pops up the conversation window, waits,
reads the report and tells you the verdict.

## How it works

```
 Claude Code                                         Codex CLI
 ───────────                                         ─────────
 writes .tunnel/tasks/<id>.task.md   (the brief)
 runs  tunnel codex <brief> --window ─────────────▶  codex exec --sandbox read-only|workspace-write
                                                      reads the brief + the tunnel protocol
                                                      works in its sandbox
 reads .tunnel/reports/<id>.codex.report.md ◀──────── final message = the report
 acts on the verdict
```

Codex → Claude is the same, mirrored: `tunnel claude <brief>` runs `claude -p`.

Everything lives in `.tunnel/` in your project (git-ignored automatically):

```
.tunnel/
  tasks/<id>.task.md                 the brief (who, role, scope, done-criteria)
  reports/<id>.<engine>.report.md    the answer, starting with "## Verdict: ..."
  logs/<id>.<engine>.jsonl           the raw live event stream
  threads/<id>.<engine>              session id, to resume the same conversation
  bus.jsonl                          append-only record of every run
```

### Verdicts

| Verdict | Meaning |
|---|---|
| `DONE` | Work complete, done-criteria met |
| `APPROVE` | Review passed, against named criteria |
| `REVISE` | Fixable issues, each with file:line and a fix |
| `BLOCK` | Cannot proceed: missing information or real risk |
| `FAILED` | The run errored (the report shows the log tail) |

### The rules every worker follows

1. The brief is the whole channel. If something is missing, it says `BLOCK`, not guesses.
2. Scope is a fence: it edits only the files the brief allows.
3. No commits, pushes, migrations, deploys, deletions or outbound actions.
4. The author never certifies its own work.
5. `APPROVE` must name the criterion it checked.
6. It never weakens or skips a test to get to green.
7. It does not start another tunnel run unless asked (and nesting is capped).

## Commands

```bash
tunnel new <slug> --to codex|claude [--role implement|review|test|research]
tunnel codex  <brief> [--window] [--detach] [--resume <id>]
tunnel claude <brief> [--window] [--detach] [--resume <id>]
tunnel watch [--window]            # the live conversation, here or in a new window
tunnel wait <run-id>               # collect a --detach run
tunnel status                      # running and recent runs with verdicts
tunnel dispatch [-p N] a.task.md b.task.md   # run briefs in dependency waves
tunnel board                       # a live web board at http://localhost:7799
tunnel doctor [--live]
```

`review` and `research` briefs run read-only. `implement` and `test` briefs may edit.

## Settings

| Variable | What it does |
|---|---|
| `TUNNEL_CODEX_MODEL` | Codex model to use, e.g. if your default is not on your plan |
| `TUNNEL_CODEX_EFFORT` | Codex reasoning effort: `low`, `medium`, `high` |
| `TUNNEL_CODEX_PROFILE` | a Codex profile (`$CODEX_HOME/<name>.config.toml`) |
| `TUNNEL_CLAUDE_MODEL` | Claude model, e.g. `sonnet` or `opus` |
| `TUNNEL_CLAUDE_ALLOW` | extra tools for writing Claude runs, e.g. `Bash(npm test:*)` |
| `TUNNEL_NETWORK=1` | let writing Codex runs use the network (off by default) |
| `TUNNEL_WINDOW=1` | always pop up the conversation window |
| `TUNNEL_NOTIFY=0` | no desktop notifications |
| `TUNNEL_MAX_DEPTH` | how deep tunnels may nest (default 2) |

A brief can also add `allow: Bash(npm test:*)` to its frontmatter, so a Claude
worker may run that one command for that one task.

## Safety model

| Run | Codex | Claude |
|---|---|---|
| review / research | `--sandbox read-only` | read, grep and read-only git only; edits refused |
| implement / test | `--sandbox workspace-write` (this repo + `.tunnel/`), no network | file edits allowed; shell limited to read-only git plus what you `allow` |

- Codex calling Claude: Claude needs the network and its own sign-in, so that one
  command runs outside Codex's sandbox. With `--trust`, the installer adds a Codex
  rule that allows exactly the `tunnel` command. Without it, Codex asks you first.
- Claude calling Codex: with `--trust`, Claude Code may run `Bash(tunnel:*)`.
- Two writing runs on the same files at once will collide. Use `tunnel dispatch`
  with `depends_on:` or separate git worktrees.

## Troubleshooting

- **Codex says the model is not supported.** Your Codex default model is not on your
  plan. Set `TUNNEL_CODEX_MODEL` to one that is, then `tunnel doctor --live`.
- **A run is FAILED with no report.** The report includes the last lines of the
  engine log. The full stream is in `.tunnel/logs/`.
- **No window pops up.** On macOS it uses Terminal (or iTerm). On Linux it tries
  `x-terminal-emulator`, `gnome-terminal`, `konsole` and `xterm`. You can always
  run `tunnel watch` in any terminal.
- **The agent's tool call timed out.** Long runs: `tunnel codex <brief> --detach`,
  then `tunnel wait <run-id>` (returns exit 124 while still running; call again).

## Uninstall

```bash
./uninstall.sh        # removes the command, skills, subagents and trust entries
```

Your projects' `.tunnel/` folders are left alone.

## Tests

```bash
tests/run.sh          # offline: fake codex/claude, throwaway HOME, no credit spent
```

CI runs it on Ubuntu and macOS (stock bash 3.2).

## License

MIT. See [LICENSE](LICENSE).

Not affiliated with Anthropic or OpenAI. "Claude" and "Codex" are trademarks of
their owners.
