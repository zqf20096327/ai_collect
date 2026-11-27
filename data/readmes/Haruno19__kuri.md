<p align="center">
  <img src="docs/images/app-icon.png" width="128" alt="Kuri app icon">
</p>

<h1 align="center">Kuri</h1>

A lightweight, macOS native, human-designed & Claude-coded app for working with language models, that can chat, think, and act on your files from a sandbox.

Kuri runs offline with local models, talks to any hosted provider when you want it to, discovers MCP servers at runtime, and runs the model's commands inside a lightweight Linux VM. 

<p align="center">
  <img height="320" alt="Main window" src="docs/images/main-window.png" />
  <img height="320" alt="Mini window" src="docs/images/mini-window.png" />
</p>

## Principles

- **Essential.** Few features, just the ones you need. Few dependencies, and only official ones (Apple, or official SDKs).
- **Local-first.** Works with no network. Hosted providers are opt-in.
- **Mac-only, Mac-native.** SwiftUI + AppKit, Apple frameworks, macOS conventions. No cross-platform abstractions.
- **Hackable.** Providers, models and MCP servers live in plain JSON5 files you can edit by hand.
- **Provider-agnostic.** Every major wire format is a first-class adapter. Switching model mid-conversation just works.

## Gallery
<p align="center">
  <img width="48%" alt="Light theme welcome page" src="docs/images/welcome-light.png" />
  <img width="48%" alt="Dark theme welcome page and inspector" src="docs/images/welcome-dark-inspector.png" />
  
  <img width="48%" alt="Dark theme chat and inspector" src="docs/images/chat-dark-inspector.png" />
  <img width="48%" alt="Light theme chat with LaTeX and sidebar" src="docs/images/chat-light-latex.png" />
  
  <img width="48%" alt="Light theme chat with both sidebars" src="docs/images/chat-light-sidebars.png" />
  <img width="48%" alt="Dark theme chat with a codeblock and sidebar" src="docs/images/chat-dark-code.png" />

  <img width="48%" alt="kuri in the terminal, switching models and saying hello" src="docs/images/cli-model.png" />
  <img width="48%" alt="kuri in the terminal, listing a folder's files with a shell command" src="docs/images/cli-shell.png" />

</p>

## Install

