<p align="center"><img src="docs/logo.png" width="560" alt="TensorLens"></p>

# TensorLens

**ML models and the runtimes that run them, inside the binary, in IDA.**

On-device machine learning is now in ordinary apps: face and object detection, keyboards, voice,
document scanners. A reverse engineer who opens one of these libraries meets two things IDA knows
nothing about:

1. **The model**: a TFLite flatbuffer or ONNX protobuf, embedded in `.rodata`, compressed inside a
   gzip/tar blob, or shipped in the APK next to the library.
2. **The runtime**: hundreds of anonymous functions (TFLite's kernels), reached only through function
   pointer tables, in a library that is usually stripped.

TensorLens handles both, and connects them.

| | |
|---|---|
| **Find models** | TFLite, ONNX, ncnn and ExecuTorch, embedded anywhere in the database or the input file, also inside gzip streams and tar archives (Rust apps embed them this way). Each is validated structurally, not just by magic bytes. |
| **Read models** | Operators, tensors, shapes, data types, quantisation, weights, custom ops, metadata, signatures, and the code that references the model. |
| **Graph view** | The model graph as an IDA graph. Hover for tensor details; double-click an operator to jump to the kernel that executes it. |
| **Recover the TFLite runtime** | Names every kernel's `Init`/`Free`/`Prepare`/`Eval` and its `TfLiteRegistration`, in stripped builds, and applies the TFLite C types (`TfLiteContext`, `TfLiteNode`, `TfLiteTensor`, ...) so pseudocode reads as `node->inputs->data[0]`. |
| **Connect them** | Each kernel's comment lists the model nodes it runs; each graph node links to its kernel; the report lists operators a model needs that the binary does not implement (they run in a delegate, or come from a custom op). |
| **Report** | HTML and JSON: models, load sites, kernels with evidence, delegates (NNAPI, GPU, XNNPACK, Hexagon), custom ops. |
| **Command-line scanner** | `tensorlens-scan` finds models in files, APKs, AARs and wheels, without IDA. |

**The model graph**, from the object detector in the Lespas photo app's APK, opened over the app's stripped
`libtensorflowlite_jni.so`. Every operator shows its output tensor and links to the kernel that runs it; the
custom op (native code outside the stock runtime) is red.

![Model graph in IDA](docs/img/graph.png)

**The kernels**, recovered from the same stripped library by decoding its op resolver, which needs neither
symbols nor strings. Kernels that run the loaded model are green and sorted first.

![TFLite kernels](docs/img/kernels.png)

**What a kernel looks like afterwards**: named, typed, with the evidence and the model nodes it runs.

![A recovered kernel](docs/img/disasm.png)

## Try it in two minutes

Everything below uses a public, open-source app, so there is nothing to build and no sample to ask for.

1. Install the plugin (see [Install](#install)).
2. Download the Lespas photo app from F-Droid: [site.leos.apps.lespas_120.apk](https://f-droid.org/repo/site.leos.apps.lespas_120.apk)
   (or the current version from its [F-Droid page](https://f-droid.org/packages/site.leos.apps.lespas/)). An APK
   is a zip: extract `lib/x86_64/libtensorflowlite_jni.so` from it.
3. Open that `.so` in IDA and press **`Ctrl+Alt+M`**. TensorLens waits for auto-analysis, then fills the
   **TFLite kernels** window: 177 kernels (172 from the op resolver, 5 of TFLite's bundled custom ops), 472
   functions named, no symbols needed.
4. **File > Load file > TensorLens: add models from a file, APK or AAR** and pick the APK itself. The
   **models** window now lists the app's object detector (64 operators, one custom op). Press `Enter` on it to
   open its graph, then double-click any operator to land in the kernel that runs it. Every operator links to
   code, including the custom op.

No app at hand? The official TFLite runtime works too:
[tensorflow-lite-2.16.1.aar](https://repo1.maven.org/maven2/org/tensorflow/tensorflow-lite/2.16.1/tensorflow-lite-2.16.1.aar)
from Maven Central is a zip; open its `jni/x86_64/libtensorflowlite_jni.so` (172 kernels recovered, 455 functions
named).

## Why it matters

- **Security review of AI features.** Which models does this app ship, what can they see, and which native
  code processes the input? Custom ops (`AddCustom("...")`) are native code in the model's data path and
  deserve a look; TensorLens lists them and colours them.
- **Model extraction and integrity.** Find the model, export it to a standalone `.tflite`/`.onnx` for Netron,
  and see where the app loads it from (code that references it, or a gzip blob that is unpacked first).
- **Runtime triage.** In a stripped `libtensorflowlite_jni.so` the ~440 kernel functions are anonymous.
  TensorLens names them from the runtime's own op resolver, so the interesting code (the app's own code,
  or a patched kernel) stands out from the stock runtime.
- **Vulnerability research.** TFLite kernels parse attacker-supplied tensors when a model or its input is
  untrusted. Typed, named kernels make that code readable.

## Results on real binaries

Measured with the headless runner (`tools/ida_suite.ps1`) on IDA Free 9.5, x86_64 builds, across four runtime
releases (TFLite 2.14, 2.16.1, LiteRT 2.4 and the versions the apps bundle). Every number below comes from a
run's `report.json`; nothing is hand-edited.

| Sample | Binary | What it is | Kernels found | Resolver calls decoded | Functions named |
|---|---|---|---|---|---|
| `tflite-runtime-2.14` | `_pywrap_tensorflow_interpreter_wrapper.so` | tflite-runtime 2.14 (with symbols) | 222 | 157 + 147 (two resolvers) | 0 (keeps the symbol names) |
| `tflite-2.16.1-aar` | `libtensorflowlite_jni.so` | TFLite 2.16.1 AAR (stripped, kernel path strings) | 172 | 168 / 168 | 455 |
| `whobird` | `libtensorflowlite_jni.so` | whobird (BirdNET) app, **no symbols** | 176 | 172 / 172 | 466 |
| `lespas` | `libtensorflowlite_jni.so` | Lespas photo app, no symbols | 177 | 172 / 172 | 472 |
| `seeneva` | `libseeneva.so` | Seeneva comic reader: Rust app, TFLite statically linked | 126 | 122 / 122 | 312 |
| `litert-2.4-win` | `libLiteRt.dll` | LiteRT 2.4 for Windows (PE, Win64 calling convention) | 220 | 172 + 172 (two resolvers) | 476 |

| Sample | Binary | Models found |
|---|---|---|
| `deepfilternet` | `libdeep_filter_ladspa.so` (DeepFilterNet, Rust) | 3 ONNX models (223, 141 and 119 ops) inside a 35 MB gzip tar in `.rodata`, with tar member names and the function that loads them |
| `seeneva` | the APK, added beside `libseeneva.so` | YOLO detector, 247 ops: every operator maps to a recovered kernel (CONV_2D runs 21 nodes, DEQUANTIZE 58, ...) |
| `lespas` | the APK, added beside its `libtensorflowlite_jni.so` | SSD detector, 64 ops: every operator maps to a kernel, including the custom op `TFLite_Detection_PostProcess` |

**Reproduce every row.** All samples are public (F-Droid, Maven Central, PyPI, GitHub releases). One command
downloads them, checks each SHA-256, extracts the library to open and writes what you should see:

```
python tools/fetch_samples.py samples/            # all nine, about 210 MB
python tools/fetch_samples.py samples/ lespas     # or just one
```

Sources, hashes and licences are in [`tools/samples.json`](tools/samples.json).

Kernels beyond the resolver's count are TFLite's bundled custom ops (`TFLite_Detection_PostProcess`, `Mfcc`,
`AudioSpectrogram`, ...), found through their registration tables. Delegates are listed too: the GPU delegate
library shipped in the same Lespas APK (`libtensorflowlite_gpu_jni.so`) is reported as `gpu`.

**Accuracy check.** On the tflite-runtime build that keeps its `Register_*` symbols, the op resolver decoder
(which never looks at symbols) agrees with the symbols on **203 of 203** registrations. The same decoder is
what names the kernels in the stripped builds above.

On binaries with no ML inside (samples `control-vcomp140` and `control-ten-vad`) TensorLens reports no models, no resolver
and no kernels. The scanner has no false positives on 128 MB of random and low-entropy data, and survives
truncation and mutation fuzzing of every fixture (`tests/`).

## In the wild: every app on F-Droid

To see what TensorLens finds outside a test corpus, `tools/fdroid_survey.py` ran the scanner over the latest
version of every app in the F-Droid repository (Nov 27 to 28, 2026). It reads each APK's zip directory with HTTP
range requests and fetches only the entries that could hold a model: 6.0 GB downloaded for 88 GB of APKs.

| | |
|---|---|
| Apps surveyed | 5,012 (45 more could not be read) |
| Apps shipping an ML runtime library | 111: ONNX Runtime 51, TFLite / LiteRT / MediaPipe 27, ggml 24, OpenCV DNN 14, ncnn 2, PyTorch 2 |
| Apps with a model TensorLens reads | 49, with 89 models: ONNX 42, TFLite 41, ncnn 6 |
| Apps whose models use custom ops | 12, with 17 distinct custom ops |

What it turned up:

- **Five chat apps ship the same background-blur model.** Element, SchildiChat, Mages, Nextcloud Talk and TRIfA
  all carry a 246-operator selfie-segmentation model for video calls. It needs `Convolution2DTransposeBias`, a
  MediaPipe custom op that stock TFLite does not have, so whatever runs the model has to bring its own kernel.
- **ONNX Runtime contrib ops** (`com.microsoft::QAttention`, `SkipLayerNormalization`, `FusedMatMul`,
  `DynamicQuantizeLSTM`, ...) in four apps' quantised transformer and speech models.
- **TensorFlow Text ops** (`TFSentencepieceTokenizeOp`, `RaggedTensorToTensor`) in a 581-operator sentence encoder
  (Knotwork), and the TFLite `TFLite_Detection_PostProcess` op in Lespas, the app the walkthrough above uses.
- **75 apps ship a runtime but no model file the scanner reads**: the model is downloaded at run time, or stored in
  a format TensorLens does not parse yet, such as the GGUF files that ggml runtimes load (24 of the 75).

Every app with a runtime or a model is listed, with the models' paths, operator counts and custom ops, in
[`docs/survey/fdroid-2026-11-28.jsonl`](docs/survey/fdroid-2026-11-28.jsonl). To rerun it:

```
python tools/fdroid_survey.py --scan build/tensorlens-scan --out survey/      # several hours, resumable
python tools/fdroid_survey.py --summary survey/
```

Limits of the survey: runtimes are recognised by their library file names, and models are looked for in the
APK's files (assets, raw resources), not inside native libraries. Entries larger than 200 MB are skipped
(400 MB for the first 1,474 apps of the run).

## Install

**With hcli** (IDA 9.5 or later):

```
hcli plugin install tensorlens
```

**By hand:** download `tensorlens-<version>.zip` from the
[releases](https://github.com/AbrahamPaulJ/tensorlens/releases) and copy the plugin for your platform
(`tensorlens.dll`, `tensorlens.so` or `tensorlens.dylib`) into `%APPDATA%\Hex-Rays\IDA Pro\plugins` (Windows)
or `~/.idapro/plugins` (Linux, macOS).

No Python, no dependencies: the flatbuffer, protobuf and zip readers are built in. Works in every IDA
edition that loads native plugins, including IDA Free 9.5.

## Usage

| Action | Where |
|---|---|
| Analyse everything (find models, recover the runtime, open the windows) | **Edit > Plugins > TensorLens** or `Ctrl+Alt+M` |
| Models found | **View > Open subviews > TensorLens: models**. `Enter` opens the graph; right-click to export the model |
| Kernels recovered | **View > Open subviews > TensorLens: TFLite kernels**. `Enter` jumps to `Eval` |
| Add the models an app ships beside the library | **File > Load file > TensorLens: add models from a file, APK or AAR** |
| Export the report | **File > Produce file > TensorLens: export report (HTML + JSON)** |

A typical session on an Android app:

1. Open `lib/x86_64/libtensorflowlite_jni.so` (or the app's own library with TFLite linked in) and press
   `Ctrl+Alt+M`. The kernels window fills with `CONV_2D`, `DEPTHWISE_CONV_2D`, ... and every kernel function
   is named and typed.
2. **Add models** and pick the APK. TensorLens reads the models in `assets/` (also inside MediaPipe `.task`
   bundles), and every kernel comment now says which model nodes it runs.
3. Open a model's graph, hover a node for its tensors, double-click it to land in its `Eval`.

**Headless** (CI, batch triage):

```
ida -Otensorlens:report.json  path/to/libfoo.so
```

writes `report.json` and `report.html` after auto-analysis and closes IDA. Set `TENSORLENS_MODELS` to a
`;`-separated list of files or APKs to add their models first. (IDA Pro can add `-A` to skip the load dialog.)

## Command-line scanner

```
tensorlens-scan [--json FILE] [--html FILE] [--extract DIR] [--tensors] [-q] files...
```

```
$ tensorlens-scan site.leos.apps.lespas_120.apk
site.leos.apps.lespas_120.apk!assets/objectdetect.tflite @0x0  TFLite schema v3, 64 ops (CONV_2D x34, DEPTHWISE_CONV_2D x13, RESHAPE x13, ...), 4.0 MB weights  (4.0 MB)
    custom op: TFLite_Detection_PostProcess
```

## How it works

**Finding models.** The scanner looks for each format's signature (`TFL3` at offset 4, ONNX's leading
`ir_version` field, ncnn's `7767517`, ExecuTorch's `ET`) and then parses the whole structure with a
bounds-checked reader: every flatbuffer offset, vtable and vector, every protobuf field. A candidate counts
only if it parses completely; its true size is the furthest byte the parser touched. Gzip streams are
inflated and scanned in turn, and tar member names are kept.

**Recovering the TFLite runtime** combines three independent sources of evidence:

1. **The op resolver** (works on fully stripped builds). `BuiltinOpResolver`'s constructor is a long run of
   `AddBuiltin(this, BuiltinOperator_X, Register_X(), min, max)`. TensorLens finds it as the function that
   calls one callee hundreds of times, then walks it once with a small register-constant tracker. The tracker
   follows `mov reg, imm`, `push imm; pop reg`, copies of constants kept in callee-saved registers, call
   clobbers and PLT thunks, then reads the operator code and the registration at each call. It works per
   ABI: SysV and Win64 on x86-64, AAPCS on ARM64 and ARM.
2. **`__FILE__` strings.** Every `TF_LITE_ENSURE` in a kernel leaves `tensorflow/lite/kernels/conv.cc` in
   `.rodata`; the functions that reference it belong to that kernel's source file.
3. **Symbols**, when the build kept `tflite::ops::builtin::Register_CONV_2D()`.

Each candidate `TfLiteRegistration` is validated (`invoke` must be code, `builtin_code` in range,
`custom_name` a string or null) before anything is named. Names are only applied over IDA's dummy names,
never over symbols or your own names. Functions shared by several operators (one `Prepare` for RELU, RELU6
and TANH) are named after the shared source file and list every operator in their comment.

## Building

```
git clone https://github.com/HexRaysSA/ida-sdk
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DIDASDK=path/to/ida-sdk
cmake --build build
ctest --test-dir build
```

Without `IDASDK`, only the core library, `tensorlens-scan` and the tests build. Windows: `tools\build.bat`.
GitHub Actions builds Windows, Linux and macOS (universal) on every push and attaches the release zip to tags.

## Limitations

- Kernel recovery covers TFLite / LiteRT. ONNX Runtime is detected (and its execution providers listed), but
  its kernels are not named yet.
- Models that are encrypted, or downloaded at run time, cannot be found in the binary; the report still shows
  the runtime and its delegates.
- The graph view shows up to 3000 operators per subgraph.
- Tested on x86_64 builds (ELF and PE) with IDA Free 9.5. The ARM64 and ARM paths use the same decoder with the AAPCS
  argument registers but have not been run in IDA yet.

## Credits

- Author: Abraham Paul Jaison.
- TFLite schema and C API types: TensorFlow (Apache-2.0). ONNX field numbers: onnx.proto (Apache-2.0).
- [miniz](https://github.com/richgel999/miniz) (MIT) for zip and inflate.
- Test fixtures from the TensorFlow and ONNX repositories (Apache-2.0).
- Built with the help of an AI coding assistant (Claude, by Anthropic) for code, tests and documentation.
  All results in this README were measured by running the plugin.

MIT licence. See [LICENSE](LICENSE).
