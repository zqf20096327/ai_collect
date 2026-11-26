# Inference optimization playbook

A map of 127 tested ideas for making huge LLMs fast on consumer GPUs. Each one has a verdict (worked, failed, or works only under conditions), the numbers, the reason, and the conditions it was tested under.

It comes from running DeepSeek V4.1 Flash, Qwen3.8-Flash-Next, GLM-5.3-Flash, MiniMax-M3.1-Flash, Tencent Hy4 Flash and Ling-3.2-air on 4x RTX 3090 with experts offloaded to RAM, and Inkling 2 Mini on a single RTX 3090 with every expert in VRAM. The big models do not fit in 96 GB of VRAM at the quants we wanted. Engines: Strata, Maya forks, an exllamav3 fork, llama.cpp, vLLM, most of them patched by hand.

| Model, setup | What changed | Before → after |
|---|---|---|
| DeepSeek V4.1 Flash, 4 cards | DMA from pinned RAM for every tensor format, layer skip on the prompt, auto chunk | prefill 32K: 430 → 2,199 tok/s |
| DeepSeek V4.1 Flash, CPU path on Zen 2 | 1 build flag (PDEP runs in microcode there) | 1 cold expert: 1.6 → 0.44 ms |
| Hy4 Flash, 1 card | 1 load of experts per block of up to 57,600 tokens, attention in tiles of 2,048 (full build) | prefill of 57,587 tokens: 415.6 → 1,510.2 tok/s |
| Hy4 Flash, 2 cards | cold experts computed on the CPU in parallel with hot ones on the GPU | decode of short code: 24.6 → 70.4 tok/s |
| Qwen3.8-Flash-Next, 1-2 cards | DFlash2 drafter | decode +44-46% |
| Qwen3.8-Flash-Next, Russian | a Cyrillic draft vocabulary, no training | draft acceptance 32% → 54% |
| MiniMax-M3.1-Flash | attention K/V gathered into VRAM once per chunk | prefill 64K ×3.3 |
| GLM-5.3-Flash at 2.05 bpw, 4 cards | tensor parallel instead of layer split | 48.3 → 66-68 tok/s |
| Inkling 2 Mini, 1 card | every expert in VRAM, a token as 1 CUDA graph, NVFP4 experts and attention on the tensor cores | decode 57 (llama.cpp) → 128.7 tok/s, 344K context |
| Ling-3.2-air, 2 cards | tiled Flash-MLA, macro-prefill, TILE=32 MLA decode, `blk.42` MTP with exact KDA rollback | prefill 32K: 248 → 3,119 tok/s; 260K decode +64.4%; MTP up to 143.8 tok/s |

And what did not work, which is most of the value:

- "Keep the hot experts in VRAM" works on 2 of the first 4 models. On MiniMax a profile gives 64-69% hits and random placement gives 61% (sim).
- Training a drafter on our own data gave little or nothing on 3 models.
- A short benchmark promised +27% decode. Real generation gave +2%.
- A drafter change matched on 4,400 tokens of the first turn and broke the second turn.

Inkling 2 Mini shows the other regime: once everything fits one card, the cost is kernel launches and memory latency, not placement ([case](cases/inkling-2-mini.md)).

## Why a map

The 6 offloaded models behaved differently. The cheapest way to serve a miss flipped between models on the same hardware, tensor parallel lost on one and won on another, a long drafter window paid on skewed routing and not on flat routing. A fixed list of steps would be wrong for half of them.

So the playbook is built for orientation. You describe your case, find its place, and see only the results that were obtained under the same conditions.

It is written for 2 readers:

- **People** who tune local inference and want to know what is worth trying before they spend a week on it.
- **Coding agents** that do the tuning for them. The repo root is a ready skill.

The numbers are from one rig. Yours will be different. The mechanisms are the same on any box with GPUs, a CPU and RAM, and chapters 01-15 each end with a checklist for moving the idea to another model.

## Start

