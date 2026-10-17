# Brand Social Media Skill — Claude Code

> Research, audit, compete, and publish. A complete social media intelligence and content production system for any brand, built as a Claude Code skill.

---

## What It Does

This Claude Code skill is a three-mode social media system:

| Mode | Command | What it produces |
|------|---------|-----------------|
| **Calendar** | `/social-calendar` | Full monthly content calendar for any platforms you choose |
| **Audit** | `/social-audit` | Scored audit report of your brand's existing social channels |
| **Competitor Intel** | `/competitor-audit` | Competitor comparison matrix + content gap analysis |
| **Full Suite** | `/social-suite` | All three — audit and competitive intel inform the calendar |

Unlike generic AI content tools, this skill:
- **Researches before it writes** — uses live Reddit, X, and web data to understand what your ICP is actually talking about this month
- **Audits before it recommends** — scores your existing channels before suggesting what to post
- **Studies competitors before it positions** — maps what competitors are and aren't doing before deciding what angles to own
- **Writes platform-native content** — not the same caption at different lengths, but genuinely different content written for each platform's audience, algorithm, and format norms

---

## Platform Coverage

You choose which platforms you need. The skill produces fully platform-native content for all of them:

| Platform | Content types produced |
|----------|----------------------|
| **LinkedIn** | Static posts, carousels (with slide-by-slide copy), short video, text-only posts |
| **X (Twitter)** | Short takes, threads, image posts with text overlay |
| **Instagram Feed** | Static posts, carousels |
| **Instagram Reels** | Short-form video scripts with VO, on-screen text, and trending audio notes |
| **Instagram Stories** | Frame-by-frame story plans with interactive element direction (polls, questions, countdowns) |
| **Facebook** | Feed posts, native video captions |
| **TikTok** | TikTok-native scripts — 0-second hook, on-screen text, trending audio notes, Duet/Stitch flags, comment-bait endings |
| **YouTube Shorts** | Shorts scripts with SEO-optimised titles and descriptions |
| **YouTube Long-form** | Full video spec: SEO title, thumbnail brief, description, chapters, tags, end screens, cards |
| **Threads** | Conversational posts and short thread series |
| **Pinterest** | Pin titles, keyword-rich descriptions, board strategy, link targets |
| **Reddit** | Value-first community posts per subreddit — practitioner tone, never promotional |

Every platform follows its own rules — audience mindset, algorithm behaviour, caption length, format norms, hashtag strategy, and optimal posting time.

---

## What Each Output Includes

### Calendar Output (Mode A)

For every post across all selected platforms:

| Element | What it is |
|---------|-----------|
| Hook | Scroll-stopping opening line — never starts with the brand name |
| Post Copy | Full creative copy — what goes on the image, slide, or screen |
| Carousel Slides | Slide-by-slide text content for carousel posts |
| Video Script | Timestamped production script ready for AI video tools |
| TikTok Script | TikTok-native script with 0-second hook, trending audio notes, Duet/Stitch flags |
| YouTube Spec | SEO title, thumbnail brief, description, chapters, tags, end screen CTA |
| Stories Plan | Frame-by-frame plan with interactive element direction per frame |
| Meme Concept | Meme format name + panel-by-panel description brief for the design team |
| Visual Direction | Design brief — background, layout, composition, brand element placement |
| Platform Caption | Written natively per platform's audience and tone rules |
| Hashtags | Platform-appropriate selection (quantity and type varies by platform) |
| CTA | Specific call to action for this post |
| Best Time | Optimal posting time for this platform |

All content lands in a styled `.xlsx` file with:
- **Overview sheet** — monthly narrative, pillar breakdown, colour legend
- **Full Calendar sheet** — all posts across all platforms in one scrollable view
- **Per-platform sheets** — one sheet per selected platform
- **Videos sheet** — all video/reel scripts in wide-format for easy reading
- **Week 1–4 sheets** — content per week for team handoff

### Audit Output (Mode B)

For each of your brand's active social channels:

- Profile health score (bio, banner, link, pinned content)
- Posting frequency — actual vs recommended for the platform
- Content mix breakdown — % by format (static / carousel / video / stories)
- Estimated engagement rate — benchmarked as Excellent / Good / Average / Poor
- Best performing content patterns — what your top posts have in common
- Worst performing content patterns — what your low-engagement posts have in common
- Hook quality rating — are your opening lines actually stopping scrolls?
- CTA analysis — are you asking for action?
- Visual consistency rating — do you look like one brand across all channels?
- Cross-posting detection — original content or copy-pasted from another channel?
- 3 priority recommendations per platform
- Overall social health score out of 100 with a ranked action plan

