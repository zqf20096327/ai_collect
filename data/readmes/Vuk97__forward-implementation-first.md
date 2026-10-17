# Forward implementation first

An agent skill that stops a coding agent from getting stuck servicing its own
paperwork.

Long-running agent pipelines grow bookkeeping: content hashes, lock files,
"receipts" that prove a stage ran, certification markers, dashboard rows,
progress metadata. None of that is the product. All of it is easy for a model
to mistake for the product. Once that happens the agent stops shipping and
starts curating, and you pay full price for an agent that produces nothing you
asked for.

This skill gives the agent one classification to make before every action, and
a short list of things it is never allowed to do. It is about 150 lines of
Markdown. It is model-agnostic, tool-agnostic, and domain-agnostic.

## The failure mode

You have a pipeline with ordered stages. Stage 40 produces a file that stage 41
consumes. Somewhere along the way the orchestrator also writes a small JSON
record saying stage 40 completed, with a hash of its inputs.

Then you change one producer. The hash no longer matches. Here is what an agent
does without this skill:

- It notices the mismatch and treats it as a correctness failure, because a
  mismatch looks like one.
- It invalidates stages 12 through 40, because it cannot prove which of them
  the change touched, and invalidating more feels safer.
- It refuses to run stage 41 by hand, because the pipeline "cannot issue a
  receipt" for a manual run.
- It spends the next several hours regenerating markers for stages whose output
  never changed and was never wrong.
- It reports progress in terms of receipts repaired, which reads like work.

Nothing in that sequence is stupid in isolation. Each step is a defensible
local decision. Together they cost days, and the output at the end is identical
to the output you already had. The pathology is that administrative metadata is
being used as a proxy for correctness, and the proxy is both cheaper to check
and completely uninformative.

The second half of the failure mode is worse: the agent tells you it cannot
proceed. You then go run the stage yourself, or open a second agent to do it,
and the first agent sits there guarding a hash.

## What the skill does

Before each action, the agent classifies it as one of three things:

1. **Semantic implementation.** Builds or connects a producer, consumer,
   adapter, runtime path, schema, fixture, or final output.
2. **Focused validation.** Tests the changed dependency cone through behavior,
   schema, counts, ordered samples, conservation, consistency, nontruncation,
   and measured time and memory.
3. **Administrative bookkeeping.** Generates or repairs hashes, locks,
   receipts, dashboards, certification markers, progress metadata, or
   presence-only records.

Do 1 and 2. Skip 3 unless the user asks for it, or the artifact is part of the
product. When category 3 blocks a path without protecting correctness, delete
the dependency.

That is the whole idea. The rest of [SKILL.md](SKILL.md) makes it hard to
weasel out of, because a model that wants to do bookkeeping will find a reason.

## What it does not relax

This is the part that makes the skill safe to install, and the part most
"just move faster" prompts get wrong. Bookkeeping is cheap to skip. Evidence is
not. The skill explicitly preserves:

- integrity that belongs to the product itself. A checksum your users verify, a
  signature your format requires, a hash that is part of the output contract.
  Those are features, not paperwork;
- input and revision identity, when it decides which version of the thing you
  are operating on. Getting that wrong means correct work on the wrong target;
- tests that assert results, benchmarks, reproductions, and end-to-end runs;
- the difference between coverage and consequence. A run that exercises a path
  is not a check that the path produced the right answer.

An execution record that carries the command, the input, the result, and the
expectation it was checked against is real evidence. Its absence blocks the
claim it supports. It does not retroactively invalidate an unrelated stage
twenty steps back. That distinction is the whole difference between rigor and
superstition, and it is the line the skill draws.

## The forward cursor rule

A pipeline stage may be replayed or rolled back only for a real reason:

- its input meaning changed;
- its target or pinned revision changed;
- its output is malformed, truncated, nonconserving, inconsistent, or
  incompatible with its consumer;
- an observed run disproves the earlier static result;
- the changed producer's declared dependency cone requires it.

Missing or stale metadata is not on that list. When a stage is blocked only by
a marker, the agent runs it manually, validates the output, publishes it,
continues from the cursor, and then removes the administrative-only gate so the
same block cannot happen again. Replay the smallest affected cone, not the
whole history.

## Parallel work: invariants, not a scheduler

The skill also covers parallelism, because the two problems show up together.
An agent that is busy with bookkeeping usually also serializes everything.

Early feedback drew one boundary the first version got wrong: a skill must not
act as an orchestrator. Scheduling, resource contention, and worker topology
belong to your runtime, and a few lines of Markdown that claim them will fight
any real scheduler. So the section is split in two.

Invariants, kept as first-class rules because they hold under any scheduler:

- Exactly one writer owns publication, cursor movement, and conclusions.
  Parallel workers prepare and inspect. They never become a second source of
  truth.
- Verify a worker's output before consuming it. A report states intent, not
  result.
- Forward progress does not wait for every worker. Consume output when the
  dependency that needs it is reached.
- Never invent busywork to fill an idle slot.

Scheduling policy itself, worker counts, wave sizes, what counts as a heavy
process, is not in the skill at all. Your runtime already owns it, and a skill
that carries its own policy would fight it. If nothing owns scheduling in your
setup, [examples/execution-profile.md](examples/execution-profile.md) is a
starting profile to copy and edit. The skill never loads it on its own.

The invariants matter more than the speedup. Cheap parallel workers are useful
precisely because they are not trusted, and the value disappears the moment
their output is merged without a check.

## Install

The skill is a single Markdown file with YAML frontmatter, following the
[Agent Skills](https://agentskills.io) convention. Copy it wherever your agent
looks for skills:

```bash
git clone https://github.com/Vuk97/forward-implementation-first
cd forward-implementation-first
./install.sh
```

`install.sh` copies `SKILL.md` into every agent skill directory it finds:

| Agent | Path |
| --- | --- |
| Claude Code | `~/.claude/skills/forward-implementation-first/` |
| Codex | `~/.codex/skills/forward-implementation-first/` |
| Shared convention | `~/.agents/skills/forward-implementation-first/` |

For a project-scoped install, copy the directory to `.claude/skills/` or
`.agents/skills/` in the repo instead. Restart the agent afterward. Running
sessions do not reload skills.

A skill is a suggestion. The model decides whether to load it. If your agent
supports always-on rules or hooks, put the decision rule there too, because
this particular failure mode is one the model walks into confidently.

## When to use it

Install it if any of these describe your setup:

- a pipeline with ordered stages and a persisted cursor;
- generated artifacts that later stages depend on;
- any manifest, lockfile, or receipt written by the orchestrator rather than by
  the work itself;
- runs long enough that you are not watching every step;
- multiple agents or sessions touching one repository.

Common shapes: staged data and ETL runs, large code migrations, build and
release pipelines, documentation generation over many inputs, batch analysis
jobs, and any roadmap an agent works through over days.

Skip it for single-shot tasks, short interactive sessions, and any workflow
where the audit trail is the deliverable. If someone is going to read your
receipts, they are not bookkeeping.

## Where this came from

This started as a prompt pasted at the top of every session in a long-running
staged pipeline, where the agent had repeatedly invalidated dozens of completed
stages over metadata drift and then declined to run stages by hand. Pasting it
every time worked. Forgetting to paste it cost days.

Turning it into a skill made the behavior default instead of remembered.

## License

MIT. See [LICENSE](LICENSE).
