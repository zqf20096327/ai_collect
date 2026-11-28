# Agent UI

**A canvas where coding agents show their work, in Emacs.**

Agent UI gives a coding agent running in [agent-shell](https://github.com/xenodium/agent-shell) a canvas at the
bottom of its session's pane: progress bars, checklists, tables, charts, diffs, diagrams, and questions for you. Each
one is updated in place as the work goes on, instead of scrolling away in the conversation.

![An agent releasing a project: its plan, the build's progress and the tests fill in under the conversation, then it asks how to go on](docs/images/release.gif)

> [!NOTE]
> Agent UI is young and under active development. Expect rough edges, and please
> [report what you find](https://github.com/smyrgeorge/agent-ui/issues).

## Features

- **30 component types**, to show and to ask ([the list](#components)), each updated in place as the work goes on.
- **Questions with real answers**: pick an option, confirm, fill in a form, rank, approve a plan, accept changes, pick
  rows. The answer goes back into the session's prompt.
- **One canvas per session**, at the bottom of its pane. It closes with the session and comes back when the session is
  resumed. A second subject gets a canvas of its own beside it.
- **Driven from the agent's shell** with one command (`bin/agent-ui`, JSON in and out), or as **MCP tools**.
- **Sources**: a component follows a command, a file or a poll by itself, so a progress bar keeps moving while the
  agent waits on a long build.
- **[Project dashboards](#project-dashboards)**: kept in a repository, opened on demand, their data fetched afresh.
- **Types of your own**: the agent defines a new component type when none fits. Nothing of its code runs before you
  review and keep it.
- **In the conversation too**: a component saved as an SVG for the agent's reply, a canvas exported as a PDF.
- **Works in a terminal**: everything has a text drawing, and a graphical frame adds SVG charts, gauges and images.
- **A doctor**: `M-x agent-ui-doctor` checks what Agent UI needs and says how to fix what's missing.

## Components

To show:

- `progress`: a bar, with its rate and the time left
- `steps`: a checklist whose steps change state
- `table`: rows that fit the width, filled in by key
- `stats`: a row of figures with their change
- `gauge`: one value against its range and target
- `chart`: lines, bars, a histogram or a sparkline
- `heatmap`: a grid coloured by value or state
- `timeline`: tasks as bars on a time axis
- `countdown`: time elapsed or left, ticking
- `graph`: nodes and edges, laid out for you
- `mermaid`: a Mermaid diagram
- `diff`: changes, by file and hunk
- `code`: a snippet, with notes on marked lines
- `files`: files and their state, flat or as a tree
- `log`: output coloured by level
- `activity`: what a script or an agent is doing now
- `tags`: chips with counts
- `text`: a paragraph
- `markdown`: Markdown, drawn as agent-shell draws replies
- `math`: LaTeX formulas, typeset
- `image`: a picture, from a file or a URL
- `html`: a web page, as a card
- `panel`: several components together, in rows and columns

To ask:

- `choice`: pick one option, or several
- `confirm`: yes or no, before something risky
- `form`: several fields filled in at once
- `rank`: items put in order
- `slider`: a number in a range
- `compare`: alternatives side by side, to pick from
- `todo`: a checklist you and the agent both tick

And three ways to ask with what's already shown: `steps` with `approve` (a plan to approve), `diff` with `accept`
(changes to accept), `select` on a `table`, `files` or `tags` (rows, files or chips to pick). Each type, its properties
and an example: [Component types](docs/components.md).

## Screenshots

| Figures | Changes |
|---|---|
| ![stats, a gauge, a line chart, a heatmap, a timeline, bars and tags](docs/images/figures.png) | ![a file tree, a module graph, a diff, code with a marked line, a log and a Mermaid diagram](docs/images/content.png) |

Asking you: a choice answered, then a ranking reordered and sent:

![A choice answered and a ranking reordered](docs/images/asking.gif)

An agent's session with its canvas, its tests canvas and a question waiting:

![An agent-shell session with three Agent UI views under it](docs/images/session.png)

## Requirements

- Emacs 29.1 or later, running as a server (`M-x server-start`): the command reaches Emacs through `emacsclient`.
- [agent-shell](https://github.com/xenodium/agent-shell) and [vui](https://github.com/d12frosted/vui.el), installed
  as dependencies.
- Optional, for some components:
  - [Mermaid's CLI](https://github.com/mermaid-js/mermaid-cli) (`mmdc`) for `mermaid` diagrams.
  - Node with `mathjax-full`, or LaTeX and `dvisvgm`, for `math`.
  - `curl` for images from URLs.
  - `rsvg-convert` (librsvg) to export a canvas as a PDF.

`M-x agent-ui-doctor` checks all of these in your Emacs and says how to fix what's missing (`agent-ui doctor` does the
same from a shell): see [Checking the setup](docs/getting-started.md#checking-the-setup).

## Install

Agent UI isn't on MELPA yet. Install it from GitHub.

With `package-vc` (Emacs 29+):

```elisp
(package-vc-install "https://github.com/smyrgeorge/agent-ui")
```

With `use-package` (Emacs 30+):

```elisp
(use-package agent-ui
  :vc (:url "https://github.com/smyrgeorge/agent-ui" :rev :newest)
  :after agent-shell
  :config
  (server-start)
  (agent-ui-mode 1))
```

With [straight.el](https://github.com/radian-software/straight.el):

```elisp
(straight-use-package
 '(agent-ui :host github :repo "smyrgeorge/agent-ui"
            :files (:defaults "bin" "skills" "assets")))
```

With Doom Emacs, in `packages.el`:

```elisp
(package! agent-ui
  :recipe (:host github :repo "smyrgeorge/agent-ui"
           :files (:defaults "bin" "skills" "assets")))
```

The package needs its `bin/`, `skills/` and `assets/` folders, not only its Lisp files: keep them in your recipe's
`:files`.

## Setup

```elisp
(require 'agent-ui)
(server-start)
(agent-ui-mode 1)
```

`agent-ui-mode` ties Agent UI to agent-shell. Each session's agent finds its own canvas, is told about it in its
system prompt (for the agents that take one), and gets Agent UI's MCP tools. Nothing is set up just by loading the
package.

Start an agent-shell session and ask the agent to show you its plan. It reads `skills/agent-ui/SKILL.md` before its
first use, as its system prompt tells it.

## Try it from a shell

Any shell can draw on a canvas while Emacs runs its server. Without an agent-shell session, the canvas opens in a
window of its own:

```sh
AGENT_UI=$(emacsclient --eval 'agent-ui-command' | tr -d '"')

$AGENT_UI show '{"id":"build","type":"progress","title":"Build","max":12,"label":"configuring"}'
$AGENT_UI update build '{"value":7,"label":"linking"}'
$AGENT_UI update build '{"value":12,"status":"done","label":"done in 41s"}'

$AGENT_UI show '{"id":"plan","type":"steps","title":"Release","steps":["Run the tests","Build","Publish"]}'
$AGENT_UI append plan '{"steps":[{"name":"Run the tests","status":"done","detail":"412 passed"}]}'

$AGENT_UI types chart     # a type's properties and an example
$AGENT_UI clear
```

Every reply is JSON: `{"ok":true,"id":"build"}`, or `{"ok":false,"error":"..."}` saying exactly what's wrong.

## Project dashboards

A project dashboard lives in a project's repository: a service's traffic and CI, a release's state, whatever
you want to see again for that project. It opens on demand in a window of its own, fetches its data afresh when it
opens and every so often while it's shown, and keeps none of it. The canvas is for what the agent shows as it works; a
dashboard is for what you come back to.

![A project dashboard: a service's figures, its error budget, its latency, its CI runs and its last errors](docs/images/dashboard.png)

**Making one.** Each dashboard is a file, `.agent-ui/dashboards/NAME.el`, committed with the project. It holds what the
dashboard shows (`:ui`, components as the agent shows them, written as a plist) and the code that fills it (`:fetch`,
run every `:every` seconds):

```elisp
;;; service.el --- Agent UI dashboard: the service  -*- lexical-binding: t; -*-
(agent-ui-dashboard
 :version 1
 :ui (:type "panel" :id "service" :title "checkout-service"
      :children ((:type "table" :id "ci" :title "CI on main" :columns ("Run" "Commit" "Status"))))
 :every 30
 :fetch (lambda (dashboard)
          (agent-ui-dashboard-run dashboard '("gh" "run" "list" "-L" "5" "--json" "number,displayTitle,conclusion")
            (lambda (runs)
              (agent-ui-dashboard-update dashboard "ci"
                :rows (mapcar (lambda (run)
                                (list (format "#%s" (alist-get 'number run))
                                      (alist-get 'displayTitle run)
                                      (or (alist-get 'conclusion run) "running")))
                              runs)))
            :component "ci")))
```

`agent-ui-dashboard-run` runs a command without making Emacs wait, and hands its output (parsed, when it's JSON) to your
function; `agent-ui-dashboard-update` changes a component as `agent-ui update` does. The easiest way to make a dashboard
is to ask your agent ("make a dashboard with our CI runs and the error rate"): it writes the file, checks it with
`agent-ui check NAME` and opens it for you. `S` on a component of a canvas saves it as a dashboard too, for its `:fetch`
to be written.

**Using it.** `M-x agent-ui-open-dashboard` lists the project's dashboards and opens the one you pick. In a dashboard,
`r` reads its file again and reruns it, `E` saves it as a PDF, `q` closes it. A dashboard's code comes from a
repository, so before it first runs you're asked (`y` run it, `p` trust the project, `v` view the file first, `n` not
now); the answer is remembered for that file's content, and asked again once it changes. A hidden dashboard fetches
nothing. The agent lists the dashboards (`agent-ui dashboards`), opens one (`agent-ui open NAME`) and reads its data
(`agent-ui get --dashboard NAME`).

**Two demos** come with this repository, in [`.agent-ui/dashboards/`](.agent-ui/dashboards/):
[`cpu`](.agent-ui/dashboards/cpu.el) (how busy the machine is, its load, its last minute, the processes using it most)
and [`memory`](.agent-ui/dashboards/memory.el) (where the memory goes, its pressure, swap, the compressor's work, the
processes holding the most). Both fetch every second, on macOS and Linux, each from one command run without waiting.
Open this repository in Emacs and `M-x agent-ui-open-dashboard`, or copy one into your project's
`.agent-ui/dashboards/`.

More: [Project dashboards](docs/dashboards.md).

## How it works

![The agent calls bin/agent-ui from its shell, or the same operations as MCP tools; the command reaches Emacs
through emacsclient; Emacs draws the session's canvas; your answers and the buttons' prompts go into the session's
prompt, back to the agent](docs/images/how-it-works.svg)

Each agent-shell session starts its agent with `AGENT_UI_SESSION` in its environment, so every request finds that
session's canvas. A component is a JSON object (`type`, `id`, its type's properties), checked against its type before
it's drawn: a wrong one is refused whole, with an error listing the right properties.

## Documentation

- [Getting started](docs/getting-started.md)
- [The command line and MCP](docs/command-line.md)
- [The canvas](docs/canvas.md): its views, keys, actions, questions, sessions
- [Component types](docs/components.md)
- [Sources](docs/sources.md), [project dashboards](docs/dashboards.md), [types of your own](docs/custom-types.md)
- [Bugs in Agent UI](docs/bugs.md), [the Emacs Lisp interface](docs/lisp.md)
- [Customization](docs/customization.md)
- [The agents' guide](skills/agent-ui/SKILL.md): what agents read before using it

## Development

```sh
make deps      # clone the dependencies into .deps/
make compile   # byte-compile, warnings as errors
make lint      # package-lint and checkdoc
make test      # the unit tests, in emacs -Q
make melpazoid # the checks MELPA's reviewers run (needs Docker)
scripts/release.sh # a release: agent-ui.el's version tagged (vX.Y.Z) and pushed, checked first
```

The screenshots and GIFs in this README are made by a script, `scripts/media.sh` (macOS: it uses `screencapture`,
and `ffmpeg` for the GIFs). Each scene in `scripts/media/media.el` plays in a GUI `emacs -Q` of its own, an
agent-shell session with a stand-in agent (`scripts/media/stand-in.el`, offline) for the session's:

```sh
make media-deps   # the dependencies, and doom-themes for the look
make media        # every scene, into docs/images/
scripts/media.sh figures asking   # some of them
```

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