| You want to | Open |
|---|---|
| Describe your case and get its tags | [protocol/situation-card.md](protocol/situation-card.md) |
| Find your place by regime or by symptom | [playbook/00-start-here.md](playbook/00-start-here.md) |
| Check if an idea was already tried under your conditions | [ledger/hypotheses.md](ledger/hypotheses.md) |
| See how it went on a model like yours | [cases/](cases/README.md) |
| Run an experiment so the result means something | [protocol/experiment-rules.md](protocol/experiment-rules.md) |
| Bring up a new model from zero | [protocol/new-model-checklist.md](protocol/new-model-checklist.md) |
| Look up a term | [glossary.md](glossary.md) |

## What is inside

```
playbook/    16 chapters by mechanism
  00  the map: entry by regime and by symptom, 15 findings
  01  cost model: time = constant + misses × cost of a miss, ceilings
  02  where to serve a miss: CPU lane vs PCIe copy
  03  hot experts: profile, domain, placement
  04  live expert cache
  05  several GPUs: layer split, TP, EP, all-reduce
  06  CPU and RAM: channels, NUMA, threads
  07  prefill and re-reading the prompt
  08  speculative decoding
  09  quants: bits vs experts in VRAM
  10  pruning and merging experts
  11  sessions, KV and the prompt cache in agent work
  12  loading, page cache, THP, big tables on NVMe, lent-VRAM vision
  13  the output head
  14  how to benchmark, and the traps
  15  quality and release gates
ledger/      every hypothesis: verdict, numbers, why, "revisit when", condition tags
cases/       the rig, a traits table and 7 model case files
protocol/    situation card, experiment rules, new-model checklist, entry template
tools/       route_sim.py (skew and cache simulator), fit_cost.py (time model fit)
SKILL.md     entry point for agents
AGENTS.md    rules for editing this repo
```

## Use it with an agent

The repo root is a skill directory: `SKILL.md`, plain markdown and 2 standard-library Python scripts.

Clone it where your agent looks for skills, for example:

```bash
git clone https://github.com/alesha-pro/inference-optimization-playbook ~/.claude/skills/inference-optimization-playbook
```

or into `.agents/skills/` or `.claude/skills/` of a project. Then ask the agent things like:

- "Decode on my 2-GPU box is 20 tok/s with most experts in RAM. What do I check first?"
- "I want to add a drafter to this engine. Was a separate wide drafter worth it?"
- "Plan the bring-up of this new MoE on 1x 24 GB + 128 GB RAM."

Without skills support, point the agent at the repo and tell it to read `SKILL.md` first.

The agent fills a situation card, gets a tag line such as `#offload #weak-skew #cpu-lane #multi-gpu #agent`, and filters the ledger with it:

```bash
grep "#weak-skew" ledger/hypotheses.md
python3 tools/route_sim.py --demo uniform --fraction 0.3
```

## What it does not have

A benchmark harness, data on concurrent load, and hardware other than our rig. The tools here help to orient, they do not launch or time a server.

## How it is maintained

This is a living notebook. New models and new results are added as dated entries. When a later check changes a decision, the old result stays next to the new one with the date, so the reason stays visible.

Every number says where it came from: a real run, a simulator on real traces (sim), a calculation (calc), a microbenchmark (micro) or someone else's number (ext).

Tested something from here on other hardware and got a different result? Open an issue with the [entry template](protocol/entry-template.md) filled in.

## Related

- [alesha-pro/4x3090-llm-benchmarks](https://github.com/alesha-pro/4x3090-llm-benchmarks): raw speed numbers with exact launch commands.
- [alesha-pro/qwen38-flashnext-strata-4x3090](https://github.com/alesha-pro/qwen38-flashnext-strata-4x3090): the full Qwen3.8-Flash-Next recipe.
- [alesha-pro/exllamav3-glm53-4x3090](https://github.com/alesha-pro/exllamav3-glm53-4x3090): the exllamav3 fork for GLM-5.3-Flash.
- [alesha-pro/project-maya](https://github.com/alesha-pro/project-maya): the Maya fork, with [Hy4 Flash notes](https://github.com/alesha-pro/project-maya/blob/82a77bf/docs/HY4-FLASH.md).
- [alesha-pro/maya-inkling-mini](https://github.com/alesha-pro/maya-inkling-mini): the Inkling 2 Mini engine on one RTX 3090, with a step by step guide.

By [@superalesha](https://x.com/superalesha). MIT license.
