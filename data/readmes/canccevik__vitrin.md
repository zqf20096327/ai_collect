# Vitrin

_Polyglot microservice backend for a social content platform — NestJS · Python · gRPC · RabbitMQ · Neo4j · Qdrant · ClickHouse_

Vitrin is an open-source backend architecture project that uses a social content platform domain to model real distributed-systems problems: service boundaries, proto-first contracts, reliable events, Redis-backed feeds, graph/vector retrieval, ML-powered ranking, workflow orchestration and end-to-end observability.

## Architecture

![System Architecture](docs/assets/system-architecture.png)

HTTP traffic enters through API Gateway; WebSocket traffic enters through Realtime Gateway. Internal synchronous calls use proto-first gRPC contracts generated from `libs/contracts`, managed by Buf and protected with lint and breaking-change checks. Asynchronous domain events flow through RabbitMQ topic routing. Services own their data boundaries, so application state stays local instead of converging on a shared database. The runtime is split across 15 services: 14 NestJS/TypeScript services and one Python ML service.

```txt
Client
  -> API Gateway / Realtime Gateway
  -> gRPC service boundary
  -> RabbitMQ domain events
  -> specialized stores and projections
```

## Feed & recommendation pipeline

> The feed system is split into two paths: a low-latency following timeline and a ranked home feed powered by retrieval, filtering, ML scoring and sessionized delivery.

### Following feed: fanout timeline

![Following Feed Fanout Timeline](docs/assets/following-feed-fanout-timeline.png)

Following feed is a delivery problem, not a query problem. Vitrin pushes post creation events into Redis-backed follower timelines and lets the fanout planner choose a delivery strategy based on author scale and write amplification tradeoffs.

| Fanout mode | When it fits | Write behavior | Read behavior |
|---|---|---|---|
| EAGER | Normal authors with manageable follower count | Push post IDs into follower timelines | Read follower timeline directly |
| LAZY | High-follower authors | Write into author-side outbox or buffer | Pull author-side candidates at read time |
| HYBRID | Medium or high-follower authors | Push to a limited follower shard plus keep author-side state | Combine pushed and pulled candidates |

The planner uses EAGER for authors whose follower counts can absorb direct fanout, LAZY when write amplification would be too high, and HYBRID when the optimal path depends on both follower scale and read frequency.

`fanout-service` turns post creation events into timeline state, while cleanup and backfill jobs keep the read model healthy over time.

The read side can combine pushed timeline state with author-side buffers when the chosen strategy requires it.

```txt
PostCreated event
  -> fanout planner
  -> EAGER: follower timelines
  -> LAZY: author outbox
  -> HYBRID: limited follower timelines + author outbox
  -> feed reads Redis-backed candidate state
```

This keeps normal authors cheap to read, while preventing high-follower authors from creating massive synchronous write amplification.

### Home feed: online serving loop

![Home Feed Recommendation Flow](docs/assets/home-feed-recommendation-flow.png)

Home feed is the ranked discovery path. It is split into retrieval, eligibility filtering, feature hydration, ML scoring, reranking, session storage and feedback collection. The request path stays low latency, but the ranking logic still has enough structure to support graph, vector and analytics signals.

| Stage | Owner | Output |
|---|---|---|
| Session resolution | `feed-service` | Fresh recommendation session or cursor continuation |
| Candidate retrieval | `recommendation-service` | Graph, vector, trending and exploration candidate pool |
| Eligibility filtering | `recommendation-service` | Blocked, seen, hidden and preference-filtered candidates removed |
| Feature hydration | `recommendation-service` | Candidate features prepared for scoring: interaction history, social distance, content metadata, source signal type, recency, context signals |
| ML scoring | `ml-service` | Scores from the active LightGBM model |
| Reranking | `recommendation-service` | Diversified ranked candidate list |
| Session storage | `feed-service` | Redis-backed ranked feed session |
| Response hydration | `feed-service` | Post, author and content response data |
| Feedback write | `feed-service` | Served and feed events written to ClickHouse |

The request path is intentionally staged: retrieval broadens the candidate pool, filtering removes invalid items, scoring ranks what remains, and reranking keeps the feed diverse enough to stay useful.

### Candidate sources

| Source | Backing system | Why it exists |
|---|---|---|
| Graph | Neo4j via `graph-service` | Social proximity, follows, interactions and second-degree discovery |
| Vector | Qdrant | Semantic similarity through embeddings |
| Trending | ClickHouse | Recent interaction momentum |
| Exploration | Recent content pool | Freshness and serendipity |

![Neo4j Graph Projection](docs/assets/neo4j-graph-projection.png)
_Neo4j graph projection used by `graph-service` for social proximity, interaction signals and graph-based recommendation candidates._

Online serving produces feedback; feedback becomes training data. The same request path that serves the feed also feeds the offline learning loop through ClickHouse interaction events.

