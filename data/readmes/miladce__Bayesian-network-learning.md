# Bayesian Network Structure Learning
This project demonstrates Bayesian Network structure learning using the Nursery dataset from the UCI Machine Learning Repository.
It compares different scoring methods for learning Bayesian network structures from sampled data, including:

- MDL / BIC
- AIC
- BDeu

The project also evaluates the learned structures against a predefined gold standard network using several structural metrics.

### Evaluation Metrics

The learned networks are evaluated against the gold standard network using:
- TP — True Positives
- TN — True Negatives
- FP — False Positives
- FN — False Negatives
- Accuracy
- Sensitivity
- AHD — Average Hamming Distance
- SHD — Structural Hamming Distance

##

### installation
for installing project dependencies via pip:
```
pip install /path/to/reqs.txt
```

##

### Notes
- The project uses Hill Climbing Search for Bayesian network structure learning.
- Different sample sizes are tested to study their impact on structure recovery.
- The `AICScore` implementation extends `pgmpy.estimators.StructureScore.` is a custom implementation of the Akaike Information Criterion (AIC) scoring function for pgmpy.
##
- **Dataset:** The project uses the [[UCI Nursery Dataset]](https://archive.ics.uci.edu/ml/datasets/nursery)
- rendered notebook is available [here](https://nbviewer.jupyter.org/github/miladce/Bayesian-network-learning/blob/master/main.ipynb)
