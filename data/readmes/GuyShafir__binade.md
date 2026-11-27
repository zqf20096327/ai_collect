<p align="center"><img src="https://raw.githubusercontent.com/GuyShafir/binade/main/docs/social-preview.png" width="100%" alt="binade: lossless LLM weights, outputs bit-identical. Below the words, a band of exponent ranks from real Gemma 4 12B weights, one square per weight."></p>

# Binade

Bit-exact compression of BF16 LLM weights that runs compressed: on NVIDIA GPUs (through MLX's CUDA backend) and on Apple Silicon (MLX).

A BF16 weight keeps its sign and mantissa as one raw byte. Its 8-bit exponent (the weight's binade) is replaced by its frequency rank in a per-tensor table, stored on disk in Rice codes at about 10.75 bits per weight instead of 16. At load, the ranks become a 4-bit runtime layout that CUDA and Metal kernels read directly during inference.

The outputs are bit-identical to the original model, not merely close. The kernels reproduce the summation order of MLX's own BF16 kernels, so prompt logits and generated tokens match the uncompressed model exactly.

## Results on NVIDIA GPUs

RTX PRO 6000 (96 GB), MLX 0.32.2's CUDA backend, greedy decoding at batch 1, median of three fresh processes. Every number comes from a script in `scripts/`; its output is in `results/`.

| | BF16 | Binade | |
|---|---|---|---|
| Llama 3.1 8B | 89.6 tok/s, 16.2 GB | 101.5 tok/s, 12.6 GB | **1.13x** ([decode_speed](results/cuda/Llama-3.1-8B-Instruct/decode_speed.md)) |
| Qwen3.5 9B | 82.2 tok/s, 18.4 GB | 97.6 tok/s, 14.4 GB | **1.19x** ([decode_speed](results/cuda/Qwen3.5-9B/decode_speed.md)) |
| Gemma 4 12B | 55.5 tok/s, 24.1 GB | 63.4 tok/s, 18.8 GB | **1.14x** ([decode_speed](results/cuda/gemma-4-12B-it/decode_speed.md)) |
| Gemma 4 31B | 22.9 tok/s, 62.1 GB | 27.4 tok/s, 47.5 GB | **1.20x** ([decode_speed](results/cuda/gemma-4-31B-it/decode_speed.md)) |
| Gemma 4 26B-A4B (MoE) | 132.3 tok/s, 51.9 GB | 133.8 tok/s, 39.1 GB | **1.01x** ([decode_speed](results/cuda/gemma-4-26B-A4B-it/decode_speed.md)) |

Exactness: logits at all 16,352 WikiText-2 positions per model identical to BF16, and 32 of 32 greedy generations ([summary](results/cuda/summary.md)); for Gemma 4 12B and 26B-A4B on every GPU listed below, also with the fused prompt kernels forced onto every prompt length.

**Against the other lossless runtime.** Llama 3.1 8B on the same GPU and prompt: DFloat11 decodes 25.8 tok/s in 12.0 GB, Binade 101.5 tok/s in 12.6 GB, 3.9 times as fast at batch 1. Each is bit-identical to its own framework's BF16: DFloat11 runs at 0.38x PyTorch's (68.3 tok/s), Binade at 1.13x MLX's (89.6 tok/s). DFloat11 rebuilds BF16 weights before each forward pass, a cost it amortizes over larger batches; Binade computes from the compressed layout. Batched serving is not in this comparison ([pytorch](results/cuda/pytorch.md)).

Where BF16 does not fit:

| GPU | model | BF16 | Binade | first token after 40 tokens |
|---|---|---|---|---|
| L4 (24 GB) | Gemma 4 12B | out of memory | 20.0 GB peak, 11.1 tok/s, identical to BF16 streamed from disk ([results/cuda-l4](results/cuda-l4/gemma-4-12B-it)) | 0.257 s (8-bit: 0.148 s) |
| A100 (40 GB) | Gemma 4 26B-A4B | out of memory | 40.0 GB peak, 46.5 tok/s, identical to BF16 streamed from disk ([results/cuda-a100](results/cuda-a100/gemma-4-26B-A4B-it)) | 0.101 s (8-bit: 0.084 s; Binade is faster from 128 tokens on) |

On the RTX PRO 6000 the first token after a 40-token prompt takes 0.059 s for the 12B (BF16 0.045) and 0.053 s for the 26B (BF16 0.041).

Multi-row products in MLX's CUDA backend go to cuBLAS, which is closed. Its BF16 GEMM order can still be reproduced: each output is a sequence of tensor-core MMA steps along K, split-K partitions follow a fixed rule, and cuBLASLt reports which algorithm and split it chose. The algorithms differ by GPU (one of them, on the A100 and L4, sums K in two slices), so the fused prompt kernels run only for algorithms verified on that GPU (`binade/mlx/cublas_plan.py`, `tests/test_cuda_gemm.py`); anything else rebuilds BF16 weights for cuBLAS, which is exact by construction.

## Results on Apple Silicon

Apple M4 Max, 48 GB, MLX 0.32.2.

| | BF16 | Binade | |
|---|---|---|---|
| Gemma 4 12B checkpoint | 23.92 GB | 16.10 GB | 10.746 bits per packed weight, bit-exact round trip ([roundtrip_v2](results/gemma-4-12B-it/roundtrip_v2.md)) |
| Gemma 4 12B greedy decode | 19.15 tok/s | 24.66 tok/s | **1.29x**, identical tokens ([decode_speed](results/gemma-4-12B-it/decode_speed.md)) |
| Gemma 4 12B exactness | | | prompt logits over the full vocabulary and 256 greedy tokens identical ([generate_check](results/gemma-4-12B-it/generate_check_r4_v2_binade_first.md)) |
| Gemma 4 12B decode with its self-draft | 18.74 tok/s | 32.19 tok/s | **1.72x**: the pack verifies a 4-bit draft of itself, 3 tokens per step; 25.0 GB resident; tokens identical to BF16 run with the same draft ([self_draft](results/gemma-4-12B-it/self_draft.md)) |
| Gemma 4 26B-A4B checkpoint | 51.61 GB | 35.05 GB | BF16 does not load on a 48 GB Mac ([roundtrip_v2](results/gemma-4-26B-A4B-it/roundtrip_v2.md)) |
| Gemma 4 E4B checkpoint | 15.99 GB | 10.70 GB | every tensor packed: the 2.8B-weight per-layer embedding table and the vision and audio towers too; Google's 4-bit QAT checkpoint (w4a16, that table left in 16-bit) is 11.51 GB ([roundtrip_v2](results/gemma-4-E4B-it/roundtrip_v2.md)) |
| Gemma 4 E4B resident after load | 14.93 GB | 10.79 GB | the per-layer table stays in its Rice coding in memory; logits at all 16,352 positions and 32 of 32 generations identical ([fit_probe](results/gemma-4-E4B-it/fit_probe.md), [exactness_scale](results/gemma-4-E4B-it/exactness_scale.md)) |
| Gemma 4 E2B checkpoint | 10.25 GB | 6.84 GB | 6.59 GB resident, decode 1.18x, identical at 16,352 positions and 32 of 32 generations ([roundtrip_v2](results/gemma-4-E2B-it/roundtrip_v2.md), [exactness_scale](results/gemma-4-E2B-it/exactness_scale.md), [decode_speed](results/gemma-4-E2B-it/decode_speed.md)) |
| Llama 3.1 8B decode with its self-draft | 30.4 tok/s | 59.6 tok/s | **1.96x**, 17.3 GB resident (BF16 with the same draft: 54.0 tok/s in 20.8 GB), identical tokens in every mode ([self_draft](results/Llama-3.1-8B-Instruct/self_draft.md)) |
| Llama 3.2 3B decode with its self-draft | 67.2 tok/s | 118.0 tok/s | **1.76x**, 7.2 GB resident, identical tokens in every mode ([self_draft](results/Llama-3.2-3B-Instruct/self_draft.md)) |
| Qwen3.5 4B checkpoint | 9.32 GB | 6.27 GB | 6.35 GB resident, decode 1.27x, identical at 16,352 positions and 32 of 32 generations ([roundtrip_v2](results/Qwen3.5-4B/roundtrip_v2.md), [exactness_scale](results/Qwen3.5-4B/exactness_scale.md), [decode_speed](results/Qwen3.5-4B/decode_speed.md)) |
| Gemma 4 26B-A4B decode | n/a | 58.8 tok/s | 40-token prompt in 0.32 s, logits and 64 tokens identical to BF16 ([decode_speed](results/gemma-4-26B-A4B-it/decode_speed.md), [generate_check](results/gemma-4-26B-A4B-it/generate_check_r4_v2_streamed_binade_first.md)) |

The 26B exactness check compares against a BF16 reference that reads one layer at a time from disk, since BF16 does not fit in memory.

- **Matvec kernel.** Batch-1 matvec on the 12B's shapes runs at 100% of BF16's bandwidth efficiency, 1.33x BF16 per token ([kernel test](results/kernel/gemma-4-12B-it.md)).
- **Distance to the floor.** The file is 0.21 to 0.30 bits per weight (2 to 3%) above the entropy of the whole BF16 pattern on four models, and a first-order context model of the exponents could save at most 0.004 bits more ([entropy_floor](results/entropy_floor.md)).
- **Prompt processing (12B matmuls).** 1.30x BF16 at 16 prompt rows, 0.77 to 0.90x at 32 to 128, and 0.95x at 2048 ([prefill_bench](results/gemma-4-12B-it/prefill_bench.md)).

## How it works

- **No exponent locality.** Neighbouring weights do not share exponents: per-tile palettes gain only 0.011 to 0.027 bits per weight over a shuffled tensor on four models ([comparison](results/comparison.md)). Binade therefore codes frequency ranks from one table per tensor.
- **Two file formats.** Format 1 uses fixed width per 128-weight tile with escapes (11.27 bits per weight). Format 2, the default, uses Rice codes (10.75 bits per weight).
- **Runtime layout.** At load a GPU kernel turns either format into R4: every rank in 4 bits, with rare escapes. R4 takes 12.07 bits per weight in memory, and its matvec streams at full bandwidth. A table that only ever feeds lookups (Gemma 4 E-models' per-layer embedding table) stays in its Rice coding in memory, and the Rice kernel decodes the rows each lookup asks for.
- **Exactness.** The matvec, the MoE expert gather and the GEMM mirror MLX's own kernels step for step. Where they cannot, the runtime rebuilds the BF16 weight and calls MLX, which is exact by construction.

[DESIGN.md](DESIGN.md) has the formats, the runtime layout and the exactness argument.

## Install

Python 3.11 or newer on Apple Silicon (or Linux with CUDA 12). Exactness depends on MLX's own kernels, so MLX and mlx-lm are pinned (0.32.2 and 0.31.3).

```
pip install binade               # Apple Silicon
pip install "binade[cuda]"       # Linux + CUDA 12
pip install "binade[torch]"      # adds PyTorch, for binade.torch.load
```

To run the tests or reproduce the results, install from a clone with the extras (`requirements.lock` has the exact versions the results used):

```
git clone https://github.com/GuyShafir/binade && cd binade
pip install -e ".[dev,eval,figures]"                  # add cuda on Linux: ".[dev,eval,figures,cuda]"
```

## Use

Load a published Binade model straight from the Hugging Face Hub: the [Binade](https://huggingface.co/Binade) organization has Gemma 4 E2B, E4B, 12B, 26B-A4B and 31B, Qwen3.5 4B and 9B, and Llama 3.1 8B and 3.2 3B Instruct. Or pack one yourself from the Hugging Face cache or a local directory:

```
hf download google/gemma-4-12B-it
binade pack google/gemma-4-12B-it --out models/gemma-4-12B-it-binade
```

Run it with mlx-lm:

```python
from mlx_lm import generate
from binade.mlx.r4 import load

model, tokenizer, _ = load("Binade/gemma-4-12B-it")      # or a local packed directory
messages = [{"role": "user", "content": "Why is the sky blue?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
print(generate(model, tokenizer, prompt, max_tokens=200))
```

`binade unpack <packed-dir or Hub repo id> --out DIR` rebuilds the original BF16 checkpoint, bit for bit.

### In PyTorch: the pack as the original weights

```python
from binade.torch import load            # pip install "binade[torch]"

model, tokenizer = load("Binade/Llama-3.1-8B-Instruct", device="cuda")   # the stock transformers model, in BF16
```

The pack is decoded at load into the tensors the source checkpoint held, bit for bit, and given to the checkpoint's own transformers class. Everything computed afterwards is PyTorch's own arithmetic on the original weights, so the outputs are the original model's in PyTorch. This saves the download and the disk (a third of BF16), not GPU memory: the loaded model is BF16. Computing from the compressed layout, which is what saves memory, is the MLX runtime above; why that runtime is not in PyTorch yet is measured in [results/cuda/torch_order.md](results/cuda/torch_order.md). `binade.torch.state_dict(path)` gives the tensors without transformers. Checked against `from_pretrained` on the source checkpoint ([torch_load](results/torch_load.md)): every tensor identical and the same greedy generation on Llama 3.2 3B, Llama 3.1 8B, Gemma 4 E2B and Qwen3.5 4B.

Or serve it over mlx-lm's OpenAI-compatible HTTP API, for any chat client:

```
binade serve --model Binade/gemma-4-12B-it --port 8080
```

`binade serve` takes every `mlx_lm.server` option; a stock (unpacked) model name loads as mlx-lm would, so one server can switch between the two.

### Faster on a Mac: the pack verifies a draft of itself

Speculative decoding needs a fast draft model with the same tokenizer. The pack supplies one from its own weights, quantized to 4-bit at load, so nothing else is downloaded; the exact model then checks the draft's tokens a few at a time in one pass over its weights. Greedy output is the exact model's output; the draft only sets the pace.

```python
from binade.mlx.draft import load
from mlx_lm import generate

model, draft, tokenizer = load("Binade/gemma-4-12B-it")
print(generate(model, tokenizer, prompt, max_tokens=200, draft_model=draft, num_draft_tokens=4))
```

```
binade serve --model Binade/gemma-4-12B-it --draft-model self --num-draft-tokens 4
```

Up to four draft tokens keep every verify pass on the wide kernel (`results/*/self_draft.md`). Resident memory grows by about 4.5 bits per weight for the draft, still below BF16's 16. mlx-lm's speculative loop needs a trimmable cache, so models with linear-attention layers (Qwen3.5's `ArraysCache`) decode without a draft; MoE experts are not drafted yet.

## Verify and reproduce

- `scripts/roundtrip_test.py`: every tensor of a packed model against the original, bit for bit.
- `scripts/generate_check.py`: greedy decoding against the BF16 model (`--reference streamed` for models that do not fit).
- `scripts/exactness_scale.py`: logits at 16,352 positions and 32 generations against BF16 (resident or streamed), optionally with the fused kernels forced.
- `scripts/decode_speed.py`, `scripts/torch_bench.py` (PyTorch BF16 and DFloat11 on the same prompt), `scripts/self_draft_bench.py`, `scripts/matvec_bench.py`, `scripts/prefill_bench.py`, `scripts/prompt_speed.py`, `scripts/cuda_gemm_bench.py`: speed.
- `scripts/cuda_exact_finite.py`: the CUDA runtime against MLX's BF16 product on data where every output shows the order of the sum; `scripts/torch_order_*.py`, `scripts/linear_chain_time.py`: which order PyTorch's BF16 linear layer sums in and how fast ([results/cuda/torch_order.md](results/cuda/torch_order.md)).
- `scripts/torch_load_bench.py`: `binade.torch.load` against `from_pretrained` on the source checkpoint (tensors, generation, load time).
- `scripts/fit_probe.py`: which variants load on a GPU; `scripts/reference_check.py`: MLX against the reference implementation.
- `scripts/histogram.py`, `scripts/mutual_info.py`, `scripts/iid_model.py`, `scripts/entropy_floor.py`, `scripts/compare.py`, `scripts/exponent_patch.py`: the exponent statistics and how far the file sits from the entropy floor.
- `pytest`: unit and kernel tests, including order-sensitive data that exposes any change in summation order.

Result files record the commit of the development repository that produced them; that history is not published. Early result files use the project's working name, `xp`.

## Limitations

- **Tied to MLX's internals.** Exactness relies on MLX 0.32.2's kernels and dispatch rules. A different MLX version or GPU generation can change the summation order, and the tests would catch it. The fused GEMM is enabled only on M3 and M4 GPUs.
- **Validated models.** Gemma 4 12B, E2B, E4B and 26B-A4B, Llama 3.1 8B, Llama 3.2 3B, Qwen3.5 4B and 9B: bit-identical to BF16 at every one of 16,352 WikiText-2 positions per model, and in greedy generation (`results/*/exactness_scale.md`). Gemma 4 31B the same on NVIDIA (`results/cuda/gemma-4-31B-it/exactness_scale.md`).
- **Vision and audio.** Their weights are packed in the file (and restored by `binade unpack`), but the runtime loads the text model through mlx-lm, so it serves text.
- **Prompt processing.** Prefill at 32 to 128 prompt rows runs at 0.77 to 0.90x BF16. On long prompts, a model without memory headroom for rebuilding weights runs the fused GEMM at 0.75x the speed of MLX's.
- **Quantization is faster.** Lossy 8-bit quantization is faster and smaller; Binade's case is exactness.
- **Speculative decoding and ties.** With a draft, the exact model checks several tokens in one multi-row pass, and MLX sums a multi-row product in a different order than a single-row one. Both are exact BF16 arithmetic, but a near-tie between two tokens can resolve differently, so speculative greedy output can differ from sequential greedy output at a few positions. The pack behaves exactly as BF16 does in both modes: `results/*/self_draft.md` compares the pack against BF16 with the same draft, token for token, and reports speculative against sequential separately.
- **CUDA.** Decoding runs at 1.01 to 1.20x BF16 (the MoE model, bound by the CPU, at 1.01x); prompts take longer (1.3x BF16's time to the first token after 40 tokens on the RTX PRO 6000). The fused prompt kernels cover dense products up to 128 rows and every expert product, on the RTX PRO 6000, L4 and A100; longer dense prompts, and dense prompts on other GPUs, rebuild BF16 weights for cuBLAS. The runtime is MLX's CUDA backend, not PyTorch: PyTorch's BF16 linear layer sums in a different order ([pytorch](results/cuda/pytorch.md)), so a PyTorch runtime needs its own exact path.
- **CUDA: no speculative decoding yet.** MLX's CUDA backend pays a setup cost on a multi-row pass each time the cache length is new, so the self-draft loses to sequential decoding there (0.76x BF16 in fresh processes, [self_draft](results/cuda/Llama-3.1-8B-Instruct/self_draft.md)); it is a Mac feature for now. Greedy decoding on that backend is also not reproducible run to run, for BF16 as for the pack, so exactness there is checked on logits for the same inputs (`scripts/exactness_scale.py`).

## Related work

Binade codes the same exponent redundancy as:
- DFloat11 (Huffman, arXiv 2504.11651; measured side by side in [results/cuda/pytorch.md](results/cuda/pytorch.md));
- ZipServ (fixed-width exponent windows fused into GEMM, arXiv 2603.17435);
- Unweight (per-tensor palettes, Cloudflare);
- ENEC (frequency ranks, arXiv 2604.03298);
- NeuZip (arXiv 2410.20650) and ZipNN (arXiv 2411.05239).

We found no public implementation of lossless compressed inference on Metal.

## Paper

[paper/binade.pdf](paper/binade.pdf): the exponent statistics behind the format, the exactness argument, and the evaluation on Apple Silicon and NVIDIA GPUs. The LaTeX source is in `paper/latex`; `paper/latex/make_assets.py` generates its tables and figures from `results/`.

## License

Apache-2.0 ([LICENSE](LICENSE)). Model weights keep their own licenses.
