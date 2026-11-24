<div align="center">

# Neural Dino

**Neural networks that teach themselves to play the Chrome dinosaur game through neuroevolution.**

[![Play in the browser](https://img.shields.io/badge/Play-in%20the%20browser-3d7a4f?style=for-the-badge&labelColor=262624)](https://samuelpedroso-dev.github.io/neural-dino/)
![Zero dependencies](https://img.shields.io/badge/dependencies-zero-c9d1d9?style=for-the-badge&labelColor=262624)
![License](https://img.shields.io/badge/license-MIT-c9d1d9?style=for-the-badge&labelColor=262624)

![Neural Dino training](preview.png)

</div>

## Overview

Dozens of dinosaurs start knowing nothing and learn to play on their own. Whoever crashes is out, and the best ones pass their genes on with small mutations, so the population gets smarter every generation. It was one of the first neural networks I built, as a study project in machine learning.

## How it works

Each dinosaur has a small neural network with 8 inputs, 10 hidden neurons and 2 outputs.

| inputs, what the network sees | outputs, what it decides |
|---|---|
| distance to the next obstacle | jump |
| width, top and bottom of its hitbox | duck |
| game speed | |
| the dinosaur's own height and vertical speed | |
| distance to the obstacle after that | |

There is no training data and no gradient. Learning happens through **neuroevolution**, a genetic algorithm applied to the network weights.

1. The whole population runs the same course at the same time
2. Each dinosaur's fitness is the distance it covers
3. The best ones go straight to the next generation (elitism)
4. The rest are born from parents chosen by tournament, with crossover and Gaussian mutation on the weights
5. A small share of the population is always new and random, to keep diversity

## The challenge of learning to duck

In the original game ducking is never required, because every pterodactyl can be jumped over. The AI learned to jump and never discovered the other button.

To fix that I added flocks of pterodactyls that cover the screen from ground to sky and can only be passed by ducking. When the flocks appeared only mid run, the population got stuck in a local optimum around 400 points, because it already had the habit of jumping over everything. Making the flocks appear from the start lets the AI learn both skills together, and it reaches 100,000 points within a few dozen generations.

## Features

* Live training from 1x up to Turbo speed
* The leader's neural network visualized while it thinks, in real time
* Best and average score per generation
* Watch the champion play alone, or play yourself
* Export and import the champion's weights to continue training later

## Run it

Everything is plain HTML, CSS and JavaScript in a single file, with no libraries. Open the [live version](https://samuelpedroso-dev.github.io/neural-dino/) or clone the repository and open `index.html`.

## License

MIT. See [LICENSE](LICENSE).

Built by [Samuel Pedroso](https://github.com/Samuelpedroso-dev) · [LinkedIn](https://linkedin.com/in/samuelpedroso)
