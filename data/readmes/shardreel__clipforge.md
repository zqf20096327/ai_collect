# shardreel

Turns long gameplay recordings into vertical 9:16 clips for Shorts, Reels and TikTok.
Runs natively on Apple Silicon Macs and on Linux (including WSL2). No Docker, no cloud renderer, no subscription.

The product is called shardreel. The Rust engine and data folder keep their internal name,
`clipforge` (`~/.clipforge`, `CLIPFORGE_*` environment variables).

| Stage | What runs on your Mac |
|---|---|
| Transcription | whisper.cpp (large-v3-turbo): Metal on Mac, CPU on Linux (CUDA optional) |
| Decode and encode | VideoToolbox on Mac, NVENC on Linux with an NVIDIA GPU, libx264/libx265 fallback |
| Moment detection | loudness spikes, on-screen action, speech rate, hype words |
| Ranking and titles (optional) | Gemini, OpenRouter, LM Studio or Ollama |
| Captions | word-by-word highlighted captions and a hook banner (libass) |
| Interface | local web UI with live progress, served by the same process |

Analysis is cached, so re-rendering with another layout skips transcription and analysis.

## Requirements

### Hardware and storage

shardreel checks these at startup (Settings > System) and refuses to start a job below the minimum.

| Resource | Minimum | Recommended |
|---|---|---|
| Free disk (in `~/.clipforge`) | 10 GB | 30 GB |
| RAM | 8 GB | 16 GB |
| CPU cores | 4 (warning only) | 8 |
| GPU | none on Linux (slow); Apple Silicon on Mac | NVIDIA GPU on Linux |

The Whisper model alone is about 1.6 GB. Source videos, cache and rendered clips need the rest.
Intel Macs are not supported.

### macOS (Apple Silicon)

```bash
brew install cmake yt-dlp ffmpeg-full
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh   # Rust
curl -fsSL https://bun.sh/install | bash                          # bun
```

`ffmpeg-full` is keg-only (it does not replace an existing ffmpeg). It includes libass, which
captions need, and shardreel looks for it first. Hardware encoding is always on on Mac.

### Linux (Debian, Ubuntu)

```bash
sudo apt install build-essential cmake pkg-config libclang-dev ffmpeg pipx
pipx install yt-dlp
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh   # Rust
curl -fsSL https://bun.sh/install | bash                          # bun
```

Transcription runs on the CPU by default. With an NVIDIA GPU and the CUDA toolkit installed,
build with `cargo run --release --features cuda`. Hardware encoding (NVENC) is used
automatically when `nvidia-smi` works and ffmpeg has `h264_nvenc`. Otherwise shardreel uses
libx264/libx265. Clips are saved to `~/Videos/clipforge/`.

### Windows through WSL2

Use WSL2 with an Ubuntu distro and follow the Linux steps inside it.

- Keep the project and `~/.clipforge` on the Linux filesystem (`/home/you`), not under `/mnt/c`.
  File access through `/mnt` is much slower, and Settings shows a warning if you do.
- For GPU support, install the NVIDIA Windows driver with WSL support. Do not install a Linux
  GPU driver inside WSL.
- Open http://127.0.0.1:8787 in your Windows browser. WSL2 forwards localhost.
- Give WSL enough memory and disk in `%UserProfile%\.wslconfig` if the checks fail.

## Build and run

```bash
cd web && bun install && bun run build && cd ..
cargo run --release
```

Open http://127.0.0.1:8787. The first build compiles whisper.cpp and takes a few minutes.
The first job with speech recognition downloads the Whisper model (about 1.6 GB) to
`~/.clipforge/models`.

Open **Settings** to check that ffmpeg, libass, yt-dlp and the hardware encoder are found.

For UI development, run `cargo run --release` and `cd web && bun run dev`
(http://localhost:5173 proxies `/api` to the backend).

## Use

1. Open **New job**. Upload a video, or enter a local path or a YouTube or Twitch URL.
2. Pick a layout (blur, crop, facecam, fit). Facecam is beta: choose a local video first, press
   **Pick on frame**, and draw a box around your webcam.
3. Optional: turn on AI ranking and pick a provider.
4. Press **Generate clips** and watch the stages. URL downloads show a progress bar.

Clips are saved to `~/Movies/clipforge/<video-name>/` (Linux and WSL: `~/Videos/clipforge/`): the `NN_title.mp4` files, a `.jpg`
thumbnail for each, and `clips.json` with timestamps, title, hook, hashtags and a caption.

Each clip carries "Built with shardreel" in its metadata, along with the title and caption.
There is no watermark. Switch it off with **Embed shardreel tag** in the job options.

### AI ranking

Set a key in **Settings**, or in `~/.clipforge/.env` (see `.env.example`). Then choose the
provider in the job form. OpenRouter defaults to `google/gemini-3.8-flash`. If you set your own
model there, use the vendor prefix. If a model call fails, the run finishes on signal ranking.

### Free disk space

**Settings > Storage** shows downloads, analysis cache, uploads and Whisper models, with a
Clear button for each. Rendered clips are never deleted.

## How moments are picked

1. **Loudness spike:** how much louder each second is than the surrounding minute.
2. **On-screen action:** ffmpeg scene-change score at 4 fps.
3. **Speech:** words per second, plus hype phrases ("no way", "bro", "five stars", "cops").
4. Peaks become candidate windows, with the peak about 65 percent of the way in. Windows snap
   to sentence boundaries and cuts, and never end before the reaction.
5. Optional: a model re-ranks the candidates within guard rails and writes the title, hook and
   hashtags.

## Layout of this repository

| Path | What it is |
|---|---|
| `src/` | Rust backend: pipeline, whisper, ffmpeg, HTTP API |
| `web/` | React UI (Vite, bun) |
| `docs/plans/` | Change plans |

## Rights

Clip your own gameplay, or streamers who allow it. Reposting other people's streams without
permission gets accounts struck.

## License

MIT. See [LICENSE](LICENSE). Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).
To report a vulnerability, see [SECURITY.md](SECURITY.md).
