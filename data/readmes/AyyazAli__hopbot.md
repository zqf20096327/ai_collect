<p align="center">
  <img src="docs/assets/banner.jpg" alt="HopBot: your crew of AI agents, always on" width="100%">
</p>

<p align="center">
  <img src="docs/brand/hopper-mark.svg" alt="" width="88">
</p>

<h1 align="center">HopBot</h1>

<p align="center">
  <b>A crew of AI agents with their own names, memory, screens and servers.</b><br>
  Free and open source. Bring your own key.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache 2.0" src="https://img.shields.io/badge/license-Apache%202.0-blue"></a>
  <img alt="macOS 13+" src="https://img.shields.io/badge/macOS-13%2B-black">
  <img alt="Windows 10+" src="https://img.shields.io/badge/Windows-10%2B-0078d4">
  <img alt="Servers: Linux" src="https://img.shields.io/badge/servers-Linux-orange">
  <img alt="Models: Claude, OpenAI, OpenRouter" src="https://img.shields.io/badge/models-Claude%20%C2%B7%20OpenAI%20%C2%B7%20OpenRouter-e8a33d">
  <a href="https://buy.stripe.com/6oU5kC7kT96UcqTeznefC00"><img alt="Buy us a coffee" src="https://img.shields.io/badge/%E2%98%95%20Buy%20us%20a%20coffee-ffdd00"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#always-on-servers">Servers</a> ·
  <a href="#models-and-keys">Models</a> ·
  <a href="#what-asks-first">Safety</a> ·
  <a href="docs/HOW-IT-WORKS.md">How it works</a> ·
  <a href="SELF-HOSTING.md">Self-hosting</a>
</p>

---

HopBot is a desktop app for running a team of AI agents. Each agent has its own
name, face, instructions, memory, skills, folder and one long-running
conversation. They run commands, write files, browse, use your connected apps,
work on schedules and hand work to each other. Put them on your Mac, or on a
server of your own, where they keep going while your laptop is closed.

<p align="center">
  <img src="docs/assets/demo.gif" alt="Scout researching in Chromium on its own screen on a server, watched live from HopBot" width="760">
  <br><sub>Scout researching on its own screen, on a server, watched live from the app.</sub>
</p>

## Features

- **A crew, not a chatbot.** Make as many agents as you like, each with its own
  job, memory and folder. Ask one to message another, or hand off a background
  task.
- **A screen for every agent.** On a server, each agent gets its own desktop and
  browser. Watch any of them live, or take control and hand it back.
- **Always on.** Add any Linux server you can SSH into. HopBot installs itself
  there, and agents keep working through routines and webhooks while your Mac
  sleeps.
- **Any model.** Claude through Anthropic, GPT and o-series models through
  OpenAI, hundreds of models through OpenRouter, or free local models with Ollama
  or LM Studio. Pick per agent.
- **Asks only when it matters.** Everyday work just runs. On your own computer,
  risky actions wait for your OK; on a server, nothing asks.
- **Connected apps.** Sign in to 54 apps through MCP, from Gmail and Slack to
  Notion, Linear and Stripe.
- **Routines and webhooks.** Schedule work every few minutes, daily, weekly or
  once, or start it from any app with a webhook.
- **Files you can open.** PDFs, images and pages agents make arrive in the chat,
  open in the app, and stay in each agent's Library.
- **Memory that lasts.** Long conversations are summarized without losing the
  thread, and each agent keeps its own memory.
- **Talk to it.** Dictate messages on your Mac, or attach images and PDFs.

## Quick start

