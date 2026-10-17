# GateKeep402

> **A reputation-gated payment layer and prompt-injection defense for AI agents using the x402 protocol.**

[![Tests](https://img.shields.io/badge/tests-44%20passed-brightgreen.svg)](tests/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

When AI agents browse the web and pay for APIs or paywalled content via HTTP 402 (`openlibx402`), they face three critical vulnerabilities:
1. **Prompt Injection Attacks**: A malicious webpage text can instruct an LLM agent to pay an attacker's wallet.
2. **Bad-Faith Counterparties**: A server can collect micro-payments and return empty responses (`{}`), disguised error pages, or bait-and-switch redirects.
3. **Runaway Autopay**: Without counterparty memory, an agent will repeatedly pay fraudulent domains on every request.

GateKeep402 solves this by wrapping `openlibx402` in an asymmetric reputation loop, a strict protocol-origin boundary (`SourceGuard`), and corroborated external registry validation (`ERC8004Reader`).

---

## Verified Against Real Public Solana Devnet (Track A & v3)

GateKeep402 has been validated end-to-end on the live **public Solana Devnet** with real transaction settlement, as well as against a local Agave Solana validator (`solana-test-validator`) for deterministic offline CI testing:

- **Settlement Network:** Public Solana Devnet (`https://api.devnet.solana.com`)
- **Verified Transaction Signature:** [`4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq`](https://explorer.solana.com/tx/4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq?cluster=devnet)
- **Explorer Links:**
  - [Solana Explorer](https://explorer.solana.com/tx/4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq?cluster=devnet)
  - [SolanaFM](https://solana.fm/tx/4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq?cluster=devnet-solana)
  - [Solscan](https://solscan.io/tx/4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq?cluster=devnet)
- **On-Chain Settlement Artifact:**
  ```text
  [Public Solana Devnet On-Chain Verification]
    Transaction Signature : 4doLCXNZZTuHXvedmSP5yDPpwLykokKiMrBLDLHRyKaBf1r3uWvcUrfpi3P4t5K8ZdxpgzqoNNJz7Y54HZM9vHiq
    Confirmation Status   : Finalized (Ok)
    Confirmed Block Slot  : 492,438,994
    Fee                   : 5000 lamports (0.000005 SOL)
    Amount Transferred    : 0.01 SOL (10,000,000 lamports)
    Program Logs          : Program 11111111111111111111111111111111 invoke [1] -> success
  ```
- **Testing Architecture:**
  - **Automated CI/Local Suite:** Uses `LocalSolanaValidator` (`solana-test-validator`), exercising 100% authentic Solana SVM runtime logic (blockhash queries, Ed25519 signatures, raw transaction wire broadcasts, and rent-exemption checks) with zero external network dependencies.
  - **Public Devnet Test:** Run `pytest tests/test_public_devnet_integration.py -v -s -m public_devnet` with your own funded keypair in `devnet-test-wallet.json` to execute and broadcast fresh transactions directly to the public Solana Devnet.

---

## Architecture & Closed-Loop Pipeline

```
  Incoming Request (e.g. GET https://api.vendor.com/v1/data)
                         │
                         ▼
             [ Initial HTTP Request ]
                         │
        ┌────────────────┴────────────────┐
   HTTP 200 (Free)                  HTTP 402 (Payment Required)
        │                                 │
        ▼                                 ▼
  Return Data                     [ 1. SourceGuard ]
                                  • Verifies HTTP 402 status
                                  • Extracts 'X-Payment-Request' header
                                  • Prohibits direct object instantiation
                                  • Verifies URI host and origin match
                                          │
                                  VerifiedPaymentRequest
                                          │
                                          ▼
                                   [ 2. TrustGate ]
                                  • Checks local SQLite TrustLedger
                                  • Reads optional ERC-8004 external signals
                                  • score >= 0.60  ──► ALLOW (Auto-pay)
                                  • score < 0.20   ──► DENY  (Hard Block)
                                  • intermediate   ──► ASK   (Human Approval)
                                          │ (If ALLOW or Approved ASK)
                                          ▼
                             [ 3. openlibx402 Payment ]
                                  • Signs & broadcasts payment tx
                                  • Dispatches paid retry request
                                          │
                                          ▼
                                [ 4. DeliveryCheck ]
                                  • HTTP 200 error disguise detection
                                  • Non-empty & minimum length check
                                  • Bait-and-switch redirect validation
                                  • Content-Type consistency parsing
                                          │
                                          ▼
                                 [ 5. TrustLedger ]
                                  • Asymmetric scoring (1 failure > 10 successes)
                                  • Time decay half-life towards neutral 0.50
                                  • Atomic SQLite thread-safe persistence
                                          │
                                          ▼
                                  Delivered Response
```

---

## Comparison: Local Trust vs. ERC-8004 Registry (Track B)

| Property | ERC-8004 Reputation Registry | GateKeep402 Local TrustLedger |
| :--- | :--- | :--- |
| **Primary Scope** | Global cross-organization discovery & identity | Individual agent's verified delivery experience |
| **Storage & Cost** | On-chain (Ethereum / Base / Arbitrum), requires gas | Local SQLite, zero gas, zero network latency |
| **Sybil Resistance** | Vulnerable to rater collusions (arXiv:2606.26028) | Immune: ratings strictly based on local HTTP delivery checks |
| **Autopay Authority** | Corroborating signal only; **NEVER alone grants ALLOW** | **Authoritative:** Direct verified experience determines ALLOW/DENY |
| **Privacy** | Public on-chain rater history | Fully private local client storage |

---

## Quickstart (3 Lines to Get Started)

```python
import asyncio
from openlibx402_client import X402AutoClient
from solders.keypair import Keypair
from gatekeep402 import GateKeep402Client, TrustGate, TrustPolicy, ERC8004Reader

async def main():
    # 1. Initialize underlying openlibx402 client
    base_client = X402AutoClient(wallet_keypair=Keypair())

    # 2. Wrap with GateKeep402 reputation layer (with optional ERC-8004 corroboration)
    reader = ERC8004Reader()
    gate = TrustGate(policy=TrustPolicy(external_signal_reader=reader))
    client = GateKeep402Client(client=base_client, gate=gate)

    # 3. Fetch protected resource with reputation gating & injection defense
    response = await client.get("https://api.marketdata.com/v1/quotes.json")
    print(response.json())

asyncio.run(main())
```

---

## Key Components

| Component | File | Role |
| :--- | :--- | :--- |
| **`SourceGuard`** | [`gatekeep402/source_guard.py`](gatekeep402/source_guard.py) | Cryptographic & protocol origin boundary. Direct constructor raises `TypeError`; instances can only be minted via `VerifiedPaymentRequest.from_http_response()`. |
| **`TrustGate`** | [`gatekeep402/gate.py`](gatekeep402/gate.py) | Pre-payment policy engine. Evaluates domain reputation against configurable thresholds (`ALLOW`, `DENY`, `ASK`) with Track B external signal corroboration. |
| **`DeliveryCheck`** | [`gatekeep402/delivery.py`](gatekeep402/delivery.py) | Post-payment structural verification. Catches disguised errors in HTTP 200s, empty payloads, broken JSON, and bait-and-switch redirects. |
| **`TrustLedger`** | [`gatekeep402/ledger.py`](gatekeep402/ledger.py) | Local persistent SQLite reputation engine with asymmetric Bayesian scoring ($\alpha_{\text{success}}=0.10$, $\alpha_{\text{failure}}=0.40$) and 30-day time decay. |
| **`ERC8004Reader`** | [`gatekeep402/external_signals.py`](gatekeep402/external_signals.py) | Read-only adapter for ERC-8004 Reputation Registry signals. |
| **`GateKeep402Client`** | [`gatekeep402/integrations/openlibx402.py`](gatekeep402/integrations/openlibx402.py) | Async-native client wrapper enforcing manual payment orchestration (Option A) to prevent automatic blind payments. |

---

## Configuration & Tunables

```python
from gatekeep402 import TrustPolicy, DeliveryCheck, TrustLedger, GateKeep402Client, ERC8004Reader

# Custom Policy Thresholds with External Corroboration
policy = TrustPolicy(
    min_score_to_autopay=0.60,          # Score threshold for automated payment
    block_below=0.20,                   # Hard-block threshold (DENY)
    unknown_domain_default="ask",       # Default for unseen domains ("ask", "allow", "deny")
    min_local_history_for_autopay=1,    # Minimum local verified deliveries required for autopay
    external_signal_reader=ERC8004Reader(), # Optional read-only external signal corroborator
)

# Custom Delivery Validation
delivery_check = DeliveryCheck(
    min_content_length=20,          # Heuristic default threshold to catch empty stubs
    strict_resource_match=True,     # Rejects arbitrary redirect path divergence
)

# Custom Ledger Persistence & Decay
ledger = TrustLedger(
    db_path="gatekeep402.db",
    decay_half_life_days=30.0,      # Half-life for inactive reputation decay
)
```

> **Note on `min_content_length=20`**: This is a tunable heuristic default designed to reject minimal stub responses like `{}` or `{"ok":true}` when a substantive data payload was paid for. For endpoints expected to return small atomic values (e.g. booleans), adjust this parameter per endpoint.

---

## What GateKeep402 is NOT

To maintain strict architectural boundaries, GateKeep402 is explicitly designed with clear non-goals:

1. **NOT a replacement for `doorno402` or equivalent client-side x402 security middleware:**
   - **doorno402** serves as prior art in x402 payment security, establishing fundamental defenses against payment prompt injection, fake delivery verification, and redirect hijacking. GateKeep402 builds upon these security foundations by introducing a persistent, time-decaying SQLite reputation engine (`TrustLedger`), a calibrated 3-state policy engine (`TrustGate`), and external signal corroboration (`ERC8004Reader`).
2. **NOT a replacement for wallet budget caps (e.g. `mnemopay` or `AgentGuard`):**
   - Tools like **mnemopay** provide dynamic wallet key management, spending velocity caps, and per-transaction budget limits. GateKeep402 does not manage wallet private keys or set spend budgets. GateKeep402 evaluates **counterparty risk** (has this site historically delivered good data?) and **prompt injection immunity** (did this payment instruction originate from a genuine HTTP 402 header?). They are complementary layers.
3. **NOT an on-chain feedback writer or global authority:**
   - GateKeep402 v2 reads ERC-8004 reputation signals for cross-domain context, but **never writes feedback on-chain** (avoiding gas costs, liability, and second-chain key management). Local delivery history is 100% authoritative for automated payments.
4. **NOT a content-quality judge or semantic evaluator:**
   - `DeliveryCheck` evaluates structural, syntactic, and transport invariants (status code, headers, JSON validness, length, redirect correspondence). It does not judge whether financial analysis is profitable or whether an article is well-written.
5. **NOT a new payment protocol or crypto library:**
   - GateKeep402 does not implement transaction signing, key generation, or blockchain RPCs. All payment mechanics are delegated strictly to `openlibx402`.

---

## Running the Demo & Tests

### Run Full Test Suite (44 Unit & Integration Tests)
```bash
pytest tests/ -v
```

### Run Real On-Chain Validator Integration Test
```bash
pytest tests/test_devnet_integration.py -v -s
```

### Run End-to-End Demonstration Script
```bash
python examples/demo.py
```

---

## Future Work (v3 Targets)

1. **Persistent Public Devnet Verification:** Live testing against public Solana Devnet RPC using a pre-funded static test keypair (bypassing public faucet rate limits).
2. **Zero-Knowledge Reputation Proofs:** Cryptographic ZK proofs for privately sharing verified delivery outcomes across independent agent fleets without leaking transaction histories.
3. **Dynamic Per-Domain Spend Limits:** Automatic budget ceiling scaling based on historical local delivery volume.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
