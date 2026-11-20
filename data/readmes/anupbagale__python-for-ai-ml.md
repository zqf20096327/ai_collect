# Python for AI & ML Engineering

A hands-on course that takes you from your first line of Python to building, evaluating and deploying machine learning systems.

Most Python tutorials teach the language in general. Most ML tutorials assume you already know Python well and jump straight into libraries. This repo sits in between. Every topic is taught with machine learning in mind: classes are explained by building a dataset loader, generators by streaming data in batches, and floats by looking at why your loss sometimes turns into `nan`.

The course has three parts, all complete. **Part 1** teaches Python, data and machine learning foundations together and ends with a capstone that goes from raw field data to a tested prediction API. **Part 2** goes deeper into machine learning itself. **Part 3** covers deep learning and modern AI, including how large language models work and how to build with them, and ends with responsible AI and a final capstone that takes a model all the way into a monitored production service.

New to AI? Start with [Start Here](00-start-here), a short introduction to what AI and machine learning actually are, with programs you can run in your browser.

Each module has four parts:

- **Lesson**: concepts explained step by step, with runnable code
- **Exercises**: problems with built-in checks, so you know right away if your answer is correct
- **Solutions**: worked answers with notes on why they're written that way
- **Mini project**: a small build that uses everything from the module (in Module 11, the capstone project)

Everything runs in Google Colab. Click the badge next to any notebook and it opens in your browser, with nothing to install.

## Free for everyone

This course is free, and it will stay free. The goal is simple: anyone, anywhere, with an internet connection and the willingness to work through it, should be able to become a capable machine learning engineer.

