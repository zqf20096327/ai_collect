# Pane

**The open-source app for running AI agents you own.**

You decide who sees your data, not a big tech company.

Pane is an open-source desktop app where you and your AI agents work in the same place. Build agents from scratch (a strategist, a developer, an auditor, a writer, or anything else) or bring the ones you already run on OpenClaw.

You write notes, keep sheets, and organize projects and tasks. Your agents read all of it and, when you let them, write to it too: draft a doc, fill a sheet, create a task and set its due date, run a job at 7 a.m. every weekday, and leave the result in a note. It all lives in one folder on your machine, and you choose which AI provider sees it.

**Download:** signed macOS builds and Linux x86_64 builds (.deb, .rpm, and AppImage) are on the [Releases](https://github.com/ThreeLaneStudios/pane/releases/latest) page and at [paneapp.ai](https://paneapp.ai). macOS 11 or later, Apple silicon and Intel. Free.

**Docs:** [https://paneapp.ai/docs](https://paneapp.ai/docs) · **Support:** join us on Discord: [https://discord.com/invite/PhRd2yGwR8](https://discord.com/invite/PhRd2yGwR8)

## Why Pane

Most people's AI agents aren't loyal to them. The agent lives on someone else's server, runs the model that company picked, and remembers what that company lets it remember. Everything you tell it, that company can read, mine for ads, sell, or hand over when a government asks.

OpenClaw fixed that for people who can run a server and read a config file: your agent, your model, your machine.

Pane is that same idea for everyone else, inside a workspace that already has what a project needs, and with one more freedom: OpenClaw gives you one main agent that spawns helpers, while in Pane any agent can lead a session and bring in any other agent as crew.

Chat, docs, sheets, a task board, jobs, and memory, all in one folder on your machine, with whatever model you choose behind it. And because everything stays in one place, it compounds. Six months in, your agents know what you decided in March and why, which option you turned down and what it would have cost, what is half-finished, and what comes next. The longer you work in it, the more they know, and the less you have to carry in your own head.

You stop forgetting, too: every decision, draft, and finished thing is searchable, so the years add up to a chronicle of what you dedicated your life to and why. You open Pane and pick up where you and your agents left off.

## What you can do in Pane

### The workspace

- Chat with your agents, in every project
- Build and launch custom agents from scratch, as many as you need
- Write in markdown notes with a real editor
- Enter your data in sheets with formulas
- Organize your work in projects with folders and a task board
- Create tasks with status, priority, due dates, and notifications
- Schedule jobs that run on a timer or when something else finishes
- Look back at any work or decision in daily logs
- Attach documents, images, and audio and video files to notes and chats
- Find everything with full-text and semantic search

Everything on that list, your agents can do too. Write the note, fill the sheet, move the task, set up the job: you do it, or you ask and they do it for you. Nothing is agent-only; you can always open the same thing and change it by hand.

### Agents that work in it

Pane writes each agent's identity file from what you tell it, and the file is yours to edit. Agents read anything in the app and write to their own project; each project can have its own crew. They can also generate images, read a dropped file, and fetch a web page, with fetched content treated as untrusted so a page can't talk an agent into editing your notes. Memory and daily logs carry them between sessions.

### Captain & Crew

For every session you pick a captain and a crew from the agents you've made. Any agent can be either; there is no fixed hierarchy. The captain hands work to the crew: each gets its own session and its own brief, they run in parallel, and they report back when they finish. You watch them from one panel.

### Jobs

Schedule anything the agent can do: once, on a cron, or as a wake-up when something else finishes. Each job runs in its own session; when it finishes you get a notification, and clicking it opens that session. The Jobs panel shows what's queued, running, and done. A morning brief, a weekly digest, a recurring research pass, a content machine: set it up once.

### Smart features

Three background tasks, each with its own model picker, separate from chat. Point them at a cheap or local model and your main model only does the real conversation.

- **Smart routing.** A small model reads each message first and decides whether it needs the big one. Simple questions, lookups, and formatting get answered by the small model on the spot; anything with real reasoning goes to your main model. You stop paying frontier-model prices for turns that never needed one.
- **Memory extraction.** After a chat, a model pulls out the facts worth keeping and hands them to the memory pipeline below. Its own picker, so it can run on a local model.
- **Search reranking.** When the agent searches memory, a model re-orders the hits by relevance before they reach the prompt. Optional; search works without it, and you tune the ranking yourself in Settings.

### Bring your own provider

Venice, Ollama, Anthropic, OpenRouter, or OpenClaw. Switch per feature: chat, smart features, semantic search, and image generation can each use a different one. Keys live in your system keychain (macOS Keychain, Secret Service on Linux), never in the database.

## Memory System

Pane agents remember across sessions, and the memory is markdown you can open.

Memory lives in three places:

- **Agent memory**, `~/Pane/.pane/system/{agent}/MEMORY.md`. Who you are, how you like things done, the agent's own style. One file per agent, always in context.
- **Project memory**, `~/Pane/Projects/{project}/Memory.md`. Decisions and facts about that project. Loaded when you work in it.
- **Daily logs**, `~/Pane/.pane/system/{agent}/logs/YYYY-MM-DD.md`. What happened each day, read back at the start of the next session.

**How it gets there.** After each chat, extraction pulls out what is worth keeping. A router (no model call) files each fact into the right place. An end-of-day pass tidies yesterday's log, and a consolidator rewrites a memory file into prose only once it has grown past a threshold. Three writers, one file each ([ADR-0010](docs/adr/0010-three-writer-memory-pipeline.md)). You can also save a fact yourself with the save icon on any chat message, or turn extraction off and save only by hand.

**You stay in control.** The `ai_memory` table in SQLite is the source of truth and the files are views of it, so when you edit or delete a fact in Settings → Memories the files follow at the next pass. Forget means forgotten, not hidden. Agent memory is bounded by category, so it stays small enough for OpenClaw to load on startup.

## Local-first, and as private as you want it

There is no account, no sign-in, and no server. Pane opens straight to Home (your chat, your jobs, your projects) with no network call on the way. Delete the app and the folder and nothing of yours exists anywhere else.

### What leaves your machine

- **Your conversation, to the provider you chose, with your own key.** A model has to see your prompt to answer it, along with whatever the agent reads that turn: notes, memory, and tool results. This is the one thing Pane sends by design. With Ollama, nothing leaves at all. With Venice, the privacy level depends on the model you pick, from zero-retention by contract up to inference inside a hardware enclave (TEE) you can verify. With Anthropic or OpenRouter, you get the models and their terms.
- **An update check** against `updates.paneapp.ai`. Download only; it sends nothing about you.
- **Web pages you ask the agent to read**, and images you ask it to generate, through your provider.
- **Memory extraction and consolidation**, which are model calls to whichever provider Smart Features points at. Point it at Ollama and memory never leaves the machine; point it at a Venice TEE model and it leaves, but once it arrives it runs inside a hardware enclave that even Venice can't open.

What Pane never does: phone home, collect telemetry, or sync your notes anywhere. The repo contains an account and encrypted-sync engine for planned team sharing and a phone app; it is off by default and unreachable in a normal build. See [ADR-0070](docs/adr/0070-local-first-launch-account-behind-flag.md) for exactly what that means.

## If you run OpenClaw

Pane gives your OpenClaw agent a workspace. Point Pane at your OpenClaw machine and the agent you already have shows up as a provider: it chats in Pane, reads your projects, writes docs and sheets, creates tasks, schedules jobs, and spawns crew, with the same tools, the same identity files, and the same memory it has in Discord or the terminal. Your projects become something you and the agent work on together instead of something you describe to it.

The connection is `pane-gateway`, a small Rust service in this repo (`src-gateway/`) that runs on the OpenClaw machine. It accepts connections only from loopback and your tailnet, pairs with an 8-digit code that locks out after ten wrong attempts, and pins its TLS certificate on first pairing. Pane never holds an OpenClaw password; the gateway holds a bearer token that never reaches a log line. Pane and the gateway on the same machine is not a supported layout. The point of the split is that the agent's machine and your data's machine are different boxes.

## Install

macOS: download the DMG from [Releases](https://github.com/ThreeLaneStudios/pane/releases/latest), open it, drag Pane to Applications. The build is signed and notarized. On first launch Pane asks for a provider and a key; after that it opens to Home.

Linux: install the .deb, .rpm, or AppImage from the same Releases page. Keys go to the Secret Service keyring. Linux launched alongside macOS but sees less daily use; what is still being finished is tracked in [#249](https://github.com/ThreeLaneStudios/pane/issues/249). Windows is not supported yet ([#250](https://github.com/ThreeLaneStudios/pane/issues/250)).

Stuck? Ask in [Discord](https://discord.com/invite/PhRd2yGwR8). Guides are at [paneapp.ai/docs](https://paneapp.ai/docs).

## Build from source

You need [Rust](https://rustup.rs/) (`rust-toolchain.toml` pins `1.99.1`; `rustup` installs that version automatically), [Node.js](https://nodejs.org/) `^20.19`, `^22.12`, or `>=24` (the ranges `vite` and `@sveltejs/vite-plugin-svelte` require via their `engines` fields, enforced by this repo's `engine-strict=true`), [pnpm](https://pnpm.io/) 10 or later, the Tauri CLI (`cargo install tauri-cli`), and on macOS the Xcode Command Line Tools (`xcode-select --install`).

```bash
git clone https://github.com/ThreeLaneStudios/pane
cd pane
pnpm install
cargo tauri dev
```

That opens the app in a native window with the dev server attached. Don't run `cargo build` from the repo root; that compiles the Rust backend alone and gives you a stub.

A local `cargo tauri build` produces an unsigned app. Signed, notarized builds come only from the release workflow (`.github/workflows/release-publish.yml`); public releases follow `docs/release-runbook.md`. The OpenClaw gateway is its own crate under `src-gateway/` with its own README.

Tests: `pnpm test` for the frontend, `cargo test` inside `src-tauri/` for the backend, `pnpm test:e2e` for the Playwright harness. The full set CI runs is in `.github/workflows/`.

## How it's built

Pane is built by Matt Carano, who doesn't write code, and three agents who do. Matt decides what gets built, reads every scope and audit, labels every PR and merges every one. The agents run on OpenClaw:

- **Brit** coordinates. She is the only agent with a GitHub account; the issues, PRs, and comments under her name are hers.
- **Reed** scopes and audits. Before anything is built he reads the code at a pinned SHA and writes the scope; after it's built he audits the open PR by running it and reporting what actually happened, not what the PR body says. His verdict is binary.
- **Stia** builds. He may deviate from a scope when the scope is wrong, and has to say so.

The rules that make this work are written down and enforced:

- **Spec first.** Behavior changes need a spec section and an ADR before an issue is filed. `docs/spec/` is the product; `docs/adr/` is why. A CI gate refuses a PR that changes core behavior without a spec reference.
- **Red first.** Every new test is shown failing against the bug before the fix lands, with the red output in the PR body. A test that can't fail is not a test.
- **Guards are proven red.** The guards that matter (the taint gate, the credential-logging check, and the dependency-audit exceptions) were each shown failing before the fix that made them hold, and the threat model records which test proves which guard.
- **The audited SHA is the merged SHA.** Nobody pushes after a PASS.
- **Show the search, not the list.** When a change touches "every place that does X," the scope and the PR must include the command that found those places and its output. A hand-written list of call sites is not accepted.

`docs/dev-hygiene-playbook.md` has the full set. Every scope, audit and fix is written on the issue or pull request it belongs to. The repo was opened from a snapshot, so earlier pull requests stay in a private archive. The open issues came across, and everything from here on is public.

## Where it is

Version 1.0.x. It is new and has not been used at scale, so the parts that only break with many users haven't broken yet.

What's next is in `ROADMAP.md`, in order, with the reasoning behind each item. The issue tracker is where it gets built.

## Contributing

Issues and pull requests are welcome. Read `CONTRIBUTING.md` first: the same gates that apply to the agents apply to you, and a PR without a red-first test or a spec reference won't pass CI. Security reports go to [admin@paneapp.ai](mailto:admin@paneapp.ai) or through GitHub's private vulnerability reporting; see `SECURITY.md`.

Questions, ideas, and show-and-tell: [join the Pane community](https://discord.com/invite/PhRd2yGwR8) on Discord.

## License

Apache-2.0. Copyright 2025–2026 Three Lane Studios LLC.
