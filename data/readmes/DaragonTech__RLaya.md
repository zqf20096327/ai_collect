# RLaya

Rust binding for **Laya**, the open typed-decision model, running in-process through the
LibLayaX library (`laya.dll` / `liblaya.so` / `liblaya.dylib`, built from
[laya.cpp](https://github.com/lkarlslund/laya.cpp)). No server, no HTTP: your program loads the
model and asks it yes/no, multiple-choice and score questions about a piece of text.

RLaya is an independent, unofficial project. It is not part of Laya or of laya.cpp.

| Path | What it is |
|---|---|
| `src/lib.rs` | The binding: the ten raw C functions (`rlaya::sys`) and the safe `Agent` type. No dependencies. |
| `build.rs` | Tells the linker where the native library is (`LAYA_LIB_DIR`). |
| `tests/rlaya.rs` | The test suite (`cargo test`). |
| `examples/ask.rs` | A small program that loads a model and asks three questions. |
| `Cargo.toml` | The crate is called `rlaya`. |
| `LICENSE` | MIT. |

This repository contains only Rust source. The native library and the model weights come from
elsewhere (see below).

## What you need

1. **The native library**, C API version 1 (LibLayaX 1.0.5 or later):

   | Your target | Library |
   |---|---|
   | Windows x64, PC with AVX2 | `laya.dll` from `laya-windows-…-avx2` |
   | Windows x64, any CPU, or x64 emulation on Windows on ARM | `laya.dll` from `laya-windows-…-compat-sse42` |
   | Windows x64 with a GPU (Vulkan) | `laya.dll` from `laya-windows-…-vulkan` |
   | Windows ARM64, native | `laya.dll` from `laya-windows-arm64-…` |
   | Linux x86-64 / ARM64 | `liblaya.so` from `laya-linux-…` |
   | macOS (Apple Silicon or Intel) | `liblaya.dylib` from `laya-macos-…` |
   
   Download the library from the [LibLayaX repository](https://github.com/DaragonTech/LibLayaX/releases/tag/v1.0.14)

2. **The model weights** (about 800 MB for the english variant), from the Hugging Face
   repository [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya). With the
   Hugging Face command-line tool:

   ```
   pip install huggingface_hub
   huggingface-cli download convaiinnovations/laya --local-dir /models/laya \
       --include "model.safetensors" "rl_agent_config.json" "encoder/*" "tokenizer/*"
   ```

   The folder you pass to `Agent::new` is the one that contains `rl_agent_config.json`. The LibLayaX
   README ("Getting the model") lists the files needed, the other ways to download them, and how
   to get the multilingual and typed-decisions variants.

3. **Rust** 1.71 or later.

## Quick start

RLaya is not published on crates.io; depend on it by path or from your own Git repository:

```toml
[dependencies]
rlaya = { path = "../RLaya" }
serde_json = "1"        # or any JSON crate, to read the answers
```

```rust
use rlaya::Agent;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Load once (a few seconds, about 1.7 GB of RAM on CPU) and keep it for the program's lifetime.
    let agent = Agent::new("/models/laya", r#"{"backend":"cpu"}"#)?;

    let json = agent.ask_yes_no(
        "Please refund the duplicate charge.",
        "Does the customer ask for a refund?",
        "refund",
    )?;
    let value: serde_json::Value = serde_json::from_str(&json)?;
    println!("P(yes) = {}", value["results"][0]["answers"]["refund"]["noul"]);

    // Choice and score questions:
    agent.ask_choice("I want to cancel my subscription.", "What does the customer want?",
                     &["cancel", "upgrade", "refund"], "intent")?;   // answers.intent.choice
    agent.ask_score("Third time I am writing!!!", "How angry is the customer?",
                    &["calm", "annoyed", "furious"], "anger")?;      // answers.anger.score

    // Anything the JSON protocol supports: several questions, several texts in one call.
    agent.predict(r#"[{"state":"...","questions":{...}}, {"state":"...","questions":{...}}]"#)?;
    Ok(())
}
```

### Finding the native library

**When building** (Linux and macOS): set `LAYA_LIB_DIR` to the folder that contains
`liblaya.so` or `liblaya.dylib`, unless it is installed in a system library directory.

    LAYA_LIB_DIR=/path/to/laya-linux/avx2 cargo build

On Windows nothing is needed at build time: the crate imports `laya.dll` directly, without an
import library.

**When running**, the program must be able to find the library:

| System | Simplest way |
|---|---|
| Windows | Put `laya.dll` next to the `.exe`. |
| Linux | Put `liblaya.so` next to the executable and add `println!("cargo:rustc-link-arg=-Wl,-rpath,$ORIGIN");` to your application's `build.rs`; or set `LD_LIBRARY_PATH`. |
| macOS | Same with `-Wl,-rpath,@executable_path`; or set `DYLD_LIBRARY_PATH`. |

On Linux and macOS the tests and examples of this crate get `LAYA_LIB_DIR` as their run-time
search path automatically, so `cargo test` and `cargo run --example ask` work with that one
variable. On Windows, put the folder that holds `laya.dll` on `PATH` for them:

    set PATH=C:\path\to\laya-windows-arm64-1.0.14;%PATH%
    cargo test

## The crate

```rust
pub struct Agent;                                   // Send + Sync, unloads the model on drop
impl Agent {
    pub fn new(model_dir: impl AsRef<Path>, options_json: &str) -> Result<Agent>;
    pub fn predict(&self, request_json: &str) -> Result<String>;     // Err on a rejected request
    pub fn try_predict(&self, request_json: &str) -> Result<String>; // returns {"error":"..."} instead
    pub fn prepare(&self, request_json: &str) -> Result<String>;     // tokenized inputs, for debugging
    pub fn info(&self) -> Result<String>;                            // backend, device, model, limits
    pub fn ask_yes_no(&self, state: &str, instructions: &str, id: &str) -> Result<String>;
    pub fn ask_choice(&self, state: &str, instructions: &str, options: &[&str], id: &str) -> Result<String>;
    pub fn ask_score(&self, state: &str, instructions: &str, levels: &[&str], id: &str) -> Result<String>;
    pub fn as_ptr(&self) -> *mut sys::laya_agent;                    // for the raw functions
}

pub fn version() -> String;          // e.g. "laya_c 1.0.14 (api 1; backends: cpu)"
pub fn api_version() -> i32;
pub fn quote(value: &str) -> String; // a JSON string literal, quotes included
pub struct Error;                    // implements std::error::Error; .message()
pub mod sys;                         // the raw extern "C" functions from laya_c.h
```

Every method returns the complete response as a JSON string:

```json
{"results":[{"model":"laya-rl-agent",
             "answers":{"refund":{"type":"noul","confidence":0.8364,"noul":0.8364,
                                  "action":{"act_probability":1.0}}},
             "usage":{"input_tokens":40,"output_tokens":0}}],
 "elapsed_ms":244.9,"backend":"CPU","device":"..."}
```

**Options** (second argument of `Agent::new`, a JSON object or `""`; unknown keys are rejected):

| Key | Values | Default |
|---|---|---|
| `backend` | `"cpu"`, `"vulkan"`, `"cuda"` (must be compiled into the library you ship) | `"cpu"` |
| `variant` | `"english"`, `"multilingual"`, `"typed-decisions"`: picks a subfolder of a model store | folder as given |
| `precision` | `"fp32"`, `"fp16"`, `"bf16"` (the half precisions need a GPU) | `"fp32"` |
| `threads` | CPU threads, 0 = all | 0 |
| `device` | GPU index, or part of its name such as `"RTX"` | first discrete GPU |
| `flash` | boolean, fused attention (GPU) | on for `fp16`/`bf16`, otherwise off |
| `tensor_core`, `allow_truncation` | booleans | off |

## Things worth knowing

* **Errors.** `Agent::new` and `predict` return `Err` (bad path, malformed JSON, unknown question
  type, text too long, a NUL character inside a string). A failed request leaves the agent usable.
* **Threads.** An `Agent` is `Send + Sync`: share it with `Arc<Agent>`. The library serializes
  calls on one agent, so for throughput send an array of requests in one `predict` rather than
  calling from many threads. In an async program, call it from `spawn_blocking`.
* **Strings.** Everything crosses the boundary as UTF-8 JSON. Model paths must be valid Unicode.
* **Memory.** About 1.7 GB per loaded model on CPU. Create one agent per model and keep it.
* **Log output.** The library writes warnings to stderr. `rlaya::sys::laya_set_log_callback`
  redirects them; there is no safe wrapper for it yet.
* **Debugging.** `LAYA_DEBUG=1` in the environment makes the library print what it is doing at
  each stage of each call.

## Running the tests

Linux and macOS:

```
LAYA_LIB_DIR=/path/to/lib cargo test                                    model-free checks
LAYA_LIB_DIR=/path/to/lib LAYA_TEST_MODEL=/path/to/model cargo test -- --nocapture     full run on the CPU
LAYA_TEST_BACKEND=vulkan ...                                            full run on another backend
LAYA_LIB_DIR=/path/to/lib cargo run --release --example ask -- /path/to/model
```

Windows (`cmd`):

```
set PATH=C:\path\to\folder-with-laya.dll;%PATH%
cargo test                                                    model-free checks
set LAYA_TEST_MODEL=C:\models\laya
cargo test -- --nocapture                                     full run on the CPU
set LAYA_TEST_BACKEND=vulkan                                  then the same on another backend
cargo run --release --example ask -- C:\models\laya
```

To build for another architecture than the machine's own, add the target and name it, for
example an x64 build on Windows on ARM (it then needs the x64 `compat-sse42` library on
`PATH`, because the emulator has no AVX):

```
rustup target add x86_64-pc-windows-msvc
cargo test --target x86_64-pc-windows-msvc -- --nocapture
```

On macOS with the GPU, add `MVK_CONFIG_LOG_LEVEL=1` to keep MoltenVK from printing about 180
lines of information, and point `LAYA_LIB_DIR` at the folder of the GPU package, which holds
`libMoltenVK.dylib` next to `liblaya.dylib`:

```
LAYA_TEST_BACKEND=vulkan MVK_CONFIG_LOG_LEVEL=1 cargo test -- --nocapture
```

`--nocapture` shows the answers the test prints. The first build downloads `serde_json`,
which only the tests and the example use.

The full run covers all three question types, JSON escaping and Unicode, error reporting,
`prepare`, a batch of two requests, and three threads sharing one agent.

## Status

Tested with LibLayaX 1.0.14 and the real english model. "Passed" means `cargo test` gives 4
passed and 0 failed plus the doc test, and the example runs.

| Target | CPU | GPU |
|---|---|---|
| Windows x64 PC (Ryzen 5 5500, RTX 3050) | passed | passed |
| macOS (Apple M3 Ultra) | passed | passed |
| Windows ARM64, native | passed | no GPU build |
| Windows x64, under emulation on ARM | passed | not run |
| Linux x86-64, Ubuntu 26.04 (Ryzen 5 5500, VMware) | passed | not run |
| Linux x86-64, Ubuntu 24.04 under WSL (Ryzen 5 5500) | passed | no GPU visible under WSL |
| Linux ARM64, Ubuntu 24.04 | passed | no GPU build |

"No GPU build" means LibLayaX has no GPU library for that platform; "not run" means there is
one and it has not been tried from Rust. Under WSL the GPU was tried: Vulkan there offered no
GPU, so the library reported `No usable Vulkan GPU found` and the CPU backend was used. That
is a property of WSL, not a failure of the library; the same machine's GPU passes from
Windows.

### The runs in detail

| Rust | Target | Backend | Model | Result |
|---|---|---|---|---|
| 1.99.0 | macOS on Apple Silicon (`aarch64-apple-darwin`), Apple M3 Ultra | CPU | real english model | passed, `noul` 0.8364 |
| 1.99.0 | macOS on Apple Silicon, Apple M3 Ultra | GPU (`vulkan`) | real english model | passed, `noul` 0.8366 |
| stable | Windows x64 PC (`x86_64-pc-windows-msvc`), AMD Ryzen 5 5500 | CPU | real english model | passed, `noul` 0.8364 |
| stable | Windows x64 PC, NVIDIA GeForce RTX 3050 | GPU (`vulkan`) | real english model | passed, `noul` 0.8364 |
| 1.91.1 | Windows 11 on ARM, native (`aarch64-pc-windows-msvc`) | CPU | real english model | passed, `noul` 0.8364 |
| 1.91.1 | Windows x64 (`x86_64-pc-windows-msvc`), built and run on Windows 11 on ARM under x64 emulation, with the `compat-sse42` library | CPU | real english model | passed, `noul` 0.8364 |
| stable, from rustup | Linux ARM64 (`aarch64-unknown-linux-gnu`), Ubuntu 24.04 | CPU | real english model | passed, `noul` 0.8364 |
| stable | Linux x86-64 (`x86_64-unknown-linux-gnu`), Ubuntu 26.04 LTS in a VMware virtual machine on an AMD Ryzen 5 5500, with the `compat-sse42` library | CPU | real english model | passed, `noul` 0.8364 |
| stable | Linux x86-64, Ubuntu 24.04.5 LTS under WSL on Windows, AMD Ryzen 5 5500, with the `vulkan` library on its CPU backend | CPU | real english model | passed, `noul` 0.8364 |
| 1.95 | Linux x86-64, the build machine | CPU | synthetic test model | passed; `cargo clippy` is clean |

The runs on the AMD Ryzen 5 5500 machine (Windows x64 on the CPU and on the RTX 3050, Ubuntu
26.04 x86-64 under VMware, and Ubuntu 24.04 under WSL) were carried out by **Roberto Marc** of
**Syhunt**. The other runs with
the real model were carried out by Felipe Daragon.

* **Windows works without an import library.** The crate imports `laya.dll` directly
  (`raw-dylib`); it built and linked for ARM64 and for x64 with no changes.
* **macOS needed one fix**, in `build.rs`: the unit-test program of the library did not get
  the library's folder as a run-time search path and failed to start. Linux hid the problem
  because its linker drops a library that a program does not call. Fixed and confirmed on
  the M3 Ultra.
* **The GPU runs through RLaya** on two machines, at full precision: an Apple M3 Ultra and an
  NVIDIA GeForce RTX 3050. The example answered its last question in 36 ms on the M3 Ultra's
  GPU (77 ms on its CPU) and in 68 ms on the RTX 3050. The first questions after loading are
  slower while the GPU warms up: 1414 ms, 660 ms and then 47 ms on the RTX 3050. The half
  precisions (`fp16`, `bf16`) have not been run from Rust.
* **Every platform has run with the real model.** On Linux x86-64 that was with the
  `compat-sse42` library (about 500 to 870 ms per question in a VMware virtual machine) and
  with the `vulkan` library on its CPU backend (about 300 ms per question under WSL, on the
  same processor). The Linux GPU backend itself has not been run on a GPU: the only attempt
  was under WSL, which exposes no GPU to Vulkan, and the library answered with a clean error.
* The multilingual and typed-decisions variants have not been run.
* 1.71 is the declared minimum Rust because that is where `raw-dylib` became stable; the
  oldest version actually tried is 1.91.1.
* Not published on crates.io. The name `rlaya` was free there when this was written; `laya` is
  taken by an unrelated HTTP client for the Laya server.

## Credits

* **[Laya](https://github.com/NandhaKishorM/laya)** by NandhaKishorM is the original project:
  the model, the typed-decision primitives (`choice`, `score`, `noul`) and the Python
  reference implementation on PyTorch and Transformers. Apache-2.0. The weights are published
  on Hugging Face under `convaiinnovations`.
* **[laya.cpp](https://github.com/lkarlslund/laya.cpp)** by Lars Karlslund is the native C++
  port of Laya inference, built on ggml, with CPU, CUDA, Vulkan and Core ML backends. MIT.
  The native library RLaya loads is built from it.
* **RLaya** and the LibLayaX library underneath it were written by Claude (Anthropic), under
  the direction of **Felipe Daragon** of **DaragonTech**, who set the goals, guided the work
  and ran the tests on Windows on ARM, macOS and Linux ARM64.
* **Roberto Marc** of **Syhunt** tested RLaya on a Windows x64 PC, on the CPU and on an
  NVIDIA GeForce RTX 3050, on Ubuntu 26.04 x86-64 and on Ubuntu 24.04 under WSL. Those were
  the first runs on an x64 PC, on an AMD processor and on Linux x86-64 with the real model.

## License

RLaya is released under the MIT License; see [LICENSE](LICENSE).

It contains no code from the projects it builds on. Those keep their own terms: the LibLayaX
library and laya.cpp are MIT, Laya is Apache-2.0, and the model weights are published on
Hugging Face under their own terms.
