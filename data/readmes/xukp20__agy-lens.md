<p align="center">
  <img src="assets/logo.svg" width="88" alt="AGY Lens Logo" />
</p>

<h1 align="center">AGY Lens</h1>

<p align="center">
  <strong>Local-first, strictly read-only telemetry sidecar for Antigravity Desktop &amp; CLI.</strong><br />
  Live context composition, prompt cache diagnostics, cross-session cache-miss observatory, long-context API-equivalent cost analytics, 16-week usage heatmap, and 2-decimal manual quota alignment.
</p>

<p align="center">
  <strong>English</strong> | <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Antigravity_Sidecar-2.22%2B-5b9cf6?style=flat-square" alt="Antigravity Sidecar 2.22+" />
  <img src="https://img.shields.io/badge/Node.js-24%2B_Zero_Deps-4eb88e?style=flat-square" alt="Node.js 24+ Zero Deps" />
  <img src="https://img.shields.io/badge/Telemetry-100%25_Local_%26_Read--Only-2e8540?style=flat-square" alt="100% Local & Read-Only" />
  <img src="https://img.shields.io/badge/Theme-Auto_Dark_%26_Light-7a5ec4?style=flat-square" alt="Auto Dark & Light Theme" />
  <img src="https://img.shields.io/badge/License-MIT-646b78?style=flat-square" alt="MIT License" />
</p>

<p align="center">
  <img src="assets/screenshots/hero-dual-theme.png" alt="AGY Lens Dual-Theme Auxiliary Pane Preview (Dark and Light Mode)" width="100%" />
</p>

---

## Why AGY Lens?

Many community usage extensions probe undocumented internal RPC endpoints, inspect OAuth tokens, or run background OS daemons that poll continuously even when hidden. **AGY Lens** takes the opposite approach:

- **Strictly Local & Read-Only**: Opens Antigravity Desktop (`~/.gemini/antigravity/conversations/*.db`) and CLI (`~/.gemini/antigravity-cli/conversations/*.db`) SQLite databases exclusively with `{ readOnly: true }`, parsing Protobuf step blobs directly in pure Node.js 24 (`node:sqlite`, zero npm dependencies).
- **Zero RPC Scraping / Zero Account Risk**: Never probes private host endpoints, never touches OAuth credentials, and never sends telemetry (optional in-panel update check only fetches public GitHub Releases metadata and can be set to `Off` anytime; remote pricing sync is off by default).
- **Visibility-Gated Zero Idle Overhead**: Built on Antigravity's native `sidecar_sdk` auxiliary pane lifecycle—automatically pauses all polling when the pane is collapsed or hidden.
- **Host-Synced Adaptive Theme**: Probes Antigravity's live CSS custom properties (`--background`, `--card`, `--primary`, etc.) so dark and light themes adapt automatically without manual theme toggles.

---

## Modular Feature Showcase

AGY Lens ships with **8 independently toggleable and reorderable modules**—all enabled out of the box (with compact collapsed KPI cards for secondary views) so every capability is immediately discoverable while keeping your sidebar clean. Disable any module anytime to skip its queries completely.

### 1. Live Context, Prompt Cache & Token Flow (Auxiliary Pane)

Shown above in the dual-theme hero preview:
- **Live Context**: Tracks tokens against the model's **Auto-Compact ceiling** (with `55%` caution and `80%` high-pressure ticks) and breaks down usage across `System Prompt`, `Tools`, `Rules`, `Skills`, `Subagents`, and `Chat Messages`; also ticks live **time since last reply** with a color-coded empirical cache-freshness badge using progressive `5h`-step lookback (`5h → 10h → … → 168h` until `≥50` follow-up turns).
- **Prompt Cache Diagnostics**: Displays last-turn hit ratio, session cumulative cache hit rate, estimated USD saved vs. uncached baseline, and a seamless **15-turn stacked bar chart** highlighting `Cold` starts and sudden `Drop` events.
- **Input/Output & Token Flow**: Splits tokens across 4 buckets (`Uncached In`, `Cache Read`, `Thinking Out`, `Visible Out`) with `Session | Global` scope switching and average `TTFT / Gen` latency.

