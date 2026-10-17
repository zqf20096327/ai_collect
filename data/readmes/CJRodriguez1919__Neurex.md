# Neurex

Open-source brain-computer interface software stack.

[![ci](https://github.com/CJRodriguez1919/Neurex/actions/workflows/ci.yml/badge.svg)](https://github.com/CJRodriguez1919/Neurex/actions/workflows/ci.yml)
[![docs](https://github.com/CJRodriguez1919/Neurex/actions/workflows/docs.yml/badge.svg)](https://docs.neurex.health)
[![PyPI](https://img.shields.io/pypi/v/neurex.svg)](https://pypi.org/project/neurex/)
[![Python](https://img.shields.io/pypi/pyversions/neurex.svg)](https://pypi.org/project/neurex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Neurex sits between consumer EEG hardware and your application. It owns
the signal processing, feature extraction, and decoding pipelines that
turn raw electrode samples into intent. It is the layer everyone with
a headset ends up writing themselves; this is one decent attempt at
writing it once and giving it away.

## What it does

Real-time decoding of:

- Motor imagery (left vs right hand) via CSP+LDA, FBCSP, or Riemannian tangent-space classifiers
- Sustained attention / focus via theta-alpha ratio
- P300 event-related potentials for spellers, with optional SWLDA
- Steady-state visual evoked potentials (SSVEP) via canonical correlation analysis
- Emotional valence via frontal alpha asymmetry

Plus the supporting infrastructure: streaming filters with bounded
latency, calibration session capture and persistence, model registry,
quality checks, ICA for offline artifact removal, hardware adapters
for OpenBCI / Muse / Crown / Galea / any LSL outlet.

## Install

```bash
pip install neurex
```

For real hardware:

```bash
pip install "neurex[brainflow]"
pip install "neurex[lsl]"
```

For development:

```bash
git clone https://github.com/CJRodriguez1919/Neurex
cd Neurex
pip install -e ".[dev]"
pre-commit install
pytest
```

## 30-second example

```python
from neurex.io.board import open_board
from neurex.decoders.decoder import MotorImageryDecoder
from neurex.streaming.pipeline import Pipeline, PipelineConfig
from neurex.preprocess.filters import FilterSpec

decoder = MotorImageryDecoder()
decoder.fit(training_windows, training_labels)

board = open_board("brainflow:cyton", serial_port="/dev/ttyUSB0")
pipeline = Pipeline(
    board=board,
    decoder=decoder,
    config=PipelineConfig(
        window_seconds=2.0,
        stride_seconds=0.5,
        filter=FilterSpec(bandpass=(8.0, 30.0), notch_hz=50.0),
    ),
)

for decision in pipeline.decisions():
    print(f"{decision.label}  conf={decision.confidence:.2f}")
```

No background threads, no callbacks. The pipeline runs on whatever
thread calls `decisions()`. If you need concurrency, wrap it.

For development without hardware:

```python
board = open_board("synthetic")
```

## What's in the box

```
neurex/
  io/                board adapters, sample types, replay
  preprocess/        causal/offline filters, ICA, quality checks
  features/          CSP, FBCSP, Riemannian, shrinkage covariance
  decoders/          motor imagery, focus, valence, P300, SSVEP
  streaming/         pipeline, ring buffer
  calibration/       session capture, persistence, randomization
  registry/          fitted-model registry with metadata
  cli/               command-line tool
```

108 tests on the suite, ruff and mypy clean. CI runs on Python 3.11,
3.12, 3.13 across Linux, macOS, and Windows.

## What this is not

- Not a medical device. The decoders are research-grade. Do not put this in a clinical setting.
- Not an LLM project. There are no language models here.
- Not a hardware company. We support common consumer EEG hardware via published protocols.
- Not finished. Active development; expect breaking changes through 1.0.

## Documentation

Full docs at [docs.neurex.health](https://docs.neurex.health):

- [Quickstart](https://docs.neurex.health/getting-started/quickstart/)
- [Hardware compatibility](https://docs.neurex.health/getting-started/hardware/)
- [Architecture rationale](https://docs.neurex.health/architecture/)
- [Algorithm references](https://docs.neurex.health/reference/papers/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Tests are mandatory for code
changes; docstrings are mandatory for public APIs; the CI matrix must
be green before review.

## License

MIT. See [LICENSE](LICENSE).

## Citation

If Neurex is useful in your research:

```bibtex
@software{neurex,
  author = {Rodriguez, Christian},
  title = {Neurex: open-source brain-computer interface software stack},
  url = {https://github.com/CJRodriguez1919/Neurex},
  version = {0.6.2},
  year = {2026},
}
```

## Acknowledgements

This library stands on a lot of prior work. The algorithms here are
implementations of published research; see [docs/REFERENCES.md](docs/REFERENCES.md)
for the full bibliography. Particular debt to the BCILAB, MNE-Python,
PyRiemann, and BrainFlow projects, all of which solved adjacent
problems years before this one existed.
