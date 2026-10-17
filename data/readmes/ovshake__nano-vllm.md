# nano-vllm

<p align="center">
  <img src="assets/logo.png" alt="nano-vllm logo" width="600">
</p>

A minimalistic, educational implementation of a high-performance LLM inference engine, inspired by [vLLM](https://github.com/vllm-project/vllm).

**Learn how LLM inference really works** - from tokenization to generation, with real-time visualizations and interactive tutorials.

```
┌─────────────────────────────────────────────────────────────────┐
│                    LLaMA Architecture                           │
├─────────────────────────────────────────────────────────────────┤
│  Input: "The capital of France is"                              │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────┐                                            │
│  │   Tokenizer     │  "The" → 450, "capital" → 7483, ...        │
│  └────────┬────────┘                                            │
│           ▼                                                     │
│  ┌─────────────────┐                                            │
│  │   Embedding     │  450 → [0.12, -0.34, 0.87, ...]  (4096-d)  │
│  └────────┬────────┘                                            │
│           ▼                                                     │
│  ╔═════════════════╗                                            │
│  ║  Decoder Layer  ║ ×32 layers                                 │
│  ║  ┌───────────┐  ║                                            │
│  ║  │ Attention │◄─╬──── KV Cache                               │
│  ║  └─────┬─────┘  ║                                            │
│  ║  ┌───────────┐  ║                                            │
│  ║  │    FFN    │  ║                                            │
│  ║  └───────────┘  ║                                            │
│  ╚═════════════════╝                                            │
│           ▼                                                     │
│      "Paris" (87%)                                              │
└─────────────────────────────────────────────────────────────────┘
```

## Features

### Core Inference Engine
- **Continuous Batching**: Process multiple requests simultaneously with iteration-level scheduling
- **PagedAttention**: Memory-efficient KV cache management (like OS virtual memory)
- **FlashAttention**: IO-aware fused attention for faster computation
- **Grouped Query Attention (GQA)**: Efficient attention with shared KV heads

### Advanced Scheduling
- **Priority Scheduling**: Process high-priority requests first
- **Preemption**: Pause low-priority requests for urgent ones
- **Chunked Prefill**: Break long prompts into manageable chunks
- **Prefix Caching**: Share KV cache blocks for common prefixes

### Optimizations
- **Speculative Decoding**: Use a draft model to speed up generation
- **Block-based Memory Management**: Zero memory waste with on-demand allocation

### Educational Modes
- **Narrator Mode**: Real-time plain-English explanations
- **X-Ray Mode**: Visualize tensor shapes and math operations
- **Dashboard Mode**: Live terminal UI with progress tracking
- **Tutorial Mode**: Interactive step-by-step learning experience

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/nano-vllm.git
cd nano-vllm

# Install in development mode
pip install -e .

# For dashboard mode (optional)
pip install -e ".[educational]"
```

### Requirements
- Python 3.10+
- PyTorch 2.0+
- transformers
- safetensors
- rich (optional, for dashboard mode)
- flash-attn (optional, for FlashAttention)

---

## Quick Start

### Basic Generation

```bash
# Single prompt
python -m nano_vllm.cli --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
    --prompt "The capital of France is"

# Multiple prompts (continuous batching)
python -m nano_vllm.cli --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
    --prompt "The capital of France is" \
    --prompt "The largest planet is" \
    --prompt "Python is a"
```

### Priority Scheduling

```bash
python -m nano_vllm.cli --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
    --prompt "Low priority task" --priority 1 \
    --prompt "High priority task" --priority 10
```

### Speculative Decoding

```bash
python -m nano_vllm.speculative.cli \
    --target-model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
    --draft-model TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
    --prompt "The future of AI is" \
    --num-speculative-tokens 5
```

---

## Educational Modes

nano-vllm includes four educational modes that help you understand what happens inside an LLM during inference. It's like watching surgery with an expert explaining each step!

### 1. Narrator Mode (`--narrate`)

Real-time plain-English commentary explaining each step as it happens.

```bash
python -m nano_vllm.cli --prompt "Hello world" --narrate
```

**What you'll see:**

```
═══════════════════════════════════════════════════════════════════
  🎓 INFERENCE ANATOMY - Educational Mode
  Understanding what happens inside an LLM
═══════════════════════════════════════════════════════════════════

📖 Prompt: "The capital of France is"
🤖 Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0

🎬 ACT 1: TOKENIZATION
┌─────────────────────────────────────────────────────────────┐
│ Converting your prompt into numbers the model understands... │
└─────────────────────────────────────────────────────────────┘
  "The capital of France is"
       ↓ Tokenizer (BPE algorithm)
  [The] [capital] [of] [France] [is] → [450, 7483, 310, 3444, 338]

  💡 WHY TOKENS? LLMs don't read text - they process numbers.

🎬 ACT 2: PREFILL PHASE (The "Reading" Phase)
┌─────────────────────────────────────────────────────────────┐
│ The model reads your entire prompt at once...                │
└─────────────────────────────────────────────────────────────┘

🎬 ACT 3: DECODE PHASE (Token-by-Token Generation)
  Step 1: Predicting token #6
  │   Top 5 predictions:
  │   ┌──────────────┬───────────┐
  │   │ Paris        │ 87.3%  ██████████ │
  │   │ the          │  4.2%  █          │
  │   │ Lyon         │  1.8%  ░          │
  │   └──────────────┴───────────┘
  └── 🎲 Sampled: "Paris"
```

The narrator explains:
- **Tokenization**: How text becomes numbers
- **Embedding**: How token IDs become vectors
- **Prefill**: How the model "reads" the prompt
- **Attention**: How tokens communicate
- **KV Cache**: Why caching matters
- **Decode**: How tokens are generated one by one
- **Sampling**: How the next token is chosen

---

### 2. X-Ray Mode (`--xray`)

Shows the actual mathematics and tensor operations happening during inference.

```bash
python -m nano_vllm.cli --prompt "Hello" --xray
```

**What you'll see:**

```
╔══════════════════════════════════════════════════════════════╗
║  X-RAY: Layer 1 - Q/K/V Projections                          ║
╚══════════════════════════════════════════════════════════════╝

Step 1: Project to Q, K, V
────────────────────────────────

  hidden_states: [1, 5, 4096]
       (batch=1, seq=5, hidden=4096)

       ↓ Linear projections (learned weights)

  Q: [1, 32, 5, 128]  (32 heads, each 128 dims)
  K: [1, 8, 5, 128]   (8 KV heads for GQA)
  V: [1, 8, 5, 128]

  💡 GQA: 32 Q heads share 8 KV heads (4:1)
     Memory saving: 4x less KV cache!

Step 2: Compute Attention Scores
─────────────────────────────────
  scores = Q @ K^T / √128

  [1,32,5,128] @ [1,32,128,5] → [1,32,5,5]
       Q           K^T           scores
```

X-Ray mode shows:
- Tensor shapes at each step
- Matrix multiplication dimensions
- Memory calculations
- GQA head sharing
- Numerical examples from running inference

---

### 3. Dashboard Mode (`--dashboard`)

A rich terminal UI with live-updating visualizations (requires `rich` library).

```bash
pip install rich
python -m nano_vllm.cli --prompt "Hello" --dashboard
```

**What you'll see:**

```
╭─────────────────── nano-vllm Inference Dashboard ───────────────────╮
│                                                                      │
│  Model: TinyLlama-1.1B    Device: CUDA    Dtype: float16            │
│                                                                      │
│  ┌─ Progress ──────────────────────────────────────────────────┐    │
│  │ Phase:    📖 PREFILL                                        │    │
│  │ Prefill:  ████████████████████████████████████████░░░░ 85%  │    │
│  │ Layer:    ████████████████░░░░░░░░░░░░░░░░░░░░░░░░ 12/32   │    │
│  │ Decode:   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0/50    │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌─ Memory ──────────┐  ┌─ Throughput ─────────────┐                │
│  │ KV Cache: 24.5MB  │  │ Prefill: 1,234 tok/s     │                │
│  │ ████████░░ 80%    │  │ Decode:    42 tok/s      │                │
│  │ Blocks: 156/200   │  │ Total:    847 tok/s      │                │
│  └───────────────────┘  └──────────────────────────┘                │
│                                                                      │
│  ┌─ Generated Text ──────────────────────────────────────────────┐  │
│  │ The capital of France is Paris.█                               │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌─ Top Predictions ─────────────────────────────────────────────┐  │
│  │ Paris    87.3%  ████████████████████████████████████          │  │
│  │ the       4.2%  ████                                          │  │
│  │ a         2.1%  ██                                            │  │
│  └────────────────────────────────────────────────────────────────┘  │
╰──────────────────────────────────────────────────────────────────────╯
```

Dashboard displays:
- **Progress**: Phase, layer, and decode progress bars
- **Memory**: KV cache usage and block allocation
- **Throughput**: Tokens per second metrics
- **Generated Text**: Live token generation
- **Predictions**: Top-k token probabilities

---

### 4. Tutorial Mode (`--tutorial`)

An interactive, step-by-step guided tour with explanations and quizzes.

```bash
python -m nano_vllm.cli --tutorial
```

**What you'll experience:**

```
═══════════════════════════════════════════════════════════════════
  🎓 NANO-VLLM INTERACTIVE TUTORIAL
  Understanding LLM Inference from the Inside Out
═══════════════════════════════════════════════════════════════════

This tutorial has 12 chapters covering:

Chapter 1: Tokenization
Chapter 2: Embedding Lookup
Chapter 3: Self-Attention
Chapter 4: Prefill Phase
Chapter 5: KV Cache
Chapter 6: Decode Phase
Chapter 7: Sampling
Chapter 8: PagedAttention
...

[Press Enter to continue...]

───────────────────────────────────────────────────────────────────
  CHAPTER 3: Self-Attention
───────────────────────────────────────────────────────────────────

Self-attention lets each position 'attend' to all previous positions...

🧠 POP QUIZ:
  Why is the attention mask 'causal' (triangular)?
    [A] To save memory
    [B] So tokens can only see past tokens, not future
    [C] To make computation faster
    [D] Because GPUs prefer triangular matrices

Your answer: _
```

The tutorial covers:
- Model architecture overview
- Tokenization and embeddings
- Self-attention mechanism
- Prefill vs decode phases
- KV cache optimization
- Sampling strategies
- PagedAttention memory management

---

### Combining Modes

You can combine educational modes for a richer learning experience:

```bash
# Narrator + X-Ray: See explanations AND tensor math
python -m nano_vllm.cli --prompt "Hello" --narrate --xray

# All three visualization modes
python -m nano_vllm.cli --prompt "Hello" --narrate --xray --dashboard
```

---

## Project Structure

```
nano_vllm/
├── __init__.py
├── config.py              # ModelConfig dataclass
├── cache.py               # KV cache implementations
├── sampler.py             # Token sampling (greedy, top-k, etc.)
├── engine.py              # Main inference engine
├── cli.py                 # Command-line interface
│
├── core/
│   ├── sequence.py        # Sequence abstraction
│   ├── scheduler.py       # Priority scheduler with preemption
│   ├── block.py           # Block abstraction for PagedAttention
│   └── block_manager.py   # KV cache block management
│
├── attention/
│   ├── paged_attention.py # PagedAttention implementation
│   └── flash_attention.py # FlashAttention integration
│
├── speculative/
│   ├── speculative_decoding.py  # Speculative decoding engine
│   └── cli.py             # CLI for speculative decoding
│
├── educational/           # 🎓 Educational visualization system
│   ├── narrator.py        # Plain-English explanations
│   ├── xray.py            # Tensor/math visualizations
│   ├── dashboard.py       # Rich terminal UI
│   ├── tutorial.py        # Interactive tutorial
│   ├── visualizers.py     # ASCII art generators
│   ├── explanations.py    # Educational text content
│   └── educational_engine.py  # Engine with educational hooks
│
└── model/
    ├── loader.py          # HuggingFace weight loading
    └── llama.py           # LLaMA model implementation
```

---

## Key Concepts Explained

### PagedAttention

Traditional inference pre-allocates KV cache for maximum sequence length, wasting memory:

```
Traditional: Pre-allocate max_length for each sequence
┌────────────────────────────────────────────────────┐
│ Seq A: █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  (1/32 used) │
│ Seq B: █████████░░░░░░░░░░░░░░░░░░░░░░░░  (9/32 used) │
└────────────────────────────────────────────────────┘
                    ↓
PagedAttention: Allocate blocks on-demand
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ B0 │ B1 │ B2 │ B3 │ B4 │ B5 │ B6 │ B7 │
│████│████│░░░░│████│████│░░░░│████│░░░░│
└────┴────┴────┴────┴────┴────┴────┴────┘
  ▲    ▲         ▲    ▲         ▲
  └────┴─────────┴────┴─────────┘
     Seq A           Seq B
   (2 blocks)      (3 blocks)
```

### Continuous Batching

Unlike static batching that waits for all sequences to finish:

```
Static Batching:
[Seq A ████████████████████]
[Seq B ██████████          ]  ← Seq B waits for A
[Seq C ████                ]  ← Seq C waits for A

Continuous Batching:
[Seq A ████████████████████]
[Seq B ██████████][Seq D ██████████]  ← D joins when B finishes
[Seq C ████][Seq E ██████████████████]  ← E joins when C finishes
```

### KV Cache

Without caching, attention recomputes K,V for all tokens every step (O(n²)).
With caching, we only compute K,V for new tokens (O(n)):

```
WITHOUT CACHE:
Step 1: Process [The]                    → 1 token
Step 2: Process [The][capital]           → 2 tokens
Step 3: Process [The][capital][of]       → 3 tokens
Total: 1+2+3+...+n = O(n²)

WITH CACHE:
Prefill: Process all tokens once         → n tokens
Decode:  Only process NEW token          → 1 token each
Total: n + 1 + 1 + ... = O(n)
```

---

## CLI Options

```bash
python -m nano_vllm.cli --help
```

| Option | Description |
|--------|-------------|
| `--model` | HuggingFace model ID or local path |
| `--prompt` | Input prompt (can specify multiple) |
| `--max-tokens` | Maximum tokens to generate (default: 50) |
| `--device` | Device to run on (cuda/cpu) |
| `--dtype` | Data type (float16/float32/bfloat16) |
| `--priority` | Request priority (higher = more important) |
| `--scheduling-policy` | fcfs or priority (default: priority) |
| `--max-prefill-tokens` | Chunked prefill budget (default: 512) |
| `--no-paged-attention` | Disable PagedAttention |
| `--no-flash-attn` | Disable FlashAttention |
| `--no-prefix-caching` | Disable prefix caching |
| `--show-memory-stats` | Show memory statistics |
| **Educational** | |
| `--narrate` | Enable narrator mode |
| `--xray` | Enable X-Ray mode |
| `--dashboard` | Enable dashboard mode |
| `--tutorial` | Run interactive tutorial |

---

## Development

### Running Tests

```bash
pytest tests/
```

### Running Benchmarks

**Advanced Scheduling Benchmarks** - Tests priority scheduling, preemption, chunked prefill, and prefix caching (requires GPU):

```bash
# Run all advanced scheduling benchmarks
python -m benchmarks.benchmark_advanced_scheduling --all

# Run specific benchmarks
python -m benchmarks.benchmark_advanced_scheduling --priority
python -m benchmarks.benchmark_advanced_scheduling --preemption
python -m benchmarks.benchmark_advanced_scheduling --chunked-prefill
python -m benchmarks.benchmark_advanced_scheduling --prefix-caching
```

**Scheduler Unit Benchmarks** - Fast benchmarks for scheduler logic (no GPU required):

```bash
python -m benchmarks.benchmark_scheduler_unit
```

**Comparison Benchmarks** - Compare nano-vllm vs HuggingFace Transformers:

```bash
python -m benchmarks.benchmark_comparison
```

---

## References

- [vLLM Paper: Efficient Memory Management for Large Language Model Serving](https://arxiv.org/abs/2309.06180)
- [FlashAttention Paper](https://arxiv.org/abs/2205.14135)
- [PagedAttention Blog Post](https://blog.vllm.ai/2023/06/20/vllm.html)
- [vLLM Repository](https://github.com/vllm-project/vllm)

---

## License

MIT License - feel free to use this for learning and experimentation!

---

## Contributing

Contributions are welcome! This is an educational project, so clarity and documentation are prioritized over raw performance.

Areas for contribution:
- Additional educational explanations
- More visualization modes
- Support for more model architectures
- Performance optimizations with educational documentation
