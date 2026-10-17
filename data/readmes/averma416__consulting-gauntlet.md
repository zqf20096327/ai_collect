# Consulting Gauntlet — Claude Code Skill

A full-stack consulting engagement skill for Claude Code. Drop in a business question and get McKinsey/Bain/BCG-quality output: sourced, framework-driven, financially rigorous, and executive-ready.

---

## Install

Download [`consulting-gauntlet.skill`](./consulting-gauntlet.skill) and drag it into Claude Code's skill settings.

That's it. No `/` commands needed — just describe your engagement naturally. I would recommend dividing the engagement problem into parts and then using this skill to prepare documents for each part to have richer research done by the agents.

---

## How to Use

Start a session in Claude Code and describe what you need:

```
Run a consulting engagement on [company / industry / question]
```

Or be more specific:

```
Market entry analysis for EV charging infrastructure in Southeast Asia
Competitive strategy review for a mid-market SaaS company
Business case for vertical integration in our supply chain
Due diligence on a Series B fintech acquisition target
Build a 5-year financial model for a D2C healthcare brand
```

The skill handles the rest — scoping, agent deployment, sourcing, frameworks, and file output.

---

## The Team

Six specialized agents work every engagement:

### Partner
The executive voice. Owns the narrative, the "so what," and the impact framing. Uses Pyramid Principle structure and BLUF (Bottom Line Up Front) communication. Sets the working hypothesis before any work begins and signs off on the final deliverable.

### Manager
Quality control. Reviews every claim, every number, every citation before anything ships. Flags hallucinations with `[HALLUCINATION RISK]`, unsourced claims with `[CITATION NEEDED]`, and runs a pre-publication checklist. Nothing leaves without a Manager pass.

### Financial Analyst
CPA-level rigor. Builds DCF models, trading comps, unit economics (LTV/CAC), multi-year P&L projections, break-even analysis, and sensitivity tables. All figures are inflation-adjusted by default. Every assumption is sourced or explicitly labeled.

### Tech Specialist
Technology expert for the relevant industry. Maps the technology landscape, assesses disruption vectors using the Gartner Hype Cycle, applies Crossing the Chasm analysis, and links technology dynamics to cost structure and competitive moat.

### Strategist
Knows and applies 16 strategy frameworks — picks the right ones for the engagement, fills them in completely, and always ends with a "so what" and a recommendation:

- Porter's Five Forces
- VRIO
- AFI Framework
- Strategic Positioning & Productivity Frontier
- Differentiation & Cost Leadership (Generic Strategies)
- PESTLE
- CAGE
- Value Chain Analysis
- Value Creation & Capture
- Business Model Archetypes
- Network Effects
- Industry Life Cycle
- Crossing the Chasm
- Buy-Borrow-Build
- Vertical Integration
- Cost-Responsiveness Framework

### Associate
Source engine and fact-checker. Finds and vets every source before any claim enters a deliverable. Enforces a 4-tier credibility system and prohibits low-quality sources entirely.

---

## Source Credibility System

| Tier | Examples |
|------|----------|
| **TIER-1** | Peer-reviewed journals (Nature, AER, Journal of Finance, IEEE) |
| **TIER-2** | McKinsey, BCG, Bain, Gartner, Forrester, IDC, IMF, World Bank, SEC filings |
| **TIER-3** | FT, WSJ, Bloomberg, The Economist, Reuters |
| **TIER-4** | Trade press — used with corroboration only |
| **PROHIBITED** | Reddit, anonymous blogs, unattributed stats, Wikipedia as primary |

Every deliverable includes a **Source Index** with credibility ratings and conflict-of-interest flags.

---

## Outputs

Depending on the engagement, the skill produces:

- **Strategy memos** (`.docx`)
- **Financial models** (`.xlsx`)
- **Presentations** (`.pptx`)
- **Executive summaries** (`.pdf`)
- **Source Index** (appended to every deliverable)

---

## Engagement Types

| Type | Agents Deployed |
|------|----------------|
| Market Entry | Strategist, Associate, Financial Analyst |
| Competitive Strategy | Strategist, Tech Specialist, Associate |
| M&A Due Diligence | Financial Analyst, Tech Specialist, Strategist, Associate |
| Full Strategy Review | All 6 agents |
| Business Case | Financial Analyst, Strategist, Associate |
| Go-to-Market | Strategist, Tech Specialist, Associate |
| Technology Assessment | Tech Specialist, Financial Analyst, Associate |

---

## Repo Structure

```
consulting-gauntlet/
├── SKILL.md                        ← skill entry point
├── consulting-gauntlet.skill       ← installable package
├── agents/
│   ├── partner.md
│   ├── manager.md
│   ├── financial-analyst.md
│   ├── tech-specialist.md
│   ├── strategist.md
│   └── associate.md
└── references/
    ├── frameworks.md
    ├── financial-models.md
    ├── engagement-types.md
    └── output-formats.md
```

---

## Contributing

Pull requests welcome. Best contributions:
- New framework additions to `agents/strategist.md`
- Additional financial model templates in `agents/financial-analyst.md`
- Expanded source credibility examples in `agents/associate.md`
- New engagement type templates in `references/engagement-types.md`
