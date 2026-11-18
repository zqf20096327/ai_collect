# TextWeb

**A text-grid web renderer for AI agents — see the web without screenshots.**

Instead of taking expensive screenshots and piping them through vision models, TextWeb renders web pages as structured text grids that LLMs can reason about natively. Full JavaScript execution, spatial layout preserved, interactive elements annotated.

📄 [Documentation](https://chrisrobison.github.io/textweb) · 📦 [npm](https://www.npmjs.com/package/textweb) · 🐙 [GitHub](https://github.com/chrisrobison/textweb)

## Why?

| Approach | Size | Requires | Speed | Spatial Layout |
|----------|------|----------|-------|----------------|
| Screenshot + Vision | ~1MB | Vision model ($$$) | Slow | Pixel-level |
| Accessibility Tree | ~5KB | Nothing | Fast | ❌ Lost |
| Raw HTML | ~100KB+ | Nothing | Fast | ❌ Lost |
| **TextWeb** | **~2-5KB** | **Nothing** | **Fast** | **✅ Preserved** |

## Quick Start

```bash
npm install -g textweb
npx playwright install chromium
```

```bash
# Render any page
textweb https://news.ycombinator.com

# Explicitly request grid mode (same as default)
textweb --output grid https://news.ycombinator.com

# Semantic JSON output for agent workflows
textweb --output semantic https://example.com

# Hybrid output (grid + semantic metadata)
textweb --output hybrid https://example.com

# Interactive mode
textweb --interactive https://github.com

# Legacy JSON output (backward compatible)
textweb --json https://example.com
```

## Example Output

```
[0]Hacker News [1]new | [2]past | [3]comments | [4]ask | [5]show | [6]jobs | [7]submit      [8]login

 1. [9]Show HN: TextWeb – text-grid browser for AI agents (github.com)
    142 points by chrisrobison 3 hours ago | [10]89 comments
 2. [11]Why LLMs don't need screenshots to browse the web
    87 points by somebody 5 hours ago | [12]34 comments

[13:______________________] [14 Search]
```

~500 bytes. An LLM can read this, understand the layout, and say "click ref 9" to open the first link. No vision model needed.

## Integration Options

TextWeb works with any AI agent framework. Pick your integration:

### 🔌 MCP Server (Claude Desktop, Cursor, Windsurf, Cline, OpenClaw)

The fastest way to add web browsing to any MCP-compatible client.

```bash
# Install globally
npm install -g textweb

# Or run directly
npx textweb-mcp
```

**Claude Desktop** — add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "textweb": {
      "command": "textweb-mcp"
    }
  }
}
```

**Cursor** — add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "textweb": {
      "command": "textweb-mcp"
    }
  }
}
```

**OpenClaw** — add to `openclaw.json` skills or MCP config.

Then just ask: *"Go to hacker news and find posts about AI"* — the agent uses text grids instead of screenshots.

**New (v0.2.1-style MCP capabilities):**
- `session_id` on every tool call for isolated parallel workflows
- `textweb_storage_save` / `textweb_storage_load` for persistent auth/session state
- `textweb_wait_for` for multi-step async UI transitions
- `textweb_assert_field` for flow guards before submit

### 🛠️ OpenAI / Anthropic Function Calling

Drop-in tool definitions for any function-calling model. See [`tools/tool_definitions.json`](tools/tool_definitions.json).

Pair with the [system prompt](tools/system_prompt.md) to teach the model how to read the grid:

```python
import json

# Load tool definitions
with open("tools/tool_definitions.json") as f:
    textweb_tools = json.load(f)["tools"]

# Load system prompt
with open("tools/system_prompt.md") as f:
    system_prompt = f.read()

# Use with OpenAI
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Go to example.com and click the first link"},
    ],
    tools=textweb_tools,
)
```

### 🦜 LangChain

