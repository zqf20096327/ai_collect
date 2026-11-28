# TutorAI

[![Open the app](https://img.shields.io/badge/Open%20the%20app-yairbarak22.github.io-2563EB?labelColor=black&style=for-the-badge)](https://yairbarak22.github.io/TutorAI/)
[![CI](https://img.shields.io/github/actions/workflow/status/yairbarak22/TutorAI/ci.yml?branch=main&label=CI&labelColor=black&style=for-the-badge)](https://github.com/yairbarak22/TutorAI/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-2563EB?labelColor=black&style=for-the-badge)](LICENSE)
[![Star on GitHub](https://img.shields.io/github/stars/yairbarak22/TutorAI?label=%E2%AD%90%20Star&labelColor=black&color=2563EB&style=for-the-badge)](https://github.com/yairbarak22/TutorAI)
[![Languages](https://img.shields.io/badge/Hebrew%20%7C%20English-RTL%20%2B%20LTR-2563EB?labelColor=black&style=for-the-badge)](#)

![The concept map of a course: concepts in stages from foundations to advanced, colored by mastery, with one concept's prerequisite chain in focus](docs/screenshots/concept-map.png)

TutorAI is an open-source study companion for university students.

Upload a course's materials and it builds a map of the course's concepts, tracks what you already know, and gives you tools that help you learn instead of handing you answers. It runs in your browser with nothing to install and no server, and your materials stay on your computer. If you already pay for Claude or ChatGPT, a one-line install lets you use that plan instead of an API key.

Use it with Claude, with a free open-source model running on your own machine, or both.

**[Open the app →](https://yairbarak22.github.io/TutorAI/)**

## Features

- A daily study session, prepared for you
- A mistakes notebook that brings every mistake back until it is fixed
- Mastery tracking per concept (Bayesian Knowledge Tracing)
- Spaced-repetition flashcards (FSRS)
- A private tutor that asks before it tells, cites the page or slide, and keeps your past conversations
- Step-by-step checking of your own solutions, with algebra verified by SymPy
- New exams in the style of past exams, graded by rubric
- Interactive simulations, plots, and 3D scenes
- Summaries, quizzes, diagrams, and a study plan up to the exam
- PDF, PowerPoint, Word, text, and Markdown
- Claude, local models (Ollama, LM Studio), or a hybrid of the two
- Hebrew and English interface

<table>
<tr>
<td width="50%" valign="top">

### Today's session

One button and about 20 minutes: due flashcards, a second try at past mistakes, questions on your weakest concepts, and one older concept mixed in.

<img src="docs/screenshots/session.png" alt="Today's session: mistakes to fix, flashcards to review, and concepts to strengthen" width="100%">

</td>
<td width="50%" valign="top">

### A tutor that teaches

Socratic by default: it asks a guiding question before giving an answer, and every claim cites a page or slide from your material.

<img src="docs/screenshots/tutor.png" alt="The private tutor answering with a guiding question and citations to lecture slides" width="100%">

</td>
</tr>
<tr>
<td width="50%" valign="top">

### Check my solution

Type or photograph your own work. You get the first mistake and graded hints, never the full answer. Algebra is verified with SymPy, which overrides the model.

<img src="docs/screenshots/check-solution.png" alt="A student's solution checked step by step, with the first mistake marked and a hint revealed" width="100%">

</td>
<td width="50%" valign="top">

### Interactive explainers

Simulations, plots, and 3D scenes generated for a concept, running in a sandbox with no network access.

<img src="docs/screenshots/explainer.png" alt="An interactive explainer of Bayes' theorem with a 2D plot and a 3D surface" width="100%">

</td>
</tr>
</table>

The app is available in English and in Hebrew (right-to-left), and demo mode works in both.

## Why not just study with a chatbot?

A general chatbot is a capable tutor with no memory of you. TutorAI is the system around the model.

| A general chatbot | TutorAI |
|---|---|
| Waits for you to know what to ask | Prepares today's session for you |
| Doesn't know which concepts you have mastered | Tracks mastery per concept across the semester |
| Forgets your mistakes when the chat ends | Brings each mistake back until it is fixed |
| Tends to give the answer | Guides with questions and graded hints |
| Can be confidently wrong on algebra | Checks math steps with SymPy |
| Citations may be invented | Every citation must point to a real page or slide; invalid ones are removed |
| You re-paste material and rewrite prompts | The course is indexed once, and every tool is a tested workflow |

## Getting started

1. Open **[the app](https://yairbarak22.github.io/TutorAI/)**. Chrome or Edge is recommended.
2. Choose where your data lives: a folder on your computer (Chrome and Edge), or browser storage.
3. Choose a model:
   - **Your Claude or ChatGPT plan:** install TutorAI on your computer with one line ([below](#use-your-claude-or-chatgpt-plan-instead-of-an-api-key)) and connect the plan you already pay for.
   - **Claude API key:** paste an API key from [console.anthropic.com](https://console.anthropic.com/settings/keys). It is stored only in your browser.
   - **Local model (free):** run Ollama or LM Studio on your computer. Settings has a ready prompt you can paste into Claude Code to do the whole setup for you.
   - **Demo mode:** no key needed. Answers are prerecorded, on a sample course.
4. Create a course and drag in your files.

You can install the site as an app from the browser menu.

### Use your Claude or ChatGPT plan instead of an API key

Install **TutorAI Local** on your computer with one line. It opens TutorAI in your usual browser and lets you connect:

- **A Claude plan (Pro / Max)** through Anthropic's official Claude Code, which you sign in to yourself. TutorAI never sees your sign-in, and usage counts against your plan. Your use of Claude Code is subject to [Anthropic's terms](https://code.claude.com/docs/en/legal-and-compliance).
- **A ChatGPT plan (Plus / Pro)** with **Continue with ChatGPT** (OpenAI's sign-in for open-source apps).

macOS or Linux, in Terminal:

```bash
curl -fsSL https://yairbarak22.github.io/TutorAI/install.sh | sh
```

Windows, in PowerShell:

```powershell
irm https://yairbarak22.github.io/TutorAI/install.ps1 | iex
```

The installer downloads the program for your computer from this repository's GitHub Releases and checks its checksum. It adds a TutorAI icon and opens the app. No administrator rights are needed, and there are no security warnings to click through. After that:

- **Open it** from its icon: on a Mac press ⌘+Space and type TutorAI (or use Launchpad / Applications); on Windows use the Desktop or Start menu icon.
- **Done for now?** Just close the browser. TutorAI stops by itself after 15 minutes without use, and everything is already saved.

It saves your data in `Documents/TutorAI` (in any browser) and updates itself. `tutorai uninstall` removes it, and your data folder is kept.

## Ask Claude about this project

Paste this into Claude to get a plain-language tour: what the app does, how to start, and how you can contribute.

```text
Help me get to know TutorAI, an open-source study companion for university students.
First read these files from GitHub:
https://raw.githubusercontent.com/yairbarak22/TutorAI/main/README.md
https://raw.githubusercontent.com/yairbarak22/TutorAI/main/CONTRIBUTING.md
https://raw.githubusercontent.com/yairbarak22/TutorAI/main/docs/architecture.md
https://raw.githubusercontent.com/yairbarak22/TutorAI/main/AGENTS.md

Then explain, briefly and in plain language:
1. What the app does, and how it differs from studying with a regular chatbot.
2. How to start using it (https://yairbarak22.github.io/TutorAI/), including the free options and using a Claude or ChatGPT plan through TutorAI Local.
3. How I can contribute, even if I can't code.

Finally, ask me what I study and what interests me, and suggest one specific way I could help.
Answer only from these files. If something isn't in them, say so.
```

Claude needs web access to read the links (Claude Code, or claude.ai with web search on).

## Privacy

- There is no TutorAI server and no telemetry.
- Course files, your progress, and the database (`tutorai.db`) stay on your device. In Chrome and Edge they are regular files in the folder you chose, so you can see them, back them up, or keep them in Google Drive.
- Model calls go straight from your browser to the model you chose, with your own key. You can keep the key only until you close the tab, and the page's security policy blocks the app's requests to any address other than Anthropic and your local model.
- Code written by the model runs in a sandboxed iframe that has no network access and can't read your data.
- Course materials belong to their lecturers. The app never shares them between students.

See [SECURITY.md](SECURITY.md) for the security model.

## Development

TutorAI Local (the program from the install line above) lives in `apps/local`. To run it from source, use `npm run local:dev`. To build the single binary, use `npm run local:build`. Its end-to-end tests run with `npm run e2e:local`. Design: [docs/rfc-local-server.md](docs/rfc-local-server.md).

Requires [Node.js 22](https://nodejs.org) and git.

```bash
git clone https://github.com/yairbarak22/TutorAI.git
cd TutorAI
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173), choose browser storage, and try demo mode. No API key is needed for development.

| Command | What it does |
|---|---|
| `npm run dev` | Start the app with hot reload |
| `npm run check` | Typecheck, unit tests, plugin evals, and browser E2E (run before a PR) |
| `npm test` | Unit tests and recorded plugin evals |
| `npm run e2e` | Playwright student journeys against a production build |
| `npm run eval:live` | Plugin evals against real Claude (needs `ANTHROPIC_API_KEY`) |
| `npm run screenshots` | Regenerate the README screenshots (run against `npm run preview`) |

```
apps/web/          React app (Vite, Tailwind); src/platform = storage, secrets, SymPy worker
packages/sdk/      Artifact schemas, the tool contract, quality checks
packages/core/     Storage, parsing, ingestion, retrieval, model clients, learner model, runtime
plugins/           One folder per tool, discovered automatically
e2e/               Playwright tests
docs/              Architecture, plugin guide, roadmap, maintainer guide
```

## Writing a tool

Every tool is a folder in [`plugins/`](plugins). Most tools need no code: a `plugin.yaml` that describes the inputs and output, and a prompt. The runtime handles retrieval, citations, validation, and rendering, and no tool is merged without passing its evals.

Start with the [plugin guide](docs/plugins.md), or [suggest a tool](https://github.com/yairbarak22/TutorAI/issues/new?template=tool-idea.yml) if you'd like someone else to build it. Students from every faculty are welcome, including non-programmers. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Documentation

- [Architecture](docs/architecture.md)
- [Writing a tool](docs/plugins.md)
- [Roadmap](docs/roadmap.md)
- [Maintainer guide](docs/maintainers.md)
- [Security](SECURITY.md)
- [Contributing](CONTRIBUTING.md) and [Code of conduct](CODE_OF_CONDUCT.md)

## License

[Apache-2.0](LICENSE)
