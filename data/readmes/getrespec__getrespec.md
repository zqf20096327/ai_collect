# Respec

[![Latest release](https://img.shields.io/github/v/release/getrespec/getrespec?label=release)](https://github.com/getrespec/getrespec/releases)
[![Tests](https://github.com/getrespec/getrespec/actions/workflows/ci.yml/badge.svg)](https://github.com/getrespec/getrespec/actions/workflows/ci.yml)
[![Node.js 20 or later](https://img.shields.io/badge/node-%3E%3D20-339933?logo=nodedotjs&logoColor=white)](https://nodejs.org)
[![Works with Claude Code, Codex, and Cursor](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-2f45c8)](#getting-started)
[![License: FSL-1.1-ALv2](https://img.shields.io/badge/license-FSL--1.1--ALv2-2f45c8)](LICENSE.md)

**English** · [Türkçe](README.tr.md)

**Respec your career for the AI era.**

In games, a *respec* resets your character's skill points so you can redistribute them into a new build. Respec helps software developers move into AI-era roles (AI Engineer, AI Product Engineer, Forward-Deployed Engineer…) through hands-on learning, without throwing away what they already know.

No platform to sign up for: Respec is a folder. Open it with your own coding agent (Claude Code, Codex, Cursor…) and the agent becomes your tutor, evaluator, and career guide.

Respec speaks your language: start with `/respec start` and write in Turkish, German, Spanish… and it will answer in kind.

## How it works

1. **Profile** – reads your CV or asks you a few questions, then runs a short placement assessment.
2. **Role discovery** – recommends 2–3 roles that fit you, based on current job-market data (`data/market/roles.md`). Undecided? It gives you a 1–2 week trial module.
3. **Curriculum** – asks how you want to learn (your goal, how deep to go, which project or domain the examples should come from), maps every skill of the role, and builds a curriculum that skips what you already know. It starts with a role map: what people in that role actually do, and where each module fits.
4. **The loop** – every module goes: lesson (opening with a real situation from your chosen project or domain) → scenario-based quiz → re-teaching of gaps with fresh examples → hands-on assignment → evaluation. The goal is knowing *what to use, where, and when*.
5. **Dashboard** – a local web app with your progress, weak spots, and level (Apprentice → Journeyman → Master). Click a module to read its lesson, review your quiz answers, browse your assignment code, and see how it was evaluated.

## Getting started

```bash
git clone https://github.com/getrespec/getrespec
cd getrespec && claude   # or open the folder with Codex / Cursor
```

Then:

```
/respec start
```

Optionally drop your CV into `learner/cv/` first (PDF or Markdown).

## Commands

| Command | What it does |
|---|---|
| `/respec start` | Builds your profile and runs a placement assessment |
| `/respec role` | Recommends roles that fit you |
| `/respec plan` | Asks a few questions and builds a curriculum for your chosen role (or refines the one you have) |
| `/respec next` | Runs the next step (lesson, quiz, review, assignment) |
| `/respec submit` | Evaluates your assignment |
| `/respec dossier` | Turns a passed assignment into an interview dossier for job applications |
| `/respec dashboard` | Opens the dashboard app in your browser |
| `/respec update-trends` | Refreshes role and job-market data from the web |
| `/respec update` | Updates Respec itself to the latest release |
| `/respec status` | Where you are and what's next |

In agents without custom slash commands (e.g. Codex), just type `respec start`, `respec next`, and so on.

## Recommended model settings

Lesson and evaluation quality depend on the model, so the repo ships with defaults:

| Agent | File | Model | Effort |
|---|---|---|---|
| Claude Code | `.claude/settings.json` | `opus` (currently Opus 5.5) | `medium` |
| Codex | `.codex/config.toml` | `gpt-6.1-sol` | `medium` |

- These are **defaults**, not requirements. Change them in a session with `/model` and `/effort` (Claude Code) or `/model` (Codex).
- Codex only reads project settings when the folder is **trusted**. Trust it when prompted on first launch.
- In Claude Code the `opus` alias always points to the current Opus. To pin a version, use `"model": "claude-opus-5-5"`.
- Keep personal overrides in `.claude/settings.local.json` (git-ignored) or `~/.codex/config.toml`.

## Dashboard

```bash
node scripts/serve.mjs --open      # http://127.0.0.1:4747
```

A read-only app that follows your progress live. The overview shows your level, next step, curriculum, skill map, weak spots, and LLM usage; each module page shows the lesson (with a table of contents and its interactive diagram), quiz history, assignment, your work in `work/`, and the evaluation with evidence linked to the exact line of your code. The server only listens on your own machine and never serves your CV or `.env`.

The app is prebuilt in `dashboard/dist`. To work on it: `cd dashboard && npm install && npm run dev`.

## LLM usage logging

Assignments that call an LLM run through a small local proxy, so you (and the evaluator) can see what each request really cost in tokens and time:

```bash
node scripts/llm-proxy.mjs                 # keep it running in a separate terminal
node scripts/usage-report.mjs              # per module and per model
```

Point your SDK at the proxy in `learner/.env` (the official SDKs read these automatically):

```
OPENAI_BASE_URL=http://localhost:8787/openai/v1
ANTHROPIC_BASE_URL=http://localhost:8787/anthropic
```

OpenRouter (`/openrouter/api/v1`) and Ollama (`/ollama/v1`) work the same way. The proxy records model, token counts, and latency only; prompts, responses, and API keys are never written to disk. The dashboard shows the totals and each module's usage.

## Versions and updates

The installed version is in `package.json`, and [`CHANGELOG.md`](CHANGELOG.md) lists what changed in each release. Releases are published on [GitHub](https://github.com/getrespec/getrespec/releases).

When a new release is out, your agent mentions it at the start of a session and the dashboard shows a notice. Run `/respec update` to install it: the agent shows what's new, checks for files you changed yourself, and pulls the new version. Your `learner/` folder is never touched by an update. To check by hand: `node scripts/check-update.mjs`.

The check asks the GitHub releases API for the latest version, at most once a day; nothing about you or your progress is sent. Set `RESPEC_NO_UPDATE_CHECK=1` to turn it off.

## Privacy

Your CV, progress, assignments, and API keys stay in the `learner/` folder, which is never committed.

## Feedback

After your first module and at the end of each phase, the agent offers a link to a short feedback form on GitHub. It fills in only your Respec version and target role; you write the rest and decide whether to send it. Nothing is sent automatically. You can also [open an issue](https://github.com/getrespec/getrespec/issues/new/choose) any time: something broke, your role or market is missing, or general feedback. Issues are public, so leave out your CV, keys, and files from `learner/`.

## Progress and certification

Your progress in `learner/` is your own learning record: plain files you can read and change, written by the agent on your behalf. That's why it isn't proof of anything, and no certificate is based on it. Certification (coming with the web app) is a separate assessment run on Respec's servers: your capstone's tests and evals, questions about your own design decisions, and a short task you haven't seen before. Each certificate links to a public page where anyone can check what was assessed and when.

## Interview dossier

After you pass an assignment, the agent offers to turn it into an interview dossier, or you can ask for one with `/respec dossier`. You get one HTML file and a PDF copy to send with a job application. The first page explains what you built in plain words, with questions a recruiter can ask without reading code. The rest is for the technical interviewer: 3–5 decisions, your defence answers, the evaluation with its gaps, questions to ask you, and excerpts of your own code at the end. The agent writes the story; scores and code come straight from your evaluation and your `work/` folder, so the two can't drift apart.

- **It's self-reported.** It shows your own agent's evaluation, not a certificate, and the page says so. Interviewers can read how to use one at [getrespec.dev/dossier](https://www.getrespec.dev/dossier/).
- **Sharing it is your choice.** The file is written to `learner/dossier/` and goes nowhere on its own. Before it's rendered you see every code excerpt that will be in it. Your CV, `.env`, and profile are never used, and the renderer refuses to write a file that contains anything shaped like an API key.
- It has no scripts or tracking and opens offline. The PDF is printed with your own Chrome or Edge; without one, open the HTML and print it to PDF. The "Made with Respec" link at the bottom is optional.
- The sample in `examples/learner-demo/dossier/` shows what one looks like.

## Requirements

- A coding agent (Claude Code, Codex, Cursor, …)
- Node.js 20+ (for the dashboard server and the usage proxy; no `npm install` needed)
- For assignments that call an LLM API: an API key (OpenAI, Anthropic, Google) or a local model (Ollama)

## License

Respec's source code is open to read, run, and change, under the [Functional Source License 1.1, Apache 2.0 Future License](LICENSE.md) (FSL-1.1-ALv2). You can use it for any purpose, at work and to train your team included, except one: offering Respec, or something built from it, to others as a competing commercial product or service. Two years after each version is released, that version is also available under the Apache License 2.0.

The license doesn't cover the Respec name or logo. Copyright 2026 [Haluk Coş](https://github.com/thesurvivor).

## Contributing

Contributions are accepted under the same license.

Run the tests with `node --test test/*.test.mjs`. Try the dashboard with sample data: `node scripts/serve.mjs --learner examples/learner-demo`.

Add what your pull request changes under `## [Unreleased]` in `CHANGELOG.md`; CI checks for it. [`RELEASING.md`](RELEASING.md) explains how versions are chosen and how a release is published: a release pull request, which publishes the GitHub release when it's merged.

This README has a Turkish version, [`README.tr.md`](README.tr.md). When you change one, update the other in the same pull request.

Market data lives in `data/market/roles.md` and is refreshed with `/respec update-trends`. Pull requests that add sourced market notes for new countries are welcome.

Respec writes to each learner in their own language, guided by `data/language/<code>.md`. Guides start as agent-written drafts and improve as learners correct them; if you use Respec in your language, reviewing its guide is one of the most useful contributions (see `data/language/README.md`).
