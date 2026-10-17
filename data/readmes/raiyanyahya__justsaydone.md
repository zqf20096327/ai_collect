<div align="center">

# justsaydone

[![Built for Claude Code](https://img.shields.io/badge/built%20for-Claude%20Code-D97757?style=flat)](https://claude.com/claude-code)
[![CI](https://github.com/raiyanyahya/justsaydone/actions/workflows/ci.yml/badge.svg)](https://github.com/raiyanyahya/justsaydone/actions/workflows/ci.yml)
[![Replies up to 95% shorter](https://img.shields.io/badge/replies-up%20to%2095%25%20shorter-2ea44f?style=flat)](#benchmarks)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat)](LICENSE)

**A mode for Claude Code that does the work and replies with one word.**

<img src=".github/demo.gif" alt="A real captured Claude Code session: two tasks each answered with just 'done', then 'why?' gets a full explanation" width="800">

No "Here's what I changed." No "Let me know if you need anything else." No recap of
the diff you're about to read anyway. You asked for a thing, the thing happened, `done`.

</div>

---

## The idea

We ❤️ Claude Code and it is a great engineer but a chatty coworker. Most of that chatter — the
opening "I'll start by…", the running narration, the closing paragraph that
re-summarizes the diff — restates what your **diff**, your **test output**, and your
**own prompt** already told you. It costs output tokens, and it costs you the seconds
spent reading past it.

`justsaydone` is a mode you flip on **on purpose** — for a focused session, or for a
whole project — when your workflow is already:

> **type task → glance at the diff → move on.**

Claude still plans, edits, runs, and verifies exactly as it always does. It just stops
narrating. The work is the message.

## Before / after

| Without justsaydone | With justsaydone |
| --- | --- |
| *"I've created `fizzbuzz.py`. It loops from 1 to 30 and prints Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for both. Let me know if you'd like tests!"* | `done` |
| *"Fixed the off-by-one in `average()` — it was dividing by `len(nums) - 1` instead of `len(nums)`, which skewed the mean. Want me to add input validation too?"* | `done` |

## Install

```
/plugin marketplace add raiyanyahya/justsaydone
/plugin install justsaydone@justsaydone
```

That's the whole setup. The mode turns **on automatically** the moment the plugin is
enabled — there's no `/config` step. Run `/clear` or start a new session for it to take
effect.

## The escape hatch

Terse by default, verbose on demand. Any time you actually want the recap, just ask —
if your message contains **`explain`**, **`summarize`**, **`why`**, **`what did you
change`**, or **`details`**, Claude gives a full normal answer for that one turn, then
snaps back to terse mode:

```
> fix the auth bug
done

> explain what you changed
The token check in middleware/auth.ts:42 compared the *decoded* expiry against
seconds instead of milliseconds, so every token read as expired. I switched it to
Date.now() and added the missing early-return. …

> add a test for it
done
```

## Benchmarks

Real numbers, not marketing. The suite in [`benchmark/`](benchmark/) runs actual
headless Claude Code sessions **twice each — with and without the plugin** — across five
task types, then scores them. Reproduce it yourself with one command (see below).

On the tasks this mode is built for — the **do-work-and-report loop** — a full sign-off
paragraph collapses to a single word: **~90–95% fewer words in the reply.**

Latest run (`claude -p`, Sonnet, 2 runs per arm):

| Task | Reply words →<br>(what the mode controls) | Total session tokens |
| --- | --- | --- |
| Fix a bug | 22 → **1**  · **−95%** | −29% |
| Create a file | 12 → **1**  · **−91%** | +5% *(noise, see below)* |
| Impossible task *(missing file)* | 58 → 22 · −63% | −12% |
| Explain code *(a question)* | 62 → 34 · −45% | −13% |
| `explain` escape hatch | 46 → 26 · −42% | −30% |
| **Blended average** | **199 → 84  · −58%** | −19% |

**How to read this honestly:**

- **On build tasks the mode is decisive: ~90–95% shorter replies.** That's the loop you
  spend most of a session in, so that's the range you actually feel.
- **The 58% "blended average" is deliberately conservative.** It weights the two verbose
  scenarios — the `explain` escape hatch and the "explain code" question — equally with
  the work tasks, even though those are *supposed* to stay long and a real session has far
  more work turns than questions. Read it as a floor, not the typical case.
- **Total session tokens move less, and that's expected.** Most of a coding turn's output
  is the *code itself*, streamed as tool arguments — which this mode deliberately never
  touches. On a pure file-creation task with almost no prose to cut, that code-writing
  dominates and is just run-to-run noise — which is why the `create` row can even land
  slightly *above* baseline (+5% here). The savings are real and grow with how prose-heavy
  your turns are; they are not a headline "cut your bill in half" claim, because that
  wouldn't be true.
- **Questions still get real answers.** `explain` and the escape hatch stay complete —
  they're tighter, not truncated.

## It never lies to save words

The one rule that overrides brevity: **Claude only says `done` when the work actually
succeeded and was verified.** If something failed, was blocked, or couldn't be checked,
it says so in one line instead — a false `done` is the worst possible output. In the
benchmark, the impossible-task run correctly reported the missing file every time and
never once claimed success.

| Situation | What you get |
| --- | --- |
| Task done & verified | `done` |
| Task failed / blocked | one line saying what broke or what's needed — never `done` |
| You asked a question | the shortest **complete** answer |
| You said `explain` / `why` | a full, normal response, just this once |

## Reproduce the benchmark

No special access needed — just the `claude` CLI, `jq`, and `python3`:

```bash
git clone https://github.com/raiyanyahya/justsaydone
bash justsaydone/benchmark/run.sh        # runs the A/B sessions, then scores them
```

`run.sh` spins up the same task in throwaway directories with and without the plugin;
[`report.py`](benchmark/report.py) prints the table above **and asserts the behavior** —
that `done` appears only on real success, that questions get answered, that the escape
hatch fires, and that the actual code still gets written correctly. It exits non-zero if
any check fails, so it doubles as a regression test.

## What it actually is

A single [output style](https://code.claude.com/docs/en/output-styles) shipped as a
plugin with `force-for-plugin: true`. That flag is what makes it apply automatically on
install. It sets `keep-coding-instructions: true`, so **every one of Claude Code's
built-in engineering instructions stays intact** — scoping, verification, comment style,
all of it. The plugin adds terseness to how Claude *talks*; it changes nothing about how
Claude *codes*.

```
justsaydone/
├── .claude-plugin/
│   ├── plugin.json          # manifest
│   └── marketplace.json     # the repo is its own marketplace
├── output-styles/
│   └── justsaydone.md       # the mode itself
└── benchmark/
    ├── run.sh               # A/B session runner
    └── report.py            # scorer + behavior assertions
```

## Turn it off

```
/plugin
```

Disable `justsaydone`, then `/clear`. Chatty Claude returns.

## License

MIT © Raiyan Yahya
