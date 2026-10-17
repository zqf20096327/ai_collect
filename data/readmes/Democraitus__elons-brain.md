# Elon's Brain

A self-contained AI brain for *talking to Elon Musk*, distilled from ***The Book of Elon*** by Eric Jorgenson (Scribe Media, 2026). Ships with the full book text plus 72 mental models as internal corpus.

## Two products, one repo

### 1. The brain — `elon/`

A single Claude Code skill that fires on any decision question (founder, engineering, product, hiring, strategy, schedule, risk) and answers in Elon's voice — blunt, physics-first, contrarian, compelled-not-balanced — with citations to the actual book passages.

Self-contained. Bundles:
- The full book text at `elon/corpus/book-of-elon.txt` (401 pages, page-marked)
- 72 mental models at `elon/skills/<name>/SKILL.md` (~380 verified direct quotes)
- Recipes (structured walkthroughs) at `elon/recipes/`

**Install the brain:**

Download `elons-brain.skill` from the [latest release](https://github.com/Democraitus/elons-brain/releases), then:

```bash
unzip elons-brain.skill
cp -R elon ~/.claude/skills/
```

Or clone the repo and install from source:

```bash
git clone git@github.com:Democraitus/elons-brain.git
cp -R elons-brain/elon ~/.claude/skills/
```

That's it. One skill, full corpus.

### 2. The pack — 72 individual Claude Code skills

The mental models, distributed as a flat pack of individually-triggered Claude Code skills. Useful when you want a specific lens fired in a specific context — code review, hiring loop, design audit — rather than the full conversational Elon.

**Install the pack:**

Download `elons-brain-pack.zip` from the [latest release](https://github.com/Democraitus/elons-brain/releases), then:

```bash
unzip elons-brain-pack.zip -d ~/.claude/skills/
```

The 72 skill directories extract directly into `~/.claude/skills/`. One line.

## Build from source

Both artifacts are derived from `elon/` — single source of truth, two outputs:

```bash
bash scripts/build-brain.sh   # → elons-brain.skill (the brain, single skill)
bash scripts/build-pack.sh    # → elons-brain-pack.zip (the 72 flat skills)
```

## The 72 mental models

**Foundational** — the-algorithm · first-principles-thinking · aspire-to-be-less-wrong · listen-well-correct-fast · utility-math · wishful-thinking-detector · probabilistic-fatalism

**Cost & design** — idiot-index · magic-wand-number · thinking-in-limits · cost-floor-thinking · factory-is-the-product · manufacturing-is-the-moat

**Execution & urgency** — attack-the-constraint · do-things-in-parallel · timeline-is-wrong-if-long · set-aggressive-timelines · exponential-curve-thinking · break-down-the-impossible · speed-is-both-offense-and-defense · just-barely-possible · supplier-as-bottleneck

**Org & communication** — shortest-path-communication · skip-level · find-design-necessity · simple-clear-humble-terms · dilbert-test · bad-news-loudly

**People & hiring** — recruit-for-exceptional-ability · retain-only-special-forces · hire-for-attitude · character-via-associates · feedback-over-feelings · create-a-culture-of-builders · a-group-with-a-goal

**Leadership & crisis** — frontline-leadership · earn-deep-understanding · eat-glass-stare-into-abyss · the-edge-of-sanity · triage-by-escalation · ego-ability-ratio · bicameral-brain · lead-product-by-leading-company

**Risk & iteration** — you-have-to-blow-things-up · failure-is-irrelevant-unless-catastrophic · risk-reward-asymmetry-design · fail-tolerant-incentives · risk-list-discipline

**Engineering depth** — best-part-is-no-part · delete-line-of-code · tolerance-stack-analysis

**Capital & founder bets** — going-all-in-again · expect-loss · invest-your-money-first

**Strategy & positioning** — sequenced-strategy · give-more-for-less · unite-and-conquer · technology-advantage-wins · build-before-they-ask · avoid-bonehead-customers · vertical-integration-when-blocked · industry-misdirection-spotter · word-of-mouth-over-marketing · detach-from-clickbait · positive-sum-audit

**Product & quality** — single-optimization-metric · train-aesthetic-eye · signal-over-noise-spending · lego-precision-standard

**Thinking sub-patterns** — pick-and-move · best-idea-wins · build-the-knowledge-tree

## Skill anatomy

Each of the 72 is one directory with:

- **`SKILL.md`** — YAML frontmatter (`name:`, `description:`, `stacks_with:`) + body (opening book quote, what it captures, when to use, how-to with cited steps, common failure modes, when NOT to use, source)
- **`evals/evals.json`** — 2–3 trigger-test prompts with objective assertions

The `stacks_with:` field declares which sibling skills naturally co-fire on the same prompt. The brain uses this graph to compose multiple lenses at synthesis time.

## Source

All thinking distilled from ***The Book of Elon*** by Eric Jorgenson (Scribe Media, 2026), freely distributed by the author. Foreword by Naval Ravikant. Visuals by Jack Butcher.

The full text ships at `elon/corpus/book-of-elon.txt`. Buying a physical or digital copy is still encouraged — the included text is for the AI to read, not a replacement for human reading.

## Repo layout

```
elons-brain/
├── README.md
├── ROADMAP.md                         # version history & build notes
├── elon/                              # ⭐ THE BRAIN — primary product
│   ├── SKILL.md                       # persona, procedure, mental-model catalog
│   ├── corpus/
│   │   ├── book-of-elon.txt           # full text, ~8K lines, page-marked
│   │   └── README.md
│   ├── skills/                        # 72 mental models (single source of truth)
│   │   ├── the-algorithm/
│   │   │   ├── SKILL.md
│   │   │   └── evals/evals.json
│   │   └── ... (71 more)
│   └── recipes/
│       └── founder-go-nogo.md
├── scripts/
│   ├── build-pack.sh                  # → elons-brain-pack.skill (derived from elon/skills/)
│   ├── build-brain.sh                 # → elons-brain.skill (the brain)
│   ├── build-pack.sh                  # → elons-brain-pack.zip (the 72 flat)
│   └── build_skill_prompt.py          # build tooling for adding new skills
├── skills-manifest.json               # full skill metadata
├── elons-brain.skill                  # built brain artifact (also in releases)
└── elons-brain-pack.zip               # built pack artifact (also in releases)
```

## License

MIT for the skill pack scaffolding. The book text is included under the author's free-distribution terms; Jorgenson & Scribe Media own the source.
