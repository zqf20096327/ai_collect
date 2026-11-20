# Akeratos

Pretrain a small language model from scratch on your Mac, with [MLX](https://github.com/ml-explore/mlx). On one M4 Max a first model trains in 41 minutes and 6.7 GiB of memory. Billet, a 162M-parameter model with a table of 6.0 billion numbers, trained for four and a half days on that Mac.

Cogvera Labs built Akeratos to test one idea: a very large learned [n-gram table](https://github.com/cogvera-labs/akeratos/blob/main/docs/learn/n-gram-memory.md), held in the Mac's unified memory beside a small transformer. A Mac has modest compute and plenty of memory, and the table costs memory more than compute. Against the same model without it, the table lowers held-out bits per byte from 0.9030 to 0.8866, one seed each, at nearly twice the training memory: [the result](https://github.com/cogvera-labs/akeratos#the-result).

```sh
git clone https://github.com/cogvera-labs/akeratos && cd akeratos
uv sync
uv run bake bench
```

You need an Apple silicon Mac on macOS 14 or later, and [uv](https://docs.astral.sh/uv/) 0.13.6 or newer. `bake bench` trains a 10M model twice on synthetic tokens, table off and table on, and prints what the table costs per step on your Mac. On the same M4 Max (48 GB) it took 74 seconds and peaked at 6.2 GiB of memory. [Smaller Macs are untested](https://github.com/cogvera-labs/akeratos/blob/main/docs/reproduce.md#your-mac): [send your Mac's row](https://github.com/cogvera-labs/akeratos/blob/main/docs/speedrun.md#bake-bench).

## What you can do

- **Train a first model in 41 minutes.** After a 285 MB download, `bake train starter` pretrains a 10M model with a table of 1.0 billion numbers on 75M tokens, through the same trainer as Billet: [a first run](https://github.com/cogvera-labs/akeratos/blob/main/docs/reproduce.md#a-first-run).
- **Enter the five-minute speedrun.** `bake speedrun` trains the model in [`speedrun/train.py`](https://github.com/cogvera-labs/akeratos/blob/main/speedrun/train.py) for 300 seconds of step time and scores it on held-out text. Change the file, beat the record, send your runs by pull request: [the Mac speedrun](https://github.com/cogvera-labs/akeratos/blob/main/docs/speedrun.md).
- **Rerun Billet in four and a half days.** `bake train billet` trains the 162M model in 24.1 GiB of memory, and `bake evaluate` scores it. Its twin takes as long again: [Reproduce](https://github.com/cogvera-labs/akeratos/blob/main/docs/reproduce.md).
- **Use Billet's weights with no training.** `bake generate` continues a prompt with [the released weights](https://huggingface.co/Cogvera-Labs/Akeratos-Billet): a 14.4 GB download, 13.0 GiB of memory. `The capital of France is` gives, greedily, ` Paris. It is the largest city in France and the second largest in Europe.` The 41-minute starter gives ` the capital of the world.` Billet is a base model: fluent, and often wrong.
- **Score the released weights in 36 minutes.** With no training and no data build, `bake evaluate` gives both published scores; the twin's takes 18 minutes: [Score](https://github.com/cogvera-labs/akeratos/blob/main/docs/reproduce.md#4-score).

Akeratos's models run in its own code, not in mlx-lm or llama.cpp. To fine-tune or chat with an existing model, start with [the options on a Mac](https://github.com/cogvera-labs/akeratos/blob/main/docs/mac-options.md).

## The result

Billet is a 162M-parameter transformer (275M with its value embeddings) with a table of 6.0 billion trained numbers: one vector for each hashed bigram and trigram, added to the residual stream before every block. Its twin is the same model without the table, trained on the same 3.2 billion tokens in the same order.

| On 7,314 held-out documents of FineWeb-Edu | Bits per byte, lower is better |
|---|---|
| Billet | 0.8866 |
| Its twin | 0.9030 |
| Billet minus its twin | **−0.0164 bits per byte** (95% interval −0.0172 to −0.0157) |

By the rule fixed before the twin finished, the table helps. Each model was trained once, on one MacBook Pro (M4 Max, 48 GB): the interval resamples held-out documents, not seeds. The two are not matched for parameters or memory: Billet's run peaked at 24.1 GiB against its twin's 12.4, and a training step takes 5.2% longer with the table on. On the 2,456 held-out documents that share no 13-gram with the training data, the difference is −0.0079 bits per byte.

![Training loss of Billet and its twin, step by step](https://github.com/cogvera-labs/akeratos/raw/main/results/billet/training-loss.svg)

The curves nearly coincide at this scale: Billet runs 0.04 to 0.06 nats below its twin. Both bend at step 19,532, where the learning rate starts to fall.

[The result page](https://github.com/cogvera-labs/akeratos/blob/main/docs/billet.md) has every readout and what one seed cannot say. [The analysis plan](https://github.com/cogvera-labs/akeratos/blob/main/docs/analysis-plan.md) is the rule as posted. [`results/billet/`](https://github.com/cogvera-labs/akeratos/tree/main/results/billet) holds the report this number is read from. The weights are on Hugging Face: [Billet](https://huggingface.co/Cogvera-Labs/Akeratos-Billet) and [its twin](https://huggingface.co/Cogvera-Labs/Akeratos-Billet-Twin).

Hashed n-gram tables are not new. [Engram](https://arxiv.org/abs/2601.07372) and the [Over-Tokenized Transformer](https://arxiv.org/abs/2501.16975) hash n-grams into embedding tables, and [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) ships 196B parameters of Engram memory. The [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) speedrun added a hashed bigram table in its record 62. [The n-gram memory](https://github.com/cogvera-labs/akeratos/blob/main/docs/learn/n-gram-memory.md) names the rest of the work this builds on.

## Read the code

- [`akeratos/model.py`](https://github.com/cogvera-labs/akeratos/blob/main/akeratos/model.py): the forward pass.
- [`akeratos/table/table.py`](https://github.com/cogvera-labs/akeratos/blob/main/akeratos/table/table.py): the table and its sparse update.
- [`speedrun/train.py`](https://github.com/cogvera-labs/akeratos/blob/main/speedrun/train.py): the whole 10M model, its optimiser and schedule, in one file.

Billet was trained with the banded attention code, and `bake train` still uses it. `bake bench` and the speedrun use the fused Metal kernels where they fit ([the code map](https://github.com/cogvera-labs/akeratos/blob/main/docs/architecture.md)).

## Open problems

[OPEN_PROBLEMS.md](https://github.com/cogvera-labs/akeratos/blob/main/OPEN_PROBLEMS.md) lists what Cogvera Labs cannot answer alone. Each question names its baseline and what counts as an answer; a negative result is an answer. [CONTRIBUTING.md](https://github.com/cogvera-labs/akeratos/blob/main/CONTRIBUTING.md) says how to send a result, a claim or a fix.

## How it is made

AI coding agents (Claude) write most of the code; Cogvera Labs reviews and merges. Development happens in a private repository where the agents' checks run; this one is exported from it, one commit per change.

Thomas Nicklin ([@BhodiSea](https://github.com/BhodiSea)) maintains Akeratos at Cogvera Labs. The licence is Apache-2.0.
