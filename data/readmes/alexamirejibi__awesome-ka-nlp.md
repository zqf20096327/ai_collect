# Awesome Georgian NLP Resources 🇬🇪

A comprehensive, curated list of Natural Language Processing resources for the Georgian language (ქართული ენა, ISO 639-1: `ka`, ISO 639-3: `kat`). Georgian is a Kartvelian language spoken by ~4 million people, written in the unique Mkhedruli script. It remains classified as a **low-resource language** for NLP, though resources have expanded significantly since 2022.

Current version generated with Claude Deep Research.

---

## Table of Contents

- [Datasets & Corpora](#datasets--corpora)
- [Pretrained Models](#pretrained-models)
- [Tools & Libraries](#tools--libraries)
- [Papers & Research](#papers--research)
- [Tutorials & Courses](#tutorials--courses)
- [Miscellaneous](#miscellaneous)

---

## Datasets & Corpora

### Text Corpora

| Name | Description | Size | License | Link |
|------|-------------|------|---------|------|
| **Georgian National Corpus (GNC)** | Diachronic corpus spanning ~1,600 years (5th c.–present), covering Modern/Middle/Old Georgian, Mingrelian, and Svan. MSD-tagged and lemmatized via Constraint Grammar. Developed by Goethe University Frankfurt & University of Bergen. | ~217M words (~20M morphologically annotated) | CC-BY-NC | [gnc.gov.ge](http://gnc.gov.ge/gnc/page) · [CLARINO](https://clarino.uib.no/gnc) |
| **Georgian Language Corpus (GLC)** | Monolingual and bilingual corpus from Ilia State University (2009–2016). Includes Old/Middle/New Georgian texts (1832–2012). Each word tagged with lemma and morphosyntactic description. | >100M word-forms | Academic | [corpora.iliauni.edu.ge](http://corpora.iliauni.edu.ge/) |
| **Georgian Wikipedia Dumps** | Full Georgian Wikipedia articles, regularly updated. ~188K articles as of late 2025. | ~188K articles | CC-BY-SA 3.0 | [dumps.wikimedia.org/kawiki](https://dumps.wikimedia.org/kawiki/) · [HuggingFace](https://huggingface.co/datasets/legacy-datasets/wikipedia) |
| **OSCAR Corpus (ka)** | Web-crawled multilingual corpus from Common Crawl with language identification. Georgian subset available across multiple versions. | Varies by version | CC0 annotations / CC ToU for text | [HuggingFace OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) · [oscar-project.org](https://oscar-project.org/) |
| **CC-100 (ka)** | Monolingual data from Common Crawl (2018) extracted via CCNet pipeline. Used for XLM-R training. | **1.1 GB** | Common Crawl ToU | [data.statmt.org/cc-100](http://data.statmt.org/cc-100/) · [HuggingFace](https://huggingface.co/datasets/statmt/cc100) |
| **mC4 (ka)** | Multilingual C4 corpus used for mT5 pre-training. Georgian subset included. Quality may vary for low-resource languages. | Varies | Common Crawl ToU | [HuggingFace](https://huggingface.co/datasets/allenai/c4) |
| **CulturaX (ka)** | Cleaned combination of mC4 + OSCAR. 6.3 trillion tokens across 167 languages including Georgian. | Part of 6.3T tokens | Research | [HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX) |
| **GeoWordsDatabase** | Database of ~310,000 unique Georgian words in MySQL format. | ~310K words | Open | [GitHub](https://github.com/bumbeishvili/GeoWordsDatabase) · [Web](https://bumbeishvili.github.io/GeoWordsDatabase/) |
| **RichNachos Georgian Corpus** | Community-contributed Georgian text corpus on HuggingFace. | — | — | [HuggingFace](https://huggingface.co/datasets/RichNachos/georgian-corpus) |
| **Georgian Dialect Corpus** | Dialectal data integrated into the GNC. Covers geographical varieties of Georgian. | — | Academic | Integrated into GNC |
| **geo-words** | Georgian words database (txt, dic, sql) + CLI web crawler. | — | Open | [GitHub (akalongman)](https://github.com/akalongman/geo-words) |

### Parallel Corpora

| Name | Description | Size | License | Link |
|------|-------------|------|---------|------|
| **OPUS Collection (ka)** | Largest open collection of parallel corpora. Georgian available in OpenSubtitles, WikiMatrix, CCAligned, GNOME/KDE/Ubuntu, Tanzil, QED, Tatoeba, and more. | Multiple sub-corpora | Varies | [opus.nlpl.eu](https://opus.nlpl.eu/) |
| **OPUS-100 (en-ka)** | English-Georgian parallel pairs from OPUS. | — | Open | [HuggingFace](https://huggingface.co/datasets/Helsinki-NLP/opus-100) |
| **FLoRes-200 / FLORES+** | Meta's n-way parallel MT benchmark including Georgian (`kat_Geor`). | ~2,000 sentences | CC-BY-SA 4.0 | [GitHub](https://github.com/facebookresearch/flores) · [HuggingFace](https://huggingface.co/datasets/openlanguagedata/flores_plus) |
| **GLC Bilingual Sub-corpora** | Georgian-English parallel "Vepkhistkaosani" (The Knight in the Panther's Skin) and Georgian-Armenian "Kartlis Tskhovreba" (Georgian Chronicles). | — | Academic | [corpora.iliauni.edu.ge](http://corpora.iliauni.edu.ge/) |
| **tbilisi-ai-lab/en-ka-human-translated** | Human-translated EN↔KA parallel pairs from Tbilisi AI Lab. | 5K pairs | — | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/en-ka-human-translated) |

### Treebanks

| Name | Description | Size | License | Link |
|------|-------------|------|---------|------|
| **UD_Georgian-GLC** | First Georgian treebank in Universal Dependencies framework. Based on GLC sentences and 3,013 Wikipedia sentences across 131 scientific domains. CoNLL-U format. | ~60K tokens (3,013 sentences) | CC BY-SA | [GitHub](https://github.com/UniversalDependencies/UD_Georgian-GLC) · [UD page](https://universaldependencies.org/treebanks/ka_glc/index.html) |
| **UD_Georgian-GNC** | Treebank from the Georgian National Corpus texts (novels and news). Uses finite-state morphological analyzer + Constraint Grammar, manually corrected. | ~22K tokens | UD license | [GitHub](https://github.com/UniversalDependencies/UD_Georgian-GNC) |
| **GRUG Parallel Treebank** | Georgian-Russian-Ukrainian-German parallel treebank. Syntactically annotated using TIGER guidelines. Viewable via Stockholm TreeAligner. | 4 monolingual + 4 parallel treebanks | CC-BY 3.0 | [CLARIN-D](https://fedora.clarin-d.uni-saarland.de/grug/) |

### NER Datasets

| Name | Description | License | Link |
|------|-------------|---------|------|
| **WikiANN / PAN-X (ka)** | Multilingual NER dataset from Wikipedia. Georgian is one of 176 languages. Tags: LOC, PER, ORG in IOB2 format. | Research use | [HuggingFace](https://huggingface.co/datasets/unimelb-nlp/wikiann) |

### Sentiment & Classification Datasets

| Name | Description | License | Link |
|------|-------------|---------|------|
| **JRC Georgian Sentiment Dataset** | First publicly available annotated dataset for Georgian sentiment classification + semantic polarity dictionary. 3-label and 4-label settings. From the European Commission Joint Research Centre. | Open | [JRC Data Catalogue](https://data.jrc.ec.europa.eu/dataset/9f04066a-8cc0-4669-99b4-f1f0627fdbbf) |
| **senti_lex (ka)** | Sentiment lexicons for 81 languages including Georgian. | — | [HuggingFace](https://huggingface.co/datasets/senti_lex) |

### Speech Corpora

| Name | Description | Size | License | Link |
|------|-------------|------|---------|------|
| **Mozilla Common Voice (ka)** | Crowd-sourced read speech with transcriptions. Primary resource for Georgian ASR. | **~76h validated** | CC-0 | [commonvoice.mozilla.org](https://commonvoice.mozilla.org/) · [HuggingFace (v17)](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0) |
| **FLEURS (ka_ge)** | Google's Few-shot Learning Evaluation of Universal Representations of Speech. N-way parallel speech benchmark in 102 languages. | ~12h per language | CC-BY 4.0 | [HuggingFace](https://huggingface.co/datasets/google/fleurs) |
| **IARPA Babel Georgian (LDC2016S12)** | Conversational and scripted telephone speech (Eastern/Western dialects). Equal gender distribution, ages 16–73. | **~190 hours** | LDC license | [LDC Catalog](https://catalog.ldc.upenn.edu/LDC2016S12) |
| **MATERIAL Georgian-English (LDC2025S01)** | Georgian-English ASR and MT resources for cross-lingual information retrieval. IARPA MATERIAL program. | — | LDC license | LDC2025S01 |
| **OpenSLR 153** | Georgian crowd-sourced speech data. Part of effort achieving 5.73% WER for Georgian. | — | CC-BY-SA 4.0 | [OpenSLR](https://www.openslr.org/153) |
| **CommonLanguage (SpeechBrain)** | Speech recordings from CommonVoice for 45 languages including Georgian, curated for language identification. | ~1h Georgian | CC-0 | [HuggingFace](https://huggingface.co/datasets/speechbrain/common_language) |

### Tbilisi AI Lab Datasets (Instruction-Tuning & Benchmarks)

The **Tbilisi AI Lab** released 19+ datasets for training and evaluating Georgian LLMs (October 2025):

| Name | Size | Description | Link |
|------|------|-------------|------|
| **kona-sft-mix-2.6M** | 2.61M pairs | Instruction/SFT training mix | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/kona-sft-mix-2.6M) |
| **kona-dpo-mix-387k** | 387K pairs | DPO preference alignment data | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/kona-dpo-mix-387k) |
| **kona-sft-function-calling-ka-93k** | 93K | Function-calling SFT data (Georgian) | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/kona-sft-function-calling-ka-93k) |
| **kona-sft-function-calling-115k** | 115K | Function-calling SFT data (English) | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/kona-sft-function-calling-115k) |
| **wiki-ka-QA** | 42.6K | Wikipedia-based QA in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/wiki-ka-QA) |
| **code-instruct-ka** | 61.3K | Code instruction in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/code-instruct-ka) |
| **math-instruct-ka** | 32.4K | Math instruction in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/math-instruct-ka) |
| **learnlm-chat-ka** | 5.86K | Educational chat data in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/learnlm-chat-ka) |
| **ai2_arc-ka** | 1.68K | ARC benchmark translated to Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/ai2_arc-ka) |
| **boolq-ka** | 3.27K | BoolQ benchmark in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/boolq-ka) |
| **commonsense_qa-ka** | 1.22K | CommonsenseQA in Georgian | [HuggingFace](https://huggingface.co/datasets/tbilisi-ai-lab/commonsense_qa-ka) |

Browse all: [huggingface.co/tbilisi-ai-lab](https://huggingface.co/tbilisi-ai-lab)

### Evaluation & Benchmark Datasets

| Name | Description | Link |
|------|-------------|------|
| **Georgian Case-Alignment Syntactic Tests** | 370 syntactic tests for evaluating LMs on Georgian split-ergative case system (nominative-dative, ergative-nominative, dative-nominative). Generated from GLC UD treebank. | [HuggingFace](https://huggingface.co/datasets/DanielGallagherIRE/georgian-case-alignment) · [GitHub](https://github.com/DanielGall500/georgian-case-alignment) |
| **GeoLogicQA** | 100-question benchmark for evaluating LLM logical reasoning in Georgian. From TSU. | [ACL Anthology](https://aclanthology.org/2025.lowresnlp-1.13.pdf) |

---

## Pretrained Models

### Georgian-Specific Language Models

| Name | Architecture | Params | Training Data | Tasks | Link |
|------|-------------|--------|---------------|-------|------|
| **Kona2-12B** | Causal LM | 12B | Georgian-first training data | Text generation | [HuggingFace](https://huggingface.co/tbilisi-ai-lab/kona2-12B) |
| **Kona2-12B-Instruct** | Causal LM | 12B | SFT + DPO alignment | Instruction following, function calling | [HuggingFace](https://huggingface.co/tbilisi-ai-lab/kona2-12B-Instruct) |
| **Kona2-12B-Base** | Causal LM | 12B | Pre-instruct base model | Base model | [HuggingFace](https://huggingface.co/tbilisi-ai-lab/kona2-12B-Base) |
| **Kona2-small-3.8B** | Causal LM | 3.8B | Georgian-first training data | Text generation | [HuggingFace](https://huggingface.co/tbilisi-ai-lab/kona2-small-3.8B) |
| **mGPT-1.3B-Georgian** | GPT-2 | 1.3B | Wikipedia + C4, fine-tuned 10K steps on Georgian | Text generation | [HuggingFace](https://huggingface.co/ai-forever/mGPT-1.3B-georgian) |
| **electra-ka** | ELECTRA | BERT-base | 33GB Georgian text from ~4.85M CommonCrawl pages | Feature extraction, fine-tuning base | [HuggingFace](https://huggingface.co/jnz/electra-ka) · [GitHub](https://github.com/davitjnz/electra-ka) |
| **georgian-distilbert-mlm** | DistilBERT | base | mC4 Georgian subset | Fill-mask, feature extraction | [HuggingFace](https://huggingface.co/Davit6174/georgian-distilbert-mlm) |
| **gpt2-ka-wiki** | GPT-2 | small | Georgian Wikipedia | Text generation | [HuggingFace](https://huggingface.co/GiorgiSekhniashvili/gpt2-ka-wiki) |
| **gpt2-geo** | GPT-2 | small | Georgian text (limited training) | Text generation | [HuggingFace](https://huggingface.co/Kuduxaaa/gpt2-geo) |

> **Note:** The **Kona2 family** from Tbilisi AI Lab (released October 2025) represents the most comprehensive Georgian-first LLM effort to date.

### Fine-Tuned Georgian Task Models

| Name | Base Model | Task | Link |
|------|-----------|------|------|
| **electra-ka-discrediting** | electra-ka | Discrediting text detection | [HuggingFace](https://huggingface.co/jnz/electra-ka-discrediting) |
| **electra-ka-fake-news-tagging** | electra-ka | Fake news classification | [HuggingFace](https://huggingface.co/jnz/electra-ka-fake-news-tagging) |
| **stefan-it Georgian NER Models** | XLM-R Large + Flair | Named entity recognition (LOC, PER, ORG) | [GitHub](https://github.com/stefan-it/georgian-ner) · [HuggingFace collection](https://huggingface.co/stefan-it) |

### Georgian Translation Models

| Name | Architecture | Direction | Link |
|------|-------------|-----------|------|
| **opus-mt-ka-en** | Marian/Transformer | Georgian → English | [HuggingFace](https://huggingface.co/Helsinki-NLP/opus-mt-ka-en) |
| **opus-mt-en-ka** | Marian/Transformer | English → Georgian | [HuggingFace](https://huggingface.co/Helsinki-NLP/opus-mt-en-ka) |
| **english-georgian** | T5-small (fine-tuned) | English → Georgian | [HuggingFace](https://huggingface.co/SoyGema/english-georgian) |

### Georgian Speech Recognition Models

| Name | Architecture | Training Data | WER | Link |
|------|-------------|---------------|-----|------|
| **NVIDIA stt_ka_fastconformer** | FastConformer Hybrid CTC-Transducer (~115M) | Common Voice + FLEURS (~163h) | **5.73%** | [HuggingFace](https://huggingface.co/nvidia/stt_ka_fastconformer_hybrid_large_pc) |
| **whisper-large-v2-ka** | Whisper Large V2 | Common Voice 11.0 (ka) | 31.85% | [HuggingFace](https://huggingface.co/anuragshas/whisper-large-v2-ka) |
| **wav2vec2-xlsr-georgian (sammy786)** | Wav2Vec2-XLS-R-1B | Common Voice 8.0 (ka) | — | [HuggingFace](https://huggingface.co/sammy786/wav2vec2-xlsr-georgian) |
| **wav2vec2-large-xlsr-georgian (m3hrdadfi)** | Wav2Vec2-XLSR-53 | Common Voice (ka) | — | [HuggingFace](https://huggingface.co/m3hrdadfi/wav2vec2-large-xlsr-georgian) |
| **wav2vec2-large-xlsr-georgian (xsway)** | Wav2Vec2-XLSR-53 | Common Voice (ka) | — | [HuggingFace](https://huggingface.co/xsway/wav2vec2-large-xlsr-georgian) |

> **Note:** The **NVIDIA FastConformer** model (5.73% WER) is the current state of the art for Georgian ASR, significantly outperforming Whisper Large V3 and Meta Seamless.

### Word Embeddings

| Name | Type | Dimensions | Training Data | Link |
|------|------|-----------|---------------|------|
| **fastText Common Crawl+Wikipedia (ka)** | CBOW with character n-grams | 300 | Common Crawl + Wikipedia | [fasttext.cc](https://fasttext.cc/docs/en/crawl-vectors.html) → `cc.ka.300.bin` |
| **fastText Wikipedia (ka)** | Skip-gram | 300 | Wikipedia | [fasttext.cc](https://fasttext.cc/docs/en/pretrained-vectors.html) → `wiki.ka` |
| **georgian-word2vec** | Word2Vec (Gensim) | — | Georgian Wikipedia dump | [GitHub](https://github.com/t1t0n/georgian-word2vec) |
| **Georgian_Word_Embedding** | FastText + Word2Vec | — | Georgian text | [GitHub](https://github.com/anz2/Georgian_Word_Embedding) |
| **ConceptNet Numberbatch** | Hybrid (word2vec + GloVe + ConceptNet) | 300 | Multilingual, includes `ka` | [GitHub](https://github.com/commonsense/conceptnet-numberbatch) |

### Multilingual Models with Georgian Support

These major multilingual models include Georgian in their training data and can be used for Georgian NLP tasks directly or via fine-tuning:

**Encoders (BERT-family):**
| Name | Languages | Link |
|------|-----------|------|
| **mBERT** (bert-base-multilingual-cased) | 104 languages (incl. ka) | [HuggingFace](https://huggingface.co/google-bert/bert-base-multilingual-cased) |
| **XLM-RoBERTa Base** | 100 languages (incl. ka) | [HuggingFace](https://huggingface.co/FacebookAI/xlm-roberta-base) |
| **XLM-RoBERTa Large** | 100 languages (incl. ka) | [HuggingFace](https://huggingface.co/FacebookAI/xlm-roberta-large) |
| **XLM-RoBERTa XL** | 100 languages (incl. ka), 3.5B params | [HuggingFace](https://huggingface.co/facebook/xlm-roberta-xl) |

**Generative:**
| Name | Languages | Link |
|------|-----------|------|
| **mGPT** (ai-forever) | 61 languages (incl. ka), 1.3B | [HuggingFace](https://huggingface.co/ai-forever/mGPT) |
| **mGPT-13B** | 60+ languages (incl. ka), 13B | [HuggingFace](https://huggingface.co/ai-forever/mGPT-13B) |

**Translation:**
| Name | Languages | Link |
|------|-----------|------|
| **NLLB-200** (Meta) | 200 languages (Georgian: `kat_Geor`) | [600M](https://huggingface.co/facebook/nllb-200-distilled-600M) · [1.3B](https://huggingface.co/facebook/nllb-200-1.3B) · [3.3B](https://huggingface.co/facebook/nllb-200-3.3B) |
| **M2M-100** (Meta) | 100 languages (incl. ka) | [418M](https://huggingface.co/facebook/m2m100_418M) · [1.2B](https://huggingface.co/facebook/m2m100_1.2B) |
| **SMaLL-100** | 100 languages (incl. ka) | [HuggingFace](https://huggingface.co/alirezamsh/small100) |

**Speech:**
| Name | Languages | Link |
|------|-----------|------|
| **Whisper** (OpenAI) | 96+ languages (incl. ka) | [Large V2](https://huggingface.co/openai/whisper-large-v2) · [Large V3](https://huggingface.co/openai/whisper-large-v3) |
| **XLS-R** (Meta) | 128 languages, base for fine-tuning | [1B](https://huggingface.co/facebook/wav2vec2-xls-r-1b) |

---

## Tools & Libraries

### NLP Toolkits

| Name | Description | Language | Status | Link |
|------|-------------|----------|--------|------|
| **Stanza (Stanford NLP)** | Full NLP pipeline for Georgian: tokenization, POS tagging, lemmatization, dependency parsing. Uses UD 2.15 models. `stanza.download("ka")` | Python | ✅ Active (2025) | [GitHub](https://github.com/stanfordnlp/stanza) |
| **spaCy (via spacy-stanza)** | Georgian support via spacy-stanza bridge. `spacy_stanza.load_pipeline("xx", lang="ka")` | Python | ✅ Active | [spacy-stanza](https://github.com/explosion/spacy-stanza) |
| **Anbani.py** | Georgian toolkit: script conversion (Mkhedruli, Asomtavruli, Nuskhuri), Latin↔Georgian transliteration, text classification. `pip install anbani` | Python | ✅ Active | [GitHub](https://github.com/Anbani/anbani.py) |
| **Anbani.js** | Script conversion, transliteration, Lorem Ipsum, letter frequency analysis, Friedman index. | JavaScript | ✅ Active | [GitHub](https://github.com/Anbani/anbani.js) |
| **QartNLPWebService** | Georgian NLP Toolset (Flask web service). Developed at Ilia State University / Unilab. | Python | ⚠️ Last updated Aug 2022 | [GitHub](https://github.com/UnilabEdu/QartNLPWebService) |
| **Georgian Language Toolkit** | Latinize/Georgianize strings, language detection (ka/en), morphological operations, Django slug generation. | Ruby, Python | ⚠️ Last updated Mar 2021 | [GitHub](https://github.com/tigeorgia/georgian-language-toolkit) |
| **georgian-linguistics-tools** | UTF-8 Georgian text handling, Latin transcription for C++ applications. | C++ | ⚠️ Likely unmaintained | [GitHub](https://github.com/panoptical/georgian-linguistics-tools) |

### Morphological Analysis

| Name | Description | Link |
|------|-------------|------|
| **FST Morphological Analyzer (Lobzhanidze)** | Comprehensive finite-state analyzer/generator for Modern Georgian using XEROX tools (xfst, lexc). Covers all POS and verb paradigms. Used in GLC annotation. | [Springer Book (2022)](https://doi.org/10.1007/978-3-030-90248-3) |
| **GNC Morphological Analyzer (Meurer)** | FST analyzer + Constraint Grammar disambiguation for Old/Middle/Modern Georgian in the GNC. | [Documentation](https://clarino.uib.no/gnc/doc/Morphosyntactic-analysis-of-Georgian.pdf) |
| **FST + FCFG Parser (Kapanadze)** | Finite-state morphological transducer/POS-tagger combined with Feature-Based CFG parser for syntactic chunking. | [TbiLLC 2023 Paper](https://archive.illc.uva.nl/Tbilisi/Tbilisi2023/uploaded_files/inlineitem/Kapanadze_.pdf) |
| **UniMorph (Georgian)** | Morphological paradigm tables for Georgian, including polypersonal verb agreement. | [unimorph.github.io](https://unimorph.github.io/) |

### Spell Checkers

| Name | Description | Link |
|------|-------------|------|
| **ka_GE.spell (Hunspell)** | Georgian orthographic spell-checking dictionary for Firefox, LibreOffice, Chrome. Auto-generated word lists from web crawling. MIT License. | [GitHub](https://github.com/gamag/ka_GE.spell) |
| **Georgian Seq2Seq Spellchecker** | Character-level spellchecker using GRU Seq2Seq model with synthetic typo dataset. | [GitHub (Dec 2025)](https://github.com/topics/georgian-language) |
| **gegram-class** | Library for replacing barbarisms in Georgian sentences. | Java |

### Transliteration & Script Tools

| Name | Description | Link |
|------|-------------|------|
| **translitit-latin-to-mkhedruli-georgian** | Latin → ქართული (Mkhedruli) transliteration function. | JavaScript |
| **translitit-mkhedruli-georgian-to-ipa** | Mkhedruli Georgian → IPA transliteration function. | JavaScript |
| **KartuliChromeExtension** | Chrome extension converting English letters to Georgian equivalents. | Chrome Web Store |
| **kautilities** | Convert Georgian ↔ Latin letters. | [PHP](https://github.com/akalongman/kautilities) |

### OCR Tools

| Name | Description | Link |
|------|-------------|------|
| **Tesseract OCR (kat)** | Google's Tesseract supports Georgian via trained data (`kat.traineddata`). | [tessdata](https://github.com/tesseract-ocr/tessdata) |
| **tesseract-georgian** | Training data for Tesseract on Georgian, derived from Wikipedia dumps. Includes wordlists and bigrams. | [GitHub](https://github.com/ddohler/tesseract-georgian) |

### TTS / STT Systems

| Name | Type | Description | Link |
|------|------|-------------|------|
| **NVIDIA FastConformer Georgian** | STT | State-of-the-art Georgian ASR (5.73% WER). NeMo toolkit. CC-BY-4.0. | [HuggingFace](https://huggingface.co/nvidia/stt_ka_fastconformer_hybrid_large_pc) |
| **ElevenLabs Georgian TTS** | TTS | Neural TTS using Eleven Multilingual v2/v3 models. Supports voice cloning. | [elevenlabs.io](https://elevenlabs.io/text-to-speech/georgian) |
| **ElevenLabs Scribe Georgian** | STT | Georgian transcription (5–10% WER). Speaker diarization support. | [elevenlabs.io](https://elevenlabs.io/speech-to-text/georgian) |
| **Google Cloud STT (ka-GE)** | STT | Georgian speech-to-text via Google Cloud API. | [cloud.google.com](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages) |
| **eSpeak NG** | TTS | Open-source formant-based TTS. Georgian supported but at early stage with limited quality. | [GitHub](https://github.com/espeak-ng/espeak-ng) |
| **Georgian eSpeak Chrome Extension** | TTS | Browser extension reading Georgian text aloud using eSpeak.js. | [GitHub](https://github.com/gmirian/Georgian-eSpeak-Chrome-Extension) |
| **Georgian-TTS** | TTS | Georgian text-to-speech synthesis system (research). | [GitHub](https://github.com/icegas/Georgian-TTS) |
| **KaRead** | TTS | Experimental TTS for Georgian using Fourier transform letter frequency analysis. | [GitHub](https://github.com/LongToeBoy/KaRead) |

> **Note:** Google Cloud TTS does **not** currently offer Georgian voice synthesis (only STT). For neural TTS, ElevenLabs is currently the primary commercial option.

### Machine Translation

| Name | Description | Link |
|------|-------------|------|
| **Google Translate** | Georgian fully supported (GNMT). | [translate.google.com](https://translate.google.com/) |
| **Google Cloud Translation API** | Georgian supported (NMT model). | [cloud.google.com](https://docs.cloud.google.com/translate/docs/languages) |
| **Meta NLLB-200** | 200 languages including Georgian (`kat_Geor`). Open-sourced. | [ai.meta.com](https://ai.meta.com/research/no-language-left-behind/) |
| **Microsoft Translator** | Georgian supported. | [microsoft.com](https://www.microsoft.com/en-us/translator/) |
| **Lingvanex** | Commercial Georgian NLP services (tokenization, NER, sentiment, MT). | [lingvanex.com](https://lingvanex.com/services/georgian-nlp/) |

### Utility Libraries

| Name | Description | Language | Link |
|------|-------------|----------|------|
| **GeoParaphrase (Gadawere)** | First Georgian paraphrasing/summarization tool (~10K+ users). | React + Express | [GitHub](https://github.com/Vashakmadze/GeoParaphrase) |
| **num2geotext** | Convert numbers to Georgian text and currency. | Python | [GitHub](https://github.com/topics/georgian-language) |
| **dimakura/ka** | Common functionality for Georgian projects. | Ruby |
| **dimakura/ka.js** | Georgian language support for Node.js. | JavaScript |
| **Stichoza/money-num-to-string** | Convert numbers/money to localized Georgian strings. | PHP, JS |
| **Declensions for Georgian** | Generate declensions for Georgian words. | — |

---

## Papers & Research

### Morphology & Morphological Analysis

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| A Finite-State Model of Georgian Verbal Morphology | Gurevich | 2006 | NAACL 2006 | [ACL Anthology](https://aclanthology.org/N06-2012.pdf) |
| Describing Georgian Morphology with a Finite-State System | Kapanadze | 2010 | FSMNLP 2009, Springer LNCS | [Springer](https://link.springer.com/chapter/10.1007/978-3-642-14684-8_12) |
| Morphological Reinflection with Multiple Arguments: An Extended Annotation Schema and a Georgian Case Study | Guriel, Goldman, Tsarfaty | 2022 | ACL 2022 (Short Papers) | [ACL Anthology](https://aclanthology.org/2022.acl-short.21/) |
| Universal Morphologies for the Caucasus Region | Chiarcos, Donandt, Ionov, Rind-Pawlowski et al. | 2018 | LREC 2018 | [ACL Anthology](https://aclanthology.org/L18-1417/) |
| Automatic Morphological Analysis and Syntactic Parsing for the Georgian Language | Kapanadze, Kapanadze | 2026 | TbiLLC 2023, Springer | [Springer](https://link.springer.com/chapter/10.1007/978-3-032-14339-6_4) |
| Finite-State Computational Morphology: An Analyzer and Generator for Georgian | Lobzhanidze | 2022 | Springer (book) | [Springer](https://doi.org/10.1007/978-3-030-90248-3) |

### Treebanks & Syntax

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Building a Universal Dependencies Treebank for Georgian | Lobzhanidze, Magradze, Berikashvili et al. | 2024 | TLT 2024 | [ACL Anthology](https://aclanthology.org/2024.tlt-1.5/) |
| Building Resources for Georgian Treebanking-Based NLP | Kapanadze, Kotzé, Hanneforth | 2022 | TbiLLC 2019, Springer LNCS | [ACM/Springer](https://dl.acm.org/doi/10.1007/978-3-030-98479-3_4) |
| A Computational Grammar for Georgian | Kapanadze | 2009 | Logic, Language, and Computation, Springer | [Springer](https://dl.acm.org/doi/10.1007/978-3-642-00665-4_1) |

### Tokenization

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| A Comparison of Different Tokenization Methods for the Georgian Language | Mikaberidze, Saghinadze, Mikaberidze, Kalandadze, Pkhakadze, van Genabith, Ostermann, van der Plas, Müller | 2024 | ICNLSP 2024 | [ACL Anthology](https://aclanthology.org/2024.icnlsp-1.22/) |

### Sentiment Analysis & Text Classification

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Resources and Experiments on Sentiment Classification for Georgian | Stefanovitch, Piskorski, Kharazi | 2022 | LREC 2022 | [ACL Anthology](https://aclanthology.org/2022.lrec-1.173/) |
| Toxicity Detection in Online Georgian Discussions | Lashkarashvili, Tsintsadze | 2022 | Int'l Journal of Information Management Data Insights | [Elsevier](https://doi.org/10.1016/j.jjimei.2022.100062) |

### Lemmatization & POS Tagging

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Lemmatization and POS-tagging process by using joint learning approach (Classical Armenian, Old Georgian, Syriac) | Vidal-Gorène, Kindt | 2020 | LT4HALA (LREC 2020) | [ACL Anthology](https://aclanthology.org/2020.lt4hala-1.4/) |
| Under-resourced studies of under-resourced languages: lemmatization and POS-tagging with LLM annotators for historical Armenian, Georgian, Greek and Syriac | Vidal-Gorène et al. | 2025 | arXiv | [arXiv:2602.15753](https://arxiv.org/abs/2602.15753) |
| A theory for words in Georgian: traditional constructs versus corpus annotation | Daraselia et al. | 2024 | Corpus Linguistics and Linguistic Theory | [De Gruyter](https://www.degruyterbrill.com/document/doi/10.1515/cllt-2023-0107/html) |

### Word Sense Disambiguation

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Homonym Sense Disambiguation in the Georgian Language | — | 2024 | arXiv | [arXiv:2405.00710](https://arxiv.org/abs/2405.00710) |

### LLM Evaluation & Syntactic Evaluation

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Targeted Syntactic Evaluation of Language Models on Georgian Case Alignment | — | 2025 | arXiv | [arXiv:2602.10661](https://arxiv.org/abs/2602.10661) |
| GeoLogicQA – A Benchmark for Evaluating Logical Reasoning in Georgian for LLMs | Koberidze, Elizbarashvili, Tsintsadze | 2025 | LowResNLP @ RANLP 2025 | [ACL Anthology](https://aclanthology.org/2025.lowresnlp-1.13.pdf) |
| Evaluating and Mitigating Linguistic Discrimination in Large Language Models | — | 2024 | arXiv | [arXiv:2404.18534](https://arxiv.org/abs/2404.18534) |

### Speech Recognition

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Developing Robust Georgian ASR with FastConformer Hybrid Transducer CTC BPE | — | 2024 | NVIDIA Blog + arXiv | [NVIDIA Blog](https://developer.nvidia.com/blog/developing-robust-georgian-automatic-speech-recognition-with-fastconformer-hybrid-transducer-ctc-bpe/) · [arXiv:2501.14788](https://arxiv.org/pdf/2501.14788) |
| Fast Multi-language LSTM-based Online Handwriting Recognition | Carbune et al. | 2020 | IJDAR / arXiv | [arXiv:1902.10525](https://arxiv.org/abs/1902.10525) |

### OCR & Handwriting Recognition

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| On Georgian Handwritten Character Recognition | Tsintsadze et al. | 2018 | IFAC-PapersOnLine | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405896318329525) |
| Optical Character Recognition Tool for Georgian Handwritten Text Recognition Based on YOLOv8 | — | ~2024 | ResearchGate | [ResearchGate](https://www.researchgate.net/publication/393691921) |

### Corpus & Language Resources

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Structuring a Diachronic Corpus: The Georgian National Corpus Project | Gippert et al. | 2012–2016 | EURALEX 2016 and others | [CLARINO](https://clarino.uib.no/gnc) |
| Enhancement Possibilities for the Georgian National Corpus | Kamarauli | 2024 | Caucasus Journal of Social Sciences | [Journal](https://cjss.ug.edu.ge/index.php/cjss/article/view/292) |
| Creating Corpus for Georgian Language Modelling | — | — | OpenReview | [OpenReview](https://openreview.net/forum?id=NNnOfMUqqGC) |

### Multilingual Works Including Georgian

| Title | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| mGPT: Few-shot learners go multilingual | Shliazhko et al. | 2024 | Computational Linguistics | — |
| UniMorph 3.0: Universal Morphology | McCarthy, Kirov et al. | 2020 | LREC 2020 | — |
| Functional and Cognitive Analysis of Grammar in Georgian Using the BERT Model | — | ~2024 | Language and Culture journal | [4science.ge](https://journals.4science.ge/index.php/enadakultura/article/view/3710) |

---

## Tutorials & Courses

### Tutorials & Projects

| Name | Type | Description | Link |
|------|------|-------------|------|
| **Georgian Language Model (BiLSTM)** | GitHub Project | Compares n-gram (perplexity 415K), Transformer (729), and BiLSTM (24) for Georgian text generation. Includes trained word2vec models. | [GitHub](https://github.com/NLP-Georgian-Language-Modeling/Georgian-Language-Model) |
| **electra-ka Training Code** | GitHub Repo | Code and instructions for training ELECTRA on 33GB Georgian text. Includes fine-tuning examples for sequence classification. | [GitHub](https://github.com/davitjnz/electra-ka) |
| **Tokenization Comparison Code** | GitHub Repo | Code for comparing BPE, WordPiece, SentencePiece tokenizers on Georgian downstream tasks. 30 stars, active (Jan 2026). | [ACL Paper](https://aclanthology.org/2024.icnlsp-1.22/) |
| **NLP Text Classification for Georgian Medical Records** | Research Paper | SVM/KNN text classification for Georgian medical records; includes Georgian stemming and stop-word removal. | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5030470/) |
| **NVIDIA Georgian ASR Blog** | Tutorial/Blog | Step-by-step development of Georgian ASR with FastConformer. Covers data preparation, tokenizer creation, training. | [NVIDIA Blog](https://developer.nvidia.com/blog/developing-robust-georgian-automatic-speech-recognition-with-fastconformer-hybrid-transducer-ctc-bpe/) |

### Conferences with Georgian NLP Content

| Name | Description | Link |
|------|-------------|------|
| **TbiLLC** | International Tbilisi Symposium on Logic, Language, and Computation. Biennial. Proceedings in Springer LNCS. | [Events page](https://events.illc.uva.nl/Tbilisi/Tbilisi2023/) · [Springer](https://link.springer.com/conference/tbillc) |
| **LMT Tbilisi 2022** | Computational Modeling of Language conference at TSU Arnold Chikobava Institute of Linguistics. | [LinguistList](https://old.linguistlist.org/issues/33/33-1728.html) |
| **LowResNLP (RANLP)** | Workshop on low-resource NLP, featuring Georgian benchmarks. | [ACL Anthology](https://aclanthology.org/volumes/2025.lowresnlp-1/) |

---

## Miscellaneous

### Unicode Information

Georgian uses **three Unicode blocks** covering four script styles:

| Block | Range | Characters | Contents |
|-------|-------|-----------|----------|
| **Georgian** | U+10A0–U+10FF | 96 | Asomtavruli (capitals, U+10A0–U+10CF) + Mkhedruli (modern lowercase, U+10D0–U+10FF) |
| **Georgian Supplement** | U+2D00–U+2D2F | 40 | Nuskhuri (ecclesiastical lowercase) |
| **Georgian Extended** | U+1C90–U+1CBF | 48 | Mtavruli (modern capitals, added Unicode 11.0, June 2018) |

- Modern Georgian uses **33 Mkhedruli letters** (5 archaic letters are obsolete)
- Georgian is primarily **unicameral** (no case distinction in standard usage), which simplifies text normalization for NLP
- Official Unicode chart: [U+10A0 PDF](https://www.unicode.org/charts/PDF/U10A0.pdf) · [U+1C90 PDF](https://www.unicode.org/charts/PDF/U1C90.pdf)
- Detailed orthography notes: [r12a.github.io](https://r12a.github.io/scripts/geor/ka)
- Interactive codepoint explorer: [symbl.cc](https://symbl.cc/en/unicode/blocks/georgian/) · [codepoints.net](https://codepoints.net/georgian?lang=en)

### Keyboard Layouts

| Name | Description | Link |
|------|-------------|------|
| **Georgian QWERTY** (most popular) | Standard keyboard layout for Georgian. | [kbdlayout.info](http://kbdlayout.info/kbdgeoqw/) |
| **Georgian Standard** (JCUKEN-based) | Government standard layout. | [Wikipedia](https://en.wikipedia.org/wiki/Georgian_keyboard) |
| **Keyman Georgian QWERTY** | Cross-platform input method (Win/Mac/Linux/iOS/Android). | [keyman.com](https://keyman.com/keyboards/basic_kbdgeoqw) |
| **GeorgianCapital (Anbani)** | Full keyboard including Mtavruli capitals for Windows. | [GitHub](https://github.com/Anbani/GeorgianCapital) |
| **Branah Online Georgian Keyboard** | Virtual keyboard with transliteration. | [branah.com](https://www.branah.com/georgian) |
| **Setup Guide (Wikibooks)** | Georgian input on Windows, Mac, Linux. | [Wikibooks](https://en.wikibooks.org/wiki/Georgian/Georgian_on_your_computer) |

### Font Resources

| Name | Description | Link |
|------|-------------|------|
| **Noto Sans Georgian** | Google's comprehensive sans-serif font for Georgian. Variable weights. | [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans+Georgian) |
| **Noto Serif Georgian** | Google's serif font for Georgian. | [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Serif+Georgian) |
| **Noto Georgian (Variable Font)** | Multiple widths and weights. | [notofonts.github.io](https://notofonts.github.io/georgian/) |
| **FONTS.GE** | "All Georgian fonts in one place" — comprehensive font repository. | [fonts.ge](https://fonts.ge/en/) |
| **BPG InfoTech Fonts** | Widely-used Unicode Georgian fonts (serif, sans-serif, monospace). | Referenced in multiple projects |
| **georgian-webfonts (npm)** | CSS package for Georgian web fonts. | [GitHub (thecotne)](https://github.com/thecotne/georgian-webfonts) |

### Wikipedia & Web Data Availability

| Source | Size | Notes | Link |
|--------|------|-------|------|
| **Georgian Wikipedia (ka.wikipedia)** | ~188K articles | Founded Nov 2003; ~150K registered users | [ka.wikipedia.org](https://ka.wikipedia.org) · [Stats](https://stats.wikimedia.org/EN/TablesWikipediaKA.htm) |
| **CC-100 Georgian** | **1.1 GB** | From 2018 Common Crawl; used for XLM-R | [data.statmt.org](http://data.statmt.org/cc-100/) |
| **OSCAR Georgian** | Multiple versions | Available in OSCAR 19, 21.09, 22.01, 23.01 | [oscar-project.org](https://oscar-project.org/) |
| **mC4 Georgian** | Part of mC4 | Quality may vary; audit recommended | [HuggingFace](https://huggingface.co/datasets/allenai/c4) |
| **CulturaX Georgian** | Part of 6.3T tokens | Cleaned mC4 + OSCAR | [HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX) |

### Other Resources

| Name | Description | Link |
|------|-------------|------|
| **Anbani.db** | Georgian datasets: "Vepkhistkaosani" full text, aphorisms, poet/writer names, baby names, alphabet data. ⚠️ Last updated 2019. | [GitHub](https://github.com/Anbani/anbani.db) |
| **Gadatsqvetilebebi** | Web spider and corpora importer for public legal decisions in Georgian. | Referenced in low-resource-languages |
| **loremtyaosani** | Georgian Lorem Ipsum — random lines from Vepkhistkaosani. | [GitHub (safareli)](https://github.com/safareli/loremtyaosani) |
| **Epigraphic Corpus of Georgia** | EpiDoc-standard digital epigraphy (Georgian, Urartian, Aramaic, Greek inscriptions). Ilia State University. | [epigraphy.iliauni.edu.ge](http://v.epigraphy.iliauni.edu.ge/en-US) |
| **Online Dictionary of Georgian Idioms** | Digital idioms dictionary from Ilia State University. | [idioms.iliauni.edu.ge](http://idioms.iliauni.edu.ge/) |
| **Megrelian Language Corpus** | Corpus for the endangered Megrelian (Kartvelian family) with morpheme-level annotation. | [xmf.iliauni.edu.ge](https://xmf.iliauni.edu.ge/) |
| **TITUS** | Frankfurt-based digital archive of South Caucasian language materials (Georgian, Megrelian, Svan, Laz). | Goethe University Frankfurt |
| **awesome-georgia** | Curated list of Georgian libraries and packages (payments, i18n, fonts, NLP). 91 stars. | [GitHub](https://github.com/Stichoza/awesome-georgia) |
| **low-resource-languages** | Meta-list including Georgian tools section. | [GitHub](https://github.com/RichardLitt/low-resource-languages) |
| **awesome-georgian-datasets** | Collection of datasets specific to Georgia. | [GitHub](https://github.com/bumbeishvili/awesome-georgian-datasets) |

### Key Research Groups & Institutions

| Institution | Focus | Key People | Links |
|-------------|-------|------------|-------|
| **Tbilisi AI Lab** | Georgian-first LLMs (Kona2 family), datasets, benchmarks | — | [HuggingFace](https://huggingface.co/tbilisi-ai-lab) · [ailab.ge](http://ailab.ge) |
| **Ilia State University** | GLC corpus, UD treebank, idiom dictionaries, epigraphy | Irina Lobzhanidze, Nino Doborjginidze | [corpora.iliauni.edu.ge](http://corpora.iliauni.edu.ge/) |
| **TSU (Tbilisi State University)** | LLM benchmarks (GeoLogicQA), toxicity detection, handwriting recognition | Magda Tsintsadze, Irakli Koberidze | — |
| **TSU Arnold Chikobava Institute of Linguistics** | Computational linguistics conferences | — | — |
| **Goethe University Frankfurt** | GNC project, TITUS archive, Caucasus languages | Jost Gippert | — |
| **University of Bergen / CLARINO** | GNC infrastructure, morphosyntactic analysis | Paul Meurer | [clarino.uib.no](https://clarino.uib.no/gnc) |
| **OK'OMPLEX** (Tbilisi) | FST morphology, GRUG treebank, computational grammar | Oleg Kapanadze | — |
| **Bar-Ilan University** | Morphological reinflection for Georgian | David Guriel, Reut Tsarfaty | — |
| **DFKI / Saarland University** | Tokenization methods for Georgian | Beso Mikaberidze, Josef van Genabith | — |
| **JRC (European Commission)** | Georgian sentiment analysis, NER | Jakub Piskorski, Sopho Kharazi | — |
| **UCLouvain** | GREgORI Project for Old Georgian | Chahan Vidal-Gorène | — |
| **Anbani** | Open-source Georgian language tools | — | [GitHub Org](https://github.com/Anbani) · [anbani.ge](https://anbani.ge/en) |

### Notable Gaps in Georgian NLP (as of early 2026)

- **No dedicated Georgian BERT model** — the closest are electra-ka and georgian-distilbert-mlm; otherwise multilingual models (mBERT, XLM-R) must be used
- **No dedicated Georgian spaCy pipeline** — must use via spacy-stanza bridge
- **No Georgian WordNet** exists
- **No Google Cloud TTS** for Georgian (only STT is available)
- **Limited NER resources** — WikiANN is the primary dataset; stefan-it provides fine-tuned models
- **Morphological analyzers** remain largely academic/closed-source tools (FST-based, require XEROX tools)
- **Small UD treebanks** — both GLC (~60K tokens) and GNC (~22K tokens) are relatively small by UD standards
- **Key NLP challenges**: agglutinative morphology, split-ergative case system, polypersonal verb agreement, free word order, unique Mkhedruli script

---

*This list aims to be comprehensive as of February 2026. Items marked with ⚠️ may be outdated or unmaintained. Contributions and corrections welcome.*
