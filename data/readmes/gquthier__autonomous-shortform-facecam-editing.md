<div align="center">

<img src="https://img.shields.io/badge/CREATIVE-VIDEO-2563EB?style=flat-square&labelColor=2563EB&color=1A1A1A" alt="CREATIVE · VIDEO">

# Autonomous Short-Form Facecam Editing

### One raw facecam take in. A finished motion-graphics ad out.

Paid-social editors charge you per video for a job that is 90 % rules.<br>This skill hands the rules to your agent — one designed card per sentence, word-synced captions,<br>sound design, brand B-roll — and renders the whole thing deterministically. You keep the taste.

<br>

<a href="https://bizos.cc">
<img src="https://img.shields.io/badge/BizOS-build%20autonomous%20companies-0A0A0A?style=for-the-badge&labelColor=0A0A0A" alt="BizOS — build autonomous companies">
</a>

<br><br>

<a href="https://x.com/gauthierthiry"><img src="https://img.shields.io/badge/@gauthierthiry-0A0A0A?style=flat-square&logo=x&logoColor=white" alt="X"></a>
<a href="https://youtube.com/@gquthier"><img src="https://img.shields.io/badge/@gquthier-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>

<br>

<sub>Claude Code skill + playbook · silence pre-cut · face-centred square & 9:16 crops (mirror) · word-level transcript · brand steal (palette, screenshots, site B-roll) · one motion-graphics card per sentence · karaoke captions · SFX + music bed · pencil-border windows · cutout variant · HyperFrames render · QA loop</sub>

</div>

---

This is a **Claude Code skill** + a complete playbook (with runnable scripts) that turns **one raw
talking-head take + one brand URL** into a finished **1080×1920 motion-graphics ad** — the way a
paid-social editor would, but scripted for an AI coding agent and rendered deterministically with
[HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP → MP4).

The take plays untouched underneath, in a tight face-centred **square window** (or full-bleed). On top:
**one designed card per sentence** — count-ups on every number, lists that pop and get struck through,
stamps on real screenshots, before/after, full-screen takeovers, the brand site scrolling in a browser
window, social proof, a CTA that pulses — plus **word-synced karaoke captions** with colour-coded money
words, **~40 sound-effect hits** landing on the exact word, a music bed, a progress bar and zoom punches.
Optional **cutout variant**: the speaker is matted out and floats over the brand paper with graphics
behind their head.

You don't brief an editor. Your agent reads the transcript, writes the storyboard, builds the
composition, checks it, looks at the frames, and renders — you redirect a draft instead of writing specs.

## What's inside

```
SKILL.md                     ← the master guide for the agent (start here)
references/                  ← deep-dives
  playbook-summary.md   card-archetypes.md   storyboard-schema.md   worked-example.md
  troubleshooting.md    gotchas.md           brand-tokens.md        audio-mix.md
scripts/
  setup_assets.sh        prep.py             words_from_whisper.py  capture_site.mjs
  make_broll.sh          make_sfx.sh         build.py               theme.css
  remove_background.sh   qa.sh
examples/
  brand.example.json (+ .fr)   storyboard.example.json (+ .fr)   lexicon.en.json / lexicon.fr.json
  corrections.example.json (+ .fr)
```

## The stack

