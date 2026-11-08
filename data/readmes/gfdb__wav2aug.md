# Wav2Aug: A Drop-In Speech Augmentation Policy

Wav2Aug is a PyTorch waveform augmentation policy with settings calibrated once
and reused across speech tasks. [Read the paper](https://arxiv.org/abs/2610.38656).

## Quick Start

Requires Python 3.10+ and [FFmpeg shared libraries](#ffmpeg).

```bash
pip install wav2aug
```

Or use `uv add wav2aug`.

The default configuration matches the paper's top-6 policy.

```python
import torch
from wav2aug.gpu import Wav2Aug

# Initialize the paper's top-6 policy once
augmenter = Wav2Aug(sample_rate=16000)

# In the training forward pass
wavs = torch.randn(3, 50000)
lens = torch.ones(wavs.size(0))
aug_wavs, aug_lens = augmenter(wavs, lens)

# Or omit lengths if they are not needed
aug_wavs = augmenter(wavs)
```

## Results

Across ten speech benchmarks, Wav2Aug remains competitive with SpecAugment on ASR.
Its top-6 configuration achieves a **12.8% average relative error reduction** over
the strongest compatible SpecAugment baseline across five non-ASR tasks. See the
paper's [ASR results](https://arxiv.org/html/2610.38656v1#S3.T2) and
[non-ASR results](https://arxiv.org/html/2610.38656v1#S3.T3) for the full comparison.

![Diagram](https://raw.githubusercontent.com/gfdb/wav2aug/main/wav2aug.png)

## Setup and Configuration

### FFmpeg

TorchCodec requires FFmpeg shared libraries for audio decoding. Install FFmpeg
before running the quick start:

```bash
# macOS (Homebrew)
brew install ffmpeg

# Ubuntu / Debian
sudo apt-get update && sudo apt-get install -y ffmpeg
```

For Windows and other platforms, follow the
[TorchCodec installation instructions](https://github.com/meta-pytorch/torchcodec#installing-torchcodec).
If installing into an existing PyTorch environment, check TorchCodec's compatibility
table for your PyTorch version.

### Noise Download and Memory

The first initialization downloads a roughly 569 MB noise archive from Hugging Face
and preloads the decoded audio into RAM. Later initializations reuse the downloaded
files. Set `WAV2AUG_DATA_DIR` before importing wav2aug to change the cache location
(default: `~/.cache/wav2aug`), or supply your own audio directory to avoid downloading:

```python
augmenter = Wav2Aug(sample_rate=16000, noise_dir="/path/to/noise")
```

Noise is stored in FP32 by default. Set `noise_dtype=torch.float16` to halve the
noise bank's RAM usage. In our testing, FP16 works very well, with less than 0.1
percentage points of WER degradation.

### Augmentation Pool

The default top-6 pool contains noise addition, frequency dropout, time dropout,
speed perturbation, amplitude clipping, and chunk swapping. Each call samples two
augmentations with replacement and applies them sequentially. Parameters are
sampled independently for each application, including when the same augmentation
is selected twice.

Set `top_k=9` to sample from all nine augmentations, or `top_k=1` to apply noise
addition once. Top-9 can outperform top-6 on some tasks, including language
identification and emotion recognition, as shown in
[Table III of the paper](https://arxiv.org/html/2610.38656v1#S3.T3).

## Augmentation Types

* **Amplitude Scaling/Clipping**: Random gain and peak limiting
* **Noise Addition**: Environmental noise with SNR control
* **Frequency Dropout**: Spectral masking with random notch filters
* **Polarity Inversion**: Random phase flip
* **Chunk Swapping**: Temporal segment reordering
* **Speed Perturbation**: Time-scale modification
* **Time Dropout**: Random silence insertion
* **Babble Noise**: Multi-speaker background (auto-enabled with sufficient buffer)

**Randomness**: all stochastic ops use PyTorch RNGs. Set a single seed and be done, e.g. `torch.manual_seed(0)`, `torch.cuda.manual_seed_all(0)`


## Development Installation

### uv

```bash
git clone https://github.com/gfdb/wav2aug
cd wav2aug

# create venv and pin Python
uv venv
source .venv/bin/activate
uv python pin 3.10  # or 3.11/3.12

# runtime only
uv sync

# extras
uv sync --extra dev
uv sync --extra test
```

### pip

```bash
git clone https://github.com/gfdb/wav2aug
cd wav2aug

# create venv
python -m venv .venv
source .venv/bin/activate

# runtime only
python -m pip install .

# editable + extras for development
python -m pip install -e '.[dev,test]'
```

## Tests

### uv

```bash
uv run pytest -q tests/
```

### pip

```bash
pytest -q tests/
```

## Contributing

* Feel free to open a PR!

* Bug reports: please open an issue with a minimal repro (env, dep versions, code snippet, expected vs. actual, traceback, etc.) ty :)

* Feature requests: please [open an issue](https://github.com/gfdb/wav2aug/issues) describing what you'd like and your use case. If it's not already in the library and fits its scope, I'd be happy to add it!
