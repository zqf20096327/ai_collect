# Custom Guru 

**An open-source engine for *grounded, auditable* AI personas — it answers *as* a person
using their own recorded words, and is honest about the difference between what they
actually said and what it's reasoning on their behalf.**

Most "chat with X" / persona bots optimize for *sounding* like someone. They can't tell you
what's a real quote versus an invention, and you can't inspect how they reached an answer.
Custom Guru treats this as a **provenance and reasoning-transparency problem**: every claim
is either tied to a **source quote that's been verified to actually exist**, or clearly
**labelled as extrapolation** — never blurred. Bring your own corpus (talks, essays, docs);
the engine ships with **zero persona data**.

## What makes it different
- **Verified grounding, not vibes.** When the persona answers from the corpus, each cited
  quote is checked to *literally occur* in the source — fabricated or paraphrased citations
  are dropped, not shown. (`_quote_supported`, `_apply_citations`.)
- **Distilled principles, not just chunks.** An offline pipeline distills a corpus into a
  small, inspectable set of **durable principles**, each backed by verified quotes
  (`principles.json`) — a model of *how the person thinks*, not just a search index.
- **Honest about extrapolation.** For questions the person never addressed, the goal is to
  reason *from their own principles* with a transparent **premise → principle → conclusion**
  trace, explicitly marked as a reasoned hypothesis — not passed off as fact.
- **Provider-agnostic & self-hostable.** One `LLMProvider` interface; swap OpenAI / Anthropic
  / a local model / a proxy with an env var. No vendor lock-in.

## Status (honest)
**Available now:** grounded Q&A in the persona's voice · verified inline citations ·
principle-extraction pipeline (map → consolidate → compress) · the **principle-based
reasoning engine** — questions the person never addressed are answered by applying the
extracted principles through a visible **factor → principle → inference** trace, labelled as
extrapolation and never passed off as a real quote · **faithfulness critic** — checks each
reasoned answer against the principles it cites and flags unsupported claims · honest fallback
for out-of-corpus questions · an evaluation harness (groundedness / voice / transparency +
routing accuracy) · optional Langfuse tracing · a Streamlit demo UI.

**In progress:** denser, more diverse corpora — the single biggest quality lever, since
grounded vs. novel retrieval distances overlap at small corpus sizes.

## Architecture
```
Streamlit UI ──HTTP──▶ FastAPI backend
                          │
        ┌─────────────────┼───────────────────┐
        ▼                 ▼                     ▼
   Retriever        Principle store        LLMProvider (adapter)
   (Chroma)         (quote-verified)        ├─ Hyperspace (default)
        │                 │                 └─ OpenAI / Claude / local (pluggable)
        └──────▶ Chat service: ground (cited) · reason-from-principles (traced) · decline
```

## Quick start

> **Don't have the Hyperspace proxy?** Set `LLM_PROVIDER=openai` (or `claude`) in `.env` —
> see [Using a different LLM provider](#using-a-different-llm-provider) below.
> You can also run all offline tests first (zero LLM access needed): `pytest -m "not live"`.

```bash
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env            # fill in your LLM provider keys — see the file for options
# drop plain-text source files into data/personas/<name>/transcripts/
python -m backend.app.rag.ingest       # build the retrieval store  (needs LLM for embeddings)
python -m backend.app.rag.principles   # distill the principle set (principles.json)
uvicorn backend.app.main:app --reload  # start the API
streamlit run frontend/streamlit_app.py
```

> **No corpus yet?** The app won't return answers until you ingest at least one transcript.
> Drop any `.txt` file (a few hundred words is enough to verify the pipeline) into
> `data/personas/example/transcripts/` before running the two pipeline steps above.
> The offline tests (`pytest -m "not live"`) work without any corpus.

## Bring your own corpus
Place plain-text files under `data/personas/<name>/transcripts/` (gitignored — your data is
never committed), set `PERSONA` in `.env`, and re-run the two pipeline steps above. The demo
ships with no persona's content.

## Using a different LLM provider

The app never calls a vendor SDK directly — it depends on one small interface,
`LLMProvider` ([`backend/app/llm/base.py`](backend/app/llm/base.py)):

```python
def generate(self, messages, system=None, max_tokens=1000) -> str   # chat completion
def embed(self, texts) -> list[list[float]]                         # embeddings
```

**Built-in providers:**
| `LLM_PROVIDER` value | Description | Key env vars |
|---|---|---|
| `hyperspace` (default) | Local proxy at `localhost:6655` | `HYPERSPACE_API_KEY`, `HYPERSPACE_LLM_MODEL`, `HYPERSPACE_EMBED_MODEL` |
| `openai` | OpenAI API (GPT-4o / text-embedding-3) | `OPENAI_API_KEY`, `OPENAI_LLM_MODEL`, `OPENAI_EMBED_MODEL` |

> An OpenAI provider adapter is available in `draft/openai_provider.py`. Copy it to
> `backend/app/llm/openai_provider.py`, register it in `factory.py` (four-line change —
> see the file header for exact instructions), and add the env vars below to `.env`.

**To add any other provider:** copy [`backend/app/llm/provider_template.py`](backend/app/llm/provider_template.py),
implement the two methods, register it in [`factory.py`](backend/app/llm/factory.py), and
set `LLM_PROVIDER` in `.env`. [`hyperspace.py`](backend/app/llm/hyperspace.py) is a full
worked example.

**Important when switching models:** embedding models are not interchangeable.
If you change `*_EMBED_MODEL`, delete `data/chroma/` and re-run `ingest` — mixing
models in the same vector store produces silent semantic garbage.

## Related work — and how this differs
- **RAG frameworks (LangChain, LlamaIndex):** provide retrieval + citation *plumbing*, but
  "citation" means "this chunk was retrieved," not "this quoted span provably exists," and
  they freely fabricate for out-of-corpus questions. Custom Guru verifies quotes and refuses
  to blur grounded vs. extrapolated.
- **Persona / character bots:** mimic *tone* (via fine-tuning/prompting) with no notion of
  evidence or honesty. Here, groundedness and auditability are first-class.
- **Prompt libraries (e.g. Fabric):** offer `extract_wisdom`-style prompts but no quote
  verification, consolidation, or provenance contract.
- **Techniques (Constitutional AI, Step-Back, rule induction):** methods, not a reusable tool
  that emits an auditable principle set + a traceable reasoning path over your corpus.

The contribution here is the **combination + the design stance**: honesty and auditability as
hard constraints, packaged as a reusable, persona-agnostic engine.

## Honest scope
"Verified" means the **evidence is real and locatable** — *not* that the interpretation is
provably correct. Principle induction and extrapolation remain the model's judgment; the
mitigations are the inspectable artifacts, the grounded/extrapolated labelling, and the
evaluation harness. We never claim to predict what a person "really" thinks.

## Responsible use
The demo ships **persona-neutral** and includes **no persona's data**. If you configure it
with a real person's words, you are responsible for having the right to use that content, and
for making clear to anyone using it that this is an **unofficial AI avatar** — not the
person, and not affiliated with or endorsed by them. Keep your corpus private; the repo
gitignores `data/` so it is never committed.

## Contributing & conduct
See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License
[MIT](LICENSE) © 2026 Gnaneshwar Adapa.
