# leOS — Latent Embedding Operating System

**v0.3.0**

**Website:** https://discoverleos.com/

A substrate for AI agents that grows with use.  leOS is a local
operating system where everything — knowledge, tools, routing
decisions, cached responses, learned patterns — lives as vectors on
the surface of a high-dimensional sphere.  Agents don't search by
keywords or match by string — they search by meaning, route by
geometry, and learn by accumulating experience in embedding space.


## The Problem leOS Solves

For an AI agent to be genuinely useful, it needs to do thousands of
things: read files, search the web, analyze images, call APIs, write
code, manage plans, process video, query databases, control devices.
Today's agent frameworks hit a hard wall: **the more tools and skills
you give an agent, the worse it performs.**

This happens for two reasons.  First, every tool definition eats
context window tokens.  Load 200 tools into an LLM's context and
there's no room left for the actual work.  Second, the more an agent
knows how to do, the harder it is for it to figure out which skill
to use right now.  An agent with 20 tools can pick the right one
most of the time.  An agent with 2,000 tools drowns in options.

The standard solutions — static tool lists, manual routing, hardcoded
skill categories — don't scale.  They require a human to decide in
advance which tools are relevant, which defeats the purpose of
autonomous agents.

leOS takes a different approach.  Instead of handing the agent a
fixed list of tools and hoping for the best, leOS **finds the right
tools semantically and assembles them into chains on the fly.**

Here's how:

**Dynamic tool selection.**  The full tool catalog lives in an
embedding-indexed registry.  When a task arrives, leOS embeds the
task description, scores it against domain centroids to discard
80-90% of tools instantly (Pass 1), then runs fine-grained semantic
+ keyword scoring on the survivors (Pass 2), blended with learned
usage history from past sessions (Pass 3).  The agent receives only
the 6-8 most relevant tools with full definitions, plus a one-liner
listing of others it can request by describing what it needs.  This
scales to hundreds or thousands of tools without flooding context.

**Composable bone chains.**  Every capability in the system — from
"embed text" to "call the dexscreener API" — is a typed atomic
operation called a bone.  Bones have typed inputs and typed outputs.
The FABRIK planner (borrowed from inverse kinematics in character
animation) works backward from the desired output and forward from
available inputs to assemble bone chains that achieve goals.  If a
chain doesn't exist, the planner builds one from parts.

**Tiered execution ladder.**  Not every request needs the main agent
model.  Requests start at the cheapest tier that can plausibly handle
them: FABRIK alone (deterministic, no LLM), then the intern model
(0.8B, CPU), then the main agent (9B, GPU).  When a user isn't
satisfied with a Tier-0 or Tier-1 answer, a retry button bumps them
up one rung.  The system records which tier each response came from,
so retries always land at the next-higher tier with the user's
optional hint added to the prompt.  Cheap requests stay cheap; only
genuinely hard ones reach the main model.

**Pre-LLM substrate gathering.**  Before any classified user query
reaches the LLM, the substrate-gather decision tree runs first.  It
classifies the query (research, codebase question, system question,
status check, feedback, general chat), extracts entities (token
addresses, URLs, DOIs, GitHub repos, etc.), checks the knowledge
base, and — for high-confidence cases — answers directly without
ever calling the model.  When confidence is mid-range, it hands the
LLM a pre-filled draft to verify or correct.  When confidence is
low, it falls through to the normal handler pipeline.  This catches
"I have the answer in the KB already" cases that would otherwise
spend several seconds and a chunk of context window doing nothing
useful.

**Learning from mistakes.**  When a tool chain fails, the system
records the failure trajectory.  The displacement codec stores the
input-to-output pattern.  Next time a similar task arrives, the
system avoids the path that failed and tries an alternative.  When
chains succeed, they're saved as "skeletons" in the bone registry —
pre-validated patterns that can be reused.  Over time, the library of
known-good chains grows and the system gets both faster and more
reliable.

**Dynamic context assembly.**  The agent's working context isn't
static either.  Scopes (work containers) hold plans, notes,
decisions, and observations organized by goal.  When the agent starts
a task, the context assembler queries the relevant scope and builds
a layered context from eight priority tiers: scope identity, current
task, active plan state, recent activity, relevant knowledge base
articles (by semantic similarity), parent scope context, similar past
tasks, and sibling scope awareness.  Each layer has a token budget.
Lower-priority layers are trimmed when the budget runs out.  The
agent always gets the most relevant context that fits.

**Self-improvement.**  The system tracks what it doesn't know.  Void
detection scans the knowledge base for gaps between clusters — "know
Python, know async, but no article about Python async."  The skill
assimilator tracks capability gaps — tasks where no tool scored above
threshold.  When gaps recur often enough, the system can generate new
tools to fill them.  The dreaming engine runs during idle time,
consolidating knowledge, repairing data structures, and growing the
nutrient field (an information-density map modeled on mycelium
networks).  The learning evaluator checks eight dimensions of system
health: displacement trajectories, reflex arc graduation rates,
skeleton library growth, nutrient field density, tool selection
accuracy, capability gap coverage, knowledge coverage, and timing
trends.

**The mission is to build the growing, adapting substrate that AI
agents need to become genuinely capable** — not a static tool
library, but a living system that gets smarter, faster, and more
knowledgeable with every interaction.


## Why There Is a Desktop

The desktop is not cosmetic.  It exists for three reasons.

**First, it gives agents eyes.**  An AI agent that can only read
JSON responses is blind to the state of the system it's operating.
The leOS desktop is a perception layer — agents can describe the
screen, identify elements at coordinates, click, type, drag, and
scroll.  External agents connecting via MCP get the same UI tools.
This means an agent can visually verify that a knowledge base article
was saved, that an app launched correctly, that search results look
right.  The desktop is the agent's visual cortex.

**Second, it gives the system a body.**  The 3D desktop (Three.js) is
the spatial representation of the embedding space itself.  Stored
vectors, SDF regions, app clusters, knowledge density — all of these
have geometric positions.  The desktop makes the invisible visible.
Over time, the native render system learns to predict draw commands
from widget properties using the displacement codec, graduating from
Python-rendered bootstrap to embedding-predicted native rendering.
This is the system learning to see itself.

**Third, it gives humans a window.**  The dashboard, knowledge base
browser, plan viewer, scope viewer, work tray, thought canvas, and
voice library are all web pages served by Flask.  You can watch what
the agent is doing, inspect its plans, read its knowledge base,
listen to its thought narration, and intervene when needed.  The
desktop is the shared workspace between human and AI.


## Theoretical Foundations

This isn't speculative.  The mathematical proofs exist and the
experimental results are published.

**Vector Symbolic Architectures are Turing complete.**  Kleyko,
Davies, Frady, Kanerva et al. (2022, Proceedings of the IEEE) proved
that three primitive operations on high-dimensional vectors —
bundling (addition), binding (circular convolution), and permutation
— form a computationally universal basis.  The emulated machine
executed over 10^9 error-free updates.  This means the class of
operations leOS uses can compute anything a conventional computer
can compute.

**The blessing of dimensionality.**  In 768+ dimensions, randomly
chosen vectors are almost always nearly orthogonal (concentration of
measure).  The system can store enormous numbers of distinct concepts
without interference.  Johnson-Lindenstrauss guarantees distance
preservation across projections.  The surface of the 768d unit sphere
has astronomically more representational capacity than any 3D
structure.

**Hypersphere geometry is computationally superior.**  The nGPT paper
(2024) showed that constraining representations to unit norm and
expressing transformations as hypersphere displacements produced a
10x training speedup.  Working on the hypersphere isn't just elegant
— it's measurably more efficient.

**Continuous reasoning without tokens.**  Meta AI's Coconut (December
2024) demonstrated LLM reasoning entirely in continuous latent space,
outperforming chain-of-thought.  Continuous thought vectors naturally
encode multiple alternative reasoning paths simultaneously —
breadth-first search natively in continuous space.

**Additional validation.**  Residue Hyperdimensional Computing (Kymn
et al., Neural Computation, January 2025) unified residue number
systems with HDC for both addition and multiplication.  The Neural
Field Turing Machine (Malhotra et al., August 2025) demonstrated the
first differentiable continuous-field computer.  Microsoft's
RenderFormer (SIGGRAPH 2025) replaced the entire graphics pipeline
with a transformer over tokenized scene embeddings.  FastLGS (2024)
achieved real-time semantic 3D querying at 70 FPS via CLIP-on-Gaussians.

**Honest caveats.**  Noise accumulation limits compositional depth to
~10-20 steps without cleanup at leOS's target dimensions — the
cleanup memory is essential.  Exact integer arithmetic requires
careful encoding via residue number systems.  These are engineering
challenges, not theoretical barriers.


## Architecture

```
┌──────────────────────────────────────────────────────────┐
│  Browser (Three.js 3D desktop / 2D canvas fallback)      │
│  Agent perception layer · Human observation window        │
└────────────────────────────┬─────────────────────────────┘
                             │  HTTP / WebSocket
┌────────────────────────────┴─────────────────────────────┐
│  SDOL — Semantic Driven Operation Layer                   │
│  Bone chains · FABRIK planner · Dynamic tool selection    │
│  Scopes · Plans · Task orchestrator · Context assembly    │
├──────────────────────────────────────────────────────────┤
│  Kernel — 540+ instructions                               │
│  Vector math · Storage · Routing · Apps · LLM escalation  │
│  Filesystem · Network · Dreaming · Scopes · Plans · Math  │
├──────────────────────────────────────────────────────────┤
│  LVM — Latent Virtual Machine                             │
│  Spherical geometry · SDF regions · Displacement codec    │
│  Partitions · Reflex arc · Gravitational lens             │
├──────────────────────────────────────────────────────────┤
│  Embedding Processors (all CPU)                           │
│  nomic-text (768d) · nomic-vision (768d)                  │
│  Qwen3-Embedding (1024d) · ImageBind (1024d multimodal)   │
└──────────────────────────────────────────────────────────┘
```

**LVM** (Latent Virtual Machine) is the hardware layer.  Four
pretrained CPU-only embedding models produce vectors.  All math uses
spherical geometry on the unit hypersphere: exp_map replaces addition,
log_map replaces subtraction, SLERP replaces interpolation, parallel
transport moves vectors between reference frames.

**Kernel** dispatches 540+ instructions across categorized files
(`kernel_storage.py`, `kernel_apps.py`, `kernel_reflex.py`,
`kernel_vsa.py`, `kernel_math.py`, `kernel_science.py`, and so on).
It never calls an LLM directly — when language generation is needed,
it escalates to the coprocessor bay.

**SDOL** (Semantic Driven Operation Layer) is the software layer.
Apps are bone chains executed through the kernel.  The FABRIK planner
assembles chains.  The tool relevance scorer selects tools.  The
scope/plan system manages work containers.  The context assembler
builds agent prompts.

**Embedding models** (all CPU, no GPU required):

