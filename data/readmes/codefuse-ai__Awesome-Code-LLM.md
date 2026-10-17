# Awesome-Code-LLM

<p align='center'>
<img src='imgs/wordcloud.png' style='width: 100%; '>
</p>

This is the repo for our TMLR [code LLM survey](https://arxiv.org/abs/2311.07989). If you find this repo helpful, please support us by citing:

```
@article{zhang2024unifying,
   title={Unifying the Perspectives of {NLP} and Software Engineering: A Survey on Language Models for Code},
   author={Ziyin Zhang and Chaoyu Chen and Bingchang Liu and Cong Liao and Zi Gong and Hang Yu and Jianguo Li and Rui Wang},
   journal={Transactions on Machine Learning Research},
   issn={2835-8856},
   year={2024},
   url={https://openreview.net/forum?id=hkNnGqZnpa}
}
```

## News

🔥🔥🔥 [2026/05/20] Featured papers:

- 🔥🔥 [Beyond Retrieval: A Multitask Benchmark and Model for Code Search](https://arxiv.org/abs/2605.04615) from Ant Group.

- 🔥 [Composer 2 Technical Report](https://arxiv.org/abs/2603.24477) from Cursor Research Team.

🔥🔥&nbsp;&nbsp;&nbsp;&nbsp; [2025/12/04] 67 papers from EMNLP 2025 have been added. Search for the keyword "EMNLP 2025"!

🔥&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [2024/09/06] Our survey has been accepted for publication by Transactions on Machine Learning Research (TMLR).

🔥🔥🔥 [2026/05/20] News from Codefuse

- We released [CoREB](https://arxiv.org/abs/2605.04615), a comprehensive code search benchmark covering two stages (retrieval, reranking), three tasks (text2code, code2text, code2code), and five languages. [[data](https://github.com/hq-bench/coreb)] [[model & data](https://huggingface.co/collections/hq-bench/beyond-retrieval)]

- Our paper [ML-Embed](https://arxiv.org/abs/2605.15081) is accepted to ICML 2026. [[code](https://github.com/codefuse-ai/CodeFuse-Embeddings)] [[model & data](https://huggingface.co/collections/codefuse-ai/codefuse-embeddings)]

- We released [F2LLM-v2](https://arxiv.org/abs/2603.19223), a family of frontier multilingual emebedding models that sets new state-of-the-art on at least 11 MTEB benchmarks. [[code](https://github.com/codefuse-ai/CodeFuse-Embeddings)] [[model & data](https://huggingface.co/collections/codefuse-ai/f2llm)]

- We are launching a new awesome project about embedding models: [Awesome-Omnimodal-Embeddings](https://github.com/codefuse-ai/Awesome-Omnimodal-Embeddings)

- We released [C2LLM](https://arxiv.org/abs/2512.21332), a family of state-of-the-art code embedding models in 0.5B and 7B sizes. C2LLM-7B ranks first on MTEB-Code leaderboard. [[code](https://github.com/codefuse-ai/CodeFuse-Embeddings)] [[model](https://huggingface.co/collections/codefuse-ai/codefuse-embeddings-68d4b32da791bbba993f8d14)]

#### How to Contribute

If you find a paper to be missing from this repository, misplaced in a category, or lacking a reference to its journal/conference information, please do not hesitate to create an issue.

## Table of Contents

1. [Surveys](#1-surveys)

2. [Models](#2-models)

   2.1 [Base LLMs and Pretraining Strategies](#21-base-llms-and-pretraining-strategies)

   2.2 [Existing LLM Adapted to Code](#22-existing-llm-adapted-to-code)

   2.3 [General Pretraining on Code](#23-general-pretraining-on-code)
   - [Encoder](#encoder)
   - [Decoder](#decoder)
   - [Encoder-Decoder](#encoder-decoder)
   - [UniLM](#unilm)
   - [Other Models](#other-models)

   <!-- prettier ignore -->

   2.4 [(Instruction) Fine-Tuning on Code](#24-instruction-fine-tuning-on-code)

   2.5 [Reinforcement Learning on Code](#25-reinforcement-learning-on-code)

3. [When Coding Meets Reasoning](#3-when-coding-meets-reasoning)

   3.1 [Coding for Reasoning](#31-coding-for-reasoning)

   3.2 [Code Simulation](#32-code-simulation)

   3.3 [Code Agents](#33-code-agents)

   3.4 [Interactive Coding](#34-interactive-coding)

   3.5 [Frontend Navigation](#35-frontend-navigation)

4. [Code LLM for Low-Resource, Low-Level, and Domain-Specific Languages](#4-code-llm-for-low-resource-low-level-and-domain-specific-languages)

5. [Methods/Models for Downstream Tasks](#5-methodsmodels-for-downstream-tasks)
   - Programming
     - [Code Generation](#code-generation)
     - [Code RAG](#code-rag)
     - [Code Ranking](#code-ranking)
     - [Code Translation](#code-translation)
     - [Code Commenting and Summarization](#code-commenting-and-summarization)
     - [Program Repair](#program-repair)
     - [Code Similarity and Embedding (Clone Detection, Code Search)](#code-similarity-and-embedding-clone-detection-code-search)
     - [Code Refactoring and Migration](#code-refactoring-and-migration)
     - [Type Prediction](#type-prediction)
     - [Repository-Level Coding](#repository-level-coding)
     - [Issue Resolution](#issue-resolution)
     - [Frontend Development](#frontend-development)
     - [Automated Machine Learning](#automated-machine-learning)
     - [Text-To-SQL](#text-to-sql)
     - [Program Proof](#program-proof)

   - Testing and Deployment
     - [Test Generation](#test-generation)
     - [Oracle Generation](#oracle-generation)
     - [Mutation Testing](#mutation-testing)
     - [Fuzz Testing](#fuzz-testing)
     - [Vulnerability Detection](#vulnerability-detection)
     - [Malicious Code Detection](#malicious-code-detection)
     - [Compiler Optimization](#compiler-optimization)
     - [Binary Analysis and Decompilation](#binary-analysis-and-decompilation)

   - DevOps
     - [Commit Message Generation](#commit-message-generation)
     - [Code Review](#code-review)
     - [Log Analysis](#log-analysis)
     - [Software Configuration](#software-configuration)
     - [Code QA & Reasoning](#code-qa--reasoning)

   - Requirement
     - [Software Modeling](#software-modeling)
     - [Requirement Engineering](#requirement-engineering)

6. [Analysis of AI-Generated Code](#6-analysis-of-ai-generated-code)
   - [Security and Vulnerabilities](#security-and-vulnerabilities)
   - [Correctness](#correctness)
   - [Hallucination](#hallucination)
   - [Efficiency](#efficiency)
   - [Robustness](#robustness)
   - [Interpretability](#interpretability)
   - [API Usage](#api-usage)
   - [Privacy](#privacy)
   - [Bias](#bias)
   - [Contamination](#contamination)
   - [AI-Generated Code Detection](#ai-generated-code-detection)
   - [Others](#others)

7. [Human-LLM Interaction](#7-human-llm-interaction)

8. [Datasets](#8-datasets)

   8.1 [Pretraining](#81-pretraining)

   8.2 [Benchmarks](#82-benchmarks)
   - [Integrated Benchmarks](#integrated-benchmarks)
   - [Evaluation Metrics](#evaluation-metrics)
   - [Program Synthesis](#program-synthesis)
   - [Visually Grounded Program Synthesis](#visually-grounded-program-synthesis)
   - [Code Reasoning and QA](#code-reasoning-and-qa)
   - [Text-to-SQL](#text-to-sql-1)
   - [Code Translation](#code-translation-1)
   - [Program Repair](#program-repair-1)
   - [Code Summarization](#code-summarization)
   - [Defect/Vulnerability Detection](#defectvulnerability-detection)
   - [Code Retrieval](#code-retrieval)
   - [Type Inference](#type-inference)
   - [Commit Message Generation](#commit-message-generation-1)
   - [Repo-Level Coding](#repo-level-coding)

9. [Recommended Readings](#9-recommended-readings)

10. [Other Awesome LLM Reading Lists](#other-awesome-llm-reading-lists)

11. [Citation](#citation)

12. [Star History](#star-history)

13. [Join Us](#join-us)

## 1. Surveys

1. "Large Language Models Meet NL2Code: A Survey" [2022-12] [ACL 2023] [[paper](https://arxiv.org/abs/2212.09420)]

2. "A Survey on Pretrained Language Models for Neural Code Intelligence" [2022-12] [[paper](https://arxiv.org/abs/2212.10079)]

3. "An Empirical Comparison of Pre-Trained Models of Source Code" [2023-02] [ICSE 2023] [[paper](https://arxiv.org/abs/2302.04026)]

4. "Large Language Models for Software Engineering: A Systematic Literature Review" [2023-08] [[paper](https://arxiv.org/abs/2308.10620)]

5. "Towards an Understanding of Large Language Models in Software Engineering Tasks" [2023-08] [[paper](https://arxiv.org/abs/2308.11396)]

6. "Pitfalls in Language Models for Code Intelligence: A Taxonomy and Survey" [2023-10] [[paper](https://arxiv.org/abs/2310.17903)]

7. "A Survey on Large Language Models for Software Engineering" [2023-12] [[paper](https://arxiv.org/abs/2312.15223)]

8. "Deep Learning for Code Intelligence: Survey, Benchmark and Toolkit" [2023-12] [[paper](https://arxiv.org/abs/2401.00288)]

9. "A Survey of Neural Code Intelligence: Paradigms, Advances and Beyond" [2024-03] [[paper](https://arxiv.org/abs/2403.14734)]

10. "Tasks People Prompt: A Taxonomy of LLM Downstream Tasks in Software Verification and Falsification Approaches" [2024-04] [[paper](https://arxiv.org/abs/2404.09384)]

11. "Automatic Programming: Large Language Models and Beyond" [2024-05] [[paper](https://arxiv.org/abs/2405.02213)]

12. "Software Engineering and Foundation Models: Insights from Industry Blogs Using a Jury of Foundation Models" [2024-10] [[paper](https://arxiv.org/abs/2410.09012)]

13. "Deep Learning-based Software Engineering: Progress, Challenges, and Opportunities" [2024-10] [[paper](https://arxiv.org/abs/2410.13110)]

14. "Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets" [2025-03] [[paper](https://arxiv.org/abs/2503.17502)]

15. "Challenges and Paths Towards AI for Software Engineering" [2025-03] [[paper](https://arxiv.org/abs/2503.22625)]

16. "Software Development Life Cycle Perspective: A Survey of Benchmarks for CodeLLMs and Agents" [2025-05] [[paper](https://arxiv.org/abs/2505.05283)]

17. "From Code Foundation Models to Agents and Applications: A Practical Guide to Code Intelligence" [2025-11] [[paper](https://arxiv.org/abs/2511.18538)]

## 2. Models

<p align='center'>
<img src='imgs/overview.png' style='width: 80%; '>
</p>

### 2.1 Base LLMs and Pretraining Strategies

These LLMs are not specifically trained for code, but have demonstrated varying coding capability.

1. **LaMDA**: "LaMDA: Language Models for Dialog Applications" [2022-01] [[paper](https://arxiv.org/abs/2201.08239)]

2. **PaLM**: "PaLM: Scaling Language Modeling with Pathways" [2022-04] [JMLR] [[paper](https://arxiv.org/abs/2204.02311)]

3. **GPT-NeoX**: "GPT-NeoX-20B: An Open-Source Autoregressive Language Model" [2022-04] [ACL 2022 Workshop on Challenges & Perspectives in Creating LLMs] [[paper](https://arxiv.org/abs/2204.06745)] [[repo](https://github.com/EleutherAI/gpt-neox)]

4. **BLOOM**: "BLOOM: A 176B-Parameter Open-Access Multilingual Language Model" [2022-11] [[paper](https://arxiv.org/abs/2211.05100)] [[model](https://huggingface.co/models?search=bigscience/bloom)]

5. **LLaMA**: "LLaMA: Open and Efficient Foundation Language Models" [2023-02] [[paper](https://arxiv.org/abs/2302.13971)]

6. **GPT-4**: "GPT-4 Technical Report" [2023-03] [[paper](https://arxiv.org/abs/2303.08774)]

7. **LLaMA 2**: "Llama 2: Open Foundation and Fine-Tuned Chat Models" [2023-07] [[paper](https://arxiv.org/abs/2307.09288)] [[repo](https://github.com/facebookresearch/llama)]

8. **Phi-1.5**: "Textbooks Are All You Need II: phi-1.5 technical report" [2023-09] [[paper](https://arxiv.org/abs/2309.05463)] [[model](https://huggingface.co/microsoft/phi-1_5)]

9. **Baichuan 2**: "Baichuan 2: Open Large-scale Language Models" [2023-09] [[paper](https://arxiv.org/abs/2309.10305)] [[repo](https://github.com/baichuan-inc/Baichuan2)]

10. **Qwen**: "Qwen Technical Report" [2023-09] [[paper](https://arxiv.org/abs/2309.16609)] [[repo](https://github.com/QwenLM/Qwen)]

11. **Mistral**: "Mistral 7B" [2023-10] [[paper](https://arxiv.org/abs/2310.06825)] [[repo](https://github.com/mistralai/mistral-src)]

12. **Gemini**: "Gemini: A Family of Highly Capable Multimodal Models" [2023-12] [[paper](https://arxiv.org/abs/2312.11805)]

13. **Phi-2**: "Phi-2: The surprising power of small language models" [2023-12] [[blog](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)]

14. **YAYI2**: "YAYI 2: Multilingual Open-Source Large Language Models" [2023-12] [[paper](https://arxiv.org/abs/2312.14862)] [[repo](https://github.com/wenge-research/YAYI2)]

15. **DeepSeek**: "DeepSeek LLM: Scaling Open-Source Language Models with Longtermism" [2024-01] [[paper](https://arxiv.org/abs/2401.02954)] [[repo](https://github.com/deepseek-ai/DeepSeek-LLM)]

16. **Mixtral**: "Mixtral of Experts" [2024-01] [[paper](https://arxiv.org/abs/2401.04088)] [[blog](https://mistral.ai/news/mixtral-of-experts/)]

17. **DeepSeekMoE**: "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models" [2024-01] [[paper](https://arxiv.org/abs/2401.12246)] [[repo](https://github.com/deepseek-ai/DeepSeek-MoE)]

18. **Orion**: "Orion-14B: Open-source Multilingual Large Language Models" [2024-01] [[paper](https://arxiv.org/abs/2401.06066)] [[repo](https://github.com/OrionStarAI/Orion)]

19. **OLMo**: "OLMo: Accelerating the Science of Language Models" [2024-02] [[paper](https://arxiv.org/abs/2402.00838)] [[repo](https://github.com/allenai/OLMo)]

20. **Gemma**: "Gemma: Open Models Based on Gemini Research and Technology" [2024-02] [[paper](https://storage.googleapis.com/deepmind-media/gemma/gemma-report.pdf)] [[blog](https://blog.google/technology/developers/gemma-open-models/)]

21. **Claude 3**: "The Claude 3 Model Family: Opus, Sonnet, Haiku" [2024-03] [[paper](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)] [[blog](https://www.anthropic.com/news/claude-3-family)]

22. **Yi**: "Yi: Open Foundation Models by 01.AI" [2024-03] [[paper](https://arxiv.org/abs/2403.04652)] [[repo](https://github.com/01-ai/Yi)]

23. **Poro**: "Poro 34B and the Blessing of Multilinguality" [2024-04] [[paper](https://arxiv.org/abs/2404.01856)] [[model](https://huggingface.co/LumiOpen/Poro-34B)]

24. **JetMoE**: "JetMoE: Reaching Llama2 Performance with 0.1M Dollars" [2024-04] [[paper](https://arxiv.org/abs/2404.07413)] [[repo](https://github.com/myshell-ai/JetMoE)]

25. **LLaMA 3**: "The Llama 3 Herd of Models" [2024-04] [[blog](https://ai.meta.com/blog/meta-llama-3/)] [[repo](https://github.com/meta-llama/llama3)] [[paper](https://arxiv.org/abs/2407.21783)]

26. **Reka Core**: "Reka Core, Flash, and Edge: A Series of Powerful Multimodal Language Models" [2024-04] [[paper](https://arxiv.org/abs/2404.12387)]

27. **Phi-3**: "Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone" [2024-04] [[paper](https://arxiv.org/abs/2404.14219)]

28. **OpenELM**: "OpenELM: An Efficient Language Model Family with Open-source Training and Inference Framework" [2024-04] [[paper](https://arxiv.org/abs/2404.14619)] [[repo](https://github.com/apple/corenet/tree/main/projects/openelm)]

29. **Tele-FLM**: "Tele-FLM Technical Report" [2024-04] [[paper](https://arxiv.org/abs/2404.16645)] [[model](https://huggingface.co/CofeAI/Tele-FLM)]

30. **DeepSeek-V2**: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model" [2024-05] [[paper](https://arxiv.org/abs/2405.04434)] [[repo](https://github.com/deepseek-ai/DeepSeek-V2)]

31. **GECKO**: "GECKO: Generative Language Model for English, Code and Korean" [2024-05] [[paper](https://arxiv.org/abs/2405.15640)] [[model](https://huggingface.co/kifai/GECKO-7B)]

32. **MAP-Neo**: "MAP-Neo: Highly Capable and Transparent Bilingual Large Language Model Series" [2024-05] [[paper](https://arxiv.org/abs/2405.19327)] [[repo](https://github.com/multimodal-art-projection/MAP-NEO)]

33. **Zyda**: "Zyda: A 1.3T Dataset for Open Language Modeling" [2024-06] [[paper](https://arxiv.org/abs/2406.01981)]

34. **Skywork-MoE**: "Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models" [2024-06] [[paper](https://arxiv.org/abs/2406.06563)]

35. **Xmodel-LM**: "Xmodel-LM Technical Report" [2024-06] [[paper](https://arxiv.org/abs/2406.02856)]

36. **GEB**: "GEB-1.3B: Open Lightweight Large Language Model" [2024-06] [[paper](https://arxiv.org/abs/2406.09900)]

37. **HARE**: "HARE: HumAn pRiors, a key to small language model Efficiency" [2024-06] [[paper](https://arxiv.org/abs/2406.11410)]

38. **DCLM**: "DataComp-LM: In search of the next generation of training sets for language models" [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]

39. **Nemotron-4**: "Nemotron-4 340B Technical Report" [2024-06] [[paper](https://arxiv.org/abs/2406.11704)]

40. **ChatGLM**: "ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools" [2024-06] [[paper](https://arxiv.org/abs/2406.12793)]

41. **FineWeb**: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" [2024-06] [[paper](https://arxiv.org/abs/2406.17557)]

42. **YuLan**: "YuLan: An Open-source Large Language Model" [2024-06] [[paper](https://arxiv.org/abs/2406.19853)]

43. **Gemma 2**: "Gemma 2: Improving Open Language Models at a Practical Size" [2024-06] [[paper](https://storage.googleapis.com/deepmind-media/gemma/gemma-2-report.pdf)]

44. **H2O-Danube3**: "H2O-Danube3 Technical Report" [2024-07] [[paper](https://arxiv.org/abs/2407.09276)]

45. **Qwen2**: "Qwen2 Technical Report" [2024-07] [[paper](https://arxiv.org/abs/2407.10671)]

46. **ALLaM**: "ALLaM: Large Language Models for Arabic and English" [2024-07] [[paper](https://arxiv.org/abs/2407.15390)]

47. **SeaLLMs 3**: "SeaLLMs 3: Open Foundation and Chat Multilingual Large Language Models for Southeast Asian Languages" [2024-07] [[paper](https://arxiv.org/abs/2407.19672)]

48. **AFM**: "Apple Intelligence Foundation Language Models" [2024-07] [[paper](https://arxiv.org/abs/2407.21075)]

49. "To Code, or Not To Code? Exploring Impact of Code in Pre-training" [2024-08] [ICLR 2025] [[paper](https://arxiv.org/abs/2408.10914)]

50. **OLMoE**: "OLMoE: Open Mixture-of-Experts Language Models" [2024-09] [[paper](https://arxiv.org/abs/2409.02060)]

51. "How Does Code Pretraining Affect Language Model Task Performance?" [2024-09] [[paper](https://arxiv.org/abs/2409.04556)]

52. **EuroLLM**: "EuroLLM: Multilingual Language Models for Europe" [2024-09] [[paper](https://arxiv.org/abs/2409.16235)]

53. "Which Programming Language and What Features at Pre-training Stage Affect Downstream Logical Inference Performance?" [2024-10] [EMNLP 2024] [[paper](https://arxiv.org/abs/2410.06735)]

54. **GPT-4o**: "GPT-4o System Card" [2024-10] [[paper](https://arxiv.org/abs/2410.21276)]

55. **Hunyuan-Large**: "Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent" [2024-11] [[paper](https://arxiv.org/abs/2411.02265)]

56. **Crystal**: "Crystal: Illuminating LLM Abilities on Language and Code" [2024-11] [[paper](https://arxiv.org/abs/2411.04156)]

57. **Zyda-2**: "Zyda-2: a 5 Trillion Token High-Quality Dataset" [2024-11] [[paper](https://arxiv.org/abs/2411.06068)]

58. **Xmodel-1.5**: "Xmodel-1.5: An 1B-scale Multilingual LLM" [2024-11] [[paper](https://arxiv.org/abs/2411.10083)]

59. **Yi-Lightning**: "Yi-Lightning Technical Report" [2024-12] [[paper](https://arxiv.org/abs/2412.01253)]

60. "RedStone: Curating General, Code, Math, and QA Data for Large Language Models" [2024-12] [[paper](https://arxiv.org/abs/2412.03398)]

61. **EXAONE 3.5**: "EXAONE 3.5: Series of Large Language Models for Real-world Use Cases" [2024-12] [[paper](https://arxiv.org/abs/2412.04862)]

62. "The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model" [2024-12] [ICLR 2025] [[paper](https://arxiv.org/abs/2412.07298)]

63. **Phi-4**: "Phi-4 Technical Report" [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]

64. **Typhoon 2**: "Typhoon 2: A Family of Open Text and Multimodal Thai Large Language Models" [2024-12] [[paper](https://arxiv.org/abs/2412.13702)]

65. **Qwen2.5**: "Qwen2.5 Technical Report" [2024-12] [[paper](https://arxiv.org/abs/2412.15115)]

66. **YuLan-Mini**: "YuLan-Mini: An Open Data-efficient Language Model" [2024-12] [[paper](https://arxiv.org/abs/2412.17743)]

67. **DeepSeek-V3**: "DeepSeek-V3 Technical Report" [2024-12] [[paper](https://arxiv.org/abs/2412.19437)]

68. **OLMo 2**: "2 OLMo 2 Furious" [2024-12] [[paper](https://arxiv.org/abs/2501.00656)]

69. **FinerWeb**: "FinerWeb-10BT: Refining Web Data with LLM-Based Line-Level Filtering" [2025-01] [[paper](https://arxiv.org/abs/2501.07314)]

70. **MiniMax-01**: "MiniMax-01: Scaling Foundation Models with Lightning Attention" [2025-01] [[paper](https://arxiv.org/abs/2501.08313)]

71. **SmolLM2**: "SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model" [2025-02] [[paper](https://arxiv.org/abs/2502.02737)]

72. **Salamandra**: "Salamandra Technical Report" [2025-02] [[paper](https://arxiv.org/abs/2502.08489)]

73. **Kanana**: "Kanana: Compute-efficient Bilingual Language Models" [2025-02] [[paper](https://arxiv.org/abs/2502.18934)]

74. **Phi-4-Mini**: "Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs" [2025-03] [[paper](https://arxiv.org/abs/2503.01743)]

75. **Ling**: "Every FLOP Counts: Scaling a 300B Mixture-of-Experts LING LLM without Premium GPUs" [2025-03] [[paper](https://arxiv.org/abs/2503.05139)]

76. **Gemma 3**: "Gemma 3 Technical Report" [2025-03] [[paper](https://arxiv.org/abs/2503.19786)]

77. **Command A**: "Command A: An Enterprise-Ready Large Language Model" [2025-04] [[paper](https://arxiv.org/abs/2504.00698)]

78. **Llama-Nemotron**: "Llama-Nemotron: Efficient Reasoning Models" [2025-05] [[paper](https://arxiv.org/abs/2505.00949)]

79. **MiMo**: "MiMo: Unlocking the Reasoning Potential of Language Model -- From Pretraining to Posttraining" [2025-05] [[paper](https://arxiv.org/abs/2505.07608)]

80. **xGen-small**: "xGen-small Technical Report" [2025-05] [[paper](https://arxiv.org/abs/2505.06496)]

81. **Qwen3**: "Qwen3 Technical Report" [2025-05] [[paper](https://arxiv.org/abs/2505.09388)]

82. **Hunyuan-TurboS**: "Hunyuan-TurboS: Advancing Large Language Models through Mamba-Transformer Synergy and Adaptive Chain-of-Thought" [2025-05] [[paper](https://arxiv.org/abs/2505.15431)]

83. **EuroLLM-9B**: "EuroLLM-9B: Technical Report" [2025-06] [[paper](https://arxiv.org/abs/2506.04079)]

84. **Gemini 2.5**: "Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities" [2025-07] [[paper](https://arxiv.org/abs/2507.06261)]

85. **EXAONE 4.0**: "EXAONE 4.0: Unified Large Language Models Integrating Non-reasoning and Reasoning Modes" [2025-07] [[paper](https://arxiv.org/abs/2507.11407)]

86. **TeleChat2**: "Technical Report of TeleChat2, TeleChat2.5 and T1" [2025-07] [[paper](https://arxiv.org/abs/2507.18013)]

87. **Kimi K2**: "Kimi K2: Open Agentic Intelligence" [2025-07] [[paper](https://arxiv.org/abs/2507.20534)]

88. **GLM-4.5**: "GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models" [2025-08] [[paper](https://arxiv.org/abs/2508.06471)]

89. **GPT-OSS**: "gpt-oss-120b & gpt-oss-20b Model Card" [2025-08] [[paper](https://arxiv.org/abs/2508.10925)]

90. **LongCat-Flash**: "LongCat-Flash Technical Report" [2025-09] [[paper](https://arxiv.org/abs/2509.01322)]

91. **LLaDA-MoE**: "LLaDA-MoE: A Sparse MoE Diffusion Language Model" [2025-09] [[paper](https://arxiv.org/abs/2509.24389)]

92. **Ring-1T**: "Every Step Evolves: Scaling Reinforcement Learning for Trillion-Scale Thinking Model" [2025-10] [[paper](https://arxiv.org/abs/2510.18855)]

93. **Motif-2**: "Motif 2 12.7B technical report" [2025-11] [[paper](https://arxiv.org/abs/2511.07464)]

94. **Instella**: "Instella: Fully Open Language Models with Stellar Performance" [2025-11] [[paper](https://arxiv.org/abs/2511.10628)]

95. **DeepSeek-V3.2**: "DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models" [2025-12] [[paper](https://arxiv.org/abs/2512.02556)]

96. **Olmo 3**: "Olmo 3" [2025-12] [[paper](https://arxiv.org/abs/2512.13961)]

97. **T5Gemma 2**: "T5Gemma 2: Seeing, Reading, and Understanding Longer" [2025-12] [[paper](https://arxiv.org/abs/2512.14856)]

98. **LLaDA2.0**: "LLaDA2.0: Scaling Up Diffusion Language Models to 100B" [2025-12] [[paper](https://arxiv.org/abs/2512.15745)]

99. **Sigma-Moe-Tiny**: "Sigma-Moe-Tiny Technical Report" [2025-12] [[paper](https://arxiv.org/abs/2512.16248)]

100. **Nemotron 3 Nano**: "Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning" [2025-12] [[paper](https://arxiv.org/abs/2512.20848)]

101. **K-EXAONE**: "K-EXAONE Technical Report" [2026-01] [[paper](https://arxiv.org/abs/2601.01739)]

102. **MiMo-V2-Flash**: "MiMo-V2-Flash Technical Report" [2026-01] [[paper](https://arxiv.org/abs/2601.02780)]

103. **Ministral 3**: "Ministral 3" [2026-01] [[paper](https://arxiv.org/abs/2601.08584)]

104. **Kimi K2.5**: "Kimi K2.5: Visual Agentic Intelligence" [2026-02] [[paper](https://arxiv.org/abs/2602.02276)]

105. **EuroLLM-22B**: "EuroLLM-22B: Technical Report" [2026-02] [[paper](https://arxiv.org/abs/2602.05879)]

106. **Step 3.5 Flash**: "Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters" [2026-02] [[paper](https://arxiv.org/abs/2602.10604)]

107. **Nanbeige4.1**: "Nanbeige4.1-3B: A Small General Model that Reasons, Aligns, and Acts" [2026-02] [[paper](https://arxiv.org/abs/2602.13367)]

108. **GLM-5**: "GLM-5: from Vibe Coding to Agentic Engineering" [2026-02] [[paper](https://arxiv.org/abs/2602.15763)]

109. **Trinity**: "Arcee Trinity Large Technical Report" [2026-02] [[paper](https://arxiv.org/abs/2602.17004)]

110. **JoyAI-LLM Flash**: "JoyAI-LLM Flash: Advancing Mid-Scale LLMs with Token Efficiency" [2026-04] [[paper](https://arxiv.org/abs/2604.03044)]

### 2.2 Existing LLM Adapted to Code

These models are general-purpose LLMs further pretrained on code-related data.

- **Codex** (GPT-3): "Evaluating Large Language Models Trained on Code" [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]

- **PaLM Coder** (PaLM): "PaLM: Scaling Language Modeling with Pathways" [2022-04] [JMLR] [[paper](https://arxiv.org/abs/2204.02311)]

- **Minerva** (PaLM): "Solving Quantitative Reasoning Problems with Language Models" [2022-06] [[paper](https://arxiv.org/abs/2206.14858)]

- **PaLM 2 \*** (PaLM 2): "PaLM 2 Technical Report" [2023-05] [[paper](https://arxiv.org/abs/2305.10403)]

- **Code LLaMA** (LLaMA 2): "Code Llama: Open Foundation Models for Code" [2023-08] [[paper](https://arxiv.org/abs/2308.12950)] [[repo](https://github.com/facebookresearch/codellama)]

- **Lemur** (LLaMA 2): "Lemur: Harmonizing Natural Language and Code for Language Agents" [2023-10] [ICLR 2024 Spotlight] [[paper](https://arxiv.org/abs/2310.06830)]

- **BTX** (LLaMA 2): "Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM" [2024-03] [[paper](https://arxiv.org/abs/2403.07816)]

- **HiRoPE**: "HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position" [2024-03] [ACL 2024] [[paper](https://arxiv.org/abs/2403.19115)]

- "Mastering Text, Code and Math Simultaneously via Fusing Highly Specialized Language Models" [2024-03] [[paper](https://arxiv.org/abs/2403.08281)]

- **CodeGemma**: "CodeGemma: Open Code Models Based on Gemma" [2024-04] [[paper](https://storage.googleapis.com/deepmind-media/gemma/codegemma_report.pdf)] [[model](https://huggingface.co/models?search=google/codegemma)]

- **DeepSeek-Coder-V2**: "DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence" [2024-06] [[paper](https://arxiv.org/abs/2406.11931)]

- "Promise and Peril of Collaborative Code Generation Models: Balancing Effectiveness and Memorization" [2024-09] [[paper](https://arxiv.org/abs/2409.12020)]

- **Qwen2.5-Coder**: "Qwen2.5-Coder Technical Report" [2024-09] [[paper](https://arxiv.org/abs/2409.12186)]

- **Lingma SWE-GPT**: "Lingma SWE-GPT: An Open Development-Process-Centric Language Model for Automated Software Improvement" [2024-11] [[paper](https://arxiv.org/abs/2411.00622)]

- **Ling-Coder-Lite**: "Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM" [2025-03] [[paper](https://arxiv.org/abs/2503.17793)]

- **Mify-Coder**: "State-of-the-art Small Language Coder Model: Mify-Coder" [2025-12] [[paper](https://arxiv.org/abs/2512.23747)]

- **Composer 2**: "Composer 2 Technical Report" [2026-03] [[paper](https://arxiv.org/abs/2603.24477)]

### 2.3 General Pretraining on Code

These models are Transformer encoders, decoders, and encoder-decoders pretrained from scratch using existing objectives for general language modeling.

<p align='center'>
<img src='imgs/model_detail.png' style='width: 90%; '>
</p>

#### Encoder

1. **CuBERT** (MLM + NSP): "Learning and Evaluating Contextual Embedding of Source Code" [2019-12] [ICML 2020] [[paper](https://arxiv.org/abs/2001.00059)] [[repo](https://github.com/google-research/google-research/tree/master/cubert)]

2. **CodeBERT** (MLM + RTD): "CodeBERT: A Pre-Trained Model for Programming and Natural Languages" [2020-02] [EMNLP 2020 findings] [[paper](https://arxiv.org/abs/2002.08155)] [[repo](https://github.com/microsoft/CodeBERT)]

3. **GraphCodeBERT** (MLM + DFG Edge Prediction + DFG Node Alignment): "GraphCodeBERT: Pre-training Code Representations with Data Flow" [2020-09] [ICLR 2021] [[paper](https://arxiv.org/abs/2009.08366)] [[repo](https://github.com/microsoft/CodeBERT)]

4. **SynCoBERT** (MLM + Identifier Prediction + AST Edge Prediction + Contrastive Learning): "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation" [2021-08] [[paper](https://arxiv.org/abs/2108.04556)]

5. **DISCO** (MLM + Node Type MLM + Contrastive Learning): "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts" [2021-10] [ACL 2022] [[paper](https://arxiv.org/abs/2110.03868)]

6. **Code-MVP** (MLM + Type Inference + Contrastive Learning): "CODE-MVP: Learning to Represent Source Code from Multiple Views with Contrastive Pre-Training" [2022-05] [NAACL 2022 Technical Track] [[paper](https://arxiv.org/abs/2205.02029)]

7. **CodeSage** (MLM + Deobfuscation + Contrastive Learning): "Code Representation Learning At Scale" [2024-02] [ICLR 2024] [[paper](https://arxiv.org/abs/2402.01935)]

8. **CoLSBERT** (MLM): "Scaling Laws Behind Code Understanding Model" [2024-02] [[paper](https://arxiv.org/abs/2402.12813)]

9. **CodeSSM**: "CodeSSM: Towards State Space Models for Code Understanding" [2025-05] [EMNLP 2025] [[paper](https://arxiv.org/abs/2505.01475)]

#### Decoder

1. **GPT-C** (CLM): "IntelliCode Compose: Code Generation Using Transformer" [2020-05] [ESEC/FSE 2020] [[paper](https://arxiv.org/abs/2005.08025)]

2. **CodeGPT** (CLM): "CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation" [2021-02] [NeurIPS Datasets and Benchmarks 2021] [[paper](https://arxiv.org/abs/2102.04664)] [[repo](https://github.com/microsoft/CodeXGLUE)]

3. **CodeParrot** (CLM) [2021-12] [[blog](https://huggingface.co/blog/codeparrot)]

4. **PolyCoder** (CLM): "A Systematic Evaluation of Large Language Models of Code" [2022-02] [DL4C@ICLR 2022] [[paper](https://arxiv.org/abs/2202.13169)] [[repo](https://github.com/VHellendoorn/Code-LMs)]

5. **CodeGen** (CLM): "CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis" [2022-03] [ICLR 2023] [[paper](https://arxiv.org/abs/2203.13474)] [[repo](https://github.com/salesforce/CodeGen)]

6. **InCoder** (Causal Masking): "InCoder: A Generative Model for Code Infilling and Synthesis" [2022-04] [ICLR 2023] [[paper](https://arxiv.org/abs/2204.05999)] [[repo](https://github.com/dpfried/incoder)]

7. **PyCodeGPT** (CLM): "CERT: Continual Pre-Training on Sketches for Library-Oriented Code Generation" [2022-06] [IJCAI-ECAI 2022] [[paper](https://arxiv.org/abs/2206.06888)] [[repo](https://github.com/microsoft/PyCodeGPT)]

8. **PanGu-Coder** (CLM): "PanGu-Coder: Program Synthesis with Function-Level Language Modeling" [2022-07] [[paper](https://arxiv.org/abs/2207.11280)]

9. **SantaCoder** (FIM): "SantaCoder: don't reach for the stars!" [2023-01] [[paper](https://arxiv.org/abs/2301.03988)] [[model](https://huggingface.co/bigcode/santacoder)]

10. **CodeGeeX** (CLM): "CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Evaluations on HumanEval-X" [2023-03] [[paper](https://arxiv.org/abs/2303.17568)] [[repo](https://github.com/THUDM/CodeGeeX)]

11. **StarCoder** (FIM): "StarCoder: may the source be with you!" [2023-05] [[paper](https://arxiv.org/abs/2305.06161)] [[model](https://huggingface.co/bigcode/starcoder)]

12. **Phi-1** (CLM): "Textbooks Are All You Need" [2023-06] [[paper](https://arxiv.org/abs/2306.11644)] [[model](https://huggingface.co/microsoft/phi-1)]

13. **CodeFuse** (CLM): "CodeFuse-13B: A Pretrained Multi-lingual Code Large Language Model" [2023-10] [[paper](https://arxiv.org/abs/2310.06266)] [[model](https://huggingface.co/codefuse-ai/CodeFuse-13B)]

14. **DeepSeek Coder** (CLM+FIM): "DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence" [2024-01] [[paper](https://arxiv.org/abs/2401.14196)] [[repo](https://github.com/deepseek-ai/DeepSeek-Coder)]

15. **StarCoder2** (CLM+FIM): "StarCoder 2 and The Stack v2: The Next Generation" [2024-02] [[paper](https://arxiv.org/abs/2402.19173)] [[repo](https://github.com/bigcode-project/starcoder2)]

16. **CodeShell** (CLM+FIM): "CodeShell Technical Report" [2024-03] [[paper](https://arxiv.org/abs/2403.15747)] [[repo](https://github.com/WisdomShell/codeshell)]

17. **CodeQwen1.5** [2024-04] [[blog](https://qwenlm.github.io/blog/codeqwen1.5/)]

18. **Granite**: "Granite Code Models: A Family of Open Foundation Models for Code Intelligence" [2024-05] [[paper](https://arxiv.org/abs/2405.04324)] "Scaling Granite Code Models to 128K Context" [2024-07] [[paper](https://arxiv.org/abs/2407.13739)]

19. **NT-Java**: "Narrow Transformer: Starcoder-Based Java-LM For Desktop" [2024-07] [[paper](https://arxiv.org/abs/2407.03941)]

20. **Arctic-SnowCoder**: "Arctic-SnowCoder: Demystifying High-Quality Data in Code Pretraining" [2024-09] [[paper](https://arxiv.org/abs/2409.02326)]

21. **aiXcoder**: "aiXcoder-7B: A Lightweight and Effective Large Language Model for Code Completion" [2024-10] [[paper](https://arxiv.org/abs/2410.13187)]

22. **OpenCoder**: "OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models" [2024-11] [ACL 2025] [[paper](https://arxiv.org/abs/2411.04905)]

23. **ObscuraCoder**: "ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding" [2025-03] [ICLR 2025] [[paper](https://arxiv.org/abs/2504.00019)]

24. "Structure-Aware Fill-in-the-Middle Pretraining for Code" [2025-05] [[paper](https://arxiv.org/abs/2506.00204)]

25. **Seed-Coder**: "Seed-Coder: Let the Code Model Curate Data for Itself" [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]

26. **CWM**: "CWM: An Open-Weights LLM for Research on Code Generation with World Models" [2025-09] [[paper](https://arxiv.org/abs/2510.02387)]

27. **Mellum**: "Mellum: Production-Grade in-IDE Contextual Code Completion with Multi-File Project Understanding" [2025-10] [[paper](https://arxiv.org/abs/2510.05788)]

28. "Scaling Laws for Code: A More Data-Hungry Regime" [2025-10] [[paper](https://arxiv.org/abs/2510.08702)]

29. "Scaling Laws for Code: Every Programming Language Matters" [2025-12] [[paper](https://arxiv.org/abs/2512.13472)]

30. **InCoder**: "InCoder-32B: Code Foundation Model for Industrial Scenarios" [2026-03] [[paper](https://arxiv.org/abs/2603.16790)]

#### Encoder-Decoder

1. **PyMT5** (Span Corruption): "PyMT5: multi-mode translation of natural language and Python code with transformers" [2020-10] [EMNLP 2020] [[paper](https://arxiv.org/abs/2010.03150)]

2. **Mastropaolo et al.** (MLM + Deobfuscation): "DOBF: A Deobfuscation Pre-Training Objective for Programming Languages" [2021-02] [ICSE 2021] [[paper](https://arxiv.org/abs/2102.02017)] [[repo](https://github.com/antonio-mastropaolo/TransferLearning4Code)]

3. **DOBF** (Span Corruption): "Studying the Usage of Text-To-Text Transfer Transformer to Support Code-Related Tasks" [2021-02] [NeurIPS 2021] [[paper](https://arxiv.org/abs/2102.07492)] [[repo](https://github.com/facebookresearch/CodeGen/blob/main/docs/dobf.md)]

4. **PLBART** (DAE): "Unified Pre-training for Program Understanding and Generation" [2021-03] [NAACL 2021] [[paper](https://arxiv.org/abs/2103.06333)] [[repo](https://github.com/wasiahmad/PLBART)]

5. **CodeT5** (Span Corruption + Identifier Tagging + Masked Identifier Prediction + Text2Code + Code2Text): "CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation" [2021-09] [EMNLP 2021] [[paper](https://arxiv.org/abs/2109.00859)] [[repo](https://github.com/salesforce/CodeT5)]

6. **SPT-Code** (Span Corruption + NSP + Method Name Prediction): "SPT-Code: Sequence-to-Sequence Pre-Training for Learning Source Code Representations" [2022-01] [ICSE 2022 Technical Track] [[paper](https://arxiv.org/abs/2201.01549)]

7. **AlphaCode** (MLM + CLM): "Competition-Level Code Generation with AlphaCode" [2022-02] [Science] [[paper](https://arxiv.org/abs/2203.07814)] [[blog](https://deepmind.google/discover/blog/competitive-programming-with-alphacode/)]

8. **NatGen** (Code Naturalization): "NatGen: Generative pre-training by "Naturalizing" source code" [2022-06] [ESEC/FSE 2022] [[paper](https://arxiv.org/abs/2206.07585)] [[repo](https://github.com/saikat107/NatGen)]

9. **ERNIE-Code** (Span Corruption + Pivot-based Translation LM): "ERNIE-Code: Beyond English-Centric Cross-lingual Pretraining for Programming Languages" [2022-12] [ACL23 (Findings)] [[paper](https://aclanthology.org/2023.findings-acl.676.pdf)][[repo](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-code)]

10. **CodeT5+** (Span Corruption + CLM + Text-Code Contrastive Learning + Text-Code Translation): "CodeT5+: Open Code Large Language Models for Code Understanding and Generation" [2023-05] [EMNLP 2023] [[paper](https://arxiv.org/abs/2305.07922)] [[repo](https://github.com/salesforce/CodeT5)]

11. **AST-T5** (Span Corruption): "AST-T5: Structure-Aware Pretraining for Code Generation and Understanding" [2024-01] [ICML 2024] [[paper](https://arxiv.org/abs/2401.03003)]

12. **DivoT5**: "Directional Diffusion-Style Code Editing Pre-training" [2025-01] [[paper](https://arxiv.org/abs/2501.12079)]

#### UniLM

1. **CugLM** (MLM + NSP + CLM): "Multi-task Learning based Pre-trained Language Model for Code Completion" [2020-12] [ASE 2020] [[paper](https://arxiv.org/abs/2012.14631)]

2. **UniXcoder** (MLM + NSP + CLM + Span Corruption + Contrastive Learning + Code2Text): "UniXcoder: Unified Cross-Modal Pre-training for Code Representation" [2022-03] [ACL 2022] [[paper](https://arxiv.org/abs/2203.03850)] [[repo](https://github.com/microsoft/CodeBERT)]

#### Other Models

1. **DiffuCoder**: "DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation" [2025-06] [[paper](https://arxiv.org/abs/2506.20639)]

2. **Dream-Coder**: "Dream-Coder 7B: An Open Diffusion Language Model for Code" [2025-09] [[paper](https://arxiv.org/abs/2509.01142)]

3. "Beyond Autoregression: An Empirical Study of Diffusion Large Language Models for Code Generation" [2025-09] [[paper](https://arxiv.org/abs/2509.11252)]

4. **CoDA**: "CoDA: Coding LM via Diffusion Adaptation" [2025-10] [[paper](https://arxiv.org/abs/2510.03270)]

5. **Stable-DiffCoder**: "Stable-DiffCoder: Pushing the Frontier of Code Diffusion Large Language Model" [2026-01] [[paper](https://arxiv.org/abs/2601.15892)]

6. **DreamOn**: "DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-size Canvas" [2026-02] [[paper](https://arxiv.org/abs/2602.01326)]

7. "CodeOCR: On the Effectiveness of Vision Language Models in Code Understanding" [2026-02] [[paper](https://arxiv.org/abs/2602.01785)]

8. **IQuest-Coder-V1**: "IQuest-Coder-V1 Technical Report" [2026-02] [[paper](https://arxiv.org/abs/2603.16733)]

### 2.4 (Instruction) Fine-Tuning on Code

These models apply Instruction Fine-Tuning techniques to enhance the capacities of Code LLMs.

1. **WizardCoder** (StarCoder + Evol-Instruct): "WizardCoder: Empowering Code Large Language Models with Evol-Instruct" [2023-06] [ICLR 2024] [[paper](https://arxiv.org/abs/2306.08568)] [[repo](https://github.com/nlpxucan/WizardLM)]

2. **PanGu-Coder 2** (StarCoder + Evol-Instruct + RRTF): "PanGu-Coder2: Boosting Large Language Models for Code with Ranking Feedback" [2023-07] [[paper](https://arxiv.org/abs/2307.14936)]

3. **OctoCoder** (StarCoder) / **OctoGeeX** (CodeGeeX2): "OctoPack: Instruction Tuning Code Large Language Models" [2023-08] [ICLR 2024 Spotlight] [[paper](https://arxiv.org/abs/2308.07124)] [[repo](https://github.com/bigcode-project/octopack)]

4. "At Which Training Stage Does Code Data Help LLMs Reasoning" [2023-09] [ICLR 2024 Spotlight] [[paper](https://arxiv.org/abs/2309.16298)]

5. **InstructCoder**: "InstructCoder: Instruction Tuning Large Language Models for Code Editing" [[paper](https://arxiv.org/abs/2310.20329)] [[repo](https://github.com/qishenghu/CodeInstruct)]

6. **MFTCoder**: "MFTCoder: Boosting Code LLMs with Multitask Fine-Tuning" [2023-11] [KDD 2024] [[paper](https://arxiv.org/abs/2311.02303)] [[repo](https://github.com/codefuse-ai/MFTCoder)]

7. "LLM-Assisted Code Cleaning For Training Accurate Code Generators" [2023-11] [ICLR 2024] [[paper](https://arxiv.org/abs/2311.14904)]

8. **Magicoder**: "Magicoder: Empowering Code Generation with OSS-Instruct" [2023-12] [ICML 2024] [[paper](https://arxiv.org/abs/2312.02120)]

9. **WaveCoder**: "WaveCoder: Widespread And Versatile Enhancement For Code Large Language Models By Instruction Tuning" [2023-12] [ACL 2024] [[paper](https://arxiv.org/abs/2312.14187)]

10. **Astraios**: "Astraios: Parameter-Efficient Instruction Tuning Code Large Language Models" [2024-01] [[paper](https://arxiv.org/abs/2401.00788)]

11. **DolphCoder**: "DolphCoder: Echo-Locating Code Large Language Models with Diverse and Multi-Objective Instruction Tuning" [2024-02] [ACL 2024] [[paper](https://arxiv.org/abs/2402.09136)]

12. **SafeCoder**: "Instruction Tuning for Secure Code Generation" [2024-02] [ICML 2024] [[paper](https://arxiv.org/abs/2402.09497)]

13. "Code Needs Comments: Enhancing Code LLMs with Comment Augmentation" [ACL 2024 Findings] [[paper](https://arxiv.org/abs/2402.13013)]

14. **CCT**: "Code Comparison Tuning for Code Large Language Models" [2024-03] [[paper](https://arxiv.org/abs/2403.19121)]

15. **SAT**: "Structure-aware Fine-tuning for Code Pre-trained Models" [2024-04] [[paper](https://arxiv.org/abs/2404.07471)]

16. **CodeFort**: "CodeFort: Robust Training for Code Generation Models" [2024-04] [EMNLP 2024 Findings] [[paper](https://arxiv.org/abs/2405.01567)]

17. **XFT**: "XFT: Unlocking the Power of Code Instruction Tuning by Simply Merging Upcycled Mixture-of-Experts" [2024-04] [ACL 2024] [[paper](https://arxiv.org/abs/2404.15247)] [[repo](https://github.com/ise-uiuc/xft)]

18. **AIEV-Instruct**: "AutoCoder: Enhancing Code Large Language Model with AIEV-Instruct" [2024-05] [[paper](https://arxiv.org/abs/2405.14906)]

19. **AlchemistCoder**: "AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data" [2024-05] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2405.19265)]

20. "From Symbolic Tasks to Code Generation: Diversification Yields Better Task Performers" [2024-05] [[paper](https://arxiv.org/abs/2405.19787)]

21. "Unveiling the Impact of Coding Data Instruction Fine-Tuning on Large Language Models Reasoning" [2024-05] [[paper](https://arxiv.org/abs/2405.20535)]

22. **SemCoder**: "SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning" [2024-06] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2406.01006)]

23. **PLUM**: "PLUM: Preference Learning Plus Test Cases Yields Better Code Language Models" [2024-06] [[paper](https://arxiv.org/abs/2406.06887)]

24. **mCoder**: "McEval: Massively Multilingual Code Evaluation" [2024-06] [ICLR 2025] [[paper](https://arxiv.org/abs/2406.07436)]

25. "Unlock the Correlation between Supervised Fine-Tuning and Reinforcement Learning in Training Code Large Language Models" [2024-06] [[paper](https://arxiv.org/abs/2406.10305)]

26. **Code-Optimise**: "Code-Optimise: Self-Generated Preference Data for Correctness and Efficiency" [2024-06] [[paper](https://arxiv.org/abs/2406.12502)]

27. **UniCoder**: "UniCoder: Scaling Code Large Language Model via Universal Code" [2024-06] [ACL 2024] [[paper](https://arxiv.org/abs/2406.16441)]

28. "Brevity is the soul of wit: Pruning long files for code generation" [2024-06] [[paper](https://arxiv.org/abs/2407.00434)]

29. "Code Less, Align More: Efficient LLM Fine-tuning for Code Generation with Data Pruning" [2024-07] [[paper](https://arxiv.org/abs/2407.05040)]

30. **InverseCoder**: "InverseCoder: Unleashing the Power of Instruction-Tuned Code LLMs with Inverse-Instruct" [2024-07] [[paper](https://arxiv.org/abs/2407.05700)]

31. "Curriculum Learning for Small Code Language Models" [2024-07] [[paper](https://arxiv.org/abs/2407.10194)]

32. **Genetic-Instruct**: "Genetic Instruct: Scaling up Synthetic Generation of Coding Instructions for Large Language Models" [2024-07] [[paper](https://arxiv.org/abs/2407.21077)]

33. **DataScope**: "API-guided Dataset Synthesis to Finetune Large Code Models" [2024-08] [[paper](https://arxiv.org/abs/2408.08343)]

34. **XCoder**: "How Do Your Code LLMs Perform? Empowering Code Instruction Tuning with High-Quality Data" [2024-09] [EMNLP 2024] [[paper](https://arxiv.org/abs/2409.03810)]

35. **GALLa**: "GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding" [2024-09] [ACL 2025] [[paper](https://arxiv.org/abs/2409.04183)]

36. **HexaCoder**: "HexaCoder: Secure Code Generation via Oracle-Guided Synthetic Training Data" [2024-09] [[paper](https://arxiv.org/abs/2409.06446)]

37. **AMR-Evol**: "AMR-Evol: Adaptive Modular Response Evolution Elicits Better Knowledge Distillation for Large Language Models in Code Generation" [2024-10] [EMNLP 2024] [[paper](https://arxiv.org/abs/2410.00558)]

38. **LintSeq**: "Training Language Models on Synthetic Edit Sequences Improves Code Synthesis" [2024-10] [ICLR 2025] [[paper](https://arxiv.org/abs/2410.02749)]

39. **CoBa**: "CoBa: Convergence Balancer for Multitask Finetuning of Large Language Models" [2024-10] [EMNLP 2024] [[paper](https://arxiv.org/abs/2410.06741)]

40. **CursorCore**: "CursorCore: Assist Programming through Aligning Anything" [2024-10] [[paper](https://arxiv.org/abs/2410.07002)]

41. **SelfCodeAlign**: "SelfCodeAlign: Self-Alignment for Code Generation" [2024-10] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2410.24198)]

42. "Mastering the Craft of Data Synthesis for CodeLLMs" [2024-10] [[paper](https://arxiv.org/abs/2411.00005)]

43. **CodeLutra**: "CodeLutra: Boosting LLM Code Generation via Preference-Guided Refinement" [2024-11] [[paper](https://arxiv.org/abs/2411.05199)]

44. **DSTC**: "DSTC: Direct Preference Learning with Only Self-Generated Tests and Code to Improve Code LMs" [2024-11] [[paper](https://arxiv.org/abs/2411.13611)]

45. **WarriorCoder**: "WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models" [2024-12] [ACL 2025] [[paper](https://arxiv.org/abs/2412.17395)]

46. **EpiCoder**: "EpiCoder: Encompassing Diversity and Complexity in Code Generation" [2025-01] [ICML 2025] [[paper](https://arxiv.org/abs/2501.04694)]

47. **Qwen2.5-xCoder**: "Multi-Agent Collaboration for Multilingual Code Instruction Tuning" [2025-02] [ACL 2025] [[paper](https://arxiv.org/abs/2502.07487)]

48. **UnitCoder**: "UnitCoder: Scalable Code Synthesis from Pre-training Corpora" [2025-02] [EMNLP 2025] [[paper](https://arxiv.org/abs/2502.11460)]

49. **GiFT**: "GiFT: Gibbs Fine-Tuning for Code Generation" [2025-02] [ACL 2025] [[paper](https://arxiv.org/abs/2502.11466)]

50. **KODCODE**: "KodCode: A Diverse, Challenging, and Verifiable Synthetic Dataset for Coding" [2025-03] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2503.02951)]

51. **NextCoder**: "NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits" [2025-03] [ICML 2025] [[paper](https://arxiv.org/abs/2503.03656)]

52. **FAIT**: "FAIT: Fault-Aware Fine-Tuning for Better Code Generation" [2025-03] [[paper](https://arxiv.org/abs/2503.16913)]

53. **Z1**: "Z1: Efficient Test-time Scaling with Code" [2025-04] [EMNLP 2025 Industry] [[paper](https://arxiv.org/abs/2504.00810)]

54. **OpenCodeReasoning**: "OpenCodeReasoning: Advancing Data Distillation for Competitive Coding" [2025-04] [[paper](https://arxiv.org/abs/2504.01943)]

55. **OpenCodeInstruct**: "OpenCodeInstruct: A Large-scale Instruction Tuning Dataset for Code LLMs" [2025-04] [[paper](https://arxiv.org/abs/2504.04030)]

56. "Data-efficient LLM Fine-tuning for Code Generation" [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]

57. "AKD : Adversarial Knowledge Distillation For Large Language Models Alignment on Coding tasks" [2025-05] [[paper](https://arxiv.org/abs/2505.06267)]

58. "CRPE: Expanding The Reasoning Capability of Large Language Model for Code Generation" [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]

59. **VisCoder**: "VisCoder: Fine-Tuning LLMs for Executable Python Visualization Code Generation" [2025-05] [EMNLP 2025 Findings] [[paper](https://arxiv.org/abs/2506.03930)]

60. "AceReason-Nemotron 1.1: Advancing Math and Code Reasoning through SFT and RL Synergy" [2025-06] [[paper](https://arxiv.org/abs/2506.13284)]

61. **MoLE**: "Mix-of-Language-Experts Architecture for Multilingual Programming" [2025-06] [[paper](https://arxiv.org/abs/2506.18923)]

62. **OpenCodeReasoning-II**: "OpenCodeReasoning-II: A Simple Test Time Scaling Approach via Self-Critique" [2025-07] [[paper](https://arxiv.org/abs/2507.09075)]

63. "CodeEvo: Interaction-Driven Synthesis of Code-centric Data through Hybrid and Iterative Feedback" [2025-07] [[paper](https://arxiv.org/abs/2507.22080)]

64. **Tree-of-Evolution**: "Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models" [2025-07] [ACL 2025] [[paper](https://aclanthology.org/2025.acl-long.14/)]

65. **SCoder**: "SCoder: Progressive Self-Distillation for Bootstrapping Small-Scale Data Synthesizers to Empower Code LLMs" [2025-09] [EMNLP 2025 Fidnings] [[paper](https://arxiv.org/abs/2509.07858)]

66. "Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models" [2025-09] [EMNLP 2025 Findings] [[paper](https://arxiv.org/abs/2509.11686)]

67. "SCoGen: Scenario-Centric Graph-Based Synthesis of Real-World Code Problems" [2025-09] [[paper](https://arxiv.org/abs/2509.14281)]

68. "Verification Limits Code LLM Training" [2025-09] [[paper](https://arxiv.org/abs/2509.20837)]

69. **JanusCoder**: "JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence" [2025-10] [[paper](https://arxiv.org/abs/2510.23538)]

70. **VisCoder2**: "VisCoder2: Building Multi-Language Visualization Coding Agents" [2025-10] [[paper](https://arxiv.org/abs/2510.23642)]

71. "Beyond Language Boundaries: Uncovering Programming Language Families for Code Language Models" [2025-12] [[paper](https://arxiv.org/abs/2512.19509)]

72. **X-Coder**: "X-Coder: Advancing Competitive Programming with Fully Synthetic Tasks, Solutions, and Tests" [2026-01] [[paper](https://arxiv.org/abs/2601.06953)]

73. **SRI**: "From Completion to Editing: Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning" [2026-01] [[paper](https://arxiv.org/abs/2601.13384)]

74. "HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-BENCH" [2026-01] [[paper](https://arxiv.org/abs/2601.20255)]

75. "Multi-task Code LLMs: Data Mix or Model Merge?" [2026-01] [[paper](https://arxiv.org/abs/2601.21115)]

76. "QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions" [2026-03] [[paper](https://arxiv.org/abs/2603.12165)]

77. "Embarrassingly Simple Self-Distillation Improves Code Generation" [2026-04] [[paper](https://arxiv.org/abs/2604.01193)]

78. "Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL" [2026-04] [[paper](https://arxiv.org/abs/2604.20835)]

### 2.5 Reinforcement Learning on Code

1. **CompCoder**: "Compilable Neural Code Generation with Compiler Feedback" [2022-03] [ACL 2022] [[paper](https://arxiv.org/abs/2203.05132)]

2. **CodeRL**: "CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning" [2022-07] [NeurIPS 2022] [[paper](https://arxiv.org/abs/2207.01780)] [[repo](https://github.com/salesforce/CodeRL)]

3. **PPOCoder**: "Execution-based Code Generation using Deep Reinforcement Learning" [2023-01] [TMLR 2023] [[paper](https://arxiv.org/abs/2301.13816)] [[repo](https://github.com/reddy-lab-code-research/PPOCoder)]

4. **RLTF**: "RLTF: Reinforcement Learning from Unit Test Feedback" [2023-07] [[paper](https://arxiv.org/abs/2307.04349)] [[repo](https://github.com/Zyq-scut/RLTF)]

5. **B-Coder**: "B-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis" [2023-10] [ICLR 2024] [[paper](https://arxiv.org/abs/2310.03173)]

6. **IRCoCo**: "IRCoCo: Immediate Rewards-Guided Deep Reinforcement Learning for Code Completion" [2024-01] [FSE 2024] [[paper](https://arxiv.org/abs/2401.16637)]

7. **StepCoder**: "StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback" [2024-02] [ACL 2024] [[paper](https://arxiv.org/abs/2402.01391)]

8. **RLPF & DPA**: "Performance-Aligned LLMs for Generating Fast Code" [2024-04] [[paper](https://arxiv.org/abs/2404.18864)]

9. "Measuring memorization in RLHF for code completion" [2024-06] [ICLR 2025] [[paper](https://arxiv.org/abs/2406.11715)]

10. "Applying RLAIF for Code Generation with API-usage in Lightweight LLMs" [2024-06] [[paper](https://arxiv.org/abs/2406.20060)]

11. **RLCoder**: "RLCoder: Reinforcement Learning for Repository-Level Code Completion" [2024-07] [[paper](https://arxiv.org/abs/2407.19487)]

12. **PF-PPO**: "Policy Filtration in RLHF to Fine-Tune LLM for Code Generation" [2024-09] [[paper](https://arxiv.org/abs/2409.06957)]

13. **Coffee-Gym**: "Coffee-Gym: An Environment for Evaluating and Improving Natural Language Feedback on Erroneous Code" [2024-09] [EMNLP 2024] [[paper](https://arxiv.org/abs/2409.19715)]

14. **RLEF**: "RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning" [2024-10] [ICML 2025] [[paper](https://arxiv.org/abs/2410.02089)]

15. **CodePMP**: "CodePMP: Scalable Preference Model Pretraining for Large Language Model Reasoning" [2024-10] [[paper](https://arxiv.org/abs/2410.02229)]

16. **CodeDPO**: "CodeDPO: Aligning Code Models with Self Generated and Verified Source Code" [2024-10] [ACL 2025] [[paper](https://arxiv.org/abs/2410.05605)]

17. "Process Supervision-Guided Policy Optimization for Code Generation" [2024-10] [[paper](https://arxiv.org/abs/2410.17621)]

18. "Aligning CodeLLMs with Direct Preference Optimization" [2024-10] [[paper](https://arxiv.org/abs/2410.18585)]

19. **FALCON**: "FALCON: Feedback-driven Adaptive Long/short-term memory reinforced Coding Optimization system" [2024-10] [[paper](https://arxiv.org/abs/2410.21349)]

20. **PFPO**: "Preference Optimization for Reasoning with Pseudo Feedback" [2024-11] [[paper](https://arxiv.org/abs/2411.16345)]

21. **o1-Coder**: "o1-Coder: an o1 Replication for Coding" [2024-11] [[paper](https://arxiv.org/abs/2412.00154)]

22. **PRLCoder**: "Process-Supervised Reinforcement Learning for Code Generation" [2025-02] [EMNLP 2025] [[paper](https://arxiv.org/abs/2502.01715)]

23. **AceCoder**: "ACECODER: Acing Coder RL via Automated Test-Case Synthesis" [2025-02] [ACL 2025] [[paper](https://arxiv.org/abs/2502.01718)]

24. **Focused-DPO**: "Focused-DPO: Enhancing Code Generation Through Focused Preference Optimization on Error-Prone Points" [2025-02] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2502.11475)]

25. **SWE-RL**: "SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution" [2025-02] [[paper](https://arxiv.org/abs/2502.18449)]

26. **AceReason-Nemotron**: "AceReason-Nemotron: Advancing Math and Code Reasoning through Reinforcement Learning" [2025-05] [[paper](https://arxiv.org/abs/2505.16400)]

27. **rStar-Coder**: "rStar-Coder: Scaling Competitive Code Reasoning with a Large-Scale Verified Dataset" [2025-05] [[paper](https://arxiv.org/abs/2505.21297)]

28. **CURE**: "Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning" [2025-06] [[paper](https://arxiv.org/abs/2506.03136)]

29. **Magistral** [2025-06] [[paper](https://arxiv.org/abs/2506.10910)]

30. **Ring-lite**: "Ring-lite: Scalable Reasoning via C3PO-Stabilized Reinforcement Learning for LLMs" [2025-06] [[paper](https://arxiv.org/abs/2506.14731)]

31. **ReST-RL**: "ReST-RL: Achieving Accurate Code Reasoning of LLMs with Optimized Self-Training and Decoding" [2025-08] [[paper](https://arxiv.org/abs/2508.19576)]

32. "Towards Better Correctness and Efficiency in Code Generation" [2025-08] [[paper](https://arxiv.org/abs/2508.20124)]

33. "Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization" [2025-09] [[paper](https://arxiv.org/abs/2509.12434)]

34. "DELTA-Code: How Does RL Unlock and Transfer New Programming Algorithms in LLMs?" [2025-09] [[paper](https://arxiv.org/abs/2509.21016)]

35. **Critique-Coder**: "Critique-Coder: Enhancing Coder Models by Critique Reinforcement Learning" [2025-09] [[paper](https://arxiv.org/abs/2509.22824)]

36. **CodeRL+**: "CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment" [2025-10] [[paper](https://arxiv.org/abs/2510.18471)]

37. "GAPO: Group Adaptive Policy Optimization for Real-World Code Edit" [2025-10] [[paper](https://arxiv.org/abs/2510.21830)]

38. **AesCoder**: "Code Aesthetics with Agentic Reward Feedback" [2025-10] [[paper](https://arxiv.org/abs/2510.23272)]

39. **MURPHY**: "MURPHY: Multi-Turn GRPO for Self Correcting Code Generation" [2025-11] [[paper](https://arxiv.org/abs/2511.07833)]

40. **VeRPO**: "VeRPO: Verifiable Dense Reward Policy Optimization for Code Generation" [2026-01] [[paper](https://arxiv.org/abs/2601.03525)]

41. **Cobalt**: "Bridging Online and Offline RL: Contextual Bandit Learning for Multi-Turn Code Generation" [2026-02] [[paper](https://arxiv.org/abs/2602.03806)]

42. **MicroCoder-GRPO**: "Breaking Training Bottlenecks: Effective and Stable Reinforcement Learning for Coding Models" [2026-03] [[paper](https://arxiv.org/abs/2603.07777)]

43. "ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning" [2026-03] [[paper](https://arxiv.org/abs/2603.05863)]

44. **EvolveCoder**: "EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning" [2026-03] [[paper](https://arxiv.org/abs/2603.12698)]

45. **Code-A1**: "Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning" [2026-03] [[paper](https://arxiv.org/abs/2603.15611)]

## 3. When Coding Meets Reasoning

### 3.1 Coding for Reasoning

1. **PAL**: "PAL: Program-aided Language Models" [2022-11] [ICML 2023] [[paper](https://arxiv.org/abs/2211.10435)] [[repo](https://github.com/reasoning-machines/pal)]

2. **PoT**: "Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks" [2022-11] [TMLR 2023] [[paper](https://arxiv.org/abs/2211.12588)] [[repo](https://github.com/wenhuchen/Program-of-Thoughts)]

3. **PaD**: "PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning" [2023-05] [NAACL 2024] [[paper](https://arxiv.org/abs/2305.13888)]

4. **CSV**: "Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification" [2023-08] [ICLR 2024] [[paper](https://arxiv.org/abs/2308.07921)]

5. **MathCoder**: "MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning" [2023-10] [ICLR 2024] [[paper](https://arxiv.org/abs/2310.03731)]

6. **CoC**: "Chain of Code: Reasoning with a Language Model-Augmented Code Emulator" [2023-12] [ICML 2024] [[paper](https://arxiv.org/abs/2312.04474)]

7. **EHRAgent**: "EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records" [2024-01] [EMNLP 2024] [[paper](https://arxiv.org/abs/2401.07128)]

8. **MARIO**: "MARIO: MAth Reasoning with code Interpreter Output -- A Reproducible Pipeline" [2024-01] [ACL 2024 Findings] [[paper](https://arxiv.org/abs/2401.08190)]

9. "Code Prompting Elicits Conditional Reasoning Abilities in Text+Code LLMs" [2024-01] [EMNLP 2024] [[paper](https://arxiv.org/abs/2401.10065)]

10. **ReGAL**: "ReGAL: Refactoring Programs to Discover Generalizable Abstractions" [2024-01] [ICML 2024] [[paper](https://arxiv.org/abs/2401.16467)]

11. **CodeAct**: "Executable Code Actions Elicit Better LLM Agents" [2024-02] [ICML 2024] [[paper](https://arxiv.org/abs/2402.01030)]

12. **MultiPoT**: "Python is Not Always the Best Choice: Embracing Multilingual Program of Thoughts" [2024-02] [EMNLP 2024] [[paper](https://arxiv.org/abs/2402.10691)]

13. **HProPro**: "Exploring Hybrid Question Answering via Program-based Prompting" [2024-02] [ACL 2024] [[paper](https://arxiv.org/abs/2402.10812)]

14. **HTL**: "How Do Humans Write Code? Large Models Do It the Same Way Too" [2024-02] [EMNLP 2024] [[paper](https://arxiv.org/abs/2402.15729)]

15. **xSTREET**: "Eliciting Better Multilingual Structured Reasoning from LLMs through Code" [2024-03] [ACL 2024] [[paper](https://arxiv.org/abs/2403.02567)]

16. **FlowMind**: "FlowMind: Automatic Workflow Generation with LLMs" [2024-03] [[paper](https://arxiv.org/abs/2404.13050)]

17. **Think-and-Execute**: "Language Models as Compilers: Simulating Pseudocode Execution Improves Algorithmic Reasoning in Language Models" [2024-04] [EMNLP 2024] [[paper](https://arxiv.org/abs/2404.02575)]

18. **CoRE**: "CoRE: LLM as Interpreter for Natural Language Programming, Pseudo-Code Programming, and Flow Programming of AI Agents" [2024-05] [[paper](https://arxiv.org/abs/2405.06907)]

19. **MuMath-Code**: "MuMath-Code: Combining Tool-Use Large Language Models with Multi-perspective Data Augmentation for Mathematical Reasoning" [2024-05] [EMNLP 2024] [[paper](https://arxiv.org/abs/2405.07551)]

20. **COGEX**: "Learning to Reason via Program Generation, Emulation, and Search" [2024-05] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2405.16337)]

21. "Arithmetic Reasoning with LLM: Prolog Generation & Permutation" [2024-05] [[paper](https://arxiv.org/abs/2405.17893)]

22. "Can LLMs Reason in the Wild with Programs?" [2024-06] [EMNLP 2024 Findings] [[paper](https://arxiv.org/abs/2406.13764)]

23. **DotaMath**: "DotaMath: Decomposition of Thought with Code Assistance and Self-correction for Mathematical Reasoning" [2024-07] [[paper](https://arxiv.org/abs/2407.04078)]

24. **CIBench**: "CIBench: Evaluating Your LLMs with a Code Interpreter Plugin" [2024-07] [[paper](https://arxiv.org/abs/2407.10499)]

25. **PyBench**: "PyBench: Evaluating LLM Agent on various real-world coding tasks" [2024-07] [[paper](https://arxiv.org/abs/2407.16732)]

26. **AdaCoder**: "AdaCoder: Adaptive Prompt Compression for Programmatic Visual Question Answering" [2024-07] [[paper](https://arxiv.org/abs/2407.19410)]

27. **PyramidCoder**: "Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering" [2024-07] [[paper](https://arxiv.org/abs/2407.20563)]

28. **CodeGraph**: "CodeGraph: Enhancing Graph Reasoning of LLMs with Code" [2024-08] [[paper](https://arxiv.org/abs/2408.13863)]

29. **SIaM**: "SIaM: Self-Improving Code-Assisted Mathematical Reasoning of Large Language Models" [2024-08] [[paper](https://arxiv.org/abs/2408.15565)]

30. **CodePlan**: "CodePlan: Unlocking Reasoning Potential in Large Langauge Models by Scaling Code-form Planning" [2024-09] [ICLR 2025] [[paper](https://arxiv.org/abs/2409.12452)]

31. **PoT**: "Proof of Thought : Neurosymbolic Program Synthesis allows Robust and Interpretable Reasoning" [2024-09] [[paper](https://arxiv.org/abs/2409.17270)]

32. **MetaMath**: "MetaMath: Integrating Natural Language and Code for Enhanced Mathematical Reasoning in Large Language Models" [2024-09] [[paper](https://arxiv.org/abs/2409.19381)]

33. "BabelBench: An Omni Benchmark for Code-Driven Analysis of Multimodal and Multistructured Data" [2024-10] [[paper](https://arxiv.org/abs/2410.00773)]

34. **CodeSteer**: "Steering Large Language Models between Code Execution and Textual Reasoning" [2024-10] [ICLR 2025] [[paper](https://arxiv.org/abs/2410.03524)]

35. **MathCoder2**: "MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code" [2024-10] [ICLR 2025] [[paper](https://arxiv.org/abs/2410.08196)]

36. **LLMFP**: "Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming" [2024-10] [[paper](https://arxiv.org/abs/2410.12112)]

37. **Prove**: "Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning" [2024-10] [[paper](https://arxiv.org/abs/2410.12608)]

38. **PROVE**: "Trust but Verify: Programmatic VLM Evaluation in the Wild" [2024-10] [[paper](https://arxiv.org/abs/2410.13121)]

39. **GeoCoder**: "GeoCoder: Solving Geometry Problems by Generating Modular Code through Vision-Language Models" [2024-10] [[paper](https://arxiv.org/abs/2410.13510)]

40. **ReasonAgain**: "ReasonAgain: Using Extractable Symbolic Programs to Evaluate Mathematical Reasoning" [2024-10] [[paper](https://arxiv.org/abs/2410.19056)]

41. **GFP**: "Gap-Filling Prompting Enhances Code-Assisted Mathematical Reasoning" [2024-11] [[paper](https://arxiv.org/abs/2411.05407)]

42. **UTMath**: "UTMath: Math Evaluation with Unit Test via Reasoning-to-Coding Thoughts" [2024-11] [[paper](https://arxiv.org/abs/2411.07240)]

43. **CoCoP**: "CoCoP: Enhancing Text Classification with LLM through Code Completion Prompt" [2024-11] [[paper](https://arxiv.org/abs/2411.08979)]

44. **REPL-Plan**: "Interactive and Expressive Code-Augmented Planning with Large Language Models" [2024-11] [[paper](https://arxiv.org/abs/2411.13826)]

45. **CrossPAL**: "Empowering Multi-step Reasoning across Languages via Program-Aided Language Models" [2024-11] [EMNLP 2024] [[paper](https://aclanthology.org/2024.emnlp-main.678/)]

46. "From Code to Play: Benchmarking Program Search for Games Using Large Language Models" [2024-12] [[paper](https://arxiv.org/abs/2412.04057)]

47. **CoinMath**: "CoinMath: Harnessing the Power of Coding Instruction for Math LLMs" [2024-12] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2412.11699)]

48. **MultiLingPoT**: "MultiLingPoT: Boosting Mathematical Reasoning in LLMs through Multilingual Program Integration" [2024-12] [EMNLP 2025 Findings] [[paper](https://arxiv.org/abs/2412.12609)]

49. **ProgCo**: "ProgCo: Program Helps Self-Correction of Large Language Models" [2025-01] [ACL 2025] [[paper](https://arxiv.org/abs/2501.01264)]

50. **PIE**: "Pseudocode-Injection Magic: Enabling LLMs to Tackle Graph Computational Tasks" [2025-01] [[paper](https://arxiv.org/abs/2501.13731)]

51. **AutoCode4Math**: "Learning Autonomous Code Integration for Math Language Models" [2025-02] [[paper](https://arxiv.org/abs/2502.00691)]

52. **MIHTCCT**: "MIH-TCCT: Mitigating Inconsistent Hallucinations in LLMs via Event-Driven Text-Code Cyclic Training" [2025-02] [[paper](https://arxiv.org/abs/2502.08904)]

53. **ToolCoder**: "ToolCoder: A Systematic Code-Empowered Tool Learning Framework for Large Language Models" [2025-02] [[paper](https://arxiv.org/abs/2502.11404)]

54. **RM-PoT**: "RM-PoT: Reformulating Mathematical Problems and Solving via Program of Thoughts" [2025-02] [[paper](https://arxiv.org/abs/2502.12589)]

55. **SBSC**: "SBSC: Step-By-Step Coding for Improving Mathematical Olympiad Performance" [2025-02] [ICLR 2025] [[paper](https://arxiv.org/abs/2502.16666)]

56. "Towards Better Understanding of Program-of-Thought Reasoning in Cross-Lingual and Multilingual Environments" [2025-02] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2502.17956)]

57. "Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs" [2025-02] [EMNLP 2025] [[paper](https://arxiv.org/abs/2502.19411)]

58. "The KoLMogorov Test: Compression by Code Generation" [2025-03] [ICLR 2025] [[paper](https://arxiv.org/abs/2503.13992)]

59. **MathCoder-VL**: "MathCoder-VL: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning" [2025-05] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2505.10557)]

60. **R1-Code-Interpreter**: "R1-Code-Interpreter: Training LLMs to Reason with Code via Supervised and Reinforcement Learning" [2025-05] [[paper](https://arxiv.org/abs/2505.21668)]

61. "Towards Effective Code-Integrated Reasoning" [2025-05] [[paper](https://arxiv.org/abs/2505.24480)]

62. "CoRT: Code-integrated Reasoning within Thinking" [2025-06] [[paper](https://arxiv.org/abs/2506.09820)]

63. "Code Execution as Grounded Supervision for LLM Reasoning" [2025-06] [EMNLP 2025] [[paper](https://arxiv.org/abs/2506.10343)]

64. **PBB**: "Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training" [2025-06] [[paper](https://arxiv.org/abs/2506.18777)]

65. "On Code-Induced Reasoning in LLMs" [2025-09] [[paper](https://arxiv.org/abs/2509.21499)]

66. **PIPS**: "Once Upon an Input: Reasoning via Per-Instance Program Synthesis" [2025-10] [[paper](https://arxiv.org/abs/2510.22849)]

### 3.2 Code Simulation

- "Code Simulation Challenges for Large Language Models" [2024-01] [[paper](https://arxiv.org/abs/2401.09074)]

- "CodeMind: A Framework to Challenge Large Language Models for Code Reasoning" [2024-02] [[paper](https://arxiv.org/abs/2402.09664)]

- "Executing Natural Language-Described Algorithms with Large Language Models: An Investigation" [2024-02] [[paper](https://arxiv.org/abs/2403.00795)]

- "Can Language Models Pretend Solvers? Logic Code Simulation with LLMs" [2024-03] [[paper](https://arxiv.org/abs/2403.16097)]

- "Evaluating Large Language Models with Runtime Behavior of Program Execution" [2024-03] [[paper](https://arxiv.org/abs/2403.16437)]

- "NExT: Teaching Large Language Models to Reason about Code Execution" [2024-04] [ICML 2024] [[paper](https://arxiv.org/abs/2404.14662)]

- "SelfPiCo: Self-Guided Partial Code Execution with LLMs" [2024-07] [[paper](https://arxiv.org/abs/2407.16974)]

- "LogicPro: Improving Complex Logical Reasoning via Program-Guided Learning" [2024-09] [ACL 2025] [[paper](https://arxiv.org/abs/2409.12929)]

- "Large Language Models as Code Executors: An Exploratory Study" [2024-10] [[paper](https://arxiv.org/abs/2410.06667)]

- "VISUALCODER: Guiding Large Language Models in Code Execution with Fine-grained Multimodal Chain-of-Thought Reasoning" [2024-10] [[paper](https://arxiv.org/abs/2410.23402)]

- "CoCoNUT: Structural Code Understanding does not fall out of a tree" [2025-01] [[paper](https://arxiv.org/abs/2501.16456)]

- "CodeI/O: Condensing Reasoning Patterns via Code Input-Output Prediction" [2025-02] [ICML 2025] [[paper](https://arxiv.org/abs/2502.07316)]

- "SURGE: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors" [2025-02] [EMNLP 2025] [[paper](https://arxiv.org/abs/2502.11167)]

- "What I cannot execute, I do not understand: Training and Evaluating LLMs on Program Execution Traces" [2025-02] [[paper](https://arxiv.org/abs/2503.05703)]

- "L0-Reasoning Bench: Evaluating Procedural Correctness in Language Models via Simple Program Execution" [2025-03] [[paper](https://arxiv.org/abs/2503.22832)]

- "PLSemanticsBench: Large Language Models As Programming Language Interpreters" [2025-10] [[paper](https://arxiv.org/abs/2510.03415)]

- "Metric Calculating Benchmark: Code-Verifiable Complicate Instruction Following Benchmark for Large Language Models" [2025-10] [[paper](https://arxiv.org/abs/2510.07892)]

- "Breaking the Attention Trap in Code LLMs: A Rejection Sampling Approach to Enhance Code Execution Prediction" [2025-11] [EMNLP 2025 Findings] [[paper](https://aclanthology.org/2025.findings-emnlp.592/)]

### 3.3 Code Agents

1. **Self-collaboration**: "Self-collaboration Code Generation via ChatGPT" [2023-04] [[paper](https://arxiv.org/abs/2304.07590)]

2. **ChatDev**: "Communicative Agents for Software Development" [2023-07] [[paper](https://arxiv.org/abs/2307.07924)] [[repo](https://github.com/OpenBMB/ChatDev)]

3. **MetaGPT**: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework" [2023-08] [[paper](https://arxiv.org/abs/2308.00352)] [[repo](https://github.com/geekan/MetaGPT)]

4. **CodeChain**: "CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules" [2023-10] [ICLR 2024] [[paper](https://arxiv.org/abs/2310.08992)]

5. **CodeAgent**: "CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges" [2024-01] [ACL 2024] [[paper](https://arxiv.org/abs/2401.07339)]

6. **CONLINE**: "CoCoST: Automatic Complex Code Generation with Online Searching and Correctness Testing" [2024-03] [EMNLP 2024] [[paper](https://arxiv.org/abs/2403.13583)]

7. **LCG**: "When LLM-based Code Generation Meets the Software Development Process" [2024-03] [[paper](https://arxiv.org/abs/2403.15852)]

8. **RepairAgent**: "RepairAgent: An Autonomous, LLM-Based Agent for Program Repair" [2024-03] [[paper](https://arxiv.org/abs/2403.17134)]

9. **MAGIS:**: "MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution" [2024-03] [[paper](https://arxiv.org/abs/2403.17927)]

10. **SoA**: "Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization" [2024-04] [[paper](https://arxiv.org/abs/2404.02183)]

11. **AutoCodeRover**: "AutoCodeRover: Autonomous Program Improvement" [2024-04] [[paper](https://arxiv.org/abs/2404.05427)]

12. **SWE-agent**: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering" [2024-05] [[paper](https://arxiv.org/abs/2405.15793)]

13. **MapCoder**: "MapCoder: Multi-Agent Code Generation for Competitive Problem Solving" [2024-05] [ACL 2024] [[paper](https://arxiv.org/abs/2405.11403)]

14. "Fight Fire with Fire: How Much Can We Trust ChatGPT on Source Code-Related Tasks?" [2024-05] [[paper](https://arxiv.org/abs/2405.12641)]

15. **FunCoder**: "Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation" [2024-05] [[paper](https://arxiv.org/abs/2405.20092)]

16. **CTC**: "Multi-Agent Software Development through Cross-Team Collaboration" [2024-06] [[paper](https://arxiv.org/abs/2406.08979)]

17. **MASAI**: "MASAI: Modular Architecture for Software-engineering AI Agents" [2024-06] [[paper](https://arxiv.org/abs/2406.11638)]

18. **AgileCoder**: "AgileCoder: Dynamic Collaborative Agents for Software Development based on Agile Methodology" [2024-06] [[paper](https://arxiv.org/abs/2406.11912)]

19. **CodeNav**: "CodeNav: Beyond tool-use to using real-world codebases with LLM agents" [2024-06] [[paper](https://arxiv.org/abs/2406.12276)]

20. **INDICT**: "INDICT: Code Generation with Internal Dialogues of Critiques for Both Security and Helpfulness" [2024-06] [[paper](https://arxiv.org/abs/2407.02518)]

21. **AppWorld**: "AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents" [2024-07] [[paper](https://arxiv.org/abs/2407.18901)]

22. **CortexCompile**: "CortexCompile: Harnessing Cortical-Inspired Architectures for Enhanced Multi-Agent NLP Code Synthesis" [2024-08] [[paper](https://arxiv.org/abs/2409.02938)]

23. **DEI**: "Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents" [2024-08] [ICLR 2025] [[paper](https://arxiv.org/abs/2408.07060)]

24. **Survey**: "Large Language Model-Based Agents for Software Engineering: A Survey" [2024-09] [[paper](https://arxiv.org/abs/2409.02977)]

25. **PairCoder**: "A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement" [2024-09] [ASE 2024] [[paper](https://arxiv.org/abs/2409.05001)] [[repo](https://github.com/nju-websoft/PairCoder)]

26. **AutoSafeCoder**: "AutoSafeCoder: A Multi-Agent Framework for Securing LLM Code Generation through Static Analysis and Fuzz Testing" [2024-09] [[paper](https://arxiv.org/abs/2409.10737)]

27. **SuperCoder2.0**: "SuperCoder2.0: Technical Report on Exploring the feasibility of LLMs as Autonomous Programmer" [2024-09] [[paper](https://arxiv.org/abs/2409.11190)]

28. **Survey**: "Agents in Software Engineering: Survey, Landscape, and Vision" [2024-09] [[paper](https://arxiv.org/abs/2409.09030)]

29. **MOSS**: "MOSS: Enabling Code-Driven Evolution and Context Management for AI Agents" [2024-09] [[paper](https://arxiv.org/abs/2409.16120)]

30. **HyperAgent**: "HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale" [2024-09] [[paper](https://arxiv.org/abs/2409.16299)]

31. "Compositional Hardness of Code in Large Language Models -- A Probabilistic Perspective" [2024-09] [[paper](https://arxiv.org/abs/2409.18028)]

32. **RGD**: "RGD: Multi-LLM Based Agent Debugger via Refinement and Generation Guidance" [2024-10] [[paper](https://arxiv.org/abs/2410.01242)]

33. **Seeker**: "Seeker: Enhancing Exception Handling in Code with LLM-based Multi-Agent Approach" [2024-10] [[paper](https://arxiv.org/abs/2410.06949)]

34. **REDO**: "REDO: Execution-Free Runtime Error Detection for COding Agents" [2024-10] [[paper](https://arxiv.org/abs/2410.09117)]

35. "Evaluating Software Development Agents: Patch Patterns, Code Quality, and Issue Complexity in Real-World GitHub Scenarios" [2024-10] [[paper](https://arxiv.org/abs/2410.12468)]

36. **EvoMAC**: "Self-Evolving Multi-Agent Collaboration Networks for Software Development" [2024-10] [ICLR 2025] [[paper](https://arxiv.org/abs/2410.16946)]

37. **VisionCoder**: "VisionCoder: Empowering Multi-Agent Auto-Programming for Image Processing with Hybrid LLMs" [2024-10] [[paper](https://arxiv.org/abs/2410.19245)]

38. **AutoKaggle**: "AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions" [2024-10] [[paper](https://arxiv.org/abs/2410.20424)]

39. **Watson**: "Watson: A Cognitive Observability Framework for the Reasoning of Foundation Model-Powered Agents" [2024-11] [[paper](https://arxiv.org/abs/2411.03455)]

40. **CodeTree**: "CodeTree: Agent-guided Tree Search for Code Generation with Large Language Models" [2024-11] [[paper](https://arxiv.org/abs/2411.04329)]

41. **EvoCoder**: "LLMs as Continuous Learners: Improving the Reproduction of Defective Code in Software Issues" [2024-11] [[paper](https://arxiv.org/abs/2411.13941)]

42. **AEGIS**: "AEGIS: An Agent-based Framework for General Bug Reproduction from Issue Descriptions" [2024-11] [[paper](https://arxiv.org/abs/2411.18015)]

43. **ExecutionAgent**: "You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects" [2024-12] [[paper](https://arxiv.org/abs/2412.10133)]

44. **GHIssueMarket**: "GHIssuemarket: A Sandbox Environment for SWE-Agents Economic Experimentation" [2024-12] [[paper](https://arxiv.org/abs/2412.11722)]

45. **SWE-Gym**: "Training Software Engineering Agents and Verifiers with SWE-Gym" [2024-12] [ICML 2025] [[paper](https://arxiv.org/abs/2412.21139)]

46. **SWE-Fixer**: "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution" [2025-01] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2501.05040)]

47. **CodeCoR**: "CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation" [2025-01] [[paper](https://arxiv.org/abs/2501.07811)]

48. **QualityFlow**: "QualityFlow: An Agentic Workflow for Program Synthesis Controlled by LLM Quality Checks" [2025-01] [[paper](https://arxiv.org/abs/2501.17167)]

49. **Cogito**: "Cogito, ergo sum: A Neurobiologically-Inspired Cognition-Memory-Growth System for Code Generation" [2025-01] [[paper](https://arxiv.org/abs/2501.18653)]

50. **OrcaLoca**: "OrcaLoca: An LLM Agent Framework for Software Issue Localization" [2025-02] [ICML 2025] [[paper](https://arxiv.org/abs/2502.00350)]

51. **BRT Agent**: "Agentic Bug Reproduction for Effective Automated Program Repair at Google" [2025-02] [[paper](https://arxiv.org/abs/2502.01821)]

52. **CodeSim**: "CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging" [2025-02] [[paper](https://arxiv.org/abs/2502.05664)]

53. **SyncMind**: "SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering" [2025-02] [ICML 2025] [[paper](https://arxiv.org/abs/2502.06994)]

54. **SoRFT**: "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning" [2025-02] [[paper](https://arxiv.org/abs/2502.20127)]

55. "Is Multi-Agent Debate (MAD) the Silver Bullet? An Empirical Analysis of MAD in Code Summarization and Translation" [2025-03] [[paper](https://arxiv.org/abs/2503.12029)]

56. **DARS**: "DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance by Adaptive Tree Traversal" [2025-03] [ACL 2025] [[paper](https://arxiv.org/abs/2503.14269)]

57. **SEAlign**: "SEAlign: Alignment Training for Software Engineering Agent" [2025-03] [[paper](https://arxiv.org/abs/2503.18455)]

58. **SWE-SynInfer**: "Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute" [2025-03] [[paper](https://arxiv.org/abs/2503.23803)]

59. **AdaCoder**: "AdaCoder: An Adaptive Planning and Multi-Agent Framework for Function-Level Code Generation" [2025-04] [[paper](https://arxiv.org/abs/2504.04220)]

60. **SICA**: "A Self-Improving Coding Agent" [2025-04] [[paper](https://arxiv.org/abs/2504.15228)]

61. **SWE-smith**: "SWE-smith: Scaling Data for Software Engineering Agents" [2025-04] [[paper](https://arxiv.org/abs/2504.21798)]

62. "Enhancing LLM Code Generation: A Systematic Evaluation of Multi-Agent Collaboration and Runtime Debugging for Improved Accuracy, Reliability, and Latency" [2025-05] [[paper](https://arxiv.org/abs/2505.02133)]

63. **SEW**: "SEW: Self-Evolving Agentic Workflows for Automated Code Generation" [2025-05] [[paper](https://arxiv.org/abs/2505.18646)]

64. **RepoMaster**: "RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task Solving" [2025-05] [[paper](https://arxiv.org/abs/2505.21577)]

65. **Code Researcher**: "Code Researcher: Deep Research Agent for Large Systems Code and Commit History" [2025-05] [[paper](https://arxiv.org/abs/2506.11060)]

66. "Lessons Learned: A Multi-Agent Framework for Code LLMs to Learn and Improve" [2025-05] [[paper](https://arxiv.org/abs/2505.23946)]

67. "EvoGit: Decentralized Code Evolution via Git-Based Multi-Agent Collaboration" [2025-06] [[paper](https://arxiv.org/abs/2506.02049)]

68. **SWE-Factory**: "SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks" [2025-06] [[paper](https://arxiv.org/abs/2506.10954)]

69. **Agent-RLVR**: "Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards" [2025-06] [[paper](https://arxiv.org/abs/2506.11425)]

70. **AlphaEvolve**: "AlphaEvolve: A coding agent for scientific and algorithmic discovery" [2025-06] [[paper](https://arxiv.org/abs/2506.13131)]

71. **USEagent**: "Unified Software Engineering agent as AI Software Engineer" [2025-06] [[paper](https://arxiv.org/abs/2506.14683)]

72. **SemAgent**: "SemAgent: A Semantics Aware Program Repair Agent" [2025-06] [[paper](https://arxiv.org/abs/2506.16650)]

73. **Trae Agent**: "Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling" [2025-07] [[paper](https://arxiv.org/abs/2507.23370)]

74. "Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity" [2025-07] [ICML 2025] [[paper](https://icml.cc/virtual/2025/poster/44274)]

75. **DebateCoder**: "DebateCoder: Towards Collective Intelligence of LLMs via Test Case Driven LLM Debate for Code Generation" [2025-07] [ACL 2025] [[paper](https://aclanthology.org/2025.acl-long.589/)]

76. "GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging" [2025-08] [[paper](https://arxiv.org/abs/2508.18993)]

77. **MapCoder-Lite**: "MapCoder-Lite: Squeezing Multi-Agent Coding into a Single Small LLM" [2025-09] [[paper](https://arxiv.org/abs/2509.17489)]

78. **Devstral**: "Devstral: Fine-tuning Language Models for Coding Agent Applications" [2025-09] [[paper](https://arxiv.org/abs/2509.25193)]

79. **Lita**: "Lita: Light Agent Uncovers the Agentic Coding Capabilities of LLMs" [2025-09] [[paper](https://arxiv.org/abs/2509.25873)]

80. **Kimi-Dev**: "Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents" [2025-09] [[paper](https://arxiv.org/abs/2509.23045)]

81. **VeriGuard**: "VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation" [2025-10] [[paper](https://arxiv.org/abs/2510.05156)]

82. **KAT-Coder**: "KAT-Coder Technical Report" [2025-10] [[paper](https://arxiv.org/abs/2510.18779)]

83. **TOM-SWE**: "TOM-SWE: User Mental Modeling For Software Engineering Agents" [2025-10] [[paper](https://arxiv.org/abs/2510.21903)]

84. **SwiftSolve**: "SwiftSolve: A Self-Iterative, Complexity-Aware Multi-Agent Framework for Competitive Programming" [2025-10] [[paper](https://arxiv.org/abs/2510.22626)]

85. **CodeClash**: "CodeClash: Benchmarking Goal-Oriented Software Engineering" [2025-11] [[paper](https://arxiv.org/abs/2511.00839)]

86. "A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric Software Engineering Tasks" [2025-10] [[paper](https://arxiv.org/abs/2511.00872)]

87. "Designing LLM-based Multi-Agent Systems for Software Engineering Tasks: Quality Attributes, Design Patterns and Rationale" [2025-11] [[paper](https://arxiv.org/abs/2511.08475)]

88. "Evaluating Software Process Models for Multi-Agent Class-Level Code Generation" [2025-11] [[paper](https://arxiv.org/abs/2511.09794)]

89. **LoCoBench-Agent**: "LoCoBench-Agent: An Interactive Benchmark for LLM Agents in Long-Context Software Engineering" [2025-11] [[paper](https://arxiv.org/abs/2511.13998)]

90. **Live-SWE-agent**: "Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?" [2025-11] [[paper](https://arxiv.org/abs/2511.13646)]

91. "Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems" [2025-11] [[paper](https://arxiv.org/abs/2511.18467)]

92. "Process-Centric Analysis of Agentic Software Systems" [2025-12] [[paper](https://arxiv.org/abs/2512.02393)]

93. **PARC**: "PARC: An Autonomous Self-Reflective Coding Agent for Robust Execution of Long-Horizon Tasks" [2025-12] [[paper](https://arxiv.org/abs/2512.03549)]

94. **DeepCode**: "DeepCode: Open Agentic Coding" [2025-12] [[paper](https://arxiv.org/abs/2512.07921)]

95. **CCA**: "Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial Scale" [2025-12] [[paper](https://arxiv.org/abs/2512.10398)]

96. **SWE-Playground**: "Training Versatile Coding Agents in Synthetic Environments" [2025-12] [[paper](https://arxiv.org/abs/2512.12216)]

97. **SSR**: "Toward Training Superintelligent Software Agents through Self-Play SWE-RL" [2025-12] [[paper](https://arxiv.org/abs/2512.18552)]

98. **RepoNavigator**: "One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents" [2025-12] [[paper](https://arxiv.org/abs/2512.20957)]

99. **SWE-RM**: "SWE-RM: Execution-free Feedback For Software Engineering Agents" [2025-12] [[paper](https://arxiv.org/abs/2512.21919)]

100. **MemGovern**: "MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences" [2026-01] [[paper](https://arxiv.org/abs/2601.06789)]

101. "APEX-SWE" [2026-01] [[paper](https://arxiv.org/abs/2601.08806)]

102. **Terminal-Bench**: "Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces" [2026-01] [[paper](https://arxiv.org/abs/2601.11868)]

103. **CooperBench**: "CooperBench: Why Coding Agents Cannot be Your Teammates Yet" [2026-01] [[paper](https://arxiv.org/abs/2601.13295)]

104. **SWE-Pruner**: "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents" [2026-01] [[paper](https://arxiv.org/abs/2601.16746)]

105. **daVinci-Dev**: "daVinci-Dev: Agent-native Mid-training for Software Engineering" [2026-01] [[paper](https://arxiv.org/abs/2601.18418)]

106. **DevOps-Gym**: "DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle" [2026-01] [[paper](https://arxiv.org/abs/2601.20882)]

107. **TerminalTraj**: "Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments" [2026-02] [[paper](https://arxiv.org/abs/2602.01244)]

108. **RPG-Encoder**: "Closing the Loop: Universal Repository Representation with RPG-Encoder" [2026-02] [[paper](https://arxiv.org/abs/2602.02084)]

109. **TDScaling**: "Beyond Quantity: Trajectory Diversity Scaling for Code Agents" [2026-02] [[paper](https://arxiv.org/abs/2602.03219)]

110. **SWE-Master**: "SWE-Master: Unleashing the Potential of Software Engineering Agents via Post-Training" [2026-02] [[paper](https://arxiv.org/abs/2602.03411)]

111. **SWE-World**: "SWE-World: Building Software Engineering Agents in Docker-Free Environments" [2026-02] [[paper](https://arxiv.org/abs/2602.03419)]

112. "Scaling Agentic Verifier for Competitive Coding" [2026-02] [[paper](https://arxiv.org/abs/2602.04254)]

113. **TermiGen**: "TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents" [2026-02] [[paper](https://arxiv.org/abs/2602.07274)]

114. **LongCLI-Bench**: "LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces" [2026-02] [[paper](https://arxiv.org/abs/2602.14337)]

115. **Hybrid-Gym**: "Hybrid-Gym: Training Coding Agents to Generalize Across Tasks" [2026-02] [[paper](https://arxiv.org/abs/2602.16819)]

116. "Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining" [2026-03] [[paper](https://arxiv.org/abs/2603.11103)]

117. **DeepCommit**: "EvoClaw: Evaluating AI Agents on Continuous Software Evolution" [2026-03] [[paper](https://arxiv.org/abs/2603.13428)]

118. **CAID**: "Effective Strategies for Asynchronous Software Engineering Agents" [2026-03] [[paper](https://arxiv.org/abs/2603.21489)]

119. "Coding Agents are Effective Long-Context Processors" [2026-03] [[paper](https://arxiv.org/abs/2603.20432)]

120. **SlopCodeBench**: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks" [2026-03] [[paper](https://arxiv.org/abs/2603.24755)]

121. **KAT-Coder-V2**: "KAT-Coder-V2 Technical Report" [2026-03] [[paper](https://arxiv.org/abs/2603.27703)]

122. **SWE Atlas**: "SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution" [2026-05] [[paper](https://arxiv.org/abs/2605.08366)]

### 3.4 Interactive Coding

- "Interactive Program Synthesis" [2017-03] [[paper](https://arxiv.org/abs/1703.03539)]

- "Question selection for interactive program synthesis" [2020-06] [PLDI 2020] [[paper](https://dl.acm.org/doi/10.1145/3385412.3386025)]

- "Interactive Code Generation via Test-Driven User-Intent Formalization" [2022-08] [[paper](https://arxiv.org/abs/2208.05950)]

- "Improving Code Generation by Training with Natural Language Feedback" [2023-03] [TMLR] [[paper](https://arxiv.org/abs/2303.16749)]

- "Self-Refine: Iterative Refinement with Self-Feedback" [2023-03] [NeurIPS 2023] [[paper](https://arxiv.org/abs/2303.17651)]

- "Teaching Large Language Models to Self-Debug" [2023-04] [[paper](https://arxiv.org/abs/2304.05128)]

- "Self-Edit: Fault-Aware Code Editor for Code Generation" [2023-05] [ACL 2023] [[paper](https://arxiv.org/abs/2305.04087)]

- "LeTI: Learning to Generate from Textual Interactions" [2023-05] [[paper](https://arxiv.org/abs/2305.10314)]

- "Is Self-Repair a Silver Bullet for Code Generation?" [2023-06] [ICLR 2024] [[paper](https://arxiv.org/abs/2306.09896)]

- "InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback" [2023-06] [NeurIPS 2023] [[paper](https://arxiv.org/abs/2306.14898)]

- "INTERVENOR: Prompting the Coding Ability of Large Language Models with the Interactive Chain of Repair" [2023-11] [ACL 2024 Findings] [[paper](https://arxiv.org/abs/2311.09868)]

- "OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement" [2024-02] [ACL 2024 Findings] [[paper](https://arxiv.org/abs/2402.14658)]

- "Iterative Refinement of Project-Level Code Context for Precise Code Generation with Compiler Feedback" [2024-03] [ACL 2024 Findings] [[paper](https://arxiv.org/abs/2403.16792)]

- "CYCLE: Learning to Self-Refine the Code Generation" [2024-03] [[paper](https://arxiv.org/abs/2403.18746)]

- "LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation" [2024-04] [[paper](https://arxiv.org/abs/2404.10100)]

- "SOAP: Enhancing Efficiency of Generated Code via Self-Optimization" [2024-05] [[paper](https://arxiv.org/abs/2405.15189)]

- "Code Repair with LLMs gives an Exploration-Exploitation Tradeoff" [2024-05] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2405.17503)]

- "ReflectionCoder: Learning from Reflection Sequence for Enhanced One-off Code Generation" [2024-05] [ACL 2025] [[paper](https://arxiv.org/abs/2405.17057)]

- "Training LLMs to Better Self-Debug and Explain Code" [2024-05] [NeurIPS 2024] [[paper](https://arxiv.org/abs/2405.18649)]

- "Requirements are All You Need: From Requirements to Code with LLMs" [2024-06] [[paper](https://arxiv.org/abs/2406.10101)]

- "I Need Help! Evaluating LLM's Ability to Ask for Users' Support: A Case Study on Text-to-SQL Generation" [2024-07] [EMNLP 2024] [[paper](https://arxiv.org/abs/2407.14767)]

- "An Empirical Study on Self-correcting Large Language Models for Data Science Code Generation" [2024-08] [[paper](https://arxiv.org/abs/2408.15658)]

- "RethinkMCTS: Refining Erroneous Thoughts in Monte Carlo Tree Search for Code Generation" [2024-09] [EMNLP 2025] [[paper](https://arxiv.org/abs/2409.09584)]

- "From Code to Correctness: Closing the Last Mile of Code Generation with Hierarchical Debugging" [2024-10] [[paper](https://arxiv.org/abs/2410.01215)] [[repo](https://github.com/YerbaPage/MGDebugger)]

- "What Makes Large Language Models Reason in (Multi-Turn) Code Generation?" [2024-10] [ICLR 2025] [[paper](https://arxiv.org/abs/2410.08105)]

- "The First Prompt Counts the Most! An Evaluation of Large Language Models on Iterative Example-based Code Generation" [2024-11] [[paper](https://arxiv.org/abs/2411.06774)]

- "Planning-Driven Programming: A Large Language Model Programming Workflow" [2024-11] [ACL 2025] [[paper](https://arxiv.org/abs/2411.14503)]

- "ConAIR:Consistency-Augmented Iterative Interaction Framework to Enhance the Reliability of Code Generation" [2024-11] [[paper](https://arxiv.org/abs/2411.15587)]

- "Socratic Human Feedback (SoHF): Expert Steering Strategies for LLM Code Generation" [2024-11] [EMNLP 2024 Findings] [[paper](https://aclanthology.org/2024.findings-emnlp.908/)]

- "PerfCodeGen: Improving Performance of LLM Generated Code with Execution Feedback" [2024-11] [[paper](https://arxiv.org/abs/2412.03578)]

- "GenX: Mastering Code and Test Generation with Execution Feedback" [2024-12] [[paper](https://arxiv.org/abs/2412.13464)]

- "Helping LLMs Improve Code Generation Using Feedback from Testing and Static Analysis" [2024-12] [[paper](https://arxiv.org/abs/2412.14841)]

- "Outcome-Refining Process Supervision for Code Generation" [2024-12] [[paper](https://arxiv.org/abs/2412.15118)]

- "Tree-of-Code: A Tree-Structured Exploring Framework for End-to-End Code Generation and Execution in Complex Task Handling" [2024-12] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2412.15305)]

- "Dynamic Scaling of Unit Tests for Code Reward Modeling" [2025-01] [ACL 2025] [[paper](https://arxiv.org/abs/2501.01054)]

- "Revisit Self-Debugging with Self-Generated Tests for Code Generation" [2025-01] [ACL 2025] [[paper](https://arxiv.org/abs/2501.12793)]

- "Learning to Generate Unit Tests for Automated Debugging" [2025-02] [[paper](https://arxiv.org/abs/2502.01619)]

- "Large Language Model Guided Self-Debugging Code Generation" [2025-02] [[paper](https://arxiv.org/abs/2502.02928)]

- "On Iterative Evaluation and Enhancement of Code Quality Using GPT-4o" [2025-02] [[paper](https://arxiv.org/abs/2502.07399)]

- "Intention is All You Need: Refining Your Code from Your Intention" [2025-02] [[paper](https://arxiv.org/abs/2502.08172)]

- "RefineCoder: Iterative Improving of Large Language Models via Adaptive Critique Refinement for Code Generation" [2025-02] [[paper](https://arxiv.org/abs/2502.09183)]

- "VisPath: Automated Visualization Code Synthesis via Multi-Path Reasoning and Feedback-Driven Optimization" [2025-02] [[paper](https://arxiv.org/abs/2502.11140)]

- "S\*: Test Time Scaling for Code Generation" [2025-02] [EMNLP 2025 Findings] [[paper](https://arxiv.org/abs/2502.14382)]

- "When Benchmarks Talk: Re-Evaluating Code LLMs with Interactive Feedback" [2025-02] [ACL 2025 Findings] [[paper](https://arxiv.org/abs/2502.18413)]

- "LLM4EFFI: Leveraging Large Language Models to Enhance Code Efficiency and Correctness" [2025-02] [[paper](https://arxiv.org/abs/2502.18489)]

- "Multi-Turn Code Generation Through Single-Step Rewards" [2025-02] [ICML 2025] [[paper](https://arxiv.org/abs/2502.20380)]

- "ConvCodeWorld: Benchmarking Conversational Code Generation in Reproducible Feedback Environments" [2025-02] [ICLR 2025] [[paper](https://arxiv.org/abs/2502.19852)]

- "Teaching Your Models to Understand Code via Focal Preference Alignment" [2025-03] [EMNLP 2025] [[paper](https://arxiv.org/abs/2503.02783)]

- "debug-gym: A Text-Based Environment for Interactive Debugging" [2025-03] [[paper](https://arxiv.org/abs/2503.21557)]

- "CodeIF-Bench: Evaluating Instruction-Following Capabilities of Large Language Models in Interactive Code Generation" [2025-03] [[paper](https://arxiv.org/abs/2503.22688)]

- "CodeFlowBench: A Multi-turn, Iterative Benchmark for Complex Code Generation" [2025-04] [[paper](https://arxiv.org/abs/2504.21751)]

- "Use Property-Based Testing to Bridge LLM Code Generation and Validation" [2025-06] [[paper](https://arxiv.org/abs/2506.18315)]

- "CodeAssistBench (CAB): Dataset & Benchmarking for Multi-turn Chat-Based Code Assistance" [2025-07] [[paper](https://arxiv.org/abs/2507.10646)]

- "SR-Eval: Evaluating LLMs on Code Generation under Stepwise Requirement Refinement" [2025-09] [[paper](https://arxiv.org/abs/2509.18808)]

- "Benchmarking Correctness and Security in Multi-Turn Code Generation" [2025-10] [[paper](https://arxiv.org/abs/2510.13859)]

### 3.5 Frontend Navigation

- "MarkupLM: Pre-training of Text and Markup Language for Visually-rich Document Understanding" [2021-10] [ACL 2022] [[paper](https://arxiv.org/abs/2110.08518)]

- "WebKE: Knowledge Extraction from Semi-structured Web with Pre-trained Markup Language Model" [2021-10] [CIKM 2021] [[paper](https://dl.acm.org/doi/abs/10.1145/3459637.3482491)]

- "WebGPT: Browser-assisted question-answering with human feedback" [2021-12] [[paper](https://arxiv.org/abs/2112.09332)]

- "CM3: A Causal Masked Multimodal Model of the Internet" [2022-01] [[paper](https://arxiv.org/abs/2201.07520)]

- "DOM-LM: Learning Generalizable Representations for HTML Documents" [2022-01] [[paper](https://arxiv.org/abs/2201.10608)]

- "WebFormer: The Web-page Transformer for Structure Information Extraction" [2022-02] [WWW 2022] [[paper](https://arxiv.org/abs/2202.00217)]

- "A Dataset for Interactive Vision-Language Navigation with Unknown Command Feasibility" [2022-02] [ECCV 2022] [[paper](https://arxiv.org/abs/2202.02312)]

- "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents" [2022-07] [NeurIPS 2022] [[paper](https://arxiv.org/abs/2207.01206)]

- "Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding" [2022-10] [ICML 2023] [[paper](https://arxiv.org/abs/2210.03347)]

- "Understanding HTML with Large Language Models" [2022-10] [EMNLP 2023 findings] [[paper](https://arxiv.org/abs/2210.03945)]

- "WebUI: A Dataset for Enhancing Visual UI Understanding with Web Semantics" [2023-01] [CHI 2023] [[paper](https://arxiv.org/abs/2301.13280)]

- "Mind2Web: Towards a Generalist Agent for the Web" [2023-06] [NeurIPS 2023] [[paper](https://arxiv.org/abs/2306.06070)]

- "A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis", [2023-07] [ICLR 2024] [[paper](https://arxiv.org/abs/2307.12856)]

- "WebArena: A Realistic Web Environment for Building Autonomous Agents" [2023-07] [[paper](https://arxiv.org/abs/2307.13854)]

- "CogAgent: A Visual Language Model for GUI Agents" [2023-12] [[paper](https://arxiv.org/abs/2312.08914)]

- "GPT-4V(ision) is a Generalist Web Agent, if Grounded" [2024-01] [[paper](https://arxiv.org/abs/2401.01614)]

- "WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models" [2024-01] [[paper](https://arxiv.org/abs/2401.13919)]

- "WebLINX: Real-World Website Navigation with Multi-Turn Dialogue" [2024-02] [[paper](https://arxiv.org/abs/2402.05930)]

- "OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web" [2024-02] [[paper](https://arxiv.org/abs/2402.17553)]

- "AutoWebGLM: Bootstrap And Reinforce A Large Language Model-based Web Navigating Agent" [2024-04] [[paper](https://arxiv.org/abs/2404.03648)]

- "WILBUR: Adaptive In-Context Learning for Robust and Accurate Web Agents" [2024-04] [[paper](https://arxiv.org/abs/2404.05902)]

- "AutoCrawler: A Progressive Understanding Web Agent for Web Crawler Generation" [2024-04] [[paper](https://arxiv.org/abs/2404.12753)]

- "GUICourse: From General Vision Language Models to Versatile GUI Agents" [2024-06] [[paper]