# A Survey of LLM × DATA

[English](README.md) | [中文](README_CN.md)

> A collection of papers and projects related to LLMs and corresponding data-centric methods. [![arXiv](https://camo.githubusercontent.com/dc1f84975e5d05724930d5c650e4b6eaea49e9f4c03d00de50bd7bf950394b4f/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f6261646765732f7261772f6d61696e2f70617065722d706167652d736d2d6461726b2e737667)](https://arxiv.org/abs/2505.18458)
>
> Other publicly-available materials: [[Slides]](./assets/DATA4LLM-10-22-en.pdf)
>
> If you find our survey useful, please cite the paper:

```
@article{LLMDATASurvey,
    title={A Survey of LLM × DATA},
    author={Xuanhe Zhou and Junxuan He and Wei Zhou and Haodong Chen and Zirui Tang and Haoyu Zhao and Xin Tong and Guoliang Li and Youmin Chen and Jun Zhou and Zhaojun Sun and Binyuan Hui and Shuo Wang and Conghui He and Zhiyuan Liu and Jingren Zhou and Fan Wu},
    year={2025},
    journal={arXiv preprint arXiv:2505.18458},
    url={https://arxiv.org/abs/2505.18458}
}
@article{tangllmasanalyst,
    title={LLM/Agent-as-Data-Analyst: A Survey},
    author={Zirui Tang and Weizheng Wang and Zihang Zhou and Yang Jiao and Bangrui Xu and Boyu Niu and Xuanhe Zhou and Guoliang Li and Yeye He and Wei Zhou and Yitong Song and Cheng Tan and Bin Wang and Conghui He and Xiaoyang Wang and Fan Wu},
    year={2025},
    journal={arXiv preprint arXiv:2509.23988},
    url={https://arxiv.org/abs/2509.23988}
}
@article{zhoullmpreparationsurvey,
    title={Can LLMs Clean Up Your Mess? A Survey of Application-Ready Data Preparation with LLMs},
    author={Wei Zhou and Jun Zhou and Haoyu Wang and Zhenghao Li and Qikang He and Shaokun Han and Guoliang Li and Xuanhe Zhou and Yeye He and Chunwei Liu and Zirui Tang and Bin Wang and Shen Tang and Kai Zuo and Yuyu Luo and Zhenzhe Zheng and Conghui He and Jingren Zhou and Fan Wu},
    year={2026},
    journal={arXiv preprint arXiv:2601.17058},
    url={https://arxiv.org/abs/2601.17058}
}
```

## 🌤 The IaaS Concept of DATA4LLM

The **IaaS** concept for LLM data (phonetically echoing *Infrastructure as a Service*) defines the characteristics of high-quality datasets along four key dimensions: (1) **Inclusiveness** ensures broad coverage across domains, tasks, sources, languages, styles, and modalities. (2) **Abundance** emphasizes sufficient and well-balanced data volume to support scaling, fine-tuning, and continual learning without overfitting. (3) **Articulation** requires clear, coherent, and instructive content with step-by-step reasoning to enhance model understanding and task performance. (4) **Sanitization** involves rigorous filtering to remove private, toxic, unethical, and misleading content, ensuring data safety, neutrality, and compliance. [![arXiv](https://camo.githubusercontent.com/dc1f84975e5d05724930d5c650e4b6eaea49e9f4c03d00de50bd7bf950394b4f/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f6261646765732f7261772f6d61696e2f70617065722d706167652d736d2d6461726b2e737667)](https://arxiv.org/abs/2505.18458)

[![Cover](https://github.com/SUPERZJ827/LLM4DB/raw/main/assets/iaas_overview_v2.png)](https://github.com/SUPERZJ827/LLM4DB/blob/main/assets/iaas_overview_v2.png)

## 🌟 LLM/Agent-as-Data-Analyst

We observe the evolution of **LLM/Agent-as-Data-Analyst** techniques follows a five-dimension trajectory: (1) Data Modality (homogeneous → heterogeneous); (2) Analysis Functionality (literal → semantic); (3) Knowledge Scope (closed-world →open-world); (4) Tool Integration (tool-coupled → tool-assisted); (5) Development Autonomy (manual → fully autonomous). [![arXiv](https://camo.githubusercontent.com/dc1f84975e5d05724930d5c650e4b6eaea49e9f4c03d00de50bd7bf950394b4f/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f6261646765732f7261772f6d61696e2f70617065722d706167652d736d2d6461726b2e737667)](https://arxiv.org/abs/2509.23988)

[![Cover2](assets/data_analysis_survey_v2.png)](assets/data_analysis_survey_v2.png)

## 📤 LLM-Enhanced Application-Ready Data Preparation

We present a systematic survey of **LLM-enhanced data preparation**, an emerging paradigm driven by growing demands for application-ready data, advances in large language models, and agent-oriented data infrastructures. 
- **(1) Paradigm Shift Identification:** We reveal the transition from rule-based, model-specific pipelines to prompt-driven, context-aware, and agentic preparation workflows;
- **(2) Task-Centric Taxonomy:** We organize existing methods into data cleaning, data integration, and data enrichment;  
- **(3) Methodological Survey:** We review representative techniques for each task, highlighting their strengths and limitations; 
- **(4) Empirical Landscape Analysis:** We examine commonly used datasets and evaluation practices; 
- **(5) Research Roadmap:** We outline open challenges and future directions toward scalable, reliable, and robust LLM-based data preparation systems. [![arXiv](https://camo.githubusercontent.com/dc1f84975e5d05724930d5c650e4b6eaea49e9f4c03d00de50bd7bf950394b4f/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f6261646765732f7261772f6d61696e2f70617065722d706167652d736d2d6461726b2e737667)](https://arxiv.org/abs/2601.17058)

[![Cover3](assets/llm_data_preparation_survey_overview.jpg)](assets/llm_data_preparation_survey_overview.jpg)

## Table of Contents

- [Datasets](#datasets)

- [0 Data Characteristics across LLM Stages](#0-data-characteristics-across-llm-stages)

  - [Data for Pretraining](#data-for-pretraining)
  - [Data for Continual Pre-training](#data-for-continual-pre-training)
  - [Data for Supervised Fine-Tuning (SFT)](#data-for-supervised-fine-tuning-sft)
  - [Data for Reinforcement Learning (RL)](#data-for-reinforcement-learning-rl)
  - [Data for Retrieval-Augmented Generation (RAG)](#data-for-retrieval-augmented-generation-rag)
  - [Data for LLM Evaluation](#data-for-llm-evaluation)
  - [Data for LLM Agents](#data-for-llm-agents)
  
- [1 Data Processing for LLM](#1-data-processing-for-llm)
  - [1.1 Data Acquisition](#11-data-acquisition)
  - [1.2 Data Deduplication](#12-data-deduplication)
  - [1.3 Data Filtering](#13-data-filtering)
  - [1.4 Data Domain Selection](#14-data-domain-selection)
  - [1.5 Data Mixing](#15-data-mixing)
  - [1.6 Data Distillation and Synthesis](#16-data-distillation-and-synthesis)
  - [1.7 End-to-End Data Processing Pipelines](#17-end-to-end-data-processing-pipelines)
  
- [2 Data Storage for LLM](#2-data-storage-for-llm)
  
  - [2.1 Data Formats](#21-data-formats)
  - [2.2 Data Distribution](#22-data-distribution)
  - [2.3 Data Organization](#23-data-organization)
  - [2.4 Data Movement](#24-data-movement)
  - [2.5 Data Fault Tolerance](#25-data-fault-tolerance)
  - [2.6 KV Cache](#26-kv-cache)
  
- [3 Data Serving for LLM](#3-data-serving-for-llm)
  
  - [3.1 Data Shuffling](#31-data-shuffling)
  - [3.2 Data Compression](#32-data-compression)
  - [3.3 Data Packing](#33-data-packing)
  - [3.4 Data Provenance](#34-data-provenance)
  
- [4 LLM for Data Management](#4-llm-for-data-management)
  
  - [4.1 LLM for Analysis](#41-llm-for-data-analysis)
  - [4.2 LLM for Data System Optimization](#42-llm-for-data-system-optimization)
  
- [5 LLM as Data Analyst](#5-llm-as-data-analyst)

   - [5.1 LLM for Structured Data Analysis](#51-llm-for-structured-data-analysis)
   - [5.2 LLM for Semi-Structured Data Analysis](#52-llm-for-semi-structured-data-analysis)
   - [5.3 LLM for Unstructured Data Analysis](#53-llm-for-unstructured-data-analysis)
  - [5.4 LLM for Heterogeneous Data Analysis](#54-llm-for-heterogeneous-data-analysis)

- [6 LLM-Enhanced Application-Ready Data Preparation](#6-llm-enhanced-application-ready-data-preparation)

  - [6.1 Data Cleaning](#61-data-cleaning)
  - [6.2 Data Integration](#62-data-integration)
  - [6.3 Data Enrichment](#63-data-enrichment)

  <!-- - [4.2 LLM for Data Analysis](#42-llm-for-data-analysis) -->

## Datasets

1. **CommonCrawl**: A massive web crawl dataset covering diverse languages and domains; widely used for LLM pretraining. [[Source](https://commoncrawl.org/latest-crawl)]

1. **The Stack**: A large-scale dataset of permissively licensed source code in multiple programming languages; used for code LLMs. [[HuggingFace](https://huggingface.co/datasets/bigcode/the-stack-v2)]

1. **RedPajama**: A replication of LLaMA’s training data recipe with open datasets; spans web, books, arXiv, and more. [[Github](https://github.com/togethercomputer/RedPajama-Data)]

1. **SlimPajama-627B-DC**: A deduplicated and filtered subset of RedPajama (627B tokens); optimized for clean and efficient training. [[HuggingFace](https://huggingface.co/datasets/MBZUAI-LLM/SlimPajama-627B-DC)]

1. **Alpaca-CoT**: Instruction-following dataset enhanced with Chain-of-Thought (CoT) reasoning prompts; used for dialogue fine-tuning. [[Github](https://github.com/PhoebusSi/Alpaca-CoT?tab=readme-ov-file)]

1. **LLaVA-Pretrain**: A multimodal dataset with image-text pairs for training visual language models like LLaVA. [[HuggingFace](https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain)]

1. **Wikipedia**: Structured and encyclopedic content; a foundational source for general-purpose language models. [[HuggingFace](https://huggingface.co/datasets/wikimedia/wikipedia)]

1. **C4**: A cleaned version of CommonCrawl data, widely used in models like T5 for high-quality web text. [[HuggingFace](https://huggingface.co/datasets/allenai/c4)]

1. **BookCorpus**: Contains free fiction books; often used to teach models long-form language understanding. [[HuggingFace](https://huggingface.co/datasets/bookcorpus/bookcorpus)]

1. **Arxiv**: Scientific paper corpus from arXiv, covering physics, math, CS, and more; useful for academic language modeling. [[HuggingFace](https://huggingface.co/datasets/arxiv-community/arxiv_dataset)]

1. **PubMed**: Biomedical literature dataset from the PubMed database; key resource for medical domain models. [[Source](https://pubmed.ncbi.nlm.nih.gov/download/)]

1. **StackExchange**: Community Q&A data covering domains like programming, math, philosophy, etc.; useful for QA and dialogue tasks. [[Source](https://archive.org/details/stackexchange)]

1. **OpenWebText2**: A high-quality open-source web text dataset based on URLs commonly cited on Reddit; GPT-style training corpus. [[Source](https://openwebtext2.readthedocs.io/en/latest/)]

1. **OpenWebMath**: A dataset of math questions and answers; designed to improve mathematical reasoning in LLMs. [[HuggingFace](https://huggingface.co/datasets/open-web-math/open-web-math)]

1. **Falcon-RefinedWeb**: Filtered web data used in training Falcon models; emphasizes data quality through rigorous preprocessing. [[HuggingFace](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)]

1. **CCI 3.0**: A large-scale multi-domain Chinese web corpus, suitable for training high-quality Chinese LLMs. [[HuggingFace](https://huggingface.co/datasets/BAAI/CCI3-Data)]

1. **OmniCorpus**: A unified multimodal dataset (text, image, audio) designed for general-purpose AI training. [[Github](https://github.com/OpenGVLab/OmniCorpus?tab=readme-ov-file)]

1. **WanJuan3.0**: A diverse and large-scale Chinese dataset including news, fiction, QA, and more; released by OpenDataLab. [[Source](https://opendatalab.org.cn/OpenDataLab/WanJuan3)]



## 0 Data Characteristics across LLM Stages

[**⬆️top**](#table-of-contents)

### Data for Pretraining

1. **OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents**
   Hugo Laurençon, Lucile Saulnier, Léo Tronchon, et al. *NeurIPS 2023*. [[Paper](https://neurips.cc/virtual/2023/poster/73589 )]
2. **Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books**
   Yukun Zhu, Ryan Kiros, Richard Zemel, et al. *ICCV 2015*. [[Paper](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zhu_Aligning_Books_and_ICCV_2015_paper.pdf)]

### Data for Continual Pre-training

1. **MedicalGPT: Training Medical GPT Model**
   Ming Xu. 2025. [[Github](https://github.com/shibing624/MedicalGPT)]
2. **BBT-Fin: Comprehensive Construction of Chinese Financial Domain Pre-trained Language Model, Corpus and Benchmark**
   Dakuan Lu, Hengkui Wu, Jiaqing Liang, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2302.09432 )]

### Data for Supervised Fine-Tuning (SFT)

#### General Instruction Following

1. **Free dolly: Introducing the world’s first truly open instruction-tuned llm**
Mike Conover, Matt Hayes, Ankit Mathur, et al. *2023*. [[Source](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm)]

#### Specific Domain Usage

1. **MedicalGPT: Training Medical GPT Model** [[Github](https://github.com/shibing624/MedicalGPT)]
2. **DISC-LawLLM: Fine-tuning Large Language Models for Intelligent Legal Services**
   Shengbin Yue, Wei Chen, Siyuan Wang, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2309.11325)]

### Data for Reinforcement Learning (RL)

#### RLHF

1. **MedicalGPT: Training Medical GPT Model** [[Github](https://github.com/shibing624/MedicalGPT)]
2. **UltraFeedback: Boosting Language Models with Scaled AI Feedback**
   Ganqu Cui, Lifan Yuan, Ning Ding, et al. *ICML 2024*. [[Paper](https://arxiv.org/abs/2310.01377)]

#### RoRL

1. **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning**
   DeepSeek-AI. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.12948)]
2. **Kimi k1.5: Scaling Reinforcement Learning with LLMs**
   Kimi Team. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.12599)]

### Data for Retrieval-Augmented Generation (RAG)

1. **DISC-LawLLM: Fine-tuning Large Language Models for Intelligent Legal Services** [[Paper](https://arxiv.org/abs/2309.11325)]
2. **DH-RAG: A Dynamic Historical Context-Powered Retrieval-Augmented Generation Method for Multi-Turn Dialogue**
   Feiyuan Zhang, Dezhi Zhu, James Ming, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.13847)]
3. **Medical Graph RAG: Towards Safe Medical Large Language Model via Graph Retrieval-Augmented Generation**
   Junde Wu, Jiayuan Zhu, Yunli Qi, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2408.04187)]
4. **ERAGent: Enhancing Retrieval-Augmented Language Models with Improved Accuracy, Efficiency, and Personalization**
   Yunxiao Shi, Xing Zi, Zijing Shi, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.06683)]
5. **PersonaRAG: Enhancing Retrieval-Augmented Generation Systems with User-Centric Agents**
   Saber Zerhoudi, Michael Granitzer. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.09394)]

### Data for LLM Evaluation

1. **MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI**
   Xiang Yue, Yuansheng Ni, Kai Zhang, et al. *CVPR 2024*. [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Yue_MMMU_A_Massive_Multi-discipline_Multimodal_Understanding_and_Reasoning_Benchmark_for_CVPR_2024_paper.pdf)]
2. **LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models**
   Haitao Li, You Chen, Qingyao Ai, et al. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2409.20288)]
3. **What disease does this patient have? a large-scale open domain question answering dataset from medical exams**
   Di Jin, Eileen Pan, Nassim Oufattole, et al. *AAAI 2021*. [[Paper](https://arxiv.org/abs/2009.13081)]
4. **Evaluating Large Language Models Trained on Code**
   Mark Chen, Jerry Tworek, Heewoo Jun, et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2107.03374)]

### Data for LLM Agents

1. **STeCa: Step-level Trajectory Calibration for LLM Agent Learning**
   Hanlin Wang, Jian Wang, Chak Tou Leong, Wenjie Li. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2502.14276)]
2. **Large Language Model-Based Agents for Software Engineering: A Survey**
   Junwei Liu, Kaixin Wang, Yixuan Chen, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.02977)]
3. **Advancing LLM Reasoning Generalists with Preference Trees**
   Lifan Yuan, Ganqu Cui, Hanbin Wang, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2404.02078)]
4. **Tool Learning in the Wild: Empowering Language Models as Automatic Tool Agents**
   Zhengliang Shi, Shen Gao, Lingyong Yan, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2405.16533)]
5. **Enhancing Chat Language Models by Scaling High-quality Instructional Conversations**
   Ning Ding, Yulin Chen, Bokai Xu, et al. *EMNLP 2023*. [[Paper](https://aclanthology.org/2023.emnlp-main.183/)]

## 1 Data Processing for LLM

### 1.1 Data Acquisition

[⬆️top](#table-of-contents)

#### Public Data Sources

Open-source or copyright-free resources

1. **Common Crawl**: A large-scale publicly accessible web crawl dataset that provides massive raw webpages and metadata. It serves as a crucial raw data source in typical pretraining data pipelines, where it undergoes multiple processing steps such as cleaning, deduplication, and formatting to produce high-quality corpora for downstream model training. [[Source](https://commoncrawl.org/)]
2. **CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages**
   Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, et al. *LREC-COLING 2024.* [[Paper](https://aclanthology.org/2024.lrec-main.377.pdf)]
3. **Project Gutenberg**: A large collection of free eBooks from the public domain; supports training language models on long-form literary text. [[Source](https://www.gutenberg.org/)]
4. **Open Library**: A global catalog of books with metadata and some open-access content; useful for multilingual and knowledge-enhanced language modeling. [[Source](https://openlibrary.org/)]
5. **GitHub**: The world’s largest open-source code hosting platform; supports training models for code generation and understanding. [[Source](https://github.com/)]
6. **GitLab**: A DevOps platform for hosting both private and open-source projects; provides high-quality programming and documentation data. [[Source](https://gitlab.com/)]
7. **Bitbucket**: A source code hosting platform by Atlassian; suitable for mining enterprise-level software development data. [[Source](https://bitbucket.org/product/)]
8. **The Stack: 3 TB of permissively licensed source code**
   Denis Kocetkov, Raymond Li, Loubna Ben Allal, et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2211.15533)]
9. **CodeSearchNet Challenge: Evaluating the State of Semantic Code Search**
   Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, et al. *arXiv 2019*. [[Paper](https://arxiv.org/abs/1909.09436)]

#### Website Crawling

1. **An Empirical Comparison of Web Content Extraction Algorithms**
   Janek Bevendorff, Sanket Gupta, Johannes Kiesel, Benno Stein. *SIGIR 2023*. [[Paper](https://dl.acm.org/doi/10.1145/3539618.3591920)]
2. **Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction**
   Adrien Barbaresi. *ACL 2021 Demo*. [[Paper](https://aclanthology.org/2021.acl-demo.15/)]
3. **Fact or Fiction: Content Classification for Digital Libraries**
   Aidan Finn, N. Kushmerick, Barry Smyth. *DELOS Workshops / Conferences 2001.* [[Paper](https://www.semanticscholar.org/paper/Fact-or-Fiction%3A-Content-Classification-for-Digital-Finn-Kushmerick/73ccd5c477b37a082f66557a1793852d405e4b6d)]

#### Website Crawling Tools

1. **Beautiful Soup**: A Python-based library for parsing HTML and XML documents; supports extracting structured information from static web pages. [[Source](https://beautiful-soup-4.readthedocs.io/en/latest/)]
2. **Selenium**: A browser automation tool that enables interaction with dynamic web pages; suitable for scraping JavaScript-heavy content. [[Github](https://github.com/seleniumhq/selenium)]
3. **Playwright**: A browser automation framework developed by Microsoft; supports multi-browser environments and is ideal for high-quality, concurrent web scraping tasks. [[Source](https://playwright.dev/)]
4. **Puppeteer**: A Node.js library that provides a high-level API to control headless Chrome or Chromium; useful for scraping complex pages, taking screenshots, or generating PDFs. [[Source](https://pptr.dev/)]

#### Layout Analysis Pipelines

Extract text from hand-written or non-textual data (e.g., scanned PDF documents)

##### Pipelines

Extract text using multiple components as a pipeline, including segmentation and OCR

1. **PaddleOCR**: An open-source Optical Character Recognition (OCR) toolkit based on the PaddlePaddle deep learning framework; supports multilingual text detection and recognition, ideal for extracting text from images and document layout analysis. [[Github](https://github.com/paddlepaddle/paddleocr)]
2. **MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing**
   Junbo Niu, Zheng Liu, Zhuangcheng Gu, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2509.22186)]
3. **MinerU: An Open-Source Solution for Precise Document Content Extraction**
   Bin Wang, Chao Xu, Xiaomeng Zhao, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2409.18839)]

##### End-to-End Models

Extract text using multi-modal LLMs as a whole, from image to text directly

1. **DeepSeek-OCR: Contexts Optical Compression**
   Haoran Wei, Yaofeng Sun, Yukun Li. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2510.18234)]
2. **dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model**
   Yumeng Li, Guang Yang, Hao Liu, Bowen Wang, Colin Zhang. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2512.02498)]
3. **General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model**
   Haoran Wei, Chenglong Liu, Jinyue Chen, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2409.01704v1)]
4. **Focus Anywhere for Fine-grained Multi-page Document Understanding**
   Chenglong Liu, Haoran Wei, Jinyue Chen, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.14295)]

##### Entity Recognition & Linking

Identify and link entities for the extracted text

1. **UMIE: Unified Multimodal Information Extraction with Instruction Tuning**
   Lin Sun, Kai Zhang, Qingyuan Li, Renze Lou. *AAAI 2024.* [[Paper](https://ojs.aaai.org/index.php/AAAI/article/view/29873)]
2. **ChatEL: Entity Linking with Chatbots**
   Yifan Ding, Qingkai Zeng, Tim Weninger. *LREC-COLING 2024*. [[Paper](https://aclanthology.org/2024.lrec-main.275/)]
3. **WebIE: Faithful and Robust Information Extraction on the Web**
   Chenxi Whitehouse, Clara Vania, Alham Fikri Aji, et al. *ACL 2023.* [[Paper](https://aclanthology.org/2023.acl-long.428/)]
4. **Alignment-Augmented Consistent Translation for Multilingual Open Information Extraction**
   Keshav Kolluru, Muqeeth Mohammed, Shubham Mittal, et al. *ACL 2022.* [[Paper](https://aclanthology.org/2022.acl-long.179/)]

### 1.2 Data Deduplication

[⬆️top](#table-of-contents)

1. **Analysis of the Reasoning with Redundant Information Provided Ability of Large Language Models**
   Wenbei Xie. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2310.04039v1)]
2. **Scaling Laws and Interpretability of Learning from Repeated Data**
   Danny Hernandez, Tom Brown, Tom Conerly, et al. *arXiv 2022.* [[Paper](https://arxiv.org/abs/2205.10487)]

#### Exact Substring Matching

Identify samples with identical patterns, such as hashes (MD5/SHA256) or substring.

##### Hashing

Identify samples with the same MD5/SHA256 hashes.

1. **MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens**
   Anas Awadalla, Le Xue, Oscar Lo, et al. *NeurIPS 2024.* [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/40b9196c25fe1d64d87ca3a80a91d0ce-Abstract-Datasets_and_Benchmarks_Track.html)]
2. **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline**
   Guosheng Dong, Da Pan, Yiding Sun, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2408.15079)]
3. **The llama 3 herd of models**
   Llama Team, AI @ Meta. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.21783)]

##### Suffix Array

1. **The RefinedWeb dataset for falcon LLM: outperforming curated corpora with web data only**
   Guilherme Penedo, Quentin Malartic, Daniel Hesslow, et al. *NeurIPS 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3666122.3669586)]
2. **Deduplicating Training Data Makes Language Models Better**
   Katherine Lee, Daphne Ippolito, Andrew Nystrom, et al. *ACL 2022.* [[Paper](https://arxiv.org/abs/2107.06499)]

##### Bloom Filter

1. **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research**
   Luca Soldaini, Rodney Kinney, Akshita Bhagia, et al. *ACL 2024*. [[Paper](https://arxiv.org/abs/2402.00159)]
2. **DataComp: In search of the next generation of multimodal datasets**
   Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang, et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2304.14108)]

#### Approximate Hash Matching

Identify samples with similar patterns. Algorithms include SimHash, MinHash and DotHash.

1. **LSHBloom: Memory-efficient, Extreme-scale Document Deduplication**
   Arham Khan, Robert Underwood, Carlo Siebenschuh, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2411.04257)]
2. **SlimPajama-DC: Understanding Data Combinations for LLM Training**
   Zhiqiang Shen, Tianhua Tao, Liqun Ma, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2309.10818)]
3. **Noise-Robust De-Duplication at Scale**
   Emily Silcock, Luca D'Amico-Wong, Jinglin Yang, Melissa Dell. *arXiv 2022.* [[Paper](https://arxiv.org/abs/2210.04261)]

**Sample-Level:**

1. **The llama 3 herd of models** [[Paper](https://arxiv.org/abs/2407.21783)]
2. **Deduplicating Training Data Makes Language Models Better** [[Paper](https://arxiv.org/abs/2107.06499)]
3. **The RefinedWeb dataset for falcon LLM: outperforming curated corpora with web data only**
   Guilherme Penedo, Quentin Malartic, Daniel Hesslow, et al. *NeurIPS 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3666122.3669586)]

**Line-Level:**

1. **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline** [[Paper](https://arxiv.org/abs/2408.15079)]

**Code Data:**

1. **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline** [[Paper](https://arxiv.org/abs/2408.15079)]
2. **DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence**
   Daya Guo, Qihao Zhu, Dejian Yang, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2401.14196)]

#### Approximate Embedding Clustering

Identify samples with similar semantics.

1. **FairDeDup: Detecting and Mitigating Vision-Language Fairness Disparities in Semantic Dataset Deduplication**
   Eric Slyman, Stefan Lee, Scott Cohen, Kushal Kafle. *CVPR 2024.* [[Paper](https://arxiv.org/abs/2404.16123)]
2. **SemDeDup: Data-efficient learning at web-scale through semantic deduplication**
   Amro Abbas, Kushal Tirumala, Dániel Simig, et al. *ICLR 2023.* [[Paper](https://iclr.cc/virtual/2023/13610)]
3. **D4: Improving LLM Pretraining via Document De-Duplication and Diversification**
   Kushal Tirumala, Daniel Simig, Armen Aghajanyan, Ari Morcos. *NeurIPS 2023.* [[Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8f8cbd7f7a5fb2c837e578c75e5b615-Abstract-Datasets_and_Benchmarks.html)]

#### Frequency-based Weighted Resampling

Identify and down-sample samples with high frequency:

1. **SoftDedup: an Efficient Data Reweighting Method for Speeding Up Language Model Pre-training**
   Nan He, Weichen Xiong, Hanwen Liu, et al. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.220/)]

Identify and up-sample samples with the removal rate after the entire filtering stage:

1. **DataComp: In search of the next generation of multimodal datasets**
   Samir Yitzhak Gadre, Gabriel Ilharco, Alex Fang, et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2304.14108)]

### 1.3 Data Filtering

[⬆️top](#table-of-contents)

#### Sample-level Filtering

##### (1) Statistical Evaluation

Filter samples based on statistical metrics (e.g., cosine similarity) or model characteristics (e.g., loss, perplexity).

**Perplexity Measuring:**

1. **Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models**
   Zachary Ankner, Cody Blakeney, Kartik Sreenivasan, et al. *ICLR 2025.* [[Paper](https://iclr.cc/virtual/2025/poster/31214)]
2. **Smaller Language Models are capable of selecting Instruction-Tuning Training Data for Larger Language Models**
   Dheeraj Mekala, Alex Nguyen, Jingbo Shang. *ACL 2024*. [[Paper](https://aclanthology.org/2024.findings-acl.623/)]
3. **From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning**
   Ming Li, Yong Zhang, Zhitao Li, et al. *NAACL 2024*. [[Paper](https://arxiv.org/abs/2308.12032)]
4. **Superfiltering: Weak-to-Strong Data Filtering for Fast Instruction-Tuning**
   Ming Li, Yong Zhang, Shwai He, et al. *ACL 2024.* [[Paper](https://doi.org/10.48550/arXiv.2402.00530)]
5. **Improving Pretraining Data Using Perplexity Correlations**
   Tristan Thrush, Christopher Potts, Tatsunori Hashimoto. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.05816)]

**Influence Assessment: Assess sample impact on LLM performance or learning process (e.g., model parameters)**

1. **Data-efficient Fine-tuning for LLM-based Recommendation**
   Xinyu Lin, Wenjie Wang, Yongqi Li, et al. *SIGIR 2024.* [[Paper](https://arxiv.org/abs/2401.17197)]
2. **SHED: Shapley-Based Automated Dataset Refinement for Instruction Fine-Tuning**
   Yexiao He, Ziyao Wang, Zheyu Shen, et al. *NeurIPS 2024.* [[Paper](https://arxiv.org/abs/2405.00705)]

**Clustering: Cluster semantically similar samples - select within the clusters reduces redundancy, while select across the clusters increases diversity**

1. **SmallToLarge (S2L): Scalable Data Selection for Fine-tuning Large Language Models by Summarizing Training Trajectories of Small Models**
   Yu Yang, Siddhartha Mishra, Jeffrey Chiang, et al. *NeurIPS 2024.* [[Paper](https://neurips.cc/virtual/2024/poster/95679)]
2. **Effective Pruning of Web-Scale Datasets Based on Complexity of Concept Clusters**
   Amro Abbas, Evgenia Rusak, Kushal Tirumala, et al. *arXiv 2024*. [[Paper](https://doi.org/10.48550/arXiv.2401.04578)]

##### (2) Model Scoring

Filter samples based on sample quality evaluated by LLM.

1. **SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection**
   Han Shen, Pin-Yu Chen, Payel Das, Tianyi Chen. *ICLR 2025.* [[Paper](https://iclr.cc/virtual/2025/poster/29422)]
2. **SCAR: Data Selection via Style-Consistency-Aware Response Ranking for Efficient Instruction Tuning of Large Language Models**
   Zhuang Li, Yuncheng Hua, Thuy-Trang Vu, et al. *ACL 2025.* [[Paper](https://arxiv.org/abs/2406.10882)]
3. **QuRating: Selecting High-Quality Data for Training Language Models**
   Alexander Wettig, Aatmik Gupta, Saumya Malik, Danqi Chen. *ICML 2024.* [[Paper](https://arxiv.org/abs/2402.09739)]
4. **What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning**
   Wei Liu, Weihao Zeng, Keqing He, et al. *ICLR 2024.* [[Paper](https://arxiv.org/abs/2312.15685)]

##### (3) Hybrid Methods

Filter samples using multiple types of methods.

1. **When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale**
   Max Marion, Ahmet Üstün, Luiza Pozzobon, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2309.04564)]
2. **Instruction Mining: Instruction Data Selection for Tuning Large Language Models**
   Yihan Cao, Yanbin Kang, Chi Wang, Lichao Sun. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2307.06290)]
3. **MoDS: Model-oriented Data Selection for Instruction Tuning**
   Qianlong Du, Chengqing Zong, Jiajun Zhang. *arXiv 2023.* [[Paper](https://doi.org/10.48550/arXiv.2311.15653)]

#### Content-level Filtering

Filter samples with specific information, including

##### Meaningless Text (e.g., special characters and unnecessary texts)

1. **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline** [[Paper](https://arxiv.org/abs/2408.15079)]
2. **The llama 3 herd of models** [[Paper](https://arxiv.org/abs/2407.21783)]
3. **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research** [[Paper](https://arxiv.org/abs/2402.00159)]
4. **When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale**
   Max Marion, Ahmet Üstün, Luiza Pozzobon, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2309.04564)]

##### Language Filtering (using [fastText](https://aclanthology.org/E17-2068.pdf), [langdetect](https://pypi.org/project/langdetect/), or [CLD2](https://pypi.org/project/pycld2/))

1. **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research** [[Paper](https://arxiv.org/abs/2402.00159)]
2. **The RefinedWeb dataset for falcon LLM: outperforming curated corpora with web data only**
   Guilherme Penedo, Quentin Malartic, Daniel Hesslow, et al. *NeurIPS 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3666122.3669586)]
3. **Exploring the limits of transfer learning with a unified text-to-text transformer**
   Colin Raffel, Noam Shazeer, Adam Roberts, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/1910.10683v4)]
4. **The Pile: An 800GB Dataset of Diverse Text for Language Modeling**
   Leo Gao, Stella Biderman, Sid Black, et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2101.00027)]
5. **CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data**
   Guillaume Wenzek, Marie - Anne Lachaux, Alexis Conneau, et al. *LREC 2020.* [[Paper](https://aclanthology.org/2020.lrec-1.494/)]

##### Toxic Information (e.g., spam, gambling, and pornographic content)

1. **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline** [[Paper](https://arxiv.org/abs/2408.15079)]
2. **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research** [[Paper](https://arxiv.org/abs/2402.00159)]
3. **The RefinedWeb dataset for falcon LLM: outperforming curated corpora with web data only**
   Guilherme Penedo, Quentin Malartic, Daniel Hesslow, et al. *NeurIPS 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3666122.3669586)]
4. **Llama 2: Open Foundation and Fine-Tuned Chat Models**
   GenAI, Meta. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2307.09288)]

##### Sensitive information (e.g., personally identifiable information)

1. **DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4**
   Zhengliang Liu, Yue Huang, Xiaowei Yu, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2303.11032)]
2. **Analyzing Leakage of Personally Identifiable Information in Language Models**
   Nils Lukas, Ahmed Salem, Robert Sim, et al. *IEEE S&P 2023.* [[Paper](https://arxiv.org/abs/2302.00539)]

### 1.4 Data Domain Selection

[⬆️top](#table-of-contents)

1. **A Survey on Data Selection for Language Models**
   Alon Albalak, Yanai Elazar, Sang Michael Xie, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2402.16827)]

2. **A Survey on Data Selection for LLM Instruction Tuning**
   Jiahao Wang, Bolin Zhang, Qianlong Du, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2402.05123)]

#### Similarity-based Data Selection

Select subset of data with similar characteristics as the target data

##### Cosine Similarity

1. **Efficient Continual Pre-training for Building Domain Specific Large Language Models**
   Yong Xie, Karan Aggarwal, Aitzaz Ahmad. *Findings of ACL 2024*. [[Paper](https://aclanthology.org/2024.findings-acl.606/)]

##### Bag-of-Words Similarity

1. **Data Selection for Language Models via Importance Resampling**
   Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang. *NeurIPS 2023.* [[Paper](https://doi.org/10.48550/arXiv.2302.03169)]

##### Lexicon Set Overlap

1. **Enabling On-Device Large Language Model Personalization with Self-Supervised Data Selection and Synthesis**
   Ruiyang Qin, Jun Xia, Zhenge Jia, et al. *DAC 2024.* [[Paper](https://doi.org/10.1145/3649329.3655665)]

##### Bayes-based Selection

1. **CoLoR-Filter: Conditional Loss Reduction Filtering for Targeted Language Model Pre-training**
   David Brandfonbrener, Hanlin Zhang, Andreas Kirsch, et al. *NeurIPS 2024.* [[Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b0f25f0a63cc544d506e4c1374a3c807-Abstract-Conference.html)]

#### Optimization-based Data Selection

Select subset of data towards improving model performance on target tasks

##### Linear Search (Datamodel)

1. **DSDM: model-aware dataset selection with datamodels**
   Logan Engstrom, Axel Feldmann, Aleksander Mądry. *ICML 2024.* [[Paper](https://dl.acm.org/doi/10.5555/3692070.3692568)]
2. **LESS: Selecting Influential Data for Targeted Instruction Tuning**
   Mengzhou Xia, Sadhika Malladi, Suchin Gururangan, et al. *ICML 2024.* [[Paper](https://doi.org/10.48550/arXiv.2402.04333)]
3. **TSDS: Data Selection for Task-Specific Model Finetuning**
   Zifan Liu, Amin Karbasi, Theodoros Rekatsinas. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.11303)]

#### Model-based Data Selection

Select subset of data with the help of LLM

1. **Autonomous Data Selection with Language Models for Mathematical Texts**
   Yifan Zhang, Yifan Luo, Yang Yuan, et al. *ICLR 2024.* [[Paper](https://iclr.cc/virtual/2024/22423)]

### 1.5 Data Mixing

[⬆️top](#table-of-contents)

1. **Mixtera: A Data Plane for Foundation Model Training**
   Maximilian Böther, Xiaozhe Yao, Tolga Kerimoglu, Dan Graur, Viktor Gsteiger, Ana Klimovic. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2502.19790)]
2. **Scalable Data Ablation Approximations for Language Models through Modular Training and Merging**
   Clara Na, Ian Magnusson, Ananya Harsh Jha, et al. *EMNLP 2024.* [[Paper](https://arxiv.org/abs/2410.15661v1)]
3. **Mixture-of-LoRAs: An Efficient Multitask Tuning for Large Language Models**
   Wenfeng Feng, Chuzhan Hao, Yuewei Zhang, et al. *COLING 2024.* [[Paper](https://arxiv.org/abs/2403.03432v1)]

#### Before-Training Mixing (Human Experience)

Empirical set mixing ratio (e.g., complexity and diversity)

1. **Exploring the limits of transfer learning with a unified text-to-text transformer** [[Paper](https://arxiv.org/abs/1910.10683v4)]
2. **Maximize Your Data's Potential: Enhancing LLM Accuracy with Two-Phase Pretraining**
   Steven Feng, Shrimai Prabhumoye, Kezhi Kong, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2412.15285)]
3. **SlimPajama-DC: Understanding Data Combinations for LLM Training**
   SlimPajama-DC: Understanding Data Combinations for LLM Training, *arXiv 2024.* [[Paper](https://arxiv.org/abs/2309.10818)]
4. **BiMix: Bivariate Data Mixing Law for Language Model Pretraining**
   Ce Ge, Zhijian Ma, Daoyuan Chen, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.14908)]

#### Before-Training Mixing (Model-Based Optimization)

Logically decide the best mixing ratio based on other factors using models

1. **RegMix: Data Mixture as Regression for Language Model Pre-training**
   Qian Liu, Xiaosen Zheng, Niklas Muennighoff, et al. *ICLR 2025.* [[Paper](https://iclr.cc/virtual/2025/poster/30960)]
2. **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance**
   Jiasheng Ye, Peiju Liu, Tianxiang Sun, et al. *ICLR 2025.* [[Paper](https://arxiv.org/abs/2403.16952)]
3. **CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models**
   Jiawei Gu, Zacc Yang, Chuanghao Ding, et al. *EMNLP 2024.* [[Paper](https://aclanthology.org/2024.emnlp-main.903)]
4. **BiMix: Bivariate Data Mixing Law for Language Model Pretraining**
   Ce Ge, Zhijian Ma, Daoyuan Chen, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.14908)]
5. **D-CPT Law: Domain-specific Continual Pre-Training Scaling Law for Large Language Models**
   Haoran Que, Jiaheng Liu, Ge Zhang, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2406.01375)]
6. **Data Proportion Detection for Optimized Data Management for Large Language Models**
   Hao Liang, Keshi Zhao, Yajie Yang, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2409.17527)]

#### During-Training Mixing (Bilevel Optimization)

Find the best mixing ratio that minimizes both training and validation loss

1. **ScaleBiO: Scalable Bilevel Optimization for LLM Data Reweighting**
   Rui Pan, Jipeng Zhang, Xingyuan Pan, et al. *ACL 2025.* [[Paper](https://arxiv.org/abs/2406.19976)]
2. **DoGE: Domain Reweighting with Generalization Estimation**
   Simin Fan, Matteo Pagliardini, Martin Jaggi. *ICML 2024.* [[Paper](https://icml.cc/virtual/2024/poster/34869)]

#### During-Training Mixing (Distributionally Robust Optimization).

Find the best mixing ratio with Distributionally Robust Optimization (DRO)

1. **Task-level Distributionally Robust Optimization for Large Language Model-based Dense Retrieval**
   Guangyuan Ma, Yongliang Ma, Xing Wu, et al. *AAAI 2025.* [[Paper](https://arxiv.org/abs/2408.10613)]
2. **DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining**
   Sang Michael Xie, Hieu Pham, Xuanyi Dong, et al. *NeurIPS 2023.* [[Paper](https://arxiv.org/abs/2305.10429)]



### 1.6 Data Distillation and Synthesis

[⬆️top](#table-of-contents)

1. **How to Synthesize Text Data without Model Collapse?**
   Xuekai Zhu, Daixuan Cheng, Hengli Li, et al. *ICML 2025*. [[Paper](https://arxiv.org/abs/2412.14689)]
2. **Differentially Private Synthetic Data via Foundation Model APIs 2: Text**
   Chulin Xie, Zinan Lin, Arturs Backurs, et al. *ICML 2024.* [[Paper](https://arxiv.org/abs/2403.01749v2)]
3. **WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions**
   Can Xu, Qingfeng Sun, Kai Zheng, et al. *ICLR 2024*. [[Paper](https://iclr.cc/virtual/2024/poster/19164)]
4. **LLM See, LLM Do: Leveraging Active Inheritance to Target Non-Differentiable Objectives**
   Luísa Shimabucoro, Sebastian Ruder, Julia Kreutzer, et al. *EMNLP 2024.* [[Paper](https://aclanthology.org/2024.emnlp-main.521)]
5. **Augmenting Math Word Problems via Iterative Question Composing**
   Haoxiong Liu, Yifan Zhang, Yifan Luo, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2401.09003)]

#### Pre-training Data Augmentation

Augment raw pre-training text into various formats to scale data

##### Rephrasing

Rephrasing raw corpora into various styles

1. **Rephrasing the Web: A Recipe for Compute and Data-Efficient Language Modeling**
   Pratyush Maini, Skyler Seto, Richard Bai, et al. *ACL 2024*. [[Paper](https://aclanthology.org/2024.acl-long.757/)]

##### Instruction Augmentation

Convert raw corpora into instructions

1. **Instruction Pre-Training: Language Models are Supervised Multitask Learners**
   Daixuan Cheng, Yuxian Gu, Shaohan Huang, et al. *EMNLP 2024*. [[Paper](https://arxiv.org/abs/2406.14491)]

##### Image Caption Augmentation

1. **VeCLIP: Improving CLIP Training via Visual-Enriched Captions**
   Zhengfeng Lai, Haotian Zhang, Bowen Zhang, et al. *ECCV 2024*. [[Paper](https://dl.acm.org/doi/10.1007/978-3-031-72946-1_7)]
2. **Improving CLIP Training with Language Rewrites**
   Lijie Fan, Dilip Krishnan, Phillip Isola, et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2305.20088)]

#### SFT Task Data Augmentation

Augment fine-tuning text for specific use cases (e.g., domain augmentation, alignment, agentic LLM, etc.)

##### Domain Data Synthesis

1. **Structural Entropy Guided Agent for Detecting and Repairing Knowledge Deficiencies in LLMs**
   Yifan Wei, Xiaoyan Yu, Tengfei Pan, et al. *NeurIPS 2025*. [[Paper](https://openreview.net/forum?id=hTGqC1h8Ig)]
2. **Multistage Collaborative Knowledge Distillation from a Large Language Model for Semi-Supervised Sequence Generation**
   Jiachen Zhao, Wenlong Zhao, Andrew Drozdov, et al. *ACL 2024*. [[Paper](https://arxiv.org/abs/2311.08640)]
3. **Synthetic Data (Almost) from Scratch: Generalized Instruction Tuning for Language Models**
   Haoran Li, Qingxiu Dong, Zhengyang Tang, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2402.13064)]

##### Instruction Data Synthesis

1. **AgentInstruct: Toward Generative Teaching with Agentic Flows**
   Arindam Mitra, Luciano Del Corro, Guoqing Zheng, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2407.03502)]
2. **Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing**
   Zhangchen Xu, Fengqing Jiang, Luyao Niu, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2406.08464)]
3. **Self-Instruct: Aligning Language Models with Self-Generated Instructions**
   Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, et al. *ACL 2023.* [[Paper](https://aclanthology.org/2023.acl-long.754)]

##### Agentic Data Synthesis

1. **Kimi K2: Open Agentic Intelligence**
   Kimi Team. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2507.20534)]

##### Privacy-Preserving Distillation

1. **PDSS: A Privacy-Preserving Framework for Step-by-Step Distillation of Large Language Models**
   Tao Fan, Weijing Chen, Yan Kang, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2406.12403)]

#### Reasoning Data Augmentation

Synthesize reasoning steps using, e.g., CoT.

1. **LIMO: Less is More for Reasoning**
   Yixin Ye, Zhen Huang, Yang Xiao, et al. *COLM 2025.* [[Paper](https://doi.org/10.48550/arXiv.2502.03387)]
1. **Distilling System 2 into System 1**
   Ping Yu, Jing Xu, Jason Weston, Ilia Kulikov. *arXiv 2024* [[Paper](https://arxiv.org/abs/2407.06023)]

##### Reasoning Ability Distillation

1. **Distilling Reasoning Capabilities into Smaller Language Models**
   Kumar Shridhar, Alessandro Stolfo, Mrinmaya Sachan. *ACL 2024*. [[Paper](https://aclanthology.org/2023.findings-acl.441/)]
2. **Symbolic chain-of-thought distillation: Small models can also "think" step-by-step**
   Liunian Harold Li, Jack Hessel, Youngjae Yu, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2306.14050)]
3. **Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes**
   Cheng-Yu Hsieh, Chun-Liang Li, Chih-kuan Yeh, et al. *ACL 2023*. [[Paper](https://aclanthology.org/2023.findings-acl.507/)]

##### Reasoning Step Augmentation

1. **Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling**
   Zhenyu Hou, Xin Lv, Rui Lu, et al. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2501.11651)]
2. **Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations**
   Peiyi Wang, Lei Li, Zhihong Shao, et al. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.510)]
3. **Let's Verify Step by Step**
   Hunter Lightman, Vineet Kosaraju, Yura Burda, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.20050)]

#### Reinforcement Learning

1. **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena**
   Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. *NeurIPS 2023*. [[Paper](https://dl.acm.org/doi/10.5555/3666122.3668142)]
2. **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback**
   Yuntao Bai, Andy Jones, Kamal Ndousse, et al. *arXiv 2022.* [[Paper](https://doi.org/10.48550/arXiv.2204.05862)]

#### Retrieval-Augmentation Generation

1. **LLMs Can Easily Learn to Reason from Demonstrations: Structure, Not Content, Is What Matters!**
   Dacheng Li, Shiyi Cao, Tyler Griggs, et al. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2502.07374)]
2. **Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search**
   Maohao Shen, Guangtao Zeng, Zhenting Qi, et al. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2502.02508)]
3. **MUSTARD: Mastering Uniform Synthesis of Theorem and Proof Data**
   Yinya Huang, Xiaohan Lin, Zhengying Liu, et al. *ICLR 2024.* [[Paper](https://arxiv.org/abs/2402.08957v3)]
4. **PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning**
   Xuekai Zhu, Biqing Qi, Kaiyan Zhang, et al. *NAACL 2024*. [[Paper](https://arxiv.org/abs/2305.13888)]
5. **Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data**
   Shenglai Zeng, Jiankun Zhang, Pengfei He, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2406.14773)]
6. **NuminaMath: The largest public dataset in AI4Maths with 860k pairs of competition math problems and solutions**
   Jia Li, Edward Beeching, Lewis Tunstall, et al. *2024*. [[Paper](http://faculty.bicmr.pku.edu.cn/~dongbin/Publications/numina_dataset.pdf)]
7. **QwQ: Reflect Deeply on the Boundaries of the Unknown**
   Qwen Team. *2024*. [[Source](https://qwenlm.github.io/blog/qwq-32b-preview/)]
8. **Knowledge Distillation Using Frontier Open-source LLMs: Generalizability and the Role of Synthetic Data**
   Anup Shirgaonkar, Nikhil Pandey, Nazmiye Ceren Abay, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.18588)]
9. **Knowledge-augmented reasoning distillation for small language models in knowledge-intensive tasks**
   Minki Kang, Seanie Lee, Jinheon Baek, et al. *NeurIPS 2023*. [[Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/97faedc90260eae5c400f92d5831c3d7-Abstract-Conference.html)]
10. **Dialogue chain-of-thought distillation for commonsense-aware conversational agents**
    Hyungjoo Chae, Yongho Song, Kai Tzu-iunn Ong, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.09343)]
11. **MCC-KD: Multi-CoT consistent knowledge distillation**
    Hongzhan Chen, Siyue Wu, Xiaojun Quan, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.14747)]
12. **Large language models are reasoning teachers**
    Namgyu Ho, Laura Schmid, Se-Young Yun. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2212.10071)]
13. **Leveraging training data in few-shot prompting for numerical reasoning**
    Zhanming Jie, Wei Lu. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.18170)]
14. **Distilling reasoning capabilities into smaller language models**
    Kumar Shridhar, Alessandro Stolfo, Mrinmaya Sachan. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2212.00193)]
15. **SCOTT: Self-consistent chain-of-thought distillation**
    Peifeng Wang, Zhengyang Wang, Zheng Li, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2305.01879)]
16. **Democratizing reasoning ability: Tailored learning from large language model**
    Zhaoyang Wang, Shaohan Huang, Yuxuan Liu, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.13332)]
17. **Explanations from large language models make small reasoners better**
    Shiyang Li, Jianshu Chen, Yelong Shen, et al. *arXiv 2022*. [[Paper](https://arxiv.org/abs/2210.06726)]
18. **Training Verifiers to Solve Math Word Problems**
    Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, et al. *arXiv 2021*. [[Paper](https://arxiv.org/abs/2110.14168)]

#### Pre-training Data Augmentation

1. **Llama 2: Open Foundation and Fine-Tuned Chat Models** [[Paper](https://arxiv.org/abs/2307.09288)]
2. **The Pile: An 800GB Dataset of Diverse Text for Language Modeling** [[Paper](https://arxiv.org/abs/2101.00027)]
3. **Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research** [[Paper](https://arxiv.org/abs/2402.00159)]
4. **BERT-Tiny-Chinese**: A lightweight Chinese BERT pre-trained model released by CKIP Lab, with a small number of parameters; suitable for use as an encoder in pre-training data augmentation tasks to enhance efficiency for compact models. [[Source](https://huggingface.co/ckiplab/bert-tiny-chinese)]
5. **Case2Code: Scalable Synthetic Data for Code Generation**
   Yunfan Shao, Linyang Li, Yichuan Ma, et al. *COLING 2025*. [[Paper](https://aclanthology.org/2025.coling-main.733/)]
6. **Advancing Mathematical Reasoning in Language Models: The Impact of Problem-Solving Data, Data Synthesis Methods, and Training Stages**
   Zui Chen, Tianqiao Liu, Mi Tian, et al. *ICLR 2025*. [[Paper](https://arxiv.org/abs/2501.14002)]
7. **Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks**
   Bin Xiao, Haiping Wu, Weijian Xu, et al. *CVPR 2024*. [[Paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Xiao_Florence-2_Advancing_a_Unified_Representation_for_a_Variety_of_Vision_CVPR_2024_paper.pdf)]
8. **DiffuseMix: Label-Preserving Data Augmentation with Diffusion Models**
   Khawar Islam, Muhammad Zaigham Zaheer, Arif Mahmood, et al. *CVPR 2024*. [[Paper](https://arxiv.org/abs/2405.14881)]
9. **Magicoder: Empowering Code Generation with OSS-Instruct**
   Yuxiang Wei, Zhe Wang, Jiawei Liu, et al. *ICML 2024*. [[Paper](https://dl.acm.org/doi/10.5555/3692070.3694228)]
10. **JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models**
    Kun Zhou, Beichen Zhang, Jiapeng Wang, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.14365)]
11. **Diffusion Models and Representation Learning: A Survey**
    Michael Fuest, Pingchuan Ma, Ming Gui, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.00783)]
12. **CtrlSynth: Controllable Image Text Synthesis for Data-Efficient Multimodal Learning**
    Qingqing Cao, Mahyar Najibi, Sachin Mehta. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.11963)]
13. **Qwen2 Technical Report**
    An Yang, Baosong Yang, Binyuan Hui, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.10671)]
14. **TinyLlama: An Open-Source Small Language Model**
    Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, Wei Lu. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2401.02385)]
15. **On the Diversity of Synthetic Data and its Impact on Training Large Language Models**
    Hao Chen, Abdul Waheed, Xiang Li, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2410.15226)]
16. **Towards Effective and Efficient Continual Pre-training of Large Language Models**
    Jie Chen, Zhipeng Chen, Jiapeng Wang, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.18743)]
17. **Effective Data Augmentation With Diffusion Models**
    Brandon Trabucco, Kyle Doherty, Max Gurinas, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2302.07944)]
18. **Mistral 7B**
    Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, et al. *arXiv 2023.* [[Paper](https://doi.org/10.48550/arXiv.2310.06825)]
19. **SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis**
    Dustin Podell, Zion English, Kyle Lacey, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2307.01952)]
20. **Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus**
    Jesse Dodge, Maarten Sap, Ana Marasović, et al. *EMNLP 2021*. [[Paper](https://arxiv.org/abs/2104.08758)]
21. **First Steps of an Approach to the ARC Challenge based on Descriptive Grid Models and the Minimum Description Length Principle**
    Sébastien Ferré (Univ Rennes, CNRS, IRISA). *arXiv 2021*. [[Paper](https://arxiv.org/abs/2112.00848)]
22. **TinyBERT: Distilling BERT for Natural Language Understanding**
    Xiaoqi Jiao, Yichun Yin, Lifeng Shang, et al. *Findings of EMNLP 2020*. [[Paper](https://arxiv.org/abs/1909.10351)]
23. **HellaSwag: Can a Machine Really Finish Your Sentence?**
    Rowan Zellers, Ari Holtzman, Yonatan Bisk, et al. *ACL 2019*. [[Paper](https://arxiv.org/abs/1905.07830)]

#### SFT Data Augmentation

1. **Augmenting Math Word Problems via Iterative Question Composing** [[Paper](https://doi.org/10.48550/arXiv.2401.09003)]
2. **Key-Point-Driven Data Synthesis with its Enhancement on Mathematical Reasoning**
   Yiming Huang, Xiao Liu, Yeyun Gong, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2403.02333)]




### 1.7 End-to-End Data Processing Pipelines

[⬆️top](#table-of-contents)

#### 1.7.1 Typical data processing frameworks

1. **Data-Juicer: A One-Stop Data Processing System for Large Language Models**
   Daoyuan Chen, Yilun Huang, Zhijian Ma, et al. *SIGMOD 2024.* [[Paper](https://doi.org/10.1145/3626246.3653385)]
2. **An Integrated Data Processing Framework for Pretraining Foundation Models**
   Yiding Sun, Feng Wang, Yutao Zhu, et al. *SIGIR 2024.* [[Paper](https://doi.org/10.1145/3626772.3657671)]
3. **Dataverse: Open-Source ETL (Extract, Transform, Load) Pipeline for Large Language Models**
   Hyunbyung Park, Sukyung Lee, Gyoungjin Gim, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2403.19340v1)]

#### 1.7.2 Typical data pipelines

1. **Exploring the limits of transfer learning with a unified text-to-text transformer** [[Paper](https://arxiv.org/abs/1910.10683v4)]
2. **The RefinedWeb dataset for falcon LLM: outperforming curated corpora with web data only**
   Guilherme Penedo, Quentin Malartic, Daniel Hesslow, et al. *NeurIPS 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3666122.3669586)]
3. **Scaling Language Models: Methods, Analysis & Insights from Training Gopher**
   Jack W. Rae, Sebastian Borgeaud, Trevor Cai, et al. *arXiv 2021.* [[Paper](https://arxiv.org/abs/2112.11446v2)]
4. **CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data**
   Guillaume Wenzek, Marie - Anne Lachaux, Alexis Conneau, et al. *LREC 2020.* [[Paper](https://aclanthology.org/2020.lrec-1.494/)]
5. **Bag of Tricks for Efficient Text Classification**
   Armand Joulin, Edouard Grave, Piotr Bojanowski, Tomas Mikolov. *arXiv 2016*. [[Paper](https://aclanthology.org/E17-2068.pdf)]

#### 1.7.3 Orchestration of data pipelines

1. **Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development**
   Daoyuan Chen, Haibin Wang, Yilun Huang, et al. *ICML 2025 (Spotlight)*. [[Paper](https://doi.org/10.48550/arXiv.2407.11784)]



## 2 Data Storage for LLM

### 2.1 Data Formats

[⬆️top](#table-of-contents)

#### Training Data Format

1. **TFRecord**: A binary data storage format recommended by TensorFlow, suitable for efficient storage and reading of large-scale training data. [[Source](https://www.tensorflow.org/tutorials/load_data/tfrecord)]
2. **MindRecord**: An efficient data storage format used by MindSpore, supporting multi-platform data management. [[Source](https://www.mindspore.cn/)]
3. **tf.data.Dataset**: An abstract interface in TensorFlow representing collections of training data, enabling flexible data manipulation. [[Source](https://www.tensorflow.org/guide/data)]
4. **COCO JSON**: COCO JSON format uses structured JSON to store images and their corresponding labels, widely used in computer vision datasets. [[Source](https://cocodataset.org/)]

#### Model Data Format

1. **PyTorch-specific formats (.pt, .pth)**: PyTorch’s .pt and .pth formats are used to save model parameters and architecture, supporting model storage and loading. [[Source](https://pytorch.org/)]
2. **TensorFlow(SavedModel, .ckpt)**: TensorFlow’s SavedModel and checkpoint formats save complete model information, facilitating model reproduction and deployment. [[Source](https://www.tensorflow.org)]
3. **Hugging Face Transformers library**: Hugging Face offers a unified model format interface to facilitate saving and usage of various pretrained models. [[Source]( https://huggingface.co/)]
4. **Pickle (.pkl)**: Pickle format is used for serializing models and data, suitable for quick saving and loading. [[Source](https://docs.python.org/3/library/pickle.html)]
5. **ONNX**: An open cross-platform model format supporting model conversion and deployment across different frameworks. [[Source](https://onnx.ai)]
6. **An Empirical Study of Safetensors' Usage Trends and Developers' Perceptions**
   Beatrice Casey, Kaia Damian, Andrew Cotaj, et al. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2501.02170)]



### 2.2 Data Distribution

[⬆️top](#table-of-contents)

1. **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** [[Paper](https://arxiv.org/abs/2501.12948)]
2. **CC-GPX: Extracting High-Quality Annotated Geospatial Data from Common Crawl**
   Ilya Ilyankou, Meihui Wang, Stefano Cavazzi, et al. *SIGSPATIAL 2024.* [[Paper](https://doi.org/10.1145/3678717.3691215)]

#### Distributed Storage Systems

1. **JuiceFS**: A high-performance cloud-native distributed file system designed for efficient storage and access of large-scale data. [[Github](https://github.com/juicedata/juicefs)]
2. **3FS**: A distributed file system designed for deep learning and large-scale data processing, emphasizing high throughput and reliability. [[Github](https://github.com/deepseek-ai/3fs)]
3. **S3**: A widely used cloud storage service offering secure, scalable, and highly available object storage solutions. [[Source](https://aws.amazon.com/s3)]
4. **Hdfs architecture guide. Hadoop apache project**
    D. Borthakur et al. *Hadoop apache project, 53(1-13):2, 2008*. [[Source](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)]

#### Heterogeneous Storage Systems

1. **ProTrain: Efficient LLM Training via Memory-Aware Techniques**
   Hanmei Yang, Jin Zhou, Yao Fu, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2406.08334)]
2. **ZeRO-infinity: breaking the GPU memory wall for extreme scale deep learning**
   Samyam Rajbhandari, Olatunji Ruwase, Jeff Rasley, et al. *SC 2021.* [[Paper](https://doi.org/10.1145/3458817.3476205)]
3. **ZeRO-Offload: Democratizing Billion-Scale Model Training**
   Jie Ren, Samyam Rajbhandari, Reza Yazdani Aminabadi, et al. *USENIX ATC 2021.* [[Paper](https://www.usenix.org/system/files/atc21-ren-jie.pdf)]
4. **ZeRO: memory optimizations toward training trillion parameter models**
   Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, et al. *SC 2020.* [[Paper](https://dl.acm.org/doi/10.5555/3433701.3433727)]
5. **vDNN: virtualized deep neural networks for scalable, memory-efficient neural network design**
   Minsoo Rhu, Natalia Gimelshein, Jason Clemons, et al. *MICRO-49 2016.* [[Paper](https://dl.acm.org/doi/10.5555/3195638.3195660)]



### 2.3 Data Organization

[⬆️top](#table-of-contents)

1. **Survey of Hallucination in Natural Language Generation**
   Ziwei Ji, Nayeon Lee, Rita Frieske, et al. *ACM Computing Surveys (2022)*. [[Paper](https://dl.acm.org/doi/10.1145/3571730)]
2. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**
   Patrick Lewis, Ethan Perez, Aleksandra Piktus, et al. *NeurIPS 2020.* [[Paper](https://doi.org/10.48550/arXiv.2005.11401)]

#### Vector-Based Organization

1. **STELLA**: A large-scale Chinese vector database supporting efficient vector search and semantic retrieval applications. [[Source](https://huggingface.co/infgrad/stella-large-zh-v2)]
2. **Milvus**: An open-source vector database focused on large-scale, high-performance similarity search and analysis. [[Source](https://milvus.io)]
3. **Weaviate**: Weaviate offers a cloud-native vector search engine supporting intelligent search and knowledge graph construction for multimodal data. [[Source](https://weaviate.io)]
4. **LanceDB**: An efficient vector database designed for large-scale machine learning and recommendation systems. [[Source](https://lancedb.com)]
5. **Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation**
   Zijie Zhong, Hanwen Liu, Xiaoya Cui, et al. *COLING 2025.* [[Paper](https://doi.org/10.48550/arXiv.2406.00456)]
6. **Dense X Retrieval: What Retrieval Granularity Should We Use?**
   Tong Chen, Hongwei Wang, Sihao Chen, et al. *EMNLP 2024*. [[Paper](https://aclanthology.org/2024.emnlp-main.845/)]
7. **Scalable and Domain-General Abstractive Proposition Segmentation**
   Mohammad Javad Hosseini, Yang Gao, Tim Baumgärtner, et al. *Findings of EMNLP 2024*. [[Paper](https://aclanthology.org/2024.findings-emnlp.517/)]
8. **A Hierarchical Context Augmentation Method to Improve Retrieval-Augmented LLMs on Scientific Papers**
   Tian-Yi Che, Xian-Ling Mao, Tian Lan, et al. *KDD 2024*. [[Paper](https://dl.acm.org/doi/10.1145/3637528.3671847)]
9. **M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation**
   Jianlyu Chen, Shitao Xiao, Peitian Zhang, et al. *Findings of ACL 2024.* [[Paper](https://aclanthology.org/2024.findings-acl.137.pdf)]
10. **Thread: A Logic-Based Data Organization Paradigm for How-To Question Answering with Retrieval Augmented Generation**
    Kaikai An, Fangkai Yang, Liqun Li, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2406.13372)]
11. **GleanVec: Accelerating Vector Search with Minimalist Nonlinear Dimensionality Reduction**
    Mariano Tepper, Ishwar Singh Bhati, Cecilia Aguerrebere, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2410.22347)]
12. **The Faiss Library**
    Matthijs Douze, Alexandr Guzhva, Chengqi Deng, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2401.08281)]
13. **Similarity Search in the Blink of an Eye with Compressed Indices**
    Cecilia Aguerrebere, Ishwar Singh Bhati, Mark Hildebrand, et al. *VLDB Endowment 2023.* [[Paper](https://doi.org/10.14778/3611479.3611537)]
14. **LeanVec: Searching Vectors Faster by Making Them Fit**
    Mariano Tepper, Ishwar Singh Bhati, Cecilia Aguerrebere, et al. *arXiv 2023.* [[Paper](https://doi.org/10.48550/arXiv.2312.16335)]
15. **Towards General Text Embeddings with Multi-stage Contrastive Learning**
    Zehan Li, Xin Zhang, Yanzhao Zhang, et al. *arXiv 2023.* [[Paper](https://arxiv.org/abs/2308.03281)]

#### Graph-Based Organization

1. **ArangoDB**: A multi-model database that supports graph, document, and key-value data, suitable for handling complex relational queries. [[Source](https://arangodb.com/)]
2. **MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation**
   Tianyu Fan, Jingyuan Wang, Xubin Ren, et al. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2501.06713)]
3. **From Local to Global: A Graph RAG Approach to Query-Focused Summarization**
   Darren Edge, Ha Trinh, Newman Cheng, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2404.16130)]
4. **LightRAG: Simple and Fast Retrieval-Augmented Generation**
   Zirui Guo, Lianghao Xia, Yanhua Yu, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2410.05779)]
5. **Graph Databases Assessment: JanusGraph, Neo4j, and TigerGraph**
   Jéssica Monteiro, et al. *Perspectives and Trends in Education and Technology 2023.* [[Paper](https://doi.org/10.1007/978-981-19-6585-2_58)]
6. **Empirical Evaluation of a Cloud-Based Graph Database: the Case of Neptune**
   Ghislain Auguste Atemezing. *KGSWC 2021.* [[Paper](https://doi.org/10.1007/978-3-030-91305-2_3)]



### 2.4 Data Movement

[⬆️top](#table-of-contents)

#### Caching Data

1. **CacheLib**: An open-source, high-performance embedded caching library developed by Meta to accelerate data access and increase system throughput. [[Source](https://cachelib.org/)]
2. **Tectonic-Shift: A Composite Storage Fabric for Large-Scale ML Training**
   Mark Zhao, Satadru Pan, Niket Agarwal, et al. *USENIX ATC 2023.* [[Paper](https://www.usenix.org/conference/atc23/presentation/zhao)]
3. **Fluid: Dataset Abstraction and Elastic Acceleration for Cloud-native Deep Learning Training Jobs**
   Rong Gu, Kai Zhang, Zhihao Xu, et al. *ICDE 2022.* [[Paper](https://doi.org/10.1109/ICDE53745.2022.00209)]
4. **Quiver: An Informed Storage Cache for Deep Learning**
   Abhishek Kumar, Muthian Sivathanu. *USENIX FAST 2020.* [[Paper](https://www.usenix.org/conference/fast20/presentation/kumar)]

#### Data/Operator Offloading

1. **cedar: Optimized and Unified Machine Learning Input Data Pipelines**
   Mark Zhao, et al. *Proceedings of the VLDB Endowment, Volume 18, Issue 2, 2025.* [[Paper](https://dl.acm.org/doi/10.14778/3705829.3705861)]
2. **Pecan: cost-efficient ML data preprocessing with automatic transformation ordering and hybrid placement**
   Dan Graur, Oto Mraz, Muyu Li, et al. *USENIX ATC 2024.* [[Paper](https://dl.acm.org/doi/10.5555/3691992.3692032)]
3. **tf.data service: A Case for Disaggregating ML Input Data Processing**
   Andrew Audibert, Yang Chen, Dan Graur, et al. *SoCC 2023.* [[Paper](https://doi.org/10.1145/3620678.3624666)]
4. **Cachew: Machine Learning Input Data Processing as a Service**
   Dan Graur, Damien Aymon, Dan Kluser, et al. *USENIX ATC 2022.* [[Paper](https://www.usenix.org/conference/atc22/presentation/graur)]
5. **Borg: the next generation**
   Muhammad Tirmazi, Adam Barker, Nan Deng, et al. *EuroSys 2020*. [[Paper](https://dl.acm.org/doi/10.1145/3342195.3387517)]

#### Overlapping of storage and computing

1. **Optimizing RLHF Training for Large Language Models with Stage Fusion**
   Yinmin Zhong, Zili Zhang, Bingyang Wu, et al. *NSDI 2025*. [[Paper](https://www.usenix.org/conference/nsdi25/presentation/zhong)]
2. **SiloD: A Co-design of Caching and Scheduling for Deep Learning Clusters**
   Hanyu Zhao, Zhenhua Han, Zhi Yang, et al. *EuroSys 2023.* [[Paper](https://doi.org/10.1145/3552326.3567499)]
3. **Optimization by Simulated Annealing**
   S. Kirkpatrick, C. D. Gelatt, Jr., M. P. Vecchi. *Science, 220(4598):671–680, 1983*. [[Paper](https://www.science.org/doi/10.1126/science.220.4598.671)]



### 2.5 Data Fault Tolerance

[⬆️top](#table-of-contents)

#### Checkpoints

1. **PaddleNLP**: PaddleNLP supports checkpoint saving and resuming during training, enabling fault tolerance and recovery for long-running training tasks. [[Source](https://paddlenlp.readthedocs.io)]
2. **MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs**
   Ziheng Jiang, Haibin Lin, Yinmin Zhong, et al. *USENIX NSDI 2024.* [[Paper](https://www.usenix.org/conference/nsdi24/presentation/jiang-ziheng)]
3. **ByteCheckpoint: A Unified Checkpointing System for Large Foundation Model Development**
   Borui Wan, Mingji Han, Yiyao Sheng, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2407.20143)]
4. **GEMINI: Fast Failure Recovery in Distributed Training with In-Memory Checkpoints**
   Zhuang Wang, Zhen Jia, Shuai Zheng, et al. *SOSP 2023.* [[Paper](https://doi.org/10.1145/3600006.3613145)]
5. **CheckFreq: Frequent, Fine-Grained DNN Checkpointing**
   Jayashree Mohan, Amar Phanishayee, Vijay Chidambaram. *USENIX FAST 2021.* [[Paper](https://www.usenix.org/conference/fast21/presentation/mohan)]

#### Redundant Computations

1. **ReCycle: Resilient Training of Large DNNs using Pipeline Adaptation**
   Swapnil Gandhi, Mark Zhao, Athinagoras Skiadopoulos, et al. *SOSP 2024*. [[Paper](https://arxiv.org/abs/2405.14009)]
2. **Bamboo: Making Preemptible Instances Resilient for Affordable Training of Large DNNs**
   John Thorpe, Pengzhan Zhao, Jonathan Eyolfson, et al.  *NSDI 2023* . [[Paper](https://www.usenix.org/conference/nsdi23/presentation/thorpe)]
3. **Oobleck: Resilient Distributed Training of Large Models Using Pipeline Templates**
   Insu Jang, Zhenning Yang, Zhen Zhang, et al. *SOSP 2023*. [[Paper](https://dl.acm.org/doi/10.1145/3600006.3613152)]



### 2.6 KV Cache

[⬆️top](#table-of-contents)

#### Cache Space Management

1. **Efficient Memory Management for Large Language Model Serving with PagedAttention**
   Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, et al. *SOSP 2023.* [[Paper](https://arxiv.org/abs/2309.06180)]
2. **VTensor: Using Virtual Tensors to Build a Layout-oblivious AI Programming Framework**
   Feng Yu, Jiacheng Zhao, Huimin Cui, et al. *PACT 2020.* [[Paper](https://dl.acm.org/doi/pdf/10.1145/3410463.3414664)]

#### KV Placement

1. **Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention**
   Bin Gao, Zhuomin He, Puru Sharma, et al. *USENIX ATC 2024.* [[Paper](https://arxiv.org/abs/2403.19708)]
2. **RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation**
   Chao Jin, Zili Zhang, Xuanlin Jiang, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2404.12457)]

#### KV Shrinking

1. **Adaptive KV-Cache Compression without Manually Setting Budget**
   Chenxia Tang, Jianchun Liu, Hongli Xu, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2509.03136)]
2. **Fast State Restoration in LLM Serving with HCache**
   Shiwei Gao, Youmin Chen, Jiwu Shu. *EuroSys 2025.* [[Paper](https://arxiv.org/abs/2410.05004)]
3. **CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving**
   Yuhan Liu, Hanchen Li, Yihua Cheng, et al. *SIGCOMM 2024.* [[Paper](https://dl.acm.org/doi/abs/10.1145/3651890.3672274)]
4. **MiniCache: KV Cache Compression in Depth Dimension for Large Language Models**
   Akide Liu, Jing Liu, Zizheng Pan, et al. *NeurIPS 2024*. [[Paper](https://neurips.cc/virtual/2024/poster/93380)]
5. **Animating rotation with quaternion curves**
   Ken Shoemake. *ACM SIGGRAPH Computer Graphics, Volume 19, Issue 3. 1985*. [[Paper](https://dl.acm.org/doi/10.1145/325165.325242)]

#### KV Indexing

1. **ChunkAttention: Efficient Self-Attention with Prefix-Aware KV Cache and Two-Phase Partition**
   Lu Ye, Ze Tao, Yong Huang, et al. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.623/)]
2. **BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix Sharing and Throughput-oriented Token Batching**
   Zhen Zheng, Xin Ji, Taosong Fang, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2412.03594)]



## 3 Data Serving for LLM

### 3.1 Data Shuffling

[⬆️top](#table-of-contents)

#### Data Shuffling for Training

1. **Velocitune: A Velocity-based Dynamic Domain Reweighting Method for Continual Pre-training**
   Zheheng Luo, Xin Zhang, Xiao Liu, et al. *ACL 2025*. [[Paper](https://arxiv.org/abs/2411.14318)]
2. **Mixtera: A Data Plane for Foundation Model Training**
   Maximilian Böther, Xiaozhe Yao, Tolga Kerimoglu, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2502.19790)]
3. **How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition**
   Guanting Dong, Hongyi Yuan, Keming Lu, et al. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.12/)]
4. **Mixture-of-Skills: Learning to Optimize Data Usage for Fine-Tuning Large Language Models**
   Minghao Wu, Thuy-Trang Vu, Lizhen Qu, et al. *EMNLP 2024.* [[Paper](https://aclanthology.org/2024.emnlp-main.787/)]
5. **Strategic Data Ordering: Enhancing Large Language Model Performance through Curriculum Learning**
   Jisu Kim, Juhwan Lee. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2405.07490)]
6. **Data Pruning via Moving-one-Sample-out**
   Haoru Tan, Sitong Wu, Fei Du, et al. *NeurIPS 2023*. [[Paper](https://arxiv.org/abs/2310.14664)]
7. **NLU on Data Diets: Dynamic Data Subset Selection for NLP Classification Tasks**
   Jean-michel Attendu, Jean-philippe Corbeil. *SustaiNLP @ ACL 2023.* [[Paper](https://aclanthology.org/2023.sustainlp-1.9/)]
8. **Efficient Online Data Mixing For Language Model Pre-Training**
   Alon Albalak, Liangming Pan, Colin Raffel, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2312.02406)]
9. **BERT on a Data Diet: Finding Important Examples by Gradient-Based Pruning**
   Mohsen Fayyaz, Ehsan Aghazadeh, Ali Modarressi, et al. *ENLSP @ NeurIPS2022.* [[Paper](https://doi.org/10.48550/arXiv.2211.05610)]
10. **Scaling Laws for Neural Language Models**
      Jared Kaplan, Sam McCandlish, Tom Henighan, et al. *arXiv 2020*. [[Paper](https://arxiv.org/abs/2001.08361)]
11. **Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory**
    James L. McClelland, Bruce L. McNaughton, Randall C. O’Reilly. *Psychological Review 1995.* [[Paper](https://cseweb.ucsd.edu/~gary/258/jay.pdf)]
12. **Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem**
    M. McCloskey, N. J. Cohen. *Psychology of Learning and Motivation 1989.* [[Paper](https://www.sciencedirect.com/science/article/abs/pii/S0079742108605368)]



#### Data Selection for RAG

1. **Cohere rerank**: Cohere's rerank model reorders initial retrieval results to improve relevance to the query, making it a key component for building high-quality RAG systems. [[Source](https://docs.cohere.com)]
2. **ASRank: Zero-Shot Re-Ranking with Answer Scent for Document Retrieval**
   Abdelrahman Abdallah, Jamshid Mozafari, Bhawna Piryani, et al. *NAACL 2025.* [[Paper](https://doi.org/10.48550/arXiv.2501.15245)]
3. **MAIN-RAG: Multi-Agent Filtering Retrieval-Augmented Generation**
   Chia-Yuan Chang, Zhimeng Jiang, Vineeth Rakesh, et al. *arXiv 2025*. [[Paper](https://arxiv.org/abs/2501.00332)]
4. **ARAGOG: Advanced RAG Output Grading**
   Matouš Eibich, Shivay Nagpal, Alexander Fred-Ojala. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2404.01037)]
5. **Large Language Model Is Not a Good Few-shot Information Extractor, but a Good Reranker for Hard Samples!**
   Yubo Ma, Yixin Cao, YongChing Hong, et al. *Findings of EMNLP 2023*. [[Paper](https://aclanthology.org/2023.findings-emnlp.710/)]
6. **Chatlaw: A Multi-Agent Collaborative Legal Assistant with Knowledge Graph Enhanced Mixture-of-Experts Large Language Model**
   Jiaxi Cui, Munan Ning, Zongjian Li, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2306.16092v2)]
7. **RankVicuna: Zero-Shot Listwise Document Reranking with Open-Source Large Language Models**
   Ronak Pradeep, Sahel Sharifymoghaddam, Jimmy Lin. *arXiv 2023.* [[Paper](https://doi.org/10.48550/arXiv.2309.15088)]



### 3.2 Data Compression

[⬆️top](#table-of-contents)

#### RAG Knowledge Compression

1. **Context Embeddings for Efficient Answer Generation in RAG**
   David Rau, Shuai Wang, Hervé Déjean, et al. *WSDM 2025.* [[Paper](https://doi.org/10.48550/arXiv.2407.09252)]
2. **xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token**
   Xin Cheng, Xun Wang, Xingxing Zhang, et al. *NeurIPS 2024.* [[Paper](https://doi.org/10.48550/arXiv.2405.13792)]
3. **RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation**
   Fangyuan Xu, Weijia Shi, Eunsol Choi. *ICLR 2024.* [[Paper](https://iclr.cc/virtual/2024/poster/17885)]
4. **Compressing Long Context for Enhancing RAG with AMR-based Concept Distillation**
   Kaize Shi, Xueyao Sun, Qing Li, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2405.03085)]
5. **Familiarity-Aware Evidence Compression for Retrieval-Augmented Generation**
   Dongwon Jung, Qin Liu, Tenghao Huang, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2409.12468)]

#### Prompt Compression

1. **LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression**
   Huiqiang Jiang, Qianhui Wu, Xufang Luo, et al. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.91/)]
2. **LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression**
   Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, et al. *Findings of ACL 2024.* [[Paper](https://aclanthology.org/2024.findings-acl.57/)]
3. **Learning to Compress Prompts with Gist Tokens**
   Jesse Mu, Xiang Lisa Li, Noah Goodman. *NeurIPS 2023.* [[Paper](https://arxiv.org/abs/2304.08467)]
4. **LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models**
   Huiqiang Jiang, Qianhui Wu, Chin-Yew Lin, et al. *EMNLP 2023.* [[Paper](https://aclanthology.org/2023.emnlp-main.825.pdf)]
5. **Adapting Language Models to Compress Contexts**
   Alexis Chevalier, Alexander Wettig, Anirudh Ajith, et al. *EMNLP 2023.* [[Paper](https://aclanthology.org/2023.emnlp-main.232.pdf)]



### 3.3 Data Packing

[⬆️top](#table-of-contents)

#### Short Sequence Insertion

1. **Fewer Truncations Improve Language Modeling**
   Hantian Ding, Zijian Wang, Giovanni Paolini, et al. *ICML 2024.* [[Paper](https://doi.org/10.48550/arXiv.2404.10830)]
2. **Bucket Pre-training is All You Need**
   Hongtao Liu, Qiyao Peng, Qing Yang, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2407.07495)]

#### Sequence Combination Optimization

1. **Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum**
   Hadi Pouransari, Chun-Liang Li, Jen-Hao Rick Chang, et al. *NeurIPS 2024.* [[Paper](https://doi.org/10.48550/arXiv.2405.13226)]
2. **Efficient Sequence Packing without Cross-contamination: Accelerating Large Language Models without Impacting Performance**
   Mario Michael Krell, Matej Kosec, Sergio P. Perez, et al. *arXiv 2021.* [[Paper](https://doi.org/10.48550/arXiv.2107.02027)]

#### Semantic-Based Packing

1. **Structured Packing in LLM Training Improves Long Context Utilization**
   Konrad Staniszewski, Szymon Tworkowski, Sebastian Jaszczur, et al. *AAAI 2025.* [[Paper](https://doi.org/10.48550/arXiv.2312.17296)]
2. **In-context Pretraining: Language Modeling Beyond Document Boundaries**
   Weijia Shi, Sewon Min, Maria Lomeli, et al. *ICLR 2024.* [[Paper](https://doi.org/10.48550/arXiv.2310.10638)]



### 3.4 Data Provenance

[⬆️top](#table-of-contents)

1. **A comprehensive survey on data provenance: : State-of-the-art approaches and their deployments for IoT security enforcement**
   Md Morshed Alam, Weichao Wang. *Journal of Computer Security, Volume 29, Issue 4. 2021*. [[Paper](https://dl.acm.org/doi/abs/10.3233/JCS-200108)]

#### Embedding Markers

1. **Bileve: Securing Text Provenance in Large Language Models Against Spoofing with Bi-level Signature**
   Tong Zhou, Xuandong Zhao, Xiaolin Xu, et al. *NeurIPS 2024*. [[Paper](https://arxiv.org/abs/2406.01946)]
2. **An Unforgeable Publicly Verifiable Watermark for Large Language Models**
   Aiwei Liu, Leyi Pan, Xuming Hu, et al. *ICLR 2024*. [[Paper](https://arxiv.org/abs/2307.16230)]
3. **Undetectable Watermarks for Language Models**
   Miranda Christ, et al. in *Proceedings of the 37th Annual Conference on Learning Theory (COLT 2024)*. [[Paper](https://arxiv.org/abs/2306.09194)]
4. **A Watermark for Large Language Models**
   John Kirchenbauer, Jonas Geiping, Yuxin Wen, et al. *ICML 2023*. [[Paper](https://arxiv.org/abs/2301.10226)]
5. **Publicly-Detectable Watermarking for Language Models**
   Jaiden Fairoze, Sanjam Garg, Somesh Jha, et al. *arXiv 2023*. [[Paper](https://arxiv.org/abs/2310.18491)]

#### Statistical Provenance

1. **A Watermark for Large Language Models** [[Paper](https://arxiv.org/abs/2301.10226)]



## 4 LLM for Data Management

### 4.1 LLM for Data Analysis

[⬆️top](#table-of-contents)

#### 4.1.1 LLM for Structured Data Analysis

##### 4.1.1.1 Relational Data Analysis

###### LLM for Natural Language Interfaces

1. **QueryBear**: A practical NL2SQL system for relational databases that lets users ask questions in plain English and build internal data tools without coding. Supports PostgreSQL and MySQL. [[Source](https://querybear.com)]
2. **RubikSQL: Lifelong Learning Agentic Knowledge Base as an Industrial NL2SQL System**
   Zui Chen, Han Li, Xinhao Zhang, et al. *to be submitted to VLDB 2026 (PVLDB Vol. 19). (2025)*. [[Paper](https://doi.org/10.48550/arXiv.2508.17590)]
3. **Cracking SQL Barriers: An LLM-based Dialect Translation System**
   Wei Zhou, Yuyang Gao, Xuanhe Zhou, Guoliang Li. *SIGMOD 2025*. [[Paper](https://dbgroup.cs.tsinghua.edu.cn/ligl/SIGMOD25-CrackSQL.pdf)]
4. **OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment**
   Xiangjin Xie, Guangwei Xu, Lingyan Zhao, Ruijie Guo. *Proc. ACM Manag. Data, Vol. 3, No. 3, Article 194, pp. 1-24 (2025)*. [[Paper](https://doi.org/10.1145/3725331)]
5. **CrackSQL: A Hybrid SQL Dialect Translation System Powered by Large Language Models**
   Wei Zhou, Yuyang Gao, Xuanhe Zhou, Guoliang Li. *arXiv 2025 (extended from SIGMOD 2025 demo)*. [[Paper](https://doi.org/10.48550/arXiv.2504.00882)]
6. **Data Interpreter: An LLM Agent for Data Science**
   Sirui Hong, Yizhang Lin, Bang Liu, et al. *ACL 2025 Findings, pp. 19796-19821 (2025)*. [[Paper](https://aclanthology.org/2025.findings-acl.1016/)]
7. **Reasoning-SQL: Reinforcement Learning with SQL-Tailored Partial Rewards for Reasoning-Enhanced Text-to-SQL**
   Mohammadreza Pourreza, Shayan Talaei, Ruoxi Sun, et al. *COLM 2025*. [[Paper](https://openreview.net/forum?id=HbwkIDWQgN)]
8. **An advanced AI driven database system**
   M. Tedeschi, S. Rizwan, C. Shringi, et al. *EDULEARN25 Conference Proceedings. 2025.* [[Paper](https://arxiv.org/abs/2507.17778)]
9. **Text to Query Plans for Question Answering on Large Tables**
   Yipeng Zhang, Chen Wang, Yuzhe Zhang, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2508.18758v1)]
10. **Automatic Metadata Extraction for Text-to-SQL**
      Vladislav Shkapenyuk, Divesh Srivastava, Theodore Johnson, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2505.19988)]
11. **CSC-SQL: Corrective Self-Consistency in Text-to-SQL via Reinforcement Learning**
      Lei Sheng, Shuai-Shuai Xu. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2505.13271)]
12. **OmniSQL: Synthesizing High-quality Text-to-SQL Data at Scale**
    Haoyang Li, Shang Wu, Xiaokang Zhang, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2503.02240)]
13. **Cheaper, Better, Faster, Stronger: Robust Text-to-SQL without Chain-of-Thought or Fine-Tuning**
    Yusuf Denizay Dönder, Derek Hommel, Andrea W Wen-Yi, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2505.14174)]
14. **A Preview of XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL**
    Yingqi Gao, Yifu Liu, Xiaoxia Li, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2411.08599)]
15. **FinSQL: Model-Agnostic LLMs-based Text-to-SQL Framework for Financial Analysis**
    Chao Zhang, Yuren Mao, Yijiang Fan, et al. *SIGMOD 2024.* [[Paper](https://doi.org/10.1145/3626246.3653375)]
16. **CodeS: Towards Building Open-source Language Models for Text-to-SQL**
    Haoyang Li, et al. *Proceedings of the ACM on Management of Data, Volume 2, Issue 3, 2024.* [[Paper](https://doi.org/10.1145/3654930)]
17. **The Dawn of Natural Language to SQL: Are We Fully Ready?**
    Boyan Li, Yuyu Luo, Chengliang Chai, Guoliang Li, Nan Tang. *VLDB 2024.* [[Paper](https://arxiv.org/abs/2406.01265)]
18. **Contextualized Data-Wrangling Code Generation in Computational Notebooks**
    Junjie Huang, Daya Guo, Chenglong Wang, et al. *ASE 2024*. [[Paper](https://dl.acm.org/doi/abs/10.1145/3691620.3695503)]
19. **PET-SQL: A Prompt-Enhanced Two-Round Refinement of Text-to-SQL with Cross-consistency**
    Zhishuai Li, Xiang Wang, Jingjing Zhao, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2403.09732)]
20. **CHESS: Contextual Harnessing for Efficient SQL Synthesis**
    Shayan Talaei, Mohammadreza Pourreza, Yu-Chen Chang, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2405.16755)]
21. **DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction**
    Mohammadreza Pourreza, Davood Rafiei. *NeurIPS 2023*. [[Paper](https://dl.acm.org/doi/10.5555/3666122.3667699)]
22. **Natural Language to Code Generation in Interactive Data Science Notebooks**
    Pengcheng Yin, Wen-Ding Li, Kefan Xiao, et al. *ACL 2023.* [[Paper](https://aclanthology.org/2023.acl-long.9/)]
23. **PaLM: Scaling Language Modeling with Pathways**
    Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, et al. *JMLR 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3648699.3648939)]

###### LLM for Semantic Analysis

1. **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** [[Paper](https://doi.org/10.48550/arXiv.2306.05685)]
2. **TableGPT2: A Large Multimodal Model with Tabular Data Integration** [[Paper](https://doi.org/10.48550/arXiv.2411.02059)]
3. **TableMaster: A Recipe to Advance Table Understanding with Language Models**
   Lang Cao. *arXiv 2025.* [[Paper](https://doi.org/10.48550/arXiv.2501.19378)]
4. **RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals**
   Xuanliang Zhang, Dingzirui Wang, Keyan Xu, Qingfu Zhu, Wanxiang Che. *arXiv 2025*. [[Paper](https://doi.org/10.48550/arXiv.2505.15110)]
5. **PPT: A Process-based Preference Learning Framework for Self Improving Table Question Answering Models**
   Wei Zhou, Mohsen Mesgar, Heike Adel, et al. *arXiv 2025.* [[Paper](https://arxiv.org/abs/2505.17565)]
6. **CABINET: Content Relevance based Noise Reduction for Table Question Answering**
   Sohan Patnaik, Heril Changwal, Milan Aggarwal, et al. *ICLR 2024.* [[Paper](https://doi.org/10.48550/arXiv.2402.01155)]
7. **ReAcTable: Enhancing ReAct for Table Question Answering**
   Yunjia Zhang, et al. *Proceedings of the VLDB Endowment, Volume 17, Issue 8, 2024.* [[Paper](https://doi.org/10.14778/3659437.3659452)]
8. **Table-GPT: Table Fine-tuned GPT for Diverse Table Tasks**
   Peng Li, et al. *Proceedings of the ACM on Management of Data, Volume 2, Issue 3, 2024*. [[Paper](https://dl.acm.org/doi/10.1145/3654979)]
9. **TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy**
   Weichao Zhao, Hao Feng, Qi Liu, et al. *NeurIPS 2024.* [[Paper](https://doi.org/10.48550/arXiv.2406.01326)]
10. **Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding**
      Zilong Wang, Hao Zhang, Chun-Liang Li, et al. *ICLR 2024.* [[Paper](https://doi.org/10.48550/arXiv.2401.04398)]
11. **TaPERA: Enhancing Faithfulness and Interpretability in Long-Form Table QA by Content Planning and Execution-based Reasoning**
    Yilun Zhao, Lyuhao Chen, Arman Cohan, Chen Zhao. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.692/)]
12. **Multimodal Table Understanding**
    Mingyu Zheng, Xinwei Feng, Qingyi Si, et al. *ACL 2024*. [[Paper](https://aclanthology.org/2024.acl-long.493/)]
13. **TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data**
    Fengbin Zhu, Ziyang Liu, Fuli Feng, et al. *ICAIF 2024.* [[Paper](https://doi.org/10.1145/3677052.3698685)]
14. **S3HQA: A Three-Stage Approach for Multi-hop Text-Table Hybrid Question Answering**
    Fangyu Lei, Xiang Li, Yifan Wei, et al. *ACL 2023.* [[Paper](https://aclanthology.org/2023.acl-short.147/)]



##### 4.1.1.2 Graph Data Analysis

1. **Blazegraph**: A high-performance graph database that supports RDF/SPARQL queries, commonly used in semantic web and knowledge graph analysis. [[Source](https://blazegraph.com/)]
2. **GraphDB**: A triplestore with ontology reasoning and SPARQL query support, widely used for enterprise knowledge management and semantic search. [[Source](https://graphdb.ontotext.com/)]
3. **Neo4j**: Neo4j is one of the most popular graph databases, based on the property graph model, supporting complex relationship queries and visual analytics. [[Github](https://github.com/neo4j/neo4j)]
4. **A Comparison of Current Graph Database Models**
   Renzo Angles. *ICDEW 2012.* [[Paper](https://doi.org/10.1109/ICDEW.2012.31)]

###### Natural Language To Graph Analysis Query

1. **R3-NL2GQL: A Model Coordination and Knowledge Graph Alignment Approach for NL2GQL**
   Yuhang Zhou, Yu He, Siyu Tian, et al. *Findings of EMNLP 2024.* [[Paper](https://aclanthology.org/2024.findings-emnlp.800/)]
2. **NAT-NL2GQL: A Novel Multi-Agent Framework for Translating Natural Language to Graph Query Language**
   Yuanyuan Liang, Tingyu Xie, Gan Peng, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.10434)]
3. **Graph Learning in the Era of LLMs: A Survey from the Perspective of Data, Models, and Tasks**
   Xunkai Li, Zhengyu Wu, Jiayi Wu, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2412.12456)]
4. **Leveraging Biomolecule and Natural Language through Multi-Modal Learning: A Survey**
   Qizhi Pei, Lijun Wu, Kaiyuan Gao, et al. *arXiv 2024*. [[Paper](https://arxiv.org/abs/2403.01528)]

###### LLM-based Semantic Analysis

1. **FlexKBQA: A Flexible LLM-Powered Framework for Few-Shot Knowledge Base Question Answering**
   Zhenyu Li, Sunqi Fan, Yu Gu, et al. *AAAI 2024.* [[Paper](https://doi.org/10.48550/arXiv.2308.12060)]
2. **GraphGPT: Graph Instruction Tuning for Large Language Models**
   Jiabin Tang, Yuhao Yang, Wei Wei, et al. *SIGIR 2024.* [[Paper](https://doi.org/10.48550/arXiv.2310.13023)]
3. **Interactive-KBQA: Multi-Turn Interactions for Knowledge Base Question Answering with Large Language Models**
   Guanming Xiong, Junwei Bao, Wen Zhao. *ACL 2024.* [[Paper](https://aclanthology.org/2024.acl-long.569/)]
4. **InstructGraph: Boosting Large Language Models via Graph-centric Instruction Tuning and Preference Alignment**
   Jianing Wang, Junda Wu, Yupeng Hou, et al. *Findings of ACL 2024.* [[Paper](https://aclanthology.org/2024.findings-acl.801/)]
5. **Call Me When Necessary: LLMs can Efficiently and Faithfully Reason over Structured Environments**
   Sitao Cheng, Ziyuan Zhuang, Yong Xu, et al. *Findings of ACL 2024.* [[Paper](https://doi.org/10.48550/arXiv.2403.08593)]
6. **Language is All a Graph Needs**
   Ruosong Ye, Caiqi Zhang, Runhui Wang, et al. *EACL 2024.* [[Paper](https://aclanthology.org/2024.findings-eacl.132/)]
7. **Direct Preference Optimization: Your Language Model is Secretly a Reward Model**
   Rafael Rafailov, Archit Sharma, Eric Mitchell, et al. *NeurIPS 2023.* [[Paper](https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html)]
8. **UniKGQA: Unified Retrieval and Reasoning for Solving Multi-hop Question Answering Over Knowledge Graph**
   Jinhao Jiang, Kun Zhou, Wayne Xin Zhao, et al. *ICLR 2023.* [[Paper](https://doi.org/10.48550/arXiv.2212.00959)]
9. **StructGPT: A General Framework for Large Language Model to Reason over Structured Data**
   Jinhao Jiang, Kun Zhou, Zican Dong, et al. *EMNLP 2023.* [[Paper](https://doi.org/10.48550/arXiv.2305.09645)]
10. **Subgraph Retrieval Enhanced Model for Multi-hop Knowledge Base Question Answering**
    Jing Zhang, Xiaokang Zhang, Jifan Yu, et al. *ACL 2022.* [[Paper](https://aclanthology.org/2022.acl-long.396/)]
11. **RoBERTa: A Robustly Optimized BERT Pretraining Approach**
    Yinhan Liu, Myle Ott, Naman Goyal, et al. *arXiv 2019*. [[Paper](https://arxiv.org/abs/1907.11692)]
12. **Inductive representation learning on large graphs**
    William L. Hamilton, Rex Ying, Jure Leskovec. *NeurIPS 2017.* [[Paper](https://dl.acm.org/doi/10.5555/3294771.3294869)]
13. **Semi-Supervised Classification with Graph Convolutional Networks**
    Thomas N. Kipf, Max Welling. *ICLR 2017.* [[Paper](https://doi.org/10.48550/arXiv.1609.02907)]



#### 4.1.2 LLM for Semi-Structured Data Analysis

1. **ST-Raptor: LLM-Powered Semi-Structured Table Question Answering**
   Zirui Tang, Boyu Niu, Xuanhe Zhou, et al. *SIGMOD 2026.* (2025). [[Paper](https://arxiv.org/abs/2508.18190v3)]
2. **Querying Semi-Structured Data**
   Serge Abiteboul. *ICDT 1997.* [[Paper](https://dl.acm.org/doi/10.5555/645502.656103)]

##### 4.1.2.1 Markup Language

##### 4.1.2.2 Semi-Structured Tables

1. **MiMoTable: A Multi-scale Spreadsheet Benchmark with Meta Operations for Table Reasoning**
   Zheng Li, Yang Du, Mao Zheng, et al. *COLING 2025.* [[Paper](https://doi.org/10.48550/arXiv.2412.11711)]
2. **AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries**
   Jiayi Wang, Guoliang Li. *CIDR 2025* [[Paper](https://vldb.org/cidrdb/papers/2025/p32-wang.pdf)]
3. **SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation**
   Zeyao Ma, Bohan Zhang, Jing Zhang, et al. *NeurIPS 2024.* [[Paper](https://doi.org/10.48550/arXiv.2406.14991)]
4. **TempTabQA: Temporal Question Answering for Semi-Structured Tables**
   Vivek Gupta, Pranshu Kandoi, Mahek Bhavesh Vora, et al. *EMNLP 2023.* [[Paper](https://doi.org/10.48550/arXiv.2311.08002)]



#### 4.1.3 LLM for Unstructured Data Analysis

##### 4.1.3.1 Documents

1. **AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries** [[Paper](https://vldb.org/cidrdb/papers/2025/p32-wang.pdf)]
2. **Focus Anywhere for Fine-grained Multi-page Document Understanding** [[Paper](https://arxiv.org/abs/2405.14295)]
3. **Exploring the limits of transfer learning with a unified text-to-text transformer** [[Paper](https://arxiv.org/abs/1910.10683v4)]
4. **General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model** [[Paper](https://arxiv.org/abs/2409.01704v1)]
5. **Palimpzest: Optimizing AI-Powered Analytics with Declarative Query Processing**
    Chunwei Liu, Matthew Russo, Michael Cafarella, et al. *CIDR 2025* [[Paper](https://www.vldb.org/cidrdb/papers/2025/p12-liu.pdf)]
6. **DocFormerv2: Local Features for Document Understanding**
   Srikar Appalaraju, Peng Tang, Qi Dong, et al. *AAAI 2024.* [[Paper](https://doi.org/10.1609/aaai.v38i2.27828)]
7. **mPLUG-DocOwl 1.5: Unified Structure Learning for OCR-free Document Understanding**
   Anwen Hu, Haiyang Xu, Jiabo Ye, et al. *Findings of EMNLP 2024.* [[Paper](https://aclanthology.org/2024.findings-emnlp.175/)]
8. **DocPedia: Unleashing the Power of Large Multimodal Model in the Frequency Domain for Versatile Document Understanding**
   Hao Feng, Qi Liu, Hao Liu, et al. *SCIS 2024.* [[Paper](https://doi.org/10.48550/arXiv.2311.11810)]
9. **Towards Accurate and Efficient Document Analytics with Large Language Models**
   Y. Lin, M. Hulsebos, R. Ma, et al. *arXiv 2024.* [[Paper](https://arxiv.org/abs/2405.04674/)]
10. **Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding**
    Kenton Lee, Mandar Joshi, Iulia Turc, et al. *ICML 2023.* [[Paper](https://dl.acm.org/doi/10.5555/3618408.3619188?ref=localhost)]
11. **Unifying Vision, Text, and Layout for Universal Document Processing**
     Zineng Tang, Ziyi Yang, Guoxin Wang, et al. *CVPR 2023.* [[Paper](https://arxiv.org/abs/2212.02623v3)]
12. **DUBLIN: Visual Document Understanding By Language-Image Network**
     Kriti Aggarwal, Aditi Khandelwal, Kumar Tanmay, et al. *EMNLP Industry Track 2023.* [[Paper](https://aclanthology.org/2023.emnlp-industry.65/)]
13. **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale**
     Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, et al. *ICLR  2021.* [[Paper](https://iclr.cc/virtual/2021/oral/3458)]
14. **The JPEG Still Picture Compression Standard**
     Gregory K. Wallace. *Communications of the ACM 1991.* [[Paper](https://doi.org/10.1145/103085.103089)]



##### 4.1.3.2 Program Language Analysis

###### LLM as Program Vulnerability Detection Tools

1. **Pre-training by Predicting Program Dependencies for Vulnerability Analysis Tasks**
   Zhongxin Liu, Zhijie Tang, Junwei Zhang, et al. *ICSE 2024.* [[Paper](https://doi.org/10.1145/3597503.3639142)]
2. **Large Language Model for Vulnerability Detection: Emerging Results and Future Directions**
   Xin Zhou, Ting Zhang, David Lo. *ICSE-NIER 2024.* [[Paper](https://doi.org/10.1145/3639476.3639762)]
3. **Vulnerability Detection by Learning From Syntax-Based Execution Paths of Code**
   Junwei Zhang, Zhongxin Liu, Xing Hu, et al. *IEEE TSE 2023.* [[Paper](https://ieeexplore.ieee.org/document/10153647)]
4. **Software Vulnerability Detection with GPT and In-Context Learning**
   Zhihong Liu, Qing Liao, Wenchao Gu, et al. *DSC 2023.* [[Paper](https://ieeexplore.ieee.org/abstract/document/10381286)]
5. **CodeBERT: A Pre-Trained Model for Programming and Natural Languages**
   Zhangyin Feng, Daya Guo, Duyu Tang, et al. *Findings of EMNLP 2020.* [[Paper](https://aclanthology.org/2020.findings-emnlp.139/)]
6. **The Probabilistic Relevance Framework: BM25 and Beyond**
   Stephen Robertson, et al. *Foundations and Trends in Information Retrieval, Volume 3, Issue 4, 2009.* [[Paper](https://dl.acm.org/doi/10.1561/1500000019)]

###### LLM-based Semantic-aware Analysis

1.  **Repoformer: Selective Retrieval for Repository-Level Code Completion**
   Di Wu, Wasi Uddin Ahmad, Dejiao Zhang, et al. *ICML 2024.* [[Paper](https://dl.acm.org/doi/abs/10.5555/3692070.3694253)]
2.  **Large Language Models are Few-Shot Summarizers: Multi-Intent Comment Generation via In-Context Learning**
   Mingyang Geng, Shangwen Wang, Dezun Dong, et al. *ICSE 2024.* [[Paper](https://doi.org/10.1145/3597503.3608134)]
3.  **Automatic Semantic Augmentation of Language Model Prompts (for Code Summarization)**
   Toufique Ahmed, Kunal Suresh Pai, Premkumar Devanbu, Earl Barr. *ICSE 2024.* [[Paper](https://doi.org/10.1145/3597503.3639183)]
4.  **CoCoMIC: Code Completion by Jointly Modeling In-file and Cross-file Context**
   Yangruibo Ding, Zijian Wang, Wasi Ahmad, et al. *LREC-COLING 2024.* [[Paper](https://aclanthology.org/2024.lrec-main.305/)]
5.  **SCLA: Automated Smart Contract Summarization via LLMs and Semantic Augmentation**
   Yingjie Mao, Xiaoqi Li, Wenkai Li, et al. *arXiv 2024.* [[Paper](https://doi.org/10.48550/arXiv.2402.04863)]
6.  **Code Structure–Guided Transformer for Source Code Summarization**
   Shuzheng Gao, et al. *ACM Transactions on Software Engineering and Methodology 2023.* [[Paper](https://doi.org/10.1145/3522674)]
7.  **RepoFusion: Training Code Models to Understand Your Re