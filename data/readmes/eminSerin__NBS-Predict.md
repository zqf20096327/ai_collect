# NBS-Predict

<p align="center">
  <img src="docs/images/NBS-Predict_logo.png" width="480px"/> 
</p>

NBS-Predict is a prediction-based extension of the Network-based Statistic (Zalesky et. al., 2010). NBS-Predict aims to provide a fast way to identify neuroimaging-based biomarkers with high generalizability by combining machine learning with graph theory in a cross-validation structure.

## Overview
NBS-Predict operates in a cross-validation structure (nested if hyperparameter optimization is desired). The general algorithm consists of model evaluation, feature selection like suprathreshold edge selection, hyperparameter optimization (optionally), and machine learning algorithm optimization (optionally).  

## Prerequisites

NBS-Predict requires the following software and toolboxes to run properly: 

```
Matlab (2020b or newer) 
Statistics and Machine Learning Toolbox
Parallel Computing Toolbox (optional)
```

## Installing

1. Download or clone this repository to a direction of your choice. 

```
git clone --recursive git@github.com:eminSerin/NBS-Predict.git
```

2. Run MATLAB and navigate the NBS-Predict's directory using either the command window or the Current Folder window. Then, type this command to add NBS-Predict to your MATLAB path. 

```
addpath(genpath(pwd));
```

## Sample Data

You can download sample data using the following link: [NITRC](https://www.nitrc.org/docman/view.php/1517/179438/).
This dataset comprises synthetic network data simulating regression and classification problems. 
Since the sample data is synthetic, please keep in mind that, results obtained following the analysis of this data do not imply any significant information. 
This sample dataset should only be used to check whether the toolbox works properly and to serve as an example input structure so that you can organize your input data accordingly.

## Example

1. Type this command to start NBS-Predict
```
start_NBSPredict();
```
2. The welcome window of NBS-Predict will automatically appear on the screen. 

<img src="docs/images/NBSPredict_1.png" width="720px"/> 

3. Using this window, create a new workspace. To do this, write a name for the workspace and press the return key. A pop-up window asking the directory for the workspace will appear. After selecting the directory, hit the "Create" button to create the workspace. The created workspace will appear on the list box below. Then, hit the "Start" button to run the workspace. 

4. The analysis setup window of NBS-Predict will automatically appear on the screen.

<img src="docs/images/NBSPredict_2.png" width="720px"/> 

5. Select the directory that contains subjects' connectivity matrices. Then, select brain parcellation and design matrix files. Specify a contrast vector for the statistical model used selecting suprathreshold edges across folds. Optionally, you may define advanced parameters such as number of CV folds, number of CV repetitions, performance metrics. Once you finish selecting data and optional parameters, hit the RUN button to start the analysis. NBS-Predict will last from minutes to hours depending on the computer, sample size, and brain parcellation atlas used. 

<img src="docs/images/NBSPredict_3.png" width="720px"/> 

6. Following the analysis, the NBS-Predict Results Viewer window will automatically appear on the screen. Here, you view display weighted adjacency matrix, weighted network on a circular graph, weighted network on a 3D brain surface (BrainNet Viewer, Xia et al., 2013), and confusion matrix. Weights represent the presence of edges in the selected connected component across outer folds and their prediction performances. That allows us to evaluate the contribution of each edge to the overall model straightforwardly. You can further set a weight threshold to visualize a subnetwork comprising the most relevant edges. Also, by clicking the "Save Figure" button, you can save figures in several formats. 

<img src="docs/images/NBSPredict_4.png" width="720px"/> 

See the [MANUAL.pdf](docs/MANUAL.pdf) file for the detailed user guide. 

Additionally, see the [Tutorial_HCP.pdf](docs/Tutorial_HCP.pdf) file for example use of NBS-Predict. 

## Terminal And Cluster Use

NBS-Predict can be run headlessly from a terminal or high-performance cluster job using the command-line interface `run_NBSPredict_cli.m`. 

You can build the entire analysis configuration directly from key-value arguments without needing to pre-build a configuration structure or `.mat` file.

### Required Arguments (when not using `configFile`):
* `corrPath`         - Path to directory containing connectivity matrices.
* `designPath`       - Path to design matrix file (`.mat` or `.csv`).
* `brainRegionsPath` - Path to brain regions parcellation file (`.mat` or `.csv`).
* `contrast`         - Contrast vector, e.g. `[1, -1]` or as a string `'[1, -1]'`.

### Example CLI usage:
```bash
# 1. Standard key-value CLI run
matlab -batch "run_NBSPredict_cli('corrPath', '/data/connectomes', 'designPath', '/data/design.csv', 'brainRegionsPath', '/data/regions.csv', 'contrast', [1, -1])"

# 2. Key-value CLI run with advanced options (parallel workers, permutation testing)
matlab -batch "run_NBSPredict_cli('corrPath', '/data/connectomes', 'designPath', '/data/design.mat', 'brainRegionsPath', '/data/regions.csv', 'contrast', '[1, -1]', 'numCores', 8, 'kFold', 5, 'repCViter', 20, 'ifPerm', 1, 'permIter', 500, 'outputFile', '/results/results.mat')"
```

### Backward Compatibility:
If you already have a pre-built configuration `.mat` file, you can load it using the `'configFile'` argument and dynamically override any parameter on top of it.
```bash
matlab -batch "run_NBSPredict_cli('configFile', '/path/to/NBSPredict_config.mat', 'numCores', 8, 'repCViter', 20)"
```

### Cluster Batch Job Example (SLURM):
Put the command in a submitted job script:

```bash
#!/bin/bash
#SBATCH --job-name=nbspredict
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=12:00:00

module load matlab
cd /path/to/NBS-Predict
matlab -batch "run_NBSPredict_cli('corrPath', '/data/connectomes', 'designPath', '/data/design.mat', 'brainRegionsPath', '/data/regions.csv', 'contrast', [1, -1], 'numCores', 8, 'outputFile', '/results/results.mat')"
```

The CLI runner disables the results viewer by default (`'ifView', 0`) for headless environment compatibility. To force it to open, pass `'ifView', 1`.

## Test

You may test the performance of NBS-Predict in predicting target variable or identifying edges with ground truth on several synthetic networks (small-world, scale-free or random) data by typing this command: 

```
test_NBSPredict(parameters);
```

The parameters are extensively documented in the test_NBSPredict.m function.

You may also use the simulation function that automatically runs the test function n times and using various parameters. To do that, type this command: 

```
sim_testNBSPredict(parameters);
```

The parameters are extensively documented in the sim_testNBSPredict.m function. 

Also, see the [Tutorial_Simulation.pdf](docs/Tutorial_Simulation.pdf) document for an example use of the simulation function.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/eminSerin/NBS-Predict).  

