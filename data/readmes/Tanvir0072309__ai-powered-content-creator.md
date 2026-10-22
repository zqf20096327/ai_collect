<div align="center">

# PsychClips v2.0

### AI-Powered Hindi/Urdu Psychology Shorts Generator

**Paste URLs → Get a ready video.** Script, voice, and editing are all automatic.

</div>

---

## What Is This?

**PsychClips** is an AI-powered short video generator that automatically creates viral Hindi/Urdu psychology videos — in the style of **YouTube Shorts / Instagram Reels**.

> **The user just pastes URLs → the system automatically:**
> - Generates a script *(Groq AI)*
> - Generates a voiceover *(ElevenLabs / gTTS)*
> - Downloads source videos *(yt-dlp)*
> - Edits and applies filters *(FFmpeg)*
> - Exports the final video

---

## Important: You Need Your Own API Keys

This project **does not come with any API keys built in**. Before you can use it, you must sign up for your own accounts and add your own keys:

| Key | Required? | Where to get it |
|---|---|---|
| **Groq API Key** | Required — used for script generation | [console.groq.com](https://console.groq.com) (free) |
| **ElevenLabs API Key** | Optional — used for premium voice quality | [elevenlabs.io](https://elevenlabs.io) (free tier available) |

If you don't add an ElevenLabs key, the app will automatically fall back to **gTTS (Google TTS)**, which is free and supports Hindi. See the [API Keys](#api-keys-setup) section below for step-by-step instructions.

---

## Skills & Tech Stack Used

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Groq](https://img.shields.io/badge/Groq_AI-F55036?style=for-the-badge&logoColor=white)](https://console.groq.com/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logoColor=white)](https://elevenlabs.io/)
[![Google TTS](https://img.shields.io/badge/gTTS-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://pypi.org/project/gTTS/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)

</div>

| Layer | Skill / Tool | Purpose |
|---|---|---|
| Backend Framework | **Flask** | Job queue, API routes, background threads |
| Script Generation | **Groq AI** *(llama-3.3-70b)* | Generates Hindi script (hook + full script + mood) from a topic |
| Voice Generation | **ElevenLabs** / **gTTS** | Text-to-speech voiceover |
| Video Sourcing | **yt-dlp** | Downloads raw clips from YouTube URLs |
| Video Processing | **FFmpeg** | Trimming, filters, cropping, audio mixing, final export |
| Frontend | **HTML / CSS / JavaScript** | UI, hook chips, settings panel, progress tracking |
| Security | **XOR + Base64 Encryption** | Local API key storage (`.keys.enc`) |
| PWA Support | **Service Worker (`sw.js`)** | Offline-friendly app shell |

---

## System Architecture

```
┌───────────────────────────────────────────────────────────┐
│                    FRONTEND (index.html)                   │
│    Topic Input → Hook Chips → Settings → Progress → DL     │
└──────────────────────────┬──────────────────────────────────┘
                            │ HTTP (JSON)
┌──────────────────────────▼──────────────────────────────────┐
│                   FLASK SERVER (server.py)                   │
│   /start   →  Job Queue  →  Background Thread                │
│   /status  →  Poll Job State                                 │
│   /download → Serve Final Video                              │
└────────┬─────────────┬───────────────────┬────────────────────┘
         │              │                  │
    ┌────▼────┐   ┌─────▼─────┐     ┌──────▼──────┐
    │  Groq    │   │ ElevenLabs │     │  yt-dlp +   │
    │  Script  │   │    TTS     │     │   FFmpeg    │
    └──────────┘   └────────────┘     └─────────────┘
```

### 5-Step Pipeline

| Step | Input | Engine | Output |
|:---:|---|:---:|---|
| **1** | Topic | Groq AI | Hindi Script *(hook + full script + mood)* |
| **2** | YouTube URLs | yt-dlp | Raw MP4 clips + music |
| **3** | Script | ElevenLabs / gTTS | `voiceover.mp3` |
| **4** | Raw clips | FFmpeg | Trimmed + filtered clips |
| **5** | Clips + Voice + Music | FFmpeg Compose | **Final Video** |

---

## Folder Structure

```
psychclips/
│
├── index.html          ← Frontend UI
├── server.py           ← Main Flask Backend
├── setup.py             ← One-time setup script
├── requirements.txt      ← Python dependencies
├── sw.js                ← Service Worker (PWA support)
│
├── outputs/             ← Final videos are saved here
├── temp/                 ← Processing temp files (job_id folders)
│   └── abc12345/
│       ├── raw/          ← Downloaded clips
│       ├── clips/         ← Trimmed + filtered clips
│       ├── concat.mp4     ← Joined video
│       ├── voiceover.mp3
│       └── bg_music.mp3
│
├── music/               ← Local music files (optional)
├── assets/               ← App assets
└── .keys.enc             ← Encrypted API keys (auto-created)
```

---

## Installation

### 1. Prerequisites — Install FFmpeg *(MOST IMPORTANT)*

| OS | Command |
|---|---|
| Windows (winget) | `winget install --id=Gyan.FFmpeg` |
| Windows (choco) | `choco install ffmpeg` |
| Mac | `brew install ffmpeg` |
| Ubuntu/Debian | `sudo apt update && sudo apt install ffmpeg` |

```bash
# Verify install
ffmpeg -version
```

### 2. Python Setup

```bash
# Requires Python 3.9+
python --version

# Create a virtual environment (recommended)
python -m venv venv

# Activate it
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies

```bash
# Automatic setup (recommended)
python setup.py

# Or manually:
pip install flask flask-cors yt-dlp gtts requests
```

### 4. Run the Server

```bash
python server.py
```

Open your browser at: **http://localhost:5000**

---

## API Keys Setup

You must obtain and add these keys yourself before the app will work. No keys are included in this repository.

### Groq API Key — Script Generation *(Required, FREE)*
1. Go to [console.groq.com](https://console.groq.com)
2. Create a free account
3. Click **"Create API Key"**
4. Copy the key: `gsk_xxxxx...`
5. In the app → **Settings → Groq AI** → paste it in

### ElevenLabs API Key — Voice *(Optional, paid)*
1. Go to [elevenlabs.io](https://elevenlabs.io)
2. Create an account (free tier available)
3. Go to **Profile → API Keys → Create**
4. Copy the key: `sk_xxxxx...`
5. In the app → **Settings → ElevenLabs** → paste it in

> **Note:** Don't have an ElevenLabs key? No problem — the app will automatically fall back to **gTTS (Google TTS)**, which is free and supports Hindi.

---

## How to Use the App

| # | Action |
|:-:|---|
| 1 | Start the server → `python server.py` |
| 2 | Open your browser → `http://localhost:5000` |
| 3 | Add your API keys under Settings |
| 4 | Paste the YouTube Shorts URLs you want to use for clips |
| 5 | Enter a topic, or pick one from the Hook Chips |
| 6 | Choose clip count, resolution, and filter |
| 7 | Click **"VIDEO BANAO"** (Generate Video) |
| 8 | Watch progress as the 5 steps complete |
| 9 | Preview the generated script |
| 10 | Download the video, plus copy the description/hashtags |

---

## Key Code Snippets

<details>
<summary><b>Script Generation (Groq)</b></summary>

```python
# Uses Groq's llama-3.3-70b model
# Prompt: topic → JSON output (hook + script + mood)
payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.8  # creativity level
}
```
</details>

<details>
<summary><b>Video Download (yt-dlp)</b></summary>

```python
cmd = [
    "yt-dlp",
    "--format", "bestvideo[ext=mp4]+bestaudio/best[ext=mp4]",
    "--no-playlist",
    "--output", "clip_%(id)s.%(ext)s",
    url
]
subprocess.run(cmd)
```
</details>

<details>
<summary><b>FFmpeg Filter Apply</b></summary>

```python
# Vintage filter example
vf = "curves=vintage,hue=s=0.8,vignette=PI/4"
# + scale to 1080x1920 (vertical)
# + crop to exact size
# + fade in/out transitions
```
</details>

<details>
<summary><b>Audio Mix (Voice + Music)</b></summary>

```python
audio_filter = (
    "[1:a]volume=1.0[voice];"           # Voice 100%
    "[2:a]volume=0.25[music];"          # Music 25%
    "[voice][music]amix=inputs=2[aout]" # Mix both
)
```
</details>

<details>
<summary><b>Encrypted Key Storage</b></summary>

```python
# Keys are XOR-encrypted and stored as base64
def _xor(data, key="psychclips"):
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

# Saved in .keys.enc — never stored as plain text
```
</details>

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `yt-dlp command not found` | `pip install yt-dlp` |
| `ffmpeg not found` | Install FFmpeg (see above) |
| Video download failed | Check the URL — it must not be a private video |
| Voice not generated | `pip install gtts` |
| Can't connect to server | Is `python server.py` running? Is port 5000 free? |
| Blank video | Update your FFmpeg version |
| Keys won't save | Check write permissions on the folder |

---

## Plan to Convert Into a SaaS

<table>
<tr>
<td valign="top" width="33%">

### Phase 1 — Local Tool
*(Current)*
- Single user, local machine
- All free APIs

</td>
<td valign="top" width="33%">

### Phase 2 — Web App
- User auth *(Flask-Login / Supabase)*
- PostgreSQL *(job history)*
- AWS S3 / Cloudflare R2 *(storage)*
- Celery + Redis *(job queue)*
- Deploy: Railway / Render / VPS

</td>
<td valign="top" width="33%">

### Phase 3 — SaaS Product
- Stripe subscriptions:
  - **Free** — 3 videos/mo, gTTS
  - **Pro** — 30 videos/mo, ElevenLabs
  - **Agency** — Unlimited + custom voice
- Multi-language support
- Custom branding
- API access + Dashboard

</td>
</tr>
</table>

### Cost Estimate *(Monthly, 1000 users)*

| Service | Free Tier | Paid |
|---|---|---|
| Groq API | 100 req/min free | Very cheap |
| ElevenLabs | 10K chars/month | $5–22/month |
| Hosting (Railway) | $5/month | Scales |
| Storage (R2) | 10GB free | $0.015/GB |

---

## Important Notes

- **yt-dlp and copyright**: Only use your own videos or royalty-free content
- **Groq free tier**: Very generous — plenty for personal use
- **Video quality**: Depends on the quality of the source video
- **Processing time**: 1–3 minutes per video *(depends on clip count and length)*
- **Disk space**: Temp files are not deleted automatically — clear them manually or set up a cron job

---

## Quick Start *(TL;DR)*

```bash
git clone <repo> && cd psychclips
python setup.py
python server.py
# Open: http://localhost:5000
# Add your own Groq (and optionally ElevenLabs) API key under Settings
# Paste URLs → Generate Video!
```

---

<div align="center">

**PsychClips v2.0** — Built with care for Hindi content creators

`Python` · `Flask` · `FFmpeg` · `Groq` · `ElevenLabs` · `yt-dlp`

</div>
