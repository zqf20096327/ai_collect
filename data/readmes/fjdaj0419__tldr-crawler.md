# TL;DR Crawler

**English** · [简体中文](README.zh-CN.md)

> A spider that crawls across the page as you read, highlights the key sentences, and weaves them into a TL;DR web with AI.

[![version](https://img.shields.io/badge/version-2.5.0-brightgreen.svg)](manifest.json)
[![CI](https://github.com/fjdaj0419/tldr-crawler/actions/workflows/ci.yml/badge.svg)](https://github.com/fjdaj0419/tldr-crawler/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/fjdaj0419/tldr-crawler?label=release)](https://github.com/fjdaj0419/tldr-crawler/releases/latest)
[![Chrome MV3](https://img.shields.io/badge/Chrome-MV3-4285F4.svg)](https://developer.chrome.com/docs/extensions/develop)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A Chrome extension written in plain JavaScript with **zero third-party dependencies**. Click the toolbar icon and a spider starts crawling across the page from your cursor, highlighting key sentences one by one. Those sentences are handed to an LLM (DeepSeek or Claude), condensed into short Chinese takeaways, and attached in real time to a spider-web map that grows as you read. Click any node on the web to expand the original sentence or jump straight to it. The map also layers itself: the model reads the whole article and groups it into blocks and topics, so a mail with two seminar talks reads as two blocks instead of one flat heap of points.

> **Note:** the extension UI and all AI-generated text are in Simplified Chinese.

## Preview

**Crawling, highlighting, and the TL;DR panel**

![Extension in action](screenshots/preview.png)

**The spider-web map**

Takeaways are not a flat list. They are grouped into branches by meaning and connected with white silk; colour appears only on the tips of the nodes and encodes *how* a sentence speaks (conclusion, data, quote, …).

![Spider-web map concept](screenshots/web-map-concept.png)

**The spider itself** — redrawn as vectors from a reference image, with procedural IK legs

![Spider build comparison](screenshots/spider-compare.png)

## Features

- 🕷️ **Cursor-following spider** — canvas-drawn, procedural IK legs, metallic silver finish. Hovering a key sentence highlights it on the page.
- 🕸️ **Living spider web** — each batch of AI results grows new nodes. White silk skeleton, colour only on the tips, denser decoration silk when the web is empty. A progressive weaving animation draws the silk outward and pops the capsules in.
- 🪜 **Layered web** — the LLM reads the whole article and groups it into **blocks → topics → sentences**, naming each level from the content itself (no hard-coded categories, proper nouns kept in the original language). Two levels are shown at a time: click a topic capsule to drill into a focused view at normal width, or to grow the next layer in place in the enlarged view. An invitation mail with two talks ends up as two blocks instead of a flat pile of points.
- 🧭 **Three-tier structure fallback** — AI grouping is used when available, HTML `h2`–`h4` headings when not, and a flat web as the last resort. A failed grouping call never empties the web.
- 💬 **Keyword flight** — when the AI returns an item, a 2–6 character keyword travels along a Bézier silk thread from the source sentence to its capsule, rests above it for a moment, then fades out. If the model omits the keyword, a regex extractor takes over.
- 📖 **Plain-language summary** — click the hub to have the captured sentences retold as one plain Chinese paragraph. Generated on demand and cached for the session.
- 🧠 **Dual engines** — DeepSeek or Anthropic Claude, switchable in the options page with a built-in connection test.
- 📌 **Node detail card** — click a capsule to see its type, branch, short summary and the full source sentence; locate or copy it in one click.
- 🌫️ **Hover transparency** — while the pointer is over the panel, the backdrop and the silk fade to a translucent state so you can read the page underneath. Buttons and lists stay fully opaque.
- 🩺 **Honest failures** — if the AI call fails, the empty web prints the actual reason (invalid key, insufficient balance, malformed response, missing structured data) instead of spinning forever.
- 📄 **Broad page support** — beyond `p` / `li` / `blockquote`, a leaf-`div` fallback lets it read mail clients, docs and admin pages whose text lives entirely in `div` / `section` / `td`.
- ⚡ **Pure vanilla** — Manifest V3, no build step, no libraries, Shadow DOM isolation so the host page is never polluted.
- 🔍 **Fallback list** — a collapsible list keeps every captured sentence with a local summary, readable even without an API key.

## Install

### From a release (no git required)

1. Download `tldr-crawler-vX.Y.Z.zip` from [Releases](https://github.com/fjdaj0419/tldr-crawler/releases/latest).
2. Unzip it to a folder you will keep (Chrome loads the extension from disk on every start).
3. Open `chrome://extensions`, turn on **Developer mode**, click **Load unpacked** and select that folder.

### From source (developer mode)

1. Clone the repository:
   ```bash
   git clone https://github.com/fjdaj0419/tldr-crawler.git
   ```
2. Open `chrome://extensions` in Chrome.
3. Turn on **Developer mode** (top right).
4. Click **Load unpacked** and select the repository root (the folder containing `manifest.json`).
5. The spider icon appears in the toolbar. Click it to start or stop.

> ⚠️ Do not put files or folders starting with `_` in the extension root — Chrome reserves that prefix (e.g. `_locales`) and will refuse to load the extension.

## Usage

1. (Optional) Open the extension options from the toolbar menu, paste an API key, pick an engine and test the connection.
2. Open any long article and move the cursor. The spider crawls toward key sentences and highlights them in gold.
3. The panel tracks `found / total` in real time; takeaways are attached to the web as the AI responds.
4. Hover a web node to highlight its source sentence; click to open the detail card. Capsules marked with **›** are topic branches — click one to drill into the next layer (at normal width) or grow it in place (in the enlarged view). Use **⤢** to enlarge the web and see up to 50 nodes.
5. Click the hub (the centre label) to expand the plain-language summary. Move the pointer over the panel to make it translucent.

### Configure an API key

The extension supports two providers; pick one in the options page.

| Engine | Fields | Notes |
|---|---|---|
| DeepSeek | `DeepSeek API Key` + model | Defaults to `deepseek-flash`, `deepseek-v4-pro` also available |
| Claude | `Anthropic API Key` + model | Uses the official Anthropic API |

No key is required to use the crawler: the spider still crawls and highlights, and the list keeps local summaries. Only the web stays empty — the AI is intentionally the sole data source for it.

## Project structure

```text
tldr-crawler/
├── manifest.json        # MV3 manifest (name, permissions, entry points)
├── content.js           # Everything in the page: spider / highlighting / panel / web map / interaction
├── background.js        # Service worker: API proxy, batching, structured parsing
├── options.html / .js   # Options page: engine switch, key management, connection test
├── icon16|48|128.png    # Toolbar and extension icons
├── spider-body.png      # Spider body asset (drawing reference)
├── screenshots/         # README images
├── CHANGELOG.md         # Full version history
├── .github/             # CI workflow, issue / PR templates, repository checks
└── LICENSE / CONTRIBUTING.md / .gitignore
```

## How it works

```text
discover → queueApi (batch of 12, 800 ms debounce) → background.summarizeBatch
        → parseStructured { topic, items[id, short, kw, branch, type], links }
        → attach to sentences → paintWeb → renderWebMap (radial layout)
        → spawnKeywords (fly new keywords into their capsules)

(3 s after the last batch) background.structureArticle
        → parseStructure { topic, blocks[name, topics[name, ids]] }
        → attach s.struct = { block, topic } → rebuildWeb (layered tree)
```

- The scanner collects text blocks (`p`, `li`, `blockquote`, `h2`–`h4`), and falls back to leaf `div` / `section` / `td` elements when it finds fewer than three standard blocks.
- Sentences are split with DOM `Range`s, scored, and the top ~25% become key sentences.
- Short label lines that fall under the 12-character sentence threshold (`Talk 1:`, `Abstract:`, `Speaker:`) are kept as a separate `hint` field on the next block, so the grouping call still sees the sectioning signal without disturbing the `Range` used for highlighting.
- The spider discovers a sentence by physically walking over it; discovery highlights it, adds it to the list and queues it for the model.
- Grouping runs once per session, three seconds after crawling goes idle. Its output takes priority over HTML headings; if it fails, the web silently falls back instead of emptying.
- Structured parsing tolerates string numbers, re-numbered ids, ```` ```json ```` fences and common JSON mistakes (trailing commas, curly quotes, unquoted values).

## Development

There is no build step. Edit the sources, then click the reload button ↻ for the extension on `chrome://extensions`. The panel header shows the running version — use it to confirm you are not testing an old build.

The JavaScript uses no third-party libraries. Visual and interaction details are documented in `screenshots/web-map-concept.png`.

## Troubleshooting

| Symptom | Meaning |
|---|---|
| Panel shows `0 / 0` and an empty list | The page had no scannable text. Most often the content lives inside an `iframe`, which a content script cannot reach. |
| Count is above zero but the web stays empty | The AI call failed. The empty web now prints the reason (e.g. invalid key, balance, malformed response). |
| Panel shows an old version after updating | Reload the extension, then reload the page. If the version still does not change, remove the extension and load it again. |

## Changelog

The complete history lives in [CHANGELOG.md](CHANGELOG.md). Recent highlights:

- **v2.5.0** — AI-driven hierarchy: once crawling goes idle, the whole article goes to the model, which groups it into blocks → topics → sentences with names of its own making (no hard-coded categories, proper nouns kept). Short label lines such as `Talk 1:` are preserved as hints so tag-structured mail stops losing its sectioning. Branch limits widened (24 points at normal width, up to 12 branches).
- **v2.4.0** — layered web: first level from HTML `h2` headings, second from AI topic branches, sentences folded into the branch's `kids`. Drill-in focuses at normal width, in-place growth in the enlarged view.
- **v2.3.6** — page support: fall back to leaf `div` / `section` / `td` when a page has no standard text blocks (mail clients, docs, admin panels).

Everything before v2.3.6 — keyword flight, plain-language summary, hover transparency, detail cards, the original web map — is listed in [CHANGELOG.md](CHANGELOG.md).

## Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 fjdaj0419