Kuri needs a Mac with Apple silicon and macOS 26. Download the `.dmg` from [Releases](https://github.com/Haruno19/kuri/releases), open it and drag Kuri to Applications.

Releases aren't notarized by Apple yet, so the first time you open Kuri macOS says it can't verify it. Open **System Settings › Privacy & Security**, scroll down to the message about Kuri and click **Open Anyway**. Or, in Terminal:

```bash
xattr -dr com.apple.quarantine /Applications/Kuri.app
```

### In the terminal

Kuri also ships `kuri`, a command-line client, inside the app. Put it on your `PATH` once; the link points into the app, so it keeps working when you update Kuri:

```bash
sudo ln -sf /Applications/Kuri.app/Contents/Helpers/kuri /usr/local/bin/kuri
```

`kuri` starts a session in the current folder, `kuri -p "…"` answers once and exits (piped input joins the prompt), `-c` continues this folder's latest conversation and `-r` picks an older one; `kuri --help` has the rest. It uses the same configuration and conversations as the app, so set up providers and keys in the app first. One runs at a time: start one while the other is open and it offers to quit the other.

## Architecture

```
+------------------------------------- Kuri.app -------------------------------------+
|                                                                                    |
|  App (SwiftUI)   main window, mini window       kuri (CLI)   in Contents/Helpers,  |
|                  (menu bar), settings                       a session or one turn  |
|        |  observes EngineEvents, calls Engine methods  |   the same, with an       |
|        v                                               v   engine of its own       |
|  KuriAgent       Engine (actor), TurnRunner, InteractionBroker                     |
|        |                                                                           |
|        +------------+------------+------------+------------+------------+          |
|        v            v            v            v            v            v          |
|  KuriInference  KuriMCP      KuriSandbox  KuriTools    KuriStore    KuriConfig     |
|  adapters       MCP servers  Linux VMs,   registry,    SQLite       JSON5 files,   |
|  (HTTP + SSE)   as tools     shell tool   built-ins    file         Keychain       |
|        +------------+---- KuriCore (domain types) ---------+------------+          |
|                                                                                    |
|  Each sandbox VM runs in its own system process (Virtualization.framework).        |
+------------------------------------------------------------------------------------+
```

**The engine is in-process.** The SwiftUI layer talks to `Engine` directly and subscribes to its event stream; the local UI never goes through HTTP. `kuri`, the command-line client, does the same with an engine of its own on the same files, so only one of the two runs at a time ([decision 0028](docs/decisions/0028-command-line-client.md)).

**Stateless towards providers.** Every request carries the history it needs, rebuilt from Kuri's database, as a list of items (messages, reasoning, tool calls and results, summaries) rather than pre-formatted chat messages. That keeps behaviour identical across providers, works offline, and makes switching model mid-conversation trivial.

**Configuration in files, data in SQLite.** Providers, models, tool policies and MCP servers live in JSON5 files in `~/.config/kuri`; conversations live in one small SQLite file; secrets in the Keychain.

### Modules

| Module | Responsibility | Depends on |
|---|---|---|
| `KuriCore` | `Item`, `Message`, `ToolCall`, `ToolSpec`, `InferenceEvent`, `Usage`, `ModelRef`, `JSONValue` | — |
| `KuriConfig` | Resolves `~/.config/kuri` and locks it (one engine at a time), loads and watches `config.json` / `mcp.json`, edits `config.json` for the UI, resolves secrets from the Keychain or the environment and keeps API keys in the Keychain | Core |
| `KuriStore` | SQLite wrapper, migrations, conversations, turns, items, full-text search, memories | Core |
| `KuriInference` | `InferenceProvider` protocol, SSE parser, one adapter per wire format, model discovery | Core, Config |
| `KuriTools` | `Tool` protocol, `ToolRegistry`, permission policy, built-in tools | Core, Store |
| `KuriAgent` | `Engine` facade, `TurnRunner` (the agent loop), `InteractionBroker` (clarify/approval), event broadcasting, `RepositoryStatus` (git status for the inspector) | all of the above |
| `KuriMCP` | MCP connections on the official Swift SDK: config diffing, discovery, process transport, MCP tools as `Tool`s | Core, Config, Tools |
| `KuriSandbox` | Linux containers on Apple's Containerization: setup, one VM per conversation, mounts; the `shell` tool | Core, Config, Tools |

Dependencies point one way: down towards `KuriCore`. Nothing in the package imports SwiftUI.

```
Kuri/
├─ Kuri.xcodeproj         The app target (sources are a folder-synchronized group)
├─ App/                   SwiftUI app
├─ CLI/                   The `kuri` command-line client, embedded in the app
├─ Packages/KuriKit/      Everything that isn't UI: the modules above, and their tests
├─ docs/                  Design, flows, configuration, UI brief, decisions
├─ CLAUDE.md              Working agreements and commands
└─ Sketches/              UI experiments (not part of the build)
```

## Tools

Every tool implements `Tool`: a spec (name, description, JSON Schema), a default policy, whether it is read-only, and an async `run`. The `ToolRegistry` holds them all, built-in and discovered alike, each tagged with its source (`builtIn` or `mcp(server:)`), and decides which ones the model sees.

| Tool | What it does | Default |
|---|---|---|
| `clarify` | Ask the user one or more questions and wait for the answers | allow |
| `tasklist` | Write the current plan (the whole list each call) | allow |
| `memory` | Add, update or remove long-term memories, in one batched call | allow |
| `conversation_search` | Full-text search over past conversations, or this one | allow |
| `shell` | Run a command in the conversation's Linux container, from `/work` | allow (it's sandboxed) |
| MCP tools | Discovered at runtime, named `<server>__<tool>` | allow if the server marks them read-only, else ask |

