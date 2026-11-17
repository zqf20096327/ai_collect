<p align="center">
  <img src="src-tauri/icons/128x128.png" width="128" height="128" alt="Loft app icon: a notch over the lines of a file" />
</p>

<h1 align="center">Loft</h1>

<h3 align="center">Your files. Your AI. Your machine.</h3>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22c55e?style=flat-square" alt="MIT license" /></a>
  <a href="#platform-status"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-1f6feb?style=flat-square" alt="Windows, macOS, and Linux" /></a>
  <a href="docs/building.md"><img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /></a>
  <a href="docs/building.md"><img src="https://img.shields.io/badge/Tauri-24C8DB?style=flat-square&logo=tauri&logoColor=white" alt="Tauri" /></a>
</p>

<p align="center"><strong>Official channels:</strong> <a href="https://github.com/nwaoga/loft">github.com/nwaoga/loft</a></p>

<p align="center">A local RAG notch that answers questions about the files in folders you choose — fully offline, on llama.cpp.</p>

<p align="center">
  <a href="#quick-start"><strong>Quick start</strong></a>
  &nbsp;·&nbsp;
  <a href="#on-your-machine"><strong>On your machine</strong></a>
  &nbsp;·&nbsp;
  <a href="docs/building.md"><strong>Building</strong></a>
  &nbsp;·&nbsp;
  <a href="docs/known-gaps.md"><strong>Known gaps</strong></a>
</p>

## Download

