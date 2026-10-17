# PocketLLM

> Your AI lives on a USB stick. Plug in. Chat locally. Unplug. Zero footprint.

**No install. No cloud. No SSD space wasted. One command: `./launch.sh`**

PocketLLM is a portable USB toolkit for running local LLMs. It bundles everything — the Ollama runtime, model weights, a chat UI, and conversation history — on a single USB drive. Plug it into any Mac or Linux machine, run one command, and you have a fully working local AI. No install required on the host. On unplug, nothing remains.

**Inference speed from USB = SSD.** After the one-time model load, we benchmarked 54 tokens/sec on both. [See benchmarks.](#benchmarks)

## Quick Start

```bash
# First time — run setup from the USB
cd /Volumes/YOUR_USB/pocketllm
./setup.sh              # Downloads Ollama runtime + GPU libraries
./setup.sh gemma4:e2b   # Pull a model (optional — or copy one manually)

# Every time after
./launch.sh             # That's it
```

This opens a terminal chat and a web UI at `http://localhost:8080`. Press `Ctrl+C` to stop.

**No Ollama installation needed on the host machine.** Everything runs from the USB.

## How It Works

```
┌─────────────────────────────────────────────┐
│                 USB DRIVE                    │
│                                              │
│  bin/           models/         context/     │
│  ollama         GGUF weights    history.db   │
│  + GPU libs     (your models)   (encrypted)  │
│                                              │
│  ui/            config/         launch.sh    │
│  web chat       settings        (entry point)│
│  + skills                                    │
└──────────────────┬──────────────────────────┘
                   │ USB 3.x
                   ▼
┌─────────────────────────────────────────────┐
│           HOST MACHINE (borrowed)            │
│                                              │
│  CPU/GPU runs inference                      │
│  RAM loads model weights via mmap            │
│  Browser opens localhost:8080                │
│                                              │
│  Nothing installed. Nothing saved to disk.   │
└─────────────────────────────────────────────┘
```

The core trick: `launch.sh` sets `OLLAMA_MODELS` to point at the USB instead of the host's disk. Ollama reads weights directly from the drive. The host's CPU/GPU handles inference, but all storage lives on the USB.

## What's on the USB

```
pocketllm/
├── launch.sh              # Plug in and run this
├── setup.sh               # First-time setup (downloads Ollama runtime)
├── eject.sh               # Safe shutdown
├── sync.sh                # Dev tool — sync code from Mac to USB
│
├── bin/
│   ├── ollama-darwin       # macOS binary (Intel + Apple Silicon)
│   ├── ollama-linux        # Linux binary
│   └── lib/                # GPU acceleration libraries (Metal, etc.)
│
├── models/                 # Your model weights (GGUF format)
│   ├── manifests/          # Model registry
│   └── blobs/              # Weight files
│
├── ui/
│   ├── index.html          # Chat interface
│   └── skills/             # Drop-in JS plugins
│
├── config/
│   ├── settings.json       # Preferences
│   └── models.json         # Recommended models list
│
└── context/
    └── history.db          # Chat history (stays on USB)
```

## Features

- **Zero install** — no Ollama, no brew, no Docker needed on the host
- **Portable** — carry your AI workspace between machines
- **Private** — unplug and nothing remains on the host
- **Any model** — works with any Ollama-compatible model (Gemma, Llama, Mistral, Phi, etc.)
- **Web UI** — browser chat with markdown rendering, code blocks, conversation history
- **Terminal chat** — drops into interactive chat on launch
- **Skills** — extend the UI with drop-in JavaScript plugins
- **Cross-platform** — macOS (Intel + Apple Silicon) and Linux

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| USB Drive | 64GB, USB 3.0 | 128GB+, USB 3.2 Gen 2 |
| Host RAM | 8GB (small models) | 16GB+ (7B+ models) |
| Host OS | macOS 12+ / Ubuntu 20+ | macOS with Apple Silicon |

### Model Sizes

| Model | Disk | RAM Needed |
|-------|------|------------|
| Phi-3 mini (3.8B) | ~2.3GB | ~3GB |
| Mistral 7B | ~4.1GB | ~5GB |
| Gemma 4 e2b | ~7.2GB | ~9GB |
| Llama 3.1 8B | ~4.7GB | ~6GB |

## Benchmarks

Tested on MacBook Pro M4, 16GB RAM. Same prompt, same token count (capped at 100), cache purged between SSD and USB runs for fair cold-start comparison.

### Cold Start — Model Load Time

This is the one-time cost when you first chat after launching. The model weights get read from disk into RAM.

| Model | SSD Load | USB Load | Slowdown |
|-------|----------|----------|----------|
| gemma4:e2b (7.2GB) | 7.0s | 47.7s | ~7x slower |
| llama3.1:8b (4.9GB) | 11.0s | 29.8s | ~3x slower |

USB cold load takes longer — this is the real I/O penalty. But it **only happens once** when you start chatting. After that, the model stays in RAM.

### Inference Speed — After Model Is Loaded

Once the model is in RAM, storage speed is irrelevant. The M4 chip does all the work.

| Model | SSD tok/s | USB tok/s | SSD TTFT | USB TTFT |
|-------|-----------|-----------|----------|----------|
| gemma4:e2b | 53.9 | 54.0 | 0.08s | 0.12s |
| llama3.1:8b | 21.2 | 21.4 | 0.17s | 0.17s |

**Identical.** Zero difference in generation speed between SSD and USB.

### Key Takeaways

- **First load is slower from USB** (7–48s vs 7–11s) — you wait once, then it's the same
- **Inference speed is identical** — 54 tok/s on both SSD and USB for gemma4, 21 tok/s for llama3.1
- **gemma4:e2b** is 2.5x faster at token generation than llama3.1:8b
- **llama3.1:8b** uses less RAM (5.5GB vs 7GB) — better for 8GB machines
- The tradeoff: ~30–40 extra seconds on first launch for full portability and zero disk usage on the host
- **The cold load is USB's only bottleneck.** With a faster external drive (USB 3.2 SSD enclosure, Thunderbolt drive), that gap shrinks significantly. At that point, the only real limit is how much RAM the host machine has — that determines what size models you can run, and no storage upgrade can change it

## Adding Models

**Option 1** — Pull directly to USB:
```bash
./setup.sh gemma4:e2b
```

**Option 2** — Copy from an existing Ollama install:
```bash
cp -R ~/.ollama/models/* /Volumes/YOUR_USB/pocketllm/models/
```

Any model that works with Ollama works with PocketLLM.

## What This Solves (and Doesn't)

**Solves:** No 5–50GB of model weights permanently on your SSD. Carry models between machines. Zero trace on the host.

**Doesn't solve:** The host still needs enough RAM to run the model. A 7B model needs ~5–6GB RAM regardless of where the weights are stored. The host's CPU/GPU still does all the compute.

## For Developers

```bash
# Sync code changes from your dev machine to USB
./sync.sh YOUR_USB_NAME

# Add a UI skill
# Drop a .js file in ui/skills/ and register it in ui/skills/manifest.json
```

## License

MIT
