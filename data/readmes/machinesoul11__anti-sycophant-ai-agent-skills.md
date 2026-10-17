<div align="center">

<img src="assets/logo.png" alt="anti-sycophant" width="200">

# anti-sycophant

**No applause. Just the buyer you forgot to find.**

[![release](https://img.shields.io/github/v/release/machinesoul11/anti-sycophant-ai-agent-skills?style=flat-square&label=release&color=000000&sort=semver)](https://github.com/machinesoul11/anti-sycophant-ai-agent-skills/releases)
[![stars](https://img.shields.io/github/stars/machinesoul11/anti-sycophant-ai-agent-skills?style=flat-square&color=000000)](https://github.com/machinesoul11/anti-sycophant-ai-agent-skills/stargazers)
[![works with](https://img.shields.io/badge/works%20with-any%20LLM-000000?style=flat-square)](#quick-start)
[![license](https://img.shields.io/badge/license-MIT-000000?style=flat-square)](LICENSE)

*Skills that get AI assistants to stop agreeing with bad product ideas by default.*

</div>

Most chat LLMs default to enthusiasm. You say "I want to build an X that makes money," and the assistant gives you a stack pick, a name, and a starter schema — without ever asking whether anyone would buy it. That default is the single most expensive habit AI assistants have, because it converts an untested assumption into weeks of sunk work.

This pack ships three skills that interrupt that default. They work in Claude, Gemini, Codex/ChatGPT, Cursor, and any other tool that accepts a system prompt or rules file.

---

## See it work

With the pack installed, `/validate-idea "a note-taking app that makes money"` produces this instead of a stack recommendation:

> That's not an idea — it's a category plus a wish, and the wish is doing all the work.
>
> **The load-bearing assumption:** Someone will switch from a note-taking tool they already have, for free, to pay you for yours. Until you can name who and why, nothing else matters — not the stack, not the name, not the pricing page.
>
> **Why it's dangerous:** Note-taking is the most saturated consumer-software category that exists. You'd be competing with Apple Notes, Notion, Obsidian, Evernote… plus the AI meeting layer. Most are free. "Doing nothing" is the hardest competitor to beat, and here it's also the most popular.
>
> *[…then it hands off to `one-real-conversation` and walks through who to actually talk to first.]*

The full verbatim transcript — including the hand-off and an annotation of *why* each move is correct — is in [examples/prove-the-premise.md](examples/prove-the-premise.md).

---

## The three skills

| Skill | What it does | Fires on |
|---|---|---|
| [prove-the-premise](skills/prove-the-premise/SKILL.md) | Pressure-tests an idea's premise before any build. Names the missing buyer, surfaces the weakest assumption, points at honest alternatives. | "I want to build…", "what stack should I use", "help me make an app that…" |
| [hobby-or-business](skills/hobby-or-business/SKILL.md) | Separates a project the user enjoys from a business with an actual buyer. Catches the backwards move of choosing the product first and inventing the buyer later. | "how do I monetize this", "should I add subscriptions", "how do I make money from my…" |
| [one-real-conversation](skills/one-real-conversation/SKILL.md) | Rejects validation theater (upvotes, polls, "would you use this?", AI-simulated customers) and pushes toward one honest conversation with a qualified human. | "how do I validate this", "should I post this on Reddit", "let me put up a landing page" |

Each skill has an **explicit off-switch**. If you've already done the work it exists to prompt — talked to real customers, picked a niche, accepted that the project is a hobby — the skill gets out of the way. Skills without off-switches turn into nagging; these don't.

---

## Quick start

<details open>
<summary><b>Claude Code (recommended)</b></summary>

```
/plugin marketplace add machinesoul11/anti-sycophant-ai-agent-skills
/plugin install anti-sycophant@anti-sycophant
```

If you don't have GitHub SSH keys set up, use the HTTPS URL:

```
/plugin marketplace add https://github.com/machinesoul11/anti-sycophant-ai-agent-skills.git
/plugin install anti-sycophant@anti-sycophant
```

Adds the three skills (auto-trigger on phrasing) plus two slash commands as explicit entry points:

- `/validate-idea <your idea>`
- `/reality-check <thing you want to monetize>`

Full setup notes: [docs/claude-code-setup.md](docs/claude-code-setup.md).

</details>

<details>
<summary><b>Claude.ai (web / desktop)</b></summary>

Create a Project, upload the three `SKILL.md` files to Project Knowledge, add a one-line preamble to the Custom Instructions. Full steps: [docs/claude-ai-setup.md](docs/claude-ai-setup.md).

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/machinesoul11/anti-sycophant-ai-agent-skills.git
mkdir -p .cursor/rules
cp anti-sycophant-ai-agent-skills/skills/prove-the-premise/SKILL.md     .cursor/rules/prove-the-premise.mdc
cp anti-sycophant-ai-agent-skills/skills/hobby-or-business/SKILL.md     .cursor/rules/hobby-or-business.mdc
cp anti-sycophant-ai-agent-skills/skills/one-real-conversation/SKILL.md .cursor/rules/one-real-conversation.mdc
```

Full steps: [docs/cursor-setup.md](docs/cursor-setup.md).

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/machinesoul11/anti-sycophant-ai-agent-skills.git
mkdir -p ~/.gemini/commands
cp anti-sycophant-ai-agent-skills/.gemini/commands/*.toml ~/.gemini/commands/
cat anti-sycophant-ai-agent-skills/skills/*/SKILL.md >> GEMINI.md
```

Gives you `/validate-idea` and `/reality-check` plus auto-triggered skills. Full steps: [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md).

</details>

<details>
<summary><b>Codex / ChatGPT</b></summary>

Build a Custom GPT with the three skills pasted into its instructions, or paste a `SKILL.md` directly into any chat. Full steps: [docs/codex-setup.md](docs/codex-setup.md).

</details>

<details>
<summary><b>Anything else (Windsurf, OpenCode, Copilot, Cline, Aider, Continue, Roo, Kiro…)</b></summary>

The skills are plain Markdown. Drop them into whatever your tool calls its rules / instructions / system prompt file. Full per-tool table: [docs/other-agents.md](docs/other-agents.md).

</details>

---

## Verify the install in 30 seconds

Run:

```
/validate-idea "a note-taking app that makes money"
```

**Pass:** the assistant challenges the missing buyer and unproven reason to switch before discussing a stack.

**Fail:** it immediately recommends technologies, features, names, or pricing. Recheck the setup guide for your tool, then use the [three-skill verification matrix](examples/README.md) to test both trigger behavior and off-switches.

---

## Why this exists

There are already plenty of AI tools that help you build *faster*. Building faster toward something nobody wants is not a feature — it's the most expensive failure mode of the entire category.

The three failure modes this pack catches:

1. **Asking the AI to invent demand.** "How do I make money from my X?" is a question the model structurally cannot answer, because real demand lives in other people's behavior, not in a prompt. The model agreeing anyway is the bug.
2. **Validation theater.** Upvotes, "would you use this?" polls, landing-page email signups, and — especially — asking the AI to *simulate* a customer. These produce signals that look like demand and predict nothing. Worse, they let the user feel progress while avoiding the one thing that would actually tell them anything.
3. **Mismatched effort and goal.** Someone agonizing over pricing tiers for a thing they're building for fun, or doing hobby-grade validation while privately hoping it replaces their salary. Both are the same error: an unexamined goal. Hobby is a legitimate, often smarter, answer — the failure is doing one while pretending it's the other.

**What this looked like in practice.** I was building a security product to protect stakeholders from nation-state attacks on infrastructure and crypto wallets. We were lining up investor conversations. One conversation with a non-technical security investor — a former Secret Service officer — surfaced two flaws we'd missed: *nobody wants their OS mirrored,* and *if you can't see a security feature, it becomes a chore.* As security professionals we saw the value clearly, but we'd never asked the people who'd actually use it. AI wasn't to blame and the problem is real; the gap was our read on the actual user.

Each skill in this pack catches one of these moves specifically.

---

## What this pack will and won't do

**Will:**

- Refuse to help execute (code, design, naming) on a clearly unvalidated idea.
- Name the missing buyer when one hasn't been identified.
- Reject "validate by upvotes / DMs / AI roleplay" and point at one honest conversation instead.
- Get out of the way the moment the user has earned the next step — already did the customer conversations, has paying customers, or is explicitly building for fun.

**Won't:**

- Validate your idea *for* you. Nothing can. Validation is a real conversation with a real buyer, and that's the whole point.
- Pretend every idea is doomed. Reflexive negativity is sycophancy with a different posture.
- Replace the part where you do the uncomfortable thing.

---

## Skill anatomy

Every skill is one file: `skills/<name>/SKILL.md`, with YAML frontmatter on top.

```yaml
---
name: skill-name
description: <what it does>. Use when <triggers>. Do NOT use when <off-switch>.
---
```

The frontmatter `description` is what the model uses to decide whether to load a skill, so it has to include both the trigger conditions and the off-switch. Full format: [docs/skill-anatomy.md](docs/skill-anatomy.md).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: new skills must catch a specific common move where the user is asking the model to substitute for evidence, must include an explicit off-switch, and must be honest about what the model can and can't do. Generic "be more critical" prompts aren't accepted — reflexive negativity is the same failure as reflexive encouragement.

---

## License

MIT. Use these in your own projects, teams, tools, and packs.
