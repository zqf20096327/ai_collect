# <center>**MIMA: Multimodal Integration with Modality-agnostic Autoencoders**</center>
<div style="text-align: center">

![MVAE Logo](/assets/model_structure.png "MIMA Model Structure")

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT Liscence][license-shield]][license-url]

</div>

<br>

## Table of Contents
1. [About the Project](#about-the-project)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
    - [Running in the command line](#running-in-the-command-line)
    - [Running in a Jupyter Notebook](#running-in-a-jupyter-notebook)
    - [Running in a Docker container](#running-in-a-docker-container)
4. [Authors](#authors)
5. [License](#license)


## 1. About the Project
This project implements a **Multimodal Variational Autoencoder** designed for the integration of heterogeneous molecular layers, enabling a comprehensive multimodal representation of the **cellular state**. The primary goal is to effectively capture **shared and unique biological signals** across different molecular data types while addressing batch effect correction to ensure more reliable downstream analyses.

This framework is designed to be **flexible and modular**, featuring a **modality-agnostic** approach that can be extended into **modality specific components** designed to account for the specificities of certain molecular data. Some of the main features of this framework are:

- **Cross-modal learning**, where information from one modality can inform another.

- **Biological signal disentanglement**, distinguishing true biological variation from technical noise.

- **Batch effect correction**, ensuring robust and reproducible multimodal integration across datasets.

The AI model at the core of this framework is designed to facilitate various applications, including cell state characterization, multimodal imputation, and enhanced biological inference. For a complete and detailed technical overview of how this framework is implemented, together with in-depth analysis on the performances of this tool for multiple downstream tasks and multiple datasets, please refer to [this research publication](http://www.atsomepoint.com).

This project has been developed within the research effort of the **Laboratory of Multi-omic Integrative Bioinformatics - KU Leuven**

## 2. Getting Started

The model can be executed locally using this repository. It is possible to integrate this framework in other Python projects using the source code files directly. <br>
Alternatively, it is possible to use the tool standalone by modelling a Jupyter Notebook based on the example templates provided within the *notebooks* folder.

The code is fully compatible with NVIDIA GPU based on CUDA, therefore if there is a GPU installed and available in the system it will be used automatically.

Lastly, the framework is redily available as a Docker Image that can be built locally. When used within Docker, the user can access the notebooks and experiment with the model using its own data.

### 2.1. Prerequisites

1. Python 3.10
2. NVIDIA CUDA support to run the model with GPU accelleration
3. Anaconda or Miniconda to manage the enviroinment
4. Docker engine to run the model as a container - **OPTIONAL**
5. Jupyter to run the tutorials - **OPTIONAL**


### 2.2. Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sifrimlab/MIMA
   ```

2. Change to the project repositry
   ```sh
   cd MIMA
   ```

3. Create the Python venv with conda (not necessary to use the Docker version)
    ```sh
    conda env create -f stable_release.yml
    conda activate mima
    ```

## 3. Usage
The framework requires the user to prepare the input data using standard formats such as **AnnData or MuData** files. The data should be pre-processed (depending on the specific data type) and, in case of multimodal (multi-omic) datasets, the modalities should be aligned/registered beforehand. **Unimodal** datasets can be provided as **AnnData** files, while paired **multimodal** datasets can be provided as **MuData** files. In order to perform multimodal data integration, the dataset must be **paired** (i.e. for a certain datapoint there are observations for each involved modality).

### 3.1. Integrating the framework in another Python Project
The source code of this package is provided in the **/src/** folder of this repository. To use the data integration model the user simply has to copy the whole repository folder into its own project folder and then use the tools provided. Multiple examples of how to use the multimodal data fusion framework can be found in the Jupyter Notebooks available in the folder **/notebooks/**.

For instance, if the user wishes to perform data integration on a single-cell multiome dataset with two modalities (i.e. scRNA and ATACseq):

```py
from MIMA.src.model import Modality, MIMA
import mudata as mu

# Load the MuData dataset
dataset = mu.read("/your/path/dataset.h5mu")

# Perform any necessary preprocessing step...

# Define one instance of Modality class for each omic layer
RNA = Modality(adata=mdata.mod["rna"], mod_name="rna", n_layers=2, n_hidden=300, z_dim=100, beta=0.01)
ATAC = Modality(adata=mdata.mod["atac"], mod_name="atac", n_layers=2, n_hidden=300, z_dim=100, beta=0.01)

# Define the overall multimodal integration model
model = MIMA([RNA, ATAC], beta=0.001)

# Define the data dictionary using the standard format
input_dict = {
    "paired": mu.MuData(
        {
            "rna":mdata.mod["rna"].copy(),
            "atac":mdata.mod["atac"].copy()
        }
    )
}

# Train the model - Learned weights and training procedure will be stored in the output path
model.train_mima(data_dict=input_dict, n_epochs=50, train_size=0.8 dataset_name="sc_dataset", output_path="/your/output/path")

# Project the input data into the latent spaces to obtain the multimodal embeddings
latent_dict = model.to_latent(input_dict, use_gpu=True)

# latent_dict["paired"]["z_poe"] contains the integrated multimodal embeddings

```


### 3.2. Running in a Jupyter Notebook
The easiest way to get familiar with the framework is to explore one of the several Jupyter Notebooks available for evaluation and analysis included in this repository (folder **notebooks**).
In order to correctly use the notebooks, it is necessary to install the conda enviroinment as explained in the [Installation section](#installation).

### 3.3. Running in a Docker Container
This framework can be run in a Docker Container in order to streamline the deployment, since the user won't have to take care about the enviroinment setup.
To support this usage mode, the machine on which the user intend to deploy the Docker Container needs to have the Docker Engine installed and running. For more informations on how to setup your machine to support docker please refer to the [official Docker guide](https://docs.docker.com/engine/install/). To use Docker, the user will need to have administrative (root) priviledges. If in the machine is already installed Docker Engine but the user do not have admin priviledges, it is possible to setup Rootless Docker following [this guide](https://docs.docker.com/engine/security/rootless/).

Once Docker Engine is installed, build (or modify, if needed for custom configurations) the project through Docker Compose:
```sh
# Move to the folder in which the repository has been downloaded
cd /your/path/MIMA

# Build the Docker project
docker compose build
```

This will build the docker image to run the container, as well as a Docker Volume to persistenly store the input (i.e. the configuration file and the datasets that the user intend to use) and the outputs of the data integration. For more information about Docker Volumes and how to manage data across them please refer to [this guide](https://docs.docker.com/engine/storage/volumes/).

By default, the Docker Volume will be mounted in the following directory in the host machine:
```sh
~/mima_data
```

Any file in this folder will be automatically available for the Docker Container. If the user wish to modify the location in which the Docker Volume is mounted (i.e. to another storage location), it is sufficient to modify the **docker-compose.yml** file at **line 14**
```yml
~/mima_data:/volume        # Change ~/mima_data with your desired path
```

Once the Docker Container is up and running, the user can connect to JupyterLab through a web browser to interact with the notebooks provided in this repository reaching the address http://localhost:8888

The conda enviroinment will be automatically installed but the user might have to select it from JupyterLab in order to use the notebooks.

## Authors

This framework has been developed in the context of the accademic research conducted at the [**Laboratory of Multi-omic Integrative Bioinformatics (LMIB)**](https://sifrimlab.org/) with the key contributions of:

1. [Jose Ignacio Alvira Larizgoitia](https://www.kuleuven.be/wieiswie/en/person/00148287)
2. [Gabriele Partel](https://www.kuleuven.be/wieiswie/en/person/00143160)
3. [Lorenzo Venturelli](https://www.kuleuven.be/wieiswie/en/person/00172804)
4. [Anis Ismail](https://www.kuleuven.be/wieiswie/en/person/00157429)


<!--LICENSE -->
## License

See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/sifrimlab/MIMA.svg?style=for-the-badge
[contributors-url]: https://github.com/sifrimlab/MIMA/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sifrimlab/MIMA.svg?style=for-the-badge
[forks-url]: https://github.com/sifrimlab/MIMA/network/members
[stars-shield]: https://img.shields.io/github/stars/sifrimlab/MIMA.svg?style=for-the-badge
[stars-url]: https://github.com/sifrimlab/MIMA/stargazers
[issues-shield]: https://img.shields.io/github/issues/sifrimlab/MIMA.svg?style=for-the-badge
[issues-url]: https://github.com//sifrimlab/MIMA/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com//sifrimlab/MIMA/LICENSE
