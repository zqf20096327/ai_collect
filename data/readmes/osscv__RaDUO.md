# RaDUO

**Version V6.7**  
**By Davon Khoo** · [www.dkly.net](https://www.dkly.net) · [Project page](https://www.dkly.net/projects/9)

**RaDUO** (Radio Dataset Utility and Organizer) turns live radio broadcasts into a multilingual speech-to-text (STT) dataset for ASR research, evaluation, and model-training preparation.

The project records multiple stations in parallel, cuts streams into short audio clips, transcribes each clip, calculates basic audio-quality features, and writes searchable metadata. The included dataset contains 16 kHz, mono WAV clips together with transcripts, station information, language labels, and optional word timings.

## Disclaimer

**Radio ASR Dataset Builder**  
Made by **KHOO LAY YANG** · [www.dkly.net](https://www.dkly.net)

### Purpose

This tool exists for learning and research: building speech datasets for study
and experimentation. It is not intended for commercial resale of the
recordings or the transcripts produced with it.

### Use at your own risk

Provided as is, with no warranty of any kind. You are responsible for how you
run it and for whatever you do with the output.

### Copyright and law

Radio broadcasts, the audio within them, and the resulting transcripts may be
protected by copyright and by other rights. Respect the original rights
holders, each broadcaster's terms of use, and the laws that apply where you
are. Obtain permission where it is required. Do not use this tool to
redistribute content you have no right to share.

### Where the streams come from

Every radio source is either a publicly available stream or comes from a
third-party directory API such as [radio-browser.info](https://www.radio-browser.info/).
This project does not own, host, control, or endorse these streams, and makes
no claim to the content they carry. Stream URLs may change or stop working at
any time.

### Be a considerate client

Do not abuse this tool. Do not use it to place unreasonable load on any stream
server or API, and do not use it for denial-of-service or anything resembling
one. Keep the number of simultaneous connections sensible, avoid needless
reconnection loops, and stop when you have what you need. One
listener-equivalent connection per station is the intended behaviour.

## What it does

- Captures live radio from a built-in roster of stations across Asia, Australia, Europe, and North America.
- Creates random-length speech segments, generally around 20–30 seconds with a longer-segment tail.
- Sends clips to configurable STT providers, including OpenAI-compatible gateways, Qwen, ElevenLabs, RevoLab, Deepgram, Inworld, OpenRouter, and Telnyx.
- Stores the transcript, detected language, station and regional metadata, timing information, and audio statistics.
- Keeps failed or incomplete rows available for retry, cleanup, review, and export.
- Produces CSV, JSONL, Excel, and Hugging Face `audiofolder`-style metadata.

## GUI

RaDUO also includes a desktop GUI for managing the complete dataset workflow.
The GUI can discover radio stations from publicly available radio-directory
APIs, manage radio sources, configure ASR models and fallback chains, collect
audio and transcripts, manage provider API keys and usage limits, edit
transcripts, inspect dataset statistics, retry processing, and follow activity
logs.

Launch it with:

```powershell
python radio_dataset.py gui
```

Running `python radio_dataset.py` without a subcommand also opens the GUI.

### Radio source and transcript management

Manage radio sources discovered from public APIs, inspect station metadata, and
review or edit collected transcripts.

![RaDUO radio source and transcript management](docs/screenshots/radio-source-and-transcripts.png)

### ASR model and fallback management

Add ASR providers, configure models, define language routes, and set ordered
fallback providers for failed requests.

![RaDUO ASR model management](docs/screenshots/asr-models.png)

### Collection

Configure and start collection jobs that capture radio audio, create clips,
send them for transcription, and save the resulting metadata.

![RaDUO collection workflow](docs/screenshots/collect.png)

### ASR API key management

Track provider keys without exposing them in the dataset. Usage limits can be
configured by units such as requests, seconds, minutes, hours, characters, or
tokens.

![RaDUO ASR API key management](docs/screenshots/api-key-management.png)

### Dataset management and statistics

Inspect language, country, station, and category balance; review dataset
quality; and manage retry, cleanup, and purge operations.

![RaDUO dataset statistics and management](docs/screenshots/dataset.png)

### Activity logs

Follow the processing activity and see what the collector, recorder, and
transcription workers are doing behind the scenes.

![RaDUO activity logs](docs/screenshots/activity-logs.png)

## Project layout

```text
RaDUO/
├── radio_dataset.py       # Capture, transcription, cleanup, and export CLI
├── docs/screenshots/      # GUI screenshots used in this README
├── source/                # Optional station and STT configuration
└── dataset/               # Generated audio and metadata
    └── sample/             # Small synthetic public schema sample
        ├── README.md
        └── metadata.jsonl  # 35 placeholder rows; no audio
    ├── audio/<station>/*.wav
    ├── metadata.jsonl     # Source-of-truth record for each clip
    ├── metadata.csv       # Training-oriented metadata
    ├── dataset_readable.csv
    ├── dataset.xlsx
    ├── manifest.csv
    ├── word_timings/*.json
    ├── removed_rows.jsonl
    └── run_config.json
```

`source/stations.json` and `source/models.json` are optional. Without them, RaDUO uses the built-in station roster and built-in STT profiles. Use `init-config` when you want editable copies.

For a public repository, use
[`source/models.example.json`](source/models.example.json) as the configuration
template. Copy it to `source/models.json` locally and set credentials through
environment variables. [`.env.example`](.env.example) lists the supported
variable names. The real `source/models.json`, API keys, key-usage state,
generated audio, and generated dataset metadata must not be published.

The committed model configuration contains only placeholders. Replace
`example.invalid` and `your-model-name` in your local copy before collecting.

The repository includes a 35-row synthetic schema sample in
[`dataset/sample/metadata.jsonl`](dataset/sample/metadata.jsonl). It contains
no audio, real broadcast transcript, API key, or live provider endpoint and is
kept only to demonstrate the expected metadata shape.

## Requirements

- Python 3.10 or newer
- `ffmpeg` available on `PATH`
- Python packages:

  ```powershell
  python -m pip install requests openpyxl
  ```

- Access to at least one configured STT endpoint. Metered providers may also require an API key.

Check the installation before collecting:

```powershell
ffmpeg -version
python radio_dataset.py guide
```

## Quick start

Run these commands from the project directory:

```powershell
# Optional: write editable station and model configuration files
python radio_dataset.py init-config

# Check whether the configured radio streams are reachable
python radio_dataset.py probe

# Collect and transcribe approximately ten hours of material
python radio_dataset.py collect --hours 10

# Inspect counts, languages, stations, and processing status
python radio_dataset.py stats
```

The collector can be stopped with `Ctrl+C`; completed clips and metadata remain in `dataset/` and can be continued or exported later.

## Useful commands

```powershell
# Collect only selected stations or languages
python radio_dataset.py collect --only cantonese --only malay
python radio_dataset.py collect --only "Hong Kong" --exclude music

# Use a fixed clip-length range instead of the default distribution
python radio_dataset.py collect --min-sec 30 --max-sec 60

# Re-run transcription for failed clips
python radio_dataset.py retry

# Rebuild Excel and CSV exports from metadata.jsonl
python radio_dataset.py export

# Review or remove unusable audio and rows
python radio_dataset.py cleanup
python radio_dataset.py purge
```

Run `python radio_dataset.py <command> --help` for command-specific options. The complete built-in guide is also available with `python radio_dataset.py guide`.

## STT configuration

Use `source/models.json` to define providers, credentials, and language routes. Prefer environment variables for secrets rather than placing API keys in files:

```powershell
$env:ELEVENLABS_API_KEY = "your-key"
$env:REVOLAB_API_KEY = "your-key"
$env:DEEPGRAM_API_KEY = "your-key"
```

For a self-hosted OpenAI-compatible endpoint:

```powershell
$env:RADUO_STT_API = "http://localhost:8820/v1/audio/transcriptions"

python radio_dataset.py collect `
  --model qwen3-asr-1-7b
```

You can also pass the endpoint for one run with `--api`. RaDUO does not
provide a built-in remote STT gateway; configure your own endpoint before
starting a collection.

Every run writes its resolved provider, model, and route information to `dataset/run_config.json`. Do not commit API keys or other credentials.

## Open-source release checklist

Before publishing to GitHub:

1. Revoke and replace any API key that has ever appeared in a config file,
   terminal output, screenshot, commit, or generated metadata.
2. Publish source code, documentation, screenshots, and
   `source/models.example.json`; do not publish `source/models.json`.
3. Keep `dataset/` private unless you have permission to redistribute every
   recording, transcript, stream-derived artifact, and word-timing file.
4. Check the repository history and GitHub secret scanning before making the
   repository public. Removing a secret from the current file does not remove
   it from old commits.

## Dataset fields and quality review

`metadata.jsonl` is the canonical per-clip record. Common fields include:

- `audio_path`, `duration_sec`, `sample_rate`, and `channels`
- `station_id`, `station_name`, `country`, `region`, `city`, and `category`
- `station_language`, `asr_lang`, `asr_lang_norm`, and `lang_match`
- `text`, `status`, `keep`, and `note`
- `rms`, `dbfs`, `peak`, `voiced_ratio`, and `clipping_ratio`
- `word_timings` and `word_timing_status`, when supported by the STT provider

Before training, review at least the rows where `lang_match` is false, `status` is not `ok`, audio is clipped or mostly silent, and transcripts contain obvious recognition errors. Radio contains music, advertisements, overlapping speakers, background noise, code-switching, and broadcast content that may not be suitable for every ASR task.

## Legal and ethical use

Radio recordings, broadcasts, station streams, and generated transcripts may be protected by copyright, privacy, broadcaster terms, or other rights. You are responsible for obtaining permission where required and for complying with applicable law. Use reasonable connection limits, avoid unnecessary reconnections, and do not redistribute material unless you have the right to do so.

## Status

RaDUO is a dataset-preparation utility, not a finished model or a guarantee of transcript accuracy. Stream URLs and third-party APIs can change or become unavailable; run `probe` before long collections and preserve the `run_config.json` file alongside each dataset release for reproducibility.

## Community
Thanks to the [LINUX DO](https://linux.do/) community for providing an open and friendly platform for technical discussions.


