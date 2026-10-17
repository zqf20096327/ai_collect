# brand.md

An open standard for AI-executable brand identity.

`brand.md` is a structured Markdown file that gives AI tools the context they need to write, design, generate, and build on brand. It is intended to live at the root of a project, next to files like `llms.txt`, `design.md`, `CLAUDE.md`, or `.cursorrules`.

Most brand guidelines describe a brand for humans. `brand.md` is built for AI systems that need to act on brand guidance.

## Why It Exists

AI tools can read a brand PDF, website, or portal, but they still miss the hidden decisions that make a brand coherent:

- why a color was chosen, not just its hex value
- what a voice trait means in behavior, not just as an adjective
- which tokens are allowed to pair, inherit, or override each other
- how imagery should be prompted and what it must avoid
- where brand identity ends and UI implementation begins

`brand.md` solves this by making brand identity portable, structured, and executable.

## The Core Idea

Every meaningful brand element should carry three layers:

| Layer | Purpose | Examples |
|---|---|---|
| Precision Layer | Exact values AI and code can verify | Hex values, token IDs, font families, motion durations, minimum logo sizes |
| Semantic Layer | Meaning AI can use while generating | Color descriptors, voice behavior, mood keywords, image prompts, comparable fonts |
| Relationship Layer | Governance and selection logic | Depends-on rules, approved pairings, channel deltas, inheritance, misuse rules |

The Semantic Layer is the key difference between a brand file AI can read and one it can execute.

## Quick Example

Hex-only brand guidance:

```markdown
- Primary green: #184F35
- Usage: headings and CTAs
```

AI-executable brand guidance:

```markdown
- Token: color.primary.deep-forest
- Hex: #184F35
- AI-optimized name: dark British racing green
- Image prompt: dark British racing green, deep forest tone, muted and natural
- Avoid confusing with: hunter green, olive, bright forest green
- Mood: grounded, natural, premium, quiet confidence
- Usage: primary CTAs, brand headlines, key UI emphasis
- Accessibility: use with white text only after contrast check
```

The first version names a value. The second version prevents AI drift.

## Where brand.md Fits

| File | Layer | Answers | Consumed by |
|---|---|---|---|
| `llms.txt` | Discovery | Where is this brand's AI-readable data? | Crawlers, agents, LLMs |
| `brand.md` | Identity | What is this brand and how does it think, speak, and look? | LLMs, image generators, content tools, coding agents |
| `design.md` | UI execution | How should this product interface be built? | Coding assistants, UI tools |
| `skills.md` | Procedures | How should specific tasks be performed? | Agents and workflow tools |
| `CLAUDE.md` / `.cursorrules` | Project overrides | What should this assistant know in this repo? | Coding assistants |

`brand.md` is upstream of `design.md`. Brand identity defines intent and constraints. Design systems execute those constraints in components, layouts, and code.

## Repository Structure

```text
brand-md/
├── README.md
├── brand.md
├── spec/
│   └── brand-md.md
├── brands/
│   ├── OFFICIAL.md
│   └── examples/
│       ├── acme-saas/
│       │   └── brand.md
│       ├── nova-agency/
│       │   └── brand.md
│       └── fold-consumer/
│           └── brand.md
├── SEMANTIC-LAYER.md
├── COMPARISON.md
├── CONTRIBUTING.md
└── LICENSE
```

## What This Repo Is

This repo is a standard and reference implementation for `brand.md`.

It includes:

- the `brand.md` specification
- the Semantic Layer model
- context for how `brand.md` relates to `llms.txt`, `design.md`, and agent instruction files
- fictional examples that demonstrate the format
- a registry model for official brand-owned files

## What This Repo Is Not

This repo is not a scraped library of famous brands.

A website is one public channel. It can show a brand's surface execution, but it cannot reveal the full brand intelligence underneath: positioning, voice governance, channel rules, campaign direction, internal guardrails, or strategic rationale.

Legitimate `brand.md` files should come from inside the brand or from a brand system built with the brand team's input.

## Generate A brand.md

Sameness generates `brand.md` from a structured brand graph, including precision, semantic, and relationship layers for identity, voice, color, typography, logo, motion, imagery, video, and audio.

Further reading: [What is brand.md?](https://www.sameness.co/blog/what-is-brand-md)

