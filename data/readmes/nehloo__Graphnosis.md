<div align="center">
  <img src="public/graphnosis-logo-550x550.png" alt="Graphnosis logo" width="180"/>

# Graphnosis

**Memory for AI harnesses that recalls a multi-graph, not a .md file or RAG chunks and a shrug.**

</div>

<div align="center">

[![npm](https://img.shields.io/npm/v/@nehloo/graphnosis?style=flat&color=cb3837&logo=npm)](https://www.npmjs.com/package/@nehloo/graphnosis)
[![Benchmark](https://img.shields.io/badge/LongMemEval-local%20r45%2077.60%25-8a8f98?style=flat)](benchmarks/benchmarks.md)
[![.gai Format](https://img.shields.io/badge/.gai-Format%20Spec-5b3fd1?style=flat)](SPEC.md)
[![Paper](https://img.shields.io/badge/paper-10.5281%2Fzenodo.20843387-4a7ebb?style=flat)](https://doi.org/10.5281/zenodo.20843387)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

</div>

## See it in ten seconds

```bash
npx -y @nehloo/graphnosis@latest demo
```

Opens a 3D graph of a sample corpus in your browser. Ask it a question and watch
the retrieval walk light up. No install, no API key, no network.

Point it at your own files instead:

```bash
npx -y @nehloo/graphnosis@latest demo ./my-vault-notes
```

Arrowheads mark **directed** edges — typed logic that points somewhere
(`causes`, `precedes`, `supersedes`, `contains`). Plain lines are **undirected**
association (`similar-to`, `shares-entity`, `co-occurs`). Both layers sit on the
same nodes and are walked together. That is the whole idea, and it is easier to
see than to read about.

Cloned the repository instead? A clone has no `dist/` until you build it — see
[Build from source](#build-from-source).

---

## Use it from any language

```bash
npx -y @nehloo/graphnosis@latest serve ./my-vault-notes
```

```bash
curl localhost:7777/query -d '{"q":"why did the deploy fail?"}'
```

Plain HTTP, so Python, Go, Ruby and curl all work. The same binary is also an MCP
server (`npx -y @nehloo/graphnosis@latest mcp`), which Claude Desktop, Cursor and Zed
connect to with one config block.

> **On other languages.** There is one implementation of the engine, on purpose.
> Retrieval from a fixed graph is deterministic — the same `.gai` and question
> give the same subgraph — and independent ports are the fastest way to lose that,
> because tie-breaking, hash iteration order and Unicode handling all differ
> subtly between runtimes. Cold ingest that enables optional LLM summaries is not
> deterministic unless those generated summaries are pinned. So other languages
> get a process boundary, not a rewrite.

---

## Use it as a library

```bash
npm install @nehloo/graphnosis
```

```ts
import { Graphnosis } from '@nehloo/graphnosis';

const g = new Graphnosis({ name: 'incident' });
g.addText('The checkout deploy failed on Tuesday because the orders migration timed out.', 'deploy-log.md');
g.addText('The orders migration timed out because the index on customer_id was missing.', 'postmortem.md');
g.addText('We added the missing index on customer_id the following morning.', 'followup.md');
g.build();

console.log(g.query('why did the checkout deploy fail?').subgraph.serialized);
```

```
=== KNOWLEDGE SUBGRAPH (4 nodes, 3 edges) ===

--- NODES ---
[n1|fact|0.49|src:deploy-log.md] The checkout deploy failed on Tuesday because the orders migration timed out.
[n3|fact|0.11|src:postmortem.md] The orders migration timed out because the index on customer_id was missing.
[n4|fact|0.04|src:followup.md] We added the missing index on customer_id the following morning.

--- DIRECTED ---
n2 -[contains:1.0]-> n1

--- UNDIRECTED ---
n1 ~[similar-to:0.4]~ n3
n3 ~[similar-to:0.5]~ n4
```

A vector store would return three passages ranked by similarity and leave the
model to guess how they relate. Here the failure, the root cause and the remedy
are linked, and the model is told so.

```ts
const prompt = g.prompt('why did the checkout deploy fail?');
// a system prompt containing that subgraph — send it to Claude, GPT, Ollama,
// Bedrock. Graphnosis never makes the call itself.
```

> Give each source its own `sourceFile`. Repeating one across several `addText`
> calls collides chunk keys and retrieval returns nothing.

---

## Graphnosis — Agentic Multi-Graph for AI

<div align="center">
  <img src="docs/screenshots/graphnosis-agentic-multi-graph-gai.png" alt="Graphnosis agentic multi-graph: directed and undirected edges over one node set, rendered from a .gai file" width="100%"/>
</div>

One node set, two edge classes, walked together. What that picture holds, and
what a folder of `.md`, a vector index, or a conventional graph database each
cannot give you:

**Two co-equal edge layers, not one.** Directed edges carry typed logic —
`causes`, `precedes`, `supersedes`, `contains`. Undirected edges carry
association — `similar-to`, `shares-entity`, `co-occurs`. Both are independently
queryable classes over the same nodes, and one BFS walks them together. A
property graph makes you commit to a schema first; RAG has no edges at all.

**Retrieval returns a subgraph, not a ranked list.** The model receives the facts
*and* the relations between them, serialized. A vector store returns passages by
cosine distance and leaves the model to guess how they connect.

**The same question gives the same subgraph.** Retrieval from a fixed graph is
deterministic — one `.gai`, one question, one answer shape, every time. No
temperature, no index drift, no re-embedding between runs.

**Contradictions surface instead of merging.** Conflicting facts are reported as
a conflict for the owner to adjudicate. Appending to a `.md` file keeps both
silently; a vector store silently returns whichever ranked higher.

**Memory ages.** Nodes carry `createdAt`, `lastAccessedAt`, `accessCount`,
`validUntil` and a confidence that decays with disuse. Superseded facts retire
without being destroyed. Flat files and vector chunks have no notion of stale.

**It is one portable file you own.** A `.gai` is bytes on your disk — copy it,
back it up, move it between machines, diff it. No server, no vector database, no
account.

**The body is not encrypted, so treat it as you would the source documents.** A
`.gai` holds the memories in the clear; `strings` on one prints them. HMAC
signing proves a file came from the holder of the key and was not modified — it
does not stop anyone from reading it. Encrypt before committing one to a
repository or sending it anywhere, and see [`SPEC.md`](SPEC.md) §4 for what the
format does and does not guarantee. The single-file design that makes a `.gai`
easy to move is the same property that makes an unencrypted one easy to leak.

**No API key, no network.** Lexical retrieval is the default and runs entirely
on-device. Embeddings and LLM summaries are optional paths, not the price of
entry.

None of these are implementation preferences. They are the properties the
substrate paper sets out and this library implements — the co-equal dual graph,
the deterministic owner-adjudicated contradiction contract, and the indelibility
and order-independent merge guarantees.

What that means for agentic graph engineering: memory stops being a probabilistic
index you hope returns the right chunk, and becomes a substrate you can reason
about before you run it. That reduces to five requirements a memory layer either
meets or does not — independent of control flow, so a loop and a graph are judged
by the same five.

**§1 Provenance.** Every fact traces back to where it came from. Nodes carry
their `src:` through retrieval, so any claim in the returned subgraph walks back
to the file that produced it. An agent that cannot cite cannot be audited.

**§2 Indelibility.** Nothing is silently overwritten — contradictions are kept
and owner-adjudicated. Supersession is an edge rather than a delete, so you can
still ask what the agent knew at the moment it acted, after it has learned
otherwise.

**§3 Determinism.** The same question gets the same answer, twice. A bad
retrieval is reproducible, which is the difference between debugging an agent and
re-rolling it. Order-independent merge extends this across writers: two agents
recording the same facts in different orders converge on the same graph, so
concurrent and resumed sessions do not drift apart.

**§4 Capped authority.** What proposes an action never approves its own limits.
The engine reports a conflict; it never picks the winner. Retraction is a soft
delete the owner can reverse, and the optional LLM passes enrich — they are never
the writer of record.

**§5 Co-location.** Memory, skills, and agents live in one place, as one
structure. This library is the substrate half: one `.gai` holding the facts and
the relations between them, with no second index to keep in sync. The procedural
half — skills held as subgraphs in that same store — is the subject of the
[second preprint](#the-desktop-app--a-use-case-for-this-library) and ships in the
desktop app.

To measure that, we wrote a preprint paper: **The Un-Brain**, CC BY 4.0 on Zenodo —
[10.5281/zenodo.20843387](https://doi.org/10.5281/zenodo.20843387)

<div align="center">
  <img src="docs/screenshots/grounded-eng-card-five-requirements.png" alt="A framework for Grounded Engineering — five requirements: provenance, indelibility, determinism, capped authority, co-location" width="100%"/>
</div>

---

## What you get that a vector store does not

### Contradictions are reported, not silently merged

```ts
const g = new Graphnosis({ name: 'policy' });
g.addText('The Acme Corporation service agreement sets the API rate limit for the Reporting endpoint at 1000 requests per minute.', 'contract-2024.md');
g.build();

const res = g.appendText(
  'The Acme Corporation service agreement was corrected: the Reporting endpoint rate limit is no longer 1000 requests per minute.',
  'contract-2025.md',
);

res.contradictions.length;          // 1
res.contradictions[0].sharedEntities; // ['The Acme Corporation', 'Acme', 'Corporation', 'Reporting']
```

**Nothing is resolved for you.** The new passage is ingested like any other, and
the old node is left exactly as it was — not retired, not rewritten, not merged
away. You are told there is a conflict and you decide: supersede, keep both, or
reject. A vector store has no place to put that decision, so it silently keeps
both and lets ranking pick a winner per query.

> Detection is deliberately conservative: two or more shared strong entities,
> both passages over 60 characters, and an explicit conflict marker (`corrected`,
> `no longer`, `superseded`, `disputed`, …). A bare numeric flip with no marker
> is missed. A false contradiction is worse than a missed one.

### Changing how much a memory counts is not the same as changing it

Lowering confidence in a fact used to mean rewriting it, which loses the old
version. `setConfidence` moves only the number:

```ts
g.setConfidence(nodeId, 0.3, 'contradicted by the incident review');
```

Same id, same content, same hash, same edges, same liveness — plus an audit stamp
saying who moved it and why. The receipt is derived from the graph *after* the
write, so it cannot disagree with what actually happened. `setConfidences` does a
batch in one pass.

### When a load fails, you can tell why without reading the message

Failures carry a stable `code` and a class, so you can branch on the class rather
than substring-matching prose:

```ts
import { isCorruption, isVersionSkew } from '@nehloo/graphnosis';

try { g.fromBuffer(bytes); }
catch (e) {
  if (isVersionSkew(e)) return 'written by a newer Graphnosis — update to open it';
  if (isCorruption(e))  return 'the file is damaged — recover from a backup';
  throw e;
}
```

The distinction matters more than it looks: a file written by a *newer* version
is perfectly intact, and treating that as corruption quarantines good data. The
message strings are frozen and tested, so existing substring classifiers keep
working — but the codes are what to build on.

### The memory is a file you own

```ts
const buf = g.toBuffer();      // .gai — msgpack, magic 'AIKG', checksummed

const restored = new Graphnosis({ name: 'notes' });
restored.fromBuffer(buf);      // instance method, not static
```

Nodes, typed edges, provenance and timestamps. Optional HMAC-SHA256 if you want
it tamper-evident. Write it to disk, put it in S3, ship it in a Lambda, hand it
to a colleague. [Format spec →](SPEC.md)

### A fixed graph gives the same subgraph

Retrieval writes nothing, and ranking depends only on the serialized graph state
plus the query — so two queries against the same `.gai` can be diffed and any
difference is a real change. The one clock it reads is retirement: a node is
excluded once its retirement instant has passed, which is why a graph holding
retired or time-bounded content answers differently tomorrow.

Pass `asOf` to remove that clock and get a fixed view:

```ts
const t = Date.parse('2026-01-01T00:00:00Z');
g.query('why did the checkout deploy fail?', { asOf: t });   // same answer, forever
```

With `asOf` set, no clock is read anywhere in the read path, so the same question
against an unchanged graph returns the same answer today, in CI, and in a year.
It is the whole determinism story in one option — before it, you had to know to
set two independent fields to the same value, one of which defaulted to the wall
clock and the other to unset.

An explicitly passed `now` or `retiredAt` still wins over `asOf`, so
`{ asOf: t, retiredAt: 0 }` is the audit view: rank as of `t`, with the
retirement gates off entirely. Optional LLM enrichment during a fresh ingest is a
separate, generative step.

---

## Five minutes

<details><summary><b>Load real files</b></summary>

```ts
await g.appendFile('./docs/architecture.md');   // auto-detects format
await g.appendFolder('./docs');
await g.appendPdf(readFileSync('spec.pdf'));    // pdf, csv, json, html too
```
`add*` builds a graph; `append*` adds to one that already exists. Calling
`append*` before `build()` fails.
</details>

<details><summary><b>Semantic retrieval (optional, needs an API key)</b></summary>

```bash
npm install ai @ai-sdk/openai
```
```ts
import { openaiEmbedAdapter } from '@nehloo/graphnosis/adapters/openai';

await g.buildEmbeddings({ adapter: openaiEmbedAdapter() });  // reads OPENAI_API_KEY
const r = await g.queryHybrid('what broke last week?');
```
`ai` and `@ai-sdk/openai` are peer dependencies, and the adapter is required —
without one `buildEmbeddings()` throws before it reaches the network. TF-IDF
works with zero network access; embeddings are opt-in and additive.
</details>

<details><summary><b>Persistence</b></summary>

```ts
g.saveGai('memory.gai');   g.loadGai('memory.gai');
const buf = g.toBuffer();  // serverless-friendly, no filesystem

// SQLite is an optional backend — `better-sqlite3` is an optionalDependency,
// so install it if your platform skipped the native build. Loading needs the
// graph id as well as the file, because one database can hold several graphs.
g.saveSqlite('memory.db');
g.loadSqlite('memory.db', 'incident');
```
</details>

<details><summary><b>Non-English corpora</b></summary>

```ts
import { unicodeAnalyzer } from '@nehloo/graphnosis';
const g = new Graphnosis({ name: 'ro', analyzer: unicodeAnalyzer });
```
The default folds diacritics and strips English stopwords. `unicodeAnalyzer`
preserves diacritics where they are phonemic.
</details>

<details><summary><b>Corrections and forgetting</b></summary>

```ts
g.supersede(oldNodeId, 'The rate limit is now 500 rpm.', 'contract renegotiated');
g.forgetTopic('deprecated-api');
g.forgetBefore(Date.parse('2024-01-01'));    // milliseconds, not a Date
const audit = g.reflect();   // contradictions + discovery in one pass

g.retired();                 // everything you have forgotten, still readable
```

**Forgetting is not erasure.** A retired node keeps its content, its id, its
edges and its provenance — it is excluded from every prompt and from nothing
else, and `retired()` is the audit surface that makes that checkable. An empty
result there means nothing has been retired, never that something was
destroyed. Retiring by `supersede` also blocks the source from re-introducing
the corrected-away text on the next sync; retiring by `delete` does not, so
re-adding a file restores it.
</details>

---

## Is this for you?

**Yes** — if you are building an agent that needs memory across sessions, you
want relationships between facts rather than nearest neighbours, you need the
answer to be reproducible, or you want the memory to be a portable file.

**Probably not** — if you want a hosted memory service, your corpus is one
document, or plain semantic search already answers your questions. Use a vector
store; it is simpler and it fits.

**Known limits.** Contradiction detection is pattern-based and misses conflicts
with no explicit marker. Retrieval is lexical by default, so a question sharing
no vocabulary with its source needs the embedding path. Identity extraction
still treats two capitalised words in content as a possible person, so
organization names can be false positives; structural headings are excluded.
Published npm (`0.12.0`) still has no replacement for the historical 78.00%
figure. A local best-first re-measure on this line (r45) landed at **77.60%** —
not a beat of 78/79; FIFO control + a best-first arm with the 0.12.0 retrieval
levers are still open before any current claim. The table below reports what is
published and reproducible — good, not solved.

---

## Benchmark

**No published current headline yet.** Historical **78.00%** (Run 30) is
FIFO-era evidence on an older line. Local **r45 = 77.60%** is best-first on the
post-retirement line and is **not** cited as beating 78/79. A FIFO control and a
best-first arm with 0.12.0 levers (`selectEvidence`, preference-lane fix)
still need to land — see
[`benchmarks/benchmarks.md`](benchmarks/benchmarks.md) and
[`CONTRIBUTING.md`](CONTRIBUTING.md) (“Engine progress”).

What is published and reproducible today, from earlier release lines:

| arm | score |
|---|---|
| historical single-run best: dual-graph + router + summaries + preferences | 78.00% |
| same, embeddings removed (TF-IDF only) | 64.60% |
| flat top-k, identical seed pool | 49.00% |
| fully on-device (Llama 3.2 3B, zero cloud) | 41.60% |

Those rows ship as raw run artifacts in
[`benchmarks/evidence/`](benchmarks/evidence/), and
`node benchmarks/evidence/verify.mjs` recomputes each one and exits non-zero if
any disagree. They are a single run each on an older line — read them as
evidence that the ablations separate, not as a current score.

---

## Build from source

The published package ships a prebuilt `dist/`. A clone does not — `dist/` is
generated, never committed — so build it once before the CLI will run:

```bash
git clone https://github.com/nehloo/Graphnosis.git
cd Graphnosis
npm install
```

`npm install` runs the `prepare` script, which runs `npm run build:lib` and
writes `dist/`. There is no separate build step to remember. Then run the CLI
from your clone:

```bash
node dist/cli/index.js demo
```

Rebuild after editing anything under `src/` — or if you installed with
`--ignore-scripts`, which skips `prepare`:

```bash
npm run build:lib
```

To put the `graphnosis` command on your PATH, pointed at your clone:

```bash
npm link
```

> **`npx` will not run your clone.** Inside the repository,
> `npx -y @nehloo/graphnosis@latest demo` still downloads the *published*
> release and runs that — a clone is not an installed dependency of itself, so
> `npx` finds nothing local and falls through to the registry. Use
> `node dist/cli/index.js` when you mean your own build.
>
> **Why every command above pins `@latest`.** Without it, `npx` will happily
> reuse an older copy it already has — one cached from an earlier run, or one
> sitting in a project's `node_modules`. If that copy predates the CLI, which
> arrived in **0.9.0**, you get `could not determine executable to run`, or
> `graphnosis: command not found`. Pinning `@latest` forces a fresh resolve
> against the registry.

---

## How it works

Documents are chunked into nodes. Two edge layers are built over the same node
set — **directed** for typed logic, **undirected** for association. A query seeds
into the graph lexically, walks both layers in one BFS with score decay, and
returns the subgraph.

Run `npx -y @nehloo/graphnosis@latest demo` and look at it; the picture explains the
rest faster than this section can.

---

## The Un-Brain research paper

A preprint, CC BY 4.0 on Zenodo.

**The Un-Brain** — the substrate this library implements: the co-equal dual graph
(directed and undirected edges as two independently queryable classes over one
node set), the deterministic owner-adjudicated contradiction contract, and the
indelibility and order-independent merge properties. It reports the retrieval
ablation the benchmark table above draws on.
[10.5281/zenodo.20843387](https://doi.org/10.5281/zenodo.20843387)

> Both papers, this one and the skills paper below, describe the wider
> Graphnosis system, of which this package is the engine. Parts they discuss
> that sit above the library — the MCP surface, encrypted sync — are separate
> repositories.

---

## The desktop app — a use case for this library

**[Graphnosis](https://graphnosis.com/download)** is a desktop application built
on this library. Source at
[nehloo-interactive/graphnosis-app](https://github.com/nehloo-interactive/graphnosis-app),
under the Functional Source License 1.1 (Apache-2.0 future) — a different licence
from this package.

The app’s product thesis is **personalize without fine-tuning**: steer connected
models with memory you own and skills (SOPs) you train — not by updating
foundation-model weights. Store truth, correct errors, train a workflow skill,
then recall or walk that skill before the answer. Guide:
[Personalize without fine-tuning](docs/personalize-without-fine-tuning.md).

A second preprint, also CC BY 4.0 on Zenodo, describes the mechanism the app
adds on top of the engine.

**Borrowable Skills as Lean Un-Ganglia Subgraphs** — procedures held as subgraphs
in the same store as the facts they operate on: trainable, composable,
bounded-loop SOPs co-located with memory, and borrowable across that store.
Continues the first paper.
[10.5281/zenodo.21205599](https://doi.org/10.5281/zenodo.21205599)

That is not a design you have to build yourself. It ships: train an SOP, walk it
a step at a time, watch it improve run over run, export it as a signed `.gsk`
pack. The [skills reference](https://graphnosis.com/reference/skills) documents
the behaviour the paper measures. Port the guide above to the app docs site when
ready (suggested URL path: `/guides/personalize-without-fine-tuning`).
