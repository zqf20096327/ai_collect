# Awesome AI Craft [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <!-- omit in toc -->

> Software products, applications, and desktop suites created through AI-driven clean-room reimplementation, reverse engineering, and agentic workflows.


## Contents <!-- omit in toc -->

- [Creative \& Media Suite (Adobe Alternatives)](#creative--media-suite-adobe-alternatives)
- [Office \& Productivity Suite (Microsoft Alternatives)](#office--productivity-suite-microsoft-alternatives)
- [Audio \& CAD Systems](#audio--cad-systems)
- [Core Engine \& Framework](#core-engine--framework)
- [AI-Built Software Reimplementations](#ai-built-software-reimplementations)
- [Parametric 3D Engineering \& Simulation](#parametric-3d-engineering--simulation)
- [Game Reimplementations](#game-reimplementations)
- [Reverse Engineering \& Agent Tooling](#reverse-engineering--agent-tooling)
- [Clean-Room Methodology](#clean-room-methodology)
- [Community \& Discussions](#community--discussions)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)
  
---

## Creative & Media Suite (Adobe Alternatives)

*Pure-Rust replacements for proprietary Adobe Creative Cloud desktop applications.*

- [PhotoCraft](https://github.com/storytold/photocraft) - Clean-room reimplementation of Adobe Photoshop written from scratch in pure Rust, featuring multi-layer editing, PSD file parsing, non-destructive adjustment layers, and native AI agent scripting.
- [VectorCraft](https://github.com/storytold/vectorcraft) - Pure-Rust clean-room replacement for Adobe Illustrator, featuring Bézier path manipulation, SVG/AI import/export, typography layout, and boolean shape operations.
- [FilmCraft](https://github.com/storytold/filmcraft) - Clean-room non-linear video editor reimplementing Adobe Premiere Pro in Rust, with multi-track timeline editing, audio waveform sync, color correction, and hardware-accelerated rendering.
- [LightCraft](https://github.com/storytold/lightcraft) - Non-destructive RAW photo development and cataloging tool built in Rust as a clean-room alternative to Adobe Lightroom.
- [EffectCraft](https://github.com/storytold/effectcraft) - Digital visual effects, compositing, and motion graphics suite written in Rust as an open-source alternative to Adobe After Effects.
- [DesignCraft](https://github.com/storytold/designcraft) - Page design and typography desktop publisher built in pure Rust as a clean-room alternative to Adobe InDesign.
- [FigCraft](https://github.com/storytold/figcraft) - Clean-room interface design and prototyping tool written in Rust as an alternative to Figma.
- [AniCraft](https://github.com/storytold/AniCraft) - 2D animation editor written from scratch in Rust as a clean-room alternative to Adobe Animate.
- [PdfCraft](https://github.com/storytold/pdfcraft) - High-performance PDF reader, annotator, form filler, and page organizer replacing Adobe Acrobat Pro.

## Office & Productivity Suite (Microsoft Alternatives)

*Pure-Rust desktop replacements for Microsoft Office desktop software.*

- [WordCraft](https://github.com/storytold/wordcraft) - Clean-room word processor written in pure Rust supporting DOCX and ODT formats, designed as a fast native alternative to Microsoft Word.
- [GridCraft](https://github.com/storytold/gridcraft) - Spreadsheet application written from scratch in Rust with formula calculation engines and XLSX import/export, replacing Microsoft Excel.
- [DeckCraft](https://github.com/storytold/deckcraft) - Native presentation software written in Rust for crafting, styling, and presenting slide decks, replacing Microsoft PowerPoint.

## Audio & CAD Systems

*Specialized engineering and audio production tools.*

- [SoundCraft](https://github.com/storytold/soundcraft) - Digital audio workstation (DAW) and clean-room reimplementation of Avid Pro Tools and Adobe Audition in Rust for multi-track audio mixing and mastering.
- [CadCraft](https://github.com/storytold/cadcraft) - Computer-aided design and drafting application built in Rust as an open alternative to Autodesk AutoCAD.

## Core Engine & Framework

*Underlying engine architectures and agent bridges.*

- [ArtCraft](https://github.com/storytold/artcraft) - The core intentional crafting engine and unified UI framework that powers the entire Craft suite, with native Model Context Protocol (MCP) servers and JSON-RPC automation channels.

## AI-Built Software Reimplementations

*Frameworks, compilers, parsers, and engines rebuilt or ported mostly by coding agents, with humans directing the work.*

- [Ladybird LibJS in Rust](https://github.com/LadybirdBrowser/ladybird) - Rust port of Ladybird's C++ JavaScript engine frontend, with its lexer, parser, AST, and bytecode generator rewritten in about two weeks using Claude Code and Codex.
- [vinext](https://github.com/cloudflare/vinext) - Cloudflare's reimplementation of the Next.js API surface on top of Vite, built in about a week by one engineer directing AI models.
- [Claude's C Compiler](https://github.com/anthropics/claudes-c-compiler) - Dependency-free C compiler in Rust written by sixteen parallel Claude agents that can build the Linux kernel, though it is not validated for production use.
- [chardet 7](https://github.com/chardet/chardet) - AI-driven rewrite of the Python character encoding detector that changed its license from LGPL to MIT and then 0BSD, a case study in contested AI clean-room relicensing.
- [FastRender](https://github.com/wilsonzlin/fastrender) - Experimental browser engine written by thousands of parallel agents in Cursor's research on long-running autonomous coding.
- [JustHTML](https://github.com/EmilStenstrom/justhtml) - Pure-Python HTML5 parser built with coding agents that passes the full html5lib test suite.
- [justjshtml](https://github.com/simonw/justjshtml) - JavaScript port of JustHTML, produced by a coding agent and checked against the same test suite.

## Parametric 3D Engineering & Simulation

*Independent clean-room engineering tools extending the Craft paradigm into mechanical CAD, finite element analysis (FEA), and multi-physics simulation.*

- [SolidCraft](https://github.com/tangency-labs/solidcraft) - Open-source, parametric 3D CAD application written in pure Rust by Tangency Labs as a clean-room alternative to Dassault Systèmes SolidWorks and Autodesk Fusion 360. Features a parametric history timeline, 2D constraint solver, multi-platform runtime, STEP/IGES/STL/3MF export, and a built-in Model Context Protocol (MCP) server.
- [FieldCraft](https://github.com/tangency-labs/fieldcraft) - Open-source multi-physics modeler and simulation workbench written from scratch in pure Rust by Tangency Labs as a clean-room alternative to Abaqus/CAE, ANSYS, and COMSOL Multiphysics. Features automated meshing, nonlinear implicit and explicit FEA, heat transfer, lattice Boltzmann CFD, and native Model Context Protocol (MCP) and CLI interfaces.

## Game Reimplementations

*Clean-room recreations, decompilations, and recompilations of commercial games, many produced with AI agents.*

- [Skate 3 Rust Engine](https://github.com/SK8-ENGINE/skate-3-rust-engine) - Rust and Bevy recreation of Skate 3 built on years of community reverse-engineering research, with skating, tricks, grinds, offboard movement, and `.skate` map support. Ships no original game assets.
- [Horizon](https://github.com/ludovic111/horizon) - Minecraft: Java Edition rewritten from scratch in Rust, checked against vanilla by 281 differential harnesses, reading your own copy's worlds and assets, with native agent control through a CLI and MCP server.
- [Super Smash Bros. Melee decompilation](https://github.com/doldecomp/melee) - Human-led decompilation of Super Smash Bros. Melee (GameCube, 2001) that finished matching all functions in 2026, with AI tools proposing candidates and some commits crediting AI co-authors.
- [Super Mario 64 DS decompilation](https://github.com/tangosdev/sm64ds-decomp) - Byte-matching decompilation of Super Mario 64 DS (Nintendo DS, 2004) into C and C++, built from scratch with Claude, Codex, and other models.
- [Snowboard Kids 2 decompilation](https://github.com/cdlewis/snowboardkids2-decomp) - 100% matching decompilation of Snowboard Kids 2 (N64, 1999) produced by running Claude in an unattended loop, one function at a time.
- [Brave Fencer Musashi decompilation](https://github.com/Druthulu/BFM-decomp) - Matching decompilation of Brave Fencer Musashi (PlayStation, 1998) whose rebuilt binaries are byte-identical to the originals, with its AI-assisted workflow documented in the repository.
- [DX-Ball reconstruction](https://github.com/N0zoM1z0/dx-ball) - Reconstruction of DX-Ball 1.07 (Windows, 1996) by a coding agent driving REA, checked against the original x86 with differential tests and a pinned MSVC toolchain.
- [Snowboard Kids decompilation](https://github.com/cdlewis/snowboardkids-decomp) - 100% matching decompilation of Snowboard Kids (N64, 1998) using the same agent-driven approach as its sequel, with several AI models.
- [Little Planet](https://github.com/carl0srmz/littleplanet) - Static recompilation of Sonic CD (Mega-CD, 1993) into a native PC program, built with AI assistance.
- [Klonoa: Empire of Dreams decompilation](https://github.com/Dream-Atelier/kl-eod-decomp) - Matching decompilation of Klonoa: Empire of Dreams (GBA, 2001), in progress, with Claude Code credited in its commits.

## Reverse Engineering & Agent Tooling

*Bridges, MCP servers, and harnesses that let AI agents study binaries and check a rebuild against the original.*

- [REA](https://github.com/morluto/rea) - Reverse-engineering toolkit that gives coding agents tools to study apps and binaries, including APKs, native code, .NET, Electron, and web pages, with evidence cited for every finding.
- [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) - MCP server that connects IDA Pro to language models.
- [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) - MCP server that lets an AI model drive Ghidra.
- [GhidrAssist](https://github.com/symgraph/GhidrAssist) - Ghidra extension that explains functions and suggests names with an LLM.
- [decomp.wtf](https://github.com/i12bp8/decomp.wtf) - Command-line tool that lets Claude Code and similar agents decompile GameCube and Wii games you own, function by function; archived by its author in October 2026.

---


## Clean-Room Methodology

How AI agents enable clean-room software recreation:

```
┌───────────────────────────┐         ┌──────────────────────────┐
│  Target Proprietary App   │         │    Public Specifications  │
│  (UI / UX / Formats)      │         │    (PSD, STEP, OOXML, SVG)│
└─────────────┬─────────────┘         └─────────────┬────────────┘
              │                                     │
              ▼                                     ▼
      ┌──────────────────────────────────────────────────┐
      │  Reverse-Engineering Bridge (e.g. morluto/rea)  │
      │  - Extracts data schemas, UI hierarchies, formats│
      │  - Traces protocols, shortcuts, and capabilities │
      └───────────────────────┬──────────────────────────┘
                              │
                              ▼ [High-level Behavioral Spec]
      ┌──────────────────────────────────────────────────┐
      │     Clean-Room Coding Agent (Claude / Codex)     │
      │  - Writes 100% fresh, original code (e.g. Rust)   │
      │  - Never incorporates original decompiled sources│
      │  - Equips native MCP / CLI / JSON-RPC interfaces │
      └───────────────────────┬──────────────────────────┘
                              │
                              ▼
      ┌──────────────────────────────────────────────────┐
      │          New Open-Source Product                 │
      │ (PhotoCraft, SolidCraft, VectorCraft, OpenPencil)│
      └──────────────────────────────────────────────────┘
```

1. **Specification Extraction**: The analyst uses tools like `rea`, `mitmproxy`, or public RFCs to document interface behaviors, file formats, and features.
2. **Clean-Room Barrier**: The AI coding agent is tasked with writing fresh, unencumbered code (e.g., in pure Rust or TypeScript) strictly conforming to the behavioral specification.
3. **Agent-Native Architecture**: Modern clones build native Model Context Protocol (MCP) servers and JSON control layers directly into the app so AI agents can control the software programmatically.

---

## Community & Discussions

- [The Storytold ArtCraft Announcement](https://github.com/storytold) - Home of the pure-Rust ArtCraft ecosystem and creative suite.
- [Tangency Labs (SolidCraft & Fieldcraft)](https://github.com/tangency-labs) - Parametric 3D CAD modeling and multi-physics simulation in pure Rust with MCP integration.
- [Hacker News Discussions on Clean-Room AI](https://news.ycombinator.com) - Debate and analysis on whether LLM-driven clean-room implementations qualify under traditional IP laws.
- [Reddit r/ReverseEngineering](https://www.reddit.com/r/ReverseEngineering/) - Technical discussions regarding binary analysis, Ghidra, IDA Pro, and machine-assisted decompilation.

---

## Other Awesome Lists

- [AI Rebuilds](https://github.com/a-barzanti/ai-rebuilds#readme) - Tracked list of software and games rebuilt by AI agents and clean-room teams, with weekly star and activity refreshes.
- [Reverse Engineering](https://github.com/michalmalik/awesome-reversing#readme) - Curated list of reverse engineering resources, tools, and training materials.
- [Open Source Alternatives](https://github.com/cloudcommunity/Cloud-Computing-Awesome-List#readme) - Open-source alternatives to commercial software.
- [Model Context Protocol (MCP)](https://github.com/punkpeye/awesome-mcp-servers#readme) - Curated list of Model Context Protocol servers and developer bridges.

---

## Contributing

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

If you know of an awesome project created via reverse engineering, clean-room reimplementation, or AI-assisted cloning:

1. Fork this repository.
2. Create a new branch: `git checkout -b add-my-project`.
3. Add your entry under the appropriate section using the standard format:
   `* [ProjectName](https://url) - Brief description specifying what proprietary software it was cloned or reverse-engineered from.*`
4. Commit your changes: `git commit -m "Add ProjectName"`.
5. Push to the branch: `git push origin add-my-project`.
6. Submit a pull request.
