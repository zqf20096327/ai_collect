<div align="center">
  <a href="https://youtu.be/VAYccITCaPo">
    <img src="https://img.youtube.com/vi/VAYccITCaPo/0.jpg" alt="DeepSeek V4.1 Flash Is INSANE! Smaller, Faster, Smarter?">
  </a>
  <h3>📺 <a href="https://youtu.be/VAYccITCaPo">Watch the full video on YouTube</a></h3>
</div>

# DeepSeek-V4.1-Flash Technical Report & Developer Guide

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-DeepSeek--V4.1--Flash-yellow)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
[![Context Window](https://img.shields.io/badge/Context-1M%20Tokens-00F0FF)](https://deepseek.com)
[![KV Cache](https://img.shields.io/badge/KV%20Cache-890%20B%2Ftok-00FF9D)](https://deepseek.com)
[![Parameters](https://img.shields.io/badge/Backbone-552B%20MoE-purple)](#key-architectural-innovations)

A technical overview and evaluation report for **DeepSeek-V4.1-Flash**, detailing its Causal Encoder-Decoder (CED) architecture, Compressed Sparse Attention 2 (CSA2), 196B Engram memory lookup system, 1M token context support, and benchmark performance.

---

## 💡 Executive Summary

**DeepSeek-V4.1-Flash** is a multimodal Mixture-of-Experts (MoE) language model featuring **552B backbone parameters**, **196B Engram conditional static memory**, native vision processing (DeepSeek-ViT), and support for sequence contexts up to **1 Million tokens**.

Through architectural innovations—most notably **Causal Encoder-Decoder (CED)** and **Compressed Sparse Attention 2 (CSA2)**—DeepSeek-V4.1-Flash compresses the global KV cache footprint down to **890 bytes per token** (a ~4-fold reduction vs. V4-Flash and ~437-fold reduction vs. V1), while outperforming frontier models like Claude Opus 5.0 and GPT-5.6 Sol on agentic coding and security benchmarks.

```
+-----------------------------------------------------------------------------------+
|                              DEEPSEEK-V4.1-FLASH                                  |
|                                                                                   |
|  [ 20-Layer Causal Encoder ]  ===========>  [ 20-Layer Causal Decoder ]            |
|       8B Active / Token                          16B Active / Token               |
|                                                          ||                       |
|                                                          || Global KV Projection  |
|                                                          \/                       |
|  [ 196B Engram Memory ]                    [ FP4 E2M1 Main KV Cache ]             |
|  [ 45T Multimodal Corpus ]                 [ 890 Bytes / Token Footprint ]        |
+-----------------------------------------------------------------------------------+
```

---

## 🛠️ Key Architectural Innovations

### 1. Causal Encoder-Decoder (CED) & Asymmetrical Activation
* **40-Layer Structure:** 20-layer causal encoder followed by a 20-layer decoder.
* **Global KV Cache Projection:** The decoder's global KV cache is projected from the final encoder hidden states rather than derived from each decoder layer's own hidden states.
* **Asymmetrical Parameters:** Activates only **8B parameters per token during prefill** and **16B parameters during decode**, resulting in ultra-fast prompt processing for input-heavy agentic workloads.
* **SWA Bounded Replay:** Reconstructs missing Sliding Window Attention (SWA) KV states on-the-fly by replaying only the most recent $n_{\text{win}}$ tokens, cutting persistent SSD KV footprint by 8×.

### 2. Compressed Sparse Attention 2 (CSA2) & FP4 Precision
* **Layer Modes:** Assigns each attention layer one of three static modes: **Full**, **Reindex**, or **Reuse**.
* **FP4 Format:** Main KV cache uses **FP4 E2M1** format (with one E4M3 scale per 16 channels).
* **Hierarchical Sparse Indexer:** Restricts deeper indexing layers to candidate pools constructed by the first Full Mode layer, bounding indexer cost independently of context length.
* **KV Cache Compression:** Achieves **890 bytes/token** global KV cache footprint.

### 3. Engram Memory & DSpark Speculative Decoding
* **Engram Conditional Memory:** 196B static parameters accessed sparsely via token-based n-gram lookup tables. Can be offloaded to NVMe SSD/RAM.
* **Single-Pass mHC:** Revised residual-stream mixing with efficient Mega-mHC kernels.
* **DSpark Draft Model:** 7.9B parameter draft model executing semi-autoregressive draft generation with confidence-scheduled verification.
* **MoE Topology:** 1 shared expert + 384 routed experts per MoE layer (6 routed experts activated per token).

### 4. Native Multimodal Architecture
* **DeepSeek-ViT:** Trained from scratch using 2D-RoPE and 3×3 pixel-unshuffle downsampling.
* **MLP Projector:** 2-layer MLP projector feeding visual embeddings directly alongside text tokens from step zero of pre-training on 45T multimodal tokens.

---

## 📊 Benchmark Evaluation Results

All instruct models evaluated under maximum reasoning effort (`reasoning_effort=100`, `temperature=1.0`, `top_p=0.95`).

### 1. Code & Agent Benchmarks

| Benchmark (Metric) | Claude Opus 5.0 | GPT-5.6 Sol | Kimi K3 | GLM-5.3 | DeepSeek-V4-Pro | DeepSeek-V4-Flash | **DeepSeek-V4.1-Flash** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Terminal-Bench 2.1** (Pass@1) | 89.1% | 88.8% | 88.3% | 88.2% | 87.9% | 82.7% | **90.6%** |
| **Terminal-Bench 3.0** (Pass@1) | 43.3% | 34.4% | 17.7% | 28.3% | 11.8% | 7.6% | **30.0%** |
| **Terminal-Bench 4.0** (Pass@1) | 51.8% | 39.9% | 12.6% | 37.9% | 12.4% | 7.0% | **31.2%** |
| **DeepSWE v1.1** (Resolved) | 74.0% | 73.0% | 67.5% | 66.9% | 62.7% | 54.4% | **74.2%** |
| **Codeforces** (Rating) | — | — | — | — | 3348 | 3289 | **3471** |
| **CyberGym** (Pass@1) | — | 84.5% | 80.0% | 84.5% | 83.3% | 76.7% | **88.1%** |
| **SEC-Bench Pro** (Pass@1) | — | 74.3% | — | — | 56.4% | 30.9% | **62.8%** |
| **AutomationBench** (Pass@1) | 50.3% | 45.8% | 46.7% | 48.8% | 43.2% | 37.7% | **54.8%** |
| **Agent's Last Exam** (Pass@1) | 28.6% | 26.7% | 27.6% | 28.5% | 25.7% | 25.2% | **31.8%** |

### 2. Base Model Core Capabilities

| Benchmark (Metric) | # Shots | DeepSeek-V4-Flash-Base | DeepSeek-V4-Pro-Base | **DeepSeek-V4.1-Flash-Base** |
| :--- | :---: | :---: | :---: | :---: |
| **Backbone Parameters** | — | 284B | 1.6T | **552B** |
| **Active Parameters** | — | 13B | 49B | **8B (Prefill) / 16B (Decode)** |
| **MMLU-Pro** (EM) | 5-shot | 68.3% | 73.5% | **74.1%** |
| **AGIEval** (EM) | 3-5 shot | 83.9% | 84.4% | **83.4%** |
| **HumanEval** (Pass@1) | 0-shot | 69.5% | 76.8% | **79.4%** |
| **GSM8K** (EM) | 8-shot | 90.8% | 92.6% | **93.0%** |
| **DocVQA** (LLM-Judge) | 4-shot | — | — | **95.6%** |
| **RefCOCO-avg** (Acc@0.5) | 0-shot | — | — | **86.0%** |

---

## 📉 KV Cache Size Across Generations

| Generation | Release Date | Global KV Cache / Token | Reduction Ratio |
| :--- | :---: | :---: | :---: |
| **DeepSeek-V1** | Nov 2023 | 389,120 Bytes | 1.0× (Baseline) |
| **DeepSeek-V3.2** | Dec 2025 | 48,068 Bytes | 8.1× Smaller |
| **DeepSeek-V4-Flash** | Apr 2026 | 3,514 Bytes | 110.7× Smaller |
| **DeepSeek-V4.1-Flash** | Sept 2026 | **890 Bytes** | **437.2× Smaller** |

---

## 💳 API Pricing & Serving Overhead

DeepSeek-V4.1-Flash is accessible via the API endpoint `deepseek-flash`.

* **HBM Footprint:** Reduced by **4×**.
* **SSD Storage:** Reduced by **8×**.
* **Off-Peak Rates:** 50% lower pricing during off-peak hours (04:00 UTC schedule).

---

## 📜 Citation

```bibtex
@misc{deepseekai2026deepseekv41flash,
      title={DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression},
      author={DeepSeek-AI},
      year={2026},
      url={https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash}
}
```

---

## 📄 License

Model weights and specifications are licensed under the **[MIT License](LICENSE)**.

---

## Keywords
DeepSeek V4.1 Flash, DeepSeek-V4.1-Flash, Causal Encoder Decoder, CED Architecture, Compressed Sparse Attention 2, CSA2, FP4 KV Cache, 196B Engram Memory, 1M Context Window, MoE Model, Agentic Benchmarks, Open Source LLM.
