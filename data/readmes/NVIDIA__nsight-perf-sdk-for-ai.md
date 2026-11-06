# NVIDIA Nsight Perf SDK for AI

Version: Beta Preview

The NVIDIA Nsight Perf SDK provides APIs and tools for continuously collecting and consuming performance data from NVIDIA GPUs and the CUDA API. It supports always-on profiling so applications can identify performance issues during execution or by post-processing captured data.


## Features

### Continuous, low-overhead profiling

NVIDIA Nsight Perf runs continuously in the background. Representative measurements observed <1% overhead for GPU-limited workloads while tracing CUDA driver API calls. Actual overhead depends on the workload, enabled providers, and configuration; see the [CUDA benchmarks](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/benchmarks/README.md).

### Rich data sources

The SDK can collect:

- CUDA API calls with CPU timestamps, kernel names, and launch dimensions
- GPU workloads, including immediate launches, CUDA graphs, and memory operations
- GPU performance-monitoring counters
- GPU power consumption; see [GPU power metrics](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md#gpu-power-metrics) for hardware, driver, and configuration requirements
- GPU context-switch activity
- NVTX marks and push-pop ranges
- host, operating-system, memory, driver, and GPU information

### Configuration and export

The service uses YAML configuration for resource limits, provider selection, GPU metrics, and sampling rates. Trace Stream Databases can be exported with the [Perfetto trace exporter](https://github.com/NVIDIA/nvtrace-tools/blob/main/PerfettoTraceExporter/README.md) and viewed in [Perfetto](https://ui.perfetto.dev). See the [daemon](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md) and [tools](https://github.com/NVIDIA/nvtrace-tools/blob/main/README.md) documentation.

## Components

- [`nvtrace-client`](https://github.com/NVIDIA/nvtrace-client/blob/main/README.md) contains the target and offline client interfaces and the versioned data formats they consume.
- [`nvtrace-tools`](https://github.com/NVIDIA/nvtrace-tools/blob/main/README.md) contains command-line tools for collecting, inspecting, and exporting traces.
- [`nvtrace-samples-cuda`](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/README.md) contains CUDA samples, tests, and benchmarks.
- [`nsight-perf-daemon`](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md) describes the NVIDIA Nsight Perf service used by the client and tools.
- `third_party` contains the pinned third-party dependencies used by the build.

## Prerequisites

- GPU: NVIDIA Blackwell and Rubin architectures
- CPU: `amd64` or `aarch64`
- OS:
  - Linux: Ubuntu 24.04 on `amd64`, or a compatible derivative such as DGX OS 7.5 on `aarch64`
- CUDA Toolkit 13.5 or newer
- NVIDIA driver:
  - Linux: 620.00.00 or newer
  - Linux kernel-mode drivers starting at 580.95.05 can use the CUDA 13.5 user-mode driver with the [CUDA Compatibility package](https://docs.nvidia.com/deploy/cuda-compatibility/latest/forward-compatibility.html). GPU GR-context tracing has an additional [driver-matching requirement](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md#gpu-gr-context-tracing-and-cuda-forward-compatibility).
- Permission to access performance counters when all metrics are required; see [Resolving ERR_NVGPUCTRPERM](https://developer.nvidia.com/nvidia-development-tools-solutions-err_nvgpuctrperm-permission-issue-performance-counters)

If a system has both supported and unsupported GPUs, use [`CUDA_VISIBLE_DEVICES`](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/environment-variables.html#cuda-visible-devices) to expose only supported devices.

The source build additionally requires CMake 3.24 or newer and a C++17-capable compiler.

For NVTX tracing, applications built against NVTX 3.7 or newer discover the CUDA driver automatically. Applications built against older NVTX versions require the [NVTX CUDA driver injection proxy](https://github.com/NVIDIA/nvtrace-tools/blob/main/NvtxCudaDriverInjectionProxy/README.md), selected through `NVTX_INJECTION64_PATH` when launching the application.

## Quick start

### Get the source

Use either the release source archive or a git clone:

- Download and extract the source archive from the release page, then build from the extracted directory.
- Or clone the repository and initialize its submodules:

  ```shell
  git clone https://github.com/NVIDIA/nsight-perf-sdk-for-ai.git
  cd nsight-perf-sdk-for-ai
  git submodule update --init --recursive
  ```

### Build the client, tools, and samples

```shell
cmake -S . -B build
cmake --build build -j 8
```

### Build output layout

The build writes executables, libraries, and benchmark runner scripts under `build/bin`.

```text
build/
└── bin/
    ├── nvidia-nsight-perf                 # downloaded service executable
    ├── libnvperf_grfx_host.so             # downloaded nvperf-core library
    ├── BenchmarkNvTraceCuda
    ├── BenchmarkNvTraceDemangler
    ├── BenchmarkNvTraceMemory
    ├── BenchmarkNvTraceNvtx
    ├── BenchmarkNvTraceServiceInitialization
    ├── BenchmarkNvTraceZipStreamingCompressor
    ├── DataModelValidator
    ├── TestNvTraceCudaContinuousProfiling
    ├── UptimeTester
    ├── nvtrace_continuous_export
    ├── nvtrace_merge_perfetto_traces
    ├── nvtrace_perfetto_trace_exporter
    ├── nvtrace_poll_until_service_ready
    ├── nvtrace_snapshot_consumer
    ├── nvtrace_streaming_consumer
    ├── nvtx_cuda_driver_injection_proxy    # shared library
    ├── BenchmarkCommon.sh
    ├── RunCudaBenchmarks.sh
    ├── RunNvtxBenchmarks.sh
    ├── benchmark and benchmark_main        # static libraries
    ├── flatbuffers                         # static library
    ├── gtest                               # static library
    ├── libprotobuf, libprotobuf-lite, and libprotoc # static library targets
    ├── perfetto_trace_proto                # static library
    └── protoc                              # native code-generation executable
```

`nvidia-nsight-perf` and its `nvperf-core` library are proprietary binaries, and are downloaded rather than built from source.
Cross-compiled builds create the host-native `protoc` used during the build under `build/third_party/perfetto/protoc_host/bin` instead of `build/bin`.

### Choose a workflow

- To verify a new SDK build, run [NvTraceContinuousProfiling as a smoke test](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/tests/NvTraceContinuousProfiling/README.md).
- To profile an existing application without source changes, start the service before the workload and capture with a [streaming](https://github.com/NVIDIA/nvtrace-tools/blob/main/StreamingConsumer/README.md) or [snapshot](https://github.com/NVIDIA/nvtrace-tools/blob/main/SnapshotConsumer/README.md) consumer.
- To profile a multi-process or Slurm workload, follow the [cluster profiling guidance](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md#cluster-profiling).

### Start the service

From the directory containing the matching service and tool binaries:

```shell
./nvidia-nsight-perf &
./nvtrace_poll_until_service_ready
```

Run the CUDA workload while the service remains active.

### Capture and export a trace

Use a streaming capture for a fixed interval:

```shell
./nvtrace_streaming_consumer --output-dir . --duration-ms 10000
```

Or use a lookback snapshot:

```shell
./nvtrace_snapshot_consumer --output-dir . --duration-ms 1000
```

Each consumer writes a Trace Stream Database directory. Export it to a Perfetto trace:

```shell
./nvtrace_perfetto_trace_exporter --tsf-database-dir <hostname>.<timestamp>
```

Open the generated `.perfetto-trace.zip` file in <https://ui.perfetto.dev>. If a trace is too large to open directly, compress an uncompressed trace with `gzip -9`; Perfetto can open `.gz` files.

For complete command-line details, see the [tool documentation](https://github.com/NVIDIA/nvtrace-tools/blob/main/README.md). For the sample build and smoke test, see the [CUDA samples](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/README.md).

## Compatibility

NVIDIA Nsight Perf makes these compatibility guarantees:

- **CUDA forward compatibility:** NVIDIA Nsight Perf release remains compatible with later CUDA Toolkit, runtime, and driver releases. Features introduced by a later CUDA release may require a newer NVIDIA Nsight Perf release and might not be collected or displayed by an older release.
- **Service-consumer compatibility:** service-connected NvTrace consumers and the NVIDIA Nsight Perf service are compatible across SDK releases in both directions. A newer consumer can connect to an older service, and an older consumer can connect to a newer service. Cross-version use provides the features understood by the participating versions; it does not make newer features available to an older component.

## Software Architecture

NVIDIA Nsight Perf has two primary layers:

1. The **service** runs in a separate process, collects data from GPU and target-side providers, and publishes provider buffers to authorized clients. One service can observe multiple processes and GPUs.
2. The **client** connects to the service, reads provider buffers through observers, writes Trace Streaming Format (`.nvtsf`) data blocks, builds an offline data model, and exports that model to formats such as Perfetto.

The profiled workload runs independently from the consumer. Start the service and consumer before the workload enters the region of interest so the observation window contains all relevant activity.

## Known issues and limitations

- Each GPU can be initialized by only one NVIDIA Nsight Perf service instance at a time because GPU PM-counter and hardware-event sessions are exclusive.
- The `nvidia-nsight-perf` executable should load a CUDA user-mode driver that matches the host kernel-mode driver. Otherwise, GPU GR-context tracing may fail, resulting in incomplete GPU-event correlation or missing GPU timings for named CUDA kernels. See [GPU GR-context tracing and CUDA forward compatibility](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/README.md#gpu-gr-context-tracing-and-cuda-forward-compatibility) for driver requirements and deployment checks.
- Kernels that start before the observation window may not appear.
- NVTX start-end ranges are not supported.
- On the 620 driver, mixing the NVTX core push-pop APIs (nvtxRangePush*/nvtxRangePop) and the Payload Extension push-pop APIs (nvtxRangePushPayload/nvtxRangePopPayload) on the same range may cause the push-pop ranges on that thread to be traced incorrectly. Use the [NVTX CUDA driver injection proxy](https://github.com/NVIDIA/nvtrace-tools/blob/main/NvtxCudaDriverInjectionProxy/README.md) to trace such ranges correctly. Driver versions later than 620 do not require this.
- On the 620 driver, using NVTX in a parent before `fork()` and in its child afterward can cause incorrect traces, hangs or crashes. Using NVTX on only one side of the fork, or in a child that calls `exec()` before using NVTX, is supported.
  - For PyTorch `DataLoader` workers, use `multiprocessing_context="spawn"` or `multiprocessing_context="forkserver"` instead of `"fork"`.
- The maximum recommended GPU PM-counter sampling rate is 20 kHz.
- For batched asynchronous memcpy (cuMemcpyBatchAsync_v2), NVIDIA Nsight Perf may display multiple copies in a CUDA submission group as one GPU memcpy event. The event's duration covers the group, but its transfer details may describe only the first copy. Do not use these events to determine per-copy counts, sizes, addresses, bandwidth, or the duration of the entire batch.


## Contributions

Contributions require signed-off commits and the Developer Certificate of Origin. See [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a change.

## Security

Do not report potential security vulnerabilities through public GitHub issues. Follow the private reporting process in [SECURITY.md](SECURITY.md).

## License

NVIDIA-authored aggregate source and build material are licensed under Apache-2.0; see [LICENSE](LICENSE). Components, imported CUDA Samples, NVTX, and proprietary binaries retain their own terms. See [LICENSING.md](LICENSING.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for component paths, source repositories, and notices.

### External materials

NOTICE AND DISCLAIMER: This software automatically retrieves, accesses or interacts with external materials.  Those retrieved materials are not distributed with this software and are governed solely by separate terms, conditions and licenses.  You are solely responsible for finding, reviewing and complying with all applicable terms, conditions, and licenses, and for verifying the security, integrity and suitability of any retrieved materials for your specific use case. This software is provided "AS IS", without warranty of any kind. The author makes no representations or warranties regarding any retrieved materials, and assumes no liability for any losses, damages, liabilities or legal consequences from your use or inability to use this software or any retrieved materials. Use this software and the retrieved materials at your own risk.

### Component source and license files

| Component path | Source repository | Source license | License file |
| --- | --- | --- | --- |
| `nsight-perf-daemon` | [NVIDIA/nsight-perf-daemon](https://github.com/NVIDIA/nsight-perf-daemon) | Apache-2.0 | [nsight-perf-daemon/LICENSE](https://github.com/NVIDIA/nsight-perf-daemon/blob/main/LICENSE) |
| `nvperf-core` | [NVIDIA/nvperf-core](https://github.com/NVIDIA/nvperf-core) | Apache-2.0 | [nvperf-core/LICENSE](https://github.com/NVIDIA/nvperf-core/blob/main/LICENSE) |
| `nvtrace-client` | [NVIDIA/nvtrace-client](https://github.com/NVIDIA/nvtrace-client) | Apache-2.0 | [nvtrace-client/LICENSE](https://github.com/NVIDIA/nvtrace-client/blob/main/LICENSE) |
| `nvtrace-samples-cuda` | [NVIDIA/nvtrace-samples-cuda](https://github.com/NVIDIA/nvtrace-samples-cuda) | Apache-2.0 | [nvtrace-samples-cuda/LICENSE](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/LICENSE) |
| `nvtrace-tools` | [NVIDIA/nvtrace-tools](https://github.com/NVIDIA/nvtrace-tools) | Apache-2.0 | [nvtrace-tools/LICENSE](https://github.com/NVIDIA/nvtrace-tools/blob/main/LICENSE) |
| `NVTX` | [NVIDIA/NVTX](https://github.com/NVIDIA/NVTX) | Apache-2.0 WITH LLVM-exception | [NVTX/LICENSE.txt](https://github.com/NVIDIA/NVTX/blob/release-v3/LICENSE.txt) |

These independently distributed components retain their own license files. The source licenses above do not cover separately downloaded proprietary binaries or override separately marked assets. See [LICENSING.md](LICENSING.md) for those boundaries.

Additional bundled license files:

- `nvtrace-samples-cuda/cuda-samples/`: BSD-style CUDA Samples terms; see [nvtrace-samples-cuda/cuda-samples/LICENSE](https://github.com/NVIDIA/nvtrace-samples-cuda/blob/main/cuda-samples/LICENSE).
- `NVTX/python/`: Apache-2.0 WITH LLVM-exception; see [NVTX/python/LICENSE.txt](https://github.com/NVIDIA/NVTX/blob/release-v3/python/LICENSE.txt).
- `NVTX/rust/`: Apache-2.0 WITH LLVM-exception; see [NVTX/rust/LICENSE](https://github.com/NVIDIA/NVTX/blob/release-v3/rust/LICENSE).
- `NVTX/docs/`: Apache-2.0 WITH LLVM-exception, subject to separately marked assets; see [NVTX/docs/LICENSE.txt](https://github.com/NVIDIA/NVTX/blob/release-v3/docs/LICENSE.txt).
- `NVTX/tools/docs/github-markdown-css/`: MIT; see [NVTX/tools/docs/github-markdown-css/license](https://github.com/NVIDIA/NVTX/blob/release-v3/tools/docs/github-markdown-css/license).
