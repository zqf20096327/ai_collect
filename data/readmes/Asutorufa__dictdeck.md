# DictDeck

<p align="center">
  <img src="./assets/dictdeck.svg" alt="DictDeck" width="128" />
</p>

DictDeck is a self-hosted AI dictionary, translator, and vocabulary flashcard app.
It brings together built-in dictionaries, streaming LLM explanations (OpenAI, Gemini, Vertex AI, Anthropic, Workers AI, and OpenAI Codex OAuth), a Master-Detail vocabulary notebook, tactile review flashcards, a cross-browser extension, a Streamable HTTP MCP server, a Telegram bot, and Cloudflare Workers deployment.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/Asutorufa/dictdeck)

- Cloudflare API token requires `D1` and `Workers AI` permissions.
- Either `d1 database id` or `d1 database name` must be provided.

## Web App

- **Dictionary Desk**: Look up words and sentences across built-in dictionaries (Weblio, コトバンク, Hujiang, Google Translate) or custom LLM providers with live streaming, collapsible thinking notes, language swap, and `⌘K` / `⌘↵` / `⌘S` shortcuts.
- **Vocabulary Workbench**: Master-Detail lexicon browser with a compact index on the left, spacious reading pane on the right, optional **Quiz veil** self-test mode, and keyboard navigation (`↑`/`↓`, `Space`, `R`, `E`).
- **Daily Review Deck**: Multi-card physical flashcard stack with drag gestures, directional stamps, keyboard shortcuts (`Space`, `←`, `→`, `Backspace`), and review progress tracking.
- **Themes & Settings**: Built-in Light / Auto / Dark theme switching, LLM provider management, Telegram integration, and MCP access token management.

![DictDeck Web Demo](./assets/images/editorial/demo.gif)

| Dictionary Desk | Vocabulary Workbench |
| :---: | :---: |
| ![Dictionary Lookup](./assets/images/editorial/home-light-result.png) | ![Vocabulary Master-Detail](./assets/images/editorial/vocabulary-light.png) |

| Daily Review Deck | Dark Mode |
| :---: | :---: |
| ![Daily Review](./assets/images/editorial/flashcard-light.png) | ![Dark Mode](./assets/images/editorial/home-dark.png) |

Local development (includes MSW mock handlers):

```bash
cd web
npm install
npm run dev
```

## Browser Extension

DictDeck includes a browser extension (Chrome, Firefox, and Safari) for translating selected text on any webpage:

- **In-Page Selection Panel**: Floating Shadow DOM lookup card with streaming responses, collapsible thinking notes, quick source/language/prompt-mode switching, one-click save to Words or Grammar, and automatic Light/Dark theme matching.
- **Popup & Options**: Quick connection status, recent lookup history, server authentication with locally encrypted credentials, and default translation settings.

![DictDeck Extension Demo](./assets/images/editorial/ext-demo.gif)

| Selection Panel (Light) | Selection Panel (Dark) |
| :---: | :---: |
| ![Extension Panel Light](./assets/images/editorial/ext-panel-light.png) | ![Extension Panel Dark](./assets/images/editorial/ext-panel-dark.png) |

| Popup (Light) | Popup (Dark) | Options |
| :---: | :---: | :---: |
| ![Popup Light](./assets/images/editorial/ext-popup-light.png) | ![Popup Dark](./assets/images/editorial/ext-popup-dark.png) | ![Options](./assets/images/editorial/ext-options-light.png) |

Local build:

```bash
cd web
npm install
npm run build:extension
```

Build outputs:

- `web/extension-dist/chrome` — unpacked Chrome extension
- `web/extension-dist/firefox` — unpacked Firefox extension
- `web/extension-dist/safari` — generated Safari project
- `web/extension-dist/safari-app` — built Safari macOS app

Notes:

- Safari packaging is built on macOS and requires Xcode / Command Line Tools.
- The Safari app is generated so the extension can be enabled through Safari on macOS.

### CI Artifacts

The GitHub Actions workflow at [`.github/workflows/rust.yaml`](./.github/workflows/rust.yaml) builds and uploads extension artifacts on macOS:

- `dictdeck-extension-chrome.zip`
- `dictdeck-extension-firefox.zip`
- `dictdeck-extension-safari-project.zip`
- `dictdeck-extension-safari-app.zip`

These files are uploaded as workflow artifacts in CI, and the release workflow also includes them in release assets.

## CLI

Build and run:

```bash
cargo build --release
./target/release/hj jc こんにちは
```

Supported commands:

- `jc <word>` — Japanese to Chinese
- `cj <word>` — Chinese to Japanese
- `kr <word>` — Korean <-> Chinese
- `en <word>` — English <-> Chinese
- `weblio <word>` — Weblio
- `ktbk <word>` — コトバンク
- `google <target> <words>` — Google Translate, e.g. `google en こんにちは`

Examples:

```shell
./target/release/hj jc こんにちは
./target/release/hj cj 你好
./target/release/hj kr 안녕하세요
./target/release/hj en hello
./target/release/hj en 你好
./target/release/hj weblio こんにちは
./target/release/hj ktbk 子供
./target/release/hj google ja Hello world!
```

![CLI screenshot](./assets/images/image.png)

## Telegram Bot

Telegram bot, HTTP API, and scheduled reminder jobs run on Cloudflare Workers.

![Telegram bot screenshot](./assets/images/telegram.png)

## Cloudflare Workers

Configure `wrangler.toml` and deploy:

```shell
vim wrangler.toml
# set the production JWT signing secret outside source control
npx wrangler secret put AUTH_SECRET
# build web frontend
cd web && npm install && npm run build && cd ..
# build and deploy worker
cargo install worker-build --version 0.8.6
npx wrangler deploy
```

`wrangler.toml` config example:

```toml
WORKER_NAME="dictdeck" # cloudflare workers name
SCHEDULE="*/20 0-15 * * *" # cron schedule
```

Register Telegram webhook:

```shell
curl https://<workers-url>/tgbot/register
```

### MCP Dictionary Server

The Worker exposes a Streamable HTTP MCP endpoint at `/mcp`. In the web **Settings** page, generate a token with `dictionary:read` and/or `dictionary:write` permission. The plaintext token is shown only once; send it as a Bearer token:

```shell
curl https://<workers-url>/mcp \
  -H 'Authorization: Bearer mcp_...' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

Read access provides `dictionary.search` and `dictionary.get`. Write access adds save, rename, delete, priority, and preview/apply batch-change tools. Set `MCP_ALLOWED_ORIGINS` to a comma-separated origin allowlist when browser-based MCP clients are used.

### Workers CI/CD

If using Cloudflare Workers Git integration, configure the following commands:

Build Command:

```shell
cd web && npm install && npm run build && cd ..
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > rustup.sh
sh rustup.sh -y
export PATH="$HOME/.cargo/bin:$PATH"
cargo install worker-build --version 0.8.6
```

Deploy Command:

```shell
export PATH="$HOME/.cargo/bin:$PATH"
npx wrangler deploy
```