| Model | Dimensions | Role |
|-------|------------|------|
| nomic-embed-text-v1.5 | 768 | Primary text space.  Search, routing, classification. |
| nomic-embed-vision-v1.5 | 768 | Images in the same 768d space.  Cross-modal search. |
| Qwen3-Embedding-0.6B | 1024 | Deep contextual text.  Context store, code-aware scoring. |
| ImageBind | 1024 | Multimodal: images, audio, text, depth in one space. |


## The Four-Model Architecture

These four models aren't just listed in a config file — they work
together as a system in ways that produce capabilities none of them
has individually.

### Shared-Space Cross-Modal Search

nomic-embed-text and nomic-embed-vision produce vectors in the same
768d space.  This is the foundational trick: embed some text, embed
an image, and cosine similarity between them tells you how related
they are.  CROSS_SEARCH queries both text_store and vision_store
with a single vector.  You can search your image collection with
text descriptions, or find text related to an image, without any
separate indexing or alignment step.

### Cross-Space Translation via Rosetta

The 768d nomic space and the 1024d Qwen/ImageBind space are
different geometries — you can't directly compare a nomic vector
with a Qwen vector.  The Rosetta codec learns a projection matrix
between them via Procrustes alignment (find the orthogonal matrix W
that minimizes ||AW - B|| for paired embeddings).  Once calibrated,
displacements learned in one space broadcast to all four models.
An experience pattern captured by nomic-text becomes available for
Qwen and ImageBind queries.

### Opponent Channels: Disagreement as Signal

When two models embed the same content, their disagreement is
decomposed into structured channels:

- **Agreement channel** — what both models see (shared ground truth)
- **Model-A exclusive** — what A sees that B doesn't
- **Model-B exclusive** — what B sees that A doesn't
- **Magnitude dispute** — same direction, different confidence
- **Purple channel** — A_exclusive + B_exclusive combined, producing
  information that exists in NEITHER model alone

The purple channel is the most valuable.  Like the color purple
(which has no wavelength — it's invented by the brain's opponent
processing of red and blue receptors), the purple signal is genuine
computation performed by the hardware topology itself.  When
nomic-text and Qwen3 disagree about something, the disagreement
pattern reveals nuance that no single model captures.

Disagreement classification sorts results into five types:
redundant, complementary, contradictory, hierarchical, or novel.
A divergence interrupt fires when cross-model disagreement exceeds
a threshold — the system notices when its models see something
fundamentally differently and flags it for attention.

### Synesthesia: Cross-Modal Data Transformation

This is where the four models produce capabilities that most people
would say embedding models can't have.

The synesthetic encoder (`synesthetic_encoder.py`) converts
arbitrary data — numbers, vectors, byte arrays, state dicts,
anything — into synthetic inputs for EVERY available modality
encoder.  Each encoder captures different structural properties
of the same underlying data:

- **Vision** — spatial relationships, color gradients, texture
- **Audio** — temporal patterns, rhythm, frequency relationships
- **Depth** — hierarchy, containment, near/far layering
- **Thermal** — priority, urgency, confidence gradients
- **IMU** — dynamics, acceleration, rate-of-change patterns

All the resulting embeddings land in ImageBind's shared 1024d space.
Opponent channels triangulate between them.  The intersection of
their agreement regions gives much higher precision than any single
encoding.

**The vector-as-image trick.**  A 768d nomic vector has 768 floats.
768 = 256 × 3 (RGB).  Pack those floats into a 16×16 RGB image and
embed it through ImageBind's vision encoder.  Now you have a 1024d
representation of that nomic vector in ImageBind's native space —
no Rosetta projection needed, no linear approximation.  The vision
encoder preserves spatial relationships between nearby floats in the
original vector because they become nearby pixels in the image.

**Multi-view bypass.**  Take that image and apply five transforms:
original, inverted, high contrast, posterized, solarized.  Embed
each one through ImageBind.  The constellation of five embeddings
characterizes the vector far more richly than any single image,
because the vision model's neural network responds nonlinearly to
each transform.  The displacement between views — how the model's
perception changes across transforms — is the most discriminative
representation because it strips away the shared "it's a small grid"
component.

**Data as sound.**  The same numerical data is sonified into audio
using four strategies: frequency sweeps (values become pitch over
time), rhythm (values become click onset patterns), chords (values
become simultaneous frequencies), and modem encoding (OFDM-style
spectral constellations tiling the mel spectrogram).  The modem
strategy was tested at 6x better spectrogram-level discrimination
than frequency sweeps.  Each strategy produces a WAV file that
ImageBind's audio encoder embeds into the same 1024d space as the
image encodings.

**Data as depth.**  Multi-layer rotated autostereograms encode data
as parallax offsets at four angles (0°, 45°, 90°, 135°), mapped to
RGB channels plus luminance modulation.  The vision encoder sees
texture patterns; a depth encoder reads the disparity.  Four
independent parallax channels give 4x the spatial resolution per
dimension compared to a single-layer stereogram.

**Consensus embedding.**  With 7+ modality pathways producing
embeddings of the same data, the consensus function weights each
pathway by its agreement with the group.  Pathways that agree get
more weight; outliers get suppressed.  Redundant pathways (e.g.,
three thermal-like encodings) are deduplicated before voting so
they can't form a bloc that drowns out a genuinely independent
pathway.  The result is more robust than any single encoding.

**Practical example: "Show me Solana price data as a particle
simulation."**  This request crosses domains that most systems
can't bridge.  In leOS, the FABRIK planner assembles a bone chain:
fetch price API → extract time series → `data_to_particles` (which
auto-maps the time column to X, highest-variance column to Y,
volume to particle size, anomaly scores to color heat) → render in
the Three.js desktop.  The data_to_particles bone analyzes each
column statistically, detects the monotonically increasing time
column, maps dimensions by variance, flags anomalous points with
larger sizes, and produces a standard particle system compatible
with the physics engine.  If you ask for `physics_mode="gravity"`,
the particles attract to clusters, revealing structure in the price
data that a line chart would never show.  If the chain fails (the
API doesn't return what was expected), the failure trajectory is
recorded, and next time the planner tries a different path.

This works because the system doesn't need a pre-built "crypto
price visualization" tool.  It composes one from parts: an API bone
for fetching, a math bone for data-to-particles, and a display bone
for rendering.  The FABRIK planner connects them because the output
types match the input types.  Synesthetic encoding means the
intermediate data can be analyzed, compared, and routed through
embedding space at every step.

### Math in Embedding Space

leOS does math — not by sending "what is 2+2" to an LLM, but
through a dedicated numpy-only math engine with 33 kernel
instructions across six domains: basic math (evaluation, constants,
unit conversion), statistics (descriptive, correlation, regression,
polynomial fitting, histograms), linear algebra (matrix multiply,
inverse, eigendecomposition, SVD, solve Ax=b), signal processing
(FFT, bandpass/lowpass/highpass filtering, cross-correlation, peak
detection, power spectral density), time series (smoothing, trend
detection, anomaly detection, forecasting, autocorrelation), and
physics (N-body particle simulation, Euler integration, SPH fluid
dynamics, smoke/buoyancy simulation, collision detection).

All 30 math operations are registered as bones with typed inputs and
outputs, so the FABRIK planner can chain them with any other bones
in the system.  "Fetch this dataset, compute the FFT, find the
peaks, and save a knowledge base article about the frequency
content" is a bone chain the planner can assemble on the fly.

The embedding models contribute to math capabilities in two ways.
First, tool selection routes math requests to the right operations
via semantic similarity — "what's the correlation between these
columns" finds STATS_CORRELATE without string matching or keyword
rules.  Second, the synesthetic encoder can run the results through
ImageBind's vision encoder (data-as-heatmap) and audio encoder
(data-as-frequency-sweep) simultaneously, producing cross-modal
embeddings that can be compared against other datasets by meaning.
This is how the system can answer "find me datasets that look
similar to this one" — it compares the synesthetic fingerprints
of different data, not the raw numbers.

### LSB Steganography and Fountain Codes

The synesthetic encoder includes a steganographic data layer.
Arbitrary bytes can be hidden in the least-significant bits of image
pixels — the vision encoder can't see the difference (it was trained
on JPEG-compressed images where LSBs are pure noise), but the system
can recover the exact bytes later.  A 224×224 RGB image holds ~37KB
of hidden storage at 2 bits per channel, or ~56KB at 3 bits per
channel.

The same data can simultaneously be hidden in the phase domain of
audio signals (spectral audio steganography, ~1.5KB per 2-second
clip) and encoded as color QR overlays (~500 bytes per overlay).
Fountain codes (Luby Transform codes) spread the data across all
available channels so that ANY sufficient subset can reconstruct
the original — if one model isn't loaded or one encoding is
corrupted, recovery still works from the remaining channels.

This creates a layered data architecture: approximate search via
embedding similarity finds the right neighborhood, then exact
recovery via steganography returns the precise original data.
Encrypted payloads add AES-256-GCM encryption with content-dependent
keys derived from the carrier image's own embedding, so different
images produce different encryption keys automatically.


## FABRIK and the Bone Chain Assembly System

This is the engine that lets leOS assemble custom tool chains on the
fly instead of relying on a fixed set of pre-wired capabilities.
The approach borrows from four different fields, each contributing
a technique that traditional agent frameworks don't use.

### Bones, Joints, and Skeletons

Every capability in leOS is registered as a **bone** — a typed atomic
operation with declared input types, output types, a cost tier, and
an embedding of its description.  "Embed text" is a bone.  "Fetch a
URL" is a bone.  "Call the dexscreener API /search endpoint" is a
bone.  Each one is a rigid unit that doesn't deform — it just has a
shape (its type signature) that determines what it can connect to.

**Joints** are connection rules between output and input types.  A
joint says "text_content can connect to text_input with direct
coupling" or "json_response connects to structured_data via a
transform bone that parses the JSON."  Some joints are direct (the
types are compatible as-is), some require a transform bone to be
inserted as an adapter.

**Skeletons** are saved bone chains that worked before.  When the
agent successfully completes a multi-step task using a chain of
bones, that chain is saved as a skeleton with a confidence score
and an embedding of the goal it achieved.  Next time a similar goal
comes up, the planner checks the skeleton library first — and if a
skeleton matches above 0.80 similarity, it's reused instantly
without solving from scratch.

### FABRIK: Inverse Kinematics for Task Planning

FABRIK (Forward And Backward Reaching Inverse Kinematics) is an
algorithm from character animation.  In animation, you want to
figure out how to position a chain of rigid bones (an arm, a leg)
so that the end effector (a hand, a foot) reaches a target point.
FABRIK solves this by alternating backward passes (start at the
target, work toward the root) and forward passes (start at the root,
work toward the target), iterating until the chain converges.

leOS applies the same algorithm to task planning.  The "bones" are
capabilities, the "target" is the goal state, and the "root" is the
current state.  The planner:

1. **Checks the skeleton library** for a known-good chain that
   matches this goal (similarity >= 0.80).  If found, reuse it
   immediately — zero solving needed.

