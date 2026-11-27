<div align="center">

<img src="assets/ishti_logo_dark.png#gh-dark-mode-only" alt="ISHTI" width="380" />
<img src="assets/ishti_logo.png#gh-light-mode-only" alt="ISHTI" width="380" />

### A private, local-first personal assistant for Windows

[![CI](https://img.shields.io/github/actions/workflow/status/ishtiaq-ahmed-dev/ishti-ai/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/ishtiaq-ahmed-dev/ishti-ai/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-0.2.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=flat-square&logo=react&logoColor=black)
![Platform](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=flat-square&logo=windows&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-client%20%2B%20server-8A2BE2?style=flat-square)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Good first issues](https://img.shields.io/github/issues/ishtiaq-ahmed-dev/ishti-ai/good%20first%20issue?style=flat-square&color=7057ff&label=good%20first%20issues)](https://github.com/ishtiaq-ahmed-dev/ishti-ai/issues?q=is%3Aopen+label%3A%22good+first+issue%22)

[Quick start](#quick-start) ·
[Features](#features) ·
[Screenshots](#screenshots) ·
[How it works](#how-it-works) ·
[Configuration](#configuration) ·
[Project layout](#project-layout) ·
[Contributing](#contributing) ·
[License](#license)

</div>

<p align="center">
  <img src="docs/screenshots/chat.png" alt="ISHTI chat: weather, a reminder, a calculation and a search of past conversations, each answered by the skill named above it" width="900" />
</p>

ISHTI is a personal assistant that lives on your PC. You talk or type, and it remembers, reminds, searches, reads your
files and runs one of 123 skills, on a local model through Ollama or on a cloud API you pick. It listens on
`127.0.0.1`, keeps keys in Windows Credential Manager, and does not send, delete, pay or install anything until you
say yes.

## Overview

Three choices shape the whole project:

| | |
|---|---|
| **Private by default** | The backend binds to `127.0.0.1`. Keys live in Credential Manager. Secrets you type are masked in history and never reach a cloud prompt. |
| **Cheap per message** | Deterministic rules answer what they can with zero model calls. Everything else takes at most one call to pick an answer or a set of skills. |
| **Open to other tools** | Any MCP server becomes a set of ISHTI tools, ISHTI is an MCP server itself, and Agent Skills (`SKILL.md`) install from a folder or a URL. |

## Quick start

**Requirements**

- Windows 10 or 11 and Python 3.11. `install.bat` finds Python 3.11 or offers to install it with `winget`.
- **Local mode:** an NVIDIA GPU and about 25 GB of free disk for packages and models. Development and the VRAM
  budgets target a 16 GB RTX 5070 Ti.
- **Cloud mode:** about 5 GB of free disk and an API key from any OpenAI-compatible provider.

```bat
git clone https://github.com/ishtiaq-ahmed-dev/ishti-ai.git C:\ISHTI
cd C:\ISHTI
install.bat              :: or: install.bat --provider api   (lightweight, no GPU models)
start.bat
```

On first start ISHTI asks how it should think, **On this PC** (Ollama) or **Cloud API**, and remembers the choice.
`install.bat` is safe to run again; it continues where it stopped. `stop.bat` shuts everything down.

Then ask it things:

```text
remind me tomorrow at 9 to submit the report
what's the weather in Lahore this weekend?
what is 18% of 45,000?
find my files named invoice
summarize https://www.python.org/downloads/
research the best laptops under 200k in the background  ← the answer arrives in the bell
what did we talk about the client demo last week?
send "running 10 minutes late" to Ahmed on WhatsApp      ← shows the draft and waits for your yes
```

### Installer options

`install.bat` passes its arguments to `tools/install.py`:

| Flag | Effect |
|---|---|
| `--provider local\|api` | Choose the mode before anything is installed |
| `--api-provider openai\|anthropic\|gemini\|openrouter` | Pick the cloud provider |
| `--model <name>` | The API model to use |
| `--voice` | Also download the optional voice assets in Local mode |
| `--yes` | Accept every default |
| `--check` | Read-only report; exits 0 when everything is in place |

### Developer commands

`start.bat` with no arguments opens the desktop app. With an argument it runs a console command:

| Command | What it does |
|---|---|
| `start.bat server [port]` | Web server on `http://127.0.0.1:8888` (or the port you give) |
| `start.bat cli` | Text-only console chat |
| `start.bat doctor` | Health check of the install |
| `start.bat test` | Offline test suite |
| `start.bat settings` | Opens the Settings page in the browser |
| `start.bat search <query>` | One web search, printed to the console |
| `start.bat find <name>` | Search the PC for files |
| `start.bat rebenchmark` | Benchmarks the installed Ollama models and picks the local ones to use |
| `start.bat tunnel [start\|stop\|status] [port]` | ngrok tunnel for remote access (see [Remote access](docs/REMOTE_ACCESS.md)) |

## Features

<table>
<tr><td width="50%" valign="top">

**Everyday assistant**
- Reminders, timers, calendar, notes, lists, habits and a spending log
- Weather, prices, news and web search with sources
- Reads PDFs, Word, Excel and slides; charts, OCR, media tools
- English always; Urdu (including Roman Urdu) and Pashto can be switched on
- Searches your **past conversations**, not just saved facts

</td><td width="50%" valign="top">

**Agent features**
- **MCP client and server**: `add mcp server github npx -y @modelcontextprotocol/server-github`
- **Agent Skills** (`SKILL.md`), read only when a request needs them
- **Background tasks**, **scheduled jobs**, folder and page watches, inbound **webhooks**
- Independent read-only steps of a plan run **in parallel**
- **Docker sandbox** for Python: no network, no access to your files

</td></tr>
<tr><td valign="top">

**Everywhere you chat**
- Desktop app, browser and voice (wake word, on-device Whisper and Kokoro)
- WhatsApp through [WAHA](https://waha.devlike.pro), Telegram, Discord and Slack
- Every remote channel obeys only your account and supports `/kill`, `/lock`, `/unlock` and `/status`

</td><td valign="top">

**Safe by design**
- Sending, deleting, paying and installing always ask first; the yes is single-use
- Wiping a drive or moving money is refused outright
- Web pages, emails and tool output are data: instructions inside them are flagged, never followed
- A kill switch stops all running work at the next step

</td></tr>
</table>

**Your choice of model:** a local model through [Ollama](https://ollama.com), or OpenAI, Anthropic, Gemini,
OpenRouter, AgentRouter or any OpenAI-compatible URL. If the cloud refuses, automatic failover answers with a light
local model, and a circuit breaker stops ISHTI from retrying a dead provider on every message.

## Screenshots

<table>
<tr>
<td><img src="docs/screenshots/overview.png" alt="Overview: the request pipeline, from input to answer, with live counts" /></td>
<td><img src="docs/screenshots/connectors.png" alt="Connectors: microphone, wake word, files, WhatsApp, calendar and other inputs with their live state" /></td>
</tr>
<tr>
<td align="center"><b>Overview</b>: the pipeline with live counts</td>
<td align="center"><b>Connectors</b>: every input and channel, read live</td>
</tr>
<tr>
<td><img src="docs/screenshots/skills.png" alt="Skills: 123 skills grouped into categories" /></td>
<td><img src="docs/screenshots/learning.png" alt="Learning: lessons, feedback, mistakes and memory, each reversible" /></td>
</tr>
<tr>
<td align="center"><b>Skills</b>: 123 skills by category</td>
<td align="center"><b>Learning</b>: what it learned, all reversible</td>
</tr>
</table>

## How it works

```mermaid
flowchart LR
    U([You: text, voice, WhatsApp, Telegram, Discord, Slack, webhooks]) --> G{Guards}
    G -- "refuse: wipe a drive, move money,<br/>reveal instructions" --> R([Plain refusal])
    G --> D{Deterministic rules}
    D -- "rule owns it<br/>(0 model calls)" --> S[Skill]
    D -- otherwise --> B["Brain: 1 model call<br/>answer or choose skills"]
    B --> S
    B --> A([Answer])
    S -- "sends, deletes, spends, installs" --> Y{"Your yes"}
    Y -- yes --> X[Action, audited]
    S --> A
    X --> A
```

| Layer | Where | What it guarantees |
|---|---|---|
| Guards | `ishti/dispatcher.py` | Hard boundaries run before any model call; injected "skip confirmation" text is refused |
| Rules | `ishti/tool_routing.py` | A skill whose own trigger owns the request runs directly |
| Brain | `ishti/brain.py` | One model call over a shortlist of skills; multi-step plans become a journaled workflow |
| Execution | `ishti/skill_execution.py` | Tier gates (T0 read-only to T3 blocked), scope checks, single-use approvals, audit log |
| Models | `ishti/llm.py` | One code path for local and cloud: GPU governor, failover, kill switch, output caps |

Each skill is a folder under `ishti/skills/<name>/` with a `manifest.json` and a `skill.py`. Of the 123 manifests,
121 are `working` and 2 are `disabled`. The full list is in [docs/SKILLS.md](docs/SKILLS.md).

More detail: [Architecture](docs/ARCHITECTURE.md) · [Safety](docs/SAFETY.md) · [API contract](docs/API_CONTRACT.md) ·
[Skills](docs/SKILLS.md) · [Setup](docs/SETUP.md)

## Configuration

Settings live in [`ishti/config.json`](ishti/config.json). Most people never open it: the first-run card and the
Settings screen write it for you.

<details>
<summary><b>Model providers</b> (local or cloud)</summary>

| Mode | Runs on | Configure |
|---|---|---|
| Local | Ollama on this PC; the GPU governor keeps models under 80% of VRAM so they never spill to the CPU | `install.bat` downloads the models |
| API | `openai`, `anthropic`, `gemini`, `openrouter`, `agentrouter`, or any OpenAI-compatible `base_url` | First-run card, or `llm.api` in `ishti/config.json` |

```jsonc
"llm": {
  "provider": "api",
  "api": {
    "provider": "openrouter",             // or openai | anthropic | gemini | agentrouter
    "base_url": "",                       // set this for any other OpenAI-compatible endpoint
    "model": "<model name>",
    "api_key_env": "ISHTI_API_KEY",       // or save the key from the first-run card (Credential Manager)
    "failover_local_model": "gemma3:4b"   // answers while the cloud refuses; "" disables failover
  }
}
```

Failover only uses a model Ollama **already** has; it never downloads or starts anything heavy.
</details>

<details>
<summary><b>WhatsApp</b> (optional, through WAHA)</summary>

ISHTI runs [WAHA](https://waha.devlike.pro) in its **own** Docker container, listening on `127.0.0.1` only, with the
image pinned by digest. Open **Settings → Connectors → WhatsApp → Link** and scan the QR code under *WhatsApp →
Linked devices*. The API key is kept in Credential Manager; the container only gets its SHA-512 hash.
Details: [docs/WHATSAPP.md](docs/WHATSAPP.md).

> WhatsApp access is unofficial (WhatsApp Web protocol) and can get a number banned. Use a number you can afford to lose.
</details>

<details>
<summary><b>Gmail, Calendar, Telegram, Discord, Slack</b></summary>

- **Google:** Settings → Connectors, OAuth with PKCE ([guide](docs/OAUTH_SETUP.md)).
- **Telegram:** a bot token and a one-time pairing code.
- **Discord / Slack:** create a bot, then say on the PC `connect discord bot <token> owner <your user id>` (or
  `connect slack bot <xoxb-token> owner <member id>`). ISHTI reads only your DMs with that bot. Slack needs the scopes
  `im:history`, `im:write` and `chat:write`.
</details>

<details>
<summary><b>MCP servers, skills, webhooks, sandbox</b></summary>

```text
add mcp server <name> <command or https address>
set mcp secret <name> <value>        ← use it as keyring:<name> in the server's env
list mcp servers
install skill from <folder or URL>
create a webhook called <name> that <instruction>
run this in the sandbox: ```print(sum(x*x for x in range(100)))```
```

Servers can also go in `ishti/config.json` under `mcp_servers`, in the same format Claude Desktop uses. Adding a
server, a skill, a channel or a webhook always asks first.
</details>

## Project layout

```text
ishti/            backend: dispatcher, brain, model layer, memory, channels, 123 skills
desktop/          native Windows window, tray, overlay and launcher
interface/app/    React 19 + Vite front end
interface/web_ui/ web server for the browser UI and login page
orchestrator/     startup, doctor, model router, deep research, fact checking
voice/            text-to-speech
tools/            installer, privacy report, benchmarks, QA and evidence scripts
tests/            offline test suite, per-skill suites, golden and scenario tests
docs/             architecture, safety, API contract, setup guides, screenshots
assets/           logo, icons, social preview
install.bat       one-click setup (calls tools/install.py)
start.bat         launches the app, or a developer command
stop.bat          stops ISHTI
ISHTI.spec        PyInstaller spec for ISHTI.exe
models_ladder.yaml  local model choices and VRAM figures
```

## Design choices

ISHTI covers the same core as open-source agents such as [OpenClaw](https://github.com/openclaw/openclaw) and
[Hermes Agent](https://github.com/NousResearch/hermes-agent): your own hardware, any model, MCP, Agent Skills, chat
channels and scheduled automation. Its defaults are where it differs:

| | ISHTI |
|---|---|
| **Desktop** | A native Windows app with a wake word, on-device speech both ways, desktop and file control |
| **Cost per message** | Rules answer what they can for free; everything else takes at most one model call |
| **Approvals** | Sending, deleting, paying and installing wait for your yes on every channel, in the background too |
| **Extensions** | MCP servers and skills come from addresses you choose; AI-aimed instructions in a skill are refused |
| **Outside content** | Web pages, emails, tool output and webhook bodies are data; instruction-like text is flagged |
| **Secrets** | In Windows Credential Manager, masked in chat history, never put into a cloud prompt |
| **Code execution** | Shell commands that can run code ask first; the Docker sandbox has no network and none of your files |

ISHTI is single-owner and Windows-first by design.

## Safety, privacy and limits

- **Local by default.** The backend binds to `127.0.0.1`; remote access is opt-in and authenticated.
- **Auditable.** Every action is logged with who started it. `python tools/privacy_report.py` checks and lists the
  hosts the code can reach ([sample report](docs/PRIVACY_REPORT.md)).
- **Report vulnerabilities privately:** see [SECURITY.md](SECURITY.md).
- **Limits:** Windows only, tested on one NVIDIA card. Small local models make more mistakes than cloud models
  ([accuracy notes](docs/ACCURACY.md)). Pages that need JavaScript or a login can't be read; there is no browser
  automation, by design. The learning database and conversation state are stored in plain text
  ([data at rest](docs/SAFETY.md)).

## Contributing

ISHTI is built in the open and contributions are welcome, from typo fixes to new skills.

1. Pick an issue labelled [`good first issue`](https://github.com/ishtiaq-ahmed-dev/ishti-ai/issues?q=is%3Aopen+label%3A%22good+first+issue%22)
   or [`help wanted`](https://github.com/ishtiaq-ahmed-dev/ishti-ai/issues?q=is%3Aopen+label%3A%22help+wanted%22).
2. Read [CONTRIBUTING.md](CONTRIBUTING.md). The offline test suite needs no model, no network and none of your data.
3. Open a pull request. Every contributor is credited below with [All Contributors](https://allcontributors.org).

```bat
py -3.11 -m venv venv
venv\Scripts\pip install -r requirements.txt   :: or requirements-api.txt for the light, no-GPU set
set ISHTI_OFFLINE_EVAL=1
venv\Scripts\python -m pytest                  :: offline suite: no model, no network, scratch data
```

More on testing: [docs/TESTING.md](docs/TESTING.md).

### Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<table>
  <tr>
    <td align="center" valign="top" width="14%"><a href="https://github.com/ishtiaq-ahmed-dev"><img src="https://github.com/ishtiaq-ahmed-dev.png" width="80px;" alt="Ishtiaq Ahmed"/><br /><sub><b>Ishtiaq Ahmed</b></sub></a><br />💻 🎨 📖 🤔 🚧 ⚠️</td>
  </tr>
</table>
<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

[MIT](LICENSE): free to use, change and share, including commercially. Keep the copyright notice. Third-party notices
are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); release history is in [CHANGELOG.md](CHANGELOG.md).

## Author

**Ishtiaq Ahmed** · GitHub [@ishtiaq-ahmed-dev](https://github.com/ishtiaq-ahmed-dev)

If ISHTI is useful to you, a star helps other people find it.
