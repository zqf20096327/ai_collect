# Real-Time Network Anomaly Detection System

A production-ready framework for monitoring network traffic and identifying anomalous patterns using an ensemble of unsupervised machine learning techniques. This system leverages both traditional statistical partitioning and modern neural network reconstruction to detect threats such as DDoS attacks, brute-force attempts, and data exfiltration.

## Features

- **Ensemble Detection Architecture**: Combines Scikit-learn's Isolation Forest with a PyTorch-based Autoencoder for dual-layered anomaly verification.
- **RESTful Inference API**: A high-speed FastAPI backend that serves model predictions with low latency and robust error handling.
- **Interactive Monitoring Dashboard**: A Streamlit interface for real-time visualization of network health, anomaly scores, and event logs.
- **Synthetic Traffic Simulation**: Includes a data generator designed to simulate both standard network activity and common cybersecurity attack vectors.
- **Modular Data Pipeline**: Automated feature engineering and scaling for IP frequency, login failure ratios, session durations, and packet statistics.

## Project Structure

```text
/Real-time Network Anomaly Detection System/
├── api/                # FastAPI backend server
├── dashboard/          # Streamlit monitoring dashboard
├── data/               # Synthetic data generation and storage
├── models/             # Machine Learning model implementations and artifacts
├── utils/              # Feature engineering and preprocessing utilities
├── train.py            # Model training and persistence script
├── main.py             # Project entry point and configuration guide
└── requirements.txt    # Python dependency manifest
```

## System Requirements

- Python 3.8 or higher
- PyTorch
- Scikit-learn
- FastAPI / Uvicorn
- Streamlit

## Setup and Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Models**:
   Run the training script to generate the initial synthetic dataset and train the ensemble models.
   ```bash
   python train.py
   ```

3. **Launch Inference API**:
   Start the FastAPI server to handle incoming prediction requests.
   ```bash
   uvicorn api.server:app --reload
   ```

4. **Launch Monitoring Dashboard**:
   Open a separate session to run the visualization layer.
   ```bash
   streamlit run dashboard/app.py
   ```

## Technical Implementation

### Feature Engineering
The system extracts and normalizes five primary network features:
- IP frequency over a sliding window
- Failed login ratio
- Session duration
- Average packet size
- Request rate per second

### Anomaly Scoring
- **Isolation Forest**: Identifies rare events by isolating them with binary partitions.
- **Autoencoder**: Learns the latent representation of "normal" data and flags events with high reconstruction loss relative to a calibrated threshold.

## License
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.

## Author
Au Amores - AI/ML Engineer
