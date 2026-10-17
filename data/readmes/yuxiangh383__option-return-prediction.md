# Option return factors on Chinese index / ETF options

Companion code for Huang, Wang, and Xiao (2025), [*Option return predictability via machine learning: new evidence from China*](https://onlinelibrary.wiley.com/doi/abs/10.1002/fut.22604), *Journal of Futures Markets*.

The repository constructs and tests option-return factors on CSI index options and SSE/SZSE ETF options. Factor definitions follow the US equity-option literature (implied-volatility slope, risk-neutral moments, liquidity, Greeks, and related signals) and are applied to the China listed-options market.

This repository is a **research codebase**, not a live trading engine. Raw option quotes are proprietary and are **not** included.

## What you can run without data access

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python examples/run_factors_synthetic.py
pytest
```

The example builds a small Black-Scholes panel, prices Greeks, interpolates 30-day ATM IV, runs a Newey–West t-test, and checks a walk-forward split with no lookahead.

## Repository layout

```
option_factors/          public helpers (paths, synthetic panel, time-series splits)
models/                  factor implementations used by the notebooks
notebooks/pipeline/      main construction pipeline (download → factors → backtest)
notebooks/research/      follow-up empirical notebooks
notebooks/archive/       older experiments, kept for provenance
examples/                scripts that run after a fresh clone
tests/                   unit tests for pricing, moments, splits, and secret hygiene
docs/                    factor dictionary and data schema
```

## Data (not redistributed)

Market data were pulled from a private ClickHouse warehouse (`backbone` option and underlying tables). Exchange option data are typically licensed; **do not commit** parquet/pickle dumps or database passwords.

Expected local layout after you download data yourself:

```
data/
  OptionAugData.pkl
  Factors/Stock/
  Factors/Bucket/
  Factors/Contract/
```

Column requirements are listed in [docs/data-schema.md](docs/data-schema.md). Point `OPTION_FACTORS_DATA` at another directory if needed.

If you have warehouse access, copy `.env.example` and export:

```bash
export CLICKHOUSE_HOST=...
export CLICKHOUSE_USER=...
export CLICKHOUSE_PASSWORD=...
```

Do not hardcode credentials. Load local extracts, then run the numbered notebooks in `notebooks/pipeline/`.

## Pipeline notebooks

Run Jupyter from any folder; each notebook cds to the repo root on the first cell.

1. `1-DataPreprocess.ipynb` — dividends, moneyness, ATM flags
2. `2-PrecalculateIV.ipynb` — implied volatility
3. `3a/3b/3c-StockLevelFactor.ipynb` — underlying-level factors
4. `4-BucketLevelFactor.ipynb` — moneyness/maturity buckets
5. `5-ContractLevelFactor.ipynb` — contract Greeks
6. `6-FilterSummarySelect.ipynb` — screening
7. `7-BackTest-daily-regression.ipynb` — out-of-sample backtests

Factor formulas and paper pointers: [docs/factors.md](docs/factors.md).

## License

MIT. `models/ipca.py` is adapted from [bkelly-lab/ipca](https://github.com/bkelly-lab/ipca) (MIT). You can `pip install ipca` instead of using the vendored file.

## Citation

If you use this code, please cite:

Huang, Y., Wang, Z., & Xiao, Z. (2025). Option return predictability via machine learning: new evidence from China. *Journal of Futures Markets*, *45*(9), 1232–1252. https://onlinelibrary.wiley.com/doi/abs/10.1002/fut.22604

```bibtex
@article{huang2025option,
  title={Option return predictability via machine learning: new evidence from China},
  author={Huang, Yuxiang and Wang, Zhuo and Xiao, Zhengyan},
  journal={Journal of Futures Markets},
  volume={45},
  number={9},
  pages={1232--1252},
  year={2025},
  publisher={Wiley Online Library},
  doi={10.1002/fut.22604},
  url={https://onlinelibrary.wiley.com/doi/abs/10.1002/fut.22604}
}
```

Please also cite the original factor papers listed in [`docs/factors.md`](docs/factors.md).
