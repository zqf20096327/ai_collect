# AI-Stock-Nowcasting

Real-time cross-sectional stock nowcasting project by Zefeng Chen and Darcy Pu at Guanghua School of Management, Peking University.

# Can Agentic AI Predict Stock Returns in Real Time?

*(Previously distributed as "Autonomous Market Intelligence: Agentic AI Nowcasting Predicts Stock Returns")*

[![View Interactive Plot](https://img.shields.io/badge/View-Interactive_Plot-blue?style=for-the-badge&logo=html5)](https://mapledust0.github.io/AI-Stock-Nowcasting/plot.html)
[![View Paper PDF](https://img.shields.io/badge/Download-Latest_PDF-green?style=for-the-badge&logo=adobeacrobatreader)](Artificial_Intelligence_ChenPu.pdf)
[![View our paper on SSRN](https://img.shields.io/badge/View-SSRN_Paper-orange?style=for-the-badge&logo=ssrn)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6134446)

> **Zefeng Chen & Darcy Pu**  
> *Guanghua School of Management, Peking University*  
> Updated: November 20, 2026 (Market data through November 6, 2026; Fama–French factors through September 30, 2026)

---

> **Disclaimer:**  
> The information and results presented in this project are for academic research and educational purposes only. They do not constitute financial advice or investment recommendations. Past performance is not indicative of future results.

---

## 📝 Abstract

Can an autonomous artificial intelligence agent predict equity returns in *real time*? We build a daily panel of AI-generated stock attractiveness scores for the Russell 1000 universe, where a frontier large language model searches the live internet and scores individual stocks before returns are realized.

Over **394 trading days** from **April 2025 through November 6, 2026** (388,629 valid 1-day scores across 407,523 stock-day return observations), a daily value-weighted portfolio of the **20 highest-ranked stocks** earns a gross cumulative return of **69.9%**, compared with **35.1%** for the Russell 1000 benchmark (+**34.8 percentage points**). Over the 367 factor-matched trading days through September 30, 2026, the portfolio generates an average excess return of **15.2 basis points per day** ($t = 2.11$), a Fama–French six-factor (FF6) alpha of **11.3 basis points per day** ($t = 1.82$, **28.4%** annualized), and an annualized Sharpe ratio of **1.63**. This abnormal return is not spanned by machine-learning factor models (IPCA, AP-Tree, and the 13-theme Kelly factor library) and beats 10,000 random 20-stock portfolios in both mean return ($p = 0.0256$) and FF6 alpha ($p = 0.0235$).

Opening the 7,876 archived written equity reports matched to Top-20 holdings shows that reports combining strong analytical reasoning with low retrieval intensity generate **61.5%** of portfolio alpha (**6.94 bps/day**, $t = 2.68$), while a Brinson theme attribution shows that **96.2%** of active outperformance comes from selecting stocks *within* investment themes rather than rotating across themes.

---

## ⚙️ Real-Time Protocol & Methodology

* **Universe & Eligibility:** Active constituents on our dated Russell 1000 research stocklist (~93% of US equity market cap; median market capitalization \$14.5 billion). Scores carry forward only within uninterrupted membership episodes; securities exiting the stocklist or delisting are excluded from new selection and removed from outstanding holdings with proportional weight rescaling over surviving names.
* **Agentic Workflow:** Every trading day since April 2025, an identical ten-part prompt is submitted to a frontier LLM with live web search enabled (Grok web interface through December 18, 2025; Gemini Flash web interface from December 19, 2025 onward). We do not pre-select news or filings; the model writes its own web queries, reads live public sources, archives a full equity report, and outputs numerical scores.
* **Strict Real-Time Archive:** All reports and extracted scores are frozen at collection with no retroactive re-evaluation.
* **Signal:** Stock attractiveness score on $[-5, +5]$ (`-5` Strong Sell to `+5` Strong Buy) across six horizons (1 day, 1 week, 1 month, 1 quarter, 2 quarters, 1 year).
* **Execution & Weighting:** Portfolio formation aligns each report's nominal date to the trading calendar, measuring open-to-open price returns from day $t$ open to day $t+1$ open. Portfolios are value-weighted with a **20%** single-stock weight cap.

---

## 📊 Interactive Visualization

**[👉 Launch the Interactive Top-N Portfolio Return Viewer](https://mapledust0.github.io/AI-Stock-Nowcasting/plot.html)**

Explore daily value-weighted (20% cap) cumulative returns across portfolio sizes from **Top 10** to **Top 200** (in steps of 5) over any custom date window between **April 15, 2025** and **November 6, 2026**, rebased to 100 against the Russell 1000 benchmark.

### Static Figure: Daily Top-20 Value-Weighted Portfolio Cumulative Return

![Daily Top-20 Value-Weighted Portfolio Cumulative Return](figs/cumret/cumret_daily_top20_vw_cap20r.png)

---

## 🔑 Key Findings

### 1. Real-Time Winner Selection in Liquid Large-Cap Stocks
The daily **Top-20 Value-Weighted Portfolio** earns **69.9%** cumulative return over April 2025–November 6, 2026 versus **35.1%** for the Russell 1000 benchmark (+34.8 pp), with an FF6 alpha of **11.3 bps/day** (28.4% annualized) and an average quoted half-spread of just **2.16 bps** on traded Top-20 holdings.

### 2. Multi-Horizon Persistence & Upper-Tail Concentration
Across longer horizons (weekly, monthly, and quarterly), overlapping Top-20 portfolios continue to deliver positive FF6 alphas (**6.7 to 9.1 bps/day**) with sharply lower turnover, while Bottom-20 portfolios trail the benchmark. Expanding the daily portfolio beyond the top conviction tier dilutes alpha.

### 3. Analytical Synthesis & Within-Theme Stock Selection
* **Reasoning vs. Retrieval:** Reports with above-median analytical reasoning and below-median retrieval intensity generate **61.5%** of Top-20 alpha (**6.94 bps/day**, $t = 2.68$), whereas high-retrieval / low-reasoning reports contribute only **1.2%** (**0.14 bps/day**).
* **Within-Theme Selection:** Across eight investment themes, **96.2%** of active alpha relative to the classified Russell 1000 universe comes from picking individual winners *within* themes, and only **3.8%** from allocating across themes.

---

## 📂 Repository Contents

This public repository shares the latest manuscript, interactive return series, and published figures and summary tables. Raw stock-level scores, written reports, and daily holdings are not published.

* `Artificial_Intelligence_ChenPu.pdf` — Latest working paper PDF (November 20, 2026)
* `plot.html` & `data.json` — Interactive Top-N (10–200) daily portfolio vs. Russell 1000 return series
* `figs/` & `figs/cumret/` — Published figures from the manuscript (PNG & PDF)
* `tables/` — Published LaTeX summary tables from the manuscript

---

## 📚 Citation

If you use this project or its results in your research, please cite:

```bibtex
@article{chen_pu_2026,
  title={Can Agentic AI Predict Stock Returns in Real Time?},
  author={Chen, Zefeng and Pu, Darcy},
  journal={Working paper, Guanghua School of Management, Peking University},
  year={2026},
  month={November}
}
```
