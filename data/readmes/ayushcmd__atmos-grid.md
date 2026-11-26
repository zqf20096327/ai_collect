# AtmosGrid
### Mapping India's Atmosphere from Space

<p align="center">
  <strong>Satellite Intelligence | Air Quality | Atmospheric Hotspot Detection</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-AtmosGrid-FF9933?style=for-the-badge" alt="AtmosGrid"/>
  <img src="https://img.shields.io/badge/Domain-Earth%20Observation-FFFFFF?style=for-the-badge&labelColor=333333" alt="Earth Observation"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-XGBoost-138808?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/Geospatial-India-FF9933?style=for-the-badge" alt="Geospatial India"/>
</p>

<p align="center">
  An independent environmental intelligence platform combining satellite observations, ground-monitoring data, machine learning, and geospatial analytics to investigate air quality and atmospheric pollution patterns across India.
</p>

---

## Overview

AtmosGrid is a satellite-assisted environmental monitoring and research platform developed to explore two interconnected challenges: estimating surface-level air quality and identifying regions with elevated atmospheric formaldehyde (HCHO) concentrations.

The project integrates ground-level air-quality observations, Sentinel-5P/TROPOMI satellite measurements, machine learning, spatial clustering, and interactive maps into a unified application.

Its objective is to make environmental datasets more accessible, investigate the relationship between satellite observations and ground-level pollution, and develop a reproducible foundation for broader air-quality analysis across India.

The project originated as a concept developed for the **Bharatiya Antariksh Hackathon (BAH) 2026**, organized by the Indian Space Research Organisation (ISRO) with Hack2skill. The initial prototype remained local and incomplete during the hackathon. Our team participated but was not shortlisted for the Grand Finale. Development continued independently, and this repository presents the more complete implementation prepared for public release in October 2026.

**Team:** Blue Planet  
**Project:** AtmosGrid  
**Hackathon:** Bharatiya Antariksh Hackathon 2026  
**Problem Statement:** Development of Surface AQI and Identification of HCHO Hotspots over India using Satellite Data.

AtmosGrid is an independent project. Participation in BAH 2026 does not imply selection, endorsement, or official affiliation with ISRO.

## Problem Statement and Objectives

### The challenge set by ISRO

BAH 2026 Problem Statement 3 focuses on using satellite data to develop surface-level Air Quality Index (AQI) estimates and identify HCHO hotspots over India.

The challenge addresses two distinct objectives.

**Objective 1 — Surface AQI estimation and mapping**

Satellite instruments measure atmospheric properties at different spatial and vertical scales, whereas surface AQI depends on pollutant concentrations measured near the ground. Relating these measurements requires suitable ground observations, meteorological information, data alignment, modelling, and validation.

The intended outcome is a spatially informative representation of surface air quality, including regions where ground-monitoring stations are sparse.

**Objective 2 — HCHO hotspot identification**

Use satellite-derived formaldehyde column-density observations to identify spatial concentration patterns and investigate their potential relationships with biomass burning, fires, atmospheric chemistry, and meteorological transport.

This requires interpreting HCHO observations alongside relevant fire detections, environmental conditions, and temporal patterns rather than treating every hotspot as a confirmed emission source.

