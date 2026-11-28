<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/logo-mark-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./docs/assets/readme/logo-mark-light.svg" />
  <img src="./docs/assets/readme/logo-mark-light.svg" alt="ArchRay" width="76" height="76" />
</picture>

<h1>ArchRay</h1>

<p><strong>Equip your AI coding agent to read real source code and build interactive, 100% offline 3D Spatial &amp; 2D Bento architecture maps.</strong></p>

<p>
  <a href="https://github.com/loofare/ArchRay/releases/latest"><img src="https://img.shields.io/badge/version-v0.6.0-E8BA55?style=flat-square&labelColor=12110E" alt="Version v0.6.0" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-10B981?style=flat-square&labelColor=12110E" alt="License MIT" /></a>
  <img src="https://img.shields.io/badge/node-20%2B-38BDF8?style=flat-square&labelColor=12110E" alt="Node.js 20+" />
  <img src="https://img.shields.io/badge/delivery-100%25%20offline%20HTML-10B981?style=flat-square&labelColor=12110E" alt="100% Offline Single HTML" />
  <a href="https://archray.dev/"><img src="https://img.shields.io/badge/website-archray.dev-E8BA55?style=flat-square&labelColor=12110E" alt="archray.dev" /></a>
</p>

<p>
  <strong>English</strong> ·
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="https://archray.dev/">Website</a> ·
  <a href="https://archray.dev/demo">Live 3D Sandbox</a> ·
  <a href="https://archray.dev/guides/">Guides</a> ·
  <a href="https://archray.dev/compare/mermaid-structurizr-eraser/">Compare Tools</a>
</p>

<br />

<a href="https://archray.dev/demo">
  <img src="./docs/assets/readme/screenshots/demo-3d-en.png" alt="ArchRay 3D Spatial Atrium Live Demo — FreshMart Commerce (5 layers, 16 modules, 19 directed edges)" width="100%" />
</a>

<p><sub>Captured live from <a href="https://archray.dev/demo">archray.dev/demo</a>: interactive 3D Spatial Atrium, 2D Bento map, Health Hotspots, and Replaceability views—click to explore live.</sub></p>

</div>

---

## Core Engineering Capabilities

