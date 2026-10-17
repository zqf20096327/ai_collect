# LLM & VLM Guide — From Transformers to Multimodal AI

> A beginner-first, story-driven guide to how modern language and multimodal models work — from the first language-model idea to Transformers, LLMs, VLMs, audio, video, and today's major model families.

**Created and maintained by [Ahmad Jeddizahed](https://github.com/AhmadJeddi).**

This guide is for the reader who opens a page about AI and sees **Transformer, attention, tokenizer, LLM, VLM, projector, multimodal, GPT, Llama, Qwen, Gemini** and a dozen other words — and wants to understand how they are connected instead of memorizing definitions one by one.

The guide is intentionally written as a journey:

```text
A user asks a question
        ↓
The machine needs to represent language
        ↓
Sequence models try to carry context
        ↓
The Transformer changes how context is connected
        ↓
Large-scale training turns Transformers into LLMs
        ↓
Text becomes tokens, representations, and generated tokens
        ↓
The user sends an image
        ↓
The language model needs a way to see
        ↓
VLMs connect vision and language
        ↓
Audio and video join the picture
        ↓
Modern model families branch in many directions
```

The goal is not to make you memorize every box in every architecture diagram. The goal is to make the next diagram you see **feel familiar**.

---

## How to use this guide

Read the main text from top to bottom. The main path tells the story.

When you see a `Technical deep dive`, open it only when you want the lower-level details. Those sections are deliberately separated so that formulas and implementation terminology do not interrupt the main explanation.

The companion files have different jobs:

- `MODEL_GUIDE.md` is the quick reference sheet.
- `REFERENCES.md` is the source map.
- `assets/` contains the architecture and flow diagrams.

---

# 1. Start with one question

Imagine you upload a picture of a cat looking at a butterfly and ask:

> **What is the cat looking at?**

A person can answer almost immediately. We see the cat, see the butterfly, notice their relationship, understand the question, and put the result into words.

Now stop and look at what the computer actually received.

The question is text.

The picture is pixels.

Those are two very different kinds of data.

That tiny example gives us the whole reason modern multimodal AI is interesting:

> **How do we turn different kinds of information into representations a neural network can combine and use to produce a useful answer?**

To answer that, we first need to understand the language side.

A language model begins with a deceptively simple idea:

> Given what has appeared so far, what is a plausible next piece of language?

For example:

```text
The sky is usually ...
```

A language model can assign different probabilities to possible continuations such as `blue`, `clear`, and so on.

That may sound like autocomplete, and at a basic level it is related to autocomplete. The difference is scale, training, architecture and learned representations. At large scale, next-token prediction becomes a way for a model to absorb patterns of grammar, facts, style, code and relationships in language.

But predicting the next token is only half of the story.

The model also has to answer a harder question:

> **How should information from one part of a sequence affect another part much farther away?**

That takes us to the models that came before today's LLMs.

---

# 2. Before the Transformer: the problem was keeping context

Before Transformers became dominant, recurrent neural networks were an important way to process sequences.

The idea was intuitive. Read one token, update an internal state, read the next token, update the state again, and continue.

```text
Token 1 → state 1 → Token 2 → state 2 → Token 3 → state 3 → ...
```

The state is a running summary of the sequence.

That works. In fact, it worked well enough to become a major family of sequence models.

The trouble appears when the sequence gets long.

Suppose a sentence starts with an important fact and only much later contains a word whose meaning depends on that fact. The information has to survive a chain of recurrent updates. Training is also naturally tied to the order of the sequence, which makes large-scale parallel computation harder.

LSTMs improved this situation with gates that help control what information should be kept, changed or forgotten. They were an important advance, not a failed experiment.

But researchers kept asking:

> **What if a token could directly look at other tokens instead of waiting for information to travel through the sequence one step at a time?**

That question leads naturally to attention.

And in 2017, it led to the Transformer.

![Before Transformers](assets/01-before-transformer.svg)

---

## The Transformer: instead of carrying everything forward, let information meet

The paper **Attention Is All You Need** introduced the Transformer in 2017. The original architecture removed recurrence and convolution from its core sequence-transduction design and relied on attention instead. The paper also showed an important practical advantage: the architecture was more parallelizable for training than recurrent alternatives in that setting. [1]

The easiest way to understand the idea is still our simple sentence.

> **The cat chased the butterfly because it moved.**

When the model reaches `it`, it benefits from information elsewhere in the sentence. Attention gives the representation at one position a learned way to gather information from other positions.

So instead of imagining one memory being dragged from left to right, imagine a group of tokens that can look at one another and decide what information is relevant.

```text
Older recurrent picture

A → B → C → D → E

Information is carried forward step by step.

Transformer-style picture

A ───────┐
B ─────┐ │
C ───┐ │ │
D ─┐ │ │ │
E ─┴─┴─┴─┘

Representations can interact through attention.
```

This was the turning point.

But there is a detail that often gets lost in beginner explanations: **the Transformer is an architecture, not the name of a single kind of model.**

The original paper used an encoder and a decoder. Later researchers reused the Transformer idea in different shapes, including encoder-only systems such as BERT, decoder-only systems in the GPT line, and encoder-decoder systems such as T5. [1][2][4]

So the mental model should be:

```text
Transformer
    ↓
architecture family
    ↓
several different ways to organize reading and generation
```

![Transformer anatomy](assets/02-transformer-anatomy.svg)

<details>
<summary>Technical deep dive: what is inside a Transformer block?</summary>

A simplified Transformer block looks like this:

```text
input representation
        ↓
attention
        ↓
residual + normalization
        ↓
MLP / feed-forward network
        ↓
residual + normalization
        ↓
output representation
```

The exact ordering differs across implementations, so do not memorize one diagram as a universal law.

The components have different jobs:

- **Attention** lets positions exchange contextual information.
- **MLP / feed-forward network** applies learned nonlinear transformations after context has been mixed.
- **Residual connection** provides a shorter path around a sub-layer, which helps deep networks train.
- **Normalization** helps stabilize the numerical behavior of the network.
- **Position information** gives the model a way to distinguish order.

The important beginner question is not "Can I name every component?" It is "Why does the block need more than attention?"

Attention mixes information. The MLP then transforms that information. Residual paths and normalization help the whole stack remain trainable and stable.

</details>

---

# 3. Attention: the mechanism that lets the pieces talk to each other

Now that we know **why** the Transformer needed a new mechanism, we can look closer at attention without losing the story.

Suppose the model is processing `it` in:

> The cat chased the butterfly because it moved.

The useful question is not "What is the definition of attention?"

It is:

> **Which other pieces of the context should matter for this representation?**

That is the job attention is trying to solve.

A useful mental picture is:

```text
Current token
     ↓
ask what information is relevant
     ↓
compare against other positions
     ↓
weight the useful information
     ↓
combine it into a better representation
```

The standard Transformer uses **Query (Q), Key (K), and Value (V)**.

You can think of them as:

- **Query:** what information am I looking for?
- **Key:** what kind of information do I have here?
- **Value:** what should be passed along if this position is relevant?

The exact mathematics matters when you start implementing or analyzing a model, but the intuition comes first.

![Attention](assets/03-attention.svg)

### Self-attention and multi-head attention are not rival generations

This is an easy place to get confused.

**Self-attention** describes the relationship between the source of the queries/keys/values: the sequence is attending to itself.

**Multi-head attention** describes running several learned attention projections in parallel.

So you can have **multi-head self-attention**.

A good analogy is asking several groups of readers to look at the same sentence from different perspectives. The model learns the perspectives; we do not manually tell one head to be "grammar" and another to be "pronouns."

**Cross-attention** is different because the information being queried can come from another representation stream.

That will become important later when vision and language need to meet.

<details>
<summary>Technical deep dive: the attention equation</summary>

The original Transformer defines scaled dot-product attention as:

```text
Attention(Q, K, V)
    = softmax(QKᵀ / √dₖ) V
```

Read it as a sequence of operations:

```text
compare Q with K
      ↓
turn the scores into weights
      ↓
use those weights to mix V
```

Multi-head attention repeats this idea over several learned projections and combines the resulting representations. [1]

The equation is the precise version of the intuition above; the intuition is the better starting point for a beginner.

</details>

---

# 4. One architecture, three important shapes

Now we can answer a natural follow-up question:

> If Transformer is an architecture family, how can the same idea be used for such different models?

The answer is that researchers changed **how the model reads and generates sequences**.

There are three classic shapes worth knowing.

![Three architectures](assets/04-three-architectures.svg)

### Encoder-only: mostly about understanding the input

BERT is the classic example. It was designed to learn deep bidirectional representations by conditioning on both left and right context. That made it especially useful for tasks where the goal is to understand or represent an input rather than generate an open-ended continuation. [2]

Imagine:

```text
sentence
   ↓
read the surrounding context
   ↓
build a rich representation
```

The important idea is **understand the input**.

### Decoder-only: keep generating the next token

Now change the task.

Instead of asking the model to build a representation for a sentence, we want it to continue the sequence:

```text
prompt
  ↓
next token
  ↓
next token
  ↓
next token
  ↓
...
```

This is the shape associated with GPT-style autoregressive language models.

The model is constrained so that when predicting a position, it does not look ahead at future tokens.

The important idea is **continue the sequence**.

### Encoder-decoder: read one sequence and produce another

The original Transformer and models such as T5 use an encoder to process the source and a decoder to generate the target. T5 made this especially intuitive by treating many NLP tasks as text-to-text transformations. [1][4]

```text
source sequence
      ↓
   encoder
      ↓
representation of source
      ↓
   decoder
      ↓
target sequence
```

Translation is an easy example:

```text
"Hello"
   ↓
"Bonjour"
```

### The connection to remember

These are not "version 1, 2 and 3" of the Transformer.

They are different **architectural arrangements for different jobs**.

| Shape | Main idea | Typical strength |
|---|---|---|
| Encoder-only | understand an input | representation / classification |
| Decoder-only | predict the next token | generation |
| Encoder-decoder | read source, generate target | translation / summarization / transformation |

Once you understand this, the phrase **decoder-only LLM** stops sounding mysterious.

---

## From that architecture to the LLM

We now have a scalable sequence architecture and a language-modeling objective.

So what turns that into an **LLM**?

There is no official parameter-count switch that flips from "language model" to "LLM." The term generally describes language models trained at large scale, where model capacity, data and compute are all much larger than in earlier systems.

GPT-3 became a landmark example. Its 2020 paper described a 175-billion-parameter autoregressive language model and showed strong few-shot performance across many tasks without task-specific gradient updates during inference. [3]

The important lesson was not simply that "bigger is better."

The deeper lesson was:

> **One large pretrained model can learn a broad set of capabilities instead of requiring a separate model for every small task.**

That changed how people thought about NLP systems.

Instead of building:

```text
one task → one model
```

research increasingly moved toward:

```text
large pretrained model
        ↓
many possible tasks through prompts, adaptation and post-training
```

This is where the modern foundation-model idea becomes important.

<details>
<summary>Technical deep dive: why parameter count alone does not define an LLM</summary>

A model's behavior depends on much more than parameter count:

```text
parameters
+ data
+ architecture
+ optimization
+ training compute
+ post-training
+ inference setup
```

Two models with similar parameter counts can have very different strengths because these other ingredients differ.

That is why a parameter number should be treated as one piece of evidence, not a universal ranking.

</details>

---

# 5. From your sentence to the answer

Here is where the story becomes concrete.

You type:

```text
The cat is looking at a butterfly.
```

The model's neural layers do not receive an English sentence in the way a human reads it.

First, a **tokenizer** turns the text into model-specific pieces called tokens.

A token might be a whole word, part of a word, punctuation, or another unit. The exact split depends on the tokenizer.

So a conceptual example like:

```text
"unbelievable!"
        ↓
"un" + "believable" + "!"
```

is only an illustration. Another tokenizer may split the text differently.

Those tokens become integer IDs. The IDs then map into learned vectors called **embeddings**.

```text
text
  ↓
tokens
  ↓
token IDs
  ↓
embeddings
  ↓
Transformer blocks
```

![Text input pipeline](assets/05-text-input-pipeline.svg)

There is one more thing the model needs to know: **order**.

Attention does not automatically make the sequence order obvious, so Transformer families use some positional mechanism. The original Transformer used sinusoidal positional encodings; later models have used other approaches.

Now the input has become something the neural network can work with:

```text
human-readable text
       ↓
model-specific tokens
       ↓
numerical representations
       ↓
context-aware representations
```

And that prepares us for the next question:

> **How do those representations turn back into an answer?**

---

## How the answer is generated

Let's ask:

> What is a butterfly?

The model processes the prompt through its Transformer layers. At the output side, it produces scores for the vocabulary — in other words, scores for possible next tokens.

Imagine the model is considering many possible continuations:

```text
A           → one score
small       → another score
butterfly   → another score
...
```

Those scores can be converted into a probability distribution, and a decoding strategy chooses the next token.

The chosen token is appended to the context, and the process runs again.

```text
prompt
  ↓
Transformer
  ↓
scores for possible next tokens
  ↓
decoding
  ↓
next token
  ↓
append token
  ↓
run again
  ↓
next token
  ↓
...
```

![Generation loop](assets/06-generation-loop.svg)

This repeated process is the basic idea behind **autoregressive generation**.

A long answer that feels like one continuous thought is produced through many prediction steps.

That does not mean the model is simply looking up the next word in a database. The learned behavior is distributed across the network's parameters and internal representations.

It also does not mean the model literally operates on human words internally. The interface exposes tokens, while the internal computation is high-dimensional.

### Why can the answer change?

Because the output depends on more than the visible prompt.

Depending on the system, generation can also be influenced by:

- sampling settings
- conversation context
- system instructions
- retrieved information
- available tools
- the specific model snapshot

So a single impressive answer is not the same thing as a reliable measurement of a model.

<details>
<summary>Technical deep dive: logits, probabilities and temperature</summary>

The final model layer produces **logits**, which are scores over the vocabulary.

```text
hidden representation
        ↓
logits
        ↓
probability distribution
        ↓
decoding
        ↓
next token
```

Softmax is commonly used to turn logits into probabilities.

Decoding may be greedy, sampled, or use strategies such as top-k or top-p.

Temperature changes the sharpness of the distribution used during sampling. It changes the selection behavior; it does not modify the trained weights.

</details>

---

# 6. How the model learned to do all of this

So far, we have been watching an already-trained model at inference time.

But where did its abilities come from?

It helps to imagine training as a progression.

```text
large amounts of data
        ↓
pretraining
        ↓
broad language capabilities
        ↓
instruction / preference post-training
        ↓
more useful behavior
        ↓
evaluation and refinement
```

### Pretraining: learn broad patterns

A simple example of an autoregressive training objective is:

```text
Input:  The cat sat on the
Target: mat
```

The real process is vastly larger: huge datasets, many batches, many optimization steps, and careful choices about data and compute.

The beginner idea is simply that the model repeatedly learns to predict missing or future pieces of data and updates its parameters when the prediction is wrong.

### Post-training: shape how the capability is used

A pretrained model can know a great deal about language without automatically behaving like a helpful assistant.

Instruction tuning and other post-training techniques can teach it to follow requests, use formats and respond in preferred ways.

So a useful mental distinction is:

> **Pretraining builds broad capability; post-training shapes behavior.**

Different organizations use different methods, and not every detail is public.

### Evaluation: the model still has to prove itself

Benchmarks are useful, but real systems need more than leaderboard numbers.

A production model may also be judged on:

- accuracy on the actual task
- robustness
- latency
- cost
- safety
- edge cases
- failure recovery

That becomes especially important when we add images, audio and video, because fluent output can hide an incorrect interpretation.

---

# 7. The moment we add an image, the problem changes

Now return to our original question:

> **What is the cat looking at?**

The text part is familiar. The image is not.

An image starts as pixels arranged in a grid. The language model's text pipeline expects learned representations of tokens.

So a multimodal system needs another route.

A common conceptual path is:

```text
image
  ↓
preprocessing
  ↓
vision encoder
  ↓
visual representation
  ↓
bridge / fusion
  ↓
language-side processing
  ↓
answer
```

That is the basic territory of a **Vision-Language Model (VLM)**.

![Image to answer](assets/07-image-to-answer.svg)

The important idea is not that the image magically becomes a sentence first.

A vision component can turn the image into learned features or visual tokens. Another mechanism then connects those features to the language side.

Vision Transformers are an important part of this history. ViT showed that Transformer-style processing could be applied directly to sequences of image patches and work strongly for image recognition. [10]

This matters because it gave vision and language a more compatible architectural vocabulary: both can be represented as sequences of learned features and processed with Transformer-style machinery.

---

## VLMs: where vision and language meet

Once you understand the problem, the variety of VLM architectures becomes much easier to read.

The key question is:

> **At what point do the visual and language representations meet?**

There is no single VLM blueprint.

### A practical pattern: vision encoder + projector + LLM

One common design looks like:

```text
image
  ↓
vision encoder
  ↓
visual features
  ↓
projector / adapter
  ↓
language model
  ↓
answer
```

The projector is a learned bridge between representation spaces.

LLaVA is an influential example of this general direction. It connects a vision encoder and an LLM and uses visual instruction tuning to improve multimodal instruction following. [8]

This design is easy to reason about because each side has a recognizable job:

```text
vision side → represent what is seen
language side → use context and generate language
bridge → make the representations usable together
```

### Another pattern: cross-attention

Instead of simply projecting visual features into the language representation space, a model can use cross-attention to let one stream query another.

Conceptually:

```text
language representations
         ↓
     cross-attention
         ↑
visual representations
```

Flamingo is an important research example. It was designed to bridge pretrained vision and language models and handle interleaved visual and textual inputs, including image and video inputs. [7]

### Newer direction: tighter multimodal integration

Modern multimodal systems increasingly blur the simple boundary between:

```text
LLM + vision add-on
```

and:

```text
one system designed around multiple modalities
```

Current model families expose combinations of text, image, audio and video, and some newer releases use architectures that integrate those modalities more deeply. For example, Meta's current Llama materials describe natively multimodal Llama 4 models, while Qwen3-Omni describes an end-to-end omni-modal system for text, images, audio and video. [18][19]

So when you encounter a VLM, do not start by asking which acronym is used.

Start with four questions:

```text
What goes in?
      ↓
How is it represented?
      ↓
Where do representations meet?
      ↓
What produces the output?
```

Those four questions will work across many papers and model cards.

---

# 8. The cat-and-butterfly example, end to end

We can finally trace the original question end to end.

```text
                 IMAGE
                   │
                   ▼
            Vision encoder
                   │
             visual features
                   │
                   ▼
Question → text representation
                   │
                   ▼
              bridge / fusion
                   │
                   ▼
             language model
                   │
                   ▼
      "The cat is looking at a butterfly."
```

Notice what the system had to combine:

- information about the cat
- information about the butterfly
- their relationship in the image
- the wording of the user's question
- the model's learned language patterns

That is why VLMs are more than ordinary image classification.

A classifier might produce:

```text
cat
```

A VLM can potentially produce:

```text
The cat is looking at a butterfly.
```

The second answer is richer because it is **language-conditioned visual understanding**, not just a class label.

But there is an important warning.

A fluent answer is not proof that the visual interpretation is correct.

A VLM can miss small details, misunderstand spatial relationships or confidently describe something that is not actually present.

So the practical question is not:

> "Can the model say something that sounds right?"

It is:

> **"Can the system answer this task accurately enough, and can we detect or recover from its failures?"**

That distinction becomes one of the most important ideas when moving from model demos to engineering.

---

## The same pattern extends to audio and video

Once you understand the idea of **modality → representation → connection → output**, audio and video stop looking like completely unrelated topics.

## Audio

Audio begins as a time-varying signal, not a text token sequence.

So a speech system needs some form of audio representation before language-style processing can be applied.

```text
audio waveform
      ↓
audio frontend / encoder
      ↓
audio representation
      ↓
language or multimodal processing
      ↓
text / speech / other output
```

Whisper is a major historical example. Its work used a very large and diverse web-audio dataset for multilingual and multitask speech recognition, with a strong emphasis on robustness across accents, noise and technical language. [9]

The larger lesson is:

> **Audio is not simply text stored in another file format. It has timing and acoustic structure that the model must represent.**

## Video

Video adds another dimension: time.

An image answers:

> What is visible now?

A video can require:

> What happened first?
> What changed?
> When did the action happen?
> What is the person doing over several moments?

So the simplified path becomes:

```text
video
  ↓
frames / visual features
  ↓
spatial understanding
  ↓
temporal relationships
  ↓
multimodal reasoning
  ↓
answer or action
```

Flamingo already demonstrated a vision-language architecture that could ingest images and videos. [7]

Current multimodal systems increasingly treat text, image, audio and video as parts of one broader interface. Google's current Gemini materials, for example, describe multimodal capabilities across these modalities, while Qwen3-Omni describes native processing of text, images, audio and video with text and speech output. [17][19]

![Audio and video](assets/08-audio-video.svg)

The exact architecture differs, but the core idea stays stable:

> **Every modality has its own structure, so every modality needs a suitable representation before the system can reason over it.**

---

# 9. Where today's model families fit

Only now — after the architecture story is clear — does it make sense to talk about names such as **GPT, Claude, Gemini, Llama, Qwen, Mistral and DeepSeek**.

The names are families and ecosystems, not interchangeable architecture labels.

![Model family landscape](assets/09-family-landscape.svg)

### OpenAI — GPT and related model families

The GPT line is historically important for large-scale autoregressive language modeling. The current OpenAI catalog is broader than the old idea of "a text model": it includes general-purpose models as well as specialized image, audio, realtime and other systems. Current model IDs and capabilities should be checked against the official model catalog. [15]

### Anthropic — Claude

Claude is a model family from Anthropic focused on language, reasoning, analysis, coding and related tasks. Anthropic's current documentation also lists vision capabilities for current models, which is a useful reminder that the old boundary between "LLM" and "VLM" is increasingly blurry. [16]

### Google — Gemini

Gemini is explicitly a multimodal family. Current Google documentation describes combinations of text, image, audio and video capabilities. [17]

### Meta — Llama

Llama became a major open-weight model family. The original LLaMA work is an important historical reference, while current Meta material includes natively multimodal Llama 4 models. [14][18]

### Qwen

Qwen has expanded from language models into vision-language and omni-modal systems. Current official material includes Qwen3-VL and Qwen3-Omni, with Qwen3-Omni describing text, image, audio and video input. [19]

### Mistral

Mistral's current catalog spans generalist text and multimodal models as well as specialized systems such as OCR-oriented models. It is also useful for seeing that one ecosystem can contain both dense and sparse model designs. [20]

### DeepSeek

DeepSeek is another major modern family, particularly visible in discussions of reasoning and efficient model design. Its active API model identifiers and capabilities should be read from the current official documentation rather than an old static list. [21]

The important point is not to memorize seven brands.

The timeline below is deliberately selective. It is a memory aid, not a complete history of every influential model.

It is to learn how to place a new model on the map:

```text
family
  ↓
generation
  ↓
variant
  ↓
modalities / behavior
  ↓
deployment
```

![Model generations](assets/10-model-generations.svg)

### Why version numbers can be misleading

A new model generation does not have to mean that the entire core architecture was replaced.

A generation can change:

- training data
- post-training
- context handling
- modality support
- routing
- efficiency
- reasoning behavior
- inference strategy

So the safe rule is:

> **Version number ≠ architecture.**

When architecture matters, read the research paper, technical report or official model documentation.

<details>
<summary>How to interpret a model name</summary>

A model name may encode several different things:

```text
Family + generation + size + variant + modality / reasoning + quantization
```

But providers do not follow one universal naming grammar. A suffix that means "vision" in one ecosystem may mean something else in another.

Treat names as clues, not proof.

</details>

---

## The field also branches beyond dense Transformers

The Transformer is the dominant idea in modern language modeling, but it is not the only direction worth understanding.

Two branches are especially useful because they explain terms that appear frequently in modern architecture discussions.

## Mixture-of-Experts: use only some parameters for each input

A dense network can send every token through the same full parameter blocks.

An **Mixture-of-Experts (MoE)** model can instead use a router to choose a subset of experts.

```text
token
  ↓
router
 ├──→ Expert A
 ├──→ Expert B
 └──→ Expert C
        ↓
   combined result
```

The attraction is that the model can contain many parameters while activating only a subset for each token.

Switch Transformer is a landmark example of this sparse-expert direction. Its paper simplified the routing design and studied large sparse models as a way to improve the parameter-to-compute trade-off. [11]

The trade-off is that routing and distributed execution introduce their own engineering complexity.

## State-space models: another way to process sequences

Mamba explored **selective state-space models** as an alternative sequence-processing mechanism. The work was motivated in part by the computational challenges of long sequences and proposed a design with efficient sequence scaling under its formulation. [12]

The right conclusion is not:

> "Transformers are obsolete."

It is:

> **There is a larger design space than one architecture.**

Modern systems can also combine ideas, which is why terms such as hybrid models and sparse architectures appear alongside traditional Transformer terminology.

---

# 10. How to read and choose a model without getting lost

At this point you should not need to memorize every architecture.

When a new model appears, ask the same questions every time.

### First: what goes in?

```text
text?
image?
audio?
video?
multiple modalities?
```

### Second: how is each input represented?

```text
text  → tokenizer / embedding pipeline
image → vision encoder / visual representation
audio → audio encoder / audio representation
video → visual + temporal representation
```

### Third: where do the streams meet?

Look for ideas such as:

```text
projector
adapter
cross-attention
fusion
shared representation
```

### Fourth: what is the main sequence architecture?

```text
encoder-only
decoder-only
encoder-decoder
MoE
hybrid
state-space based
```

### Fifth: what comes out?

```text
text
speech
structured data
tool calls
action
```

This is a much better reading strategy than memorizing a brand name and trying to infer everything from it.

---

## Choosing a model: start with the problem, not the leaderboard

Suppose three projects arrive on your desk.

### Project A — summarize documents

You mainly need language understanding and generation.

### Project B — rename wallpapers from what is visible in the image

Now visual understanding matters, so a VLM or multimodal model is relevant.

### Project C — listen to a meeting, understand slides, and produce action items

Now text, audio and images may all be useful.

The selection process is therefore:

```text
problem
  ↓
inputs
  ↓
outputs
  ↓
constraints
  ↓
candidate models
  ↓
real evaluation
```

Useful constraints include:

- VRAM / RAM
- latency
- throughput
- budget
- privacy
- offline operation
- license
- context length
- modality support

For a multimodal application, your evaluation set should contain the kinds of difficult examples the system will actually see: cluttered images, ambiguous scenes, small text, misleading context, unusual inputs and edge cases.

A model that is slightly weaker on a public benchmark can still be the better engineering choice if it fits your hardware, cost and failure tolerance better.

![Model selection](assets/11-model-selection.svg)

---

# 11. The whole journey in one picture

We started with one question:

> **What is the cat looking at?**

Now we can trace the ideas backward.

```text
USER QUESTION
     │
     ├────────────── text ──────────────┐
     │                                  │
     ▼                                  ▼
 tokenizer                         image input
     │                                  │
 embeddings                       vision encoder
     │                                  │
     └──────────────┬───────────────────┘
                    ▼
               representation
                    │
                    ▼
              Transformer /
            multimodal processing
                    │
                    ▼
             next-token or
             output prediction
                    │
                    ▼
              decoding / output
                    │
                    ▼
                  ANSWER
```

And behind that pipeline is a longer history:

```text
sequence modeling
      ↓
RNN / LSTM era
      ↓
attention
      ↓
Transformer
      ↓
encoder / decoder variants
      ↓
large-scale pretraining
      ↓
LLMs
      ↓
vision-language connections
      ↓
VLMs
      ↓
audio + video + multimodal systems
```

That is the story this guide is trying to make intuitive.

---

## The most important things to remember

You do not need to remember every model name, every paper or every formula.

Remember these relationships:

### Transformer is an architecture, not a synonym for LLM.

An LLM is a large-scale language model. A Transformer is an architectural idea that many models use.

### Self-attention, multi-head attention and cross-attention describe different things.

They are not three consecutive product generations.

### Encoder-only, decoder-only and encoder-decoder are architectural choices.

They reflect different ways of using Transformer components for different tasks.

### An LLM turns text into representations and repeatedly predicts output tokens.

The answer is generated step by step through the decoding loop.

### A VLM has to solve one extra problem.

It needs to turn visual information into a representation that the language side can use.

### There is no single VLM architecture.

Projectors, adapters, cross-attention and more integrated multimodal designs are all possible.

### Audio and video are not merely extra file types.

They carry their own structure — especially time — and need suitable representations.

### Model families are ecosystems, not architecture labels.

GPT, Claude, Gemini, Llama, Qwen, Mistral and DeepSeek can each contain different generations, variants and modalities.

### Parameter count is not a quality score.

Training data, architecture, post-training, inference, modality support and task fit all matter.

### The best starting question is always the problem.

```text
What am I trying to build?
        ↓
What information does the model need?
        ↓
How should that information be represented?
        ↓
How should the representations interact?
        ↓
What output do I need?
        ↓
What constraints do I have?
```

Once you can answer those questions, the model names become much easier to understand.

---

# Appendix A — Quick reference

For a compact reference version of the models, families, architectures, and comparisons covered in this guide, see **[MODEL_GUIDE.md](MODEL_GUIDE.md)**.

The main README is the story. The model guide is the cheat sheet.

---

# Appendix B — Small glossary

### Token
A model-specific unit of text used as input/output pieces.

### Embedding
A learned vector representation used to turn discrete or other inputs into numerical representations the network can process.

### Attention
A mechanism for computing how strongly one representation should use information from other representations.

### Self-attention
Attention where the relevant representations come from the same sequence/stream.

### Cross-attention
Attention that connects different representation streams.

### Transformer
An architecture family centered on attention and related building blocks.

### LLM
A large-scale language model. The term does not define one fixed architecture.

### VLM / LVLM
A vision-language model/system connecting visual information and language. Terminology varies across the literature.

### Multimodal model
A model that works with more than one modality, such as text, image, audio or video.

### Vision encoder
A neural component that converts visual input into learned representations.

### Projector / adapter
A learned bridge that maps one representation space into another.

### MoE
Mixture-of-Experts: a sparse architecture in which routing selects a subset of expert parameters for an input.

### Quantization
A numerical representation technique used to reduce storage and/or computation, often with a quality trade-off.

### Context window
The amount of input/context a model can process under a particular model and configuration.

### Inference
Using a trained model to produce outputs.

### Pretraining
Large-scale training that builds broad capabilities.

### Post-training
Later training stages that shape instruction following, preferences, safety or other behaviors.

---

# Appendix C — A simple learning path

Read the main story once before going deep into formulas.

Then revisit it in this order:

```text
1. Language model
2. RNN / LSTM motivation
3. Transformer
4. Attention
5. Encoder / decoder shapes
6. LLM and autoregressive generation
7. Tokenization
8. Training and post-training
9. Vision-language connection
10. VLM architectures
11. Audio / video
12. Model families and architecture reading
```

For research reading, start with the original Transformer, BERT, GPT-3, ViT, Flamingo, LLaVA and Whisper papers. Then move to current official model documentation when studying active model families.

---

# References

See **[REFERENCES.md](REFERENCES.md)** for the full annotated source list.

The source policy is deliberately strict:

1. Use the original research paper for historical and architectural claims whenever possible.
2. Use an official technical report or model paper for a specific model family.
3. Use official documentation for current model names, capabilities, APIs and availability.
4. Use secondary material only when it adds context that is not better provided by a primary source.

---

## Repository structure

```text
LLM-VLM-Guide/
├── README.md
├── MODEL_GUIDE.md
├── REFERENCES.md
├── LICENSE
└── assets/
    ├── 01-before-transformer.svg
    ├── 02-transformer-anatomy.svg
    ├── 03-attention.svg
    ├── 04-three-architectures.svg
    ├── 05-text-input-pipeline.svg
    ├── 06-generation-loop.svg
    ├── 17-image-to-answer.svg
    ├── 18-audio-video.svg
    ├── 09-family-landscape.svg
    ├── 10-model-generations.svg
    └── 11-model-selection.svg
```

## License

The written material and diagrams in this repository are provided under the [MIT License](LICENSE) unless a referenced source or third-party asset has its own terms. Names and trademarks belong to their respective owners.

