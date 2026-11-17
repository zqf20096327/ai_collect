# Stock Price Prediction and Trend Analysis Using LSTM and GRU

A deep learning project combining historical stock-price trend analysis with a comparison of **LSTM** and **GRU** neural networks for one-step-ahead prediction of adjusted closing prices and five-observation moving averages across five major technology companies.

This project was developed collaboratively. The results below come from saved experiments using historical data through August 2025; rerunning the notebook may produce different results.

## Project overview

The analysis covers five stocks:

| Company | Ticker |
| --- | --- |
| Apple | `AAPL` |
| Microsoft | `MSFT` |
| Alphabet | `GOOGL` |
| Amazon | `AMZN` |
| NVIDIA | `NVDA` |

Daily market data is downloaded using **yfinance** with `auto_adjust=True`. The saved run requested data from **September 3, 2015, to August 31, 2025**. The code uses a rolling ten-year date range, so a new execution will request a different period.

The notebook includes exploratory visualizations of adjusted closing prices, trading volume, daily returns, moving averages, and correlations.

## Methodology

For each stock, the notebook trains separate LSTM and GRU models on two targets:

- **Close:** adjusted daily closing price.
- **MA5:** trailing five-trading-observation moving average of the adjusted closing price.

Each model uses the preceding **60 observations** to predict the next value. The workflow applies MinMax scaling, a chronological approximately **80% / 20%** train/test split, and inverse transformation before evaluating predictions with **root mean squared error (RMSE)**.

| Configuration | LSTM | GRU |
| --- | --- | --- |
| Recurrent layers | 2 × LSTM (50 units each) | 2 × GRU (50 units each) |
| Dropout | 0.2 after each recurrent layer | 0.2 after each recurrent layer |
| Dense layers | 25 units, then 1 output | 25 units, then 1 output |
| Optimizer | Adam | Adam |
| Loss function | Mean squared error | Mean squared error |
| Epochs | 20 | 20 |
| Batch size | 32 | 32 |

The notebook performs **20 model fits** in total: five stocks × two architectures × two targets. This is a one-step-ahead historical evaluation using preceding observed values, not a multi-step forecast from the train/test boundary.

## Results

Saved test RMSE values (in the original target's USD units; lower is better **within the same stock and target**):

| Stock | LSTM — Close | LSTM — MA5 | GRU — Close | GRU — MA5 |
| --- | ---: | ---: | ---: | ---: |
| AAPL | 8.06 | 8.48 | 5.26 | 6.73 |
| MSFT | 15.78 | 20.75 | 17.13 | 7.20 |
| GOOGL | 5.04 | 4.29 | 4.02 | 2.91 |
| AMZN | 6.46 | 5.62 | 4.77 | 3.06 |
| NVDA | 8.27 | 9.54 | 8.47 | 3.55 |

For daily closing-price prediction, GRU recorded lower RMSE for **AAPL, GOOGL, and AMZN**, while LSTM recorded lower RMSE for **MSFT and NVDA**. For the MA5 target, GRU recorded lower RMSE for all five stocks. Because `Close` and `MA5` are different targets, their errors should not be interpreted as directly interchangeable.

## Notebook and tools

Open **[stock_price_prediction.ipynb](stock_price_prediction.ipynb)** to review the analysis, model code, saved prediction plots, and results.

**Tools and libraries:** Python, Jupyter Notebook, yfinance, Pandas, NumPy, scikit-learn, TensorFlow/Keras, Matplotlib, and Seaborn.

To attempt a fresh run, open the notebook in Jupyter, install the required packages, and run the cells in order with internet access enabled for market-data downloads. The original environment is not fully pinned or verified, and a new run may produce different dates and scores. For that reason, use a copy of the notebook if you want to preserve its saved outputs.

## Limitations

- **Data leakage risk:** `MinMaxScaler` is fitted on the complete target series before the train/test split, so the saved RMSE values are not a leakage-free benchmark.
- **No baseline comparison:** The experiments do not include a naive persistence benchmark, walk-forward validation, or repeated-run uncertainty analysis.
- **Reproducibility:** Live data downloads, unpinned dependencies, and the absence of fixed random seeds can affect repeatability.
- **Scope:** The project evaluates prediction errors, not trading profitability or real-world investment performance.

## Contributors

This project was developed collaboratively by **Parsa AliKhani** and **Mahdi Ghiyasi**.
