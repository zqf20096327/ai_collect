# 🦞 KOL Ops Suite v3 — Composition Skill for OpenClaw / Claude Code

A modular, composable skill system for managing the full lifecycle of overseas KOL/influencer marketing campaigns.

```
CSV Import → Screen → Outreach → Evaluate → Brief → QC → Monitor → Dashboard → Comments → Review
  Skill 1    Skill 2  Skill 1.5  Skill 3   Skill 4  4.5  Skill 5   Skill 5.5  Skill 6
```

---

## What's New in v3

| Skill | Status | What it does |
|-------|--------|--------------|
| Skill 1 | ✅ Existing | CSV cleaning & health scoring |
| Skill 2 | ✅ Existing | Email outreach tracking & reply detection |
| **Skill 1.5** | 🔄 Updated | Deep evaluation — now with 3-layer data strategy + contract management + 🟡 manual field warnings |
| **Skill 3** | 🆕 New | Brand knowledge base + personalized brief generation per KOL |
| **Skill 4** | 🆕 New | Content QC — script/transcript compliance check + KOL reliability tracking |
| **Skill 4.5** | 🆕 New | Mid-campaign monitor — daily alerts, cross-video patterns, pre-publish brief adjustments |
| Skill 5 | ✅ Existing | Post-campaign analytics dashboard |
| **Skill 5.5** | 🆕 New | Comment analysis — sentiment, purchase intent, SEO/AEO blog topics |
| Skill 6 | ✅ Existing | Strategic review + renewal tiers + next-round brief |

---

## Key Features

### 🟡 Three-Layer Data Strategy (Skill 1.5)
KOL evaluation uses a realistic hybrid approach:
- **YouTube API (auto):** Hard data — views, engagement, follower counts, metadata
- **EasyKOL plugin (manual):** Audience demographics estimate, brand @ mention history
- **Wednesday plugin (manual):** Estimated quote range, CPE/CPV

Fields that require manual plugin input are **highlighted yellow** in the Excel scorecard so nothing gets auto-filled with missing data silently.

Fields that can never be retrieved automatically (audience geography, KOL rates, contract status) are marked `[MANUAL]` and must be filled by the human operator.

### 🧠 Persistent Brand Knowledge Base (Skill 3)
Set up your brand profile once. Every subsequent campaign reuses it. After each campaign, Skill 6 feeds the best-performing content patterns back into `content-templates.md`, so briefs get smarter over time.

### 🔴 Mid-Campaign Adjustments (Skill 4.5)
Don't wait until the campaign is over to learn what's working. Skill 4.5 benchmarks each live video against that KOL's own historical average (not platform benchmarks), generates daily Red/Yellow/Green alerts, and recommends brief adjustments for KOLs who haven't published yet.

### 💬 Comment Intelligence → SEO Topics (Skill 5.5)
Every question in the comments is a search query. Skill 5.5 classifies comments by intent, extracts high-frequency questions, and converts them into a prioritized SEO/AEO blog content calendar.

### 📋 KOL Compliance History (Skill 4)
Every QC review appends to a persistent `kol-compliance-history.md` file. KOLs who consistently hit mandatory elements and never violate red lines get "Reliable Partner" flags. Those with repeat issues get flagged for closer monitoring. This history feeds Skill 6's renewal decisions.

---

## Directory Structure

```
kol-ops-suite/
├── SKILL.md                              # Master orchestrator (9-skill pipeline)
├── README.md                             # This file
├── skill-1-kol-screener/
│   └── SKILL.md
├── skill-1.5-kol-evaluator/
│   └── SKILL.md                          # Updated: 3-layer data + contract mgmt + yellow fields
├── skill-2-outreach-monitor/
│   └── SKILL.md
├── skill-3-brief-generator/
│   └── SKILL.md                          # New
├── skill-4-content-qc/
│   └── SKILL.md                          # New
├── skill-4.5-campaign-monitor/
│   └── SKILL.md                          # New
├── skill-5-data-dashboard/
│   └── SKILL.md
├── skill-5.5-comment-analysis/
│   └── SKILL.md                          # New
├── skill-6-campaign-review/
│   └── SKILL.md
└── references/
    └── analysis-framework.md
```

---

## Installation

Copy the `kol-ops-suite/` folder to your OpenClaw workspace skills directory:

```bash
cp -r kol-ops-suite ~/openclaw/workspace/skills/
```

Add to `AGENTS.md`:
```
When I ask about KOL campaigns, influencer outreach, creator partnerships, campaign analytics, KOL briefs, content QC, or campaign monitoring, read and follow ~/skills/kol-ops-suite/SKILL.md — it contains a 9-skill pipeline for end-to-end KOL marketing operations.
```

---

## Usage Examples

```
"I exported a CSV from NoxInfluencer, screen it"
→ Skill 1

"Check if any KOLs replied to our outreach"
→ Skill 2

"These 8 KOLs are interested. Evaluate them — conversion goal"
→ Skill 1.5 (uses EasyKOL + Wednesday data you enter manually)

"Generate briefs for the 5 KOLs we selected"
→ Skill 3

"[KOL name] submitted their script, check it against the brief"
→ Skill 4

"Check how our live videos are performing"
→ Skill 4.5

"Build a campaign performance dashboard"
→ Skill 5

"What are people saying in the comments? Any blog topics?"
→ Skill 5.5

"How did this campaign go? Renewal recommendations?"
→ Skill 6
```

---

## What This Doesn't Do

This skill suite automates data collection, formatting, scoring, QC flagging, and analysis. It deliberately leaves these to humans:

- Final KOL selection (AI recommends, human decides)
- Rate negotiation (AI tracks, human negotiates)
- Content approval (AI flags issues, human approves)
- Brief sending (AI drafts, human reviews and sends)
- Budget decisions (AI surfaces data, human decides spend)

---

## License

MIT — use it, fork it, improve it.
