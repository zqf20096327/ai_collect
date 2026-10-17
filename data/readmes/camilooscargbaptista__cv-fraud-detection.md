# CV Fraud Detection

Computer Vision pipeline for document fraud detection and digital forensics

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

End-to-end pipeline for detecting manipulations in documents, images and videos using deep learning. This project provides comprehensive tools for digital forensics, including CNN-based classifiers, pixel-level analysis, metadata verification, and forensic artifact detection.

## Features

- **Document Authenticity Verification**: Validate document integrity and detect forged elements
- **Image Manipulation Detection**: Identify cloning, splicing, and content-aware fills
- **Deepfake Preliminary Screening**: Detect synthetic media in document images
- **Compression Artifact Analysis**: Analyze JPEG compression inconsistencies
- **Metadata Consistency Checks**: Verify EXIF data, timestamps, and software signatures

## Architecture

```
CV Fraud Detection Pipeline
|
├── Input Document
│   ├── Image Loading & Preprocessing
│   └── Format Validation
|
├── Analysis Pipeline
│   ├── Pixel Analysis
│   │   ├── Error Level Analysis (ELA)
│   │   ├── Noise Analysis
│   │   └── Clone Detection
│   │
│   ├── Metadata Analysis
│   │   ├── EXIF Data Extraction
│   │   ├── Compression History
│   │   └── Software Signatures
│   │
│   └── Deep Learning Classification
│       ├── Feature Extraction
│       ├── CNN Classifier
│       └── Confidence Scoring
|
└── Forensic Report
    ├── Detection Results
    ├── Confidence Metrics
    ├── Artifact Evidence
    └── Recommendations
```

## Installation

### Requirements

- Python 3.10 or higher
- CUDA 11.8+ (optional, for GPU acceleration)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/camilogiradelli/cv-fraud-detection.git
cd cv-fraud-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Usage

### Single Document Analysis

```python
from cv_fraud.analyzer import DocumentAnalyzer

analyzer = DocumentAnalyzer()
results = analyzer.analyze_document("path/to/document.pdf")
report = analyzer.generate_report(results)
print(report)
```

### Batch Processing

```python
from cv_fraud.analyzer import DocumentAnalyzer
import os

analyzer = DocumentAnalyzer()
documents_dir = "path/to/documents"

for filename in os.listdir(documents_dir):
    if filename.endswith(('.pdf', '.jpg', '.png')):
        results = analyzer.analyze_document(os.path.join(documents_dir, filename))
        report = analyzer.generate_report(results)
        print(f"{filename}: {report.fraud_detected}")
```

### Advanced Analysis

```python
from cv_fraud.analyzer import DocumentAnalyzer
from cv_fraud.pixel_analysis import PixelAnalyzer
from cv_fraud.metadata import MetadataVerifier

analyzer = DocumentAnalyzer()

# Analyze with custom configuration
results = analyzer.analyze_document(
    "document.png",
    enable_ela=True,
    enable_metadata_check=True,
    model_confidence_threshold=0.75
)

# Access individual analysis modules
pixel_analyzer = PixelAnalyzer()
metadata_verifier = MetadataVerifier()
```

## Supported Formats

### Images
- JPEG (.jpg, .jpeg) - Primary format, supports EXIF
- PNG (.png) - Lossless format analysis
- TIFF (.tif, .tiff) - High-quality document scans
- BMP (.bmp) - Uncompressed format analysis

### Documents
- PDF - Multi-page document support
- TIFF stacks - Document imaging standard

## Datasets

This project is compatible with the following forensics datasets:

- NIST DFIG (Digital Forensics Image Gallery)
- IEEE Forensics & Security Challenge datasets
- CAIDA (Copymove-Aware Image Dataset)
- SpliceRAD (Splicing Rate Aware Detection)

For training your own models, ensure images are labeled with ground truth manipulation masks.

## Project Structure

```
cv-fraud-detection/
├── src/cv_fraud/
│   ├── __init__.py
│   ├── analyzer.py              # Main analysis orchestrator
│   ├── pixel_analysis.py         # Pixel-level forensics
│   ├── metadata.py               # EXIF and metadata analysis
│   ├── report.py                 # Report generation
│   ├── utils.py                  # Utility functions
│   └── models/
│       ├── __init__.py
│       ├── classifier.py         # CNN classification model
│       └── feature_extractor.py  # Feature extraction pipeline
├── examples/
│   ├── analyze_document.py       # Single document example
│   └── batch_analysis.py         # Batch processing example
├── tests/
│   ├── test_pixel_analysis.py   # Pixel analysis tests
│   └── test_metadata.py         # Metadata tests
├── README.md
├── LICENSE
├── requirements.txt
└── setup.py
```

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_pixel_analysis.py -v

# Run with coverage
pytest --cov=src/cv_fraud tests/
```

## Performance

Typical analysis times (GPU enabled):

- Single image analysis: 100-500ms
- Batch of 100 images: 10-50s
- Large format document (300dpi): 1-3s

Memory requirements:

- Minimum: 2GB RAM
- Recommended: 8GB RAM + GPU with 4GB VRAM

## Citation

If you use this project in academic or professional work, please cite:

```bibtex
@software{girardelli2026cvfraud,
  author = {Girardelli, Camilo},
  title = {CV Fraud Detection: Computer Vision Pipeline for Document Fraud Detection},
  year = {2026},
  url = {https://github.com/camilogiradelli/cv-fraud-detection}
}
```

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Contributing

Contributions are welcome. Please ensure code follows PEP 8 style guidelines and includes appropriate tests.

## Author

**Camilo Girardelli**
- IEEE Senior Member
- Senior Software Architect
- CTO at Girardelli Tecnologia

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated**: March 2026
**Version**: 1.0.0
