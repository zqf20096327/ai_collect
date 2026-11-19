<div align="center">

# Woolly

**Memory that knows when it's wrong.**

One local memory for Claude Code, Cursor and Codex. Every fact points at its code, and Woolly flags the ones that go stale.

[![Release](https://img.shields.io/github/v/release/rjcuff/woolly?color=111111)](https://github.com/rjcuff/woolly/releases/latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-111111)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rjcuff/woolly?color=111111)](https://github.com/rjcuff/woolly/stargazers)

[Website](https://usewoolly.com) · [Docs](https://usewoolly.com/docs) · [Download for Mac and Windows](https://usewoolly.com/download) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

![Woolly saving notes for two projects, Claude Code loading only the acme notes at startup, and woolly log showing what each app did](docs/demo.gif)

</div>

## The problem

You switch between Claude Code, Cursor and Codex on the same repo, and each one starts from zero. You explain the pin map again, the config value you settled on, the gotcha that cost you a day. Tools that do remember have a worse problem. They keep repeating facts the code stopped backing up weeks ago, and your agent follows them with confidence.

Woolly is project memory your coding agents can trust. It runs on your machine, and it knows when a fact goes stale. Every fact points at the file, function or lines it's about. When that code changes, Woolly marks the fact stale instead of letting your agent follow it.

```
$ woolly check
Checked 24 facts in drone against 4e1c9a2.
  stale  imu_read_accel returns raw counts; divide by 16384 for g
         main/imu.c: imu_read_accel was renamed to imu_read_accel_g in 4e1c9a2
1 fact went stale. Run woolly review to confirm, fix or retire it.
```

## Get started

```sh
curl -fsSL https://usewoolly.com/install.sh | sh
woolly connect
woolly init --hooks   # in your repo
```

Claude Code, Cursor, Codex, Gemini CLI, VS Code, Windsurf, Claude Desktop, LM Studio and opencode now share one memory for the repo, and every commit checks it against the code. On Windows, run `irm https://usewoolly.com/install.ps1 | iex` instead.

Prefer an app? [Download Woolly for Mac or Windows](https://usewoolly.com/download). Also on [Homebrew and Linux](https://usewoolly.com/docs/quickstart).

## Check the notes your agents already read

```sh
cd your-repo
woolly check
```

No setup. Woolly reads CLAUDE.md, AGENTS.md, Cursor rules, Copilot instructions, Claude Code's auto memory, Codex memories and claude-mem, and flags every line that names a function, file or script the code no longer has, with the commit that changed it. `woolly check --fix` rewrites renamed names and moved paths for you. [Check your agent files](https://usewoolly.com/docs/memory-files)

## What you get

**It knows when a fact goes stale.** On every commit and on `woolly check`, each fact is checked against the code it points at. Rename a function, delete a file or change a pin number, and the fact that relied on it is flagged with the commit that broke it. `woolly review` lets you confirm, fix or retire it. [Stale facts](https://usewoolly.com/docs/stale-facts)

**`woolly why` explains any line.** Point it at a file, a line or a function and it shows the decisions and gotchas behind it, what was rejected, and whether the code still backs each one up. Agents ask it too before changing code. [Why is this code like this](https://usewoolly.com/docs/why)

**Pull requests say what they break.** A GitHub Action comments when a change makes a project fact stale, so the whole team sees it before it merges. [Pull request checks](https://usewoolly.com/docs/pull-requests)

**Every fact cites its source.** A file, function or line range, the commit it was saved at, and the session it came from.

**One memory for every agent on the repo.** Claude Code, Cursor and Codex read and update the same notes, and teammates get them through git. [Project memory](https://usewoolly.com/docs/project-memory)

**Sessions that start warm.** Each session opens with a short brief with the project's current facts, where you left off, and which facts were kept out because the code changed. `woolly caught` counts every one, with a badge for your README. [Connect](https://usewoolly.com/docs/connect)

**Decisions stick.** When a session ends, Woolly saves what you decided, why, and what you ruled out, so no agent pitches it again.

**Facts keep their history.** Nothing is deleted. A replaced or stale fact stays on disk with the date it stopped being true. When an AI contradicts something you said, your version wins.

**It dreams.** While you're away, your local model merges duplicates, settles facts that changed, and turns past sessions into lessons. The next session starts with what it did, and `woolly recap` shows it too. [Dreaming](https://usewoolly.com/docs/dreaming)

**Fully local.** No cloud, no account, no telemetry. Ollama is optional, and stale detection never needs a model. Passwords and API keys are refused, and an AI can't plant instructions in your memory. [Security](https://usewoolly.com/docs/security)

**Memory you can read.** Every memory is a Markdown file. Open it, grep it, edit it by hand, and see which tool saved it. [The app](https://usewoolly.com/docs/review)

### Also in Woolly

- **Personal memory** that follows you across every AI app. [How it works](https://usewoolly.com/docs/how-it-works)
- **Memory for the agents you build**, with an API shaped like mem0's and Python and JavaScript packages. [Memory API](https://usewoolly.com/docs/memory-api)
- **Memory for Ollama** and any OpenAI or Anthropic app, with `woolly proxy`. [Proxy](https://usewoolly.com/docs/proxy)
- **Import** your ChatGPT or Claude history, and **sync** your machines over your own network. [Import](https://usewoolly.com/docs/import) · [Sync](https://usewoolly.com/docs/sync)

## Your team's agents share one project memory

```sh
woolly init
```

Run it in a repo and commit `.woolly/`. The first time, it brings in what your CLAUDE.md, AGENTS.md and Cursor rules already say, and points those facts at the code. Every teammate's agent now reads and updates the same notes on the stack, conventions, decisions, gotchas and commands. Think of it as a CLAUDE.md that keeps itself up to date and checks itself against the code.

- One fact per line in `.woolly/woolly.md`, so diffs are readable and you can edit it by hand.
- Facts about you never go in the repo.
- Two people adding facts at once don't conflict.

[Project memory](https://usewoolly.com/docs/project-memory)

## Fast on a laptop

On a sample of the [LOCOMO](https://github.com/snap-research/locomo) long-conversation benchmark, Woolly had the answer in its top 20 results for 83.2% of 382 questions, 95.6% for questions about dates and time, in a median of 19 ms. It runs entirely on a laptop with Ollama. [Run it yourself](https://usewoolly.com/docs/benchmark)

## Questions

**Do I need Ollama?** No. Woolly works on its own, and stale detection never needs a model. With Ollama running, it also searches by meaning and picks out decisions and gotchas when a session ends.

**How is this different from other memory tools?** Most remember what a conversation said. Woolly also checks it against the code: every project fact cites its source, and when the code changes, the fact is flagged instead of trusted. It runs on your own machine with no cloud, works with every agent at once, and uses a local model only.

**Is this a memory API for my app?** It has one, shaped like mem0's, with [JavaScript](https://usewoolly.com/docs/javascript) and [Python](https://usewoolly.com/docs/python) packages. But Woolly is built first for your own coding agents. If you're adding memory to a product with thousands of users, a hosted memory API is the better fit.

**Does anything leave my machine?** No. There are no Woolly servers.

## Built in public

Woolly ships weekly, and every release is in the [changelog](CHANGELOG.md). Issues, ideas and pull requests are welcome. [CONTRIBUTING.md](CONTRIBUTING.md) explains how the repo is laid out and how to run the tests.

If Woolly saved you from re-explaining your stack one more time, a star helps other people find it.

- [Docs](https://usewoolly.com/docs) and [all commands](https://usewoolly.com/docs/cli)
- [Security](SECURITY.md)
- [Bluesky](https://bsky.app/profile/usewoolly.com) · [LinkedIn](https://www.linkedin.com/company/usewoolly)

MIT license.
