# Decoding Digit Sequences in Real-World Photos (TensorFlow, SVHN)

A [TensorFlow](https://www.tensorflow.org/) implementation of a
[convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
that reads multi-digit sequences, such as house numbers, from real-world photos. It is trained on the
[SVHN dataset](http://ufldl.stanford.edu/housenumbers/).

> Built in 2016 as the capstone project for the Udacity Machine Learning Nanodegree.
> The code targets Python 2.7 and early TensorFlow 1.x APIs and is kept here as-is for reference.
> The full write-up is in [`capstone report final.pdf`](capstone%20report%20final.pdf).

## Installation
```
git clone https://github.com/bdiesel/tensorflow-svhn.git
cd tensorflow-svhn
```

## Libraries and dependencies
The project needs these Python 2.7 libraries:
* h5py
* matplotlib
* numpy
* PIL
* tensorflow
* scipy
* six
* sklearn

## Step 1: Download and preprocess the SVHN data
Download and preprocess the SVHN data with the `svhn_data.py` utility:

`python svhn_data.py`

This creates a `data/svhn` folder with two subdirectories, `cropped` and `full`.

The `cropped` directory contains 2 downloaded .mat files and 6 NumPy files for each dataset, which are used for training.

The `full` directory contains two subdirectories, `test` and `full`, with PNG images of various sizes. It also contains 6 NumPy files and 3 tar.gz files. You can delete the tar.gz files to free up disk space.

## Step 2: Train your own models
First train the classifier. The weights it produces are reused to train the multi-digit reader. This step can take a while, depending on your hardware. Pre-trained weights are available for the [single-digit reader](https://s3.amazonaws.com/tensorflow-weights/classifier.ckpt) and the [multi-digit reader](https://s3.amazonaws.com/tensorflow-weights/regression.ckpt).

`python train_classifier.py`

This produces a TensorFlow checkpoint file:

`classifier.ckpt`

Next, train the multi-digit reader:

`python train_regressor.py`

This produces a TensorFlow checkpoint file:

`regression.ckpt`

## Step 3: Check model performance
The training scripts write logs that you can open in TensorBoard to inspect the models' performance over time.

To view single-digit performance after running `train_classifier.py`:

`tensorboard --logdir="/tmp/svhn_classifier_logs"`

To view multi-digit performance after running `train_regressor.py`:

`tensorboard --logdir="/tmp/svhn_regression_logs"`

## Usage

Single-digit reader, for an image file `1.png`: `python single_digit_reader.py 1.png`

Multi-digit reader, for an image file `123.png`: `python multi_digit_reader.py 123.png`
