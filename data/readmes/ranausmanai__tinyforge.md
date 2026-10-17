<div align="center">

# 🔥 tinyforge

**A tiny model that teaches itself to get better — at anything with a test.**
**On your laptop. 6GB RAM. No cloud. No teacher model. No human feedback.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Apple Silicon](https://img.shields.io/badge/Apple_Silicon-M1/M2/M3/M4-000000?style=for-the-badge&logo=apple&logoColor=white)](https://support.apple.com/en-us/HT211814)
[![MLX](https://img.shields.io/badge/MLX-Framework-F97316?style=for-the-badge)](https://github.com/ml-explore/mlx)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![RAM](https://img.shields.io/badge/RAM-6GB-a855f7?style=for-the-badge)]()

*We discovered that a **0.8B parameter model** can meaningfully improve itself by learning from its own failures — using only **6GB of RAM** on a MacBook Air. We proved it on code. The technique works anywhere you can automatically verify the output.*

</div>

<br/>

```bash
pip install -e .
tinyforge --model models/mlx-q4-qwen35-08b --quick
```

<br/>

## 🧠 What this actually does

The model tries to solve coding problems. It fails. It sees *exactly* what failed (which test, what input, what it expected vs what it got). It tries again. When it finds a better solution, we extract the weak-to-strong pair and train the model on it.

> **This is self-play for code. The "game" is passing tests.**

<br/>

<div align="center">

<img src="docs/architecture.svg" alt="tinyforge architecture" width="100%"/>

</div>

<br/>

## 📊 Key Results

> All results are on **fresh holdout slices** the model never saw during training.

### 🔧 The repair training effect

*Fresh HumanEval slice 40-47:*

| Setup | Public Tests | Hidden HumanEval+ |
|:---|---:|---:|
| Base model, single-pass | 16/50 | 2/8 |
| **Repair-trained, single-pass** | **28/50** | **4/8** |
| Base model + evolutionary search | 42/50 | 5/8 |
| **Repair-trained + evolutionary search** | **44/50** | **6/8** |

> 📈 **Single-pass improved 75%** (16 → 28) just from training on 13 self-generated repair pairs.

### 🔄 The feedback loop effect

*Fresh HumanEval slice 56-63 (overnight run):*

| Setup | Public Tests | Hidden HumanEval+ |
|:---|---:|---:|
| Base adapter + feedback loop | 42/58 | 4/8 |
| **Repair-trained + feedback loop** | **47/58** | **5/8** |

> 💡 The trained model doesn't just write better code — it becomes a **better participant in the repair loop**. It learns how to fix code when told what's wrong.

### 🏔️ Hard problems (slice 72-79)

| Setup | Public Tests | Hidden HumanEval+ |
|:---|---:|---:|
| Base model, single-pass | 28/70 | 0/8 |
| **Repair-trained + search + feedback** | **53/70** | **3/8** |

> From **0/8 to 3/8** on the hardest unseen problems. Not magic. But real.

<br/>

## 🔬 What We Discovered

| # | Discovery | Details |
|:---:|:---|:---|
| 🖥️ | **Fine-tune on a laptop** | QLoRA + LoRA rank 4 on 4-bit Qwen3.5-0.8B. Peak: 6.5-13GB. Runs on a MacBook Air M4. |
| 🔧 | **Repair > final-answer training** | "Here's broken code, fix it" works better than "here's the problem, here's the answer." Small models learn fixing patterns, not memorized solutions. |
| 🧬 | **Evolutionary search = biggest jump** | Generate multiple attempts, test them, keep the best, mutate using failure feedback. This is where most gains come from. |
| 🎯 | **Specific failure feedback matters** | `input=[15] expected='FizzBuzz' got='Fizz'` helps more than `3/6 tests passed`. Evidence > scores. |
| 🤝 | **Model learns to be a repair partner** | Biggest overnight finding: the trained model writes much better code *inside the feedback loop*. It learned how to respond to test failures. |
| ⚠️ | **More compute ≠ better results** | Wider search, colder sampling, extra generalization — we tried them. They didn't reliably help. |

<br/>

## ⚡ Quick Start

### Requirements

- 🍎 macOS with Apple Silicon (M1/M2/M3/M4)
- 💾 8GB+ RAM (16GB+ recommended)
- 🐍 Python 3.10+

### Install

```bash
git clone https://github.com/ranausmanai/tinyforge.git
cd tinyforge
pip install -e .
pip install mlx-lm pyyaml
```

### Download a base model

```bash
# Quantized Qwen3.5-0.8B (smallest, ~400MB)
python -c "from mlx_lm import load; load('mlx-community/Qwen2.5-Coder-0.5B-Instruct-4bit')"
```

Or convert the model we trained on:

```bash
python -m mlx_lm.convert \
  --hf-path Qwen/Qwen3.5-0.8B \
  --mlx-path models/mlx-q4-qwen35-08b \
  -q --q-bits 4
```

### Run

```bash
# ⚡ Quick demo (~5-10 minutes, 5 tasks)
tinyforge --model models/mlx-q4-qwen35-08b --quick

# 🔥 Full run (~45-60 minutes, 20 tasks)
tinyforge --model models/mlx-q4-qwen35-08b
```

### What you'll see

```
🔥 tinyforge
   A model teaching itself to code better.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 BEFORE (single-pass baseline)
   [1/5] fizzbuzz ............ 4/6
   [2/5] valid_parens ........ 2/5
   ...

🧬 EVOLVING (search + feedback)
   [1/5] fizzbuzz ............ 6/6  ✓  (gen=2)
   ...

🎓 TRAINING on 8 self-generated repair pairs
   Mixing with 40 rehearsal samples...
   Training for 20 iterations...

🏁 AFTER (trained model + search)
   [1/5] fizzbuzz ............ 6/6  ✓
   ...

   Before:  12/26  ████░░░░░░  46%
   Search:  22/26  ████████░░  85%
   After:   24/26  █████████░  92%
```

### Use with your own adapter

```bash
tinyforge --model models/mlx-q4-qwen35-08b --adapter outputs/biolora6g/grow
```

<br/>

## ⚙️ How It Works

### 🧬 The evolutionary loop

For each coding task:

1. **🌱 Seed** — Generate `population_size` candidate solutions
2. **🧪 Evaluate** — Run each candidate against test cases in a sandboxed subprocess
3. **🏆 Select** — Keep the top `elites` unique solutions
4. **🔀 Mutate** — Generate new candidates using failure feedback from the best parents
5. **🔁 Repeat** for `generations` rounds
6. **✅ Return** the best solution found

### 🔧 Repair pair extraction

After evolution, we pair weak solutions with strong ones:

```
Weak (3/6 tests):                    Strong (6/6 tests):
def fizzbuzz(n):                     def fizzbuzz(n):
    if n % 3 == 0: return "Fizz"         if n % 15 == 0: return "FizzBuzz"
    if n % 5 == 0: return "Buzz"         if n % 3 == 0: return "Fizz"
    return str(n)                        if n % 5 == 0: return "Buzz"
                                         return str(n)
```

The training prompt includes the weak code + test failures. The training target is the strong code. The model learns: *"when you see this kind of failure, fix it like this."*

### 🎓 Training

| Parameter | Value |
|:---|:---|
| Method | MLX LoRA (4-bit quantized base + low-rank adapters) |
| LoRA rank | 4 (extremely small — adds minimal parameters) |
| Optimizer | Adafactor (memory-efficient) |
| Data | Self-generated repair pairs + rehearsal data (prevents forgetting) |
| Iterations | 40 (~2-3 minutes) |
| Peak memory | 6.5-13GB depending on sequence length |

<br/>

## 📝 Custom Tasks

Create a JSONL file with your own tasks:

```jsonl
{"id": "add", "type": "code", "prompt": "Write a function add(a, b) that returns the sum", "entry_point": "add", "tests": [{"input": [1, 2], "expected": 3}, {"input": [-1, 1], "expected": 0}]}
```

```bash
tinyforge --model my-model --tasks my_tasks.jsonl
```

See `examples/` for more task formats.

<br/>

## 📁 Project Structure

```
src/finetuneqwen/
  tinyforge/                          # 🔥 The self-improvement engine
    cli.py                            # Main CLI & demo experience
    evolve.py                         # Evolutionary search
    verify.py                         # Test verification (sandboxed)
    extract.py                        # Repair pair extraction
    builtin_tasks.py                  # 20 built-in coding problems
    task.py                           # Task definition

  # 🔬 Original research pipeline
  humaneval_evolutionary_eval.py      # HumanEval-specific evolutionary eval
  export_humaneval_repair_pairs.py    # HumanEval repair data extraction
  train_qlora.py                      # PyTorch QLoRA training
  prepare_data.py                     # Dataset preparation

configs/                              # MLX training configs
scripts/                              # Shell scripts for experiments
data/                                 # Training data (repair pairs, rehearsal)
examples/                             # Example task files
results/                              # Evaluation summaries
```

<br/>

## 🔁 Reproduce Our Results

### Best result (repair-v1, slice 40-47)

```bash
# Evolutionary search with base adapter
bash scripts/50_humaneval_evo.sh \
  models/mlx-q4-qwen35-08b \
  outputs/biolora6g/grow \
  results/humaneval_repair_v1 \
  8 40 4 3 2 0.6 1337 base_evo_40_47 1

# With repair adapter
bash scripts/50_humaneval_evo.sh \
  models/mlx-q4-qwen35-08b \
  outputs/humaneval_repair_v1/adapter \
  results/humaneval_repair_v1 \
  8 40 4 3 2 0.6 1337 repair_evo_40_47 1
```

### Build repair training data

```bash
bash scripts/60_humaneval_build_repair_v1.sh
```

### Train repair adapter

```bash
python -m mlx_lm.lora \
  --model models/mlx-q4-qwen35-08b \
  --data data/humaneval_repair_v1/mlx \
  --config configs/biolora6g/humaneval_repair_v1_qwen35_08b.yaml \
  --adapter-path outputs/humaneval_repair_v1/adapter \
  --resume-adapter-file outputs/biolora6g/grow/adapters.safetensors
```

<br/>

## 🤔 Honest Limitations

- 🚫 This is **not** a magic one-shot model. The gains come from the system (model + search + feedback), not from the model alone.
- 📏 Tested on HumanEval slices, not full benchmarks. Results are real but scoped.
- 📈 Transfer is stronger on harder problems and weaker on easy ones (where the base model is already decent).
- 🐜 A 0.8B model will never match GPT-4. **That's not the point.**

<br/>

## 🌍 Why This Matters

> If a 0.8B model can teach itself to code better on a laptop with 6GB RAM — what happens when you run this technique on a 7B model? A 70B model? With a real GPU cluster?

The **technique** is the contribution, not the model size.

Self-play works for Go *(AlphaGo)*. Self-play works for math *(AlphaProof)*. We're showing it works for **code**, on hardware anyone can afford.

<br/>

## 🌐 Beyond Code — Where This Technique Applies

The core loop is simple: **generate something → check if it's good → learn from what went wrong → try again.** We proved it on code. But it works anywhere you can measure whether the output is right or wrong.

### For engineers & researchers

| Domain | What's the "test"? |
|:---|:---|
| 🗃️ **SQL queries** | Run the query, check if the results match |
| 🔢 **Math proofs** | Verify the proof mechanically (Lean, Coq, SymPy) |
| ⚡ **Chip design (Verilog/VHDL)** | Simulate the circuit against test benches |
| 🧪 **Drug molecules** | Check properties via physics simulation |
| 🔐 **Security testing** | Did the generated input crash the software? |
| 🤖 **Robotics** | Run the policy in simulation, measure the score |
| 📊 **Data pipelines / ETL** | Input data in, expected data out — compare |

### For marketers, creators & everyone else

| Domain | What's the "test"? |
|:---|:---|
| 📣 **Ad copy** | A/B test it — did people click? Click rate is automatic feedback |
| 📧 **Email outreach** | Did they open? Did they reply? Open/reply rate = the verifier |
| 🔎 **SEO content** | Did it rank? Did it get traffic? Google tells you |
| 🛒 **Product descriptions** | Conversion rate — did people buy? |
| 📱 **Social media posts** | Engagement. Likes, shares, saves — all measurable |
| 🎓 **Teaching / tutoring** | Did the student get the next question right? |
| ✍️ **Headlines & hooks** | Scroll-stop rate. You already track this |

> **The idea:** if you can score the output — even roughly — the model can learn from its own mistakes. No labeled dataset needed. No expert in the loop. The model makes its own training data by failing and fixing.

### 🔑 What you need

1. **A task** — what you want the model to produce
2. **A way to check** — any script/metric that says "good" or "bad" (and ideally, why)
3. **A small model** — even 0.8B parameters is enough to start

That's it. The model teaches itself. On your laptop. Your data never leaves your machine.

<br/>

## 📦 Resource Envelope

| Phase | Peak Memory | Time (MacBook Air M4) |
|:---|:---|:---|
| 🧬 Evolutionary search (8 tasks) | ~4GB | ~10 min |
| 🔧 Repair pair extraction | ~100MB | seconds |
| 🎓 LoRA training (40 iters) | 6.5-13GB | ~3 min |
| 🔥 Full tinyforge demo (5 tasks) | ~10GB | ~8 min |

<br/>

## 📄 License

MIT — do whatever you want with it.

<br/>

## 📖 Citation

If you use this technique in your work:

```bibtex
@misc{tinyforge2025,
  title   = {tinyforge: Self-improving tiny language models through test-driven repair training},
  author  = {Usman Muhammad},
  year    = {2025},
  url     = {https://github.com/ranausmanai/tinyforge}
}
```

<br/>

<div align="center">

---

**Built with 🔥 on a MacBook Air M4 with 24GB RAM**

*No GPUs were harmed in the making of this project.*

</div>
