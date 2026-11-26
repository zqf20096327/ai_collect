<p align="center">
  <img src="assets/mash-logo.svg" alt="Mash logo" width="320">
</p>

<p align="center">
  <a href="https://github.com/mashhq/mash/actions/workflows/ci.yml"><img src="https://github.com/mashhq/mash/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/mashhq/mash/actions/workflows/windows.yml"><img src="https://github.com/mashhq/mash/actions/workflows/windows.yml/badge.svg?branch=main" alt="Windows"></a>
  <a href="https://github.com/mashhq/mash/actions/workflows/desktop.yml"><img src="https://github.com/mashhq/mash/actions/workflows/desktop.yml/badge.svg?branch=main" alt="Desktop"></a>
  <a href="https://getmash.io"><img src="https://github.com/mashhq/mash/actions/workflows/docs.yml/badge.svg?branch=main" alt="Documentation"></a>
  <a href="https://github.com/mashhq/mash/releases/latest"><img src="https://img.shields.io/github/v/release/mashhq/mash" alt="Latest release"></a>
  <a href="#licence"><img src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg" alt="MIT or Apache 2.0 licence"></a>
  <a href="https://discord.gg/jsxVgVn36"><img src="https://img.shields.io/badge/Discord-join%20the%20chat-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

# Mash: The Multi-Agent Search History Tool

[Español](docs/es/index.md) · [Français](docs/fr/index.md) · [简体中文](docs/zh-cn/index.md) · [日本語](docs/ja/index.md)

Search the chats your coding agents already saved, find the message behind a
decision, and pick up work in another agent. Mash is open source and self-hosted.
By default, indexing and search stay on your machine and require no account.
[How Mash handles your history](docs/privacy.md)

