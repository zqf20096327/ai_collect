# EdgeAI Kit 🧠📱

**The missing UI toolkit for on-device LLMs in Flutter.**

[![Flutter](https://img.shields.io/badge/Flutter-3.41+-blue.svg)](https://flutter.dev)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)

EdgeAI Kit fills the gap between `flutter_gemma` (inference engine) and what developers actually need: device capability checks, model management UI, onboarding flows, and ready-made chat/vision/tool-calling widgets.

**Inspired by [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery)** (22.5k ⭐) — rebuilt for Flutter.

## Screenshots

<p align="center">
  <img src="screenshots/04_chat.jpg" width="180" alt="AI Chat" />
  <img src="screenshots/01_tool_use.jpg" width="180" alt="Function Calling" />
  <img src="screenshots/02_benchmark.jpg" width="180" alt="Benchmark" />
  <img src="screenshots/03_prompt_lab.jpg" width="180" alt="Prompt Lab" />
  <img src="screenshots/05_models.jpg" width="180" alt="Model Management" />
</p>

## Features

| Feature | Description |
|---------|-------------|
| 🔍 **Device Capability Check** | Detect RAM, GPU, storage, chipset. Classify device tier. |
| 📋 **Model Catalog** | 7 models with metadata, sizes, capability badges |
| 🎯 **Model Recommendations** | Score models against device profile — "Great fit" / "Not enough RAM" |
| 🚀 **Onboarding Flow** | First-launch: scan device → recommend → one-tap download → ready |
| 💬 **AI Chat** | Multi-turn streaming conversation with markdown rendering |
| 🖼️ **Ask Image** | Camera/gallery → model analyzes image on-device |
| 🛠️ **Tool Use** | Real function calling — weather API, time, calculator with tool call visualization |
| 🧠 **Thinking Mode** | Chain-of-thought reasoning visualization |
| ⚙️ **Prompt Lab** | Test prompts with temperature, top-k, max tokens sliders |
| 📊 **Benchmark** | Measure tokens/sec, TTFT on your device |
| 💾 **Storage Management** | Delete models, storage usage bar, multi-model management |
| 🎨 **Material 3 Theme** | Light + dark, ColorScheme.fromSeed, Google AI Edge Gallery style |

## Supported Models

| Model | Size | Vision | Audio | Tools | Thinking |
|-------|------|:------:|:-----:|:-----:|:--------:|
| Gemma 4 E2B | 2.4 GB | ✅ | ✅ | ✅ | ✅ |
| Gemma 4 E4B | 4.3 GB | ✅ | ✅ | ✅ | ✅ |
| Gemma 3 1B | 0.5 GB | | | ✅ | |
| DeepSeek R1 1.5B | 1.86 GB | | | ✅ | ✅ |
| Qwen3 0.6B | 586 MB | | | ✅ | ✅ |
| Phi-4 Mini | 3.94 GB | | | ✅ | |
| SmolLM 135M | 167 MB | | | | |

## Installation

**Git dependency** (add to your `pubspec.yaml`):
```yaml
dependencies:
  edge_ai_kit:
    git:
      url: https://github.com/sumitvairagar/edge-ai-kit.git
```

**Or clone and run the demo app:**
```bash
git clone https://github.com/sumitvairagar/edge-ai-kit.git
cd edge-ai-kit
flutter run
```

## Quick Start

```dart
import 'package:edge_ai_kit/edge_ai_kit.dart';

// Initialize
LLMService.initialize();

// Check device capabilities
final profile = await DeviceCapabilityChecker.check();
final recommendations = DeviceCapabilityChecker.recommendModels(profile);

// Download & load a model
await LLMService.install(ModelCatalog.all.first);
await LLMService.load(ModelCatalog.all.first);

// Use ChatView widget
ChatView(
  messages: messages,
  generating: isGenerating,
  onSend: (text) => handleSend(text),
  suggestions: ['Tell me a joke', 'What is Flutter?'],
)
```

## Architecture

```
lib/
├── edge_ai_kit.dart              # Package barrel export
├── src/
│   ├── device/
│   │   └── device_checker.dart   # RAM/GPU/storage detection + recommendations
│   ├── models/
│   │   └── model_catalog.dart    # Model registry with metadata
│   ├── services/
│   │   ├── llm_service.dart      # flutter_gemma wrapper
│   │   └── tool_executor.dart    # Real tool implementations
│   ├── widgets/
│   │   └── chat_view.dart        # Shared chat UI component
│   └── theme/
│       └── app_theme.dart        # Material 3 theme
└── ui/screens/                   # Demo app screens (8 screens)
```

## ChatView Message Types

```dart
ChatMessage.user('Hello!')                    // User bubble
ChatMessage.ai('Here is the **answer**...')   // AI bubble (markdown, streaming)
ChatMessage.thinking('Let me analyze...')     // Thinking block (collapsible)
ChatMessage.toolCall(name: 'get_weather',     // Tool call card (JSON)
  input: {...}, output: {...})
ChatMessage.loading()                         // Loading indicator
```

## Device Capability Check

```dart
final profile = await DeviceCapabilityChecker.check();
print(profile.totalRamMB);      // 8192
print(profile.tier);             // DeviceTier.high
print(profile.gpuRenderer);      // "OpenGL ES 3.1+"

final recs = DeviceCapabilityChecker.recommendModels(profile);
for (final rec in recs) {
  print('${rec.model.name}: ${rec.fit} — ${rec.reason}');
  // Gemma 4 E2B: ModelFit.great — Great fit for your device
}
```

## Benchmark Results (Gemma 4 E4B on Snapdragon)

| Metric | Value |
|--------|-------|
| Tokens/sec | 13.0 tok/s |
| Time to First Token | 475 ms |
| Total Tokens | 250 |
| Total Time | 18.6 sec |

## Requirements

- Flutter 3.41+
- Android 12+ / iOS 16+
- 4GB+ RAM recommended

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding models, screens, and code style.

## License

Apache 2.0 — see [LICENSE](LICENSE).

## Credits

Built with [flutter_gemma](https://pub.dev/packages/flutter_gemma) by [DenisovAV](https://github.com/DenisovAV).
