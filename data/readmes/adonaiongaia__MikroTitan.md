# MikroTitan

<img src="docs/logo/mikrotitan-lockup.png" alt="MikroTitan" width="440" />

**A dual-inference local AI desktop studio.** Run **Janas-LLM** models with SSD streaming so models larger than RAM stay usable, or run **GGUF** models with **llama.cpp** — on your own hardware, with no account and no telemetry.

MikroTitan is a local AI studio with **agent mode**, a local document vault, **local voice input**, branching chat history, per-chat workspaces, system prompts and MCP tool scopes, crash-safe session storage, and three themes. It is built with **Tauri 2.12.6**, **Rust**, **React 18**, **TypeScript**, and **Tailwind CSS**, manages the `janas-server` and `llama-server` processes, proxies their OpenAI-compatible SSE streams into the webview, browses GGUF repositories on Hugging Face, and drives `janas-convert` / upstream `gguf2jns` with a live console.

> **Independent, unofficial project.** MikroTitan is a community project. It is not affiliated with, sponsored by, or endorsed by the Janas project or by llama.cpp. The official Janas project lives at <https://github.com/prabanta-dev/janas>.

**Engine attribution:** **Janas-LLM** by **Maurizio Cammalleri**, licensed under [GPL-3.0-or-later](https://github.com/prabanta-dev/janas/blob/main/LICENSE). llama.cpp is used through its upstream `llama-server` release and is not redistributed with this app.

## Key highlights

- **Dual engines.** `janas-server` streams `.jns` models from SSD, so a model larger than RAM can still run; `llama-server` runs `.gguf` models on CPU or GPU. One switch selects the engine, and the supervisor guarantees only one runs at a time.
- **Agent mode** — a bounded Think → Act → Observe loop with workspace tools, a live trace, risk-aware approvals (including per-workspace remembered commands), planning, auto-compaction, verification and per-file undo.
- **Local document vault** — persistent collections of notes, code, data and PDFs, searched on-device with hybrid BM25 + hashed TF-IDF retrieval, a per-chat Docs scope, and clickable `[D#]` citations in both chat and agent replies.
- **Local voice input** — toggle or hold-to-talk dictation backed by a managed `whisper.cpp` runtime and curated on-device models. Linux records the system-default Pulse/PipeWire microphone through native `parec`, with a `pw-record` fallback; transcripts can be inserted into the draft or sent immediately.
- **Branching chats** — edit a prompt or regenerate a reply without losing the old path; switch versions with arrows or branch a new chat from any message.
- **Per-chat context** — drafts, project bundles, workspace roots, system prompts and MCP tool scopes follow the chat instead of the window.
- **Persona library** — save a prompt as a reusable persona; chats without their own prompt inherit a separate saved default.
- **Smart model companions** — GGUF header inspection pairs vision projectors and vocabulary-matched speculative draft models, saves them as one-click bundles, and refuses unsafe combinations before llama.cpp starts.
- **Gated models** — an optional Hugging Face access token unlocks gated and private repositories without affecting public downloads.
- **Crash-safe history** — one JSON file per chat, schema v2, atomic writes, automatic previous-version backups, image assets on disk, and export/import/restore.
- **MCP scope controls** — a Tools badge, All/None controls, per-chat server selection, and automatic reconciliation when servers are removed or re-created.
- **Three themes** — Acid, Ember and Tide.

See [CHANGELOG.md](CHANGELOG.md) for the release history.

## Screenshots

![Chat workspace with branching history, a per-chat draft, and the MCP scope badge](docs/screenshots/chat-workspace.png)

*Chat workspace: branching history, per-chat drafts, and the MCP scope badge.*

![Agent run trace with plan, tool calls, context compaction, and changed files](docs/screenshots/agent-mode.png)

*Agent mode: plan, read/edit/run tool calls, context compaction, and run changes.*

![Per-chat MCP tool scope with All and None controls](docs/screenshots/mcp-scope.png)

*Per-chat MCP scope: All/None controls, enabled servers, and server-level auto-approve.*

## Quickstart (AppImage)

1. **Launch it.** `chmod +x "MikroTitan_0.2.0_amd64.AppImage"`, then run it. The build is unsigned, and it needs FUSE 2: install `libfuse2` if mounting fails, or start it with `APPIMAGE_EXTRACT_AND_RUN=1`.
2. **Let first-run setup finish.** The window opens immediately while the backend detects the CPU/GPU and downloads `llama-server` plus the current Janas release's `janas-server`, `janas-chat`, `gguf2jns` and `janas-mcp` into its managed `bin` folder. Progress, installed versions and warnings are in **Settings → Automatic engine setup**; **Retry setup** runs it again. The first run needs network access for both engines; later launches reuse the managed tools.
3. **Get a model.** Open **Models**, search Hugging Face, pick a quantization and download it. The file lands in your models folder and appears in **Library**.
4. **Load it.** Press **Use** in **Library**, or pick the file in the model selector at the top of the chat. A `.gguf` loads with llama.cpp; a `.jns` loads with Janas. To run a GGUF on Janas, compile it first in the **Compiler**. The Janas / llama.cpp switch and runtime flags live in **Engine Settings** on the right.
5. **Wait for Ready, then chat.** The bottom-left status card and the header pill show **Ready** once the engine is up. **Agent** enables agent mode, and **Tools** opens the per-chat MCP scope.
6. **Optional: set up voice input.** In **Settings → Voice**, install the managed `whisper-cli`, download a speech model, enable the composer microphone, and save the change. The mic button then records the system-default input; `Ctrl + Space` toggles dictation from the chat view.

## Core features

### Dual-engine architecture

MikroTitan runs two inference engines behind one interface:

- **Janas-LLM** — the experimental C engine. It runs `.jns` models and streams weights from SSD, which is what makes models larger than RAM usable. `janas-server` is launched with the selected model, host, port, optional API key and extra arguments, and its four states (`Disconnected`, `Indexing`, `LoadingModel`, `Ready`) are published over `engine://status`.
- **llama.cpp** — `llama-server` runs `.gguf` models on CPU or GPU. The adapter probes the installed build and only emits flags that build advertises.

Starting either engine stops the other. `EngineSupervisor` serializes every switch, stops the active engine and waits for it to release the hardware before launching the replacement.

The installer deliberately does **not** bundle a llama binary: a Tauri AppImage is mounted read-only under `/tmp/.mount_XXXXXX`, and the release archives differ by CPU, GPU and C runtime. The app downloads, verifies and updates the engine at runtime instead.

#### Runtime path strategy

All mutable engine files resolve through Tauri's `app_local_data_dir()`, never through the resource directory or the executable's folder:

```text
<app_local_data_dir>/bin/
  llama-server                 current verified binary
  llama-server.bak             exactly one previous binary
  libllama.so, libggml*.so     companion shared libraries
  janas-server                 current downloaded Janas release tools
  janas-chat
  gguf2jns
  janas-mcp
  libjanas_*.so                libraries from the same Janas release
  *.bak                        exactly one previous copy per Janas tool
  .rollback/llama/             libraries that belong with llama-server.bak
  .staging/<uuid>/             download and extraction workspace
<app_config_dir>/settings.json
```

#### Automatic onboarding and provisioning

`src-tauri/src/provision.rs` runs once in the background at startup. It never blocks the window and never writes into the AppImage mount. The startup task:

- Detects Linux/macOS/Windows, x86-64/ARM64, AVX2, Apple Silicon/Metal, NVIDIA CUDA (including the driver's CUDA version), AMD ROCm and Vulkan.
- Resolves the canonical `ggml-org/llama.cpp` repository (formerly `ggerganov/llama.cpp`) from the GitHub Releases API, preferring the latest stable tag. Because the current stable release may only contain `nightly-tag.txt`, it falls back to the newest release that actually contains a matching build and records that fallback in the report.
- Selects CUDA, ROCm, Vulkan, Metal or CPU assets by OS, architecture and backend, then retries the CPU asset if a GPU build is rejected by its startup probe.
- Installs `llama-server` through the same verified downloader, extraction guard, permission and rollback path used by Settings.
- Fetches the current pre-built `janas-server`, `janas-chat`, `gguf2jns` and `janas-mcp` tools from `prabanta-dev/janas` when they are missing, installs their shared libraries, and keeps one `.bak` per tool. No Janas binaries are bundled or pinned; existing working managed copies are left unchanged until you press **Retry setup**, which updates them to the current release.
- Creates and secures the engine cache (`~/.cache/janas` on Linux, the platform cache equivalent on macOS, and `%LOCALAPPDATA%\janas\cache` on Windows) without following a final-path symlink.

The report is available as JSON through `get_engine_setup_status`, a manual retry is exposed as `rerun_engine_setup`, and progress is emitted on `setup://status`. The Settings panel shows the detected hardware, selected releases, installed binaries, cache path and any fallback warnings.

The supervisor also writes a PID file and reconciles it on startup. A process is only signalled after `/proc/<pid>/cmdline` confirms that it is the expected engine, so a stale PID file can never kill an unrelated process. On Unix engines are spawned with their own process group and stopped with `SIGTERM` (then `SIGKILL`) against that group; a watcher removes the PID file on exit and the app's `RunEvent::Exit` path performs a final synchronous shutdown.

#### Version probing and CLI adapters

Before launch, the backend asynchronously runs `{binary} --version` and `{binary} --help`. `parse_build`, `first_version_line` and the `advertises` helpers select a flag layout from what the binary actually reports. If a build advertises an unknown layout, the app still launches with the safest common flags and emits `engine://adapter-warning`; the panel shows the warning instead of failing silently. Examples of adapted flags include `--flash-attn [on|off|auto]`, `--cache-type-k/v`, `--ctx-size` versus `--ctx`, and Janas's optional SSD streaming flags.

##### Vulkan KV-cache guard

llama.cpp's Vulkan backend cannot schedule the KV cache of a sliding-window or recurrent-hybrid model while that cache lives in a GPU buffer. Qwen3.8 (`qwen35`) is one example: it declares recurrent layers and a full-attention interval instead of a sliding-window size. Builds after b12236 abort inside the scheduler before the server binds its port:

```text
ggml-backend.cpp:1358: pre-allocated tensor (cache_k_l1 (view)) in a buffer (Vulkan0) that cannot run the operation (SET_ROWS)
```

The process dies with `SIGABRT`, which the app only sees as an immediate exit. Upstream issue #29082 tracks the regression. The probe therefore also runs `--list-devices` (skipped when the build does not advertise it), and the launch adapter falls back to CPU execution (`--device none`) when all of these hold: the build advertises `-nkvo`, a Vulkan device is available, GPU layers are requested, the build is newer than b12236, and the selected GGUF declares sliding-window or hybrid recurrent attention (`<architecture>.attention.sliding_window`, `<architecture>.attention.recurrent_layers`, or a nonzero `<architecture>.full_attention_interval`).

`-nkvo` is not a free substitute here: it leaves attention on the CPU while the weights stay on the GPU. Measured on a Radeon 660M iGPU with a 4 B Q5_K_M sliding-window model, that split produced 6.7 tok/s against 14.2 tok/s for a full CPU launch and 17.1 tok/s for b12236 with GPU KV offload, so a CPU launch is the safer automatic default. The substitution emits an `engine://adapter-warning` that names the issue and both overrides: `-nkvo` in **Extra llama arguments** keeps the weights on the GPU with a host KV cache (better when the model is larger than RAM), and `-kvo` forces GPU KV offload back on. Any explicit `--device`, `-nkvo` or `-kvo` in the extra arguments disables the fallback. Full-attention models, CPU-only launches, CUDA/ROCm/Metal hosts and b12236 and older are untouched.

#### Updates, backup and rollback

`download_and_extract_binary(engine_type, download_url)` accepts only `https://` URLs (HTTP is allowed for loopback test servers), streams progress on `engine://binary-progress`, and rejects archives that contain absolute paths, parent traversal, symlinks, too many entries or more than 8 GiB extracted. It stages the download under `bin/.staging`, installs companion libraries, sets `0o755`, renames the current binary to `[binary_name].bak`, and runs the new binary's probe. Release archives express SONAME aliases such as `libllama.so.0` as symlinks; safe extraction skips those links, so the installer materializes the aliases as regular library files before probing. A failed probe restores both the `.bak` binary and its library snapshot automatically. `rollback_binary(engine_type)` performs the same verified swap in reverse; the UI exposes both actions in Settings.

#### Engine Settings

The chat's Engine Settings panel has an explicit Janas / llama.cpp switch. The Top-K slider ranges from 1 to 100 (step 1, default 40) and sits next to Temperature and Top-P with live numeric feedback. With llama.cpp active, the panel exposes:

- `--n-gpu-layers` capped to the selected GGUF's block count, context size, Flash Attention and KV cache K/V quantization, plus llama tokens/s, KV usage and RSS.
- A llama-only **Direct CPU MoE Compute** toggle and a **Max CPU compute threads** field. The toggle enables llama.cpp's PR #30966 path with `--cpu-moe`, a 2 GiB `--moe-cache-mib` default, and `--moe-cache-cpu-share 1.0`; the thread value is passed as `--threads` only while the toggle is on. These are launch arguments scoped to the `llama-server` child, never Janas settings or `janas-server` flags.

With Janas active, the panel hides the GPU controls and exposes Flash attention (`JANAS_ATTN`: auto, exact or fast), KV cache quantization (`JANAS_KV`: auto, 8-bit or 16-bit), SSD streaming, an optional SSD cache directory, and live SSD read/IOPS/KV telemetry. Janas reads those two settings from its environment rather than accepting llama.cpp's `--flash-attn` and `--cache-type-k/v` flags. Model path, optional `--mmproj` vision projector for image input, llama port, binary URL, install, rollback and probe actions live in Settings. The llama section's **Extra llama arguments** box is parsed with shell-word rules; it is the place to override the default MoE cache size or thread count.

The Sampling block is capability-aware. On mount and whenever the active engine changes readiness, `get_backend_capabilities` probes loopback-only `/props`, `/v1/config`, `/v1/capabilities` and `/v1/models` with short timeouts. llama.cpp's generation settings are read strictly; Janas model/capability objects and `sampling_params`/`supported_parameters` lists are merged over safe defaults. Missing or null parameters are false. Today's Janas builds expose no sampling capability metadata, so the fallback hides Min-P while keeping Temperature, Top-P, Top-K, Repeat penalty and Max reply visible. If a later Janas build exposes those keys, the same UI unlocks them without an app update. A dependency-free DOM controller toggles `.hidden-param` on `[data-param]`; `.sampling-stack` uses flex gap so hidden controls leave no residual margin or broken grid rhythm.

#### Models, downloads and the GGUF → JNS compiler

- **Hugging Face explorer:** live search against `https://huggingface.co/api/models` with a GGUF-only filter and download/likes metadata. Results are enriched by reading each repository's tree API, showing real GGUF quantizations, file counts and byte sizes.
- **Download dialog and tray:** pick a quantization, preview destination paths and a RAM/VRAM estimate, then stream to disk with aggregate progress. Downloads run in Rust, are cancellable, emit `download://progress`, and support pause/resume; pausing keeps the stream open and resume continues from the same byte.
- **Gated repositories:** Settings has an optional Hugging Face access token. When set, it is sent only to `huggingface.co` on search, tree/checksum and download requests, so gated or private GGUF repositories work. A 401 points to an invalid or expired token; a 403 points to the model licence or the token's access. Public models keep working without one.
- **Model Library:** local `.jns`/`.gguf` files with architecture, parameter count, publisher, size and quantization, plus one-click activation. Thinking and Tools badges come from a GGUF chat template when present, otherwise from the model family/name; the badge tooltip says which source was used.
- **Integrity checks and cleanup:** verify any local model against the SHA-256 recorded in the download manifest, with a clear result when no upstream checksum was recorded. Delete a model with an awaited confirmation; the action is blocked while that file is the active model.
- **GGUF → JNS compiler:** drag-and-drop or native file picker, output path picker, overwrite guard and destination directory creation. A dedicated console shows timestamped stdout/stderr, error highlighting, copy/clear, percentage progress, elapsed time and output size. On success, **Use this model in Chat** saves it as the active model.
- **Converter resolution:** MikroTitan uses the `janas-convert` / `gguf2jns` path in Settings, then the managed copy, then `PATH`. If the converter name is left as `janas-convert` and it is not found, the studio also tries upstream's `gguf2jns`. `janas-server` uses the managed copy when it exists, otherwise the configured path.

#### Optional build-time sidecar declaration

The repository includes `src-tauri/tauri.sidecar.conf.json` as a reference fragment for developers who intentionally want a build-time sidecar:

```json
{
  "bundle": {
    "externalBin": ["binaries/llama-server"]
  }
}
```

Tauri v2 expects the actual source files beside that declaration with a target-triple suffix, for example:

```text
src-tauri/binaries/llama-server-x86_64-unknown-linux-gnu
src-tauri/binaries/llama-server-aarch64-unknown-linux-gnu
src-tauri/binaries/llama-server-x86_64-pc-windows-msvc.exe
src-tauri/binaries/llama-server-aarch64-apple-darwin
```

The config path stays unsuffixed; Tauri selects the file matching the build target and names the bundled resource `llama-server`. This fragment is **not** merged into `tauri.conf.json`, and the default build has no `externalBin` entry, so normal AppImage builds never require or ship a llama binary. If you deliberately opt in, merge the fragment with the Tauri CLI's `--config` option. At runtime every path still goes through the managed `bin` folder, including installs and rollbacks.

### Agent mode

The composer's **Agent** toggle turns a chat into a bounded tool-running loop. Instead of one completion, the model plans, calls tools, reads observations and continues until it finishes, hits the step limit or is stopped. The run is shown inline as a trace attached to the reply.

- **Workspace tools:** `read_file`, `write_file`, `edit_file`, `list_directory`, `search_files` and `run_command`. `search_knowledge_base` joins them when the chat has document collections attached. `web_search` is exposed only when the Internet toggle is on; enabled MCP tools in the chat's scope join the same tool list.
- **Workspace root:** file, search and shell tools stay disabled until a folder is chosen. A run pins that folder and cannot switch while it is active or has pending undo state. Picking a folder canonicalizes and validates it first. Each chat can override the global workspace, the Agent settings clear button removes both that override and the saved default, and a missing-folder error names the exact path. `AGENTS.md` or `.janas/instructions.md` in the workspace is injected into the agent prompt.
- **Approval policies:** *destructive* (read-only tools run automatically; writes, shell and MCP ask), *all* (everything except reads asks), or *full auto*. Irreversible commands (force-push, hard reset, recursive delete, publishing, `curl | sh`) and sensitive paths (`.env`, `.git`, SSH keys, cloud credentials) always ask, even under full auto. Tool output is scrubbed for likely secrets before it reaches the trace or model.
- **Remembered commands:** an approval card can remember one plain shell command for the current workspace. The rule covers the same command with extra arguments, but never compound commands, commands the secret scrubber recognises, irreversible commands or sensitive paths. Rules are stored per canonical workspace in `agent-approvals.json` and can be revoked individually or cleared in Engine Settings → Agent configuration. MCP tools are not covered.
- **File-edit shortcut:** approving a `write_file` or `edit_file` with “allow file edits for this run” skips later file-edit prompts for that run; shell and MCP calls remain gated.
- **Diff previews:** file-edit approvals show a bounded diff with added and removed line counts before you approve or reject.
- **Planning and limits:** an optional `<plan>` checklist before the first tool call, a 1–25 iteration cap, optional auto-compaction at a configurable share of the context window, and an optional verification command that runs after edits and before the agent may finish.
- **Trace:** plan, thoughts, each tool call with its risk and duration, approval cards, compaction notices, final status and changed files. The trace is stored with the chat message.
- **Undo:** workspace checkpoints keep bounded pre-images for a whole-run undo or per-file restore/keep. A run with pending changes locks the workspace root until those changes are undone or kept.
- **Stall protection and cancellation:** each model call allows up to 180 s for response headers and for the first streamed token, then 90 s of silence on an open stream. Stop aborts the pending HTTP request as well as the stream loop; a timeout ends the run with an actionable error instead of leaving the trace spinning, and Stop marks it **Stopped** immediately.
- **Broad model support:** engines with native tool calling use it directly; models without a tool template get a prompt-mode tool catalogue and fenced-JSON protocol. Tool schemas are budgeted against the active context window.
- **Safety:** paths resolve inside the pinned workspace, symlink escapes are rejected, commands run in their own process group and are killed on timeout or abort, and the approval matrix is covered by Rust tests.

### Local document vault (RAG)

The **Knowledge** view builds persistent, local collections from folders and files. Collections are independent of any chat; a chat attaches one or more of them with the composer's **Docs** button, and every turn retrieves only from that scope.

- **What can be indexed:** Markdown (`md`, `markdown`, `mdx`, `rst`), plain text (`txt`, `text`, `log`), source code (Rust, TypeScript/JavaScript, Python, Go, Java, C/C++, C#, Ruby, PHP, Swift, Kotlin, shell, SQL, HTML/CSS, Vue, Svelte, Lua, R and Elixir), structured data (`json`, `toml`, `yaml`/`yml`, `csv`/`tsv`, `ini`, `conf`, `cfg`, `xml`) and text PDFs. Scanned PDFs are reported as unreadable instead of silently producing an empty index. Hidden folders and the same `node_modules` / `target` / `.git` ignore list as project ingestion are skipped.
- **Incremental indexing:** each collection keeps a per-file manifest with modification time and SHA-256. Adding a folder indexes only new or changed files, while **Re-index** re-walks every saved source and skips unchanged ones. Indexing runs on the Rust blocking pool, streams `rag://index-progress`, can be cancelled between files, and keeps completed files. Removing a source or deleting a collection updates the manifest and index immediately.
- **Local hybrid retrieval:** Okapi BM25 ranks exact symbols, names and paths; a 512-dimensional hashed TF-IDF vector cosine ranks paraphrases and prose. Reciprocal Rank Fusion combines the two rankings. There is no embedding server, Python sidecar or network call.
- **Structure-aware chunks:** documents are split on headings and code/data boundaries toward about 420 tokens per chunk (520 maximum, 3 lines of overlap), with the nearest heading and a stable chunk id. Chunks carry their file and 1-based line range.
- **Budgeted citations:** retrieval runs before the prompt is sent, using only what is left of the running engine's real prompt budget after the system prompt, conversation, reply reserve and tool schemas. The selected chunks are appended to the system prompt as `[D1]`, `[D2]`, … and charged to the same token budget; if the context is too tight, the turn runs without vault context and says so rather than failing with HTTP 400.
- **Evidence and pills:** `chat://rag-sources` carries the retrieved chunks, token use and collection names. Inline `[D#]` markers become clickable pills, and a **Docs** row lists the cited files; clicking either opens the source drawer with the collection, path, line range, score and chunk text. The per-chat **Docs** drawer also exposes Top-K (1–16) and Max RAG tokens (128–4000), clamped against the live context window.
- **Agent lookups:** when collections are attached, the agent receives a read-only `search_knowledge_base` tool and can search across its iterations instead of a single prefetched block. The chunks it retrieves are attached to the final `agent:done` payload as `rag_sources`, so the agent's `[D#]` tags are clickable exactly like normal chat; repeated chunks and citation tags are deduplicated so one tag always points at one snippet.
- **Scope hygiene:** attached collection IDs are stored per chat, pruned when a collection is deleted, and shown in the composer's Docs badge. An empty scope means no retrieval, not every collection.

### Smart model companions

Large GGUF models are rarely useful alone. A multimodal build needs a matching `--mmproj` projector before it can read an image, and a small same-family draft model can make generation faster through speculative decoding. The companion manager discovers both from real GGUF metadata instead of filenames alone.

- **Header-only GGUF inspector.** A bounds-checked GGUF v2/v3 reader in `src-tauri/src/companions.rs` reads the magic, version, key/value metadata and tensor directory with `std::io::{Read, Seek}`. It captures `general.architecture`, `general.name`, `tokenizer.ggml.model`, the `tokenizer.ggml.tokens` count, `<architecture>.context_length`, `clip.*` / vision markers and tensor shapes. Parameter counts and vocabulary sizes come from the tensor directory; tensor payloads are never loaded, so a 60 GB file costs the same few hundred kilobytes of reads as a 200 MB one. Results are cached by path, size and modification time.
- **Roles from evidence.** Files are classified as **text model**, **vision model**, **vision projector** (`mmproj` name, `clip` architecture, or a vocab-less file with vision tensors) or **draft-sized** (≤ 3B parameters with a tokenizer). Vision families (Qwen2.5-VL, Qwen3-VL, Gemma 3, LLaVA, MiniCPM-V, Pixtral/Mistral-Small-3, InternVL and others) are normalised for comparison; Gemma 3 1B/270M stay text-only because their files carry no vision tower.
- **Safe pairing rules.** A draft model is only offered when its `general.architecture` **and** exact vocabulary size match the main model — a mismatch aborts `llama-server` before it binds its port. Projectors are ranked by family match, shared folder, name overlap and quant (f16, then bf16, then q8_0) and are marked incompatible across families rather than guessed.
- **Library badges and drawer.** **Vision ready**, **Missing MMPROJ · Pair**, **Draft paired (+Speculative)** and **Draft available** badges sit on every library row. **Pair** opens a drawer that lists every local projector and draft-sized model with its compatibility reasons, shows the combined **Main + Draft + MMPROJ** footprint with a resident RAM estimate and a fully-offloaded VRAM estimate, and validates the exact tuple before **Use bundle** applies it and restarts llama.cpp.
- **Saved bundles.** A bundle stores `(main_model_path, mmproj_path, draft_model_path, draft_max_tokens, draft_min_tokens, draft_p_min)`. Bundles live in `settings.json`; **Use bundle** sets the llama.cpp model, projector and draft paths in one action, and pressing **Use** on a library model that already has a saved bundle re-applies that bundle's projector and draft paths. Deleting a projector or draft file that an active bundle still binds is refused.
- **Hugging Face bundle inspector.** The download dialog asks the Hub for a repo's tree once, splits `mmproj-*.gguf` files out of the main quantization list, preselects the reference projector (f16 or bf16), shows the combined download size, and queues the main files plus the projector in one download. A non-intrusive hint names a 0.5B / 1B / 1.5B sibling under the same publisher when one exists.
- **Engine wiring and guardrails.** llama.cpp receives `--mmproj`, `--spec-draft-model` (`--model-draft` on older builds) and, when the probed help text advertises them, `--draft-max` (default 8), `--draft-min` and `--draft-p-min`. The composer inspects the active model as soon as an image is attached; if it is a vision model without a bound projector, an inline banner offers **Pair detected MMPROJ** or **Download MMPROJ** and send is blocked until it is resolved.

### Voice input

Voice input is local dictation backed by a managed `whisper.cpp` runtime. It is off until enabled in **Settings → Voice**, where you can install or update `whisper-cli`, download one of four curated GGML models (Tiny English, Base English, Small multilingual, Large v3 Turbo Q5_0), choose a spoken language, and test the microphone. The runtime and models live in the app data directory; on Linux, no system Whisper installation is required.

- **Composer dictation:** the mic button records canonical 16 kHz mono WAV. Use click-to-toggle or hold-to-talk, `Ctrl + Space` to toggle, `Enter` to finish and transcribe, and `Esc` to cancel. Finished text is inserted into the current chat's draft, or sent immediately when **Auto-send transcripts** is enabled and the composer is empty and idle; a non-empty draft or pending images are never discarded. **Strip non-speech annotations** removes Whisper output such as `[BLANK_AUDIO]` and `(music)`.
- **Linux default source:** on Linux the webview's `getUserMedia` path is bypassed. Rust records the Pulse/PipeWire system default through `parec --device=@DEFAULT_SOURCE@`, falling back to `pw-record` when `parec` is absent. This avoids WebKitGTK selecting the first enumerated input instead of the desktop default. Other platforms use the Web Audio path.
- **Microphone test and setup:** Settings → Voice installs the isolated `whisper-cli` runtime with its own libraries and keeps one previous runtime for update rollback. Model downloads show progress and are verified against pinned SHA-256 digests. A four-second mic test exercises the same capture path without transcribing.
- **Audio files:** attach or drop WAV, MP3, OGG or FLAC files up to 200 MB (two per drop); their transcripts are appended to the draft. WebM/Opus is converted in the webview when its decoder is available, because whisper.cpp's release CLI does not decode it.
- **Local only:** audio is normalised to 16 kHz mono WAV and handed to the local `whisper-cli` process; it is never uploaded. Runtime installation and model downloads are explicit actions.

### Chat workspace and MCP

- **Chat sessions rail** (left, collapsible) with multiple chats, search, rename, pinning, per-chat deletion, per-chat import/export, and a **Memory** tab.
- **Rust-backed chat store (schema v2):** each chat is one JSON file under the app data directory, with images extracted to `assets/<chat-id>/`. Saves are atomic and keep one previous version per chat. Settings → Chat history and backups exposes size stats, whole-shelf export/import, restore of the previous version, and orphaned-image cleanup.
- **Branching and version history:** editing a user turn or regenerating a reply preserves the old suffix as an archived branch. Previous/next arrows switch sibling versions; **Branch** creates a new chat from the selected message's prefix. Branches inherit the source chat's project, workspace and MCP scope but not its draft.
- **Per-chat drafts and context:** composer text and pending images are saved per chat and restored after restart. Attached projects, workspace roots, document collections, system prompts and MCP server scopes are also per chat, while sampling settings remain global. A debounced save plus close-time flush keeps pending edits from being lost when the window closes.
- **Per-chat system prompt and personas:** the system prompt panel shows whether the chat is using the saved default or its own prompt. **Use default** clears the override, **Make default** copies the current prompt into the default for new and unmodified chats, and **Save as persona** stores a reusable prompt in a machine-local persona library. Personas can be applied to a chat or deleted; deleting one does not alter chats that already use its text. Branches inherit the source chat's prompt.
- **Token-aware context budget:** every send reserves space for the reply, keeps the system prompt and current turn, trims attached project/web context first, then drops or truncates the oldest turns until the prompt fits the **context the running engine was actually launched with**, not an edited setting that has not been restarted. If the current message and system prompt alone cannot fit, the send is stopped before it is added to the transcript, and the input stays editable. The Rust proxy is also a safety net: if either server still returns HTTP 400 with its context size, the prompt is rebuilt around the current turn and retried once automatically. MCP tool definitions count as prompt input too; when an enabled server's schema cannot fit, the turn runs without those tools and the app explains why instead of sending an impossible request.
- **System Telemetry** (bottom, collapsible): a separate **prompt-read** and **reply-write** token ticker, SSD read throughput and IOPS sampled from the engine's `/proc/<pid>/io`, RSS/CPU, GPU/NPU counters from sysfs when the driver exposes them, an estimated RAM-vs-disk layer split, an expert-routing heatmap, and a 64 MB storage benchmark that warns when a drive will bottleneck 48 GB or 70 B+ mixtures.
- **Composer:** a context-window ring next to Send, image attachments with a patch-token estimate, drag-and-drop project ingestion, an Internet toggle, and the per-chat Docs scope with retrieval tuning.
- **Internet pipeline:** DuckDuckGo (with a Bing fallback) → top three pages fetched and converted to text → bundled with the prompt as numbered `[S1]` evidence. A live ticker reports each stage, and the reply carries clickable source badges that open in the system browser.
- **Persistent memory:** the model can call its `save_to_memory_bank` tool to store durable facts in a Rust-managed JSON bank on disk. Facts are recalled by local vector similarity, injected into the next relevant turn, and can be added, corrected, or forgotten from the Memory tab. The system prompt tells the model when to save and forbids storing secrets.
- **Streaming resilience:** the Rust SSE proxy tolerates CRLF, split chunks, raw newline-delimited JSON, malformed frames, final chunks without a newline, reasoning aliases, and content arrays. Malformed chunks are counted instead of crashing the app, and the chat view is wrapped in a render boundary so one bad reply cannot blank the window.
- **Project ingestion:** drop a folder on the window (or pick it) and the studio walks the tree, skips build/vendor noise, and builds a semantic bundle with a token estimate before sending it to the prefill layer.
- **Message actions** under every prompt and reply: copy, edit and resend, delete, branch, and previous/next version arrows for sibling replies.
- **MCP Server Hub:** register stdio servers with arguments, per-server environment variables and an optional working directory. Probes allow 30 seconds for startup, capture stderr and report early exits. Enabled servers' tools are namespaced into the chat model's tool list, executed through the same stdio session during the turn, and shown in the activity drawer. Per-server auto-approve skips the approval card for normal chat tool calls.
- **Per-chat MCP tool scope:** the Tools drawer shows an All/None/count badge, a zero-tools warning, and checkboxes for the enabled servers. An empty selection stores `[]` and sends no MCP tools; leaving the scope untouched means all enabled servers. Scopes are applied to both normal and agent requests. On chat load, servers that no longer exist are pruned and servers re-created under the same name are remapped to their new ID.
- **Themes and settings:** Acid (lime/graphite), Ember (copper/soot) and Tide (cyan/deep water), selectable in Settings and persisted locally. Settings also holds engine and converter binary paths with a `--version` probe, the active `.jns` model, models folder, server host/port, extra arguments, local API key, the optional Hugging Face token, local model scanning, agent preferences, remembered command rules, voice setup, chat-history maintenance and reset-defaults actions.
- **Chat runtime:** per-chat system prompt with a saved default, Temperature (0.0–2.0) and Top-P (0.0–1.0) in every request payload, a live status pill for all four engine states, streaming markdown with reasoning blocks, copy actions, stop generation, token/timing stats, and an automatic engine restart when the active `.jns` model changes.

### Privacy and network access

MikroTitan has no accounts, analytics, crash reporting or telemetry upload. Chat history, images, project bundles, document-vault collections and memory facts are written to the local app data directory, and runtime settings to the platform config directory; small UI preferences such as the theme, agent defaults, the saved default system prompt and personas live in local storage. Voice audio is captured and transcribed locally by the managed `whisper-cli`; recordings are not uploaded and are not added to chat history. The transcript becomes a draft or chat message under the same local storage rules. The settings file (which may contain the local API key and Hugging Face token) and the agent approval-rule file are restricted to the owner on Unix. The engine runs locally and binds to loopback by default, and the webview's CSP only permits its own origin, Tauri IPC and the local dev server, so network calls happen in the Rust backend.

**Engine setup runs automatically at startup**, whether or not you open Settings. On every launch the app detects the host and checks GitHub for the latest llama.cpp release, so one request reaches `api.github.com` even if you never download a model. It looks up Janas releases only when its managed Janas tools are missing or unusable, and it downloads a binary only when one needs installing or you press **Retry setup**. Whisper's runtime and models are downloaded only when you press **Install** or **Download** in Settings → Voice. Apart from those explicit setup actions and the startup check, the remaining network features are user-triggered:

| Feature | What is sent | Destination |
| --- | --- | --- |
| Engine setup | An automatic release lookup at every startup; binary downloads when an engine needs installing, or when you retry setup | `api.github.com` and GitHub release assets |
| Voice setup and models | A whisper.cpp release lookup and runtime download when you press Install; the selected GGML model from Hugging Face when you press Download. Audio and transcripts are never uploaded | `api.github.com`, GitHub release assets and `huggingface.co` |
| Model search and download | Search terms, the selected repository/file, and the optional Hugging Face token when one is configured | `huggingface.co` |
| Web search, with **Internet** on | The search query, then the result pages it reads | DuckDuckGo (Bing fallback) and those result sites |
| Opening a citation | The URL you click | Your default browser |

**System Telemetry** is sampled locally from the engine process and the kernel and is never uploaded.

MCP servers run as local stdio processes. The app does not proxy their traffic, so a server can make its own network calls; register only servers you trust. Agent `run_command` executes on this machine under the approval policy you choose. Tool output is scrubbed for likely secrets before it reaches the trace or model, and sensitive paths (`.env`, `.git`, SSH keys, cloud credentials) always require approval, even under full auto.

## Requirements and building from source

### Requirements

- **Tested platform:** Linux x86-64, running the AppImage built below. This is the only bundle target in `tauri.conf.json`; the build and runtime checks below were run on it.
- **Untested platforms:** the engine and provisioning modules contain macOS and Windows paths, but no macOS or Windows installer is configured or tested here. Treat those paths as unverified.
- Rust 1.77.2+ and Node 18+.
- **Tauri 2.12.6**, pinned in `src-tauri/Cargo.lock`. This release fixes the webview-manager event-emit deadlock that could freeze the window while the `tracing` feature was enabled; keep the lockfile at 2.12.6 or newer.
- For voice input on Linux, at least one of `parec` (usually from `pulseaudio-utils`) or `pw-record` (usually from `pipewire-bin`). The app prefers `parec` and falls back to `pw-record`. Whisper itself is downloaded by the app on demand.
- WebKitGTK 4.1 / GTK3 development packages, plus the GStreamer plugins that
  `bundleMediaFramework` copies into the AppImage:

```bash
sudo apt install build-essential pkg-config file libwebkit2gtk-4.1-dev \
  libgtk-3-dev librsvg2-dev patchelf libfuse2 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
  gstreamer1.0-alsa gstreamer1.0-pipewire
```

The GStreamer runtime set covers PulseAudio/PipeWire/ALSA capture and the
WAV/MP3/OGG/FLAC decoders used for audio attachments. The bundler copies the
plugins installed on the build host; `-dev` packages are not needed for them.

- A local Janas build is optional: startup setup downloads the current release. For a manual install, upstream's release tarball provides `janas-server`, `janas-chat`, `gguf2jns`, `janas-mcp`, `jns_planes` and the shared libraries:

```bash
curl -LO https://github.com/prabanta-dev/janas/releases/latest/download/janas-linux-x86_64.tar.gz
tar xf janas-linux-x86_64.tar.gz
```

> Upstream Janas is an early, experimental engine whose CLI and API change without notice. Verify flags against the release you install. Point the studio at a server that implements `POST /v1/chat/completions` and `GET /health`, which is the contract used here.

### Run from source

```bash
npm install
npm run tauri dev
```

The Vite dev server runs on `http://localhost:1420`; the Rust backend owns the window and the engine processes.

### Build an AppImage

Build on **Ubuntu 22.04** (or another system with the same glibc 2.35 baseline and WebKitGTK 4.1). An AppImage does not bundle glibc, so it can only be as old as the build host; an AppImage built on Ubuntu 24.04 or Linux Mint 22 needs glibc 2.39 and will not start on Ubuntu 22.04, which is what AppImageHub tests.

```bash
npm run appimage
```

The build ends with `scripts/check-appimage-glibc.sh`, which extracts the AppImage and fails if any bundled ELF file needs a glibc newer than 2.35. For a local-only build on a newer host, `APPIMAGE_MAX_GLIBC=2.39 npm run appimage` overrides the guard; do not upload that artifact. For a release build on a newer host, use the Docker target below.

The artifact is written to:

```text
src-tauri/target/release/bundle/appimage/MikroTitan_0.2.0_amd64.AppImage
```

Run it with `chmod +x` and execute directly. The image bundles its WebKitGTK/GTK runtime libraries (verified with `ldd` on the extracted payload); a graphical Linux session with working display and GPU drivers is still required.

For releases, run **Actions → Build AppImage** and set the release tag (for example `MikroTitan`) to replace that release's AppImage asset with the Ubuntu 22.04 build. Leave the tag empty to only produce a workflow artifact.

### Build the AppImage with Docker (Ubuntu 22.04)

If Docker is installed but the host is not Ubuntu 22.04, build the release artifact in a jammy container:

```bash
npm run appimage:docker
```

This uses `Dockerfile.appimage` and writes `release/MikroTitan_0.2.0_amd64.AppImage`. The first run installs the toolchain and compiles the Rust dependencies; later runs reuse the BuildKit Cargo cache. The container uses the same dependency set as the **Build AppImage** workflow, runs `scripts/check-appimage-glibc.sh` before the artifact leaves the build stage, and the wrapper checks the extracted file again on the host.

Upload the local artifact to an existing release with the GitHub UI or:

```bash
gh release upload MikroTitan release/MikroTitan_0.2.0_amd64.AppImage --clobber
```

### Dual-engine integration harness

The mock-runtime harness uses Tauri's `MockRuntime` and compiles a dependency-free fake server into a temporary managed bin directory as both `llama-server` and `janas-server`. It starts llama.cpp, switches to Janas through the real `EngineManager`, switches back to llama.cpp, and exercises process-group shutdown, log forwarding, `/health` readiness, `/metrics` telemetry and active-engine events without a model, GPU or external service.

```bash
./scripts/run-dual-engine-harness.sh
```

The failed-update test in `src-tauri/src/engines/binary.rs` installs a deliberately silent binary, verifies that it fails the probe, and asserts that the previous binary and executable permissions are restored.

## Architecture and IPC reference

`EngineRunner` is the trait both engines implement, and its surface is intentionally identical:

```rust
#[async_trait]
pub trait EngineRunner: Send + Sync {
    async fn spawn_process(&self, app: &AppHandle, settings: &AppSettings) -> AppResult<EngineLaunch>;
    async fn kill_process(&self, app: &AppHandle, launch: &EngineLaunch) -> AppResult<()>;
    async fn monitor_telemetry(&self, app: &AppHandle, launch: EngineLaunch) -> AppResult<()>;
}
```

<details>
<summary><strong>Source directory tree</strong></summary>

```text
src/
  types.ts                 shared IPC and UI types
  lib/api.ts               typed invoke wrappers + event names
  lib/chatSessions.ts      session normalization, branching, versions, drafts
  lib/mcpScope.ts          per-chat MCP filtering, request inputs, reconciliation
  lib/rag.ts               citation pills, per-chat retrieval tuning and scope helpers
  hooks/                   engine, settings, chat, agent, downloads, converter, voice
  components/chat/         workspace, messages, composer, agent trace, MCP drawer, sessions rail
  components/knowledge/    knowledge vault, Docs drawer, source drawer
  components/models/       marketplace, library, download dialog/tray
  components/mcp/          server hub
  components/converter/    compiler form and console
  components/settings/     runtime, theme, voice, and chat-history panels
src-tauri/src/
  main.rs                  Tauri setup, state, command registration
  engine.rs                Janas lifecycle, SSE proxy, knowledge retrieval and tool loop
  agent.rs                 agent loop, workspace tools, approvals, approval rules and safety
  agent/checkpoint.rs      per-run file pre-images and undo state
  rag.rs                   local document vault: indexing, hybrid retrieval and citations
  engines/                 dual-engine supervisor, Janas/llama adapters, binary installer
  linux_media.rs           WebKitGTK media-capture permission and stream setup
  native_audio.rs          Linux default-source capture (parec, then pw-record)
  whisper.rs               managed whisper.cpp runtime, WAV normalisation and transcription
  chat_store.rs            schema-v2 chat sessions, assets, backups, export/import
  mcp.rs                   stdio MCP client/runtime and probes
  provision.rs             startup hardware detection and engine provisioning
  companions.rs            GGUF header inspector, projector/draft pairing, saved bundles
  converter.rs             janas-convert job runner
  huggingface.rs           Hub search, quant discovery, downloads
  capabilities.rs          runtime sampling-capability probing
  settings.rs              persisted config, Hugging Face token, binary resolution, probing
  memory.rs                persistent memory bank + save_to_memory_bank handler
  system.rs                telemetry, benchmark, ingest, web search, library, model verify/delete, MCP, source opener
  error.rs                 serializable command errors
```

</details>

<details>
<summary><strong>Rust engine modules</strong></summary>

- `src-tauri/src/engines/mod.rs` — `EngineRunner` trait, `EngineKind`, `EngineSupervisor`, the `tokio::sync::Mutex` state machine, managed-path helpers, process-group cleanup, CLI probing, log forwarding and telemetry.
- `src-tauri/src/engines/llama.rs` — version/help probe, argument adapters for legacy, transitional and modern llama.cpp builds, health/`/metrics` polling, GPU layers, context, Flash Attention, KV cache K/V, Top-K, jinja, metrics and shared-library resolution.
- `src-tauri/src/engines/janas.rs` — wraps the original `EngineManager` without removing its log promotion, health checks or SSE proxy; it prefers `bin/janas-server` when that managed binary exists, and the launch path applies Janas's `JANAS_ATTN` and `JANAS_KV` environment overrides.
- `src-tauri/src/engines/binary.rs` — streaming downloader, ZIP/tar.gz/single-executable extraction with path traversal and size guards, `0o755` permissions, one-step backup, post-install probe, automatic restore on failure, manual rollback and managed-binary probe.
- `src-tauri/src/provision.rs` — startup hardware detection, GitHub release/asset selection, Janas multi-binary provisioning, cache preparation and the JSON setup report.
- `src-tauri/src/engine.rs` — spawns `janas-server`, publishes the four engine states, streams stdout/stderr to `engine://log`, promotes state from log lines, stops with `SIGTERM` (or `kill` on Windows), waits six seconds, then force-kills, and proxies `POST /v1/chat/completions` with `stream: true` by parsing SSE in Rust and emitting `chat://delta`, `chat://done`, and `chat://error`. This avoids CORS and keeps the local engine bound to loopback.
- `src-tauri/src/converter.rs` — launches the converter with `--input <gguf> --output <jns>`, or positional arguments when the binary is upstream's `gguf2jns`. Tracks stdout/stderr, parses percentages, emits `convert://log`, `convert://progress`, `convert://started`, and `convert://finished`, and supports cancel.
- The `save_to_memory_bank` tool runs a bounded tool loop: streamed `tool_calls` are reassembled by index, validated, executed against the on-disk memory bank, and returned to the model for a follow-up reply. Malformed tool arguments become a normal tool error the model can correct instead of terminating the stream. Cancellation drops the HTTP stream promptly.

New UI pieces: `chat/SessionsRail`, `chat/EnginePanel`, `chat/TelemetryPanel`, `chat/TokenTicker`, `chat/Composer` (multimodal), `chat/AgentTrace`, `chat/McpLogDrawer`, `models/ModelLibraryView`, `mcp/McpView`, `settings/ThemePicker`, `settings/VoiceSettings`, and `settings/ChatHistoryPanel`.

Voice capture lives in `hooks/useVoiceRecorder.ts`. On Linux it delegates to the native commands; elsewhere it uses Web Audio and encodes the same canonical WAV before invoking Whisper.

</details>

<details>
<summary><strong>IPC commands</strong></summary>

| Command | Purpose |
| --- | --- |
| `start_engine`, `stop_engine`, `get_engine_status` | process lifecycle |
| `switch_engine(engine)` | `"janas"`, `"llama"` or `"none"`; performs mutual exclusion |
| `get_active_engine` | active engine metadata |
| `stream_chat`, `cancel_chat` | SSE proxy and cancellation |
| `start_conversion`, `cancel_conversion` | converter lifecycle |
| `search_models`, `list_model_quants` | Hugging Face metadata |
| `start_download`, `cancel_download`, `pause_download`, `resume_download` | downloads and pause/resume |
| `get_settings`, `save_settings`, `probe_binary`, `scan_local_models` | configuration |
| `get_telemetry`, `benchmark_storage` | hardware sampling and drive test |
| `ingest_project`, `web_search`, `transcribe_audio`, `transcribe_audio_file` | project, web and speech pipelines |
| `save_to_memory_bank`, `memory_list`, `memory_update`, `memory_delete`, `memory_clear` | persistent memory bank |
| `open_external` | open a citation in the system browser |
| `library_models`, `mcp_probe` | local model shelf with thinking/tool badges and MCP handshake with stderr/exit diagnostics |
| `get_backend_capabilities` | dynamic sampling-control availability from the active engine |
| `download_and_extract_binary(engine_type, download_url)` | install or update a managed binary |
| `rollback_binary(engine_type)` | restore the single `.bak` and its libraries |
| `probe_managed_binary(engine_type)` | probe the installed binary without launching it |
| `get_engine_setup_status` | return the latest hardware/provisioning report as JSON |
| `rerun_engine_setup` | re-run detection and provisioning (forced update/retry) |
| `get_whisper_status`, `install_whisper_binary`, `download_whisper_model`, `cancel_whisper_download` | Whisper runtime/model management and progress |
| `start_native_capture`, `stop_native_capture`, `cancel_native_capture`, `native_capture_level` | Linux default-source microphone capture and live meter |
| `chat_sessions_list`, `chat_session_save`, `chat_session_delete`, `chat_asset_data_url` | schema-v2 session store and image assets |
| `chat_export_session`, `chat_import_session`, `chat_branch_session`, `chat_export_all`, `chat_import_all`, `chat_backup_list`, `chat_restore_backup`, `chat_store_gc`, `chat_store_stats` | branching, backup, export/import and maintenance |
| `verify_local_model`, `delete_local_model` | SHA-256 verification and model deletion |
| `agent_start`, `agent_resolve_approval`, `agent_abort` | agent run, approval decisions and cancellation |
| `agent_validate_workspace` | canonicalize and validate a workspace folder before it is pinned |
| `agent_approval_rules`, `agent_forget_approval_rule`, `agent_clear_approval_rules` | list, revoke and clear remembered shell commands for a workspace |
| `agent_undo`, `agent_undo_file`, `agent_keep_file`, `agent_undo_availability`, `agent_undo_state` | per-run and per-file agent undo |
| `rag_list_collections`, `rag_collection_detail`, `rag_create_collection`, `rag_delete_collection`, `rag_index_paths`, `rag_reindex_collection`, `rag_cancel_index`, `rag_query`, `rag_remove_path` | local document vault collections, indexing and retrieval |

</details>

<details>
<summary><strong>Events</strong></summary>

| Event | Payload |
| --- | --- |
| `engine://status` | full `EngineSnapshot` |
| `engine://active` | `ActiveEngineInfo` or `null` |
| `engine://log` | stream, line, timestamp |
| `engine://telemetry` | Tokens/s, KV usage, SSD read throughput/IOPS and RSS |
| `engine://adapter-warning` | Unknown CLI layout warning with version and adapter name |
| `engine://binary-progress` | Download/extract/install phase and percentage |
| `engine://exited` | Process exited; the UI refreshes the snapshot |
| `setup://status` | Current `SetupReport` during startup or a manual retry |
| `chat://delta` / `chat://done` / `chat://error` | streaming reply lifecycle |
| `memory://changed` | the full memory list after a model or user write |
| `convert://log` / `convert://progress` / `convert://finished` | build console |
| `download://progress` | aggregate download status |
| `whisper://progress` | Whisper runtime install or model download phase, bytes and percentage |
| `chat://notice` / `chat://tool-approval` | context/tool notices and MCP approval requests |
| `chat://rag-sources` | retrieved document chunks, token use and collection names |
| `rag://index-progress` | collection index phase, file/chunk counts and percentage |
| `mcp://activity` | MCP handshake and tool activity |
| `agent:plan` / `agent:thought` / `agent:tool_start` / `agent:tool_result` | agent plan, live reasoning and tool steps |
| `agent:approval_needed` / `agent:context_compacted` / `agent:done` / `agent:error` / `agent:notice` | agent approvals, compaction and completion; `agent:done` also carries the run's `rag_sources` |

The OpenAI-compatible `/v1/chat/completions` SSE proxy is reused for both engines. It accepts a `top_k` integer in the request payload and routes to the active engine's host and port instead of assuming Janas is running on the settings port.

</details>

## Notes, limitations and verification

### Verification summary

The **0.2.0** AppImage was rebuilt against Tauri 2.12.6 and inspected on Linux x86-64. `npm run build` (TypeScript + Vite), `cargo check`, the full Vitest suite and the full Rust suite pass for this revision; the manual runtime checks further down were recorded during 0.1.1 verification.

- `npm run appimage` — release build and AppImage bundling completed:
  - Artifact: `src-tauri/target/release/bundle/appimage/MikroTitan_0.2.0_amd64.AppImage`
  - Size: 171,211,256 bytes (163.28 MiB)
  - SHA-256: `11268eab87f9806a0cda3cc75a43f6b779b0b2bd5745b9048bd3385186ec589b`
  - Bundle checks: the desktop entry reports `Name=MikroTitan`, the running app's window title is **MikroTitan**, the bundled icon and `.DirIcon` match `src-tauri/icons/128x128.png` and `src-tauri/icons/128x128@2x.png`, and `usr/share/licenses/mikrotitan/LICENSE` plus `usr/share/doc/mikrotitan/THIRD_PARTY_NOTICES.md` match the repository files byte-for-byte. No `studio-for-janas` paths remain. No Janas binaries are bundled, and the WebKit media framework used by microphone capture is included.
- **Screenshots:** regenerated against the 0.2.0 build with the new sidebar mark and the **MikroTitan** assistant reply heading, covering the per-chat draft/MCP badge, the agent run trace, and the Tools scope drawer.
- `npm run check` / `npm run build` — TypeScript typecheck and production build passed for 0.2.0.
- `npm test` — 81 Vitest tests pass across 6 files: persistent-store handling, RAG citations and budgets, context budgeting, chat-session normalization/branching, artifacts, and MCP scope/reconciliation.
- `cargo test` — 249 tests pass, 0 failed, 2 ignored: the local two-target benchmark that needs both engines and models, and the network-dependent live-search smoke test.
- **Tauri 2.12.6 smoke test:** the rebuilt AppImage launched, both engines reached Ready, and the window and chat input stayed responsive with no freeze.
- **Document vault:** Rust tests cover stable chunking, hybrid ranking, incremental re-indexing, restart persistence, collection deletion, source removal, scanned-PDF handling, secret/heavy-directory skipping and index cancellation. Vitest covers `[D#]` linkification, citation lookup and ordering, deleted-collection pruning and retrieval-budget clamping. In the rebuilt AppImage, a collection was created, indexed, attached to a chat, retrieved as `[D1]` with the Docs row and source drawer, and the agent's `search_knowledge_base` answer kept its clickable citation after a reload.
- **Voice input:** the AppImage opened the USB microphone as the Pulse/PipeWire default through `parec`, and a stop/transcription run against a virtual system default produced the expected transcript. The fallback was exercised with a PATH containing only `pw-record`; it selected `pw-record`, captured the system-default source, stopped cleanly and produced the same transcript. Closing while recording left no capture process or source-output. Rust tests cover WAV normalisation/resampling, transcript cleanup, language validation and backend preference.
- **Agent resilience:** a scripted engine verified that Stop ends a stalled request immediately, and that a silent stream is ended by the 90 s idle timeout and a silent pre-stream request by the 180 s first-token timeout, each with an actionable error and an unlocked composer.
- **Workspace and approvals:** a deleted workspace produced an error naming the full missing path, the chat pin and saved default could be cleared, and a subsequent run completed without a workspace. The approval-rule store and Hugging Face token/error plumbing are covered by Rust and Vitest suites, including owner-only temporary files, 401/403 distinctions and token redaction.
- **Companions and MCP:** synthetic GGUF v2/v3 headers exercise metadata/array skipping, vocabulary and parameter extraction, projector classification, vision families, exact architecture/vocab draft pairing and bundle validation. llama.cpp argument tests assert draft flags, and repository-tree tests assert `mmproj` splitting and f16 selection. The companion UI was typechecked and bundled, but no interactive Tauri click-through or live Hugging Face/mmproj download was performed. The Tools badge, All/None controls, zero-tools hint and scope reconciliation are covered by typecheck, unit tests and the production build.

### Limitations and caveats

- No Janas binaries or model weights are bundled. Engine setup downloads the current Janas release into the managed `bin` folder, so an offline first run needs a local Janas build selected in Settings.
- Some telemetry is necessarily an estimate: `janas-server` does not expose expert IDs or per-layer residency, so the RAM/disk split and the expert heatmap are labelled estimates. SSD throughput and IOPS come from the kernel; GPU/NPU counters only appear when the driver publishes them under `/sys/class/drm` or `/sys/class/accel`.
- llama.cpp image input needs a vision-capable GGUF plus its matching `--mmproj` projector; the companion manager pairs it from local metadata, and the composer blocks an image send until one is bound. A projector from a different vision family is reported as incompatible instead of being tried at launch. Speculative pairing is deliberately conservative: if a file does not declare both its architecture and vocabulary size, no draft is offered.
- Persistent memory is an in-app hashed TF-IDF vector store, not ChromaDB, so there is no Python sidecar. Facts live in `memory.json` under the app data directory and never leave the machine.
- The document vault lives under `knowledge/` in the app data directory: `collections.json`, plus `collections/<id>/manifest.json` and `index.json.gz` per collection. Files are capped at 4 MiB, a collection at 4,000 files and the vault at 256 collections. Only selectable PDF text is extracted, so scanned PDFs need OCR before indexing. Retrieval uses BM25 and hashed TF-IDF, not neural embeddings.
- The app assumes a single local engine instance and a single active model.
- Chat sessions and their images live under `chat-sessions/` in the app data directory, one JSON file per chat plus `assets/<chat-id>/`, with one previous version kept per chat. Engine/agent preferences, theme choice, the saved default system prompt and the persona library live in `localStorage`; memory facts live in `memory.json`; server settings live in the platform config directory.
- Remembered agent commands live in `agent-approvals.json` in the app data directory, one rule set per canonical workspace, and are restricted to the owner on Unix. They cover shell commands only; MCP tools remain governed by their per-server auto-approve setting. Rules for a workspace that no longer exists stay in the file; delete `agent-approvals.json` to remove them.
- The Hugging Face token is optional and saved in `settings.json` alongside the local API key; both are sent to the webview on settings reads and restricted to the owner on Unix. The token is never written to download manifests, logs or chat history.
- Per-chat MCP scopes store server IDs and names. On chat load, missing servers are pruned and servers re-created under the same name are remapped automatically.
- Janas writes its own cache under `~/.cache/janas`. Converting large models can need roughly three times the model size in free disk space, as documented upstream.
- Only GGUF quantizations supported by the installed converter will compile.
- Voice input is opt-in. The managed `whisper-cli` runtime and curated models are downloaded on demand; on Linux the microphone is the Pulse/PipeWire system default (there is no per-app input picker), and capture needs at least one of `parec` or `pw-record`. Recordings are not persisted as audio; only the resulting transcript is inserted into the draft or chat.
- The AppImage bundles WebKitGTK's media framework so microphone capture works in the packaged app; this is the main reason the artifact is larger than earlier builds.
- The AppImage is unsigned.

## License and attribution

MikroTitan is released under the [GNU General Public License, version 3 only](LICENSE) (`GPL-3.0-only`). The AppImage bundle ships that text at `usr/share/licenses/mikrotitan/LICENSE`, and the bundle metadata points at it through `bundle.licenseFile`. It also ships `usr/share/doc/mikrotitan/THIRD_PARTY_NOTICES.md`, which records the Janas-LLM attribution, copyright and source link.

Janas-LLM is licensed under GPL-3.0-or-later and is not redistributed with this app: engine setup downloads the current release directly from the Janas project. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

MikroTitan is an independent, unofficial project and is not affiliated with, sponsored by, or endorsed by the Janas project or llama.cpp.
