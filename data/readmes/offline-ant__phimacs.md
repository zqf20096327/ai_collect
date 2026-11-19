# Phimacs

> **[Human prelude]**
>
> **Why this exists:** For a long time I used [Herdr](https://herdr.dev), a
> terminal workspace for coding agents. When Emacs turned 50, I went back to
> Emacs and rebuilt, as Emacs packages, the Herdr features that I use. I
> [mentioned this on Hacker News](https://news.ycombinator.com/item?id=50298436#50300314),
> and people asked me to publish it. So I put the tools that I built with AI
> agents over the past year into this one repository, to make my setup easy to
> try.
>
> Phimacs is the result of solving problems that I had; I added each part when I
> needed it. AI agents wrote all of the code; none of it was written by me. They
> also wrote all of the text; I proofread only some of this README. So this isn't
> a carefully planned project that I plan to maintain for use cases other than my
> own. It's here so that you can see how I work and take whatever parts you find
> useful.

Phimacs is my opinionated setup for [Pi](https://github.com/earendil-works/pi-mono)
coding agents in Emacs, inspired by Herdr. It uses
[Pilish](https://github.com/dnouri/pilish) for the Pi chat in Emacs and adds
the parts around it. I made it mostly mouse-driven: frankly, working with AI
has made me rusty with keyboard shortcuts.

I work with my agents in Emacs, but Emacs doesn't run them. A background
service, [pimux](packages/pimux/README.md), does. I can close Emacs while an
agent works, then open that same agent on my phone in
[Tau](docs/install.md#tau-experimental); it is the same running chat, not a
copy. The [orchestration tools](packages/orchestration/README.md) start workers
in pimux too, so they show under their parent in Emacs and in Tau. In the demo,
one agent gives two failing tests to two workers that run in parallel.

[![Phimacs demo](docs/demo/phimacs.gif)](docs/demo/README.md)

## What it adds

- **Agents that keep running.** Closing Emacs or losing an SSH connection
  leaves them running; Close stops an agent. When pimux starts again, for
  example after a reboot, your chats come back idle. Workers and unfinished
  tasks do not come back.
- **Project spaces.** Each project has its own space with its own window
  layout. A sidebar lists all agents and shows which ones need you.
- **Workers.** An agent can give a task to a helper agent, a "worker":
  - `do` forks the current chat. The worker knows everything said so far, does
    the task, and only its final answer goes back to the agent.
  - `delegate` starts a new agent. It knows only the written brief and the
    project instructions.
- **Terminals.** Agents can run servers and long commands in terminals that you
  can see and use too.
- **[Tau (experimental)](docs/install.md#tau-experimental).** I don't use it
  much, but it lets me check in on the same agents from my phone's browser.

  <a href="docs/install.md#tau-experimental"><img src="docs/demo/tau-phone.png" width="240" alt="Tau on a phone: an agent in the stats project explains two failing tests"></a>
- **Dictation (optional).** Speak into the chat input or any Emacs buffer: click
  the 🎤 button or press a key. It needs a speech-to-text server.

## Agent tools

Phimacs adds these tools to Pi. The *Complete setup* column shows what
`phimacs setup` turns on; a selection that you saved with `/tools` still
applies. Each package's README explains its tools.

| Package | Tools | Complete setup | Plain Pi (`phimacs setup pi`) |
|---|---|---|---|
| [orchestration](packages/orchestration/README.md) | `do`, `microdo`, `delegate`: give a task to a worker. `panel-start`, `panel-read`, `panel-send`, `panel-close`: terminals for the agent. `wait`: wait for output or a process. | on | on |
| [extensions](packages/extensions/README.md) | `ask`: ask you a question. `py`: run a short Python script. `prompt_history`: read an earlier prompt. `self_compact`: the agent summarizes a long chat and continues. `/tools`: choose which tools are on. Safety checks for shell commands. | [add it](docs/install.md#optional-pi-packages) | on |
| [browser](packages/browser/README.md) | `browser`, `web_search`, `web_fetch`, `web_read`: use a browser, search and read web pages. | [add it](docs/install.md#optional-pi-packages) | with `--browser` |
| [sound](packages/sound/README.md) | `/dictate` or Alt+V in Pi, the 🎤 button in Emacs: dictation. `/speak`: read text aloud. | [add it](docs/install.md#optional-pi-packages), then [configure it](packages/sound/README.md#configuration) | with `--sound`, then [configure it](packages/sound/README.md#configuration) |

A worker can also run on a second model: choose the model pair with
`/delegate-alt`. `fresh_look` starts a worker that gets the task, but not your
conversation or project instructions. It is off by default; turn it on with
`/tools`, which comes with the extensions package.

## My AGENTS.md rules

[agents-md-template.md](packages/extensions/extensions/agents-md-template.md)
holds the rules that I give my coding agents in most projects. You can copy
them without Phimacs. With the extensions package, `/init-agents-md` asks the
agent to create or update a project's `AGENTS.md` from them.

## Status

Early: version 0.1.0. I use it every day, but expect rough edges. It runs on
Linux only and is tested with Pi 1.5.2. These instructions use the `main`
branch; the v0.1.0 release does not have all the features shown here.

## Get started

**With a coding agent:** point it at the [installation guide](docs/install.md).

**Without Emacs:** the same tools also work in plain `pi` in Herdr or tmux.
There, workers and terminals open as panes instead of running in pimux, so Tau
does not see them. See
[Pi in Herdr or tmux](docs/install.md#pi-in-herdr-or-tmux-without-emacs).

### Complete Emacs setup

You need Linux, Git, a C compiler, Node 24 or newer, and Emacs 31.1 or newer
built with tree-sitter and module support.

1. Install Phimacs:

   ```sh
   mkdir -p "$HOME/.local/bin"
   export PATH="$HOME/.local/bin:$PATH"  # also add this line to your shell startup file
   # Only if you do not have Pi yet:
   npm install --global --prefix "$HOME/.local" --ignore-scripts \
     @earendil-works/pi-coding-agent@1.5.2
   git clone https://github.com/offline-ant/phimacs
   cd phimacs
   npm ci --ignore-scripts
   npm run compile
   ln -s "$PWD/bin/phimacs" "$HOME/.local/bin/phimacs"
   ```

   Keep the `phimacs` folder: the launcher runs from it.
2. Log in. Run `pi`, enter `/login` and choose your provider, then choose a
   model with `/model`. Quit Pi. If an agent installs Phimacs for you, do this
   step yourself.
3. Run `phimacs setup` once. It installs the Emacs packages and compiled
   helpers.
4. Open a terminal in a project folder and run `phimacs`. Emacs opens in that
   terminal; add `--gui` for a window.

Phimacs starts a separate Emacs in the background and does not change
`~/.emacs.d`. The
[installation guide](docs/install.md) explains each step and how to connect
from other computers.

### Your own Emacs configuration

Install only the packages that you want with `use-package :vc`. You do not need
the theme, completion or keys of the complete setup. See
[existing Emacs configuration](docs/install.md#existing-emacs-configuration).

## License

Phimacs's own code is MIT. The Pilish chat package in `emacs/pilish/` is a fork
of [Pilish](https://github.com/dnouri/pilish) and stays GPL-3.0-or-later.
Third-party files keep their own licenses; see
[third-party sources](provenance/README.md). Phimacs does not include my private
model providers, accounts, credentials or personal settings.

## Documentation

Using Phimacs:

- [Installation](docs/install.md)
- [Demo](docs/demo/README.md)

Contributing:

- [Development and focused checks](docs/development.md)
- [Architecture](docs/architecture.md)
- [Runtime lifecycle](docs/lifecycle.md)
- [Runtime protocol](docs/runtime-contract.md)
- [Pilish upstream maintenance](docs/pilish-upstream.md)
- [Dependency security](docs/dependency-security.md)
