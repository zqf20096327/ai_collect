# id-legal-rag

> A retrieval-augmented generation pipeline for Indonesian legal documents — laws, court decisions, ministerial regulations.

I work with a small team that helps SMEs in Indonesia navigate compliance. The amount of legal text out there is wild — `peraturan.go.id` alone holds tens of thousands of laws and regulations, and `putusan.mahkamahagung.go.id` (the Supreme Court decisions portal) keeps growing every week. Asking lawyers to grep through this manually is painful. So I started building a RAG over it. This repo is where I keep the working notebooks and a thin Python layer that I lift into production once something proves itself.

The model running on top is local — `ollama` with either `llama3.1:8b-instruct-q4_K_M` or `qwen2.5:7b-instruct` depending on which one is less hallucinatory that week. For Indonesian, `qwen2.5` has been winning recently.

## Architecture (current)

```
                     ┌─────────────────────────┐
                     │  peraturan.go.id (UU,   │
   scrapers/   ───▶  │  PP, Perpres, Permen)   │
                     │  putusan.mahkamahagung  │
                     │  .go.id (court rulings) │
                     └────────────┬────────────┘
                                  │
                                  ▼
                          ┌───────────────┐
                          │  PDF / HTML   │
                          │   cleaner     │  ── src/clean.py
                          └───────┬───────┘
                                  │
                                  ▼
                          ┌───────────────┐
                          │   chunker     │  ── src/chunk.py
                          │  (legal-aware │     keeps Pasal/Ayat
                          │   sectioning) │     boundaries intact
                          └───────┬───────┘
                                  │
                          ┌───────▼───────┐
                          │ sentence-     │  paraphrase-multilingual
                          │ transformers  │  -MiniLM-L12-v2 (fast)
                          │   embedder    │  OR e5-large (better, slow)
                          └───────┬───────┘
                                  │
                          ┌───────▼───────┐
                          │  FAISS index  │  IndexFlatIP
                          │  (+ metadata  │  + sqlite metadata
                          │   side-car)   │
                          └───────┬───────┘
                                  │
        user query ──▶ ┌──────────▼──────────┐
                       │  hybrid retriever   │  BM25 + dense ∪ rerank
                       └──────────┬──────────┘
                                  │
                       ┌──────────▼──────────┐
                       │  prompt builder     │  + Pasal citations
                       └──────────┬──────────┘
                                  │
                       ┌──────────▼──────────┐
                       │  ollama (local LLM) │  qwen2.5:7b / llama3.1:8b
                       └─────────────────────┘
```

Nothing fancy. The clever bits are:

1. **Legal-aware chunking** — Indonesian laws are organised into Bab → Bagian → Pasal → Ayat → Huruf. Splitting on token windows alone destroys the citation structure. `src/chunk.py` keeps each Pasal intact when possible.
2. **Hybrid retrieval** — BM25 dominates on exact-citation queries ("Pasal 1320 KUHPerdata"). Dense retrieval dominates on intent queries ("kalau kontrak tidak ditandatangani, apakah masih sah?"). The union with a cross-encoder rerank gives a real lift.
3. **Citation-grounded prompts** — the LLM is forced to return Pasal numbers, and we post-validate against the retrieved chunks. If it cites something we didn't retrieve, we reject.

## Why I care about AMD ROCm GPUs

Honestly, the embedding step and the local LLM are the bottleneck. Embedding ~50k legal documents (each chunked into 5–15 pieces) on a CPU is a non-starter; one full re-index on my workstation is 6+ hours. On an MI250 I can run the whole pipeline — embeddings on one GCD, ollama serving on the other — and re-index in under 20 minutes. The MI300X is even nicer for the LLM side because the 192 GB HBM lets me hold the 70B Qwen variant in a single device without weird offload tricks. The ROCm port of `llama.cpp` (which ollama uses) is in good shape now, and the price-per-hour on the AMD Developer Cloud is what makes this project sustainable for a self-funded effort — running an A100 24/7 for a side project isn't realistic. That's the honest reason.

## Repo layout

```
notebooks/
  01_scrape_peraturan.ipynb     # how I pull UU/PP from peraturan.go.id
  02_clean_and_chunk.ipynb      # Pasal-aware chunking walkthrough
  03_build_faiss_index.ipynb    # embedding + index construction
  04_hybrid_retrieval.ipynb     # BM25 ∪ dense + rerank experiments
  05_rag_eval.ipynb             # end-to-end QA evaluation
src/
  clean.py        # PDF -> text, footer/header stripping
  chunk.py        # legal-aware chunker
  embed.py        # sentence-transformers wrapper
  index.py        # FAISS build / query
  retrieve.py     # hybrid BM25 + dense + rerank
  llm.py          # ollama client + prompt templates
data/sample/     # 3 sample UU + 2 court decisions, redistributable
```

## Quickstart

```bash
# 1. env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. pull a local LLM via ollama
ollama pull qwen2.5:7b-instruct

# 3. run the notebooks in order, or:
python -m src.index --input data/sample --out indexes/sample.faiss
python -c "from src.retrieve import ask; print(ask('Apa syarat sah suatu perjanjian?'))"
```

## Data sources

| Source                              | What                              | Access     |
|-------------------------------------|-----------------------------------|------------|
| https://peraturan.go.id             | UU, PP, Perpres, Permen           | Public web |
| https://putusan.mahkamahagung.go.id | Supreme Court decisions           | Public web |
| https://jdih.kemenkeu.go.id         | Finance Ministry regs (good HTML) | Public web |

A few sample documents (public domain — Undang-Undang are not copyrighted under Indonesian law per UU Hak Cipta) are included in `data/sample/` so you can run the notebooks end-to-end without scraping.

## Notes / Open issues

- The chunker still breaks on UU with weird PDF layouts (looking at you, UU Cipta Kerja). Probably needs a layout-aware parser.
- BM25 over Bahasa Indonesia benefits from Sastrawi stemming; using it as the tokenizer in `rank_bm25` was a 4-point recall@10 jump.
- The reranker (`cross-encoder/ms-marco-MiniLM-L-6-v2`) is multilingual-adjacent but not Indonesian-tuned. There's a TODO to swap it for an mMARCO-id fine-tune.

## License

MIT. See `LICENSE`. Sample documents in `data/sample/` are public-domain legal texts and not subject to this license.
