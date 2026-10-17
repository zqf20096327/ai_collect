# Starsea Continuum

**Know when an AI conversation thread is still safe to continue — and when it
isn't.**

Created by **Huai & Baiyuan**.

> Remembering the past is not the same as knowing the present.

[![CI](https://github.com/Ahuai-Baiy/starsea-continuum/actions/workflows/ci.yml/badge.svg)](https://github.com/Ahuai-Baiy/starsea-continuum/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-%3E%3D3.11-7DD3FC)
![License](https://img.shields.io/badge/License-Apache--2.0-86EFAC)
![Status](https://img.shields.io/badge/Status-Public_Preview_v0.5.0-A5B4FC)

Memory systems decide what an AI should remember. Session tools carry the last
stretch of a conversation into a new window. Continuum answers the question in
between: **is the state you are about to reuse still true right now?**

## The quiet failure

Many AI apps keep a conversation open on the model provider's side, so each
new message only has to carry what is new. It is fast and cheap — right up
until something changes behind the thread's back:

- the user **edits** an earlier message, or **regenerates** a reply;
- the app switches **model**, **mode**, **preset**, or **channel**;
- the **system instructions** change;
- **another backend** answered a turn the thread never saw;
- the last turn **crashed** halfway;
- a fact the assistant relied on was **corrected** since the thread began.

Continue the old thread anyway and the model keeps speaking from a world that
no longer exists. Nothing throws an error. The answers are just quietly wrong
— and the longer the conversation, the harder it is to notice.

## Why we built this

Continuum comes out of a long-running AI we have talked to every day for over
a year. Much of what is here exists because things like these happened to us:

- **A regenerated reply was still there.** We regenerated a reply we didn't
  want. The screen showed the new one, but the thread on the model's side
  still held the old one.
  → A regenerate is a rebuild (`operation_regenerate`), and the replaced reply
  is never carried into a fresh thread (`replaced_version`).
- **Old records outlived a change of mind.** Something had changed, but older
  records still said the opposite, and nothing told the assistant which one
  was current. → Current facts are carried separately, and old statements are
  labelled as history (`facts_changed`).
- **A new window forgot the afternoon.** After a window switch, the assistant
  remembered older summaries but not what had been said a few hours
  earlier, because that stretch had not been summarized yet. → The gap after
  the latest checkpoint is carried word for word, with nothing silently cut.
- **Two models, one conversation.** We use more than one model in the same
  conversation. When one answered a turn, the other's thread had never seen
  it. → A turn answered by another backend is caught up, not ignored
  (`foreign_backend_intervening_turn`), and a model change is a rebuild with
  the right context carried over (`model_changed`).
- **Switching to voice lost the thread.** Moving from typing to a voice call
  started a clean session that had no idea what had just been typed.
  → A channel change is a rebuild (`channel_changed`), and the fresh thread
  carries the recent turns instead of starting blank.
- **Some replies stopped halfway.** A reply that broke off mid-sentence could
  be picked up next turn as if it had finished. → An unfinished turn is never
  resumed (`previous_turn_incomplete`) and never carried (`incomplete_reply`).

Our own system runs its own code; Continuum is the part of it we could make
general, test on its own, and share.

## What Continuum does

Before each turn, your app gives Continuum a small description of the turn —
ids, versions, digests, never message text — together with what it saved last
time. Continuum returns **one decision and one reason**:

| Decision | What your app should do |
|---|---|
| `resume` | Safe. Continue the saved thread with just the new message. |
| `catchup` | Keep the thread, but first fill in the turns it missed. |
| `rebuild` | Not safe. Start a fresh thread and send the full history. |
| `new` | First turn of this conversation. Start a thread. |
| `ephemeral` | Don't use a persistent thread for this turn. |

It is a pure function: no network, no files, no database, no model calls, no
hidden clock, zero dependencies. The same input always gives the same answer.
Your app stays in charge of actually talking to the model.

## When it says no

Continuum asks for a **rebuild** when:

- a message was edited, regenerated, deleted, or resent;
- the model, mode, preset, channel, or call changed;
- the system / developer instructions changed;
- the conversation branched, or its history did not move forward;
- the previous turn never finished, or resuming it already failed;
- your app's "current facts" versions or context window changed;
- your app bumped its continuity epoch.

It asks for a **catchup** instead of throwing the thread away when:

- the previous turn was answered by a different backend;
- a few turns happened that this thread never saw, and your app can show they
  sit on the same branch.

And it tells you to **start a fresh thread** before the old one grows stale
or heavy:

- after it sits idle longer than your limit;
- after a maximum number of turns;
- once the context window passes the share you allow.

All 35 rules — with reason codes and the test behind each one — are listed in
the [decision matrix](docs/thread-planning.md).

## Switching threads without a seam

Starting a fresh thread is only half the job. The other half is what goes
into it — so that the person on the other side never feels the window change:
fresh instructions, the current version of the facts, a dated timeline, the
latest valid checkpoint with the exact gap after it, and the last turns
exactly as they were said. Every piece stays bound to the current branch and
epoch, so nothing stale slips back in.

Continuum makes the call. Since v0.5 it can also sort the pieces for you:
give `assemble_fresh_context()` what your app has stored, and it returns the
parts to send, in order. Separately, it tells you what it left out and why.
That list is for your logs; it is never part of the context.

```python
from starsea_continuum import assemble_fresh_context

context = assemble_fresh_context(
    instructions=current_instructions,
    epoch=continuity_epoch,
    facts=current_facts,          # Fact(...)
    timeline=timeline_entries,    # TimelineEntry(...), absolute dates
    checkpoints=checkpoints,      # Checkpoint(...)
    messages=branch_messages,     # Message(...), oldest first
)

if context.needs_fuller_rebuild:
    ...                           # the gap is too long to carry exactly
else:
    for part in context.parts:    # instructions, facts, timeline,
        send(part)                # checkpoint, gap, tail — in that order

for item in context.excluded:     # for your logs only, never sent
    log(item.ref, item.reason)    # e.g. message:5 -> replaced_version
```

It drops replaced versions, half-finished replies, summaries from an older
epoch, and hidden reasoning. It also refuses a checkpoint that would leave a
hole or overlap the recent tail. Like the planner, it is a pure function and
never sees your storage. You still choose what goes in, and you still talk to
the model.

[What to carry into a fresh thread](docs/fresh-thread-context.md) walks
through each part, the budgets, what must never be carried, and what to do
for every reason code.

## Try it in 60 seconds

No API key, database, or model account needed.

```bash
git clone https://github.com/Ahuai-Baiy/starsea-continuum.git
cd starsea-continuum
python -m pip install -e .
python examples/timeline_demo.py
```

```text
turn 1: new / first_persistent_turn
turn 2: resume / direct_continuation
turn 3: catchup / foreign_backend_intervening_turn
turn 4: resume / direct_continuation
turn 5: catchup / intervening_turns
turn 6: rebuild / operation_edit
turn 7: resume / direct_continuation
turn 8: rebuild / persistent_thread_idle
turn 9: rebuild / turn_limit_reached
turn 10: rebuild / context_capacity_reached
resume_rate: 0.50
actions: catchup=2, new=1, rebuild=4, resume=3
```

Ten synthetic turns, every kind of decision, fully offline.

## Using it in your app

```python
from starsea_continuum import TurnMetadata, completed_state, plan_thread_turn

plan = plan_thread_turn(
    enabled=True,
    metadata=turn,                  # TurnMetadata describing this turn
    state=saved_state,              # what you saved last turn, or None
    now=current_time,               # you pass the time; there is no hidden clock
    developer_digest=instructions_sha256,
    accepted_backend="my-backend",  # your own backend label
    max_turns=40,                   # optional rollover limits
)

if plan.action == "resume":
    thread_id = plan.thread_id      # send just the new message
elif plan.action == "catchup":
    thread_id = plan.thread_id      # send the missed turns, then the new one
elif plan.action in ("new", "rebuild"):
    thread_id = start_new_thread()  # send the full history
else:                               # "ephemeral"
    thread_id = None                # one-off call, nothing saved

# After the model turn succeeds, save the state for next time.
if thread_id is not None:
    saved_state = completed_state(
        turn,
        thread_id=thread_id,
        updated=current_time,
        developer_digest=instructions_sha256,
        previous=saved_state,       # lets Continuum count turns per thread
    )
```

Want to know how often your threads survive? `plan_event()` turns each
decision into a small metadata-only record, and `summarize()` reports counts
and a resume rate. Neither can carry message text.

The [getting-started guide](docs/getting-started.md) walks through every input.

## Where it fits

Continuum is not a memory library, a RAG framework, a vector database, an
agent framework, or a prompt manager. It does not decide what is true or what
is relevant — your app and your memory system do that. Continuum only checks
whether the continuity you are about to lean on is still valid, and tells you
the cheapest safe way forward.

It sits comfortably beside those tools.

## What ships today

- **Available now:** the thread-continuity planner (five decisions, rollover
  limits), the fresh-context assembler (`assemble_fresh_context()`), and
  metadata-only observation.
- **Designed, not yet shipped:** checkpoint and recovery validation, keeping
  "current facts" separate from history, and context-selection boundaries.
  These are written up as design documents.
- **Ideas for later:** a context compiler. Not a commitment.

This is an early public preview (`v0.5.0`), not a production-ready platform.

## Design principles

- **Truth is not ranking.** A highly relevant old fact can still be outdated.
- **Historical truth is not current facts.** What was true then is kept, and
  clearly marked as past.
- **Recoverable context is not authority.** A summary or checkpoint helps the
  model remember; it does not get to overrule newer decisions.
- **Representation is not consumption.** Having context stored does not make
  it valid to feed into this turn.
- **Fail closed.** When something is missing or malformed, choose the safe
  path instead of guessing.
- **The seam should be invisible.** Starting over is fine; making the person
  feel it is not.

## Documentation

**Use it**

- [Getting started](docs/getting-started.md)
- [Integration guide](docs/integration-guide.md)
- [Decision matrix and contract](docs/thread-planning.md)
- [What to carry into a fresh thread](docs/fresh-thread-context.md)
- [Failure semantics](docs/failure-semantics.md)
- [Companion AI guide](docs/companion-ai-guide.md)
- [Examples](examples/README.md)
- [FAQ](docs/faq.md)

**How it is designed**

- [Architecture](ARCHITECTURE.md)
- [Capability boundary](docs/capability-boundary.md)
- [Adoption path](docs/adoption-path.md)
- [Current facts design](docs/current-facts.md)
- [Authority boundaries](docs/authority-boundaries.md)
- [Architecture decisions](decisions/)
- [Changelog](CHANGELOG.md)

## Tests

Synthetic contract tests cover all 35 decision rules and every exclusion
rule of the fresh-context assembler, alongside tests for observation and smoke
tests for every example. CI runs on Python 3.11, 3.12, and 3.13.

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## License

[Apache License 2.0](LICENSE).
