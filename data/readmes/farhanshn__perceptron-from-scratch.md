# Perceptron from Scratch

Learning project: implementing the perceptron algorithm in pure Python,
then comparing it with scikit-learn's implementation.

## How it works
For each sample: z = w1*x1 + w2*x2 + b, predict 1 if z >= 0, else 0.

Update rule: w += learning_rate * (y - prediction) * x

## Contents
- `final_perceptron.ipynb`: training from scratch, decision boundary plot, and comparison with scikit-learn

## Run
pip install numpy matplotlib scikit-learn jupyter
jupyter notebook
