# vllm4j

**English** | [中文](README.zh-CN.md)

A minimal Java LLM inference engine implementing the core techniques of modern serving systems:
**paged KV cache (PagedAttention) + prefix caching + continuous batching + chunked prefill + recompute preemption**,
in ~1.5K lines of dependency-light Java. CPU-only, SIMD-accelerated via the Java Vector API.

Supports **Qwen3 dense** models — verified token-exact against HuggingFace transformers
greedy output with Qwen3-0.6B.

Inspired by [nano-vllm](https://github.com/GeeeekExplorer/nano-vllm).

## Requirements

- Java 21+ (uses `jdk.incubator.vector`)
- Maven 3.9+
- A Qwen3 dense model directory containing `config.json`, `tokenizer.json`, `*.safetensors`
- Memory: ~8GB heap recommended for the 0.6B model (F32 weights ~2.4GB + KV cache)

## Quick start

```bash
# 1. Download the model into a plain directory (mirror endpoint optional)
HF_ENDPOINT=https://hf-mirror.com hf download Qwen/Qwen3-0.6B \
    model.safetensors config.json tokenizer.json generation_config.json \
    --local-dir ~/models/Qwen3-0.6B

# 2. Run tests (engine logic + SIMD kernel cross-checks; E2E auto-skips without the model)
mvn test

# 3. Run the demo (4 prompts sharing a prefix -> continuous batching + prefix cache)
MODEL=~/models/Qwen3-0.6B
mvn -q compile exec:java -Dexec.args="--model $MODEL"
```

## Documentation

- **[Architecture](docs/ARCHITECTURE.md)** — how it works: paged KV cache,
  prefix caching, continuous batching, chunked prefill, preemption, the
  attention kernel, verification, design trade-offs. ([中文版](docs/ARCHITECTURE.zh-CN.md))

## Usage

### CLI

```bash
MODEL=~/models/Qwen3-0.6B

# Custom prompts (--prompt is repeatable; multiple prompts form one concurrent batch)
mvn -q compile exec:java -Dexec.args="--model $MODEL \
  --prompt 'Explain KV cache in one sentence' \
  --prompt 'Write a haiku about autumn' \
  --max-tokens 128 --temperature 0.7"
```

| Flag | Description | Default |
|---|---|---|
| `--model <dir>` | Model directory | required |
| `--prompt "..."` | Repeatable; multiple prompts run as one batch | 4 built-in demo prompts |
| `--max-tokens N` | Max generated tokens per request | 64 |
| `--temperature T` | 0 = greedy (deterministic), >0 = sampling | 0.7 |
| `--thinking` | Enable Qwen3 thinking mode (off = inject empty `<think>` block) | off |

JVM flags (`--add-modules=jdk.incubator.vector -Xmx8g`) are picked up automatically
from `.mvn/jvm.config` when running through Maven from the project root. When running
with plain `java`, pass them explicitly.

### As a Java library

Runnable versions of all snippets below live in
[`src/main/java/io/github/vllm4j/examples/`](src/main/java/io/github/vllm4j/examples/):

```bash
MODEL=~/models/Qwen3-0.6B
mvn -q compile exec:java -Dexec.mainClass=io.github.vllm4j.examples.BatchGenerationExample   -Dexec.args="$MODEL"
mvn -q compile exec:java -Dexec.mainClass=io.github.vllm4j.examples.ConcurrentRequestsExample -Dexec.args="$MODEL"
mvn -q compile exec:java -Dexec.mainClass=io.github.vllm4j.examples.ManualLoopExample         -Dexec.args="$MODEL"
mvn -q compile exec:java -Dexec.mainClass=io.github.vllm4j.examples.RawTokensExample          -Dexec.args="$MODEL"
```

#### 1. Batch generation (simplest)

```java
import io.github.vllm4j.*;
import java.nio.file.Path;
import java.util.List;

Config config = new Config(Path.of("/path/to/Qwen3-0.6B"));
try (LLM llm = new LLM(config)) {
    SamplingParams params = new SamplingParams(0.7f, 128); // temperature, maxTokens

    // Qwen3 chat template (<|im_start|> format; second arg toggles thinking mode)
    String prompt = llm.applyChatTemplate("What is paged attention?", false);

    List<LLM.Output> outputs = llm.generate(List.of(prompt), params);
    System.out.println(outputs.get(0).text());
}
```

#### 2. Concurrent requests (continuous batching kicks in automatically)

```java
try (LLM llm = new LLM(config)) {
    // All requests share one scheduler: common prefixes hit the prefix cache,
    // decode steps are batched across sequences automatically.
    List<String> prompts = questions.stream()
            .map(q -> llm.applyChatTemplate(q, false))
            .toList();
    List<LLM.Output> outputs = llm.generate(prompts, SamplingParams.greedy(64));
    for (LLM.Output o : outputs) {
        System.out.println(o.seqId() + ": " + o.text());
    }
}
```

#### 3. Driving the engine loop manually (streaming / dynamic request injection)

The `addRequest` + `step` pattern, suited for server-side scenarios:

```java
try (LLM llm = new LLM(config)) {
    long id1 = llm.addRequest(llm.applyChatTemplate("Question one", false), new SamplingParams(0.7f, 64));
    long id2 = llm.addRequest(llm.applyChatTemplate("Question two", false), SamplingParams.greedy(32));

    while (!llm.isFinished()) {
        List<LLM.Output> finished = llm.step(); // one step = one prefill batch or one decode batch
        for (LLM.Output o : finished) {
            System.out.println("request " + o.seqId() + " done: " + o.text());
        }
        // New requests may be added here at any time; the scheduler folds them in.
    }
}
```

#### 4. Raw token ids (bypassing the tokenizer)

```java
int[] promptTokens = ...; // pre-encoded tokens
List<Integer> completion = llm.generateTokens(promptTokens, SamplingParams.greedy(32));
```

#### 5. Engine configuration

```java
Config config = new Config(modelDir)
        .maxNumSeqs(16)            // max sequences per batch
        .maxNumBatchedTokens(2048) // max tokens per step (chunked-prefill granularity)
        .kvCacheBlockSize(32)      // KV block size in tokens
        .numKvCacheBlocks(256);    // total KV blocks: the main memory knob (~1.8GB at 0.6B)
```

When KV blocks run out the engine preempts (recompute-style) instead of OOMing;
preempted sequences usually recover quickly via the prefix cache.

Sampling semantics: `temperature = 0` is greedy (fully deterministic); `> 0` uses
Gumbel-max temperature sampling — fix the seed with `new LLM(config, seed)` for
reproducible sampled runs.

## Verifying against HuggingFace

```bash
python3 scripts/gen_golden.py "$MODEL"    # HF transformers greedy golden tokens
mvn test -Dtest=E2eTest                  # token-exact comparison on the Java side
```

## Architecture

```
LLM (facade)            tokenize -> schedule -> run -> postprocess loop
├── Scheduler           continuous batching: prefill-priority, chunked prefill, preemption
│   └── BlockManager    paged block pool, ref-counted sharing, chained-hash prefix cache
├── ModelRunner         packs varlen batches, slot mappings, block tables
│   └── Qwen3Model      GQA + per-head QK-Norm + RoPE + SwiGLU (float[] weights)
│       ├── PagedAttention   online-softmax over block tables (CPU stand-in for flash-attn)
│       └── TensorOps        Vector API SIMD matmul/dot/saxpy/rmsnorm
└── KvCache             [layer][block][kvHead][blockSize][headDim] float arrays
```

Design notes: CPU-only by design (no GPU/tensor-parallel/CUDA graphs); attention
metadata travels through an explicit `ForwardContext` rather than a global singleton;
block size defaults to 32 since CPUs have no kernel-launch overhead to amortize;
greedy sampling is built in to enable exact-match verification against HF.

## License

MIT
