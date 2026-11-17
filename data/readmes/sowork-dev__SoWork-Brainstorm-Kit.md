# SoWork-Brainstorm-Kit

### Stop asking AI for "10 ideas." Make a council argue about yours.

**English · [繁體中文](README.zh-TW.md)**

[![Validate text bundle](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/actions/workflows/validate.yml/badge.svg)](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
**v0.4.0 · Public preview · Text workflow · Built for ChatGPT- and Claude-style chats**

<p align="center"><img src="docs/demo.gif" alt="SoWork Brainstorm Kit: download the text pack, bring a question, let the council begin" width="800"></p>

Drop one text file into an AI chat and name a topic. A cast of famous **fictional** personas proposes ideas, challenges each other's proposals, and hands you a practical plan. You just say **"Continue," "Swap the cast," or "You decide."**

[Try it in 30 seconds](#try-it-in-30-seconds) · [See a full session](locales/en/examples/persona-council.md) · [Real model transcript](examples/test-runs/open-cast-en.md) · [FAQ](#faq) · [Roadmap](docs/roadmap.zh-en.md)

## The problem

Ask a chatbot for campaign ideas and you get ten polite, interchangeable bullets, then homework: "Which one do you like?"

A real workshop works because **people with different instincts push on each other**. This kit makes the AI do that on purpose:

- **Contrasting lenses, not renamed generic advisers.** Each character has a job: propose, challenge one specific idea, or improve how it works.
- **You steer with one word.** Swapping people keeps your topic, constraints, and progress.
- **It ends in a decision.** Comparable directions, a recommendation with its assumptions, and a small first experiment.

No install, Python, or API key. No prompt-writing project.

## Try it in 30 seconds

1. Download **[START-HERE.en.txt](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/raw/main/START-HERE.en.txt)** and attach it to a new ChatGPT or Claude conversation. Ask the AI to confirm it can read the file.
2. Paste this and replace the topic:

```text
Use the attached SoWork-Brainstorm-Kit in LAZY_COUNCIL mode.
My topic: How can a neighborhood bookstore attract repeat visits on a small budget?
Pick a complementary named cast, start proposing now, let them challenge
each other's ideas, then recommend a direction. Do not give me homework.
```

3. Say **"Continue"** whenever you want more. Want a different room? Say *"Give me five filmmakers"* or *"Use David Bowie and Coco Chanel only."*

> *Authored illustration, not a recorded model run.* Topic: a low-budget refill campaign. **Systems lens:** a refill card stamped on visits 3, 6 and 9. **Experience lens:** a stamp card is a chore; make the 3rd refill a ritual with a hand-numbered label. **Revision:** the numbered label doubles as a collectible and a shareable asset. **Output:** three directions, one recommendation, a one-week first experiment.

Full examples: [authored walkthrough](locales/en/examples/persona-council.md) · [recorded GPT-6.1-sol run](examples/test-runs/open-cast-en.md) (see its limitations).

## Use it as a Claude skill

Prefer a reusable skill over attaching a file each time? Copy the folder [`skills/brainstorm-council`](skills/brainstorm-council/SKILL.md) into your Claude skills directory (for Claude Code: `~/.claude/skills/brainstorm-council/`), or zip it and upload it under Settings > Capabilities > Skills in Claude. It is a condensed version of the facilitator protocol; the full text pack above stays the reference for methods and personas.

## Who it's for

Marketers, founders, creators, and small teams who want a better first draft of thinking before a meeting, pitch, or launch.

> **Honest limits.** The cast is fictional role-play inside one AI conversation, not the actual people, authentic quotations, endorsements, or independently deployed agents. This is a portable text workflow, not a native plugin. ChatGPT web acceptance testing is incomplete. Details in the [FAQ](#faq).

## Contents

- [Why use it?](#why-use-it)
- [Quick start](#quick-start)
- [Things to try](#things-to-try)
- [Build your own cast](#build-your-own-cast)
- [Steer the session](#steer-the-session)
- [What a round delivers](#what-a-round-delivers)
- [Examples and test evidence](#examples-and-test-evidence)
- [FAQ](#faq)
- [Repository map](#repository-map)
- [Contribute and validate](#contribute-and-validate)
- [Sources, credits, and rights](#sources-credits-and-rights)

## Why use it?

- **Start with the problem, not a prompt-writing project.** Give a topic; the facilitator selects a method and starts proposing instead of handing you an intake questionnaire.
- **Get contrasting mechanisms, not renamed generic advisers.** Each character has a job: propose, challenge a specific idea, or improve how it works.
- **Change the room without starting over.** Swapping people keeps your topic, constraints, and useful progress.
- **Move from possibilities to a choice.** Compare directions, see a recommendation and its assumptions, then develop a small first experiment.
- **Use the language you work in.** Separate English and Traditional Chinese text packs share stable method and persona IDs.

The reference library contains **31 method cards**, including related variants—not 31 independent theories. In the default **LAZY_COUNCIL** mode, the AI uses these methods to do the ideation. Human practice is available only when you explicitly request **TEACHING**.

## Quick start

**No local installation, Python, or API key is needed to try the text pack.** You need an AI tool/account that can actually read the attachment; the tool's own access requirements still apply.

1. Download one v0.4.0 language pack:
   - **[English · START-HERE.en.txt](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/raw/main/START-HERE.en.txt)**
   - **[繁體中文 · START-HERE.txt](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/raw/main/START-HERE.txt)**
   - [Release notes and assets](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/releases/tag/v0.4.0)
2. Upload **one** complete language pack to a new AI conversation. Ask the AI to confirm it can read it; do not accept a claim based only on the filename.
3. Paste this and replace the topic:

```text
Use the attached SoWork-Brainstorm-Kit in LAZY_COUNCIL mode.
My topic: How can a neighborhood bookstore attract repeat visits on a small budget?
Choose a complementary named cast and a method. Start proposing now,
let the characters challenge and improve specific ideas, then recommend a direction.
State reasonable assumptions for noncritical gaps. Do not give me idea-list homework.
```

Have no topic yet? Say **“Start.”** The intended first response is one short topic question, not a form.

**Replacing an older release?** Download the new pack and start a fresh conversation, or explicitly replace the old attachment and instructions. A repository update does not update a file already in your chat. See [setup](SETUP.md) for attachment and URL-entry alternatives. If release assets are not available yet, use the repository copies of [English](START-HERE.en.txt) or [Traditional Chinese](START-HERE.txt), checking their version headers.

## Things to try

These are **sample inputs**, not reported outcomes:

| Your task | Give the AI this starting point |
| --- | --- |
| Campaign concepts | “Build a space-scientist council for a low-budget refill campaign. Choose five named people.” |
| Product ideas | “Give Ada Lovelace and Leonardo da Vinci a fictional design workshop for a screen-free family game. Exactly two people.” |
| Content angles | “Assemble a Renaissance-artists group for a series about everyday creativity. You pick the people.” |
| Experience design | “Make a Taiwanese-chefs council for a neighborhood food event. Keep it affordable and accessible.” |
| Stress-testing | “Use six fictional perspectives to challenge this launch plan. Keep my budget and deadline.” |
| Solo thinking | “Use just David Bowie as a fictional reinvention lens. Propose, self-critique, and refine.” |

You can request a new theme without knowing its members. The AI should choose named, complementary people rather than send you away to build the roster. Safety and factual uncertainty still apply.

## Build your own cast

Specify a **theme**, **people**, **count**, or any combination:

```text
Choose a group of women scientists for my topic; pick the people yourself.
Use Yang Guifei and Qin Shi Huang only. Do not add a third person.
Give me five filmmakers, not the starter casts.
Expand to six people and keep everyone I already named.
Swap to an architecture council. Keep the same topic, budget, and deadline.
```

For people outside the bundled profiles, the AI creates clearly labeled **fictional editorial thinking roles**. It must not invent quotations, research, life events, or personal positions. When verification is unavailable, the role remains fiction—not a sourced biographical profile. Ambiguous identities may need clarification.

### Optional starter groups

Use these as shortcuts, not the limits of the product:

| Group | Starting lineup | Workshop roles |
| --- | --- | --- |
| **Across the Ages** · 古今綜合組 | Qin Shi Huang · Yang Guifei · David Bowie | Repeatable rules · memorable experiences · identity reframing |
| **Rock Legends** · 熱門搖滾組 | David Bowie · Freddie Mercury · Joan Jett | Reinvention · shared participation · DIY execution |
| **The Glamour Council** · 美美女組 | Yang Guifei · Cleopatra VII · Coco Chanel | Sensory moments · reciprocal alliances · precise editing |
| **The Ruthless Strategists** · 殘暴組 | Qin Shi Huang · Genghis Khan · Napoleon | Hard trade-offs · distributed nodes · focused stress tests |

The English labels are preview localizations; Chinese aliases and stable IDs are retained. These are playful editorial themes—not popularity charts, beauty rankings, historical personality claims, or approval of violence. [Persona guide](locales/en/personas/README.md) · [Bilingual map](docs/bilingual-map.md)

## Steer the session

| Say | Intended behavior |
| --- | --- |
| **Continue** | Develop the recommended direction with a new mechanism or concrete detail. |
| **Swap the cast / replace a member** | Change the requested people, preserve the topic and constraints, then continue ideating. |
| **Make it five people / just two people** | Respect the requested count instead of automatically restoring three. |
| **Go bolder** | Change an assumption or interaction mechanism, not just the adjectives. |
| **Make it practical** | Reduce cost, dependencies, and steps. |
| **Direction 2** | Develop that option without restarting discovery. |
| **You decide** | Choose and expand a direction; do not reset the cast or bounce the choice back. |
| **Teach me to practice brainstorming** | Explicitly enter TEACHING and wait for real human exercises. |

Ordinary council use should not require you to write five or ten ideas first. The topic, known constraints, chosen direction, and current cast should survive short follow-ups.

## What a round delivers

The intended experience is **cast → proposals → concrete challenges and revisions → comparable directions → a recommendation**.

- A named cast with different jobs, not a long biography for each person.
- One or two concrete proposals per character, with the mechanism explained.
- In a multi-person round, at least two specific cross-improvements—not just “I agree.” A one-person request uses self-critique and refinement rather than invented extra speakers.
- Normally three comparable directions, a recommendation, and any unverified assumptions.
- Simple next-step controls so you can keep going without supplying new ideas.

Larger casts may need shorter contributions or multiple rounds. This is not a promise of unlimited context, unlimited output, verified commercial results, or real expert consensus.

## Examples and test evidence

**Keep demonstrations and execution evidence separate:**

- **Authored fiction:** [English council walkthrough](locales/en/examples/persona-council.md) · [中文共創示例](examples/persona-council.md). These illustrate the intended format; they are not recorded model runs.
- **Model-run transcripts:** [English open-cast run](examples/test-runs/open-cast-en.md) · [繁中開放組隊實測](examples/test-runs/open-cast-zh.md). The engine is **GPT-6.1-sol via Hermes provider prompt evaluation**, not ChatGPT web or file-upload acceptance. Read each record for its exact inputs, outputs, source version, and limitations; a linked run is not a universal pass claim.
- **Acceptance criteria and scope:** [Testing guide](tests/README.md) · [Behavioral cases](tests/BEHAVIORAL-ACCEPTANCE.zh-en.md) · [Public-launch review](docs/public-launch-review.zh-en.md).

In this small trial set, a separate AI review marked seven turns as meeting expectations and one Chinese closing brief as partial: the plan is useful, but the five current names are not explicitly visible and the output remains dense. This is not a human rating or a universal pass rate. [Read the full assessment](examples/test-runs/review.zh-en.md).

The badge above reports the repository's **static validation workflow**, not model quality. **ChatGPT browser acceptance remains incomplete: access was blocked by human verification.** Model prompt evaluation does not prove browser attachment handling, repository retrieval, or equivalent behavior in another product/account.

## FAQ

**How many people can the cast have?** Any number the AI tool can handle: one, two, five, six or more. Three is the default, not a hard maximum. New people are fictional editorial lenses, not newly verified biographies; output depth depends on the AI tool's context and response limits.

**Is this a native ChatGPT/Claude plugin or an installed agent framework?**

No. It is a portable text workflow. Uploading instructions does not install a plugin, authorize tools, or create background workers. See [compatibility](locales/en/docs/compatibility.md).

**Are the characters independent agents or the real people?**

Neither. One AI simulates contrasting fictional perspectives in one conversation. They do not run as separately deployed agents, attend your meeting, vote as real participants, or endorse the output.

**Am I limited to the nine profiles, four groups, or three people?**

No. Request any theme, name other people, or let the AI choose them. One, two, five, six or more are valid requests; three is only the default. Actual context, response limits, safety restrictions, and uncertainty can require a smaller or staged round—not a fixed four-group menu.

**Will it ask me to do brainstorming homework?**

Not in default LAZY_COUNCIL mode. The AI proposes and improves ideas. Human exercises are opt-in through [TEACHING](locales/en/TEACHING.md).

**Can I just paste the repository URL?**

Only if the AI can retrieve the actual needed files and confirms what it read. A landing page is not the entire kit. If retrieval fails, use a complete text attachment; see [setup](SETUP.md).

**Is my session private?**

The kit cannot guarantee an AI provider's confidentiality, retention settings, or account policies. Use fictional or anonymized inputs. Never post client data, personal information, private URLs, credentials, or raw private conversations in public Issues or PRs. See [security and privacy](SECURITY.md).

**Can I redistribute or use it commercially?**

Yes. Original material is released under the [MIT License](LICENSE). Third-party method names, trademarks, websites and original teaching materials remain subject to their own rights and are credited in [method sources](locales/en/SOURCES.md) and [persona sources](locales/en/personas/SOURCES.md). The fictional personas are editorial lenses, not endorsements by the real people they reference.

## Repository map

| Area | English | 繁體中文 / shared |
| --- | --- | --- |
| Start and setup | [Text pack](START-HERE.en.txt) · [Setup](SETUP.md) | [文字包](START-HERE.txt) · [使用說明](SETUP.zh-TW.md) |
| Facilitator | [Protocol](locales/en/FACILITATOR.md) | [主持規約](FACILITATOR.md) |
| Methods | [Index](locales/en/methods/index.md) · [Sources](locales/en/SOURCES.md) | [索引](methods/index.md) · [來源](SOURCES.md) |
| Personas and starters | [Guide](locales/en/personas/README.md) · [Sources](locales/en/personas/SOURCES.md) | [人物指南](personas/README.md) · [組合資料](personas/packs.json) · [來源](personas/SOURCES.md) |
| Session templates | [Brief](locales/en/templates/meeting-brief.md) · [State](locales/en/templates/session-state.md) · [Outcome](locales/en/templates/outcome.md) | [準備](templates/meeting-brief.md) · [狀態](templates/session-state.md) · [成果](templates/outcome.md) |
| Quality and direction | [Testing](tests/README.md) · [Changelog](CHANGELOG.md) | [中英對照](docs/bilingual-map.md) · [Roadmap](docs/roadmap.zh-en.md) · [Presentation research](docs/repository-presentation.zh-en.md) |

## Contribute and validate

Useful contributions include **small reproducible behavior reports, clearer translations, source-backed method corrections, and focused tests**. Start with [CONTRIBUTING](CONTRIBUTING.md), [community expectations](CODE_OF_CONDUCT.md), or [open an issue](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/issues/new/choose). Use synthetic examples; do not upload private work sessions.

For local maintenance, use Python 3.10+ and the standard library:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

The build produces separate language packs. Validation checks package consistency, IDs, links, language coverage, and common sensitive-data patterns; it does **not** establish AI quality or platform acceptance. Record actual behavioral evidence separately. See the [roadmap](docs/roadmap.zh-en.md) for priorities and acceptance gates, not promised delivery dates.

## Sources, credits, and rights

Concept and product direction: **CJ Wang**. Method references and persona background sources are credited separately in [method sources](locales/en/SOURCES.md) and [persona sources](locales/en/personas/SOURCES.md). Public reference context is distinct from author-created thinking mechanisms; improvised dialogue is not historical evidence. Do not invent quotations, imitate large passages of copyrighted works, or present proposals as events that already happened.

[Public-material policy](locales/en/docs/sanitization-policy.md) · [Security](SECURITY.md) · [MIT License](LICENSE)
