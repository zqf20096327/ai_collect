# shardreel

Turns long gameplay recordings into vertical 9:16 clips for Shorts, Reels and TikTok.
Runs natively on Apple Silicon Macs and on Linux (including WSL2). No Docker, no cloud renderer, no subscription.

The product is called shardreel. The Rust engine and data folder keep their internal name,
`clipforge` (`~/.clipforge`, `CLIPFORGE_*` environment variables).

| Stage | What runs on your Mac |
|---|---|
| Transcription | whisper.cpp (large-v3-turbo): Metal on Mac, CPU on Linux (CUDA optional) |
| Decode and encode | VideoToolbox on Mac; on Linux NVENC (NVIDIA), else VAAPI (Intel/AMD, integrated GPUs too), else libx264/libx265 |
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
| RAM | 4 GB (8 GB for the large Whisper models) | 16 GB |
| CPU cores | 4 (warning only) | 8 |
| GPU | none on Linux (light mode); Apple Silicon on Mac | NVIDIA GPU on Linux |

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
build with `cargo run --release --features cuda`. Hardware encoding is picked automatically:
NVENC when `nvidia-smi` works, else VAAPI on Intel/AMD GPUs (integrated ones too; needs
`/dev/dri/renderD*`, override with `CLIPFORGE_VAAPI_DEVICE`), else libx264/libx265. Each
hardware encoder is test-encoded once before use, so a listed but unsupported one is skipped.
Clips are saved to `~/Videos/clipforge/`.

Without an NVIDIA GPU, new jobs start in **light mode** with the base Whisper model: clips
render at 30 fps, one at a time, which roughly halves render time and memory on 60 fps sources.
Both can be changed per job.

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

While a job runs, **Cancel** stops it within a second. A failed or cancelled job has a
**Resume** button: it reruns with the same settings and reuses the download, analysis and,
in scan mode, every clip already rendered. Turn on **Review before rendering** (Clips card)
to untick, retitle and trim the picked moments before anything renders; for URLs each moment
has a link that opens the video at that time.

For long streams from a URL, turn on **Long videos** in the job options. It never downloads
the whole video. Two strategies:

- **Scan whole video** (default): downloads only the audio (about 50 MB per hour), finds the
  best moments across the full length from loudness spikes and YouTube's "most replayed"
  heatmap, then downloads and renders only those moments. Speech recognition runs on the final
  clips only, unless AI ranking is on (it then reads every candidate). A 2-hour stream gives
  3 clips in about 2.5 minutes on a 4-core laptop without a dedicated GPU.
- **Chunk by chunk**: downloads, analyses and renders a few minutes at a time, deleting each
  piece, and stops once it has enough clips. It also uses on-screen action, but without a
  heatmap the clips come from early in the video.

Downloads use 4 parallel range requests (YouTube throttles single connections to about
1 MB/s), for whole videos too. If YouTube kept the live chat replay, scan mode downloads it in
the background and also weights the moments chat reacted to. Live streams still in progress, and videos under about 10 minutes, run in one pass.

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
