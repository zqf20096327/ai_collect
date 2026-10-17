# Privacy-Preserving Federated Learning for Chest X-Ray Diagnosis

A federated learning framework that enables multiple hospitals to collaboratively train a chest X-ray diagnosis model **without sharing patient data**.

Instead of transferring sensitive medical images to a central server, each hospital trains locally on its own dataset and shares only model updates. These updates are aggregated into a global model using **Federated Averaging (FedAvg)**, allowing institutions to benefit from collective learning while preserving patient privacy.

---

## 📌 Problem Statement

Medical AI systems perform better when trained on large and diverse datasets. However, hospitals cannot freely exchange patient records due to privacy regulations, ethical concerns, and institutional policies.

As a result:

- Hospitals often train models in isolation.
- Valuable medical knowledge remains siloed.
- Collaborative AI development becomes difficult.
- Patient privacy remains a major concern.

This project addresses these challenges by enabling collaborative model training while ensuring patient data never leaves the hospital where it was collected.

---

## Key Features

### Federated Learning

- Flower-based federated learning framework
- Distributed training across multiple hospital nodes
- FedAvg aggregation strategy
- Local model training at each institution

###  Differential Privacy

- Implemented using Opacus
- Per-sample gradient clipping
- Noise injection before parameter sharing
- Privacy budget (ε) tracking across training rounds

###  DenseNet121 Transfer Learning

- ImageNet-pretrained DenseNet121
- Fine-tuning on chest X-ray data
- Efficient learning using transfer learning techniques

###  Byzantine Detection Support

- Aggregation-level anomaly detection hooks
- Support for identifying suspicious model updates
- Protection against model poisoning attempts

###  Model Checkpointing

- Global model checkpoint storage
- Round-wise model tracking
- Resume training support

###  Dashboard Support

Provides APIs for:

- Node status monitoring
- Training round tracking
- Accuracy visualization
- Privacy budget monitoring
- System logs and metrics

---

##  System Architecture

### Hospital Nodes

Each hospital node contains:

- Local PadChest dataset partition
- DenseNet121 training pipeline
- Differential Privacy module
- Flower client
- FastAPI service
- Diagnosis interface

### Central Aggregator

The aggregator is responsible for:

- Coordinating federated learning rounds
- Receiving model updates
- Running FedAvg aggregation
- Tracking privacy budget consumption
- Logging training metrics
- Managing global checkpoints

### Dashboard Layer

The dashboard visualizes:

- Hospital node status
- Training progress
- Model accuracy
- Privacy budget usage
- Round history
- Security alerts

---

## Scalability and further enhancements 


###  Diagnosis Service

- Upload chest X-ray images
- Run inference using the latest global model
- Local diagnosis workflow

---

##  Federated Learning Workflow

```text
Hospital A
      \
Hospital B ----> Aggregator ----> Global Model
      /
Hospital C
```

### Training Cycle

1. Hospital nodes receive the latest global model.
2. Each hospital trains locally on its own X-ray dataset.
3. Differential Privacy is applied during training.
4. Model weights are sent to the aggregator.
5. FedAvg combines updates into a new global model.
6. Metrics and privacy statistics are recorded.
7. The updated model is redistributed to all nodes.
8. The cycle repeats until convergence.

> **Patient images never leave their originating hospital.**

---

## 📂 Repository Structure

```text
Koffee_with_Kode/

├── dataprep/
│   ├── dataprep.py
│   └── dataprep.txt
│
├── fl_framework/
│   ├── aggregator_api.py
│   ├── client.py
│   ├── config.py
│   ├── dataset.py
│   ├── model_utils.py
│   ├── node_api.py
│   ├── run_local_simulation.py
│   ├── server.py
│   ├── strategy.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

---

##  Technology Stack

### Federated Learning

- Flower
- FedAvg

### Machine Learning

- PyTorch
- DenseNet121
- Transfer Learning

### Privacy

- Opacus
- Differential Privacy

### Backend

- FastAPI
- Python

### Dataset

- PadChest Chest X-Ray Dataset

### Networking

- Ngrok
- gRPC

---

##  API Endpoints

### Aggregator API

| Endpoint | Description |
|-----------|-------------|
| `/global_model` | Latest global model weights |
| `/round_status` | Current training round information |
| `/privacy_budget` | Privacy budget tracking |
| `/accuracy` | Accuracy and loss history |
| `/diagnose` | Global model inference |

### Hospital Node API

| Endpoint | Description |
|-----------|-------------|
| `/status` | Node status |
| `/metrics` | Training metrics |
| `/train` | Trigger local training |
| `/diagnose` | Diagnose uploaded X-ray |
| `/` | Local upload interface |

---

## Configuration

Most system parameters can be configured through:

```text
fl_framework/config.py
```

Configuration includes:

- Aggregator address
- Number of federated rounds
- Client requirements
- Dataset locations
- Disease labels
- Differential Privacy parameters
- Learning rate
- Batch size
- Checkpoint settings

---

##  Running the Project

### Install Dependencies

```bash
pip install -r fl_framework/requirements.txt
```

---

### Run Local Simulation

```bash
python fl_framework/run_local_simulation.py
```

This simulates multiple federated clients on a single machine.

---

### Start Aggregator

```bash
python fl_framework/aggregator_api.py
```

or

```bash
uvicorn fl_framework.aggregator_api:app --host 0.0.0.0 --port 8000
```

---

### Start Hospital Nodes

```bash
python fl_framework/node_api.py --node-id node_1
```

```bash
python fl_framework/node_api.py --node-id node_2
```

```bash
python fl_framework/node_api.py --node-id node_3
```

---

##  Model Details

### Base Model

**DenseNet121** (ImageNet Pretrained)

### Fine-Tuned Components

- `denseblock4`
- `norm5`
- `classifier`

### Dataset

**PadChest Chest X-Ray Dataset**
- https://www.kaggle.com/datasets/seoyunje/padchest-small-dataset

### Classification Type

Multi-label classification

Current configured disease labels:

- Pulmonary Fibrosis
- Scoliosis
- Emphysema

### Results

![Confusion Matrix](results/confusion_matrices.png)
![ROC Curve](results/roc_curves.png)
![Loss Graph](results/training_curves.png)
---

##  Dashboard Features

### Central Dashboard

- Hospital node monitoring
- Federated training rounds
- Global accuracy tracking
- Privacy budget visualization
- Live logs
- Training progress indicators

### Hospital Interface

- X-ray upload
- Diagnosis results
- Node status
- Global model version

---

##  Future Improvements

- Production-grade Byzantine detection
- Larger federated deployments
- Additional disease classes
- Enhanced dashboard analytics
- Secure aggregation support
- Expanded medical imaging tasks

---

##  Project Goal

The core idea behind this project is simple:

> **Patient data stays local, while the knowledge gained from that data becomes global.**

By combining Federated Learning, Differential Privacy, and collaborative training, this system enables hospitals to improve diagnostic AI models without compromising patient privacy.

---

## 👥 Team

**Koffee_with_Kode**

SC guiding-Antara 

Anika, Annika, Bhakti, Mohit

Built for privacy-preserving collaborative healthcare AI.
