<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/lockup-dark.svg">
    <img src="assets/logo/lockup.svg" alt="Solipsist" height="56">
  </picture>
</h1>

<p align="center">
  Think, work, collaborate with your local AI agents in your markdown docs. They suggest; you decide.
</p>

<p align="center">
  <a href="https://github.com/pulkitsharma07/solipsist/actions/workflows/ci.yml"><img src="https://github.com/pulkitsharma07/solipsist/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/licence-FSL--1.1--MIT-blue" alt="Licence: FSL-1.1-MIT"></a>
</p>

<p align="center">
  <img src="site/public/demo.gif" alt="Solipsist in 15 seconds: the writer presses ⌘. at the end of a sentence, an agent works on it with their tools, and its suggestion waits in green until they accept it" width="880">
</p>

<p align="center">
  <a href="site/public/launch.mp4">▶ Watch the 80-second film</a>
</p>

<p align="center">
  <a href="https://solipsist.sh">🌐 Website</a> ·
  <a href="https://solipsist.sh/docs/">📖 Docs</a> ·
  <a href="CONFIGURATION.md">⚙️ Configuration</a> ·
  <a href="https://github.com/pulkitsharma07/solipsist/discussions">💬 Discussions</a>
</p>

## Install

On macOS or Linux:

```bash
curl -fsSL https://solipsist.sh/install | sh
cd ~/my-notes && solipsist
```

On Windows (PowerShell): `irm https://solipsist.sh/install.ps1 | iex`.

The installer downloads the release for your system, checks it against the release's checksums and puts `solipsist` where
you choose (`~/.local/bin` by default, no sudo). No Bun. Run it again to update. `solipsist --version` says which build you have.

Open <http://localhost:3000>. The first launch lists the markdown files in that folder. Pick the ones to work on, or
start a new page if there are none.
Prefer to run from source? You need [Bun](https://bun.sh) and a clone of this repository. More in
[Install and run](https://solipsist.sh/docs/start/install/).

## What it does

- **Ask at the cursor or about a selection.** Press `Mod-.` and say what you want. An agent works in the background
  and the result comes back as a suggestion you accept, reject, ask again or chat about.
- **Rewrite anything.** Select text and ask for it shorter, friendlier or as a table; old and new sit side by side
  until you choose.
- **Research in the page.** Ask a question and the agent searches, reads and writes up what it found under it. Each
  task gets its own agent, so several run while you keep writing.
- **Page review.** An agent reads the whole page and leaves questions in the margin. It changes nothing in your text.
- **Save a task as a button.** Press it to run the task again and update the text in place, or put it on a schedule.
- **A real editor.** Headings, lists, tables, images and links with the usual shortcuts, Vim keys if you want them,
  and daily and monthly spending limits.

## How your files are kept safe

Solipsist copies the files you pick into `.solipsist/` and you work on the copies. Your files change only when you
press **Sync to file**, and then only in what you changed. If a file changed since you loaded it, Solipsist asks
first and offers **Reload from file**. Comments and agent tasks stay in `.solipsist/`, on your machine.

`git clean -fdx` deletes `.solipsist/`, along with anything not synced yet.

To find files in subfolders, add patterns to a `solipsist.yaml` in that folder:

```yaml
md_search_paths:
  - "*.md"
  - docs/**/*.md
```

Dot-folders, `node_modules` and anything git ignores are never offered. Every setting is in
[`CONFIGURATION.md`](CONFIGURATION.md).

## Connect a model

The agents are [Pi](https://github.com/earendil-works/pi), an open-source coding agent, built in: you don't need to
install it.

- **OpenRouter:** set `SOLIPSIST_OPENROUTER_KEY` in your environment (your shell's profile, say).
- **Pi's own logins:** if you use Pi already, its saved logins, skills and connected tools work here too (`pi`, then
  `/login`, to add one). That includes subscriptions you already pay for and models running on your own computer.

Like Pi in a terminal, an agent can run commands on your computer. Solipsist doesn't sandbox them. More in
[Connect a model](https://solipsist.sh/docs/start/connect-a-model/).

## Privacy

Solipsist sends nothing about you or your use of it anywhere: no account, no analytics, no telemetry, no update
check. Your pages stay on disk. When you ask an agent for something, the text it needs goes to the model you connect,
under that provider's terms, and to any tools you connected to Pi (a search, a browser, your calendar) if the agent
uses them. More in [Privacy](https://solipsist.sh/docs/reference/privacy/).

## Development

```bash
bun install
bun run dev         # the app, with hot reload, on this folder
bun test            # the whole suite
bun run typecheck
bun run features    # regenerates FEATURES.html
```

The docs site is in `site/` (`cd site && bun run dev`). Solipsist is closed to code contributions for now; issues
and [Discussions](https://github.com/pulkitsharma07/solipsist/discussions) are open. See
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licence

[FSL-1.1-MIT](LICENSE): use, change and self-host Solipsist for anything except a competing product; each release
becomes MIT two years after it ships. Third-party licences are in [`NOTICE`](NOTICE). Security reports go as in
[`SECURITY.md`](SECURITY.md); the [Code of Conduct](CODE_OF_CONDUCT.md) applies to issues and Discussions.
