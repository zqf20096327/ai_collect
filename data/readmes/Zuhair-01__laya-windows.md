<p align="center">
  <img src="assets/banner.svg" alt="Laya Windows — Arabic-first typed decisions on ONNX + DirectML" width="100%" />
</p>

<h1 align="center">Laya Windows</h1>
<p align="center"><b>The open-source, self-hosted decision engine for Windows</b></p>
<p align="center">Typed, non-generative AI decisions — <code>choice</code> / <code>score</code> / <code>noul</code> — in a single forward pass, with calibrated probabilities and zero hallucination risk. Ported off macOS-only Core ML onto ONNX Runtime + DirectML, so it runs on any Windows PC.</p>
<p align="center"><i>Same category as <a href="https://typesafe.ai/">TypeSafe's Jev</a> — open-weight, Apache-2.0, and yours to run.</i></p>
<p align="center">
  🌐 <a href="README.ar.md">العربية</a> ·
  <a href="README.zh-CN.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.pt-BR.md">Português</a> ·
  <a href="README.hi.md">हिन्दी</a> ·
  <a href="README.ru.md">Русский</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <a href="https://github.com/Zuhair-01/laya-windows/actions"><img src="https://img.shields.io/github/actions/workflow/status/Zuhair-01/laya-windows/ci.yml?branch=main&label=build" alt="build status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="Apache 2.0 license"></a>
  <a href="https://github.com/Zuhair-01/laya-windows/stargazers"><img src="https://img.shields.io/github/stars/Zuhair-01/laya-windows?style=social" alt="GitHub stars"></a>
  <img src="https://img.shields.io/badge/platform-Windows%2010%2F11-0078D6?logo=windowsxp&logoColor=white" alt="Windows 10/11">
  <img src="https://img.shields.io/badge/GPU-DirectML%20(any%20DX12%20GPU)-5c2d91" alt="DirectML">
  <img src="https://img.shields.io/badge/language-Arabic%20%2B%20100%2B-2ea44f" alt="Arabic + 100 languages">
</p>

---

> **TL;DR:** `laya-coreml` only runs on Apple Silicon Macs. **Laya Windows** ports the same
> Laya typed-decision model (no text generation, just calibrated `choice`/`score`/`noul`
> probabilities) onto ONNX Runtime + DirectML, so it runs on any Windows PC with any DX12
> GPU, with a dedicated Arabic evaluation suite the original doesn't have.

## Why this exists

