# Inference optimization playbook

My field notebook for tuning LLM inference on consumer GPUs. The ledger covers 138 tested hypotheses across 7 model cases, with the verdict, measurements and test conditions for each. I publish it as a read-only reference for people tuning local inference and as a skill for coding agents.

My rig measurements use 1-4 RTX 3090 cards (24 GB each). The cases cover expert offload to RAM and models or quants that fit in VRAM, including Inkling 2 Mini on 1 card and Ling-3.2-air R3 on 3-4 cards. Engines include Strata, Maya forks, an exllamav3 fork, llama.cpp and vLLM. [Rig details and model cases](cases/README.md)

| Model and setup | What changed | Result |
|---|---|---|
| [DeepSeek V4.1 Flash](cases/deepseek-v4.1-flash.md), 4 cards | DMA from pinned RAM for all formats, prompt layer skipping, automatic chunking | 32K prefill rose from 430 to 2,199 tok/s |
| DeepSeek V4.1 Flash, Zen 2 CPU | Disabled the PDEP path at build time | Time per cold expert dropped from 1.6 to 0.44 ms |
| [Hy4 Flash](cases/hy4-flash.md), 1 card | Loaded each needed expert once per block of up to 57,600 tokens, with 2,048-token attention tiles | The full build raised 57,587-token prefill from 415.6 to 1,510.2 tok/s |
| Hy4 Flash, 2 cards | Ran cold experts on the CPU while the GPUs ran hot experts | Short code decode rose from 24.6 to 70.4 tok/s |
| [Qwen3.8-Flash-Next](cases/qwen3.8-flash-next.md), 1-2 cards | DFlash2 drafter | Decode gained 44-46% over plain decode |
| Qwen3.8-Flash-Next, Russian | Cyrillic draft vocabulary | Draft acceptance rose from 32% to 54% |
| [MiniMax-M3.1-Flash](cases/minimax-m3.1-flash.md) | Gathered attention K/V into VRAM once per chunk | 3.3x faster 64K prefill |
| [GLM-5.3-Flash](cases/glm-5.3-flash.md), 2.05 bpw in VRAM, 4 cards | Switched from layer split to tensor parallel | Decode rose from 48.3 to 66-68 tok/s |
| [Inkling 2 Mini](cases/inkling-2-mini.md), 1 card | Resident experts, 1 CUDA graph per token, tensor cores for experts and attention | The final build reached 128.7 tok/s after 47 prompt tokens with a 344K window, and 62.3 tok/s after 340K tokens |
| [Ling-3.2-air](cases/ling-3.2-air.md) R3, 4 cards, FP16 KV | Restored stage pipelining with every expert in VRAM | 32K prefill rose from 2,230 to 5,439 tok/s. Plain decode reached 124.4 tok/s |
| Ling-3.2-air R3, 2 cards, INT8 KV | Enabled adaptive `blk.42` MTP | Warm decode after a 2K prompt rose from 120.31 to 143.8 tok/s |

### Negative results

- A static MiniMax expert profile gave 64-69% hits against 61% for random placement (sim).
- Fine-tuning drafters on my own data gave little or no gain across 3 models.
- A short DeepSeek quant benchmark showed a 27% decode gain. Real generation gained 2%.
- On Hy4 Flash, quantizing the drafter head matched the first 4,400 tokens and shifted a cache snapshot boundary, changing the second turn.
- When streaming Ling-3.2-air experts from NVMe with a cold page cache, buffered reads gave 45-92% higher throughput than `O_DIRECT` under 8 and 24 GiB memory caps.

The cheapest way to serve an expert miss flipped between models on the same rig. Use the placement, hardware and workload tags to find a result that applies to your setup. Chapters 01-15 end with steps for testing the mechanism on another model.

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
playbook/    start page and 15 chapters by mechanism
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
protocol/    situation card, experiment rules, new-model checklist, rig experiment log format
tools/       route_sim.py (skew and cache simulator), fit_cost.py (time model fit)
SKILL.md     entry point for agents
AGENTS.md    internal notebook maintenance rules
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

## Notes on the measurements

Most measurements are for 1 active request. The tools estimate routing, cache behavior and token time from inputs you supply. Use your engine's benchmark or session replay to measure throughput.

Unlabeled results come from measured runs. Labels mark simulations (sim), calculations (calc), microbenchmarks (micro), external measurements (ext) and single runs (1 run). When a later test changes a verdict, I keep the earlier result next to the new one.

## Related

- Per-run speed measurements and exact launch commands. [4x3090 benchmark archive](https://github.com/alesha-pro/4x3090-llm-benchmarks)
- Qwen3.8-Flash-Next setup and raw traces. [Strata recipe](https://github.com/alesha-pro/qwen38-flashnext-strata-4x3090)
- GLM-5.3-Flash engine and setup. [exllamav3 fork](https://github.com/alesha-pro/exllamav3-glm53-4x3090)
- Hy4 Flash engine and implementation notes. [Maya fork](https://github.com/alesha-pro/project-maya), [Hy4 Flash notes](https://github.com/alesha-pro/project-maya/blob/82a77bf/docs/HY4-FLASH.md)
- Inkling 2 Mini engine and setup for 1 RTX 3090. [maya-inkling-mini](https://github.com/alesha-pro/maya-inkling-mini)
- Ling-3.2-air engine and benchmark notes. [Upstream Maya pull request #1224](https://github.com/mw00/project-maya/pull/1224)

MIT license. [@superalesha](https://x.com/superalesha)
