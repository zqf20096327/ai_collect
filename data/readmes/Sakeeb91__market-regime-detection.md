# Financial Market Regime Detection

A regime detection system using Hidden Markov Models and machine learning to identify market states (bull, bear, high-volatility) and adapt investment strategies accordingly.

## Problem Statement

Financial markets exhibit distinct behavioral regimes that require different trading strategies. A strategy optimized for bull markets often fails during bear markets or high-volatility periods. This system automatically identifies market regimes and enables regime-aware portfolio management.

## Industry Applications

- Quantitative trading firms
- Asset management (regime-aware allocation)
- Risk management (volatility forecasting)
- Algorithmic trading systems
- Portfolio optimization
- Market timing strategies

## Key Features

- **Hidden Markov Models (HMM)**: Unsupervised regime detection with Gaussian emissions
- **Gaussian Mixture Models (GMM)**: Alternative clustering-based approach
- **Change Point Detection**: Structural break identification
- **Regime-Conditioned Trading**: Adaptive strategies based on detected regime
- **Walk-Forward Validation**: Proper backtesting without lookahead bias

## Detected Regimes

| Regime | Characteristics |
|--------|-----------------|
| Bull/Calm | Low volatility, positive returns |
| Bear/Crisis | High volatility, negative returns |
| Transition | Medium volatility, mixed returns |

## Technical Architecture

```
Market Data (Yahoo Finance)
        |
        v
+------------------+
|  Feature Eng     |
|  - Returns       |
|  - Volatility    |
|  - Technicals    |
+------------------+
        |
        v
+------------------+     +------------------+
| Regime Detection | --> | Strategy Engine  |
| - HMM            |     | - Position Sizing|
| - GMM            |     | - Risk Mgmt      |
| - Change Points  |     +------------------+
+------------------+              |
        |                         v
        v               +------------------+
+------------------+    |   Backtesting    |
| Visualization    |    | - Walk-Forward   |
| - Regime Plots   |    | - Metrics        |
| - Equity Curves  |    +------------------+
+------------------+
```

## Project Structure

```
market-regime-detection/
├── data/                    # Cached market data
├── src/
│   ├── data_loader.py       # Yahoo Finance data fetching
│   ├── features.py          # Feature engineering
│   ├── hmm_regime.py        # HMM regime detection
│   ├── gmm_regime.py        # GMM clustering approach
│   ├── changepoint.py       # Change point detection
│   ├── strategy.py          # Regime-based trading strategies
│   ├── backtest.py          # Backtesting framework
│   ├── visualize.py         # Regime visualization
│   └── walk_forward.py      # Walk-forward validation
├── notebooks/
│   └── EDA.ipynb            # Exploratory data analysis
├── docs/
│   └── IMPLEMENTATION_PLAN.md
├── tests/
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# Clone repository
git clone https://github.com/Sakeeb91/market-regime-detection.git
cd market-regime-detection

# Install dependencies
pip install -r requirements.txt

# Download market data
python src/data_loader.py --ticker SPY --start 2000-01-01

# Fit HMM and detect regimes
python src/hmm_regime.py --n-states 3

# Run backtest
python src/backtest.py --strategy regime

# Generate visualizations
python src/visualize.py
```

## Expected Results

| Metric | Target |
|--------|--------|
| Regime detection | Correctly identify 2008, 2020 crises |
| Strategy Sharpe | 0.5-1.0 (after costs) |
| Max Drawdown | Reduced vs buy-and-hold |
| Volatility | Lower than benchmark |

## Key Insights

The system should detect:
- **2008 Financial Crisis**: Transition to bear regime in late 2008
- **2020 COVID Crash**: Sharp regime change in March 2020
- **Bull Markets**: Extended periods of low-volatility positive returns

## Requirements

- Python 3.8+
- hmmlearn
- scikit-learn
- yfinance
- pandas
- numpy
- ruptures
- matplotlib
- seaborn

## License

MIT License

## Author

Sakeeb Rahman - [GitHub](https://github.com/Sakeeb91)

## Disclaimer

This project is for educational purposes only. Past performance does not guarantee future results. This is not financial advice.