- **No cost, no sign-up for the course.** Everything is in this repository under the MIT licence. You can study it, copy it, translate it, and teach classes with it.
- **Several ways to run it**, so nobody is locked out:
  - **Google Colab**: click a badge; needs a free Google account.
  - **Binder**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anupbagale/python-for-ai-ml/HEAD) opens the whole course in a browser with **no account at all**. It can take a few minutes to start.
  - **Your own computer**: any ordinary laptop works (see [Running locally](#running-locally)), and once installed it works offline.
  - **Just reading**: every notebook is saved with its outputs, so you can read it on GitHub with the results and charts already shown.
- **No expensive hardware.** Part 1 runs on a basic laptop or free Colab, with small datasets and no graphics card. Parts 2 and 3 are designed the same way: free Colab is enough, with open datasets and open models, and **never a paid API key**.
- **No background assumed.** No maths beyond school arithmetic is needed to start; the maths is taught in code when it's needed. Plain English throughout, with a [glossary](00-start-here/glossary.md) for every term.
- **Charts are readable by everyone.** Colours are chosen to stay distinguishable with colour blindness, groups also differ by marker shape, and every chart is explained in the text.

## Who this is for

- Complete beginners who want to learn AI and machine learning properly, from the ground up
- People who know a bit of Python and want to move into AI/ML engineering
- ML learners who can follow tutorials but get stuck when writing their own code
- Anyone who wants to understand what NumPy, pandas and PyTorch are doing underneath

No prior ML knowledge is needed. The math is introduced when it's needed and kept practical.

## Roadmap

### Part 1: Python, data and ML foundations

| #  | Module | Topics | Status |
|----|--------|--------|--------|
| 00 | [Start Here](00-start-here) | What AI, machine learning, deep learning and LLMs are, how learning works, the kinds of ML, overfitting, and how a real project runs | Available |
| 01 | [Python Foundations](01-python-foundations) | Types, floats, strings, control flow, functions, comprehensions, errors | Available |
| 02 | [Data Structures](02-data-structures) | Lists, tuples, dicts, sets, `collections`, `heapq`, and how fast each one really is | Available |
| 03 | [OOP for ML](03-oop-for-ml) | Classes, dunder methods, properties, inheritance, dataclasses, PyTorch-style `Dataset`, `DataLoader` and autograd | Available |
| 04 | [Pythonic Tools](04-pythonic-tools) | Iterators, generators, `itertools`, decorators, context managers, type hints | Available |
| 05 | [Files and Data](05-files-and-data) | pathlib, encodings, CSV, JSON, cleaning messy data, saving models, with real penguin data | Available |
| 06 | [NumPy](06-numpy) | Arrays, views, broadcasting, vectorization, linear algebra, a neural network from scratch | Available |
| 07 | [pandas](07-pandas) | Reading, cleaning, groupby, merging, encoding, time-based features and leakage | Available |
| 08 | [Visualization](08-visualization) | Matplotlib, Seaborn, choosing charts, honest colour and axes, model diagnostic plots | Available |
| 09 | [Math in Code](09-math-in-code) | Floating point, vectors, gradients, the chain rule, gradient descent, probability and statistics, by hand and checked | Available |
| 10 | [Engineering Practices](10-engineering-practices) | Project layout, environments, pytest, logging, configs, CLIs, reproducibility, profiling | Available |
| 11 | [Capstone](11-capstone) | scikit-learn pipelines, honest evaluation, and a tested FastAPI service, built from raw field data | Available |

### Part 2: Machine learning in depth

| #  | Module | Topics | Status |
|----|--------|--------|--------|
| 12 | [Supervised Learning in Depth](12-supervised-learning) | Linear and logistic models, L1 and L2 regularisation, bias and variance, feature engineering, regression metrics, learning curves | Available |
| 13 | [Evaluating Classifiers](13-evaluating-classifiers) | Precision, recall, F1, ROC and precision-recall curves, thresholds, calibration, class imbalance, cost-sensitive decisions | Available |
| 14 | [Trees and Ensembles](14-trees-and-ensembles) | Decision trees and gradient boosting from scratch, bagging and random forests, histogram boosting and the XGBoost and LightGBM family, permutation importance and partial dependence | Available |
| 15 | [Unsupervised Learning](15-unsupervised-learning) | k-means and PCA from scratch, Gaussian mixtures, hierarchical clustering, DBSCAN, t-SNE (and UMAP), anomaly detection, checking whether clusters are real | Available |
| 16 | [Time Series and Recommendations](16-time-series-and-recommendations) | Forecasting baselines, exponential smoothing, time-based validation, lag features, prediction intervals, collaborative filtering, matrix factorisation, evaluating recommenders | Available |

### Part 3: Deep learning and modern AI

| #  | Module | Topics | Status |
|----|--------|--------|--------|
| 17 | [Deep Learning with PyTorch](17-deep-learning-pytorch) | Tensors, autograd, `nn.Module`, optimisers, initialisation, normalisation, dropout, learning-rate schedules, GPUs, debugging training | Available |
| 18 | [Computer Vision](18-computer-vision) | Convolutions from scratch, CNNs, data augmentation, transfer learning with pretrained models | Available |
| 19 | [Sequences and Transformers](19-sequences-and-transformers) | Tokenisation, embeddings, attention from scratch, training a small GPT | Available |
| 20 | [LLMs in Practice](20-llms-in-practice) | Pretrained models, prompting, embeddings and vector search, retrieval-augmented generation, fine-tuning with LoRA, evaluating LLM applications | Available |
| 21 | [Responsible and Production AI](21-responsible-and-production-ai) | Fairness, interpretability, privacy, experiment tracking, model cards, serving and containers, monitoring, and the final capstone | Available |

## Notebooks

| Module | Lesson | Exercises | Solutions | Mini project |
|--------|--------|-----------|-----------|--------------|
| [00 Start Here](00-start-here) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/00-start-here/01_lesson.ipynb) | Self-check questions in the lesson | Answers in the lesson | [Glossary](00-start-here/glossary.md) |
| [01 Python Foundations](01-python-foundations) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/01-python-foundations/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/01-python-foundations/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/01-python-foundations/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/01-python-foundations/04_mini_project.ipynb) k-NN classifier |
| [02 Data Structures](02-data-structures) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/02-data-structures/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/02-data-structures/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/02-data-structures/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/02-data-structures/04_mini_project.ipynb) Naive Bayes spam filter |
| [03 OOP for ML](03-oop-for-ml) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/03-oop-for-ml/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/03-oop-for-ml/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/03-oop-for-ml/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/03-oop-for-ml/04_mini_project.ipynb) Autograd engine + neural net |
| [04 Pythonic Tools](04-pythonic-tools) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/04-pythonic-tools/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/04-pythonic-tools/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/04-pythonic-tools/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/04-pythonic-tools/04_mini_project.ipynb) Hyperparameter search |
| [05 Files and Data](05-files-and-data) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/05-files-and-data/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/05-files-and-data/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/05-files-and-data/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/05-files-and-data/04_mini_project.ipynb) Penguin classifier, saved as JSON |
| [06 NumPy](06-numpy) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/06-numpy/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/06-numpy/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/06-numpy/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/06-numpy/04_mini_project.ipynb) Digit-reading neural network |
| [07 pandas](07-pandas) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/07-pandas/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/07-pandas/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/07-pandas/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/07-pandas/04_mini_project.ipynb) Customer churn from raw tables |
| [08 Visualization](08-visualization) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/08-visualization/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/08-visualization/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/08-visualization/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/08-visualization/04_mini_project.ipynb) Visual model report |
| [09 Math in Code](09-math-in-code) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/09-math-in-code/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/09-math-in-code/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/09-math-in-code/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/09-math-in-code/04_mini_project.ipynb) Logistic regression by hand |
| [10 Engineering Practices](10-engineering-practices) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/10-engineering-practices/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/10-engineering-practices/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/10-engineering-practices/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/10-engineering-practices/04_mini_project.ipynb) From notebook to project |
| [11 Capstone](11-capstone) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/11-capstone/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/11-capstone/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/11-capstone/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/11-capstone/04_capstone.ipynb) Penguin sexing service, raw data to API |
| [12 Supervised Learning](12-supervised-learning) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/12-supervised-learning/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/12-supervised-learning/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/12-supervised-learning/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/12-supervised-learning/04_mini_project.ipynb) California house values |
| [13 Evaluating Classifiers](13-evaluating-classifiers) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/13-evaluating-classifiers/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/13-evaluating-classifiers/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/13-evaluating-classifiers/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/13-evaluating-classifiers/04_mini_project.ipynb) Who should the bank call? |
| [14 Trees and Ensembles](14-trees-and-ensembles) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/14-trees-and-ensembles/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/14-trees-and-ensembles/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/14-trees-and-ensembles/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/14-trees-and-ensembles/04_mini_project.ipynb) The rematch: trees vs linear |
| [15 Unsupervised Learning](15-unsupervised-learning) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/15-unsupervised-learning/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/15-unsupervised-learning/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/15-unsupervised-learning/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/15-unsupervised-learning/04_mini_project.ipynb) Customer groups for a wholesaler |
| [16 Time Series and Recommendations](16-time-series-and-recommendations) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/16-time-series-and-recommendations/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/16-time-series-and-recommendations/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/16-time-series-and-recommendations/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/16-time-series-and-recommendations/04_mini_project.ipynb) Bike demand and shop recommendations |
| [17 Deep Learning with PyTorch](17-deep-learning-pytorch) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/17-deep-learning-pytorch/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/17-deep-learning-pytorch/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/17-deep-learning-pytorch/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/17-deep-learning-pytorch/04_mini_project.ipynb) Clothing classifier |
| [18 Computer Vision](18-computer-vision) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/18-computer-vision/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/18-computer-vision/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/18-computer-vision/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/18-computer-vision/04_mini_project.ipynb) Recycling sorter |
| [19 Sequences and Transformers](19-sequences-and-transformers) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/19-sequences-and-transformers/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/19-sequences-and-transformers/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/19-sequences-and-transformers/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/19-sequences-and-transformers/04_mini_project.ipynb) A transformer that adds |
| [20 LLMs in Practice](20-llms-in-practice) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/20-llms-in-practice/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/20-llms-in-practice/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/20-llms-in-practice/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/20-llms-in-practice/04_mini_project.ipynb) Ask the Course |
| [21 Responsible and Production AI](21-responsible-and-production-ai) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/21-responsible-and-production-ai/01_lesson.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/21-responsible-and-production-ai/02_exercises.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/21-responsible-and-production-ai/03_solutions.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/python-for-ai-ml/blob/main/21-responsible-and-production-ai/04_mini_project.ipynb) Final capstone: From Notebook to Service |

