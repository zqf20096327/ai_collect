<div align="center">

<img src="docs/assets/banner.svg" alt="OpenBot: free AI teammates with their own computers" width="100%">

<br>

<img src="public/img/icon-512.png" width="96" alt="OpenBot app icon">

# OpenBot

**AI teammates you can give real work to, for free.**<br>
Bots that use their own computer, learn your workflows, work in parallel, and come back with finished work.<br>
Plus a video brain that transcribes, understands and searches every video you own.

[![License: MIT](https://img.shields.io/badge/license-MIT-8b6cff?style=for-the-badge)](LICENSE)
[![Free forever](https://img.shields.io/badge/price-%240%20forever-43d17a?style=for-the-badge)](#-why-openbot)
[![Runs locally](https://img.shields.io/badge/runs-100%25%20local-111111?style=for-the-badge&logo=apple&logoColor=white)](#-quick-start)
[![Electron](https://img.shields.io/badge/desktop-Electron-47848f?style=for-the-badge&logo=electron&logoColor=white)](electron/main.cjs)
[![Ollama](https://img.shields.io/badge/models-Ollama%20%7C%20Groq%20%7C%20Gemini-f2a65a?style=for-the-badge)](#-free-model-options)
[![CI](https://img.shields.io/github/actions/workflow/status/satiricalguru/OpenBot/ci.yml?style=for-the-badge&label=CI)](.github/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/satiricalguru/OpenBot?style=for-the-badge&label=release&color=8b6cff)](https://github.com/satiricalguru/OpenBot/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/satiricalguru/OpenBot/total?style=for-the-badge&color=222)](https://github.com/satiricalguru/OpenBot/releases)

<a href="https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-mac-arm64.dmg"><img src="https://img.shields.io/badge/Download%20for%20macOS-ffffff?style=for-the-badge&logo=apple&logoColor=black" alt="Download for macOS" height="40"></a>&nbsp;
<a href="https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-windows-x64-setup.exe"><img src="https://img.shields.io/badge/Download%20for%20Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Download for Windows" height="40"></a>&nbsp;
<a href="https://openbot-zeta.vercel.app"><img src="https://img.shields.io/badge/Website-8b6cff?style=for-the-badge&logo=vercel&logoColor=white" alt="OpenBot website" height="40"></a>

[**Website**](https://openbot-zeta.vercel.app) · [**Quick start**](#-quick-start) · [**Features**](#-features) · [**Screenshots**](#-screenshots) · [**Demo video**](docs/assets/demo.mp4) · [**How it works**](#-how-it-works) · [**Contributing**](CONTRIBUTING.md)

<br>

<img src="docs/assets/demo.gif" alt="OpenBot walkthrough: chats, the bot's computer, crew chat, light mode and video search" width="92%">

<sub>▶ A real, unedited capture of the desktop app running on a laptop with a local model. <a href="docs/assets/demo.mp4">Watch the MP4</a></sub>

<br><br>

<a href="https://openbot-zeta.vercel.app"><img src="docs/assets/website.gif" alt="The OpenBot website: Nova follows the cursor, then splits into a line-art exploded view of its parts as you scroll" width="92%"></a>

<sub>🌐 <a href="https://openbot-zeta.vercel.app"><b>openbot-zeta.vercel.app</b></a>: the download site, with a Three.js hero and a scroll-driven exploded view of a bot. <a href="docs/assets/website.mp4">MP4</a></sub>

</div>

> [!NOTE]
> **New in 0.3.0:** bots drive a real browser you can watch live, you can text them from Telegram or Slack, there are native installers for **Windows** and Linux, and team mode adds sign-in. [Release notes →](https://github.com/satiricalguru/OpenBot/releases/tag/v0.3.0)

---

## ✨ Why OpenBot?

Always-on AI teammates arrived in 2026, but they sit behind expensive plans. OpenBot gives you the same idea **for $0**, on your own machine, with your own data.

| | **OpenBot** | Grok Bot (xAI) | dots (OpenAI) | muse.ai |
|---|:---:|:---:|:---:|:---:|
| Price | **Free, MIT** | SuperGrok Heavy / Cursor Ultra | ChatGPT Pro / Business Premium | Paid plans |
| Runs fully local & private | ✅ | ❌ | ❌ | ❌ |
| Bots with their own computer | ✅ sandboxed workspace | ✅ | ✅ | — |
| Group chats where bots hand off work | ✅ | ✅ | — | — |
| Learn a workflow once, repeat it (skills) | ✅ | ✅ | ✅ | — |
| Scheduled routines & proactive mode | ✅ | ✅ | ✅ | — |
| Allow / Ask / Block rules + approvals | ✅ | ✅ | ✅ | — |
| AI video search (speech + visuals) | ✅ | — | — | ✅ |
| Transcripts, chapters, clips, embeds | ✅ | — | — | ✅ |
| Bring any model (Ollama, Groq, Gemini…) | ✅ | ❌ | ❌ | — |

---

## 🚀 Quick start

**Option A: download the app.**

Current version: **v0.3.0** (Nov 15, 2026). Every link below always points to the latest release.

| Platform | Download | Size | First launch |
|---|---|---|---|
| **macOS** (Apple silicon) | [OpenBot-mac-arm64.dmg](https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-mac-arm64.dmg) · [.zip](https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-mac-arm64.zip) | ~228 MB | Not notarized yet: **System Settings → Privacy & Security → Open Anyway** |
| **Windows** 10/11 (x64) | [OpenBot-windows-x64-setup.exe](https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-windows-x64-setup.exe) | ~219 MB | Unsigned: SmartScreen → **More info → Run anyway** |
| **Linux** (x86_64) | [AppImage](https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-linux-x86_64.AppImage) · [.deb](https://github.com/satiricalguru/OpenBot/releases/latest/download/OpenBot-linux-amd64.deb) | ~448 / 361 MB | `chmod +x` the AppImage |

You'll still need `ffmpeg` and a free model: `brew install ffmpeg ollama` (macOS) or `winget install Gyan.FFmpeg Ollama.Ollama` (Windows), then `ollama pull qwen3:8b`.

**Option B: run from source** (macOS, Linux or Windows):

```bash
# 1. Install the free tools (macOS shown; Linux/Windows work too)
brew install node ffmpeg ollama
ollama pull qwen3:8b            # any tool-capable model works

# 2. Get OpenBot
git clone https://github.com/satiricalguru/OpenBot.git
cd OpenBot && npm install

# 3. Launch the desktop app
npm run app
```

> [!TIP]
> Prefer the browser? Run `npm start` and open **http://localhost:4321**.
> Build installers yourself with `npm run dist:mac`, `npm run dist:win` or `npm run dist:linux` (output in `dist/`). Pushing a `v*` tag builds all three on GitHub Actions and attaches them to a release.

The first video you add downloads the open Whisper and CLIP models (~250 MB) once. After that everything runs offline.

---

## 🧩 Features

<table>
<tr>
<td width="50%" valign="top">

### 🤖 Bots with personality
Create teammates and design how they look: **shape, eyes, mouth, accessory, gaze and colors**. They're alive, too: they blink and glance around when idle, bob and scan while working, hop with a red badge when they need you, and bounce when they talk.

</td>
<td width="50%" align="center">
<img src="docs/assets/bots.gif" width="300" alt="Animated bot customizer">
</td>
</tr>
<tr>
<td valign="top">

### 💻 Their own computer
Every bot has a private, sandboxed workspace with a **terminal, browser and files**. Open the **Computer** panel to watch what it's doing live, browse the files it made, and read its activity log.

**New:** a **real browser** (Playwright driving your Chrome/Edge) that bots can click and type in, streamed live into the Computer panel.

On macOS, commands run in a Seatbelt sandbox that can only write inside the bot's workspace.

</td>
<td valign="top">

### 👥 Crews that collaborate
Put several bots in a group chat. Mention `@Scout` or `@all`. The lead picks up the work and **hands off** to teammates (`message_agent`) or assigns **background tasks** (`assign_task`). You only get pulled in for judgment calls.

</td>
</tr>
<tr>
<td valign="top">

### 🛡️ You stay in control
For every tool you choose **Allow**, **Ask** or **Block**. "Ask" pauses the bot and shows an approval card: *Allow once*, *Always allow* or *Deny*. Passwords, `sudo`, the keychain and destructive commands are always blocked.

</td>
<td valign="top">

### 🧠 Memory, skills & routines
Bots **remember** your preferences, **learn skills** (walk through a task once, then click *Save chat as a skill*), and run **routines** on a schedule ("every weekday at 9, brief me on…"). **Proactive mode** does read-only research while you're away.

</td>
</tr>
<tr>
<td valign="top">

### 🎬 A video brain
Upload videos or audio and OpenBot will:
- **Transcribe** speech locally with Whisper (editable, with VTT/SRT export)
- **See** every scene with CLIP, so you can search *"whiteboard"* or *"red car"*
- Write **summaries, tags and chapters**
- Answer questions with **clickable timestamps**
- Make **clips**, share links and an **embeddable player**, with private analytics

</td>
<td valign="top">

### 🎙️ And more
- **Voice calls** with any bot, using free in-browser speech
- **Dark mode by default**, with Light and System themes
- **Telegram & Slack bridges**: text your bots from your phone
- **Team mode**: accounts with admin/member roles and sign-in
- **Menu-bar app**: close the window and your bots keep working
- **Search everything** with ⌘K, create a new bot with ⌘N
- **No build step**: plain ES modules and SQLite (`node:sqlite`)

</td>
</tr>
</table>

---

## 📸 Screenshots

<div align="center">

**Chat with a bot and watch its computer**
<img src="docs/assets/chat-computer-dark.png" alt="Chat with Scout and its Computer panel (dark)" width="92%">

<br><br>

**Crew chat, dark and light**

<table>
<tr>
<td><img src="docs/assets/crew-dark.png" alt="Crew group chat in dark mode"></td>
<td><img src="docs/assets/crew-light.png" alt="Crew group chat in light mode"></td>
</tr>
</table>

**Search inside videos by what's said and what's seen**
<img src="docs/assets/video-dark.png" alt="Video page with multimodal search for 'budget'" width="92%">

<details>
<summary><b>More screenshots</b></summary>
<br>

| Overview | Bot studio |
|---|---|
| <img src="docs/assets/home-dark.png" alt="Overview"> | <img src="docs/assets/studio-dark.png" alt="Bot customizer"> |
| **Video bot answering with timestamps** | **Light mode** |
| <img src="docs/assets/reel-dark.png" alt="Reel answering about a video"> | <img src="docs/assets/chat-computer-light.png" alt="Light mode"> |
| **Video library** | |
| <img src="docs/assets/library-dark.png" alt="Video library"> | |

</details>

</div>

---

## 🆓 Free model options

Pick one in **Settings → Brain**. You can switch any time, or give each bot its own model.

| Provider | Cost | Good for |
|---|---|---|
| **Ollama** (default) | Free, local | Private, offline. Try `qwen3:8b`, `llama3.1`, `gemma4`, `gpt-oss` |
| **LM Studio** | Free, local | Any OpenAI-compatible local server |
| **Groq** | Free tier | Very fast Llama models |
| **OpenRouter** | `:free` models | Lots of open models |
| **Google Gemini** | Free tier | OpenAI-compatible endpoint |

---

## 🔧 How it works

```mermaid
flowchart LR
  subgraph App["🖥️ OpenBot desktop app (Electron)"]
    UI["Messenger UI<br/>animated bots · Computer panel"]
  end
  UI <-- "REST + live events (SSE)" --> S["Local server<br/>Node + SQLite"]
  S --> R["Agent runtime<br/>tools · rules · approvals"]
  R --> T1["🌐 Web search & browse"]
  R --> T2["⌨️ Sandboxed terminal & files"]
  R --> T3["🧠 Memory · skills · routines"]
  R --> T4["🤝 Handoffs & background tasks"]
  R --> L["🦙 Free LLM<br/>Ollama · Groq · Gemini"]
  S --> V["Video pipeline<br/>ffmpeg"]
  V --> W["🗣️ Whisper<br/>speech → text"]
  V --> C["👁️ CLIP<br/>frames → vectors"]
  V --> E["🔎 MiniLM<br/>semantic search"]
```

<details>
<summary><b>Project structure</b></summary>

```
electron/          desktop shell: window, menu-bar icon, theme sync
server/
  agents/          agent loop (runtime.js), tools + rules (tools.js), real browser (browser.js), scheduler
  auth.js          team mode: accounts, sessions, roles
  bridges.js       Telegram + Slack bridges
  video/           ffmpeg pipeline, Whisper/CLIP/MiniLM models, search & Q&A
  llm.js           Ollama + OpenAI-compatible providers
  index.js         REST API + live events
public/
  js/bot.js        procedural animated bot characters
  js/chat.js       messenger-style chat view
  js/icons.js      icon set
  app.css          design system (dark default + light)
scripts/
  capture.cjs      regenerates README screenshots/GIFs/video
site/              landing page (Three.js), deployed to Vercel (openbot-zeta.vercel.app) and GitHub Pages
docs/assets/       README media
```

</details>

<details>
<summary><b>Configuration</b></summary>

| Env var | Default | |
|---|---|---|
| `PORT` | `4321` | Server port |
| `OPENBOT_HOST` | `127.0.0.1` | Set `0.0.0.0` to share on your network (add auth first!) |
| `OPENBOT_DATA` | `./data` (dev) · `~/Library/Application Support/OpenBot/data` (app) | Database, videos, workspaces, models |
| `OPENBOT_AUTH` | off | `1` requires sign-in (team mode). Always on when `OPENBOT_HOST` isn't local |
| `OPENBOT_BROWSER` | auto-detect | Path to a Chromium-based browser for real browser control |
| `OPENBOT_BROWSER_HEADFUL` | off | `1` shows the bot's browser window instead of running headless |

</details>

<details>
<summary><b>Agent tools</b></summary>

| Tool | Default rule | What it does |
|---|---|---|
| `web_search`, `browse` | Allow | Search DuckDuckGo, read pages |
| `browser_open`, `browser_read`, `browser_screenshot` | Allow | Drive a real Chrome/Edge, live view in the Computer panel |
| `browser_click`, `browser_type` | **Ask** | Click and type on pages (password fields always refused) |
| `read_file`, `list_files`, `write_file` | Allow | Work inside the bot's own workspace |
| `run_command` | **Ask** | Shell, sandboxed to the workspace |
| `http_request` | **Ask** | Call APIs and webhooks |
| `delete_file`, `schedule_routine` | **Ask** | Side effects need your OK |
| `remember`, `recall`, `save_skill` | Allow | Long-term memory and skills |
| `search_videos`, `ask_video`, `list_videos` | Allow | Use the video library |
| `message_agent`, `assign_task` | Allow | Collaborate with teammates |
| `notify_user` | Allow | Ping you when done |

</details>

---

## 🔒 Privacy & safety

- Everything (chats, files, videos, embeddings) stays in a local SQLite database and folder.
- The server listens on `127.0.0.1` only, with no telemetry and no accounts.
- Risky actions default to **Ask**. See [SECURITY.md](SECURITY.md).

> [!WARNING]
> Team mode adds sign-in, but OpenBot doesn't terminate TLS. Before exposing it beyond your network, put HTTPS in front of it (for example Cloudflare Access, Tailscale or a reverse proxy).

---

## 📱 Bridges: text your bots

Open **Settings → Bridges**.

- **Telegram**: create a bot with [@BotFather](https://t.me/BotFather) and paste its token. Message your bot once; it replies with your chat ID, which you add to *Allowed chat IDs*. Only those chats can talk to your bots.
- **Slack**: create an app, enable **Socket Mode** (app-level token with `connections:write`), add the bot scopes `chat:write`, `im:history` and `app_mentions:read`, and subscribe to `message.im` and `app_mention`. Paste both tokens. Then DM the bot or @mention it.

Both use outbound connections only, so you don't need a public URL. Anyone in your Slack workspace who can DM the app can talk to your bot, so keep risky tools on **Ask**. Conversations also show up in the bot's chat in the app, and approvals still happen there.

## 👥 Team mode

**Settings → Team → Set up team** creates the first admin account and turns on sign-in. Admins can add people as members or admins. Everyone shares the same crew, chats and videos; only admins can change settings, bridges and the team. Passwords are hashed with scrypt, sessions are HttpOnly cookies, and failed logins are rate-limited. Running with `OPENBOT_HOST=0.0.0.0` turns sign-in on automatically, and in that case the first admin can only be created from the machine itself.

---

## 🗺️ Roadmap

- [x] Real browser control for bots (Playwright) with a live screen view
- [x] Slack / Telegram bridges so you can text your bots
- [x] Windows & Linux installers
- [ ] Signed macOS build: the release pipeline is ready and signs and notarizes as soon as an Apple Developer ID certificate is added as a repo secret (see [release.yml](.github/workflows/release.yml))
- [x] Multi-user mode with auth (shared team workspace)
- [ ] Per-user private bots and chats in team mode
- [ ] Intel Mac and Windows on ARM builds

Ideas and PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

<div align="center">

**If OpenBot is useful to you, a ⭐ helps others find it.**

<sub>MIT licensed · Built with Node, Electron, SQLite, ffmpeg, transformers.js, Whisper, CLIP and your favorite open model.<br>
OpenBot is an independent project and is not affiliated with xAI, OpenAI or muse.ai.</sub>

</div>