[`laya-coreml`](https://github.com/mizorewww/laya-coreml) ports the [Laya](https://github.com/NandhaKishorM/laya)
typed-decision model onto Apple's Neural Engine. macOS and Apple Silicon only. Most of the
world, and most of our own stack, runs Windows. **Laya Windows** ports the same idea onto
**ONNX Runtime + DirectML**, Microsoft's cross-vendor GPU inference stack, so it runs on
**any DirectX 12 GPU** (NVIDIA, AMD, Intel, integrated) with no CUDA requirement, plus a
first-class **Arabic** demo and evaluation suite the original project doesn't ship.

Laya itself evaluates typed questions (`choice`, `score`, `noul`) over any text or JSON
state in a single forward pass. No autoregressive decoding, nothing to parse. You get
calibrated probabilities back, not a wall of generated text.

```python
# Full typed-decision API (CPU/CUDA via PyTorch — works today, any OS):
import laya
agent = laya.load("convaiinnovations/laya-multilingual")
result = agent.predict(
    "تم خصم المبلغ مرتين من حسابي، الرجاء استرجاع الفرق بأسرع وقت",
    {
        "refund": {"type": "noul", "instructions": "Does the customer request a refund?"},
        "urgency": {"type": "score", "criteria": ["not urgent", "soon", "critical"]},
    },
)
print(result["answers"]["refund"])

# Windows-native fast path (ONNX + DirectML encoder — see Status below):
from laya_windows import LayaWindowsEngine
engine = LayaWindowsEngine.from_dir("models")
vector = engine.embed("تم خصم المبلغ مرتين من حسابي")
```

## Laya Windows vs. TypeSafe Jev

[Jev](https://typesafe.ai/) is a commercial "System One" model from TypeSafe, announced in
September 2026, in the same non-generative, typed-probability category as Laya (`choice`/
`score`/`noul` answers, no token generation). It's closed-weight and API-metered. **Laya
Windows** is the open-weight route to the same category: self-hosted, Apache-2.0, no
per-call billing, running on your own Windows GPU instead of TypeSafe's cloud.

| | TypeSafe Jev | Laya Windows |
|---|---|---|
| Weights | Closed, API-only | Open (Apache-2.0), self-hosted |
| Cost model | Per-token API pricing | Free, your own hardware |
| Deployment | Cloud API | Local — Windows, any DX12 GPU or CPU |
| Data | Leaves your machine | Stays local |
| Arabic | Not documented | Dedicated benchmark suite |

## What's different from the Mac-only original

| | `laya-coreml` (upstream) | **Laya Windows** |
|---|---|---|
| Platform | macOS 15+, Apple Silicon only | Windows 10/11, any DX12 GPU |
| Accelerator | Core ML / Apple Neural Engine | ONNX Runtime / DirectML (GPU-agnostic) |
| Quantization | Core ML W8 palette | ONNX dynamic int8 |
| Arabic support | Inherited from base model, untested | First-class: dedicated eval suite + demo below |
| Evaluation | Public benchmark fixtures | Same fixtures + an Arabic/English triage benchmark against real support-message phrasing |

## Benchmarks

**Live, searchable results: [zuhair-01.github.io/laya-windows](https://zuhair-01.github.io/laya-windows/)**

A sortable table, generated only from real committed runs of `bench/run_eval.py` (department
routing, urgency scoring, refund-intent detection, Arabic + English mixed). No estimated
numbers are published here or in this README; the page says so plainly when it's empty.
See [`bench/`](bench/) for the harness itself, and [CONTRIBUTING.md](CONTRIBUTING.md) to add
your own hardware's results.

## Install

```bash
git clone https://github.com/Zuhair-01/laya-windows
cd laya-windows
pip install -r requirements.txt

# 1. Export the encoder to ONNX (one-time, per checkpoint)
python onnx_export.py --model convaiinnovations/laya-multilingual --out models/laya-multilingual.onnx

# 2. Optional: int8 quantize for lower latency / smaller footprint
python quantize.py --in models/laya-multilingual.onnx --out models/laya-multilingual.int8.onnx

# 3. Run the Arabic triage demo
python demo/triage_demo.py
```

Requires Windows 10 1903+ / Windows 11, Python 3.10+. DirectML ships in the box on
modern Windows — no separate GPU driver stack to install beyond your normal GPU driver.

## Status

- [x] Encoder export (PyTorch → ONNX)
- [x] DirectML / CPU inference engine
- [x] Dynamic int8 quantization
- [x] Arabic + English triage benchmark harness
- [ ] Decision-head (RL projection layer) full ONNX port. Currently loaded from the
      original `transformers` checkpoint; encoder runs on DirectML, head runs on CPU.
      Tracked in [#1](https://github.com/Zuhair-01/laya-windows/issues/1).

This project is upfront about what's ported and what isn't — same spirit as upstream's own
"limits" section. No inflated claims.

## Use cases

- **Support/lead triage**: route incoming messages by department, urgency, refund/churn
  intent, in Arabic or English, without an LLM call.
- **Local classification gate**: cheap first-pass filter (spam, urgency, intent) ahead of
  an LLM, cutting API cost on high-volume inboxes.
- **Offline/on-prem deployments**: no cloud dependency, runs on a normal Windows machine.

## FAQ

**Does this need a Mac or an Apple Neural Engine?**
No. That's the whole point — it runs on plain Windows 10/11 with any DirectX 12 GPU
(NVIDIA, AMD, Intel, or integrated), via ONNX Runtime + DirectML instead of Core ML.

**Is this the same model as `laya-coreml`?**
Yes, same underlying Laya weights (`convaiinnovations/laya-multilingual` etc. on Hugging
Face) — different execution backend. Accuracy is identical; only latency and platform
differ.

**Does it generate text like an LLM?**
No. It answers typed questions (`choice`, `score`, `noul`) with calibrated probabilities
in a single forward pass. There's no decoding step and nothing to hallucinate.

**Is Arabic actually supported, or just "should work"?**
The `laya-multilingual` checkpoint is trained on 100+ languages including Arabic. This
repo adds a dedicated Arabic/English triage benchmark (see [`bench/`](bench/)) to verify
it, rather than assuming multilingual claims transfer without checking.

**Can I run this without a GPU?**
Yes — it falls back to `CPUExecutionProvider` automatically if DirectML isn't available.

## Credits

Independent Windows port of [Laya](https://github.com/NandhaKishorM/laya) by Convai
Innovations, following the same approach as the Apple-only
[`laya-coreml`](https://github.com/mizorewww/laya-coreml) port. Not an official Convai
Innovations, Apple, or Microsoft release. Apache-2.0, see [NOTICE](NOTICE).

---

<sub>Keywords: Laya Windows, Core ML alternative Windows, ONNX Runtime DirectML NLP,
typed decision model, Arabic text classification offline, local LLM alternative Windows,
run Apple Neural Engine model on Windows, Arabic intent classification, offline support
ticket triage, GPU-agnostic transformer inference.</sub>
