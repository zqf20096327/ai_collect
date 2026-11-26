# micro-qwen3 on ESP32-S3

A language model with **1,056,656 parameters** that writes short stories on an ESP32-S3 microcontroller, offline, at about **72 tokens per second**. Name up to three words, for example *dragon, cookie, school*, and the board writes a story that uses all of them.

The model follows the Qwen3 architecture block by block and is trained from scratch on [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories). Its weights take **0.68 MB** (676,934 bytes) in a 4-bit format designed for the chip. Inference is a single dependency-free C file, and the same file runs on a computer for testing.

To watch the same model work step by step in your browser, open [TensorLupa](https://tensorlupa.com). You can see the words it weighs, where its attention looks, and what flows through each layer.

> Not affiliated with Qwen or Alibaba Cloud. "Qwen3" refers to the architecture. The weights, the 4096-token vocabulary and the sizes are our own.

## What is in this repository

| Folder | Contents |
|---|---|
| `firmware/` | ESP-IDF project: the inference engine (`microqwen.c`, `microqwen.h`), the web demo (`main/`), the partition table |
| `host/` | The same engine built for macOS or Linux, to run the model without a board |
| `models/` | The demo model in W4R format, its tokenizer and a reference output for the parity check |
| `parity/` | Checks that the C engine gives the same tokens and logits as the reference in MLX |
| `training/` | The model and training code (MLX), data preparation, export to W4R, the two training recipes, and a Colab notebook that repeats the whole chain in PyTorch |
| `logs/` | Training and evaluation logs of the two runs behind the demo model |

## Flash a board

You need an ESP32-S3 module with 16 MB flash and 8 MB PSRAM (N16R8).

**From the browser.** Open [tensorlupa.com/flash](https://tensorlupa.com/flash) in Chrome or Edge on a computer, plug the board in and press one button. The page walks you through every step.

**From a terminal, without ESP-IDF.** Download `micro-qwen3-esp32s3-v1.2.1.bin` from the [latest release](../../releases/latest): it holds the bootloader, the partition table, the firmware and the model in one file.

```bash
pip install esptool
esptool.py --chip esp32s3 --port PORT write_flash 0x0 micro-qwen3-esp32s3-v1.2.1.bin
```

**From source,** with ESP-IDF 5.3:

```bash
cd firmware
idf.py set-target esp32s3
idf.py -p PORT flash
# the model goes into its own partition
esptool.py --port PORT --chip esp32s3 --after no_reset write_flash 0x210000 ../models/tsim900-sft-x-w4r.bin
```

**Using it.** The board starts its own Wi-Fi network **micro-qwen3** (password `microqwen`). Join it and open http://192.168.4.1. The network name and password are `AP_SSID` and `AP_PASS` at the top of `firmware/main/main.c`. The page prints the story as it is written, in small batches every 50 ms, and shows the speed. Type up to three words, or tap one of the seven tested orders. You can set the temperature, top-k, the length and the seed: the same seed writes the same story again, and the page shows the seed of every story. Two devices can join at once: one story is written while the next one waits.

The serial console works too: type the start of a story, or `/words cat moon cake` to order one; `/seed 33` before it fixes the seed of the next story.

The model runs on core 1, while Wi-Fi and the web server run on core 0.

## Run it on a computer

```bash
make -C host
./host/microqwen models/tsim900-sft-x-w4r.bin gen "Once upon a time" 200 0.6 40
```

A story order with the board's own loop (the word bonus, the spelling automaton, the loop penalty), for one seed or a range of seeds:

```bash
make -C host order
./host/order models/tsim900-sft-x-w4r.bin "dragon, cookie, school" 33
./host/order models/tsim900-sft-x-w4r.bin "dragon, cookie, school" 1..200    # one line per seed
```

Since v1.2 a seed found on a computer writes the same story on the board, letter for letter: 30 of 30 random orders matched. In v1.1 only 3 of 7 did, because the chip and a computer computed the exponent with different C library code and the chip's compiler fused multiplications with additions. Now the engine has its own exponent made of plain + and ×, and both builds use `-ffp-contract=off`. The seven orders on the board's page were found with `host/order` on a computer, read, and checked on a real ESP32-S3.

## Parity check

The C engine works in integers on the board: 4-bit weights and 8-bit activations. The reference is the same quantized model simulated in MLX in floating point.

```bash
uv sync
uv run parity/check_c.py --bin models/tsim900-sft-x-w4r.bin --tokenizer models/tsim900-sft-x.tokenizer.json --exe host/microqwen
```

Current result for the demo model:

| Check | Result |
|---|---|
| Tokenizer | the same tokens as Hugging Face `tokenizers` on all 9 test strings |
| Logits at the last prompt position | largest difference 0.24, at a logit scale of about 14 |
| Top-1 and top-5 next tokens | the same |
| Greedy generation | the same first 49 of 60 tokens |

The greedy runs part where two tokens are almost equally likely and the small integer difference tips the choice.

## The model

| | Qwen3-0.6B | micro-qwen3 |
|---|---|---|
| Block | RMSNorm (pre-norm), GQA, QK-norm, RoPE, SwiGLU, no bias, tied embeddings | the same |
| Layers × hidden size | 28 × 1024 | **3 × 112** |
| MLP | 3072 | 336 |
| Attention | 16 heads × 128, 8 KV heads | 4 heads × 64, 2 KV heads |
| Vocabulary | 151,936 | 4096, byte-level BPE with the Qwen pre-tokenizer |
| Context | 32K | 256 |
| Parameters | about 596M | 1.057M |

At this size the model knows grammar, punctuation and the shape of a children's story. It does not know facts about the world, which do not fit into a million parameters.

## How the architecture was chosen

Every size and setting above came from a grid of short training runs. This repository keeps only the winner, with its full recipe and logs. Below are the summaries of the grids.

**How the grids were run:**
- Quality is bits per byte (bpb) on held-out text. Unlike perplexity, it stays comparable across tokenizers.
- Each variant was trained once, so differences under about 0.01 bpb count as ties.
- The shape grids used 500 MB of FineWeb-Edu; the data and precision grids used TinyStories.

**Vocabulary** (about 0.6M parameters):

| Tokens | 2048 | **4096** | 8192 |
|---|---|---|---|
| val bpb | 1.747 | **1.710** | 1.785 |

A smaller vocabulary means tiny tokens. A larger one lets the embeddings eat the budget of the layers.

**Depth against width** (fixed budget of about 0.6M parameters):

| Layers × width | 2 × 96 | **3 × 88** | 4 × 80 | 7 × 64 | 15 × 48 | 28 × 32 (Qwen proportions) |
|---|---|---|---|---|---|---|
| val bpb | 1.774 | **1.694** | 1.701 | 1.710 | 1.744 | stopped, 0.15 behind |
| Training speed, tokens/s | 336K | 273K | 234K | 187K | 103K | about 70K |

Three or four layers are best, with a cliff at two. A faithful 28-layer miniature of Qwen3 was the worst: Qwen's layer count does not scale down a thousand times, but its width-to-depth ratio does.

**Attention.** Quality follows the product "heads × head size", while time follows the number of heads. Four heads of 64 gave the best quality per second.

**The final shape** (about 1M parameters, attention 4 × 64):

| Shape | val bpb | Training speed |
|---|---|---|
| **3 × 112** | **1.612** | **261K tokens/s** |
| 4 × 96 | 1.614 | 237K tokens/s |

A tie in quality, and three layers are 9% faster.

**Context.** 512 tokens instead of 256 gave only 0.8% better bpb at 29% lower speed. The model barely uses distant context, so the demo uses 256.

**Data.** The demo uses TinyStories V2 (stories written by GPT-4). A run of the same model on the first version of TinyStories did not beat it on V2 stories (0.769 against 0.669 bpb).

**Precision.** Is a larger model with fewer bits per weight better at the same memory on the board? At about 770 KiB (0.8 MB), 4-bit weights win:

| Weights | Parameters | On the board | val bpb |
|---|---|---|---|
| ternary layers, 3 × 192 | 2.23M | 782 KiB | 0.697 |
| int2 layers, 3 × 192 | 2.23M | 782 KiB | 0.698 |
| **int4, 3 × 144** | 1.48M | 764 KiB | **0.643** |

Below 4 bits quality drops in a step, and int2 and ternary hit the same floor that more training data does not break. int3 recovers well with quantization-aware training, but lands on the same quality-per-byte line as int4, so it does not pay for a more complex kernel.

## How the demo model was made

Two training runs on a MacBook (M3 Pro) with MLX: [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories) V2 from scratch, then [TinyStoriesInstruct](https://huggingface.co/datasets/roneneldan/TinyStoriesInstruct) on top. The recipes are in `training/recipes/`, and the logs and evaluations are in `logs/`.

1. **Base model `ts2-base`.** Trained from scratch on TinyStories V2 (stories written by GPT-4), 500 MB of text, bf16, AdamW, learning rate 3e-3 with cosine decay.
2. **Instruction tuning `tsim900-sft-x`.** Further training on 900K dialogues from TinyStoriesInstruct converted to the Qwen chat format. The loss counts only the answer. This run trains on 600 MB of text with learning rate 1e-3, and quantization-aware training (QAT) for the 4-bit format runs from the start, so the model learns with the weights it will have on the chip.
3. **Export to W4R.** Weights become 4-bit integers with one scale per row. The scale is searched per row to minimise the error.

```bash
uv sync
uv run training/scripts/prepare_data.py --dataset tinystories-v2 --num-docs 800000 --out data/ts2-v4096-qwen
uv run training/scripts/train.py --recipe training/recipes/ts2-base.json --out runs/ts2-base
uv run training/scripts/prepare_data.py --dataset tinystories-instruct --num-docs 900000 \
    --tokenizer data/ts2-v4096-qwen/tokenizer.json --out data/tsim900-v4096-qwen
uv run training/scripts/train.py --recipe runs/ts2-base/recipe.json --data data/tsim900-v4096-qwen --init-from runs/ts2-base \
    --train-bytes 6e8 --lr 1e-3 --warmup 100 --qat int4row-clip --out runs/tsim900-sft-x
uv run training/scripts/export_esp.py --ckpt runs/tsim900-sft-x --bits 4r --clip --out models/tsim900-sft-x-w4r.bin
```

The export reproduces `models/tsim900-sft-x-w4r.bin` byte for byte from the trained checkpoint. The full-precision weights of both runs, with the 8-bit and 4-bit builds, are on Hugging Face: [olanokhin/micro-qwen3](https://huggingface.co/olanokhin/micro-qwen3).

### Train it yourself in Colab

No Mac is needed. [`training/colab/train_micro_qwen3.ipynb`](training/colab/train_micro_qwen3.ipynb) repeats the same recipe in PyTorch on a free T4 GPU: [open it in Colab](https://colab.research.google.com/github/olanokhin/micro-qwen3-esp32/blob/main/training/colab/train_micro_qwen3.ipynb), set the runtime to T4 GPU and run all cells. It downloads the two datasets, trains the tokenizer and both stages, exports the W4R file, builds the C engine and writes a story from the model it has just trained.

A run on a T4, next to the runs behind the published weights:

| | Colab, T4, PyTorch | MacBook, M3 Pro, MLX |
|---|---|---|
| Base model, bits per byte on held-out stories | 0.667 | 0.669 |
| After instruction tuning, full-precision weights | 0.706 | 0.706 |
| After instruction tuning, 4-bit weights | 0.721 | 0.721 |
| Training time, base model | 7.1 min | 8.5 min |
| Training time, instruction tuning | 10.2 min | 11 min |

The tokenizer trained in Colab is the same file, byte for byte, as `models/tsim900-sft-x.tokenizer.json`. The weights are not: the two frameworks draw different random numbers, so this is the same recipe and the same quality, not the same model. The whole notebook, from an empty runtime to the story from the C engine, ran in 35 minutes: downloading and tokenizing the data takes about as long as the training itself.

At the end it packs the files you ask for (`EXPORT`): full-precision weights of both stages, an 8-bit `.bin` and a 4-bit `.bin`. The 8-bit file opens in the [TensorLupa](https://tensorlupa.com/studio) studio (model menu, Load from computer), the 4-bit one opens there too and runs on the board. Not going to use a board? Set `QAT = False` and skip the 4-bit file.

Every setting is in plain view: the amount of data, the model shape, the learning rates. Keep them to get a model like the published one, or change them and compare. `QUICK = True` in the first code cell runs the whole chain on a small slice in a few minutes. The notebook is built from `training/colab/train_micro_qwen3.py`, which also runs as a plain script.

### Stories with requested words

With instruction tuning alone, only 64% of the requested words make it into the story. The model "wants" the words: their logits are high at every step, but rarely high enough to win. A small decoding rule closes the gap:

```
bias = base · (u + 1) · (1 + t / τ)        base 2, τ 100, temperature 0.6
  u: how many requested words are already in the text (each found word raises the pressure on the rest)
  t: tokens since the last requested word appeared (the longer it waits, the stronger the push)
```

With this rule, all three words appeared in every one of the 200 test orders it was tuned on, and in 298 of 300 stories from orders the model had never seen, with the board's settings. A small spelling automaton (FSM) finishes multi-token words correctly once they start, and only allows the endings English spelling allows (daring, stopped, invitations). The same rules run on the board.

Sampling uses top-k 40 and **min-p 0.02**: a token 50 or more times less likely than the favourite is never drawn. Such rare draws are how invented words begin. With the board's settings (4-bit weights, a simple repetition penalty), the cut lowers the share of stories with an invented word from 4.0% to 0.7% of 300 stories on orders the model had never seen; looping stories go from 4% to 6%. The board keeps the simple penalty because it needs no table; the [TensorLupa](https://tensorlupa.com) studio uses one that knows which repeats are natural in children's stories.

## How the 4-bit weights were made

W4R is not plain int4. The goal was 4-bit weights that behave as close as possible to 8-bit ones.

**Result for the demo model.** Measured in a simulation of the device on TinyStories V2 held-out text, against the same model in full precision:

| Weights | Loss, bpb | |
|---|---|---|
| int8, one scale per row | +0.000 | lossless |
| int4, plain rounding | +0.045 | about 6% worse text by this metric |
| **W4R** | **+0.015** | about 2%: two thirds of the 4-bit loss won back |

W4R does not fully reach 8 bits, but it is much smaller (0.68 MB against 1.14 MB) and faster on the board (76 tokens per second against 54).

**Against standard QAT.** On the base model of the same line (0.669 bpb in full precision), with the same 100 MB of further training for both QAT variants:

| Variant | Loss, bpb |
|---|---|
| int4, plain rounding | +0.045 |
| int4 with the scale search, no training | +0.037 |
| standard int4 QAT | +0.029 |
| **W4R: QAT with the scale search** | **+0.022** |

The scale search inside QAT cuts the loss of standard int4 QAT by about a quarter.

**How the recipe was found.** The search ran on an earlier model of the same shape (3 × 112). The demo model inherited the result: QAT with the per-row scale search. A check on the demo model confirmed it, and also confirmed that a Hadamard rotation makes things worse once QAT is in place (+0.024 instead of +0.015).

Steps of the search, each measured on the same held-out text in a simulation of the device (weights quantized, activations int8):

| Step | val bpb | Cost against full weights |
|---|---|---|
| Full-precision weights | 0.786 | |
| int8, one scale per row | 0.786 | none |
| int4, one scale per row, plain rounding | 0.832 | +0.046 |
| + per-row scale search with clipping | 0.824 | |
| + Hadamard rotation before quantizing | 0.818 | |
| Quantization-aware training (QAT) for int4, 100 MB of text | 0.817 | |
| **QAT with the per-row scale search** | **0.809** | **+0.023**, the chosen recipe |
| Hadamard rotation baked into the weights, then QAT | 0.801 | needs an untied output layer: +458K parameters, 0.96 MB instead of 0.68 MB |
| The same rotation at an equal parameter budget | 0.808 to 0.811 | the same as without rotation |

**What the steps show:**
- **Per-row scale search.** For each row, it tries 25 clipping levels between 40% and 100% of the largest weight and keeps the one with the smallest error. Clipping a few outliers lets the other weights use the 15 levels more finely.
- **QAT.** The same search runs inside training, so the model learns weights that survive it. Together they cut the int4 loss in half.
- **Hadamard rotation.** It spreads outliers across a row and helped plain rounding. Once the scale search and QAT were in place, it gave nothing extra at the same number of parameters. Its apparent gain came from a separate output layer, which means more parameters, not a better format.
- **Weight groups.** int4 with a separate scale for every 32 weights (as in GGUF Q4) was tested on the board and ran slower than int8: leaving the integer pipeline every 32 weights costs more than the smaller weights save. One scale per row keeps the whole dot product in integers, and the scale is applied once at the end.

The demo model uses this recipe directly: instruction tuning runs with QAT and the scale search from the first step (`--qat int4row-clip`), and the export applies the same search (`--clip`).

## Speed on the chip

| Step | Tokens per second |
|---|---|
| Scalar C, int8 weights | 13.6 |
| + PIE vector instructions (16 int8 multiplies per instruction) | 43.8 |
| + int8 KV cache in internal SRAM, attention also on PIE | 54.0 |
| + W4R weights: two int4 per byte, one scale per row, unpacked in registers | 76.0 |
| + own exponent and rounding instead of the C library, each input quantized once (v1.2) | 85 |

These are decode benchmarks on short generations, 64 to 128 tokens on one core. Attention cost grows with the text, so a full story is slower: 74.0 to 78.4 tokens per second on 30 random orders over the console, 75.2 on average (v1.1: 62 to 64). Through the web page it is 72 to 73: the board sends the story in batches every 50 ms, because every Wi-Fi packet wakes core 0, and core 0 shares the memory bus with the model (one packet per token gave 67). Splitting the matrix work across both cores reached 80.7 tokens per second, but the firmware keeps core 0 for Wi-Fi and the web server.

The numbers for v1.2 include min-p and the spelling rules. Profile of a token on the board: output layer 33%, MLP 24%, attention 17%, q/k/v 12%, o 6%, the rest 7%. The output layer waits for memory: a row from internal SRAM is 2.1 times faster than one from PSRAM. A shortlist of the output layer over the top bits of the weights kept every one of 200 stories but did not pay on this chip; the details are in [How micro-qwen3 was made](https://tensorlupa.com/docs/model/how-it-was-made/).

Grouped int4 and the Hadamard rotation were also tried, see [How the 4-bit weights were made](#how-the-4-bit-weights-were-made).

## License

Apache 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). The model was trained on [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories), released under CDLA-Sharing-1.0, and on [TinyStoriesInstruct](https://huggingface.co/datasets/roneneldan/TinyStoriesInstruct) by the same authors, Eldan and Li (2023); the TinyStoriesInstruct page states no license.

Made by [Alex Anokhin](https://github.com/olanokhin).
