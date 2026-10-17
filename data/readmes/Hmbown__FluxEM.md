# FluxEM

[![PyPI version](https://img.shields.io/pypi/v/fluxem-tools)](https://pypi.org/project/fluxem-tools/)
[![CI](https://github.com/Hmbown/FluxEM/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Hmbown/FluxEM/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**Deterministic tools for exact tasks that small models still miss.**

## Status

FluxEM is now tools-first.

- Supported product surface: `fluxem-tools-pkg/` -> `fluxem-tools`
- Supported release scope: a validated core of 35 tools across 9 domains
- Experimental or archived: `fluxem/`, old RL/research harnesses, research docs, and older benchmark artifacts

Archive details live in [docs/ARCHIVE_STATUS.md](/Volumes/VIXinSSD/FluxEM/docs/ARCHIVE_STATUS.md).

## What ships

`fluxem-tools` is a deterministic tool catalog for LLM tool calling. The package registry currently contains 210 tools across 42 domains, but the supported release surface is intentionally narrower:

- `arithmetic`
- `number_theory`
- `physics`
- `chemistry`
- `biology`
- `statistics`
- `finance`
- `temporal`
- `information_theory`

That validated core is the current product story. The broader catalog stays in-repo as experimental surface until it is benchmarked and documented to the same standard.

## Repository layout

- `fluxem-tools-pkg/` - supported package, release gate, catalog manifest, validation scripts
- `examples/` - small-model and OpenAI-compatible integration examples
- `benchmarks/` - current Qwen3.5-2B benchmark harness
- `fluxem/` - archived research track
- `experiments/` - archived or experimental evaluation/training work
- `docs/` - package docs plus archived research pages

## Quick start

```bash
pip install fluxem-tools
```

```python
from fluxem_tools import call_tool

print(call_tool("arithmetic", expr="789123 * 456789"))
print(call_tool("physics_convert", value=88, from_unit="ft/s", to_unit="m/s"))
print(call_tool("finance_npv", rate=0.1, cashflows=[-100, 30, 40, 50, 60]))
```

## SSD-backed Hugging Face cache

Benchmarks and local model downloads should use the SSD-backed Hugging Face root at `/Volumes/VIXinSSD/huggingface`.

```bash
export FLUXEM_HF_ROOT=/Volumes/VIXinSSD/huggingface
export HF_HOME=/Volumes/VIXinSSD/huggingface
export HF_HUB_CACHE=/Volumes/VIXinSSD/huggingface/hub
export HF_DATASETS_CACHE=/Volumes/VIXinSSD/huggingface/datasets
export TRANSFORMERS_CACHE=/Volumes/VIXinSSD/huggingface/hub
```

## Local MLX quickstart (Apple Silicon)

Serve the validated model locally and run with retrieved tools:

```bash
# Start the MLX server
pip install mlx-lm
mlx_lm.server --model mlx-community/Qwen3.5-2B-OptiQ-4bit --port 8000

# Run a query
uv run python examples/qwen35_2b_openai_tools.py \
  "What is 789123 * 456789?" \
  --base-url http://127.0.0.1:8000/v1
```

## Benchmark results

Qwen3.5-2B (4-bit, MLX) on 18 cases across 9 validated domains:

| Condition | Accuracy | Avg Latency |
|-----------|----------|-------------|
| Model only | 38.9% | 908 ms |
| Retrieved tools (max 8) | 88.9% | 911 ms |
| Full registry (210 tools) | 72.2% | 1302 ms |

The retrieved-tools path is the recommended integration for models under 7B. Smaller tool surfaces produce better results on small models.

Entry points:

- `examples/qwen35_2b_openai_tools.py` - end-to-end example
- `benchmarks/qwen35_2b_tools_benchmark.py` - benchmark harness

## Catalog and validation

The package now owns the release-facing catalog artifacts:

- [fluxem-tools-pkg/catalog/manifest.json](/Volumes/VIXinSSD/FluxEM/fluxem-tools-pkg/catalog/manifest.json)
- [fluxem-tools-pkg/catalog/summary.md](/Volumes/VIXinSSD/FluxEM/fluxem-tools-pkg/catalog/summary.md)

To regenerate them:

```bash
cd fluxem-tools-pkg
python scripts/build_catalog_artifacts.py --strict-core
```

## MCP server

```bash
pip install "fluxem-tools[mcp]"
fluxem-tools-mcp
```

The server exposes:

- `fluxem_search`
- `fluxem_call`

## Research archive

The algebraic embedding work remains in the repository as archive material only. It is not the supported product story and it is not the release path for current FluxEM work.
