# littlebit-gguf

Run **sub-1-bit LittleBit and LittleBit-2 language models in llama.cpp**, using the 1-bit `Q1_0` tensor type llama.cpp already ships instead of writing new kernels.

> **This is a research project.** It is independent and experimental, and it is not affiliated with or endorsed by Samsung or the llama.cpp project. Expect breaking changes and rough edges.

## The idea

LittleBit (Samsung Research, NeurIPS 2025) and LittleBit-2 (ICML 2026) compress every linear layer of a transformer into two small sign matrices and three scale vectors, reaching 0.1 to 1 bit per weight. A layer computes:

```
y = h ⊙ U±( l ⊙ V±( g ⊙ x ) )
```

llama.cpp's `Q1_0` type stores weights in blocks of 128 bits with one fp16 scale `d` per block, and each bit means `+d` or `−d`. Because that scale belongs to a block within a single row, LittleBit's row scales fold straight into it:

- `V' = diag(l) · V±` : every block in row `k` gets `d = l_k`
- `U' = diag(h) · U±` : every block in row `i` gets `d = h_i`

So a LittleBit layer becomes one element-wise multiply and two ordinary `Q1_0` matrix multiplies:

```
y = U' · ( V' · ( g ⊙ x ) )          (and the same again for the residual path)
```

The patched graph uses ggml's existing `Q1_0` kernel and element-wise multiply.

## What it costs

`Q1_0` needs each row length to be a multiple of 128, so the rank is padded up to the next multiple of 128 (padded rows get `d = 0` and add nothing; with `--unpadded-v` only `lb_u` is padded, see below), and each block carries 16 bits of scale. Estimated bits per weight for the compressed layers:

| Model | Trained at | In GGUF |
|---|---|---|
| Llama-2-7B | 1.0 | ~1.15 |
| Llama-2-7B | 0.55 | ~0.69 |
| Llama-2-7B | 0.1 | ~0.12 |
| Qwen2.5-0.5B | 0.55 | ~0.80 |
| Qwen2.5-0.5B | 0.1 | ~0.47 |

Large models lose little. Small models at very low bit rates lose a lot to padding, because their ranks are tiny. Training with ranks that are multiples of 128 avoids it, and the converter warns when padding is heavy. (Estimates from the shape arithmetic; the converter prints the real figure for each file.)

The other half of the story is the layers LittleBit leaves alone. The reference keeps token embeddings and the output layer in 16 bits, and in small models they are most of the file: about 272 MB for Qwen2.5-0.5B next to about 4 MB of LittleBit layers at 0.1 bits per weight. The converter can store them as `Q8_0`, `Q6_K` or `Q4_K` instead.

## Status

| Component | Status |
| --- | --- |
| Design and format notes | Done. See [design](docs/DESIGN.md) and [format](docs/FORMAT.md). |
| Converter and embedding fallbacks | Done for F16, Q8_0, Q4_K and Q6_K requests, including tied embeddings. |
| llama.cpp CPU patch | Done for Llama, Qwen2 and Qwen3 with projection inputs divisible by 128. |
| GGUF format version 2 and opt-in GPU build switches | Version 2 (unpadded `lb_v`) is done and tested on CPU. The GPU switches are untested here. |
| Fast tests, published checkpoint checks and CPU benchmarks | Done. Published checks cover Qwen2.5 and Qwen3 at both bit rates. |
| Qwen3-0.6B 1.0 bpw under the original float limits | Failing under the original limits. The published test uses limits based on measured cache and activation rounding for this checkpoint. |
| Architecture coverage and upstream integration | Partial. More architectures and backends remain outside the CPU milestone. The local patch is required. |

Until the changes are upstream, LittleBit GGUF files need the patched build from this repo. Stock llama.cpp, Ollama and LM Studio will not load them yet.

## Build on Linux or WSL

