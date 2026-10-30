# 🎯 Hookshot

**Paste a YouTube link. Get scroll-stopping vertical clips. 100% free, 100% local.**

Hookshot watches a long video or a multi-hour stream, finds the moments most likely to go viral, and turns them into captioned 9:16 clips ready for **YouTube Shorts, TikTok and Instagram Reels**. It's a free, open-source alternative to paid tools like OpusClip: no subscription, no credits, no uploads to anyone's cloud. Everything runs on your own PC.

- **Virality Score for every clip**, with a plain-English reason, e.g. `Score: 82/100 – Strong question hook, high emotional intensity, no dead air, ends on a payoff`
- **Uses YouTube's "Most replayed" data**, the graph of where real viewers rewound, as a scoring signal
- **Local AI judge** (Qwen3 via Ollama) that grades the hook, emotion, payoff and brand safety, and writes titles and hashtags
- **Auto layouts:** follows the speaker's face, or stacks a streamer's facecam over the gameplay
- **TikTok-style word-by-word captions** and an on-screen hook title
- **Post queue with auto-posting:** approve clips and they publish to YouTube Shorts (and TikTok) at your daily time slots
- **Thumbnails for every clip:** 3 vertical covers plus a YouTube thumbnail, built from the most expressive frame, with the person cut out and bold text
- **Built for long streams:** a 4-hour VOD takes about 16 minutes on an RTX-class GPU

---

## ⚡ Quick start (Windows)

### What you need
| | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 / 11 | Windows 11 |
| GPU | Any (runs on CPU, but slowly) | NVIDIA RTX with 8 GB+ VRAM |
| RAM | 16 GB | 32 GB+ |
| Disk | 15 GB free | 30 GB+ free |

### Install (one time, about 10–20 minutes, mostly downloads)
1. **Download Hookshot:** click the green **Code** button above → **Download ZIP**, then extract it somewhere like `C:\Hookshot`.
   (Or, if you use git: `git clone https://github.com/jaxstudio1/hookshot.git`)
