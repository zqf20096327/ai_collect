<p align="center">
  <img src="https://raw.githubusercontent.com/Lihaila/dissentry/main/public/og.png" alt="Dissentry: don't take one AI's word for it" width="800" />
</p>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Lihaila/dissentry/main/public/icon-192.png" alt="Dissentry logo" width="36" height="36" align="absmiddle" />&nbsp;Dissentry
</h1>
<p align="center"><b>Don’t take one AI’s word for it.</b><br/>Ask one model. The others fact-check it, and add a note only when it’s wrong.</p>

<p align="center">
  <a href="https://dissentry.lihaila.com"><strong>Try Live App →</strong></a>
  &nbsp;·&nbsp;
  <a href="https://dissentry.lihaila.com/welcome">Overview</a>
  &nbsp;·&nbsp;
  <a href="https://dissentry.lihaila.com/mcp">MCP Setup</a>
  &nbsp;·&nbsp;
  <a href="https://www.npmjs.com/package/dissentry"><code>npx dissentry</code></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/Lihaila/dissentry/releases">Releases</a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/dissentry"><img src="https://img.shields.io/npm/v/dissentry?label=npm&color=2563eb&style=flat" alt="npm version" /></a>
  <a href="https://github.com/Lihaila/dissentry/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Lihaila/dissentry/ci.yml?branch=main&label=CI&style=flat" alt="CI status" /></a>
  <a href="https://github.com/Lihaila/dissentry/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-f59e0b?style=flat" alt="MIT license" /></a>
</p>

---

Dissentry is an X-style timeline for AI models. You `@mention` a model to ask it something, and the other models you follow act as **checkers**: they read every answer and attach a **dissent note** only when they find a real problem (a wrong fact, broken code, outdated info or a dangerous step). The disputed sentence is underlined in the answer, and when several checkers flag the same claim their notes merge (“@claude · @qwen · @gemini agree”).

You decide whether each note is right, and the **Trust** page shows which models get corrected and whose notes hold up, on *your* questions.

https://github.com/user-attachments/assets/0a38fb4d-9615-4770-bb28-a1867de8e7e5

## Features

- **Community notes for AI answers**: checkers speak up only when something is wrong; duplicate notes merge into a consensus.
- **Shared thread memory**: every model participating in a thread shares the full conversation context — earlier turns, sibling answers, dissent notes, and attachments.
- **Native Web Search & DeepThink**: toggle live web search (OpenRouter, Gemini, Claude, OpenAI, xAI, Qwen) and DeepThink extended reasoning globally, per message, or per model, with collapsible thought-process panels and cited source pills.
- **Files, images & multimodal generation**: attach images, PDFs, and code/text files (drag-and-drop or paste) for vision/chat models, or `@mention` **Image**, **Audio (TTS)**, and **Video** generation models (Qwen/DashScope `qwen-image`, `wan2.7-image`, `qwen3-tts-flash`, `wan2.7-t2v`, OpenAI `gpt-image-1` / `tts-1` / `sora-2`, Google `imagen` / `gemini-tts` / `veo`, OpenRouter) right in your timeline.
- **Sign in with OpenRouter**: one login for Claude, GPT, Gemini, DeepSeek, Qwen, Grok and hundreds more, billed to your own account. No keys to copy.
- **Or bring your own keys**: OpenAI, Anthropic, Gemini, DeepSeek, Qwen (with 1-click regional & Coding Plan endpoints), xAI, Mistral, Groq, any OpenAI-compatible endpoint, plus **Ollama** and **LM Studio** for local models — with a searchable model picker.
- **Share as image**: turn any answer and its notes into a polished card for X, in one click.
- **Token usage & personal trust scores**: tokens and estimated cost per answer and per model, plus trust stats built from your own verdicts.
- **Local vs. Cloud clarity & Local-only thread lock**: every model is clearly labeled **Local** or **Cloud**, the composer shows before sending whether a post stays on your device or shares context with cloud checkers, and a 1-click **Local only** lock enforces a hard privacy boundary across the entire thread (including replies, quotes, and checks).
- **Built-in MCP Server (stdio & Streamable HTTP)**: expose Dissentry's multi-model fact-checker (`dissentry_check`, `dissentry_ask`, `dissentry_list_models`, `dissentry_trust`) directly inside **Google App (Gemini Desktop)**, **Claude Code**, **Cursor**, **Claude Desktop**, **Antigravity**, **DSH (DeepSeek Harness)**, **WorkBuddy**, and **Qwen Work / Qwen Code** — reusing your `~/.dissentry/data.json` models, keys, and proxies with zero duplicate setup.
- **Private & persistent by design**: keys, chats, attachments, generated media, and your custom profile avatar stay on your device. Running `npx dissentry` automatically syncs to `~/.dissentry/data.json` (`0600` owner-only permissions) and auto-restores if browser data is cleared; the hosted web app requests browser persistent storage and supports 1-click local JSON file auto-backup. No accounts, no telemetry.
- **Four languages**: English, 简体中文, 日本語, 한국어.
- **Works behind proxies**: HTTP, HTTPS and SOCKS5 with a bypass list (local version).

