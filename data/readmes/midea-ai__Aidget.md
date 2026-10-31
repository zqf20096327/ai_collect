<div align="center">

<h1><img src="./docs/assets/aidget-logo.png" alt="Aidget" width="320"></h1>
<p><strong>Compact C programs for resource-efficient edge inference.</strong></p>
<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0-1F94D2?style=flat" alt="License: Apache-2.0"></a>
  <a href="./runtime/README.md"><img src="https://img.shields.io/badge/Runtime-C-555555?style=flat&amp;logo=c&amp;logoColor=white" alt="Runtime: C"></a>
  <a href="./docs/USAGE.md#python-environment"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&amp;logo=python&amp;logoColor=white" alt="Python: 3.10+"></a>
  <a href="./tools/converter/README.md"><img src="https://img.shields.io/badge/Input-TFLite-FF6F00?style=flat&amp;logo=tensorflow&amp;logoColor=white" alt="Input: TFLite"></a>
</p>
<p>
  <a href="./docs/GETTING_STARTED.md">Get started</a> ·
  <a href="./docs/ARCHITECTURE.md">Architecture</a> ·
  <a href="./docs/BENCHMARKS.md">Benchmarks</a>
</p>
<p><strong>English</strong> · <a href="./README.zh-CN.md">简体中文</a></p>

</div>

Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources. It is used for AI deployment across Midea's business divisions and has supported the mass production of smart appliances, including air conditioners, refrigerators, and robot vacuums.

This version update of [midea-ai/Aidget](https://github.com/midea-ai/Aidget) provides the inference runtime and model conversion toolchain in source form.

The engine converts fixed-shape TFLite models into model-specific C programs for CPUs and MCUs. Model preparation runs on the host; the device executes direct C calls with application-controlled memory. Supported numerical paths include FP32, INT8, and hybrid operators, with optional Arm NEON, CMSIS-NN, and ESP-NN acceleration.

| Static execution | Planned memory | Flexible integration |
| --- | --- | --- |
| Prepare operator settings and parameter layouts before deployment. | Reuse tensor and workspace storage with explicit placement policies. | Embed C sources or integrate through static and shared libraries. |

## ESP32-S3 performance

**240 MHz · One inference thread on CPU0 · SRAM working memory**

The comparison includes Aidget, TFLM, tuned TVM, ncnn, ExecuTorch, and uTensor, retaining original model arithmetic.

![ESP32-S3 comparison: latency, working memory, executable code, and board energy.](./docs/figures/esp32-comparison.png)

*Blue: absolute Aidget(speed) values. Other cells: ratio to the same-model baseline; lower is better. A dash indicates no comparable measurement.*

Working memory excludes stacks and state outside the pool; code includes platform support but excludes weights and other data. [Full results and methodology →](./docs/BENCHMARKS.md)

## Raspberry Pi Zero W performance

**Fixed 1 GHz · Single ARMv6 core · Original FP32 models**

![Raspberry Pi Zero W comparison: deployment code size and latency for AD, IC, VWW, and KWT3.](./docs/figures/raspberry-pi-comparison.png)

*Lower-left is better; both axes are logarithmic. Points show median latency across 12 timing-group means; bars show the observed range. Code is linked deployment `.text`, excluding data and shared system libraries.*

[Configurations, measurements, and methodology →](./docs/benchmarks/raspberry-pi-zero-w.md)

## Documentation

| Guide | Scope |
| --- | --- |
| **[Beginner tutorial](./docs/GETTING_STARTED.md)** | A bundled random model: conversion, C deployment, consistency checks, and performance measurement |
| **[Usage and deployment](./docs/USAGE.md)** | Python environment, model conversion, source integration, static libraries, and shared libraries |
| [Architecture](./docs/ARCHITECTURE.md) · [Converter](./tools/converter/README.md) | Execution model, memory planning, and supported conversion options |
| [C API](./runtime/include/README.md) · [Backends](./docs/BACKENDS.md) | Application interfaces, platform hooks, and optional acceleration |
| [Development](./docs/DEVELOPMENT.md) · [Tests](./tests/README.md) | Contributor workflow and regression coverage |

---

[Apache-2.0](./LICENSE) · [Notice](./NOTICE) · [Third-party notices](./THIRD_PARTY_NOTICES.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
