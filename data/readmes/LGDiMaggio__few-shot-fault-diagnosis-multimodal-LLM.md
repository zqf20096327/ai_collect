# Few-Shot Bearing Fault Diagnosis with Multimodal LLMs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18376905.svg)](https://doi.org/10.5281/zenodo.18376905)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📄 Overview

This repository provides the official implementation for few-shot learning-based bearing fault diagnosis using:

1. **Multimodal Large Language Models (MLLMs)**:

   - GPT-4o (OpenAI)
   - GPT-5.1 (OpenAI)
   - Claude 4.5 Haiku (Anthropic)
   - Claude 4.5 Sonnet (Anthropic)
   - LLaVA-1.5-7B (Open-source, HuggingFace: `liuhaotian/llava-v1.5-7b`)
2. **Prototypical Networks** (baseline):

   - ResNet-50 backbone (pretrained on ImageNet)
   - Swin Transformer V2-T backbone (pretrained on ImageNet)

### Problem Setup

- **Task**: 4-way classification of bearing health conditions:

  - **H**: Healthy machine
  - **IR**: Inner race fault
  - **OR**: Outer race fault
  - **B**: Rolling element (ball) fault
- **Input**: Continuous Wavelet Transform (CWT) images of vibration signals

  - Envelope analysis with 1400-2800 Hz band-pass filter
  - Morse wavelet with 24 voices per octave
  - 300x300 pixel images
- **Few-Shot Configurations**: 1-shot, 5-shot, 10-shot learning
- **Evaluation**: 10 repetitions with t-Student 95% confidence intervals

---

## 🚀 Quick Start

See [QUICKSTART.md](QUICKSTART.md) for detailed installation and usage instructions.

### Prerequisites

- Python 3.8+
- (Optional) CUDA-compatible GPU for LLaVA local inference

### Installation

```bash
# Clone repository
git clone https://github.com/LGDiMaggio/few-shot-fault-diagnosis-multimodal-LLM.git
cd few-shot-fault-diagnosis-multimodal-LLM

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. **Copy .env.example to .env**:
   ```bash
   cp .env.example .env
   ```

2. **Add your API keys** to `.env`:
   ```
   OPENAI_API_KEY=sk-your-openai-key
   ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
   ```

3. **Prepare your dataset**:

   - You must provide your own bearing vibration data
   - Generate CWT images (see Data Format section)
   - Update \config.yaml\ with your data path

### Run Evaluation

```bash
# Evaluate MLLMs
python evaluate_models.py

# Evaluate Prototypical Networks (ResNet-50)
python evaluate_prototypical.py --model resnet50 --n-shots 1 5 10

