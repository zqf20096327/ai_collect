# ⚔️ ATHENA AI

### Your AI. Your Workspace. Your Intelligence.

Athena AI is a cross-platform AI-powered personal assistant designed to bring intelligent conversations, voice interaction, screen-aware assistance and local AI capabilities into one unified application.

Built with **Tauri, Rust, React and TypeScript**, Athena combines the flexibility of modern AI models with a powerful, customizable interface.

Whether you're using Windows, macOS, Linux or Android, Athena aims to provide an intelligent workspace that adapts to your device.

Choose between cloud-based AI providers and locally running models, interact with Athena using your voice, manage conversations, and access AI assistance without constantly switching between applications.

---

## 🚀 Platform Support

Athena is designed to support four major platforms.

| Platform | Architecture | Distribution |
|---|---|---|
| Windows | Desktop | `.exe`, `.msi` |
| macOS | Desktop | `.dmg` |
| Linux | Desktop | `.AppImage`, `.deb` |
| Android | Mobile | `.apk`, `.aab` |

Platform availability and feature compatibility depend on the published release.

### Windows
Full desktop-oriented Athena experience, including the main chat interface, desktop integrations, voice assistant and supported overlay functionality.

### macOS
Desktop experience adapted for macOS, with platform-specific application and permission handling.

### Linux
Desktop experience with Linux-compatible application packaging and supported integrations.

### Android
A dedicated mobile experience designed around touch interaction, responsive layouts, Android permissions and mobile lifecycle management.

Android functionality is developed separately where desktop APIs are unavailable.

---

## 📱 ATHENA MOBILE

Athena is being adapted into a dedicated Android application rather than simply shrinking the desktop interface.

### Mobile Interface

- Dedicated mobile chat interface.
- Responsive layouts for phones and tablets.
- Mobile-friendly navigation.
- Touch-optimised controls.
- Adaptive message input.
- Conversation history.
- Model selection.
- Provider configuration.
- Mobile settings.
- Android back-button support.
- Portrait and landscape compatibility.

### Mobile AI Assistant

- AI conversations.
- Streaming responses where supported.
- Model switching.
- Conversation persistence.
- File attachments where supported.
- Voice interaction.
- Read-aloud functionality.
- Provider-specific request handling.

### Android Screen Assistant

The mobile Screen Assistant is designed around Android's screen-capture permissions rather than desktop floating-window APIs.

Planned capabilities include:

- User-authorised screen capture.
- Screenshot previews.
- Asking questions about captured content.
- Vision-capable AI integration.
- Screenshot region selection or cropping.
- Temporary screenshot management.

Screen capture must use Android-supported permissions and APIs. Availability depends on the Android build and implementation.

### Mobile Local AI

Athena Local is being evaluated for Android-compatible inference.

Potential capabilities include:

- Compatible GGUF models.
- llama.cpp-based inference.
- Model importing.
- Model downloading.
- Model management.
- Memory compatibility checks.
- CPU inference.
- Supported hardware acceleration.

Local model support depends on device hardware, memory, runtime compatibility and the available Android implementation.

---

## 🧠 CORE FEATURES

### 🎙️ Voice Assistant

Interact with Athena naturally using your voice instead of typing every prompt.

- Wake Word Activation.
- Hands-Free Interaction.
- Voice Responses.
- ElevenLabs Integration.
- Custom Voice Settings.
- Stop Phrase.
- Kill Phrase.
- Listening Controls.
- Voice Feedback.

Voice functionality depends on the installed build, configuration and platform permissions.

### 🖥️ Screen Assistant

Access AI assistance through a dedicated on-screen interface.

- Quick Access.
- Screen-Aware Assistance.
- Screenshot Capture.
- Contextual Help.
- Screenshot Previews.
- Vision Model Integration.

Screen Assistant functionality varies by operating system. Desktop overlay functionality and Android screen capture use different platform-specific implementations.

### 🧠 Athena Local

Run compatible AI models locally.

- llama.cpp Integration.
- GGUF Model Support.
- Model Discovery.
- Hugging Face Integration.
- Repository Inspection.
- Selective Downloads.
- Model Management.
- Runtime Management.
- Inference Configuration.
- Offline Inference.

### 💬 AI Conversations

