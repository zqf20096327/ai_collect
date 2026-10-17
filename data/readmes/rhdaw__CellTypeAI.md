# CellTypeAI: Automated cell identification for scRNA-seq using local generative-AI

CellTypeAI, a streamlined, scalable program developed to perform context-dependent cell identification in scRNA-seq datasets, which leverages locally-run LLMs with enhanced RAG methods and optional ensemble methods.

CellTypeAI builds upon local LLM hosting technol-ogies and integrates directly into scanpy-based scRNA-seq analysis pipelines to enable accurate cell type identification of pre-clustered scRNA-seq data

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation
### Dev version:
```bash
#Using pip:
pip install git+https://github.com/rhdaw/celltypeai

#Using uv: 
uv add git+https://github.com/rhdaw/celltypeai

# Navigate into the directory to install requirements from .toml
cd CellTypeAI
pip install .

# Or using uv:
uv pip install -r pyproject.toml
```

### pip installation
```bash
pip install celltypeai
#or
uv add celltypeai
```

## Usage
### Ollama Requirements:
- Install Ollama (https://ollama.com/)
- Pull model of choice (https://ollama.com/search), i.e:
```bash
ollama pull phi4:14b
```
- Initialise ollama server via **ollama serve** in terminal / powershell
```bash
ollama serve
```

### Running CellTypeAI
Following standard scRNA-seq processing with **leiden** OR **louvain** clustering.
```python
import celltypeai as cta

cta.cell_annotator(
                "Human",
                "Intestine",
                adata,
                model="qwen3:32b",
                num_genes=200,
                n_iterations=3,
            )
```
On completion, annotations are stored in adata.obs["cell_type_ai"]

### `cell_annotator(adata, species, tissue, ...)`

Takes a processed `.h5ad` object, extracts Differentially Expressed Genes (DEGs) from each cluster, and utilizes a local LLM via Ollama to define and annotate cell types.

| Parameter      | Type      | Default      | Description                                                                                                                                                    |
| :------------- | :-------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`adata`**    | `AnnData` | *Required*   | Annotated data matrix containing cell clusters (Leiden or Louvain).                                                                                            |
| **`species`**  | `str`     | *Required*   | The biological species (e.g., "Human", "Mouse").                                                                                                               |
| **`tissue`**   | `str`     | *Required*   | The tissue type being analyzed. Must be one of: *Adrenal, Brain, Eye, Heart, Immune system, Intestine, Kidney, Liver, Lung, Muscle, Pancreas, Placenta, Spleen, Stomach, Thymus, Skin.* |
| `model`        | `str`     | `"phi4:14b"` | The Ollama model to use. Recommended: `"phi4:14b"`, `"qwen3:32b"`, `"qwen3:235b"`.                      |
| `num_genes`    | `int`     | `200`        | Number of top marker genes to provide to the LLM for each cluster.                                                                                             |
| `n_iterations` | `int`     | `3`          | Ensemble size. The model prompts `n` times and selects the mode (most frequent) annotation.                 |
| `verbose`      | `bool`    | `False`      | If `True`, outputs detailed logs and saves the engineered prompt to the working directory for inspection.                                                      |

**Returns:**
- `adata` (`AnnData`): The input object with a new `.obs` column containing the predicted cell types.

## Contributing

Fork the repo, create a feature branch, and submit a pull request.
Please add tests and update documentation for new features.

## License

GNU GPL-2.0 license - see LICENSE file