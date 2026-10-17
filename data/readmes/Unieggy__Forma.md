<p align="center">
  <img src="public/forma-logo.svg" width="340" alt="Forma" />
</p>

<h3 align="center">A reading workspace for technical papers</h3>

<p align="center">
  Read a paper, select an equation, figure, or passage, and get a step-by-step walkthrough —<br/>
  term-by-term math, process and architecture flows, and worked examples — grounded in the paper itself.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-16-000?logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-19-149eca?logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5-3178c6?logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/local--first-privacy-55603c" alt="Local-first" />
</p>

<p align="center">
  <img src="public/screenshot.png" width="900" alt="Forma reading workspace" />
</p>

---

## What is Forma?

Forma is a **local-first** workspace for reading technical and scientific papers the way you actually
study them: not by skimming top to bottom, but by stopping on the hard parts and asking *"what is this
step doing, and why?"*

It works for math, CS, machine learning, robotics, physics, and beyond — anywhere a paper leans on
equations, diagrams, and dense derivations.

Load a PDF and Forma reads the whole thing to build a **semantic paper map**. Click any paragraph,
equation, or figure to attach it as context, ask a question, and get an answer that adapts to what
you selected. Click the same selected paragraph again to clear it when you are done:

- **Equation** → the whole expression first, then each term, then a worked numeric example.
- **Process / architecture** → a numbered, in-order trace of a method, algorithm, or pipeline: what
  enters each step, what it does, and what comes out.
- **Passage** → a plain, conversational explanation, with an example only when it helps.

For machine-learning papers it goes a step further, tracing **real tensor shapes** from input to
output with per-axis meaning and clean ASCII sketches. Everything stays grounded in the loaded paper,
and answers keep paper-grounded claims separate from outside background knowledge.

## Features

- 📄 **Full-document PDF rendering** with one-click paragraph selection and exact figure cropping
- 🔍 **Reader zoom controls** — pinch or ctrl/⌘-scroll on a trackpad, or use the in-reader − / + controls
- 🗺️ **Semantic paper map** — sections, key equations, methods, and figures, each linked to its page
- 🧩 **Adaptive explanations** — equation walkthroughs, process/architecture flows, and plain answers, chosen from what you select
- 💬 **Side questions** — open a compact scratchpad for quick clarifications without interrupting the main conversation; it carries the paper, recent answers, and a lightweight model choice
- ↟ **Prompt recall** — press ↑ in the main composer to revisit sent questions, with ↓ to move forward and restore your draft
- 🔢 **Tensor-shape tracing** for ML papers — dimensions from input to output, with per-axis meaning and ASCII sketches
- ✍️ **Math rendering** — inline and display LaTeX via KaTeX
- 📚 **Local paper library** — every PDF reopens with its own conversation, map, notes, and reading position
- 📓 **Editable notebook** for saving explanations and your own thoughts
- 🔐 **Local-first & private** — the PDF never leaves your browser; extracted text goes only to your locally signed-in agent

## How it works

The PDF is parsed and rendered entirely in the browser. When you ask a question, the extracted
paper text and your current selection are sent to a **locally signed-in agent CLI** — no API keys,
no cloud storage. Answers come back as structured, mode-aware explanations rendered in the side panel.
The compact side-question scratchpad uses a fresh ephemeral branch and receives the full paper plus
the relevant main-thread answer, so a quick follow-up stays grounded without becoming another long
conversation.

```
 PDF (in browser)  ──►  paper map + selection  ──►  local agent CLI  ──►  adaptive walkthrough
```

### Providers

Forma talks to whichever assistant you already have signed in locally:

| Provider | Auth | Notes |
| --- | --- | --- |
| **Codex / ChatGPT** | `codex` app-server (ChatGPT sign-in) | Uses your ChatGPT plan; ephemeral threads |
| **Claude Code** | `claude` CLI (`claude auth login`) | Uses your Claude Code subscription |
| **Gemini** | `gemini` CLI (Google OAuth or `GEMINI_API_KEY`) | Detected automatically when installed |

Conversations are **not** persisted to your ChatGPT or Claude history — they run in ephemeral /
non-persistent mode and are stored only locally inside Forma.

## Getting started

```bash
npm install
npm run dev
```

Then open **http://localhost:3000**, sign in to a provider, and open a PDF.

Sign in to at least one agent first, for example:

```bash
codex login          # Codex / ChatGPT
claude auth login    # Claude Code
```

### Run it like an app (macOS)

Double-click **`Launch Forma.command`** in the project folder — it loads Node, installs
dependencies on first run, starts the server, and opens your browser automatically. Leave the
window open while you use it; press `Ctrl-C` to stop.

## Tech stack

- **Next.js 16** (App Router) + **React 19** + **TypeScript**
- **pdf.js** / **react-pdf** for in-browser PDF rendering and text extraction
- **react-markdown** + **remark-math** + **rehype-katex** for prose and math
- Local agent CLIs (Codex app-server, Claude Code, Gemini) for grounded answers

## Privacy

Your PDF stays in the browser. Only extracted paper text and the current selection are sent to your
locally signed-in agent when you ask a question. Forma stores no provider secrets and creates no
cloud copies of your papers.
