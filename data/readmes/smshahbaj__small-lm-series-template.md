# Small LM Series Template

### Ship your own small language model family — docs, examples, Space.

<p align="center">
  <a href="https://github.com/smshahbaj/small-lm-series-template/generate"><img src="https://img.shields.io/badge/GitHub-Use%20this%20template-black?logo=github" alt="Use this template"></a>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT">
  <a href="https://huggingface.co/collections/smshahbaj/rifa-text-series"><img src="https://img.shields.io/badge/Example-RIFA%20Series-FFD21E?logo=huggingface&logoColor=black" alt="RIFA example"></a>
</p>

<p align="center"><b>Hub weights + GitHub docs + optional Space</b> — the clean way to ship a small-LM family.</p>

---

## What this is

A **ready-to-copy skeleton** for publishing a *series* of small language models like a product, not a random dump of checkpoints.

| You keep | You do not put here |
|----------|---------------------|
| Model **weights** on [Hugging Face](https://huggingface.co) | Multi-GB `.safetensors` / `.bin` in git |
| **Docs, scripts, Space starter** in this repo | Private training logs / secrets |

Click **Use this template** → rename → replace `YOUR_` placeholders → link your models.

---

## Live reference (real series)

This template was extracted from a working stack:

| Asset | Link |
|-------|------|
| **Collection** | [RIFA Text Series](https://huggingface.co/collections/smshahbaj/rifa-text-series) |
| **Docs hub** | [RIFA-Text-Series](https://github.com/smshahbaj/RIFA-Text-Series) |
| **Public Space** | [RIFA-Chat](https://huggingface.co/spaces/smshahbaj/RIFA-Chat) |
| **Author** | [@smshahbaj](https://github.com/smshahbaj) |

Use it as the pattern: **collection → per-model cards → GitHub narrative → demo Space**.

---

## Why not only Hugging Face?

| Only HF | With this template |
|---------|-------------------|
| Checkpoints exist | Series *story* exists |
| Hard for others to mirror structure | One-click **Use this template** |
| Demo often missing | `examples/` + `space/` starters |
| Weak discoverability outside Hub | GitHub search, stars, forks |

---

## 5-minute setup

1. **Use this template** → create `yourname/your-series-hub`
2. Open [`PLACEHOLDERS.md`](PLACEHOLDERS.md) — replace every `YOUR_`
3. Upload models to Hugging Face; create a **collection**
4. Duplicate `docs/models/example-model.md` once per model
5. Fill the model table below; link model cards back to this repo
6. Optional: deploy `space/` as a Gradio Space

---

## Repository layout

```text
small-lm-series-template/
├── README.md                 # Series homepage (you are here)
├── PLACEHOLDERS.md          # Checklist for YOUR_* strings
├── CONTRIBUTING.md
├── LICENSE                  # MIT (template code/docs)
├── CITATION.cff
├── requirements-examples.txt
├── docs/
│   ├── overview.md
│   └── models/
│       └── example-model.md
├── examples/
│   ├── chat.py              # CLI generate demo
│   └── list_models.py
├── space/                   # Gradio Space starter
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── .github/
    └── CODEOWNERS
```

---

## Model table (edit)

| Model | Params | Role | Hugging Face |
|-------|--------|------|--------------|
| Your-Nano | 0.5B | Edge / prototype | `YOUR_HF_USERNAME/YOUR_NANO` |
| Your-Flash | 1.7B | Default public demo | `YOUR_HF_USERNAME/YOUR_FLASH` |
| Your-Pro | 3B | Highest quality in family | `YOUR_HF_USERNAME/YOUR_PRO` |

---

## Design principles

1. **Efficient** — sizes people can run (CPU / consumer GPU)
2. **Documented** — one series page + one page per checkpoint
3. **Demoable** — script and/or Space, not cards alone
4. **Honest** — state limits; no fake benchmark theater
5. **Portable** — others can fork the *process*, not only your weights

---

## Optional: local chat smoke test

```bash
pip install -r requirements-examples.txt
python examples/list_models.py
python examples/chat.py --model YOUR_HF_USERNAME/YOUR_FLASH --prompt "Hello"
```

---

## Citation

```bibtex
@misc{small_lm_series_template,
  title  = {Small LM Series Template},
  author = {smshahbaj},
  year   = {2026},
  url    = {https://github.com/smshahbaj/small-lm-series-template}
}
```

---

## License

- **This template** (docs + scripts): [MIT](LICENSE)
- **Your model weights**: whatever you set on each Hugging Face model card

---

<div align="center">

**Small LM Series Template**

*Ship small models like a series — not a pile of files.*

[Use this template](https://github.com/smshahbaj/small-lm-series-template/generate) · [Example series](https://github.com/smshahbaj/RIFA-Text-Series) · [Example Space](https://huggingface.co/spaces/smshahbaj/RIFA-Chat)

</div>