## Authors

NBS-Predict was designed by Emin Serin, Andrew Zalesky, Johann D. Kruschwitz and Henrik Walter, and developed by Emin Serin. 

## Contributing

You may contribute in this project in many ways such as bringing new features to NBS-Predict, improving documentantation or reporting bugs. See the [CONTRIBUTING.md](CONTRIBUTING.md) file for details

## Citation

If you use the toolbox, please cite the following paper: 

Serin, E., Zalesky, A., Matory, A., Walter, H., & Kruschwitz, J. D. (2021). NBS-Predict: A Prediction-based Extension of the Network-based Statistic. NeuroImage, 118625.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## References

References for the functions or toolboxes used in NBS-Predict toolbox: 

1. Morel, (2018). Gramm: grammar of graphics plotting in Matlab. Journal of Open Source Software, 3(23), 568, https://doi.org/10.21105/joss.00568
2. Paul Kassebaum (2020). circularGraph (https://github.com/paul-kassebaum-mathworks/circularGraph), GitHub. Retrieved September 6, 2020.
3. Roland Pfister (2019). dlmcell (https://www.mathworks.com/matlabcentral/fileexchange/25387-dlmcell), MATLAB Central File Exchange. Retrieved September 3, 2019.
4. Xia, M., Wang, J., & He, Y. (2013). BrainNet Viewer: a network visualization tool for human brain connectomics. PloS one, 8(7), e68910.
5. Zalesky, A., Fornito, A., & Bullmore, E. T. (2010). Network-based statistic: identifying differences in brain networks. Neuroimage, 53(4), 1197-1207.