Saved as: `[Brand]-Social-Audit-[Date].md`

### Competitor Intelligence Output (Mode C)

- Competitor discovery — finds competitors automatically if you don't provide them
- Per-platform comparison matrix — followers, posting frequency, engagement rate, formats, tone
- What's working for each competitor — their best content types and why they land
- What's not working — common failures across the competitive set
- Whitespace opportunities — content angles, formats, tones, and platforms nobody is owning
- Recommended competitive positioning — content, tone, platform, and format strategy
- 30-day competitive action plan — week-by-week priorities

Saved as: `[Brand]-Competitor-Intel-[Date].md`

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| **Claude Code** | Any plan — claude.ai/code |
| **Python 3.8+** | For running the generated calendar build script |
| **openpyxl** | `pip install openpyxl` |
| **/last30days skill** | Optional but strongly recommended — adds live Reddit, X, and YouTube research data to Mode A Phase 3. Without it, Phase 3 falls back to WebSearch only. |

---

## Installation

**Step 1 — Clone this repo**

```bash
git clone https://github.com/[username]/social-calendar-skill.git
```

**Step 2 — Copy the skill file to Claude Code**

```bash
# macOS / Linux
mkdir -p ~/.claude/skills/social-calendar-skill
cp social-calendar-skill/SKILL.md ~/.claude/skills/social-calendar-skill/SKILL.md

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\social-calendar-skill"
Copy-Item "social-calendar-skill\SKILL.md" "$env:USERPROFILE\.claude\skills\social-calendar-skill\SKILL.md"
```

**Step 3 — Install Python dependency**

```bash
pip install openpyxl
```

**Step 4 — Verify**

Open Claude Code and type `/social-calendar`. If the skill is installed, Claude will ask for your brand details and begin.

---

## Quick Start

**Build a monthly calendar:**
```
/social-calendar Stripe June 2026
```
Claude asks which platforms you want, researches the community, presents a narrative brief for your approval, then builds the full calendar and saves the Excel file.

**Audit your social channels:**
```
/social-audit Stripe
```
Claude discovers which platforms Stripe is on, studies each one, and delivers a scored audit report.

**Analyse competitors:**
```
/competitor-audit Stripe
```
Claude identifies Stripe's competitors, studies their social channels, and produces a gap analysis with whitespace opportunities.

**Run everything together:**
```
/social-suite Stripe June 2026
```
Runs Audit → Competitor Intel → Calendar in sequence. The calendar is informed by what the audit found and what competitors are missing.

---

## More Invocation Examples

```
# Calendar — specify platforms
/social-calendar Figma August 2026 — LinkedIn and TikTok only this month
/social-calendar Linear June 2026 — ICP is senior engineers, skip Facebook and Pinterest

# Calendar — specify ICP
/social-calendar Vercel June 2026 — ICP is platform engineers and DevOps leads at scale-ups

# Audit — specify focus
/social-audit Webflow — I think we're underperforming on Instagram specifically

# Competitor intel — provide competitors
/competitor-audit Vercel — competitors are Netlify, Railway, and Render
/competitor-audit Notion — focus on the productivity and PKM space

# Full suite
/social-suite Loom June 2026
```

---

## How Each Mode Works

### Mode A — Calendar Build

**Phase 1: Brand Study**
Reads the brand website (homepage + up to 5 sub-pages) and all selected social profiles. Extracts USPs, product pillars, key terminology, ICP signals, tone of voice, and current content performance per platform.

**Phase 2: Keyword Extraction**
Pulls primary keywords, pain point language, competitor names, and ICP role keywords from the brand study.

**Phase 3: Community Research**
Uses `/last30days` to run 4 targeted queries across Reddit, X, YouTube, and the web — finding what the ICP is actively struggling with, what's trending in the industry, and how competitors are being talked about this month.

**Phase 4: Narrative Brief** *(the only approval gate)*
Synthesises everything into a strategic foundation: what the community is talking about, key pain points surfaced, how the brand responds, the recommended monthly narrative, 3–4 content pillars, tone guidance, platform-specific strategy notes, and suggested content mix. **You review and approve this before a single post is written.**

**Phase 5: Calendar Build**
Writes all content pieces for all selected platforms following platform-native rules. Generates the Python build script, runs it, and delivers the styled Excel file.

---

### Mode B — Social Media Audit

1. Discovers the brand's active social channels via WebSearch
2. Confirms the channel list with the user
3. Studies each channel: profile completeness, posting frequency, content mix, engagement rate estimates, hook quality, visual consistency, cross-posting detection
4. Identifies the top 3 performing and bottom 3 performing post patterns per platform
5. Scores each channel out of 100 and produces a prioritised action plan
6. Saves the full audit report as a Markdown file

