# Scope


This repository contains source code for the classical docking setup, input data processing, result generation, and evaluation on [PLINDER](https://www.plinder.sh/) and [PoseBusters](https://doi.org/10.1039/D3SC04185A) protein-ligand docking benchmarks.

Details: [ArtiDock: Accurate Machine Learning Approach to Protein–Ligand Docking Optimized for High-Throughput Virtual Screening](https://doi.org/10.1021/acs.jcim.5c02777)

# Dataset


The ready-to-use datasets can be downloaded from Zenodo:


- [PLINDER](https://zenodo.org/records/17937766) (`plinder-v2-eval.tar.gz`)
- [PoseBusters](https://zenodo.org/records/8278563) (`posebusters_paper_data.zip`)


# Setup


1. Install [Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install) or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html).


2. Clone the source code and set up the environment.


   ```#!/bin/bash
   git clone https://github.com/receptor-ai/dock-eval.git
   cd dock-eval/
   ```


3. Create environment.


   - AutoDock:


   ```#!/bin/bash
   conda env create --file requirements/autodock/environment.yml
   conda activate autodock
   pip install -r requirements/autodock/requirements.txt --no-cache-dir
   ```
   If you are going to use AutoDock-GPU, it should be installed additionally.
   Run `conda activate autodock && bash requirements/autodock/install_autodock_gpu.sh`.
   The script was tested on a machine with an RTX 3000/4000 Series GPUs and CUDA 12.4 using `nvidia/cuda:12.4.1-devel-ubuntu22.04` Docker image template.
   You may also try `conda install hcc::autodock-gpu`.

   - Glide:


   To use Glide, you should have Schrödinger Suite installed on your machine.
   Locate the path that contains `utilities/prepwizard`, `ligprep`, and `glide` tools required for the docking (e.g., `/home/user/software/schrodinger2024-3/`).


   - Evaluation:


   ```#!/bin/bash
   conda env create --file requirements/eval/environment.yml
   conda activate dock-eval
   pip install -r requirements/eval/requirements.txt --no-cache-dir
   ```


# Usage

- The short custom usage examples of the docking module are available in `examples/docking.ipynb` (`autodock` environment)
- The short custom usage example of the evaluation module is available in `examples/evaluate.ipynb` (`dock-eval` environment)

## Running docking for benchmark


- AutoDock:


   ```#!/bin/bash
   conda activate autodock

   # AutoDock-CPU (AutoDock4) example:
   python -m autodock.plinder_v2 --ds_root ../data/plinder-v2-eval/ --split test --workdir workdir/autodock-cpu/plinder-v2-test --docked_sdf result_1.sdf --grid_size 20 20 20 --type cpu --params ga_num_evals=350000 ga_run=20 --parallel

   # AutoDock-GPU example:
   python -m autodock.plinder_v2 --ds_root ../data/plinder-v2-eval/ --split test --workdir workdir/autodock-gpu/plinder-v2-test --docked_sdf result_1.sdf --grid_size 20 20 20 --type gpu

   # Vina example:
   python -m autodock.plinder_v2 --ds_root ../data/plinder-v2-eval/ --split test --workdir workdir/autodock-vina/plinder-v2-test --docked_sdf result_1.sdf --grid_size 20 20 20 --type vina --params exhaustiveness=16
   ```


- Glide:


   ```#!/bin/bash
   export SCHRODINGER="/home/user/software/schrodinger2024-3/"

   # only basic dependencies are needed, so we can use the already installed dock-eval
   conda activate dock-eval

   python -m glide.plinder_v2 --ds_root ../data/plinder-v2-eval/ --split test --workdir workdir/glide/plinder-v2-test --docked_sdf result_1.sdf --outerbox 20 20 20 --dock_params POSTDOCK_NPOSE=80 --parallel
   ```


These examples will launch docking on the PLINDER test dataset (holo) and save results to `--workdir`.
To launch docking on the PLINDER MLSB test dataset (undound), change `--split` to `test-mlsb` and provide another `--workdir`.
To launch docking on the PoseBusters dataset, use the corresponding `posebusters.py` scripts, remove `--split` argument, and provide the `--ds_root` folder with complexes (e.g., `python -m autodock.posebusters --ds_root ../data/posebusters_benchmark_set/ --workdir workdir/autodock-cpu/posebusters/ --docked_sdf result_1.sdf --grid_size 25 25 25 --type cpu --parallel`).


## Running evaluation for benchmark


To evaluate the docking performance, use the same `--ds_root`, `--split` (for PLINDER), `--workdir`, and `--docked_sdf` arguments as for a docking launch. Example for AutoDock-CPU evaluation:


```#!/bin/bash
conda activate dock-eval

python -m eval.plinder_v2 --ds_root ../data/plinder-v2-eval/ --split test --workdir workdir/autodock-cpu/plinder-v2-test --docked_sdf result_1.sdf --parallel
```

# TODO
- Virtual screening mode for docking
- Unit tests
