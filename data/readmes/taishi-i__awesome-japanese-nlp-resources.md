# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of resources dedicated to Python libraries, llms, dictionaries, and corpora of NLP for Japanese

- Listed information on [895 GitHub repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md)
- Listed information on [450 Hugging Face repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md) (models and datasets)
- Listed information on [156 multilingual libraries, models, and datasets that also support Japanese](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.md)

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)

## 🎉 The latest additions

**Corpus**
 * [jmeeteval](https://github.com/nishika-inc/jmeeteval) - J-MeetEval: 日本語会議タスクにおける指示追従性評価ベンチマーク

_Updated on Oct 13, 2026_


## Claude Code & Codex Plugin

Search, discover, and track Japanese NLP resources directly from [Claude Code](https://claude.ai/code) or [Codex](https://developers.openai.com/codex) using the `awesome-japanese-nlp-resources` plugin. Both tools use the same skills and the same bundled data.

**Claude Code:**

```shell
# Add the marketplace and install
/plugin marketplace add taishi-i/awesome-japanese-nlp-resources
/plugin install awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
/reload-plugins
```

**Codex** (run in your terminal, then start a new Codex session):

```shell
codex plugin marketplace add taishi-i/awesome-japanese-nlp-resources
codex plugin add awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

The plugin ships four skills:

| Skill | Purpose |
|---|---|
| `/awesome-japanese-nlp-resources:search <query>` | Search the bundled 1,200+ resource dataset |
| `/awesome-japanese-nlp-resources:discover <tool-or-topic>` | Given a tool, find alternatives (listed and unlisted); given a topic, find contribution candidates not yet in the list |
| `/awesome-japanese-nlp-resources:compare <tool-or-topic>` | Compare several libraries/models/datasets across a few criteria as a ○/△/✕ table |
| `/awesome-japanese-nlp-resources:research <topic>` | Survey the dataset + latest web research for a combined trend + challenges report |

In Codex, call the same skills with `$` instead of `/` (e.g. `$awesome-japanese-nlp-resources:search <query>`).

All skills detect the query language and respond in kind — English by default, Japanese when the query contains Japanese characters.

**`search` example:**

```shell
/awesome-japanese-nlp-resources:search What tutorials are recommended for beginners learning Japanese NLP?
```

Output includes a **Use-case Selection Guide** table:

| Use case | Recommended | Popularity | Why |
|---|---|---|---|
| Learn modern NLP/LLM concepts from scratch | [llm-book](https://github.com/ghmagazine/llm-book) | ⭐387 | Most popular intro; covers LLMs end-to-end with practical Japanese code examples |
| Build practical skills through exercises | [nlp100v2025](https://github.com/upura/nlp100v2025) | ⭐82 | Classic "100 Knock" challenge series; best way to learn by doing |
| Learn BERT and transformer-based NLP | [bert-book](https://github.com/stockmarkteam/bert-book) | ⭐262 | Hands-on BERT programming with clear explanations for Japanese NLP beginners |


For full documentation, see the [plugin README](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/plugins/awesome-japanese-nlp-resources/README.md).


## Contents
 * [Hugging Face](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md)
   * [Models](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#models)
   * [Datasets](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#datasets)
 * [Python library](#python-library)
   * [Morphology analysis](#morphology-analysis)
   * [Parsing](#parsing)
   * [Converter](#converter)
   * [Preprocessor](#preprocessor)
   * [Sentence splitter](#sentence-splitter)
   * [Sentiment analysis](#sentiment-analysis)
   * [Machine translation](#machine-translation)
   * [Named entity recognition](#named-entity-recognition)
   * [OCR](#ocr)
   * [Tool for pretrained models](#tool-for-pretrained-models)
   * [Others](#others)
 * [C++](#c)
   * [Morphology analysis](#morphology-analysis-1)
   * [Parsing](#parsing-1)
   * [Others](#others-1)
 * [Rust crate](#rust-crate)
   * [Morphology analysis](#morphology-analysis-2)
   * [Converter](#converter-1)
   * [Search engine library](#search-engine-library)
   * [Others](#others-2)
 * [JavaScript](#javascript)
   * [Morphology analysis](#morphology-analysis-3)
   * [Converter](#converter-2)
   * [Others](#others-3)
 * [Go](#go)
   * [Morphology analysis](#morphology-analysis-4)
   * [Others](#others-4)
 * [Java](#java)
   * [Morphology analysis](#morphology-analysis-5)
   * [Others](#others-5)
 * [Pretrained model](#pretrained-model)
   * [Word2Vec](#word2vec)
   * [Transformer based models](#transformer-based-models)
 * [ChatGPT](#chatgpt)
 * [Dictionary and IME](#dictionary-and-ime)
 * [Corpus](#corpus)
   * [Part-of-speech tagging / Named entity recognition](#part-of-speech-tagging--named-entity-recognition)
   * [Parallel corpus](#parallel-corpus)
   * [Dialog corpus](#dialog-corpus)
   * [Others](#others-6)
 * [Tutorial](#tutorial)
 * [Research summary](#research-summary)
 * [Reference](#reference)
 * [Contributors](#contributors)


## Python library

### Morphology analysis
Libraries that split Japanese text into words or morphemes and assign part-of-speech and base forms

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6* and above are developed as Sudachi.rs.
 * [Janome](https://github.com/mocobeta/janome) - Japanese morphological analysis engine written in pure Python
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python. you can find original version here:http://taku910.github.io/mecab/
 * [mecab](https://github.com/ikegami-yukino/mecab) - This repository is for building Windows 64-bit MeCab binary and improving MeCab Python binding.
 * [fugashi](https://github.com/polm/fugashi) - A Cython MeCab wrapper for fast, pythonic Japanese tokenization and morphological analysis.
 * [nagisa](https://github.com/taishi-i/nagisa) - A Japanese tokenizer based on recurrent neural networks
 * [pyknp](https://github.com/ku-nlp/pyknp) - A Python Module for JUMAN++/KNP
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - Python wrapper for KyTea
 * [konoha](https://github.com/himkt/konoha) - Konoha: Simple wrapper of Japanese Tokenizers
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-py combines the Python programming language with MeCab, the part-of-speech and morphological analyzer for the Japanese language.
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - Rakuten MA (Python version)
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) -  Vaporetto is a fast and lightweight pointwise prediction based tokenizer. This is a Python wrapper for Vaporetto.
 * [dango](https://github.com/mkartawijaya/dango) - An easy to use tokenizer for Japanese text, aimed at language learners and non-linguists
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - Yet another Python binding for Juman++/KNP
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) -  Viterbi-based accelerated tokenizer (Python wrapper)
 * [jagger-python](https://github.com/lighttransport/jagger-python) - Python binding for Jagger(C++ implementation of Pattern-based Japanese Morphological Analyzer)
 * [Mecari](https://github.com/zbller/Mecari) - Mecari (Japanese Morphological Analysis with Graph Neural Networks)


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 313k | 📦 75M | ⭐ 443 | 🔴 october 2022|
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 43k | 📦 14M | ⭐ 918 | 🟡 june|
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 133k | 📦 42M | ⭐ 579 | 🟡 november 2025|
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 68k | 📦 3M | ⭐ 274 | 🔴 october 2024|
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 143k | 📦 19M | ⭐ 535 | 🟡 october 2025|
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 46k | 📦 10M | ⭐ 422 | 🟢 september|
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 531 | 📦 3M | ⭐ 93 | 🟡 january|
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 606 | 📦 591k | ⭐ 36 | 🟡 march|
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 33k | 📦 7M | ⭐ 265 | 🟢 last wednesday|
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 2k | 📦 34M | ⭐ 95 | 🔴 november 2023|
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 11 | 📦 27k | ⭐ 23 | 🔴 may 2017|
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 402 | 📦 192k | ⭐ 21 | 🟡 may|
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 25 | 📦 27k | ⭐ 26 | 🔴 november 2021|
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 10k | 📦 2M | ⭐ 40 | 🟢 last tuesday|
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 128 | 📦 128k | ⭐ invalid | 🟡 may|
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 1k | 📦 339k | ⭐ 13 | 🔴 march 2024|
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 41 | 🔴 september 2025|


### Parsing
Libraries that analyze syntactic and dependency structures of Japanese sentences

 * [ginza](https://github.com/megagonlabs/ginza) - A Japanese NLP Library using spaCy as framework based on Universal Dependencies
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - NLP libary for creating pipeline components
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese with BERT models
 * [depccg](https://github.com/masashi-y/depccg) - A* CCG Parser with a Supertag and Dependency Factored Model
 * [bertknp](https://github.com/ku-nlp/bertknp) - A Japanese dependency parser based on BERT
 * [esupar](https://github.com/KoichiYasuoka/esupar) - Tokenizer POS-Tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models for Japanese and other languages
 * [yomikata](https://github.com/passaglia/yomikata) - Heteronym disambiguation library using a fine-tuned BERT model.
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - Python binding for J.DepP(C++ implementation of Japanese Dependency Parsers)
 * [lightblue](https://github.com/daisukebekki/lightblue) - A CCG parser for Japanese with DTS-representations
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simpleは日本語の係り受け関係検索システム
 * [jdeppy](https://github.com/matsurih/jdeppy) - Python wrapper for J.DepP, fast Japanese Dependency Parser


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 9k | 📦 2M | ⭐ 873 | 🟢 september|
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 55 | 📦 56k | ⭐ 7 | 🔴 august 2022|
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 273 | 📦 341k | ⭐ 38 | 🟡 december 2025|
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 337 | 📦 281k | ⭐ 336 | 🔴 august 2021|
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) | 📥 222 | 📦 125k | ⭐ 21 | 🟢 august|
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 233 | 📦 52k | ⭐ 103 | 🟢 august|
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 373 | 📦 187k | ⭐ 55 | 🟢 september|
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 25 | 📦 51k | ⭐ 36 | 🔴 october 2023|
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 544 | 📦 321k | ⭐ 4 | 🔴 february 2024|
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 29 | 🟢 last thursday|
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 | 🟢 last tuesday|
| 🔗 [jdeppy](https://github.com/matsurih/jdeppy) | 📥 14 | 📦 12k | ⭐ 3 | 🔴 february 2022|


### Converter
Libraries that convert between character types such as kana, romaji, and full-width/half-width forms

 * [pykakasi](https://github.com/miurahr/pykakasi) - Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman.
 * [cutlet](https://github.com/polm/cutlet) - Japanese to romaji converter in Python
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - Convert English alphabet to Katakana
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - Converts Arabic numerals, or 'western' style numbers, to a Japanese context.
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Mozc for Python: Kana-Kanji converter
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - Japanese text parser to separate Hiragana/Katakana string into morae (syllables).
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 日本語文を音素列へ変換するスクリプト
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - A fast character conversion and transliteration library based on the scheme defined for Japan National Tax Agency (国税庁) 's
 * [wiredify](https://github.com/eggplants/wiredify) - Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - Simple Python package (CLI/Python API) for getting japanese readings (yomigana) and accents using MeCab.
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 数量表現や時間表現の抽出・正規化を行うNormalizeNumexpのPython実装
 * [Jusho](https://github.com/nagataaaas/Jusho) - Easy wrapper for the postal code data of Japan
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - Japanese text normalizer that resolves spelling inconsistencies. （日本語表記揺れ解消ツール）
 * [e2k](https://github.com/Patchethium/e2k) - A tool for automatic English to Katakana conversion
 * [alkana.py](https://github.com/zomysan/alkana.py) - A tool to get the katakana reading of an alphabetical string.
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 英語文字列をカタカナに変換するプログラム
 * [kanjiconv](https://github.com/sea-turt1e/kanjiconv) - Kanji Converter to Hiragana, Katakana, Roman alphabet.
 * [kanjize](https://github.com/nagataaaas/kanjize) - Kanjize(カンジャイズ): Easy converter between Kanji-Number and Integer


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 557k | 📦 41M | ⭐ 464 | 🟢 july|
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 23k | 📦 2M | ⭐ 387 | 🟢 september|
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 194 | 📦 65k | ⭐ 15 | 🟡 february|
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 51 | 🔴 november 2020|
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 258 | 📦 21k | ⭐ 49 | 🔴 february 2025|
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 249 | 📦 12k | ⭐ 11 | 🟡 february|
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 | 🔴 may 2023|
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 753 | 📦 149k | ⭐ 21 | 🟡 march|
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 31 | 📦 7k | ⭐ 3 | 🟡 december 2025|
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 23 | 📦 5k | ⭐ 7 | 🟢 september|
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 24 | 📦 15k | ⭐ 8 | 🔴 april 2024|
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 730 | 📦 70k | ⭐ 12 | 🔴 june 2024|
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 66 | 📦 22k | ⭐ 6 | 🔴 march 2025|
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 727 | 📦 42k | ⭐ 20 | 🟡 march|
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 35 | 🔴 october 2021|
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 | 🟢 august|
| 🔗 [kanjiconv](https://github.com/sea-turt1e/kanjiconv) | 📥 914 | 📦 30k | ⭐ 20 | 🟢 august|
| 🔗 [kanjize](https://github.com/nagataaaas/kanjize) | 📥 15k | 📦 2M | ⭐ 68 | 🔴 june 2025|


### Preprocessor
Libraries that normalize and clean text before analysis

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, and Zenkaku
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A fast converter between Japanese hankaku and zenkaku characters
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - A powerful text cleaner for Japanese web texts
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 複数の前処理を構成して管理するテキスト前処理ツール
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese.
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - Yet Another Fast Japanese String Converter
 * [kairyou](https://github.com/bikatr7/kairyou) - Quickly preprocesses Japanese text using NLP/NER from SpaCy for Japanese translation or other NLP tasks.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 9k | 📦 2M | ⭐ 290 | 🟡 may|
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 812k | 📦 85M | ⭐ 351 | 🟡 february|
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 49k | 📦 13M | ⭐ 154 | 🔴 january 2024|
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 | 🔴 november 2022|
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 1k | 📦 1M | ⭐ 127 | 🟢 september|
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 151 | 📦 26k | ⭐ 5 | 🟡 march|
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 5k | 📦 3M | ⭐ 6 | 🟡 october 2025|
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 163 | 📦 35k | ⭐ 6 | 🔴 june 2025|


### Sentence splitter
Libraries that automatically detect sentence boundaries and split text

 * [Bunkai](https://github.com/megagonlabs/bunkai) - Sentence boundary disambiguation tool for Japanese texts (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - Japanese Sentence Breaker
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - Yet another sentence-level tokenizer for the Japanese text
 * [budoux](https://github.com/google/budoux) - Standalone. Small. Language-neutral. BudouX is the successor to Budou, the machine learning powered line break organizer tool.
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - japanese sentence segmentation library for python
 * [hasami](https://github.com/mkartawijaya/hasami) - A tool to perform sentence segmentation on Japanese text
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Japanese Text Segmenter for Python written in Rust
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - Comparison of Japanese Sentence Segmentation Tools
 * [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) - Japanese sentence splitting(日本語文境界判定器), 40–250× faster via a Rust-accelerated Python library with near-perfect API compatibility with megagonlabs/bunkai.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 261 | 📦 124k | ⭐ 200 | 🔴 august 2023|
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 7 | 📦 7k | ⭐ 14 | 🔴 february 2021|
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 214 | 📦 139k | ⭐ 24 | 🟡 november 2025|
| 🔗 [budoux](https://github.com/google/budoux) | 📥 22k | 📦 846k | ⭐ 1.8k | 🟢 last saturday|
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 3k | 📦 285k | ⭐ 76 | 🟢 july|
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 112 | 📦 47k | ⭐ 6 | 🔴 february 2021|
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 91 | 📦 31k | ⭐ 6 | 🔴 june 2025|
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 10 | 🔴 february 2023|
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 79 | 📦 10k | ⭐ 77 | 🟡 october 2025|


### Sentiment analysis
Libraries that detect emotions or polarity in text

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese negative positive classification.日本語文書のネガポジを判定。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text
 * [asari](https://github.com/Hironsan/asari) - Japanese sentiment analyzer implemented in Python.
 * [kotobacore](https://github.com/ekiyo55/kotobacore) - Japanese semantic understanding engine for LLM, RAG, SNS analysis, and AI agents ? dependency-free tokenizer + Plutchik emotion + intent + RAG keywords.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 305 | 📦 176k | ⭐ 99 | 🔴 august 2025|
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 152 | 🔴 august 2017|
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 25 | 📦 68k | ⭐ 119 | 🔴 july 2024|
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 69 | 📦 83k | ⭐ 153 | 🔴 october 2022|
| 🔗 [kotobacore](https://github.com/ekiyo55/kotobacore) | - | - | ⭐ 1 | 🟢 september|


### Machine translation
Libraries that automatically translate text between languages

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - An example usage of JParaCrawl pre-trained Neural Machine Translation (NMT) models.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: Japanese-specific Sequence to Sequence Pre-training for Neural Machine Translation (LREC2020) & Linguistically Driven Multi-Task Pre-Training for Low-Resource Neural Machine Translation (ACM TALLIP)
 * [PheMT](https://github.com/cl-tohoku/PheMT) - A phenomenon-wise evaluation dataset for Japanese-English machine translation robustness. The dataset is based on the MTNT dataset, with additional annotations of four linguistic phenomena; Proper Noun, Abbreviated Noun, Colloquial Expression, and Variant. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - An ambiguous subtitles dataset for visual scene-aware machine translation
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - A command-line interface for translation using the plamo-2-translate model with local execution.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 104 | 🔴 april 2021|
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 20 | 🔴 february 2021|
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 | 🔴 october 2022|
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 352 | 🟢 last saturday|


### Named entity recognition
Libraries that extract names of people, places, and organizations from text

 * [namaco](https://github.com/chakki-works/namaco) - Character Based Named Entity Recognition.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia is an Extended Named Entity Dictionary from Wikipedia.
 * [noyaki](https://github.com/ken11/noyaki) - Converts character span label information to tokenized text-based label information.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - Code to perform finetuning of the BERT model. BERTモデルのファインチューニングで固有表現抽出用タスクのモデルを作成・使用するサンプルです
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 詳細なアノテーション基準に基づく症例報告コーパスからの固有表現及び関係の抽出精度の推論を行うコード
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp, A python module for geotagging Japanese texts.
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERTによる日本語固有表現抽出のファインチューニング用プログラム
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - Examples to finetune encoder-only and encoder-decoder transformers for Japanese language (Hugging Face) Resources
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - BERTのfine-tuningによる固有表現抽出


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 | 🔴 february 2018|
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 | 🔴 december 2018|
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 127 | 📦 25k | ⭐ 5 | 🔴 august 2022|
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 | 🔴 june 2022|
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 2 | 🔴 november 2021|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 294 | 📦 30k | ⭐ 22 | 🟡 march|
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 5 | 🔴 september 2022|
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 | 🔴 october 2023|
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 | 🔴 june 2024|


### OCR
Libraries that recognize and extract text from images

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - About Optical character recognition for Japanese text, with the main focus being Japanese manga
 * [mokuro](https://github.com/kha-white/mokuro) - Read Japanese manga inside browser with selectable text.
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - Handwritten Japanese OCR demo using touch panel to draw the input text using Intel OpenVINO toolkit
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 日本語OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCRのアプリケーション
 * [donut](https://github.com/clovaai/donut) - Official Implementation of OCR-free Document Understanding Transformer (Donut) and Synthetic Document Generator (SynthDoG), ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - manga translator - get japanese manga from url to translate manga image
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - OCR system for recognizing modern Japanese magazines
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR用テキスト認識モジュール
 * [Poricom](https://github.com/blueaxis/Poricom) - Optical character recognition in manga images. Manga OCR desktop application
 * [owocr](https://github.com/aurorawright/owocr) - Optical character recognition for Japanese text
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku is an AI-powered document image analysis package designed specifically for the Japanese language.
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - Japanese OCR with CenterNet
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - A simple OCR for manga (Japanese traditional and Japanese vertical)
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - 日本語の文章画像に対するOCRの性能を評価
 * [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) - Fine-tune PaddleOCR-VL on the Manga109s dataset for Japanese manga text recognition. The base model struggles with vertical Japanese text reading order in manga. After fine-tuning, the model correctly handles manga-specific text layouts.
 * [MangaOCR](https://github.com/gnurt2041/MangaOCR) - A lightweight OCR model for Japanese text, especially in Manga
 * [meikiocr](https://github.com/rtr46/meikiocr) - high-speed, high-accuracy, local ocr for japanese video games
 * [meikipop](https://github.com/rtr46/meikipop) - universal japanese ocr popup dictionary for windows, linux and macos


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 3k | 📦 402k | ⭐ 2.8k | 🟢 july|
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 607 | 📦 115k | ⭐ 1.8k | 🟢 july|
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 37 | 🔴 april 2022|
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 251 | 🔴 april 2021|
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 683 | 🔴 september 2025|
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 89 | 📦 205k | ⭐ 6.9k | 🔴 july 2023|
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 87 | 🔴 january 2021|
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 153 | 🟢 july|
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 | 🔴 july 2023|
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 442 | 🔴 june 2023|
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 304 | 🟡 march|
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 929 | 📦 134k | ⭐ 1.6k | 🟢 october|
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 66 | 🔴 august 2025|
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) | - | - | ⭐ 7 | 🔴 march 2025|
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 | 🔴 march 2024|
| 🔗 [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) | - | - | ⭐ 15 | 🟡 december 2025|
| 🔗 [MangaOCR](https://github.com/gnurt2041/MangaOCR) | - | - | ⭐ 40 | 🔴 may 2024|
| 🔗 [meikiocr](https://github.com/rtr46/meikiocr) | 📥 631 | 📦 55k | ⭐ 100 | 🟢 september|
| 🔗 [meikipop](https://github.com/rtr46/meikipop) | - | - | ⭐ 683 | 🟢 yesterday|


### Tool for pretrained models
Libraries that utilize pretrained models to improve accuracy and efficiency

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE: Japanese General Language Understanding Evaluation
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - Use custom tokenizers in spacy-transformers
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - T5による会話生成
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - To investigate various DNN text classifiers including MLP, CNN, RNN, BERT approaches.
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - Deploying sentiment analysis server with FastAPI and BERT
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - Masked Language Model-based Scoring for Japanese and Vietnamese
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - AllenNLP integration for Shiba: Japanese CANINE model
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - script to evaluate pre-trained Japanese word2vec model on Japanese similarity dataset
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - BERT-based GEC tagging for Japanese
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - Japanese-BPEEncoder
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - Japanese-BPEEncoder Version 2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日本語文法誤り訂正ツール
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - A BERT model for nagisa
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - Japanese Tokenizer for transformers library
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - How do different tokenizers perform on downstream tasks in scriptio continua languages?: A case study in Japanese-ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - A framework for few-shot evaluation of autoregressive language models.
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - The repository contains scripts and merge scripts that have been modified to adapt an Alpaca-Lora adapter for LoRA tuning when assuming the use of the "rinna/japanese-gpt-neox..." [gpt-neox] model converted to ggml.
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - このリポジトリは日本語LLMのキャラクターロールプレイに関する性能を評価するために作成しました。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - This repository supports YuzuAI's Rakuda leaderboard of Japanese LLMs, which is a Japanese-focused analogue of LMSYS' Vicuna eval.
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - このツールは、複数のデータセットを横断して日本語の大規模言語モデルを自動評価するものです．
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - This repository contains the code for supervised fine-tuning of LLM-jp models.
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - LLM勉強会（LLM-jp）で開発しているLLM用のトークナイザー関連をまとめたリポジトリです．
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - Japanese Language Model Financial Evaluation Harness
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - Japanese Vicuna QA Benchmark
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - Swallowプロジェクト 大規模言語モデル 評価スクリプト
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - Swallowプロジェクト 事後学習ずみ大規模言語モデル 評価フレームワーク
 * [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) - pretrained doc2vec models on Japanese Wikipedia
 * [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) - A repository of Japanese Phoneme-Level BERT


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 350 | 🔴 march 2025|
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 432 | 📦 280k | ⭐ 16 | 🟢 september|
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 | 🔴 april 2021|
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 | 🔴 february 2022|
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 54 | 📦 23k | ⭐ 12 | 🔴 june 2021|
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 | 🔴 november 2024|
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 20 | 🔴 june 2021|
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 42 | 🔴 september 2021|
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 | 🔴 january 2023|
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 | 🔴 september 2020|
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 26 | 📦 63k | ⭐ 5 | 🟡 february|
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 18 | 🟢 last tuesday|
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 77 | 📦 31k | ⭐ 5 | 🔴 february 2024|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 155 | 🔴 november 2023|
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 | 🔴 june 2023|
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 | 🔴 june 2023|
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 97 | 🔴 july 2023|
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 19 | 🔴 may 2023|
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 42 | 🔴 november 2023|
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 | 🔴 march 2024|
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 173 | 🟢 august|
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 65 | 🔴 june 2024|
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 53 | 🟢 september|
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 80 | 🟡 june|
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 | 🔴 june 2024|
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 26 | 🔴 september 2025|
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 34 | 🟡 may|
| 🔗 [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) | - | - | ⭐ 25 | 🔴 january 2019|
| 🔗 [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) | - | - | ⭐ 24 | 🔴 december 2023|


### Others
General-purpose tools supporting Japanese language processing


<details markdown="1">
<summary>Show 212 items</summary>

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - A tool for dividing the Japanese full name into a family name and a given name.
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - A curated list of resources dedicated to Python libraries of NLP for Japanese
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - python版日本語意味役割付与システム（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - A comparison tool of Japanese tokenizers
 * [ja-timex](https://github.com/yagays/ja-timex) - 自然言語で書かれた時間情報表現を抽出/規格化するルールベースの解析器
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - A set of metrics for feature selection from text data
 * [daaja](https://github.com/kajyuuen/daaja) - This repository has implementations of data augmentation for NLP for Japanese.
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - The purpose of this repository is to make prototypes as case study in the context of proof of concept(PoC) and research and development(R&D) that I have written in my website. The main research topics are Auto-Encoders in relation to the representation learning, the statistical machine learning for energy-based models, adversarial generation net…
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - A processor for KyotoCorpus, KWDLC, and AnnotatedFKCCorpus
 * [nlplot](https://github.com/takapy0210/nlplot) - Visualization Module for Natural Language Processing
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - Rapid Automatic Keyword Extraction algorithm for Japanese
 * [jel](https://github.com/izuna385/jel) - Japanese Entity Linker.
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - Latest version of MedEX/J (Japanese disease name extractor)
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - Zunda: Japanese Enhanced Modality Analyzer client for Python.
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - A PyTorch implementation of the Japanese Predicate-Argument Structure (PAS) analyser presented in the paper of Matsubayashi & Inui (2018) with some improvements.
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - Darts-clone python binding
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - Example codes for Japanese Realistic Textual Entailment Corpus
 * [desuwa](https://github.com/megagonlabs/desuwa) - Feature annotator to morphemes and phrases based on KNP rule files (pure-Python)
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - Restaurant Search System through Dialogue in Japanese.
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - Samples codes for natural language processing in Japanese
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Small example scripts for working with Japanese texts in Python
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - Japanese version of DNorm
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph is a development platform for high-level NLP applications in Japanese.
 * [ishi](https://github.com/ku-nlp/ishi) - Ishi: A volition classifier for Japanese
 * [python-npylm](https://github.com/musyoku/python-npylm) - ベイズ階層言語モデルによる教師なし形態素解析
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 条件付確率場とベイズ階層言語モデルの統合による半教師あり形態素解析
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 教師なし品詞タグ推定
 * [negima](https://github.com/cocodrips/negima) - Negima is a Python package to extract phrases in Japanese text by using the part-of-speeches based rules you defined.
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - Extractive summarizer using BertSum as summarization model
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - A parser for Japanese number (Kanji, arabic) in the natural language.
 * [kantan](https://github.com/itayperl/kantan) - Lookup japanese words by radical patterns
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - Get Japanese dialogue corpus
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - A summarizer for Japanese articles.
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpText is a collection of text processing tools for Python.
 * [yubin](https://github.com/alvations/yubin) - Japanese Address Munger
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - Japanese Wikipedia Cleaner
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - A python library to convert Japanese to phoneme.
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - This repository contains codes related to the experiments in "An Experimental Evaluation of Japanese Tokenizers for Sentiment-Based Text Classification"
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - Generates plain or tokenized text files from the Aozora Bunko
 * [JLM](https://github.com/jiali-ms/JLM) - A fast LSTM Language Model for large vocabulary language like Japanese and Chinese
 * [NTM](https://github.com/m3yrin/NTM) - Testing of Neural Topic Modeling for Japanese articles
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - This is a English-Japanese lexicon for Machine Learning and Deep Learning terminology.
 * [text-generation](https://github.com/discus0434/text-generation) - Easy-to-use scripts to fine-tune GPT-2-JA with your own texts, to generate sentences, and to tweet them automatically.
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - Neural Image Caption (NIC) on chainer, its pretrained models on English and Japanese image caption datasets.
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - The official repository for "UnihanLM: Coarse-to-Fine Chinese-Japanese Language Model Pretraining with the Unihan Database", AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - Code to perform finetuning of the mBART model.
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - xvector model on jtubespeech
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - TinySegmenter用の学習モデルを自作するためのツール．
 * [Grongish](https://github.com/shogo82148/Grongish) - 日本語とグロンギ語の相互変換スクリプト
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - WordCloudでの日本語文章をMecab（形態素解析エンジン）を使用せずに形態素解析チックな表示を実現するスクリプト
 * [snark](https://github.com/hiraokusky/snark) - 日本語ワードネットを利用したDBアクセスライブラリ
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 日本語文を絵文字だけの文に変換するなにか
 * [termextract](https://github.com/kanjirz50/termextract) - - 専門用語抽出アルゴリズムの実装の練習
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - Japanese-Dialog-Transformerの応答候補に対して、KenLMによるN-gram言語モデルでスコアリングし、フィルタリング若しくはリランキングを行う。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Mixture of Unigram Model and Infinite Mixture of Unigram Model in Python. (混合ユニグラムモデルと無限混合ユニグラムモデル)
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Hidden Markov Model (HMM) and Infinite Hidden Markov Model (iHMM) in Python. (隠れマルコフモデルと無限隠れマルコフモデル)
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - Ngram language model in Python. (Nグラム言語モデル)
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - Automatic Speech Recognition with deepspeech2 model in pytorch with support from Zakuro AI.
 * [neural_ime](https://github.com/yohokuno/neural_ime) - Neural IME: Neural Input Method Engine
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - Can neural networks transliterate Romaji into Japanese correctly?
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - tokenizer specified for Japanese
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - Data Augmentation for Japanese Text on AugLy
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - A Python script for adding furigana to Japanese epub books using Mecab and Unidic.
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - Japanese verb/adjective inflections tool
 * [jageocoder](https://github.com/t-sagara/jageocoder) - Pure Python Japanese address geocoder
 * [nksnd](https://github.com/yoriyuki/nksnd) - New kana-kanji conversion engine
 * [JaMIE](https://github.com/racerandom/JaMIE) - A Japanese Medical Information Extraction Toolkit
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - fasttextとword2vecの比較と、実行スクリプト、学習スクリプトです
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小のサーチエンジン/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 5chの過去ログをスクレイピングして、過去流行った単語(ex, 香具師, orz)などを追跡調査
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Twitter日本語評判分析データセットのためのツイートダウンローダ
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - Aggregating Japanese words based on Juman++ and ConceptNet5.5
 * [jinf](https://github.com/hkiyomaru/jinf) - A Japanese inflection converter
 * [kwja](https://github.com/ku-nlp/kwja) - A unified language analyzer for Japanese
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - Reproduced package based on Masked Language Model Scoring (ACL2020).
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] ClipCap for Japanese
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] Show, Attend and Tell for Japanese
 * [cihai](https://github.com/cihai/cihai) - Python library for CJK (Chinese, Japanese, and Korean) language dictionary
 * [marine](https://github.com/6gsn/marine) - MARINE : Multi-task leaRnIng-based JapaNese accent Estimation
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - Finetuning Whisper ASR model
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字正規化ライブラリ
 * [akaza](https://github.com/tokuhirom/akaza) - Yet another Japanese IME for IBus/Linux
 * [posuto](https://github.com/polm/posuto) -  Japanese postal code data.
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - Tacotron2 implementation of Japanese
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - ひらがなIME for IBus
 * [furiganapad](https://github.com/esrille/furiganapad) - ふりがなパッド
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - Japanese synonym library
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - JapaneseEmbeddingEval
 * [shuwa](https://github.com/google/shuwa) - Extend GNOME On-Screen Keyboard for Input Methods
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - This repository provides the code for Japanese NLI model, a fine-tuned masked language model.
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - A tool for Japanese-English translation and English-Japanese translation by using FuguMT
 * [fugumt](https://github.com/s-taka/fugumt) - ぷるーふおぶこんせぷと で公開した機械翻訳エンジンを利用する翻訳環境です。 フォームに入力された文字列の翻訳、PDFの翻訳が可能です。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE: Automatic Evaluation Metric Using Predicate-Argument Structures for Image Captioning Models
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - jp-localization
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - Python wrapper for OpenJTalk
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - Make learning Japanese easier by adding readings for every kanji in the eBook
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - Whisper based Japanese subtitle generator
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - Rinna-3.6B、OpenCALM等の日本語対応LLM(大規模言語モデル)用の簡易Webインタフェースです
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translator translates English PDF files into Japanese, preserving the original layout.
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - Haystack + Elasticsearch + wikipedia(ja) を用いた、日本語の質問応答システムのサンプル
 * [mozc-devices](https://github.com/google/mozc-devices) - Automatically exported from code.google.com/p/mozc-morse
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）の学習と音声合成のGradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - A Japanese law parser
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - Japanese dictation kit using Julius
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - Juliusを使ったセグメンテーション支援ツール
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXの音声合成エンジン
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP is a Japanese VLM trained by LLaVA method
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [bertjsc](https://github.com/er-ri/bertjsc) - Japanese Spelling Error Corrector using BERT(Masked-Language Model). BERTに基づいて日本語校正
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - Project of llm evaluation to Japanese tasks
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - Modifying LAVIS' BLIP2 Q-former with models pretrained on Japanese datasets.
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本語の文を、各種日本語の embeddings や faiss index へと変換するスクリプト等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - Exploring Japanese SimCSE
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - GPT-4 を用いて、言語モデルの応答を自動評価するスクリプト
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日本語T5モデル
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - A repo for evaluating Japanese LLMs　・　日本語LLMを評価するレポ
 * [jmteb](https://github.com/sbintuitions/jmteb) - The evaluation scripts of JMTEB (Japanese Massive Text Embedding Benchmark)
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - 日本語音声に対して音素ラベルをアラインメントするためのツールです
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - 軽量で規制も検閲もない日本語ローカル LLM『LightChatAssistant-TypeB』による、簡単なノベル生成アシスタントです。ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - 日本語データセットでのqlora instruction tuning学習サンプルコード
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Japanese rōmaji input schema for Rime IME
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - 深層学習を用いたクイズ自動生成（日本語T5モデル）
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - Magpieという手法とNemotron-4-340B-Instructを用いて合成対話データセットを作るコード
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - 日本語データセットでのqlora instruction tuning学習サンプルコード
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki Dictionary is a dictionary generated from the Japanese Wikipedia for Mozc.
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - Japanese / English Bilingual LLM
 * [llm-translator](https://github.com/hpprc/llm-translator) - Mixtral-based Ja-En (En-Ja) Translation model
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - Whisperのデコーダをllm-jp-1.3b-v1.0に置き換えた音声認識モデルを学習させるためのコード
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [monaka](https://github.com/komiya-lab/monaka) - A Japanese Parser (including historical Japanese)
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - A state-of-the-art open-source Japanese <--> English machine translation system based on the latest NMT research.
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - 連続部分文字列の単語判定を行います
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - This project is a benchmarking tool for evaluating and comparing the performance of various Vision Language Models (VLMs). It uses two datasets: LLaVA-Bench-In-the-Wild and Japanese HERON Bench to measure model performance.
 * [text2dataset](https://github.com/llm-jp/text2dataset) - Easily turn large English text datasets into Japanese text datasets using open LLMs.
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - MeCabを利用した日本語形態素解析WebAPI
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - Mecab wrapper to generate furigana readings.
 * [vits](https://github.com/zassou65535/vits) - VITSによるテキスト読み上げ器&ボイスチェンジャー
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - 音声認識、文章生成、音声合成を使って対話するチャットボットアプリ
 * [kudasai](https://github.com/bikatr7/kudasai) - Streamlining Japanese-English Translation with Advanced Preprocessing and Integrated Translation Technologies
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - MeCabの形態素解析結果を可視化するツール
 * [add-dictionary](https://github.com/massao000/add-dictionary) - OpenJTalkのユーザ辞書をGUIで追加するアプリ
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi: A Japanese Full-duplex Spoken Dialogue System
 * [jatts](https://github.com/unilight/jatts) - JATTS: Japanese TTS (for research)
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - a Frontier Japanese Speech Generation net
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - ElasticsearchやGiNZA、患者表現辞書を使った患者表現揺れ吸収する意味構造検索を試した
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評価を行うためのPythonツール
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - Colaboratory上でAsagi(合成データセットを活用した大規模日本語VLM)をお試しするサンプル
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - This tool automatically evaluates Japanese multi-modal large language models across multiple datasets.
 * [manga109api](https://github.com/manga109/manga109api) - Simple python API to read annotation data of Manga109
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - fastrtc用の日本語TTSとSTT追加キット
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - Pythonを使用したWhisperモデルによる音声文字起こしツール
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - LLMを活用した自律調査エージェント。手軽に情報収集、概要把握。
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - A tool to easily benchmark Japanese translation skills
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa は 5～15秒の日本語音声と日本語テキストから日本語音声を生成する TSTS (TextSpeechToSpeech) です。
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - 氏名漢字カナ突合モデル
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - OpenReview論文を自動で発見・分析する日本語対応AIエージェント
 * [pitchbench](https://github.com/shewiiii/pitchbench) - Experimental Japanese pitch accent based LLM Benchmark
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - English to Japanese Transformer from scratch
 * [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) - VOICEVOXのコア内で用いられているディープラーニングモデルの推論コード
 * [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) - pyopenjtalk-plus: A Python wrapper for OpenJTalk with additional improvements
 * [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) - Japanese Spelling Correction
 * [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) - python kaomoji
 * [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) - This repository contains the code for training llm-jp/llm-jp-3-vila-14b, modified from VILA repository.
 * [kanjivg-radical](https://github.com/yagays/kanjivg-radical) - kanjivg-radical
 * [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) - This project visualizes the Japanese Wordnet (日本語ワードネット) with web application built by Django
 * [piper-plus](https://github.com/ayutaz/piper-plus) - Enhanced Piper TTS with Japanese support, WebAssembly, multi-GPU training, and quality improvements.
 * [Japanera](https://github.com/nagataaaas/Japanera) - Easy Tools for Japanese Era System
 * [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) - Japanese Sentence Summarization with BERT
 * [kyujipy](https://github.com/drturnon/kyujipy) - A Python library to convert Japanese texts from Shinjitai (新字体) to Kyujitai (舊字體) and vice versa
 * [jitenbot](https://github.com/konstantindjairo/jitenbot) - Web crawler for creating personal copies of Japanese dictionaries
 * [ja-icd10](https://github.com/yagays/ja-icd10) - ICD-10 国際疾病分類の日本語情報を扱うためのPythonパッケージ
 * [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) - VITS2 using Phoneme-Level Japanese BERT
 * [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) - NDCPredictorの機械学習モデル（書誌情報から日本十進分類を推測するfastTextの学習済みモデル）
 * [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) - pfmt-bench-fin-ja: Preferred Multi-turn Benchmark for Finance in Japanese
 * [marine-plus](https://github.com/tsukumijima/marine-plus) - MARINE : Multi-task leaRnIng-based JapaNese accent Estimation (Also supported Windows)
 * [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) - Compare the speed of various Japanese tokenizers in Python.
 * [yat](https://github.com/yagays/yat) - yat: Yet Another Tokenizer for Japanese NLP
 * [igakuqa119](https://github.com/docto-rin/igakuqa119) - Evaluating LLMs on the 119th Japanese Medical Licensing Examination
 * [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) - Japanese Long-Unit-Word Tokenizer with RemBertTokenizerFast of Transformers
 * [ibus-jig](https://github.com/y-koj/ibus-jig) - ibus-jig: Japanese-language Input-method using GPT-4
 * [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) - A lightweight Python library designed to filter stopwords from Japanese text based on customizable rules.
 * [yasumail](https://github.com/terallite/yasumail) - Synthetic Japanese business email generator for ML training data
 * [himotoki](https://github.com/msr2903/himotoki) - A Python-based Japanese Tokenizer, Dictionary, Morphological Analyzer and Romanization Tool. Based on JMDict for Language Learning.
 * [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) - A toolkit for synthesizing filler-rich, short-utterance Japanese dialogue scripts for speech-based interaction using Large Language Models (LLMs) This project is designed to generate data in two phases: Seed Generation (metadata creation) and Dialogue Generation (script creation).
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - Evaluating Multimodal Large Language Models on Vertically Written Japanese Text
 * [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) - 本コードは，大規模言語モデル（LLM）の学習用コーパスから，個人情報の中でも特に配慮が求められる「要配慮個人情報」をフィルタリングするためのものです.
 * [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) - 小説テキストから雑談対話コーパスを構築する手法
 * [OneCompression](https://github.com/FujitsuResearch/OneCompression) -  富士通研究所による LLM 向け後学習量子化 (PTQ) パイプライン。QEP (NeurIPS 2025)、ILP 混合精度、回転前処理、vLLM プラグインを統合。論文: [arXiv:2603.28845](https://arxiv.org/abs/2603.28845)。
 * [manga-translator](https://github.com/georgescutelnicu/manga-translator) - Translate text found within speech bubbles in manga images.
 * [shirabe-address-api](https://github.com/techwell-inc-jp/shirabe-address-api) - Shirabe Address API — Japanese address normalization for AI agents (Cloudflare Workers + Fly.io NRT, abr-geocoder backed)
 * [medical-paper-summarizer-public](https://github.com/yush02084/medical-paper-summarizer-public) - 毎日PubMedから最新の循環器内科論文を自動収集・AI要約してGmailに届けるシステム
 * [Irodori-TTS](https://github.com/Aratako/Irodori-TTS) - A Flow Matching-based Text-to-Speech Model with Emoji-driven Style Control
 * [sarashina2.2-tts](https://github.com/sbintuitions/sarashina2.2-tts) - Sarashina2.2-TTS is a Japanese-centric text-to-speech system built on a large language model, developed by SB Intuitions.
 * [manga-translator](https://github.com/Detopall/manga-translator) - A manga translator created using Yolov8, manga_ocr and deep-translator.
 * [jp-tl-bench](https://github.com/shisa-ai/jp-tl-bench) - Anchored Pairwise LLM Evaluation for Bidirectional Japanese-English Translation
 * [novel2hermes_jp](https://github.com/kgmkm/novel2hermes_jp) - メモリ機能が強力なhermes-agentと、日本語検索に強い外部メモリvecmemoriを活かし、長文に耐える小説を企画/プロッティング/執筆するためのskills.md
 * [moshi-finetune](https://github.com/nu-dialogue/moshi-finetune) - Fine-tuning Moshi/J-Moshi on your own spoken dialogue data
 * [simple-evals-mm](https://github.com/llm-jp/simple-evals-mm) - A lightweight library for evaluating vision language models on English and Japanese benchmarks.
 * [medvoice-jp-asr](https://github.com/nikotora/medvoice-jp-asr) - MedVoice-JP LoRA60: 日本語医療特化ASR (whisper-small + LoRA, 60話者) と国内初の医療ASRベンチマーク (フルFT版 FT60 も収録)
 * [open-zeimu-mcp](https://github.com/zeimu-ai/open-zeimu-mcp) - OSS MCP server for Japanese tax primary sources (法令・通達・タックスアンサー・質疑応答事例・文書回答事例・裁決事例)
 * [llm-jp-moshi](https://github.com/llm-jp/llm-jp-moshi) - LLM-jp-Moshi: Japanese Full-duplex Spoken Dialogue Models
 * [shirabe-sdk-python](https://github.com/techwell-inc-jp/shirabe-sdk-python) - Official Python SDK for the Shirabe Japan data APIs — ready-made LangChain / OpenAI Agents SDK tools for Japanese name reading (JMnedict-backed candidates), name splitting, address normalization, corporate number lookup, and calendar (rokuyo). Zero-dependency core.
 * [fuseji](https://github.com/sserada/fuseji) - 日本語特化のPII検出・マスキングミドルウェア（LLMオブザーバビリティ向け）
 * [moine](https://github.com/tagucci/moine) - Romanization-aware string comparison for Japanese and Mandarin Chinese.
 * [bpe2regex](https://github.com/t3tra-dev/bpe2regex) - BPE tokenizer をクソデカ正規表現に変換する意味わからんやつ
 * [sanoTTS-jp](https://github.com/ayutaz/sanoTTS-jp) - 559 K パラメータの日本語 TTS を ESP32-S3 で実時間合成。漢字かな交じり文の形態素解析・アクセント推定まで端末内で走る（M5Stack CoreS3 実機で確認）。推論は依存ゼロの C99、ブラウザ demo あり。arXiv:2608.21378 sanoTTS の日本語 clean-room 再実装。⚠️ コードは MIT ですが、配布モデルの重みは MIT ではありません（LICENSE-MODEL.md。出力に用途制限が伝播します）
 * [jev-auto-ime](https://github.com/kzkhykw/jev-auto-ime) - 打っている言葉が日本語か英語かをJevに聞いて、Macの入力モードを切り替える道具。個人利用のみ。
 * [yomiyasu](https://github.com/nanaism/yomiyasu) - AI生成の日本語を自然な日本語へ推敲するAgent Skill / Agent Skill for Refining AI-Generated Japanese into Natural Japanese
 * [natural-japanese-writing](https://github.com/kojikojikojikoji/natural-japanese-writing) - An agent skill for Claude Code, Codex and Cursor that rewrites AI-sounding Japanese into natural Japanese without changing the facts.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 1k | 📦 112k | ⭐ 252 | 🟢 today|
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 25 | 📦 32k | ⭐ 11 | 🔴 february 2019|
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 | 🔴 january 2020|
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 13 | 📦 28k | ⭐ 122 | 🟡 november 2025|
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 698 | 📦 144k | ⭐ 140 | 🔴 november 2023|
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 138 | 🔴 march 2019|
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 42 | 📦 27k | ⭐ 64 | 🔴 february 2023|
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 115 | 📦 157k | ⭐ 329 | 🔴 december 2023|
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 894 | 📦 70k | ⭐ 10 | 🔴 june 2024|
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 79 | 📦 117k | ⭐ 238 | 🔴 september 2022|
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 | 🔴 october 2018|
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 10 | 📦 8k | ⭐ 12 | 🔴 july 2021|
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 | 🔴 may 2022|
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 8 | 📦 6k | ⭐ 10 | 🔴 november 2019|
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 10 | 📦 8k | ⭐ 6 | 🔴 june 2018|
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 2k | 📦 9M | ⭐ 20 | 🔴 april 2022|
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 19 | 📦 11k | ⭐ 6 | 🔴 may 2022|
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 274 | 🔴 may 2016|
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 66 | 🔴 april 2021|
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 27 | 🔴 june 2019|
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 | 🔴 june 2022|
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 37 | 📦 69k | ⭐ 9 | 🔴 september 2022|
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 8 | 📦 7k | ⭐ 2 | 🔴 may 2020|
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 | 🔴 january 2019|
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 | 🔴 march 2018|
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 | 🔴 october 2017|
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 15 | 📦 17k | ⭐ 14 | 🔴 august 2018|
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 | 🔴 september 2020|
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 1k | 📦 2M | ⭐ 21 | 🔴 april 2020|
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 | 🔴 october 2024|
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 | 🔴 september 2017|
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 | 🔴 august 2022|
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 9k | 📦 410k | ⭐ 7 | 🔴 october 2022|
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 14 | 📦 3k | ⭐ 3 | 🔴 october 2019|
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 26 | 📦 26k | ⭐ 6 | 🔴 february 2021|
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 13 | 📦 5k | ⭐ 1 | 🔴 february 2022|
| 🔗 [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) | - | - | ⭐ 1 | 🔴 march 2022|
| 🔗 [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) | - | - | ⭐ 11 | 🔴 september 2017|
| 🔗 [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) | - | - | ⭐ 9 | 🔴 june 2025|
| 🔗 [JLM](https://github.com/jiali-ms/JLM) | - | - | ⭐ 112 | 🔴 june 2019|
| 🔗 [NTM](https://github.com/m3yrin/NTM) | - | - | ⭐ 13 | 🔴 july 2019|
| 🔗 [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) | - | - | ⭐ 41 | 🔴 march 2021|
| 🔗 [text-generation](https://github.com/discus0434/text-generation) | - | - | ⭐ 19 | 🔴 august 2025|
| 🔗 [chainer_nic](https://github.com/yuyay/chainer_nic) | - | - | ⭐ 17 | 🔴 december 2018|
| 🔗 [unihan-lm](https://github.com/JetRunner/unihan-lm) | - | - | ⭐ 2 | 🔴 november 2020|
| 🔗 [mbart-finetuning](https://github.com/ken11/mbart-finetuning) | - | - | ⭐ 3 | 🔴 october 2021|
| 🔗 [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) | - | - | ⭐ 47 | 🔴 november 2023|
| 🔗 [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) | - | - | ⭐ 74 | 🔴 september 2022|
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 26 | 🟢 september|
| 🔗 [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) | - | - | ⭐ 10 | 🔴 january 2020|
| 🔗 [snark](https://github.com/hiraokusky/snark) | - | - | ⭐ 11 | 🔴 march 2020|
| 🔗 [toEmoji](https://github.com/mkan0141/toEmoji) | - | - | ⭐ 4 | 🔴 april 2018|
| 🔗 [termextract](https://github.com/kanjirz50/termextract) | - | - | ⭐ 18 | 🔴 september 2018|
| 🔗 [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) | - | - | ⭐ 1 | 🔴 july 2022|
| 🔗 [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) | - | - | ⭐ 6 | 🔴 june 2017|
| 🔗 [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) | - | - | ⭐ 5 | 🔴 june 2017|
| 🔗 [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) | - | - | ⭐ 5 | 🔴 december 2017|
| 🔗 [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) | - | - | ⭐ 71 | 🟢 october|
| 🔗 [neural_ime](https://github.com/yohokuno/neural_ime) | - | - | ⭐ 67 | 🔴 december 2016|
| 🔗 [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) | - | - | ⭐ 178 | 🔴 september 2017|
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 93k | 📦 181k | ⭐ repo not found | 🔴 november 2015|
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 48 | 📦 33k | ⭐ 7 | 🟢 september|
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 22 | 📦 13k | ⭐ 34 | 🔴 september 2021|
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 38 | 📦 24k | ⭐ 13 | 🔴 march 2025|
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 4k | 📦 486k | ⭐ 107 | 🟡 march|
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 | 🔴 may 2018|
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 | 🟡 march|
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 48 | 🔴 august 2017|
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 | 🔴 july 2019|
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 75 | 🔴 november 2018|
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 | 🔴 august 2022|
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 | 🔴 august 2018|
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 308 | 📦 69k | ⭐ 4 | 🟢 august|
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 301 | 📦 66k | ⭐ 147 | 🟢 september|
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 | 🔴 december 2022|
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 13 | 🔴 october 2022|
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 | 🔴 october 2022|
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 506 | 📦 229k | ⭐ 93 | 🟢 october|
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 99 | 📦 18k | ⭐ 38 | 🔴 september 2022|
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 | 🔴 december 2022|
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 10 | 🔴 december 2022|
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 265 | 🟡 june|
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 8k | 📦 935k | ⭐ 236 | 🟢 october|
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 266 | 🔴 september 2022|
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 81 | 🟡 march|
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 20 | 🔴 april 2025|
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 221 | 📦 70k | ⭐ 55 | 🔴 february 2022|
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 | 🔴 may 2022|
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ invalid | 🔴 october 2024|
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 145 | 🔴 december 2022|
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 6 | 🔴 october 2022|
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 5 | 🔴 march 2023|
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 65 | 🔴 february 2021|
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 5 | 📦 2k | ⭐ 9 | 🟡 june|
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 47 | 🔴 april 2023|
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 20k | 📦 2M | ⭐ 261 | 🔴 april 2025|
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 15 | 📦 9k | ⭐ 27 | 🔴 february 2024|
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k | 🔴 february 2025|
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 | 🔴 may 2024|
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 346 | 🔴 may 2024|
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 | 🔴 december 2022|
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 3k | 🟢 october|
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 | 🔴 january 2024|
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 | 🔴 january 2024|
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 166 | 🔴 april 2019|
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 | 🔴 august 2021|
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.8k | 🟢 october|
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 64 | 🔴 june 2024|
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 | 🔴 may 2025|
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 14 | 🔴 august 2024|
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 95 | 🟡 may|
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 18 | 🟢 last tuesday|
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 14 | 🔴 september 2025|
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 12 | 🔴 march 2024|
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 69 | 🔴 october 2023|
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 17 | 🔴 june 2024|
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 117 | 🔴 september 2025|
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 | 🔴 april 2024|
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 94 | 🟢 last friday|
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 43 | 🔴 august 2025|
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 235 | 🔴 july 2024|
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 | 🔴 september 2025|
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 57 | 🟢 last thursday|
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 | 🔴 march 2023|
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 8 | 🔴 july 2024|
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 | 🔴 july 2024|
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 33 | 🟢 october|
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 35 | 🟡 december 2025|
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 21 | 🔴 january 2025|
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 | 🔴 may 2025|
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 8 | 🔴 january 2025|
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 | 🔴 september 2024|
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 | 🟡 november 2025|
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 | 🔴 december 2024|
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 32 | 🔴 january 2025|
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 | 🔴 july 2022|
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 21 | 🟢 october|
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 93 | 🔴 february 2023|
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 | 🟡 october 2025|
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 | 🔴 june 2025|
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 | 🔴 september 2023|
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 324 | 🟢 september|
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 | 🟡 march|
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 65 | 🔴 may 2025|
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 | 🔴 february 2021|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 64 | 🟢 september|
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 | 🔴 march 2025|
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 44 | 🟡 april|
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 116 | 📦 49k | ⭐ 132 | 🔴 march 2022|
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 6 | 🔴 may 2025|
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 21 | 🟡 january|
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 10 | 🔴 april 2025|
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 13 | 🟡 october 2025|
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 26 | 🔴 september 2025|
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 120 | 🟡 april|
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 13 | 🟡 november 2025|
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 2 | 🟡 february|
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) | - | - | ⭐ 31 | 🟡 december 2025|
| 🔗 [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) | 📥 16k | 📦 738k | ⭐ 66 | 🟢 last saturday|
| 🔗 [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) | - | - | ⭐ 16 | 🔴 september 2023|
| 🔗 [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) | 📥 8 | 📦 39k | ⭐ 6 | 🔴 december 2018|
| 🔗 [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) | - | - | ⭐ 10 | 🔴 august 2025|
| 🔗 [kanjivg-radical](https://github.com/yagays/kanjivg-radical) | - | - | ⭐ 107 | 🔴 august 2018|
| 🔗 [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) | - | - | ⭐ 3 | 🔴 november 2022|
| 🔗 [piper-plus](https://github.com/ayutaz/piper-plus) | - | - | ⭐ 235 | 🟢 last saturday|
| 🔗 [Japanera](https://github.com/nagataaaas/Japanera) | 📥 6k | 📦 479k | ⭐ 35 | 🔴 june 2025|
| 🔗 [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) | - | - | ⭐ 49 | 🔴 december 2019|
| 🔗 [kyujipy](https://github.com/drturnon/kyujipy) | 📥 70 | 📦 24k | ⭐ 22 | 🟡 january|
| 🔗 [jitenbot](https://github.com/konstantindjairo/jitenbot) | - | - | ⭐ 4 | 🔴 december 2024|
| 🔗 [ja-icd10](https://github.com/yagays/ja-icd10) | - | - | ⭐ 5 | 🔴 july 2021|
| 🔗 [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) | - | - | ⭐ 14 | 🔴 december 2023|
| 🔗 [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) | - | - | ⭐ 14 | 🔴 august 2021|
| 🔗 [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | - | - | ⭐ 9 | 🔴 march 2025|
| 🔗 [marine-plus](https://github.com/tsukumijima/marine-plus) | 📥 83 | 📦 14k | ⭐ 9 | 🟡 march|
| 🔗 [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) | - | - | ⭐ 7 | 🔴 february 2022|
| 🔗 [yat](https://github.com/yagays/yat) | - | - | ⭐ 7 | 🔴 june 2018|
| 🔗 [igakuqa119](https://github.com/docto-rin/igakuqa119) | - | - | ⭐ 10 | 🟢 september|
| 🔗 [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) | - | - | ⭐ 6 | 🔴 december 2021|
| 🔗 [ibus-jig](https://github.com/y-koj/ibus-jig) | - | - | ⭐ 4 | 🔴 december 2023|
| 🔗 [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) | 📥 0 | 📦 7k | ⭐ 4 | 🟢 august|
| 🔗 [yasumail](https://github.com/terallite/yasumail) | - | - | ⭐ 3 | 🟡 january|
| 🔗 [himotoki](https://github.com/msr2903/himotoki) | 📥 63 | 📦 7k | ⭐ 8 | 🟢 last thursday|
| 🔗 [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) | - | - | ⭐ 0 | 🟡 january|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 3 | 🟡 may|
| 🔗 [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) | - | - | ⭐ 7 | 🔴 march 2025|
| 🔗 [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) | - | - | ⭐ 0 | 🟡 february|
| 🔗 [OneCompression](https://github.com/FujitsuResearch/OneCompression) | - | - | ⭐ 434 | 🟢 october|
| 🔗 [manga-translator](https://github.com/georgescutelnicu/manga-translator) | - | - | ⭐ 27 | 🟢 august|
| 🔗 [shirabe-address-api](https://github.com/techwell-inc-jp/shirabe-address-api) | - | - | ⭐ 0 | 🟢 july|
| 🔗 [medical-paper-summarizer-public](https://github.com/yush02084/medical-paper-summarizer-public) | - | - | ⭐ 20 | 🟡 april|
| 🔗 [Irodori-TTS](https://github.com/Aratako/Irodori-TTS) | - | - | ⭐ 1.4k | 🟢 september|
| 🔗 [sarashina2.2-tts](https://github.com/sbintuitions/sarashina2.2-tts) | - | - | ⭐ 89 | 🟡 june|
| 🔗 [manga-translator](https://github.com/Detopall/manga-translator) | - | - | ⭐ 19 | 🟡 june|
| 🔗 [jp-tl-bench](https://github.com/shisa-ai/jp-tl-bench) | - | - | ⭐ 6 | 🟡 february|
| 🔗 [novel2hermes_jp](https://github.com/kgmkm/novel2hermes_jp) | - | - | ⭐ 105 | 🟢 september|
| 🔗 [moshi-finetune](https://github.com/nu-dialogue/moshi-finetune) | - | - | ⭐ 106 | 🟡 january|
| 🔗 [simple-evals-mm](https://github.com/llm-jp/simple-evals-mm) | - | - | ⭐ 5 | 🟢 august|
| 🔗 [medvoice-jp-asr](https://github.com/nikotora/medvoice-jp-asr) | - | - | ⭐ 5 | 🟡 june|
| 🔗 [open-zeimu-mcp](https://github.com/zeimu-ai/open-zeimu-mcp) | - | - | ⭐ 1 | 🟡 june|
| 🔗 [llm-jp-moshi](https://github.com/llm-jp/llm-jp-moshi) | - | - | ⭐ 25 | 🟡 march|
| 🔗 [shirabe-sdk-python](https://github.com/techwell-inc-jp/shirabe-sdk-python) | - | - | ⭐ 0 | 🟢 july|
| 🔗 [fuseji](https://github.com/sserada/fuseji) | - | - | ⭐ 1 | 🟡 june|
| 🔗 [moine](https://github.com/tagucci/moine) | - | - | ⭐ 10 | 🟢 september|
| 🔗 [bpe2regex](https://github.com/t3tra-dev/bpe2regex) | - | - | ⭐ 9 | 🟢 august|
| 🔗 [sanoTTS-jp](https://github.com/ayutaz/sanoTTS-jp) | - | - | ⭐ 68 | 🟢 october|
| 🔗 [jev-auto-ime](https://github.com/kzkhykw/jev-auto-ime) | - | - | ⭐ 11 | 🟢 september|
| 🔗 [yomiyasu](https://github.com/nanaism/yomiyasu) | - | - | ⭐ 1.9k | 🟢 yesterday|

</details>


## C++

### Morphology analysis
High-performance libraries for Japanese morphological analysis

 * [mecab](https://github.com/taku910/mecab) - Yet another Japanese morphological analyzer
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (a Morphological Analyzer Toolkit)
 * [kytea](https://github.com/neubig/kytea) - The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc.
 * [juman](https://github.com/ku-nlp/juman) - Japanese Morphological Analysis System JUMAN


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k | 🔴 february 2025|
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 413 | 🟡 april|
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 217 | 🔴 april 2020|
| 🔗 [juman](https://github.com/ku-nlp/juman) | - | - | ⭐ 12 | 🔴 december 2021|

### Parsing
Libraries for dependency and syntactic parsing of Japanese sentences

 * [cabocha](https://github.com/taku910/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [knp](https://github.com/ku-nlp/knp) - A Japanese Parser


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 120 | 🔴 february 2025|
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 35 | 🔴 november 2023|

### Others
Other Japanese NLP and text processing libraries

<details markdown="1">
<summary>Show 7 items</summary>

 * [jsc](https://github.com/yohokuno/jsc) - Joint source channel model for Japanese Kana Kanji conversion, Chinese pinyin input and CJE mixed input.
 * [aquaskk](https://github.com/codefirst/aquaskk) - An input method without morphological analysis.
 * [mozc](https://github.com/google/mozc) - Mozc - a Japanese Input Method Editor designed for multi-platform
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: An (Exact|Prefix|Approximate) String Matching Library
 * [resembla](https://github.com/tuem/resembla) - Resembla: Word-based Japanese similar sentence search library
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ SKK-like Japanese Input Method Editor for Windows
 * [mozuku](https://github.com/t3tra-dev/mozuku) - 日本語文章の解析・校正を行う LSP サーバー。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 | 🔴 december 2012|
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 373 | 🟢 september|
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 3k | 🟢 last friday|
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 | 🟡 february|
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 74 | 🔴 august 2025|
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 376 | 🟢 august|
| 🔗 [mozuku](https://github.com/t3tra-dev/mozuku) | - | - | ⭐ 419 | 🟡 april|

</details>


## Rust crate

### Morphology analysis
Fast Japanese morphological analysis crates written in Rust

 * [lindera](https://github.com/lindera-morphology/lindera) - A morphological analysis library.
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto: Very Accelerated POintwise pREdicTion based TOkenizer
 * [goya](https://github.com/Leko/goya) - Japanese Morphological Analysis written in Rust
 * [vibrato](https://github.com/daac-tools/vibrato) - vibrato: Viterbi-based accelerated tokenizer
 * [yoin](https://github.com/agatan/yoin) - A Japanese Morphological Analyzer written in pure Rust
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - Safe Rust bindings for mecab a part-of-speech and morphological analyzer library
 * [awabi](https://github.com/nakagami/awabi) - A morphological analyzer using mecab dictionary
 * [kanpyo](https://github.com/togatoga/kanpyo) - Japanese Morphological Analyzer written in Rust
 * [mecrab](https://github.com/cool-japan/mecrab) - A pure Rust implementation of a morphological analyzer compatible with MeCab dictionaries (IPADIC format).


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 2.6M | ⭐ 692 | 🟢 today|
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 332k | ⭐ 299 | 🟢 july|
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 12k | ⭐ 84 | 🔴 december 2021|
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 98k | ⭐ 425 | 🟢 october|
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 3.1k | ⭐ 26 | 🔴 october 2017|
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 41k | ⭐ 72 | 🔴 september 2023|
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 27k | ⭐ 11 | 🟡 november 2025|
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k | ⭐ 109 | 🟡 february|
| 🔗 [mecrab](https://github.com/cool-japan/mecrab) | - | - | ⭐ 8 | 🟡 january|


### Converter
Crates for script and character conversion in Japanese text

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - Utility library for checking and converting between Japanese characters - Hiragana, Katakana - and Romaji
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - A Rust library to convert Japanese Half-width-kana[半角ｶﾅ] and Wide-alphanumeric[全角英数] into normal ones
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana
 * [kanaria](https://github.com/samunohito/kanaria) - このライブラリは、ひらがな・カタカナ、半角・全角の相互変換や判別を始めとした機能を提供します。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 日本の住所を都道府県/市区町村/町名/その他に分割するライブラリです
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina is a transliteration library deals with the letters and symbols used in Japanese writing.
 * [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) - Rust implementation of a fast converter between Japanese hankaku and zenkaku characters, mojimoji.
 * [haqumei](https://github.com/o24s/haqumei) - A Japanese Grapheme-to-Phoneme (G2P) library.
 * [ja-furigana](https://github.com/RyuuNeko1107/ja-furigana) - 日本語フリガナ (ルビ) を扱う Rust 製ライブラリ + ローカル HTTP サーバー。ルールはすべてデータ駆動 (TOML)。
 * [jpnorm](https://github.com/yoshitakaoyama/jpnorm) - 日本語テキスト正規化ライブラリ (Rust core + Python)。neologdn 互換・用途別プリセット・URL 保護・カスタム辞書 / Fast, configurable Japanese text normalization


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 655k | ⭐ 91 | 🟡 may|
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 70k | ⭐ 19 | 🔴 april 2020|
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 12 | 🔴 january 2023|
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 | 🟡 february|
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 14 | 🟡 june|
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 27 | 🟡 april|
| 🔗 [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) | - | - | ⭐ 4 | 🔴 november 2022|
| 🔗 [haqumei](https://github.com/o24s/haqumei) | - | - | ⭐ 10 | 🟢 yesterday|
| 🔗 [ja-furigana](https://github.com/RyuuNeko1107/ja-furigana) | - | - | ⭐ 21 | 🟢 today|
| 🔗 [jpnorm](https://github.com/yoshitakaoyama/jpnorm) | - | - | ⭐ 1 | 🟢 yesterday|


### Search engine library
Libraries for Japanese full-text search and indexing

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - A Tantivy tokenizer using Vibrato.
 * [sqlite-vaporetto](https://github.com/hotchpotch/sqlite-vaporetto) - SQLite FTS5 extension for fast Japanese full-text search with 🛥Vaporetto / Vaporetto による高速な日本語全文検索を SQLite FTS5 で実現する拡張機能
 * [duckdb-vaporetto](https://github.com/hotchpotch/duckdb-vaporetto) - DuckDB extension for Japanese full-text search with 🛥Vaporetto / Vaporetto による DuckDB + 日本語全文検索拡張機能
 * [lindera-sqlite](https://github.com/lindera/lindera-sqlite) - Lindera for SQLite FTS5 extention


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 234k | ⭐ 70 | 🟢 august|
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.6k | ⭐ 3 | 🟡 april|
| 🔗 [sqlite-vaporetto](https://github.com/hotchpotch/sqlite-vaporetto) | - | - | ⭐ 21 | 🟡 april|
| 🔗 [duckdb-vaporetto](https://github.com/hotchpotch/duckdb-vaporetto) | - | - | ⭐ 12 | 🟡 april|
| 🔗 [lindera-sqlite](https://github.com/lindera/lindera-sqlite) | - | - | ⭐ 23 | 🟢 august|


### Others
Supplementary crates for Japanese text and IME processing

<details markdown="1">
<summary>Show 26 items</summary>

 * [daachorse](https://github.com/daac-tools/daachorse) - A fast implementation of the Aho-Corasick algorithm using the compact double-array data structure in Rust.
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - Finding all pairs of similar documents time- and memory-efficiently
 * [crawdad](https://github.com/daac-tools/crawdad) - Rust library of natural language dictionaries using character-wise double-array tries.
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) -  Comparison code of various tokenizers
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - Here provides benchmark tools to compare the performance of data structures for string matching.
 * [vime](https://github.com/algon-320/vime) - Using Vim as an input method for X11 apps
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのコア
 * [akaza](https://github.com/akaza-im/akaza) - Yet another Japanese IME for IBus/Linux
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - A free online, self-hostable, multilang Japanese dictionary.
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - Google 日本語入力用DvorakJPローマ字テーブル / DvorakJP Roman Table for Google Japanese Input
 * [niinii](https://github.com/Netdex/niinii) -  Japanese glossator for assisted reading of text using Ichiran
 * [cskk](https://github.com/naokiri/cskk) - SKK (Simple Kana Kanji henkan) library
 * [japanki](https://github.com/tysonwu/japanki) - Learn Japanese vocabs 🇯🇵 by doing quizzes on CLI!
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - Japanese text preprocessor for Text-to-Speech applications (OpenJTalk rewrite in rust language)
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 裁判例のデータ一覧を裁判所のホームページ(https://www.courts.go.jp/index.html) をスクレイピングして生成するソフトウェア
 * [jisho](https://github.com/eagleflo/jisho) - Jisho is a CLI tool & Rust library that provides a Japanese-English dictionary.
 * [kanalizer](https://github.com/voicevox/kanalizer) - 英単語から読みを推測するライブラリ。
 * [koharu](https://github.com/mayocream/koharu) - Automated manga translation tool with LLM, written in Rust.
 * [yomine](https://github.com/mcgrizzz/yomine) - A Japanese vocabulary mining tool designed to help language learners mine new words and expressions.
 * [matsuba](https://github.com/mrpicklepinosaur/matsuba) - lightweight japanese ime written in rust
 * [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) - 日本語辞書 by Rust, support Telegram bot, AWS Lambda and Cloudflare Workers. Support LLM and search RAG.
 * [mecab-dic-converter](https://github.com/tomokane/mecab-dic-converter) - MeCab 用のコンパイル済み辞書を読み取り、解析・再構成し、最終的に Vibrato や Lindera のようなMecab互換 tokenizer が使える辞書へ変換するための Rust crate です。
 * [jp-deinflector](https://github.com/btrkeks/jp-deinflector) - A high-performance Rust crate for deinflecting Japanese words using perfect hash tables
 * [mikke](https://github.com/kimushun1101/mikke) - 日本語 Markdown ノートのローカル検索 CLI 👀 — BM25 全文検索 (SQLite FTS5) + optional なローカル semantic/hybrid。単一バイナリ・外部 API 不使用、AI コーディングエージェント向け。
 * [suiko](https://github.com/nwiizo/suiko) - 日本語文書の自然さと読みやすさを再現可能に診断するRust CLI / Deterministic diagnostics for natural and readable Japanese writing
 * [daac-bpe](https://github.com/vbkaisetsu/daac-bpe) - Fast incremental BPE tokenizer based on daachorse


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 7.8M | ⭐ 284 | 🟢 august|
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k | ⭐ 62 | 🔴 march 2025|
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 194k | ⭐ 39 | 🟢 august|
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 | 🔴 march 2023|
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 228 | 🔴 november 2022|
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1.1k | 🟢 yesterday|
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 265 | 🟡 june|
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 210 | 🔴 january 2024|
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 58 | 🟢 october|
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 16 | 🟢 october|
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 85 | 🟢 yesterday|
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 4 | 🔴 october 2023|
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 60 | 🟡 june|
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 7 | 🟢 july|
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 18 | 🟡 april|
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 31 | 🟡 may|
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 6k | 🟢 last thursday|
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 64 | 🟢 october|
| 🔗 [matsuba](https://github.com/mrpicklepinosaur/matsuba) | - | - | ⭐ 19 | 🔴 march 2023|
| 🔗 [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) | - | - | ⭐ 72 | 🟢 october|
| 🔗 [mecab-dic-converter](https://github.com/tomokane/mecab-dic-converter) | - | - | ⭐ 1 | 🟡 may|
| 🔗 [jp-deinflector](https://github.com/btrkeks/jp-deinflector) | -