## ML platform

### Online scoring path

```txt
Recommendation Service
  -> candidate pool
  -> online feature hydration
  -> ML Service ScoreCandidates
  -> active LightGBM model
  -> scored candidates
  -> rerank / fallback
```

`ml-service` is a dedicated Python 3.12 runtime. Recommendation Service builds the candidate pool and sends hydrated features to `ml-service` over gRPC. `ModelLoader` keeps the active champion model in memory and scores candidates on each request. The Python runtime keeps model serving, feature materialization and embedding workflows close to the Python ML ecosystem while product services remain in NestJS.

### Offline learning loop

| Step | Component | Output |
|---|---|---|
| Materialize features | Feast / `ml-service` | online/offline feature values |
| Build dataset | ClickHouse / `ml-service` | training dataset artifact |
| Train candidate | LightGBM | candidate model |
| Evaluate | `ml-service` | AUC, NDCG@20 and dataset quality metrics |
| Promote | MLflow | champion alias update |
| Reload | `ml-service` | active model hot-swap |

Feed and interaction events accumulate in ClickHouse. `workflow-service` triggers the continuous learning cycle as an orchestrated saga: materialize features, build the training dataset, train a candidate model, evaluate it, check the promotion gate, promote the candidate in MLflow and reload the serving model without restart.

### Model lifecycle

- `ModelLoader` tracks the active champion model.
- MLflow holds registry metadata, experiment runs and candidate/champion aliases.
- Model and dataset artifacts are stored in Cloudflare R2 through S3-compatible storage.
- Promotion gates combine ranking metrics and dataset quality signals.

### ML observability

The ML runtime emits OpenTelemetry traces, Prometheus metrics and structured logs around scoring, feature materialization, training, evaluation and reload operations.

## Workflow engine & sagas

`workflow-service` orchestrates long-running multi-service workflows. Each step is tracked, failures trigger compensating actions and the workflow can resume from the last successful checkpoint.

### Why a workflow service?

Without a dedicated orchestrator, long-running flows get split across domain services as ad-hoc state machines, timeouts and compensating calls scattered through business logic. workflow-service centralizes step tracking, so every workflow has an explicit execution record: which step ran, what it returned, whether it succeeded. When a step fails, the engine executes the compensating action for each completed step in reverse order, leaving domain state consistent. When a transient failure occurs mid-flow, the workflow resumes from the last successful checkpoint instead of restarting from scratch. Domain services stay unaware of the broader orchestration — they only handle the individual gRPC or event calls directed at them.

### Registration saga

```txt
Create pending account
  -> send verification code
  -> wait for verification signal
  -> create/activate user profile
  -> complete registration
```

Registration coordinates the multi-step user onboarding flow across `auth-service` and `user-service`: account creation, OTP verification, profile initialization and completion. Compensating steps handle partial failures at each stage.

### ML continuous learning saga

```txt
training window
  -> feature materialization
  -> dataset build
  -> candidate training
  -> evaluation
  -> promotion gate
  -> model promotion
  -> serving reload
```

`workflow-service` issues gRPC calls to `ml-service` for each job, tracks step state, applies the promotion gate decision and triggers model reload on success. Failed evaluations or gate failures leave the current champion model untouched.

## Event-driven architecture

```txt
Service local write
  -> outbox
  -> RabbitMQ topic
  -> consumer inbox
  -> projection / side effect
```

| Layer | Responsibility |
|---|---|
| Event contracts | Shared schema under `libs/contracts` |
| Outbox | Stores publish intent with local writes |
| RabbitMQ | Routes events by topic |
| Inbox | Deduplicates consumer handling |
| DLQ | Isolates messages that cannot be processed |
| Trace headers | Preserve observability across async boundaries |

Domain events use RabbitMQ topic routing. Event contracts live alongside gRPC contracts under `libs/contracts` and cover auth, user, post, graph, library and messaging domains. The outbox/inbox pattern makes publication transactional with the originating write and keeps consumer handling idempotent through event-ID deduplication. Retry and dead-letter queues are configured per consumer.

## Infrastructure & reliability

`libs/infrastructure` is the shared platform layer behind the services. It prevents each domain service from re-implementing the same distributed-systems concerns: reliable event publishing, idempotent writes, Redis runtime state, service-to-service resilience, tracing, metrics, logging, health checks and graceful shutdown.

| Module map | What it covers |
|---|---|
| `outbox` `inbox` `rmq` | Reliable event publishing, deduplication and retry isolation |
| `redis` `cache` `counter` | Sessions, timelines, ranked feed state, counters and atomic coordination |
| `grpc` `http` | Resilience wrappers for outbound calls |
| `idempotency` | Request replay protection for writes |
| `observability` `logger` `metrics` `sentry` | Tracing, metrics, structured logs and error tracking |
| `database` `clickhouse` `elasticsearch` `qdrant` | Store-specific connection and module patterns |
| `health` `rate-limit` `shutdown` `config` | Health probes, rate limiting, shutdown hooks and config loading |

