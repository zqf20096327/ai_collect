# convoca

Demonstrate and learn cellular automata using convolutional neural networks in PyTorch

![Game of Life training stages](demos/glider_stages.gif)

The video above shows different stages of training a network to learn Conway's Game of Life. 
This code both implements and analyzes known CA rulesets using PyTorch, and it also learns the rules of unknown CA given an image sequence as training data.
If you find this code useful, please consider citing the accompanying publication:

> Gilpin, William. "Cellular automata as convolutional neural networks." Physical Review E 100.3 (2019): 032402. [arXiv](https://arxiv.org/abs/1809.02942)

## Demos and features

The `demos/demos.ipynb` illustrates a minimal example of training a CNN on the Game of Life, including example outputs.
Models are instantiated using the `initialize_model(...)` function, which builds a network with a trainable convolutional filter as the first layer, which serves to extract information about the neighborhood of each cell. Repeated 1x1 convolutions in subsequent layers implement the CA rules, and a final softmax layer assigns an output state to each cell.
For cases in which the CA ruleset is radially symmetric, the optional `SymmetricConvolution` layer imposes radially-symmetric structure on the learned convolutional kernels, which is often the case for natural systems with "totalistic" rules. An optional `Wraparound2D` layer also allows periodic boundary conditions to be implemented in the convolutions.

## Installation and Requirements

Install and run with [`uv`](https://docs.astral.sh/uv/):

	uv sync
	uv run pytest
	uv run convoca-benchmark

+ Python >=3.10
+ PyTorch >=2.2
+ numpy
+ matplotlib
+ Jupyter notebooks (for demos: `uv sync --extra notebook`)

## Structure

The `convoca` package contains the following modules

`convoca.train_ca` : requires PyTorch

`convoca.ca_funcs` : requires PyTorch

`convoca.benchmark` : simulation, training, and inference benchmarks (`uv run convoca-benchmark`)

`convoca.utils` : minor functions that support the main methods. Requires numpy only.

`demos/demos.ipynb` : demonstration of the code for learning the game of life


## Updates

As of 2.26.2020, the code has been significantly re-factored to use Tensorflow 2.0 and Keras.  The previous implementation has been placed in the "resources" directory, for reference.

## Planned future work

+ Add methods for simulating totalistic CA
+ Add methods for Moore neighborhood CA
+ Add demos recreating classic experiments, such as the results in Langton. Physica D, 1990.
+ Add statistical physics calculations such as an efficient calculation of "activity" for a CA
+ CA on graphs using an adjacency matrix --> grid convolutional operator