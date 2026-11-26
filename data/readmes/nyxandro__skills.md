<div align="center">

# nyxandro skills

**Agent skills for Claude Code, Codex, OpenCode and Cursor. Install any of them as a Claude Code plugin from one catalog.**

[![Validate catalog](https://github.com/nyxandro/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/nyxandro/skills/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/nyxandro/skills)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-SKILL.md-6f42c1)](https://agentskills.io/specification)
[![Claude Code marketplace](https://img.shields.io/badge/Claude%20Code-marketplace-d97757)](#install)

**English** · [Русский](README.ru.md)

</div>

A Claude Code plugin marketplace with my agent skills. Each skill lives in its own repository, with
its own versions, releases and changelog. This repository only lists them, so Claude Code can
install any of them from one place. The same skills work in Codex, OpenCode, Cursor and other
agents that read Agent Skills.

## Install

| Agent | Command |
|---|---|
| Claude Code 2.1.275 or later | `/plugin install <skill> --marketplace nyxandro/skills` |
| Older Claude Code | `/plugin marketplace add nyxandro/skills`, then `/plugin install <skill>@nyxandro` |
| Codex, OpenCode, Cursor and others | `npx skills add nyxandro/<skill>-skill` |

Replace `<skill>` with a name from the table below, for example
`/plugin install prod-recon --marketplace nyxandro/skills`. Every installed skill adds its
description to every session, so install only the ones you use.

<details>
<summary>Updates</summary>

<br>

The catalog pins no versions, so every commit to a skill's repository reaches plugin users as an
update. Run `claude plugin marketplace update nyxandro` and then
`claude plugin update <skill>@nyxandro` in your shell, or turn on auto-update for the catalog under
`/plugin` → Marketplaces.

</details>

## Skills

**Planning and quality**

| Skill | What it does | Version |
|---|---|---|
| [feature-blueprint](https://github.com/nyxandro/feature-blueprint-skill) | Writes the feature spec and the implementation plan before any code, with research behind every decision and questions only about what changes the product | ![release](https://img.shields.io/github/v/release/nyxandro/feature-blueprint-skill?label=) |
| [property-testing](https://github.com/nyxandro/property-testing-skill) | Property-based tests with fast-check and Hypothesis, with honest generators and proof that each test can fail | ![release](https://img.shields.io/github/v/release/nyxandro/property-testing-skill?label=) |
| [sparring](https://github.com/nyxandro/sparring-skill) | A second opinion from Claude or Codex on a plan, architecture or code, argued over several turns | ![release](https://img.shields.io/github/v/release/nyxandro/sparring-skill?label=) |
| [skill-picker](https://github.com/nyxandro/skill-picker-skill) | Picks, vets and installs the skills your project's stack needs and shows what's covered | ![release](https://img.shields.io/github/v/release/nyxandro/skill-picker-skill?label=) |

**Running a project**

| Skill | What it does | Version |
|---|---|---|
| [prod-recon](https://github.com/nyxandro/prod-recon-skill) | Read-only check of prod or stage. Finds the server, reads logs and the database, reports and fixes nothing | ![release](https://img.shields.io/github/v/release/nyxandro/prod-recon-skill?label=) |
| [issue-register](https://github.com/nyxandro/issue-register-skill) | Keeps the list of open problems true to the code, in one file, with only what's left to do | ![release](https://img.shields.io/github/v/release/nyxandro/issue-register-skill?label=) |
| [session-handoff](https://github.com/nyxandro/session-handoff-skill) | Carries unfinished work to a new agent session in one document checked against the repository | ![release](https://img.shields.io/github/v/release/nyxandro/session-handoff-skill?label=) |
| [goal-rules](https://github.com/nyxandro/goal-rules-skill) | Lets the agent finish a long `/goal` task while you're away, with recorded decisions and a stop-list | ![release](https://img.shields.io/github/v/release/nyxandro/goal-rules-skill?label=) |
| [owner-decisions](https://github.com/nyxandro/owner-decisions-skill) | Answers a decision question the way you already answered a similar one. Keeps your decisions from all projects in a private base and asks you only what is new | ![release](https://img.shields.io/github/v/release/nyxandro/owner-decisions-skill?label=) |
| [materials-intake](https://github.com/nyxandro/materials-intake-skill) | Takes in a project's incoming materials. Files what's new in `inbox/`, keeps secrets out of git and keeps one inventory of what's there and what it says, with decisions, contradictions and open questions | ![release](https://img.shields.io/github/v/release/nyxandro/materials-intake-skill?label=) |

**Domains**

| Skill | What it does | Version |
|---|---|---|
| [telegram-bot-development](https://github.com/nyxandro/telegram-bot-development-skill) | Telegram bots and Mini Apps against the live Bot API, checking the docs and your installed library before any call | ![release](https://img.shields.io/github/v/release/nyxandro/telegram-bot-development-skill?label=) |
| [t-invest](https://github.com/nyxandro/t-invest-skill) | Access to your T-Invest brokerage account. Portfolio, returns, analytics and trades on your command | ![release](https://img.shields.io/github/v/release/nyxandro/t-invest-skill?label=) |
| [bitrix24-workspace](https://github.com/nyxandro/bitrix24-workspace-skill) | Read-only access to your Bitrix24 workspace. Chats, tasks, projects, Drive files, mail, calendar and meeting summaries from the live portal | ![release](https://img.shields.io/github/v/release/nyxandro/bitrix24-workspace-skill?label=) |

Each skill's README says what it needs and how to use it.

<details>
<summary>How the catalog works</summary>

<br>

- `.claude-plugin/marketplace.json` has one entry per skill that points to the skill's own
  repository. Claude Code reads it when you add the catalog.
- On every push, GitHub runs `claude plugin validate --strict` on the catalog, so a broken entry
  can't quietly break installs for everyone.
- Versions, releases and changelogs live in each skill's repository, not here.

```text
.claude-plugin/marketplace.json   the catalog, one entry per skill
.github/workflows/validate.yml    the catalog check on every push
README.md, README.ru.md           this page in English and in Russian
```

</details>

## License

[MIT](LICENSE), for the files of this repository. It doesn't cover the skills themselves, see each
skill's repository.
