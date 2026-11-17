# Codjiva

Codjiva is a desktop app that looks like a code editor but shows a **picture of the code** in place of its text.
You open a folder, pick a file, and an AI agent you already use reads the code and draws how it works.

- **Visualise** makes a still, interactive blueprint of one file or one folder. You can pan and zoom, click a
  part to see what it does and where it is in the code, and switch layers on and off.
- **Animate** makes a short narrated film that follows one piece of work through a file and the files around it.
- **Compose** joins the artifacts of several files into one pipeline, where their code meets.

Everything Codjiva makes is plain HTML, saved in a `.codjiva/` folder inside your project. An exported artifact
is one file that opens in any browser, offline.

Codjiva runs on macOS, Windows and Linux. It is built with Tauri and Svelte.

## What you need

One of these, to do the reading and drawing:

| | How Codjiva uses it |
|---|---|
| **Claude Code** | The `claude` program, signed in. This is the best tested path. |
| **Cursor Agent** | The `cursor-agent` program, signed in. Tested with a real run. |
| **Codex CLI, Gemini CLI, Antigravity CLI, Pi** | Supported by definition files that have not yet been confirmed against the real programs. Settings marks them so. |
| **An API key** | For Anthropic, OpenAI, Google Gemini, or any server that speaks the OpenAI chat format (OpenRouter, Ollama, LM Studio). Codjiva then talks to the provider itself and no agent program is needed. |

Open **Settings** (the sliders icon in the title bar, or Cmd/Ctrl+,) to see which agents were found and to add a key.

## Using it

1. **Open a folder.** The explorer on the left lists it. Folders named in `.gitignore` are left out.
2. **Select a file** and click **Visualise**. You can say what the picture should show, or leave that empty.
   The job panel at the bottom shows what the agent is doing. A visual takes about three minutes.
3. **Explore the visual.** Click a part to see its role and a link to the line of code. The **Source** tab shows
   the file itself, read-only.
4. **Animate** asks which companion files the agent should read, what the film should show, and how long it
   should be. Codjiva suggests companions from the file's imports, its tests and the files that use it. Use
   **Ignore always…** next to a suggestion to keep that file, or a whole folder it is in, out of the suggestions
   for good. The story outline appears while the film is being made, and you can change it. The film
   opens on the **Film** tab as soon as it is finished, and plays at 0.75×, 1×, 1.25×, 2× or 4×.
5. **Feedback.** Under the inspector, write what should change. Codjiva attaches the moment of the film you are
   at and, with **Point at…**, the element you mean. A new version is made with only that change.
6. **Compose.** Tick two or more artifacts in the library and click **Compose**. Codjiva proposes joins between
   their ports, and you confirm them.

**Rationale.** A visual or a film says what the code does. Where the code also shows why it is built that
way, the agent records that as a rationale, with the line that gives the reason. Each one is marked "Stated
in the code" when a comment or a name gives the reason, and "Inferred from the code" when the agent concluded
it from how the code works. A rationale is never drawn until you ask for it:

- In a visual, select a part to read its rationale in the inspector. The **Rationale** switch under Layers
  puts a **?** on every part that has one, and a click on the **?** opens it.
- In a film, a bubble that has one carries a small **rationale** chip. Clicking it pauses the film and opens
  the reason inside the bubble. The inspector lists all rationales of the film.

**How long a job takes.** Before a job starts, its dialog says how long it usually takes to make, as a range
such as "8–13 min", and the job panel repeats that next to the running clock. The first estimates come from
how long the code is, how much it branches and, for a film, the length you chose. Codjiva then notes how
long each of your jobs really took and corrects the estimate with them, separately for each agent and
model. Those notes are kept in `timings.json` in the app's settings folder. They hold numbers and the names
of the agent and the model, and no file names or code.

To visualise a **whole folder**, hover the folder in the explorer and click the small icon on its row. Codjiva
tells you how many files and roughly how many tokens that means before you start, because a folder costs more
than a file.

### The three panels

The sidebar on the left, the inspector on the right and the job panel at the bottom work the same way.

- Drag a panel's inner edge to change its size.
- Drag that edge all the way to the side of the window to close the panel.
- A closed panel leaves a short grip on the edge of the window. Drag the grip into the window, or click it,
  to show the panel again.
- The sizes of the panels, and which of them are open, are remembered for the next time the app starts.
- The title bar has a button for each panel. The keys are ⌘0 for the sidebar, ⌥⌘0 for the inspector and ⇧⌘Y
  for the job panel on macOS, and the same with Ctrl in place of ⌘ elsewhere.

### Versions and staleness

Every job adds a version; nothing is overwritten. The version list is in the toolbar, followed by icons that
make the artifact again, export it as one HTML file, open it in the browser and show its files. Each icon says
what it does when the pointer is over it.

**Back** and **Forward**, at the left end of the toolbar, move through the files, tabs and pipelines you have
looked at (⌘[ and ⌘] on macOS, Alt+← and Alt+→ elsewhere). A film that you return to continues
from the moment you left it, for example after you followed a link to a line of code or looked at the Source
tab.

In the explorer, a file that has a visual or a film has a dot, and every folder above it is tinted, so a closed
folder shows that it leads to one. The library under the explorer lists everything that was made. Click its
heading to close it, or drag its top edge to change its height.

Codjiva records a hash of every source file an artifact was made from. When one of them changes, the artifact is
marked **stale** and the inspector names the file. Nothing is regenerated by itself: you decide when to spend an
agent run.

## What it does to your project

- Codjiva writes only inside `<your project>/.codjiva/`. On first use it asks whether to add that folder to
  `.gitignore`.
- The agent is told to write only into the folder of the version it is making. Claude Code is held to that by
  its own permission rules. Other agents cannot be confined that tightly; Settings says what each one can do.
