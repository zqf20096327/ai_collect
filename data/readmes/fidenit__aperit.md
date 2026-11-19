# APERIT

*aperit* (Latin): it opens, it shows · [한국어](README.ko.md)

> **APERIT was called KITE until version 0.3.** Settings, keys and boards made under the old name keep working. The protocol it is built on is [PATET](https://github.com/fidenit/patet).

> A screen full of text is the worst way to use AI.

Humanity built an extraordinary engine and bolted it to a wooden cart. The engine is AI. The cart is a chat window full of text.

Every answer comes back as a scroll of paragraphs. Most of it goes unread. The chat window, a tool made for people typing to each other, became the place where we work with a machine that can do far more than type.

People have already built many excellent project and collaboration tools: Jira, monday.com, Asana, Notion, Trello. Yet in front of AI, all of us went back to plain text. And those tools are too complex, with features spread too wide, to be the place where you talk to an AI.

What we want is one place. Every conversation and every topic lives there, shown as the information you actually need, shaped so it reads at a glance, in an interface that adapts as you speak. No tsunami of text.

APERIT is that place. You say what you need, and the AI arranges the screen for you: a schedule as a timeline, a trip as a route, a choice as a card you tap.

The name is what it does. *Aperit* is Latin for "it opens, it shows": the answer is opened up in front of you, not buried in paragraphs. The language the AI writes it in is called [PATET](https://github.com/fidenit/patet), "it lies open". Only what you need stays in front of you.

Nothing like it existed, so we built it. We hope it makes working with AI less tiring and more productive for everyone.

**Two things live in this repository.**

| | What it is | Where |
|---|---|---|
| **PATET** | The open language an AI writes to build and edit a screen: one op per line, 14 kinds of cards, answers from the user coming back the same way. Any model or agent can write it; any app can render it | [protocol/](https://github.com/fidenit/patet) |
| **APERIT** and **APERIT Pro** | The first products built on it: the desktop app for Windows and macOS described below, and the Android apps | this page, [android/](android) |

![APERIT by FIDENIT: a wall of text gives way to a live board. One request plans a workshop; the route, schedule, budget and checklist appear, and the one decision that needs your confirmation is always shown at the left.](docs/images/hero.gif)

**See it in two minutes.** One request from start to finish, then each part up close: cards shaped to the content, a long project that always shows what to do next and what needs your confirmation, and moving freely around the board.

[![Watch the 2-minute video. A frame from it: weeks into a project, the next decision waits on the left while the board turns to the part of the project it belongs to.](docs/images/promo.jpg)](https://github.com/fidenit/aperit/releases/download/v0.3.0/KITE-promo.mp4)

## What is different

**The screen is the answer.** The AI does not write to you. It edits a board of cards, one line at a time, and you watch the board change. Ask about the same thing again and the same card updates. The board shows where things stand now. It is not a transcript.

![Asking for a to-do list, then reporting progress: the same cards update](docs/images/todo.gif)

**You do not have to say what to do next.** It always shows what to do next and what needs your confirmation. When the AI needs a decision or a value from you, that one card moves to the "my turn" slot beside the conversation, and the board slides to the part of the work it belongs to. Answer it and the next one arrives.

![The AI compares options, then brings the question it needs answered to the "my turn" slot](docs/images/myturn.gif)

Tap any card and it comes to the same slot, with only the cards on the same topic left beside it. Close it and the whole board comes back.

![Dragging the board to another topic, tapping a card: it moves to the left and the board keeps only its topic](docs/images/focus.gif)

**One board for everything.** No chat rooms and no threads. Topics sit on a single canvas, grouped into areas the AI creates, renames and merges as your work grows. One scroll step takes you up a level, from cards to topics to groups; one step back takes you into the group or topic you point at. Drag to move around. Finished work is shelved and comes back when you mention it.

![One scroll step at a time: from a topic's cards out to its group, out to the whole board, then into another group and one of its topics](docs/images/canvas.gif)

**The right card for each piece.** Big numbers, timelines, checklists, progress, tables, charts, forms to fill in, routes, drawings, pictures and web pages. When a topic has more than fits at a readable size, the less important cards fold under "+N more" instead of the text shrinking.

![One request, many kinds of cards: big numbers, a timeline, a bar chart, a checklist, and a form that waits for your confirmation](docs/images/components.gif)

**It draws.** Routes with real distances and travel times, line, bar and donut charts, flows and layouts, pictures. The AI picks the form that reads fastest.

![Asking for a drive: the AI finds the places, reads the travel time and draws the route](docs/images/route.gif)

![A trend line, a budget split and a release flow drawn on request](docs/images/charts.gif)

**It remembers.** Facts worth keeping are picked out after every turn. Old conversations related to what you just said are found and brought along. Everything is stored as plain Markdown in a folder you can open in Obsidian.

**It does the work.** It runs commands, reads and edits files, searches the web and drives a browser on the board. It also has a browser of its own that runs out of sight: it opens sites, fills in forms and clicks through, and shows you the page only when a person is needed, such as a login or a captcha. The last button, like confirming a booking or paying, is left for you to press. Longer jobs are written up as a work order and handed to workers that run in parallel while you keep talking.

**You can talk to it.** Speak and listen instead of typing. Interrupt it while it is speaking.

## Quick start

**Look around first.** With no key, APERIT opens in a demo that plays prepared scenes and says so on screen. To really use it, pick an engine (below).

### Windows: download and run

1. Download the latest `APERIT-…-windows-x64.zip` from [Releases](https://github.com/fidenit/aperit/releases).
2. Unpack it anywhere.
3. Run `aperit.exe`.

There is no installer. On first start a window asks for a key. Skip it to stay in the demo.

### Build from source

| | You need | Command |
|---|---|---|
| Windows | [Rust](https://rustup.rs) `stable-x86_64-pc-windows-gnu`, MinGW ([WinLibs](https://winlibs.com)) | `.\run.ps1` |
| macOS | Rust via rustup, Xcode command line tools | `./run.sh` |
| Linux | not supported yet (see below) | |

`run.ps1` and `run.sh` build and start the program. Add `test` to run the tests, or `pack` to make a folder you can carry (`portable/APERIT`). Steps and code layout: [docs/DEVELOPING.md](docs/DEVELOPING.md).

Linux: the build stops at the GTK and WebKit libraries (`glib-sys`) on a machine without them, and speech, opening the memory folder and the phone tools are written for macOS and Windows. A Linux port is open.

### Pick an engine

The engine is who answers. Open **Settings** at the bottom left and do one of two things: press **Sign in with Claude** (it uses the Claude Code on this computer; no key), or **paste a key**. APERIT tells from the key whose it is (Claude, OpenAI, Gemini, OpenRouter, Groq, xAI) and picks the model. You can also just ask ("switch to Korean", "use Sonnet"); a change of engine or permission opens the window for you to save, and a key pasted into the conversation goes into the window instead of to the model. Everything is on one screen: on the left the ways in (also a local model or another address, a server over SSH, an agent of your own), in the middle what the chosen way needs, on the right what you have spent.

| Engine | You need | What you get |
|---|---|---|
| Demo | nothing | Prepared scenes. Start with no key |
| Claude API | a [Claude API key](https://console.anthropic.com/settings/keys); usage is billed to your account | Everything APERIT does. Paste the key under **Settings** (it is kept encrypted inside the app), or set `ANTHROPIC_API_KEY` |
| Claude Code | [Claude Code](https://claude.com/claude-code) installed and logged in; no API key | Everything, through your Claude Code: its login, `CLAUDE.md`, skills, hooks, MCP servers and permissions apply |
| Claude Code on a server | a server you reach with SSH (a key or a password), with Claude Code installed and logged in there | The same, with the server's files and commands; APERIT's memory and tools stay on your computer ([how](docs/DRIVING.md#a-server-claude-code-over-ssh)) |
| Another model | an OpenAI-compatible endpoint: OpenAI, a local model behind Ollama or LM Studio, OpenRouter | APERIT's own loop with that model. Web search is with Claude only |
| Your own agent | an agent that speaks MCP or AG-UI | The board as your agent's screen. APERIT runs no model |

**Claude Code as the engine.** APERIT hands each turn to it instead of calling the API. Files, commands and the web go through Claude Code's tools. APERIT's own tools (route maps, memory notes, reading the board, workers) are offered to it through a small local MCP server inside APERIT, and workers and memory keeping also run through Claude Code. A turn costs more tokens than with the API key, because Claude Code brings its own instructions. By default it does only what your Claude Code settings allow; the same window lets you allow file edits, or everything. Extra options for Claude Code, such as `--model sonnet`, go in `claude-args.txt` in the program folder.

**Optional second key.** A [TypeSafe AI](https://typesafe.ai) Jev key (**Settings**, or `TYPESAFE_API_KEY`). Jev is a small, fast model that only makes decisions. With it, APERIT picks the topic before answering, puts important cards first, tidies overlapping topics, and recalls only the past conversations that matter. Without it, APERIT works the same.

Keys, the board and the memory vault live in the program's own folder. Move the folder and everything moves with it.

### Use it with your own agent

APERIT draws whatever writes [PATET](https://github.com/fidenit/patet). Your agent does not have to be Claude, and you do not have to change it.

**An agent that speaks MCP** (Claude Code, Cursor, one of your own):

1. In APERIT: **Settings** → **Your own agent** → **Save**.
2. **Settings** again → **Copy the Claude Code command**, and run it in a terminal (other clients: **Copy the config (JSON)**).
3. Ask your agent to answer on the board. It has four tools: `guide`, `board_read`, `screen`, `events`.

**An agent built with an AG-UI framework** (LangGraph, CrewAI, Pydantic AI, ...): give APERIT the agent's address under **Settings** → **Your own agent** → **AG-UI address**.

**A script:** start APERIT with `APERIT_PROTOCOL_PORT=7878` and write lines to that port.

```
topic ws Team Workshop
card k2 decision ws 3x3 Which venue?
set k2 text Where should the workshop be?
add k2 o1 Gangneung | Far, but better facilities
add k2 o2 Gapyeong | Close and cheaper
```

When the user taps Gapyeong, the agent hears `user set k2 chosen o2`.

How each of these works, with the settings: [docs/DRIVING.md](docs/DRIVING.md). The language itself: [protocol/SPEC.md](https://github.com/fidenit/patet/blob/main/SPEC.md), and the [guide to give your model](https://github.com/fidenit/patet/blob/main/GUIDE.md). How it compares with A2UI, json-render, AG-UI and MCP Apps: [protocol/COMPARISON.md](https://github.com/fidenit/patet/blob/main/COMPARISON.md).

## Know before you run

- **APERIT is the interface; the engine decides what happens on your computer.** What may be done without asking is set per engine, under **Settings**:

  | Engine | Commands and file changes |
  |---|---|
  | Claude API, another model | Asked first, with a card in "my turn" (Allow once / Allow all like this / Don't). You can allow file edits, or everything |
  | Claude Code | Your Claude Code permission settings. You can allow file edits, or everything |
  | Your own agent | Whatever your agent does. APERIT only draws its board |

  Reading files and searching the web are not asked about.
- **It costs money as you use it.** By default it uses the most capable Claude model (Opus 5.5); **Settings** offers Sonnet and Haiku too, each with what a turn roughly costs. A turn sends about as much as a Claude Code turn does; what was measured is in [docs/COSTS.md](docs/COSTS.md). **Settings** shows what your Claude API key has spent today and this month, and takes a daily limit: at the limit, no new work starts that day.
- **It is early.** One person uses it daily. English and Korean, switched in the corner; cards and answers follow the language you choose. See [what changed](CHANGELOG.md) and [what is next](docs/NEXT.md) (Korean).
- **Other models and agents are new.** The Claude engines are the ones used every day. The others were checked with real runs (Claude Code connected over MCP as an outside agent; a real server behind the OpenAI-compatible engine; an agent built with Pydantic AI over AG-UI) but are not in daily use, and no model that is not Claude was tried: recognising a key and picking a model for OpenAI, Gemini and the others is untested against those services.
- Distances and times on route cards are read from Kakao Map, so routes work in South Korea.

## For developers

**The protocol** is in [protocol/](https://github.com/fidenit/patet): the [specification](https://github.com/fidenit/patet/blob/main/SPEC.md), the [guide for agents](https://github.com/fidenit/patet/blob/main/GUIDE.md), a [comparison](https://github.com/fidenit/patet/blob/main/COMPARISON.md) with other formats, a JSON schema, examples, [conformance cases](https://github.com/fidenit/patet/tree/main/conformance), and implementations with no dependencies in Rust and JavaScript. Three implementations pass the conformance cases: Rust (the desktop app), Kotlin (the Android app) and JavaScript.

**A board in your own web app:** [`<patet-board>`](https://github.com/fidenit/patet/tree/main/web) is one custom element. What your agent writes goes in as lines, and what the user does comes out as events.

**The desktop app** is Rust and [egui](https://github.com/emilk/egui), with no web front end. With a Claude engine, the model's output is the op stream, applied as each line arrives; the board, written back in the same language, is what the model sees on the next turn. Build steps, the layout of the code and how to add a new kind of card: [docs/DEVELOPING.md](docs/DEVELOPING.md).

**The Android apps** (APERIT with your own key, APERIT Pro with nothing to set up) are in [android/](android), one codebase.

Most of the code was written together with AI (Claude). The idea and the design decisions are human.

## License

[Apache License 2.0](LICENSE). Keep the [NOTICE](NOTICE) file when you redistribute. The name "APERIT" may not be used as the name of a derived product.

---

**FIDENIT** · for the world.
