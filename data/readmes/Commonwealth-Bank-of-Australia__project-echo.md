# Project ECHO

> [!NOTE]
> This repository is published by Commonwealth Bank of Australia for research, educational and community purposes only. It is not financial, investment, legal, tax or model-performance advice and must not be relied upon as such. It does not represent the systems, models or controls CBA uses in production, nor any commitment by CBA to adopt or use the content in production. The content is provided “as is”, without warranty of any kind. To the maximum extent permitted by law, CBA excludes liability arising from or in connection with the content or its use. Views expressed by individual contributors are their own and do not necessarily represent the official views of CBA.

More than a century of CommBank history is preserved by the CBA Group Archives team across records, photographs, artefacts and thousands of hours of audiovisual material. Part of this collection includes video recordings stored on physical VHS, Betamax, and other magnetic tape archives. These tapes are slowly degrading, so they're being digitised right now, but much of the information inside it remains difficult to search. That's the challenge this project tackles.

Project ECHO is an AI Labs project that turns raw archival footage into a searchable knowledge base. It does this by:
- Transcribing the audio using speech-to-text models, turning decades of spoken content into text.
- Extracting representative keyframes from the footage and using multi-modal AI models (VLMs) to generate scene descriptions. Together, these capabilities can make large record collections easier to catalogue and search, helping surface historical material that may otherwise be difficult to discover.

Storage and database backends are configurable independently, so it can run anywhere from a laptop with sufficient video memory to production infrastructure.

This is accompanying code to the [_Preserving CommBank’s Archives with AI: From VHS to Vision Models_](https://medium.com/@CommBankTechnology/preserving-commbanks-archives-with-ai-from-vhs-to-vision-models-3caff6d4f166) post on the CommBank Technology blog on Medium.

## Requirements

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/) package manager
- `ffmpeg` for audio extraction, scene-change detection, and frame extraction
- A running OpenAI-compatible Whisper endpoint for transcription.
- An OpenAI-compatible vision/LLM endpoint for frame description and summarisation.

## Quick Start

```bash
# 1. Install dependencies
uv sync

# 2. Copy and fill in the environment template
cp .env.example .env.local

# 3. Preview what would be processed (no changes made)
uv run video-annotate --dry-run

# 4. Run for real
uv run video-annotate
```

## How It Works

For each file in `UPLOADED` state:

1. **Transcribe** audio to text using a Whisper-compatible server (chunked automatically for long files)
2. **Describe** keyframes detected by `ffmpeg` using a vision model served over an OpenAI-compatible endpoint
3. **Summarise** (optional) the frame descriptions + transcription into a narrative using an LLM
4. **Persist** results to the database; optionally write files to disk/storage if `SAVE_OUTPUT_FILES=true`
5. Mark file `PROCESSED` (or `FAILED` on error)

## Setup

**Storage:** Local filesystem (default) or S3 (set `S3_BUCKET`)  
**Database:** SQLite (default, requires `scripts/create_db.sql`) or DynamoDB (set `DYNAMODB_ENABLED=true`)



## Common Options

```bash
uv run video-annotate --hours 6              # Last 6 hours (default: 24)
uv run video-annotate --hours 0              # All UPLOADED files
uv run video-annotate --max-files 5          # Limit to 5 files
uv run video-annotate --summary              # Enable summarisation (off by default)
uv run video-annotate --refresh              # Reprocess PROCESSED/FAILED files
uv run video-annotate --dry-run              # Preview without changes
uv run video-annotate --verbose              # Debug output
```

## Configuration Reference

Priority order: CLI flags > environment variables > `.env.local` > `.env` > built-in defaults.

### Core

