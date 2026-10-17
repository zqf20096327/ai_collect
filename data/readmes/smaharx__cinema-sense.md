# 🎬 Cinema-Sense
 
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AI](https://img.shields.io/badge/AI-HuggingFace%20%7C%20FAISS-orange)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-lightgrey)
![Status](https://img.shields.io/badge/Version-v2.0.0--beta-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A high-performance semantic movie recommendation engine powered by deep learning and vector similarity search. The system understands the actual *meaning* behind a user's search query, bypassing traditional keyword-matching limitations to deliver instant, highly relevant movie suggestions through a sleek dark-mode UI.

---

## Overview

Traditional search engines rely on exact text matches (e.g., searching for "alien" only returns movies with the exact word "alien"). Cinema-Sense elevates the search experience by utilizing dense vector embeddings. 

The system passes movie metadata through a HuggingFace Transformer model to compress contextual meaning into a 384-dimensional mathematical space. When a user searches for something like *"a bank heist in space"*, the engine converts the query, uses Facebook's AI Similarity Search (FAISS) to instantly find the closest mathematical neighbors, and safely passes them through strict Pandas data filters before asynchronously fetching movie posters for the UI.

---

## Key Features

* **Semantic Context Search:** True NLP understanding via HuggingFace's `all-MiniLM-L6-v2` transformer model.
* **Millisecond Retrieval:** Lightning-fast nearest-neighbor calculations using a FAISS vector database.
* **Smart Over-Fetching Architecture:** Retrieves deep data pools prior to filtering to eliminate "filter starvation" on strict year/rating queries.
* **Asynchronous API Integration:** Parallel thread-pooling for TMDb API calls, ensuring zero-lag poster rendering in the UI.
* **RAM-Optimized Engine:** `@st.cache_resource` integration loads the 5,000+ vector map into memory once, enabling instant consecutive searches.

---

## System Architecture

The application relies on a decoupled data ingestion pipeline and a highly optimized runtime engine:

1. **Presentation Layer** — Streamlit UI handling state management and async image rendering.
2. **Hybrid Engine Layer** — Coordinates vector translation, FAISS retrieval, and deterministic Pandas filtering.
3. **Machine Learning Layer** — HuggingFace sentence-transformers.
4. **Data Access Layer** — FAISS Index (`.faiss`) and serialized DataFrames (`.pkl`).

*(For an in-depth breakdown of the dense vector pipeline and math flow, see [ARCHITECTURE.md](ARCHITECTURE.md))*

---

## Technology Stack

| Component             | Technology              |
| --------------------- | ----------------------- |
| Programming Language  | Python                  |
| Web Framework         | Streamlit               |
| Deep Learning Model   | HuggingFace (BERT)      |
| Vector Database       | FAISS (CPU)             |
| Data Manipulation     | Pandas, NumPy           |
| External API          | TMDb (The Movie DB)     |

---

## Project Structure

```text
CINEMA-SENSE/
│
├── requirements.txt       # Direct Python dependencies
├── README.md              # Project documentation and setup
├── ARCHITECTURE.md        # System design and data flow details
├── .env.example           # API key template
│
├── data/                  # Local database storage (Git-ignored)
│   ├── processed/         # Serialized Pandas Dataframes (.pkl)
│   └── vector_db/         # Compiled FAISS index maps (.faiss)
│
└── src/                   # Application Source Code
    ├── app.py             # Main Streamlit UI entry point
    ├── data_pipeline/     # Ingestion and HuggingFace vectorization scripts
    ├── models/            # Core Hybrid Engine (Search & Filter logic)
    └── utils/             # Async API networking and helpers
```
## Installation

Clone the repository:

git clone [https://github.com/smaharx/cinema-sense.git](https://github.com/smaharx/cinema-sense.git)

cd cinema-sense    

Set up a virtual environment and install dependencies:

python -m venv .venv

# Activate on Windows:
.venv\Scripts\activate
# Activate on Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt

## Configuration
The application requires an API key to fetch live movie posters.

  1. Locate the .env.example file in the root directory.

  2. Duplicate it and rename the copy to .env.

  3. Add your free TMDb API key inside:
     TMDB_API_KEY=your_actual_api_key_here

## Building the Vector Database (Initial Setup)
Because GitHub limits file sizes, the massive .pkl and .faiss vector maps are not included in the repository. You must generate them locally before running the app.

Run the preprocessor pipeline to download, vectorize, and map the dataset:

python src/data_pipeline/preprocessor.py

## Running the Application

Once the vector database is built, boot up the UI dashboard:

streamlit run src/app.py

## Future Improvements (V3.0 Roadmap)

- **Cloud Deployment**: Pushing the application live via Streamlit Community Cloud.
- **Docker Containerization**: Writing a Dockerfile for OS-agnostic deployment.
- **Cloud Vector DB**: Migrating from local FAISS to a serverless Pinecone or Weaviate architecture.
- **Production Logging**: Replacing standard output with Python's logging module for robust error tracking.

## Authors

- **Shahzaib Mahar** (https://github.com/smaharx)

## License

This project is licensed under the MIT License. See the LICENSE file for details.


