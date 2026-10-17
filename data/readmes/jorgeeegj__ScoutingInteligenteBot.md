# ScoutingInteligenteBot  

**Public portfolio release · Multi-agent RAG system for football scouting**

ScoutingInteligenteBot is an end-to-end AI system for football scouting. It combines vector retrieval, deterministic filtering and statistical scoring with LLM-generated explanations and automated visualizations, exposed through a Telegram bot interface.

The project started as my MSc thesis and evolved into a productized side project focused on reliable AI system design: each stage has a clear responsibility, and the LLM explains the output but does not decide the ranking.

<p align="center">
    <img src="figuras/Logo.PNG" alt="Logo del proyecto" width="400">
</p>

---

## Public release note



This repository is a **public, data-free portfolio release** of the system.



It includes the application architecture, ETL structure, multi-agent pipeline, scoring logic, visualization modules, Docker setup and Telegram bot integration.



It does **not** include:



* raw third-party player data,

* the private local data snapshot,

* processed player databases,

* generated FAISS indices,

* API keys, bot tokens or private environment files.



The original system was developed and validated on a private local snapshot of **14,508 players** as of **2026-04-01**: **13,020 outfield players** and **1,488 goalkeepers**. That snapshot is not redistributed in this repository because the underlying data comes from third-party sources.



To run the system end-to-end, you must provide your own authorized data and generate compatible processed databases and FAISS indices.



Active private development may continue separately beyond this public release.



---



## What the system does



A scout can ask a natural-language query such as:



> “Right-footed U23 right winger, strong in dribbling and crossing, max market value 500k, less than two years left on contract”



The system then:



1. retrieves a broad candidate pool using FAISS and multilingual embeddings;

2. applies hard filters for explicit constraints such as age, position, market value, foot, height, contract, league and nationality;

3. scores candidates using deterministic statistical logic based on percentiles, minutes and league coefficients;

4. generates a natural-language explanation of the Top-3 candidates;

5. produces comparative radar charts and individual player profile visualizations.



The ranking is produced by deterministic scoring logic. The LLM is used for explanation, not for deciding the final ranking.



---



## System architecture



The system follows a retrieval → filtering → scoring → explanation → visualization pipeline:

<p align="center">
  <img src="figuras/grafo_pipeline_compacto.png" alt="Pipeline LangGraph" width="700"/>
</p>

---

## Core components:

* **LangGraph** for multi-agent orchestration.

* **FAISS** for vector retrieval.

* **SentenceTransformers** with multilingual embeddings.

* **Polars** for dataframe processing.

* **OpenAI API** for natural-language explanations.

* **Plotly** and **mplsoccer** for radar/player profile visualizations.

* **Docker / Docker Compose** for reproducible execution.

* **Telegram Bot API** as the user interface.



---



## Repository structure



```text

ScoutingInteligenteBot/

├── data/                 # Local data folder, not versioned

│   ├── processed/

│   │   ├── merged/       # Expected processed player databases

│   │   └── indices/      # Expected FAISS indices + metadata

├── src/

│   ├── scouting/

│   │   ├── etl/          # ETL, merge, enrichment and indexing modules

│   │   └── agents/       # Multi-agent pipeline implementation and Telegram integration



├── figuras/              # README and demo images

├── .env.example          # Environment variable template

├── docker-compose.yml

├── Dockerfile

├── pyproject.toml

└── README.md

```



---



## Data availability



This repository does not ship with the player database or generated FAISS indices.



Expected local files for an end-to-end run:



```text

data/

├─ processed/

│  ├─ merged/

│  │  ├─ db_jugadores.json

│  │  └─ db_porteros.json

│  └─ indices/current/

│     ├─ faiss_jugadores.index

│     ├─ faiss_porteros.index

│     ├─ metadata_jugadores.json

│     └─ metadata_porteros.json

```



These files must be generated from your own authorized data sources or adapted from your own internal databases.



The ETL modules included in `src/scouting/etl/` document the data engineering approach used by the system: collection, normalization, identity matching, merge and FAISS indexing. They are provided as a reference implementation that can be adapted to compatible datasets.



Users are responsible for complying with the terms of service, licensing conditions and legal requirements of any data provider they use.



---



## Quick start



### 1. Clone the repository



```bash

git clone https://github.com/jorgeeegj/ScoutingInteligenteBot.git

cd ScoutingInteligenteBot

cp .env.example .env

```



Edit `.env` with your own credentials:



```bash

OPENAI_API_KEY=...

TELEGRAM_BOT_TOKEN=...

```



### 2. Build the Docker image



```bash

docker compose build --no-cache --pull

```



### 3. Provide local data



The bot expects processed databases and FAISS indices under:



```text

data/processed/merged/

data/processed/indices/current/

```



These files are not included in the public repository.



### 4. Run the bot



```bash

docker compose up -d bot

docker compose logs -f bot

```



Then send a scouting query to your Telegram bot, for example:



> “Extremo izquierdo joven, habilidoso, con regate y gol. Precio máximo 500k”



---



## ETL overview



The ETL layer is included to show how the system was designed and how compatible data can be prepared.



Main stages:



1. **Collection**

   Source-specific collectors gather player statistics, identity fields, market information and contract-related attributes.



2. **Merge and identity matching**

   Records from different sources are cleaned, normalized and matched without relying on a single shared ID. The matching logic combines names, dates of birth, height, dominant foot, teams, leagues and other identity signals.



3. **Vector indexing**

   Player metadata is embedded and indexed in FAISS for broad semantic retrieval.



