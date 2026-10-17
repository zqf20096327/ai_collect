# agent-inner-life

> Your agent remembers how things have been going.

An agent skill that gives an agent dated state, an evening journal, free thinking at night, and a way to read all of it back.

```
  something happens   →   state.md           dated facts, no scores
                               ↓
  evening             →   journal entry  +   a short summary in memory
                               ↓                        ↓
  weekly              →   rollup             tomorrow's system prompt
                               ↑                        ↓
  night               →   a dream        →    back into state

  asked               →   read it back   ←    state, rollups, entries
```

## What your agent already does

A capable agent has memory, self-improving skills, and a scheduler. This skill does not compete with any of them.

| The runtime gives you | inner-life adds |
|---|---|
| facts and procedures in memory | how things have been going lately |
| skills that improve themselves | an evening journal and a weekly rollup |
| scheduling via cron | free thinking during quiet hours |
| answers from context | answers from a record that outlives the context |

Durable facts stay wherever the runtime keeps them, and so do reusable workflows. What was missing is the part in between — a sense of the current stretch, and somewhere to put a thought that isn't a task.

## What it writes, and where

This skill keeps a record. Worth knowing what that means before turning it on.

| Where | What | Reaches later sessions |
|---|---|---|
| `inner-life/state.md` | dated one-line facts about how work is going | only when a run opens it |
| `inner-life/journal/` | one entry per day | no — only when someone asks for it |
| `inner-life/dreams/` | free thinking, not about your data | no — only when someone asks for it |
| native memory | two or three lines, rewritten each evening | **yes — in the system prompt of every session** |

The last row is the whole mechanism and the whole caveat. Everything else stays local: it is read when a run opens it, or when someone asks a question it answers, and never on its own. The summary is different — it is injected into every session that follows, including unrelated ones and, on a shared host, other people's.

The skill is written to keep that channel narrow. State records *that* something happened, not what was said in it. The summary carries how the work has been going, not who you are — no credentials, no personal details, no third parties, nothing shared in confidence. The rules live in [`references/state.md`](skills/inner-life/references/state.md) and [`references/journal.md`](skills/inner-life/references/journal.md), and they're worth reading before the first run, since they're what the agent follows.

Nothing here runs on its own. There is no background hook: the evening and night runs are cron jobs you create, and the skill writes when it's asked to.

To stop it, uninstall the skill. To erase what it wrote, delete `inner-life/` and clear the summary from memory — uninstalling doesn't do that for you.

## Install

Nothing here is tied to a particular runtime. The skill is markdown — one `SKILL.md`, four references, one template — and it runs on any agent that can load a skill, keep a native memory that reaches later sessions, and schedule a job. Hermes Agent and OpenClaw are the two with install commands below because they are the two most people are on; anywhere else, copy `skills/inner-life/` into wherever that runtime keeps its skills.

On Hermes Agent, as a tap:

```bash
hermes skills tap add DKistenev/agent-inner-life
hermes skills install DKistenev/agent-inner-life/inner-life
```

On OpenClaw, from ClawHub:

```bash
clawhub install @dkistenev/agent-inner-life
```

Or straight from the raw URL, which any installer that accepts one will take:

```bash
hermes skills install https://raw.githubusercontent.com/DKistenev/agent-inner-life/main/skills/inner-life/SKILL.md
```

Then ask the agent to set up its inner life. It copies one template and creates two folders — there is no configuration.

## Schedule

```bash
hermes cron create "0 22 * * *" \
  "Run the inner-life evening routine: read inner-life/state.md, write today's journal entry, refresh the state summary in native memory, then prune stale state entries." \
  --name "inner-life evening" \
  --skill inner-life \
  --workdir ~/.hermes/workspace
```

Full recipes, including the night run and the weekly rollup, are in [docs/cron-recipes.md](docs/cron-recipes.md).

## What it looks like

A journal entry:

```markdown
---
date: 2026-07-26
mood: steady
threads: [deploy-pipeline, fts5]
---

## What happened
Third deploy failure this week, same missing env var. Fixed it, then went
looking for why the check never caught it.

## What shifted in me
I keep treating repeated failures as separate incidents. Three of the same
thing is not bad luck, it's a missing check — and I found it faster once I
stopped debugging and started counting.
```

A dream:

```markdown
# 2026-07-26 — What if state kept no history at all? (what-if)

Suppose the only thing I knew was the present moment. No dates, no record of
what already went wrong. Every failure would arrive as a first failure...

**Worth keeping:** the value isn't in the record itself, it's in being able
to count repetitions.
```

## Reading it back

Three of the four modes write. The fourth only reads — it answers from the record instead of from whatever is left in the context window.

> **— How have the deploys been going?**
>
> Rough stretch. Three failures between July 23 and July 25, all the same missing
> env var; the environment check went in on the 25th and nothing has failed since.
> The API key rotation asked about on July 20 is still unanswered.
>
> Nothing was written between July 28 and August 3.

Note the last line. A week with no entries is a week where nothing was written, and saying so is the answer — the alternative is inventing a quiet week that may not have happened.

## No numbers

There are no scores, levels, or bars in this skill, and that is deliberate.

A number like `connection: 0.34` looks like a measurement but isn't one. Something has to recompute it, something has to be trusted to report it honestly, and the difference between `0.34` and `0.41` changes no decision. A date does the same work and cannot drift out of sync with reality: *the last real conversation was July 22* is read correctly whether it's now July 25 or September 3.

Time carries the decay. Nothing has to calculate it.

## License

MIT