### 2. Global Cache Observatory (Module #6)

Diagnose cross-session prompt-cache instability—such as idle-gap TTL decay, transient routing misses, and prefix boundary cuts—with a configurable multi-metric matrix, rich cell inspection cards, and an anonymized report generator.

<p align="center">
  <img src="assets/screenshots/cache-observatory.png" alt="AGY Lens Global Cache Observatory: Multi-Metric Matrix, Metric Config Popover, Pinned Cell Detail Card, Log Scatter & Top Anomalies" width="100%" />
</p>

- **4 Health KPI Tiles**: Follow-up Hit %, Unexpected `0%` Misses (with **Bounce-Back** recovery count), Boundary Cuts (excluding intentional model switches and compactions), and estimated Miss Penalty USD.
- **Configurable Multi-Metric & Custom Idle-Gap `Model × Idle-Gap` Matrix**: Defaults to 6 side-pane-friendly buckets spanning up to `1h` (`<=10s`, `10-60s`, `1-5m`, `5-10m`, `10-60m`, `>1h`) alongside a strictly consistent sample-weighted **All (Total)** column. Use **`Gaps · ≤1h ▾`** to toggle preset breakpoints (`2s`–`6h`) or add custom durations (`1s`–`24h`, e.g. `45s`, `15m`, `2h`) that automatically form `<=min`, adjacent middle intervals, and `>max` while adapting the log scatter plot X-axis. Use **`Hit % +2 ▾`** to pick any of **6 metrics**—**Token Hit Ratio** (default primary), **Cache Keep Rate** & **Avg Cost / Turn** (default stacked sub-rows), **Bucket Total Cost**, **Miss Penalty**, and **Follow-up Turns**—stacking any number of vertical in-cell sub-rows while preserving the previous primary as a sub-row when switching.
- **Hover Preview & Click-to-Pin Full Detail Card**: Hover any bucket or Total cell to preview all metrics with `[Main]`/`[Sub]` tags, anomaly breakdown, cache savings, average input context, and wasted tokens; click any cell to pin the detail card for side-by-side inspection.
- **Idle-Gap vs. Hit-Rate Log Scatter Plot**: Filterable via a compact model dropdown, visually separating normal hits, `0%` misses, boundary cuts, and low-hit turns on a logarithmic time axis.
- **On-Demand `Timeline` & `Compare` Views (`Matrix` Default)**: Switch anytime between the default `Matrix`, **`Timeline`** (`1h` / `5h` / `1d` / `7d` slices with `≤5m Active` vs. `All Gaps` scope, dual-band Hit % + volume + `0%`-miss trend chart, `Time × Idle-Gap` heatmap, and per-slice model-mix breakdown), and **`Compare`** (2–4 period retention-curve overlays dynamically aligned to the chosen slice length, Delta summary bar, and one-click `Copy Compare Markdown`).
- **Top Anomalies & `Copy Issue Markdown`**: Inspect `prev → miss → next` hit transitions, `Idle Gap` vs. `Start Gap`, and export a **privacy-sanitized** Markdown table ready for GitHub issues.

### 3. Models, Long-Context Cost & 16-Week Calendar Heatmap (Modules #4 & #5)

<p align="center">
  <img src="assets/screenshots/cost-calendar.png" alt="Models API-Equivalent Cost and 16-Week Calendar Heatmap" width="100%" />
</p>

