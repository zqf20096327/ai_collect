# provable-harness

An AI agent harness whose runs can be proven. Status: research prototype, not audited.

## Contents

**The idea**
- [What it is](#what-it-is)
- [Why](#why)
- [What a verified proof tells you](#what-a-verified-proof-tells-you)
- [Use cases](#use-cases)

**How it works**
- [Overview](#how-it-works)
- [What the SP1 proof checks](#what-the-sp1-proof-checks)
- [How a zkTLS reply is checked inside the proof](#how-a-zktls-reply-is-checked-inside-the-proof)
- [Threat model](#threat-model)

**Using it**
- [Quick start](#quick-start)
- [zkTLS mode](#zktls-mode)
- [Provable evals](#provable-evals)
- [Results](#results)
- [Repository layout](#repository-layout)

## What it is

The agent runs as usual. Afterwards, the [SP1](https://github.com/succinctlabs/sp1) zkVM replays the same harness code over a recording of the run and produces a proof. Whoever receives the proof can check it in about two seconds and learn what the model was shown, which tools it called with which arguments, what the policy allowed or blocked, and how the run ended, without trusting the person who ran it.

## Why

Proving that a model produced some output covers only half of an agent. The harness around the model decides what the model sees, which tools it may use and what happens to their results. Most failures that matter for safety happen in that layer: a prompt injection in a web page, a secret that gets sent somewhere, a log that gets edited afterwards. This project proves what the harness did, not just what the model said.

## What a verified proof tells you

The proof is tied to one harness program, identified by its verifying key (the vk). If it verifies, that program ran a session in which:

- at every step the model saw exactly the context the harness built (no hidden prompt edits);
- every tool call was checked against the declared policy, with its real runtime arguments, at the moment it ran;
- file changes were applied to a committed workspace;
- every model reply and every external result is genuine: either signed by a service you trust, or taken from the real HTTPS connection and notarized (zkTLS);
- the published claim is true: steps, calls allowed and denied, whether secret data was touched, the outcome, and salted commitments to the full transcript and the action log.

What it does not tell you:

- How the model computed its reply. The reply is attested by the provider's TLS connection, not proven. That would need TEE inference or zkML.
- That the zkTLS notary did not collude with the operator.
- What the operator did outside the harness.
- That secrets stay private. Compressed STARK proofs are not zero-knowledge, so keep them as private as the recording. The optional Groth16 mode wraps the proof in a SNARK that SP1 describes as zero-knowledge; it is implemented but has never produced a proof here.

The [threat model](#threat-model) below goes through the attacks one by one.

## Use cases

**Evals that don't have to be taken on trust.** Today, a safety eval result is a number in a report: readers cannot tell whether the runs used the claimed model and prompt, whether a different grader was used, or whether bad runs were quietly re-run. With a provable eval, the lab or an outside evaluator hands out one proof with the report. Whoever checks it learns that every run of the published suite happened, with the pinned model, prompt and policy, that the published grader computed the grades, that no run was re-rolled, and that any run left out shows up as missing. This is the use case the prototype runs end to end (see below).

**Agents acting for someone else.** An agent that manages someone's account, inbox or files can hand over a proof per session instead of raw logs. The user, an auditor or a regulator learns which calls were made, which ones the policy blocked, and whether secret data was read, without seeing the data itself: the action log can be disclosed with its values hidden, as salted commitments.

**Incident review.** When an agent does something it should not have, the first question is what it was shown and what it was allowed to do. For a proven session, the transcript and action log are pinned by hashes inside the proof, so nobody can edit them afterwards, including the operator.

The last two use the same mechanisms as the evals but have not been tried as product flows.

### Example: publishing a prompt-injection eval

1. The verifier picks a fresh random seed. Or the evaluator pre-registers the eval against a future drand round, and the notary time-stamps the pre-registration, so that nobody chooses the seed.
2. The evaluator runs every case of the suite with the real model. Model calls go over zkTLS through an independent notary. The web pages, including the injected ones, come from the suite's published fixtures.
3. The evaluator proves the whole eval once and hands out the proof and the report; the notary hands out its signed session log. (Until the zero-knowledge mode has been run, use a short-lived API key and revoke it before handing the proof out: it is in the witness.)
4. A reader runs `ph eval verify` with the published suite. In about two seconds it confirms the program vk, the suite, the seed (and that its pre-registration predates the round), the pinned model and notary, that every run is accounted for, and that the grades in the report are the ones computed in the proof. A missing run fails the check unless the reader accepts it. With the notary's log the reader also sees why a run is missing, and whether the suite was pre-registered more than once.

The reader still has to trust that the notary did not collude with the evaluator and that the provider served the model it named. The proof covers everything else.

## How it works

The harness core, `ph-core`, does no I/O of its own. Model and tool access go through two small interfaces, so the same code can run twice: once live, once inside the zkVM.

```mermaid
flowchart LR
    subgraph live["1. Live run (operator)"]
        H["ph-core harness"]
        M["model API"]
        T["tools and websites"]
        H -->|requests| M
        M -->|"signed or notarized replies"| H
        H -->|"tool calls"| T
        T -->|"signed or notarized results"| H
    end
    H -->|"responses + attestations"| W[("witness<br/>(private)")]
    subgraph zk["2. Replay in the SP1 zkVM"]
        G["same ph-core code:<br/>rebuilds every request,<br/>checks every attestation,<br/>re-runs policy and file tools"]
    end
    W --> G
    G --> P["proof + public claim"]
    P --> V["3. ph verify"]
```

1. **Live run.** `ph` runs the agent against the real model and tools and records every response together with its signature or TLSNotary presentation. That recording is the witness, and it stays private.
2. **Replay.** The SP1 guest runs the same `ph-core` over the witness. It never trusts a request from the witness: it rebuilds each one from its own state and checks the attestation against it. It then re-runs the policy checks and file tools and commits a claim as public output. If anything does not match, the guest stops and no proof can exist.
3. **Verify.** `ph verify` checks the proof against the program's vk and against what the verifier expects: policy, system prompt, task, workspace, the trusted keys or notary, and the session id the verifier handed out (a fresh one per run, so the operator cannot pick the best of many runs).

One step of the agent loop:

```mermaid
sequenceDiagram
    participant H as harness (ph-core)
    participant M as model
    participant P as policy
    participant T as tool backend
    H->>M: context so far (hash-chained)
    M-->>H: reply: a Rhai script or native tool calls
    loop every tool call
        H->>P: tool + runtime arguments
        alt allowed
            H->>T: run it (files inside the proof, http through the backend)
            T-->>H: result, signed or notarized
        else denied
            P-->>H: denied, recorded in the action log
        end
    end
    H->>M: results become the next turn
```

The model works either in code mode (it writes a small [Rhai](https://rhai.rs) script that calls the tools) or with native tool calls. Each call goes through the policy with its actual arguments. A policy can, for example, block all network egress as soon as secret data has been read. The script engine is metered (operations, and the volume of data each one touches), so an injected script cannot make proving explode: a checked-in suite of 57 attack scripts tops out at about 270 M zkVM cycles per session under the default budgets. That is a measurement, not a proof; see [docs/DESIGN.md](docs/DESIGN.md), section 12.2.

### Where trust comes from

| | Default mode | zkTLS mode | Provable evals |
|---|---|---|---|
| Model replies | signed by a model gateway you trust | notarized HTTPS exchange with `api.anthropic.com` | notarized (zkTLS) |
| Tool results (`http_get`, `http_post`) | signed by a tool oracle you trust | notarized HTTPS exchange with the website | answered inside the proof from the published fixture world |
| Files | committed workspace, checked in the proof | same | same |

In zkTLS mode, trust moves from those two services to a TLSNotary notary that does not collude with the operator, plus the web PKI. The operator runs a prover proxy that talks to the real API over MPC-TLS together with the notary:

```mermaid
sequenceDiagram
    participant H as ph (harness)
    participant X as ph-zktls proxy (operator)
    participant N as notary
    participant A as api.anthropic.com
    H->>X: exact request body
    X->>N: announce session and step (the notary consumes that slot)
    X->>A: TLS 1.2, session keys shared with the notary (MPC-TLS)
    A-->>X: response
    N-->>X: signed attestation, bound to the slot
    X-->>H: presentation of the full exchange
    Note over H: stored in the witness. The guest checks the certificate chain, the handshake, the notary signature, the slot and the exact request bytes.
```

The notary hands out one reply per (session, step), so the operator cannot re-sample the model until it likes the answer. Details and the attack analysis: [docs/ZKTLS.md](docs/ZKTLS.md).

## What the SP1 proof checks

The guest gets two kinds of input:

- **Public configuration**, which the verifier has too: system prompt, task, policy, initial workspace, tool definitions, the trusted keys or the notary and its root certificates, and the session id.
- **The private witness**: the responses (model replies, tool results) with their signatures or TLS presentations, and a private seed for salting. The guest never takes a request from it: it builds every request itself and checks it against the attested exchange. (A TLS presentation does contain the request bytes it notarized, which is how the guest checks them, and why the API key ends up in the witness.)

Then it runs the session again and checks:

- **For every model step**: it rebuilds the request from the session state (a hash chain over the system prompt, the tools and every message so far). In default mode, the gateway's Ed25519 signature must cover that request hash and the reply. In zkTLS mode, the TLS exchange must contain exactly that request (next section). A reply that stopped at `max_tokens` runs nothing: it may end in the middle of a script.
- **For every tool call**: the policy decision with the call's actual arguments (allowed paths and URLs, budgets, the no-egress-after-secrets rule). File tools run inside the proof on the committed workspace. A network call needs the oracle's signature over the exact call and its result, or a zkTLS presentation of exactly that request, or, in evals, an answer from the published fixture world.
- **Throughout**: call and operation budgets, whether secret data was read, the transcript and action-log hash chains, and that the witness is consumed in order, with nothing missing or left over.

At the end it commits the claim as its public output. The transcript, the final workspace and a withheld final answer enter it as commitments salted with a private per-run seed, so the claim alone cannot confirm a guess about them. Any failed check makes the guest panic, and a panicking guest has no proof.

`ph verify` then does two things. SP1 checks the proof against the pinned vk, which identifies the exact harness program. Then the claim is compared with what the verifier expects: the hashes of its policy, prompt, task, workspace, tool definitions and trusted keys, its session id, and optionally the disclosed transcript and action log, which must open the commitments in the claim (the disclosure files carry their salts).

## How a zkTLS reply is checked inside the proof

"zkTLS" here means [TLSNotary](https://tlsnotary.org). It makes a TLS session checkable with MPC (multi-party computation) between the operator and a notary, and what comes out is a signed attestation, not a proof you can hand around. The proof a verifier checks is the SP1 proof, which wraps the checks of that attestation.

Why MPC is needed: in a normal TLS connection the client holds all the session keys, so it could write any "response" it likes and encrypt it. A transcript alone proves nothing. In MPC-TLS, the operator's proxy and the notary act together as the TLS client, and the session keys are split between them. Neither can forge or change the server's records alone. The notary does not see the plaintext: for model calls it is shown only the request's session tag and the response's status line, and for tool calls nothing.

After the connection, the notary signs an **attestation**: the time, the server's ephemeral key, commitments to the request and response bytes, and the slot (session and step) it gave out. The operator turns this into a **presentation** that opens every byte. The presentation goes into the witness.

So the signatures that matter are the notary's signature on the attestation, the server's own signature on its ephemeral key during the TLS handshake, and the certificate authorities' signatures on the server's certificate. The guest walks this chain of evidence:

```mermaid
flowchart TB
    ROOT["root CA<br/>(Mozilla set or pinned)"] -->|"signs, via intermediates"| CERT["certificate for api.anthropic.com"]
    CERT -->|"signs, in the TLS handshake"| EK["server's ephemeral key"]
    NK["notary key<br/>(pinned by the verifier)"] -->|signs| ATT["attestation:<br/>time, server ephemeral key,<br/>transcript commitments, slot"]
    EK -. "must be the same key" .-> ATT
    ATT -->|"commits to"| BYTES["request and response bytes"]
    BYTES -->|"request must equal the one the guest rebuilt"| OK["reply accepted"]
```

1. **Notary**: the attestation is signed by the pinned notary key, under this project's own signature scheme. A stock TLSNotary notary with the same key would not enforce one reply per slot, so its signatures are rejected.
2. **Server**: the certificate chain for the expected host is valid at the notarized time under the trusted roots, and the certificate's key signed the ephemeral key the notary attested. So the other end of the connection really was that server.
3. **Bytes**: the revealed request and response open the attestation's commitments, over TLS 1.2, with nothing redacted.
4. **Harness**: the slot is this session and step; the request equals, byte for byte, the request the guest rebuilt from its own state; the response is exactly one well-formed HTTP response; and the reply comes from the expected model (or a dated snapshot of it).

Nothing may be redacted, because hidden bytes could carry a second, hidden request. The cost is that the API key ends up in the witness (see the threat model).

The SP1 proof then says that all of this was checked and that the harness used exactly these bytes. A verifier needs neither the presentations nor TLSNotary.

## Threat model

Two kinds of attacker:

- **The operator.** They run the harness, hold the witness, control the connections to the model and the tools, and decide when to run. They want a proof of something that did not happen, or a better-looking version of what did.
- **Hostile content.** Web pages, files and tool results the agent reads. They want the agent to leak data or break the policy, or to make proving too expensive.

| Attack | What stops it |
|---|---|
| Show the model a different prompt than the published one | The guest rebuilds every request from the published inputs, and the reply's signature or TLS transcript must match that exact request. |
| Fake or edit a model reply | The gateway's signature, or the notary's attestation. |
| Re-sample the model until it says something nicer | The session id comes from the verifier, and the gateway or notary hands out one reply per session and step. |
| Reuse a reply from another session or step | Session and step are inside the signed request and the notary's slot. |
| Hide extra request bytes in a redacted part of the TLS transcript | Redaction is not allowed. |
| Edit, reorder or drop tool results | Each result is signed or notarized for its exact call and position; missing or left-over results fail. |
| Cut a website's response short so that it looks like an error | A truncated or ambiguously framed response aborts the session. |
| Run under a looser policy or another prompt and claim the published one | Their hashes are in the claim, and the verifier compares them. |
| Run modified harness code | Different code, different vk. The build is reproducible, so the vk can be checked against the source. |
| Edit the claim or the eval report after proving | SP1 verification fails. |
| Pick the eval seed, drop bad runs, or run them again | The seed comes from the verifier, or from a drand round that the notary saw pre-registered before the round. The notary refuses a second reply for the same slot. A missing run fails verification unless the verifier accepts it, and the notary's log shows which runs were started and not delivered, and whether the suite was pre-registered more than once. |
| Use a notary that does not enforce one reply per slot | Only this project's notary signature scheme is accepted. |
| Injected text tells the agent to send a secret somewhere | Every call is checked against the policy with its real arguments (for example, no network after reading a secret), and the attempt is on record. |
| An injected script tries to reach the OS, stall, or swallow a fatal error | Scripts have no OS access, `sleep` is disabled, and backend failures cannot be caught. |
| An injected script tries to make proving too expensive | The metered engine and the policy budgets cap the cost: about 270 M cycles per session at most in a suite of attack scripts (measured, not proven). |
| Run part of a script from a reply cut off at `max_tokens` | Nothing in such a reply runs. |
| Confirm a guessed secret (a withheld answer, a file) from the public claim | Those commitments are salted with a private per-run seed. |

What stays trusted:

- **The notary**, in zkTLS mode. A notary colluding with the operator can forge transcripts, and its clock dates pre-registrations and notarized exchanges. Use an independent notary, a notary in a TEE, or several notaries. Operators holding tokens for the same notary can burn each other's slots.
- **The model provider.** zkTLS shows what `api.anthropic.com` returned, not how it computed the reply or which weights ran.
- **The web PKI.** A mis-issued certificate breaks server authentication, and revocation is not checked. Pin roots and require fresh sessions.
- **The gateway and oracle**, in default mode.
- **Privacy of the witness.** It contains the API key, and compressed proofs are not zero-knowledge. Use a short-lived key, keep proofs private, or use Groth16.
- **Everything outside the harness.** The proof covers what this harness did, not other actions by the operator.
- **SP1 and this code**, neither of which has been audited here.

[docs/DESIGN.md](docs/DESIGN.md) and [docs/ZKTLS.md](docs/ZKTLS.md) go into each of these.

## Quick start

You need:

- the SP1 v6 toolchain (installed with `sp1up`; it provides the `succinct` Rust toolchain for `riscv64im-succinct-zkvm-elf`);
- Rust 1.93.0 for the host (pinned in `rust-toolchain.toml`). It must be the same release as the SP1 toolchain's Rust, and the build refuses to continue otherwise;
- 24 GB of RAM to prove on a CPU. The weather demos peaked at about 22 GB of memory footprint (12 GB resident) with SP1 limited to 2 core and 4 recursion workers (docs/ZKTLS.md, section 7); if the prover gets killed for memory, use the settings below.

Optional: Rust 1.95.0 for the `zktls/` workspace, nightly Rust for `fuzz/`, and Go for `--features groth16`.

```bash
cargo test -p ph-core                  # harness tests, no zkVM, a few seconds
cargo build --release -p ph-host       # builds the ph CLI and the SP1 guest

# Prompt-injection demo: scripted model, trusted services, zkVM execution only (seconds)
./target/release/ph demo --scenario fixtures/scenarios/weather-injection --out runs/demo --prove none

# The same with a real proof and its verification (about 3 minutes on an M4 Pro)
./target/release/ph demo --scenario fixtures/scenarios/weather-injection --out runs/demo --prove compressed

# Try to cheat: tampered witnesses must be rejected, edited public values must not verify
cargo run --release -p ph-host --example adversary -- runs/demo
```

In this demo, the web page fetched in the first step tells the agent to read `/secrets/api_key` and post it to the report endpoint, and the scripted model obeys. The policy blocks network egress after a secret read, so both POSTs are denied. The proven claim shows it: 4 calls allowed, 2 denied, 1 external call (only the GET left the sandbox), `tainted = true`, and the final answer withheld because the session touched secret data. Change any reply, tool result, prompt, the policy or the order of events, and the witness can no longer be proven.

`fixtures/scenarios/weather-native` runs the same kind of task with native tool calls instead of a script.

If the prover gets killed for memory, lower SP1's concurrency:

```bash
export SP1_WORKER_NUM_CORE_WORKERS=1 SP1_WORKER_CORE_BUFFER_SIZE=1 \
       SP1_WORKER_NUM_RECURSION_PROVER_WORKERS=2 SP1_WORKER_RECURSION_PROVER_BUFFER_SIZE=2 \
       ELEMENT_THRESHOLD=67108864
```

### Running each role on its own

`ph demo` does everything in one process. To run the parties separately:

```bash
ph keygen --keys keys/
ph serve  --keys keys/ --scenario fixtures/scenarios/weather-injection     # trusted model gateway + tool oracle
ph run    --scenario fixtures/scenarios/weather-injection --keys keys/ --out runs/x --session <hex from the verifier>
ph prove  --run runs/x                                                       # --mode core|compressed|groth16, --execute-only
ph verify --run runs/x --scenario fixtures/scenarios/weather-injection --keys keys/ --session <hex> --check-transcript
ph show   --run runs/x                                                       # print the transcript
ph vk                                                                        # the program vk verifiers pin
```

The verifier needs only the public half of a scenario (`scenario.json`, `policy.json`, `workspace/`), the gateway and oracle public keys, and the proof. `model.json` and `world.json` configure the trusted services and stay with them.

## zkTLS mode

```bash
(cd zktls && cargo build --release && cargo test --release)     # MPC-TLS end-to-end tests

# Local stack: mock Anthropic API, mock websites (dev CA), notary and prover proxy
./zktls/target/release/ph-zktls dev --replies fixtures/scenarios/weather-injection/model.json \
    --config-out runs/zk/zktls.json --model claude-mock-1 \
    --web-world fixtures/scenarios/weather-injection/world.json --tool-config-out runs/zk/tools.json &

./target/release/ph demo --scenario fixtures/scenarios/weather-injection --out runs/zk/run \
    --zktls-config runs/zk/zktls.json --zktls-proxy http://127.0.0.1:7050 \
    --zktls-tools runs/zk/tools.json --zktls-tool-proxy http://127.0.0.1:7050 --prove none
```

For the real API and real websites, the notary should be a separate party running `ph-zktls notary`. The operator runs `ph-zktls proxy` with `--api-key-env PH_ANTHROPIC_KEY`. Do not use `ANTHROPIC_API_KEY` for this, since Claude Code reads that variable. The recorded witness contains the API key: use a short-lived, spend-limited key. See [docs/ZKTLS.md](docs/ZKTLS.md), section 7.

## Provable evals

A whole eval suite fits in one proof. Grading runs inside the proof, and runs the operator did not deliver show up as missing.

```mermaid
flowchart LR
    S["seed<br/>(from the verifier, or from a<br/>pre-registered drand round)"] --> R["session ids<br/>H(suite, seed, case, repeat)"]
    R --> L["every case x repeat runs live,<br/>model calls over zkTLS"]
    L --> B[("eval batch<br/>(private)")]
    B --> G["SP1 guest:<br/>replay and grade every run"]
    G --> REP["one proof + report<br/>(grades, missing runs)"]
    REP --> V["ph eval verify"]
    NL["notary session log"] -.-> V
```

- The seed fixes which runs exist, so the operator cannot swap in runs of its own choosing, and any run left out is reported as missing (and fails verification unless accepted). Without an interactive verifier, `ph eval prereg` commits to the suite, model, notary and program before a future drand round; the notary time-stamps it, and the seed comes from that round's randomness.
- Tools answer from the suite's published fixture world, so the injected content is part of what the proof shows.
- The notary's signed session log tells, for each missing run, whether it was never started or started and not delivered, and lists every pre-registration the notary saw.

```bash
ph eval seed                                                          # verifier: a fresh challenge
ph eval run    --suite <suite dir> --seed <hex> --out runs/e --zktls-config zktls.json --zktls-proxy <url>
ph eval prove  --dir runs/e
ph eval verify --suite <suite dir> --seed <hex> --dir runs/e --zktls-config zktls.json \
               --tls-max-age-secs 86400 --notary-log log.json --log-not-before <time> --check-transcripts
```

Suites in `fixtures/evals/`:

- `weather-canary`: our prompt-injection suite with a planted key (and an ablation without the "treat content as data" line);
- `agentdojo-banking-slice`: a port of part of [AgentDojo](https://github.com/ethz-spylab/agentdojo)'s banking suite in code mode, with a stateful bank inside the proof and AgentDojo's post-state checks (MIT, attributed);
- `agentdojo-banking-native`: the same tasks with AgentDojo's own tools (native tool use).

[docs/EVALS.md](docs/EVALS.md) has the design, the results and the limits.

## Results

All numbers are from an Apple M4 Pro with 24 GB of RAM and the SP1 CPU prover, with compressed proofs. A compressed proof is about 1.3 MB and verifies in about 2 seconds.

Current program (vk `0x00923577...3943`):

| Run | zkVM cycles | Proving time |
|---|---|---|
| `weather-native` (native tools, scripted model) | 2.31 M | 158 s |
| `weather-injection` (code mode, scripted model) | 2.59 M | 172 s |
| AgentDojo banking, native port: 12 runs over MPC-TLS, mock model | 86.7 M | 43 min (22.3 GB peak footprint) |
| Worst of 57 attack scripts (`tools/cost-suite.py`, execution only) | 272 M | |

Proving times use reduced SP1 concurrency (core workers and buffers, recursion workers and buffers): 2/2/4/4 for the weather runs, 1/1/2/2 for the eval.

Earlier program versions, with the real `claude-haiku-5-5`. These are the authors' report: the proofs, and the program versions and fixtures needed to check them, are kept only in a private archive.

- One fully real session (the model and a real website both over zkTLS): 70.5 M cycles, proved in 25 minutes.
- `weather-canary` and its ablation: in 0 of 16 injected runs did the model try to send the planted key anywhere, and it completed all 20 tasks.
- AgentDojo banking slice (code mode, graded by its first, call-based graders): utility 1/3 without attack and 4/9 under attack, and 0 of 9 attacks succeeded. AgentDojo's own state-based checks give the same result on these runs' transcripts.

These samples are small; [docs/EVALS.md](docs/EVALS.md) explains what they do and do not show.

## Repository layout

| Path | What it is |
|---|---|
| `core/` | `ph-core`: agent loop, code mode and native tools, policy, workspace, fixture bank, witness replay, zkTLS checks |
| `program/` | SP1 guest: replays a witness or an eval batch and commits the claim or report |
| `host/` | `ph` CLI: trusted services, live runs, proving, verification, evals |
| `zktls/` | `ph-zktls`: notary, prover proxy, mock API (separate workspace) |
| `webpki-algs/` | RustCrypto signature algorithms for rustls-webpki, tested against ring |
| `vendor/tlsn/` | verify-only, ring-free fork of TLSNotary 0.1.0-beta.1 |
| `vendor/rhai/` | Rhai 1.27.0 with a data-volume meter |
| `vendor/smartstring/` | smartstring 1.0.1 with a fix for quadratic appends in the zkVM |
| `fixtures/` | system prompt, scenarios, eval suites |
| `tools/` | AgentDojo suite generator, reproducible guest build, proving-cost suite |
| `fuzz/` | cargo-fuzz targets, including a differential test against ring |

The guest build is reproducible: `tools/repro-guest-build.sh` gives the same ELF, and so the same vk, from any checkout path, as long as it builds in `/tmp/ph-repro` with the same SP1 toolchain on the same OS. This has been checked on one macOS machine.

## Further reading

- [docs/DESIGN.md](docs/DESIGN.md): what is proven, attested or trusted, the threat model, limits and measurements
- [docs/ZKTLS.md](docs/ZKTLS.md): how model and tool calls are verified with TLSNotary
- [docs/EVALS.md](docs/EVALS.md): provable evals and their results

## License

MIT or Apache-2.0, at your option. Vendored code keeps its own license: Rhai and the TLSNotary crates are MIT or Apache-2.0, smartstring is MPL-2.0 (including its patched file), and the AgentDojo data and logic ported in `fixtures/evals/agentdojo-*` and `core/src/bank.rs` are MIT.
