# job-eval

**Score your resume against any number of jobs — locally, for free, with a
model that tells you *why*.**

`job-eval` reads your resume and a list of job descriptions and gives each one
four scores from **1 to 5** — plus the exact paragraph that drove each score. No
API keys, no per-call cost, no data leaving your machine. It runs on a laptop
**CPU** in a few seconds and on a **GPU** instantly.

It's powered by a purpose-trained **156M-parameter ModernBERT cross-encoder** —
not a giant general LLM — so it's small enough to run yourself and cheap enough
to run on hundreds of postings in one pass.

- 🧠 **Model:** [huggingface.co/kasraahmadi/job-eval-modernbert](https://huggingface.co/kasraahmadi/job-eval-modernbert)
- 🌐 **Hosted version for recruiters & non-technical users:** [job-eval.com](https://job-eval.com)

> Use this repo when you want to run the model yourself — batch-score a whole job
> board against your CV inside your own job-hunting pipeline, on your own GPU.
> Use the website when you just want to paste one resume and one job and get an
> answer without installing anything.

---

## What you get

Every run creates a fresh timestamped folder under `output/` with two files:

**`evaluation.csv`** — one row per job:

| Resume_source_path | JD_Link_or_text | requirement_coverage | seniority_fit | domain_alignment | ats_keyword_overlap | average_score | band |
| --- | --- | --- | --- | --- | --- | --- | --- |
| my_cv.pdf | Senior Backend Engineer… | 3.87 | 4.20 | 4.71 | 3.79 | 4.14 | Strong match |

**`explanation.txt`** — human-readable, ranked best-first, and for **each aspect**
it quotes the paragraph the model weighted most heavily:

```
[1] Senior Backend Engineer — FinServe
    OVERALL 4.14/5   Strong match   ████████████████····

    Requirement Coverage  —  3.87/5   ██████████████······
      How well the resume covers the skills the job asks for.
      Resume evidence: "Designed and shipped an event-driven ledger service…"
      Job asks for:    "5+ years of Python, strong AWS experience, distributed…"
```

### The four scores

| Aspect | Question it answers |
| --- | --- |
| `requirement_coverage` | How well the resume covers the skills/responsibilities the job asks for |
| `seniority_fit` | Whether your experience level matches the role's seniority |
| `domain_alignment` | How closely your industry / problem domain matches the job |
| `ats_keyword_overlap` | Overlap of concrete keywords an ATS screener looks for |

---

## Quickstart (CPU — works on any machine)

```bash
git clone https://github.com/kasraahmadi/job-eval
cd job-eval

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Score the bundled example resume against the bundled example jobs:
python run.py
```

The first run downloads the model (~600 MB) from Hugging Face and caches it. Then:

```bash
# Your own resume (PDF or text) against your own jobs:
python run.py --resume my_cv.pdf --jobs jobs.csv
```

Open the printed `output/<date_time>/` folder to see `evaluation.csv` and
`explanation.txt`.

## Running on a GPU

If you have an NVIDIA GPU, install the CUDA build of PyTorch **first**, then the
rest, and set `device: cuda` (or `--device cuda`):

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121   # match your CUDA
pip install -r requirements.txt
python run.py --device cuda --resume my_cv.pdf --jobs jobs.csv
```

`device: auto` (the default in `config.yaml`) uses a GPU if it finds one and
falls back to CPU otherwise, so you usually don't need to touch this.

---

## Configuring it

Everything lives in **`config.yaml`** — edit it and just run `python run.py`:

```yaml
device: auto                 # auto | cpu | cuda
resume: examples/resume.md   # your resume: .pdf, .md, or .txt
jobs: examples/jobs.csv      # see "Input formats" below
output_dir: output
model_repo: kasraahmadi/job-eval-modernbert
max_len: 1024                # tokens of (resume + job) the model reads
```

Any option can be overridden on the command line — run `python run.py --help`.

## Input formats

**Resume** (`--resume`): a `.pdf` (parsed to text automatically), or any `.md` /
`.txt` / plain-text file.

**Jobs** (`--jobs`): whatever is convenient —

- a **`.csv`** file — one job per row. A `jd` / `description` / `url` column is
  used for the text (or the first column), and an optional `title` / `company`
  column names it in the report.
- a **`.txt` / `.md`** file — a single job, **or** several jobs separated by a
  line of `---`, **or** one URL per line.
- a **folder** — one job per `.txt` / `.md` file inside.
- a **single URL**, or comma-separated URLs (best-effort fetch — many job boards
  need JavaScript or block scrapers, so pasting the text is the reliable path).
- a **single block of text** in quotes.

---

## How it works

The model is a partially-unfrozen [ModernBERT](https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base)
cross-encoder. Resume and job description go in together; the encoder's token
states feed a **per-aspect attention pooler** that learns, separately for each of
the four scores, which parts of each document matter. That attention is sparse
(α-entmax) and trained to stay peaked, which is what makes the "Resume evidence"
lines above real rather than a post-hoc guess — they are the spans the model
actually put its weight on.

- **156M parameters**, ~16.5M trainable; the rest of the encoder is frozen.
- Trained on LLM-judged (resume, JD) pairs with a masked-MSE objective and an
  attention-entropy penalty for legibility.
- **Held-out accuracy:** on 100 hand-scored pairs the average score tracks human
  judgement at **Pearson r ≈ 0.90 / Spearman ρ ≈ 0.84 / quadratic-weighted
  κ ≈ 0.83**, with **99% of predictions within one point**.

Full training write-up and metrics are on the
[model card](https://huggingface.co/kasraahmadi/job-eval-modernbert).

## Responsible use

`job-eval` is a **triage and explanation aid, not a hiring decision**. It ranks
and explains fit; keep a human in the loop and never use it for automated
rejection. It's trained on English resumes, `seniority_fit` is its weakest head,
and — like any resume model — it can reflect biases in its training labels.

## License

Code: [MIT](LICENSE). Model weights: Apache-2.0 (matching the base encoder).
