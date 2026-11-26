# from-scratch-neural-networks

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/from-scratch-neural-networks)](https://github.com/smartlegionlab/from-scratch-neural-networks/releases)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/from-scratch-neural-networks)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/from-scratch-neural-networks)](https://github.com/smartlegionlab/from-scratch-neural-networks/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/from-scratch-neural-networks?style=social)](https://github.com/smartlegionlab/from-scratch-neural-networks/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/from-scratch-neural-networks?style=social)](https://github.com/smartlegionlab/from-scratch-neural-networks/network/members)

![Neural Network](https://img.shields.io/badge/neural%20network-MLP-00d2ff)
![From Scratch](https://img.shields.io/badge/from%20scratch-100%25-4fc3f7)
![Pure JavaScript](https://img.shields.io/badge/pure%20JavaScript-ES6-f7df1e)
![No Frameworks](https://img.shields.io/badge/no%20frameworks-yes-00e676)
![Backprop](https://img.shields.io/badge/backpropagation-momentum%20%2F%20Adam-ff5252)
![SGD / Adam](https://img.shields.io/badge/optimizers-SGD%20%2F%20Adam-ff7043)
![Live Visualization](https://img.shields.io/badge/live%20visualization-orbs%20%2B%20graphs-b388ff)
![Model Export](https://img.shields.io/badge/model-export%20%2F%20import-00c853)

A collection of real multilayer perceptrons (MLPs) implemented **from scratch in pure JavaScript**. No frameworks, no external libraries, no runtime dependencies. Each app is a self-contained single HTML file that trains and runs a neural network entirely in the browser, with live visualization of the learning process.

---

## Overview

This repository contains four independent, ready-to-run applications. Each one implements a complete training pipeline by hand: the forward pass, error backpropagation, and weight updates with gradient descent. Everything runs client-side, so no server or build step is required.

The apps are designed as an educational demonstration: they show, in real time, how a small network reorganizes its weights to solve a specific problem. All values rendered on screen correspond to the actual state of the network.

---

## Feature summary

- **Networks trained from scratch** in plain JavaScript (sigmoid activation, backpropagation, mini-batch SGD; the Boolean app also offers Adam as an optimizer).
- **Interactive input** - draw, type, or flip values and watch predictions update live.
- **Live visualization** - neurons are rendered as pulsing orbs whose brightness reflects activation; synapse lines show the sign and relative magnitude of weights; loss graphs and decision maps reflect the real training dynamics.
- **Model persistence** - every app can export its trained weights to a JSON file and import them back, so trained models can be saved, shared, or reused without retraining.
- **Responsive layout** - the interfaces adapt for desktop, tablet, and mobile, including touch drawing.
- **Built-in Help and About dialogs** in every application.

---

## Applications

| # | File (repo)                                                                              | Live demo                                                                                        | App                                          | Network        | Learns                       |
|---|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------|----------------|------------------------------|
| 1 | [logic-gates-neural-network.html](logic-gates-neural-network.html)                       | [try it](https://smartlegionlab.github.io/interctive/logic-gates-neural-network.html)            | Boolean-Logic Neural Network                 | 2 → 3 → 1      | XOR / AND / OR / NAND / XNOR |
| 2 | [digit-recognition-neural-network.html](digit-recognition-neural-network.html)           | [try it](https://smartlegionlab.github.io/interctive/digit-recognition-neural-network.html)      | Handwritten-Digit Recognition Neural Network | 144 → 24 → 10  | Handwritten digits 0–9       |
| 3 | [x-o-recognition-neural-network.html](x-o-recognition-neural-network.html)               | [try it](https://smartlegionlab.github.io/interctive/x-o-recognition-neural-network.html)        | X / O Shape Recognition Neural Network       | 64 → 12 → 2    | The letters X and O          |
| 4 | [name-gender-classifier-neural-network.html](name-gender-classifier-neural-network.html) | [try it](https://smartlegionlab.github.io/interctive/name-gender-classifier-neural-network.html) | Name Gender Classifier Neural Network        | 2,746 → 48 → 1 | Gender from RU/EN names      |

---

## Screenshots

![Handwritten-Digit Recognition Neural Network](https://raw.githubusercontent.com/smartlegionlab/from-scratch-neural-networks/master/data/images/digit-recognition-neural-network.png)

![Boolean-Logic Neural Network](https://raw.githubusercontent.com/smartlegionlab/from-scratch-neural-networks/master/data/images/logic-gates-neural-network.png)

![Name Gender Classifier Neural Network](https://raw.githubusercontent.com/smartlegionlab/from-scratch-neural-networks/master/data/images/name-gender-classifier-neural-network.png)

![X / O Shape Recognition Neural Network](https://raw.githubusercontent.com/smartlegionlab/from-scratch-neural-networks/master/data/images/x-o-recognition-neural-network.png)

---

## Getting started

### Run locally

Every application is a single HTML file that runs entirely in the browser - **a web server is not required**.

- **Double-click:** open the downloaded HTML file directly in any modern browser.
- **Static server (optional):** if you prefer, serve the folder, for example:
  ```bash
  python -m http.server 8000
  ```
  then open `http://localhost:8000` in a browser and pick the HTML file.

No build step, no package manager, and no internet connection is required - everything runs 100% client-side.

The published demos for this project currently live under the `interctive/` path, with an index of all demonstrations at [interctive/index.html](https://smartlegionlab.github.io/interactive.html).

---

## Applications in detail

### 1. Boolean-Logic Neural Network - `logic-gates-neural-network.html`

A small **2 → 3 → 1** network that learns classic logic gates. It is a good introduction to why a hidden layer is necessary: a single-layer perceptron cannot learn XOR, because its two "true" inputs sit diagonally and cannot be separated by a straight line.

**How to use:**

1. Choose a logic function: **XOR, AND, OR, NAND or XNOR**. Switching a function resets the network, so each gate trains from zero.
2. Flip the **a** and **b** inputs (switches, or by clicking the input neurons in the network view). The answer is shown in green when correct and red when wrong, together with a confidence bar.
3. Press **Start Training** or **Fast Learn → 100%**. Training stops automatically once all 4 of 4 cases are correct, which keeps the result stable.
4. Optionally adjust the **learning rate** (Precise by default) and choose the **optimizer** (**SGD + momentum** by default, or **Adam**).
5. Use **Export / Import** to save or load the trained brain as a JSON file.

The right-hand panel shows a **decision map**: every pixel of the input space is fed through the network and colored by its output, so you can watch the boundary reshape as the network learns.

### 2. Handwritten-Digit Recognition Neural Network - `digit-recognition-neural-network.html`

A **144 → 24 → 10** network (12×12 grayscale input grid → 24 hidden neurons → 10 outputs) that recognizes the digits 0–9. Training uses mini-batch SGD with momentum and exact MSE backpropagation.

**How to use:**

1. Draw a digit **0–9** on the grid with the mouse, finger, or stylus. Strokes are smoothed and anti-aliased.
2. Tap the matching digit below - it becomes the active **label**.
3. Press **✓ Save** to add the sample to the dataset (the grid clears automatically).
4. Erase mistakes with the **Eraser** button, the **E** key, or by holding the **right mouse button**.
5. Press **Auto-gen** to add 250 hand-styled samples (25 per digit) generated with random rotation, scale, shear, offset, bends, wobble, pen-lift gaps, and variable stroke thickness.
6. Press **Start Training** or **Fast Learn**. The **Acc** figure shows the percentage of the dataset answered correctly in real time.

While training, the network shows its guess for whatever is currently drawn, along with a confidence bar and per-class percentages.

### 3. X / O Shape Recognition Neural Network - `x-o-recognition-neural-network.html`

A minimal **64 → 12 → 2** dense network that learns to distinguish the letters **X** and **O** drawn on an 8×8 grid. It is a clear starting point for understanding image-style classification with a plain dense network.

**How to use:**

1. Draw the letter **X** on the 8×8 grid.
2. Press **+ This is X** to save it (the grid clears automatically).
3. Draw the letter **O** (a ring near the edges of the cells).
4. Press **+ This is O**.
5. Repeat **3–5 times per letter**, varying size and position - more varied samples improve accuracy.
6. Press **Start Training** and watch the loss graph go down.
7. Draw a new X or O at any time - the network replies instantly with a guess and a confidence percentage.

You can keep drawing while training runs; predictions update live.

### 4. Name Gender Classifier Neural Network - `name-gender-classifier-neural-network.html`

A **2,746 → 48 → 1** network that guesses gender from names written in **Russian, English, or transliteration**. Names are normalized to a single 27-letter Latin alphabet and converted into sparse features: letter positions, reversed positions, first letter, final bigram/trigram, patronymic bigram/trigram, length bucket, vowel/consonant buckets, and diminutive markers. About 700 names are included in the dataset.

**How to use:**

1. Press **Start Training** - the built-in name dataset is loaded automatically.
2. Type a name in Russian, English, or translit (for example **Александра**, **Анна Сергеевна**, or **Alexander**).
3. Add your own names with **+ Is Female** / **+ Is Male**.
4. **Resplit** reshuffles the 80/20 train/validation split; the loss graph shows loss (green), train accuracy (blue), and validation accuracy (orange).
5. Keep a name in the input for about one second to record it in the **Guess History**. Known names are marked OK/WRONG automatically; for unknown ones you mark them yourself.
6. Use **Export / Import** to save or load the trained brain as a JSON file.

The input orbs indicate **connection strength**: the brighter a letter or suffix, the more the network relies on that feature for its answer.

---

## Model export and import

Every application includes **Export** and **Import** buttons in its network panel:

- **Export** downloads the current network weights (and associated settings) as a JSON file.
- **Import** loads such a file and applies the weights to the network, so a trained brain can be restored or shared without retraining.

---

## License

This project is licensed under the **BSD 3-Clause License** - see [LICENSE](LICENSE).

---

**Author:** Alexander Suvorov · **Repository:** [github.com/smartlegionlab/from-scratch-neural-networks](https://github.com/smartlegionlab/from-scratch-neural-networks)

