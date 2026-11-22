# ✂️ ClipCutter

**Any video or stream → viral 9:16 clips, automatically.** Paste a YouTube, Twitch or Kick link. ClipCutter
finds the best moments and cuts them to vertical clips with a **hook up front** and **Gen Z word-pop captions**
(English + Hindi). It also writes the title, post caption and hashtags.

Free and local: it runs on your own computer. No subscription, no upload limits.

### Easiest: download the app

**[Download ClipCutter for Mac or Windows](https://github.com/pandeymynk/clipcutter/releases/latest)**, install,
double-click. Nothing else to set up. First-open security warnings and how to get past them:
**[docs/INSTALL.md](docs/INSTALL.md)**.

### From source (developers)

```bash
git clone https://github.com/pandeymynk/clipcutter.git && cd clipcutter
bash scripts/setup.sh            # Windows: powershell -ExecutionPolicy Bypass -File scripts\setup.ps1
uv run clipcutter serve          # open http://localhost:8787
```

Full guide for macOS, Windows and Linux: **[docs/SETUP.md](docs/SETUP.md)** · 📄 [PDF version](docs/ClipCutter-Setup-Guide.pdf)

---

## What each clip looks like

| part | what happens |
|---|---|
| **Hook** (first ~2.5 s) | the peak moment, zoomed in, with big hook text ("bhai GTA 6 mein ye bhi hai?? 😳") and a bass boom |
| **Main** | rewinds to the setup, then plays build-up → payoff |
| **Captions** | 1–3 words at a time, spoken word highlighted, emoji on reactions. Hindi (Devanagari) supported |
| **Layout** | automatic: facecam on top + gameplay below when there's a webcam, otherwise gameplay over a blurred background |
| **Output** | 1080×1920 MP4, loudness normalized for TikTok / Shorts / Reels, plus a `.json` with title, caption and hashtags |

## Features

- 🔗 **Any link**: YouTube, Twitch, Kick and ~1000 sites (via yt-dlp), or a local video file
- ⚡ **Fast**: downloads the video once and uses the platform's own captions when available (no speech-to-text wait)
- 🎯 **Moment detection**: loudness spikes, chat spam spikes (when a chat log exists), hype words in English and Hindi, fast cuts
- 📈 **Virality score** (0–99) on every clip
- 👀 **Creator tracker**: add channels and their new videos get clipped automatically. `discover` finds popular channels for a topic
- 🖥️ **Web app**: paste a link, watch a live progress bar, and see clips appear as they're made. Copy caption, download
- 🗣️ **Gen Z style** by default (`genz`), or `hype` / `clean`. Hinglish hooks for Hindi videos
- 🤖 **Optional AI hooks** with Claude or a free local model (Ollama)
- 🤝 **Agent-ready**: works with Antigravity, Claude Code, Cursor and others ([AGENTS.md](AGENTS.md))

## Website (multi-user, deployable)

A full web app with a landing page, accounts, monthly plans, a moment preview, a built-in editor (hook text, captions, trim,
layout) and phone install (PWA). Even 24-hour streams work: it reads captions, chat and the "most replayed" graph,
then downloads only the minute that becomes a clip.

```bash
uv run clipcutter site            # http://localhost:8000
uv run clipcutter site-worker     # background worker
```
Deploy on a free Oracle Cloud server or Hetzner: [docs/DEPLOY.md](docs/DEPLOY.md) · design: [docs/SYSTEM_DESIGN.md](docs/SYSTEM_DESIGN.md)

## Live mode: clip while the stream is still live

```bash
uv run clipcutter live https://www.twitch.tv/<channel>          # or a YouTube live link, or kick.com/<channel>
```
The stream is recorded in 5-minute chunks (no re-encode) while chat is captured live (Twitch IRC, YouTube live
chat). Every finished chunk is scored (loudness + smart chat votes: one viewer can't spam a highlight, super
chats/gifts count more, sudden bursts get a bonus), and only strong moments become clips, about 5 minutes behind
the stream. On the website: **Create → Live clipping → Start**. Clips show up in My clips as they're made.

## Command line

```bash
uv run clipcutter run "https://www.youtube.com/watch?v=..." --clips 3
uv run clipcutter discover "gta 6 live"
uv run clipcutter add https://www.youtube.com/@channel --keyword gta
uv run clipcutter track --every 30
uv run clipcutter doctor          # check your install
```

Settings: copy `config.example.yaml` to `config.yaml`.

## How it works

1. **Download** the video and its captions (or chat replay) with yt-dlp.
2. **Transcript** from the platform's captions, or local speech-to-text (Whisper) when there are none.
3. **Score** every second (audio, chat, speech, visuals) → pick the top moments → snap them to full sentences.
4. **Write** the hook, title and caption (templates, or an LLM if configured).
5. **Render** with ffmpeg: hook segment + main segment + layout + caption overlay + sound + loudness.

Roadmap and competitor comparison: [PLAN.md](PLAN.md).

## Responsible use

Only post clips of content you own or have permission to use (for example, a streamer's official clipper
program). Each tracked creator has a `permission` flag for this.
