# rag-eval-workflow

A framework-neutral Codex Agent Skill for building reproducible RAG evaluations, with additional guidance for Chinese narrative scripts and jubensha knowledge bases.

It helps an agent:

- version source, OCR, chunking, embedding, index, retrieval, and generation settings;
- create and validate a golden evaluation set;
- measure retrieval separately from answer generation;
- compare candidates with a saved baseline and explicit regression gates;
- diagnose failures by ingestion, chunking, retrieval, reranking, generation, or evaluation layer;
- test script-specific chronology, character knowledge, relationships, clues, round access, host truth, and spoiler boundaries.

It does not require NVIDIA, RAGAS, a particular vector database, or a hosted judge.

## Install

Clone directly into the Codex personal skill directory:

```bash
git clone https://github.com/w93139/rag-eval-workflow.git ~/.codex/skills/rag-eval-workflow
```

Codex can discover the skill on a later turn. Invoke it explicitly with `$rag-eval-workflow`, or let its narrow description match RAG and vector-retrieval evaluation work automatically.

## Start a project evaluation

```bash
python ~/.codex/skills/rag-eval-workflow/scripts/init_rag_eval.py --project /path/to/project
```

Add curated cases to `rag-eval/eval/golden.jsonl`, then validate them:

```bash
python ~/.codex/skills/rag-eval-workflow/scripts/validate_golden.py /path/to/project/rag-eval/eval/golden.jsonl
```

To score retrieval results containing stable chunk IDs:

```bash
python ~/.codex/skills/rag-eval-workflow/scripts/score_retrieval.py \
  --golden /path/to/project/rag-eval/eval/golden.jsonl \
  --results /path/to/results.jsonl \
  --k 5
```

`results.jsonl` uses one object per line with `id` and `retrieved_chunks`; chunks may be ID strings or objects containing an `id` string.

## Verify this repository

```bash
python -m unittest discover -s tests -v
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## High-star workflow absorption

Yes. The skill adopts selected ideas from NVIDIA's `rag-eval`, `obra/superpowers`, and `addyosmani/agent-skills`: explicit data contracts, baseline comparisons, per-query evidence, failure-layer diagnosis, fresh verification, and regression gates. It independently implements data/expected/output concepts inspired by `Macondooo/codex-research-examples`; that repository had no declared license when reviewed, so no text or code was copied.

The design remains framework-neutral and adds script-specific truth, viewpoint, clue, round, access, and spoiler checks. Exact revisions and rejected vendor-specific constraints are in [references/provenance.md](references/provenance.md).

## Copyright and private corpora

Do not publish copyrighted scripts, private OCR text, embeddings, or golden-set passages unless you have permission. Public repositories should contain the workflow and synthetic examples, while private project data stays local.

## License

MIT. See [LICENSE](LICENSE).
