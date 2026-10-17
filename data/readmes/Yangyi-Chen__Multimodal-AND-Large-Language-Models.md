# Multimodal & Large Language Models

**Note:** This paper list is only used to record papers I read in the daily arxiv for personal needs. I only subscribe to and cover the following subjects: Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computer Vision and Pattern Recognition (cs.CV), and Machine Learning (cs.LG). If you find I missed some important and exciting work, it would be super helpful to let me know. Thanks!

**Update:** Starting from June 2024, I'm focusing on reading and recording papers that I believe offer unique insights and substantial contributions to the field.


## Table of Contents

- [Survey](#survey)
- [Position Paper](#position-paper)
- [Structure](#structure)
- [Planning](#planning)
- [Reasoning](#reasoning)
- [Generation](#generation)
- [Representation Learning](#representation-learning)
- [LLM Analysis](#llm-analysis)
- [LLM Safety](#llm-safety)
- [LLM Evaluation](#llm-evaluation)
- [LLM Reasoning](#llm-reasoning)
- [LLM Application](#llm-application)
- [LLM with Memory](#llm-with-memory)
- [LLM with Human](#llm-with-human)
- [Inference-time Scaling (via RL)](#inference-time-scaling)
- [Long-Context LLM](#long-context-llm)
- [LLM Foundation](#llm-foundation)
- [Scaling Law](#scaling-law)
- [LLM Data Engineering](#llm-data-engineering)
- [VLM Data Engineering](#vlm-data-engineering)
- [Alignment](#alignment)
- [Scalable Oversight&amp;SuperAlignment](#scalable-oversight-&-superalignment)
- [RL Foundation](#rl-foundation)
- [Beyond Bandit](#beyond-bandit)
- [Agent](#agent)
- [DeepResearch](#deepresearch)
- [SWE-Agent](#swe-agent)
- [Evolution](#evolution)
- [Interaction](#interaction)
- [Critique Modeling](#critic-modeling)
- [MoE/Specialized](#moe/specialized)
- [Vision-Language Foundation Model](#vision-language-foundation-model)
- [Vision-Language Model Analysis &amp; Evaluation](#vision-language-model-analysis&evaluation)
- [Vision-Language Model Application](#vision-language-model-application)
- [Multimodal Foundation Model](#multimodal-foundation-model)
- [Image Generation](#image-generation)
- [Diffusion](#diffusion)
- [Document Understanding](#document-understanding)
- [Tool Learning](#tool-learning)
- [Instruction Tuning](#instruction-tuning)
- [Incontext Learning](#incontext-learning)
- [Learning from Feedback](#learning-from-feedback)
- [Reward Modeling](#reward-modeling)
- [Video Foundation Model](#video-foundation-model)
- [Key Frame Detection](#key-frame-detection)
- [Pretraining](#pretraining)
- [Vision Model](#vision-model)
- [Adaptation of Foundation Model](#adaptation-of-foundation-model)
- [Prompting](#prompting)
- [Efficiency](#efficiency)
- [Analysis](#analysis)
- [Grounding](#grounding)
- [VQA Task](#vqa-task)
- [VQA Dataset](#vqa-dataset)
- [Social Good](#social-good)
- [Application](#application)
- [Benchmark &amp; Evaluation](#benchmark-&-evaluation)
- [Dataset](#dataset)
- [Robustness](#robustness)
- [Hallucination&amp;Factuality](#hallucination&factuality)
- [Cognitive NeuronScience &amp; Machine Learning](#cognitive-neuronscience-&-machine-learning)
- [Theory of Mind](#theory-of-mind)
- [Cognitive NeuronScience](#cognitive-neuronscience)
- [World Model](#world-model)
- [Resource](#resource)

## Survey

- **Multimodal Learning with Transformers: A Survey;** Peng Xu, Xiatian Zhu, David A. Clifton
- **Multimodal Machine Learning: A Survey and Taxonomy;** Tadas Baltrusaitis, Chaitanya Ahuja, Louis-Philippe Morency; Introduce 4 challenges for multi-modal learning, including representation, translation, alignment, fusion, and co-learning.
- **FOUNDATIONS & RECENT TRENDS IN MULTIMODAL MACHINE LEARNING: PRINCIPLES, CHALLENGES, & OPEN QUESTIONS;** Paul Pu Liang, Amir Zadeh, Louis-Philippe Morency
- **Multimodal research in vision and language: A review of current and emerging trends;** Shagun Uppal et al;
- **Trends in Integration of Vision and Language Research: A Survey of Tasks, Datasets, and Methods;** Aditya Mogadala et al
- **Challenges and Prospects in Vision and Language Research;** Kushal Kafle et al
- **A Survey of Current Datasets for Vision and Language Research;** Francis Ferraro et al
- **VLP: A Survey on Vision-Language Pre-training;** Feilong Chen et al
- **A Survey on Multimodal Disinformation Detection;** Firoj Alam et al
- **Vision-Language Pre-training: Basics, Recent Advances, and Future Trends;** Zhe Gan et al
- **Deep Multimodal Representation Learning: A Survey;** Wenzhong Guo et al
- **The Contribution of Knowledge in Visiolinguistic Learning: A Survey on Tasks and Challenges;** Maria Lymperaiou et al
- **Augmented Language Models: a Survey;** Grégoire Mialon et al
- **Multimodal Deep Learning;** Matthias Aßenmacher et al
- **Sparks of Artificial General Intelligence: Early experiments with GPT-4;** Sebastien Bubeck et al
- **Retrieving Multimodal Information for Augmented Generation: A Survey;** Ruochen Zhao et al
- **Is Prompt All You Need? No. A Comprehensive and Broader View of Instruction Learning;** Renze Lou et al
- **A Survey of Large Language Models;** Wayne Xin Zhao et al
- **Tool Learning with Foundation Models;** Yujia Qin et al
- **A Cookbook of Self-Supervised Learning;** Randall Balestriero et al
- **Foundation Models for Decision Making: Problems, Methods, and Opportunities;** Sherry Yang et al
- **Bridging the Gap: A Survey on Integrating (Human) Feedback for Natural Language Generation;** Patrick Fernandes et al
- **Reasoning with Language Model Prompting: A Survey;** Shuofei Qiao et al
- **Towards Reasoning in Large Language Models: A Survey;** Jie Huang et al
- **Beyond One-Model-Fits-All: A Survey of Domain Specialization for Large Language Models;** Chen Ling et al
- **Unifying Large Language Models and Knowledge Graphs: A Roadmap;** Shirui Pan et al
- **Interactive Natural Language Processing;** Zekun Wang et al
- **A Survey on Multimodal Large Language Models;** Shukang Yin et al
- **TRUSTWORTHY LLMS: A SURVEY AND GUIDELINE FOR EVALUATING LARGE LANGUAGE MODELS’ ALIGNMENT;** Yang Liu et al
- **Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback;** Stephen Casper et al
- **Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies;** Liangming Pan et al
- **Challenges and Applications of Large Language Models;** Jean Kaddour et al
- **Aligning Large Language Models with Human: A Survey;** Yufei Wang et al
- **Instruction Tuning for Large Language Models: A Survey;** Shengyu Zhang et al
- **From Instructions to Intrinsic Human Values —— A Survey of Alignment Goals for Big Models;** Jing Yao et al
- **A Survey of Safety and Trustworthiness of Large Language Models through the Lens of Verification and Validation;** Xiaowei Huang et al
- **Explainability for Large Language Models: A Survey;** Haiyan Zhao et al
- **Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models;** Yue Zhang et al
- **Survey on Factuality in Large Language Models: Knowledge, Retrieval and Domain-Specificity;** Cunxiang Wang et al
- **ChatGPT’s One-year Anniversary: Are Open-Source Large Language Models Catching up?;** Hailin Chen et al
- **Vision-Language Instruction Tuning: A Review and Analysis;** Chen Li et al
- **The Mystery and Fascination of LLMs: A Comprehensive Survey on the Interpretation and Analysis of Emergent Abilities;** Yuxiang Zhou et al
- **Efficient Large Language Models: A Survey;** Zhongwei Wan et al
- **The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision);** Zhengyuan Yang et al
- **Igniting Language Intelligence: The Hitchhiker’s Guide From Chain-of-Thought Reasoning to Language Agents;** Zhuosheng Zhang et al
- **Toward General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis;** Yafei Hu et al
- **Multimodal Foundation Models: From Specialists to General-Purpose Assistants;** Chunyuan Li et al
- **A Survey on Large Language Model based Autonomous Agents;** Lei Wang et al
- **Video Understanding with Large Language Models: A Survey;** Yunlong Tang et al
- **A Survey of Preference-Based Reinforcement Learning Methods;** Christian Wirth et al
- **AI Alignment: A Comprehensive Survey;** Jiaming Ji et al
- **A SURVEY OF REINFORCEMENT LEARNING FROM HUMAN FEEDBACK;** Timo Kaufmann et al
- **TRUSTLLM: TRUSTWORTHINESS IN LARGE LANGUAGE MODELS;** Lichao Sun et al
- **AGENT AI: SURVEYING THE HORIZONS OF MULTIMODAL INTERACTION;** Zane Durante et al
- **Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: A Short Survey;** Cedric Colas et al
- **Safety of Multimodal Large Language Models on Images and Text;** Xin Liu et al
- **MM-LLMs: Recent Advances in MultiModal Large Language Models;** Duzhen Zhang et al
- **Rethinking Interpretability in the Era of Large Language Models;** Chandan Singh et al
- **Large Multimodal Agents: A Survey;** Junlin Xie et al
- **A Survey on Data Selection for Language Models;** Alon Albalak et al
- **What Are Tools Anyway? A Survey from the Language Model Perspective;** Zora Zhiruo Wang et al
- **Best Practices and Lessons Learned on Synthetic Data for Language Models;** Ruibo Liu et al
- **A Survey on the Memory Mechanism of Large Language Model based Agents;** Zeyu Zhang et al
- **A Survey on Self-Evolution of Large Language Models;** Zhengwei Tao et al
- **When LLMs step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via Multi-modal Large Language Models;** Xianzheng Ma et al
- **An Introduction to Vision-Language Modeling;** Florian Bordes et al
- **Towards Scalable Automated Alignment of LLMs: A Survey;** Boxi Cao et al
- **A Survey on Mixture of Experts;** Weilin Cai et al
- **The Synergy between Data and Multi-Modal Large Language Models: A Survey from Co-Development Perspective;** Zhen Qin et al
- **Retrieval-Augmented Generation for Large Language Models: A Survey;** Yunfan Gao et al
- **Towards a Unified View of Preference Learning for Large Language Models: A Survey;** Bofei Gao et al
- **From Decoding to Meta-Generation: Inference-time Algorithms for Large Language Models;** Sean Welleck et al
- **A Survey on the Honesty of Large Language Models;** Siheng Li et al
- **Autoregressive Models in Vision: A Survey;** Jing Xiong et al
- **Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective;** Zhiyuan Zeng et al
- **Next Token Prediction Towards Multimodal Intelligence: A Comprehensive Survey;** Liang Chen et al
- **(MIS)FITTING: A SURVEY OF SCALING LAWS;** Margaret Li et al
- **Thus Spake Long-Context Large Language Model;** Xiaoran Liu et al
- **Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models;** Yang Sui et al
- **A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future;** Jialun Zhong et al


## Position Paper

- **Eight Things to Know about Large Language Models;** Samuel R. Bowman et al
- **A PhD Student’s Perspective on Research in NLP in the Era of Very Large Language Models;** Oana Ignat et al
- **Brain in a Vat: On Missing Pieces Towards Artificial General Intelligence in Large Language Models;** Yuxi Ma et al
- **Towards AGI in Computer Vision: Lessons Learned from GPT and Large Language Models;** Lingxi Xie et al
- **A Path Towards Autonomous Machine Intelligence;** Yann LeCun et al
- **GPT-4 Can’t Reason;** Konstantine Arkoudas et al
- **Cognitive Architectures for Language Agents;** Theodore Sumers et al
- **Large Search Model: Redefining Search Stack in the Era of LLMs;** Liang Wang et al
- **PROAGENT: FROM ROBOTIC PROCESS AUTOMATION TO AGENTIC PROCESS AUTOMATION;** Yining Ye et al
- **Language Models, Agent Models, and World Models: The LAW for Machine Reasoning and Planning;** Zhiting Hu et al
- **A Roadmap to Pluralistic Alignment;** Taylor Sorensen et al
- **Towards Unified Alignment Between Agents, Humans, and Environment;** Zonghan Yang et al
- **Video as the New Language for Real-World Decision Making;** Sherry Yang et al
- **A Mechanism-Based Approach to Mitigating Harms from Persuasive Generative AI;** Seliem El-Sayed et al
- **Concrete Problems in AI Safety;** Dario Amodei et al
- **Towards System 2 Reasoning in LLMs: Learning How to Think With Meta Chain-of-Thought;** Violet Xiang et al






## Structure

- **Finding Structural Knowledge in Multimodal-BERT;** Victor Milewski et al
- **Going Beyond Nouns With Vision & Language Models Using Synthetic Data;** Paola Cascante-Bonilla et al
- **Measuring Progress in Fine-grained Vision-and-Language Understanding;** Emanuele Bugliarello et al
- **PV2TEA: Patching Visual Modality to Textual-Established Information Extraction;** Hejie Cui et al

**Event Extraction**

- **Cross-media Structured Common Space for Multimedia Event Extraction;** Manling Li et al; Focus on image-text event extraction. A new benchmark and baseline are proposed.
- **Visual Semantic Role Labeling for Video Understanding;** Arka Sadhu et al; A new benchmark is proposed.
- **GAIA: A Fine-grained Multimedia Knowledge Extraction System;** Manling Li et al; Demo paper. Extract knowledge (relation, event) from multimedia data.
- **MMEKG: Multi-modal Event Knowledge Graph towards Universal Representation across Modalities;** Yubo Ma et al

**Situation Recognition**

- **Situation Recognition: Visual Semantic Role Labeling for Image Understanding;** Mark Yatskar et al; Focus on image understanding. Given images, do the semantic role labeling task. No text available. A new benchmark and baseline are proposed.
- **Commonly Uncommon: Semantic Sparsity in Situation Recognition;** Mark Yatskar et al; Address the long-tail problem.
- **Grounded Situation Recognition;** Sarah Pratt et al
- **Rethinking the Two-Stage Framework for Grounded Situation Recognition;** Meng Wei et al
- **Collaborative Transformers for Grounded Situation Recognition;** Junhyeong Cho et al

**Scene Graph**

- **Action Genome: Actions as Composition of Spatio-temporal Scene Graphs;** Jingwei Ji et al; Spatio-temporal scene graphs (video).
- **Unbiased Scene Graph Generation from Biased Training;** Kaihua Tang et al
- **Visual Distant Supervision for Scene Graph Generation;** Yuan Yao et al
- **Learning to Generate Scene Graph from Natural Language Supervision;** Yiwu Zhong et al
- **Weakly Supervised Visual Semantic Parsing;** Alireza Zareian, Svebor Karaman, Shih-Fu Chang
- **Scene Graph Prediction with Limited Labels;** Vincent S. Chen, Paroma Varma, Ranjay Krishna, Michael Bernstein, Christopher Re, Li Fei-Fei
- **Neural Motifs: Scene Graph Parsing with Global Context;** Rowan Zellers et al
- **Fine-Grained Scene Graph Generation with Data Transfer;** Ao Zhang et al
- **Towards Open-vocabulary Scene Graph Generation with Prompt-based Finetuning;** Tao He et al
- **COMPOSITIONAL PROMPT TUNING WITH MOTION CUES FOR OPEN-VOCABULARY VIDEO RELATION DETECTION;** Kaifeng Gao et al; Video.
- **LANDMARK: Language-guided Representation Enhancement Framework for Scene Graph Generation;** Xiaoguang Chang et al
- **TRANSFORMER-BASED IMAGE GENERATION FROM SCENE GRAPHS;** Renato Sortino et al
- **The Devil is in the Labels: Noisy Label Correction for Robust Scene Graph Generation;** Lin Li et al
- **Knowledge-augmented Few-shot Visual Relation Detection;** Tianyu Yu et al
- **Prototype-based Embedding Network for Scene Graph Generation;** Chaofan Zhen et al
- **Unified Visual Relationship Detection with Vision and Language Models;** Long Zhao et al
- **Structure-CLIP: Enhance Multi-modal Language Representations with Structure Knowledge;** Yufeng Huang et al

**Attribute**

- **COCO Attributes: Attributes for People, Animals, and Objects;** Genevieve Patterson et al
- **Human Attribute Recognition by Deep Hierarchical Contexts;** Yining Li et al; Attribute prediction in specific domains.
- **Emotion Recognition in Context;** Ronak Kosti et al; Attribute prediction in specific domains.
- **The iMaterialist Fashion Attribute Dataset;** Sheng Guo et al; Attribute prediction in specific domains.
- **Learning to Predict Visual Attributes in the Wild;** Khoi Pham et al
- **Open-vocabulary Attribute Detection;** Marıa A. Bravo et al
- **OvarNet: Towards Open-vocabulary Object Attribute Recognition;** Keyan Chen et al

**Compositionality**

- **CREPE: Can Vision-Language Foundation Models Reason Compositionally?;** Zixian Ma et al
- **Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality;** Tristan Thrush et al
- **WHEN AND WHY VISION-LANGUAGE MODELS BEHAVE LIKE BAGS-OF-WORDS, AND WHAT TO DO ABOUT IT?;** Mert Yuksekgonul et al
- **GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering;** Drew A. Hudson et al
- **COVR: A Test-Bed for Visually Grounded Compositional Generalization with Real Images;** Ben Bogin et al
- **Cops-Ref: A new Dataset and Task on Compositional Referring Expression Comprehension;** Zhenfang Chen et al
- **Do Vision-Language Pretrained Models Learn Composable Primitive Concepts?;** Tian Yun et al
- **SUGARCREPE: Fixing Hackable Benchmarks for Vision-Language Compositionality;** Cheng-Yu Hsieh et al
- **An Examination of the Compositionality of Large Generative Vision-Language Models;** Teli Ma et al

**Concept**

- **Cross-Modal Concept Learning and Inference for Vision-Language Models;** Yi Zhang et al
- **Hierarchical Visual Primitive Experts for Compositional Zero-Shot Learning;** Hanjae Kim et al

## Planning

- **Multimedia Generative Script Learning for Task Planning;** Qingyun Wang et al; Next step prediction.
- **PlaTe: Visually-Grounded Planning with Transformers in Procedural Tasks;** Jiankai Sun et al; Procedure planning.
- **P3IV: Probabilistic Procedure Planning from Instructional Videos with Weak Supervision;** He Zhao et al; Procedure planning. Using text as weak supervision to replace video clips.
- **Procedure Planning in Instructional Videos;** Chien-Yi Chang et al; Procedure planning.
- **ViLPAct: A Benchmark for Compositional Generalization on Multimodal Human Activities;** Terry Yue Zhuo et al
- **Actional Atomic-Concept Learning for Demystifying Vision-Language Navigation;** Bingqian Lin et al

## Reasoning

- **VisualCOMET: Reasoning about the Dynamic Context of a Still Image;** Jae Sung Park et al; Benchmark dataset, requiring models to reason about a still image (what happen past & next).
- **Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering;** Pan Lu et al
- **See, Think, Confirm: Interactive Prompting Between Vision and Language Models for Knowledge-based Visual Reasoning;** Zhenfang Chen et al
- **An Empirical Study of GPT-3 for Few-Shot Knowledge-Based VQA;** Zhengyuan Yang et al
- **Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering;** Pan Lu et al
- **Multimodal Chain-of-Thought Reasoning in Language Models;** Zhuosheng Zhang et al
- **LAMPP: Language Models as Probabilistic Priors for Perception and Action;** Belinda Z. Li et al
- **Visual Chain of Thought: Bridging Logical Gaps with Multimodal Infillings;** Daniel Rose et al
- **Symbol-LLM: Leverage Language Models for Symbolic System in Visual Human Activity Reasoning;** Xiaoqian Wu et al


**Common sense.**

- **Improving Commonsense in Vision-Language Models via Knowledge Graph Riddles;** Shuquan Ye et al
- **VIPHY: Probing “Visible” Physical Commonsense Knowledge;** Shikhar Singh et al
- **Visual Commonsense in Pretrained Unimodal and Multimodal Models;** Chenyu Zhang et al

## Generation

- **ClipCap: CLIP Prefix for Image Captioning;** Ron Mokady et al; Train an light-weight encoder to convert CLIP embeddings to prefix token embeddings of GPT-2.
- **Multimodal Knowledge Alignment with Reinforcement Learning;** Youngjae Yu et al; Use RL to train an encoder that projects multimodal inputs into the word embedding space of GPT-2.

## Representation Learning

- **Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering;** Peter Anderson et al
- **Fusion of Detected Objects in Text for Visual Question Answering;** Chris Alberti et al
- **VLMixer: Unpaired Vision-Language Pre-training via Cross-Modal CutMix;** Teng Wang et al
- **Vision-Language Pre-Training with Triple Contrastive Learning;** Jinyu Yang et al
- **Vokenization: Improving Language Understanding with Contextualized, Visual-Grounded Supervision;** Hao Tan et al; Use visual supervision to pretrain language models.
- **HighMMT: Quantifying Modality & Interaction Heterogeneity for High-Modality Representation Learning;** Paul Pu Liang et al
- **Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture;** Mahmoud Assran et al
- **PIGLeT: Language Grounding Through Neuro-Symbolic Interaction in a 3D World;** Rowan Zellers et al
- **Learning the Effects of Physical Actions in a Multi-modal Environment;** Gautier Dagan et al
- **Multimodality Helps Unimodality: Cross-Modal Few-Shot Learning with Multimodal Models;** Zhiqiu Lin et al
- **Learning Visual Representations via Language-Guided Sampling;** Mohamed El Banani et al
- **Image as Set of Points;** Xu Ma et al
- **ARCL: ENHANCING CONTRASTIVE LEARNING WITH AUGMENTATION-ROBUST REPRESENTATIONS;** Xuyang Zhao et al
- **BRIDGING THE GAP TO REAL-WORLD OBJECT-CENTRIC LEARNING;** Maximilian Seitzer et al
- **Learning Transferable Spatiotemporal Representations from Natural Script Knowledge;** Ziyun Zeng et al
- **Understanding and Constructing Latent Modality Structures in Multi-Modal Representation Learning;** Qian Jiang et al
- **VLM2VEC: TRAINING VISION-LANGUAGE MODELS FOR MASSIVE MULTIMODAL EMBEDDING TASKS;** Ziyan Jiang et al
- **When Does Perceptual Alignment Benefit Vision Representations?;** Shobhita Sundaram et al
- **NARAIM: Native Aspect Ratio Autoregressive Image Models;** Daniel Gallo Fernández et al
- **Masked Autoencoders Are Scalable Vision Learners;** Kaiming He et al



## LLM Analysis

- **GROKKING: GENERALIZATION BEYOND OVERFITTING ON SMALL ALGORITHMIC DATASETS;** Alethea Power et al
- **Unified View of Grokking, Double Descent and Emergent Abilities: A Perspective from Circuits Competition;** Yufei Huang et al
- **A Categorical Archive of ChatGPT Failures;** Ali Borji et al
- **Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling;** Stella Biderman  et al
- **Are Emergent Abilities of Large Language Models a Mirage?;** Rylan Schaeffer et al
- **A Drop of Ink may Make a Million Think: The Spread of False Information in Large Language Models;** Ning Bian et al
- **Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting;** Miles Turpin et al
- **SYMBOL TUNING IMPROVES IN-CONTEXT LEARNING IN LANGUAGE MODELS;** Jerry Wei et al
- **What In-Context Learning “Learns” In-Context: Disentangling Task Recognition and Task Learning;** Jane Pan et al
- **Measuring the Knowledge Acquisition-Utilization Gap in Pretrained Language Models;** Amirhossein Kazemnejad et al
- **Scaling Data-Constrained Language Models;** Niklas Muennighoff et al
- **The False Promise of Imitating Proprietary LLMs;** Arnav Gudibande et al
- **Counterfactual reasoning: Testing language models’ understanding of hypothetical scenarios;** Jiaxuan Li et al
- **Inverse Scaling: When Bigger Isn’t Better;** Ian R. McKenzie et al
- **DECODINGTRUST: A Comprehensive Assessment of Trustworthiness in GPT Models;** Boxin Wang et al
- **Lost in the Middle: How Language Models Use Long Contexts;** Nelson F. Liu et al
- **Won’t Get Fooled Again: Answering Questions with False Premises;** Shengding Hu et al
- **Generating Benchmarks for Factuality Evaluation of Language Models;** Dor Muhlgay et al
- **Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations;** Yanda Chen et al
- **Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation;** Ruiyang Ren et al
- **Large Language Models Struggle to Learn Long-Tail Knowledge;** Nikhil Kandpal et al
- **SCALING RELATIONSHIP ON LEARNING MATHEMATICAL REASONING WITH LARGE LANGUAGE MODELS;** Zheng Yuan et al
- **Multimodal Neurons in Pretrained Text-Only Transformers;** Sarah Schwettmann et al
- **SIMPLE SYNTHETIC DATA REDUCES SYCOPHANCY IN LARGE LANGUAGE MODELS;** Jerry Wei et al
- **Studying Large Language Model Generalization with Influence Functions;** Roger Grosse et al
- **Taken out of context: On measuring situational awareness in LLMs;** Lukas Berglund et al
- **OpinionGPT: Modelling Explicit Biases in Instruction-Tuned LLMs;** Patrick Haller et al
- **Neurons in Large Language Models: Dead, N-gram, Positional;** Elena Voita et al
- **Are Emergent Abilities in Large Language Models just In-Context Learning?;** Sheng Lu et al
- **The Reversal Curse: LLMs trained on “A is B” fail to learn “B is A”;** Lukas Berglund et al
- **Language Modeling Is Compression;** Grégoire Delétang et al
- **FROM LANGUAGE MODELING TO INSTRUCTION FOLLOWING: UNDERSTANDING THE BEHAVIOR SHIFT IN LLMS AFTER INSTRUCTION TUNING;** Xuansheng Wu et al
- **RESOLVING KNOWLEDGE CONFLICTS IN LARGE LANGUAGE MODELS;** Yike Wang et al
- **LARGE LANGUAGE MODELS CANNOT SELF-CORRECT REASONING YET;** Jie Huang et al
- **ASK AGAIN, THEN FAIL: LARGE LANGUAGE MODELS’ VACILLATIONS IN JUDGEMENT;** Qiming Xie et al
- **FRESHLLMS: REFRESHING LARGE LANGUAGE MODELS WITH SEARCH ENGINE AUGMENTATION;** Tu Vu et al
- **Demystifying Embedding Spaces using Large Language Models;** Guy Tennenholtz et al
- **An Emulator for Fine-Tuning Large Language Models using Small Language Models;** Eric Mitchell et al
- **UNVEILING A CORE LINGUISTIC REGION IN LARGE LANGUAGE MODELS;** Jun Zhao et al
- **DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS;** Weijia Shi et al
- **BENCHMARKING AND IMPROVING GENERATOR-VALIDATOR CONSISTENCY OF LMS;** Xiang Lisa Li et al
- **Trusted Source Alignment in Large Language Models;** Vasilisa Bashlovkina et al
- **THE UNLOCKING SPELL ON BASE LLMS: RETHINKING ALIGNMENT VIA IN-CONTEXT LEARNING;** Bill Yuchen Lin et al
- **Can Large Language Models Really Improve by Self-critiquing Their Own Plans?;** Karthik Valmeekam et al
- **TELL, DON’T SHOW: DECLARATIVE FACTS INFLUENCE HOW LLMS GENERALIZE;** Alexander Meinke et al
- **A Closer Look at the Limitations of Instruction Tuning;** Sreyan Ghosh et al
- **PERSONAS AS A WAY TO MODEL TRUTHFULNESS IN LANGUAGE MODELS;** Nitish Joshi et al
- **Beyond Probabilities: Unveiling the Misalignment in Evaluating Large Language Models;** Chenyang Lyu et al
- **Dated Data: Tracing Knowledge Cutoffs in Large Language Models;** Jeffrey Cheng et al
- **Context versus Prior Knowledge in Language Models;** Kevin Du et al
- **Training Trajectories of Language Models Across Scales;** Mengzhou Xia et al
- **Retrieval Head Mechanistically Explains Long-Context Factuality;** Wenhao Wu et al
- **Let’s Think Dot by Dot: Hidden Computation in Transformer Language Models;** Jacob Pfau et al
- **Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?;** Zorik Gekhman et al
- **An Emulator for Fine-Tuning Large Language Models using Small Language Models;** Eric Mitchell et al
- **To Code, or Not To Code? Exploring Impact of Code in Pre-training;** Viraat Aryabumi et al
- **LATENT SPACE CHAIN-OF-EMBEDDING ENABLES OUTPUT-FREE LLM SELF-EVALUATION;** Yiming Wang et al
- **Physics of Language Models: Part 3.1, Knowledge Storage and Extraction;** Zeyuan Allen-Zhu et al
- **Physics of Language Models: Part 3.2, Knowledge Manipulation;** Zeyuan Allen-Zhu et al
- **IMPROVING PRETRAINING DATA USING PERPLEXITY CORRELATIONS;** Tristan Thrush et al
- **Overtrained Language Models Are Harder to Fine-Tune;** Jacob Mitchell Springer et al
- **Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification;** Anqi Zhang et al
- **Model Merging in Pre-training of Large Language Models;** ByteDance Seed
- **How Alignment Shrinks the Generative Horizon;** Chenghao Yang et al
- **EvoLM: In Search of Lost Language Model Training Dynamics;** Zhenting Qi et al



**Calibration & Uncertainty**

- **Knowledge of Knowledge: Exploring Known-Unknowns Uncertainty with Large Language Models;** Alfonso Amayuelas et al
- **Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs;** Miao Xiong et al
- **LLAMAS KNOW WHAT GPTS DON’T SHOW: SURROGATE MODELS FOR CONFIDENCE ESTIMATION;** Vaishnavi Shrivastava et al
- **Navigating the Grey Area: How Expressions of Uncertainty and Overconfidence Affect Language Models;** Kaitlyn Zhou et al
- **R-Tuning: Teaching Large Language Models to Refuse Unknown Questions;** Hanning Zhang et al
- **Relying on the Unreliable: The Impact of Language Models’ Reluctance to Express Uncertainty;** Kaitlyn Zhou et al
- **Prudent Silence or Foolish Babble? Examining Large Language Models’ Responses to the Unknown;** Genglin Liu et al
- **Benchmarking LLMs via Uncertainty Quantification;** Fanghua Ye et al
- **Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback;** Katherine Tian et al
- **Deal, or no deal (or who knows)? Forecasting Uncertainty in Conversations using Large Language Models;** Anthony Sicilia et al
- **Calibrating Long-form Generations from Large Language Models;** Yukun Huang et al
- **Distinguishing the Knowable from the Unknowable with Language Models;** Gustaf Ahdritz et al
- **Introspective Planning: Guiding Language-Enabled Agents to Refine Their Own Uncertainty;** Kaiqu Liang et al
- **Asking the Right Question at the Right Time: Human and Model Uncertainty Guidance to Ask Clarification Questions;** Alberto Testoni et al
- **Into the Unknown: Self-Learning Large Language Models;** Teddy Ferdinan et al
- **The Internal State of an LLM Knows When It’s Lying;** Amos Azaria et al
- **SELFCHECKGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models;** Potsawee Manakul et al
- **Calibrating Large Language Models with Sample Consistency;** Qing Lyu et al
- **Gotcha! Don’t trick me with unanswerable questions! Self-aligning Large Language Models for Responding to Unknown Questions;** Yang Deng et al
- **Unfamiliar Finetuning Examples Control How Language Models Hallucinate;** Katie Kang et al
- **Few-Shot Recalibration of Language Models;** Xiang Lisa Li et al
- **When to Trust LLMs: Aligning Confidence with Response Quality and Exploring Applications in RAG;** Shuchang Tao et al
- **Linguistic Calibration of Language Models;** Neil Band et al
- **Large Language Models Must Be Taught to Know What They Don’t Know;** Sanyam Kapoor et al
- **SaySelf: Teaching LLMs to Express Confidence with Self-Reflective Rationales;** Tianyang Xu et al
- **Uncertainty is Fragile: Manipulating Uncertainty in Large Language Models;** Qingcheng Zeng et al
- **SEMANTIC UNCERTAINTY: LINGUISTIC INVARIANCES FOR UNCERTAINTY ESTIMATION IN NATURAL LANGUAGE GENERATION;** Lorenz Kuhn et al
- **I Don’t Know: Explicit Modeling of Uncertainty with an [IDK] Token;** Roi Cohen et al




## LLM Safety

- **Learning Human Objectives by Evaluating Hypothetical Behavior;** Siddharth Reddy et al
- **Universal and Transferable Adversarial Attacks on Aligned Language Models;** Andy Zou et al
- **XSTEST: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models;** Paul Röttger et al
- **Jailbroken: How Does LLM Safety Training Fail? Content Warning: This paper contains examples of harmful language;** Alexander Wei et al
- **FUNDAMENTAL LIMITATIONS OF ALIGNMENT IN LARGE LANGUAGE MODELS;** Yotam Wolf et al
- **BEAVERTAILS: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset;** Jiaming Ji et al
- **GPT-4 IS TOO SMART TO BE SAFE: STEALTHY CHAT WITH LLMS VIA CIPHER;** Youliang Yuan et al
- **Red-Teaming Large Language Models using Chain of Utterances for Safety-Alignment;** Rishabh Bhardwaj et al
- **Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs;** Yuxia Wang et al
- **SafetyBench: Evaluating the Safety of Large Language Models with Multiple Choice Questions;** Zhexin Zhang et al
- **Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions;** Federico Bianchi et al
- **Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations;** Hakan Inan et al
- **EMULATED DISALIGNMENT: SAFETY ALIGNMENT FOR LARGE LANGUAGE MODELS MAY BACKFIRE!;** Zhanhui Zhou et al
- **Logits of API-Protected LLMs Leak Proprietary Information;** Matthew Finlayson et al
- **Simple probes can catch sleeper agents;** Monte MacDiarmid et al
- **AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs;** Anselm Paulus et al
- **SYCOPHANCY TO SUBTERFUGE: INVESTIGATING REWARD-TAMPERING IN LARGE LANGUAGE MODELS;** Carson Denison et al
- **SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal Behaviors;** Tinghao Xie et al
- **WILDGUARD: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs;** Seungju Han et al
- **Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs;** Rudolf Laine et al
- **Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?;** Richard Ren et al
- **LANGUAGE MODELS LEARN TO MISLEAD HUMANS VIA RLHF;** Jiaxin Wen et al
- **MEASURING AND IMPROVING PERSUASIVENESS OF GENERATIVE MODELS;** Somesh Singh et al
- **LOOKING INWARD: LANGUAGE MODELS CAN LEARN ABOUT THEMSELVES BY INTROSPECTION;** Felix J Binder et al
- **Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming;** Mrinank Sharma et al
- **Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs;** Jan Betley et al
- **Reasoning Models Don’t Always Say What They Think;** Yanda Chen et al


## LLM Evaluation

- **IS CHATGPT A GENERAL-PURPOSE NATURAL LANGUAGE PROCESSING TASK SOLVER?;** Chengwei Qin et al
- **AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models;** Wanjun Zhong et al
- **A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity;** Yejin Bang et al
- **On the Robustness of ChatGPT: An Adversarial and Out-of-distribution Perspective;** Jindong Wang et al
- **A Comprehensive Capability Analysis of GPT-3 and GPT-3.5 Series Models;** Junjie Ye et al
- **KoLA: Carefully Benchmarking World Knowledge of Large Language Models;** Jifan Yu et al
- **SCIBENCH: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models;** Xiaoxuan Wang et al
- **FLASK: FINE-GRAINED LANGUAGE MODEL EVALUATION BASED ON ALIGNMENT SKILL SETS;** Seonghyeon Ye et al
- **Efficient Benchmarking (of Language Models);** Yotam Perlitz et al
- **Can Large Language Models Understand Real-World Complex Instructions?;** Qianyu He et al
- **NLPBENCH: EVALUATING LARGE LANGUAGE MODELS ON SOLVING NLP PROBLEMS;** Linxin Song et al
- **CALIBRATING LLM-BASED EVALUATOR;** Yuxuan Liu et al
- **GPT-FATHOM: BENCHMARKING LARGE LANGUAGE MODELS TO DECIPHER THE EVOLUTIONARY PATH TOWARDS GPT-4 AND BEYOND;** Shen Zheng et al
- **L2CEval: Evaluating Language-to-Code Generation Capabilities of Large Language Models;** Ansong Ni et al
- **Revisiting Out-of-distribution Robustness in NLP: Benchmark, Analysis, and LLMs Evaluations;** Lifan Yuan et al
- **TIGERSCORE: TOWARDS BUILDING EXPLAINABLE METRIC FOR ALL TEXT GENERATION TASKS;** Dongfu Jiang et al
- **DO LARGE LANGUAGE MODELS KNOW ABOUT FACTS?;** Xuming Hu et al
- **PROMETHEUS: INDUCING FINE-GRAINED EVALUATION CAPABILITY IN LANGUAGE MODELS;** Seungone Kim et al
- **CRITIQUE ABILITY OF LARGE LANGUAGE MODELS;** Liangchen Luo et al
- **BotChat: Evaluating LLMs’ Capabilities of Having Multi-Turn Dialogues;** Haodong Duan et al
- **Instruction-Following Evaluation for Large Language Models;** Jeffrey Zhou et al
- **GAIA: A Benchmark for General AI Assistants;** Gregoire Mialon et al
- **ML-BENCH: LARGE LANGUAGE MODELS LEVERAGE OPEN-SOURCE LIBRARIES FOR MACHINE LEARNING TASKS;** Yuliang Liu et al
- **TASKBENCH: BENCHMARKING LARGE LANGUAGE MODELS FOR TASK AUTOMATION;** Yongliang Shen et al
- **GENERATIVE JUDGE FOR EVALUATING ALIGNMENT;** Junlong Li et al
- **InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks;** Xueyu Hu et al
- **AGENTBOARD: AN ANALYTICAL EVALUATION BOARD OF MULTI-TURN LLM AGENTS;** Chang Ma et al
- **WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue;** Xing Han Lu et al
- **MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization;** Zhiyu Yang et al
- **Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference;** Wei-Lin Chiang et al
- **DevBench: A Comprehensive Benchmark for Software Development;** Bowen Li et al
- **REWARDBENCH: Evaluating Reward Models for Language Modeling;** Nathan Lambert et al
- **Long-context LLMs Struggle with Long In-context Learning;** Tianle Li et al
- **LLM Reasoners: New Evaluation, Library, and Analysis of Step-by-Step Reasoning with Large Language Models;** Shibo Hao et al
- **Benchmarking Benchmark Leakage in Large Language Models;** Ruijie Xu et al
- **PROMETHEUS 2: An Open Source Language Model Specialized in Evaluating Other Language Models;** Seungone Kim et al
- **Revealing the structure of language model capabilities;** Ryan Burnell et al
- **MixEval: Deriving Wisdom of the Crowd from LLM Benchmark Mixtures;** Jinjie Ni et al
- **BEHONEST: Benchmarking Honesty of Large Language Models;** Steffi Chern et al
- **SciCode: A Research Coding Benchmark Curated by Scientists;** Minyang Tian et al
- **Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation;** Tu Vu et al
- **MMAU: A Holistic Benchmark of Agent Capabilities Across Diverse Domains;** Guoli Yin et al
- **Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries;** Kiran Vodrahalli et al
- **Easy2Hard-Bench: Standardized Difficulty Labels for Profiling LLM Performance and Generalization;** Mucong Ding et al
- **Law of the Weakest Link: Cross Capabilities of Large Language Models;** Ming Zhong et al
- **HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly;** Howard Yen et al
- **GPQA: A Graduate-Level Google-Proof Q&A Benchmark;** David Rein et al
- **Humanity's Last Exam;** Long Phan et al
- **VERDICT: A Library for Scaling Judge-Time Compute;** Nimit Kalra et al
- **BIG-Bench Extra Hard;** Mehran Kazemi et al
- **VerifiAgent: a Unified Verification Agent in Language Model Reasoning;** Jiuzhou Han et al
- **PaperBench: Evaluating AI’s Ability to Replicate AI Research;** Giulio Starace et al
- **SEALQA: Raising the Bar for Reasoning in Search-Augmented Language Models;** Thinh Pham et al
- **UQ: Assessing Language Models on Unsolved Questions;** Fan Nie et al



## LLM Reasoning

- **STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning;** Eric Zelikman et al
- **Generated Knowledge Prompting for Commonsense Reasoning;** Jiacheng Liu et al
- **SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT REASONING IN LANGUAGE MODELS;** Xuezhi Wang et al
- **LEAST-TO-MOST PROMPTING ENABLES COMPLEX REASONING IN LARGE LANGUAGE MODELS;** Denny Zhou et al
- **REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS;** Shunyu Yao et al
- **The Capacity for Moral Self-Correction in Large Language Models;** Deep Ganguli et al
- **Learning to Reason and Memorize with Self-Notes;** Jack lanchantin et al
- **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models;** Lei Wang et al
- **T-SciQ: Teaching Multimodal Chain-of-Thought Reasoning via Large Language Model Signals for Science Question Answering;** Lei Wang et al
- **Tree of Thoughts: Deliberate Problem Solving with Large Language Models;** Shunyu Yao et al
- **Introspective Tips: Large Language Model for In-Context Decision Making;** Liting Chen et al
- **Testing the General Deductive Reasoning Capacity of Large Language Models Using OOD Examples;** Abulhair Saparov et al
- **Reasoning with Language Model is Planning with World Model;** Shibo Hao et al
- **Interpretable Math Word Problem Solution Generation Via Step-by-step Planning;** Mengxue Zhang et al
- **Towards Understanding Chain-of-Thought Prompting: An Empirical Study of What Matters;** Boshi Wang et al
- **Recursion of Thought: A Divide-and-Conquer Approach to Multi-Context Reasoning with Language Models;** Soochan Lee et al
- **Large Language Models Are Reasoning Teachers;** Namgyu Ho et al
- **Meta-Reasoning: Semantics-Symbol Deconstruction For Large Language Models;** Yiming Wang et al
- **BeamSearchQA: Large Language Models are Strong Zero-Shot QA Solver;** Hao Sun et al
- **AdaPlanner: Adaptive Planning from Feedback with Language Models;** Haotian Sun et al
- **ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models;** Binfeng Xu et al
- **SKILLS-IN-CONTEXT PROMPTING: UNLOCKING COMPOSITIONALITY IN LARGE LANGUAGE MODELS;** Jiaao Chen et al
- **SOLVING CHALLENGING MATH WORD PROBLEMS USING GPT-4 CODE INTERPRETER WITH CODE-BASED SELF-VERIFICATION;** Aojun Zhou et al
- **MAMMOTH: BUILDING MATH GENERALIST MODELS THROUGH HYBRID INSTRUCTION TUNING;** Xiang Yue et al
- **DESIGN OF CHAIN-OF-THOUGHT IN MATH PROBLEM SOLVING;** Zhanming Jie et al
- **NATURAL LANGUAGE EMBEDDED PROGRAMS FOR HYBRID LANGUAGE SYMBOLIC REASONING;** Tianhua Zhang et al
- **MATHCODER: SEAMLESS CODE INTEGRATION IN LLMS FOR ENHANCED MATHEMATICAL REASONING;** Ke Wang et al
- **META-COT: GENERALIZABLE CHAIN-OF-THOUGHT PROMPTING IN MIXED-TASK SCENARIOS WITH LARGE LANGUAGE MODELS;** Anni Zou et al
- **TOOLCHAIN: EFFICIENT ACTION SPACE NAVIGATION IN LARGE LANGUAGE MODELS WITH A SEARCH;** Yuchen Zhuang et al
- **Learning From Mistakes Makes LLM Better Reasoner;** Shengnan An et al
- **Chain of Code: Reasoning with a Language Model-Augmented Code Emulator;** Chengshu Li et al
- **Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives;** Wenqi Zhang et al
- **Divide and Conquer for Large Language Models Reasoning;** Zijie Meng et al
- **The Impact of Reasoning Step Length on Large Language Models;** Mingyu Jin et al
- **REFT: Reasoning with REinforced Fine-Tuning;** Trung Quoc Luong et al
- **Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding;** Mirac Suzgun et al
- **SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures;** Pei Zhou et al
- **Guiding Large Language Models with Divide-and-Conquer Program for Discerning Problem Solving;** Yizhou Zhang et al
- **Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning;** Zhiheng Xi et al
- **V-STaR: Training Verifiers for Self-Taught Reasoners;** Arian Hosseini et al
- **Verified Multi-Step Synthesis using Large Language Models and Monte Carlo Tree Search;** David Brandfonbrener et al
- **BOOSTING OF THOUGHTS: TRIAL-AND-ERROR PROBLEM SOLVING WITH LARGE LANGUAGE MODELS;** Sijia Chen et al
- **Language Agents as Optimizable Graphs;** Mingchen Zhuge et al
- **MathScale: Scaling Instruction Tuning for Mathematical Reasoning;** Zhengyang Tang et al
- **Teaching Large Language Models to Reason with Reinforcement Learning;** Alex Havrilla et al
- **Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking;** Eric Zelikman et al
- **TREE SEARCH FOR LANGUAGE MODEL AGENTS;** Jing Yu Koh et al
- **DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search;** Huajian Xin et al
- **Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning;** Yuxi Xie et al
- **Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs;** Xuan Zhang et al
- **B-STAR: MONITORING AND BALANCING EXPLORATION AND EXPLOITATION IN SELF-TAUGHT REASONERS;** Weihao Zeng et al




**Self-consistency**

- **Enhancing Self-Consistency and Performance of Pre-Trained Language Models through Natural Language Inference;** Eric Mitchell et al
- **Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs;** Angelica Chen et al
- **Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation;** Niels Mündler et al
- **Measuring and Narrowing the Compositionality Gap in Language Models;** Ofir Press et al
- **Self-consistency for open-ended generations;** Siddhartha Jain et al
- **Question Decomposition Improves the Faithfulness of Model-Generated Reasoning;** Ansh Radhakrishnan et al
- **Measuring Faithfulness in Chain-of-Thought Reasoning;** Tamera Lanham et al
- **SELFCHECK: USING LLMS TO ZERO-SHOT CHECK THEIR OWN STEP-BY-STEP REASONING;** Ning Miao et al
- **On Measuring Faithfulness or Self-consistency of Natural Language Explanations;** Letitia Parcalabescu et al
- **Chain-of-Thought Unfaithfulness as Disguised Accuracy;** Oliver Bentham et al

(with images)

- **Sunny and Dark Outside?! Improving Answer Consistency in VQA through Entailed Question Generation;** Arijit Ray et al
- **Maintaining Reasoning Consistency in Compositional Visual Question Answering;** Chenchen Jing et al
- **SQuINTing at VQA Models: Introspecting VQA Models with Sub-Questions;** Ramprasaath R. Selvaraju et al
- **Logical Implications for Visual Question Answering Consistency;** Sergio Tascon-Morales et al
- **Exposing and Addressing Cross-Task Inconsistency in Unified Vision-Language Models;** Adyasha Maharana et al
- **Co-VQA: Answering by Interactive Sub Question Sequence;** Ruonan Wang et al
- **IdealGPT: Iteratively Decomposing Vision and Language Reasoning via Large Language Models;** Haoxuan You et al
- **Understanding ME? Multimodal Evaluation for Fine-grained Visual Commonsense;** Zhecan Wang et al

## LLM Application

- **ArK: Augmented Reality with Knowledge Interactive Emergent Ability;** Qiuyuan Huang et al
- **Can Large Language Models Be an Alternative to Human Evaluation?;** Cheng-Han Chiang et al
- **Few-shot In-context Learning for Knowledge Base Question Answering;** Tianle Li et al
- **AutoML-GPT: Automatic Machine Learning with GPT;** Shujian Zhang et al
- **Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs;** Jinyang Li et al
- **Language models can explain neurons in language models;** Steven Bills et al
- **Large Language Model Programs;** Imanol Schlag et al
- **Evaluating Factual Consistency of Summaries with Large Language Models;** Shiqi Chen et al
- **WikiChat: A Few-Shot LLM-Based Chatbot Grounded with Wikipedia;** Sina J. Semnani et al
- **Language Models Can Improve Event Prediction by Few-Shot Abductive Reasoning;** Xiaoming Shi et al
- **Images in Language Space: Exploring the Suitability of Large Language Models for Vision & Language Tasks;** Sherzod Hakimov et al
- **PEARL: Prompting Large Language Models to Plan and Execute Actions Over Long Documents;** Simeng Sun et al
- **LayoutGPT: Compositional Visual Planning and Generation with Large Language Models;** Weixi Feng et al
- **Judging LLM-as-a-judge with MT-Bench and Chatbot Arena;** Lianmin Zheng et al
- **LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion;** Dongfu Jiang et al
- **Benchmarking Foundation Models with Language-Model-as-an-Examiner;** Yushi Bai et al
- **AudioPaLM: A Large Language Model That Can Speak and Listen;** Paul K. Rubenstein et al
- **Human-in-the-Loop through Chain-of-Thought;** Zefan Cai et al
- **LARGE LANGUAGE MODELS ARE EFFECTIVE TEXT RANKERS WITH PAIRWISE RANKING PROMPTING;** Zhen Qin et al
- **Language to Rewards for Robotic Skill Synthesis;** Wenhao Yu et al
- **Visual Programming for Text-to-Image Generation and Evaluation;** Jaemin Cho et al
- **Mindstorms in Natural Language-Based Societies of Mind;** Mingchen Zhuge et al
- **Responsible Task Automation: Empowering Large Language Models as Responsible Task Automators;** Zhizheng Zhang et al
- **Large Language Models as General Pattern Machines;** Suvir Mirchandani et al
- **A Stitch in Time Saves Nine: Detecting and Mitigating Hallucinations of LLMs by Validating Low-Confidence Generation;** Neeraj Varshney et al
- **VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models;** Wenlong Huang et al
- **External Reasoning: Towards Multi-Large-Language-Models Interchangeable Assistance with Human Feedback;** Akide Liu et al
- **OCTOPACK: INSTRUCTION TUNING CODE LARGE LANGUAGE MODELS;** Niklas Muennighoff et al
- **Tackling Vision Language Tasks Through Learning Inner Monologues;** Diji Yang et al
- **Can Language Models Learn to Listen?;** Evonne Ng et al
- **PROMPT2MODEL: Generating Deployable Models from Natural Language Instructions;** Vijay Viswanathan et al
- **AnomalyGPT: Detecting Industrial Anomalies using Large Vision-Language Models;** Zhaopeng Gu et al
- **LARGE LANGUAGE MODELS AS OPTIMIZERS;** Chengrun Yang et al
- **Large Language Model for Science: A Study on P vs. NP;** Qingxiu Dong et al
- **Physically Grounded Vision-Language Models for Robotic Manipulation;** Jensen Gao et al
- **Compositional Foundation Models for Hierarchical Planning;** Anurag Ajay et al
- **STRUC-BENCH: Are Large Language Models Really Good at Generating Complex Structured Data?;** Xiangru Tang et al
- **XATU: A Fine-grained Instruction-based Benchmark for Explainable Text Updates;** Haopeng Zhang et al
- **TEXT2REWARD: AUTOMATED DENSE REWARD FUNCTION GENERATION FOR REINFORCEMENT LEARNING;** Tianbao Xie et al
- **EUREKA: HUMAN-LEVEL REWARD DESIGN VIA CODING LARGE LANGUAGE MODELS;** Yecheng Jason Ma et al
- **CREATIVE ROBOT TOOL USE WITH LARGE LANGUAGE MODELS;** Mengdi Xu et al
- **Goal Driven Discovery of Distributional Differences via Language Descriptions;** Ruiqi Zhong et al
- **Can large language models provide useful feedback on research papers? A large-scale empirical analysis.;** Weixin Liang et al
- **DRIVEGPT4: INTERPRETABLE END-TO-END AUTONOMOUS DRIVING VIA LARGE LANGUAGE MODEL;** Zhenhua Xu et al
- **QUALEVAL: QUALITATIVE EVALUATION FOR MODEL IMPROVEMENT;** Vishvak Murahari et al
- **LLM AUGMENTED LLMS: EXPANDING CAPABILITIES THROUGH COMPOSITION;** Rachit Bansal et al
- **SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems;** Dong Zhang et al
- **DEMOCRATIZING FINE-GRAINED VISUAL RECOGNITION WITH LARGE LANGUAGE MODELS;** Mingxuan Liu et al
- **Solving olympiad geometry without human demonstrations;** Trieu H. Trinh et al
- **AI-Augmented Predictions: LLM Assistants Improve Human Forecasting Accuracy;** Philipp Schoenegger et al
- **What Evidence Do Language Models Find Convincing?;** Alexander Wan et al
- **Tx-LLM: A Large Language Model for Therapeutics;** Juan Manuel Zambrano Chaves et al
- **Language Models as Science Tutors;** Alexis Chevalier et al
- **Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers;** Chenglei Si et al
- **Model-GLUE: Democratized LLM Scaling for A Large Model Zoo in the Wild;** Xinyu Zhao et al


## LLM with Memory

- **Neural Turing Machines;** Alex Graves et al
- **Narrative Question Answering with Cutting-Edge Open-Domain QA Techniques: A Comprehensive Study;** Xiangyang Mou et al
- **Memory and Knowledge Augmented Language Models for Inferring Salience in Long-Form Stories;** David Wilmot et al
- **MemPrompt: Memory-assisted Prompt Editing with User Feedback;** Aman Madaan et al
- **LANGUAGE MODEL WITH PLUG-IN KNOWLEDGE MEMORY;** Xin Cheng et al
- **Assessing Working Memory Capacity of ChatGPT;** Dongyu Gong et al
- **Prompted LLMs as Chatbot Modules for Long Open-domain Conversation;** Gibbeum Lee et al
- **Beyond Goldfish Memory: Long-Term Open-Domain Conversation;** Jing Xu et al
- **Memory Augmented Large Language Models are Computationally Universal;** Dale Schuurmans et al
- **MemoryBank: Enhancing Large Language Models with Long-Term Memory;** Wanjun Zhong et al
- **Adaptive Chameleon or Stubborn Sloth: Unraveling the Behavior of Large Language Models in Knowledge Clashes;** Jian Xie et al
- **RET-LLM: Towards a General Read-Write Memory for Large Language Models;** Ali Modarressi et al
- **RECURRENTGPT: Interactive Generation of (Arbitrarily) Long Text;** Wangchunshu Zhou et al
- **MEMORIZING TRANSFORMERS;** Yuhuai Wu et al
- **Augmenting Language Models with Long-Term Memory;** Weizhi Wang et al
- **Statler: State-Maintaining Language Models for Embodied Reasoning;** Takuma Yoneda et al
- **LONGNET: Scaling Transformers to 1,000,000,000 Tokens;** Jiayu Ding et al
- **In-context Autoencoder for Context Compression in a Large Language Model;** Tao Ge et al
- **MemoChat: Tuning LLMs to Use Memos for Consistent Long-Range Open-Domain Conversation;** Junru Lu et al
- **KnowledGPT: Enhancing Large Language Models with Retrieval and Storage Access on Knowledge Bases;** Xintao Wang et al
- **LONGBENCH: A BILINGUAL, MULTITASK BENCHMARK FOR LONG CONTEXT UNDERSTANDING;** Yushi Bai et al
- **ChipNeMo: Domain-Adapted LLMs for Chip Design;** Mingjie Liu et al
- **LongAlign: A Recipe for Long Context Alignment of Large Language Models;** Yushi Bai et al
- **RAPTOR: RECURSIVE ABSTRACTIVE PROCESSING FOR TREE-ORGANIZED RETRIEVAL;** Parth Sarthi et al
- **A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts;** Kuang-Huei Lee et al
- **Transformers Can Achieve Length Generalization But Not Robustly;** Yongchao Zhou et al
- **Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context;** Gemini Team, Google
- **HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models;** Bernal Jiménez Gutiérrez et al
- **ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities;** Peng Xu et al

**Advanced**

- **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent;** Hongli Yu et al



**Retrieval-augmented LLM**

- **Training Language Models with Memory Augmentation;** Zexuan Zhong et al
- **Enabling Large Language Models to Generate Text with Citations;** Tianyu Gao et al
- **Multiview Identifiers Enhanced Generative Retrieval;** Yongqi Li et al
- **Meta-training with Demonstration Retrieval for Efficient Few-shot Learning;** Aaron Mueller et al
- **SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND CRITIQUE THROUGH SELF-REFLECTION;** Akari Asai et ak
- **RAP: Retrieval-Augmented Planning with Contextual Memory for Multimodal LLM Agents;** Tomoyuki Kagaya et al
- **Unsupervised Dense Information Retrieval with Contrastive Learning;** Gautier Izacard et al
- **LONGCITE: ENABLING LLMS TO GENERATE FINE-GRAINED CITATIONS IN LONG-CONTEXT QA;** Jiajie Zhang et al
- **ONEGEN: EFFICIENT ONE-PASS UNIFIED GENERATION AND RETRIEVAL FOR LLMS;** Jintian Zhang et al
- **OPENSCHOLAR: SYNTHESIZING SCIENTIFIC LITERATURE WITH RETRIEVAL-AUGMENTED LMS;** Akari Asai et al
- **AUTO-RAG: AUTONOMOUS RETRIEVAL-AUGMENTED GENERATION FOR LARGE LANGUAGE MODELS;** Tian Yu et al



## LLM with Human

- **CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities;** Mina Lee et al
- **RewriteLM: An Instruction-Tuned Large Language Model for Text Rewriting;** Lei Shu et al
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models;** Kaiyu Yang et al
- **Evaluating Human-Language Model Interaction;** Mina Lee et al




## Inference-time Scaling (via RL)

- **An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models;** Yangzhen Wu et al
- **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters;** Charlie Snell et al
- **Large Language Monkeys: Scaling Inference Compute with Repeated Sampling;** Bradley Brown et al
- **Stream of Search (SoS): Learning to Search in Language;** Kanishk Gandhi et al
- **Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation;** Rohin Manvi et al
- **Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning;** Amrith Setlur et al
- **EXACT: TEACHING AI AGENTS TO EXPLORE WITH REFLECTIVE-MCTS AND EXPLORATORY LEARNING;** Xiao Yu et al
- **Technical Report: Enhancing LLM Reasoning with Reward-guided Tree Search;** Jinhao Jiang et al
- **KIMI K1.5: SCALING REINFORCEMENT LEARNING WITH LLMS;** Kimi Team
- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning;** DeepSeek-AI
- **s1: Simple test-time scaling;** Niklas Muennighof et al
- **Demystifying Long Chain-of-Thought Reasoning in LLMs;** Edward Yeo et al
- **Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling;** Runze Liu et al
- **Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?;** Zhiyuan Zeng et al
- **Scaling Test-Time Compute Without Verification or RL is Suboptimal;** Amrith Setlur et al
- **LLMs Can Easily Learn to Reason from Demonstrations Structure, not content, is what matters!;** Dacheng Li et al
- **Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning;** Tian Xie et al
- **Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach;** Jonas Geiping et al
- **Cognitive Behaviors that Enable Self-Improving Reasoners, or, Four Habits of Highly Effective STaRs;** Kanishk Gandhi et al
- **Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models;** Wenxuan Huang et al
- **R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning;** Huatong Song et al
- **Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning;** Yuxiao Qu et al
- **Understanding R1-Zero-Like Training: A Critical Perspective;** Zichen Liu et al
- **Reasoning to Learn from Latent Thoughts;** Yangjun Ruan et al
- **ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning;** Mingyang Chen et al
- **Scaling Evaluation-time Compute with Reasoning Models as Process Evaluators;** Seungone Kim et al
- **SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild;** Weihao Zeng et al
- **Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model;** Jingcheng Hu et al
- **Climbing the Ladder of Reasoning: What LLMs Can—and Still Can’t—Solve after SFT?;** Yiyou Sun et al
- **Learning Adaptive Parallel Reasoning with Language Models;** Jiayi Pan et al
- **TTRL: Test-Time Reinforcement Learning;** Yuxin Zuo et al
- **Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** Yang Yue et al
- **Reinforcement Learning for Reasoning in Large Language Models with One Training Example;** Yiping Wang et al
- **DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition;** Z.Z. Ren et al
- **Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers;** Kusha Sareen et al
- **Absolute Zero: Reinforced Self-play Reasoning with Zero Data;** Andrew Zhao et al
- **RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning;** Kaiwen Zha et al
- **Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective;** Zhoujun Cheng et al
- **QWENLONG-L1: Towards Long-Context Large Reasoning Models with Reinforcement Learning;** Fanqi Wan et al
- **AceReason-Nemotron: Advancing Math and Code Reasoning through Reinforcement Learning;** Yang Chen et al
- **AceReason-Nemotron 1.1: Advancing Math and Code Reasoning through SFT and RL Synergy;** Zihan Liu et al
- **Skywork Open Reasoner 1 Technical Report;** Jujie He et al
- **Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction;** Junhong Shen et al
- **Skywork-R1V3 Technical Report;** Multimodal Team, Skywork AI
- **Reinforcement Pre-Training;** Qingxiu Dong et al
- **Scaling Up RL: Unlocking Diverse Reasoning in LLMs via Prolonged Training;** NVIDIA
- **MEGASCIENCE: PUSHING THE FRONTIERS OF POST-TRAINING DATASETS FOR SCIENCE REASONING;** Run-Ze Fan et al
- **Group Sequence Policy Optimization;** Chujie Zheng et al
- **AGENTIC REINFORCED POLICY OPTIMIZATION;** Guanting Dong et al
- **AlgoTune: Can Language Models Speed Up General-Purpose Numerical Programs?;** Ori Press et al
- **WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning;** Kuan Li et al
- **PUSHING TEST-TIME SCALING LIMITS OF DEEP SEARCH WITH ASYMMETRIC VERIFICATION;** Weihao Zeng et al
- **PretrainZero: Reinforcement Active Pretraining;** Xingrun Xing et al




**Vision-Language or Vision-Only**

- **Visual-RFT: Visual Reinforcement Fine-Tuning;** Ziyu Liu et al
- **LMM-R1: Empowering 3B LMMs with Strong Reasoning Abilities Through Two-Stage Rule-Based RL;** Yingzhe Peng et al
- **MM-EUREKA: EXPLORING VISUAL AHA MOMENT WITH RULE-BASED LARGE-SCALE REINFORCEMENT LEARNING;** Fanqing Meng et al
- **DeepPerception: Advancing R1-like Cognitive Visual Perception in MLLMs for Knowledge-Intensive Visual Grounding;** Xinyu Ma et al
- **Video-R1: Reinforcing Video Reasoning in MLLMs;** Kaituo Feng et al
- **Boosting MLLM Reasoning with Text-Debiased Hint-GRPO;** Qihan Huang et al
- **Skywork R1V2: Multimodal Hybrid Reinforcement Learning for Reasoning;** Chris et al
- **ACTIVE-O3 : Empowering Multimodal Large Language Models with Active Perception via GRPO;** Muzhi Zhu et al
- **DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models;** Chenbin Pan et al
- **Mixed-R1: Unified Reward Perspective For Reasoning Capability in Multimodal Large Language Models;** Shilin Xu et al
- **Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning;** Yana Wei et al
- **RLPR: EXTRAPOLATING RLVR TO GENERAL DO MAINS WITHOUT VERIFIERS;** Tianyu Yu et al
- **GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning;** GLM-V Team
- **Scaling RL to Long Videos;** Yukang Chen et al
- **Zebra-CoT: A Dataset for Interleaved Vision-Language Reasoning;** Ang Li et al
- **VL-Cogito: Progressive Curriculum Reinforcement Learning for Advanced Multimodal Reasoning;** Ruifeng Yuan1 et al
- **Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning;** Hao Shao etal



**Image in Thoughts**

- **GeoGramBench: Benchmarking the Geometric Program Reasoning in Modern LLMs;** Shixian Luo et al
- **DeepEyes: Incentivizing “Thinking with Images” via Reinforcement Learning;** Ziwei Zheng et al
- **Pixel Reasoner: Incentivizing Pixel-Space Reasoning with Curiosity-Driven Reinforcement Learning;** Alex Su et al
- **Visual Planning: Let’s Think Only with Images;** Yi Xu et al
- **Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing;** Junfei Wu et al




**Latent Space**

- **Training Large Language Models to Reason in a Continuous Latent Space;** Shibo Hao et al
- **Soft Thinking: Unlocking the Reasoning Potential of LLMs in Continuous Concept Space;** Zhen Zhang et al
- **Machine Mental Imagery: Empower Multimodal Reasoning with Latent Visual Tokens;** Zeyuan Yang et al
- **LATENT VISUAL REASONING;** Bangzheng Li et al

**Pre-Training**

- **RLP: Reinforcement as a Pretraining Objective;** Ali Hatamizadeh et al



**Understanding & Analysis**

- **The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning;** Shivam Agarwal et al
- **Maximizing Confidence Alone Improves Reasoning;** Mihir Prabhudesai et al
- **Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning;** Shenzhi Wang et al
- **Spurious Rewards: Rethinking Training Signals in RLVR;** Rulin Shao et al
- **The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models;** Ganqu Cui et al
- **REASONING WITH EXPLORATION: AN ENTROPY PERSPECTIVE;** Daixuan Cheng et al
- **REINFORCEMENT FINE-TUNING NATURALLY MITIGATES FORGETTING IN CONTINUAL POST-TRAINING;** Song Lai et al
- **REASONING OR MEMORIZATION? UNRELIABLE RESULTS OF REINFORCEMENT LEARNING DUE TO DATA CONTAMINATION;** Mingqi Wu et al


## Long-context LLM

- **UniMem: Towards a Unified View of Long-Context Large Language Models;** Junjie Fang et al
- **Data Engineering for Scaling Language Models to 128K Context;** Yao Fu et al
- **How to Train Long-Context Language Models (Effectively);** Tianyu Gao et al
- **Qwen2.5-1M Technical Report;** Qwen Team, Alibaba Group





## LLM Foundation

- **QWEN TECHNICAL REPORT;** Jinze Bai et al
- **DeepSeek LLM: Scaling Open-Source Language Models with Longtermism;** DeepSeek-AI
- **Retentive Network: A Successor to Transformer for Large Language Models;** Yutao Sun et al
- **Skill-it! A Data-Driven Skills Framework for Understanding and Training Language Models;** Mayee F. Chen et al
- **Secrets of RLHF in Large Language Models Part I: PPO;** Rui Zheng et al
- **EduChat: A Large-Scale Language Model-based Chatbot System for Intelligent Education;** Yuhao Dan et al
- **WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct;** Haipeng Luo et al
- **SlimPajama-DC: Understanding Data Combinations for LLM Training;** Zhiqiang Shen et al
- **LMSYS-CHAT-1M: A LARGE-SCALE REAL-WORLD LLM CONVERSATION DATASET;** Lianmin Zheng et al
- **Mistral 7B;** Albert Q. Jiang et al
- **Tokenizer Choice For LLM Training: Negligible or Crucial?;** Mehdi Ali et al
- **ZEPHYR: DIRECT DISTILLATION OF LM ALIGNMENT;** Lewis Tunstall et al
- **LEMUR: HARMONIZING NATURAL LANGUAGE AND CODE FOR LANGUAGE AGENTS;** Yiheng Xu et al
- **System 2 Attention (is something you might need too);** Jason Weston et al
- **Camels in a Changing Climate: Enhancing LM Adaptation with TÜLU 2;** Hamish Ivison et al
- **The Falcon Series of Open Language Models;** Ebtesam Almazrouei et al
- **LLM360: Towards Fully Transparent Open-Source LLMs;** Zhengzhong Liu et al
- **OLMO: Accelerating the Science of Language Models;** Dirk Groeneveld et al
- **InternLM-Math: Open Math Large Language Models Toward Verifiable Reasoning;** Huaiyuan Ying et al
- **Gemma: Open Models Based on Gemini Research and Technology;** Gemma Team
- **StarCoder 2 and The Stack v2: The Next Generation;** Anton Lozhkov et al
- **Yi: Open Foundation Models by 01.AI;** 01.AI
- **InternLM2 Technical Report;** Zheng Cai et al
- **Jamba: A Hybrid Transformer-Mamba Language Model;** Opher Lieber et al
- **JetMoE: Reaching Llama2 Performance with 0.1M Dollars;** Yikang Shen et al
- **RHO-1: Not All Tokens Are What You Need;** Zhenghao Lin et al
- **DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model;** DeepSeek-AI
- **MAP-Neo: Highly Capable and Transparent Bilingual Large Language Model Series;** M-A-P
- **Nemotron-4 340B Technical Report;** NVIDIA
- **Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models;** Tianwen Wei et al
- **Gemma 2: Improving Open Language Models at a Practical Size;** Gemma Team
- **ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools;** Team GLM
- **Reuse, Don’t Retrain: A Recipe for Continued Pretraining of Language Models;** Jupinder Parmar et al
- **QWEN2 TECHNICAL REPORT;** An Yang et al
- **Apple Intelligence Foundation Language Models;** Apple
- **Jamba-1.5: Hybrid Transformer-Mamba Models at Scale;** Jamba Team
- **The Llama 3 Herd of Models;** Llama Team, AI @ Meta
- **QWEN2.5-MATH TECHNICAL REPORT: TOWARD MATHEMATICAL EXPERT MODEL VIA SELF IMPROVEMENT;** An Yang et al
- **Qwen2.5-Coder Technical Report;** Binyuan Hui et al
- **TÜLU 3: Pushing Frontiers in Open Language Model Post-Training;** Nathan Lambert et al
- **Phi-4 Technical Report;** Marah Abdin et al
- **Byte Latent Transformer: Patches Scale Better Than Tokens;** Artidoro Pagnoni et al
- **Qwen2.5 Technical Report;** Qwen Team
- **DeepSeek-V3 Technical Report;** DeepSeek-AI
- **2 OLMo 2 Furious;** OLMo Team 
- **Titans: Learning to Memorize at Test Time;** Ali Behrouz et al
- **Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs;** Microsoft et al
- **Command A: An Enterprise-Ready Large Language Model;** Cohere
- **MiMo: Unlocking the Reasoning Potential of Language Model – From Pretraining to Posttraining;** Xiaomi LLM-Core Team
- **Qwen3 Technical Report;** Qwen Team
- **Seed-Coder: Let the Code Model Curate Data for Itself;** ByteDance Seed
- **MiniCPM4: Ultra-Efficient LLMs on End Devices;** MiniCPM Team
- **Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities;** Gemini Team, Google
- **Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance;** Falcon LLM Team
- **KIMI K2: OPEN AGENTIC INTELLIGENCE;** Kimi Team
- **Front-Loading Reasoning: The Synergy between Pretraining and Post-Training Data;** Syeda Nahida Akter et al
- **Olmo 3;** Olmo Team
- **Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models;** Boxin Wang et al
- **DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models;** DeepSeek-AI


## Scaling Law

- **Scaling Laws for Neural Language Models;** Jared Kaplan et al
- **Explaining Neural Scaling Laws;** Yasaman Bahri et al
- **Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws;** Zeyuan Allen-Zhu et al
- **Training Compute-Optimal Large Language Models;** Jordan Hoffmann et al
- **Scaling Laws for Autoregressive Generative Modeling;** Tom Henighan et al
- **Scaling Laws for Generative Mixed-Modal Language Models;** Armen Aghajanyan et al
- **Beyond neural scaling laws: beating power law scaling via data pruning;** Ben Sorscher et al
- **Scaling Vision Transformers;** Xiaohua Zhai et al
- **Scaling Laws for Reward Model Overoptimization;** Leo Gao et al
- **Scaling Laws from the Data Manifold Dimension;** Utkarsh Sharma et al
- **BROKEN NEURAL SCALING LAWS;** Ethan Caballero et al
- **Scaling Laws for Transfer;** Danny Hernandez et al
- **Scaling Data-Constrained Language Models;** Niklas Muennighoff et al
- **Revisiting Neural Scaling Laws in Language and Vision;** Ibrahim Alabdulmohsin et al
- **SCALE EFFICIENTLY: INSIGHTS FROM PRE-TRAINING AND FINE-TUNING TRANSFORMERS;** Yi Tay et al
- **Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer;** Greg Yang et al
- **Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster;** Nolan Dey et al
- **Language models scale reliably with over-training and on downstream tasks;** Samir Yitzhak Gadre et al
- **Unraveling the Mystery of Scaling Laws: Part I;** Hui Su et al
- **nanoLM: an Affordable LLM Pre-training Benchmark via Accurate Loss Prediction across Scales;** Yiqun Yao et al
- **Understanding Emergent Abilities of Language Models from the Loss Perspective;** Zhengxiao Du et al
- **Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance;** Jiasheng Ye et al
- **The Fine Line: Navigating Large Language Model Pretraining with Down streaming Capability Analysis;** Chen Yang et al
- **UNLOCK PREDICTABLE SCALING FROM EMERGENT ABILITIES;** Shengding Hu et al
- **Scaling Laws for Data Filtering—Data Curation cannot be Compute Agnostic;** Sachin Goyal et al
- **A Large-Scale Exploration of µ-Transfer;** Lucas Dax Lingle et al
- **Observational Scaling Laws and the Predictability of Language Model Performance;** Yangjun Ruan et al
- **Selecting Large Language Model to Fine-tune via Rectified Scaling Law;** Haowei Lin et al
- **D-CPT Law: Domain-specific Continual Pre-Training Scaling Law for Large Language Models;** Haoran Que et al
- **Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms;** Rafael Rafailov et al
- **Scaling and evaluating sparse autoencoders;** Leo Gao et al
- **Why Has Predicting Downstream Capabilities of Frontier AI Models with Scale Remained Elusive?;** Rylan Schaeffer et al
- **REGMIX: Data Mixture as Regression for Language Model Pre-training;** Qian Liu et al
- **Scaling Retrieval-Based Language Models with a Trillion-Token Datastore;** Rulin Shao et al
- **Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies;** Chaofan Tao et al
- **AutoScale–Automatic Prediction of Compute-optimal Data Composition for Training LLMs;** Feiyang Kang et al
- **ARE BIGGER ENCODERS ALWAYS BETTER IN VISION LARGE MODELS?;** Bozhou Li et al
- **An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models;** Yangzhen Wu et al
- **Scaling Laws for Data Poisoning in LLMs;** Dillon Bowen et al
- **SCALING LAW WITH LEARNING RATE ANNEALING;** Howe Tissue et al
- **Optimization Hyper-parameter Laws for Large Language Models;** Xingyu Xie et al
- **Scaling Laws and Interpretability of Learning from Repeated Data;** Danny Hernandez et al
- **U-SHAPED AND INVERTED-U SCALING BEHIND EMERGENT ABILITIES OF LARGE LANGUAGE MODELS;** Tung-Yu Wu et al
- **Revisiting the Superficial Alignment Hypothesis;** Mohit Raghavendra et al
- **SCALING LAWS FOR DIFFUSION TRANSFORMERS;** Zhengyang Liang et al
- **ADAPTIVE DATA OPTIMIZATION: DYNAMIC SAMPLE SELECTION WITH SCALING LAWS;** Yiding Jiang et al
- **Scaling Laws for Predicting Downstream Performance in LLMs;** Yangyi Chen et al
- **SCALING LAWS FOR PRE-TRAINING AGENTS AND WORLD MODELS;** Tim Pearce et al
- **Towards Precise Scaling Laws for Video Diffusion Transformers;** Yuanyang Yin et al
- **Predicting Emergent Capabilities by Finetuning;** Charlie Snell et al
- **Densing Law of LLMs;** Chaojun Xiao et al
- **Establishing Task Scaling Laws via Compute-Efficient Model Ladders;** Akshita Bhagia et al
- **SLOTH: SCALING LAWS FOR LLM SKILLS TO PREDICT MULTI-BENCHMARK PERFORMANCE ACROSS FAMILIES;** Felipe Maia Polo et al
- **LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws;** Prasanna Mayilvahanan et al
- **Predictable Scale: Part I — Optimal Hyperparameter Scaling Law in Large Language Model Pretraining;** Houyi Li et al
- **A MULTI-POWER LAW FOR LOSS CURVE PREDICTION ACROSS LEARNING RATE SCHEDULES;** Kairong Luo et al
- **Scaling Laws of Synthetic Data for Language Models;** Zeyu Qin et al
- **Compression Laws for Large Language Models;** Ayan Sengupta et al
- **Scaling Laws for Native Multimodal Models;** Mustafa Shukor et al
- **Parallel Scaling Law for Language Models;** Mouxiang Chen et al
- **Power Lines: Scaling Laws for Weight Decay and Batch Size in LLM Pre-training;** Shane Bergsma et al
- **Farseer: A Refined Scaling Law in Large Language Models;** Houyi Li et al
- **The Art of Scaling Reinforcement Learning Compute for LLMs;** Devvrit Khatri et al


**MoE**

- **UNIFIED SCALING LAWS FOR ROUTED LANGUAGE MODELS;** Aidan Clark et al
- **SCALING LAWS FOR SPARSELY-CONNECTED FOUNDATION MODELS;** Elias Frantar et al
- **Toward Inference-optimal Mixture-of-Expert Large Language Models;** Longfei Yun et al
- **SCALING LAWS FOR FINE-GRAINED MIXTURE OF EXPERTS;** Jakub Krajewski et al
- **Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent;** Tencent Hunyuan Team 







## LLM Data Engineering

- **Textbooks Are All You Need II: phi-1.5 technical report;** Yuanzhi Li et al
- **Orca: Progressive Learning from Complex Explanation Traces of GPT-4;** Subhabrata Mukherjee et al
- **Symbol-LLM: Towards Foundational Symbol-centric Interface For Large Language Models;** Fangzhi Xu et al
- **Orca 2: Teaching Small Language Models How to Reason;** Arindam Mitra et al
- **REST MEETS REACT: SELF-IMPROVEMENT FOR MULTI-STEP REASONING LLM AGENT;** Renat Aksitov et al
- **WHAT MAKES GOOD DATA FOR ALIGNMENT? A COMPREHENSIVE STUDY OF AUTOMATIC DATA SELECTION IN INSTRUCTION TUNING;** Wei Liu et al
- **ChatQA: Building GPT-4 Level Conversational QA Models;** Zihan Liu et al
- **AGENTOHANA: DESIGN UNIFIED DATA AND TRAINING PIPELINE FOR EFFECTIVE AGENT LEARNING;** Jianguo Zhang et al
- **Advancing LLM Reasoning Generalists with Preference Trees;** Lifan Yuan et al
- **WILDCHAT: 1M CHATGPT INTERACTION LOGS IN THE WILD;** Wenting Zhao et al
- **MAmmoTH2: Scaling Instructions from the Web;** Xiang Yue et al
- **Scaling Synthetic Data Creation with 1,000,000,000 Personas;** Xin Chan et al
- **AgentInstruct: Toward Generative Teaching with Agentic Flows;** Arindam Mitra et al
- **Skywork-Math: Data Scaling Laws for Mathematical Reasoning in Large Language Models — The Story Goes On;** Liang Zeng et al
- **WizardLM: Empowering Large Language Models to Follow Complex Instructions;** Can Xu et al
- **Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated Chatbot Arena;** Haipeng Luo et al
- **Automatic Instruction Evolving for Large Language Models;** Weihao Zeng et al
- **AgentInstruct: Toward Generative Teaching with Agentic Flows;** Arindam Mitra et al
- **Does your data spark joy? Performance gains from domain upsampling at the end of training;** Cody Blakeney et al
- **ScalingFilter: Assessing Data Quality through Inverse Utilization of Scaling Laws;** Ruihang Li et al
- **BaichuanSEED: Sharing the Potential of ExtensivE Data Collection and Deduplication by Introducing a Competitive Large Language Model Baseline;** Guosheng Dong et al
- **How Does Code Pretraining Affect Language Model Task Performance?;** Jackson Petty et al
- **DecorateLM: Data Engineering through Corpus Rating, Tagging, and Editing with Language Models;** Ranchi Zhao et al
- **Data Selection via Optimal Control for Language Models;** Yuxian Gu et al
- **HARNESSING WEBPAGE UIS FOR TEXT-RICH VISUAL UNDERSTANDING;** Junpeng Liu et al
- **Aioli: A unified optimization framework for language model data mixing;** Mayee F. Chen et al
- **HOW TO SYNTHESIZE TEXT DATA WITHOUT MODEL COLLAPSE?;** Xuekai Zhu et al
- **Predictive Data Selection: The Data That Predicts Is the Data That Teaches;** Kashun Shum et al
- **DataDecide: How to Predict Best Pretraining Data with Small Experiments;** Ian Magnusson et al
- **Ultra-FineWeb: Efficient Data Filtering and Verification for High-Quality LLM Training Data;** Yudong Wang et al
- **Scaling Physical Reasoning with the PHYSICS Dataset;** Shenghe Zheng et al
- **OpenThoughts: Data Recipes for Reasoning Models;** Etash Guha et al
- **BeyondWeb: Lessons from Scaling Synthetic Data for Trillion-scale Pretraining;** DatologyAI Team 
- **Scaling Agents via Continual Pre-training;** Liangcai Su et al



## VLM Data Engineering

- **Multimodal ArXiv: A Dataset for Improving Scientific Comprehension of Large Vision-Language Models;** Lei Li et al
- **MANTIS: Interleaved Multi-Image Instruction Tuning;** Dongfu Jiang et al
- **ShareGPT4V: Improving Large Multi-Modal Models with Better Captions;** Lin Chen et al
- **ShareGPT4Video: Improving Video Understanding and Generation with Better Captions;** Lin Chen et al
- **OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text;** Qingyun Li et al
- **MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens;** Anas Awadalla et al
- **PIN: A Knowledge-Intensive Dataset for Paired and Interleaved Multimodal Documents;** Junjie Wang et al
- **Web2Code: A Large-scale Webpage-to-Code Dataset and Evaluation Framework for Multimodal LLMs;** Sukmin Yun et al
- **MAVIS: Mathematical Visual Instruction Tuning;** Renrui Zhang et al
- **MiraData: A Large-Scale Video Dataset with Long Durations and Structured Captions;** Xuan Ju et al
- **On Pre-training of Multimodal Language Models Customized for Chart Understanding;** Wan-Cyuan Fan et al
- **MMInstruct: A High-Quality Multi-Modal Instruction Tuning Dataset with Extensive Diversity;** Yangzhou Liu et al
- **VILA^2: VILA Augmented VILA;** Yunhao Fang et al
- **VIDGEN-1M: A LARGE-SCALE DATASET FOR TEXTTO-VIDEO GENERATION;** Zhiyu Tan et al
- **MMEVOL: EMPOWERING MULTIMODAL LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT;** Run Luo et al
- **InfiMM-WebMath-40B: Advancing Multimodal Pre-Training for Enhanced Mathematical Reasoning;** Xiaotian Han et al
- **MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning;** Haotian Zhang et al
- **DATACOMP: In search of the next generation of multimodal datasets;** Samir Yitzhak Gadre et al
- **VIDEO INSTRUCTION TUNING WITH SYNTHETIC DATA;** Yuanhan Zhang et al
- **REVISIT LARGE-SCALE IMAGE-CAPTION DATA IN PRETRAINING MULTIMODAL FOUNDATION MODELS;** Zhengfeng Lai et al
- **CompCap: Improving Multimodal Large Language Models with Composite Captions;** Xiaohui Chen et al
- **MAmmoTH-VL: Eliciting Multimodal Reasoning with Instruction Tuning at Scale;** Jarvis Guo et al
- **BIGDOCS: AN OPEN AND PERMISSIVELY-LICENSED DATASET FOR TRAINING MULTIMODAL MODELS ON DOCUMENT AND CODE TASKS;** Juan Rodriguez et al
- **VisionArena: 230K Real World User-VLM Conversations with Preference Labels;** Christopher Chou et al
- **DIVING INTO SELF-EVOLVING TRAINING FOR MULTIMODAL REASONING;** Wei Liu et al
- **Eagle 2: Building Post-Training Data Strategies from Scratch for Frontier Vision-Language Models;** Zhiqi Li et al
- **Scaling Pre-training to One Hundred Billion Data for Vision Language Models;** Xiao Wang et al
- **MM-RLHF The Next Step Forward in Multimodal LLM Alignment;** Yi-Fan Zhang et al
- **TASKGALAXY: SCALING MULTI-MODAL INSTRUCTION FINE-TUNING WITH TENS OF THOUSANDS VISION TASK TYPES;** Jiankang Chen et al
- **Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation;** Yue Yang et al
- **GneissWeb: Preparing High Quality Data for LLMs at Scale;** Hajar Emami Gohari et al
- **OmniAlign-V: Towards Enhanced Alignment of MLLMs with Human Preference;** Xiangyu Zhao et al
- **SpiritSight Agent: Advanced GUI Agent with One Look;** Zhiyuan Huang et al
- **R1-Onevision: Advancing Generalized Multimodal Reasoning through Cross-Modal Formalization;** Yi Yang et al
- **SHOULD VLMS BE PRE-TRAINED WITH IMAGE DATA?;** Sedrick Keh et al
- **Vision-G1: Towards General Vision Language Reasoning with Multi-Domain Data Curation;** Yuheng Zha et al


## Alignment

- **AI Alignment Research Overview;** Jacob Steinhardt 
- **Language Model Alignment with Elastic Reset;** Michael Noukhovitch et al
- **Alignment for Honesty;** Yuqing Yang et al
- **Align on the Fly: Adapting Chatbot Behavior to Established Norms;** Chunpu Xu et al
- **Combining weak-to-strong generalization with scalable oversight A high-level view on how this new approach fits into our alignment plans;** JAN LEIKE
- **SLEEPER AGENTS: TRAINING DECEPTIVE LLMS THAT PERSIST THROUGH SAFETY TRAINING;** Evan Hubinger et al
- **Towards Efficient and Exact Optimization of Language Model Alignment;** Haozhe Ji et al
- **Aligner: Achieving Efficient Alignment through Weak-to-Strong Correction;** Jiaming Ji et al
- **DeAL: Decoding-time Alignment for Large Language Models;** James Y. Huang et al
- **Step-On-Feet Tuning: Scaling Self-Alignment of LLMs via Bootstrapping;** Haoyu Wang et al
- **Dissecting Human and LLM Preferences;** Junlong Li1 et al
- **Reformatted Alignment;** Run-Ze Fan et al
- **Capability or Alignment? Respect the LLM Base Model’s Capability During Alignment;** Jingfeng Yang
- **Learning or Self-aligning? Rethinking Instruction Fine-tuning;** Mengjie Ren et al
- **Ensuring Safe and High-Quality Outputs: A Guideline Library Approach for Language Models;** Yi Luo et al
- **Weak-to-Strong Extrapolation Expedites Alignment;** Chujie Zheng et al
- **Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization;** Wenkai Yang et al
- **Baichuan Alignment Technical Report;** Mingan Lin et al





## Scalable Oversight & SuperAlignment

- **Supervising strong learners by amplifying weak experts;** Paul Christiano et al
- **Deep Reinforcement Learning from Human Preferences;** Paul F Christiano et al
- **AI safety via debate;** Geoffrey Irving et al
- **Scalable agent alignment via reward modeling: a research direction;** Jan Leike et al
- **Recursively Summarizing Books with Human Feedback;** Jeff Wu et al
- **Self-critiquing models for assisting human evaluators;** William Saunders et al
- **Measuring Progress on Scalable Oversight for Large Language Models;** Samuel R. Bowman et al
- **Debate Helps Supervise Unreliable Experts;** Julian Michael et al
- **WEAK-TO-STRONG GENERALIZATION: ELICITING STRONG CAPABILITIES WITH WEAK SUPERVISION;** Collin Burns et al
- **Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models;** Zixiang Chen et al
- **Discovering Language Model Behaviors with Model-Written Evaluations;** Ethan Perez et al
- **Towards Explainable Harmful Meme Detection through Multimodal Debate between Large Language Models;** Hongzhan Lin et al
- **Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate;** Tian Liang et al
- **Improving Weak-to-Strong Generalization with Scalable Oversight and Ensemble Learning;** Jitao Sang et al
- **PRD: Peer Rank and Discussion Improve Large Language Model based Evaluations;** Ruosen Li et al
- **Vision Superalignment: Weak-to-Strong Generalization for Vision Foundation Models;** Jianyuan Guo et al
- **Improving Factuality and Reasoning in Language Models through Multiagent Debate;** Yilun Du et al
- **CHATEVAL: TOWARDS BETTER LLM-BASED EVALUATORS THROUGH MULTI-AGENT DEBATE;** Chi-Min Chan et al
- **Debating with More Persuasive LLMs Leads to More Truthful Answers;** Akbir Khan et al
- **Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision;** Zhiqing Sun et al
- **The Unreasonable Effectiveness of Easy Training Data for Hard Tasks;** Peter Hase et al
- **LLM Critics Help Catch LLM Bugs;** Nat McAleese et al
- **On scalable oversight with weak LLMs judging strong LLMs;** Zachary Kenton et al
- **PROVER-VERIFIER GAMES IMPROVE LEGIBILITY OF LLM OUTPUTS;** Jan Hendrik Kirchner et al
- **TRAINING LANGUAGE MODELS TO WIN DEBATES WITH SELF-PLAY IMPROVES JUDGE ACCURACY;** Samuel Arnesen et al
- **Great Models Think Alike and this Undermines AI Oversight;** Shashwat Goel et al




## RL Foundation

- **Proximal Policy Optimization Algorithms;** John Schulman et al
- **PREFERENCES IMPLICIT IN THE STATE OF THE WORLD;** Rohin Shah et al
- **Hindsight Experience Replay;** Marcin Andrychowicz et al
- **Learning to Reach Goals via Iterated Supervised Learning;** Dibya Ghosh et al
- **The Wisdom of Hindsight Makes Language Models Better Instruction Followers;** Tianjun Zhang et al
- **REWARD UNCERTAINTY FOR EXPLORATION IN PREFERENCE-BASED REINFORCEMENT LEARNING;** Xinran Liang et al

**With Foundation Model** 

- **Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs;** Arash Ahmadian et al
- **DAPO: An Open-Source LLM Reinforcement Learning System at Scale;** ByteDance Seed 
- **VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks;** ByteDance Seed
- **TAPERED OFF-POLICY REINFORCE Stable and efficient reinforcement learning for LLMs;** Nicolas Le Roux et al
- **AlgoTune: Can Language Models Speed Up General-Purpose Numerical Programs?;** Ori Press et al
- **Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models;** Zhipeng Chen et al
- **InternBootcamp Technical Report: Boosting LLM Reasoning with Verifiable Task Scaling;** Peiji Li et al
- **VERLTOOL: TOWARDS HOLISTIC AGENTIC REINFORCEMENT LEARNING WITH TOOL USE;** Dongfu Jiang et al
- **Reinforcement Learning on Pre-Training Data;** Siheng Li et al
- **Defeating the Training-Inference Mismatch via FP16;** Penghui Qi et al
- **Stabilizing Reinforcement Learning with LLMs: Formulation and Practices;** Chujie Zheng et al
- **DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning;** Zhihong Shao et al


## Beyond Bandit

- **ZERO-SHOT GOAL-DIRECTED DIALOGUE VIA RL ON IMAGINED CONVERSATIONS;** Joey Hong et al
- **LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models;** Marwa Abdulhai et al
- **ELICITING HUMAN PREFERENCES WITH LANGUAGE MODELS;** Belinda Z. Li et al
- **ITERATED DECOMPOSITION: IMPROVING SCIENCE Q&A BY SUPERVISING REASONING PROCESSES;** Justin Reppert et al
- **Let’s Verify Step by Step;** Hunter Lightman et al
- **Solving math word problems with process and outcome-based feedback;** Jonathan Uesato et al
- **EMPOWERING LANGUAGE MODELS WITH ACTIVE INQUIRY FOR DEEPER UNDERSTANDING A PREPRINT;** Jing-Cheng Pang et al
- **Uncertainty of Thoughts: Uncertainty-Aware Planning Enhances Information Seeking in Large Language Models;** Zhiyuan Hu et al
- **Tell Me More! Towards Implicit User Intention Understanding of Language Model-Driven Agents;** Cheng Qian et al
- **MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues;** Ge Bai et al
- **ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL;** Yifei Zhou et al
- **Probing the Multi-turn Planning Capabilities of LLMs via 20 Question Games;** Yizhe Zhang et al
- **STaR-GATE: Teaching Language Models to Ask Clarifying Questions;** Chinmaya Andukuri et al
- **Bayesian Preference Elicitation with Language Models;** Kunal Handa et al
- **Multi-turn Reinforcement Learning from Preference Human Feedback;** Lior Shani et al
- **Improve Mathematical Reasoning in Language Models by Automated Process Supervision;** Liangchen Luo et al
- **MODELING FUTURE CONVERSATION TURNS TO TEACH LLMS TO ASK CLARIFYING QUESTIONS;** Michael J.Q. Zhang et al

## Agent

- **Generative Agents: Interactive Simulacra of Human Behavior;** Joon Sung Park et al
- **SWIFTSAGE: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks;** Bill Yuchen Lin et al
- **Large Language Model Is Semi-Parametric Reinforcement Learning Agent;** Danyang Zhang et al
- **The Role of Summarization in Generative Agents: A Preliminary Perspective;** Xiachong Feng et al
- **CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society;** Guohao Li et al
- **Plan, Eliminate, and Track-Language Models are Good Teachers for Embodied Agents;** Yue Wu et al
- **Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents;** Zihao Wang et al
- **Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory;** Xizhou Zhu et al
- **TOWARDS A UNIFIED AGENT WITH FOUNDATION MODELS;** Norman Di Palo et al
- **MotionLM: Multi-Agent Motion Forecasting as Language Modeling;** Ari Seff et al
- **A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis;** Izzeddin Gur et al
- **Guide Your Agent with Adaptive Multimodal Rewards;** Changyeon Kim et al
- **Generative Agents: Interactive Simulacra of Human Behavior;** Joon Sung Park et al
- **AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents;** Weize Chen et al
- **METAGPT: META PROGRAMMING FOR MULTI-AGENT COLLABORATIVE FRAMEWORK;** Sirui Hong et al
- **YOU ONLY LOOK AT SCREENS: MULTIMODAL CHAIN-OF-ACTION AGENTS;** Zhuosheng Zhang et al
- **SELF: LANGUAGE-DRIVEN SELF-EVOLUTION FOR LARGE LANGUAGE MODEL;** Jianqiao Lu et al
- **Towards End-to-End Embodied Decision Making via Multi-modal Large Language Model: Explorations with GPT4-Vision and Beyond;** Liang Chen et al
- **A Zero-Shot Language Agent for Computer Control with Structured Reflection;** Tao Li et al
- **Character-LLM: A Trainable Agent for Role-Playing;** Yunfan Shao et al
- **CLIN: A CONTINUALLY LEARNING LANGUAGE AGENT FOR RAPID TASK ADAPTATION AND GENERALIZATION;** Bodhisattwa Prasad Majumder et al
- **FIREACT: TOWARD LANGUAGE AGENT FINE-TUNING;** Baian Chen et al
- **TrainerAgent: Customizable and Efficient Model Training through LLM-Powered Multi-Agent System;** Haoyuan Li et al
- **LUMOS: LEARNING AGENTS WITH UNIFIED DATA, MODULAR DESIGN, AND OPEN-SOURCE LLMS;** Da Yin et al
- **TaskWeaver: A Code-First Agent Framework;** Bo Qiao et al
- **Pangu-Agent: A Fine-Tunable Generalist Agent with Structured Reasoning;** Filippos Christianos et al
- **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation;** Qingyun Wu et al
- **TRUE KNOWLEDGE COMES FROM PRACTICE: ALIGNING LLMS WITH EMBODIED ENVIRONMENTS VIA REINFORCEMENT LEARNING;** Weihao Tan et al
- **Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution;** Cheng Qian et al
- **OS-COPILOT: TOWARDS GENERALIST COMPUTER AGENTS WITH SELF-IMPROVEMENT;** Zhiyong Wu et al
- **LONGAGENT: Scaling Language Models to 128k Context through Multi-Agent Collaboration;** Jun Zhao et al
- **When is Tree Search Useful for LLM Planning? It Depends on the Discriminator;** Ziru Chen et al
- **DATA INTERPRETER: AN LLM AGENT FOR DATA SCIENCE;** Sirui Hong et al
- **Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II as a Case Study;** Weihao Tan et al
- **SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents;** Ruiyi Wang et al
- **Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models;** Zehui Chen et al
- **LLM Agent Operating System;** Kai Mei et al
- **Symbolic Learning Enables Self-Evolving Agents;** Wangchunshu Zhou et al
- **Executable Code Actions Elicit Better LLM Agents;** Xingyao Wang et al
- **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents;** Pranav Putta et al
- **MindSearch: Mimicking Human Minds Elicits Deep AI Searcher;** Zehui Chen et al
- **xLAM: A Family of Large Action Models to Empower AI Agent Systems;** Jianguo Zhang et al
- **Agent-as-a-Judge: Evaluate Agents with Agents;** Mingchen Zhuge et al
- **Search-o1: Agentic Search-Enhanced Large Reasoning Models;** Xiaoxi Li et al
- **The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks;** Alejandro Cuadron et al
- **ARMAP: SCALING AUTONOMOUS AGENTS VIA AUTOMATIC REWARD MODELING AND PLANNING;** Zhenfang Chen et al
- **SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks;** Yifei Zhou et al
- **Visual Agentic Reinforcement Fine-Tuning;** Ziyu Liu et al
- **AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning;** Zhong Zhang et al
- **GTA1: GUI Test-time Scaling Agent;** Yan Yang et al
- **OPENCUA: Open Foundations for Computer-Use Agents;** Xinyuan Wang et al
- **AGENTRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework;** Hanchen Zhang et al
- **The FM Agent;** Annan Li et al



**AutoTelic Agent**

- **AUGMENTING AUTOTELIC AGENTS WITH LARGE LANGUAGE MODELS;** Cedric Colas et al
- **Visual Reinforcement Learning with Imagined Goals;** Ashvin Nair et al


**Evaluation**

- **AgentBench: Evaluating LLMs as Agents;** Xiao Liu et al
- **EVALUATING MULTI-AGENT COORDINATION ABILITIES IN LARGE LANGUAGE MODELS;** Saaket Agashe et al
- **OpenAgents: AN OPEN PLATFORM FOR LANGUAGE AGENTS IN THE WILD;** Tianbao Xie et al
- **SMARTPLAY : A BENCHMARK FOR LLMS AS INTELLIGENT AGENTS;** Yue Wu et al
- **ClawBench: Can AI Agents Complete Everyday Online Tasks?;** Yuxuan Zhang et al; arXiv:2604.08523. Live-website browser-agent benchmark; 283 tasks (V1 153 + V2 130) across 163 live platforms; two-stage scoring (HTTP-interception + LLM judge on payload). [project page](https://claw-bench.com) [code](https://github.com/reacher-z/ClawBench)
- **WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?;** Alexandre Drouin et al
- **Autonomous Evaluation and Refinement of Digital Agents;** Jiayi Pan et al


**VL Related Task**

- **LANGNAV: LANGUAGE AS A PERCEPTUAL REPRESENTATION FOR NAVIGATION;** Bowen Pan et al
- **VIDEO LANGUAGE PLANNING;** Yilun Du et al
- **Fuyu-8B: A Multimodal Architecture for AI Agents;** Rohan Bavishi et al
- **GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation;** An Yan et al
- **Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld;** Yijun Yang et al
- **STEVE: See and Think: Embodied Agent in Virtual Environment;** Zhonghan Zhao et al
- **JARVIS-1: Open-world Multi-task Agents with Memory-Augmented Multimodal Language Models;** Zihao Wang et al
- **STEVE-EYE: EQUIPPING LLM-BASED EMBODIED AGENTS WITH VISUAL PERCEPTION IN OPEN WORLDS;** Sipeng Zheng et al
- **OCTOPUS: EMBODIED VISION-LANGUAGE PROGRAMMER FROM ENVIRONMENTAL FEEDBACK;** Jingkang Yang et al
- **CogAgent: A Visual Language Model for GUI Agents;** Wenyi Hong et al
- **GPT-4V(ision) is a Generalist Web Agent, if Grounded;** Boyuan Zheng et al
- **WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models;** Hongliang He et al
- **MOBILE-AGENT: AUTONOMOUS MULTI-MODAL MOBILE DEVICE AGENT WITH VISUAL PERCEPTION;** Junyang Wang et al
- **V-IRL: Grounding Virtual Intelligence in Real Life;** Jihan Yang et al
- **An Interactive Agent Foundation Model;** Zane Durante et al
- **RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis;** Yao Mu et al
- **Scaling Instructable Agents Across Many Simulated Worlds;** SIMA Team
- **Do We Really Need a Complex Agent System? Distill Embodied Agent into a Single Model;** Zhonghan Zhao1 et al
- **Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs;** Keen You et al
- **OSWORLD: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments;** Tianbao Xie et al
- **GUICourse: From General Vision Language Model to Versatile GUI Agent;** Wentong Chen et al
- **VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents;** Xiao Liu et al
- **ShowUI: One Vision-Language-Action Model for GUI Visual Agent;** Kevin Qinghong Lin et al
- **UI-TARS: Pioneering Automated GUI Interaction with Native Agents;** Yujia Qin et al
- **Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents;** Saaket Agashe et al
- **Thyme: Think Beyond Images;** Yi-Fan Zhang et al

## DeepResearch

- **Tongyi DeepResearch Technical Report;** Tongyi DeepResearch Team


## SWE-Agent

### Agent Framework

- **AutoCodeRover: Autonomous Program Improvement;** Yuntong Zhang et al
- **CODER: ISSUE RESOLVING WITH MULTI-AGENT AND TASK GRAPHS;** Dong Chen et al
- **SWE-AGENT: AGENT-COMPUTER INTERFACES ENABLE AUTOMATED SOFTWARE ENGINEERING;** John Yang et al
- **OpenHands: An Open Platform for AI Software Developers as Generalist Agents;** Xingyao Wang et al
- **Coding Agents with Multimodal Browsing are Generalist Problem Solvers;** Aditya Bharat Soni et al
- **Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling;** Trae Research



### Component Improvement

- **REPOGRAPH: ENHANCING AI SOFTWARE ENGINEERING WITH REPOSITORY-LEVEL CODE GRAPH;** Siru Ouyang
- **AGENTLESS: Demystifying LLM-based Software Engineering Agents;** Chunqiu Steven Xia et al

### Data & Env

- **SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents;** Ibragim Badertdinov et al
- **SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks;** Lianghong Guo et al
- **SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling;** Haoran Wang et al
- **R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents;** Naman Jain et al
- **SWE-smith: Scaling Data for Software Engineering Agents;** John Yang et al
- **SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution;** Chengxing Xie et al
- **Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs;** Liang Zeng et al
- **SWE-LEGO: PUSHING THE LIMITS OF SUPERVISED FINE-TUNING FOR SOFTWARE ISSUE RESOLVING;** Chaofan Tao et al
- **Immersion in the GitHub Universe: Scaling Coding Agents to Mastery;** Jiale Zhao et al
- **daVinci-Env: Open SWE Environment Synthesis at Scale;** Dayuan Fu et al




### RL

- **Training Software Engineering Agents and Verifiers with SWE-Gym;** Jiayi Pan et al
- **SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution;** Yuxiang Wei et al
- **https://nebius.com/blog/posts/training-and-search-for-software-engineering-agents**
- **Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards;** Jeff Da et al
- **Introducing Kimi-Dev: A Strong and Open-source Coding LLM for Issue Resolution;** Kimi Team
- **DeepSWE: Training a Fully Open-sourced, State-of-the-Art Coding Agent by Scaling RL;** Michael Luo et al
- **SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution;** Zhenyu He et al
- **KIMI-DEV: AGENTLESS TRAINING AS SKILL PRIOR FOR SWE-AGENTS;** Zonghan Yang et al
- **SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFTWARE ENGINEERING AGENTS;** Kashun Shum et al
- **Toward Training Superintelligent Software Agents through Self-Play SWE-RL;** Yuxiang Wei et al
- **Qwen3-Coder-Next Technical Report;** Ruisheng Cao et al
- **Composer 2 Technical Report;** Cursor Research Team
- **KAT-Coder-V2 Technical Report;** KwaiKAT Team



### Pre-Training/Mid-Training

- **CWM: An Open-Weights LLM for Research on Code Generation with World Models;** Meta FAIR CodeGen Team
- **SWE-Universe: Scale Real-World Verifiable Environments to Millions;** Mouxiang Chen et al




### Benchmark

- **SWE-BENCH: CAN LANGUAGE MODELS RESOLVE REAL-WORLD GITHUB ISSUES?;** Carlos E. Jimenez
- **SWE-BENCH MULTIMODAL: DO AI SYSTEMS GENERALIZE TO VISUAL SOFTWARE DOMAINS?;** John Yang et al
- **SWE-Bench Verified;** Neil Chowdhury et al
- **SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering;** Xuehang Guo et al
- **Programming with Pixels: Computer-Use Meets Software Engineering;** Pranjal Aggarwal et al
- **SWE-bench Goes Live!;** Linghao Zhang et al
- **SWINGARENA: Competitive Programming Arena for Long-context GitHub Issue Solving;** Wendong Xu et al
- **SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner;** Lei Zhang et al
- **SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?;** Xiang Deng etal



## Evolution

- **AlphaEvolve: A coding agent for scientific and algorithmic d