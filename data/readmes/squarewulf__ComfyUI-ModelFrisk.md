# ComfyUI-ModelFrisk

A custom node/plugin for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that automatically detects and fixes missing model paths in your workflow.

## Features

- **Auto-Location**: Scans your loaded workflow for nodes with missing models (red nodes).
- **Exact Match Fix**: If the model exists in a different folder (e.g., moved from `models/loras` to `models/loras/flux`), it automatically updates the path.
- **Fuzzy Match**: If an exact match isn't found, it looks for similar filenames (e.g. typos or version name changes) and prompts you with a "Near Match" selection dialog.
- **Batch Processing**: Fix all missing models in one click.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/squarewulf/ComfyUI-ModelFrisk.git
    ```
2.  Restart ComfyUI.

## Usage

1.  Open ComfyUI and load a workflow.
2.  **Right-click** anywhere on the empty workspace background.
3.  Select **"Frisk & Fix Models"** from the context menu.
4.  If missing models are found, a dialog will appear showing what was fixed or asking for confirmation on near matches.


