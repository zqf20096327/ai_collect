# <img src="media/a.ico" width="24" height="24" alt="" /> [Algolume](https://algolume.ru)

Paste a Python program. Algolume runs it under its own tracer, replays it line by line, and draws
the data structure your code is actually building, with your variable names and your input.

<img src="media/algolume_demo.gif" alt="Stepping through a segment tree build" width="880" />

<sub>A segment tree built one traced line at a time, then hovered to reveal which range each node covers.</sub>

Plenty of sites visualise a fixed set of algorithms. Accepting someone else's code is the harder
problem, and it breaks into three parts. The trace has to carry state rather than line numbers, so
every step keeps a deep copy of the live variables. The renderer then has to know which variable is
the parent array and which is the DP table, which the trace cannot tell it, so the user maps them
once by name. And the classifier has to cope with algorithms that look almost identical in source:
Prim and Dijkstra differ by one line, Fenwick and segment trees solve one problem two ways.

<table>
<tr>
<td width="50%"><img src="media/screenshot-detect.png" alt="Algorithm detection on pasted code" /></td>
<td width="50%"><img src="media/screenshot-session.png" alt="A traced DFS session with the graph drawn from the code" /></td>
</tr>
<tr>
<td><sub>Pasted code, classified, with the variable mapping the visualiser needs.</sub></td>
<td><sub>The same code stepped through, with the graph built from its own adjacency list.</sub></td>
</tr>
</table>

## Tracing

`backend/code_exec/` installs a `sys.settrace` hook and records, for each executed line, the line
number, call-stack depth, stdout so far, stdin consumed, and a snapshot of every local and global.
The frontend replays that log, which is why stepping backwards costs nothing. Values that will not
serialise become strings instead of disappearing, so no step renders blank.

## Complexity from the trace

`backend/complexity/` reruns the program on generated inputs of growing size, counts executed trace
steps, and fits the result against `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n²)`, `O(n³)` and
`O(2ⁿ)`. Fitting happens on log-log axes, so each candidate is a straight line and the constant
factor drops out as an offset. Candidates rank by residual error rather than by one coefficient.

The verdict comes with its fit quality and the raw measurements, so you can check it. When fewer
than four sizes produced data, or the best fit explains under 90% of the variance, or the two
leading curves land within 12% of each other, the answer is "insufficient data" instead of a guess.
Inputs are generated as arrays, strings or graphs.

Measured here: a summation loop reads as `O(n)` at 0.995 fit quality, a nested loop as `O(n²)` at
1.000. Sizes stop at `n = 320`, because a full variable snapshot per step means a quadratic program
reaches the 256 MB cap around there. That ceiling belongs to the tracer, not the fitting.

<img src="media/screenshot-complexity.png" alt="The complexity panel: verdict, fitted curve and the raw measurements" width="880" />

<sub>The verdict never travels alone: the fitted curve and every measured point ship with it.</sub>

## Recognising the algorithm

`/api/predict` sorts pasted code into seven classes: BFS, DFS, Dijkstra, Grasshopper DP, prefix
function, Turtle DP, Z-function.

Pattern matching does not survive this problem. Prim and Dijkstra share the import, the visited
array and the relaxation loop. A Z-function can be a two-pointer loop, a recursion, a comprehension
or a slicing trick under any naming. And most pasted code is not an algorithm at all, which a
matcher has no way to say.

So the classifier is a learned model, and everything around it fights the temptation to memorise
surface form. The corpus is synthetic on purpose: 1050 samples, 150 per class, generated from two
prompt families per algorithm. One produces bare routines with no I/O, the other complete programs
that parse stdin and print. Both demand structurally different implementations with renamed
variables in every variant, because a model fed one idiomatic version per algorithm learns the
idiom instead. Then `backend/model/preprocess.py` canonicalises everything the same way at training
and inference: comments and docstrings out, I/O out, every identifier renamed, AST unparsed back to
source. A snippet and a full program collapse to the same input, and naming carries no signal.

The model is GraphCodeBERT (`microsoft/graphcodebert-base`, a 12-layer RoBERTa encoder) fine-tuned
with a `768 → 384 → n_labels` head over the CLS embedding, capped at 256 tokens, exported to ONNX
and served through `onnxruntime`, which is why the production image ships without PyTorch.

## Admitting it does not know

Seven classes is a closed set, so unrelated code still forces the softmax to commit somewhere. A
confidence threshold turns that into an explicit state. It lives in `backend/classifier_config.py`
and comes from calibration rather than taste: `ml/evaluate_rejection.py` scores a held-out corpus,
drops any row whose code hash appears in training, and picks the threshold that maximises F1 over
accept and reject. On this checkout: `samples 196, raw_accuracy 1.0, threshold 0.889, coverage 1.0`.

Coverage 1.0 means the threshold rejects none of those held-out samples, which proves it is free,
not that it works. The evidence that it works comes from code belonging to no class. Six such
snippets (JSON echo, FizzBuzz, word statistics, matrix transpose, a small class, binary search) were
all rejected, with top-class confidence between 0.24 and 0.87. Binary search landed at 0.865, close
to the line, which seems fair for algorithmic code with no matching class.

Rejected code gets no algorithm-specific visualisation, but tracing and complexity estimation carry
on, since neither depends on the classifier.

## A note on running submitted code

Submitted programs execute in a child process behind an AST whitelist, a five-second wall clock and
a 256 MB memory cap, with container memory and PID limits on top. That is enough to keep the public
demo usable, and it is not a security boundary. Anyone self-hosting this should put real isolation
around the executor before exposing it.

## Layout

```
backend/
  app/debug_server.py     Flask app: pages, session generation, /api/predict, /api/complexity
  code_exec/              the tracer, the AST whitelist, the time and memory limiter
  complexity/             input generators and log-log curve fitting
  algorithms/             reference implementations (DSU, Fenwick, segment tree, Prim, Kruskal)
frontend/
  theory/                 one page per algorithm, the landing page, the i18n dictionary
  python_debug_sessions/  templates a generated session renders from
ml/                       corpus generation, training, threshold calibration
tests/
```

English is the default (`lang="en"` and English in the markup); Russian lives in
`frontend/theory/i18n.js` and is applied by the language switch.

`ml/` started as a separate project (AlgoScout) and was merged in with its full history, so there is
no submodule and nothing extra to clone. [`ml/README.md`](ml/README.md) covers the corpus design,
canonicalisation, the model and calibration in detail.

## Running it

```bash
docker compose up -d --build
```

The app listens on `5612`, and compose also starts the Redis the rate limiter needs. Without Docker:

```bash
pip install -r requirements.txt
PYTHONPATH=. REDIS_HOST=127.0.0.1 gunicorn backend.app.debug_server:app -b 127.0.0.1:5612
```

Tests run with `python -m pytest tests/ --ignore=tests/get_debug_log`. The ignored directory holds
sample programs that read stdin, not test cases.

Retraining and recalibration:

```bash
python ml/dataset/generate_all.py        # build the corpus (resumable)
python ml/model/template/train.py        # fine-tune, writes model_ckpt/
python -m ml.evaluate_rejection          # recalibrate the rejection threshold
```

Serving reads `backend/app/model_ckpt/` and `backend/app/static/model.onnx`. Neither is in git;
both are build artefacts.

---

© 2026 Algolume. Created by Ivan Kochergin.
