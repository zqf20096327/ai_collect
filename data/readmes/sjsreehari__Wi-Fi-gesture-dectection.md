<img src="docs/images/image.png" style="height:350px; width:100%">

<div align="center" style="display: flex; flex-wrap: wrap;">
  <a href="https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://pytorch.org/" target="_blank">
    <img src="https://img.shields.io/badge/PyTorch-2.0+-red.svg?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  </a>
  <a href="https://numpy.org/" target="_blank">
    <img src="https://img.shields.io/badge/NumPy-1.24+-blue?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  </a>
  <a href="https://librosa.org/" target="_blank">
    <img src="https://img.shields.io/badge/Librosa-0.10+-green?style=for-the-badge&logo=python" alt="Librosa">
  </a>
  <a href="https://scikit-learn.org/" target="_blank">
    <img src="https://img.shields.io/badge/scikit--learn-1.3+-orange?style=for-the-badge&logo=scikit-learn" alt="Scikit-learn">
  </a>
  <a href="https://scipy.org/" target="_blank">
    <img src="https://img.shields.io/badge/SciPy-1.10+-purple?style=for-the-badge&logo=scipy" alt="SciPy">
  </a>
  <a href="https://www.espressif.com/en/products/socs/esp32" target="_blank">
    <img src="https://img.shields.io/badge/ESP32-Hardware-black?style=for-the-badge&logo=espressif" alt="ESP32">
  </a>
</div>

# WiFi CSI Gesture Detection

WiFi CSI Gesture Detection is an innovative **deep learning-based system** that leverages WiFi Channel State Information (CSI) to detect human presence and gestures without cameras or wearables. The system employs a novel dual-path ensemble architecture combining CNN2D and CNN1D-LSTM models to achieve 90.2% accuracy in classifying occupancy states through ubiquitous WiFi infrastructure, offering a privacy-first, contact-free alternative to traditional vision-based sensing systems.

This project is built and developed by **Sreehari S J**

## Key Features

- **Ensemble Architecture**: Dual-path fusion of CNN2D (spectrogram) and CNN1D-LSTM (temporal) models
- **Contact-Free Sensing**: Detects gestures through WiFi signals without cameras or wearables
- **Privacy-Preserving**: No visual data capture - CSI signals cannot reconstruct images
- **Multi-Class Detection**: Classifies Not Occupied, Occupied Static, and Occupied Motion
- **Real-Time Performance**: <50ms inference time on CPU hardware
- **ESP32 Integration**: Commodity WiFi hardware for CSI data collection
- **Advanced Features**: STFT spectrograms + 8 statistical features per subcarrier
- **Robust Pipeline**: End-to-end preprocessing, feature extraction, and training workflow
- **Through-Wall Detection**: RF signals penetrate non-metallic barriers
- **90.2% Accuracy**: Validated on balanced dataset with 1,680 samples across 3 classes




## System Architecture

![System Architecture](docs/images/System%20Architecture%20Diagram.png)

The system employs a multi-stage pipeline for CSI signal processing and classification:

1. **Preprocessing Module**: Raw CSI amplitude normalization, outlier detection, and sliding window segmentation
2. **Feature Extraction**: Short-Time Fourier Transform (STFT) spectrograms and statistical feature computation
3. **Deep Learning Models**: Ensemble fusion of CNN2D (spectrogram analysis) and CNN1D-LSTM (temporal sequence modeling)
4. **Training Framework**: Cross-validation with early stopping and learning rate scheduling
5. **Evaluation Metrics**: Multi-class accuracy, precision, recall, F1-score, and confusion matrix analysis



## Technical Specifications

### Model Architecture

![Model Architecture - Ensemble](docs/images/Model%20Architecture_(Ensemble).png)

**Ensemble Configuration:**
- CNN2D Branch: Processes 128×128 STFT spectrograms for frequency-time pattern recognition
- CNN1D-LSTM Branch: Analyzes 121-timestep sequences with 8 per-subcarrier statistical features
- Fusion Strategy: Weighted combination (α=0.6 for CNN2D, α=0.4 for LSTM)
- Total Parameters: ~2.1M trainable parameters