- Multiple conversations.
- Persistent conversation history.
- Streaming responses.
- Markdown rendering.
- Model selection.
- Conversation context.
- Memory support.
- File attachments where supported.
- Agent and Chat interaction modes.

### ⚡ Multiple AI Providers

Athena supports integrations with multiple AI providers.

- OpenAI-compatible API providers.
- Google Gemini.
- Groq.
- Anthropic, where supported by the build.
- Ollama.
- llama.cpp.
- Custom AI endpoints.

Provider availability depends on the configured integration and model.

### 📊 Token Usage Estimation

- Input token estimation.
- Live updates.
- Model-aware estimation where supported.
- Context awareness.
- Optional display through Settings.
- Local token estimation.

Estimated token counts may differ from actual provider usage.

### 🔊 Text-to-Speech

- Read-aloud functionality.
- ElevenLabs integration.
- Configurable voices.
- Playback controls.
- Interruptible playback where supported.

### 🧩 Tools & Integrations

- Integrated plugin architecture.
- Tool-assisted AI workflows.
- Configurable integrations.
- Voice and Screen Assistant integration.
- External service support.

### 🎨 Customisable Interface

- Custom themes.
- Obsidian Waves theme.
- Liquid Glass appearance.
- Custom backgrounds where supported.
- Configurable assistant behaviour.
- Responsive layouts.
- Dedicated Settings and Guides.

---

## 🏗️ TECHNOLOGY STACK

Athena uses a combination of modern web technologies and native application components.

| Technology | Purpose |
|---|---|
| React | User interface |
| TypeScript | Frontend architecture |
| Rust | Native backend |
| Tauri 2 | Desktop and Android application framework |
| Vite | Frontend development and bundling |
| Android SDK | Android application development |
| Gradle | Android build system |
| llama.cpp | Local AI inference |
| GGUF | Local model format |

The application uses shared frontend and backend components where practical, with platform-specific implementations for operating-system-dependent functionality.

---

## 🔐 SECURITY & PRIVACY

Athena is designed with user-controlled AI provider configuration and local inference capabilities.

Security considerations include:

- Secure handling of provider credentials.
- Platform-specific credential storage where supported.
- Production build optimisation.
- Restricted application permissions.
- Input validation.
- Application integrity considerations.
- Platform-native signing support.
- Local model inference.
- User-controlled provider selection.

**Privacy note:** Cloud AI providers may process prompts and attachments sent to their services. Local inference can keep supported model processing on-device. Review the selected provider's data-handling policies before sending sensitive information.

No desktop or mobile application can be made completely immune to reverse engineering.

---

## 📥 DOWNLOADS

