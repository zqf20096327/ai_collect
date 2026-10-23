# Deep Reasoning

Stop your agent from answering on its first plausible idea.

**English** | [简体中文](README.zh-CN.md)

Ask a model a hard question and it will produce a confident answer in one pass. Ask it to "think deeply" and you usually get the same answer wearing a longer coat. Deep Reasoning is a skill that changes what the model is structurally required to do before it is allowed to answer: produce multiple fundamentally different options, attack each one adversarially, test and update its own beliefs, and only then converge — delivering a short conclusion first, with the full reasoning record available on request.

## The honest premise

**This skill cannot increase a model's compute budget.** No prompt file can. If the gap between a mediocre answer and a great one is raw reasoning capacity, a skill will not close it.

What a skill can do is remove the room to be lazy:

- make reasoning **visible**, so it cannot be skipped silently
- force a **structured framework** to completion instead of stopping at the first idea
- force **self-attack**, so the model cannot close with self-congratulation
- publish **counts** (options generated, attack rounds, beliefs moved) so a skipped phase is visible

If you want the compute ceiling raised, use your platform's reasoning-effort setting. Step 0 of this skill reminds you to check it. That is the only thing here that changes the ceiling, and it is honest about being the only thing.

## What it enforces

Four techniques, split into two families. Doing only one family always produces a half-finished result.

**Generative** — answers "what else could be true":

- first principles + MECE decomposition
- parallel option generation + weighted scoring matrix, then a robustness check on the winner
- the status quo is always an option, and every weight names who set it — user, project constraint, or the model's own judgment

**Adversarial** — answers "does it survive contact":

- red team / blue team rounds with steelman-first discipline
- falsification + pre-mortem

Each tier carries hard floors. Falling short means the work is not finished:

| Check | T1 fast | T2 deep | T3 full throttle |
|-------|---------|---------|------------------|
| Distinct options | 2 | 3 | 5 |
| Attack rounds | 1 | 2 | 3 |
| Material belief updates | 1 | 2 | 3 |
| External verification | where fact-dependent | where fact-dependent | same, plus independent confirmations |

## Why the output is short

The most common failure of "think harder" prompts is that they dump the entire reasoning transcript into the reply. Reading 200 lines of deliberation is not thinking — it is work the user did not ask for.

This skill separates **generating** from **displaying**. The process still runs in full, because writing the reasoning down is itself a quality mechanism. But delivery is compressed:

```
Assumption: <only when the framing diverges from what you asked>

## Conclusion
**Recommendation:** ...
**Why this one:** 1. ... 2. ... 3. ...
**Largest risk:** ... — trigger: ...
**Confidence:** medium, mainly because of ...
**Falsification condition:** if <signal> appears, revisit
**Verified:** <what was actually checked and how>

[Process line — print only when an inspectable artifact is displayed above; otherwise omit]
*Process: 3 options · 2 attack rounds · 2 belief updates.*
```

Three switches, always available:

| Say | Get |
|-----|-----|
| `expand` | the full record — option space, scoring matrix, per-round attack log, pre-mortem |
| `save` | the full record written to a markdown file, chat reply still compressed |
| `be brief` | conclusion + 3 lines — internal process intensity unchanged |

Three things may never be compressed away: the falsification / revision condition, any counter-evidence found, and the largest risk with its trigger. A conclusion with no falsification condition is not a strong conclusion — it is an evasion.

A fourth line is mandatory even when the answer is short: `Verified:`. In the first eval pass, checking one performance claim turned a confident yes into a conditional answer — and nothing in the output would have revealed that anything had been checked. A count in the process line says how many checks ran; the `Verified:` line says which.

The `Process:` line is printed **only when an artifact the user can inspect sits behind it**. It was the most common ritual found in testing: a claim about work, in the one mode that deliberately shows no work. A reader must not be left unable to tell a model that ran four attack rounds from one that typed the sentence.

## Install

Copy the `deep-reasoning` folder into your agent's skills directory. The folder name must stay `deep-reasoning` and `SKILL.md` must sit at its root.

```bash
# Claude Code (user-level)
cp -r deep-reasoning ~/.claude/skills/

# Claude Code (project-level)
cp -r deep-reasoning .claude/skills/

# WorkBuddy
cp -r deep-reasoning ~/.workbuddy/skills/

# TRAE
cp -r deep-reasoning ~/.trae-cn/skills/
```

Any other agent that loads `SKILL.md` files works the same way — put the folder wherever that agent looks for skills. If the agent auto-triggers on the description rather than on explicit invocation, the description is written to require an explicit request, so it will not fire on ordinary questions.

## How to use it

Just ask, and say one of the trigger phrases:

```
深度思考：把 xyz 的架构选型过一遍，别偷懒
think harder about whether we should shard this now
what am I missing here — poke holes in this plan
```

Default tier is T2. Say "full throttle" / "满油门" / "max" for T3. Say "be brief" for a shorter delivery.

Add the skill only where it earns its keep: it needs at least 2 options and one attack round to function. Simple lookups, single-step instructions, and formatting tasks do not need it — the skill lists these as explicit non-use cases.

## Repository layout

```
deep-reasoning/
├── SKILL.md                    # the skill itself — steps, hard floors, output contract
├── references/
│   ├── techniques.md           # operating manuals, attack angles, anti-patterns
│   └── checklist.md            # internal checklist + the three delivery templates
├── adapters/
│   └── workbuddy/              # reference implementation of the step 0 budget check
├── examples/                   # a worked input → output pair
├── evals/                      # task set, scoring rubric, scorecard, results
├── LICENSE
└── README.md / README.zh-CN.md
```

`references/` is loaded on demand, keeping `SKILL.md` lean. The skill is platform-neutral: nothing in `SKILL.md` or `references/` refers to a specific product. The one platform-specific piece lives in `adapters/` and is optional.

## Porting to your platform

Step 0 asks the model to check whether the host exposes a reasoning-effort or thinking-budget control, and to tell you how to raise it — never to change your configuration without consent. On a platform without such a control, the step is skipped silently.

`adapters/workbuddy/check_reasoning_effort.py` is a working example for one platform. To port it, copy the script and change the settings path and the key name. See `adapters/workbuddy/README.md`.

Ideas worth adding adapters for — pull requests welcome:

- OpenAI and Anthropic API `reasoning_effort` / extended-thinking parameters
- IDE agents that expose a thinking-budget toggle in their settings UI
- CLI agents with a config file containing a reasoning or verbosity key

## Scope

This skill constrains the model's **own** reasoning. It does not interrogate you about your plan — that is a different job, better served by a dedicated interviewing skill. Keeping the two separate keeps both triggers clean.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports about the instructions themselves are the most useful kind — if a rule is ambiguous enough that a model interpreted it the wrong way, say so and quote the rule.

## License

[MIT](LICENSE) © 2026 Ziliang Qiu
