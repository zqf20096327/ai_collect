<p align="center">
  <img src="src/pgw/templates/logo.png" width="400" alt="PolyglotWhisperer logo">
</p>

<h1 align="center">PolyglotWhisperer</h1>

<p align="center">
  Turn any video into a language-learning tool.<br>
  Transcribe, translate, and study — all in one pipeline.
</p>

---

## What it does

Give it a video — any video. A YouTube link, a file on your computer, a Swiss news broadcast. It will:

1. **Transcribe** the speech into subtitles (in the original language)
2. **Refine** the transcription (fixing grammar, filling gaps)
3. **Translate** everything into your target language
4. **Analyse vocabulary** — which words are rare, which are common, your CEFR level
5. **Export** everything as bilingual subtitles, PDFs, or EPUBs for offline reading

Then open the web interface and **play the video with dual subtitles**, click any word to see its difficulty and save it as a flashcard, and review your flashcards with spaced repetition.

No GPU needed — you can run everything through cloud APIs in a few clicks.

---

## Quick start

```bash
git clone https://github.com/RizhongLin/PolyglotWhisperer.git
cd PolyglotWhisperer
uv sync --all-extras
```

You'll need [Python 3.12+](https://python.org), [uv](https://docs.astral.sh/uv/), and [ffmpeg](https://ffmpeg.org/). That's it.

### Process your first video

```bash
# From a URL — transcribe French audio, translate to English
pgw run "https://www.rts.ch/play/tv/19h30/video/..." -l fr --translate en

# From a local file
pgw run ~/Videos/talk.mp4 -l de --translate en

# With cloud APIs (no GPU, no model download)
pgw run video.mp4 --backend api --llm-backend api --translate en
```

Results land in `pgw_workspace/` — subtitles, vocabulary breakdown, and a bilingual PDF.

---

## The web interface

```bash
pgw serve --no-open
# Open http://localhost:8321
```

The web app has four pages, each doing one thing well:

### Library — your processed videos

All your workspaces in one place. See the language pair, difficulty level, and date at a glance. Click any card to open the player.

### Player — watch and study

The video streams directly from its source (no need to download it). On the right, a clickable transcript — click any line to jump to that moment. Click any word to see its difficulty and save it as a flashcard. Switch between original subtitles, translation, or bilingual view.

### Studio — process something new

Paste a URL or upload a file. Pick the source language and (optionally) a target for translation. Hit **Start job** and watch the progress live. Close the tab, come back later — your job keeps running and the result appears in your Library.

### Review — spaced repetition flashcards

Cards you saved from the Player appear here, scheduled by an FSRS algorithm. Rate them (Again / Hard / Good / Easy) and the algorithm handles the rest. Audio clips play automatically so you hear the word in context.

When an LLM is configured, each card is automatically enriched in the background: the raw word is replaced with its dictionary lemma, a concise definition in **your native language**, IPA pronunciation, a usage register (formal / informal / colloquial…), grammar notes for irregular forms, a context example sentence, and an optional mnemonic. The enriched card appears as soon as the LLM is done — usually within seconds.

### Your account

Click your avatar in the top-right corner to open **Settings**. From there you can:

- Set your **display name** and **native language** — the native language drives which language your flashcard definitions are written in
- Change your password
- Save your language and backend preferences (they'll pre-fill the Studio form)
- Add your own API keys (OpenAI, Groq, DeepSeek…) — they're encrypted and never leave the server

Admins will also see an **Admin** link to manage user accounts.

---

## Docker

```bash
docker compose up -d
```

That's it. Postgres + pgw start together. Open `http://localhost:8321`.

Mount your videos and workspace data:

```bash
docker run --rm -it -p 8321:8321 -v "$PWD:/data" pgw serve --no-open
```

### Rebuilding after changes

```bash
docker compose down
docker compose build pgw
docker compose up -d
```

Use `docker compose down -v` only to wipe the database (creates a fresh start).

---

## API keys

You can set API keys two ways:

**For CLI use** — put them in `.env`:

```env
GROQ_API_KEY=gsk_...
OPENAI_API_KEY=sk-...
PGW_SECRET_KEY=<generate with: python -c "import secrets; print(secrets.token_urlsafe(32))">
```

**For the web interface** — sign in, open **Settings**, and add your keys under "API Credentials". They're encrypted and used per-user — each person uses their own keys. In production, set `PGW_REQUIRE_USER_CREDENTIALS=1` to require every user to add their own keys.

---

## Commands

| Command          | What it does                                             |
| ---------------- | -------------------------------------------------------- |
| `pgw run`        | Full pipeline: transcribe → refine → translate → vocab   |
| `pgw transcribe` | Transcribe only (get subtitles in the original language) |
| `pgw translate`  | Translate an existing subtitle file                      |
| `pgw vocab`      | Vocabulary analysis for a workspace                      |
| `pgw export`     | Export vocabulary as CSV for Anki                        |
| `pgw play`       | Play a video with dual subtitles via mpv                 |
| `pgw serve`      | Launch the web interface                                 |
| `pgw clean`      | Clear cached files                                       |
| `pgw languages`  | List supported languages                                 |

---

## Configuration

Config is stacked: **built-in defaults** → `~/.config/pgw/config.toml` → `./pgw.toml` → `.env` → CLI flags.

```toml
# pgw.toml
[whisper]
backend = "api"
language = "fr"

[llm]
backend = "api"
target_language = "en"
```

Env vars use a `PGW_` prefix: `PGW_WHISPER__BACKEND=api`, `PGW_LLM__API_MODEL=groq/...`.

For local LLMs, pull a model first: `ollama pull qwen3:8b`

---

## Contribute

For developers: this is a Python + TypeScript project. The backend is FastAPI. The frontend is React with TanStack Router and Tailwind.

```bash
# Backend dev (auto-reload not included — restart to pick up changes)
pgw serve --no-open --port 8321

# Frontend dev with hot reload
cd frontend && npm run dev        # opens http://localhost:5173
```

---

## License

[MIT](LICENSE)
