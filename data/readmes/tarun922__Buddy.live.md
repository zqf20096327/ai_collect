<div align="center">

<img src="docs/buddy-512.png" width="120" alt="Buddy logo" />

# Buddy

### The floating AI coding companion that works in a safe copy of your project.
**Free-model friendly · Your keys, your machine · Review before anything touches your repo**

[![Release](https://img.shields.io/github/v/release/tarun922/Buddy.live?style=for-the-badge&color=8b5cf6&include_prereleases)](https://github.com/tarun922/Buddy.live/releases)
[![Downloads](https://img.shields.io/github/downloads/tarun922/Buddy.live/total?style=for-the-badge&logo=github&color=22c55e&label=downloads)](https://github.com/tarun922/Buddy.live/releases)
[![Stars](https://img.shields.io/github/stars/tarun922/Buddy.live?style=for-the-badge&logo=github&color=fbbf24)](https://github.com/tarun922/Buddy.live/stargazers)
[![Forks](https://img.shields.io/github/forks/tarun922/Buddy.live?style=for-the-badge&logo=github&color=34d399)](https://github.com/tarun922/Buddy.live/network/members)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

[![Issues](https://img.shields.io/github/issues/tarun922/Buddy.live?style=flat-square)](https://github.com/tarun922/Buddy.live/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/tarun922/Buddy.live?style=flat-square)](https://github.com/tarun922/Buddy.live/pulls)
[![Last commit](https://img.shields.io/github/last-commit/tarun922/Buddy.live?style=flat-square)](https://github.com/tarun922/Buddy.live/commits)
[![Contributors](https://img.shields.io/github/contributors/tarun922/Buddy.live?style=flat-square)](https://github.com/tarun922/Buddy.live/graphs/contributors)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
![Electron](https://img.shields.io/badge/Electron-33-47848F?style=flat-square&logo=electron&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-ESM-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Platforms](https://img.shields.io/badge/Windows%20·%20macOS%20·%20Linux-lightgrey?style=flat-square)

**[Download](#-download) · [Features](#-features) · [Quick start](#-quick-start) · [Linux](#-linux--hyprland-notes) · [Free models](#-bring-your-own-model-free-ones-welcome) · [Safety](#-safety-first) · [Plugins](#-buddysap-plugins) · [Docs](#-documentation) · [Contributing](#-contributing) · [Roadmap](#-roadmap)**

⭐ **If Buddy saves you time, a star helps other developers find it.** ⭐

</div>

<div align="center">

<video src="https://github.com/tarun922/Buddy.live/raw/main/assets/teaser-hq.mp4" width="720" controls muted loop autoplay playsinline></video>

<br/>

<video src="https://github.com/tarun922/Buddy.live/raw/main/assets/demo2-hq.mp4" width="720" controls muted playsinline></video>

<video src="https://github.com/tarun922/Buddy.live/raw/main/assets/demo3-hq.mp4" width="720" controls muted playsinline></video>

<sub>Video not playing? [Teaser](assets/teaser-hq.mp4) · [Demo 1](assets/demo2-hq.mp4) · [Demo 2](assets/demo3-hq.mp4)</sub>

</div>


<div align="center">

## 🎉 Buddy is **open source** — the full code is here, today.

**Early-released ahead of schedule. Thank you for the support!** If it helps you, [⭐ star the repo](https://github.com/tarun922/Buddy.live) so others can find it.

</div>

---

## 👋 What is Buddy?

Buddy is a small bubble that floats in the corner of your screen. Press a hotkey, point it at a project folder, and **chat, ask questions about your code, or let it do the work** — plan, edit, run tests, commit — all using **your own API keys** (free tiers included) and a personality you design yourself.

The big idea: **Buddy never edits your project directly.** It works in a private clone on its own `buddy` branch. You look at what it did, pick the files you like, and bring them into your repo with one click. Don't like it? Nothing of yours was touched.

> **Built for people who can't or don't want to pay for AI.** Buddy's routing, memory and micro agents are designed to get good results out of free models — and it still works great with Claude, GPT and Gemini if you have them.

---

## 🎯 Next milestone

| Stars | Unlocks |
|:--|:--|
| ⭐ **1,000** | Signed installers for Windows, macOS and Linux |
| ⭐ **2,500** | Plugin marketplace + more wake-word languages (Hindi / Hinglish) |
| ⭐ **5,000** | Buddy Mobile companion *(experiment)* |

Watch 👁️ the repo (**Watch → Releases**) to get pinged for every release.

---

## ✨ Features

### 🧠 Works the way you think
| | |
|---|---|
| **Five modes** | **Chat**, **Ask** (read-only), **Agent** (full tools), **Architect** (plan first, then build), **Study** (a tutor that plans, teaches and quizzes). One shared memory across all of them. |
| **Small talk stays small** | A bare "hi" gets a one-line reply — never a plan, never code. A hard gate in front of every mode, not a polite request to the model. |
| **Understands "yes"** | Say *yes / haan / kar do* in plain words and Buddy switches to Agent mode and does the offered job. Say *no* and it stops asking. |
| **Asks when it matters** | The `ask_user` tool lets the AI ask you a multiple-choice question mid-task instead of guessing. |

### 🛡️ Your repo stays yours
- **Isolated workspace** — Buddy works in a clone on the `buddy` branch.
- **Review & Apply** — see every changed file, pick what you want, merge. Files *you* edited meanwhile are never overwritten.
- **Timeline / Undo** — go back to any save point, one click.
- **Crash-safe** — atomic writes plus a run journal. Power cut mid-task? Resume or discard with one click, project intact.

### 🤖 Micro agents (small helpers around the main model)
| Agent | Job |
|---|---|
| 🔭 **Scout** | Picks the right skills and tools from a big library for *this* task, before the main model starts. |
| 🧭 **Pathfinder** | Pinpoints the exact files, functions and line ranges in a large or unfamiliar codebase. |
| 🧠 **Memory keeper** | Folds long chats into summaries and learns durable facts about you and the project. |
| ✍️ **Committer** | Writes clean commit messages. |
| 🔎 **Reviewer** | Reads the diff after a run and reports only real problems. |

Each can run on its **own model and key** — put a tiny fast model on Scout and keep the big one for the real work.

### 🔌 Models: free first, premium welcome
OpenRouter · NVIDIA NIM · Mistral · Gemini · Cerebras · Ollama (local) · **Claude (Anthropic)** · **OpenAI** · **Kaggle / Colab cloud model** · plugin providers.
Key rotation and automatic fallback when a free tier runs out.

### 🎙️ Voice & computer control *(opt-in)*
- **🎤 Mic button** and hands-free **"Ok Buddy"** with an **offline wake word** — nothing is sent anywhere until you say it.
- Speech-to-text through Groq's free tier (add as many keys as you like — they take turns) or OpenAI.
- Say *"open YouTube and search what is React"* and Buddy does it on your real computer — **only after you type your Buddy password**, which the AI never sees. [Details ↓](#-safety-first)

### 🖥️ A terminal that behaves
Live, visible, **isolated** — installs go into Buddy's own folder, never your system. `pnpm`-first with automatic npm/yarn translation. Dangerous commands need a click; catastrophic ones are blocked. Stop any command any time.

### 🧩 And more
- **Memory that learns** — TF-IDF recall per message, durable facts, `/memory`, `/unlearn`.
- **Outline-first editing** — the agent reads a symbol, not a whole file (`read_symbol`, `replace_symbol`, `patch_file`) so edits on big files hit real code.
- **Skills library** — thousands of `SKILL.md` playbooks matched automatically.
- **Past chats & notes** — restore any conversation; `/remember` things once.
- **Personality Builder** — name, tone, language, sliders; export and share your Buddy.
- **9 themes** — Midnight, OLED, Daylight, Paper, Auto… plus accent, blur, radius, spacing.
- **[BuddySAP plugins](#-buddysap-plugins)** — Gmail, scheduling, your own.

---

## ⬇️ Download

[![Total downloads](https://img.shields.io/github/downloads/tarun922/Buddy.live/total?style=for-the-badge&logo=github&color=22c55e&label=total%20downloads)](https://github.com/tarun922/Buddy.live/releases)
[![Latest release downloads](https://img.shields.io/github/downloads/tarun922/Buddy.live/latest/total?style=for-the-badge&color=8b5cf6&label=latest%20release)](https://github.com/tarun922/Buddy.live/releases/latest)

**Grab the installer for your system from the [latest release →](https://github.com/tarun922/Buddy.live/releases/latest)**

| System | Download | Notes |
|:--|:--|:--|
| 🪟 **Windows** | `Buddy-…-win-x64.exe` (installer) · portable `.exe` | Unsigned for now: if SmartScreen warns, click **More info → Run anyway** |
| 🍎 **macOS** (Apple Silicon & Intel) | `Buddy-…-mac-arm64.dmg` · `Buddy-…-mac-x64.dmg` | Unsigned: first launch **right-click → Open** |
| 🐧 **Linux · any distro** | `Buddy-…-linux-x86_64.AppImage` | `chmod +x Buddy-*.AppImage && ./Buddy-*.AppImage` |
| 🐧 **Debian · Ubuntu · Mint** | `Buddy-…-linux-amd64.deb` | `sudo apt install ./Buddy-*.deb` |
| 🐧 **Fedora · RHEL · openSUSE** | `Buddy-…-linux-x86_64.rpm` | `sudo dnf install ./Buddy-*.rpm` |
| 🐧 **Arch · Manjaro · EndeavourOS** | `Buddy-…-linux-x64.pacman` | `sudo pacman -U Buddy-*.pacman` |
| 📦 **Any Linux** | `Buddy-…-linux-x64.tar.gz` | Extract and run `./buddy` |

Each release also ships `SHA256SUMS.txt`:
```bash
sha256sum -c SHA256SUMS.txt --ignore-missing
```

> Prefer building from source? See [Quick start](#-quick-start).

---

## 🚀 Quick start

**Requirements:** Node.js 20+ (22 recommended) and Git. Works on Windows, macOS and Linux.

```bash
git clone https://github.com/tarun922/Buddy.live.git
cd Buddy.live
npm install            # or: pnpm install
npm run setup:skills   # optional: clones the skills library into future-skills/
npm run dev            # Vite + Electron with hot reload
# or
npm start              # build the UI, then run Electron
```

1. Click the bubble (or press **`Ctrl/Cmd + Shift + Space`**). **Drag** the bubble anywhere you like — it remembers its spot.
2. **Choose folder** — the project Buddy should work on.
3. **Settings → Models** — paste one API key. A free one is enough to start.
4. Type what you want. Press **`Esc`** to tuck Buddy away.

> **First time with no key?** Get a free one from [OpenRouter](https://openrouter.ai), [Mistral](https://console.mistral.ai), [Gemini](https://aistudio.google.com) or [Cerebras](https://cloud.cerebras.ai) — or run [Ollama](https://ollama.com) locally with no key at all.

<details>
<summary><b>Useful commands</b></summary>

| Command | What it does |
|---|---|
| `/agent <task>` · `/chat` · `/ask` · `/architect` · `/study` | Switch mode (or run a task directly) |
| `/apply` | Review & bring Buddy's work into your repo |
| `/undo` · `/diff` · `/commit` | Save points and changes |
| `/remember <text>` · `/notes` · `/forget` | Things Buddy keeps in mind |
| `/memory` · `/unlearn` | What Buddy learned on its own |
| `/index` · `/find` · `/tree` · `/map` | Explore the project |
| `/help` | Everything else |

</details>

---

## 🐧 Linux / Hyprland notes

Buddy is a frameless, transparent, always-on-top window — tiling compositors need a hint.

```bash
# if the window is blank or only a small box shows
npm run build && npx electron . --ozone-platform=x11       # XWayland: dragging + positioning work
npx electron . --ozone-platform-hint=auto --no-sandbox      # native Wayland, if the sandbox complains
```

Hyprland rules (find the class with `hyprctl clients`):

```ini
windowrule = float on, match:class ^(Buddy|electron)$
windowrule = pin on,   match:class ^(Buddy|electron)$
# older Hyprland:
# windowrulev2 = float, class:^(Buddy|electron)$
# windowrulev2 = pin,   class:^(Buddy|electron)$
```

<details>
<summary><b>Electron binary won't download (slow / blocked network)?</b></summary>

```bash
npm install --ignore-scripts
V=33.4.11   # the Electron 33 patch release you want
mkdir -p node_modules/electron/dist
curl -L -o /tmp/electron.zip "https://github.com/electron/electron/releases/download/v$V/electron-v$V-linux-x64.zip"
unzip -o /tmp/electron.zip -d node_modules/electron/dist
printf 'electron' > node_modules/electron/path.txt
chmod +x node_modules/electron/dist/electron
```
With **pnpm**, run `pnpm approve-builds` and allow `electron` if the download is skipped.
</details>

Using **fish**? `nvm` is bash-only — use [`fnm`](https://github.com/Schniz/fnm) or `nvm.fish`.

---

## 🆓 Bring your own model (free ones welcome)

| Option | Cost | Best for |
|---|---|---|
| OpenRouter / Mistral / Gemini / Cerebras / NIM free tiers | Free | Getting started fast |
| **Ollama** | Free, runs on your PC | Total privacy, offline |
| **Kaggle notebook** *(recommended cloud option)* | Free GPU | A big open model without your own GPU — private by default, wiped when the session ends |
| Colab notebook | Free GPU | Works too, but tied to your Google account |
| Claude · OpenAI | Paid | Hardest tasks |

**Cloud model in 3 steps:** open `buddy/buddy.ipynb` on Kaggle → run all cells → paste the *connect code* it prints into **Settings → Cloud model**.

---

## 🔒 Safety first

Buddy is designed so that **nothing surprising can happen to your computer or your code**.

- **Your project is never edited directly** — a private clone + explicit Apply.
- **Terminal is isolated** — global installs stay in Buddy's folder; `sudo` and system installs are refused.
- **Dangerous commands ask first**; catastrophic ones are blocked.
- **Keys are encrypted at rest** (OS keychain when available) and never shown back in the UI.
- **Computer control is off by default** and sits behind a **Buddy password**:
  - Typed only in a private dialog — never in chat, never visible to the AI or to a web page.
  - Stored as a salted `scrypt` hash. 5 wrong tries → growing lock-outs.
  - Every action shows *exactly* what will happen first.
  - Only three actions: **search**, **open URL**, **open app**. No shell, no typing into other programs, no file access.
  - Local/private addresses, `file:` / `javascript:` URLs and system tools (`cmd`, `powershell`, `terminal`, `sudo` …) are refused.
  - Every action is logged. Max 10 per minute.
- **Voice is opt-in**: the wake word runs **offline on your machine**; audio is never stored.
- **Plugins start disabled** and must be approved permission by permission.

Found a vulnerability? Please read [SECURITY.md](SECURITY.md) and report it privately.

---

## 🧩 BuddySAP plugins

Drop a plugin folder into `buddysap/plugins/` and it appears in the 🧩 tab. Plugins can add **tools, AI providers, panels, themes and custom screens** through a real SDK — and every one is **off until you approve what it may do**. See [`buddysap/README.md`](buddysap/README.md).

---

## 📚 Documentation

| Guide | What's inside |
|---|---|
| [Full guide](docs/GUIDE.md) | Every feature in depth: modes, workspace & Apply, Timeline, micro agents, Pathfinder, memory, study mode, terminal, cloud model, voice & wake word, computer control per OS, skills library |
| [CONFIGURATION.md](CONFIGURATION.md) | All config options |
| [buddysap/README.md](buddysap/README.md) | Writing plugins |
| [SECURITY.md](SECURITY.md) | Threat model & reporting |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Dev setup, tests, PR checklist |

---

## 🏗️ How it's built

```
electron/    main process, preload (strict channel allow-list), IPC api
src/         React + Vite UI (bubble, chat, work card, terminal, settings…)
core/        the agent: session, tools, memory, micro agents, workspace, vault, voice
providers/   model adapters + router (rotation, fallback, error mapping)
toolhub/     skills & tools library with BM25 search
buddysap/    plugin host + SDK
buddy/       Kaggle / Colab notebook for the cloud model
test/        20+ test suites  →  npm test
```

Electron + React (Vite). The agent core is plain Node ESM running in the main process. The renderer has **no Node access** — everything goes through an explicit allow-list of IPC channels.

```bash
npm test          # full suite
npm run test:desktop   # computer-control safety rules
npm run test:wake      # wake word + model download
```

---

## 🗺️ Roadmap

- [ ] Signed installers for Windows / macOS / Linux
- [ ] More wake-word languages (Hindi / Hinglish)
- [ ] Plugin marketplace
- [ ] Inline diff review inside the chat
- [ ] Per-project model profiles
- [ ] More micro agents (tests, docs)

Vote with 👍 on issues or open a [discussion](https://github.com/tarun922/Buddy.live/discussions) — the roadmap follows the community.

---

## 🤝 Contributing

Contributions of every size are welcome — bug reports, docs, plugins, themes, translations, code.

1. ⭐ **Star** the repo (it genuinely helps).
2. **Fork** → create a branch → make your change → `npm test`.
3. Open a **pull request** describing what and why.

Look for [`good first issue`](https://github.com/tarun922/Buddy.live/labels/good%20first%20issue) and [`help wanted`](https://github.com/tarun922/Buddy.live/labels/help%20wanted). Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

<a href="https://github.com/tarun922/Buddy.live/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tarun922/Buddy.live" alt="Contributors" />
</a>

---

## ⭐ Star history

<a href="https://star-history.com/#tarun922/Buddy.live&Date">
  <img src="https://api.star-history.com/svg?repos=tarun922/Buddy.live&type=Date" alt="Star History Chart" width="600" />
</a>

---

## ❓ FAQ

<details><summary><b>Does Buddy send my code anywhere?</b></summary>
Only to the model provider <i>you</i> choose, with <i>your</i> key. Use Ollama or the Kaggle cloud model if you want it to stay off third-party providers.
</details>

<details><summary><b>Can it break my project?</b></summary>
It works in a private clone on its own branch. Nothing reaches your repo until you review and apply it, and you can undo from the Timeline.
</details>

<details><summary><b>Do I need a paid model?</b></summary>
No. Buddy is built to work well with free tiers, local Ollama, and a free Kaggle GPU.
</details>

<details><summary><b>Is the "Ok Buddy" wake word always listening to the cloud?</b></summary>
No. It's off by default; when on, a small offline model on your computer listens for the phrase. Only the command you speak <i>after</i> it is sent for transcription.
</details>

<details><summary><b>Why does it ask for a password to open an app?</b></summary>
Anything that touches your real computer is gated by your own Buddy password so a webpage, a file or a mis-heard word can never trigger it.
</details>

---

## 📄 License

[MIT](LICENSE) © 2026 Buddy contributors.

<div align="center">

**Made with 💜 for developers who want an AI helper that respects their code, their machine and their budget.**

⭐ **Star** · 🍴 **Fork** · 🐛 **Report a bug** · 💡 **Request a feature**

</div>
