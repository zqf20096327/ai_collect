# AirHealthClassifier

Klasifikasi multi-kelas untuk memprediksi kategori dampak kesehatan (`HealthImpactClass`) dari enam parameter polutan udara menggunakan K-Nearest Neighbors (KNN) dan `NeighborhoodComponentsAnalysis` (NCA).

## Overview

Repositori ini berisi alur eksperimen dan pemodelan KNN di `notebooks/01_AirQuality_HealthImpact_KNN.ipynb`. Pada tahap data cleaning, 291 baris ekor (`RecordID >= 5521`) terdeteksi berlabel acak sehingga dibersihkan sebelum pelatihan, dan kolom `HealthImpactScore` dikeluarkan karena merupakan skor penentu kelas.

Pipeline akhir menggunakan 6 fitur polutan inti (`AQI`, `PM10`, `PM2_5`, `NO2`, `SO2`, `O3`) melalui `StandardScaler -> NCA -> KNN` di dalam `sklearn.pipeline.Pipeline`. Seleksi model dan hyperparameter tuning dijalankan dengan 5-Fold Stratified Cross-Validation pada 80% data latih berbasis `Macro F1-score`, lalu diuji satu kali pada 20% hold-out test set.

## Dataset

Menggunakan *Air Quality and Health Impact Dataset* dari Kaggle (`5.520` baris bersih pada 4 kelas target dengan 6 fitur polutan inti).

Detail sumber, skema kolom, catatan pembersihan data, dan atribusi lisensi (`CC BY 4.0`) tersedia di [DATASET.md](DATASET.md).

## Results

### 5-Fold Stratified Cross-Validation (`X_train`, `n = 4.416`)

| Eksperimen | Fitur | Proyeksi | Model | CV Macro F1 (Mean +/- Std) | CV Accuracy |
| --- | --- | --- | --- | :---: | :---: |
| `Baseline_0_Dummy` | 12 fitur | None | `DummyClassifier(most_frequent)` | `0.2313 +/- 0.0001` | `0.8605` |
| `Baseline_1_KNN_All12` | 12 fitur | None | `KNN(k=5, uniform, euclidean)` | `0.3587 +/- 0.0451` | `0.8689` |
| `Exp_1_Core6_Pollutants` | 6 polutan | None | `KNN(k=5, uniform, euclidean)` | `0.5052 +/- 0.0716` | `0.9047` |
| `Exp_2_LDA_KNN` | 6 polutan | `LDA(n=2)` | `KNN(k=5, uniform, euclidean)` | `0.9174 +/- 0.0160` | `0.9762` |
| `Exp_3_NCA_KNN` | 6 polutan | `NCA(n=1)` | `KNN(k=5, uniform, euclidean)` | `0.9706 +/- 0.0198` | `0.9941` |
| **Konfigurasi Terbaik** | **6 polutan** | **`NCA(n=1)`** | **`KNN(k=21, uniform, euclidean)`** | **`0.9787 +/- 0.0102`** | **`0.9948`** |

### Evaluasi Held-Out Test Set (`n = 1.104`)

- **Accuracy:** `0.9909` | **Macro F1:** `0.9488` | **Weighted F1:** `0.9909` | **Error:** `10 / 1.104` (`0,91%`, seluruhnya antar kelas berdekatan)
- **F1 per kelas:** C0 `0.9989` (support 950), C1 `0.9561` (104), C2 `0.9070` (42), C3 `0.9333` (8)
- **Model artifact:** `models/knn_air_health.joblib`, `models/metrics.json`

![Confusion Matrix dan Metrik Per Kelas](reports/figures/knn_test_confusion_and_metrics.png)

## Getting Started

### Instalasi dan Eksekusi

1. Buat dan aktifkan virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependensi:
   ```powershell
   pip install -r requirements.txt
   ```
3. Jalankan notebook dari root repositori:
   ```powershell
   python -m nbconvert --to notebook --execute --inplace notebooks/01_AirQuality_HealthImpact_KNN.ipynb
   ```

### Prasyarat

- Python `3.13+`

## License

Proyek ini dirilis di bawah lisensi MIT. Lihat [LICENSE](LICENSE) untuk detail lengkap.
