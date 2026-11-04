<div align="center">
  <img src="crates/minimlx-gpui/assets/brand/AppIcon.png" width="128" alt="MiniMLX icon" />
  <h1>MiniMLX</h1>
  <p><strong>Run models faster. Keep things simple.</strong><br />
  Your favorite AI models, ready to run on your Mac.</p>
  <p>
    <img src="https://img.shields.io/badge/platform-Apple%20Silicon-111827?style=flat-square" alt="Apple Silicon" />
    <img src="https://img.shields.io/badge/powered%20by-MLX-2563eb?style=flat-square" alt="Powered by MLX" />
    <img src="https://img.shields.io/badge/API-OpenAI%20compatible-10b981?style=flat-square" alt="OpenAI-compatible API" />
    <img src="https://img.shields.io/badge/license-Apache--2.0-64748b?style=flat-square" alt="Apache 2.0 license" />
  </p>
  <p>
    <a href="#install">Install</a> ·
    <a href="#featured-models">Featured models</a> ·
    <a href="#features">Features</a> ·
    <a href="#quickstart">Quickstart</a> ·
    <a href="#connect-your-apps">Connect your apps</a> ·
    <a href="#license">License</a>
  </p>
  <p><strong>English</strong> · <a href="README.zh.md">简体中文</a></p>
</div>

---

<p align="center">
  <img src="docs/images/overview.png" alt="MiniMLX overview showing a running model, inference service, and system resources" width="100%" />
</p>

A powerful model shouldn't come with a complicated setup. MiniMLX brings model downloads, local inference, and an API server into one native Mac app. Pick a model, start the service, and put it to work.

## Featured models

MiniMLX supports a broad range of popular MLX-format models available on Hugging Face, including Qwen and Llama. Discover new models in the app or bring the ones you already have — from compact everyday models to more demanding choices, they're all at home in the same library.

We're especially focused on making **Qwen3.8 Flash Next** and **Qwen3.8 27B** great to use on your Mac. Both can be discovered and managed in MiniMLX, and compatible Flash Next configurations can take advantage of MTP acceleration. If you're looking for a place to start, try searching for:

- `mlx-community/Qwen3.8-Flash-Next-4bit-mtp`
- `mlx-community/Qwen3.8-27B-4bit`

These are just two examples of the models you can explore. Compatibility, memory requirements, and performance depend on the exact checkpoint and your Mac; larger models can require substantial memory and disk space.

## Features

### Find your next model

Search **Hugging Face** and **ModelScope** from MiniMLX. Compare model details, download the checkpoints you want, and keep track of your collection without juggling folders and terminal commands.

Already have models on your Mac? Add your existing model directories and manage them alongside your downloads. You can pause and resume downloads, inspect model information, and load or unload models from one place.

### Made for your Mac

MiniMLX is built for Apple Silicon and designed around a native macOS experience. It considers your available memory when loading supported models, so you can spend less time working out how to fit a model and more time using it.

Model settings let you adjust supported options for your machine and your workload. MiniMLX also makes it possible to use certain larger models when they do not fit entirely in available memory; support and speed vary by model and hardware.

### Faster when it matters

Get more from compatible models with acceleration features such as MTP. For supported models, you can adjust performance-related settings to find a balance that works for your Mac.

Run the built-in performance test to see prompt processing, generation speed, latency, and memory use across the context lengths you care about. Keep a history of results and export them when you want to compare.

### Your models, ready for your apps

Start a local inference service with a click and connect applications that support an **OpenAI-compatible API**. MiniMLX shows the server address and lets you copy the model name your client needs.

Use your local models for chat, coding, or your own projects while managing the service from one familiar interface. The address, port, and optional authentication are configurable in Settings.

### Everything at a glance

See the active model, service state, requests, token throughput, memory use, and GPU activity in the overview. When you need more detail, inspect model information or run a performance test without leaving the app.

Keep MiniMLX close at hand in the macOS menu bar. Show or hide the main window, check service status, and start or stop the service when you need it. You can also choose whether the window appears when MiniMLX starts.

## Install

### macOS app

Download the Apple Silicon DMG from [GitHub Releases](https://github.com/shijizhi/MiniMLX/releases). Open the DMG, drag **MiniMLX** into **Applications**, and launch it.

The release DMG is signed with Developer ID and notarized by Apple. Models are downloaded separately.

**Requirements:** a Mac with Apple Silicon. Available memory, free disk space, and the model you choose affect what you can run. The minimum supported macOS version has not yet been established.

## Quickstart

1. Open **MiniMLX** from Applications.
2. In **Models**, search for a compatible model or add one already on your Mac.
3. Download and load the model, then start the inference service. MiniMLX can also prompt you to choose a model when you start the service.
4. Connect your app to the local API and use the model name copied from MiniMLX.

That's it. MiniMLX keeps the model, service, and performance information within reach as you work.

## Connect your apps

The default base URL for OpenAI-compatible clients is:

```text
http://127.0.0.1:18765/v1
```

Use the API model name copied from MiniMLX or check the model exposed by the service:

```bash
curl http://127.0.0.1:18765/v1/models
```

To send a chat request, replace `YOUR_MODEL_ID` with the model name shown by MiniMLX:

```bash
curl http://127.0.0.1:18765/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "YOUR_MODEL_ID",
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 128
  }'
```

If you enable API authentication, include your configured key as a Bearer token. The listen address and port can be changed in Settings.

## License

MiniMLX is open source under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for third-party attribution.
