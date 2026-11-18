# junior-narrative-analysis

JUNIOR (Job-entry Understanding through NLP of Interviews, Opinions and Reports) is a local research tool for qualitative analysis of podcasts, talks, blogs, and manually imported LinkedIn posts.

## Project status

This repository currently contains the project structure and environment configuration. Pipeline implementation will be added in later steps.

## Requirements

- Python 3.10 or newer
- Ollama for local language-model classification
- An Ollama model matching `config.yaml` (default: `qwen2.5:7b`)

All processing is designed to run locally. No paid APIs are required.

## Folder structure

```text
.
├── config.yaml
├── codebook.yaml
├── requirements.txt
├── data/
│   ├── raw/
│   ├── transcripts/
│   ├── segments/
│   ├── coded/
│   └── manual_coding/
├── src/
├── outputs/
│   ├── charts/
│   └── reports/
└── tests/
```

`config.yaml` contains input/output paths, model names, segmentation limits, and retry settings.

## Setup on Windows

Open PowerShell in the repository folder:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, enable it for the current user and repeat the activation step:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Install [Ollama](https://ollama.com/download/windows), then download the configured model:

```powershell
ollama pull qwen2.5:7b
```

## Setup on macOS

Open Terminal in the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install [Ollama](https://ollama.com/download/mac), then download the configured model:

```bash
ollama pull qwen2.5:7b
```

Keep the virtual environment activated while working on the project. Deactivate it with `deactivate`.

## Configuration

Update [config.yaml](config.yaml) if you need different paths, models, or segment sizes. Paths are relative to the repository root. The configured Ollama service is expected at `http://localhost:11434`. Add or edit qualitative-analysis entries in [codebook.yaml](codebook.yaml).

To transcribe audio after placing files in `data/raw`, run:

```bash
python src/transcribe.py
```

Timestamped JSON files are written to `data/transcripts`. Existing transcript files are skipped.

To create sentence-boundary segments from transcripts and blog text, run:

```bash
python src/segment.py
```

Segments are written to `data/segments` as JSON files with source metadata and transcript time ranges. Existing segment files are skipped.

To classify segments with the local Ollama model, run:

```bash
python src/classify.py
```

Validated classifications are saved to `data/coded/coded_segments.csv`. Invalid JSON or Pydantic-invalid responses are retried up to `processing.retry_attempts` times.

To compare AI classifications with manual coding and print Cohen's kappa, place one or more CSV files in `data/manual_coding` and run:

```bash
python src/validate.py
```

Manual CSV files should contain `segment_id` and either `code` or `codes`. The validator prints an overall score based on complete code sets and a binary score for each individual code.

To aggregate code frequencies, create charts, and generate a Markdown report with representative quotes, run:

```bash
python src/report.py
```

The report is written to `outputs/reports/report.md`, with frequency data in `outputs/reports/code_frequencies.csv` and charts in `outputs/charts`.

## Planned pipeline

1. Collect podcast audio, web pages, and manually imported CSV data.
2. Transcribe audio locally with faster-whisper.
3. Clean and split text into 300–500 word segments.
4. Classify segments against a qualitative codebook using Ollama.
5. Compare AI coding with manual coding using Cohen's kappa.
6. Aggregate results and generate charts and reports.
