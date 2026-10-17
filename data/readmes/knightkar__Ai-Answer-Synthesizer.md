<p align="center">
  <img src="assets/banner.png" alt="AI Answer Synthesizer" width="800"/>
</p>

<h1 align="center">AI Answer Synthesizer</h1>

<p align="center">
  <strong>Stop reading 5 AI answers. Get one clear recommendation.</strong>
</p>

<p align="center">
  <a href="#installation"><img src="https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square" alt="Claude Skill"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License"/></a>
  <a href="#status"><img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status: Active"/></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-orange?style=flat-square" alt="PRs Welcome"/></a>
</p>

<p align="center">
  <a href="#the-problem">The Problem</a> · 
  <a href="#how-it-works">How It Works</a> · 
  <a href="#installation">Installation</a> · 
  <a href="#usage">Usage</a> · 
  <a href="#examples">Examples</a> · 
  <a href="#roadmap">Roadmap</a> · 
  <a href="#contributing">Contributing</a>
</p>

---

## The Problem

You ask the same question to ChatGPT, Claude, Gemini, Copilot, and Perplexity. You get five long responses. Now you're **more confused than before**.

The AI Answer Synthesizer solves this. Paste multiple AI responses into Claude and get back:

- **One clear recommendation** (not five summaries)
- **Confidence scoring** (how much the AIs actually agree)
- **Real disagreement detection** (not just vocabulary differences)
- **An action plan matched to your skill level**
- **A list of what to ignore** (so you don't drown in options)

This is not a summarizer. It's an **adjudicator**.

## How It Works

The skill uses a 6-step analytical methodology that goes beyond summarization:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  1. EXTRACT CLAIMS    → Break each response into    │
│                         discrete, testable claims   │
│                                                     │
│  2. MAP CONSENSUS     → Which claims do multiple    │
│                         AIs actually agree on?      │
│                                                     │
│  3. COLLAPSE ALIASES  → "MVP" and "prototype"       │
│                         mean the same thing          │
│                                                     │
│  4. DETECT CONFLICTS  → Where do they ACTUALLY      │
│                         disagree, not just differ?   │
│                                                     │
│  5. ASSESS FIT        → Match complexity to the     │
│                         user's real skill level      │
│                                                     │
│  6. SYNTHESIZE        → One recommended path with   │
│                         honest confidence level      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Key Safeguards

| Safeguard | What It Prevents |
|-----------|-----------------|
| **Anti-Consensus Bias** | Majority vote burying a better minority answer |
| **Hallucination Cascade Detection** | LLM summarizing LLM errors and amplifying them |
| **Lone Claim Flagging** | One AI's unsupported claim slipping in as fact |
| **Complexity Filter** | The most advanced answer winning over the most useful one |

## Installation

### Claude.ai (Recommended)

1. Go to [claude.ai](https://claude.ai) → **Settings** → **Skills**
2. Click **Create Skill**
3. Copy the contents of [`skills/ai-answer-synthesizer/SKILL.md`](skills/ai-answer-synthesizer/SKILL.md)
4. Paste into the skill instructions
5. Save

### Claude Code

```bash
# Clone and install
git clone https://github.com/knightkar/Ai-Answer-Synthesizer.git
cd ai-answer-synthesizer

# The skill file is at:
# skills/ai-answer-synthesizer/SKILL.md
```

## Usage

### Quick Mode — Just give me the answer

```
I asked ChatGPT and Gemini the same question. Here are their responses:
[paste responses]
Give me a quick synthesis.
```

**Output:** 2-4 sentence answer + confidence level + one next step.

### Deep Mode — Help me understand

```
I asked 3 AIs how to deploy a web app. Here are all their responses:

ChatGPT said: [paste]
Gemini said: [paste]  
Copilot said: [paste]

Synthesize these and tell me the best path for a beginner.
```

**Output:** Full structured analysis with consensus map, disagreement detection, recommended path, and ignore list.

## Examples

<details>
<summary><strong>Example 1: Conflicting technical advice</strong></summary>

**You:** "ChatGPT says use React, Claude says use plain HTML, Gemini says use Next.js. I just want to build a simple landing page."

**Synthesizer output:**

> **The Short Answer:** Use plain HTML and CSS. For a simple landing page, a framework adds complexity you don't need yet.
>
> **Confidence:** High — two of three responses support starting simple, and the React/Next.js suggestions assume you need features you haven't mentioned.
>
> **What They Agree On:**
> - You need a landing page, not a web app
> - Start simple, scale later
> - Good design matters more than the framework
>
> **Where They Actually Disagree:**
> The "disagreement" is really about scale. React and Next.js are for when you need interactivity and routing. A landing page doesn't need either. This isn't a real conflict — it's different assumptions about what you're building.
>
> **Recommended Path:**
> 1. Create an `index.html` file
> 2. Add your content and basic CSS
> 3. Deploy free on GitHub Pages or Netlify
> 4. Only add a framework if you need dynamic features later

</details>

<details>
<summary><strong>Example 2: Overwhelmed beginner</strong></summary>

**You:** "I feel overwhelmed by these AI answers. Please simplify and tell me only what matters."

**Synthesizer output (Quick Mode):**

> **The answer:** All three AIs are telling you the same thing in different words: start with the smallest version that proves your idea works. Don't build the full system yet.
>
> **Confidence:** High — complete consensus on the core recommendation.
>
> **Do this next:** Write down your idea in one sentence, then build only the piece that tests whether anyone actually wants it.

</details>

<details>
<summary><strong>Example 3: Two responses only</strong></summary>

**You:** "Perplexity and Claude gave me different investment strategies. Which should I follow?"

**Synthesizer output:**

> **The Short Answer:** Both suggest diversification but differ on allocation. With only two sources and a financial decision, treat this as a starting point for research, not a final answer.
>
> **Confidence:** Medium — two sources with partial agreement, but financial advice requires more context than either AI had.

</details>

See [`examples/sample-prompts.md`](examples/sample-prompts.md) for more test scenarios.

## Repository Structure

```
ai-answer-synthesizer/
├── README.md                          # You are here
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # How to contribute
├── .gitignore                         # Git ignore rules
├── skills/
│   └── ai-answer-synthesizer/
│       └── SKILL.md                   # The skill (install this)
├── examples/
│   └── sample-prompts.md              # Test prompts to try
└── assets/
    └── banner.png                     # Repo banner image
```

## Status

This project is **actively maintained** and in use. Current priorities:

- [x] Core synthesis methodology (6-step analysis)
- [x] Quick Mode and Deep Mode
- [x] Anti-consensus bias safeguards
- [x] Hallucination cascade detection
- [x] Lone claim risk flagging
- [ ] Test on 20+ real-world multi-AI comparisons
- [ ] Community-contributed edge cases
- [ ] Browser-based input tool (v2)

## Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **v1.0** | Core Claude Skill with full methodology | ✅ Complete |
| **v1.1** | Community testing and edge case refinement | 🔄 In Progress |
| **v2.0** | Browser-based input collector (paste UI) | 📋 Planned |
| **v3.0** | Browser extension for one-click collection | 💡 Exploring |

## Design Principles

- **Adjudicate, don't summarize** — Produce verdicts, not book reports
- **Simplicity over sophistication** — The most useful answer beats the most impressive one
- **Honest confidence** — Say when you're uncertain instead of hedging with filler
- **One path when possible** — Recommend, don't fence-sit
- **Complexity is not quality** — The longest answer is rarely the best answer
- **Consensus is a signal, not a verdict** — A well-reasoned minority view can beat a generic majority

## Contributing

Contributions are welcome. The most impactful contributions right now:

- **Real-world test cases** — paste actual multi-AI comparisons and share how the skill performed
- **Edge cases** — scenarios where the synthesis logic breaks down
- **SKILL.md improvements** — sharper methodology, better phrasing
- **Documentation** — clearer README, better examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[MIT](LICENSE) — Use it, fork it, improve it, ship it.

## Acknowledgments

Built by synthesizing insights from ChatGPT, Claude, Gemini, Copilot, and Perplexity — which is exactly the kind of problem this skill was made to solve.

Inspired by the growing need for **AI adjudication** as multi-model workflows become the norm. Special thanks to the Claude Skills ecosystem and the open-source community for the patterns that shaped this project.

---

<p align="center">
  <sub>If this skill saved you from reading five AI essays, consider giving it a ⭐</sub>
</p>