<table>
  <tr>
    <td width="50%" valign="top">
      <p><img src="./docs/assets/readme/icons/ic-layers.svg" alt="" width="20" height="20" align="absmiddle" /> &nbsp;<strong>True 3D Spatial Atrium + 2D Bento Map</strong></p>
      <p>VisionOS-style floating HUD powered by <strong>deterministic ELK port routing</strong>, separating client surfaces, central service spines, async/AI wings (<code>-X</code>), external SaaS orbits (<code>+X</code>), and storage plinths.</p>
    </td>
    <td width="50%" valign="top">
      <p><img src="./docs/assets/readme/icons/ic-evidence.svg" alt="" width="20" height="20" align="absmiddle" /> &nbsp;<strong>Verified Source Evidence &amp; Honest Provenance</strong></p>
      <p>Every node and dependency cites repository <code>sourcePaths</code>; numeric metrics cleanly distinguish direct measurements (<code>measured</code>) from static estimates (<code>≈</code>)—never faking live APM telemetry.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <p><img src="./docs/assets/readme/icons/ic-health.svg" alt="" width="20" height="20" align="absmiddle" /> &nbsp;<strong>Health Hotspots &amp; Replaceability Prompts</strong></p>
      <p>Surface coupling bottlenecks and lock-in risk, compare drop-in OSS or managed alternatives by effort/risk, and copy ready-to-run AI migration prompts back to your coding agent.</p>
    </td>
    <td width="50%" valign="top">
      <p><img src="./docs/assets/readme/icons/ic-offline.svg" alt="" width="20" height="20" align="absmiddle" /> &nbsp;<strong>Zero-Network Single-File HTML</strong></p>
      <p>Emits a self-contained <code>.archray/index.html</code> (opens directly via <code>file://</code>) bundling <strong>167 embedded vector tech logos</strong>, unclipped full-canvas PNG export, and offline QR share posters.</p>
    </td>
  </tr>
</table>

---

## How It Works: Separating Semantics from Deterministic Layout

LLMs excel at reading repository structure and control flow—but collapse into crossed edges when hand-authoring SVG coordinates or raw diagrams. ArchRay decouples semantic extraction from layout math:

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/pipeline-en-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./docs/assets/readme/pipeline-en-light.svg" />
    <img src="./docs/assets/readme/pipeline-en-light.svg" alt="ArchRay 4-stage pipeline: Real Source Repo -> AI Coding Agent (/archray) -> Deterministic ELK -> Offline Single HTML" width="100%" />
  </picture>
</div>

---

## View Gallery: Four Inspection Lenses on One Verified Graph

Analyze source once into `.archray/graph.json`, then switch projections, health diagnostics, and shareable exports with zero extra LLM calls:

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://archray.dev/demo?locale=en&projection=2d&lens=topology">
        <img src="./docs/assets/readme/screenshots/demo-2d-en.png" alt="ArchRay 2D Bento Map View" width="100%" />
      </a>
      <br />
      <strong>2D Bento Map</strong><br />
      <sub>L0–L4 deterministic containment layers, adaptive reflow &amp; live minimap</sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://archray.dev/demo?locale=en&projection=3d&lens=health">
        <img src="./docs/assets/readme/screenshots/demo-health-en.png" alt="ArchRay Health Hotspots Lens" width="100%" />
      </a>
      <br />
      <strong>Health Hotspots Lens</strong><br />
      <sub>Highlights critical hotspots (6.2k LOC sync lock) with measured vs <code>≈</code> labels</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://archray.dev/demo?locale=en&projection=3d&lens=replaceability">
        <img src="./docs/assets/readme/screenshots/demo-replace-en.png" alt="ArchRay Replaceability & AI Migration Prompts" width="100%" />
      </a>
      <br />
      <strong>Replaceability &amp; Migration Prompts</strong><br />
      <sub>Compare Passport → Clerk / Keycloak options with downstream impact preview</sub>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://archray.dev/">
        <img src="./site/share-en.png" alt="ArchRay Unclipped PNG Export & Offline QR Poster" width="100%" />
      </a>
      <br />
      <strong>Unclipped PNG &amp; Offline QR Poster</strong><br />
      <sub>Full world-bounds PNG projection &amp; zero-network QR cards for team handoffs</sub>
    </td>
  </tr>
</table>

---

## 1. 30-Second Install & First Map

> **Requirements**: Node.js 20+, `curl`, and `tar` (on Windows, run the installer inside Git Bash or WSL; it emits `.archray\archray.cmd`).

### One-Line Install in Target Repository Root

```sh
curl -fsSL https://github.com/loofare/ArchRay/releases/latest/download/install.sh | sh -s -- . claude
```

Replace `claude` with your AI host (comma-separated lists like `claude,cursor` or `all` are supported):

| AI Host | Argument | Session Trigger | Host Files Written |
|---|---|---|---|
| <picture><source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/icons/claude.svg" /><img src="./docs/assets/readme/icons/claude.svg" alt="Claude Code" width="16" height="16" align="absmiddle" /></picture> &nbsp;**Claude Code** | `claude` | `/archray`, `/archray:frontend`, … | `.claude/skills/archray/`, `.claude/commands/` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/icons/cursor-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="./docs/assets/readme/icons/cursor-light.svg" /><img src="./docs/assets/readme/icons/cursor-light.svg" alt="Cursor" width="16" height="16" align="absmiddle" /></picture> &nbsp;**Cursor** | `cursor` | `/archray`, `/archray-frontend`, … | `.cursor/rules/archray.mdc`, `.cursor/commands/` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/icons/antigravity.svg" /><img src="./docs/assets/readme/icons/antigravity.svg" alt="Antigravity" width="16" height="16" align="absmiddle" /></picture> &nbsp;**Antigravity** | `antigravity` | `/archray` or Skill trigger | `.agent/skills/archray/`, `.agent/commands/` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/icons/pi.svg" /><img src="./docs/assets/readme/icons/pi.svg" alt="Pi" width="16" height="16" align="absmiddle" /></picture> &nbsp;**Pi** | `pi` | `/archray`, `/archray-frontend`, `/skill:archray` | `.agents/skills/archray/`, `.pi/prompts/` |
| <picture><source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/icons/codex-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="./docs/assets/readme/icons/codex-light.svg" /><img src="./docs/assets/readme/icons/codex-light.svg" alt="Codex" width="16" height="16" align="absmiddle" /></picture> &nbsp;**Codex** | `codex` | `$archray` or `/skills` | `.agents/skills/archray/SKILL.md` |

<details>
<summary>Prefer letting your AI coding assistant run setup? Paste this prompt</summary>

```text
Download https://github.com/loofare/ArchRay/releases/latest/download/install.sh to a temporary file, verify it succeeded, and run `sh <temp-file> . claude` from this repo root (replace claude with your host).
```

</details>

### Generate Your First Map

1. Open a fresh AI coding session in the repository.
2. Run `/archray` (`$archray` on Codex), or simply ask: **“Use archray to inspect source code and build a 3D map”**.
3. Open `.archray/index.html` directly in any browser.

---

## 2. L0–L9 Spatial Layers & Instant Slicing

Once `.archray/graph.json` is generated, slice any single layer or comma-separated cross-layer path on demand—direct one-hop neighbors remain softly dimmed for context:

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./docs/assets/readme/layers-en-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="./docs/assets/readme/layers-en-light.svg" />
    <img src="./docs/assets/readme/layers-en-light.svg" alt="ArchRay L0-L9 Spatial 4-Quadrant Zoning & CLI Layer Slicing" width="100%" />
  </picture>
</div>

| Goal | Slash Command / Args | What It Focuses |
|---|---|---|
| **View All (Default)** | `/archray` or `/archray:full` | All 10 architectural layers (`L0–L9`) |
| **Frontend** | `/archray:frontend` or `/archray frontend` | `L0 client` web apps, mobile & UI surfaces |
| **Backend + Async** | `/archray:backend` or `/archray backend` | `L3 service` domain APIs + `L4 async` queues/workers |
| **Data & Storage** | `/archray:data` or `/archray data` | `L5 data` SQL databases, Redis caches, search & S3 |
| **Network & Edge** | `/archray:network` or `/archray network` | `L1 edge` + `L2 gateway` CDN, WAF & ingress |
| **Security & Auth** | `/archray:security` or `/archray security` | `L2 gateway` OAuth/OIDC, JWT guards & rate limits |
| **Cross-Layer Combos** | `/archray frontend,backend`<br>`/archray backend,data`<br>`/archray ai,async,data` | Combine any layers with commas (EN & ZH aliases work) |
| **Theme & Locale** | `--style blueprint --lang en` | Themes: `tech` / `blueprint` / `glass` / `paper` |
| **Update / Uninstall** | `/archray update` / `/archray uninstall` | Safely keeps `graph.json`, `view.json`, and HTML |

---

## 3. Verified Monorepo Benchmarks & Tool Comparison

Tested on real engineering repositories—confirming non-overlapping ELK layouts, `+N` auto-collapsing on dense monorepos, and v0.6.0 UTF-8 without BOM enforcement:

| Benchmark Repository | Scale & Topology | Build / Layout Speed | Verified Highlights |
|---|---|---|---|
| **calcom/cal.com** (`ae027bb`) | `7,712` tracked files → `33` modules · `75` edges · `7` layers | **`196ms`** Node ELK layout | Dense packages fold (`+N`), 60fps 3D orbit |
| **FreshMart Commerce** (Live Demo) | `16` modules · `19` edges · `5` layers · Checkout flow | Instant single-file HTML | Surfaces 6.2k LOC lock hotspot & Clerk migration plan |
| **SaaS Starter & RealWorld** | `43–49` source files | **`0.03s`** CLI build | Maps App Router/Prisma/Stripe, flags `JWT_SECRET` fallback |

- Comparing ArchRay against **Mermaid, Structurizr DSL, Eraser, or Excalidraw**? See the full matrix: [ArchRay vs Mermaid, Structurizr & Eraser](https://archray.dev/compare/mermaid-structurizr-eraser/).
- Playbooks & specs: [Claude Code Guide](https://archray.dev/guides/claude-code-architecture-diagram/) · [Cursor Guide](https://archray.dev/guides/cursor-codebase-visualization/) · [Codex, Pi & Antigravity](https://archray.dev/guides/codex-pi-antigravity/) · [Layers & CLI Reference](https://archray.dev/guides/architecture-layers-reference/).

---

## 4. CLI & Maintenance (From Repo Root)

Self-contained wrapper inside `.archray/` with zero global pollution (`.archray\archray.cmd` on Windows):

```sh
./.archray/archray doctor                                      # Check packaged assets & Node version
./.archray/archray validate .archray/graph.json                # Validate TypeBox schema, locales & UTF-8
./.archray/archray build .archray/graph.json --force --no-open # Rebuild single-file offline HTML
./.archray/archray build .archray/graph.json --layers frontend,data --style blueprint --force
```

**Upgrade & Uninstall:**

```sh
./.archray/archray update --check       # Check latest release without modifying files
./.archray/archray update               # Verify SHA-256 & update (keeps graph/view/HTML)

./.archray/archray uninstall --dry-run  # Preview files to be removed
./.archray/archray uninstall            # Remove tool & host commands (keeps graph/view/HTML)
./.archray/archray uninstall --purge    # Remove the entire .archray/ directory
```

<details>
<summary>One-time upgrade from v0.4.0 or earlier</summary>

```sh
curl -fsSL https://github.com/loofare/ArchRay/releases/latest/download/install.sh | sh -s -- . auto --force
```

</details>

---

## 5. Privacy & Honest Boundaries

> [!NOTE]
> **100% Local · Zero Source Upload · Verifiable Provenance**
>
> - ArchRay CLI and generated `.archray/index.html` views run completely offline over `file://`; source code, paths, and graphs never leave your machine (analysis happens solely inside your authorized coding-agent session).
> - Not a SaaS scanner or live APM agent; `sourcePaths`, health findings, and replacement candidates are static review claims to verify against code.
> - Only an explicit `update` contacts GitHub Releases read-only to check `latest.json` and verify SHA-256 archives.

See [Host Compatibility](docs/host-compatibility.md) · [Changelog](docs/changelog.md) · [NOTICE](NOTICE) · [MIT License](LICENSE) · [archray.dev](https://archray.dev).
