# Ace

A native code editor on GPUI, made for work with coding agents. It runs agent sessions next to your code,
shows what each turn changed for review, and opens pull requests, on a local folder or over SSH.

Agents plug in through one model of Ace's own (`crates/agents`): Claude Code, Cursor and Codex (over the Agent
Client Protocol), and Ace's own agent.

## Build and run

Rust 2024 (stable). macOS and Linux.

```sh
cargo run -p ace-app       # the editor
cargo run -p ace-gallery   # every component in each state
go run ./tools/dev check       # every check a change needs: tests, clippy, the gallery, the vendored crates
```

An agent runs as its own program on the project's host, so install and sign in to the agent you want there
(for example `claude` for Claude Code, `agent` for Cursor).

## Layout

The UI is built from ace-ui, the design system, which lives in `crates/ui`.

| Path | What it holds |
| --- | --- |
| `crates/app` | The window: projects, sessions, review, PR view, tasks, settings. |
| `crates/agents` | Agent sessions: the model, and a backend for each agent. See [docs/agents.md](docs/agents.md). |
| `crates/editor`, `crates/lsp` | The code editor and language servers. |
| `crates/project`, `crates/remote` | A project on this machine or on an SSH host. |
| `crates/review`, `crates/pr-view`, `crates/forge` | Review of agent turns, pull requests, and the code host. |
| `crates/tracker`, `crates/settings` | Tasks, and the settings file. |
| `crates/gallery` | The gallery: every component in each state, with sample data. |
| `vendor` | Patched copies of `gpui-base` and `gpui-component`. See each one's `PATCHES.md`. |
| `docs` | How each part works. |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[AGPL-3.0](LICENSE). If you run a modified Ace for other people, including as a hosted service, you must
offer them the source. ace-ui is GPL-3.0 or commercial, and GPL-3.0 code may join an AGPL-3.0 work. The copies
in `vendor` keep their own Apache-2.0 license. The crates that other programs link to, such as `ace-capabilities`, are MIT or Apache-2.0 (see CONTRIBUTING.md). Agent and lab logos in `crates/agents/assets` belong to their owners
and show which agent or model is in use.
