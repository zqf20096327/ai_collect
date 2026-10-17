# Darija-Translator
### A From-Scratch Tunisian Darija–English NLP Pipeline & Field-Collected Dataset

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-2.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-3DA639?style=for-the-badge" alt="License">
</p>
<p align="center">
  <a href="https://huggingface.co/Dhiadev-tn/darija-translator"><img src="https://img.shields.io/badge/🤗_Model-HuggingFace-FFD21E?style=for-the-badge" alt="Model"></a>
  <a href="https://huggingface.co/datasets/Dhiadev-tn/tunisian-darija-english"><img src="https://img.shields.io/badge/🤗_Dataset-HuggingFace-FFD21E?style=for-the-badge" alt="Dataset"></a>
</p>

---

## 🌍 Why This Exists

I felt a pang in my chest the day I realized how underrepresented my Tunisian dialect is in the digital world.

I searched, and what I found didn't fit: Moroccan datasets that weren't my dialect, and little clean, open Tunisian–English data I could actually build on. So I decided to build my own, openly and from scratch.

This project is not just a translation model. It is a statement. Tunisia is a true standing culture that deserves recognition, and it has minds capable of fighting each day despite limited resources and restricted horizons.

This is a pipeline built entirely from scratch: no shortcuts, no pre-trained foundations, every component written by hand.

What's uncommon here: a small dataset built by hand from real Tunisian speakers, with consent and provenance tracked for every pair.

---

## 🎯 The Problem

**Tunisian Darija is spoken by ~12 million people. It has very limited representation in modern NLP research.**

- Clean, open, parallel Tunisian Darija–English datasets remain scarce
- Existing Arabic NLP tools fail on Tunisian dialect
- Arabizi, the way Tunisians write their dialect using Latin letters and numbers (3→ع, 7→ح, 9→ق, 5→خ), is completely unsupported by standard tokenizers
- The digital world has ignored an entire identity

This project is a step toward changing that.

---

## 🛠️ What Was Built

A complete NLP pipeline built from scratch, starting on an RTX 3050 Laptop (4GB VRAM):

```
vocab.py          → Custom BPE tokenizer with Arabizi support
                    Handles 3, 7, 9, 5 as protected markers
                    16,000 token vocabulary

data_loader.py    → Dataset pipeline
                    35,977 cleaned Darija-English pairs

clean_data.py     → Data cleaning pipeline
                    Removed duplicates, noise, and Moroccan-specific terms

model.py          → Nano-Transformer architecture
                    15.6M parameters
                    Built entirely in PyTorch

train.py          → Full training loop
                    Mixed precision (fp16)
                    Gradient accumulation
                    VRAM-safe (peak: 628MB / 3500MB limit)

finetune.py       → Fine-tuning pipeline
                    500 hand-crafted Tunisian sentence pairs
                    Built manually by a native speaker

split_data.py     → Stratified train/val/test split
                    8 train / 1 val / 1 test per category
                    Ensures honest evaluation on unseen data

evaluate.py       → BLEU scoring on locked test set
                    First honest metric: test set never trained on

inference.py      → Translation interface
```

---

## 📊 The Dataset

### Foundation Layer: Cleaned Moroccan Darija
- **Source**: atlasia/darija_english (HuggingFace)
- **After cleaning**: 35,977 pairs
- **Removed**: 8,736 pairs, duplicates, short pairs, untranslated sentences, Moroccan-specific vocabulary

### Tunisian Layer: Native-speaker written + field-collected
- **500 pairs** self-written and validated by a native speaker, across the first **50 categories** (`self`)
- **53 pairs** field-collected from family and community speakers, with consent and provenance tags, adding **3 further categories** (51-53 below)
- **Zero automated generation**: every pair is either self-written or transcribed from a real speaker; nothing synthetic
- Categories:
  1. greetings
  2. farewells
  3. family
  4. food_drinks
  5. shopping_money
  6. time_directions
  7. emotions_feelings
  8. compliments_insults
  9. school_studying
  10. health_illness
  11. tunisian_slang
  12. tunisian_proverbs
  13. weather
  14. seasons
  15. islamic_expressions
  16. transportation
  17. french_loanwords_darija
  18. cafe_culture
  19. code_switching
  20. wedding_celebrations
  21. hammem_culture
  22. 7ouma_life
  23. ramadan_culture
  24. market_medina
  25. barbershop_culture
  26. bureaucracy_paperwork
  27. football_culture
  28. bac_exam_culture
  29. work_jobseeking
  30. coffee_shop_arguments
  31. louage_culture
  32. 3aylet_gathering
  33. 3rouset_el_7ouma
  34. police_w_dawla
  35. el_ghorba
  36. el_3aza_w_mawt
  37. summer_beach_culture
  38. 3id_el_kbir
  39. el_pharmaci_w_dwa
  40. mawsem_el_zitoun
  41. nhar_el_jom3a
  42. el_hajj_w_el_omra
  43. taxi_culture
  44. military_service
  45. university_life
  46. fishing_culture
  47. political_talk
  48. social_pressure
  49. farming_life
  50. sbitar_culture
  51. memories *(field-collected)*
  52. rural_life *(field-collected)*
  53. daily_life *(field-collected)*