### Reliable events: outbox + inbox

Reliable event delivery starts at the write boundary. The domain service persists its state and publish intent together, then the broker publish happens after commit, and consumers keep their side effects idempotent through inbox state.

```txt
Service command
  -> local database transaction
  -> outbox record
  -> outbox publisher
  -> RabbitMQ topic exchange
  -> consumer inbox dedupe
  -> projection / side effect
```

- The outbox stores publish intent in the same transaction as the domain write.
- The publisher moves events to RabbitMQ after commit.
- The inbox deduplicates consumer handling by event identity.
- Retry, delayed retry and DLQ behavior isolate failed messages.
- Trace and correlation headers continue across RabbitMQ message headers.

### Idempotent writes

HTTP and gRPC write paths can be protected with idempotency keys. Request fingerprints prevent key reuse with a different payload. Retried requests can replay the original response instead of executing the handler again. This protects against duplicate side effects during client retries, network timeouts or gateway retries.

### Redis as a runtime layer

| Use case | How Redis is used |
|---|---|
| Sessions | API Gateway session state |
| Feed timelines | Following feed timeline state |
| Home feed sessions | Ranked result session and cursor state |
| Cache | Service-level cache with stampede protection |
| Counters | High-frequency interaction deltas as a speed layer |
| Idempotency | Request replay records and conflict state |
| Locks | Stampede protection and atomic coordination |

Redis is not used only as a cache. It acts as low-latency runtime infrastructure for sessions, timelines, ranked feed sessions, counters, idempotency records and coordination locks.

High-frequency counters use a speed-layer pattern: Redis absorbs realtime deltas, while scheduled batch jobs flush aggregated values back to persistent storage.

### Service-to-service resilience

Downstream failures should not cascade across the request graph.

```txt
gRPC call
  -> deadline / timeout
  -> retry policy
  -> circuit breaker
  -> fallback or mapped error
```

gRPC clients are wrapped with timeout, retry and circuit breaker policies. HTTP outbound helpers follow the same resilience model. Error mapping keeps infrastructure failures and domain failures distinguishable.

### Operational primitives

- health probes
- rate limiting
- graceful shutdown
- centralized config loading
- Sentry error tracking
- shared data-store modules

_See [`docs/infrastructure.md`](docs/infrastructure.md) for the full design._

## Observability

Observability is part of the platform layer, not an external afterthought. Services emit structured logs, expose Prometheus metrics and propagate OpenTelemetry context across HTTP, gRPC and RabbitMQ.

![Grafana Service Dashboard](docs/assets/grafana-service-dashboard.png)
_Per-service Grafana dashboard: request rate, latency percentiles, error rate and outbox backlog._

![Home Feed Distributed Trace](docs/assets/home-feed-trace.png)
_Distributed trace for a home feed request: API Gateway → Feed Service → Recommendation Service → ML Service, including gRPC spans and ClickHouse write._

| Signal | Tooling | Example |
|---|---|---|
| Metrics | Prometheus + Grafana | request rate, latency, error rate, outbox backlog, ML scoring latency |
| Logs | Loki + structured logging | correlation IDs, request IDs, trace IDs |
| Traces | OpenTelemetry + Tempo | API Gateway -> Feed Service -> Recommendation Service -> ML Service |
| Errors | Sentry | captured exceptions and service context |

```txt
GET /feed/home
  -> api-gateway
  -> feed-service
  -> recommendation-service
  -> ml-service ScoreCandidates
  -> ClickHouse feed-event write
```

A home feed request can be traced from API Gateway to Feed Service, Recommendation Service and ML Service, including downstream gRPC spans, model scoring latency and ClickHouse feed-event writes.

## Proto-first contracts

All service APIs are defined as Protocol Buffer contracts under `libs/contracts`. TypeScript clients are generated for NestJS services; Python clients are generated for `ml-service`. The same contract layer covers both gRPC service definitions and RabbitMQ event schemas.

Buf manages the full contract lifecycle:

```txt
libs/contracts
  -> protoc + Buf plugins
  -> generated TypeScript gRPC clients (NestJS services)
  -> generated Python gRPC clients (ml-service)
  -> shared event schema contracts
```

Breaking-change detection runs against the previous contract snapshot, so interface regressions are caught before they reach service boundaries. Proto lint enforces field naming, deprecation and style rules across all definitions.

```bash
pnpm run lint:proto
pnpm run breaking:proto
pnpm run generate:proto
```

## Realtime & messaging

