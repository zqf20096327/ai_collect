# Mackani

An unofficial Apple Silicon port of [YASAKANI](https://github.com/yasakani-dev/yasakani), written from scratch in Rust. Version 0.1.0.

[日本語](README.ja.md)

[Download Mackani for macOS](https://github.com/TKY-27/Mackani/releases/latest)

YASAKANI is an Apache-2.0 local LLM engine for Windows and one NVIDIA RTX 5090. It runs Qwen3.8-27B from compressed `.yskn` files. Mackani reads the same published model folder on a Mac. It uses Metal for compressed projections, and NEON and a thread pool for the remaining work. Its Rust engine was written against the behaviour specification in [docs/spec/](docs/spec/), derived from upstream commit `758ef28`, without copying upstream engine code.

The model files and the `.yskn` format are the YASAKANI authors' work. Thank you to the YASAKANI authors for publishing them and their engine. Mackani is not affiliated with or endorsed by the YASAKANI authors, the Qwen team or any other organisation.

**Tested on exactly one machine: a MacBook with a base Apple M5 (4 performance + 6 efficiency CPU cores, 10-core GPU), 24 GB memory and macOS 27. Only the speed model was tested.** Other Apple Silicon Macs should work through runtime feature detection and fallbacks, but have not been tested. Tuning tables were calibrated on the M5 only. No comparison with other engines has been made.

## Requirements

- A Mac with Apple Silicon and macOS 26 or later.
- The published model folder, downloaded separately.

For a source build, see the Rust and Xcode requirements in [BUILDING.md](BUILDING.md).

The default configuration reserves a 32,768-token context and enables the draft model. Its estimated memory need is 19.03 GiB. Startup refuses a configuration that does not fit physical memory and lists alternatives that would fit. `info` prints the estimate without loading the model.

By the same estimate, a 16 GB Mac can use `--draft none --ctx 16384`. This has not been tested on a 16 GB Mac. The estimate is not a measurement of peak memory.

## Get the model

Download the tested [speed model](https://huggingface.co/yasakani-dev/Qwen3.8-27B-YASAKANI-speed), which upstream calls its “fastest model”. With the Hugging Face CLI (`hf`) installed:

```sh
hf download yasakani-dev/Qwen3.8-27B-YASAKANI-speed --local-dir ~/models/qwen38-speed
```

The folder is about 12 GB: `qwen38_27b_speed.yskn` is 10.31 GB, plus the draft model and supporting files. Keep the whole folder. Do not modify its files while Mackani is running.

The [quality model](https://huggingface.co/yasakani-dev/Qwen3.8-27B-YASAKANI-quality) has not been tested with Mackani. Model files are distributed by the YASAKANI authors, separately from Mackani.

## Build and check

From the repository root:

```sh
cargo build --release -p mackani
./target/release/mackani info --model-dir ~/models/qwen38-speed
./target/release/mackani selfcheck --model-dir ~/models/qwen38-speed
```

The binary is `target/release/mackani`. `info` reports the model, machine and memory estimate without loading weights. `selfcheck` checks the exact token sequences recorded by upstream in the model folder's `selfcheck.json`; it takes about 30 seconds.

Every command except `info` loads the model, which takes about 18 seconds and most of the memory of a 24 GB Mac. Run one at a time.

## Terminal chat

```sh
./target/release/mackani chat --model-dir ~/models/qwen38-speed
```

Thinking is on by default. Add `--no-think` to turn it off. `--max-tokens` sets the answer limit and `--temperature` sets sampling temperature. Type `/exit` to quit.

## Local HTTP API

```sh
./target/release/mackani serve --model-dir ~/models/qwen38-speed
```

The default address is `http://127.0.0.1:8765`; `--port` changes the port. The server binds to loopback by default. A non-loopback bind is refused without an API key. `--api-key` enables bearer-key authentication. `/health` answers 503 while the model loads and 200 when the server is ready. Stop the server with Ctrl+C.

For a streaming chat completion, in another terminal:

```sh
curl -N http://127.0.0.1:8765/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"qwen3.8-27b","messages":[{"role":"user","content":"Explain how a hash table works."}],"stream":true,"stream_options":{"include_usage":true}}'
```

The OpenAI-compatible API supports streaming, usage counts and tool calls. Thinking is on by default and arrives first, as `reasoning_content`; add `"enable_thinking":false` to the request for a direct answer, and `"max_tokens"` to bound it. The server also provides `/v1/models` and `/health`. See the [HTTP reference and limits](crates/mackani-cli/README.md) and [security policy](SECURITY.md).

## macOS app

Download the app ZIP from [GitHub Releases](https://github.com/TKY-27/Mackani/releases/latest), unzip it and move `Mackani.app` to Applications. The native SwiftUI app starts and stops its bundled server. On first launch, click **Choose Model Folder** and select the downloaded folder. You can change it later in Settings.

The app is ad-hoc signed and unnotarized. See the [installation instructions](app/README.md#install) if macOS blocks the first launch. To build the app from source, see [BUILDING.md](BUILDING.md#native-app).

![Mackani in the light appearance](app/docs/screenshot-light.png)

[Dark appearance](app/docs/screenshot-dark.png)

## Benchmark

```sh
./target/release/mackani bench --model-dir ~/models/qwen38-speed
./target/release/mackani bench --model-dir ~/models/qwen38-speed --draft none
```

The tasks cover prose, code, structured output and thinking. The first command uses the default draft model; the second disables it. `--n` sets the tokens per task. `--json FILE` saves metrics. Draft speculation changes speed, never the output.

Every fast path matches the scalar reference bit for bit in the test suite. On upstream's fixed text set, the default-cache perplexity reference is 2.075937; Mackani reproduces it within 0.001. Selfcheck token sequences match upstream's recording exactly. These are checks against the compressed model, not a claim that its output equals the original uncompressed Qwen model.

## Measured on the test machine

The test machine is the base M5 MacBook described above, with nothing else running. The speeds come from one run of `mackani bench` with its defaults (512 tokens per task, greedy decoding). Prefill was measured on that benchmark's short prompts (28 to 64 tokens). Upstream's recorded perplexity is 2.075937. Nothing has been compared with other engines.

| Task | Tokens/s with draft (default) | Tokens/s without draft |
|---|---|---|
| Prose | 9.5 | 5.6 |
| Code | 11.2 | 5.8 |
| Structured output | 10.6 | 5.8 |
| Thinking | 10.1 | 5.7 |

| Metric | Default configuration |
|---|---|
| Time to load (seconds) | 18 |
| Prefill tokens/s | 15 to 21 |
| Perplexity on upstream's fixed text set | 2.075687 |

## Known limits

- One machine and one model tested. Other chips and the quality model are untested.
- One request runs at a time; other requests wait within the server's queue limits.
- Text only; images are not supported.
- Forced `tool_choice`, `logprobs` and `n > 1` are rejected.
- Long contexts are slow to prefill.

## Read more

- [Building and checks](BUILDING.md), [contributing](CONTRIBUTING.md) and [security](SECURITY.md).
- [Architecture and verification examples](docs/ARCHITECTURE.md) and [design notes](docs/DESIGN_NOTES.md).
- [Upstream behaviour specification](docs/spec/) and [HTTP reference](crates/mackani-cli/README.md).
- Workspace crates: `mackani-format` reads `.yskn`; `mackani-ref` defines the scalar reference bits; `mackani-engine` implements the fast engine; `mackani-text` handles tokenization, chat templates and stream decoding; `mackani-cli` builds the `mackani` binary.

## Licence

Copyright 2026 [TKY-27](https://github.com/TKY-27). Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the software and model attributions.
