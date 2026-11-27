# <img src="docs/media/logo.svg" alt="" width="36" height="36" align="top"> Digress

**A branching chat for learning.** Highlight any words in an answer or document, ask about them, and the reply opens in its own thread beside the one it came from. Follow a tangent as far as you like, carry the takeaway back, and pick up right where you left off.

https://github.com/user-attachments/assets/4435b865-4ed3-46e9-b086-07de01d6515c

**[Try the demo](https://digress.neejweej.workers.dev/)** in your browser (nothing to install; pre-written sample replies, or connect your own Google Gemini API key straight from your browser — no Digress backend stores your data) — or run it locally with your Claude, ChatGPT, or Gemini account in 30 seconds.

## Quick start

Needs **Node 22.5+** and at least one model connection (your existing Claude or ChatGPT subscription, or an Anthropic / Gemini API key):

```sh
git clone https://github.com/NeejWeej/digress && cd digress

# connect one or more providers:
npm run chatgpt -- login                     # ChatGPT Plus or Pro plan
claude                                       # Claude Code CLI on your Claude plan (then /exit)
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env  # or an Anthropic API key (or add Anthropic/Gemini keys in-app)

npm start                                    # → http://127.0.0.1:8787
```

Open <http://127.0.0.1:8787>, click **New conversation** or **New from a document**, and ask something.

## Why branch?

Learning something hard is not a straight line. A good explanation raises three new questions, and in a normal chat each tangent pushes the main thread off-screen until you lose it.

Digress keeps them apart. Every question about a passage becomes a **branch** anchored to the exact words it came from. The main thread stays readable, each side question gets a focused answer with full context up to the fork, and the tree shows how ideas connect.

![Digress in Columns view: the main thread on the left, a branch from one of its sentences, and a branch of that branch, whose takeaway has been carried back into its parent](docs/media/columns.png)

## What it does

### Highlight → branch, then carry the takeaway back

![Selecting a phrase in an answer, typing a question, and a new branch opening beside it](docs/media/branching.gif)

- **Branch from any passage:** select text in a reply or document and ask (or pick a quick chip like *Explain simpler*, *Example*, *Why?*, *Go deeper*, *Quiz me*). The model gets the conversation up to the fork plus your highlight—never sibling branches or later main-thread messages.
- **Jump back and forth:** numbered markers mark where each branch starts; **Show in source** flashes the exact words it came from.
- **Takeaways:** click **Takeaway** in a branch to distill 2–4 bullets back into the parent thread so your main discussion builds on what you learned.
- **Non-destructive editing & rewinding:** **Redo**, **Edit**, **Start over**, and **Move what follows into a branch** never overwrite answers—they create another version beside the original so you can compare and switch with **Use this version**.

### Read with PDFs, Markdown & web articles

![A PDF of lecture notes on the left, a summary with page links in the middle, and a branch about one highlighted sentence on the right](docs/media/document.png)

- **Drop in a PDF, Markdown/text file, or URL:** web articles open cleanly in reader view (no scripts run; images wait for your click).
- **Document tools:** documents under ~200k chars (~100 pages) go in whole; longer ones start from the table of contents and first pages, and the model uses `search`, `read_pages`, and `view_page` (read-only, in your browser) to inspect the rest. Citations like `[p. 2]` jump straight to the page.
- **Snips & screenshots:** snip any figure, table, equation, or image in a PDF, Markdown doc, or article—or paste/drop screenshots into any message box.

### Three views: Columns, Rows & Canvas

<img src="docs/media/canvas.png" alt="The same conversation as cards on a canvas in the dark theme, one card expanded to read in place, connected by lines from each highlight to its branch" width="700">

- **Columns** (side-by-side panes with connector wires), **Rows** (full-width stacked panes), and **Canvas** (infinite pan/zoom board with docking, per-card zoom, full-screen reading, and saved views).
- **Focused reading:** collapsible strips, **Collapse others**, **Zen mode** (`⌘.`), reading-mark ribbons, inline LaTeX math, syntax-highlighted code, zoomable Mermaid diagrams, 25+ themes (including blue-free night themes and PDF color modes), and 15+ fonts.

### Remember & organize

- **Optional spaced-repetition flashcards (FSRS):** turn on per conversation to draft cards from highlights, snips, and takeaways into an inbox, review offline, jump back to the exact source sentence, or ask the model to **Fix…** a card ([docs/flashcards.md](docs/flashcards.md)).
- **Search everything (`⌘K`):** typo-tolerant BM25 search across all conversations and documents, plus **Describe it instead** (two-step LLM search when you only half-remember).
- **Folders, prompts & skills:** organize chats into folders (with optional starting system prompts), customize your system prompt and quick chips, load `SKILL.md` skills, inspect **What the model sees**, track learning in **Activity**, sync across devices with automatic 3-way merge, and export/import `.digress`, `.md`, or Anki `.csv`.

For the full walkthrough of every feature, theme, and setting, see the **[Feature guide](docs/guide.md)** (or click **?** beside *How it works* in the sidebar for **Ask about Digress**).

## Models & web search

Connect any combination of providers at the same time (manage API keys in-app via **Connections…** at the bottom of the model picker):

- **ChatGPT (Plus or Pro plan):** `npm run chatgpt -- login` via OpenAI's *Sign in with ChatGPT* (Responses API, `store: false`, counts against your plan).
- **Claude (Pro or Max plan):** uses the [Claude Code](https://docs.claude.com/en/docs/claude-code) CLI with all of its own tools/hooks/config disabled so it answers on your plan.
- **Claude (Anthropic API key):** add in **Connections…** or `ANTHROPIC_API_KEY` in `.env`, with prompt caching.
- **Google Gemini (API key):** add in **Connections…** or `GEMINI_API_KEY` in `.env`.

**Web search is off by default:** toggle **Web** in the top bar for questions that need it. Search runs strictly on the provider's side—no page fetching or local shell/file tools are ever exposed to the model. Each branch keeps its own model and effort, and every reply shows its token usage and prompt-cache hit rate.

## Your data stays on your machine

Digress is a zero-build client (`web/index.html` + `web/styles.css` + native ES modules in `web/js/`) and a zero-dependency Node server (`server/server.mjs`). Conversations and documents live as plain JSON and files in `data/`; the server binds to `127.0.0.1`, has no accounts, refuses cross-origin/DNS-rebinding requests, and blocks auto-loading remote images in model output.

## Keyboard shortcuts

`⌘` on a Mac, `Ctrl` elsewhere (`⌃.` for Zen on iPadOS). Press `?` in Digress for a live, filterable shortcuts panel.

| Keys | What it does |
| --- | --- |
| <kbd>⌘K</kbd> | Search (in search: <kbd>↑</kbd> <kbd>↓</kbd> <kbd>Enter</kbd> open a result, <kbd>⌘Enter</kbd> opens it and keeps searching, <kbd>Tab</kbd> switches everywhere / this conversation / this pane) |
| <kbd>⌘B</kbd> | Show or hide the sidebar (in Zen too, over the panes) |
| <kbd>⌘.</kbd> | Zen |
| <kbd>⌘'</kbd> | Canvas, or back to the panes (Columns or Rows, whichever you had) |
| <kbd>⌘⇧'</kbd> | Switch Columns and Rows |
| <kbd>⌘\\</kbd> | Collapse the pane you're in to a strip, or expand it again (on the canvas: expand or shrink the selected card) |
| <kbd>⌘⇧\\</kbd> | Close the pane you're in; the toast's **Undo** brings it back |
| <kbd>Enter</kbd> / <kbd>⇧Enter</kbd> | Send / a new line |
| <kbd>Esc</kbd> | Close the question box; expand the panes **Collapse others** folded |
| <kbd>?</kbd> | Show or hide the keyboard shortcuts (not while typing) |
| <kbd>Space</kbd> | On the canvas: read the selected card full screen (again or <kbd>Esc</kbd>: back) |
| <kbd>⌘⌥←</kbd> <kbd>⌘⌥→</kbd> <kbd>⌘⌥↑</kbd> <kbd>⌘⌥↓</kbd> | On the canvas: dock the selected card left, right, full screen; undock it |
| <kbd>⌥</kbd> scroll | On the canvas: zoom one card |
| <kbd>Space</kbd> / <kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd> <kbd>4</kbd> / <kbd>S</kbd> / <kbd>O</kbd> / <kbd>E</kbd> / <kbd>F</kbd> | Reviewing flashcards: show the answer / rate it (Again, Hard, Good, Easy) / skip it / open where it came from / edit it / Fix… |
| <kbd>⌘</kbd> click | A conversation in the sidebar: open it in a new window |

## Documentation

- [Feature guide](docs/guide.md) — detailed reference for every feature, theme, view, prompt/skill, and setting.
- [Browser Clipper extension](docs/clipper.md) — clip tweets, selections, and paywalled articles straight into Digress with per-site rules.
- [Setup and configuration](docs/setup.md) — model connections, `.env` options, link fetching, and data layout.
- [Flashcards](docs/flashcards.md) — drafting, inbox, FSRS review, fixing cards, and offline sync.
- [Using it from other devices](docs/remote-access.md) — Tailscale, running as a service, and phone/iPad use.
- [Development](docs/development.md) & [AGENTS.md](AGENTS.md) — tests, live reload, media generation, and architecture notes.
- [Future directions](docs/future.md) & [Done](docs/done.md) — roadmap and completed ideas.

## License

MIT — developed with Claude Opus 5.5.
