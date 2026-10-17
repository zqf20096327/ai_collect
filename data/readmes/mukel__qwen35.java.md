# Qwen35.java

<p align="center">
  <img src="https://github.com/user-attachments/assets/fc8a55cb-5ba0-4de9-a32f-f1fcf5dbbbda" width="400">
</p>

<div align="center">

![Java 21+](https://img.shields.io/badge/Java-21%2B-007396?logo=java&logoColor=white)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg?logo=apache)](LICENSE)
[![GraalVM](https://img.shields.io/badge/GraalVM-Native_Image-F29111?labelColor=00758F)](https://www.graalvm.org/latest/reference-manual/native-image/)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)

Fast, zero-dependency, inference engine for [Qwen 3.5](https://qwen.ai/) in pure Java.

</div>

----

## Features

- Single file, **no dependencies**, based on [llama3.java](https://github.com/mukel/llama3.java)
- Supports **all** tested Qwen 3.5 model families: `0.8B`, `2B`, `4B`, `9B`, `27B`, and `35B-A3B` (MoE)
- Fast [GGUF format](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) parser
- Supported dtypes/quantizations: `F16`, `BF16`, `F32`, `Q4_0`, `Q4_1`, `Q4_K`, `Q5_K`, `Q6_K`, `Q8_0`
- Matrix-vector kernels using Java's [Vector API](https://openjdk.org/jeps/469)
- CLI with `--chat` and `--prompt` modes
- GraalVM Native Image support
- AOT model preloading for **instant time-to-first-token**

## Setup

Download GGUF models from Hugging Face:

| Model | Architecture | GGUF Repository |
|-------|-------------|-----------------|
| 0.8B | Dense, ~0.8B total params | [unsloth/Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) |
| 2B | Dense, ~2B total params | [unsloth/Qwen3.5-2B-GGUF](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF) |
| 4B | Dense, ~4B total params | [unsloth/Qwen3.5-4B-GGUF](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF) |
| 9B | Dense, ~9B total params | [unsloth/Qwen3.5-9B-GGUF](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF) |
| 27B | Dense, ~27B total params | [unsloth/Qwen3.5-27B-GGUF](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF) |
| 35B-A3B | Mixture of Experts (MoE) | [unsloth/Qwen3.5-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF) |

**Larger MoE models are not tested.**

#### Optional: pure quantizations

`Q4_0` files are often mixed-quant in practice (for example, `token_embd.weight` and `output.weight` may use `Q6_K`).
A pure quantization is not required, but can be generated from an F32/F16/BF16 GGUF source with `llama-quantize` from [llama.cpp](https://github.com/ggml-org/llama.cpp):

```bash
./llama-quantize --pure ./Qwen3.5-4B-F16.gguf ./Qwen3.5-4B-Q4_0.gguf Q4_0
```

Pick any supported target quantization, for example `Q4_0`, `Q4_1`, `Q4_K`, `Q5_K`, `Q6_K`, or `Q8_0`.


## Build and run

Java 21+ is required, in particular for the [`MemorySegment` mmap-ing feature](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/channels/FileChannel.html#map(java.nio.channels.FileChannel.MapMode,long,long,java.lang.foreign.Arena)).

[`jbang`](https://www.jbang.dev/) is a good fit for this use case.

No-setup one-liner, no git clone, no manual model download required ... ~5GB download once, then cached by `jbang`:
```bash
jbang qwen35@mukel \
    --model %{https://hf.co/unsloth/Qwen3.5-4B-GGUF/resolve/main/Qwen3.5-4B-Q8_0.gguf} \
    --system-prompt "You are a helpful assistant" \
    --chat
```
Alternatively:
```
jbang Qwen35.java --help
jbang Qwen35.java --model ./Qwen3.5-4B-Q4_0.gguf --chat
jbang Qwen35.java --model ./Qwen3.5-4B-Q4_0.gguf --prompt "Explain quantum computing like I'm five"
```

Or run it directly (still via [`jbang`](https://www.jbang.dev/)):
```bash 
chmod +x Qwen35.java
./Qwen35.java --help
```

#### Optional: Makefile

A simple [Makefile](./Makefile) is provided. Run `make jar` to produce `qwen35.jar`.

Run the resulting `qwen35.jar` as follows: 
```bash
java --enable-preview --add-modules jdk.incubator.vector -jar qwen35.jar --help
```

### GraalVM Native Image

Compile with `make native` to produce a `qwen35` executable, then:

```bash
./qwen35 --model ./Qwen3.5-4B-Q8_0.gguf --chat
```

### AOT model preloading

`Qwen35.java` supports AOT model preloading to reduce parse overhead and time-to-first-token (TTFT).

To AOT pre-load a GGUF model:
```bash
PRELOAD_GGUF=/path/to/model.gguf make native
```

A larger specialized binary is generated with parse overhead removed for that specific model.
It can still run other models with the usual parsing overhead.

## Related Repositories

- [llama3.java](https://github.com/mukel/llama3.java)
- [gemma4.java](https://github.com/mukel/gemma4.java)
- [gptoss.java](https://github.com/mukel/gptoss.java)
- [qwen35.java](https://github.com/mukel/qwen35.java)

## License

Apache 2.0