```python
from tools.langchain import get_textweb_tools

# Start the server first: textweb --serve 3000
tools = get_textweb_tools(base_url="http://localhost:3000")

# Use with any LangChain agent
from langchain.agents import initialize_agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent.run("Find the top story on Hacker News")
```

### 🚢 CrewAI

```python
from tools.crewai import TextWebBrowseTool, TextWebClickTool, TextWebTypeTool

# Start the server first: textweb --serve 3000
researcher = Agent(
    role="Web Researcher",
    tools=[TextWebBrowseTool(), TextWebClickTool(), TextWebTypeTool()],
    llm=llm,
)
```

### 🌐 HTTP API

```bash
# Start the server
textweb --serve 3000

# Navigate
curl -X POST http://localhost:3000/navigate \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com"}'

# Click, type, scroll
curl -X POST http://localhost:3000/click -d '{"ref": 3}'
curl -X POST http://localhost:3000/type -d '{"ref": 7, "text": "hello"}'
curl -X POST http://localhost:3000/scroll -d '{"direction": "down"}'
```

### 📦 Node.js Library

```javascript
const { AgentBrowser } = require('textweb');

const browser = new AgentBrowser({ cols: 120 });
const { view, elements, semantic, meta } = await browser.navigate('https://example.com');

console.log(view);        // The text grid
console.log(elements);    // { 0: { selector, tag, text, href }, ... }
console.log(semantic);    // { mode, url, title, elements: [...] }
console.log(meta.stats);  // { totalElements, interactiveElements, renderMs }

await browser.click(3);              // Click element [3]
await browser.type(7, 'hello');      // Type into element [7]
await browser.scroll('down');        // Scroll down
await browser.waitFor({ selector: '.step-2.active' }); // Wait for next step
await browser.assertField(7, 'hello', { comparator: 'equals' }); // Validate field state
await browser.saveStorageState('/tmp/textweb-state.json');
await browser.loadStorageState('/tmp/textweb-state.json');
await browser.query('nav a');        // Find elements by CSS selector
await browser.screenshot();          // PNG buffer (for debugging)
console.log(browser.getCurrentUrl());// Current page URL
await browser.close();
```

## Grid Conventions

| Element | Rendering | Interaction |
|---------|-----------|-------------|
| Links | `[ref]link text` | `click(ref)` |
| Buttons | `[ref button text]` | `click(ref)` |
| Text inputs | `[ref:placeholder____]` | `type(ref, "text")` |
| Checkboxes | `[ref:X]` / `[ref: ]` | `click(ref)` to toggle |
| Radio buttons | `[ref:●]` / `[ref:○]` | `click(ref)` |
| Dropdowns | `[ref:▼ Selected]` | `select(ref, "value")` |
| File inputs | `[ref:📎 Choose file]` | `upload(ref, "/path")` |
| Headings | `═══ HEADING ═══` | — |
| Separators | `────────────────` | — |
| List items | `• Item text` | — |
| Blocked (occluded) controls | `⟨Accept⟩`, `⟨____⟩`, or plain link text — **no ref** | not clickable right now |

## Output Modes

`textweb <url>` (and every MCP tool) returns **compact-hybrid** by default: a whitespace-collapsed grid followed by a compact legend of the target metadata the grid cannot show.

```
[0]Home                      [1]Pricing               [2]Sign in

══ PRODUCTS ═══════  ══ COMPANY ═════════  ══ SUPPORT ════
[3]Alpha             [4]About us           [5]Help center

--- refs ---
[0] link "Home" href="/home"
[1] link "Pricing" href="/pricing"
[4] link "About us" href="/about" aria-label="About the company"
[6] input[email] placeholder="you@example.com" required
[7] button
```

One legend line per interactive `[ref]`. Redundant attributes are dropped: a button whose text is fully visible is just `[7] button`; a link repeats its text only because it carries an `href`; a form label is omitted when it is already visible in the grid. State (`checked`, `disabled`, `required`, `value`) is always shown.

