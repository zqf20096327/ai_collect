<h1 align="center">
  <a href="https://kition.ai"><img src="public/logo-mark.png" alt="Kition logo" width="64" valign="middle" /></a> Kition
</h1>

<p align="center">
  <strong>English</strong> ·
  <a href="docs/readme/README.zh-CN.md">简体中文</a> ·
  <a href="docs/readme/README.ru-RU.md">Русский</a> ·
  <a href="docs/readme/README.ja-JP.md">日本語</a> ·
  <a href="docs/readme/README.vi-VN.md">Tiếng Việt</a> ·
  <a href="docs/readme/README.fr-FR.md">Français</a> ·
  <a href="docs/readme/README.de-DE.md">Deutsch</a> ·
  <a href="docs/readme/README.es-ES.md">Español</a>
</p>

<p align="center">
  <strong>Kition: the open pro suite for AI.</strong><br />
  Notes, tables, boards and professional editors in one desktop workspace, edited by you and your agent.
</p>

<p align="center">
  <a href="https://github.com/KitionAI/kition/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/KitionAI/kition/ci.yml?branch=main&amp;style=flat-square&amp;logo=githubactions&amp;logoColor=white&amp;label=CI" alt="CI status" /></a>
  <a href="https://github.com/KitionAI/kition/releases/latest"><img src="https://img.shields.io/github/v/release/KitionAI/kition?include_prereleases&amp;sort=semver&amp;style=flat-square&amp;color=5645d4" alt="Latest release" /></a>
  <a href="https://github.com/KitionAI/kition/releases"><img src="https://img.shields.io/github/downloads/KitionAI/kition/total?style=flat-square&amp;color=5645d4&amp;label=downloads" alt="Total GitHub release downloads" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/KitionAI/kition?style=flat-square&amp;color=5645d4" alt="License: Apache-2.0" /></a>
  <img src="https://img.shields.io/badge/status-beta-f5d75e?style=flat-square" alt="Project status: beta" />
  <img src="https://img.shields.io/badge/macOS-supported-5645d4?style=flat-square&amp;logo=apple&amp;logoColor=white" alt="macOS supported" />
  <img src="https://img.shields.io/badge/Windows-supported-5645d4?style=flat-square&amp;logo=windows11&amp;logoColor=white" alt="Windows supported" />
  <img src="https://img.shields.io/badge/Linux-experimental-f5d75e?style=flat-square&amp;logo=linux&amp;logoColor=111827" alt="Linux experimental" />
</p>

<h3 align="center"><a href="https://github.com/KitionAI/kition/releases/latest"><ins>Download Kition</ins></a></h3>

<p align="center">
  <a href="https://kition.ai">Website</a> ·
  <a href="https://github.com/KitionAI/kition/releases/latest">Download</a> ·
  <a href="https://github.com/KitionAI/kition/discussions">Discussions</a> ·
  <a href="https://discord.gg/bFSjRDjVY">Discord</a> ·
  <a href="https://www.reddit.com/r/Kition">Reddit</a> ·
  <a href="https://x.com/KitionAI">X</a> ·
  <a href=".github/CONTRIBUTING.md">Contributing</a> ·
  <a href=".github/SUPPORT.md">Support</a> ·
  <a href=".github/SECURITY.md">Security</a>
</p>

<p align="center">
  <img src="docs/readme/kition-overview.webp" alt="Kition product overview showing documents, structured data tables, boards, and Agent research" width="100%" />
</p>

Kition brings Markdown documents, structured table files, infinite
Boards, a tool-using AI agent, and web research into one desktop workspace.
Instead of making every task begin in a blank chat, Kition gives the Agent
editable project files, typed records, and attachments to work with. This
makes AI work easier to inspect, correct, and repeat without handing context
between disconnected tools.

> Kition is currently in beta. Back up important workspaces and review agent
> changes before relying on them in production workflows.

## Why Kition

