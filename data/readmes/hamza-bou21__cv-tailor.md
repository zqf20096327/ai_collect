# CV Tailor

[![Tests](https://github.com/hamza-bou21/cv-tailor/actions/workflows/tests.yml/badge.svg)](https://github.com/hamza-bou21/cv-tailor/actions/workflows/tests.yml)

A CV tailoring tool where the model never writes your bullet points. It only selects and ranks bullets and skills from your own master CV by ID, and numbers and skills in the cover letter are checked against that CV with deterministic code.

![CV Tailor demo](media/demo.gif)
## Overview

CV Tailor takes a master CV and a job posting, produces a fit assessment, and generates a tailored one-page CV and a cover letter (English or French) compiled from LaTeX.

The design goal is simple: the output should never contain experience you do not have. The CV side is protected by construction, because the model can only pick existing items. The cover letter side is protected by validation, with automatic re-prompting when a check fails. The section "What it guarantees and what it does not" spells out exactly where that protection ends.

Master data, databases and generated documents stay on your machine. The CV and job text you analyze are sent to the model provider (Groq) for processing.

## What it guarantees and what it does not

What it guarantees:

1. Every bullet and skill in the generated CV comes from your master CV. The model refers to items by ID, any ID that does not exist is dropped, and any valid item the model leaves out is added back in your CV's own order.
2. Each cover letter sentence that states a fact must cite IDs, and a cited ID that does not exist in your master CV is flagged. Digits in the letter must appear in your facts block or your bullets, and technical skill names the letter mentions must be in your skill list. A failed check triggers a re-prompt, up to two retries. These checks run as code and do not rely on the model checking itself.
3. Every generated document is logged with a SHA-256 hash, and manual text edits are flagged so the audit trail stays honest.

What it does not guarantee:

1. Cover letter prose is written by the model. The checks are narrow and cannot catch a wrong framing, such as describing a supporting role as a leading one, or a claim that contains no digit and no listed skill name. Read the letter before you send it.
2. The role line under your name is written by the model to match the posting and is not checked against your master CV. Make sure it is a title you are comfortable claiming.
3. The citation check confirms that a cited ID exists. It does not confirm that the sentence is actually supported by the bullet it cites.
4. The skill check uses a fixed vocabulary of about 140 common technical terms (languages, frameworks, databases, cloud and devops tools). A fabricated skill outside that list, for example Tableau or Excel, would not be flagged.
5. The number check works on digits and compares by value. A figure passes if it appears in any bullet or fact, even when the sentence attaches it to a different achievement. Numbers written out as words are not checked.
6. If a letter still fails verification after re-prompting, it is not blocked. It is still compiled and offered for download, with the warnings shown in the app and recorded in the audit log. Check for warnings before you use it.
7. The fit score and verdict (apply, stretch, skip) are model judgments. They have not yet been compared against human labels, so treat them as a rough signal.
8. The tool cannot rephrase a bullet to mirror a posting's wording. Tailoring happens through selection and ranking only.
9. The master CV is only as accurate as its source. PDF extraction can make parsing mistakes, so review `master_cv.yaml` after importing a PDF.

## Features

Ingestion. `init_cv.py` extracts text, reading order and embedded hyperlinks from a CV PDF with `pymupdf` and builds a validated, bilingual `master_cv.yaml` using Pydantic models. Grouped skills are split into atomic entries, spoken-language proficiency is preserved, and a professional summary is captured only if it exists in the source, never invented.

Fit engine. Analyzes a raw job posting against `master_cv.yaml` using Groq (`openai/gpt-oss-120b` by default). Outputs a fit score from 0 to 100, a verdict, confirmed strengths and a gap analysis.

Ranking-based selection. The model ranks every skill, experience bullet and project bullet by relevance instead of filtering them, so the layout engine decides what gets trimmed, not the model. Hallucinated IDs are dropped and any valid items the model left out are re-appended deterministically.

One-page compilation. LaTeX templates in a clean single-column style, with grouped skills and an optional summary block. If the page overflows, a two-stage loop first tightens typography and spacing (down to a 9.5pt readability floor), then prunes the lowest-ranked items.

Cover letter. A cite-then-validate engine with automatic re-prompting on failed checks, a compact single-language context payload, and localised salutation, date and sign-off.

Audit history. Every generated document is stored in a local SQLite database with its hash, and can be browsed or deleted from the web app.

## Architecture and core rules

1. Rank-then-trim, cite-then-validate. The model never writes new bullet points. It selects and ranks existing ones by ID.
2. Deterministic checks. Numerals and named skills are validated with regex and set comparison, not by trusting model self-reflection.
3. Layout-budgeted content. Content is preserved through typography compaction and only trimmed, lowest-ranked first, as a last resort.
4. Local-first. Master data (`*.yaml`), the SQLite database (`*.db`) and compiled `*.pdf` and `*.tex` files are ignored by version control.
5. Provenance tracking. Selection edits do not trigger re-verification. Manual text edits set `manually_edited = true`.

## Project structure

```text
cv-tailor/
├── .env.example          # Template for required environment variables
├── .gitignore            # Git ignore rules for privacy and build artifacts
├── .dockerignore         # Files excluded from the Docker build context
├── Dockerfile            # Container image (Python + LaTeX + Streamlit)
├── docker-compose.yml    # One-command deployment with persistent volumes
├── LICENSE               # MIT License
├── README.md             # Project documentation
├── REQUIREMENTS.md       # Consolidated product specifications
├── requirements.txt      # Python dependencies
├── demo/
│   ├── master_cv.yaml    # Sample master CV for trying things out
│   └── posting.txt       # Sample job posting
├── tests/
│   ├── test_selection.py                 # Deterministic ID-scrubbing tests
│   ├── test_verification.py              # Numeral, skill and citation verification tests
│   ├── test_pdf_extraction.py            # PDF to master_cv extraction and grounding tests
│   ├── test_layout_and_summaries.py      # Selection ranking, layout, grouped skills, summaries
│   └── test_cover_letter_localization.py # Localization, TPM budget and reasoning-model tests
├── models.py             # Pydantic data schemas and verification contracts
├── core.py               # Fit analysis, selection, verification, PDF parsing
├── latex_builder.py      # LaTeX CV and cover-letter rendering, PDF compilation
├── db.py                 # SQLite audit log and history helpers
├── init_cv.py            # Bootstrap script to parse a PDF into master_cv.yaml
├── analyze.py            # Command-line pipeline (analysis, CV, cover letter)
└── app.py                # Streamlit web interface
```

## Quickstart with Docker (recommended)

No local Python or LaTeX install is needed. The image bundles TeX Live with every package `latex_builder.py` uses, including T1 fonts and French language support.

Prerequisite: Docker with the Compose plugin.

1. Clone the repository:

   ```bash
   git clone https://github.com/hamza-bou21/cv-tailor.git
   cd cv-tailor
   ```

2. Build and start:

   ```bash
   docker compose up --build
   ```

3. Open http://localhost:8501 and paste your [Groq](https://console.groq.com/) API key into the sidebar. No key is needed to start the container.

Stop it with `docker compose down`. Add `-v` to also delete the persisted data and output volumes.

With plain Docker:

```bash
docker build -t cv-tailor .
docker run --rm -p 8501:8501 \
  -v cv_tailor_data:/app/data \
  -v cv_tailor_output:/app/output \
  cv-tailor
```

Persistence and configuration:

1. The SQLite audit database is written to `/app/data/audit.db` inside the container, on a mounted volume. Override the location with the `CV_TAILOR_DB_PATH` environment variable. Outside Docker it defaults to `history.db` in the project root.
2. Generated PDFs and `.tex` sources persist in the `/app/output` volume.
3. Master CV profiles live in `/app/profiles`. Mount that path as a volume to keep your profiles across rebuilds.

The web app asks for your Groq API key in the sidebar. The key is held in the session's memory only and is never written to disk, so it is not stored in the image, the volumes or the database.

## Local installation

Prerequisites: Python 3.10 or newer, a [Groq Cloud](https://console.groq.com/) API key, and a LaTeX distribution that provides `pdflatex` (MiKTeX or TeX Live). On Windows, `latex_builder.py` finds `pdflatex` on PATH or in the default MiKTeX locations.

```bash
git clone https://github.com/hamza-bou21/cv-tailor.git
cd cv-tailor

# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Then open `.env`. The web app asks for the key in its sidebar, so the key here is only needed for the command line pipeline:

```text
GROQ_API_KEY=gsk_your_actual_key_here
# Optional: where the SQLite audit database is stored.
# CV_TAILOR_DB_PATH=/app/data/audit.db
```

Model and provider notes:

1. The default model is `openai/gpt-oss-120b`. Reasoning models such as `gpt-oss` and `qwen` spend part of `max_tokens` on internal reasoning before emitting JSON. The client caps their reasoning (`reasoning_effort` set to `low` or `none`) and sizes `max_tokens` per call to stay under Groq's 8,000 TPM single-request ceiling. Plain models such as `llama-3.3-70b-versatile` are called without `reasoning_effort`, since they reject the parameter.
2. Rate and token-limit errors (429 and 413) trigger a 10-second backoff before retrying, so the rolling TPM window can clear.

## Usage

### Streamlit web app

```bash
streamlit run app.py
```

Paste your Groq API key into the sidebar first. It is kept in session memory only, so you enter it again after restarting the app.

The app has three tabs:

1. Job Tailoring: paste a posting, run the fit analysis, and download the tailored CV and cover letter.
2. Sources and Profile Manager: import a CV from PDF, and inspect, edit or delete saved `master_cv.yaml` profiles.
3. Provenance and Audit History: browse every generated document with its SHA-256 hash, and delete individual records or purge all history.

### Command line

```bash
# Analyze a posting against the demo CV and compile a CV with a cover letter
python analyze.py --job demo/posting.txt --letter

# Use a specific profile, French output, and a named company
python analyze.py --cv profiles/jane_doe.yaml --job posting.txt --lang fr --company "Acme Inc"

# Generate even when the fit verdict is skip
python analyze.py --force
```

| Flag | Description |
|------|-------------|
| `--cv` | Path to master CV YAML (falls back to `demo/master_cv.yaml`) |
| `--job` | Path to job posting text file |
| `--lang` | Target language: `en` or `fr` (default `en`) |
| `--letter` | Also generate a verified cover letter |
| `--company` | Company name recorded in the audit log |
| `--force` | Generate even if the fit verdict is `skip` |

### Build your master CV from a PDF

```bash
python init_cv.py "path/to/your_cv.pdf"
```

Review the resulting `master_cv.yaml` before using it. Everything the tool writes is grounded in this file.

## Testing

The test suite covers selection, verification, PDF extraction, layout and summaries, and cover-letter localization. It runs fully offline and needs no API key.

```bash
pytest
```

## License

Distributed under the [MIT License](LICENSE).