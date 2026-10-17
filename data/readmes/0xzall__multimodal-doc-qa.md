# multimodal-doc-qa

> A personal research project exploring multimodal document understanding — combining
> vision-language models with text retrieval to answer questions over PDFs that contain
> figures, tables, and complex layouts.

I started this in mid-April 2026 after getting frustrated with how poorly text-only RAG
systems handle technical PDFs. Charts get OCR'd into garbage. Tables lose their structure.
Diagrams are invisible. So I'm trying something different: keep the visual context, query
both modalities.

## Current state

Week 6. Baseline retrieval works. VLM eval pipeline finally runs end-to-end without OOM.
Still chasing a quality bug in figure-grounded answers — see `RESEARCH-LOG.md` for the
ongoing journal.

## Architecture (rough sketch)

```
PDF -> pdf2image -> page renders + text extraction
     |                |
     v                v
  VLM (LLaVA)    Text retriever (LlamaIndex + BGE)
     |                |
     +------+---------+
            v
     fused reranker
            v
    LLaVA answer generation
```

## Stack

- `LLaVA-1.6` (Mistral-7B variant) — vision-language backbone
- `LangChain` — orchestration glue
- `LlamaIndex` — text-side retrieval
- `pdf2image` + `tesseract` — page rendering and fallback OCR
- `accelerate` — multi-GPU
- PyTorch, transformers (HF)

## Compute

I've been running ablations on a single 24GB consumer GPU which has been... painful.
LLaVA-1.6 at FP16 barely fits with batch 1. To make any real progress on the multi-page
context experiments I'm planning, I need >40GB per device.

This is why I'm applying for AMD Developer Cloud access. MI250's 128GB HBM and MI300X's
192GB would let me drop the gradient checkpointing hacks I'm currently using, fit longer
multimodal contexts, and actually run the full ablation grid in `notebooks/ablations/`.

ROCm 6.x has the bits I need (flash-attention port, bitsandbytes-rocm, accelerate works).
I want to publish ROCm vs CUDA throughput numbers as part of the writeup.

## Read this for the actual story

The README is mostly here so GitHub has something pretty. The honest version of what's
working, what isn't, and why I made each decision lives in [`RESEARCH-LOG.md`](RESEARCH-LOG.md).

## License

MIT. Use whatever you want. If you build on this and beat my numbers, please tell me.