**[Download the Latest Athena AI Release](https://github.com/lord-kirby-kirk69/Athena-Ai-Downloads/releases/latest)**

Choose the installer compatible with your operating system and processor.

| Operating System | Format |
|---|---|
| Windows | `.exe` / `.msi` |
| Linux | `.AppImage` / `.deb` |
| macOS | `.dmg` |
| Android | `.apk`, if published |

Check release notes for available architectures and platform-specific limitations.

---

## 🛠️ BUILDING ATHENA FROM SOURCE

The following instructions are intended for developers with access to the Athena source repository.

### Prerequisites

- Node.js and npm.
- Rust toolchain.
- Tauri CLI.
- Git.
- Android Studio for Android development.
- Android SDK.
- Android NDK.
- Java JDK compatible with the Android Gradle configuration.

### Desktop Development

Install dependencies:

```bash
npm install
```

Start Athena on desktop:

```bash
npm run tauri dev
```

Create a desktop production build:

```bash
npm run tauri build
```

### Android Development

Configure the Android development environment and install the required Rust Android targets.

For the Android emulator, launch your virtual device through Android Studio.

Check connected devices:

```bash
adb devices
```

Start Android development:

```bash
npm run tauri android dev
```

### Android Production Build

Generate an Android package:

```bash
npm run tauri android build
```

To request an APK where supported by the configured Tauri CLI:

```bash
npm run tauri android build -- --apk
```

Android build outputs are generally located under:

```text
src-tauri/gen/android/app/build/outputs/
```

The exact output directory depends on the selected build variant.

### Android Architecture

Athena's Android build uses Tauri's Android integration.

Platform-specific Rust code must be isolated appropriately to prevent desktop-only APIs from breaking Android compilation.

Desktop and Android builds should be tested independently.

---

## ⚙️ GETTING STARTED

1. Download the latest compatible Athena release.
2. Install and launch the application.
3. Complete initial setup.
4. Open provider or model settings.
5. Configure an AI provider or compatible local model.
6. Enter the required API credentials.
7. Save your settings.
8. Start chatting with Athena.

Some providers require an API key, internet access or a separate account.

For local inference, install the supported runtime and download or import a compatible GGUF model.

---

## 🎙️ VOICE ASSISTANT SETUP

1. Open Athena.
2. Navigate to Voice Assistant settings.
3. Configure available voice options.
4. Grant microphone permission when requested.
5. Enable the assistant.
6. Use the configured wake phrase.
7. Speak your request.

Speech recognition and synthesis availability depend on the selected implementation and platform.

---

## 🖥️ SCREEN ASSISTANT SETUP

1. Launch Athena.
2. Open Settings.
3. Navigate to Screen Assistant.
4. Configure the available controls.
5. Grant required permissions.
6. Open the assistant using its configured shortcut or supported mobile interface.

Screen capture functionality differs between desktop and Android.

---

## 🧠 ATHENA LOCAL SETUP

1. Open Model Hub or Athena Local.
2. Install the supported inference runtime.
3. Browse available model repositories.
4. Inspect model files.
5. Select a compatible GGUF model.
6. Download or import it.
7. Configure inference settings.
8. Load the model.
9. Start a local conversation.

Model performance depends on available RAM, CPU, GPU, quantization and model size.

Do not automatically load models that exceed device memory.

---

## 🔑 GOOGLE GEMINI API KEY

Athena supports Google Gemini where the integration is available.

1. Visit [Google AI Studio](https://aistudio.google.com/apikey).
2. Sign in.
3. Create an API key.
4. Open Athena provider settings.
5. Select Google Gemini.
6. Enter your API key.
7. Save the configuration.

Google's free usage tiers are subject to current quotas, eligibility and terms.

Official documentation: [Gemini API Key Guide](https://ai.google.dev/gemini-api/docs/api-key)

---

## 🛡️ PRIVACY & DATA HANDLING

- Cloud provider requests may leave your device.
- Screen captures may contain sensitive information.
- Local inference can process supported prompts without a cloud provider.
- API credentials should remain private.
- Avoid sending passwords, banking information or confidential documents to external AI services.
- Review provider policies before using sensitive information.

---

## 🧰 TROUBLESHOOTING

### Athena does not launch

- Check that you downloaded the correct installer.
- Verify system compatibility.
- Reinstall the application if necessary.
- Check release notes for known issues.

### AI responses are not working

- Verify internet connectivity.
- Check provider configuration.
- Verify API credentials.
- Check model availability and provider limits.

### Android build fails

- Verify Android SDK installation.
- Verify Android NDK installation.
- Check Java compatibility.
- Check installed Rust Android targets.
- Confirm that the emulator is running.
- Review Rust and Gradle compilation errors.

### Voice assistant does not work

- Check microphone permissions.
- Verify the selected speech provider.
- Check wake-word configuration.
- Restart the voice assistant.

### Screen Assistant does not work

- Verify platform support.
- Check operating-system permissions.
- Check the configured shortcut.
- Review release notes for known limitations.

---

## 🔄 UPDATES

New releases, installers and fixes are published here:

[**Athena AI Releases**](https://github.com/lord-kirby-kirk69/Athena-Ai-Downloads/releases)

Check release notes before updating. Back up important local data before installing a new version.

---

## ⚖️ LEGAL & USAGE

Athena AI is distributed as compiled application software. Downloading the application does not transfer ownership of its intellectual property.

Third-party components may be subject to their respective licences.

AI-generated responses may be inaccurate or incomplete. Verify important information independently before relying on it.

---

## 📂 SOURCE CODE

This repository is dedicated to distributing Athena AI installers and release information.

The application's source code is maintained separately and is not included in this downloads repository.

---

<p align="center">

# ⚔️ ATHENA AI

**Your AI. Your Workspace. Your Intelligence.**

*Intelligence, shaped around your workspace.*

© 2026 N Nishchith Sharma. All rights reserved.

</p>
