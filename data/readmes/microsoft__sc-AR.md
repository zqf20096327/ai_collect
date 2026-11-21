# Adaptive Resampling for Improved Machine Learning in Imbalanced Single-cell Datasets

This repository contains the code that accompanies our paper, "Adaptive resampling for improved machine learning in imbalanced single-cell datasets". You can find the link to the preprint here: https://www.biorxiv.org/content/10.1101/2025.11.04.686583v1

## Abstract
While machine learning models trained on single-cell transcriptomics data have shown great promise in providing biological insights, existing tools struggle to effectively model underrepresented and out-of-distribution cellular features or states. We present a generalizable adaptive resampling (AR) approach that addresses these limitations and enhances single-cell representation learning by resampling data based on its learned latent structure in an online, adaptive manner concurrent with model training. Experiments on gene expression reconstruction, cell type classification, and perturbation response prediction tasks demonstrate that the AR training approach leads to significantly improved downstream performance across datasets and metrics. Additionally, AR often produces higher-quality cellular embeddings than standard training methods and performs competitively with label-based class balancing as a training-data composition strategy, without requiring extrinsic annotations or metadata. Our results suggest that AR may serve as a valuable technique for improving representation learning and predictive performance in single-cell transcriptomic models.

---

## Environmental Setting

Create a new environment (Python 3.10.13 was used in our experiments):

```bash
conda env create -f requirements.yaml
conda activate scar-env
```

## Codebase overview

```bash
├── bash          # drivers that run each experiment with the settings used in the paper
├── scripts       # data generation, model training and prediction, AR weights
├── eval_scripts  # evaluation, plots and plotting notebooks
├── data          # input data (from Zenodo, see Datasets)
├── saved_models  # trained models will be saved here, written by the drivers
├── result        # evaluation results and figures will be saved here, written by the drivers
```

## Reproducing Results

All datasets, the run settings of the trained models and sample model checkpoints are available on Zenodo: [doi:10.5281/zenodo.24384415](https://doi.org/10.5281/zenodo.24384415). Unpack the archives in the repository root (`data.zip` gives `data/`). The drivers in `bash/` list their stages and options when called without arguments.

## Datasets

For the scGen models: `data/species.h5ad`, `data/pbmc.h5ad` and `data/hpoly.h5ad`, the Species, PBMC and H. poly perturbation datasets of the original scGen study ([scgen-reproducibility](https://github.com/theislab/scgen-reproducibility)). The designed datasets used for training and evaluation are generated from them with the following command, which created data files to `data/designed/`.

```bash
bash bash/make_designed_data.sh all
```


For the scVI models, the following files are in `data/sctab/`, used in our experiments:

- BaseModel_scTabAll_seed0_allbase_TrainingData.h5ad: generated using [https://github.com/microsoft/scFM-datamix/blob/main/Preprocess/preprocess_data_allbase.py]

- BaseModel_scTabBloodOnly_seed0_bloodbase_TrainingData.h5ad: generated using [https://github.com/microsoft/scFM-datamix/blob/main/Preprocess/preprocess_data_bloodbase.py]

- Neurons_H1830002_10Ksubset.h5ad: generated using [https://github.com/microsoft/scFM-datamix/blob/main/Preprocess/preprocess_eval_data.py]

- sctab_train_10pct_heart_nohematopoietic.h5ad: The dataset termed "Heart" was created by subsampling all the cells labeled "heart" in the scTab data and retaining only those with the following cell type labels: cardiac muscle cell; pericyte; capillary endothelial cell; fibroblast of cardiac tissue; endothelial cell of artery; smooth muscle cell; endothelial cell; vein endothelial cell; neuron; endothelial cell of lymphatic vessel; cardiac neuron; and mesothelial cell. This left the final evaluation dataset with 13,571 cells.

- sctab_train_10pct_kidney_nohematopoietic.h5ad: The dataset termed "Kidney" was created by subsampling all the cells labeled "kidney" in the scTab data and retaining only those with the following cell type labels: epithelial cell of proximal tubule; kidney loop of Henle thick ascending limb epithelial cell; endothelial cell; kidney collecting duct principal cell; kidney distal convoluted tubule epithelial cell; kidney interstitial fibroblast; kidney collecting duct intercalated cell; kidney connecting tubule epithelial cell; kidney loop of Henle thin descending limb epithelial cell; kidney loop of Henle thin ascending limb epithelial cell; renal interstitial pericyte; and vascular associated smooth muscle cell. This left the final evaluation dataset with 8,468 cells.

## scGen

All scGen stages are run by `bash/run_scgen.sh <stage> <dataset>`, with `<dataset>` one of `species`, `pbmc`, `lps-hpoly` or `all`. On a SLURM cluster, the train, predict and eval stages can be submitted with `bash/submit_scgen_slurm.sh`.

### Training

```bash
bash bash/run_scgen.sh train species
```

Trains six arms for every design, rare-cell percentage and seed: Standard, uniform resampling, and AR with the maximum, mean, geometric mean and k-nearest-neighbor aggregation functions. Each model is saved in `saved_models/scgen/<data>/<hash>/`, where `<hash>` is computed from the run settings.

### Prediction and evaluation

`bash/run_scgen.sh` also runs the prediction, evaluation and plotting of the trained models, one stage at a time. Called without arguments, it lists its stages.

## scVI
### Training and evaluation

`bash/run_scvi.sh` trains scVI on the scTab data with standard training and AR, and evaluates gene expression reconstruction and cell type classification:

```bash
bash bash/run_scvi.sh train
bash bash/run_scvi.sh eval-recon
bash bash/run_scvi.sh eval-class
```

The same script runs the class-balancing and geometric-sketching baselines; the steps are listed in its header.

The results are saved in `result/test/scVI-{reconstruction,classification}-evals*/`.


## Adaptive Resampling module

To use AR in your own pipeline, pass the latent projections of all training samples to `calculate_resampling_weights()` in `scripts/AR_resampling_weight_calculator.py`. It returns one resampling weight per sample, which can be used to draw the training samples of the next epoch. The weights can also be computed once before training, from the embeddings of a large-scale foundation model, to change the training data distribution for any downstream task.

`ar_aggregation_ablation.ipynb` is an example of the different aggregation functions you can use in your own projects to turn the latent projections into one resampling weight per sample: the maximum (the default in `calculate_resampling_weights()`), the mean, the geometric mean and a k-nearest-neighbor rule, with uniform resampling as a control. It trains a Standard and an AR model with each function on a small example dataset. The functions are in `scripts/ar_aggregation_variants.py`; `calculate_resampling_weights_with_method()` selects one by name.

## Citation

If our work assists your research, please use the following to cite our work:

```bash
@article {Navidi2025.11.04.686583,
	author = {Navidi, Zeinab and Thoutam, Akshaya and Hughes, Madeline and Raghavan, Srivatsan and Winter, Peter S. and Crawford, Lorin and Amini, Ava P.},
	title = {Adaptive resampling for improved machine learning in imbalanced single-cell datasets},
	elocation-id = {2025.11.04.686583},
	year = {2025},
	doi = {10.1101/2025.11.04.686583},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2025/11/05/2025.11.04.686583},
	eprint = {https://www.biorxiv.org/content/early/2025/11/05/2025.11.04.686583.full.pdf},
	journal = {bioRxiv}
    }

```

## License

This project is available under the MIT License.

## Transparency Documentation

Microsoft's Responsible AI Transparency Documentation for Research is provided on this repository, please see [scAR_Transparency](https://github.com/microsoft/sc-AR/blob/main/scAR_Transparency.pdf).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional comments or questions.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.