---

### Mode C — Competitor Intelligence

1. Discovers 3–6 competitors via WebSearch (or uses a provided list)
2. Confirms the competitor list with the user before proceeding
3. Studies each competitor's social channels across relevant platforms
4. Builds a per-platform comparison matrix
5. Identifies what's working, what's failing, and what nobody is doing
6. Produces whitespace opportunity rankings and a competitive positioning strategy
7. Saves the intelligence report as a Markdown file

---

### Mode D — Full Suite

Runs B → C → A in sequence. The narrative brief in Phase 4 of Mode A explicitly incorporates:
- Weaknesses found in the audit → areas to improve this month
- Gaps identified from competitors → angles to own this month
- Best-performing formats from the audit → formats to double down on

This is the most powerful way to run the skill — the calendar is not just community-research-informed but also audit-informed and competition-aware.

---

## Platform Rules — What Makes This Different

Most social media tools treat platforms as distribution channels for the same content. This skill doesn't.

**LinkedIn** — First 3 lines visible before "see more" — the hook is everything. External links always go in comments (the algorithm penalises links in post body). 2–3 hashtags at the very end. Carousel documents (PDFs) get the highest saves. Posting frequency: 3–5x per week.

**X (Twitter)** — Under 200 characters for retweetability. Zero to one hashtag — more than that tanks reach. Threads for depth: first tweet stands alone as a hook, each subsequent tweet = one idea. Ends with a question or provocation to drive replies. Never automated cross-posts from LinkedIn — wrong tone entirely.

**Instagram Reels** — Hook text on screen within the first 1 second. Most Reels are watched without sound — text overlays are not optional. Trending audio noted for the editor to select at production time. Under 30 seconds for most brand content.

**TikTok** — First spoken word at second 0. No silent intros. No slow logo builds. Creator-native feel — polished corporate content fails. Every script ends with a comment-bait line ("Comment X if you want part 2"). Duet and Stitch opportunities flagged. Optimal length: 15–45 seconds for B2B.

**YouTube** — Title written for search, not just for viewers. Thumbnail brief provided for designers. Chapters always included. First 2 lines of description visible in search results — written for click-through, not just description.

**Pinterest** — This is a search engine, not a social feed. Descriptions are keyword-rich for SEO. Every pin links somewhere. Vertical 2:3 format. Volume matters more than on any other platform (5–15 pins per day).

**Reddit** — Community engagement channel, not a publishing channel. Never pitch directly. Brand mentioned only in comments if directly relevant. Written like a practitioner who works at the brand — not a marketer who works for it.

---

## Repo Structure

```
social-calendar-skill/
├── SKILL.md                              ← The skill file — install this into Claude Code
├── README.md                             ← This file
├── scripts/
│   └── build_calendar_template.py       ← Annotated example of the generated build script
├── examples/
│   └── narrative-brief-example.md       ← Sample Phase 4 narrative brief output
├── requirements.txt
└── .gitignore
```

---

## Troubleshooting

**Skill isn't triggering**
The file must be at `~/.claude/skills/social-calendar-skill/SKILL.md`. The subdirectory name is required — Claude Code loads skills from named subdirectories inside `~/.claude/skills/`.

**Python script fails with a codec error on Windows**
Run with the UTF-8 flag: `PYTHONUTF8=1 python3 build_calendar.py`

**Excel file can't be saved (PermissionError)**
The file is open in Excel. Close it and re-run the script.

**Phase 3 community research feels shallow**
Install the `/last30days` skill. Without it, Phase 3 falls back to WebSearch only, missing Reddit thread data, X engagement signals, and YouTube content.

**Audit can't find engagement metrics**
The skill works from publicly visible data only. For impression counts, reach, click-through rates, and follower growth trends, pull your native platform analytics (LinkedIn Analytics, X Analytics, Instagram Insights, TikTok Creator Center) and share the key numbers — Claude will incorporate them into the audit.

**Competitor list is wrong**
The skill always asks you to confirm the competitor list before Phase C2 starts. Never proceeds without confirmation.

---

## Requirements

```
Python >= 3.8
openpyxl >= 3.1.0
```

---

## Contributing

Pull requests welcome. Areas where contributions are most valuable:

- **Industry-specific variants** — a version tuned for SaaS, ecommerce, DTC, agency, or creator brands
- **Additional platform profiles** — Snapchat, BeReal, Discord, WhatsApp Channels, Telegram
- **Audit scoring refinements** — better engagement rate benchmarks per industry
- **Competitor discovery improvements** — better WebSearch queries for specific industries

---

## License

MIT — use it, fork it, build on it.
