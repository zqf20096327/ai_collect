# Automatic Recycling Bin

A research project that tackles waste sorting as a statistical classification problem, using Machine Learning and Deep Learning to build predictive models and real-world applications.

## Overview

This project explores how Data Science can improve resource utilization through automated waste classification. It addresses two research questions:

1. How can waste sorting be analyzed as a statistical classification problem?
2. What applications can be implemented using predictive models?

## Data Collection

Three strategies were used to gather training data:

- **Web Scraping** — HTML Parsing to collect 41,042 images across 129 categories
- **Telegram Chatbot** — A bot that receives and stores user-submitted waste photos (1,348 images)
- **Arduino-based Bin** — A custom-built bin with sensors to record structured data about waste items (weight, transparency, conductivity, etc.)

## Models

### Structured Data
- **Gradient Boosting Machine (GBM)** — 96% accuracy
- **Multi-Layer Perceptron (MLP)** — 84% accuracy

### Unstructured Data (Images)
- **ResNet (variant 1)** — 85% accuracy
- **ResNet (variant 2)** — 79% accuracy

### Ensemble Learning
Models were combined via Stacking to achieve higher performance:
- **Ensemble 1** — 92% accuracy
- **Ensemble 2** — 95% accuracy

## Applications

1. **Telegram Bot** — Receives a photo and returns the predicted waste category
2. **Automatic Recycling Bin** — A physical bin that sorts waste automatically using the trained models

## Project Structure

```
├── index.html                   # Project webpage
├── TESI_SACCAGGI_GIACOMO.pdf    # Full research paper (Italian)
├── video.mp4                    # Demo video
└── README.md
```

## Technologies

- Python, Arduino
- Deep Learning (ResNet, CNN)
- Machine Learning (GBM, MLP, Ensemble/Stacking)
- Web Scraping, Telegram Bot API
- GoJS, Highcharts (visualization)

## License

Copyright © Giacomo Saccaggi