4. **Runtime query pipeline**

   At runtime, the bot does not fetch live data. It queries the local processed snapshot and indices.



Typical commands:



```bash

# Full ETL pipeline

docker compose run --rm etl python -m scouting.etl.main_etl



# Merge data

docker compose run --rm etl python -m scouting.etl.merge_data



# Build FAISS indices

docker compose run --rm etl python -m scouting.etl.vector_store_indexing

```



The exact collectors may require maintenance as websites, APIs and data providers change.



For professional or production use, the recommended path is to adapt the schema and transformation logic to your own authorized data sources or internal databases.



<p align="center">
  <img src="figuras/diagrama.png" alt="ETL pipeline" width="700"/>
</p>

---



## Multi-agent pipeline



The core implementation lives in `src/scouting/agents/`.



```text

src/scouting/agents/

├── agent0.py        # Vector Retriever

├── agent1.py        # Hard Filter

├── agent2.py        # Score Evaluator

├── agent3/          # LLM Explanation layer

├── agent4/          # Visualization / report compositor

├── common.py        # Shared contracts, config and utilities

├── pipeline.py      # LangGraph multi-agent pipeline

└── telegram_bot.py  # Telegram polling interface

```



### Agent 0 · Vector Retriever



Retrieves a broad candidate pool from FAISS using multilingual embeddings.



Main responsibilities:



* encode the normalized scouting query;

* search separate FAISS indices for outfield players and goalkeepers;

* return a Polars dataframe with structured player metadata;

* preserve enough recall for later deterministic filtering.



Default retrieval is intentionally broad so that hard filters and scoring can operate on a large candidate set.



### Agent 1 · Hard Filter



Applies explicit constraints from the query.



Supported filter families include:



* age,

* position,

* market value,

* dominant foot,

* height,

* contract duration,

* nationality,

* league and country of league.



This stage is deterministic and exists to enforce hard user constraints before ranking.



### Agent 2 · Score Evaluator



Ranks the filtered candidates using statistical logic.



The scoring layer combines:



* query-relevant metric selection,

* percentiles and per-90 values,

* minutes-aware adjustments,

* league coefficients,

* role-specific metric profiles.



The LLM does not rank players. Ranking is produced by this deterministic scoring layer.



### Agent 3 · Explanation



Generates a professional natural-language scouting explanation for the selected candidates.



The explanation agent receives structured evidence from Agent 2 and writes a user-facing report in the language of the original query.



It is constrained to explain the available data rather than invent new attributes.



### Agent 4 · Visualizations



Generates comparative visual outputs:



* radar charts for selected key metrics,

* per-90 radar comparisons,

* player profile visualizations,

* report-ready image artifacts for Telegram.



Visualizations are generated with Python libraries, not by an LLM.

---



## Telegram bot



The Telegram interface uses polling and delegates each message to the LangGraph pipeline.



Run:



```bash

docker compose up -d bot

docker compose logs -f bot

```



The bot:



* reads updates through the Telegram Bot API;

* stores the last processed update ID to avoid repeated messages;

* applies an optional chat allowlist;

* sends back the scouting explanation and generated images.



Relevant environment variables:



```bash

OPENAI_API_KEY=...

TELEGRAM_BOT_TOKEN=...

OPENAI_MODEL_SUPERVISOR=gpt-4o

INDICES_DIR=/data/processed/indices/current

TELEGRAM_ALLOWED_CHAT_IDS=

TELEGRAM_ALLOWED_CHAT_IDS_FILE=

TELEGRAM_ALLOW_ALL=0

```



---



## 🖼️ Demo


Example real interaction through Telegram:

<p align="center">
  <img src="figuras/telegram_output.png" alt="Interfaz real de Telegram con la explicación del Agente 3" width="700"/>
</p>

Comparative radar chart:

<p align="center">
  <img src="figuras/radar_comparativo.png" alt="Radar comparativo" width="700"/>
</p>

Individual player profile visualizations:

<p align="center">
  <img src="figuras/player_radars.png" alt="Radar perfiles" width="700"/>
</p>

The demo shows how a natural-language scouting query is transformed into:



1. a reasoned Top-3 of player candidates;

2. a natural-language scouting explanation;

3. comparative radar charts;

4. individual player profile visualizations.



---



## Troubleshooting



### PNG generation / Kaleido error



Check that Chrome or Chromium is available inside the container:



```bash

docker compose exec bot sh -lc 'which google-chrome-stable || which google-chrome || which chromium || which chromium-browser'

```



If no browser is found, rebuild the image.



### The bot repeats the same message



Check that `/data/last_update_id.txt` exists and that the `./data:/data` volume is mounted.



### No candidates are returned



Check that:



* processed databases exist under `data/processed/merged/`;

* FAISS indices and metadata exist under `data/processed/indices/current/`;

* metadata files contain the fields expected by the filtering and scoring layers.



### WSL / Docker Desktop issue on Windows



```bash

wsl --shutdown

```



Then reopen Docker Desktop.



---



## Security and privacy



This repository intentionally excludes:



* `.env` files,

* API keys,

* Telegram bot tokens,

* private chat IDs,

* raw data,

* processed player databases,

* generated FAISS indices.



Use `.env.example` as a template and keep real credentials local.



---



## License



This project is released under the MIT License. See [LICENSE](LICENSE).



---



## Author



Developed by **Jorge Gómez Jerez** as a public portfolio release of an end-to-end AI scouting system.



GitHub: [github.com/jorgeeegj](https://github.com/jorgeeegj)

