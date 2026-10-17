[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**[繁體中文](README.zh-TW.md)** | **[日本語](README.ja.md)** | English

# Expert Skills

Make your AI think like Munger, Feynman, or Paul Graham — not by role-playing, but by loading the actual mental models they use to make decisions.

```
You:    "My friend wants me to invest $50K in his restaurant. He's a great cook."

Claude: "Sure, let's look at the opportunity..."

Claude + expert-munger:
        "You said 'he's a great cook' — that's Circle of Competence Violation:
         you're judging investment ability by cooking skill.
         Invert: what guarantees this fails in 5 years?
         33% of savings, illiquid, and your only evidence is a personality trait."
```

> Giving Claude a persona ("act as Charlie Munger") produces worse outputs than loading Munger's actual frameworks. The persona is decoration. The framework is the mechanism.

---

## Install

```bash
npx openskills install https://github.com/AskRoundtable/expert-skills
```

Works with Claude Code, Cursor, Windsurf, or any SKILL.md-compatible tool.

---

## Experts

| Module | How they think | Ask them about |
|--------|---------------|----------------|
| **expert-munger** | Inversion, Circle of Competence, Margin of Safety | "Should I invest in X?" "What could go wrong with this deal?" |
| **expert-naval** | Leverage (code/media/capital), Specific Knowledge, Principal vs Agent | "Should I take this job?" "How do I build long-term wealth?" |
| **expert-feynman** | First Principles decomposition, Feynman Technique, Analogy | "Explain X to me like I'm 12" "How does this actually work?" |
| **expert-kahneman** | System 1 vs System 2, Loss Aversion, Anchoring | "Am I being rational about this?" "What biases am I missing?" |
| **expert-graham** | Do Things That Don't Scale, Schlep Blindness, Default Alive | "Is this a good startup idea?" "How do I get my first users?" |

---

## Examples

**Career decision + expert-naval:**
```
You:    "I got a job offer — 40% pay raise but I'd be managing a team instead of coding."

Claude: "That's a significant raise. Let's weigh the pros and cons..."

Claude + expert-naval:
        "This is a Leverage trap. You're trading permissionless leverage (code)
         for the oldest, weakest form — labor leverage (managing people).
         The raise is linear; your coding career compounds.
         Ask: in 10 years, which version of you has more Specific Knowledge
         and more options?"
```

**Startup idea + expert-graham:**
```
You:    "I want to build an AI app for meal planning. The market is huge."

Claude: "Great idea! The meal planning market is growing fast..."

Claude + expert-graham:
        "You said 'the market is huge' — that's a Tarpit Idea signal.
         If it's obviously good and the market is huge, why hasn't someone
         already won? What's the schlep everyone is avoiding?
         More important: do YOU have this problem? Are you Default Alive
         if you build this — or are you betting on funding?"
```

**Cognitive bias + expert-kahneman:**
```
You:    "We tested 3 marketing strategies. Strategy B got 20% more clicks
         last week so we're going all-in on it."

Claude: "Strategy B clearly outperformed. Here's how to scale it..."

Claude + expert-kahneman:
        "One week of data is textbook System 1 thinking — your brain wants
         a narrative from noise. With 3 strategies and 1 week, you're
         anchored to a small sample. What's the base rate for weekly
         variance in your click data? This could be regression to the mean
         dressed up as a winner."
```

---

## Why Not Just "Act as Munger"?

Persona prompting tells the AI *who to be*. Expert Skills tells it *how to think*.

Each module encodes an expert's actual cognitive process:
- **Patterns** they recognize ("this looks like a Circle of Competence violation")
- **Mental models** they apply (Inversion, Leverage, First Principles)
- **Cues** they notice that others miss
- **Blind spots** they carry (so the analysis flags its own limitations)

All driven by a 6-step cognitive engine based on how real experts make decisions under uncertainty (Gary Klein's Recognition-Primed Decision model).

---

## Performance

Evaluated against baseline Claude (no expert modules, temperature=0) using a 4-dimension rubric across 3 real-world cases per expert.

| Expert | Domain | Delta vs Baseline |
|--------|--------|-------------------|
| expert-graham | Startups / Growth | +38% to +83% |
| expert-feynman | First Principles / Learning | +38% to +57% |
| expert-naval | Career / Wealth / Life | +38% to +57% |
| expert-kahneman | Behavioral Economics / Decisions | +31% to +63% |
| expert-munger | Investment / Business | +18% to +41% |

Rubric dimensions: pattern recognition accuracy, mental model application, blind spot awareness, and actionability of recommendation.

---

## How It Works

Two-layer architecture: a cognitive engine runs the thinking process, expert modules supply domain knowledge.

```
┌──────────────────────────────────────────┐
│              expert-engine               │
│         6-step cognitive process         │
│                                          │
│  Pattern Recognition → Mental Simulation │
│  → Anomaly Detection → Insight           │
│  → Epistemic Audit                       │
└──────────────────┬───────────────────────┘
                   │ loads domain content from
        ┌──────────┼──────────┐
        ▼          ▼          ▼
  expert-munger  expert-naval  expert-feynman
  patterns.md    models-core   blind-spots.md
  models-core    blind-spots   ...
```

The engine runs every time. Expert modules supply situation patterns, mental models, cue sensitivity lists, and known blind spots — content the engine could never have without domain knowledge.
