# LLaMA-2 FPGA Inference Accelerator — Zynq UltraScale+ ZCU102

A hybrid FPGA/CPU inference engine for LLaMA-2, built by offloading its four matrix-multiplication shapes to dedicated Vitis HLS kernels on a Xilinx/AMD Zynq UltraScale+ ZCU102, while nonlinear operators (RMSNorm, RoPE, attention, SwiGLU) stay on the onboard ARM Cortex-A53.

Built as part of a research effort comparing FPGA, GPU, and CPU acceleration strategies for LLaMA-2 inference — see the companion **[llama2-cuda](https://github.com/Salik-Devv/llama2-cuda)** GPU implementation (RTX 4060 Laptop).

---

## Results at a Glance

| Platform | tok/s (decode) | GOPS | Δ Power (PMBus, n=8) | GOPS/W |
|---|---|---|---|---|
| CPU-only (ARM Cortex-A53, scalar) | 13.88 | 0.422 | 0.339 ± 0.006 W | 1.24 |
| **FPGA hybrid (this repo)** | **41.55** | **1.39–1.41** | **0.326 ± 0.021 W** | **4.45** |

The FPGA path is **3.3× faster** and **3.59× more power-efficient (GOPS/W)** than the CPU-only baseline, on the same board. Power figures are rail-level PMBus measurements (n=8 trials/condition, idle-subtracted) — see [Power Methodology](#power-methodology) for why an earlier, simpler measurement pass gave an untrustworthy number.

---

## Architecture

The design keeps LLaMA-2's nonlinear operators on the ARM cores and offloads its four distinct matmul shapes to dedicated kernels:

| Kernel | Shape | Weight(s) | PS Port(s) |
|---|---|---|---|
| `gemv_top` | 288×288 ×4 | Wq, Wk, Wv, Wo (attention projections) | HPC0 |
| `ffn_up_top` | 768×288 ×2 | W1, W3 (FFN up-projection) | HP2 |
| `ffn_down_top` | 288×768 | W2 (FFN down-projection) | HP3 |
| `classifier_top` | 288×32,000 | Wcls (output logits) | HPC1, HP0, HP1 |

Every non-ACP HP/HPC port on the ZCU102 is committed — four kernels' AXI master interfaces span exactly the six available high-performance ports.

Model: LLaMA-2 **stories15M** (dim=288, hidden=768, 6 layers, 6 heads, vocab=32,000), via [Karpathy's llama2.c](https://github.com/karpathy/llama2.c) checkpoint format.

---

## Repository Structure

```
llama2acc/
├── src/
│   ├── hw/                    # Vitis HLS kernel sources
│   │   ├── gemv_{compute,memory,top}.cpp / gemv.h
│   │   ├── ffn_up_{compute,memory,top}.cpp / ffn_up.h
│   │   ├── ffn_down_{compute,memory,top}.cpp / ffn_down.h
│   │   └── classifier_{compute,memory,top}.cpp / classifier.h
│   └── sw/
│       └── host.cpp           # ARM-side host application (XRT)
├── tb/                        # Testbenches (HLS cosim + standalone)
│   └── data/
├── script/                    # HLS build scripts
│   ├── run_hls_classifier.tcl
│   ├── run_hls_ffn_up.tcl
│   ├── run_hls_ffn_down.tcl
│   └── run_hls.tcl            # gemv_top
├── results/                   # Measured results (CPU baseline, FPGA hybrid)
├── power_final/                # PMBus/INA226 power-measurement scripts & logs
└── hls_classifier/, hls_ffn_up/, hls_ffn_down/, hls_component/,
    new_viv_comp/, _ide/        # Vitis/Vivado auto-generated build output (gitignored)
```

`miscellaneous/` and all auto-generated HLS/Vivado project directories are gitignored — see [`.gitignore`](.gitignore).

---

## Hardware & Software

| Item | Detail |
|---|---|
| Board | Xilinx/AMD Zynq UltraScale+ ZCU102 (xczu9eg-ffvb1156-2-e) |
| CPU | Quad-core ARM Cortex-A53 (scalar, ≤1199.99 MHz) |
| OS | PetaLinux 2022.2 (kernel 5.15.36-xilinx-v2022.2) |
| Toolchain | Vitis HLS / Vivado 2024.2, XRT 2.14.0 |
| Power measurement | PMBus (Maxim MAX15301/MAX15303) via I2C, INA226 |

---

## Build

Each kernel is synthesized independently via its own Tcl script:

```bash
vitis_hls -f script/run_hls_classifier.tcl
vitis_hls -f script/run_hls_ffn_up.tcl
vitis_hls -f script/run_hls_ffn_down.tcl
vitis_hls -f script/run_hls.tcl        # gemv_top
```

Each produces an IP core under its respective `hls_*` output directory, integrated in Vivado (block design + AXI SmartConnect topology per the port table above) to produce the bitstream (`.xsa` / `.xclbin`).

> Adjust paths/flags above if your Tcl scripts differ — this reflects the standard Vitis HLS batch-mode flow.

### Host application

```bash
# Cross-compile for aarch64 (PetaLinux sysroot)
aarch64-linux-gnu-g++ -o host src/sw/host.cpp -lxrt_coreutil -I<xrt_include> -L<xrt_lib>
```

Deploy `host`, the compiled `.xclbin`, and the `stories15M.bin` + `tokenizer.bin` checkpoint (same format as [llama2.c](https://github.com/karpathy/llama2.c)) to the ZCU102's PetaLinux filesystem, then run:

```bash
./host stories15M.bin -z tokenizer.bin -i "Once upon a time" -n 200
```

> Confirm the exact CLI flags against `src/sw/host.cpp` — the above mirrors the CUDA companion repo's interface.

---

## Power Methodology

An early pass estimated FPGA power by summing 16 Linux `hwmon` `power1_input` nodes — this reported a **constant 2.68–2.77 W regardless of workload**, i.e. it was measuring a static idle baseline, not the design's actual power cost. Any GOPS/W computed from it (~0.50) is not trustworthy.

The measurement was replaced with direct PMBus rail sampling (12 regulator rails over I2C, 50 ms interval, SIGUSR1-bracketed active windows), run **n=8 times per condition** within a single boot session — a reboot between conditions was found to shift `VCCINT`'s idle baseline by ~8.5 A, large enough to invalidate cross-reboot comparisons. Results are aggregated to mean ± SE with a `|mean| > 2×SE` significance screen, cross-checked against physical plausibility (e.g., BRAM-rail power tracking PL activity only during FPGA runs).

**Use the PMBus, multi-trial numbers in the [Results](#results-at-a-glance) table — not any single-run or `hwmon`-based figure.**

---

## Debugging Journey

Four issues that shaped the final architecture:

**Classifier control-plane tax.** An early design tiled the 288×32,000 classifier through `gemv_top`'s existing 288×288 datapath — 112 calls/token. Measured honestly, this cost ~21 ms/token, *slower* than the 6.84 ms/token CPU-only classifier it was meant to replace: 111 of 112 calls were redundant register-write/poll/done round-trips. Fixed with a dedicated `classifier_top` streaming kernel split across 3 AXI ports, down to 7,129 µs/token.

**`ap_fixed` ternary ambiguity.** `ap_fixed`'s `operator+` returns a wider intermediate type than a bare value, so a ternary folding a pipelined accumulator's two branches is rejected by Vitis HLS as type-ambiguous. Fixed with an explicit `if`/`else`.

**`DATAFLOW` canonical-form violation.** `DATAFLOW` requires exactly one reader and one writer per top-level port; a port-split implementation calling the same load/store routine twice against one pointer fails synthesis. Fixed with a single consolidated task fanning data out (or in) internally, draining outputs in an interleaved rather than sequential order.

**Profiling code lying to itself.** Two accounting bugs were found in the *profiling* code, not the design: classifier cost silently understated by dividing by the model's 6 layers "for CSV column parity," and a total-time accumulator that double-counted the classifier call while dropping all per-layer CPU-side time. Both were caught only by cross-checking against known call counts — either would have driven real design decisions against numbers wrong by several times.

---

## Related Work

- **[llama2-cuda](https://github.com/Salik-Devv/llama2-cuda)** — companion CUDA/GPU implementation (RTX 4060 Laptop), the cross-platform throughput/efficiency reference point for this project.
- A research paper comparing all three platforms (CPU / FPGA / GPU) is in preparation.

---

## Citation / Reference

This work builds on:
- [Karpathy's llama2.c](https://github.com/karpathy/llama2.c) — original single-file C inference engine
- [LLaMA 2](https://arxiv.org/abs/2307.09288) — Touvron et al., 2023
- [HLSTransform](https://arxiv.org/abs/2405.00738) — He et al., 2024 (closest related FPGA/HLS work)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
