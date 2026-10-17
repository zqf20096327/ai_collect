# ⚖️ IndianBailJudgments-1200: Annotated Indian Bail Order Dataset (1975–2025)

**IndianBailJudgments-1200** is a high-quality, structured dataset comprising **1,200** annotated Indian bail-related court orders spanning **five decades (1975–2025)**. It captures granular legal information across **78 courts** and **28 regions**, including crime types, IPC sections invoked, judge names, legal issues, bail outcomes, and bias indicators.

Designed for use in **legal NLP**, **fairness analysis**, and **judicial research**, this dataset enables exploration of legal reasoning patterns, procedural parity, and systemic bias in Indian bail decisions.

It supports tasks such as **text classification**, **summarization**, **document question answering**, and **legal transparency benchmarking**.

---

## 📦 What's Included

- `indian_bail_judgments.json` — Main JSON dataset (1200 objects)
- `indian_bail_judgments.csv` and `indian_bail_judgments.xlsx` — Tabular versions
- `IndianBailJudgments-1200_PDFS/` — Folder containing 1200 corresponding court PDF files (`case0001.PDF` to `case1200.PDF`)
- `summarized_stats.txt` — Statistical summary of dataset

📦 View the hosted dataset on [Hugging Face 🤗](https://huggingface.co/datasets/SnehaDeshmukh/IndianBailJudgments-1200)

---

## 📊 Dataset Statistics

**Total Cases**: 1200  
**Years Covered**: 1975–2025  
**Courts**: 78  
**Regions**: 28  
**Crime Types**: 12 (e.g., Murder, Fraud, Cybercrime...)  
**Bail Outcomes**: 736 Granted, 464 Rejected  
**Landmark Cases**: 147  
**Bias Flagged**: 13 cases  
📍 _See `summarized_stats.txt` for full breakdown._

---

## 📚 Fields in Each Case

Each JSON object includes:

- `case_id`, `case_title`, `court`, `date`, `judge`
- `ipc_sections`, `bail_type`, `bail_outcome`, `bail_cancellation_case`, `landmark_case`
- `accused_name`, `accused_gender`, `prior_cases`, `crime_type`
- `facts`, `legal_issues`, `judgment_reason`, `summary`
- `bias_flag`, `parity_argument_used`, `region`, `source_filename`

---

## 🔍 Use Cases

- Legal NLP tasks (summarization, extraction, fairness)
- Judicial transparency & criminal justice research
- Law school curriculum & annotation training

---

## ⚖️ License

Released under [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)  
You are free to use, adapt, and redistribute. Please provide appropriate credit to the authors.

---

## 👥 Authors

- Sneha Deshmukh (deshmusn@gmail.com)  
- Prathmesh Kamble (prathameshk990@gmail.com)

---

## 📣 Citation

```bibtex
@misc{indianbail2025,
  title  = {IndianBailJudgments-1200: Annotated Dataset of 1200 Indian Bail Judgments},
  author = {Sneha Deshmukh and Prathmesh Kamble},
  year   = {2025},
  url    = {https://huggingface.co/datasets/SnehaDeshmukh/IndianBailJudgments-1200},
  note   = {Dataset publicly released under CC BY 4.0 License}
}
```

---

# 🔗 Citation and GitHub Mirror

This GitHub repo mirrors the dataset publicly hosted on Hugging Face. For full interactive data viewer and loading support, use the 🤗 link above. Thank You!
