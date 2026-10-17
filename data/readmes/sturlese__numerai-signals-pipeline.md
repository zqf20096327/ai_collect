# Numerai Signals Pipeline

> Build **your own** technical-analysis features from Yahoo Finance data and submit them to the
> [Numerai Signals](https://signals.numer.ai/) tournament.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Tests](https://img.shields.io/badge/tests-93%20passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/coverage-99%25-brightgreen.svg)
![Lint](https://img.shields.io/badge/lint-ruff-261230.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

The pipeline downloads price/volume data from Yahoo Finance, builds a large set of custom
technical-analysis features (indicators → lags → per-era normalisation), joins them to
Numerai's official targets, trains an XGBoost model and produces a valid tournament
submission.

## What is Numerai Signals?

Numerai runs a hedge fund driven by a crowd-sourced meta-model. In **Signals** you map
stock-market data to a per-ticker **signal** — a number strictly between 0 and 1 — over the
global equity universe. Numerai neutralises your signal against its own risk factors, scores
the residual alpha, and pays or burns your stake based on live performance. A submission is
just: *for each ticker in the current round's universe, a signal in (0, 1)*.

## Quickstart

Requires Python ≥ 3.10.

```sh
# install (uv recommended; plain venv + pip works too)
uv venv --python 3.13
uv pip install -e '.[dev]'

# run the full pipeline: download → features → train → submit
nsp run --properties props.json

# or build the files without uploading (and train on CPU)
nsp run --properties props.json --no-submit --device cpu
```

`props.json` holds your Numerai credentials — keep it out of git:

```json
{ "public_id": "...", "secret_key": "...", "model_id": "..." }
```

Useful flags: `--root` (data dir, default `data`), `--jobs` (parallel processes for indicator
computation), `--device` (`cuda` by default, `cpu` to train without a GPU), `--skip-download`,
`--static-data`, `--no-submit`, `--keep-intermediate`. See `nsp run --help`.

## Architecture

Pure, IO-free logic (unit-tested) is separated from thin IO/network/multiprocessing glue.

```
raw OHLCV ──▶ indicators ──▶ denoise ──▶ lags ──▶ per-era normalise + encode ──┐
 (Yahoo)      (registry)    (winsorise)  (shift)   (bin / zscore / rank)        │
                                                                                ▼
    Numerai API ── targets + universe ─────────────────▶ assemble ML dataset ──▶ XGBoost ──▶ submission
    (download_dataset / ticker_universe)                                              numerai_ticker + signal ∈ (0,1)
```

The centrepiece is the **declarative feature/lag engine**:

- Indicators are pure functions in a registry (`nsp.domain.indicators`), keyed by name — no
  boilerplate classes.
- An immutable `IndicatorSpec` (`nsp.domain.specs`) is the single source of truth for *what*
  to build. `build_specs()` is the only place lags are resolved: windowed indicators get lags
  that are fractions of their window (`int(window * fraction)`, de-duplicated); fixed
  indicators get absolute integer lags.
- Lagging is one vectorised `groupby(ticker).shift(lag)` (`nsp.domain.features.apply_lags`),
  not a per-ticker Python loop.

### Project layout

```
src/nsp/
  config.py            immutable dataclass config (Data/Indicator/Model/Submission)
  paths.py  io.py       filesystem layout + parquet/csv helpers
  naming.py            canonical feature-column naming (single source of truth)
  domain/
    indicators/        registry of pure indicator functions (price / volume / custom ADX,ATR)
    specs.py           IndicatorSpec + build_specs (lag resolution)
    features.py        compute indicators, apply_lags, normalise_per_era, encode_labels
    denoise.py         outlier-row drop + winsorising
    tickers.py         bloomberg↔numerai_ticker + Yahoo ticker map
    target.py          optional custom forward-return target
  data/
    yahoo.py           OHLCV downloader (pure parsers + network glue)
    numerai.py         Numerai data-API adapter (targets / universe / upload)
  dataset.py           assemble train/validation/live ML frame
  model/predict.py     feature selection, training, submission builder
  pipeline.py  cli.py   orchestration + command-line entry point
tests/                 unit tests + an offline end-to-end pipeline test
```

### Data sources

- **Prices** — Yahoo Finance (`nsp.data.yahoo`).
- **Targets & universe** — Numerai's data API (`nsp.data.numerai`):
  `download_dataset('signals/<version>/{train,validation}.parquet')` for targets and
  `SignalsAPI.ticker_universe()` for the live universe.
- **Bloomberg↔Yahoo ticker map** — a configurable community mirror with a bundled fallback.
  Bloomberg tickers are mapped to `numerai_ticker` via the ISO country-code table from
  Numerai's `example_model.ipynb`.

## Configuration

Immutable dataclasses in `nsp.config`:

- `IndicatorConfig` — indicators (windowed vs fixed), `windows`, `windowed_lag_fractions`,
  `fixed_lags`, and the per-era `transformation` (`bin` / `zscore` / `rank`).
- `ModelConfig` — XGBoost hyper-parameters, `target_name`, `device` (GPU by default),
  `max_feature_corr` (highly-correlated TA features are dropped before training).
- `DataConfig` — data root, dataset version, `min_era_size`, ticker-map URL.

## Output

Under `--root` (default `data/`):

- `db_ml_csv/ml_data.csv` — the assembled train/validation/live dataset (features + target).
- `db_predictions/submission.csv` — the upload file: `numerai_ticker, friday_date, signal`,
  with `signal` rank-normalised strictly into `(0, 1)`.
- `db_raw_downloaded/` — cached Yahoo data (reusable with `--skip-download`).

Intermediate directories are wiped after a run unless `--keep-intermediate` is passed.

## Testing

```sh
pytest                 # 93 tests, ~99% coverage (configured in pyproject.toml)
ruff check src tests   # lint
```

The suite is fully offline — synthetic fixtures, no network, no GPU — with unit tests for
every transformation plus an end-to-end pipeline run that produces a valid submission.

## Running live (notes)

A real run needs your Numerai credentials, downloads the multi-GB v2.x parquet datasets and
(by default) trains on a GPU. The offline tests exercise every transformation, but the live
data path is not run here. Confirm one thing against a real download: the exact target column
in `signals/<version>/*.parquet` (set via `ModelConfig.target_name`, default `target`);
`nsp.data.numerai` raises a clear `DataError` listing the available columns if it does not
match.

## Roadmap

- Era-wise purged cross-validation for hyper-parameter tuning.
- Feature selection via Mean Decrease Accuracy.
- Signal neutralisation against Numerai's risk factors before submitting.
- Confirm the v2.x parquet schema (target / id column names) against a live download.

## License

MIT (see `pyproject.toml`).
