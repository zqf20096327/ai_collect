# 🎬 Neural RAG Movie Search Engine

[English](#english) | [فارسی](#persian)

---

<a name="english"></a>
## 🇬🇧 English Description

### Overview
A high-performance semantic search engine for movie discovery built with **FastAPI**, **FAISS**, and **Sentence-Transformers**. This project utilizes Retrieval-Augmented Generation (RAG) concepts to understand context and intent in queries, returning relevant movies based on vector similarity rather than simple keyword matching.

### 🚀 Key Features
- **Semantic Understanding:** Captures natural language query intent across multiple languages.
- **Fast Vector Indexing:** Powered by Meta's **FAISS** for fast distance and similarity calculations.
- **Interactive REST API:** Built using **FastAPI** with automatic Swagger UI documentation.
- **Multilingual Support:** Handles English and Persian queries effortlessly using local embeddings.

### 🛠️ Tech Stack
- **Backend Framework:** FastAPI, Uvicorn
- **AI & Vector DB:** Sentence-Transformers, PyTorch, FAISS (CPU)
- **Data Validation & Structure:** Pydantic, Pandas, NumPy

---

<a name="persian"></a>
## 🇮🇷 توضیحات فارسی

### معرفی پروژه
موتور جستجوی هوشمند فیلم بر پایه پردازش معنایی متن (Semantic Search) و معماری RAG. این سیستم به جای اتکا به کلمات کلیدی، مفهوم و قصد اصلی کاربر از جستجو را درک کرده و شبیه‌ترین فیلم‌ها را از نظر معنایی پیدا می‌کند.

### 🚀 ویژگی‌های کلیدی
- **فهم معنایی جملات:** درک مفاهیم پیچیده و توصیفی به زبان‌های مختلف (انگلیسی و فارسی).
- **ایندکس برداری سریع:** بهره‌گیری از کتابخانه **FAISS** شرکت Meta جهت محاسبه تشابه بردارها.
- **رابط کاربری API:** توسعه داده شده با **FastAPI** به همراه مستندات تعاملی Swagger.

---

## 📜 License & Copyright / مجوز و کپی‌رایت

© 2026 **Sina Shojaeian (3INA3)**. All Rights Reserved.

This project is open-source and licensed under the **MIT License**. You are free to inspect, fork, and learn from the codebase. Any redistribution or commercial use must retain this original copyright notice and credit the author.