<p align="center"><img src="docs/assets/nestor-cli-wordmark.svg" alt="Nestor Agent" width="880"></p>

# Nestor Agent

<p align="center">
  <a href="docs/README.md"><img alt="Documentation" src="https://img.shields.io/badge/DOCS-NESTOR_AGENT-f4c430?style=for-the-badge"></a>
  <a href="docs/screenshots.md#english"><img alt="Screenshots" src="https://img.shields.io/badge/GALLERY-SCREENSHOTS-5457de?style=for-the-badge"></a>
  <a href="LICENSE"><img alt="License: AGPL-3.0-or-later" src="https://img.shields.io/badge/LICENSE-AGPL--3.0--OR--LATER-4d8a16?style=for-the-badge"></a>
  <br>
  <a href="README.vi.md"><img alt="Tiếng Việt" src="https://img.shields.io/badge/LANG-TI%E1%BA%BENG_VI%E1%BB%86T-c83e47?style=for-the-badge"></a>
</p>

Nestor Agent is an open-source personal AI assistant that runs on your machine. Chat in the terminal or browser, ask questions about your documents, and hand off jobs to a background gateway. Nestor stores conversations, workspace files, and memory locally. You choose whether to use a local model or a cloud provider.

## What Nestor can do

| Capability | How it works |
|---|---|
| **Your choice of models** | Run Ollama or another OpenAI-compatible local endpoint, or configure cloud providers such as Gemini, Claude, OpenAI, and OpenRouter. Set fallback providers in your configuration. |
| **Terminal, browser, and messaging** | Use the interactive CLI with streaming responses and slash commands, open the web UI with a workspace panel, or connect Telegram or Zalo OA through the gateway. |
| **Ask across your documents** | Index PDF, Word, spreadsheets, slides, Markdown, and text. Search a single category or the whole library and follow citations back to source passages. OCR supports scanned PDFs when Tesseract is available. |
| **Notes and office files** | Edit notebook pages with an AI panel. Create Word documents, Excel workbooks with formulas, and PowerPoint decks. Dedicated assistants support Vietnamese administrative documents. |
| **Background work and automations** | Dispatch a Kanban card, monitor long-running tasks, schedule recurring jobs, and use Heartbeat to check for things that need attention. |
| **Memory, skills, and tools** | Reuse Markdown memory and search past conversations. Install `SKILL.md` skills or connect MCP servers to add tools. |
| **Integrate with other apps** | Invoke Nestor with an API token through `POST /v1/run` or expose it to an MCP client through `agent_run`. |

## Quick install

### From source

Requires Python 3.11 or newer. Building the web interface also requires Node.js 20 or newer.

```bash
git clone https://github.com/tranvanhuy-hichan/ai-nestor-agent.git
cd ai-nestor-agent
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e app/backend
nestor onboard
```

For the web interface, build the frontend from the repository root.

```bash
(cd app/frontend && npm install && npm run build)
nestor start
nestor open
```

### Docker

```bash
docker compose up -d --build
```

Open the web UI at `http://127.0.0.1:8787`. The Compose setup stores data in `./user-data`. See the [installation guide](docs/huong-dan-su-dung.md#2-cài-đặt-và-chạy-lần-đầu) for desktop packages and setup details.

## Getting started

```bash
nestor                         # Start an interactive terminal chat
nestor run "Summarize this file" # Run a single task and exit
nestor onboard                 # Configure models, workspace, and integrations
nestor status                  # Inspect the gateway and current configuration
nestor skills list             # Browse installed and available skills
nestor logs -f                 # Follow gateway logs
nestor doctor                  # Diagnose setup problems
```

`nestor` and `nestor run` work without a running gateway. Start the gateway for the web UI or messaging channels. For automatic startup, see `nestor service install` in the [CLI reference](docs/cli.md). The CLI defaults to English. Use `--lang vi` or `NESTOR_LANG=vi` for Vietnamese.

## Documentation

| Guide | What's covered |
|---|---|
| [User guide](docs/huong-dan-su-dung.md) | Installation, models, chat, documents, automations, and troubleshooting |
| [CLI reference](docs/cli.md) | Commands, flags, environment variables, and examples |
| [API and assistant workflows](docs/api-assistants.md) | Calling specialized assistants from other applications |
| [Architecture](docs/kien-truc.md) | Gateway, agent loop, tool permissions, and storage |
| [Screenshot gallery](docs/screenshots.md#english) | Web UI, document citations, notebooks, and terminal screens |

Most in-depth guides are currently in Vietnamese.

## Data and security

Nestor uses `user-data/` by default. Set `NESTOR_HOME` to choose another location. The gateway binds to localhost by default. Review downloaded skills and MCP servers before enabling them, and keep tool approval enabled for actions you want to confirm. Use `nestor backup` before moving your workspace. See the [security policy](SECURITY.md) for reporting vulnerabilities.

## Contributing

Bug reports, translations, docs, skills, and code contributions are welcome. See the [contribution guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md).

## License

GNU AGPL-3.0-or-later. See [LICENSE](LICENSE).
