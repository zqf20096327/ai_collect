# 🔍 Danbooru Dataset Filter: High-Speed Metadata Explorer for AI Training

<p align="center">
  <img src="preview.png" alt="Danbooru Dataset Filter GUI Preview" width="800">

**Danbooru Dataset Filter** is a high-performance GUI toolkit designed specifically for curating and preparing AI training datasets. It allows you to filter millions of images in seconds to build the perfect training set.

---

### 🎯 Who is this for?
A must-have tool for AI researchers and model trainers working on:
*   **LoRA Training (Characters, Styles, Concepts)**
*   **Checkpoint Training (Anima / XL / Flux / etc.)**
*   **ControlNet & T2I Adapters**
*   **Computer Vision Dataset Curation**

---

### 🚀 Key Advantages
*   **Blazing Fast:** Processes millions of records using the `Polars` engine and `Parquet` storage.
*   **Quality Filtering:** Sort and filter by Score, Favorites, Date, and Rating (SFW/NSFW) to ensure high-quality training data.
*   **Composition Control:** Filter by Aspect Ratio (Portrait, Landscape, Square) for optimal batch bucket training.
*   **Data Integrity:** Built-in MD5 deduplication to prevent overfitting—a crucial step for stable LoRA convergence.
*   **Smart Tagging:** Integrated tag dictionary with autocomplete and color-coded categories (Artist, Character, Copyright, General).
*   **Scale Estimation:** Real-time dataset size calculation (GB/MB) to plan your storage and training steps.

---

### 🛠 Core Features
1.  **Advanced Tag Logic:** Flexible Include/Exclude (Blacklist) system with multi-line support.
2.  **Quality Thresholds:** Set minimum Score or Favorite counts to filter out "low-effort" artwork.
3.  **Visual Preview:** High-speed data table with color-coded tags for easy content verification.
4.  **Batch Export:** Export direct image URLs to `.txt` for seamless downloading.
5.  **Modern UI:** Dark-themed interface optimized for long curation sessions.

---

### 📦 Installation & Setup

#### Option 1: Automated Setup (Recommended for Windows)
The easiest way to get started is to use the provided batch files. 

1.  **Run `setup.bat`**: This script performs a full one-click installation:
    *   **Virtual Environment**: Creates an isolated `.venv` folder to keep your system clean.
    *   **Dependencies**: Installs `polars`, `pyarrow`, and `PyQt6` automatically.
    *   **Data Download**: Creates a `/data` folder and uses `curl` to fast-download the latest database and tag dictionary (~4GB) from Hugging Face.
2.  **Run `run_app.bat`**: Launches the application instantly using the virtual environment.

---

#### Option 2: Manual Installation
If you prefer to set up everything manually (e.g., on Linux or macOS):

1.  **Environment & Libraries**:
    ```bash
    pip install polars pyarrow PyQt6
    ```
2.  **Download Metadata**:
    Visit the [danbooru-2026-clean-metadata](https://huggingface.co/datasets/ThetaCursed/danbooru-2026-clean-metadata) repository and download these files:
    *   [`danbooru2026_clean.parquet`](https://huggingface.co/datasets/ThetaCursed/danbooru-2026-clean-metadata/resolve/main/danbooru2026_clean.parquet?download=true)
    *   [`tags_dictionary.parquet`](https://huggingface.co/datasets/ThetaCursed/danbooru-2026-clean-metadata/resolve/main/tags_dictionary.parquet?download=true)
3.  **File Structure**:
    Place the files into a folder named `data` in the script's root directory:
    ```text
    /your-project-folder
    ├── data/
    │   ├── danbooru2026_clean.parquet
    │   └── tags_dictionary.parquet
    ├── main.py
    └── ...
    ```
4.  **Run the App**:
    ```bash
    python main.py
    ```
---

### 🛠 Tech Stack
*   **GUI:** PyQt6
*   **Data Engine:** Polars (Lightning-fast DataFrame library)
*   **Storage Format:** Apache Parquet