| Mode | Flag | Output |
|------|------|--------|
| `compact-hybrid` (default) | `--output compact-hybrid` (alias `compact`) | grid + `--- refs ---` legend |
| `grid` | `--output grid` | the bare grid (MCP: `output: "grid"` keeps the legacy response) |
| `semantic` / `hybrid` / `json` | `--output semantic\|hybrid\|json` | structured JSON, unchanged |

## Layout Options

| Option | CLI | MCP | HTTP | Default |
|--------|-----|-----|------|---------|
| Elastic columns | `--compact-grid` / `--no-compact-grid` | `compact_grid` | `compactGrid` | `true` |
| Collapsed gutter width | `--gutter <n>` | — | `gutterWidth` | `2` |
| Modal isolation | `--isolate-modals` / `--no-isolate-modals` | `isolate_modals` | `isolateModals` | `true` |
| Incremental diff | `--diff` | `diff` | `diff` | `false` |

HTTP options may be top-level body fields or inside `body.options`; for `GET /snapshot` use query params (`?diff=true`). Node: `new AgentBrowser({ compactGrid, gutterWidth, isolateModals })`, or per call, `browser.snapshot({ diff: true })`.

### Adaptive column compression

Linear pixel→character projection wastes most of every line on margins and gutters on widescreen layouts. With `compactGrid` (default):

- empty horizontal gutters wider than 2 columns collapse to `gutterWidth` (default 2); the leading margin collapses to 0;
- the column map is **global and monotone**, so left / centre / right placement and multi-column alignment between rows are preserved;
- a vertical gap becomes at most **one** blank row;
- labels are **never clipped** — a label wider than its slot pushes later cells right, using the space that collapsing freed;
- heading rules stop before the next cell on their row, so a row of headings stays aligned over its columns.

`compactGrid: false` gives the strict proportional layout (linear columns, proportional blank rows).

### Modal isolation

An active modal — `<dialog open>`, `[aria-modal="true"]`, a positioned `[role=dialog]`, or a `position:fixed`, high-z-index container covering at least 40% of the viewport — is rendered alone inside a labelled boundary. The inert background is summarised underneath with **no refs**, so an agent cannot attempt an invalid click:

```
=== ACTIVE MODAL "Confirm delete" [refs=0-1] ===
══ CONFIRM DELETE ══

This cannot be undone.

 [0 Cancel] [1 Delete]
=== END MODAL ===
=== BACKGROUND (inactive while modal is open; no refs) ===
══ MAIN PAGE ════════════════════════════════════════
Background link A
⟨Background field⟩
```

Smaller fixed overlays (a cookie banner) are not isolated, but any control one of them is painted over loses its ref (checked with a real hit-test, restricted to fixed / sticky / top-layer blockers so clipped scroll containers are never mistaken for overlays).

### Diff snapshots

With `diff`, each response after the first is a unified diff against the previous snapshot of that session (2 lines of context) plus `+ref` / `-ref` / `~ref` lines for refs added, removed or changed:

```
=== DIFF vs previous snapshot: 3/27 rows changed ===
@@ -2,5 +2,7 @@
  [0 Add item] [1 Remove last] [2:Your name]
 
-Items: 0
+Items: 1
+
+    [3]Item 1
 
 Static line 01
+ref [3] link "Item 1" href="#i1"
```

It falls back to a full snapshot (labelled `[full snapshot: <reason>]`) when there is no previous snapshot, the origin or path changed, layout options or the scroll position changed, 40% or more of the rows changed, or the diff would not be smaller than the full output. In diff sessions refs are **stable** across snapshots of the same page — an element keeps its number, new elements get fresh ones, and a removed number is not recycled — so "added/removed refs" is meaningful. Without `diff`, refs are numbered in reading order exactly as before.

## How It Works

