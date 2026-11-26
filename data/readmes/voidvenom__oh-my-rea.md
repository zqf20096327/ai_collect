<div align="center">

# omr

**An evidence-first reverse-engineering agent for your terminal, powered by [REA](https://github.com/morluto/rea).**

[![npm](https://img.shields.io/npm/v/oh-my-rea?color=cb3837&logo=npm)](https://www.npmjs.com/package/oh-my-rea)
[![CI](https://github.com/voidvenom/oh-my-rea/actions/workflows/ci.yml/badge.svg)](https://github.com/voidvenom/oh-my-rea/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%5E22.23.4%20%7C%7C%20%5E24.22.1%20%7C%7C%20%3E%3D26.12.1-339933?logo=node.js&logoColor=white)](package.json)

[Quick start](#quick-start) · [Examples](#examples) · [Models](#models) · [Commands](#commands) · [Reference](docs/REFERENCE.md)

</div>

---

Point `omr` at an app, binary, firmware image, or website and ask a question. It investigates with REA's analysis tools and answers with citations to the Evidence it actually retained, so every claim can be traced back to something it observed.

It works like the terminal coding agents you may already use (Claude Code, Codex, opencode), but built for reverse engineering and security work.

## Quick start

```bash
npm install --global oh-my-rea
omr
```

omr needs REA for analysis. If REA is missing, the first interactive launch explains why and asks before running `npm install --global rea-agents`. `omr /status` works without REA; once it connects, `/doctor` shows which providers are available on the current host.

Then set a model. Either set an API key that omr recognizes (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, ...) or write `omr-model.json` as shown in [Models](#models).

### Platform notes

- **Linux:** Use a UTF-8 terminal. Install `wl-clipboard` for Wayland or `xclip`/`xsel` for X11 if clipboard access is unavailable. Session scripts use `unshare -rn` only if the kernel permits it.
- **macOS:** Terminal.app and iTerm2 can use the CLI and TUI. Set Option to send Escape/Meta for Alt shortcuts. Clipboard text uses `pbcopy`/`pbpaste`; image paste can use `pngpaste`. Terminal.app uses the 256-color palette unless truecolor is explicitly advertised.
- **Windows:** Use a supported native Node build. Run `omr` in cmd or `omr.cmd` in PowerShell if the npm `.ps1` shim is blocked by execution policy. `npm prefix --global` is the directory to add to `PATH` on Windows; add its `bin` subdirectory on macOS/Linux. Windows Terminal is recommended for color, Unicode and mouse reporting; conhost, legacy console mode and terminal-owned Ctrl+Shift+C may not render or forward every TUI feature. Use `--plain` or `--json` if needed. `omr_run` uses `python3`, `py -3`, or `python` for `.py`, and `pwsh` or Windows PowerShell for `.ps1` if available. Bang commands use `cmd.exe` with native Windows Node, even if launched from PowerShell or Git Bash.
- **Git Bash / WSL:** Native Windows Node still uses Windows paths and child-process rules when launched in Git Bash. Use a real Windows console (or `winpty` where available) if MinTTY does not expose a TTY to Node. In WSL, install Linux Node and REA together; use Linux paths. Clipboard interoperability needs the Windows tools on WSL's PATH or a working Linux display clipboard.
- **Optional hosts and providers:** Check [REA's installation guide](https://github.com/morluto/rea/blob/main/docs/getting-started/installation.md) and `rea doctor` for the current provider and architecture requirements. An installed CLI does not imply Frida, Ghidra, or other external providers are available. `omr_run` is **not** a sandbox when network isolation is unavailable. Windows tree termination is best effort for live roots; descendants already detached or orphaned are not guaranteed to stop. `bench:startup` uses Python's POSIX PTY, not Windows ConPTY.

Configuration defaults to `~/.config/rea` on Linux, `~/Library/Application Support/rea` on macOS, and `%APPDATA%\rea` on Windows (`XDG_CONFIG_HOME/rea` overrides these). Existing legacy files are retained. Model metadata caches honor `XDG_CACHE_HOME`, then use the platform cache or a legacy cache. Sessions honor `OMR_SESSIONS_DIR`, retain existing `~/.rea/sessions`, and otherwise use `XDG_STATE_HOME/rea/sessions` if set, `~/Library/Application Support/rea/sessions` on macOS, or `%LOCALAPPDATA%\rea\sessions` on Windows. Windows storage privacy follows inherited ACLs rather than POSIX mode bits.

## Examples

```bash
omr                                          # interactive TUI in the current directory
omr app.apk                                  # open a target in the TUI
omr app.apk "which API endpoints does this app call, and how are requests signed?"
omr --profile android app.apk                  # pre-load Android tooling and prompts
omr /status                                  # one-shot command, no model needed
omr --json app.apk "find the license check"  # machine-readable events for scripts and CI
```

## Features

- **Evidence first.** Findings cite retained Evidence IDs (`ev_…`). Open questions go to an Unknown ledger instead of being guessed.
- **REA's full toolset.** Native, Android, Electron/JavaScript, browser, firmware and network analysis through REA, with one session journal for both your commands and the model's.
- **Any model.** 33 built-in providers (OpenAI, Anthropic, Gemini, OpenRouter, DeepSeek and more) plus local servers (Ollama, LM Studio, vLLM, llama.cpp, LocalAI) any OpenAI-compatible endpoint, and local routers (9Router, OmniRoute) that omr detects on this computer when you open the model picker. A **Custom provider** entry at the top of the picker (`Alt+M`) connects any endpoint by base URL and optional key. Switch live with `/model`.
- **Guided workflows.** Slash commands such as `/triage`, `/investigate`, `/crypto`, `/frida`, `/masvs`, `/firmware` and `/ioc` run structured playbooks instead of a blank prompt.
- **Subagents.** Spawn background workers, view the task graph, steer them mid-run.
- **Safe to interrupt.** The conversation is checkpointed after every step. `omr --resume` continues an interrupted turn.
- **Scriptable.** `--json` event stream, stable exit codes, and an embeddable SDK (`oh-my-rea/sdk`).
- **Accurate context accounting.** Context windows come from the provider or [models.dev](https://models.dev), never from a guess. If a window is unknown, omr says so.

In 0.6.0 the terminal paints before backend startup, and `omr --resume` shows a transcript preview while the session loads. Turns run without a default step limit. Set `OMR_MAX_STEPS` to cap a turn and `OMR_AUTO_EXTEND_STEPS` to opt into extra step blocks. A saved `max_steps: 40` from an older version is treated as the legacy default.

## How it works

```
you ──▶ omr ──▶ model (any provider)
          │
          └────▶ REA (MCP) ──▶ analysis providers, Evidence ledger, session journal
```

omr runs the agent loop (prompting, streaming, tool routing, compaction, reports). REA owns the facts. Every tool call goes through REA, so the journal covers what you ran and what the model ran.

## Models

Zero-config works if a supported key is set in your environment. For a custom endpoint, create `omr-model.json` in the config directory printed by `omr --help`:

```json
{
  "base_url": "https://your-endpoint/v1",
  "model": "your-model-id",
  "api_key_env": "YOUR_API_KEY_ENV"
}
```

`api_key_env` names the environment variable that holds the key, so the key itself stays out of the file. Add `"context_window": 1000000` if your endpoint does not report its window. See the [reference](docs/REFERENCE.md#model-configuration) for failover chains, token budgets, reasoning effort and every environment variable.

## Commands

Type `/` in the TUI for the full palette, or run `omr --help`. A few to start with:

| Command | What it does |
| --- | --- |
| `/open <path>` | Bind a target (binary, APK, bundle, archive) |
| `/triage` | Fast reconnaissance: format, protections, entry points |
| `/investigate <goal>` | Bounded, Evidence-backed investigation |
| `/explain <symbol\|addr>` | Decompile and explain a function |
| `/find <query>` | Zero-token search of classes, strings and procedures |
| `/evidence`, `/unknowns` | Inspect the Evidence and Unknown ledgers |
| `/report` | View or export the session report |
| `/model`, `/effort` | Switch model or reasoning effort |
| `/resume`, `/fork`, `/rewind` | Manage sessions |
| `/doctor` | Check REA providers and configuration |

Profiles (`--profile recon|malware|vuln|crypto|frida|android|firmware|web`) pre-load the right tools and prompts for a kind of task.

## Keeping up to date

```bash
omr update      # update omr and REA to the latest npm release
omr setup       # re-check the environment
```

Every interactive launch checks npm for newer omr and REA releases in the background, after the UI is already on screen. When a newer version exists, an **Update Available** box with the version and the `omr update` command appears in the same session, as soon as the registry answers. A result from an earlier check shows immediately and is updated in place. The check has a 3-second timeout and fails silently offline. To avoid hammering the registry, a launch within 60 seconds of the previous check reuses that result instead of asking again. The registry follows `npm_config_registry` if you use a mirror. Set `OMR_NO_UPDATE_CHECK=1` to disable update checks and notices. CI never checks.

## Changelog

Use `omr changelog` for the installed version, `omr changelog 0.5.1` for a specific version, or `omr changelog --all` for the full history. In the TUI, `/changelog` opens a scrollable view. A new installed version shows a short summary once, either after `omr update` or on the first interactive launch with packaged notes. [Full changelog](CHANGELOG.md)

## Language

Use `omr --lang tr` for Turkish or `omr --lang en` for English in the current launch. In the TUI, `/lang` shows the active language, and `/lang tr` or `/lang en` switches and saves it. Startup uses the flag, then `OMR_LANG`, then the saved preference, then the terminal locale. JSONL events remain in English.

## Support

If you’d like to support omr, you can buy the maintainer a coffee. [Buy Me a Coffee](https://buymeacoffee.com/omrdev)

## Requirements

- Node.js `^22.23.4`, `^24.22.1` or `>=26.12.1` (REA's requirement)
- [REA](https://github.com/morluto/rea) (`rea-agents`), installed for you on first run
- Linux is the primary platform. Some REA analysis providers (Ghidra, JADX, Frida and others) need their own tools. Run `rea doctor` to see what is available.

## Development

```bash
git clone https://github.com/voidvenom/oh-my-rea.git
cd oh-my-rea
npm install
npm run build
npm test
node bin/omr.js --help
```

`npm test` runs the unit and integration fixtures with a temporary home and a fixed English locale. Language tests supply their own locale or language override. Live provider and tool checks are separate scripts under `test/live-*.mjs`.

When omr runs next to a REA checkout, it uses that checkout. Override with `OMR_REA_COMMAND`.

## Responsible use

omr is a dual-use security tool. Analyze only software, devices and services that you own or are explicitly authorized to test. You are responsible for staying within scope and within the law. Content that omr reads from a target is treated as data, never as instructions.

## Documentation

- [Reference](docs/REFERENCE.md): configuration, all commands, tools, session layout, SDK
- [REA](https://github.com/morluto/rea): the analysis engine omr is built on

## License

[MIT](LICENSE)
