# swift-model — Language Models From Scratch, in Pure Swift

> A four-part, build-it-yourself course that climbs from *counting letters* all
> the way to *retrieval-augmented generation* — every idea written out in plain
> Swift, every line commented, nothing hidden behind a framework you can't read.

This repository is **a textbook you can run**. Each part is a small, complete,
heavily-commented Swift program that teaches one rung of the ladder of modern
language modelling. You read the prose, you read the code, you run it, you watch
the numbers move, and you come away understanding *how the thing actually
works* — not just how to call an API.

<p align="center">
  <img src="docs/diagrams/learning-journey.svg" alt="The learning journey: ngram → neural-char → mini-gpt → swift-rag" width="100%">
</p>

---

## Table of contents

- [Why this exists](#why-this-exists)
- [The companion book](#the-companion-book)
- [The four parts at a glance](#the-four-parts-at-a-glance)
- [Quick start](#quick-start)
- [The learning journey](#the-learning-journey)
- [What each part teaches](#what-each-part-teaches)
- [Navigation — where to read what](#navigation--where-to-read-what)
- [How the repository is laid out](#how-the-repository-is-laid-out)
- [The root scripts](#the-root-scripts)
- [Requirements & platforms](#requirements--platforms)
- [How the parts relate](#how-the-parts-relate)
- [FAQ](#faq)
- [Credits & further reading](#credits--further-reading)

---

## Why this exists

Most explanations of language models are either **hand-wavy** ("attention lets
words look at each other") or **buried in a giant framework** where the
interesting math is three call-stacks deep in C++ and CUDA. Neither lets you
actually *see* the mechanism.

This project takes the opposite approach. The same simple task — **"predict what
comes next"** — is solved four times, each time with a little more machinery, and
each time the machinery is built *in front of you*:

1. by **counting** (no learning at all),
2. by **learning weights with a hand-built autograd engine**,
3. by **a real self-attention Transformer on a production array framework**, and
4. by **grounding a real language model in your own documents** (RAG).

By the end you have seen, in code you can read in an afternoon, every core idea
behind a system like ChatGPT: tokenization, probability and sampling, gradients
and backpropagation, embeddings, attention, training loops, overfitting,
retrieval, and prompting.

> **Philosophy.** Clarity over speed, everywhere. Part 2 differentiates single
> scalars instead of tensors; Part 4 uses a 15M-parameter toy model. These are
> deliberate choices: the goal is to make the *ideas* visible, not to set
> benchmarks. Each part says plainly where it trades performance for clarity.

---

## The companion book

This repository is the **code companion to the book *How LLMs Work — From Zero to
Your Own Transformer*** by **Andrey Sapunov**. The book is the prose half of the
same climb: what a token really is, how attention works, how training works, what
RAG and agents actually do — written plain-language first, with *engineering
asides* for readers who want the formulas. It uses **Swift** for every code
example, and its chapters point straight at the parts in this repo:
[`ngram.swift`](ngram.swift) (Chapters 2 and 5), [`neural-char/`](neural-char/)
(Chapters 6–7), [`mini-gpt/`](mini-gpt/) (Parts III and V),
[`swift-rag/`](swift-rag/) (Chapter 20).

| Edition | Store | Link |
|---|---|---|
| 🇬🇧 **English** — *How LLMs Work: From Zero to Your Own Transformer* | Amazon US | [amazon.com/dp/B0H7BPJLHC](https://www.amazon.com/dp/B0H7BPJLHC) |
| 🇪🇸 **Español** — *Cómo funciona un LLM: De cero a tu propio Transformer* | Amazon US | [amazon.com/dp/B0H7C1D3NT](https://www.amazon.com/dp/B0H7C1D3NT) |
| 🇪🇸 **Español** — *Cómo funciona un LLM: De cero a tu propio Transformer* | Amazon ES | [amazon.es/dp/B0H7C1D3NT](https://www.amazon.es/dp/B0H7C1D3NT) |

You can read the book without ever cloning this repo, and you can work through
this repo without ever opening the book — but they were written to be used
together: the book explains the mechanism, the code here lets you run it, break
it, and watch what changes.

### Also by the author

- **[How Modern Voice-to-Voice AI Models Work](https://hackernoon.com/how-modern-voice-to-voice-ai-models-work)**
  (HackerNoon) — a long-read on speech-to-speech systems: cascade vs.
  speech-native architectures, neural audio codecs and RVQ, streaming and the
  real cost of the KV-cache, full-duplex conversation, and what closed realtime
  APIs do and don't disclose. A natural next step once the text-only Transformer
  in Part 3 makes sense.

---

## The four parts at a glance

| # | Part | What you build | Key ideas it introduces | Language / deps | Runs on |
|---|------|----------------|-------------------------|-----------------|---------|
| **1** | [`ngram.swift`](ngram.swift) | A counting **n-gram** model in a single script | Tokenization, the next-char *probability distribution*, sampling | Pure Swift, **0 deps**, one file | Linux · macOS |
| **2** | [`neural-char/`](neural-char/) | A **scalar autograd engine**, then a neural **bigram → MLP** | Backpropagation, softmax + cross-entropy, gradient descent, embeddings, temperature | Pure Swift, **0 deps** | Linux · macOS |
| **3** | [`mini-gpt/`](mini-gpt/) | A real char-level **GPT Transformer** | Self-attention, multi-head, causal mask, residuals, LayerNorm, AdamW, overfitting | Swift + **MLX** (Metal) | **Apple Silicon** macOS |
| **4** | [`swift-rag/`](swift-rag/) | A full **RAG** pipeline over a local corpus | Chunking, inverted index, **BM25**, prompt budgeting, local LLM inference | Pure Swift + vendored `llama2.swift` | Linux · macOS |

Each part is **independent** — its own package, its own build, no shared state —
so you can dive into any one of them. But the intended path is the climb
**1 → 2 → 3 → 4**, because each part answers a question the previous one raises.

---

## Quick start

From the repository root, one script runs any part and installs/builds whatever
that part needs the first time:

```bash
./run.sh ngram                         # Part 1 — counting n-gram on the sample text
./run.sh neural                        # Part 2 — train the autograd bigram + MLP
./run.sh gpt --steps 1500              # Part 3 — train MiniGPT (Apple Silicon)
./run.sh rag ask "what is lava?"       # Part 4 — retrieve + answer from the corpus
```

Anything after the part name is **passed straight through** to that part, so:

```bash
./run.sh ngram mytext.txt              # train Part 1 on your own UTF-8 file
./run.sh neural mytext.txt             # train Part 2 on your own file
./run.sh gpt --temperature 0.7 --prompt "MENENIUS:"
./run.sh rag search "honey bees"       # retrieval only — no model download/load
```

First time on a machine? Warm everything up (checks your Swift toolchain and
pre-builds the pure-Swift parts) with:

```bash
./setup.sh        # verify toolchain + pre-build parts 1, 2, 4
./test.sh         # quick smoke test: does every part still compile/run?
```

> `./run.sh` with no arguments prints the menu of parts. Parts are addressable by
> number too: `./run.sh 1` ≡ `./run.sh ngram`.

---

## The learning journey

The whole repository is one continuous argument, told in four moves. Read the
diagram above alongside this:

**Part 1 — `ngram.swift` — the target.**
We start with no learning at all. We just **count**: how often does each
character follow the previous *n* characters? Normalize the counts into
probabilities, sample from them, and you already get text with the right
"flavour". This shows you *what distribution a language model is trying to
produce* — and where pure counting breaks down (unseen contexts are dead ends,
and there is no way to share knowledge between similar contexts).

**Part 2 — `neural-char/` — how learning works.**
Now we *learn* that distribution instead of counting it. To do that honestly we
first build a **reverse-mode automatic-differentiation engine** from scratch —
the same idea as Karpathy's *micrograd*, but in Swift — and prove it correct with
finite-difference gradient checks. Then we train a **neural bigram** (watch the
loss fall below the `ln(V)` "pure-guessing" line — direct proof of learning) and
graduate to a **multi-layer perceptron** with character embeddings and a hidden
layer. This is the part where *backpropagation* stops being a buzzword.

**Part 3 — `mini-gpt/` — the modern recipe.**
The MLP can only see a fixed, short window. The **Transformer** fixes this with
**self-attention**: every position decides, for itself, which earlier positions
are worth listening to. We build a real GPT — token + positional embeddings,
multi-head causal self-attention computed *by hand* (matmul → scale → mask →
softmax → matmul), feed-forward MLPs, residual connections, LayerNorm, and an
AdamW training loop — on **MLX**, Apple's array/autodiff framework. It trains in
minutes and you even get to *watch it overfit*, which teaches you why we hold out
a validation set.

**Part 4 — `swift-rag/` — making it useful.**
A trained model only knows what was baked into its weights. To answer questions
about *your* documents, we **retrieve** the relevant passages first (classic
lexical search with **BM25** over an inverted index, built from scratch) and then
hand them to a **local Llama-2** model inside the prompt. Retrieval does the
"knowing"; generation does the "phrasing". This is the architecture behind most
real-world LLM applications today — and here it runs entirely on your machine
with no cloud and no Python.

---

## What each part teaches

Reading the four parts in order, each concept is introduced once (filled dot
below) and then reinforced in later parts (rings). Nothing is assumed; the ideas
accumulate.

<p align="center">
  <img src="docs/diagrams/concept-map.svg" alt="Concept coverage matrix across the four parts" width="100%">
</p>

If you already know the basics, this map also tells you **where to jump in**: want
attention? Part 3. Want backprop? Part 2. Want retrieval? Part 4.

---

## Navigation — where to read what

Every part ships **three teaching artifacts**: a `README.md` (the map), a
`docs/TEXTBOOK.md` (the full chapter-by-chapter course), and a `docs/diagrams/`
folder (clean SVGs of every mechanism). Here is the whole shelf:

### Part 1 — n-gram (counting)

| | |
|---|---|
| Code & textbook in one | [`ngram.swift`](ngram.swift) — a single, exhaustively-commented script that *is* its own textbook |
| Run | `./run.sh ngram` &nbsp;·&nbsp; or `swift ngram.swift [yourfile.txt]` |

### Part 2 — neural-char (autograd + neural LM)

| | |
|---|---|
| Overview | [`neural-char/README.md`](neural-char/README.md) |
| Full course | [`neural-char/docs/TEXTBOOK.md`](neural-char/docs/TEXTBOOK.md) — *13 chapters*: gradients → the autograd engine → backprop → gradient checking → data → softmax/cross-entropy → the neural bigram → generation → the MLP → experiments, + a `Value` API cheat-sheet and a bridge to the Transformer |
| Diagrams | [`neural-char/docs/diagrams/`](neural-char/docs/diagrams/) — backprop, the computation graph, topological sort, op derivatives, softmax/cross-entropy, the bigram, MLP architecture, temperature, loss curves, the ladder |
| Run | `./run.sh neural` &nbsp;·&nbsp; or `cd neural-char && swift run -c release` |

### Part 3 — mini-gpt (Transformer on MLX)

| | |
|---|---|
| Overview | [`mini-gpt/README.md`](mini-gpt/README.md) |
| Full course | [`mini-gpt/docs/TEXTBOOK.md`](mini-gpt/docs/TEXTBOOK.md) — *12 chapters*: the big picture → data → embeddings → **attention** → the MLP → the block (residuals & norm) → the full model → training → generation → experiments → glossary, + shape & MLX-API cheat-sheets |
| Diagrams | [`mini-gpt/docs/diagrams/`](mini-gpt/docs/diagrams/) — architecture, tokenization, embeddings, attention, multi-head, the causal mask, the block, the loss curve |
| Run | `./run.sh gpt [args]` &nbsp;·&nbsp; or `cd mini-gpt && ./run.sh` &nbsp;·&nbsp; guided demos: `cd mini-gpt && ./examples.sh` |

### Part 4 — swift-rag (retrieval-augmented generation)

| | |
|---|---|
| Overview | [`swift-rag/README.md`](swift-rag/README.md) |
| Full course | [`swift-rag/docs/TEXTBOOK.md`](swift-rag/docs/TEXTBOOK.md) — *13 chapters*: the big picture → chunking → the inverted index → **BM25** → retrieval → the local LLM → building the prompt → generation → the whole pipeline → experiments → dense retrieval → glossary, + a worked BM25-by-hand example and engine/file-format appendices |
| Diagrams | [`swift-rag/docs/diagrams/`](swift-rag/docs/diagrams/) — the pipeline, chunking, the inverted index, BM25, BM25-vs-dense, retrieval, prompt budget, the transformer, generation |
| Run | `./run.sh rag [chat\|ask\|search ...]` &nbsp;·&nbsp; or `cd swift-rag && ./run.sh` |

---

## How the repository is laid out

<p align="center">
  <img src="docs/diagrams/repo-map.svg" alt="Repository layout and the three teaching artifacts" width="100%">
</p>

```
swift-model/
├── README.md              ← you are here: the overview + navigation
├── run.sh                 ← run any part:   ./run.sh <part> [args…]
├── setup.sh               ← verify toolchain + pre-build the pure-Swift parts
├── test.sh                ← smoke test: does every part still build/run?
├── docs/diagrams/         ← the overview diagrams embedded above
│
├── ngram.swift            ← Part 1: one self-contained, commented script
├── neural-char/           ← Part 2: autograd engine + neural bigram + MLP
├── mini-gpt/              ← Part 3: a char-level GPT Transformer (MLX/Metal)
└── swift-rag/             ← Part 4: BM25 retrieval + local Llama-2 generation
```

Parts 2–4 are each a standalone SwiftPM package with its own `Sources/`,
`README.md`, and `docs/`. There is **no shared build state** — building or
deleting one never touches another.

---

## The root scripts

Three small, well-commented scripts at the root tie the parts together. They are
**smart**: where a part needs setup (dependencies, the Metal shader compile, the
one-time model download), they trigger that part's own self-installing setup for
you.

| Script | What it does |
|--------|--------------|
| [`run.sh`](run.sh) | **The one command.** `./run.sh <part> [args…]` builds the chosen part if needed (delegating to its smart `run.sh`/`setup.sh`) and runs it, forwarding all arguments. Parts: `ngram`/`1`, `neural`/`2`, `gpt`/`3`, `rag`/`4`. |
| [`setup.sh`](setup.sh) | **Warm-up.** Checks for a Swift toolchain, reports each part's platform readiness, and pre-builds the pure-Swift parts (1, 2, 4) so the first `run.sh` is instant. Part 3 (MLX/Metal) is prepared via its own setup on first run. |
| [`test.sh`](test.sh) | **Smoke test.** Compiles every part (and actually *runs* Part 1), skipping Part 3 automatically off Apple Silicon. Prints a pass/fail/skip summary and exits non-zero on any failure — handy before committing. |

The per-part scripts they delegate to ([`mini-gpt/run.sh`](mini-gpt/run.sh),
[`mini-gpt/setup.sh`](mini-gpt/setup.sh),
[`mini-gpt/prepare_metal.sh`](mini-gpt/prepare_metal.sh),
[`swift-rag/run.sh`](swift-rag/run.sh),
[`swift-rag/setup.sh`](swift-rag/setup.sh)) handle the heavier, platform-specific
work — they are documented in each part's README.

---

## Requirements & platforms

| Part | Swift toolchain | Extra requirements | Linux | macOS (Intel) | macOS (Apple Silicon) |
|------|-----------------|--------------------|:-----:|:-------------:|:---------------------:|
| 1 · ngram | 5.9+ | none | ✅ | ✅ | ✅ |
| 2 · neural-char | 5.9+ | none | ✅ | ✅ | ✅ |
| 3 · mini-gpt | 5.9+ | **MLX** + full Xcode with the **Metal Toolchain** | ❌ | ❌ | ✅ |
| 4 · swift-rag | 5.9+ | `curl` (one-time model download ~58–418 MB) | ✅ | ✅ | ✅ |

Three of the four parts run anywhere Swift runs. Only **Part 3 requires an
Apple-Silicon Mac**, because MLX executes on the Metal GPU with no CPU/CUDA
fallback. (`test.sh` and `setup.sh` detect this and skip Part 3 elsewhere rather
than failing.)

Check your toolchain with `swift --version` (tested with Swift 6.x).

---

## How the parts relate

The four parts are deliberately built around **one shared task** so the contrast
is exact. Each step removes a limitation of the previous one:

| | Part 1 · n-gram | Part 2 · neural-char | Part 3 · mini-gpt | Part 4 · swift-rag |
|---|---|---|---|---|
| **How it gets the next-token distribution** | counts frequencies | learns weights by gradient descent | learns weights *with attention* | uses a *pre-trained* model + retrieved context |
| **Context it can use** | last *n* chars | 1 char (bigram) → fixed window (MLP) | the whole block, via attention | the question + retrieved passages |
| **Unseen input** | dead end | always produces a distribution | always produces a distribution | retrieval finds *something* relevant |
| **What's genuinely new** | the *target* to match | *how* training works (backprop) | *attention* & scaling to a real framework | *grounding* answers in your own data |
| **Speed vs. clarity trade-off** | instant; no learning | scalar autograd: slow but transparent | minutes on a GPU; framework-backed | tiny model on CPU; honest about quality |

The clearest single lesson lives at each boundary: **1→2** shows the difference
between *counting* and *learning* the same probabilities; **2→3** shows what
*attention* buys you over a fixed context window; **3→4** shows that a fixed,
trained model becomes useful on *new* knowledge only when you *retrieve and feed*
it that knowledge.

---

## FAQ

**Do I need a GPU?**
Only for Part 3 (MiniGPT on MLX/Metal, Apple Silicon). Parts 1, 2, and 4 are
plain CPU Swift and run on Linux or any Mac.

**Where should I start?**
If you want the full story, start at Part 1 and climb. If you have a specific
goal, use the [concept map](#what-each-part-teaches) to jump straight to the part
that introduces it.

**README vs. TEXTBOOK — what's the difference?**
The `README.md` in each part is the quick map (what it is, how to run it, the
concepts in brief). The `docs/TEXTBOOK.md` is the actual course: numbered
chapters that walk the real code line by line, with the math, the diagrams, and
exercises. Read the README to get going; read the textbook to *understand*.

**Is the generated text supposed to be good?**
Up to a point. Parts 1–3 produce text that looks increasingly like the training
data (real words, then sentences, then speaker tags and structure). Part 4's
*retrieval* is genuinely useful, but its bundled *generator* is a 15–110M-param
TinyStories model with a 256-token window, so answers are often loosely
on-topic — that's called out honestly in its README, and swapping in a larger
checkpoint improves it with no code changes.

**Why Swift, and why from scratch?**
Swift is fast, readable, and strongly typed, which makes the math easy to follow
without ceremony. "From scratch" is the whole point: the value here is seeing the
mechanism, so the only thing we *don't* reimplement is Part 3's array framework
(MLX) and Part 4's inference kernel (a vendored, unmodified `llama2.swift`) —
and both parts say exactly what they delegate and why.

---

## Credits & further reading

This course stands on the shoulders of some wonderful teaching work:

- **Andrej Karpathy** — [micrograd](https://github.com/karpathy/micrograd) (the
  spirit of Part 2's autograd engine), [makemore](https://github.com/karpathy/makemore)
  (the bigram → MLP progression), [nanoGPT](https://github.com/karpathy/nanoGPT)
  (the shape of Part 3), and [llama2.c](https://github.com/karpathy/llama2.c)
  (the inference engine behind Part 4).
- **Bengio, Ducharme, Vincent & Jauvin (2003)** — *A Neural Probabilistic
  Language Model* (the design behind Part 2's MLP).
- **Vaswani et al. (2017)** — *Attention Is All You Need* (Part 3's Transformer).
- **Robertson & Zaragoza** — *The Probabilistic Relevance Framework: BM25 and
  Beyond* (Part 4's retrieval).
- [MLX Swift](https://github.com/ml-explore/mlx-swift) — Apple's array & autodiff
  framework used in Part 3.
- The vendored `llama2.swift` engine comes from
  [`asaptf/swift-os`](https://github.com/asaptf/swift-os); see
  [`swift-rag/NOTICE`](swift-rag/NOTICE) for the full attribution chain and model
  provenance.

Each part's own README and TEXTBOOK list more specific references for its topic.

---

*Built to be read. Open any part's `docs/TEXTBOOK.md`, run its examples, and
change a number to see what happens — that's the fastest way to learn this.*
