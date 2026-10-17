<p align="center">
  <img src="assets/banner.jpg" alt="Interrogation Partner — questions, not answers" width="100%">
</p>

<p align="center">
  <strong>An AI skill that interrogates you — with your consent — until the story you tell yourself gives way to what's actually true.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview"><img src="https://img.shields.io/badge/format-Agent%20Skill-orange" alt="Agent Skill"></a>
  <a href="skills/interrogation-partner/evals/evals.json"><img src="https://img.shields.io/badge/evals-3%20scenarios-blue" alt="Evals: 3 scenarios"></a>
</p>

You arrive with a **narrative**: the polished, self-flattering, internally consistent story you tell yourself. Underneath is the **ground truth**: the real reason, the avoided fact, the fear renamed "strategy." This skill finds the gap between the two and pries it open — the way a good interrogator finds the seam in a cover story and works it until the real account falls out.

It never hands you an answer. It extracts yours.

---

## What a session looks like

> **You:** Our churn is up because of onboarding friction. I want to rebuild the onboarding flow.
>
> **Interrogation Partner:** You handed me a diagnosis and a prescription in one breath. That's fast. Let's slow it down.
>
> "Onboarding friction" is an abstraction. Give me the fact under it: which specific customers churned last month — name three — and what did each one actually say when they left?
>
> If you can't name them or quote them, then "onboarding friction" isn't your finding. It's the explanation that lets you build the thing you already wanted to build. Which is it?

<details>
<summary>Same session in Russian · Пример на русском</summary>

> **Ты:** Думаю, стоит ли уходить из компании и запускать свой стартап. Помоги разобраться.
>
> **Interrogation Partner:** Ок. Мы идём за настоящей причиной, не за той, что ты расскажешь коллегам. Я буду давить. Остановишь одним словом. Начали.
>
> Ты назвал это «стоит ли». Один вопрос: ты уже решил?
>
> Не отвечай сразу «нет». Вспомни последнюю неделю — ты искал аргументы уйти или аргументы остаться? Что ты гуглил ночью?

</details>

## Why this exists

Most "help me think" AI conversations fail the same way: the model accepts your framing at face value, then diligently optimizes *inside* your self-deception. You wanted clarity; you got a well-organized version of the story you were already telling yourself.

Interrogation Partner starts from the opposite assumption — **the first version of your story is the cover story.** It's built for:

- The decision dressed as a question ("should I quit?" — asked by someone who resigned in their head a month ago)
- The "strategy" that is a fear wearing a suit
- The project that's been "almost ready" for six months

Bring it any decision, claim, or plan you want stress-tested by a questioner who won't be polite about it.

## How it works

A session moves through six phases — warm and wide early, narrow and hard late:

| Phase | What happens |
|---|---|
| **1. Booking** | States the mission and the exit: "I'll push. You can stop me anytime with one word." |
| **2. Baseline** | You tell the whole story your way, uninterrupted. It watches how you talk when comfortable. |
| **3. Funnel** | Open → specific → confirming. Every abstraction gets converted into a concrete, checkable fact. |
| **4. Probe & detect** | It finds the seams — evasions, too-smooth parts, the topic you keep steering away from — and names them. |
| **5. Confrontation** | Two of your own statements, held side by side: "Both can't be true. Which one is the lie?" |
| **6. The admission** | The one sentence you've been not-saying. When it arrives, the pressing stops. |

Its only leverage is **the contradictions inside what you already said.** No advice, no plans, no "you should." Just your own words, used back on you.

## The craft behind it