| Layer | Tech |
|-------|------|
| Renderer | [HyperFrames](https://hyperframes.heygen.com) — one paused GSAP timeline, seek-safe HTML → MP4 |
| Footage prep | `ffmpeg` (silence detection, trims, crops, keyframe/s) · OpenCV Haar (face centring) |
| Transcript | whisper.cpp (`whisper-cli`), word-level, strict monotonic timestamps |
| Brand capture | Playwright (full-page screenshot, section crops, palette) · synthesized scroll B-roll |
| Sound design | ElevenLabs sound-generation + music API (optional — bring your own kit) |
| Composition | `build.py` — 11 card archetypes, 4 framing modes, karaoke captions, SFX placement |
| Cutout | `hyperframes remove-background` (u2net) → alpha WebM; Apple Vision recipe in the references |
| QA | `hyperframes check` (lint · runtime · layout · contrast) → snapshots → `qa.sh` (LUFS / true-peak) |

## The pipeline

```
 take.mp4 ─┐                         ┌─ band.mp4  (square window, face-centred, mirrored, keyframe/s)
           ├─ prep.py ───────────────┼─ vert.mp4  (full-bleed 9:16 tight crop)
 silences, │  (silences, restarts,   ├─ voice.mp3 / voice.wav  (−16 LUFS)
 --cut a-b ┘   face → crops)         └─ metadata.json (keep segments, boxes)
                      │
                      ▼
          words_from_whisper.py ──► words.json (strict monotonic) · transcript.txt (indexed "i@t word")
                      │                                   ▲ corrections.json
 brand URL ─► capture_site.mjs ──► site/*.png · palette.json · broll/page-1080.png ─► make_broll.sh ─► broll/*.mp4
 ELEVENLABS ─► make_sfx.sh ──────► sfx/*.mp3 (−3 dB, trimmed) · music/bed.mp3
                      │
   YOU / the agent ──► storyboard.json  (one card per sentence, timed on word indexes, 4 framing modes)
                      │
                      ▼
                  build.py ──► public/index.html  (cards · karaoke captions · SFX · bed · shapes · progress · punches)
                      │
   npx hyperframes check ─► snapshot ─► LOOK ─► render ─► qa.sh (loudness, contact sheet)      [--cutout: remove_background.sh]
```

## Card archetypes

| type | what it is |
|---|---|
| `title` | kicker + serif headline + delayed detail line |
| `countup` | a number counting from → to on the exact word, suffix, label, delayed sub-line (red = cost, green = win, blue = brand) |
| `stamp` | a real screenshot in a white card with a rotated stamp slamming on the key word |
| `list` | rows that pop word-by-word, get struck through (pen scratch) or glow as the answer |
| `takeover` | full-screen: video hidden, one giant word landing with an impact (goes *behind* the speaker in cutout mode) |
| `broll` | the brand site scrolling inside a browser window (traffic lights + URL pill) |
| `chips` | floating pills over the full-bleed close-up, popping in cascade |
| `cta` | logo, headline, offer, pulsing button, bouncing arrow — the last 3 seconds |
| `quote` | a punchline card sliding in with an accent bar |
| `proof` | count-up + five gold stars + rating + review screenshot |
| `beforeafter` | BEFORE (red) slides from the left, arrow, AFTER (green) from the right — text or screenshots |

Four framing modes: `split` (card on top, square video window below — the workhorse), `solo` (circle-masked
speaker, banners above and below), `fullhim` (full-bleed close-up + floating chips), `full` (takeover). The
window alternates rounded / pill / circle with a hand-drawn pencil border.

## Quickstart

1. **Prereqs** — Node ≥ 22, `ffmpeg`/`ffprobe`, `whisper-cli` + a ggml model, Python 3 (+ `opencv-python`), `npx hyperframes doctor` once. `ELEVENLABS_API_KEY` is optional (drop your own mp3s in `assets/sfx/raw`).
2. **Assets** — `bash $SK/scripts/setup_assets.sh $P` (GSAP from npm, open fonts).
3. **Footage** — `python3 $SK/scripts/prep.py take.mp4 $P --square --mirror` → look at 3 frames of `media/band.mp4`. → `SKILL.md` §2
4. **Transcript** — `python3 $SK/scripts/words_from_whisper.py $P --lang en --print` → read it, fix names in `corrections.json`. → §3
5. **Brand** — `node $SK/scripts/capture_site.mjs https://brand.com assets` + `make_broll.sh` + `make_sfx.sh`, fill `brand.json`. → §4
6. **Storyboard** — one card per sentence, timed on word indexes. This is where the taste lives. → `references/card-archetypes.md`, `references/worked-example.md`
7. **Build & check** — `python3 $SK/scripts/build.py $P && npx hyperframes check public` → snapshots → fix what you *see*.
8. **Render & verify** — `npx hyperframes render public -o out.mp4 --fps 30` → `bash $SK/scripts/qa.sh` (contact sheet, LUFS, true-peak).

```bash
SK=~/.claude/skills/autonomous-facecam-editing; P=./my-ad; mkdir -p $P && cd $P && npm init -y && npm i playwright
bash $SK/scripts/setup_assets.sh . && python3 $SK/scripts/prep.py take.mp4 . --square --mirror
python3 $SK/scripts/words_from_whisper.py . --lang en --print
node $SK/scripts/capture_site.mjs https://brand.com assets && cp $SK/examples/brand.example.json brand.json
python3 $SK/scripts/build.py . && npx hyperframes check public && npx hyperframes render public -o out.mp4 --fps 30
```

## Install as a Claude Code skill

```bash
# personal (all projects)
git clone https://github.com/gquthier/autonomous-shortform-facecam-editing.git \
  ~/.claude/skills/autonomous-facecam-editing

# or project-scoped
git clone https://github.com/gquthier/autonomous-shortform-facecam-editing.git \
  .claude/skills/autonomous-facecam-editing
```

Claude Code picks it up automatically. It triggers when you ask things like *"turn this take into an ad"*,
*"package my facecam video with motion graphics"*, *"Claude Edit"*, or when you share a talking-head clip + a brand URL.
The agent asks three questions once (framing, layout mix, hook variants) and runs to a reviewable draft.

## Tested

End-to-end on a 44 s French take (4K 120 fps HEVC source): prep 3-4 min, whisper 20 s, build < 1 s,
`hyperframes check` 0 errors / 23 contrast checks, render ≈ 2 min → 1080×1920 30 fps, −16.7 LUFS, −1.2 dBTP.

## Contributing

- One PR per archetype / script / doc change. Keep `build.py` free of brand-specific text — everything
  brand-related lives in `brand.json`, `lexicon.json` and `theme.css` tokens.
- A new archetype = a `card_<name>()` in `build.py` (every delayed element starts with `style="opacity:0"`,
  every entrance is a `fromTo(..., immediateRender:false)`), its CSS in `theme.css`, a row in the archetype
  table, a JSON example + "common mistakes" in `references/card-archetypes.md`.
- Before opening a PR: `python3 -c "import ast,sys;[ast.parse(open(f).read()) for f in sys.argv[1:]]" scripts/*.py`,
  `bash -n scripts/*.sh`, then a real `npx hyperframes check public` on a test project — paste the summary line in the PR.
- Bugs: open an issue with the exact lint/check message, the storyboard beat involved and a snapshot.
  See `references/troubleshooting.md` first.

## Credits & license

Method: the **Claude Edit** playbook by [Caleb Kruse / Mr Paid Social](https://skool.com/mrpaidsocial), generalised
and extended (mirror + tight re-crop from the native source, pencil-border windows, cutout variant, silence pre-cut).
Renderer: [HyperFrames](https://hyperframes.heygen.com) by HeyGen. Fonts: Tinos (Apache 2.0), Libre Franklin (OFL).
GSAP is fetched from npm (free for all uses since 3.13).

MIT — bring your own footage, brand and API keys.

---

<div align="center">

<br>

### Building something that runs itself?

**[bizos.cc](https://bizos.cc)** — build autonomous companies.

<br>

<a href="https://x.com/gauthierthiry"><img src="https://img.shields.io/badge/@gauthierthiry-0A0A0A?style=flat-square&logo=x&logoColor=white" alt="X"></a>
<a href="https://youtube.com/@gquthier"><img src="https://img.shields.io/badge/@gquthier-FF0000?style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>

<br><br>

<sub>Built by <a href="https://x.com/gauthierthiry">Gauthier Thiry</a></sub>

</div>