## How long it takes

About 1 hour for Start Here, then roughly 6 to 10 hours per module in Part 1 and 8 to 12 hours per module in Parts 2 and 3, including the exercises and the project. In total, that's about 150 to 230 hours.

At 5 to 8 hours a week:

| Part | Modules | Time |
|------|---------|------|
| Part 1: Python, data and ML foundations | 1 to 11 | 2 to 5 months |
| Part 2: Machine learning in depth | 12 to 16 | 1 to 3 months |
| Part 3: Deep learning and modern AI | 17 to 21 | 1 to 3 months |
| **Whole course** | | **about 4 months to a year** |

There's no deadline: go at the pace that works for you, and repeat anything that didn't stick. Going slowly and doing every exercise beats rushing through.

With about 8 hours a week, a module a week works well. With less time, take two weeks per module and keep the same steps:

1. **Lesson:** read it and run every cell, changing things as you go.
2. **Exercises:** do them without looking at the solutions.
3. **Solutions:** compare with your answers and read the notes.
4. **Mini project:** build it, and try at least one of its extension ideas.

## How to use this repo

1. If AI and machine learning are new to you, read [Start Here](00-start-here) first.
2. Go through the modules in order. Later modules build on earlier ones.
3. Read the lesson and run every cell. Change the code and see what breaks.
4. Do the exercises without looking at the solutions. Each exercise has a check cell that tells you which input your code got wrong.
5. Compare your answers with the solutions afterwards. There's usually more than one good way to solve a problem.
6. Build the mini project, then try the extension ideas at the end of it.

