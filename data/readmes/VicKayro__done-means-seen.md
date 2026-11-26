<p align="center">
  <img src="assets/hero.svg" width="100%" alt="A terminal. Claude says the settings page is done. The Stop hook runs the typecheck, finds an error and sends Claude back to work while the andon light turns red. Claude fixes it, the check turns green, and Claude reports done again, after saving a value, reloading the page and seeing it stick.">
</p>

<p align="center">
  <b>When Claude says it's done, this hook reruns your typecheck and tests,<br>and sends Claude back to work if they fail.</b>
</p>
<p align="center">
  Plus the rules that go with it, and Andon: a log of what your agents got wrong<br>that never accepts the same fix twice.
</p>

<p align="center">
  <a href="https://github.com/VicKayro/done-means-seen/actions/workflows/tests.yml"><img alt="tests" src="https://img.shields.io/github/actions/workflow/status/VicKayro/done-means-seen/tests.yml?branch=main&label=tests&style=flat-square&labelColor=0d0d0c&color=35d07f"></a>
  <img alt="python 3.9+" src="https://img.shields.io/badge/python-3.9%2B-ecebe6?style=flat-square&labelColor=0d0d0c">
  <img alt="zero dependencies" src="https://img.shields.io/badge/dependencies-0-ecebe6?style=flat-square&labelColor=0d0d0c">
  <a href="https://docs.claude.com/en/docs/claude-code/hooks"><img alt="Claude Code Stop hook" src="https://img.shields.io/badge/claude_code-stop_hook-ffb224?style=flat-square&labelColor=0d0d0c"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-ecebe6?style=flat-square&labelColor=0d0d0c"></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#how-the-hook-decides">The hook</a> ·
  <a href="#andon">Andon</a> ·
  <a href="#receipts">Receipts</a> ·
  <a href="#faq">FAQ</a>
</p>

---

## Why

For months my real job was being the tester of my own Claude Code agents: *"done!"*, I open it, it doesn't work, I paste the error back, and again. (I run an AI consulting company in France, and I'm not a developer.)

On 21/10/2026, after a talk called *Stop babysitting your agents*, I wrote one rule, then the few pieces of code that make it hard to skip. This is what runs on my Mac today, across 28 projects.

## Install

```bash
git clone https://github.com/VicKayro/done-means-seen && cd done-means-seen
./install.sh --dry-run   # shows every action, writes nothing
./install.sh
```

It installs into `~/.claude`, backs up anything it replaces, never overwrites your `CLAUDE.md` or `verify.json`, and ships the hook **switched off**. Then:

1. Tell the hook what "it works" means for each project, in `~/.claude/verify.json`:
   ```json
   { "name": "web-app", "repo": "you/web-app",
     "static": ["npm run typecheck", "npx eslint {changed}"], "changed_glob": ["src/*.ts", "src/*.tsx"] }
   ```
2. Replay a past session without blocking anything (the installer prints the exact command for your latest one):
   ```bash
   python3 ~/.claude/hooks/verify_on_stop.py --dry-run ~/.claude/projects/<project>/<session>.jsonl
   ```
3. When the replay looks right, switch it on: `"guard_enabled": true`.

Python 3.9+, macOS or Linux, no dependencies.

## The four rules

They live in [`CLAUDE.md`](CLAUDE.md), written from Claude's side:

1. **"Done" means I have seen it work.** Run it for real and see the effect: a screen, a log line, a row, a file. Re-reading the code does not count.
2. **I loop on my own until it passes.** I stop only on a real blocker (a missing secret, production access, a decision that belongs to the human) and name it in one sentence.
3. **I never make the human test in my place.** They get the proof, and whatever is still unverified, said plainly.
4. **Verification never touches production.** Local, preview, branch or dry run.

Rules in a prompt get ignored on a bad day. The rest of this repo is what happens when they are.

## How the hook decides

