# Founder Skills for AI Agents

A collection of **24 AI agent skills** designed for startup founders. Build pitch decks, convert presentations, research investors, monitor competitors, and scale your content — all with AI coding agents like Claude Code, OpenAI Codex, Cursor, and Windsurf.

Part of [UniqueClub](https://uniqueclub.ai) — tools and community for ambitious founders.

Built by [吴畏 (Wu Wei)](https://github.com/wulaosiji). Want hands-on help with your startup? Check out [UniqueClub](https://uniqueclub.ai) for founder resources, pitch reviews, and growth strategies.

**Contributions welcome!** Have a skill idea or improvement? [Open an issue](https://github.com/wulaosiji/founder-skills/issues) or submit a PR.

---

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for founder-specific tasks. When you add these to your project, your agent recognizes when you're working on fundraising, content, or growth — and applies the right frameworks automatically.

All 24 skills have passed a 7-dimension quality audit (100/100): naming, description with trigger keywords, usage boundaries, six-step workflow, output specification, guardrails, and cross-references.

---

## How Skills Work Together

`unique-club-founder-kit` is the navigation layer: use it to choose a workflow, then invoke the task-specific skills. Company context is collected by the selected skill when required; the kit does not create or persist a founder profile.

**Workflow Example:**
1. Start with `unique-club-founder-kit` — choose the fundraising workflow
2. Use a BP planner or framework — decide the story and evidence structure
3. Use `pitch-deck-creator` — generate a 10-slide PPTX from approved company data
4. Use `deck-web-converter` — convert that deck into responsive HTML for sharing
5. Use `investor-research` and `investor-due-diligence` — prioritize the outreach list

---

## Available Skills

### Foundation (1 skill)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [unique-club-founder-kit](skills/unique-club-founder-kit/) | Navigation layer for the complete 24-skill AI founder toolkit across foundation, fundraising, market intelligence, content, and operations. | "AI创业工具包", "founder toolkit", "startup skills", "创业者技能", "工具包导航" |

### Fundraising (10 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [business-plan-ppt](skills/business-plan-ppt/) | Create a professional 18-page Chinese fundraising deck with detailed content and visual specification. White background with navy accents, PPTX or PDF output. | "路演PPT", "商业计划书", "融资方案PPT", "投资备忘录", "BP制作" |
| [pitch-deck-creator](skills/pitch-deck-creator/) | Generate an editable 10-slide PPTX from structured startup JSON using a bundled Python script. Covers problem, solution, business model, traction, team, and funding ask. | "生成pitch deck", "融资PPT", "BP生成", "pitch deck PPTX", "10页融资deck" |
| [deck-web-converter](skills/deck-web-converter/) | Convert PPT/PDF pitch decks into responsive, self-contained HTML for web sharing. Mobile-friendly, fast-loading, shareable via link or QR code. | "BP转网页", "PPT转HTML", "pitch deck online", "把PPT变成网页", "在线演示文稿" |
| [fundraising-bp-planner](skills/fundraising-bp-planner/) | Generate a structured Chinese fundraising BP outline covering six core modules with data-presentation guidance and visualization tips. | "融资BP", "商业计划书", "pitch deck大纲", "理一下融资思路", "准备投资人材料" |
| [investor-pitch-planner](skills/investor-pitch-planner/) | Generate a structured English investor pitch outline covering Problem, Solution, Market, Business Model, Competition, Traction, Team, and Ask. | "pitch deck outline", "融资大纲", "investor presentation", "帮我写pitch deck", "pitch deck framework" |
| [investor-research](skills/investor-research/) | Research VCs, angels, and accelerators. Generate target lists with firm profiles, thesis fit, portfolio, contact strategy, and warm intro paths. | "投资人调研", "找VC", "research investors", "VC list", "融资对象" |
| [investor-due-diligence](skills/investor-due-diligence/) | Rate investors before meeting them. Michelin-style 3-star system based on six dimensions (1-4 scale). Helps founders decide if an investor is worth meeting. | "投资人背调", "查VC", "rate this VC", "投资人评级", "值不值得见" |
| [sequoia-structured-bp](skills/sequoia-structured-bp/) | Sequoia Capital-style 10-12 slide structured BP framework. Data-driven, investor-grade, with slide-by-slide writing guides and checklists. Best for Series A+ and institutional rounds. | "红杉BP", "Sequoia pitch deck", "结构化BP", "数据驱动BP", "A轮融资deck" |
| [yc-insight-driven-bp](skills/yc-insight-driven-bp/) | Y Combinator-style insight-first BP framework. Minimalist 5-8 slides built around a contrarian insight. Best for pre-seed/seed, accelerators, and angels. | "YC BP", "Y Combinator pitch", "洞察驱动BP", "极简BP", "加速器申请" |
| [raskin-narrative-bp](skills/raskin-narrative-bp/) | Andy Raskin-style narrative pitch framework. 5-beat story format for live presentations and Demo Day. Creates urgency through world-level framing, not product-level description. | "Raskin pitch", "叙事BP", "故事驱动pitch", "Demo Day演示", "路演比赛" |

### Which BP Skill Should You Use?

| Need | Recommended skill | Output |
|------|-------------------|--------|
| Generate an editable deck from structured data | `pitch-deck-creator` | 10-slide PPTX; bundled script |
| Design a detailed Chinese financing deck | `business-plan-ppt` | 18-page content and visual specification |
| Plan a Chinese fundraising story before design | `fundraising-bp-planner` | Chinese BP outline |
| Plan an English investor presentation | `investor-pitch-planner` | English pitch outline |
| Prepare for Series A+ or institutional review | `sequoia-structured-bp` | Evidence-led 10-12 slide structure |
| Prepare a Pre-seed/Seed or accelerator pitch | `yc-insight-driven-bp` | Insight-first 5-8 slide structure |
| Prepare a Demo Day or live narrative | `raskin-narrative-bp` | Five-beat presentation narrative |

### Market Intelligence (5 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [competitor-tracker](skills/competitor-tracker/) | Monitor competitor news, product launches, pricing changes, and strategic moves. Track competitive intelligence over time. | "竞品追踪", "监控竞争对手", "competitor tracker", "竞争分析", "竞品动态" |
| [market-intel-brief](skills/market-intel-brief/) | Generate daily/weekly AI and startup industry intelligence briefings with signal tracking and trend analysis for founders. | "市场情报", "行业简报", "market intelligence", "startup news", "AI日报" |
| [market-research-extractor](skills/market-research-extractor/) | Extract and analyze content from multiple platforms for market research and competitive intelligence. Multi-platform content extraction. | "内容抓取", "竞品分析", "市场调研", "内容提取", "competitive research" |
| [social-intelligence](skills/social-intelligence/) | Monitor Twitter/X for competitor activity, industry trends, sentiment shifts, and market signals. Social listening for founders. | "社交监控", "竞品动态", "Twitter监控", "社交情报", "social listening" |
| [china-content-research](skills/china-content-research/) | Research and analyze WeChat articles and Chinese social content for market intelligence. China-specific content research. | "微信公众号研究", "微信文章分析", "中国市场调研", "WeChat research", "China market research" |

### Content Creation (6 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [content-multiplier](skills/content-multiplier/) | Transform one piece of content into multiple platform-optimized formats for different channels. One fish, many meals — cross-posting and repurposing. | "内容放大", "一鱼多吃", "repurposing content", "content distribution", "多平台分发" |
| [founder-content-writer](skills/founder-content-writer/) | Write long-form founder content: blog posts, LinkedIn articles, thought leadership, and technical essays. | "创始人写作", "长文写作", "博客文章", "LinkedIn长文", "thought leadership" |
| [social-post-generator](skills/social-post-generator/) | Create engaging social media posts for LinkedIn, Twitter/X, WeChat, 小红书, Instagram, and more. | "写社媒文案", "social media post", "发LinkedIn", "Twitter文案", "小红书文案" |
| [video-script-creator](skills/video-script-creator/) | Write scripts for product demos, explainer videos, elevator pitches, and founder storytelling. | "写视频脚本", "video script", "产品演示视频", "explainer video", "宣传片脚本" |
| [infographic-generator](skills/infographic-generator/) | Create high-density information graphics, data visualizations, and blueprint-style infographics for pitches, reports, and social sharing. | "信息图生成", "数据可视化", "infographic", "蓝图风格", "长图制作" |
| [newsletter-autopilot](skills/newsletter-autopilot/) | Draft newsletter content from company updates, meeting notes, or founder reflections. Automated email newsletter creation. | "newsletter", "写newsletter", "邮件营销", "newsletter automation", "公司月报" |

### Operations & Daily (2 skills)

| Skill | Description | Triggers |
|-------|-------------|----------|
| [meeting-minutes-ai](skills/meeting-minutes-ai/) | Extract action items, decisions, and key insights from meeting transcripts or recordings. | "会议纪要", "meeting minutes", "提取行动项", "action items", "会议总结" |
| [founder-daily-brief](skills/founder-daily-brief/) | Generate a personalized daily briefing with tasks, meetings, industry news, and competitor updates for startup founders. | "创始人日报", "每日简报", "startup daily brief", "morning founder report", "创业日报" |

---

## Installation

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install:

```bash
# Install all founder skills
npx skills add wulaosiji/founder-skills

# Install specific skills
npx skills add wulaosiji/founder-skills --skill pitch-deck-creator deck-web-converter

# List available skills
npx skills add wulaosiji/founder-skills --list
```

This automatically installs to your `.agents/skills/` directory.

### Option 2: Clone and Copy

```bash
git clone https://github.com/wulaosiji/founder-skills.git
cp -r founder-skills/skills/* .agents/skills/
```

---

## Usage

Once installed, just ask your agent:

```
"帮我做一个融资PPT，我们是做AI编程助手的"
→ Uses pitch-deck-creator skill

"把刚才的BP转成网页版"
→ Uses deck-web-converter skill

"先建立我的创始人档案"
→ Uses unique-club-founder-kit skill

"帮我监控竞品的最新动态"
→ Uses competitor-tracker skill

"生成今天的市场情报简报"
→ Uses market-intel-brief skill
```

You can also invoke skills directly:

```
/unique-club-founder-kit
/pitch-deck-creator
/deck-web-converter
/market-intel-brief
```

---

## Skill Network

Skills are designed to work together through bidirectional cross-references. Below are the key workflow chains:

### Fundraising Chain
```
unique-club-founder-kit (导航)
  → fundraising-bp-planner / investor-pitch-planner (大纲规划)
    → sequoia-structured-bp / yc-insight-driven-bp / raskin-narrative-bp (框架选择)
      → pitch-deck-creator / business-plan-ppt (生成PPT)
        → deck-web-converter (转网页分享)
          → investor-research (找投资人)
            → investor-due-diligence (评级筛选)
```
- `fundraising-bp-planner` ↔ `investor-pitch-planner`: 中英文大纲互补
- `sequoia-structured-bp` ↔ `yc-insight-driven-bp` ↔ `raskin-narrative-bp`: 三大框架按轮次和场景选择，三者互相关联
- `pitch-deck-creator` → `deck-web-converter`: PPTX → HTML 无缝流转
- `investor-research` → `investor-due-diligence`: 先建清单再评级
- `investor-research` → `pitch-deck-creator`: 根据投资人 thesis 定制 deck 内容

### Market Intelligence Chain
```
market-research-extractor (多平台抓取)
  ├── social-intelligence (Twitter/X 监控)
  ├── china-content-research (微信/中文平台)
  └── competitor-tracker (竞品定向追踪)
    → market-intel-brief (汇总成简报)
      → content-multiplier (情报转内容)
        → newsletter-autopilot (生成newsletter)
```
- `competitor-tracker` ↔ `social-intelligence`: 竞品追踪与社媒监听互补
- `china-content-research` ↔ `market-research-extractor`: 中文深度研究与通用抓取配合
- `market-intel-brief` → `content-multiplier`: 行业洞察直接转化为多平台内容
- `market-intel-brief` → `newsletter-autopilot`: 简报内容直接进入邮件营销

### Content Creation Chain
```
founder-content-writer (深度长文)
  ├── content-multiplier (一鱼多吃，多平台改写)
  │   ├── social-post-generator (社媒短文案)
  │   ├── video-script-creator (视频脚本)
  │   ├── newsletter-autopilot (newsletter)
  │   └── infographic-generator (信息图配图)
  └── infographic-generator (长文数据可视化)
```
- `founder-content-writer` → `content-multiplier`: 长文是内容放大的源头
- `content-multiplier` → `social-post-generator`: 长文拆成社媒片段
- `content-multiplier` → `video-script-creator`: 文字内容转视频脚本
- `content-multiplier` → `newsletter-autopilot`: 多平台内容汇总成邮件
- `infographic-generator` → `social-post-generator`: 信息图作为社媒视觉素材

### Operations Chain
```
meeting-minutes-ai (会议纪要提取)
  → founder-daily-brief (汇入每日简报)
    → competitor-tracker / market-intel-brief (补充竞品和行业动态)
      → content-multiplier (简报内容可二次分发)
```
- `meeting-minutes-ai` → `founder-daily-brief`: 会议行动项进入日报
- `founder-daily-brief` ↔ `competitor-tracker`: 日报集成竞品监控结果
- `founder-daily-brief` → `content-multiplier`: 日报洞察可转化为对外内容

### Cross-Category Hubs
- **`unique-club-founder-kit`** connects to: `pitch-deck-creator`, `competitor-tracker`, `founder-content-writer`, `meeting-minutes-ai`, `founder-daily-brief`, `market-intel-brief`, `content-multiplier` — the central navigation node
- **`content-multiplier`** is the most connected content hub, linking to 5 other content skills + market intelligence + operations
- **`market-intel-brief`** bridges market intelligence and content creation, feeding insights into `content-multiplier` and `newsletter-autopilot`

---

## Requirements

- Claude Code, Cursor, or any AI agent supporting the [Agent Skills spec](https://agentskills.io)
- For `pitch-deck-creator`: Python with `python-pptx` library
- For `deck-web-converter`: Python with `python-pptx` and `pymupdf`
- For `infographic-generator`: Python with `matplotlib` and `Pillow`

## Executable Scripts

Six skills include executable Python scripts for standalone use:

| Skill | Script | Description |
|-------|--------|-------------|
| `pitch-deck-creator` | [`scripts/generate_pitch_deck.py`](skills/pitch-deck-creator/scripts/generate_pitch_deck.py) | Generate a 10-slide PPTX from JSON data |
| `deck-web-converter` | [`scripts/convert_deck.py`](skills/deck-web-converter/scripts/convert_deck.py) | Convert PPT/PDF to HTML |
| `investor-research` | [`scripts/research_investors.py`](skills/investor-research/scripts/research_investors.py) | Generate an investor research report |
| `content-multiplier` | [`scripts/multiplier.py`](skills/content-multiplier/scripts/multiplier.py) | Transform content for multiple platforms |
| `meeting-minutes-ai` | [`scripts/extract_minutes.py`](skills/meeting-minutes-ai/scripts/extract_minutes.py) | Extract minutes from a transcript |
| `founder-daily-brief` | [`scripts/daily_brief.py`](skills/founder-daily-brief/scripts/daily_brief.py) | Generate a daily founder briefing |

### Using the Scripts

```bash
# 1. Install a skill's dependencies
cd skills/pitch-deck-creator
pip install -r requirements.txt

# 2. Run the script
python scripts/generate_pitch_deck.py --input startup.json --output deck.pptx

# 3. See help for all options
python scripts/generate_pitch_deck.py --help
```

---

## About UniqueClub

These skills are part of the **UniqueClub** founder toolkit.

🌐 **https://uniqueclub.ai** — Tools, community, and resources for startup founders.

📂 **https://github.com/wulaosiji/founder-skills** — 24 skills and growing.

Built by founders, for founders.

---

## Contributing

1. Fork this repository
2. Create your skill in `skills/your-skill-name/SKILL.md`
3. Follow the [skill format guide](https://agentskills.io/docs)
4. Submit a PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

MIT © 吴畏 (Wu Wei) / UniqueClub

---

*Last updated: 2026-09-09*
*Audit status: 24/24 skills passed 7-dimension quality audit (100/100)*
