# HybridRAG

**Does adding a knowledge graph to RAG actually help, or does vector search cover it?**

This notebook answers that by running the same corpus and the same questions through three retrieval configurations and comparing the answers side by side.

Short version: vector search handles "what is X" fine and falls over on anything relational or ordinal. Graph traversal fixes exactly that class of question.

---

## The finding

Same corpus, same model, same question. Only the retrieval changes.

> **"Who came second in 2023?"**

| Retrieval | Answer |
|---|---|
| Vector only | *"Unfortunately, I don't have information about the results of the Formula One World Championship for 2023."* |
| Vector + keyword | *"I don't know that information."* |
| **Vector + graph** | *"According to the text, Sergio Pérez secured second place in the Drivers Championship in 2023."* |

The answer was in the corpus the whole time. Vector retrieval could not surface it, because "came second" is a position in an ordered relationship rather than a phrase that embeds close to anything in the source text. Graph traversal reaches it because the ordering is an edge, not a sentence.

The same pattern shows on identity and affiliation questions:

| Question | Vector only | Vector + graph |
|---|---|---|
| Who is Max Verstappen? | *"likely refers to a question about the performance or skills of Max Verstappen"* | *"Dutch Formula One racing driver. Currently drives for Red Bull Racing-Honda RBPT, reigning World Drivers' Champion since 2022."* |
| Who won the 2023 championship? | not retrieved | *"Max Verstappen, driving for Red Bull Racing-Honda RBPT."* |

One failure worth calling out on its own. Asked to compare drivers and teams across 2022 to 2024, the vector only chain answered with the phrase **"According to my training data"** and produced a summary from the model's weights rather than from the retrieved context. That is the failure mode RAG exists to prevent, and it does not announce itself: the answer reads fine and is not grounded in anything.

---

## Architecture

Three configurations, built up in order.

**1. Vector RAG.** PDFs are chunked at 1000 characters, embedded with `llama3.2` through Ollama, and stored in a local Neo4j instance as vectors. A similarity retriever pulls the top 5 chunks into a LangChain `RetrievalQA` chain.

**2. Vector + keyword.** The same chunks indexed with Neo4j's hybrid search, combining vector similarity with a full text keyword index over the `Chunk` nodes. This is still unstructured retrieval, just with lexical matching added.

**3. Vector + graph.** Two retrievers running against the same question:

- **Structured retriever.** A Gemini call with Pydantic structured output extracts person and organization entities from the question. Each entity is turned into a fuzzy full text query with a two character edit distance tolerance, so misspellings still resolve. Matching nodes are looked up in a full text index, and a Cypher query walks their neighborhood in both directions, excluding `MENTIONS` edges, capped at 50 relationships.
- **Unstructured retriever.** Vector similarity over the chunk embeddings, as above.

Both results are concatenated into a single context block, labeled by source, and passed to the LLM with the question.

```
question
   ├──> entity extraction (Gemini, structured output)
   │       └──> fuzzy full text lookup ──> neighborhood traversal (Cypher)
   └──> vector similarity (Ollama embeddings)
                 └──> combined context ──> llama3.2 ──> answer
```

---

## Stack

| Component | Choice |
|---|---|
| Orchestration | LangChain |
| Vector store | Neo4j (local) |
| Knowledge graph | Neo4j Aura |
| Embeddings and generation | `llama3.2` via Ollama |
| Entity extraction | `gemini-pro` with structured output |
| Graph construction | Neo4j `llm-graph-builder` with Gemini 1.5 |
| Corpus | Wikipedia articles on Formula 1 championships (PDFs in `/data`) |

The knowledge graph came out at **5,364 nodes and 37,055 relationships**.

A note on how the graph was built. The original plan was to construct it in code with LangChain's `LLMGraphTransformer`, which did not work against Gemini, the only free option available at the time. The graph was built instead with Neo4j's hosted `llm-graph-builder` tool. That step is therefore manual and is not reproducible from this repo alone.

---

## Running it

1. Start a local Neo4j instance for the vector store, and a Neo4j Aura instance for the knowledge graph.
2. Install and run Ollama with `llama3.2` pulled.
3. Set `NEO4J_AURA_URL`, `NEO4J_AURA_USERNAME`, `NEO4J_AURA_PASSWORD`, and `GOOGLE_API_KEY`.
4. Put source PDFs in `./data`.
5. Build the knowledge graph from those PDFs using [llm-graph-builder](https://llm-graph-builder.neo4jlabs.com/) and point it at the Aura instance.
6. Run `rag.ipynb` top to bottom.

---

## What this is and is not

It is a worked comparison. Each stage is built up in the notebook with the reasoning written out, and the same questions are re-run at each stage so the difference in retrieval is visible in the answers rather than asserted.

It is not an evaluated benchmark. The comparison is qualitative. There is no recall or answer accuracy measured over a labeled question set, so the claim here is "this class of question fails one way and succeeds the other," not a number.

Known gaps, in rough priority order:

- **No quantitative evaluation.** The honest next step is a labeled question set split by type, relational against factual, scored per configuration.
- **Graph construction is a manual step** through a hosted tool rather than code in this repo.
- **Two Neo4j instances** are needed, one local and one Aura, which is an artifact of how the project grew rather than a design choice.
