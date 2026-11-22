<div align="center">

<img alt="AGY Hyper — Before (151K blind reads & cold cache) vs. With AGY Hyper (live cache meter, inline WAL Diff & 1-click Undo)" src="./assets/hero-bobbycat.png" width="100%">

<br/><br/>

# AGY Hyper

**Local Quota Burn Audit, Live Cache-TTL Cockpit, Inline WAL Undo & Rust MCP Accelerator for Google Antigravity (App & CLI)**

[![CI](https://img.shields.io/github/actions/workflow/status/BobbyCats/agy-hyper/ci.yml?branch=main&style=flat-square&label=CI&logo=githubactions&logoColor=white)](https://github.com/BobbyCats/agy-hyper/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/BobbyCats/agy-hyper?style=flat-square&color=E25B2A&labelColor=1E2022)](https://github.com/BobbyCats/agy-hyper/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-0EA5E9.svg?style=flat-square)](./LICENSE)
[![Antigravity App + CLI](https://img.shields.io/badge/Surface-App_%2B_CLI_(agy)-16A34A.svg?style=flat-square)](#antigravity-cli-agy-support)
[![Rust](https://img.shields.io/badge/Single_Binary-Rust_~4.5MB_tar.gz-111827.svg?style=flat-square&logo=rust&logoColor=white)](#security--transparency)
[![Follow on X](https://img.shields.io/badge/Follow-@BobbyCat2025-000000.svg?style=flat-square&logo=x&logoColor=white)](https://x.com/BobbyCat2025)

**English** · [简体中文](./README.zh-CN.md) · [Quick Install](#install-in-one-line) · [CLI Support](#antigravity-cli-agy-support) · [Analysis Report](./docs/ANALYSIS_REPORT.md) · [Security](#security--transparency) · [Benchmarks](#reproducible-benchmarks) · [Uninstall](#uninstall--preserved-files)

</div>

---

**Find out why your Antigravity quota drains so fast — without giving up native inline diffs.**

Analyzing **80 real local sessions (4,184 turns)** exposed two hidden killers: half of coding sessions load **`151k+` tokens of exploratory file reads before editing a single line**, and each model family's prompt cache drops off a different cliff (**`~90s`** on Carbon, **`~120s`** on Opus, **`~180s`** on Neon/Argon). **AGY Hyper** gives you a 10-second offline burn audit (`agy-hyper audit --png audit.png` / `--svg`), a live sidecar/terminal cache meter, crash-safe BLAKE3 WAL line-level Diff Undo, and layered Rust MCP acceleration (`Observe` / `Safe` / `Balanced` / `Hyper`).

| First-Edit Context Bloat | Empirical Cache TTL Cliffs | Native Diffs Preserved | Local Engine & CLI |
| :---: | :---: | :---: | :---: |
| **`151.4k` P50**<br><sub>`241.3k` P90 · `44.9%` File Reads · [Report](./docs/ANALYSIS_REPORT.md)</sub> | **`90s` / `120s` / `180s`**<br><sub>Carbon / Opus / Neon · `38%` spend uncached</sub> | **`Observe` & `Safe`**<br><sub>Zero native-diff loss · Inline WAL Diff in `Hyper`</sub> | **`0.13ms` UDS RTT**<br><sub>App Sidecar + `agy` CLI (`v1.5.14` verified)</sub> |

<div align="center">
  <img src="./assets/ui-showcase.png" alt="AGY Hyper Deck Live Sidecar, Context X-Ray, Inline WAL Unified Diff, and 10s Local Burn Audit SVG" width="100%"/>
</div>

> **100% Official Antigravity Plugin Protocol**: Built strictly on native MCP, Lifecycle Hooks, Rules, and `SIDECAR_UI_ENTRYPOINT_AUX_PANE` (`agy plugin validate --strict` passes with **0 warnings**). Zero Electron DOM injection, zero `--remote-debugging-port`, zero edits to `~/.gemini/config/config.json`, and 100% offline.

---

## Install in One Line

Start in **zero-intrusion `Observe` mode** (live cockpit, burn audit & passive WAL capture — native tools and inline diff cards untouched) or install the default `Balanced` mode:

```bash
# Recommended first try: zero-intrusion Observe mode (macOS & Linux)
curl -fsSL https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.sh | bash -s -- --observe

# Standard Balanced mode (macOS & Linux)
curl -fsSL https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.sh | bash
```

```powershell
# Windows (PowerShell; set `$env:AGY_HYPER_OBSERVE="1"` first for Observe-only mode)
irm https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.ps1 | iex
```

```bash
# Prefer building from source? (Zero prebuilt binary needed)
git clone https://github.com/BobbyCats/agy-hyper.git && cd agy-hyper && ./install.sh --observe
```

> **Works standalone or alongside `agy-fast`**: Already using `agy-fast` or another MCP accelerator? Keep it — install AGY Hyper in `--observe` mode to run side by side with zero tool-call overlap, while adding live cache-TTL countdowns, 10-second local burn audits, Context X-Ray, and passive WAL file undo.

### Antigravity CLI (`agy`) Support

Verified end-to-end on **`agy v1.5.14`** (`agy plugin validate --strict` passes with 0 warnings; scans `~/.gemini/{antigravity,antigravity-ide,antigravity-cli}/brain/`):

- `install.sh` / `install.ps1` automatically detects `agy` on your `PATH` and runs `agy plugin enable agy-hyper`.
- Attach the `<2ms` live context & cache-TTL status bar to your terminal:
  ```bash
  agy-hyper cli-setup --apply   # writes statusLine & title to ~/.gemini/antigravity-cli/settings.json (backs up first)
  ```
- Open the full visual cockpit (ECharts, Context X-Ray, inline WAL Diff Undo & SVG export) in your browser anytime:
  ```bash
  agy-hyper ui                  # http://127.0.0.1:47821
  ```

### Security & Transparency

We know running any local binary next to your coding workspace requires real trust:

- **Auditable builds**: Every release archive is built in public GitHub Actions (`.github/workflows/release.yml`), paired with `SHA256SUMS` (verified by `install.sh`/`install.ps1` before atomic swap) and GitHub Artifact Attestations. Don't want a prebuilt binary? Clone and run `./install.sh` to compile locally from 100% open-source MIT Rust code.
- **Zero telemetry / zero cloud uploads**: All transcripts, WAL snapshots, usage ledgers, and SVG audit cards stay strictly on disk under `~/.gemini/antigravity/agy-hyper/`.
- **Strict workspace jail, `PLUGIN_ROOT` guard & Secret Shield**: MCP tools cannot escape your workspace root, fail fast if a host spawns MCP inside the plugin install directory / `$HOME` / `/` without passing `workspace`, disable shell execution in `hyper_check` (allowlisted build/test tools only), and shield `.env` / key files by default.

### AI One-Click Install

Paste this prompt into **Antigravity (App or CLI), Claude Code, Codex, or Cursor** to install and verify automatically via [SKILL.md](./SKILL.md):

> Read `https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/SKILL.md` and install AGY Hyper in `--observe` mode using the platform installer (`install.sh` on macOS/Linux or `install.ps1` on Windows), then run `agy-hyper doctor` and `agy-hyper audit` and report the results.

Terminal essentials:

```bash
agy-hyper audit --png audit.png   # 10s local burn audit + shareable 2x Retina PNG (1920x1200, pure Rust)
agy-hyper audit --svg audit.svg   # vector dark/light SVG diagnostic card
agy-hyper doctor                  # verify Tree-sitter grammars, gix, daemon RTT & security posture
agy-hyper tx diff <tx_id>         # inspect line-level unified diff for any WAL snapshot before undo
agy-hyper bench --cache-ttl       # inspect empirical per-model prompt-cache TTL decay curves
agy-hyper usage --window 7d       # view 24h / 7d / 30d / 90d tokens & API-equivalent value
agy-hyper ui                      # launch AGY Hyper Deck standalone at http://127.0.0.1:47821
```

---

## Local Burn Audit Card (`agy-hyper audit`)

Run `agy-hyper audit --days 14 --png audit-card.png` (or `--svg audit-card.svg`) to audit your own Antigravity transcripts 100% locally (zero cloud uploads, zero external Chrome/ImageMagick deps). It surfaces empirical per-model cache TTL cliffs, uncached input spend, pre-edit context bloat, blanket-read turns, and an unadjusted local cohort view in a crisp shareable 2x Retina PNG or vector SVG card:

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/audit-card-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/audit-card-light.svg">
    <img src="./assets/audit-card-dark.svg" alt="AGY Hyper Local Telemetry Burn Audit Card" width="100%"/>
  </picture>
</div>

---

## AGY Hyper Deck (Native Sidecar Cockpit)

Docked directly in Antigravity's auxiliary pane via `SIDECAR_UI_ENTRYPOINT_AUX_PANE`, powered 100% offline by **Apache ECharts 6** and **i18next** (`English / 简体中文 / 日本語`, zero CDN). Luminance-synced with your host Light/Dark theme.

- **Layered Zero-Intrusion Design**: start in **Observe** mode (read-only cockpit + burn audit + passive WAL capture; native tools & diff cards untouched), switch to **Safe** (bundled reads & preset checks while keeping native `edit_file` inline diffs), or unlock **Balanced / Hyper** full Rust MCP acceleration — plus granular per-tool toggles (`MCP Read`, `MCP Edit`, `MCP Check`) under **Engine**.
- **Simple Mode** keeps daily essentials front and center: context level, Turn P50, step vs. session cache hit rate, linked subagent tree strip (highlighting active redlines and `STALLED` subagents silent `>=90s`), session/tree usage ribbon with quick currency switch, **auto-calibrated per-model cache warmth bar** (empirical vs. default TTL badge & loop-guard alerts), 4-mode layered profile switch, and **inline WAL Unified Diff preview + 1-click Undo**.
- **Pro Mode** opens five deep telemetry tabs: **Waterfall** (disjoint LLM vs. Hyper vs. Standard spans), **Context** (dual-axis cached/uncached curve + **Context X-Ray** composition bar with first-edit token load and blanket-read count), **Usage** (`24H / 7D / 30D / 90D` incremental ledger across 8 currencies, manual **Sync FX**, plus **Local Burn Audit & TTL Cliffs** with 1-click **Export PNG** & **SVG** card download), **Engine** (AST/pack cache hits & granular MCP layer switches), and **WAL & Audit**.

<div align="center">
<table>
  <tr>
    <td align="center" width="50%">
      <strong>Simple · Empirical TTL, 4-Mode Switch &amp; Inline WAL Diff (Dark)</strong><br/>
      <sub>~180s empirical TTL · Observe/Safe/Balanced/Hyper · Expandable Unified Diff &amp; 1-click Undo</sub><br/><br/>
      <img src="./assets/cockpit-simple-dark.png" alt="AGY Hyper Deck Simple Dark" width="100%"/>
    </td>
    <td align="center" width="50%">
      <strong>Simple · Clean Light Cockpit &amp; Delta Chips (Light)</strong><br/>
      <sub>Luminance-synced light theme · Empirical warmth bar · Native i18next</sub><br/><br/>
      <img src="./assets/cockpit-simple-light.png" alt="AGY Hyper Deck Simple Light" width="100%"/>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <strong>Pro · Usage Ledger, Burn Audit &amp; Model TTL Cliffs</strong><br/>
      <sub>Multi-currency ledger · Empirical TTL pills · Top findings · 1-click Export Card (.svg)</sub><br/><br/>
      <img src="./assets/cockpit-usage-dark.png" alt="AGY Hyper Deck Usage Ledger and Burn Audit" width="100%"/>
    </td>
    <td align="center" width="50%">
      <strong>Pro · Context Efficiency &amp; Context X-Ray Composition</strong><br/>
      <sub>Dual-axis cached/uncached curve · Post-compact X-Ray · 1st-edit load &amp; blanket-read count</sub><br/><br/>
      <img src="./assets/cockpit-context-dark.png" alt="AGY Hyper Deck Context X-Ray" width="100%"/>
    </td>
  </tr>
</table>
</div>

<details>
<summary><strong>More Views: Pro Turn-by-Turn Execution Waterfall</strong></summary>
<br/>
<div align="center">
  <img src="./assets/cockpit-pro-dark.png" alt="AGY Hyper Deck Pro Waterfall" width="520"/>
</div>
</details>

---

## How It Works

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/mechanics-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/mechanics-light.svg">
  <img alt="AGY Hyper Core Mechanics — Semantic Packing, 3-Phase Atomic WAL, Zero-Trust Sandbox, Adaptive Telemetry" src="./assets/mechanics-dark.svg" width="100%">
</picture>
</div>

<br/>

1. **Single-Pass Semantic Pack (`hyper_pack`)**: One parallel scan combines embedded `ripgrep`, 7 compiled Tree-sitter grammars (Rust, TypeScript/TSX, JavaScript, Python, Go, JSON), multi-language 1-hop import neighbors, `gix` hotspots, and inline source slices for top matches. Payloads stay strictly `<= 8.5KB` so they never spill past Antigravity's 10KB disk threshold; daemon true-LRU hits return in `14ms`.
2. **3-Phase Atomic WAL (`hyper_edit`)**: Acquires an exclusive `flock` with BLAKE3 ETag CAS and BOM/CRLF preservation, `fsync`s pre-image bytes to the WAL journal, then stages temp files and commits via atomic `rename`. On `ENOSPC` or permission errors, temp files are dropped and live files remain untouched. Every commit runs `<1ms` Tree-sitter syntax verification, and `PostToolUse` logs verified native `edit_file` / `write_file` pre-images into the same 1-click Undo ledger.
3. **Compile-Time Zero-Trust Sandbox & Anti-Hang Watchdog**: `gix` is linked with write-ref and network transports compiled out (zero `git` subprocesses). A strict `realpath` jail blocks `../`, symlink escapes, and dangling directory symlinks; Secret Shield blocks `.env`, `*.pem`, `*.key`, and `id_rsa` by default while allowing `.env.example`. `hyper_check` runs with `shell: false`, strips credential env vars, keeps a 64KB head + 512KB tail ring buffer, guards test/script runs with smart silence (`idle_timeout_secs`) and dual-condition fatal-hang (`fail_fast`) watchdogs while exempting compile/static presets from false kills, and kills entire process trees (`setsid` / `taskkill /F /T`) on abort, timeout, or cancellation.
4. **Lock-Free Telemetry, Empirical Cache TTL, Context X-Ray & Antigravity CLI Statusline**: Snapshot polling, CLI `StatuslinePulse`, rollbacks, and incremental byte-offset usage aggregation (`usage_ledger.json` v2, 180-day retention, 8 currencies) run outside the daemon state mutex so concurrent polls never stall MCP calls. Per-model cache decay buckets auto-calibrate each model family's effective cache TTL (`agy-hyper bench --cache-ttl`), single-pass transcript scans break down post-`/compact` context composition (file reads, command output, Hyper tools, thinking/text, media, and first-edit context load), `PreInvocation` arms a consecutive-error `[AGY Hyper Loop Guard]` alongside model-adaptive watermarks (`96k / 115k`, `140k / 175k`, `180k / 280k`), and `agy-hyper statusline` feeds Antigravity CLI's native `statusLine` and plain-text `title` hooks in `<5ms` wall time.

---

## Architecture

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/architecture-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/architecture-light.svg">
  <img alt="AGY Hyper System Architecture" src="./assets/architecture-dark.svg" width="100%">
</picture>
</div>

### Five Focused MCP Tools (`<= 8.5KB` Inline Contract)

Compact tool schemas are pre-inlined in `plugin/rules/AGENTS.md` so the agent invokes them immediately without spending a schema-discovery turn.

| Tool | Mode | Purpose |
| :--- | :---: | :--- |
| `hyper_pack` | `read-only` | Single-pass ripgrep + Tree-sitter AST outlines & matched symbol slices + 1-hop imports + `gix` hotspots + BLAKE3 `etag`s. |
| `hyper_search` | `read-only` | Multi-pattern parallel ripgrep, gitignore-aware file globbing, and zero-subprocess `gix` read-only Git inspection. |
| `hyper_edit` | `atomic WAL` | Multi-file exact or Tree-sitter `symbol` edits with BLAKE3 ETag CAS, BOM/CRLF preservation, WAL journal, and `<1ms` syntax check. |
| `hyper_check` | `sandboxed` | Auto-discovered safe presets (`cargo:check`, `pkg:test`, `py:pytest`, `go:vet`, monorepo scopes) with smart `idle_timeout_secs` & dual-condition `fail_fast` watchdogs, head+tail ring buffer, Tier-2 pre-warm, and `h_xxxx` spill handles. |
| `hyper_tx` | `undo / drill` | List WAL edit ledger, atomically `rollback` any `tx_id`, or `1ms` slice/grep into spilled check handles. |

---

## Reproducible Benchmarks

Measured on Apple Silicon (release LTO build, cold MCP process spawn included) via `./bench/run-bench.sh`; GitHub Actions CI verifies Rust tests, Sidecar JS/i18n/HTML compilation, and release builds on **Ubuntu, macOS, and Windows**:

| Operation | Measured Wall Time | Notes |
| :--- | ---: | :--- |
| Daemon RPC ping (`agy-hyper daemon status`) | **0.12 ms** | Singleton UDS on Unix · token-authenticated loopback TCP on Windows |
| `hyper_pack` (warm Daemon AST + pack cache HIT) | **14 ms** | Full MCP stdio spawn + initialize + response |
| `hyper_search` + `gix` read-only Git (1 call) | **20 ms** | vs **43 ms** baseline `git status && git log && grep -rn` (**2.2x faster**) |
| `hyper_pack` (cold single-pass ripgrep + AST + slices + `gix` + 1-hop) | **58 ms** | Zero external `rg` or `git` binaries |
| `agy-hyper statusline` (warm Daemon pulse + CLI stdin) | **4.2 ms** | Full process exec + lock-free UDS RPC + ANSI/plain-title render (always exits `0`) |
| Full Rust unit & security chaos suite (`53/53`) | **2.1 s** | Covers ENOSPC staging, dangling symlinks, 4-lang 1-hop, WAL rollback, idle/fail-fast watchdog, empirical TTL migration, Context X-Ray, Loop Guard, CLI statusline, pure-Rust 2x PNG audit export, and MCP `PLUGIN_ROOT` fail-fast guard |

Reproduce on your own repository:

```bash
./bench/run-bench.sh /path/to/your/repo
```

<details>
<summary><strong>CLI Reference, Telemetry Methodology &amp; Supply-Chain Discipline</strong></summary>

```bash
agy-hyper doctor                                # Tree-sitter, gix, daemon RTT & security self-check
agy-hyper daemon start|stop|status              # Manage the shared local Rust daemon
agy-hyper ui [--port 47821]                     # Launch AGY Hyper Deck standalone in browser
agy-hyper audit [--days 14] [--sessions 80] [--png card.png] [--svg card.svg] [--theme dark|light] [--json]
agy-hyper usage [--window 24h|7d|30d|90d] [--currency CNY] [--json]
agy-hyper bench [--sessions 10] [--svg waterfall.svg] [--cache-ttl] [--json]
agy-hyper statusline [--format compact|rich|json] [--title] [--no-color]
agy-hyper cli-setup [--apply] [--format compact|rich]  # Print or opt-in apply Antigravity CLI statusLine & title config
agy-hyper tx list                               # Inspect BLAKE3 WAL transaction ledger
agy-hyper tx diff <tx_id> [--json]              # Print line-level Unified Diff for any WAL transaction
agy-hyper tx rollback <tx_id> [--force]         # Atomically restore files to pre-edit bytes
agy-hyper config show                           # Print active configuration
agy-hyper config profile observe|safe|balanced|hyper    # Switch layered cockpit / MCP acceleration mode
agy-hyper config toggle enable_mcp_read|enable_mcp_edit|enable_mcp_check true|false
agy-hyper config currency USD|CNY|JPY|EUR|GBP|HKD|SGD|KRW
agy-hyper config fx <CODE> <RATE_PER_USD>       # Set custom offline FX override
```

- **Ground-Truth Context & Compaction**: reads live `input_tokens + cache_read_tokens` directly from Antigravity's latest `PLANNER_RESPONSE`, resets counters on `/compact`, explains cross-model cache re-warming, excludes user-initiated cancellations, and tags transient network events (`proxy_reset`, `stream_timeout`) explicitly.
- **Honest Usage & Multi-Currency Estimates**: incremental byte-offset scanner aggregates local transcripts into `usage_ledger.json` with zero background network calls. Legacy turns without `model` tags are counted in token totals and excluded from cost (attribution % shown transparently). Currency FX defaults to offline reference rates and only fetches live rates when you click **Sync FX** manually.
- **Honest Paired TPS & Disjoint Waterfalls**: `llm_inference_ms` measures planner start -> first tool dispatch; `tool_exec_ms` measures first tool dispatch -> final tool completion. Excluded idle spans (`>180s`) are removed from both numerator and denominator.
- **Supply-Chain Discipline**: zero silent background self-updates; every release ships with `SHA256SUMS` and Sigstore/Cosign build provenance attestation.

</details>

---

## Uninstall & Preserved Files

Remove AGY Hyper cleanly at any time:

```bash
# macOS & Linux (preserves config, usage ledger & WAL undo snapshots)
curl -fsSL https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.sh | bash -s -- --uninstall

# macOS & Linux (complete purge including runtime state & WAL snapshots)
curl -fsSL https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.sh | bash -s -- --uninstall --purge
```

```powershell
# Windows PowerShell (preserves config, usage ledger & WAL undo snapshots)
$env:AGY_HYPER_UNINSTALL = "1"; irm https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.ps1 | iex

# Windows PowerShell (complete purge)
$env:AGY_HYPER_UNINSTALL = "1"; $env:AGY_HYPER_PURGE = "1"; irm https://raw.githubusercontent.com/BobbyCats/agy-hyper/main/install.ps1 | iex
```

- **Removed**: stops the local Rust daemon and Hyper Deck sidecar, deletes `~/.gemini/config/plugins/agy-hyper`, removes `~/.local/bin/agy-hyper` (Unix) or the plugin `bin` entry from User `PATH` (Windows).
- **Preserved by default**: `~/.gemini/antigravity/agy-hyper/` (`config.json`, `usage_ledger.json`, and `wal/` undo snapshots) so your custom rates and file backups stay safe unless you pass `--purge` (`-Purge`). `~/.gemini/config/config.json` is never modified at install or uninstall.

---

## Author, Contributing & License

Built in public by **BobbyCat** ([`@BobbyCat2025` on X](https://x.com/BobbyCat2025) · [GitHub](https://github.com/BobbyCats)). If AGY Hyper helped you spot a hidden quota drain (or saved a late-night refactor with 1-click WAL Undo), come say hi on X — I share Rust AI tooling, Antigravity workflow breakdowns, and the empirical logs behind them.

<details>
<summary>☕ <strong>Enjoying AGY Hyper? Buy Me a Coffee (WeChat Tip QR)</strong></summary>
<br/>
<div align="center">
  <img src="./assets/wechat-coffee.png" alt="Buy BobbyCat a coffee via WeChat" width="300"/>
</div>
</details>

<br/>

- **MIT Licensed & PRs Welcome**: AGY Hyper is 100% open source under the [MIT License](./LICENSE) — free for personal and commercial use on any work machine. Contributions for additional Tree-sitter grammars, preset runners, translations, and Windows/Linux testing are very welcome; see [CONTRIBUTING.md](./CONTRIBUTING.md).
- **Acknowledgments**: Initial exploration into Antigravity latency optimization was sparked by [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast). Big thanks to the open-source community for pushing AI tooling forward.

---

MIT © [BobbyCats](https://github.com/BobbyCats) & AGY Hyper Contributors.