2. **Backward pass**: starting at the goal embedding, searches for
   bones whose outputs match what the goal needs.  At each step, it
   tracks what TYPE the next bone requires as input and searches for
   bones that PRODUCE that type, ranked by semantic similarity.
   This is type-aware search, not just "find something that sounds
   right."  Candidates are re-ranked using learned success history:
   joint affinity scores (how often this bone co-succeeded with the
   previous bone) and nutrient density (how successful this region
   of embedding space has been).

3. **Forward pass**: starting at the current state, walks the
   proposed chain and verifies that each bone's output types connect
   to the next bone's input types.  When a connection doesn't work,
   the forward pass tries three repair strategies: insert a transform
   bone as an adapter, find a bridge bone that accepts the current
   output and produces what the next bone needs, or replace the
   incompatible bone with a type-compatible alternative that's
   semantically similar.

4. **Convergence check**: measures the semantic distance between
   the chain's predicted output and the goal.  If below threshold
   (0.05), the plan is ready.  If not, iterate — up to 5 passes.

The result is a validated chain of typed operations that connects
the current state to the goal, with cost estimates (each bone has a
cost tier from "free" to "gpu_heavy") and a reachability assessment.

### Raymarching Through Capability Space

Borrowed from demoscene sphere tracing.  When FABRIK needs to find
bones between the current state and the goal, it can cast a ray
through embedding space and use SDF (Signed Distance Field) values
to determine step sizes.  The SDF tells the planner how far away the
nearest useful capability is.  Dense regions (many tools) produce
small careful steps.  Sparse regions (few tools) produce big jumps.
Empty regions are skipped entirely.  This makes search adaptive to
local capability density rather than using a fixed grid.

### Proportional Navigation

Borrowed from missile guidance systems.  When the agent is mid-task
and the goal seems to be drifting (new information changes what
"success" looks like), proportional navigation computes a course
correction.  The correction is proportional to the line-of-sight
rotation rate times the navigation constant N' times the closing
velocity.

Each agent type has a tuned N' value: researchers and analysts use
conservative values (2.5 — small corrections, never overshoots),
coders and architects use the optimal value (3.0 — minimizes total
effort), and creative agents use aggressive values (4.0 — bold moves,
front-loaded corrections).  N' adapts over time based on success
rates — high success allows more aggression, low success forces
conservatism.

The zero-effort miss metric tells the system how much correction is
needed per remaining budget unit.  When budget is running low and
distance to goal is still large, urgency spikes and the system
invests more compute.  When the goal is close and budget is
plentiful, it coasts.

### Predictive Preparation

When the planner has a solved chain, it looks ahead at upcoming bones
and identifies resources they'll need.  If step 3 needs a URL
fetched, the system can prefetch it during step 1.  If step 4 needs
an embedding, it can pre-embed during step 2.  Preparation tasks
run on cheap CPU workers (bots) while the main model works on the
current step.

### Decision Trees: Routing Without LLM Calls

Not every decision needs the LLM.  Decision trees handle structured
routing: given a situation, which of several possible actions should
the system take?

Trees are defined declaratively, not generated by the LLM.  Each
node is either a **CheckNode** (a Python function — "does this file
exist?", "is the response longer than N characters?", "did the tool
return an error?") or an **LLMNode** (a constrained question posed
via quick_ask, where the answer is guaranteed to be one of the
allowed choices).  Leaves are actions: continue, retry, escalate,
replan.

CheckNodes cost zero LLM tokens.  LLMNodes use the lightweight
utility model (0.8b) rather than the main model.  A typical decision
tree resolves a post-step validation (should we continue, retry, or
replan?) with 0-2 cheap LLM calls instead of burning the main
model's context on routing logic.

The decision tree system includes evolution: tree effectiveness is
tracked from displacement logs, the dreaming engine proposes
threshold adjustments, and void detection identifies situations where
no tree exists — suggesting new trees to be created.

**Response-quality classifier.**  The decision tree library ships
with five reference embedding corpora (`non_answer.json`,
`plan_only.json`, `process_only.json`, `placeholder_content.json`,
`off_topic.json`) that the post-step validator uses to detect
"describing instead of doing" failures — responses that talk about
what they would do without actually doing it, or that produce a plan
when the user wanted a result.  Without these example libraries, the
classifier has no reference points and every response short-circuits
to "real_answer."

### XPBD Constraint Solving

The constraint solver validates bone chains using XPBD (Extended
Position-Based Dynamics) from physics simulation.  Each constraint
has a compliance parameter: alpha=0 means rigid (type safety — must
satisfy), alpha>0 means soft (style preference — flexes under
pressure).  The solver iterates like a ragdoll physics engine,
prioritizing rigid constraints while letting soft ones settle.

Type safety and output format are rigid (alpha=0.0).  Semantic
coherence has slight flex (alpha=0.1).  Performance targets are
flexible (alpha=0.3).  Style preferences are very soft (alpha=0.5).
This means the planner can bend non-critical constraints to make a
chain work rather than failing because a style preference wasn't
perfectly met.

### Multi-Chain Coordination

When multiple bone chains need to execute (coordinated bot groups),
the multi-chain solver allocates shared resources.  It enforces GPU
concurrency limits (only N chains get GPU at once, sorted by
priority), observation rate caps (reduce the noisiest chain's rate
if the total exceeds the limit), and escalation budgets.  This is
planning-time only — it produces a conflict-free execution order.

### How It All Fits Together

When the agent receives a task:

1. Dynamic tool selection picks the 6-8 most relevant tools from
   the registry (3-pass scoring: domain routing, semantic+keyword,
   usage history).

2. If the task needs multiple steps, the planner checks the skeleton
   library for a known-good chain.  If found, it reuses it.

3. If no skeleton matches, FABRIK assembles a new chain — backward
   pass to find bones, forward pass to validate types and insert
   adapters, constraint solver to verify the chain is sound.

4. The chain executes.  At each step, decision trees handle routing
   (continue/retry/replan) using cheap CheckNodes and utility model
   LLMNodes.  Predictive preparation prefetches resources for
   upcoming steps.

5. Proportional navigation adjusts course if the goal drifts
   mid-execution.  Zero-effort miss tracks urgency.

6. If the chain succeeds, it's saved as a skeleton.  Joint
   affinities update.  The nutrient field records success.  Next
   time, this path is faster.

7. If the chain fails, the failure trajectory is recorded.  The
   skill assimilator notes the gap.  Next time, the planner avoids
   this path and tries an alternative.


## The Tiered Execution Ladder and Retry Escalation

The orchestrator picks the cheapest tier that can plausibly answer
each request.  When the user isn't satisfied, a retry button bumps
them up one rung at a time.

**Tier 0 — FABRIK only.**  Pure bone chain execution, no LLM
involvement.  The substrate-gather decision tree, the reflex arc, and
deterministic research routing all live here.  Cost: free.

**Tier 1 — intern model.**  The 0.8B utility model (CPU) handles the
request.  Used for status questions, simple lookups, structured-output
extraction, and anything the intern can plausibly do without the
full agent context.  Cost: a few hundred CPU tokens.

**Tier 2 — main agent.**  The full 9B model (GPU) with the complete
tool loop, scope context, and plan execution.  This is where complex
reasoning, multi-step plans, and creative work happen.  Cost: the
expensive path.

Every response carries a `tier_used` field on its plan record.  When
the user clicks "try again" on a Tier-0 or Tier-1 answer, the system
reads that field, increments by one, and re-runs the same request at
the next tier with the user's optional hint added to the prompt.
At Tier 2, the retry button changes meaning — there's no higher tier,
so the button either disappears or becomes "report as unresolved"
which logs the case for later review.

The orchestrator records every tier choice and every retry (with
feedback text if provided) on the plan, so the system-wide learning
loop has data to calibrate from.  Over time, the system learns which
kinds of requests reliably succeed at lower tiers vs. which need to
start at Tier 2.

The existing `force_main_agent` button is the original instance of
this pattern — a Tier-1→Tier-2 escalation that's been generalized to
work at every tier transition.


## Substrate Gather: The Pre-LLM Decision Tree

Before any classified user query reaches the LLM, the substrate-
gather package (`bots/substrate_gather/`) runs first.  This is the
mechanism that turns "what is Xavier" from a 30-second LLM round trip
into a 100ms KB lookup when an article on Xavier already exists.

The companion brain classifies queries into six categories:
**status_check**, **codebase_question**, **system_question**,
**feedback_for_agent**, **general_chat**, and **research**.  For
the first three (status, feedback, chat), substrate gathering doesn't
help — they're handled directly without lookup.  For the other three,
each has its own sub-tree:

**research.py** is the only fully implemented sub-tree.  It extracts
entities from the query (token addresses, URLs, DOIs, arXiv IDs,
GitHub repos), queries the knowledge base, runs research-source
routing (see next section), and decides whether to format an answer
directly from the KB, combine KB context with API results, fire an
API call, or escalate to the intern.

**codebase.py** and **system.py** are stubs today.  They escalate
to the brain's existing fetcher pipeline, leaving the architectural
hook in place for later sub-tree implementations.

Every sub-tree returns the same shape: an action
(`format_from_kb`, `format_combined`, `format_from_api`,
`escalate_intern_think`), a confidence score, the path through the
decision tree (for debugging), and a payload of gathered evidence.
Callers threshold on confidence — `>= 0.70` is solid, `>= 0.85` is
very strong.  Below 0.70 the substrate result is treated as advisory
and the normal handler pipeline runs anyway.

The package sits next to `companion_brain.py` in `bots/`.  When
substrate gather can't import (bad install, stale flat module), the
brain catches the ImportError and falls through to its old pipeline
gracefully — the system still works, just without the short-circuit.


## Research Source Routing (Plan 24)

When the substrate-gather research tree needs to fetch external
data, it doesn't hand a free-text query to a generic web search.
Instead it dispatches to a curated **peer group** of sources that
are known good for that kind of query.

The source registry (`source_registry.py`) catalogs every external
source the system has registered — APIs learned via the API adapter
plus URLs from the curated web directory.  Sources are organized
into named peer groups (`crypto_market_data`, `scientific_papers`,
`code_repos`, etc.) defined in `data/research/peer_groups.json`.
Each group has a topic vector computed from its members'
descriptions.

The research router (`research_router.py`) is the reflex-arc path
for research queries:

1. Extract real-world entities from the query (regex extraction —
   Solana addresses including pump.fun suffix detection, EVM
   addresses, URLs, DOIs, arXiv IDs, GitHub paths).
2. Match the query embedding against group topic vectors to find
   the right peer group.
3. Among that group's sources, rank by historical reliability
   (live counters from `data/research/source_stats.json`) and
   topic relevance.
4. If confidence is high and entities are sufficient to build a
   complete API call, fire the call directly — no LLM round trip.
5. On failure, fall over to the next source in the group.  After
   two consecutive failures, escalate with a full trace.
6. If confidence is mid-range, hand the intern a pre-filled draft
   to verify or correct.  If low, return a ranked source list and
   let the intern pick.

