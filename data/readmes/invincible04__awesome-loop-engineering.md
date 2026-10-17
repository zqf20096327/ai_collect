<div align="center">

<img src="assets/loop-engineering.png" alt="Loop Engineering: build the loop that prompts your agents" width="880">

<h1>Awesome Loop Engineering</h1>

<p><b>Learn loop engineering</b>: the practice of designing systems that prompt, check,<br>remember, and re-run AI coding agents <i>for</i> you, instead of prompting them by hand, turn after turn.</p>

<p>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-CF4520?style=flat-square" alt="MIT License"></a>
<a href="https://invincible04.github.io/awesome-loop-engineering/"><img src="https://img.shields.io/badge/read_it-online-1A1714?style=flat-square" alt="Read it online"></a>
<a href="skill/loop-engineering/"><img src="https://img.shields.io/badge/agent_skill-included-CF4520?style=flat-square" alt="Agent skill included"></a>
<a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-1A1714?style=flat-square" alt="PRs welcome"></a>
<a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
</p>

<p>
<a href="https://invincible04.github.io/awesome-loop-engineering/"><b>Website</b></a> &nbsp;&middot;&nbsp;
<a href="docs/"><b>Learn</b></a> &nbsp;&middot;&nbsp;
<a href="prompts/"><b>Prompts</b></a> &nbsp;&middot;&nbsp;
<a href="skill/loop-engineering/"><b>Build your own loop</b></a> &nbsp;&middot;&nbsp;
<a href="CHEATSHEET.md"><b>Cheat sheet</b></a>
</p>

</div>

---

This is a **teaching repo**, not a link dump. It has four parts:

1. **[Learn](docs/)** — in-depth, plain-language chapters that explain loop engineering from first principles.
2. **[Read](reading-list.md)** — a large, annotated reading list (~100 sources): the essays that named the field, the papers it stands on, the evals/observability canon, the talks, and the skeptics.
3. **[Practice](prompts/)** — a library of **real, copy-paste loop prompts** (Ralph loops, `/goal` and `/loop` commands, Codex automations, maker/checker sub-agents, verifier rubrics, and full loop contracts).
4. **[Build](skill/loop-engineering/)** — a portable **agent skill** that walks you through designing and scaffolding a loop for *your own* workflow, plus a small **[runnable example](examples/)** in plain Python.

**Fast paths:**

