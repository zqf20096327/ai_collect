<div align="center">

# Woolly

**Your agents share one brain.**

Every AI coding tool starts from zero. Woolly gives Claude Code, Cursor, Codex and Ollama one memory, so you explain your project once. It lives on your laptop, in files you can read.

[![Release](https://img.shields.io/github/v/release/rjcuff/woolly?color=111111)](https://github.com/rjcuff/woolly/releases/latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-111111)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rjcuff/woolly?color=111111)](https://github.com/rjcuff/woolly/stargazers)

[Website](https://usewoolly.com) · [Docs](https://usewoolly.com/docs) · [Download for Mac and Windows](https://usewoolly.com/download) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

![Woolly saving notes for two projects, Claude Code loading only the acme notes at startup, and woolly log showing what each app did](docs/demo.gif)

</div>

## The problem

You explain your stack to Cursor. Then you open Claude Code and explain it again. Then Codex. Each tool keeps its own memory, or none at all, and none of them know what you decided yesterday or what your teammate's agent learned this morning.

Woolly is the memory they share. One folder on your laptop, plain Markdown, no cloud, no account.

## Get started

```sh
curl -fsSL https://usewoolly.com/install.sh | sh
woolly connect
```

That's the whole setup. Claude Code, Claude Desktop, Cursor, VS Code, Windsurf, Codex, Gemini CLI, LM Studio and opencode now read and write the same memory. On Windows, run `irm https://usewoolly.com/install.ps1 | iex` instead.

Prefer an app? [Download Woolly for Mac or Windows](https://usewoolly.com/download). Also on [Homebrew and Linux](https://usewoolly.com/docs/quickstart).

## What you get

**One brain, every tool.** Tell Claude Code once. Cursor, Codex and Gemini already know. [How it works](https://usewoolly.com/docs/how-it-works)

**Sessions that start warm.** Claude Code opens every session with your profile, the project's notes and where you left off. [Connect](https://usewoolly.com/docs/connect)

**Decisions stick.** When a session ends, Woolly saves what you decided, why, and what you ruled out, so no agent pitches it again.

**Facts stay current.** A newer fact replaces the old one. When an AI guesses something that contradicts you, your version wins and the guess is flagged for review.

**Build agents that remember.** A memory layer API with mem0's routes: send a conversation, and a local model adds, updates or retires facts per user, keeping every old version as history. [Memory API](https://usewoolly.com/docs/memory-api)

**It dreams.** While you're away, Woolly merges duplicates, settles facts that changed, and turns your past sessions into lessons for the next one. Nothing is deleted. [Dreaming](https://usewoolly.com/docs/dreaming)

**Your local models remember too.** `woolly proxy` adds memory to Ollama, or any app that uses the OpenAI or Anthropic API. [Proxy](https://usewoolly.com/docs/proxy)

**Memory you can read.** Every memory is a Markdown file. Open it, grep it, edit it by hand, and see which tool saved it. The Woolly app shows the same thing with search. [The app](https://usewoolly.com/docs/review)

**Private by design.** No cloud, no account, no telemetry. Passwords and API keys are refused, and an AI can't plant instructions in your memory. [Security](https://usewoolly.com/docs/security)

**Bring your history.** Drop in your ChatGPT or Claude export and keep the facts that matter. [Import](https://usewoolly.com/docs/import)

**Syncs your machines.** Laptop, desktop and Raspberry Pi stay in step over your own network, encrypted. [Sync](https://usewoolly.com/docs/sync)

## Your team's agents share one project memory

```sh
woolly init
```

Run it in a repo and commit `.woolly/`. Every teammate's agent now reads and updates the same notes: the stack, conventions, decisions, gotchas and commands. Think of it as a CLAUDE.md that keeps itself up to date.

- One fact per line in `.woolly/woolly.md`, so diffs are readable and you can edit it by hand.
- Facts about you never go in the repo.
- Two people adding facts at once don't conflict.

[Project memory](https://usewoolly.com/docs/project-memory)

## Fast on a laptop

On a sample of the [LOCOMO](https://github.com/snap-research/locomo) long-conversation benchmark, Woolly found the right memory for 87% of questions in a median of 23 ms, running entirely on a laptop with Ollama. [Run it yourself](https://usewoolly.com/docs/benchmark)

## Questions

**Do I need Ollama?** No. Woolly works on its own. With Ollama running, it also searches by meaning, learns facts from your chats and saves decisions when a session ends.

**Is this a memory API for my app?** No, on purpose. Woolly makes your own AI workflow better. There are [JavaScript](https://usewoolly.com/docs/javascript) and [Python](https://usewoolly.com/docs/python) packages for scripts and side projects (`npm install woolly-ai` or `pip install woolly-ai`), but if you're adding memory to a product with thousands of users, a hosted memory API is the better fit.

**Does anything leave my machine?** No. There are no Woolly servers.

## Built in public

Woolly ships weekly, and every release is in the [changelog](CHANGELOG.md). Issues, ideas and pull requests are welcome. [CONTRIBUTING.md](CONTRIBUTING.md) explains how the repo is laid out and how to run the tests.

If Woolly saved you from re-explaining your stack one more time, a star helps other people find it.

- [Docs](https://usewoolly.com/docs) and [all commands](https://usewoolly.com/docs/cli)
- [Security](SECURITY.md)
- [Bluesky](https://bsky.app/profile/usewoolly.com) · [LinkedIn](https://www.linkedin.com/company/usewoolly)

MIT license.
