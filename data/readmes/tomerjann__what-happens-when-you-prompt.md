# What happens when you send a prompt to an LLM chat?


<img width="1022" height="540" alt="what-happens-when-you-prompt svg" src="https://github.com/user-attachments/assets/67adbe3d-751a-439f-82ab-5f2a14515485" />

This repository answers a deceptively deep question:

> **"What happens  -  at every layer of the stack  -  when you type a message into Claude or ChatGPT and press Send?"**

Inspired by the classic [`what-happens-when`](https://github.com/alex/what-happens-when) repository for browser navigation, this traces the full journey of a prompt: from keystroke to rendered response, skipping nothing.

The target reader is an engineer who already understands transformers, attention, and RAG  -  and wants **production intuition**, not another introductory walkthrough.

Contributions welcome. If you see a missing layer, open a PR.

> **Disclaimer:** Neither Anthropic nor OpenAI publishes their infrastructure internals. This document describes general patterns that are well-established across the industry - grounded in public research, open-source inference frameworks, and published API documentation. Where specific examples are needed (model architecture, pricing, safety classifiers), they draw from open-source models or a single provider's public docs and may not reflect every provider's exact implementation. If you have firsthand knowledge that contradicts something here, please open a PR.

---

## Table of Contents

- [The user types a character](#the-user-types-a-character)
- [The Send button is pressed](#the-send-button-is-pressed)
- [The HTTP request leaves the browser](#the-http-request-leaves-the-browser)
- [The API Gateway receives the request](#the-api-gateway-receives-the-request)
- [Authentication and rate limiting](#authentication-and-rate-limiting)
- [Input moderation and safety pre-screening](#input-moderation-and-safety-pre-screening)
- [Context assembly](#context-assembly)
- [Tokenization](#tokenization)
- [Routing to an inference node](#routing-to-an-inference-node)
- [KV cache lookup (prefix caching)](#kv-cache-lookup-prefix-caching)
- [The prefill phase](#the-prefill-phase)
- [The decode phase (autoregressive generation)](#the-decode-phase-autoregressive-generation)
- [Sampling and the logit pipeline](#sampling-and-the-logit-pipeline)
- [Token is emitted  -  streaming begins](#token-is-emitted--streaming-begins)
- [Tool use / function calling](#tool-use--function-calling)
- [Output moderation and safety post-screening](#output-moderation-and-safety-post-screening)
- [The response reaches the browser](#the-response-reaches-the-browser)
- [Markdown rendering and streaming display](#markdown-rendering-and-streaming-display)
- [The final token arrives](#the-final-token-arrives)
- [Billing, logging, and observability](#billing-logging-and-observability)

---

## The user types a character

Before a single byte leaves the browser, a surprising amount of work happens locally.

### Live token counting

Some LLM chat UIs run a real tokenizer client-side as you type  -  not a server round-trip, but a WASM-compiled tokenizer (such as tiktoken for OpenAI-compatible APIs, or a JavaScript port of SentencePiece for others) running in a Web Worker so it doesn't block the main thread. Other UIs use character-count heuristics and don't bother with real tokenization.

```
[Main Thread]             [Web Worker]
     |                        |
  keystroke                   |
     | ---postMessage(text)--> |
     |                  tokenize(text)
     | <--postMessage(count)-- |
  update counter              |
```

The count shown is always an approximation. The server-side tokenization adds special tokens, role markers, and prompt wrapping that the client doesn't know about  -  so displayed counts typically run 1–3 tokens low.

### Auto-save and draft state

The *current unsent message* is persisted to `localStorage` or `IndexedDB` with debounced writes so the browser can recover from a tab crash. This is draft recovery for the input field - not the conversation history.

The conversation history lives in the app's in-memory state (React state, Redux, or equivalent). Some apps also write it to `localStorage` so the UI can reload past messages after a page refresh, but that's display persistence. What actually gets serialized into every API request is assembled from runtime memory at the moment you press Send - covered in the next section.

---

## The Send button is pressed

### Client-side validation

Three checks before any network call:

- **Token budget**: Is the estimated prompt length within the model's context limit? If not, warn or refuse locally.
- **Empty message guard**: Whitespace-only messages are rejected client-side.
- **Rate limit optimism**: The frontend may track remaining quota locally to give immediate feedback without waiting for a 429.

### Conversation state serialization

This is the architectural fact that surprises most people when they first see it: the entire conversation history  -  not just your new message  -  is serialized into every request. LLMs are stateless. There is no session on the server storing your previous messages. Every turn is a fresh inference call with the full history in the context window.

```
What the server actually receives for "What's the capital of France?":
──────────────────────────────────────────────────────────────────────
[system]    You are a helpful assistant...
[user]      Hi, can you help me with geography?
[assistant] Of course! What would you like to know?
[user]      What's the capital of France?      <── your new message
──────────────────────────────────────────────────────────────────────
```

The cost implication is direct: inference cost grows with conversation length. The attention mechanism is O(n²) in sequence length during prompt processing  -  a conversation at turn 50 costs dramatically more than the same conversation at turn 5. This is not O(1). Long conversations are expensive.

### Optimistic UI update

The UI renders your message immediately (before server acknowledgment) and shows a streaming indicator. This is an optimistic update  -  if the request fails, the UI must roll back to the last valid state.

---

## The HTTP request leaves the browser

### Streaming protocol selection

LLM responses stream. Two protocols handle this in practice:

**Server-Sent Events (SSE)**  -  the dominant choice for LLM chat UIs:
```
POST /v1/messages HTTP/1.1
Accept: text/event-stream
Cache-Control: no-cache

── server pushes ──────────────────────────────────────────────
data: {"type":"content_block_delta","delta":{"text":"The "}}
data: {"type":"content_block_delta","delta":{"text":"capital"}}
data: {"type":"content_block_delta","delta":{"text":" is Paris"}}
data: [DONE]
```

SSE is unidirectional and text-based over a persistent HTTP connection. The browser's native `EventSource` API handles SSE natively and includes automatic reconnection  -  but `EventSource` is GET-only. LLM APIs use POST. So in practice, production clients use `fetch()` + `ReadableStream`, which gives you SSE parsing without the reconnect handling. You implement reconnection yourself.

**WebSockets** appear in multi-modal or bidirectional-streaming applications (e.g., sending audio chunks while receiving text). For text-only chat, SSE wins on simplicity.

### Request body

A typical request to the Claude or OpenAI API:

```json
POST /v1/messages
{
  "model": "claude-opus-4-6",
  "max_tokens": 4096,
  "stream": true,
  "system": "You are a helpful assistant...",
  "messages": [
    {"role": "user",    "content": "Hi, can you help me with geography?"},
    {"role": "assistant","content": "Of course! What would you like to know?"},
    {"role": "user",    "content": "What's the capital of France?"}
  ]
}
```

Anthropic's API separates `system` from `messages` because the system prompt occupies a fundamentally different position in the model's principal hierarchy  -  it represents operator-level instructions with a different trust level than user turns. A side effect of its stable position is that it's the prime candidate for prefix caching, described later.

---

## The API Gateway receives the request

### Edge routing and TLS termination

The request first hits a CDN edge node or global load balancer (Cloudflare, AWS Global Accelerator, or a proprietary anycast network). TLS terminates here  -  not at the model server. That means:

- The edge node decrypts the request
- Re-encrypts it for the internal hop to the application layer (mTLS)
- The data is decrypted in memory at the edge node before re-encryption for internal transit

This has implications for data residency compliance: if TLS terminates at a geographically distributed edge, the request is briefly in plaintext at that location.

### Request routing

The gateway routes based on:

1. **API key** → identifies the organization and its tier (free, pro, enterprise)
2. **Model name** → routes to the appropriate model cluster
3. **Geographic affinity** → for data residency requirements (EU data stays in EU infrastructure)
4. **Load** → consistent hashing or least-connections to inference nodes

```
Internet ──► Edge POP ──► API Gateway ──► [Auth Service]
                              │
                    ┌─────────┼──────────┐
                    ▼         ▼          ▼
               [claude-3   [claude-3  [claude-3
                haiku]      sonnet]    opus]
               cluster     cluster    cluster
```

---

## Authentication and rate limiting

### API key validation

The API key is looked up in a low-latency key-value store (typically Redis or equivalent distributed cache). The lookup validates:

- Key exists and is not revoked
- Associated account is in good standing
- Key has permission to use the requested model
- Key has not been flagged for suspicious activity

This is on the critical path for every request  -  sub-millisecond lookup latency is the target.

### Rate limiting

Rate limiting for LLM APIs is more complex than for traditional APIs because request cost is highly variable. A 10-token request and a 100,000-token request hit the same endpoint but consume radically different resources.

Modern LLM rate limiters operate on multiple dimensions simultaneously:

| Dimension | Typical Unit | Why it matters |
|-----------|-------------|----------------|
| Requests per minute (RPM) | count/min | Protects against connection flooding |
| Input tokens per minute (ITPM) | tokens/min | Prefill is GPU-compute-intensive |
| Output tokens per minute (OTPM) | tokens/min | Decode is GPU-memory-bandwidth-bound |

Some providers use a combined TPM metric rather than splitting input/output, and may layer on daily request limits (RPD).

The common enforcement algorithms are token bucket and sliding window  -  the choice trades burst handling against fairness under sustained load. When a limit is hit, the server returns `429 Too Many Requests` with a `Retry-After` header indicating when capacity will be available. The practical problem is that most client SDKs don't implement proper backoff, causing thundering herd behavior when limits reset.

---

## Input moderation and safety pre-screening

Before the prompt reaches the model, it passes through dedicated safety classifiers  -  these are separate models, not the main LLM. They range from small encoder models (~0.2B parameters, think DeBERTa-class) to fine-tuned generative models (Llama Guard at 8B, ShieldGemma at 2B–27B) running in parallel or as a fast pre-filter.

```
Request ──► [Fast Safety Classifier] ──► BLOCK / PASS
                    │
                    ▼ (if uncertain)
            [Deeper Analysis Model]
                    │
                    ▼
              BLOCK / PASS / FLAG_FOR_REVIEW
```

### What is being classified

- **Policy violations**: Content that violates the provider's usage policy (CSAM, detailed weapon synthesis, targeted harassment, etc.)
- **Prompt injection attempts**: User content trying to override the system prompt  -  e.g., "Ignore all previous instructions and..."
- **Jailbreak patterns**: Known attack patterns against the model's trained behaviors
- **PII detection**: Some deployments scrub or flag personally identifiable information before it reaches the model

### The classifier is itself a model

Smaller guard models run in single-digit milliseconds. Larger ones may take tens of milliseconds  -  fast enough to stay off the perceptible critical path. But these classifiers have their own false positive rate, and appeals processes exist for incorrectly blocked enterprise customers.

### Prompt injection: a deep problem

Prompt injection is the LLM equivalent of SQL injection  -  untrusted user content (or external content retrieved via tools/RAG) co-mingles with trusted control-flow instructions in the same context window, with no type system or privilege separation to distinguish them. There is no fully solved defense. Current mitigations:

- **Sandwich prompting**: Repeating key instructions after user content
- **Delimiter strategies**: Clearly marking trust boundaries with special tokens
- **Trained resistance**: RLHF-based training to resist override attempts
- **Separate classifier**: A dedicated model evaluating whether the assembled prompt has been compromised

None of these are foolproof. This is an active research area.

---

## Context assembly

This is the highest-leverage, least-documented stage in production LLM systems. What actually goes into the context window matters more than most engineers realize.

### What goes into the context window

The raw user messages are only one component. The full assembled context typically contains:

```
┌─────────────────────────────────────────────────────────────┐
│  CONTEXT WINDOW (e.g., 200k tokens)                         │
├─────────────────────────────────────────────────────────────┤
│  1. System Prompt                                           │
│     - Provider default behavior instructions               │
│     - Operator system prompt (from API caller)             │
│     - Dynamic injections (date/time, user preferences)     │
├─────────────────────────────────────────────────────────────┤
│  2. Tool Definitions                                        │
│     - JSON schemas for available functions/MCP tools       │
│     - Usage instructions per tool                         │
├─────────────────────────────────────────────────────────────┤
│  3. Retrieved Context (if RAG)                              │
│     - Chunks from vector search                            │
│     - Re-ranked and truncated to fit budget                │
├─────────────────────────────────────────────────────────────┤
│  4. Conversation History                                    │
│     - Previous turns (user + assistant)                    │
│     - Possibly summarized if too long                      │
├─────────────────────────────────────────────────────────────┤
│  5. Current User Message                                    │
│     - The new prompt                                       │
│     - Any attached files/images (tokenized separately)     │
├─────────────────────────────────────────────────────────────┤
│  6. Assistant Turn Prefix (optional)                        │
│     - "Pre-filling" the start of the model's response      │
│     - Support varies by provider and model                 │
└─────────────────────────────────────────────────────────────┘
```

### Context window management

When the assembled context exceeds the model's limit, something has to be dropped. The tradeoffs are brutal:

**Sliding window truncation**: Drop the oldest turns. Cheap and simple. The classic failure mode: "my name is Alice" gets forgotten by turn 30.

**Summarization**: Run a cheaper model to summarize old turns, inject the summary. Adds latency and a second inference cost. The summary loses information  -  hallucinated summaries compound quietly over a long session.

**Semantic retrieval**: Store old turns in a vector DB and retrieve relevant ones. Adds retrieval latency; relevance judgment is imperfect.

**Selective retention**: Always keep the system prompt, first user message, and last N turns; drop the middle. Heuristic, cheap, and surprisingly effective.

The right choice depends on your cost/latency/quality tradeoff. Simple sliding window truncation was the industry default for years. Providers are increasingly offering server-side summarization (e.g., Anthropic's compaction) for both consumer and enterprise use cases.

---

## Tokenization

The model never sees your text. It sees a sequence of integers. Tokenization is the step that bridges them  -  and its mechanics have consequences that reach all the way into model capability.

### BPE encoding

The assembled context is tokenized using Byte-Pair Encoding (BPE). The tokenizer is a deterministic algorithm  -  it applies a fixed set of merge rules built from corpus frequency during offline training. Tokenization takes microseconds.

```
Input:  "What's the capital of France?"

GPT-4 (cl100k_base):
Tokens: ["What", "'s", " the", " capital", " of", " France", "?"]
IDs:    [3923, 596, 279, 6864, 315, 9822, 30]
```

Several non-obvious properties matter in production:

**Token boundaries are not word boundaries.** BPE builds its vocabulary from corpus frequency, so common words become single tokens and rare or foreign words fragment. A surname like "Schwarzenegger" might split into 4–5 tokens. A technical term appearing rarely in training data might fragment where you'd least expect it. This asymmetry is not a bug  -  it's a direct consequence of frequency-driven vocabulary construction.

**Leading spaces are part of tokens.** In GPT-family BPE, `" capital"` (with a leading space) is often a different token than `"capital"`. This is why models are sensitive to formatting  -  a space before a key term changes the token sequence and can subtly shift model behavior.

**Numbers tokenize inconsistently.** Large numbers fragment at boundaries that aren't numerically meaningful. Multi-digit numbers don't have a consistent token split point  -  the tokenizer has no concept of digit significance, only which substrings appeared frequently in training data. Arithmetic is hard partly because the model sees token IDs, not digits.

**Special tokens are injected.** The tokenized sequence is wrapped with model-specific special tokens: beginning-of-sequence markers, role separators, and end-of-sequence markers. The exact format is vendor-specific  -  OpenAI's ChatML format uses `<|im_start|>user`, while Anthropic, Google, and others use different conventions. These tokens are never visible in the UI but consume context budget.

### The tokenization counts don't match what you expect

After tokenization, the system validates the final token count against the requested `max_tokens` and the model's context limit. If input tokens + `max_tokens` exceeds the context window, the request is rejected  -  not silently truncated. This is why production applications must track token usage precisely rather than relying on character counts.

---

## Routing to an inference node

### Model serving infrastructure

Large language models run on clusters of GPUs (typically NVIDIA H100s, A100s, or Google TPUs). Models too large to fit on one device are sharded across many using **tensor parallelism** (splitting individual weight matrices across devices) and/or **pipeline parallelism** (assigning different layers to different devices).

```
Model: 70B parameter Llama
Tensor Parallel across 8x H100 GPUs:

GPU 0: attention head 0-7,   FFN rows 0-N/8
GPU 1: attention head 8-15,  FFN rows N/8-N/4
...
GPU 7: attention head 56-63, FFN rows 7N/8-N

All-reduce synchronization after each layer
```

### Batching and scheduler

The inference scheduler decides which requests to process together. Batching is critical for GPU utilization  -  a single request uses only a fraction of available FLOPS. Modern inference systems (vLLM, TensorRT-LLM, SGLang) use **continuous batching** (also called iteration-level batching): new requests join the active batch at the token level rather than waiting for the current batch to finish. This dramatically improves throughput without sacrificing latency for short sequences.

```
Time →
Seq A: [prefill.........][tok][tok][tok][tok][DONE]
Seq B:          [prefill....][tok][tok][DONE]
Seq C:                  [prefill.......][tok][tok][tok]

Batch at decode step t:  { Seq A token t, Seq B token t, Seq C token t }
```

A newly arrived request enters at the next decode step rather than waiting for the current batch to drain.

---

## KV Cache lookup (prefix caching)

This is one of the most impactful optimizations in production LLM inference  -  and it's almost completely absent from introductory material.

### What the KV cache is

During attention computation, every token attends to every previous token. The intermediate results  -  the **Key** and **Value** matrices for each layer, for each token in the context  -  are computed once during prefill and then reused during every decode step. This is the KV cache.

Without it, generating a 500-token response would require running a full forward pass 500 times, each time recomputing attention over the growing context. With the KV cache, each decode step only needs to compute the new token's K/V vectors and run attention against the cached K/V of everything preceding it.

### Prefix caching

Prefix caching extends this across requests: if two requests share a common prefix (e.g., the same system prompt), the KV cache for that prefix can be reused.

```
Request 1:  [System prompt][History A][User message A]
Request 2:  [System prompt][History B][User message B]
             └──────────────┘
             Shared prefix: KV cache computed once,
             reused for both requests

Cache hit → skip prefill for shared prefix → lower latency, lower cost
```

For high-traffic deployments with a fixed system prompt, prefix cache hit rates above 90% are achievable. This translates directly to reduced time-to-first-token (TTFT) and lower compute cost. Anthropic's prompt caching feature exposes this explicitly to API users.

### KV cache memory management

The KV cache is large. For LLaMA 2 70B  -  80 layers, 64 query heads, 8 KV heads due to Grouped-Query Attention  -  the KV cache for a single 8k-token sequence is approximately 2.5 GB of GPU HBM in FP16. Without GQA (full multi-head attention with 64 KV heads), the same sequence would consume roughly 20 GB. GQA's memory reduction is the main reason it was adopted in production models.

vLLM introduced **PagedAttention** to manage this: KV cache is allocated in fixed-size pages (analogous to virtual memory pages), allowing non-contiguous allocation and reducing fragmentation. This allows serving far more concurrent sequences than naive contiguous allocation.

---

## The prefill phase

When no cached prefix covers the full input, the system runs the **prefill** phase: a single forward pass through the entire transformer stack for all input tokens simultaneously.

This is the expensive part. Compute scales O(n²) in sequence length due to the attention matrix. A 100k-token context is orders of magnitude more expensive than a 1k-token context  -  which is why long-context requests cost dramatically more and why time-to-first-token degrades with context length.

### What happens in a transformer layer (prefill)

For each of the model's N layers (e.g., 80 in LLaMA 2 70B), for each token position:

```
Input embeddings
      │
      ▼
 ┌──────────────────────────────────────────┐
 │  Layer Norm (RMSNorm in LLaMA-family)    │
 └──────────────────────────────────────────┘
      │
      ▼
 ┌──────────────────────────────────────────┐
 │  Multi-Head Self-Attention               │
 │                                          │
 │  Q = X · Wq    (query projection)        │
 │  K = X · Wk    (key projection)          │
 │  V = X · Wv    (value projection)        │
 │                                          │
 │  Attention(Q,K,V) = softmax(QKᵀ/√d_k)·V │
 │  where d_k = key dimension per head      │
 │                                          │
 │  Causal mask: position i cannot attend   │
 │  to position j > i                       │
 └──────────────────────────────────────────┘
      │
      ▼ (residual connection)
 ┌──────────────────────────────────────────┐
 │  Layer Norm (RMSNorm in LLaMA-family)    │
 └──────────────────────────────────────────┘
      │
      ▼
 ┌──────────────────────────────────────────┐
 │  Feed-Forward Network (MLP)              │
 │  Classic: FFN(x) = GELU(x·W1+b1)·W2+b2  │
 │  Modern: FFN(x) = (SiLU(x·Wgate)⊙(x·Wup))·Wdown │
 │  (SwiGLU: 3 weight matrices, no biases)  │
 │  Hidden dim: 4x model dim (classic) or   │
 │  ~2.7x model dim (SwiGLU, to match       │
 │  parameter count with 3 matrices)         │
 └──────────────────────────────────────────┘
      │
      ▼ (residual connection)
 Output to next layer
```

After all N layers, the K and V matrices for every token are stored in the KV cache. The final hidden state at the last token position is projected to a vocabulary-sized logit vector.

### Flash Attention and memory efficiency

Standard attention requires materializing the full n×n attention matrix in GPU HBM. At n=100k: 100,000 × 100,000 × 2 bytes (fp16) ≈ 20 GB  -  well beyond what fits in GPU memory. **FlashAttention** (Dao et al., 2022, with significant improvements in later versions) reorders the computation using tiling: attention is computed in chunks that fit in fast on-chip GPU SRAM, avoiding the HBM round-trip entirely. Long-context inference became practically feasible primarily because of this optimization.

---

## The decode phase (autoregressive generation)

After prefill, the model enters the decode loop  -  generating one token at a time.

```python
for step in range(max_new_tokens):
    logits = model.forward(last_token, kv_cache)
    next_token = sample(logits)
    if next_token == EOS:
        break
    yield next_token
    kv_cache.append(next_token.kv)
```

Each decode step is a forward pass for a single new token, attending to the KV cache of everything preceding it. At batch size 1, this is **memory-bandwidth-bound**: the bottleneck is loading model weights and KV cache from HBM, not the matrix multiplications themselves. At large batch sizes  -  which is how you get throughput in production  -  arithmetic intensity rises and the workload shifts closer to compute-bound. This is why the memory-bandwidth framing is accurate for latency optimization (single user experience) but incomplete for throughput optimization (serving many users concurrently).

Decode throughput is measured in tokens per second. For a 70B model on 8x H100s, throughput for a single sequence is typically in the range of 30–80+ tokens/second, depending on inference framework, quantization, and KV cache pressure.

---

## Sampling and the logit pipeline

The raw output of the final transformer layer is a vector of **logits**  -  one real-valued score per vocabulary token (~32,000 to ~200,000 depending on the model). No word has been chosen yet. The sampling pipeline converts this into a single selected token through a series of filtering and scaling steps.

### The logit pipeline

```
Raw logits (dim: vocab_size)
      │
      ▼
 [Repetition Penalty]
 Penalizes tokens that have appeared in the context.
 One common implementation (e.g., Hugging Face):
   positive logits → divide by penalty factor
   negative logits → multiply by penalty factor
 Both operations shift the token's logit toward zero,
 reducing its selection probability relative to unseen tokens.
      │
      ▼
 [Temperature Scaling]
 logits = logits / temperature
 T < 1.0 → sharper distribution (more deterministic)
 T > 1.0 → flatter distribution (more random)
 T = 0   → argmax (greedy decoding; implemented as special case to avoid division by zero)
      │
      ▼
 [Top-K Filtering] (optional)
 Set all logits not in the top K to -∞ (zero probability after softmax)
      │
      ▼
 [Top-P (Nucleus) Filtering] (optional)
 Keep the smallest set of tokens whose cumulative probability ≥ P
 Dynamically adjusts how many tokens are in the candidate set
      │
      ▼
 [Min-P Filtering] (optional, newer)
 Remove tokens with probability < min_p × max_token_probability
      │
      ▼
 [Softmax]
 probs = softmax(filtered_logits)
 Converts remaining logits to a probability distribution
      │
      ▼
 [Sample]
 Draw one token from the filtered distribution
```

### Tradeoffs of sampling parameters

| Parameter | Low value effect | High value effect | When to tune |
|-----------|-----------------|-------------------|--------------|
| temperature | Deterministic, repetitive | Creative, random, incoherent | Creativity vs. accuracy tasks |
| top_k | Focuses on highest-prob tokens | More diversity | Rarely tuned directly; use top_p |
| top_p | Conservative, predictable | More diverse vocabulary use | Default 0.9–0.95 is usually fine |
| repetition_penalty | No penalty, allows loops | Aggressively avoids repeating tokens | Long generation, documents |

### Greedy vs. sampling: the non-obvious tradeoff

Greedy decoding (temperature=0) is not always better for factual tasks. Because uncertainty is distributed across tokens at every step, always taking the argmax can lead the sequence into a locally likely but globally poor path  -  it's hill-climbing, not global optimization. Beam search keeps B candidate sequences simultaneously and selects the highest-probability complete sequence, which sounds better but has a well-documented failure mode with large generative models: it produces repetitive, degenerate text. It's also 2–5x more expensive. Production systems use temperature sampling with top-p as the standard.

---

## Token is emitted  -  streaming begins

The first token is sent to the client as soon as it's sampled. The server does not wait for the full response. This is where the user sees the first character appear.

### Time to First Token (TTFT)

TTFT is the latency from request submission to first streamed token. It's dominated by:

1. Network RTT to the API gateway
2. Auth + rate limit check
3. Queue wait time (if the system is under load)
4. **Prefill time**  -  the dominant term for long inputs

A 100k-token prefill can take 5–15 seconds on current hardware, during which the user sees nothing. This is why streaming indicators ("Claude is thinking...") are not just UX decoration  -  they're covering a real gap. Long-context features are hard to make feel responsive precisely because prefill time is unavoidable.

### Server-Sent Events encoding

Each token (or small batch of tokens, for efficiency) is UTF-8 encoded and wrapped in an SSE event:

```
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Par"}}

data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"is"}}

data: {"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":42}}

data: [DONE]
```

The event stream is chunked HTTP/1.1 or multiplexed HTTP/2. Each `data:` line is followed by two newlines. The client's SSE parser splits on these delimiters.

### UTF-8 boundary problem

Multi-byte UTF-8 characters (Chinese characters, emoji, accented characters) can be split across token boundaries. The byte sequence for a single character may span two tokens. The server must buffer incomplete byte sequences and emit only complete Unicode codepoints  -  otherwise the client receives malformed UTF-8 that breaks the render.

---

## Tool use / function calling

When the model produces a tool call, the streaming response includes a structured tool-call block, which triggers a multi-step **agentic loop**.

```
┌─────────────────────────────────────────────────────────────┐
│                    TOOL USE LOOP                            │
│                                                             │
│  User message                                               │
│      │                                                      │
│      ▼                                                      │
│  Model generates ──► tool_call: {                           │
│                          name: "web_search",                │
│                          input: {query: "capital France"}   │
│                      }                                      │
│      │                                                      │
│      ▼                                                      │
│  Orchestrator executes tool ──► "Paris is the capital..."   │
│      │                                                      │
│      ▼                                                      │
│  Tool result injected into context:                         │
│      [assistant] <tool_call>...</tool_call>                 │
│      [user]      <tool_result>Paris...</tool_result>        │
│      │                                                      │
│      ▼                                                      │
│  Model generates final response                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Each tool call round-trip is a full new inference request, re-sending the entire context including the tool call and result. Deep agentic pipelines (10+ tool calls) consume enormous context and cost significantly more than a simple chat turn.

### Parallel tool calls

Modern APIs support returning multiple tool calls in a single response, which the orchestrator can execute concurrently before sending all results back in one follow-up request. For tasks requiring multiple independent lookups, this cuts latency significantly.

### Tool result injection and trust

From the model's perspective, tool results are just more tokens. There is no cryptographic guarantee that a tool result is authentic or uncompromised. A malicious web page retrieved by a browsing tool, a crafted document, or a compromised tool server can inject text that attempts to override the model's behavior. This is prompt injection resurfacing in the agentic context  -  and it's harder to defend against here because the "user" content is now machine-generated and arrives at scale.

---

## Output moderation and safety post-screening

The model's response is screened  -  sometimes per-chunk during streaming, sometimes after the full response is buffered.

### Post-generation safety classifiers

Even with training-time alignment (RLHF/RLAIF/Constitutional AI), the model can produce policy-violating outputs in edge cases. A post-generation classifier is a second layer of defense. For streaming responses, the tradeoff is stark:

**Check per-chunk**: Low added latency, but content may have already rendered in the user's browser before a mid-stream violation is detected. The UI must blank or replace already-visible content  -  a bad user experience.

**Buffer then release**: The user sees nothing until the full response passes moderation. Higher TTFT, but clean UX on violation. Some providers use a hybrid: buffer for the first N tokens, then stream, with ongoing background classification.

### Factuality and grounding checks

Some deployments run a post-hoc factuality classifier or groundedness check (verifying model output against retrieved context in RAG pipelines) before returning to the user. This reduces hallucination impact at the cost of added latency.

---

## The response reaches the browser

### Client-side SSE parsing

The browser's native `EventSource` API handles SSE reconnection automatically but is GET-only. Production LLM clients use `fetch()` + `ReadableStream` for POST support, with reconnection logic implemented manually:

```javascript
const response = await fetch('/v1/messages', {
  method: 'POST',
  body: JSON.stringify(payload),
  headers: { 'Accept': 'text/event-stream' }
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  const chunk = decoder.decode(value);
  // parse "data: {...}\n\n" events from chunk
  // dispatch tokens to UI state
}
```

The chunk from `reader.read()` doesn't align with SSE event boundaries. The parser maintains a buffer and splits on `\n\n`. This is fiddlier than it sounds when chunks arrive mid-event.

### Network interruptions

SSE connections drop. Mobile networks change cells. Corporate proxies time out idle connections. The client SDK handles reconnection either by using the `Last-Event-ID` header if the server supports resume, or re-issuing the full request and discarding already-rendered tokens. Neither approach is invisible to the user.

---

## Markdown rendering and streaming display

The response renders as Markdown  -  but it arrives one token at a time, mid-word, which standard Markdown parsers weren't designed for.

### Incremental markdown parsing

A code block fence (` ``` `) may have been opened but not yet closed. A table row may be half-formed. Production LLM UIs work around this with a combination of approaches:

- Buffer tokens until a structural Markdown element is complete (e.g., wait for the closing ` ``` ` before rendering a code block as formatted HTML)
- Use optimistic rendering with re-flow when the closing delimiter arrives
- Fall back to rendering raw text for in-progress structural elements

### The blinking cursor

The typing cursor at the active position in the response is typically a CSS animation on a `::after` pseudo-element on the last rendered text node (or an inline `<span>` with `border-right`). It's removed when the `[DONE]` event arrives.

### Code block syntax highlighting

Highlighting streaming code is particularly awkward: the language is declared in the opening fence (` ```python `), but highlighting requires the full token stream. Libraries like Prism, Shiki, or highlight.js re-highlight the partial code block on each token arrival. At scale  -  many concurrent chats, long code responses  -  this is non-trivial browser CPU load.

---

## The final token arrives

### Stop conditions

Generation terminates when any of the following occur:

1. The model produces the `<EOS>` special token (`stop_reason: "end_turn"`)
2. A configured stop sequence is generated (e.g., `"\nHuman:"` in legacy prompt formats) (`stop_reason: "stop_sequence"`)
3. The `max_tokens` budget is exhausted (`stop_reason: "max_tokens"`)
4. The model produces a tool call, stopping to yield to the orchestrator (`stop_reason: "tool_use"`)
5. A long-running agentic turn is paused (`stop_reason: "pause_turn"`)
6. A safety refusal is triggered (`stop_reason: "refusal"`)

When `max_tokens` is hit, the response is truncated mid-generation. Well-designed clients surface this explicitly  -  a silently cut-off response is a common source of user confusion.

### Usage accounting

The server calculates and returns final token counts:

```json
"usage": {
  "input_tokens": 847,
  "output_tokens": 312,
  "cache_read_input_tokens": 720,
  "cache_creation_input_tokens": 0
}
```

The distinction between `cache_read_input_tokens` and regular `input_tokens` matters for billing: tokens served from the prefix cache are significantly cheaper. Cache read prices are typically around 0.1x base input price. Cache write prices are higher than base input (roughly 1.25x–2x depending on TTL). Output tokens are priced higher than input tokens (typically 4–5x) because the decode phase is slower and more resource-intensive than prefill.

---

## Billing, logging, and observability

### Token counting and cost calculation

After the request completes, token counts are written to a billing aggregation service. The cost formula:

```
cost = (input_tokens × input_price_per_MTok)
     + (output_tokens × output_price_per_MTok)
     + (cache_creation_tokens × cache_write_price_per_MTok)
     + (cache_read_tokens × cache_read_price_per_MTok)
```

### Logging and replay

The full request and response are typically logged for:
- **Abuse detection**: Identifying policy violations after the fact
- **Fine-tuning data**: High-quality production conversations are valuable training signal
- **Debugging**: Reproducing issues reported by users
- **Billing disputes**: Audit trail

Logs are stored in encrypted, append-only stores with retention policies governed by the provider's data policy and enterprise contracts.

### Observability for developers

Production LLM applications emit traces (OpenTelemetry or custom), structured logs, and metrics. The key metrics and what they actually reveal:

| Metric | What it reveals |
|--------|----------------|
| TTFT (time to first token) | Prefill latency, queue depth, cache hit rate |
| TPOT (time per output token) | Decode throughput, KV cache pressure |
| Total latency | End-to-end response time |
| Input/output token ratio | Whether prompts are efficient |
| Cache hit rate | System prompt stability, cost optimization |
| Error rate by type | Rate limit pressure, content policy trends |
| Tool call depth | Agentic pipeline complexity, runaway agents |

---

## Contributing

This document covers the main path through a text-only chat interaction. Several major subsystems aren't covered yet:

- **Multimodal inputs** (image tokenization via ViT patch embeddings, audio)
- **Extended thinking / reasoning traces** (chain-of-thought with scratchpad)
- **Retrieval-augmented generation** (embedding, vector search, re-ranking, context stuffing)
- **Model training pipeline** (pretraining, RLHF, Constitutional AI, RLAIF)
- **Speculative decoding** (using a draft model to propose tokens verified by the main model)
- **Model quantization** (INT8/INT4 inference, GGUF formats)
- **Federated and on-device inference** (Apple Intelligence, on-device Gemini Nano)
- **Multi-agent coordination** (how orchestrators manage networks of agents)
- **Evaluation and red-teaming pipelines**

If you have production experience in any of these areas, please contribute.

---

## License

[Creative Commons Zero](https://creativecommons.org/publicdomain/zero/1.0/)  -  public domain.
