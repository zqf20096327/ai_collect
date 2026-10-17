# dsh-visual-plugin

<p align="center">
  <img src="https://raw.githubusercontent.com/jyh20030112/dsh-visual-plugin/main/assets/deepseek_neon_pixel_whale_transparent.svg" width="240" alt="DeepSeek neon pixel whale">
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/dsh-visual-plugin"><img src="https://img.shields.io/npm/v/dsh-visual-plugin?logo=npm&label=npm" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/dsh-visual-plugin"><img src="https://img.shields.io/npm/dm/dsh-visual-plugin?label=downloads" alt="npm downloads"></a>
  <a href="https://github.com/jyh20030112/dsh-visual-plugin/stargazers"><img src="https://img.shields.io/github/stars/jyh20030112/dsh-visual-plugin?logo=github&label=Stars" alt="GitHub stars"></a>
  <a href="https://github.com/jyh20030112/dsh-visual-plugin/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-65a30d?style=flat" alt="MIT license"></a>
  <br>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=fff" alt="TypeScript">
  <img src="https://img.shields.io/badge/zero__runtime__deps-16a34a?style=flat" alt="zero runtime deps">
</p>

<p align="center">
  <b>A local-first visual media plugin for DeepSeek Harness.</b><br>
  Validate, transcode, and extract video keyframes locally; understand images and
  videos with DSH's current vision model, view image history, and play videos in the right panel.
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> · <a href="README.zh.md">简体中文</a>
</p>

A plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

Video preprocessing and plugin-owned media storage stay on the machine running DSH. Images and extracted keyframes are sent through DSH to your selected model; whether inference runs locally depends on your DSH model configuration.

## Features

- **Native image understanding** — uploaded images stay on DSH's native attachment and model path; the plugin does not configure or call a separate vision model.
- **Copyable image history** — the right panel records the current DSH model's final answer beside each image thumbnail, with expandable history and one-click copy.
- **Plugin-owned video upload** — accepts MP4, M4V, MOV, AVI, MPG/MPEG, MKV, and WebM only when extension, signature, and FFprobe agree.
- **Scene-aware video analysis** — normalizes to H.264/yuv420p MP4, extracts keyframes with PySceneDetect, and sends ordered timestamped images to the current DSH vision model.
- **Right-side panel** — switch between image/video views, play normalized videos directly, and stage a selected video in the chat draft.
- **Advanced video settings** — tune upload size, storage quota, duration, output size, FPS, CRF, and keyframe count from the plugin settings card.

## How it works

<p align="center">
  <img src="https://raw.githubusercontent.com/jyh20030112/dsh-visual-plugin/main/assets/vision-bridge-flow.svg" width="720" alt="Image and video analysis in the dsh web right panel">
</p>

```
image → DSH native attachment → current image-capable model → final answer
  → /vision-bridge/recent → panel thumbnail + copyable description

video → container validation → H.264/yuv420p normalization → PySceneDetect
  → timestamped keyframes → DSH native image attachments → current model answers
```

The plugin never rewrites model messages or calls a private vision endpoint. Select an image-capable model in DSH before sending images or asking about a video.

## Quick start

Plugin `0.4.x` targets DSH `0.2.0-rc.2`; keep plugin `0.3.2` for DSH `0.1.x`. No exact-version risk exemption is needed.

### 1. Install host dependencies

Image features work without these tools. Video support requires FFmpeg/FFprobe `>= 6.1` from the same major release, an FFmpeg build with `libx264`, and PySceneDetect `>= 0.7.1 < 0.8`.

Install the tools on the machine and under the user account that runs `dsh web`. The commands `ffmpeg`, `ffprobe`, and `scenedetect` must be available on that process's `PATH`, from any directory. If DSH runs in Docker, WSL, or on a remote server, install the dependencies inside that environment.

#### macOS (Homebrew)