- **Connected documents.** Write Markdown with live preview, links, backlinks,
  callouts, code, math, diagrams, daily notes, and export.
- **Structured data beside the knowledge.** Turn research and content into
  typed records, formulas, filters, groups, views, attachments, and AI fields.
- **Visual thinking with reviewable AI changes.** Build diagrams, mind maps,
  flows, and freeform sketches on a Board, then review the Agent's changes
  before keeping them.
- **An Agent that can act.** Search the web, inspect documents and
  table schemas, update content, and save useful output into the active project.
- **Reviewable document edits.** Let the Agent edit the active document, inspect
  every addition and deletion, then accept or reject individual changes.
- **Kits for every kind of file.** Sixteen kits in four product lines open sheets, slides,
  photos, films, CAD drawings, and more as ordinary workspace files, and the Agent
  works on them through each kit's tools. See [Kits](#kits).

## Let the Agent Edit—Keep the Final Say

Instead of returning another suggestion to copy and paste, the Kition Agent can
read the active Markdown document, make scoped changes, and write the result
back into the workspace. The document and the complete task trace remain
visible together while the Agent works.

<p align="center">
  <img src="docs/readme/agent-document-edit.webp" alt="Kition open source AI Agent reading and editing the active Markdown document beside a visible tool execution trace" width="100%" />
</p>

When a file changes outside the editor, Kition opens a document review surface
that highlights additions, deletions, and rewrites. Each change can be accepted
or rejected individually, or the complete edit can be reviewed as one set.

<p align="center">
  <img src="docs/readme/agent-document-diff-review.webp" alt="Kition document diff review showing AI additions and deletions with controls to accept or reject each change" width="100%" />
</p>

This creates a controlled document workflow: describe the goal in natural
language, let the Agent edit the real file, inspect the diff, and decide exactly
what remains in the final document.

## Start With Work, Not a Blank Prompt

A capable Agent is useful, but a blank prompt still asks the user to design the
task, describe every input, choose an output format, and recover when a step
goes wrong. Kition moves that complexity into familiar work surfaces:
documents, table fields, records, and templates.

The built-in scenarios below are ordinary `.ktable` files. Their prompts,
field relationships, generated assets, and review states stay visible and can
be adapted to a real project.

### Generate campaign assets in batches

Start with a key message and a face photo. Typed fields keep the content type
and intended emotion explicit, while AI fields generate linked 16:9 and 9:16
thumbnail variants for every record. The table becomes both the batch queue and
the review surface.

<p align="center">
  <img src="docs/readme/scenarios/thumbnail-generator.webp" alt="Kition table generating 16:9 and 9:16 video thumbnails from messages, portraits, content types, and emotions" width="100%" />
</p>

### Turn receipt images into searchable records

Drop receipt photos into an attachment field. Vision-powered fields extract
the vendor, address, category, structured JSON, and plain OCR text directly
into the same row. The results can then be filtered, corrected, or summarized
by the Agent.

<p align="center">
  <img src="docs/readme/scenarios/receipt-ocr.webp" alt="Kition receipt OCR table extracting vendor, address, category, structured data, and plain text from images" width="100%" />
</p>

### Expand one product brief into a complete asset pipeline

One product concept can drive multiple design candidates, orthographic views,
a feature image, a lifestyle shot, a style board, and launch copy. Each result
remains attached to the source record, so the full chain is easier to compare,
regenerate, and hand off than a collection of disconnected chat outputs.

<p align="center">
  <img src="docs/readme/scenarios/batch-product-designer.webp" alt="Kition batch product design table with generated designs, orthographic views, feature images, lifestyle shots, style boards, and launch copy" width="100%" />
</p>

These scenarios show the intended Kition loop: use documents for narrative
context, tables for structured state, Boards for visual thinking, and the
Agent for uncertain work.

## Product Tour

<table>
<tr>
<td width="42%" valign="middle">

### Write connected documents