The router is a pure function — no internal state.  All persistent
counters and group memberships live in the registry.  The
`peer_groups.json` file is seeded on first boot from
`SEED_PEER_GROUPS`, after which the user owns it.  Reliability stats
live in a separate file so peer-group edits and runtime counter
writes never fight over the same file.

The router is also exposed as a `RESEARCH_ROUTE` kernel instruction,
so it's callable from tests and SDOL programs without going through
the brain.


## The Curiosity Loop (Plan 23)

When leOS does research, it doesn't stop after one tool call.  The
curiosity loop turns every tool result into a list of follow-up
candidates and decides which are worth pursuing.

The classic failure mode it prevents: an agent calls
`leos_api(service='dexscreener', endpoint='get_token_by_address')`,
gets a clean JSON payload that includes `info.websites` and
`info.socials`, and writes a report saying "the project has a
website and Twitter presence" without ever reading either.  The
*signals* for what to investigate next were in the response — the
response itself named them.

The curiosity policy works in three steps:

**1. Candidates come from tool results, not from guesses.**  Every
relevant tool result already contains follow-up signals: URLs,
socials, citations, entity mentions, schema-tagged fields.
Extraction is format-aware: HTML uses the existing link-harvest path,
API responses use a `discover_fields()` walker, long pages that
already trigger intern summarization contribute their `ENTITIES:`
and `USEFUL LINKS:` sections for free.

**2. Internal cross-reference runs before any external fetch.**  Each
candidate gets embedded and queried across every accumulated
partition — `text_store`, `vision_store`, `multimodal_store`,
`context_store` — plus the KB, site_knowledge, and web_directory.
This uses the existing `CROSS_SEARCH` instruction.  Sub-second
similarity across multimodal memory makes "have we seen this before?"
essentially free.  External fetches only happen for candidates that
fail internal lookup.

**3. Coverage saturation stops the loop.**  As candidates resolve,
the system tracks how much of the original goal's embedding has
been "covered" by accumulated findings.  When coverage saturates —
new candidates stop adding signal, marginal information gain drops
below threshold — the loop stops.  This is the stopping rule that
matters as much as the pursuit rule; without it, curiosity is an
infinite loop.

The curiosity loop is what lets a research request go one or two
levels deep without an explicit multi-step plan from the user.
It's also why leOS's research depth scales with its accumulated
memory: more past data means more candidates resolve internally,
which means deeper research at lower cost.


## Scopes, Plans, and the Orchestration Lifecycle

Scopes and plans are how leOS organizes work.  A scope is a named
container; a plan is a sequence of steps.  Plans live inside scopes.
Scopes nest inside other scopes.  The orchestrator executes plans
step by step, creating ephemeral child scopes for context isolation.

### Scopes: The Universal Work Container

A scope is a flexible work container.  What a scope IS depends on
what fields are set:

- Scope with a **goal** → behaves like a project
- Scope with a **schedule** → behaves like a service
- Scope with **both** → a monitored initiative
- Scope with **neither** → a folder

Every scope has: id, name, description, status, parent_id, goal,
success_criteria, plan_ids[], notes[], tags, wiring[], config, and
timestamps.  Statuses follow a lifecycle: **active** → **waiting**
→ **complete** (or **paused**, **needs_replan**, **archived**).

Notes are typed observations attached to a scope: **decision** (a
choice that was made and why), **observation** (something noticed
during work), **post_mortem** (what was learned after completion),
and **general** (everything else).  Decision notes are the primary
mechanism for passing information between plan steps — when a child
scope completes, its key finding crosses the boundary into the
parent scope as a decision note.

Scopes nest via parent_id.  A research project scope might contain
child scopes for each sub-investigation.  The path string
("Research / Solar Panel Efficiency / Monocrystalline Analysis") is
computed automatically by walking up the parent chain.  Top-level
scopes have parent_id = null.

### Plans: Structured Multi-Step Execution

A plan has: id, goal, steps[], scope_id, tags, status.  Each step
has: description, deliverable, success_criteria, status, result,
depends_on[], and notes[].

**Deliverables are verification criteria**, not vague descriptions.
"FITS files saved to /data/fits/" is a deliverable.  "Download the
data" is not.  The orchestrator verifies each deliverable after
execution — if the step says a file should exist, the system checks
that the file exists.

Plans link to scopes via scope_id.  A scope's plan_ids[] array
tracks which plans belong to it.  Multiple plans can live in the
same scope (e.g., a main plan and a contingency plan, or sequential
plans for different phases of work).

### Projects, Goals, and Auto-Population

Projects (`project_manager.py`) are higher-level workspaces — folders
under the workspace root with their own metadata, conversation
history, working files, and per-project skills.  Each project has a
`project.json` and a sluggified ID derived from its name.

Project goals (`project_goals.py`) replace the old "user_message
string as a project goal" pattern with structured deliverables.  A
goals file holds a project summary and multiple goals, each with a
title, description, optional deliverables (concrete outputs to
verify against), status tracking, and a `can_parallel` flag.  This
gives the orchestrator a structured brief instead of a freeform
prompt.

Goal auto-population (`goal_auto_populate.py`) bridges the gap when
a user provides a freeform request.  A structured LLM call extracts
goals and deliverables, and the result is saved as a leOS plan in
`data/plans/` where each deliverable becomes a step with verification
criteria.  This lets the agent track progress step-by-step and lets
the system verify deliverables were actually produced before
declaring success.

### Scope Wiring: Triggers, Dependencies, and Constraints

Wires connect scopes to each other and to plans, bots, and KB
articles.  Three wire types:

