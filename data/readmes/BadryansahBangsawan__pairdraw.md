# Pairdraw

[![MIT license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![npm](https://img.shields.io/npm/v/@pairdraw/cli?label=%40pairdraw%2Fcli)](https://www.npmjs.com/package/@pairdraw/cli)

Open-source design editor. Opens `.fig` and `.pen` design files, includes built-in AI, and ships as a programmable toolkit with a headless Vue SDK for building custom editors.

> **Status:** Active development. Usable today, with some rough edges as features evolve.

**[Download](https://github.com/BadryansahBangsawan/pairdraw/releases/latest)** · [Documentation](packages/docs/) · [Roadmap](packages/docs/development/roadmap.md)

![Pairdraw editor: an AI agent designing a five-screen budgeting app on the canvas while the chat explains its work](packages/docs/public/screenshot.png)

## Installation

Download the desktop app for macOS on Apple Silicon (`.dmg` or `.zip`) from the [releases page](https://github.com/BadryansahBangsawan/pairdraw/releases/latest). The build is not signed or notarized yet, so open it the first time with right-click → **Open**. Windows, Linux, and Intel Macs build from source (see [Building from source](packages/docs/getting-started.md#building-from-source)), and the web app runs from a checkout of this repository with `bun install` and `bun run dev` (see [CONTRIBUTING.md](CONTRIBUTING.md)). There is no hosted web app.

Requires macOS 13 or later with current Safari updates, Windows 10 or later, or Linux with WebKitGTK 2.40+; the web app needs Chrome 111, Edge 111, Firefox 128, or Safari 16.4 or later. See [system requirements](packages/docs/getting-started.md#system-requirements).

Pairdraw sends no usage data: no daily ping, analytics, or usage statistics. The [privacy page](packages/docs/overview/privacy.md) lists what the app connects to and when.

## What it does

- **Opens `.fig` and `.pen` files** — read and write native Figma files, open supported Pencil documents from the app or OS file browser, copy & paste nodes between apps
- **AI builds designs** — describe what you want in chat, on Home, or in the prompt at the bottom of the canvas, and 100+ tools create and modify nodes. Bring your own key for the major providers or any compatible endpoint, or let the chat use a coding agent already on your computer
- **Watch the AI draw** — layers an agent adds trace in one after another, the frames it works in shimmer, and a notice counts what it added and changed once it stops; turn it off in Settings ([Watching the assistant draw](packages/docs/programmable/ai-chat.md#watching-the-assistant-draw))
- **Goodies** — styles, design systems, scripts, and shaders to start from, one click from the top bar
- **Built-in browser** — open `http` and `https` pages in a separate desktop window that shares nothing with the editor, import the whole page or one picked element as layers, place a screenshot on the canvas, and let the chat read the page, mark an element, and click, type, or scroll on it with approval
- **Research on a board** — on a board you already have (Pairdraw does not create new ones), quote the page open in the built-in browser as a sticky note that keeps its address, title, quote, and read time ([Research on a board](packages/docs/user-guide/research.md))
- **Fully programmable** — headless CLI, XPath queries, Figma Plugin API plus a `pairdraw` API via `eval`, MCP server for AI agents, and agent integrations for Claude Code, Codex, Gemini CLI, omp, and Pi in the desktop app and, through a local companion, the browser
- **Lint, convert, and extract tokens** — inspect documents, lint naming/layout/accessibility, convert between supported formats, analyze colors/typography/spacing/clusters, and extract design tokens
- **Components and variants** — create reusable components, group variants into component sets, insert local assets as instances, and switch variants from the inspector
- **Working controls** — give a component a Reka UI behaviour (switch, slider, tabs, text field, …) and preview it live over the canvas, with real inputs, focus, and keyboard
- **Script layers** — draw a layer's contents from a JavaScript program stored in the document, with `@input` controls bindable to variables, live re-runs, and one step to convert the result into ordinary layers ([Script layers](packages/docs/user-guide/script-layers.md))
- **Prototypes** — link frames with click or after-delay interactions that navigate, open or close an overlay, or go back, then play them on the canvas with instant or dissolve transitions ([Playing a prototype](packages/docs/user-guide/playing-a-prototype.md))
- **Image vectorization** — convert image layers into editable vector layers with Recraft or fal.ai
- **Design-to-code export** — export selections as JSX/Tailwind, generate token outputs, and map designs into component-oriented code workflows
- **VS Code extension** — open and save `.fig` and `.pen` files in a VS Code custom editor that runs the web editor; it is not published to a marketplace, so build it from the repository ([VS Code extension](packages/docs/programmable/vscode.md))
- **Vue SDK for custom editors** — headless components and composables for embedding Pairdraw into other apps or building workflow-specific editing surfaces. [Read the SDK docs →](packages/docs/programmable/sdk/index.md)
- **Optional Cloud** — keep documents on your team's own [Pairdraw Cloud](packages/docs/user-guide/pairdraw-cloud.md) server, share them by invitation or link, and edit them together with cursors, presence, and follow mode
- **Plugins** — install plugin manifests, run a plugin's command from the command palette on the open document, and grant only the permissions it needs; one plugin runs at a time, and network access is refused ([Plugins](packages/docs/user-guide/plugins.md))
- **Auto layout & CSS Grid** — flex and grid layout via Yoga WASM, with gap, padding, alignment, track sizing
- **Small desktop app** — Tauri v2 for macOS, Windows, and Linux, with a macOS installer of about 20 MB; release builds are published for macOS on Apple Silicon so far. Also runs in the browser as a PWA

## CLI

```sh
npm install -g @pairdraw/cli
# or: bun add -g @pairdraw/cli
```

### Inspect design files

Browse node trees, search by name or type, dig into properties — all without opening the editor:

```sh
pairdraw tree design.fig
pairdraw find design.pen --type TEXT
pairdraw node design.fig --id 1:23
pairdraw info design.fig
```

```
[0] [page] "Getting started" (0:46566)
  [0] [section] "" (0:46567)
    [0] [frame] "Body" (0:46568)
      [0] [frame] "Introduction" (0:46569)
        [0] [frame] "Introduction Card" (0:46570)
          [0] [frame] "Guidance" (0:46571)
```

### Query with XPath

Find nodes by type, attributes, and structure:

```sh
pairdraw query design.fig "//FRAME[@width < 300]"  # Frames under 300px
pairdraw query design.fig "//SECTION//TEXT"        # Text inside sections
```

### Export, convert, and import

Render to PNG, JPG, WEBP, SVG, PDF, PPTX, draw.io, HTML, JSX, Storybook stories, or `.fig`, convert between `.fig`, `.pen`, and draw.io, and turn HTML/CSS into editable layers:

```sh
pairdraw export design.fig                  # PNG
pairdraw export design.fig -f jpg -s 2      # JPG at 2x
pairdraw export design.fig -f tailwind-jsx  # Tailwind JSX
pairdraw export design.fig -f storybook     # Storybook stories per component
pairdraw convert design.pen -o design.fig   # Between document formats (.fig, .pen, .drawio)
pairdraw import card.html --css card.css    # HTML/CSS → editable .fig
```

### Lint and analyze

Catch naming, layout, and accessibility issues, and audit a design system's real palette, type scale, spacing, and repeated components:

```sh
pairdraw lint design.fig --preset strict  # Naming, layout, accessibility
pairdraw analyze colors design.fig        # Also typography, spacing, clusters
pairdraw variables design.fig             # Variables and collections
```

```
#1d1b20  ██████████████████████████████ 17155×
#49454f  ██████████████████████████████ 9814×
#ffffff  ██████████████████████████████ 8620×
#6750a4  ██████████████████████████████ 3967×
```

### Script with the Figma Plugin API

`eval` runs JavaScript against the document with Figma's Plugin API; `-w` writes the result back:

```sh
pairdraw eval design.fig -c "figma.currentPage.selection.forEach(n => n.opacity = 0.5)" -w
```

### Control the running app

Omit the file argument and the CLI works on the document open in the editor:

```sh
pairdraw tree                                 # Inspect the live document
pairdraw documents list                       # Also open, new, save, close, activate
pairdraw tool call get_selection              # Run any MCP tool
pairdraw undo                                 # Undo the newest automation change
pairdraw settings set appearance.theme light  # Change editor settings
```

Every command supports `--json`. See the [CLI reference](packages/docs/reference/cli.md) for all commands and options.

## AI & MCP

### Built-in chat

Press <kbd>⌘</kbd><kbd>J</kbd> (<kbd>Ctrl</kbd><kbd>J</kbd> on Windows and Linux) to open the AI chat in its own column beside the properties panel. It has more than 130 tools that can create shapes, set fills and strokes, manage auto-layout, work with components and variables, run boolean operations, analyze design tokens, and export assets. Bring your own API key for OpenRouter, Anthropic, OpenAI, ChatGPT, Google AI, DeepSeek, Z.ai, MiniMax, xAI, Meta, Kimi For Coding, Moonshot AI, Together AI, Fireworks AI, OpenCode Zen and Go, Amazon Bedrock, Google Vertex AI, or an OpenAI- or Anthropic-compatible endpoint. No backend, no account.

Not every provider works in the browser, and not every model streams tool calls correctly. See [BYOK provider & model compatibility](packages/docs/programmable/byok-provider-compatibility.md) for measured results — contributions welcome.

### Coding agents

Use Claude Code, Codex, Gemini CLI, omp, or Pi as the design agent in the chat panel. It runs with your own subscription and reaches the canvas through the editor's MCP server. The desktop app runs them itself; in the web app, run `npx -p @pairdraw/mcp pairdraw-connect` and open the link it prints so a companion on your computer runs Claude Code, Codex, Gemini CLI, or omp ([Coding agents in the browser](packages/docs/programmable/browser-agents.md)).

When no model is set up, the chat uses Claude Code, Codex, Gemini CLI, or omp if one is already installed, and offers a sign-in or its connector with one button when the agent needs one. In the desktop app, **Connect** installs the agent's adapter and Pairdraw's MCP server, signs the agent in, and checks that it reaches Pairdraw's tools, showing each step; **Retry** continues from a step that failed. Pi runs through the `@pairdraw/harness` companion. See [Coding agents](packages/docs/programmable/coding-agents.md) for each agent's install command.

### MCP server

Connect Claude Code, Cursor, Windsurf, or any MCP client to inspect, modify, and export the document open in the running editor. [Full docs →](packages/docs/programmable/mcp-server.md)

**Stdio** (Claude Code, Cursor, Windsurf):

```sh
npm install -g @pairdraw/mcp
claude mcp add --scope user pairdraw -- pairdraw-mcp
```

For other MCP clients:

```json
{
  "mcpServers": {
    "pairdraw": {
      "command": "pairdraw-mcp"
    }
  }
}
```

**HTTP** (scripts, CI):

```sh
pairdraw-mcp-http   # Unix socket on macOS/Linux + http://127.0.0.1:7600/mcp
```

Set `PAIRDRAW_MCP_ROOT` to limit file access to one directory; it defaults to the current working directory (the home directory on Windows).

### [AI agent skill](skills/pairdraw/SKILL.md)

Teach your AI coding agent to use Pairdraw — inspect designs, export assets, analyze tokens, modify .fig files:

```sh
npx skills add BadryansahBangsawan/pairdraw
```

Works with Claude Code, Cursor, Windsurf, Codex, and any agent that supports [skills](https://skills.sh).

For documentation-aware agents, building the VitePress docs in `packages/docs` generates `llms.txt`, `llms-full.txt`, and per-page Markdown files.

## Collaboration

Pairdraw has no live peer-to-peer rooms: local documents have no Share link, and there is no joining by room link and no voice call. To edit together, keep the document on a [Pairdraw Cloud](packages/docs/user-guide/pairdraw-cloud.md) server your team runs ([self-hosting guide](packages/docs/reference/self-hosting-cloud.md)); everyone who opens it sees each other's cursors and edits live and can follow each other's view. AI agents show their cursors on the canvas in any document.

## Why

Figma is a closed platform that resists programmatic access: its MCP server is read-only, and automation outside the Plugin API breaks when it ships a point release. Your design files are in a proprietary binary format that only its software can fully read.

Pairdraw is the alternative: open source (MIT), local-first, reads .fig files natively, and every operation is scriptable.

See the [roadmap](packages/docs/development/roadmap.md) for product direction and current Figma compatibility gaps.

## Community

- **[Issues](https://github.com/BadryansahBangsawan/pairdraw/issues)** — reproducible bugs, questions, and feature proposals; report security problems through a [private advisory](https://github.com/BadryansahBangsawan/pairdraw/security/advisories/new)

## Contributing

```sh
bun install
bun run dev:portless  # Web editor at https://pairdraw.localhost
bun run tauri dev     # Desktop app (requires Rust)
```

[CONTRIBUTING.md](CONTRIBUTING.md) covers setup, quality gates, pull requests, and commits. [AGENTS.md](AGENTS.md) maps the repository and links the guide inside each package. Desktop builds need [Rust](https://rustup.rs/) and the [Tauri v2 prerequisites](https://v2.tauri.app/start/prerequisites/); run `bun run tauri build`.

### Tech stack

| Layer         | Tech                                               |
| ------------- | -------------------------------------------------- |
| Rendering     | Skia (CanvasKit WASM)                              |
| Layout        | Yoga WASM (flex and CSS Grid, from a Yoga fork)    |
| UI            | Vue 3, Reka UI, Tailwind CSS 4                     |
| File format   | Kiwi binary + Zstd + ZIP                           |
| Collaboration | Yjs (CRDT), synced through a Pairdraw Cloud server |
| Desktop       | Tauri v2                                           |
| AI/MCP        | Vercel AI SDK (multi-provider BYOK), MCP SDK, Hono |

## License

Pairdraw is MIT licensed (see [LICENSE](./LICENSE)), except Pairdraw Cloud, which is licensed under the [Apache License 2.0](./LICENSES/Apache-2.0.txt). [`REUSE.toml`](./REUSE.toml) lists the exact paths.
