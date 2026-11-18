# Curated AI / ML / DL Interview Resources

[English](README.md) | [简体中文](README.zh-CN.md)

A curated, categorized, and link-verified collection of interview question banks for artificial intelligence, machine learning, deep learning, LLMs, and ML systems. Instead of collecting shallow trivia, this guide is organized around four skills that matter in real interviews:

> ML/DL theory + Transformers/LLMs + PyTorch implementation + ML system design

All links were verified on **July 20, 2026**. This repository provides descriptions and study guidance only; the questions, answers, and code remain the property of their respective projects.

## Quick Selection Guide

| Your goal | Start here | Supplement with |
| --- | --- | --- |
| Build a complete interview knowledge map | [Machine Learning Interviews](#1-machine-learning-interviews) | [Machine-Learning-Interviews](#4-machine-learning-interviews-preparation-guide) |
| Strengthen mathematical theory and derivations | [Deep Learning Interviews](#2-deep-learning-interviews) | [MLQuestions](#8-mlquestions) |
| Practice implementing models in PyTorch | [TorchLeet](#3-torchleet) | [TorchCode](#6-torchcode), [HappyTorch](#7-happytorch) |
| Prepare for Transformer and LLM interviews | [LLMInterviewQuestions](#5-llminterviewquestions) | [Devinterview LLM](#11-devinterview-llm) |
| Understand the complete ML interview process | [Machine-Learning-Interviews](#4-machine-learning-interviews-preparation-guide) | [Machine Learning Interviews](#1-machine-learning-interviews) |
| Prepare for AI system design | [AI System Design Question Bank](#12-ai-system-design-question-bank) | The system design section in Machine Learning Interviews |
| Run a final verbal knowledge check | [Devinterview series](#devinterview-series) | [MLQuestions](#8-mlquestions) |

## Recommended Core Resources

### 1. Machine Learning Interviews

- Link: [chiphuyen/ml-interviews-book](https://github.com/chiphuyen/ml-interviews-book)
- Role: master index, knowledge map, and gap-finding framework
- Coverage: roles and interview processes, mathematics and probability, ML workflows, metrics, models, training, and open-ended ML system design
- Rating: **9/10**

Its coverage is broad, and many questions target common misconceptions. Some questions do not include detailed reference answers, so it works best as an active-recall map: answer each question first, then return to textbooks, papers, or official documentation to fill the gaps.

### 2. Deep Learning Interviews

- Link: [BoltzmannEntropy/interviews.ai](https://github.com/BoltzmannEntropy/interviews.ai)
- Role: mathematically rigorous theory bank with worked answers
- Coverage: information theory, calculus, automatic differentiation, Bayesian methods, logistic regression, ensemble learning, feature extraction, neural networks, deep learning, and selected Python, PyTorch, and C++ implementations
- Rating: **9.5/10**

This is closer to a technical interview book than a collection of definition questions. Readers with a strong mathematical background can prioritize Information Theory, Automatic Differentiation, Logistic Regression, Deep Learning, Optimization, and probabilistic modeling.

### 3. TorchLeet

- Link: [Exorust/TorchLeet](https://github.com/Exorust/TorchLeet)
- Role: LeetCode-style PyTorch implementation practice and the recommended coding track
- Coverage: tensor operations, linear regression, softmax, normalization, attention, embeddings, Transformers, KV cache, LoRA, alignment, training, and debugging
- Rating: **10/10**

The project offers tracks for core PyTorch, building an LLM from scratch, and systems, kernels, and modern model architectures. Exercises include incomplete code and reference solutions. For maximum value, implement and test each problem independently and explain its complexity before reading the solution. Company tags are mostly aggregated from interview experiences rather than official company question banks, so treat them as informal signals only.

### 4. Machine-Learning-Interviews (Preparation Guide)

- Link: [alirezadir/Machine-Learning-Interviews](https://github.com/alirezadir/Machine-Learning-Interviews)
- Role: preparation guide organized around real ML interview rounds
- Coverage: general coding, ML coding, ML fundamentals, ML system design, agentic AI systems, behavioral interviews, LLMs, multimodal AI, and GenAI system design
- Rating: **9/10**

Its main value is showing how ML Engineer and Applied Scientist interviews may assess candidates across multiple rounds rather than presenting isolated questions. It is particularly useful for Applied Scientist, AI Research Engineer, Quant/AI, and LLM evaluation roles.

### 5. LLMInterviewQuestions

- Link: [llmgenai/LLMInterviewQuestions](https://github.com/llmgenai/LLMInterviewQuestions)
- Role: a modern LLM interview checklist
- Coverage: Transformers, prompt engineering, embeddings, vector databases, RAG, SFT, RLHF/DPO, evaluation, hallucinations, deployment, agents, prompt security, and case studies
- Rating: **8/10**

The question coverage is broad, but many complete answers live on an external website. Use it as a checklist rather than a standalone textbook: write your own answer to every question and verify it against original papers or official documentation.

## Supplementary Question Banks

### 6. TorchCode

- Link: [duoan/TorchCode](https://github.com/duoan/TorchCode)
- Role: LeetCode-style PyTorch exercises with automatic grading
- Coverage: implementing softmax, neural-network layers, attention, Transformers, GPT-2, and related components from scratch

It overlaps with TorchLeet, but its instant grading makes it a useful secondary practice source: **use TorchLeet as the main track and TorchCode for reinforcement**.

### 7. HappyTorch

- Link: [Rivflyyy/HappyTorch](https://github.com/Rivflyyy/HappyTorch)
- Role: PyTorch coding platform ranging from fundamentals to modern generative models
- Coverage: activation functions, Transformer components, LLMs, diffusion, PEFT, and selected RLHF topics

Use it to find extra implementation exercises when a topic proves difficult, or as a focused environment for practicing tensors and deep-learning components.

### 8. MLQuestions

- Link: [andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions)
- Role: rapid review of classic ML and computer vision questions
- Coverage: bias–variance trade-off, gradient descent, overfitting, regularization, evaluation, classic ML algorithms, and computer vision

The questions and answers are concise. It is useful for review and verbal checks shortly before an interview, but not as a complete learning resource.

### Devinterview Series

These three repositories provide topic-specific questions and answers. Their breadth makes them useful for quick verbal checks, but many answers are conceptual summaries with inconsistent depth and rigor. They should not be the primary learning path.

#### 9. Devinterview Deep Learning

- Link: [Devinterview-io/deep-learning-interview-questions](https://github.com/Devinterview-io/deep-learning-interview-questions)
- Role: deep-learning concepts and short-answer questions
- Best for: quickly checking knowledge of neural networks, training, and common architectures

#### 10. Devinterview PyTorch

- Link: [Devinterview-io/pytorch-interview-questions](https://github.com/Devinterview-io/pytorch-interview-questions)
- Role: PyTorch concepts, APIs, and practical questions
- Best for: reviewing framework knowledge that complements implementation practice

#### 11. Devinterview LLM

- Link: [Devinterview-io/llms-interview-questions](https://github.com/Devinterview-io/llms-interview-questions)
- Role: LLM concepts and short-answer questions
- Best for: quick topic-by-topic review before an interview

### 12. AI System Design Question Bank

- Link: [ombharatiya/ai-system-design-guide: Question Bank](https://github.com/ombharatiya/ai-system-design-guide/blob/main/00-interview-prep/01-question-bank.md)
- Role: engineering- and architecture-focused AI system design practice
- Coverage: answer frameworks, follow-up questions, interviewer signals, recommendation, ranking, fraud detection, RAG, LLM serving, evaluation, monitoring, retraining, and latency/cost trade-offs

It is best approached after building a solid foundation in model internals and PyTorch. A complete answer should cover requirements, metrics, data, modeling, online architecture, evaluation, monitoring, feedback loops, and cost constraints.

## A Practical Study Path

1. Use **Machine Learning Interviews** to build a knowledge map and record every gap.
2. Use **Deep Learning Interviews** to strengthen mathematics, theory, optimization, and probabilistic modeling.
3. Complete a **TorchLeet** implementation every day; use TorchCode and HappyTorch for targeted reinforcement.
4. Turn **LLMInterviewQuestions** into a Transformer/LLM checklist and write answers backed by papers or official documentation.
5. Use **Machine-Learning-Interviews** to design mock interview rounds for your target role.
6. Move to the **AI System Design Question Bank** and practice explaining end-to-end architectures.
7. Use **MLQuestions** and the **Devinterview series** for final verbal review.

## How to Use This Index

- Do not merely read answers: give yourself a time limit, answer verbally or in writing, and only then check the reference.
- For theory questions, cover the definition, intuition, formulas and assumptions, failure modes, and engineering implications.
- For coding questions, include an independent implementation, unit tests, shape checks, numerical stability, and complexity analysis.
- For system design questions, cover requirements, data, metrics, modeling, serving, evaluation, monitoring, iteration, and cost.
- Treat company labels and “real interview question” claims as unofficial unless the project provides a verifiable primary source.
- Repository size, question counts, and content change over time; consult each project's current README for the latest details.

## Data and Contributions

- [resources.yml](resources.yml) contains machine-readable data for all 12 resources.
- Found a broken link, outdated description, or another high-quality resource? Issues and pull requests are welcome.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a new resource.

## Acknowledgments and License

Thank you to the authors and contributors of every linked project. The original guide text in this repository is available under the [MIT License](LICENSE); each linked project remains subject to its own license. This repository does not copy or relicense external questions, answers, or code.
