# Codjiva

Codjiva is a desktop app that looks like a code editor but shows a **picture of the code** in place of its text.
You open a folder, pick a file, and an AI agent you already use reads the code and draws how it works.

[![A film made by Codjiva. An order moves through the machines of a Go order handler, and a caption explains each step.](docs/images/film.gif)](https://aayushch.github.io/codjiva/#demo)

*A film Codjiva made from [one Go file](fixtures/go-orders/internal/orders/handler.go). This recording is
silent. [The project's web page](https://aayushch.github.io/codjiva/#demo) plays the same film with sound.*

- **Visualise** makes a still, interactive blueprint of one file or one folder. You can pan and zoom, click a
  part to see what it does and where it is in the code, and switch layers on and off.
- **Animate** makes a short narrated film that follows one piece of work through a file and the files around it.
- **Step through** makes a drawing of a file's states that you can run: type an input or pick an example, and
  step forwards and backwards through what the code does with it, with every variable and output in view.
- **Compose** joins the artifacts of several files into one pipeline, where their code meets.
- **Four views that Codjiva lays out from data**, for code that is not a flow of work:
  - **Schema** shows the data shapes of a file: every type with its fields, how the types refer to each other,
    and which code reads and writes each field.
  - **Lanes** shows who talks to whom in time order, one message at a time, with a scenario for each way the
    exchange can go.
  - **Structure** shows a data structure in memory: type a sequence of operations and step through what each
    one does to it.
  - **Map** shows a folder level by level, down to single functions, and links each file to everything that
    was made of it.

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
2. **Select a file.** Its card lists the six views that can be made of it. Click **Visual**. You can say what
   the picture should show, or leave that empty. The job panel at the bottom shows what the agent is doing. A
   visual takes about three minutes.
3. **Explore the visual.** Click a part to see its role, the lines of its code, what it reads and writes, where
   the work goes from it, and the edge cases the agent found in it. The **Source** tab shows the file itself,
   read-only.
4. **Film** on the card asks which companion files the agent should read, what the film should show, and how
   long it should be. Codjiva suggests companions from the file's imports, its tests and the files that use
   it. Use **Ignore always…** next to a suggestion to keep that file, or a whole folder it is in, out of the
   suggestions for good. The story outline appears while the film is being made, and you can change it. The
   film opens on the **Film** tab as soon as it is finished, and plays at 0.75×, 1×, 1.25×, 2× or 4×.
5. **Step through.** Click **Step-through** on the card of a file. It suits a parser, a state machine,
   a validator or any other code whose behaviour depends on its input. The agent draws the states and writes
   a step function that restates the code. You then run it on the examples it chose or on your own input,
   one step at a time. The same command is in the menu that a right-click on a file opens.
6. **The other views of a file** are behind the **More** tab: Schema, Lanes and Structure. Its menu says what
   each one is for. Choose one to open its tab, and click its small card there to make it. A folder has a
   **Map** tab. The same commands are in the menu that a right-click in the explorer opens. On a map, click a
   box twice to see what is inside it.

   **Not sure which one to make?** A file can be shown in six ways: Visual, Film, Step-through, Schema, Lanes
   and Structure. The card of a file has a small card for each, and a click on one starts making it. Click
   **Which view fits this file?** under them, or choose the same command in the menu of the **More** tab.
   Your agent reads the file and ranks the six, with one sentence of reason for each. The first is marked as
   suggested on the card and its tab is underlined. Point at a small card to read the agent's reason for
   that view. The answer takes a few seconds and is kept until the file changes. It only suggests: you can
   make any of the six.
7. **Feedback.** Under the inspector, write what should change. Codjiva attaches the moment of the film you are
   at and, with **Point at…**, the element you mean. A new version is made with only that change.
8. **Compose.** Tick two or more artifacts in the library and click **Compose**. Codjiva proposes joins between
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

### Following names in the Source view

The **Source** tab shows a file read-only, and the names in its code can be followed.

- Click a name to select it. Its other uses in the file are marked, and the panel on the right lists where
  the name is defined and where it is used. Click a place in a list to go there. Esc selects nothing.
- ⌘-click a name (Ctrl+click on Windows and Linux) to go to its definition. F12 does the same for the selected
  name, and Shift+F12 lists its references.
- A right-click on a name offers the same commands. For C and C++ it also offers **Go to declaration**, which
  is the prototype in the header, where **Go to definition** is the function with its body.
- ⌘T (Ctrl+T) goes to a definition by its name. It is the dialog of ⌘P with a `#` in front of the text.
- **Back** returns to the line you came from.

Codjiva reads the code itself for this and starts no other program. It knows names, scopes, what each class
derives from and the type written next to a field or a variable. It does not work out the type of every
expression, as a compiler does. That gives two kinds of answer, and the panel says which one you are looking
at:

- A parameter or a local variable is found **exactly**, with all of its uses.
- Anything else is found **by name**. Every definition with that name is a candidate, and the code around the
  name decides which candidates are likely:
  - A candidate that belongs to the owner of the name comes first. In `sink.write()` the owner is the type
    written for `sink`, whether `sink` is a local variable or a field. In a method of a C++ or Java class, a
    name with nothing in front of it can belong to that class.
  - A candidate that the owner inherits comes next: a member of a base class, of an implemented interface, of
    a struct embedded in a Go struct, or of a Rust trait the type implements.
  - Then come candidates in the same file, in a file the file imports, and in the same folder.

  The panel shows the likely candidates. The others, which only have the same name, are behind the line
  **Others with this name**. Codjiva goes straight to a definition only when one candidate is clearly the
  closest. The references of such a name are every use of that name, so two different things with one name
  are listed together.

When the code writes a type for the selected name, as in `const Reading last = ...`, the panel also lists
where that type is defined, under **Type**.

Parsed languages are C, C++, Go, Java, JavaScript, Python, Rust and TypeScript, and the code between the
`<script>` tags of Svelte and Vue files. Any other language is read as text: a definition is a name after a
keyword such as `class` or `def`, and a use is the same word. A name that is defined outside the open folder,
for example in a standard library, is not found.

### Versions and staleness

Every job adds a version; nothing is overwritten. The version list is in the toolbar, followed by icons that
make the artifact again, export it as one HTML file, open it in the browser and show its files. Each icon says
what it does when the pointer is over it.

**Back** and **Forward**, at the left end of the toolbar, move through the files, tabs and pipelines you have
looked at (⌘[ and ⌘] on macOS, Alt+← and Alt+→ elsewhere). A film that you return to continues
from the moment you left it, for example after you followed a link to a line of code or looked at the Source
tab.

In the explorer, a file that has a visual or a film has a dot, and every folder above it has a smaller dot, so a
closed folder shows that it leads to one. Only the selected row has a coloured background. The library under the explorer lists everything that was made. Click its
heading to close it, or drag its top edge to change its height.

Codjiva records a hash of every source file an artifact was made from. When one of them changes, the artifact is
marked **stale** and the inspector names the file. Nothing is regenerated by itself: you decide when to spend an
agent run.

## What it does to your project

- Codjiva writes only inside `<your project>/.codjiva/`. On first use it asks whether to add that folder to
  `.gitignore`.
- The agent is told to write only into the folder of the version it is making. Claude Code is held to that by
  its own permission rules. Other agents cannot be confined that tightly; Settings says what each one can do.
- After every agent run, Codjiva compares the whole project with a snapshot taken before the run. If a file
  outside `.codjiva/` changed, the job panel lists it, with a button that restores the files git tracks to
  their last commit. Codjiva cannot tell whether the agent or you changed a file, so the job is not stopped,
  and a visual or film made from a changed file is marked stale. A job that changes an already saved version
  is stopped and its result is discarded.
- The answer to **Which view fits this file?** is kept in `.codjiva/suggestions/`. The agent is given the
  file's text for that question and draws nothing. With Claude Code it is asked with the small model, `haiku`,
  whatever model Settings names for jobs.
- Several jobs can run at the same time. Only a second job for the same visual, film or pipeline has to wait
  until the first has ended.
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

You need Rust (stable), a C compiler, Node.js 22 and, on Linux, the system packages Tauri lists plus
`libdbus-1-dev`. The C compiler builds the parsers that code navigation reads source files with.

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
| `crates/codjiva-nav/` | Code navigation for the Source view: where a name is defined and where it is used. |
| `ui/` | The Svelte interface and, in `ui/src-tauri/`, the Tauri shell. |
| `resources/` | Prompts, schemas, agent definitions, the queries of code navigation, fonts and the theme. |
| `fixtures/` | Small workspaces for testing, and sessions recorded from real agent runs. |
| `scripts/` | Scripts for testing, for the landing page, and for formatting. |
| `landing/` | The project's web page. `scripts/landing.sh` builds its live examples, and a workflow publishes it to GitHub Pages. |

More: [adding or changing an agent](docs/AGENTS.md), and
[adding a language to code navigation](resources/nav/README.md).

## Contributing

Read the [contributing guide](.github/CONTRIBUTING.md) before you open an issue or a pull request. Everyone who
takes part is expected to follow the [code of conduct](.github/CODE_OF_CONDUCT.md). To report a security
problem, follow the [security policy](.github/SECURITY.md) and do not open a public issue.

## Licence

Codjiva is licensed under the [Apache License, Version 2.0](LICENSE). The bundled JetBrains Mono typeface is
licensed under the SIL Open Font License; see [NOTICE](NOTICE).