### Current composition (553 pairs, 53 categories)
- **500 pairs**: self-written by a native speaker, across the first 50 categories (`self`)
- **53 pairs**: field-collected from family and community speakers (with consent and provenance tags), introducing **3 new categories**: `memories`, `rural_life`, `daily_life`

Field collection is ongoing; the self-written pairs are the majority of the dataset. See `FIELD_LOG.md` for methodology and consent notes.

### Growing the Dataset (ongoing)
- Collecting from family, community, and everyday Tunisian life: cafes, markets, gatherings
- Multiple sources: self, family members, friends, strangers; every pair provenance-tagged
- Priority is provenance and quality over raw volume; no faked or padded pairs
- Retrain and re-measure BLEU as the dataset grows

---

## ⚙️ Technical Highlights

| Component | Detail |
|-----------|--------|
| Architecture | Encoder-Decoder Transformer |
| Parameters | ~15.6M |
| Tokenizer | SentencePiece BPE: 16,000 tokens, trained on combined Darija+English corpus, shared between source and target, Arabizi-aware |
| Embedding dim | 256 (source + target, weight-tied output layer) |
| Encoder / Decoder | 4 layers each |
| Training data | ~35,000 cleaned Moroccan Darija pairs |
| Pre-training | 15 epochs on Moroccan data (RTX 3050 Laptop, 4GB VRAM) |
| Fine-tuning data | 500 hand-crafted Tunisian pairs, stratified 8/1/1 split |
| Fine-tuning | 20 epochs, best checkpoint by val loss (RTX 4070 Desktop) |
| BLEU score | **3.89** (v1 baseline, June 2026) |
| Model size | ~59.4 MB (float32) |
| Peak VRAM (pre-training) | 628MB out of 3,500MB limit |
| Framework | PyTorch 2.1 + CUDA 12.1 |

> **Architecture note**: The output projection layer shares weights with the target embedding (weight tying), a deliberate design decision that reduces parameters and improves generalization on low-resource translation tasks.

---

## 📈 Current Results

| Metric | Value |
|--------|-------|
| BLEU score | **3.89** (v1 baseline, 500 pairs, June 2026) |
| Best checkpoint | Epoch 7 / 20 (by validation loss) |
| Test set | 50 pairs, locked, never trained on |

The model demonstrates partial understanding of Darija structure. Simple sentences translate with recognizable meaning. Complex cultural expressions reveal the core limitation: **not enough Tunisian data yet.**

This is not a failure. This is the finding.

The pipeline works. The architecture is proven. The data gap is documented firsthand. 3.89 is the baseline to beat. It will improve, retrain by retrain, as the dataset grows through careful, provenance-tagged collection.

---

## 🚀 How To Run It

### Requirements
```bash
Python 3.10+
PyTorch 2.1.0 (CUDA 12.1)
sentencepiece
sacrebleu
```

### Setup
```bash
git clone https://github.com/dhiadev-tn/darija-translator
cd darija-translator
pip install sentencepiece sacrebleu
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

### Train
```bash
python train.py
```

### Translate
```bash
python inference.py
```

### Evaluate
```bash
python evaluate.py
```

---

## 📌 Status

**v1 baseline (June 2026).** The pipeline is built and evaluated; the dataset is growing through
community and crowdsourcing collaboration, with provenance and quality prioritized over volume.

---

## 📜 License

This project is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

You are free to use, share, and build on this work for non-commercial purposes, as long as you credit the author and share your improvements under the same license.

---

## 👤 About

Built by **Dhia** ([@dhiadev-tn](https://github.com/dhiadev-tn)), Tunisia

*This project is a bridge. A link between Tunisia and the digital world. Proof that identity deserves representation, and that the people who carry that identity are capable of building that representation themselves.*

---

> *"No lab. No funding. No mentor. I built it anyway."*