| Option / Env Var | Default | Description |
|---|---|---|
| `--bucket` / `S3_BUCKET` | - | S3 bucket name; enables S3 storage when set |
| `DYNAMODB_ENABLED` | `false` | Enable DynamoDB backend (`true`/`1`/`yes`) |
| `DYNAMODB_ENDPOINT` | - | Optional DynamoDB endpoint override (localstack/dev) |
| `--table` / `DYNAMODB_MEDIA_TABLE` | `videos` | DynamoDB media table name |
| `DYNAMODB_USERS_TABLE` | `video_users` | DynamoDB users table name |
| `--region` / `AWS_REGION` | `ap-southeast-2` | AWS region |
| `LOCAL_MEDIA_DIR` | `./media` | Input directory when `S3_BUCKET` is not set |
| `SQLITE_DATABASE` | `videodb.sqlite` | SQLite database path (when DynamoDB is disabled) |
| `--hours` | `24` | Lookback window for UPLOADED files (`0` = all) |
| `--output-dir` | `./transcripts` | Local output directory |
| `SAVE_OUTPUT_FILES` | `false` | Write transcript/summary files to disk and upload to storage |
| `--refresh` | `false` | Also reprocess `PROCESSED` and `FAILED` files |
| `--max-files` | `0` (unlimited) | Maximum files to process per run |
| `--dry-run` | `false` | Preview what would be processed without making changes |
| `MAX_FILE_SIZE_BYTES` | `838860800` (800MB) | Skip files larger than this (`0` = unlimited). Oversized files stay `UPLOADED` and are logged with a warning; safety net against a small crafted file driving unbounded downstream work. Internal/trusted deployments can raise or disable this |

### AI Pipeline

