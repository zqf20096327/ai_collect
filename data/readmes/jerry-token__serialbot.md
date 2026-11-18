<div align="center">

<img src="app/src-tauri/icons/128x128.png" width="96" alt="SerialBot logo">

# SerialBot

**A lightweight, cross-platform serial port assistant with a built-in MCP server, so AI agents can drive your serial ports too** 🔌🤖

[![CI](https://github.com/jerry-token/serialbot/actions/workflows/ci.yml/badge.svg)](https://github.com/jerry-token/serialbot/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/jerry-token/serialbot?include_prereleases&label=release&color=orange)](https://github.com/jerry-token/serialbot/releases)
![Platforms](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue)
[![License](https://img.shields.io/badge/license-GPL--3.0-green)](LICENSE)

English · [简体中文](README.zh-CN.md)

<img src="docs/images/demo.gif" width="800" alt="An AI agent opens a port over MCP, sends commands and waits for replies while the window shows every step">

<sub>☝️ Claude Code opens a dev board's port over MCP, sends commands and waits for the replies. The window shows every step.</sub>

</div>

> [!NOTE]
> 🚧 **Alpha.** The basics work. Please try it and [report problems](https://github.com/jerry-token/serialbot/issues).

## ✨ Features

- 🪶 **Lightweight**: a 3.5 MB Windows installer, or a 16 MB portable exe that runs without installing.
- 💻 **Cross-platform**: Windows, macOS (Apple Silicon and Intel) and Linux.
- 🗂️ **Many ports at once**: one tab per port, each with its own log and counters.
- 🌈 **Receive view**:
  - text or HEX, with millisecond timestamps
  - **ANSI colors** (Zephyr, ESP-IDF and other colored logs)
  - encodings: UTF-8, GBK, GB18030, Big5, Shift_JIS and more
  - auto frame split, pause, `Ctrl/Cmd+F` search
  - stays smooth with tens of thousands of lines
- ✍️ **Send**: multi-line text or HEX, with a choice of line ending. `Enter` sends, `Shift+Enter` adds a line, `↑` recalls history; timed send.
  Data goes out as raw bytes, exactly as typed: no framing or protocol is added, only the line ending you pick (none for HEX).
- 📋 **Command lists**: saved commands in groups; click one to send it, or run a group in order with a delay after each.
- 📄 **Send a file** in chunks, with an optional pause between chunks for devices without flow control.
- 💾 **Save the log** once or keep writing it to a file as data arrives.
- 🌐 **TCP and UDP** besides serial ports: TCP client, TCP server (one client at a time, connects and leaves are logged) and UDP. Pick the type at the left of the connection bar; for AI agents, open `tcp://host:port`, `tcp-server://:port` or `udp://host:port?local=:port` like a port.
- 🔁 **Auto-reconnect**: unplug and replug the adapter and the session carries on; the port list follows hot-plug.
- 🎛️ **Signals**: DTR / RTS switches, CTS / DSR / RI / CD lamps, and every change is marked in the log.
- 🤖 **AI-ready**: a built-in MCP server lets Claude Code and other agents
  - list and open ports
  - send data and wait for a matching reply
  - drive DTR / RTS

  A port you opened in the window can be used by the agent, and everything the agent sends shows up in the window.

## 📸 Screenshots

| Dark | Light |
|:---:|:---:|
| <img src="docs/images/terminal-dark.png" alt="Terminal page in the dark theme"> | <img src="docs/images/terminal-light.png" alt="Terminal page in the light theme"> |

<details>
<summary>🤖 AI page: MCP server settings</summary>

<img src="docs/images/ai-dark.png" width="800" alt="AI page with the MCP server enabled and the claude mcp add command">

</details>

## 📦 Download

Get the file for your system from [Releases](https://github.com/jerry-token/serialbot/releases):

| System | File | Notes |
|---|---|---|
| 🪟 Windows 10/11 | `SerialBot_*_x64-setup.exe` | Installer (~3.5 MB, compressed), no admin rights needed |
| 🪟 Windows 10/11 | `serialbot_windows_x64.exe` | Portable (~16 MB, uncompressed), just run it |
| 🍎 macOS 11+ | `SerialBot_*_universal.dmg` | Apple Silicon and Intel |
| 🐧 Ubuntu / Debian | `SerialBot_*_amd64.deb` | `sudo apt install ./SerialBot_*.deb` |
| 🐧 Other Linux | `SerialBot_*_amd64.AppImage` | `chmod +x`, then run |

<details>
<summary>⚠️ Warning on first launch?</summary>

- **macOS says the app "is damaged" or "can't be opened"**: the alpha is not notarized yet. Run once:
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
2. 📥 The receive view shows timestamps by default. The chips at the top right switch HEX view, sent data, auto-scroll and pause. 🔍 searches; ⚙️ sets the encoding, frame gap and ANSI colors.
3. 📤 Type a command in the box at the bottom and press `Enter`. Tick HEX to send bytes such as `01 03 00 00`.
4. 🎛️ To reset a board, use **DTR / RTS** in the status bar.

> [!TIP]
> Keep flow control at "None" unless your board wires CTS. With RTS/CTS on and CTS inactive, nothing gets sent.

## 🤖 Let AI agents use your ports (MCP)

1. Open **AI** on the left and tick **Enable MCP server**. It listens on `127.0.0.1` only and requires a token.
2. Press **Copy** and run the command in a terminal, for example:
   ```sh
   claude mcp add --transport http serialbot http://127.0.0.1:9633/mcp \
     --header "Authorization: Bearer <your token>"
   ```
3. Ask Claude Code: *"List the serial ports, open the ESP32 one and send `version`."* 🎉

| Tool | What it does |
|---|---|
| `port.list` / `session.list` | List ports / open sessions |
| `session.open` | Open a port (optionally with an alias such as `esp32`) |
| `io.write` / `io.read` | Send data / read the timestamped log from a cursor |
| `io.wait_for` | Wait until received data matches a regex |
| `io.send_and_expect` | Send a command and wait for the expected reply |
| `io.signals` | Set DTR / RTS, read CTS / DSR / RI / CD |

## 🗺️ Roadmap

- [x] Serial I/O, multiple sessions, timestamps, HEX
- [x] ANSI colors, encodings, frame split, search, smooth large logs
- [x] DTR / RTS and line states
- [x] Built-in MCP server
- [x] Installers for all three platforms, published automatically
- [x] Timed send, send history
- [x] Send a file
- [x] Command lists (groups, run in order)
- [x] Save received data to a file, export
- [x] Hot-plug detection, auto-reconnect
- [x] TCP client / server, UDP
- [ ] Built-in AI assistant "Bo"

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

## 📄 License

The core is [GPL-3.0-only](LICENSE). Plugin SDKs and device-side libraries will be MIT-licensed.
