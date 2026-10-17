# 🎲 RPG Campaign Factory

A multi-agent AI pipeline that generates complete, ready-to-play tabletop RPG
campaigns — bilingual (🇮🇹 IT / 🇬🇧 EN), from a one-line brief to a print-ready PDF.
Specialized agents each own one craft (world, plot, cast, encounters, maps, QA,
translation, layout) and are orchestrated end-to-end.

> A personal project exploring how far a well-structured multi-agent workflow can
> take long-form creative generation. Sample content uses the openly-licensed
> **D&D 5e SRD 5.1** (CC-BY-4.0).

![Sample pages from "The Veil of the Seals"](assets/preview.png)

📥 **Sample campaign PDF** — *The Veil of the Seals* (D&D 5e SRD, 43 pages):
[English](https://github.com/lballoriani/rpg-campaign-factory/releases/latest/download/dnd5e-il-velo-dei-sigilli_en.pdf) ·
[Italiano](https://github.com/lballoriani/rpg-campaign-factory/releases/latest/download/dnd5e-il-velo-dei-sigilli_it.pdf)
— see [Releases](https://github.com/lballoriani/rpg-campaign-factory/releases).

## How it works

```
Brief ─▶ Orchestrator
          ├─ Lore Architect     worldbuilding, factions, hooks
          ├─ Plot Weaver        arc + session-by-session structure
          ├─ Cast Designer      NPCs & bosses with stat blocks
          ├─ Encounter Builder  fights, traps, puzzles (balanced)
          ├─ Cartographer       region/city/dungeon maps + AI prompts
          ├─ QA Reviewer        consistency & balance pass
          ├─ Translator         IT ▶ EN
          └─ Layout Publisher   Typst ▶ PDF
```

Each agent is a versioned system prompt in [`agents/`](agents/); the Python tools
in [`tools/`](tools/) validate structure, generate maps (FLUX.1-schnell), export a
catalog and build the PDFs.

## What comes out

For each campaign: setting, plot & session guides, NPC/boss sheets, encounters,
AI-generated maps, and a laid-out **PDF in both languages**. See the sample sources
under [`campaigns/dnd5e/`](campaigns/dnd5e/) and the finished PDFs in
[Releases](https://github.com/lballoriani/rpg-campaign-factory/releases).

## Run it

```bash
cp .env.example .env        # add your ANTHROPIC_API_KEY (+ optional HF_TOKEN for maps)
python3 tools/validate-campaign.py campaigns/dnd5e/il-velo-dei-sigilli
./tools/build-pdf.sh        # render the PDF via Typst
```

## Project layout

```
agents/       specialist agent system prompts (the orchestration core)
tools/        pipeline: validate, generate maps, export catalog, build PDF
templates/    empty campaign skeleton + Typst PDF templates
campaigns/    generated campaigns (D&D 5e SRD sample included)
```

## Licensing

Code, agents and tooling: **MIT** (see [LICENSE](LICENSE)). Sample content derives
from the **D&D 5e SRD 5.1** under **CC-BY-4.0**. Other game systems are the IP of
their publishers and are **not** included — supply your own licensed reference
material locally.

## Stack

Python · Claude (multi-agent) · FLUX.1-schnell (maps) · Typst (PDF)