2. **Double-click `setup.bat`.** It installs and configures everything for you:
   - [FFmpeg](https://ffmpeg.org/) (video processing), [uv](https://github.com/astral-sh/uv) (Python manager), [Deno](https://deno.com/) (needed by the YouTube downloader) and [Ollama](https://ollama.com/) (runs the local AI), all through `winget`
   - A private Python 3.12 environment inside the Hookshot folder, so nothing else on your PC is touched
   - The Whisper speech model (~1.6 GB), the Qwen3 8B AI model (~5 GB) and the face detection + person cutout models (~175 MB)
   - CUDA libraries if an NVIDIA GPU is found

   If Windows asks for permission to install something, click **Yes**.

### Run it
**Double-click `Start Hookshot.bat`.** Your browser opens. Paste a YouTube link, press **Find clips**, and wait for the preview cards to appear. Leave the black console window open while you use it.

> 💡 Make sure **Ollama is running** (it starts with Windows after setup; look for the llama icon in the system tray). Without it, Hookshot still works but ranks clips on the measured signals alone, with no AI judge.

---

## 🖥️ Using it

![flow](https://img.shields.io/badge/link-%E2%86%92%20download%20%E2%86%92%20transcribe%20%E2%86%92%20score%20%E2%86%92%20AI%20judge%20%E2%86%92%20render-ff5a1f)

**Settings** (the collapsible panel on the page):

| Setting | What it does |
|---|---|
| Number of clips | How many clips to render (runners-up are listed below the cards) |
| Min / Max length | Clip length range in seconds (default 15–60) |
| Layout | `auto` (recommended), `track`, `stack` or `fit`; see [Layouts](#-layouts) |
| Word-by-word captions | Burn in TikTok-style captions |
| Hook title at start | On-screen hook text for the first 3 seconds |
| Brand-safe scoring | Lower scores for slurs and explicit content that platforms limit |
| Thumbnails | Make 3 vertical covers and a YouTube thumbnail for each clip |
| Speech model | `large-v3-turbo` (fast, default) or `large-v3` (most accurate, about 3x slower) |
| Ollama model | Any Ollama model; `qwen3:8b` is the tested default |

You can also paste a **local video file path** instead of a link.

**Output** is saved in `jobs/<video id>/clips_<date-time>/`:
- `01_<title>.mp4` and so on: 1080×1920 H.264, ready to upload
- `01_<title>_cover1.jpg` … `_cover3.jpg`: 1080×1920 covers for Shorts / TikTok / Reels, from three different moments
- `01_<title>_youtube.jpg`: a 1280×720 YouTube thumbnail
- `post_captions.txt`: a title, a credit line and hashtags for each clip, ready to paste
- `clips.json`: timestamps, Virality Scores, the score for each signal, the reasoning and the runners-up

Downloads and transcripts are cached, so a second run on the same video with different settings is quick.

### Command line
```bat
.venv\Scripts\python.exe -m clipper "https://www.youtube.com/watch?v=..." -n 5 --min 15 --max 60
```
Options: `--layout auto|track|stack|fit`, `--no-captions`, `--no-hook`, `--no-thumbnails`, `--allow-unsafe`, `--whisper large-v3`, `--llm <ollama model>`.

Make thumbnails with your own text for any video file:
```bat
.venv\Scripts\python.exe -m clipper.thumbnail "jobs\...\01_my-clip.mp4" --text "HE DID WHAT"
```

---

## 🧠 How the Virality Score works

1. **Download.** [yt-dlp](https://github.com/yt-dlp/yt-dlp) fetches the video (up to 1080p) plus YouTube's **"Most replayed" heatmap**.
2. **Transcribe.** [faster-whisper](https://github.com/SYSTRAN/faster-whisper) produces word-level timestamps. Names from the video title are passed as hotwords so they're spelled correctly.
3. **Score every segment.** Every sentence-aligned 15–60 s segment is scored on measurable signals ([`clipper/scoring.py`](clipper/scoring.py)):

   | Signal | Weight | What it measures |
   |---|---|---|
   | **Hook (first 3s)** | 30% | Questions, bold claims, trigger phrases, "you", numbers, emotional or loud opens. Penalties for opening mid-thought ("and so…"), needing context ("he said…") or a slow start |
   | **Emotion** | 25% | Sentiment intensity of the text ([VADER](https://github.com/cjhutto/vaderSentiment) plus streamer hype words) and vocal energy compared with the rest of the video |
   | **Keywords** | 15% | Density of scroll-stopping trigger words, plus the video's own key topic terms |
   | **Pacing** | 15% | Dead air (gaps that are both silent *and* quiet; loud gameplay doesn't count) and speech rate |
   | **Payoff & context** | 15% | Ends on a finished thought or punchline, and makes sense without the rest of the video |
   | *Most replayed* | 25% of total | When YouTube has it: how much viewers rewatched the clip's peak moment |
   | *Brand safety* | multiplier | Slurs and explicit content reduce reach on every platform |

4. **AI judge.** The best non-overlapping segments go to a local LLM ([Ollama](https://ollama.com/) + `qwen3:8b`), which grades each one 0–10 on hook, emotion, payoff, standalone and brand safety, then writes the title, hook text and hashtags. Its grades are blended with the measured signals.
5. **Render.** Vertical crop, captions and NVENC (GPU) encoding when available.

### Long streams (over 40 minutes)
- **Audio first.** Only the audio is downloaded for analysis. Then just the picked sections are downloaded in 1080p, in parallel, and lined up to the exact frame by matching their audio against the full track. For a 4-hour stream that's about 350 MB instead of 4 GB.
- **Relative scoring.** Scores are half absolute and half ranked against the rest of the same stream, and loudness is compared with the surrounding ~10 minutes, so a big moment stands out even from a streamer who's loud all the time.
- **One clip per moment.** Clips are kept at least 2 minutes apart, and the AI judges about one candidate per 4 minutes of stream (up to 72).

---

## 🎬 Layouts

| Layout | Best for | What it does |
|---|---|---|
| `track` | Podcasts, IRL, talking heads | 9:16 crop that smoothly follows the main face |
| `stack` | Gaming streamers | Facecam panel on top, gameplay below, captions on the divider |
| `fit` | Anything without faces | Whole frame on a blurred, darkened background |

`auto` picks one for each clip using [YuNet](https://github.com/opencv/opencv_zoo/tree/main/models/face_detection_yunet) face detection. It tells a webcam overlay (bottom or corner of the frame) apart from a real on-camera speaker.

---

## 📤 Auto-posting (Post queue)

Every rendered clip lands in the **Post queue** tab for review. Edit the title and description, pick platforms, then:
- **Approve → next slot**: the clip takes the next free daily slot (default **9:00 AM, 1:00 PM and 7:00 PM** in your time zone; change them under *Accounts & schedule → Schedule*)
- **Post now**: goes live in about 2 minutes
- **Skip**: stays out of the queue (you can restore it later)

Use **Import clips from earlier runs** to queue clips you made before this feature existed.

### YouTube Shorts setup (one time)
1. In [Google Cloud Console](https://console.cloud.google.com/apis/credentials), create a project and enable **YouTube Data API v3**.
2. **Google Auth Platform → Audience → Publish app**, so it's *In production*. (In *Testing*, Google expires your sign-in every 7 days. You don't need Google's verification for personal use.)
3. **Clients → Create client → Desktop app**, then download the JSON.
4. In Hookshot: **Post queue → Accounts & schedule → YouTube**, load the JSON and click **Connect YouTube**. Sign in with the channel's Google account. On the "Google hasn't verified this app" screen, choose *Advanced → Go to …* (it's your own app).

Approved clips upload right away as private videos with a scheduled publish time, and **YouTube makes them public at the slot time**, so your PC doesn't need to be on then. The API allows 100 uploads a day. Your credentials stay in `secrets/` and the queue in `data/`; both are gitignored, so they never end up on GitHub.

### TikTok (optional)
1. Create an app at [TikTok for Developers](https://developers.tiktok.com/apps). Add **Login Kit** (Desktop) and the **Content Posting API** with the `video.publish` scope, and register the redirect URI `http://localhost:8765/callback/`.
2. In Hookshot: **Post queue → Accounts & schedule → TikTok**, paste the client key and secret, then click **Connect TikTok**.

Until TikTok audits your app, posts are **private (only you can see them)** and the TikTok account has to be private; this is TikTok's rule for unaudited apps. TikTok's API can't schedule, so **Hookshot must be running at the slot time** for TikTok posts (late posts go out as soon as it starts again).

---

## 🖼️ Thumbnails

For each clip Hookshot:
1. **Picks the frame.** It samples the clip 4 times a second and scores each frame on face size, sharpness, how loud that moment is (reactions mean expressive faces), how frontal the face is, and exposure. The three best moments, at least 1.5 s apart, become the three covers.
2. **Cuts the person out** with [U²-Net human segmentation](https://github.com/xuebinqin/U-2-Net) running locally, then adds a white sticker outline and a soft shadow over a darkened, blurred background.
3. **Frames it for each format.** On the covers the face sits in the upper third, so the text stays clear of TikTok's buttons. On the YouTube thumbnail the face goes on one side and the text on the other. When a streamer's webcam is stuck in a corner, the person is cut out and placed big and centered on a blurred version of the scene.
4. **Adds text.** The AI judge writes 2–4 punchy words (e.g. `HE DID WHAT`), set in Arial Black with a thick outline, with the key word in yellow.

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `setup.bat` says *winget was not found* | Install **App Installer** from the Microsoft Store, then run setup again |
| A tool "isn't recognized" right after setup | Close the window and open a new one (Windows only updates PATH for new windows), then run setup again |
| "Ollama is not running" in the log | Start the **Ollama** app from the Start menu |
| YouTube download errors | Update the downloader: `.venv\Scripts\python.exe -m pip install -U "yt-dlp[default]"` (or re-run `setup.bat`) |
| Transcription is very slow | No NVIDIA GPU was found, so it's using the CPU. Pick `medium` as the speech model in Settings for speed |
| Port 7860 already in use | Hookshot is probably already running; check the other console window |

### macOS / Linux (manual, untested)
Install `ffmpeg`, `uv` and `ollama` with your package manager, then:
```bash
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -r requirements.txt
ollama pull qwen3:8b
.venv/bin/python app.py
```
(On Linux with an NVIDIA GPU, also install `requirements-gpu.txt`.)

---

## ⚖️ Use it responsibly
Hookshot is a tool. What you post is on you.
- **Only clip creators who allow it.** Many streamers run official clipping programs or paid clipping campaigns. Reposting without permission can get your accounts copyright strikes or bans.
- **Always credit the creator.** `post_captions.txt` includes a credit line for every clip.
- Downloading from YouTube may be against YouTube's Terms of Service. Use content you have rights or permission to use.

By using Hookshot you agree to the [Terms of Service](TERMS_OF_SERVICE.md).

## 🔒 Privacy
Hookshot collects **nothing**: no accounts, no analytics, no telemetry, and no uploads. Your videos, transcripts and clips never leave your computer, and the optional analytics in the libraries it uses are switched off. It only goes online to download the videos you ask for and its open-source models. Details are in the [Privacy Policy](PRIVACY_POLICY.md).

## 🙏 Built with
[yt-dlp](https://github.com/yt-dlp/yt-dlp) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [Ollama](https://ollama.com/) · [Qwen3](https://github.com/QwenLM/Qwen3) · [OpenCV](https://opencv.org/) + [YuNet](https://github.com/opencv/opencv_zoo) · [U²-Net](https://github.com/xuebinqin/U-2-Net) via [rembg's model release](https://github.com/danielgatis/rembg) · [VADER](https://github.com/cjhutto/vaderSentiment) · [FFmpeg](https://ffmpeg.org/) · [Gradio](https://www.gradio.app/)

## 📄 License
[MIT](LICENSE). Models and tools that are downloaded during setup keep their own licenses. See also the [Terms of Service](TERMS_OF_SERVICE.md) and the [Privacy Policy](PRIVACY_POLICY.md).