Policies (`allow`, `ask`, `deny`) can be set per tool in `config.json` and per MCP server in `mcp.json`. There are no file tools and no artifacts: the shell lists, reads, searches and writes files, and a file the model creates is just a file. See [docs/design.md](docs/design.md#tools).

## Providers

| Wire format | Used for |
|---|---|
| `open-responses` | OpenAI, Ollama, LM Studio, vLLM, and anything else speaking the Open Responses spec |
| `anthropic-messages` | Anthropic's API, and servers that copy it (Ollama among them) |
| `apple-foundation-models` | Apple's on-device model (FoundationModels): offline and free, text only, a natural utility model |

## Setting up a provider

Providers are declared in `~/.config/kuri/config.json`; their API keys live in the Keychain. Starting from a Claude API key:

1. **Declare the provider.** Settings › General › Open config.json, and add it under `providers` (Kuri reloads the file when you save it):

   ```json5
   anthropic: { format: "anthropic-messages" },
   ```

2. **Save the key.** Settings › Models › anthropic › API key: paste it and press Return. Kuri stores it in the Keychain (service `Kuri`, named `anthropic`) and writes `apiKey: "keychain:anthropic"` into the provider; the key itself never touches a file.
3. **Add a model.** In the same section, pick one from the Model id suggestions (the models your key can use), give it a context window (1,000,000 for current Claude models, for automatic compaction) and Add. Its menu has Use for New Conversations.

Any other provider works the same way with its own `format` and, if it isn't the format's default, `baseURL`; local servers like Ollama need no key. Every option is in [docs/config.md](docs/config.md).

## Footprint

Measured on a MacBook Pro (M1 Pro, 16 GB, macOS 27.2) as the memory figure Activity Monitor shows (physical footprint).

| | Kuri |
|---|---|
| On disk | 58 MB (Apple silicon): 27 MB for the app and 25 MB for `kuri`, each with the whole engine in it, plus ≈ 1.6 GB for the sandbox once it's set up with Kuri's image, ≈ 0.8 GB with `python:3-slim` (7) |
| Running, idle | ≈ 40 MB |
| Running, during an agent turn | ≈ 40–65 MB (1) |
| A conversation open | + ≈ 30 MB for the transcript, however long it is (3) |
| Once a reply has LaTeX | + ≈ 25 MB for MathJax, kept until quit (4) |
| Mini window open | + ≈ 18 MB, and ≈ 10 MB more with a chat in it, however long (5) |
| Inspector open | + ≈ 2–4 MB, from a short chat to 200 commands and 150 changed files (6) |
| The meadow on the new chat page | + ≈ 0.3 MB, ≈ 2% CPU while it's on screen (8) |
| Sandbox VM, booted or doing light shell work | + ≈ 300 MB |
| Sandbox VM after a 300 MB workload | + ≈ 600 MB until the container stops (2) |

1. The app idle (≈ 40 MB) plus the engine alone during a turn that ran shell commands (24 MB at its peak).
2. The Linux guest doesn't hand freed memory back to macOS, so a VM holds its peak until it stops: after `idleMinutes` (10 by default), on Stop, or on quit. `sandbox.memoryMiB` (2 GB by default) caps it.
3. Measured by rendering the app's own reply views in an offscreen window, with 40 and with 120 Markdown-heavy answers (text, a list, a code block and a table each): both ≈ 32 MB. The transcript only builds the messages near the visible area; built in full, the same answers took ≈ 217 MB and ≈ 611 MB.
4. MathJax loads the first time a formula appears; with 40 answers holding formulas the transcript came to ≈ 56 MB.
5. Measured like (3), with the app's own mini window views in an off-screen panel: its second model on the engine adds under 1 MB, the empty glass window ≈ 18 MB, and a chat of 40 or of 120 Markdown-heavy answers ≈ 10 MB more (its transcript is lazy too). It has no LaTeX rendering, so MathJax never loads for it.
6. Measured like (3), with the app's own main window in an off-screen window, opening the inspector on a chat of 8 commands, on one of 204 commands with output, and on the same with a repository of 150 changed files: + 2.4, + 2.8 and + 3.8 MB. Steps shows the latest few and lists the rest lazily on Show all (built in full, the 204 took ≈ 12 MB), and Git the first 12 changes of each repository (all 150 took ≈ 18 MB). Git status runs `git` in separate, short-lived processes. At rest, open or closed, the inspector takes no CPU.
7. Measured with `python:3-slim` (a 45 MB download). Kuri's image is a 254 MB download; its total is estimated from the layer sizes, not yet measured.
8. Memory measured like (3), the app's new chat page with `meadow` on and off; CPU measured in its sketch (`Sketches/Meadow.swift`) at 12 frames a second. It stops while the window is hidden and with Reduce Motion.

## Documentation

| Document | What's in it |
|---|---|
| [docs/design.md](docs/design.md) | How each part works, in detail |
| [docs/flows.html](docs/flows.html) | Every flow as a sequence diagram with the code behind each step, and the event and protocol reference (open it in a browser) |
| [docs/config.md](docs/config.md) | Every configuration key |
| [docs/ui.md](docs/ui.md) | The UI and UX brief: principles, style, layout |
| [docs/decisions/](docs/decisions/) | Why things are the way they are |
| [CLAUDE.md](CLAUDE.md) | Working agreements, build and test commands |

## Dependencies

| Dependency | Why |
|---|---|
| Apple frameworks (SwiftUI, Swift Charts, AppKit, Foundation, Security, SQLite3, Virtualization, FoundationModels, JavaScriptCore, ServiceManagement) | Everything |
| [modelcontextprotocol/swift-sdk](https://github.com/modelcontextprotocol/swift-sdk) | MCP client |
| [apple/swift-log](https://github.com/apple/swift-log) | The SDK's logging API, which a custom transport has to implement |
| [apple/containerization](https://github.com/apple/containerization) | Sandbox (pinned to an exact version: its API moves between minor versions) |
| [MathJax](https://github.com/mathjax/MathJax) 3.2.2 | Typesetting LaTeX in replies, run in JavaScriptCore and bundled in `App/MathJax` (Apache 2.0; [decision 0019](docs/decisions/0019-latex-with-mathjax.md)) |
| [Literata](https://github.com/googlefonts/literata), [DM Sans](https://github.com/googlefonts/dm-fonts), [iA Writer Mono](https://github.com/iaolo/iA-Fonts) | The reply, interface and code faces, bundled under the SIL Open Font License (licences in `App/Fonts`; decisions [0015](docs/decisions/0015-typography.md), [0018](docs/decisions/0018-literata.md)) |

The sandbox's default image is Kuri's own ([`Sandbox/Dockerfile`](Sandbox/Dockerfile), published to `ghcr.io/haruno19/kuri-sandbox` by a GitHub Actions workflow. It runs inside the VM, not in Kuri: the official `python:3-slim`, plus `poppler-utils`, `pandoc`, `ImageMagick`, `ripgrep`, `jq`, `git` and `sqlite3` from Debian, and `pypdf`, `pdfplumber`, `pandas`, `openpyxl`, `python-docx`, `Pillow` and `matplotlib` from PyPI, so the model can work with PDFs, Office files, images and data locally, without a network.

The inspector's git status runs the host's `git` when one is installed (Homebrew's or the developer tools'); nothing is bundled for it.

The MCP SDK brings in, transitively, `apple/swift-system`, `apple/swift-log` and `mattt/eventsource` (SSE parsing for its HTTP transport); those are what end up linked into Kuri. SwiftPM also fetches `apple/swift-nio` and friends, used only by the SDK's own sample executables.

Containerization is the heavy one: it brings gRPC (`grpc/grpc-swift-2` and friends, to talk to the VM's init process), `SwiftNIO`, `swift-crypto`, `swift-protobuf`, `swift-server/async-http-client` and `facebook/zstd`. 

## Contributing

Kuri means to stay small and essential: bug fixes, performance and usability improvements to what already exists, and specialized sandbox images are welcome; ideas for new features or UI are open to discussion, and forks are encouraged. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Kuri is licensed under the [Apache License 2.0](LICENSE). Bundled fonts and MathJax keep their own licences, listed above.
