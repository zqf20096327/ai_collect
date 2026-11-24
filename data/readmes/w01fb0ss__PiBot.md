# Pi Bot

**An open-source, local-first AI agent team for your desktop.** Named AI Bots work on your own
computer: chat with one or put several in a group chat, and they plan, run commands, edit files,
browse the web and use your computer, while every risky step waits for your approval. Runs on
macOS, Windows and Linux, with an Android app. Built on the [pi](https://github.com/earendil-works/pi)
agent kernel.

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://github.com/w01fb0ss/PiBot/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/w01fb0ss/PiBot?include_prereleases"></a>
  <img alt="Platforms" src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux%20%7C%20Android-lightgrey">
  <a href="https://pibot.space"><img alt="Website" src="https://img.shields.io/badge/website-pibot.space-8b5cf6"></a>
  <a href="https://pibot.space/en/guides/"><img alt="Docs" src="https://img.shields.io/badge/docs-pibot.space%2Fen%2Fguides-0ea5e9"></a>
</p>

<p align="center">
  <a href="docs/assets/pibot-intro-60s.mp4"><img src="docs/assets/pibot-intro-15s.gif" width="800" alt="Pi Bot in 15 seconds (click for the 60-second video with sound)"></a>
</p>

<p align="center">▶ <a href="docs/assets/pibot-intro-60s.mp4">Watch the 60-second video</a> · <a href="https://pibot.space">Download</a> · <a href="docs/guide/README.md">User guide</a> · <a href="https://pibot.space/en/guides/">Online docs</a></p>

[English](README.md) · [中文](README.zh-CN.md) · [日本語](README.ja.md)

Pi Bot is a desktop app in which a team of named Bots works on your own computer. You chat with a
Bot directly or put several in a group chat, give them a working folder, and they plan, run
commands, edit files and hand work to each other, while every risky step waits for your approval.
The "brain" runs on your machine too: chats, files, memory and keys stay local, and only the
model provider you choose sees the prompts you send.

Website and downloads: <https://pibot.space> · User guide: [docs/guide](docs/guide/README.md) · Online docs: <https://pibot.space/en/guides/>

## What it does

- **Bots and roles.** Create Bots with a name, a role (developer, researcher, writer, translator,
  …), their own model, skills, permissions and memory.
- **Direct and group chats.** A group has a coordinator that plans, hands steps to members and
  collects the results; you confirm the plan before it runs.
- **Working folders and changes.** Bots work inside folders you choose. Every change is listed,
  reviewable and, on macOS, restorable from automatic checkpoints.
- **Approvals and permissions.** Every tool call goes through one policy engine. Commands run in
  a sandbox ([`@anthropic-ai/sandbox-runtime`](https://github.com/anthropics/sandbox-runtime)),
  and approvals, commands and anything sent outward are written to an audit log.
- **Routines and to-dos.** Scheduled, folder-triggered and connection-triggered tasks.
- **Connections.** Apps, MCP servers, skills and knowledge bases.
- **Models.** Local models through Ollama, OpenRouter, your own API keys, and supported
  subscription sign-ins.
- **More devices, optional.** An Android app, runners on other computers or servers, a relay you
  can host yourself, and use from editors over ACP.

Pi Bot runs on macOS 13 Ventura or later, Windows 10 / 11 and 64-bit Linux. It has no telemetry,
and Pi Bot's own servers never receive your chats or files. Besides the model provider you choose,
it connects only for update checks, the websites and searches your Bots use, and features you turn
on (phone, runners, connections), each explained first. See
[docs/privacy](docs/privacy/en/outbound-connections.md) for every outbound connection.

## Install

Download the desktop app from <https://pibot.space>, then follow
[Getting started](docs/guide/en/01-getting-started.md).

## Build from source

Requirements: Node from [`.nvmrc`](.nvmrc) and pnpm 12.

```sh
git clone https://github.com/w01fb0ss/PiBot.git
cd PiBot
nvm use
pnpm install
pnpm dev        # start the desktop app in development
```

Set `PIBOT_DATA_DIR` to keep development data apart from an installed Pi Bot. Other commands:

| Command | Purpose |
|---|---|
| `pnpm check` | Frozen install, typecheck, lint, policy matrix and tests |
| `pnpm check:changed [base]` | The same checks limited to what changed |
| `pnpm verify` | `check`, build, renderer smoke test and the end-to-end acceptance suites |
| `pnpm build` | electron-vite build (no installer) |

## Repository layout

| Path | Contents |
|---|---|
| `apps/desktop` | The Electron app (main process, renderer, packaging) |
| `apps/mobile` | The Android app (React Native + Expo) |
| `apps/relay` | The relay for phone and runner connections (Cloudflare Worker) |
| `apps/runner`, `apps/cli` | The headless runner and command-line entry |
| `apps/plugins` | Bundled plugins (MCP and/or skills) |
| `packages/teams/builtin` | The roles and groups bundled for offline use; the full role library is [pibot-roles](https://github.com/w01fb0ss/pibot-roles) |
| `packages/*` | The brain and its capabilities, in five layers; see [AGENTS.md](AGENTS.md) |
| `docs/guide`, `docs/privacy` | User guide and outbound-connection notes |
| `tests`, `tools` | End-to-end suites, the fake model and development tools |

The agent kernel is [pi](https://github.com/earendil-works/pi), pinned as an npm dependency and
used only in `packages/agent`. The brain does not depend on Electron, so the same code runs
headless.

## Contributing

Issues and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and the rules
in [AGENTS.md](AGENTS.md) first; report security problems as described in
[SECURITY.md](SECURITY.md), not in public issues.

## Contributors

Thank you to everyone who has contributed to Pi Bot. See the
[contribution activity](https://github.com/w01fb0ss/PiBot/graphs/contributors) on GitHub.

<!-- CONTRIBUTORS:START -->
- [@w01fb0ss](https://github.com/w01fb0ss)
- [@juemimgcd](https://github.com/juemimgcd)
- [@eltociear](https://github.com/eltociear)
- [@agooll](https://github.com/agooll)
<!-- CONTRIBUTORS:END -->

## Star History

<a href="https://www.star-history.com/#w01fb0ss/PiBot&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date" />
  </picture>
</a>

## License

[Apache License 2.0](LICENSE). See [NOTICE](NOTICE) and
[THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES) for attributions.
