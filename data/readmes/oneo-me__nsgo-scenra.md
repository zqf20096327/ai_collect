<p align="center">
  <img src="cmd/scenra/assets/Icon.png" alt="Scenra" width="128">
</p>

<h1 align="center">Scenra</h1>

<p align="center">
  <strong>English</strong> |
  <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/oneo-me"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-oneo--me-181717?logo=github&logoColor=white"></a>
  <a href="https://oneo.me"><img alt="Blog" src="https://img.shields.io/badge/Blog-oneo.me-0969da"></a>
  <a href="https://x.com/oneo666"><img alt="X" src="https://img.shields.io/badge/X-%40oneo666-000000?logo=x&logoColor=white"></a>
  <a href="https://github.com/sponsors/oneo-me"><img alt="GitHub Sponsors" src="https://img.shields.io/badge/GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white"></a>
</p>

<p align="center">
  A desktop app and flow designer where you design an app's screens and flow charts by talking with an AI assistant that draws them as you agree.
</p>

<p align="center">
  <img src="cmd/scenra/assets/Preview.png" alt="Scenra">
</p>

## The name

Scenra is a coined word: *scene*, the screens an app is made of, joined by *-ra*, the flow that leads from one to the next. A Scenra project holds both: a folder of designs of the screens and charts of the paths between them.

## Features

- Scenra works in a folder: the left lists its Scenra files, each holding designs or flow charts, the windows and screens kept at the folder's top and grouped by names such as `Orders/Detail` under the components, a Flows group holding the flows of `flows/` and a Views group holding the pages of `views/` that fill those windows, the file you choose shows beside it, and the conversation runs the window's height on the right; ⌘B hides both sides to give the canvas the whole window. ⌘1 shows the canvas at its actual size, ⌘2 fits it to the window, and ⌘+ and ⌘- zoom in and out. In a Git repository, each file shows the lines it added and removed since the last commit.
- A screen shows what happens on it in its own design, through taps, outlets and notes; flows in `flows/` are workflows of their own, such as checkout, named for what they do rather than for a screen.
- Each folder opens in a tab of its own, with its own conversations, beside the Home tab, which shows the folders opened lately, each by one of its designs, and the settings. Choosing another file saves the one shown, as does ⌘S, closing a tab (⌘W) saves its file, and the tabs and their files reopen at the next start.
- Phone, tablet and desktop designs are drawn from boxes, texts, icons, images and SVG shaped by Tailwind CSS classes, so a draft can look like anything; zoom, pan and select its elements as in the flow charts.
- The assistant is a coding agent you have installed, such as Claude Code, Codex, pi or CodeBuddy Code: it asks what it needs, then writes and makes the folder's files as the Scenra skill teaches, and each redraws as it writes.
- Designs play as the app would: pressing an element opens another screen, closes the one shown or switches tabs, and a tab bar marks the screen shown. A screen can fill a window's content area, so playing the window swaps only its content and its sidebar stays.
- Resting the pointer on an element shows its comment and note: a comment asks the assistant for a change, and a note records what the design cannot show.
- The assistant works on what you select, resolves your comments, keeps the notes true, and works in the open folder, so it can chart how the code there works.
- Sending a message saves your changes; while the assistant works the files stay as it leaves them, and each of its turns undoes as one step.
- Pieces screens share, such as a tab bar, are components in the folder's `components/`, which designs draw with `use`, so changing one changes every screen; as with Figma's instances, a use can pick the component's variants, change the texts, icons, styles and taps of the elements its component names, and fill the slots it leaves with elements of its own, components inside included. **Components** atop the list shows them all together, grouped by their names as files are, small ones scaled up to stay legible.
- Pictures a design shows live in the folder's `assets/`, where the assistant copies the ones you give it, and images name them with `src="assets/…"`.
- Designs are plain-text `.scenra` files you can read, diff and edit by hand.
- Runs on macOS, Windows and Linux, in English and Simplified Chinese.

## Run

Scenra needs [Go](https://go.dev/dl/). From the repository root:

```sh
go tool nsgo dev cmd/scenra     # run
go tool nsgo build cmd/scenra   # build macOS, Windows and Linux into cmd/scenra/dist/
```

On macOS, `.scenra` files open with the app from the Finder; on Windows and Linux, a Scenra file or folder given on the command line opens at start. A file opens with the folder holding it.

## Getting started

1. Install and sign in to a coding agent such as [Claude Code](https://claude.com/claude-code) or [Codex](https://github.com/openai/codex); **Settings** on the Home tab (⌘,) shows the agents Scenra found and turns them or their models on or off, and under **Conversation titles** takes a model behind an OpenAI-compatible API, which names each new conversation from its first message.
2. Open a folder (⌘O), such as a project's, which the assistant works in, or `examples/coffee-shop` to start from an example; it opens in a new tab, and again from **Recent** on the Home tab.
3. Describe an app or a process in the assistant, such as "Design the sign-in screen of a coffee shop app" or "Chart how we handle an order".
4. Answer its questions and watch it make and draw the designs and flows; pick one in the list on the left.
5. Start another conversation with ⌘N; new conversations keep the agent, model and settings chosen last.

The [`flowfile` package comment](flowfile/) describes the file format.

## Usage statistics

Release builds send anonymous usage statistics to Umami: how often and how long the app is used, under a random install ID. No chart, message or file path is sent. Turn them off under **Settings** → **Statistics**. Builds of `nsgo dev` and tests send nothing.

## Use in your app

`scenraview` gives other NSGo apps Scenra's editor for `.scenra` files: an `Editor` of a folder and the file shown, and views of it, the `Window` as Scenra shows it, or a `Header`, `Sidebar`, `Workspace` and `Assistant` to lay out themselves. The assistant runs the agents of an [Agio](https://github.com/oneo-me/nsgo-agio) backend; give them the skill in `cmd/scenra/resources/skills/scenra`, which teaches the format, `scenra-app` beside it, which teaches the `Server`, and the `Server` that tells them what the user sees, which tells several editors apart by the ID each conversation's instructions give. `Cover` draws a project small, as Scenra's recent folders show.

```sh
go get github.com/oneo-me/nsgo-scenra
```

```go
nsgo.Run(func(cx *core.Scope) core.Node {
	e := scenraview.New(cx, scenraview.Options{})
	e.OpenPath("designs") // a folder, or a file, which opens with its folder
	return core.View{Style: core.Style{Direction: core.Row, FlexGrow: 1}, Children: []core.Node{
		scenraview.Sidebar{Editor: e}, scenraview.Workspace{Editor: e},
	}}
})
```

`flowfile` reads and writes the format without NSGo.

## Development

From the repository root:

```sh
go tool nsgo check          # vet, catalogs and generated files
go tool nsgo test           # tests, headless against a scripted agent
```

Read [ARCHITECTURE.md](ARCHITECTURE.md) for the design and [AGENTS.md](AGENTS.md) for the rules contributors follow.

See [CHANGELOG.md](CHANGELOG.md) for changes.

## License

Scenra is released under the [MIT License](LICENSE). Contributions are accepted under the same license.
