# thread

**Run a team of coding agents from one terminal, on the subscriptions you already pay for.**

`thread` is a lightweight agent harness in Rust: one ~5 MB binary, SQLite bundled, no server, no daemon. You talk to one agent, **main**, and it spawns **background threads** that work in parallel. Each thread has its own conversation, its own git worktree and branch, and its own model. Claude can plan while Codex fixes tests and a local Ollama model writes docs. They share a memory that learns what's true about your repo.

```
main› spawn a thread to find why the search tests are flaky, and another to add rate limiting to /api/login
• spawn_thread {"name":"flaky-search-tests", ...}
◆ spawned flaky-search-tests on thread/flaky-search-tests — /switch flaky-search-tests to watch
• spawn_thread {"name":"login-rate-limit", ...}
◆ spawned login-rate-limit on thread/login-rate-limit
Started both. I'll tell you when they report back.
main› ⚠ [login-rate-limit] wants to bash `cargo test -p api` — /y login-rate-limit or /n login-rate-limit
main› /y login
main› /switch flaky
── flaky-search-tests [running] · thread/flaky-search-tests
flaky-search-tests› also check whether it only fails on CI      ← steers it mid-run
flaky-search-tests› /main
main› ✓ [flaky-search-tests] finished (success): race in index warmup — /switch flaky-search-tests
flaky-search-tests finished: the index warmup races the first query. Fix is on thread/flaky-search-tests; want me to merge it?
```

## Why thread

- **Your subscriptions, not API bills.** thread drives the official `claude`, `codex`, `grok` and `fx` CLIs headlessly, so your Claude Pro/Max, ChatGPT, SuperGrok or fx login does the work. thread never touches their tokens. API keys and fully local models work too.
- **Parallel work without collisions.** Every thread that edits code gets its own worktree on branch `thread/<name>`. Approve, steer or stop any of them without leaving main.
- **Mix models per task.** Say "have codex fix the tests" or "review it with opus" and main spawns the thread on that provider.
- **Sessions that survive.** Every step is saved to SQLite. Quit with work in flight and it resumes on the next launch.
- **Memory that learns cheaply.** Facts come from the model that already has the context, so there are no transcript re-reads and usually no extra calls.
- **Confined by default.** Each thread is locked to the directory you opened thread in, and on macOS the OS sandbox enforces it, `--yolo` included.
- **Works in any terminal.** Plain line output with no TUI framework, so it runs the same in iTerm, tmux, SSH and editor terminals, and in scripts.

## Footprint

thread sits close to zero when it's waiting on you, so it's fine to leave open all day.

| state | CPU | memory (RSS) | OS threads |
|---|---|---|---|
| idle on main, no threads | ~0.1% of one core | ~6 MB | 2 |
| idle on main, 3 background threads finished | ~0.1% of one core | ~9 MB | 6 |

Measured on an Apple M5 (macOS) over 60-second windows, release build, under a real pty, with the offline mock model. Figures are the average of two runs.

While a thread is working, the cost is the model call itself. CLI providers (`claude`, `codex`, `grok`, `fx`) are launched once per turn and exit when the turn ends, so nothing extra stays resident between turns. The exception is `fm serve`, which stays up after first use until thread exits.

## Quick start

Requires macOS or Linux and a Rust toolchain.

```bash
git clone https://github.com/Phytonking/thread && cd thread
cargo build --release && ln -sf "$PWD/target/release/thread" ~/.local/bin/thread

thread login claude        # or: codex, grok, fx, api, ollama, fm, local
thread status              # what's installed / logged in, and the default
cd ~/code/some-repo
thread                     # opens main
```

Ask main for work in plain English. `/switch <name>` watches a thread, `/main` goes back, `exit` quits.

## Documentation

| doc | read it for |
|---|---|
| [Guide](docs/guide.md) | a walkthrough of a working session, everyday workflows, scripting with `thread ask`, terminal support |
| [Commands](docs/commands.md) | every CLI command, flag, REPL input, and the tools the agent can call |
| [Providers](docs/providers.md) | claude, codex, grok, fx, api, ollama, fm, local: login, models, quirks |
| [Safety](docs/safety.md) | approvals, `--yolo`, and the zone that confines each thread |
| [Memory](docs/memory.md) | how facts and skills are learned, trusted, superseded and forgotten |
| [Configuration](docs/configuration.md) | every environment variable and config file |
| [Architecture](docs/architecture.md) | runtime model, persistence, code layout, known gaps |
| [Contributing](CONTRIBUTING.md) | build, test, conventions, and how to add a provider or scenario |

## License

[MIT](LICENSE)
