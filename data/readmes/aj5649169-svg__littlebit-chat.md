# LittleBit Chat

Private, on-device AI chat and image editing for Android ARM64. No accounts, no telemetry: bring a GGUF model and keep conversations and photos on your phone. The **Offline** edition has no network permission at all; the **Standard** edition adds opt-in web search and bring-your-own-key cloud APIs.

![Android ARM64](https://img.shields.io/badge/Android_9%2B-ARM64-326149) ![Engines](https://img.shields.io/badge/llama.cpp_%2B_stable--diffusion.cpp-on--device-344861) ![UI](https://img.shields.io/badge/Jetpack_Compose-Material_3-624979) [![Download release APK](https://img.shields.io/badge/Download-release_APK-136449)](https://github.com/aj5649169-svg/littlebit-chat/releases/latest)

## Two signed editions

| Edition | Network permission | What it adds |
| --- | --- | --- |
| **Offline** (`com.littlebit.chat`) | None. CI parses the merged release manifest and fails on `INTERNET`/`ACCESS_NETWORK_STATE`. | Chat, Model Hub, Image Studio, offline TTS, assistants and pinned notes, KV cache. Downloads open in your browser; nothing in the app can reach the network. |
| **Standard** (`com.littlebit.chat.standard`) | `INTERNET` only | Everything in Offline plus opt-in, per-message DuckDuckGo/SearXNG Web Search and a `Local | Cloud` mode for OpenAI-compatible APIs. Installs alongside Offline. |

Both editions are signed ARM64 APKs of about **41 MB**, bundling two native engines: patched `llama.cpp` (LittleBit `Q1_0` + Arm KleidiAI) and `stable-diffusion.cpp` in `libsd_jni.so`. Model weights are separate downloads and are never bundled.

## Quick start

1. Download the APK for the edition you want from [Releases](https://github.com/aj5649169-svg/littlebit-chat/releases/latest) and open it. If Android asks, allow **Install unknown apps** for the browser or file manager; you can revoke it afterwards.
2. Open **Model Hub** → **Load Local .gguf** and pick a model. Direct loading keeps Android's zero-copy file descriptor: nothing is copied, no extra storage is used, and multi-gigabyte models start immediately. Providers that cannot serve a seekable file offer a one-time **Private copy** instead.
3. Pick **Fast** for short answers or **Think** for reasoning models, then send. If a direct load ever fails, the model error card offers **Import private copy instead** in one tap.
4. For images, open **☰ → Image Studio**, choose a model, and generate or paint a mask over a photo.

## Model Hub and RAM fit

The catalog groups models into **0.55-Bit (LittleBit)**, **8B spotlight**, **Compact**, **Large 2-bit** and **Image**. Badges (`Great fit` / `Tight — use 2K ctx` / `May OOM`) and the **Fits my phone** filter are computed from **total device RAM** minus realistic Android OS headroom — not from the fluctuating `availMem` value — so results stay stable while other apps run.

- **0.55-Bit (LittleBit).** The exclusive `Q1_0` path sits right next to the 8B spotlight and carries an **Exclusive · Q1_0** badge. An 8B model fits in roughly 1.2 GiB of weights — an experimental early checkpoint for ultra-low-RAM testing, not an everyday model yet. Correctness and long-context quality are still being measured, and the entry links to the upstream conversion instructions rather than a prebuilt file.
- **8B spotlight.** Qwen3 8B, DeepSeek R1 0528 Qwen3 8B, Ministral 3 8B, Llama 3.1 8B and Qwen2.5 Coder 7B at roughly 2.8–3.8 GB. A 3.5 GB 2-bit 8B model is `Great fit` on a 12 GB phone and stays visible with **Fits my phone** on.
- **Image.** Verified Hugging Face links that open in the browser, so the Offline edition keeps zero internet permission:
  - **SD 1.5 Inpainting** — recommended for 6–8 GB phones such as the Exynos 1380; brush-mask photo inpainting. Ships as a single 1.9 GB `Q8_0` **`.gguf`** (no unsupported `.ckpt` checkpoint).
  - **SD-Turbo** — 1–4 step text-to-image at 512 px on 6–8 GB phones.
  - **Qwen-Image-2.1-Turbo (2-Bit)** — `AD-Q2_K`/`Q2_K` denoiser plus a 2-bit Qwen3-VL-8B text encoder, the Qwen Image 2.1 VAE and an optional `mmproj-F16` for photo edits.

### Diffusion files never reach llama.cpp

GGUF and SafeTensors are shared by chat and image models. Before a load or a private copy, Model Hub inspects the file name and the GGUF metadata (architecture, metadata keys, tensor names such as `model.diffusion_model.*`, `first_stage_model.*` or `cond_stage_model.*`). An image model is never handed to `llama.cpp` and never offered a private copy; the card reads **"This looks like an Image Studio model, not a text chat LLM."** with a one-tap **Open Image Studio** button, and any failed copy is cleaned up.

## Image Studio

The bundled `stable-diffusion.cpp` engine runs fully on-device. SD 1.5 / SD-Turbo use a single weights file; Qwen Image 2.1 Turbo takes denoiser, text encoder, VAE and optional vision projector slots.

`stable-diffusion.cpp` opens weights with `std::ifstream`, which Android 11–16 FUSE blocks for `/proc/self/fd/<N>`. Image Studio therefore **stages** a picked weight once into app-private storage:

- Headers and sizes are always read through `contentResolver.openInputStream(uri)`; no validator ever reopens a descriptor path by string.
- A file whose display name and byte size already match is reused instantly, with zero re-copying.
- Otherwise a confirmation dialog shows the exact size and a progress bar while the copy runs on `Dispatchers.IO`, writes `<name>.tmp`, and renames atomically. Cancelling or failing deletes the partial file.
- The active staged model name and size are shown in the slot card with a one-tap **Delete staged copy** button, and **Generate** enables once every required slot is staged.

**Cancel** stops a run, chat RAM is released before generation starts, and resolution chips scroll horizontally so `1024×1024` is never clipped. Results can be saved to Photos or shared.

## Chat

- **Engines.** Vulkan GPU offload by default, falling back to Arm KleidiAI CPU if initialization fails; tune GPU layers and threads in Settings. Quick Benchmark and **Auto-pick fastest backend** compare backends without clearing the active chat.
- **Streaming.** KV-prefix reuse avoids re-decoding unchanged history, prefill progress is reported per token, and completed Markdown blocks are cached while you scroll manually.
- **Ergonomics.** A floating **Jump to bottom** button appears when you scroll up (driven by `derivedStateOf`, never by reading `layoutInfo` in composition), Send hides the keyboard, and a thin **context usage bar** shows estimated used versus active context tokens.
- **Thinking.** ` thinking…</think>` and `<thinking>…</thinking>` are parsed identically, including a closing tag split across streaming chunks and cancelled partial thoughts. Reasoning stays in a collapsible card.
- **Attachments & plugins.** The `+` sheet uses rounded, elevated action rows with tinted leading icons, titles and subtitles instead of bare text lines.
- **Chat tools.** Attach text or code, use prompt templates, `/calc`, optional local clock context, system personas, edit-and-resend, regenerate, continue, forks, pin/rename/search chats, and Markdown export.

## Offline read-aloud

Every finished reply has a **Speak / Stop** control. `OfflineTtsController` uses the platform `TextToSpeech` engine (declared through a manifest `<queries>` entry, with no network permission), starts lazily on the first tap, and reports a readable message when no engine or matching voice is installed. `TtsTextSanitizer` strips reasoning blocks, fenced code and Markdown, then splits the text into sentence-safe chunks of at most 3,000 characters (`QUEUE_FLUSH` for the first, `QUEUE_ADD` for the rest). The engine is stopped and shut down in `onCleared()`.

## Assistants and pinned notes

Chat stays a blank scratchpad by default; nothing is blocked behind a character picker. **☰ → Assistants & Notes** offers three ready-made assistants plus **Create Assistant**:

- Each assistant stores a name, a system prompt and optional temperature, output-token and Think/Fast overrides. Existing v1.2.x custom personas migrate once into a **Custom** assistant.
- **Pinned context notes** can be global or per-chat, with a title, short text and an enabled toggle. Enabled notes are appended to the system context as an explicit user-authored block.

## Save KV cache (opt-in)

Settings → **Backend & Model** has **Save KV cache on disk**, off by default, and a **Clear KV cache (X.X MB)** button that reports real usage of `cacheDir/kv_cache/`.

- Saves `<chatId>.kv` plus `<chatId>.meta.json` (`modelFingerprint`, `nCtx`, `kvCacheType`, `backendMode`, `nGpuLayers`, `llamaCommit = 6aee508`, `savedTokenCount`, `promptHash`) through a `.tmp` file and an atomic rename.
- Restores only when every sidecar field and the conversation-prefix hash match. Any mismatch, corruption or failed load clears the KV memory, deletes the stale pair and falls back to a normal prefill — a cache miss is never a crash, and the native LCP check keeps token reuse safe.
- Keeps the two most recently used chats and evicts the rest.

## Standard edition: web search and cloud APIs

Web Search is per-message and opt-in. When it is on and snippets attach for a turn, the offline refusal clause is replaced with an explicit search-grounded instruction ("Live web search results are attached. Answer directly using these results and cite sources…"). When it is off, the strict offline grounding stays. Short or referential follow-ups ("now you can", "try again", "search it") are combined with the most recent substantive question by a pure `SearchQueryBuilder`, and the Sources sheet shows **Searched: "…"** at the top.

**Local | Cloud** is gated to the Standard edition: the interface and UI live in the shared source set, `CloudFactory` is a no-op in `offline` (no network imports, no permission) and a real `HttpURLConnection` client in `standard`.

- Presets: **OpenRouter** (`https://openrouter.ai/api/v1`, with `HTTP-Referer` and `X-Title: LittleBit Chat`), **NVIDIA NIM**, **Groq**, **Ollama (Local LAN)** and **Custom OpenAI-compatible**, plus a model-ID field and **Fetch models** (`GET /models`).
- Streaming `/v1/chat/completions` handles `data:` and `data: ` spellings, blank lines, `: OPENROUTER PROCESSING` keep-alives, `[DONE]`, `delta.reasoning_content`, `delta.reasoning`, inline thinking tags, `errorStream` bodies and immediate Stop via `disconnect()`.
- `CloudEndpointValidator` requires `https://` for every public host and allows cleartext `http://` only for `localhost`, `127.0.0.1`, `::1` and private `10.x` / `172.16–31.x` / `192.168.x` addresses. User info, query strings and fragments are rejected.
- API keys are encrypted with **AndroidKeyStore** (`AES/GCM/NoPadding`, randomized encryption, fresh 12-byte IV stored as `[IV || ciphertext]`), excluded from Android backups, never logged, and unreadable entries are cleared with a prompt to re-enter the key instead of crashing.

## Settings

Device & memory banner, backend and sampling sliders built on the lightweight `LittleBitSlider` (thin track, no tick dots, 16 dp thumb, haptic steps, numeric value pill), appearance (System/Light/Dark/AMOLED, accents, 13/15/17 sp), generation notification, auto-unload policy, KV cache controls, cloud panel (Standard only) and a readable last-crash log with real line breaks.

## What changed in 1.3.0

- **Image Studio input fix.** No component opens `/proc/self/fd/<N>` by string path any more; weights are validated through SAF streams and staged once into app-private storage with progress, atomic writes and a delete button. Top spacing and scrolling resolution chips fix the clipped UI.
- **Image models rejected by Model Hub.** A filename plus GGUF metadata guard stops diffusion files from reaching `llama.cpp` and offers **Open Image Studio** instead.
- **0.55-Bit (LittleBit).** The sub-1-bit tier is promoted next to the 8B spotlight with an **Exclusive · Q1_0** badge and an honest ~1.2 GiB RAM note.
- **Search grounding.** The system prompt switches between offline and search modes, follow-up queries are resolved against the previous substantive message, and the searched query is recorded on the message.
- **Polished UI.** Sheet action rows, aligned drawer icons, minimal sliders, jump-to-bottom, keyboard dismissal, context usage bar and both thinking tag forms.
- **Offline TTS.** Speak/Stop per reply with chunking and full lifecycle cleanup.
- **Assistants and pinned notes.** Optional one-tap personas and global/per-chat context notes.
- **KV cache.** Opt-in, LRU-limited save/restore with strict sidecar validation.
- **Cloud APIs.** Standard-only `Local | Cloud` streaming, presets, model listing and AndroidKeyStore key storage.
- **16 KiB ELF alignment (Android 15–16).** Both editions build with **NDK r28c (`28.2.13676358`)**. CI verifies both release APKs with `unzip -t`, `zipalign -c -P 16 4`, `apksigner verify --verbose`, `aapt2 dump badging` and an `llvm-readelf` 16 KiB `LOAD` alignment check on every packaged `.so`.

## What changed in 1.2.1

- No leaked SAF descriptors: provider `ParcelFileDescriptor`s are closed on load failure, model replacement and unload.
- Foreground-service stop race fixed with revision-gated stop intents.
- Stale private-copy prompts cleared on unload, unlink, dismissal or a successful copy.
- Honest RAM estimates derived from measured `totalMem`, so a "12 GB" phone is planned at ~9.5 GB.
- Supported inpainting download (public `Q8_0` `.gguf` instead of an unsupported `.ckpt`).
- Crash-log normalization for literal `\n`/`\r\n`/`\t` escapes.
- Image Studio in the drawer, opens without a loaded model and returns to Chat on system Back.

## Device testing status

Tested on Android 16 with a 12 GB phone and an 8 GB Exynos 1380 device: direct GGUF loading, 2-bit 8B chat, Model Hub RAM hints, Image Studio navigation and background generation. SD 1.5 Inpainting and Qwen Image 2.1 Turbo 2-bit were exercised on the 12 GB device; the 0.55-bit checkpoint, low-RAM timings and cloud providers are still being measured. Report device, RAM, model, quant and provider when filing an issue.

## Build and credits

Clone with `git clone --recurse-submodules https://github.com/aj5649169-svg/littlebit-chat.git`, then run `bash scripts/apply-patches.sh` from the root. It applies `patches/0001-littlebit.diff` (LittleBit `Q1_0`) and `patches/0002-android-saf-fd.diff` (Android SAF loading with a buffered-read fallback) against `llama.cpp` `6aee508`. The script is idempotent: already-applied patches are detected with `git apply --reverse --check` and skipped.

The [Android build workflow](.github/workflows/build-android-apk.yml) pins JDK 17, Android SDK, **NDK r28c (`28.2.13676358`)** for 16 KiB-aligned arm64 libraries, Gradle 8.10 and the host Vulkan shader compiler, runs the offline and standard unit tests, builds `:app:assembleRelease` for both flavors, then verifies **each** APK with `unzip -t`, `zipalign -c -P 16 4`, `apksigner verify --verbose`, `aapt2 dump badging` and a 16 KiB ELF `LOAD` alignment check on every packaged `.so` (`libllama_jni.so`, `libsd_jni.so`, `libc++_shared.so`). Pushes to `main` publish a build artifact; version tags publish both APKs with SHA-256 checksums. Release builds need `ANDROID_RELEASE_KEYSTORE_BASE64`, `ANDROID_RELEASE_STORE_PASSWORD`, `ANDROID_RELEASE_KEY_ALIAS` and `ANDROID_RELEASE_KEY_PASSWORD` as repository secrets; keep the same signing key for updates.

Built on [llama.cpp](https://github.com/ggml-org/llama.cpp) (pinned at `6aee508`), [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp), [Arm KleidiAI](https://github.com/ARM-software/kleidiai), and the LittleBit work from [GeniusDevam/littlebit-gguf](https://github.com/GeniusDevam/littlebit-gguf). The upstream MIT notice is preserved in [LICENSE](LICENSE). Third-party components and separately downloaded model weights retain their respective licenses.