- **Dependency** — gates a scope until a condition is met ("don't
  start this scope until scope X is complete")
- **Constraint** — an invariant that must hold; fires an effect if
  violated ("if the error rate exceeds 5%, pause this scope")
- **Trigger** — fires once when a condition transitions false→true
  ("when the data arrives, start processing")

Conditions can reference any scope's fields, any plan step's status,
or computed virtual fields like age_seconds, idle_seconds, and
notes_count.  This creates reactive relationships between work
containers without hardcoding the coordination logic.

### The 8-Layer Context Assembly Engine

When an agent starts working within a scope, the context assembler
(`scope_context.py`) builds the right context for the right moment.
Eight layers, each with a priority and token budget:

0. **Scope Identity** (~50 tokens) — always included, tells the
   agent where it is and what the scope is about
1. **Current Task** (~200-500) — the specific task, wire gates
2. **Active Plan State** (~200-400) — plan summary, which steps are
   done, what's next, prior step results
3. **Recent Scope Activity** (~200-600) — notes, bot observations
4. **Relevant Knowledge** (~300-800) — KB articles found by
   embedding similarity to the current task
5. **Parent Scope Context** (~100-300) — parent's goal, key
   decisions (this is how deliverables from sibling steps flow in)
6. **Institutional Memory** (~100-400) — similar past tasks and
   their outcomes from the displacement log
7. **Sibling Awareness** (~100-200) — what peer scopes are doing

Lower-priority layers are trimmed or dropped when the token budget
runs out.  Relevance scoring weights semantic similarity (50%),
recency (30%), author authority (10%), and note type (10% —
decisions rank higher than general observations).

### The Orchestration Lifecycle

When a user makes a request that requires multiple steps, the
orchestrator (`task_orchestrator.py` plus eight specialized
sub-modules — corrections, step_utils, media, planning, verification,
scope, reflection, and helpers) runs an 8-step lifecycle:

**1. PLAN** — One LLM call breaks the user request into steps with
concrete deliverables and success criteria.  The prompt includes
lessons from similar past tasks (found by embedding similarity in
the displacement log) so the system doesn't repeat mistakes.

**2. PERSIST** — The plan is saved via PLAN_CREATE and linked to the
parent scope.

**3. CLASSIFY** — Each step is classified as `ingest` (contains a
URL that the media pipeline handles — no LLM involved), `delegate`
(monitoring task that a bot handles better), or `think` (requires
LLM reasoning and tool use).

**4. SCOPE** — Each step gets its own ephemeral child scope.  This
is the context isolation mechanism: tool calls, retries, and
intermediate work accumulate in the child scope, never polluting the
parent.

**5. EXECUTE** — Ingest steps run at the Python level (media
download, wait for processing, poll for completion).  Think steps
run the LLM tool loop with a focused tool subset inside the child
scope's context.  The LLM never polls.  The LLM never sees tools it
doesn't need for this specific step.

**6. VERIFY** — After each step, the output is checked via
DRIFT_RELEVANCE (is the response semantically aligned with the
task?) and deliverable verification (does the concrete artifact
exist?).  If verification fails, the intern model analyzes what
went wrong, and the step retries with that analysis injected into
the prompt.

**7. DELIVER** — The intern model summarizes the step result into a
compact deliverable.  This summary crosses the scope boundary into
the parent scope as a decision note.  The child scope is archived.
Subsequent steps see prior deliverables through the parent context
layer (Layer 5).

**8. COMPLETE** — After all steps finish, the overall goal is
verified.  The parent scope status moves to complete.  A post-mortem
learning entry records what worked and what didn't, embedded for
future retrieval.

The key design principle: **the LLM should only run when there is
THINKING to do.**  Waiting for a download is not thinking — it's a
Python sleep loop.  The LLM runs to decide what to do, the
orchestrator handles the mechanics, and the LLM runs again when
results are ready.

### Simplified Single-Agent Orchestration

The current orchestrator (`leos_orchestrator.py`, ~300 lines) replaces
an earlier architecture (~10,400 lines across `orchestrator.py` and
`agent_factory.py`) that coordinated multiple qwen-agent Assistant
instances through a Director/Worker pattern.  The old system had
separate agents — Director, DevOps, Librarian, Coder, Researcher —
each with a subset of tools, and the Director created plans, delegated
to workers, reviewed output, and replanned.

The simplification came from a single insight: **leOS has ONE agent
with 36 tools, and the tools ARE the specialists.**  The agent plans,
executes, and reviews in a single session, and the tool-calling loop
in `agent_session.py` handles the generate → tool_call → execute →
feed-back cycle automatically.  No hand-offs to marshal, no
inter-agent context passing, no Director-vs-Worker callbacks.  The
result was a 35x reduction in orchestration code while preserving
every behavioral capability.  Dynamic tool selection narrows the 36
to the most relevant 6-8 per task, so the agent never sees the full
set in any single turn.


## How the System Learns

These mechanisms work together to make leOS improve with use.

**Displacement codec.**  Every agent interaction records the
input-to-output trajectory as a tangent vector on the hypersphere.
Similar trajectories compress into shared I-frames (keyframes) and
P-frames (deltas), like H.264 video compression.  The codec doesn't
store responses — it stores patterns of transformation.

**Reflex arc.**  When enough consistent displacements accumulate in a
region, the reflex engine fires cached responses without calling the
LLM.  Conformal prediction provides statistical confidence bounds.
Familiar patterns bypass the LLM entirely and replay from geometric
cache in microseconds.

**Skeleton library.**  Successful bone chains are saved as skeletons
— pre-validated patterns.  When the FABRIK planner encounters a
similar goal, it tries known skeletons first before assembling a new
chain.  The library grows with every successful task.

**Tool selection memory.**  Every agent session records which tools
were actually used for which tasks.  This usage history feeds back
into the scoring algorithm (Pass 3, 20% weight blend).  Over time,
the system learns that "PDF table extraction" reliably needs
`doc_query`, not `leos_files`.

**Skill assimilator.**  Tracks capability gaps — tasks where no tool
scored well.  Gap vectors cluster naturally; many requests for the
same missing capability form a dense cluster.  When frequency crosses
a threshold, the system can generate a new tool from existing parts.

**Void detection.**  The KB void map probes the space between
knowledge clusters to find gaps.  "Know Python, know async, but no
article on Python async" is a void.  The dreaming engine can
autonomously research and fill these gaps during idle time.

**Self-extending instructions.**  When an LLM escalation succeeds on
a novel task, the displacement compiler captures the trajectory and
the one-shot transfer system creates a permanent reflex arc entry.
One successful LLM call can teach the system to handle all similar
tasks without LLM involvement.

**Source reliability tracking.**  Every research-router dispatch
updates `data/research/source_stats.json` — counters for success,
failure, and average latency per source.  Future dispatches rank
peers by reliability, so a source that consistently times out or
returns errors gets demoted automatically.  No human has to flag
bad sources; the data does it.

**Dreaming engine.**  During idle time: consolidate the displacement
codec, run void detection, grow/prune the living medium (nutrient
field), check reflex arc hit/miss rates, compact stale scopes, audit
registered bones for failures, render deferred thought monologues,
generate reflections from unprocessed learning experiences, and
attempt self-repair.  The system uses itself to improve itself.


## Voice, Thought Canvas, and the Inner Monologue Learning Loop

This is where drift detection, voice synthesis, visual rendering,
and the knowledge base connect into a single learning loop.  A
flagged learning experience becomes a narrated thought video that
gets triple-embedded and stored as a searchable knowledge base
article.  Future agents find these videos by meaning and learn from
past mistakes without anyone writing documentation.

### The Thought Canvas: Visual Thinking

The thought canvas (`thought_canvas.py`) is a 256×224 pixel numpy
array where agents render 2D Gaussian splats while they work.  Each
splat is a small blob with position, size, opacity, and color.  The
canvas isn't decorative — it's a spatial workspace where the agent
can lay out concepts, show relationships, and visualize its process.

The canvas API is simple: `make_circle` to represent a concept,
`make_background` for context, and direct splat placement for
emphasis.  Agents emit THOUGHT_EMIT kernel instructions during work,
which write splats to the canvas.  The `/thought` web page shows
the canvas in real time.

### EmotionMapper: Drift State Becomes Voice

The EmotionMapper class is the bridge between the drift detector's
geometric measurements and ChatterboxTTS's voice parameters.  Each
drift classification maps to an emotional profile:

**Redshift** (diverging from expectations) → uncertain delivery.
Speech rate drops to 0.85×, exaggeration is restrained (0.4),
pauses come before speaking (the voice hesitates).  At mild
magnitude: `[sniff]`.  At strong magnitude: `[sigh]`.

**Blueshift** (converging toward target) → excited delivery.
Speech rate rises to 1.15×, exaggeration increases to 0.7, speech
flows freely with no pauses.  Mild: `[chuckle]`.  Strong: `[laugh]`.

**Convergence** (arrived, stable) → confident delivery.  Normal
pace, balanced exaggeration, pauses come after statements (for
effect).  Strong: `[clears throat]` (settling in).

**Void** (unknown territory, sparse space) → contemplative delivery.
Speech rate drops to 0.75×, exaggeration is quiet and intimate
(0.3), pauses come both before and after (the voice is thinking).
Mild: `[sniff]`.  Strong: `[gasp]`.

The paralinguistic tags (`[sigh]`, `[laugh]`, `[gasp]`, etc.) are
rendered by ChatterboxTTS Turbo as natural vocal reactions in the
cloned voice.  They're not sound effects — they're generated by the
same voice model that produces the speech, so a `[sigh]` during
redshift sounds like a real sigh from the speaker.

Drift magnitude scales the intensity: a small redshift produces
subtle hesitation, a large redshift produces audible concern.
Confidence from conformal prediction modulates certainty — high
confidence means the emotion is expressed clearly, low confidence
adds wavering.

Voice modulation goes deeper than speech rate and expressiveness.
Each drift state also adjusts the sampling parameters of the TTS
model itself: blueshift lowers min_p (more creative output) and
reduces repetition penalty (more expressive flow), while redshift
raises min_p (more stable output) and increases repetition penalty
(more coherent delivery).  Void pushes both highest — the most
grounded, careful delivery.  The voice isn't just speaking
differently; the model is generating differently.

### ChatterboxTTS: Zero-Shot Voice Cloning

ChatterboxTTS is a two-stage neural TTS model (T3 autoregressive +
S3Gen decoder).  leOS patches it at startup via `patch_chatterbox.py`
to fix float32 dtype mismatches on CPU.  Voice cloning is zero-shot:
provide 5-30 seconds of reference audio and the model matches the
timbre, pitch, and cadence of the speaker.  No fine-tuning required.

The voice library (`voice_library.py`) manages cloned voice
profiles.  Sources for reference audio include direct uploads, audio
extracted from video via ffmpeg, or URLs processed through yt-dlp.
Each profile stores the reference clip path and metadata.  Seven
voices ship preloaded with leOS.  The active inner monologue voice
can be set per-agent.

The `resemble-perth` watermarker is integrated to mark all
synthesized speech as AI-generated.

### The Monologue Renderer: Composing Thought Videos

The monologue renderer (`monologue_renderer.py`) combines everything:
the thought canvas provides the visual frames, ChatterboxTTS provides
the emotionally inflected narration, and the EmotionMapper drives the
emotional parameters from drift state.

A monologue session works like this:

1. **Begin session** — A renderer is created with a voice profile,
   drift state, and mode (realtime or deferred).

2. **Emit lines** — As the agent works, it emits narration lines.
   Each line carries the current drift state from the drift detector.
   The EmotionMapper converts drift_type + magnitude + confidence
   into TTS parameters.  ChatterboxTTS synthesizes the audio with
   the appropriate emotion.  The thought canvas renders the
   corresponding visual frame.

3. **Compose** — When the session ends, ffmpeg composites the audio
   clips and visual frames into an MP4 video.  Video duration is
   driven by audio length — frames are generated or repeated to fill
   the narration time.

4. **Store** — The MonologueStore saves the video as a KB article
   with triple embeddings:
   - **nomic-vision** on a representative frame (768d) — visual
     search finds similar imagery
   - **ImageBind** on the audio track (1024d) — audio search finds
     similar emotional contours
   - **nomic-text** on the transcript (768d) — text search finds
     relevant content

   This means a future agent can find a past thought video by
   searching with text ("how did we handle the API rate limit?"),
   by visual similarity (a similar-looking thought canvas layout),
   or by emotional similarity (a video where the voice had the same
   frustrated/uncertain tone).

### The Learning Loop: From Experience to Searchable Knowledge

Here's how a learning experience becomes permanent knowledge:

**1. Something goes wrong (or right).** During plan execution, the
orchestrator detects that a step failed and had to retry, or
succeeded in an unexpected way, or the drift detector flagged
unusual behavior.  This becomes a "flagged learning experience."

**2. The intern extracts a lesson.** The intern model (CPU, doesn't
block the main agent) analyzes the experience and produces a compact
2-3 sentence lesson: "The Coinbase API returns rate-limit errors as
HTTP 429 with a Retry-After header.  Waiting the specified time and
retrying succeeds reliably.  Don't retry immediately."

**3. The lesson is embedded and stored.** The lesson text is embedded
via nomic-text and stored in the displacement log with
`type: lesson_learned`.  It's immediately discoverable by future
plan generation (step 1 of the orchestration lifecycle checks for
past lessons from similar tasks).

**4. The dreaming engine generates a reflection (idle time).** When
the system is idle, the dreaming engine finds unprocessed
lesson_learned entries and generates reflective inner monologues.
The LLM produces a reflection exploring three questions: "What can
be learned from this experience?", "Why is this worth learning?",
and "Why didn't I already know how to handle this?"

**5. The reflection is narrated and rendered.** The reflection text
flows through the full monologue pipeline: EmotionMapper reads the
drift state that was captured at the time of the original
experience, ChatterboxTTS narrates with the appropriate emotional
tone, the thought canvas renders visual frames, and ffmpeg composes
the video.

**6. The video is triple-embedded and stored as a KB article.**
Now a future agent searching for "API rate limiting" finds: the
original lesson (text), the reflection video (visual + audio +
text), and the emotional context (was the system frustrated?
confused? confident?).  The triple embedding means the knowledge
is accessible from any modality.

### Deferred Mode: Learning During Dreams

In realtime mode, TTS synthesis and video composition happen during
active work — expensive.  In deferred mode, the renderer writes
events to a JSONL log file instead.  Lines, drift states, and
timestamps are captured, but no audio is synthesized and no video is
composed.

The dreaming engine picks up unrendered logs during idle time and
replays them through the full pipeline: Chatterbox TTS, frame
rendering, ffmpeg composition, triple-embedding, KB storage.  This
means the system can log learning experiences cheaply during active
work and render them into searchable videos later, when resources
are free.

The result: every significant experience the system has — every
failure, every unexpected success, every novel pattern — eventually
becomes a narrated, emotionally contextualized, triple-embedded,
searchable knowledge base article.  The system doesn't just learn
from experience; it creates documentation of its own learning
process, accessible to any future agent through any modality.


## The Intern Model and Bots: CPU-Parallel Workers

One of the biggest practical problems with LLM-based systems is
that the GPU is a bottleneck.  While the main agent is generating
a response, nothing else can use the model.  leOS solves this with
a two-tier architecture where a lightweight model and an army of
bots operate on CPU in parallel with the main agent, never competing
for GPU memory.

### The Intern Model (qwen3.5:0.8b)

The intern is a 0.8-billion parameter model that runs on CPU with
`num_gpu=0`.  It's not user-facing — it handles internal bookkeeping
that would be wasteful to run through the main 9B model.  It's
called via the kernel's ASSIST instruction, which checks the reflex
arc first (maybe the answer is cached) before invoking the model.

The intern handles work across 40+ modules in the system:

**Failure analysis** — When a plan step fails, the intern analyzes
what went wrong in 2-3 sentences before the system retries.  This
analysis gets injected into the retry prompt so the main agent
doesn't repeat the same mistake.  The main agent never sees or pays
for this analysis work.

**Deliverable summarization** — When a plan step produces output
that needs to cross a scope boundary (from child scope to parent),
the intern produces a purposeful summary instead of a blind
truncation.  This preserves critical findings while staying within
token budgets.

**Context compaction** — When conversation history grows too long,
the intern summarizes older messages.  The compaction pipeline tries
the intern first (CPU, cheapest), falls back to the main model only
if the intern fails.  This runs while the main agent is idle between
tool calls.

**Blackboard recording** — When the agent completes work, the intern
summarizes it for the shared project blackboard.  Other agents see
the compact summary instead of the full verbose output.

**Decision tree evaluation** — LLMNode questions in decision trees
use the intern rather than the main model.  A typical post-step
validation ("should we continue, retry, or replan?") costs 0-2
intern calls instead of burning main model context on routing logic.

**Plan coherence scoring** — When the orchestrator generates a
multi-step plan, the intern scores it for internal consistency.

**Lesson extraction** — When the agent learns something new during
a task (a flagged learning experience), the intern extracts the
lesson as a compact statement that gets stored in the knowledge
base.

**Status companion** — When the main agent is busy, the companion
brain routes user questions to the intern with structured scaffolding
(embedding-based classification → decision tree → pre-structured
prompt template).  The intern can explain what the agent is doing,
acknowledge user feedback, and post notes to the blackboard — all
without interrupting the main agent's work.

**Structured output extraction** — The two-pass pattern: the main
model generates a response in thinking mode (normal generation),
then the intern does a structure pass (`/no_think` + `json_mode`) to
extract structured data from the response.  This avoids forcing the
main model into a constrained output mode that degrades reasoning.

The intern processes ASSIST calls at ~100-200 tokens/second on CPU.
It's not fast by GPU standards, but it's free — it runs in parallel
with everything else and never blocks the main model.

### Bots: Pure CPU Workers

Bots are the system's subconscious.  They run on schedules, monitor
data sources, detect anomalies, and only escalate to an LLM when
something genuinely needs language understanding.  A bot cycle
(perceive → evaluate → act) runs entirely on CPU — HTTP requests,
file reads, embedding comparisons (~0.1ms each), threshold checks,
regex patterns.  The system can run dozens of bot cycles per minute
without touching Ollama.

Bots are assembled from components, not programmed.  The factory
combines reusable templates:

```python
create_bot("price_watcher", {
    "perceive": {"type": "api_call", "url": "https://api.coingecko.com/..."},
    "evaluate": {"type": "threshold", "field": "price", "op": ">", "value": 50000},
    "act": {"type": "alert_inbox", "message": "BTC above $50K!"},
    "schedule": {"interval_seconds": 300},
})
```

**15 perception types** — `http_fetch` (fetch a page), `api_call` (call a JSON API), `rss_parse` (parse an RSS feed), `file_read_bot` (read a local file), `dir_scan` (list directory contents), `site_crawl` (crawl a site structure), `kb_read` (search the knowledge base), `partition_search` (query an embedding partition), `observation_read` (read the observation ledger), `kernel_query` (execute a kernel instruction), `diff_observe` (detect changes since last cycle), `multi_source` (combine multiple perception sources), `field_extract` (pull a field from structured data), `regex_extract` (regex-match against text), `html_extract` (extract content from HTML).

**18 action types** — `log_observation` (write to observation log), `alert_inbox` (send notification to inbox), `file_write_bot` (write a file), `kb_save_bot` (save a knowledge base article), `escalate_bot` (flag for agent review), `trigger_bot` (run a bone chain), `ingest_pages` (run the media pipeline), `partition_write` (store in an embedding partition), `spawn_child_bot` (create another bot), `kernel_exec` (execute a kernel instruction), `displace_record` (record a displacement), `data_transform` (apply a data transform), `ledger_emit` (publish an event to the subscription bus), `entry_merge` (combine observations), `entry_tag` (add tags to entries), `entry_link` (create cross-references), `partition_promote` (upgrade entries to a higher-tier partition), `llm_infer` (escalate to LLM via ESCALATE instruction).

**Predictive coding** — Bots don't just observe; they predict.
Before each perception cycle, a bot predicts what it expects to see
based on the last observation.  After perceiving, it compares
prediction to reality.  Only prediction errors generate
observations.  A price staying flat produces no records.  A price
jumping 10% triggers an observation because it violates the
prediction.  This filters noise automatically — bots that monitor
stable sources produce almost no data, while bots monitoring
volatile sources produce exactly the interesting events.

**Evaluation types** include threshold checks, regex pattern
matching, embedding similarity comparison (is this observation
close to a reference embedding?), change detection (did anything
change since last cycle?), and composite rules (AND/OR combinations
of simpler evaluators).

**Bot groups** coordinate multiple bots as a team.  The multi-chain
solver (from the FABRIK module) allocates shared resources across
the group: GPU time slots for any bots that need LLM escalation,
observation rate caps to prevent flooding, and priority-based
scheduling.

**Self-spawning** — A bot can create other bots via `act_spawn_bot`.
A "scout" bot monitoring an RSS feed can spawn a "detail" bot for
each interesting article it finds, with the detail bot configured
to fetch, analyze, and summarize that specific URL.  The scout
keeps scanning; the detail bots handle the deep dives.  When a
detail bot finishes, it records its findings and exits.

### How the Three Tiers Work Together

The main agent (9B, GPU) handles user-facing conversation, complex
reasoning, multi-step plans, and creative work.  It has the full
tool set and can call any kernel instruction.

The intern model (0.8B, CPU) handles everything the main agent
shouldn't waste time on: failure analysis, deliverable compression,
context compaction, decision tree routing, structured output
extraction, plan scoring, lesson extraction, user status updates.
It runs in parallel with the main agent.

Bots (no model, CPU) handle everything that doesn't need language
at all: monitoring web pages, polling APIs, watching file changes,
scanning partitions for anomalies, listening on membrane ports,
detecting embedding drift.  They run continuously on schedules,
producing observations that the agent can act on when it's ready.

When a bot detects something that needs language understanding, it
escalates.  The escalation goes through the reflex arc first — if
the system has seen this pattern before, it replays the cached
response without touching any model.  If it's genuinely novel, it
reaches the agent.  This three-tier architecture means the system
is always watching, always working, and always learning, even when
the main agent is busy generating a response.


## Novel Techniques

**SDF regions and gravitational lensing** — Named ellipsoidal regions
in embedding space define semantic boundaries using Signed Distance
Field math from computer graphics.  Union is min(a,b), intersection
is max(a,b), subtraction is max(a,-b) — arbitrarily complex semantic
filters from trivial operations on simple primitives.  The gradient
of the SDF provides a free "direction to nearest boundary" vector for
routing.  The gravitational lens uses a Barnes-Hut tree (the same
O(n log n) algorithm used for galaxy N-body simulation) to warp
query trajectories so that frequently accessed or highly connected
vectors exert pull on nearby queries — geodesic focusing via
Riemannian geometry.

**Holographic cache** — Circular convolution (O(n log n) via FFT)
stores multiple key-value pairs in a single fixed-width vector,
queried with approximate inverse.  Based on Tony Plate's Holographic
Reduced Representations.  You can store `record = key1⊗val1 +
key2⊗val2 + ... + keyN⊗valN` and retrieve any value with
`valI ≈ keyI† ⊗ record`.  Noise accumulates after 10-20 compositions
— the cleanup memory maps noisy vectors back to their nearest clean
representation, analogous to error correction in digital systems.

**Living medium** — A nutrient field modeled on mycelium networks
that tracks information density across embedding space.  Grows toward
areas of activity via success density feedback.  Prunes neglected
regions.  Hub vectors with many adjacencies become knowledge
redistributors (modeled on Simard's "mother tree" research showing
mycorrhizal networks have scale-free topology).  When an agent
succeeds in a region, the nutrient field strengthens; when it fails,
density decreases.  The dreaming engine uses the nutrient map to
focus consolidation on high-value regions.

**Thought externalization** — See "Voice, Thought Canvas, and the
Inner Monologue Learning Loop" above for the full explanation of how
agents render visual thought, drift detection drives emotional voice
synthesis, and learning experiences become triple-embedded searchable
KB articles.


## Drift Detection: Catching Hallucination with Astronomy

The drift detector (`drift_detector.py`) is leOS's quality control
system.  It detects when an agent is hallucinating, looping, going
off-task, or producing shallow non-answers — without making a single
LLM call.  Everything is pure vector geometry on the unit hypersphere.

The core concept is borrowed from cosmological observation:

**Redshift** means the agent's response is drifting AWAY from the
task intent.  The displacement vector (the tangent vector from task
embedding to response embedding, computed via log_map) is unusually
long compared to what the neighborhood predicts.  In astronomy,
redshift means an object is receding.  In leOS, redshift means the
response is semantically receding from the task — hallucination,
off-topic drift, or confabulation.

**Blueshift** means the response is collapsing TOWARD the task too
closely.  The displacement is suspiciously short, or the response
embedding is nearly identical to the task embedding.  In astronomy,
blueshift means an object is approaching.  In leOS, blueshift means
the response is just echoing the task back in different words — a
non-answer like "I'll do that!" rather than actual work output.

Here's how it works:

1. When the agent produces a response, the detector computes the
   geodesic distance between the task and response embeddings.

2. It queries the displacement log for the K most similar past tasks
   and computes the mean and standard deviation of their displacement
   magnitudes.  This is the "neighborhood prediction" — what
   displacement is normal for this region of embedding space.

3. If the actual displacement exceeds the prediction by more than
   1.8 standard deviations: **redshift warning**.  The agent may have
   drifted off-topic.

4. If the actual displacement is below the prediction by more than
   1.5 standard deviations, or if the task-response cosine similarity
   exceeds 0.92: **blueshift warning**.  The response may be shallow
   or formulaic.

5. If the displacement log has fewer than 3 similar past tasks: the
   region is flagged as **void** — unexplored territory where the
   system can't make confident predictions yet.  Not an error, just
   low confidence.

6. **Convergence detection** tracks the last N responses in a session.
   If their pairwise cosine similarity exceeds 0.85, the agent is
   probably stuck in a loop — even if the text looks different each
   time.  Embedding-based loop detection catches semantic loops that
   text comparison would miss.

The drift detector handles quality checking with pure math instead of
LLM calls.  It runs on every agent response automatically and costs
zero LLM tokens.  The redshift/blueshift metaphor also drives the
emotion parameters for thought externalization — an agent experiencing
redshift narrates with more uncertainty, while convergence produces
a frustrated tone.


## Intelligence Infrastructure

Beyond the core embedding operations, leOS has a layer of
subsystems that give the system self-awareness, predictive
capability, and the ability to improve its own internals.

### Predictive Coding (System 1 / System 2)

Based on Karl Friston's active inference framework.  A lightweight
linear predictor per task category estimates the expected output
embedding BEFORE running any agent.  If the prediction is confident
(low expected error), the system uses the predicted response without
LLM inference — this is System 1, fast and automatic.  When the
prediction is uncertain or the task is high-stakes, the full LLM
runs — System 2, slow and deliberate.  Target ratio: System 1
handles ~80% of routine tasks, System 2 handles the ~20% that are
genuinely novel.  Precision weighting adjusts sensitivity per task
type: lower tau for high-stakes decisions, higher tau for routine
work.

### Generation Probe: Reading the Model's Mind

Before the intern model generates even one output token, the
generation probe reads its hidden state after input prefill and
predicts the routing decision: REFLEX (handle from cache), ASSIST
(intern can handle it), or ESCALATE (needs the main model).  The
probe is a simple linear classifier (numpy least-squares) that
trains online from accumulated routing outcomes — no GPU, no
training loop, just `numpy.linalg.lstsq` called every 10 samples.
It starts untrained and improves automatically with use, reaching
92%+ accuracy based on the finding (Ashok & May, NeurIPS 2025) that
model hidden states after reading a task already encode what kind of
computation is needed.

### Activation Steering: Compiled Geometry

The steering library computes activation steering vectors for the
intern model — geometry injected directly into the model's forward
pass.  Run the model on contrastive example pairs (desired behavior
vs. undesired behavior), compute the mean hidden state difference,
normalize to unit length.  At inference time, inject via forward
hook: `hidden += alpha * steering_vector`.  Cost: one tensor
addition per position per token — microseconds.

Default vectors computed at startup: `json_output` (push toward
structured JSON), `concise` (push toward brief responses),
`classification` (push toward single-word labels).  This replaces
fragile prompt engineering with compiled geometric subroutines.

### Voight-Kampff Baseline Calibration

Named after Blade Runner's replicant test.  A fixed set of 40
anchor phrases spanning diverse semantic domains are embedded and
their 40×40 pairwise similarity matrix is saved as the model's
fingerprint.  When the model changes (new version, different
quantization, Ollama update, even temperature variation), the
matrix shifts.  The Frobenius norm of the difference = total model
drift.  Individual pair deviations pinpoint which semantic regions
shifted.

This drift feeds into the drift detector as a threshold adjustment
— if the model itself drifted by 0.05 in average pairwise
similarity, the redshift/blueshift sigma thresholds widen
proportionally to avoid false positives.  Each of the four embedding
models gets its own baseline.

### Proprioception: System Self-Awareness

Proprioception in biology is knowing where your body is in space.
For leOS, it means knowing: how much of the embedding space the
system is currently using (coverage radius, effective
dimensionality), how fast the system's focus is moving (centroid
velocity — rapid drift means chaotic behavior), whether agents are
healthily dispersed or unhealthily clustered, and how many
capabilities are actually being utilized.  All metrics are computed
from embedding vectors already being generated — zero additional
cost.  Anomalous proprioception triggers a review.

