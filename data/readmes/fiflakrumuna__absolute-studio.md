# ⚡ Absolute Studio

> Lightweight, desktop workspace and autonomous AI coding agent built with **Tauri v2**, **Rust**, and **React + TypeScript**.

![Tauri](https://img.shields.io/badge/Tauri-v2-24C8D8?style=flat-square&logo=tauri&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-Backend-000000?style=flat-square&logo=rust&logoColor=white)
![React](https://img.shields.io/badge/React-TypeScript-61DAFB?style=flat-square&logo=react&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-white?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)


[Absolute Studio Preview](./screenshot.png)

---

## 🚀 Overview

**Absolute Studio** bridges local and cloud Large Language Models with your local filesystem and terminal. Unlike standard chat wrappers, it acts as an **autonomous coding and research agent** capable of reading, searching, creating, and patching files on disk, compiling and running commands, and searching the live web—all inside a fast, low-overhead native desktop window.

---

## ✨ Key Features

- **🔄 Hybrid LLM Engine (Local & Cloud):**
  - **Local Mode:** Native integration with **Ollama** (`qwen3.5:9b` or any locally pulled model) for 100% private, offline inference.
  - **Cloud Mode:** Connect to **OpenRouter**, Cloudflare Tunnels, or any OpenAI-compatible API endpoint with persistent API key & model storage.
- **🤖 Autonomous Workspace Agent:**
  - Mount any local project directory (`WORKSPACE`) to grant the agent controlled access to workspace tools:
    - `list_files` & `search_files` — Explore project structure and search symbols across files.
    - `read_file` & `write_file` — Read context and create or overwrite files directly on disk.
    - `edit_file` — Apply surgical code patches using exact `<<<SEARCH / >>>REPLACE` blocks.
    - `run_command` — Compile code, run tests, and execute shell scripts with real-time `EXIT_CODE` feedback.
- **🌐 Live Web Research Tools:**
  - Built-in `web_search` and clean webpage text extraction (`fetch_url`) implemented natively in Rust—works even when no local workspace is mounted.
- **⚡ Real-Time Streaming & Instant Abort:**
  - Token-by-token streaming over Tauri IPC channels with full **GitHub Flavored Markdown** rendering, tables, and one-click code block copying.
  - Instant mid-stream generation cancellation via the **`■ STOP`** button or **`Esc`** key (backed by an atomic Rust abort flag).
- **🎨 Customizable Terminal Aesthetic:**
  - 5 built-in themes (**Matrix**, **Amber**, **Cyber**, **Minimal**, **Clean**), custom accent color picker, font family switcher, and persistent UI preferences.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Desktop Framework** | Tauri v2 (`@tauri-apps/api`, `@tauri-apps/plugin-dialog`) |
| **Backend** | Rust, `tokio`, `reqwest` (streaming HTTP), `serde` |
| **Frontend** | React 18, TypeScript, Vite |
| **Markdown & UI** | `react-markdown`, `remark-gfm`, CSS Variables |
| **AI Providers** | Ollama REST API, OpenRouter / OpenAI Chat Completions API |

---

## 📦 Installation & Usage

### Option 1: Download Pre-built Release (Windows)
1. Go to the [**Releases**](https://github.com/fiflakrumuna/absolute-studio/releases) page.
2. Download the latest `.exe` (NSIS) or `.msi` installer from **Assets**.
3. Run the installer and launch **Absolute Studio**.

### Option 2: Build from Source

#### Prerequisites
- [Node.js](https://nodejs.org/) (v18+)
- [Rust & Cargo](https://rustup.rs/)
- [Tauri v2 Windows Prerequisites](https://v2.tauri.app/start/prerequisites/) (WebView2 & C++ Build Tools)
- *(Optional)* [Ollama](https://ollama.com/) running locally (`ollama run qwen3.5:9b`)

#### Development Mode
```bash
git clone [https://github.com/](https://github.com/)fiflakrumuna/absolute-studio.git
cd <nazwa-repo>
npm install
npm run tauri dev
```

#### Production Build

```bash
npm run tauri build
```