[Try the demo without installing](https://getmash.io/demo/#/search?q=checkout) · [Quick start](#quick-start) · [Docs](https://getmash.io/guides/)

[![Supported agents: Claude Code, Codex, GitHub Copilot, Cursor, OpenCode, Antigravity](assets/supported-agents.svg)](docs/supported-agents.md)

[![Mash dashboard showing the original sign-in decision in a Claude Code conversation](assets/screenshots/dashboard.webp)](https://getmash.io/demo/#/chat/sign-in-tokens?node=laptop&message=sign-in-tokens-2)

<span id="why-mash"></span>

## Highlights

- **Pick up work in another agent.** Ask an agent connected over MCP to find
  the decision you made, cite the original message, and tell you what’s still open.
  [Follow a Claude Code to Codex handoff](docs/pick-up-work.md#follow-a-sample-handoff)
- **Multi-agent search.** Search by word or exact phrase across chats that
  Claude Code, Codex, GitHub Copilot, Cursor, OpenCode, and Antigravity already
  saved. [Supported histories](docs/supported-agents.md)
- **Multi-machine search.** Find a chat from your workstation on your laptop
  through an optional Mash server you run. Each machine keeps a local index
  it can search offline. [Search across your machines](docs/search-across-machines.md)
- **Jump straight to the original message.** Read the surrounding conversation
  and tool output in the dashboard.
  [Open the checkout outage chat](https://getmash.io/demo/#/chat/checkout-outage-review?node=build-box&message=checkout-outage-review-1&shared=true)
- **Save decisions with a source.** Ask a connected agent to remember a
  decision, then follow its supporting quote back to the chat.
  [Open the saved sign-in decision](https://getmash.io/demo/#/record/record-sign-in-tokens?node=laptop)
- **Export a whole conversation.** Save it from the dashboard as Markdown,
  HTML, or PDF. [Export a transcript](docs/dashboard.md#save-a-transcript)
- **Search from Raycast.** Find a past chat from Raycast as you type, read
  it there, or open it in its agent. [Mash for Raycast](#mash-for-raycast)
- <img src="dashboard/public/mashy.png" alt="" width="20"> **Mashy, an optional dashboard assistant.**
  Bring your own model service and API key to ask questions about your history
  and get links to chats and saved decisions.
  [Set up Mashy](docs/mashy.md#set-up-mashy)
- **GPU acceleration for semantic search.** Optional embeddings use DirectML
  on supported Windows GPUs, Core ML on Apple silicon, or the CPU when local
  acceleration is unavailable. Indexing can also use a configured remote worker.
  [Embedding inference](docs/configuration.md#embedding-inference)

<details>
<summary>See Mashy answer a question</summary>

![Asked what caused the checkout outage last week, Mashy traces it to a database migration and quotes the Claude Code chat it came from](assets/mashy-answer.webp)

</details>

## Quick start

Already using Mash? [Upgrade your installation](docs/upgrades.md#upgrade-an-existing-installation).

By the end you'll have every chat your coding agents saved on this machine
in one searchable place, and an agent that remembers your decisions.

### Download the app

The Mash app is the quickest start: [download it for macOS, Windows or
Linux](docs/downloads.md#desktop-app), open it, and it walks you through
setup. Prefer the terminal, or setting up a server? Install with a command
instead.

### Install it yourself

Run the command for your system. It downloads Mash and opens setup in your
browser. You’ll need at least one saved chat from a [supported agent](docs/supported-agents.md).
See [what setup changes](docs/installation.md#what-setup-changes) and
[how to verify the download](docs/downloads.md#verify-the-checksum).

**macOS (Apple silicon) or Linux (x86-64 or ARM64)**

Linux and WSL require a [systemd user session](docs/local-search.md#linux-without-a-systemd-user-session).

```bash
curl -fsSL https://raw.githubusercontent.com/mashhq/mash/main/install.sh | sh -s -- --dashboard
```

**Windows x64 or ARM64 (PowerShell)**

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/mashhq/mash/main/install.ps1))) -Dashboard
```

Open the link the installer shows you and leave the terminal open.

### Choose what Mash reads

Setup lists the agent histories it found on this machine. Pick the agents,
how far back to go, and which agents should be able to search Mash. Then
choose **Set up and index**. Your original chats are only read, never changed.

![Setup lists the histories Mash will read, how far back it goes, and which agents it connects to](assets/screenshots/setup.webp)

You can skip connecting agents or clear any preselected agents.
[See every setup step](docs/dashboard.md#set-up-mash-from-the-dashboard)

<span id="try-it"></span>

### Find your first chat

When setup says search is ready, type a word you remember into the search
box at the top: an error message, a function name, a ticket number. Mash
searches every agent at once and highlights where each chat matches.

![Searching for “checkout” finds a saved memory, a Codex chat and a Claude Code chat, with the matching words highlighted and the selected chat previewed beside them](assets/screenshots/search.webp)

Use the filters to narrow the results to one agent, machine, project or time.
[Ways to search](docs/search.md#your-first-search) ·
[Find a missing chat](docs/find-missing-chat.md)

### Read it in context

Open a result and Mash takes you to the exact message, with the conversation
around it. The left column lists your own prompts in that chat, so you can
jump between them, and the other sessions from the same project.

![A chat opened at its matching message, with your prompts and the project’s other sessions beside it](assets/screenshots/chat.webp)

Choose **Find in chat** to search inside a long conversation, or
**Export** to save it as Markdown. [Find and read a chat](docs/dashboard.md#find-and-read-a-chat)

### Let your agent remember

Connect an agent during setup and it can save what you decide, quoting the
message where you said it. Just ask:

> Remember that this project keeps its refresh tokens in the device keychain.

Open **memory** to see every decision and preference your agents saved.

![The memory page lists saved decisions and preferences with their project, machine and agent, with the selected decision and its evidence beside them](assets/screenshots/memory.webp)

Each one keeps its evidence. Choose **open the message** to read the exact
words it came from. A later session can ask Mash what was decided and why.

![A saved decision with the reason, the quoted message it came from, and its revision history](assets/screenshots/record.webp)

[Use Mash memory](docs/records.md) · [Connect an agent](docs/agents.md#connect-claude-code-codex-or-copilot)

### See it all at a glance

The overview is where the dashboard opens. It shows your latest chats, the
newest memories, and how many chats each machine and agent has.

![The overview: the chat to pick up where you left off, counts of chats, memories, machines and agents, then recent chats beside the memories waiting for confirmation](assets/screenshots/overview.webp)

To reopen the dashboard later, run `mash dash` and open the address it prints.
If your terminal can’t find `mash`, use the full path shown during setup or
[add Mash to your PATH](docs/troubleshooting.md#mash-command-not-found).

### Keep going

- **Search every machine.** Share chats from your laptop and workstation
  through a Mash server you run. [Set up a shared index](docs/shared-index.md)
- **Ask Mashy.** Ask questions about your history in plain language and
  follow the answer back to its sources. [Ask Mashy](docs/mashy.md)
- **Search from the terminal.** `mash search 'refresh token'` works anywhere.
  [Search from the terminal](docs/search.md#your-first-search)
- **Export chats.** Save many chats at once as Markdown, JSON or a Mash
  archive. [Export many chats](docs/dashboard.md#export-many-chats-at-once)
- **Open it on your phone.** Reach the dashboard from another device.
  [Open the dashboard elsewhere](docs/dashboard-access.md)

### Ask your agent

Prefer to let your agent do the setup? Paste this into Claude Code, Codex, or
another coding agent.

> Read https://getmash.io/setup.md and set up Mash on this machine.
> Review the choices with me first.

If you already have the [Mash plugin](docs/plugin.md#start-with-the-plugin),
ask your agent to use its `setup` skill. If you installed Mash yourself, you
can [connect an agent later](docs/agents.md#connect-claude-code-codex-or-copilot).

<span id="build-from-source"></span>

For package managers, source builds, or terminal setup, see the
[installation guide](docs/installation.md). To try Mash with less history,
follow the [local trial guide](docs/privacy.md#try-a-small-local-setup).

<!-- quick-start-end -->

## Mash for Raycast

On a Mac, the Raycast extension searches your chats as you type, shows the
passage that matched, and opens a chat in Mash, Claude or Codex. A second
command lists the decisions and notes Mash remembers.

![Mash in Raycast: a search for “customers” lists matching chats under Today and This week, each with its agent’s tile, project and age](raycast/metadata/mash-1.png)

The extension is waiting for review in the Raycast Store. Until it is
listed, you can [run it from this repository](raycast/README.md#development).

## Privacy

With the default local setup, indexing and search stay on your machine.
Sharing history across your machines is optional.

Mash masks recognizable credentials in results by default, but detection is
best effort. Local history and exports can contain sensitive text;
treat backups like the original chats. Mash never modifies the contents of
the agent’s source history. When an agent searches through Mash, the results
it receives become part of that agent's context. [Privacy and redaction →](docs/privacy.md)

## Tested with

See [how each agent's history has been tested on Linux, macOS, and Windows](docs/supported-agents.md#tested-with).
[Linux CI](https://github.com/mashhq/mash/actions/workflows/ci.yml) · [Windows CI](https://github.com/mashhq/mash/actions/workflows/windows.yml) · [Docs checks](https://github.com/mashhq/mash/actions/workflows/docs.yml)

## Documentation and contributions

[Browse the guides](docs/README.md), [get help with a problem](docs/troubleshooting.md),
or [report a security concern privately](SECURITY.md#report-a-vulnerability).
[Architecture overview](docs/architecture.md) ·
[Download and verify a release archive](docs/downloads.md).
To fix a guide, improve a translation, or send a code change, see [Contributing](CONTRIBUTING.md#where-to-start).

## Licence

Mash is licensed under either the [MIT licence](LICENSE-MIT) or the
[Apache License 2.0](LICENSE-APACHE), at your option.