### Dark Matter: Hidden Concept Discovery

In astrophysics, dark matter is detected by its gravitational
effects on visible matter.  In leOS, "dark matter" = concepts that
the system consistently works around but has never explicitly named.
Detection: cluster displacement vectors by direction (not magnitude),
look for convergence patterns where multiple unrelated tasks all
point toward the same region.  That region contains a concept the
system implicitly uses but has never articulated.

Cross-modal dark matter detection uses ImageBind: if text tasks
about "debugging" and image analyses of "error screenshots" both
produce displacement vectors pointing toward the same region, that
region represents a cross-modal concept.  Cross-modal convergence is
much less likely to be coincidence than single-modality.

### Danger Model: Damage vs. Novelty

Based on Polly Matzinger's immunological danger model.  The immune
system doesn't respond to foreignness — it responds to damage.  A
novel but harmless substance doesn't trigger a response; a familiar
but damaging one does.

Applied to leOS: novel observations should NOT automatically trigger
escalation (that causes alert fatigue).  Observations that cause
DAMAGE should: error rate increases, repeated tool failures, agent
loops, resource exhaustion, plan step regressions, response quality
degradation.  The danger model adds a damage dimension alongside
the salience network's signal density and the drift detector's
trajectory analysis.

### Observation Ledger and Salience Network

