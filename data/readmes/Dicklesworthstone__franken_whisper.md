# franken_whisper

<div align="center">
  <img src="https://raw.githubusercontent.com/Dicklesworthstone/franken_whisper/main/franken_whisper_illustration.webp" alt="franken_whisper — agent-first Rust ASR orchestration stack">
</div>

<div align="center">

[![License: MIT+Rider](https://img.shields.io/badge/License-MIT%2BOpenAI%2FAnthropic%20Rider-blue.svg)](./LICENSE)
[![Rust Edition](https://img.shields.io/badge/Rust-2024_Edition-orange.svg)](https://doc.rust-lang.org/edition-guide/rust-2024/)
[![unsafe audited](https://img.shields.io/badge/unsafe-audited-success.svg)](https://github.com/rust-secure-code/safety-dance/)
[![Latest Release](https://img.shields.io/github/v/release/Dicklesworthstone/franken_whisper.svg)](https://github.com/Dicklesworthstone/franken_whisper/releases)

</div>

**Agent-first Rust ASR stack with a real in-process pure-Rust Whisper engine (no FFI, no Python, no subprocess), adaptive Bayesian backend routing, real-time NDJSON streaming (true-live mic/pipe streaming via `fw robot listen`; batch robot mode streams sequenced stage events), DTW word timestamps, and SQLite-backed run history. In current live-incumbent, same-invocation matched-greedy CPU comparisons, the native large-v3-turbo engine is 2.99× faster than whisper.cpp on a 124.5-second whole job; tiny.en is 1.52× faster on a 124.5-second transcribe-only workload and 1.51× faster on a 300-second transcribe-only workload. These ratios were measured with the int8 encoder, which is now opt-in (`FW_ENC_ATTN_OUT_I8I32=1`); the default f32 encoder is slower (turbo whole job 1.38× in a same-binary A/B).**

<div align="center">
<h3>Install in one line</h3>

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/franken_whisper/main/install.sh?$(date +%s)" | bash
```

<sub>SHA-256-verified prebuilt binaries for <b>Linux</b> (x86_64 / aarch64), <b>macOS</b> (Intel / Apple&nbsp;Silicon), and <b>WSL</b> — proxy-aware, airgap-capable (<code>--offline</code>), reversible (<code>--uninstall</code>). Windows users: grab <code>windows_amd64.zip</code> from the newest <code>vX.Y.Z</code> release on <a href="https://github.com/Dicklesworthstone/franken_whisper/releases">the releases page</a> (model packages are published as releases too). All flags: <a href="#installation">Installation</a>.</sub>

</div>

## Agent quickstart

The release installs two equivalent binary names: `fw` is the concise
agent-facing name, and `franken_whisper` remains the descriptive name. Start
with the live triage payload instead of scraping help text:

```bash
fw --version
fw robot triage
fw capabilities --json
fw models --json
fw pull all --json
fw doctor --json
fw robot schema
fw robot listen --list-devices   # live streaming capture check
```

`fw robot run --input AUDIO --backend auto` streams NDJSON. Robot syntax
errors are also emitted as one path-safe JSON object on stdout with exit code
2; runtime failures use one of the 13 exact `FW-*` codes published by
`fw capabilities --json`. Discovery, inference, and doctor commands do not
download models. `fw pull all` is the explicit in-binary network path for the
native defaults. It streams the 1,624,555,275-byte Whisper package and the
separately licensed 491,570,584-byte Sortformer package into the per-user cache,
then admits each only after its compiled size and SHA-256 trust roots pass. The
installer runs that command by default. A doctor `ready` result means both
packages passed static preflight; the payload still sets
`operationally_verified: false` until an actual transcription succeeds. The
model weights are never stored in Git. Whisper is distributed as the
`whisper-large-v3-turbo-f16-v1` release artifact; its GGML f16 bytes are
identity-preserved from the pinned upstream revision and selected for the native
Rust loader and optimized FrankenTorch kernels. Sortformer is distributed as
`sortformer-v2.1-f32-v1` beside the NVIDIA Open Model License, required notice,
and deterministic conversion receipt.
Release archives also carry [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md),
which records the licensed libc++ selection logic translated into safe Rust for
the pinned PyTorch CPU top-k parity contract.

> **The native engine is real, fast, and benchmarked at matched decode settings.** The in-process pure-Rust Whisper engine (built on [FrankenTorch](https://github.com/Dicklesworthstone/frankentorch) kernels) is compared below against the actual `whisper-cli` incumbent, side-by-side in one harness invocation with both engines using greedy decode. The whole-job turbo row's transcript is within **WER 0.025090** of whisper.cpp's (7 edits over 279 words); the tiny.en reference conformance remains **WER 0.0000**. The full measurement record is in [the performance ledger](docs/PERF_LEDGER.md). These rows ran the int8 encoder, the default when they were measured. The default encoder is now f32 because int8 measured more word errors on a 389-utterance corpus ([DISC-010](docs/planning/DISCREPANCIES.md)); `FW_ENC_ATTN_OUT_I8I32=1` selects the encoder those rows measured. The default's incumbent ratios have not been re-certified.
>
> | Model / workload | Mode | Matched-greedy result |
> |---|---|---|
> | large-v3-turbo, 124.5 s / 5 windows | whole job, no timestamps | **2.99× faster** |
> | tiny.en, 124.5 s / 5 windows | transcribe only, no timestamps | **1.52× faster** |
> | tiny.en, 300 s / 10 windows | transcribe only, no timestamps | **1.51× faster** |

---

## The Problem

Speech-to-text pipelines are fragmented. Existing stacks combine `whisper.cpp` for speed, `insanely-fast-whisper` for GPU batching, and Python diarization systems for speaker attribution. Each has its own CLI, output format, error handling, and deployment story. Orchestrating them from scripts means parsing inconsistent stdout, handling timeouts manually, killing zombie subprocesses, and losing all run history when something crashes.

Agent workflows make the problem worse. Modern LLM agents need **structured**, **streaming**, **machine-readable** output, not human-oriented terminal decorations that break the moment they touch `jq`, pipes, or SSH.

## The Solution

`franken_whisper` is a single Rust binary that wraps every major Whisper backend behind a unified, agent-first interface — and ships its own engine:

- **A real in-process Whisper engine, in pure Rust.** ggml model parsing, log-mel frontend, encoder/decoder transformer inference on FrankenTorch CPU kernels, greedy decoding with whisper.cpp's full timestamp-rule suite, and cross-attention DTW word timestamps. No FFI, no Python, no subprocess — drop a ggml model file in place and transcribe.
- **Rust-native Sortformer speaker diarization by default.** The in-process fused model emits anonymous activity lanes and overlapping turns for up to four speakers, then projects that independent timeline onto Whisper segments. It remains development-uncertified: four lanes are a hard capacity boundary, not proof that a recording has no additional speakers. Known intervals and requests beyond that capacity use the bounded acoustic path, which is an available but uncertified fallback. Explicit ECAPA modes remain available for experiments with pinned speaker embeddings. None of these modes claims gender or biometric identity.
- **Adaptive Bayesian backend routing.** Each `auto` request runs a formal decision contract with an explicit loss matrix, per-backend Beta posteriors, Brier-scored calibration, and deterministic fallback when the model is mis-calibrated.
- **Real-time NDJSON streaming.** Every pipeline stage emits sequenced, timestamped events on stable schema `v1.1.0` (the 1.0.0 contract plus the additive listen-event family). No fragile regex; agents parse JSON.
- **Durable run history.** Every transcription persists to SQLite with full event logs, replay envelopes, and JSONL export/import, even when the process crashes mid-run.
- **Cooperative cancellation.** Ctrl+C propagates through the pipeline via
  cancellation tokens. Owned subprocess trees are terminated and verified,
  transactions roll back via savepoints, and finalizers run within a bounded
  budget. Cleanup failures are reported instead of being relabeled as clean
  cancellation.
- **No external decoder for common audio.** MP3, AAC, FLAC, WAV, OGG,
  Vorbis, and ALAC decode in-process via `symphonia`. `ffmpeg` is a fallback
  for video and exotic codecs, and is auto-provisioned on Linux x86_64 if
  missing.
- **Native engine rollout governance.** In-process Rust replacements follow a 5-stage rollout (Shadow → Validated → Fallback → Primary → Sole). The shipped default is `Sole`, so bridges run only after an explicit operator opt-out or rollout override.
- **TTY audio transport.** Compressed audio (mu-law + zlib + base64) over PTY links with handshake, integrity hashes, deterministic retransmission, and an adaptive bitrate controller. A transcript-streaming control-frame vocabulary (protocol v2) is defined with library emitters and parsers; no CLI command yet streams a live transcription over the link (handshakes still negotiate v1).
- **Word-level timestamps.** First-class support via `whisper.cpp`'s word-timestamp pipeline, with the cancellation token threaded into the inner extraction loop.

### Why franken_whisper?

| Feature | whisper.cpp | insanely-fast-whisper | whisper-diarization | **franken_whisper** |
|---------|:-----------:|:---------------------:|:-------------------:|:-------------------:|
| Streaming output | partial | — | — | **sequenced NDJSON stage events** |
| Machine-readable errors | exit code only | exceptions | exceptions | **13 exact `FW-*` error codes** |
| Adaptive backend selection | — | — | — | **Bayesian decision contract** |
| Run persistence | — | — | — | **SQLite + JSONL replay packs** |
| Diarization | TinyDiarize hints | yes (HF token) | yes | **native Sortformer default + Rust acoustic fallback + explicit ECAPA** |
| Compute acceleration | CUDA / Metal | CUDA / MPS | CUDA | **FrankenTorch CPU kernels + automatic Metal on macOS** |
| Cancellation | `SIGKILL` | `KeyboardInterrupt` | `SIGKILL` | **cooperative `CancellationToken`** |
| TTY audio relay | — | — | — | **mulaw + zlib + base64 NDJSON** |
| Native audio decode | WAV only | needs ffmpeg | needs ffmpeg | **MP3 / AAC / FLAC / WAV / OGG / ALAC** |
| Memory-safety boundary | C++ | Python | Python | **safe Rust with explicitly scoped, audited native kernels** |

---

## Quick Example

```bash
# Native Whisper transcription plus native Sortformer diarization is the default.
# MP3 / FLAC / OGG / AAC are decoded in process; no ffmpeg is needed.
franken_whisper transcribe --input meeting.mp3 --json

# Skip diarization when only a transcript is needed.
franken_whisper transcribe --input meeting.mp3 --no-diarize --json

# Transcribe a video file. Audio extracted automatically via ffmpeg fallback.
franken_whisper transcribe --input presentation.mp4 --json

# Stream real-time pipeline events for agents
franken_whisper robot run --input meeting.mp3 --backend auto

# Speculative streaming: fast partial transcripts with quality-model corrections
franken_whisper robot run --input meeting.mp3 --speculative \
  --fast-model tiny.en --quality-model large-v3

# Select the built-in acoustic fallback explicitly (no Python or HF token)
franken_whisper transcribe --input meeting.mp3 \
  --diarization-engine acoustic --json

# Explicit ECAPA identity fused with bounded acoustic channel evidence
# (requires the pinned local ECAPA package, but no Python or HF token)
franken_whisper transcribe --input meeting.mp3 \
  --diarization-engine ecapa-fused --json

# TinyDiarize: whisper.cpp's built-in speaker-turn detection (no HF token needed)
franken_whisper transcribe --input meeting.mp3 --tiny-diarize --json

# Discover available backends and their capabilities
franken_whisper robot backends

# System health check (backends, ffmpeg, database, resources)
franken_whisper robot health

# Query run history
franken_whisper runs --limit 10 --format json

# Export run history to a portable JSONL snapshot (full or incremental)
franken_whisper sync export-jsonl --output ./snapshot

# Compressed audio over a text-only channel (PTY, SSH, serial)
franken_whisper tty-audio encode --input audio.wav > frames.ndjson
cat frames.ndjson | franken_whisper tty-audio decode --output restored.wav
```

---

## Design Philosophy

### Agent-First, Human-Optional

The primary interface is `robot`. Every command in robot mode emits sequenced, timestamped NDJSON on stdout with schema version `1.1.0` (bumped additively from `1.0.0` when the listen event family landed; batch events are unchanged). Human-friendly output (`transcribe` without `--json`) is the exception. Robot mode never mixes decorative stderr into the data stream; structured `run_error` envelopes replace human prose even for argument-parsing failures.

### Deterministic by Default

Given identical inputs and parameters, `franken_whisper` produces identical outputs. The TTY retransmit loop, replay envelopes, replay packs, and conformance harness all enforce determinism. Random elements (UUIDs, wall-clock timestamps) are quarantined to metadata fields; they never enter computational output.

### Fail Loud, Recover Gracefully

Every error has a structured code (`FW-IO`, `FW-CMD-TIMEOUT`, `FW-BACKEND-UNAVAILABLE`, `FW-STAGE-TIMEOUT`, …) and propagates through the NDJSON event stream. Cancellation tokens let in-flight work checkpoint and clean up instead of dying mid-write. In-progress SQLite transactions roll back via savepoints; owned subprocess trees are terminated and checked; temporary resources are handled by registered finalizers under a bounded budget.

### Composition Over Configuration

The pipeline is **composed** dynamically per request. The 10 canonical stages (Ingest, Normalize, VAD, Source Separate, Backend, Accelerate, Align, Punctuate, Diarize, Persist) are skipped when unnecessary, budgeted independently, and profiled automatically. The `PipelineBuilder` validates ordering at build time; runtime never hits "stage X requires stage Y" errors.

### Audited Unsafe Boundaries

The crate uses `#![deny(unsafe_code)]`. Native-engine SIMD and
fully-overwritten-buffer kernels opt in at explicit sites with local safety
arguments; unannotated unsafe code is rejected. The performance rationale and
measurements are retained in
[`docs/NEGATIVE_EVIDENCE.md`](docs/NEGATIVE_EVIDENCE.md).

### No External Decoder for Common Audio

`franken_whisper` decodes MP3, AAC, FLAC, WAV, OGG (Vorbis), and ALAC entirely in-process via `symphonia`; no `ffmpeg`, no Python, no `PATH` lookup. `ffmpeg` is only invoked as a fallback for video files, exotic codecs (AC3, DTS, Opus-in-MKV), and live microphone capture. When `ffmpeg` *is* needed and missing on Linux x86_64, it is downloaded once into the per-user state directory.

### Adaptive Controllers With Conservative Fallbacks

Every adaptive controller in the system (the backend router, the speculative window controller, the budget tuner, the TTY adaptive bitrate controller, the correction tracker) ships with an explicit *alien-artifact engineering contract*: state space, action space, loss matrix, posterior, calibration metric, deterministic fallback, and an evidence ledger. When models drift, the system **falls back to a deterministic policy** rather than confidently making bad decisions.

---

## The Whisper Ecosystem Landscape

```
          +--------------------------------------------------------------+
          |            INFERENCE ENGINES (run the model)                 |
          |                                                              |
          | whisper.cpp           (C++, CPU/Metal/CUDA)                  |
          | faster-whisper        (Python/CTranslate2)                   |
          | OpenAI Whisper        (Python/PyTorch)                       |
          +--------------------------------------------------------------+
                                         |
          +------------------------------v-------------------------------+
          |     ENHANCED PIPELINES (add features on top)                 |
          |                                                              |
          | WhisperX               (faster-whisper + wav2vec2 + pyannote)|
          | whisper-diarization    (Whisper + Demucs + NeMo TitaNet)     |
          | insanely-fast-whisper  (HuggingFace Transformers, max GPU)   |
          | whisper-timestamped    (DTW word timestamps)                 |
          +--------------------------------------------------------------+
                                         |
          +------------------------------v-------------------------------+
          | ORCHESTRATION (manage engines/pipelines)                     |
          |                                                              |
          | > franken_whisper <    (Rust, Bayesian routing,              |
          |                         10-stage pipeline, conformance       |
          |                         gating, native engine rollout,       |
          |                         evidence-based decisions)            |
          +--------------------------------------------------------------+
```

Most tools occupy one level. `franken_whisper` is the orchestration layer: it wraps inference engines and enhanced pipelines behind a unified interface, then adds capabilities none of them provide individually.

---

## How franken_whisper Compares

### Orchestration & Architecture

| Capability | whisper.cpp | faster-whisper | WhisperX | WhisperLive | WhisperS2T | **franken_whisper** |
|------------|:-----------:|:--------------:|:--------:|:-----------:|:----------:|:-------------------:|
| Language | C++ | Python | Python | Python | Python | **Rust** |
| Multi-backend | — | — | — | 3 | 4 | **3 bridge families + native counterparts** |
| Backend selection | — | — | — | manual | manual | **Bayesian decision contract** |
| Pipeline stages | monolithic | monolithic | 3 | monolithic | monolithic | **10 composable stages** |
| Per-stage budgets | — | — | — | — | — | **independent timeouts + auto profiling** |
| Speculative streaming | — | — | — | single-model | — | **dual-model fast+quality with retraction** |
| Conformance validation | — | — | — | — | — | **cross-engine, 50 ms tolerance, drift detection** |
| Native rollout governance | — | — | — | — | — | **5-stage Shadow → Sole with conformance gates** |
| Memory-safety boundary | C++ | Python GC | Python GC | Python GC | Python GC | **safe Rust with explicitly scoped, audited native kernels** |

### Persistence & Observability

| Capability | whisper.cpp | faster-whisper | WhisperX | WhisperLive | **franken_whisper** |
|------------|:-----------:|:--------------:|:--------:|:-----------:|:-------------------:|
| Run history | — | — | — | — | **SQLite WAL + JSONL export/import** |
| Decision audit trail | — | — | — | — | **200-entry evidence ledger** |
| Replay envelopes | — | — | — | — | **SHA-256 content + output hashes** |
| Replay packs | — | — | — | — | **4-artifact deterministic reproducibility bundle** |
| Structured errors | exit code | exceptions | exceptions | — | **13 exact terminal `FW-*` codes** |
| NDJSON streaming | partial | — | — | WebSocket | **sequenced stage events** |
| Cancellation | `SIGKILL` | `KeyboardInterrupt` | — | — | **cooperative `CancellationToken`** |
| Resource cleanup | none guaranteed | GC | GC | GC | **RAII + bounded LIFO finalizers** |
| Latency profiling | — | — | — | — | **per-stage utilization with tuning recommendations** |

### Audio & Format Support

| Capability | whisper.cpp | faster-whisper | WhisperX | **franken_whisper** |
|------------|:-----------:|:--------------:|:--------:|:-------------------:|
| Native audio decode | WAV only | needs ffmpeg | needs ffmpeg | **MP3 / AAC / FLAC / WAV / OGG / Vorbis / ALAC via `symphonia`** |
| ffmpeg required? | for non-WAV | always | always | **fallback only (video + exotic codecs + mic)** |
| Video audio extraction | — | — | — | **automatic via `-vn`** |
| TTY audio transport | — | — | — | **mulaw + zlib + base64 NDJSON** |
| Microphone capture | — | — | — | **cpal (CoreAudio/ALSA/WASAPI) with ffmpeg fallback** |
| Auto-provisioned ffmpeg | — | — | — | **downloads static binary if missing (Linux x86_64)** |

### Commercial API Comparison

| Capability | Groq Whisper API | Deepgram Nova-3 | AssemblyAI | **franken_whisper** |
|------------|:----------------:|:---------------:|:----------:|:-------------------:|
| Runs locally | no | no | no | **yes** |
| Open source | no | no | no | **yes (MIT + rider)** |
| Data leaves machine | yes | yes | yes | **never by core; external tools are explicit and operator-controlled** |
| Billing model | usage-priced | usage-priced | usage-priced | **local compute only** |
| Inference speed | very fast | fast | moderate | **depends on selected backend** |
| Multi-model routing | — | — | — | **Bayesian adaptive** |
| Diarization | limited | yes | yes | **native Sortformer default, acoustic fallback, explicit ECAPA/external routes** |
| Custom pipeline stages | — | — | — | **10 composable stages** |

---

## Installation

### Quick Install (Pre-built Binary)

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/franken_whisper/main/install.sh?$(date +%s)" | bash
```

The installer downloads the release asset for the detected platform, verifies
its SHA-256 checksum, validates the staged binary's self-reported version, and
installs both `fw` and `franken_whisper` to `~/.local/bin`. It then downloads
and verifies the pinned native Whisper and Sortformer packages (about 2.12 GB
combined). Interactive installs show a `Y/n` prompt with **Yes** as the default;
quiet and headless installs provision automatically. `--no-pull` is the explicit
opt-out. An offline install accepts a preseeded verified cache or requires
`--no-pull`; it never contacts the network. Under `sudo ... --system`, model
provisioning drops back to the validated invoking user so the packages do not
land in root's private cache. A release download failure never silently falls
back to a source build; use `--from-source` explicitly. Before a fresh model
pull, the installer requires at least 2.4 GB free on the cache filesystem; an
already-complete cache is admitted after both compiled trust roots are verified.

Options:

| Flag | Purpose |
|------|---------|
| `--system` | Install to `/usr/local/bin` instead of `~/.local/bin` |
| `--easy-mode` | Auto-update shell `PATH` and rc files |
| `--verify` | Verify both binary names, agent schemas, and both native model packages |
| `--no-pull` | Skip automatic native Whisper and Sortformer model provisioning |
| `--version vX.Y.Z` | Pin to a specific release |
| `--force` | Reinstall even if the same version is present |
| `--offline TARBALL` | Airgap install from a local archive (verifies sibling `.sha256`) |
| `--from-source` | Build from a source clone (clones sibling FrankenSuite deps) |
| `--quiet` / `--no-gum` | Script-friendly / plain-ANSI output |
| `--no-verify` | Skip checksum verification (testing only) |
| `--uninstall` | Remove both binary names and installer-added `PATH` lines |

`HTTP_PROXY`/`HTTPS_PROXY` are honored on every download.
`FW_INSTALL_PROMPT_TIMEOUT` changes the interactive prompt timeout from 120
seconds, and `FRANKEN_WHISPER_MODEL_DIR` selects an absolute cache root shared
by `fw pull all`, model discovery, and the installer. Prebuilt targets are
`linux_amd64`, `linux_arm64`, `darwin_amd64`, `darwin_arm64`, and
`windows_amd64` (zip; manual install on native Windows).

### Homebrew

```bash
brew install dicklesworthstone/tap/franken-whisper
fw pull all
```

Homebrew installs both binary names but does not bundle model weights. The
second command downloads the same SHA-256-pinned native Whisper and Sortformer
packages used by the installer. Model inference remains offline after that
one-time provisioning step.

### From Source

```bash
git clone https://github.com/Dicklesworthstone/franken_whisper.git
cd franken_whisper

# Provision the exact clean sibling commits used by release builds.
# Existing mismatched sibling directories are never modified.
scripts/prepare_release_siblings.sh

# default CLI and library
cargo build --locked --release --bins

# with TUI support
cargo build --release --features tui
```

The native engine always uses FrankenTorch CPU kernels. On macOS, large eligible
matrix operations automatically use the target-gated Metal kernel when a Metal
device is available; `FRANKEN_WHISPER_GPU=0` forces CPU execution. The only
production Cargo feature is `tui`; `fj-oracle` enables a test-only FrankenJAX
differential oracle and is not a runtime acceleration backend. The release
profile uses `opt-level = 3`, full LTO, one codegen unit, `panic = "abort"`, and
stripped symbols.

### Prerequisites

- **Rust nightly for source builds** (2024 edition; pinned via `rust-toolchain.toml`).
- **ALSA on Linux.** Version 0.10.0 adds native microphone capture through CPAL. Both Linux executables require the ALSA runtime library `libasound.so.2` at startup, including for file transcription. Install your distribution's ALSA runtime package before using a prebuilt release; source builds also require the ALSA development headers and `pkg-config`. The installer validates both executable names before replacing an existing installation and reports this prerequisite if executable validation fails.
- **ffmpeg** (optional): needed for video files, exotic codecs `symphonia` cannot decode, batch `transcribe --mic`, and as the fallback live-capture backend when cpal cannot open the device. On Linux x86_64 it is auto-provisioned on first use unless `FRANKEN_WHISPER_AUTO_PROVISION_FFMPEG=0`.
- **The two native default model packages.** The installer provisions them, or run `fw pull all`. Native Whisper uses the pinned `whisper-large-v3-turbo-f16-v1` GGML f16 release; native diarization uses the pinned four-lane `sortformer-v2.1-f32-v1` package. Both are hash-checked against compiled trust roots. No external backend binary is required for the default pipeline. The native engine's ggml parser accepts f32 and f16 `.bin` models (`hparams.ftype` 0/1); quantized ggml variants are rejected today and remain on the roadmap (see [`docs/PERF_LEDGER.md`](docs/PERF_LEDGER.md) for the measured f16 frontier).
- **The pinned ECAPA package** (only for `ecapa` or `ecapa-fused`): `ecapa_tdnn_voxceleb.safetensors`, SHA-256 `9276a840c52cdd2e9afb73cd87a38e15749e12bf494d3ca47b5bc162f237cbcc`, under `$FRANKEN_WHISPER_MODEL_DIR/aux/` or `~/.cache/franken_whisper/models/aux/`. The converted artifact is not published, so `scripts/fetch_aux_models.sh` prints the pinned conversion instructions and expected digest instead of downloading it.
- **Bridge backend binaries** (optional explicit alternates):
  - `whisper-cli` (from whisper.cpp); override via `FRANKEN_WHISPER_WHISPER_CPP_BIN`
  - `insanely-fast-whisper` (Python entry point); override via `FRANKEN_WHISPER_INSANELY_FAST_BIN`
  - `python3` with `pyannote.audio` installed (only for the optional external diarization backend); override via `FRANKEN_WHISPER_PYTHON_BIN`
- **HuggingFace token** (external diarization only): `--hf-token`, `FRANKEN_WHISPER_HF_TOKEN`, or `HF_TOKEN`. Native acoustic and ECAPA diarization need neither Python nor a token; the ECAPA modes do require the local package above.

### Sibling Crate Dependencies

`franken_whisper` integrates several crates from the FrankenSuite ecosystem.
Published packages resolve them from **crates.io**. A source checkout uses
versioned path dependencies for the exact local FrankenSQLite, FrankenTorch,
FrankenTTS, optional FrankenTUI, and optional FrankenJAX sources;
`scripts/prepare_release_siblings.sh` stages
the release-pinned sibling commits without modifying an existing mismatched
checkout.

| Crate | Source | Purpose |
|-------|--------|---------|
| `asupersync` | crates.io `=0.5.0` | Cancel-correct orchestration primitives |
| `franken-kernel` | crates.io `=0.5.0` | Budget, TraceId, time utilities |
| `franken-evidence` | crates.io `=0.5.0` | Evidence ledger primitives |
| `franken-decision` | crates.io `=0.5.0` | Decision contract framework |
| `fsqlite` / `fsqlite-types` | crates.io `^0.4.0`; source path `../frankensqlite` | Pure-Rust SQLite persistence and value types |
| `ft-core` / `ft-kernel-cpu` | crates.io `0.1.0`; source path `../frankentorch` | Required tensor types and native Whisper CPU kernels |
| `ft-kernel-metal` *(macOS)* | crates.io `0.1.0`; source path `../frankentorch` | Automatic Metal compute for eligible large operations |
| `ftts-kernels` | crates.io `0.1`; source path `../frankentts` | Required FastEnhancer-S denoising kernels |
| `ftui` *(feature: `tui`)* | crates.io `0.7.0`; source path `../frankentui` | Optional terminal UI framework |
| `fj-lax` / `fj-core` *(feature: `fj-oracle`)* | source path `../frankenjax` | Independent differential oracle for native-kernel conformance tests (seeded, 1e-4 tolerance; see [docs/conformance-contract.md](docs/conformance-contract.md)) |

---

## Quick Start

### 1. Basic Transcription

```bash
# one "[HH:MM:SS.mmm --> HH:MM:SS.mmm]  [SPEAKER_00] text" line per segment
# (plain text with --no-timestamps)
franken_whisper transcribe --input audio.mp3

# full JSON report (segments + timing + backend identity + replay envelope)
franken_whisper transcribe --input audio.mp3 --json

# explicit backend
franken_whisper transcribe --input audio.mp3 --backend whisper-cpp --json

# language hint
franken_whisper transcribe --input audio.mp3 --language ja --json
```

### 2. Robot Mode (Agent Integration)

```bash
franken_whisper robot run --input audio.mp3 --backend auto
```

Output (one JSON object per line, schema `1.1.0`):

```json
{"event":"run_start","schema_version":"1.1.0","request":{"input":"audio.mp3","backend":"auto"}}
{"event":"stage","schema_version":"1.1.0","run_id":"...","seq":1,"ts":"2026-07-28T00:00:00Z","stage":"ingest","code":"ingest.start","message":"materializing input","payload":{}}
{"event":"stage","schema_version":"1.1.0","run_id":"...","seq":2,"ts":"2026-07-28T00:00:01Z","stage":"normalize","code":"normalize.ok","message":"audio normalized","payload":{}}
{"event":"stage","schema_version":"1.1.0","run_id":"...","seq":3,"ts":"2026-07-28T00:00:02Z","stage":"backend","code":"backend.routing.decision_contract","message":"routing decision","payload":{"chosen_action":"try_whisper_cpp"}}
{"event":"run_complete","schema_version":"1.1.0","run_id":"...","trace_id":"...","started_at":"2026-07-28T00:00:00Z","finished_at":"2026-07-28T00:00:03Z","backend":"whisper_cpp","language":"en","transcript":"Hello world...","segments":[],"acceleration":null,"diarization":null,"warnings":[],"evidence":[]}
```

### 3. Speaker Diarization

```bash
franken_whisper transcribe --input meeting.mp3 --json
```

The default path runs the native four-lane Sortformer package and returns
anonymous `SPEAKER_NN` turns. It is fast, in-process, and development-
uncertified: a lane count is not a calibrated estimate of the true number of
speakers, and recordings with more than four speakers exceed the model's
capacity. Use `--no-diarize` for transcription only.

Turn evidence is fused into the transcript (`projection-fusion-v1`): every
segment that overlaps a labeled turn gets that speaker, segments in short turn
gaps take the nearest labeled turn within 2 seconds, and word-level speaker
changes snap to the nearest sentence-final punctuation within four words so
turn-initial words land on the speaker who says them. The result also carries
`diarization.speaker_segments`, a merged view of consecutive same-speaker runs
with joined text and duration-weighted turn confidence, so consumers do not
rebuild the turn/segment join. Untimed segments and audio beyond the gap bound
stay `speaker: null`. Requests with known
intervals or count constraints beyond the four-lane boundary fall back to the
native acoustic engine under the default `acoustic` fallback policy.

On this project's Apple M4 Pro development host, a repeated-public-audio
ten-minute probe took 35.86 seconds end to end for Sortformer (29.91 seconds of
model inference, inference RTF 0.04984). That scales to about 3.6 minutes of
diarization per audio hour when one model load is included. The matched native
Whisper probe took about 9.0 minutes per audio hour, for roughly 12.6 minutes
combined. This is a throughput orientation row, not a natural-conversation
accuracy result or a promise for other hardware.

Omitting all count options means inference intent. Acoustic and ECAPA reports
contain a versioned `speaker_count.estimate` object and retain explicit
uncalibrated/unresolved mass. A soft preference can be added with
`--speaker-count-range 2..5` or
`--speaker-count-prior 2=0.25,3=0.75`. Use
`--speaker-count-hard 3` only when the caller intentionally wants a hard search
constraint; it never fabricates occupancy or removes UNKNOWN. Soft count
options are supported by the native acoustic, `ecapa`, and `ecapa-fused`
engines; external backends reject them rather than silently hardening them.

Known intervals can enroll an opaque speaker reference without retaining the
hint document's source path or raw source bytes:

```json
{"schema_version":"speaker-hints-v1","known_intervals":[
  {"speaker_ref":"caller_a","start_ms":1200,"end_ms":5400,
   "confidence":0.98,"policy":"hard_must_link"}
]}
```

Pass it with `--speaker-hints /private/path/hints.json`. Hard intervals are
immutable must-links; soft enrollment can be rejected when acoustically
contradictory. Parsed hint fields are part of the typed request and are
persisted with the run unless `--no-persist` is used. Labels remain within-run
references, not biometric identities.

When `known_intervals` is nonempty, execution rejects both an external engine
and `--diarization-fallback external`: external labels cannot enforce immutable
hint identities, so this combination fails closed instead of discarding them.

Evaluation uses the frozen `diarization-scorer-v5` contract. In addition to
DER/JER, it reports typed speaker-count evidence with explicit authority,
unresolved and zero-probability outcomes, effective occupancy,
dominant/reference collapse, phantom labels, and optional transcript-free
aligned-word WDER. Fixed-safe results are explicitly uncalibrated, and current
probabilistic results are development-uncertified; neither is described as a
calibrated posterior unless a future certified authority says so.
This prevents a nominally correct label count from hiding a run where one
label received nearly all speech. Public ablations aggregate these metrics by
reference count and duration; `diarization-eval` emits the same evidence only
as a path-free, aggregate-only confidential result. Aligned-word inputs retain
opaque non-lexical IDs and timing/speaker annotations, never token text. See
[`docs/acoustic_diarization_contract.md`](docs/acoustic_diarization_contract.md)
for the versioned schemas and fail-closed policy.

The multiscale acoustic sidecar is exposed only through the separate public
evaluation command `diarization-corpus sidecar-study`, using
`public-diarization-acoustic-sidecar-study-v6` and its v8 runner. It is not a
`transcribe` option: normal segmentation, clustering, robot output,
persistence, and the normal transcription route are not mutated by the
sidecar study. This is a routing guarantee, not a claim that current reports
are byte-identical to historical acoustic-v2 reports. The command runs a
frozen full-v2 baseline plus twelve ordered sidecar lanes, retains only
aggregate path-free and transcript-free evidence, and creates both outputs in
external directories on Linux, Android, and Apple platforms. Other targets
return `public_corpus.output_platform` before corpus materialization. On a
successful supported-platform run, stdout bytes exactly match the retained
study evidence file.

The frozen protocol uses oracle VAD speech regions while leaving speaker count
in inferred mode. Its DER/JER and speaker-count results therefore measure
segmentation and clustering conditioned on reference speech activity; they are
not end-to-end VAD-accuracy evidence.

Development fits separate adjacent-boundary and lagged different-speaker
calibrations. The boundary-fusion-v2 configuration hash binds the selected change-detector
mode as well as the sidecar/calibration and selector constants, so materially
different fallback and peak-selection behavior cannot share an identity.
Conditional diagnostics begin with one lane-independent universe
of uniquely reference-labeled 25/50/100/200-frame-lag pairs. Each recording
retains at most 4,096 members by a score-, label-, and availability-independent
selection-key-v3 SHA-256 over normalized clipped PCM identity, frame indices,
and lag. The pair scorer is separately protocol-bound and is not part of that
key. A reference-labeled selected-sequence-v2 digest binds every retained key,
frame pair, lag, and same/different label and must match across evaluated lanes. Evidence
retains aggregate selected/scored same/different counts, overall and per-class
score coverage, recording support, linked reliability moments, and a 100-bin
score-order histogram; it retains no selected keys, labels, frame indices, or
probabilities. The producer bins exact clamped-`f32` scores. The verifier checks
linked counts, class moments, and first/second-moment feasibility against each
bin's exact clamped-`f32` support, which rejects direct aggregate
contradictions. Because the individual selected probabilities are
intentionally omitted, those sufficient statistics cannot establish every
member's bin assignment or replay score ordering; they are aggregate internal-
consistency evidence, not member-level provenance. Promotion requires at least
0.25 total and per-class score coverage, 100 scored pairs and five recordings in each class, pair
discrimination/calibration bounds, and substantial owner-specific same-speaker
auxiliary-dominance evidence wherever Voice and that owner coexist.

A completed study is not an automatic promotion. The artifact records whether
each candidate was rejected, advanced for held-out certification, or adopted,
and no lane has such authority until a real public-corpus result establishes
it. When any lane is accuracy-eligible, development ranks one winner first; if
that lane fails an operational bound, no lower-ranked lane advances. RTF and
RSS are host-dependent observations against the live unfused baseline in the
same invocation; passing them is not a speed or memory-win claim. The
deterministic accuracy projection removes performance-only failures and
`NotSelectedByRanking`, zeros timing/RSS, allocator capacities, and target-sized
retained-state bytes, and clears certification's locked development result hash
while retaining its accuracy hash before recomputing selection/adoption.

The verifier recomputes aggregate metrics, fine/coarse score-distribution
consistency, coverages, gates, ranking, dispositions, and hashes. It validates
calibration fingerprints and fit-count provenance, but aggregate evidence
cannot prove each omitted probability's histogram membership, refit
calibrations, regenerate selected pairs, replay audio-derived metrics, or
reproduce bootstrap intervals; verification proves aggregate internal
consistency, not member-level provenance or corpus replay. Paired intervals use a fixed versioned
lane/split seed and a cancellable SplitMix64 stream. Reference annotations use
a monotonic overlap-aware sweep instead of rescanning all turns every 10 ms.

The library's `adversarial_corpus` module supplies a Rust-native, public-safe
accuracy harness without checking audio fixtures into the repository. It
generates transcript-free harmonic calls with deterministic speaker, turn,
overlap, pitch, playback, and stereo regimes, then applies bounded gain,
muffling, band-limit, resampling, quantization, clipping, noise, reverb,
interruption, silence, channel-shift, playback, channel-swap, and overlap
recipes. Retained repro seeds contain parameters, stable classifications, and
content hashes—not samples, paths, transcripts, embeddings, or real speaker
identifiers. Plans declare synthetic source authority or bind a hash of an
external public-license acknowledgement. The same API attributes the first
divergent pipeline stage and delta-minimizes a failing transform sequence while
preserving its exact classification.

For development-only differential diagnosis, `diarization-oracle` can compare
the native stage document with an operator-installed pyannote, NeMo spectral,
VBx, EEND, DiaPer, or Sortformer adapter. Start with
`franken_whisper diarization-oracle registry`, then run the selected adapter
against absolute external audio and stage-document paths. Comparisons are
separate for speech activity, opaque word timing, change boundaries,
label-permutation-invariant clusters, overlap, and final projection. Missing
or failing tools produce a path-free skipped report; disagreements are
diagnostic only and can never certify that the native path is wrong. External
tools remain optional subprocesses with no normal runtime or Cargo dependency.
The Sortformer entry is narrower than the generic adapters: it pins
[`nvidia/diar_streaming_sortformer_4spk-v2.1`](https://huggingface.co/nvidia/diar_streaming_sortformer_4spk-v2.1)
at immutable revision `fafaab5faa1617a0ca52d38dd3dc4bd636800d3d`, requires
canonical mono 16 kHz PCM16 WAV input, and freezes the documented high-latency
340/40/40/300/188 streaming-cache profile plus untuned 0.5/0.5 post-processing.
The `300` value is the configured cache-update period. Pinned NeMo only warns
when it is shorter than the 340-frame chunk; its FIFO update computes
`min(max(configured, chunk - fifo_capacity + current_fifo), current_fifo + chunk)`.
That moves 300 frames on the first full chunk and 340 in the full-chunk steady
state, while tail chunks remain state-dependent.
The accepted v2 operator adapter fails closed unless installed package metadata
binds NeMo to commit `40ace43c7cf151af78dc22027c02feeca7e06b6a` and the frozen
Python/PyTorch/torchaudio/NumPy versions. It derives BLAS and CPU-feature facts
from the installed runtimes and asserts the raw streaming profile plus the
derived FIFO-pop schedule after NeMo validates it; those facts may not be
supplied by literals alone.
The operator-installed adapter remains an explicit trust boundary. The host
hashes its resolved path before execution, rejects an initial mismatch against
the compiled SHA-256 pin, and rechecks the path after the version probe and
oracle run before validating schema and attestations. This catches ordinary
drift, but a swap-and-restore inside the remaining hash-to-exec window is still
an open oracle-authority gate. Activation-seam capture therefore uses a
separately reviewed exporter and digest; the final-output adapter pin does not
authorize intermediate values.
The first admitted activation pack is synthetic-only: four deterministic
non-human frontend fixtures, 46 F32/I64 tensors, and 44 stage-level replay
observations that are byte-exact across five runs requested in each configured
one-thread and eight-thread regime.
Rust authenticates the separate receipt/package roots and runs the complete f32
graph in process through L8 anonymous speaker turns. The same engine powers the
default pipeline and remains available through a focused diagnostic command:

```bash
fw pull sortformer --json
fw sortformer-diarize --input call.m4a

# Optional caller assertions/suggestions for anonymous-lane mapping:
fw sortformer-diarize --input call.m4a --speaker-hints /private/hints.json
```

The bounded hint file can be a bare interval array or this versioned form:

```json
{
  "schema_version": "speaker-hints-v1",
  "known_intervals": [
    {
      "speaker_ref": "speaker-a",
      "start_ms": 1200,
      "end_ms": 4800,
      "confidence": 1.0,
      "policy": "hard_must_link",
      "provenance": "caller-context"
    }
  ]
}
```

`fw pull` is restartable across verified per-file cache hits, cooperative under
Ctrl+C, and never emits cache paths in JSON mode. The installer invokes
`fw pull all` by default; inference stays offline. Behind a TLS-inspecting
proxy, point `FRANKEN_WHISPER_CA_BUNDLE` (or the conventional `SSL_CERT_FILE`)
at a PEM bundle to add its roots; every artifact stays pinned to its SHA-256
digest and size, so an added root cannot change which bytes are accepted. An
unusable `FRANKEN_WHISPER_CA_BUNDLE` is an error; an unusable `SSL_CERT_FILE`
is logged and ignored. The focused diarization command
rehashes the cached package and conversion receipt, runs completely offline,
and emits one path-free `sortformer-diarization-v1` object with turns, inferred
active-lane count, timing, and the candid capacity status
`four_lane_capped_output_true_speaker_count_unknown`; an inferred lane count is
never presented as proof that the recording contains no additional speakers.
Hard known intervals may bind a
unique anonymous lane to a caller-provided opaque reference; contradictory or
ambiguous hard evidence fails closed. Soft intervals remain non-authoritative
suggestions, every non-hard-bound lane remains anonymous, and inference never
mutates model weights. `--diarization-engine auto` now selects this native
runtime under the owner-directed default. The model registry and focused
diagnostic command report `development_uncertified`. The
authenticated NVIDIA-recommended streaming
truth pack covers four public fixtures and 4,540 L1-L8 tensors. On its complete
102-second three-speaker row, native L5 probabilities stayed within the frozen
envelope (maximum absolute difference `1.072883606e-6`, relative L2
`8.214150678e-8`), and L7 activity plus all 16 L8 turns were byte-exact. The
historical four one-frame boundary differences came from comparing the old
archive-default streaming geometry with the recommended profile, not from a
same-profile Rust/source loss. Same-host L6 tied-selection parity is resolved
by the pinned safe libc++ `nth_element` translation. This is parity evidence,
not broad corpus accuracy, greater-than-four-speaker capacity, cross-platform,
or broad accuracy certification evidence; the registry and focused diagnostic
command therefore report `development_uncertified`. The converted f32 package is
491,570,584 bytes
(SHA-256 `487fa30cb0aa9799c77bd9985e6787962c3991fab8d4d576a4f1221d45298f6a`).
Its distribution policy is `github_release_with_license_and_notice`: weights
remain outside Git and are attached to the dedicated model release with the
license, notice, and authenticated conversion receipt.
The default cache is `~/.cache/franken_whisper/models`; an override through
`FRANKEN_WHISPER_MODEL_DIR` must be absolute. Partially downloaded files retain
hidden staging names for diagnosis and are never admitted as model artifacts.
Speaker-hints JSON must be a bounded regular non-symlink file.
Full proof details and current performance/resource rows are in
[`SORTFORMER_RUST_PORT.md`](docs/SORTFORMER_RUST_PORT.md).
The external Sortformer adapter's version probe must bind the frozen contract
hash, independently verify that
the 471,367,680-byte local artifact hashes to the pinned Hugging Face LFS
SHA-256, and retain a path-free runtime fingerprint. The frozen evaluation row
is CPU-only float32 with autocast and quantization disabled, deterministic
algorithms enabled, zero data-loader workers, eight PyTorch intra-op threads,
and one inter-op thread. Output labels are arrival-ordered `speaker_0` through
`speaker_3`; a reference containing five or more speakers is retained as an
explicit model-capacity skip rather than being dropped or forced into four
labels. The external Python/NeMo oracle remains operator-installed. This is
separate from the native Rust runtime's explicit `fw pull sortformer` cache.
The full adapter protocol, environment overrides, privacy rules, and authority
boundary are in the
[`acoustic diarization contract`](docs/acoustic_diarization_contract.md#114-stage-aware-external-differential-oracles).

ReDimNet2-B2 is a separate compact speaker-embedding experiment, not an
end-to-end diarizer and not an `auto` route. The offline
`scripts/export_redimnet2.py` command accepts the pinned upstream checkpoint,
the exact v1.0.0 source tree, and a new output directory:

```bash
python3 scripts/export_redimnet2.py INPUT.pt SOURCE_ROOT OUTPUT_DIR
```

All three arguments must resolve outside this checkout, `OUTPUT_DIR` must not
exist, and the command performs no download. The exporter installs a Python
audit hook that denies socket and child-process events for the full conversion.
Its exporter and conversion-receipt schemas are v3; the synthetic truth tensor
contract remains v1. It requires Python 3.12.12 with
torch/torchaudio 2.7.1, NumPy 2.2.6, SciPy 1.15.3, and safetensors 0.5.3. It
hash-binds the 15,897,450-byte upstream checkpoint and 14 source files, rejects
every unmanifested regular file, symlink, bytecode file, or native extension in
the executable `redimnet2` package tree, disables bytecode writes, and refuses
preloaded ReDimNet modules. The receipt binds the interpreter binary, Python
implementation/cache tag, distribution RECORD/METADATA digests, and a
path-free commitment after verifying every hashed RECORD entry's bytes. It also
binds the Torch Git/build identity and build-configuration digest. It
drops only 68 scalar batch counters, and writes a metadata-free 15,745,544-byte
f32 package (SHA-256
`d41a729f5ef008d70c6d6bf4ab7ca27e299a478ff665665a4e31afff7f46ddeb`),
an 8,828,392-byte non-human synthetic seam pack (SHA-256
`21042537873c3dacafafd134d7c9e296318458f55f1a429c00bc9542f95f3238`),
and a canonical path-free receipt. Two final hardened v2 exports were
byte-identical; their immutable v2 receipt SHA-256 is
`e4e5aab1838dd386895425acc11e3405191e30ce2111c313c2734bfc2bccd77e`. The
model has 3,677,760 total parameters, of which 3,676,320 are trainable and 1,440
are frozen; its raw 192-vector is retained separately from consumer-side L2
normalization. Every manually captured terminal embedding must equal the real
upstream `forward` output bit-for-bit. Known upstream warnings and the one
pinned initialization message are captured and retained only as path-free
code/count/byte/digest records; any unknown warning or console output fails.
Publication uses a stable destination directory handle with no-follow,
create-exclusive files, inode checks, and
fsync. Those historical v2 receipts remain `operator_local_no_release`; they
are not relabeled by the v3 schema. The immutable v1.0.0 README identifies the
repository's official pretrained weights, links the exact release assets, and
declares MIT. Its source commit and GitHub release record predate the checkpoint
upload, so this is contemporaneous scope evidence rather than a later
retroactive inference. The exporter pins that README at SHA-256
`27d500b510a1cdc054a8ccbad484cf6062639fcb9d6b661714214fe766ed4e76` and
pins the later canonical 1,067-byte MIT payload at commit `2a8d15f65b1d`,
SHA-256 `3d5a4bf9936a7d09dd770588c0d7cb116fc16916a0310d71fb1fff5d64562101`.
Fresh v3 receipts therefore mark license scope resolved while keeping artifacts
`operator_local_pending_release_manifest`. A public raw or converted package
must still carry that exact license payload and notice and be bound by a
separate identity-checked release manifest before it may claim
`github_release_with_license_and_notice`. No ReDimNet weights, truth tensors,
feature values, local paths, audio, transcripts, or biometric vectors belong in
Git or public runtime reports. The historical package, truth, and v2 receipt
hashes above are not evidence that a fresh v3 receipt has been reproduced.

The two explicit Rust-native ECAPA modes run the pinned ECAPA-TDNN speaker
representation in process through the common segmentation, known-speaker
constraints, profile/count machinery, temporal UNKNOWN/overlap handling,
canonical labels, and transcript projection:

- `--diarization-engine ecapa` uses ECAPA embeddings for speaker identity and
  does not add acoustic channel evidence to pair scoring.
- `--diarization-engine ecapa-fused` authorizes ECAPA speaker identity plus
  bounded acoustic channel evidence and consensus. If no selected consensus
  merge joins a compatible pair with valid channel features, it conservatively reports generic consensus
  provenance instead. The library/JSON request spelling is `ecapa_fused`.

Both modes remain outside `auto`, and both are development-uncertified rather
than production-accuracy claims. Neither downloads a model: the exact
converted package must already resolve through the auxiliary model search
path. The library freezes and verifies the
license-compatible source revision, deterministic 200-tensor safetensors
package, exact package hash and metadata, a scalar conformance oracle, public
analytic golden stages, and fail-closed numerical tolerances. The bounded
safe-Rust runtime path implements a fixed-FFT periodic-Hamming PCM frontend,
TDNN/SE-Res2 aggregation, attentive statistics pooling, projection, and
embedding normalization on explicit FrankenTorch CPU kernels, with cooperative
cancellation, content-hash-validated process caching, and content-redacted
diagnostics. The package verifier reuses the native safetensors loader; no
parallel weight format or sidecar manifest is introduced. A
separately authenticated 2,160,320-byte public seven-stage oracle lets the
external conformance test compare all 539,616 frontend and neural `f32` values,
then recheck all 523,456 neural values through the composed Rust frontend, not
only selected checkpoints. Safe RAII logical-buffer leases enforce and report
the preplanned ECAPA-owned logical `f32` scratch-payload bound. Both generated
artifacts remain outside Git. The
project does not vendor weights or parse PyTorch checkpoints at runtime. The
current provider identity is
`ecapa-tdnn-voxceleb-cosine-v6-development`; the current clustering policy is
`acoustic-clustering-probabilistic-v20-channel-evidence-bound-fused-consensus-development`.
Reports distinguish the ECAPA-only `ecapa_spherical` partition from the
channel-aware five-lane `ecapa_fused_consensus` partition. The fused method is
  emitted only after at least one selected consensus merge joins a compatible
  ECAPA pair with valid channel features; otherwise the fused engine conservatively reports
generic `probabilistic_consensus` provenance and is ineligible for the
supported-profile redecode experiment. Cross-mode method claims fail
validation.
Its equal-loss different-speaker boundary is cosine distance `0.80`, and robust
final-assignment and held-out-validation separation begin at the same `0.80`.
Lane consensus and temporal recurrence may require stricter evidence, never a
hidden `0.70` gate. This is a versioned development decision bound, not an
accuracy-certification claim. Tracklets of at least two seconds use disjoint
discovery and held-out validation windows, each capped at three seconds;
shorter admitted tracklets use a discovery window, with sub-half-second input
zero-padded to the runtime minimum. Direct 192-dimensional cosine evidence is
marked development-uncertified;
failed public-development candidates remain negative evidence rather than
rollout authority. See the
[`ECAPA conformance boundary`](docs/acoustic_diarization_contract.md#115-optional-ecapa-model-and-numerical-conformance-boundary).

### 4. Microphone Capture

```bash
# record 30 seconds from the default mic
franken_whisper transcribe --mic --mic-seconds 30 --json

# specific device
franken_whisper transcribe --mic --mic-device "hw:0" --json
```

### 5. Stdin Input

```bash
cat audio.mp3 | franken_whisper transcribe --stdin --json
```

### 6. Batch Transcription (many files, one model load)

Repeat `--input`, or pass `--inputs-from FILE` (one path per line; `-` reads
the list from stdin; lines are taken verbatim, blank lines are skipped, a
leading UTF-8 byte order mark is ignored, and a relative path resolves against
the current directory). One process loads and
authenticates the native models once and runs every input through the normal
pipeline, so each input's result matches a single-input run with the same
flags. (A repeated input is answered from the in-process transcript cache:
same transcript, segments and timings, but its `raw_output.decode_work` retry
counters read 0 because no decode ran.)

```bash
ls narration/*.wav | fw transcribe --inputs-from - --json --no-diarize --no-persist \
  --language en --max-segment-length 1 --split-on-word
```

`--json` prints one NDJSON record per input, in input order:
`{"schema_version":"franken-whisper-batch-result-v1","index":0,"total":2,"input":"a.wav","status":"ok","report":{...}}`,
where `report` is exactly what single-input `fw transcribe --json` prints, or
`"status":"error","error":{"code":"FW-...","message":"..."}`. A failed input
does not stop the batch; the process exits 1 (`FW-BATCH-INCOMPLETE`) if any
input failed. `fw transcribe --json` prints no summary line, so its exit status
is the batch outcome: 0 when every input succeeded, 1 when an input failed or
the whole batch was invalid (then no records are printed and stderr says why),
130 when interrupted; the `FW-BATCH-INCOMPLETE` code itself appears only on the
robot stream below. `--timeout` bounds each input separately, not the batch: an
input that runs past it fails on its own and the next input starts with a fresh
budget (wrap the command in `timeout(1)` for a whole-batch limit). A panic
inside one input's run fails only that input, with `FW-CONTRACT-VIOLATION`, in
both commands, in an unwinding build (debug builds, library use); the shipped
release binary is built with `panic = "abort"`, so there a panic still ends the
process. `fw robot run` accepts the same flags: each input's `run_start`,
`run_complete` and `run_error` carry `"batch":{"index","total","input"}`, and
the stream ends with a `batch.complete` event, which carries
`"code":"FW-BATCH-INCOMPLETE"` when an input failed. Ctrl+C stops the batch
after the running input (which reports `FW-CANCELLED`); the process exits 130
and `batch.complete` says `"status":"cancelled"`, `"code":"FW-CANCELLED"`, even
when the interrupted input was the last one. If the stream's reader goes away,
the first event write that fails (EPIPE) cancels the input in flight: it stops
at its next checkpoint and is not persisted unless its persist stage had
already committed, no later input starts, and the process exits 1. fw notices only when it writes, so a reader that leaves while
a stage is silent (a long backend run) is noticed at that stage's next event.
A batch that is invalid as a whole
(shared flags, an unreadable list) fails before any input runs, like an invalid
single run: `run_start`, then `run_error`, neither tagged with `batch`, and no
`batch.complete`. Agents can feature-detect
this through `fw capabilities --json | jq .batch`. `--stdin`, `--mic`,
`--speaker-hints` and `--transcript-path` apply to one recording and are
rejected in batch mode. `--output-*` files go to `./<input stem>.<ext>` as in
a single run, so a batch that names two different inputs with the same stem
(`day1/part1.wav`, `day2/part1.wav`) is rejected before any work instead of
letting one input's files overwrite the other's. Stems are compared ignoring
case (`Talk.wav` and `talk.mp3` collide: `./Talk.srt` and `./talk.srt` are one
file on the default macOS and Windows file systems), on every OS, so a batch is
accepted or rejected the same way everywhere; one file named twice (`a.wav`,
`./a.wav`) is just a repeated input.

---

## YouTube Ingestion

`franken_whisper youtube run` downloads YouTube audio and transcribes each video into a clean, deep-linked **markdown + JSON** pair. Hand it individual video URLs, playlist URLs (auto-expanded to their videos), or a file of URLs — it downloads, transcribes, and writes one transcript per video into `youtube_transcripts/` (override with `--output-dir`). Because the transcription runs on the same engine as `transcribe`, this pairs naturally with the in-process native engine: **no cloud, no API keys, your audio never leaves the machine.**

```bash
# Single video
franken_whisper youtube run "https://www.youtube.com/watch?v=jNQXAC9IVRw" --model tiny.en

# Several videos at once
franken_whisper youtube run \
  "https://youtu.be/VIDEO_A" \
  "https://youtu.be/VIDEO_B" \
  --concurrency 4

# A whole playlist (expanded to its videos automatically)
franken_whisper youtube run "https://www.youtube.com/playlist?list=PLxxxxxxxx"

# A file with one URL per line (blank lines and #/;/] comments ignored)
franken_whisper youtube run --batch-file urls.txt --output-dir ./talks
```

URLs may be passed positionally or with repeated `--url` flags, and mixed freely with `--batch-file`. A `watch?v=X&list=Y` URL is treated as the **single video** `X`, not the surrounding playlist.

The same command group provides agent-oriented catalog helpers:
`franken_whisper youtube search <QUERY>` emits deduplicated JSON hits, and
`franken_whisper youtube enrich <TARGET>...` resolves full metadata for chosen
URLs or ids. Run each subcommand with `--help` for its focused flags.

### Output

Each video produces a markdown transcript and a JSON sidecar. The default slug style is `{upload_date}_{title}_{id}` with lowercase ASCII title text and an intact, case-preserved YouTube id; `--naming-style pretty` selects the historical `{upload_date} - {title} [{id}]` layout. The downloaded audio is kept under `audio/<id>.<ext>` (delete it automatically with `--no-keep-audio`), and a `.fw_youtube_manifest.json` state file tracks per-video progress.

```
youtube_transcripts/
├── 20050424_me_at_the_zoo_jNQXAC9IVRw.md
├── 20050424_me_at_the_zoo_jNQXAC9IVRw.json
├── audio/
│   └── jNQXAC9IVRw.webm
└── .fw_youtube_manifest.json
```

The **markdown** leads with the title, a metadata line, a source link, and an honesty note, then paragraphs grouped on natural pauses and detected speaker changes. Each paragraph starts with a `youtu.be` deep-link to that moment. Pass `--no-diarize` to omit the speaker stage.

```markdown
# Me at the zoo

**Channel:** jawed · **Uploaded:** 2005-04-24 · **Duration:** 0:19
**Source:** [www.youtube.com/watch?v=jNQXAC9IVRw](https://www.youtube.com/watch?v=jNQXAC9IVRw) · **Transcribed:** franken_whisper 0.2.0 (native, tiny.en)

> Note: machine transcription; timestamps are approximate and deep-link into the video.

---

**[0:00](https://youtu.be/jNQXAC9IVRw?t=0)** All right, so here we are in front of the elephants…

---
_Transcribed by franken_whisper 0.2.0 (native, tiny.en, auto) in 0.48s — RTF 0.025_
```

The **JSON** sidecar carries the structured form — `video` metadata, `run` metadata, native `windows` decode evidence, and a flat `utterances` array (one record per segment with `start_sec` / `end_sec` / `text` / `confidence`, plus `speaker` when diarized). External subprocess backends emit an empty `windows` array; an in-process `native-v2` result must provide the complete typed window contract or rendering fails closed:

```json
{
  "video": { "id": "jNQXAC9IVRw", "title": "Me at the zoo", "channel": "jawed",
             "upload_date": "20050424", "duration": 19,
             "webpage_url": "https://www.youtube.com/watch?v=jNQXAC9IVRw" },
  "run":   { "model": "tiny.en", "engine": "native", "backend": "auto",
             "version_tag": "0.2.0", "started": "2026-06-07T00:00:00Z",
             "wall_ms": 480, "rtf": 0.025 },
  "windows": [
    { "window_offset_sec": 0.0, "tokens": 23,
      "avg_logprob": -0.31, "no_speech_prob": 0.02 }
  ],
  "utterances": [
    { "i": 0, "start_sec": 0.0, "end_sec": 4.2,
      "text": "All right, so here we are in front of the elephants…",
      "confidence": 0.91, "speaker": null }
  ]
}
```

### Flags

| Flag | Default | Description |
|------|---------|-------------|
| `[URL]...` / `--url <U>` | — | Video or playlist URLs (positional or repeated `--url`) |
| `--batch-file <F>` | — | File with one URL per line (`#`/`;`/`]` comments and blanks ignored) |
| `--output-dir <DIR>` | `youtube_transcripts` | Destination for markdown, JSON, and `audio/` |
| `--model <M>` | backend-specific | Model name or path forwarded to the engine |
| `--language <L>` | auto-detect | Language hint (ISO 639-1) |
| `--backend <B>` | `auto` | `auto`, `whisper-cpp`, `insanely-fast`, `whisper-diarization` |
| `--diarize` | `true` | Explicitly retain the default speaker diarization stage |
| `--no-diarize` | `false` | Disable native speaker diarization |
| `--concurrency <N>` | `3` | Maximum concurrent downloads |
| `--batch-size <N>` | `0` | Bound videos per download/transcribe wave (`0` processes all in one wave) |
| `--naming-style <S>` | `slug` | `slug`, `pretty`, or ASCII-lossy `ascii` artifact names |
| `--no-keep-audio` | `false` | Delete each audio file after its transcript is written |
| `--no-retry` | `false` | Do not retry videos previously marked failed in the manifest |
| `--abort-on-error` | `false` | Stop scheduling later waves after a per-video failure |
| `--json-summary` | `false` | Emit the final run summary as JSON on stdout (for scripting) |
| `--robot` | `false` | Stream per-video NDJSON robot events (`youtube.*`, schema 1.1.0) on stdout |

### Idempotent & Resumable

The `.fw_youtube_manifest.json` makes terminal work idempotent: a re-run **skips videos already `done`** and **retries previously failed videos** (unless `--no-retry`). Incomplete intermediate work is recovered from either an explicit `downloaded` manifest state or a completed `audio/<id>.<ext>` artifact left between download and the terminal transition; partial files, symlinks, wrong ids, and paths outside the owned audio directory are rejected. **Ctrl+C cancels cleanly** — yt-dlp is killed, in-flight transcription aborts, and the manifest stays honest about what completed. By default a partial failure is recorded, emitted as `youtube.failed`, and the run continues; `--abort-on-error` stops scheduling later waves after a failure, while videos already running in the current wave may finish. Every robot run that gets past `youtube.run_start` funnels through exactly one terminal `youtube.run_complete` emission attempt.

### Requires `yt-dlp`

This subcommand orchestrates [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), which you install separately:

```bash
brew install yt-dlp        # macOS
pipx install yt-dlp        # cross-platform, isolated
pip install -U yt-dlp      # cross-platform
```

Point `franken_whisper` at a specific build with `FRANKEN_WHISPER_YTDLP_BIN=/path/to/yt-dlp` if it is not on `PATH`.

**Keep yt-dlp current.** YouTube changes its site frequently, and a stale
`yt-dlp` is a common cause of download failures. franken_whisper warns when the
resolved `yt-dlp` build is **more than 90 days old**. Update it with:

```bash
yt-dlp -U                       # update to the latest stable
yt-dlp --update-to nightly      # or track the nightly channel for the freshest fixes
```

franken_whisper deliberately downloads with the forgiving `bestaudio/best` format selector rather than a strict codec filter, so a slightly stale yt-dlp still succeeds in more cases — but when YouTube breakage does occur, updating yt-dlp is the first and usually the only step.

---

## Real-Time Streaming (`fw robot listen`)

`fw robot listen` is **true live streaming**: speak into a microphone (or pipe raw PCM / replay a WAV) and act on transcript events while the speaker is still talking. It is a separate driver from batch `robot run`, not a flag on it: batch robot mode streams sequenced *stage* events, but those events are buffered per stage and only reach stdout when each stage completes — time-to-first-text equals full-file latency. The live driver calls the native engine directly in a bounded rolling-buffer loop (capture → resample → VAD → step decode → emission policy → NDJSON), bypassing the 10-stage pipeline whose path-typed stages and fixed wall-clock budgets are structurally wrong for an unbounded session.

### Quickstart

```bash
# Live microphone -> agent-consumable NDJSON (default: multilingual tiny fast
# lane, tiny.en with --language en; AlignAtt policy)
fw robot listen | jq -r 'select(.event == "transcript.delta") | .text'

# No device needed: pipe any producer in as raw PCM (16 kHz mono s16le shown; rate/channels configurable)
ffmpeg -i stream.mp3 -f s16le -ar 16000 -ac 1 - | fw robot listen --source stdin-pcm

# Deterministic replay of a WAV through the identical event contract
fw robot listen --source file-replay --input meeting.wav --realtime-pace
```

### The event contract (schema `1.1.0`)

One JSON object per line on stdout, explicitly flushed. Every event carries `schema_version`, a strictly increasing per-session `seq`, an RFC-3339 `ts`, and the session `run_id`. A live session IS a run: it never emits `run_start`/`run_complete`; a success stream ends with `listen.session_stats {final: true}`, a fatal error ends with `run_error`.

| Event | Meaning |
|-------|---------|
| `listen.session_start` | Session configuration echo: source, capture backend, device, models, policy, step cadence, VAD parameter snapshot |
| `speech_started` | VAD opened an utterance (`utterance_id`, monotonically increasing from 1; utterances never nest) |
| `transcript.delta` | **Append-only committed text** — concatenating an utterance's deltas yields its transcript; committed text is never rewritten by later events |
| `transcript.partial` | Mutable preview of the uncommitted tail (suppress with `--no-partials`; the first remedy for slow consumers) |
| `utterance_end` | The "act now" signal: full committed `text` (32 KiB cap with `text_truncated` flag; deltas always carry the full text), `delta_count`, close `reason` = `endpoint` \| `timeout` \| `max_len` \| `session_end` |
| `transcript.confirm` / `transcript.correct` | Quality-lane verdicts keyed by `utterance_id`; may arrive **after** their `utterance_end` (async confirm lane; never blocks the live lane) |
| `listen.warning` | Structured non-fatal degradation: `silent_input`, `capture_overrun`, `fallback_capture_backend`, `fast_model_fallback`, `quality_model_unavailable`, `confirm_lag`, `forced_trim`, `decode_behind`, `persist_degraded`, `endpoint_flush_timeout`, … |
| `listen.session_stats` | Liveness heartbeat (default every 30 s, silence included) and terminal stats: `ttft_ms`, `mean/p95_step_latency_ms`, `deltas`, `utterances`, `capture_overruns`, `policy_holdbacks`, confirm-lag p50/p95/max |
| `listen.controller` | Default-off `--adaptive` decision evidence: bounded cadence/holdback transition, Brier calibration, observation count, and deterministic-fallback status |

Lifecycle invariants (enforced by contract tests): every `speech_started` is matched by exactly one later `utterance_end` carrying the same `utterance_id`; an utterance whose decode commits nothing still closes with empty text (breath/cough triggers are normal, never errors); an utterance's deltas always precede its `utterance_end`; `seq` strictly increases across every event.

```text
speech_started ──► transcript.delta* ─────► utterance_end ──► transcript.confirm/correct?
  (VAD onset)       append-only commits +      (endpoint / timeout /    async quality lane,
                    mutable partial previews    max_len / session_end)   keyed by utterance_id
```

### Emission policies

- **`--policy alignatt` (default).** AlignAtt (Simul-Whisper / SimulStreaming): a segment commits once its tokens' alignment-head cross-attention sits at least `--alignatt-holdback-ms` (default 200 ms) behind the live audio edge. Mid-utterance deltas flow as soon as attention stops attending near the buffer edge. A quality gate holds all commits for steps with high no-speech probability or very low mean log-prob (counted in `policy_holdbacks`) so non-speech audio does not hallucinate committed text.
- **`--policy endpoint-commit`.** Zero-intelligence baseline: mutable partials every step, one committed delta when the utterance closes. Kept forever as the latency harness's control arm.
- **`--policy local-agreement`.** LocalAgreement-2 fallback (whisper_streaming, arXiv 2307.14743): commit only the segment-text prefix two consecutive decodes agree on. Model-agnostic insurance (needs no attention tap); never the default.

jfk-style single-sentence utterances close before policies can differ; continuous monologues (>12 s single utterance) are where AlignAtt separates from endpoint-commit.

### Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `--source` | `mic` | `mic` \| `stdin-pcm` \| `file-replay` |
| `--input` + `--realtime-pace` | — / off | WAV input for `file-replay`; pace at real time vs. as-fast-as-possible |
| `--capture-backend` / `--mic-device` | `auto` / system default | capture backend `auto`\|`cpal`\|`ffmpeg`; input device name |
| `--list-devices` | off | enumerate input devices as NDJSON and exit (metadata only; never triggers a TCC prompt) |
| `--fast-model` | auto | fast-lane model override (default tiny.en for `en`, multilingual tiny otherwise) |
| `--policy` / `--alignatt-holdback-ms` | `alignatt` / 200 | emission policy (above); AlignAtt danger-zone width |
| `--step-ms` / `--max-buffer-sec` | 300 / 12 | decode cadence; rolling buffer cap |
| `--adaptive` | off | adapt cadence and AlignAtt holdback within fixed bounds; Brier calibration failures deterministically restore configured values and emit `listen.controller` evidence |
| `--language` | detect-and-pin | ISO 639-1 hint |
| `--max-seconds` / `--max-utterance-sec` | 0 / 90 | listening-time cap from capture start, model load excluded (0 = unbounded); force-close long open speech |
| `--no-partials` | off | suppress mutable partial previews (first remedy for slow consumers) |
| `--stats-interval-sec` | 30 | `listen.session_stats` heartbeat interval (0 = final only) |
| `--no-context` / `--capture-buffer-sec` | off / 30 | disable prompt carry; capture ring capacity |
| `--no-vad`, `--vad-gate-db`, `--vad-min-speech-ms`, `--vad-endpoint-ms` | off, 9, 250, 600 | VAD gating and tuning |
| `--quality-model`, `--confirm-drain-sec`, `--confirm-queue-bound` | auto, 10, 4 | confirm-lane controls (above) |
| `--db` / `--no-persist` | `.franken_whisper/storage.sqlite3` / off | persistence store; disable persistence |
| `--stdin-rate` / `--stdin-channels` / `--stdin-format` | 16000 / 1 / s16le | stdin-pcm format |

Full semantics per flag: [`docs/realtime-streaming.md`](docs/realtime-streaming.md).

### Models and the quality-confirm lane

The fast lane runs a small resident model: `tiny.en` when `--language en`, multilingual `tiny` otherwise (detect-and-pin). Missing fast-lane packages fall back to the turbo model with a `fast_model_fallback` warning; provision them with `fw pull tiny` / `fw pull tiny-en`.

The confirm lane re-transcribes each closed utterance with a quality model in a background thread. `--quality-model auto` (default) enables it iff the large-v3-turbo package is installed AND the fast lane did not fall back to turbo (self-confirmation is meaningless); `none` disables it; an explicit spec is honored unless it names the effective fast model. Verdicts reuse the batch CorrectionTracker and surface as `transcript.confirm`/`transcript.correct`. The live lane never blocks on the quality lane: more than `--confirm-queue-bound` (default 4) unconfirmed utterances drops the oldest with a `confirm_lag` warning, and session end waits at most `--confirm-drain-sec` (default 10) before a `confirm_drain_timeout` warning.

### Persistence

Sessions persist to SQLite by default (`--db`, default `.franken_whisper/storage.sqlite3`; disable with `--no-persist`) as ONE run row with backend `native-listen`, durability advancing at UTTERANCE granularity inside savepoint transactions. Mutable `transcript.partial` previews are deliberately NOT persisted (unlike batch, where every event is kept). A crashed session is recognizable as a listen run lacking its session-end marker; `runs.finished_at` is bumped at each flush as "last known alive".

### Latency expectations (measured, not aspirational)

From the first streaming latency campaign (`examples/listen_latency_ab.rs`, release build, `--source stdin-pcm`, paced 20 ms PCM injection; PERF_LEDGER 2026-08-23, bd-rt-latency-harness-3dkh, artifact `docs/perf_artifacts/listen_latency_campaign1_2026-08-23.json`) on a **loaded shared host** (load average ≈28–43):

- TTFT (first `transcript.delta` minus speech-onset injection): medians 3.1–5.6 s across fixtures — dominated by model load + first decode under contention, not steady-state stepping.
- Commit lag p50: ~0.79–1.21 s behind the audio being committed.
- Partial cadence: inter-partial p50 489 ms against `--step-ms 300` (cadence = step interval + decode time).
- Retraction count: 0 by construction (append-only deltas). Joined delta text was identical across policy arms on every fixture; the tone-only negative fixture produced zero output.

Honesty note: that campaign's A/A nulls missed the pre-declared band (host load), so it banks NO cross-policy comparison — quiet-host reruns can. Do not quote these rows as comparative wins; they are self-relative observations under load.

Live sessions transcribe only: speaker diarization is not part of the live driver (attribution stays a batch/post-hoc feature), and the fast lane decodes greedy-only (AlignAtt requires the attention tap, which fails requests with beam > 1).

### Agent integration

**Python:**

```python
import json, sys, subprocess

proc = subprocess.Popen(
    ["fw", "robot", "listen", "--source", "stdin-pcm"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
)
for line in proc.stdout:
    event = json.loads(line)
    if event["event"] == "transcript.delta":
        print("COMMIT:", event["text"])           # append-only: safe to persist
    elif event["event"] == "utterance_end":
        print("ACT ON UTTERANCE:", event["text"]) # complete turn, act now
    elif event["event"] == "listen.warning":
        print("DEGRADED:", event["reason"], file=sys.stderr)
    elif event["event"] == "listen.session_stats" and event.get("final"):
        break
```

**Node.js:**

```javascript
import { spawn } from "node:child_process";
import readline from "node:readline";

const proc = spawn("fw", ["robot", "listen"]);
const rl = readline.createInterface({ input: proc.stdout });
for await (const line of rl) {
  const event = JSON.parse(line);
  if (event.event === "transcript.delta") console.log("COMMIT:", event.text);
  if (event.event === "utterance_end") console.log("ACT ON UTTERANCE:", event.text);
  if (event.event === "listen.session_stats" && event.final) break;
}
```

Key on `transcript.delta` for durable state (it never changes after arrival) and `utterance_end` for turn-taking actions (answering, tool calls). Treat `transcript.partial` as ephemeral display garnish. Full architecture, design rationale, tunables, and failure-mode tables: [`docs/realtime-streaming.md`](docs/realtime-streaming.md).

## Command Reference

`franken_whisper` exposes ten top-level subcommands.

### `transcribe`

Core transcription command. Runs ingest, normalization, native Whisper,
native speaker diarization, optional alignment/punctuation stages, and
persistence. Use `--no-diarize` for transcript-only work.

```bash
franken_whisper transcribe [OPTIONS]
```

**Input (mutually exclusive):**

| Flag | Description |
|------|-------------|
| `--input <PATH>` | Audio or video file path; repeat it for batch mode |
| `--inputs-from <FILE>` | Batch mode: one input path per line (`-` = stdin); see [Batch Transcription](#6-batch-transcription-many-files-one-model-load) |
| `--stdin` | Read audio bytes from stdin |
| `--mic` | Capture from microphone via ffmpeg |

**Backend & Model:**

| Flag | Default | Description |
|------|---------|-------------|
| `--backend <KIND>` | `auto` | `auto`, `whisper_cpp`, `insanely_fast`, `whisper_diarization` |
| `--model <MODEL>` | backend-specific | Model name or path forwarded to backend |
| `--language <LANG>` | auto-detect | Language hint (ISO 639-1) |
| `--translate` | `false` | Translate to English |
| `--diarize` | `true` | Explicitly retain the default typed speaker-diarization stage |
| `--no-diarize` | `false` | Disable the speaker-diarization stage |

**Output:**

| Flag | Description |
|------|-------------|
| `--json` | Full JSON run report on stdout |
| `--output-txt` | Plain text (whisper.cpp side-output) |
| `--output-vtt` | WebVTT subtitles |
| `--output-srt` | SRT subtitles |
| `--output-csv` | CSV |
| `--output-json-full` | Extended JSON with metadata |
| `--output-lrc` | LRC karaoke format |

**Storage:**

| Flag | Default | Description |
|------|---------|-------------|
| `--db <PATH>` | `$FRANKEN_WHISPER_DB`, else `<state dir>/storage.sqlite3` | SQLite database path |
| `--no-persist` | `false` | Skip persistence entirely |
| `--timeout <SEC>` | — | Pipeline deadline (seconds) for one run; in batch mode it bounds each input separately |

**Inference Tuning (whisper.cpp):**

| Flag | Default | Description |
|------|---------|-------------|
| `--threads <N>` | `RAYON_NUM_THREADS`, else every logical CPU on a host with at most 32, else the physical core count but at least 32 | Compute threads: the whole run (model load, mel, encoder/decoder kernels, diarization) computes on one pool of exactly N workers, reused across a batch's inputs; the process adds at most 12 fixed non-compute threads (6 in a plain single-input run). An N above the CPUs the process may use (affinity mask, cgroup CPU quota) is clamped to that count, with a `warning:` line on stderr (robot mode: an `orchestration.threads_clamped` stage event and a `run_complete` warning) |
| `--processors <N>` | 1 | Parallel processors |
| `--no-gpu` | `false` | Force CPU-only |
| `--beam-size <N>` | 5 | Beam search width |
| `--best-of <N>` | 5 | Sampling candidates |
| `--temperature <F>` | 0.0 | Sampling temperature |
| `--temperature-increment <F>` | — | Temperature fallback increment |
| `--entropy-threshold <F>` | — | Entropy threshold for fallback |
| `--logprob-threshold <F>` | — | Log-probability threshold |
| `--no-speech-threshold <F>` | — | No-speech probability threshold |
| `--max-context <N>` | — | Max context tokens from prior segment |
| `--max-segment-length <N>` | — | Max segment length (characters) |
| `--no-timestamps` | `false` | Suppress timestamps |
| `--detect-language-only` | `false` | Detect language and exit |
| `--split-on-word` | `false` | Split segments on word boundaries |
| `--no-fallback` | `false` | Disable temperature fallback |
| `--suppress-nst` | `false` | Suppress non-speech tokens |
| `--tiny-diarize` | `false` | Enable TinyDiarize (speaker-turn token injection) |
| `--normalize-segment-text` | `false` | Opt in to rule-based segment-text normalization (sentence-casing + terminal periods); off by default so `segments[].text` stays byte-faithful to the transcript |
| `--prompt <TEXT>` | — | Initial prompt to guide transcription style |
| `--carry-initial-prompt` | `false` | Keep the prompt as a prefix of every 30 s window's context, not just the first |

**Audio Windowing (whisper.cpp):**

| Flag | Default | Description |
|------|---------|-------------|
| `--offset-ms <N>` | 0 | Start transcription at offset (ms); honored by every native backend (PCM sliced before decode) and the whisper.cpp bridge (`-ot`). Emitted timestamps stay in source-file time; VAD and diarization still cover the whole clip |
| `--duration-ms <N>` | — | Transcribe only this duration (ms); wall-clock scales with the slice. Bridges that cannot honor the window (insanely-fast-whisper, whisper-diarization) record it in `warnings` |
| `--audio-ctx <N>` | — | Encoder audio context in frames (0 = full 30 s window); the native engine maps N > 0 to a fixed encoder context |
| `--word-threshold <F>` | — | Per-word confidence threshold (drop words below) |
| `--suppress-regex <REGEX>` | — | Suppress tokens matching regex |

Word-level timestamp *extraction* (max-len, token-threshold, token-sum-threshold) is exposed through the `WordTimestampParams` struct via the library API; the bridge parser already extracts nested `words` arrays from `whisper.cpp` output when those parameters are set programmatically.

**VAD (Voice Activity Detection):**

| Flag | Description |
|------|-------------|
| `--vad` | Enable Voice Activity Detection |
| `--vad-model <PATH>` | Custom VAD model path |
| `--vad-threshold <F>` | Speech detection threshold |
| `--vad-min-speech-ms <N>` | Minimum speech duration (ms) |
| `--vad-min-silence-ms <N>` | Minimum silence duration (ms) |
| `--vad-max-speech-s <F>` | Maximum speech duration (seconds) |
| `--vad-speech-pad-ms <N>` | Speech padding (ms) |
| `--vad-samples-overlap <N>` | Sample overlap between windows |

**Batching (insanely-fast-whisper):**

| Flag | Default | Description |
|------|---------|-------------|
| `--batch-size <N>` | 24 | Parallel inference batch size |
| `--gpu-device <DEV>` | auto | GPU device (`0`, `cuda:0`, `mps`) |
| `--flash-attention` | `false` | Enable Flash Attention 2 |
| `--hf-token <TOKEN>` | env | HuggingFace token for diarization |
| `--timestamp-level` | `chunk` | `chunk` or `word` granularity (`word` emits one segment per word) |
| `--transcript-path <PATH>` | — | Override transcript output path |

**Diarization:**

| Flag | Default | Description |
|------|---------|-------------|
| `--diarization-engine <ENGINE>` | `auto` | `auto` selects native Sortformer; alternatives are `sortformer`, `acoustic`, `external`, `ecapa`, and `ecapa-fused` |
| `--diarization-fallback <POLICY>` | `acoustic` | `unknown`, `acoustic`, `external`, or `error`; the default handles missing/capacity-ineligible Sortformer evidence in Rust |
| `--speaker-hints <PATH>` | — | Read a `speaker-hints-v1` document in place; the path is not retained, but parsed fields persist with the run unless `--no-persist` is used |
| `--enrollment-edge-guard-ms <N>` | `100` | Remove boundary-adjacent audio before enrolling a known interval |
| `--diarization-max-prototypes <N>` | `512` | Bounded global native-diarization prototype cap (`1..=512`) |
| `--persist-speaker-profiles` | `false` | Record explicit persistence consent; schema v6 still stores privacy-safe summaries rather than reusable acoustic vectors |
| `--speaker-count-hard <K>` | — | Explicit hard search constraint; success still requires independent evidence for every speaker and uncertain speech remains UNKNOWN |
| `--speaker-count-range <MIN..MAX>` | — | Soft bounded count preference; native evidence may disagree or remain unresolved |
| `--speaker-count-prior <PRIOR>` | — | Soft point prior (`K`) or normalized distribution (`K=P,K=P`); never forces occupancy |
| `--no-stem` | `false` | Disable external-backend vocal isolation |
| `--suppress-numerals` | `false` | Spell out numbers for external alignment stability |
| `--diarization-model <MODEL>` | — | Override the external diarization model |

ECAPA fallback is deliberately asymmetric so a missing external result is not
mistaken for successful fallback:

| Policy | ECAPA ran, but evidence is insufficient | ECAPA package/load/inference unavailable |
|---|---|---|
| `unknown` | Retain the native result, hard-hint assignments, and UNKNOWN where evidence is insufficient | Emit hard hints where possible and UNKNOWN elsewhere under `native-ecapa-unavailable-v1` |
| `acoustic` | Rerun the common stack with acoustic-v2 speaker identity while retaining ECAPA provenance | Rerun acoustic identity and attach an unavailable-ECAPA summary |
| `external` | Use valid external labels when present; otherwise retain the insufficient ECAPA result | Use valid external labels when present; otherwise return an error |
| `error` | Return an inner-diarizer error | Return an error |

**Speculative Streaming:**

| Flag | Default | Description |
|------|---------|-------------|
| `--speculative` | `false` | Enable dual-model speculative cancel-correct mode |
| `--fast-model <MODEL>` | — | Fast model for low-latency partial transcripts |
| `--quality-model <MODEL>` | — | Quality model for correction / verification |
| `--speculative-window-ms <N>` | 3000 | Sliding window size (ms) |
| `--speculative-overlap-ms <N>` | 500 | Window overlap (ms) |
| `--correction-tolerance-wer <F>` | — | WER tolerance for confirmation vs. retraction |
| `--no-adaptive` | `false` | Disable adaptive window sizing |
| `--always-correct` | `false` | Force quality model on every window (evaluation mode) |

### `diarization-corpus`

External-only preparation and aggregate evaluation for public or
operator-licensed diarization corpora. The registry does not download data or
accept a license on the operator's behalf.

`registry` is available on every supported CLI target. The artifact-writing
`prepare-voxconverse`, `build`, `ablate`, `sidecar-study`, and `compare-models`
commands require Linux, Android, or an Apple platform; Windows and other targets return
`public_corpus.output_platform` before reading corpus media or annotations.

```bash
# inspect frozen source, license, conversion, and acknowledgement contracts
franken_whisper diarization-corpus registry

# hash the official extracted VoxConverse WAV/RTTM files in place and write a
# deterministic descriptor beneath the external input root; no media is copied
franken_whisper diarization-corpus prepare-voxconverse \
  --input-root /absolute/external/voxconverse \
  --development-audio-root /absolute/external/voxconverse/dev-wav/audio \
  --test-audio-root /absolute/external/voxconverse/test-wav/voxconverse_test_wav \
  --annotation-root /absolute/external/voxconverse/labels \
  --output /absolute/external/voxconverse/descriptor.json \
  --source-version <IMMUTABLE_UPSTREAM_ARCHIVE_AND_LABEL_ID> \
  --license-ack accept-voxconverse-cc-by-4.0-and-original-copyright

# validate external WAV/RTTM inputs and create one path-free bundle
franken_whisper diarization-corpus build \
  --input-root /absolute/external/corpus \
  --descriptor /absolute/external/corpus/descriptor.json \
  --output /absolute/external/results/bundle.json \
  --license-ack <REGISTRY_ACKNOWLEDGEMENT_ID>

# run the existing acoustic-v2 representation/detector/clustering ablation v8
franken_whisper diarization-corpus ablate \
  --input-root /absolute/external/corpus \
  --descriptor /absolute/external/corpus/descriptor.json \
  --bundle-output /absolute/external/results/ablation-bundle.json \
  --output /absolute/external/results/ablation-development.json \
  --license-ack <REGISTRY_ACKNOWLEDGEMENT_ID> \
  --stage development

# run the separate, evaluation-only multiscale sidecar study
franken_whisper diarization-corpus sidecar-study \
  --input-root /absolute/external/corpus \
  --descriptor /absolute/external/corpus/descriptor.json \
  --bundle-output /absolute/external/results/sidecar-bundle.json \
  --output /absolute/external/results/sidecar-development.json \
  --license-ack <REGISTRY_ACKNOWLEDGEMENT_ID> \
  --stage development

# compare all native lanes with the pinned operator-installed Sortformer oracle
RAYON_NUM_THREADS=8 franken_whisper diarization-corpus compare-models \
  --input-root /absolute/external/corpus \
  --descriptor /absolute/external/corpus/descriptor.json \
  --bundle-output /absolute/external/results/model-comparison-bundle.json \
  --output /absolute/external/results/model-comparison-development.json \
  --license-ack <REGISTRY_ACKNOWLEDGEMENT_ID>
```

The VoxConverse adapter preserves original file hashes and applies one narrow,
evidenced geometry normalization in memory: an official turn that starts before
WAV EOF may be clipped when it overruns EOF by at most 100 ms. The preparation
receipt and bundle retain clipped-turn and clipped-millisecond counts; larger
overruns and turns beginning at EOF fail closed.

`compare-models` is a development-only, diagnostic comparison of
`native_acoustic`, `native_ecapa`, `native_ecapa_fused`, `native_sortformer`,
and `external_sortformer`. It infers speaker count, fixes native and Sortformer CPU
worker counts at eight, and applies the same frozen 1800-second attempt timeout
to every lane. The application downloads neither the ECAPA
package nor the external Sortformer adapter/model; the native Sortformer lane
uses the release-bound cache installed by the installer or `fw pull sortformer`. Absent
components become typed lane skips. Protocol v6 pins the complete effective native request
for each lane, its ordered payload-free outcome taxonomy, and its own canonical
digest. Any change to those bindings requires a new version-and-digest pair.

The comparison evidence is aggregate-only and cannot authorize a superiority
or production-routing claim. Every lane/observation runs in a fresh process
under the balanced Williams order. The worker rechecks the executable, audio,
normalized PCM, reference, scorer, protocol, and applicable model artifact
identities. Parent-observed wall time includes process launch, bounded IPC,
worker identity validation, audio decode, model load, inference, output
validation, scoring, parent-side post-run identity validation, and the native
platform resource probe. The parent kills the complete descendant process
group on cancellation or timeout, records a live recursive-descendant
cancellation probe through the same bounded observer path used by real lanes.
Cancellation, timeout, and output-limit checks run before observation. On Unix,
cleanup reaps the root and verifies that the owned process group is absent;
cleanup failure overrides a nominal success, cancellation, or timeout. An
initial group-signal error is accepted only when the subsequent absence probe
still certifies that the complete group is gone. Before
reading its request, the worker opens an inherited kernel-pipe capability bound
to its direct parent and starts a liveness watcher. Abrupt parent death closes
the sole write end, causing the worker to terminate its complete process group;
unsupported platforms fail before launching an observed worker. The RSS
field is an approximate sampled maximum of the concurrent process-group sum,
including nested subprocess adapters. Sample starts are no closer than 50 ms,
and each platform probe has its own fixed bound; this is not an exact process
high-water mark or a promise of exactly 50 ms between samples. A worker that
exits before any sample is explicitly unavailable, while repeated disappearance
of a still-live group fails the resource probe. The platform scan checks both
cancellation and the enclosing attempt deadline. A matched live Linux group
member cannot be silently omitted: every such member must expose a valid RSS
field. A complete zero-only scan is treated as a missing sample, never as a
measured zero, and repeated zero-only observations fail closed. Wall time, RTF,
sampled whole-tree RSS, and cancellation latency carry explicit scope,
authority, and cap dispositions rather than zero or shared-process estimates.
The companion path-free public bundle is record-level scorer input and therefore
retains opaque public recording/speaker IDs and reference timestamps, but no
source path, filename, audio, or transcript.

`verify_public_model_comparison_bundle_identity_pair` validates both retained
artifacts and proves that their corpus, source, descriptor, bundle, split, and
recording-count identities agree. Because the evidence is aggregate-only, this
API does not derive its observation-set commitment or metrics from the bundle;
that stronger proof still requires source reconstruction and a fresh run.

All path arguments must be absolute. Entire output file names must use lowercase
ASCII letters, digits, period, underscore, and hyphen and end in the exact
suffix `.json`; a handle-relative preflight also rejects an existing
ASCII-case-fold sibling, making ordinary case-sensitive and case-insensitive
collisions fail consistently. Exact-name no-clobber publication remains the
atomic creation guard. Input data must
remain outside the checkout, and bundle/evidence parents must be outside both
the checkout and input root. Outputs use create-new semantics and are never overwritten. On
Linux, Android, and Apple platforms, complete JSON is privately staged relative
to an identity-bound directory handle and atomically published with no-clobber
semantics. The terminal parent may not be a symlink; it must be owned by the
effective user and not group/world writable. This protects handle-relative
directory contents while treating the effective user as trusted, because that
user can also alter a final artifact afterward. Requested and canonical
terminal-directory identities are checked throughout. Ancestor rename
authority, ACLs, privileged mount changes, and arbitrary mount aliases of a
checkout/input descendant are outside this boundary; use a privately controlled
output path and filesystem without broader ACL access. Other platforms fail
closed for this public-artifact path. Add
`--maximum-recording-duration-ms <N>` to freeze a deterministic prefix. A
pre-publication failure creates no final-name artifact and never modifies an
existing final-name entry. After permission verification, later failures
truncate and synchronize the private staging inode to a zero-length mode-0600
marker; this is not a secure block erase. Creation is followed by an explicit
mode-0600 permission operation and verification that the inode is a regular
file owned by the effective user with exactly those access bits; failure is
reported before payload serialization. POSIX/NFSv4 ACLs and mount policies
that grant access beyond Unix mode bits are outside this writer's authority, so
public-artifact output directories must reside on a filesystem where such
broader access is absent. A permission-establishment failure leaves an empty
marker but makes no mode claim. A storage failure during a payload scrub reports
`public_corpus.output_cleanup_uncertain`. An error after the
no-clobber rename is reported as
`public_corpus.output_commit_uncertain`, because the final artifact may already
exist and is not truncated. An ambiguous rename error uses the same
commit-uncertain result and conservatively preserves the held inode; only an
authoritative no-clobber conflict is treated as definitely pre-commit. Bundle
and evidence files are each published
atomically, but their two renames are not a cross-file transaction; successful
evidence publication is the completion signal for the pair. A
sidecar certification run uses `--stage certification` and must also supply
`--locked-development-evidence <PATH>`; it evaluates the unfused baseline and
only the single candidate selected by the exact locked development artifact.
Both stages parse and hash the complete descriptor and audit its path-free
cross-split metadata, but materialize WAV, RTTM, and optional word-annotation
bytes only for the stage's selected split. Certification validates the retained
development artifact's complete internal contract—including both calibration
fingerprints and provenance, selected lane, recomputed gates/ranking/disposition,
and result/accuracy hashes—then binds the current descriptor and protocol before
opening held-out inputs. This validation does not refit calibration or replay
development audio. Development and certification
therefore create distinct split-specific bundle hashes; the shared descriptor
and protocol hashes are the cross-stage lock.
Source paths, filenames, recording/speaker identifiers, per-recording
observations, feature values, audio, and transcripts never enter the aggregate
study evidence.

### `robot`

Agent-first interface with structured NDJSON output and a stable schema contract.

```bash
# streaming transcription with stage events
franken_whisper robot run [TRANSCRIBE_OPTIONS]

# live microphone / pipe streaming (see "Real-Time Streaming" section)
franken_whisper robot listen [--source mic|stdin-pcm|file-replay ...]

# emit the full JSON schema for every event type
franken_whisper robot schema

# discover backends and capabilities
franken_whisper robot backends

# system health diagnostics (backends, ffmpeg, database, resources)
franken_whisper robot health

# query routing decision history
franken_whisper robot routing-history [--run-id <ID>] [--limit 20]
```

**Robot Event Catalog (schema `1.1.0`; the six core `listen.*` / speech-lifecycle events and the optional adaptive-controller event are additive members of the same contract):**

| Event | Description |
|-------|-------------|
| `run_start` | Request accepted, pipeline starting |
| `stage` | Pipeline stage progress (sequenced, timestamped) |
| `run_complete` | Transcription finished with full result |
| `run_error` | Pipeline failed with structured error code |
| `backends.discovery` | Backend availability + per-backend capabilities |
| `routing_decision` | Backend routing decision: chosen action, calibration score, e-process, fallback state, recommended order |
| `health.report` | System health (backend / ffmpeg / DB / resource status) |
| `transcript.partial` | Speculative fast-model partial transcript (immediate) |
| `transcript.confirm` | Quality model confirms partial (drift within tolerance) |
| `transcript.retract` | Quality model retracts partial (drift exceeds tolerance) |
| `transcript.correct` | Quality model correction with corrected segments |
| `transcript.speculation_stats` | Aggregate speculation pipeline statistics |
| `listen.session_start` | Live session configuration echo (additive 1.1.0 family; a session never emits `run_start`/`run_complete`) |
| `speech_started` | VAD opened an utterance (`utterance_id` from 1, never nested) |
| `transcript.delta` | Append-only committed text for the live driver (concatenating deltas = the utterance transcript) |
| `utteranc