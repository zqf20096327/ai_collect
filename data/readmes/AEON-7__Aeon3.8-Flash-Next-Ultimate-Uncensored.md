# Aeon3.8-Flash-Next ULTIMATE UNCENSORED: quick-start guides for the NVIDIA DGX Spark

[![Tip AEON Forge on LotusMake](https://lotusmake.com/badges/coffee-light.v2.svg)](https://lotusmake.com/support?mode=gpu&from=%2Fc%2Faeon-forge#once) [![Subscribe to AEON Forge on LotusMake](https://lotusmake.com/badges/subscribe-light.v2.svg)](https://lotusmake.com/support?mode=tiers&billing=month&from=%2Fc%2Faeon-forge)

![Six measured results: 180B parameters, 98 GiB on disk, 60 tok/s on one Spark, 748 tok/s on four, 0 of 56 refusals, 28 of 28 hidden facts recalled](assets/hero.png)

**A 180-billion-parameter model with the refusals removed, running on one desktop DGX Spark at 60 tokens a second.**

This repo holds the copy-paste serve guides for [Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS): an uncensored (abliterated) build of Qwen3.8-Flash-Next, 180B parameters, quantized to 4-bit NVFP4 so that it fits in 98 GiB. It runs on Strata or on AEON vLLM Ultimate (our vLLM build for the Spark), serves an OpenAI-compatible API, reads images, and holds 131K to 256K of context. There are five validated setups, for one, two and four DGX Sparks.

**Start here**

1. [Before you start](quickstart/before-you-start.md): three short steps, the same for every setup.
2. Pick your seat in the table below and open its guide. Every guide ends in commands you can paste as they are.
3. [Use it](quickstart/use-it.md): the address to point your app at, and a Python example.

If an AI agent is doing the setup for you, give it [`AGENTS.md`](AGENTS.md) and nothing else.

## Pick your seat

![The five validated setups compared: tokens per second for one user and for many users at once](assets/recipes.png)

| Seat | Hardware | Engine | Context | One user | Many users | Guide |
|---|---|---|---|---|---|---|
| **1** | 1 DGX Spark | Strata + DFlash2 | 131K, images | **60.6 tok/s** | 73 across 4 | [Open the guide](quickstart/seat-1-strata-one-spark.md) |
| **2** | 1 DGX Spark | AEON vLLM Ultimate + DFlash2, n-gram table on disk | 131K, images | 38.9 tok/s | **97.5** across 4 | [Open the guide](quickstart/seat-2-aeon-vllm-ultimate-one-spark.md) |
| **3** | 2 DGX Sparks, linked | AEON vLLM Ultimate + DFlash2, tensor-parallel | 131K, images | 58 to 65 tok/s | **359** across 16 | [Open the guide](quickstart/seat-3-two-sparks-team-server.md) |
| **4** | 2 DGX Sparks, linked | AEON vLLM Ultimate, tensor-parallel | **256K**, images | 51 tok/s | 145 across 4 | [Open the guide](quickstart/seat-4-two-sparks-long-thinking.md) |
| **5** | 4 DGX Sparks | AEON vLLM Ultimate, two replicas and a balancer | 131K, images | 58 to 65 tok/s | **748** across 32 | [Open the guide](quickstart/seat-5-four-sparks.md) |

Speeds are greedy decoding with thinking off, except Seat 4, which was measured at the [recommended sampling](quickstart/sampling.md). Each guide lists its own numbers at those settings and with thinking on. Everything was measured on our own Sparks in November 2026.

**Three rules of thumb.**

- **For one stream, Strata. For many, AEON vLLM Ultimate.** On one Spark, Strata is 56% faster for a single user (60.6 against 38.9 tok/s). But it tapers as sessions are added: its total rises from 61 to 73 tok/s at four streams and stays there, and it never decodes more than 8 streams in parallel. AEON vLLM Ultimate goes the other way, from 39 to 98 tok/s at four streams on the same box, then to 359 on two Sparks and 748 on four.
- **A second Spark buys concurrency, not single-user speed.** One user gets about 60 tok/s on one Spark and 58 to 65 on two. Sixteen simultaneous requests share 71 tok/s on one Spark with Strata, and 359 on two Sparks.
- **Pick the drafter by workload.** DFlash2 is faster on average and pulls furthest ahead on predictable output: math, code, repeated text. The built-in MTP head is ahead on multilingual text and, on two Sparks, holds its speed better behind very long prompts.

![Total tokens per second as concurrent sessions rise on one DGX Spark, Strata against AEON vLLM Ultimate](assets/ladder.png)

## The settings that matter

Use these on every seat. They are explained one by one in [Sampling settings](quickstart/sampling.md).

```
temperature 0.6
top_p 0.95
top_k 20
presence_penalty 0.5
repetition_penalty 1.0
```

Seats 2 to 5 apply them by default. On Seat 1 your app sends them with each request.

## Where everything is

| What | Where |
|---|---|
| The weights, every measurement, charts, limits | [Hugging Face: NVFP4-XS](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS) |
| The 360 GB master, and how the uncensoring was done and tested | [Hugging Face: BF16](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-Ultimate-Uncensored-BF16) |
| The story of the build | [180 Billion Parameters, No Refusals, One Desk](https://lotusmake.com/posts/180-billion-parameters-no-refusals-one-desk) |
| The engine behind Seats 2 to 5 | [AEON vLLM Ultimate](https://github.com/AEON-7/vllm-ultimate-dgx-spark) |
| The engine behind Seat 1 | [Strata](https://github.com/Niko1221/Strata) |
| Instructions written for AI agents | [`AGENTS.md`](AGENTS.md), also in the Hugging Face repo |

## For AI agents

[`AGENTS.md`](AGENTS.md) is written for an agent that has been asked to bring the model up, including a small one. It tells the agent how to identify the hardware, which seat that hardware maps to, the exact commands for each seat, how to wait for the server and test it, what numbers to expect, what it may and may not change, and what to report. The commands are the same ones as in the guides.

The same file is in the Hugging Face repo, at [`AGENTS.md`](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS/blob/main/AGENTS.md), so an agent that only has the weights still has the instructions.

## Status

- **All five seats run on public software as written.** Seat 2 uses `ghcr.io/aeon-7/aeon-vllm-ultimate:2026-11-25-v0.33.0-omni-dflash2-ngram-disk`. Seats 3 to 5 use `2026-11-23-v0.33.0-omni-dflash2`. Seat 1 uses Strata 0.2.18.
- **Validated hardware is the DGX Spark only.** There is no recipe for other GPUs yet.
- **Not measured:** a single job at tensor-parallel size 4, and a four-Spark setup with two identical DFlash2 replicas (Seat 5 was measured with one DFlash2 replica and one MTP replica).

## Responsibility and license

This is an **uncensored** model. Its refusal behaviour has been removed, and it makes no judgement about whether to comply. You are the safety layer. The full [User Responsibility & Arbitration Clause](https://huggingface.co/AEON-7/Aeon3.8-Flash-Next-ULTIMATE-UNCENSORED-NVFP4-XS#user-responsibility--arbitration-clause) on the model card applies to every use of it.

The weights are under the Qwen Community License 1.0. The recipes and instructions in this repo are documentation for them.

## Support the work

AEON-7 models, engines and tools are built independently, on my own hardware. If they are useful to you:

[![Tip AEON Forge on LotusMake](https://lotusmake.com/badges/coffee-light.v2.svg)](https://lotusmake.com/support?mode=gpu&from=%2Fc%2Faeon-forge#once) [![Subscribe to AEON Forge on LotusMake](https://lotusmake.com/badges/subscribe-light.v2.svg)](https://lotusmake.com/support?mode=tiers&billing=month&from=%2Fc%2Faeon-forge)

**[AEON FORGE on LotusMake](https://lotusmake.com/c/aeon-forge)**
