# Anti-Slop Design Skills

**Design, presentation and document discipline that stops AI output from looking AI-generated.**

Vibe-coded UIs, generated decks and model-written documents share a look: Inter and neon
purple, three identical cards, a blue-gradient cover with a giant centered title, bullet soup,
the "In today's fast-paced world..." intro, everything in bold. It works, and it screams
"template". This kit is the discipline that fixes that, wired for [Claude Code](https://docs.claude.com/en/docs/claude-code).

It ships as three **skills** and two **agents**:

| Piece | Medium | What it does |
|---|---|---|
| `antislop-web` (skill) | Web / app UI | Bans the tells, sets VARIANCE/MOTION/DENSITY dials, requires one signature element, generates `DESIGN.md`. |
| `antislop-decks` (skill) | pptx / Google Slides / HTML | Kills bullet soup with assertion-evidence structure, rotates slide archetypes, data-ink charts, generates `DECK.md`. |
| `antislop-docs` (skill) | docx / Google Docs / PDF | BLUF structure, no bold-bombing, prose-vs-list discipline, real editorial typography, generates `DOC.md`. |
| **Presentation Architect** (agent) | Decks | Directs, audits and **builds** the real deck end-to-end. |
| **Document Architect** (agent) | Documents | Directs, writes, lays out and **builds** the real document end-to-end. |

No vendor, no MCP, no paid service. Everything runs on tools you already have.

## The idea in two rules

1. **Ban the tells, then add one signature.** The bans remove what looks generated. But absence
   of tells is not presence of character, so every deliverable declares exactly one *signature
   element* -- the thing it is remembered for. One, or none.
2. **The pre-flight is a gate.** Each skill ends with a checklist. Any unwaived failure = not
   shippable.

See [`docs/how-it-works.md`](docs/how-it-works.md) for the full mental model.

## Install

### Option A -- Claude Code plugin (recommended)

```
/plugin marketplace add jhuse25/anti-slop-design-skills
/plugin install anti-slop-design-skills
```

### Option B -- install script (clone first)

```bash
git clone https://github.com/jhuse25/anti-slop-design-skills
cd anti-slop-design-skills
./install.sh          # macOS / Linux / Git Bash
```

```powershell
.\install.ps1         # Windows PowerShell
```

Both copy `skills/` and `agents/` into `~/.claude/`. Skills are available immediately; agents
become dispatchable on your next Claude Code session.

Optional: paste [`docs/claude-md-snippet.md`](docs/claude-md-snippet.md) into your `CLAUDE.md`
to make the workflow automatic.

### Option C -- any other tool or model

Cursor, Windsurf, Copilot, a raw LLM or the API — the skills are plain `SKILL.md` files you load as
context. See [INSTALL.md](INSTALL.md).

## Use

- **A screen or app UI** -> invoke the `antislop-web` skill. Generate `DESIGN.md`, build against
  it, run the pre-flight.
- **A presentation** -> ask for a deck and the **Presentation Architect** agent takes it
  end-to-end, or invoke `antislop-decks` directly.
- **A document** -> ask for the document and the **Document Architect** agent takes it
  end-to-end, or invoke `antislop-docs` directly.

Decks and documents **inherit** the client's `DESIGN.md` (the same brand in another medium), so
generate the web design system first when a project spans several media.

## Repository layout

```
anti-slop-design-skills/
├── skills/
│   ├── antislop-web/SKILL.md
│   ├── antislop-decks/SKILL.md
│   └── antislop-docs/SKILL.md
├── agents/
│   ├── presentation-architect.md
│   └── document-architect.md
├── reference/            design-vocabulary.md, ui-checklist.md
├── docs/                 how-it-works.md, claude-md-snippet.md
├── .claude-plugin/       plugin.json, marketplace.json
├── install.sh / install.ps1
├── LICENSE  NOTICE  CHANGELOG.md
```

## What this is not

- Not a theme or component library. It ships discipline, not colors or components.
- Not a guarantee of conversion or of a correct argument. Brief and content still rule.
- Not for a "deck" that is really a document (or vice versa). The agents route you to the right
  medium.

## License

MIT -- see [LICENSE](LICENSE). Lineage and attribution in [NOTICE](NOTICE).
