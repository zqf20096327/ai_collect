# 🦜 Macaw — the Siri you always wanted, that's actually yours

**Macaw is a private AI model that runs entirely on your Mac and controls it** — 97 verified tools for mail, files, calendar, music, system settings, and multi-step chains, in plain English. No cloud, no accounts, no payments.

It's **live today** — not a waitlist. Weights on Hugging Face, source right here, MIT code, fully local on Apple Silicon.

- **Model weights:** [`badtheorylabs/Macaw`](https://huggingface.co/badtheorylabs/Macaw) (BF16) · [`badtheorylabs/Macaw-4bit-MLX`](https://huggingface.co/badtheorylabs/Macaw-4bit-MLX) (~1.5 GB on-device build)
- **Measured (Apple M2, 4-bit):** 10/10 tool-call accuracy · 1.21 s mean request · ~40 tok/s decode
- **Architecture:** fine-tune of [Liquid AI LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
- **Landing page:** [badtheorylabs.com/macaw](https://badtheorylabs.com/macaw)

---

## Quick start

### 1. Serve the model

```bash
pip install mlx mlx-lm
python -m mlx_lm.server --model badtheorylabs/Macaw-4bit-MLX --port 8138
```

### 2. Run the macOS app

```bash
swift build          # in app/
```

The app runs in the menu bar, starts the server automatically (point `MACAW_PYTHON` at a Python with mlx-lm if it's not on your PATH), and exposes a floating prompt bar (⌥ Space). The model can then call the 97 macOS tools in `runtime/tools.json`.


### Install the runtime

Seven tools (screen reading, document reading, app control) shell out to helper
scripts. Put them where the tools expect to find them:

```bash
mkdir -p ~/.macaw
cp runtime/*.py runtime/tools.json runtime/tools_prompt.json ~/.macaw/
```

Point `MACAW_PYTHON` at a Python that has `mlx-lm` and `pyobjc` if it isn't your
default:

```bash
export MACAW_PYTHON=/path/to/python
export MACAW_HOME=~/.macaw        # only if you put them elsewhere
```

Screen reading also needs **Screen Recording** permission, and app control needs
**Accessibility** — both in System Settings › Privacy & Security. macOS will
prompt the first time each is used.

### 3. CLI agent (optional)

```bash
pip install mlx mlx-lm pyobjc-framework-Vision
python runtime/agent.py          # multi-turn agent loop
python runtime/loop.py           # autonomous loop, terminal-style
```

---

## How it works

```
┌─────────────────────────────────────────────┐
│  Macaw app (Swift, menu bar)                │
│  ─ prompt bar → /v1/chat/completions        │
│  ─ tool schema from tools.json (top-12 by   │
│    retrieval)                               │
│  ─ tool name + args checked, then executed  │
│    (model never writes the AppleScript)     │
└──────────────────────┬──────────────────────┘
                       │ 127.0.0.1:8138
┌──────────────────────▼──────────────────────┐
│  mlx_lm server — Macaw-4bit-MLX on Metal    │
│  on-device, no network                      │
└─────────────────────────────────────────────┘
```

**Prompt hygiene.** The model was fine-tuned to emit a tool call immediately after the assistant turn — no `<think>` preamble. The shipped `chat_template.jinja` is patched so generation doesn't prefill `<think>`, which would otherwise cost ~20 s of reasoning per request. The app sends a `system` message ("You are Macaw, an on-device AI assistant running on this Mac.") so the model presents as Macaw rather than its base identity.

**Safety.** Only a tool name plus literal arguments cross from model to machine, validated against `tools.json`. The model never produces the AppleScript that runs; the app does. Untrusted text the model reads (mail, filenames, web pages) can never talk it into executing arbitrary script.

## Repository layout

```
app/         macOS menu-bar app (Swift/SwiftUI)
runtime/     Python agent loop, tool executor, screen reader, benchmark
landing/     Launch page (static HTML)
```

`app/` needs macOS 14+ and the model server. `runtime/` needs Python 3.10+ with `mlx`, `mlx-lm`, and on macOS `pyobjc-framework-Vision` for screen reading.

## Benchmarks

`runtime/bench.py` measures end-to-end tool-call accuracy and latency against the live server:

| Metric | Value |
| --- | --- |
| Tool-call accuracy | 10/10 |
| Mean request | 1.21 s |
| Median request | 1.14 s |
| Best request | 0.77 s |
| Decode | 40.3 tok/s |

## License

- **Code in this repo:** [MIT](LICENSE)
- **Model weights:** derivatives of LFM2.5-2.6B under the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-2.6B/raw/main/LICENSE). Redistribution must retain that license and Liquid AI attribution; commercial use is restricted for entities ≥ $10M annual revenue.

## Contact

Bad Theory Labs · model repos on [Hugging Face](https://huggingface.co/badtheorylabs)
