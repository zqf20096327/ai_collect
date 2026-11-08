# TradingView MCP

**A comprehensive MCP server for TradingView Desktop.** Create, save, backtest and fine-tune Pine Script strategies entirely from an agent — full chart control, the complete Pine Script lifecycle, complete Strategy Tester extraction, layouts, replay and DOM-driven UI automation, all over Chrome DevTools Protocol.

**No computer vision. No screenshots. Everything is data.**

![MCP](https://img.shields.io/badge/MCP-104_tools-blueviolet)
![TradingView Desktop](https://img.shields.io/badge/TradingView-Desktop_3.4-2962FF)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6)
![Vision](https://img.shields.io/badge/computer_vision-none-critical)
![License](https://img.shields.io/badge/license-MIT-green)

---

**Contents:** [What it is](#what-it-is) · [Quick start](#quick-start) · [How it works with TradingView](#how-it-works-with-tradingview) · [Agent interoperability](#agent-interoperability) · [What you can call & analyze](#what-you-can-call--analyze) · [Showcases](#showcases) · [Safety model](#workspace--safety-model) · [Configuration](#configuration) · [Verified state](#verified-state) · [Limitations](#known-limitations) · [Troubleshooting](#troubleshooting) · [Development](#development) · [Documentation](#documentation) · [Upstream credit](#standing-on-the-shoulders-of-tradesdontlietradingview-mcp)

## What it is

TradingView's desktop app is normally driven by hand: click the editor, paste code in, press buttons, screenshot the tester. TradingView MCP exposes the app's **own internal APIs** (chart widget model, strategy report engine, Pine editor facades, pine-facade REST) through **104 MCP tools**, so an agent can run the entire strategy research loop at machine speed:

- 📝 **Write Pine safely** — load code into the editor, compile it onto the chart, save new scripts and new cloud versions through the app's own save path — with a **protected-script registry**, automatic local backups and post-save verification.
- 📊 **Read backtests in their entirety** — 40+ metrics, *every* trade (entry/exit time + price, run-up, drawdown, commission, account value), the full equity curve and buy&hold — read from the strategy's **internal report model**, not scraped from the screen.
- 🔬 **Fine-tune at speed** — read and override strategy inputs, wait for recomputes, and sweep parameter matrices in one call; every run is appended to a JSONL ledger for reproducible analysis.
- 📈 **Control everything** — symbols, timeframes, chart types, trading sessions (RTH ⇄ ETH), studies, layouts, alerts, watchlists, drawings, replay, panes and tabs.
- 🤖 **Built for agents** — flat JSON results, precise tool contracts, large payloads dumped to files, and an [`AGENTS.md`](AGENTS.md) that teaches any agent to operate it without wrecking your account.
- 🚫 **Zero computer vision** — interactions use internal APIs and the DOM (normalized text matching, React-fiber fallbacks); outputs are structured data. Deterministic, testable, scriptable.

Built for quant researchers, strategy tinkerers and automation folks who'd rather call a tool than click a button.

## Quick start

**Requirements:** Windows with **TradingView Desktop** installed (Microsoft Store/MSIX or classic installer), **Node.js ≥ 20**, and any MCP client (Hermes Agent, Claude Desktop, Cursor, …).

```bash
git clone https://github.com/JostQQ/tradingview-mcp.git
cd tradingview-mcp
npm install
```

*(Or grab `tradingview-mcp-v1.0.0.zip` from [Releases](https://github.com/JostQQ/tradingview-mcp/releases) — it's the same tree, no install needed beyond Node.)*

**Register it with your client:**

```bash
# Hermes Agent
hermes mcp add tvmcp --command node --args "<absolute path to tradingview-mcp>\src\server.js"
```

```jsonc
// Claude Desktop (claude_desktop_config.json) — any MCP client works the same way
{
  "mcpServers": {
    "tvmcp": { "command": "node", "args": ["<absolute path to tradingview-mcp>\\src\\server.js"] }
  }
}
```

**Connect to the app:** start TradingView with the debug port — `TradingView.exe --remote-debugging-port=9222` — or just call `tv_launch` from the agent. Then verify with `tv_health_check` (you'll see your chart's symbol/timeframe back).

**The 60-second loop** (what this MCP exists for):

```
strategy_list                          → strategies on the chart (entity id + linked script id)
pine_set_source {source}               → load new code into the editor (nothing saved yet)
pine_compile                           → apply to the chart (never saves to the cloud)
strategy_get_report                    → all metrics + the exact tested window
strategy_get_trades {write_file: true} → every trade, dumped as JSON to the workspace
strategy_scan {entity_id, variants:[…]}→ sweep parameters; one JSONL ledger entry per run
pine_save_next {script_id}             → publish the buffer as a new version (backed up + verified)
```

## How it works with TradingView

TradingView MCP connects to the **running app** over Chrome DevTools Protocol (`127.0.0.1:9222`) and works in three layers, in order of preference:

1. **The app's internal JavaScript APIs** — chart widget model, the strategy engine's `reportData()`, the Pine editor's dialog/bottom facades.
2. **In-page REST** — cloud script operations (save / new version / rename / delete / versions) run through the app's *own* pine-facade fetch, so cookies, auth and error semantics are exactly what the app itself would do.
3. **The DOM** — only where no API exists (dialogs, menus, toggles), driven by normalized text matching with React-fiber `onClick` fallbacks. TradingView renders doubled labels (`"Add to chartAdd to chart"`); the UI layer normalizes that.

```
┌────────────────────┐   CDP (127.0.0.1:9222)    ┌──────────────────────────────────┐
│  MCP client        │ ◄───────────────────────► │  TradingView Desktop             │
│  (Hermes, Claude,  │         stdio             │  ├─ chart page (TradingViewApi)  │
│   Cursor, any)     │                           │  │    ├─ chart widget model    │
└────────────────────┘                           │  │    ├─ strategy reports      │
        │                                        │  │    ├─ Pine editor facade    │
        ▼                                        │  │    └─ DOM (dialogs / menus) │
  src/server.js ─► core/* ─► connection.js       │  └─ pine-facade REST (in-page)   │
      104 tools       modules     multi-target    └──────────────────────────────────┘
                                                          workspace/  (backups, ledgers, dumps)
```

Because nothing depends on pixels, behavior is **deterministic and rerunnable** — and it works while the window is occluded, minimized or on another desktop.

Deep dive into every internal path used: **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

## Agent interoperability

- **Standard stdio MCP server** — works with Hermes Agent, Claude Desktop, Cursor, or anything speaking the Model Context Protocol. Tool discovery, calls and results follow the standard protocol; a raw handshake + live tool calls are exercised in [`tests/mcp_stdio_test.mjs`](tests/mcp_stdio_test.mjs).
- **Tool contracts, not guesswork** — 104 tools with flat `group_action` names. Every description states what it does, what it touches (chart vs editor vs cloud) and its safety behavior. Full auto-generated reference: **[docs/TOOLS.md](docs/TOOLS.md)**.
- **Result convention** — every call returns flat JSON with `success`; failures come back as `isError` with a human-readable `error`. Anything large (all bars, all trades, equity curves, scans) is written to workspace files via `write_file: true` and referenced by path, so agent context stays small.
- **Safe by default** — `pine_compile` can never click a Save button; cloud writes go through guarded REST paths; a **protected-script registry** (`workspace/protected_scripts.json`) makes `pine_save_next` / `pine_delete` refuse to touch scripts you list there unless explicitly overridden. [`AGENTS.md`](AGENTS.md) ships golden rules, a tool-routing cheat-sheet, standard workflows and a failure playbook so *any* agent behaves well.
- **Escape hatch** — `tv_eval` executes raw JS in the app when you need something exotic.

Example asks that work out of the box:

> “Backtest the strategy on my chart and give me the full report plus every trade.”
> “Sweep Fast EMA from 5 to 21 on the EMA crossover and rank by profit factor.”
> “Check this script for compile errors before we touch the chart.” *(side-effect-free `pine_check`)*
> “Save the current editor buffer as a new version of my strategy and confirm the version bumped.”

## What you can call & analyze

**104 tools in 13 groups.** Complete parameter-level reference: **[docs/TOOLS.md](docs/TOOLS.md)**.

| Group | Tools | Highlights |
|---|---|---|
| Health & launch | 5 | `tv_health_check`, `tv_launch`, `tv_discover`, `tv_ui_state`, `tv_eval` |
| Chart & studies | 17 | symbols, timeframes, chart types, **sessions (RTH⇄ETH)**, zoom, visible range, scroll-to-date, study add/remove, study inputs, symbol search |
| Pine Script | 17 | full lifecycle: `pine_list_scripts`, `pine_open`, `pine_save_new`, `pine_save_next`, `pine_rename`, `pine_delete`, `pine_versions`, `pine_get_version`, plus buffer ops and offline validation |
| Strategy Tester | 8 | `strategy_get_report/trades/equity/inputs`, `strategy_set_inputs`, `strategy_wait`, `strategy_scan`, `strategy_list` |
| Market & study data | 12 | OHLCV (incl. the full loaded history), quotes, study values, Pine lines/labels/tables/boxes, DOM depth |
| Layouts | 7 | list / current / switch / save / rename / delete / create — verified against TradingView's id-lag traps |
| Replay | 6 | start, step, autoplay, trade, stop, status |
| Drawings | 5 | draw, list, remove, clear, properties |
| Alerts | 3 | create, list, delete |
| Watchlist | 4 | get, add, bulk-add, remove |
| Panes & tabs | 9 | pane layout/focus/symbol, tab new/switch/close |
| UI automation | 10 | `ui_find/click/type/key/menu/hover/scroll`, `ui_dialog_scan/click/dismiss` — no vision |
| Batch | 1 | `batch_run`: symbol × timeframe matrices with workspace dumps |

What the backtest tools actually give you:

- **Report** — `netProfit`, `percentProfitable`, `profitFactor`, `sharpeRatio`, `sortinoRatio`, `maxStrategyDrawDown`, `maxStrategyRunUp`, `buyHoldReturn`, `commissionPaid`, `marginCalls`, `maxContractsHeld`, `avgWinTrade` / `avgLosTrade` / `ratioAvgWinAvgLoss`, `grossProfit` / `grossLoss`, trade counts by side, and **the exact tested window** (`dateRange.backtest`).
- **Every trade** — `side`, `entry_time` + price + bar + comment, `exit_time` + price + bar + comment, `qty`, `profit` (+%), cumulative profit, **run-up (MAE)**, **drawdown (MFE)**, `commission`, `account_value`. No panel caps — the full array, streamed to a file if you want.
- **Equity** — per-trade account values, cumulative PnL, drawdown, the buy&hold baseline, initial capital and final equity.

## Showcases

Real captures from the verification suite against TradingView Desktop 3.4.x (throwaway EMA-crossover strategy on MES 1m).

### 1. Idea → applied → full extraction

```
pine_set_source {source: "<EMA crossover strategy>"}   → buffer loaded (not saved)
pine_compile {expect_doc_name: "…"}                    → applied to chart ("Add to chart")
strategy_get_report                                    → full metrics for the new study
strategy_get_trades {write_file: true}                 → 657 trades → workspace/dumps/trades-….json
strategy_get_equity {write_file: true}                 → equity + buy&hold → workspace/dumps/equity-….json
```

`strategy_get_report` excerpt (real numbers from the run):

```json
{
  "success": true,
  "strategy": "TVMCP Smoke 2026-10-10-17-03",
  "entity_id": "pd2PyI",
  "metrics": {
    "netProfit": -1937.5,
    "percentProfitable": 0.2546,
    "profitFactor": 0.8359,
    "sharpeRatio": -0.4354,
    "sortinoRatio": -0.4262,
    "maxStrategyDrawDown": 2215,
    "maxStrategyRunUp": 1030,
    "buyHoldReturn": 830,
    "commissionPaid": 0,
    "totalTrades": 656
  }
}
```

One trade object from the full export:

```json
{
  "n": 1, "side": "long",
  "entry_time_ms": 1790550720000, "entry_price": 7783.25, "entry_bar": 72, "entry_comment": "LONG",
  "exit_time_ms": 1790552100000,  "exit_price": 7782,    "exit_bar": 95, "exit_comment": "SHORT",
  "qty": 2, "profit": -12.5, "cum_profit": -12.5,
  "runup": 20, "drawdown": 20, "commission": 0, "account_value": 77832.5
}
```

### 2. Parameter sweep in one call

```
strategy_scan → {"entity_id":"pd2PyI",
                 "variants":[{"label":"fast_9","overrides":{"in_0":9}},
                             {"label":"fast_15","overrides":{"in_0":15}}],
                 "metrics":["netProfit","profitFactor","totalTrades","maxStrategyDrawDown","percentProfitable"]}
```

Each variant is applied, recomputed and read back — and everything is appended to a per-scan JSONL ledger in `workspace/scans/` so you can close the loop offline:

```json
{
  "entity_id": "pd2PyI",
  "baseline_metrics": {
    "netProfit": -1937.5, "profitFactor": 0.8359, "percentProfitable": 0.2546,
    "maxStrategyDrawDown": 2215, "sharpeRatio": -0.4354, "totalTrades": 656
  },
  "variants": [ … ]
}
```

### 3. The full script lifecycle

```
pine_save_new {name}                 → new cloud script (local backup of previous buffer written first)
pine_save_next {script_id}           → version bumped, verified via the version list
pine_versions {script_id}            → [{"created":"…17:04:08Z","version":"2.0"},
                                       {"created":"…17:03:30Z","version":"1.0"}]
pine_get_version {script_id, version}→ fetch any historical version's source
pine_rename / pine_delete            → guarded (delete requires confirm; protected scripts refuse)
```

## Workspace & safety model

```
workspace/
  protected_scripts.json   # scripts that save/delete refuse to touch without explicit override
  backups/                 # .pine backups written before/after every save + editor snapshots
  dumps/                   # bars, trades, equity, scan summaries, workflow reports
  scans/                   # JSONL ledgers — one line per variant run (the fine-tuning record)
```

- **Compile is save-free by construction** — `pine_compile` only ever drives the *Add to chart* / *Update on chart* buttons (matched by `title` — TradingView renders them icon-only); it can never overwrite a cloud script, and `expect_doc_name` guards against compiling into the wrong document.
- **Verified writes** — every `pine_save_next` re-reads the version list and reports `version_moved`; layout renames verify the active layout name before and after (TradingView's `layoutId()` famously lags after create).
- **Protected scripts** — list your keepers in `workspace/protected_scripts.json`; `pine_save_next`/`pine_delete` refuse them unless you pass `allow_protected: true`, and a local backup is always written regardless.
- **Cleanup** — `node scripts/cleanup_smoke.mjs` removes any test residue and rebinds the champion script from the registry.

Override the workspace location with the `TVMCP_WORKSPACE` environment variable (handy to keep runtime artifacts out of the repo folder entirely).

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `TV_CDP_HOST` / `TV_CDP_PORT` (or `CDP_HOST`/`CDP_PORT`) | `127.0.0.1` / `9222` | CDP endpoint |
| `TVMCP_WORKSPACE` | `<repo>/workspace` | file outputs (dumps, ledgers, backups) |

## Verified state

Live-verified against **TradingView Desktop 3.4.x** (Microsoft Store/MSIX build):

- **104 tools** register and pass a full stdio MCP handshake (`tests/mcp_stdio_test.mjs`).
- **Full 48-step end-to-end workflow: 0 failed** (`tests/live_workflow.mjs`) — create script → bind editor → compile → add to chart → full report / 657-trade export / equity → input tweak → 2-variant scan → save-next version bump → rename → version fetch → symbol/timeframe switches → RTH⇄ETH session switch → zoom — then cleanup that leaves the account byte-identical to its starting state (script count, protected-script version and metrics all verified unchanged).
- Replay, drawings, watchlists, alerts, panes, tabs and layout round-trips exercised separately.
- The engine here reads from the running app itself — numbers above are real outputs from the checks above.

## Known limitations

- **Windows-first.** The launcher has macOS/Linux paths, but live verification (and the MSIX fallback) is Windows-only so far.
- **Account-writing tools are real writes** (`pine_save_*`, `pine_rename`, `pine_delete`, `layout_*`). They are guarded and backed up — read descriptions before calling.
- **Alert/watchlist writes** ride on tested upstream logic but were not re-verified end-to-end in the latest pass; reads are solid.
- **Deep backtesting** (TradingView Premium+ feature) and script *publishing* are not implemented.
- **No screenshot tooling — by design.** Everything is derivable as data; if a human wants a picture, use any screenshot utility.
- **Feed limits are TradingView's**, not ours: available history per symbol/timeframe follows your plan; the workspace receipts always tell you the exact tested window.
- Large responses are dumped to files (`write_file: true`) by design.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `tv_health_check` → connection refused | TradingView isn't running with CDP → `tv_launch {kill_existing: false}`, retry |
| "No TradingView chart target found" | App is up but no chart tab is open |
| `pine_compile` says no button found | Pine editor isn't visible — `pine_open` / `pine_new` first |
| "Bottom editor can be opened only for a specific script." | Editor binding needs a version — `pine_open {script_id}` resolves it |
| Report "not ready" | `strategy_get_report` auto-opens the tester; `strategy_wait` polls for recompute |
| Layout shows a stale name/URL after create/switch | Allow a beat — the tools verify and re-check; a hard navigation normalizes URLs |
| Live tests hang when run in background | Run them **foreground** (background runners can break Node stdio) |

## Development

```
src/server.js        — MCP server + tool registry (buildServer)
src/connection.js    — multi-target CDP client (liveness ping, auto-reconnect)
src/core/*           — feature modules (chart, pine, strategy, layouts, data, ui, replay, …)
src/tools/*          — zod tool registration, one file per group
tests/               — catalog (offline), live smoke, full live workflow, stdio handshake
scripts/             — gen_tools_doc, sync_protected, cleanup_smoke, make_dist
docs/                — TOOLS.md (generated), ARCHITECTURE.md
```

```bash
npm test                        # offline: all 104 tools register, no duplicates
node tests/mcp_stdio_test.mjs   # real MCP handshake + live calls
node tests/live_workflow.mjs    # full live workflow incl. create/cleanup (foreground)
node scripts/gen_tools_doc.mjs  # regenerate docs/TOOLS.md
npm run dist                    # package dist/tradingview-mcp-v<version>.zip (tracked files only)
```

Adding a tool = one module in `src/core/` + one registration file in `src/tools/` + a `register*Tools(server)` line. The invariants (never click Save; guarded writes; auto-recovering connection; ES5-safe page code) are documented in [`AGENTS.md`](AGENTS.md).

## Documentation

- **[docs/TOOLS.md](docs/TOOLS.md)** — auto-generated reference for all 104 tools (parameters, defaults, descriptions)
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — every internal API path, facade and endpoint used, and the safety layer
- **[AGENTS.md](AGENTS.md)** — operating rules for agents: golden rules, routing cheatsheet, workflows, failure playbook
- **[LICENSE-tradingview-mcp-original.txt](LICENSE-tradingview-mcp-original.txt)** — upstream attribution

## Standing on the shoulders of tradesdontlie/tradingview-mcp

This project exists because **[tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** exists.

It is the original CDP bridge between AI agents and the TradingView Desktop app — built in the open, published under MIT, and full of pioneering work this repository relies on every day: the Chrome DevTools Protocol connection layer, the MSIX launch workarounds, the Pine editor toolkit, the doubled-text DOM normalization, and the core philosophy that the app should be driven from code and read as data — never from pixels. Its 6.8k stars and 2.8k forks are thoroughly earned.

**Thank you, tradesdontlie and all twelve contributors — ❤️ genuinely, a lot.** We forked your base (84 tools), kept your tool-naming style, and carry your license with us (`LICENSE-tradingview-mcp-original.txt`). If what you need is chart analysis with Claude Code, [their project](https://github.com/tradesdontlie/tradingview-mcp) is excellent — use it first.

Where this fork went further, for the strategy-research workflow:

| Area | Upstream base (84 tools) | This project (104 tools) |
|---|---|---|
| **Pine script lifecycle** | Editor-centric: open, edit, compile | **Full cloud lifecycle via the app's own pine-facade REST** — save new scripts, publish new versions, rename, delete, full version history, fetch any version's source |
| **Save safety** | Compile could fall back to clicking Save-labeled buttons (in the base we forked) | **Save-free by construction** — only `Add to chart` / `Update on chart` are ever clicked; protected-script registry; local backup before every overwrite; post-save verification (`version_moved`) |
| **Backtest depth** | Reads tied to the selected strategy in the panel | **Per-entity reads of the internal report model** — any strategy by id/name, whatever the panel shows; 40+ metrics, *every* trade (run-up, drawdown, commission, account value), equity + buy&hold, the exact tested window |
| **Fine-tuning** | Manual input tweaks | **`strategy_scan`** — parameter matrices in one call with recompute detection; a JSONL ledger for every run |
| **Sessions** | — | **RTH ⇄ ETH switching** (`chart_set_session`) |
| **Layouts** | list / new / switch | **+ current, headless save, rename, delete, create** — hardened against TradingView's id-lag traps |
| **UI automation** | find / click / type / key / hover / scroll, screenshots | **+ dialogs (scan / click / dismiss) and menus** — and **no screenshots, by design**: structured data only |
| **Safety stack** | — | Protected registry, `workspace/` backups + dumps + scan ledgers, verified destructive ops, cleanup tooling |

The core idea — your agent should never have to drive the app by looking at it — started upstream. We're proud to carry it further.

## Credits & license

Built on the shoulders of [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) — the full thank-you and side-by-side comparison live in the section above.

MIT licensed (see [`LICENSE`](LICENSE)). **Unofficial** — not affiliated with, endorsed by, or
associated with TradingView Inc. You are responsible for using it within TradingView's Terms of Use.
