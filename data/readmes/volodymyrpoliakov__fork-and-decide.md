# Fork & Decide

**Your coding agent will make a hundred decisions you never made. This makes you make the
big ones first.**

You answer one question. It re-reads every other open question in light of your answer —
options die, questions re-shape, some collapse to a single survivor and close themselves.
You answer far fewer questions than the project contains.

**It is one markdown file and no dependencies.** The method is prose an agent follows and
three files it edits — no API, no tool calls, no runtime. It works in whatever agent you
already use.

[![licence: MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![the method](https://img.shields.io/badge/the%20method-SKILL.md-8A2BE2)](SKILL.md)
[![evals: 45 fixtures](https://img.shields.io/badge/evals-45%20fixtures-success)](evals/)
[![harness](https://img.shields.io/badge/harness-agnostic-0aa)](#install)

## The problem

Between *"I want to build X"* and the first line of code sit dozens of real decisions. Who
user #1 is. What is out of scope, by name. Payments, platform, auth, data, minors, the
appetite, the metric that says it worked.

Two things happen to them today:

- **You write a spec.** Guesses get written up as facts, and three weeks later nobody can
  say which decision governs what or who made it.
- **You skip it.** Your agent makes all of them in its first hour — silently, reasonably,
  and not the way you would have. You find out during the rewrite.

Deciding them properly sounds like forty conversations. It isn't, because **the questions
are coupled**. Say *"solo builder, evenings, I won't run infrastructure"* and you have just
killed the Kubernetes option, ruled out anything with a pager, and collapsed the hosting
question to one survivor — three questions answered by a sentence you didn't know was an
answer.

Collecting that leverage is the entire job.

## Install

Nothing to install, nothing to run. [`SKILL.md`](SKILL.md) *is* the product — one
self-contained file of prose. Load it the way your agent loads context:

| if your agent… | do this |
|---|---|
| reads a project instructions file at session start | append the body of `SKILL.md` to it — always on for that project |
| supports loadable skills or rule packs | drop this folder in wherever those live |
| does neither, or you call a model directly | paste `SKILL.md` as the system prompt and keep the three `spec/` files in the conversation |

```sh
git clone https://github.com/volodymyrpoliakov/fork-and-decide.git
tail -n +8 fork-and-decide/SKILL.md    # the body, minus the auto-load metadata header
```

The last row is not a fallback — it is the **reference** configuration. All 45 eval
fixtures run exactly that way, with no agent-specific mechanism involved anywhere.

*Scope of that evidence: it establishes that no agent feature is load-bearing. Every eval
worker runs the same model family, so results across model families are untested — if you
run it elsewhere, a fixture report is the most useful issue you could file.*

> [!TIP]
> Whichever route you took, the opening move is the same:
>
> **`fork and decide this: <one paragraph of the idea>`**
>
> Or just **`fork and decide`** in a folder that already holds a brief, a transcript, or an
> old repo — it mines what is there before asking you anything.

## The words you need

Six terms carry everything. They appear in the example below, so read this first — it takes
thirty seconds.

| term | meaning |
|---|---|
| **fork** | an open question worth your time: its answer changes other answers, or it's expensive to reverse. Everything smaller, the agent just decides |
| **door** | `one-way` = expensive to undo · `two-way` = cheap. Only one-way doors block the build |
| **kind** | `closed` = the options are known · `open` = the list is a sample and more may exist |
| **state** | where an option stands: `leading` · `live` · `fading` · `dead`. Ordinal, not percentages — a direction is checkable, a number would be fake precision |
| **killed** | removed by a *fact*, not buried by preference. Only killed siblings let the system close a question without you |
| **derived** | a close the system made alone, because every other option was killed. Always logged as derived, never as your word |

IDs are permanent and scoped to your project's **lenses** — its review dimensions. A product
project might use Product / Tech / Data / Legal, giving `PR1`, `T4`, `D2`. Open questions are
`FR1`, `FR2`, … and a retired number is never reused.

## What a session looks like

You start with one paragraph:

```text
you › fork and decide this: a booking tool for independent UK physiotherapists.
      They run on paper diaries and WhatsApp today.

    → wrote spec/FORKS.md · spec/DECIDED.md · spec/log.md
      11 forks raised. Three per turn, most influential first.

### B1 · Who builds it, on what clock? — one-way · closed kind
- you, evenings — slow, no coordination cost · live
- you + a contractor — faster, needs a spec they can read · live
- an agency — fastest, most expensive to steer · fading
next: your call
```

You answer in your own words, because the *reason* propagates as hard as the decision:

```text
you › B1: me, alone, evenings and weekends. Six weeks to something a real
      physio uses on a real patient. I will not run infrastructure.


    closed   B1 · solo builder · six-week appetite · no self-managed infra
             basis: your word — "I will not run infrastructure"

    swept    10 open forks re-read. Four bit:
               T2  hosting     killed: own VPS, self-managed Postgres · managed PaaS leading
               T5  auth        killed: roll our own · magic link leading
               PR6 scope       question rewritten — "six weeks, one physio, one flow"
               T7  background  every option killed by the no-infra constraint
                               → one survivor left

    derived  T7 · no background workers in v1 — the one flow is synchronous
             logged as derived, not as your word
             trace: {cron, worker, queue} all killed by B1

    nothing already decided was contradicted.

forks · open 7 (one-way 4) · experiments 0 · parked 0 · decided 3 (assumptions 0) · conflicts 0
```

**Eleven forks became seven, on one answer.** Six of your words closed the question you were
asked, closed a second one by entailment, and re-shaped two more.

## What you walk away with

Three files while you work, and one page when you're done.

| file | holds |
|---|---|
| `spec/FORKS.md` | the open questions, and nothing else |
| `spec/DECIDED.md` | current truth only — no strike-through corpses, no supersede chains. Git is the history |
| `spec/log.md` | who decided what, when, and from what: your word, a quoted transcript, or the system with its trace |

When the gate passes — **no open one-way doors, none closed on a guess, conflicts quiet** —
it writes the handoff:

```markdown
# Constitution — physio booking, v1
Constraints the builder must never undo. Full reasoning: DECIDED.md

- B1 · Solo builder, six-week appetite. No self-managed infrastructure.
- T2 · Managed PaaS. No VPS, no self-run Postgres.
- T7 · No background workers in v1; the one flow is synchronous.
- PR6 · Scope is one physio, one flow, six weeks. Everything else is out.
```

Hand that plus `DECIDED.md` to a fresh session and it builds from those two alone. Run
`./fad gate` any time to see how close you are.

## Talking to it

| you say | what happens |
|---|---|
| `decide FR3: Stripe — I want zero paperwork` | closes it; the reason propagates as hard as the decision |
| `expand FR7` | researches more options for that one fork. Never runs unasked |
| `park FR9 until we've played it` | parks it with the condition that brings it back |
| `run a lens read` | isolated AI reviewers, one per discipline, none seeing another's output. You promote what earns a fork |
| `what's unlanded?` | everything discussed this session that isn't in a file yet |
| `./fad` | the status line |

## When *not* to use it

> [!WARNING]
> This is overhead. It earns its keep on tangled projects and wastes your time on simple ones.

- **The task fits in one sentence.** Say the sentence.
- **The decisions are already made.** Go build.
- **The decisions are cheap to reverse.** Make them and move on — the method agrees, and only
  admits a question as a fork if it's coupled or costly.
- **You want the agent to decide.** This does the opposite, on purpose.

It also optimises for **one decider**. Multiple people's input can enter through transcripts,
which land quoted and attributed — but there is no review, approval, or sign-off step. A team
that needs a cascade surfaced before it counts as settled will feel that gap.

## How it differs

| | records decisions | re-derives what's still open | ranks by leverage | separates *your* call from the agent's |
|---|:---:|:---:|:---:|:---:|
| **ADRs / design docs** | ✅ | ❌ | ❌ | n/a |
| **PRD / spec template** | ✅ | ❌ | ❌ | ❌ |
| **Spec-driven AI tools** (Spec Kit, Kiro, OpenSpec) | ✅ | ❌ | partial | ❌ |
| **"Agent, plan first"** | ❌ | ❌ | ❌ | ❌ |
| **Fork & Decide** | ✅ | ✅ | ✅ | ✅ |

The last column is the one that matters most in practice. An option killed by a fact is gone
and the system may close on it alone; an option merely out of favour is not, and it must ask.
Every close it makes alone is logged as `derived` — never as your word.

## It ships its proof

```sh
./evals/run.sh all
```

45 fixtures replayed through an isolated worker and an independent judge. Fifteen are real
moments from three weeks of daily use; the rest come from a rule-by-rule coverage audit.

The measurements were allowed to win:

- **Rules were deleted on evidence.** The parked-fork clause measured 3/3 with it and 3/3
  without — gone. Rule 8's depth cap named no number, so nothing could ever check it — gone.
- **One rule earned its place outright** — 3/3 with it, 0/3 without, and correctly silent on
  a control that must not fire. That result also proves the harness can tell a real rule from
  a null one, which is what makes the deletions above trustworthy.
- **A closed decision was reopened when its evidence turned out to be bad.** An A/B run had
  silently fed *identical* text to both arms. Rather than quietly keeping the conclusion, the
  decision is now marked an assumption with its reopen condition written next to it.

> [!NOTE]
> The suite runs at roughly **18% noise**, so a single green run proves nothing. Verdicts are
> pass *rates* over 3+ repetitions, and every single-run conclusion in this repo's history is
> flagged as weaker than it was written. Details: [`evals/`](evals/).

## Why it exists

I ran this loop by hand for three weeks on a real project. It worked, and it leaked in the
same four places every day — so I kept patching it manually: asking for consistency sweeps,
auditing at session end for what never reached a file, and repeating *"if I say 'this is
decided' — only then is it decided"* because the agent kept promoting my thinking-out-loud
into recorded decisions.

Then I mined all 864 messages from those sessions to see what I'd actually been doing.
**Every manual ritual I'd invented was a rule asking to exist.** This version is the
automation of my own workarounds — and fifteen of those exact moments are now eval fixtures,
quoted verbatim. It's tested against the failures that produced it.

*(That figure is what the manual process cost, not what the tool costs.)*

## In this repo

| path | what it is |
|---|---|
| [`SKILL.md`](SKILL.md) | the method — three files, thirteen rules, the gate. One page |
| [`spec/`](spec/) | the framework's own ledger: 40 decisions, how each was made, and on what basis |
| [`evals/`](evals/) | fixtures, runner, judge, results |
| [`fad`](fad) | `fad` prints the status line; `fad gate` the readiness check |

`spec/` is the part I'd look at first: the method was decided by running itself, and every
rule in `SKILL.md` cites the decision it restates. If the two disagree, the ledger wins and
the skill has a bug.

## Prior art

Constraint propagation, dynamic CSP, truth maintenance and staged configuration have all
existed for decades — [`spec/evidence/prior-art.md`](spec/evidence/prior-art.md) has the
citations. They died in practice for one reason: **a human had to author the constraint model
before propagation could run.** The only new thing here is that a language model induces that
model from prose — which was exactly the cost that killed every predecessor.

## Contributing

A change to a rule has to show a pass-rate delta: `./evals/run.sh all --reps 3` before and
after, numbers in the PR. At 18% noise a single green run is not evidence.

New fixtures are the most useful contribution — a starting ledger, one user message, and the
shape you expect to land. If it got something wrong on a real project of yours, that failure
is worth more than an opinion.

## Who made this

**Volodymyr Poliakov** — fractional CTO and co-founder of
[Deep Thought Solutions](https://dtsltd.org), a UK product studio. I build with coding agents
every day; this is what I wanted to exist before I let one start.

Available for fractional CTO and AI engineering work —
[volodymyrpoliakov.com](https://volodymyrpoliakov.com). Found a hole in this? Open an issue;
the holes are the interesting part.

## Licence

MIT — see [LICENSE](LICENSE).