Write Markdown with live preview, internal links, backlinks, tags, outlines,
embeds, callouts, code, math, diagrams, templates, daily notes, and tabs.
Export finished work to PDF when it needs to leave
the workspace.

</td>
<td width="58%">
  <img src="docs/readme/documents.webp" alt="Kition document editor showing Markdown content and workspace navigation" width="100%" />
</td>
</tr>
<tr>
<td width="58%">
  <img src="docs/readme/tables.webp" alt="Kition structured table with typed fields, views, filters, and record controls" width="100%" />
</td>
<td width="42%" valign="middle">

### Turn data into useful tools

Create structured table files with typed fields, attachments, formulas, filters,
sorting, grouping, multiple views, and fast record editing. Use them for
research, content pipelines, lightweight CRM, inventory, or project tracking.

</td>
</tr>
<tr>
<td width="42%" valign="middle">

### Give the agent real context

Ask the Kition agent to read and update documents, inspect table schemas,
create or modify records, search the web, use tools, and follow a
plan. Agent output can be written back into the active workspace.

</td>
<td width="58%">
  <img src="docs/readme/agent.webp" alt="Kition Agent working beside a document and saving a result into the workspace" width="100%" />
</td>
</tr>
<tr>
<td width="58%">
  <img src="docs/readme/boards.webp" alt="Kition Board with a launch mind map and a process flow chart in the Board kit" width="100%" />
</td>
<td width="42%" valign="middle">

### Think and plan visually

Build diagrams, mind maps, flowcharts, sticky-note clusters, and freeform
sketches on an infinite canvas. Boards are `.kboard` files the Board kit edits,
and the Agent works on them through the kit's tools, live or as a draft you
review before it becomes part of the workspace.

</td>
</tr>
</table>

## Kits

A kit is an editor for one kind of file. Its engine is compiled to WebAssembly
and runs in a Web Worker, and the kit draws its own editor inside Kition. The
Agent edits the same files through the kit's tools, so its changes stay
visible and reviewable. Kition's kits come in four product lines; the packages
Kition ships are pinned in [`kits/kits.lock.json`](kits/kits.lock.json).

<p align="center">
  <a href="https://github.com/KitionAI/kition-showcase"><img src="docs/readme/kits-grid.webp" alt="Sixteen files made with Kition's kits, one per kit in the order of the table below: a release plan note, a task tracker table, a mind map board, a magazine feature document, a sign-up forecast spreadsheet with a chart, a dashboard slide, an annotated PDF report, a coffee shop landing page, a sale poster, a mountain lake illustration, a garden trifold, an analytics dashboard design, an aurora title card, a logo reveal, a lighting circuit drawing and a 3D donut." width="100%" /></a>
</p>

