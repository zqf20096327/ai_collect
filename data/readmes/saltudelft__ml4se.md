# Machine Learning for Software Engineering
![GitHub last commit](https://img.shields.io/github/last-commit/saltudelft/ml4se)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/mir-am/0d2ee0d88d518e1a916aef1f8c77a666/raw/ml4se-paper-no.json)

This repository contains a curated list of papers, PhD theses, datasets, and tools that are devoted to research on Machine Learning for Software Engineering. The papers are organized into popular research areas so that researchers can find recent papers and state-of-the-art approaches easily.

Please feel free to send a pull request to add papers and relevant content that are not listed here.

## Content
- [Papers](#papers)
    - [Type Inference](#type-inference)
    - [Code Completion](#code-completion)
    - [Code Generation](#code-generation)
    - [Code Summarization](#code-summarization)
    - [Code Embeddings/Representation](#code-embeddingsrepresentation)
    - [Code Changes/Editing](#code-changesediting)
    - [Code Comments](#code-comments)
    - [Bug/Vulnerability Detection](#bugvulnerability-detection)
    - [Source Code Modeling](#source-code-modeling)
    - [Program Repair](#program-repair)
    - [Program Translation](#program-translation)
    - [Program Analysis](#program-analysis)
    - [Software Testing](#software-testing)
    - [Code Clone Detection](#code-clone-detection)
    - [Code Search](#code-search)
    - [Code Language Models](#code-language-models)
    - [Code Review](#code-review)
    - [Code Documentation](#code-documentation)
    - [Empirical Studies](#empirical-studies)
    - [Surveys](#surveys)
    - [Misc](#misc)
- [PhD Theses](#phd-theses)
- [Talks](#talks)
- [Datasets](#datasets)
- [Tools](#tools)
    - [Source Code Analysis \& Processing](#source-code-analysis--processing)
    - [Machine Learning](#machine-learning)
    - [Code de-duplication](#code-de-duplication)
    - [Misc](#misc-1)
- [Research Groups](#research-groups)
- [Venues](#venues)
    - [Conferences](#conferences)
    - [Journals](#journals)

# Papers

## Type Inference

- **Concrete Type Inference for Code Optimization using Machine Learning with SMT Solving** (2023), OOPSLA'23, Ye, Fangke, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3622825)
- **Learning Type Inference for Enhanced Dataflow Analysis** (2023), ESORICS'23, Seidel, Lukas, et al. [[pdf]](https://arxiv.org/pdf/2310.00673) 
- **Domain Knowledge Matters: Improving Prompts with Fix Templates for Repairing Python Type Errors** (2023), ICSE'24, Peng, Yun, et al. [[pdf]](https://arxiv.org/pdf/2306.01394)
- **DeepInfer: Deep Type Inference from Smart Contract Bytecode** (2023), ESEC/FSE '23, Zhao, Kunsong, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3611643.3616343)
- **Statistical Type Inference for Incomplete Programs** (2023), ESEC/FSE '23, Peng, Yaohui, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3611643.3616283)
- **DeMinify: Neural Variable Name Recovery and Type Inference** (2023), ESEC/FSE '23, Li, Yi, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3611643.3616368)
- **Learning Type Inference for Enhanced Dataflow Analysis** (2023), ESORICS '23, Seidel, L. & Baker Effendi, D., et al. [[pdf]](https://arxiv.org/pdf/2310.00673.pdf)
- **FQN Inference in Partial Code by Prompt-tuned Language Model of Code** (2023), TOSEM journal, Huang, Qing, et al. 
- **Generative Type Inference for Python** (2023), ASE'23, Peng, Yun, et al. [[pdf]](https://arxiv.org/pdf/2307.09163)
- **Type Prediction With Program Decomposition and Fill-in-the-Type Training** (2023), arxiv, Cassano, Federico, et al. [[pdf]](https://arxiv.org/pdf/2305.17145)
- **TypeT5: Seq2seq Type Inference using Static Analysis** (2023), ICLR'23, Wei, Jiayi, et al. [[pdf]](https://arxiv.org/pdf/2303.09564)
- **Do Machine Learning Models Produce TypeScript Types that Type Check?** (2023), arxiv, Yee, M., and Arjun G. [[pdf]](https://arxiv.org/pdf/2302.12163)
- **Cross-Domain Evaluation of a Deep Learning-Based Type Inference System** (2022), arxiv, Gruner, Bernd, et al. [[pdf]](https://arxiv.org/pdf/2208.09189) [[code]](https://gitlab.com/dlr-dw/type-inference)
- **Learning To Predict User-Defined Types** (2022), TSE'22, Jesse, Keven, et al. [[pdf]](https://www.cs.ucdavis.edu/~devanbu/DiverseTyper_TSE.pdf)
- **Recovering Container Class Types in C++ Binaries** (2022), CGO'22, Wang, Xudong, et al.
- **Finding the Dwarf: Recovering Precise Types from WebAssembly Binaries** (2022), PLDI'22, Lehmann, Daniel and Pradel, Michael [[pdf]](https://dlehmann.eu/publications/WasmTypePrediction-pldi2022.pdf)
- **Type4Py: Practical Deep Similarity Learning-Based Type Inference for Python** (2022), ICSE'22, Mir, Amir, et al. [[pdf]](https://arxiv.org/pdf/2101.04470.pdf)[[code]](https://github.com/saltudelft/type4py)
- **Static Inference Meets Deep Learning: A Hybrid Type Inference Approach for Python** (2022), ICSE'22, Peng, Yun, et al. [[pdf]](https://arxiv.org/pdf/2105.03595)

<details><summary><b>Older:</b></i></summary>
<div>

- **StateFormer: Fine-grained Type Recovery from Binaries Using Generative State Modeling** (2021), FSE'21, Pei, Kexin, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3468264.3468607)[[code]](https://github.com/CUMLSec/stateformer)
- **Type Inference as Optimization** (2021), NeurIPS'21 AIPLANS,  Pandi, Irene Vlassi, et al. [[pdf]](https://openreview.net/pdf?id=yHYZaQ0Zvml)
- **SimTyper: Sound Type Inference for Ruby using Type Equality Prediction** (2021), OOPSLA'21, Kazerounian, Milod, et al.
- **Learning type annotation: is big data enough?** (2021), FSE 2021, Jesse, Kevin, et al. [[pdf]](https://www.cs.ucdavis.edu/~devanbu/typebert_esec_fse_.pdf)[[code]](https://github.com/typebert/typebert)
- **Cross-Lingual Adaptation for Type Inference** (2021), arxiv 2021, Li, Zhiming, et al. [[pdf]](https://arxiv.org/pdf/2107.00157)
- **PYInfer: Deep Learning Semantic Type Inference for Python Variables** (2021), arxiv 2021, Cui, Siwei, et al. [[pdf]](https://arxiv.org/pdf/2106.14316)
- **Advanced Graph-Based Deep Learning for Probabilistic Type Inference** (2020), arxiv 2020, Ye, Fangke, et al. [[pdf]](https://arxiv.org/pdf/2009.05949.pdf)
- **Typilus: Neural Type Hints** (2020), PLDI 2020, Allamanis, Miltiadis, et al. [[pdf]](https://arxiv.org/pdf/2004.10657)[[code]](https://github.com/typilus/typilus)
- **LambdaNet: Probabilistic Type Inference using Graph Neural Networks** (2020), arxiv 2020, Wei, Jiayi, et al. [[pdf]](https://arxiv.org/pdf/2005.02161)
- **TypeWriter: Neural Type Prediction with Search-based Validation** (2019), arxiv 2019, Pradel, Michael, et al. [[pdf]](https://arxiv.org/pdf/1912.03768)
- **NL2Type: Inferring JavaScript Function Types from Natural Language Information** (2019), ICSE 2019, Malik, Rabee S., et al. [[pdf]](http://software-lab.org/publications/icse2019_NL2Type.pdf)[[code]](https://github.com/sola-da/NL2Type)
- **Deep Learning Type Inference** (2018), ESEC/FSE 2018, Hellendoorn, Vincent J., et al. [[pdf]](http://vhellendoorn.github.io/PDF/fse2018-j2t.pdf)[[code]](https://github.com/DeepTyper/DeepTyper)
- **Python Probabilistic Type Inference with Natural Language Support** (2016), FSE 2016, Xu, Zhaogui, et al.
- **Predicting Program Properties from “Big Code”** (2015) ACM SIGPLAN 2015, Raychev, Veselin, et al. [[pdf]](https://files.sri.inf.ethz.ch/website/papers/jsnice15.pdf)

</div>
</details>

## Code Completion

- **EXECREPOBENCH: Multi-level Executable Code Completion Evaluation** (2025), arxiv, Yang, Jian, et al. [[pdf]](https://arxiv.org/pdf/2412.11990)
- **ContextModule: Improving Code Completion via Repository-level Contextual Information** (2025), arxiv, Guan, Zhanming, et al. [[pdf]](https://arxiv.org/pdf/2412.08063)
- **REPOFUSE: Repository-Level Code Completion with Fused Dual Context** (2024), arxiv, Liang, Ming, et al. [[pdf]](https://arxiv.org/pdf/2402.14323)
- **Non-Autoregressive Line-Level Code Completion** (2024), TOSEM, Liu, Fang, et al.
- **IRCoCo: Immediate Rewards-Guided Deep Reinforcement Learning for Code Completion** (2024), arxiv, Li, Bolun, et al. [[pdf]](https://arxiv.org/pdf/2401.16637)
- **Language Models for Code Completion: A Practical Evaluation** (2024), ICSE'24, Izadi et al. [[pdf]](https://arxiv.org/pdf/2402.16197)
- **Context Composing for Full Line Code Completion** (2024), IDE'24, Semenkin et al. [[pdf]](https://arxiv.org/pdf/2402.09230)  
- **De-Hallucinator: Iterative Grounding for LLM-Based Code Completion** (2024), arxiv, Eghbali, A., & Pradel, M. [[pdf]](https://arxiv.org/pdf/2401.01701)
- **When Neural Code Completion Models Size up the Situation: Attaining Cheaper and Faster Completion through Dynamic Model Inference** (2024), ICSE'24, Sun, Zhensu, et al. [[pdf]](https://arxiv.org/abs/2401.09964v1) 
- **CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion** (2023), NeurIPS'23, Ding, Yangruibo, et al. [[pdf]](https://arxiv.org/abs/2310.11248)
- **Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context** (2023), NeurIPS'23, Agrawal, Lakshya A., et al. [[pdf]](https://openreview.net/pdf?id=qPUbKxKvXq)
- **Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation** (2023), NeurIPS'23, Liu, Jiawei, et al. [[pdf]](https://arxiv.org/abs/2305.01210)
- **Domain Adaptive Code Completion via Language Models and Decoupled Domain Databases** (2023), arxiv, Tang, Ze, et al. [[pdf]](https://arxiv.org/pdf/2308.09313)
- **RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems** (2023), arxiv, Liu, T., et al. [[pdf]](https://arxiv.org/pdf/2306.03091)
- **A Static Evaluation of Code Completion by Large Language Models** (2023), arxiv, Ding, Hantian, et al. [[pdf]](https://arxiv.org/pdf/2306.03203)
- **Large Language Models of Code Fail at Completing Code with Potential Bugs** (2023), NeurIPS'23, Dinh, Tuan, et al. [[pdf]](https://arxiv.org/pdf/2306.03438)
- **RepoFusion: Training Code Models to Understand Your Repository** (2023), arxiv, Shrivastava, Disha, et al., [[pdf]](https://arxiv.org/pdf/2306.10998)
- **LongCoder: A Long-Range Pre-trained Language Model for Code Completion** (2023), ICML'23, Guo, Daya, et al. [[pdf]](https://arxiv.org/pdf/2306.14893)
- **R-U-SURE? Uncertainty-Aware Code Suggestions By Maximizing Utility Across Random User Intents** (2023), arxiv, Johnson, Daniel D, et al. [[pdf]](https://arxiv.org/pdf/2303.00732) 
- **Optimized Tokenization Process for Open-Vocabulary Code Completion: An Empirical Study** (2023), EASE'23, Hussain, Yasir, et al.
- **Enriching Source Code with Contextual Data for Code Completion Models: An Empirical Study** (2023), MSR'23, van Dam, Tim, et al. [[pdf]](https://arxiv.org/pdf/2304.12269)
- **RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation** (2023), arxiv, Zhang, Fengji, et al. [[pdf]](https://arxiv.org/pdf/2303.12570)

<details><summary><b>Older:</b></i></summary>
<div>

- **COCOMIC: ✿✿✿✿ Code ✿✿✿✿ Completion By Jointly Modeling In-file and ✿✿Cross-file Context** (2022), Ding, Yangruibo, et al. [[pdf]](https://arxiv.org/pdf/2212.10007)
- **Boosting source code suggestion with self-supervised Transformer Gated Highway** (2022), JSS, Hussain, Yasir, et al.
- **Syntax-Aware On-the-Fly Code Completion** (2022), arxiv, Takerngsaksiri, W., et al. [[pdf]](https://arxiv.org/pdf/2211.04673)
- **Learning to Prevent Profitless Neural Code Completion** (2022), arxiv, Sun, Z., et al. [[pdf]](https://arxiv.org/pdf/2209.05948)
- **All You Need Is Logs: Improving Code Completion by Learning from Anonymous IDE Usage Logs** (2022), arxiv, Bibaev, Vitaliy, et al. [[pdf]](https://arxiv.org/pdf/2205.10692.pdf)
- **CodeFill: Multi-token Code Completion by Jointly Learning from Structure and Naming Sequences** (2022), ICSE'22, Izadi, Maliheh, et al. [[pdf]](https://arxiv.org/pdf/2202.06689.pdf) [[code]](https://github.com/saltudelft/codefill)
- **Code Completion by Modeling Flattened Abstract Syntax Trees as Graphs** (2021), AAAI'21, Wang, Yanlin, et al. [[pdf]](https://www.aaai.org/AAAI21Papers/AAAI-1654.WangY.pdf)
- **Code Prediction by Feeding Trees to Transformers** (2021), ICSE'21, Kim, Seohyun, et al. [[pdf]](https://arxiv.org/pdf/2003.13848)
- **Fast and Memory-Efficient Neural Code Completion** (2020), arxiv 2020, Svyatkovskoy, Alexey, et al. [[pdf]](https://arxiv.org/pdf/2004.13651)
- **Pythia: AI-assisted Code Completion System** (2019), KDD'19, Svyatkovskiy, Alexey, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3292500.3330699)
- **Code Completion with Neural Attention and Pointer Networks** (2018), arxiv 2018, Li, Jian, et al. [[pdf]](https://arxiv.org/pdf/1711.09573)

</div>
</details>

## Code Generation

- **QualityFlow: An Agentic Workflow for Program Synthesis Controlled by LLM Quality Checks** (2025), arxiv, Hu, Yaojie, et al. [[pdf]](https://arxiv.org/pdf/2501.17167)
- **Towards Advancing Code Generation with Large Language Models: A Research Roadmap** (2025), arxiv, Jin, Haolin, et al. [[pdf]](https://arxiv.org/pdf/2501.11354)
- **CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging** (2025), arxiv, Islam, M. A. et al. [[pdf]](https://arxiv.org/pdf/2502.05664)
- **Large Language Models for Code Generation: The Practitioners’ Perspective** (2025), arxiv, Rasheed, Zeeshan, et al. [[pdf]](https://arxiv.org/pdf/2501.16998)
- **Enhancing Code Generation for Low-Resource Languages: No Silver Bullet** (2025), ICPC'25, Giagnorio, A., et al. [[pdf]](https://arxiv.org/pdf/2501.19085)
- **How Efficient is LLM-Generated Code? A Rigorous & High-Standard Benchmark** (2025), ICLR'25, Qiu, Ruizhong, et al. [[pdf]](https://q-rz.github.io/static/iclr25/iclr25-enamel-paper.pdf)
- **COFFE: A Code Efficiency Benchmark for Code Generation** (2025), FSE'25, Peng, Yun, et al. [[pdf]](https://arxiv.org/pdf/2502.02827)
- **Process-Supervised Reinforcement Learning for Code Generation** (2025), arxiv, Ye, Yufan, et al. [[pdf]](https://arxiv.org/pdf/2502.01715)
- **ACECODER: Acing Coder RL via Automated Test-Case Synthesis** (2025), arxiv, Zeng, Huaye, et al. [[pdf]](https://arxiv.org/pdf/2502.01718)
- **FairCode: Evaluating Social Bias of LLMs in Code Generation** (2025), arxiv, Du, Yongkang, et al. [[pdf]](https://arxiv.org/pdf/2501.05396?)
- **Revisit Self-Debugging with Self-Generated Tests for Code Generation** (2025), arxiv, Chen, Xiancai, et al. [[pdf]](Revisit Self-Debugging with Self-Generated Tests for Code Generation)
- **Chain of Grounded Objectives: Bridging Process and Goal-oriented Prompting for Code Generation** (2025), arxiv, Yeo, Sangyeop, et al. [[pdf]](https://arxiv.org/pdf/2501.13978)
- **Extracting the Essence and Discarding the Dross: Enhancing Code Generation with Contrastive Execution Feedback** (2025), arxiv, Zhang, X., & Yang, Q. [[pdf]](https://aclanthology.org/2025.coling-main.704.pdf)
- **Case2Code: Scalable Synthetic Data for Code Generation** (2025), arxiv, Shao, Yunfan, et al. [[pdf]](https://aclanthology.org/2025.coling-main.733.pdf)
- **Effective LLM-Driven Code Generation with PYTHONESS** (2025), arxiv, Levin, Kyla H., et al. [[pdf]](https://arxiv.org/pdf/2501.02138)
- **Knowledge-Aware Code Generation with Large Language Models** (2024), ICPC'24, Huang et al. [[pdf]](https://arxiv.org/pdf/2401.15940.pdf)
- **Helping LLMs Improve Code Generation Using Feedback from Testing and Static Analysis** (2025), arxiv, Dolcetti, Greta, et al. [[pdf]](https://arxiv.org/pdf/2412.14841)
- **CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation** (2025), arxiv, Pan, Ruwei, et al. [[pdf]](https://arxiv.org/pdf/2501.07811)
- **EpiCoder: Encompassing Diversity and Complexity in Code Generation** (2025), arxiv, Wang, Yaoxiang, et al. [[pdf]](https://arxiv.org/pdf/2501.04694)
- **Automated Program Refinement: Guide and Verify Code Large Language Model with Refinement Calculus** (2025), arxiv, Cai, Yufan, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3704905)
- **CGP-Tuning: Structure-Aware Soft Prompt Tuning for Code Vulnerability Detection** (2025), arxiv, Feng, Ruijun, et al. [[pdf]](https://arxiv.org/pdf/2501.04510)
- **Unseen Horizons: Unveiling the Real Capability of LLM Code Generation Beyond the Familiar** (2025), ICSE'25, Zhang, Yuanliang, et al. [[pdf]](https://arxiv.org/pdf/2412.08109)
- **CODEELO: Benchmarking Competition-level Code Generation of LLMs with Human-comparable Elo Ratings** (2025), arxiv, Quan, Shanghaoran, et al. [[pdf]](https://arxiv.org/pdf/2501.01257)
- **Effectiveness of symmetric metamorphic relations on validating the stability of code generation LLM** (2025), JSS, Chan, P. Y. P. et al.
- **SPDZCoder: Teaching LLMs to Synthesize Privacy Computing Code without Massive Training Data** (2024), arxiv, Dong, Xiaoning, et al. [[pdf]](https://arxiv.org/pdf/2501.00363)
- **HumanEval Pro and MBPP Pro: Evaluating Large Language Models on Self-invoking Code Generation** (2024), arxiv, Yu, Zhaojian, et al. [[pdf]](https://arxiv.org/pdf/2412.21199)
- **The Impact of Prompt Programming on Function-Level Code Generation** (2024), arxiv, Khojah, Ranim, et al. [[pdf]](https://arxiv.org/pdf/2412.20545)
- **Aligning Crowd-Sourced Human Feedback for Reinforcement Learning on Code Generation by Large Language Models** (2024), TBD Journal, Wong, M. F. et al.
- **A-CodGen: A Repository-Level Code Generation Framework for Code Reuse With Local-Aware, Global-Aware, and Third-Party-Library-Aware** (2024), TSE, Liao, Dianshu, et al. 
- **Tree-of-Code: A Tree-Structured Exploring Framework for End-to-End Code Generation and Execution in Complex Task Handling** (2024), arxiv, Ni, Ziyi, et al. [[pdf]](https://arxiv.org/pdf/2412.15305)
- **PPM: Automated Generation of Diverse Programming Problems for Benchmarking Code Generation Models** (2024), arxiv, Chen, Simin, et al. [[pdf]](https://arxiv.org/pdf/2401.15545)
- **Ocassionally Secure: A Comparative Analysis of Code Generation Assistants** (2024), arxiv, Elgedawy et al. [[pdf]](https://arxiv.org/pdf/2402.00689.pdf) 
- **StepCoder: Improve Code Generation with Reinforcement Learning from Compiler Feedback** (2024), arxiv, [[pdf]](https://arxiv.org/pdf/2402.01391v1.pdf)
- **Grounding Data Science Code Generation with Input-Output Specifications** (2024), arxiv, Wen, Yeming, et al. [[pdf]](https://arxiv.org/pdf/2402.08073)
- **MPIrigen: MPI Code Generation through Domain-Specific Language Models** (2024), arxiv, Schneider, Nadav, et al. [[pdf]](https://arxiv.org/pdf/2402.09126)
- **Instruction Tuning for Secure Code Generation** (2024), arxiv, He, Jingxuan, et al. [[pdf]](https://arxiv.org/pdf/2402.09497)
- **Make Every Move Count: LLM-based High-Quality RTL Code Generation Using MCTS** (2024), arxiv, DeLorenzo, Matthew, et al. [[pdf]](https://arxiv.org/pdf/2402.03289)
- **ARKS: Active Retrieval in Knowledge Soup for Code Generation** (2024), arxiv, Su, Hongjin, et al. [[pdf]](https://arxiv.org/pdf/2402.12317)
- **Test-Driven Development for Code Generation** (2024), arxiv, Mathews, N. S., & M. Nagappan [[pdf]](https://arxiv.org/pdf/2402.13521)
- **RRGcode: Deep hierarchical search-based code generation** (2024), JSS, Gou, Qianwen, et al.
- **LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step** (2024), arxiv, Zhong et al. [[pdf]](https://arxiv.org/pdf/2402.16906)
- **Ansible Lightspeed: A Code Generation Service for IT Automation** (2024), arxiv, Sahoo, Priyam, et al. [[pdf]](https://arxiv.org/pdf/2402.17442)
- **DeceptPrompt: Exploiting LLM-driven Code Generation via Adversarial Natural Language Instructions** (2024), arxiv, Wu et al. [[pdf]](https://arxiv.org/pdf/2312.04730)
- **Chain-of-Thought in Neural Code Generation: From and For Lightweight Language Models** (2024), arxiv, Yang, Guang, et al. [[pdf]](https://arxiv.org/pdf/2312.05562)
- **DevEval: Evaluating Code Generation in Practical Software Projects** (2024), arxiv, Li, Jia, et al. [[pdf]](https://arxiv.org/pdf/2401.06401.pdf)
- **Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation** (2024), arxiv, Wang, Chong, et al. [[pdf]](https://arxiv.org/pdf/2401.06391v1.pdf)
- **CODEAGENT: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges** (2024), arxiv, Zhang, Kechi, et al. [[pdf]](https://arxiv.org/pdf/2401.07339.pdf)
- **On the Reliability and Explainability of Language Models for Program Generation** (2024), TOSEM, Liu, Yue, et al. [[pdf]](https://arxiv.org/abs/2302.09587)
- **AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation** (2024), arxiv, Huang, Dong, et al.  [[pdf]](https://arxiv.org/pdf/2312.13010)
- **Dynamic Retrieval-Augmented Generation** (2024), arxiv, Shapkin et al. [[pdf]](https://arxiv.org/pdf/2312.08976.pdf)
- **Test-Case-Driven Programming Understanding in Large Language Models for Better Code Generation** (2024), arxiv, Tian, Z., & Chen, J. [[pdf]](https://arxiv.org/pdf/2309.16120)


<details><summary><b>Older:</b></i></summary>
<div>

- **Context-Aware Code Generation Framework for Code Repositories: Local, Global, and Third-Party Library Awareness** (2023), arxiv, Liao, Dianshu, et al. [[pdf]](https://arxiv.org/pdf/2312.05772)
- **CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules** (2024), ICLR'24, Le, Hung, et al. [[pdf]](https://arxiv.org/pdf/2310.08992)
- **Bias Testing and Mitigation in LLM-based Code Generation** (2024), arxiv, Huang, Dong, et al. [[pdf]](https://arxiv.org/pdf/2309.14345)
- **Magicoder: Source Code Is All You Need** (2023), arxiv, Wei, Yuxiang, et al. [[pdf]](https://arxiv.org/pdf/2312.02120.pdf)
- **Structured Chain-of-Thought Prompting for Code Generation** (2023), arxiv, Li, Jia, et al. [[pdf]](https://lj2lijia.github.io/papers/SCoT_Preprint.pdf)
- **Evaluating In-Context Learning of Libraries for Code Generation** (2023), arxiv, Patel, Arkil, et al. [[pdf]](https://arxiv.org/pdf/2311.09635)
- **Neural Rankers for Code Generation via Inter-Cluster Modeling** (2023), arxiv, To, Hung Quoc et al. [[pdf]](https://arxiv.org/pdf/2311.03366)
- **Enhancing Large Language Models for Secure Code Generation: A Dataset-driven Study on Vulnerability Mitigation** (2023), ICSE'24, Wang, Jiexin, et al. [[pdf]](https://arxiv.org/pdf/2310.16263)
- **Automatic Unit Test Data Generation and Actor-Critic Reinforcement Learning for Code Synthesis** (2023), arxiv, Gorinski, P. J., et al. [[pdf]](https://arxiv.org/pdf/2310.13669)
- **ClarifyGPT: Empowering LLM-based Code Generation with Intention Clarification** (2023), arxiv, Mu, Fangwen, et al. [[pdf]](https://arxiv.org/pdf/2310.10996)
- **Large Language Model-Aware In-Context Learning for Code Generation** (2023), arxiv, Li, Jia, et al. [[pdf]](https://arxiv.org/pdf/2310.09748)
- **From Misuse to Mastery: Enhancing Code Generation with Knowledge-Driven AI Chaining** (2023), ASE'23, Ren, Xiaoxue, et al. [[pdf]](https://arxiv.org/pdf/2309.15606)
- **Exploring Parameter-Efficient Fine-Tuning Techniques for Code Generation with Large Language Models** (2023), arxiv, Weyssow, Martin, et al. [[pdf]](https://arxiv.org/pdf/2308.10462)
- **CodeGen4Libs: A Two-Stage Approach for Library-Oriented Code Generation** (2023), arxiv, Liu, Mingwei, et al. [[pdf]](https://www.researchgate.net/profile/Mingwei-Liu-4/publication/373192571_CodeGen4Libs_A_Two-Stage_Approach_for_Library-Oriented_Code_Generation/links/64ded6fbcaf5ff5cd0c39162/CodeGen4Libs-A-Two-Stage-Approach-for-Library-Oriented-Code-Generation.pdf)
- **Is Model Attention Aligned with Human Attention?: An Empirical Study on LLMs for Code Generation** (2023), arxiv, Kou, Bonan, et al. [[pdf]](https://arxiv.org/pdf/2306.01220)
- **Demystifying GPT Self-Repair for Code Generation** (2023), arxiv, Olausson, Theo X., et al. [[pdf]](https://arxiv.org/pdf/2306.09896)
- **Exploring Continual Learning for Code Generation Models** (2023), arxiv, Yadav, Prateek, et al. [[pdf]](https://arxiv.org/pdf/2307.02435)
- **CodePrompt: Task-Agnostic Prefix Tuning for Program and Language Generation** (2023), ACL'23, Choi, Y., & Lee, J. H. [[pdf]](https://aclanthology.org/2023.findings-acl.325.pdf)
- **Aligning Offline Metrics and Human Judgments of Value for Code Generation Models** (2023), ACL'23, Dibia, Victor, et al. [[pdf]](https://aclanthology.org/2023.findings-acl.540.pdf)
- **RLTF: Reinforcement Learning from Unit Test Feedback** (2023), arxiv, Liu, Jiate, et al. [[pdf]](https://arxiv.org/pdf/2307.04349)
- **A Lightweight Framework for High-Quality Code Generation** (2023), arxiv, Siddiq, M. L., et al. [[pdf]](https://arxiv.org/pdf/2307.08220)
- **Large Language Models for Code: Security Hardening and Adversarial Testing** (2023), ICML'23 workshop, He, J., & Vechev, M. [[pdf]](https://openreview.net/pdf?id=Km1XyJJVpS)
- **Reinforcement Learning for Syntax-Guided Synthesis** (2023), arxiv, Parsert, J., and E. Polgreen [[pdf]](https://arxiv.org/pdf/2307.09564)
- **Refining ChatGPT-Generated Code: Characterizing and Mitigating Code Quality Issues**, arxiv, Liu, Yue, et al. [[pdf]](https://arxiv.org/pdf/2307.12596)
- **ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis**, arxiv, Shi, Kensen, et al. [[pdf]](https://arxiv.org/pdf/2307.13883)
- **Private-Library-Oriented Code Generation with Large Language Models** (2023), arxiv, Zan, Daoguang, et al. [[pdf]](https://arxiv.org/pdf/2307.15370)
- **LLM is Like a Box of Chocolates: the Non-determinism of ChatGPT in Code Generation** (2023), arxiv, Ouyang, Shuyin, et al. [[pdf]](https://arxiv.org/pdf/2303.00732)
- **No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT** (2023), arxiv, Liu, Zhijie, et al. [[pdf]](https://arxiv.org/pdf/2308.04838)
- **Think Outside the Code: Brainstorming Boosts Large Language Models in Code Generation** (2023), arxiv, Li, Xin-Ye, et al. [[pdf]](https://arxiv.org/pdf/2305.10679) 
- **Neural Machine Translation for Code Generation** (2023), arxiv, KC, Dharma, and Clayton T. M. [[pdf]](https://arxiv.org/pdf/2305.13504)
- **CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Evaluations on HumanEval-X** (2023), arxiv, Zheng, Qinkai, et al. [[pdf]](https://arxiv.org/pdf/2303.17568)
- **Towards Enhancing In-Context Learning for Code Generation** (2023), arxiv, Li, Jia, et al. [[pdf]](https://arxiv.org/pdf/2303.17780)
- **Knowledge Transfer for Pseudo-code Generation from Low Resource Programming Language** (2023), arxiv, Sontakke, Ankita, et al. [[pdf]](https://arxiv.org/pdf/2303.09062)
- **MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation** (2023), TSE, Paul, Rishov, et al.  
- **Self-collaboration Code Generation via ChatGPT** (2023), arxiv, Dong, Yihong, et al. [[pdf]](https://arxiv.org/pdf/2304.07590)
- **Greener yet Powerful: Taming Large Code Generation Models with Quantization** (2023), arxiv, Wei, Xiaokai, et al. [[pdf]](https://arxiv.org/pdf/2303.05378.pdf)
- **A Syntax-Guided Multi-Task Learning Approach for Turducken-Style Code Generation** (2023), arxiv, Yang, Guang, et al. [[pdf]](https://arxiv.org/pdf/2303.05061)
- **WikiCoder: Learning to Write Knowledge-Powered Code** (2023), arxiv, Matricon, Théo, et al. [[pdf]](https://arxiv.org/pdf/2303.08574)
- **Self-planning Code Generation with Large Language Model** (2023), arxiv, Jiang, Xue, et al. [[pdf]](https://arxiv.org/pdf/2303.06689)
- **Systematically Finding Security Vulnerabilities in Black-Box Code Generation Models.** (2023), arxiv, Hajipour, Hossein, et al. [[pdf]](https://arxiv.org/pdf/2302.04012)
- **Exploring Data Augmentation for Code Generation Tasks** (2023), arxiv, C., Pinzhen, and G. Lampouras [[pdf]](https://arxiv.org/pdf/2302.03499)
- **Controlling Large Language Models to Generate Secure and Vulnerable Code** (2023), arxiv, He, J., and M. Vechev [[pdf]](https://arxiv.org/pdf/2302.05319)
- **SKCODER: A Sketch-based Approach for Automatic Code Generation** (2023), arxiv, Li, Jia, et al. [[pdf]](https://arxiv.org/pdf/2302.06144)
- **LEVER: Learning to Verify Language-to-Code Generation with Execution** (2023), arxiv, Ni, Ansong, et al. [[pdf]](https://arxiv.org/pdf/2302.08468)
- **CodeScore: Evaluating Code Generation by Learning Code Execution** (2023), arxiv, Dong, Yihong, et al. [[pdf]](https://arxiv.org/pdf/2301.09043)
- **Program Generation from Diverse Video Demonstrations** (2023), arxiv, Manchin, Anthony, et al. [[pdf]](https://arxiv.org/pdf/2302.00178) 
- **Execution-based Code Generation using Deep Reinforcement Learning** (2023), arxiv, Shojaee, Parshin, et al. [[pdf]](https://arxiv.org/pdf/2301.13816)
- **SantaCoder: don't reach for the stars!** (2023), arxiv, Allal, Loubna Ben, et al. [[pdf]](https://arxiv.org/pdf/2301.03988.pdf)
- **Exploring and Evaluating Personalized Models for Code Generation**, FSE'22, Zlotchevski, Andrei, et al.
- **Natural Language to Code Generation in Interactive Data Science Notebooks** (2022), arxiv, Yin, Pengcheng, et al. [[pdf]](https://arxiv.org/pdf/2212.09248)
- **Asking Clarification Questions for Code Generation in General-Purpose Programming Language** (2022), arxiv, Li, Haau-Sing, et al. [[pdf]](https://arxiv.org/pdf/2212.09885)
- **ExploitGen: Template-augmented exploit code generation based on CodeBERT** (2022), JSS journal, Yang, Guang, et al.
- **Explicit Knowledge Transfer for Weakly-Supervised Code Generation** (2022), arxiv, Azerbayev, Zhangir, et al. [[pdf]](https://arxiv.org/pdf/2211.16740)
- **Program Generation from Diverse Video Demonstrations** (2022), Manchin123, Anthony, et al. [[pdf]](https://bmvc2022.mpi-inf.mpg.de/1039.pdf)
- **Coder Reviewer Reranking for Code Generation** (2022), arxiv, Zhang, Tianyi, et al. [[pdf]](https://arxiv.org/pdf/2211.16490)
- **Execution-based Evaluation for Data Science Code Generation Models** (2022), arxiv, Huang, Junjie, et al. [[pdf]](https://arxiv.org/pdf/2211.09374)
- **Multi-lingual Evaluation of Code Generation Models** (2022), arxiv, Athiwaratkun, Ben, et al. [[pdf]](https://arxiv.org/pdf/2210.14868)[[code]](https://github.com/amazon-science/mbxp-exec-eval)
- **DocCoder: Generating Code by Retrieving and Reading Docs** (2022), arxiv, Zhou, Shuyan, et al. [[pdf]](https://arxiv.org/pdf/2207.05987)
- **Compilable Neural Code Generation with Compiler Feedback** (2022), ACL'22, Wang, Xin, et al. [[pdf]](https://aclanthology.org/2022.findings-acl.2.pdf)
- **T5QL: Taming language models for SQL generation** (2022), arxiv, Arcadinho, S., et al. [[pdf]](https://arxiv.org/pdf/2209.10254)
- **Incorporating Domain Knowledge through Task Augmentation for Front-End JavaScript Code Generation** (2022), arxiv, Shen, Sijie, et al. [[pdf]](https://arxiv.org/pdf/2208.10091)
- **Language Models Can Teach Themselves to Program Better** (2022), arxiv, Haluptzok, Patrick, et al. [[pdf]](https://arxiv.org/pdf/2207.14502)
- **DocCoder: Generating Code by Retrieving and Reading Docs** (2022), arxiv, Zhou, Shuyan, et al. [[pdf]](https://arxiv.org/pdf/2207.05987)
- **CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning** (2022), arxiv, Le, Hung, et al. [[pdf]](https://arxiv.org/pdf/2207.01780)
- **Repository-Level Prompt Generation for Large Language Models of Code** (2022), arxiv, Shrivastava, Disha, et al. [[pdf]](https://arxiv.org/pdf/2206.12839)
- **CERT: Continual Pre-Training on Sketches for Library-Oriented Code Generation** (2022), arxiv, Zan, Daoguang, et al. [[pdf]](https://arxiv.org/pdf/2206.06888)
- **NatGen: Generative pre-training by “Naturalizing” source code** (2022), FSE'22, Chakraborty, Saikat, et al. [[pdf]](https://arxiv.org/pdf/2206.07585)
- **StructCoder: Structure-Aware Transformer for Code Generation** (2022), arxiv, Tipirneni, Sindhu, et al. [[pdf]](https://arxiv.org/pdf/2206.05239)
- **Compilable Neural Code Generation with Compiler Feedback** (2022), arxiv 2022, Wang, Xin, et al. [[pdf]](https://arxiv.org/pdf/2203.05132.pdf)
- **Predictive Synthesis of API-Centric Code** (2022), arxiv 2022, Nam, Daye, et al. [[pdf]](https://arxiv.org/pdf/2201.03758.pdf)
- **Code Prediction by Feeding Trees to Transformers** (2020), arxiv 2020, Kim, Seohyun, et al. [[pdf]](https://arxiv.org/pdf/2003.13848)
- **TreeGen: A Tree-Based Transformer Architecture for Code Generation** (2019), arxiv 2019, Zhu, Qihao, et al. [[pdf]](https://arxiv.org/abs/1911.09983)
- **A Parallel Corpus of Python Functions and Documentation Strings for Automated Code Documentation and Code Generation** (2017), arxiv 2017, Barone, Antonio V. M., et al. [[pdf]](https://arxiv.org/pdf/1707.02275)

</div>
</details>

## Code Summarization

- **Optimizing Datasets for Code Summarization: Is Code-Comment Coherence Enough?** (2025), arxiv, Vitale, Antonio, et al. [[pdf]](https://arxiv.org/pdf/2502.07611)
- **Rethinking-based Code Summarization with Chain of Comments** (2025), COLING'25, Cao, Liuwen, et al. [[pdf]](https://aclanthology.org/2025.coling-main.204.pdf)
- **Resource-Efficient & Effective Code Summarization** (2025), arxiv, Afrin, Saima, et al. [[pdf]](https://arxiv.org/pdf/2502.03617)
- **Context-aware code summarization with multi-relational graph neural network** (2025), ASE Journal, Wang, Yanlin, et al.
- **Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs** (2025), arxiv, Dhulshette, N. et al. [[pdf]](https://arxiv.org/pdf/2501.07857)
- **Transforming Code Understanding: Clustering-Based Retrieval for Improved Summarization in Domain-Specific Languages** (2025), arxiv, Gain, Baban, et al.  [[pdf]](https://aclanthology.org/2025.coling-industry.47.pdf)
- **Evaluating LLMs for Arabic Code Summarization: Challenges and Insights from GPT-4** (2024), arxiv, Aljohani, Ahmed, et al. [[pdf]](https://easychair.org/publications/preprint/2z1C/open)
- **Can Large Language Models Serve as Evaluators for Code Summarization?** (2024), arxiv, Wu, Yang, et al. [[pdf]](https://arxiv.org/pdf/2412.01333)
- **A Prompt Learning Framework for Source Code Summarization** (2024), TOSEM, Sun et al.
- **Evaluating Code Summarization Techniques: A New Metric and an Empirical Characterization** (2024), arxiv, Mastropaolo, Antonio, et al. [[pdf]](https://arxiv.org/pdf/2312.15475)
- **SparseCoder: Identifier-Aware Sparse Transformer for File-Level Code Summarization** (2024), arxiv, Wang et al. [[pdf]](https://arxiv.org/pdf/2401.14727.pdf)
- **Towards Summarizing Code Snippets Using Pre-Trained Transformers** (2024), ICPC'24, Mastropaolo et al. [[pdf]](https://arxiv.org/pdf/2402.00519.pdf)
- **Do Machines and Humans Focus on Similar Code? Exploring Explainability of Large Language Models in Code Summarization** (2024), ICPC'24, Li, Jiliang, et al. [[pdf]](https://arxiv.org/pdf/2402.14182)
- **EyeTrans: Merging Human and Machine Attention for Neural Code Summarization** (2024), arxiv, Zhang, Yifan, et al. [[pdf]](https://arxiv.org/pdf/2402.14096)
- **Deep Is Better? An Empirical Comparison of Information Retrieval and Deep Learning Approaches to Code Summarization** (2024), TOSEM, Zhu, Tingwei, et al. 
- **Binary Code Summarization: Benchmarking ChatGPT/GPT-4 and Other Large Language Models** (2023), arxiv, Jin, Xin, et al. [[pdf]](https://arxiv.org/pdf/2312.09601)
- **Revisiting File Context for Source Code Summarization** (2023), arxiv, Bansal, Aakash, et al. [[pdf]](https://arxiv.org/pdf/2309.02326)
- **Distilled GPT for Source Code Summarization** (2023), arxiv, Su, C. Y., & McMillan, C. [[pdf]](https://arxiv.org/pdf/2308.14731)
- **An data augmentation method for source code summarization** (2023), Journal of Neurocomputing, Song, Zixuan, et al.
- **Multilingual Adapter-based Knowledge Aggregation on Code Summarization for Low-Resource Languages** (2023), arxiv, Saberi, Iman et al. [[pdf]](https://arxiv.org/pdf/2307.07854)
- **Statement-based Memory for Neural Source Code Summarization** (2023), arxiv, Bansal, Aakash, et al. [[pdf]](https://arxiv.org/pdf/2307.11709)
- **Tram: A Token-level Retrieval-augmented Mechanism for Source Code Summarization** (2023), arxiv, Ye, Tong, et al. [[pdf]](https://arxiv.org/pdf/2305.11074)
- **Automatic Code Summarization via ChatGPT: How Far Are We?** (2023), arxiv, Sun, Weisong, et al. 
- **Function Call Graph Context Encoding for Neural Source Code Summarization** (2023), TSE, Bansal, Aakash, et al.
- **Label Smoothing Improves Neural Source Code Summarization** (2023), arxiv, Haque, Sakib, et al. [[pdf]](https://arxiv.org/pdf/2303.16178)
- **Demystifying What Code Summarization Models Learned** (2023), arxiv, Wang, Yu, and Ke Wang. [[pdf]](https://arxiv.org/pdf/2303.02333)
- **CoSS: Leveraging Statement Semantics for Code Summarization** (2023), TSE, Shi, Chaochen, et al.
- **An Extensive Study of the Structure Features in Transformer-based Code Semantic Summarization** (2023), RG, Yang, Kang, et al. [[pdf]](https://www.researchgate.net/profile/Shangwen-Wang/publication/369273643_An_Extensive_Study_of_the_Structure_Features_in_Transformer-based_Code_Semantic_Summarization/links/641313ce92cfd54f84060e2f/An-Extensive-Study-of-the-Structure-Features-in-Transformer-based-Code-Semantic-Summarization.pdf)
- **Interpretation-based Code Summarization** (2023), arxiv, Geng, Mingyang, et al. [[pdf]](https://www.researchgate.net/profile/Shangwen-Wang/publication/368755660_Interpretation-based_Code_Summarization/links/63f842890d98a97717b27fb8/Interpretation-based-Code-Summarization.pdf)
- **Towards Retrieval-Based Neural Code Summarization: A Meta-Learning Approach** (2023), TSE, Zhou, Ziyi, et al.
- **CLG-Trans: Contrastive Learning for Code Summarization via Graph Attention-based Transformer** (2023), SCP journal, Zeng, Jianwei, et al.

<details><summary><b>Older:</b></i></summary>
<div>

- **ClassSum: a deep learning model for class-level code summarization** (2022), Springer NCA, Li, Mingchen, et al. [[code]](https://github.com/classsum/ClassSum)
- **Boosting Code Summarization by Embedding Code Structures** (2022), COLING'22, Son, Jikyoeng, et al. [[pdf]](https://aclanthology.org/2022.coling-1.521.pdf)
- **Low-Resources Project-Specific Code Summarization** (2022), ASE'22, Xie, Rui, et al. [[pdf]](https://arxiv.org/pdf/2210.11843)
- **Few-shot training LLMs for project-specific code-summarization** (2022), arxiv, A., Toufique, and P. Devanbu. [[pdf]](https://arxiv.org/pdf/2207.04237)
- **Are We Building on the Rock? On the Importance of Data Preprocessing for Code Summarization** (2022), FSE'22, Shi, Lin, et al. [[pdf]](https://arxiv.org/pdf/2207.05579)
- **Learning code summarization from a small and local dataset** (2022), arxiv, Ahmed, Toufique, and Devanbu, P. [[pdf]](https://arxiv.org/pdf/2206.00804)
- **Modeling Hierarchical Syntax Structure with Triplet Position for Source Code Summarization** (2022), ACL'22, Guo, Juncai, et al. [[pdf]](https://aclanthology.org/2022.acl-long.37.pdf)
- **AST-Trans: Code Summarization with Efficient Tree-Structured Attention** (2022), ICSE'22, Tang, Ze, et al. [[pdf]](http://lichuanyi.info/files/papers/2022-Ze%20Tang-AST-Trans%20ICSE2022.pdf)
- **GypSum: Learning Hybrid Representations for Code Summarization** (2022), ICPC'22, Wang, Yu, et al. [[pdf]](https://arxiv.org/pdf/2204.12916)
- **M2TS: Multi-Scale Multi-Modal Approach Based on Transformer for Source Code Summarization** (2022), ICPC'22, Gao, Yuexiu and Lyu, Chen [[pdf]](https://arxiv.org/pdf/2203.09707)
- **Project-Level Encoding for Neural Source Code Summarization of Subroutines** (2021), ICPC'21, Bansal, Aakash, et al. [[pdf]](https://arxiv.org/pdf/2103.11599)
- **Code Structure Guided Transformer for Source Code Summarization** (2021), arxiv 2021, Gao, Shuzheng, et al. [[pdf]](https://arxiv.org/pdf/2104.09340)
- **Source Code Summarization Using Attention-Based Keyword Memory Networks** (2020), IEEE BigComp 2020, Choi, YunSeok, et al.
- **A Transformer-based Approach for Source Code Summarization** (2020), arxiv 2020, Ahmad, Wasi Uddin, et al. [[pdf]](https://arxiv.org/pdf/2005.00653)
- **Learning to Represent Programs with Graphs** (2018), ICLR'18, Allamanis, Miltiadis, et al. [[pdf]](https://arxiv.org/pdf/1711.00740)
- **A Convolutional Attention Network for Extreme Summarization of Source Code** (2016), ICML 2016, Allamanis, Miltiadis, et al. [[pdf]](http://www.jmlr.org/proceedings/papers/v48/allamanis16.pdf)

</div>
</details>

## Code Embeddings/Representation

- **Transformer-based code model with compressed hierarchy representation** (2025), EMSE, Zhang, Kechi, et al.
- **OpTrans: enhancing binary code similarity detection with function inlining re-optimization** (2024), EMSE, Sha, Zihan, et al. 
- **CLAP: Learning Transferable Binary Code Representations with Natural Language Supervision** (2024),ISSTA'24, Wang, Hao, et al. [[pdf]](https://arxiv.org/pdf/2402.16928.pdf) [[code]](https://github.com/Hustcw/CLAP)
- **CONCORD: Towards a DSL for Configurable Graph Code Representation** (2024), arxiv, Saad, M., & Sharma, T. [[pdf]](https://arxiv.org/pdf/2401.17967)
- **Code Representation Learning at Scale** (2024), ICLR'24, Zhang et al. [[pdf]](https://arxiv.org/pdf/2402.01935v1.pdf)
- **Structured Code Representations Enable Data-Efficient Adaptation of Code Language Models** (2024), arxiv, Agarwal, Mayank, et al. [[pdf]](https://arxiv.org/pdf/2401.10716)
- **Pass-Tuning: Towards Structure-Aware Parameter-Efficient Tuning for Code Representation Learning** (2023), EMNLP'23, Chen, Nuo, et al. [[pdf]](https://aclanthology.org/2023.findings-emnlp.42.pdf)
- **TransformCode: A Contrastive Learning Framework for Code Embedding via Subtree transformation** (2023), arxiv, Xian, Zixiang, et al. [[pdf]](https://arxiv.org/pdf/2311.08157)
- **CoCoAST: Representing Source Code via Hierarchical Splitting and Reconstruction of Abstract Syntax Trees** (2023), EMSE, Shi, Ensheng, et al. 
- **Language Agnostic Code Embeddings** (2023), arxiv, Utpala, Saiteja et al. [[pdf]](https://arxiv.org/pdf/2310.16803)
- **Code Representation Pre-training with Complements from Program Executions** (2023), arxiv, Huang, Jiabo, et al. [[pdf]](https://arxiv.org/pdf/2309.09980)
- **FAIR: Flow Type-Aware Pre-Training of Compiler Intermediate Representations** (2023), ICSE'24, Niu, Changan, et al. [[pdf]](https://arxiv.org/pdf/2309.04828.pdf) 
- **CombTransformers: Statement-Wise Transformers for Statement-Wise Representations** (2023), TSE, Bertolotti, F., & Cazzola, W.
- **kTrans: Knowledge-Aware Transformer for Binary Code Embedding** (2023), arxiv, Wenyu, Zhu, et al. [[pdf]](https://arxiv.org/pdf/2308.12659.pdf)[[code]](https://github.com/Learner0x5a/kTrans-release)
- **TransCoder: Towards Unified Transferable Code Representation Learning Inspired by Human Skills** (2023), arxiv, Sun, Qiushi, et al. [[pdf]](https://arxiv.org/pdf/2306.07285)
- **CodeGrid: A Grid Representation of Code** (2023), ISSTA'23, Kaboré, Abdoul Kader, et al.
- **Symmetry-Preserving Program Representations for Learning Code Semantics** (2023), arxiv, Pei, Kexin, et al. [[pdf]](https://arxiv.org/pdf/2308.03312)
- **PERFOGRAPH: A Numerical Aware Program Graph Representation for Performance Optimization and Program Analysis** (2023), NeurlIPS'23, TehraniJamsaz, Ali, et al. [[pdf]](https://arxiv.org/pdf/2306.00210)
- **xASTNN: Improved Code Representations for Industrial Practice** (2023), arxiv, Xu, Zhiwei, et al. [[pdf]](https://arxiv.org/pdf/2303.07104)
- **Toward Interpretable Graph Tensor Convolution Neural Network for Code Semantics Embedding** (2023), TOSEM, Yang, Jia, et al.

<details><summary><b>Older:</b></i></summary>
<div>

- **jTrans: Jump-Aware Transformer for Binary Code Similarity Detection** (2022), ISSTA, Hao, Wang, et al. [[pdf]](https://arxiv.org/pdf/2205.12713.pdf)[[code]](https://github.com/vul337/jTrans)
- **Trex: Learning Approximate Execution Semantics from Traces for Binary Function Similarity** (2022), TSE, Pei, Kexin, et al. [[pdf]](https://arxiv.org/pdf/2012.08680.pdf)[[code]](https://github.com/CUMLSec/trex)
- **Practical Binary Code Similarity Detection with BERT-based Transferable Similarity Learning** (2022), ACSAC'22, Ahn, Sunwoo, et al.
- **CLAWSAT: Towards Both Robust and Accurate Code Models** (2022), arxiv, Jia, Jinghan, et al. [[pdf]](https://arxiv.org/pdf/2211.11711)
- **sem2vec: Semantics-Aware Assembly Tracelet Embedding** (2022), TSE, Wang, Huaijin, et al.
- **COMBO: Pre-Training Representations of Binary Code Using Contrastive Learning** (2022), arxiv, Zhang, Yifan, et al. [[pdf]](https://arxiv.org/pdf/2210.05102.pdf)
- **Soft-Labeled Contrastive Pre-training for Function-level Code Representation** (2022), arxiv, Li, Xiaonan, et al. [[pdf]](https://arxiv.org/pdf/2210.09597) 
- **A Tree-structured Transformer for Program Representation Learning** (2022), arxiv, Wang, Wenhan, et al. [[pdf]](https://arxiv.org/pdf/2208.08643)
- **What does Transformer learn about source code?** (2022), arxiv, Zhang, Kechi, et al. [[pdf]](https://arxiv.org/pdf/2207.08466)
- **Diet Code is Healthy: Simplifying Programs for Pre-Trained Models of Code** (2022), arxiv, Zhang, Zhaowei, et al. [[pdf]](https://arxiv.org/pdf/2206.14390)
- **MetaTPTrans: A Meta Learning Approach for Multilingual Code Representation Learning** (2022), arxiv, Pian, Weiguo, et al. [[pdf]](https://arxiv.org/pdf/2206.06460)
- **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** (2022), ACL'22, Ding, Yangruibo, et al. [[pdf]](https://aclanthology.org/2022.acl-long.436/)
- **Towards Learning Generalizable Code Embeddings using Task-agnostic Graph Convolutional Networks** (2022), TOSEM, Ding, Zishuo, et al.
- **Learning to Represent Programs with Code Hierarchies** (2022), arxiv, Nguyen, Minh and Nghi DQ Bui, [[pdf]](https://arxiv.org/pdf/2205.15479)
- **CV4Code: Sourcecode Understanding via Visual Code Representations** (2022), arxiv, Shi, Ruibo, et al. [[pdf]](https://arxiv.org/pdf/2205.08585)
- **Hyperbolic Representations of Source Code** (2022), AAAI'22, Khan, Raiyan, et al. [[pdf]](https://assets.amazon.science/55/d9/58097f0d41b886269b30e5c68522/hyperbolic-representations-of-source-code.pdf)
- **Unified Abstract Syntax Tree Representation Learning for Cross-Language Program Classification** (2022), ICPC'22, Wang, Kesu, et al. [[pdf]](https://arxiv.org/pdf/2205.00424)
- **Hierarchical Semantic-Aware Neural Code Representation** (2022), JSS'22, Jiang, Yuan, et al.
- **CODE-MVP: Learning to Represent Source Code from Multiple Views with Contrastive Pre-Training** (2022), arxiv 2022, Wang, Xin, et al. [[pdf]](https://arxiv.org/pdf/2205.02029)
- **Hierarchical Heterogeneous Graph Attention Network for Syntax-Aware Summarization** (2022), AAAI'22, Song, Z., and King, I., [[pdf]](https://www.aaai.org/AAAI22Papers/AAAI-6812.SongZ.pdf)
- **Unleashing the Power of Compiler Intermediate Representation to Enhance Neural Program Embeddings** (2022), ICSE'22, Li, Zongjie, et al. [[pdf]](https://arxiv.org/pdf/2204.09191.pdf)
- **XCode: Towards Cross-Language Code Representation with Large-Scale Pre-Training** (2022), TOSEM'22, Lin, Zehao, et al.
- **Fold2Vec: Towards a Statement Based Representation of Code for Code Comprehension** (2022), TOSEM'22, Bertolotti, Francesco and Cazzola, Walter
- **HELoC: Hierarchical Contrastive Learning of Source Code Representation** (2022), ICPC'22, Wang, Xiao, et al. [[pdf]](https://arxiv.org/pdf/2203.14285)
- **Multi-View Graph Representation for Programming Language Processing: An Investigation into Algorithm Detection** (2022), AAAI'22, Long, Tin et al. [[pdf]](https://www.aaai.org/AAAI22Papers/AAAI-928.LongT.pdf)
- **UniXcoder: Unified Cross-Modal Pre-training for Code Representation** (2022), arxiv 2022, Guo, Daya, et al. [[pdf]](https://arxiv.org/pdf/2203.03850)
- **SPT-Code: Sequence-to-Sequence Pre-Training for Learning Source Code Representations** (2022), ICSE'22, Niu, Changan, et al. [[pdf]](https://arxiv.org/pdf/2201.01549.pdf)
- **GraphCode2Vec: Generic Code Embedding via Lexical and Program Dependence Analyses** (2022), MSR'22, Ma, Wei, et al.
- **OSCAR: How could Neural Networks understand Programs?** (2021), ICML'21, Peng, Dinglan, et al. [[pdf]](http://proceedings.mlr.press/v139/peng21b/peng21b.pdf)
- **PROGRAML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations** (2021), ICML'21, Cummins, Chris, et al. [[pdf]](http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf)
- **CoTexT: Multi-task Learning with Code-Text Transformer** (2021), arxiv, Phan, Long, et al. [[pdf]](https://arxiv.org/pdf/2105.08645)
- **TreeCaps: Tree-Based Capsule Networks for Source Code Processing** (2021), AAAI'21, Bui, Nghi DQ, et al. [[pdf]](https://www.aaai.org/AAAI21Papers/AAAI-9746.BuiNDQ.pdf) [[code]](https://github.com/bdqnghi/treecaps)
- **Language-Agnostic Representation Learning of Source Code from Structure and Context** (2021), ICLR'21, Zügner, Daniel, et al. [[pdf]](https://arxiv.org/pdf/2103.11318)
- **IR2Vec: LLVM IR Based Scalable Program Embeddings** (2020), TACO journal, VenkataKeerthy, S., et al. 
- **Compiler-Based Graph Representations for Deep Learning Models of Code** (2020), CC'20, Brauckmann, Alexander, et al.
- **Learning and Evaluating Contextual Embedding of Source Code** (2020), ICML 2020, Kanade, Aditya, et al. [[pdf]](http://proceedings.mlr.press/v119/kanade20a/kanade20a.pdf)
- **Learning Semantic Program Embeddings with Graph Interval Neural Network** (2020), OOPSLA'20, Wang, Yu, et al.
- **Contrastive Code Representation Learning** (2020), arxiv 2020, Jain, Paras, et al. [[pdf]](https://arxiv.org/pdf/2007.04973.pdf)
- **SCELMo: Source Code Embeddings from Language Models** (2020), arxiv 2020, Karampatsis, Rafael-Michael, et al. [[pdf]](https://arxiv.org/pdf/2004.13214)
- **code2vec: Learning Distributed Representations of Code** (2019), ACM POPL 2019, Alon, Uri, et al. [[pdf]](http://www.cs.technion.ac.il/~mbs/publications/code2vec-popl19.pdf)
- **COSET: A Benchmark for Evaluating Neural Program Embeddings** (2019), arxiv 2019, Wang, Ke, et al. [[pdf]](https://arxiv.org/pdf/1905.11445)
- **A Literature Study of Embeddings on Source Code** (2019), arxiv 2019, Chen, Zimin, et al. [[pdf]](https://arxiv.org/pdf/1904.03061)
- **code2seq: Generating Sequences from Structured Representations of Code** (2018), arxiv 2018, Alon, Uri, et al. [[pdf]](https://arxiv.org/pdf/1808.01400)
- **Neural Code Comprehension: A Learnable Representation of Code Semantics** (2018), NIPS 2018, Ben-Nun, Tal, et al. [[pdf]](http://papers.nips.cc/paper/7617-neural-code-comprehension-a-learnable-representation-of-code-semantics.pdf)
- **Convolutional Neural Networks over Tree Structures for Programming Language Processing** (2016), AAAI'16, Mou, Lili, et al. [[pdf]](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/11775/11735)


</div>
</details>

## Code Changes/Editing

- **Suggesting Code Edits in Interactive Machine Learning Notebooks Using Large Language Models** (2025), arxiv, Jin, B. et al. [[pdf]](https://arxiv.org/pdf/2501.09745)
- **You Don’t Have to Say Where to Edit! jLED – Joint Learning to Localize and Edit Source Code** (2025), TOSEM, Pian, Weiguo, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3712187)
- **A Retrospective of ChangeDistiller: Tree Differencing for Fine-Grained Source Code Change Extraction** (2025), TSE, Fluri, Beat, et al.
- **Large Language Model Critics for Execution-Free Evaluation of Code Changes** (2025), arxiv, Yadavally, Aashish, et al. [[pdf]](https://arxiv.org/pdf/2501.16655)
- **Can It Edit? Evaluating the Ability of Large Language Models to Follow Code Editing Instructions** (2023), arxiv, Cassano, Federico, et al. [[pdf]](https://arxiv.org/pdf/2312.12450)
- **Grace: Language Models Meet Code Edits** (2023), FSE'23, Gupta, Priyanshu, et al.
- **AdaptivePaste: Intelligent Copy-Paste in IDE** (2023), FSE'23, Liu, Xiaoyu, et al.
- **Learning to Represent Patches** (2023), ICSE'24, Tang, Xunzhu, et al. [[pdf]](https://arxiv.org/pdf/2308.16586)
- **InstructCoder: Empowering Language Models to Edit Code** (2023), arxiv, Hu, Qisheng, et al. [[pdf]](https://openreview.net/pdf?id=islVqaCzfa)
- **CCBERT: Self-Supervised Code Change Representation Learning** (2023), ICSME'23, Zhou, Xin, et al. [[pdf]](https://arxiv.org/pdf/2309.15474)
- **Automated Code Editing with Search-Generate-Modify** (2023), arxiv, Liu, Changshu, et al. [[pdf]](https://arxiv.org/pdf/2306.06490)
- **Multilingual Code Co-Evolution Using Large Language Models** (2023), arxiv, Zhang, Jiyang, et al. [[pdf]](https://arxiv.org/pdf/2307.14991)
- **Coeditor: Leveraging Contextual Changes for Multi-round Code Auto-editing** (2023), arxiv, Wei, Jiayi, et al. [[pdf]](https://arxiv.org/pdf/2305.18584)
- **CCT5: A Code-Change-Oriented Pre-Trained Model** (2023), arxiv, Lin, Bo, et al. [[pdf]](https://arxiv.org/pdf/2305.10785)
- **GrACE: Generation using Associated Code Edits** (2023), arxiv, Gupta, Priyanshu, et al. [[pdf]](https://arxiv.org/pdf/2305.14129)
- **Slice-Based Code Change Representation Learning** (2023), arxiv, Zhang, Fengyi, et al. [[pdf]](https://chenbihuan.github.io/paper/saner23-zhang-ccs2vec.pdf)
- **Towards Generating Functionally Correct Code Edits from Natural Language Issue Descriptions** (2023), arxiv, Fakhoury, Sarah, et al. [[pdf]](https://arxiv.org/pdf/2304.03816)
- **CCRep: Learning Code Change Representations via Pre-Trained Code Model and Query Back** (2023), arxiv, Liu, Zhongxin, et al. [[pdf]](https://arxiv.org/pdf/2302.03924)
- **CoditT5: Pretraining for Source Code and Natural Language Editing** (2022), ASE 2022, Jiyang, Zhang, et al. [[pdf]](https://arxiv.org/abs/2208.05446)
- **Commit2Vec: Learning Distributed Representations of Code Changes** (2021), SN Computer Science, Lozoya, Rocío Cabrera, et al.
- **CODIT: Code Editing with Tree-Based Neural Models** (2020), TSE 2020, Chakraborty, Saikat, et al.
- **On learning meaningful code changes via neural machine translation** (2019), ICSE 2019, Tufano, Michele, et al.

## Code Comments

- **CupCleaner: A Data Cleaning Approach for Comment Updating** (2023), arxiv, Liang, Qingyuan, et al. [[pdf]](https://arxiv.org/pdf/2308.06898)
- **Large Language Models are Few-Shot Summarizers: Multi-Intent Comment Generation via In-Context Learning** (2023), ICSE'24, Geng, Mingyang, et al. [[pdf]](https://www.researchgate.net/profile/Shangwen-Wang/publication/370228019_Large_Language_Models_are_Few-Shot_Summarizers_Multi-Intent_Comment_Generation_via_In-Context_Learning/links/648aeb559605ba270e45bf26/Large-Language-Models-are-Few-Shot-Summarizers-Multi-Intent-Comment-Generation-via-In-Context-Learning.pdf)
- **Snippet Comment Generation Based on Code Context Expansion** (2023), arxiv, GUO, HANYANG, et al.
- **An Empirical Study on Using Large Language Models for Multi-Intent Comment Generation** (2023), arxiv, Geng, Mingyang, et al. [[pdf]](https://arxiv.org/pdf/2304.11384)
- **An Intra-Class Relation Guided Approach for Code Comment Generation** (2023), EACL'23, Wang, Zhenni, et al. [[pdf]](https://aclanthology.org/2023.findings-eacl.97.pdf)
- **APIContext2Com: Code Comment Generation by Incorporating Pre-Defined API Documentation** (2023), arxiv, Shahbazi, R., and Fard F. [[pdf]](https://arxiv.org/pdf/2303.01645)
- **Developer-Intent Driven Code Comment Generation** (2023), arxiv, Mu, Fangwen, et al. [[pdf]](https://arxiv.org/pdf/2302.07055)
- **ALSI-Transformer: Transformer-Based Code Comment Generation With Aligned Lexical and Syntactic Information** (2023), IEEE Access, Park, Youngmi, et al.

## Bug/Vulnerability Detection

- **LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights** (2025), arxiv, Sheng, Ze, et al. [[pdf]](https://arxiv.org/pdf/2502.07049)
- **Large Language Models for In-File Vulnerability Localization Can Be “Lost in the End”** (2025), FSE'25, Sovrano, F. et al. [[pdf]](https://arxiv.org/pdf/2502.06898)
- **HAFix: History-Augmented Large Language Models for Bug Fixing** (2025), arxiv, Shi, Yu, et al. [[pdf]](https://arxiv.org/pdf/2501.09135)
- **Fault Localization via Fine-tuning Large Language Models with Mutation Generated Stack Traces** (2025), arxiv, Jambigi, Neetha, et al. [[pdf]](https://arxiv.org/pdf/2501.18005)
- **Software Vulnerability Detection Using LLM: Does Additional Information Help?** (2025), WAITI'24, Shimmi, Samiha, et al. [[pdf]](https://web.mit.edu/ha22286/www/papers/WAITI24.pdf)
- **APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching** (2025), USENIX'25, [[pdf]](https://arxiv.org/pdf/2408.13597)
- **COSMosFL: Ensemble of Small Language Models for Fault Localisation** (2025), LLM4Code'25, Cho, Hyunjoon, et al. [[pdf]](https://arxiv.org/abs/2502.02908)
- **Automating the Detection of Code Vulnerabilities by Analyzing GitHub Issues** (2025), arxiv, Cipollone, Daniele, et al. [[pdf]](https://arxiv.org/pdf/2501.05258)
- **Evaluating Large Language Models in Vulnerability Detection Under Variable Context Windows** (2025), arxiv, Lin, J., & Mohaisen, D. [[pdf]](https://arxiv.org/pdf/2502.00064)
- **Structuring Semantic-Aware Relations Between Bugs and Patches for Accurate Patch Evaluation** (2025), Journal of Software, Zhao, Lingxiao, et al.
- **OrcaLoca: An LLM Agent Framework for Software Issue Localization** (2025), arxiv, Yu, Zhongming, et al. [[pdf]](https://arxiv.org/pdf/2502.00350)
- **Directional Diffusion-Style Code Editing Pre-training** (2025), arxiv, Liang, Qingyuan, et al. [[pdf]](https://arxiv.org/pdf/2501.12079)
- **REPOAUDIT: An Autonomous LLM-Agent for Repository-Level Code Auditing** (2025), arxiv, Guo, Jinyao, et al. [[pdf]](https://arxiv.org/pdf/2501.18160)
- **PATCH: Empowering Large Language Model with Programmer-Intent Guidance and Collaborative-Behavior Simulation for Automatic Bug Fixing** (2025), arxiv, Zhang, Yuwei, et al. [[pdf]](https://arxiv.org/pdf/2501.16149)
- **One-for-All Does Not Work! Enhancing Vulnerability Detection by Mixture-of-Experts (MoE)** (2025), FSE'25, Yang, Xu, et al. [[pdf]](https://arxiv.org/pdf/2501.16454)
- **Code Change Intention, Development Artifact and History Vulnerability: Putting Them Together for Vulnerability Fix Detection by LLM** (2025), arxiv, Yang, Xu, et al. [[pdf]](https://arxiv.org/pdf/2501.14983)
- **HAFix: History-Augmented Large Language Models for Bug Fixing** (2025), arxiv, Shi, Yu, et al. [[pdf]](https://arxiv.org/pdf/2501.09135)
- **Vulnerability Detection in Popular Programming Languages with Language Models** (2025), arxiv, Dolcetti, Greta, et al. [[pdf]](https://arxiv.org/pdf/2412.15905)
- **Investigating Large Language Models for Code Vulnerability Detection: An Experimental Study** (2025), arxiv, Jiang, Xuefeng, et al. [[pdf]](https://arxiv.org/pdf/2412.18260)
- **LLM4CVE: Enabling Iterative Automated Vulnerability Repair with Large Language Models** (2025), arxiv, Fakih, Mohamad, et al. [[pdf]](https://arxiv.org/pdf/2501.03446)
- **The Impact of Input Order Bias on Large Language Models for Software Fault Localization** (2024), arxiv, Nakhla Rafi, Md, et al. [[pdf]](https://arxiv.org/pdf/2412.18750)
- **Enhancing IR-based Fault Localization using Large Language Models** (2024), arxiv, Shao, S., & Yu, T. [[pdf]](https://arxiv.org/pdf/2412.03754)
- **Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks** (2024), ICSE'24, Liu et al. [[pdf]](https://arxiv.org/pdf/2402.00657.pdf)
- **JITGNN: A deep graph neural network framework for Just-In-Time bug prediction** (2024), JSS, Keshavarz, H., and G. Rodríguez-Pérez
- **DeepCode AI Fix: Fixing Security Vulnerabilities with Large Language Models** (2024), arxiv, Berabi, Berkay, et al. [[pdf]](https://arxiv.org/pdf/2402.13291)
- **Analyzing source code vulnerabilities in the D2A dataset with ML ensembles and C-BERT** (2024), EMSE, Pujar, Saurabh, et al. 
- **Chain-of-Thought Prompting of Large Language Models for Discovering and Fixing Software Vulnerabilities** (2024), arxiv, Nong, Yu, et al. [[pdf]](https://arxiv.org/pdf/2402.17230)
- **Code Security Vulnerability Repair Using Reinforcement Learning with Large Language Models** (2024), arxiv, N. T. Islam & P. Najafirad [[pdf]](https://arxiv.org/pdf/2401.07031.pdf)
- **Vision Transformer Inspired Automated Vulnerability Repair** (2024), TOSEM, Fu, Michael, et al.
- **Can Large Language Models Identify And Reason About Security Vulnerabilities? Not Yet** (2023), arxiv, Ullah, Saad, et al. [[pdf]](https://arxiv.org/pdf/2312.12575)
- **BinGo: Identifying Security Patches in Binary Code with Graph Representation Learning** (2023), ASIACC'24, He, Xu, et al. [[pdf]](https://arxiv.org/pdf/2312.07921)
- **Commit-Level, Neural Vulnerability Detection and Assessment** (2023), FSE'23, Li, Yi, et al. 
- **Learning Defect Prediction from Unrealistic Data** (2023), arxiv, Alrashedy, Kamel, et al. [[pdf]](https://arxiv.org/html/2311.00931v2)
- **SparseCoder: Advancing Source Code Analysis with Sparse Attention and Learned Token Pruning** (2023), arxiv, Yang, Xueqi, et al. [[pdf]](https://arxiv.org/pdf/2310.07109)
- **How Far Have We Gone in Vulnerability Detection Using Large Language Models** (2023), arxiv, Zeyu, Gao, et al. [[pdf]](https://arxiv.org/pdf/2311.12420.pdf)
- **Pre-training Code Representation with Semantic Flow Graph for Effective Bug Localization** (2023), arxiv, Du, Y., & Yu, Z. [[pdf]](https://arxiv.org/pdf/2308.12773)
- **PrAIoritize: Learning to Prioritize Smart Contract Bugs and Vulnerabilities** (2023), arxiv, Soud, Majd, et al. [[pdf]](https://arxiv.org/pdf/2308.11082)
- **Transformer-based Vulnerability Detection in Code at EditTime: Zero-shot, Few-shot, or Fine-tuning?** (2023), arxiv, Chan, Aaron, et al. [[pdf]](https://arxiv.org/pdf/2306.01754)
- **LIVABLE: Exploring Long-Tailed Classification of Software Vulnerability Types** (2023), arxiv, Wen, Xin-Cheng, et al. [[pdf]](https://arxiv.org/pdf/2306.06935)
- **Learning to Quantize Vulnerability Patterns and Match to Locate Statement-Level Vulnerabilities** (2023), arxiv, Fu, Michael, et al. [[pdf]](https://arxiv.org/pdf/2306.06109)
- **CPVD: Cross Project Vulnerability Detection Based on Graph Attention Network and Domain Adaptation** (2023), TSE, Zhang, Chunyong, et al. 
- **FLAG: Finding Line Anomalies (in code) with Generative AI** (2023), arxiv, Ahmad, Baleegh, et al. [[pdf]](https://arxiv.org/pdf/2306.12643)
- **A Novel Approach to Identify Security Controls in Source Code** (2023), arxiv, Okutan, Ahmet, et al. [[pdf]](https://arxiv.org/pdf/2307.05605)
- **Limits of Machine Learning for Automatic Vulnerability Detection** (2023), arxiv, Risse, N., & Böhme, M. [[pdf]](https://arxiv.org/pdf/2306.17193)
- **Detecting Condition-Related Bugs with Control Flow Graph Neural Network** (2023), ISTTA'23, Zhang, Jian, et al.
- **A New Era in Software Security: Towards Self-Healing Software via Large Language Models and Formal Verification** (2023), arxiv, Charalambous, Yiannis, et al. [[pdf]](https://arxiv.org/pdf/2305.14752)
- **An Unbiased Transformer Source Code Learning with Semantic Vulnerability Graph** (2023), arxiv, Islam, Nafis Tanveer, et al. [[pdf]](https://arxiv.org/pdf/2304.11072)
- **Large Language Models and Simple, Stupid Bugs** (2023), arxiv, Jesse, Kevin, et al. [[pdf]](https://arxiv.org/pdf/2303.11455)
- **Vulnerability Detection with Graph Simplification and Enhanced Graph Representation Learning** (2023), arxiv, Wen, Xin-Cheng, et al. [[pdf]](https://arxiv.org/pdf/2302.04675)
- **DeepVD: Toward Class-Separation Features for Neural Network Vulnerability Detection** (2023), arxiv, Wang, Wenbo, et al. [[pdf]](https://aashishyadavally.github.io/files/C4.pdf)
- **CSGVD: A deep learning approach combining sequence and graph embedding for source code vulnerability detection** (2023), JSS journal, Tang, Wei, et al.
- **Fixing Hardware Security Bugs with Large Language Models** (2023), arxiv, Ahmad, Baleegh, et al. [[pdf]](https://arxiv.org/pdf/2302.01215)
- **VulEye: A Novel Graph Neural Network Vulnerability Detection Approach for PHP Application** (2023), Applied Sciences journal, Lin, Chun, et al. [[pdf]](https://www.mdpi.com/2076-3417/13/2/825/pdf)


<details><summary><b>Older:</b></i></summary>
<div>

- **VDGraph2Vec: Vulnerability Detection in Assembly Code using Message Passing Neural Networks** (2022), ICMLA'22, Diwan, Ashita, et al. [[pdf]](https://dmas.lab.mcgill.ca/fung/pub/DLF22icmla.pdf)
- **VulChecker: Graph-based Vulnerability Localization in Source Code** (2022), Usenix, Mirsky, Yisroel, et al. [[pdf]](https://www.usenix.org/system/files/sec23summer_449-mirsky-prepub.pdf)
- **DeepVulSeeker: A Novel Vulnerability Identification Framework via Code Graph Structure and Pre-training Mechanism** (2022), arxiv, Wang, Jin, et al. [[pdf]](https://arxiv.org/pdf/2211.13097)
- **Compact Abstract Graphs for Detecting Code Vulnerability with GNN Models** (2022), ACSAC'22, Luo, Yu, et al.
- **An Empirical Study of Deep Learning Models for Vulnerability Detection** (2022), arxiv, Steenhoek, Benjamin, et al. [[pdf]](https://arxiv.org/pdf/2212.08109)
- **Variable-Based Fault Localization via Enhanced Decision Tree** (2022), arxiv, Jiang, Jiajun, et al. [[pdf]](https://arxiv.org/pdf/2211.11526)
- **SPVF: security property assisted vulnerability fixing via attention-based models** (2022), EMSE, Zhou, Zhou, et al. 
- **Modeling function-level interactions for file-level bug localization** (2022), EMSE, Liang, H., et al.
- **Practical Automated Detection of Malicious npm Packages** (2022), ICSE'22, Sejfia, A., and M. Schäfer [[pdf]](https://arxiv.org/pdf/2202.13953)
- **Machine Learning for Source Code Vulnerability Detection: What Works and What Isn't There Yet** (2022), IEEE Security & Privacy, Marjanov, Tina, et al.
- **Path-sensitive code embedding via contrastive learning for software vulnerability detection** (2022), ISSTA'22, Cheng, Xiao, et al.
- **VulBERTa: Simplified Source Code Pre-Training for Vulnerability Detection** (2022), arxiv 2022, Hanif, H. and Maffeis, S. [[pdf]](https://arxiv.org/pdf/2205.12424)
- **Katana: Dual Slicing-Based Context for Learning Bug Fixes** (2022), arxiv 2022, Sintaha, Mifta, et al. [[pdf]](https://arxiv.org/pdf/2205.00180)
- **LineVul: A Transformer-based Line-Level Vulnerability Prediction** (2022), MSR'22, Fu, M., & Tantithamthavorn, C. [[pdf]](https://www.researchgate.net/profile/Chakkrit-Tantithamthavorn/publication/359402890_LineVul_A_Transformer-based_Line-Level_Vulnerability_Prediction/links/623ee3d48068956f3c4cbede/LineVul-A-Transformer-based-Line-Level-Vulnerability-Prediction.pdf)[[code]](https://github.com/awsm-research/LineVul)
- **Transformer-Based Language Models for Software Vulnerability Detection: Performance, Model's Security and Platforms** (2022), arxiv 2022, Thapa, Chandra, et al. [[pdf]](https://arxiv.org/pdf/2204.03214.pdf)
- **LineVD: Statement-level Vulnerability Detection using Graph Neural Networks** (2022), MSR'22, Hin, David, et al. [[pdf]](https://arxiv.org/pdf/2203.05181)
- **Nalin: Learning from Runtime Behavior to Find Name-Value Inconsistencies in Jupyter Notebooks** (2022), ICSE'22, Patra, Jibesh, et al. [[pdf]](https://arxiv.org/pdf/2112.06186.pdf)
- **Hoppity: Learning graph transformations to detect and fix bugs in programs** (2020), ICLR 2020, Dinella, Elizabeth, et al. [[pdf]](https://openreview.net/pdf/9d37b18aba351f4294aa84e69ea330d1fa51c471.pdf)
- **Deep Learning based Software Defect Prediction** (2020), Neurocomputing, Qiao, Lei, et al.
- **Software Vulnerability Discovery via Learning Multi-domain Knowledge Bases** (2019), IEEE TDSC, Lin, Guanjun, et al.
- **Neural Bug Finding: A Study of Opportunities and Challenges** (2019), arxiv 2019, Habib, Andrew, et al. [[pdf]](https://arxiv.org/pdf/1906.00307)
- **Automated Vulnerability Detection in Source Code Using Deep Representation Learning** (2018), ICMLA 2018, Russell, Rebecca, et al.
- **DeepBugs: A Learning Approach to Name-based Bug Detection** (2018), ACM PL 2018, Pradel, Michael, et al. [[pdf]](http://software-lab.org/publications/DeepBugs_arXiv_1805.11683.pdf)
- **Automatically Learning Semantic Features for Defect Prediction** (2016), ICSE 2016, Wang, Song, et al.

</div>
</details>

## Source Code Modeling

- **Learning in the Wild: Towards Leveraging Unlabeled Data for Effectively Tuning Pre-trained Code Models** (2024), ICSE'24, Gao, Shuzheng, et al. [[pdf]](https://arxiv.org/pdf/2401.01060)
- **CONCORD: Clone-aware Contrastive Learning for Source Code** (2023), ISSTA'23, Ding, Yangruibo, et al. [[pdf]](https://arxiv.org/pdf/2306.03234)
- **TRACED: Execution-aware Pre-training for Source Code** (2023), ICSE'24, Ding, Yangruibo, et al. [[pdf]](https://arxiv.org/pdf/2306.07487)
- **ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning** (2023), arxiv, Liu, Shangqing, et al. [[pdf]](https://arxiv.org/pdf/2301.09072)
- **ERNIE-Code: Beyond English-Centric Cross-lingual Pretraining for Programming Languages** (2022), arxiv, Chai, Yekun, et al. [[pdf]](https://arxiv.org/pdf/2212.06742)
- **Do Bugs Lead to Unnaturalness of Source Code?** (2022), FSE'22, Jiang, Yanjie, et al.
- **On the Naturalness of Bytecode Instructions** (2022), ASE'22, Choi, Y., and J. Nam. [[pdf]](https://isel.handong.edu/papers/ase22-140.pdf)
- **CodeBERT-nt: code naturalness via CodeBERT** (2022), arxiv, Khanfir, Ahmed, et al. [[pdf]](https://arxiv.org/pdf/2208.06042)
- **CommitBART: A Large Pre-trained Model for GitHub Commits** (2022), arxiv, Liu, S., et al, [[pdf]](https://arxiv.org/pdf/2208.08100) 
- **Towards Learning (Dis)-Similarity of Source Code from Program Contrasts** (2022), ACL'22, Ding, Yangruibo, et al. [[pdf]](https://aclanthology.org/2022.acl-long.436.pdf)
- **Multilingual training for Software Engineering** (2022), ICSE'22, Ahmed, Toufique, et al. [[pdf]](https://arxiv.org/pdf/2112.02043)
- **Big Code != Big Vocabulary: Open-Vocabulary Models for Source Code** (2020), ICSE'20, Karampatsis, Rafael-Michael, et al.
- **Maybe Deep Neural Networks are the Best Choice for Modeling Source Code** (2019), arxiv 2019, Karampatsis, Rafael-Michael, et al. [[pdf]](https://arxiv.org/pdf/1903.05734)
- **Are Deep Neural Networks the Best Choice for Modeling Source Code?** (2017), FSE 2017, Hellendoorn, Vincent J., et al. [[pdf]](https://vhellendoorn.github.io/PDF/fse2017.pdf)

## Program Repair

- **Agentic Bug Reproduction for Effective Automated Program Repair at Google** (2025), arxiv, Cheng, Runxiang, et al. [[pdf]](https://arxiv.org/pdf/2502.01821)
- **MultiMend: Multilingual Program Repair with Context Augmentation and Multi-Hunk Patch Generation** (2025), arxiv, Gharibi, Reza et al. [[pdf]](https://arxiv.org/pdf/2501.16044)
- **Towards Reliable Evaluation of Neural Program Repair with Natural Robustness Testing** (2025), TOSEM, Le-Cong, Thanh, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3716167) 
- **Comprehensive Fine-Tuning Large Language Models of Code for Automated Program Repair** (2025), TSE, Huang, Kai, et al. 
- **Evaluating the Generalizability of LLMs in Automated Program Repair** (2025), ICSE'25, Li, Fengjie, et al. [[pdf]](https://xgdsmileboy.github.io/files/paper/ICSE2025_NIER.pdf)
- **Evaluating Agent-based Program Repair at Google** (2025), arxiv, Rondon, Pat, et al. [[pdf]](https://arxiv.org/pdf/2501.07531)
- **Defects4Ruby: Benchmarking and Analyzing Bug Detection and Repair for Ruby Using Language Models** (2025), ICPC'25, Dehghan, Meghdad, et al. [[pdf]](https://jie-jw-wu.github.io/assets/ICPC_2025_RENE.pdf)
- **T5APR: Empowering Automated Program Repair across Languages through Checkpoint Ensemble** (2024), JSS, Gharibi, Reza, et al. [[pdf]](https://arxiv.org/pdf/2309.15742)
- **RepairLLaMA: Efficient Representations and Fine-Tuned Adapters for Program Repair** (2024), arxiv, Silva, André et al. [[pdf]](https://arxiv.org/pdf/2312.15698)
- **On Repairing Quantum Programs Using ChatGPT** (2024), Q-SE'24, Guo et al. [[pdf]](https://arxiv.org/pdf/2401.14913.pdf)
- **CigaR: Cost-efficient Program Repair with LLMs** (2024), arxiv, Hidvégi, Dávid, et al. [[pdf]](https://arxiv.org/pdf/2402.06598)
- **PyTy: Repairing Static Type Errors in Python** (2024), ICSE'24, Chow, Yiu W., et al. [[pdf]](https://arxiv.org/pdf/2401.06619.pdf)
- **A Novel Approach for Automated Program Repair using Round-Trip Translation with Large Language Models** (2024), arxiv, Ruiz, F. Vallecillos, et al. [[pdf]](https://arxiv.org/pdf/2401.07994.pdf)
- **APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models** (2024), TSE, Zhang, Quanjun, et al. [[pdf]](https://arxiv.org/pdf/2301.12453)
- **Towards Low-Resource Automatic Program Repair with Meta-Learning and Pretrained Language Models** (2023), EMNLP'23, Wang, Weishi, et al. [[pdf]](https://openreview.net/pdf?id=aLkknJNdl6)
- **GPT-3-Powered Type Error Debugging: Investigating the Use of Large Language Models for Code Repair** (2023), SLE'23, Ribeiro, Francisco, et al.
- **Enhancing Automated Program Repair through Fine-tuning and Prompt Engineering** (2023), arxiv, Paul, Rishov, et al. [[pdf]](https://lsiddiqsunny.github.io/public/2304.07840.pdf)
- **Code Similarity and Location-Awareness Automatic Program Repair** (2023), Applied Sciences, Cao, Heling, et al. [[pdf]](https://www.mdpi.com/2076-3417/13/14/8519/pdf) 
- **The Future Can’t Help Fix The Past: Assessing Program Repair In The Wild** (2023), RG, Kabadi, Vinay, et al. [[pdf]](https://www.researchgate.net/profile/Xuan-Bach-D-Le/publication/372788577_The_Future_Can't_Help_Fix_The_Past_Assessing_Program_Repair_In_The_Wild/links/64c8d8ff862f8d2999875f1e/The-Future-Cant-Help-Fix-The-Past-Assessing-Program-Repair-In-The-Wild.pdf)
- **Revisiting the Plastic Surgery Hypothesis via Large Language Models** (2023), arxiv, Xia, Chunqiu Steven et al. [[pdf]](https://arxiv.org/pdf/2303.10494)
- **A Survey on Automated Program Repair Techniques** (2023), arxiv, Huang, Kai, et al. [[pdf]](https://arxiv.org/pdf/2303.18184)
- **Keep the Conversation Going: Fixing 162 out of 337 bugs for $0.42 each using ChatGPT** (2023), arxiv, Xia, C. S., and Lingming Z. [[pdf]](https://arxiv.org/pdf/2304.00385)
- **MUFIN: Improving Neural Repair Models with Back-Translation** (2023), arxiv, Silva, André, et al. [[pdf]](https://arxiv.org/pdf/2304.02301)
- **Explainable Automated Debugging via Large Language Model-driven Scientific Debugging** (2023), arxiv, Kang, Sungmin, et al. [[pdf]](https://arxiv.org/pdf/2304.02195)
- **A study on Prompt Design, Advantages and Limitations of ChatGPT for Deep Learning Program Repair** (2023), arxiv, Cao, Jialun, et al. [[pdf]](https://arxiv.org/pdf/2304.08191)
- **ITER: Iterative Neural Repair for Multi-Location Patches** (2023), arxiv, Ye, He, and Martin M. [[pdf]](https://arxiv.org/pdf/2304.12015)
- **TraceFixer: Execution Trace-Guided Program Repair** (2023), arxiv, Bouzenia, Islem, et al. [[pdf]](https://arxiv.org/pdf/2304.12743)
- **PatchZero: Zero-Shot Automatic Patch Correctness Assessment** (2023), arxiv, Zhou, Xin, et al. [[pdf]](https://arxiv.org/pdf/2303.00202)
- **Rete: Learning Namespace Representation for Program Repair** (2023), ICSE'23, Parasaram, Nikhil et al. [[pdf]](https://mechtaev.com/files/icse23.pdf)
- **InferFix: End-to-End Program Repair with LLMs over Retrieval-Augmented Prompts** (2023), arxiv, Jin, Matthew, et al. [[pdf]](https://arxiv.org/pdf/2303.07263)
- **Automated Program Repair in the Era of Large Pre-trained Language Models** (2023), arxiv, Xia, C. S. et al. [[pdf]](https://lingming.cs.illinois.edu/publications/icse2023a.pdf)
- **KNOD: Domain Knowledge Distilled Tree Decoder for Automated Program Repair** (2023), ICSE'23, Jiang, Nan, et al. [[pdf]](https://arxiv.org/pdf/2302.01857)
- **Impact of Code Language Models on Automated Program Repair** (2023), ICSE'23, Jiang, Nan, et al. [[pdf]](https://arxiv.org/pdf/2302.05020)
- **Embedding Context as Code Dependencies for Neural Program Repair** (2023), ICST'23, Nashid, Noor, et al. [[pdf]](https://people.ece.ubc.ca/amesbah/resources/papers/icst23.pdf)
- **Tare: Type-Aware Neural Program Repair** (2023), arxiv, Zhu, Qihao, et al. [[pdf]](https://xiongyingfei.github.io/papers/ICSE23a.pdf)
- **Conversational Automated Program Repair** (2023), arxiv, Xia, Chunqiu Steven et al. [[pdf]](https://arxiv.org/pdf/2301.13246) 
- **An Analysis of the Automatic Bug Fixing Performance of ChatGPT** (2023), arxiv, Sobania, Dominik, et al. [[pdf]](https://arxiv.org/pdf/2301.08653)
- **Improving Automated Program Repair with Domain Adaptation** (2023), arxiv, Zirak, A., and Hemati, H. [[pdf]](https://arxiv.org/pdf/2212.11414)
- **A Survey of Learning-based Automated Program Repair** (2023), arxiv, Zhang, Quanjun, et al.  [[pdf]](https://arxiv.org/pdf/2301.03270.pdf)
- **TransplantFix:  Graph Differencing-based Code Transplantation for Automated Program Repair** (2023), ASE'22, Yang, Deheng, et al. [[pdf]](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=8734&context=sis_research)

<details><summary><b>Older:</b></i></summary>
<div>

- **Program Repair: Survey** (2022), arxiv, Gao, Xiang, et al. [[pdf]](https://arxiv.org/pdf/2211.12787.pdf)
- **SelfAPR: Self-supervised Program Repair with Test Execution Diagnostics** (2022), ASE'22, He et al. [[pdf]](http://arxiv.org/pdf/2203.12755)
- **Neural Program Repair using Execution-based Backpropagation** (2022), ICSE'22, He et al. [[pdf]](https://arxiv.org/abs/2105.04123)
- **Practical Program Repair in the Era of Large Pre-trained Language Models** (2022), arxiv, Xia, C. S. et al. [[pdf]](https://arxiv.org/pdf/2210.14179)
- **SYNSHINE: improved fixing of Syntax Errors** (2022), IEEE TSE, Ahmed, T. et al.
- **TransRepair: Context-aware Program Repair for Compilation Errors** (2022), ASE'22, Li, Xueyang, et al. [[pdf]](https://arxiv.org/pdf/2210.03986)
- **Repairing Bugs in Python Assignments Using Large Language Models** (2022), arxiv, Zhang, Jialu, et al. [[pdf]](https://arxiv.org/pdf/2209.14876.pdf)
- **Repair Is Nearly Generation: Multilingual Program Repair with LLMs** (2022), arxiv, Joshi, Harshit, et al. [[pdf]](https://arxiv.org/pdf/2208.11640)
- **VulRepair: A T5-Based Automated Software Vulnerability Repair** (2022), FSE'22, Fu, Michael, et al. [[pdf]](https://www.researchgate.net/profile/Chakkrit-Tantithamthavorn/publication/362092639_VulRepair_A_T5-Based_Automated_Software_Vulnerability_Repair/links/62d67c1ef976fb7443cecc35/VulRepair-A-T5-Based-Automated-Software-Vulnerability-Repair.pdf)
- **Less Training, More Repairing Please: Revisiting Automated Program Repair via Zero-shot Learning** (2022), FSE'22, Xia, Chunqiu Steven, and Lingming Z. [[pdf]](https://arxiv.org/pdf/2207.08281)
- **Can we learn from developer mistakes? Learning to localize and repair real bugs from real bug fixes** (2022), arxiv, Richter, Cedric, and Heike W. [[pdf]](https://arxiv.org/pdf/2207.00301)
- **AdaptivePaste: Code Adaptation through Learning Semantics-aware Variable Usage Representations** (2022), arxiv 2022, Liu, Xiaoyu, et al. [[pdf]](https://arxiv.org/pdf/2205.11023)
- **DEAR: A Novel Deep Learning-based Approach for Automated Program Repair** (2022), ICSE'22, Li, Yi, et al. [[pdf]](https://arxiv.org/pdf/2205.01859)
- **TFix: Learning to Fix Coding Errors with a Text-to-Text Transformer** (2021), ICML'21, Berabi, Berkay, et al. [[pdf]](http://proceedings.mlr.press/v139/berabi21a/berabi21a.pdf)
- **Neural Transfer Learning for Repairing Security Vulnerabilities in C Code** (2021), Chen, Zimin, et al. [[pdf]](https://arxiv.org/pdf/2104.08308)
- **Generating Bug-Fixes Using Pretrained Transformers** (2021), arxiv 2021, Drain, Dawn, et al. [[pdf]](https://arxiv.org/pdf/2104.07896)
- **Global Relational Models of Source Code** (2020), ICLR'20, Hellendoorn, Vincent J., et al. [[pdf]](https://openreview.net/pdf?id=B1lnbRNtwr)
- **Neural Program Repair by Jointly Learning to Localize and Repair** (2019), arxiv 2019, Vasic, Marko, et al. [[pdf]](https://arxiv.org/pdf/1904.01720)


</div>
</details>

## Program Translation

- **I Can’t Share Code, but I need Translation - An Empirical Study on Code Translation through Federated LLM** (2025), arxiv, Kumar, Jahnavi, et al. [[pdf]](https://arxiv.org/pdf/2501.05724)
- **ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation** (2025), arxiv, He, Minghua, et al. [[pdf]](https://arxiv.org/pdf/2501.18460)
- **C2SAFERRUST: Transforming C Projects into Safer Rust with NeuroSymbolic Techniques** (2025), arxiv, Nitin, Vikram, et al. [[pdf]](https://arxiv.org/pdf/2501.14257)
- **Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation** (2025), arxiv, Zhang, Xing, et al. [[pdf]](https://arxiv.org/pdf/2501.16050)
- **Scalable, Validated Code Translation of Entire Projects using Large Language Models** (2024), arxiv, Zhang, Hanliang, et al. [[pdf]](https://arxiv.org/pdf/2412.08035)
- **Fortran2CPP: Automating Fortran-to-C++ Translation using LLMs via Multi-Turn Dialogue and Dual-Agent Integration** (2025), arxiv, Chen, Le, et al. [[pdf]](https://arxiv.org/pdf/2412.19770)
- **Few-shot code translation via task-adapted prompt learning** (2024), JSS, Li, Xuan, et al.
- **Unsupervised Binary Code Translation with Application to Code Similarity Detection and Vulnerability Discovery** (2023), EMNLP'23, Ahmad, I., & Luo, L. [[pdf]](https://openreview.net/pdf?id=5EHI2FGf1D)
- **TransMap: Pinpointing Mistakes in Neural Code Translation** (2023), FSE'23, Wang, Bo, et al. 
- **On the Evaluation of Neural Code Translation: Taxonomy and Benchmark** (2023), arxiv, Jiao, Mingsheng, et al. [[pdf]](https://arxiv.org/pdf/2308.08961)
- **Attention, Compilation, and Solver-based Symbolic Analysis are All You Need** (2023), arxiv, Jana, Prithwish, et al. [[pdf]](https://arxiv.org/pdf/2306.06755)
- **Understanding the Effectiveness of Large Language Models in Code Translation** (2023), arxiv, Pan, Rangeet, et al. [[pdf]](https://arxiv.org/pdf/2308.03109)
- **On ML-Based Program Translation: Perils and Promises** (2023), arxiv, Malyala, Aniketh, et al. [[pdf]](https://arxiv.org/pdf/2302.10812)
- **Boosting Neural Networks to Decompile Optimized Binaries** (2022), ACSAC'22, Cao, Ying, et al.
- **The Effectiveness of Transformer Models for Analyzing Low-Level Programs** (2022), MIT Primes, Zifan Guo [[pdf]](https://math.mit.edu/research/highschool/primes/materials/2021/GuoCarl.pdf)
- **Code Translation with Compiler Representations** (2022), arxiv, Szafraniec, Marc, et al. [[pdf]](https://arxiv.org/pdf/2207.03578)
- **BabelTower: Learning to Auto-parallelized Program Translation** (2022), ICML'22, Wen, Yuanbo, et al. [[pdf]](https://proceedings.mlr.press/v162/wen22b/wen22b.pdf)
- **Multilingual Code Snippets Training for Program Translation** (2022), AAAI'22, Zhu, Ming, et al. [[pdf]](https://people.cs.vt.edu/~reddy/papers/AAAI22.pdf)
- **Semantics-Recovering Decompilation through Neural Machine Translation** (2021), arxiv 2021, Liang, Ruigang, et al. [[pdf]](https://arxiv.org/pdf/2112.15491.pdf)
- **Unsupervised Translation of Programming Languages** (2020), arxiv 2020, Lachaux, Marie-Anne et al. [[pdf]](https://arxiv.org/abs/2006.03511)

## Program Analysis

- **LLM-Powered Static Binary Taint Analysis** (2025), TOSEM, Liu, Puzhuo, et al.[[pdf]](https://dl.acm.org/doi/pdf/10.1145/3711816)
- **Predictive Program Slicing via Execution Knowledge-Guided Dynamic Dependence Learning** (2024), FSE'24, Yadavally, Aashish, et al. [[pdf]](https://aashishyadavally.github.io/assets/pdf/pub-fse2024.pdf)
- **A Learning-Based Approach to Static Program Slicing** (2024), OOPSLA'24, Yadavally, Aashish, et al. [[pdf]](https://aashishyadavally.github.io/assets/pdf/pub-oopsla2024.pdf)[[code]](https://github.com/aashishyadavally/ns-slicer)
- **On the Effectiveness of Machine Learning-based Call Graph Pruning: An Empirical Study** (2024), MSR'24, Mir, Amir et al. [[pdf]](https://arxiv.org/pdf/2402.07294)
- **Static Code Analysis in the AI Era: An In-depth Exploration of the Concept, Function, and Potential of Intelligent Code Analysis** (2023), arxiv, Fan, Gang, et al. [[pdf]](https://arxiv.org/pdf/2310.08837)
- **(Partial) Program Dependence Analysis** (2023), ICSE'23, Yadavally, Aashish, et al. [[pdf]](https://aashishyadavally.github.io/assets/pdf/pub-icse2023-(1).pdf)[[code]](https://github.com/aashishyadavally/NeuralPDA/)
- **Precise Data-Driven Approximation for Program Analysis via Fuzzing** (2023), ASE'23, Parasaram, Nikhil, et al. [[pdf]](https://mechtaev.com/files/ase23.pdf)
- **The Hitchhiker’s Guide to Program Analysis: A Journey with Large Language Models** (2023), arxiv, Li, Haonan, et al. [[pdf]](https://arxiv.org/pdf/2308.00245)
- **AutoPruner: Transformer-Based Call Graph Pruning** (2022), FSE'22, Le-Cong, Thanh, et al. [[pdf]](https://arxiv.org/pdf/2209.03230)[[code]](https://github.com/soarsmu/AutoPruner/)
- **Striking a Balance: Pruning False-Positives from Static Call Graphs** (2022), ICSE'22, Utture, Akshay, et al. [[pdf]](http://compilers.cs.ucla.edu/papers/balancing-callgraphs.pdf)[[code]](https://zenodo.org/record/6057691)

## Software Testing

- **Test Wars: A Comparative Study of SBST, Symbolic Execution, and LLM-Based Approaches to Unit Test Generation** (2025), ICST'25, Abdullin, A. et al. [[pdf]](https://arxiv.org/pdf/2501.10200)
- **LlamaRestTest: Effective REST API Testing with Small Language Models** (2025), FSE'25, Kim, M., et al. [[pdf]](https://arxiv.org/pdf/2501.08598)
- **DrWASI: LLM-assisted Differential Testing for WebAssembly System Interface Implementations** (2025), TOSEM, Zhang, Yixuan, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3716379)
- **Otter: Generating Tests from Issues to Validate SWE Patches** (2025), arxiv, Ahmed, Toufique, et al. [[pdf]](https://arxiv.org/pdf/2502.05368)
- **Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators** (2025), USENIX'25, Zhang, Kunpeng, et al. [[pdf]](https://arxiv.org/pdf/2501.19282)
- **RagVerus: Repository-Level Program Verification with LLMs using Retrieval Augmented Generation** (2025), arxiv, Zhong, Sicheng, et al.  [[pdf]](https://arxiv.org/pdf/2502.05344)
- **AsserT5: Test Assertion Generation Using a Fine-Tuned Code Language Model** (2025), AST'25, Primbs, S., et al. [[pdf]](https://arxiv.org/pdf/2502.02708)
- **exLong: Generating Exceptional Behavior Tests with Large Language Models** (2025), ICSE'25, Zhang, Jiyang, et al. [[pdf]](https://users.ece.utexas.edu/~gligoric/papers/ZhangETAL25exLong.pdf) 
- **Learning to Generate Unit Tests for Automated Debugging** (2025), arxiv, Prasad, Archiki, et al. [[pdf]](https://arxiv.org/pdf/2502.01619)
- **Mutation-Guided LLM-based Test Generation at Meta** (2025), FSE'25, Foster, Christopher, et al.  [[pdf]](https://arxiv.org/pdf/2501.12862)
- **CITYWALK: Enhancing LLM-Based C++ Unit Test Generation via Project-Dependency Awareness and Language-Specific Knowledge** (2025), arxiv, Zhang, Yuwei, et al. [[pdf]](https://arxiv.org/pdf/2501.16155)
- **Enhancing LLM’s Ability to Generate More Repository-Aware Unit Tests Through Precise Contextual Information Injection** (2025), arxiv, Yin, Xin, et al. [[pdf]](https://arxiv.org/pdf/2501.07425)
- **DeCon: Detecting Incorrect Assertions via Postconditions Generated by a Large Language Model** (2025), arxiv, Yu, Hao, et al. [[pdf]](https://arxiv.org/pdf/2501.02901)
- **Improving the Readability of Automatically Generated Tests using Large Language Models** (2025), ICST'25, Biagiola, Matteo, et al. [[pdf]](https://arxiv.org/abs/2412.18843)
- **The Prompt Alchemist: Automated LLM-Tailored Prompt Optimization for Test Case Generation** (2025), arxiv, Gao, Shuzheng, et al. [[pdf]](https://arxiv.org/pdf/2501.01329)
- **A Large-scale Empirical Study on Fine-tuning Large Language Models for Unit Testing** (2025), ISSTA'25, Shang, Ye, et al. [[pdf]](https://arxiv.org/pdf/2412.16620)
- **Detecting Test Smells in Python Test Code Generated by LLM: An Empirical Study with GitHub Copilot** (2025), SBES'24, Alves, Victor Anthony, et al. [[pdf]](https://www.researchgate.net/profile/Ivan-Machado-2/publication/385117950_Detecting_Test_Smells_in_Python_Test_Code_Generated_by_LLM_An_Empirical_Study_with_GitHub_Copilot/links/674f5660a7fbc259f1aacf16/Detecting-Test-Smells-in-Python-Test-Code-Generated-by-LLM-An-Empirical-Study-with-GitHub-Copilot.pdf)
- **Automated Test Case Repair Using Language Models** (2024), arxiv, Yaraghi, A. S., et al. [[pdf]](https://arxiv.org/pdf/2401.06765)
- **Using GitHub Copilot for Test Generation in Python: An Empirical Study** (2024), AST'24, El Haji, Khalid et al. [[pdf]](https://azaidman.github.io/publications/elhajiAST2024.pdf)
- **Intent-Driven Mobile GUI Testing with Autonomous Large Language Model Agents** (2024), arxiv, Yoon, Juyeon et al. [[pdf]](https://coinse.github.io/publications/pdfs/Yoon2024aa.pdf)
- **Enhancing Large Language Models for Text-to-Testcase Generation** (2024), arxiv, Alagarsamy, Saranya, et al. [[pdf]](https://arxiv.org/pdf/2402.11910)
- **CovRL: Fuzzing JavaScript Engines with Coverage-Guided Reinforcement Learning for LLM-based Mutation** (2024), arxiv, Eom, Jueon et al. [[pdf]](https://arxiv.org/pdf/2402.12222)
- **Code-Aware Prompting: A study of Coverage guided Test Generation in Regression Setting using LLM** (2024), arxiv, Ryan, Gabriel, et al. [[pdf]](https://arxiv.org/pdf/2402.00097)
- **LLM4FUZZ: Guided Fuzzing of Smart Contracts with Large Language Models** (2024), arxiv, Shou, Chaofan, et al. [[pdf]](https://arxiv.org/pdf/2401.11108.pdf)
- **Automated Test Case Repair Using Language Models** (2024), arxiv, Yaraghi, A. S., et al. [[pdf]](https://arxiv.org/pdf/2401.06765.pdf)
- **Fuzz4All: Universal Fuzzing with Large Language Models** (2024), ICSE'24, Xia, C., et al. [[pdf]](https://www.software-lab.org/publications/icse2024_Fuzz4All.pdf)
- **TDD Without Tears: Towards Test Case Generation from Requirements through Deep Reinforcement Learning** (2024), arxiv, Takerngsaksiri, Wannita, et al. [[pdf]](https://arxiv.org/html/2401.07576v1)
- **Unit Test Generation using Generative AI : A Comparative Performance Analysis of Autogeneration Tools** (2024), arxiv, Bhatia, Shreya, et al. [[pdf]](https://arxiv.org/pdf/2312.10622)
- **CAT-LM: Training Language Models on Aligned Code And Tests**, ASE'23, Rao, Nikitha, et al. [[pdf]](https://arxiv.org/pdf/2310.01602)
- **LLM4TDD: Best Practices for Test Driven Development Using Large Language Models** (2023), arxiv, Piya, S., & Sullivan, A. [[pdf]](https://arxiv.org/pdf/2312.04687)
- **Autonomous Large Language Model Agents Enabling Intent-Driven Mobile GUI Testing** (2023), arxiv, Yoon, Juyeon, et al. [[pdf]](https://arxiv.org/pdf/2311.08649)
- **White-box Compiler Fuzzing Empowered by Large Language Models** (2023), arxiv, Yang, Chenyuan, et al. [[pdf]](https://arxiv.org/pdf/2310.15991)
- **Test Case Recommendations with Distributed Representation of Code Syntactic Features** (2023), ASEW'23, Rezaei, M. et al. [[pdf]](https://arxiv.org/pdf/2310.03174)
- **Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models** (2023), arxiv, Plein, Laura, et al. [[pdf]](https://arxiv.org/pdf/2310.06320)
- **The Program Testing Ability of Large Language Models for Code** (2023), arxiv, Xiong, W. et al. [[pdf]](https://arxiv.org/pdf/2310.05727)
- **Revisiting Neural Program Smoothing for Fuzzing** (2023), FSE'23, Bansal, Aakash et al. [[pdf]](https://arxiv.org/pdf/2309.02326)
- **An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation** (2023), arxiv, Schäfer, Max, et al. [[pdf]](https://arxiv.org/pdf/2302.06527)
- **Automated Test Case Generation Using Code Models and Domain Adaptation** (2023), arxiv, Hashtroudi, Sepehr, et al. [[pdf]](https://arxiv.org/pdf/2308.08033.pdf)
- **Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing** (2023), arxiv, Dakhel, A. M., et al. [[pdf]](https://arxiv.org/pdf/2308.16557)
- **Automatic Unit Test Generation for Deep Learning Frameworks based on API Knowledge** (2023), arxiv, Narayanan, A., et al. [[pdf]](https://arxiv.org/pdf/2307.00404)
- **Black-Box Prediction of Flaky Test Fix Categories Using Language Models** (2023), arxiv, Fatima, S., et al. [[pdf]](https://arxiv.org/pdf/2307.00012)
- **Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models** (2023), ISSTA'23, Deng, Yinlin, et al. [[pdf]](https://arxiv.org/abs/2212.14834)
- **Understanding Large Language Model Based Fuzz Driver Generation** (2023), arxiv, Zhang, Cen, et al. [[pdf]](https://arxiv.org/pdf/2307.12469)
- **Universal Fuzzing via Large Language Models** (2023), arxiv, Xia, Chunqiu Steven, et al. [[pdf]](https://arxiv.org/pdf/2308.04748)
- **SAGA: Summarization-Guided Assert Statement Generation** (2023), arxiv, Zhang, Yuwei, et al. [[pdf]](https://arxiv.org/pdf/2305.14808)
- **Towards More Realistic Evaluation for Neural Test Oracle Generation** (2023), ISSTA'23, Liu, Zhongxin, et al. [[pdf]](https://arxiv.org/pdf/2305.17047)
- **LTM: Scalable and Black-box Similarity-based Test Suite Minimization based on Language Models** (2023), arxiv, Pan, Rongqi, et al. [[pdf]](https://arxiv.org/pdf/2304.01397)
- **ChatGPT and Software Testing Education: Promises & Perils** (2023), arxiv, Jalil, Sajed, et al. [[pdf]](https://arxiv.org/pdf/2302.03287)
- **Adaptive Test Generation Using a Large Language Model** (2023), arxiv, Schäfer, Max, et al. [[pdf]](https://arxiv.org/pdf/2302.06527)
- **CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models** (2023), ICSE'23, Lemieux, Caroline, et al. [[pdf]](https://www.carolemieux.com/codamosa_icse23.pdf) 
- **Learning Deep Semantics for Test Completion** (2023), arxiv, Nie, Pengyu, et al. [[pdf]](https://arxiv.org/pdf/2302.10166)
- **A3Test: Assertion-Augmented Automated Test Case Generation** (2023), arxiv, Alagarsamy, Saranya, et al. [[pdf]](https://arxiv.org/pdf/2302.10352)
- **Efficient Mutation Testing via Pre-Trained Language Models** (2023), arxiv, Khanfir, Ahmed, et al. [[pdf]](https://arxiv.org/pdf/2301.03543)

<details><summary><b>Older:</b></i></summary>
<div>

- **Test2Vec: An Execution Trace Embedding for Test Case Prioritization** (2022), arxiv, Jabbar, Emad, et al. [[pdf]](https://arxiv.org/pdf/2206.15428.pdf)
- **Generating Accurate Assert Statements for Unit Test Cases using Pretrained Transformers** (2022), AST'22, Tufano, Michele, et al.
- **On Learning Meaningful Assert Statements for Unit Test Cases** (2020), ICSE'20, Watson, Cody, et al.

</div>
</details>

## Code Clone Detection

- **An enhanced transformer-based framework for interpretable code clone detection** (2025), JSS, Nashaat, Mona, et al. 
- **CEBin: A Cost-Effective Framework for Large-Scale Binary Code Similarity Detection** (2024),ISSTA'24, Wang, Hao, et al. [[pdf]](https://arxiv.org/pdf/2402.18818.pdf) [[code]](https://github.com/Hustcw/CEBin)
- **Investigating the Efficacy of Large Language Models for Code Clone Detection** , ICPC'24, Khajezade, Mohamad, et al. [[pdf]](https://arxiv.org/pdf/2401.13802) 
- **Improving Cross-Language Code Clone Detection via Code Representation Learning and Graph Neural Networks** (2023), arxiv, Mehrotra, Nikita, et al.
- **ZC3: Zero-Shot Cross-Language Code Clone Detection** (2023), arxiv, Li, Jia, et al. [[pdf]](https://arxiv.org/pdf/2308.13754)
- **Comparison and Evaluation of Clone Detection Techniques with Different Code Representations** (2023), ICSE'23, Wang, Yuekun, et al. [[pdf]](https://wu-yueming.github.io/Files/ICSE2023_TACC.pdf)
- **Towards Understanding the Capability of Large Language Models on Code Clone Detection: A Survey** (2023), arxiv, Dou, Shihan, et al. [[pdf]](https://arxiv.org/pdf/2308.01191)
- **CCT-Code: Cross-Consistency Training for Multilingual Clone Detection and Code Search** (2023), arxiv, Sorokin, Nikita, et al. [[pdf]](https://arxiv.org/pdf/2305.11626.pdf)
- **Neuro-symbolic Zero-Shot Code Cloning with Cross-Language Intermediate Representation** (2023), arxiv, Hasija, Krishnam, et al. [[pdf]](https://arxiv.org/pdf/2304.13350)
- **Pathways to Leverage Transcompiler based Data Augmentation for Cross-Language Clone Detection** (2023), arxiv, Pinku, Subroto Nag et al. [[pdf]](https://arxiv.org/pdf/2303.01435)
- **Graph-based code semantics learning for efficient semantic code clone detection** (2022), IST journal, Yu, Dongjin, et al.
- **Efficient transformer with code token learner for code clone detection** (2022), arxiv, Zhang, Aiping, et al.
- **Evaluation of Contrastive Learning with Various Code Representations for Code Clone Detection** (2022), arxiv, Zubkov, Maksim, et al. [[pdf]](https://arxiv.org/pdf/2206.08726)
- **Cross-Language Source Code Clone Detection Using Deep Learning with InferCode** (2022), arxiv 2022, Yahya, M., and Kim, D., [[pdf]](https://arxiv.org/pdf/2205.04913)
- **funcGNN: A Graph Neural Network Approach to Program Similarity** (2020), ESEM'20, Nair, Aravind, et al. [[pdf]]()
- **Cross-Language Clone Detection by Learning Over Abstract Syntax Trees** (2019), MSR'19, Perez, Daniel, et al.
- **The Adverse Effects of Code Duplication in Machine Learning Models of Code** (2019), Onward! 2019, Allamanis, Miltiadis, [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3359591.3359735)

## Code Search

- **MM-SCS: Leveraging Multimodal Features to Enhance Smart Contract Code Search** (2025), TSE, Shi, Chaochen, et al.
- **Fine-Grained Features-based Code Search for Precise Query-Code Matching** (2025), COLING'25, Zhang, Xinting, et al. [[pdf]](https://aclanthology.org/2025.coling-main.482.pdf) 
- **Rapid: Zero-shot Domain Adaptation for Code Search with Pre-trained Models** (2024), TOSEM, Fan et al.
- **Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search** (2024), arxiv, Li, Haochen et al. [[pdf]](https://arxiv.org/pdf/2401.04514) 
- **Rapid: Zero-shot Domain Adaptation for Code Search with Pre-trained Models** (2024), TOSEM, Fan, Guodong, et al.
- **Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search** (2024), arxiv, Li, Haochen, et al. [[pdf]](https://arxiv.org/pdf/2401.04514.pdf)
- **Intervention-Based Alignment of Code Search with Execution Feedback** (2023), EMNLP'23, Han, Hojae, et al. [[pdf]](https://aclanthology.org/2023.findings-emnlp.148.pdf)
- **You Augment Me: Exploring ChatGPT-based Data Augmentation for Semantic Code Search** (2023), ICSME'23, Wang, Yanlin, et al. [[pdf]](https://yanlin.info/papers/ChatDance-icsme23.pdf)
- **Efficient Text-to-Code Retrieval with Cascaded Fast and Slow Transformer Models** (2023), FSE'23, Gotmare, A., et al. 
- **GraphSearchNet: Enhancing GNNs via capturing global dependencies for semantic code search** (2023), TSE, Liu, Shangqing, et al. [[pdf]](https://arxiv.org/pdf/2111.02671)
- **KAPE: kNN-based Performance Testing for Deep Code Search** (2023), TOSEM, uo, Yuejun, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3624735)
- **Two Birds with One Stone: Boosting Code Generation and Code Search via a Generative Adversarial Network** (2023), OOPSLA'23, Wang, Shangwen, et al. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3622815)
- **Hyperbolic Code Retrieval: A Novel Approach for Efficient Code Search Using Hyperbolic Space Embeddings** (2023), arxiv, Tang, Xunzhu, et al. [[pdf]](https://arxiv.org/pdf/2308.15234)
- **Rethinking Negative Pairs in Code Search** (2023), EMNLP'23, Li, Haochen, et al. [[pdf]](https://arxiv.org/abs/2310.08069)[[code]](https://github.com/Alex-HaochenLi/Soft-InfoNCE)
- **Hyperbolic Code Retrieval: A Novel Approach for Efficient Code Search Using Hyperbolic Space Embeddings** (2023), AAAI'24, Tang, Xunzhu, et al. [[pdf]](https://arxiv.org/pdf/2308.15234)
- **Self-Supervised Query Reformulation for Code Search** (2023), FSE'23, Mao, Yuetian, et al. [[pdf]](https://arxiv.org/pdf/2307.00267)
- **Evaluating and Optimizing the Effectiveness of Neural Machine Translation in Supporting Code Retrieval Models: A Study on the CAT Benchmark** (2023), CIKM'23, P. Hung, and A. Jannesari. [[pdf]](https://arxiv.org/pdf/2308.04693)
- **CoCoSoDa: Effective Contrastive Learning for Code Search** (2023) ICSE'23, Shi, Ensheng, et al. [[pdf]](https://arxiv.org/pdf/2204.03293.pdf)
- **Improving Code Search with Multi-Modal Momentum Contrastive Learning** (2023), ICPC'23, Shi, Zejian, et al. [[pdf]](https://szj2935.github.io/icpc2023mococs.pdf)
- **MulCS: Towards a Unified Deep Representation for Multilingual Code Search** (2023), SANER'23, Ma, Yingwei, et al. [[pdf]](https://yuyue.github.io/res/paper/MulCS-saner2023.pdf)
- **A mutual embedded self-attention network model for code search** (2023), JSS, Hu, Haize, et al.

<details><summary><b>Older:</b></i></summary>
<div>

- **You See What I Want You to See: Poisoning Vulnerabilities in Neural Code Search** (2022), FSE'22, Wan, Yao, et al.
- **How to Better Utilize Code Graphs in Semantic Code Search?** (2022), FSE'22, Shi, Yucen, et al.
- **Exploring Representation-Level Augmentation for Code Search** (2022), EMNLP'22, Li, Haochen, et al. [[pdf]](https://arxiv.org/pdf/2210.12285)[[code]](https://github.com/Alex-HaochenLi/RACS)
- **A code search engine for software ecosystems** (2022), CEUR, Pfaff, Chris, et al. [[pdf]](https://benevol2022.github.io/papers/ChrisPfaff.pdf)
- **Cross-Domain Deep Code Search with Meta Learning** (2022), ICSE'22, Chai, Yitian, et al. [[pdf]](https://guxd.github.io/papers/cdcs.pdf)

</div>
</details>

## Code Language Models

- **CodeFuse-13B: A Pretrained Multi-lingual Code Large Language Model** (2023), arxiv, Di, Peng, et al. [[pdf]](https://arxiv.org/pdf/2310.06266)
- **Code Llama: Open Foundation Models for Code** (2023), Meta AI, Rozière et al. [[pdf]](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/)
- **Gorilla: Large Language Model Connected with Massive APIs** (2023), arxiv, Patil, Shishir G., et al. [[pdf]](https://arxiv.org/pdf/2305.15334)
- **CodeT5+: Open Code Large Language Models for Code Understanding and Generation** (2023), arxiv, Wang, Yue, et al. [[pdf]](https://arxiv.org/pdf/2305.07922)
- **Better Language Models of Code through Self-Improvement** (2023), arxiv, To, Hung Quoc, et al. [[pdf]](https://arxiv.