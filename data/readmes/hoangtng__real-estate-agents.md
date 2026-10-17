<p align="center">
  <img src="banner.svg" alt="Real Estate Agents — A complete AI real estate agency" width="100%"/>
</p>

# 🏡 Real Estate Agency — AI Agent Division

> A complete real estate agency in two parts: **12 AI agent personas** (the team) + **12 production skills** (the deliverables they produce). Built as a vertical extension of [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents).

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"/></a>
  <a href="#-the-agents"><img src="https://img.shields.io/badge/Agents-12-blue.svg" alt="12 Agents"/></a>
  <a href="#%EF%B8%8F-the-skills"><img src="https://img.shields.io/badge/Skills-12-purple.svg" alt="12 Skills"/></a>
  <a href="#-contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"/></a>
  <a href="https://github.com/hoangtng/real-estate-agents/stargazers"><img src="https://img.shields.io/github/stars/hoangtng/real-estate-agents?style=social" alt="GitHub stars"/></a>
</p>

---

## 🎬 See It In Action

<p align="center">
  <img src="demo.svg" alt="Demo: Claude generating a CMA using the Market Analyst agent" width="100%"/>
</p>

> *Above: Claude using the **CMA Generator** skill with the **Market Analyst** agent — pulling comparables, recommending price tiers, then chaining into the next skill in the workflow. All animated, all real output from the repo.*

---

## 🧩 Agents vs. Skills — What's the Difference?

| | **Agents** | **Skills** |
|---|---|---|
| **What it is** | A persona Claude becomes | A deliverable Claude produces |
| **Format** | `agents/realestate-*.md` (system prompt) | `skills/*/SKILL.md` (workflow) |
| **Example** | "Be Marcus the Listing Agent" | "Generate a complete CMA" |
| **When triggered** | You invoke a persona | Claude auto-triggers based on context |
| **Output** | Conversational expertise | Structured document |

Use agents when you want **expertise**. Use skills when you want a **deliverable**.

---

## 🚀 Quick Install

### Clone the repo
```bash
git clone https://github.com/hoangtng/real-estate-agents.git
cd real-estate-agents
```

### Install agents (Claude Code or Claude.ai)
```bash
cp agents/realestate-*.md ~/.claude/agents/
```

### Install skills (Claude Code only)
```bash
cp -r skills/*/  ~/.claude/skills/
```

### Activation
```bash
# Agent activation (explicit)
Use the Listing Agent to help me prepare a presentation for 14 Ashford Terrace.

# Skill activation (automatic — Claude detects the task)
Generate a CMA for 14 Ashford Terrace, 4BD/3BA, 2400SF, Pacific Heights.
```

---

## 🎭 The Agents

| # | Agent | Character | Best For |
|---|-------|-----------|----------|
| 1 | 🤝 Client Relationship Manager | **Alexandra** | Client trust and retention |
| 2 | 🏠 Listing Agent | **Marcus** | Pricing strategy and seller management |
| 3 | 🔑 Buyer's Agent | **Priya** | Needs analysis and offer strategy |
| 4 | 📋 Transaction Coordinator | **Chen** | Contract-to-close compliance |
| 5 | 📊 Market Analyst | **Nadia** | CMAs and investment modeling |
| 6 | 🎨 Creative Director | **Isabelle** | Listing marketing campaigns |
| 7 | 🔢 Estimator & SOW Specialist | **Derek** | Scoping and pricing engagements |
| 8 | 💰 Investment Advisor | **Rajan** | Underwriting and BRRRR analysis |
| 9 | 🎯 Business Development Director | **Leo** | Listing presentations and prospecting |
| 10 | 🏢 Property Manager | **Sandra** | Rental property operations |
| 11 | 🧳 Concierge & Relocation Specialist | **Claire** | Welcome packages and orientation |
| 12 | ⚖️ Legal & Compliance Advisor | **Thomas** | Disclosure and fair housing |

