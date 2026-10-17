# NPU Design

[中文](README_CN.md)

An educational full-stack NPU accelerator demo: end-to-end from 16×16 systolic array RTL design, AXI4 SoC integration, C/Python runtime, UART serial driver, and TVM BYOC compiler backend to neural network inference.

```
NPU_design/
├── systolic_array/         ← RTL + testbenches + SoC integration
│   ├── rtl/                7 compute modules + define.vh
│   ├── soc/                9 SoC integration modules (DMA, regfile, AXI4)
│   ├── tb/                 17 self-checking testbenches + golden model
│   ├── spec/               module specifications (CN/EN)
│   └── principles/         systolic array architecture principles (CN/EN)
├── compiler/               ← ML compiler toolchain
│   ├── cosim/              RTL co-simulation harness (Python + Verilog)
│   ├── runtime/            C runtime + Python reference + UART serial driver
│   ├── tvm_npu/            TVM BYOC target + codegen
│   └── spec/               compiler specification

├── DEPENDENCIES_CN.md / DEPENDENCIES_EN.md   dependency list (CN/EN)
└── README.md               this file
```

## systolic_array — 16×16 Weight-Stationary Systolic Array

### Compute Core (rtl/)

| Module | Description |
|--------|-------------|
| `pe.v` | Processing element (INT8 MAC + data forwarding) |
| `systolic_array.v` | 16×16 PE grid (generate-loop) |
| `systolic_array_ctrl.v` | 3-state FSM (IDLE/COMPUTE/DRAIN) |
| `ifmap_buffer.v` | Dual-buffer with per-row skew chain |
| `weight_buffer.v` | Dual-buffer with row/column dual read |
| `accumulator.v` | Cross-tile accumulator + output buffer |
| `systolic_array_top.v` | System top (dual-skew aligned + streaming I/O) |

### SoC Integration (soc/)

| Module | Description |
|--------|-------------|
| `npu_soc_top.v` | NPU SoC top-level (DMA + SA + stream adapters) |
| `reg_file.v` | Control/status register file |
| `axi4_lite_regfile.v` | AXI4-Lite → register file bridge |
| `dma_engine.v` | DMA controller (protocol-agnostic) |
| `axi4_mem_bridge.v` | AXI4 memory bridge |
| `axi4_dma_wrapper.v` | AXI4 DMA wrapper (engine + bridge) |
| `stream_splitter.v` | DMA byte stream → ifmap/weight dual streams |
| `result_packer.v` | SA wide result → DMA byte stream |
| `npu_uart_bridge.v` | UART → AXI4-Lite bridge for embedded control |

### Quick Start

```bash
# Run the full SoC cosim (requires Icarus Verilog 12)
cd compiler/cosim
make test_M8_K64_N8

# Run a single testbench
cd systolic_array
iverilog -I rtl -o pe_tb.out rtl/pe.v tb/pe_tb.v && vvp pe_tb.out

# Generate test vectors
python tb/test_vectors/golden_model.py gen
```

## compiler — ML Compiler Toolchain

| Component | Description |
|-----------|-------------|
| `cosim/` | Python test generation + cosim_tb.v + Makefile |
| `runtime/npu_runtime.c` | C bare-metal GEMM runtime |
| `runtime/npu_serial.py` | Python UART serial driver |
| `tvm_npu/python/` | TVM BYOC target, codegen, and setup |
| `e2e_pipeline.py` | End-to-end cosim pipeline |

### Quick Start

```bash
# Python-only reference
python compiler/runtime/npu_runtime.py check

# C runtime integration test
gcc -std=c99 -Wall -Wextra -O2 -DTEST_NPU_RUNTIME \
    -o npu_test compiler/runtime/npu_runtime.c && ./npu_test

# TVM BYOC setup
python compiler/tvm_npu/python/setup_tvm_npu.py
```

## Test Results

All 17 testbenches passing (iverilog simulation) across PE, SA, buffer, accumulator, golden model,
SoC integration, DMA engine, and AXI4 bridge levels.

## Hardware Verification

Deployed and verified on real silicon — **XCZU4EV-SFVC784-1-I** FPGA board, clocked at **175 MHz**.

| Item | Specification |
|------|--------------|
| Chip | Xilinx Zynq UltraScale+ XCZU4EV |
| Clock Frequency | 175 MHz |
| FPGA Toolchain | Vivado 2023.2 (recommended) |
| Peak Throughput | 256 MAC × 175 MHz = **44.8 GMAC/s (INT8)** |
| Peak OPS | 512 OPS × 175 MHz = **89.6 GOPS** |
| Power | 2.1 W (NPU logic only) |
| Efficiency | 21.3 GMAC/s/W |

### LeNet-5 Handwritten Digit Recognition (32×32 → 10 classes)

- **TVM Backend**: Relax IR → `FuseOpsByPattern` → `npu_gemm()` calls — full BYOC pipeline verified on hardware
- **Direct Invocation**: No TVM dependency; hand-written C calling `npu_runtime.c` GEMM interface — also verified
- Model: Conv1(1→6, 5×5) → Pool → Conv2(6→16, 5×5) → Pool → FC(256→120) → FC(120→84) → FC(84→10)
- Inference latency (Python cycle model estimate): **655 SA calls**, 875k cycles, **5.0 ms** @ 175 MHz (NPU compute only)
- End-to-end latency (measured on FPGA): **5.1 ms** over PCIe/ETH; ~1 s over UART

### Transport Comparison (single 32×32 image)

| Transport | End-to-End Measured Latency | Notes |
|-----------|---------------------------|-------|
| UART (115200 baud) | ~1 s | Debug/low-speed control; serial transfer |
| PCIe | 5.1 ms | DMA transfer; compute and transport decoupled |
| Ethernet | 5.1 ms | Raw UDP frames; compute and transport decoupled |

## License

GNU AGPLv3 — see [LICENSE](LICENSE).

---
> **Document Version**: v0.8.0 | **Last Updated**: 2026-07-29
