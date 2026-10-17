# coral-rs

**A pure-Rust driver and inference runtime for the Google Coral USB Accelerator (Edge TPU).**

[![crates.io](https://img.shields.io/crates/v/coral-usb.svg?label=coral-usb)](https://crates.io/crates/coral-usb)
[![crates.io](https://img.shields.io/crates/v/coral-model.svg?label=coral-model)](https://crates.io/crates/coral-model)
[![CI](https://github.com/theohmwoa/coral-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/theohmwoa/coral-rs/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)

Run compiled Edge TPU models with **no C or C++ in your process**: no `libedgetpu`, no
TensorFlow Lite runtime, no kernel driver. From USB enumeration to a classified image,
every instruction executed on the host is Rust, built on the pure-Rust
[`nusb`](https://github.com/kevinmehall/nusb) USB stack.

```text
$ cargo run --release -p coral-usb --example infer -- mobilenet_edgetpu.tflite parrot.jpg labels.txt
chip brought up
input 150528 bytes, output 1008 bytes
first inference (incl. parameter caching): 17.6ms
second inference: 6.8ms
top 5:
  macaw: 255
  ...
```

Verified bit-identical against the official `libedgetpu` stack on the same device and
image — at **6.8 ms** steady-state per inference vs the official stack's 12.1 ms
(USB 3, mobilenet v1).

## Why

Google has effectively abandoned the Coral software stack: `pycoral` is stuck on old
Python versions, the kernel driver breaks on new kernels, and the community lives on
third-party rebuilds of an unmaintained C++ codebase. The only prior Rust binding
([edgetpu-rs](https://github.com/ionosnetworks/edgetpu-rs)) wrapped that C++ and was
archived in 2024.

The USB Accelerator needs no kernel driver — the entire protocol is userspace USB.
That makes a from-scratch memory-safe implementation practical: this project ports the
runtime logic of [google-coral/libedgetpu](https://github.com/google-coral/libedgetpu)
(Apache-2.0, used as the reference specification) to Rust.

## What works today

| Capability | Status |
| --- | --- |
| DFU firmware flash (bootloader `1a6e:089a` → runtime `18d1:9302`) | ✅ hardware-verified |
| CSR register access (vendor control transfers) | ✅ hardware-verified |
| Chip bring-up (reset/clock sequencing, feed setup, run control) | ✅ hardware-verified |
| Compiled-model parsing (DarwiNN package out of `*_edgetpu.tflite`) | ✅ verified vs known model shapes |
| Instruction linking (bit-level base-address relocation) | ✅ hardware-verified |
| Single-EP ML transport (tagged bulk streams, completion events) | ✅ hardware-verified |
| End-to-end inference with parameter caching | ✅ hardware-verified, output bit-identical to libedgetpu |
| Multi-chunk instruction models (e.g. mobilenet v2) | ✅ hardware-verified, output identical to libedgetpu |
| Object detection (SSD mobilenet v2), boxes + labels | ✅ hardware-verified: `coral_model::ssd` decodes boxes + per-class NMS, matching the official stack (bird 97.3%, cat 95.7%) |
| M.2 / PCIe Coral devices | ❌ out of scope for now (different transport) |

Everything marked hardware-verified was exercised on a physical USB Accelerator on a
5 Gbps link, with the official stack run side-by-side as the oracle.

## Quick start

**1. Permissions (Linux).** The device nodes are root-owned by default; install the
bundled udev rule once to grant your user access:

```sh
sudo cp udev/99-coral.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

then replug the device. On NixOS, put the contents of
[`udev/99-coral.rules`](udev/99-coral.rules) in `services.udev.extraRules` instead.
The rule uses `TAG+="uaccess"` (access for the locally seated user) plus group
read/write; tighten or loosen to taste.

**2. Flash the firmware.** The Edge TPU firmware is RAM-resident — the device forgets it
on every unplug and re-enumerates as a DFU bootloader. Flashing takes well under a second
(the firmware blob ships in this repo):

```sh
cargo run --release -p coral-usb --example flash
```

**3. Run an inference.** Grab a compiled model and test data from
[google-coral/test_data](https://github.com/google-coral/test_data):

```sh
curl -LO https://raw.githubusercontent.com/google-coral/test_data/master/mobilenet_v1_1.0_224_quant_edgetpu.tflite
curl -LO https://raw.githubusercontent.com/google-coral/test_data/master/parrot.jpg
curl -LO https://raw.githubusercontent.com/google-coral/test_data/master/imagenet_labels.txt

cargo run --release -p coral-usb --example infer -- \
    mobilenet_v1_1.0_224_quant_edgetpu.tflite parrot.jpg imagenet_labels.txt
```

## Library usage

```rust
let accelerator = coral_usb::Accelerator::open()?; // discovers, flashes if needed, brings up
let model = coral_model::EdgeTpuModel::parse(&std::fs::read("model_edgetpu.tflite")?)?;
let mut runner = accelerator.load(&model)?;

let output = runner.invoke(&input_bytes)?;        // one concatenated buffer, or:
let tensors = runner.invoke_named(&input_bytes)?; // per-layer named tensors with dims
```

`Accelerator::open` handles discovery, firmware flashing (the RAM firmware is lost on
every power cycle), and chip bring-up. Loading a model links its instruction streams;
the parameter-caching executable runs once before the first inference, then each
`invoke` replays the model's deterministic DMA program.

### Object detection (SSD)

SSD detection models leave box decoding and non-maximum suppression to the CPU (the TPU
emits raw box encodings and per-class scores). `coral_model::ssd` reads the anchors,
scale factors, thresholds, and output quantization straight from the model file and turns
the two raw tensors into labeled boxes:

```rust
let ssd = coral_model::ssd::SsdPostProcessor::from_model(&model_bytes)?.expect("an SSD model");
let outputs = runner.invoke_named(&input_bytes)?;
let boxes  = outputs.iter().find(|t| t.name == ssd.box_tensor).unwrap();
let scores = outputs.iter().find(|t| t.name == ssd.score_tensor).unwrap();
for d in ssd.decode(&boxes.bytes, &scores.bytes, 0.3) {
    println!("class {} @ {:.0}% {:?}", d.class_id, d.score * 100.0, d.bbox);
}
```

See the `detect` example. Verified against the official stack: `bird 97.3%` /
`cat 95.7%` on the Coral test images, boxes matching to within `u8` quantization.

## Architecture

```text
┌─────────────────────────────────────────────────────────┐
│ your application                                        │
├─────────────────────────────────────────────────────────┤
│ coral-model    parse *_edgetpu.tflite → DarwiNN package │
│                (instruction streams, parameters, I/O    │
│                layout, DMA hints, relocations)          │
├─────────────────────────────────────────────────────────┤
│ coral-usb      DFU flash · CSR bring-up · instruction   │
│                linker · tagged bulk ML transport ·      │
│                hint-driven run loop                     │
├─────────────────────────────────────────────────────────┤
│ nusb           pure-Rust userspace USB                  │
├─────────────────────────────────────────────────────────┤
│ Linux xhci / usbfs          Coral USB Accelerator       │
└─────────────────────────────────────────────────────────┘
```

| Crate | Purpose |
| --- | --- |
| [`coral-usb`](crates/coral-usb) | The driver: device discovery, DFU firmware download, chip bring-up over CSR registers, ML transport, model runner |
| [`coral-model`](crates/coral-model) | Model parsing: extracts the DarwiNN executable package from the `edgetpu-custom-op` inside a compiled `.tflite` (no TFLite runtime involved) |
| [`edgetpu-sys`](crates/edgetpu-sys) / [`edgetpu`](crates/edgetpu) | Optional FFI bindings to the C `libedgetpu` + TFLite C API, kept as a cross-checking oracle — hardware-verified against real library builds |

The only components that remain non-Rust are outside the runtime by nature: Google's
closed-source offline `edgetpu_compiler` (produces the `*_edgetpu.tflite` you feed in)
and the TPU silicon itself.

## Troubleshooting

- **`permission denied`** — install the udev rule above and replug.
- **Device shows as `1a6e:089a` / "no runtime device"** — it's in bootloader mode; this
  is normal after every unplug or power cycle. `RuntimeDevice::open_or_flash()` (used by
  the `infer` example) flashes it automatically; the `flash` example does it explicitly.
- **Every output read fails with `endpoint stalled`** — check your link speed
  (`lsusb -t`). On a degraded link (e.g. a flaky hub negotiating 12 Mbps USB 1.1) the
  device's 512-byte bulk endpoints cannot function and *all* stacks fail this way,
  including the official one. Plug the Accelerator directly into a USB 3 port.
- **Inference wedged / weird state** — unplug/replug (or the `detach` example) and
  re-flash; the RAM firmware restarts clean.

## Roadmap

Tracked in [issues](https://github.com/theohmwoa/coral-rs/issues): verifying the
stage-1 FFI oracle ([#4](https://github.com/theohmwoa/coral-rs/issues/4)), broader model
coverage (detection models, co-compiled workloads), and broader
device support.

## Development

```sh
# Unit tests, no hardware needed. Exclude the FFI oracle crates — they need
# libedgetpu + the TFLite C API present to link:
cargo test -p coral-usb -p coral-model
cargo clippy --workspace --all-targets --exclude edgetpu-sys --exclude edgetpu
```

A device runs one `ModelRunner` at a time: the bulk endpoints are claimed
exclusively, so switch models by dropping one runner before loading the next
(the device stays up). If an inference fails on a transport error the runner is
poisoned — drop it and build a new one.

Hardware-facing examples in `crates/coral-usb/examples/`: `flash`, `infer` (classification),
`detect` (SSD object detection), `bringup`, `read_chip`, `hibcheck` (error/status registers),
`detach` (runtime → bootloader).

To build the optional FFI oracle crates, point the build at real libraries
(`libedgetpu` is in nixpkgs; the TFLite C API builds with
`cmake tensorflow/lite/c` from a TensorFlow checkout — use cmake 3.x):

```sh
EDGETPU_LIB_DIR=/path/to/libs TFLITE_C_LIB_DIR=/path/to/libs     cargo run -p edgetpu --example classify -- model_edgetpu.tflite
```

The reference implementation is
[google-coral/libedgetpu](https://github.com/google-coral/libedgetpu); porting notes and
protocol details live in the commit history, which is written to be read.

## License

Apache-2.0. This project embeds the Edge TPU firmware blob and ports driver logic from
[google-coral/libedgetpu](https://github.com/google-coral/libedgetpu), Copyright 2019
Google LLC, Apache-2.0. Flatbuffer schemas are vendored from libedgetpu and TensorFlow
(Apache-2.0).

Not affiliated with or endorsed by Google. "Coral" and "Edge TPU" are trademarks of
Google LLC.
