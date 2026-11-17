<p align="center">
  <a href="https://tokspur.com/#gh-light-mode-only"><img src="https://tokspur.com/assets/brand/tokspur-wordmark-960.png" width="320" alt="tokspur"></a>
  <a href="https://tokspur.com/#gh-dark-mode-only"><img src="https://tokspur.com/assets/brand/tokspur-wordmark-reversed-960.png" width="320" alt="tokspur"></a>
</p>

<p align="center"><strong>Private chat and code on your Mac.</strong></p>

<p align="center">
  <a href="https://tokspur.com/">Website</a> |
  <a href="https://tokspur.com/get-started/">Get started</a> |
  <a href="https://tokspur.com/docs/">Docs</a> |
  <a href="https://tokspur.com/engine/">Engine</a> |
  <a href="https://github.com/san-digital/tokspur">GitHub</a>
</p>

Tokspur runs Qwen3.8 Flash-Next locally on a Mac. It uses a native Metal worker and serves an OpenAI-compatible chat API.

Tokspur needs an Apple M5 Max with a 40-core GPU, 128 GB of unified memory and macOS 27 or later. Run the installer in Terminal, then follow the [setup guide](https://tokspur.com/get-started/) to verify the installation and connect a client.

```sh
curl -fsSL https://tokspur.com/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
```

## Add the model

The `pull` and directory-based `serve` commands below require Tokspur 0.3.1 or later.

`tokspur pull` downloads the pinned base GGUF, pre-built Planar Pack v3 and shared Q8 MTP sidecar from [`san-digital/Qwen3.8-Flash-Next-Q4_K-Tokspur-GGUF`](https://huggingface.co/san-digital/Qwen3.8-Flash-Next-Q4_K-Tokspur-GGUF), verifies every file by SHA-256 and configures local state with no extra `adopt`, `configure` or `pack build` step (see the [model guide](https://tokspur.com/docs/models/)).

```sh
tokspur pull
tokspur serve --speed-preset
```

If you already downloaded the repository folder separately with `hf download`, point `serve` directly at that directory:

```sh
tokspur serve /path/to/Qwen3.8-Flash-Next-Q4_K-Tokspur-GGUF --speed-preset
```

Connect to `http://127.0.0.1:18081/v1` with model `tokspur` and the generated API key.

For faster block-8 speculative decoding across code, `<think>` reasoning and multilingual workloads, pull the optional drafter [`san-digital/Qwen3.8-Flash-Next-DFlash2`](https://huggingface.co/san-digital/Qwen3.8-Flash-Next-DFlash2):

```sh
tokspur pull --dflash2
tokspur serve --speed-preset --drafter dflash2 --shared-prefix-cache
```

Add `--dflash2-vocab-gather cjk64k --dflash2-lookup hybrid --ple-ram-resident` when serving multilingual or CJK prompts alongside `<think>` reasoning.

### Pack formats

[`san-digital/Qwen3.8-Flash-Next-Q4_K-Tokspur-GGUF`](https://huggingface.co/san-digital/Qwen3.8-Flash-Next-Q4_K-Tokspur-GGUF) includes Planar Pack v3 (`Qwen3.8-Flash-Next-Q4_K.tokspur.gguf`), which Tokspur uses directly from the model directory with no local pack build. The pinned asset profile requires this pre-built pack and its matching base GGUF and MTP sidecar. `--pack-v3` on `serve` refuses fallback to an older layout.

## Context and output

The default context window is **64K (65,536 tokens)**. Restart the server with `--context-length 131072` to select **128K (131,072 tokens)**. The option works with MTP and DFlash2, and the larger window needs additional memory headroom. Speed mode keeps the default window unless you select a larger one.

```sh
tokspur serve --speed-preset --context-length 131072
```

The rendered prompt, including chat history and tool declarations, shares the window with generated output. Set your client's context size to match the server. The API defaults to **8,192 output tokens**, including thinking. Set either `max_tokens` or `max_completion_tokens` from **1 to 32,768**. The server lowers the output limit to the space remaining after the prompt and refuses prompts that leave no generation space. A 128K window keeps the same output limit.

Thinking is enabled by default. Set `enable_thinking: false` to disable it, or use `reasoning_effort` (`low`, `medium`, `high` or `xhigh`) to guide the model. Use `thinking_budget` from 0 to 32,768 for a token budget within the total output limit, with 0 disabling thinking. A positive budget is ignored when thinking is explicitly disabled. See the [API guide](https://tokspur.com/docs/api/) for request settings.

## Build

Install Xcode with the Metal toolchain, Git, Python 3.12 and Rust 1.99.1. Run these commands from the checkout root.

```sh
python3.12 scripts/bootstrap.py
.venv/bin/tokspur doctor
```

## Licences

[Apache 2.0](LICENSE). See [NOTICE](NOTICE) for third-party credits and [model licences](MODEL_LICENCES.md) for the weights. Report vulnerabilities through the [Security page](https://github.com/san-digital/tokspur/security).
