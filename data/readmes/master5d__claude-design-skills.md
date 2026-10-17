# Design Harness for Claude Code

A 3-layer design system for engineers who want to ship great UI without being designers. Based on Neethan Wu's ["Design Without Designing"](https://x.com/neethanwu/status/2034786360356204934).

---

## Layer 1 — Skills (the expertise)

Skills are instruction files that load design expertise into your agent. This plugin bundles 6 of them.

### Bundled in this plugin

| Skill | Invoke | What it does |
|-------|--------|--------------|
| `emil-design-eng` | `/emil-design-eng` | Emil Kowalski's animation & UI polish philosophy. Review table format, spring physics, clip-path tricks, performance rules. |
| `baseline-ui` | `/baseline-ui` | Tailwind constraints, accessible primitives, animation rules. Catches AI-generated slop. |
| `fixing-accessibility` | `/fixing-accessibility` | ARIA, keyboard nav, focus traps, WCAG audit. |
| `fixing-metadata` | `/fixing-metadata` | OG tags, canonical URLs, SEO, social card audit. |
| `fixing-motion-performance` | `/fixing-motion-performance` | Compositor-only animation, layout thrash prevention, scroll perf. |
| `interface-design` | `/interface-design` | Intent-first design system. Domain exploration, signature elements, surface elevation, craft checks. |

**Sources:** [emilkowalski/skill](https://emilkowal.ski/skill) · [ibelick/ui-skills](https://ui-skills.com) · [Dammyjay93/interface-design](https://interface-design.dev)

### Also install separately

**Impeccable** (`pbakaus/impeccable`) — 20+ commands including `/delight`, `/polish`, `/audit`, `/animate`, `/typeset`, `/arrange`. The most-used skill in the harness.

```
/plugin add impeccable@impeccable
```

---

## Layer 2 — Agent Canvas (the surface)

Design surfaces that use your agent as the kernel. No built-in AI — they expose MCP tools and let Claude do the work.

### Pencil

Git-diffable `.pen` format. Design files live in your repo, versioned like code. Supports agent swarm mode (up to 6 agents working on the canvas simultaneously).

- **Install:** [pencil.dev](https://pencil.dev) — free
- **MCP:** Installed via the Pencil desktop app (auto-registers MCP server)
- **Permission:** already added to `settings.json` → `permissions.allow: ["mcp__pencil"]`

### Paper

HTML/CSS canvas — what you design is actual code, no translation layer. MCP exposes full read/write to design files.

- **Install:** [paper.design](https://paper.design) — free tier available
- **MCP:** Runs locally when the Paper desktop app is open with a file

```bash
# Already added to your Claude Code user config:
claude mcp add paper --transport http http://127.0.0.1:29979/mcp --scope user
```

> Paper MCP starts automatically when you open a `.paper` file in the desktop app. If tools stop responding, restart the agent session to re-establish the connection.

**Available Paper MCP tools:** `get_basic_info`, `get_selection`, `get_node_info`, `get_children`, `get_tree_summary`, `get_screenshot`, `get_jsx`, `get_computed_styles`, `create_artboard`, `write_html`, `set_text_content`, `rename_nodes`, `duplicate_nodes`, `update_styles`, `delete_nodes`

---

## Layer 3 — Inspiration (the eye)

Tools for training visual taste. Use before design work to calibrate what "good" looks like.

| Tool | URL | What it does |
|------|-----|--------------|
| **Variant** | [variant.ai](https://variant.ai) | Type an idea → endless non-repeating design interpretations. Style Dropper absorbs visual DNA from any design and transfers it. Export as React or copy prompts with HTML references for your coding agent. |
| **Mobbin** | [mobbin.com](https://mobbin.com) | Curated mobile + web UI patterns from top apps. Best for onboarding, settings, checkout flows. Figma plugin available. |
| **Awwwards** | [awwwards.com](https://awwwards.com) | Jury-scored cutting-edge web craft. Raises the ceiling for what's possible. |
| **Cosmos** | [cosmos.so](https://cosmos.so) | Visual inspiration board. Hex color search, vague description search, curated collections. Web, interiors, typography, photography. |

**Workflow:** Spend ~20 minutes in Variant or Cosmos before any design session. Build clusters of visual references. Then prompt your agent with specific references or export Variant components directly to code.

---

## How the layers work together

```
Inspiration (Layer 3)
  ↓ calibrates taste, gives references
Skills (Layer 1)
  ↓ encode expertise, enforce quality
Agent Canvas (Layer 2)
  ↓ Claude executes with real tools
→ shipped design
```

1. Open Variant or Cosmos, find a direction that fits your product
2. Open Pencil or Paper with a design file
3. Invoke the right skill for the task:
   - Starting fresh → `/interface-design` (domain exploration + intent)
   - Polishing existing UI → `/delight` or `/polish` (Impeccable)
   - Reviewing animations → `/emil-design-eng`
   - Checking a11y → `/fixing-accessibility`
   - Auditing overall → `/audit` (Impeccable)
4. Let Claude work on the canvas via MCP
5. Export code directly — no handoff

---

## Credits

- [Neethan Wu](https://x.com/neethanwu) — the harness concept
- [Emil Kowalski](https://emilkowal.ski) — design engineering skill
- [Julien Thibeaut](https://x.com/ibelick) — UI Skills
- [Oyindamola Akinleye](https://x.com/Dammyjay93) — Interface Design
- [Paul Bakaus](https://x.com/pbakaus) — Impeccable
