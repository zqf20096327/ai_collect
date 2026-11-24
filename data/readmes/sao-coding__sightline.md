<p align="center">
  <a href="../../releases"><img alt="Release" src="https://img.shields.io/github/v/release/sao-coding/sightline?include_prereleases"></a>
  <a href="../../actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/sao-coding/sightline/ci.yml?branch=main&label=CI"></a>
  <img alt="Windows 10 and 11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4">
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue"></a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a></p>

# sightline

Eyes and a stopwatch for AI coding agents on Windows. One small exe, command `sight`.

sightline finds windows, screenshots them even when covered, waits until the UI stops changing,
and tells the agent how image pixels map to screen pixels. It also measures CPU and memory of a
whole process tree. It **only observes**: it never clicks, types or moves the mouse. The agent
acts with its own tools, then uses sightline to check the result.

[Why](#why-sightline) • [Install](#install) • [Quick start](#quick-start) • [Use with agents](#use-it-with-ai-agents) • [Reference](docs/REFERENCE.md) • [FAQ](#faq)

```
sight list --exe notepad                  # which window?
sight shot --hwnd 15603054 --settle 300   # what does it look like, once it is stable?
sight stat --pid 19668 --duration 2000    # how much CPU and RAM?
```

## Why sightline

Asked to "check the dialog looks right", an agent on Windows usually writes a throwaway
PowerShell script: `Start-Sleep 3`, `CopyFromScreen`, a hard-coded PID. sightline replaces that.

| The throwaway script | What goes wrong | sightline |
|---|---|---|
| `Start-Sleep 3` | Too short is flaky, too long is slow | `--settle 300` waits until pixels stop changing, with a timeout and an honest `settled:false` |
| `CopyFromScreen` | Whatever is on top ends up in the image | `shot --hwnd` captures the window itself, even when covered |
| Window capture APIs | Right-click menus are separate windows and get missed | The app's own popups are detected and included |
| The model resizes the image | Pixel positions no longer match the screen | Every shot returns a `formula` from image px to screen px |
| 150% DPI scaling | Hand-made coordinate math breaks | Per-Monitor DPI aware; reports `dpi_scale` and `monitor_dpi_scale` |
| `Get-Process` | One process, hard-coded PID | `list` finds the PID; `stat` covers the whole tree with avg / p95 / max |
| Free-form text | The agent parses prose and guesses what failed | One JSON line, stable error codes, and a `hint` naming the next step |

Images are written to a file and only the **path** is returned, never base64, so a screenshot
costs one file read instead of thousands of tokens.

## Commands

| Command | Answers | Notes |
|---|---|---|
| `list` | Which windows exist, and which PID / HWND do I target? | Rect, monitor, DPI, minimized state; noisy windows hidden by default |
| `shot` | What does this window look like now? | Covered windows, popups, settle wait, coordinate `formula` |
| `stat` | How much CPU and RAM over time? | Whole process tree (Electron, browsers, games); private bytes |
| `doctor` | What monitors and DPI scales does this machine have? | First stop when something looks off |

## Install

**PowerShell one-liner** (installs to `%LOCALAPPDATA%\Programs\sight` and adds it to your user `PATH`):

```powershell
irm https://raw.githubusercontent.com/sao-coding/sightline/main/install.ps1 | iex
```

Open a **new terminal** afterwards so the `PATH` change is picked up, then check with `sight doctor`.
Pin a version, change the folder, or uninstall:

```powershell
$env:SIGHT_VERSION = "0.1.0"; irm https://raw.githubusercontent.com/sao-coding/sightline/main/install.ps1 | iex
$env:SIGHT_INSTALL_DIR = 'D:\tools\sight'; irm https://raw.githubusercontent.com/sao-coding/sightline/main/install.ps1 | iex
$env:SIGHT_UNINSTALL = 1; irm https://raw.githubusercontent.com/sao-coding/sightline/main/install.ps1 | iex
```

The script verifies the download against the `sight.exe.sha256` published with each release.

**Manual.** Download `sight.exe` from [Releases](../../releases) (`sight-windows-x64.zip` also holds the
docs and the skill), put it in a folder, and add that folder to `PATH`:

```powershell
# example: C:\tools\sight (user PATH, no admin needed)
[Environment]::SetEnvironmentVariable('Path', "$([Environment]::GetEnvironmentVariable('Path','User'));C:\tools\sight", 'User')
```

Or via Settings → System → About → Advanced system settings → Environment Variables → `Path` → New.
Restart the terminal (and the agent) afterwards. Agents must be able to find `sight` on their `PATH`.

**From source** (Windows 10/11, Rust toolchain):

```powershell
cargo build --release     # target\release\sight.exe
```

## Quick start

```
sight doctor                              # monitors and DPI
sight list --exe notepad                  # find the target
sight shot --hwnd 15603054 --settle 300   # capture it once stable
```

One turn of the agent loop:

1. **Find the target.**

   ```
   > sight list --exe notepad
   {"v":1,"ok":true,"data":{"count":1,"windows":[{"hwnd":15603054,"pid":19668,"exe":"Notepad.exe","title":"Untitled - Notepad","rect":{"x":3010,"y":362,"w":1178,"h":637},"monitor":1,"dpi_scale":1.0,"monitor_dpi_scale":1.0,"minimized":false}]},"warnings":[]}
   ```

2. **Look.** Open `data.path` with the agent's image viewer.

   ```
   > sight shot --hwnd 15603054 --settle 300
   {"v":1,"ok":true,"data":{"path":"C:\\Users\\me\\AppData\\Local\\Temp\\sightline\\shot-20261123-214402-405.jpg","image":{"w":1178,"h":637},"maps_to":{"space":"screen_physical","x":3010,"y":362,"w":1178,"h":637},"scale":1.0,"formula":"screen_x = 3010 + px / 1.0; screen_y = 362 + py / 1.0","settled":true,"elapsed_ms":945,"popups":[]},"warnings":[]}
   ```

3. **Act** with the agent's own input tool, at screen coordinates computed from `formula`.
4. **Re-check** with the same `shot` and compare. For performance, run `stat` while the app works:

   ```
   > sight stat --pid 17400 --duration 2000
   {"v":1,"ok":true,"data":{"pid":17400,"exe":"powershell.exe","duration_ms":2038,"samples":4,"logical_cores":16,"cpu_core_pct":{"avg":100.42,"p95":104.98,"max":104.98},"cpu_total_pct":{"avg":6.28,"p95":6.56,"max":6.56},"mem_mb":{"avg":52.87,"p95":52.87,"max":52.87},"processes":[...]},"warnings":[]}
   ```

   One full core (`cpu_core_pct` ≈ 100) out of 16 (`cpu_total_pct` ≈ 6.3): a busy loop.

## Use it with AI agents

- **[AGENTS.md](AGENTS.md)** is a one-page brief: commands, the observe loop, the coordinate
  formula, and what to do for each error code. Codex, Cursor and others read it automatically in
  this repo; copy it, or link to it, from your own project's instructions.
- **`skills/sightline/SKILL.md`** is the same guidance as an Agent Skill, loaded only when needed.
  For Claude Code:

  ```
  xcopy /E /I skills\sightline %USERPROFILE%\.claude\skills\sightline
  ```

Make sure `sight` is on the agent's `PATH` (see [Install](#install)).

## Reference

Full flags and output fields for every command, the coordinate and DPI rules, popup handling, the
output contract and the error codes are in **[docs/REFERENCE.md](docs/REFERENCE.md)**.

## FAQ

**Which Windows versions work?** Windows 10 and 11.

**Does anything leave my machine?** No. There is no network code; images stay in a local file.

**Why don't `stat` numbers match Task Manager?** Memory is *private bytes* (commit), not
Task Manager's "private working set".

## Building from source

```powershell
cargo build --release --locked
cargo test
```

## Limitations

- `WINDOW_PROTECTED` is untested against a real capture-protected window.
- Classic Win32 `#32768` menus are untested, so their popup fallback is unverified.
- The PID-reuse check uses process start time at 1-second resolution, so a PID reused within the
  same second is not detected.

## License

[AGPL-3.0](LICENSE).
