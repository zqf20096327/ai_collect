<div align="center">

# Awesome Continuous Language Models

**The paper collection for our survey, *A Survey on Continuous Diffusion and Flow Language Models*.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-137-blue)
[![alphaXiv](https://img.shields.io/badge/alphaXiv-Survey-b31b1b)](https://www.alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://continuous-lm.github.io/)

<a href="https://sophtang.github.io/">Sophia Tang</a><sup>1</sup> &emsp; <a href="https://david3684.github.io/">Chanhyuk Lee</a><sup>2</sup> &emsp; <a href="https://flooreijkelboom.github.io/">Floor Eijkelboom</a><sup>3</sup> &emsp; <a href="https://jw9730.github.io/">Jinwoo Kim</a><sup>2</sup>

<sub><a href="mailto:sophtang@engineering.upenn.edu">sophtang@engineering.upenn.edu</a> &emsp; <a href="mailto:chanhyuk-lee@kaist.ac.kr">chanhyuk-lee@kaist.ac.kr</a> &emsp; <a href="mailto:f.eijkelboom@uva.nl">f.eijkelboom@uva.nl</a> &emsp; <a href="mailto:jinwoo-kim@kaist.ac.kr">jinwoo-kim@kaist.ac.kr</a></sub>

<sup>1</sup> University of Pennsylvania &emsp; <sup>2</sup> KAIST &emsp; <sup>3</sup> University of Amsterdam

<!-- GitHub only plays README videos hosted at github.com/user-attachments. For a video player, drag assets/paper_map_demo.mp4 into GitHub's web editor and replace this link with the URL it gives you. -->
<a href="assets/paper_map_demo.mp4"><img src="assets/paper_map_demo.gif" alt="Demo of the interactive map of continuous language models" width="100%"></a>

<sub>A tour of our <a href="https://continuous-lm.github.io/map/">interactive paper map</a>.</sub>

[News](#news) · [What are continuous language models?](#what-are-continuous-language-models) · [Start here](#-start-here) · [Recently added](#-recently-added) · [More papers](#-more-papers) · [Contributing](#contributing) · [BibTeX](#bibtex) · [Star History](#star-history)

</div>

## News

- **Nov 9, 2026**: The survey is live on [alphaXiv](https://www.alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models).
- **Nov 9, 2026**: Our [Map of Continuous Language Models](https://continuous-lm.github.io/map/) and [paper list](https://github.com/sophtang/Awesome-Continuous-Language-Models) are live.

## What are continuous language models?

> Continuous language models generate text by transforming noise into continuous representations of tokens, then decoding those representations into tokens.

These representations include learned embeddings, compressed latents, points on the probability simplex or sphere, and one-hot or binary encodings. A continuous model can refine many token positions in parallel while preserving the dependencies between them. By contrast, autoregressive models predict one token at a time, and discrete diffusion models operate directly on token sequences. This collection also includes hybrid models that combine discrete and continuous dynamics, as well as applications such as reasoning and biological sequence design.

For a comprehensive understanding of the field, read our [survey paper](https://www.alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models). Also be sure to check out some of the amazing blog posts on ideas in this field:
- [Continuous Diffusion Language Models](https://sander.ai/2026/08/24/continuous-dlms.html) by Sander Dielman (24 Aug 2026)
- [How to Generate Text in One Step](https://one-step-lm.github.io/blog/index.html) by Jinwoo Kim and Nicholas M. Boffi (4 Apr 2026)
- [An Intuitive Introduction to Flow-Based Language Generation](https://flow-based-llms.github.io/) by Floor Eijkelboom (Apr 2026)
- [How to Train a One-Step Language Model Without a Teacher](https://sophtang.github.io/discrete-beckmann-transport/blog/) by Sophia Tang (Oct 2026)

## 🌟 Start here

These are the representative models from the model table in our survey. The table lists embedding and latent models first, then simplex and spherical models, flow and flow map models, and hybrid models.

| Paper | Links | Venue | Representation | Formulation | Main loss | Few-step | Key feature |
|:--|:--|:--|:--|:--|:--|:--|:--|
| <b>Diffusion-LM</b> Improves Controllable Text Generation | <a href="https://arxiv.org/abs/2205.14217">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2205.14217">alphaXiv</a> · <a href="https://github.com/XiangLi1999/Diffusion-LM"><img src="https://img.shields.io/github/stars/XiangLi1999/Diffusion-LM?style=social&label=Code" alt="Code"></a> | NeurIPS 2022 | Learned vocab. emb. | Gaussian diff. | MSE + CE | – | Classifier guidance |
| <b>DiffuSeq</b>: Sequence to Sequence Text Generation with Diffusion Models | <a href="https://arxiv.org/abs/2210.08933">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2210.08933">alphaXiv</a> · <a href="https://github.com/Shark-NLP/DiffuSeq"><img src="https://img.shields.io/github/stars/Shark-NLP/DiffuSeq?style=social&label=Code" alt="Code"></a> | ICLR 2023 | Learned vocab. emb. | Gaussian diff. | MSE + CE | – | Seq2seq denoising |
| <b>CDCD</b>: Continuous Diffusion for Categorical Data | <a href="https://arxiv.org/abs/2211.15089">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2211.15089">alphaXiv</a> | arXiv 2022 | Learned vocab. emb. | Gaussian diff. | CE | – | Learned time warp |
| <b>Plaid</b>: Likelihood-Based Diffusion Language Models | <a href="https://arxiv.org/abs/2305.18619">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.18619">alphaXiv</a> · <a href="https://github.com/igul222/plaid"><img src="https://img.shields.io/github/stars/igul222/plaid?style=social&label=Code" alt="Code"></a> | NeurIPS 2023 | Learned vocab. emb. | Gaussian diff. | ELBO | – | Learned noise schedule |
| <b>Sigma</b>: Large Language Continuous Diffusion Models | <a href="https://arxiv.org/abs/2610.02665">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.02665">alphaXiv</a> | arXiv 2026 | Learned vocab. emb. | Gaussian diff. | ELBO + AR CE | Distill. | Uniformity regularization |
| <b>SED</b>: Self-conditioned Embedding Diffusion for Text Generation | <a href="https://arxiv.org/abs/2211.04236">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2211.04236">alphaXiv</a> | arXiv 2022 | Frozen vocab. emb. | Gaussian diff. | MSE + readout CE | – | Self-conditioning |
| <b>LD4LG</b>: Latent Diffusion for Language Generation | <a href="https://arxiv.org/abs/2212.09462">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2212.09462">alphaXiv</a> · <a href="https://github.com/justinlovelace/latent-diffusion-for-language"><img src="https://img.shields.io/github/stars/justinlovelace/latent-diffusion-for-language?style=social&label=Code" alt="Code"></a> | NeurIPS 2023 | Compressed latents | Gaussian diff. | $v$-MSE | – | Pretrained AR decoder |
| <b>LDLM</b>: How to Train Your Latent Diffusion Language Model Jointly With the Latent Space | <a href="https://arxiv.org/abs/2605.07933">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.07933">alphaXiv</a> | arXiv 2026 | Contextual latents | Gaussian diff. | MSE + recon. losses | – | Joint latent learning |
| <b>SSD-LM</b>: Semi-autoregressive Simplex-based Diffusion Language Model for Text Generation and Modular Control | <a href="https://arxiv.org/abs/2210.17432">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2210.17432">alphaXiv</a> · <a href="https://github.com/xhan77/ssd-lm"><img src="https://img.shields.io/github/stars/xhan77/ssd-lm?style=social&label=Code" alt="Code"></a> | ACL 2023 | Simplex | Gaussian logits | CE | – | Semi-AR blocks |
| <b>TESS</b>: Text-to-Text Self-Conditioned Simplex Diffusion | <a href="https://arxiv.org/abs/2305.08379">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.08379">alphaXiv</a> · <a href="https://github.com/allenai/tess-diffusion"><img src="https://img.shields.io/github/stars/allenai/tess-diffusion?style=social&label=Code" alt="Code"></a> | EACL 2024 | Simplex | Gaussian logits | CE | – | Self-conditioning |
| <b>Dirichlet FM</b>: Dirichlet Flow Matching with Applications to DNA Sequence Design | <a href="https://arxiv.org/abs/2402.05841">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2402.05841">alphaXiv</a> · <a href="https://github.com/HannesStark/dirichlet-flow-matching"><img src="https://img.shields.io/github/stars/HannesStark/dirichlet-flow-matching?style=social&label=Code" alt="Code"></a> | ICML 2024 | Simplex | Dirichlet flow | CE | Distill. | Classifier / CFG guidance |
| <b>Gumbel-Softmax FM</b>: Gumbel-Softmax Flow Matching with Straight-Through Guidance for Controllable Biological Sequence Generation | <a href="https://arxiv.org/abs/2503.17361">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2503.17361">alphaXiv</a> | arXiv 2025 | Simplex | Gumbel-softmax | CE | – | Straight-through guidance |
| <b>Fisher-Flow</b>: Fisher Flow Matching for Generative Modeling over Discrete Data | <a href="https://arxiv.org/abs/2405.14664">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2405.14664">alphaXiv</a> · <a href="https://github.com/olsdavis/fisher-flow"><img src="https://img.shields.io/github/stars/olsdavis/fisher-flow?style=social&label=Code" alt="Code"></a> | NeurIPS 2024 | Sphere | Geodesic flow | Riemannian FM | – | Fisher–Rao geometry |
| <b>S-FLM</b>: Language Modeling with Hyperspherical Flows | <a href="https://arxiv.org/abs/2605.11125">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.11125">alphaXiv</a> · <a href="https://github.com/jdeschena/s-flm"><img src="https://img.shields.io/github/stars/jdeschena/s-flm?style=social&label=Code" alt="Code"></a> | arXiv 2026 | Spherical emb. | Geodesic flow | CE | – | State dimension $d\ll V$ |
| <b>FLM</b>: Flow Map Language Models: One-step Language Modeling via Continuous Denoising | <a href="https://arxiv.org/abs/2602.16813">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.16813">alphaXiv</a> · <a href="https://github.com/david3684/flm"><img src="https://img.shields.io/github/stars/david3684/flm?style=social&label=Code" alt="Code"></a> | arXiv 2026 | One-hot | Linear flow | CE | – | Time reparameterization |
| <b>LangFlow</b>: Continuous Diffusion Rivals Discrete in Language Modeling | <a href="https://arxiv.org/abs/2604.11748">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.11748">alphaXiv</a> · <a href="https://github.com/nealchen2003/LangFlow"><img src="https://img.shields.io/github/stars/nealchen2003/LangFlow?style=social&label=Code" alt="Code"></a> | arXiv 2026 | Learned vocab. emb. | VP flow | CE | – | Learned noise schedule |
| <b>ELF</b>: Embedded Language Flows | <a href="https://arxiv.org/abs/2605.10938">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.10938">alphaXiv</a> · <a href="https://github.com/lillian039/ELF"><img src="https://img.shields.io/github/stars/lillian039/ELF?style=social&label=Code" alt="Code"></a> | arXiv 2026 | Contextual emb. | Linear flow | Velocity MSE + CE | Distill. | Single-pass guidance |
| <b>CFM</b>: Categorical Flow Maps | <a href="https://arxiv.org/abs/2602.12233">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.12233">alphaXiv</a> · <a href="https://github.com/olsdavis/semicat"><img src="https://img.shields.io/github/stars/olsdavis/semicat?style=social&label=Code" alt="Code"></a> | ICML 2026 | One-hot | Flow map | CE + consistency | Self-dist. | Endpoint consistency |
| <b>FMLM</b>: Flow Map Language Models: One-step Language Modeling via Continuous Denoising | <a href="https://arxiv.org/abs/2602.16813">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.16813">alphaXiv</a> · <a href="https://github.com/david3684/flm"><img src="https://img.shields.io/github/stars/david3684/flm?style=social&label=Code" alt="Code"></a> | arXiv 2026 | One-hot | Flow map | Semigroup CE | Distill. | FLM teacher |
| <b>DFM</b>: Discrete Flow Maps | <a href="https://arxiv.org/abs/2604.09784">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.09784">alphaXiv</a> | arXiv 2026 | One-hot | Flow map | CE/KL consistency | Self-dist. | Logit-space targets |
| <b>DBTM</b>: Discrete Beckmann Transport Models for One-Step Language Modeling and Reasoning | <a href="https://arxiv.org/abs/2609.15903">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.15903">alphaXiv</a> · <a href="https://github.com/sophtang/DBTM"><img src="https://img.shields.io/github/stars/sophtang/DBTM?style=social&label=Code" alt="Code"></a> | arXiv 2026 | One-hot | Endpoint map | Transport + CE | Direct | No time input |
| <b>CANDI</b>: Hybrid Discrete-Continuous Diffusion Models | <a href="https://arxiv.org/abs/2510.22510">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2510.22510">alphaXiv</a> | ICML 2026 | One-hot + mask | Gaussian + masking | Weighted CE | – | Decoupled corruption |
| <b>CADD</b>: Continuously Augmented Discrete Diffusion Model for Categorical Generative Modeling | <a href="https://arxiv.org/abs/2510.01329">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2510.01329">alphaXiv</a> · <a href="https://github.com/apple-aiml-research/ml-cadd"><img src="https://img.shields.io/github/stars/apple-aiml-research/ml-cadd?style=social&label=Code" alt="Code"></a> | ICLR 2026 | Tokens + emb. | Gaussian + masking | Masked CE | – | Latent-guided unmasking |
| <b>CCDD</b>: Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner | <a href="https://arxiv.org/abs/2510.03206">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2510.03206">alphaXiv</a> · <a href="https://github.com/zhouc20/CCDD"><img src="https://img.shields.io/github/stars/zhouc20/CCDD?style=social&label=Code" alt="Code"></a> | ICML 2026 | Tokens + latent | Joint diffusion | Noise MSE + CE | – | Joint denoising |

## 🆕 Recently added

Papers added after the survey's literature cutoff (November 2, 2026) will appear here, newest first.

| Added | Paper | Links | Family |
|:--|:--|:--|:--|
|  | No papers yet. |  |  |

## 📚 More papers

These are the remaining 114 papers, grouped by model family and listed newest first. Click a family to open its table.

<details>
<summary><b>🌊 Vocabulary embeddings</b> (12 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑27 | <b>SERF</b>: Self-Regularized Flow Language Models | <a href="https://arxiv.org/abs/2610.37115">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.37115">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑24 | <b>ReLF</b>: Rectified Language Flow | <a href="https://arxiv.org/abs/2610.33811">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.33811">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑20 | <b>Lafa</b>: Large Flow Language Models | <a href="https://arxiv.org/abs/2610.28559">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.28559">alphaXiv</a> · <a href="https://github.com/lafa-gh/large-flow-lms"><img src="https://img.shields.io/github/stars/lafa-gh/large-flow-lms?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑15 | <b>LangDiT</b>: Designing Transformers for Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.22330">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.22330">alphaXiv</a> | arXiv 2026 |
| 2026‑08‑24 | <b>ConvergeFlow</b>: Language Flow with Provable Convergence to Token Embeddings | <a href="https://arxiv.org/abs/2608.23551">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2608.23551">alphaXiv</a> · <a href="https://github.com/Na-Li66/ConvergeFlow"><img src="https://img.shields.io/github/stars/Na-Li66/ConvergeFlow?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑05‑18 | <b>RePlaid</b>: Continuous Diffusion Scales Competitively with Discrete Diffusion for Language | <a href="https://arxiv.org/abs/2605.18530">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.18530">alphaXiv</a> | NeurIPS 2026 |
| 2026‑02‑20 | <b>InfoNoise</b>: Noise Scheduling as Information-Guided Allocation in Diffusion Training | <a href="https://arxiv.org/abs/2602.18647">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.18647">alphaXiv</a> | arXiv 2026 |
| 2025‑05‑24 | <b>Smoothie</b>: Smoothing Diffusion on Token Embeddings for Text Generation | <a href="https://arxiv.org/abs/2505.18853">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2505.18853">alphaXiv</a> · <a href="https://github.com/ashaba1in/smoothie"><img src="https://img.shields.io/github/stars/ashaba1in/smoothie?style=social&label=Code" alt="Code"></a> | ICML 2026 |
| 2024‑02‑19 | <b>TREC</b>: Text Diffusion with Reinforced Conditioning | <a href="https://arxiv.org/abs/2402.14843">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2402.14843">alphaXiv</a> | arXiv 2024 |
| 2022‑12‑22 | <b>GENIE</b>: Text Generation with Diffusion Language Models: A Pre-training Approach with Continuous Paragraph Denoise | <a href="https://arxiv.org/abs/2212.11685">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2212.11685">alphaXiv</a> · <a href="https://github.com/microsoft/ProphetNet/tree/master/GENIE"><img src="https://img.shields.io/github/stars/microsoft/ProphetNet?style=social&label=Code" alt="Code"></a> | ICML 2023 |
| 2022‑12‑20 | <b>SeqDiffuSeq</b>: Text Diffusion with Encoder-Decoder Transformers | <a href="https://arxiv.org/abs/2212.10325">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2212.10325">alphaXiv</a> · <a href="https://github.com/Yuanhy1997/SeqDiffuSeq"><img src="https://img.shields.io/github/stars/Yuanhy1997/SeqDiffuSeq?style=social&label=Code" alt="Code"></a> | arXiv 2022 |
| 2022‑12‑19 | <b>Difformer</b>: Empowering Diffusion Models on the Embedding Space for Text Generation | <a href="https://arxiv.org/abs/2212.09412">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2212.09412">alphaXiv</a> · <a href="https://github.com/zhjgao/difformer"><img src="https://img.shields.io/github/stars/zhjgao/difformer?style=social&label=Code" alt="Code"></a> | NAACL 2024 |

</details>

<details>
<summary><b>🌌 Contextual &amp; latent spaces</b> (21 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑22 | <b>Cola2</b>: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation | <a href="https://arxiv.org/abs/2610.31305">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.31305">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑09 | <b>PSF</b>: Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation | <a href="https://arxiv.org/abs/2610.12898">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.12898">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑07 | <b>BLD</b>: Denoising Blocks, Not Tokens: Efficient Compressed Continuous Diffusion with Branching Token Realization | <a href="https://arxiv.org/abs/2610.09311">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.09311">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑06 | <b>H-CoBit</b>: Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling | <a href="https://arxiv.org/abs/2610.08738">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.08738">alphaXiv</a> · <a href="https://github.com/matol-16/HCDLM"><img src="https://img.shields.io/github/stars/matol-16/HCDLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑01 | <b>Diffusibility</b>: Scaling and Distilling Text Embeddings for Better Diffusibility | <a href="https://arxiv.org/abs/2610.01016">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.01016">alphaXiv</a> · <a href="https://github.com/la0ka1/diffusing-scaled-text-embeddings"><img src="https://img.shields.io/github/stars/la0ka1/diffusing-scaled-text-embeddings?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑09‑27 | <b>JPEG-DLM</b>: One Latent, Many Tokens: Jointly Learning Compressed Embeddings for Efficient Language Diffusion | <a href="https://arxiv.org/abs/2609.33698">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.33698">alphaXiv</a> · <a href="https://github.com/infiniteYuanyl/JPEG-DLM"><img src="https://img.shields.io/github/stars/infiniteYuanyl/JPEG-DLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑09‑24 | <b>ELF-REG</b>: Scaling Continuous Diffusion Language Models to Reasoning Tasks | <a href="https://arxiv.org/abs/2609.29102">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.29102">alphaXiv</a> · <a href="https://github.com/lizeyu090312/scaling_dLM"><img src="https://img.shields.io/github/stars/lizeyu090312/scaling_dLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑08‑03 | <b>AURORA-LM</b>: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling | <a href="https://arxiv.org/abs/2608.02602">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2608.02602">alphaXiv</a> · <a href="https://github.com/fyv587/AURORA-LM"><img src="https://img.shields.io/github/stars/fyv587/AURORA-LM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑08‑02 | <b>DeltaFlow</b>: Noise-Adaptive Bidirectional Gated Delta Networks for Embedded Language Flows | <a href="https://arxiv.org/abs/2608.01240">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2608.01240">alphaXiv</a> | arXiv 2026 |
| 2026‑06‑07 | <b>Decoder Interface</b>: Continuous Language Diffusion as a Decoder-Interface Problem | <a href="https://arxiv.org/abs/2606.08810">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.08810">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑14 | <b>Manta-LM</b>: Language Generation as Optimal Control: Closed-Loop Diffusion in Latent Control Space | <a href="https://arxiv.org/abs/2605.14531">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.14531">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑08 | <b>TextLDM</b>: Language Modeling with Continuous Latent Diffusion | <a href="https://arxiv.org/abs/2605.07748">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.07748">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑07 | <b>Cola DLM</b>: Continuous Latent Diffusion Language Model | <a href="https://arxiv.org/abs/2605.06548">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.06548">alphaXiv</a> · <a href="https://github.com/ByteDance-Seed/Cola-DLM"><img src="https://img.shields.io/github/stars/ByteDance-Seed/Cola-DLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑05‑07 | <b>Representation Alignment</b>: Don't Retrain, Align: Adapting Autoregressive LMs to Diffusion LMs via Representation Alignment | <a href="https://arxiv.org/abs/2605.06885">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.06885">alphaXiv</a> · <a href="https://github.com/pengzhangzhi/Open-dLLM"><img src="https://img.shields.io/github/stars/pengzhangzhi/Open-dLLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑03‑03 | <b>CoDAR</b>: Continuous Diffusion Language Models are More Powerful Than You Think | <a href="https://arxiv.org/abs/2603.02547">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2603.02547">alphaXiv</a> | EMNLP 2026 |
| 2025‑06‑26 | <b>Cosmos</b>: Compressed and Smooth Latent Space for Text Diffusion Modeling | <a href="https://arxiv.org/abs/2506.21170">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2506.21170">alphaXiv</a> · <a href="https://github.com/MeshchaninovViacheslav/cosmos"><img src="https://img.shields.io/github/stars/MeshchaninovViacheslav/cosmos?style=social&label=Code" alt="Code"></a> | NeurIPS 2025 |
| 2024‑12‑15 | <b>SLD</b>: Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models | <a href="https://arxiv.org/abs/2412.11333">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2412.11333">alphaXiv</a> · <a href="https://github.com/SpaceHunterInf/Segment_Level_Diffusion"><img src="https://img.shields.io/github/stars/SpaceHunterInf/Segment_Level_Diffusion?style=social&label=Code" alt="Code"></a> | ACL 2025 |
| 2024‑12‑11 | <b>LCM</b>: Large Concept Models: Language Modeling in a Sentence Representation Space | <a href="https://arxiv.org/abs/2412.08821">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2412.08821">alphaXiv</a> · <a href="https://github.com/facebookresearch/large_concept_model"><img src="https://img.shields.io/github/stars/facebookresearch/large_concept_model?style=social&label=Code" alt="Code"></a> | arXiv 2024 |
| 2024‑08‑08 | <b>DGLM</b>: Diffusion Guided Language Modeling | <a href="https://arxiv.org/abs/2408.04220">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2408.04220">alphaXiv</a> · <a href="https://github.com/justinlovelace/Diffusion-Guided-LM"><img src="https://img.shields.io/github/stars/justinlovelace/Diffusion-Guided-LM?style=social&label=Code" alt="Code"></a> | Findings of ACL 2024 |
| 2024‑02‑29 | <b>TEncDM</b>: Understanding the Properties of the Diffusion Model in the Space of Language Model Encodings | <a href="https://arxiv.org/abs/2402.19097">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2402.19097">alphaXiv</a> · <a href="https://github.com/M0RJIQUE/tencdm"><img src="https://img.shields.io/github/stars/M0RJIQUE/tencdm?style=social&label=Code" alt="Code"></a> | AAAI 2025 |
| 2023‑06‑05 | <b>PLANNER</b>: Generating Diversified Paragraph via Latent Language Diffusion Model | <a href="https://arxiv.org/abs/2306.02531">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2306.02531">alphaXiv</a> · <a href="https://github.com/apple-aiml-research/ml-planner"><img src="https://img.shields.io/github/stars/apple-aiml-research/ml-planner?style=social&label=Code" alt="Code"></a> | NeurIPS 2023 |

</details>

<details>
<summary><b>🔺 Simplex &amp; sphere</b> (9 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑26 | <b>SBD</b>: Spherical Brownian Diffusion for Language Modeling | <a href="https://arxiv.org/abs/2610.35101">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.35101">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑23 | <b>LLaCO</b>: Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling | <a href="https://arxiv.org/abs/2610.32604">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.32604">alphaXiv</a> · <a href="https://github.com/WhenGIX/LLaCO"><img src="https://img.shields.io/github/stars/WhenGIX/LLaCO?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑09‑28 | <b>SDM</b>: Simplex Diffusion Models | <a href="https://arxiv.org/abs/2609.35553">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.35553">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑07 | <b>Spherical Flows</b> for Sampling Categorical Data | <a href="https://arxiv.org/abs/2605.05629">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.05629">alphaXiv</a> · <a href="https://github.com/JChemseddine/SFCD"><img src="https://img.shields.io/github/stars/JChemseddine/SFCD?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2025‑02‑19 | <b>TESS 2</b>: A Large-Scale Generalist Diffusion Language Model | <a href="https://arxiv.org/abs/2502.13917">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2502.13917">alphaXiv</a> · <a href="https://github.com/hamishivi/tess-2"><img src="https://img.shields.io/github/stars/hamishivi/tess-2?style=social&label=Code" alt="Code"></a> | ACL 2025 |
| 2025‑02‑17 | <b>RDLM</b>: Continuous Diffusion Model for Language Modeling | <a href="https://arxiv.org/abs/2502.11564">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2502.11564">alphaXiv</a> · <a href="https://github.com/harryjo97/RDLM"><img src="https://img.shields.io/github/stars/harryjo97/RDLM?style=social&label=Code" alt="Code"></a> | NeurIPS 2025 |
| 2023‑08‑14 | <b>BFN</b>: Bayesian Flow Networks | <a href="https://arxiv.org/abs/2308.07037">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2308.07037">alphaXiv</a> · <a href="https://github.com/nnaisense/bayesian-flow-networks"><img src="https://img.shields.io/github/stars/nnaisense/bayesian-flow-networks?style=social&label=Code" alt="Code"></a> | arXiv 2023 |
| 2023‑05‑24 | <b>SSD-2</b>: David helps Goliath: Inference-Time Collaboration Between Small Specialized and Large General Diffusion LMs | <a href="https://arxiv.org/abs/2305.14771">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.14771">alphaXiv</a> | NAACL 2024 |
| 2023‑05‑18 | <b>DDSM</b>: Dirichlet Diffusion Score Model for Biological Sequence Generation | <a href="https://arxiv.org/abs/2305.10699">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.10699">alphaXiv</a> · <a href="https://github.com/jzhoulab/ddsm"><img src="https://img.shields.io/github/stars/jzhoulab/ddsm?style=social&label=Code" alt="Code"></a> | ICML 2023 |

</details>

<details>
<summary><b>💧 One-hot, binary &amp; flow maps</b> (11 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑30 | <b>aFLM / aFMLM</b>: Asynchronous Flow Map Language Models | <a href="https://arxiv.org/abs/2610.42018">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.42018">alphaXiv</a> · <a href="https://github.com/david3684/async-fmlm"><img src="https://img.shields.io/github/stars/david3684/async-fmlm?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑20 | <b>BCT</b>: Bayes-Consistent Tempering for Flow Language Models | <a href="https://arxiv.org/abs/2610.27641">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.27641">alphaXiv</a> · <a href="https://github.com/daioba/bct"><img src="https://img.shields.io/github/stars/daioba/bct?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑07‑23 | <b>EFlows / EFM</b>: Expanding Flow Maps | <a href="https://arxiv.org/abs/2607.21585">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2607.21585">alphaXiv</a> | arXiv 2026 |
| 2026‑07‑01 | <b>FMLM\*</b>: Self-conditioned Flow Map Language Models via Fixed-point Flows | <a href="https://arxiv.org/abs/2607.00714">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2607.00714">alphaXiv</a> · <a href="https://github.com/Ugness/self-conditioned-fmlm"><img src="https://img.shields.io/github/stars/Ugness/self-conditioned-fmlm?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑06‑26 | <b>MLFM</b>: Masked Language Flow Models | <a href="https://arxiv.org/abs/2606.27617">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.27617">alphaXiv</a> · <a href="https://github.com/imbirik/mlfm"><img src="https://img.shields.io/github/stars/imbirik/mlfm?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑06‑23 | <b>FMLM+</b>: Posterior Refinement: Fast Language Generation via Any-Order Flow Maps | <a href="https://arxiv.org/abs/2606.24773">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.24773">alphaXiv</a> · <a href="https://github.com/MananAg007/posterior-refinement"><img src="https://img.shields.io/github/stars/MananAg007/posterior-refinement?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑05‑12 | <b>BitLM</b>: Unlocking Multi-Token Language Generation with Bitwise Continuous Diffusion | <a href="https://arxiv.org/abs/2605.11577">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.11577">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑08 | <b>Scaling CFM</b>: Scaling Categorical Flow Maps | <a href="https://arxiv.org/abs/2605.07820">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.07820">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑07 | <b>CoBit</b>: Language Modeling with Bitstream Diffusion | <a href="https://arxiv.org/abs/2605.07013">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.07013">alphaXiv</a> · <a href="https://github.com/GBATZOLIS/BitstreamDiffusion"><img src="https://img.shields.io/github/stars/GBATZOLIS/BitstreamDiffusion?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2024‑06‑07 | <b>CatFlow</b>: Variational Flow Matching for Graph Generation | <a href="https://arxiv.org/abs/2406.04843">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2406.04843">alphaXiv</a> | NeurIPS 2024 |
| 2022‑08‑08 | <b>Analog Bits</b>: Generating Discrete Data using Diffusion Models with Self-Conditioning | <a href="https://arxiv.org/abs/2208.04202">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2208.04202">alphaXiv</a> · <a href="https://github.com/google-research/pix2seq"><img src="https://img.shields.io/github/stars/google-research/pix2seq?style=social&label=Code" alt="Code"></a> | ICLR 2023 |

</details>

<details>
<summary><b>⚡ Few-step &amp; one-step</b> (20 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑19 | <b>PLM</b>: Parallel Language Models via Variational Decoding | <a href="https://arxiv.org/abs/2610.26693">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.26693">alphaXiv</a> · <a href="https://github.com/mandt-lab/plm"><img src="https://img.shields.io/github/stars/mandt-lab/plm?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑09 | <b>Seq-Drifting</b>: One-Step Text Generation by Seq-Drifting | <a href="https://arxiv.org/abs/2610.12879">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.12879">alphaXiv</a> · <a href="https://github.com/jyliu-ai/Seq-Drifting"><img src="https://img.shields.io/github/stars/jyliu-ai/Seq-Drifting?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑05 | <b>Rep-MMD</b>: Representation-Space MMD for Diffusion Language Models | <a href="https://arxiv.org/abs/2610.06648">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.06648">alphaXiv</a> · <a href="https://github.com/yandex-research/dlm-mmd"><img src="https://img.shields.io/github/stars/yandex-research/dlm-mmd?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑03 | <b>R-WGF</b>: One-Step Generation via Riemannian Wasserstein Gradient Flows | <a href="https://arxiv.org/abs/2610.04454">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.04454">alphaXiv</a> | arXiv 2026 |
| 2026‑09‑30 | <b>GSF</b>: Gumbel Straight Flow: Distilling Autoregressive Models into One-step Flow Maps | <a href="https://arxiv.org/abs/2610.00497">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.00497">alphaXiv</a> | arXiv 2026 |
| 2026‑09‑30 | <b>S/R-DMD</b>: Distribution Matching Distillation for Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2609.40235">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.40235">alphaXiv</a> | arXiv 2026 |
| 2026‑08‑03 | <b>BTM</b>: Beckmann Transport Models: From Autonomous Flows to One-Step Maps | <a href="https://arxiv.org/abs/2608.01692">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2608.01692">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑08 | <b>Coupling Models</b> for One-Step Discrete Generation | <a href="https://arxiv.org/abs/2605.07193">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.07193">alphaXiv</a> · <a href="https://github.com/pengzhangzhi/Coupling-Models"><img src="https://img.shields.io/github/stars/pengzhangzhi/Coupling-Models?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑04‑07 | <b>FastDiSS</b>: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation--Full Version | <a href="https://arxiv.org/abs/2604.05551">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.05551">alphaXiv</a> | Findings of ACL 2026 |
| 2026‑04‑06 | <b>FlowLM</b>: Few-Step Language Modeling via Diffusion-to-Flow Adaptation | <a href="https://arxiv.org/abs/2605.20199">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.20199">alphaXiv</a> | arXiv 2026 |
| 2026‑03‑23 | <b>Gumbel Distillation</b> for Parallel Text Generation | <a href="https://arxiv.org/abs/2603.22216">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2603.22216">alphaXiv</a> · <a href="https://github.com/hxixixh/gumbel-distill"><img src="https://img.shields.io/github/stars/hxixixh/gumbel-distill?style=social&label=Code" alt="Code"></a> | ICLR 2026 |
| 2026 | <b>Shortcut FM</b>: One-step Nonautoregressive Natural Language Generation with Shortcut Flow Matching Models | <a href="https://aclanthology.org/2026.acl-short.53/">ACL Anthology</a> | ACL 2026 |
| 2026 | <b>Categorical Drifting</b> Models | <a href="https://icml.cc/virtual/2026/74221">ICML</a> | ICML Workshop 2026 |
| 2026 | <b>CoFlow</b>: Latent Space Co-training for Few-Step Text Generation | <a href="https://scholar.google.com/scholar?q=Latent+Space+Co-training+for+Few-Step+Text+Generation">Google Scholar</a> | NeurIPS Workshop 2026 |
| 2025‑12‑24 | <b>PTP</b>: Parallel Token Prediction for Language Models | <a href="https://arxiv.org/abs/2512.21323">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2512.21323">alphaXiv</a> · <a href="https://github.com/mandt-lab/ptp"><img src="https://img.shields.io/github/stars/mandt-lab/ptp?style=social&label=Code" alt="Code"></a> | ICLR 2026 |
| 2025‑10‑31 | <b>CALM</b>: Continuous Autoregressive Language Models | <a href="https://arxiv.org/abs/2510.27688">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2510.27688">alphaXiv</a> · <a href="https://github.com/shaochenze/calm"><img src="https://img.shields.io/github/stars/shaochenze/calm?style=social&label=Code" alt="Code"></a> | arXiv 2025 |
| 2025‑05‑30 | <b>DLM-One</b>: Diffusion Language Models for One-Step Sequence Generation | <a href="https://arxiv.org/abs/2506.00290">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2506.00290">alphaXiv</a> | arXiv 2025 |
| 2024‑03‑25 | <b>LF</b>: Language Rectified Flow: Advancing Diffusion Language Generation with Probabilistic Flows | <a href="https://arxiv.org/abs/2403.16995">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2403.16995">alphaXiv</a> | NAACL 2024 |
| 2024 | <b>FlowSeq</b>: Flow Matching for Conditional Text Generation in a Few Sampling Steps | <a href="https://aclanthology.org/2024.eacl-short.33/">ACL Anthology</a> · <a href="https://github.com/dongzhuoyao/flowseq"><img src="https://img.shields.io/github/stars/dongzhuoyao/flowseq?style=social&label=Code" alt="Code"></a> | EACL 2024 |
| 2024 | <b>FMSeq</b>: Enable Fast Sampling for Seq2Seq Text Diffusion | <a href="https://aclanthology.org/2024.findings-emnlp.497/">ACL Anthology</a> | Findings of EMNLP 2024 |

</details>

<details>
<summary><b>🔀 Hybrid &amp; scheduled</b> (13 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑01 | <b>Clock Diffusion</b>: Efficient Semi-Autoregressive Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.00894">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.00894">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑01 | <b>HC-DLM</b>: Hierarchical Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.02193">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.02193">alphaXiv</a> · <a href="https://github.com/rhfeiyang/HC-DLM"><img src="https://img.shields.io/github/stars/rhfeiyang/HC-DLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑07‑12 | <b>Sticky Jump Diffusions</b>: A Unifying View of Masked, Continuous, and Hybrid Diffusion | <a href="https://arxiv.org/abs/2607.10951">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2607.10951">alphaXiv</a> · <a href="https://github.com/PascalJD/sticky-jump-diffusions"><img src="https://img.shields.io/github/stars/PascalJD/sticky-jump-diffusions?style=social&label=Code" alt="Code"></a> | NeurIPS 2026 |
| 2026‑06‑27 | <b>$x$-Prediction Flow</b>: Efficient Continuous Decoding for Masked Diffusion Language Models | <a href="https://arxiv.org/abs/2606.29066">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.29066">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑31 | <b>DSL-LLaDA</b>: Scaling Continuous Denoising to 8B Masked Diffusion LMs | <a href="https://arxiv.org/abs/2606.01024">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.01024">alphaXiv</a> | Findings of EMNLP 2026 |
| 2026‑05‑22 | <b>DiLaDiff</b>: Distilled Latent-Augmented Diffusion for Language Modeling | <a href="https://arxiv.org/abs/2605.23605">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.23605">alphaXiv</a> | arXiv 2026 |
| 2026‑05‑07 | <b>TTCD</b>: Token Time Continuous Diffusion for Language Modeling | <a href="https://arxiv.org/abs/2607.14106">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2607.14106">alphaXiv</a> | arXiv 2026 |
| 2026‑03‑21 | <b>Random CSPs</b>: Generating from Discrete Distributions Using Diffusions: Insights from Random Constraint Satisfaction Problems | <a href="https://arxiv.org/abs/2603.20589">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2603.20589">alphaXiv</a> | arXiv 2026 |
| 2026‑03‑02 | <b>CRoCoDiL</b>: Continuous and Robust Conditioned Diffusion for Language | <a href="https://arxiv.org/abs/2603.20210">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2603.20210">alphaXiv</a> | arXiv 2026 |
| 2025‑06‑12 | <b>Duo</b>: The Diffusion Duality | <a href="https://arxiv.org/abs/2506.10892">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2506.10892">alphaXiv</a> · <a href="https://github.com/s-sahoo/duo"><img src="https://img.shields.io/github/stars/s-sahoo/duo?style=social&label=Code" alt="Code"></a> | ICML 2025 |
| 2025‑05‑28 | <b>NeoDiff</b>: Unifying Continuous and Discrete Text Diffusion with Non-simultaneous Diffusion Processes | <a href="https://arxiv.org/abs/2505.22165">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2505.22165">alphaXiv</a> | ACL 2025 |
| 2023‑10‑09 | <b>DiffuSeq-v2</b>: Bridging Discrete and Continuous Text Spaces for Accelerated Seq2Seq Diffusion Models | <a href="https://arxiv.org/abs/2310.05793">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2310.05793">alphaXiv</a> · <a href="https://github.com/Shark-NLP/DiffuSeq"><img src="https://img.shields.io/github/stars/Shark-NLP/DiffuSeq?style=social&label=Code" alt="Code"></a> | Findings of EMNLP 2023 |
| 2023‑05‑16 | <b>AR-Diffusion</b>: Auto-Regressive Diffusion Model for Text Generation | <a href="https://arxiv.org/abs/2305.09515">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.09515">alphaXiv</a> · <a href="https://github.com/microsoft/ProphetNet"><img src="https://img.shields.io/github/stars/microsoft/ProphetNet?style=social&label=Code" alt="Code"></a> | NeurIPS 2023 |

</details>

<details>
<summary><b>🧭 Guidance &amp; inference</b> (14 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑30 | <b>RangeSWA</b>: Training-Free Length Extrapolation for Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.42084">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.42084">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑21 | <b>GRAFT</b>: Restoring the Missing Sampling Interface in Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.29136">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.29136">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑17 | <b>FlashMap</b>: Flow Map Speculative Decoding | <a href="https://arxiv.org/abs/2610.24365">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.24365">alphaXiv</a> · <a href="https://github.com/al-jshen/flashmap"><img src="https://img.shields.io/github/stars/al-jshen/flashmap?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑13 | <b>Verifier Backprop</b>: Backpropagating Verifier Rewards Through Continuous Flow Language Models | <a href="https://arxiv.org/abs/2610.19080">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.19080">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑09 | <b>DoubleCat / SemiCat</b>: On the Design Space of Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2610.13834">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.13834">alphaXiv</a> | arXiv 2026 |
| 2026‑09‑16 | <b>Probe Guidance</b>: How to Guide Your Language Flow | <a href="https://arxiv.org/abs/2609.19356">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.19356">alphaXiv</a> | arXiv 2026 |
| 2026‑08‑23 | <b>Untied Self-Cond.</b>: Improving Few-Step Language Flows with Untied Self-Conditioning | <a href="https://arxiv.org/abs/2608.22244">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2608.22244">alphaXiv</a> | arXiv 2026 |
| 2026‑07‑01 | <b>ACE</b>: A Dominant Self-Conditioning Direction Drives Repetition in Unconditional Continuous Diffusion Language Models | <a href="https://arxiv.org/abs/2607.00588">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2607.00588">alphaXiv</a> · <a href="https://github.com/ZhangShuai1230/ACE-DLM"><img src="https://img.shields.io/github/stars/ZhangShuai1230/ACE-DLM?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑04‑29 | <b>FMRG</b>: How to Guide Your Flow: Few-Step Alignment via Flow Map Reward Guidance | <a href="https://arxiv.org/abs/2604.27147">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.27147">alphaXiv</a> · <a href="https://github.com/jrrhuang/fmrg"><img src="https://img.shields.io/github/stars/jrrhuang/fmrg?style=social&label=Code" alt="Code"></a> | ICML 2026 |
| 2026‑04‑02 | <b>Why Gaussian Fails</b>: Why Gaussian Diffusion Models Fail on Discrete Data and How to Prevent It? | <a href="https://arxiv.org/abs/2604.02028">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.02028">alphaXiv</a> | arXiv 2026 |
| 2026‑02‑12 | <b>Diffinity</b>: Continuous Diffusion Models Can Obey Formal Syntax | <a href="https://arxiv.org/abs/2602.12468">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.12468">alphaXiv</a> · <a href="https://github.com/large-loris-models/Diffinity"><img src="https://img.shields.io/github/stars/large-loris-models/Diffinity?style=social&label=Code" alt="Code"></a> | ICML 2026 |
| 2026 | <b>INCO</b>: Inverse-Confidence Sampling for Continuous Diffusion Language Models | <a href="https://icml.cc/virtual/2026/74210">ICML</a> | ICML Workshop 2026 |
| 2023‑05‑18 | <b>Stopping Criteria</b>: Diffusion Language Models Generation Can Be Halted Early | <a href="https://arxiv.org/abs/2305.10818">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2305.10818">alphaXiv</a> | arXiv 2023 |
| 2023‑02‑20 | <b>DINOISER</b>: Diffused Conditional Sequence Learning by Manipulating Noises | <a href="https://arxiv.org/abs/2302.10025">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2302.10025">alphaXiv</a> · <a href="https://github.com/yegcjs/DINOISER"><img src="https://img.shields.io/github/stars/yegcjs/DINOISER?style=social&label=Code" alt="Code"></a> | arXiv 2023 |

</details>

<details>
<summary><b>🧠 Reasoning, multimodal &amp; evaluation</b> (14 papers)</summary>
<br>

| Date | Paper | Links | Venue |
|:--|:--|:--|:--|
| 2026‑10‑20 | <b>JUICE</b>: Unified Multimodal Modeling in Pretrained Representation Spaces | <a href="https://arxiv.org/abs/2610.28801">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.28801">alphaXiv</a> · <a href="https://github.com/Ced3-han/JUICE-Code"><img src="https://img.shields.io/github/stars/Ced3-han/JUICE-Code?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑09 | <b>Multimodal CoBit</b>: Multimodal Co-Generation With Continuous Bitstream Diffusion | <a href="https://arxiv.org/abs/2610.14349">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.14349">alphaXiv</a> · <a href="https://github.com/GBATZOLIS/BitstreamDiffusion"><img src="https://img.shields.io/github/stars/GBATZOLIS/BitstreamDiffusion?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑10‑07 | <b>Efficient FLM Reasoning</b>: Efficient Reasoning with Flow Language Models | <a href="https://arxiv.org/abs/2610.09416">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.09416">alphaXiv</a> | arXiv 2026 |
| 2026‑10‑05 | <b>SOL</b>: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics | <a href="https://arxiv.org/abs/2610.06513">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2610.06513">alphaXiv</a> · <a href="https://github.com/GregorKornhardt/SOL"><img src="https://img.shields.io/github/stars/GregorKornhardt/SOL?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑09‑30 | <b>MF-1</b>: Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces | <a href="https://arxiv.org/abs/2609.40362">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.40362">alphaXiv</a> · <a href="https://github.com/hustvl/Multimodal-Flow"><img src="https://img.shields.io/github/stars/hustvl/Multimodal-Flow?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑09‑10 | <b>Looped Flows</b>: Thinking with Looped Flows | <a href="https://arxiv.org/abs/2609.11801">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2609.11801">alphaXiv</a> · <a href="https://github.com/MisakiTaro0414/looped-flows"><img src="https://img.shields.io/github/stars/MisakiTaro0414/looped-flows?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑06‑28 | <b>FRM</b>: Flow Reasoning Models: Turning Flows Into Efficient Recurrent Reasoners | <a href="https://arxiv.org/abs/2606.29150">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.29150">alphaXiv</a> · <a href="https://github.com/helblazer811/Flow-Reasoning-Models"><img src="https://img.shields.io/github/stars/helblazer811/Flow-Reasoning-Models?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑06‑07 | <b>Hacking Generative Perplexity</b>: Why Unconditional Text Evaluation Needs New Metrics | <a href="https://arxiv.org/abs/2606.08417">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2606.08417">alphaXiv</a> · <a href="https://github.com/antoniofrancaib/dlmbench"><img src="https://img.shields.io/github/stars/antoniofrancaib/dlmbench?style=social&label=Code" alt="Code"></a> | arXiv 2026 |
| 2026‑05‑19 | <b>GRAM</b>: Generative Recursive Reasoning | <a href="https://arxiv.org/abs/2605.19376">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2605.19376">alphaXiv</a> | arXiv 2026 |
| 2026‑04‑03 | <b>Generative Frontiers</b>: Why Evaluation Matters for Diffusion Language Models | <a href="https://arxiv.org/abs/2604.02718">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2604.02718">alphaXiv</a> | arXiv 2026 |
| 2026‑02‑02 | <b>CHASE</b>: Repurposing Protein Language Models for Latent Flow-Based Fitness Optimization | <a href="https://arxiv.org/abs/2602.02425">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2602.02425">alphaXiv</a> | arXiv 2026 |
| 2025‑04‑15 | <b>ProtFlow</b>: Fast Protein Sequence Design via Flow Matching on Compressed Protein Language Model Embeddings | <a href="https://arxiv.org/abs/2504.10983">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2504.10983">alphaXiv</a> | arXiv 2025 |
| 2024‑03‑06 | <b>DiMA</b>: Diffusion on Language Model Encodings for Protein Sequence Generation | <a href="https://arxiv.org/abs/2403.03726">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2403.03726">alphaXiv</a> · <a href="https://github.com/MeshchaninovViacheslav/DiMA"><img src="https://img.shields.io/github/stars/MeshchaninovViacheslav/DiMA?style=social&label=Code" alt="Code"></a> | ICML 2025 |
| 2021‑02‑02 | <b>MAUVE</b>: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers | <a href="https://arxiv.org/abs/2102.01454">arXiv</a> · <a href="https://www.alphaxiv.org/abs/2102.01454">alphaXiv</a> · <a href="https://github.com/krishnap25/mauve"><img src="https://img.shields.io/github/stars/krishnap25/mauve?style=social&label=Code" alt="Code"></a> | NeurIPS 2021 |

</details>

## Contributing

We welcome new papers, corrections, and questions about scope. To suggest a change, [open an issue](https://github.com/sophtang/Awesome-Continuous-Language-Models/issues).

## BibTeX

If you find this collection useful, please cite our survey.

```bibtex
@article{tang2026survey,
  author = {Tang, Sophia and Lee, Chanhyuk and Eijkelboom, Floor and Kim, Jinwoo},
  title = {A Survey on Continuous Diffusion and Flow Language Models},
  url = {https://www.alphaxiv.org/abs/2611.continuous-diffusion-flow-language-models},
  publisher = {alphaXiv},
  year = {2026}
}
```

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=sophtang%2FAwesome-Continuous-Language-Models&type=date&theme=dark">
  <img alt="Star history of sophtang/Awesome-Continuous-Language-Models" src="https://api.star-history.com/svg?repos=sophtang%2FAwesome-Continuous-Language-Models&type=date">
</picture>