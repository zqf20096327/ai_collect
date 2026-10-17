<p align="center">
  <a href="https://github.com/TetiAI/memraw">
    <img src="docs/images/banner.svg" width="820px" alt="memraw — no vectors, no retrieval; the whole memory, in the prompt">
  </a>
</p>

<h3 align="center">Probably impossible. Possibly inevitable.</h3>
<p align="center">
  An open experiment in memory for AI agents — the whole memory, always in the prompt.
</p>

Most memory systems assume context is scarce, so they embed, rank and retrieve.
memraw bets the other way: windows keep growing and prompt caching keeps getting
cheaper, so maybe you can skip retrieval entirely. Conversations get distilled
into dense, **importance-scored** fact lines; when the memory fills up, the
least important go first — forgetting by importance, not by age. Maybe we're
wrong about where this is all going — forecasting the future has a terrible
track record. But someone should be waiting at the door when it knocks, so here
we are: early, chairs set up, snacks ready, saving everyone a seat.

- **No embeddings, no vector DB, no infra of its own.** A memory is one
  plain-text string, kept wherever you already keep data. Zero dependencies;
  the only external call is the LLM your agent already uses.
- **Reading can't fail** — there is no retrieval step to miss. Multi-hop,
  temporal and negation queries come for free; the open question is write time,
  and that's what [the evals](evals/README.md) measure.
- **Forget by importance, not by age.** Every fact carries a 1–9 score; trivia
  dies first, identity never. An explicit `forget()` deletes on demand - or `"*"` to wipe it all. 
- **Prompt-cache friendly**: adds only append, so the document is a byte-stable
  prefix.
- **Inspectable**: a diffable text file in your own language, not rows in
  someone else's database.

```
<memory v="7" u="2026-07-09T16:40">
9 2026-07-05T16:40 name Alice, CTO at Acme               ← edge: read best
8 2026-07-05T16:40 celiac, Swedish origin
5 2026-07-08T09:05 set the launch for 2026-09-15
1 2026-07-09T14:20 the office coffee is nice             ← middle: trivia
5 2026-07-09T14:20 uploaded pricing deck https://acme.co/pricing.pdf
9 2026-07-09T16:40 prefers concise answers               ← edge: read best
</memory>
```

Each line: a 1–9 **importance** digit, the **insertion timestamp** (a date the
fact refers to just lives in the text), then the fact in plain language — the
owner in first person, other people by name. New facts append at the bottom.
And the same memory through `narrate()` — complete prose, capped at 50% of the
facts, generated on demand and never stored back:

```
Alice, CTO at Acme, is celiac and of Swedish origin. The office coffee is
nice. She set the launch for September 15 — pricing deck at
https://acme.co/pricing.pdf — and prefers concise answers.
```

## Install & use

```bash
npm install memraw        # zero dependencies
```

```ts
import { Memraw } from "memraw";

const memraw = new Memraw({
  llm: { apiKey: "<YOUR_API_KEY>", model: "google/gemini-2.5-flash", baseUrl: "https://openrouter.ai/api/v1" },
  budget: 100_000, // total tokens; ~10-20% of your model's window
});

let memory = ""; // load it from wherever you keep it ("" for a new one)

// a plain fact…
({ memory } = await memraw.add(memory, "Alice is CTO at Acme, gluten-free"));

// …or a WHOLE conversation: the model keeps only what's worth remembering
({ memory } = await memraw.add(memory, {
  topic: "kickoff call",
  messages: [
    { role: "user", content: "I'm Alice, CTO at Acme — let's plan the launch", at: "2026-07-08T09:00" },
    { role: "assistant", content: "Great — when do you want to ship?", at: "2026-07-08T09:01" },
    { role: "user", content: "September 15th. Deck is at https://acme.co/pricing.pdf", at: "2026-07-08T09:02" },
  ],
}));

({ memory } = memraw.consolidate(memory));   // valley-reorder (pure code) — run when YOU choose
const profile = await memraw.narrate(memory); // prose view, never stored back

// save `memory` anywhere — file, DB row, S3. To use it: drop the whole
// string into your system prompt. That's the entire read path.
```

Storage is yours (`FsStore` / `MemStore` helpers included — or implement the
5-method `MemoryStore` interface). There's also a CLI (`memraw add|show|context`)
and an MCP server for Claude Code / Cursor
(`{ "mcpServers": { "memraw": { "command": "npx", "args": ["memraw-mcp"] } } }`),
both reading the same env:

```bash
OPENROUTER_API_KEY=<YOUR_API_KEY> # or OPENAI_API_KEY / LLM_API_KEY
LLM_MODEL=google/gemini-2.5-flash
MEMRAW_DIR=~/.memraw             # storage root (fs adapter)
```

Any OpenAI-compatible endpoint works. Without a key memraw still runs: adds are
stored raw — only distillation and importance scoring need an LLM. Full API in
[GUIDE.md](docs/GUIDE.md).

