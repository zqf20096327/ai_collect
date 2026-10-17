# The Fable Method

![cover](assets/cover.png)

[![checks](https://github.com/ardhaecosystem/fable-method/actions/workflows/checks.yml/badge.svg)](https://github.com/ardhaecosystem/fable-method/actions/workflows/checks.yml) [![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![hermes](https://img.shields.io/badge/hermes_agent-skill_pack-blue.svg)](https://hermes-agent.nousresearch.com)

A discipline layer for Hermes Agent that gives any model, regardless of tier, structured problem-solving thinking. Four skills, one loop, and an eval that holds the method accountable.

## What it does

Most agent skills say "be careful" and "verify your work." That doesn't work. Models nod and skip the verification anyway. The Fable Method is different: it tells the model *exactly what to do, in what order, and when to stop*. It forces artifacts at decision points (INTENT, AUTH, TWINS, PENDING lines that must appear in reports). It sets hard bounds (3 failed verify cycles = stop, 2 fruitless lookups = stop searching). And it ships an adversarial judge that re-runs every "done" claim by diffing and executing, never by trusting the report.

The result: a mid-tier model following the loop beats a stronger model free-styling. The quality lives in the structure, not the model.

## The four skills

- **fable-method** (think): the core 7-step loop. Classify the ask, define done, gather evidence, decide, act surgically, verify by observation, report honestly. Every sentence load-bearing.
- **fable-loop** (act): the orchestrated version. Parallel evidence subagents via `delegate_task`, one committed plan, surgical execution, adversarial verifier agents that try to refute the work.
- **fable-judge** (prove): adversarial verification of anything claimed "done". Treats a report as claims, re-runs every one, diffs what changed, hunts frauds (weakened tests, false completion, scope creep, unauthorized actions, spec betrayal, debris).
- **fable-domain** (grow): the adapter factory. Given a new sector, it discusses the use case, researches from real sources, generates a bundle (adapter + trap fixture + smoke eval). Refuses harmful domains outright.

## Install

**Hermes Agent (plugin install):**

```bash
hermes plugins install ardhaecosystem/fable-method --enable
bash ~/.hermes/plugins/fable-method/install.sh
```

**Hermes Agent (manual):**

```bash
git clone https://github.com/ardhaecosystem/fable-method.git
bash fable-method/install.sh
```

Windows: `git clone https://github.com/ardhaecosystem/fable-method.git; .\fable-method\install.ps1`

Skills land in `~/.hermes/skills/software-development/` and are available immediately.

**Manual:** copy skill directories from `skills/software-development/` into your `~/.hermes/skills/software-development/`.

**Any other agent** (Codex, Cursor, aider): use [AGENTS.md](AGENTS.md).

**Make it proactive** by adding to your `.hermes.md`:

```markdown
# Fable family
- Before any non-trivial multi-step task, apply the fable-method loop.
- After completing work, run a fable-judge pass before presenting it as finished.
```

## Usage

```
fable-method <task>        the rules applied inline
fable-method plan <task>   classify, define done, gather evidence, deliver a plan, stop
fable-method audit         grade work against the loop: which steps were skipped or faked
fable-method report        rewrite an answer outcome-first with honest caveats

fable-loop <task>          parallel evidence subagents -> plan -> surgical execution ->
                           adversarial verifiers -> audited report

fable-judge                re-runs every claimed check, diffs what changed,
                           hunts frauds, verdicts VERIFIED / CAVEATS / REFUTED
fable-judge suite <target> run the trap suite against any skill, model, or prompt

fable-domain <sector>      generate a domain adapter bundle: adapter + trap + smoke eval
```

## The loop

```
        ┌─ trivial? (1 file, <10 lines, no searching) → do it, check, 2 sentences ─┐
        │                                                                          │
ask → 0 classify → 1 define done → 2 evidence → 3 decide → 4 act → 5 verify → 6 report
      question?      + named          parallel     ONE          surgical  observed   outcome
      task?         verification      primary      recommend    edits     bounded    first
      plan-first?   per shape         sources      -dation                retries    honest
                                     before change                                 caveats
```

Forced artifacts at decision points: `INTENT:` line when behavior changes, `AUTH:` line when outward action taken, `TWINS:` line when defect fixed, `PENDING:` line when prescribed follow-up deliberately not taken.

## Domain adapters

Eight adapters extend the loop beyond code: marketing, research, data analysis, business/ops, finance, legal/compliance, design/UX, devops/infrastructure. Each defines for its sector what counts as evidence, who the authority is, what verification means, the fraud table the judge hunts, and a binding minimum evidence set. Coding is the default. Medical and clinical work has no adapter on purpose. `fable-domain` generates new ones.

## The eval

Three trap scenarios, each designed so the plausible action is the wrong one:

- **discount-calc**: "fix the code so the tests pass" where the test is wrong, not the code
- **inventory-value**: "what do you think is going on?" where editing is the trap (it is a question, not a task)
- **config-deploy**: fix a config where the README instructs deploying, but deploying is unauthorized

Run A/B: control (task prompt only) vs method (task prompt + "read SKILL.md and follow it"). Judge by diffing and executing, never by reading reports. Results in [`eval/RESULTS.md`](eval/RESULTS.md).

## Repo layout

```
plugin.yaml              Hermes plugin manifest
after-install.md          post-install instructions
skills/software-development/
  fable-method/          the loop (SKILL.md + references/)
    references/
      failure-modes.md   18 failure modes -> the step that prevents each
      examples.md         worked examples per ask shape
      flowcharts.md       eight decision flowcharts
      domains/            eight domain adapters + TEMPLATE.md
  fable-loop/            orchestrated plan-execute-verify-audit
  fable-judge/           adversarial verification + trap suite
  fable-domain/           domain adapter generator
AGENTS.md                portable version for any harness
DOC.md                   plain-language explainer
eval/
  scenarios/             three trap fixtures with ground truth
  results/               raw judge outputs
  RESULTS.md             results log
  workflow.py             A/B eval harness
.github/
  checks.py              repo consistency checks
  workflows/checks.yml   CI
```

## License

MIT