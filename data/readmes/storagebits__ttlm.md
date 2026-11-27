<p align="center"><img src="docs/img/moth.png" width="96" alt="TTLM moth"></p>

<h1 align="center">TTLM</h1>

<p align="center"><b>Transistor-Transistor Language Model</b><br>
A tiny transformer that runs on a computer with no CPU.</p>

<p align="center"><img src="docs/img/ttlm-demo.gif" width="640" alt="Chatting with the moth on a Gigatron"><br>
<sub>A full conversation, sped up 4×. The top of the screen is the model itself.</sub></p>

<p align="center"><b><a href="https://storagebits.github.io/ttlm/">▶ Talk to the moth in your browser</a></b><br>
<sub>A cycle-accurate Gigatron, emulated in the page, running the same program at the same speed.</sub></p>

---

The [Gigatron TTL](https://gigatron.io/) is an 8-bit computer built from about
30 ordinary 7400-series logic chips: adders, registers, multiplexers. There is
no microprocessor on the board. It runs at 6.25 MHz, has 32 KB of RAM, and
draws its 160×120 VGA picture in software, one pixel at a time.

TTLM puts a language model on it. It's not a lookup table or a chatbot script: it's a
real decoder-only transformer, with attention, a KV cache and an MLP, trained like any other
language model, then squeezed until it fits next to the screen in 32 KB and needs no multiplier.

You type a question. The Gigatron thinks for a while, then answers one word at a time.

## Meet the moth

On 9 September 1947, operators of the Harvard Mark II found a moth stuck in a
relay and taped it into the logbook: *"First actual case of bug being found."*

TTLM's model is that moth. It now lives inside the Gigatron. It loves the glow
of the screen and the warmth of the chips, it eats dust, and it knows nothing
else, which is about right for 22,000 parameters.

```
> hi moth
  hello. i see your light.
> where is the cpu
  there is no cpu here. the chips do the work.
> are you an ai
  i do not think much. i have no cpu.
> what is money
  i do not know. i only know light.
> do you like the dark
  oh no. please keep the screen on.
> can you code
  no. i only know light. but i can fly.
> good night moth
  i sleep in the day. the night is for the light.
```

The first language model without a CPU is, quite literally, a bug.

## The model

| | |
|---|---|
| Architecture | decoder-only transformer (GPT-style), causal self-attention |
| Layers | 2 |
| Width | 32 (2 heads of 16) |
| MLP | 64, ReLU |
| Vocabulary | 155 words (word-level, unknown words become `<unk>`) |
| Context | 20 tokens |
| Parameters | 21,984, all ternary |
| Weights | ternary: −1, 0 or +1 ([BitNet b1.58](https://arxiv.org/abs/2402.17764) style), 63 % zeros |
| Activations | 8-bit integers (queries and keys: 6-bit) |
| Arithmetic | integers only: additions, shifts, table lookups |
| Size on the Gigatron | 9 KB of weights, 2.5 KB of KV cache |

It was trained on 40,000 synthetic dialogues generated from templates (like
[GuppyLM](https://github.com/arman-bd/guppylm), whose goldfish inspired this
project), on a laptop, in about five minutes.

## How it works

### No multiplications

A transformer is mostly matrix-vector products. With weights restricted to
−1, 0 and +1, a product collapses into additions and subtractions of the
inputs. TTLM stores each matrix row as a list of the inputs to add or
subtract, so the Gigatron never multiplies anything in the linear layers.
63 % of the weights are zero and cost nothing at all.

The inner loop is ten lines of hand-written vCPU assembly. Before each product
the inputs are written to a single 256-byte memory page, `x` at offset 0 and
`−x` at offset 128. A stored index byte is then directly the address of the
value to add, sign included: one load and one add per non-zero weight, no
branches.

### Integer-only everything else

The parts of a transformer that usually need floating point are replaced by
integer equivalents that the model is trained with from the start:

- **Normalization**: instead of LayerNorm, each vector is scaled by a power of two so
  that its mean absolute value lands in a fixed range. That's a single shift.
- **Scales**: every matrix has one power-of-two output scale, so rescaling is
  a shift too.
- **Softmax**: a 32-entry table of `2^(−z/4)` and a table of reciprocals turn
  attention scores into weights that sum to about 64. No division.
- **Attention products**: query·key and weight·value need real multiplications. They use
  quarter squares, `a·b = ⌊(a+b)²/4⌋ − ⌊(a−b)²/4⌋`, with a 128-entry table.
  Queries and keys are kept to 6 bits so the sums fit in 16 bits.

### One model, three implementations, zero differences

The model is defined once, in PyTorch, as integer arithmetic: every rounding
is explicit and trained through with straight-through estimators. The same
computation then exists as:

1. the PyTorch training model (`model/qmodel.py`),
2. a plain-Python integer reference, token by token with a KV cache (`model/ref.py`),
3. the C and vCPU assembly that runs on the Gigatron (`gigatron/src`).

All three produce **bit-identical logits**. `make test` checks the C version
running on a Gigatron simulator against the Python reference.

### A coin for close calls

The Gigatron and the Python reference compute the same logits, bit for bit. To pick the
next word, the reference always takes the best one. The Gigatron does too, except when
the two best words are nearly tied: then it flips a coin, using the ROM's entropy byte,
which is stirred every frame. So the moth does not always give the same answer.

### The model is on the screen

<p align="center"><img src="docs/img/answer.png" width="400" alt="Screen layout"> <img src="docs/img/thinking.png" width="400" alt="Thinking"></p>

The Gigatron has no separate video memory: the picture is drawn directly from
RAM. With the screen taking 19 KB of the 32 KB, there is nowhere else to put
the model. So the top 60 % of the screen *is* the model: weights, embeddings
and KV cache, shown as colored pixels. The thin line just above the title holds
the activations, and you can see it flicker while the moth thinks.

<p align="center"><img src="docs/img/xray.png" width="800" alt="The Gigatron screen next to its X-ray: what each pixel holds"></p>

The X-ray above shows what each pixel holds. The word embeddings and the program code
are not visible: they are tucked into the 96 bytes past the end of each line, which the
video never draws. The browser version shows this X-ray live under *Advanced view*.

While thinking, the Gigatron switches to a video mode that only draws one
scanline in four (right picture above). Generating the picture is the
Gigatron's main job, and every skipped line is CPU time handed back to the
model, about ten times more of it.

### Speed

Measured in a cycle-accurate emulation of the Gigatron:

| | |
|---|---|
| Reading the question | ~1.3 s per word |
| Writing the answer | ~2 s per word |
| A typical exchange | 25 to 35 s |

That's around 0.5 tokens per second, on 1970s logic at 6.25 MHz.

## Run it

### On a real Gigatron

You need a Gigatron with 32 KB and ROM v4 (`gigatron/ttlm.gt1`). For ROM v3,
use the experimental `gigatron/ttlm_v3.gt1`.

Programs are sent through the game controller port with an Arduino running
[BabelFish](https://github.com/kervinck/gigatron-rom/tree/master/Utils/BabelFish):

| Arduino Uno / Nano | Gigatron controller port (DB9) |
|---|---|
| D13 | pin 2 (data) |
| D12 | pin 3 (latch) |
| D11 | pin 4 (pulse) |
| GND | ground |

Select **Loader** in the Gigatron menu, then:

```sh
python3 gigatron-rom/Utils/sendFile.py gigatron/ttlm.gt1
```

Type with a PS/2 keyboard (Pluggy adapter), or send keystrokes from your
computer through BabelFish. If nobody types for 30 seconds, the moth starts a
conversation with itself.

### In your browser

**[storagebits.github.io/ttlm](https://storagebits.github.io/ttlm/)** boots an emulated
Gigatron straight into TTLM. Type a question or pick one, and watch it think. While the moth
thinks it runs faster than the real machine; tick *Real speed* for the authentic wait. The page lives
in `web/` (built with `make web`); its simulator core is
[Philip Thomas' Gigatron simulator](https://github.com/kervinck/gigatron-rom/tree/master/Contrib/PhilThomas) (BSD 2-clause).

### In an emulator

Any Gigatron emulator that loads `.gt1` files will do. The repository also
includes `tools/gtshot`, a small headless cycle-accurate Gigatron that can
type and take screenshots:

```sh
make tools/gtshot
tools/gtshot v4.rom gigatron/ttlm.gt1 w2 "thi moth|" w30 vshot.ppm
```

## Build from source

Requirements: Python 3.10+, [uv](https://github.com/astral-sh/uv) (or pip),
a C compiler, GNU make, and [glcc](https://github.com/lb3361/gigatron-lcc),
the C compiler for the Gigatron, installed into `third_party/glcc-install`.

```sh
git clone https://github.com/lb3361/gigatron-lcc third_party/gigatron-lcc
(cd third_party/gigatron-lcc && gmake PREFIX=$PWD/../glcc-install install)

uv venv && uv pip install torch numpy pyserial

cd model
python data.py                                   # look at the vocabulary and samples
python qtrain.py --soft --seed 1 --out s.pt      # train without rounding
python qtrain.py --init s.pt --seed 1 --lr 1e-3 --steps 5000 --out moth.pt
python ref.py moth.pt                            # integer reference: quality and exactness
cd ..

make            # gigatron/ttlm.gt1 and gigatron/ttlm_v3.gt1
make test       # C on the Gigatron simulator vs the Python reference: BIT-EXACT
```

## Repository

```
model/          training data, integer-exact model, reference, C exporter
  data.py         the moth's dialogues and vocabulary
  qmodel.py       the integer transformer (PyTorch, straight-through estimators)
  ref.py          pure-Python integer inference, the specification
  export_c.py     weights -> C arrays laid out for the Gigatron's memory
gigatron/src/   the program
  engine.c        inference: embeddings, norms, attention, MLP, output head
  row.s           the ternary dot product, in vCPU assembly
  ttlm.c          chat interface, tokenizer, demo mode
web/            the browser version (GitHub Pages)
tools/          gtshot (headless Gigatron), screen X-ray, GT1 post-processing, icon
```

## Limitations

- The moth knows about 150 words and one subject. Everything else becomes `<unk>`,
  and it will tell you it only knows light.
- One question at a time: there is no memory between exchanges.
- Questions are cut at 7 words, and the question plus the answer must fit in 20 tokens.
- It is slow. That is part of the point.

## Credits

- The [Gigatron TTL](https://gigatron.io/) by Marcel van Kervinck and Walter Belgers.
  `tools/gtshot.c` is built on the reference emulator from
  [gigatron-rom](https://github.com/kervinck/gigatron-rom) (BSD 2-clause).
- [glcc](https://github.com/lb3361/gigatron-lcc), the Gigatron C compiler, by lb3361.
- The browser simulator by Philip Thomas (BSD 2-clause), in `web/emu`.
- [GuppyLM](https://github.com/arman-bd/guppylm) for the idea of a tiny model with a tiny world.
- [BitNet b1.58](https://arxiv.org/abs/2402.17764) for ternary weights.
- The moth, Harvard Mark II, 1947.

## License

MIT, see [LICENSE](LICENSE). By [storagebits](https://github.com/storagebits).