- After every agent run, Codjiva compares the whole project with a snapshot taken before the run. If any file
  outside `.codjiva/` changed, the result is discarded and you are shown the files, with a button that restores
  the ones git tracks.
- Artifacts are shown in a sandboxed frame that can run scripts and nothing else, with a policy that blocks
  every network request. An artifact cannot reach the app, your files or the internet.

## Privacy

- Your code goes only to the agent or provider you chose, in the same way as when you use that agent yourself.
- API keys are stored in the operating system's credential store (Keychain, Credential Manager, Secret Service),
  or read from the provider's environment variable. They are never written to a file.
- Codjiva has no telemetry. It makes two kinds of network request of its own: the calls to an API provider
  that you set up, and a request to GitHub for the newest release, to offer an update. The second can be
  switched off in **Settings › Updates**.

## Settings worth knowing

| Setting | Default | |
|---|---|---|
| Agent | the first one found | Claude Code is used first when it is installed. |
| Model | `sonnet` for Claude Code | The model a job asks the agent for. Type another model's name to use that one. |
| Thinking effort | Automatic | Low for a visual, medium for a film or a pipeline. |
| Fix rounds | 3 | How often a result that fails its checks is sent back to the agent. |
| Spending limit per job | none | For agents that can enforce one. |
| Never suggest these files and folders | `vendor/`, `third_party/`, `node_modules/` | Patterns for third-party and generated code that should not be suggested as companion files. One per line, written like a line of a `.gitignore` file: `vendor/` is every folder of that name, `/internal/generated/` is that one folder, `*.pb.go` is every file with that ending. |
| Look for updates automatically | on | Asks GitHub for the newest release shortly after the app starts and every two hours. With this off, the app looks only when you click **Check for updates**. |
| Theme | Match the system | Light or dark, for the window and for the visuals and films shown in it. An artifact made by an earlier version stays dark until it is made again, and an exported film is dark. |

## Building from source

You need Rust (stable), Node.js 22 and, on Linux, the system packages Tauri lists plus `libdbus-1-dev`.

```sh
cd ui
npm ci
npx tauri dev            # run the app
cd .. && scripts/build.sh   # build an installer for this system
```

`scripts/build.sh` passes its arguments on to `tauri build`. It leaves out the signed bundles for the app's
updater unless the signing key is in the environment, so that anyone can build the app.

### Releases and updates

1. `scripts/set-version.sh 0.2.0`, then commit.
2. `git tag v0.2.0 && git push --tags`.
3. The `Release` workflow builds the installers for macOS (Apple silicon and Intel), Windows and Linux and
   attaches them to a draft release named after the tag, with the updater bundles and `latest.json` next to
   them. Publish the draft when the files look right.

An installed copy of Codjiva reads that `latest.json` a few seconds after it starts and every two hours. When
the release is newer, the title bar offers the update; the app downloads it, checks its signature, installs it
and asks for a restart. **Settings › Updates** has a button to check at once, and a switch that turns the
automatic check off.

The updater bundles are signed with a minisign key. Its public half is in `ui/src-tauri/tauri.conf.json`. The
private half and its password must be in the repository secrets `TAURI_SIGNING_PRIVATE_KEY` and
`TAURI_SIGNING_PRIVATE_KEY_PASSWORD`, or the release build fails. Keep the key safe: an app that is already
installed accepts only updates signed with it. On Linux the updater works for the AppImage only.

### Tests

```sh
cargo test --workspace                   # the core, the builder and the app shell
cd ui && npm run check && npm test       # the interface: types and unit tests
cd ui && npm run build && npm run e2e    # the interface in a real browser, with a stand-in backend
cd runtime/test && npm ci && npm test    # the runtime: frames, self-test, three browser engines
scripts/selfcheck.sh                     # the real app window touring itself (macOS)
```

`scripts/selfcheck.sh` can also run real jobs with a real agent on a copy of a fixture; see the comments at
the top of the script and `fixtures/README.md`.

### Formatting

The code is formatted by tools, with lines of at most 80 columns: Prettier for JavaScript, TypeScript, Svelte
and CSS, and rustfmt for Rust. ESLint looks for mistakes in the JavaScript, TypeScript and Svelte code.

```sh
npm ci                # once, at the top of the repository: installs Prettier and ESLint
npm run format        # formats every file and wraps comments that are too wide
npm run style         # what CI runs: is everything formatted, lint, and the width of lines
```

`.editorconfig` gives editors the same indentation and width. A long string, a web address and the markup of
a Svelte file may be wider than 80 columns; `scripts/line-width.mjs` lists the cases. The test data in
`fixtures/` and the example film in `runtime/reference/` are not formatted.

### Where things are

| Folder | |
|---|---|
| `runtime/` | The JavaScript that every artifact carries: the drawing parts, the film engine, the self-test. |
| `crates/codjiva-build/` | Turns an agent's source files into one HTML page, after checking them. |
| `crates/codjiva-core/` | Workspaces, agents, jobs, artifacts and the write guard. No user interface. |
| `ui/` | The Svelte interface and, in `ui/src-tauri/`, the Tauri shell. |
| `resources/` | Prompts, schemas, agent definitions, fonts and the theme. |
| `fixtures/` | Small workspaces for testing, and sessions recorded from real agent runs. |
| `scripts/` | Scripts for testing, for the landing page, and for formatting. |
| `landing/` | The project's web page. `scripts/landing.sh` builds its live examples, and a workflow publishes it to GitHub Pages. |

More: [adding or changing an agent](docs/AGENTS.md).

## Licence

Codjiva is licensed under the [Apache License, Version 2.0](LICENSE). The bundled JetBrains Mono typeface is
licensed under the SIL Open Font License; see [NOTICE](NOTICE).
