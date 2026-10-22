# revenant

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/tag/DatanoiseTV/revenant?sort=semver&label=release)](https://github.com/DatanoiseTV/revenant/releases)
[![Container image](https://img.shields.io/badge/ghcr.io-revenant-2496ED?logo=docker&logoColor=white)](https://github.com/DatanoiseTV/revenant/pkgs/container/revenant)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](pyproject.toml)

**Resurrect abandoned hardware and software.** revenant is an LLM-powered,
automated reverse-engineering engine for firmware and binaries that vendors no
longer support. Point it at a firmware image or a compiled program and it
identifies the target, reconstructs its structure, and produces the artifacts
you need to keep the device alive: a pin map, a device tree, a peripheral
inventory, a buildable custom-firmware project, recovered function names, and —
optionally — a clean-room open-source reimplementation.

Runs entirely in Docker. Mount your working folder and go.

<p align="center">
  <img src="docs/img/demo.gif" alt="revenant live TUI — stage-DAG pipeline animating, progress bar, rolling log" width="820">
  <br>
  <sub>Live TUI (scales to your terminal): the stage DAG runs on the left while
  results fill in on the right — SoC, peripherals, external components (sensors,
  port expanders, rotary encoders, displays, LED strips, audio DACs) and the pin
  map. Timings are from a real claude-code run (agentic identification ~96 s / 11
  turns over radare2 MCP; full pipeline ~3 min); GIF playback is accelerated. The
  on-screen data is an illustrative synthetic target, not a real device.</sub>
</p>

---

## Legal and ethical use — read this first

revenant is built for **lawful, authorized** reverse engineering:

- **Repair and preservation** of hardware whose vendor has abandoned it.
- **Interoperability** — making your own devices work together.
- **Security research** on systems you own or are authorized to test.
- **Education** and archival of computing history.

These are protected or permitted activities in many jurisdictions (for example,
interoperability and repair exemptions). They are also the *only* use this
project is for.

**Do not use revenant to:**

- Infringe copyright or misappropriate trade secrets. revenant reconstructs
  *behavior and interfaces* for interoperability; it is not a tool for copying
  proprietary code or assets.
- Circumvent technical protection measures, license enforcement, or access
  controls where doing so is unlawful in your jurisdiction.
- Analyze firmware, binaries, or devices you do not own and are not authorized
  to examine.

You are responsible for ensuring your use complies with the laws and contracts
that apply to you. Reverse engineering law varies by country and by contract
(EULAs, DMCA §1201 and its exemptions, the EU Software Directive, etc.). When in
doubt, get legal advice. The authors provide this software "as is", for research
and educational purposes, with no warranty — see [LICENSE](LICENSE).

Reconstructions are **best-effort inferences from static analysis**. Verify
every result against the real hardware and authoritative documentation before
relying on it.

---

## What it does

revenant runs a parallel, cached analysis pipeline and routes work down one of
two tracks depending on what you give it.

**Hardware firmware** (MCU images, embedded Linux):
- Identify the SoC/MCU, CPU core, architecture and endianness.
- Inventory peripherals (UART, I2C, SPI, GPIO, timers, ADC, USB, …) from
  memory-mapped register accesses, symbols and strings.
- Reconstruct a **pin map** in the SoC's native naming (PA9, GPIO17, IO0, …).
- Emit a **device tree source** (`.dts`) skeleton.
- Generate a **complete, buildable custom-firmware project** (ESP-IDF, Arduino,
  Zephyr, STM32, bare-metal, …) — with a provider, the LLM writes real
  register-level init for the exact part: RCC clock enables, GPIO
  alternate-function config matching the recovered pins, peripheral init, startup
  + vector table, a linker script, and a Makefile. In a controlled STM32F4 test
  the generated project compiled cleanly with `arm-none-eabi-gcc` to a flashable
  image. Falls back to a deterministic skeleton without an LLM.
- Recommend the **safest flashing path first** — a non-bricking route (USB DFU /
  ROM bootloader) where the part has one, with SWD/JTAG as the fallback.

**Software** (native ELF/PE/Mach-O, or bytecode — `.pyc`/JVM/`.jar`/wasm):
- Identify language, runtime, frameworks and build system.
- Break the program into logical components and reconstruct their behavior
  (inputs, outputs, side effects, data formats/protocols).

**Both tracks:**
- **Determine file types and find compression** — libmagic identification plus a
  full binwalk signature scan that locates compressed blobs and embedded
  filesystems at every offset, then recursively extracts them.
- **Ghidra decompilation** (`--decompile`, and implied by `--reimplement` /
  `--cross-validate`) — its decompiler produces far more readable C than
  radare2, feeding better behavior reconstruction, naming, and rewrites.
- **Recover meaningful function names** for stripped binaries and emit a
  radare2 script to apply them.
- **Adversarial cross-validation** (on by default; `--no-verify` to disable):
  an independent pass tries to *refute* each claim and recalibrates confidence,
  so weak or hallucinated findings get flagged instead of shipped.
- **Capability detection** (`--capabilities`, or `--deep`): Mandiant capa
  identifies what a binary can do (network, crypto, anti-analysis, persistence).
- Optional **1:1 open-source reimplementation** (`--reimplement`).
- A human-readable `report.md`, a machine-readable `report.json`, and Mermaid
  graphs of the architecture and the pipeline.

## Quickstart (Docker)

```bash
git clone https://github.com/DatanoiseTV/revenant.git
cd revenant

# First run builds the image automatically (radare2-based; fast).
./revenant.sh analyze firmware.bin
```

`revenant.sh` mounts your current directory at `/work`, so it reads
`firmware.bin` from your folder and writes the `revenant-out/` workspace back
into it. The host only needs Docker.

```bash
# Software binary, with a reimplementation attempt:
./revenant.sh analyze ./app --mode software --reimplement

# Give it a hint when you already know the part:
./revenant.sh analyze fw.bin --soc STM32F405RG --load-addr 0x08000000

# Large/complex binary: faster shallow analysis (verify runs by default):
./revenant.sh analyze big.elf --fast
# Thorough pass (Ghidra decompile + capa capabilities + SBOM/CVE):
./revenant.sh analyze app.elf --mode software --deep

# What tools/providers are available:
./revenant.sh doctor
```

### Try it on public binaries

revenant ships with no binaries — point it at one you have the right to analyze.
To see it run without touching anything proprietary, use openly-licensed,
freely-redistributable targets:

```bash
# Iconic old software, software track — MS-DOS (MIT, open-sourced by Microsoft).
# Pick any .COM/.EXE in the clone; the path layout depends on the version dir.
git clone --depth 1 https://github.com/microsoft/MS-DOS.git
./revenant.sh analyze MS-DOS/v2.0/bin/COMMAND.COM --mode software

# Open-source MCU firmware, firmware track — e.g. GRBL, Marlin, Betaflight,
# QMK (all GPL, distributed as prebuilt images). Convert Intel HEX to raw if
# needed, then analyze. Because the source is public, you can check the
# reconstruction against it.
objcopy -I ihex -O binary firmware.hex firmware.bin
./revenant.sh analyze firmware.bin
```

Analyze your own firmware exactly the same way. Do not point revenant at images
you are not authorized to examine — see the legal note above.

### Prebuilt image (GHCR)

CI publishes the image to GitHub Container Registry on every push to `main` and
every release tag:

```bash
docker pull ghcr.io/datanoisetv/revenant:latest
REVENANT_IMAGE=ghcr.io/datanoisetv/revenant:latest ./revenant.sh analyze firmware.bin
```

The published image is built for **linux/amd64** (CI runners). On Apple Silicon,
`revenant.sh`'s local build is native arm64 and faster than the amd64 image under
emulation. No credentials are baked into the image — provider auth is supplied at
runtime by `revenant.sh` from your existing login, never stored in the image or
the repository.

## LLM providers

The semantic stages (identification, pin map, behavior, naming, verification,
reimplementation) use a pluggable LLM backend. The deterministic stages
(triage, extraction, disassembly, device tree, templates) run without one.

| Provider | Flag | Notes |
|---|---|---|
| Claude Code (default) | `--provider claude-code` | Agentic: drives radare2 over MCP in an adaptive loop. Auth via a mounted `~/.claude` or `ANTHROPIC_API_KEY`. |
| OpenAI | `--provider openai` | Set `OPENAI_API_KEY`. |
| LM Studio (local) | `--provider lmstudio` | Local OpenAI-compatible server. From Docker: `REVENANT_BASE_URL=http://host.docker.internal:1234/v1`. |
| none | `--provider none` | Deterministic stages only (no identification/pinmap). |

With no provider, the deterministic stages still produce a real report:
architecture/endianness, extraction tree, function/string/import inventory, and
MMIO base-address candidates for firmware.

## Output

Everything lands in `revenant-out/` (configurable with `-o`):

```
revenant-out/
├── report.md                     # human-readable report
├── report.json                   # machine-readable report
├── artifacts/disasm.txt          # radare2 analysis dump
└── reconstruction/
    ├── peripherals.json          # inferred peripherals (firmware)
    ├── pinmap.json / pinmap.md    # reconstructed pin map (firmware)
    ├── devicetree.dts             # device tree skeleton (firmware)
    ├── firmware-template/         # complete buildable firmware project (firmware)
    ├── software-profile.json      # language/components (software)
    ├── behavior.md                # reconstructed behavior (software)
    ├── function-names.json        # recovered names
    ├── rename.r2                  # apply with: r2 -i rename.r2 <binary>
    ├── verification.json          # cross-validation verdicts
    └── graphs/                    # architecture.mmd, pipeline.mmd (Mermaid)
```

## How it works

A dependency-aware DAG engine runs every ready stage concurrently and caches
each stage's output by a content hash of its inputs, so re-runs are instant and
only changed work re-executes.

```
recon → triage → extract → disasm → semantic → decompile ─┬─ naming
   (file type +                       (Ghidra, when needed) ├─ (firmware) pinmap → devicetree → firmware_template
    compression scan)                                       ├─ (software) behavior
                                                            ├─ verify        (--cross-validate)
                                                            └─ reimplement   (--reimplement)
                                                                      └────────── report
```

Identification runs on the **completion path** by default: precomputed radare2
features (imports, strings, MMIO bases, disassembly excerpt) plus a researched
peripheral-address reference are handed to the model in a single call. It is
fast and works with any backend, local models included. Pass `--agentic` to let
`claude-code` instead drive radare2 itself through the
[radare2 MCP server](https://github.com/radareorg/radare2-mcp) in an iterative
loop — more thorough on hard targets, but slower, so it is opt-in and wall-clock
bounded.

Before the model runs, a pure-Python pass locates every code image in the file —
scanning for ARM Cortex-M vector tables at any offset and for i.MX RT FlexSPI
boot images (FCFB + IVT) — so **non-standard containers and multi-processor
update files are split and identified automatically** (e.g. a control MCU plus a
DSP in one blob). Observed MMIO base addresses are matched against a database of
known parts (STM32, i.MX RT / Teensy, RP2040, nRF, Kinetis, SAMD, and boards like
the Daisy Seed) to name the SoC and its peripherals — even when the LLM is
unavailable.

## Live TUI

Install the `tui` extra (bundled in the Docker image) for a live view — a
stage-DAG tree with per-stage status and timings, an animated progress bar, a
rolling log panel, and a final summary with peripheral/pin/component tables. It
is built on [rich](https://github.com/Textualize/rich) (`Tree`/`Table`/`Panel`/
`ProgressBar`/`Live`), so layout and Unicode cell widths are computed correctly
— no hand-aligned ASCII. It auto-enables on a terminal; use `--no-tui` for plain
logs (the default in CI/headless runs).

<p align="center">
  <img src="docs/img/tui-summary.png" alt="revenant result summary — identified SoC, peripherals, and reconstructed pin map" width="700">
</p>

_(Illustrative synthetic target: an STM32F4 environmental controller — identified
SoC, peripherals at their real MMIO bases, external components on the I2C bus, and
a pin map with correct alternate functions.)_

## Tooling

The image bundles a current (2026) reverse-engineering toolset; the engine uses
them directly and the agentic backend can drive any of them:

- **Disassembly / decompilation:** radare2 (built from source, incl. arm64),
  Ghidra (native decompiler built for the image's arch).
- **Extraction:** unblob (preferred recursive extractor) and binwalk, with
  jefferson / ubi-reader / squashfs-tools / 7-zip for nested filesystems.
- **Identification:** `file`/libmagic, LIEF (PE/Mach-O/ELF parsing), yara.
- **Binary analysis libs:** capstone, unicorn, pyelftools, and — for symbolic
  execution and emulation — angr, qiling, capa.
- **Dynamic analysis:** QEMU user-mode (`--emulate`).
- **Supply chain:** Syft (SBOM) + Grype / cve-bin-tool for known-CVE scanning
  (`--sbom`).

Run `revenant doctor` to see exactly what is available in your environment.
Heavy tools (angr/qiling/capa/SBOM) can be dropped with
`--build-arg INSTALL_HEAVY=false` for a smaller image.

## Running locally (without Docker)

The engine is stdlib-only, so it installs instantly; the external tools
(radare2, binwalk, optionally Ghidra) must be on your PATH.

```bash
pip install -e ".[all]"      # rich TUI + r2pipe + PyYAML
revenant analyze firmware.bin
revenant doctor              # check tool/provider availability
```

## CLI reference

```
revenant analyze <firmware> [options]

  -o, --out DIR           output workspace (default: revenant-out)
      --mode MODE         auto | firmware | software   (track selection)
      --provider P        claude-code | openai | lmstudio | none
      --model M           model id for the provider
      --agentic           opt into MCP-driven agentic identification (slower; default is completion)
      --no-agentic        force the completion path (this is the default)
      --toolchain T       firmware template: esp-idf|arduino|zephyr|stm32-hal|bare-metal|linux
      --arch / --soc / --load-addr   detection hints
      --only / --skip STAGE...       run/skip specific stages
      --deep              thorough: enable decompile + capabilities + sbom
      --no-verify         disable the default adversarial cross-validation pass
      --decompile         run Ghidra headless decompilation (better C for the LLM)
      --capabilities      capa capability detection (network/crypto/anti-analysis)
      --emulate           run a target Linux ELF under user-mode QEMU (executes it)
      --sbom              software bill of materials + known-CVE scan (syft/grype)
      --reimplement       also produce a 1:1 open-source reimplementation
      --fast              shallower (faster) radare2 analysis for large binaries
  -j, --concurrency N     max parallel stages (default 6)
      --no-cache          ignore the stage cache
      --tui / --no-tui    force/disable the live TUI

revenant doctor           report tool + provider availability
revenant init             write a sample revenant.yaml config
```

## Status and limitations

- Identifications and reconstructions are **best-effort static inferences**. The
  confidence scores and the default adversarial verify pass help catch weak
  findings, but verify against the real hardware and authoritative docs.
- The reimplementation stage is agentic and bounded — treat its output as a
  scaffold, not a finished port.
- Ghidra ships in the default image; build a smaller radare2-only image with
  `--build-arg INSTALL_GHIDRA=false`.
- ELF is parsed natively; Mach-O/PE headers are identified via radare2/LIEF.

## Contributing

Issues and pull requests are welcome. The engine is stdlib-first — no required
runtime dependencies — and the external tools are optional and discovered at
runtime, so the test suite is pure-logic and needs neither tools nor network:

```bash
pip install -e ".[all]"
pytest -q
```

Release history is in [CHANGELOG.md](CHANGELOG.md). When reporting a result that
looks wrong, attach `report.json` and the firmware's size and SHA-256 — not the
firmware itself, unless you have the right to share it.

## License

[Apache-2.0](LICENSE). Use it for repair, preservation, interoperability,
security research, and education — see the disclaimer above.
