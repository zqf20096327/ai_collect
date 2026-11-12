<div align="center">

![Banner](./assets/banner.svg)
<br>
  <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch (training)">
  <img src="https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/-Numba-00A3E0?style=for-the-badge&logo=numba&logoColor=white" alt="Numba">
  <img src="https://img.shields.io/badge/-ONNX%20Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime">
  <a href="https://colab.research.google.com/github/DavidTorro/gdg-uam-ml-contest-2026/blob/main/colab.ipynb"><img src="https://img.shields.io/badge/-Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Run the submission check in Google Colab"></a>
  <a href="https://github.com/DavidTorro">
    <img src="https://img.shields.io/badge/author-David%20Torr%C3%B3-181717?style=for-the-badge&logo=github&logoColor=white" alt="Author: David Torró">
  </a>
  <p>
    <img src="assets/language-en-active.svg" alt="English (current language)" width="56" height="30"><a href="README.es.md"><img src="assets/language-es-inactive.svg" alt="Leer en español" width="56" height="30"></a><a href="https://gdg-ml.davidtorro.com/?lang=en"><img src="assets/web-link.svg" alt="Website: videos and 3D viewer" width="72" height="30"></a>
  </p>
</div>

# GDG UAM ML Contest 2026

My individual entry for the [GDG UAM ML Contest 2026](https://gdguam.es/blog/guia-concurso-de-ml). The task is to classify a four-channel, 256-step time series into one of eight classes. The official harness calls `predict` on one sample at a time and scores both accuracy and throughput.

## Model

`model.py` loads `models/exp033.sesgo.onnx` by default. It is a 1D CNN exported to ONNX, including the class-6 logit adjustment in the weight file. Inference uses ONNX Runtime on one CPU thread. Numba compiles preprocessing during setup; reusable buffers and ONNX Runtime I/O Binding reduce per-sample overhead. The default inference path does not require PyTorch or training data.

The [approach note](APPROACH.md) explains how we chose and prepared the model.

## Demo results

![Results table: 338 of 400 correct on the official demo, 84.5% accuracy and 3.779 score; 120.576 score in Colab with the same samples repeated](assets/results-table-en.svg)

A short Colab timing of 0.1064 ms per prediction suggested roughly 142 points if sustained. The full 60 s harness run averaged 0.1473 ms across 407,260 predictions and scored 120.576 on the repeated demo. With the same sample mix, the score scales roughly with the square root of the number of answers; the lower sustained throughput explains the difference. These runs reuse the same 400 public samples.

## Submission files

![Submission files table: model.py, the ONNX weight, five src modules, and requirements.txt with their purposes](assets/files-table-en.svg)

The official harness provides `competition_api.py`; it is not part of this repository.

## Test from a fresh clone

Choose your environment below. The local commands need Git, Python 3.10 or newer, and `curl`. Run each block in order from a new directory.

### macOS · Terminal

**1. Clone the submission and official materials**

```bash
mkdir gdg-uam-submission-check
cd gdg-uam-submission-check
git clone https://github.com/DavidTorro/gdg-uam-ml-contest-2026.git submission-check
git clone https://github.com/GDG-UAM/ml-contest-materials.git
```

**2. Create the Python environment and install inference dependencies**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r submission-check/requirements.txt
```

**3. Download the public demo and run the official harness**

```bash
curl -fL --create-dirs -o ml-contest-materials/data/test_demo.npz \
  https://github.com/GDG-UAM/ml-contest-materials/releases/latest/download/test_demo.npz
cd ml-contest-materials
../.venv/bin/python harness.py evaluate --model ../submission-check/model.py \
  --source file:data/test_demo.npz --runs 1
```

### Linux · Terminal

**1. Clone the submission and official materials**

```bash
mkdir gdg-uam-submission-check
cd gdg-uam-submission-check
git clone https://github.com/DavidTorro/gdg-uam-ml-contest-2026.git submission-check
git clone https://github.com/GDG-UAM/ml-contest-materials.git
```

**2. Create the Python environment and install inference dependencies**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r submission-check/requirements.txt
```

**3. Download the public demo and run the official harness**

```bash
curl -fL --create-dirs -o ml-contest-materials/data/test_demo.npz \
  https://github.com/GDG-UAM/ml-contest-materials/releases/latest/download/test_demo.npz
cd ml-contest-materials
../.venv/bin/python harness.py evaluate --model ../submission-check/model.py \
  --source file:data/test_demo.npz --runs 1
```

### Windows · PowerShell

**1. Clone the submission and official materials**

```powershell
New-Item -ItemType Directory gdg-uam-submission-check
Set-Location gdg-uam-submission-check
git clone https://github.com/DavidTorro/gdg-uam-ml-contest-2026.git submission-check
git clone https://github.com/GDG-UAM/ml-contest-materials.git
```

**2. Create the Python environment and install inference dependencies**

```powershell
py -3 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r .\submission-check\requirements.txt
```

**3. Download the public demo and run the official harness**

```powershell
curl.exe -fL --create-dirs -o ml-contest-materials\data\test_demo.npz `
  https://github.com/GDG-UAM/ml-contest-materials/releases/latest/download/test_demo.npz
Set-Location ml-contest-materials
& ..\.venv\Scripts\python.exe harness.py evaluate --model ..\submission-check\model.py `
  --source file:data/test_demo.npz --runs 1
```

The public demo should report **338 correct predictions out of 400** (84.5%). Runtime and latency depend on the computer.

### Google Colab · no local setup

The [English verification notebook](https://colab.research.google.com/github/DavidTorro/gdg-uam-ml-contest-2026/blob/main/colab.ipynb) runs the same check in a Colab CPU runtime. It clones both public repositories, installs the pinned inference dependencies, verifies the demo download by SHA-256, and calls the official harness.

1. Open the notebook and connect to a **fresh CPU runtime**. If the runtime already contains a previous clone, choose **Runtime → Disconnect and delete runtime**, then reconnect.
2. Choose **Runtime → Run all**. Colab runs the cells in order; the dependency installation and model setup can take a few minutes.
3. Check the final **✅ PASS · public demo** table: 400 samples, 338 correct predictions, and a demo score of approximately 3.778906. The displayed commit is the revision cloned during that run; latency can vary.

The notebook only downloads the public demo and does not train the model.

## License

The original source code, notebooks, documentation, and SVG assets in this repository are available under the [MIT License](LICENSE). The ONNX weight at `models/exp033.sesgo.onnx` is excluded: it is provided for evaluation of this contest entry, and no separate license for reuse is granted.
