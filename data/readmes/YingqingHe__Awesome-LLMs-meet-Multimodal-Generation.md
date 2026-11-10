
<div align="center">
<h2> LLMs Meet Multimodal Generation and Editing: A Survey </h2> 
<a href='https://arxiv.org/abs/2405.19334'><img src='https://img.shields.io/badge/ArXiv-2405.19334-red'></a>
</div>

# 🤗 Introduction
- This repository contains a curated list of **LLMs meet multimodal generation**. Modalities consist of visual (including image, video and 3D) and audio (including sound, speech and music). 
  <p align="center">
  <img src="assets/fig.jpg" width=300"">
</p>

- We welcome any contributions and suggestions to our repository or the addition of your own work. Feel free to make a pull request or leave your comments!!


# 📋 Contents
- [🤗 Introduction](#-introduction)
- [📋 Contents](#-contents)
- [💘 Tips](#-tips)
- [📍 Multimodal Generation](#-multimodal-generation)
  - [Image Generation](#image-generation)
    - [🔅 LLM-based](#-llm-based)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5)
    - [Datasets](#datasets)
  - [Video Generation](#video-generation)
    - [🔅 LLM-based](#-llm-based-1)
    - [Non-LLM-based](#non-llm-based)
    - [Video VAE/Tokenizers](#video-vaetokenizers)
    - [Audio-Video](#audio-video)
    - [Benchmarks](#benchmarks)
    - [Datasets](#datasets-1)
  - [3D Generation](#3d-generation)
    - [🔅 LLM-based](#-llm-based-2)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5-1)
    - [Datasets](#datasets-2)
  - [Audio Generation](#audio-generation)
    - [🔅 LLM-based](#-llm-based-3)
    - [Non-LLM-based](#non-llm-based-1)
    - [Datasets](#datasets-3)
  - [Generation with Multiple Modalities](#generation-with-multiple-modalities)
    - [🔅 LLM-based](#-llm-based-4)
    - [Non-LLM-based](#non-llm-based-2)
- [📍 Multimodal Editing](#-multimodal-editing)
  - [Image Editing](#image-editing)
    - [🔅 LLM-based](#-llm-based-5)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5-2)
  - [Video Editing](#video-editing)
    - [🔅 LLM-based](#-llm-based-6)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5-3)
  - [3D Editing](#3d-editing)
    - [🔅 LLM-based](#-llm-based-7)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5-4)
  - [Audio Editing](#audio-editing)
    - [🔅 LLM-based](#-llm-based-8)
    - [Non-LLM-based (Clip/T5)](#non-llm-based-clipt5-5)
- [📍 Multimodal Agents](#-multimodal-agents)
- [📍 Multimodal Understanding with LLMs](#-multimodal-understanding-with-llms)
  - [Multiple modalities](#multiple-modalities)
  - [Image Understanding](#image-understanding)
  - [Video Understanding](#video-understanding)
  - [3D Understanding](#3d-understanding)
  - [Audio Understanding](#audio-understanding)
- [📍 Multimodal LLM Safety](#-multimodal-llm-safety)
  - [Attack](#attack)
  - [Defense and Detect](#defense-and-detect)
  - [Alignment](#alignment)
  - [Datasets](#datasets-4)
  - [3D, Video and Audio Safety](#3d-video-and-audio-safety)
- [📍 Related Surveys](#-related-surveys)
  - [LLM](#llm)
  - [Vision](#vision)
- [👨‍💻 Team](#-team)
- [😉 Citation](#-citation)
- [⭐️ Star History](#️-star-history)



# 💘 Tips
- **✅ Paper searching via catatogue**: directly clicking the content of the catatogue to select the area of your research and browse related papers.
- **✅ Paper searching via author name**: Free feel to search papers of a specific author via `ctrl + F` and then type the author name. The dropdown list of authors will automatically expand when searching.
- **✅ Paper searching via tag**: You can also search the related papers via the following tags: `customization`, `iteractive`, `human motion generation` `tokenizer`. (More tags are ongoing)


# 📍 Multimodal Generation

## Image Generation

### 🔅 LLM-based


+ **I Think, Therefore I Diffuse: Enabling Multimodal In-Context Reasoning in Diffusion Models** (12 Feb 2025)<details><summary>Zhenxing Mi, Kuan-Chieh Wang, Guocheng Qian, et al.</summary>Zhenxing Mi, Kuan-Chieh Wang, Guocheng Qian, Hanrong Ye, Runtao Liu, Sergey Tulyakov, Kfir Aberman, Dan Xu</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.10458)
[![Code](https://img.shields.io/github/stars/MiZhenxing/ThinkDiff.svg?style=social&label=Star)](https://github.com/MiZhenxing/ThinkDiff?tab=readme-ov-file)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://mizhenxing.github.io/ThinkDiff/)

+ **MetaMorph: Multimodal Understanding and Generation via Instruction Tuning** (18 Dec 2024)<details><summary>Shengbang Tong, David Fan, Jiachen Zhu, et al.</summary>Shengbang Tong, David Fan, Jiachen Zhu, Yunyang Xiong, Xinlei Chen, Koustuv Sinha, Michael Rabbat, Yann LeCun, Saining Xie, Zhuang Liu</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.14164v1)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://tsb0601.github.io/metamorph/)

+ **X-Prompt: Towards Universal In-Context Image Generation in Auto-Regressive Vision Language Foundation Models** (2 Dec 2024)<details><summary>Zeyi Sun, Ziyang Chu, Pan Zhang, et al.</summary>Zeyi Sun, Ziyang Chu, Pan Zhang, Tong Wu, Xiaoyi Dong, Yuhang Zang, Yuanjun Xiong, Dahua Lin, Jiaqi Wang</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.01824)
[![Code](https://img.shields.io/github/stars/SunzeY/X-Prompt.svg?style=social&label=Star)](https://github.com/SunzeY/X-Prompt)


+ **Cosmos Tokenizer: A suite of image and video neural tokenizers** (06 Nov 2024)<details><summary>Fitsum Reda, Jinwei Gu, Xian Liu et al.</summary>Fitsum Reda, Jinwei Gu, Xian Liu, Songwei Ge, Ting-Chun Wang, Haoxiang Wang, Ming-Yu Liu</details></details>
[![Code](https://img.shields.io/github/stars/NVIDIA/Cosmos-Tokenizer.svg?style=social&label=Star)](https://github.com/NVIDIA/Cosmos-Tokenizer?tab=readme-ov-file)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://research.nvidia.com/labs/dir/cosmos-tokenizer/)`tokenizer`



+ **[ICLR 2025 Spotlight] Rare-to-Frequent: Unlocking Compositional Generation Power of Diffusion Models on Rare Concepts with LLM Guidance** (29 Oct 2024)<details><summary>Dongmin Park, Sebin Kim, Taehong Moon et al.</summary>Dongmin Park, Sebin Kim, Taehong Moon, Minkyu Kim, Kangwook Lee, Jaewoong Cho</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.22376)
[![Code](https://img.shields.io/github/stars/LargeWorldModel/ElasticTok.svg?style=social&label=Star)](https://github.com/krafton-ai/Rare-to-Frequent)


+ **ElasticTok: Adaptive Tokenization for Image and Video** (10 Oct 2024)<details><summary>Wilson Yan, Matei Zaharia, Volodymyr Mnih et al.</summary>Wilson Yan, Matei Zaharia, Volodymyr Mnih, Pieter Abbeel, Aleksandra Faust, Hao Liu</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.08368)
[![Code](https://img.shields.io/github/stars/LargeWorldModel/ElasticTok.svg?style=social&label=Star)](https://github.com/LargeWorldModel/ElasticTok)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://largeworldmodel.github.io/elastictok/)`tokenizer`

+ **DART: Denoising Autoregressive Transformer for Scalable Text-to-Image Generation** (10 Oct 2024)<details><summary>Jiatao Gu, Yuyang Wang, Yizhe Zhang et al.</summary>Jiatao Gu, Yuyang Wang, Yizhe Zhang, Qihang Zhang, Dinghuai Zhang, Navdeep Jaitly, Josh Susskind, Shuangfei Zhai</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.08159)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=61bfd967a6ba21e50276e52f353fa74dd68990a6)](https://www.semanticscholar.org/paper/DART%3A-Denoising-Autoregressive-Transformer-for-Gu-Wang/61bfd967a6ba21e50276e52f353fa74dd68990a6)



+ **VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation** (6 Sep 2024)<details><summary>Yecheng Wu, Zhuoyang Zhang, Junyu Chen et al.</summary>Yecheng Wu, Zhuoyang Zhang, Junyu Chen, Haotian Tang, Dacheng Li, Yunhao Fang, Ligeng Zhu, Enze Xie, Hongxu Yin, Li Yi, Song Han, Yao Lu</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.04429)
[![Code](https://img.shields.io/github/stars/mit-han-lab/vila-u.svg?style=social&label=Star)](https://github.com/mit-han-lab/vila-u)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://hanlab.mit.edu/projects/vila-u)


+ **OmniTokenizer: A Joint Image-Video Tokenizer for Visual Generation** (13 Jun 2024)<details><summary>Junke Wang, Yi Jiang, Zehuan Yuan et al.</summary>Junke Wang, Yi Jiang, Zehuan Yuan, Binyue Peng, Zuxuan Wu, Yu-Gang Jiang</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.09399)
[![citation](https://img.shields.io/badge/citation-5-blue.svg?paper=8613c1081a6ab34e2f980e35c06a1af461d7314e)](https://www.semanticscholar.org/paper/OmniTokenizer%3A-A-Joint-Image-Video-Tokenizer-for-Wang-Jiang/8613c1081a6ab34e2f980e35c06a1af461d7314e)
[![Code](https://img.shields.io/github/stars/FoundationVision/LlamaGen.svg?style=social&label=Star)](https://github.com/FoundationVision/OmniTokenizer)
`tokenizer`

+ **InstantUnify: Integrates Multimodal LLM into Diffusion Models** (Aug 2024)<details><summary>Qixun Wang, Xu Bai, Rui Wang et al.</summary>Qixun Wang, Xu Bai, Rui Wang, Haofan Wang</details></details>
[![Code](https://img.shields.io/github/stars/instantX-research/InstantUnify.svg?style=social&label=Star)](https://github.com/instantX-research/InstantUnify)


+ **Show-o: One Single Transformer to Unify Multimodal Understanding and Generation** (22 Aug 2024)<details><summary>Jinheng Xie, Weijia Mao, Zechen Bai, et al.</summary>Jinheng Xie, Weijia Mao, Zechen Bai, David Junhao Zhang, Weihao Wang, Kevin Qinghong Lin, Yuchao Gu, Zhijie Chen, Zhenheng Yang, Mike Zheng Shou</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.12528)
[![citation](https://img.shields.io/badge/citation-49-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/Show-o%3A-One-Single-Transformer-to-Unify-Multimodal-Xie-Mao/9dc337bd18bc0201839942931b12aff8ec1c93f5)
[![Code](https://img.shields.io/github/stars/showlab/Show-o.svg?style=social&label=Star)](https://github.com/showlab/Show-o)

+ **Image Textualization: An Automatic Framework for Creating Accurate and Detailed Image Descriptions** (11 Jun 2024)<details><summary>Renjie Pi, Jianshu Zhang, Jipeng Zhang et al.</summary> Renjie Pi, Jianshu Zhang, Jipeng Zhang, Rui Pan, Zhekai Chen, Tong Zhang</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07502)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/91b4f447bb06d081a7947b42df57491a04fa46f9)



+ **T2S-GPT: Dynamic Vector Quantization for Autoregressive Sign Language Production from Text** (11 Jun 2024)<details><summary>[ACL 2024] Aoxiong Yin, Haoyuan Li, Kai Shen et al.</summary> Aoxiong Yin, Haoyuan Li, Kai Shen, Siliang Tang, Yueting Zhuang</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07119)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/186910d697bf7eb605aa055aee78fd91ce3ce9fe)


+ **Open-World Human-Object Interaction Detection via Multi-modal Prompts** (11 Jun 2024)<details><summary>Jie Yang, Bingliang Li, Ailing Zeng et al.</summary>Jie Yang, Bingliang Li, Ailing Zeng, Lei Zhang, Ruimao Zhang</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07119)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/186910d697bf7eb605aa055aee78fd91ce3ce9fe)


+ **Commonsense-T2I Challenge: Can Text-to-Image Generation Models Understand Commonsense?** (11 Jun 2024)<details><summary>Xingyu Fu, Muyu He, Yujie Lu et al.</summary>Xingyu Fu, Muyu He, Yujie Lu, William Yang Wang, Dan Roth</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07221v1)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/f0acf2a2293d963c3786e83bb198c75612adc446)



+ **An Image is Worth 32 Tokens for Reconstruction and Generation** (11 Jun 2024)<details><summary>Qihang Yu, Mark Weber, Xueqing Deng et al.</summary> Qihang Yu, Mark Weber, Xueqing Deng, Xiaohui Shen, Daniel Cremers, Liang-Chieh Chen</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07550)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/1e31f4a4ccfc0d1e461be05361d77b5e045f4d37)


+ **TRINS: Towards Multimodal Language Models that Can Read** (10 Jun 2024)<details><summary>[CVPR 2024] Ruiyi Zhang, Yanzhe Zhang, Jian Chen et al.</summary> Ruiyi Zhang, Yanzhe Zhang, Jian Chen, Yufan Zhou, Jiuxiang Gu, Changyou Chen, Tong Sun</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.06730)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/784260e953b2ce34df52086804681e35d57e5843)

+ **[LlamaGen] Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation** (10 Jun 2024)<details><summary>Peize Sun, Yi Jiang, Shoufa Chen et al.</summary>Peize Sun, Yi Jiang, Shoufa Chen, Shilong Zhang, Bingyue Peng, Ping Luo, Zehuan Yuan</details></details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.06525)
[![citation](https://img.shields.io/badge/citation-42-blue.svg?paper=b15e6e2b1d81bc110f8fc98c3caf2e25e2512539)](https://www.semanticscholar.org/paper/Autoregressive-Model-Beats-Diffusion%3A-Llama-for-Sun-Jiang/b15e6e2b1d81bc110f8fc98c3caf2e25e2512539)
[![Code](https://img.shields.io/github/stars/FoundationVision/LlamaGen.svg?style=social&label=Star)](https://github.com/FoundationVision/LlamaGen)



<!-- + **Genie: Generative Interactive Environments** (26 Feb 2024)<details><summary>Jake Bruce, Michael Dennis, Ashley Edwards, et al.</summary> Jake Bruce, Michael Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar, Richie Steigerwald, Chris Apps, Yusuf Aytar, Sarah Bechtle, Feryal Behbahani, Stephanie Chan, Nicolas Heess, Lucy Gonzalez, Simon Osindero, Sherjil Ozair, Scott Reed, Jingwei Zhang, Konrad Zolna, Jeff Clune, Nando de Freitas, Satinder Singh, Tim Rocktäschel</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.15391v1) -->

+ **Chameleon: Mixed-Modal Early-Fusion Foundation Models** (16 May 2024)<details><summary>Chameleon Team</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.09818)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=32112b798f70faab00e14806f51d46058cf5e597)](https://www.semanticscholar.org/paper/Chameleon%3A-Mixed-Modal-Early-Fusion-Foundation-Team/32112b798f70faab00e14806f51d46058cf5e597?utm_source=direct_link)

+ **SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation** (22 Apr 2024)<details><summary>Yuying Ge, Sijie Zhao, Jinguo Zhu, et al.</summary>Yuying Ge, Sijie Zhao, Jinguo Zhu, Yixiao Ge, Kun Yi, Lin Song, Chen Li, Xiaohan Ding, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2404.14396)
[![citation](https://img.shields.io/badge/citation-44-blue.svg?paper=9259b476c31ba52b7e9ed059e5fbce2125092738)](https://www.semanticscholar.org/paper/SEED-X%3A-Multimodal-Models-with-Unified-and-Ge-Zhao/ef03c907ee24e2e6c0f2d24639551c82862d1080)
[![Code](https://img.shields.io/github/stars/AILab-CVC/SEED-X.svg?style=social&label=Star)](https://github.com/AILab-CVC/SEED-X)


+ **Graphic Design with Large Multimodal Model** (22 Apr 2024)<details><summary>Yutao Cheng, Zhao Zhang, Maoke Yang, et al.</summary> Yutao Cheng, Zhao Zhang, Maoke Yang, Hui Nie, Chunyuan Li, Xinglong Wu, and Jie Shao</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2404.14368)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=9259b476c31ba52b7e9ed059e5fbce2125092738)](https://www.semanticscholar.org/paper/9259b476c31ba52b7e9ed059e5fbce2125092738)
[![Code](https://img.shields.io/github/stars/graphic-design-ai/graphist.svg?style=social&label=Star)](https://github.com/graphic-design-ai/graphist)


+ **PMG : Personalized Multimodal Generation with Large Language Models** (7 Apr 2024)<details><summary>Xiaoteng Shen, Rui Zhang, Xiaoyan Zhao, et al.</summary>Xiaoteng Shen, Rui Zhang, Xiaoyan Zhao, Jieming Zhu, Xi Xiao</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2404.08677)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=cfb9eba1b5c55bb0052df41eaaff8716f9c420bd)](https://www.semanticscholar.org/paper/PMG-%3A-Personalized-Multimodal-Generation-with-Large-Shen-Zhang/cfb9eba1b5c55bb0052df41eaaff8716f9c420bd)


+ **MineDreamer: Learning to Follow Instructions via Chain-of-Imagination for Simulated-World Control** (19 Mar 2024)<details><summary>Enshen Zhou, Yiran Qin, Zhenfei Yin, et al.</summary>Enshen Zhou, Yiran Qin, Zhenfei Yin, Yuzhou Huang, Ruimao Zhang, Lu Sheng, Yu Qiao, Jing Shao</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.12037)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=ae06df762adcc4221162e83a737ea63cff47e65d)](https://www.semanticscholar.org/paper/ae06df762adcc4221162e83a737ea63cff47e65d)
[![Code](https://img.shields.io/github/stars/Zhoues/MineDreamer.svg?style=social&label=Star)](https://github.com/Zhoues/MineDreamer)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://sites.google.com/view/minedreamer/main)



+ **ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment** (8 Mar 2024)<details><summary>Xiwei Hu, Rui Wang, Yixiao Fang, et al.</summary> Xiwei Hu, Rui Wang, Yixiao Fang, Bin Fu, Pei Cheng, Gang Yu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.05135)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=da0d382c7fa981ba185ca633868442b75cb76de6)](https://www.semanticscholar.org/paper/da0d382c7fa981ba185ca633868442b75cb76de6)
[![Code](https://img.shields.io/github/stars/ELLA-Diffusion/ELLA.svg?style=social&label=Star)](https://github.com/ELLA-Diffusion/ELLA)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ella-diffusion.github.io/)


+ **StrokeNUWA: Tokenizing Strokes for Vector Graphic Synthesis** (30 Jan 2024)<details><summary>Zecheng Tang, Chenfei Wu, Zekai Zhang, et al.</summary>Zecheng Tang, Chenfei Wu, Zekai Zhang, Mingheng Ni, Shengming Yin, Yu Liu, Zhengyuan Yang, Lijuan Wang, Zicheng Liu, Juntao Li, Nan Duan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.17093)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=b2f6830afe63eb477294f17f0d3a6923135950f9)](https://www.semanticscholar.org/paper/StrokeNUWA%3A-Tokenizing-Strokes-for-Vector-Graphic-Tang-Wu/b2f6830afe63eb477294f17f0d3a6923135950f9)
`tokenizer`

+ **DiffusionGPT: LLM-Driven Text-to-Image Generation System** (18 Jan 2024)<details><summary>Jie Qin, Jie Wu, Weifeng Chen, et al.</summary> Jie Qin, Jie Wu, Weifeng Chen, Yuxi Ren, Huixia Li, Hefeng Wu, Xuefeng Xiao, Rui Wang, Shilei Wen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.10061)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=d4b1a1c62a03ccffcf24983eb4fe22335cbb89b6)](https://www.semanticscholar.org/paper/d4b1a1c62a03ccffcf24983eb4fe22335cbb89b6)
[![Code](https://img.shields.io/github/stars/DiffusionGPT/DiffusionGPT.svg?style=social&label=Star)](https://github.com/DiffusionGPT/DiffusionGPT)


+ **StarVector: Generating Scalable Vector Graphics Code from Images** (17 Dec 2023)<details><summary>Juan A. Rodriguez, Shubham Agarwal, Issam H. Laradji, et al.</summary> Juan A. Rodriguez, Shubham Agarwal, Issam H. Laradji, Pau Rodriguez, David Vazquez, Christopher Pal, Marco Pedersoli</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.11556)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=60d3ade5c0085f5de1f5ab944cc058c78706ac66)](https://www.semanticscholar.org/paper/60d3ade5c0085f5de1f5ab944cc058c78706ac66)
[![Code](https://img.shields.io/github/stars/joanrod/star-vector.svg?style=social&label=Star)](https://github.com/joanrod/star-vector)


+ **VL-GPT: A Generative Pre-trained Transformer for Vision and Language Understanding and Generation** (14 Dec 2023)<details><summary>Jinguo Zhu, Xiaohan Ding, Yixiao Ge, et al.</summary> Jinguo Zhu, Xiaohan Ding, Yixiao Ge, Yuying Ge, Sijie Zhao, Hengshuang Zhao, Xiaohua Wang, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.09251)
[![citation](https://img.shields.io/badge/citation-6-blue.svg?paper=ea6982a936a2b263bbf46ff6eb27fc0b63fddaf7)](https://www.semanticscholar.org/paper/ea6982a936a2b263bbf46ff6eb27fc0b63fddaf7)
[![Code](https://img.shields.io/github/stars/AILab-CVC/VL-GPT.svg?style=social&label=Star)](https://github.com/AILab-CVC/VL-GPT)


+ **StoryGPT-V: Large Language Models as Consistent Story Visualizers** (13 Dec 2023)<details><summary>Xiaoqian Shen, Mohamed Elhoseiny</summary> Xiaoqian Shen, Mohamed Elhoseiny</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.02252)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=e49cb2ab3a7990e3d05042197ae8b3fd934453de)](https://www.semanticscholar.org/paper/e49cb2ab3a7990e3d05042197ae8b3fd934453de)



+ **GENIXER: Empowering Multimodal Large Language Models as a Powerful Data Generator** (11 Dec 2023)<details><summary>Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou</summary> Henry Hengyuan Zhao, Pan Zhou, Mike Zheng Shou</details> 
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.06731)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=cb2295766b2f8f35524f6a9f93ae39d948d50bd4)](https://www.semanticscholar.org/paper/cb2295766b2f8f35524f6a9f93ae39d948d50bd4)


+ **Customization Assistant for Text-to-image Generation** (5 Dec 2023)<details><summary>Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, et al.</summary> Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, Tong Sun</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.03045)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=f30bb09dbd95845d792bdac217a9a652635ee8a5)](https://www.semanticscholar.org/paper/f30bb09dbd95845d792bdac217a9a652635ee8a5)`customization`



+ **ChatIllusion: Efficient-Aligning Interleaved Generation ability with Visual Instruction Model** (29 Nov 2023) <details><summary>Xiaowei Chi, Yijiang Liu, Zhengkai Jiang, et al.</summary> Xiaowei Chi, Yijiang Liu, Zhengkai Jiang, Rongyu Zhang, Ziyi Lin, Renrui Zhang, Peng Gao, Chaoyou Fu, Shanghang Zhang, Qifeng Liu, Yike Guo</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17963)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=22d55c52f43f59634586ab95fefbb7dba8c8b190)](https://www.semanticscholar.org/paper/22d55c52f43f59634586ab95fefbb7dba8c8b190)
[![Code](https://img.shields.io/github/stars/litwellchi/ChatIllusion.svg?style=social&label=Star)](https://github.com/litwellchi/ChatIllusion)


+ **DreamSync: Aligning Text-to-Image Generation with Image Understanding Feedback** (29 Nov 2023) <details><summary>Jiao Sun, Deqing Fu, Yushi Hu, et al.</summary>Jiao Sun, Deqing Fu, Yushi Hu, Su Wang, Royi Rassin, Da-Cheng Juan, Dana Alon, Charles Herrmann, Sjoerd van Steenkiste, Ranjay Krishna, Cyrus Rashtchian</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17946)
[![citation](https://img.shields.io/badge/citation-5-blue.svg?paper=d16f72b7be526dee5eb49e5afffeea2bddba5e66)](https://www.semanticscholar.org/paper/d16f72b7be526dee5eb49e5afffeea2bddba5e66)




+ **COLE: A Hierarchical Generation Framework for Graphic Design** (28 Nov 2023) <details><summary>Peidong Jia, Chenxuan Li, Zeyu Liu, et al.</summary>Peidong Jia, Chenxuan Li, Zeyu Liu, Yichao Shen, Xingru Chen, Yuhui Yuan, Yinglin Zheng, Dong Chen, Ji Li, Xiaodong Xie, Shanghang Zhang, Baining Guo</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16974)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=8441c30ad4abdca9ee380aa6f22ffd731b10231b)](https://www.semanticscholar.org/paper/8441c30ad4abdca9ee380aa6f22ffd731b10231b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://graphic-design-generation.github.io/)



+ **TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering** (28 Nov 2023) <details><summary>Jingye Chen, Yupan Huang, Tengchao Lv, et al.</summary>Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16465)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=1c6e2a4da1ead685a95c079751bf4d7a727d8180)](https://www.semanticscholar.org/paper/1c6e2a4da1ead685a95c079751bf4d7a727d8180)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jingyechen.github.io/textdiffuser2/)
[![Code](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social&label=Star)](https://github.com/microsoft/unilm/tree/master/textdiffuser-2)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/JingyeChen22/TextDiffuser-2)

+ **LLMGA: Multimodal Large Language Model based Generation Assistant** (27 Nov 2023)<details><summary>Bin Xia, Shiyin Wang, Yingfan Tao, et al.</summary> Bin Xia, Shiyin Wang, Yingfan Tao, Yitong Wang, Jiaya Jia</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16500)
[![citation](https://img.shields.io/badge/citation-2-blue.svg?paper=769a924d0af014acec326f50c15c5d70d258a969)](https://www.semanticscholar.org/paper/769a924d0af014acec326f50c15c5d70d258a969)
[![Code](https://img.shields.io/github/stars/dvlab-research/LLMGA.svg?style=social&label=Star)](https://github.com/dvlab-research/LLMGA)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llmga.github.io/)





+ **Self-correcting LLM-controlled Diffusion Models** (27 Nov 2023)<details><summary>Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, et al.</summary> Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, Boyi Li, Trevor Darrell</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16090)
[![citation](https://img.shields.io/badge/citation-4-blue.svg?paper=42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e)](https://www.semanticscholar.org/paper/42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e)
[![Code](https://img.shields.io/github/stars/tsunghan-wu/SLD.svg?style=social&label=Star)](https://github.com/tsunghan-wu/SLD)


+ **[ParaDiffusion] Paragraph-to-Image Generation with Information-Enriched Diffusion Model** (29 Nov 2023)<details><summary>Weijia Wu, Zhuang Li, Yefei He, et al.</summary>Weijia Wu, Zhuang Li, Yefei He, Mike Zheng Shou, Chunhua Shen, Lele Cheng, Yan Li, Tingting Gao, Di Zhang, Zhongyuan Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.14284)
[![citation](https://img.shields.io/badge/citation-19-blue.svg?paper=ed4f1b0f6c09f59d07e817e532a25f4d25e94dbc)](https://www.semanticscholar.org/paper/ed4f1b0f6c09f59d07e817e532a25f4d25e94dbc)
[![Code](https://img.shields.io/github/stars/weijiawu/ParaDiffusion.svg?style=social&label=Star)](https://github.com/weijiawu/ParaDiffusion)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://weijiawu.github.io/ParaDiffusionPage/)


+ **Tokenize and Embed ALL for Multi-modal Large Language Models** (8 Nov 2023)<details><summary>Zhen Yang, Yingxue Zhang, Fandong Meng, et al.</summary> Zhen Yang, Yingxue Zhang, Fandong Meng, Jie Zhou</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.04589)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=59d716b442ab760a78f58de6748c0fa1d507bfc1)](https://www.semanticscholar.org/paper/59d716b442ab760a78f58de6748c0fa1d507bfc1)
`tokenizer`


+ **WordArt Designer: User-Driven Artistic Typography Synthesis using Large Language Models** (20 Oct 2023)<details><summary>Jun-Yan He, Zhi-Qi Cheng, Chenyang Li, et al.</summary> Jun-Yan He, Zhi-Qi Cheng, Chenyang Li, Jingdong Sun, Wangmeng Xiang, Xianhui Lin, Xiaoyang Kang, Zengke Jin, Yusen Hu, Bin Luo, Yifeng Geng, Xuansong Xie, Jingren Zhou</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.18332)
[![citation](https://img.shields.io/badge/citation-4-blue.svg?paper=58b77dc0603eb52559d98a383bf9649fd31d0bc5)](https://www.semanticscholar.org/paper/58b77dc0603eb52559d98a383bf9649fd31d0bc5)


+ **LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts** (16 Oct 2023)<details><summary>[ICLR 2024] Hanan Gani, Shariq Farooq Bhat, Muzammal Naseer, et al.</summary>Hanan Gani, Shariq Farooq Bhat, Muzammal Naseer, Salman Khan, Peter Wonka</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.10640)
[![citation](https://img.shields.io/badge/citation-4-blue.svg?paper=4cb2c262ce34f41974f1b1623fc5a6e32956ded3)](https://www.semanticscholar.org/paper/4cb2c262ce34f41974f1b1623fc5a6e32956ded3)
[![Code](https://img.shields.io/github/stars/hananshafi/llmblueprint.svg?style=social&label=Star)](https://github.com/hananshafi/llmblueprint)



+ **Making Multimodal Generation Easier: When Diffusion Models Meet LLMs** (13 Oct 2023)<details><summary>Xiangyu Zhao, Bo Liu, Qijiong Liu, et al.</summary>Xiangyu Zhao, Bo Liu, Qijiong Liu, Guangyuan Shi, Xiao-Ming Wu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08949v1)
[![citation](https://img.shields.io/badge/citation-N/A-blue.svg?paper=833cdd713c27ab5899bb912a1d511c10af61cefb)](https://www.semanticscholar.org/paper/833cdd713c27ab5899bb912a1d511c10af61cefb)
[![Code](https://img.shields.io/github/stars/zxy556677/EasyGen.svg?style=social&label=Star)](https://github.com/zxy556677/EasyGen)


+ **Idea2Img: Iterative Self-Refinement with GPT-4V(ision) for Automatic Image Design and Generation** (12 Oct 2023)<details><summary>Zhengyuan Yang, Jianfeng Wang, Linjie Li, et al.</summary>Zhengyuan Yang, Jianfeng Wang, Linjie Li, Kevin Lin, Chung-Ching Lin, Zicheng Liu, Lijuan Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08541)
[![citation](https://img.shields.io/badge/citation-6-blue.svg?paper=1d14a708622917da4b9820ada6d32af24fc1651a)](https://www.semanticscholar.org/paper/1d14a708622917da4b9820ada6d32af24fc1651a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://idea2img.github.io/)
[![Code](https://img.shields.io/github/stars/zyang-ur/Idea2Img.svg?style=social&label=Star)](https://github.com/zyang-ur/Idea2Img)


+ **OpenLEAF: Open-Domain Interleaved Image-Text Generation and Evaluation** (11 Oct 2023)<details><summary>Jie An, Zhengyuan Yang, Linjie Li, et al.</summary>Jie An, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu, Lijuan Wang, Jiebo Luo</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.07749)
[![citation](https://img.shields.io/badge/citation-3-blue.svg?paper=7f1ba5630c3baa09b11cc665b3f71cdb117e5ffb)](https://www.semanticscholar.org/paper/7f1ba5630c3baa09b11cc665b3f71cdb117e5ffb)



+ **Mini-DALLE3: Interactive Text to Image by Prompting Large Language Models** (11 Oct 2023)<details><summary>Zeqiang Lai, Xizhou Zhu, Jifeng Dai, et al.</summary>Zeqiang Lai, Xizhou Zhu, Jifeng Dai, Yu Qiao, Wenhai Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.07653)
[![citation](https://img.shields.io/badge/citation-6-blue.svg?paper=f669d7a6fab0147253178a6fc854e05e3d92fb3f)](https://www.semanticscholar.org/paper/f669d7a6fab0147253178a6fc854e05e3d92fb3f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://minidalle3.github.io/)
[![Code](https://img.shields.io/github/stars/Zeqiang-Lai/Mini-DALLE3.svg?style=social&label=Star)](https://github.com/Zeqiang-Lai/Mini-DALLE3)


+ **[DALL-E 3] Improving Image Generation with Better Captions** <details><summary>James Betker, Gabriel Goh, Li Jing, et al.</summary>James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu, Yunxin Jiao, Aditya Ramesh</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://cdn.openai.com/papers/dall-e-3.pdf)
[![citation](https://img.shields.io/badge/citation-146-blue.svg?paper=cfee1826dd4743eab44c6e27a0cc5970effa4d80)](https://www.semanticscholar.org/paper/cfee1826dd4743eab44c6e27a0cc5970effa4d80)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://openai.com/dall-e-3)


+ **MiniGPT-5: Interleaved Vision-and-Language Generation via Generative Vokens** (3 Oct 2023)\
Kaizhi Zheng, Xuehai He, Xin Eric Wang.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.02239)
[![citation](https://img.shields.io/badge/citation-26-blue.svg?paper=e7d09b6f2bc878cf2c993acf675f409d0b55f35a)](https://www.semanticscholar.org/paper/e7d09b6f2bc878cf2c993acf675f409d0b55f35a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://eric-ai-lab.github.io/minigpt-5.github.io/)
[![Code](https://img.shields.io/github/stars/eric-ai-lab/MiniGPT-5.svg?style=social&label=Star)](https://github.com/eric-ai-lab/MiniGPT-5)


+ **Making LLaMA SEE and Draw with SEED Tokenizer** (2 Oct 2023)<details><summary>Yuying Ge, Sijie Zhao, Ziyun Zeng, et al.</summary>Yuying Ge, Sijie Zhao, Ziyun Zeng, Yixiao Ge, Chen Li, Xintao Wang, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.01218)
[![citation](https://img.shields.io/badge/citation-19-blue.svg?paper=5ba1525dc6d382ee0a4a1ca3c64fc5907ca64c67)](https://www.semanticscholar.org/paper/5ba1525dc6d382ee0a4a1ca3c64fc5907ca64c67)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/seed/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/SEED.svg?style=social&label=Star)](https://github.com/AILab-CVC/SEED)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://dad1ed9a9fb76fe83b.gradio.live/)
`tokenizer`


+ **InstructCV: Instruction-Tuned Text-to-Image Diffusion Models as Vision Generalists** (30 Sep 2023)<details><summary>Yulu Gan, Sungwoo Park, Alexander Schubert, et al.</summary>Yulu Gan, Sungwoo Park, Alexander Schubert, Anthony Philippakis, Ahmed M. Alaa</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.00390)
[![citation](https://img.shields.io/badge/citation-5-blue.svg?paper=819f477065088220a6f706cd9ef76dbcb4b4c134)](https://www.semanticscholar.org/paper/819f477065088220a6f706cd9ef76dbcb4b4c134)
[![Code](https://img.shields.io/github/stars/AlaaLab/InstructCV.svg?style=social&label=Star)](https://github.com/AlaaLab/InstructCV)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/alaa-lab/InstructCV)

+ **InternLM-XComposer: A Vision-Language Large Model for Advanced Text-image Comprehension and Composition** (26 Sep 2023)<details><summary>Pan Zhang, Xiaoyi Dong, Bin Wang, et al.</summary> Pan Zhang, Xiaoyi Dong, Bin Wang, Yuhang Cao, Chao Xu, Linke Ouyang, Zhiyuan Zhao, Haodong Duan, Songyang Zhang, Shuangrui Ding, Wenwei Zhang, Hang Yan, Xinyue Zhang, Wei Li, Jingwen Li, Kai Chen, Conghui He, Xingcheng Zhang, Yu Qiao, Dahua Lin, Jiaqi Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.15112)
[![citation](https://img.shields.io/badge/citation-48-blue.svg?paper=c1e450284e7d6cac1855330a1197df8537df653f)](https://www.semanticscholar.org/paper/c1e450284e7d6cac1855330a1197df8537df653f)
[![Code](https://img.shields.io/github/stars/InternLM/InternLM-XComposer.svg?style=social&label=Star)](https://github.com/InternLM/InternLM-XComposer)




+ **Text-to-Image Generation for Abstract Concepts** (26 Sep 2023) <details><summary>Jiayi Liao, Xu Chen, Qiang Fu, et al.</summary>Jiayi Liao, Xu Chen, Qiang Fu, Lun Du, Xiangnan He, Xiang Wang, Shi Han, Dongmei Zhang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.14623)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=0d38f1edac66b4645cf5fa05abaf9d92cba5d5d3)](https://www.semanticscholar.org/paper/0d38f1edac66b4645cf5fa05abaf9d92cba5d5d3)




+ **DreamLLM: Synergistic Multimodal Comprehension and Creation** (20 Sep 2023)<details><summary>[ICLR 2024] Runpei Dong, Chunrui Han, Yuang Peng, et al.</summary>Runpei Dong, Chunrui Han, Yuang Peng, Zekun Qi, Zheng Ge, Jinrong Yang, Liang Zhao, Jianjian Sun, Hongyu Zhou, Haoran Wei, Xiangwen Kong, Xiangyu Zhang, Kaisheng Ma, Li Yi</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.11499)
[![citation](https://img.shields.io/badge/citation-38-blue.svg?paper=7b689adb8c156d6158660f90d1c86888ee281f63)](https://www.semanticscholar.org/paper/7b689adb8c156d6158660f90d1c86888ee281f63)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreamllm.github.io/)
[![Code](https://img.shields.io/github/stars/RunpeiDong/DreamLLM.svg?style=social&label=Star)](https://github.com/RunpeiDong/DreamLLM)


+ **SwitchGPT: Adapting Large Language Models for Non-Text Outputs** (14 Sep 2023)\
Wang, Xinyu, Bohan Zhuang, and Qi Wu.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.07623)
[![citation](https://img.shields.io/badge/citation-2-blue.svg?paper=366564d210768814bc880e391b909cfbd95f8964)](https://www.semanticscholar.org/paper/366564d210768814bc880e391b909cfbd95f8964)
[![Code](https://img.shields.io/github/stars/xinke-wang/SwitchGPT.svg?style=social&label=Star)](https://github.com/xinke-wang/SwitchGPT)

+ **NExT-GPT: Any-to-Any Multimodal LLM** (11 Sep 2023)<details><summary>Shengqiong Wu, Hao Fei, Leigang Qu, et al.</summary>Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, Tat-Seng Chua</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.05519)
[![citation](https://img.shields.io/badge/citation-94-blue.svg?paper=fa75a55760e6ea49b39b83cb85c99a22e1088254)](https://www.semanticscholar.org/paper/fa75a55760e6ea49b39b83cb85c99a22e1088254)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://next-gpt.github.io/)
[![Code](https://img.shields.io/github/stars/NExT-GPT/NExT-GPT.svg?style=social&label=Star)](https://github.com/NExT-GPT/NExT-GPT)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://9704af1b453125102e.gradio.live/)

+ **LayoutLLM-T2I: Eliciting Layout Guidance from LLM for Text-to-Image Generation** (9 Aug 2023)<details><summary>Leigang Qu, Shengqiong Wu, Hao Fei, et al. ACM MM 2023</summary>Leigang Qu, Shengqiong Wu, Hao Fei, Liqiang Nie, Tat-Seng Chua</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.05095)
[![citation](https://img.shields.io/badge/citation-10-blue.svg?paper=7d78238a9bad60433d616abdd93c735087d99670)](https://www.semanticscholar.org/paper/7d78238a9bad60433d616abdd93c735087d99670)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://layoutllm-t2i.github.io/)
[![Code](https://img.shields.io/github/stars/LayoutLLM-T2I/LayoutLLM-T2I.svg?style=social&label=Star)](https://github.com/LayoutLLM-T2I/LayoutLLM-T2I)

+ **Planting a SEED of Vision in Large Language Model** (16 Jul 2023)<details><summary>Yuying Ge, Yixiao Ge, Ziyun Zeng, et al.</summary>Yuying Ge, Yixiao Ge, Ziyun Zeng, Xintao Wang, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.08041)
[![citation](https://img.shields.io/badge/citation-30-blue.svg?paper=40298b8d50109c52fc10763eddc64a07cf8acb31)](https://www.semanticscholar.org/paper/40298b8d50109c52fc10763eddc64a07cf8acb31)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/seed/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/SEED.svg?style=social&label=Star)](https://github.com/AILab-CVC/SEED)

+ **Generative Pretraining in Multimodality** (11 Jul 2023)<details><summary>Quan Sun, Qiying Yu, Yufeng Cui, et al.</summary>Quan Sun, Qiying Yu, Yufeng Cui, Fan Zhang, Xiaosong Zhang, Yueze Wang, Hongcheng Gao, Jingjing Liu, Tiejun Huang, Xinlong Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.05222)
[![citation](https://img.shields.io/badge/citation-43-blue.svg?paper=94053805cd59f2e9a47fe3f080c7e7afefb337cc)](https://www.semanticscholar.org/paper/94053805cd59f2e9a47fe3f080c7e7afefb337cc)
[![Code](https://img.shields.io/github/stars/baaivision/Emu.svg?style=social&label=Star)](https://github.com/baaivision/Emu)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](http://218.91.113.230:9002)

+ **SPAE: Semantic Pyramid AutoEncoder for Multimodal Generation with Frozen LLMs** (30 Jun 2023) <details><summary>[NeurIPS 2023 Spotlight] Lijun Yu, Yong Cheng, Zhiruo Wang, et al.</summary>Lijun Yu, Yong Cheng, Zhiruo Wang, Vivek Kumar, Wolfgang Macherey, Yanping Huang, David A. Ross, Irfan Essa, Yonatan Bisk, Ming-Hsuan Yang, Kevin Murphy, Alexander G. Hauptmann, Lu Jiang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.17842)
[![citation](https://img.shields.io/badge/citation-12-blue.svg?paper=376f494126d1ea4f571ea0263c43ac2b6331800a)](https://www.semanticscholar.org/paper/376f494126d1ea4f571ea0263c43ac2b6331800a)

+ **Controllable Text-to-Image Generation with GPT-4** (29 May 2023) <details><summary>Tianjun Zhang, Yi Zhang, Vibhav Vineet, et al.</summary>Tianjun Zhang, Yi Zhang, Vibhav Vineet, Neel Joshi, Xin Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.18583)
[![citation](https://img.shields.io/badge/citation-20-blue.svg?paper=3a79545719fb193a6b4042ef7d1d87cfd267be06)](https://www.semanticscholar.org/paper/3a79545719fb193a6b4042ef7d1d87cfd267be06)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://github.com/tianjunz/Control-GPT) 

+ **Generating Images with Multimodal Language Models** (26 May 2023)\
[NeurIPS 2023] Koh, Jing Yu, Daniel Fried, and Ruslan Salakhutdinov. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.17216)
[![citation](https://img.shields.io/badge/citation-73-blue.svg?paper=6fb5c0eff3696ef252aca9638e10176ecce7cecb)](https://www.semanticscholar.org/paper/6fb5c0eff3696ef252aca9638e10176ecce7cecb)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jykoh.com/gill)
[![Code](https://img.shields.io/github/stars/kohjingyu/gill.svg?style=social&label=Star)](https://github.com/kohjingyu/gill)

+ **LayoutGPT: Compositional Visual Planning and Generation with Large Language Models** (24 May 2023)<details><summary>[NeurIPS 2023] Weixi Feng, Wanrong Zhu, Tsu-jui Fu, et al.</summary>Weixi Feng, Wanrong Zhu, Tsu-jui Fu, Varun Jampani, Arjun Akula, Xuehai He, Sugato Basu, Xin Eric Wang, William Yang Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.15393)
[![citation](https://img.shields.io/badge/citation-31-blue.svg?paper=66d755730f5d08a6f4fcc5e81f24982ba389dca9)](https://www.semanticscholar.org/paper/66d755730f5d08a6f4fcc5e81f24982ba389dca9)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://layoutgpt.github.io/)
[![Code](https://img.shields.io/github/stars/weixi-feng/LayoutGPT.svg?style=social&label=Star)](https://github.com/weixi-feng/LayoutGPT)

+ **Visual Programming for Text-to-Image Generation and Evaluation** (24 May 2023)\
[NeurIPS 2023] Jaemin Cho, Abhay Zala, Mohit Bansal.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.15328)
[![citation](https://img.shields.io/badge/citation-24-blue.svg?paper=9837349417e36ef5be06da0fd6c74042148bdaa2)](https://www.semanticscholar.org/paper/9837349417e36ef5be06da0fd6c74042148bdaa2)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://vp-t2i.github.io/)
[![Code](https://img.shields.io/github/stars/j-min/VPGen.svg?style=social&label=Star)](https://github.com/j-min/VPGen)

+ **LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models** (23 May 2023) <details><summary>Long Lian, Boyi Li, Adam Yala, et al.</summary>Long Lian, Boyi Li, Adam Yala, Trevor Darrell</details>[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.13655)
[![citation](https://img.shields.io/badge/citation-39-blue.svg?paper=e9ae0c76a71b8f302eb17b1c4462b9cc97d87cd0)](https://www.semanticscholar.org/paper/e9ae0c76a71b8f302eb17b1c4462b9cc97d87cd0)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llm-grounded-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedDiffusion)

+ **Interactive Data Synthesis for Systematic Vision Adaptation via LLMs-AIGCs Collaboration** (22 May 2023)<details><summary>Qifan Yu, Juncheng Li, Wentao Ye, et al.</summary>Qifan Yu, Juncheng Li, Wentao Ye, Siliang Tang, Yueting Zhuang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.12799)
[![citation](https://img.shields.io/badge/citation-7-blue.svg?paper=43a55dbd95c9d5cd82de8db276f41adeec4a937d)](https://www.semanticscholar.org/paper/43a55dbd95c9d5cd82de8db276f41adeec4a937d)
[![Code](https://img.shields.io/github/stars/Yuqifan1117/Labal-Anything-Pipeline.svg?style=social&label=Star)](https://github.com/Yuqifan1117/Labal-Anything-Pipeline)

+ **LLMScore: Unveiling the Power of Large Language Models in Text-to-Image Synthesis Evaluation** (18 May 2023)<details><summary>[NeurIPS 2023] Yujie Lu, Xianjun Yang, Xiujun Li, et al.</summary>Yujie Lu, Xianjun Yang, Xiujun Li, Xin Eric Wang, William Yang Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.11116)
[![citation](https://img.shields.io/badge/citation-10-blue.svg?paper=972501b057e2b84d6ce6506f70bcac697bab7872)](https://www.semanticscholar.org/paper/972501b057e2b84d6ce6506f70bcac697bab7872)
[![Code](https://img.shields.io/github/stars/YujieLu10/LLMScore.svg?style=social&label=Star)](https://github.com/YujieLu10/LLMScore)

+ **SUR-adapter: Enhancing Text-to-Image Pre-trained Diffusion Models with Large Language Models** (9 May 2023)<details><summary>[ACM MM 2023] Shanshan Zhong, Zhongzhan Huang, Wushao Wen, et al.</summary>Shanshan Zhong, Zhongzhan Huang, Wushao Wen, Jinghui Qin, Liang Lin</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.05189)
[![Code](https://img.shields.io/github/stars/Qrange-group/SUR-adapter.svg?style=social&label=Star)](https://github.com/Qrange-group/SUR-adapter)

+ **Grounding Language Models to Images for Multimodal Inputs and Outputs** (31 Jan 2023)\
[ICML 2023] Koh, Jing Yu, Ruslan Salakhutdinov, and Daniel Fried.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.13823)
[![citation](https://img.shields.io/badge/citation-35-blue.svg?paper=6173520a1eb2814d067e8c5fd16212b7cbf6ee78)](https://www.semanticscholar.org/paper/6173520a1eb2814d067e8c5fd16212b7cbf6ee78)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jykoh.com/fromage)
[![Code](https://img.shields.io/github/stars/kohjingyu/fromage.svg?style=social&label=Star)](https://github.com/kohjingyu/fromage)

+ **[RPG-DiffusionMaster] Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs** (22 Jan 2024) <details><summary>[ICML 2024] Ling Yang, Zhaochen Yu, Chenlin Meng, et al.</summary>Ling Yang, Zhaochen Yu, Chenlin Meng, Minkai Xu, Stefano Ermon, Bin Cui</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.11708)
[![citation](https://img.shields.io/badge/citation-23-blue.svg?paper=140cfda71bfff852c3e205b7ad61854b78c76982)](https://www.semanticscholar.org/paper/140cfda71bfff852c3e205b7ad61854b78c76982)
[![Code](https://img.shields.io/github/stars/YangLing0818/RPG-DiffusionMaster.svg?style=social&label=Star)](https://github.com/YangLing0818/RPG-DiffusionMaster)

+ **RealCompo: Balancing Realism and Compositionality Improves Text-to-Image Diffusion Models** (20 Feb 2024)<details><summary>Xinchen Zhang, Ling Yang, Yaqi Cai, et al.</summary>Xinchen Zhang, Ling Yang, Yaqi Cai, Zhaochen Yu, Kai-Ni Wang, Jiake Xie, Ye Tian, Minkai Xu, Yong Tang, Yujiu Yang, Bin Cui</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.12908)
[![citation](https://img.shields.io/badge/citation-6-blue.svg?paper=9c2ba04c376f127da506b63c566887fca2861b25)](https://www.semanticscholar.org/paper/9c2ba04c376f127da506b63c566887fca2861b25)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://cominclip.github.io/RealCompo_Page/)
[![Code](https://img.shields.io/github/stars/YangLing0818/RealCompo.svg?style=social&label=Star)](https://github.com/YangLing0818/RealCompo)

### Non-LLM-based (Clip/T5)
+ **Edify Image: High-Quality Image Generation with Pixel Space Laplacian Diffusion Models** (11 Nov 2024)<details><summary>NVIDIA: Yuval Atzmon, Maciej Bala, Yogesh Balaji, et al.</summary>NVIDIA: Yuval Atzmon, Maciej Bala, Yogesh Balaji, Tiffany Cai, Yin Cui, Jiaojiao Fan, Yunhao Ge, Siddharth Gururani, Jacob Huffman, Ronald Isaac, Pooya Jannaty, Tero Karras, Grace Lam, J. P. Lewis, Aaron Licata, Yen-Chen Lin, Ming-Yu Liu, Qianli Ma, Arun Mallya, Ashlee Martino-Tarr, Doug Mendez, Seungjun Nah, Chris Pruett, Fitsum Reda, Jiaming Song, Ting-Chun Wang, Fangyin Wei, Xiaohui Zeng, Yu Zeng, Qinsheng Zhang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.06959)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://research.nvidia.com/labs/dir/edify-image/)


+ **InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation** (3 Apr 2024)<details><summary>Haofan Wang, Matteo Spinelli, Qixun Wang, et al.</summary>Haofan Wang, Matteo Spinelli, Qixun Wang, Xu Bai, Zekui Qin, Anthony Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2404.02733)
[![citation](https://img.shields.io/badge/citation-N/A-blue.svg?paper=6b5fc164c4f21e4a4f151df60bfd5e32b061a903)](https://www.semanticscholar.org/paper/InstantStyle%3A-Free-Lunch-towards-Style-Preserving-Wang-Spinelli/6b5fc164c4f21e4a4f151df60bfd5e32b061a903)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://instantstyle.github.io/)
[![Code](https://img.shields.io/github/stars/instantX-research/InstantStyle.svg?style=social&label=Star)](https://github.com/instantX-research/InstantStyle)

+ **InstantID: Zero-shot Identity-Preserving Generation in Seconds** (15 Jan 2024)<details><summary>Qixun Wang, Xu Bai, Haofan Wang, et al.</summary>Qixun Wang, Xu Bai, Haofan Wang, Zekui Qin, Anthony Chen, Huaxia Li, Xu Tang, Yao Hu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.07519)
[![citation](https://img.shields.io/badge/citation-N/A-blue.svg?paper=0f9b66c9208b11369e9d94d85b7dc23bcc5115e9)](https://www.semanticscholar.org/paper/InstantID%3A-Zero-shot-Identity-Preserving-Generation-Wang-Bai/0f9b66c9208b11369e9d94d85b7dc23bcc5115e9)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://instantid.github.io/)
[![Code](https://img.shields.io/github/stars/instantX-research/InstantID.svg?style=social&label=Star)](https://github.com/instantX-research/InstantID)

+ **PIXART-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis** (30 Sep 2023)<details><summary>[ICLR 2024] Junsong Chen, Jincheng Yu, Chongjian Ge, et al.</summary>Junsong Chen, Jincheng Yu, Chongjian Ge, Lewei Yao, Enze Xie, Yue Wu, Zhongdao Wang, James Kwok, Ping Luo, Huchuan Lu, Zhenguo Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.00426)
[![citation](https://img.shields.io/badge/citation-N/A-blue.svg?paper=7dfe1c9f1d7120102499c7e561efc2326e7a0358)](https://www.semanticscholar.org/paper/7dfe1c9f1d7120102499c7e561efc2326e7a0358)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://pixart-alpha.github.io/)
[![Code](https://img.shields.io/github/stars/PixArt-alpha/PixArt-alpha.svg?style=social&label=Star)](https://github.com/PixArt-alpha/PixArt-alpha)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/PixArt-alpha/PixArt-alpha)

+ **TextDiffuser: Diffusion Models as Text Painters** (18 May 2023) <details><summary>[NeurIPS 2023] Jingye Chen, Yupan Huang, Tengchao Lv, et al.</summary>Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.10855)
[![citation](https://img.shields.io/badge/citation-12-blue.svg?paper=e779781f1bea273573fc9d3f1a5e874bcff2cd2b)](https://www.semanticscholar.org/paper/e779781f1bea273573fc9d3f1a5e874bcff2cd2b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jingyechen.github.io/textdiffuser/)
[![Code](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social&label=Star)](https://github.com/microsoft/unilm/tree/master/textdiffuser)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/JingyeChen22/TextDiffuser)

+ **TiGAN: Text-Based Interactive Image Generation and Manipulation** (Dec 2022)<details><summary>[AAAI 2022] Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, et al.</summary>Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, Chris Tensmeyer, Tong Yu,Changyou Chen, Jinhui Xu, Tong Sun</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/20270)
[![citation](https://img.shields.io/badge/citation-9-blue.svg?paper=839dc73c1adae268144d9cfb9d70985b2001304f)](https://www.semanticscholar.org/paper/839dc73c1adae268144d9cfb9d70985b2001304f)
Tags: `iteractive`

+ **Multi-Concept Customization of Text-to-Image Diffusion** (8 Dec 2022)<details><summary>[CVPR 2023] Nupur Kumari, Bingliang Zhang, Richard Zhang, et al.</summary>Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.04488)
[![citation](https://img.shields.io/badge/citation-307-blue.svg?paper=144eca44e250cc462f6fc3a172abb865978f66f5)](https://www.semanticscholar.org/paper/144eca44e250cc462f6fc3a172abb865978f66f5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.cs.cmu.edu/~custom-diffusion/)
[![Code](https://img.shields.io/github/stars/adobe-research/custom-diffusion.svg?style=social&label=Star)](https://github.com/adobe-research/custom-diffusion)\
Tags: `customization`

+ **DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation** (25 Aug 2022)<details><summary>[CVPR 2023] Nataniel Ruiz, Yuanzhen Li, Varun Jampani, et al.</summary>Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, Kfir Aberman</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.12242)
[![citation](https://img.shields.io/badge/citation-1090-blue.svg?paper=5b19bf6c3f4b25cac96362c98b930cf4b37f6744)](https://www.semanticscholar.org/paper/5b19bf6c3f4b25cac96362c98b930cf4b37f6744)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreambooth.github.io/)\
Tags: `customization`

+ **An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion** (2 Aug 2022)<details><summary>Rinon Gal, Yuval Alaluf, Yuval Atzmon, et al. </summary>Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.01618)
[![citation](https://img.shields.io/badge/citation-1090-blue.svg?paper=5b19bf6c3f4b25cac96362c98b930cf4b37f6744)](https://www.semanticscholar.org/paper/5b19bf6c3f4b25cac96362c98b930cf4b37f6744)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreambooth.github.io/)
[![Code](https://img.shields.io/github/stars/rinongal/textual_inversion.svg?style=social&label=Star)](https://github.com/rinongal/textual_inversion)\
Tags: `customization`

+ **Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding** (23 May 2022)\
[NeurIPS 2022] <details><summary>Saharia, Chitwan Chan, William Saxena, Saurabh Li, Lala Whang, Jay Denton, Emily L Ghasemipour, Kamyar Gontijo Lopes, Raphael Karagol Ayan, Burcu Salimans, Tim others</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2205.11487)
[![citation](https://img.shields.io/badge/citation-2844-blue.svg?paper=9695824d7a01fad57ba9c01d7d76a519d78d65e7)](https://www.semanticscholar.org/paper/9695824d7a01fad57ba9c01d7d76a519d78d65e7)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://imagen.research.google/) 

+ **High-Resolution Image Synthesis with Latent Diffusion Models** (20 Dec 2021)\
[CVPR 2022 (Oral)] <details><summary>Rombach, Robin Blattmann, Andreas Lorenz, et al. </summary>Rombach, Robin Blattmann, Andreas Lorenz, Dominik Esser, Patrick Ommer, Bj{\"o}rn</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2112.10752)
[![citation](https://img.shields.io/badge/citation-5641-blue.svg?paper=c10075b3746a9f3dd5811970e93c8ca3ad39b39d)](https://www.semanticscholar.org/paper/c10075b3746a9f3dd5811970e93c8ca3ad39b39d)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ommer-lab.com/research/latent-diffusion-models/)
[![Code](https://img.shields.io/github/stars/CompVis/stable-diffusion.svg?style=social&label=Star)](https://github.com/CompVis/stable-diffusion)

### Datasets


+ **MIMIC-IT: Multi-Modal In-Context Instruction Tuning** (8 Jun 2023)<details><summary>[NeurIPS 2023] Bo Li, Yuanhan Zhang, Liangyu Chen, et al.</summary>Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Fanyi Pu, Jingkang Yang, Chunyuan Li, Ziwei Liu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.05425)
[![citation](https://img.shields.io/badge/citation-78-blue.svg?paper=d47524cd5c3c4b57af2e5a29f6f91c420310f236)](https://www.semanticscholar.org/paper/d47524cd5c3c4b57af2e5a29f6f91c420310f236)
[![Code](https://img.shields.io/github/stars/Luodian/otter.svg?style=social&label=Star)](https://github.com/Luodian/otter)



+ **[LAION-Glyph] GlyphControl: Glyph Conditional Control for Visual Text Generation** (29 May 2023)<details><summary>[NeurIPS 2023] Yukang Yang, Dongnan Gui, Yuhui Yuan, et al.</summary>Yukang Yang, Dongnan Gui, Yuhui Yuan, Weicong Liang, Haisong Ding, Han Hu, Kai Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.18259)
[![citation](https://img.shields.io/badge/citation-12-blue.svg?paper=5fbe4c92791fbecb179c1ab79bba9a59b2e155ba)](https://www.semanticscholar.org/paper/5fbe4c92791fbecb179c1ab79bba9a59b2e155ba)
[![Code](https://img.shields.io/github/stars/AIGText/GlyphControl-release.svg?style=social&label=Star)](https://github.com/AIGText/GlyphControl-release)





+ **[MARIO-10M] TextDiffuser: Diffusion Models as Text Painters** (18 May 2023)<details><summary>[NeurIPS 2023] Jingye Chen, Yupan Huang, Tengchao Lv, et al.</summary>Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.14108)
[![citation](https://img.shields.io/badge/citation-12-blue.svg?paper=e779781f1bea273573fc9d3f1a5e874bcff2cd2b)](https://www.semanticscholar.org/paper/e779781f1bea273573fc9d3f1a5e874bcff2cd2b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jingyechen.github.io/textdiffuser/)
[![Code](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social&label=Star)](https://github.com/microsoft/unilm)



+ **DataComp: In search of the next generation of multimodal datasets** (27 Apr 2023)<details><summary>[NeurIPS 2023] Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang, et al.</summary>Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang, Jonathan Hayase, Georgios Smyrnis, Thao Nguyen, Ryan Marten, Mitchell Wortsman, Dhruba Ghosh, Jieyu Zhang, Eyal Orgad, Rahim Entezari, Giannis Daras, Sarah Pratt, Vivek Ramanujan, Yonatan Bitton, Kalyani Marathe, Stephen Mussmann, Richard Vencu, Mehdi Cherti, Ranjay Krishna, Pang Wei Koh, Olga Saukh, Alexander Ratner, Shuran Song, Hannaneh Hajishirzi, Ali Farhadi, Romain Beaumont, Sewoong Oh, Alex Dimakis, Jenia Jitsev, Yair Carmon, Vaishaal Shankar, Ludwig Schmidt</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.14108)
[![citation](https://img.shields.io/badge/citation-103-blue.svg?paper=f9570989919338079088270a9cf1a7afc8db8093)](https://www.semanticscholar.org/paper/f9570989919338079088270a9cf1a7afc8db8093)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.datacomp.ai/)
[![Code](https://img.shields.io/github/stars/mlfoundations/datacomp.svg?style=social&label=Star)](https://github.com/mlfoundations/datacomp)

+ **[LLava-instruct] Visual Instruction Tuning** (17 Apr 2023)<details><summary>[NeurIPS 2023] Haotian Liu, Chunyuan Li, Qingyang Wu, et al.</summary>Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.08485)
[![citation](https://img.shields.io/badge/citation-820-blue.svg?paper=a5036f31f0e629dc661f120b8c3b1f374d479ab8)](https://www.semanticscholar.org/paper/a5036f31f0e629dc661f120b8c3b1f374d479ab8)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llava-vl.github.io//)
[![Code](https://img.shields.io/github/stars/haotian-liu/LLaVA.svg?style=social&label=Star)](https://github.com/haotian-liu/LLaVA)



+ **Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved with Text** (14 Apr 2023)<details><summary>[NeurIPS 2023] Wanrong Zhu, Jack Hessel, Anas Awadalla, et al.</summary>Wanrong Zhu, Jack Hessel, Anas Awadalla, Samir Yitzhak Gadre, Jesse Dodge, Alex Fang, Youngjae Yu, Ludwig Schmidt, William Yang Wang, Yejin Choi</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.06939)
[![citation](https://img.shields.io/badge/citation-64-blue.svg?paper=df958800014d310b6df34ad83d771314d68fbb2d)](https://www.semanticscholar.org/paper/df958800014d310b6df34ad83d771314d68fbb2d)
[![Code](https://img.shields.io/github/stars/allenai/mmc4.svg?style=social&label=Star)](https://github.com/allenai/mmc4)





+ **Language Is Not All You Need: Aligning Perception with Language Models** (27 Feb 2023)<details><summary>[NeurIPS 2023] Shaohan Huang, Li Dong, Wenhui Wang, et al.</summary>Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui, Owais Khan Mohammed, Barun Patra, Qiang Liu, Kriti Aggarwal, Zewen Chi, Johan Bjorck, Vishrav Chaudhary, Subhojit Som, Xia Song, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.14045)
[![citation](https://img.shields.io/badge/citation-261-blue.svg?paper=fbfef4723d8c8467d7bd523e1d0b703cce0e0f9c)](https://www.semanticscholar.org/paper/fbfef4723d8c8467d7bd523e1d0b703cce0e0f9c)



+ **COYO-700M: Image-Text Pair Dataset** (31 Aug 2022)\
[![Code](https://img.shields.io/github/stars/kakaobrain/coyo-dataset.svg?style=social&label=Star)](https://github.com/kakaobrain/coyo-dataset)


+ **LAION-5B: An open large-scale dataset for training next generation image-text models** (16 Oct 2022)<details><summary>[NeurIPS 2022] Christoph Schuhmann, Romain Beaumont, Richard Vencu, et al. </summary>Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine Crowson, Ludwig Schmidt, Robert Kaczmarczyk, Jenia Jitsev</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.08402)
[![citation](https://img.shields.io/badge/citation-1288-blue.svg?paper=e5c8960eb2ec034ffbd353ef39fd1cb541d3c7c9)](https://www.semanticscholar.org/paper/e5c8960eb2ec034ffbd353ef39fd1cb541d3c7c9)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://laion.ai/blog/laion-5b/)




+ **LAION COCO: 600M SYNTHETIC CAPTIONS FROM LAION2B-EN** (15 Sep 2022)<details><summary>Christoph Schuhmann, Andreas Köpf , Theo Coombes, et al.</summary>Christoph Schuhmann, Andreas Köpf , Theo Coombes, Richard Vencu, Benjamin Trom , Romain Beaumont</details>
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://laion.ai/blog/laion-coco/)


+ **[M3W] Flamingo: a Visual Language Model for Few-Shot Learning** (29 Apr 2022)<details><summary>[NeurIPS 2022] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, et al.</summary>Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2204.14198)
[![citation](https://img.shields.io/badge/citation-1483-blue.svg?paper=26218bdcc3945c7edae7aa2adbfba4cd820a2df3)](https://www.semanticscholar.org/paper/26218bdcc3945c7edae7aa2adbfba4cd820a2df3)




+ **[LAION-FACE]General Facial Representation Learning in a Visual-Linguistic Manner** (6 Dec 2021)<details><summary>[NeurIPS 2021] Yinglin Zheng, Hao Yang, Ting Zhang, et al.</summary>Yinglin Zheng, Hao Yang, Ting Zhang, Jianmin Bao, Dongdong Chen, Yangyu Huang, Lu Yuan, Dong Chen, Ming Zeng, Fang Wen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2112.03109)
[![citation](https://img.shields.io/badge/citation-70-blue.svg?paper=037bab9d26ef7da11ee32d7682836604d2cc8a72)](https://www.semanticscholar.org/paper/037bab9d26ef7da11ee32d7682836604d2cc8a72)
[![Code](https://img.shields.io/github/stars/FacePerceiver/FaRL.svg?style=social&label=Star)](https://github.com/FacePerceiver/FaRL)




+ **[LAION-400M] Open Dataset of CLIP-Filtered 400 Million Image-Text Pairs** (3 Nov 2021)<details><summary>[NeurIPS 2021] Christoph Schuhmann, Richard Vencu, Romain Beaumont, et al. </summary>Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, Aran Komatsuzaki</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2111.02114)
[![citation](https://img.shields.io/badge/citation-756-blue.svg?paper=b668ce936cff0b0ca8b635cd5f25a62eaf4eb3df)](https://www.semanticscholar.org/paper/b668ce936cff0b0ca8b635cd5f25a62eaf4eb3df)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://laion.ai/laion-400-open-dataset/)




+ **WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning** (2 Mar 2021)<details><summary>[SIGIR 2021] Krishna Srinivasan, Karthik Raman, Jiecao Chen, et al.</summary>Krishna Srinivasan, Karthik Raman, Jiecao Chen, Michael Bendersky, Marc Najork</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2103.01913)
[![citation](https://img.shields.io/badge/citation-186-blue.svg?paper=98e565fa06f6c7bf7c46833b5106b26dc45130c4)](https://www.semanticscholar.org/paper/98e565fa06f6c7bf7c46833b5106b26dc45130c4)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://github.com/google-research-datasets/wit)

+ **Conceptual 12M: Pushing Web-Scale Image-Text Pre-Training To Recognize Long-Tail Visual Concepts** (17 Feb 2021)<details><summary>[CVPR 2021] Soravit Changpinyo, Piyush Sharma, Nan Ding, et al.</summary>Soravit Changpinyo, Piyush Sharma, Nan Ding, Radu Soricut</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2102.08981)
[![citation](https://img.shields.io/badge/citation-617-blue.svg?paper=394be105b87e9bfe72c20efe6338de10604e1a11)](https://www.semanticscholar.org/paper/394be105b87e9bfe72c20efe6338de10604e1a11)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://github.com/google-research-datasets/conceptual-12m)


+ **[ALIGN] Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision** (11 Feb 2021)<details><summary>[ICML 2021] Chao Jia, Yinfei Yang, Ye Xia, et al. </summary>Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V. Le, Yunhsuan Sung, Zhen Li, Tom Duerig</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2102.05918)
[![citation](https://img.shields.io/badge/citation-2120-blue.svg?paper=141a5033d9994242b18bb3b217e79582f1ee9306)](https://www.semanticscholar.org/paper/141a5033d9994242b18bb3b217e79582f1ee9306)



+ **[MS COCO] Microsoft COCO: Common Objects in Context** (1 May 2014)<details><summary>[ECCV 2014] Tsung-Yi Lin, Michael Maire, Serge Belongie, et al. </summary>Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva Ramanan, C. Lawrence Zitnick, Piotr Dollár</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/1405.0312)
[![citation](https://img.shields.io/badge/citation-33630-blue.svg?paper=71b7178df5d2b112d07e45038cb5637208659ff7)](https://www.semanticscholar.org/paper/71b7178df5d2b112d07e45038cb5637208659ff7)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://cocodataset-org.translate.goog/?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN&_x_tr_pto=sc#home)



+ **[Im2Text] Describing Images Using 1 Million Captioned Photographs** (12 Dec 2011)\
[NeurIPS 2011] Vicente Ordonez, Girish Kulkarni, Tamara Berg\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://papers.nips.cc/paper_files/paper/2011/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html)
[![citation](https://img.shields.io/badge/citation-1192-blue.svg?paper=8e080b98efbe65c02a116439205ca2344b9f7cd4)](https://www.semanticscholar.org/paper/8e080b98efbe65c02a116439205ca2344b9f7cd4)



## Video Generation

### 🔅 LLM-based


+ **Loong: Generating Minute-level Long Videos with Autoregressive Language Models** (3 Oct 2024)<details><summary>Yuqing Wang, Tianwei Xiong, Daquan Zhou, et al.</summary>Yuqing Wang, Tianwei Xiong, Daquan Zhou, Zhijie Lin, Yang Zhao, Bingyi Kang, Jiashi Feng, Xihui Liu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.02757)
[![citation](https://img.shields.io/badge/citation-2-blue.svg?paper=1ac7fc5a55ce5843fb8a19d9f62b623e822bb7de)](https://www.semanticscholar.org/paper/Loong%3A-Generating-Minute-level-Long-Videos-with-Wang-Xiong/1ac7fc5a55ce5843fb8a19d9f62b623e822bb7de)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://epiphqny.github.io/Loong-video/)


+ **Compositional 3D-aware Video Generation with LLM Director** (31 Aug 2024)<details><summary>Hanxin Zhu, Tianyu He, Anni Tang, et al.</summary>Hanxin Zhu, Tianyu He, Anni Tang, Junliang Guo, Zhibo Chen, Jiang Bian</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2409.00558)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.microsoft.com/en-us/research/project/compositional-3d-aware-video-generation/)


+ **Anim-Director: A Large Multimodal Model Powered Agent for Controllable Animation Video Generation** (19 Aug 2024)<details><summary>[SIGGRAPH Asia 2024] Yunxin Li, Haoyuan Shi, Baotian Hu, et al.</summary>Yunxin Li, Haoyuan Shi, Baotian Hu, Longyue Wang, Jiashun Zhu, Jinyi Xu, Zhen Zhao, Min Zhang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.09787)
[![Code](https://img.shields.io/github/stars/HITsz-TMG/Anim-Director.svg?style=social&label=Star)](https://github.com/HITsz-TMG/Anim-Director?tab=readme-ov-file)

+ **[BSQ-ViT] Image and Video Tokenization with Binary Spherical Quantization** (11 Jun 2024)\
[Tech Report]Yue Zhao, Yuanjun Xiong, Philipp Krähenbühl\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.07548v1)  `tokenizer`


+ **DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation** (11 Mar 2024)<details><summary>Guosheng Zhao, Xiaofeng Wang, Zheng Zhu, et al.</summary>Guosheng Zhao, Xiaofeng Wang, Zheng Zhu, Xinze Chen, Guan Huang, Xiaoyi Bao, Xingang Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.06845)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=b34fb645165da381e27077282d69ff224dd2d5f5)](https://www.semanticscholar.org/paper/DriveDreamer-2%3A-LLM-Enhanced-World-Models-for-Video-Zhao-Wang/b34fb645165da381e27077282d69ff224dd2d5f5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://drivedreamer2.github.io/)


+ **[Sora] Video generation models as world simulators** (15 Feb 2024)<details><summary>Tim Brooks, Bill Peebles, Connor Holmes, et al.</summary>Tim Brooks and Bill Peebles and Connor Holmes and Will DePue and Yufei Guo and Li Jing and David Schnurr and Joe Taylor and Troy Luhman and Eric Luhman and Clarence Ng and Ricky Wang and Aditya Ramesh</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://openai.com/research/video-generation-models-as-world-simulators)


+ **[LWM] World Model on Million-Length Video And Language With Blockwise RingAttention** (13 Feb 2024)<details><summary>Hao Liu, Wilson Yan, Matei Zaharia, et al.</summary>Hao Liu, Wilson Yan, Matei Zaharia, Pieter Abbeel</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.08268)
[![citation](https://img.shields.io/badge/citation-38-blue.svg?paper=9259b476c31ba52b7e9ed059e5fbce2125092738)](https://www.semanticscholar.org/paper/World-Model-on-Million-Length-Video-And-Language-Liu-Yan/db7498f569be9852a04b2bb5bd68bd2885820bea)


+ **[LGVI] Towards Language-Driven Video Inpainting via Multimodal Large Language Models** (18 Jan 2024)<details><summary>Jianzong Wu, Xiangtai Li, Chenyang Si, et al.</summary>Jianzong Wu, Xiangtai Li, Chenyang Si, Shangchen Zhou, Jingkang Yang, Jiangning Zhang, Yining Li, Kai Chen, Yunhai Tong, Ziwei Liu, Chen Change Loy</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.10226)
[![citation](https://img.shields.io/badge/citation-3-blue.svg?paper=02d96eb0da4a282831f14923d1a65976952b7177)](https://www.semanticscholar.org/paper/Towards-Language-Driven-Video-Inpainting-via-Large-Wu-Li/02d96eb0da4a282831f14923d1a65976952b7177)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jianzongwu.github.io/projects/rovi/)

+ **Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization: Content-Consistent Multi-Scene Video Generation with LLM** (2 Jan 2024)<details><summary>Yang Jin, Zhicheng Sun, Kun Xu, et al.</summary>Yang Jin, Zhicheng Sun, Kun Xu, Kun Xu, Liwei Chen, Hao Jiang, Quzhe Huang, Chengru Song, Yuliang Liu, Di Zhang, Yang Song, Kun Gai, Yadong Mu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.03161)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=c1b5195bc09a2232ec2b69e5a2a6bd39b3162c62)](https://www.semanticscholar.org/paper/c1b5195bc09a2232ec2b69e5a2a6bd39b3162c62)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://video-lavit.github.io/)
`tokenizer`

+ **VideoDrafter: Content-Consistent Multi-Scene Video Generation with LLM** (2 Jan 2024)<details><summary>Fuchen Long, Zhaofan Qiu, Ting Yao, et al.</summary>Fuchen Long, Zhaofan Qiu, Ting Yao, Tao Mei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.01256)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=fc84fcf269a37ed7ddcb1b0f2d7d1a00f677eaea)](https://www.semanticscholar.org/paper/fc84fcf269a37ed7ddcb1b0f2d7d1a00f677eaea)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://videodrafter.github.io/)

+ **[PRO-Motion] Plan, Posture and Go: Towards Open-World Text-to-Motion Generation** (22 Dec 2023)<details><summary>Jinpeng Liu, Wenxun Dai, Chunyu Wang, et al.</summary>Jinpeng Liu, Wenxun Dai, Chunyu Wang, Yiji Cheng, Yansong Tang, Xin Tong</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.14828)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=4599d5af850da482f591a02a3b17d56e0d358771)](https://www.semanticscholar.org/paper/4599d5af850da482f591a02a3b17d56e0d358771)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://moonsliu.github.io/Pro-Motion/)

+ **VideoPoet: A Large Language Model for Zero-Shot Video Generation** (21 Dec 2023)<details><summary>Dan Kondratyuk, Lijun Yu, Xiuye Gu, et al.</summary>Dan Kondratyuk, Lijun Yu, Xiuye Gu, José Lezama, Jonathan Huang, Rachel Hornung, Hartwig Adam, Hassan Akbari, Yair Alon, Vighnesh Birodkar, Yong Cheng, Ming-Chang Chiu, Josh Dillon, Irfan Essa, Agrim Gupta, Meera Hahn, Anja Hauth, David Hendon, Alonso Martinez, David Minnen, David Ross, Grant Schindler, Mikhail Sirotenko, Kihyuk Sohn, Krishna Somandepalli, Huisheng Wang, Jimmy Yan, Ming-Hsuan Yang, Xuan Yang, Bryan Seybold, Lu Jiang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.14125)
[![citation](https://img.shields.io/badge/citation-18-blue.svg?paper=0c4f46e4dcae5527018e6432fb60cfe8c3354e97)](https://www.semanticscholar.org/paper/0c4f46e4dcae5527018e6432fb60cfe8c3354e97)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://sites.research.google/videopoet/)

+ **FlowZero: Zero-Shot Text-to-Video Synthesis with LLM-Driven Dynamic Scene Syntax** (27 Nov 2023)<details><summary>[arXiv 2023] Yu Lu, Linchao Zhu, Hehe Fan, et al.</summary>Yu Lu, Linchao Zhu, Hehe Fan, Yi Yang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.15813)
[![citation](https://img.shields.io/badge/citation-1-blue.svg?paper=9cdb7e415a96795dc6705e66f3b798238b4dec2c)](https://www.semanticscholar.org/paper/8feb33300c04fffa050e0dca59c3fdcafc920a3b)

+ **InterControl: Generate Human Motion Interactions by Controlling Every Joint** (27 Nov 2023)<details><summary>Zhenzhi Wang, Jingbo Wang, Dahua Lin, et al.</summary>Zhenzhi Wang, Jingbo Wang, Dahua Lin, Bo Dai</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.15864)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=9cdb7e415a96795dc6705e66f3b798238b4dec2c)](https://www.semanticscholar.org/paper/9cdb7e415a96795dc6705e66f3b798238b4dec2c)
[![Code](https://img.shields.io/github/stars/zhenzhiwang/intercontrol.svg?style=social&label=Star)](https://github.com/zhenzhiwang/intercontrol)\
Tags: `human motion generation`
+ **MotionLLM: Multimodal Motion-Language Learning with Large Language Models** (27 May 2024)<details><summary>Qi Wu, Yubo Zhao, Yifan Wang, et al.</summary>Qi Wu, Yubo Zhao, Yifan Wang, Yu-Wing Tai, Chi-Keung Tang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.17013)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=480da1ac2d39b5e036ce786af081366c23f08d1b)](https://www.semanticscholar.org/paper/480da1ac2d39b5e036ce786af081366c23f08d1b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://knoxzhao.github.io/MotionLLM/)\
Tags: `general human motion generation`
+ **GPT4Motion: Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning** (21 Nov 2023)<details><summary>Jiaxi Lv, Yi Huang, Mingfu Yan, et al.</summary>Jiaxi Lv, Yi Huang, Mingfu Yan, Jiancheng Huang, Jianzhuang Liu, Yifan Liu, Yafei Wen, Xiaoxin Chen, Shifeng Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.12631)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=9cdb7e415a96795dc6705e66f3b798238b4dec2c)](https://www.semanticscholar.org/paper/9cdb7e415a96795dc6705e66f3b798238b4dec2c)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://gpt4motion.github.io/)

+ **[LVD] LLM-grounded Video Diffusion Models** (29 Sep 2023)<details><summary>Long Lian, Baifeng Shi, Adam Yala, et al.</summary>Long Lian, Baifeng Shi, Adam Yala, Trevor Darrell, Boyi Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.17444)
[![citation](https://img.shields.io/badge/citation-10-blue.svg?paper=87bf66eb6d22df17f70170a0e575b4f12c4813ef)](https://www.semanticscholar.org/paper/87bf66eb6d22df17f70170a0e575b4f12c4813ef)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llm-grounded-video-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedVideoDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedVideoDiffusion)

+ **VideoDirectorGPT: Consistent Multi-scene Video Generation via LLM-Guided Planning** (26 Sep 2023)<details><summary>[arXiv 2023] Han Lin, Abhay Zala, Jaemin Cho, et al.</summary>Han Lin, Abhay Zala, Jaemin Cho, Mohit Bansal</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.15091)
[![citation](https://img.shields.io/badge/citation-12-blue.svg?paper=16753e0317730e8c1b297338300a8c6163dd06f2)](https://www.semanticscholar.org/paper/16753e0317730e8c1b297338300a8c6163dd06f2)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://videodirectorgpt.github.io/)
[![Code](https://img.shields.io/github/stars/HL-hanlin/VideoDirectorGPT.svg?style=social&label=Star)](https://github.com/HL-hanlin/VideoDirectorGPT)

+ **Free-Bloom: Zero-Shot Text-to-Video Generator with LLM Director and LDM Animator** (25 Sep 2023)<details><summary>[NIPS 2023] Hanzhuo Huang, Yufan Feng, Cheng Shi, et al.</summary>Hanzhuo Huang, Yufan Feng, Cheng Shi, Lan Xu, Jingyi Yu, Sibei Yang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.14494)
[![citation](https://img.shields.io/badge/citation-24-blue.svg?paper=120aca3e415b6641a0b0cd20695ab85ed7789612)](https://www.semanticscholar.org/paper/120aca3e415b6641a0b0cd20695ab85ed7789612)
[![Code](https://img.shields.io/github/stars/SooLab/Free-Bloom.svg?style=social&label=Star)](https://github.com/SooLab/Free-Bloom)

+ **[Dysen-VDM] Empowering Dynamics-aware Text-to-Video Diffusion with Large Language Models** (26 Aug 2023)<details><summary>[CVPR 2024] Hao Fei, Shengqiong Wu, Wei Ji, et al.</summary>Hao Fei, Shengqiong Wu, Wei Ji, Hanwang Zhang, Tat-Seng Chua</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.13812)
[![citation](https://img.shields.io/badge/citation-6-blue.svg?paper=d0a7f7fe31e0e0c42b471b4c47a313bd8c8e5206)](https://www.semanticscholar.org/paper/d0a7f7fe31e0e0c42b471b4c47a313bd8c8e5206)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](http://haofei.vip/Dysen-VDM/)
[![Code](https://img.shields.io/github/stars/scofield7419/Dysen.svg?style=social&label=Star)](https://github.com/scofield7419/Dysen)

+ **[DirecT2V] Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation** (23 May 2023)<details><summary>[arXiv 2023] Susung Hong, Junyoung Seo, Sunghwan Hong, et al.</summary>Susung Hong, Junyoung Seo, Sunghwan Hong, Heeseong Shin, Seungryong Kim</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.14330)
[![citation](https://img.shields.io/badge/citation-15-blue.svg?paper=b1750d2a6e3480e690999916a86c8b3876577b39)](https://www.semanticscholar.org/paper/b1750d2a6e3480e690999916a86c8b3876577b39)
[![Code](https://img.shields.io/github/stars/KU-CVLAB/DirecT2V.svg?style=social&label=Star)](https://github.com/KU-CVLAB/DirecT2V)

+ **Text2Motion: From Natural Language Instructions to Feasible Plans** (21 Mar 2023)<details><summary>[Autonomous Robots 2023] Kevin Lin, Christopher Agia, Toki Migimatsu, et al.</summary>Kevin Lin, Christopher Agia, Toki Migimatsu, Marco Pavone, Jeannette Bohg</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.12153)
[![citation](https://img.shields.io/badge/citation-110-blue.svg?paper=8f2d4758e6d525509ae36bb30224dc9259027e6b)](https://www.semanticscholar.org/paper/8f2d4758e6d525509ae36bb30224dc9259027e6b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://sites.google.com/stanford.edu/text2motion)
[![Code](https://img.shields.io/github/stars/KU-CVLAB/DirecT2V.svg?style=social&label=Star)](https://github.com/KU-CVLAB/DirecT2V)

### Non-LLM-based


+ **OSV: One Step is Enough for High-Quality Image to Video Generation** (17 Sep 2024)<details><summary>Xiaofeng Mao, Zhengkai Jiang, Fu-Yun Wang, et al.</summary>Xiaofeng Mao, Zhengkai Jiang, Fu-Yun Wang, Wenbing Zhu, Jiangning Zhang, Hao Chen, Mingmin Chi, Yabiao Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://www.arxiv.org/abs/2409.11367)

+ **[PAB] Real-Time Video Generation with Pyramid Attention Broadcast** (26 Jun 2024)<details><summary>Xuanlei Zhao, Xiaolong Jin, Kai Wang, et al.</summary>Xuanlei Zhao,  Xiaolong Jin,  Kai Wang,  Yang You</details>
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://oahzxl.github.io/PAB/)
[![Code](https://img.shields.io/github/stars/NUS-HPC-AI-Lab/OpenDiT.svg?style=social&label=Star)](https://github.com/NUS-HPC-AI-Lab/OpenDiT)



+ **Video-Infinity: Distributed Long Video Generation** (24 Jun 2024)<details><summary>Zhenxiong Tan, Xingyi Yang, Songhua Liu, et al.</summary>Zhenxiong Tan, Xingyi Yang, Songhua Liu, Xinchao Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.16260)




+ **Pandora: Towards General World Model with Natural Language Actions and Video** (12 Jun 2024)<details><summary>Jiannan Xiang, Guangyi Liu, Yi Gu, et al.</summary>Jiannan Xiang, Guangyi Liu, Yi Gu, Qiyue Gao, Yuting Ning, Yuheng Zha, Zeyu Feng, Tianhua Tao, Shibo Hao, Yemin Shi, Zhengzhong Liu, Eric P. Xing, Zhiting Hu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.09455)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://world-model.maitrix.org/)
[![Code](https://img.shields.io/github/stars/yhZhai/mcm.svg?style=social&label=Star)](https://github.com/maitrix-org/Pandora)



+ **Text-Animator: Controllable Visual Text Video Generation** (25 Jun 2024)<details><summary>Lin Liu, Quande Liu, Shengju Qian, et al.</summary>Lin Liu, Quande Liu, Shengju Qian, Yuan Zhou, Wengang Zhou, Houqiang Li, Lingxi Xie, Qi Tian</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.09455)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://laulampaul.github.io/text-animator.html)


+ **MotionBooth: Motion-Aware Customized Text-to-Video Generation** (25 Jun 2024)<details><summary>Jianzong Wu, Xiangtai Li, Yanhong Zeng, et al.</summary>Jianzong Wu, Xiangtai Li, Yanhong Zeng, Jiangning Zhang, Qianyu Zhou, Yining Li, Yunhai Tong, Kai Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.17758v1)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jianzongwu.github.io/projects/motionbooth/)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=7178bbc5e8d2d9b11c890c60486ba2cc2b79b784)](https://www.semanticscholar.org/paper/MotionBooth%3A-Motion-Aware-Customized-Text-to-Video-Wu-Li/7178bbc5e8d2d9b11c890c60486ba2cc2b79b784)

+ **FreeTraj: Tuning-Free Trajectory Control in Video Diffusion Models** (24 Jun 2024)<details><summary>Haonan Qiu, Zhaoxi Chen, Zhouxia Wang, et al.</summary>Haonan Qiu, Zhaoxi Chen, Zhouxia Wang, Yingqing He, Menghan Xia, Ziwei Liu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.16863)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](http://haonanqiu.com/projects/FreeTraj.html)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=1868d2c2f56a92044908a789049fdd44094fc8f2)](https://www.semanticscholar.org/paper/FreeTraj%3A-Tuning-Free-Trajectory-Control-in-Video-Qiu-Chen/1868d2c2f56a92044908a789049fdd44094fc8f2)
[![Code](https://img.shields.io/github/stars/arthur-qiu/FreeTraj.svg?style=social&label=Star)](https://github.com/arthur-qiu/FreeTraj)


+ **Identifying and Solving Conditional Image Leakage in Image-to-Video Diffusion Model** (22 Jun 2024)<details><summary>Min Zhao, Hongzhou Zhu, Chendong Xiang, et al.</summary>Min Zhao, Hongzhou Zhu, Chendong Xiang, Kaiwen Zheng, Chongxuan Li, Jun Zhu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.15735v1)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://cond-image-leak.github.io/)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=ebf4f746d24d79d61c070f8c354b3371f461aafb)](https://www.semanticscholar.org/paper/Identifying-and-Solving-Conditional-Image-Leakage-Zhao-Zhu/ebf4f746d24d79d61c070f8c354b3371f461aafb)
[![Code](https://img.shields.io/github/stars/thu-ml/cond-image-leakage.svg?style=social&label=Star)](https://github.com/thu-ml/cond-image-leakage/)


+ **Image Conductor: Precision Control for Interactive Video Synthesis** (21 Jun 2024)<details><summary>Yaowei Li, Xintao Wang, Zhaoyang Zhang, et al.</summary>Yaowei Li, Xintao Wang, Zhaoyang Zhang, Zhouxia Wang, Ziyang Yuan, Liangbin Xie, Yuexian Zou, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.15339)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://cond-image-leak.github.io/)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=b0bd64273dc8075db530fd696ee7eecb179bb908)](https://www.semanticscholar.org/paper/Image-Conductor%3A-Precision-Control-for-Interactive-Li-Wang/b0bd64273dc8075db530fd696ee7eecb179bb908)
[![Code](https://img.shields.io/github/stars/liyaowei-stu/ImageConductor.svg?style=social&label=Star)](https://github.com/liyaowei-stu/ImageConductor)


+ **VIDEOSCORE: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation** (21 Jun 2024)<details><summary>Xuan He, Dongfu Jiang, Ge Zhang, et al.</summary>Xuan He, Dongfu Jiang, Ge Zhang, Max Ku, Achint Soni, Sherman Siu, Haonan Chen, Abhranil Chandra, Ziyan Jiang, Aaran Arulraj, Kai Wang, Quy Duc Do, Yuansheng Ni, Bohan Lyu, Yaswanth Narsupalli, Rongqi Fan, Zhiheng Lyu, Yuchen Lin, Wenhu Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.15252)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://tiger-ai-lab.github.io/VideoScore/)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=1680eedc706ef081c0b103457bb52c071ab924b8)](https://www.semanticscholar.org/paper/VideoScore%3A-Building-Automatic-Metrics-to-Simulate-He-Jiang/1680eedc706ef081c0b103457bb52c071ab924b8)
[![Code](https://img.shields.io/github/stars/TIGER-AI-Lab/VideoScore/.svg?style=social&label=Star)](https://github.com/TIGER-AI-Lab/VideoScore/)


+ **Dreamitate: Real-World Visuomotor Policy Learning via Video Generation** (24 Jun 2024)<details><summary>Junbang Liang, Ruoshi Liu, Ege Ozguroglu, et al.</summary>Junbang Liang, Ruoshi Liu, Ege Ozguroglu, Sruthi Sudhakar, Achal Dave, Pavel Tokmakov, Shuran Song, Carl Vondrick</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.16862)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreamitate.cs.columbia.edu/)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=b0ac4f62f55bcf0427008e18f1b4b5bf7ee43df2)](https://www.semanticscholar.org/paper/Dreamitate%3A-Real-World-Visuomotor-Policy-Learning-Liang-Liu/b0ac4f62f55bcf0427008e18f1b4b5bf7ee43df2)




+ **[MCM] Motion Consistency Model: Accelerating Video Diffusion with Disentangled Motion-Appearance Distillation** (11 Jun 2024)<details><summary>Yuanhao Zhai, Kevin Lin, Zhengyuan Yang, et al.</summary>Yuanhao Zhai, Kevin Lin, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Chung-Ching Lin, David Doermann, Junsong Yuan, Lijuan Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.06890v1)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://yhzhai.github.io/mcm/)
[![Code](https://img.shields.io/github/stars/yhZhai/mcm.svg?style=social&label=Star)](https://github.com/yhZhai/mcm)


+ **Searching Priors Makes Text-to-Video Synthesis Better** (5 Jun 2024)<details><summary>Haoran Cheng, Liang Peng, Linxuan Xia, et al.</summary>Haoran Cheng, Liang Peng, Linxuan Xia, Yuepeng Hu, Hengjia Li, Qinglin Lu, Xiaofei He, Boxi Wu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.03215)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=0dd0e0bdff37973e102a042f82cd882b890476cc)](https://www.semanticscholar.org/paper/Searching-Priors-Makes-Text-to-Video-Synthesis-Cheng-Peng/0dd0e0bdff37973e102a042f82cd882b890476cc)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://hrcheng98.github.io/Search_T2V/)

+ **ZeroSmooth: Training-free Diffuser Adaptation for High Frame Rate Video Generation** (3 Jun 2024)<details><summary>Shaoshu Yang, Yong Zhang, Xiaodong Cun, et al.</summary>Shaoshu Yang, Yong Zhang, Xiaodong Cun, Ying Shan, Ran He</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.00908v1)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=2917706886df4e3bf57acd0b41bd4e396be77506)](https://www.semanticscholar.org/paper/ZeroSmooth%3A-Training-free-Diffuser-Adaptation-for-Yang-Zhang/2917706886df4e3bf57acd0b41bd4e396be77506#cited-papers)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ssyang2020.github.io/zerosmooth.github.io/)


+ **EasyAnimate: A High-Performance Long Video Generation Method based on Transformer Architecture** (30 May 2024)<details><summary>Sijie Zhao, Yong Zhang, Xiaodong Cun, et al.</summary>Sijie Zhao, Yong Zhang, Xiaodong Cun, Shaoshu Yang, Muyao Niu, Xiaoyu Li, Wenbo Hu, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.20279)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=70569a07d841f86faf8914aea435a1696f911a32)](https://www.semanticscholar.org/paper/CV-VAE%3A-A-Compatible-Video-VAE-for-Latent-Video-Zhao-Zhang/70569a07d841f86faf8914aea435a1696f911a32)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/cvvae/index.html)
[![Code](https://img.shields.io/github/stars/AILab-CVC/CV-VAE.svg?style=social&label=Star)](https://github.com/AILab-CVC/CV-VAE)

+ **[MOFT] Video Diffusion Models are Training-free Motion Interpreter and Controller** (23 Mar 2024)<details><summary>Zeqi Xiao, Yifan Zhou, Shuai Yang, et al.</summary>Zeqi Xiao, Yifan Zhou, Shuai Yang, Xingang Pan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.14864)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=4f3e62c0fea3dc43f345e775192c972760b9d113)](https://www.semanticscholar.org/paper/Video-Diffusion-Models-are-Training-free-Motion-and-Xiao-Zhou/4f3e62c0fea3dc43f345e775192c972760b9d113)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://xizaoqu.github.io/moft/)

+ **StreamingT2V: Consistent, Dynamic, and Extendable Long Video Generation from Text** (21 Mar 2024)<details><summary>Roberto Henschel, Levon Khachatryan, Daniil Hayrapetyan, et al.</summary>Roberto Henschel, Levon Khachatryan, Daniil Hayrapetyan, Hayk Poghosyan, Vahram Tadevosyan, Zhangyang Wang, Shant Navasardyan, Humphrey Shi</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2403.14773)
[![citation](https://img.shields.io/badge/citation-0-blue.svg?paper=21a77ed349c8621d0a0ef8407eb744e3de3b13c5)](https://www.semanticscholar.org/paper/StreamingT2V%3A-Consistent%2C-Dynamic%2C-and-Extendable-Henschel-Khachatryan/21a77ed349c8621d0a0ef8407eb744e3de3b13c5)
[![Code](https://img.shields.io/github/stars/Picsart-AI-Research/StreamingT2V.svg?style=social&label=Star)](https://github.com/Picsart-AI-Research/StreamingT2V)

+ **Snap Video: Scaled Spatiotemporal Transformers for Text-to-Video Synthesis** (22 Feb 2024)<details><summary>Willi Menapace, Aliaksandr Siarohin, Ivan Skorokhodov, et al.</summary>Willi Menapace, Aliaksandr Siarohin, Ivan Skorokhodov, Ekaterina Deyneka, Tsai-Shien Chen, Anil Kag, Yuwei Fang, Aleksei Stoliar, Elisa Ricci, Jian Ren, Sergey Tulyakov</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2402.14797)
[![citation](https://img.shields.io/badge/citation-7-blue.svg?paper=97cb2eb0d0517e34bf4202f0593600bb6fa043cd)](https://www.semanticscholar.org/paper/Snap-Video%3A-Scaled-Spatiotemporal-Transformers-for-Menapace-Siarohin/97cb2eb0d0517e34bf4202f0593600bb6fa043cd)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://snap-research.github.io/snapvideo/)

+ **VideoCrafter2: Overcoming Data Limitations for High-Quality Video Diffusion Models** (17 Jan 2024)<details><summary>Haoxin Chen, Yong Zhang, Xiaodong Cun, et al.</summary>Haoxin Chen, Yong Zhang, Xiaodong Cun, Menghan Xia, Xintao Wang, Chao Weng, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.09047)
[![citation](https://img.shields.io/badge/citation-7-blue.svg?paper=492bc8339d8aac442c4ec13f8c1d59e980a3af2f)](https://www.semanticscholar.org/paper/VideoCrafter2%3A-Overcoming-Data-Limitations-for-Chen-Zhang/492bc8339d8aac442c4ec13f8c1d59e980a3af2f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/videocrafter2/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/VideoCrafter.svg?style=social&label=Star)](https://github.com/AILab-CVC/VideoCrafter)


+ **Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets** (25 Nov 2023)<details><summary>Andreas Blattmann, Tim Dockhorn, Sumith Kulal, et al.</summary>Andreas Blattmann, Tim Dockhorn, Sumith Kulal, Daniel Mendelevitch, Maciej Kilian, Dominik Lorenz, Yam Levi, Zion English, Vikram Voleti, Adam Letts, Varun Jampani, Robin Rombach</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.15127)
[![citation](https://img.shields.io/badge/citation-51-blue.svg?paper=1206b05eae5a06ba662ae79fb291b50e359c4f42)](https://www.semanticscholar.org/paper/1206b05eae5a06ba662ae79fb291b50e359c4f42)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://stability.ai/research/stable-video-diffusion-scaling-latent-video-diffusion-models-to-large-datasets)
[![Code](https://img.shields.io/github/stars/Stability-AI/generative-models.svg?style=social&label=Star)](https://github.com/Stability-AI/generative-models)

+ **VideoCrafter1: Open Diffusion Models for High-Quality Video Generation** (30 Oct 2023)<details><summary>Haoxin Chen, Menghan Xia, Yingqing He, et al.</summary>Haoxin Chen, Menghan Xia, Yingqing He, Yong Zhang, Xiaodong Cun, Shaoshu Yang, Jinbo Xing, Yaofang Liu, Qifeng Chen, Xintao Wang, Chao Weng, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.19512)
[![citation](https://img.shields.io/badge/citation-38-blue.svg?paper=1891c3756f870d902a0b793a1dcd5cc34c778612)](https://www.semanticscholar.org/paper/1891c3756f870d902a0b793a1dcd5cc34c778612)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/videocrafter/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/VideoCrafter.svg?style=social&label=Star)](https://github.com/AILab-CVC/VideoCrafter)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggi