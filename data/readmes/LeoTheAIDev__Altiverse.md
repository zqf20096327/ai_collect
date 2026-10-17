<div align="center">

<img src="./docs/banner.svg" alt="AltiVerse — fork a decision. Watch the worlds it creates." width="760" />

<br/>

**Take one choice. Play it forward as several alternate realities — each a small living world of people who move, stress out, break rules, burn out, form friendships and rivalries, and tell you how it felt.**

[![Live demo](https://img.shields.io/badge/▶_live_demo-altiverse.vercel.app-7c3aed?style=for-the-badge)](https://altiverse.vercel.app/)

[![License: MIT](https://img.shields.io/badge/License-MIT-0a0a0a.svg)](./LICENSE)
![Local-first](https://img.shields.io/badge/local--first-no%20backend-22c55e)
![Vite](https://img.shields.io/badge/Vite-React%20%2B%20TypeScript-646cff)
![Runs offline](https://img.shields.io/badge/runs-fully%20offline-7c3aed)
![Node](https://img.shields.io/badge/Node-18%2B-339933)

**▶ [Try the online demo — no install, no key](https://altiverse.vercel.app/)**

</div>

---

## What is AltiVerse?

AltiVerse forks a single decision — *a school phone ban, a 4-day week, 8- vs 12-hour hospital shifts* — into **2–4 alternate realities** and runs each one forward as a small, living simulation. Up to ~1,000 people with personalities, moods, and relationships move through rooms, react to the policy, and slowly pull the worlds apart. You watch *when* and *why* the realities diverge, click any person to compare how they fare across timelines, and export a full report with a recommendation.

It is a **thinking tool, not a predictor.** Every number and quote comes from a **deterministic** engine (same seed → same world, every time), with an **optional** local or online LLM layer to write the prose: in-character thoughts, Q&A, headlines, and reports. Use it to reason about the **second-order effects** of a decision — the stuff that doesn't show up in a spreadsheet.

> 🔒 **Local-first & private.** No backend. No telemetry. Nothing is uploaded. Runs, presets, and any API key live only in your browser's `localStorage`. It works **100% offline** out of the box.

<div align="center">
  <img src="./docs/screenshots/03-studio.png" alt="Two alternate realities running side by side — Confiscate Phones vs Let Students Self-Regulate — with a shared timeline, living maps, and daily dispatch." width="900" />
  <br/>
  <em>Two realities, one shared timeline — watch both worlds live, side by side.</em>
</div>

---

## Table of contents

- [Quick start](#quick-start)
- [Using a model (optional)](#using-a-model-optional)
- [How to use it](#how-to-use-it)
- [Features](#features)
- [Screenshots](#screenshots)
- [The simulation, explained](#the-simulation-explained)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [Tech & architecture](#tech--architecture)
- [Privacy](#privacy)
- [FAQ](#faq)
- [License](#license)

---

## Quick start

> ▶ **Just want to look around?** Open the **[live demo at altiverse.vercel.app](https://altiverse.vercel.app/)** — runs right in your browser, no install or key needed (deterministic/offline mode; add your own model for the AI prose).

You need [Node.js](https://nodejs.org) **18 or newer**. Then run **one line** — it downloads AltiVerse, installs it, boots the app, and pops open your browser:

```bash
npx github:LeoTheAIDev/Altiverse
```

That's the whole install. No clone, no `cd`, no account, no key, no server — it just opens at **http://localhost:5173** (or the next free port). Nothing to run is built ahead of time.

<details>
<summary><b>Prefer to clone it?</b> (keeps the repo so you can hack on it)</summary>

```bash
git clone https://github.com/LeoTheAIDev/Altiverse.git altiverse
cd altiverse
npm install
npm start          # boots the app and opens your browser at http://localhost:5173
```

</details>

### Other commands

```bash
npm run dev        # dev server (without auto-opening the browser)
npm run build      # type-check + production build into dist/
npm run preview    # serve the production build locally
node bin/altiverse.mjs   # the same one-shot launcher the `altiverse` bin uses
```

> 💡 If you `npm link` (or install globally), the **`altiverse`** command launches the app from anywhere.

---

## Using a model (optional)

AltiVerse runs **fully offline** with deterministic content. Turn on a model to get AI-written scenarios, in-character thoughts, character Q&A, daily headlines, and the final report. It speaks to **any OpenAI-compatible `/chat/completions` endpoint** — open **Settings** and point it wherever you like:

| Mode | Examples | Key needed? |
|------|----------|-------------|
| **Local** *(nothing leaves your machine)* | [Ollama](https://ollama.com) (default `http://localhost:11434/v1`), LM Studio, llama.cpp | No |
| **Online** *(bring your own key)* | OpenAI, OpenRouter, Groq, Together | Yes — stored only in your browser |

```bash
# Local, private, free — using Ollama
ollama pull llama3.2          # or qwen2.5, mistral, gemma3 …
OLLAMA_ORIGINS=* ollama serve  # OLLAMA_ORIGINS=* lets the browser reach it
```

One-click provider presets, a **Model** picker, and a **Test connection** button are built into Settings. Your API key is stored **only** in `localStorage` and sent **straight to the provider you chose** — never to us (there is no us; there's no backend).

<div align="center">
  <img src="./docs/screenshots/08-settings.png" alt="Settings panel with provider presets (Ollama, LM Studio, llama.cpp, OpenAI, OpenRouter, Groq, Together), endpoint, model, API key, and test-connection button." width="820" />
</div>

---

## How to use it

A run goes **Setup → Studio → Report**, and every run is saved to **History** so you can replay it.

### 1 · Set up a scenario

Pick whichever entry point fits how much you want to specify:

- **One-click presets** — *Phones at school · School start time · Office remote work · Hospital shifts · Prison food · Grading*. Loads a complete scenario; just press play.
- **Describe it in a sentence** *(needs a model)* — e.g. *"A hospital deciding between 8- and 12-hour nursing shifts — who burns out, who stays sharp, and how patient care changes."* The model fills in the environment, cast, metrics, and realities.
- **Build it field by field** — full control over environment, the question, each reality's policy, the groups of people, named/pinned characters, metrics, number of days, and the random seed.

<div align="center">
  <img src="./docs/screenshots/02-setup.png" alt="Setup screen: preset chips, a free-text scenario box, environment selector, the question, and the realities to compare." width="820" />
</div>

### 2 · Watch the realities evolve

Press play and watch the worlds run forward day by day on their own **living maps**. People move between rooms, get stressed, break rules, burn out, bond, and clash. Scrub the timeline, change speed, and **click anyone** to open their cross-reality card. Live metrics, trends, the divergence tree, the wellbeing histogram, causal chains, and a per-day newspaper headline all update as you go.

### 3 · Interrogate & report

Open the **Report** for an executive summary, in-character interviews, per-metric explanations, and a **recommendation** for which reality to pick — then export it to **Markdown or PDF**.

<div align="center">
  <img src="./docs/screenshots/09-report.png" alt="Final report modal: recommendation, executive summary, and what the people say — with Copy Markdown and Print/PDF export." width="820" />
</div>

---

## Features

### 🌍 Alternate realities, side by side
- Fork **2–4 realities** from one shared baseline and run them on a **single synchronized timeline**.
- Each reality gets its own **living map** — a pannable 2-D world of rooms (classrooms, hallway, cafeteria, playground, offices…) with agents drifting around via smooth, physics-based motion.
- A per-day **Daily Fork** newspaper headline for each reality (deterministic, or AI-rewritten on demand).

### 🧑‍🤝‍🧑 People who actually live there
- Up to **~1,000 people** with archetypes (the *anxious overachiever*, *jokester*, *rule-bender*, *weary veteran*…), emoji, roles, and personality **traits** (stress-prone, rule-prone, burnout-prone).
- The **same person exists in every reality** — so you can see how *this exact individual* fares under each policy.
- Emergent **relationships, rivalries, popularity, and rumours** that spread day to day — none of it scripted.
- **Click anyone** for a card: their mood strip across all days, a wellbeing score, friends & rivals, AI-written thoughts, and a Q&A box to *ask them questions in character*.

### 📊 See when and why worlds split
- **Live metrics** (0–100) compared across realities — use the **8 defaults** (Focus, Grades, Trust, Stress, Burnout, Rule-breaking, Conflict, Corner-cutting) or define **your own** (up to 10); direction (“higher is better” vs “lower is better”) is auto-detected.
- **Metric trends** — sparklines per metric, every reality on one chart.
- **Divergence tree** — an SVG fan from the shared baseline showing exactly which day the worlds split.
- **Wellbeing histogram** — the *distribution* of how people are doing, not just the average.
- **Causal chains** — a *rule → consequence → second-order effect* breakdown for each reality.

### 🤖 Optional AI layer (bring your own model)
- Works with **any OpenAI-compatible endpoint** — local (Ollama, LM Studio, llama.cpp) or online (OpenAI, OpenRouter, Groq, Together).
- Powers AI scenario generation, in-character thoughts & Q&A, daily headlines, per-metric explanations, interviews, and the recommendation.
- Robust to small-model quirks: malformed JSON is auto-repaired with [`jsonrepair`](https://www.npmjs.com/package/jsonrepair).

### 🎛️ Control & reproducibility
- **Deterministic engine** — a seeded Mulberry32 PRNG means the same seed always produces the same world. **Reseed** to explore variations without re-calling the model.
- Full **timeline controls** — play/pause, step day-by-day, scrub, and **0.5× / 1× / 2× / 4×** speeds.
- **History** — every run is saved (up to 24), replayable, and resumable.
- Export the report to **Markdown / PDF**.

### 🔒 Local-first by design
- **No backend, no telemetry, nothing uploaded.** Runs, presets, and keys live only in your browser. Fully usable offline.

---

## Screenshots

<div align="center">

<table>
  <tr>
    <td width="50%"><img src="./docs/screenshots/01-home.png" alt="Home page" /><br/><sub><b>Home</b> — fork a decision, pick a question</sub></td>
    <td width="50%"><img src="./docs/screenshots/02-setup.png" alt="Setup screen" /><br/><sub><b>Setup</b> — presets, free-text, or field-by-field</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="./docs/screenshots/05-metrics-trends.png" alt="Metrics, trends, divergence tree and wellbeing histogram" /><br/><sub><b>Metrics & trends</b> — divergence tree + wellbeing spread</sub></td>
    <td width="50%"><img src="./docs/screenshots/06-causal-chains.png" alt="Divergence panel and causal chains" /><br/><sub><b>Divergence & causal chains</b> — why the worlds split</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="./docs/screenshots/07-character-card.png" alt="Character card showing one person across realities" /><br/><sub><b>Character card</b> — one person, across every reality</sub></td>
    <td width="50%"><img src="./docs/screenshots/09-report.png" alt="Final report" /><br/><sub><b>Report</b> — recommendation, interviews, export</sub></td>
  </tr>
</table>

<details>
  <summary><b>See the whole studio in one shot</b></summary>
  <br/>
  <img src="./docs/screenshots/04-studio-full.png" alt="The full studio: living maps, daily dispatch, metrics, trends, divergence tree, wellbeing histogram, and causal chains" width="520" />
</details>

</div>

---

## The simulation, explained

| Concept | What it means |
|---|---|
| **Reality / branch** | One alternate world forked from the baseline, defined by a *policy* (e.g. “Confiscate phones at the door”). 2–4 per run. |
| **Persona** | A person who exists across **all** realities — fixed identity, name, archetype, emoji, and traits. |
| **Agent** | That persona *on a given day in a given reality* — with state (stressed / rule-breaking / burned-out) and a position in a room. |
| **Metric** | A 0–100 measure (Focus, Stress, Trust, …). Default set of 8, or define up to 10 of your own. |
| **Event** | Something that happened that day — policy, organic (state-driven), or social (a bond, a clash, a rumour). |
| **Divergence** | The metric-distance between realities over time, the day they first split, and the top metrics driving the gap. |
| **Causal chain** | A *rule → consequence → second-order effect* narrative explaining a reality's movement. |
| **Seed** | The integer that makes a run reproducible. Same seed → identical world. **Reseed** bumps it to explore variations. |

**Environments** ship as presets — **School, Office, Startup, Hospital, Prison, Summer Camp** — each with its own roles (student/teacher, employee/manager, nurse/patient…) and rooms. Type anything else and it builds a custom environment around your text.

**Defaults at a glance:** seed `20260607` · 30 days · 18 members + 4 staff · 2 realities · 8 metrics · speed 1× · model `llama3.2` @ `http://localhost:11434/v1`.

---

## Keyboard shortcuts

*(in the Studio)*

| Key | Action |
|-----|--------|
| `Space` | Play / pause |
| `←` / `→` | Step one day back / forward |
| `Home` / `End` | Jump to the first / last day |
| `Esc` | Close the open character card |
| *click a person* | Open their cross-reality card |

---

## Tech & architecture

- **Vite + React + TypeScript.** No backend, no build step required to run (`npm start`).
- **Deterministic core** — a Mulberry32 PRNG drives every world; each branch runs on a derived seed so realities stay independent yet reproducible.
- **LLM layer** — a thin, dependency-light client (plain `fetch`) against any OpenAI-compatible `/chat/completions` endpoint, with JSON repair for small models. Disable it and everything still works deterministically.
- **Smooth motion** — agents move with spring physics + damping, written straight to the DOM so hundreds render without per-frame React re-renders.
- **Persistence** — runs, presets, and config live in `localStorage` (history capped at 24 entries).

```
src/
├── sim/         # deterministic engine: types, scenario builder, engine, RNG
├── llm/         # OpenAI-compatible client + scenario / thoughts / explain / report
├── components/  # the studio, maps, panels, cards, report, setup, pages
├── hooks/       # simulation clock + agent motion
└── app/         # run history & persistence
```

---

## Privacy

AltiVerse has **no backend** and collects **nothing**.

- Runs, saved presets, and any API key live only in your browser's `localStorage`.
- With a **local** model (Ollama / LM Studio / llama.cpp), **nothing leaves your machine**.
- With an **online** model, requests go **directly** from your browser to the provider you chose — your key is never sent anywhere else.
- Works **fully offline** with deterministic content and no model at all.

---

## FAQ

**Does it predict the future?**
No. It's a structured *thinking tool* for second-order effects — a way to feel out the trade-offs of a decision, not a forecast.

**Do I need an API key or internet?**
No. It runs fully offline and deterministically. A model is optional and only adds the written prose (thoughts, headlines, reports).

**Will my API key leak?**
It's stored only in your browser and sent only to the provider you pick. There's no backend to leak it to.

**Why do two runs look identical?**
Because they're deterministic — same seed, same world. Hit **Reseed** to explore a variation.

**Can I add my own metrics / people / environment?**
Yes — define custom metrics (up to 10), pin named characters with their own personalities, and type any environment you like.

---

## License

[MIT](./LICENSE) — open source. **Fork it, change it, ship it.**

<div align="center">
<br/>
<sub>Built with Vite · React · TypeScript — and a deterministic little universe.</sub>
</div>
