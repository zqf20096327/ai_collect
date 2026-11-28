![ai-life-performance-coach by PushBased: Set goals across your projects, areas, and habits. Break them into workstreams of deliverable tasks to plan your years, quarters, months, weeks, and days, then turn completed workstreams into Intermediate Packets to help create new ones. Bring books, articles, and papers, then synthesize them to learn deeply and achieve mastery.](docs/assets/banner.png)

# ai-coach

[![CI](https://github.com/push-based/ai-life-performance-coach/actions/workflows/ci.yml/badge.svg)](https://github.com/push-based/ai-life-performance-coach/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-site-2f6f5e)](https://push-based.github.io/ai-life-performance-coach/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Organize your notes, learn what you read until you can teach it, and plan your days, all in one Obsidian vault.**

ai-coach works on your own notes in an [Obsidian](https://obsidian.md) vault. It does four things:

- **Organize.** It keeps your notes in Projects, Areas, Resources and Archive, and connects them: every task, goal and idea links to the project, area or source it belongs to.
- **Learn.** It takes an idea from a book, a course, a paper or a talk from "I've read it" to "I can teach it", in seven steps. A demanding tutor checks your work at each step and never gives you the answer.
- **See.** It shows your vault in the browser: the graph of your notes, your sources chapter by chapter, your plans and how far you've climbed with each idea.
- **Plan.** With an AI coding agent such as Claude Code or Codex, it plans your year down to your day: goals, projects, tasks and daily habits.

**📖 The full documentation is a [Docusaurus](https://docusaurus.io) site: [push-based.github.io/ai-life-performance-coach](https://push-based.github.io/ai-life-performance-coach/)**, with search.

## Organize: Projects, Areas, Resources, Archive

Your vault follows [PARA](docs/guide/glossary.md#para), from Tiago Forte's _Building a Second Brain_. Everything sits in one of five folders:

| Folder        | Holds                                                              |
| ------------- | ------------------------------------------------------------------ |
| `0.Inbox`     | quick notes waiting to be filed                                    |
| `1.Projects`  | work with an end date, each split into workstreams                 |
| `2.Areas`     | standards you keep up with no end date, such as health or a team   |
| `3.Resources` | what you know: your sources, their chapter notes and concept notes |
| `4.Archive`   | finished projects                                                  |

- `coach init` sets up the folders, and moves your existing ones into place after a preview.
- `coach capture` writes a quick note to the inbox. `coach file` moves it where it belongs, and its sparring history moves with it.
- `coach archive` moves a finished project to the archive. First it suggests which notes to keep in Resources: concept notes, notes you've sparred, and notes that quote a source. When a workstream is done, the planning skills turn its reusable checklists and notes into Intermediate Packets, ready for your next project.
- Links hold it together. A task belongs to its project, workstream or area. A goal links the goal it serves. A concept note quotes the chapter it came from. The graph view draws all of it, and clicking a note shows only what's connected to it.

## Learn: the climb

It starts from what you want to learn. Keep your sources under `3.Resources/0.Raw/`, in a folder per kind:

- **Books** and long **documents**
- **Courses**: handouts, slides and transcripts of the videos
- **Papers and articles**, such as arXiv preprints

Save each one as a PDF.

The vault server converts a PDF into one note per chapter, or into blocks of pages when it has no table of contents. Read it on paper or with `coach read`, then mark it in Obsidian: bold what matters, highlight the best. `coach synthesize` turns your marks into [concept notes](docs/guide/glossary.md#concept-note), one idea each, in your words.

Then you climb each idea:

| Step         | You…                                                    | Command                                  |
| ------------ | ------------------------------------------------------- | ---------------------------------------- |
| 1. Read      | write down what resonated, and sum up each chapter      | `coach read`                             |
| 2. Group     | sort a book's ideas into layers you name                | `coach group`                            |
| 3. Generate  | guess an idea before you look at it                     | `coach generate`                         |
| 4. Retrieve  | explain the idea from memory, then get it judged        | `coach spar`, `coach judge`              |
| 5. Elaborate | say why it works, what it's like and where you'd use it | `coach elaborate`                        |
| 6. Space     | explain it again days later, when it's due              | `coach due`, `coach spar`, `coach judge` |
| 7. Teach     | teach it to a student who believes something wrong      | `coach teach`                            |

A local model ([Gemma](https://ai.google.dev/gemma) on [Ollama](https://ollama.com)) does the sparring, offline. It pushes back on vague answers and buzzwords, and names what you left out:

```text
coach> Explain, as if to a newcomer, why a note is distilled in layers rather than all at once.
you> You bold what matters on the first pass, then highlight the best of the bold.
coach> You said "the best of the bold". What makes one bolded sentence better than
       another when you come back to the note months later?
```

An online judge (Gemini) then checks your answers for gaps. It sees only the questions and your answers, never your notes. `coach study` walks you through what you missed. Each idea comes back for review just before you'd forget it, mixed with ideas from other topics. `coach climb` shows where each idea stands. Read [The climb](docs/guide/the-climb.md) for every step.

## See: your vault in the browser

`npm run coach -- view` opens the [vault view](docs/guide/vault-view.md) at http://127.0.0.1:4747, on your machine only:

- **The graph:** every note and link, by PARA folder, with how well you know each idea. Books fold into their chapters.
- **The reader:** read any note. In a chapter, bold, highlight and summarise right on the page.
- **Plans** (`/plans`): your goals nested under the goals they serve, beside a timeline of the period.
- **The climb** (`/climb`): each idea's steps. Draw how a book's ideas build on each other from memory, then compare your drawing with your structure.

## Plan: your year down to your day

The [planning skills](.agents/skills/README.md) work in any AI coding agent that reads skills and plan in the same vault, as [Planning and habits](docs/guide/planning.md) explains. Say "plan my week" and the agent reviews last week, rolls over what slipped, sets this week's goals under the month's, and lays the tasks out day by day.

- **Goals chain upward:** a day's work serves the week, the week the month, up to the year.
- **Tasks** live in their project, workstream or area, with a size, so a review shows where your effort went.
- **Habits** such as "up at 6:00 🔁 every day" are checked off in each day plan. A missed day is never carried over, and reviews count your streaks.
- **Reviews** for any day, week, month, quarter or year: goals met or missed, effort per project, and what keeps slipping.

## Safe by design

- **One gatekeeper.** Only the [vault server](docs/guide/glossary.md#vault-server) reads or writes your vault. The CLI, the browser view and your AI agent all go through it.
- **Preview first.** Every change is shown before it's written, and nothing is written until you confirm. When you plan or mark a chapter in the browser, a note you changed in Obsidian in the meantime is never overwritten.
- **Your notes stay home.** Sparring runs offline. Only questions and answers go to the judge. See [Privacy](docs/guide/privacy.md) for exactly what leaves your machine, and what your AI agent sees when you plan.

## Quick setup

### 1. Get the tools

| Tool                                                                       | What it's for                             | Cost                     |
| -------------------------------------------------------------------------- | ----------------------------------------- | ------------------------ |
| [Node.js 24+](https://nodejs.org)                                          | runs ai-coach                             | free, open source        |
| [Obsidian](https://obsidian.md) ([download](https://obsidian.md/download)) | where you read, mark and write your notes | free                     |
| [Ollama](https://ollama.com) ([source](https://github.com/ollama/ollama))  | runs the local model that spars with you  | free, open source        |
| A [Gemini API key](https://aistudio.google.com/apikey) (optional)          | the online judge                          | see Google's pricing     |
| An AI coding agent (optional), such as Claude Code or Codex                | the planning skills                       | that agent's plan or key |

Your vault is a folder of plain Markdown files, so it stays readable without any of these. For planning, install these Obsidian community plugins (Settings → Community plugins → Browse):

| Plugin                                                                | Needed      | What it's for                                                                                                  |
| --------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| [Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks)       | yes         | shows the task lists in your plans; without it they show as raw text. Tasks and habits use its syntax          |
| [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) | recommended | opens today's and this week's plan from Obsidian; set it up as in [Planning](docs/guide/planning.md#set-it-up) |

You don't need to turn on JavaScript in the Tasks settings.

### 2. Pull a local model

The sparring partner is [Gemma](https://ai.google.dev/gemma), running on your machine through Ollama:

```sh
ollama pull gemma3          # the sparring partner
ollama pull gemma3:12b      # optional: a larger model that checks your answers more fairly
```

Set the first as `ollama.model` in your config, and the larger one as `ollama.checkModel` if you pulled it.

### 3. Add a Gemini key for the judge (optional)

The judge runs on Gemini, `gemini-4-argon` by default. The example config adds `gemini-3.8-flash` as a fallback for when it's busy. Create a key in [Google AI Studio](https://aistudio.google.com/apikey) and put it in a `.env` file in the repository root, which git ignores:

```sh
GEMINI_API_KEY=your-key-here
```

Without a key, everything works except `coach judge`. Your sessions wait for the judge until you add one.

### 4. Install and run

Try it on a **copy** of your vault first.

```sh
npm install && npx nx run-many -t build
cp coach.config.example.json coach.config.json   # set vault and ollama.model
npm run coach -- init                            # set up the vault folders
npm run coach -- due                             # see what to study today
npm run coach -- view                            # open your vault in the browser
```

[Setup](docs/guide/setup.md) explains each step and how to connect your AI agent. [Your first session](docs/guide/first-session.md) takes one book through the whole loop.

## Learn more

| I want to…                     | Read                                                                              |
| ------------------------------ | --------------------------------------------------------------------------------- |
| Install and connect everything | [Setup](docs/guide/setup.md)                                                      |
| Try the loop on a real book    | [Your first session](docs/guide/first-session.md)                                 |
| Go from familiar to mastered   | [The climb](docs/guide/the-climb.md)                                              |
| Plan my week and keep habits   | [Planning and habits](docs/guide/planning.md)                                     |
| See my vault in the browser    | [The vault view](docs/guide/vault-view.md)                                        |
| Look up a command or a setting | [Commands](docs/guide/commands.md) · [Configuration](docs/guide/configuration.md) |
| Pick how the coach pushes me   | [Coaching styles](docs/guide/coaching-styles.md)                                  |
| Know what leaves my machine    | [Privacy](docs/guide/privacy.md)                                                  |
| Fix an error                   | [Troubleshooting](docs/guide/troubleshooting.md)                                  |
| Understand a term              | [Glossary](docs/guide/glossary.md)                                                |
| See how it's built, and why    | [Architecture](ARCHITECTURE.md) · [Decisions](kb/README.md)                       |
| Change the code                | [Contributing](CONTRIBUTING.md)                                                   |

All of these pages are built from the Markdown in this repository and published to the [documentation site](https://push-based.github.io/ai-life-performance-coach/).

## Code from kb-template

The vault server (`libs/vault/*`, `apps/vault-server` and `apps/climb-board`) was first written in [kb-template](docs/guide/glossary.md#kb-template), a separate, private project, and moved here with its history ([ADR-AIC-0048](kb/source/initiatives/ai-coach/decisions/ADR-AIC-0048-keep-the-vault-server-in-this-repository-behind-the-same-mcp-boundary.md)). It was written for ai-coach. Only these three files hold code that was already in kb-template before that work began:

| File                                                                                                                                                                          | Comes from kb-template's                       | What it is                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [`libs/vault/domain/src/lib/md.ts`](libs/vault/domain/src/lib/md.ts) and [`libs/vault/adapter-markdown/src/lib/markdown.ts`](libs/vault/adapter-markdown/src/lib/markdown.ts) | `core/src/kernel/md/frontmatter.ts`, `yaml.ts` | reading a note's frontmatter and body (`parseFrontmatter`, `extractBody`) and `yamlString`, slightly simplified |
| [`apps/vault-server/src/tool-types.ts`](apps/vault-server/src/tool-types.ts)                                                                                                  | `mcp/src/tool-types.ts`                        | the shape of an MCP tool (`ToolDef`, `defineTool`), copied as is apart from formatting                          |
| [`apps/vault-server/src/main.ts`](apps/vault-server/src/main.ts)                                                                                                              | `cli/src/main.ts`                              | the command dispatcher's shape; the `serve` and `view` commands are new                                         |

Everything else in this repository was written for ai-coach.

Kudos to [Kirill](https://github.com/Karnaukhov-kh), who wrote kb-template. The vault server grew out of kb-template, and all of this was possible thanks to Kirill. Kirill also made kb-kit and the docs-mcp engine, which keep this project's [decision records](kb/README.md).

## Status

ai-coach is a personal project, used daily and still changing. Small local models make mistakes, so treat a sparring verdict as a first opinion. That is what the judge is for.

## License

[MIT](LICENSE) © 2026 push-based.