**Windows (x64).** Loft 0.1.2 is a full release. Download [Loft_0.1.2_x64-setup.exe](https://github.com/nwaoga/loft/releases/tag/v0.1.2) or [Loft_0.1.2_x64_en-US.msi](https://github.com/nwaoga/loft/releases/tag/v0.1.2). The `.exe` installs for the current user (no administrator needed) and adds Loft to the Start menu. Settings, models and indexes are kept in `%APPDATA%\com.loft.desktop`. The installer is unsigned, so Windows SmartScreen may warn: choose More info, then Run anyway. Check the download against `SHA256SUMS.txt`.

**macOS and Linux.** No installer in this release yet. Build from source using the steps below.

## Quick start

Node.js 18+ and Rust 1.85 or newer (the lockfile is edition 2024). Windows also needs the MSVC C++ build tools and the Windows 10/11 SDK. WebView2 is the webview, and it is already on Windows 11. Linux needs the packages in [Building](docs/building.md), including WebKitGTK 4.1 and the tray library. macOS needs the Xcode command-line tools.

```bash
npm install
npm run fetch-llama
```

`fetch-llama` downloads the llama.cpp server builds for **this** OS into `src-tauri/binaries/` (gitignored). Models are downloaded later, in the app.

**Windows.** `scripts\win-dev.bat` selects the MSVC toolset and runs the app.

**macOS and Linux:**

```bash
npm run tauri dev
```

The notch UI on its own, with mock data and no Rust: `npm run dev` → http://localhost:1420.

In the app: **Settings** (the gear) → download and select a chat model and an embedding model → **Folders** → add a folder → **Ask**. Ctrl/Cmd+Shift+Space summons the notch. [`sample-docs/`](sample-docs/) is a small folder for trying this. Its `scans/` hold a picture and a scanned PDF, to try OCR on Windows.

These builds are unsigned. macOS and Windows may warn you the first time. The app is not damaged. See [First open](docs/first-open.md). Installers and the per-platform steps are in [Building](docs/building.md).

<p align="center">
  <img src="docs/screenshots/answer.png" width="760" alt="Loft on Linux: an answer, the sources drawer open under it, and CPU named in the corner" />
</p>

<p align="center">An answer, with its sources open. Linux.</p>

## On your machine

Loft runs llama.cpp on this computer. A question does not call a cloud API and does not need an API key. Two local `llama-server` processes do the work: one for chat, one for embeddings (embedding models don't reliably share a process with chat).

<p align="center">
  <img src="docs/screenshots/notch.png" width="320" alt="The Loft notch, collapsed: a green dot, the name, and Ask your files" />
</p>

- The window is a notch: a pill at the top centre that expands. *Right* stands it on the right edge. *Floating* is a window you drag, and it stays where you leave it.
- The servers are official builds of one pinned llama.cpp release (`b12110`). Loft refuses an archive that does not match the size and SHA-256 in [`src-tauri/engines.json`](src-tauri/engines.json).
- A question the files don't cover is refused, and the refusal names your folders. Small talk ("hi", "thanks", "who are you?") gets a short reply instead, with no search.

## Ask your folders

Add a folder, or remove one, and ask about what is in it: text and code, PDF, Word, PowerPoint, spreadsheets, and pictures. Loft chunks them and keeps the index up to date as files change. Rebuild or delete that index from the same tab.

<p align="center">
  <img src="docs/screenshots/folders.png" width="640" alt="The Folders tab while a folder is indexing, showing the file count and the current file" />
</p>

- **Drag files straight onto the window** to add them without the folder picker. A dropped file is copied into a Loft **library** (kept at `<app data>/Library/`, so it stays even if you move or delete the original) and indexed; dropping the same file twice does nothing, and a type Loft can't read is kept but not indexed. Drop a folder and it is added in place. The library appears in **Folders** once you have dropped something.
- While a folder indexes it shows the file count and, for a large file, how far through that file it is.
- A file is capped at 2,000 chunks (about 3 MB of text). The folder says how many files were cut short. Rebuild to apply the cap to an older index.
- Pictures and scanned PDF pages are read with the OCR built into Windows. On macOS and Linux they yield no text. A picture with no readable text is not indexed, unless picture descriptions are on.

## Answers, with the sources

The reply leads. Under it, an "N sources" drawer holds the excerpts it was written from (open for the newest answer by default). Click one to open a document or picture in its default app. Code and scripts are only revealed in the file manager. They are never run.

<p align="center">
  <img src="docs/screenshots/answer.png" width="640" alt="An answer with the sources drawer open, each excerpt named with its file" />
</p>

- The question is embedded, the 6 nearest chunks are fetched, and chunks well below the best match are dropped. What remains (up to about 6 KB) goes into the prompt.
- A PDF opens at the cited page when the default PDF app is a browser (Edge, Chrome, Firefox…), Acrobat, or SumatraPDF on Windows. Otherwise it just opens.
- Small models are not asked for citation numbers in the prose. They get them wrong. The drawer is the citation.

## CPU, GPU, and an experimental NPU

You choose the engine and the device. CPU and Vulkan ship with `fetch-llama`. Metal does, on a Mac. CUDA and OpenVINO are optional, installed from Settings or with `npm run fetch-llama cuda` / `openvino`. Mains and battery can use different choices.

<p align="center">
  <img src="docs/screenshots/answer.png" width="640" alt="The same answer. The corner names the engine that is actually running: CPU, in this frame" />
</p>

- What the status shows is what the server's own log says is running. When that differs from the request, both are shown, with the reason.
- *Automatic* prefers a discrete GPU when plugged in, and built-in graphics or the CPU on battery, until you have measured them.
- OpenVINO is experimental and is not chosen automatically unless it has been measured. An Intel NPU has been run on one Windows laptop, with one model. Treat any other as unknown until *Try NPU now* reports a verified answer. The figures are in [Engines](docs/engines.md#openvino-and-the-npu-what-experimental-means-here).

## History stays local

Conversations are kept in `chats.db` in the app-data folder, and nowhere else. It is a different database from the index: deleting an index never touches a chat, and deleting a chat never touches your files.

<p align="center">
  <img src="docs/screenshots/answer.png" width="640" alt="The open conversation, with New chat at the top right. The history list is a separate panel and is not open here" />
</p>

- The question is stored when you ask it. The answer is stored when it ends, with the model, the usage figures, and the excerpts.
- Reopening a conversation shows it as it was saved. A file that is no longer indexed is marked *no longer available*. One whose contents changed is marked *changed since*.
- The saved history and the prompt are separate. The next question is still sent with the last 4 turns at most. **New chat** starts over. Loft reopens the last conversation at launch.

## Swap the model

The catalog is a built-in list. In Settings, download a chat model and an embedding model from it. A download that misses the SHA-256 in [`src-tauri/catalog.json`](src-tauri/catalog.json) is discarded. Only a different embedding model rebuilds the index. A different device keeps it.

<p align="center">
  <img src="docs/screenshots/folders.png" width="640" alt="The Folders tab. The gear at the top right opens Settings, which is where the models are chosen" />
</p>

- Chat: Qwen2.5 3B Instruct (the recommended one), Llama 3.2 3B, Gemma 3 4B, Phi 3.5 Mini. All Q4_K_M.
- Embeddings: Nomic Embed Text v1.5 (recommended), EmbeddingGemma 300M, and BGE-M3. The relevance floor is measured for the first two only. BGE-M3 still uses the default, which may be wrong for it.
- Picture descriptions are optional and off by default: SmolVLM 500M, a separate download. Descriptions are approximate and stored as such. Pictures inside PDFs and Office files are not described.

Length, tone, citations, temperature, and whether answers may leave your files are a sheet of options beside Send. They stay in the webview's local storage. The full list is in [How it works](docs/how-it-works.md).

## Platform status

The planned milestones (M0–M6) are implemented. What was actually run is narrower than that, and [HANDOVER.md](HANDOVER.md) is the record.

| Platform | Where it stands |
|---|---|
| Windows | **Tested** on Windows 11, on the CPU and on a Vulkan GPU. |
| macOS | **Initially validated.** Built and run once on a GitHub-hosted macOS 15 Apple Silicon runner (14 November 2026): Metal, an answer from `sample-docs`, window resizing, a tray icon in the menu bar, and an ad-hoc-signed `.app` and `.dmg`. The runner did not press the hotkey or open the tray menu, and it is not Retina. The owner has pressed Cmd+Shift+Space on a real Retina Mac and it summoned Loft. |
| Linux | **Built once under Xvfb** at 1920×1080 (x64): the debug app, a `.deb`, and an AppImage, an answer on the CPU, and Ctrl+Shift+Space via `xdotool`. The record is in [HANDOVER.md](HANDOVER.md). Still open: Wayland, a machine with a GPU, arm64, and installing those packages with a package manager. |

The rest of the holes — unsigned installers, OCR only on Windows, the NPU on one machine, power changes that were simulated — are in [Known gaps](docs/known-gaps.md).

## Further down

| Doc | What it holds |
|---|---|
| [How it works](docs/how-it-works.md) | Indexing, how an answer is built, OCR, options, follow-ups, chat history, and a map of the processes. |
| [Building](docs/building.md) | Windows, macOS, and Linux: prerequisites, debug runs, installers, signing. |
| [First open](docs/first-open.md) | Gatekeeper and SmartScreen, for these unsigned builds. |
| [Running Loft](docs/using.md) | Themes, notch or floating, tray, launch at login, icons. |
| [Engines, performance and battery](docs/engines.md) | Devices, fallback, OpenVINO, the NPU run, and the performance test. |
| [Testing](docs/testing.md) | Unit tests and the smoke scripts. |
| [Known gaps](docs/known-gaps.md) | What has not been exercised. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | The code, the data, and why it is shaped this way. |

## Project layout

```
src/                      # notch UI (Svelte 5 + Vite)
  App.svelte              # notch shell: pill ⇄ panel, tabs
  lib/components/         # Ask, Folders, Settings (themes, Models, general)
  lib/theme.svelte.ts     # theme list + remembered choice (colours are in app.css)
  lib/api.ts              # Tauri commands (+ browser mocks)
  lib/types.ts            # DTOs shared with Rust
src-tauri/                # Rust backend (Tauri 2)
  src/lib.rs              # commands, window sizing, tray, hotkey
  src/inference.rs        # engines and devices: the decision rules (no processes; unit-tested)
  src/engine.rs           # the coordinator: every start, switch and restart of a server
  src/runtime.rs          # finding the engines, starting and stopping llama-server
  src/hardware.rs, power.rs   # what the OS says: GPUs, NPUs, drivers; mains or battery
  src/installer.rs        # optional engines: pinned download, checksum, safe unpacking
  src/bench.rs            # Test performance, Try … now, and what the measurements suggest
  src/history.rs          # chat history: conversations, messages and their sources (chats.db)
  src/models.rs           # model downloads
  src/store.rs            # sqlite-vec store
  src/parse.rs, chunk.rs, indexer.rs, jobs.rs   # indexing + file watching
  src/ocr.rs              # text recognition for pictures and scanned PDF pages (Windows)
  src/vision.rs           # optional picture descriptions from a small vision model
  src/rag.rs, opener.rs   # answers + opening sources
  catalog.json            # curated model catalog (GGUF URLs)
  engines.json            # the llama.cpp builds of one pinned release, with checksums
  tauri.conf.json         # transparent, top-center, always-on-top window; bundle config
scripts/
  fetch-llama.mjs         # download + verify the llama.cpp builds for this OS
  make-engines-manifest.py   # re-pin engines.json to another llama.cpp release
  smoke-ui.js             # drives the real UI in a debug build (see docs/testing.md)
  smoke-engines.js        # the same for engines, power, fallback and the performance test
  smoke-restart.js        # after smoke-ui.js: the chat history survived closing Loft
  set-version.mjs         # the version number (package.json and Cargo.toml)
  icons.mjs               # src-tauri/icons from app-icon.svg (`npm run icons`)
  windows/release.bat     # a Windows release: version, checks, installer -> releases/windows/<version>/
  win-dev.bat, win-build.bat, msvc-env.bat   # Windows build environment
docs/                     # how it works, building, engines, testing, known gaps
app-icon.svg              # the icon's design: every size in src-tauri/icons is made from it
releases/                 # made by the release scripts, one folder per platform (not checked in)
```

## Milestones

- **M1** llama.cpp runtime: spawn + supervise the two servers.
- **M2** Model manager: download with progress + checksum, select chat + embed.
- **M3** Store & embeddings: sqlite-vec schema, embed + KNN query.
- **M4** Indexing: parsers (text/code/md/PDF/Office), chunker, incremental hashing, FS watch.
- **M5** RAG answers: retrieve → grounded prompt → streamed answer + sources; follow-up
  questions within a conversation.
- **M6** Polish & packaging: tray + quit, window sizing, GPU builds with CPU fallback, crash
  restart, launch at login, checksums, Windows installers.

## License

[MIT](LICENSE). Copyright (c) 2026 EAN Digital.

Issues and pull requests: [CONTRIBUTING.md](CONTRIBUTING.md). Vulnerabilities: [SECURITY.md](SECURITY.md).

<p align="center"><strong>Fork it. Break it. Make it yours.</strong></p>
