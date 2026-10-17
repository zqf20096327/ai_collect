# Automatic Music Sample Identification with Multi-Track Contrastive Learning

### Abstract

Sampling, the technique of reusing pieces of existing audio tracks to create new music content, is a very common practice in modern music production. In this paper, we tackle the challenging task of automatic sample identification, that is, detecting such sampled content and retrieving the material from which it originates. To do so, we adopt a self-supervised learning approach that leverages a multi-track dataset to create positive pairs of artificial mixes, and design a novel contrastive learning objective. We show that such method significantly outperforms previous state-of-the-art baselines, that is robust to various genres, and that scales well when increasing the number of noise songs in the reference database. In addition, we extensively analyze the contribution of the different components of our training pipeline and highlight, in particular, the need for high-quality separated stems for this task.

### Authors

Alain Riou, Joan Serrà, & Yuki Mitsufuji.

### Reference and links

A. Riou, J. Serrà, & Y. Mitsufuji (2025). **Automatic Music Sample Identification with Multi-Track Contrastive Learning**. IEEE Int. Conf. on Acoustics, Speech, and Signal Processing (ICASSP), pp. 14587-14591.

[[`arxiv`](https://arxiv.org/abs/2510.11507)] [[`ieee`](https://doi.org/10.1109/ICASSP55912.2026.11461576)] [[`checkpoint`](https://zenodo.org/records/17413869)]

## Inference with pretrained checkpoint

For inference, the only required dependencies are PyTorch, Hydra, numpy, scipy and tqdm. First, install them following the respective procedures. Then, clone and install this repository:
```sh
git clone https://github.com/sony/sampleid.git
cd sampleid
pip install -e .
```

Then, to use the available checkpoint in your own Python project, type the following:
```python
import torch

from sampleid import SampleID

sampleid_model = SampleID.load_checkpoint()

x = torch.randn(3, 16000 * 5)  # 5 seconds of audio at 16kHz (batch of 3 mono signals)
with torch.inference_mode():
    embeddings = sampleid_model(x, audio=True)

print(embeddings.shape)  # should be (batch_size, 1, embed_dim)
```
You can use a custom checkpoint by setting `SampleID.load_checkpoint(ckpt_path="path/to/ckpt")`. Otherwise, the checkpoint available on Zenodo will be loaded.

**Note:** the model always averages embeddings in time, regardless of the length of the audio input. If you want to compute embeddings per audio chunks from a full song, audio chunks should be computed manually beforehand (you can then process them in parallel as batches).


## Training your own models

### Setup

1.  Clone the repository
    ```sh
    git clone https://github.com/sony/sampleid.git
    ```

2.  Install all the dependencies

3.  This model is aimed to be trained on multi-track data. Before training, we start by pre-computing the activation masks and list of sources for each audio.
    ```sh
    python src/compute_activations.py <path/to/your/dataset> <path/to/metadata>
    ```
    By default, the metadata path defaults to `data/`.

    You can define a validation and a test set by changing the flags at the beginning of the file.

    By default, the format for the initial dataset is supposed to be:
    ```
    your_dataset/
    ├── part1/
    |   ├── song1/
    |   |   ├── bass.wav
    |   |   ├── lead.wav
    |   |   ...
    |   |   └── piano.wav
    |   ├── song2/
    |   |   ├── guitar1.wav
    |   |   ├── guitar2.wav
    |   |   └── drums + perc.wav
    |   ...
    ├── part2/
    |   ...
    └── valid/
        └── whatever_song/
            ├── vocals.wav
            ├── back.wav
            ├── drums.wav
            └── fx.wav
    ```
    If it is different but you don't want to touch your dataset, or if you want to filter out specific instruments, etc. update the `list_wav_files` function or the definition of `all_song_dirs` at the beginning of `main`.

4.  Write a `mydata.yaml` file in `configs/data` with the appropriate paths, and following the given example.

5.  Train!
    ```sh
    python src/train.py data=mydata model=resnet50 logger=csv
    ```
    To use another logger, just replace `logger=csv` by `logger=tensorboard`, `logger=wandb`...

### Usage

#### Code organization

This repository builds upon the [lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template) which, as its name suggests, relies on [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable) for training and [Hydra](https://hydra.cc) for handling configurations. We refer to the corresponding documentations for more info.

Folder names are (hopefully) self-explanatory: configs are recursively defined in `configs/` while source code is implemented in `src/`. `scripts/` contains mostly evaluation scripts that are called either by the user or from the training process.

Within `src`, most folder names are clear. Just a few remarks:
- There are both `models/` and `networks/`. `models/` contains the logic (training loops, loss functions) while `networks/` contains neural architectures (ResNet, etc.)
- Things implemented in `callbacks/` are excluded from the computation of the signature (see below). Therefore, nothing affecting the final results of the training should be implemented here.
- For most audio effects, we use the great [pedalboard](https://github.com/spotify/pedalboard) library. In `src/data/pedalboard.py`, we implement a subclass of the original class that enables randomizing the parameters of the effects on-the-fly, making it quite handy to use.
An example of the syntax is provided in `configs/data/moisesdb.yaml`.

#### Experiment management

For launching and managing different experiments, we use [Dora](https://github.com/facebookresearch/dora).

We refer to Dora's doc for advanced usage. However, we provide here basic commands.

To start training your model locally, instead of `python src/train.py`, you can type `dora run`.

If you are working on a SLURM-based cluster, type:
```sh
dora launch -p <partition_name> -g <num_gpus> data=mydata model=resnet50 [whatever hydra args...]
```

An interesting aspect of Dora is that it generates a hashed signature for each experiment based on the config. Checkpoints will be stored based on these signatures, and they are also used as default experiment name/id in Weights & Biases if you are using it. This implies that it is the *same* command for starting a new experiment, restarting a failed/timed-out one, and checking the final results of a finished run. Signatures can be re-injected in YAML configs using `${dora:xp.sig}`.

**Bonus:** When you are debugging, it does not create dozens of empty log folders.

A drawback is that **you cannot do dirty hacks by overwriting yaml configs on-the-fly. It will mess up EVERYTHING.**

Instead do this:
- If you want to change a few parameters, use Hydra command-line.
- If you want to change many things, create a `configs/experiment/newconf.yaml` with the new options, then add `experiment=newconf` at the end of your command.
- If you want to a slight variant of a previous xp but with just one (or a few) different parameters, use dora's `-f` option:
  ```sh
  dora run/launch -f <previous xp sig> param=new_value
  ```

## Performances

Here are the performances of our model compared to previous state-of-the-art:
| Model                           | mAP   | HR@1  | HR@10 |
|----------------------------------|-------|-------|-------|
| [Cheston et al. (2025)](https://arxiv.org/abs/2502.06364)            | 0.441 | -     | -     |
| [Bhattacharjee et al. (2025)](https://www.arxiv.org/abs/2506.14684)      | 0.442 | 0.155 | 0.191 |
| Ours                             | 0.603 | 0.587 | 0.733 |
| Ours + Top-5 retrieval           | **0.622** | **0.600** | **0.747** |

Additional results are provided in the [paper](https://arxiv.org/abs/2510.11507).

## Cite

```bibtex
@article{RiouSampleID,
   author = {Alain Riou and Joan Serrà and Yuki Mitsufuji},
   title = {Automatic Music Sample Identification with Multi-Track Contrastive Learning},
   url = {https://arxiv.org/abs/2510.11507},
   year = {2025}
}
```
