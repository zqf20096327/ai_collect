# Clipsmith

**A free, open-source alternative to OpusClip. Turn one long YouTube video into a batch of ready-to-post Shorts, on your own laptop.**

[![tests](https://github.com/AbdulSamad94/clipsmith/actions/workflows/tests.yml/badge.svg)](https://github.com/AbdulSamad94/clipsmith/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![Runs offline](https://img.shields.io/badge/runs-offline-brightgreen)
![No API key](https://img.shields.io/badge/API%20key-not%20needed-brightgreen)
![No GPU](https://img.shields.io/badge/GPU-not%20needed-brightgreen)
[![GitHub stars](https://img.shields.io/github/stars/AbdulSamad94/clipsmith?style=social)](https://github.com/AbdulSamad94/clipsmith/stargazers)

Paste a YouTube link. Clipsmith finds the best 30–60 second moments, crops them to vertical 9:16 around the speaker, burns in animated word-by-word captions, and ranks them by how likely they are to hold a viewer.

- **Free and unlimited.** No credits, no monthly plan, no watermark, no clips that expire after 3 days.
- **Runs offline.** Moment picking uses a local AI model (Qwen via Ollama). No API key, no account, your videos never leave your computer.
- **Works on an ordinary laptop.** No GPU needed; it was built and tested on a 4-core Intel laptop CPU.

> Not affiliated with OpusClip. "OpusClip" is mentioned only to describe what this project is an alternative to.

![Clipsmith screenshot](docs/ss.png)

## Clipsmith vs OpusClip

| | Clipsmith | OpusClip Free | OpusClip paid |
|---|---|---|---|
| Price | **Free forever** | $0 | from $15/month |
| Clips per month | **Unlimited** | 60 credits | 150+ credits |
| Watermark | **None** | Yes | No |
| Clips expire | **Never** | After 3 days | After 30 days+ |
| Runs on your computer, offline | **Yes** | No | No |
| Your videos stay private | **Yes** | Uploaded | Uploaded |
| Open source | **Yes (MIT)** | No | No |
| AI picks + viral score | Yes | No score | Yes |
| Animated captions + 9:16 reframe | Yes | Yes | Yes |
| B-roll, scheduler, team features | Not yet | No | Yes |

*OpusClip details from its public pricing page, November 2026.*

## What it does

1. **Downloads** the video and YouTube's captions (or transcribes the audio with Whisper if there are none).
2. **Picks the moments** that open strong, stand on their own and end on a complete thought, and gives each a viral score, a title, an on-screen hook, a caption and hashtags.
3. **Reframes** to 9:16, following the speaker's face. Wide shots get the full frame over a blurred background instead.
4. **Captions** every word as it's spoken, in one of three styles.
5. **Exports** MP4s you can download and upload to YouTube Shorts, TikTok or Reels.

## Install

You need **Python 3.10+**, **ffmpeg** and, for AI moment picking, **Ollama**.

### 1. Prerequisites

| | Windows | macOS | Linux |
|---|---|---|---|
| Python | [python.org](https://www.python.org/downloads/) | `brew install python` | your package manager |
| ffmpeg | `winget install Gyan.FFmpeg` | `brew install ffmpeg` | `sudo apt install ffmpeg` |
| Ollama | [ollama.com/download](https://ollama.com/download) | [ollama.com/download](https://ollama.com/download) | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Deno *(YouTube downloads need a JS runtime)* | `winget install DenoLand.Deno` | `brew install deno` | `curl -fsSL https://deno.land/install.sh \| sh` |

Node.js works instead of Deno if you already have it.

### 2. Download the AI model (about 3.3 GB, once)

```
ollama pull qwen3.5:4b
```

### 3. Set up Clipsmith

```
git clone https://github.com/AbdulSamad94/clipsmith.git
cd clipsmith
```

- **Windows:** double-click `setup.bat`
- **macOS / Linux:** `./setup.sh`

## Run

- **Windows:** double-click `run.bat`
- **macOS / Linux:** `./run.sh`

Then open **http://127.0.0.1:8765**, paste a YouTube link and click **Get clips**.

## How long it takes

On a 4-core laptop CPU, a 12-minute video takes about **10 minutes**: a few minutes for the AI to read it, then about 1–3 minutes per clip to render. Longer videos take proportionally longer. Fewer clips means faster results.

## Post straight to YouTube

Connect your channel once and every clip gets a **Post to YouTube** button: the AI's title, description and hashtags are filled in, and you can post now or **schedule** it (YouTube publishes it at that time, even if your computer is off). Setup takes about 5 minutes with your own free Google app: see **[docs/youtube-setup.md](docs/youtube-setup.md)**.

## Choosing the AI

Set this in `.env` (copy it from `.env.example`):

| Option | Cost | Speed | Setting |
|---|---|---|---|
| **Local Qwen** (default) | Free | Slow on CPU | `AI_PROVIDER=ollama` |
| Google Gemini | Free tier | Fast | `AI_PROVIDER=gemini` + `GEMINI_API_KEY` |
| Anthropic Claude | Paid | Fast | `AI_PROVIDER=claude` + `ANTHROPIC_API_KEY` |
| None | Free | Fastest | `AI_PROVIDER=none` (basic scoring by rules) |

On a machine with more RAM or a GPU, try a bigger local model for better picks, e.g. `OLLAMA_MODEL=qwen3.5:9b`.

## Known limitations

- The small local model sometimes gets facts or numbers wrong in titles. **Check titles before posting.**
- Face tracking is basic (OpenCV). Fast camera cuts can make the crop lag.
- No direct posting to YouTube yet; you download the MP4 and upload it yourself.

## Roadmap

- [ ] Filler word and silence removal
- [ ] "Prompt to clip": describe the moment you want
- [ ] Edit clip start/end and caption text before export
- [ ] Keyword and emoji highlights in captions
- [ ] Brand template (logo, fonts, colours)
- [x] Post and schedule directly to YouTube

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) and the [`good first issue`](https://github.com/AbdulSamad94/clipsmith/labels/good%20first%20issue) label. If Clipsmith saves you money, a ⭐ helps other people find it.

## Use responsibly

Only post clips of videos you own, or that the creator allows you to clip (for example through a creator's clipping or affiliate program). Re-uploading other people's streams or videos without permission can lead to Content ID claims and copyright strikes.

Monetization is a separate question: YouTube's [reused-content policy](https://support.google.com/youtube/answer/1311392) is separate from copyright and **applies even if you have permission from the original creator**. Channels that mostly repost others' content with little of their own added can be refused monetization.

Downloading from YouTube may also break YouTube's Terms of Service. You are responsible for how you use this tool.

## License

[MIT](LICENSE)
