# MSGNN
MSGNN: A Spectral Graph Neural Network Based on a Novel Magnetic Signed Laplacian (LoG 2022)

For details, please read [our paper](https://arxiv.org/pdf/2209.00546.pdf). You are also welcome to read our [poster](https://github.com/SherylHYX/MSGNN/blob/main/LoG2022_MSGNN_poster.pdf).

MSGNN is also implemented in the [PyTorch Geometric Signed Directed](https://github.com/SherylHYX/pytorch_geometric_signed_directed) library.

**Citing**


If you find MSGNN useful in your research, please consider adding the following citation:

```bibtex
@inproceedings{he2022msgnn,
  title={MSGNN: A Spectral Graph Neural Network Based on a Novel Magnetic Signed Laplacian},
  author={He, Yixuan and Perlmutter, Michael and Reinert, Gesine and Cucuringu, Mihai},
  booktitle={Learning on Graphs Conference},
  pages={40--1},
  year={2022},
  organization={PMLR}
}
```

--------------------------------------------------------------------------------

## Environment Setup
### Overview
<!-- The underlying project environment composes of following componenets: -->
The current implementation requires Python >= 3.10, PyTorch >= 2.4, and
PyG >= 2.6. Its current CPU reference environment uses Python 3.11,
PyTorch 2.11.0, PyG 2.8.0, and PyGSD 1.2.0. Install PyTorch and PyG using
their platform-specific instructions before installing the remaining packages.

A minimal reference package set is:
```
python                          3.11
torch                           2.11.0
torch-geometric                 2.8.0
torch-geometric-signed-directed 1.2.0
networkx                        >=2.7
numpy
scipy
scikit-learn
tensorboard
```

## Folder structure
- ./execution/ stores files that can be executed to generate outputs. For vast number of experiments, we use [parallel](https://www.gnu.org/software/parallel/), which can be downloaded in command line and make it executable via:
```
wget http://git.savannah.gnu.org/cgit/parallel.git/plain/src/parallel
chmod 755 ./parallel
```

- ./joblog/ stores job logs from parallel. 
You might need to create it by 
```
mkdir joblog
```

- ./Output/ stores raw outputs (ignored by Git) from parallel.
You might need to create it by 
```
mkdir Output
```

- ./data/ stores processed data sets.

- ./src/ stores files to train various models, utils and metrics.

- ./*_results/ stores results for different data sets.

## Options
<p align="justify">
MSGNN provides the following command line arguments, which can be viewed in the ./src/parser_node.py for the node clustering tasks and ./src/parser_link.py for the link prediction tasks.
</p>

## Reproduce results
First, get into the ./execution/ folder:
```
cd execution
```
To reproduce all results for MSGNN on GPU 0 (group a):
```
bash a0.sh
```
Other execution files are similar to run.

Note that if you are operating on CPU, you may delete the commands ``CUDA_VISIBLE_DEVICES=xx". You can also set you own number of parallel jobs, not necessarily following the j numbers in the .sh files.

You can also use CPU for training if you add ``--cpu".

## Direct execution with training files

First, get into the ./src/ folder:
```
cd src
```
Then, below are various options to try:

Creating an MSGNN model for SDSBM on the node clustering task of the default setting on the 3c data set (remeber to specify a data set name).
```
python ./main_SDSBM_node.py --dataset 3c --weighted_input_feat --sd_input_feat
```
Creating a model for the FiLL-pvCLCL data set in the year 2010 on the link prediction task 4C with some custom learning rate and epoch number, for the SigMaNet method.
```
python ./main_signed_directed_link.py --dataset pvCLCL --year 2010 --lr 0.001 --epochs 300 --num_classes 4 --method SigMaNet --weighted_input_feat --sd_input_feat
```
Creating a model for the FiLL-OPCL data set in the year 2016 on the link prediction task 3C and use CPU, for the SDGNN method.
```
python ./main_signed_directed_link.py --dataset OPCL --year 2016 --cpu --num_classes 5 --direction_only_task --method SDGNN
```

## Note

- The version of this paper which was published in LoG has a minor error and says that the entries of $\Theta^{(q)}$ lie in $[0,\pi]$ rather than $[-\pi,\pi]$. We also note that one may readily modify the version of $q_0$ so that the entries lie in other intervals. For instance, if we instead use the formula of $q_0$ but replace $2$ with $4$ (i.e., replacing $q_0$ with $q_0/2$), we would have entries in $[-\pi/2,\pi/2]$ with the same half-circle range as stated in the published version. These modifications may improve network performance for some tasks.
- `K` is the order (degree) of the Chebyshev polynomial in both the paper and
  this code. Consequently, the filter contains `K + 1` terms, from order zero
  through order `K`; the default `K=1` therefore uses two terms.

--------------------------------------------------------------------------------