All AI settings target OpenAI-compatible endpoints - this includes self-hosted [vLLM](https://docs.vllm.ai/) deployments (see [`deployment/vllm`](deployment/vllm/README.md)) as well as OpenAI's own API or any other compatible provider. Model names and endpoints below are just the defaults; point them at whatever endpoint/model you're running.

| Env Var | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | (required) | API key for the OpenAI-compatible endpoint. A placeholder value (e.g. `NONE`) works for self-hosted vLLM servers that don't enforce auth |
| `WHISPER_SERVER_URL` | (required) | OpenAI-compatible Whisper server URL (e.g. a self-hosted vLLM endpoint) |
| `WHISPER_MODEL` | `whisper-large-v3-turbo` | Model name sent to the transcription API |
| `WHISPER_LANGUAGE` | `en` | Transcription language code |
| `WHISPER_TIMEOUT` | `600` | Seconds to wait for a Whisper response (increase for long files) |
| `WHISPER_CHUNK_DURATION` | `600` | Max audio chunk length in seconds before splitting |
| `WHISPER_CHUNK_OVERLAP` | `2` | Overlap in seconds between consecutive audio chunks |
| `WHISPER_MAX_CHUNKS` | `20` | Max chunks transcribed per file (`0` = unlimited; ~3.3h of audio by default). Safety net against long/crafted audio tying up a worker |
| `DESCRIBE_MODEL` | `gpt-4o` | Vision model for frame descriptions - set to whatever model your endpoint serves (e.g. a vLLM-hosted model) |
| `DESCRIBE_BASE_URL` | (`OPENAI_BASE_URL`) | Vision API endpoint (vLLM or other OpenAI-compatible endpoint) |
| `DESCRIBE_API_KEY` | (`OPENAI_API_KEY`) | API key for vision model |
| `DESCRIBE_CONCURRENCY` | `12` | Max concurrent async frame description requests |
| `DESCRIBE_BATCH_SIZE` | (`DESCRIBE_CONCURRENCY`) | Batch size for streaming frame description |
| `SCENE_THRESHOLD` | `0.3` | ffmpeg scene-change sensitivity (0.0–1.0; lower = more frames) |
| `SCENE_MIN_INTERVAL` | `0.5` | Minimum seconds between accepted keyframes |
| `MAX_FRAMES_PER_VIDEO` | `300` | Max frames processed per video (`0` = unlimited). Safety net against a crafted video producing unbounded vision-API call volume |
| `--summary` / `--summary-model` / `--summary-base-url` | - | Enable narrative summarisation via an OpenAI-compatible LLM endpoint (e.g. self-hosted vLLM); optionally override model and endpoint |
| `SUMMARIZE_MODEL` | `gpt-5.2` | Summarisation model - set to whatever model your endpoint serves |
| `OPENAI_BASE_URL` | - | Fallback OpenAI-compatible endpoint for both description and summarisation (e.g. a vLLM base URL) |

### Cluster-Aware Scene Detection (opt-in)

When rapid scene transitions are present (e.g. chyrons appearing before the actual content), the standard pipeline may describe the wrong frame. Enable cluster detection to send all frames from a rapid burst to the vision model in a single call for a consolidated description.

| Env Var | Default | Description |
|---|---|---|
| `ENABLE_CLUSTER_DETECTION` | `false` | Enable multi-pass cluster-aware detection |
| `CLUSTER_WINDOW_SECONDS` | `3.0` | Max gap between scene changes to be grouped |
| `CLUSTER_TIGHT_THRESHOLD` | `1.5` | At least one pair in a group must be below this to qualify as a cluster |
| `CLUSTER_MIN_SCENES` | `2` | Minimum changes to form a cluster |
| `CLUSTER_SETTLE_OFFSET` | `0.5` | Seconds after a scene change to extract a "settling" frame |
| `CLUSTER_MAX_SAMPLES` | `5` | Maximum frames per cluster (caps API cost) |
| `SEEK_CONCURRENCY` | `4` | Parallel ffmpeg seek processes for frame extraction |

When enabled, the pipeline uses two passes: a full decode to collect all timestamps (no disk I/O), followed by concurrent seek-based extraction (partial decodes, piped directly to memory). For videos with many filtered frames, this is typically faster than the standard single-pass approach.

## Output

Content is always saved to the database. Transcript and summary text are stored directly in the `transcript` and `summary` fields of each media record.

When `SAVE_OUTPUT_FILES=true`, files are also written to the output directory and uploaded to storage:

| File | Description |
|---|---|
| `{video_name}_transcript.txt` | Timestamped transcription (`[00:00.000 --> 00:05.230] Welcome...`) |
| `{video_name}_summary.md` | Multi-modal narrative summary (markdown) |


## Development

```bash
# Install all dependencies including test and dev tools
uv sync

# Lint (with autofix)
uv run ruff check src/ --fix

# Format
uv run ruff format src/

# Type check (scoped to src/core/ and src/cli.py)
uv run pyright

# Run all pre-commit hooks
uv run pre-commit run --all-files

# Install hooks so they run automatically on git commit
uv run pre-commit install
```

### Testing

```bash
# Full test suite with coverage enforcement (80% minimum)
uv run pytest

# Stop on first failure, no coverage overhead
uv run pytest -x --no-cov

# Run a specific module
uv run pytest tests/core/
uv run pytest tests/transcription/
uv run pytest tests/description/

# HTML coverage report
uv run pytest --cov-report=html
```

All external services are mocked (tests run without AWS credentials, an OpenAI key, or a running Whisper server).

### Repo Structure

```
src/
├── cli.py                  # Click CLI entry point
├── core/
│   ├── models.py           # Pydantic data models (MediaEntry, ProcessingResult)
│   ├── database.py         # DynamoDB + SQLite backends; stuck-state recovery
│   ├── storage.py          # S3 + local filesystem backends (StorageBackend protocol)
│   └── processor.py        # Pipeline orchestration; prefetch, graceful shutdown
├── transcription/
│   ├── config.py           # Whisper configuration
│   └── transcribe.py       # Audio extraction (ffmpeg), chunked Whisper API client
└── description/
    ├── config.py            # Description/summarisation configuration
    ├── clustering.py        # Cluster-aware scene grouping algorithm
    ├── extract_frames.py    # ffmpeg scene detection; single-pass and multi-pass extraction
    ├── describe_frames.py   # Async structured vision descriptions (single + multi-image)
    ├── streaming.py         # Producer-consumer pipeline; cluster-aware variant
    ├── render_markdown.py   # Render descriptions JSON → markdown
│   ├── summarize.py         # Multi-modal summarisation via an OpenAI-compatible LLM endpoint
    └── prompts/             # Jinja2 prompt templates

tests/                      # Mirrors src/ structure; >80% coverage enforced
docs/
└── design.md               # Full architecture and implementation reference
```
