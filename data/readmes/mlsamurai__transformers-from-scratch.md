# Transformers from scratch to production

A free course in ten lessons. We write an English–Russian translator in PyTorch, starting from the tokenizer, and
carry it all the way to a Docker image that anyone can run.

Every lesson is a notebook that runs on a free GPU on Kaggle or Colab, and a post on
[blog.korolevalab.com](https://blog.korolevalab.com/teaching/transformers-from-scratch/) with all of its outputs and figures. A lesson
downloads what the earlier ones produced, the tokenizer and the checkpoints, so any of them can be opened on its own.
You need to read Python; some PyTorch helps from lesson 2 on.

## Lessons

### Part 1. Build the model

| | Lesson | Notebook |
|---|---|---|
| 1 | [Tokenization and BPE from scratch](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-01-tokenization/)<br>What GPT-4o and Llama 3 receive when you type, and why Russian costs more tokens than English. We clean the parallel data, split it without leaks and write byte-pair encoding by hand. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-01-tokenization) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/01_tokenization.ipynb) |
| 2 | [A Transformer from scratch in PyTorch](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-02-transformer/)<br>The encoder–decoder of the 2017 paper, from attention and masks to positions, with every part checked against real models. Along the way you'll see why attention divides by √d_k. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-02-the-transformer) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/02_transformer.ipynb) |
| 3 | [Training a Transformer and decoding with beam search](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-03-training/)<br>The translator learns from half a million sentence pairs on a free GPU. We look at what warm-up and label smoothing do, then compare greedy search, beam search and sampling on its output. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-03-training-decoding) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/03_training.ipynb) |

### Part 2. Measure and improve it

| | Lesson | Notebook |
|---|---|---|
| 4 | [Evaluating machine translation with chrF and COMET](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-04-evaluation/)<br>BLEU and chrF written from scratch and COMET run by hand, then compared with the judgments of professional translators. The paired bootstrap tells a real gain from noise, and a test set seen in training shows what leakage does to the scores. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-04-bleu-chrf-comet) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/04_evaluation.ipynb) |
| 5 | [What Llama changed in the Transformer with RoPE, RMSNorm and SwiGLU](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-05-llama/)<br>Pre-norm, RMSNorm, SwiGLU and RoPE go into the translator one at a time. Each change is measured against what a new random seed does on its own, and fused attention and a KV cache come last. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-05-what-llama-changed) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/05_llama.ipynb) |
| 6 | [Hyperparameter tuning on a free GPU with W&B Sweeps](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-06-sweeps/)<br>One hour of a free GPU spent on hyperparameters. We write a learning-rate range test, random search and successive halving, then hand the search to W&B Sweeps and check the gain against seeds. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-06-w-b-sweeps-tuning) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/06_sweeps.ipynb) |

### Part 3. Ship it

| | Lesson | Notebook |
|---|---|---|
| 7 | [Turning a notebook into a Python package with tests and CI](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-07-package/)<br>The model leaves the notebook and becomes a package anyone can install, with a command line, tests checked by mutation testing and CI on GitHub Actions. Its model card lists what it can't do. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-07-package-tests-ci) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/07_package.ipynb) |
| 8 | [Serving a Transformer with FastAPI and measuring it under load](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-08-serving/)<br>The translator goes behind an HTTP API and is measured the way its users meet it. Open-loop load tests, queueing theory checked against the numbers, dynamic batching, and int8 quantization that doesn't pay off. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-08-serving-under-load) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/08_serving.ipynb) |
| 9 | [A reproducible Docker image for a machine learning model](https://blog.korolevalab.com/blog/2026/transformers-from-scratch-09-docker/)<br>An image that builds to the same bytes twice and runs the same next year. Lock files with hashes, digests, CI that rebuilds and compares, and an ONNX export for a demo in the browser. | [Kaggle](https://www.kaggle.com/code/qmarva/transformers-from-scratch-09-reproducible-docker) · [Colab](https://colab.research.google.com/github/mlsamurai/transformers-from-scratch/blob/main/notebooks/colab/09_docker.ipynb) |

### Part 4. A better translator

| | Lesson | Notebook |
|---|---|---|
| 10 | Making the translator better with distillation and more data<br>Which helps a small translator most, distillation from a bigger model, synthetic data from its domain, a bigger student or an ensemble. NLLB and LLMs serve as reference points. | coming |

## What is here

`notebooks/` holds every lesson twice, for Colab and for Kaggle. `src/tfs/` is the small helper package the notebooks
install: it knows where a notebook runs and draws the course's plots and token chips. `perevod/` is the translator as
the package that lessons 7 to 9 build, test and ship, with its image published by the workflows in `.github/`, and
`space/` is its demo that runs in the browser.

The next course, [Transformer architectures from BERT to diffusion](https://github.com/mlsamurai/transformer-architectures),
has a repository of its own. The copies of its notebooks and figures still found here, under `notebooks/colab/a*` and
`assets/*/a*`, are kept as they were when it moved, because notebooks already published on Kaggle read from them. The
folders under `articles/` point to where the code of the blog's articles lives now.

## Citing

[CITATION.cff](CITATION.cff) has the reference; GitHub shows it under "Cite this repository".

## License

Code under the [MIT License](LICENSE). The IBM Plex fonts bundled with the helpers are under the
[SIL Open Font License](src/tfs/viz/fonts/OFL.txt).