Each agent is a fully realized character with personality, critical rules, deliverable templates, workflow process, and success metrics. See individual files in `agents/` for full profiles.

---

## 🛠️ The Skills

Each skill takes raw input (property details, buyer profile, market context) and produces a structured, professional deliverable.

| # | Skill | Folder | What It Produces |
|---|-------|--------|-----------------|
| 1 | 📊 CMA Generator | `skills/cma-generator/` | Full comparative market analysis with 3-tier pricing |
| 2 | ✍️ Listing Description Writer | `skills/listing-description-writer/` | Story-first MLS copy and headlines |
| 3 | 🎯 Offer Strategy Builder | `skills/offer-strategy-builder/` | Complete offer brief with contingency guidance |
| 4 | 📋 Transaction Timeline Manager | `skills/transaction-timeline-manager/` | Dated milestone tracker through close |
| 5 | 💰 Investment Property Underwriter | `skills/investment-property-underwriter/` | NOI, cap rate, BRRRR, and STR models |
| 6 | 🎨 Property Marketing Plan | `skills/property-marketing-plan/` | Marketing plan with photography brief |
| 7 | 🏢 Tenant Screening Report | `skills/tenant-screening-report/` | Criteria, scorecard, adverse action notice |
| 8 | 🧳 Relocation Welcome Package | `skills/relocation-welcome-package/` | Personalized neighborhood guide |
| 9 | 🔢 Scope of Work Generator | `skills/scope-of-work-generator/` | Itemized SOW with change-order policy |
| 10 | 📈 Market Report Generator | `skills/market-report-generator/` | Neighborhood report with absorption rate |
| 11 | ⚖️ Compliance Audit | `skills/compliance-audit/` | Disclosure checklist and fair housing review |
| 12 | 🏆 Listing Presentation Builder | `skills/listing-presentation-builder/` | Full presentation script with objection handlers |

### How Skills Trigger

Skills auto-activate when Claude detects a relevant task. You don't need to name the skill explicitly — natural-language requests work:

| You say | Skill activated |
|---------|----------------|
| "What's this house worth?" | CMA Generator |
| "Write a listing description for this property" | Listing Description Writer |
| "How should I structure an offer?" | Offer Strategy Builder |
| "Build me a closing timeline" | Transaction Timeline Manager |
| "Does this rental property pencil?" | Investment Property Underwriter |
| "Plan the launch for this listing" | Property Marketing Plan |
| "Should I approve this tenant?" | Tenant Screening Report |
| "Make a welcome guide for clients moving to Austin" | Relocation Welcome Package |
| "What goes in our listing agreement?" | Scope of Work Generator |
| "What's the market doing in [neighborhood]?" | Market Report Generator |
| "Check this listing copy for fair housing issues" | Compliance Audit |
| "Help me prep for tomorrow's listing presentation" | Listing Presentation Builder |

---

## 🔄 Real-World Workflows

### New Listing Engagement
```
Estimator      →  SOW + fee agreement                      [Skill: scope-of-work-generator]
Market Analyst →  CMA + pricing recommendation             [Skill: cma-generator]
Business Dev   →  Listing presentation prepared            [Skill: listing-presentation-builder]
Listing Agent  →  Property description + pricing strategy  [Skill: listing-description-writer]
Creative Dir.  →  Marketing plan + photography brief       [Skill: property-marketing-plan]
Compliance     →  Disclosure checklist + fair housing review [Skill: compliance-audit]
Transaction Co.→  Contract-to-close timeline built         [Skill: transaction-timeline-manager]
Client Mgr     →  Weekly seller updates through close      (Agent)
```