**Performance Metrics:**
- Test Accuracy: 90.2%
- Validation Accuracy: 88-92%
- Inference Time: <50ms per prediction (CPU)
- Classes: Not Occupied, Occupied Static, Occupied Motion

### Dataset Structure

```
data/
├── raw/                    # Raw CSI CSV files (timestamp, amplitude vectors)
│   ├── not_occupied/      # Background/empty room recordings
│   ├── occupied_static/   # Stationary human presence
│   └── occupied_motion/   # Active hand gestures and movements
├── preprocessed/          # Normalized and segmented CSI windows (.npy)
└── features/              # Extracted spectrograms and statistical features (.npy)
```

### Dependencies

**Core Libraries:**
- PyTorch >= 2.0.0 (Deep learning framework)
- NumPy >= 1.24.0 (Numerical computing)
- Librosa >= 0.10.0 (Audio signal processing for STFT)
- Scikit-learn >= 1.3.0 (Machine learning utilities)
- SciPy >= 1.10.0 (Scientific computing)

## Usage

### Training Pipeline

Execute the main training script:

```bash
python main.py
```

**Available Operations:**
1. Complete pipeline execution (preprocessing + feature extraction + training)
2. Ensemble model training (requires preprocessed features)
3. Performance metrics visualization
4. Training log inspection

### Directory Structure

```
.
├── ai_pipeline/           # Core machine learning pipeline
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── models.py
│   ├── training.py
│   ├── train_ensemble.py
│   └── models/           # Trained model weights (.pth)
├── data/                 # Dataset repository
├── results/              # Training outputs and evaluation metrics
│   ├── logs/            # JSON metrics and text logs
│   └── plots/           # Training curves and confusion matrices
├── hardware/            # ESP32 CSI data collection firmware
├── utils/               # Utility functions and ONNX export
└── main.py              # Entry point
```

## Data Format Specification

**Input CSV Format:**
```csv
timestamp,csi_raw_data
2025-11-10 00:35:22.099022,"CSI_DATA,STA,MAC_ADDRESS,...,[amplitude_values]"
```

**CSI Vector:**
- Length: 128 subcarriers
- Type: Amplitude values (float32)
- Range: Normalized to [-1, 1]

**Feature Representation:**
- Spectrogram: 128×128 frequency-time matrix (STFT with Hann window)
- Statistical: 8 features × 121 subcarriers (mean, std, skewness, kurtosis, RMS, range, min, max)

## Model Training

**Hyperparameters:**
- Optimizer: AdamW (lr=2e-3, weight_decay=1e-4)
- Batch Size: 32
- Epochs: 40 (with early stopping, patience=10)
- Loss Function: Cross-Entropy Loss
- Learning Rate Schedule: ReduceLROnPlateau (factor=0.5, patience=5)

**Data Split:**
- Training: 80%
- Validation: 20%
- Stratified sampling to maintain class balance

## Results

Trained models are automatically saved to:
- `ai_pipeline/models/ensemble_model_YYYYMMDD_HHMMSS.pth`
- `results/logs/ai_training/metrics_YYYYMMDD_HHMMSS.json`

Performance visualizations:
- Training/validation loss curves
- Accuracy progression
- Confusion matrix heatmap
- Per-class precision-recall metrics

## Model Export

Models can be exported to ONNX format for deployment:
- Dynamic batch size support
- Optimized for CPU inference
- Compatible with ONNX Runtime



## License

This project is licensed under the MIT License.

## Technical Notes

- System designed for training pipeline only (real-time inference components removed)
- Optimized for batch processing of collected CSI datasets
- GPU acceleration supported (CUDA-compatible devices)
- Model checkpoint saving after each improvement in validation accuracy
- Reproducible results with fixed random seed (seed=42)