Official challenge reference: [Bharatiya Antariksh Hackathon 2026 — ISRO and Hack2skill](https://hack2skill.com/event/bah2026/).

### How AtmosGrid addresses the challenge

- Process and analyse real ground-monitoring observations.
- Calculate daily AQI values where the required data and completeness conditions are satisfied.
- Train and evaluate an XGBoost regression model using historical AQI observations.
- Detect elevated HCHO concentration clusters using spatial density-based clustering.
- Display monitoring stations, cluster locations, and Indian administrative boundaries on interactive maps.
- Assess data coverage across all 36 Indian states and union territories.
- Document data provenance, model performance, validation boundaries, and outstanding scientific requirements.

The current implementation establishes a working analytical foundation. It does not yet provide a scientifically validated nationwide surface-AQI prediction product.

## Dashboard

AtmosGrid includes an interactive Streamlit application for exploring the available observations, model outputs, hotspot clusters, and data-quality information.

### National geospatial overview

![AtmosGrid national geospatial overview](docs/atmosgrid-overview.png)

The overview combines available ground-monitoring stations, HCHO cluster centroids, administrative boundaries, AQI statistics, and geographic coverage information.

### Ground AQI analytics

![AtmosGrid ground AQI analytics](docs/atmosgrid-aqi-analytics.png)

Explore historical observations, actual-versus-predicted AQI, residual distributions, chronological test results, and model feature importance.

### HCHO hotspot explorer

![AtmosGrid HCHO hotspot explorer](docs/atmosgrid-hcho-explorer.png)

Inspect the three detected HCHO clusters using an interactive geographic map, cluster footprints, concentration statistics, and downloadable analytical outputs.

### Data quality and methodology

![AtmosGrid data quality and methodology](docs/atmosgrid-data-quality.png)

Review data provenance, daily observation completeness, state-level coverage, satellite-data readiness, mathematical formulations, and scientific limitations.



## Project Demonstration

The following section is reserved for the AtmosGrid walkthrough video.

**Tutorial video asset:** `public/videos/atmosgrid.mp4`

<!-- Replace VIDEO_URL with a publicly accessible video URL supported by GitHub. -->
<p align="center">
  <a href="public/videos/atmosgrid.mp4">
  </a>
</p>


For the associated web application, a file stored at `public/videos/atmosgrid.mp4` is normally accessible at `/videos/atmosgrid.mp4`. GitHub README playback requires a suitable hosted video URL; the repository-relative MP4 path alone does not guarantee inline playback.

## Current Results

The following figures are reported by the current implementation and its verification report.

| Metric | Current result |
|---|---:|
| Hourly ground observations | 70,033 |
| Ground-monitoring stations | 6 |
| States/territories with ground observations | 4 |
| Valid daily station observations | 1,542 |
| Detected HCHO clusters | 3 |
| Elevated satellite pixels in the clusters | 29 |
| Administrative territories represented | 36 |
| Automated tests passed in the reported run | 66 |

### Ground-data coverage

The current ground-monitoring network covers Delhi, Uttar Pradesh, Maharashtra, and Telangana.

The state/UT coverage report classifies the remaining 32 administrative territories as satellite-only, based on the currently available coverage assessment. **No state currently has a validated nationwide surface-AQI model classification.**

Satellite observations and ground-level AQI measurements represent different quantities and must not be treated as interchangeable.

## Surface AQI Modelling

AtmosGrid uses an XGBoost regression model trained on historical daily AQI observations.

The existing evaluation uses a chronological held-out test period from October 23 to December 31, 2024.

| Evaluation metric | Reported value |
|---|---:|
| Test MAE | 39.6 AQI |
| Test RMSE | 48.7 AQI |
| Test R² | 0.794 |
| Historical-median baseline MAE | 197.7 AQI |
| Reported MAE reduction against baseline | Approximately 80% |

The model's primary features include lagged AQI and seasonal variables. Previous-day AQI accounts for the largest share of the reported feature importance.

These metrics describe performance on the current evaluation dataset. They do not establish equivalent predictive performance across unobserved stations or across all of India. Broader station coverage and spatially independent validation are required before making nationwide surface-AQI claims.

## HCHO Hotspot Detection

AtmosGrid applies DBSCAN using Haversine great-circle distance to identify clusters of elevated Sentinel-5P/TROPOMI HCHO column-density observations.

| Cluster region | Pixel count | Mean HCHO column density |
|---|---:|---:|
| Delhi-NCR and Western Uttar Pradesh | 14 | \(2.19 \times 10^{16}\) molecules/cm² |
| Singrauli/Sonbhadra energy belt | 10 | \(1.95 \times 10^{16}\) molecules/cm² |
| Mumbai metropolitan/Western corridor | 5 | \(1.89 \times 10^{16}\) molecules/cm² |

The current clustering configuration uses a 50 km neighbourhood radius, a minimum of five samples, and a configured 90th-percentile concentration threshold.

The application provides cluster coordinates, pixel counts, mean and maximum concentrations, interactive map popups, and CSV/GeoJSON exports.

**Interpretation:** HCHO clusters indicate spatial patterns in atmospheric column density. They do not independently establish ground-level AQI, confirmed industrial emissions, or verified fire locations. Atmospheric chemistry, transport, and boundary-layer dynamics influence the observations.

## Data Sources

| Source | Purpose |
|---|---|
| OpenAQ AWS S3 Open Data Archive | Ground-monitoring observation ingestion |
| CPCB monitoring network | Ground-level pollution measurements and AQI methodology |
| Sentinel-5P/TROPOMI | Tropospheric HCHO column-density observations |
| Indian administrative boundaries | State/UT mapping and geographic coverage assessment |
| NASA FIRMS | Fire-data availability and future HCHO/fire correlation |
| MODIS MAIAC AOD | Planned satellite aerosol inputs for surface-AQI estimation |
| Copernicus ERA5 | Planned meteorological inputs, including boundary-layer height |
| Google Earth Engine | Potential satellite-data processing and acquisition |

The existing satellite benchmark and local datasets can be explored without authenticating every external provider. Full AOD and meteorological fusion, as well as completed fire-correlation analysis, remain dependent on additional data acquisition and validation.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python |
| Dashboard | Streamlit |
| Interactive charts | Plotly |
| Geospatial maps | Folium, streamlit-folium |
| Data processing | Pandas, NumPy |
| Machine learning | XGBoost, scikit-learn |
| Spatial clustering | DBSCAN, Haversine distance |
| Geographic formats | GeoJSON, CSV |
| Ground-data ingestion | OpenAQ AWS S3, DuckDB HTTPFS |
| Testing | Pytest, Streamlit AppTest |

## Architecture

```text
Ground Monitoring Data          Satellite Observations
OpenAQ / CPCB                   Sentinel-5P / TROPOMI
          |                              |
          v                              v
Data Validation                 HCHO Preprocessing
Hourly Processing               Quality Filtering
Daily AQI Calculation           Column-Density Analysis
          |                              |
          v                              v
XGBoost AQI Model               Haversine DBSCAN
Chronological Evaluation        Hotspot Clustering
          |                              |
          +--------------+---------------+
                         |
                         v
                 Processed Artifacts
               CSV / JSON / GeoJSON
                         |
                         v
                Streamlit Dashboard
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
    AQI Analytics   HCHO Explorer    Data Quality
                         |
                         v
              India Coverage Overview
```

## Repository Structure

```text
AtmosGrid/
├── backend/
│   ├── scripts/
│   │   └── expand_ground_data.py
│   ├── src/
│   │   └── data/
│   │       └── satellite_meteo_pipeline.py
│   ├── tests/
│   └── requirements.txt
├── dashboard/
│   ├── app.py
│   ├── data_loader.py
│   ├── map_utils.py
│   └── pages_impl/
│       ├── overview.py
│       ├── aqi_analytics.py
│       ├── hcho_explorer.py
│       └── data_quality.py
├── data/
│   └── processed/
│       ├── cpcb_raw_hourly.csv
│       ├── cpcb_daily_aqi.csv
│       ├── tropomi_hcho_india_benchmark.csv
│       └── india_states_simplified.geojson
├── models/
│   └── aqi_xgboost.pkl
├── outputs/
│   ├── hotspots/
│   ├── metrics/
│   └── predictions/
├── public/
│   └── videos/
│       └── atmosgrid.mp4
├── docs/
│   └── screenshots/
└── README.md
```

This structure represents the current implementation. Generated datasets and model files may not all be included in a fresh clone.

## Getting Started

### Prerequisites

- Python compatible with the pinned project dependencies.
- Git.
- Internet access for dependency installation and public basemap tiles.
- Optional credentials for external satellite and meteorological data providers.

### Installation

Clone the repository:

```powershell
git clone https://github.com/ayushcmdx/AtmosGrid.git
cd AtmosGrid
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
```

Launch the dashboard:

```powershell
streamlit run dashboard\app.py
```

Open `http://localhost:8501` in your browser.

Run the test suite:

```powershell
python -m pytest backend\tests\ -v
```

Run satellite and meteorological readiness diagnostics:

```powershell
python backend\src\data\satellite_meteo_pipeline.py
```

The ground-data acquisition workflow can be executed with:

```powershell
python backend\scripts\expand_ground_data.py
```

This acquisition script may update local datasets and requires access to its configured data source. Review the configuration and existing outputs before rerunning it.

## Scientific Limitations

AtmosGrid is an independent research and software project. Its current outputs have the following limitations:

- Ground observations cover only six monitoring stations across four states/territories.
- A validated nationwide surface-AQI prediction model is not yet available.
- Satellite atmospheric column densities cannot be directly interpreted as surface pollutant concentrations.
- HCHO hotspots are not, by themselves, proof of a particular emission source or fire.
- MODIS MAIAC AOD and ERA5 fusion require further implementation and validation.
- Fire–HCHO correlation and source-attribution analysis are not yet complete.
- The existing model requires spatially independent evaluation beyond its current chronological test.
- External data availability, credentials, observation quality, and licensing can affect reproducibility.

The dashboard distinguishes measured observations, satellite products, model predictions, and analytical outputs to avoid presenting unsupported estimates as established measurements.

## Acknowledgements and References

- [Indian Space Research Organisation (ISRO)](https://www.isro.gov.in/)
- [Bharatiya Antariksh Hackathon 2026 — Hack2skill](https://hack2skill.com/event/bah2026/)
- [OpenAQ](https://openaq.org/)
- [OpenAQ AWS Open Data](https://registry.opendata.aws/openaq/)
- [Copernicus Sentinel-5P](https://www.copernicus.eu/en)
- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)
- [Google Earth Engine](https://earthengine.google.com/)
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/)
- [Streamlit](https://streamlit.io/)
- [Folium](https://python-visualization.github.io/folium/)
- [XGBoost](https://xgboost.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)

The project draws inspiration from the scientific objectives of BAH 2026 while being developed and maintained independently.



## License

AtmosGrid's original contributions controlled by the copyright holder are offered under the [Apache License, Version 2.0](LICENSE) for new distributions. See [NOTICE](NOTICE). The previous [MIT license](LICENSES/MIT-previous.txt) remains available for historical distributions and prior grants.

**Note:** This license applies to the project code and accompanying materials
owned by the project author. Third-party datasets, satellite products, libraries,
and external services remain subject to their respective licenses and terms.

---

<p align="center">
  <strong>AtmosGrid</strong>
  <br/>
  Mapping India's Atmosphere from Space
  <br/>
  <em>Satellite observations. Ground evidence. Environmental intelligence.</em>
</p>
