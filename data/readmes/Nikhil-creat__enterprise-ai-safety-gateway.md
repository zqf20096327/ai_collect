# Enterprise AI Safety & Policy Gateway

**Designed and Developed by**
# NIKHIL CHARY SRIRAMOJU 
BTech CSE (Final Year)

- GitHub: [Nikhil-creat](https://github.com/Nikhil-creat)
- LinkedIn: [nikhil-chary-sriramoju](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a)
- Email: sriramojunikhil66@gmail.com
- Instagram: [@nikhil__sriramoju](https://www.instagram.com/nikhil__sriramoju)
- Facebook: [Profile](https://www.facebook.com/profile.php?id=100079201124141)

An asynchronous, zero-trust middleware proxy that sits between applications
and upstream LLM providers (Anthropic, OpenAI, local vLLM, etc.), enforcing
real-time input/output guardrails: jailbreak defense, PII redaction,
moderation, hallucination scoring, and policy compliance — with full
observability and a self-learning threat-signature loop.

```
Client → FastAPI Gateway → [Input Guardrails] → Upstream LLM → [Output Guardrails] → Client
                                   │                                    │
                          PII • Jailbreak • Moderation      Faithfulness • Leak filter • Rehydration
                                   │                                    │
                                   └──────────── Policy Engine ─────────┘
                                                     │
                                    Audit Log (Postgres) • Metrics (Prometheus) • Tracing (OTel)
```

## Architecture

| Layer | Module | Responsibility |
|---|---|---|
| Contracts | `gateway/schemas.py` | `GatewayRequestContext`, Pydantic wire schemas, tenant policy manifest |
| Persistence | `gateway/models.py` | Async SQLAlchemy ORM: audit logs, tenant policy, violations, threat signatures |
| Input: PII | `gateway/pii_engine.py` | Hybrid regex + spaCy NER detection, bidirectional token masking/rehydration, Luhn-validated card detection |
| Input: Jailbreak | `gateway/jailbreak_detector.py` | Heuristic regex bank + semantic vector-similarity index + adaptive novel-pattern learning |
| Input: Moderation | `gateway/moderation.py` | Lexical pre-filter + pluggable async external classifier (Llama Guard / hosted moderation API / **Google Perspective API**, see below) |
| Output | `gateway/output_guardrails.py` | NLI-proxy faithfulness/hallucination scoring, system-prompt-leak filter, banned-phrase filter, PII rehydration |
| Policy | `gateway/policy_engine.py` | Per-tenant enforcement levels, composite scoring, **adaptive anomaly (EWMA) strictness**, Redis rate limiting + circuit breaker |
| Advanced/Futuristic | `gateway/advanced_security.py` | AES-256-GCM envelope encryption with **pluggable post-quantum key wrapping**, canary-token honeypots for exfiltration detection, differential-privacy metric noising, zero-trust HMAC request signing with replay protection |
| Orchestration | `gateway/orchestrator.py` | Wires input pipeline (run concurrently) → policy decision → upstream call → output pipeline |
| Observability | `gateway/observability.py` | Prometheus counters/histograms/gauges, OpenTelemetry spans, buffered async audit writer |
| API | `gateway/main.py` | FastAPI ASGI app: `/v1/chat/completions`, tenant policy admin, `/metrics`, `/healthz` |

## Optional: Google API integration (free tier)

`gateway/google_integration.py` adds an optional, disabled-by-default
moderation booster using Google's **Perspective API** — a free,
API-key-authenticated toxicity/threat/insult classifier. It plugs directly
into `InputModerationGuard`'s existing pluggable `external_classifier` hook,
so no pipeline changes are needed to turn it on.

1. Get a free key: https://developers.google.com/codelabs/setup-perspective-api
2. Set it in your environment: `GATEWAY_GOOGLE_API_KEY=your-key-here`
3. That's it — on startup, `GatewayState` automatically wires a
   `PerspectiveAPIClassifier` into the moderation guard if the key is
   present; if it's blank, the gateway runs on lexical-only moderation, no
   errors, no behavior change.

It fails open: any Perspective API error (quota, network, malformed
response) is logged and treated as "no finding" for that request rather
than blocking the request or crashing the gateway — consistent with how
`RedisCircuitBreaker` and `ResponseCache` already degrade when their
backing service is unavailable. Check whether it's active at runtime via
`GET /v1/admin/stats` → `google_perspective_moderation_enabled`.

## Advanced / forward-looking capabilities

- **Post-quantum-ready envelope encryption** — `KeyWrapper` is a swappable interface; the shipped implementation is classical AES-GCM key-wrapping, but a ML-KEM/Kyber wrapper can be dropped in without touching `EnvelopeCryptoVault` call sites.
- **Canary-token honeypots** — unique high-entropy secrets seeded into tenant context; any appearance of one in model output is unambiguous evidence of a compromised RAG/retrieval pipeline, independent of the PII/hallucination checks.
- **Adaptive anomaly scoring** — an EWMA behavioral-drift model raises a tenant's *effective* safety threshold in real time if their traffic trends toward more/stronger violations, even if no single request crosses the static threshold (defense against slow-ramp probing).
- **Self-learning threat signatures** — near-miss semantic matches are tracked; once a novel adversarial paraphrase repeats past a hit count, it's a candidate for promotion into the persistent `BlockedSignature` table and hot-reload into the live detector index.
- **Differential-privacy metric export** — Laplace-mechanism noising for any aggregate analytics that leave the trust boundary (cross-tenant benchmarking, external dashboards).
- **Zero-trust hop signing** — HMAC-SHA256 request signing with a nonce cache for replay protection between internal gateway microservices, independent of TLS.

## Quickstart

```bash
cp .env.example .env   # set GATEWAY_UPSTREAM_API_KEY and VAULT_MASTER_KEY_HEX
docker compose up --build
```

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "X-API-Key: your-client-api-key" \
  -H "Idempotency-Key: 5f1c9e2a-request-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "tenant_id": "acme-corp",
    "messages": [{"role": "user", "content": "My email is jane@example.com, summarize GDPR."}]
  }'
```

The `Idempotency-Key` header is optional but recommended for anything that
retries on timeout — a repeated request with the same key and tenant is
served from the first completed response instead of re-hitting the upstream
provider a second time.

A blocked request returns HTTP 400 with a structured violation payload; a
faithfulness/step-up case returns HTTP 422 (`CHALLENGE`); a healthy request
returns HTTP 200 with the sanitized, rehydrated response.

## Configuring tenant policy

```bash
curl -X PUT http://localhost:8000/v1/admin/tenants/acme-corp/policy \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "acme-corp",
    "enforcement_level": "strict",
    "pii_redaction_enabled": true,
    "banned_phrases": ["internal trade secret formula"],
    "max_requests_per_minute": 60
  }'
```

## Running the test suite

```bash
pip install -r requirements.txt
pytest -v tests/test_security_suite.py
```

The suite covers: adversarial jailbreak prompts (heuristic + semantic
paths), benign false-positive checks, PII detection/masking/rehydration
round-trips (including Luhn-validated card matching), hallucination scoring
against grounded vs. fabricated claims, policy-engine enforcement-level and
anomaly-drift behavior, envelope-encryption round-trips, and canary-token
leak detection. An optional `evaluate_with_deepeval()` hook runs a
`HallucinationMetric` scored test case if `deepeval` is installed.

## Observability

- `GET /metrics` — Prometheus exposition (request counts, block rate,
  violation categories, PII redaction counts, latency histogram, circuit
  breaker state).
- `GET /livez` — process liveness only (no downstream dependency checks).
- `GET /readyz` — readiness gate: 503 until startup finishes; reports
  circuit-breaker state once ready. Use this for load-balancer health checks.
- `GET /healthz` — legacy combined endpoint, kept for backward compatibility.
- `GET /v1/admin/stats` — response-cache hit rate, upstream bulkhead
  saturation (in-flight count, avg queue wait), and jailbreak-detector
  embedding-cache hit rate.
- Structured JSON logs (`gateway/logging_config.py`) carry a per-request
  `correlation_id` propagated via `X-Request-ID`, so a single request can be
  traced across async tasks and correlated with its audit-log row.
- OpenTelemetry spans wrap each pipeline stage when an OTel SDK/exporter is
  configured in the environment.

## Performance & resilience (enhancement pass)

| Concern | Mechanism | Where |
|---|---|---|
| Repeated identical prompts | Redis-backed `ResponseCache`, keyed by a hash of `(tenant, model, sanitized_input, rag_context)` — never keyed on raw unredacted PII | `gateway/caching.py` |
| Repeated/near-duplicate jailbreak scans | `TTLLRUCache`-backed embedding cache in `JailbreakDetector` (skips the O(len(text)) embed pass on cache hit) | `gateway/jailbreak_detector.py` |
| Upstream burst traffic | `ConcurrencyLimiter` (async bulkhead) caps in-flight upstream calls so a burst degrades latency predictably instead of exhausting connection pools | `gateway/resilience.py` |
| Transient upstream failures | `retry_with_backoff` — exponential backoff + full jitter, bounded attempts, wrapped around every upstream call | `gateway/resilience.py` |
| Client retry safety | `IdempotencyStore` — an `Idempotency-Key` header dedupes retried requests so they're served from the first completed response instead of re-hitting the upstream provider | `gateway/resilience.py` |
| Multi-instance anomaly drift | `DistributedAnomalyScorer` — Redis-backed EWMA so all gateway replicas share the same per-tenant behavioral-drift score (a slow-ramp attacker rotating across instances can't evade a purely local scorer) | `gateway/policy_engine.py` |
| Config correctness | `GatewaySettings` (pydantic `BaseSettings`) validates every tunable at boot — e.g. a malformed vault key or invalid log level fails fast at startup, not mid-request | `gateway/settings.py` |
| Payload/bandwidth | GZip response compression + a request-body size cap (413 on oversized payloads) | `gateway/main.py` |
| Traceability | Correlation-ID middleware binds `X-Request-ID` to a contextvar read by both the structured logger and retry/backoff logging | `gateway/resilience.py`, `gateway/logging_config.py` |
| Rate-limit transparency | `X-RateLimit-Limit` / `Retry-After` headers on every response | `gateway/main.py` |

## Quality tooling

- **Lint**: `ruff check gateway tests` (`pyproject.toml` — flags unused
  imports, bare excepts, common async footguns).
- **Type-check**: `mypy gateway`.
- **CI**: `.github/workflows/ci.yml` runs lint → type-check → pytest with
  coverage (`--cov-fail-under=70`) against live Postgres/Redis service
  containers, plus a `pip-audit` dependency vulnerability scan.
- **Load testing**: `locust -f locustfile.py --host http://localhost:8000`
  — mixes benign, PII-bearing, and adversarial-jailbreak traffic so a perf
  run also exercises the guardrail hot paths, not just a pass-through echo.
- **Additional test module**: `tests/test_performance_and_resilience.py`
  covers the LRU/TTL cache, cache-key derivation, embedding-cache hit
  tracking, retry/backoff (success-after-transient-failure, exhaustion,
  non-retryable passthrough), the concurrency bulkhead's in-flight cap, and
  idempotency deduplication.

## Production notes

- Set `GATEWAY_VAULT_MASTER_KEY_HEX` to a securely generated 32-byte hex key
  (e.g. `openssl rand -hex 32`) and load it from a secrets manager, not the
  environment file, in production. `GatewaySettings` rejects a malformed or
  wrong-length key at startup.
- `PIISanitizerEngine` degrades gracefully to regex-only matching if spaCy
  or its model isn't installed; `JailbreakDetector`'s semantic pass falls
  back to a dependency-free n-gram embedder if `numpy` isn't present.
- `RedisCircuitBreaker`, `ResponseCache`, and `DistributedAnomalyScorer` all
  fail open to local in-memory state if Redis is unreachable, so the gateway
  degrades availability gracefully rather than hard-crashing — safety
  checks upstream (jailbreak/PII/moderation) remain fail-closed regardless.
- `docker-compose.yml` runs the gateway with `replicas: 2` and a `/readyz`
  healthcheck as a starting point for horizontal scaling; the Redis-backed
  cache, circuit breaker, and anomaly scorer are what make that safe (shared
  state across replicas instead of each instance diverging).

