# Codjiva

Codjiva is a desktop app that looks like a code editor but shows a **picture of the code** in place of its text.
You open a folder, pick a file, and an AI agent you already use reads the code and draws how it works.

[![The Codjiva window. The source of a Go file is on screen. The Visuals menu opens and Film is chosen. The film then plays: an order moves through the machines of a Go order handler, and a caption explains each step.](docs/images/film.gif)](https://aayushch.github.io/codjiva/#demo)

*Codjiva playing a film it made from [one Go file](fixtures/go-orders/internal/orders/handler.go). This
recording is silent. [The project's web page](https://aayushch.github.io/codjiva/#demo) plays the same film
with sound.*

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
- **Ask** puts a question about what is on screen to the agent that drew it. The answer names the lines of
  code it relies on, and it can put numbered notes on the parts of the picture.
- **Select code** in a file to discuss only those lines, or to make any of the six views of only that function
  or type.

Everything Codjiva makes is plain HTML, saved in a `.codjiva/` folder inside your project. An exported artifact
is one file that opens in any browser, offline.

Codjiva runs on macOS, Windows and Linux. It is built with Tauri and Svelte.

## What you need

One of these, to do the reading and drawing:

| | How Codjiva uses it |
|---|---|
| **Claude Code** | The `claude` program, signed in. This is the best tested path. |
| **Cursor Agent** | The `cursor-agent` program, signed in. Tested with a real run. |
| **Codex CLI** | The `codex` program, signed in. Tested with a real run. |
| **Gemini CLI, Antigravity CLI, Pi** | Supported by definition files that have not yet been confirmed against the real programs. Settings marks them so. |
| **An API key** | For Anthropic, OpenAI, Google Gemini, or any server that speaks the OpenAI chat format (OpenRouter, Ollama, LM Studio). Codjiva then talks to the provider itself and no agent program is needed. |

Open **Settings** (the sliders icon in the title bar, or Cmd/Ctrl+,) to see which agents were found and to add a key.

## Using it

1. **Open a folder.** The explorer on the left lists it. Folders named in `.gitignore` are left out.
2. **Select a file.** Its card lists the six views that can be made of it. Click **Blueprint**. You can say
   what the picture should show, or leave that empty. The job panel at the bottom shows what the agent is
   doing. A blueprint takes about three minutes.
3. **Explore the blueprint.** Click a part to see its role, the lines of its code, what it reads and writes,
   where the work goes from it, and the edge cases the agent found in it. The **Source** button, the `</>`
   icon at the right end of the bar above the file, shows the file itself, read-only.
4. **Film** on the card asks which companion files the agent should read, what the film should show, and how
   long it should be. Codjiva suggests companions from the file's imports, its tests and the files that use
   it. Use **Ignore always…** next to a suggestion to keep that file, or a whole folder it is in, out of the
   suggestions for good. The story outline appears while the film is being made, and you can change it. The
   film is shown as soon as it is finished, and plays at 0.75×, 1×, 1.25×, 2× or 4×.
5. **Step through.** Click **Step-through** on the card of a file. It suits a parser, a state machine,
   a validator or any other code whose behaviour depends on its input. The agent draws the states and writes
   a step function that restates the code. You then run it on the examples it chose or on your own input,
   one step at a time. The same command is in the menu that a right-click on a file opens.
6. **Schema, Lanes and Structure** are the other three views of a file. Each has a small card on the card of
   the file, and a click on it starts making it. A folder has a **Map** tab beside its **Blueprint** tab. The
   same commands are in the menu that a right-click in the explorer opens. On a map, click a box twice to see
   what is inside it.

   **Switching between them.** The **Visuals** button at the right end of the bar above the file opens a menu
   of all six: Blueprint, Film, Step-through, Schema, Lanes and Structure. Point at one to read what it is
   for, and choose one to show it. While one of them is on screen, the button has its name.

   **Not sure which one to make?** Click **Which view fits this file?** under the small cards, or choose the
   same command in the menu of the **Visuals** button.
   Your agent reads the file and ranks the six, with one sentence of reason for each. The first is marked as
   suggested on the card and in the menu, and the **Visuals** button is underlined. Point at a small card to
   read the agent's reason for that view. The answer takes a few seconds and is kept until the file changes. It only suggests: you can
   make any of the six.
7. **Feedback.** Under the inspector, write what should change. Codjiva attaches the moment of the film you are
   at and, with **Point at…**, the element you mean. A new version is made with only that change.
8. **Ask.** The inspector has an **Ask** tab beside **About**. Write a question about the picture or the code
   behind it. The agent that drew the picture answers, usually within seconds. See
   [Asking about a visual](#asking-about-a-visual).
9. **Compose.** Tick two or more artifacts in the library and click **Compose**. Codjiva proposes joins between
   their ports, and you confirm them.

**Rationale.** A blueprint or a film says what the code does. Where the code also shows why it is built that
way, the agent records that as a rationale, with the line that gives the reason. Each one is marked "Stated
in the code" when a comment or a name gives the reason, and "Inferred from the code" when the agent concluded
it from how the code works. A rationale is never drawn until you ask for it:

- In a blueprint, select a part to read its rationale in the inspector. The **Rationale** switch under Layers
  puts a **?** on every part that has one, and a click on the **?** opens it.
- In a film, a bubble that has one carries a small **rationale** chip. Clicking it pauses the film and opens
  the reason inside the bubble. The inspector lists all rationales of the film.

**How long a job takes.** Before a job starts, its dialog says how long it usually takes to make, as a range
such as "8–13 min", and the job panel repeats that next to the running clock. The first estimates come from
how long the code is, how much it branches and, for a film, the length you chose. Codjiva then notes how
long each of your jobs really took and corrects the estimate with them, separately for each agent and
model. Those notes are kept in `timings.json` in the app's settings folder. They hold numbers and the names
of the agent and the model, and no file names or code.

### Asking about a visual

The **Ask** tab of the inspector holds the discussions about the blueprint, film or view on screen.

- **Who answers.** The question goes to the agent that drew the picture and continues the conversation in
  which it was drawn, so the agent has already read the code. When that conversation cannot be continued, a
  new one is started and given the text of the discussion. This happens with an agent that cannot resume a
  conversation, with an API key, and with a picture that was made on another computer.
- **The answer** is text. A place in the code, written as `path:line`, is a link to that line when the file
  and the line exist. A place that does not exist stays plain text.
- **Notes.** An answer can put notes on parts of the picture. Each note is a numbered mark on the corner of
  its part, and a click on the mark shows its text. The picture is not made again for this. The switch
  **Notes on the blueprint** above the discussion hides the marks and keeps the notes. In a film, a note is a
  card that is shown for a few seconds at one moment of the film. A click on the note in the Ask tab goes to
  that moment and pauses.
- **Change the blueprint from this…** under the last answer starts a job that makes a new version. The agent
  is given the discussion with your instruction.
- **Several discussions.** **New** starts another discussion about the same picture, and **Delete** removes
  one with its notes.
- **One question at a time.** A second question cannot be sent until the first is answered. A question
  about a picture cannot be sent while a job is making a new version of it. **Stop** ends a question that is
  being answered.
- **Who asked.** The app has no accounts. Each question carries the `user.name` of your git configuration as
  a label, or the name of your account on the computer when git has none.

A question changes no file of your project. The agent is started with an empty folder as the only place it
may write to, and its answer is its reply.

**A picture made by an earlier version of Codjiva.** Notes are drawn by the code a picture carries inside
it, and a picture keeps the code it was built with. When a note is to be shown on a picture that was built
before notes existed, the Ask tab offers **Update it**. This builds a new version from the same source
files, without an agent. The earlier version is kept, and the new one is discarded when it does not pass
the checks at least as well.

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

Beside the Source view the panel on the right has a width of its own, and it has two sections. See
[A part of a file](#a-part-of-a-file).

### Following names in the Source view

The **Source** view shows a file read-only, and the names in its code can be followed.

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

### A part of a file

A discussion or a picture can be about a part of a file: one function, one type, or any lines.

- **Select lines** in the Source view. A bar appears at the selection with **Discuss** and **Visualise**.
  When the lines lie inside a function or a type, the bar offers a choice between those lines and that
  whole definition. A right-click on the selection offers the same commands.
- **Discuss** opens a discussion about that code in the panel on the right. It works like the Ask tab.
- **Visualise** makes any of the six views of only that code. The agent still reads the whole file, and
  draws the part. The picture is shown in the panel on the right, above the discussion, and an answer can
  put notes on it.
- **Marks.** A line that starts code with a discussion or a picture has a mark in the margin. A click on
  the mark opens that code in the panel, and its lines are tinted. With nothing open, the panel lists what
  the file has.
- **Two sections.** The panel shows the definitions and references of a clicked name in one section and the
  open discussion or picture in the other. Drag the line between them to give one more room. A button swaps
  them. Drag the panel's edge to make it as wide as you need, up to a narrow strip that is left for the
  code.
- **Maximise** shows the picture in place of the code, with the inspector and its Ask tab beside it.
  **Back to the code** in the toolbar returns.

Codjiva remembers the code by what it is, and not only by its line numbers.

- A part that is a whole definition is found again by its name after the file changes, also when it has
  moved.
- A part that is a range of lines is found again by its text, also when it has moved. When the text of the
  lines was edited, the panel says that the code is no longer in the file as it was, and shows where it
  used to be.
- In a language that Codjiva does not parse, a part is always a range of lines.

A picture of a part is marked stale only when the code of that part changes. A change elsewhere in the file
leaves it as it is. The library lists such a picture as `file › name`. It cannot be ticked for **Compose**.

### Versions and staleness

Every job adds a version; nothing is overwritten. The version list is in the toolbar, followed by icons that
make the artifact again, export it as one HTML file, open it in the browser and show its files. Each icon says
what it does when the pointer is over it.

**Back** and **Forward**, at the left end of the toolbar, move through the files, tabs and pipelines you have
looked at (⌘[ and ⌘] on macOS, Alt+← and Alt+→ elsewhere). A film that you return to continues
from the moment you left it, for example after you followed a link to a line of code or looked at the
source.

In the explorer, a file that has a blueprint or a film has a dot, and every folder above it has a smaller dot, so a
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
  and a blueprint or film made from a changed file is marked stale. A job that changes an already saved version
  is stopped and its result is discarded.
- Discussions are kept in `.codjiva/threads/`, one file for each, with their questions, answers and notes.
  Your teammates see them exactly when `.codjiva/` is tracked by git. Each question in such a file carries
  the name it was asked under.
- The answer to **Which view fits this file?** is kept in `.codjiva/suggestions/`. The agent is given the
  file's text for that question and draws nothing. With Claude Code it is asked with the small model, `haiku`,
  whatever model Settings names for jobs.
- Several jobs can run at the same time. Only a second job for the same blueprint, film or pipeline has to wait
  until the first has ended. Questions are asked one at a time.
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
| Let the agent load my own setup | off | Shown for an agent that can be started without your own setup for it. With the switch off, Claude Code is started with `--safe-mode`, which keeps out your own `CLAUDE.md` files, skills, plugins, hooks and custom agents. Codex is started without the project's `AGENTS.md` files, your hooks and your plugins, Gemini CLI without your extensions, and Pi without `AGENTS.md` and `CLAUDE.md` files. Settings names the exact arguments. Turn the switch on to start the agent without them. |
| Thinking effort | Automatic | Low for a blueprint, medium for a film or a pipeline. |
| Fix rounds | 3 | How often a result that fails its checks is sent back to the agent. A round that only repairs a result that could not be built or drawn is not counted, once per job. |
| Spending limit per job | none | For agents that can enforce one. |
| Never suggest these files and folders | `vendor/`, `third_party/`, `node_modules/` | Patterns for third-party and generated code that should not be suggested as companion files. One per line, written like a line of a `.gitignore` file: `vendor/` is every folder of that name, `/internal/generated/` is that one folder, `*.pb.go` is every file with that ending. |
| Look for updates automatically | on | Asks GitHub for the newest release shortly after the app starts and every two hours. With this off, the app looks only when you click **Check for updates**. |
| Theme | Match the system | Light or dark, for the window and for the blueprints and films shown in it. An artifact made by an earlier version stays dark until it is made again, and an exported film is dark. |

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
cd ui && npm run e2e -- --browser webkit # the same in WebKit; `--scheme light` runs it in the light theme
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
