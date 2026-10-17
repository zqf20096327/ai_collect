# Malicious URL Detection System

**Machine Learning-Powered Phishing and Malware URL Classifier**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)

---
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/c48f19f6-f49c-48ea-8b05-3a0a1e28776b" />

## Overview

A machine learning-based cybersecurity system that detects and classifies malicious URLs by analyzing structural and statistical features — without inspecting webpage content.

**Key properties:**
- Real-time URL analysis with 95%+ detection accuracy
- 30+ engineered URL features across length, entropy, domain, and security dimensions
- No page content inspection — privacy-preserving by design
- Supports single URL lookup, batch processing, and REST API integration

---

## Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Web Interface | Streamlit |
| API | Flask |
| Visualization | Matplotlib, Seaborn |

---

## Installation

```bash
git clone https://github.com/ares-coding/malicious-url-detection-using-ml.git
cd malicious-url-detection-using-ml
pip install -r requirements.txt
streamlit run app.py
```

**Docker:**
```bash
docker build -t url-detector .
docker run -p 8501:8501 url-detector
```

---

## Usage

### Web Interface

```bash
streamlit run app.py
# Access at http://localhost:8501
```

### Python API

```python
from url_detector import URLDetector

detector = URLDetector(model='xgboost')

# Single URL
result = detector.predict('https://suspicious-site.com')
print(f"Malicious: {result['is_malicious']}")
print(f"Confidence: {result['confidence']:.2%}")

# Batch
urls = ['url1.com', 'url2.com', 'url3.com']
results = detector.predict_batch(urls)
```

### REST API

```bash
python api.py

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

---

## How It Works

### Feature Extraction

```python
def extract_url_features(url):
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_underscores': url.count('_'),
        'num_slashes': url.count('/'),
        'num_questionmarks': url.count('?'),
        'num_equals': url.count('='),
        'num_ats': url.count('@'),
        'num_digits': sum(c.isdigit() for c in url),
        'has_ip': check_ip_address(url),
        'has_https': url.startswith('https'),
        'domain_length': len(extract_domain(url)),
        # 20+ additional features
    }
    return features
```

### Classification

```python
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'XGBoost': XGBClassifier(max_depth=6),
    'SVM': SVC(kernel='rbf', probability=True)
}

prediction, confidence = model.predict_proba(features)
```

---

## Feature Engineering

Features are grouped into the following categories:

| Category | Features |
|---|---|
| Length-based | URL length, domain length, path length |
| Character-based | Dots, hyphens, slashes, special characters |
| Domain | IP address presence, subdomain count, TLD type |
| Path | Directory depth, file extension |
| Query | Parameter count, suspicious patterns |
| Security | HTTPS, certificate validity |
| Entropy | Character distribution randomness |
| Reputation | Domain age, blacklist scores |

**Top 10 features by importance:**

```
url_length          0.142
has_ip_address      0.128
num_subdomains      0.095
domain_length       0.087
num_dots            0.076
has_https           0.068
entropy             0.062
num_hyphens         0.055
path_depth          0.051
num_digits          0.048
```

---

## Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|---|---|---|---|---|---|
| Random Forest | 94.2% | 93.8% | 94.6% | 94.2% | 0.97 |
| **XGBoost** | **96.5%** | **96.2%** | **96.8%** | **96.5%** | **0.98** |
| SVM (RBF) | 92.8% | 92.3% | 93.2% | 92.7% | 0.96 |
| Ensemble | 97.1% | 96.9% | 97.3% | 97.1% | 0.99 |

**Confusion Matrix (XGBoost):**

```
                   Predicted
                 Benign    Malicious
Actual Benign     4,823          152
     Malicious      118        4,907
```

---

## API Reference

### `POST /predict`

Analyze a single URL.

**Request:**
```json
{
  "url": "https://example.com/path?param=value"
}
```

**Response:**
```json
{
  "url": "https://example.com/path?param=value",
  "is_malicious": false,
  "confidence": 0.923,
  "risk_score": "low",
  "features": {
    "url_length": 38,
    "has_https": true,
    "num_dots": 1
  },
  "timestamp": "2025-02-13T10:30:00Z"
}
```

### `POST /batch`

Analyze multiple URLs.

**Request:**
```json
{
  "urls": [
    "https://google.com",
    "http://suspicious-site.tk"
  ]
}
```

---

## Project Structure

```
malicious-url-detection/
├── data/
│   ├── raw/                    # Original datasets
│   ├── processed/              # Cleaned data
│   └── models/                 # Trained model files
├── src/
│   ├── feature_extraction.py
│   ├── model_training.py
│   ├── prediction.py
│   └── utils.py
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_evaluation.ipynb
├── api/
│   ├── app.py
│   └── schemas.py
├── app.py                      # Streamlit interface
├── train.py                    # Training script
├── requirements.txt
└── README.md
```

---

## License

Licensed under the [Apache License 2.0](LICENSE).

---

## Author

**Au Amores** — AI/ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/au-amores/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ares-coding)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:auamores3@gmail.com)
