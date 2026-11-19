# Janas Studio

A local AI studio with **agent mode**, branching chat history, per-chat workspaces and MCP tool scopes, crash-safe session storage, and three themes.

Janas Studio is a local AI studio for the [Janas](https://github.com/prabanta-dev/janas) C inference engine, built with **Tauri 2**, **Rust**, **React 18**, **TypeScript**, and **Tailwind CSS**.

Janas Studio manages the `janas-server` process, proxies its OpenAI-compatible SSE stream into the webview, browses GGUF repositories on Hugging Face, and drives `janas-convert` / upstream `gguf2jns` with a live console.

![Janas Studio](src-tauri/icons/128x128@2x.png)

## Highlights

- **Agent mode** — a bounded Think → Act → Observe loop with workspace tools, a live trace, risk-aware approvals, planning, auto-compaction, verification and per-file undo.
- **Branching chats** — edit a prompt or regenerate a reply without losing the old path; switch versions with arrows or branch a new chat from any message.
- **Per-chat context** — drafts, project bundles, workspace roots and MCP tool scopes follow the chat instead of the window.
- **Crash-safe history** — one JSON file per chat, schema v2, atomic writes, automatic previous-version backups, image assets on disk, and export/import/restore.
- **MCP scope controls** — a Tools badge, All/None controls, per-chat server selection, and automatic reconciliation when servers are removed or re-created.
- **Three themes** — Acid, Ember and Tide.

See [CHANGELOG.md](CHANGELOG.md) for the release history.

## Screenshots

Screenshots use a demo workspace and a demo model.

![Chat workspace with branching history, a per-chat draft, and the MCP scope badge](docs/screenshots/chat-workspace.png)

*Chat workspace: branching history, per-chat drafts, and the MCP scope badge.*

![Agent run trace with plan, tool calls, context compaction, and changed files](docs/screenshots/agent-mode.png)

*Agent mode: plan, read/edit/run tool calls, context compaction, and run changes.*

![Per-chat MCP tool scope with All and None controls](docs/screenshots/mcp-scope.png)

*Per-chat MCP scope: All/None controls, enabled servers, and server-level auto-approve.*

## Dual-engine architecture: Janas and llama.cpp

This build adds `llama-server` from `llama.cpp` as a second inference engine next to the experimental Janas streaming engine. The installer deliberately does **not** bundle a llama binary: a Tauri AppImage is mounted read-only under `/tmp/.mount_XXXXXX`, and the release archives differ by CPU, GPU and C runtime. The app downloads, verifies and updates the engine at runtime instead.

### Runtime path strategy

All mutable engine files are resolved through Tauri's `app_local_data_dir()`, never through the resource directory or the executable's folder:

```text
<app_local_data_dir>/bin/
  llama-server                 current verified binary
  llama-server.bak             exactly one previous binary
  libllama.so, libggml*.so     companion shared libraries
  .rollback/llama/             libraries that belong with llama-server.bak
  .staging/<uuid>/             download and extraction workspace
<app_config_dir>/settings.json
```

### Automatic onboarding and provisioning

`src-tauri/src/provision.rs` runs once in the background at startup. It never blocks the window and never writes into the AppImage mount. The startup task:

- Detects Linux/macOS/Windows, x86-64/ARM64, AVX2, Apple Silicon/Metal, NVIDIA CUDA (including the driver's CUDA version), AMD ROCm and Vulkan.
- Resolves the canonical `ggml-org/llama.cpp` repository (formerly `ggerganov/llama.cpp`) from the GitHub Releases API, preferring the latest stable tag. Because the current stable release may only contain `nightly-tag.txt`, it falls back to the newest release that actually contains a matching build and records that fallback in the report.
- Selects CUDA, ROCm, Vulkan, Metal or CPU assets by OS, architecture and backend, then retries the CPU asset if a GPU build is rejected by its startup probe.
- Installs `llama-server` through the same verified downloader, extraction guard, permission and rollback path used by Settings.
- Fetches the pre-built `janas-server` and `janas-chat` tools from `prabanta-dev/janas` when they are missing, installs their shared libraries, and keeps one `.bak` per tool. Existing working managed copies are left unchanged; the bundled Janas tools remain an offline fallback.
- Creates and secures the engine cache (`~/.cache/janas` on Linux, the platform cache equivalent on macOS, and `%LOCALAPPDATA%\janas\cache` on Windows) without following a final-path symlink.

The report is available as JSON through `get_engine_setup_status`, a manual retry is exposed as `rerun_engine_setup`, and progress is emitted on `setup://status`. The Settings panel shows the detected hardware, selected releases, installed binaries, cache path and any fallback warnings.

The supervisor also writes a PID file and reconciles it on startup. A process is only signalled after `/proc/<pid>/cmdline` confirms that it is the expected engine, so a stale PID file can never kill an unrelated process. On Unix engines are spawned with their own process group and stopped with `SIGTERM` (then `SIGKILL`) against that group; a watcher removes the PID file on exit and the app's `RunEvent::Exit` path performs a final synchronous shutdown.

### Rust modules

- `src-tauri/src/engines/mod.rs` — `EngineRunner` trait, `EngineKind`, `EngineSupervisor`, the `tokio::sync::Mutex` state machine, managed-path helpers, process-group cleanup, CLI probing, log forwarding and telemetry.
- `src-tauri/src/engines/llama.rs` — version/help probe, argument adapters for legacy, transitional and modern llama.cpp builds, health/`/metrics` polling, GPU layers, context, Flash Attention, KV cache K/V, Top-K, jinja, metrics and shared-library resolution.
- `src-tauri/src/engines/janas.rs` — wraps the original `EngineManager` without removing its log promotion, health checks or SSE proxy; it prefers `bin/janas-server` when that managed binary exists, and the launch path applies Janas's `JANAS_ATTN` and `JANAS_KV` environment overrides.
- `src-tauri/src/engines/binary.rs` — streaming downloader, ZIP/tar.gz/single-executable extraction with path traversal and size guards, `0o755` permissions, one-step backup, post-install probe, automatic restore on failure, manual rollback and managed-binary probe.
- `src-tauri/src/provision.rs` — startup hardware detection, GitHub release/asset selection, Janas multi-binary provisioning, cache preparation and the JSON setup report.

The trait surface is intentionally identical for both engines:

```rust
#[async_trait]
pub trait EngineRunner: Send + Sync {
    async fn probe(&self, app: &AppHandle, settings: &AppSettings) -> AppResult<EngineProbe>;
    async fn spawn_process(&self, app: &AppHandle, settings: &AppSettings) -> AppResult<EngineLaunch>;
    async fn kill_process(&self, app: &AppHandle, launch: &EngineLaunch) -> AppResult<()>;
    async fn monitor_telemetry(&self, app: &AppHandle, launch: EngineLaunch) -> AppResult<()>;
}
```

`EngineSupervisor` serializes every switch, stops the currently active engine and waits for it to release the hardware before it starts the other one. Starting Janas stops llama.cpp and vice versa.

### Version probing and CLI adapters

Before launch, the backend asynchronously runs `{binary} --version` and `{binary} --help`. `parse_build`, `first_version_line` and the `advertises` helpers select a flag layout from what the binary actually reports. If a build advertises an unknown layout, the app still launches with the safest common flags and emits `engine://adapter-warning`; the panel shows the warning instead of failing silently. Examples of adapted flags include `--flash-attn [on|off|auto]`, `--cache-type-k/v`, `--ctx-size` versus `--ctx`, and Janas's optional SSD streaming flags.

#### Vulkan KV-cache guard

llama.cpp's Vulkan backend cannot schedule the KV cache of a sliding-window (hybrid) model while that cache lives in a GPU buffer. Builds after b12236 abort inside the scheduler before the server binds its port:

```text
ggml-backend.cpp:1358: pre-allocated tensor (cache_k_l1 (view)) in a buffer (Vulkan0) that cannot run the operation (SET_ROWS)
```

The process dies with `SIGABRT`, which the app only sees as an immediate exit. Upstream issue #29082 tracks the regression. The probe therefore also runs `--list-devices` (skipped when the build does not advertise it), and the launch adapter falls back to CPU execution (`--device none`) when all of these hold: the build advertises `-nkvo`, a Vulkan device is available, GPU layers are requested, the build is newer than b12236, and the selected GGUF declares `<architecture>.attention.sliding_window`.

`-nkvo` is not a free substitute here: it leaves attention on the CPU while the weights stay on the GPU. Measured on a Radeon 660M iGPU with a 4 B Q5_K_M sliding-window model, that split produced 6.7 tok/s against 14.2 tok/s for a full CPU launch and 17.1 tok/s for b12236 with GPU KV offload, so a CPU launch is the safer automatic default. The substitution emits an `engine://adapter-warning` that names the issue and both overrides: `-nkvo` in **Extra llama arguments** keeps the weights on the GPU with a host KV cache (better when the model is larger than RAM), and `-kvo` forces GPU KV offload back on. Any explicit `--device`, `-nkvo` or `-kvo` in the extra arguments disables the fallback. Full-attention models, CPU-only launches, CUDA/ROCm/Metal hosts and b12236 and older are untouched.

### Updates, backup and rollback

`download_and_extract_binary(engine_type, download_url)` accepts only `https://` URLs (HTTP is allowed for loopback test servers), streams progress on `engine://binary-progress`, and rejects archives that contain absolute paths, parent traversal, symlinks, too many entries or more than 8 GiB extracted. It stages the download under `bin/.staging`, installs companion libraries, sets `0o755`, renames the current binary to `[binary_name].bak`, and runs the new binary's probe. Release archives express SONAME aliases such as `libllama.so.0` as symlinks; safe extraction skips those links, so the installer materializes the aliases as regular library files before probing. A failed probe restores both the `.bak` binary and its library snapshot automatically. `rollback_binary(engine_type)` performs the same verified swap in reverse; the UI exposes both actions in Settings.

### Commands and events

| Command | Purpose |
| --- | --- |
| `start_engine` / `stop_engine` | Start or stop the preferred engine under the supervisor. |
| `switch_engine(engine)` | `"janas"`, `"llama"` or `"none"`; performs mutual exclusion. |
| `get_engine_status` / `get_active_engine` | Current snapshot and active engine metadata. |
| `download_and_extract_binary(engine_type, download_url)` | Install or update a managed binary. |
| `rollback_binary(engine_type)` | Restore the single `.bak` and its libraries. |
| `probe_managed_binary(engine_type)` | Probe the installed binary without launching it. |
| `get_engine_setup_status` | Return the latest hardware/provisioning report as JSON. |
| `rerun_engine_setup` | Re-run detection and provisioning (forced update/retry). |

| Event | Payload |
| --- | --- |
| `engine://status` | `EngineSnapshot` for the status pill. |
| `engine://active` | `ActiveEngineInfo` or `null`. |
| `engine://log` | Streamed stdout/stderr lines. |
| `engine://telemetry` | Tokens/s, KV usage, SSD read throughput/IOPS and RSS. |
| `engine://adapter-warning` | Unknown CLI layout warning with version and adapter name. |
| `engine://binary-progress` | Download/extract/install phase and percentage. |
| `engine://exited` | Process exited; the UI refreshes the snapshot. |
| `setup://status` | Current `SetupReport` during startup or a manual retry. |

The existing OpenAI-compatible `/v1/chat/completions` SSE proxy is reused for both engines. It now accepts a `top_k` integer in the request payload and routes to the active engine's host and port instead of assuming Janas is running on the settings port.

### AI settings panel

The chat's Engine Settings panel has an explicit Janas / llama.cpp switch. The Top-K slider ranges from 1 to 100 (step 1, default 40) and sits next to Temperature and Top-P with live numeric feedback. With llama.cpp active, the panel exposes `--n-gpu-layers` capped to the selected GGUF's block count, context size, Flash Attention and KV cache K/V quantization, plus llama tokens/s, KV usage and RSS. It also has a llama-only **Direct CPU MoE Compute** toggle and a **Max CPU compute threads** field. The toggle enables llama.cpp's PR #30966 path with `--cpu-moe`, a 2 GiB `--moe-cache-mib` default, and `--moe-cache-cpu-share 1.0`; the thread value is passed as `--threads` only while the toggle is on. These are launch arguments scoped to the llama-server child, never Janas settings or `janas-server` flags. With Janas active, the panel hides the GPU controls and exposes Flash attention (`JANAS_ATTN`: auto, exact or fast), KV cache quantization (`JANAS_KV`: auto, 8-bit or 16-bit), SSD streaming, an optional SSD cache directory, and live SSD read/IOPS/KV telemetry. Janas reads those two settings from its environment rather than accepting llama.cpp's `--flash-attn` and `--cache-type-k/v` flags. Model path, optional `--mmproj` vision projector for image input, llama port, binary URL, install, rollback and probe actions live in Settings. The llama section already has an **Extra llama arguments** box parsed with shell-word rules; it is the place to override the default MoE cache size or thread count.

The Sampling block is capability-aware. On mount and whenever the active engine changes readiness, `get_backend_capabilities` probes loopback-only `/props`, `/v1/config`, `/v1/capabilities` and `/v1/models` with short timeouts. llama.cpp's generation settings are read strictly; Janas model/capability objects and `sampling_params`/`supported_parameters` lists are merged over safe defaults. Missing or null parameters are false. Today the bundled Janas build exposes no sampling capability metadata, so the fallback hides Min-P while keeping Temperature, Top-P, Top-K, Repeat penalty and Max reply visible. If a later Janas build exposes those keys, the same UI unlocks them without an app update. A dependency-free DOM controller toggles `.hidden-param` on `[data-param]`; `.sampling-stack` uses flex gap so hidden controls leave no residual margin or broken grid rhythm.

### Optional build-time sidecar declaration

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

## This build adds

### Agent mode

The composer's **Agent** toggle turns a chat into a bounded tool-running loop. Instead of one completion, the model plans, calls tools, reads observations and continues until it finishes, hits the step limit or is stopped. The run is shown inline as a trace attached to the reply.

- Built-in workspace tools: `read_file`, `write_file`, `edit_file`, `list_directory`, `search_files` and `run_command`. `web_search` is exposed only when the Internet toggle is on; enabled MCP tools in the chat's scope join the same tool list.
- **Workspace root:** file, search and shell tools stay disabled until a folder is chosen. A run pins that folder and cannot switch while it is active or has pending undo state. Each chat can override the global workspace, and `AGENTS.md` or `.janas/instructions.md` in the workspace is injected into the agent prompt.
- **Approval policies:** *destructive* (read-only tools run automatically; writes, shell and MCP ask), *all* (everything except reads asks), or *full auto*. Irreversible commands (force-push, hard reset, recursive delete, publishing, `curl | sh`) and sensitive paths (`.env`, `.git`, SSH keys, cloud credentials) always ask, even under full auto. Tool output is scrubbed for likely secrets before it reaches the trace or model.
- **File-edit shortcut:** approving a `write_file` or `edit_file` with “allow file edits for this run” skips later file-edit prompts for that run; shell and MCP calls remain gated.
- **Diff previews:** file-edit approvals show a bounded diff with added and removed line counts before you approve or reject.
- **Planning and limits:** an optional `<plan>` checklist before the first tool call, a 1–25 iteration cap, optional auto-compaction at a configurable share of the context window, and an optional verification command that runs after edits and before the agent may finish.
- **Trace:** plan, thoughts, each tool call with its risk and duration, approval cards, compaction notices, final status and changed files. The trace is stored with the chat message.
- **Undo:** workspace checkpoints keep bounded pre-images for a whole-run undo or per-file restore/keep. A run with pending changes locks the workspace root until those changes are undone or kept.
- **Broad model support:** engines with native tool calling use it directly; models without a tool template get a prompt-mode tool catalogue and fenced-JSON protocol. Tool schemas are budgeted against the active context window.
- **Safety:** paths resolve inside the pinned workspace, symlink escapes are rejected, commands run in their own process group and are killed on timeout or abort, and the approval matrix is covered by Rust tests.

### Chat workspace

- **Chat sessions rail** (left, collapsible) with multiple chats, search, rename, pinning, per-chat deletion, per-chat import/export, and a **Memory** tab.
- **Rust-backed chat store (schema v2):** each chat is one JSON file under the app data directory, with images extracted to `assets/<chat-id>/`. Saves are atomic and keep one previous version per chat. Settings → Chat history and backups exposes size stats, whole-shelf export/import, restore of the previous version, and orphaned-image cleanup.
- **Branching and version history:** editing a user turn or regenerating a reply preserves the old suffix as an archived branch. Previous/next arrows switch sibling versions; **Branch** creates a new chat from the selected message's prefix. Branches inherit the source chat's project, workspace and MCP scope but not its draft.
- **Per-chat drafts and context:** composer text and pending images are saved per chat and restored after restart. Attached projects, workspace roots and MCP server scopes are also per chat, while sampling settings remain global. A debounced save plus close-time flush keeps pending edits from being lost when the window closes.
- **Token-aware context budget**: every send reserves space for the reply, keeps the system prompt and current turn, trims attached project/web context first, then drops or truncates the oldest turns until the prompt fits the **context the running engine was actually launched with**, not an edited setting that has not been restarted. If the current message and system prompt alone cannot fit, the send is stopped before it is added to the transcript, and the input stays editable. The Rust proxy is also a safety net: if either server still returns HTTP 400 with its context size, the prompt is rebuilt around the current turn and retried once automatically. MCP tool definitions count as prompt input too; when an enabled server's schema cannot fit, the turn runs without those tools and the app explains why instead of sending an impossible request.
- **Engine Settings** (right, collapsible): temperature, top-p, top-k, min-p, repeat penalty, max reply, thinking mode, structured JSON output, context-prefetch window, LRU/LFU eviction, and a system prompt — all applied per request. Sampling controls the active engine does not advertise are hidden at runtime. Server runtime flags are edited here too: `--ctx`, `--cache`, `--mtp` / `--no-mtp`, draft model, `--prompt-on` / `--reply-on` / `--drafts-on`, `--npu-int8`, `--mode`, plus Janas's `JANAS_ATTN` and `JANAS_KV` overrides, with an explicit restart action. When llama.cpp is active, the panel also has the llama-only Direct CPU MoE Compute toggle, `--cpu-moe` / `--moe-cache-mib` / `--moe-cache-cpu-share` launch pipeline, and `--threads` cap; those values never reach Janas. A trash button in the header restores the sampling, context and runtime defaults and clears the editable system prompt; Settings also has a Reset defaults action that loads the AppSettings defaults into the form for review before Save changes.
- **System Telemetry** (bottom, collapsible): a separate **prompt-read** and **reply-write** token ticker, SSD read throughput and IOPS sampled from the engine's `/proc/<pid>/io`, RSS/CPU, GPU/NPU counters from sysfs when the driver exposes them, an estimated RAM-vs-disk layer split, an expert-routing heatmap, and a 64 MB storage benchmark that warns when a drive will bottleneck 48 GB or 70 B+ mixtures.
- **Composer**: a context-window ring next to Send, image attachments with a patch-token estimate, drag-and-drop project ingestion, and an Internet toggle.
- **Internet pipeline**: DuckDuckGo (with a Bing fallback) → top three pages fetched and converted to text → bundled with the prompt as numbered `[S1]` evidence. A live ticker reports each stage, and the reply carries clickable source badges that open in the system browser.
- **Persistent memory**: the model can call its `save_to_memory_bank` tool to store durable facts in a Rust-managed JSON bank on disk. Facts are recalled by local vector similarity, injected into the next relevant turn, and can be added, corrected, or forgotten from the Memory tab. The system prompt tells the model when to save and forbids storing secrets.
- **Streaming resilience**: the Rust SSE proxy tolerates CRLF, split chunks, raw newline-delimited JSON, malformed frames, final chunks without a newline, reasoning aliases, and content arrays. Malformed chunks are counted instead of crashing the app, and the chat view is wrapped in a render boundary so one bad reply cannot blank the window.
- **Project ingestion**: drop a folder on the window (or pick it) and the studio walks the tree, skips build/vendor noise, and builds a semantic bundle with a token estimate before sending it to the prefill layer.
- **Message actions** under every prompt and reply: copy, edit and resend, delete, branch, and previous/next version arrows for sibling replies.

### Models and tools

- **Download pause/resume** in the download dialog and the tray; pausing keeps the stream open and resume continues from the same byte.
- **RAM/VRAM estimate** and destination preview for every quantization before download.
- **Model Library** view: local `.jns`/`.gguf` files with architecture, parameter count, publisher, size and quantization, plus one-click activation. Thinking and Tools badges come from a GGUF chat template when present, otherwise from the model family/name; the badge tooltip says which source was used.
- **Integrity checks and cleanup:** verify any local model against the SHA-256 recorded in the download manifest, with a clear result when no upstream checksum was recorded. Delete a model with an awaited confirmation; the action is blocked while that file is the active model.
- **MCP Server Hub**: register stdio servers with arguments, per-server environment variables and an optional working directory. Probes allow 30 seconds for startup, capture stderr and report early exits. Enabled servers' tools are namespaced into the chat model's tool list, executed through the same stdio session during the turn, and shown in the activity drawer. Per-server auto-approve skips the approval card for normal chat tool calls.
- **Per-chat MCP tool scope:** the Tools drawer shows an All/None/count badge, a zero-tools warning, and checkboxes for the enabled servers. An empty selection stores `[]` and sends no MCP tools; leaving the scope untouched means all enabled servers. Scopes are applied to both normal and agent requests. On chat load, servers that no longer exist are pruned and servers re-created under the same name are remapped to their new ID.
- **Bundled binaries**: `janas-server`, `gguf2jns` and `janas-mcp` ship as Tauri resources, so the AppImage works without pointing Settings at an external build (a binary on `PATH` or an explicit path still wins).

### Appearance, settings and history

- **Themes:** Acid (lime/graphite), Ember (copper/soot) and Tide (cyan/deep water), selectable in Settings and persisted locally.
- **Agent configuration:** max iterations, approval policy, workspace root, planning step, auto-compaction threshold and verification command live in the Engine Settings panel.
- **Chat history and backups:** live size statistics, per-chat previous versions with restore, whole-shelf export/import, and orphaned-image cleanup.
- **Reset defaults:** the Engine Settings trash action restores sampling, context and runtime defaults and clears the editable system prompt; Settings also previews AppSettings defaults before saving.

## What is included

### Rust process and environment manager

- `src-tauri/src/engine.rs` — spawns `janas-server` with the selected `.jns` model, host, port, name, optional API key, and extra arguments. Publishes the four engine states over `engine://status`:
  - `Disconnected`
  - `Indexing`
  - `LoadingModel`
  - `Ready` (confirmed by polling `GET /health`)
- Streams stdout/stderr to `engine://log` and promotes state from log lines. Stops the server gracefully with `SIGTERM` (or `kill` on Windows), waits six seconds, then force-kills.
- Proxies `POST /v1/chat/completions` with `stream: true`, parses SSE in Rust, and emits `chat://delta`, `chat://done`, and `chat://error`. This avoids CORS and keeps the local engine bound to loopback.
- Runs a bounded tool loop for `save_to_memory_bank`: streamed `tool_calls` are reassembled by index, validated, executed against the on-disk memory bank, and returned to the model for a follow-up reply. Malformed tool arguments become a normal tool error the model can correct instead of terminating the stream.
- Supports cancellation per request, including dropping the HTTP stream promptly.
- `src-tauri/src/converter.rs` — launches the converter with `--input <gguf> --output <jns>`, or positional arguments when the binary is upstream's `gguf2jns`. Tracks stdout/stderr, parses percentages, emits `convert://log`, `convert://progress`, `convert://started`, and `convert://finished`, and supports cancel.
- On app exit, kills any child processes it owns.

### Chat workspace

- Global system prompt, persisted locally.
- Temperature (0.0–2.0) and Top-P (0.0–1.0) sliders included in every request payload.
- Live status pill for all four engine states.
- Streaming markdown chat with reasoning blocks, copy actions, stop generation, and token/timing stats.
- Auto-restarts the engine when you switch the active `.jns` model.

### Hugging Face explorer

- Live search against `https://huggingface.co/api/models`, with a GGUF-only filter and download/likes metadata.
- Enriches results by reading each repository's tree API, showing real GGUF quantizations, file counts, and byte sizes.
- Download dialog picks a quantization, shows destination paths, and streams to disk with aggregate progress.
- Downloads run in Rust, are cancellable, and emit `download://progress`.

### GGUF → JNS compiler

- Drag-and-drop or native file picker for `.gguf` files.
- Output path picker, overwrite guard, and destination directory creation.
- Dedicated console with timestamped stdout/stderr, error highlighting, copy/clear, percentage progress, elapsed time, and output size.
- On success, "Use this model in Chat" saves it as the active model.

### Settings

- Engine and converter binary paths with a `--version` probe.
- Active `.jns` model, models folder, server host/port, extra arguments, and local API key.
- Scan for local `.jns` models and select one.
- Theme picker (Acid, Ember, Tide), agent preferences, and reset-defaults actions.
- Chat history statistics, whole-shelf backup/export/import, previous-version restore, and orphaned-image cleanup.

## Requirements

- Linux (x86-64) for the AppImage build.
- Rust 1.77+ and Node 18+.
- WebKitGTK 4.1 / GTK3 development packages:

```bash
sudo apt install build-essential libwebkit2gtk-4.1-dev libjavascriptcoregtk-4.1-dev \
  libsoup-3.0-dev libgtk-3-dev librsvg2-dev libssl-dev patchelf libfuse2
```

- A local Janas build. Upstream's release tarball provides `janas-server`, `gguf2jns`, `jns_planes`, and `janas-chat`:

```bash
curl -LO https://github.com/prabanta-dev/janas/releases/latest/download/janas-linux-x86_64.tar.gz
tar xf janas-linux-x86_64.tar.gz
```

The studio looks for `janas-server` and `janas-convert` on `PATH`, or at the absolute paths in **Settings**. If the converter name is left as `janas-convert` and it is not found, the studio also tries upstream's `gguf2jns`. Upstream currently documents `gguf2jns` and `jns_planes` as the conversion tools; `janas-convert` is supported as the studio's requested interface.

> Upstream Janas is an early, experimental engine whose CLI and API change without notice. Verify flags against the release you install. Point the studio at a server that implements `POST /v1/chat/completions` and `GET /health`, which is the contract used here.

## Development

```bash
npm install
npm run tauri dev
```

The Vite dev server runs on `http://localhost:1420`; the Rust backend owns the window and the engine processes.

### Dual-engine integration harness

The mock-runtime harness uses Tauri's `MockRuntime` and compiles a dependency-free fake server into a temporary managed bin directory as both `llama-server` and `janas-server`. It starts llama.cpp, switches to Janas through the real `EngineManager`, switches back to llama.cpp, and exercises process-group shutdown, log forwarding, `/health` readiness, `/metrics` telemetry and active-engine events without a model, GPU or external service.

```bash
./scripts/run-dual-engine-harness.sh
```

The failed-update test in `src-tauri/src/engines/binary.rs` installs a deliberately silent binary, verifies that it fails the probe, and asserts that the previous binary and executable permissions are restored.

## Build an AppImage

```bash
npm run appimage
```

The artifact is written to:

```
src-tauri/target/release/bundle/appimage/Janas Studio_0.1.0_amd64.AppImage
```

Run it with `chmod +x` and execute directly. The image bundles its WebKitGTK/GTK runtime libraries (verified with `ldd` on the extracted payload); a graphical Linux session with working display and GPU drivers is still required.

## Architecture

```
src/
  types.ts                 shared IPC and UI types
  lib/api.ts               typed invoke wrappers + event names
  lib/chatSessions.ts      session normalization, branching, versions, drafts
  lib/mcpScope.ts          per-chat MCP filtering, request inputs, reconciliation
  hooks/                   engine, settings, chat, agent, downloads, converter
  components/chat/         workspace, messages, composer, agent trace, MCP drawer, sessions rail
  components/models/       marketplace, library, download dialog/tray
  components/mcp/          server hub
  components/converter/    compiler form and console
  components/settings/     runtime, theme, and chat-history panels
src-tauri/src/
  main.rs                  Tauri setup, state, command registration
  engine.rs                Janas lifecycle, SSE proxy and tool loop
  agent.rs                 agent loop, workspace tools, approvals and safety
  agent/checkpoint.rs      per-run file pre-images and undo state
  engines/                 dual-engine supervisor, Janas/llama adapters, binary installer
  chat_store.rs            schema-v2 chat sessions, assets, backups, export/import
  mcp.rs                   stdio MCP client/runtime and probes
  provision.rs             startup hardware detection and engine provisioning
  converter.rs             janas-convert job runner
  huggingface.rs           Hub search, quant discovery, downloads
  capabilities.rs          runtime sampling-capability probing
  settings.rs              persisted config, binary resolution, probing
  memory.rs                persistent memory bank + save_to_memory_bank handler
  system.rs                telemetry, benchmark, ingest, web search, library, model verify/delete, MCP, source opener
  error.rs                 serializable command errors
```

New UI pieces: `chat/SessionsRail`, `chat/EnginePanel`, `chat/TelemetryPanel`,
`chat/TokenTicker`, `chat/Composer` (multimodal), `chat/AgentTrace`,
`chat/McpLogDrawer`, `models/ModelLibraryView`, `mcp/McpView`,
`settings/ThemePicker`, and `settings/ChatHistoryPanel`.

### IPC/event contract

| Command | Purpose |
| --- | --- |
| `start_engine`, `stop_engine`, `get_engine_status` | process lifecycle |
| `stream_chat`, `cancel_chat` | SSE proxy and cancellation |
| `start_conversion`, `cancel_conversion` | converter lifecycle |
| `search_models`, `list_model_quants` | Hugging Face metadata |
| `start_download`, `cancel_download`, `pause_download`, `resume_download` | downloads and pause/resume |
| `get_settings`, `save_settings`, `probe_binary`, `scan_local_models` | configuration |
| `get_telemetry`, `benchmark_storage` | hardware sampling and drive test |
| `ingest_project`, `web_search`, `transcribe_audio` | project, web and speech pipelines |
| `save_to_memory_bank`, `memory_list`, `memory_update`, `memory_delete`, `memory_clear` | persistent memory bank |
| `open_external` | open a citation in the system browser |
| `library_models`, `mcp_probe` | local model shelf with thinking/tool badges and MCP handshake with stderr/exit diagnostics |
| `get_backend_capabilities` | dynamic sampling-control availability from the active engine |
| `chat_sessions_list`, `chat_session_save`, `chat_session_delete`, `chat_asset_data_url` | schema-v2 session store and image assets |
| `chat_export_session`, `chat_import_session`, `chat_branch_session`, `chat_export_all`, `chat_import_all`, `chat_backup_list`, `chat_restore_backup`, `chat_store_gc`, `chat_store_stats` | branching, backup, export/import and maintenance |
| `verify_local_model`, `delete_local_model` | SHA-256 verification and model deletion |
| `agent_start`, `agent_resolve_approval`, `agent_abort` | agent run, approval decisions and cancellation |
| `agent_undo`, `agent_undo_file`, `agent_keep_file`, `agent_undo_availability`, `agent_undo_state` | per-run and per-file agent undo |

| Event | Payload |
| --- | --- |
| `engine://status` | full `EngineSnapshot` |
| `engine://log` | stream, line, timestamp |
| `chat://delta` / `chat://done` / `chat://error` | streaming reply lifecycle |
| `memory://changed` | the full memory list after a model or user write |
| `convert://log` / `convert://progress` / `convert://finished` | build console |
| `download://progress` | aggregate download status |
| `chat://notice` / `chat://tool-approval` | context/tool notices and MCP approval requests |
| `mcp://activity` | MCP handshake and tool activity |
| `agent:plan` / `agent:thought` / `agent:tool_start` / `agent:tool_result` | agent plan, live reasoning and tool steps |
| `agent:approval_needed` / `agent:context_compacted` / `agent:done` / `agent:error` / `agent:notice` | agent approvals, compaction and completion |

## Verification performed

- `npm run check` — TypeScript typecheck passed.
- `npm test` — 23 Vitest tests pass across chat-session normalization/branching and MCP scope/reconciliation, including empty-scope request building and persistence-boundary checks.
- `cargo test` — 143 tests pass, 0 failed; one network-dependent live-search smoke test is ignored by default.
- `npm run appimage` — release build and AppImage bundling completed:
  - Artifact: `src-tauri/target/release/bundle/appimage/Janas Studio_0.1.0_amd64.AppImage`
  - Size: 90,397,176 bytes (86.21 MiB)
  - SHA-256: `79988fe824edcc2d6791f4d02c87d43b11884953609300ee32e2cb76780378a9`
- Runtime passes in an isolated profile exercised branching and version switching, per-chat drafts and MCP scope, backup restore and export/import, close-time saving, and model verify/delete. The delete confirmation now awaits the Tauri dialog, and window close flushes pending chat writes before destroying the window.
- The Tools badge, All/None controls, zero-tools hint and scope reconciliation are covered by typecheck, unit tests and the production build; the final AppImage was not visually rechecked for these last UI additions.
- Engine-specific checks from earlier builds (llama.cpp Vulkan KV-cache guard, context retry, MCP schema budget, bundled binaries) remain covered by the Rust suite.

## Notes and limitations

- The Janas binaries are bundled in the AppImage under `binaries/`; the `.jns` model weights are still yours to download.
- Some telemetry is necessarily an estimate: `janas-server` does not expose expert IDs or per-layer residency, so the RAM/disk split and the expert heatmap are labelled estimates. SSD throughput and IOPS come from the kernel; GPU/NPU counters only appear when the driver publishes them under `/sys/class/drm` or `/sys/class/accel`.
- llama.cpp image input needs a vision-capable GGUF plus its matching `--mmproj` projector selected in Settings; otherwise the engine's error is shown verbatim.
- Persistent memory is an in-app hashed TF-IDF vector store, not ChromaDB, so there is no Python sidecar. Facts live in `memory.json` under the app data directory and never leave the machine.
- The app assumes a single local engine instance and a single active model.
- Chat sessions and their images live under `chat-sessions/` in the app data directory, one JSON file per chat plus `assets/<chat-id>/`, with one previous version kept per chat. Engine/agent preferences, theme choice and other UI state live in `localStorage`; memory facts live in `memory.json`; server settings live in the platform config directory.
- Per-chat MCP scopes store server IDs and names. On chat load, missing servers are pruned and servers re-created under the same name are remapped automatically.
- Janas writes its own cache under `~/.cache/janas`. Converting large models can need roughly three times the model size in free disk space, as documented upstream.
- Only GGUF quantizations supported by the installed converter will compile.
- The AppImage is unsigned.
