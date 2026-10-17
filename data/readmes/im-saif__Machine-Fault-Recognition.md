<div align="center">
  <h1>⚙️ Machine Listener System</h1>
  <p><strong>Machine Fault Recognition using STgram-EfficientNet Architecture</strong></p>
  
  [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
  [![PyTorch](https://img.shields.io/badge/PyTorch-2.2+-ee4c2c.svg)](https://pytorch.org/)
  [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Deployed-yellow.svg)](https://huggingface.co/spaces/youssefwafa/machine-fault-demo)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](#)
</div>

---

## 📖 Abstract
This repository contains the development of an automated **“Machine Listener”** system designed to classify acoustic emissions from industrial machinery. Leveraging a hybrid **STgram-EfficientNet-B0** architecture, the system distinguishes between normal and abnormal operations across three distinct machine types. By integrating log-Mel spectrograms with a 1D-CNN temporal feature extractor (TgramNet), our model achieved a test accuracy of **97%**. The implementation follows a robust pipeline including silence trimming, RMS normalization, and Focal Loss to address class imbalance.

---

## 🚀 Introduction
Predictive maintenance is a critical component of modern Industry 4.0, aiming to detect mechanical failures before they escalate into costly downtime. Acoustic signals provide a non-intrusive way to monitor machine health. This project focuses on a 6-class classification problem involving three machine types, each having “Normal” and “Abnormal” states. 

The primary challenge lies in handling background noise, volume variations, and the inherent similarity between acoustic signatures of different machines. This work builds on established benchmarks for industrial machine anomaly detection, including the MIMII dataset and the DCASE challenge framework.

---

## 🧠 System Architecture

![System Architecture Pipeline](./architecture.png)

The system architecture follows a dual-path approach to extract both frequency and temporal features from raw audio:

- **Preprocessing**: Audio files are resampled to 16kHz and converted to mono. We apply RMS normalization and trim silences to ensure the model focuses on relevant machine sounds.
- **Feature Extraction**: The system generates a 128-band Mel Spectrogram with CMVN (Cepstral Mean and Variance Normalization). Simultaneously, a TgramNet (1D CNN) processes the raw wave to extract temporal embeddings.
- **Model Backbone**: We utilize an EfficientNet-B0 backbone, modified to accept a 2-channel input (Spectrogram + Tgram).
- **Classification Head**: A multi-layer perceptron (MLP) mapping 2560 features down to the final 6 classes.

---

## ⚙️ Experimental Setup
Our experiments utilized a dataset of 56,236 audio files, split using a session-aware strategy to prevent data leakage between training and testing (67.5% train / 11.7% validation / 20.8% test). Training was distributed across 2 GPUs with an effective batch size of 256. The model contains **5.49M parameters**.

- **Hyperparameters**: AdamW optimizer with a learning rate of $3 \times 10^{-4}$ and a cosine annealing scheduler.
- **Data Augmentation**: Gain variations, Gaussian noise, and frequency/time masking (SpecAugment) to improve robustness.
- **Loss Function**: Focal Loss ($\gamma = 2.0$) to handle class imbalance between Normal and Abnormal samples.
- **SWA**: Stochastic Weight Averaging was enabled in the final 12 epochs to improve generalization.

---

## 📊 Results
The model converged after 29 epochs due to early stopping, reaching a **test accuracy of 97%** on the unseen held-out test set of 11,333 samples.

| Class | Precision | Recall | F1-score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **M1-Normal** | 0.99 | 1.00 | 0.99 | 3245 |
| **M1-Abnormal** | 1.00 | 0.92 | 0.96 | 584 |
| **M2-Normal** | 0.93 | 1.00 | 0.96 | 3561 |
| **M2-Abnormal** | 0.98 | 0.69 | 0.81 | 901 |
| **M3-Normal** | 1.00 | 1.00 | 1.00 | 2447 |
| **M3-Abnormal** | 1.00 | 1.00 | 1.00 | 595 |
| **Accuracy** | | | **0.97** | **11333** |
| **Macro Avg** | 0.98 | 0.94 | 0.95 | 11333 |
| **Weighted Avg** | 0.97 | 0.97 | 0.97 | 11333 |

**Analysis**: The system performs exceptionally well on Machine 3, achieving perfect precision and recall. However, a notable drop in recall is observed for "M2-Abnormal" (0.69), where abnormal sounds were frequently misclassified as normal. This is consistent with the acoustic characteristics of Machine 2, where the deviation between normal and abnormal states is more subtle. The high precision for M2-Abnormal (0.98) confirms that when the model does predict abnormal, it is almost always correct — the challenge lies purely in detection sensitivity.

---

## 🛠️ Usage & Inference

### Requirements
To install requirements locally:
```bash
pip install -r requirements.txt
```

Alternatively, build the Docker environment:
```bash
docker build -t machine-listener .
```

### Running Inference
Ensure your trained model is saved as `best_model.pkl` in the root directory.

Run inference by passing the directory containing `.wav` test files:
```bash
python infer.py /path/to/data
```
This will output `results.txt` and `time.txt` in the current directory, respecting the numerical order of the file names (e.g., `1.wav`, `2.wav`, `3.wav`).

---

## ☁️ Cloud Deployment (Bonus)
The model has been deployed as an interactive demo on Hugging Face Spaces, allowing real-time inference on uploaded audio files:
👉 **[Interactive Demo](https://huggingface.co/spaces/karimzakzouk/machine-fault-demo)**


---

## 📚 References
1. Y. Koizumi et al., “Description and discussion on DCASE2020 challenge task 2: Unsupervised anomalous sound detection for machine condition monitoring,” in Proc. DCASE Workshop, 2020.
2. H. Purohit et al., “MIMII dataset: Sound dataset for malfunctioning industrial machine investigation and inspection,” arXiv:1909.09347, 2019.
3. Y. Liu, J. Guan, Q. Zhu, and W. Wang, “Anomalous sound detection using spectral-temporal information fusion,” in Proc. ICASSP, 2022.
4. T.-Y. Lin et al., “Focal loss for dense object detection,” IEEE Trans. Pattern Anal. Mach. Intell., 2020.
5. P. Izmailov et al., “Averaging weights leads to wider optima and better generalization,” in Proc. UAI, 2018.

---


## 👥 Contributors

<table width="100%">
  <tr>
    <td align="center"><a href="https://github.com/im-saif"><img src="https://github.com/im-saif.png" width="80" style="border-radius:50%" alt="im-saif"></a><br><a href="https://github.com/im-saif"><b>@im-saif</b></a></td>
    <td align="center"><a href="https://github.com/karimzakzouk"><img src="https://github.com/karimzakzouk.png" width="80" style="border-radius:50%" alt="karimzakzouk"></a><br><a href="https://github.com/karimzakzouk"><b>@karimzakzouk</b></a></td>
    <td align="center"><a href="https://github.com/MazenEwiss"><img src="https://github.com/MazenEwiss.png" width="80" style="border-radius:50%" alt="MazenEwiss"></a><br><a href="https://github.com/MazenEwiss"><b>@MazenEwiss</b></a></td>
    <td align="center"><a href="https://github.com/Youssefwafa7"><img src="https://github.com/Youssefwafa7.png" width="80" style="border-radius:50%" alt="Youssefwafa7"></a><br><a href="https://github.com/Youssefwafa7"><b>@Youssefwafa7</b></a></td>
  </tr>
</table>