The llama.cpp submodule is pinned to `6aee50801d091f78b3baacd505f5e95d8e8f6838`. The build script initializes the submodule, applies the patches, and builds the CPU tools. It can be rerun on the same checkout. Use a C++ compiler, CMake, Ninja, and Python 3.12.

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install 'torch>=2.6' --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r requirements.txt pytest ruff
bash scripts/build.sh
python -m pytest
```

Set `LITTLEBIT_BUILD_DIR` to an absolute path to put build output on another drive. Set `LITTLEBIT_JOBS` to change the build's two-job default. `LITTLEBIT_NATIVE=OFF` disables CPU-native tuning.

### GPU builds (opt-in, untested here)

The default build is CPU-only. `LITTLEBIT_CUDA=ON`, `LITTLEBIT_METAL=ON` and `LITTLEBIT_VULKAN=ON` turn on the matching llama.cpp backend, for example `LITTLEBIT_CUDA=ON bash scripts/build.sh`. **No GPU build has been tested by this project.** The development machine has no NVIDIA GPU, so these switches only pass the standard `GGML_CUDA`, `GGML_METAL` and `GGML_VULKAN` options to llama.cpp. For GPU results, see the CUDA runs that luben93 made with this tree: [speed on an RTX A1000](https://github.com/luben93/littlebit-llamacpp/blob/5ca825f6f71e5c690cd2dc4326ff615d73667cda/results/geniusdevam/bench-cuda.tsv) and [12-window perplexity](https://github.com/luben93/littlebit-llamacpp/blob/5ca825f6f71e5c690cd2dc4326ff615d73667cda/results/geniusdevam/ppl-8853f81-cuda-f16-12chunks.txt) (20.8654, built with `-DGGML_CUDA=ON` at revision 2) and [the issue thread](https://github.com/GeniusDevam/littlebit-gguf/issues/1).

## Convert and run

```sh
python convert_littlebit_to_gguf.py checkpoints/littlebit --outfile model.gguf \
    --embd-type q8_0 --validate 5