# Evaluate Prototypical Networks (Swin Transformer)
python evaluate_prototypical.py --model swin_v2_t --n-shots 1 5 10
```

---

## 📊 Data Format

### Required Dataset Structure

The code expects CWT images organized in a single directory with filenames following this convention:

```
{Condition}_{RPM}rpm_{FR}kN_{FA}kN_{Index}.png
```

**Example**:
```
H_607rpm_124.8kN_0kN_1.png
IR_607rpm_124.8kN_0kN_1.png
OR_1214rpm_124.8kN_0kN_5.png
B_1821rpm_124.8kN_0kN_12.png
```

### CWT Preprocessing (from Paper)

1. **Envelope Analysis**:

   - Band-pass filter: 1400-2800 Hz
   - Extract vibration envelope from raw signal
2. **Continuous Wavelet Transform**:

   - Wavelet: Morse wavelet
   - Frequency resolution: 24 voices per octave
   - Output: Time-frequency representation (300x300 pixels)
3. **Image Encoding**:

   - Save as PNG format
   - RGB or grayscale

### User Data Requirements

⚠️ **Important**: This repository does NOT include the original dataset used in the paper. You must:

1. Collect your own bearing vibration signals
2. Apply the CWT preprocessing described above
3. Place images in the `data/cwt_images/` directory
4. Update `config.yaml` with appropriate file naming patterns

---

## 🧠 Models

### Multimodal LLMs

All MLLM implementations use vision-enabled models with few-shot prompting:

| Model             | Provider  | API Model ID                 | Type                |
| ----------------- | --------- | ---------------------------- | ------------------- |
| GPT-4o            | OpenAI    | `gpt-4o-2024-08-06`          | Cloud API           |
| GPT-5.1           | OpenAI    | `gpt-5.1-2025-11-13`         | Cloud API           |
| Claude Haiku 4.5  | Anthropic | `claude-haiku-4-5-20251001`  | Cloud API           |
| Claude Sonnet 4.5 | Anthropic | `claude-sonnet-4-5-20250929` | Cloud API           |
| LLaVA-1.5-7B      | Open      | `liuhaotian/llava-v1.5-7b`   | Local (HuggingFace) |

**LLaVA Note**: First run downloads ~13GB model from HuggingFace. Requires GPU for practical inference.

### Prototypical Networks

Traditional few-shot learning baseline using:

- **easyfsl** library for episodic training
- Pretrained feature extractors (ImageNet):
  - ResNet-50: Deep residual network
  - Swin Transformer V2-T: Vision transformer

**Method**: Compute class prototypes as mean of support embeddings, classify via Euclidean distance.

---

## 📁 Repository Structure

```
.
├── README.md                    # This file
├── QUICKSTART.md               # Quick start guide
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
├── config.yaml                 # Experiment configuration
├── .env.example                # API key template
├── .gitignore                  # Git ignore rules
│
├── utils/                      # Core utilities
│   ├── __init__.py
│   ├── models.py              # MLLM interfaces (OpenAI, Anthropic, LLaVA)
│   ├── prompts.py             # Few-shot prompt construction
│   ├── data_loader.py         # CWT image loading
│   └── metrics.py             # Evaluation metrics
│
├── evaluate_models.py          # Main MLLM evaluation script
├── evaluate_prototypical.py    # Prototypical Networks evaluation
│
└── results/                    # Output directory (created on run)
    └── *.xlsx                 # Per-model results
```

---

## 🔧 Configuration

Edit `config.yaml` to customize:

- `experiment.n_shot_configs`: Few-shot values (e.g., `[1, 5, 10]`)
- `experiment.n_repetitions`: Number of repetitions (default: 10)
- `experiment.prompt_style`: `"concise"` or `"detailed"`
- `dataset.folder_path`: Path to your CWT images
- `models[].enabled`: Enable/disable specific models

---

## 📈 Results

Results are saved as Excel files in `results/`:

- **Per-repetition metrics**: Accuracy, Precision, Recall, F1, Time
- **Summary statistics**: Mean, Std, 95% CI (t-Student distribution)

**Example output**:
```
results/
├── gpt-4o_detailed_1-shot_all_speeds.xlsx
├── gpt-4o_detailed_5-shot_all_speeds.xlsx
├── claude-sonnet-4.5_detailed_10-shot_all_speeds.xlsx
└── ...
```

---

## 📖 Citation

If you use this code in your research, please cite:

```bibtex
@software{dimaggio2026fewshot,
  author       = {Di Maggio, Luigi Gianpio},
  title        = {Few-Shot Bearing Fault Diagnosis with Multimodal 
                  LLMs and Prototypical Networks},
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.18376905},
  url          = {https://doi.org/10.5281/zenodo.18376905}
}
```

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **LLaVA**: Liu et al., "Visual Instruction Tuning" (NeurIPS 2023)
  - HuggingFace model: `liuhaotian/llava-v1.5-7b`
- **Prototypical Networks**: Snell et al., "Prototypical Networks for Few-shot Learning" (NeurIPS 2017)
- **easyfsl**: Few-Shot Learning library by Sicara

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request.

---

## ⚠️ Disclaimer

This repository was prepared with AI support to facilitate academic reproducibility. All code derives from the original research implementation used in the paper.

**Users must provide their own bearing vibration datasets.** No original data is included in this repository.

---

## 📧 Contact

For questions or collaboration:

- **Luigi Gianpio Di Maggio**: [luigi.dimaggio@polito.it](mailto:luigi.dimaggio@polito.it)

**Affiliation**: Politecnico di Torino, Department of Mechanical and Aerospace Engineering
