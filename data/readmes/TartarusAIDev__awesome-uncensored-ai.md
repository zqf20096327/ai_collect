<p align="center">
  <a href="https://tartarusai.dev/?utm_source=github&utm_medium=readme&utm_campaign=awesome-uncensored-ai&utm_content=banner">
    <img src="assets/banner.svg" alt="awesome-uncensored-ai — Curated uncensored and locally-runnable AI tooling" width="100%">
  </a>
</p>

# Awesome Uncensored AI [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> A curated list of uncensored and locally-runnable AI: coding agents, SDKs,
> model runners, uncensoring techniques, benchmarks, and guides.

Mainstream assistants refuse a large and growing share of legitimate technical
requests: security research, red-teaming, low-level systems code, scraping,
content other people find distasteful. This list collects the tools that don't.

Everything here is open source or self-hostable unless marked **hosted**.

## Contents

- [Coding agents](#coding-agents)
- [SDKs and tooling](#sdks-and-tooling)
- [Model runners](#model-runners)
- [Uncensoring techniques](#uncensoring-techniques)
- [Benchmarks](#benchmarks)
- [Guides](#guides)
- [Finding models](#finding-models)
- [Self-hosting and hardware](#self-hosting-and-hardware)
- [Reading](#reading)
- [Contributing](#contributing)

## Coding agents

Terminal- and editor-based agents that read, write and run code.

- **[Tartarus](https://tartarusai.dev/?utm_source=github&utm_medium=readme&utm_campaign=awesome-uncensored-ai&utm_content=body)** **(hosted)** — Uncensored coding agent.
  CLI (`pip install tartarus-console`) plus an OpenAI-compatible API. Ships code
  instead of refusals; crypto-only billing, no KYC.
- [Aider](https://github.com/Aider-AI/aider) — Pair-programming in your terminal;
  bring your own model.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — Autonomous software
  agent; runs any OpenAI-compatible backend.
- [Cline](https://github.com/cline/cline) — Agentic coding inside VS Code; works
  with local and self-hosted endpoints.
- [Continue](https://github.com/continuedev/continue) — Open-source IDE
  autocomplete and chat; point it at any model.

## SDKs and tooling

- [tartarus-sdk](https://github.com/TartarusAIDev/tartarus-sdk) — Typed
  TypeScript client (chat, streaming, tool-calling).
- [tartarus-mcp](https://github.com/TartarusAIDev/tartarus-mcp) — Model Context
  Protocol server; use an uncensored model as a tool in Claude Desktop, Cursor,
  Cline.
- [tartarus-cookbook](https://github.com/TartarusAIDev/tartarus-cookbook) —
  Runnable Python/Node/curl examples for an OpenAI-compatible uncensored API.

Any OpenAI SDK works against an OpenAI-compatible endpoint; just change the base
URL.

## Model runners

Run models locally, or serve them behind an OpenAI-compatible endpoint.

- [llama.cpp](https://github.com/ggml-org/llama.cpp) — The reference CPU/GPU
  inference engine; `llama-server` exposes an OpenAI-compatible API.
- [Ollama](https://github.com/ollama/ollama) — One-command local models.
- [vLLM](https://github.com/vllm-project/vllm) — High-throughput GPU serving.
- [LM Studio](https://lmstudio.ai) — Desktop app with a local server.
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) —
  Batteries-included local UI and API.
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) — Single-binary llama.cpp
  wrapper with a built-in API.

## Uncensoring techniques

How refusal behaviour is removed or bypassed, for research.

- **Abliteration** — Refusal is largely mediated by a single direction in
  activation space; projecting it out suppresses refusals without retraining
  (Arditi et al., 2024). Most community "abliterated" models apply this.
- **Fine-tuning / DPO** — Preference tuning on compliant responses to override
  safety alignment.
- **System-prompt and decoding steering** — Weaker, prompt-level methods that
  don't touch weights.

See [how-abliteration-works](https://github.com/TartarusAIDev/uncensored-ai-guide/blob/main/docs/how-abliteration-works.md)
for the mechanism.

## Benchmarks

- [refusal-bench](https://github.com/TartarusAIDev/refusal-bench) — Measure how
  often a model refuses *legitimate* coding tasks (false-refusal rate) against
  any OpenAI-compatible endpoint.
- **XSTest** — The reference over-refusal test set from the research literature;
  the inspiration for false-refusal evaluation.

## Guides

- [The Uncensored AI Guide](https://github.com/TartarusAIDev/uncensored-ai-guide)
  — What "uncensored" means, how abliteration works, local vs hosted, and the
  chat-template gotcha that breaks tool-calling.

## Finding models

- [Hugging Face: "abliterated"](https://huggingface.co/models?search=abliterated)
  — community-uncensored variants of open models.
- [Hugging Face: "uncensored"](https://huggingface.co/models?search=uncensored)
  — fine-tuned uncensored models.
- Prefer GGUF quantizations (Q4_K_M and up) for llama.cpp / Ollama.

## Self-hosting and hardware

- A 30B mixture-of-experts model at Q4 fits in ~18-20 GB of VRAM; two 24 GB
  consumer GPUs run it comfortably with long context.
- Memory bandwidth, not FLOPs, is the usual bottleneck for single-user
  inference; size your GPU by VRAM and bandwidth first.
- Rent by the hour (vast.ai, RunPod, Lambda) before buying.

## Reading

- "Refusal in Language Models Is Mediated by a Single Direction" — Arditi et al.,
  2024. The paper behind abliteration.
- llama.cpp [server docs](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
  — OpenAI-compatible endpoint reference.

## Contributing

PRs welcome. One entry per line, alphabetical within a section, a one-line
description, and a working link. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and
related rights to this work.