Claude Code runs [Stop hooks](https://docs.claude.com/en/docs/claude-code/hooks) when the model is about to end its turn. [`verify_on_stop.py`](hooks/verify_on_stop.py):

- reads the session transcript and finds the files Claude wrote to, through the edit tools and through shell commands that write (`sed -i`, heredocs, redirections, `git commit`, `mv`, `cp`),
- maps them to projects in `~/.claude/verify.json`, by GitHub repo or by folder,
- runs each project's `static` commands, where `{changed}` expands to the changed files only, so a lint reads what changed and nothing else,
- on red, exits with code 2, and Claude gets this (a real run, on a real TypeScript error):

```
ERROR: the check for web-app fails after your changes.
  command: npm run typecheck
--- end of output ---
> typecheck
> tsc --noEmit

src/settings.ts(4,9): error TS2322: Type 'string' is not assignable to type 'Timezone'.
---
WHY: "done" means the checks are green (CLAUDE.md, rule 1).
FIX: read the output, fix the cause, and hand back: the check reruns by itself.
If the failure is not caused by your changes (it was there before, or comes from another session),
say so in one line in your answer and hand back without changing anything: the hook will let you through.
(block 1 of 3 for this request)
```

It is built so it never becomes the thing you babysit:

| Rule | Why |
|---|---|
| **Green is remembered** | A project already verified in the same state (same commit, same diff) is skipped. Most turns cost nothing. |
| **One block per red state** | If Claude stops again without changing anything, it has decided the failure isn't from its changes, and it must say so in its answer. |
| **Three blocks per request** | After that the turn ends anyway, with its own line in the log, so a broken environment can't trap Claude in a loop. Your next message starts a fresh count. |
| **Never blocks for its own failure** | Missing tool, timeout, unreadable config: one line in the log, and the turn ends. |

## Andon

Every complaint about one of your agents gets logged with its cause and its fix. If the same problem comes back, the tool refuses another fix at the same level: words that didn't hold have to become code.

<p align="center">
  <img src="assets/ladder.svg" width="100%" alt="The Andon ladder, weakest first: 1 instruction, 2 example, 3 guardrail, 4 mechanism, 5 standard. Instructions and examples are words a model can ignore; guardrails, mechanisms and standards are code.">
</p>

On a Toyota line, the andon is the cord anyone pulls when something is wrong: the line stops, someone comes, and it only restarts once the cause is dealt with. Here the cord is a complaint, like *"the project bot posts too much"* or *"you told me it was done and it wasn't"*. It becomes an entry with its cause (one of 10, such as *noise*, *wrong*, *silence* or *trust*), the fix, and a date to check whether the fix held.

On the [example registry](andon/registry.example.json) (fictional), the project bot got chatty again after a fix that changed how it posts. Someone tries to answer with a prompt edit:

```
$ andon add < complaint.json      # cause: noise, fix: "Prompt says: only post when something changed."

REFUSED: Recurrence of A002: the last countermeasure went up to level "mechanism" and the cause came back.
Go above it (standard), or say plainly that it is a different defect (different_defect),
or write why this level is enough this time (same_level).
```

It also refuses to mark a fix as held without proof, because silence is not proof. `andon review` lists what's due: fixes to check, what's waiting on whom, problems that came back. The [skill](andon/SKILL.md) teaches Claude Code the whole loop, from "someone told me" to the message back to that person.

```bash
ANDON_REGISTRY=andon/registry.example.json andon review
```

## Receipts

<p align="center">
  <img src="assets/receipt.svg" width="420" alt="Receipt, Oct 21 to Nov 23, 2026. Stop hook: 171 sessions, 386 checks green at end of turn, 16 red when Claude tried to stop, 8 sent back to work, 198 could not judge. Andon: 71 complaints logged, 0 fixes that are just a prompt, 8 came back and were forced up a level, 7 complaints about Claude itself. Silence is not proof.">
</p>

**16 times in 33 days, Claude tried to end its turn on a red check.** That's from my own logs. 8 times it was sent back to work. The other 8 got through, because the block counter was per session and two long sessions had used their 3 blocks on earlier requests: a reader spotted it in the code the day this repo went public. Since 0.2.0 the count is per request, and replayed on the same log, all 8 would have been blocked. The 198 turns it could not judge are explained under [Limits](#limits).

In Andon, none of the fixes is just a prompt edit, 8 problems came back and were pushed one level up, and 7 of the 71 complaints are about Claude Code itself. Whether the fixes hold is the next number: the first checks come due this week. Until then the registry can only count what came back, not what held, and this section will be updated.

## FAQ

**Does it slow Claude down?** A state already green is skipped, so most turns cost nothing. A red check costs what your commands take: on my projects, 2 seconds for a static site, 12 for a typecheck, 32 for a test suite. The hook never calls a model.

**Can it loop forever?** No. The same red state blocks once, a request gets 3 blocks, and Claude Code itself stops after 8 Stop-hook blocks in a row (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` changes that ceiling).

**What if the failure isn't Claude's?** It says so in one line and hands back. The same red state never blocks twice.

**Does the hook look at the UI?** Only through your commands: put your Playwright suite in `static` (there's one in the [example map](config/verify.example.json)) and an end-to-end run becomes part of "done". Seeing the screen is also Claude's job under rule 1, the last line of the animation above.

**Why not `/goal`?** Use both. `/goal` is for one task: you type a condition, and a separate model judges after each turn whether it's met. This hook is always on, in every session, and judged by exit codes.

**Why not a pre-commit hook?** Keep yours. Claude says "done" long before anything gets committed, and often nothing does. The hook runs when the turn ends, skips states already green, and `{changed}` lints only what changed.

**Why rules in `CLAUDE.md` and not a skill?** A skill loads when the model decides it's relevant, and these rules are for the moment it decides they aren't. The file is about 1,500 tokens.

**Can I use one piece without the others?** Yes. The rules, the hook and Andon are independent.

## What's inside

| Path | What it is |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | The rules: four hard ones, the loop on every change, parallel agents, background loops, complaints. |
| [`hooks/verify_on_stop.py`](hooks/verify_on_stop.py) | The Stop hook. |
| [`config/`](config/) | Example `verify.json`, and the `settings.json` wiring. |
| [`andon/`](andon/) | The registry CLI, the Claude Code skill, a morning round that only wakes a model when something is due, and the example registry. |
| [`install.sh`](install.sh) | The installer: backups, safe to rerun, hook born switched off. |
| [`hooks/`](hooks/) | Two helpers from my own setup: a syntax check for script folders with no tests, and a fix for `node_modules` stored in iCloud. |

## Limits

- When a check can't even start (typically an agent's worktree with no dependencies installed), the hook lets the turn end rather than guess. On my machine that was 198 turns in 33 days.
- Detecting writes in shell commands is a regex heuristic. It errs on the side of checking: a read-only script fed through a heredoc from inside a project counts as a write to that project, so you may get blocked on a failure someone else left there. That's what the "say it's not yours" escape is for.
- One request can use its 3 blocks and end on red. The log says so, in its own line.
- The Andon registry is one JSON file in a git repo, for one person.

## Contributing

The most useful issue is a case where the hook got it wrong: a write it missed, or a read it took for a write. See [CONTRIBUTING.md](CONTRIBUTING.md). Tests: `uv run --with pytest python -m pytest -q tests/ andon/tests/`.

## See also

[Leash](https://github.com/VicKayro/leash): see what your agents did last night (costs, loops, dead crons), one `npx` command.

---

<sub>MIT · Visuals set in DM Mono ([SIL Open Font License](assets/OFL-DM-Mono.txt)) · Built with Claude Code, obviously.</sub>
