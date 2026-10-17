<p align="center">
  <img src="logo.png" alt="CosmicWatch Logo" width="200"/>
</p>

<h1 align="center">CosmicWatch</h1>

<p align="center">
  <strong>Real-Time Earth & Space Monitoring Platform</strong><br>
  AI-powered intelligence dashboard combining NASA satellite data, machine learning, and interactive visualizations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-blue?logo=python&logoColor=white" alt="Python 3.11+"/>
  <img src="https://img.shields.io/badge/Dash-4.0-00b4d8?logo=plotly&logoColor=white" alt="Dash 4.0"/>
  <img src="https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML%20Pipeline-f7931e?logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/NASA-Open%20Data-e03c31?logo=nasa&logoColor=white" alt="NASA Open Data"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"/>
</p>

---

CosmicWatch is a full-stack data intelligence platform that ingests, processes, and visualizes real-time data from multiple NASA sources. It uses **machine learning pipelines** to classify exoplanets, score asteroid risk, detect trajectory anomalies, forecast wildfire activity, and generate unified threat reports — all through an interactive dark-theme dashboard.

<p align="center">
  <img src="screenshots/1.png" alt="CosmicWatch Home" width="100%"/>
</p>

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Architecture](#architecture)
- [AI & Machine Learning Pipeline](#ai--machine-learning-pipeline)
- [Data Sources](#data-sources)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Planet Explorer
Analyze **5,000+ confirmed exoplanets** from the NASA Exoplanet Archive. The AI pipeline computes an Earth Similarity Index (ESI) for every planet, runs KMeans clustering to group similar worlds, and flags anomalies with DBSCAN — helping you discover which distant planets are most like Earth.

- Vectorized ESI computation across all known exoplanets
- ML-based habitability classification (KMeans + DBSCAN)
- Interactive HR Diagram, ESI scatter plots, 3D cluster visualization
- Planet-vs-Earth radar comparison chart
- Filter by habitability class, discovery method, temperature, and ESI range

### Asteroid Tracker
Monitor **near-Earth objects** using JPL's Close Approach and Sentry Risk APIs. Each asteroid gets a composite risk score computed from proximity, size, velocity, and impact probability — with an Isolation Forest model flagging trajectory anomalies that deviate from expected orbital patterns.

- Composite risk scoring: `0.35 × proximity + 0.30 × size + 0.20 × velocity + 0.15 × probability`
- Isolation Forest anomaly detection on trajectory features
- 3D orbital visualization of close approaches
- Risk heatmap (distance vs. velocity), timeline, and distribution charts
- Object Detail Inspector with full orbital parameters

### Wildfire Tracker
Track **49,000+ active fire detections** worldwide using NASA FIRMS satellite data. The pipeline classifies fire intensity, maps detections by region, and runs ARIMA time-series forecasting to predict fire activity 7 days ahead — with CUSUM changepoint detection to flag sudden shifts in wildfire behavior.

- Live satellite fire detection map (MODIS/VIIRS)
- ARIMA(2,1,2) forecasting with 95% confidence intervals
- CUSUM changepoint detection for trend shifts
- Intensity classification (Very Low → Extreme) based on Fire Radiative Power
- Filter by region, confidence, FRP, date range, day/night, and intensity

### Space Report
A unified threat assessment that runs all three modules simultaneously, correlates findings across domains, and generates a single intelligence briefing with threat scores, cross-module correlations, and prioritized alerts.

- One-click report generation across all modules
- Per-module threat scoring with color-coded bar chart
- Cross-module temporal correlation analysis
- Prioritized alert feed with severity badges
- Unified threat level classification (LOW → CRITICAL)

---

## Screenshots

### Planet Explorer — Exoplanet Habitability Analysis
<p align="center">
  <img src="screenshots/light.png" alt="Planet Explorer" width="100%"/>
</p>

> ESI scatter plots, HR diagrams, discovery timelines, 3D cluster visualization, and planet-vs-Earth radar comparison. Filters let you drill into habitability class, discovery method, temperature range, and ESI score.

### Asteroid Tracker — Near-Earth Object Risk Radar
<p align="center">
  <img src="screenshots/3.png" alt="Asteroid Tracker" width="100%"/>
</p>

> Composite risk assessment for every tracked NEO. Includes 3D orbital plots, risk heatmaps, Isolation Forest anomaly flags, and a detailed Object Inspector with full orbital parameters.

### Wildfire Tracker — Global Fire Monitoring
<p align="center">
  <img src="screenshots/4.png" alt="Wildfire Tracker" width="100%"/>
</p>

> Real-time satellite fire map, regional breakdowns, intensity distribution, date-region heatmaps, ARIMA forecasting with changepoint detection. Filter by region, confidence, FRP threshold, and more.

### Space Report — Unified Threat Assessment
<p align="center">
  <img src="screenshots/5.png" alt="Space Report" width="100%"/>
</p>

> Combined intelligence briefing with module summaries, threat score chart, cross-module correlations, and a prioritized alert feed. One click generates the full report.

### Loading Experience & Dark/Light Theme
<p align="center">
  <img src="screenshots/loading.png" alt="Loading Screen" width="100%"/>
</p>

> Smooth loading screens with progress bars while data pipelines run. Full dark and light theme support with automatic persistence.

---

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    CosmicWatch Platform                   │
├──────────┬──────────┬──────────┬─────────────────────────┤
│  Dash    │ FastAPI  │ Rich CLI │   Scheduled Jobs        │
│ Dashboard│ REST API │ Terminal │   (APScheduler)         │
├──────────┴──────────┴──────────┴─────────────────────────┤
│              Correlation Engine & Threat Matrix           │
├──────────────────────────────────────────────────────────┤
│   Planet Explorer  │  Asteroid Tracker  │ Wildfire Tracker│
│   ─────────────    │  ────────────────  │ ────────────── │
│   ESI Computation  │  Risk Scoring      │ ARIMA Forecast │
│   KMeans Clusters  │  Isolation Forest  │ CUSUM Detect   │
│   DBSCAN Anomaly   │  Orbital Mechanics │ Geospatial Map │
├──────────────────────────────────────────────────────────┤
│           ML Ensemble │ Feature Store │ Pipelines        │
├──────────────────────────────────────────────────────────┤
│      Data Layer: httpx Downloader │ SQLite Cache │ Store │
├──────────────────────────────────────────────────────────┤
│  NASA Exoplanet   │  JPL CNEOS/Sentry  │  NASA FIRMS    │
│  Archive (TAP)    │  (Close Approach)   │  (MODIS/VIIRS) │
└──────────────────────────────────────────────────────────┘
```

### Plugin-Based Module System
Each data module (exoplanet, NEO, wildfire) is self-contained with its own ETL pipeline, ML models, and visualizations. Modules self-register via a plugin registry, communicate through an async event bus, and feed into the unified correlation engine.

### ETL Pipeline Design
Every module follows a 4-stage pipeline: **Extract → Validate → Transform → Load**

1. **Extract** — Download raw data from NASA APIs (httpx with progress tracking)
2. **Validate** — Remove nulls, deduplicate, enforce ranges, coerce types
3. **Transform** — Compute derived features, run ML models, classify results
4. **Load** — Cache processed DataFrames in memory + persist to disk

---

## AI & Machine Learning Pipeline

CosmicWatch uses AI and machine learning throughout its data processing pipeline — not as an afterthought, but as the core intelligence layer that transforms raw NASA data into actionable insights.

### Data Cleaning & Preprocessing

Raw NASA datasets are messy: missing values, inconsistent units, duplicates, and outlier noise. The pipeline handles this automatically:

- **Missing value imputation** — Median fill for numerical features (radius, mass, temperature) to preserve distribution shape without introducing bias
- **Type coercion** — Automatic conversion of mixed-type columns to numeric with error handling
- **Duplicate removal** — Deduplication by primary key (planet name, asteroid designation) keeping canonical entries
- **Range validation** — Physical constraint checks (latitude ±90°, longitude ±180°, positive radius/mass)
- **Outlier filtering** — DBSCAN-based anomaly detection removes physically impossible values before downstream analysis
- **Feature engineering** — Derived columns computed from raw data: bulk density from mass/radius, escape velocity, habitable zone boundaries, fire intensity categories

### Earth Similarity Index (ESI) — Vectorized Computation

The ESI quantifies how similar an exoplanet is to Earth on a 0-1 scale. The formula is computed across **all 5,000+ planets simultaneously** using NumPy vectorized operations:

```
ESI = ∏ (1 - |x_i - x_earth| / (x_i + x_earth)) ^ (w_i / n)
```

| Parameter | Earth Value | Weight |
|---|---|---|
| Radius | 1.0 R⊕ | 0.57 |
| Bulk Density | 5.51 g/cm³ | 1.07 |
| Escape Velocity | 11.186 km/s | 0.70 |
| Surface Temperature | 288 K | 5.58 |

Density and escape velocity are **estimated from observable properties** (mass, radius) when not directly available — enabling ESI computation even for planets with incomplete data.

### Unsupervised Classification (KMeans + DBSCAN)

```
Raw Features → StandardScaler → KMeans(k=6) → Cluster Labels
                                     ↓
                              DBSCAN(eps=1.5) → Anomaly Flags
```

- **KMeans (k=6)** groups planets into natural categories based on radius, mass, temperature, orbital period, and stellar properties
- **DBSCAN** identifies outlier planets that don't fit any cluster — these are flagged as potentially interesting anomalies worth investigating
- Features are standardized with `StandardScaler` before clustering to prevent scale dominance

### Asteroid Risk Scoring

Each near-Earth object receives a composite risk score:

```
Risk = 0.35 × Proximity + 0.30 × Size + 0.20 × Velocity + 0.15 × Impact Probability
```

Components are min-max normalized to [0, 1]. Risk levels: **CRITICAL** (≥0.75), **HIGH** (≥0.50), **MODERATE** (≥0.25), **LOW** (<0.25).

### Isolation Forest Anomaly Detection

```
Trajectory Features → StandardScaler → IsolationForest(n=100, contamination=5%)
                                              ↓
                                     Anomaly Score [-1, 1]
```

Detects asteroids with unusual trajectory characteristics (unexpected distance-velocity combinations, unusual orbital parameters) that may warrant closer observation. Uses 100 estimators with 5% expected contamination rate.

### ARIMA Time-Series Forecasting

```
Daily Fire Counts → ARIMA(2,1,2) → 7-Day Forecast + 95% CI
                         ↓
                  CUSUM Changepoint Detection → Trend Shift Alerts
```

- **ARIMA(2,1,2)** model trained on daily fire count time series
- Produces 7-day ahead forecasts with confidence intervals
- **CUSUM** (Cumulative Sum Control Chart) detects sudden shifts in fire activity — useful for identifying emerging wildfire crises before they escalate

### Ensemble Classifier

```
Features → StandardScaler → VotingClassifier(soft) → Prediction
                                    ├── RandomForest(100 trees)
                                    ├── GradientBoosting(100 estimators)
                                    └── LogisticRegression
```

Soft voting combines probability estimates from three diverse models, providing more robust predictions than any single algorithm.

---

## Data Sources

All data comes from official NASA open-data APIs — **no API key required** for the bulk download approach:

| Source | API | Data |
|---|---|---|
| [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/) | TAP Sync Service | 5,000+ confirmed exoplanets with planetary and stellar properties |
| [JPL CNEOS](https://cneos.jpl.nasa.gov/) | Close Approach API | Near-Earth object close approaches within 0.05 AU |
| [JPL Sentry](https://cneos.jpl.nasa.gov/sentry/) | Sentry Risk API | Impact probability assessments for potentially hazardous asteroids |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) | Active Fire Data | Global fire detections from MODIS and VIIRS satellites |

Data is downloaded once and cached locally. The scheduler can refresh datasets every 6 hours automatically.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Plotly Dash 4, Plotly.js, Dash Bootstrap Components |
| **API** | FastAPI, Uvicorn, Pydantic |
| **ML/AI** | scikit-learn (KMeans, DBSCAN, IsolationForest, RandomForest, GradientBoosting, VotingClassifier) |
| **Forecasting** | statsmodels (ARIMA), CUSUM changepoint detection |
| **Data** | pandas, NumPy, httpx, SQLAlchemy, SQLite |
| **CLI** | Typer, Rich (tables, progress bars, panels) |
| **Config** | Pydantic Settings, PyYAML, structlog |
| **Scheduling** | APScheduler (6h data refresh, 24h report generation) |
| **Visualization** | Plotly (scatter, 3D, heatmaps, radar), Folium (geo maps) |

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip or uv package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/aymenhmaidiwastaken/cosmicwatch.git
cd cosmicwatch

# Install dependencies
pip install -e ".[dev]"

# Download all NASA datasets
cosmicwatch download all
```

### Quick Start

```bash
# Launch the dashboard
cosmicwatch serve

# Open in browser
# Dashboard: http://localhost:8050/dashboard/
# API:       http://localhost:8000/docs
```

---

## Usage

### Dashboard

Navigate to `http://localhost:8050/dashboard/` after starting the server. The home page shows all four modules — click any card to explore.

### CLI Commands

```bash
# Download datasets
cosmicwatch download all          # Download all datasets
cosmicwatch download exoplanet    # Download exoplanet data only
cosmicwatch download neo          # Download NEO data only
cosmicwatch download wildfire     # Download wildfire data only

# Run analysis
cosmicwatch exoplanet classify    # Run exoplanet classification pipeline
cosmicwatch neo scan              # Run NEO risk assessment
cosmicwatch wildfire monitor      # Run wildfire monitoring

# Generate reports
cosmicwatch report cosmic-weather # Generate unified Space Report

# Start services
cosmicwatch serve                 # Start API + Dashboard

# Check status
cosmicwatch status                # Show data availability and system status
```

### Makefile

```bash
make install    # Install package
make dev        # Install with dev dependencies
make test       # Run test suite
make lint       # Check code quality
make format     # Format code
make download   # Download all datasets
make serve      # Start services
make clean      # Remove all data and cache
```

### REST API

The FastAPI server exposes endpoints for each module:

```
GET  /api/v1/exoplanet/summary     # Exoplanet analysis summary
GET  /api/v1/neo/summary           # NEO risk assessment
GET  /api/v1/wildfire/summary      # Wildfire monitoring data
GET  /api/v1/correlation/report    # Unified Space Report
GET  /api/v1/health                # Health check
```

Full interactive docs at `http://localhost:8000/docs`.

---

## Project Structure

```
cosmicwatch/
├── pyproject.toml                 # Package config & dependencies
├── Makefile                       # Development commands
├── config/
│   ├── default.yaml               # App configuration
│   └── regions.yaml               # Geographic region definitions
├── data/                          # Downloaded datasets (gitignored)
│   ├── raw/                       # Original NASA data files
│   ├── processed/                 # Cleaned & transformed data
│   └── cache.sqlite               # Query cache
├── src/nasa_sentinel/
│   ├── app.py                     # Application factory
│   ├── core/                      # Config, logging, registry, events
│   ├── data/                      # Downloader, cache, ETL pipeline base
│   ├── modules/
│   │   ├── exoplanet/             # ESI computation, KMeans, DBSCAN
│   │   ├── neo/                   # Risk scoring, Isolation Forest
│   │   └── wildfire/              # ARIMA forecast, CUSUM, geospatial
│   ├── correlation/               # Cross-module analysis, threat matrix
│   ├── ml/                        # Ensemble classifier, feature store
│   ├── api/                       # FastAPI routers & middleware
│   ├── dashboard/                 # Plotly Dash layouts & callbacks
│   ├── cli/                       # Typer CLI commands
│   ├── reports/                   # Jinja2 report templates
│   └── scheduler/                 # APScheduler jobs & alerts
├── tests/                         # pytest test suite
└── screenshots/                   # Dashboard screenshots
```

---

## Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run the test suite (`make test`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built by <a href="https://github.com/aymenhmaidiwastaken">@aymenhmaidiwastaken</a>
</p>

