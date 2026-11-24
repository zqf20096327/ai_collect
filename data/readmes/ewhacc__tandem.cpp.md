# tandem.cpp

tandem.cpp is a patch set for [llama.cpp](https://github.com/ggml-org/llama.cpp) that runs MoE models much larger than your
GPU, and larger than your RAM too. The most-used experts sit in a VRAM cache, the CPU computes a share of the misses, and the
rest are read from RAM or the SSD. **It works with any MoE model llama.cpp supports**, for one user at a time: measured on
Qwen3.8-Flash-Next, DeepSeek-V4.1-Flash, gpt-oss-120b, GLM-4.5-Air and Qwen3.6-35B-A3B, from 22 GB to over 300 GB of weights.

It is an independent project, not affiliated with ggml-org. Base: llama.cpp `f5222f25c` (2026-10-28, see `BASE_COMMIT`).
Version **v0.5.0** (2026-11-23). Changes: [CHANGELOG.md](CHANGELOG.md).

## Speed and quality at a glance

Decode tok/s, one user, greedy, cold start, tandem.cpp v0.5.0, re-measured for every release. The other engine is measured the
same day, on the same PC, with the same file and its own recommended settings. KL against the original weights: see
[Which model file](#which-model-file) (the same file gives the same KL on Strata and on tandem.cpp: 0.0260 vs 0.0259).

| Model, file | PC | tandem.cpp | Other engine, same day |
|---|---|---|---|
| Qwen3.8-Flash-Next IQ3_S + MTP (78 GiB) | RTX 5090 32 GB, 128 GB RAM | 190.5 | Strata v0.2.18: **201.1** |
| Qwen3.8-Flash-Next IQ3_S + MTP | RTX 5070 Ti 16 GB, 64 GB | 74.3 | Strata: **87.5** |
| Qwen3.8-Flash-Next IQ3_S + MTP | RTX 5070 Ti 16 GB, **32 GB** | **52.4** | Strata: 30.2–35.4 |
| Qwen3.8-Flash-Next IQ4_XS + MTP (91 GiB) | RTX 5070 Ti 16 GB, 64 GB | 49.5 | |
| DeepSeek-V4.1-Flash Maya-XS (102 GiB of experts) | RTX 5090 32 GB, 128 GB | **60.7** | Maya v1.1.73: 39.6, with DSpark 56.4 |
| DeepSeek-V4.1-Flash Maya-S (157 GiB of experts) | RTX 5090 32 GB, 128 GB | **29.0** | Maya: 22.9, with DSpark 22.4 |
| DeepSeek-V4.1-Flash Maya-S | RTX 5070 Ti 16 GB, **64 GB** | **9.4** | Maya: 6.0, with DSpark 6.1 |
| DeepSeek-V4.1-Flash IQ2_XS (139 GiB of experts) | RTX 5070 Ti 16 GB, 64 GB | 13.1 | |

When the model fits in RAM, Strata is faster on Qwen3.8; once it doesn't, tandem.cpp is. On long prompts read from the SSD the
other engines are faster: 15.7k tokens take 53 s on the 32 GB row (Strata 27–31 s) and 21 s on the Maya-S 128 GB row (Maya 14 s).
CPUs: i5-14600KF (5090 rows), i5-12400F (5070 Ti rows). Full tables, prompt times and older comparisons with llama.cpp:
[docs/results.md](docs/results.md).

For a big card serving many concurrent streams, use [Tandem-vLLM](https://github.com/ewhacc/tandem) instead.

## What's new in v0.5.0 (2026-11-23)

- **Up to +15% decode when the model is bigger than RAM.** The experts VRAM evicts are copied back to RAM on a second stream
  while the GPU computes, instead of in line with the uploads (Maya-S on 128 GB 25.2 → 29.0 tok/s, on 64 GB 8.6 → 9.4;
  DeepSeek-V4.1 IQ2_XS on 64 GB 12.5 → 13.1).
- **2× decode when the model just misses fitting in RAM.** Once the RAM store holds every expert, the CPU keeps computing its
  share of the misses instead of uploading all of them (Qwen3.8 IQ4_XS on a 16 GB card with 64 GB: 24.7 → 49.5 tok/s).
- **Faster long prompts when most of the model is in RAM:** layer streaming now also runs when part of the model is on the SSD,
  reading each layer's missing experts one layer ahead (Maya-S on 128 GB, 15.7k tokens: 30–40 → 20–26 s).
- Under a memory limit (Docker, systemd), the RAM store is sized to the limit instead of the host's RAM.

## Build

```
bash build.sh            # clones llama.cpp into ./tandem, checks out the base commit, applies tandem.patch, builds llama-server
```

or by hand:

```
git clone https://github.com/ggml-org/llama.cpp tandem && cd tandem && git checkout f5222f25c
git apply ../tandem.patch
cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --target llama-server
```

Tested with CUDA 13.0–13.4 on Ubuntu 22.04 and 24.04, sm_89 (RTX 4090, RTX 6000 Ada) and sm_120 (RTX PRO 6000 Blackwell).

### AMD GPUs (ROCm)

The patch builds with HIP. We use the same code as on CUDA; kernel work is done once in that shared code and measured on an RX 7900 XTX too:

```
git clone https://github.com/ggml-org/llama.cpp tandem && cd tandem && git checkout f5222f25c
git apply ../tandem.patch
cmake -B build -DGGML_HIP=ON -DGGML_HIP_GRAPHS=ON -DGPU_TARGETS=gfx1100 -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --target llama-server
```

Set `GPU_TARGETS` to your card (gfx1100 = RX 7900 series). `-DGGML_HIP_GRAPHS=ON` matters: without graphs every layer's kernels are
launched one by one. For `-ot`, use the ROCm device name, `ROCm0`, where the examples say `CUDA0`. `tandem-run.py` supports NVIDIA only.

AMD numbers (one RX 7900 XTX) are in [docs/results.md](docs/results.md#amd-rocm-2026-11-15).

## Quick start

```
bash build.sh                                  # builds llama-server (see Build above)
python3 tandem-run.py --model qwen3.8          # or: gpt-oss-120b, or --model /path/to/any-moe.gguf
```

`tandem-run.py` is one file (Python 3 standard library; Linux + NVIDIA only). It looks at your machine, picks the flags from the
[tuning guide](docs/tuning.md#how-it-works-and-the-flags) for it, prints each flag with a one-line reason and the exact command, then runs `llama-server` in the
foreground. When it prints `URL: http://127.0.0.1:8080/` the OpenAI-compatible API is ready at `/v1`.

It finds `llama-server` on your `PATH`, in `$TANDEM_SERVER`, or at `--server-bin`. `qwen3.8` and `gpt-oss-120b` are built in
with their MTP head / EAGLE3 draft: if the files are missing it shows the `hf download` commands and sizes and asks before
downloading (`--yes` accepts; files go to `--models-dir`, default `~/tandem-models`). Any other GGUF gets the generic MoE rules
and the plan says so. If the model fits in VRAM the launcher leaves the expert cache out, because plain llama.cpp is faster there.

What the launcher's plan and notes mean, `--dry-run`, calibration and other options: [docs/tuning.md](docs/tuning.md#the-launcher-tandem-runpy-in-detail).

## Which model file

Pick by RAM. Quality is the KL divergence of the next-token distribution against the original weights (Qwen3.8: the FP8 release; DeepSeek-V4.1: the official checkpoint), teacher-forced over about 8.6k tokens of greedy answers to 36 prompts; lower is better. Decode speed: tandem.cpp v0.5.0 (128 GB column: v0.4.0 except Maya-S), cold start, greedy, Qwen3.8 with the MTP head below.

| Model | File | Size | KL | Top-1 agreement | RTX 5090 + 128 GB | RTX 5070 Ti + 64 GB | Pick |
|---|---|---|---|---|---|---|---|
| Qwen3.8-Flash-Next | bartowski [Q4_K_M](https://huggingface.co/bartowski/Qwen3.8-Flash-Next-GGUF) | 111 GiB | **0.0173** | 95.4% | 102 tok/s | — | best quality, 128 GB+ |
| Qwen3.8-Flash-Next | bartowski [IQ4_XS](https://huggingface.co/bartowski/Qwen3.8-Flash-Next-GGUF) | 91 GiB | 0.0216 | 95.3% | 144 tok/s | 50 tok/s | balance; 128 GB, or 64 GB for better quality than IQ3_S |
| Qwen3.8-Flash-Next | ISTA [IQ3_S](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) | 78 GiB | 0.0259 | 94.8% | 191 tok/s | **74 tok/s** | fastest; the pick for 64 GB and 32 GB PCs |
| DeepSeek-V4.1-Flash | ISTA [IQ2_XS](https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF) | 139 GiB of experts | 0.1495 | 88.1% | 26–33 tok/s | 13 tok/s | balance; the pick for 64 GB |
| DeepSeek-V4.1-Flash | Maya [Maya-S](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF) | 157 GiB of experts | **0.1017** | 89.9% | 29 tok/s | 9.4 tok/s | best quality, 128 GB+ (Maya's engine: 23 tok/s) |
| DeepSeek-V4.1-Flash | Maya [Maya-XS](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF) | 102 GiB of experts | 0.2504 | 84.7% | 61 tok/s | — | fastest on 128 GB, lowest quality (Maya's engine: 40 tok/s) |

- On 64 GB, IQ4_XS no longer fits in RAM (part of it is read from the SSD): 50 tok/s against IQ3_S's 74, with lower KL. IQ3_S for speed, IQ4_XS for quality.
- Maya's DeepSeek-V4.1 quants run on tandem.cpp after a one-time conversion ([details](docs/results.md#deepseek-v41-maya-s-and-maya-xs-the-same-weights-on-both-engines)), which with `--link` writes about 210 GB beside Maya's files (the first shard and the joined Engram table). Maya-S's experts are larger than 128 GB of RAM, so both engines read part of every token from the SSD; on 64 GB it runs at 9.4 tok/s where IQ2_XS runs at 13.1 in the same session. IQ2_XS on 128 GB is a range: its experts just miss fitting in the page cache, so its speed depends on what the SSD has to re-read (two runs in one session: 31.6 and 25.5).
- Qwen3.8 below 3 bits loses too much (IQ2_XS: KL 0.126, 89.0%); DeepSeek-V4.1, a much larger model, holds up at 2 bits.
- Bartowski's Q4_K_M keeps the expert down-projections at 5–8 bits (5.3 bits per expert weight on average), which is where most of its lead comes from; IQ4_XS is 4.25.
- A better DeepSeek-V4.1 quant is coming: VQ2 + FP4, the main quant of [Tandem-vLLM](https://github.com/ewhacc/tandem), already on Hugging Face for that engine. Its GGUF comes out together with Tandem-vLLM's support for both the original DeepSeek-V4.1 and VQ2.
- The same MTP head works with all three Qwen3.8 files. For the bartowski files: `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include 'Qwen3.8-Flash-Next-IQ4_XS/*' --local-dir models` (or `Q4_K_M`), then pass the first shard to `-m`.

Qwen3.8-Flash-Next with its MTP head (the head as a separate GGUF). Download the model (IQ3_S, 78 GiB, two files) and the head (Q4_K):

```
hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include 'IQ3_S/*' --local-dir models
hf download ewhacc/qwen38-mtp-outq4_K-expsq4_K --include '*.gguf' --local-dir models
```

then run:

```
LLAMA_MTP_DRAFT_VOCAB=100000 llama-server -m models/IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf \
  -ngl 99 -cmoe --moe-cache-mib auto -lm none -np 1 -c 16384 \
  --spec-type draft-mtp -md models/qwen38-mtp-outq4_K-expsq4_K.gguf --spec-draft-n-max 3 --spec-draft-sampling probabilistic \
  -bs -ot '^token_embd\.weight=CUDA0'
```

- The head ([ewhacc/qwen38-mtp-outq4_K-expsq4_K](https://huggingface.co/ewhacc/qwen38-mtp-outq4_K-expsq4_K), Qwen Community License 1.0) was made with `convert_hf_to_gguf.py --mtp` on the original checkpoint (Q8_0), then its output and expert tensors to Q4_K: `llama-quantize --allow-requantize --tensor-type output=q4_K --tensor-type _exps=q4_K qwen38-mtp-q8_0.gguf qwen38-mtp.gguf Q8_0`. That takes it from 3.6 to 1.8 GiB of VRAM with the same acceptance; the freed memory goes to the expert cache.
- `--spec-draft-n-max 3` is best on 24 GB cards and 6–10 core CPUs; 4 on a 48 GB card.
- `--spec-draft-sampling probabilistic` keeps sampled output exact (rejection sampling) and acceptance high at the model's default temperature.

gpt-oss-120b with its EAGLE3 draft (`ggml-org/gpt-oss-120b-GGUF`):

```
llama-server -m gpt-oss-120b-MXFP4.gguf -ngl 99 -cmoe --moe-cache-mib auto -lm none -np 1 -c 16384 \
  --spec-type draft-eagle3 -md eagle3-gpt-oss-120b-Q8_0.gguf --spec-draft-n-max 4
```

EAGLE3 helps on 10+ core CPUs and slows things down on a 6-core one (see the consumer PC table).

More flags, how the cache works, and every default: [docs/tuning.md](docs/tuning.md).

## Limits

- Greedy output is not repeatable run to run with an expert cache: which experts are cached, and which misses the CPU computes, depends on timing, and the CPU and GPU round differently. Accuracy is unchanged. A fixed share (e.g. `LLAMA_MOE_CPU=0.2`) makes it repeatable.
- Built for one user at a time. Concurrent requests work (tested at 2 and 4, accuracy unchanged) but gain less, and with a small cache several requests together can be slower in total than one.
- Multi-GPU: only `-sm layer` (the default) works with the cache; checked for correctness on 2 GPUs, not tuned for speed.
- Layer streaming for long prompts needs one GPU, CUDA's virtual memory management, and every expert outside VRAM in pinned RAM; with CUDA older than 12.8 its copies go one by one, which is slower (it still works).
- Linux only. Tuned and tested on NVIDIA (CUDA). AMD (ROCm) works and gets the shared kernel work, but it has had less tuning and was tested on one RX 7900 XTX ([build](#amd-gpus-rocm)); it does not borrow cache VRAM for prompts (no VMM in ROCm builds), so its cache is a little smaller.
- Qwen3.8 GGUFs converted with a current llama.cpp may be a little slower than the ISTA files we measured (one fusion does not apply to their layout).
- Known issues, to be fixed:
  - models much larger than RAM (read from the SSD) depend on the drive (see the gaming-PC rows for a PCIe 4.0 drive);
  - DeepSeek-V4.1 with `-lm none` loads very slowly (its 103 GiB Engram tables are copied page by page); run it without `-lm none`;
  - a model whose experts are a little larger than RAM (DeepSeek-V4.1 IQ2_XS, 139 GiB, on 128 GB) runs from the page cache, and
    long prompts read the SSD again on every batch (15.7k tokens: ~57 s on the RTX 5090 PC; Maya-XS, which fits, 16.5 s).

## Licence

MIT, see [LICENSE](LICENSE). tandem.patch modifies llama.cpp, which is MIT-licensed by the ggml authors.
If you use ideas from tandem.cpp in your own project, a link back is appreciated.
