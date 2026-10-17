# HydroGAT

Accurate flood forecasting remains a critical challenge for water‐resource management, as it demands simultaneous modeling of local, time-varying runoff drivers (e.g., rainfall-induced peaks, baseflow trends) and complex spatial interactions across a river network.

Traditional data-driven approaches, such as convolutional networks and sequence-based models, ignore topological information about the region. Graph Neural Networks (GNNs), in contrast, propagate information exactly along the river network, making them ideal for learning hydrological routing. However, state-of-the-art GNN-based flood prediction models still collapse pixels to coarse catchment polygons because the cost of training explodes with graph size and higher resolution. Furthermore, most existing methods treat spatial and temporal dependencies separately, either applying GNNs solely on spatial graphs or transformers purely on temporal sequences, thus failing to simultaneously capture spatiotemporal interactions critical for accurate flood prediction.

To address these limitations, we introduce a **heterogenous basin graph** to represent every land and river pixel as a node connected by both physical hydrological flow directions as well as inter-catchment relationships. We also propose **HydroGAT**, a novel spatiotemporal network that adaptively learns both local temporal importance as well as most influential upstream locations.

Evaluated in two Midwestern US basins and across five baseline architectures, our model achieves higher **NSE (up to 0.97)**, improved **KGE (up to 0.96)**, and low bias (**PBIAS within ± 5%**) in hourly discharge prediction, while offering interpretable attention maps that reveal sparse, structured intercatchment influences. To support high-resolution basin-scale training, we develop a distributed data-parallel pipeline that scales efficiently up to **64 NVIDIA A100 GPUs** on NERSC Perlmutter supercomputer, demonstrating up to **15× speedup** across nodes.

## Cite Us

If you use HydroGAT, please cite:

```bibtex
@inproceedings{sarkar2025hydrogat,
  author    = {Sarkar, Aishwarya and Hakimi, Autrin and Chen, Xiaoqiong and Huang, Hai and Lu, Chaoqun and Demir, Ibrahim and Jannesari, Ali},
  title     = {HydroGAT: Distributed Heterogeneous Graph Attention Transformer for Spatiotemporal Flood Prediction},
  booktitle = {Proceedings of the ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (SIGSPATIAL '25)},
  year      = {2025},
  address   = {Minneapolis, MN, USA},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3748636.3764172},
  url       = {https://doi.org/10.1145/3748636.3764172},
  note      = {Licensed under CC BY 4.0}
}
```

## Setup

### Prerequisites

- Python 3.10 or higher
- CUDA-enabled GPU (for training and inference)
- CUDA toolkit 11.7 or compatible version (11.8, 12.1, etc.)

### Environment Setup

