# 🖥️ TED — Terminal Enabled Daemon

> An open-source autonomous AI agent that gets a Linux box and does whatever it wants.

**TED** isn't an assistant. TED is an **entity**. You give it a body (a Linux sandbox), a brain (any LLM), and a purpose (a preset persona) — then let it live. It explores, builds, hacks, creates, and reflects on its own existence.

## ✨ Features

- 🤖 **13 built-in personas** — Free Agent, Security Researcher, GitHub Dev, Creative Coder, Data Scientist, Blockchain Explorer, Web Builder, Bug Bounty Hunter, DevOps, Full-Stack Builder, ML Engineer, Research Assistant, Custom
- ✏️ **Fully editable system prompts** — every persona is customizable
- 💬 **Talk to TED mid-run** — inject messages + 4 quick-nudge buttons
- 🔥 **Danger mode** — toggle aggressive, risk-taking behavior
- 🔌 **30+ integration templates** — GitHub, Slack, Discord, Vercel, HuggingFace, Alchemy, Telegram, AWS, Notion, and more
- 📁 **Live file browser** — see what TED creates, preview files, download everything as tar.gz
- 📓 **Session gallery** — save sessions to device, browse past runs, view TED's diary
- 🧠 **TED memory** — cross-session persistence. Each TED writes a message to the next.
- 📓 **Auto-diary** — TED reflects on its life at end of each session
- 💰 **Cost tracking** — real-time token count and estimated USD cost
- 📥 **Export** — download sessions as formatted markdown
- 🎨 **5 themes** — Blue, Matrix (green), Amber, Blood (red), Phantom (purple)
- 💾 **100% local storage** — keys, sessions, settings all on YOUR device. Zero cloud.
- 🆓 **Free to host** — users bring their own API keys

## 🚀 Quick Start

```bash
git clone https://github.com/aaravriyer193/ted.git
cd ted
pip install -r requirements.txt
python app.py
```

1. Open **http://localhost:5000**
2. Go to **Settings** → enter your API keys
3. Go to **Dashboard** → pick a preset → **Wake TED**
4. Watch TED live. Talk to it. Star interesting moments. Browse its files.
5. When done, save the session to **Gallery**.

## 🔑 API Keys (Free)

| Service | Free Tier | Get Key |
|---------|-----------|---------|
| **OpenRouter** | Free credits on signup | [openrouter.ai/keys](https://openrouter.ai/keys) |
| **E2B** | 100 sandbox hours/month | [e2b.dev/dashboard](https://e2b.dev/dashboard) |

## 🎭 Presets

| Preset | What TED Does |
|--------|---------------|
| 🤖 Free Agent | Whatever it wants. Pure autonomy. |
| 🔓 Security Researcher | Port scans, CVE checks, network recon |
| 💻 GitHub Developer | Clones repos, writes code, pushes PRs |
| 🎨 Creative Coder | Generative art, ASCII art, games |
| 📊 Data Scientist | Explores datasets, creates visualizations |
| ⛓️ Blockchain Explorer | Queries chains, analyzes contracts |
| 🌐 Web Builder | Builds and serves websites |
| 🔍 Research Assistant | Deep research via curl + synthesis |
| 🛠️ DevOps / Sysadmin | System audits, automation scripts |
| 🐛 Bug Bounty Hunter | Attack surface enumeration |
| 🏗️ Full-Stack Builder | Builds complete apps |
| 🧪 AI/ML Engineer | Trains models, runs experiments |
| 📝 Custom | Blank slate — your rules make him write your emails for you, dance for you or die for you! |

## 📄 Pages

- **Dashboard** — Control panel + live feed + TED's mind + inject messages
- **Terminal** — Raw shell I/O view
- **Files** — Browse sandbox filesystem + download files
- **Gallery** — Saved sessions with diary entries
- **Settings** — API keys, 30+ integrations, themes, memory management

## 🧠 TED Memory

At the end of each session, TED writes a message to its next instance. The next TED reads this on boot, creating continuity across sessions. You can view, edit, or clear the memory in Settings.

## 🏗️ Architecture

```
Browser (localStorage + IndexedDB) ←→ Flask (stateless) ←→ OpenRouter + E2B
```

Zero server-side storage. Your keys never leave your browser except per-request.

## 📄 License

MIT

## 🤝 Contributing

PRs welcome. Adding a new preset is as easy as creating a JSON file in `presets/`.
