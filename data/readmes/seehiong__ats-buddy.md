# ATS Buddy

Compare your resume against a job description and get back a match score, the keywords you're missing, and a rewritten resume — **entirely on your own machine**. No server, no upload, no account.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Why local

Resumes are among the most sensitive documents most people own: full name, address, phone number, employment history. Handing one to a third-party service in exchange for keyword advice is a poor trade.

ATS Buddy runs the model on your hardware. Your resume is read in the browser, analysed by a model on your own machine, and the report is saved to a file you already have. Nothing crosses the network.

## How it goes

Four steps:

1. **Choose where it runs** — local Ollama, or a model in the browser.
2. **Add your documents** — your resume PDF and the job description.
3. **Tailor the analysis** *(optional)* — how strictly to judge, how detailed the suggestions should be, areas to weight, and free-text notes.
4. **Results** — the score, the gaps, and your rewritten documents.

Each step unlocks the next; nothing is lost moving back and forth.

## What it does

- **Match score** against a specific job description
- **Missing keywords and skills**, split into technical and soft
- **Actionable suggestions** grounded in what your resume actually says
- **Cover letter and rewritten resume** tailored to the posting
- **Scanned PDFs** read by a local vision model, for resumes with no text layer (slow — see below)
- **Reports** saved as Markdown or a self-contained HTML file
- **History** kept in your browser, clearable at any time

## Requirements

There are two ways to run the model. Ollama is the better one.

### Ollama (recommended)

Works in any browser and gives noticeably better results, because it can run models far larger than a browser can hold.