Each picture is a file a kit built with its own commands and rendered with its
own engine; more of them are in
[Kition Showcase](https://github.com/KitionAI/kition-showcase).

| Product line | Kit | Edits | Opens | Creates |
| --- | --- | --- | --- | --- |
| Office | [Note](https://github.com/KitionAI/kition-note) | Markdown notes, saved byte for byte | `.md` `.markdown` | `.md` |
| Office | [Table](https://github.com/KitionAI/kition-table) | Tables, views and dashboards in one file | `.ktable` | `.ktable` |
| Office | [Board](https://github.com/KitionAI/kition-board) | An infinite whiteboard for diagrams, mind maps and sketches | `.kboard` | `.kboard` |
| Office | [Doc](https://github.com/KitionAI/kition-doc) | Word-processing documents (`.docx`) | `.docx` `.html` `.htm` | `.docx` |
| Office | [Sheet](https://github.com/KitionAI/kition-sheet) | Spreadsheets (`.xlsx`) with formulas | `.xlsx` `.xlsm` `.xltx` `.xltm` `.xls` `.xlt` `.et` `.ett` `.xlsb` `.ods` `.csv` | `.xlsx` |
| Office | [Slide](https://github.com/KitionAI/kition-slide) | Slides, including `.pptx` files | `.kslide` `.pptx` | `.kslide` |
| Office | [PDF](https://github.com/KitionAI/kition-pdf) | Read and edit PDF files | `.pdf` | `.pdf` |
| Office | [HTML](https://github.com/KitionAI/kition-html) (Preview) | HTML pages, with a live preview | `.html` `.htm` | `.html` |
| Design | [Photo](https://github.com/KitionAI/kition-photo) | Layered images, including `.psd` files | `.psd` `.psb` `.kphoto` | `.psd` |
| Design | [Vector](https://github.com/KitionAI/kition-vector) | Vector graphics | `.kvector` `.svg` `.ai` `.eps` | `.kvector` |
| Design | [Layout](https://github.com/KitionAI/kition-layout) | Page layouts: flyers, posters and books | `.klayout` `.idml` | `.klayout` |
| Design | [Design](https://github.com/KitionAI/kition-design) (Preview) | Interface and screen designs | `.kdesign` `.fig` `.sketch` | `.kdesign` |
| Media | [Film](https://github.com/KitionAI/kition-film) | Video timelines | `.kfilm` | `.kfilm` |
| Media | [Motion](https://github.com/KitionAI/kition-motion) | Motion graphics with keyframes and effects | `.kmotion` | `.kmotion` |
| Engineering | [CAD](https://github.com/KitionAI/kition-cad) | 2D CAD drawings (`.dxf`) | `.dxf` | `.dxf` |
| Engineering | [Scene](https://github.com/KitionAI/kition-scene) (Preview) | 3D scenes | `.kscene` | `.kscene` |

Kits marked Preview are early: expect gaps. All sixteen ship with Kition.

Each kit is developed in its own repository; see
[Kits](docs/kits.md) for how kits plug into Kition.

Also included:

- AI-assisted table fields for generating text, structured values, and media
  from record context.
- Model, proxy, MCP, account, usage, update, and desktop integration settings.
- A seeded Getting Started workspace with practical document and table
  examples.

## Install

Desktop builds are published through
[GitHub Releases](https://github.com/KitionAI/kition/releases/latest).

- **macOS (Apple silicon or Intel):** download the latest `.dmg`.
- **Windows (x64):** download the latest `-setup.exe` installer.
- **Linux (experimental):** download the latest x86_64 `.AppImage`.
- **Previous versions:** browse the complete
  [release history](https://github.com/KitionAI/kition/releases).

## Open Source Boundary

Everything that makes up the Kition desktop app is open source in this
repository:

- the React renderer (`src/`): document, table, Agent, settings, scenario,
  and kit-host UI;
- the Tauri desktop shell (`src-tauri/`) and desktop integration;
- the Rust runtime (`crates/`), which the shell runs in-process and which
  serves its HTTP API on loopback only. See
  [Runtime development](docs/runtime-development.md);
- the runtime contracts in [`contracts/runtime/`](contracts/runtime/), mocks,
  fixtures, and black-box tests;
- the kit pins (`kits/`) and packaging and release workflows.

Kits are developed in separate repositories. Kition ships each kit's published
package, pinned by version and checksum in
[`kits/kits.lock.json`](kits/kits.lock.json).

## Contributing

Issues and pull requests are welcome. How to run Kition from source, the
repository layout, and the technology it uses are in
[CONTRIBUTING.md](.github/CONTRIBUTING.md).

1. Follow the [Kition Development Standard](docs/development-standard.md),
   including the recommended Orca worktree workflow.
2. When a change crosses the renderer and the runtime, update the contract in
   `contracts/runtime/`, the renderer mock, and the runtime together.
3. Report security-sensitive issues through
   [.github/SECURITY.md](.github/SECURITY.md), not a public issue.

For product questions, account help, and private workspace concerns, see
[.github/SUPPORT.md](.github/SUPPORT.md).

## License

Kition, including its runtime in `crates/`, is licensed under Apache-2.0
([LICENSE](LICENSE)).
