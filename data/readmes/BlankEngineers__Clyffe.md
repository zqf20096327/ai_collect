# Clyffe — Native LittleBit-2 Language Model

**Organization:** Blank Engineers (ARC III Ecosystem)  
**Model Name:** Clyffe (Research Code: `ARC-LB-01`)  
**Current Verified Baseline:** `Clyffe v0.1.1`  

**Project Leads:**  
Developed by **Vishnupriyan Sivanesan** (Head of Blank Engineers) and **Chittari Hari Dhanush** (Vice Head of Blank Engineers).  
*Part of the **ARC III** ecosystem — Property of **Blank Engineers**.*

---

## Project Description

**Clyffe** is an independently initialized, independently trained experimental language model built from random initialization using **LittleBit-2** binary latent factorization, Internal Latent Rotation, Joint Iterative Quantization (Joint-ITQ), Dual-SVID multi-scale compensation, and Quantization-Aware Training (QAT) — **without** pretrained LLM weights, external AI APIs, or knowledge distillation.

Unlike conventional post-training compression pipelines that compress pretrained FP16 LLMs, Clyffe investigates native LittleBit-2 representation across all learned weight matrices—including token embeddings and the output projection (`lm_head`)—with bit-packed offline inference.

---

## Features

- **From-Scratch Initialization:** Zero pretrained weights, zero knowledge distillation, zero external LLM APIs.
- **Native LittleBit-2 Computing Engine:** Low-rank SVD factorization, Internal Latent Rotation, Joint-ITQ (`T=50`), Dual-SVID multi-scale compensation, and `SmoothSign` / `STEBinary` QAT.
- **Full-Model Binary Latent Coverage:** `99.76%` of dense-equivalent parameters in `Clyffe v0.1.1` (`240,640 / 241,216`) stored in LittleBit-2 form (`1.1727` actual BPW; `94,817` bytes `.pt` vs `979,648` bytes dense).
- **Custom Digit-Aware BPE Tokenizer:** Trained exclusively on project corpora (`vocab_size=600` in `v0.1.1`, expanded to `2,048`–`4,096` in general-LM experiments).
- **100% Offline Packed Inference:** Executes directly on `int32`-packed binary factors and FP16 scales via CLI (`run_clyffe.py`) and local web dashboard (`frontend/server.py`).
- **Multi-Checkpoint Comparison & Audit:** Side-by-side Dense Control (`A`), LittleBit-SVD (`B`), LittleBit-2 SmoothSign (`C1`), and LittleBit-2 STE (`C2`).

---

## Architecture Overview (Non-Sensitive)

- **Model Family:** Decoder-only Transformer with pre-norm `RMSNorm`, Rotary Position Embeddings (`RoPE`), causal multi-head self-attention, and GELU feed-forward network.
- **Stage 0 Verified Baseline (`Clyffe v0.1.1`):**
  - **Layers / Width / Heads:** `4` layers, `d_model = 64`, `4` attention heads, `d_ff = 192`, `context = 96`
  - **Dense-Equivalent Parameters:** `241,216` (`99.76%` LittleBit-2 covered; `576` 1D RMSNorm parameters in FP16)
  - **Validation Performance:** `val_loss = 0.0782` (`PPL = 1.08` on `C1_SmoothSign`) vs `0.0829` (`PPL = 1.09`) Dense Control
  - **Offline Inference:** `~51.5 ms` average latency on CPU (`0.37 MB` peak Python RAM)

---

## Live Demo (Local Offline Runtime)

Because Clyffe runs 100% offline with zero external APIs, you can launch the live local web interface or CLI directly from this repository:

```bash
# 1. Start the offline web dashboard (http://127.0.0.1:8765)
PYTHONPATH=. .venv/bin/python frontend/server.py --host 127.0.0.1 --port 8765

# 2. Or run the interactive CLI
PYTHONPATH=. .venv/bin/python run_clyffe.py
```

---

## Screenshots and Demo Videos

*Add captured UI screenshots and demo recordings to `docs/media/` and link them here:*

- **Dashboard & Checkpoint Switcher Screenshot:** `docs/media/clyffe-dashboard.png` *(pending upload)*
- **Offline CLI & Native Inference Demo Video:** `docs/media/clyffe-demo.mp4` *(pending upload)*

---

## Roadmap

- [x] **Stage 0 (`Clyffe v0.1` / `v0.1.1`):** LittleBit-2 math engine, unit tests, 4-condition benchmark (`A`, `B`, `C1-SmoothSign`, `C2-STE`), packed offline inference, and Stage 0 gate verification.
- [x] **Phase 1 Audit & General-LM Prototyping (`v0.1.2` / `v0.2`):** Protected LittleBit-2 integrity hashes, Hugging Face human-written corpus pipeline (Simple Wikipedia, Dolly-15k, ARC-Easy, GSM8K), and multi-turn runtime support.
- [ ] **CUDA GPU Acceleration:** Enable CUDA PyTorch on RTX 4050 for large-scale pretraining.
- [ ] **Stage 1 (`Clyffe v0.2`, ~2M params):** 40M-token pretraining on Simple Wikipedia + Project Gutenberg followed by multi-turn SFT & held-out generalization evaluation.
- [ ] **Stage 2 (`Clyffe v0.3`, ~10M params):** 200M-token pretraining with `16k` vocabulary and full packed-kernel benchmarking.

---

## Attribution & License

- **License:** All Rights Reserved — **Blank Engineers (ARC III Ecosystem)**. Public viewing and showcase only; copying, modification, or redistribution is strictly prohibited. See [LICENSE](LICENSE).
- **Research Attribution:** LittleBit and LittleBit-2 mathematical methods are attributed to Banseok Lee, Dongkyu Kim, Youngcheon You, and Youngmin Kim (Samsung Research, NeurIPS 2025 & ICML 2026, CC BY-NC 4.0).