The `cheatsheet.md` in each module is a one-page summary for revision.

## Running locally

If you prefer working on your own machine:

```bash
git clone https://github.com/anupbagale/python-for-ai-ml.git
cd python-for-ai-ml
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Python 3.10 or newer is recommended.

## Getting help

Stuck on something, or found a mistake? [Open an issue](https://github.com/anupbagale/python-for-ai-ml/issues) on GitHub. Say which module and notebook, which cell, what you expected and what happened (copy the full error message). Questions are welcome: if something confused you, it probably confused someone else too, and the answer can improve the course for everyone.

## Contributing

Corrections, clearer explanations, extra exercises and **translations** are all welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Repo structure

```
python-for-ai-ml/
├── 00-start-here/
│   ├── README.md
│   ├── 01_lesson.ipynb
│   └── glossary.md
├── 01-python-foundations/
│   ├── README.md
│   ├── 01_lesson.ipynb
│   ├── 02_exercises.ipynb
│   ├── 03_solutions.ipynb
│   ├── 04_mini_project.ipynb
│   └── cheatsheet.md
├── 02-data-structures/
│   └── (same layout)
├── 03-oop-for-ml/
│   └── (same layout)
├── 04-pythonic-tools/
│   └── (same layout)
├── 05-files-and-data/
│   ├── (same layout)
│   └── data/penguins.csv
├── 06-numpy/
│   └── (same layout)
├── 07-pandas/
│   └── (same layout)
├── 08-visualization/
│   └── (same layout)
├── 09-math-in-code/
│   └── (same layout)
├── 10-engineering-practices/
│   └── (same layout)
├── 11-capstone/
│   ├── (same layout, with 04_capstone.ipynb)
│   └── data/penguins_raw.csv
├── 12-supervised-learning/
│   ├── (same layout)
│   └── data/california_housing.csv
├── 13-evaluating-classifiers/
│   ├── (same layout)
│   └── data/bank_marketing.csv.gz
├── 14-trees-and-ensembles/
│   └── (same layout)
├── 15-unsupervised-learning/
│   ├── (same layout)
│   └── data/wholesale_customers.csv
├── 16-time-series-and-recommendations/
│   ├── (same layout)
│   └── data/ (bike rentals, online shop transactions)
├── 17-deep-learning-pytorch/
│   ├── (same layout)
│   └── data/README.md (Fashion-MNIST is downloaded when you run the mini project)
├── 18-computer-vision/
│   ├── (same layout)
│   └── data/README.md (TrashNet photos are downloaded when you run the mini project)
├── 19-sequences-and-transformers/
│   ├── (same layout)
│   └── data/ (Tiny Shakespeare)
├── 20-llms-in-practice/
│   ├── (same layout)
│   └── data/ (a made-up library handbook)
├── 21-responsible-and-production-ai/
│   ├── (same layout, with the final capstone as 04_mini_project.ipynb)
│   └── data/adult.csv.gz
├── CONTRIBUTING.md
├── requirements.txt
└── LICENSE
```

## Data

All datasets are free and openly available, and each data folder has a README with its source and licence.

- **Palmer penguins** (Modules 5 to 11): collected by Dr. Kristen Gorman and the Palmer Station Long Term Ecological Research Program, packaged as [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) by Allison Horst, Alison Hill and Kristen Gorman. Public domain (CC0). Details in [05-files-and-data/data](05-files-and-data/data/README.md) and [11-capstone/data](11-capstone/data/README.md).
- **California housing** (Modules 12 and 14): built from the 1990 US Census by Kelley Pace and Ronald Barry (1997), distributed through StatLib. Details in [12-supervised-learning/data](12-supervised-learning/data/README.md).
- **Bank marketing** (Module 13): calls from a Portuguese bank's campaigns, 2008 to 2010, by Sérgio Moro, Paulo Rita and Paulo Cortez (2014), from the UCI Machine Learning Repository. CC BY 4.0. Details in [13-evaluating-classifiers/data](13-evaluating-classifiers/data/README.md).
- **Wholesale customers** (Module 15): annual spending of 440 customers of a Portuguese wholesale distributor, by Margarida Cardoso (2013), from the UCI Machine Learning Repository. CC BY 4.0. Details in [15-unsupervised-learning/data](15-unsupervised-learning/data/README.md).
- **Bike sharing** (Module 16): daily and hourly rentals from Capital Bikeshare, Washington, D.C., 2011 and 2012, by Hadi Fanaee-T (2013), from the UCI Machine Learning Repository. CC BY 4.0.
- **Online retail** (Module 16): a year of transactions from a UK online shop, by Daqing Chen (2015), from the UCI Machine Learning Repository. CC BY 4.0. Details for both in [16-time-series-and-recommendations/data](16-time-series-and-recommendations/data/README.md).
- **Fashion-MNIST** (Module 17): 70,000 small photos of clothing from Zalando's catalogue, by Han Xiao, Kashif Rasul and Roland Vollgraf (2017). MIT licence. Downloaded from the [official repository](https://github.com/zalandoresearch/fashion-mnist) when the mini project runs. Details in [17-deep-learning-pytorch/data](17-deep-learning-pytorch/data/README.md).
- **TrashNet** (Module 18): 2,527 photos of rubbish in six recycling classes, by Gary Thung and Mindy Yang (Stanford, 2016). MIT licence. Downloaded from the [official repository](https://github.com/garythung/trashnet) when the mini project runs. Module 18 also uses ResNet-18 weights pretrained on ImageNet, downloaded by torchvision, and sample photos bundled with scikit-image. Details in [18-computer-vision/data](18-computer-vision/data/README.md).
- **Tiny Shakespeare** (Module 19): about 40,000 lines of Shakespeare's plays in one text file, collected by Andrej Karpathy for [char-rnn](https://github.com/karpathy/char-rnn) (MIT licence; the plays are in the public domain). Details in [19-sequences-and-transformers/data](19-sequences-and-transformers/data/README.md).
- **Models for Module 20**: SmolLM2-135M-Instruct, SmolLM2-360M-Instruct and all-MiniLM-L6-v2, all Apache 2.0, downloaded from the Hugging Face Hub when the notebooks run. The library handbook used there is invented for the course. Details in [20-llms-in-practice/data](20-llms-in-practice/data/README.md).
- **Adult census income** (Module 21): 32,561 records from the 1994 United States census, by Barry Becker and Ronny Kohavi (1996), from the UCI Machine Learning Repository. CC BY 4.0. The final capstone reuses the bank marketing data from Module 13. Details in [21-responsible-and-production-ai/data](21-responsible-and-production-ai/data/README.md).
- Small datasets bundled with scikit-learn (diabetes, breast cancer, handwritten digits) are used in some lessons.

## License

MIT. Use it, share it, adapt it for your own study group or class.
