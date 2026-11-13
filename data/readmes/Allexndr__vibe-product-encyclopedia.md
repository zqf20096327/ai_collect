<p align="center">
  <img src=".github/assets/banner.svg" alt="Vibe & Product Engineering Vault - Live Skill & API" width="100%" />
</p>

# Vibe & Product Engineering Encyclopedia (Live Skill + API)

> **If this saves you hours of debugging or prompt-wrangling, please drop a ⭐ Star - it helps more builders find this vault!**

**Languages:** **English** | [Русский](README.ru.md) | [Қазақша](README.kk.md) | [中文](README.zh.md) | [Español](README.es.md)

[![Live Mind-Map & API](https://img.shields.io/badge/Live_Mind--Map_%26_API-vibemap.murdasoft.kz-10b981?style=for-the-badge)](https://vibemap.murdasoft.kz)
[![Chapters](https://img.shields.io/badge/89_Chapters-997_Pages-0f172a?style=for-the-badge)](https://vibemap.murdasoft.kz)
[![Skill Ready](https://img.shields.io/badge/Skill-Claude_%7C_Codex_%7C_Cursor-f59e0b?style=for-the-badge)](SKILL.md)

---

## Why This Repo Exists (The Real Story)

For the last **2+ years**, every useful link, architecture pattern, security fix, prompt recipe, UI/UX breakdown, and hard-won lesson I found ended up in one place: **my Telegram Saved Messages**. Every production project I ship is built on top of those notes.

Instead of keeping thousands of fragments buried in Telegram history, I distilled them into a structured **89-chapter (~997-page) non-linear reference** - and wired it into two ways you can actually use in your daily work:

1. **As a Local AI Skill (`SKILL.md`)** - drop it into Claude Code, Codex, Cursor, or Antigravity so your agent stops guessing and follows principal-level engineering, security, and product standards automatically.
2. **As a Live Auto-Updating Knowledge API (`vibemap.murdasoft.kz`)** - because I continuously add new findings to this vault, connecting via API means your agent always pulls the **latest** version without manually re-downloading files.

---

## ⚡ Quick Start: Connect Live Skill & API (Auto-Updating)

1. Get your free personal API key (`ms_vibe_...`) in **1 click via Telegram (`@MurdaSoft_bot`)** or by email at **[vibemap.murdasoft.kz](https://vibemap.murdasoft.kz)** (click **`🔑 API Ключ`**).
2. Sync the live `SKILL.md` directly into your agent:

```bash
mkdir -p ~/.claude/skills/vibe-product-encyclopedia
curl -fsSL "https://vibemap.murdasoft.kz/api/v1/vibe-knowledge?format=skill&apiKey=YOUR_API_KEY" \
  -o ~/.claude/skills/vibe-product-encyclopedia/SKILL.md
```

3. Query any topic from scripts, CI, or custom agents in real time:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://vibemap.murdasoft.kz/api/v1/vibe-knowledge?q=docker+security"
```

### API Parameters (`GET /api/v1/vibe-knowledge`)

| Parameter | Values | Description |
|---|---|---|
| `apiKey` (or `Authorization: Bearer`) | `ms_vibe_...` | Personal API key from `vibemap.murdasoft.kz` |
| `q` | e.g. `docker`, `anti-slop`, `hooks` | Full-text search across all 89 chapters |
| `chapter` | e.g. `vol1-ch09-live-archivist-threads-vault` | Fetch full content of a specific chapter |
| `format` | `json` (default), `markdown`, `skill` | Output format (`skill` returns live `SKILL.md`) |
| `lang` | `en`, `ru`, `kk`, `zh`, `es` | Preferred language |

---

## 🆕 Latest Updates (2026.11)

- **1-Click Telegram Registration (`@MurdaSoft_bot`):** Instant `ms_vibe_...` API key provisioning via Telegram deep-link (`/api/vibe-auth`) with webhook confirmation and instant polling.
- **Light Editorial Documentation UI:** Unified Notion / Stripe Docs style reader on `vibemap.murdasoft.kz` with clean React Markdown rendering, Quick-Capture callout cards, collapsible Table of Contents, and 375px mobile support.
- **Zero-Noise Clean Typography:** All 89 chapters and 5 `SKILL.*.md` editions cleaned of raw markdown artifacts and em-dashes.

---

## 🧭 What's Inside (Non-Linear Reference - Jump Anywhere)

You don't read this cover-to-cover. Open the visual Mind-Map at **[vibemap.murdasoft.kz](https://vibemap.murdasoft.kz)** or jump straight to the problem you're solving right now:

- **Part I - Vibe-Coding, Reverse Prompting & 2026 Agent Workflows (10 Core Modules)**
  - `I-1`: How to turn this encyclopedia into a Universal Skill (`SKILL.md`)
  - `I-2`: 3-Step Reverse Prompting & 6 Production Bottleneck Fixes
  - `I-3`: 101 GitHub Repos & 123 Engineering Lifehacks (from 2 years of Telegram Saved Messages)
  - `I-4`: Atlas of 951 AI Agent Skills
  - `I-5`: Architecture, Design Tokens, Security & Optimization Guidebook
  - `I-6`: FSD Architecture, Landing Pages & Mobile Adaptive (`44x44px`, zero horizontal overflow)
  - `I-7`: DevSecOps Master Directive (Docker + UFW bypass prevention, SSRF, idempotency)
  - `I-8`: Managing AI Agents like a Corporate Engineering Org
  - `I-9`: **Live Archivist 2026**: `CLAUDE.md` (<400 lines), Anti-Context Collapse (Subagents + Git Worktrees), Deterministic Hooks (`PreToolUse` / `PostToolUse`), MCP Zero-Trust, and Live Knowledge API
  - `I-10`: **Vibe MapOS Full Ecosystem**: Executable `AGENTS.md`, `memory-bank/`, `mcp-registry/`, Swarm protocols, and `.well-known` AEO/GEO endpoints
- **Part II - World-Class Product Playbook (52 Modules)**
  - Discovery, JTBD, Unit Economics, High-Load, DB Indexing, SRE, Payments, Growth
- **Part III - Orchestrating a 100-Specialist AI Team (27 Modules)**
  - 8-stage product lifecycle, quality gates, zero-stub shipping

---

## 🛠️ Manual Local Install (Offline `SKILL.md`)

If you prefer a static local copy without the Live API:

```bash
git clone https://github.com/Allexndr/vibe-product-encyclopedia.git
mkdir -p ~/.claude/skills/vibe-product-encyclopedia
cp vibe-product-encyclopedia/SKILL.md ~/.claude/skills/vibe-product-encyclopedia/SKILL.md
```

(Also included: [`SKILL.ru.md`](SKILL.ru.md), [`SKILL.kk.md`](SKILL.kk.md), [`SKILL.zh.md`](SKILL.zh.md), [`SKILL.es.md`](SKILL.es.md), and the full [`VIBE_PRODUCT_ENCYCLOPEDIA_978P.md`](VIBE_PRODUCT_ENCYCLOPEDIA_978P.md)).

---

## Author & Links

- **Author:** Alexander Murdasov ([MurdaSoft](https://murdasoft.kz))
- **Interactive Mind-Map + AI Archivist + API Key:** [vibemap.murdasoft.kz](https://vibemap.murdasoft.kz)
- **License:** [MIT](LICENSE)
