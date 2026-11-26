# LittleBit Chat

100% offline, private, Vulkan-accelerated AI chat for Android. No cloud, accounts or telemetry. Bring a GGUF model and keep your conversations on your phone.

![Android ARM64](https://img.shields.io/badge/Android_9%2B-ARM64-326149) ![Backends](https://img.shields.io/badge/Vulkan_%2B_Arm_KleidiAI-inference-344861) ![UI](https://img.shields.io/badge/Jetpack_Compose-Material_3-624979) [![Download release APK](https://img.shields.io/badge/Download-release_APK-136449)](https://github.com/aj5649169-svg/littlebit-chat/releases/latest)

## Demo

*Demo clip and screenshots coming soon.*
<!-- Edit this README on github.com and drag a short MP4 under 10 MB into this section. Leave the generated attachment URL on its own line for inline playback. Drag screenshots underneath it. -->

## Quick start

1. Open [Releases](https://github.com/aj5649169-svg/littlebit-chat/releases/latest) and download the signed ARM64 APK (about 15 MB). Model weights are separate.
2. Open the APK. If Android asks, allow **Install unknown apps** for the browser or file manager you used. You can turn this permission off after installation.
3. Open **Model Hub**. The catalog opens public model downloads in your browser. If you already have a GGUF, skip the download.
4. Tap **Load Local .gguf** and select the file with Android’s document picker. Supported local documents can load directly. Other providers may require an app-private copy. Reload the last model from the chat screen.
5. Start a chat. Choose **Fast** for short answers or **Think** for a reasoning model. Inference works in airplane mode.

| Phone RAM | Models to try |
| --- | --- |
| 4–6 GB | Qwen3 0.6B or 1.7B, Llama 3.2 1B |
| 6–8 GB | Qwen3 4B, Llama 3.2 3B |
| 8–12 GB | Qwen3 8B Q4_K_M, or IQ2_XS for a smaller footprint |
| 12 GB+ | Start with 8B. Explore the heavyweight catalog with a modest context window. |

RAM tiers are starting points. Model size, context length and memory used by other apps all matter.

## Inference and chat

- **Local engine.** Patched llama.cpp defaults to Vulkan offload and falls back to Arm KleidiAI CPU inference if GPU initialization fails. Tune GPU layers and CPU threads in Settings. Quick Benchmark uses a separate context to compare backends without clearing the active chat’s cache.
- **Streaming.** KV-prefix reuse avoids decoding unchanged chat history. Prefill reports completed tokens. Vulkan attempts Flash Attention with Q8_0 keys and values and can fall back to F16. Completed Markdown blocks are cached, and manual scrolling takes priority during generation.
- **Reading and writing.** Fast mode adds `/no_think`. Think mode supports collapsible reasoning. Replies support headings, tables, common LaTeX symbols, and fenced code blocks with a copy button. Tap the speed caption for time to first token, prefill, decode and context usage.
- **Local tools.** Attach text or code with **+**, use prompt templates, evaluate expressions with `/calc`, or enable local date/time context. Pick a system persona or write your own. Edit and resend, regenerate, continue a cut-off reply, search history, pin or rename conversations, and export Markdown.
- **Appearance.** Start a new chat in one tap. Choose System, Light, Dark or AMOLED Pure Black (#000000), with Emerald, Ocean Blue, Violet, Amber or Rose accents, 13/15/17 sp chat text and optional haptics.

## On-device measurements

Owner-reported results on a **Realme P3 Ultra, 12 GB RAM**, using **Qwen3-8B-Q4_K_M** (5.03 GB).

| Configuration | Workload | Reported speed |
| --- | --- | --- |
| Vulkan, 99 GPU layers | Sustained Think/code generation | 5.5–5.6 generated tokens/s |
| Vulkan, 99 GPU layers | Quick Benchmark prefill | 108.5 prompt tokens/s |
| Arm KleidiAI CPU, earlier build | Decode baseline | 2.7 generated tokens/s |

These measurements come from different runs. To compare on your phone, keep the model, thread count and context fixed, reload after changing backend, and run Quick Benchmark on each configuration.

## Build and credits

Clone with `git clone --recurse-submodules https://github.com/aj5649169-svg/littlebit-chat.git`. Run `bash scripts/apply-patches.sh` from the root. The [Android build workflow](.github/workflows/build-android-apk.yml) pins the JDK, Android SDK/NDK, Gradle and host Vulkan shader compiler. It runs `:app:assembleRelease` in `android-app/`, enables R8 and verifies the ARM64 APK signature. Pushes to main build an artifact. Version tags build and publish the APK and SHA-256 checksum. Release builds require the distribution keystore and its credentials. Configure `ANDROID_RELEASE_KEYSTORE_BASE64`, `ANDROID_RELEASE_STORE_PASSWORD`, `ANDROID_RELEASE_KEY_ALIAS`, and `ANDROID_RELEASE_KEY_PASSWORD` as repository Actions secrets. Keep the same signing key for subsequent updates. Debug builds use debug signing.

The [verified hardening build](https://github.com/aj5649169-svg/littlebit-chat/actions/runs/45613979747/attempts/2) includes chat backup exclusions, HTTPS link validation and JNI prefill error handling. Its [signed APK artifact](https://github.com/aj5649169-svg/littlebit-chat/actions/runs/45613979747/artifacts/15023878258) contains the changes since v1.1.0.

Built on [llama.cpp](https://github.com/ggml-org/llama.cpp) (pinned at `6aee508`), [Arm KleidiAI](https://github.com/ARM-software/kleidiai), and the LittleBit work from [GeniusDevam/littlebit-gguf](https://github.com/GeniusDevam/littlebit-gguf). The upstream MIT notice is preserved in [LICENSE](LICENSE). Third-party components and separately downloaded model weights retain their respective licenses.