## Why the memory is shaped like a valley

LLMs read a long context unevenly: strong at the **start** and the **end**, weak
in the **middle** — the "lost in the middle" effect
([Liu et al. 2023](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf)).
So `consolidate()` arranges the list as a **valley** — importance mirrors the
attention curve:

![The valley: LLMs read the start and end of the context best, so memraw puts the most important facts at the edges and trivia in the middle](docs/images/valley.svg)

It's pure code, and **manual by design**: reordering rewrites the document and
invalidates the prompt cache, so you run it when *you* choose — not on every
add. The prose follows the same curve — it opens with identity, buries trivia
mid-story, and closes with what matters:

![The narrated prose follows the same valley: it opens with identity, buries trivia mid-story, and closes with what matters](docs/images/prose-valley.svg)

Same rule, same reason: LLMs read the edges best, so the edges carry the most.
The research behind every format rule is in [SPEC.md](SPEC.md).

## How it performs (so far)

Honest numbers: everything below comes from **one LOCOMO conversation** and
points a direction, nothing more ([details & limitations](evals/README.md)).
19 sessions of dialogue → a memory of **11,076 tokens** (1.5x compression —
benchmark dialogue is nearly all facts; real chatty conversations compress far
more). The SAME memory, and its prose view (**4,426 tokens, 40% of the facts**),
read by six models on 58 balanced questions, judged by a fixed external judge
(`gpt-4o`):

| reader model | facts (11,076 tk) | prose view (4,426 tk) |
|---|---|---|
| gemini-2.5-flash-lite | 56.9% | 55.2% |
| gemini-2.5-flash | 63.8% | 63.8% |
| gemini-2.5-pro | 65.5% | 56.9% |
| gemini-3.1-pro-preview | 67.2% | 65.5% |
| glm-5.2 | 70.7% | 60.3% |
| gpt-5 | **75.9%** | **69.0%** |

Two takeaways. **The same memory scores 56.9% → 75.9% just by swapping the
reader** — memraw has no index or pipeline of its own to bottleneck on, so
every model generation lifts it for free, at write time and at read time. And
**the prose holds close to the facts at 40% of the tokens** — the facts never
lose, but both formats rise together with the model. Promising.

## The fact economy

A fact is one dense line — **~30 tokens**. Capacity is arithmetic: budget ÷ 30.
The rule: the memory takes **10–20% of the model's window**, the rest stays free
for the conversation.

| model window | memory budget (10–20%) | facts held hot | prose view (≤50%) |
| ------------ | ---------------------- | -------------- | ------------------ |
| 128k         | 13k–26k               | ~430–870      | ≤6.5k–13k tokens  |
| 1M (flash)   | 100k–200k             | ~3,300–6,700  | ≤50k–100k tokens  |
| 10M          | 1M–2M                 | ~33,000–67,000 | ≤500k–1M tokens   |

3,000+ facts already hot is far past what a single user accumulates in years —
on models that exist **today**. And memraw rides two curves that only go up:
better models → the same budget holds a more accurate memory; bigger windows →
more facts stay hot, eviction fires later or never.

## Where we think memory ends up

Today agent memory lives in a **vector database**, fetched by a *stop-and-fetch*
loop: pause, embed, search, paste, then speak. memraw moves it into the
**prompt**, always present. We think the final step is memory living **inside
the model itself** — research already points there (retrieval fused into the
forward pass — RETRO, kNN-LM; trainable memory layers; test-time memory modules
like Titans): models generating with a memory index inside the network,
association resolved per token, the way a memory *surfaces* while you speak. If
that happens, the durable asset is holding memory in a form a model can absorb
— atomic, dense, dated facts: units of thought, ready to be indexed.

And it is **not a bet against prose** — memraw renders prose on demand, and our
numbers show that view holding close to the facts at 40% of the tokens. It's a
bet on which form is the **source**: facts → prose is a lossless render you can
produce anytime; prose → facts drops something at every rewrite. Storing facts
keeps both futures open. That's why memraw **compresses to facts and narrates
to prose**.

## Docs

- [PAPER.md](PAPER.md) — the working notes: full reasoning, design decisions, lessons learned.
- [GUIDE.md](docs/GUIDE.md) — full usage guide: mental model, API, config, CLI, MCP, storage.
- [SPEC.md](SPEC.md) — the on-disk format and the research behind each rule.
- [evals/README.md](evals/README.md) — benchmarks, methodology, honest limitations.

## Status

**This is an experiment, not a product.** memraw (v0.0.1) is us trying an idea
in the open — expect rough edges and breaking changes; the format spec is the
most stable part. Roadmap: Postgres adapter, richer LOCOMO harness, smarter
eviction. Contributions, holes in the idea, and better benchmarks all very
welcome.

## License

[Apache 2.0](LICENSE) © TetiAI LLC
