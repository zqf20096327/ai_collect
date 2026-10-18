<div align="center">

# 🛡️ ZTC — Zero-Token Confidence

### Judge whether an answer can be trusted, in a single forward pass, with zero generated tokens.

[![Models](https://img.shields.io/badge/%F0%9F%A4%97_Models-FINAL--Bench-ffb020?style=for-the-badge)](https://huggingface.co/FINAL-Bench)
[![S1MB #1](https://img.shields.io/badge/S1MB-%231_of_102-ff6b8b?style=for-the-badge)](https://huggingface.co/spaces/hotchpotch/S1MB-leaderboard)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)

[![Website](https://img.shields.io/badge/Website-vidraft.net-4ea8ff)](https://vidraft.net)
[![Stars](https://img.shields.io/github/stars/final-bench/ztc?style=social)](https://github.com/final-bench/ztc)
[![X](https://img.shields.io/badge/%F0%9D%95%8F-@VIDRAFT__ai-000000)](https://x.com/VIDRAFT_ai)
[![Threads](https://img.shields.io/badge/Threads-@vidraft__lab-101010)](https://www.threads.com/@vidraft_lab)

</div>

---

**ZTC (Zero-Token Confidence)** reads a question and an answer written by any model and returns whether that answer can be trusted. It does this in one forward pass and generates **zero tokens**: it takes the final-layer hidden state at the last position and applies a calibrated probe. The result is fast, deterministic, and cheap enough to run on every answer.

This repository holds the **inference code, the model index, and the method**. The weights live on Hugging Face. The training corpus and the probe-fitting pipeline are not part of this repository.

## 🧬 The ZTC family

| Model | Role | Params | Hugging Face |
|---|---|---|---|
| **ZTC-Judge-4B** | Answer verification, light (runs on CPU) | 4B | [link](https://huggingface.co/FINAL-Bench/ZTC-Judge-4B) |
| **ZTC-Judge-9B** | Answer verification, balanced | 9B | [link](https://huggingface.co/FINAL-Bench/ZTC-Judge-9B) |
| **ZTC-Judge-27B** | Answer verification, best quality | 27B | [link](https://huggingface.co/FINAL-Bench/ZTC-Judge-27B) |
| **Darwin-27B-ZTC-v2** | Typed-decision judge, **#1 on S1MB (102 models)** | 27B | [link](https://huggingface.co/FINAL-Bench/Darwin-27B-ZTC-v2) |
| **Darwin-27B-ZTC** | Typed-decision judge | 27B | [link](https://huggingface.co/FINAL-Bench/Darwin-27B-ZTC) |
| **Darwin-397B-ZTC** | Largest judge | 397B | [link](https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC) |

Two lines: **ZTC-Judge** verifies someone else's answer (question + answer -> trust). **Darwin-ZTC** scores typed decisions (condition / choice / score), and leads the System One Mosaic Benchmark.

## 🔬 How it works

```
text = template(question, answer)
h    = model(text).last_hidden_state[last_non_pad_token]   # one forward pass, 0 tokens generated
# linear probe -> raw trust score, with review / clear thresholds -> verdict
score = ((h - mu) / sd) @ w
# curved probe -> RBF ranking signal
```

- **Determinism:** no sampling, so the same input gives the same score.
- **Cost:** one forward pass per answer, no decoding loop.
- **Calibration:** the probe is fitted leave-one-domain-out, so each reported figure comes from a domain the probe never saw.

See `ztc_judge.py` (linear probe, verdict) and `usage_curve.py` (curved probe). These are the official inference files from the model cards.

## ⚡ Usage

```python
from ztc_judge import ZTCJudge
j = ZTCJudge.from_pretrained("FINAL-Bench/ZTC-Judge-9B")   # or -4B / -27B
print(j.score("By what mechanism do statins lower LDL cholesterol?",
              "Statins inhibit HMG-CoA reductase, lowering cholesterol synthesis."))
# -> {"score": ..., "verdict": "이상 없음 / 판단 보류 / 검토 요망", "generated_tokens": 0}
```

The 4B model is light enough to run on CPU, which is how [ONGRID](https://github.com/final-bench/ongrid) verifies answers without a GPU.

## 📊 Results

- **S1MB (System One Mosaic Benchmark, 102 models):** Darwin-27B-ZTC-v2 is **#1 overall**.
- **typed-decisions:** #1 at accuracy 0.743 (zero-shot).
- Calibration and per-domain figures are published on each model card. ZTC-Judge is strongest on professional exams, biology, and science reasoning; outside those domains treat the score as a ranking signal.

## ⚠️ Scope

ZTC-Judge reports the verifier's judgement, not the answering model's own confidence. It is not a safety or policy classifier, and the probability is a ranking and thresholding signal rather than an absolute guarantee outside the measured domains.

## ❓ FAQ

<details><summary><b>What is ZTC (Zero-Token Confidence)?</b></summary>
ZTC is a method that judges whether an answer is trustworthy in a single forward pass, generating zero tokens. It reads the question and answer, takes the final-layer hidden state, and applies a calibrated probe to return a trust score.
</details>

<details><summary><b>What is zero-token answer verification?</b></summary>
It is verifying an LLM answer without generating any text. Instead of asking another model to critique the answer (which is slow and adds hallucinations), ZTC reads the answer in one forward pass and outputs a calibrated trust score.
</details>

<details><summary><b>How is ZTC different from LLM-as-a-judge?</b></summary>
LLM-as-a-judge generates a critique token by token, so it is slow, non-deterministic, and can hallucinate. ZTC generates zero tokens, is deterministic, and costs one forward pass per answer, so it can run on every answer in production.
</details>

<details><summary><b>Can ZTC run on CPU?</b></summary>
Yes. ZTC-Judge-4B is light enough to run on CPU, which is how ONGRID verifies answers without a GPU.
</details>

<details><summary><b>Which ZTC model tops the S1MB benchmark?</b></summary>
Darwin-27B-ZTC-v2 is #1 overall on the System One Mosaic Benchmark among 102 models.
</details>

## 📫 Connect

🌐 [vidraft.net](https://vidraft.net) · 🤗 [FINAL-Bench](https://huggingface.co/FINAL-Bench) · 🧵 [@vidraft_lab](https://www.threads.com/@vidraft_lab) · 𝕏 [@VIDRAFT_ai](https://x.com/VIDRAFT_ai) · ✉️ `vidraft@mail.vidraft.net`

## 📜 License

Apache-2.0 · Built by **VIDRAFT** · *Beyond AI, Toward AGI.*

<div align="center"><sub>zero-token verification · answer verification · hallucination detection · LLM judge · calibration · ZTC · S1MB</sub></div>