- 🌐 **[Website](https://invincible04.github.io/awesome-loop-engineering/)** (the one-page tour)
- 🛑 **[When *not* to build a loop](docs/00-when-not-to-loop.md)** (the decision rule + readiness scorecard)
- 🧩 **[Build a loop for your workflow](skill/loop-engineering/)** (the skill)
- 📄 **[Cheat Sheet](CHEATSHEET.md)** (the whole field on one page)
- 📊 **[Case studies](docs/11-case-studies.md)** (real loops, real numbers)
- ❓ **[FAQ](FAQ.md)** (is this just cron? is prompting dead?)
- 🛠 **[Hands-on: Claude Code / Codex / Cursor / OpenCode](docs/10-building-loops-claude-code-and-codex.md)**
- 🧠 **[Field Notes](FIELD-NOTES.md)** (13 hard-won lessons)

---

## What is loop engineering, in one paragraph

For two years, getting work out of a coding agent meant writing a prompt, reading the reply, and typing the next prompt — you held the tool the whole time. **Loop engineering replaces *you* as the thing that prompts the agent.** You build a small system that discovers work, hands it to an agent, checks the result with a *separate* verifier, writes down what's done, decides what's next, and re-runs on a schedule. As Addy Osmani put it in the essay that named the field (June 2026): *"Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go."*

The two quotes that kicked it off:

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — **Peter Steinberger**

> "I don't prompt Claude anymore. I have loops running. They're the ones prompting Claude and figuring out what to do. My job is to write loops." — **Boris Cherny**, creator of Claude Code

## Who this is for

- **You use a coding agent daily** (Claude Code, Codex, Cursor) and you're tired of being its full-time hand-cranker.
- **You keep re-typing the same prompts** ("fix the failing tests", "triage the new issues") and suspect a machine should be doing the typing.
- **You want the leverage without losing the plot** — to automate the inner loop while staying the engineer who owns verification, comprehension, and intent.

No prior "agent" theory required. If you can write a shell `while` loop and read a diff, you can start.

## Where it sits: the lineage

Loop engineering is the newest floor in a four-story stack. Each layer makes the one below it more useful:

| Layer | The question it answers |
|-------|-------------------------|
| **Prompt engineering** | What should I *say* to the model? |
| **Context engineering** (Karpathy) | What state and knowledge should the model *see*? |
| **Harness engineering** | What tools, permissions, tests, and sandboxes should *surround* one agent run? |
| **Loop engineering** | What recurring *system* should discover, delegate, verify, persist, and re-run — when the human is no longer in the inner loop? |

Prompt, context, and harness make *one run* better. The loop makes *recurring work* reliable, observable, and governable. → Full explanation in **[docs/02 — The Lineage](docs/02-the-lineage.md)**.

## The shape of a loop

```text
Objective
  │
  ▼
Trigger / cadence            ← an automation fires the loop (the "heartbeat")
  ▼
Discover / intake work       ← read CI failures, issues, alerts, a task list
  ▼
Delegate to an agent         ← the "maker" proposes a change
  ▼
Act in an isolated workspace ← a git worktree, so parallel agents don't collide
  ▼
Verify with a SEPARATE checker  ← tests, lint, an independent reviewer agent (the "/goal")
  ├── fail → feed the evidence back and retry
  └── pass → persist state, then decide what's next
  ▼
Repeat — or stop on: goal met · budget spent · stalled · needs-a-human
```

A loop is **not** a cron job. A cron job repeats blindly; a loop *discovers, verifies, persists, and decides what's next* — and stops for an honest reason. → **[docs/03 — Anatomy of a Loop](docs/03-anatomy-of-a-loop.md)**.

## Start here (a reading path)

In a hurry? The **[Cheat Sheet](CHEATSHEET.md)** is the whole field on one page, and the **[FAQ](FAQ.md)** clears up the common confusions. Otherwise, read in order:

1. **[docs/01 — What Is Loop Engineering](docs/01-what-is-loop-engineering.md)** — the idea, plainly.
2. **[docs/02 — The Lineage](docs/02-the-lineage.md)** — prompt → context → harness → loop.
3. **[docs/03 — Anatomy of a Loop](docs/03-anatomy-of-a-loop.md)** — the lifecycle and the "loop contract."
4. **[docs/04 — The Five Building Blocks](docs/04-the-five-building-blocks.md)** — automations, worktrees, skills, connectors, sub-agents (+ memory).
5. Build your own: run the **[loop-engineering skill](skill/loop-engineering/)**, or copy a prompt from **[prompts/](prompts/)** into Claude Code, Codex, Cursor, or OpenCode, or follow the hands-on **[docs/10 guide](docs/10-building-loops-claude-code-and-codex.md)**.
6. Go deeper: **[verification](docs/05-stop-conditions-and-verification.md)**, **[memory](docs/06-memory-and-state.md)**, **[stacking loops](docs/07-stacking-loops.md)**.
7. Stay honest: **[token economics](docs/08-token-economics.md)** and **[the risks](docs/09-risks-and-the-debt-trilogy.md)**.
8. Steal the lessons: **[Field Notes](FIELD-NOTES.md)** — 13 cross-cutting things that took everyone else a while to learn.

## The docs (learn it in depth)

| # | Chapter | What you'll learn |
|---|---------|-------------------|
| 01 | [What Is Loop Engineering](docs/01-what-is-loop-engineering.md) | The core idea and why it appeared in 2026 |
| 02 | [The Lineage](docs/02-the-lineage.md) | Prompt → Context → Harness → Loop |
| 03 | [Anatomy of a Loop](docs/03-anatomy-of-a-loop.md) | The lifecycle + the 11-part loop contract |
| 04 | [The Five Building Blocks](docs/04-the-five-building-blocks.md) | Automations · Worktrees · Skills · Connectors · Sub-agents · Memory |
| 05 | [Stop Conditions & Verification](docs/05-stop-conditions-and-verification.md) | `/loop` vs `/goal`, maker/checker, LLM-as-judge |
| 06 | [Memory & State](docs/06-memory-and-state.md) | Ralph, session-as-event-log, brain/hands/session |
| 07 | [Stacking Loops](docs/07-stacking-loops.md) | Loopcraft, the 4-loop stack, going UP vs DOWN |
| 08 | [Token Economics](docs/08-token-economics.md) | O(N²) cost, the 4×/15× figures, budgets, the orchestration tax |
| 09 | [Risks & the Debt Trilogy](docs/09-risks-and-the-debt-trilogy.md) | Comprehension, cognitive, and intent debt; cognitive surrender |
| 10 | [Building Loops in Claude Code, Codex, Cursor & OpenCode](docs/10-building-loops-claude-code-and-codex.md) | Hands-on: `claude -p`, `codex exec`, `cursor-agent`, `opencode run`, the brakes per tool |
| 11 | [Case Studies](docs/11-case-studies.md) | Real loops with real numbers — and the loops that bit back |
| 12 | [Security & Failure Modes](docs/12-security-and-failure-modes.md) | Reward hacking, the lethal trifecta, doom loops, the threat catalog |
| 13 | [Evaluating the Loop](docs/13-evaluating-the-loop.md) | Evals as the regression suite, trajectory vs outcome, proving the verifier |
| 00 | [When *Not* to Build a Loop](docs/00-when-not-to-loop.md) | The decision rule: when a loop is the wrong tool |
| — | [Glossary](docs/glossary.md) | Every term in one place |
| — | [Field Notes](FIELD-NOTES.md) | Hard-won synthesis: 13 cross-cutting lessons |
| — | [Cheat Sheet](CHEATSHEET.md) | The whole field distilled to one page |
| — | [FAQ](FAQ.md) | The questions everyone asks first |

## Practice (copy-paste loop prompts)

The **[prompts/](prompts/)** library collects real prompts you can adapt today:

- **[Ralph loops](prompts/ralph-loops.md)** — the `while :; do cat PROMPT.md \| agent; done` technique and its refined descendants.
- **[`/goal` & `/loop`](prompts/goal-and-loop.md)** — Claude Code stop-condition and cadence prompts.
- **[Automations](prompts/automations.md)** — OpenAI Codex scheduled-automation prompts (triage, CI repair, PR babysitting).
- **[Sub-agents (maker/checker)](prompts/subagents-maker-checker.md)** — explorer, implementer, and independent-verifier skills.
- **[Verification rubrics](prompts/verification-rubrics.md)** — LLM-as-judge graders that return PASS/FAIL with evidence.
- **[Loop contracts](prompts/loop-contracts.md)** — full specs (PR babysitter, CI repair, incident response, dependency triage, PR review, doc-drift repair, flaky-test hunt).

## Build a loop for your own workflow (the skill)

The **[loop-engineering skill](skill/loop-engineering/)** is a portable [agent skill](https://www.anthropic.com/news/skills) you can drop into Claude Code, Codex, Cursor, or OpenCode. Point your agent at it and it will interview you about the work you keep doing by hand, fill in an 11-part **loop contract**, choose honest stop conditions and budgets, and scaffold the files so you finish with a loop you can actually run — and trust.

Install it with one command — it asks which agent you use and where to put it:

```bash
npx github:invincible04/awesome-loop-engineering
```

Or copy the folder yourself (a skill is just a folder with a `SKILL.md`):

```bash
cp -r skill/loop-engineering .claude/skills/loop-engineering   # Claude Code
cp -r skill/loop-engineering .opencode/skills/loop-engineering  # OpenCode
```

Then ask your agent: **"Use the loop-engineering skill to help me design a loop for &lt;the thing you keep doing by hand&gt;."** See **[skill/loop-engineering/README.md](skill/loop-engineering/README.md)** for every install path and tool.

## A runnable example

**[examples/runnable/](examples/)** is a dependency-free Python implementation of the loop machinery — engine, budget, memory, a separate verifier, and the four honest stop conditions — with a test suite. Read it to see the ideas execute, not just described.

```bash
cd examples/runnable
python -m loop_cookbook                    # watch a maker/checker loop converge and stop
python -m unittest discover -s tests -v    # 10 tests, standard library only
```

## Contributing

New chapters, sources, and (especially) real attributed prompts are welcome — see **[CONTRIBUTING.md](CONTRIBUTING.md)**. Released under the [MIT License](LICENSE): use anything here freely.

## Spread the loop

If this helped you stop hand-cranking your agents, **star the repo** and pass it on. The best way to share it is the one-page **[website](https://invincible04.github.io/awesome-loop-engineering/)** — it teaches the whole idea in a single scroll.

> A note on dates: loop engineering is young (the term took off in **June 2026**). Perishable claims — token multipliers, tool features, model behavior — carry an "as of" note, because they expire. What changed between revisions is tracked in the **[CHANGELOG](CHANGELOG.md)**. Corrections via PR are very welcome.
