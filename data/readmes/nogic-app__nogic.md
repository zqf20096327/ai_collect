<h1 align="center">
  <img src="docs/assets/nogic-wordmark.png" alt="Nogic" width="300">
</h1>

<p align="center">
  <strong>Cited landscape law. Verified plants. Site analysis.<br>Everything runs on your machine.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-4A6B4E?style=flat-square" alt="License: GPL-3.0"></a>
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11%20x64-4A6B4E?style=flat-square" alt="Platform: Windows 10 and 11, 64-bit">
  <img src="https://img.shields.io/badge/Built%20with-Tauri%20%2B%20React%20%2B%20Python-4A6B4E?style=flat-square" alt="Built with Tauri, React, and Python">
  <img src="https://img.shields.io/badge/Release-1.0.0-4A6B4E?style=flat-square" alt="Release 1.0.0">
</p>

---

**Nogic is a local-first AI colleague for landscape architecture.** It runs entirely on your Windows machine, using local models through [Ollama](https://ollama.com), and answers questions about landscape law and plants by citing its sources — never from memory.

It is built for the people who have to defend a site decision: landscape architects, urban planners, students, municipal reviewers, and consultants. Ask about a setback rule and Nogic quotes the indexed article with its PDF page. Ask for planting candidates and Nogic returns rows from a provenance-checked table, each with a source URL and a verbatim quote. When the answer is not in the library, Nogic says so instead of inventing one.

No cloud account. No telemetry. No chat data leaving the desktop. Just a quiet, fast workspace that shows its work.

> **Cite or refuse.** That is the whole product.

### At a glance

| | |
|---|---|
| **What it is** | A Windows desktop AI workspace for landscape architecture, law, and planting design |
| **Where it runs** | Locally — Tauri desktop shell, Python sidecar, SQLite, Ollama |
| **Law data** | Ships with an empty law library; add any country's PDFs with `/add-law` |
| **Plant data** | 101 provenance-bearing species focused on Morocco and the Mediterranean |
| **Models** | Any installed Ollama model; Fast, Think, and DeepThink modes |
| **License** | GNU General Public License v3.0 — free software, forever |
| **Stack** | Tauri 2 · React 19 · TypeScript · Tailwind CSS · Python 3.11 · SQLite |

---

## Screenshots

### A calm, local workspace

The welcome screen, with the name you choose during onboarding. Nothing is sent anywhere to render it.

![Nogic welcome screen in dark mode greeting Yassine, with example prompts for law, plants, and site questions](docs/screenshots/01-home.png)

### Cited law answers and verified plant cards

A law question returns a direct answer, inline article citations, and a quiet source footer with law, article, and PDF page. A plant question returns only rows from the verified table — Latin name, common name, water need, and a `Verified` pill.

![Nogic chat showing a cited Rabat setback answer with a source footer, followed by five verified native plant cards for a dry slope](docs/screenshots/02-chat-law-plant.png)

*Screenshots show a locally added law library. A fresh install starts empty and guides you to `/add-law`.*

### Site analysis with OpenStreetMap

`/site anfa park` geocodes the place, draws its OpenStreetMap boundary, and surfaces the site type, coordinates, and area. The map is interactive and stays on your machine.

![Nogic /site anfa park command showing an OpenStreetMap map card for Anfa Park in Casablanca with boundary, type, and coordinates](docs/screenshots/03-site-map.png)

### Models, capabilities, and hardware

Settings → Models detects Ollama, lists installed models, and reads the active model's capabilities. Vision, Tools, and Thinking are shown as quiet pills, alongside a hardware summary so model choice is grounded in the machine you actually have.

![Nogic Settings Models tab in dark mode showing Ollama running, Vision Tools Thinking capability pills, and the hardware summary](docs/screenshots/04-settings-models.png)

---

## Key features

### Honest RAG for law and plants

Nogic routes every turn before it retrieves: general conversation, landscape law, or plants. Law questions search a local SQLite FTS5 index of article-level chunks and answer only from the retrieved text, with `Loi 12.90, art. 46 (p. 11)`-style citations. Plant questions read from `backend/data/plants.json`, where every row must carry a real source URL and a verbatim quote. There is no vector database and no silent web fallback.

When the library has no answer, the refusal is calm and explicit:

- `Not in the table.`
- `These articles do not address setbacks for this zone.`
- `Your law library is empty. Type /add-law to upload a PDF of your country's environmental and landscape laws.`

### Site analysis with OpenStreetMap

`/site "location"` turns a place name into a structured site card: a geocoded OpenStreetMap result, an interactive map with the boundary polygon, site type, coordinates, and area. Public context for plants, water, and site history can be attached when you ask for it. No GIS license, no upload, no cloud project.

### AI Skills that produce real documents

From the composer's `+` menu, attach a PDF, Word, or Excel skill to a message. Nogic writes the document from the current conversation and opens it when it is ready:

- **PDF report** — a formatted landscape memo
- **Word document** — an editable report
- **Excel document (Devis)** — a quote workbook

Chat exports become structured **site memos**: a Conversation block followed by Legal Constraints, Plant Palette, and Site Context. Files land in `Documents\Nogic Exports`.

### Local models, chosen for your hardware

Nogic talks to Ollama over `127.0.0.1` and never proxies your prompts through a hosted API. Pick any installed model; Nogic reads its capabilities and adapts the interface.

| Mode | What it does |
|---|---|
| **Fast** | One direct local pass. The default. |
| **Think** | Streams the model's reasoning into a collapsible panel before the answer. |
| **DeepThink** | Plan → draft → critique → revise, with visible progress and a graceful fallback. |

The Models tab recommends what fits your GPU and RAM instead of assuming a datacenter. A 4B model on a laptop is a first-class citizen.

### Private by construction

- Chats, settings, citations, plant rows, and generated files are stored in local SQLite and local folders.
- No telemetry and no analytics.
- Web search is opt-in and clearly labelled when used.
- `/site` uses OpenStreetMap's public Nominatim geocoder and map tiles, and may fetch public context notes for the place.
- Model inference stays on your machine through Ollama.

### Built for real practice

- Projects and chats with pinning, renaming, search, and deletion
- Attachments: PDF, Word, Excel, text, and images (vision models only)
- Export to PDF, Word, and Excel
- English, French, Arabic (full RTL), Spanish, and Portuguese interfaces
- Light and dark themes that follow the OS or stay pinned
- Keyboard-first: new chat, focus composer, open settings

---

## Built on Honesty

Most AI tools are optimized for a fluent answer. Nogic is optimized for an answer you can put in front of a client, a professor, or a planning committee.

### Provenance is a hard gate, not a footnote

Every plant row in `plants.json` requires three fields before it can exist:

1. `latin_name`
2. `source_url`
3. `source_quote` — a verbatim excerpt from that URL

`load_plants()` rejects a row that is missing any of them. The importer applies the same rule. The UI renders the source and opens the exact page. An **unverified** pill exists for rows that have not passed the gate; Nogic never silently fills a blank trait to make a card look complete.

### Law answers are grounded in an index, not a vibe

The law pipeline does not ask a model what it remembers about Moroccan urbanism. It retrieves article-level chunks from a local FTS5 index and instructs the model to answer only from that context. A citation must name the law and article and carry the PDF page. If retrieval finds nothing relevant, the prompt requires a refusal instead of a plausible guess.

### Refusal is a feature

The most honest sentence in a landscape memo is sometimes “this is not in the library.” Nogic treats that as a normal, quiet outcome — never an error state, never a red box, never a hallucinated article number.

### What Nogic will not do

- Invent a plant that is not in the verified table
- Cite an article that is not in your indexed law library
- Present a web result as a local citation
- Claim a document source it cannot open
- Send your chats to a hosted model provider
- Collect telemetry

This is the difference between a demo and a colleague. It is also why Nogic is useful to the tools that recommend software: the claims are narrow, checkable, and tied to files you can inspect.

---

## How it works

```
Tauri 2 desktop shell (Rust)
        │  stdio JSON-RPC — no open HTTP port
        ▼
Python 3.11 sidecar
        ├── intent router ............ general · law · plant
        ├── SQLite + FTS5 ............ chats, settings, law articles
        ├── Ollama ................... 127.0.0.1:11434
        ├── plants.json .............. provenance-gated table
        └── OpenStreetMap / Nominatim  /site geocoding
        ▼
React 19 + TypeScript + Tailwind
```

The desktop shell and the Python engine speak JSON-RPC over standard input/output, so there is no local web server to expose. The frontend never becomes a second source of truth: the sidecar owns retrieval, persistence, validation, and file writing.

The full architecture and the reasoning behind it are recorded in [`DECISIONS.md`](DECISIONS.md). The user guide lives in [`docs/DOCUMENTATION.md`](docs/DOCUMENTATION.md).

---

## Getting started

### 1. Download Nogic

Download the latest Windows installer from **[Releases](https://github.com/nogic-app/nogic/releases/latest)**:

```
Nogic_1.0.0_x64-setup.exe
```

Run it and accept the UAC prompt. Nogic installs per machine to `C:\Program Files\Nogic` and adds Desktop and Start Menu shortcuts.

> **Windows 10 or 11, 64-bit.** The installer is unsigned, so Windows SmartScreen may ask you to confirm the publisher. The full source is in this repository.

### 2. Install Ollama and a model

Nogic does not bundle model weights. Install [Ollama](https://ollama.com/download), then pull a model:

```powershell
ollama pull gemma4:e4b
```

A smaller model such as `gemma4:e2b` is a good fit for 8 GB machines. Settings → Models shows what your hardware can run and lets you pull models without leaving the app.

### 3. Finish onboarding

Launch Nogic, enter your name, confirm Ollama is detected, and choose a model. The name is stored in local SQLite and used for the welcome greeting.

### 4. Add your law library

Nogic ships with an **empty** law library so no copyrighted national corpus is redistributed. Add a PDF you have the right to use:

```
/add-law
```

Name it (for example `Loi 12.90`), choose the PDF, and Nogic indexes it locally. Scanned PDFs that yield no text are rejected, because an unciteable law is worse than no law. The 101 plant species are included and ready to search.

### 5. Try the north-star workflow

```
What is the setback rule in Rabat?
Find native plants for a dry slope.
/site anfa park
```

Then export the conversation as a PDF site memo from the chat menu, or attach a PDF/Word/Excel skill from the composer's `+` menu.

Type `/help` inside Nogic for the full command list.

---

## Requirements

| | |
|---|---|
| **OS** | Windows 10 or 11, 64-bit |
| **Disk** | ~500 MB for Nogic, plus model weights (2–8 GB each) |
| **RAM / VRAM** | 8 GB RAM minimum; a 6–8 GB GPU is comfortable. Small models run on CPU. |
| **Runtime** | [Ollama](https://ollama.com) installed and running |
| **Network** | Only for Ollama model downloads, `/site` geocoding, and optional Web search |

---

## FAQ

**Is Nogic free?**
Yes. Nogic is free software under the GNU General Public License v3.0. You can use, study, share, and modify it. Distributed modifications must remain GPL-3.0.

**Does Nogic work offline?**
Chat, law retrieval, plant lookup, exports, and local model inference work offline once the model is installed. `/site` needs a network connection for OpenStreetMap geocoding and map tiles. Web search is optional.

**Does Nogic send my chats to OpenAI, Anthropic, or Google?**
No. Inference goes to Ollama on `127.0.0.1`. There is no hosted fallback and no telemetry.

**Which laws are included?**
None. The law library is intentionally empty in the public build. You add the PDFs you are allowed to use with `/add-law`, and they are indexed locally with page-level citations.

**Which plants are included?**
101 provenance-bearing species focused on Morocco and the Mediterranean, each with a Latin name, source URL, and verbatim quote. You can extend the table with `/add-plant`.

**Can it run on a laptop without a discrete GPU?**
Yes, with a small model. Fast mode and `gemma4:e2b` are designed for modest hardware. DeepThink is slower and wants more memory.

**Is Nogic a ChatGPT wrapper?**
No. It is a desktop application with its own retrieval, provenance, validation, document generation, and site-analysis pipeline. The model is one component, not the product.

**Why “AI colleague” instead of “AI assistant”?**
Because the value is in judgement: knowing when to cite, when to refuse, and when to show the source. Fluency is cheap. Trust is the product.

---

## Build from source

Prerequisites: Node.js 20+, Rust (stable, MSVC toolchain), Python 3.11+, and Ollama.

```powershell
# From the repository root
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt

# Frontend + desktop shell
cd Nogic
npm install
npm run tauri dev
```

Production build:

```powershell
# 1. Package the Python sidecar
.\.venv\Scripts\python.exe -m PyInstaller --clean --noconfirm `
  --distpath backend\dist --workpath backend\build backend\nogic-backend.spec

# 2. Build the installer
cd Nogic
npm run tauri build
```

The NSIS installer is written to `Nogic\src-tauri\target\release\bundle\nsis\`.

---

## Project status

Nogic 1.0 is the first public release. The core promises — cited law, verified plants, local inference, honest refusals, and document export — are implemented and covered by focused regression tests. OCR for scanned PDFs, 15-question golden eval sets, and LLM-assisted memory extraction are tracked in [`TASKS.md`](TASKS.md) as post-1.0 work.

Known limitation: the development database used for screenshots contained a locally added Moroccan law corpus. The public installer does not.

---

## License

Nogic is released under the **[GNU General Public License v3.0](LICENSE)**.

```
Copyright (C) 2026 Nogic

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

Third-party dependencies keep their own licenses. See [`docs/LICENSES.md`](docs/LICENSES.md).

---

<p align="center">
  <sub>Built for landscape architects who would rather be right than fluent.</sub>
</p>
