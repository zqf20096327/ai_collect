<img src="clippy/web/static/brand/logo.svg" alt="Clippy" height="56">

# Clippy: free, open-source AI clipper for TikTok, Shorts and Reels

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/Web-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Whisper](https://img.shields.io/badge/Speech-faster--whisper_large--v3-412991?style=flat)
![Ollama](https://img.shields.io/badge/LLM-Qwen3_14B_via_Ollama-000000?style=flat&logo=ollama&logoColor=white)
![FFmpeg](https://img.shields.io/badge/Video-FFmpeg_NVENC-007808?style=flat&logo=ffmpeg&logoColor=white)
![Captions](https://img.shields.io/badge/Captions-the_video's_own_language-9E1D3E?style=flat)
![Platform](https://img.shields.io/badge/Platform-Windows_%7C_macOS_%7C_Linux-0078D6?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

[![Clippy in one minute: paste a link, get vertical clips with captions, edit them by asking in the chat](docs/assets/demo.gif)](https://clippyai.vercel.app/assets/demo.mp4)

**[Watch the one-minute demo in 4K with sound](https://clippyai.vercel.app/assets/demo.mp4)**: a link goes in,
three captioned clips come out, then one is edited from the chat. The clips are made from a public-domain NASA video;
the long wait is sped up and marked.

**Clippy** turns a video, podcast or stream (YouTube, TikTok, Instagram, Twitch, Kick, Facebook…) into vertical **9:16 clips**: on your own computer, for
free. Paste a link into a ChatGPT-style chat and it:

* **picks the moments with the strongest hooks** with a local LLM (Qwen3-14B through Ollama), ranked against each other,
* **cuts them tight**: dead air and filler words out, cuts on real word boundaries,
* **frames the speaker** with a virtual camera (shot detection, face tracking, active speaker),
* **adds animated word-by-word captions** from the transcript,
* **masters the sound** for phones (voice EQ, compressor, two-pass −14 LUFS),
* and nothing else: a new clip is the moment itself. Everything more (opening text, CTA, music, effects, stickers,
  sound effects, speed, another format, B-roll, joined clips) you **ask for in the chat** (*"start clip 2 two
  seconds earlier and put the opening text on it"*).

No subscription and no upload: fast on an NVIDIA RTX GPU, and it also runs on the CPU.

## Quick start

**One-step install.** In the cloned folder run `powershell -ExecutionPolicy Bypass -File install.ps1` on Windows
(add `-Studio` for the voice isolation extras) or `sh install.sh` on macOS and Linux: it creates the Python
environment, installs the GPU packages when an NVIDIA card is there, sets up the local LLM in Ollama and the `clippy`
command with tab completion. The manual steps are below.

Requirements: Windows 10/11, macOS or Linux, [Python 3.12](https://www.python.org/downloads/), [Node.js](https://nodejs.org/) or
[Deno](https://deno.com/) (for YouTube downloads) and [Ollama](https://ollama.com/) for the local LLM. An NVIDIA
GPU with 12-16 GB VRAM is recommended; ffmpeg ships with the pip packages.

```bat
git clone https://github.com/hajdu-patrik/clippy.git
cd clippy
py -3.12 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pip install -r requirements-gpu.txt   :: NVIDIA GPU (cuBLAS + cuDNN for Whisper)
copy .env.example .env
ollama pull hf.co/Qwen/Qwen3-14B-GGUF:Q6_K
ollama create clippy-qwen3:14b-q6k -f models\Modelfile.qwen3-14b-q6k
bin\clippy install                                            :: the clippy command + tab completion
```

Optional studio extras (~3 GB) for voice isolation and word-level alignment:

```bat
.venv\Scripts\python -m pip install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cu128
.venv\Scripts\python -m pip install -r requirements-ml.txt
```

Open a new terminal, then:

| Command | Purpose |
| --- | --- |
| `clippy start` | start the web app in the background and open it in the browser |
| `clippy down` | stop it completely (running renders too) and free the GPU; `--all` stops Ollama as well |
| `clippy status` | is it running, what is it doing, how much VRAM the model holds |
| `clippy clip <link>` | make clips from the command line (`clippy clip -h` lists every option) |
| `clippy llm [mode]` | show or change the AI (`ollama`, `openrouter`, `claude`, `codex`, `none`); `--model`, `--test` |
| `clippy restart --lan` · `clippy pair` | use it from a phone or tablet on the same Wi-Fi (see below) |
| `clippy restart` · `open` · `logs` · `install` | the rest; bare `clippy` shows the banner and the full list |

**Phone or tablet.** `clippy restart --lan` (or `CLIPPY_LAN=1` in `.env`) also listens on the local network and
prints a one-time pairing link with a QR code (`pip install segno` for the QR code). Open it on the phone on the same
Wi-Fi; it is valid for 10 minutes and once, and the phone keeps a cookie that lets it in afterwards. Unpaired devices,
public addresses and other host names are refused; the computer itself needs no pairing. When Windows asks whether
Python may accept connections, allow private networks only. `clippy pair` gives a new link, `clippy pair --reset`
forgets every paired device.

Tab completion works in PowerShell and in cmd through [Clink](https://chrisant996.github.io/clink/)
(`winget install chrisant996.Clink`, then `clippy install` again). The first run downloads the Whisper model
(≈ 3 GB) and the YuNet face model (~230 KB, checked against a pinned SHA-256).

## How it works

```
link ─► yt-dlp (≤4K SDR + Opus) ─► Demucs voice isolation ─► Whisper large-v3 (hotwords, the video's own language) ─► MMS_FA word alignment
     ─► reactions (loud moments, laughter, action, stream chat) ─► Qwen3 hook scoring + global re-rank ─► tight edit (dead air / fillers out, on the audio envelope and frame grid)
     ─► shot detection + YuNet faces + active speaker ─► virtual camera (spring follow, punch-ins)
     ─► sub-pixel Lanczos 9:16 + ASS captions ─► BT.709 NVENC p7 + voice EQ, compressor, two-pass −14 LUFS
```

| Surface | What you get |
| --- | --- |
| **Web app** (`clippy start`, http://127.0.0.1:7860) | chats on the left, the conversation in the middle; finished clips appear as playable cards with download, copy text and edit |
| **Chat agent** | understands requests in plain words and turns them into jobs: generate, more clips, edit clips (with attached images, music, video or LUTs), delete |
| **Live progress** | queue position, a step bar (download, voice, transcript, timing, picking, render), percentage, detail (*Reading part 3 of 8*, *Clip 2 of 4*) and a self-calibrating time-left estimate |
| **Command line** | `clippy clip` runs the same pipeline without the browser; `--only-select` + `--from-json` let you edit the plan by hand |

Every change becomes a new version (v2, v3…) and older versions stay playable. GPU jobs run one at a time while
you keep chatting. The layout works from 320 px phones to wide desktops, with a swipe drawer, keyboard shortcuts
(`Ctrl+Shift+O`, `/`, `Esc`) and motion that honours *reduce motion*.

**Languages.** Every video is transcribed in its own language: an English video gets English captions and texts,
a Hungarian one Hungarian, a Spanish stream Spanish (any language Whisper knows; an unsure guess falls back to
Hungarian or English, which Whisper sometimes mistakes for Finnish). The language you write to the chat in never
changes that. Ask for another language only when you want it (*"magyar felirattal"*, *"English captions on clip
5"*, `--captions hu`): captions are then translated into Hungarian or English line by line and kept in sync with
the speech. The app, the chat replies and the command line are in English.

## Ready-made prompts

The start screen has four buttons. Each one puts a tested prompt into the message box; add the video link after
"Videó:" / "Video:" (and anything else after "Egyéb kérés:" / "Extra wishes:") and send it. The same button always
gives the same kind of clips: the count, the lengths and the CTA come from the text, everything else from the preset.

| Button | Clips | Framing and sound | Picks |
| --- | --- | --- | --- |
| 🎙️ Podcast | 6 × 30-90 s | follows the speaker, speech tuned, dead air out | standalone opinions, surprising facts, stories with a payoff, banter, confessions |
| 🎮 Gameplay & stream | 5 × 20-75 s | facecam on top, game below (blurred full frame without a facecam), natural sound, quiet parts kept | clutch plays, wins, fails, twists, loud reactions, jokes with chat; peaks found by sound, picture and the stream chat, even without speech |
| 📣 Video & promo | 4 × 15-30 s | follows the speaker, speech tuned, opening text and a CTA | the main benefit, a demo, a strong claim or number, a testimonial (hook → proof → CTA) |
| ⚡ Quick shorts | 3 × 10-25 s | automatic, dead air out | jokes, punchlines, surprising lines and reactions |

**Post text.** Every clip comes with a ready-to-paste post (*Copy text* on the card, and the `.txt` file next to
the video): a one-line teaser ending with an emoji, the comment question, the link of the original video, your own
profiles (YouTube as a follow line, Instagram, TikTok) and hashtags; the curiosity title for YouTube Shorts is listed
under it. Set your profile links once under *Settings, General* (the gear in the sidebar), one per line, e.g.
`TikTok: https://www.tiktok.com/@you`; they stay on your computer in `data/web/settings.json`, and changing them
rewrites every clip's post text.

## Editing in the chat

Ask for a change in your own words and attach what it needs with the paperclip button,
drag and drop or paste: images, music, video and `.cube` LUTs (each file is checked by its content, images are
re-encoded, sizes are capped):

> *"Put my logo in the top right corner of clip 2 and this song under it, quietly."*
> *"A 3. klipről vedd le a nyitó feliratot, a feliratok legyenek nagyobbak, sárga kiemeléssel."*
> *"Amikor azt mondja, hogy pénz, legyen ráközelítés és egy dörrenés, a végét lassítsd le, és tegyél fel egy 🔥-t."*
> *"Make it 16:9 for YouTube and put clip 3 after it with a slide."*

You never edit by hand: you say what you want, Clippy does it. Every clip has a **timeline**: the cut, the virtual
camera, the format, the speed, captions, opening and call-to-action texts, overlays, stickers, effects, sounds,
colour, music, B-roll, joined clips and intro / outro. The local LLM turns a request into a short list of validated
edit operations, Clippy applies them as a dry run first and asks back when something is unclear. The result is a new
version with a **change card** listing what changed and a one-click **undo**.

| What you can ask for | Examples |
| --- | --- |
| texts | add, rewrite, move or remove; opening text and CTA; appearing with a fade, pop, slide or typewriter effect |
| captions | size, colour, highlight, height, language, hide, fix a misheard word |
| cut | start earlier / end later, cut out a part, hide the jump with a flash, a dip to black or a zoom |
| speed | slow motion or faster, for the whole clip or a part (the voice keeps its pitch) |
| format | 9:16 (TikTok, Shorts, Reels), 1:1 and 4:5 (feed posts), 16:9 (YouTube: the whole source frame) |
| effects | punch-in zoom, shake, flash, dip to black, black and white, blur, vignette, at a word or a second |
| stickers | any emoji in colour, with a pop, bounce, float or fade |
| sound | music with ducking, sound effects (pop, ding, boom, click, whoosh, riser, bleep) or your own file at a moment, speech volume |
| pictures and video | logo or image overlay, B-roll from an attached video (full frame or small), colour, LUTs |
| sequence | intro / outro with a transition, other clips of the chat joined after this one |
| other | framing, dead-air cutting, sound processing, post title, undo |

Rendering is split in two: the camera-framed **base** is rendered once per cut and cached, every later caption,
colour, overlay or music edit only re-runs a fast finishing pass (about 7 s for a 1080p clip instead of a full
re-render). Older versions stay playable.

## Posting

A finished clip goes straight to your own YouTube, Instagram, Facebook Page, TikTok and X with the **Post** button on
its card, or from the chat (*"posztold ki a 2. klipet YouTube-ra"*). It goes up with its post text and, on YouTube, its
title; the card then links each post. You make a free developer app per platform once and sign in on the platform's own
page: the tokens stay in `data/web/accounts.json` on this computer. *Settings, Accounts* shows all seven platforms as
cards. **Twitch and Kick** can be connected, but neither offers apps any way to upload a video, so Clippy does not post
there (and uses no unofficial way). TikTok sends the clip to your drafts (or posts it as private until it reviews your
app); YouTube may keep uploads of a new API project private until its audit; X's API is paid per use. Setup, step by
step, with what each platform allows: **[docs/publishing.md](docs/publishing.md)**.

## Voice input and notifications

The microphone button next to Send turns your speech into the message (a small Whisper model on the CPU, so it never
waits for a running job). *Settings, General* lets the browser tell you when a job is done, also when the
window is in the background. Both need a secure page: they work on the computer that runs Clippy
(http://127.0.0.1); a phone over the local network cannot use the microphone or notifications without HTTPS.

## Style kit, covers and A/B titles

*Settings, Style* saves your look once: caption font, highlight colour and capitals, and if you want a logo (with
its corner), a short intro and an outro; none of them is required. Every new clip gets the caption look at once, and
the logo, intro and outro as its next version (with a change card and undo). Every clip also gets a cover with its
title written on it (*Cover* on the card) and a second cover with a B title (*Cover B*); the Post dialog lets you
post the A or the B title to YouTube. Hungarian titles,
teasers and questions get a native editor's proofreading pass and Hungarian quotation marks.

Streams (Twitch and Kick VODs, YouTube streams that were live) use the stream layout by default: the facecam on top,
the game below, or the blurred full frame when there is no facecam.

## Watching channels and planned posts

Give Clippy a YouTube channel, a Twitch channel or a playlist under *Settings, Automation*, or say it in the
chat (*"figyeld ezt a gaming csatornát: https://www.twitch.tv/…"*). It looks for new videos every 15 minutes to once
a day; each new video becomes its own chat that makes clips with the kind you chose (podcast, gameplay & stream, video
& promo, quick shorts). Videos already on the channel are left alone; tick *Clip the newest video now too* for one
right away. A YouTube channel is read from its uploads and its past streams; live streams wait until they have ended.

**A streamer by name.** Say *"klippeld N3on legújabb streamjét"* or *"clip the latest stream of Kai Cenat"* in the
chat, no link needed. Clippy knows about fifty of the biggest streamers (Kai Cenat, IShowSpeed, xQc, Adin Ross, N3on,
Ibai, Jynxzi and more, in `clippy/streamers.py`), looks on their YouTube, Twitch and Kick channels for the newest stream
that has ended (one that is on right now gives way to the one before it) and clips it with the gameplay & stream kind;
the reply says which stream it picked. A number works too (*"5 klipet"*), and a name that is not in the list can be given
as `twitch.tv/name`, `kick.com/name` or `@name`. Kick's stream list is read with yt-dlp, and from Kick's public JSON when
yt-dlp cannot.

**Daily picks.** Say *"minden nap 3 GTA VI klipet"* or *"every day 3 GTA VI clips"* (or start it under *Settings,
Automation*): every morning at 09:00 Clippy takes the most watched clips of the last day in that game's Twitch and
Kick category, which are the streamers' biggest live reactions, keeps one per streamer in the audience's language,
and makes a vertical clip of each in its own chat, with the stream layout and a post text that credits the streamer.
Each pick comes with a time to post it for a US audience (New York 19:00, 15:00 and 12:00 by default, the most
watched moment first), shown in your own time too; *Settings, Automation* lists today's picks with their times and
a *Copy text* button. Tick YouTube under *Post each clip at its time* and every pick also goes out by itself:
YouTube gets it as soon as it is made and publishes it at its time. GTA VI, GTA V, Minecraft, Fortnite, Valorant, Counter-Strike, League of Legends and Warzone are
known by name (`clippy/categories.py`).

Posts can wait for their time: choose *At a set time* in the Post dialog, and the card shows the planned post with a
*cancel* link. The **Scheduler** (in the sidebar) lists everything that waits, day by day, with each clip's cover, chat,
platforms and time, and schedules a clip from one place: pick the chat and clip, the platforms, a date and time (or your
saved posting times, *Settings, General*, and the next free one). YouTube keeps its time itself, so that video goes out
even while this computer is off; the other platforms wait in Clippy's plan, which has to be running, and can be moved
or removed in the Scheduler. A YouTube video's time is changed or removed in YouTube Studio (Clippy's YouTube access can
upload but not edit), and the Scheduler links there. A watched channel can also post its new clips by itself: give it the platforms and the daily times
(*18:00, 21:00*) and each new clip takes the next free time, one clip per time across all channels. That is off until
you set both, and it uses your own connected accounts (YouTube public, TikTok drafts).

**Learning from the results.** The numbers of every post (views, likes, comments, shares, how much people watch)
come back onto its card, and *Settings, Results* shows which openings, lengths, kinds of moment and posting times
do better than your usual. The clear patterns steer the picker for the next videos.

## Choosing the AI

The AI picks the moments and writes the titles and texts. You choose it the first time you start (the web app asks
once, `clippy install` asks too) and can change it any time in *Settings, AI* or with `clippy llm <mode>`; the next
request uses it, no restart needed.

| Mode | What it uses |
| --- | --- |
| `ollama` (default) | a model on your own computer, free and private ([docs/local-llm.md](docs/local-llm.md)) |
| `openrouter` | [OpenRouter](https://openrouter.ai) with your own API key; model ids ending in `:free` cost nothing |
| `claude` | your Claude subscription, through the Claude Code app (`claude` signed in once; no API key) |
| `codex` | your ChatGPT subscription, through the Codex app (`codex login` once; no API key) |
| `none` | no AI: simple automatic picking, and the chat cannot answer |

*Settings, AI* shows whether the chosen tool is installed and signed in and has a *Test* button that asks the AI one
tiny question. The choice, the model of each mode and an OpenRouter key are kept in `data/web/llm.json` (never in the
repository); a key is never shown again, and the AI can only be changed on the computer that runs Clippy. The two
subscription modes run the tools without tools or file access of their own and without an API key; their use counts
against your subscription's limits.

## Configuration

`.env` (copied from [.env.example](.env.example)) and environment variables. The AI chosen in Settings or with
`clippy llm` wins over the `CLIPPY_LLM_*` variables, which stay as the defaults before anyone chose:

| Variable | Default | Meaning |
| --- | --- | --- |
| `CLIPPY_LLM_BACKEND` | `ollama` | `ollama` (local), `openrouter`, `claude`, `codex`, `openai` (any OpenAI-compatible API: Groq, Gemini) or `none` (heuristic) |
| `CLIPPY_LLM_MODEL` | `clippy-qwen3:14b-q6k` | the model name for that backend |
| `CLIPPY_LLM_BASE_URL`, `CLIPPY_LLM_API_KEY` | - | for hosted backends |
| `CLIPPY_LLM_THINK` | `1` | reasoning mode when picking clips (better choices, slower) |
| `CLIPPY_LLM_CTX`, `CLIPPY_LLM_KEEP_ALIVE` | `16384`, `30m` | context size and how long the model stays in VRAM |
| `CLIPPY_LIBRARY` | `~/Videos/Clippy` | where finished clips are copied |
| `CLIPPY_PORT` | `7860` | web app port |
| `CLIPPY_LAN` | - | `1`: phones and tablets on the same Wi-Fi can use it after pairing (`clippy pair`) |
| `CLIPPY_BROWSER` | Opera GX, else Edge / Chrome / default | browser to open the UI in |
| `CLIPPY_COOKIES_FROM_BROWSER` | - | `firefox` (or another browser) when a site only shows a video to signed-in users (Instagram, Vimeo, Reddit…); Chrome's cookies cannot be read on Windows |
| `CLIPPY_COOKIES_FILE` | - | a `cookies.txt` (Netscape format) exported from any signed-in browser with an extension; Clippy only reads it, each download uses a private copy. Keep it in `data/` (ignored), it is as good as your login |
| `CLIPPY_YOUTUBE_CLIENT_ID`, `CLIPPY_YOUTUBE_CLIENT_SECRET` | - | your Google "Desktop app" OAuth client, for posting to YouTube ([docs/publishing.md](docs/publishing.md)) |
| `CLIPPY_TIKTOK_CLIENT_KEY`, `CLIPPY_TIKTOK_CLIENT_SECRET` | - | your TikTok developer app, for posting to TikTok |
| `CLIPPY_FACEBOOK_APP_ID`, `CLIPPY_FACEBOOK_APP_SECRET` | - | your Meta app, for posting Reels to a Facebook Page (optional `CLIPPY_FACEBOOK_PAGE_ID`, `CLIPPY_FACEBOOK_CONFIG_ID`) |
| `CLIPPY_X_CLIENT_ID` | - | your X developer app's client id, for posting to X (optional `CLIPPY_X_CLIENT_SECRET` for a confidential app) |
| `CLIPPY_TWITCH_CLIENT_ID`, `CLIPPY_TWITCH_CLIENT_SECRET`, `CLIPPY_KICK_CLIENT_ID`, `CLIPPY_KICK_CLIENT_SECRET` | - | your Twitch / Kick developer apps, only to connect the account (neither platform lets apps upload videos) |
| `CLIPPY_WORKERS`, `CLIPPY_RENDER_SLOTS` | `3`, `3` | jobs of different chats at once, clips rendered at once (the GPU always runs one heavy model at a time) |

**Where files go.** Finished clips: `<CLIPPY_LIBRARY>\<video title>\` (mp4 + cover jpg + post text), never removed
automatically. Everything else lives in `data/`: the shared download / audio / transcript cache, one folder per
chat (removed with the chat, together with any cache no other chat uses), command-line plans and the chat database.

## Guides

* **[docs/cli.md](docs/cli.md)**: every command and `clippy clip` option, with examples.
* **[docs/publishing.md](docs/publishing.md)**: connecting YouTube, Instagram, Facebook, TikTok, X, Twitch and Kick (posting on the first five).
* **[docs/playbook.md](docs/playbook.md)**: what works on TikTok, Shorts and Reels (hooks, length, captions, CTA,
  posting, rights) and where Clippy applies it.
* **[docs/quality.md](docs/quality.md)**: what each stage does for the picture, the sound and the captions, and how hooks are scored.
* **[docs/local-llm.md](docs/local-llm.md)**: Qwen3-14B Q6_K tuned for a 16 GB GPU: quantisation, context, sampling, VRAM scheduling.
* **[docs/BRAND.md](docs/BRAND.md)**: the logo, colours, type and motion rules (icons and the social image are
  regenerated with `dev/make_icons.py` and `dev/make_og.py`).

## Security

The web app listens on `127.0.0.1` only (with `--lan` also on the local network, for paired devices only: a one-time
code becomes an HttpOnly, SameSite=Strict device cookie whose hash alone is stored) and is hardened against the OWASP Top 10 risks that apply to it: a host
allow-list (DNS rebinding), a same-origin check plus a custom header on every state-changing request (CSRF), a strict
Content-Security-Policy with no inline script or style, a media endpoint that serves only a chat's own clip files,
SSRF filtering of video links, parameterised SQL, a pinned hash for the downloaded face model and prompt-injection
guards (transcript text is fenced as data; deleting, downloading or posting needs the user's own words).
Accounts for posting are connected from this computer only, with a single-use sign-in state and PKCE; their tokens
never reach the browser.
Dependencies are checked with `pip-audit`.

## Development

```
clippy/            the package: control.py (the clippy command), shell.py, cli.py, pipeline.py, i18n.py, ...
clippy/web/        FastAPI server, chat service, job runner + live progress, chat agent, static/ (ES modules)
tests/             pytest suite (~3 s)            docs/   guides            models/   Ollama Modelfile
```

```bat
.venv\Scripts\python -m pip install -e .[dev]
git config core.hooksPath .githooks          :: pre-commit: pyflakes + pytest
.venv\Scripts\python -m pyflakes clippy tests
.venv\Scripts\python -m pytest -q
```

Conventions: [CLAUDE.md](CLAUDE.md). Release history: [CHANGELOG.md](CHANGELOG.md).

## Limitations

* Windows-first: it is used and tuned on Windows 10/11 with an NVIDIA GPU. macOS and Linux run the same code (tested
  in CI on both, `install.sh`, bash completion); there the encoder falls back to x264 unless NVENC is available, and
  captions use the system's fonts (DejaVu or Liberation on Linux).
* The camera follows the active speaker by mouth motion; the voices are told apart only for picking (who says
  what), by a light voice print that labels speakers only when their voices clearly differ.
* The interface is in English. Videos are transcribed and captioned in their own language; caption translation
  works between English and Hungarian, and words in non-Latin scripts keep Whisper's timing.
* Post and monetise only your own footage, footage you have permission for, or content from an official clipping
  campaign. Downloading may be restricted by a platform's terms of service.

## FAQ

**What is Clippy?** A free, open-source AI clipper that runs on your own computer: paste a video link (YouTube, TikTok, Instagram, Twitch and the other sites yt-dlp supports) or a video
file) into a chat and get vertical 9:16 clips for TikTok, YouTube Shorts and Instagram Reels, with the strongest hooks,
animated captions and a call to action.

**Is it really free and private?** Yes. MIT license, local models only (faster-whisper, Qwen3-14B through Ollama,
FFmpeg), no subscription and no upload.

**Which languages?** Every video is transcribed and captioned in its own language. The interface is in English, and
captions can be translated between English and Hungarian.

**Can I edit a clip after it is made?** Yes, by asking in the chat: music, logos, texts, colours, LUTs, intro / outro,
cutting parts out, undo. Edits re-render in seconds from a cached base.

**What hardware?** Windows 10/11, macOS or Linux with Python 3.12; an NVIDIA GPU with 12-16 GB VRAM is recommended, the
CPU works too.

Project page: [clippyai.vercel.app](https://clippyai.vercel.app/) · machine-readable summary:
[llms.txt](docs/llms.txt).

## License

[MIT](LICENSE.md). Clippy is not affiliated with Microsoft; product and model names are trademarks of their
respective owners, and the models it downloads come under their own licenses.
