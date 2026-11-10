# BrainLift Writer Skill

![BrainLift Writer Skill banner](assets/brainlift-writer-banner.png)

BrainLift Writer is an AI-agnostic skill for turning research, notes, and rough thinking into a structured BrainLift: a reusable context document that helps any AI model understand the author's mental model quickly.

It is based on the BrainLift pattern of moving from purpose and scope to DOK 2 knowledge trees, DOK 3 insights, and DOK 4 spiky points of view.

## What This Helps With

- Draft a BrainLift from messy notes, transcripts, articles, or research dumps
- Improve an existing BrainLift so it has stronger structure and sharper synthesis
- Audit whether a BrainLift has clear scope, evidence, insights, and defensible POVs
- Create portable context that works across Codex, Claude, ChatGPT, Cursor, Gemini, and other AI tools
- Keep AI focused on organizing and sharpening human thinking instead of replacing it

## Repository Layout

```text
brainlift-writer-skill/
|-- assets/
|   `-- brainlift-writer-banner.png
|-- brainlift-writer/
|   |-- SKILL.md
|   |-- agents/
|   |   `-- openai.yaml
|   `-- references/
|       `-- brainlift-template.md
|-- README.md
`-- LICENSE
```

The installable skill lives in `brainlift-writer/`. The root README exists for GitHub users and is not part of the skill payload.

## Install For Codex

Copy the skill folder into your Codex skills directory:

```bash
cp -R brainlift-writer ~/.codex/skills/
```

Then invoke it with:

```text
Use $brainlift-writer to turn these notes into a BrainLift.
```

## Use With Any AI Tool

This skill is intentionally portable. For Claude Projects, ChatGPT custom GPTs, Cursor rules, or other agents:

1. Copy the contents of `brainlift-writer/SKILL.md` into the tool's instruction area.
2. Add `brainlift-writer/references/brainlift-template.md` as supporting reference material.
3. Ask the model to draft, revise, or audit a BrainLift using those instructions.

Example prompt:

```text
Use the BrainLift Writer instructions to turn the notes below into a BrainLift. Keep facts, summaries, insights, and spiky POVs clearly separated. Mark gaps instead of inventing evidence.
```

## What Makes A Good BrainLift

A strong BrainLift is not just a summary. It is structured context that captures how the author thinks about a domain.

The skill pushes the model to:

- Start with a clear purpose and explicit scope boundaries
- Build a DOK 2 knowledge tree from source-level facts and summaries
- Convert that foundation into DOK 3 original insights
- Synthesize DOK 4 spiky points of view that are strong, useful, and defensible
- Preserve uncertainty and source provenance

## GitHub Description

AI-agnostic skill for writing BrainLifts: structured context docs that turn research into DOK knowledge trees, insights, and spiky POVs.

## Suggested GitHub Topics

`ai`, `ai-agents`, `brainlift`, `knowledge-management`, `personal-knowledge-management`, `pkm`, `prompt-engineering`, `context-engineering`, `learning-science`, `depth-of-knowledge`, `dok`, `knowledge-synthesis`, `writing`, `research`, `spiky-pov`, `ai-skills`, `codex-skill`, `claude`, `chatgpt`, `cursor`

## Source Inspiration

This package was created from the shared Nessie context ["BrainLift: The Complete Template"](https://nessielabs.com/context/f3bee4f8-8176-472e-aa73-24982eae4f63), then rewritten as portable agent instructions.
