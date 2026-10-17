# CS224N Stanford NLP Study

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)](https://pytorch.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![core_architectures](https://img.shields.io/badge/core__architectures-planned-yellow)]()
[![resources](https://img.shields.io/badge/resources-planned-yellow)]()

A comprehensive study companion for Stanford's [CS224N: Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/) (Winter 2023).

This repository contains lecture slides, completed assignment solutions (code + written), and infrastructure for a reproducible learning environment.

## Repository Structure

```text
CS224N-Stanford-NLP-Study/
├── 01-lecture-word-vectors-I/              # Word Vectors I (Word2Vec, skip-gram, CBOW)
├── 02-lecture-word-vectors-II/             # Word Vectors II (GloVe, evaluation)
├── 03-lecture-neural-networks-backprop/    # Neural Networks & Backpropagation
├── 04-lecture-dependency-parsing/          # Dependency Parsing
├── 05-lecture-language-models-rnns/        # Language Models & RNNs
├── 06-lecture-fancy-rnns-lstm-gru-seq2seq/ # Fancy RNNs (LSTMs, GRUs, Seq2Seq, Attention)
├── 07-lecture-final-project-overview/      # Final Project Overview
├── 08-lecture-transformers-self-attention/ # Transformers & Self-Attention
├── 09-lecture-pretraining-bert-gpt-elmo/   # Pretraining (BERT, GPT, ELMo)
├── 10-lecture-instruction-tuning-rlhf/     # Instruction Tuning & RLHF
├── 11-lecture-model-adaptation-finetuning-prompting/ # Model Adaptation
├── 12-lecture-question-answering/          # Question Answering
├── 13-lecture-security-privacy-nlp/        # Security & Privacy in NLP
├── 14-lecture-evaluation-bias/             # Evaluation & Bias
├── 15-lecture-code-generation/           # Code Generation
├── 16-lecture-multimodal-deep-learning/    # Multimodal Deep Learning
├── 17-lecture-human-centered-nlp/          # Human-Centered NLP
├── 18-lecture-deployment-efficiency/       # Deployment & Efficiency
├── 19-lecture-open-problems-future/        # Open Problems & Future Directions
├── assignments/              # Completed assignment solutions (code + written)
├── core_architectures/       # Implementations of Word2Vec, RNNs, Transformers, etc.
├── .devcontainer/            # VS Code devcontainer for reproducible environment
├── environment.yml           # Conda environment specification
├── Makefile                  # Lint, format, and environment management
├── pyproject.toml            # Python tooling config (ruff, black, isort)
└── requirements.txt          # Alternative pip-based dependencies
```

## Assignments

| # | Topic | Code | Written Solutions | Weight |
|---|-------|------|-------------------|--------|
| 1 | Introduction to word vectors | [`a1/`](assignments/a1/) | — | 6% |
| 2 | Word2Vec algorithm | [`a2/`](assignments/a2/) | [`a2_written/`](assignments/a2_written/) | 12% |
| 3 | Dependency parsing & neural networks | [`a3/`](assignments/a3/) | [`a3_written/`](assignments/a3_written/) | 12% |
| 4 | NMT with seq2seq, attention, subwords | [`a4/`](assignments/a4/) | [`a4_written/`](assignments/a4_written/) | 12% |
| 5 | Self-supervised learning & Transformers | [`a5/`](assignments/a5/) | [`a5_written/`](assignments/a5_written/) | 12% |

## Quick Start

### Option A: Conda (recommended)

```bash
git clone https://github.com/allaninfo-tech/CS224N-Stanford-NLP-Study.git
cd CS224N-Stanford-NLP-Study
conda env create -f environment.yml
conda activate cs224n
```

### Option B: pip + venv

```bash
git clone https://github.com/allaninfo-tech/CS224N-Stanford-NLP-Study.git
cd CS224N-Stanford-NLP-Study
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Option C: VS Code Devcontainer

Open the repository in VS Code and click "Reopen in Container" when prompted. This provides a fully reproducible environment with all dependencies pre-installed.

## Study Schedule

This course covers 19 lectures. A suggested study plan:

| Week | Lectures | Topics | Papers to Read |
|------|----------|--------|----------------|
| 1 | 1–2 | Word Vectors I & II | word2vec, GloVe papers |
| 2 | 3–4 | Neural Networks, Dependency Parsing | backprop notes |
| 3 | 5–6 | RNNs, LSTMs, Seq2Seq | RNN paper, LSTM blog |
| 4 | 7–8 | Final Project, Transformers | Attention Is All You Need |
| 5 | 9–11 | Pretraining (BERT, GPT), Instruction Tuning, Model Adaptation | BERT, GPT papers |
| 6 | 12–14 | QA, Security, Evaluation & Bias | — |
| 7 | 15–17 | Code Gen, Multimodal, Human-Centered NLP | — |
| 8 | 18–19 | Deployment, Open Problems | — |

Complete the corresponding assignment after each lecture block. Detailed reading lists and video links are available in each assignment folder.

## Contributing

Contributions are welcome — check [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE). Assignment solutions are based on [Florian Kark's CS224n solutions](https://github.com/floriankark/cs224n-win2223) (MIT). Infrastructure files adapted from [suous/cs224n](https://github.com/suous/cs224n).
