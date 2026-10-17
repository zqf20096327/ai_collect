# Gemma 4 in Godot

> [!WARNING]
> This is not a game-ready project. It is an experiment to see whether LLM inference can run directly in Godot without external dependencies (only gdscript and compute shaders).
> It is about an order of magnitude slower than a real inference stack such as llama.cpp with CUDA kernels, so it should only be treated as an experiment.

This Godot 4.7 project runs exactly one model: `gemma-4-E2B-it-Q4_K_M.gguf`. The transformer executes in compute shaders; GDScript handles the model's GGUF metadata, tokenizer, sampling, cache, and chat UI. There is no external inference process, native extension, HTTP service, model catalog, or runtime model selection.

![The Gemma chat interface running in Godot](docs/app-screenshot.png)

## Model file

Keep the model directly in `models/`:

```text
models/
└── gemma-4-E2B-it-Q4_K_M.gguf
```

Open the project and run `node_2d.tscn`. An exported build looks for the same exact filename at `models/gemma-4-E2B-it-Q4_K_M.gguf` beside the executable, then falls back to the project resource during development. The model path cannot be overridden at runtime.

The runtime is `llm/gemma/Gemma4E2BQ4KRuntime.gd`, backed by `llm/gemma/GemmaGpuPipeline.gd`. Shared code under `llm/common/` exists only for the GGUF representation, tokenizer, sampler, prefill cache, quantized tensor reads, and GPU operations required by this Gemma artifact.

## Benchmark

```powershell
Godot.exe --rendering-driver vulkan --path . --script res://tools/benchmark.gd -- --tokens 32 --runs 1 --warmup 0 --temperature 0.5 --top-k 40 --no-cache --show-text
```

The benchmark follows the same message-template flow and sampling defaults as the chat UI. It asks two related questions, carries the first answer into the second round, reports reusable-prefix and GPU timing metrics, and checks that the answers mention Paris and the Seine without repeated phrases. Use `--verify-reference` with deterministic sampling to compare optimized and reference token IDs. Run with `--help` for tuning and reporting options. There is deliberately no model-path or model-selection option.

## Requirements and limitations

- godot 4.7 with a local Vulkan-capable `RenderingDevice`
- the exact `gemma-4-E2B-it-Q4_K_M.gguf` artifact in the fixed location above
- text generation only
- the implementation is specialized for this model's expected tensors, dimensions, prompt format, token IDs, and attention layout
- gguf metadata is consumed as stored; mismatched or incomplete model data is rejected during loading or tensor validation





![Gemma refuses to reveal the tomahawk steak temperature](docs/gemma-steak-joke.png)

## Inference flow

### 1. Load the model

- open the model file
- check the file header and version
- read model settings and tokenizer data
- read the tensor list: name, shape, type, offset, and size
- check that all required tensors exist and have the expected shapes
- keep large weights on disk until they are needed, or upload them all at startup

### 2. Prepare weights

- most weights are quantized to save memory
- a block stores small integer values plus one or more scales
- compute kernels unpack the values while doing matrix multiplication
- small tensors, such as norm weights, can be converted to floats once
- dot products usually use float accumulators to reduce rounding errors

### 3. Allocate memory

- weight buffers hold model tensors
- scratch buffers hold temporary layer results
- the KV cache holds old keys and values for attention
- logit buffers hold scores for the full vocabulary
- candidate buffers hold the best tokens for sampling
- buffer offsets, shapes, and alignment must match the compute kernels

### 4. Build the prompt

- join system, user, and assistant messages
- add the model's special turn markers
- add the prefix that tells the model to start the assistant reply
- the exact prompt format matters because it was used during training

### 5. Tokenize

- split text into token pieces
- convert pieces to token IDs
- handle special tokens separately
- keep the token IDs in order
- the model receives IDs, not words or characters

### 6. Prefill the prompt

- read the embedding row for each prompt token
- run every prompt token through every transformer layer
- use a causal mask so tokens cannot see future tokens
- process several prompt tokens together when possible
- store their keys and values in the KV cache
- keep the logits from the last prompt position

### 7. Run one transformer layer

- normalize the input vector
- project it into query, key, and value vectors
- apply position data to queries and keys
- write the new key and value to the KV cache
- compare the query with visible cached keys
- scale the attention scores
- apply the causal or sliding-window mask
- run softmax over the scores
- use the scores to mix cached values
- project the attention result back to hidden size
- add the residual connection
- normalize again
- run the feed-forward gate, activation, and projections
- add the second residual connection
- pass the result to the next layer

### 8. Attention details

- each query head reads one or more KV heads
- grouped-query attention lets several query heads share KV heads
- sliding attention reads only recent cache entries
- global attention can read the full cache
- softmax subtracts the largest score before `exp` to avoid overflow
- long-context kernels can process the cache in blocks instead of storing every score

### 9. Create logits

- normalize the output of the final layer
- multiply it by the output matrix
- produce one score for each vocabulary token
- block tokens that are not allowed
- apply repetition or frequency penalties if enabled
- keep only the best candidates when the full logit list is not needed

### 10. Pick the next token

- greedy decoding picks the highest score
- temperature changes how sharp the score distribution is
- top-k keeps only the best `k` tokens
- top-p keeps enough tokens to reach a probability limit
- convert the remaining scores to probabilities
- draw one token using the random seed
- stop on EOS, a stop sequence, cancellation, context limit, or token limit

### 11. Decode one token

- add the selected token to the output list
- convert token pieces back to bytes
- wait if the last bytes are only part of a UTF-8 character
- remove special tokens from visible output
- send the new valid text to the UI

### 12. Generate more tokens

- feed the selected token back into the model
- run it through every layer
- append its new keys and values to the KV cache
- read old context from the cache instead of recomputing it
- create new logits
- pick another token
- repeat until a stop condition is reached

### 13. Why prefill and generation have different speeds

- prefill processes many known tokens together
- large matrix operations use the GPU well
- generation handles one unknown token at a time
- every new token reads most of the model weights again
- generation is often limited by memory bandwidth
- smaller quantized weights mean less data to read per token

### 14. Synchronization

- each compute step depends on earlier results
- barriers make writes visible to later kernels
- missing barriers can cause random output or GPU-specific bugs
- buffers can be reused only after earlier work has finished with them
- cpu readback must wait for the device to finish writing candidates

### 15. Prompt cache

- save the KV cache after a prompt
- save the token position and next-token candidates
- restore them when the exact same prompt is used again
- include model identity, tokens, settings, and cache version in the key
- reject old cache data when shapes or settings change

### 16. Validation

- test tokenization against known token IDs
- test quantized block decoding
- compare kernel outputs with a simple reference path
- compare greedy token output between optimized and reference paths
- check tensor shapes, cache offsets, head mapping, and token positions
- repetitive but readable output can still mean the math is wrong

### 17. Cleanup

- flush any remaining decoded text
- keep the KV cache if the conversation will continue
- free request scratch buffers when they are no longer needed
- keep model weights loaded for the next request
- wait for queued device work before destroying GPU resources
