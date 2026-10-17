# Optical Character Recognition

[![CI](https://github.com/mftnakrsu/Comparison-of-OCR/actions/workflows/ci.yml/badge.svg)](https://github.com/mftnakrsu/Comparison-of-OCR/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%E2%80%93%203.13-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

OCR (Optical Character Recognition) is a technology that enables the conversion of document types such as scanned paper documents, PDF files or pictures taken with a digital camera into editable and searchable data. OCR creates words from letters and sentences from words by selecting and separating letters from images.

![robot](https://user-images.githubusercontent.com/57320216/156442638-c681624f-a8cd-45ed-a4cc-8a626d295f46.jpg)

This repository runs several OCR engines over the same images and reports what each
one read, how long it took and how confident it was — so you can see the trade-offs
rather than read about them.

# Table of Content
- [Optical Character Recognition](#optical-character-recognition)

  * [Engines](#engines)
  * [Requirements](#requirements)
  * [Usage](#usage)
  * [Python API](#python-api)
  * [Results](#results)
  * [Conclusion](#conclusion)
  * [Project layout](#project-layout)
  * [Source](#source)


## Engines

Each engine is an optional extra, so you install only the ones you want to run.

| Engine | Extra | Install weight | Notes |
| --- | --- | --- | --- |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | `tesseract` | tiny (needs a system binary) | Fast, best on clean high-resolution scans |
| [EasyOCR](https://github.com/JaidedAI/EasyOCR) | `easyocr` | large (torch) | Good all-rounder, 80+ languages, handles noise well |
| [RapidOCR](https://github.com/RapidAI/RapidOCR) | `rapidocr` | small (onnxruntime) | PaddleOCR models in ONNX — the lightest way to get modern accuracy |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | `paddle` | large (paddlepaddle) | Strongest accuracy in this line-up |
| [keras-ocr](https://github.com/faustomorales/keras-ocr) | `keras-legacy` | large (TensorFlow) | The original 2022 engine — see the note below |

Check what you have installed at any time:

```bash
python -m ocr_compare --list-engines
```

> **About keras-ocr.** It has had no release since 0.9.3 (November 2023) and pins
> `efficientnet==1.0.0` and `imgaug` (last released in 2020), which do not resolve
> against NumPy 2 or Keras 3. It therefore needs Python ≤ 3.11 and lives behind the
> `keras-legacy` extra so it cannot constrain the rest of the project. If it is not
> installed it simply reports as unavailable and everything else still runs.
> The keras-ocr output shown under [Results](#results) is the original 2022 run.

## Requirements

Python 3.10 or newer.

```bash
git clone https://github.com/mftnakrsu/Comparison-of-OCR.git
cd Comparison-of-OCR

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[easyocr,tesseract]"               # or pick your own engines
```

Or, with [uv](https://docs.astral.sh/uv/):

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[easyocr,tesseract]"
```

Available extras: `tesseract`, `easyocr`, `rapidocr`, `paddle`, `keras-legacy`,
`all` (everything except `keras-legacy`), and `dev` (pytest + ruff).

Tesseract also needs its system binary — the pip package is only a wrapper:

```bash
brew install tesseract tesseract-lang                  # macOS
sudo apt install tesseract-ocr tesseract-ocr-tur       # Debian / Ubuntu
```

Windows builds: <https://github.com/UB-Mannheim/tesseract/wiki>

`pip install -r requirements.txt` still works and installs the core plus the two
lightest engines.

## Usage

```bash
python main.py                    # every installed engine, over test/
python -m ocr_compare             # the same thing
```

```bash
# pick engines and languages
python -m ocr_compare test/ --engines tesseract,easyocr --languages tr,en

# save the comparison figure instead of opening a window
python -m ocr_compare test/ --engines all --save-plot results/compare.png

# machine-readable output, no plotting
python -m ocr_compare test/ --no-plot --json results/run.json
```

Output looks like this:

```
[tesseract] 2.jpg  0.31s  7 boxes
    Comparison of OCR engines
[easyocr] 2.jpg  1.84s  6 boxes
    Comparison of OCR engines

engine     images  boxes  total (s)  s/image  mean conf  errors
---------  ------  -----  ---------  -------  ---------  ------
tesseract       1      7       0.31     0.31      0.912       0
easyocr         1      6       1.84     1.84      0.887       0
```

All options: `python -m ocr_compare --help`.

## Python API

```python
from ocr_compare import EasyOCREngine, TesseractEngine
from ocr_compare import format_table, run_benchmark, summarize

engines = [
    TesseractEngine(languages=["tr", "en"]),
    EasyOCREngine(languages=["tr", "en"]),
]

results = run_benchmark(engines, "test/")
print(format_table(summarize(results)))

for result in results:
    print(result.engine, result.elapsed_s, result.text)
    for box in result.boxes:
        print(" ", box.text, box.polygon, box.confidence)
```

Every engine returns the same `TextBox(text, polygon, confidence)` shape, so adding
an engine means writing one small adapter in `ocr_compare/engines/` and registering
it — nothing else changes.

The original class-based API still works:

```python
from ocr import OCR

ocr = OCR(image_folder="test/")
ocr.easyocr_model_works()
ocr.pytesseract_model_works()
ocr.compare()                     # every installed engine, side by side
```

 ## Results
 ![kerasocr1](https://user-images.githubusercontent.com/57320216/156442703-ff06fce6-174a-4859-9d45-b32b4187b1d5.png)
![kerasocr2](https://user-images.githubusercontent.com/57320216/156442709-cea41264-e369-48a3-92b0-afa752c313fb.png)
![kerasocr3](https://user-images.githubusercontent.com/57320216/156442712-c05cbf58-0c9b-41fa-bd7b-c42704194527.png)

 
 ## Conclusion
 
 - It seems that pytesseract is not very good at detecting text in the entire image and converting str. Instead, text should be detected first with text detection and the texts have to given OCR engines.
 
 - While keras_ocr is good in terms of accuracy but it is costly in terms of time. Also if you’re using CPU, time might be an issue for you.
Keras-OCR is image specific OCR tool. If text is inside the image and their fonts and colors are unorganized.

- Easy-OCR is lightweight model which is giving a good performance for receipt or PDF conversion. It is giving more accurate results with organized texts like PDF files, receipts, bills. Easy OCR also performs well on noisy images.

- Pytesseract is performing well for high-resolution images. Certain morphological operations such as dilation, erosion, OTSU binarization can help increase pytesseract performance.
    

- All these results can be further improved by performing specific image operations. OCR Prediction is not only dependent on the model and also on a lot of other factors like clarity, grey scale of the image, hyper parameter, weight age given, etc.
 
    
### Notes

The comparison above was made in 2022 with keras-ocr, EasyOCR and pytesseract. Since
then RapidOCR and PaddleOCR have joined the line-up, and keras-ocr has stopped being
maintained. Run the benchmark on your own images before drawing conclusions — the
right engine depends heavily on the images you have.

## Project layout

```
ocr_compare/
  base.py          TextBox / EngineResult and the OCREngine base class
  engines/         one adapter per engine, plus the registry
  images.py        finding and loading images
  benchmark.py     running engines and summarising timings
  visualize.py     the images x engines comparison figure
  cli.py           python -m ocr_compare
ocr.py             backwards-compatible OCR class
main.py            entry point
tests/             runs without any engine installed, downloads nothing
```

Development:

```bash
pip install -e ".[dev]"
pytest
ruff check . && ruff format --check .
```

 ## Source
 https://github.com/faustomorales/keras-ocr  
 https://github.com/JaidedAI/EasyOCR  
 https://pypi.org/project/pytesseract/  
 https://github.com/RapidAI/RapidOCR  
 https://github.com/PaddlePaddle/PaddleOCR  
