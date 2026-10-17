# DSFSI Public Datasets Registry

**Official dataset registry for the Data Science for Social Impact (DSFSI) Research Group**

[![GitHub](https://img.shields.io/badge/GitHub-dsfsi-blue)](https://github.com/dsfsi)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/dsfsi)
[![Website](https://img.shields.io/badge/Web-dsfsi.co.za-green)](https://www.dsfsi.co.za)

**Last Updated**: December 31, 2025

This repository serves as the comprehensive catalog and registry for all publicly available datasets produced by the DSFSI research group at the University of Pretoria. Our datasets span multiple domains including Natural Language Processing, Speech Recognition, Public Health, Legal Documents, Financial Data, and more, with a focus on South African and African languages and contexts.

## Table of Contents

- [Featured Datasets](#featured-datasets)
- [Datasets by Category](#datasets-by-category)
  - [Speech & Audio](#speech--audio)
  - [Text & NLP](#text--nlp)
  - [Terminology & Lexicons](#terminology--lexicons)
  - [Legal Documents](#legal-documents)
  - [Public Health](#public-health)
  - [Financial Data](#financial-data)
  - [Educational Datasets](#educational-datasets)
- [Datasets by Language](#datasets-by-language)
- [Datasets by Platform](#datasets-by-platform)
- [Local Datasets](#local-datasets)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Citation](#citation)
- [Contact](#contact)

---

## Featured Datasets

Our most popular and impactful datasets:

### 🎤 African Next Voices (ZA-ANV)
**The largest publicly available multilingual speech dataset for South African languages**

- **Platform**: [HuggingFace](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices)
- **Type**: Speech/Audio
- **Size**: 3,000 hours of audio
- **Languages**: 7 South African languages (isiZulu, Setswana, Sesotho sa Leboa, Tshivenda, Xitsonga, isiXhosa, Sesotho)
- **Models**: 8 Whisper-based ASR models available
- **License**: Custom (see dataset card)
- **Use Cases**: Automatic Speech Recognition, Speech-to-Text, Low-resource Language Processing

### 📚 za-mafoko: Multilingual Terminology Collection
**Comprehensive multilingual terminologies and glossaries for South African languages**

- **Platform**: [HuggingFace Collection](https://huggingface.co/collections/dsfsi/za-mafoko)
- **Type**: Terminology/Lexicon
- **Datasets**: 9+ specialized glossaries
- **Languages**: 11 South African languages
- **Notable Collections**:
  - [DSAC Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-dsac)
  - [StatsSA Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-statssa)
  - [OERTB Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-oertb)
  - [UP Glossary](https://huggingface.co/datasets/dsfsi/za-mafoko-up-glossary)
- **License**: Various (see individual datasets)
- **Use Cases**: Machine Translation, Terminology Management, Multilingual NLP

### 🦠 COVID-19 South Africa Data
**Comprehensive COVID-19 data repository and dashboard for South Africa**

- **Platform**: [GitHub](https://github.com/dsfsi/covid19za) | [Zenodo](https://zenodo.org/record/3819126)
- **Type**: Public Health/Time Series
- **Coverage**: Provincial and district-level data (2020-present)
- **Stars**: 256 | **Forks**: 197 | **Contributors**: 64+
- **Dashboard**: [Live Dashboard](https://dsfsi.github.io/covid19za-dash/)
- **Data Includes**: Cases, deaths, testing, vaccination, mobility, hospital surveillance
- **License**: Code (MIT), Data (CC BY-SA 4.0)
- **Use Cases**: Epidemiology, Public Health Research, Data Visualization
- **Showcase**: 14+ projects using this data

### 📰 Vuk'uzenzele Multilingual Corpus
**South African government magazine corpus in 11 languages**

- **Platform**: [GitHub](https://github.com/dsfsi/vukuzenzele-nlp) | [Zenodo](https://zenodo.org/record/7598539)
- **Type**: Text/Parallel Corpus
- **Languages**: 11 South African languages (English, Afrikaans, isiZulu, isiXhosa, Sesotho, Sepedi, Setswana, isiNdebele, Siswati, Tshivenda, Xitsonga)
- **Size**: 2,200+ aligned sentence pairs
- **Stars**: 7 | **Forks**: 6
- **License**: Code (MIT), Data (CC 4.0 BY)
- **Use Cases**: Machine Translation, Multilingual NLP, Sentence Alignment
- **Paper**: [RAIL 2023](https://link.springer.com/chapter/10.1007/978-3-031-37599-1_7)

### 🤖 PuoBERTa & PuoData
**Setswana language model and curated dataset**

- **Platform**: [GitHub](https://github.com/dsfsi/PuoBERTa) | [HuggingFace Model](https://huggingface.co/dsfsi/PuoBERTa) | [HuggingFace Dataset](https://huggingface.co/datasets/dsfsi/PuoData)
- **Type**: Text/Language Model
- **Language**: Setswana (Tswana)
- **GitHub Stars**: 5
- **Variants**: PuoBERTa-News, PuoBERTa-NER, PuoBERTa-POS
- **License**: CC BY 4.0
- **Performance**: 83.4 F1 (POS tagging), 78.2 F1 (NER)
- **Use Cases**: Text Classification, NER, POS Tagging, Embeddings
- **Paper**: [arXiv:2310.09141](https://arxiv.org/abs/2310.09141)

---

## Datasets by Category

### Speech & Audio

| Dataset | Platform | Languages | Size |
|---------|----------|-----------|------|
| [African Next Voices (ZA-ANV)](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices) | HuggingFace | 7 SA languages | 3,000 hours |
| [Vuk'uzenzele isiXhosa Speech (ViXSD)](https://huggingface.co/datasets/lelapa/Vukuzenzele_isiXhosa_Speech_Dataset_ViXSD) | HuggingFace | isiXhosa | - |
| [NCHLT Speech Corpus](https://rma.nwu.ac.za/index.php/resource-catalogue/nchlt-speech-corpus.html) | NWU Repository | 11 SA languages | - |
| [Lwazi Speech Corpus](https://repo.sadilar.org/handle/20.500.12185/7) | SADiLaR | Multiple | - |

**ASR Models Available**:
- [Multilingual Whisper v3 Turbo](https://huggingface.co/dsfsi-anv/multilingual-whisper-v3-turbo) (0.8B params)
- Language-specific Whisper models for Tshivenda, Xitsonga, Setswana, isiZulu, Sesotho
- [MMS-1B models](https://huggingface.co/dsfsi/mms-1b-all-nchlt) (NCHLT & Lwazi variants)
- [W2V-BERT 2.0 models](https://huggingface.co/dsfsi/w2v-bert-2.0-nchlt)

### Text & NLP

#### Multilingual Corpora

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [Vuk'uzenzele Corpus](https://github.com/dsfsi/vukuzenzele-nlp) | GitHub/Zenodo | 11 SA languages | Government magazine corpus with 2,200+ aligned sentences | CC 4.0 BY |
| [ZA-Gov Multilingual](https://github.com/dsfsi/gov-za-multilingual) | GitHub | Multiple | Cabinet statements from SA government | MIT |
| [Gov-ZA Cabinet Statements](https://huggingface.co/datasets/dsfsi/govza-sa-cabinet-statements-sentence-aligned) | HuggingFace | Multiple | Sentence-aligned government statements | - |

#### News & Media

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [IsiZulu & Siswati News 2022](https://github.com/dsfsi/za-isizulu-siswati-news-2022) | GitHub | isiZulu, Siswati | News categorization (Izindaba-Tindzaba) | - |
| [South African News Data (2020)](https://zenodo.org/record/3668495) | Zenodo | Multiple | News articles for classification | - |
| [AG News Dataset](local) | Local (this repo) | English | Text classification dataset | - |

#### Disinformation & Fact-Checking

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [ZA Fake News 2020](https://zenodo.org/record/4682843) | Zenodo | English | SA disinformation website data | - |
| [ZA Fake News Repo](https://github.com/dsfsi/za-fake-news-2020) | GitHub | English | Fake news detection corpus | - |

#### Language-Specific Datasets

| Dataset | Platform | Language | Description |
|---------|----------|----------|-------------|
| [PuoData](https://huggingface.co/datasets/dsfsi/PuoData) | HuggingFace | Setswana | Curated Setswana text corpus |
| [ANV Paper Sample](https://huggingface.co/datasets/dsfsi/anv_paper_sample) | HuggingFace | Multiple | Sample from ANV research |

#### Cross-lingual & Translation

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [Umsuka EN-IsiZulu Parallel Corpus](https://zenodo.org/record/5035171) | Zenodo | English, isiZulu | Parallel corpus for MT | - |
| [Kinyarwanda-Kirundi Models](https://github.com/rulezcasa/Cross-lingual-Kinyarwanda_Kirundi) | GitHub | Kinyarwanda, Kirundi | Cross-lingual transfer | - |
| [Masakhane MT](https://github.com/masakhane-io/masakhane-mt) | GitHub | 40+ African languages | Participatory MT resources | - |

#### Embeddings

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [African Pre-Trained Embeddings](https://zenodo.org/record/3668481) | Zenodo | Multiple African | Word embeddings for African languages | - |

#### Code-Switching

| Dataset | Platform | Languages | Description | License |
|---------|----------|-----------|-------------|---------|
| [AfroCS-xs](https://aclanthology.org/2025.acl-long.1601/) | ACL Anthology | Multiple African | Compact code-switched dataset | - |

### Terminology & Lexicons

The **za-mafoko** collection provides comprehensive multilingual terminologies:

| Dataset | Platform | Source |
|---------|----------|--------|
| [DSAC Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-dsac) | HuggingFace | Dept. Sport, Arts & Culture |
| [StatsSA Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-statssa) | HuggingFace | Statistics South Africa |
| [UNISA Multilingual](https://huggingface.co/datasets/dsfsi/za-mafoko-unisa-multilingual) | HuggingFace | University of South Africa |
| [OERTB Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-oertb) | HuggingFace | Open Educational Resources |
| [UP Glossary](https://huggingface.co/datasets/dsfsi/za-mafoko-up-glossary) | HuggingFace | University of Pretoria |
| [AI Glossary](https://huggingface.co/datasets/dsfsi/za-mafoko-ai-glossary) | HuggingFace | AI/ML terminology |
| [UNISA Robotics](https://huggingface.co/datasets/dsfsi/za-mafoko-unisa-robotics) | HuggingFace | Robotics terminology |
| [Tshivenda Augmented](https://huggingface.co/datasets/dsfsi/mafoko-tshivenda-augmented-translations) | HuggingFace | Tshivenda translations |

**Web Portal**: [za-mafoko.dsfsi.co.za](https://www.dsfsi.co.za/za-mafoko/)

**Other Lexicon Resources**:
- [WordNets for SA Languages (2020)](https://zenodo.org/record/4299515) - Zenodo
- [Loughran McDonald-SA-2020 Sentiment Word List](https://researchdata.up.ac.za/articles/dataset/Loughran_McDonald-SA-2020_Sentiment_Word_List/14401178) - UP Repository

### Legal Documents

| Dataset | Platform | Description | License |
|---------|----------|-------------|---------|
| [ZASCA-Sum](https://researchdata.up.ac.za/articles/journal_contribution/ZASCA-Sum) | UP Repository | Supreme Court of Appeal judgments and media summaries | - |
| [State Capture Commission Transcripts](https://github.com/dsfsi/project-state-capture) | GitHub | Zondo Commission transcripts (Oct 2022) | - |

### Public Health

| Dataset | Platform | Coverage | Description | Stars/Downloads |
|---------|----------|----------|-------------|-----------------|
| [COVID-19 ZA](https://github.com/dsfsi/covid19za) | GitHub | 2020-present | Comprehensive COVID-19 data for South Africa | 256 ⭐ / 197 forks |
| [COVID-19 ZA (Zenodo)](https://zenodo.org/record/3819126) | Zenodo | 2020-present | Archived version with DOI | - |

### Financial Data

| Dataset | Location | Coverage | Description | Format |
|---------|----------|----------|-------------|--------|
| [JSE Top 40 Stock Data](local) | This repo | 2019-2024 | Daily closing prices for JSE Top 40 companies | CSV, Pickle |

**Data Structure**:
- Ticker lists: `data/stocks/top40_jse_YYYY.csv`
- Performance data: `data/stocks/top40_jse_YYYY_performance.csv`
- Years: 2019, 2021, 2022, 2023, 2024
- Time range: First 4 months of each year (Jan-Apr)

### Educational Datasets

Curated datasets for coursework and teaching:

| Dataset | Location | Course | Description |
|---------|----------|--------|-------------|
| Customer Segmentation | `data/cos781/` | COS781 | Customer demographics and behavior |
| Hypermarket Dataset | `data/cos781/` | COS781 | Retail transaction data |
| Market Basket Data | `data/cos781/` | COS781 | Association rule mining |
| Online Retail II | `data/cos781/` | COS781 | E-commerce transactions (zipped) |
| AG News | `data/cos802/ag_news_csv/` | COS802 | News text classification |
| What's Cooking | `data/whats-cooking/` | - | Kaggle competition data |

---

## Datasets by Language

### isiZulu (Zulu)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele Corpus
- IsiZulu News 2022
- Umsuka EN-IsiZulu Parallel Corpus
- za-mafoko collections
- Whisper ASR models

### Setswana (Tswana)
- African Next Voices (ZA-ANV)
- PuoData & PuoBERTa
- Vuk'uzenzele Corpus
- za-mafoko collections
- Whisper ASR models

### isiXhosa (Xhosa)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele isiXhosa Speech Dataset (ViXSD)
- Vuk'uzenzele Corpus
- za-mafoko collections

### Sesotho (Southern Sotho)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele Corpus
- za-mafoko collections
- Whisper ASR models

### Sepedi (Northern Sotho / Sesotho sa Leboa)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele Corpus
- za-mafoko collections

### Tshivenda (Venda)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele Corpus
- za-mafoko collections
- Mafoko Tshivenda Augmented Translations
- Whisper ASR models

### Xitsonga (Tsonga)
- African Next Voices (ZA-ANV)
- Vuk'uzenzele Corpus
- za-mafoko collections
- Whisper ASR models

### Siswati (Swati)
- Siswati News 2022
- Vuk'uzenzele Corpus
- za-mafoko collections

### isiNdebele (Ndebele)
- Vuk'uzenzele Corpus
- za-mafoko collections

### English
- COVID-19 ZA
- ZA Fake News
- Most corpora include English
- AG News Dataset

### Afrikaans
- Vuk'uzenzele Corpus
- za-mafoko collections

### Other African Languages
- Kinyarwanda & Kirundi (Cross-lingual models)
- 40+ languages in Masakhane MT
- African Pre-Trained Embeddings

---

## Datasets by Platform

### HuggingFace 🤗

**Organization**: [dsfsi](https://huggingface.co/dsfsi)
- 22+ datasets, 30+ models
- Collections: za-mafoko, PuoBERTa

**Organization**: [dsfsi-anv](https://huggingface.co/dsfsi-anv)
- African Next Voices dataset (3,000 hours multilingual speech)
- 8 Whisper ASR models

**Browse All**: [HuggingFace DSFSI Datasets](https://huggingface.co/dsfsi)

### GitHub

**Organization**: [github.com/dsfsi](https://github.com/dsfsi)
- 10+ dataset repositories
- Code and preprocessing scripts
- Documentation and papers

### Zenodo

Archived datasets with DOIs for academic citation:
- COVID-19 ZA
- Vuk'uzenzele NLP
- Umsuka Parallel Corpus
- SA News Data
- African Embeddings
- WordNets
- ZA Fake News 2020

### University of Pretoria Repository

- [Loughran McDonald-SA-2020 Sentiment Word List](https://researchdata.up.ac.za/articles/dataset/Loughran_McDonald-SA-2020_Sentiment_Word_List/14401178)
- [ZASCA-Sum](https://researchdata.up.ac.za/articles/journal_contribution/ZASCA-Sum)

### SADiLaR

- [Lwazi Speech Corpus](https://repo.sadilar.org/handle/20.500.12185/7)

### NWU Repository

- [NCHLT Speech Corpus](https://rma.nwu.ac.za/index.php/resource-catalogue/nchlt-speech-corpus.html)

---

## Local Datasets

This repository hosts small-scale datasets locally in the `data/` directory:

### Financial Data
- **JSE Top 40 Stock Performance** (2019-2024)
  - Location: `data/stocks/`
  - Format: CSV and pickle files
  - Contains daily closing prices for Johannesburg Stock Exchange Top 40 companies

### Course Datasets
- **COS781 Datasets** - Customer analytics and retail data
  - Location: `data/cos781/`

- **COS802 Datasets** - Text classification datasets
  - Location: `data/cos802/`

### Kaggle Datasets
- **What's Cooking** - Recipe classification data
  - Location: `data/whats-cooking/`

**Note**: These datasets are version-controlled locally but .gitignore rules are in place for the data/ directory.

---

## How to Use

### Accessing HuggingFace Datasets

```python
from datasets import load_dataset

# Load a dataset
dataset = load_dataset("dsfsi/PuoData")

# Load za-mafoko terminology
terminology = load_dataset("dsfsi/za-mafoko-dsac")

# Load African Next Voices
anv = load_dataset("dsfsi-anv/za-african-next-voices")
```

### Accessing GitHub Repositories

```bash
# Clone a repository
git clone https://github.com/dsfsi/covid19za.git

# Clone this registry
git clone https://github.com/dsfsi/dsfsi-datasets.git
```

### Using HuggingFace Models

```python
from transformers import pipeline

# Load PuoBERTa for masked language modeling
model = pipeline("fill-mask", model="dsfsi/PuoBERTa")

# Load Whisper ASR model
asr = pipeline("automatic-speech-recognition",
               model="dsfsi-anv/multilingual-whisper-v3-turbo")
```

### Working with Local JSE Stock Data

```python
import pandas as pd

# Load stock ticker list
tickers = pd.read_csv("data/stocks/top40_jse_2024.csv")

# Load performance data
performance = pd.read_csv("data/stocks/top40_jse_2024_performance.csv")

# Or load pickle format
performance_df = pd.read_pickle("data/stocks/top40_jse_2024_performance.df")
```

### Citing Datasets

When using our datasets, please cite appropriately:
- Use DOIs from Zenodo/repository pages when available
- Cite associated papers listed in dataset descriptions
- Reference this registry for general dataset discovery

---

## Contributing

We welcome contributions to this registry! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Submitting new datasets
- Updating dataset information
- Reporting issues with datasets
- Proposing improvements to the registry

### Quick Links
- **Publications**: [dsfsi.co.za/publications](https://www.dsfsi.co.za/publications/)
- **Research Group**: [dsfsi.co.za](https://www.dsfsi.co.za)
- **GitHub**: [github.com/dsfsi](https://github.com/dsfsi)
- **HuggingFace**: [huggingface.co/dsfsi](https://huggingface.co/dsfsi)

---

## Citation

If you use datasets from the DSFSI collection, please cite both the specific dataset and this registry:

```bibtex
@misc{dsfsi-datasets-2025,
  title={DSFSI Public Datasets Registry},
  author={{Data Science for Social Impact Research Group}},
  year={2025},
  publisher={University of Pretoria},
  url={https://github.com/dsfsi/dsfsi-datasets}
}
```

For specific datasets, please see individual dataset pages for citation information.

---

## Contact

**Data Science for Social Impact (DSFSI) Research Group**
- **Institution**: University of Pretoria, South Africa
- **Website**: [www.dsfsi.co.za](https://www.dsfsi.co.za)
- **Email**: dsfsi.info@up.ac.za
- **Lead**: Prof Vukosi Marivate (vukosi.marivate@cs.up.ac.za)
- **GitHub**: [github.com/dsfsi](https://github.com/dsfsi)
- **Twitter/X**: [@dsfsi_research](https://twitter.com/dsfsi_research)
- **LinkedIn**: [DSFSI Research Group](https://www.linkedin.com/company/dsfsi)
- **Bluesky**: [@dsfsi.bsky.social](https://bsky.app/profile/dsfsi.bsky.social)

---

## License

- **This registry**: MIT License
- **Individual datasets**: See individual dataset licenses (varies by dataset)
- **Code in this repository**: MIT License
- **Local data**: Various licenses (see dataset-specific documentation)

---

**Last Updated**: December 2025

**Maintained by**: DSFSI Research Group, University of Pretoria
