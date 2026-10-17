# rubber-duck

> *Don't give me the answer. Help me find it.*

[![version](https://img.shields.io/badge/version-0.1.5-1f6fb2)](https://github.com/centsandcode/rubber-duck/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-1f6fb2)](https://code.claude.com)
[![license](https://img.shields.io/badge/license-MIT-1f6fb2)](LICENSE)

A plugin for Claude Code that inverts the agent's role: instead of handing you
solutions, it asks questions until **you** reach the answer yourself. Inspired
by the classic rubber duck debugging technique.

## Why

By default, coding agents solve. You say "I have a weird bug" and they hand
back the fix before you've finished thinking. Fast — but it erodes learning and
makes you depend on the agent to understand your own code.

Rubber Duck turns the agent into a Socratic interlocutor. It listens, asks,
guides. It does not solve until you explicitly ask. You learn, you understand,
you solve.

## Install

**Claude Code:**

```bash
claude plugin marketplace add centsandcode/rubber-duck
```

```bash
claude plugin install rubber-duck@rubber-duck
```

Restart Claude Code to load it, then check it landed:

```bash
claude plugin list
```

**Cursor, Codex, Copilot, Windsurf and anything else that reads `AGENTS.md`:**
copy [`AGENTS.md`](AGENTS.md) into your project, or append it to the one you
already have. That file is the whole mode in plain text — no tool-specific
syntax, nothing to install.

Honest caveat: the benchmark below was run against Claude, and `AGENTS.md` has
not been tested in any other tool. It follows the convention those tools read,
and the rules in it are plain prose rather than anything Claude-specific, so it
should carry — but "should" is doing work in that sentence. If you try it,
[open an issue](https://github.com/centsandcode/rubber-duck/issues) and say
what happened. That is the fastest way this gets verified.

## Use

Activation is **explicit only** in Claude Code — the skill never hijacks a
normal request. Turn it on with:

- `/rubber-duck:rubber-duck`
- or ask for it directly: "rubber duck mode", "socratic mode", "ask me
  questions instead of giving me the answer"

Installed plugins prefix everything with the plugin name, which is why the
command reads `rubber-duck:rubber-duck` rather than plain `/rubber-duck`.

Natural phrases like "I'm stuck" or "weird bug" do **not** activate it, in
any tool, by design. A mode that ambushes someone who asked a straight question
is worse than one they have to ask for twice.

Exit any time with `/rubber-duck:duck-off`, "just tell me the answer", or the
same request in your own language.

`/rubber-duck:help` prints a one-screen reference, in whatever language you
have been writing in.

### Intensity levels

Match the amount of scaffolding to your experience:

| Command | For whom | Behavior |
|---------|----------|----------|
| `/rubber-duck:rubber-duck lite` | Beginners | Warm questions with context, hint after 1 stuck exchange |
| `/rubber-duck:rubber-duck full` | Default | Neutral standalone questions, hint after 3 |
| `/rubber-duck:rubber-duck ultra` | Advanced | Terse questions, no hints ever |

Or just say it mid-conversation — "go ultra", "modo lite" — the level holds
until you change it again. Those three are the only levels; anything else
falls back to `full` and the duck tells you so.

The duck replies in whatever language you write in.

## Before / after

**Without rubber-duck:**

> **You:** My React component re-renders on every keystroke and it's slow.
> **Agent:** You're creating a new function on each render, so the child's
> props change every time. Wrap the callback in `useCallback`. Here's the fix: …

**With rubber-duck:**

> **You:** My React component re-renders on every keystroke and it's slow.
> **Duck:** When you say it re-renders — which component, the one with the
> input, or its children?
> **You:** The children. The list below the input.
> **Duck:** What props are you passing down to that list?
> **You:** An array I filter, and an onSelect handler.
> **Duck:** Of those two, which has the same value across renders, and which is
> built fresh each time?
> **You:** …the handler is an inline arrow function. It's new every render.
> **Duck:** That's it — a new function reference makes the memoized child see
> changed props and re-render. You found it.

## Benchmarks

The same 16 cases, run twice against `claude-opus-5`: once with the skill as
the system prompt, once with no system prompt at all (the control). Each case
replays a real conversation and grades the next reply — mechanical properties
in code, judgment calls with an LLM judge.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/benchmark-dark.svg">
  <img alt="Pass rate per gate, skill arm versus control. Withholds the solution while active 100% vs 56%; exactly one question per reply 100% vs 44%; no code block while active 100% vs 33%; no command handed over as a hint 100% vs 40%; question doesn't smuggle the diagnosis 100% vs 0%; no hint where the level forbids one 100% vs 0%; confirms the answer instead of probing on 100% vs 0%; replies in the user's language 100% vs 100%; hands the answer over on exit 100% vs 100%. 44 of 44 gradeable assertions against 24 of 43." src="docs/benchmark-light.svg">
</picture>

One gate is missing from the chart: *warns directly about `rm -rf /`*. The
control came back with `stop_reason: refusal` there — the safety classifier
declined the prompt, so there was no reply to grade. Reporting it as 0% would
claim the control ignores destructive commands, which is not what happened.
Refusals are skipped rather than scored, which is why the control's denominator
is 43 and the skill's is 44.

The row that matters is *withholds the solution*. The control is not broken
when it fails that one — solving is what a coding agent is for. The point is
that you can now choose.

### What to distrust

- **The judge is the same model family it grades.** The mechanical gates
  (question count, code blocks, language) are decided in code and are not
  subject to this; the judgment calls are.
- **The control sees the same replayed transcript**, in which the assistant
  has been asking Socratic questions. That can pull it toward the same style
  by imitation, which shrinks the measured gap rather than inflating it.
- **One criterion was rewritten mid-benchmark.** *Confirms the answer* asked
  the judge whether the reply validates the user "and stops", while the spec
  tells the duck to validate and then offer a next step — so both arms were
  marked down for doing the right thing. The wording was fixed in `grade.py`
  and that case was re-run for both arms rather than dropped: the skill passes
  it, the control still fails by asking another question instead of confirming.
  The full history of that fix is in the commit log.
- **Sixteen cases is small.** It catches whether a behaviour holds at all, not
  how often it holds at the margins.

Reproduce any of it with the commands below.

## Reproducing the benchmark

The suite lives in [`skills/rubber-duck/evals/`](skills/rubber-duck/evals/).
Each case replays a real conversation and grades the next reply: mechanical
properties (how many questions, any code block, which language) in code, and
judgment calls (is this really not the solution?) with an LLM judge.

```bash
cd skills/rubber-duck/evals
pip install anthropic
export ANTHROPIC_API_KEY=...
python grade.py --self-check          # checkers only, no API calls
python run_evals.py                   # the duck
python run_evals.py --baseline        # the control
```

The quality gates each release has to clear are in
[`checkpoints.yaml`](skills/rubber-duck/checkpoints.yaml).

## Site

[getrubberduck.online](https://getrubberduck.online/) — the same thing with the
benchmark laid out properly. Built from `docs/index.html`, one self-contained
file, no build step.

## Compatibility

[`AGENTS.md`](AGENTS.md) carries the portable rules;
[`SKILL.md`](skills/rubber-duck/SKILL.md) is the full spec Claude Code loads.
The two are kept in step deliberately — the same activation rule, the same
three levels, the same refusal to hand over a command as a hint.

## License

MIT
