<p align="center">
  <img src="docs/images/icon.png" width="96" alt="Meboki icon">
</p>

<h1 align="center">Meboki</h1>

<p align="center">
  A private grammar checker for macOS.<br>
  An open-source AI model runs on your Mac and fixes your English in any app. Your text never leaves your Mac.
</p>

<p align="center">
  <a href="https://meboki.com">Website</a> ·
  <a href="https://meboki.com/api/download">Download</a> ·
  <a href="#build-from-source">Build from source</a> ·
  <a href="LICENSE">GPL-3.0</a>
</p>

![Meboki underlines mistakes in a note and shows the fix in a card](docs/images/screenshot.jpg)

## Features

- **Works in any app:** native text fields, Safari, Chrome and web editors such as Gmail, Notion, Slack, x.com and Obsidian.
- **Runs on your Mac:** Gemma 4 through a bundled [llama.cpp](https://github.com/ggml-org/llama.cpp) server. Works offline after the model download.
- **Apple Intelligence, no download:** on macOS 26 with Apple Intelligence on, Apple's on-device model can check your text right away. It fixed 39 of 45 test mistakes; Gemma 4 is more accurate (43 to 45).
- **Checks as you type,** or on demand with **⌃⌥G**.
- **Wavy underlines** by kind of mistake. Return applies every fix, Shift-Return applies one, and ⌘Z in your app undoes it.
- **Three popup styles:** glass card, anchored bubble, island under the menu bar.
- **US and UK English,** casual mode for chat apps, per-app On / Casual / Off.
- **Optional cloud** with your own OpenRouter or OpenAI key. Off by default.
- **No account, no telemetry.**

## Install

**Requirements:** Apple Silicon Mac, macOS 14 or later, about 5 GB of free disk for the model. On macOS 26 with Apple Intelligence on, no download is needed.

1. [Download the DMG](https://meboki.com/api/download) and drag Meboki to Applications.
2. Open it. The Welcome window walks you through setup:
   - choose the writing model: Apple Intelligence where it's available (no download), or download Gemma 4. Recommended: Apple Intelligence on 8 GB Macs, Gemma 4 E2B on 16 GB, Gemma 4 E4B on 32 GB or more;
   - turn on Meboki in **System Settings › Privacy & Security › Accessibility** (needed to go on);
   - try it on a sample sentence.

Reopen the guide any time: right-click the menu-bar icon › Welcome Guide.

## Usage

When the menu-bar popover says **Ready**, type in any text field. Meboki checks when you pause and underlines mistakes. In fields it doesn't check automatically (search boxes, terminals, code editors), press **⌃⌥G**. With a selection, ⌃⌥G checks only the selection.

Click an underline to open the fix:

| Key | Action |
|---|---|
| Return | Apply all fixes |
| Shift-Return | Apply this fix |
| Tab | Ignore |
| ← → | Previous / next fix |
| Esc | Close (Esc again hides the underlines) |

Keep typing and the underlines follow the text; the sentence you edit is checked again when you pause.

## Settings

Click the menu-bar icon, then the gear (or press ⌘,).

| Pane | What you set |
|---|---|
| General | Popup style, check as you type, launch at login, menu-bar icon, shortcut, updates |
| Appearance | Color tone of underlines and popups |
| Writing | US or UK English, what to check (Spelling, Grammar, Full), casual mode, protect names, code and links, explain each fix |
| Models | Apple Intelligence (macOS 26); download, switch, pause local models; cloud with your own key |
| Apps | On / Casual / Off per app |
| Privacy | Logs on or off (default off); short text snippets in logs on or off (default off) |
| Licence | Enter a licence key |

### Cloud with your own key

Settings › Models › **Cloud · your own API key**: pick OpenRouter or OpenAI, paste a key (stored in your login Keychain), pick a model, press **Test**, then **Use**. OpenRouter is limited to zero-data-retention hosts, OpenAI requests run with storage off. A cloud symbol shows while cloud is in use. Pick a local model to switch back.

## Trial and licence

The source code is free under GPL-3.0. The signed app from meboki.com has a 7-day full trial, counting only days you check text. After that it keeps working in **free mode**: ⌃⌥G checks any field with every model and your own key, and applying fixes and every privacy setting stay free. Checking as you type, the bubble and island styles, check level and casual mode need a licence.

The key is checked offline on your Mac. No account, no sign-in. With a licence installed, Meboki downloads the public list of refunded keys from meboki.com once a day; nothing about you or your key is sent.

## Known limits

- Works where the app exposes its text through Accessibility. Not in Google Docs or other canvas editors.
- Password fields and Secure Input are never read.
- If an app ignores Accessibility writes, Apply falls back to select and paste, then restores the clipboard.
- Some web and Electron fields don't report word positions: there's no underline, and the card opens below the field instead.
- Grammarly Desktop can capture Return. Click **Apply all** or pause Grammarly.

## Build from source

Needs Xcode 26 (selected with `xcode-select`), CMake (`brew install cmake`) and a code-signing identity. Create a free self-signed one first: see [docs/self-signed-certificate.md](docs/self-signed-certificate.md).

```sh
Scripts/build-llama-server.sh           # once: static Metal llama-server → Vendor/bin/ (~2 min)
Scripts/make-app.sh --install           # build, sign, copy to ~/Applications, open
Scripts/make-app.sh --debug --install   # DEBUG build with debug menus
```

Builds you make yourself have no auto-updater. Updates and releases: [docs/releasing.md](docs/releasing.md).

## Development

```sh
swift build                                       # app + core
swift test                                        # core unit tests (prompt, post-filters, diff)
MEBOKI_SERVER=http://127.0.0.1:8080 swift test    # plus live tests against a running llama-server
.build/debug/Meboki --gallery                     # design component gallery, light + dark
.build/debug/Meboki --demo-popups --all           # card, toast, bubble and island with sample content
```

| Path | What it holds |
|---|---|
| `Packages/Core` | `MebokiCore`: prompt, local and cloud clients, post-filters, word diff. No AppKit. |
| `App/Sources/Meboki` | The menu-bar app: Accessibility read and write, hotkey, underlines, popups, model download, llama-server process. |
| `App/Sources/Meboki/Design` | Design tokens and shared UI components. |
| `eval/` | Model and prompt benchmark. See [eval/README.md](eval/README.md). |

Logs: `~/Library/Logs/Meboki/`.

## Contributing

Issues and pull requests are welcome.

- Run `swift test` before opening a pull request.
- Changes to the prompt, post-filters or model files need an `eval/` run; include the numbers in the pull request.
- Report security issues privately to support@meboki.com.

## Licence

[GPL-3.0](LICENSE). Contributions are accepted under the same licence.
