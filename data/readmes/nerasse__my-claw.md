# my-claw

Self-hosted AI agent orchestrator: one agent, real tools, your own machine.

<p>
  <a href="https://github.com/nerasse/my-claw/releases/latest"><img src="https://img.shields.io/github/v/release/nerasse/my-claw?style=flat-square" alt="Latest release"></a>
  <a href="https://github.com/nerasse/my-claw-app/releases/latest"><img src="https://img.shields.io/github/v/release/nerasse/my-claw-app?label=android&style=flat-square" alt="Android release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-3f4d3a?style=flat-square" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/runtime-Bun-f472b6?style=flat-square" alt="Runtime: Bun">
</p>

https://github.com/user-attachments/assets/6f21ec84-b772-471f-8abe-5f1170681f86

20 seconds, MP4, real speed, no montage: the prompt, the tools streaming, a reviewer spawned in the background, its `returned` card, the test run, then the browser panel.

## What it is

my-claw is a single-user agent that runs on a machine you own. You reach it from the web client or
the Android app, and it works with the shell, the files, a browser and sub-agents on that machine.
Every conversation is a log on disk, so a restart does not lose the thread.

The model is configuration: an OpenAI-compatible endpoint, a ChatGPT or Claude subscription,
Gemini, OpenRouter, or a local server. There is no hosted tier. Prompts go to the provider you
declare, and everything else stays on your hardware.

## What you get

- Shell, files, search, fetch, a real Chromium, cron jobs, skills, and sub-agents with their own
  sessions. A blacklist decides which tools ask for approval before they run.
- Workspaces: one agent, several codebases. Each keeps its own directory, prompt layers, skills and
  agents; the session list says which one a thread belongs to and filters down to it.
- One device list shared by the web client and the Android app: same threads, same memory, same
  queue.
- Providers and models declared in `config.json`, a model pin per agent, tags that carry several
  routes in order, and a switch from the chat header.
- Quota errors handled: the run parks, the app offers a retry, and a tag walks its routes until one
  answers.
- Sessions that survive restarts, with `/compact`, `/undo`, and continue after a stop.
- Remote nodes: pair another machine and its shell, files and search become tools of the same agent.
- Tool calls folded into one run in the transcript, reasoning folded under it, sub-agents reporting
  in place.
- Ten themes and a custom palette, with light, dark and AMOLED modes.
- Tags that name a route once: a model, its fallbacks, an effort and a context cap. Point a
  session, an agent or a job at the tag, then update the tag when a model changes and every caller
  follows. Retry-on-quota and Siphon both take a tag.

## Install

Linux x86_64, Debian or Ubuntu. The installer adds Bun, Chromium, ffmpeg and the systemd units; it
needs sudo once.

```bash
V=$(curl -fsSL https://api.github.com/repos/nerasse/my-claw/releases/latest | grep -m1 '"tag_name"' | cut -d'"' -f4 | sed 's/^v//')
curl -fsSLO "https://github.com/nerasse/my-claw/releases/download/v$V/my-claw-$V-linux-x64.tar.gz"
tar xzf "my-claw-$V-linux-x64.tar.gz"
sudo "my-claw-$V-linux-x64/packaging/install.sh"
```

The installer ends with a pairing code, a link and a QR code. Open the link: the client asks for the
first model, voice and services. The web client is served by the server itself.

Android app: [APK releases](https://github.com/nerasse/my-claw-app/releases/latest).

Updates come from GitHub releases every 15 minutes, or from `myclaw update`.

## Screenshots

![A conversation, with a Python file open on the right](docs/assets/readme/desktop.png)

![Two reviewers spawned as sub-agents, filed in a folder](docs/assets/readme/agents.png)

![The session list filtered by workspace, each row naming its own](docs/assets/readme/workspaces.png)

![The model picker, every provider](docs/assets/readme/models.png)

![Ten themes, light, dark and AMOLED](docs/assets/readme/themes.png)

![A conversation on a phone](docs/assets/readme/mobile.png)

The rest of the tour is in [docs/gallery.md](docs/gallery.md): a markdown file open beside the
chat, images in a carousel, tags and the session sheet, workspaces, the browser and its VNC
access, the status of a run, tools folded into steps, and voice notes.

## Documentation

The README is the product page; the details live in [the docs](https://nerasse.github.io/my-claw/), built from [`docs/`](docs/).

| If you want to | Read |
|---|---|
| install on a VPS or a VM, step by step | [docs/setup-guide.md](https://nerasse.github.io/my-claw/setup-guide/) |
| understand the code layout | [docs/architecture.md](https://nerasse.github.io/my-claw/architecture/) |
| declare providers, models and tags | [docs/config.md](https://nerasse.github.io/my-claw/config/), [docs/model-identity.md](https://nerasse.github.io/my-claw/model-identity/) |
| run sub-agents | [docs/subagents.md](https://nerasse.github.io/my-claw/subagents/) |
| add another machine as a node | [docs/remote-nodes.md](https://nerasse.github.io/my-claw/remote-nodes/) |
| resume a stopped run | [docs/continue.md](https://nerasse.github.io/my-claw/continue/) |
| build and release | [docs/ci-cd.md](https://nerasse.github.io/my-claw/ci-cd/) |

## Development

```bash
bun install
bun run check && bun test
bun run dev
```

Tests point `MY_CLAW_DIR` at a temporary directory, so a run never touches a real `~/.my-claw`.

## License

MIT. Copyright Yassir EL KSSIMI. Use it, change it, sell it, ship it closed; the copyright notice
travels with the copy.

Contributors: Yassir EL KSSIMI ([nerasse](https://github.com/nerasse)), Hicham Berrada
([Nawroski](https://github.com/Nawroski)), Nabil El Abassi
([LastryCoding](https://github.com/LastryCoding)), Anthony Von Bieler
([Tony224x](https://github.com/Tony224x)).