The observation ledger is the stigmergic coordination substrate.
Bots write observations, other bots read them, patterns emerge
without direct communication.  Key operations: write (with dual
embedding), semantic query, reinforce (second bot confirms a
pattern → boost confidence), decay (reduce by age, remove expired),
promote (convert confirmed patterns to permanent KB entries).

The salience network is the attention bridge between the CPU bot
layer and the GPU agent layer.  It runs periodically, checks each
active service's observation density, and schedules an agent session
when density crosses a threshold or a critical observation appears.
This is the "when does the system need to think hard about
something?" decision — it runs on CPU and never blocks the agent.

### Semantic Compass and Success Gradients

Every completed task stores its displacement vector (task → response)
with a success/failure annotation.  Over time, this creates a
gradient field in embedding space: find the k nearest successes and
k nearest failures to the current position, compute the gradient
from the failure centroid toward the success centroid.  The gradient
points the direction that leads to good outcomes in this region of
embedding space.  Strategy synthesis by analogy uses this gradient
to suggest approaches for new tasks based on what worked nearby.

### Generative Raytracing in Embedding Space

The ray engine (`ray_engine.py`) replaces traditional geometric
ray-plane intersection with learned rendering in 768d.  During
bootstrap, real geometric intersection produces ground truth pixels.
Each ray is encoded geometrically into 768d using positional
encoding (sin/cos at multiple frequencies), preserving the
mathematical structure so similar rays produce similar vectors.  The
displacement codec records (ray_vector → color_vector) as I-frames
and P-frames.

For a new ray: encode geometrically → find nearest I-frame → apply
stored displacement + interpolated delta via exp_map → decode to
RGB.  SLERP between nearby displacements produces colors for rays
that the bootstrap never computed.  In 768d, a single matrix-vector
multiply implicitly encodes all panel intersection tests because
the scene geometry is bundled into the ray encoding.

### Visual Generation Through Experience

The visual generator (`visual_generator.py`) gives agents the
ability to create images without predefined asset libraries.  The
SplatFitter decomposes ingested media into 2D Gaussian splat
representations, learning what things "look like."  The
VisualGenerator produces output from concept embeddings using the
learned splat-to-concept mapping plus a perceptual critic.  The
MemeGenerator produces still images in standard meme/diagram formats.
The DreamingVisualPractice module runs idle-time splat fitting
practice, tracking concept coverage and developing visual skills
progressively.  Visual capability emerges organically through media
consumption, the same way every other leOS capability emerges
through experience.

### Chart Pattern Matching

The chart snapshot tool (`chart_snapshot.py`) generates standardized
candlestick chart images from OHLCV data and automatically embeds
them through the multi-model pipeline.  The key insight: when
nomic-vision and ImageBind see the same chart differently (high
cross-space divergence), the chart contains patterns that traditional
analysis doesn't have names for.  The `search_similar` action finds
historically similar charts by visual embedding similarity and
returns what happened to the price afterward — catching unnamed
patterns that moving averages and RSI would never detect.

### Warm Start and Integration Exercise

The warm start protocol (`warm_start.py`) seeds a fresh system with
curated knowledge and runs 200+ synthetic queries to bootstrap the
displacement log, reflex arc, and nutrient field.  After warm start,
the system has initial experience to work from instead of starting
completely cold.

The integration exercise (`integration_exercise.py`) is a
deliberate training regimen: Round 1 establishes baseline
performance on simple tasks, Round 2 forces failures and edge cases
(deliberately vague prompts, requests for things that don't exist),
Round 3 repeats Round 1 to measure whether the system learned.
After all rounds, the dreaming engine consolidates.  The learning
evaluator then checks whether reflex hit rates improved, skeletons
were saved, and response times decreased.

### Claude API Integration

leOS can use Anthropic Claude models alongside local Ollama models.
The Claude API client (`claude_api.py`) implements the full Messages
API with tool calling — Claude agents can use every tool and skill
that Ollama agents can.  The API key is stored encrypted via the
secrets store (never in config.json).  The system routes
automatically to Claude when a Claude model is selected in any of
the three model slots (working, thinking, vision).

### Encrypted Secrets Store

Tool credentials (API keys, passwords, tokens) are stored encrypted
at rest using Fernet symmetric encryption with a machine-derived key
(hostname + MAC address + random salt).  Secrets are NEVER exposed
to agents in conversation context — they're injected into tool
configuration at execution time.  Each secret can have global and
per-project overrides.


## VSA Computation Primitives

These modules implement the actual Turing-complete Vector Symbolic
Architecture operations — the mathematical foundation that makes
"computing in embedding space" real, not metaphorical.

### Residue Arithmetic: Integer Math via Vectors

The residue arithmetic module (`residue_arithmetic.py`) lets leOS do
actual integer math using vector operations.  No if-statements, no
ALU — just embedding-space computation.

The trick is the Chinese Remainder Theorem.  Pick several small
coprime moduli (e.g., [7, 11, 13, 17, 19, 23] — product = 3.2
million).  For each modulus m, create m random "digit vectors" (one
per residue class).  To encode an integer N: compute N mod each
modulus, look up the corresponding digit vector, and BIND them all
together.  The resulting single 768d vector uniquely represents N.

Addition becomes binding.  Subtraction becomes binding with the
inverse.  Comparison becomes cosine similarity.  The system does
arithmetic on integers up to 3.2 million using only vector
operations that the embedding hardware already supports.

### Resonator Networks: Vector Factorization

When you BIND several vectors together, the result is a single
opaque vector.  The resonator network (`resonator_network.py`) is
how you take it apart again — it decomposes a bound vector into its
constituent factors.

Given a composite vector s = x₁ ⊗ x₂ ⊗ ... ⊗ xF and a set of
codebooks (candidate factors), each factor estimate iteratively
updates until convergence in 5-50 iterations.  Capacity scales
quadratically with dimension: at 1024d, approximately 160,000 items
per resonator.  This is essential for parsing, pattern matching,
and structured retrieval from holographic memory.

### Superposed Computation: Parallel Hypothesis Evaluation

The superposed compute module (`superposed_compute.py`) evaluates
multiple hypotheses simultaneously using BUNDLE (superposition).
Multiple alternative bone chain results are encoded in a single
vector.  The system evaluates all of them in parallel, then uses
RESONATE or COMPARE to determine which path won.

This is not parallel processing (many processors, one state each)
— it's superposed processing (one processor, many states
simultaneously).  The continuous thought vectors naturally encode
multiple alternatives, and the evaluation happens through vector
operations rather than sequential comparison.

### Program Algebra: Self-Modifying Programs

The program algebra module (`program_algebra.py`) collapses the
distinction between code and data.  A compiled bone chain can be
embedded as a single vector.  Once it's a vector:

- BLEND two programs → hybrid capability (SLERP interpolation)
- RESONATE to decompose a program into component operations
- QUERY to find programs similar to a goal
- Programs modify themselves by blending with other programs

The program `sort` and the concept `ordering` and the visual pattern
of `ascending bars` all exist in the same space and interact through
the same operations.

### Feynman Path Integrals for Reflex Selection

When multiple reflex arcs could fire for a given task, the path
integral module (`path_integral.py`) selects among them using a
physics-inspired action functional borrowed from quantum mechanics:

P(arc) = (1/Z) × exp(-S[arc] / T)