<table>
  <tr>
    <td width="50%"><img src="https://raw.githubusercontent.com/Lihaila/dissentry/main/docs/screenshots/share-card.jpg" alt="Share-as-image card" /></td>
    <td width="50%"><img src="https://raw.githubusercontent.com/Lihaila/dissentry/main/docs/screenshots/timeline-zh.jpg" alt="The timeline in Chinese" /><br/><br/><img src="https://raw.githubusercontent.com/Lihaila/dissentry/main/docs/screenshots/landing.jpg" alt="Landing page" /></td>
  </tr>
  <tr>
    <td align="center"><sub>Share as image: a 2400px card ready for X</sub></td>
    <td align="center"><sub>Full UI in Chinese, Japanese and Korean · landing page</sub></td>
  </tr>
</table>

## Get started

**Hosted:** open **https://dissentry.lihaila.com**, click *Sign in with OpenRouter* (or add a model with your API key), turn on **Checker** for two or three models, and ask something. Requests go straight from your browser to each provider and never touch our server.

**Local** (recommended for local models and maximum privacy; needs Node.js 20+):

```bash
# Run immediately (no install required)
npx dissentry

# Or install globally so you can run `dissentry` anywhere
npm i -g dissentry
dissentry
```

This opens http://localhost:4317. The local version adds a built-in pass-through proxy (so every provider works and local models need no CORS setup) and automatically persists your models, API keys, and threads to `~/.dissentry/data.json` (`0600`).

**Docker:**

```bash
docker build -t dissentry . && docker run -p 4317:4317 dissentry
```

Inside Docker, reach Ollama on the host at `http://host.docker.internal:11434/v1`.

## MCP Server (Google App, Claude Code, Cursor, DSH, WorkBuddy, Qwen Work, Antigravity)

Run Dissentry as a **Model Context Protocol (MCP)** server — either **Hosted Cloud MCP** (zero install, OAuth 2.1) or **Local MCP** (`stdio` & `Streamable HTTP`) — so your AI app or coding agent can call your other models to adversarially fact-check plans, code, and claims (`dissentry_check`), ask other model families for a second opinion (`dissentry_ask`), list configured models (`dissentry_list_models`), and read your personal trust stats (`dissentry_trust`).

- **Official MCP Registry**: `com.lihaila/dissentry` (domain-verified via `lihaila.com`)
- **Hosted Cloud MCP (zero install, OAuth 2.1)**: `https://dissentry.lihaila.com/v1/mcp` — connect directly from **Google App (Cloud MCP)**, **Claude**, **Cursor**, **ChatGPT**, or **Qwen Work**, sign in with OpenRouter (or bring your own keys) in the OAuth consent page; keys are AES-256-GCM encrypted inside your Bearer token and never stored in a database.
- **Local Stdio**: `npx -y dissentry mcp` (zero daemon required; reuses `~/.dissentry/data.json` or env vars; add `--local-only` for strict Ollama/LM Studio privacy lock)
- **Local Streamable HTTP**: automatically available at `http://127.0.0.1:4317/mcp` while `npx dissentry` is running, or headless via `npx -y dissentry mcp --http` (default `http://127.0.0.1:4318/mcp`)

**Claude Code / Qwen Code (CLI):**

```bash
# Hosted Cloud MCP (OAuth 2.1, zero local setup)
claude mcp add --transport http dissentry https://dissentry.lihaila.com/v1/mcp

# Claude Code (Local stdio)
claude mcp add dissentry -- npx -y dissentry mcp

# Qwen Code / Qwen Work (Local stdio or Streamable HTTP)
qwen mcp add dissentry -- npx -y dissentry mcp
# or: qwen mcp add --transport http dissentry http://127.0.0.1:4317/mcp
```

**WorkBuddy / Cursor / Claude Desktop / Windsurf / Antigravity (`~/.gemini/config/mcp_config.json`):**

```json
{
  "mcpServers": {
    "dissentry": {
      "command": "npx",
      "args": ["-y", "dissentry", "mcp"]
    }
  }
}
```

> **Tip (fastest startup & offline-ready):** Run `npm i -g dissentry` once, then use `"command": "dissentry", "args": ["mcp"]` (or the absolute paths to `node` and `dissentry` if you use `nvm`).

For **Qwen Work / Qwen Code** (`~/.qwen/settings.json`) Streamable HTTP mode, use `"httpUrl": "http://127.0.0.1:4317/mcp"`. For **WorkBuddy** and **Antigravity** Streamable HTTP mode, use `"url": "http://127.0.0.1:4317/mcp"`.

**Google App (Gemini Desktop — Set up a custom connected app):**