1. **Install PyTorch (GPU version)**

   First, install PyTorch with CUDA support. Check [PyTorch's official website](https://pytorch.org/) for installation commands matching your CUDA version. Replace `cu117` in the URL with your CUDA version (e.g., `cu118`, `cu121`).
   
   Example for CUDA 11.7:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
   ```
   
   Example for CUDA 11.8:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Install DGL (Deep Graph Library)**

   Install DGL compatible with your CUDA version. Adjust the CUDA version in the URL to match your PyTorch installation (e.g., `cu117`, `cu118`, `cu121`).
   
   Example for CUDA 11.7:
   ```bash
   pip install dgl -f https://data.dgl.ai/wheels/cu117/repo.html
   ```
   
   Example for CUDA 11.8:
   ```bash
   pip install dgl -f https://data.dgl.ai/wheels/cu118/repo.html
   ```

3. **Install other dependencies**

   Install the remaining dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

   **Important Notes:**
   - Do NOT install `torch-cpu` as it will break DGL compatibility
   - When installing packages via `pip install`, verify that PyTorch and DGL are not being downgraded to CPU versions
   - Some packages from conda-forge may have dependencies that require CPU-only PyTorch - check installation output carefully

### Required Python Packages

The following packages are required (see `requirements.txt` for versions):

- **Core DL**: torch (GPU), dgl (GPU)
- **Scientific**: numpy, scipy, scikit-learn
- **Data**: pandas, xarray, netCDF4
- **Geospatial**: geopandas, rasterio, rioxarray, pyproj
- **Utilities**: Pillow, matplotlib, seaborn, networkx, tqdm

## Data Preparation

### Graph Processing

Before training, you need to process your raw data (precipitation, discharge, flow direction, DEM, etc.) into a graph format. Use the `graph_processor.py` script:

```bash
python preprocess/graph_processor.py \
    --basin_name "cedar-river-basin" \
    --precip_raw_dir "data/cedar-river-basin/NCPrecipitation_fixed" \
    --flow_dir_file "data/cedar-river-basin/BasinAttribution/flow_dir.nc" \
    --target_node_file "data/cedar-river-basin/BasinAttribution/CedarRiverBasin_Guage.shp" \
    --discharge_dir "data/cedar-river-basin/Discharge_NA_Fill" \
    --discharge_raw_dir "data/discharge/data_time_series" \
    --distance_file "data/cedar-river-basin/BasinAttribution/distance.nc" \
    --dem_file "data/cedar-river-basin/BasinAttribution/dem.nc" \
    --catchment_relationship_file "data/discharge/catchment_relationship.csv" \
    --output_dir "data/cedar-river-basin/graph-with-catchment-relationship" \
    --months "5,6,7,8,9" \
    --years "2012,2013,2014,2015,2016,2017,2018" \
    --add_catchment_relationship \
    --node_coordinates \
    --update_output
```

**Required Arguments:**
- `--basin_name`: Name of the basin
- `--precip_raw_dir`: Directory containing raw precipitation NetCDF files
- `--flow_dir_file`: Flow direction NetCDF file path
- `--target_node_file`: Target node shapefile path
- `--discharge_dir`: Directory containing processed discharge CSV files
- `--discharge_raw_dir`: Directory containing raw discharge CSV files
- `--distance_file`: Distance data NetCDF file path
- `--dem_file`: Digital Elevation Model NetCDF file path
- `--catchment_relationship_file`: Catchment relationship CSV file path
- `--output_dir`: Output directory for the processed graph

**Optional Arguments:**
- `--months`: Comma-separated months (default: "5,6,7,8,9")
- `--years`: Comma-separated years (default: "2012,2013,2014,2015,2016,2017,2018")
- `--debug`: Enable debug mode (generates debug plots)
- `--clip`: Clip precipitation data using flow direction mask
- `--flip`: Flip data for coordinate system
- `--add_catchment_relationship`: Add catchment relationship edges
- `--use_distance`: Use distance information for edge weights
- `--connect_to_main_component`: Connect all nodes to main component
- `--node_coordinates`: Include node coordinates (default: True)
- `--update_output`: Write output files (if not set, runs in dry-run mode)

## Training

### Single GPU Training

For training on a single GPU:

```bash
python src/dist_train.py \
    --launcher slurm \
    --mode train \
    --graph_dir "data/cedar-river-basin/graph-with-catchment-relationship" \
    --checkpoint_dir "checkpoints/cedar-river-basin" \
    --model hydrogat \
    --basin_name "cedar-river-basin" \
    --epochs 100 \
    --batch_size 8 \
    --input_steps 72 \
    --output_steps 72 \
    --tgcn_hidden_size 32 \
    --s_heads 2 \
    --t_heads 2 \
    --catchment_relationship
```

### Distributed Training (Multi-GPU/Multi-Node)

HydroGAT supports distributed training across multiple GPUs and nodes using PyTorch's DistributedDataParallel (DDP). The code supports SLURM job schedulers.

#### SLURM Example

Create a SLURM job script (`train.sh`):

```bash
#!/bin/bash
#SBATCH --nodes=1              # Number of nodes
#SBATCH --gpus-per-node=4       # GPUs per node
#SBATCH --constraint=gpu
#SBATCH --time=08:00:00
#SBATCH --job-name=hydrogat

# Set environment variables
NNODES=${SLURM_NNODES:-1}
NGPUS_PER_NODE=4
WORLD_SIZE=$((NNODES * NGPUS_PER_NODE))

echo "Nodes=$NNODES  GPUs/node=$NGPUS_PER_NODE  World size=$WORLD_SIZE"

MASTER_ADDR=$(scontrol show hostname $SLURM_NODELIST | head -n1)
MASTER_PORT=29501

export MASTER_ADDR=$MASTER_ADDR
export MASTER_PORT=$MASTER_PORT
export WORLD_SIZE=$WORLD_SIZE

nvidia-smi

# Activate your environment
# source activate your_env  # or conda/micromamba activate

# Run distributed training
srun --ntasks=${WORLD_SIZE} \
     --ntasks-per-node=${NGPUS_PER_NODE} \
     --gres=gpu:${NGPUS_PER_NODE} \
     --cpu-bind=cores \
     python src/dist_train.py \
       --launcher slurm \
       --mode train \
       --graph_dir "data/cedar-river-basin/graph-with-catchment-relationship" \
       --checkpoint_dir "checkpoints/cedar-river-basin" \
       --model hydrogat \
       --basin_name "cedar-river-basin" \
       --epochs 100 \
       --batch_size 8 \
       --input_steps 72 \
       --output_steps 72 \
       --tgcn_hidden_size 32 \
       --s_heads 2 \
       --t_heads 2 \
       --catchment_relationship
```

Submit with:
```bash
sbatch train.sh
```

**Key Distributed Training Parameters:**

- `--launcher`: Must be `slurm` to set up distributed environment correctly
- `WORLD_SIZE`: Total number of GPUs (nodes × GPUs per node)
- `MASTER_ADDR` and `MASTER_PORT`: Used for inter-node communication

**Note:** According to the [HydroGAT paper](https://arxiv.org/html/2509.02481v1), when using `--model hydrogat`, the learning rate is automatically set to 0.01 (AdamW optimizer) with weight decay 1e-4 and scheduler patience 5. The default hyperparameters for HydroGAT are: 72 hours input/output windows, 32 hidden features, 2 attention heads per module (spatial and temporal), and batch size 8.

## Evaluation

To evaluate a trained model, you need to provide the checkpoint path and ensure all model parameters match those used during training.

### Single GPU Evaluation

For evaluating on a single GPU:

```bash
python src/dist_train.py \
    --launcher slurm \
    --mode evaluate \
    --graph_dir "data/cedar-river-basin/graph-with-catchment-relationship" \
    --checkpoint "checkpoints/cedar-river-basin/cedar-river-basin_hydrogat_epoch100_lr0.001_patience5_input72_output12_batch8_controlTTSS_y2012_2018_m5-9.pt" \
    --model hydrogat \
    --basin_name "cedar-river-basin" \
    --input_steps 72 \
    --output_steps 72 \
    --tgcn_hidden_size 32 \
    --s_heads 2 \
    --t_heads 2 \
    --catchment_relationship
```

**Required Arguments for Evaluation:**
- `--mode evaluate`: Set mode to evaluation
- `--checkpoint`: Path to the trained model checkpoint file
- `--graph_dir`: Directory containing the processed graph file
- `--basin_name`: Name of the basin (must match training configuration)
- `--model`: Model name (must match training configuration, e.g., `hydrogat`)
- `--input_steps`: Number of input timesteps (must match training)
- `--output_steps`: Number of output timesteps (must match training)
- `--tgcn_hidden_size`: Hidden size for temporal GCN (must match training)
- `--s_heads`: Number of spatial attention heads (must match training)
- `--t_heads`: Number of temporal attention heads (must match training)

**Evaluation Flags:**
- `--catchment_relationship`: Include if model was trained with catchment relationships
- `--target_only`: Include if model was trained with target-only nodes
- `--use_distance`: Include if model was trained with distance information

## Model Options

The code supports multiple models:
- `hydrogat`: HydroGAT (proposed model)
- `stgcnwave`: STGCN-Wave baseline
- `rgcn`: Recurrent GCN baseline
- `dcrnn`: DCRNN baseline
- `graphwavenet`: GraphWaveNet baseline
- `gcrnn`: GCRNN baseline

Use `--model <model_name>` to select the model.

## Additional Options

For a complete list of training and evaluation options:

```bash
python src/dist_train.py --help
```

Key options include:
- `--input_steps`: Number of input timesteps (default: 72)
- `--output_steps`: Number of output timesteps to predict (default: 12, but paper uses 72)
- `--tgcn_hidden_size`: Hidden size for temporal GCN (default: 32)
- `--s_heads`: Number of spatial attention heads for GAT (default: 2)
- `--t_heads`: Number of temporal attention heads for Transformer (default: 2)
- `--learning_rate`: Learning rate (default: 0.001, but automatically set to 0.01 for hydrogat model)
- `--batch_size`: Batch size (default: 8)
- `--epochs`: Number of training epochs (default: 30, we use 100)
- `--catchment_relationship`: Use catchment relationship edges
- `--target_only`: Only use target nodes
- `--use_distance`: Use distance information for edges
