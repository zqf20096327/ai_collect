<p align="center">
  <a href="../../releases"><img alt="Release" src="https://img.shields.io/github/v/release/sao-coding/sightline?include_prereleases"></a>
  <a href="../../actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/sao-coding/sightline/ci.yml?branch=main&label=CI"></a>
  <img alt="Windows 10 and 11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D4">
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue"></a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a></p>

# sightline

Eyes and a stopwatch for AI coding agents on Windows. One small exe, command `sight`.

sightline finds windows, screenshots them even when covered, waits for the UI to change and then stop
changing, and tells the agent how image pixels map to screen, window and client coordinates. It also
measures CPU and memory of a whole process tree. It **only observes**: it never clicks, types or
moves the mouse. The agent acts with its own tools, then uses sightline to check the result.

[Why](#why-sightline) • [Install](#install) • [Quick start](#quick-start) • [Use with agents](#use-it-with-ai-agents) • [Reference](docs/REFERENCE.md) • [FAQ](#faq)

```
sight list --exe notepad                  # which window?
sight shot --hwnd 15603054 --settle 300   # what does it look like, once it is stable?
sight wait --hwnd 15603054 --change --settle 300   # after my click: has the UI changed and settled?
sight stat --pid 19668 --duration 2000    # how much CPU and RAM?
```

## Why sightline

Asked to "check the dialog looks right", an agent on Windows usually writes a throwaway
PowerShell script: `Start-Sleep 3`, `CopyFromScreen`, a hard-coded PID. sightline replaces that.

| The throwaway script | What goes wrong | sightline |
|---|---|---|
| `Start-Sleep 3` | Too short is flaky, too long is slow | `--settle 300` waits until pixels stop changing, with a timeout and an honest `settled:false` |
| `Start-Sleep 0.5` after a click | The UI may not have started changing yet, so a plain settle returns the old frame | `--expect-change` waits for pixels to differ from a baseline first, then settles |
| `CopyFromScreen` | Whatever is on top ends up in the image | `shot --hwnd` captures the window itself, even when covered |
| Window capture APIs | Right-click menus are separate windows and get missed | The app's own popups are detected and included |
| The model resizes the image | Pixel positions no longer match the screen | Every shot returns a `formula` from image px to screen px |
| Hand-cut `Crop`, window moved to a fixed spot first | Breaks when the window is somewhere else | `--crop x,y,w,h` is window-relative and position-independent; `formula_window` and `formula_client` map pixels to window and client coordinates |
| 150% DPI scaling | Hand-made coordinate math breaks | Per-Monitor DPI aware; reports `dpi_scale` and `monitor_dpi_scale` |
| `Get-Process` | One process, hard-coded PID | `list` finds the PID; `stat` covers the whole tree with avg / p95 / max |
| Free-form text | The agent parses prose and guesses what failed | One JSON line, stable error codes, and a `hint` naming the next step |

Images are written to a file and only the **path** is returned, never base64, so a screenshot
costs one file read instead of thousands of tokens.

## Commands

| Command | Answers | Notes |
|---|---|---|
| `list` | Which windows exist, and which PID / HWND do I target? | Rect, monitor, DPI, minimized state; noisy windows hidden by default |
| `shot` | What does this window look like now? | Covered windows, popups, change and settle wait, window-relative `--crop`, coordinate formulas |
| `wait` | Has the UI changed and settled after my action? | Same waiting as `shot`, no image; `changed`, `change_ms`, `settled` |
| `rec` | Show me what happened: an animated GIF | Window, crop or region to GIF; merges identical frames; `--until-settled`, `--keyframes` stills |
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

3. **Act** with the agent's own input tool, at coordinates computed from the formulas below.
4. **Wait for the UI**, then look. Right after an external click the UI may not have started
   changing, so a plain `--settle` could return the old frame. `--expect-change` (or `wait
   --change`) first waits for pixels to differ from a baseline, then settles. Both phases share
   `--timeout`:

   ```
   > sight wait --hwnd 15603054 --change --settle 300
   {"v":1,"ok":true,"data":{"changed":true,"change_ms":326,"settled":true,"elapsed_ms":492},"warnings":[]}
   > sight shot --hwnd 15603054 --expect-change --settle 300     # same wait, then saves the image
   ```

   If nothing changes before the timeout, `shot` still saves the latest frame and both commands
   fail with `TIMEOUT` (exit 5) and `data.changed:false`. Tiny noise such as a blinking caret does
   not count: a change needs `--min-change-px` differing pixels (default 16). The baseline is the
   first captured frame, which arrives about 0.3 s after `sight` starts, so a change that already
   finished by then is not seen (`TIMEOUT`, `changed:false`: take a plain `shot` and look).

   **Instant reactions: `--baseline`.** Take a shot *before* acting and wait against it, so a change
   that finishes before `sight` even starts is still detected:

   ```
   > sight shot --hwnd 15603054 --out before.png
   # act with your own tool; the UI reacts instantly
   > sight wait --hwnd 15603054 --baseline before.png --settle 300
   {"v":1,"ok":true,"data":{"changed":true,"change_ms":318,"settled":true,"elapsed_ms":502},"warnings":[]}
   ```

   The same order with `wait --change` and no `--baseline` fails with a false `TIMEOUT`. Each shot
   writes a sidecar `before.sight.json`; a baseline from another window, with another `--crop`, or
   of another kind (window vs region) is `INVALID_ARGS`, never a silent wrong comparison. A window that
   was resized or expanded since the baseline counts as a change (`changed:true`, warning
   `baseline_size_changed`).

5. **Re-check** with the same `shot` and compare. For performance, run `stat` while the app works:

   ```
   > sight stat --pid 17400 --duration 2000
   {"v":1,"ok":true,"data":{"pid":17400,"exe":"powershell.exe","duration_ms":2038,"samples":4,"logical_cores":16,"cpu_core_pct":{"avg":100.42,"p95":104.98,"max":104.98},"cpu_total_pct":{"avg":6.28,"p95":6.56,"max":6.56},"mem_mb":{"avg":52.87,"p95":52.87,"max":52.87},"processes":[...]},"warnings":[]}
   ```

   One full core (`cpu_core_pct` ≈ 100) out of 16 (`cpu_total_pct` ≈ 6.3): a busy loop.

### Recording a GIF

`sight rec` records a window or region for README demos and test evidence. It blocks until it is
done, so run it in the background while you act:

```powershell
$job = Start-Job { sight rec --hwnd 123456 --duration 10000 --until-settled 500 --keyframes 3 --out C:\tmp\demo.gif }
Start-Sleep -Milliseconds 700                       # capture needs ~0.3 s to start
# ... act with your own tool (click, type) ...
$rec = Receive-Job $job -Wait -AutoRemoveJob | ConvertFrom-Json   # data.path, data.keyframes[].path
```

The result has `frames`, `fps`, `duration_ms`, `size_bytes` and the same coordinate formulas as
`shot`. Identical frames are merged (a static window is one long frame), and `--keyframes 3` also
saves PNG stills of the biggest changes so an agent can check the recording without decoding the
GIF. Defaults: `--fps 10` (max 30), `--max-edge 800`.

`rec` picks one capture source when it starts and never switches: `--source auto` (default) uses
screen capture of the window's rect, which includes menus, tooltips and popups, unless another window
covers the target, and then window capture (`source`, `source_reason` and the warning
`rec_window_source_no_popups` say which). `--pad 40` also records 40 px around the window so a
dropdown that sticks out is included. The capture follows a window that moves; windows covering it
mid-recording are listed in `occlusion_events`.

### Coordinates: pick the origin your input tool uses

For a window shot, `shot` returns one formula per origin. Use the one that matches the origin of
your own input tool, with `px, py` in the saved image:

```
> sight shot --hwnd 11736012 --crop 100,120,300,200 --max-edge 0
{"v":1,"ok":true,"data":{"image":{"w":300,"h":200},"maps_to":{"space":"screen_physical","x":307,"y":270,"w":300,"h":200},"scale":1.0,"formula":"screen_x = 307 + px / 1.0; screen_y = 270 + py / 1.0","window":{"frame":{"x":207,"y":150,"w":642,"h":452},"client":{"x":208,"y":181,"w":640,"h":420},"client_offset":{"x":1,"y":31}},"formula_window":"win_x = 100 + px / 1.0; win_y = 120 + py / 1.0","formula_client":"client_x = 99 + px / 1.0; client_y = 89 + py / 1.0","settled":true,"changed":false,"change_ms":null,"elapsed_ms":351,"popups":[]},"warnings":[]}
```

| Field | Origin | Use it for |
|---|---|---|
| `formula` | the screen (virtual desktop), physical px | tools that click at absolute screen coordinates |
| `formula_window` | top-left of the window's DWM frame | tools relative to the window; same origin as `--crop` |
| `formula_client` | top-left of the client area, below the title bar | tools relative to the client area |

`window.frame` and `window.client` are in screen px; `client_offset` is the client top-left minus
the frame top-left. Image point (50, 40) above is screen (357, 310), window (150, 160), client
(149, 129).

`--crop x,y,w,h` is relative to the window frame, so it selects the same part of the window
wherever the window is. It is applied before `--scale` and `--max-edge`; `--max-edge 0` disables
downscaling, so `--crop ... --max-edge 0` is exactly w×h pixels. It works with `--hwnd` and `--pid`
(not `--region`), and `wait` accepts it too.

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

- `--expect-change` / `wait --change` baseline on the first captured frame (about 0.3 s after
  start), so a change that finished earlier is not detected; use `--baseline` for that.
- The window formulas and `--crop` were only verified on 100% DPI monitors; they are plain physical-px
  arithmetic, but not tested at 125% or 150%.
- `WINDOW_PROTECTED` is untested against a real capture-protected window.
- Classic Win32 `#32768` menus are untested, so their popup fallback is unverified.
- The PID-reuse check uses process start time at 1-second resolution, so a PID reused within the
  same second is not detected.

## License

[AGPL-3.0](LICENSE).
