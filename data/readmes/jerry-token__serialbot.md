<div align="center">

<img src="app/src-tauri/icons/128x128.png" width="96" alt="SerialBot logo">

# SerialBot

**The verification loop for embedded hardware: a lightweight serial assistant whose built-in MCP server lets AI agents flash, read and verify real boards themselves** 🔌🤖

[![CI](https://github.com/jerry-token/serialbot/actions/workflows/ci.yml/badge.svg)](https://github.com/jerry-token/serialbot/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/jerry-token/serialbot?include_prereleases&label=release&color=orange)](https://github.com/jerry-token/serialbot/releases)
![Platforms](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux%20%28x64%2C%20arm64%29-blue)
[![License](https://img.shields.io/badge/license-GPL--3.0-green)](LICENSE)

English · [简体中文](README.zh-CN.md) · 🌐 [serialbot.aiany.cc](https://serialbot.aiany.cc)

<img src="docs/images/demo.gif" width="800" alt="An AI agent asks to open a port and send commands; the user approves and the commands appear in the log tagged AI">

<sub>☝️ An AI agent opens a dev board's port over MCP and sends commands. You approve, and every step shows up in the window, tagged AI.</sub>

</div>

> [!NOTE]
> 🧪 **Beta.** The features planned for the first release are in, and real hardware checks are under way. Please try it and [report problems](https://github.com/jerry-token/serialbot/issues).

## 💡 Why SerialBot

**SerialBot is the verification loop for embedded hardware.**

Coding agents earn trust by checking their own work. The teams getting the most out of them treat verification as the core of the job: [Lauren Tan (@poteto)](https://x.com/poteto), who builds Grok Bot, describes letting agents run the app, take traces and test it the way a user would, and keep going until it really works. Closing that loop is what makes their output trustworthy.

Firmware has had no such loop. Whether embedded code works is decided on the board, and the board speaks through its serial port. So a person sits in the middle: flash, watch the log, copy the interesting lines into the chat, explain what happened. The agent can write the code, but it cannot see what the code does.

SerialBot is the missing piece. The agent works on the device directly:

- 🔥 **Flashes the board**: it hands the port to your flashing tool, then takes it back. The log continues.
- 👀 **Reads the log itself**: it waits for the line it expects, or gives up after a timeout.
- 🐛 **Verifies its own work**: it adds debug prints, rebuilds, flashes and reads again, until the log shows the firmware does what it should.

You stay in charge. Every change to a port needs your approval, and every line the agent sent is marked in the window.

**SerialBot only moves the data; your skills bring the knowledge.** SerialBot passes raw bytes between the device and the model, with timestamps, markers and waits, and nothing more. What to run, in which order, and what a log line means depends on the chip, the board and the project: datasheets, boot sequences, error codes, house rules. That knowledge belongs in your repository, as skills (for example Claude Code skills or a `CLAUDE.md`), where you can version it and share it with your team.

## ✨ Features

**Light and everywhere**
- 🪶 A Windows installer of about 4.5 MB, or a portable exe of about 19 MB that runs without installing.
- 💻 Windows, macOS (Apple Silicon and Intel) and Linux (x64 and arm64, Raspberry Pi included).

**Connect**
- 🗂️ Many ports at once: one tab per port, each with its own log and counters; double-click a tab (or ⧉) to watch that port in a window of its own. Close stops the port but keeps the tab and log; Open continues there, and × on the tab closes it.
- 🌐 TCP client, TCP server (several clients at once; sending goes to all of them, and the log shows who sent what) and UDP besides serial ports; pick the type at the left of the connection bar.
- 🔁 Unplug and replug the adapter and the session carries on; the port list follows hot-plug.
- 🎛️ DTR / RTS switches, CTS / DSR / RI / CD lamps, **BRK** for a BREAK, and **⏱** for a timed DTR/RTS sequence such as `DTR=0 RTS=1, 100, RTS=0` (a reset pulse). Every change is marked in the log.

**Receive**
- 🌈 Text or HEX with millisecond timestamps, **ANSI colors** (Zephyr, ESP-IDF and other colored logs), and encodings such as UTF-8, GBK, GB18030, Big5 and Shift_JIS.
- ✂️ Auto frame split by gap; **Δt** shows the time since the line before, so in HEX view you see the gaps between frames.
- 🔎 `Ctrl/Cmd+F` search, "only matching lines" filter, and **keyword highlight** (`ERROR`, `WARN`, … in ⚙️).
- 📈 **Plot**: numbers in received lines (`temp=23.6 hum=41`, or `1.2, 3.4, 5.6`) become live curves, each on its own scale.
- 🖥️ **Terminal mode (TTY)**: a full terminal emulator on any session (cursor, colors, `top`, `vi`); keys go straight to the device, so you can log in to a Linux board's shell.
- 🔢 Line numbers (**#**) and ★ **bookmarks**: mark the lines that matter and jump back to them.
- ⏸️ Pause, and smooth scrolling through tens of thousands of lines.
- 💾 Save the log once, or keep writing it to a file as data arrives.

**Send**
- ✍️ Multi-line text or HEX with a choice of line ending. `Enter` sends, `Shift+Enter` adds a line, `↑` recalls history. Data goes out as raw bytes, exactly as typed: only the line ending you pick is added.
- 🧮 Checksums appended to HEX data: CRC-8, CRC-16 (Modbus, CCITT), CRC-32, XOR, SUM8, LRC.
- ⏲️ Timed send, 📋 saved command lists (click to send, or run a group in order; ⧉ opens them in their own window with its own target port), and 📄 file send in chunks.

**AI agents, under your control**
- 🤖 A built-in MCP server lets Claude Code, Claude Desktop and other agents list and open ports, send data, wait for replies and drive DTR / RTS, on the same sessions you see in the window.
- ✅ Before an agent sends data, toggles a line or opens, closes or reconfigures a port, SerialBot asks you: **allow once**, **allow for the session**, or **deny** (unanswered requests are refused after 60 s).
- 🟣 Everything an agent did is tagged **AI** in the log; **AI access** in the status bar keeps a session away from agents.
- 🔒 The server is off until you turn it on, listens on `127.0.0.1` by default and always needs a token. It can also serve the local network (`0.0.0.0`) when you choose to.

**Comfortable**
- 🌗 Light, dark or system theme; log font size; lines kept per session; keep the window on top.
- 🌏 English and Chinese, following the system or chosen in Settings.
- ❓ A Help page in the app: what SerialBot is for, first steps, every control, connecting an AI agent, and keys.

## 📸 Screenshots

| Dark | Light |
|:---:|:---:|
| <img src="docs/images/terminal-dark.png" alt="Terminal in the dark theme: an agent's commands tagged AI next to a command sent from the list, line numbers, Δt, a bookmarked line and the command list; the gps tab's blue dot marks new data"> | <img src="docs/images/terminal-light.png" alt="The same terminal in the light theme"> |

**🪟 Several ports side by side**: double-click a tab to move that port into a window of its own.

<img src="docs/images/windows.png" alt="The main window showing a GPS port, and esp32 in a window of its own with its log, toolbar and send box">

| 📈 Plot | 🖥️ Terminal mode |
|:---:|:---:|
| <img src="docs/images/plot-dark.png" alt="Temperature, humidity and pressure from the log drawn as live curves, each on its own scale, with the values under the cursor"> | <img src="docs/images/tty-dark.png" alt="Terminal mode: vim editing a Zephyr main.c on a board's shell"> |
| **📋 Command list in its own window** | **❓ Help page** |
| <img src="docs/images/command-window.png" alt="The main window next to the command window, which sends the Demo board commands to esp32"> | <img src="docs/images/help-dark.png" alt="Help page: what SerialBot is for, getting started, and what each control does"> |

<details>
<summary>✅ Approving what an AI agent wants to do</summary>

<img src="docs/images/approval.png" width="800" alt="Dialog: an AI agent wants to write version to /tmp/ttyA; Allow, Allow for this session, Deny">

</details>

<details>
<summary>🤖 AI page: MCP server settings</summary>

<img src="docs/images/ai-dark.png" width="800" alt="AI page with the MCP server enabled, the confirmation setting, Reachable from set to this computer only, and the Claude Code and Claude Desktop snippets">

</details>

<details>
<summary>⚙️ Settings</summary>

<img src="docs/images/settings-dark.png" width="800" alt="Settings page: theme, language, log font size, lines kept, keep on top">

</details>

## 📦 Download

Get the file for your system from [Releases](https://github.com/jerry-token/serialbot/releases):

| System | File | Notes |
|---|---|---|
| 🪟 Windows 10/11 | `SerialBot_*_x64-setup.exe` | Installer (~4.5 MB, compressed), no admin rights needed |
| 🪟 Windows 10/11 | `serialbot_windows_x64.exe` | Portable (~19 MB, uncompressed), just run it |
| 🍎 macOS 11+ | `SerialBot_*_universal.dmg` | Apple Silicon and Intel (~11 MB) |
| 🐧 Ubuntu / Debian | `SerialBot_*_amd64.deb` | ~6 MB; `sudo apt install ./SerialBot_*.deb` |
| 🐧 Ubuntu / Debian arm64 | `SerialBot_*_arm64.deb` | Raspberry Pi 4/5 (64-bit OS) and other ARM boards; `sudo apt install ./SerialBot_*_arm64.deb` |
| 🐧 Other Linux arm64 | `SerialBot_*_aarch64.AppImage` | `chmod +x`, then run |
| 🐧 Other Linux | `SerialBot_*_amd64.AppImage` | ~80 MB (bundles its libraries); `chmod +x`, then run |

<details>
<summary>⚠️ Warning on first launch?</summary>

- **macOS says the app "is damaged" or "can't be opened"**: the builds are not notarized yet. Run once:
  ```sh
  xattr -dr com.apple.quarantine /Applications/SerialBot.app
  ```
- **Windows SmartScreen warns about an unknown publisher**: click "More info" → "Run anyway".
- **Linux can't open a port (permission denied)**: run this, then log out and back in:
  ```sh
  sudo usermod -aG dialout $USER
  ```

</details>

## 🚀 Quick start

1. 🔌 Plug in a USB-serial adapter, pick the port at the top and set the baud rate. Data bits, parity, stop bits and flow control are under `8N1 ▾`. Then press **Open**.
2. 📥 The receive view shows timestamps by default. The chips at the top right switch Δt, HEX view, sent data, auto-scroll and pause. 🔍 searches; ⚙️ sets the encoding, frame gap, ANSI colors and highlighted keywords.
3. 📤 Type a command in the box at the bottom and press `Enter`. Tick HEX to send bytes such as `01 03 00 00`.
4. 🎛️ To reset a board, use **DTR / RTS** in the status bar, or **⏱** for a timed sequence.

> [!TIP]
> Keep flow control at "None" unless your board wires CTS. With RTS/CTS on and CTS inactive, nothing gets sent.

## 🤖 Let AI agents use your ports (MCP)

1. Open **AI** on the left and tick **Enable MCP server**. It listens on `127.0.0.1` only and requires a token. To let agents on other computers in your network use it, set **Reachable from** to *The local network too*; the AI page then shows the address and command for those computers. Use that only on networks you trust: HTTP is not encrypted, and the token is the only protection.
2. Press **Copy** and run the command in a terminal, for example:
   ```sh
   claude mcp add --transport http serialbot http://127.0.0.1:9633/mcp \
     --header "Authorization: Bearer <your token>"
   ```
3. Ask Claude Code: *"List the serial ports, open the ESP32 one and send `version`."* 🎉
4. ✅ SerialBot asks before the agent opens the port or sends anything. Pick **Allow for this session** to stop being asked for that port, or untick "Ask before AI agents send data or change a port" on the AI page.

**Claude Desktop** (and other clients that only start stdio servers): copy the second snippet on the AI page into `claude_desktop_config.json`. It runs `serialbot mcp`, a small bridge to the running app, so SerialBot must be open with the MCP server on:

```json
{ "mcpServers": { "serialbot": { "command": "/Applications/SerialBot.app/Contents/MacOS/serialbot", "args": ["mcp"] } } }
```

On Windows the command is the path of `serialbot.exe` (installed or portable); on Linux the path of the AppImage or `/usr/bin/serialbot`.

| Tool | What it does |
|---|---|
| `port.list` / `session.list` | List ports / open sessions |
| `session.open` | Open a port (optionally with an alias such as `esp32`) |
| `io.write` / `io.read` | Send data / read the timestamped log from a cursor |
| `io.wait_for` | Wait until received data matches a regex |
| `io.send_and_expect` | Send a command and wait for the expected reply |
| `io.signals` | Set DTR / RTS, read CTS / DSR / RI / CD |
| `session.close` | Close a session's port; the session and log stay so you can look back, and `session.open` on that port continues it |
| `session.release` / `session.reopen` | Hand the port to another tool (a flasher) and take it back; the log continues |
| `session.configure` | Change the baud rate without closing the port |
| `log.mark` / `log.query` | Set a named marker; summarize or search what happened after it |
| `command.list` / `command.call` | Further commands: rename, auto-reconnect, send BREAK |

## 🗺️ Roadmap

- [x] Serial, TCP and UDP; many sessions; text / HEX, ANSI colors, encodings, frame split
- [x] Send: history, timed send, command lists, files, checksums
- [x] Signals: DTR / RTS, line states, BREAK, timed sequences
- [x] Log: search, filter, Δt, keyword highlight, save and capture
- [x] Built-in MCP server (HTTP and stdio), approvals, per-session AI access
- [x] Installers for Windows, macOS and Linux (x64 / arm64), published automatically
- [x] TCP server with several clients
- [x] Command list in its own window
- [x] Terminal mode (VT100, interactive shells)
- [x] Waveform plots of received numbers
- [ ] Built-in AI assistant "Bo"
- [ ] JS scripts
- [ ] BLE

## 🛠️ Build from source

You need Rust (the version in `rust-toolchain.toml` installs itself) and Node 22+. Linux also needs some system libraries:

```sh
sudo apt install libwebkit2gtk-4.1-dev librsvg2-dev libayatana-appindicator3-dev libudev-dev
```

```sh
cd app && npm ci && npm run tauri dev     # run the desktop app
cargo test --workspace                    # Rust tests
cd app && npm test                        # frontend tests
cargo run -p serialbot-mcp                  # MCP server only, without a window
```

Every change ships with tests and must pass the format, clippy, test and coverage checks; see [CLAUDE.md](CLAUDE.md).

## 🤝 Feedback

Found a bug or have an idea? Open an [issue](https://github.com/jerry-token/serialbot/issues) with:

- 📷 a screenshot
- 💻 your OS
- 🔌 your USB-serial chip (CH340 / CP2102 / FT232 / CH9344 …)

For anything else, write to [support@aiany.cc](mailto:support@aiany.cc).

## 📄 License

The core is [GPL-3.0-only](LICENSE). Plugin SDKs and device-side libraries will be MIT-licensed.