`realtime-gateway` handles all WebSocket connections. Presence state and typing indicators are maintained per connection and surfaced to conversation participants in realtime. `messaging-service` owns the conversation model: messages are stored as encrypted envelopes, so the server never holds plaintext message content. Each user device holds its own decryption material. Read receipts and delivery receipts are tracked per device.

```txt
Client WebSocket
  -> realtime-gateway
  -> presence state
  -> typing indicators
  -> messaging-service (encrypted envelopes, receipts, device keys)
```

## Services

Each service owns a focused boundary and communicates through contracts rather than shared tables. API Gateway composes client-facing HTTP responses; domain services own writes; read models, feeds and recommendations are built through events and specialized stores.

| Service | Runtime | Responsibility |
|---|---|---|
| `api-gateway` | NestJS / TypeScript | HTTP ingress, session auth, gRPC orchestration |
| `auth-service` | NestJS / TypeScript | Registration, login, OTP, password recovery |
| `user-service` | NestJS / TypeScript | Accounts, profiles, summaries |
| `post-service` | NestJS / TypeScript | Posts, comments, reactions, saves, counters |
| `explore-service` | NestJS / TypeScript | Provider search, external content indexing |
| `library-service` | NestJS / TypeScript | Library states, favorites, ratings, content stats |
| `messaging-service` | NestJS / TypeScript | Conversations, encrypted envelopes, devices, receipts |
| `realtime-gateway` | NestJS / TypeScript | Socket delivery, presence, typing |
| `notification-service` | NestJS / TypeScript | Auth email delivery events |
| `workflow-service` | NestJS / TypeScript | Workflow engine, registration saga, ML lifecycle saga |
| `graph-service` | NestJS / TypeScript | Follows, blocks, Neo4j recommendation graph |
| `fanout-service` | NestJS / TypeScript | Timeline fanout, backfill, cleanup |
| `feed-service` | NestJS / TypeScript | Following feed, home feed sessions, feed events |
| `recommendation-service` | NestJS / TypeScript | Candidate generation, filtering, ranking orchestration |
| `ml-service` | Python 3.12 | Online scoring, embeddings, training, model lifecycle |

## Tech stack

| Area | Technologies |
|---|---|
| Backend | NestJS, TypeScript, Node.js |
| ML Service | Python 3.12, LightGBM, pandas, MLflow |
| Communication | gRPC, Protocol Buffers, RabbitMQ, WebSocket |
| Data Stores | PostgreSQL, Redis, ClickHouse, Elasticsearch, Neo4j, Qdrant |
| ML Platform | Feast, MLflow, Qdrant, Cloudflare R2 / S3-compatible artifact storage |
| Reliability | Outbox, inbox, idempotency, circuit breaker, rate limiting |
| Observability | OpenTelemetry, Prometheus, Grafana, Loki, Tempo |
| Deployment | Docker Compose, Kubernetes, Kustomize |
| Tooling | Nx, pnpm, Buf |

## Local development

```bash
pnpm install
pnpm run generate:proto
docker compose -f infra/compose/docker-compose.infra.yml up -d
pnpm run clickhouse:migrate --service feed-service
pnpm run start:api
pnpm run ml:main
# optional: seed demo data
# generates users, follows, posts, interactions, negative signals and feed events
# negative interactions (not-interested, blocks) and feed events are required for realistic ML training data
pnpm run seed:dev
```

- `pnpm@11.0.8` is declared in `package.json`.
- Python `ml-service` requires Python `>=3.12`.
- ClickHouse migrations are explicit through `tools/clickhouse/migrate.ts`.
- Environment references live in per-service `.env.example` files and `infra/compose/.env.example`.
- Kubernetes manifests live under `infra/k8s` with Kustomize overlays for environment separation. Docker Compose is used for local infrastructure only.
- Each service has its own manifest; data store deployments are included for staging and production environments.

## Documentation

- [Architecture](docs/architecture.md)
- [Infrastructure & Reliability](docs/infrastructure.md)
- [Services](docs/services.md)
- [Event-driven Architecture](docs/event-driven-architecture.md)
- [Feed & Recommendation](docs/feed-recommendation.md)
- [ML Platform](docs/ml-platform.md)
- [Observability](docs/observability.md)
- [Workflows](docs/workflows.md)
- [Local Development](docs/local-development.md)
- [Seeding](docs/seeding.md)

## Contributing

Vitrin is open to architecture feedback, bug reports and focused contributions.

- [Contributing Guide](CONTRIBUTING.md) explains how to set up the project, follow commit conventions and open pull requests.
- [Code of Conduct](CODE_OF_CONDUCT.md) defines the expected community standards.
- [Security Policy](SECURITY.md) explains how to report security issues responsibly.
- GitHub issue templates are available for bug reports and feature requests.
- Pull requests use the repository PR template to keep changes reviewable and consistent.

## License

This project is licensed under the [AGPL-3.0-only](LICENSE).
