[![ci](https://github.com/robotgamedevelopers/inky/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/robotgamedevelopers/inky/actions/workflows/ci.yml)

<img width="2172" height="724" alt="image" src="https://github.com/user-attachments/assets/1ae045b5-9adc-4590-8746-bd55b8bedad8" />

Fast local inference for [**Inkling 2 Mini**](https://thinkingmachines.ai/news/inkling-2-mini/) on Apple silicon.

With **inky**, you can:

* Run Thinking Machines' Inkling 2 Mini on an M5 Mac, from the LM Studio GGUF
* Decode at **95–106 tok/s** on a single lane (**2.3x–2.6x** faster than llama.cpp's 41 tok/s on Apple M5 Max) and prefill prompts at **4,186–4,531 tok/s**
* Scale across **64 parallel lanes** to **323–434 tok/s** at 20K context (**1.5x–2.0x** faster than llama.cpp's 215 tok/s short-context ceiling), **530–578 tok/s** at 2K context, and **322 tok/s** at 42K context
* Match llama.cpp argmaxes (worst KL <= 0.01) across CI's checked reference positions: 58/58 on short-prompt decode, 24/24 after a 2380-token long-prompt prefill, and 58/58 on short-prompt decode steps
* Serve many coding-agent tasks at once over HTTP from one process, sharing cached prompt prefixes in memory (**6.8x** lower KV at 16×8K) and on SSD. See [performance](docs/PERFORMANCE.md), [design](docs/DESIGN.md), and [roadmap](docs/ROADMAP.md).

[![Throughput vs. parallel lanes at 20K context on Apple M5 Max (128 GB)](docs/assets/readme-lanes-speed.svg)](docs/PERFORMANCE.md)

This is a fork of [erisinky](https://github.com/Eriskii/erisinky) by Eris.

Built by Glenn Fiedler ([yojimbo](https://github.com/mas-bandwidth/yojimbo), [netcode](https://github.com/mas-bandwidth/netcode)), Rowan Claude and Eris.

For more information, please ask your AI to [read the docs](docs/README.md), or see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for building and running the validation suite with or without an M5 Mac.
