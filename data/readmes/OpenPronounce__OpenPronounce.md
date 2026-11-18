<h1 align="center">OpenPronounce</h1>

<p align="center">
  <b>Open-source, phoneme-level pronunciation assessment.</b><br>
  Give it a recording. Get the scores a human rater would give (overall, accuracy, fluency, prosody) and the words that went wrong, with the sounds actually heard. With the expected sentence or without. On your machine, on CPU.
</p>

<p align="center">
  <a href="https://pypi.org/project/openpronounce/"><img src="https://img.shields.io/pypi/v/openpronounce.svg" alt="PyPI"></a>
  <a href="https://github.com/OpenPronounce/OpenPronounce/actions/workflows/tests.yml"><img src="https://github.com/OpenPronounce/OpenPronounce/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="https://colab.research.google.com/github/OpenPronounce/OpenPronounce/blob/main/OpenPronounce-demo.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a>
  <a href="LICENSING.md"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue.svg" alt="License: AGPL-3.0"></a>
</p>

<p align="center">
  <img src="./docs/demo.gif" alt="OpenPronounce web demo: record a sentence, get a score, see which sounds went wrong" width="720">
</p>

```console
$ openpronounce developer.wav "Hello, I am a good designer"
Score        : 36.2/100
               accuracy 36.6, fluency 55.0, prosodic 45.9
Warning      : not said: good (scores unreliable)
Transcription: HELLO I AM A DEVELOPER
Heard phones : /h ə l oʊ aɪ æ m ə d ɪ v ɛ l ə p ɚ/
Mispronounced:
  - good: not said
  - designer: expected /dɪzaɪnɚ/, heard /vɛləpɚ/ (confidence 89%)
```

Azure Speech, SpeechAce or ELSA sell this behind an API key and a per-minute price. Here there is no key and no meter, and your learners' voices never leave your servers.

## Install

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu   # CPU wheels, much smaller
pip install openpronounce
```

You need Python 3.10+ and `ffmpeg`; every language other than English also needs the `espeak-ng` program. The first run downloads two Wav2Vec2 checkpoints of 1.2 GB each.

## Use it

```bash
openpronounce recording.wav "Hello, I am a developer"            # you know the sentence
openpronounce talk.wav                                           # you do not: free speech, any length
openpronounce bonjour.wav "Bonjour, je suis développeur" --lang fr
```

```python
from openpronounce import load_audio, assess

result = assess(load_audio("recording.wav"), "Hello, I am a developer")
print(result["score"], result["scores"])     # 76.6 {'total': 76.6, 'accuracy': 86.0, 'fluency': 79.3, 'prosodic': 77.1}
print(result["reliable"], result["reasons"]) # False when the score should not be shown as it is

talk = assess(load_audio("talk.wav"))        # no text: free speech
```

With the sentence, you get the words that went wrong and their sounds, the words that were not said and what was said in excess. Without it, the transcript, the same four scores and the words that came out unclear. `--fast` loads one checkpoint instead of two, `--json` prints everything.

A web demo and an HTTP API come with it: `docker run -p 8000:8000 $(docker build -q .)`, then http://localhost:8000. Fields, endpoints and settings are in [docs/reference.md](docs/reference.md).

## How good is it

On 2,500 recordings of learners the models never heard, each rated by five experts ([speechocean762](https://www.openslr.org/101/)), this is how closely the overall score follows the raters (Pearson correlation):

| | Sentence known | Free speech |
|---|---|---|
| Adults | 0.85 | 0.82 |
| Everyone | 0.79 | 0.71 |
| Children of 12 and under | 0.67 | 0.42 |

One word in twenty is reported, and the raters rejected 54 % of those. English is the measured language. French, Spanish, German, Italian, Portuguese and Dutch run on the same models, with or without the sentence. Their native speakers score like English ones, but nobody rated learners of these languages, and the few recordings of learners that exist give a mixed picture ([limits](docs/limits.md)).

Those learners speak Mandarin and read short sentences. Yours may not, so measure it on your own rated recordings before you trust it:

```bash
openpronounce-evaluate manifest.csv      # columns: audio, score, and text when the sentence is known
```

It prints the correlation with your assessors and its 95 % interval. What the product does not do is listed in [docs/limits.md](docs/limits.md), the method in [docs/how-it-works.md](docs/how-it-works.md), every figure and script in [benchmarks/](benchmarks/README.md).

## Licence

Free software under the AGPL: use it, change it, publish what you build on it under the same terms. To ship it inside a closed product, a commercial licence replaces the AGPL, for every language. See [LICENSING.md](LICENSING.md). Releases up to 0.4 remain MIT.
