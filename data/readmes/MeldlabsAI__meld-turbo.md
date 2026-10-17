<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/media/logo-dark.svg">
    <img src="docs/media/logo-light.svg" width="96" alt="Meld Labs">
  </picture>
</p>
<h1 align="center">Meld Turbo</h1>

<p align="center"><strong>A 125B-parameter model, fully local, on a MacBook.</strong><br>
Qwen3.8-Flash-Next at ~45 tokens/s on Apple silicon — and ~35 tokens/s with 32K tokens of context. No cloud, no API key, nothing leaves your Mac.</p>

<p align="center">🏁 <b>~45 tokens/s on a 2023 MacBook Pro (M2 Max) — and it fits in 64 GB</b><br>
<sub>64 GB measured in a simulation so far — <a href="https://github.com/MeldlabsAI/meld-turbo/issues/1">help us confirm it on a real one</a></sub></p>

<p align="center">
  <a href="https://meldlabs.ai/meld-turbo"><b>Project page</b></a> ·
  <a href="https://huggingface.co/meldlabs"><b>Hugging Face</b></a> ·
  <a href="#quick-start"><b>Quick start</b></a> ·
  <a href="docs/PERFORMANCE.md">Performance notes</a> ·
  <a href="https://meldlabs.ai/research/meld-turbo-performance">Research write-up</a>
</p>

<p align="center">
  <img alt="Apple silicon" src="https://img.shields.io/badge/Apple%20silicon-M2%20Max%2B-black">
  <img alt="macOS" src="https://img.shields.io/badge/macOS-14%2B-black">
  <img alt="engine" src="https://img.shields.io/badge/engine-llama.cpp%20%2B%20patches-orange">
  <img alt="API" src="https://img.shields.io/badge/API-OpenAI--compatible-brightgreen">
  <img alt="MIT" src="https://img.shields.io/badge/license-MIT-blue">
</p>

---

**News**

