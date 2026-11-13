
<div align="center">

<img src="docs/images/machx-logo.png" alt="Mach X" width="420">

# Mach X — LLM Inference Engine for Intel Arc

**A C++/SYCL local LLM inference engine for Intel Arc GPUs, built and tuned on two Arc Pro B70 cards: XMX kernels, quantized models, multi-GPU execution, an OpenAI-compatible server — and now text-to-video.**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Language](https://img.shields.io/badge/C%2B%2B20-SYCL%20%2F%20DPC%2B%2B-orange)
![Platform](https://img.shields.io/badge/Intel%20Arc-Battlemage%20B70-0071C5?logo=intel&logoColor=white)
[![Model coverage](https://img.shields.io/badge/models-dense%20%2B%20MoE%20%2B%20hybrid-brightgreen)](#supported-architectures)
![Vision](https://img.shields.io/badge/vision-VLM%20ready-purple)
![Multi-GPU](https://img.shields.io/badge/multi--GPU-tensor--parallel-success)
[![Release](https://img.shields.io/github/v/release/Red-Weasel/machx-inference-engine)](https://github.com/Red-Weasel/machx-inference-engine/releases)

</div>

> [!IMPORTANT]
> ## 🚀 Qwen 4 — ready to run on Intel Arc the day it is released
>
> **We will have Qwen 4 up on Mach X the same day it drops.** Qwen3.8-Flash-Next is the public preview of Qwen 4's architecture (`qwen4exp`: QSA sparse attention + Gated DeltaNet, a 512-expert MoE, hyper-connections, per-layer n-gram embeddings, an MTP draft head), and Mach X already runs it on Arc Pro B70 cards. In v0.2.36–v0.2.38 we built ahead of time everything a Qwen 4 release is expected to ship with:
>
> - **Every community quant on its own kernels:** Q4_K, Q5_K, Q6_K, Q8_0, Q5_0 and Q4_0 expert banks stream as they lie on disk (no host F16 copy). Unsloth's UD-Q5_K_XL, UD-Q6_K_XL and Q8_0 Flash-Next builds were downloaded, loaded and checked against an fp64 reference, then perplexity, lossless speculation and speed.
> - **The draft head and the config the way the converters write them:** the MTP head in llama.cpp's `nextn` layout (Unsloth's `MTP/*.gguf` or inside the model), the hyperparameters llama.cpp reads (per-block attention schedule, per-block arrays), and the `qwen35` pre-tokenizer (30 of 30 lines identical to the HF tokenizer).
> - **Whatever shape Qwen 4 ships in:** a dense model with no experts, hidden size 5120, 4 KV heads, no sparse-attention indexer, fused gate/up expert banks, the `qwen4` / `qwen4moe` arch names. Each was built as a small random model from the Hugging Face reference code, written as a GGUF in llama.cpp's layout and run through the engine end to end: **15 shapes match the reference's output**. Four failed before v0.2.37 (hidden 5120 lost the GPU; dense and indexer-less files were refused) and are fixed.
> - **One card to four:** `--gpus N` splits the model into N stages, and on three or more cards every stage reads the prompt on its own thread (v0.2.38): a 12K-token prompt on four stages reads 572 → 910 tok/s, measured with two stages per card here.
> - **Fast where it counts:** integer-dot and XMX (DPAS) kernels for the K-quant and Q8_0 banks, and a faster decode step (two cards 41.1 → 49.7 tok/s over v0.2.36 and v0.2.37, the long-context step 26.2 → 20.1 ms of GPU time), all with identical output.
>
> <table>
> <tr><th align="left">Qwen 4 on Mach X</th><th align="left">Status</th></tr>
> <tr><td>Weights released</td><td><i>waiting for Alibaba's release</i></td></tr>
> <tr><td>Running in <code>ie serve</code></td><td><b>release day</b> — the model link, the files and the launch line go here</td></tr>
> <tr><td>Decode / prompt reading, 1 and 2 × Arc Pro B70</td><td><b>release day</b> — measured, not estimated</td></tr>
> </table>
>
> <sub>Placeholder: this box is replaced with the measured numbers the day Qwen 4 is out. If the release changes the preview architecture (other sizes, other head counts), the config reader already takes llama.cpp's hyperparameters, 15 such shapes already run against the reference, and anything the engine cannot run yet is refused by name instead of guessed.</sub>

**Latest**

- **v0.2.42, November 13 — DeepSeek-V4.1's VRAM expert set follows the conversation too:** a hot RAM expert trades places with the coldest expert of the fixed VRAM set, about once a token and card, with no extra memory: **16.4 → 17.7 tok/s** on one conversation, **13.8 → 17.2 tok/s** with three requests at once, greedy replies identical on and off. Also: Flash-Next honours `--no-prompt-cache` at one request lane and says when it does not take `--prefill-chunk`, a contributed container build (`Containerfile.b70`), and the first four-card numbers measured by a user. [Details](#new-in-v0242).
- **v0.2.41, November 12 — DeepSeek-V4.1 and MiMo-V2.6 keep the experts the conversation is using in fast memory:** both models held a fixed set of experts in VRAM and RAM, chosen by a ranking file. On real traffic expert use is strongly recent, so the sets now follow it. **DeepSeek-V4.1** (default on): an expert read from the NVMe tier takes the RAM place of the layer's coldest RAM expert, with no extra memory: one conversation of prose / code / prose turns decodes at **12.4 / 6.9 / 10.6 → 14.1 / 13.1 / 14.6 tok/s**, and greedy replies are identical with it on and off. **MiMo-V2.6** (opt-in, `IE_MIMO26_ADAPTIVE=1`, 34 GiB more RAM): every VRAM slot follows recent use: **19.0 → 23.9 tok/s**. [Details](#new-in-v0241). Also in v0.2.41: a Flash-Next load without its image encoder file is text-only again, not an error: v0.2.40 refused to load Flash-Next when no mmproj file was beside the model. The encoder is still loaded at the start whenever the file is there; without it the model now loads text-only with a warning that says what to add. `IE_VISION_REQUIRED=1` keeps v0.2.40's behaviour for a deployment where a model that cannot see must not load, and a file `ie.env` beside the `ie` binary can hold such `IE_NAME=value` defaults for one machine.
- **v0.2.40, November 10 — Flash-Next decodes 24 % faster with the same tokens, uses the whole card, and always reads images:** at `--gpus 2 --ctx 262000 --parallel 4 --spec` one conversation at 33–39K tokens decodes at **37.3 → 46.2 tok/s** (**36.6 → 44.9 tok/s** at temperature 1.0) and its 33.4K-token prompt reads in 33.1 s instead of 37.0, every greedy reply byte-identical to v0.2.39. Found with a [profile](#new-in-v0240): the card no longer idles while a missed expert uploads, the speculation guard re-tries rounds after 6 steps instead of 48, and three changes give the expert cache memory that sat unused — the token embedding moved to system RAM, the context buffers grow with the conversation, and the cards are filled to a real 1 GiB margin instead of leaving ~4 GiB free (**304 / 280 expert slots a layer, were 203 / 165**). The image encoder loads with every Flash-Next load that has its file. One lane (`--parallel 1`): 38.2 → 45.9 tok/s.
- **v0.2.39, November 10 — long conversations stop re-reading themselves:** on the request lanes (`--parallel N`) one changed token anywhere in a conversation's history used to re-read the whole prompt — 53 times and 7,711 seconds in one 37-hour session. Every lane now keeps [restart points](#new-in-v0239): a prompt with one word changed 85 % in reads in **14.6 s instead of 38.3 s**, a rewritten last turn reads 30 tokens instead of 33,609, replies byte-identical. Also: a reference check for [any architecture and any quant](#new-in-v0239) that found and fixed five engine defects, dense models on Intel GPUs without a matrix engine, and a 40-minute soak gate.
- **v0.2.38, November 8 — Flash-Next on four cards reads prompts up to 60 % faster:** on three or more cards every stage of the [layer split](#new-in-v0238) now reads its part of the prompt on its own thread; before, stages 1 … N − 1 read one after another. A 12,069-token prompt on four stages (two per card here) reads **572 → 910 tok/s**, and **610 → 975** with the request lanes, with byte-identical replies. The scheduling is a small header with its own race test, and two cards are unchanged. [Details](#new-in-v0238)
- **v0.2.37, November 8 — Qwen 4's possible shapes tested before the weights exist, and Flash-Next decodes 12 % faster:** a new [mini end-to-end check](#new-in-v0237) builds small random models from the Hugging Face reference code in 15 shapes a Qwen 4 tier may take (dense, hidden 5120, 4 KV heads, no sparse-attention indexer, fused expert banks, …), writes them in llama.cpp's layout and compares the engine's output with the reference. It found that hidden 5120 lost the GPU and that dense and indexer-less files were refused; all fixed. Fused gate/up expert banks load. Flash-Next's hyper-connection mixing reads 8-bit and its expert routing runs on the GPU when that pays: two cards **44.4 → 49.7 tok/s**, the tokens unchanged. [Details](#new-in-v0237)
- **v0.2.36, November 8 — Qwen 4 day-one readiness, Flash-Next decodes faster, and a request can no longer forge a control token:** every community quant of [Flash-Next](#new-in-v0236) (the Qwen 4 preview architecture) streams on its own kernels — Q8_0, Q5_K, Q6_K, Q5_0 and Q4_0 expert banks beside Q4_K — proven on Unsloth's UD-Q5_K_XL, UD-Q6_K_XL and Q8_0 builds; the MTP head loads in llama.cpp's layout; integer-dot and XMX kernels for the bigger quants (the Q8_0 build reads 87.4 → 103.9 tok/s on two cards). The decode step lost launches, a 3× faster sparse attention and a 4× faster router GEMV: two cards **41.1 → 44.4 tok/s**, the step at ~3K context 26.2 → 21.0 ms of GPU time, the output identical. Every chat renderer now keeps a control-token spelling inside a request's own text as text (a fetched page could open a turn or a tool call), a tool call whose JSON lost its last bracket is repaired, and DeepSeek-V4.1 serves with the expert ranking profiled on its own traffic (code-writing replies 7.8 → 12.8 tok/s). [Details](#new-in-v0236)
- **v0.2.35, November 2 — Flash-Next on N cards, and community GGUFs read right:** `ie serve --gpus N` runs [Flash-Next](#new-in-v0235) as an N-stage layer split (stage s owns layers [s·48/N, (s+1)·48/N)), with the request lanes, the draft head's rounds, the prompt cache, the restart points and the pictures all going through one chain, so no path can skip a stage; on this two-card box the 4-stage chain was proven byte-identical to the 2-stage one by running two stages per card (`IE_Q4E_LOGICAL_CARDS=2`), the way DeepSeek-V4.1's 4-card split was. The per-layer-embedding table of a community Q8_0 / UD-Q6_K_XL GGUF was read with the converter's IQ4_NL layout (garbage replies); it is read by its dtype now, and anything else is refused by name. The P2P context takes every card. An opt-in pinned-memory path for the expert uploads is there for boxes whose copy engine faults on the file mapping; here it cost 14–23 % of decode and made the first token 47 % later, so it is off by default.
- **v0.2.34, October 29 — Nanbeige4.3-33B, and the dense path three times faster with a prompt cache and prompt-lookup speculation:** [Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) (a plain Llama-architecture dense model, Apache 2.0, 512K context, Qwen's ChatML `<think>` template) serves at **28.7 / 27.8 tok/s on two cards** at 0.9K / 5.3K of context in 65K (6.3 / 2.6 before the port), 19.3 on one card. The shared dense path (every K-quant `llama` / `qwen3` dense GGUF) got its Q6_K projections on the c32 int-dot kernel, the fa2 decode attention under tensor parallel, a prompt cache (turn 2 of a 5.4K-token conversation prefills in 1.7 s instead of 21.4, the reply byte-identical) and prompt-lookup `--spec` (a repeated passage at **78 tok/s** on two cards, 50 on one, the texts byte-identical to plain). The Nanbeige file is our own build from the authors' release. [Details](#new-in-v0234)
- **v0.2.33, October 23 — Flash-Next's request lanes take pictures, wake on demand, and run the draft head with `--spec`:** at `ie serve --parallel 4` an image prompt was refused and the three idle lanes took 20 % of the expert cache at the load; now a request's images are staged on its lane (the replies byte-identical to one lane's, alone or in a decoding group), a lane's VRAM is allocated on its first request (**224 / 227** resident experts a layer on the cards with one conversation, were 179 / 193), and `--spec` — Dream's speculation toggle — runs the MTP draft head's rounds on a lane decoding alone. At `--ctx 262000 --parallel 4 --slot-ctx 75000`, temperature 1.0: a 9.8K-token conversation **27.3 / 26.1 / 25.4 → 28.3 / 27.2 / 26.5 tok/s** over three turns, with `--spec` **29.5 / 28.0 / 27.2**; a 17.3K document 26.3 → 26.9, with `--spec` **30.0**; the tokens the same. [Details](#new-in-v0233)
- **v0.2.32, October 22 — the XMX decode attention keeps its output in registers:** the kernel the Qwen3.8-27B and the 35B-A3B class run from 4K context now uses one 32-lane work-group of two sub-groups per 64-key chunk (the scores and the softmax once, the next block's scores computed under this block's softmax, each sub-group's half of the output in registers), with the same bits. On the 35B-A3B: a 9.8K conversation **83.7 → 86.5 tok/s**, a 17K document 77.2 → 82.0, greedy decode at a 32K-token prompt 62.8 → 69.8 (+11 %); prompt reading unchanged. [Details](#new-in-v0232)
- **v0.2.31, October 22 — Qwen3.8-35B-A3B decodes 5–6 % faster, byte-identically:** the decode step's 705 kernel launches a card are now ~460 (one quantize per activation, the shared-expert gate inside the router launch, the DeltaNet prepare in one kernel, the residual folded into the next norm, SiLU fused with its quantize), with the same tokens. In `ie serve` at ctx 262144 with 6 lanes: one request **85.4 → 90.6 tok/s**, a 9.8K conversation 80.0 → 83.7, a 17K document 73.8 → 77.2, three at once 69.7 → 71.7 each; prompt reading unchanged. [Details](#new-in-v0231)
- **v0.2.30, October 22 — Flash-Next reads 35–45 % faster and its draft head is on by default; the 27B's lanes no longer starve its rounds and cache:** in `ie serve` on two cards at `--ctx 262000`, [Flash-Next](#new-in-v0230) reads a 9.8K-token conversation to its first token in **13.0 s** (was 16.7) and a 17.3K-token document in **21.1 s** (was 26.9); the bench reads unique text at **589 / 897 / 946 / 945 tok/s** at 2K / 8K / 16K / 32K (was 466 / 666 / 698 / 711), output byte-identical. The MTP draft head loads by itself when `mtp-head.gguf` sits beside the model (greedy decode +9–19 %, tokens identical; a sampled request gets speculative sampling and the rounds pause while they do not pay). The Qwen3.8-27B at `--parallel 8 --slot-ctx 60000` decodes **17.5 → 28.7 tok/s** and answers later turns from the prompt cache in **0.6–0.75 s** (were 4 s re-reads): its idle lanes had taken the VRAM the rounds and the cache needed. [Details](#new-in-v0230)
- **v0.2.28, October 21 — DeepSeek-V4.1's October 17 weights, faster tensor parallel, 27B Q8_0 drafts:** the [1017 update of DeepSeek-V4.1-Flash](#new-in-v0228) runs unchanged (perplexity 1.538 vs 1.517 for the September weights), and the disk prompt cache and the NVMe expert file now record the weight files they were made from. Tensor parallel (`IE_DS41_TP=1`) reads a 23.6K-token prompt at **325–352 tok/s** (was 280–288). The 27B's `--spec` lanes check three rows on Q8_0: one request **30.6 tok/s** (27.4), two at once 53.1 together (49.0), the same replies. GLM-5.3-Flash no longer refuses a conversation whose earlier reply was cut inside a tool call.
- **v0.2.27, October 21 — Qwen3.8-27B: MTP on the request lanes, Q4, pictures on the lanes; DeepSeek-V4.1 on more than two cards:** with `--spec --parallel N` the [27B's request lanes](#new-in-v0227) draft with its MTP head: one request writes **38 tok/s** at Q4_K_M (27.2 plain) and **27.4** at Q8_0 (17.4), two at once 63.1 together (51.8), with the same replies. The 27B's Q4_K_M decodes 27.5 tok/s on two cards (22.8) and 27.8 on one (19.1). Pictures work on the request lanes of the 27B and the 35B-A3B class, a VRAM leak of about 100 MiB a card per request is fixed, and DeepSeek-V4.1-Flash runs on more than two cards, with opt-in tensor parallel (`IE_DS41_TP=1`: 17.2 tok/s decode on two B70s against 14.6). [Details](#new-in-v0227)
- **v0.2.26, October 20 — GLM-5.3-Flash served fast, and issue #2:** in `ie serve`, [GLM-5.3-Flash](#new-in-v0226) reads a 9.6K-token agent prompt in **32.4 s** (was 243 s), answers later turns from the prompt cache in **9.5–9.7 s** (was 273–311 s) and decodes **13.5–14.3 tok/s** (was 10.8–11.5); the re-published `glm5-next` GGUF loads. Host↔device copies on the Qwen3.8-27B and 35B-A3B two-card splits and in `--spec`'s draft head go through pinned memory, at most 64 MiB a copy, for [issue #2](https://github.com/Red-Weasel/machx-inference-engine/issues/2) (a B70 wedged under the 27B). [Details](#new-in-v0226)
- **v0.2.25, October 20 — two new models:** [Laguna S 2.1](#new-in-v0225) (118B-A8B) and Inkling-Small (276B-A12B) run in `ie serve` on one card or two; Laguna writes **33.7–35.1 tok/s** on two cards. DeepSeek-V4.1-Flash decodes **10.6 % faster** with byte-identical output. Host↔device copies on the new models and in the VRAM self-test go through pinned memory, and the 27B's `ie serve` no longer crashes on exit. [Details](#new-in-v0225)
- **Video, October 5–6:** [LTX-2.5](docs/ltx25/LTX25_ON_ARC.md) makes 5 seconds of 1280×704 video with sound in about 21 s on two Arc Pro B70 cards (stock PyTorch: 79 s).
- **v0.2.23, October 12 — MiMo faster:** MiMo-V2.6-Flash writes **23–26 % faster** with the same tokens (27.8–28.3 tok/s with its drafter, 21.8–23.3 before) and reads long prompts up to **43 % faster** in `ie serve` (37,810 tokens: 92.5 → 53.4 s). DeepSeek-V4.1-Flash decodes about 7 % faster. [Details](#new-in-v0223)
- **v0.2.21, October 7 — Flash-Next sees long images:** Flash-Next answered image prompts of more than 2,048 tokens as if there were no image (v0.2.10 through v0.2.20); fixed. A conversation edited in the middle restarts from a saved point on Flash-Next too (28.5 → 18.4 s on a 15.7K-token prompt), and image conversations keep their restart points (second turn on Flash-Next 24.8 → 3.0 s). `--spec` is now offered for the 35B-A3B class and Flash-Next. [Details](#new-in-v0221)
- **v0.2.20, October 5 — one card:** an Arc Pro B70 now runs the Qwen models on the same fast code as two cards. On **one** card the 27B at Q6_K reads **823 tok/s** (it was 190) and writes 22 (33 with `--spec`), and the 35B-A3B class at Q5_K_M reads **1,337** (that file did not load before) and writes 87. A load is tried as asked: memory estimates warn, they do not refuse. [Details](#new-in-v0220)
- **v0.2.18, October 5:** replies that copy text already in the conversation are written several times faster with `--spec` (a 1,800-token file edit: 108 s → 28 s on the 27B, 24 s → 7 s on the 35B-A3B class, 69 s → 31 s on Flash-Next), and a conversation edited in the middle restarts from a saved point. [Details](#new-in-v0218)
- **v0.2.13, October 4 — two cards:** prompts are read 1.4–3.7× faster on the Qwen models. The 27B goes from 1,037 to **2,962 tok/s** at Q8_0 and from 987 to 1,378 at Q6_K; the 35B-A3B class at Q8_0 from 1,816 to 2,896. [Details](#new-in-v0213)

<sub>Why 2,962 and 823 are not a slowdown: reading speed depends on the card count and the file. The same 27B reads 2,962 tok/s at Q8_0 on two cards, 1,378 at Q6_K on two cards and 823 at Q6_K on one card.</sub>

Intel Arc is a genuinely capable AI GPU that inference tooling has mostly ignored. **Mach X is built for it from the metal up** — no fork of llama.cpp, no PyTorch in the language-model engine (the video pipeline uses PyTorch's Intel GPU build), no vendor runtime. Hand-written SYCL kernels (XMX matrix engines, int-dot quantized GEMV, tiled FlashAttention), an OpenAI-compatible server, tensor-parallel multi-GPU, and day-one support for the newest model architectures — often running them fast on Arc *before* anyone else does.

---

## ⚡ What people run on it

<sub>Per-model launch settings, the sampler each model is served with, and the figures measured there: [docs/MODEL_SETTINGS.md](docs/MODEL_SETTINGS.md).</sub>

One video model and seven language models, each run on **two Arc Pro B70 cards** (64 GB VRAM), with host RAM holding the
experts that do not fit. Dates, workloads and methods are in [Benchmarks](#benchmarks); every date is 2026.

### 🆕 New: video with LTX-2.5

<table>
<tr>
<td width="64" align="center" valign="middle"><img src="docs/images/logo-ltx.png" width="48" height="48" alt="Lightricks LTX"></td>
<td align="left" valign="middle"><b>LTX-2.5</b> · Lightricks' text-to-video model, with sound<br>
<b>5 s of 1280×704 video in about 21 s</b> on two Arc Pro B70 cards (stock PyTorch: 79 s) · <b>a clip every 17 s</b> with one process per card · loads in 20 s</td>
</tr>
</table>

- **What runs:** the transformer is stored in 8 bits (the Q8_0 layout, 19 GB, so a whole copy fits one 32 GB card). Both cards work in every block, the 8-bit weights go straight into the XMX multiply through Mach X's own video kernels, and the model card's two-stage flow does the rest (8 steps at half size, a 2× upscale, 3 steps at full size). Measured October 5–6.
- **Not the language-model engine:** the video pipeline runs in Python on PyTorch's Intel GPU build, with Mach X kernels called on PyTorch's own queue. The video scripts are not in this repository yet.
- **Quality:** the Mach X kernels add no loss of their own against stock operations on the same 8-bit weights (28.4 dB PSNR, 0.954 SSIM); the 8-bit weights themselves cost about 26 dB against bf16 — the same scenes, with small changes in detail.
- **Known issue:** about one clip in 30 comes out invalid (all NaN) on the test machine. The script catches it, saves the evidence and makes the clip again once; the cause is not found yet.
- **Every step, the rejected experiments and the numbers:** [LTX-2.5 on two Arc Pro B70 cards](docs/ltx25/LTX25_ON_ARC.md).

### Language models

<table>
<thead>
<tr>
<th align="left" colspan="2">Model</th>
<th align="left">Weights</th>
<th align="left">Prefill <sub>tok/s</sub></th>
<th align="left">Decode <sub>tok/s</sub></th>
</tr>
</thead>
<tbody>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-qwen.png" width="36" height="36" alt="Qwen"></td>
<td align="left" valign="middle" nowrap><b>Qwen3.8-27B</b><br><sub>dense · measured Oct 4–5<br>prompt cache · vision · 16 lanes</sub></td>
<td align="left" valign="middle" nowrap>Q8_0 GGUF</td>
<td align="left" valign="middle" nowrap><b>2,962</b> <sub>2.4K</sub><br><b>3,001</b> <sub>10.7K</sub></td>
<td align="left" valign="middle" nowrap><b>24.3</b> <sub>with <code>--spec</code></sub><br><b>17.1</b> <sub>plain</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"></td>
<td align="left" valign="middle" nowrap><b>Nanbeige4.3-33B</b><br><sub>dense (llama arch) · measured Oct 29<br>two cards · 65K context · prompt cache · lookup spec</sub></td>
<td align="left" valign="middle" nowrap>Q6_K GGUF<br><sub>27 GB</sub></td>
<td align="left" valign="middle" nowrap><b>367</b> <sub>at 0.9K</sub><br><b>254</b> <sub>at 5.3K</sub></td>
<td align="left" valign="middle" nowrap><b>28.7</b> <sub>at 0.9K</sub><br><b>27.8</b> <sub>at 5.3K</sub> · <b>78</b> <sub>on repeats, --spec</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-qwen.png" width="36" height="36" alt="Qwen"></td>
<td align="left" valign="middle" nowrap><b>Qwen3.8-35B-A3B</b><br><sub>MoE · measured Oct 4–22<br>16 lanes · 15-agent replay in 77 s</sub></td>
<td align="left" valign="middle" nowrap>Q8_0 GGUF</td>
<td align="left" valign="middle" nowrap><b>2,896</b> <sub>2.4K</sub><br><b>2,808</b> <sub>10.7K</sub></td>
<td align="left" valign="middle" nowrap><b>89.0</b> <sub>at 2K</sub><br><b>86.6</b> <sub>at 9.8K</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-qwen.png" width="36" height="36" alt="Qwen"></td>
<td align="left" valign="middle" nowrap><b>Qwen3.8-Flash-Next</b><br><sub>MoE · measured Oct 22<br>native vision · 16 lanes</sub></td>
<td align="left" valign="middle" nowrap>UD-Q4_K_XL GGUF<br><sub>104 GB</sub></td>
<td align="left" valign="middle" nowrap><b>978</b> <sub>at 8K</sub><br><b>1,031</b> <sub>at 16K</sub></td>
<td align="left" valign="middle" nowrap><b>38.9</b> <sub>MTP head, greedy</sub><br><b>35.6</b> <sub>plain</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-mimo.png" width="36" height="36" alt="Xiaomi MiMo"></td>
<td align="left" valign="middle" nowrap><b>Xiaomi MiMo-V2.6-Flash</b><br><sub>MoE · measured Oct 12<br>native vision · tool calls · 120K context</sub></td>
<td align="left" valign="middle" nowrap>FP8 + MXFP4<br><sub>178 GB safetensors</sub></td>
<td align="left" valign="middle" nowrap><b>596–630</b> <sub>at 5–6K</sub><br><b>708–716</b> <sub>at 38K</sub></td>
<td align="left" valign="middle" nowrap><b>27.8–28.3</b> <sub>with drafter</sub><br><b>16.9–18.9</b> <sub>plain</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-deepseek.png" width="36" height="36" alt="DeepSeek"></td>
<td align="left" valign="middle" nowrap><b>DeepSeek-V4.1-Flash</b><br><sub>MoE · measured Sep 16–27<br>native vision · tool calls · 223K context</sub></td>
<td align="left" valign="middle" nowrap>FP8 + MXFP4<br><sub>475 GB safetensors</sub></td>
<td align="left" valign="middle" nowrap><b>304</b> <sub>at 2K</sub><br><b>319</b> <sub>at 32K–223K</sub></td>
<td align="left" valign="middle" nowrap><b>14.9–15.3</b> <sub>one request</sub><br><b>25.1–25.8</b> <sub>two lanes together</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-deepseek.png" width="36" height="36" alt="DeepSeek"></td>
<td align="left" valign="middle" nowrap><b>DeepSeek-V4-Flash</b><br><sub>MoE · measured Sep 11<br>tool calls · prompt cache</sub></td>
<td align="left" valign="middle" nowrap>MXFP4 + Q8_0<br><sub>155 GB GGUF</sub></td>
<td align="left" valign="middle" nowrap><b>571</b> <sub>at 4K</sub></td>
<td align="left" valign="middle" nowrap><b>26.1</b> <sub>at 4K</sub><br><b>32.7</b> <sub>short prompt</sub></td>
</tr>
<tr>
<td width="48" align="center" valign="middle"><img src="docs/images/logo-glm.png" width="36" height="36" alt="Z.ai GLM"></td>
<td align="left" valign="middle" nowrap><b>GLM-5.3-Flash</b><br><sub>MoE · measured Oct 20<br>MTP draft · prompt cache</sub></td>
<td align="left" valign="middle" nowrap>UD-Q4_K_XL GGUF<br><sub>host-resident experts</sub></td>
<td align="left" valign="middle" nowrap><b>300</b> <sub>at 9.6K, served</sub></td>
<td align="left" valign="middle" nowrap><b>13.5–14.3</b> <sub>as served</sub><br><b>14.0–14.4</b> <sub>runner, at 16K</sub></td>
</tr>
</tbody>
</table>

<sub>Prefill is prompt reading and decode is writing, in tokens per second; 2.4K and 10.7K are prompt lengths in tokens (`ie-prompt-bench`, prompt cache off, greedy). "Plain" is without speculative decoding; `--spec` is speculative decoding: the 27B's own MTP draft head, and on Flash-Next lookup drafts, which pay only on replies that copy text already in the conversation. Qwen figures were measured on community fine-tunes of the models: the 35B-A3B on the Qwen3.8-35B-A3B Distill (the September 26 – October 1 rows of [Benchmarks](#benchmarks) used a Qwen3.6-35B-A3B fine-tune). GLM's 300 and 13.5–14.3 are `ie serve` with its defaults on a 9.6K-token agent prompt (October 20), and 14.0–14.4 the standalone runner with its MTP draft at 16K; Flash-Next's decode with its MTP head in the standalone runner is 37.1–38.2 chat and 44.4–44.6 code (September 27), and `ie serve` does not load that head. Every figure, with its date and conditions, is listed below.</sub>

<details>
<summary><b>Every figure, with its date and conditions</b></summary>

**Qwen3.8-27B** · Q8_0 GGUF, split over both cards
- **Prefill:** 2,962 / 3,001 tok/s at 2.4K / 10.7K tokens (`ie-prompt-bench`, prompt cache off, greedy; October 4, v0.2.13; it was 1,037 / 820 before). Q6_K: 1,378 / 1,549. An earlier version of this table said 945 tok/s at 2K, measured in August.
- **Decode:** 17.1 tok/s plain; 24.3 with `--spec` (`ie serve`, temperature 0.7, short prompt) and 29.7 as the median of five short prompts (bench, greedy). Q6_K 21.5 / 19.8 plain, 26.9 / 21.6 with `--spec`; Q5_K 23.3 / 21.4 and 26.3 / 22.9 (2.4K / 10.7K-token prompts, October 4–5). An August figure of 24.5 tok/s used the opt-in tensor-parallel path (`IE_QWEN35_TP`) with speculative decoding.
- **Serving:** prompt cache (layer-split); 16 requests at once at 153.5 tok/s together, 17.2–17.3 alone (`--ctx 8192 --parallel 16`, October 1); a reply that returns a file with one identifier renamed (1,800 tokens, temperature 0.7) takes 108.5 s plain and 28.4 s with `--spec`. With `--spec --parallel N` the lanes draft with the MTP head (v0.2.27, October 21, greedy): one request 17.4 → 27.4 tok/s, four at once 64.8 / 63.9 together.
- **Q4_K_M** (October 21, v0.2.27, a Q4_K_M re-quantized from the Q8_0): decode 27.5 tok/s on two cards and 27.8 on one; a 3,382-token prompt read at 1,393 / 1,045 tok/s; one request with `--spec` 37.1–39.6, at `--parallel N` 36.0–40.2 alone and 63.1 for two together. v0.2.29 (3 rows a round, the integer-dot kernel): one request 41.9 tok/s on the lanes and 38.9 at `--parallel 1`, two together 67.8; huihui-ai's Q4_K made from BF16 43.4 / 42.5 / 74.0.
- **One card** (Q6_K, October 5): prefill 823 / 830, decode 22.0 / 20.4, 32.6 / 19.8 with `--spec`.

**Qwen3.8-35B-A3B** · Q8_0 GGUF, split over both cards; measured on community fine-tunes (October 4–5: the Qwen3.8-35B-A3B Distill; earlier rows: a Qwen3.6-35B-A3B fine-tune, where this README says "35B-A3B class")
- **Prefill:** 2,896 / 2,808 tok/s at 2.4K / 10.7K tokens (October 4, v0.2.13; it was 1,816 / 1,256). One request, cold prompt: 2K in 1.28 s (October 2), 8K in 5.96 s, 32K in 48.4 s (October 1, before v0.2.13).
- **Decode (v0.2.32, October 22):** the XMX decode attention rewritten with the same bits: served at ctx 262144 with 6 lanes a 9.8K-token conversation 86.5 / 86.1 / 83.3 tok/s over three turns (v0.2.31: 83.7 / 82.9 / 78.7), a 17.3K-token document 82.0 (77.2); `ie-prompt-bench` greedy at 2K / 9.8K / 17K / 32K-token prompts 89.0 / 86.6 / 82.4 / 69.8 (89.2 / 83.8 / 77.2 / 62.8); prefill unchanged. [Details](#new-in-v0232)
- **Decode (v0.2.31, October 22):** served at ctx 262144 with 6 lanes, temperature 0.6: 90.6 tok/s on short prompts, 83.7 / 82.9 / 78.7 over the three turns of a 9.8K-token conversation, 77.2 at a 17.3K-token document, 71.7 each with three requests at once (v0.2.30: 85.4; 80.0 / 79.5 / 75.0; 73.8; 69.7), the same tokens; `ie-prompt-bench` (greedy, prompt cache off) at 2K / 9.8K / 17K / 32K-token prompts 84.4 / 78.9 / 73.4 / 60.5 → 89.2 / 83.8 / 77.2 / 62.8, prefill unchanged at 2,465 / 2,677 / 2,643 / 2,219. [Details](#new-in-v0231)
- **Decode (earlier):** 78.2 / 72.5 tok/s plain at 2.4K / 10.7K tokens (October 4–5); 85.7 on a short prompt (October 1); 60.9 at a 33K-token prompt (September 30). One card, Q5_K_M: 87.2 / 82.9 (October 5).
- **Serving:** up to 16 requests at once, the lane count picked at load: 16 at 414.1 tok/s together, 25.9 each (October 1); the 15-agent replay takes 77.1–77.2 s (October 4; 116.1 s before v0.2.13); a file edit takes 24.3 s plain and 7.1 s with `--spec`; XML tool calls and reasoning in the OpenAI fields; native Q6_K / Q5_K; image input with `--mmproj`, on every request lane since v0.2.27.

**Qwen3.8-Flash-Next** · UD-Q4_K_XL GGUF (104 GB)
- **Lanes (v0.2.33, October 23):** pictures on all request lanes (replies byte-identical to one lane's); a lane's VRAM is allocated on its first request, so one conversation keeps 224 / 227 resident experts a layer on the cards (were 179 / 193 with three idle lanes); the MTP draft head's rounds run on a lane decoding alone with `--spec` (Dream's speculation toggle). At `--ctx 262000 --parallel 4 --slot-ctx 75000`, temperature 1.0: a 9.8K-token conversation 27.3 / 26.1 / 25.4 → 28.3 / 27.2 / 26.5 tok/s over three turns, with `--spec` 29.5 / 28.0 / 27.2; a 17.3K-token document 26.3 → 26.9, with `--spec` 30.0. [Details](#new-in-v0233)
- **Prefill:** 628 / 978 / 1,031 / 1,006 tok/s on unique 2K / 8K / 16K / 32K-token prompts at `--ctx 40000` (bench, October 22, v0.2.30; it was 461 / 677 / 712 / 725) and 589 / 897 / 946 / 945 at `--ctx 262000`; served at that context a 9.8K-token conversation reaches its first token in 13.0 s (was 16.7) and a 17.3K-token document in 21.1 s (was 26.9). The expert cache kept re-uploading the whole bank every chunk (`IE_Q4E_PF_RING`, default 96 slots; 0 = the old behaviour); output byte-identical (greedy text and a 4,096-token perplexity to every digit). Earlier figures: 470 new text / 688 repeated prompt (October 4).
- **Decode:** the MTP draft head loads by itself from `mtp-head.gguf` beside the model (`scripts/fetch_mtp_head.py` + `scripts/mtp_to_gguf.py` make it from the official checkpoint; `IE_Q4E_MTP=0` = off): greedy 35.6 → 38.9 tok/s on short prompts and 26.4 → 31.4 at 8–64K of context, tokens identical to plain decoding; a sampled request (temperature 1.0, top_k 20) gets speculative sampling — the plain sampler's distribution — at 30–33 tok/s where plain gives 31 (the rounds pause by themselves while they do not pay). Its prefill cost is ~1 % (was 17 %) and its experts load as a Q8_0 bank. `--spec` alone = the lookup drafts (40.7 on a copy prompt, 26.9 plain).
- **Serving:** native vision; up to 16 requests at once (two at 59.0–62.6 tok/s together, ×1.94–2.06; 16 at 118.4 with row batching and 128.0 at `--ctx 8192`); a file edit takes 68.7 s plain and 30.7 s with `--spec`. Image prompts longer than 2,048 tokens are read with the image since v0.2.21 (v0.2.10 through v0.2.20 dropped it).

**Xiaomi MiMo-V2.6-Flash** · 178 GB safetensors (FP8 dense, MXFP4 experts), 256 GB RAM
- **Prefill:** 596–630 tok/s at 5.4–6K and 708–716 at 38K in `ie serve`, the two cards reading overlapping pieces of the prompt (v0.2.23, October 12; 416–465 and 409–414 with that off, same build); earlier builds 434–438 at 32K and 322 at 120K (September 22–27).
- **Decode:** 27.8–28.3 tok/s with its DFlash drafter on seven agent-style prompts and 16.9–18.9 without (v0.2.23, October 12; 21.8–23.3 and 14.1–14.7 with the new code switched off, same tokens); four requests at once 25.6 tok/s together (20.6 off). Earlier builds: 23.1–23.9 chat with the drafter, 24.3 on agent-style copy edits (September 22); `--parallel 2` / `4` 28.38 / 28.46 together (September 26).
- **Also:** released and running the same day; its bundled DFlash drafter, native vision, tool calls, thinking on/off, 120K context verified, other conversations kept in host memory, up to 16 requests at once in `ie serve` (`--parallel N`, [below](#several-requests-at-once-request-lanes)).

**DeepSeek-V4.1-Flash** · 475 GB safetensors (FP8 dense, MXFP4 experts), 256 GB RAM
- **Prefill:** 304 tok/s at 2K, 319 at 32K–223K (September 16–17).
- **Decode:** 12.8 tok/s chat, 14.0 in agent loops (September 17–18); 14.9–15.3 for one request on two tool-calling prompts (September 27); with `ie serve --parallel 2`, 25.1–25.8 together (×1.68–1.69 against one request in the same run); 25.7 together at 16.
- **Also:** native vision, tool calls, 223K context, 1–2 s follow-up turns from the prompt cache, a disk prompt cache that survives rebuilds, up to 16 requests at once in `ie serve` (`--parallel N`, [below](#several-requests-at-once-request-lanes)).

**DeepSeek-V4-Flash** · 155 GB GGUF (MXFP4 experts, Q8_0 dense)
- **Prefill** 571 tok/s at 4K; **decode** 26.1 tok/s at 4K, 32.7 on a short prompt; tool calls, prompt cache. Measured on the previous driver stack (September 11).

**GLM-5.3-Flash** · UD-Q4_K_XL GGUF, host-resident experts
- **Served (`ie serve`, October 20):** a 9.6K-token agent prompt is read at 300 tok/s (first token in 32.4 s, was 243 s); each later turn restores the conversation from the prompt cache and answers in 9.5–9.7 s (was 273–311 s); decode 13.5–14.3 tok/s with the MTP draft, which is on by default (was 10.8–11.5). Prefill runs expert batches of 32+ rows (split-K GEMMs), dense projections and MLA absorbs on XMX, in 2048-token chunks. [Measurements](docs/glm53/SERVE_SPEED_2026-10-19.md).
- **Standalone runner:** prefill 156.4 tok/s at 16K (September 27); decode 14.0–14.4 tok/s at 16K (`ie-glm5next-run`, MTP draft).
- **Also:** two-GPU pipelined prefill, request lanes in a test tool (two lanes ×1.68 against one request). `ie serve` runs GLM one request at a time.

</details>

**Also runs:** <img src="docs/images/logo-openai.png" width="22" height="22" alt="OpenAI" align="middle"> gpt-oss-120B (the former flagship) and 20B · <img src="docs/images/logo-gemma.svg" width="22" height="22" alt="Gemma" align="middle"> Gemma-4 31B and 26B-A4B · the Qwen3, Qwen3-Next and Qwen2.5 families · Llama-, Mistral-, Phi- and Granite-compatible GGUFs. See [Supported architectures](#supported-architectures).

Everything runs behind one OpenAI-compatible server (`ie serve`) with tool calls. Since v0.2.0, `ie supervise` puts
several servers — one per card set — behind **one endpoint that routes by model name**, and the
[Dream Agent Harness](https://github.com/Red-Weasel/Dream-Agent-Harness) drives either one as a local agent. Since
v0.2.6, `ie serve` picks its own number of request lanes and serves a lead with up to 15 sub-agents on the 35B-A3B
class ([New in v0.2.6](#new-in-v026)).

<sub>Logos are trademarks of their owners and identify the models only; they imply no endorsement.</sub>

![DeepSeek-V4.1-Flash running locally in the Dream Agent Harness, served by Mach X on two Arc Pro B70 cards](docs/images/dream-deepseek-v41.png)
<sub>DeepSeek-V4.1-Flash on two Arc Pro B70 cards, served by `ie serve` and driven from Dream — reasoning shown, 11.7 tok/s.</sub>

---

<a id="new-in-v0242"></a>
## 🆕 New in v0.2.42

### DeepSeek-V4.1: the fixed VRAM expert set follows the conversation

v0.2.41 let the RAM set follow the traffic (an expert read from NVMe takes the coldest RAM expert's place). The VRAM set was still fixed by the ranking file: its experts have no copy in RAM, and RAM is full, so they cannot simply be made replaceable. Now, at the end of a decode step, the hottest RAM expert the step found in a replaceable slot trades places with the coldest fixed-set expert the step did not use: the old one is read back into the newcomer's place in RAM, the newcomer is copied into the fixed slot. A step's uploads also go to the experts used most lately. No extra RAM or VRAM. Default on; `IE_DS41_EXCHANGE=0` turns it off.

Measured on 2 × Arc Pro B70 + 256 GB RAM, `--gpus 2 --ctx 265000 --parallel 4 --slot-ctx 75000 --prefill-chunk 2048 --thinking on --reasoning-effort high`, temperature 1.0, the v0.2.41 conversation (a 7.7K-token document, then prose / code / prose turns of 450 tokens). Single runs; both columns were measured the same day (the v0.2.41 section's 13.9 tok/s was a slower day for the whole machine).

| | v0.2.41 | v0.2.42 |
|---|---|---|
| Decode, all three turns | 16.4 tok/s | **17.7 tok/s** |
| Experts computed on the CPU per token | 58 | 45 |
| Three requests at once (different tasks, two turns each), together | 13.8 tok/s | **17.2 tok/s** |

With the CPU leg off (`IE_DS41_CPU_MISS=0`, the bit-exact mode) and greedy sampling, the replies are identical with the exchange on and off (2,458 exchanges in that run).

What did not work, for the record: the first version exchanged whenever a candidate had twice the recent use, about six times a token. Each exchange costs about 0.8 ms of the card, so it took back five of the six milliseconds the better set saved (16.4 → 16.6 tok/s). The replay of the recorded trace found the settings that keep the set nearly as good with a fifth of the exchanges (four times the recent use, a longer memory, eight steps of rest for a layer after one) and predicted the 0.9 exchanges a token that the real run then showed.

MiMo-V2.6 can use the same exchange (`IE_DS41_EXCHANGE=1`) when the RAM for `IE_MIMO26_ADAPTIVE=1` is not there: 19.5 → 21.0 tok/s, against 25.7 for adaptive residency.

### Flash-Next: two flags that were dropped without a word

Both were found by a user on a four-card box ([issue #3](https://github.com/Red-Weasel/machx-inference-engine/issues/3#issuecomment-6805091553)).

- `--no-prompt-cache` at one request lane now reads every prompt from its first token. It was ignored: a prompt that continued the previous one still reused it. With `--parallel` above 1 a lane still continues its own conversation, and the load says so; the per-request log line states the cached tokens either way.
- `--prefill-chunk N` is not used by Flash-Next, which reads in chunks of 4096 (the fastest measured). The load now says so and names `IE_Q4E_PREFILL_CHUNK=N`, the switch that does change it.

### A container build, and the first four-card numbers

`Containerfile.b70` at the top of the tree is a contributed, pinned container build (oneAPI 2026.0.0, compute-runtime 26.35.39758.10, IGC 2.41.5) with a slim runtime image: `podman build -f Containerfile.b70 -t machx-b70 .`. It is shipped as its author built and ran it on four Arc Pro B70 cards with v0.2.39; we have not built it in our own CI yet.

The same user measured v0.2.39 on four physical B70 cards (Flash-Next Q8_0, one stage a card, one request lane, no draft head, ctx 262144), from the server's own log lines with 0 cached tokens. Their caveats apply: single observations per arm, warm caches, not a general speedup estimate.

| Prompt | Deep pipeline (default) | `IE_Q4E_NO_DEEP_PIPE=1` |
|---|---|---|
| Prose, 33,804 tokens | 564 / 549 tok/s | 414 / 432 tok/s |
| Code, 8,768 tokens | 599 / 564 tok/s | 416 / 427 tok/s |
| Code, 34,370 tokens | 836 / 824 tok/s | 494 / 503 tok/s |
| Filler with a hidden code, 195,432 tokens | 1,171 tok/s | 499 tok/s |

Replies were byte-identical across the arms, decode ran at about 31 tok/s, and the hidden code was returned at every length up to 195K tokens. The device loss they reported on v0.2.38 happened with `IE_Q4E_NO_PIN_BANKS=1`, the case v0.2.39 moved onto pinned staging by itself; their v0.2.39 runs showed no fault.

---

<a id="new-in-v0241"></a>
## 🆕 New in v0.2.41

### DeepSeek-V4.1 and MiMo-V2.6: the expert sets follow the conversation

Both models are larger than the two cards, so each layer's experts live in three places: VRAM, pinned system RAM (computed on the CPU or uploaded when needed) and, for DeepSeek-V4.1, the NVMe drive. Until now a ranking file fixed which expert lives where, on the reasoning that training equalises expert use and no replacement policy can beat a fixed set. A recorded trace of real decode traffic says otherwise: expert use is strongly recent, and a change of subject (prose to code) moves it.

`IE_DS41_PICK_TRACE=<prefix>` records every expert a decode step uses and where it lived; `scripts/ds41_cache_sim.py` replays the record through other policies without a GPU. The replay predicted the MiMo result below within 1.5 points before any engine code was written.

**DeepSeek-V4.1, default on** (`IE_DS41_PROMOTE=0` turns it off). A decode step that reads an expert from the NVMe tier already holds its bytes; when that expert has been used more lately than the layer's coldest RAM expert, the bytes are copied into that expert's place in RAM and the two trade tiers. No extra RAM, no extra read.

Measured on 2 × Arc Pro B70 + 256 GB RAM, `--gpus 2 --ctx 265000 --parallel 4 --slot-ctx 75000 --prefill-chunk 2048 --thinking on --reasoning-effort high`, temperature 1.0, one conversation: a 7.7K-token document, then three turns of 450 tokens (prose, C++ code, prose). Single runs.

| | v0.2.40 | v0.2.41 |
|---|---|---|
| Decode, prose / code / prose turn | 12.4 / 6.9 / 10.6 tok/s | **14.1 / 13.1 / 14.6 tok/s** |
| Decode, all three turns | 9.4 tok/s | **13.9 tok/s** |
| Expert uses served from NVMe, card 0 / card 1 | 7.2 / 5.6 % | 1.3 / 0.6 % |
| Prompt reading (7.7K tokens) | 238 tok/s | 244 tok/s |

The code turn's first 100 tokens ran at 8.6 tok/s and the rest at 15.5: the set adapts within about a hundred tokens of a change of subject. With the CPU leg off (`IE_DS41_CPU_MISS=0`, the bit-exact mode) and greedy sampling, the three replies are identical with promotion on and off (3,581 promotions in that run).

**MiMo-V2.6, opt-in** (`IE_MIMO26_ADAPTIVE=1`). No fixed VRAM set: every slot starts from the ranking file and is then replaced by recency; the uploads a decode step already made go to the experts used most lately; a prompt read may only replace the 8 coldest slots of a layer, so reading does not flush the set. The cost is system RAM: every expert keeps a pinned copy (149.8 GiB, about 34 GiB more than before), which is why it is not the default. When RAM is short at load the engine says so and serves on the fixed set.

| `--gpus 2 --parallel 1`, same conversation | fixed set | `IE_MIMO26_ADAPTIVE=1` |
|---|---|---|
| Experts not in VRAM when a step needs them, card 0 / card 1 | 52.0 / 42.6 % | 36.4 / 24.9 % |
| Decode, greedy, ctx 200000 | 21.0 tok/s | **27.6 tok/s** |
| Decode, temperature 1.0, thinking on, ctx 250000 | 19.0 tok/s | **23.9 tok/s** |
| Prompt reading (8.2K tokens) | 646 tok/s | 653 tok/s |

Single runs on one conversation; MiMo's output is not deterministic run to run (its CPU expert leg), so the texts of the two arms differ. Raising the share of misses that is uploaded did not help with it on (0.4: 24.4 tok/s, 0.6: 18.9).

Not built yet: the same exchange between VRAM and RAM for DeepSeek-V4.1, where RAM is too full for MiMo's "every expert has a RAM copy" (the replay: experts not in VRAM 44 → 33 % and 34 → 26 %).

### A Flash-Next load without its image encoder file is text-only again

v0.2.40 refused to load Flash-Next when no mmproj file was beside the model. The encoder is still loaded at the start whenever the file is there; without it the model loads text-only with a warning that says what to add, and image requests are refused by name. `IE_VISION_REQUIRED=1` keeps v0.2.40's behaviour, and a file `ie.env` beside the `ie` binary can hold `IE_NAME=value` defaults for one machine (the environment wins).

---

<a id="new-in-v0240"></a>
## 🆕 New in v0.2.40

### Flash-Next decodes 24 % faster, with identical output

Measured on 2 × Arc Pro B70, UD-Q4_K_XL, `--gpus 2 --ctx 262000 --parallel 4 --slot-ctx 75000 --spec --spec-k 3`, one conversation at 33–39K tokens (6 turns of 300 tokens, each after a ~1K-token tool result). Greedy replies are byte-identical to v0.2.39 in every comparison below.

| | v0.2.39 | v0.2.40 |
|---|---|---|
| decode, greedy | 37.3 tok/s | **46.2 tok/s** |
| decode, temperature 1.0 | 36.6 tok/s | **44.9 tok/s** |
| a plain step | 29.1 ms | 26.9 ms |
| a 4-row speculative round | 73.2 ms | 59.6 ms |
| the 33.4K-token prompt, read cold | 37.0 s | 33.1 s |
| ~1K new tokens a turn | 333 tok/s | 396 tok/s |
| expert slots a layer at the load (card 0 / card 1) | 221 / 185 | 304 / 280 |
| free memory on the cards while serving | ~2.2 GiB (of a nominal 4) | ~1.0–1.6 GiB |
| one lane (`--parallel 1`), decode | 38.2 tok/s | 45.9 tok/s |

A profile came first. Flash-Next has 512 experts a layer and two 32 GB cards hold about 40 % of them, so a decode step missed ~36 experts and a 4-row speculative round ~141, each a 3 MiB upload at the PCIe rate; a quarter of a round was the card waiting for those uploads. Attention does not matter here: its cost is the same at 3K and at 39K tokens.

- **Cached experts compute while missed ones upload.** The kernels of the experts already in the cache are launched first; the uploads stream beside them and only the missed experts' jobs wait. A first version that merely reordered the launches gained nothing — the small job table's upload sat behind the expert uploads on the copy engine and held everything back. `IE_Q4E_HITS_FIRST=0` = the old order. **+8 %.**
- **The speculation guard re-tries after 6 plain steps, not 48** (`IE_Q4E_MTP_OFF_STEPS=N`). With rounds cheaper, the text passes the break-even again long before 48 steps are over. **+6 %**, on the request lanes and on one lane.
- **The token embedding lives in system RAM.** The 1.2 GiB table sat on both cards (the second only embeds the draft head's 1–3 tokens a round). Rows are now gathered on the host and uploaded, 5 KiB each: 17 more expert slots a layer on each card. Costs 1.2 GiB of RAM for each stage that embeds. `IE_Q4E_HOST_EMBED=0` keeps it on the cards. **+2.7 %.**
- **Lane 0's context grows with its conversation.** The lane that holds the whole `--ctx` (lane 0 with `--parallel N`, the only lane at `--parallel 1`) took 4.3 GiB on card 0 and 4.8 GiB on card 1 from the first token. They now start at 16,384 tokens and grow in 32,768-token steps before a longer prompt is read (rows saved to RAM, slots taken from the expert cache, buffers remade, rows restored: about a second a step at 100K tokens). The cache keeps what the conversation does not use yet. Gated on a conversation from 83K to 123K tokens with a history edit and a second conversation beside it, and the same on one lane: identical replies. `IE_Q4E_ELASTIC_CTX=0` = allocated whole. **+3.8 %** at 33–39K, less as a conversation nears the full context.

- **The cards are filled to a real margin.** The expert cache used to be sized before several workspaces existed, against an estimate plus a 4 GiB reserve; in practice ~2.2 GiB stayed free, and with the elastic context ~3.8 GiB. The cache is now sized last, against the memory really left, with a 1 GiB reserve (`IE_Q4E_RESERVE_GIB=N.N`) plus the image encoder's scratch on its card. Probed through a load, a 33K read, a 1024 × 1024 image, a second lane's wake and a context growth: nothing after the load took more than 0.25 GiB. **A guard** checks free memory at every request's start and has the cache give slots back below 384 MiB (another process, the driver's own growth), so an over-committed card — where the driver starts moving device memory and decode falls to a fraction of a token a second — is not reached silently. `IE_Q4E_VRAM_GUARD=0` = off.

### Several agents at once

The same launch with C conversations decoding at once (short 4K-token conversations, 300 tokens each, greedy; `--parallel 4` for up to 4, `--parallel 8 --slot-ctx 32768` for 8, `--parallel 16 --slot-ctx 16384` for 16). Tokens a second of all conversations together:

| conversations at once | v0.2.39 | v0.2.40 | each, v0.2.40 |
|---|---|---|---|
| 1 | 35.3 | 44.8 | 44.8 tok/s |
| 2 | 55.7 | 66.7 | 33.3 |
| 4 | 59.8 | **90.0** | 22.5 |
| 8 | 65.0 | **110.8** | 13.8 |
| 16 | 47.6 | **109.2** | 6.8 |

v0.2.39 lost ground past 8 conversations (every awake lane took expert slots from a cache that was already short); v0.2.40 holds its ceiling of about 110 tok/s from 8 on.

### Flash-Next always reads images

The image encoder is part of the load at every lane count: its weights go up before the expert cache of its card is sized and its scratch is reserved, so the first picture allocates nothing. Without an mmproj file beside the model (or `--mmproj`) the model loads text-only and says so; `IE_VISION_REQUIRED=1` makes that load fail instead, naming the files to add (v0.2.40 failed it always; v0.2.41 made that a choice).

### Measuring it

- `ie-qwen4exp-profile <gguf> [gpu] [ctx] [depth]`: a plain step against 2- and 4-row verify forwards, kernel by kernel, at any depth, with miss counts; with `IE_QUEUE_PROFILING=1` or without (true wall time).
- Counters, all off by default: `IE_Q4E_FWD_STATS=1` (forwards by kind: wall, expert accesses, misses, evictions), `IE_LANES_ROUND_STATS=1` (plain steps and rounds: tokens, pipe / draft / sampling ms), `IE_Q4E_MTP_STATS=1` (the draft head's step), `IE_ALLOC_LOG_MIB=N` (every device allocation of N MiB or more).
- `tests/unit/fill_overlap_bench`: does a cache fill run beside a compute kernel on this card, alone and in a 24-layer stage in miniature.

### Tried and left off

- The per-layer router copy and job table as compute-queue kernels (`IE_Q4E_KCOPY`): 3.7 % slower / no change.
- The existing segmented-LRU eviction (`IE_Q4E_ECACHE_SLRU=1`): more misses than the default on real traffic.

### What is still slow, and not checked

- The draft head costs 9 ms of a 60 ms round, and its expert bank holds 2.4 GiB of card 1.
- A ~1K-token tool result still reads at ~370 tok/s: each chunk streams most of the expert bank across PCIe.

---

<a id="new-in-v0239"></a>
## 🆕 New in v0.2.39

### Long conversations stop re-reading themselves (Flash-Next, request lanes)

With `--parallel N` a lane's prompt cache was all or nothing: one changed token anywhere in the history re-read the whole prompt. In one 37-hour session at `--parallel 4 --spec`, ctx 262000, that happened 53 times and cost 7,711 seconds — the worst single read took 332 s for 215,566 tokens.

- **Restart points on every lane.** While a prompt is read, every stage keeps copies of its recurrent state: every 8,192 tokens and at the last four turn boundaries, in pinned system RAM, allocated on first use. A prompt that changed its history is read from the copy below the change; the KV rows under it never left.
- **Gated byte-identical** to `IE_Q4E_LANE_LADDER=0` on a 33.6K-token prompt at 2 cards, 4 lanes, `--spec`: alone, with a second lane decoding the whole time (the read goes through the lane pipe), and on a 4-stage chain.

  | Request | Before | Now |
  |---|---|---|
  | One word changed 85 % into the prompt | 38.3 s (33,584 tokens read) | 14.6 s (9,008 read) |
  | The last assistant turn rewritten | a full re-read | 30 tokens read |
  | The first word changed | a full read | a full read (nothing can be reused) |

- **A restart point never steals a lane.** It makes a lane the prompt's own only when the prompt is that lane's conversation — about as long as it, or sharing at least half of it.
- **The log names the cause.** `[q4e lanes] lane L: the prompt (N tokens) leaves the lane's conversation (S tokens) at token X (P % in), after "…": the conversation went on "…", the prompt goes on "…"`. `IE_Q4E_DIVERGE_LOG=0` drops the text.
- **Soaked** for 40 minutes on that launch (`scripts/soak/`): 116 turns up to 118K tokens with 36 in-place history edits, a repeated greedy job whose reply never changed, client disconnects and bursts — no GPU fault, no error line, 972,064 tokens not re-read.

### A reference check for any architecture and any quant

`scripts/mini_oracle/generic_mini.py` builds a tiny random model with transformers, converts it with llama.cpp's own converter (or re-quantizes it with `llama-quantize`), runs the engine on it and compares every step's logits with the reference — about a minute a shape, no download, and a planted bug must fail each check. What it found:

| Found | Now |
|---|---|
| A matrix width that is not a multiple of 64 aborted the load (10 kernels) | Fixed, with a regression test |
| Every Llama / Mistral / Granite file in Q8_0 or Q5_K was refused | Fixed |
| `qwen35moe` read no shape from the file | The shape is read; a shape other than 35B-A3B's is refused with a message naming both |
| `moe_router` did nothing for any shape but 256 experts / top-8 | A general router, unit-tested on 7 shapes |
| The shared expert ran at the routed experts' width | Its own width |

Passing against the reference: qwen3, qwen2, llama, mistral, granite, qwen35 (Q8_0); llama Q4_K_M, qwen3 Q5_K_M, qwen2 IQ4_XS, qwen3moe Q4_K_M / Q6_K. Still refused: a Q8_0 token embedding on qwen3moe / qwen3next, and `qwen35moe` shapes other than 35B-A3B (their decode rows still leave the reference on random-weight models).

### Intel GPUs without a matrix engine

A GPU with no XMX (an integrated Xe-LPG, for one) now serves the dense models (qwen3 / qwen2 / llama family) with no switch: the engine sees the missing capability and takes its SIMD kernels. On an Arrow Lake integrated GPU a 2-layer test model matches the reference (cosine 0.999998). Other architectures still need XMX.

### Stability and tooling

- `IE_Q4E_NO_PIN_BANKS=1` (the low-RAM mode) stages expert uploads through pinned memory by itself, so the copy engine never reads pageable file memory. No speed cost in that mode (347 vs 357 tok/s reading); replies identical. `IE_Q4E_PINNED_UPLOADS=0` keeps the old direct copies.
- `scripts/soak/soak.sh` — the traffic gate above, for any launch line.
- `scripts/ci/host_tests.sh` and a GitHub Actions workflow: the 19 unit tests that need no GPU, built with plain g++ on every push.
- `scripts/compare/head_to_head.sh` — Mach X against llama.cpp builds on the same box and the same file, losses included.
- `IE_Q4E_PICK_TRACE` + `scripts/q4e_cache_sim.py` — record the expert accesses of real traffic and replay them through other cache policies. First result: an opt-in segmented LRU (`IE_Q4E_ECACHE_SLRU=1`) would miss 31–39 % fewer decode accesses on mixed four-lane traffic, and measured no decode gain in a single conversation (37.5 vs 37.2 tok/s) — so it stays off.

---

<a id="new-in-v0238"></a>
## 🆕 New in v0.2.38

### Flash-Next on three or more cards: every stage reads the prompt on its own thread

The N-stage chain (v0.2.35) overlapped only stage 0 with the rest. While stage 0 read chunk k + 1, stages 1 … N − 1 read chunk k one after another on a single thread, so on four cards three stages waited in line. Now every stage after the first runs on its own thread, chunk k on stage s beside chunk k + 1 on stage s − 1, and an N-card prompt read is bounded by the slowest stage. This is GitHub [issue 3](https://github.com/Red-Weasel/machx-inference-engine/issues/3)'s finding 7, rebuilt on our gates. The reporter measured +49–52 % prompt reading at 16K+ tokens on four B70s with their version.

- **The two races the reporter hit are designed out**, in one small header (`include/ie/deep_pipe.hpp`):
  - A stage's part of a chunk waits for its producer *and* for its own previous chunk, whatever either returned, so a stage is never driven by two threads.
  - The futures are shared and captured by value.
  - Chunk k's handoff buffer is ring slot k mod N, written only after the last stage is done with chunk k − N.
- **`deep_pipe_test`** (host-only, also clean under ThreadSanitizer) runs fake stages through the ring. Every value arrives intact, every stage sees its chunks in order, and no stage ever runs on two threads. A latch that only the next stage can open proves the stages really overlap, and an error drains without running a later part.
- **Measured** on the real UD-Q4_K_XL file at four stages, two per card (`IE_Q4E_LOGICAL_CARDS=2 --gpus 2`, ctx 32768), with a 12,069-token prompt:

  | `ie serve` | before | now |
  |---|---|---|
  | one request (`--parallel 1`) | 572 tok/s | **910 tok/s** |
  | request lanes (`--parallel 4`) | 610 tok/s | **975 tok/s** |
  | two stages on two cards (unchanged) | 921 tok/s | 921 tok/s |

  The replies to the prompt and to a follow-up turn are byte-identical in every row (the deep and the previous form, one request and the lanes, two and four stages); the follow-up restarts from the prompt cache in ~0.6 s. On four real cards each stage has a card to itself, so the gain should be larger, but we cannot measure that here.
- Restart points, the draft head's record and the request lanes' prefill all run through it. Two cards are unchanged (there is no middle stage to overlap). `IE_Q4E_NO_DEEP_PIPE=1` gives the previous form, and the startup log names the deep pipeline when it runs.

<a id="new-in-v0237"></a>
## 🆕 New in v0.2.37

### Qwen 4, day one: the shapes it may ship in, tested before the weights exist

Qwen 4's tiers are not out, and the rumoured ones differ from Flash-Next in size and layout. The new mini end-to-end check, [`scripts/qwen4exp_oracle/mini_gate.sh`](scripts/qwen4exp_oracle/README.md), builds a 4-block model with seeded random weights from the Hugging Face reference classes, writes it as a GGUF in llama.cpp's `qwen4exp` layout with every converter transform applied, runs the engine on it three ways (token-by-token decode, one prefill, a prefill split in two) and scores the logits against the reference's. It needs no download and takes about 30 s a shape. A negative control (one wrong norm transform in one block) must fail, and does.

- **Found and fixed:** hidden 5120 lost the GPU (the per-layer-embedding kernels and the dense-matmul scratch were sized for Flash-Next's 2560); a file without the QSA indexer was refused (it now attends densely); a dense model (no experts, a SwiGLU FFN in every block) was refused and now runs through the int-dot GEMV, the batched rows and the s8 GEMM; the `qwen4` / `qwen4moe` arch names read with the file's own key prefix.
- **15 shapes match the reference:** Flash-Next's own, 4 KV heads, no indexer, hidden 5120, dense at 2560 and at 5120 (with 4 KV heads and no indexer), head_dim 128, 32 Q / 8 KV heads, 64 experts top-8, 32 DeltaNet value heads, no per-layer embedding, 8 hyper-connection streams, low rank 512, a fused gate/up bank and the `qwen4` arch name. Decode rows and a prefill split in two reach cosine ≥ 0.999, a one-shot prefill ≥ 0.9998; rows where the reference's router scores nearly tie are held to 0.995, because F16 routing may pick the other expert there.
- The dense and hidden-5120 shapes, given the real tokenizer, pass `ie preflight` and answer a chat through `ie serve` on one card and on a two-card split.
- **Fused gate/up expert banks** (llama.cpp's `--fuse-gate-up-exps`, `ffn_gate_up_exps`) load, in the model and in an MTP head file: each expert's halves are split while the bank is copied to pinned host memory, so every kernel is unchanged, and the logits are byte-identical to the separate-bank file's. They were refused before.
- **On four cards:** checked on a 4-stage chain, two stages per card here (`ie-qwen4exp-run2 <file> 4 2`, the `--gpus 4` split): the real Flash-Next file and 8-block mini models with Q8_0 expert banks (Flash-Next's shape, dense, hidden 5120, fused banks) give logits bit-identical to one card, and `ie serve` of the dense shape on four stages answers exactly as on one card and on two.
- The real Flash-Next file's output is bit-identical before and after these changes.

### Flash-Next decodes faster again, with the same tokens

- **The hyper-connection mixing reads the file's 8-bit blocks** at decode and verify instead of F16 copies (half the bytes at 97 sites a step): the mixing 3.24 → 2.19 ms a step, two cards 44.3 → 47.2 tok/s. `IE_Q4E_HC_Q8=0` is the F16 path.
- **Expert routing on the GPU when it pays:** while the decode miss rate stays at or below 2 %, a MoE layer routes on the device straight into the expert-job table, and a missed expert is read from pinned host memory in place. The host routes with the device's arithmetic bit for bit, so the side never changes a token. Two cards 47.1 → 49.7 tok/s; a cold one-card cache stays on the host. `IE_Q4E_DEV_ROUTE=0` is host routing.
- **The QSA decode attention splits a head's keys into 64 tiles** (was 16): 131 → 44 µs a layer, the one-card step at ~3.1K context 21.0 → 20.1 ms of GPU time. `IE_Q4E_QSA_TILES=16` gives v0.2.36's sums bit for bit.
- Two cards **44.4 → 49.7 tok/s** over v0.2.36 (`ie-prompt-bench`, UD-Q4_K_XL, measured at each step). Every step was checked with the batched-verify probe, lossless speculation and the greedy text.

### EXL3: all three exllamav3 codebooks

turboderp's Flash-Next EXL3 quants use the `mul1` codebook, and the EXL3 kernels decoded only the default one (3INST), so they would have read such tensors as wrong values without a word. The kernels now decode 3INST, mcg and mul1 (device == host on all 65,536 codes of each). The importer refuses an `.mcg` / `.mul1` tensor by name until the GGUF carries its codebook. Flash-Next itself has no EXL3 path yet.

### What is still not checked
- A dense model's MTP draft head is refused (serving uses lookup drafts), and a dense model's request lanes decode one at a time (no row batching).
- A per-layer embedding on more than one block, or with a geometry other than Flash-Next's, is refused by name: no converter writes one yet.
- Tensor names a release adds that nobody has published cannot be tested before the files exist.

<a id="new-in-v0236"></a>
## 🆕 New in v0.2.36

### Qwen 4, day one: Flash-Next's every community quant streams natively

Qwen3.8-Flash-Next (`qwen4exp`) is the preview of Qwen 4's architecture. The Unsloth UD-Q5_K_XL, UD-Q6_K_XL and Q8_0 builds — and the Qwen 4 builds that will follow the same recipe — carry Q8_0 down banks on every layer and Q5_K / Q6_K / Q8_0 gate/up banks; bartowski's carry Q5_0 down banks. The engine streamed only Q4_K gate/up and Q5_1 down banks raw and dequantised everything else at load to a pinned host F16 copy (2 bytes an element): the Q8_0 file needed about 225 GiB of RAM and ran at 0.7 tok/s for the [issue 3](https://github.com/Red-Weasel/machx-inference-engine/issues/3) reporter.

- **New bank kernels** stream Q8_0, Q5_K, Q6_K, Q5_0 and Q4_0 banks as they lie on disk at every MoE site — decode, the speculative verify, the prefill tiles, the row batches — one column walk per type shared by every variant, so each is bit-identical to the solo kernel (`ie-qwen4-bank-test`, against an fp64 reference). On real banks the raw path is 4.5–4.8e-4 from fp64 where the old F16 copy was 1.0–1.8e-2. `IE_Q4E_RAW_KQ=0` is the old copy.
- **Proven on the real files:** Unsloth's UD-Q6_K_XL and Q8_0 builds load with every bank streaming raw, score 5.470 and 5.473 perplexity on the same prose the Q4 file scores 5.491 on, and decode losslessly under speculation with either MTP head. Integer-dot Q5_K / Q6_K gate/up kernels (decode and prefill) run at 308–395 GB/s where the floating-point unpack ran ALU-bound at ~100 GB/s: on UD-Q5_K_XL two-card decode 32.3 → 34.1 tok/s and prefill 104 → 124 tok/s for 0.3 % perplexity, the same int8-activation trade the Q4_K path makes (`IE_Q4E_KQ_INTDOT=0` keeps the unpack). int8-DPAS gate/up tiles and exact-int f16-DPAS down tiles for the Q8_0 banks: the Q8_0 build's two-card prefill 87.4 → 103.9 tok/s, perplexity 5.473 → 5.443.
- **The loader takes what the converters write:** llama.cpp's merged tensors (`attn_qkv_gate`, `ssm_beta_alpha`, `hc_*_down_inject`), every dtype with a reference dequant, the n-gram table in Q5_0 / Q5_1 / Q4_0 / F16 / BF16 / F32 beside IQ4_NL / Q8_0. A fused `ffn_gate_up_exps` bank is refused with the reason.
- **The MTP draft head in llama.cpp's layout:** Unsloth's `MTP/mtp-Qwen3.8-Flash-Next-{Q8_0,shared-Q8_0}.gguf` (a 49th block, `blk.48.nextn.*`) or a main file converted with the head inside; found beside the model, in `../MTP/` or inside it, and `--spec-head` takes either. Unsloth's head is lossless against plain greedy decoding like ours.
- **The config reader takes llama.cpp's hyperparameters:** a per-block `attention.recurrent_layers` schedule, `full_attention_interval` defaulting to 4, head counts and the expert FFN size as per-block arrays, the MTP blocks counted in `block_count`; where the kernels are fixed (a QSA compress ratio other than 4, a top-k not a multiple of 4) the load names the limit instead of selecting the wrong blocks. A `qwen35` pre-tokenizer matches the HF tokenizer on 30 of 30 golden lines.
- **Found and fixed on the way:** the batched-verify probe had not been bit-identical to serial decode for batches above four rows since the hyper-connection mix got its small-batch grid (the two grids add the fp32 sums in a different order); the verify path runs the mix in four-row pieces now. The default speculative shape (four rows) never was affected.

### Flash-Next decodes faster, with identical output

Measured on the UD-Q4_K_XL file with `ie-prompt-bench` (two cards, 128 tokens × 3) and the kernel profiler at ~3K tokens of context on one card; every change was checked bit-identical (the batched-verify probe, lossless speculation, the greedy text byte for byte):

- **Fewer launches a MoE layer:** SwiGLU fused into the grouped gate/up kernels, the ordered reduce + the shared expert's gated add + the cast in one launch, one pick-table copy a layer, the shared expert through the batched int-dot path (17 launches + 2 copies → 12 + 1 a layer); the hyper-connection combine fused with the next mix's norm; the shared expert queued behind the router read so the GPU works while the host routes.
- **The QSA decode attention 3× faster:** the query row in registers, the next key's rows loaded before the current key's softmax chain, the per-lane arrays sized at compile time (a runtime trip count had sent them to private memory): 393 → 131 µs a layer.
- **The router GEMV 4× faster:** the F16 rows kernel read each row's activation from global memory inside its loop; one row now runs the plain kernel and 2–8 rows stage their activations in shared local memory (the router 29 → ~7.7 µs a call; the speculative verify's four rows 37 → 12 µs).
- Two cards **41.1 → 44.4 tok/s**; the step at ~3K context **26.2 → 21.0 ms** of GPU time (wall 33.2 → ~28 ms).

### A request's own text can no longer forge a control token

Every chat renderer built its prompt by joining the template's markers with the request's strings, and the serve tokenised the whole string with special-token matching on — so the spelling of a control token inside a user message, a tool result or a tool argument (a page a tool fetched, say) became that control token: it could open a turn, end the model's reasoning or open a tool-call block. Now only the markers the template itself inserted are control tokens, the rule the official DeepSeek API states: `Tokenizer::encode` takes the byte ranges of the request's text and keeps a spelling inside them as text, and every renderer records those ranges (DeepSeek-V4.1, ChatML / Qwen, GLM5, MiMo, Laguna, Inkling, Llama-3, Mistral, R1-distill, DeepSeek-V4, Granite, Gemma, gpt-oss). No request is refused for it and nothing changes for a request without a spelling in its text: the golden suites hold and 4,016 old-vs-new renders are byte for byte identical. The raw-prompt completion endpoint is the caller's own text and keeps specials on.

### Also
- **Tool calls whose JSON lost its last bracket are repaired:** the closers owed at the end of a parameter are added when every string is closed and nothing dangles after a comma or a colon; an unterminated string, a trailing comma or a missing value stay errors.
- **DeepSeek-V4.1 serves with the expert ranking profiled on its own traffic** once the served profile holds 100K generated tokens (`IE_DS41_RANKING` overrides; the init line says which): on a code-writing reply 7.8 → 12.8 tok/s, the NVMe tier's share of selections 9 % → 1.6 %.
- The V4.1 staging tier's huge-page warning names the pool, the free pages and the processes holding them.
- `scripts/env.sh` pins the oneAPI compiler the build directories are configured with (`IE_ONEAPI_COMPILER`, default 2026.1): a newer oneAPI install linked 2026.1's SYCL runtime against the new loader and nothing linked.

### What is still slow, and not checked
- Speculation on Flash-Next at one card is not faster than plain decoding (36.1 vs 35.7 ms a token on the profile's text): the verify's four rows touch more experts than one.
- Expert pinning from a usage histogram (`IE_Q4E_EXPERT_PINS`, `IE_Q4E_EXPERT_HIST`) is built and lossless but measured no gain here: within a sequence the cache already keeps the hot set. Opt-in.
- A cold prefill chunk streams the experts that miss the VRAM cache over PCIe at link rate; the remaining prefill cost on the big quants is that upload, not a kernel.

<a id="new-in-v0235"></a>
## 🆕 New in v0.2.35

### Flash-Next on N cards: the layer split as a chain, proven on two

A 4 × Arc Pro B70 user ([issue 3](https://github.com/Red-Weasel/machx-inference-engine/issues/3)) wanted Flash-Next on all four cards. The engine's split was a pair, A → B, and `--gpus` was clamped at two. Now:

- **`--gpus N`** loads an N-stage chain: stage s owns layers [s·48/N, (s+1)·48/N) on card s (24 / 24 at two cards, 12 each at four); the wide state crosses every stage boundary through the host; each stage sizes its own expert cache from its card's free VRAM and logs its range (`[qwen4exp] stage 2/4: layers [24, 36) on card 2`). The device-to-device wide push (`IE_P2P=1`) stays a two-stage feature: the reporter measured the host bounce faster on B70, and so did we.
- **One chain for every path.** The forward, the pipelined prefill (stage 0 reads chunk k+1 while the rest of the chain runs chunk k), the MTP draft head's verify rounds and their commits, the prompt-lookup rounds' snapshot and restore, the prompt cache, the in-place restart points, the request lanes' stash and the shared-prefix store, the pictures' staging: each goes through the bundle's stage list, so a new path cannot skip a stage. The reporter's own first cut wired the middle stages into some paths and not others; a 4-card serve ran 24 of 48 layers and passed every gate he had.
- **The request lanes over the chain:** `--parallel N` at any stage count. The card pipe runs one thread per stage; the middle stages read and rewrite the lane's wide buffer; the tail keeps the logits, the sampler and the head.
- **Proven on two cards.** `IE_Q4E_LOGICAL_CARDS=k` (a test switch) runs each card as k stages, the way DeepSeek-V4.1's four-card split was proven here in October. At the owner's launch (`--gpus 2 --ctx 262000 --parallel 4 --slot-ctx 75000`) with `IE_Q4E_LOGICAL_CARDS=2` — a four-stage chain on two cards — the greedy replies to one, three and four requests at once and to an 8K-token prompt are byte-identical to the two-stage serve's. With the request lanes over the chain at the same launch (`--parallel 4`, four stages on two cards) the replies to one, three and four requests at once and to the 8K prompt are byte-identical to the two-stage serve's and to v0.2.34's, and the lazy lanes wake on every stage. With `--spec` as well, the full launch does not fit the two-card emulation (two stage contexts with four lanes each on one card, plus the 4.7 GiB head and its per-lane state, leave the tail 20 slots a layer, and the lanes' admission refuses the load, as it should); at `--ctx 131000 --slot-ctx 40000` the four-stage `--spec` serve is byte-identical to the two-stage one on all four request sets. The gate tool `ie-qwen4exp-run2 <gguf> [stages] [cards]` checks an N-stage chain's logits bit-for-bit against the one-card reference, counts every stage on every forward, and `IE_Q4E_RUN2_SKIP_STAGE=s` is its self-check (a chain that skips a stage fails it): on this box, 4 and 3 stages on two cards pass it (prefill logits identical to one card, every stage counted on every forward, the pipelined prefill identical to the serial chain), and the self-check fails it with the skipped stage's count at 0. Served the same way at `--parallel 1` (ctx 262000, the draft head's rounds on), the four-stage chain's greedy replies and 8K-prompt reply are byte-identical to the two-stage serve's, the prompt cache restores across the chain on later turns, and each of the four stages keeps 82–147 expert slots a layer from its half of a card.
- Four real cards were not available to us; the reporter's numbers on v0.2.35 would be the first.

### Community GGUFs: the per-layer-embedding table read by its dtype

The engine's own converter writes Flash-Next's `per_layer_token_embd.weight` as IQ4_NL (90 bytes a row); the community files (Unsloth Q8_0, UD-Q6_K_XL) carry it as Q8_0 (170 bytes a row). The gather read every table as IQ4_NL, so a community file loaded and answered garbage. The table is read by its dtype now; any other dtype, or a table whose bytes do not match its row count, is refused by name at load. `ie-qwen4-ple-test` gates the Q8_0 rows byte-for-byte against the reference dequant. (The routed-expert banks of those files still take the load-time F16 copy, 1.88× the file in host RAM; the raw Q8_0 streaming is a separate piece of work.)

### Also
- `gpu_p2p_shared_context` keeps every matching card and enables peer access both ways for every pair (it capped at two).
- **The expert uploads through pinned host memory, opt-in (`IE_Q4E_PINNED_UPLOADS=1`).** The issue-3 reporter saw the copy engine fault on the file mapping under page-cache pressure (`bcs -ENOENT`), on UD-Q4_K_XL too, and staged every upload through pinned memory. Built here as a ring of 32 pinned entries, one DMA a slot, measured at the owner's launch: the tokens identical, but a 9.4 MiB CPU copy per expert miss costs decode 28.5 / 27.0 / 26.0 → 24.4 / 21.7 / 20.0 tok/s over three turns, the first token 13.6 → 19.9 s, concurrent greedy requests 29–74 % longer, and the bench's reading 161 → 144 tok/s (that bench run also started with a colder page cache, so the served figures are the ones to trust). It stays off unless a box needs it; we never saw the fault here (no `xe` fault lines in any gate run).
- IGC 2.41.15 miscompiles a qwen4exp kernel on the reporter's box (all-nonfinite logits); 2.41.5 stays the pin (docs/INTEL_STACK_LIVING.md).
- A stray empty file named `src/*.cpp` was tracked and published; it is gone.

### What is still slow, and not checked
- Four physical cards: not measured here. The chain's per-stage expert caches should grow with the cards (the reporter saw 319–336 slots a layer at four cards against 70 at two on his Q8_0 file); the decode gain is his to measure.
- The deep per-stage prefill pipeline (every stage one chunk behind the previous, as the reporter's patch 0006 does) is not built: stage 0 runs ahead and the rest of the chain runs together behind it. At four stages that leaves the middle cards idle during a chunk; a later phase.
- Q8_0 expert banks stream through a host F16 copy at load.

---

<a id="new-in-v0234"></a>
## 🆕 New in v0.2.34

### Nanbeige4.3-33B, and the dense path three times faster: a prompt cache and prompt-lookup speculation for every dense GGUF

[Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) (BOSS Zhipin, Apache 2.0, a plain Llama-architecture dense model with a 512K context and Qwen's ChatML `<think>` template) loads as a `llama` GGUF and serves at **28.7 tok/s on two cards with 65K of context** (`--gpus 2 --ctx 65536`; 6.3 before the port, 24 after its first pass), 19.3 tok/s on one card at 8K. Getting there fixed three things in the engine that any dense GGUF on this path benefits from:

- **Correctness for a llama-arch GGUF with a ChatML thinking template:** the reasoning split and the thinking switch were gated on a Qwen architecture, so the model's thinking leaked into `content`; and a GGUF that declares `<|im_start|>` as its BOS got a doubled tag at the start of every prompt (25 / 30 tokens where llama.cpp has 24 / 29), which made the thinking-off reply ramble. Both fixed; the engine's thinking-off reply is byte-identical to llama.cpp's on the same render.
- **The dense path's Q6_K projections on the c32 int-dot kernel** (the kernel the 27B split already used): the four K = 7168 projections per layer ran a W6A16 SLM-slab GEMV at 132 GB/s, 80 % of a decode step; now 51 ms a token instead of 168 on one card. The load-time Q8_0 copy of ffn_down is gone with it: on a 33B it was a second 8.7 GB of one tensor that over-committed the card and halved prefill. `IE_DENSE_KQ_C32=0` keeps the old path.
- **The two-card tensor-parallel dense path ran the naive prefill attention at T = 1**, so decode cost grew with context (11.5 tok/s at 900 tokens, 3.3 at 5K); it takes the fa2 decode kernel now: 24.2 and 23.6.

Perplexity on the same text as llama.cpp: 21.05 before, 20.94 after (llama.cpp 22.28 by its half-context method; 15.20 vs 15.27 on identical positions). Measured against llama.cpp on the identical GGUF: tokenizer ids identical on 5,400 tokens, every layer's activations at cosine 0.9998 or better. Settings and numbers: docs/MODEL_SETTINGS.md.

**October 29: the dense path's serving features.** The generic dense path (every `llama` / `qwen3` dense GGUF) had none of what the Qwen splits have. One-card loads now run on the two-card class on a one-card fleet, so the features are built once:

- **A prompt cache** (the engine's fleet prefix cache on the per-card KV): turn 2 of a 5.4K-token conversation restores 5,250 of its 5,414 tokens in 6 ms and prefills in 1.7 s instead of 21.4, the warm reply byte-identical to a cold one. Making the class's decode body run the one-card class's launch sequence (the fused norm + Q8 quant, the int-dot lm_head over a load-time SoA repack) took two-card decode from 24.4 to **29 tok/s**.
- **Prompt-lookup speculative decoding** (`--spec`): when the text being written repeats something in the context, the following tokens run as one forward of up to 16 rows and the sampler is answered from those rows; a row it does not follow costs only a length reset. A repeated passage decodes at **78 tok/s on two cards** (50 on one), 515 of 539 drafts accepted; prompts without repetition decode at exactly the plain speed, and every gate text is byte-identical to plain.
- Request lanes (`--parallel` up to 16) for the dense path are the next phase.

The Nanbeige file served here is our own build from the authors' release (the per-layer refusal-direction edit and its before/after report are in docs/MODEL_SETTINGS.md), not a third-party upload.

**Also in this release — DeepSeek-V4.1-Flash's NVMe tier and the first copy on each card.** The tier's 16 staging slots a tier were anonymous memory imported into the driver, which does not pin such a mapping: every page the kernel split, compacted or swapped forced a rebind on the card's own migrate queue, the queue that hung in three of three unrecoverable card-0 wedges, each time with the host under heavy reclaim. The slots are hugetlb pages now when the host has a pool (`vm.nr_hugepages`, 320 of 2 MiB here), never moved by the kernel; without a pool, or when the driver refuses the import, the anonymous slots of before with a warning naming the sysctl (`IE_DS41_STAGE_HUGETLB=0` keeps them). The first DMA on each card waits at most `IE_DS41_LINK_PROBE_DEADLINE_S` (10 s) a copy and then exits 76 with the diagnosis (the PCI link, the journal line, the devcoredump path) instead of hanging the load; `ie supervise` does not relaunch on that code.

### What is still slow, and not checked
- No request lanes on the dense path yet: `--parallel N` queues the requests. The next phase.
- With the prompt cache on, the prompt's last few tokens run as their own small forward (the int-dot rows kernel and the naive attention), so a one-card greedy reply can drift at a near-tie after 50–80 words against a cache-less prefill, and a warm turn's wall is mostly that tail (164 tokens in 1.7 s).
- `--int8-kv` on this path keeps the fp16 cache too (no VRAM saving).
- The speculative decoding was checked on one card and two (the texts byte-identical to plain on every request, 515 of 539 drafts accepted) by its author only; a second, independent pass over it is still to come.
- The abliterated file: 7 of 48 held-out harmful prompts still refuse with thinking off, about 37 % with thinking on; a wider layer window is the next iteration.

<a id="new-in-v0233"></a>
## 🆕 New in v0.2.33

### Flash-Next's request lanes: pictures on every lane, lanes that wake on demand, and the draft head's rounds with `--spec`

At `ie serve --parallel 4` — the usual Flash-Next launch — three things were wrong with the request lanes. An image prompt was refused (`image inputs need --parallel 1`) although the 27B and the 35B-A3B class have taken pictures on their lanes since v0.2.27. The three idle lanes took 3 × 1.13 GiB a card at the load whether or not a second request ever came, so the expert cache held 179 / 193 resident experts a layer (cards 0 / 1) instead of 224 / 227. And the MTP draft head, the default at one lane since v0.2.30, was never loaded on the lanes: every turn was plain decoding at 23–26 tok/s.

- **Pictures on all request lanes.** A request's images are encoded on its own thread and staged on its lane (its image rows and its M-RoPE table); the request stays out of the prompt cache (pad ids cannot key it); a decoding group may hold a lane with pictures — its rows rope at the lane's offset, the same arithmetic the one-lane path runs once the three streams are equal. The vision tower is placed at the load, before the expert caches are sized (on card 1, or on card 0 when the head's bank takes card 1), so no late allocation lands beside a full card; `/props` says `images on all N request lanes`. The greedy reply to a 1024-px photo is byte-identical at `--parallel 1` and on the lanes, alone and beside two text requests, and the text requests' replies are the one-lane path's.
- **Lazy lanes.** A lane's VRAM is allocated on its first request and taken back from the expert cache then: every layer's cache buffer is remade smaller and the page-alias self-test runs again (about 0.3 s a card; the residents stream back in over the next few hundred tokens). One conversation at a time keeps 224 / 227 experts a layer on the cards; the chooser prefers a lane that is already awake, so a second conversation wakes one more. `IE_Q4E_LAZY_LANES=0` is the eager load.
- **The draft head's rounds on the lanes, with `--spec`** (Dream's speculation toggle, offered for Flash-Next since v0.2.21): a lane decoding alone drafts with the head and verifies the drafts in one step — one lane's sampled rounds (speculative sampling, exact at any temperature; a greedy request compares), the tokens plain decoding's; the head's record is kept per lane. More lanes decoding share the cards in rows groups as before. It is opt-in on the lanes because the head's expert bank costs card 1 about 35 resident experts a layer, which three or four conversations decoding at once feel (−17 % in the table); one conversation gains. At one lane the head stays the default. `IE_Q4E_LANES_MTP=0` turns the rounds off with the head loaded; `IE_Q4E_LANES_MTP_MAX` lets more lanes round.

| `ie serve`, two B70s, `--ctx 262000 --parallel 4 --slot-ctx 75000`, temperature 1.0 / top_k 20 / top_p 0.95 | v0.2.32 | v0.2.33 | v0.2.33 `--spec` |
|---|---|---|---|
| a 9.8K-token conversation, decode over turns 1 / 2 / 3 | 27.3 / 26.1 / 25.4 | **28.3 / 27.2 / 26.5** | **29.5 / 28.0 / 27.2** |
| a 17.3K-token document | 26.3 | **26.9** | **30.0** |
| short prompts, median of three | 29.6 | 30.4 | 30.0 |
| three requests at once, 256 tokens each, lanes warm (time to finish) | 14.3 s | 14.5 s | 16.9 s |
| four at once | 17.3 s | 18.1 s | 20.7 s |
| resident experts a layer, cards 0 / 1, one lane awake | 179 / 193 | **208 / 210** | 191 / 162 |

Gates: the greedy texts with the rounds on and off are byte-identical on one lane, in three- and four-lane groups and on an 8K prompt; a conversation's text is the same before and after another lane wakes; the one-lane lossless tool is unchanged (`ie-qwen4exp-spec2`: 44.2 tok/s, 2.12 tokens a round). The first request on a lane pays the wake (+0.5 s on a cold 9.8K first token). The rounds' acceptance at temperature 1.0 moves from run to run: an earlier run of the same code gave 29.8 / 32.7 / 27.1 on the conversation and 32.0 on the document.

### What is still slow
- The head's expert bank on card 1 (2.5 GB as Q8_0) is what the concurrent case pays; placing it on card 0 does not help (that card has less room to begin with). A Q4_K bank or a bank of the head's most-used experts would give 15–25 slots back.
- On a lane with pictures the head drafts from the pad tokens' view of the prompt (its rope knows no images); the verify is exact, so the tokens are plain decoding's, and a picture description still went 120 tokens in 50 steps. A shared-prefix restore breaks the head's record for that request (plain steps until its next sequence).
- The rows path still ingests each group row into its lane's head record when the head is loaded (not measurable in the table, but there).

Other models: their code did not change; the shared lanes module accepts a draft shorter than the round (the 27B always drafts the full round).

<a id="new-in-v0232"></a>
## 🆕 New in v0.2.32

### The XMX decode attention keeps its output in registers, with the same bits

`full_attention_fa2_decode_xmx` — the decode attention the Qwen3.8-27B and the 35B-A3B class run from 4K context (head_dim 256) — ran one 16-lane work-group per (KV head, 64-key chunk) with the running output in local memory: every 16-key block loaded, multiplied and stored all 16 output tiles through SLM, and the 16 K-tile loads, the 8-lane softmax and the 16 P·V tiles ran one after the other. Latency-bound, about 0.12 ms a layer at 8K for 17 MB of KV. The new kernel (`IE_FA2_XMX_V2=3`, the default) uses one 32-lane work-group of two sub-groups per chunk: sub-group 0 computes the scores and the row softmax once, sub-group 1 computes the next block's scores meanwhile (into the other of two score buffers), and both accumulate their half of the output columns in `joint_matrix` registers; the FA-2 rescale goes through SLM only on the blocks where a row's max moved, the same multiply on the same values. Every fp32 operation on every output element is the old kernel's in the old kernel's order, so the bits are the same.

Gates on the 35B-A3B: the standalone outputs (`ie-attn-profile --mode xmx --dump-y`) byte-identical to the old kernel's at 4K–32K; the engine's greedy texts byte-identical on one lane and on three concurrent lanes; the 128-token greedy continuations of 2K / 8K / 16K / 32K-token prompts byte-identical (the ones that run this kernel).

| 35B-A3B Q8_0, two B70s | v0.2.31 | v0.2.32 |
|---|---|---|
| `ie serve` ctx 262144, 6 lanes: a 9.8K-token conversation, turns 1 / 2 / 3 | 83.7 / 82.9 / 78.7 | **86.5 / 86.1 / 83.3** |
| the same, a 17.3K-token document | 77.2 | **82.0** |
| `ie-prompt-bench` (greedy, prompt cache off), prompts of 2K / 9.8K / 17K / 32K tokens | 89.2 / 83.8 / 77.2 / 62.8 | **89.0 / 86.6 / 82.4 / 69.8** |
| `ie-qwen35moe-bench`, 8.3K context | 85.3 | **88.2** |
| three requests at once, short prompts | 71.7 | 71.7 |

The gain grows with context (+3 % at 10K, +7 % at 17K, +11 % at 32K); prompt reading is unchanged. Standalone, the partial pass at the 35B shape takes 0.07 / 0.10 / 0.25 ms a layer at 8K / 16K / 32K against 0.12 / 0.15 / 0.34 (−35–40 %). Two intermediate variants stay in the code for the A/B: `IE_FA2_XMX_V2=1` (two 16-lane work-groups per chunk with the scores and the softmax computed by both — bit-identical but slower in the engine, 83.7 → 78.9 at 9.8K: the duplicated K reads cost more than the SLM traffic saved) and `=2` (the new kernel without the pipelining); `=0` is the old kernel. The 27B uses the same kernel at head_dim 256; it was byte-checked standalone, not timed in the engine.

`ie-attn-profile` gained `--dump-y FILE` (the output vector after every context's sweep, the byte check) beside `--mode xmx`; time it with `--layers 10` — one short kernel a step lets the GPU's clock drift and the numbers do not repeat.

### What is still slow
- For one request the two cards still take turns (4.3 + 5.2 ms a token); expert-parallel across both is the larger lever.
- The router's two kernels (1.3 ms a token on the 35B-A3B), the rows path's per-lane DeltaNet conv and recurrence launches, and this kernel's combine pass.

<a id="new-in-v0231"></a>
## 🆕 New in v0.2.31

### Qwen3.8-35B-A3B decodes 5–6 % faster, byte-identically

At `ie serve --ctx 262144 --parallel 6 --slot-ctx 40000` the 35B-A3B's request lanes and prompt cache were already in good shape (0.41 GiB a lane, 4.8 GiB of snapshots a card), so the work went to the decode step: 12.4 ms a token, of which 10.4 ms GPU-busy in **705 kernel launches a card**, the expert and dense weight streams near the memory roofline and about 1.7 ms a card in small kernels at the launch floor. Five changes bring the launches to ~460 a card with the same tokens — the greedy texts of one lane and of three concurrent lanes equal v0.2.30's byte for byte:

- one `quantize_q8_1` per activation: each norm quantizes its own row in the same launch (`rms_norm_f32w_quant_q8_1`, `residual_add_rms_norm_{exact,fused}_quant_q8_1`), and the projections and the MoE read it (`pre_q8` on the dense GEMV routes; the q projection's quantization serves k and v, the qkv projection's the DeltaNet gate, the MoE's the shared expert);
- the shared-expert gate's serial chain runs as an extra work-group of the router's dot launch (`moe_router`'s `sh_gate_w` / `sh_gate_out`), not as its own ~14 µs kernel;
- the DeltaNet prepare (split, two L2 norms, two tiled repeats) is one launch, `dn_qkv_split_norm_fused` (its B70 kernel is `l2_128`'s lane order and fma chain), on the single-lane and the rows path; the padded alpha/beta row is read in place;
- `x += moe_y` rides with the next layer's norm (`residual_add_rms_norm_exact`: `residual_add`'s clamp and fp16 rounding, then `rms_norm_f32w`'s loop);
- the SiLU product and `sh_down`'s activation quantize are one launch (`swiglu_quant_q8_1`).

| `ie serve`, two B70s, ctx 262144, 6 lanes, temperature 0.6 | v0.2.30 | v0.2.31 |
|---|---|---|
| one request, short prompts | 85.4 tok/s | **90.6** |
| a 9.8K-token conversation, turns 1 / 2 / 3 (TTFT 3.6 / 0.4 / 0.3 s) | 80.0 / 79.5 / 75.0 | **83.7 / 82.9 / 78.7** |
| a 17.3K-token document (TTFT 5.3 s) | 73.8 | **77.2** |
| three requests at once, each | 69.7 | **71.7** |
| `ie-qwen35moe-bench`, 8.3K context | 80.7 | **85.3** |
| `ie-prompt-bench` (greedy, prompt cache off), prompts of 2K / 9.8K / 17K / 32K tokens | 84.4 / 78.9 / 73.4 / 60.5 | **89.2 / 83.8 / 77.2 / 62.8** |

Prompt reading is unchanged (the prefill path keeps every kernel: 2,465 / 2,677 / 2,643 / 2,219 tok/s at those four prompts on both builds). The per-token profile (`IE_DECODE_PROF=1 IE_QUEUE_PROFILING=1`) after the third set: 705 → 491 launches a card, GPU-busy 4.72 / 5.65 → 4.34 / 5.18 ms, the idle gaps between kernels down to ~0.06 ms a card. The MTP head in the GGUF is not used on this model: a 4-row verify re-reads up to four times the experts, so a round costs ~1.8 steps for ~2.1 tokens.

### What is still slow
- The XMX decode attention's partial pass: one sub-group per 64-key chunk with the running output in local memory, ~0.16 ms a layer at 8K (about 17 % of the card's bandwidth), growing with context — at a 32K-token prompt this release gains only 4 % (60.5 → 62.8) because the attention owns the step there. A register-resident rewrite that keeps the bits is next.
- For one request the two cards still take turns (4.3 + 5.2 ms a token); expert-parallel across both is the larger lever.
- `ie-attn-profile` gained `--mode xmx` (the 27B/35B decode kernel at head_dim 256); its partials scratch is now sized for that kernel — the old sizing overran under it and could take the card down at 32K.

<a id="new-in-v0230"></a>
## 🆕 New in v0.2.30

### Flash-Next reads 35–45 % faster, byte-identically

A 2,048-token chunk routes nearly every one of a layer's 512 experts, and the VRAM expert cache holds about 257 of them, so the LRU, walked in ascending expert order, evicted each resident expert just before its turn: every chunk uploaded the whole bank again (~40 GiB per card). Now the experts resident at a chunk's start keep their slots for the pass, misses stream through a 96-slot ring, and the resident experts' jobs run first (`IE_Q4E_PF_RING`, 0 = the old LRU). The per-token sums keep their order, so the output is byte-identical: the greedy text of five prompts and a 4,096-token perplexity equal to every digit.

| unique text, two cards, `ie-prompt-bench` | 2K | 8K | 16K | 32K |
|---|---|---|---|---|
| v0.2.29, `--ctx 40000` | 461 | 677 | 712 | 725 |
| **v0.2.30**, `--ctx 40000` | **628** | **978** | **1,031** | **1,006** |
| v0.2.29, `--ctx 262000` | 466 | 666 | 698 | 711 |
| **v0.2.30**, `--ctx 262000` | **589** | **897** | **946** | **945** |

Served at `--ctx 262000` (temperature 1.0, top_k 20): a 9.8K-token conversation reaches its first token in 13.0 s (was 16.7), a 17.3K-token document in 21.1 s (was 26.9). A 4,096-token pipeline chunk reads 16–32K prompts another 6–10 % faster but is not the same arithmetic (perplexity 1.0841 → 1.0854 over 8,192 tokens), so it stays an opt-in (`IE_Q4E_PIPE_CHUNK=4096`) until that is understood.

### Flash-Next's MTP draft head is on by default, and exact at any sampler

The head loads by itself when `mtp-head.gguf` sits beside the model (`scripts/fetch_mtp_head.py` and `scripts/mtp_to_gguf.py` make the 5.2 GB file from the official checkpoint; `IE_Q4E_MTP=0` = off), 3 rows a round. Its ingest ran the head's whole layer for every prompt token it read and nothing used the result (−17 % prefill): the ingest now stops after the attention half. Its experts load as a Q8_0 bank (the tail card keeps 186 instead of 157 expert slots at `--ctx 262000`). Greedy requests keep the bit-exact compare path: 35.6 → 38.9 tok/s on short prompts, 26.4 → 31.4 at 8–64K of context, the tokens plain decoding's. A sampled request used to lose with it (argmax drafts kept only when the sampled token happened to match: 31.0 → 26.1 tok/s at temperature 1.0 / top_k 20); now the drafts are drawn from the head's own distribution and verified by speculative sampling, a confidence gate ends an unsure draft (`IE_Q4E_MTP_QMIN`, 0.5), and a guard measures each request's plain step against its rounds and pauses them while they do not pay (`IE_Q4E_MTP_ADAPT=0` = always on). On this MoE a 4-row verify streams about 27 distinct experts against a step's 10, so a round costs about 2.6 plain steps and pays above about 2.6 tokens a round: maths and document conversations gain, free prose at temperature 1.0 comes out about even (30.7 / 29.6 / 33.4 against 31.4 / 31.1 / 30.8 plain). `IE_Q4E_LOOKUP_STATS=1` prints the rounds and the guard's yardstick per request.

### Qwen3.8-27B: the request lanes no longer starve the rounds and the prompt cache

At a launch like `--ctx 222222 --parallel 8 --slot-ctx 60000 --spec` on Q8_0, the seven idle lanes allocated 13.3 GiB a card at the load, the MTP rounds were then refused on "32 MiB free" and the prompt cache sized itself at 0 GB: the 27B decoded plain (17.5 tok/s) and re-read every turn (4.0 s for 10K tokens), where `--parallel 1` gave 29. Now a lane's state is allocated when a request first lands on it (`IE_QWEN35_LANES_EAGER=1` = at the load as before), the lane choice prefers an idle lane that is already allocated, and the prompt cache hands back what a filling lane takes (its budget re-fits to the cards' measured free memory). At those flags, served at temperature 1.0 / top_k 20: decode 17.4 / 17.5 / 17.5 → 20.7 / 28.7 / 29.5 on short prompts and 16.6 / 16.6 / 16.2 → 19.8 / 20.8 / 20.3 on a 9.8K-token conversation, whose turns 2 and 3 come from the cache in 0.75 / 0.61 s (were 4.0 s re-reads); a 17K prompt reads at 2,552 tok/s as before; two concurrent requests 17.1 / 16.5 each (as before). The engine's load log says what it allocates: `[27b-split-cache] lane N filled: the cache's budget a → b GB a card`.

### What is still slow, and not checked

- The 4,096-token pipeline chunk on Flash-Next (+6–10 % at 16–32K) changes the logits; opt-in until the differing kernel is found.
- Flash-Next's draft head still takes 52 expert slots of the tail card at `--ctx 262000` (7–8 % of prefill there); a smaller bank or the head on the roomier card would recover it. Its rounds on this MoE cost ~2.6 plain steps for 4 rows; a verify that reuses the step's routed experts would raise the sampled gain above "about even".
- The 27B's two concurrent lanes with rounds decode 17.1 / 16.5 each at the launch above, not the `--parallel 2` figure of 53 together; the round checkpoints are sized for every lane (1.7 GiB for 8 at K = 3) where a pool for the two that draft at once would be 0.4 GiB.
- None of the other models changed code; their tokens are v0.2.29's.

<a id="new-in-v0229"></a>
## 🆕 New in v0.2.29

Everything since [v0.2.28](https://github.com/Red-Weasel/machx-inference-engine/releases/tag/v0.2.28). Measured
October 21, 2026, on two Arc Pro B70 cards. All of it is the Qwen3.8-27B (and the 35B-A3B class's Q6_K / Q5_K
experts); every other model gives v0.2.28's tokens.

### Qwen3.8-27B: MTP checks cost less on the K-quants, and every file drafts 2 tokens a round

The decode kernel for Q4_K, Q5_K and Q6_K weights now takes its integer dot products from the GPU's own integer dot
instruction instead of building them byte by byte. The integers are the same, so the results are the same bit for bit,
and each extra row of an MTP check costs much less: Q4_K `ffn_down` at 1 / 3 / 4 rows went from 95 / 148 / 179 µs to
88 / 119 / 135. With that, every file now checks 3 rows a round (2 drafted tokens) by default, on the request lanes and
at `--parallel 1`; `--spec-k` still sets it.

| Qwen3.8-27B, `--spec`, two cards, 256 tokens a reply | v0.2.28 | v0.2.29 |
|---|---|---|
| Q4_K_M, one request (`--parallel 2`) | 37.2 tok/s | **41.9** |
| Q4_K_M, two at once, together | 63.2 | **67.8** |
| Q6_K, one request / two together | 31.8 / 52.5 | **37.4 / 61.8** |
| `--parallel 1`, one request: Q4_K_M / Q6_K / Q8_0 | 36.0 / 29.9 / 26.8 | **38.9 / 34.7 / 29.4** |

- Plain decoding is unchanged or a little faster (Q4_K_M two lanes 27.2 / 51.8 → 27.7 / 53.5); the 35B-A3B class's
  Q6_K experts take the same kernel change (two lanes 94.6 / 173.9 → 95.8 / 176.6 tok/s, the same text).
- **A better Q4 file for `--spec`:** huihui-ai's own `Huihui-Qwen3.8-27B-abliterated-Q4_K.gguf`, quantized from BF16,
  accepts more drafts than a Q4_K_M we re-quantized from the Q8_0 (2.00 against 1.92 tokens a round): **43.4 / 74.0**
  tok/s on two lanes, **42.5** at `--parallel 1`, plain the same 27.7. Its perplexity is within 0.2 % of the
  re-quantized file's (16,127 wikitext tokens: 4.784 against 4.775; Q8_0 4.728).
- **Checks:** every `--spec` reply has the same text and token count as plain decoding (lanes and `--parallel 1`,
  Q4_K_M, Q6_K and Q8_0, both Q4 files); the kernel unit test checks Q4_K, Q5_K and Q6_K rows against one row bit for
  bit. Four Q8_0 lanes with `--spec`: 8 of 8 replies the same as plain and as v0.2.28 (63.8 tok/s together). Every
  other model gives v0.2.28's tokens (Flash-Next, the 35B-A3B class, the 27B 