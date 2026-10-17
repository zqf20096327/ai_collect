# WebGPU Inference

> [!WARNING]
> **Experimental — not ready for production use.** APIs may change, and stability,
> performance, and device compatibility have not been validated for production workloads.
> This repository was created for experimentation. The library is not published to
> Maven Central or any other external artifact repository; build it from source to try it.

A small GPU inference runtime for Android, built with Kotlin and AndroidX WebGPU.
It supports static FP32 models, custom WGSL kernels, reusable model sessions, and
explicit GPU buffer budgets.

The included **WebGPU Denoise Lab** app demonstrates tiled photo denoising with
NAFNet. Select a JPEG or PNG, compare the result, and export it as a PNG.

## Demo

<img src="https://github.com/user-attachments/assets/9f24300a-cd48-414e-9a37-bf6cf65dc042" width="360" height="760" alt="WebGPU Denoise Lab photo denoising demo" />

<video src="public/demo.mp4" controls muted playsinline preload="none" poster="public/demo-result.png" width="320">
  <a href="public/demo.mp4">Watch the demo — MP4, 31 seconds</a>
</video>

Select a photo, tap **DENOISE PHOTO**, move the comparison slider, then tap
**SAVE PHOTO** to export the PNG. The recording shows processing and comparison;
idle pauses were removed without speeding up inference. The demo uses its default
25% inference duty cycle. The sample photograph is CC0 by Rachel Michetti, via
[scikit-image](https://scikit-image.org/docs/0.25.x/api/skimage.data.html#skimage.data.coffee).
It demonstrates the workflow, not denoising quality on a noisy-photo dataset.
[Media sources and capture details](public/README.md).

## Build and run

Requirements: JDK 21, Android SDK 37, Python 3.12+, CMake, Ninja, and Android NDK
`28.2.13676358`. Set `ANDROID_HOME` or `sdk.dir` in `local.properties`.
The demo requires Android 8.0 (API 26) or newer and a compatible GPU.

Model weights are not included. Follow [model setup](docs/model-setup.md) before
running inference, then build the app:

```sh
./gradlew :app:assembleDebug
```

The first build compiles the [patched WebGPU native dependency](tools/webgpu-native/README.md);
subsequent builds reuse the native cache.

## Use the runtime

Add `implementation(project(":library"))` to your Android module.

```kotlin
import java.io.File
import io.github.l2hyunwoo.webgpu.inference.model.ModelDefinition
import io.github.l2hyunwoo.webgpu.inference.runtime.SessionOptions
import io.github.l2hyunwoo.webgpu.inference.runtime.loadModelSession
import io.github.l2hyunwoo.webgpu.inference.runtime.useSuspending

suspend fun runModel(
    manifestJson: String,
    weightsFile: File,
    inputValues: FloatArray,
): FloatArray {
    val model = ModelDefinition.fromJson(manifestJson)
    val options = SessionOptions(maxGpuBufferBytes = 256L * 1024 * 1024)

    return loadModelSession(
        model = model,
        options = options,
        openWeights = { weightsFile.inputStream() },
    ).useSuspending { session ->
        val result = session.run(mapOf(model.inputs.single() to inputValues))
        result.outputs.getValue(model.outputs.single())
    }
}
```

See [runtime and custom kernels](docs/runtime.md) for model definitions, resource
ownership, supported operators, and the tiled denoising adapter.

## Measured performance

On the same SM-S948N, a separate 100-inference run of NAFNet FP32 with a
256×256 input measured **266.0 ms median** and **506.2 ms p95**. Model initialization
took **2.29 seconds**. This used a debug APK, patched WebGPU alpha05, and no added
rest between inferences. All 100 results passed the PyTorch-reference check.

<img src="public/inference-latency.png" width="960" alt="Measured latency for all 100 inferences and their distribution" />

Timing includes input upload, command encoding, GPU completion, and readback.
It excludes initialization, photo decoding, tiling, pacing, and PNG export, so
these numbers are **not full-photo processing times**. This is one device/session,
not a comparison against other runtimes. No warm-up samples were discarded.
[Measurement conditions, CSV data, and reproduction](docs/benchmarks.md).

## Project structure

- `library`: model definitions, GPU execution, kernels, and photo denoising.
- `app`: Compose photo-denoising demo.
- `tools`: model preparation, native dependency builds, and device profiling.

## Current scope

The runtime uses AndroidX WebGPU 1.0.0-alpha05 and supports:

- Static FP32 tensors with model definitions created in Kotlin or read from the
  project's exported graph format.
- Multiple named inputs and outputs in Kotlin model definitions. The exported
  file format currently has one input and one output.
- Custom WGSL kernels registered from Kotlin, reusable model sessions,
  intermediate-buffer reuse, and explicit GPU buffer budgets.

`ModelSession.run` accepts and returns CPU-side `FloatArray` values. FP16,
dynamic tensor shapes, and public APIs for GPU-resident inputs/outputs are not
implemented. ONNX, TFLite, and GGUF files cannot be loaded directly.

The demo processes photos in tiles and defaults to a 25% inference duty cycle.
Tiling can differ from whole-image inference because NAFNet uses global pooling.
RAW/HDR preservation is not supported.

## License

Project code is [MIT licensed](LICENSE). Model sources and pretrained weights have
separate terms; see [model licensing and preparation](docs/model-setup.md#license-and-model).
Photo attribution and recording details are in [demo assets](public/README.md).
