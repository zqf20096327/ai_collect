
<p align="center">
  <img width="75" height="75" alt="image" src="https://github.com/user-attachments/assets/4c061c9a-a3bb-4838-b6d1-fac595e94bdf" />
</p>
<h1 align="center">WhiteLotus</h1>
<p align="center">
  <em>a readable, from-scratch LLM inference engine</em>
</p>
<p align="center">
<img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey" />
<img src="https://img.shields.io/badge/C%2B%2B-17-00599C?logo=cplusplus&logoColor=white" />

<img src="https://img.shields.io/badge/Eigen-3-blue" />
<img src="https://img.shields.io/badge/pybind11-2.x-blue" />

<img src="https://img.shields.io/badge/weights-safetensors-ff6f00" />
<img src="https://img.shields.io/badge/arch-GPT--2-black" />
</p>



## LLM Usage Disclosure
This project is entirely hand written; LLMs have not been used in **any** part of the process.

## Design philosophy

WhiteLotus targets CPU execution and prioritizes clarity over speed. Every component (tokenizer, engine, scheduler, transformer attention, KV cache, and sampler) is implemented by hand, so that you can read the codebase top to bottom and understand exactly how LLM inference works.

The C++ core and Python API layer are cleanly separated, with pybind11 bridging the two. The codebase includes tests, benchmarks, and a Python API that mirrors what a production engine would expose.

> **Note:** Named after the Order of the White Lotus from Avatar: The Last Airbender... working quietly behind the scenes to make the Avatar's journey possible, much like an inference engine behind a model \ (•◡•) /

## Architecture
<img width="6697" height="3091" alt="image" src="https://github.com/user-attachments/assets/578949ed-c516-4f93-8556-e6471e612689" />

## Features

- BPE tokenizer
- GPT2 Transformer with multi-head attention, GELU FFN, layer norm
- KV cache
- Sampling strategies: temperature, top-K, top-P, repetition penalty
- Async request engine
— scheduler queue with worker thread, supports multiple concurrent requests
- Python bindings with pybind11 wrapper
- Zero-copy weight loading with memory-mapped safetensors

## Installation
```
git clone --recursive https://github.com/Anirudh171202/WhiteLotus
cd WhiteLotus
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

You will also need to download a model to run inference on.

```
pip install -e ".[scripts]"
# This downloads the TinyStories-33M model.
python scripts/download_model.py
# This converts binary weights to safetensors.
python scripts/convert_pytorch.py
```
## Usage 
```
>>> from WhiteLotus import Engine
>>> import asyncio
>>> engine = Engine()
[2026-03-18 20:08:02.182] [wl] [info] Loaded config: vocab=50257, hidden=768, heads=16, layers=4, maxSeq=2048
[2026-03-18 20:08:02.200] [wl] [info] Weights loaded successfully
>>> asyncio.run( engine.generate( "Yip yip, Appa " ) )
>>> [2026-03-18 20:09:56.356] [wl] [info] Request 1155300761 finished eos=true, maxToken=false, generated 7 tokens
'Yip yip, Appa cake! Mummy!'
```

Yeah I don't know what that means either.

## How It Works

- [You're Billed by the Token. Here's What That Means.](http://anirudhsathiya.com/blog/tokenizer) — BPE Tokenizers under the hood, and where tokenization breaks math, spelling and code
- [Why Your First Token Is Always Late](http://anirudhsathiya.com/blog/transformer) — The inference side of transformers, along with systems tricks that make production LLMs fast
- [The Last Mile of LLM Inference](http://anirudhsathiya.com/blog/sampler) — Sampling strategies and why inference optimizations pose a security tradeoff

## License
MIT.