where S[arc] sums over steps: 0.5 × ||displacement||² - V(position),
T is a temperature controlling exploration vs. exploitation, and
V(position) is the nutrient field value at that point.  Arcs that
pass through high-nutrient regions (historically successful areas)
have lower action and higher probability.  Temperature controls
whether the system exploits known-good paths or explores alternatives.


## Topology and Structure Analysis

### Cosmic Web Classification

The cosmic web module (`cosmic_web.py`) applies astronomical large-
scale structure classification to the embedding space.  Just as
astrophysicists classify the universe into galaxy clusters (nodes),
connecting filaments, sheet-like walls, and empty voids, leOS
classifies its embedding space into:

- **Nodes** — high-competence app regions (dense clusters)
- **Filaments** — capability chains connecting regions
- **Walls** — SDF boundaries between semantic domains
- **Voids** — capability gaps (where nothing has been learned)

Uses k-nearest-neighbor density estimation with eigenvalue analysis
of the local covariance matrix to classify structure type.  This
tells you the shape of what the system knows.

### Persistent Homology Across MRL Scales

The persistent homology module (`persistent_homology.py`) tracks
which topological features — clusters, loops, voids — persist
across Matryoshka Representation Learning truncation scales.  The
same embeddings at 1024d, 512d, 256d, 128d, 64d, 32d reveal
different structure.  Features that persist from 1024d down to 32d
are fundamental.  Features that only exist at high dimensions are
fine structure or noise.

Uses union-find connected components (Betti-0 numbers) at each
scale, tracking which components merge or split as dimensions
decrease.  Persistence = death_scale - birth_scale.  Long-lived
features are the real structure of the knowledge space.

### Fractal Self-Similarity Detection

The fractal detector (`fractal_detector.py`) finds recurring
patterns at different scales in the displacement log.  "Read →
Analyze → Report" at the application level is self-similar to
"Query → Filter → Format" at the bone chain level, which is
self-similar to "Embed → Nearest → Rank" at the kernel instruction
level.

If the same abstract pattern recurs at every scale, an Iterated
Function System (IFS) can describe the entire log with a handful of
transformation rules — fractal compression of experience.


## Agent Specialization

### Agent Lens: Perspective Filtering

The agent lens (`agent_lens.py`) makes each agent see the knowledge
base differently, like different brain regions extracting different
features from the same stimulus.  Three tiers of perspective
filtering: metadata filtering (who created a record), dimensional
attention masks (which embedding dimensions matter for this agent's
expertise), and collective queries (group perspective).  Also
provides the SDF capability fields that FABRIK and raymarching use
for routing.

### Agent Expertise: Learned Specialization

The expertise module (`agent_expertise.py`) tracks what each agent
is good and bad at by accumulating task embeddings into running
centroids.  Every success folds the task embedding into the agent's
"success centroid."  Every failure goes into the "failure centroid."
Over time, the centroids drift toward what the system actually needs
— without anyone coding rules about agent capabilities.

### Agent Fabrication: Dynamic Agent Creation

The fabricator (`agent_fabricator.py`) creates agents dynamically
from a blueprint library.  It uses prompt_focus for system prompt
composition (a fragment library instead of monolithic prompts),
tool_relevance for tool selection, temperature calibration from
displacement statistics, and confidence scoring.  Agents are
assembled for the task at hand, not pre-defined.


## Additional Systems

### Dual-Source Planning Engine

The plan engine (`plan_engine.py`) coordinates two independent
planning approaches: FABRIK (geometric — knows what's possible)
and the LLM (semantic — knows what's smart).  A cross-examination
step compares the two candidate plans and merges them into a final
plan that's both mechanically valid and strategically sound.
FABRIK catches unreachable goals that the LLM would optimistically
plan for.  The LLM catches edge cases that FABRIK's type system
doesn't model.

### Knowledge Graph Traversal

The knowledge graph (`knowledge_graph.py`) walks the links between
KB entries and media records using embeddings to find connections
that nobody explicitly created.  Link types include explicit
references (related articles, media refs), parent-child
relationships, and implicit embedding similarity connections.  This
turns the knowledge base from a flat collection into a navigable
graph.

### Document Digestion Pipeline

The doc digest module (`doc_digest.py`) processes large documents
(books, research papers, code repositories) into a searchable
multi-level index.  Three passes: structural decomposition
(chapters, sections, paragraphs), per-section embedding and
summarization, and cross-reference link generation.  Agents can
query specific sections without loading the entire document into
their context window.

### Reference Library

The reference library (`reference_library.py`) is a curated list of
known-good documentation URLs plus a domain blacklist of sites to
avoid.  Stored as a single JSON file — human-readable and easy to
edit by hand.  References can be tagged by topic; bad domains
(thin content, AI-generated filler, SEO spam) get added to the
blacklist with a reason field.

The reference library helps agents land on official documentation
first instead of wading through SEO spam and AI-generated slop.
The agent (and the user) can add references they discover, and bad
domains they encounter get blacklisted so future research avoids
them.  Combined with the research router's peer-group reliability
counters, this is the system's accumulating defense against the
modern web's signal-to-noise ratio.

### Memetic Detector: The "Right-Click Save" Instinct

The memetic detector (`memetic_detector.py`) scores every piece
of content flowing through the ingestion pipeline for memetic
value — striking images, catchy phrases, absurd juxtapositions.
Scoring uses pure embedding-space signals: uniqueness (distance
from all existing content), cross-modal surprise (text and image
disagree about what's interesting), and information density
(Shannon entropy of the embedding).  High-scoring content is
flagged and stored in a dedicated memetic index for later retrieval.
This gives leOS the same instinct humans have for saving
interesting content.

### Cross-Modal Embedding Arithmetic

The ImageBind operations module (`imagebind_ops.py`) gives agents
the ability to compute with the shared 1024d space, not just search
it.  "Blend the mood of this audio with the scene from this image"
is a vector operation.  "A is to B as C is to ???" works across
modalities — the analogy between a text concept and a visual
concept produces a meaningful result because they share the same
space.  This is genuine cross-modal reasoning, not text-to-image
retrieval.

### Synesthetic Store: The Image IS the Database

The synesthetic store (`synesthetic_store.py`) unifies index and
data into a single image.  Every vector database separates the
search index from the stored payload.  leOS doesn't.  A synesthetic
image IS both: the multi-layer autostereogram gives ImageBind
approximate matching through parallax texture similarity (the
"index"), while the steganographic payload hidden in the LSBs gives
back the exact original vector bit-for-bit (the "data").

This means you can search a collection of images by embedding
similarity, find the best match, and extract the exact original
data from the image pixels.  Approximate search, exact recovery —
in a single file.  With VectorCodec compression tiers (exact/high/
fast/turbo), a 768d float32 vector can be stored in as few as ~500
bytes hidden inside the image.

### Plugin System

The plugin loader (`plugin_loader.py`) lets you extend leOS without
editing core files.  A plugin is a folder under `plugins/` with a
`plugin.json` manifest declaring what it provides: Flask route
blueprints (UI panels, API endpoints), tools (registered via
decorators), skills (SKILL.md instruction folders), decision tree
check functions, test suites, and hook handlers (callbacks fired on
system events like "agent session started" or "plan step completed").

### Multi-User Support

The multi-user module (`multi_user.py`) provides isolated sessions
for multiple simultaneous users (human owner, LLM agents, external
API clients).  Each user gets their own desktop state, their own
displacement log (learned patterns are per-user), and their own
reflex arc.  The owner has god-mode visibility across all sessions.

### Task-Aware Context Calibration

The embedding context module (`embedding_context.py`) makes tool
descriptions adapt to the current task.  A static description like
"search the media library" means very different things for "find
photos of cats" vs. "analyze the audio mood of podcast episodes."
The module calibrates the tool's context presentation based on the
task embedding, so the agent gets descriptions tuned to what it's
actually doing.

### Circuit Breaker and VRAM Management

The circuit breaker (`circuit_breaker.py`) tracks consecutive
failures per agent and transitions through states: closed (normal)
→ open (blocking) → half-open (testing).  When an agent's breaker
opens, the orchestrator skips it and reassigns the task.  This
prevents the "zombie agent" problem.

The VRAM manager (`vram_manager.py`) coordinates GPU resources
between Ollama and ComfyUI on single-GPU machines.  It discovers
all loaded models via Ollama's API and unloads them before ComfyUI
needs VRAM for image generation, then reloads afterward.

### Monte Carlo Plan Estimation

The estimation engine uses Monte Carlo simulation
(`monte_carlo.py`) for probabilistic plan timing.  Each step has
3-point estimates (low/expected/high), sampled from lognormal
distributions.  The dependency graph determines the critical path
per run.  Across 1000+ simulations, the system produces percentile
estimates (P50, P75, P90) and criticality indices showing which
steps most affect the schedule.

### Issue Tracker

The issue tracker (`issue_tracker.py`) provides file-based bug,
tech debt, and enhancement tracking.  Issues are global (not per-
project) and searchable via embedding similarity.  Agents create
issues when they encounter problems, and the dreaming engine can
review open issues during idle maintenance.

### Semantic Reader Mode

The semantic reader (`semantic_reader.py`) extracts content from
web pages using embeddings instead of DOM heuristics.  While
Apple's Reader Mode uses CSS classes and content density rules,
leOS embeds every content block (paragraphs, headings, images)
and finds the densest cluster in embedding space — that's the
article content.  Blocks distant from the cluster centroid are
noise.  Blocks where nomic-text and Qwen3 disagree are ads or CTAs.
The displacement codec learns site patterns so the reflex arc
knows the layout after 3 articles from the same site.


## The Science Behind the System

leOS borrows mathematics and techniques from disciplines that
traditionally don't talk to each other.  These aren't metaphors —
they're direct applications of the same math to a different medium.

### From Character Animation

FABRIK (Forward And Backward Reaching Inverse Kinematics) solves
bone chains through bidirectional iteration.  XPBD (Extended
Position-Based Dynamics) validates constraints with compliance
parameters.  The bone/joint/skeleton vocabulary describes typed
atomic operations wired into chains, validated by a physics-style
constraint solver.

### From Astronomy

Redshift and blueshift classify displacement anomalies.
Neighborhood-based prediction mirrors how astronomers establish
baseline expectations for a region of sky.  The displacement log's
similarity search is nearest-neighbor regression in embedding space
— the same technique used to calibrate photometric redshifts from
galaxy surveys.

### From the Demoscene

Signed Distance Fields (SDFs) define semantic regions with
composable Boolean algebra: union is min(a,b), intersection is
max(a,b), subtraction is max(a,-b).  Raymarching through SDF
capability space adapts step size to local density — dense
capability regions get small careful steps, sparse regions get big
jumps.  This is the same sphere-tracing algorithm used in 4KB and
64KB demos to render complex scenes from mathematical descriptions.
The demoscene philosophy of storing *descriptions of change* rather
than the change itself directly inspired the displacement codec:
store the transformation pattern, reconstruct the output on the fly.
The thought canvas renders 2D Gaussian splats at demoscene-era
resolution (256x224) because the visual output is a byproduct of
computation, n