1. Install [Ollama](https://ollama.com).
2. Pull a model for the analysis:
   ```bash
   ollama pull llama3.1:8b
   ```
3. Optional — for scanned PDFs, pull a vision model:
   ```bash
   ollama pull qwen3-vl:8b
   ```
4. If the page can't reach Ollama, allow its origin and restart:
   ```bash
   # macOS/Linux
   OLLAMA_ORIGINS='*' ollama serve
   ```
   ```powershell
   # Windows PowerShell
   $env:OLLAMA_ORIGINS='*'; ollama serve
   ```

### In the browser

No install needed, but a model downloads on first use and results are weaker than Ollama's.

You choose which model to download, from 1.6 GB up to 6.3 GB:

| Model | Size | |
| --- | --- | --- |
| Qwen2.5 1.5B | 1.6 GB | Fastest to download, weakest results |
| Llama 3.2 3B | 2.2 GB | Balanced default |
| Phi-3.5 Mini | 3.6 GB | Stronger reasoning than its size suggests |
| Mistral 7B | 4.5 GB | Good writing quality |
| Llama 3.1 8B | 4.9 GB | Best quality — same family as the recommended Ollama model |
| Qwen3.5 9B | 6.3 GB | Largest offered; needs a capable GPU |

Every option stays selectable. Browsers expose no dependable measure of available GPU memory, so the app flags models that look demanding for your machine rather than blocking them — you know your hardware better than the heuristic does. Whichever you choose is cached in the browser, so the download happens once.

Needs **WebGPU** — Chrome or Edge 113+ on a desktop, with hardware acceleration enabled. Phones and tablets are not supported, because the model will not fit in memory. The app checks for this up front and explains what is missing rather than failing at submit.

**Expect the machine to feel sluggish while it generates.** The model runs on the same GPU that draws your screen, so the desktop can stutter — and anything else GPU-heavy (games, video calls, screen recording) will make it markedly worse. Taking a screenshot mid-generation is a reliable way to make the whole system pause, because it forces a readback from an already-saturated GPU.

This is inherent to running a model in a browser tab, not a bug in the app, though ATS Buddy does what it can about it: generation yields to the browser between tokens so the page keeps painting, and the in-browser engine is given a smaller per-call token budget than Ollama. If you want a responsive machine while it works, use Ollama — it runs the model outside the browser and leaves the display alone.

## Choosing a model

The picker rates every model Ollama has installed and hides the ones that cannot do the job at all (embedding and code-completion models).

| Label | Meaning |
| --- | --- |
| `(recommended)` | Verified against this workload — reliable structured output, responsive |
| `large — best quality, much slower` | 30B and up. Better writing, considerably longer waits |
| `thinks first — several times slower` | Reasoning models. They work, but deliberate at length before answering |
| `small — may not hold the JSON format` | Under 3B. Often drifts from the required output shape |
| `vision model` | Used for reading scanned pages, not for analysis |

Reasoning models such as `deepseek-r1` are **supported but not recommended**. In testing, the same analysis took roughly 61s on `deepseek-r1:8b` against 14s on `llama3.1:8b`, with no better result. The app suppresses their reasoning output where Ollama allows it and strips it from the response where it does not.

## Running it

```bash
npm install
npm run dev
```

Then open the printed URL. To produce a production build:

```bash
npm run build
npm run preview
```

## Tests

```bash
npm test              # once
npm run test:watch    # on change
npm run test:coverage
```

Vitest with jsdom. The suite covers the wizard's navigation rules, prompt tailoring (including the handling of text that tries to redirect the model), streaming response handling for both engines, response parsing, report rendering and escaping, cache keys and storage, model rating, and each step's component behaviour.

Anything needing a GPU, a network call, or the pdf.js worker is exercised through browser testing instead — those cannot run meaningfully under jsdom.

## How it works

```
PDF ──► pdf.js ──► has a text layer?
                        │
                 yes ───┴─── no ──► render pages ──► vision model (OCR)
                  │                                         │
                  └────────────────┬────────────────────────┘
                                   ▼
                        analysis prompt ──► local model ──► JSON
                                   ▼
                        report, and optionally a rewrite
```

Everything above happens in the browser tab, apart from the model call itself, which goes to `localhost` when using Ollama.

### How long it takes

Measured with `llama3.1:8b` and `qwen3-vl:8b` on a desktop GPU:

| Step | Time |
| --- | --- |
| Text-layer extraction | Under a second |
| Analysis | ~15s |
| Cover letter and rewritten resume | ~35s |
| Repeat of an identical run | Instant — served from the cache |
| **OCR, per scanned page** | **30–90s, depending on scan resolution** |

Scanned PDFs are by far the slowest path — a two-page scan runs roughly one to three minutes before the analysis even begins, and higher-resolution scans cost proportionally more. If your resume has a text layer (anything exported from a word processor does), none of that applies. Export to PDF rather than scanning a printout where you have the choice.

| Concern | Approach |
| --- | --- |
| PDF text | pdf.js, with the worker and font data bundled locally rather than fetched from a CDN |
| Scanned pages | Rendered to a canvas and transcribed by a local vision model |
| Analysis | Prompted for JSON, then parsed defensively (below) |
| Caching | SHA-256 of the resume bytes plus the job description, stored in IndexedDB |
| Reports | Built in memory and saved through a blob download |

### Parsing local model output

Hosted models return well-formed JSON fairly reliably. Local models are less predictable, so the parser handles reasoning blocks, markdown fences, prose before and after the payload, trailing commas, and smart quotes, and coerces every field rather than trusting it.

Where a response contains more than one JSON-looking object, it selects the one carrying the expected schema — prose containing braces (`I considered {several options}`) is itself syntactically valid JSON and would otherwise win.

If a response still cannot be parsed, the app retries once with the failed output attached before giving up.

## Migrating from AWS

This began as a serverless AWS application: **S3** for uploads, **Textract** for extraction, **Comprehend** for PII redaction, **Bedrock** (Nova Lite) for analysis, **DynamoDB** for caching, and **Lambda** behind **API Gateway** tying it together.

It worked, but it had to be hosted, it cost money per analysis, and every resume was uploaded to a third party.

| Then | Now |
| --- | --- |
| S3 upload | The file never leaves the page |
| Textract | pdf.js, plus a local vision model for scans |
| Comprehend PII redaction | Unnecessary — nothing is transmitted |
| Bedrock Nova Lite | Ollama, or in-browser WebLLM |
| DynamoDB cache | IndexedDB |
| Presigned S3 URLs | Blob downloads |
| Lambda + API Gateway | None |

The PII redaction is the interesting one to lose. It existed because resumes were being sent elsewhere, and it was always partial — high-confidence entities only, capped at the first 5,000 characters. Keeping the data on the machine removes the problem it was mitigating rather than reducing it.

Running locally also permits *larger* models than the hosted version used, so analysis quality went up rather than down.

## Samples

[`samples/`](samples/) contains material for trying the app out.

Five single-page résumés, each with a matching job description, plus one scanned PDF.

| Résumé | Pair it with | Roughly scores |
| --- | --- | --- |
| `backend_engineer.pdf` | `backend_engineer.txt` | 65–75% |
| `frontend_developer.pdf` | `frontend_developer.txt` | 65–75% |
| `data_scientist.pdf` | `data_scientist.txt` | 65–75% |
| `devops_engineer.pdf` | `devops_engineer.txt` | 65–75% |
| `career_changer.pdf` | `junior_developer.txt` | 65–75% |
| `scanned_resume.pdf` | any | exercises the OCR path |

Cross them deliberately to see the score move — the frontend résumé against the backend posting lands around 25%, and the career changer against the DevOps role around 45%.

All names, employers, and contact details are invented.

## Project layout

```
src/
  services/     pdf, ollama, webllm, the llm facade, parsing, prompts, reports, db
  hooks/        backend selection, analysis orchestration
  components/   form, results, progress, history, capability gate
scripts/        copies pdf.js assets into public/
samples/        resumes and job descriptions for testing
```

## Privacy

- Your resume is never uploaded. It is read in the page and passed to a model on your machine.
- Analyses are cached in IndexedDB in this browser only; "Clear history" erases them.
- No analytics, no telemetry, no accounts, no cookies.
- The deployed site is static. There is no backend to send anything to.

## Licence

MIT — see [LICENSE](LICENSE).