Install [Homebrew](https://brew.sh/) first if needed, and follow its post-install instructions to add `brew` to your `PATH`. Then install [FFmpeg](https://formulae.brew.sh/formula/ffmpeg), which includes FFprobe, and [uv](https://docs.astral.sh/uv/getting-started/installation/):

```sh
brew install ffmpeg uv
```

#### Arch Linux (pacman)

Install the official [FFmpeg](https://archlinux.org/packages/extra/x86_64/ffmpeg/) and [uv](https://archlinux.org/packages/extra/x86_64/uv/) packages:

```sh
sudo pacman -Syu ffmpeg uv
```

#### Windows (PowerShell, WinGet)

Open PowerShell and confirm [WinGet](https://learn.microsoft.com/windows/package-manager/winget/) is available with `winget --version`. If it is missing, install or update **App Installer** using the instructions in that link. On Windows x64, install FFmpeg (including FFprobe) and uv:

```powershell
winget install --id Gyan.FFmpeg --exact
winget install --id astral-sh.uv --exact
```

Close and reopen PowerShell before continuing so the new `PATH` takes effect. If WinGet is unavailable, use a Windows build linked from the [FFmpeg download page](https://ffmpeg.org/download.html), extract it to a permanent directory such as `C:\Tools\ffmpeg`, and add the directory containing `ffmpeg.exe` and `ffprobe.exe` (usually `bin`) to your user `Path` in **Environment Variables**. Install uv using its [official Windows instructions](https://docs.astral.sh/uv/getting-started/installation/).

#### Install PySceneDetect with uv (all three systems)

Run the following in your terminal or PowerShell:

```sh
uv tool install --python 3.12 "scenedetect>=0.7.1,<0.8"
uv tool update-shell
```

This installs PySceneDetect as a persistent command in an isolated environment for the current user. uv downloads Python 3.12 if needed; the standard `scenedetect` package includes its OpenCV dependencies. You do not need to activate a virtual environment before starting DSH. See the [uv tool guide](https://docs.astral.sh/uv/guides/tools/) and [PySceneDetect installation guide](https://www.scenedetect.com/download/).

### 2. Verify dependencies

Close and reopen your terminal after `uv tool update-shell`. In the same environment you will use to start DSH, run:

```sh
ffmpeg -version
ffprobe -version
ffmpeg -hide_banner -encoders
scenedetect version
```

Confirm FFmpeg and FFprobe are both `>= 6.1` and have the same major version, the encoder list includes `libx264`, and PySceneDetect is `>= 0.7.1 < 0.8`.

If a command is missing, locate it with `command -v ffmpeg ffprobe scenedetect` on macOS/Arch, or `Get-Command ffmpeg, ffprobe, scenedetect` in PowerShell. For PySceneDetect, `uv tool dir --bin` shows the directory that must be on `PATH`. Services and containers must also receive this `PATH`; restart the DSH process after changing it.

The plugin never downloads these tools or runs installers. The settings card reports video dependency issues while image features remain available.

### 3. Install the plugin

```sh
dsh plugin --profile web add dsh-visual-plugin   # or: github:jyh20030112/dsh-visual-plugin
```

When developing this checkout against a local DeepSeek Harness source tree, install the local package instead:

```sh
cd /absolute/path/to/dsh-visual-plugin
npm run bootstrap
dsh plugin --profile web add link:/absolute/path/to/dsh-visual-plugin
```

`bootstrap` requires an installed, built `dsh-v0.2.0-rc.2` Harness checkout and automatically finds a sibling or ancestor-adjacent checkout.
For another layout, set its location explicitly:

```sh
HARNESS=/absolute/path/to/deepseek-harness npm run bootstrap
```

### 4. Restart and use

Restart `dsh web` from the environment where the dependency checks passed, then:

1. Open **Settings → Plugins**, then the **dsh-visual-plugin** detail page and its **Visual Media** configuration. Use **Sidebar** to show or hide the right panel and adjust advanced video settings. Changes apply immediately, persist in the current profile across restarts, and recover valid archived video preferences without overwriting new settings during upgrades.

   <img src="https://raw.githubusercontent.com/jyh20030112/dsh-visual-plugin/main/assets/vision-bridge-config-rc2.png" width="560" alt="Visual Media configuration on the DSH rc.2 plugin detail page">

2. Select an image-capable model in DSH; there is no separate vision-model configuration in this plugin.
3. Send an image. The current model answers natively, and the image panel records the thumbnail and final answer for copying.
4. Upload a video from **Upload video** beside the composer. Once processing finishes, select **Videos** in the right panel to play it; **Ask in chat** stages a draft and never submits automatically.

### Vision model

Image and keyframe understanding use the image-capable model currently selected in DSH. Model providers, endpoints, and credentials are managed by DSH rather than this plugin.

## Uninstall

```sh
dsh plugin --profile web remove dsh-visual-plugin
```

Restart `dsh web`. The command forwards to `pnpm remove` inside the profile, and the bundle layer list reconciles to drop the plugin automatically.

## Project layout

```
src/
  index.ts      native image history, video_describe tool, settings, and HTTP routes
  config.ts     advanced video-processing settings and runtime policy
  video/        upload, container probing, transcoding, scene detection, keyframes, and HTTP Range playback
  client/       image/video panel, upload controls, advanced settings, locales, and CSS
cordis.patch.yml  bundle patch layer
```

## Build

```sh
npm run bootstrap && npm run typecheck && npm run build   # needs a local harness checkout
```

Prebuilt `lib/` is committed, so consumers never build.

## CI/CD

`ci.yml` verifies artifacts and the pack contents on every push/PR. `release.yml` (tag `v*`) checks the version, packs, creates a GitHub Release, and publishes to npm.

## Resources

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — the plugin host this project extends.
- [PySceneDetect](https://www.scenedetect.com/) — scene detection used to select video keyframes.
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) — the curated DSH plugin list where this plugin is registered.

## Friendly Links

- [LINUX DO](https://linux.do)

## Thanks

- [HsiangNianian](https://github.com/HsiangNianian/) — for their help and insights during development.
- [tingfeng347](https://github.com/tingfeng347) — for the build-stability and local-harness-setup fixes.
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) — a DSH Web UI plugin that auto-resumes interrupted requests with 「继续」 (error classification, adaptive backoff, browser notifications); a handy companion.

## License

[MIT](LICENSE)