- **Models & API-Eq. Cost**: Aggregates compute value by model or workspace, computes cache savings, uses flat 1M standard rates for Gemini 4 & Claude 5.5, and automatically applies **>200k tiered long-context pricing** (`>200k` badge) on models or user overrides that carry a long-context tier.
- **16-Week Calendar Heatmap & Day Drill-Down**: Tracks active day streaks, Today vs. 7-day average deltas, 14-day sparkbars, and a crisp 1:1 pixel heatmap (`API-eq. $ | Tokens | Turns`). Click any day cell to drill down into that date's sessions and costs.
- **Request Log & Speed (Module #8)**: On-demand SQL-paginated single-row request log (`GET /api/requests`) with model/source/0%-miss/slow filters and multi-field sorting, displaying `uncached/cacheRead/out`, hit %, TTFT, Decode & End-to-End TPS, and pure API-equivalent cost (never multiplied by quota calibration factors), with expandable per-turn details (`thinking/visible` split, timing, cache saved, `provider_request_id`). Its **Speed & Periods** view adds an orthogonal **`Token-Weighted` | `Per-Req P50`** switch, per-model speed comparisons, and `1h / 5h / 1d / 7d` period averages & totals.

### 4. Manual Quota Alignment & Cycle Budget Inversion (Module #7)

Because Antigravity exposes no official Sidecar Quota API, AGY Lens keeps quota tracking 100% compliant via **2-decimal manual alignment anchors** (`e.g. 94.25%`).

<p align="center">
  <img src="assets/screenshots/quota-budget.png" alt="Manual Quota Alignment and Implied Cycle Budget" width="100%" />
</p>

- **Independent Per-Pool `7d` Cycles & Precision-Aware Reset Boundaries**: `Gemini`, `Argon`, and `Third-Party` each track their own independent `7d` cycle `[start → reset]` derived from explicit reset timestamps; two-pass cycle segmentation with precision-interval intersection prevents hour/day countdown jitter (`e.g. 6d 23h`) from falsely splitting cycles, keeps boundary-band trailing anchors from polluting new-cycle Δu, and scopes both calibration and the default anchor history strictly to each pool's active `7d` cycle (older `7d` cycles and `5h` records stay cleanly grouped and collapsed).
- **Dynamic Reset Inheritance, Inline Editing & Single-Anchor Bootstrap**: Persists only explicit reset timestamps and derives cycle inheritance dynamically at read time (with inline reset editing/clearing and zero stale copies); when a cycle expires, archived anchors fold automatically while first-turn-triggered rollover tracks new-cycle spend alongside the previous cycle's reference budget, and a single new-cycle snapshot can immediately produce a conservative `100%` cycle-start bootstrap estimate (open upper CI bound) before smoothly switching to pure differential calibration.
- **Orthogonal 3-Factor Weight Calibration Lab (`M / C / O` All-Subsets Selection)**: Shares default Base anchors with `pricing_defaults.json` (`defaultAnchors`) and lets you switch the `1.00×` Base model right in the UI; decouples **Model Multipliers (`M`)**, **Cache-Read Multiplier (`C`)**, and **Output Multiplier (`O`)** into 3 independent switches (so single-model cycles can still calibrate `C` or `O`), evaluates all 8 subsets with profile-grid Huber-WLS + LOOCV + `VIF < 10`, conservatively coalesces settlement lag / short gaps (`<10m` for `7d`, `<5m` for `5h`) & micro-rebounds, and transparently shows trial estimates alongside an Observed vs. Predicted (`pp`) residual chart.
- **Strictly Local Manual Multi-Account & Switch Timeline (Zero-Clutter Stealth Mode)**: Never reads OAuth credentials or host logs. Single-account users see zero extra UI; adding a 2nd account in **Settings → Accounts & Switch Timeline** unlocks a custom header account filter menu and Quick Switch popover (`All` / `CLI` / `Desktop` scope, retroactive backfill with **Preview Impact**, plus one-click per-session override or "Start switch here" on Live Context). Analytics, 5h/7d quota cycles, anchor calibrations, and Cache Observatory cross-account guards are strictly isolated per account and preserved across index rebuilds.

### 5. Settings Drawer, In-Panel Auto-Update, `?` Help & Bilingual UI

<p align="center">
  <img src="assets/screenshots/settings-drawer.png" alt="AGY Lens Main Header Update Pill, Update Popover, Settings Drawer with 7 Modules, Version & Auto-Update Controls, and ? Help Tooltip" width="100%" />
</p>

- **In-Panel Auto-Update & One-Click Rollback**:
  - **Header Micro-Pill & Release Popover**: When a newer release is available, a compact `↑ vX.Y.Z` badge appears right beside the `AGY Lens` title (blue while pending, green once verified & staged). Click it to inspect release notes and trigger **Restart to Apply** in one click, or skip the version.
  - **3 Configurable Policies (`Auto` | `Notify` | `Off`)**: Defaults to **`Auto`**—checks GitHub Releases every 6h while the pane is active, downloads & smoke-tests in an isolated subprocess (`AGY_LENS_SMOKE=1`), and applies cleanly at next cold start (or after 10 minutes idle / immediate click). Maintainers can also mark minor releases as manual-only via an invisible `<!-- agy-lens:manual-only -->` tag in the GitHub Release body (skips auto-push & header pill while remaining manually installable from Settings). Switch to **`Notify`** or **`Off`** (100% offline) anytime in **Settings → Version & Auto-Update**.
  - **Crash-Safe `boot.mjs` Bootstrap & Auto-Rollback**: Updates are applied by a minimal, self-contained `boot.mjs` before `main.mjs` loads—preventing frontend/backend mismatches. If a new version ever fails startup twice, `boot.mjs` **automatically rolls back** to the previous backup and marks the bad version; a manual **Rollback to vX.Y.Z** button is also available in Settings.
- **7 Independent Modules & Reordering**: All 7 modules are enabled out of the box (with compact collapsed KPI cards for secondary views); disable or reorder (`↑ / ↓`) any module anytime.
- **Built-in `?` Help Tooltips**: Every module header and settings control carries an interactive `?` callout explaining *what it shows*, *when to enable*, and *exact scan scope*.
- **Instant Bilingual Switch**: Toggle `English` / `中文` anytime (`?lang=en` / `?lang=zh-CN` URL override also supported for previews).

---

## Privacy & Compliance Guarantee

| Aspect | AGY Lens Guarantee |
| :--- | :--- |
| **Conversation DB Access** | Opened strictly with `new DatabaseSync(path, { readOnly: true })` (WAL-aware incremental mtime/size indexing; never writes to source DBs). |
| **Host RPC & Auth Tokens** | **Zero** internal RPC probing, **zero** OAuth/credential file reads, **zero** undocumented host endpoint calls. |
| **Background Execution** | Runs solely as an Antigravity-managed UI sidecar (`on-failure`); polling pauses automatically when the pane is hidden (`Off` / `15s` / `30s` / `60s` / `5m`). |
| **Optional Network Access** | In-panel auto-update only `GET`s public GitHub Releases metadata over strict HTTPS host allowlists (zero local data uploaded; disable via `Settings → Update Policy → Off`). Remote pricing sync is disabled by default. |
| **Local Cache Storage** | Incremental index, settings, pricing overrides, update backups, and quota anchors live locally under `~/.gemini/antigravity/sidecar_data/agy-lens/lens_panel/data/` (physically isolated from plugin code). |
| **Issue Report Export** | `Copy Issue Markdown` strips workspaces, local paths, and conversation titles—emitting only aggregated stats, model IDs, gap durations, and provider request IDs. |

---

## Installation & Updates

### Option A: Clone Directly into Antigravity Plugins (Recommended)

```bash
git clone https://github.com/xukp20/agy-lens.git ~/.gemini/config/plugins/agy-lens
agy plugin validate --strict ~/.gemini/config/plugins/agy-lens
```

*Recommended*: Supports **both** in-panel Git exact-tag auto-updates (with dirty-tree and non-`main` branch protection) **and** manual `git pull --ff-only` updates.

### Option B: Standalone Install via CLI or Release Archive

```bash
git clone https://github.com/xukp20/agy-lens.git /tmp/agy-lens
agy plugin install /tmp/agy-lens
```

*Also supports in-panel auto-updates*: Even without `.git`, AGY Lens downloads official GitHub release tarballs over HTTPS, extracts them with a zero-dependency pure-Node `.tar.gz` parser, verifies SHA-256 checksums + isolated smoke tests, and applies them safely via `boot.mjs` on Linux, macOS, and Windows.

> **Note**: Requires Antigravity `2.22+` (Sidecar Web UI support) and Node.js `24+` (built-in `node:sqlite`). No `npm install` step is needed.

### Option C: Standalone Web Server & Headless SSH / CLI Mode (No Antigravity Desktop Required)

On headless Linux / SSH machines running Antigravity CLI, launch the full AGY Lens dashboard directly at a local URL—sharing the same read-only conversation DBs and `sidecar_data/` directory with zero npm dependencies:

```bash
# Start on 127.0.0.1:4319 (forward via `ssh -L 4319:127.0.0.1:4319 user@remote`)
node bin/agy-lens.mjs serve --port 4319
# Or directly from an installed plugin directory:
node ~/.gemini/config/plugins/agy-lens/sidecars/lens_panel/standalone.mjs --port 4319

# Print a compact Today / 7d API-eq. cost & 7d quota summary (supports --account and --json):
node bin/agy-lens.mjs status
node bin/agy-lens.mjs status --account "Ultra Alt"

# Log an account switch (supports --scope all|cli|desktop, --at -30m|<ISO>, and --dry-run preview):
node bin/agy-lens.mjs switch "Ultra Alt" --scope cli --at -15m --dry-run

# Reverse proxy under a subpath with token authentication (env var avoids ps aux exposure):
AGY_LENS_TOKEN=your-secret node bin/agy-lens.mjs serve \
  --base-path /agy-lens --trust-proxy --allowed-hosts lens.example.com --read-only
```

- **Security Guardrails**: Defaults to `127.0.0.1` with strict `Host` validation (DNS Rebinding protection, allowing arbitrary SSH-forwarded ports on loopback), `Origin`/`Sec-Fetch-Site` CSRF checks, mandatory token + `HttpOnly` HMAC cookie auth whenever bound to non-loopback hosts or `--trust-proxy`, optional `--read-only` mode, and `256 KB` request body caps.
- **Standalone UX**: Auto-detects browser Dark/Light preference with a header theme toggle, provides a recent CLI/Desktop conversation switcher in Live Context, and aligns the header cleanly with the wide-screen 2-column grid.

### How Updates Work (3 Ways)

1. **Automatic In-Panel Updates (Default — Recommended)**: Checks GitHub Releases every 6h while active, stages & smoke-tests updates in the background, and applies automatically at next cold start (or immediately when you click the green `↑ vX.Y.Z` pill next to `AGY Lens`). Works for **both** Git clone and Standalone installs; preserves all user data in `sidecar_data/` and protects uncommitted local Git edits.
2. **Manual In-Panel Check & Apply**: Set **Settings → Version & Auto-Update → Update Policy** to `Notify` or `Off`, then click **Check Now** / **Update & Restart** whenever you want (with one-click **Rollback** to the previous version).
3. **CLI Manual Update** (for `git clone` installs):
   ```bash
   git -C ~/.gemini/config/plugins/agy-lens pull --ff-only
   agy plugin validate --strict ~/.gemini/config/plugins/agy-lens
   ```

---

## Customizing Model Pricing

AGY Lens uses a **3-tier pricing resolution engine** (`sidecars/lens_panel/lib/pricing.mjs`):

1. **User Overrides (`pricing_overrides.json`)** — Highest precedence. Edit per-model input, output, thinking, cache-read, cache-write, and `>200k` long-context tiered rates directly in the **Settings → Pricing Management** UI (or reset back to default anytime).
2. **Bundled Date-Versioned Defaults (`sidecars/lens_panel/lib/pricing_defaults.json`)** — Built-in offline baseline covering Gemini 4, Gemini 3.8, and Claude 5.5 tiers including scheduled effective dates and `>200k` multipliers.
3. **Optional Remote Sync (`remote_pricing_cache.json`)** — Disabled by default for 100% offline operation. Enable **Auto-Sync Remote Pricing** (24h TTL) or click **Sync Pricing Now** to refresh public reference prices from LiteLLM / OpenRouter JSON catalogs.

---

## Local Architecture & Data Flow

```text
  Read-Only Source DBs (mode=ro)              AGY Lens Sidecar (Node.js 24)
  ──────────────────────────────              ─────────────────────────────
  ~/.gemini/antigravity/                      sidecars/lens_panel/
   └─ conversations/<uuid>.db   ──┐            ├─ lib/protobuf.mjs    (raw wire decode)
                                  ├─(ro)────▶  ├─ lib/indexer.mjs     (WAL incremental index)
  ~/.gemini/antigravity-cli/      │            ├─ lib/pricing.mjs     (3-tier + >200k rates)
   └─ conversations/<uuid>.db   ──┘            ├─ lib/cache_observatory.mjs
                                               ├─ lib/quota.mjs       (2-decimal CI budget)
                                               ├─ lib/updater.mjs     (Git & tarball self-update)
                                               ├─ lib/tar_extract.mjs (pure-JS PAX/USTAR unpack)
                                               ├─ boot.mjs            (cold-start apply & rollback)
                                               └─ main.mjs            (SidecarApp REST API)
                                                     │
                                                     ▼  127.0.0.1 HTTP + /preload.js theme tokens
                                               web/{index.html,styles.css,app.js}
                                               (Antigravity Aux Pane — 7 modular cards)
```

---

## Local Demo Mode & Screenshot Tools

Preview the full AGY Lens UI in any browser using anonymized synthetic telemetry—no local Antigravity databases required:

```bash
node scripts/demo_server.mjs --port 4318
```

Then open:
- Dark Mode (English): `http://127.0.0.1:4318/?theme=dark&lang=en`
- Light Mode (中文): `http://127.0.0.1:4318/?theme=light&lang=zh-CN`

### Regenerating Documentation Screenshots

- **Zero-browser 2x Retina previews** (`cairosvg` + `Pillow`):
  ```bash
  python3 scripts/render_previews.py
  ```
- **Optional real-browser Playwright capture** (on machines with Chromium):
  ```bash
  npm install --no-save playwright && npx playwright install chromium
  node scripts/capture_screenshots.mjs --out assets/screenshots/live
  ```

---

## Acknowledgements & Inspiration

AGY Lens stands on the shoulders of pioneering local-first telemetry work across the Antigravity and AI coding CLI ecosystem:

- **[`ahmetdotsh/agy-context`](https://github.com/ahmetdotsh/agy-context) & [`ahmetdotsh/agy-usage`](https://github.com/ahmetdotsh/agy-usage)** — Pioneered strictly local, read-only SQLite + Protobuf inspection for Antigravity conversation databases.
- **OpenAI Codex CLI (`/status` & `/usage`) & [`steipete/CodexBar`](https://github.com/steipete/CodexBar)** — Inspired the clean separation between live session telemetry and account-level quota tracking, the `Left / Used` perspective switch, and Even-Use pace indicators.
- **`cc-switch` & `ccusage`** — Inspired multi-source (`Desktop + CLI`) toggles, editable model pricing overrides, 4-bucket token flow breakdowns, and daily usage calendar heatmaps.
- **Antigravity Built-in `swarm_board` Sidecar** — Reference pattern for `SidecarApp` lifecycle, `/preload.js` luminance probing, and zero-flicker host CSS token synchronization.
- **[`google-antigravity/antigravity-cli#1533`](https://github.com/google-antigravity/antigravity-cli/issues/1533)** — Community prompt-cache telemetry discussions that inspired Module #6 (Global Cache Observatory): `Model × Idle-Gap` hit matrices, boundary-cut thresholds, bounce-back classification, and anonymized `Copy Issue Markdown`.

---

<p align="center">
  Released under the <a href="LICENSE">MIT License</a>.
</p>
