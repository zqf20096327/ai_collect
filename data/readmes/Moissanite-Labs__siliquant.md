# siliquant

Research on rounding model weights to a few bits each (quantisation), and on the mathematics around it. It sits beside [weft](https://github.com/Moissanite-Labs/weft), the software of ML Weft, and [weft-loom](https://github.com/Moissanite-Labs/weft-loom), its research records.

The repository follows one rule from weft-loom: a path is closed only on a proof. So it keeps a table of proved limits, and a proposal is read against that table before anything is run.

## What is here

| Folder | What it holds |
|---|---|
| `bounds/` | Proved floors and ceilings for rounding weights, computed from their formulas: Shannon's floor, the best scalar quantiser, what the shape of a lattice cell is worth. Also lattice constants, covering thickness and codebook counts, the cells of the point set F_n of incentre-lattices, the best lattices known above 8 dimensions, and what the region of a code is worth when one scale serves a group: for Gaussian weights from integrals, and its limits for any weights. Start with `bounds/bounds.out`. |
| `perm/` | Exact counting of matchings that avoid forbidden pairs: derangements, rook and hit polynomials, permanents, bounds on permanents, and the closure of a set of forbidden cells, with a witness for every cell that a second function checks from the board alone. Counts are tested against full enumeration on small cases, and bounds against exact values. `perm/demo.out` holds the figures the notes quote. |
| `lattice/` | Nearest-point decoders for the lattices Z^n, D_n, E_8, A_n and A_n\*, Voronoi codes, scalar reference quantisers, and row and column balancing. Tested against brute force and against known constants. |
| `shape/` | The process of issue #10 as code, for weight error. Codebooks cut from the integers or E8 by the ball of a p-norm, counted exactly. The region part of the error, computed from the weights with nothing rounded, and a formula for the error with no fitted constant. A receipt in whole numbers. For five arms the pick in exact arithmetic with a certificate, and a checker that shares no code with it. A closed-form scale with a proved bound on the error. `shape/ballindex.py` numbers the points of a codebook cut by a ball over any number of weights, so that a block can be stored in the bits of its number; `shape/ballindex.out` gives the sizes of its tables. `shape/ballpack.py` with `shape/ballpack.c` is a packed file format for integer levels in a ball: 18 bytes for a block of 32 weights, read back exactly. `shape/hammingindex.py` numbers the points of a ball of A_16, A_32 or E8 turned (A_8) repeated over a group, through the syndrome trellis of the extended Hamming code. `shape/hampack.py` with `shape/hampack.c` is the packed format with A_16, A_32 or A_8 in place of the integers: the same 18 bytes for a block of 32 weights, read back exactly. Not yet scored on a model. |
| `persist/` | The score called neural persistence: the maximum spanning tree of a layer read as a graph, the score built on it, the paper's bound under both readings of its count, and a distance between two layers' sorted tree sizes. Tested against full enumeration on small graphs. `persist/demo.out` holds the figures the note quotes. |
| `harness/` | Tools for experiments on real model files: read weights out of a GGUF file and write a changed copy, round on a GPU, and score a changed model against the original with llama.cpp's own tool. `harness/test_tq.py` checks the GPU code against `lattice/`. |
| `checks/` | Programs that read the repository itself: whether each record's plan was committed before its data, read from git; whether each row of a check note names a file for what it says was recomputed; and a trace of the numbers in the records, which measures how little such a trace can catch. [checks/README.md](checks/README.md) says what each found. |
| `experiments/` | One folder per study, each with its plan, program, output and limits. Index in [experiments/README.md](experiments/README.md). |
| `notes/` | [concept-map.md](notes/concept-map.md): the combinatorics the project owner listed, mapped to code, to the closure rule and to rounding. [brief-check.md](notes/brief-check.md): a source check of the two briefs the repository started from. [pr6-proposal-check.md](notes/pr6-proposal-check.md): a check of the research report in PR #6, claim by claim, and what follows from it. [issue10-proposal-check.md](notes/issue10-proposal-check.md): the same for the proposal of issue #10 and the published work it cites, with what PR #5 has that bears on it. [grafts-followup.md](notes/grafts-followup.md): what became of the fifteen crossings of the grafts note. [issue15-proposal-check.md](notes/issue15-proposal-check.md): the claims of issue #15 read against what was measured, and what issue #14 asks for. [persistence-and-flow-check.md](notes/persistence-and-flow-check.md): a check of a document on neural persistence and of two replies that map drag reduction onto models, with the bit budget that is left and its arithmetic in `notes/budget.out`. [cross-org-survey-2026-11-24.md](notes/cross-org-survey-2026-11-24.md) and [warp-drive-2026-11-24.md](notes/warp-drive-2026-11-24.md): what the other organisations hold for this work. [analysis-2026-11-24/](notes/analysis-2026-11-24/README.md): what the committed arms say at equal bits, the new lattices in the packed file's block, p-norm balls over 128 weights, and ranked proposals. |

## How to check it

The counting code needs only Python 3. The rest needs NumPy. The harness also needs torch. The shape toolkit does not.

```bash
python3 -m unittest perm/test_permlib.py
```

```bash
python3 -m unittest lattice/test_lattices.py
```

```bash
python3 -m unittest shape/test_shapelib.py shape/test_certified.py shape/test_ballindex.py shape/test_ballpack.py shape/test_ballformula.py shape/test_ggufread.py shape/test_npforward.py shape/test_hammingindex.py shape/test_hampack.py
```

```bash
python3 -m unittest persist/test_persist.py
```

```bash
python3 bounds/bounds.py
```

```bash
python3 harness/test_tq.py
```

```bash
python3 checks/plan_before_data.py && python3 checks/claim_ledger.py
```

## Run the kernel harness

The CUDA decode engine and its benchmark live in `studies/aletheion-qwen25-live-llm-engine/` (`qwen25_sm86_a16_engine.cu` for the sm_86 GPU engine, `qwen25_avx512_a16_engine.c` for the AVX-512 CPU engine, driven by `aletheion_live_llm_bench.py`). The standalone sm_86 PTX/SASS and AVX-512 kernel benchmarks live in `studies/aletheion-sm86-ptx-avx512-foundry/` (`aletheion_sm86_ptx_foundry.cu`, `aletheion_avx512_a16_decoder.c`).

Build and run the standalone kernel benchmarks with the commands below, copied verbatim from `studies/aletheion-sm86-ptx-avx512-foundry/SM86_PTX_AVX512_FOUNDRY_REPORT.md`, section "3. Build & Verification Commands":

```bash
# Verify committed JSON receipts and study invariants (Python 3 stdlib only):
python3 -I -B studies/aletheion-sm86-ptx-avx512-foundry/test_sm86_avx512_foundry_r5.py

# Re-compile and run CUDA sm_86 foundry (requires CUDA toolkit + sm_86 GPU):
nvcc -O3 -std=c++17 -arch=sm_86 --ptxas-options=-v \
  studies/aletheion-sm86-ptx-avx512-foundry/aletheion_sm86_ptx_foundry.cu -o /tmp/sm86_foundry
/tmp/sm86_foundry

# Re-compile and run Intel AVX-512 decoder (requires AVX-512F/BW/VL/VBMI/VPOPCNTDQ/VNNI CPU):
gcc -O3 -march=native -mavx512f -mavx512bw -mavx512vl -mavx512vbmi -mavx512vpopcntdq -mavx512vnni \
  -funroll-loops -fopenmp -Wall -Wextra \
  studies/aletheion-sm86-ptx-avx512-foundry/aletheion_avx512_a16_decoder.c -o /tmp/avx512_decoder -lm
OMP_PROC_BIND=spread OMP_PLACES=cores /tmp/avx512_decoder
```

### Full-model decode engine (PR #88): pending confirmation on an sm_86 GPU

The four core steps, run from `studies/aletheion-qwen25-live-llm-engine/`. Marks: VERIFIED-ON-BOX means it ran on a check machine with no GPU; STATIC means read from the code, not run; NEEDS-SM86 means it can only be confirmed on an sm_86 GPU.

```bash
huggingface-cli download Qwen/Qwen2.5-0.5B --revision 060db6499f32faf8b98477b0a26969ef7d8b9987
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"
export MODEL_DIR="$HF_HOME/hub/models--Qwen--Qwen2.5-0.5B/snapshots/060db6499f32faf8b98477b0a26969ef7d8b9987"
sha256sum "$MODEL_DIR/model.safetensors"   # must equal 88c142557820ccad55bb59756bfcfcf891de9cc6202816bd346445188a0ed342
# STATIC (inferred — command itself is a GAP; repo id/snapshot/sha pins are STATIC from oracle.py:45-61)

nvcc -O3 -std=c++17 -arch=sm_86 --ptxas-options=-v -shared -Xcompiler -fPIC \
  qwen25_sm86_a16_engine.cu -o libqwen25_sm86_a16_engine.so
# NEEDS-SM86 (flags STATIC from report line 28; -shared/-o are GAP-1)

gcc -O3 -march=native -mavx512f -mavx512bw -mavx512vl -mavx512vbmi -mavx512vpopcntdq \
  -mavx512vnni -fopenmp -shared -fPIC \
  qwen25_avx512_a16_engine.c -o libqwen25_avx512_a16_engine.so -lm
# VERIFIED-ON-BOX (compile only; flags STATIC from report line 33; -shared -fPIC -o -lm are GAP-1)

python3 aletheion_live_llm_bench.py \
  --phase all \
  --model-dir "$MODEL_DIR" \
  --sm86-so ./libqwen25_sm86_a16_engine.so \
  --avx512-so ./libqwen25_avx512_a16_engine.so \
  --out-json ./qwen25_live_engine_empirical_results_repro.json \
  --cpu-threads 8
# NEEDS-SM86 (invocation STATIC from bench.py:1489-1523; run aborts without CUDA at bench.py:751-752 "CUDA GPU not available")
```

In the `--out-json` file the B1 figure is the `gpu_event_tok_s` field of `arm_b_sm86_ptx_a16_gpu.b1_pure_dp4a.full_e2e_with_bf16_lm_head`.

Known gaps:

- No script writes the `.so` link step, and the `-shared`/`-fPIC` flags are an addition untested with nvcc (GAP-1).
- CUDA toolkit and Python package versions are unrecorded; only driver 615.78.08 and Python 3.14.8 are recorded (GAP-2, GAP-3).
- The model download is not scripted (GAP-4).
- RAPL must be readable or CPU energy silently reads 0 (GAP-5).
- There is no per-arm flag, so B1 and A need one full run with both `.so` files and an AVX-512 CPU (GAP-8).
- The `mlos` tool and its profile are not in the repo (GAP-6).

Full steps, citations and checks: [REPRO.md](studies/aletheion-qwen25-live-llm-engine/REPRO.md). Nothing in the B1 path has been confirmed without an sm_86 GPU.

## How records are kept

The conventions are those of [weft-loom's CONTRIBUTING.md](https://github.com/Moissanite-Labs/weft-loom/blob/main/CONTRIBUTING.md). In short:

- A study has a plan committed before its data, or says "not preregistered".
- Every number in a README can be traced to a committed output file.
- A null or negative result is recorded the same way as a positive one.
- No model weights and no datasets are committed. A record names the file it used by its SHA-256.

## Status

Twenty-six studies so far. The newest results are at the end of this section.

The first measured weight error only: at 2 bits per weight the lattice E8 beats scalar rounding on every matrix tried, and the lattice the starting briefs proposed, A8\*, gains less than half as much in the mean of each family of data.

The second measured the output of a real model, `gemma-4-E4B-it`. Weight error turned out not to say what the output does. In these runs the output followed how the scale is set more than the size of the error.

With one scale per 32 weights, set from the largest entry, E8 gives a closer output than llama.cpp's `Q4_0` at the same 4.5 bits. With one scale per matrix and no balancing, E8 is worse than scalar rounding at 4 and 5 bits. One model and one text so far.

The other three were run on 2026-11-17 to read the proposals of PR #6 and to answer issue #4. They measure weight error only, on synthetic matrices and one small speech model.

- **The codebooks PR #6 proposes do not beat scalar rounding or E8 as proposed.** The point set of incentre-lattices has cells worth 1.2 to 2.0 dB less than a cube. A vortex codebook is about as good as the best scalar quantiser. The 880 realisations of a graph are a worse codebook than 880 random points.
- **E8's gain under the largest-entry rule needs no model, and most of it is not the lattice.** On Gaussian data it is 1.36 dB with groups of 32 and 2.3 dB per row. Per row, 0.65 dB is the cell and 1.64 dB is the scale: the rule lets E8 use a smaller scale because the region of its code is nearly a ball.
- **The region can be chosen.** Integer levels cut by a ball reach 76 to 89 percent of E8's gain on the real matrices with no lattice. E8 cut by a ball beats the E8 Voronoi code by 0.13 to 0.20 dB on 29 to 32 of 32 real matrices, at no more bits. These codebooks have no packed format yet.

None of the three was scored on a language model.

The sixth, also of 2026-11-17, reads the proposal of issue #10: a formula that gives the error of a rounding from the weights alone and picks the shape of the code's region, the size of a group and the directions kept. It measures weight error on 109 matrices that no codebook had been run on, 85 of them real, from one small speech model and one small language model.

- **From 4 bits up the formula gives the error and picks the best arm.** It has no fitted constant. On the real matrices it is within 0.3 dB of the measured error in 96.6 percent of 5,525 runs, and the arm it picks among 13 is the measured best in 96 percent of 425 choices. At 2 bits it is low by 0.8 dB.
- **The best region on real weights is between the cross-polytope and the ball**, a p-norm ball with p = 5/4 or 3/2, by 0.2 to 0.3 dB. At 4.5 bits groups of 128 weights are the best size on 82 of 85 real matrices. Dropping directions loses on 83 and wins on two, and the formula says which.
- **Two limits are proved.** On a round cloud no region beats the ball. For any weights a region is worth at most 2.5 log10 of a ratio of volumes: 4.50 dB for a ball over the cube and 11.51 for a cross-polytope.
- **A rule with a proved guarantee costs about half a decibel.** With a closed-form scale nothing is clipped and the error is under a bound, by two short proofs and in 1,308 of 1,308 runs. For five arms the pick is whole-number arithmetic with a certificate. No proof assistant has run on any of it.

Nothing in the sixth is scored on a model's output, and its codebooks have no packed format.

The seventh, of the same date, cut codebooks by a ball over 8 to 128 weights. The gain grows with the block as the limits table's formula says, and with one ball per group of weights the error does not depend on the weights. Weight error only.

The eighth answers issue #9: the fold of incentre-lattices as a path of codebooks over 3 weights. The cell does improve along the fold, and its best state is its end, close packing, worth a quarter of a decibel. Every state loses to a fitted codebook, to E8 and to a longer ball.

The ninth scores a second model, `Qwen2.5-1.5B-Instruct`, on a second text, for issue #3: 32 variants.

- **As the gemma record ran it, E8's win shrinks with groups of 32 and reverses with one scale per row.** The cause is in the harness: its E8 Voronoi code subtracts the mean of its codewords, so none of them is zero. With a codeword at zero the same code is ahead of the scalar rule at all three bit points. The change is invisible in mean weight error and worth a factor of 17 in KL per row.
- **One ball per group of weights is far ahead at equal bits.** E8 in one ball per group of 128 scores a mean KL of 0.0195 at 4.5 bits. llama.cpp's `Q4_0` scores 0.0623 at 4.5 bits and its `Q4_K_M` 0.0333 at 4.81. Integer levels with no lattice score 0.0227.
- **For those arms a decibel of weight error is a decibel of KL**, within a tenth, over nine arms from 4.0 to 4.5 bits.

The tenth scores the same arms on a third model, `SmolLM2-1.7B-Instruct`, on the same text.

- **The headline holds.** At 4.5 bits one ball per group of 128 scores 0.0560 for integer levels and 0.0609 for E8, where `Q4_K_M` scores 0.0838 at 4.82 bits and `Q4_0` 0.1271 at 4.5.
- **Two things do not carry.** Integer levels are ahead of E8 on this model, and its E8 arms gain less on the output than their weight error says. And the harness's Voronoi code is not broken per row here: a codeword at zero is level per row and a little worse with groups of 32.
- **So the arm that both models agree on is the plain one**: integer levels in one ball per group of 128 weights.

The eleventh answers issue #14: llama.cpp's files made with an importance matrix, beside the ball arms, on both models.

- **The matrix helps llama.cpp's files, by 15 percent of KL on Qwen2.5 and 55 percent on SmolLM2.** With it, `Q4_K_M` is ahead of the ball arm with no data on SmolLM2 and still behind it on Qwen2.5.
- **Given the same matrix at half strength, the ball arm is ahead on both**: 0.0209 and 0.0282 at 4.5 bits, against 0.0282 and 0.0378 for `Q4_K_M` with the matrix at 4.8 bits. At full strength it does worse. The half-strength arm was planned and not predicted to win. A sweep of five strengths on the validation text then chose that strength by a rule fixed beforehand.

What these do not show: a matrix from other text, or a score on another kind of text. The twentieth and twenty-first studies, below, take those up. Their bits are counted from the codebook. The fourteenth study, below, puts one arm in a file, and the seventeenth scores a task.

The twelfth, also of 2026-11-17 and from another lane of work, goes back to the output of `gemma-4-E4B-it` and treats the loss as a budget with parts. One model and one text, with no packed format.

- **Bits split by measured gain beat equal bits.** At 4.5 bits the split scores a mean KL of 0.0805 against 0.1173 for the `Q4_0` rule. The split is fitted on the text it is scored on.
- **Keeping 0.17 percent of the weights exact more than halves the KL of a row scale**, for 0.049 bit. A scale stored in 8 bits costs 2.1 percent of KL. With all three joined the score is 0.0629 at 4.484 bits.
- **One matrix carries the damage of clipping large weights.** Clipped alone, the `ffn_down` of layer 10 scores 0.1560 and the other 41 layers add up to 0.0182. None of three figures of its large entries picks it out, and its ten units with the most change do not carry the damage. Between one scale rule that clips and one that does not, at 32 levels, it accounts for a third to a half of the gap.
- **The two kinds of matrix that looked sensitive in the second study do not stand out under a scale per 32 weights that clips nothing.** The two rules differ in group size and in clipping, and the study does not separate them. A measure built on neural persistence ranked new arms worst of five.

The thirteenth, from the lane of issue #10, asks why integer levels beat E8 on SmolLM2 against their weight error. It runs the model in NumPy on 16 passages.

- **E8's error costs what noise of its size costs. The error of integer levels costs 1.1 dB less.** All of that is at the 7.8 percent of the weights that integer rounding sends to zero.
- **E8 cannot have that gain**: it moves half of those weights to plus or minus half a step.

The fourteenth, of 2026-11-18, stores the integer ball arm in a file and scores the model read back from it.

- **4.5 bits a weight in a file, read back bit for bit.** 18 bytes for a block of 32 weights. The file of Qwen2.5 is 737 megabytes.
- **The model the file holds is ahead of llama.cpp's `Q4_K_M` at 4.8 bits on both models**: 0.0245 against 0.0333 and 0.0589 against 0.0838. With the importance matrix on both sides, 0.0227 against 0.0282 and 0.0309 against 0.0378.
- **It decodes at 20 to 25 million weights a second on one core**, about a minute for a model. Nothing is saved when the model runs: the file is decoded to floats first.

The fifteenth, of 2026-11-18, is run 3 of issue #20: the clip of `ffn_down` on each layer of Qwen2.5 alone, by the rule of the twelfth study.

- **Not one matrix as on gemma: two, at the ends of the model.** Layer 1 holds 40.6 percent of the summed damage and the last layer 29.8. With their neighbours, 83.3 percent in four matrices of 28.
- **Here the weights say which.** The four matrices the clip changes most are the four that cost most. On gemma no figure of the weights found the matrix.
- **The damage does not add.** All layers at once cost a mean KL of 0.593, five times the sum of the 28 alone.

The sixteenth, of 2026-11-18, is run 1 of issue #20: the split of bits by kind of matrix of the twelfth study, fitted on one text and scored on another, on Qwen2.5.

- **The split holds on the text it never read.** At 4.5 bits it is 17.4 percent under equal bits on the validation text it was fitted on, and 17.9 percent under on the test text. At 3.5 bits, 25.8 and 20.4 percent.
- **The gain is smaller than on gemma**, where it was 31.4 percent, and small beside what one ball per group gains on this model with no fit: 63 percent.
- Both texts are Wikipedia prose of one source. A text of another kind is not tested.

The seventeenth, of 2026-11-18, is the task benchmark of issue #14: 2,000 questions of MMLU in llama.cpp's multiple-choice mode, six variants on two models, compared question by question.

- **Accuracy does not separate the ball arms from the 16-bit model.** Their differences are -0.70 to +0.15 points, and the run can see a loss of 1.1 to 1.3. So the result for accuracy is a bound.
- **How often a variant keeps the 16-bit model's answer follows its KL**, in order, through all five variants on both models. By that measure the ball arm with the matrix is ahead of `Q4_K_M` with the matrix on both: a tie on Qwen2.5, 2.3 errors on SmolLM2.
- It is not MMLU as published: bare questions and answers scored as continuations. HumanEval and GSM8K were not run.

The eighteenth, of 2026-11-18, is the clip of the fifteenth study on a third model, SmolLM2.

- **Neither picture.** Two matrices, layers 1 and 7 of 24, hold 56.9 and 40.9 percent of the summed damage. gemma had one matrix in the middle and Qwen2.5 two at the ends.
- **The clip costs most where it removes almost nothing.** In layer 1 it changes 387 entries of 16.8 million, and that alone costs a mean KL of 1.74. All 24 layers at once cost 4.12, where I predicted under 0.06.
- **The weights do not say which matrix here.** The clip's weight error ranks the layers at 0.39, against 0.77 on Qwen2.5. The activity of the columns the clip removes ranks them at 0.90, and that figure needs calibration text.

The nineteenth, of 2026-11-18, asks what those matrices have that a clip must not touch, and whether rounding must protect it too.

- **On SmolLM2 it is a handful of weights.** The clip in ten columns of layer 1, 41 entries, costs a mean KL of 1.449. The clip everywhere else in that matrix costs 0.0003. Two weights of one hidden unit cost 1.175 by themselves.
- **On Qwen2.5 it is ten columns in layer 1 and not in the last layer.** On gemma it was not the ten units either.
- **It hardly matters to rounding.** With those columns left whole the ball arm on SmolLM2 scores 0.0528 against 0.0560, where I predicted a gain of at least 20 percent. They are a ninth of what an importance matrix gains on that model.

The twentieth, of 2026-11-18, asks what an importance matrix's gain is made of. It belongs to issue #14.

- **On SmolLM2 two thirds of it is in three matrices.** With only the matrices through which the attention reads the stream weighted, 18.75 percent of the weights, the ball arm gets 68.5 percent of the whole gain. What the attention reads there sits in ten dimensions of 2,048.
- **The matrix does not need a text with a meaning.** Made from random pieces of the model's own vocabulary, it buys the ball arm 88.6 percent of what the wikitext matrix buys on SmolLM2, and llama.cpp's `Q4_K_M` 95.5 percent. On Qwen2.5 it does the ball arm neither good nor harm.
- **So with no text read, the ball arm at 4.5 bits is under `Q4_K_M` made with real text on both models**: 0.0314 against 0.0378 and 0.0228 against 0.0282. As a packed file it is ahead on Qwen2.5 and level on SmolLM2, where I predicted ahead on both.
- The model is still run, on 51,200 tokens of noise. No dataset is needed. Forward passes are.

The twenty-first, of 2026-11-18, scores the headline comparisons on a second text: Python source in place of Wikipedia prose.

- **All three hold on both models.** The ball arm at 4.5 bits is under `Q4_K_M` at 4.8 bits by 13.2 and 9.3 errors with no matrix on either side, by 11.2 and 5.0 with the wikitext matrix on both, and by 8.7 and 3.6 with a matrix from noise on its side against the wikitext matrix on the other.
- **On SmolLM2 a matrix from noise is as good as one from Wikipedia on a text neither has read**: it buys 99.3 percent of the gain for `Q4_K_M` and 95.1 for the ball arm.
- **On Qwen2.5 the ball arm is best with no matrix on this text.** Both matrices cost it 2 to 3 errors. Its gain from the wikitext matrix on prose was a gain on the kind of text the matrix was made from.

The twenty-second, of 2026-11-19, runs the comparisons on a third model of another family, `Llama-3.2-1B-Instruct`, on both texts.

- **With no matrix on either side the ball arm is behind `Q4_K_M` on this model**: 0.0478 against 0.0432 on the wikitext text, 4.9 errors, and 8.3 errors behind on Python. On the two earlier models it was 9 to 15 errors ahead.
- **With a matrix it is far ahead, as on the other two**: 18.2 and 17.0 errors with the wikitext matrix on both sides, 11.1 and 13.7 with a matrix from noise against the wikitext matrix. Those two comparisons now hold on three models and two texts.
- **This model's loss is two hidden units.** 92.6 percent of what a matrix gains here is in the two writing matrices, and one column of `ffn_down` left whole in each of the first two layers takes the ball arm from 0.0478 to 0.0302.
- **The weights alone find them.** With the ten loud columns of every `ffn_down` left whole, at 4.505 bits, no data and no forward pass, the ball arm is under `Q4_K_M` with no matrix on all three models: by 12.5, 16.8 and 17.3 errors.
- A rule I had drawn from the first two models, keyed on how much of the attention's input sits in ten dimensions, is refuted by this one.

The twenty-third, of 2026-11-19, gives that arm a file. The packed format of the fourteenth study now stores columns kept whole.

- **A file of 4.5 bits a weight, made from the weights alone, is ahead of `Q4_K_M` at 4.8 bits with no matrix on all three models**: mean KL 0.0247 against 0.0333, 0.0581 against 0.0838 and 0.0340 against 0.0432, which is 10.2, 13.5 and 11.9 errors. No data is read and the model is never run. Each file was read back from disk bit for bit.
- **On Llama-3.2 the kept columns are what the file needs**: 0.0519 without them, 9.0 errors behind `Q4_K_M`, and 0.0340 with them. On the other two models they cost nothing.
- It is not ahead of `Q4_K_M` made with an importance matrix on SmolLM2. And no engine reads the file: it is decoded to floats first.

The twenty-fourth, of 2026-11-23, runs the proposal of draft pull request 24 on real weights: E8 turned by a Hadamard matrix of order 8.

- **At 4.5 bits with no data the turned lattice is the lowest arm, or within 2 errors of it, on all three models, and ahead of `Q4_K_M` on all three**: mean KL 0.018875, 0.051522 and 0.036038 against 0.033348, 0.083761 and 0.043179. On SmolLM2 it is 5.4 errors under plain E8 and 3.0 under integer levels, with the weight error unchanged: it stores 85.9 percent of the smallest weights as zero where E8 stores 60.7.
- **At 3.0 bits there is no single winner**, and in a Voronoi code turning helps on one model, hurts on the other and does not reach `Q4_K_M`. No E8 arm has a file or a decoder yet.

The twenty-fifth, of 2026-11-24, tests two results of a survey of the other organisations' work: the lattices of the longer extended Hamming codes, and a baseline scored the way the ball arms are.

- **At 4.5 bits with no data the lattice A_16, in one ball per 128 weights, is the arm to recommend.** Mean KL 0.018974, 0.047957 and 0.034455: the lowest arm on all three models or tied with it. It rounds 93 to 96 percent of the smallest weights to zero, and has 0.12 dB less weight error than E8. With ten columns of each `ffn_down` kept it scores 0.024053 on Llama-3.2. A_32 rounds even more weights to zero and wins SmolLM2, but loses Llama-3.2.
- **At 3.0 bits a lattice closes the gap on SmolLM2.** A_32 scores 0.358845 and A_16 0.380994, against 0.419643 for integer levels, which had been far ahead of every E8 arm. On Qwen2.5 A_16 is the lowest arm.
- **The committed `Q4_K_M` rows paid for 8-bit activations that the ball arms never paid.** Multiplied at 16 bits, `Q4_K_M` scores 0.031690, 0.072237 and 0.041195. Every lead of a ball arm holds, by 0.8 to 5.4 errors less. bitsandbytes' NF4, which the organisation trains in, is 26.5 to 46.4 errors behind E8 turned.
- A numbering of these balls (`shape/hammingindex.py`) and a file with A_16 in the packed format's block (`shape/hampack.py`) were written during the run. The file has its own plan.

The twenty-sixth, of 2026-11-24, puts A_16 in the repository's file format: the 18 bytes for 32 weights of `shape/ballpack.py`, with A_16 × A_16 in place of Z^32 (`shape/hampack.py`).

- **At the same size to the byte, the A_16 file is lower than the integer file on all three models**: by 4.6 to 12.7 errors with no columns kept, and by 6.2 to 12.4 with ten columns of each `ffn_down` kept. With the columns kept it scores 0.020816, 0.047987 and 0.026708, 14.9 to 21.8 errors under `Q4_K_M@16`. It is the file to recommend with no data. All six predictions hold.
- **It decodes 2.5 to 3.0 times slower**, about 100 seconds per billion weights on one core, and a model packs in 8 to 15 minutes on 4 cores against about one.
- **The ball of 128 weights with a 16-bit scale is still 3.1 to 6.7 errors lower** at the same 4.5 bits. A file with blocks of 128 weights is the next step.

## Licence

No licence file yet. The owner has not chosen one.

## Disclosure

Most of the code and text here was written by AI agents under the owner's direction, and checked by a second agent before merging.
