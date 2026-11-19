<div align="center">

# 🎬 Clip Agent

**An AI agent that runs a gaming clip channel for you: finds the best moments, edits them into original vertical shorts, credits every creator and queues them for TikTok, Reels and Shorts. Ships with a GTA 6 preset.**

[![Claude Code](https://img.shields.io/badge/Claude_Code-Agent-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.com/claude-code)
[![Python](https://img.shields.io/badge/Python-≥3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Video-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![Whisper](https://img.shields.io/badge/Captions-Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/SYSTRAN/faster-whisper)
[![Preset](https://img.shields.io/badge/Preset-GTA_6-FF5BA7?style=for-the-badge)](presets/gta6.json)
[![Buffer](https://img.shields.io/badge/Publish-Buffer-231F20?style=for-the-badge&logo=buffer&logoColor=white)](https://buffer.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## What is this?

Running a clip channel means hours of watching streams, cutting moments, reframing them to 9:16, adding
captions, writing titles and posting on three platforms every day. This repo turns that into a
conversation. Open the folder in [Claude Code](https://claude.com/claude-code), tell the agent what you
want ("make shorts from today's best Twitch clips"), and it does the work. It finds the
moments, edits them, credits the creators, writes captions and queues the posts after you approve them.

It works for any game or streamer niche. A **GTA 6 preset** is included, so it's ready for launch day;
for another game, the setup guide creates a preset with you in a minute.

The first time you open it, the agent becomes a **setup guide**. It asks which game you clip, checks your PC, helps you pick a
channel name that's still free, walks you through every account you need, and generates your profile
picture and banner.

---

## ✨ Features

| | |
|---|---|
| 🔥 **Chat spike finder** | Downloads a stream's chat replay and finds the seconds where chat exploded, which is where the highlight is |
| 🎮 **Any game, GTA 6 ready** | Game presets set the Twitch category, spoiler text and hashtags. GTA 6 included |
| 🧠 **Cuts that make sense** | Reads the transcript and picks complete moments with a point. Never cuts someone off mid-sentence |
| 📺 **4 clip sources** | Top Twitch clips of the day, Twitch VODs, live streams (records video + chat), YouTube, and your own gameplay |
| 📱 **Auto 9:16 edit** | Detects the streamer's webcam: **facecam on top, gameplay below**. Pure gameplay gets a zoomed, blurred-background layout |
| 💬 **Word-by-word captions** | Whisper runs locally and free, with GPU acceleration on NVIDIA cards |
| 🗣️ **Human-sounding voiceover** | Free local [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) voices, male and female, with captions |
| ⚠️ **Game-style spoiler card** | Red "SPOILER WARNING" with a 3-2-1 countdown before story clips |
| 💥 **Effects** | Hook title, screen shake and flash on loud moments, music that ducks under voices, loudness normalised for social |
| 🏷️ **Credits everyone** | Creator tag on screen and in every caption, plus @tags. One command removes everything from a creator who asks |
| ✅ **Human approval** | Nothing is posted until you say yes |
| 📅 **Publishing** | Covers, per-platform captions and hashtags, Buffer queue, posting-time suggestions, calendar reminders |
| 🎨 **Channel setup** | Free channel-name check, AI profile picture, banners and thumbnails |
| 🎬 **Compilations** | 16:9 YouTube compilations with per-clip credits |

---

## 🏗️ How it works

```
 you: "make 3 shorts from today's top clips"
                         │
                         ▼
              Claude Code agent (CLAUDE.md)
                         │  runs  python -m clipagent …
   ┌──────────────┬──────┴───────┬────────────────┐
   ▼              ▼              ▼                ▼
 FIND           PICK           EDIT            PUBLISH
 ─────          ─────          ─────           ───────
 Twitch clips   chat spikes    facecam split   cover + captions
 Twitch VODs    transcript     captions        creator credits
 live + chat    audio peaks    voiceover       you approve ✅
 YouTube        frame scan     spoiler card    Buffer queue
 your inbox/                   effects, music  calendar reminder
```

1. **Find:** the Twitch API for top clips and VODs, yt-dlp for YouTube, streamlink plus anonymous
   Twitch chat for live streams. Every clip is saved with who made it.
2. **Pick:** chat messages per 5 s are compared to a rolling baseline, and hype words (KEKW, CLIP IT…)
   count extra. Spikes become 15-45 s windows. For videos, the agent reads the transcript and picks one
   complete thought with a payoff, checked against the frames; loud-audio peaks help with footage without talking.
3. **Edit:** the agent writes a small `plan.json` (segments, layout, hook, voiceover script), and FFmpeg
   renders it in two passes. Pass one handles layout, captions, credit and effects; pass two handles the
   spoiler card, hook, voiceover and music. NVENC is used on NVIDIA GPUs (~1.5 min per short on an RTX 3060).
4. **Publish:** `package` builds the cover and captions with a credits block. After your OK, posts go
   to Buffer through its website or its beta API.

### 🔎 How it finds moments

Every signal gives a score for each second of video. The scores are weighted and added, and a second that
crosses the threshold becomes a clip window (about 22 s before the peak and 14 s after). Weights live in the game preset
(`presets/gta6.json`, `"signals"` block). Run it on any recording:
`python -m clipagent spikes multi <video> --chat <chat.json> --signals chat,audio,event,speech,screen`

| Signal | What it measures | In `spikes multi` by default |
|---|---|---|
| 💬 **Chat speed** | Messages per second against the stream's own rolling baseline (robust z-score), shifted back ~6 s because chat reacts late | yes |
| 🔥 **Hype words** | Chat lines with KEKW, CLIP IT, NO WAY, OMEGALUL… count 2.5× a normal message. Sub, raid, giveaway and greeting floods are filtered out | yes |
| 🔊 **Voice volume** | The streamer's loudness (dB) jumping above a rolling 3-minute median: shouting, screaming, laughing. Gunfire alone can't trigger a clip, it only boosts the others | yes |
| 🌫️ **Grey screen (generic)** | A sudden, lasting drop in colour saturation, the way many games grey out on death. Game-agnostic, so it also fires on black fades and night scenes: of 43 saved GTA 6 moments where it fired, none was a death screen. For GTA 6 use the screen plugin below | yes |
| 🗣️ **Speech keywords** | Hype phrases the streamer says in the Whisper transcript: "no way", "let's go", "oh my god", "what the…", "да ладно", "ничего себе"… | no: `config signals_speech=true` |
| 💀 **GTA 6 screen events** | Full-screen game text found by template matching on edge maps (`clipagent/gta6screen.py`). Ships with the real GTA 6 **wasted** and **busted** screens, cut from live streams; add more (mission passed…) from your own recordings with `screen-template` | no: `config signals_gta6_screen=true` |
| 🎯 **Combined score** | `chat×1.0 + volume×0.45 + grey-screen×3 + speech×0.8 + screen×4`, threshold 4. A death screen alone is a moment; volume and speech only boost | — |

Templates: `python -m clipagent screen-template <video> <second> wasted` cuts the text from a real frame, and
`python -m clipagent screen-events <video>` lists what it finds. Without templates the screen plugin does nothing.

---

## 🚀 Quick Start

**Prerequisites:** [Claude Code](https://claude.com/claude-code), Python 3.10+, [FFmpeg](https://ffmpeg.org/download.html).
An NVIDIA GPU is recommended but not required.

### 1. Clone

```bash
git clone https://github.com/mishgoldenberg/clip-agent.git
```

```bash
cd clip-agent
```

### 2. Install

```bash
python -m venv .venv
```

```bash
.venv/Scripts/python -m pip install -r requirements.txt
```

On Mac/Linux use `.venv/bin/python`.

### 3. Download the human voices (optional, ~350 MB)

```bash
mkdir models && curl -L -o models/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && curl -L -o models/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```

### 4. Open it in Claude Code and say "set me up"

The agent takes it from there: game preset (say "GTA 6" to use the built-in one), PC check, channel name, accounts, API keys, brand images, music, posting
schedule.

---

## 💬 Talk to it like this

- "Get the top 10 Twitch clips for my game from today and make shorts from the best 3"
- "Find the craziest moments in this streamer's last VOD using chat spikes"
- "Record this stream for an hour and clip the best part"
- "I put my stunt recordings in the inbox, make a short with a funny voiceover"
- "Make a 10-minute compilation of this week's best fails for YouTube"
- "Queue the approved shorts for tomorrow evening"
- "This streamer asked me to remove his clips"

---

## ⚙️ Configuration Reference

### Keys (`.env`)

| Variable | Needed for | Get it |
|---|---|---|
| `TWITCH_CLIENT_ID` / `TWITCH_CLIENT_SECRET` | Twitch clips, VODs, chat | [dev.twitch.tv/console/apps](https://dev.twitch.tv/console/apps) |
| `BUFFER_API_KEY` | Buffer API route (optional) | [publish.buffer.com/settings/api](https://publish.buffer.com/settings/api) |
| `GEMINI_API_KEY` | Better brand images (optional) | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |

### Game presets (`python -m clipagent preset gta6`)

A preset is a small JSON file in [`presets/`](presets) with the exact Twitch category, a short name for
titles, the spoiler-card text, default hashtags, YouTube search ideas and hook examples.
[`gta6.json`](presets/gta6.json) ships with the repo; copy [`_template.json`](presets/_template.json) for
another game, or just tell the agent which game you clip.

### Settings (`python -m clipagent config key=value`)

| Key | Default | What it does |
|---|---|---|
| `voice_male` / `voice_female` | `am_michael` / `af_heart` | Voiceover voices (`voices` lists all) |
| `credit_mode` | `corner` | `corner`, `intro` ("CLIP: …" card) or `both` |
| `spoiler_default` | `true` | Spoiler card on new posts |
| `max_seconds` | `59` | Max short length |
| `post_times` | `["12:00","18:00","21:00"]` | Posting slots |
| `whisper_model` | `auto` | `medium` on GPU, `small` on CPU |
| `encoder` | `auto` | NVENC if available, else x264 |
| `buffer_media_url_prefix` | empty | Public URL that mirrors `output/` (Buffer API video upload) |
| `signals_speech` | `false` | Add the streamer's hype phrases (Whisper transcript) to `spikes multi` |
| `signals_gta6_screen` | `false` | Add GTA 6 full-screen text events (templates in `presets/gta6_screens/`) to `spikes multi` |

---

## 🗂️ Project Structure

```
CLAUDE.md            the agent's brain: rules, setup guide, workflows
presets/             game presets (gta6.json + _template.json)
.claude/skills/      /setup /find-clips /make-short /compilation /publish /takedown
clipagent/
  twitch.py          top clips, VODs, chat replay (Helix API)
  live.py            record live stream + chat
  youtube.py         search, download, credit metadata
  spikes.py          chat / audio highlight finder
  layout.py          webcam detection
  transcribe.py      Whisper word timings
  tts.py             Kokoro / Edge voiceover
  subs.py            captions, hook, credit, spoiler card (ASS)
  render.py          FFmpeg two-pass renderer
  publish.py         package, approve, Buffer, reminders
  brand.py           profile, banners, covers
  names.py           channel-name availability
  takedown.py        blocklist + removal list
inbox/               drop your own recordings here
library/  output/    downloaded clips / finished posts (git-ignored)
music/  brand/       your tracks + credits.json / fonts and images
```

---

## ⚖️ Using other people's clips

Reusing streamers' and YouTubers' footage can get copyright claims. The agent credits every creator
on screen and in captions, makes each clip transformative (captions, commentary, edits), and removes
everything from a creator who objects in one step. It's still your channel and your responsibility.
Many streamers welcome clip channels; when in doubt, ask. Use no-copyright music, or add trending sounds
inside TikTok and Instagram.

---

## 📄 License

[MIT](LICENSE) © 2026 Michael Goldenberg