### Buyer Representation
```
Buyer's Agent     →  Needs analysis + tour shortlist                 (Agent)
Market Analyst    →  Property valuation + neighborhood report        [Skill: market-report-generator]
Buyer's Agent     →  Offer strategy brief                            [Skill: offer-strategy-builder]
Transaction Co.   →  Contract-to-close timeline                      [Skill: transaction-timeline-manager]
Concierge         →  Welcome package + community orientation         [Skill: relocation-welcome-package]
Client Mgr        →  Post-close follow-up + referral cultivation     (Agent)
```

### Investment Property Acquisition
```
Investment Advisor →  Underwriting + deal verdict                    [Skill: investment-property-underwriter]
Market Analyst     →  Rental comps + rent growth projections         [Skill: market-report-generator]
Buyer's Agent      →  Investment-grade offer strategy                [Skill: offer-strategy-builder]
Transaction Co.    →  Contract-to-close                              [Skill: transaction-timeline-manager]
Property Manager   →  Tenant placement + management setup            [Skill: tenant-screening-report]
Compliance         →  Entity structure coordination                  [Skill: compliance-audit]
```

---

## 📂 Repository Structure

```
real-estate-agents/
├── README.md
├── LICENSE
│
├── agents/
│   ├── realestate-business-development.md
│   ├── realestate-buyers-agent.md
│   ├── realestate-client-relationship-manager.md
│   ├── realestate-concierge-relocation.md
│   ├── realestate-creative-director.md
│   ├── realestate-estimator-sow.md
│   ├── realestate-investment-advisor.md
│   ├── realestate-legal-compliance.md
│   ├── realestate-listing-agent.md
│   ├── realestate-market-analyst.md
│   ├── realestate-property-manager.md
│   └── realestate-transaction-coordinator.md
│
└── skills/
    ├── cma-generator/SKILL.md
    ├── compliance-audit/SKILL.md
    ├── investment-property-underwriter/SKILL.md
    ├── listing-description-writer/SKILL.md
    ├── listing-presentation-builder/SKILL.md
    ├── market-report-generator/SKILL.md
    ├── offer-strategy-builder/SKILL.md
    ├── property-marketing-plan/SKILL.md
    ├── relocation-welcome-package/SKILL.md
    ├── scope-of-work-generator/SKILL.md
    ├── tenant-screening-report/SKILL.md
    └── transaction-timeline-manager/SKILL.md
```

---

## 🧩 Agent Format

Every agent file follows this structure:

```markdown
---
name: [Role Name]
description: [One-sentence summary for agent discovery]
color: [UI color tag]
---

# [Emoji] [Role Name]

## Identity & Memory      ← Named character with voice and philosophy
## Core Mission           ← What success looks like
## Critical Rules         ← The non-negotiables (5–8 items)
## Technical Deliverables ← Production-ready templates
## Workflow Process       ← Step-by-step in practice
## Success Metrics        ← Measurable outcomes
```

## 🛠️ Skill Format

Every skill follows this structure:

```markdown
---
name: [skill-name]
description: [Triggering description — when to activate]
---

# [Skill Name]

## What You Need From the User
## Output Format            ← Structured deliverable template
## Behavior Notes           ← Edge cases and rules
```

---

## 🤝 Contributing

PRs welcome. To add:

**A new agent:**
1. Follow the agent format above
2. File: `agents/realestate-[role-name].md`
3. Give them a name, not just a job title
4. Include at least one production-ready deliverable template

**A new skill:**
1. Folder: `skills/[skill-name]/`
2. File inside: `SKILL.md`
3. Include a triggering description that's specific about when to activate
4. Provide a full output format template

**Ideas for new additions:** Mortgage Advisor · Home Stager · Escrow Officer · HOA Specialist · Commercial Leasing Agent · Luxury Auction Specialist · 1031 Exchange Coordinator · Open House Planner skill · Net Sheet Calculator skill

---

## ⭐ Star this repo

If this saves you time, **star the repo** — it helps other agents and developers find it.

---

## 📜 License

MIT — use freely, adapt for your market, contribute back.

---

*Built as a real estate vertical for [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents). Same design philosophy, same quality bar.*