build/bin/llama-cli -m model.gguf -ngl 0 -t 4 -c 512 --single-turn -p 'Once upon a time' -n 32
```

By default the rank is padded in both `lb_u` and `lb_v` (GGUF format version 1). `--unpadded-v` stores `lb_v` at the true rank and writes format version 2, which saves the padding in `lb_v`; the loader pads the latent at run time. When every rank is already a multiple of 128 both layouts are the same bytes and the file stays at version 1. The loader reads both versions and refuses any other. The layout is specified in [the format notes](docs/FORMAT.md#gguf-layout), including the reserved layout for mixture-of-experts tensors, which this repository does not implement yet. `--model-name` sets `general.name`; the default is `LittleBit <family> <size>`, where the size counts the dense weights.

The converter reads `littlebit_config.json` or the fields in `config.json`. Older checkpoints can supply `--eff-bit`, `--residual` or `--no-residual`, and `--use-itq` when needed. `--embd-type` and `--output-type` accept `f16`, `q8_0`, `q6_k`, and `q4_k`. The output defaults to the embedding type. Tied embeddings remain shared when the effective embedding and output types match. Aligned K types require the compiled `libggml-base.so`. When the row width is incompatible, the converter prints a notice and uses the same fallback types as the pinned `llama-quantize`: Q4_K becomes Q5_0, and Q6_K becomes Q8_0. If the width also fails the smaller block alignment, the converter uses F16. Qwen2.5-0.5B uses the fallback at width 896. SmolLM2-135M is out of scope because its 576-wide projections fail the 128-column input alignment.

The synthetic generator applies Dual-SVID initialization to a local Hugging Face checkpoint or model ID. It supports `--residual` and `--no-residual`. Synthetic checkpoints are for arithmetic and runtime checks. Their language-model quality reflects initialization without training.

The slow test compares four synthetic checkpoints with a plain PyTorch reference and a reference that rounds activations before both Q1_0 matmuls. For Qwen3-0.6B at 1.0 bpw, changing only the cache precision moved logits by up to 5.54. The Q8-aware reference and F32-cache runtime agreed on 77.86% of token positions. The test uses a separate tolerance for this checkpoint and checks the Q8-aware result separately.

```sh
python tools/make_synthetic.py Qwen/Qwen3-0.6B checkpoints/qwen3-0.1 --eff-bit 0.1
python convert_littlebit_to_gguf.py checkpoints/qwen3-0.1 --outfile checkpoints/qwen3-0.1-f16.gguf
LITTLEBIT_TEST_DATA=checkpoints python -m pytest -m slow -s -k '0.1 and qwen3'
```

## Measured file sizes

These are initialized synthetic checkpoints with residuals enabled and tied embeddings. File sizes include metadata and tokenizer data and use decimal MB. Projection bits per weight exclude embeddings and the output head.

| Model | Target bpw | Requested embedding | Stored embedding | File (MB) | Projection bpw |
| --- | --- | --- | --- | --- | --- |
| Qwen2.5-0.5B | 0.1 | F16 | F16 | 300.31 | 0.4865 |
| Qwen2.5-0.5B | 0.1 | Q8_0 | Q8_0 | 172.69 | 0.4865 |
| Qwen2.5-0.5B | 0.1 | Q4_K | Q5_0 | 121.64 | 0.4865 |
| Qwen2.5-0.5B | 0.1 | Q6_K | Q8_0 | 172.69 | 0.4865 |
| Qwen2.5-0.5B | 1.0 | F16 | F16 | 333.27 | 1.2234 |
| Qwen2.5-0.5B | 1.0 | Q8_0 | Q8_0 | 205.64 | 1.2234 |
| Qwen2.5-0.5B | 1.0 | Q4_K | Q5_0 | 154.59 | 1.2234 |
| Qwen2.5-0.5B | 1.0 | Q6_K | Q8_0 | 205.64 | 1.2234 |
| Qwen3-0.6B | 0.1 | F16 | F16 | 342.44 | 0.4542 |
| Qwen3-0.6B | 0.1 | Q8_0 | Q8_0 | 196.58 | 0.4542 |
| Qwen3-0.6B | 0.1 | Q4_K | Q4_K | 118.79 | 0.4542 |
| Qwen3-0.6B | 1.0 | F16 | F16 | 383.72 | 1.2042 |
| Qwen3-0.6B | 1.0 | Q8_0 | Q8_0 | 237.87 | 1.2042 |
| Qwen3-0.6B | 1.0 | Q4_K | Q4_K | 160.07 | 1.2042 |

The Qwen2.5-0.5B run at 0.1 measured 0.4865 bits per compressed weight, compared with the shape estimate of about 0.47 above. Rank padding and the F32 input scales count toward the measured figure.

## CPU throughput

Measured on an Intel Core i7-8550U in Ubuntu WSL2 with the pinned llama.cpp commit above. The Release build used `GGML_NATIVE=ON` with AVX2, FMA, F16C and BMI2, and OpenMP was enabled. GPU backends and BLAS were disabled. All rows ran sequentially in one session with four CPU threads. Timings are the mean and standard deviation of five repetitions. Batch size was 2048, micro-batch size was 512 and flash attention used automatic selection.

```sh
build/bin/llama-bench -m model.gguf -ngl 0 -t 4 -p 128 -n 32 -r 5 -o json
```

| Model | Weights | File (MB) | Prompt 128 (tok/s) | Generation 32 (tok/s) |
| --- | --- | --- | --- | --- |
| Qwen2.5-0.5B | LittleBit 0.1, F16 | 300.31 | 199.30 ± 23.38 | 29.93 ± 4.68 |
| Qwen2.5-0.5B | LittleBit 1.0, F16 | 333.27 | 110.14 ± 3.45 | 26.71 ± 2.49 |
| Qwen2.5-0.5B | Dense Q1_0 | 75.70 | 138.16 ± 12.68 | 65.67 ± 7.05 |
| Qwen2.5-0.5B | Dense Q4_0 | 284.09 | 231.68 ± 9.07 | 47.53 ± 1.02 |
| Qwen2.5-0.5B | Dense Q8_0 | 531.07 | 157.81 ± 18.79 | 19.24 ± 2.53 |
| Qwen2.5-0.5B | LittleBit 0.1, Q4_K → Q5_0 | 121.64 | 208.50 ± 9.51 | 57.36 ± 1.21 |
| Qwen2.5-0.5B | LittleBit 0.1, Q6_K → Q8_0 | 172.69 | 78.87 ± 15.66 | 45.49 ± 3.53 |
| Qwen2.5-0.5B | LittleBit 1.0, Q4_K → Q5_0 | 154.59 | 115.89 ± 4.86 | 42.19 ± 0.71 |
| Qwen2.5-0.5B | LittleBit 1.0, Q6_K → Q8_0 | 205.64 | 114.92 ± 6.52 | 38.45 ± 0.96 |
| Qwen3-0.6B | LittleBit 0.1, F16 | 342.44 | 188.86 ± 4.55 | 29.62 ± 5.69 |
| Qwen3-0.6B | LittleBit 0.1, Q4_K | 118.79 | 181.92 ± 5.46 | 55.46 ± 8.01 |
| Qwen3-0.6B | LittleBit 1.0, F16 | 383.72 | 64.27 ± 7.45 | 20.48 ± 1.04 |
| Qwen3-0.6B | Dense Q1_0 | 111.90 | 113.45 ± 12.12 | 46.66 ± 4.48 |
| Qwen3-0.6B | Dense Q4_0 | 428.97 | 172.80 ± 26.63 | 35.92 ± 4.72 |
| Qwen3-0.6B | Dense Q8_0 | 804.75 | 117.88 ± 13.26 | 19.10 ± 3.47 |

14 of the 30 timings had a standard deviation above 10% of the mean after five repetitions. The table gives the deviation for each comparison.

## Trained Qwen3-8B checkpoint

These measurements use a trained LittleBit-2 checkpoint with residual paths and untied embeddings and output weights. The checkpoint is CC BY-NC 4.0. The checkpoint and converted GGUFs are kept local. [Checkpoint revision `6b2c47a`](https://huggingface.co/LittleBitLLM/littlebit-qwen3-8b-0.55bpw/tree/6b2c47aa9707e624e2e737d16d64a66be8090ae9)

The tests ran on an Intel Core i7-8550U with four threads in Ubuntu WSL2 using the pinned CPU build. Perplexity uses 2,048-token windows of the WikiText-2 raw test split. Speed is the mean of five `llama-bench` repetitions at `-p 128 -n 32`.

| Embedding / output | File (GB) | PPL after 4 windows | PPL after 12 windows | Prompt 128 (tok/s) | Generation 32 (tok/s) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Q4_K / Q6_K | 1.457 | 26.3547 | 20.9236 | 8.47 | 5.11 |
| F16 / F16 | 3.086 | 26.2586 | 20.8386 | 5.04 | 4.80 |

The compressed projections use 0.6787 bits per dense projection weight, including both paths and the F32 input multipliers. Rank padding accounts for 56.7 MB of projection data. Conversion with `--validate 3` flushed 56 nonzero scales to zero and preserved FP16 subnormals.

### Unpadded `lb_v` (format version 2)

The same checkpoint converted with `--unpadded-v` and Q4_K / Q6_K gives a 1,430,186,784-byte file, 26,873,856 bytes (1.84%) smaller than the padded 1,457,060,640 bytes. The remaining padding is in `lb_u`. Perplexity after 12 windows is 20.9236, the same as the padded file, and the logits for two full windows are bit-identical to the padded file's. The speed rows below were measured back to back in one session with `llama-bench -ngl 0 -t 4 -p 128 -n 32 -r 5` on the padded file with the previous build and with this build, and on the unpadded file with this build, two rounds each. The previous build cannot load the unpadded file. These numbers come from a faster session than the table above and are not comparable with it.

| Build | File | Prompt 128 (tok/s) | Generation 32 (tok/s) |
| --- | --- | ---: | ---: |
| Revision 3 | padded | 10.88 ± 0.72, 11.01 ± 0.49 | 7.00 ± 0.07, 6.97 ± 0.05 |
| This build | padded | 11.38 ± 0.13, 11.37 ± 0.05 | 6.96 ± 0.08, 6.98 ± 0.04 |
| This build | unpadded | 11.52 ± 0.26, 11.48 ± 0.25 | 7.06 ± 0.16, 7.16 ± 0.05 |

## Against a dense model of the same size

The 8B checkpoint with Q2_K embeddings and output is about 1250 MiB. A dense Qwen3-1.7B at Q4_K_M is 1223 MiB. On WikiText-2 the dense model scores better:

| Model | File | WikiText-2 perplexity |
| --- | ---: | ---: |
| LittleBit Qwen3-8B 0.55 bpw, Q2_K embeddings and output | 1250 MiB | 22.41 ± 0.18 |
| Qwen3-1.7B Q4_K_M | 1223 MiB | 15.02 ± 0.14 |

These runs are luben93's, not reproduced here, because this project has no GPU. Protocol: `llama-perplexity -c 2048 -b 2048 -ngl 99` on an RTX A1000 6 GB with llama.cpp `9183a55` plus luben93's patch, over all 145 windows of the WikiText-2 test split, scoring the second half of each window. The numbers are not comparable with the 12-window CPU tables above. Sources: [LittleBit](https://github.com/luben93/littlebit-llamacpp/blob/5ca825f6f71e5c690cd2dc4326ff615d73667cda/results/same-size/ppl-littlebit-8b-q2_k.wiki.txt) and [Qwen3-1.7B](https://github.com/luben93/littlebit-llamacpp/blob/5ca825f6f71e5c690cd2dc4326ff615d73667cda/results/same-size/ppl-qwen3-1.7b-Q4_K_M.wiki.txt) logs, and the speed table in [bench-cuda.tsv](https://github.com/luben93/littlebit-llamacpp/blob/5ca825f6f71e5c690cd2dc4326ff615d73667cda/results/same-size/bench-cuda.tsv). ScarionWorkspace measured the same ordering on a different GPU with all positions scored: 24.70 for a 1225 MiB LittleBit file against 16.90 for the 1223 MiB dense model, in [their baseline table](https://github.com/ScarionWorkspace/littlebit-gguf/blob/ef3ebbafc6386ea72d689311365ee87e29ad269a/results/baselines/TABLE.md). At this size this checkpoint does not beat the dense model.

## Related work

- LittleBit: [arXiv:2506.13771](https://arxiv.org/abs/2506.13771). LittleBit-2: [arXiv:2603.00042](https://arxiv.org/abs/2603.00042).
- Official training code: [SamsungLabs/LittleBit](https://github.com/SamsungLabs/LittleBit) (CC BY-NC 4.0). No code from it is used or redistributed here.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT), whose `Q1_0` type was added for PrismML's 1-bit Bonsai models.
- Sister project: [littlebit.cpp](https://github.com/GeniusDevam/littlebit.cpp), dedicated CPU kernels for LittleBit layers.
- [luben93/littlebit-llamacpp](https://github.com/luben93/littlebit-llamacpp) (MIT) is a parallel implementation of the same Q1_0 approach.

## License

MIT, see [LICENSE](LICENSE). llama.cpp is MIT licensed. Model weights keep their own licenses.

## Citation

Please cite the original papers:

```bibtex
@inproceedings{lee2025littlebit,
  title     = {LittleBit: Ultra Low-Bit Quantization via Latent Factorization},
  author    = {Lee, Banseok and Kim, Dongkyu and You, Youngcheon and Kim, Youngmin},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2025}
}

@inproceedings{lee2026littlebit2,
  title     = {LittleBit-2: Maximizing the Spectral Energy Gain in Sub-1-Bit LLMs via Latent Geometry Alignment},
  author    = {Lee, Banseok and Kim, Youngmin},
  booktitle = {International Conference on Machine Learning},
  year      = {2026}
}
```