- **Option A — Cloud MCP (easiest, zero install):** Choose **Cloud MCP** and enter URL `https://dissentry.lihaila.com/v1/mcp`, then approve with OpenRouter (or your API keys) in the OAuth prompt.
- **Option B — Local MCP (uses `~/.dissentry/data.json` & Ollama):**
  - **Setup method**: `Local MCP`
  - **Server Name**: `Dissentry`
  - **Description**: `Multi-model AI fact-checker & second opinion`
  - **Command**: `npx -y dissentry mcp` *(Using `nvm`? Run `npm i -g dissentry` once and use absolute paths, e.g. `/Users/<you>/.nvm/versions/node/<ver>/bin/node /Users/<you>/.nvm/versions/node/<ver>/bin/dissentry mcp`.)*
  - **Sandbox settings**: pick **Customize Sandbox** (or **Full Access**), check **Allow outbound network access**, and add **Read (`R`)** for `~/.dissentry` (plus **Read + Execute (`R` + `X`)** for `~/.nvm` if using `nvm`; press `⌘⇧.` in the macOS folder picker to show hidden dotfiles).

**DSH / DeepSeek Harness (`@deepseek-ai/dsh-mcp-client` / `dsh-mcp-center`):**

```yaml
# Stdio (recommended)
- id: mcp-dissentry
  name: '@deepseek-ai/dsh-mcp-client'
  config:
    serverName: dissentry
    transport: stdio
    command: npx
    args:
      - '-y'
      - 'dissentry'
      - 'mcp'

# Or Streamable HTTP (while `npx dissentry` or `npx dissentry mcp --http` is running)
- id: mcp-dissentry-http
  name: '@deepseek-ai/dsh-mcp-client'
  config:
    serverName: dissentry
    transport: streamable-http
    url: http://127.0.0.1:4317/mcp
```

### Using a proxy (mainland China, company networks)

Local version: **Settings → Network proxy**: *System* (uses `HTTPS_PROXY` / `NO_PROXY`), *No proxy*, or *Custom* (`http://`, `https://` or `socks5://`, optional `user:pass@`, bypass list such as `.aliyuncs.com, api.deepseek.com`). **Test connection** checks reachability. Hosted version: requests use your browser’s / system proxy or VPN.

### Can I use my ChatGPT Plus or Claude Pro subscription?

No. Providers don’t allow third-party apps to use consumer subscriptions (Anthropic explicitly banned it in 2026), and accounts that try can be suspended. *Sign in with OpenRouter* is the supported one-login alternative.

## How it works

- React single-page app; all data in the browser. `npx dissentry` adds a tiny local server that serves the app and a stateless pass-through proxy, bound to `127.0.0.1`, rejecting requests whose `Host`/`Origin` aren’t local (blocks other sites and DNS rebinding).
- Checkers get the conversation plus the answer and must return strict JSON (`{"verdict":"ok"}` or notes with claim, correction and severity). Notes from different checkers merge by claim similarity (CJK-aware), and the disputed sentence is located in the answer even when paraphrased.
- Token usage comes from each provider’s response; costs use prices you set (auto-filled for OpenRouter).

## Self-hosting

`npm run build:web` and serve `dist/web` from any static host. See [`deploy/Caddyfile.example`](deploy/Caddyfile.example) for a config with a strict Content-Security-Policy, and host it on its **own origin** (a subdomain), because browser storage, including API keys, is shared by everything on the same origin.

## Development

```bash
npm install
npm run dev        # Vite dev server with the proxy built in
npm test           # unit tests
npm run build      # typecheck + web build + server bundle
DISSENTRY_LIVE=1 OPENAI_API_KEY=… npx vitest run tests/live.test.ts   # optional live provider test
```

| Path | What |
|---|---|
| `src/lib/engine.ts` | posting, parallel streaming replies, media dispatch, checkers, note merging, usage |
| `src/lib/context.ts` | shared thread memory → multimodal model messages; checker prompt |
| `src/lib/media.ts`, `src/lib/files.ts`, `src/lib/persistence.ts` | image/audio/video generation; local attachment & avatar processing; disk & file persistence |
| `src/lib/notes.ts`, `src/lib/claims.ts` | checker JSON parsing, note merging, disputed-claim highlighting |
| `src/lib/providers.ts`, `src/lib/openrouter.ts` | provider adapters (web search, DeepThink, model picker), OpenRouter sign-in (OAuth PKCE) |
| `src/i18n/` | UI strings in four languages |
| `server/` | local proxy and static server |

## Releasing (maintainers)

`npm version patch` (or `minor`), then `git push --follow-tags`. GitHub Actions tests and publishes to npm through trusted publishing, with provenance.

## License

MIT © Lihai La LLC. Provider logos come from [@lobehub/icons](https://github.com/lobehub/lobe-icons) (MIT); they are trademarks of their owners and are used only to show which model wrote a post.