- **2026-10-17** · [Meld Turbo 0.1.1](https://github.com/MeldlabsAI/meld-turbo/releases/tag/v0.1.1): a quality profile, code edits up to ~130 tok/s, ~33–37 tok/s at 32K context, faster prompts, and the Messages and Ollama APIs on the same port.
- **2026-10-17** · New on Hugging Face: [the quality profile's model file](https://huggingface.co/meldlabs/Qwen3.8-Flash-Next-Meld-Turbo-Quality-GGUF) (EXL3 experts, 2.625 bits per weight, 96 GB Macs): HumanEval 97.6%, MMLU 87.5%.

**Meld Turbo** runs **Qwen3.8-Flash-Next** — a Mixture-of-Experts model with 125B parameters, 6B of them active per token — on a single Mac, behind an OpenAI-compatible API. Any chat client, coding agent or script that speaks that API can use it — for example the [Pi coding agent](https://github.com/earendil-works/pi) ([setup below](#use-it)).

Models of this size are usually served from a GPU cluster. A MoE model only reads a small part of its weights for each token, though, and Apple silicon puts a large, fast unified memory right next to the GPU. Meld Turbo is the set of engine changes, tools and settings that turns that into a usable local model: **~40–47 tokens/s** of generation on a MacBook Pro with an M2 Max and 96 GB, **~33–37 tokens/s** with 32K tokens of context, and up to **~130 tokens/s** when a reply repeats much of its input (edits, rewrites).

It is the first open-source release from [Meld Labs](https://meldlabs.ai).

https://github.com/user-attachments/assets/5787a5b1-2af7-41f1-9bef-a13976c2e2f4

<p align="center"><sub>Real use on a MacBook Pro M2 Max, 96 GB: the built-in chat UI writing a Python script, thinking off. Idle pauses are trimmed; the speed is not edited.<br>
<b>No player above?</b> Open <a href="docs/media/meld-turbo-demo.mp4">docs/media/meld-turbo-demo.mp4</a> — the same video — in this repository.</sub></p>

## Results

MacBook Pro 14" · M2 Max (38-core GPU) · 96 GB · ~400 GB/s

| | **fast** (default) | **quality** |
|---|---|---|
| **Generation** | ~40–47 tok/s on code and English, ~41 tok/s on Chinese; ~33–37 tok/s at 32K context | ~35 tok/s on short open-ended replies; ~31 tok/s at 32K context |
| **Edits and rewrites** | up to ~130 tok/s | up to ~95 tok/s |
| **Prompt processing** | ~335–350 tok/s up to 16K tokens, ~315–325 tok/s at 32K | ~290 tok/s up to 16K tokens, ~275 tok/s at 32K |
| **Task scores** (GSM8K / HumanEval / MMLU) | 98.0% / 93.3% / 82.5% | 96.5% / 97.6% / 87.5% |
| **Memory** | ~53 GB on 96 GB Macs, ~45–50 GB on 64 GB Macs | ~56 GB, 96 GB Macs only |
| **On disk** | ~68 GB | ~75 GB |
| **Context** | 128K tokens | 128K tokens |

Numbers are end-to-end through the API with speculative decoding on; task scores are greedy with thinking off. Generation speed depends on the reply: text that restates the prompt is faster, open-ended writing is at the low end. See [docs/PERFORMANCE.md](docs/PERFORMANCE.md) for how they were measured, including the task-score subsets.

To our knowledge, as of October 17, 2026, this is the fastest generation for Qwen3.8-Flash-Next on an M2 Max with 64 or 96 GB.

## Which profile?

Both profiles run the same model with the same engine; they differ in how the experts are stored.

- **fast** — 2-bit experts. The fastest option, and the one that fits 64 GB Macs. Start here.
- **quality** — EXL3 experts at 2.625 bits per weight. Better answers on code and knowledge questions (HumanEval 98% vs 93%, MMLU 88% vs 83%), at about 15% lower generation speed on short replies (~5% at 32K context). Needs a Mac with 96 GB or more.

Not sure? Use **fast**. On a 96 GB Mac where answer quality matters more than speed, use **quality**. You can install both and switch with `PROFILE=` at start.

## Quick start

You need a Mac with Apple silicon (Max-class GPU or better) and **64 GB of unified memory or more** (96 GB recommended, and required for the quality profile), plus Xcode command-line tools, CMake, Python 3 with `numpy`, and about 110 GB of free disk for one profile.

Tested on 96 GB. **64 GB works in a simulation** on the 96 GB Mac (GPU memory capped at the 48 GB that macOS allows on a 64 GB machine, 27–32 GB of RAM locked away): with the default settings the server uses ~45–50 GB and generates at ~39 tok/s on short replies and ~32 tok/s at 32K context, up to ~120 tok/s on edits, with prompts at ~230–265 tok/s. Close memory-heavy apps first (the rest of the system swaps), and if the server does not start, try `CTX=32768`. Have a real 64 GB Mac? Please post a run in [issue #1](https://github.com/MeldlabsAI/meld-turbo/issues/1).

**1. Build** (both profiles):

```zsh
git clone https://github.com/MeldlabsAI/meld-turbo && cd meld-turbo
./setup.sh                      # fetch llama.cpp, apply patches/, build with Metal
pip install -U huggingface_hub  # for the downloads below
M=~/.meld-turbo/models; mkdir -p $M
hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "MTP/mtp-Qwen3.8-Flash-Next-shared-Q8_0.gguf" --local-dir $M
mv $M/MTP/*.gguf $M/            # the MTP draft head, used by both profiles
```

**2a. fast profile** (default):

```zsh
hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "Q2_0/*.gguf" --local-dir $M
mv $M/Q2_0/*.gguf $M/

# re-encode the dense layers to Q8_0 (~3 minutes); the n-gram shard is reused as is
python3 tools/requant_dense.py $M/Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00001-of-00002.gguf \
                               $M/Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-d8-00001-of-00002.gguf
ln -s Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00002-of-00002.gguf $M/Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-d8-00002-of-00002.gguf

./serve.sh                      # API at http://127.0.0.1:8080/v1, chat UI at http://127.0.0.1:8080
```

**2b. quality profile** (96 GB Macs):

```zsh
hf download meldlabs/Qwen3.8-Flash-Next-Meld-Turbo-Quality-GGUF \
  Qwen3.8-Flash-Next-Meld-Turbo-Quality-2.6bpw.gguf --local-dir $M

PROFILE=quality ./serve.sh
```

## Use it

`./serve.sh` starts one server at `http://127.0.0.1:8080`. It is all you need: no Ollama, no other runtime.

### Connect directly (nothing else to install)

The server speaks three API formats on the same port. Any API key and any model name will do.

| Client | Address to give it |
|---|---|
| OpenAI-compatible (most chat apps, coding agents, SDKs) | `http://127.0.0.1:8080/v1` |
| Messages API format (`/v1/messages`, streaming included) | `http://127.0.0.1:8080` |
| Ollama API (`/api/chat`, `/api/generate`, `/api/tags`, …) | `http://127.0.0.1:8080` as the Ollama address |

```zsh
curl http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"Write a haiku about unified memory."}]}'
```

**As a coding agent** — with [pi](https://github.com/earendil-works/pi), add a provider to `~/.pi/agent/models.json`:

```json
"local-mac": {
  "baseUrl": "http://127.0.0.1:8080/v1", "api": "openai-completions", "apiKey": "local",
  "compat": {"supportsDeveloperRole": false, "supportsReasoningEffort": false, "supportsStore": false, "thinkingFormat": "qwen"},
  "models": [{"id": "qwen3.8-flash-next", "name": "Qwen3.8-125B-MoE (local)", "reasoning": true, "contextWindow": 131072, "maxTokens": 8192}]
}
```

Then run `pi --provider local-mac --model qwen3.8-flash-next`. Add `--thinking off` for faster replies.

### Through the Ollama command line (optional)

Already have [Ollama](https://ollama.com) installed and like its terminal chat? Point its command line at Meld Turbo:

```zsh
OLLAMA_HOST=http://127.0.0.1:8080 ollama run qwen3.8-flash-next
```

Here `ollama` is only the chat client. The model runs in Meld Turbo; Ollama's own server and model library are not used, so `ollama pull` and model management commands do not apply. `ollama list` shows the model Meld Turbo is serving.

### Settings

`serve.sh` settings: `PROFILE` (`fast` or `quality`), `PORT`, `CTX` (context, default 131072), `NP` (parallel slots, default 1), `NPREDICT` (reply cap, default 16384), `LISTEN=0.0.0.0` to serve your LAN, `IDLE=<seconds>` to release the model's memory when idle (it reloads in ~4 s on the next request). Thinking is on by default. Turn it off per request with `"chat_template_kwargs": {"enable_thinking": false}`.

### Tuning for your Mac

The defaults were tuned on one machine, an M2 Max. Other chips (M1 to M5; Pro, Max, Ultra) have different GPUs and memory bandwidth, so other settings may be faster on yours. Worth trying, one at a time:

- `NMAX` — tokens drafted per speculative round (default 3).
- `UB` — prompt micro-batch (default 2048 on Macs with 96 GB or more, 512 otherwise). Larger is faster on long prompts and needs more memory.
- `LOOKUP=0` — prompt lookup off, to see how much it helps your workload.

Measure with `bench/api_bench.py` (e.g. `python3 bench/api_bench.py --src <a source tree> --ctx 1000,16000`), and alternate each setting with the default a few times: the GPU slows down after a few seconds of load, so a single short run is optimistic. If you find better settings for your Mac, please share chip, memory, settings and numbers in an issue; we will add recommendations per chip.

## How it gets there

- **Speculative decoding with the model's own MTP head.** Three draft tokens per round, verified in one pass of the full model.
- **A smaller draft vocabulary.** The draft head scores 106K common tokens instead of all 248K. A draft step drops from 3.5 to 2.4 ms with no change in acceptance, including for Chinese.
- **Dense layers re-encoded to Q8_0.** On Apple GPUs, low-bit K-quant kernels are integer-ALU bound when they verify several tokens at once. Q8_0 decodes cheaply, so verification gets 14% faster and generation 19% faster. Re-encoding changes the model by a KL divergence of only 0.0026.
- **Prompt lookup in front of the MTP head.** When the reply repeats part of the prompt (a code edit, a rewrite, a quote), long spans are drafted straight from the prompt and verified in one pass.
- **Sparse attention for long prompts.** The model's sparse-attention indexer picks the relevant blocks of the context; its pooled keys are cached between tokens instead of being recomputed, which makes generation at 32K context ~35% faster with identical output.
- **Faster prompt processing.** Larger prompt batches on 96 GB Macs, a split path for small batches, and an expert matrix kernel chosen by batch size.
- **EXL3 experts for the quality profile.** Experts stored in EXL3, a trellis-coded format that keeps more of the model per bit; Metal kernels decode it on the fly, with the input and output rotations fused into the expert matrix products.
- **Metal kernels** for 2-bit experts and for the small-batch matrix–vector products that verification is made of.

## Known limits

- **Sustained load.** The GPU holds its top clock for a few seconds, then settles about 20% lower. Long sessions run slower than short benchmarks.
- **Quality.** Both profiles are quantized (2-bit and 2.625-bit experts). Task scores are above; a direct comparison with the original BF16 model has not been run.
- **The quality profile needs 96 GB.** A version for 64 GB Macs is planned.
- **First turn of long sessions.** At ~315–350 tok/s of prompt processing, a 32K-token first prompt takes about 100 s. Later turns reuse the prompt cache.
- **One request at a time** by default.

Results and tuned settings from other Macs are very welcome — see [Tuning for your Mac](#tuning-for-your-mac) and [CONTRIBUTING.md](CONTRIBUTING.md).

## FAQ

**Can a 125B model really run on a MacBook?**
Yes. Qwen3.8-Flash-Next is a Mixture-of-Experts model: 125B parameters, but only 6B are active per token. With 2-bit experts it needs ~53 GB of memory on a 96 GB Mac (~45–50 GB on a 64 GB Mac) and generates ~40–47 tokens/s on an M2 Max.

**Does it need the internet or an API key?**
Only for the download. After that it runs offline; prompts and replies never leave your Mac.

**Which Macs does it run on?**
Apple silicon with a Max-class GPU or better and 64 GB of unified memory or more. Tested on an M2 Max with 96 GB; 64 GB works in a simulation (see [Quick start](#quick-start)). The quality profile needs 96 GB.

**Does it work with my tools?**
The server speaks an OpenAI-compatible chat API, the Messages API format and the Ollama API on one port, so chat apps, coding agents, SDKs and the `ollama` command connect directly. See [Use it](#use-it).

**How good are the answers?**
Greedy, thinking off, on fixed subsets: GSM8K 98.0%, HumanEval 93.3%, MMLU 82.5% (fast profile) and 96.5% / 97.6% / 87.5% (quality profile). See [Which profile?](#which-profile) and [docs/PERFORMANCE.md](docs/PERFORMANCE.md).

## What's in this repository

| Path | |
|---|---|
| `patches/` | 13 patches on llama.cpp (`danielhanchen/llama.cpp`, branch `qwen4exp/mtp`, pinned in `setup.sh`) |
| `setup.sh`, `serve.sh` | build and run |
| `tools/requant_dense.py` | re-encode dense K-quant / IQ4_XS tensors to Q8_0, copying experts byte for byte |
| `tools/gpu_pstate.c` | GPU frequency and performance-state logger (no root needed) |
| `bench/api_bench.py` | generation and prompt speed through the API |
| `data/draft_vocab.bin` | the 106,299-token draft vocabulary |
| `docs/PERFORMANCE.md` | measurements: what helped, what did not, known limits |

The quality profile's model file is on Hugging Face: [meldlabs/Qwen3.8-Flash-Next-Meld-Turbo-Quality-GGUF](https://huggingface.co/meldlabs/Qwen3.8-Flash-Next-Meld-Turbo-Quality-GGUF).

## About Meld Labs

[Meld Labs](https://meldlabs.ai) builds AI infrastructure — inference, training and research compute, agent sandboxes — so that developers can spend their time on ideas instead of plumbing. Meld Turbo is our first open-source project: a community release for running a frontier-scale model on your own machine.

## Credits and license

Built on [llama.cpp](https://github.com/ggml-org/llama.cpp) and Unsloth's MTP branch of it. The model is by the Qwen team, the GSQ-RCO quantizations are by ISTA-DASLab, the MTP head GGUF and the Q8_0 dense layers of the quality profile are by Unsloth, and the draft vocabulary comes from [Strata](https://github.com/Niko1221/Strata) (MIT). The quality profile's experts use EXL3, turboderp's format from [exllamav3](https://github.com/turboderp-org/exllamav3); they are taken from the 2.6 bpw pack of [Sushi](https://github.com/beamivalice/sushi) (MIT), whose decoder and kernel layout our EXL3 Metal kernels follow. Third-party notices are in [NOTICE](NOTICE).

MIT — © 2026 The Meld Labs Authors. Model weights are under their own licenses: Qwen3.8-Flash-Next and the files derived from it, including the quality profile's model file, are under the Qwen Community License 1.0.
