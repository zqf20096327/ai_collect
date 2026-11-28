# Neural Network Circuit Game

[![Download](https://img.shields.io/github/v/release/luangrezende/neural-network-circuit-game?label=Download%20Windows%20EXE&style=for-the-badge&logo=github&color=2ea043)](https://github.com/luangrezende/neural-network-circuit-game/releases/latest)

Watch 80 cars learn to drive a track you draw, evolved by a
[genetic algorithm](https://en.wikipedia.org/wiki/Neuroevolution) in about 2,000 lines of Python and NumPy, with no
deep-learning framework.

Each generation, the whole population drives the circuit at once. Every car is a small neural network reading seven
distance sensors; the best drivers survive, are crossed and mutated, and the next generation tries again. No
backpropagation: the weights only change through evolution. It runs in real time in a Matplotlib window, with live
charts of the learning curve.

**Status:** hobby project (v1.1.0, November 2026), maintained when I have time. It runs from source on Python 3.11+ and as a Windows
executable; [issues](https://github.com/luangrezende/neural-network-circuit-game/issues) are welcome.
[MIT licensed](LICENSE).

## Why not NEAT-Python or ML-Agents?

[NEAT-Python](https://github.com/CodeReclaimers/neat-python) evolves the network's shape as well as its weights, and
[Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) trains agents with reinforcement learning inside
a game engine. Use them for real projects. This one is meant to be read: a fixed 8-14-2 network, a plain genetic
loop, physics and collision in NumPy, all small enough to follow in an afternoon, plus an editor to draw your own
tracks.

## Getting started

### Windows executable

Download the latest `.zip` from [Releases](https://github.com/luangrezende/neural-network-circuit-game/releases/latest),
extract it and run `neural-network-circuit-game.exe`. No Python needed. The executable is not code-signed, so
Windows SmartScreen may ask you to confirm.

### From source

Python 3.11 or newer:

```bash
git clone https://github.com/luangrezende/neural-network-circuit-game.git
cd neural-network-circuit-game
python -m venv .venv
.venv\Scripts\activate        # Linux / macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Press `Q` or close the window to stop. Training ends when a car completes 10 laps. Run from source, it then saves the
winning network's weights, the generation and the best lap time to `resultados.json`.

### Draw your own track

```bash
python track_editor.py
```

Click to place control points, set the track width with the slider, and save. The start line sits between the first
two points. The editor writes `track.json`, and the simulator uses it on the next run.

## The neural network

```
8 inputs (7 distance sensors + speed)
        ↓
   14 hidden units  (sigmoid)
        ↓
 2 outputs: steer (-1..+1), throttle (0..1)  (sigmoid)
```

Weights evolve each generation through uniform crossover and Gaussian mutation. Population size, rewards,
penalties and car physics are all in `config.json`; the keys, the code layout and how the executable is built are in
[docs/development.md](docs/development.md).

## License

[MIT](LICENSE).
