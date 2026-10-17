# Awesome Jev Alternatives [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open, self-hostable alternatives and building blocks for System One style decision models.

TypeSafe AI's Jev is a closed model that answers typed yes/no, choice, and score questions with probabilities. The large awesome-jev catalogs list software built on that hosted API. This list is the other side: open engines, reproductions, calibration tools, datasets, and papers on fast logprob judgments.

Entries are alphabetical inside each section. Each link was fetched, and each GitHub repository was read from the GitHub API for stars, the license identifier, and the last push. Archived repositories are omitted. A repository with no push in 365 days is omitted unless the entry is marked historical. Descriptions name a limitation. They do not repeat benchmark tables this list did not run.

## Contents

- [Decision engines](#decision-engines)
- [Runtimes and ports](#runtimes-and-ports)
- [Zero-shot classifiers](#zero-shot-classifiers)
- [Calibration](#calibration)
- [Benchmarks and datasets](#benchmarks-and-datasets)
- [Research](#research)
- [Related lists](#related-lists)

## Decision engines

- [CLM](https://github.com/Contrastive-LM/CLM) - Contrastive model that embeds a state and each candidate with a frozen Qwen3-8B plus small heads. The server accepts yes/no, choice, and score questions. Serving the 8B encoder needs a GPU, the citation is a Notion note rather than a paper, and the documented speedup comes from caching a reused action set.
- [decider](https://github.com/Mapika/decider) - Fine-tune of Qwen3.5 that returns choice, score, and yes/no distributions in one forward pass, with published sizes from 0.8B to a 35B mixture-of-experts. The larger checkpoints need a GPU. A prior long-state check, not re-run for this list, put the 0.8B checkpoint under a constant-answer baseline; the bigger sizes were not in that check.
- [jevlike](https://github.com/vinnylarouge/jevlike) - Small option scorer you train yourself, with a byte encoder or a frozen pretrained encoder. The author calls it a research starter: the byte encoder is weak, and the repo does not claim parity with Jev.
- [Kev](https://github.com/jaredpalmer/kev) - Decision models on Qwen3.5 and Qwen3.8 with yes/no, choice, and score questions, a temperature file per checkpoint, and a TypeSafe-shaped server. The project documents sizes from 0.8B to 27B, so the large checkpoint needs a big GPU, and the weights are a separate training run.
- [Laya](https://github.com/NandhaKishorM/laya) - Encoder model (ModernBERT and mmBERT) with a decision head for choice, score, and yes/no, a language router, and a Jev-shaped HTTP server that can run on CPU. The project says the base checkpoints are a fine-tune base, not a zero-shot engine, and a prior long-state check, not re-run for this list, put them under a constant-answer baseline. Choice labels written as yes/no or true/false are unsafe on the shipped checkpoints.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Small Qwen3-0.6B model with decision heads that emit a distribution over candidates, aimed at game actions such as ViZDoom. It is a task model with a training pipeline, not a general text router.
- [Open Alternative to Jev](https://github.com/ikermoel/open-alternative-jev) - Library that reads option probabilities from an open-weights model in one forward pass through Hugging Face or vLLM. You supply the GPU and the base model; it does not ship a trained decision checkpoint.
- [Open-Jev](https://github.com/Zefan-Cai/Open-Jev) - LoRA decision adapters and a scalar head on large open bases, with a workbench and notes for smaller GPUs. The 27B package still expects a GPU, and the comparison figures in the README are the author's.
- [open-jev-typed-decision-engine](https://github.com/intikhab49/open-jev-typed-decision-engine) - Training scripts and a Colab notebook for a 150M non-autoregressive decision model, including a temperature step. It is a recipe that expects a T4, not a maintained inference server, and the accuracy figures are the author's.
- [OpenJev (DiffusionGemma)](https://github.com/razorback16/openjev) - Jev-shaped server that reads typed answers from DiffusionGemma through vLLM on an NVIDIA GPU or MLX on Apple silicon. It is tied to that model family and to a GPU or a Mac.
- [openjev (Gemma)](https://github.com/daseinlabs/open-jev) - One-pass option scoring on Gemma 3 4B, on Apple MLX or on PyTorch CPU or GPU, by reading option-token log-probabilities. A 4B model is heavy on CPU, and it scores the option strings rather than a single letter token.
- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) - Reads declared option logits from a frozen open model in one forward pass, with shared-state prefill and a browser demo. The documented CUDA path wants a GPU that holds a 4B model; a llama.cpp CPU path is included and is slower. It reproduces the request shape, not Jev's training.
- [Verdict](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - ModernBERT-sized decision engine, about 151M parameters, with calibration code and an in-browser WebGPU demo. The LICENSE file is Apache-2.0 text, while the GitHub license API returns NOASSERTION, and the accuracy numbers in the README were not re-run here.
- [Von](https://github.com/wfzyx/von) - Non-autoregressive decision model with a local server and a TypeSafe-shaped API. It is a small open model with the author's own benchmarks, not a copy of Jev's weights.

## Runtimes and ports

- [Allan Boll's letter-logprob wrapper](http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html) - Single Python function, published inline on a blog, that softmaxes one-step letter logprobs into yes/no, choice, or score answers, including images, via llama.cpp or the OpenAI Responses API. The post does not call the scores calibrated, there is no versioned license, and a server that drops logprobs gives it nothing to read. xAI's docs say grok-4.20 and newer silently ignore logprobs.
- [JEV-CPU](https://github.com/leesk212/JEV-CPU) - CPU port of SemIf's logit readout, plus a small web UI, so the forward pass does not need a GPU. Quality is limited to the GGUF that fits on the machine.
- [laya-mlx](https://github.com/mizorewww/laya-mlx) - MLX runtime that loads Laya's own checkpoints on Apple silicon, including that project's temperature buckets. It does not run an NVIDIA build, and it inherits Laya's zero-shot limits, including the long-state baseline miss.
- [Ollaya](https://github.com/ollaya-dev/ollaya) - Rust runtime that pulls open decision models, including Laya, decider, Kev, Von, NLI, and GLiClass, and serves one of them behind a TypeSafe-shaped local API. The API docs have no ensemble, and the runtime does not fix a weak checkpoint: the long-state check of Laya and decider 0.8B stayed under a constant-answer baseline.
- [stuntd](https://github.com/bladedevoff/stuntd) - Local proxy that answers Jev-shaped requests with stock Laya or with a small head trained on labels it records. It is marked v0.1, and until a head is trained, unsure calls go back to an upstream provider, which may be paid Jev.

## Zero-shot classifiers

- [GLiClass](https://github.com/Knowledgator/GLiClass) - Zero-shot sequence classifier that scores every label in one forward pass. It is a label scorer, not a choice, score, and yes/no server, and the DeBERTa-sized models are a poor fit for long agent state.
- [Zeroshot classifiers](https://github.com/MoritzLaurer/zeroshot-classifier) - Training notebooks for NLI models that score each label as an entailment hypothesis. Cost grows with the label count, the last push was December 2024, and this historical entry is here because the Hugging Face checkpoints are still what people run.

## Calibration

- [Calibrated confidence demo](https://github.com/WestdeutscherRundfunkKoeln/calibrated-confidence-demo) - Demo that reads a score from the logprob distribution over score tokens in one chat call. It needs an API that returns logprobs, it is GPL-3.0, and it scores judgments rather than hosting a decision model.
- [MAPIE](https://github.com/scikit-learn-contrib/MAPIE) - Conformal-prediction library that turns classifier scores into prediction sets and risk controls. You bring the scores; it does not run a language model.
- [net:cal](https://github.com/EFS-OpenSource/calibration-framework) - Python library for measuring miscalibration, including ECE, and for applying temperature scaling to classifier probabilities. It has no notion of choice, score, or yes/no questions.
- [Temperature scaling](https://github.com/gpleiss/temperature_scaling) - Short reference implementation of the scalar temperature from Guo et al. The last push was July 2025, outside the one-year window, so this is the historical method rather than a maintained project, and it is not a language-model server.

## Benchmarks and datasets

- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) - Static Hugging Face page listing decision-model checkpoints and writeups, including open weights. It is a catalog of other people's results, not a harness in this repository.
- [jev-laya-classification-bench](https://github.com/bhushankinge/jev-laya-classification-bench) - Pipeline that labels U.S. federal IT solicitations with Jev, Laya, and Qwen3.5-35B and compares them with reseller quotes. One procurement domain, and the Jev arm needs an API key.
- [Korean Decision Benchmark](https://github.com/jkf87/korean-decision-benchmark) - Colab notebook and scripts that run SemIf, decider, Laya, and Jev on Korean hate-speech comments. The open models want a GPU, and the Jev column needs an API key.
- [typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) - English synthetic rows with yes/no, choice, and score labels over a shared state, covering customer service, invoices, security incidents, and agent traces, under Apache-2.0. Hugging Face records the set as under 1K rows.

## Research

- [Balancing Classification and Calibration](https://arxiv.org/abs/2601.13284) - Study of the accuracy-versus-calibration tradeoff when fine-tuning decision-token probabilities, plus a calibration-aware reinforcement-learning objective. No code repository was verified for this paper.
- [Building Efficient Universal Classifiers with NLI](https://arxiv.org/abs/2312.17543) - Method paper for treating each label as an entailment hypothesis. A large label set costs one forward pass per label, unlike a single-pass decision head.
- [GLiClass paper](https://arxiv.org/abs/2508.07662) - Write-up of the single-pass label scorer. The runnable library is the GLiClass entry above.
- [Improving LLM-as-a-Judge Inference with the Judgment Distribution](https://arxiv.org/abs/2503.03064) - Argument for using the distribution over score tokens instead of the greedy score digit. It assumes the API exposes logprobs, and it evaluates judgments rather than a self-hosted decision model.
- [Just Ask for Calibration](https://arxiv.org/abs/2305.14975) - Comparison of verbalized confidence and token probabilities for models fine-tuned with human feedback. A reason not to treat raw logprobs as calibrated.
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) - Study of what token probabilities reveal about a model's own knowledge, including a P(True) probe. It does not ship a decision server.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) - Source paper for temperature scaling, one scalar on the logits. It predates language-model decision engines; the short code is the Temperature scaling entry.

## Related lists

- [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev) - Catalog of open-source projects built with hosted Jev. Applications live there; this list does not repeat them.
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) - Curated list of public projects and discussions that use Jev for a typed decision. Same boundary: hosted-API apps stay on that list.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this work. The waiver is [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
