<div align="center">

# aha-paper

**Turn a paper into a guided read.**<br>
It narrates a PDF while marking the sentence it is explaining — on the paper itself.

[![CI](https://github.com/yh2072/aha-paper/actions/workflows/ci.yml/badge.svg)](https://github.com/yh2072/aha-paper/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Narration](https://img.shields.io/badge/narration-中文%20%C2%B7%20English-c2824c.svg)](app/lang.py)

**[▶ Try it live](https://aha-paper.vercel.app)** &nbsp;·&nbsp; [中文说明](README.zh.md)

<sub>A real explainer, playing in your browser: 12 chapters, 13 minutes, no sign-up and no key.</sub>

<br>

<img src="docs/media/studio.jpg" width="820" alt="The aha-paper studio: a composer for the paper and the focus, over a library of explainers">

</div>

---

## See it

**[The demo is live at aha-paper.vercel.app](https://aha-paper.vercel.app)** — the
exported bundle of this very explainer, served as a static site with no backend
at all. One paper, read end to end. The video is three chapters of it, unedited —
three different figures, each walked panel by panel.

<div align="center">

<a href="docs/media/walkthrough-16x9.mp4"><img src="docs/media/walkthrough-16x9.jpg" width="320" alt="Poster frame of the demo: a figure from the paper with the cursor on it and a caption beneath"></a>

**[▶ Watch the walkthrough](docs/media/walkthrough-16x9.mp4)** &nbsp;·&nbsp; 3 min 42 s · 1280×720

<sub>GitHub strips <code>&lt;video&gt;</code> from a README, so the file opens on its own page — where it plays.</sub>

<br>

<img src="docs/media/cursor-16x9.gif" width="660" alt="The cursor moving across a figure from the paper while the caption names the panel it is on">

</div>

**It marks the sentence it is saying.** The voice explains how many people were
scanned; the page shows the sentence that claim came from, marked where it
actually sits.

<img src="docs/media/player-page.jpg" width="820" alt="The paper's own page, with one sentence highlighted while the narration below explains it">

**It points at the panel it is describing.** The narration names a panel and the
regions in it; the cursor is already there, and the view has zoomed in.

<img src="docs/media/player-zoom.jpg" width="820" alt="A figure from the paper, zoomed to one panel, with the cursor resting on the region being described">

> **The paper in the demo.** Tomoya Nakai, Rieko Kubo and Shinji Nishimoto,
> “Cross-domain encoding models reveal shared and domain-specific neural
> representations across language and mathematics,” *Science Advances* **12**,
> eaej5555 (2026). [doi:10.1126/sciadv.aej5555](https://doi.org/10.1126/sciadv.aej5555) ·
> © the authors, licensed [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
> Its figures and pages appear above as aha-paper displays them, unaltered, in a
> non-commercial demonstration of the tool.

---

## Why it can be trusted

Every frame is either **a figure from the paper** or **a page of the paper**. The
model answers one question — *which sentence of the source is this line of
narration explaining?* — and every coordinate is computed from the PDF's own text
layer.

That split is the point. A wrong answer can highlight a different real sentence;
it cannot invent a position. A fabricated quotation resolves to nothing, so
nothing is drawn. There is no third renderer and no generated diagram.

---

## Quick start

```sh
python -m venv .venv
.venv/bin/pip install -r requirements.txt
npm ci --ignore-scripts
cp .env.example .env          # add OPENROUTER_API_KEY
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8321
```

Open <http://localhost:8321> and drop in a PDF.

Needs **Python 3.12+**, **Node 22+** and **FFmpeg**. Edge TTS needs no key, but
does need network. Keys are written only to a local `.env`; the API reports
whether a provider is configured and never returns the credential itself.

A 12-page paper takes about **5 minutes**, most of it writing the script. An
interrupted run resumes without paying for finished work twice, and a fully
cached rebuild takes about 2 seconds.

---

## More

| | |
|---|---|
| [docs/setup.md](docs/setup.md) | Docker · desktop window · building a signed installer · hosting it |
| [docs/reference.md](docs/reference.md) | The two kinds of frame · length and scope · output files · configuration |
| [CONTRIBUTING.md](CONTRIBUTING.md) | The three rules that matter, and how to run the tests |
| [CHANGELOG.md](CHANGELOG.md) | What changed |
| [SECURITY.md](SECURITY.md) | What this app holds, and how to report a vulnerability |

## Acknowledgements

[Twemoji](https://github.com/jdecked/twemoji) for the interface icons ·
[Pi](https://github.com/earendil-works/pi) for the provider and model catalogue ·
[Edge TTS](https://github.com/rany2/edge-tts) for speech ·
Fraunces, Nunito and Pinyon Script for the lettering.
Full attributions and licences in [NOTICE](NOTICE).

Apache-2.0.
