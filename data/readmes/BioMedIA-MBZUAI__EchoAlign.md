# EchoAlign

[![Preprint](https://img.shields.io/badge/Preprint-arXiv-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2611.27517)
[![Weights](https://img.shields.io/badge/Weights-Hugging%20Face-FFD21E)](https://huggingface.co/EchoAlign/EchoAlign)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](#installation)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.6.0-EE4C2C?logo=pytorch&logoColor=white)](#installation)

## Abstract

Echocardiography assesses the structure and function of the heart. Cardiologists read each study across several standard views and report the findings visible in those views by cardiac structure. AI foundation models can learn to analyze these studies from clinical reports, reducing annotation burden and supporting clinical interpretation. However, existing models are trained by pairing each video with the full clinical report, including structures and findings its view does not show. This mismatch lets a model associate a finding with incidental or spurious signals rather than its visual evidence, which limits accuracy, anatomical grounding and clinical trust. Here we introduce EchoAlign, a vision-language foundation model developed on 2.87 million echocardiographic videos and images from 159 clinical centers. EchoAlign aligns each cardiac structure, video and study with its report text, and a visibility matrix restricts supervision to the views that actually depict each structure. We compare it with five public foundation models on 0.47 million test videos across ten unseen external datasets from more than 25 clinical centers. EchoAlign achieves the highest mean AUROC of 0.890 (95% CI, 0.881 to 0.897) for classification and the highest mean quadratic weighted kappa of 0.530 (95% CI, 0.511 to 0.544) for severity grading. Across 62 clinical findings, EchoAlign provides one model that detects findings, grades their severity, estimates measurements and segments cardiac structures.

## Model weights

![EchoAlign pipeline: a video encoder and a study transformer aligned with a text encoder at the video, structure, and study levels](assets/echoalign_pipeline.png)

All model weights are in one file:

| File | Video encoder | Study transformer | Text encoder | PCA bases | Total | Download |
|---|---:|---:|---:|---:|---:|---|
| `EchoAlign.pt` | 124.4 M | 5.5 M | 109.9 M | 0.9 M | 240.7 M | [Hugging Face](https://huggingface.co/EchoAlign/EchoAlign) |

Counts are parameters. The PCA (principal component analysis) bases are fitted after training. They project the 13 outputs onto 64 components each, which gives the 832-number representation used for linear probes.

After you complete the [installation](#installation), create the folder with `mkdir -p weights` and save the file as `weights/EchoAlign.pt`.

## Installation

The code was tested with Python 3.10 in a Conda environment, PyTorch 2.6.0, and ffmpeg.

To set up the environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone --recursive https://github.com/BioMedIA-MBZUAI/EchoAlign.git
   cd EchoAlign
   ```

2. Create a Python 3.10 environment:

   ```bash
   conda create -n echoalign python=3.10
   conda activate echoalign
   ```

3. Install PyTorch 2.6.0 and torchvision 0.21.0 for your hardware. Pick the command that matches your GPU from the [PyTorch previous-versions page](https://pytorch.org/get-started/previous-versions/#v260). For example, for CUDA 12.4:

   ```bash
   pip install torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124
   ```

   For ROCm 6.2, use `--index-url https://download.pytorch.org/whl/rocm6.2.4`. For CPU only, use `--index-url https://download.pytorch.org/whl/cpu`.

4. Install the other packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Check that PyTorch sees your GPU:

   ```bash
   python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
   ```

   On AMD GPUs, PyTorch also reports ROCm devices through `torch.cuda`.

## Baseline models

The evaluation benchmarks EchoAlign against five published models: **EchoPrime**, **PanEcho**, **EchoCLIP**, **EchoJEPA**, and **EchoFM**.
EchoJEPA and EchoFM are video encoders without a text encoder or task heads, so they are evaluated by linear probing only, not zero-shot.
Their official code is included as Git submodules in `models/`. See [BASELINES.md](BASELINES.md) for download links, setup instructions, and how to test your own model.

For the parameter count of each baseline, see [Model size](BASELINES.md#model-size) in BASELINES.md.

## Datasets

The paper evaluates EchoAlign on both private and public datasets. The private dataset is an in-house cohort and is not shared.
See [DATASETS.md](DATASETS.md) for the public datasets, access instructions, and manifest file formats.

The paper's MIMIC-IV-Echo labels are built from [MIMIC-IV-Echo v1.0](https://physionet.org/content/mimic-iv-echo/1.0/).

## Evaluate the models

The paper evaluates every model in three ways, all on frozen encoders:

- **Zero-shot:** each model scores each finding with its own method, with no training on the evaluation labels.
- **Linear probing:** a linear model is fitted on each model's study features for each task. Tasks are of three types:
  - **Binary classification** (finding present or absent): logistic regression, scored by AUROC (area under the ROC curve).
  - **Severity grading** (more than two ordered grades, such as none, mild, moderate, severe): multinomial logistic regression, scored by quadratic weighted kappa (QWK) and by AUROC at each boundary between grades.
  - **Regression** (continuous measurements, such as ejection fraction): ridge regression, scored by root-mean-square error.
- **Segmentation:** a linear head and a small decoder are trained on the feature map of EchoAlign, EchoPrime, PanEcho, and EchoCLIP to segment the heart chambers on CAMUS, EchoNet-Dynamic, and EchoNet-Pediatric.

`scripts/run.py` runs the paper's evaluation up to the predictions. `configs/run.yaml` chooses the
cohorts (`private`, `mimic_iv_echo`, `cardiobench`), the models, the tasks and the steps. `run.py` does
not build labels or manifests: it reads the files that `configs/cohorts.yaml` names for each cohort.

The default cohorts are `mimic_iv_echo` and `cardiobench`. The `private` cohort needs the private data,
which is not distributed.

To run the evaluation, follow these steps:

1. Download the datasets and set their folders in `configs/datasets.local.yaml`. See
   [DATASETS.md](DATASETS.md).
2. Build the MIMIC-IV-Echo split and label files and the CardioBench label files:

   ```bash
   python scripts/make_mimic_labels.py --mimic-echo <MIMIC-IV-Echo folder>
   python scripts/make_cardiobench_labels.py
   ```

3. Write the manifests:

   ```bash
   python scripts/make_manifests.py
   ```

4. Check that every step runs, on 5 studies per split of each cohort:

   ```bash
   python scripts/run.py --dry-run
   ```

5. Run the evaluation from the repository root:

   ```bash
   python scripts/run.py
   ```

   With 8 GPUs, embed in parallel first: run this once per GPU, with `<i>` from 0 to 7, then run the command above.

   ```bash
   CUDA_VISIBLE_DEVICES=<i> python scripts/run.py --set embed_shards=8 --set embed_shard=<i>
   ```

To change a setting for one run, use `--set`, for example
`python scripts/run.py --set datasets=[cardiobench] --set steps.segmentation=false`. To see the
commands without running them, use `--print`.

| Step | What it writes |
|---|---|
| `embed` | One embedding file per model and cohort, in `embeddings/<cohort>/` |
| `zeroshot` | Zero-shot scores per model, in `results/<cohort>/zeroshot/` |
| `probes` | Linear-probe predictions on TEST, in `results/<cohort>/probe/` |
| `segmentation` | Segmentation heads and test predictions, in `results/segmentation/` |

A failed step does not stop the others. Each script also runs on its own; run it with `--help` for its options.

To compute the metrics and reproduce each result in the paper, see [RESULTS.md](RESULTS.md).

### Individual analyses

The notebooks in `notebooks/` show the main functions on example data. To analyze your own results, point them at the files that `scripts/run.py` writes:

- `01_quickstart.ipynb`: embed one echo clip and score findings zero-shot.
- `02_linear_probing.ipynb`: fit a linear probe on EchoAlign's 832-number representation.
- `03_evaluation_and_analysis.ipynb`: AUROC with cluster-bootstrap confidence intervals and model comparisons.
- `04_segmentation.ipynb`: EchoAlign's patch-token map for one frame and a linear segmentation head.

## License

[CC BY-NC 4.0](LICENSE).

## Citation

```bibtex
@misc{aly2026echoalignechocardiographyfoundationmodel,
      title={EchoAlign: Echocardiography foundation model with multilevel report alignment},
      author={Ahmed Aly and Darya Taratynova and Lotfi Abdelkrim Mecharbat and Roman A. Sandler and Joseph Z. Sokol and Joshua Penn and Klaus H. Maier-Hein and Numan Saeed and Mohammad Yaqub},
      year={2026},
      eprint={2611.27517},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2611.27517},
}
```
