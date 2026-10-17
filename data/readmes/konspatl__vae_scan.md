# VAE-SCAN
A deep learning library for XAI-ECG analysis.

![](docs/vae_scan_framework.png)

## Installation
Install the Python requirements and *vaescan* package from the project directory:
```bash
pip install -r requirements.txt
pip install .
```

## Overview
VAE-SCAN is a variational autoencoder framework for explainable ECG analysis. This framework consists of an inherently explainable architecture that allows the discovery of bi-directional associations between ECG features and associated clinical factors.

The VAE-SCAN framework satisfies the following XAI requirements:
* Mapping of an abstract concept into a human-interpretable domain
* Explanations by monotonic associations to interpretable ECG features
* Fidelity of Explanations
* Robustness of explanations and model predictions to small input perturbations

## Example Usage

Examples of VAE and SCAN model training, testing, and visualizations can be found in the notebooks.

Training and testing scripts can be run with the following configuration files:

```bash
# VAE Model Training
python scripts/vae_train.py --dataset configs/ecg_dataset.json \
                            --split configs/split_train_val.json \
                            --train configs/train_vae.json

# VAE Model Testing
python scripts/vae_test.py --dataset configs/ecg_dataset.json \
                           --split configs/split_test.json \
                           --test configs/test_vae.json

# SCAN Model Training
python scripts/scan_train.py --dataset configs/ecg_dataset.json \
                             --labels configs/ecg_labels.json \
                             --split configs/split_train_val.json \
                             --train configs/train_scan.json

# SCAN Model Testing
python scripts/scan_train.py --dataset configs/ecg_dataset.json \
                             --labels configs/ecg_labels.json \
                             --split configs/split_test.json \
                             --test configs/test_scan.json
```

## Configuration files

- **dataset**: specifies the directory and structure of the ECG dataset (e.g., IDs, lead names, sfreq, etc.)
- **labels**: specifies a labels csv file that includes the ECG IDs and a number of selected targets
- **split**: specifies the csv files with the ECG IDs used for training, validation, and testing.
- **train**: specifies the model parameters used for training.
- **test**: specifies the model parameters used for testing.

For full details on each config file, see docs/configuration.md

## Interactive Visualizations
https://cardiacep.dept.ic.ac.uk/scan_viz/

## Citation
If you use this library, please cite our work: 

Patlatzoglou, K., Pastika, L., Barker, J. et al. The cost of explainability in artificial intelligence-enhanced electrocardiogram models. npj Digit. Med. 8, 747 (2025). https://doi.org/10.1038/s41746-025-02122-y

## License
[BSD 3-Clause](./LICENSE)
