<div align="center">

# Build an LLM Inference Engine From Scratch

**Twenty chapters and two capstones. One `while` loop that becomes vLLM.**

Read the diagram → break the simulator → take the quiz → run the code.

[![CI](https://github.com/xinbetween/learn-llm-inference-from-scratch/actions/workflows/ci.yml/badge.svg)](https://github.com/xinbetween/learn-llm-inference-from-scratch/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-3b82f6.svg?style=flat-square)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-4b8bbe.svg?style=flat-square)](https://www.python.org/)
[![Dependencies: NumPy](https://img.shields.io/badge/dependencies-numpy-013243.svg?style=flat-square)](https://numpy.org/)
[![GPU required: none](https://img.shields.io/badge/GPU_required-none-16a34a.svg?style=flat-square)](code/)
[![Languages: EN · 中文](https://img.shields.io/badge/languages-EN%20·%20中文-f59e0b.svg?style=flat-square)](#-translating)

[**Read it →**](https://llminference.xinbetween.com/) &nbsp;·&nbsp;
[**Star on GitHub**](https://github.com/xinbetween/learn-llm-inference-from-scratch) &nbsp;·&nbsp;
[**Follow on X**](https://x.com/xinbetween)

</div>

---

Everyone can call an inference API. Almost nobody can explain why `vllm serve` is
40× faster than the twenty lines of PyTorch they wrote last week. Closing that
gap is what this course is for.

It starts with a `while` loop that calls a model. It ends with a paged KV cache,
a preempting scheduler, speculative decoding, tensor parallelism and a streaming
OpenAI-compatible server. Each of those arrives **only after you have felt the
specific pain that made it necessary.**

```python
# Chapter 1. This is the entire engine.
for _ in range(max_tokens):
    logits = model(ids)          # ← this line is 99% of the cost
    ids.append(sample(logits[-1]))
    if ids[-1] == eos: break
```

Nineteen chapters later that loop is unrecognisable, and you will be able to point
at any line of vLLM and say what it is for.

**No GPU. No downloads. No PyTorch.** 6,700 lines of NumPy that run on a laptop in
about six seconds.

---

## Who this is for

| | |
| --- | --- |
| **You ship on top of an inference engine** and want to stop guessing which knob to turn. | Chapters S09–S11 and S19 are the ones your on-call pager cares about. |
| **You are interviewing for inference / systems roles.** | "Why is decode memory-bound?" and "what does PagedAttention actually page?" are S05 and S06. |
| **You read the vLLM source once and bounced off it.** | Every chapter names where its idea lives in vLLM, SGLang and llama.cpp. |
| **You learn by breaking things.** | Twenty-two simulators. Push the KV pool until it thrashes. |

Prerequisites: Python, and roughly what a transformer is. Not calculus, not CUDA.

---

## What makes it different

|  | |
| --- | --- |
| 📊 **Diagrams of the mechanism** | Actual data movement rather than boxes and logos, drawn so you can see where the cost accumulates. |
| 🎛 **Simulators you can break** | Real implementations running in the page. Push the KV pool until it thrashes. Set `top-p` above the model's confidence and watch it divide by zero. |
| ✅ **138 quiz questions** | Six graded per chapter, each with an explanation that names the section to reread. |
| 🐍 **Code that runs** | 22 self-contained NumPy files. All 22 pass in about six seconds, in CI, on every push. |
| 🌏 **English and 中文** | Fully translated — prose, quizzes, simulator tooltips and every label inside every SVG. |

---

## The curriculum

<table>
<tr><th align="left">Layer</th><th align="left">Chapters</th><th align="left">You learn</th></tr>
<tr>
<td><b>The Machine</b></td>
<td>S00</td>
<td>The roofline · arithmetic intensity · HBM vs SRAM · bf16/fp8 · tensor-core tiling · systolic arrays</td>
</tr>
<tr>
<td><b>The Model</b></td>
<td>S01–S04</td>
<td>Generation loop · BPE tokenizer · RMSNorm/RoPE/GQA/SwiGLU · sampling</td>
</tr>
<tr>
<td><b>Memory &amp; KV Cache</b></td>
<td>S05–S08</td>
<td>KV cache · PagedAttention · prefix caching · quantization</td>
</tr>
<tr>
<td><b>Batching &amp; Scheduling</b></td>
<td>S09–S12</td>
<td>Continuous batching · scheduler &amp; preemption · chunked prefill · FlashAttention</td>
</tr>
<tr>
<td><b>Decoding Acceleration</b></td>
<td>S13–S16</td>
<td>CUDA graphs · speculative decoding · grammar-constrained output · MoE</td>
</tr>
<tr>
<td><b>Distributed Serving</b></td>
<td>S17–S20</td>
<td>Tensor/pipeline parallelism · prefill/decode disaggregation · the API · the complete engine</td>
</tr>
<tr>
<td><b>Capstone I</b></td>
<td>S21</td>
<td>picoLM, in Python — a real C engine ported module by module · GGUF &amp; mmap · K-quants · grammar masking</td>
</tr>
<tr>
<td><b>Capstone II</b></td>
<td>S22</td>
<td>mini-picoLM, in TypeScript — the same engine rebuilt for the browser tab, runs with Node · ArrayBuffer arena · fused quant matmul</td>
</tr>
</table>

Each layer answers a question the previous one created:

0. The machine has two speeds. **…which tells you what "fast" even means here. Now write something slow. So:**
1. The model runs. **…which leaves the loop correct and unusably slow. So:**
2. The cache fixes that. **…which makes memory the scarce resource, not FLOPs. So:**
3. Paging and quantization fix that. **…which saturates one GPU with many requests. So:**
4. Batching and scheduling fix that. **…which is as fast as one machine gets. So:**
5. You go distributed.

Read them in order the first time. The dependencies are real.

---

## Quickstart

```bash
git clone https://github.com/xinbetween/learn-llm-inference-from-scratch
cd learn-llm-inference-from-scratch

# --- the code (one dependency) ---
python3 -m venv .venv && source .venv/bin/activate
pip install numpy

python code/s01_generation_loop.py     # start here
python code/run_all.py                 # all 22 chapters, ~6 seconds

# --- the site ---
npm install
npm run dev                            # http://localhost:3000
```

Two files do more than print:

```bash
python code/s19_server.py --serve      # a real OpenAI-compatible SSE server
python code/s20_complete_engine.py     # full engine + leave-one-out ablation
```

---

## The code asserts its own claims

Every file proves the chapter's thesis rather than describing it. This is the
actual CI output, not a summary of it:

```
✓ s00  batch-1 decode asks 1 FLOP/byte of a machine that wants 295 — 0.3% of peak
✓ s05  cached and uncached generation are token-for-token identical
✓ s06  paged attention == contiguous attention to 1.7e-16, at 2× utilisation
✓ s08  grouping recovers 13 dB on outlier weights; unfused dequant moves MORE bytes than fp16
✓ s09  2.9× faster drain, zero padding — and better latency at the same time
✓ s11  chunked prefill produces a bit-identical KV cache; 25× better tail ITL at 32k
✓ s12  online softmax is exact; paged and split-K variants agree to 1e-15
✓ s14  speculative decoding's empirical distribution matches the target within 0.002
✓ s15  200/200 schema-valid outputs vs 0/200 unconstrained; 62% of decode steps skipped
✓ s17  Megatron sharding is exact; TP8 loses to TP1 on Ethernet at batch 512

22/22 passed in 5.9s
```

`run_all.py` only checks exit codes, so the house rule does the real work: **every
claim a chapter makes is checkable by the file next to it.** A chapter without
assertions is a chapter that isn't finished.

Some results are uncomfortable and shipped anyway — the S20 ablation reports
**speculative decoding as a net loss at batch 64.** That is the answer, not a bug:
speculation spends spare compute, and at that concurrency there is none spare. A
course that only shows techniques winning is a brochure.

---

## Repo layout

```
code/                      ALL chapter code lives here
  s00..s21_*.py            one runnable file per chapter + run_all.py
  picolm/                  S21 capstone — a real Python package
  minipicolm/              S22 capstone — the TypeScript engine, imported
                           by the browser simulator via the @engine/* alias
src/
  app/[locale]/            locale-prefixed routes (/en/…, /zh/…)
  content/                 structure, not text
    chapters.ts            chapter metadata: num, layer, loc, file
    bodies/s00..s22.ts     code snippets, shared by every locale
    pages.ts               non-chapter page structure
  components/
    diagrams/              one inline SVG per chapter
    sim/                   one interactive simulator per chapter
  i18n/
    config.ts              LOCALES, href(), Translated<T>
    locales/en/            EVERY English string: ui, sim, diagrams,
    locales/zh/            chapters, pages, bodies/s00..s22 — copy a
                           directory to add a language
  lib/                     seo.ts, jsonld.ts, site.ts, analytics.ts
scripts/brand/             icon + OG card sources, and the script that rasterises them
```

The site is a Next.js static export — no server, no database. It builds to a
folder of HTML you can host anywhere.

Every push to `main` builds and publishes to GitHub Pages via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml); no build output
is committed. It serves from a custom domain at the origin root, so the deploy
sets `NEXT_PUBLIC_SITE_URL` and leaves `NEXT_PUBLIC_BASE_PATH` unset, and
[`public/CNAME`](public/CNAME) carries the domain into every artifact.

To host it somewhere else, copy `.env.example` and set `NEXT_PUBLIC_SITE_URL`:
canonical URLs, `hreflang`, the sitemap and the Open Graph tags are absolute, and
they all derive from it. Analytics (GA4 and Google Tag Manager) is opt-in through
the same file — unset, the build loads no third-party scripts at all.

---

## 🌏 Translating

A new language is a mechanical task with a compiler-generated checklist. There is
**no runtime fallback**, on purpose: a half-translated page is worse than an honest
one, and TypeScript is a better reviewer than a human reading diffs.

**To add a language:**

Every translatable string lives under `src/i18n/locales/<code>/`, one directory per
language. English is the reference shape, and every other locale is type-checked
against it.

1. Add its code to `LOCALES` in `src/i18n/config.ts` and fill in `LOCALE_META`.
2. Copy `src/i18n/locales/en/` to `src/i18n/locales/<code>/`. That directory is
   the whole job:

   | File | What it holds |
   | --- | --- |
   | `ui.ts` | Site chrome, nav, quiz UI |
   | `sim.ts` | Simulator labels, readouts, tooltips and notes |
   | `diagrams.ts` | Every label baked into the chapter SVGs |
   | `chapters.ts` | Layer blurbs, chapter titles, taglines, theses |
   | `pages.ts` | Home, layers, timeline, compare, glossary, setup, references |
   | `bodies/sNN.ts` | Chapter prose and quizzes, one file per chapter |

3. Name the new bundle in the six assemblers that pair locales together —
   `src/i18n/{ui,sim,diagrams}.ts` and
   `src/content/{chapters,pages,bodies/index}.ts` — each of which holds a single
   `{ en, zh, … }` literal.
4. Run `npx tsc --noEmit`. Every remaining gap is a compile error, because
   `Translated<T>` is exhaustive over `LOCALES`.
5. `npm run build` and check both locales.

Code snippets are never translated: they live once in `src/content/bodies/sNN.ts`
and are shared by every language. Only a snippet's caption and filename label are
translatable, and those sit with the prose.

**Conventions.** Code identifiers (`d_model`, `top-p`, `cu_seqlens`), notation
(`softmax(S)`, `q = round(w / scale) + zero`), paper titles and model names stay in
English — they are what the reader will type or search for. Everything else,
including every diagram label and every simulator tooltip, is translated. Prose
uses a small inline markup subset (`**bold**`, `` `code` ``, `[label](/s05/)`) so
translators never touch JSX.

---

## Contributing

Issues and PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Particularly useful:

- **Corrections.** If a claim is wrong, open an issue with the measurement. This is
  the most valuable contribution there is.
- **Translations.** See above — the compiler will tell you exactly what's missing.
- **Quiz questions.** Six per chapter; more good ones are always welcome.
- **A chapter this course is missing.** Multimodal inputs, LoRA serving, embeddings
  and encoder-decoder models are all absent and all interesting.

---

## Credits

Built on the work of the people who actually solved these problems — the vLLM,
SGLang, FlashAttention, Orca, Sarathi-Serve, GPTQ/AWQ and EAGLE authors, among many
others. Full list on the references page.

Special thanks to the minimal engines that make these ideas readable:
[picoLM](https://github.com/RightNow-AI/picolm),
[quant.cpp](https://github.com/quantumaikr/quant.cpp),
[baseRT](https://github.com/basecompute/baseRT) and
[llama.cpp](https://github.com/ggml-org/llama.cpp).

This is an educational reimplementation and is not affiliated with any of them.
Production engines are the real thing; this teaches you how to read them.

---

<div align="center">

**[Start with Chapter 1 →](https://llminference.xinbetween.com/en/s01/)**

If this helped, a ⭐ makes it findable for the next person.

[GitHub](https://github.com/xinbetween/learn-llm-inference-from-scratch) · [X](https://x.com/xinbetween) · MIT licensed

</div>
