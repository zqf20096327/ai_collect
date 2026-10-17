# Entrepreneur Claude Skills

Production-ready skill packages for Claude Code and AI coding agents. The best-of-the-best skills for building, growing, and scaling a business — curated by a founder who uses AI to run his own company.

**24 skills across 6 categories** | **Built for founders, by a founder** | **Works with Claude Code, Cursor, Windsurf, and more**

> **Free Playbook:** [The AI Founder's Playbook](https://www.mattwarren.co/ai-founder-playbook/) — How to launch a product in a weekend using these skills. Step-by-step, idea to live product in 48 hours. [Get it free →](https://www.mattwarren.co/ai-founder-playbook/)

## Why This Exists

Most AI skill collections are written by prompt engineers. These are written by someone who actually runs a CPG brand, builds software products, and does his own marketing with Claude Code every day. Every skill here solves a real problem I've faced as a founder.

## Categories

### Marketing & Growth (5 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [copywriting](skills/marketing-growth/copywriting/) | Direct response copy, landing pages, ads, and email sequences using proven frameworks (PAS, AIDA, BAB) | ✅ Ready |
| [seo-content](skills/marketing-growth/seo-content/) | SEO blog posts, keyword research, meta descriptions, and content calendars that rank | ✅ Ready |
| [email-campaigns](skills/marketing-growth/email-campaigns/) | Welcome sequences, launch campaigns, re-engagement flows, and segmentation strategy | ✅ Ready |
| [social-media](skills/marketing-growth/social-media/) | Platform-native content for Twitter/X, LinkedIn, and Instagram with scheduling | ✅ Ready |
| [paid-ads](skills/marketing-growth/paid-ads/) | Meta Ads, Google Ads creative and copy. A/B test variants and performance analysis | ✅ Ready |

### Sales & Revenue (4 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [offer-creation](skills/sales-revenue/offer-creation/) | Build irresistible offers using Alex Hormozi's value equation and $100M Offers framework | ✅ Ready |
| [cold-outreach](skills/sales-revenue/cold-outreach/) | Cold email, LinkedIn DMs, and personalized outreach sequences that get replies | ✅ Ready |
| [pricing-strategy](skills/sales-revenue/pricing-strategy/) | Value-based pricing, tiered offers, anchoring, and price sensitivity analysis | ✅ Ready |
| [objection-handling](skills/sales-revenue/objection-handling/) | Sales objection scripts, FAQ generation, and trust-building content | ✅ Ready |

### Product & Strategy (4 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [market-research](skills/product-strategy/market-research/) | TAM/SAM/SOM analysis, customer interviews, survey design, and market sizing | ✅ Ready |
| [competitive-analysis](skills/product-strategy/competitive-analysis/) | Competitor teardowns, SWOT analysis, positioning maps, and differentiation strategy | ✅ Ready |
| [product-market-fit](skills/product-strategy/product-market-fit/) | PMF surveys, Sean Ellis test, retention analysis, and pivot frameworks | ✅ Ready |
| [landing-pages](skills/product-strategy/landing-pages/) | High-converting landing page wireframes, copy, and CRO recommendations | ✅ Ready |

### Operations & Systems (4 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [sop-builder](skills/operations/sop-builder/) | Standard operating procedures from scratch — document any repeatable process | ✅ Ready |
| [hiring-playbook](skills/operations/hiring-playbook/) | Job descriptions, interview scorecards, take-home assignments, and evaluation rubrics | ✅ Ready |
| [automation-workflows](skills/operations/automation-workflows/) | Identify automation opportunities and design workflows for Zapier, Make, or n8n | ✅ Ready |
| [delegation-framework](skills/operations/delegation-framework/) | Task audit, delegation matrices, and handoff documentation | ✅ Ready |

### Finance & Fundraising (4 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [financial-modeling](skills/finance/financial-modeling/) | Revenue forecasts, expense modeling, cash flow projections, and scenario analysis | ✅ Ready |
| [pitch-deck](skills/finance/pitch-deck/) | Investor pitch deck structure, narrative arc, and slide-by-slide content | ✅ Ready |
| [unit-economics](skills/finance/unit-economics/) | CAC, LTV, payback period, contribution margin, and break-even analysis | ✅ Ready |
| [fundraising](skills/finance/fundraising/) | Fundraising strategy, investor targeting, term sheet analysis, and SAFE/convertible notes | ✅ Ready |

### Leadership & Mindset (3 skills)
| Skill | Description | Status |
|-------|-------------|--------|
| [decision-frameworks](skills/leadership/decision-frameworks/) | Structured decision-making using reversibility analysis, weighted scoring, and pre-mortems | ✅ Ready |
| [founder-productivity](skills/leadership/founder-productivity/) | Time audits, energy management, deep work scheduling, and priority frameworks | ✅ Ready |
| [team-building](skills/leadership/team-building/) | Culture documents, team charters, 1-on-1 templates, and feedback frameworks | ✅ Ready |

## Installation

### Method 1: Claude Code Plugin (Recommended)

```bash
/plugin marketplace add mfwarren/entrepreneur-claude-skills
```

### Method 2: npx Skills CLI

```bash
npx skills add mfwarren/entrepreneur-claude-skills
```

### Method 3: Individual Skill Install

```bash
# Install just the skills you need
npx skills add mfwarren/entrepreneur-claude-skills --skill copywriting
npx skills add mfwarren/entrepreneur-claude-skills --skill offer-creation
```

### Method 4: Universal AI Agent Installer

```bash
# Works with Claude Code, Cursor, Windsurf, VS Code + Copilot, and more
npx ai-agent-skills install mfwarren/entrepreneur-claude-skills
```

### Method 5: Git Clone

```bash
git clone https://github.com/mfwarren/entrepreneur-claude-skills.git
cp -r entrepreneur-claude-skills/skills/* ~/.claude/skills/
```

### Method 6: Git Submodule

```bash
# Add to an existing project for version-controlled skills
git submodule add https://github.com/mfwarren/entrepreneur-claude-skills.git .claude/skills/entrepreneur
```

## Usage

Once installed, skills activate automatically based on your requests:

```
You: "Write a cold email sequence for my SaaS product"
→ cold-outreach skill activates

You: "Analyze my unit economics — CAC is $45, LTV is $380"
→ unit-economics skill activates

You: "Create an irresistible offer for my coaching program"
→ offer-creation skill activates

You: "Build an SOP for our customer onboarding process"
→ sop-builder skill activates
```

## Skill Format

Every skill uses a consistent structure:

```
skills/category/skill-name/
├── SKILL.md          # Core skill file (YAML frontmatter + prompts)
├── README.md         # Skill documentation and examples
├── examples/         # Example inputs and outputs
└── references/       # Frameworks, templates, supporting material
```

### SKILL.md Frontmatter

```yaml
---
name: skill-name
version: 1.0.0
category: Marketing & Growth
domain: copywriting
author: Matt Warren
license: MIT
status: production
updated: 2026-02-07
activation_triggers:
  - "write copy"
  - "landing page copy"
  - "sales page"
tools: []
---
```

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on submitting skills.

**Skill ideas welcome!** Open an issue describing the entrepreneurship skill you'd like to see.

## About

Built by [Matt Warren](https://mattwarren.co) — founder, engineer, and AI-first operator. I use Claude Code to run my business daily and these skills reflect real workflows, not theoretical prompts.

- Blog: [mattwarren.co](https://mattwarren.co)
- Twitter/X: [@matt_warren](https://x.com/matt_warren)
- GitHub: [@mfwarren](https://github.com/mfwarren)

## Stay Updated

New skills, workflows, and founder-tested AI strategies — delivered weekly.

**[Subscribe to the newsletter →](https://www.mattwarren.co/ai-founder-playbook/)**

## License

MIT — use these skills however you want.
