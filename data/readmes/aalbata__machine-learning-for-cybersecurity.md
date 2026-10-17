# Machine Learning for Cybersecurity

A free course by Dr. Ali Al Bataineh, Higher Colleges of Technology, United Arab Emirates.

![Code: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)
![Content: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-lightgrey.svg)

The course covers two related subjects. The first is how machine learning is applied to security problems such as intrusion, malware, phishing and fraud detection. The second is how machine learning systems themselves are attacked and defended, from adversarial examples and poisoned training data to deepfakes and prompt injection against language models.

Read the course online at https://aalbata.github.io/machine-learning-for-cybersecurity/

Units 1 to 11 each have three lessons with the mathematics, worked examples and references, labs that run on Google Colab or on a laptop CPU, exercises with worked solutions, and a self-check quiz. Unit 12 is a guide to a project of your own.

## Why I made this

I believe knowledge should be shared, and that no one should have to pay to learn.

Security teams are being asked to adopt machine learning, and attackers have started to use it as well. Much of the material that teaches both sides properly is spread across paid courses and papers behind paywalls. Someone studying at a small college, or an analyst whose organization has no training budget, should be able to learn it to the same depth as anyone else.

I wrote this course so that they can, at no cost. The labs run in a free browser notebook, every lab result quoted in the text comes from code you can run yourself, and claims that are not common knowledge cite their sources. Nothing here needs a GPU or a paid service. To run the labs, the only account you may want is a free Google account for Colab, and you can also run every lab on your own computer.

If it helps you, share it with someone who is starting out. If you find a mistake, please tell me by opening an issue on GitHub, so that the next reader learns it correctly.

Ali Al Bataineh

## Contents

| Unit | Topic | Labs (open in Colab) |
|---|---|---|
| 1 | [Machine learning meets security](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-01/index.html) | [A first look at the network data](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-01/lab01-first-look.ipynb) |
| 2 | [Data, leakage and evaluation](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-02/index.html) | [How leakage inflates a detector](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-02/lab02-leakage.ipynb) |
| 3 | [Supervised learning](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-03/index.html) | [Comparing classifiers on a time-ordered split](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-03/lab03-models.ipynb); [Detecting phishing URLs from their text](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-03/lab03-phishing-urls.ipynb) |
| 4 | [Unsupervised learning and anomaly detection](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-04/index.html) | [Clustering and anomaly detection on network flows](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-04/lab04-anomaly.ipynb) |
| 5 | [Neural networks](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-05/index.html) | [Backpropagation by hand, then in PyTorch](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-05/lab05-backprop.ipynb); [A neural detector and an autoencoder](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-05/lab05-mlp-autoencoder.ipynb) |
| 6 | [Convolutional, sequence and reinforcement learning models](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-06/index.html) | [A convolutional network and transfer learning](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-06/lab06-cnn.ipynb); [Detecting anomalous log sequences with an LSTM](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-06/lab06-log-lstm.ipynb); [Q-learning on a small network](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-06/lab06-qlearning.ipynb) |
| 7 | [Adversarial examples and evasion](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-07/index.html) | [FGSM and PGD against an image classifier](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-07/lab07-evasion-images.ipynb); [Evading a network detector under realistic constraints](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-07/lab07-evasion-flows.ipynb) |
| 8 | [Poisoning, privacy and defenses](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-08/index.html) | [Label flipping and a backdoor](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-08/lab08-poisoning.ipynb); [Membership inference and DP-SGD](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-08/lab08-privacy.ipynb); [Adversarial training and its cost](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-08/lab08-adversarial-training.ipynb) |
| 9 | [Deepfakes and synthetic media](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-09/index.html) | [Generator fingerprints and the generalization gap](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-09/lab09-fingerprints.ipynb) |
| 10 | [Security of language models and agents](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-10/index.html) | [Measuring indirect prompt injection on a small model](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-10/lab10-injection.ipynb); [Least privilege for a tool-using agent](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-10/lab10-agent-guardrails.ipynb) |
| 11 | [Governance, fairness and accountability](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-11/index.html) | [Auditing a detector across two sites](https://colab.research.google.com/github/aalbata/machine-learning-for-cybersecurity/blob/main/labs/unit-11/lab11-fairness-audit.ipynb) |
| 12 | [Capstone project](https://aalbata.github.io/machine-learning-for-cybersecurity/unit-12/index.html) | Project guide |

Before Unit 1, read [How to use this course](https://aalbata.github.io/machine-learning-for-cybersecurity/start.html). If Python, NumPy, pandas or scikit-learn are new to you, start with the [Python primer](https://aalbata.github.io/machine-learning-for-cybersecurity/primer.html).

## Running the labs

In Colab, open a lab from the table above, choose File, then Save a copy in Drive, and run the cells from the top. Colab is free with a Google account.

To run everything on your own computer (Python 3.12):

```
python -m venv .venv             # on macOS or Linux: python3 -m venv .venv
.venv\Scripts\activate          # on macOS or Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Then open any notebook under `labs/`. No lab needs a GPU.

## Repository layout

| Folder | Contents |
|---|---|
| `content/` | The lessons, exercises and quizzes in Markdown and YAML, and the bibliography in `content/refs/` |
| `labs/src/` | The source of each lab, one Python file per notebook |
| `labs/unit-NN/` | The executed notebooks, with their outputs |
| `labs/results/` | The numbers each lab produced, which the lessons quote |
| `data/` | The synthetic course datasets and the script that generates them (see `data/DATA.md`) |
| `figures/` | Every figure, generated by `tools/figures/` |
| `tools/` | The scripts that build the notebooks, the figures and the website |
| `docs/` | The website, as published on GitHub Pages |

## Rebuilding from source

Every number, figure and page is generated from the sources, so the whole course can be rebuilt with four commands from the repository root:

```
python data/make_dataset.py      # regenerates data/flows.csv and data/urls.csv
python tools/build_labs.py       # runs every lab and records its results
python tools/make_figures.py     # draws every figure
python tools/build_site.py       # builds the website in docs/
```

## How to cite

If you use this course in your teaching or research, please cite it as follows.

> Al Bataineh, A. (2026). *Machine Learning for Cybersecurity* (Version 1.0) [Online course]. Higher Colleges of Technology, United Arab Emirates. https://aalbata.github.io/machine-learning-for-cybersecurity/

```bibtex
@misc{albataineh2026mlsecurity,
  author       = {Al Bataineh, Ali},
  title        = {Machine Learning for Cybersecurity},
  year         = {2026},
  version      = {1.0},
  howpublished = {\url{https://aalbata.github.io/machine-learning-for-cybersecurity/}},
  note         = {Online course, Higher Colleges of Technology, United Arab Emirates}
}
```

GitHub also offers these details through the Cite this repository button, which reads `CITATION.cff`.

## License

- Lessons, exercises, quizzes, figures and website text: [Creative Commons Attribution 4.0 (CC BY 4.0)](CONTENT-LICENSE.md).
- Code, notebooks and the synthetic datasets: [MIT License](LICENSE).

You may use, adapt and share all of it, including in your own courses. Please credit it as "Machine Learning for Cybersecurity" by Dr. Ali Al Bataineh, Higher Colleges of Technology.

## Questions and corrections

If something does not work or you find a mistake, please open an issue on GitHub or write to aalbataineh@hct.ac.ae.
