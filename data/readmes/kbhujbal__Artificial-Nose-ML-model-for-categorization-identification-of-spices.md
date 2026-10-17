# Artificial Nose — Spice Identification using Machine Learning

Implementation of the research paper:

> **Artificial Nose: Machine Learning model for categorization & identification of spices**  
> Kunal Bhujbal, Prof. Asha Rawat — IEEE Conference, 2023

---

## Overview

An Artificial Nose system that identifies three spices — **Cinnamon**, **Clove**, and **Nutmeg** — using an array of 8 MOS gas sensors and a **Random Forest classifier** (10 decision trees). A Multilayer Perceptron (MLP) is also trained for comparison.

| Model | Cinnamon | Clove | Nutmeg |
|-------|----------|-------|--------|
| **Random Forest** | **100%** | **100%** | **100%** |
| MLP Neural Network | ~96% | ~97% | ~97% |

---

## System Architecture

```
Odour Sample → Gas Sensor Array (×8) → Signal Conditioning
             → PIC Microcontroller (10-bit ADC) → Serial USB
             → PC Data Acquisition (Java / Excel)
             → Python ML Pipeline → Spice Classification
```

### Sensors Used
| Sensor | Type |
|--------|------|
| MQ 135 | Air quality / ammonia |
| TGS 813 | Combustible gases |
| TGS 800 | Air contaminants |
| TGS 823 | Organic solvents |
| TGS 2610 | LP gas / butane (**most important feature**) |
| TGS 2602 | VOCs / odorous gases |
| TGS 2620 | Organic solvents |
| TGS 2611 | Methane |

---

## Project Structure

```
Artificial Nose/
├── data/
│   ├── raw/                    # Raw sensor CSVs (real or synthetic)
│   └── processed/              # Reserved for future use
├── src/
│   ├── data_generator.py       # Synthetic data / real CSV loader
│   ├── preprocessor.py         # Clean → encode → scale → split
│   ├── evaluator.py            # Metrics: Table I, Table II, confusion matrix
│   ├── visualizer.py           # Figures 6, 7, 8 + comparison chart
│   └── models/
│       ├── random_forest.py    # Primary model (paper's main contribution)
│       └── mlp.py              # Comparison model
├── notebooks/
│   └── analysis.ipynb          # Full walkthrough with inline figures
├── results/                    # Auto-generated figures (PNG)
├── main.py                     # Entry point
└── requirements.txt
```

---

## Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run with synthetic data (no hardware required)
python main.py

# 3. Run with real PIC sensor data
#    CSV must have columns: MQ135, TGS813, TGS800, TGS823,
#                           TGS2610, TGS2602, TGS2620, TGS2611, label
python main.py --data data/raw/sensor_data.csv

# 4. Run without opening plot windows (CI / headless server)
python main.py --no-plots
```

---

## Using Real Hardware Data

If you have the physical Artificial Nose setup (PIC microcontroller + sensor array):

1. Run the Java acquisition software — it saves readings to an Excel file.
2. Export as CSV with these **exact column names**:
   ```
   MQ135, TGS813, TGS800, TGS823, TGS2610, TGS2602, TGS2620, TGS2611, label
   ```
   where `label` is one of: `cinnamon`, `clove`, `nutmeg`.
3. Place the file at `data/raw/sensor_data.csv` and run `python main.py`.

---

## Output — Paper Figures

| File | Corresponds to |
|------|---------------|
| `results/figure6_sensor_responses.png` | Figure 6 — Avg sensor voltage per spice |
| `results/figure7_confusion_matrix_random_forest.png` | Figure 7 — RF confusion matrix |
| `results/figure7_confusion_matrix_mlp_neural_network.png` | Figure 7 — MLP confusion matrix |
| `results/figure8_feature_importance.png` | Figure 8 — TGS2610 most important |
| `results/algorithm_comparison.png` | Table II — RF vs MLP bar chart |

---

## Key Results (Paper)

**Table I** — Mean accuracy across 9 test runs (Random Forest):

| Spice | Accuracy |
|-------|----------|
| Clove | 90.65% |
| Cinnamon | 90.06% |
| Nutmeg | 99.09% |

**Table II** — Final test accuracy:

| Algorithm | Cinnamon | Clove | Nutmeg |
|-----------|----------|-------|--------|
| Random Forest | 100% | 100% | 100% |
| MLP | 96.87% | 97.38% | 97.32% |

---

## Notebook

For an interactive walkthrough with inline figures, open:

```bash
jupyter notebook notebooks/analysis.ipynb
```

---

## Citation

```
Bhujbal, K., & Rawat, A. (2023). Artificial Nose: Machine Learning model
for categorization & identification of spices. IEEE Conference.
```