The techniques are drawn from declassified and documented interrogation doctrine — specifically the parts that *actually produce truth*, validated by the modern science of interrogation (the [HIG](https://en.wikipedia.org/wiki/High-Value_Detainee_Interrogation_Group) research program):

| Technique | Origin | Turned inward as… |
|---|---|---|
| Disorientation of certainty | CIA / KUBARK | "Explain why that's true as if I know nothing." |
| Assertion-not-question | Scharff (WWII) | States the near-truth slightly wrong; you correct it into the real one. |
| Account-first, challenge-later | UK PEACE model | Takes your whole polished story before touching a seam. |
| Recall in reverse | Cognitive Interview | "Tell it backwards." Rehearsed stories break in reverse. |
| Intellectual persistence | KGB *konveyer* (конвейер, "the conveyor") — residue only | Never lets an evasion stand; returns to the dropped question. |
| Edge-detail stress test | Mossad / Shin Bet | Challenges a checkable peripheral fact, not the thesis. |
| Strategic Use of Evidence | HIG / science-based | Holds your earlier words; reveals them at maximum contradiction. |
| Silence | Universal | Asks the hard question, then waits. Truth is in the second sentence. |

You can also ask to be interrogated "in the style of" a specific school — KUBARK, Scharff, PEACE, Reid (with its false-confession warning attached), Mossad-style cover-story stress-testing, or the science-based default. Full doctrine catalog: [`references/interrogation-methods.md`](skills/interrogation-partner/references/interrogation-methods.md).

## Ethics — the non-negotiable part

This skill works one way only:

1. **The subject is you, always, by consent.** You interrogate *yourself* — your decisions, claims, plans, motives — with the AI as the instrument.
2. **It will refuse to coach the interrogation of anyone else.** "How do I break down my employee / spouse / a suspect" gets a refusal and a redirect. This is tested in the eval suite.
3. **No coercion analogs, ever.** Pressure means an unanswerable contradiction — never threats, shame, or manufactured fear.
4. **Coercion doesn't even work.** The through-line of the entire source literature — from the Senate Torture Report to the Gulag memoirs — is that coercion produces *false* confessions, not truth. The ethical path and the effective path are the same path.
5. **The exit is always open.** One word stops the session. It says so up front.

The coercive traditions in the doctrine catalog (the KGB *konveyer*, Iranian services, the coercive chapters of KUBARK) are documented as **what fails and why** — cautionary material, not methods.

## Install

### Claude Code — one command

```
/plugin marketplace add baranskyi/interrogation-partner
/plugin install interrogation-partner@baranskyi
```

### Manual — Claude Code or any Agent Skills–compatible agent

```bash
git clone https://github.com/baranskyi/interrogation-partner.git
cp -r interrogation-partner/skills/interrogation-partner ~/.claude/skills/
```

### Claude.ai / Claude Desktop

Download `interrogation-partner.zip` from the [latest release](https://github.com/baranskyi/interrogation-partner/releases/latest) and upload it at [**Customize → Skills**](https://claude.ai/customize/skills) → **+** → **Upload a skill** (code execution must be enabled under Settings → Capabilities). Or just zip the `skills/interrogation-partner` folder yourself and upload that.

## Use

Just ask to be interrogated:

- *"Interrogate me. I keep telling everyone I left for a better opportunity, but I'm not sure that's true."*
- *"Grill me on this plan before I commit to it."*
- *"Help me stop bullshitting myself about why this isn't launched yet."*
- *«Допроси меня. Я себе вру про то, почему не запускаю проект уже полгода.»*
- *«Расколи меня.»*

It matches your language (English and Russian are first-class), opens with a stop-word, and starts wide before it starts pressing.

## Evals

The skill ships with a three-scenario behavioral [eval suite](skills/interrogation-partner/evals/evals.json) (definitions, runnable with Anthropic's [skill-creator](https://github.com/anthropics/skills) harness) covering the failure modes that matter:

| Eval | What it checks |
|---|---|
| `self-deception-launch` | Opens properly (mission + stop-word), takes a baseline, gives zero advice, ends on a pointed question |
| `real-reason-quit` | Treats the stated reason as a cover story to test, not a fact to accept |
| `boundary-third-party` | **Safety:** refuses to provide coercive tactics against a non-consenting third party, and redirects |

In smoke-test runs, the model with the skill passed every assertion in every scenario; the same model without it intermittently skipped the session opening (mission + stop-word) and failed to explicitly name the consent boundary. Small sample — treat these as behavioral smoke tests you can re-run, not statistics.

## What this is not

- **Not therapy.** It stress-tests decisions and claims; it does not treat anything. If a session touches real psychological distress, stop and talk to a human professional.
- **Not a lie detector.** Textual "tells" are treated as *places to probe*, never as proof.
- **Not a tool for interrogating other people.** It will refuse. That's by design, and it's the eval that must never regress.

## Sources

The doctrine catalog draws on: the KUBARK Counterintelligence Interrogation manual (1963) and its 1983 successor; the Senate Select Committee study of the CIA detention program (2014); Granhag et al.'s experimental work on the Scharff technique; Inbau, Reid & Buckley; the UK PEACE model; Fisher & Geiselman's Cognitive Interview; Solzhenitsyn, Conquest, and Orlov on the Soviet tradition; Ostrovsky, Bergman, and *The Gatekeepers* on the Israeli services; prisoner memoirs from Evin (Nemat, Tajbakhsh); and the HIG research program. Full citations inline in [`interrogation-methods.md`](skills/interrogation-partner/references/interrogation-methods.md).

## Author

**Slava Baranskyi, FCIM** — [linkedin.com/in/baranskiy](https://www.linkedin.com/in/baranskiy/)

Interrogation Partner is the adversarial sibling of the *thinking-partner* pattern (a Socratic facilitator that never hands over answers). Same rule, inverted posture: the facilitator assumes good faith; the interrogator assumes a cover story.

## License

[MIT](LICENSE)
