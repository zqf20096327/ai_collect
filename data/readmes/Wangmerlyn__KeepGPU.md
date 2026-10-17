# KeepGPU

[![PyPI Version](https://img.shields.io/pypi/v/keep-gpu.svg)](https://pypi.org/project/keep-gpu/)
[![Docs Status](https://readthedocs.org/projects/keepgpu/badge/?version=latest)](https://keepgpu.readthedocs.io/en/latest/?version=latest)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17129114.svg)](https://doi.org/10.5281/zenodo.17129114)

KeepGPU is a small, polite GPU keeper for shared machines. It allocates only
when utilization backoff permits, keeps the requested VRAM signal lightweight,
and releases cleanly when you are done.

## Quick Start

```console
pip install keep-gpu
keep-gpu --gpu-ids 0 --vram 1GiB --interval 60
```

Press `Ctrl+C` to release. CUDA, ROCm/HIP, and Apple Silicon MPS are supported
when PyTorch can see the target device.

## Documentation

- [Documentation](https://keepgpu.readthedocs.io/en/latest/) is the full guide hub.
- [Getting Started](https://keepgpu.readthedocs.io/en/latest/getting-started/) covers install options and the first hardware check.
- [Citation](https://keepgpu.readthedocs.io/en/latest/citation/) has the BibTeX entry.