Download HopBot for macOS (Apple silicon or Intel) or Windows from the
[latest release](https://github.com/AyyazAli/hopbot/releases/latest). It updates
itself from there.

On Windows, agents on your PC run their commands in Git Bash: install
[Git for Windows](https://git-scm.com/download/win) too.

### From source

**Requirements:** [Node.js](https://nodejs.org) 22.19 or later; on a Mac, the
Xcode Command Line Tools (`xcode-select --install`).

```bash
git clone https://github.com/AyyazAli/hopbot.git
cd hopbot
npm install
npm start
```

Then:

1. Open **Settings → Default model**, choose a **Provider** and a **Model**, and
   paste that provider's API key.
2. Message the **HopBot** agent. Ask it to "create an agent called Scout that
   researches things for me", or press **+** in the sidebar.
3. For computer use on your Mac, grant HopBot (in development, **Electron**)
   **Accessibility** and **Screen Recording** in System Settings → Privacy &
   Security, then turn on **Computer use** under the message box.

## Always-on servers

Open the computer menu at the top of the sidebar → **Add a computer…** → **Install
on my server**. Enter the address and user, confirm the server's fingerprint, and
HopBot installs everything over SSH, with no ports to open. Check **Set up a
screen for computer use** to give each agent on it its own desktop.

Prefer the command line? Install with one script or with Docker, then pair it
with the app:

```bash
curl -fsSL https://raw.githubusercontent.com/AyyazAli/hopbot/main/server/install.sh | sh
```

[SELF-HOSTING.md](SELF-HOSTING.md) covers Docker, screens, keys and updates.

## Models and keys

| Provider | Models | API key |
|---|---|---|
| Anthropic | Claude (Opus, Sonnet, Haiku, Fable) | [console.anthropic.com](https://console.anthropic.com/settings/keys) |
| OpenAI | GPT and o-series models that can use tools | [platform.openai.com](https://platform.openai.com/api-keys) |
| OpenRouter | Hundreds of models from many companies, with one key | [openrouter.ai](https://openrouter.ai/settings/keys) |
| Local or custom server | Models on your own machine with [Ollama](https://ollama.com), [LM Studio](https://lmstudio.ai) or vLLM, or any OpenAI-compatible endpoint | Usually none; free to run |

Choose the default in Settings, or a different provider and model for each agent.
For a local server, pick **Local or custom server**, choose the Ollama or LM Studio
shortcut (or type any address), and pick one of its models. Give it room: at
least a 32k context and a model that supports tool calling.
Keys are stored encrypted with your Keychain on a Mac, and in a private file on a
server. `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` and `OPENROUTER_API_KEY` work too.

HopBot uses API keys, not your Claude or ChatGPT subscription. Computer use and
the built-in web search need a Claude model. Agents on other
models use everything else: the shell, files, memory, connected apps, routines
and teamwork.

## What asks first

| Action | On your computer | On a server |
|---|---|---|
| Shell commands | Only risky ones: installing software, `sudo`, deleting outside its folder, pushing code | Never |
| Files in its folder | Never | Never |
| Computer use | Only risky ones: quitting apps, deleting files, logging out | Never |
| Agents, skills, routines | Never | Never |
| Connected apps | Only changes, like sending or posting | Never |

Change any of these under **Settings → Ask before**.

## Privacy

- Conversations, memory and files stay on your computers: your Mac and the servers
  you add.
- HopBot talks only to the model provider you choose, the apps you connect, and
  your own servers. There's no HopBot account and no telemetry, and nothing is
  sent to HopBot's authors.
- The desktop app checks GitHub Releases for a newer version at launch and every
  six hours. Set `HOPBOT_NO_UPDATES=1` to turn that off.
- Server connections go through SSH with pinned host keys; hopbot-server listens
  on localhost only.

## Code signing policy

The macOS app is signed with innovage.io LLC's Developer ID certificate and
notarized by Apple.

Windows releases are to be signed through the SignPath Foundation program: free
code signing provided by [SignPath.io](https://signpath.io), certificate by
[SignPath Foundation](https://signpath.org). Until the project is approved,
Windows releases are unsigned.

Only installers built by the [Release workflow](.github/workflows/release.yml)
from this repository's source are signed, and every signing request is approved
by hand.

| Role | Members |
|---|---|
| Authors: change the source without further review | [AyyazAli](https://github.com/AyyazAli) |
| Reviewers: review contributions from others | [AyyazAli](https://github.com/AyyazAli) |
| Approvers: approve each signing request | [AyyazAli](https://github.com/AyyazAli) |

See [Privacy](#privacy) for what HopBot sends and where.

## Platforms

| | |
|---|---|
| Desktop app | macOS 13 or later (Apple silicon and Intel). Windows 10 or later (x64 and Arm), without computer use and dictation on the PC for now. |
| Phone app | Coming soon, for iPhone and Android |
| Servers | Linux on x86_64 or ARM64 (Ubuntu, Debian, Fedora and most others) |
| Screens on servers | 2 GB of memory or more, plus root or passwordless sudo to install packages |

## Documentation

- [How it works](docs/HOW-IT-WORKS.md): agents, tools, models, approvals, servers,
  screens, code layout and tests
- [Self-hosting](SELF-HOSTING.md): install script, Docker, screens and the
  `hopbot-server` command line
- [Releasing](docs/RELEASING.md): packaging, signing, notarization and updates

## Roadmap

- The phone app, for iPhone and Android
- Computer use and dictation on Windows
- A published server release for the install script
- Messages between agents on different computers
- Background tasks that survive a restart

## Support HopBot

HopBot is free and has no paid plan. If it saves you time, you can
[buy us a coffee](https://buy.stripe.com/6oU5kC7kT96UcqTeznefC00) to help keep it going.
Starring the repo and telling a friend help too.

<a href="https://buy.stripe.com/6oU5kC7kT96UcqTeznefC00"><img alt="Buy us a coffee" src="https://img.shields.io/badge/%E2%98%95%20Buy%20us%20a%20coffee-ffdd00?style=for-the-badge"></a>

## Contributing

Bug reports, fixes and ideas are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).
To report a security problem privately, see [SECURITY.md](SECURITY.md).

## License

HopBot is licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE)
for third-party software. The HopBot name and logo are trademarks and aren't
covered by the license; see [TRADEMARKS.md](TRADEMARKS.md).

HopBot is an independent project, not affiliated with or endorsed by Anthropic,
OpenAI or OpenRouter. Claude is a trademark of Anthropic.
