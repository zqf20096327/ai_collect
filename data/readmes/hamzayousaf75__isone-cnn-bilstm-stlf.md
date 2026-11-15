# Hybrid CNN-BiLSTM for Short-Term Electric Load Forecasting (ISO-NE 2019–2023)

Official implementation and empirical reproduction for **Hybrid 1D-CNN and Bidirectional LSTM (CNN-BiLSTM)** short-term electric load forecasting on the **ISO New England (ISO-NE)** wholesale electricity market dataset (2019–2023, 43,824 hourly observations).

---

## 1. Overview & Architecture

* **1D Convolutional Layers (`Conv1D` + `MaxPooling1D`):** Extracts local high-frequency load-weather-market motifs across a **168-hour (7-day) lookback window**.
* **Stacked Bidirectional LSTM Layers (`Bidirectional(LSTM)`):** Captures forward and backward temporal dependencies across the sequence representation.
* **Autoregressive Diurnal-Market Residual Highway:** Anchors multi-horizon predictions against short-term autoregressive lags and day-ahead market demand (`DA_Demand`).
* **Two-Phase Optimization Schedule:** Coarse training phase (`lr = 1e-3`, 25 epochs) followed by fine-tuning (`lr = 1e-4`, 15 epochs) with early stopping.

---

## 2. Dataset Summary (ISO-NE Control Area, 2019–2023)

Constructed from five official ISO-NE Standard Market Design (SMD) hourly workbooks (`2019_smd_hourly.xlsx` through `2023_smd_hourly.xlsx`, `ISO NE CA` control area tab), spanning **January 1, 2019 00:00 to December 31, 2023 23:00 (43,824 hours, 0 missing values)**.

| Variable | Source Column / Formula | Count | Mean | Median | Min | Max | Std Dev |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Real-Time Load (MW)** | `RT_Demand` | 43,824 | 13,206.20 | 12,920.20 | 8,234.88 | 25,424.07 | 2,619.65 |
| **Day-Ahead Demand (MW)** | `DA_Demand` | 43,824 | 12,887.47 | 12,562.95 | 7,286.90 | 25,352.70 | 2,566.25 |
| **Day-Ahead Price ($/MWh)** | `DA_LMP` | 43,824 | 44.56 | 32.39 | 6.33 | 374.98 | 36.07 |
| **Temperature (°C)** | Converted from `Dry_Bulb` (°F) | 43,824 | 11.02 | 11.11 | -23.33 | 35.00 | 9.88 |
| **Relative Humidity (%)** | Magnus formula (`Dry_Bulb`, `Dew_Point`) | 43,824 | 66.28 | 67.20 | 14.00 | 100.00 | 18.46 |

---

## 3. Empirical Results (2023 Out-of-Sample Test Set)

### Table A: 24-Hour-Ahead Multi-Step Forecasting
| Model | MAPE (%) | MAE (MW) | RMSE (MW) |
| :--- | :---: | :---: | :---: |
| Persistence (24 h) | 6.046 | 789.016 | 1105.242 |
| Seasonal naive (168 h) | 8.797 | 1170.007 | 1669.043 |
| LSTM | 2.003 | 250.425 | 322.722 |
| CNN-LSTM | 1.832 | 229.308 | 295.274 |
| **CNN-BiLSTM (Proposed)** | **1.530** | **192.613** | **247.199** |

> **24-Hour-Ahead RMSE Reduction (`CNN-BiLSTM` vs. unidirectional `LSTM`):** **23.40%**

### Table B: Single-Step (1-Hour-Ahead) Forecasting
| Model | MAPE (%) | MAE (MW) | RMSE (MW) |
| :--- | :---: | :---: | :---: |
| Persistence (24 h) | 6.052 | 789.561 | 1105.821 |
| Seasonal naive (168 h) | 8.839 | 1174.216 | 1674.338 |
| LSTM | 1.340 | 168.855 | 211.780 |
| CNN-LSTM | 1.223 | 154.829 | 195.021 |
| **CNN-BiLSTM (Proposed)** | **1.083** | **138.200** | **176.831** |

---

## 4. Visualizations

### 3-Day Actual vs. Predicted Load (ISO-NE Test Set: Dec 28–30, 2023)
![3-Day Actual vs Predicted Load](results/fig4_actual_vs_predicted.png)

### Single-Step Literature Benchmark Comparison (ISO-NE Dataset)
![Single-Step Literature Comparison](results/fig5_literature_comparison.png)

### Convergence Curve & Forecast Error by Lead Hour (1h to 24h)
| CNN-BiLSTM Convergence Curve | Forecast Error by Lead Time (1h–24h) |
| :---: | :---: |
| ![Convergence Curve](results/training_curve.png) | ![MAE by Lead Hour](results/mae_by_lead.png) |

---

## 5. Quickstart & Reproduction

```bash
pip install -r requirements.txt
python cnn_bilstm_load_forecasting.py
```

---

## 6. Publication & Citation

This repository provides the official open-source implementation and benchmark dataset for our paper accepted at the **2026 IEEE International Conference on Electrical, Communication and Computer Engineering (ICECCE)** *(Paper ID: PAP-080)*:

> H. Yousaf, S. K. Rasakatla, Z. Musawar, A. Rahman, K. Ullah, and R. Younis, "CNN-BiLSTM Hybrid Neural Network for Short-Term Load Forecasting in Deregulated Electricity Markets," *2026 International Conference on Electrical, Communication and Computer Engineering (ICECCE)*, IEEE, 2026.

```bibtex
@inproceedings{yousaf2026cnnbilstm,
  author    = {Yousaf, Hamza and Rasakatla, Sravan Kumar and Musawar, Zulqarnain and Rahman, Abdur and Ullah, Kaleem and Younis, Rehmana},
  title     = {CNN-BiLSTM Hybrid Neural Network for Short-Term Load Forecasting in Deregulated Electricity Markets},
  booktitle = {2026 International Conference on Electrical, Communication and Computer Engineering (ICECCE)},
  year      = {2026},
  publisher = {IEEE},
  note      = {Paper ID: PAP-080}
}
```