```
┌─────────────────────────────────────────────┐
│  Your Agent (any LLM)                        │
│  "click 3" / "type 7 hello" / "scroll down"  │
├─────────────────────────────────────────────┤
│  TextWeb                                     │
│  Pixel positions → character grid            │
│  Interactive elements get [ref] annotations  │
├─────────────────────────────────────────────┤
│  Headless Chromium (Playwright)              │
│  Full JS/CSS execution                       │
│  getBoundingClientRect() for all elements    │
└─────────────────────────────────────────────┘
```

1. **Real browser** renders the page (full JS, CSS, dynamic content)
2. **Extract** every visible element's position, size, text, and interactivity
3. **Map** pixel coordinates to character grid positions (spatial layout preserved)
4. **Annotate** interactive elements with `[ref]` numbers for agent interaction

## Selector Strategy

TextWeb builds stable CSS selectors for each interactive element, preferring resilient strategies over brittle positional ones:

| Priority | Strategy | Example |
|----------|----------|---------|
| 1 | `#id` | `#email` |
| 2 | `[data-testid]` | `[data-testid="submit-btn"]` |
| 3 | `[aria-label]` | `input[aria-label="Search"]` |
| 4 | `[role]` (if unique) | `[role="navigation"]` |
| 5 | `[name]` | `input[name="email"]` |
| 6 | `a[href]` (if unique) | `a[href="/about"]` |
| 7 | `nth-child` (fallback) | `div > a:nth-child(3)` |

This means selectors survive DOM changes between snapshots — critical for multi-step agent workflows.

## ATS Workflow Examples (Greenhouse / Lever)

For multi-step ATS flows, use a stable `session_id` and combine wait/assert guards:

```javascript
// Keep one session for the whole application
await textweb_navigate({ url: 'https://job-boards.greenhouse.io/acme/jobs/123', session_id: 'apply-acme' });

// Fill + continue
await textweb_type({ ref: 12, text: 'Christopher', session_id: 'apply-acme' });
await textweb_type({ ref: 15, text: 'Robison', session_id: 'apply-acme' });
await textweb_click({ ref: 42, session_id: 'apply-acme', retries: 3, retry_delay_ms: 400 });

// Guard transition
await textweb_wait_for({ selector: '#step-2.active', timeout_ms: 8000, session_id: 'apply-acme', retries: 2 });

// Validate before submit
await textweb_assert_field({ ref: 77, expected: 'San Francisco', comparator: 'includes', session_id: 'apply-acme' });

// Persist auth/session for follow-up flow
await textweb_storage_save({ path: '/tmp/ats-state.json', session_id: 'apply-acme' });
```

Useful session tools:
- `textweb_session_list` → inspect active sessions
- `textweb_session_close` → close one session or all

## App Runtime Prototype

The experimental manifest-driven app shell (LARC) used to live in this repo. It now lives, isolated and marked experimental, in [`packages/app-runtime-prototype/`](packages/app-runtime-prototype/). It is not part of the published `textweb` package.

## Testing

```bash
# Everything, including live-network tests
npm test

# Everything that needs no network (fast)
npm run test:offline

npm run test:layout   # adaptive column compression
npm run test:legend   # compact-hybrid output + legend (CLI, MCP, HTTP)
npm run test:modal    # modal isolation + occlusion
npm run test:diff     # diff snapshots + stable refs
npm run test:output   # CLI output modes and flags
npm run test:form     # form fixture
npm run test:ats      # ATS multi-step fixture
npm run test:live     # example.com, HN, Wikipedia (network)
```

Test fixtures are in `test/fixtures/`. The experimental app runtime has its own tests: `cd packages/app-runtime-prototype && npm test`.

## Design Principles

1. **Text is native to LLMs** — no vision model middleman
2. **Spatial layout matters** — flat element lists lose the "where"
3. **Cheap and fast** — 2-5KB per render vs 1MB+ screenshots
4. **Full web support** — real Chromium runs the JS
5. **Interactive** — reference numbers map to real DOM elements

## License

MIT © [Christopher Robison](https://cdr2.com)
