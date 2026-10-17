# Tiny LLM Reasoning-RL Lab

Train a 41,328-parameter decoder-only transformer on a fixed two-step arithmetic
task. It generates character tokens autoregressively. Supervised initialization
is followed by group-relative REINFORCE-style updates with a KL penalty. It runs
on CPU.

## One example

The prompt asks the model to add first, then multiply:

```text
Q:2+3,*2
A:
```

The target completion is generated one character at a time:

```text
2+3=5;5*2=10;10
```

Python verifies that `2 + 3 = 5`, that `5 * 2 = 10`, and that the final answer
is `10`. A fully correct trace receives reward `1.0`: `0.10` for valid format,
`0.25` for correct addition, `0.35` for correct multiplication, and `0.30` for
the correct final answer.

## Level 1 — Run it

Predict whether 30 RL updates will increase exact-answer accuracy.

### macOS or Linux

```bash
git clone https://github.com/vukrosic/tiny-reasoning-rl-lab.git && cd tiny-reasoning-rl-lab && ./first_win.sh
```

### Windows PowerShell

```powershell
git clone https://github.com/vukrosic/tiny-reasoning-rl-lab.git; cd tiny-reasoning-rl-lab; .\first_win.bat
```

Already inside the repository? Run only `./first_win.sh` or `.\first_win.bat`.

The first run downloads CPU PyTorch. Later runs train, evaluate, save a JSON
receipt and PNG, and open the PNG in about five seconds on the development Mac.

One seeded macOS reference run:

```text
Before RL: 42% exact answers
After RL:  58% exact answers
```

Verified-trace accuracy changed from 6% to 20%. Training took 4.79 seconds.

Your numbers can differ across computers. Report the result from your own JSON
receipt.

## Level 2 — Change one number

Compare two group sizes while holding the other settings fixed.

```bash
./experiment.sh --group-size 2 --image results/group2.png --receipt results/group2.json
./experiment.sh --group-size 8 --image results/group8.png --receipt results/group8.json
```

Windows: use `experiment.bat` with the same parameters.

Before running, write:

```text
I predict group size ___ will produce higher exact-answer accuracy because ___.
```

Then compare the two PNGs and JSON receipts. Keep everything except group size
fixed.

One seeded macOS reference run:

| Group size | Before RL | After RL |
|---:|---:|---:|
| 2 | 42% | 42% |
| 8 | 42% | **58%** |

## Level 3 — Write a reward

Open `student_reward.py` and implement:

```text
Return 1 if the final generated number is correct.
Return 0 otherwise.
```

Check your code:

```bash
.venv/bin/python check_my_reward.py
```

Windows:

```powershell
.venv\Scripts\python.exe check_my_reward.py
```

Train with your reward:

```bash
./experiment.sh --reward student \
  --image results/student_reward.png \
  --receipt results/student_reward.json
```

The bare answer `6` earns full reward without a valid trace. Compare
exact-answer accuracy with fully verified trace accuracy.

The reference solution is in `solutions/level3_reward.py`. Try first.

## What is happening?

```text
prompt
  ↓
transformer samples 8 completions token by token
  ↓
Python checks format, addition, multiplication, and final answer
  ↓
solutions receive mechanical rewards
  ↓
group-relative policy gradient updates the transformer
  ↓
the checkpoint with highest mean reward is reported
```

This is group-relative REINFORCE-style policy optimization with a KL penalty.
It is not a full GRPO implementation.

## The important limitation

The same 50 problems supply RL rewards, checkpoint selection, and reported
evaluation. The result demonstrates optimization on a known benchmark, not
generalization to unseen arithmetic.

The next research step is a frozen unseen test set and multiple random seeds.

## YouTube slideshow

Open [`slides.html`](slides.html) in a browser.

- `←` / `→` or `Space`: navigate
- `F`: fullscreen
- `Home` / `End`: first or last slide

## Verify the repository

```bash
.venv/bin/python -m unittest discover -s tests -v
```

GitHub Actions verifies Linux, macOS, and Windows.

## Sources

- [OpenAI — Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)
- [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948)

MIT License
