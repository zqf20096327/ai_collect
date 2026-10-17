# llama2.c-260k-rtl-fpga

`llama2.c-260k-rtl-fpga` is an engineering project that progressively maps the `stories260K` model from the open-source `llama2.c` project into Verilog RTL and runs token-level inference on FPGA.

This repository was developed with Codex as an engineering assistant, contributing to code organization, RTL development collaboration, simulation flow cleanup, and documentation writing.

The current mainline has completed the full 6-level development path from basic operators to the top-level UART token inference flow:

```text
Level 0  Basic operators
Level 1  Vector-level modules
Level 2  Transformer submodules
Level 3  Single Transformer layer
Level 4  5-layer forward core
Level 5  UART top-level token inference
```

## Project Goal

The goal of this project is not to build a full chat system. The goal is to make the following minimum hardware inference chain work:

```text
token_id -> FPGA forward -> next_token_id
```

Responsibility split:

```text
PC   : text encoding, tokenizer, UART interaction, output decoding
FPGA : token embedding -> Transformer forward -> classifier -> argmax
```

## Current Status

The following key results are already implemented and kept in the repository:

1. The quantized `stories260K` parameter package has been fixed into hardware-side data files.
2. Level 0 through Level 5 each have corresponding RTL, cocotb testbenches, and simulation entry scripts.
3. `token_top_uart` completes the PC <-> FPGA UART loop.
4. The final Vivado GUI project is preserved in `build/vivado/token_top_uart_final/`.
5. The target FPGA device is `XCVU9P-2FLGB2104I`.

The mainline status, architecture, and implementation notes are primarily documented in `docs/` and the top-level RTL entry points.

The current Level 5 top-level summary is:

```text
LUT        = 235,704
FF         = 142,128
BRAM Tile  = 435
DSP        = 188
WNS        = 1.799 ns
TNS        = 0
Critical path = qkv_projection_mem -> rope_core
```

## Top-Level Architecture

```text
+-------------------------------+
| PC Host                       |
| - tokenizer                   |
| - UART request/response       |
| - text decode                 |
+-------------------------------+
                |
                v
+-----------------------------------------------+
| FPGA token_top_uart_board                     |
|  +-----------------------------------------+  |
|  | token_top_uart                          |  |
|  |  +-----------------------------------+  |  |
|  |  | uart_token_bridge                 |  |  |
|  |  +-----------------------------------+  |  |
|  |  | forward_core_5layer               |  |  |
|  |  |  token embedding                  |  |  |
|  |  |  5 x transformer_layer_runtime    |  |  |
|  |  |  final rmsnorm                    |  |  |
|  |  |  classifier                       |  |  |
|  |  |  argmax                           |  |  |
|  |  +-----------------------------------+  |  |
|  +-----------------------------------------+  |
+-----------------------------------------------+
```

## Quick Start

### 1. Run the golden reference model

```powershell
python golden_reference.py --interactive --show-full --max-new-tokens 80
```

Streaming output example:

```powershell
python golden_reference.py --max-new-tokens 60 --stream
```

### 2. Run the Level 5 UART smoke simulation

```powershell
python sim\level5_token_top\run_token_top_uart.py
```

The corresponding test is:

- [tb/level5_token_top/test_token_top_uart.py](tb/level5_token_top/test_token_top_uart.py)

### 3. Open the final Vivado GUI project

The main GUI project is:

- [build/vivado/token_top_uart_final/project/token_top_uart_final.xpr](build/vivado/token_top_uart_final/project/token_top_uart_final.xpr)

The corresponding board-level top module is:

- [rtl/final_token_top/token_top_uart_board.v](rtl/final_token_top/token_top_uart_board.v)

### 4. Use the provided bitstream on the same board

If you have the same target board and matching hardware setup, you can directly use the provided bitstream instead of rebuilding the design:

- [build/vivado/token_top_uart_final/bit/token_top_uart_board.bit](build/vivado/token_top_uart_final/bit/token_top_uart_board.bit)

The target FPGA device is:

```text
XCVU9P-2FLGB2104I
```

### 5. Run the PC-side UART host

After programming the board, you can drive the Level 5 UART top from the PC side:

Interactive mode:

```powershell
python host\run_token_chat_uart.py --port COM12 --interactive --show-full
```

Single prompt example:

```powershell
python host\run_token_chat_uart.py --port COM12 --prompt "Once upon a time" --max-new-tokens 64 --show-full
```

## Repository Layout

```text
llama2.c-260k-rtl-fpga/
  rtl/                      Verilog RTL implementation
  tb/                       cocotb testbenches
  sim/                      ModelSim simulation entry scripts
  scripts/                  vector and mem generation scripts
  host/                     PC-side UART and interaction scripts
  docs/                     architecture, quantization, and development docs
  data/                     hardware parameter package and test vectors
  reference/                reference output samples
  build/vivado/token_top_uart_final/
                            final Vivado Project Mode project
```

## Key Files

Recommended reading order for the current mainline:

1. [docs/ARCHITECTURE_MAP.md](docs/ARCHITECTURE_MAP.md)
2. [rtl/level3_transformer_layer/transformer_layer.v](rtl/level3_transformer_layer/transformer_layer.v)
3. [rtl/level4_forward_core/forward_core_5layer.v](rtl/level4_forward_core/forward_core_5layer.v)
4. [rtl/level5_token_top/token_top_uart.v](rtl/level5_token_top/token_top_uart.v)
5. [rtl/final_token_top/token_top_uart_board.v](rtl/final_token_top/token_top_uart_board.v)

## Data and Model

The current fixed hardware-side parameter package is:

- `data/stories260K_q8_fixed.npz`
- `data/stories260K_q8_fixed_manifest.json`

The current golden model entry point is:

- `golden_reference.py`

## Known Boundaries

1. The current implementation is fixed to the `stories260K` model.
2. The numeric formats, parameter package, and storage layout are all specialized for this model.
3. The board-level project and XDC files are tied to the current validation platform and are not guaranteed to work on other boards without modification.
4. The repository keeps the final Vivado GUI project, but does not keep large run caches or simulation build artifacts.
5. The focus of this repository is reproducible RTL, simulation, and the final FPGA project, not a generic inference framework.
6. The provided `.bit` file is intended for the same board and matching peripheral setup used during validation.

## Related Documents

- [docs/ARCHITECTURE_MAP.md](docs/ARCHITECTURE_MAP.md)

## Upstream Reference

This project is based on the `llama2.c` project and specifically targets the `stories260K` model flow.

Upstream repository:

- https://github.com/karpathy/llama2.c
