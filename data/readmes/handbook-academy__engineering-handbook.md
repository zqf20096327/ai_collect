<div align="center">

<img src="logo.svg" alt="Handbook Academy" width="140" />

# The Engineering Handbook

**Free, open-source engineering books for people who build software.**<br/>
System design, data structures and algorithms, and AI engineering, each taught in full and free to read forever.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![CI](https://github.com/handbook-academy/engineering-handbook/actions/workflows/content-ci.yml/badge.svg)](https://github.com/handbook-academy/engineering-handbook/actions)
[![GitHub stars](https://img.shields.io/github/stars/handbook-academy/engineering-handbook?style=social)](https://github.com/handbook-academy/engineering-handbook/stargazers)

**[Read online at handbook.academy](https://handbook.academy)**

[HLD Handbook](#the-hld-handbook) · [DSA Handbook](#the-dsa-handbook) · [AI Engineering Handbook](#the-ai-engineering-handbook) · [Where to start](#where-to-start) · [Study plans](#study-plans) · [Contributing](#contributing) · [FAQ](#faq)

</div>

---

## Table of contents

- [About this project](#about-this-project)
- [The three handbooks](#the-three-handbooks)
- [Read online](#read-online)
- [Who it's for](#who-its-for)
- [Where to start](#where-to-start)
- [The HLD Handbook](#the-hld-handbook)
  - [Parts at a glance](#hld-parts-at-a-glance)
  - [Trade-offs Library](#trade-offs-library)
- [The DSA Handbook](#the-dsa-handbook)
  - [Parts at a glance](#dsa-parts-at-a-glance)
  - [Pattern decision pages](#pattern-decision-pages)
  - [Long-form editorials](#long-form-editorials)
  - [Interactive widget specs](#interactive-widget-specs)
- [The AI Engineering Handbook](#the-ai-engineering-handbook)
  - [Parts at a glance](#ai-engineering-parts-at-a-glance)
- [Study plans](#study-plans)
- [How the books are written](#how-the-books-are-written)
- [Contributing](#contributing)
- [Repository structure](#repository-structure)
- [Development setup](#development-setup)
- [FAQ](#faq)
- [License](#license)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [Community](#community)

---

## About this project

The Engineering Handbook is a set of free textbooks for software engineers. Each book is a complete course: every topic is taught on the page, from first principles to the mistakes teams make in production. You won't find outlines, link lists, or "read this elsewhere" here.

The books live in this repository as plain Markdown. They render on GitHub with every diagram, figure and footnote intact, and the same text powers the websites at [handbook.academy](https://handbook.academy). Everything is licensed [CC BY-SA 4.0](LICENSE), so the text stays free to read, share and adapt.

What makes the books different:

- **Taught in full.** Each chapter explains the idea, shows it in diagrams and worked examples, compares the alternatives, and ends with what to watch for in production.
- **Opinionated.** Chapters recommend an approach and explain why. When reasonable people disagree, the trade-offs are spelled out so you can decide.
- **Sourced.** Claims are backed by footnoted primary sources: papers, RFCs, official documentation and engineering postmortems.
- **Current.** The books cover today's stack: LLM serving, RAG, agents, MCP, CRDTs, edge computing, FinOps and post-quantum cryptography. Every chapter records when it was last updated.
- **Open.** Anyone can suggest a fix, and every change goes through review.

## The three handbooks

| Handbook | What you'll learn | Best for | Read |
|---|---|---|---|
| **[HLD Handbook](#the-hld-handbook)** | How to design large software systems: networking and storage, distributed systems theory, architecture, reliability, security, end-to-end case studies, and AI system design. | System design interviews, and engineers who design or operate backend systems. | [Chapters](#hld-parts-at-a-glance) · [Website](https://hld.handbook.academy) |
| **[DSA Handbook](#the-dsa-handbook)** | Data structures and algorithms organized by pattern, with LeetCode problems solved in Python, and most also in Java, C++ and Go. | Coding interviews, competitive programming, and sharpening problem-solving. | [Chapters](#dsa-parts-at-a-glance) · [Website](https://dsa.handbook.academy) |
| **[AI Engineering Handbook](#the-ai-engineering-handbook)** | How to build and run production AI products on top of model APIs: prompts, evals, context, retrieval, agents, observability, security, cost and product. | Software engineers shipping AI features. No model training required. | [Chapters](#ai-engineering-parts-at-a-glance) · [Website](https://ai-eng.handbook.academy) |

## Read online

Each book also has its own website. Every chapter is free to read there, for anyone, with no sign-in needed.

| Site | Address | What's there |
|---|---|---|
| **Home** | [handbook.academy](https://handbook.academy) | All three books |
| **HLD Handbook** | [hld.handbook.academy](https://hld.handbook.academy) | The HLD Handbook |
| **DSA Handbook** | [dsa.handbook.academy](https://dsa.handbook.academy) | The DSA Handbook |
| **AI Engineering Handbook** | [ai-eng.handbook.academy](https://ai-eng.handbook.academy) | The AI Engineering Handbook |

Prefer GitHub? Every chapter link in this README opens the source file, and Mermaid diagrams render right in the browser.

## Who it's for

- **Engineers preparing for interviews.** DSA for the coding rounds, HLD for system design, and both books' interview framework parts for the round itself.
- **Engineers moving up a level.** HLD's distributed systems, reliability and security parts are what separate Senior from Staff designs.
- **Engineers building AI features.** The AI Engineering Handbook covers making an LLM feature reliable, measurable, secure and affordable.
- **Self-taught engineers.** HLD's Prerequisites and DSA's Foundations cover the computer science a degree would have given you.
- **Career switchers** moving from frontend to backend, backend to infrastructure, or software to AI, who need system-level intuition fast.
- **Teachers and course creators** who want a full curriculum to build on. The license allows it.

**Not the right fit:** if you've never programmed, start with [CS50](https://cs50.harvard.edu/) or [The Odin Project](https://www.theodinproject.com/) and come back. The books also teach concepts that apply across languages rather than any one language's syntax.

## Where to start

| I want to… | Start here |
|---|---|
| Get a quick taste of system design | [Scalability](content/hld/part-1-core-fundamentals/00-scalability.md) → [Back-of-the-envelope estimation](content/hld/part-1-core-fundamentals/04-back-of-envelope-estimation.md) → [Design a URL shortener](content/hld/part-8-case-studies/00-url-shortener.md) |
| Prepare for a system design interview | [How to approach a design question](content/hld/part-1-core-fundamentals/05-how-to-approach-design-questions.md), then the [interview prep plan](#interview-prep-sde1-to-sde2) |
| Refresh my distributed systems foundations | [HLD Part 3 — Distributed Systems Theory](#hld-part-3) |
| Get better at coding interviews | [Arrays](content/dsa/part-1-linear-data-structures/00-arrays.md) → [Two pointers](content/dsa/part-3-pointers-window-prefix/00-two-pointers-opposite.md) → [Sliding window](content/dsa/part-3-pointers-window-prefix/03-sliding-window-variable.md) |
| Choose between two approaches | The [Trade-offs Library](#trade-offs-library) for design, the [pattern decision pages](#pattern-decision-pages) for algorithms |
| Build an AI feature that holds up | [What an AI engineer is](content/ai-eng/part-0-start-here/00-what-an-ai-engineer-is.md) → [The escalation ladder](content/ai-eng/part-0-start-here/03-the-escalation-ladder.md) → [Why you can't ship without evals](content/ai-eng/part-4-eval-fundamentals/00-why-you-cant-ship-without-evals.md) |
| Design AI systems at scale | [HLD Part 9 — AI & ML System Design](#hld-part-9) and the [AI systems case studies](#ai-systems) |
| Follow a plan with a deadline | [Study plans](#study-plans), from one weekend to the full curriculum |

---

## The HLD Handbook

**How to design large software systems, from the network up to LLM serving.**

[Website](https://hld.handbook.academy) · [`content/hld/`](content/hld/) · [Style guide](STYLE_GUIDE.md)

The HLD Handbook starts with the prerequisites (networking, operating systems, databases, API design) and builds up through the building blocks, distributed systems theory, data systems and architecture patterns. It then covers what it takes to run systems for real: reliability, operations and security. The case studies put it all together in end-to-end designs, and the last parts cover AI system design and how to handle the interview.

**How a chapter is built.** Each teaching chapter follows the same path: an introduction, the idea from first principles, diagrams, a worked example, the trade-offs, production gotchas, and references. Case studies follow the interview shape instead: requirements, estimates, API, data model, architecture, deep dives, and scaling.

### HLD parts at a glance

Pick a part number to jump to its chapters, or open any part below.

| Part | What it covers | Level |
|---|---|---|
| [0](#hld-part-0) | **Prerequisites** — networking, OS, data structures, databases, API design | Beginner |
| [1](#hld-part-1) | **Core Fundamentals** — scalability, latency, availability, consistency, estimation, trade-off thinking | Beginner to intermediate |
| [2](#hld-part-2) | **Building Blocks** — load balancers, caches, queues, CDNs, databases, sharding, pub/sub, rate limiting, blob storage, geo, edge | Intermediate to advanced |
| [3](#hld-part-3) | **Distributed Systems Theory** — consensus, consistency, clocks, CRDTs, transactions | Intermediate to advanced |
| [4](#hld-part-4) | **Data Systems** — storage engines, OLTP/OLAP, warehouses/lakes, streams, search, time-series, graph, vector, KV | Intermediate to advanced |
| [5](#hld-part-5) | **Architecture Patterns** — monolith vs micro, event-driven, CQRS, ES, serverless, BFF, strangler, hex, multi-region, multi-tenant, CRDT apps | Intermediate to advanced |
| [6](#hld-part-6) | **Reliability & Operations** — observability, SLOs, resilience, scaling, deploys, chaos, incidents, FinOps, platform | Intermediate to advanced |
| [7](#hld-part-7) | **Security at Scale** — AuthN/Z, OAuth/OIDC, JWT, mTLS, secrets, DDoS/WAF, compliance, supply chain, privacy, PQC | Intermediate to advanced |
| [8](#hld-part-8) | **Case Studies** — end-to-end designs, grouped by theme; the centerpiece of interview prep | Intermediate to advanced |
| [9](#hld-part-9) | **AI & ML System Design** — LLM serving, RAG, vector search, agents, LLMOps, safety, recommenders, multimodal | Intermediate to advanced |
| [10](#hld-part-10) | **Emerging Patterns** — green and sustainable computing | Intermediate |
| [11](#hld-part-11) | **Interview Framework** — RESHADED/PEDALS/ADEPT, requirements, diagrams, trade-offs, company flavors, RFCs | Intermediate to advanced |

<details>
<summary><a id="hld-part-0"></a><strong>Part 0 · Prerequisites</strong></summary>

**Level:** Beginner &nbsp;·&nbsp; **For:** Engineers without a CS degree, or anyone who wants to confirm their foundations before moving on.

Foundational topics that the rest of the handbook assumes. If you can explain TCP's three-way handshake, the difference between a process and a thread, a B-tree's internal structure, and why idempotent PUT is better than non-idempotent POST for a retry-prone endpoint — you can skip this part.

| # | Chapter | What it covers |
|:-:|---|---|
| 0.0 | [Networking Fundamentals for System Design](content/hld/part-0-prerequisites/00-networking-fundamentals.md) | A practical tour of OSI layers, TCP/UDP, HTTP/1.1 through HTTP/3, DNS, TLS 1.3, and realtime transports like WebSockets and SSE. |
| 0.1 | [Operating System Essentials for System Design](content/hld/part-0-prerequisites/01-os-essentials.md) | Processes, threads, memory hierarchy with real latency numbers, I/O models (epoll, kqueue, io_uring), and file system internals you need to design systems. |
| 0.2 | [Data Structures for Distributed Systems](content/hld/part-0-prerequisites/02-data-structures-for-systems.md) | The handful of data structures that power modern infrastructure: hash tables, B-trees, LSM-trees, Bloom filters, skip lists, and consistent hashing rings. |
| 0.3 | [Database Fundamentals for System Design](content/hld/part-0-prerequisites/03-database-fundamentals.md) | SQL, ACID, indexing, query execution, and the normalization vs denormalization debate, covered at the depth you need to design real systems. |
| 0.4 | [API Design Basics: REST, GraphQL, gRPC, and the Hard Parts](content/hld/part-0-prerequisites/04-api-design-basics.md) | Resource modeling, GraphQL's N+1 problem, gRPC streaming, versioning strategies, idempotency keys, and cursor pagination done right. |

</details>

<details>
<summary><a id="hld-part-1"></a><strong>Part 1 · Core Fundamentals</strong></summary>

**Level:** Beginner to intermediate &nbsp;·&nbsp; **For:** Everybody — read this part even if you know the topic, because the vocabulary here is used for the rest of the book.

The vocabulary and the reasoning habits that every later chapter assumes. "Scalability," "consistency," "trade-off," and "back-of-envelope" get defined here rigorously so they mean something specific when we use them later.

| # | Chapter | What it covers |
|:-:|---|---|
| 1.0 | [Scalability: Growing a System Without Breaking It](content/hld/part-1-core-fundamentals/00-scalability.md) | Vertical vs horizontal scaling, stateless services, read vs write scaling, and when scaling is the wrong answer. The vocabulary every system design conversation uses. |
| 1.1 | [Latency and Throughput: The Two Numbers That Matter](content/hld/part-1-core-fundamentals/01-latency-and-throughput.md) | Latency vs throughput, Jeff Dean's numbers, tail latency (p50/p95/p99), Little's Law, and how to find the real bottleneck in any system. |
| 1.2 | [Availability and Reliability: Nines, SLOs, and Staying Up](content/hld/part-1-core-fundamentals/02-availability-and-reliability.md) | Availability math, MTBF/MTTR, redundancy patterns, SLI/SLO/SLA, error budgets, dependency math, and real-world outage lessons. |
| 1.3 | [Consistency Models: What Readers Actually See](content/hld/part-1-core-fundamentals/03-consistency-models.md) | Strong, eventual, and causal consistency. Read-your-writes, monotonic reads, and the client-centric vs data-centric distinction that makes consistency tractable. |
| 1.4 | [Back-of-the-Envelope Estimation](content/hld/part-1-core-fundamentals/04-back-of-envelope-estimation.md) | Powers of 2 and 10, storage and bandwidth templates, QPS math, and worked examples for Twitter and YouTube scale. The interview skill that matters in production too. |
| 1.5 | [How to Approach a System Design Question](content/hld/part-1-core-fundamentals/05-how-to-approach-design-questions.md) | A repeatable 6-step framework for 45-minute system design interviews: clarify, estimate, API, high-level design, deep dive, trade-offs. Minute-by-minute plan with company-specific flavors. |
| 1.6 | [Trade-off Thinking](content/hld/part-1-core-fundamentals/06-trade-off-thinking.md) | Every design decision is a trade-off. How to articulate, structure, and defend your choices, and how to recognize when not choosing is the right move. |

</details>

<details>
<summary><a id="hld-part-2"></a><strong>Part 2 · Building Blocks</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone who'll assemble backend systems. This part is the Lego brick inventory.

Deep dives on the pieces you assemble to build real systems: load balancers, caches, queues, CDNs, databases (SQL and NoSQL), partitioning, replication, pub/sub, rate limiters, service discovery, blob storage, geospatial indexes, and edge compute.

| # | Chapter | What it covers |
|:-:|---|---|
| 2.0 | [Load Balancers: Spreading Traffic, Absorbing Failure](content/hld/part-2-building-blocks/00-load-balancers.md) | L4 vs L7 load balancing, algorithms, health checks, and how Envoy, HAProxy, NGINX, and AWS ALB/NLB actually work in production. |
| 2.1 | [Reverse Proxies and API Gateways: The Smart Edge](content/hld/part-2-building-blocks/01-reverse-proxies-api-gateways.md) | TLS termination, routing, auth, rate limiting, and why an API gateway is more than a smarter load balancer. |
| 2.2 | [Content Delivery Networks: Moving Bytes Closer to Users](content/hld/part-2-building-blocks/02-cdns.md) | How CDNs work, edge caching, cache keys and invalidation, and how Cloudflare, Akamai, and Fastly differ in practice. |
| 2.3 | [Caching: From Browser to Database](content/hld/part-2-building-blocks/03-caching.md) | Cache hierarchy, five write patterns, eviction policies (LRU/TinyLFU), stampede prevention, and why invalidation is the hardest problem in distributed systems. |
| 2.4 | [SQL Databases: The Boring Technology That Wins](content/hld/part-2-building-blocks/04-sql-databases.md) | B-trees, MVCC, isolation levels, indexing, and why PostgreSQL and MySQL are still the right answer for most systems. |
| 2.5 | [NoSQL Databases: Picking the Right Non-Relational Tool](content/hld/part-2-building-blocks/05-nosql-databases.md) | Key-value, document, wide-column, and graph stores, and how DynamoDB, Cassandra, MongoDB, and Neo4j differ in practice. |
| 2.6 | [Database Partitioning and Sharding: When One Node Is Not Enough](content/hld/part-2-building-blocks/06-database-partitioning-sharding.md) | Range, hash, and consistent-hash partitioning, hot spots, resharding, and how Notion, Figma, and Discord partition data in practice. |
| 2.7 | [Database Replication: Keeping Copies in Sync](content/hld/part-2-building-blocks/07-database-replication.md) | Leader-follower, multi-leader, and leaderless replication, sync vs async, failover, and how Postgres, MySQL, Cassandra, and DynamoDB differ. |
| 2.8 | [Message Queues and Streaming: Decoupling at Scale](content/hld/part-2-building-blocks/08-message-queues-streaming.md) | Queues vs logs, Kafka vs RabbitMQ vs SQS, delivery semantics, partitioning, consumer groups, and when streaming beats request-response. |
| 2.9 | [Pub/Sub: Fan-Out and Event-Driven Systems](content/hld/part-2-building-blocks/09-pub-sub.md) | Topics, subscriptions, fan-out strategies, and how Google Pub/Sub, Redis, NATS, and SNS+SQS implement publish/subscribe at scale. |
| 2.10 | [Real-Time Communication: WebSockets, SSE, and Long Polling](content/hld/part-2-building-blocks/10-real-time-communication.md) | Long polling, Server-Sent Events, WebSockets, WebRTC, and MQTT: when to use each, how to scale persistent connections, and production lessons from Discord and Slack. |
| 2.11 | [Rate Limiting: Protecting Systems from Themselves](content/hld/part-2-building-blocks/11-rate-limiting.md) | Token bucket, leaky bucket, fixed and sliding windows, distributed rate limiting, and how Stripe, Cloudflare, and GitHub protect their APIs. |
| 2.12 | [Service Discovery and Service Mesh: Finding and Talking to Services](content/hld/part-2-building-blocks/12-service-discovery-mesh.md) | DNS, client-side and server-side discovery, health checks, sidecars, mTLS, and what Consul, Envoy, Istio, and Linkerd actually solve. |
| 2.13 | [Blob and Object Storage: Storing the Big Stuff](content/hld/part-2-building-blocks/13-blob-object-storage.md) | S3 semantics, object storage internals, multipart uploads, lifecycle policies, and when to pick S3 vs GCS vs MinIO vs a filesystem. |
| 2.14 | [Geospatial Indexing: Geohash, Quadtree, R-tree, S2, and H3](content/hld/part-2-building-blocks/14-geospatial-indexing.md) | Space-filling curves, hierarchical grids, and tree indexes for location queries - with decision guidance on geohash vs quadtree vs R-tree vs S2 vs H3. |
| 2.15 | [Edge Computing (Cloudflare Workers, Lambda@Edge, Deno Deploy)](content/hld/part-2-building-blocks/15-edge-computing.md) | Design applications for the edge: cold starts, state replication with Durable Objects, edge databases, and the limits of running code close to users. |

</details>

<details>
<summary><a id="hld-part-3"></a><strong>Part 3 · Distributed Systems Theory</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** SDE2+ preparing for Senior/Staff. If you haven't internalized linearizability vs serializability, read this.

The theory that makes distributed systems *distributed*: consensus (Raft/Paxos), the full consistency spectrum, CAP/PACELC in 2025 framing, logical clocks, CRDTs, distributed transactions (2PC/Saga), exactly-once delivery, failure detection, consistent hashing, and Merkle-tree anti-entropy.

| # | Chapter | What it covers |
|:-:|---|---|
| 3.0 | [Consensus Protocols: How Distributed Systems Agree](content/hld/part-3-distributed-systems-theory/00-consensus-protocols.md) | Raft and Multi-Paxos explained: leader election, log replication, safety under term numbers, and why etcd, Consul, and CockroachDB picked Raft. |
| 3.1 | [Consistency Deep Dive: Linearizability, Serializability, and the Spectrum Between](content/hld/part-3-distributed-systems-theory/01-consistency-deep-dive.md) | Linearizability vs serializability vs causal vs eventual, external consistency, and how to reason precisely about what your database actually gives you. |
| 3.2 | [Quorums and Replication: The Math of R + W > N](content/hld/part-3-distributed-systems-theory/02-quorums-and-replication.md) | Read and write quorums, Dynamo-style replication, sloppy quorums, hinted handoff, and when quorums give you linearizability (and when they do not). |
| 3.3 | [CAP and PACELC: The Tradeoff That Keeps Confusing People](content/hld/part-3-distributed-systems-theory/03-cap-and-pacelc.md) | What CAP actually says (and what it doesn't), the three big misconceptions, and how PACELC fixes the omission of latency. |
| 3.4 | [Clocks and Ordering: Lamport, Vector, and Hybrid Logical Clocks](content/hld/part-3-distributed-systems-theory/04-clocks-and-ordering.md) | Why wall-clock time lies, happens-before, Lamport clocks, vector clocks, hybrid logical clocks, and Google TrueTime. |
| 3.5 | [CRDTs: Conflict-Free Replicated Data Types](content/hld/part-3-distributed-systems-theory/05-crdts.md) | State-based (CvRDT) and op-based (CmRDT) CRDTs, G-Counter, PN-Counter, OR-Set, LWW-Register, and how Yjs, Automerge, Figma, and Redis use them. |
| 3.6 | [Distributed Transactions: 2PC, Saga, and When to Avoid Both](content/hld/part-3-distributed-systems-theory/06-distributed-transactions.md) | Two-phase commit, Percolator, Sagas, outbox pattern, and the honest answer to distributed transactions: don't, or pay the price. |
| 3.7 | [Idempotency and Exactly-Once: The Honest Truth About Delivery Guarantees](content/hld/part-3-distributed-systems-theory/07-idempotency-exactly-once.md) | Why exactly-once delivery is a myth, how idempotency keys make at-least-once feel exactly-once, and how Stripe and Kafka implement it. |
| 3.8 | [Failure Detection: Deciding a Node Is Dead](content/hld/part-3-distributed-systems-theory/08-failure-detection.md) | Heartbeats, phi-accrual detectors, gossip (SWIM), and why 'is it dead or just slow?' has no correct answer. |
| 3.9 | [Consistent Hashing: Keys to Nodes Without Global Reshuffles](content/hld/part-3-distributed-systems-theory/09-consistent-hashing.md) | The hash ring, virtual nodes, bounded-load variant, rendezvous hashing, Maglev, and jump hash for distributing keys across dynamic node sets. |
| 3.10 | [Merkle Trees and Anti-Entropy: Keeping Replicas in Sync Cheaply](content/hld/part-3-distributed-systems-theory/10-merkle-trees-anti-entropy.md) | Merkle trees, anti-entropy protocols, read repair, hinted handoff, and how Dynamo, Cassandra, and Git use hashed trees to find the differences. |

</details>

<details>
<summary><a id="hld-part-4"></a><strong>Part 4 · Data Systems</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone who owns a data pipeline or picks a database.

Every flavor of data system you might pick, and when each actually fits. Storage engines (B-tree vs LSM), OLTP vs OLAP, warehouses/lakes/lakehouses, streaming vs batch, CDC, search, time-series, graph, vector, and key-value.

| # | Chapter | What it covers |
|:-:|---|---|
| 4.0 | [Storage Engines: B-Trees, LSM-Trees, and Why Your Database Feels the Way It Does](content/hld/part-4-data-systems/00-storage-engines.md) | How B-tree and LSM-tree storage engines shape read, write, and space amplification, with examples from InnoDB, PostgreSQL, RocksDB, and Cassandra. |
| 4.1 | [OLTP vs OLAP: Row Stores, Column Stores, and Matching Shape to Workload](content/hld/part-4-data-systems/01-oltp-vs-olap.md) | Why transactional systems use row-oriented storage and analytical systems use columnar, with examples from Postgres, MySQL, Redshift, BigQuery, ClickHouse, and Snowflake. |
| 4.2 | [Data Warehouses and Data Lakes: Structure, Schema, and the Lakehouse](content/hld/part-4-data-systems/02-data-warehouses-lakes.md) | How Redshift, BigQuery, Snowflake, S3-based lakes, and the lakehouse pattern with Delta Lake, Iceberg, and Hudi actually fit together. |
| 4.3 | [Stream vs Batch Processing: Lambda, Kappa, and the End of That Debate](content/hld/part-4-data-systems/03-stream-vs-batch.md) | Batch with Spark and Hadoop, streaming with Kafka Streams, Flink, and Spark Streaming, and how Lambda and Kappa architectures stack up. |
| 4.4 | [Change Data Capture: Streaming the Database's Inner Monologue](content/hld/part-4-data-systems/04-change-data-capture.md) | How Debezium, Maxwell, and the outbox pattern turn WAL and binlog entries into reliable event streams, and when each approach is the right call. |
| 4.5 | [Search Systems: Inverted Indexes, BM25, and Running Elasticsearch in Production](content/hld/part-4-data-systems/05-search-systems.md) | How Elasticsearch, OpenSearch, and Solr build inverted indexes, score with BM25, and handle faceting, relevance tuning, and sharding at scale. |
| 4.6 | [Time-Series Databases: Metrics, Events, and Retention at Scale](content/hld/part-4-data-systems/06-time-series-databases.md) | How Prometheus, InfluxDB, TimescaleDB, and VictoriaMetrics handle write-heavy time-series workloads with downsampling and retention policies. |
| 4.7 | [Graph Databases: Property Graphs, Cypher, and When Joins Are the Problem](content/hld/part-4-data-systems/07-graph-databases.md) | How Neo4j, Amazon Neptune, and Dgraph model relationships, and when graph queries beat recursive SQL joins. |
| 4.8 | [Vector Databases: Embeddings, ANN Indexes, and the Retrieval Layer for AI](content/hld/part-4-data-systems/08-vector-databases.md) | How Pinecone, Weaviate, Milvus, and pgvector store and search embeddings using HNSW and IVF approximate nearest neighbor indexes. |
| 4.9 | [Key-Value Stores: Redis, Memcached, DynamoDB, and Picking the Right Hash Table](content/hld/part-4-data-systems/09-key-value-stores.md) | How Redis, Memcached, and DynamoDB differ in durability, data model, and scaling, and when each is the right key-value store. |

</details>

<details>
<summary><a id="hld-part-5"></a><strong>Part 5 · Architecture Patterns</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Engineers making architecture-level decisions or leading service migrations.

The architectural shapes you choose between when you design anything bigger than a single service: monolith vs microservices, event-driven, CQRS, event sourcing, serverless, BFF, strangler fig, hexagonal/clean, multi-region, multi-tenancy, CRDT-based apps.

| # | Chapter | What it covers |
|:-:|---|---|
| 5.0 | [Monolith vs Microservices: Team Topology, Conway's Law, and the Distributed System Tax](content/hld/part-5-architecture-patterns/00-monolith-vs-microservices.md) | When a modular monolith beats microservices, how Conway's Law shapes architecture, and what the distributed system tax actually costs you. |
| 5.1 | [Event-Driven Architecture: Notifications, State Transfer, and Choreography](content/hld/part-5-architecture-patterns/01-event-driven-architecture.md) | The three flavors of events, how Kafka and event buses enable loose coupling, and when choreography beats orchestration. |
| 5.2 | [CQRS: Separating Reads from Writes Without Losing Your Mind](content/hld/part-5-architecture-patterns/02-cqrs.md) | Command Query Responsibility Segregation in practice: when to split read and write models, how to handle eventual consistency, and when CQRS is overkill. |
| 5.3 | [Event Sourcing: Events as the Source of Truth](content/hld/part-5-architecture-patterns/03-event-sourcing.md) | Storing state as an append-only log of events, with replay, projections, snapshots, and the ops reality of running event-sourced systems. |
| 5.4 | [Serverless: Functions, Cold Starts, and When FaaS Actually Saves Money](content/hld/part-5-architecture-patterns/04-serverless.md) | AWS Lambda, Google Cloud Functions, and Azure Functions in practice: cold starts, concurrency models, and the honest economics of serverless. |
| 5.5 | [Backend for Frontend: Per-Client API Aggregation Done Right](content/hld/part-5-architecture-patterns/05-backend-for-frontend.md) | When one API cannot serve web, mobile, and partner clients well, the BFF pattern gives each client its own aggregation layer. |
| 5.6 | [Strangler Fig: Incremental Migration Without a Big Bang](content/hld/part-5-architecture-patterns/06-strangler-fig.md) | Martin Fowler's strangler fig pattern for replacing legacy systems incrementally, with routing, facades, and how teams actually execute multi-year migrations. |
| 5.7 | [Hexagonal and Clean Architecture: Keeping Business Logic Independent](content/hld/part-5-architecture-patterns/07-hexagonal-clean-architecture.md) | Ports and adapters, clean architecture, and onion architecture: how to keep domain logic testable and framework-independent. |
| 5.8 | [Multi-Region Architecture: Active-Passive, Active-Active, and CRDTs](content/hld/part-5-architecture-patterns/08-multi-region-architecture.md) | Designing systems that survive regional failure: DNS failover, active-passive replication, active-active with CRDTs, and Cloudflare's model. |
| 5.9 | [Multi-Tenancy: Silo, Pool, and the SaaS Isolation Spectrum](content/hld/part-5-architecture-patterns/09-multi-tenancy.md) | Designing SaaS platforms that host many tenants on shared infrastructure: isolation levels, noisy-neighbor defenses, per-tenant metering, and when to graduate a whale. |
| 5.10 | [CRDT Applications (Yjs, Automerge, Local-First Software)](content/hld/part-5-architecture-patterns/10-crdt-applications.md) | Design local-first collaborative software with CRDTs: Yjs, Automerge, peer-to-peer sync, and the architectural shift away from authoritative central servers. |

</details>

<details>
<summary><a id="hld-part-6"></a><strong>Part 6 · Reliability & Operations</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone on-call, anyone who signs SLAs, anyone paying a cloud bill.

The engineering that separates "it compiles" from "it runs reliably at 3 a.m. on a long weekend": observability, SLOs, resilience patterns, auto-scaling, deployments, chaos engineering, incident response, health checks, FinOps, platform engineering.

| # | Chapter | What it covers |
|:-:|---|---|
| 6.0 | [Observability: Metrics, Logs, Traces, and the OpenTelemetry Standard](content/hld/part-6-reliability-and-operations/00-observability.md) | The three pillars of observability, USE vs RED methods, and how OpenTelemetry, Prometheus, Grafana, and Jaeger fit together in production. |
| 6.1 | [SLI, SLO, SLA, and Error Budgets: Making Reliability Quantitative](content/hld/part-6-reliability-and-operations/01-sli-slo-sla-error-budgets.md) | The Google SRE framework for reliability: what to measure, what to target, what to promise, and how error budgets fund feature work vs reliability work. |
| 6.2 | [Resilience Patterns: Timeouts, Retries, Circuit Breakers, and Bulkheads](content/hld/part-6-reliability-and-operations/02-resilience-patterns.md) | The defensive patterns that keep distributed systems from cascading into total failure, from Hystrix to modern service mesh implementations. |
| 6.3 | [Graceful Degradation: When Partial Service Beats No Service](content/hld/part-6-reliability-and-operations/03-graceful-degradation.md) | Load shedding, feature flags, cached fallbacks, and the product-engineering decisions behind degrading one feature to save the system. |
| 6.4 | [Auto-Scaling and Capacity Planning: From HPA to Predictive Scaling](content/hld/part-6-reliability-and-operations/04-auto-scaling-capacity.md) | Horizontal pod autoscalers, cluster autoscalers, predictive scaling, and the capacity planning math that keeps systems sized right without overspending. |
| 6.5 | [Deployment Strategies: Blue-Green, Canary, Rolling, and Feature Flags](content/hld/part-6-reliability-and-operations/05-deployment-strategies.md) | How to ship changes safely with blue-green, rolling, canary, and progressive delivery, plus the role of feature flags and LaunchDarkly-style tooling. |
| 6.6 | [Chaos Engineering: Breaking Things on Purpose](content/hld/part-6-reliability-and-operations/06-chaos-engineering.md) | Netflix's Chaos Monkey, the Principles of Chaos, and how to run game days and fault injection experiments without making your on-call call in sick. |
| 6.7 | [Incident Management: From Detection to Blameless Postmortem](content/hld/part-6-reliability-and-operations/07-incident-management.md) | On-call, incident command, severity levels, communication, and how to run postmortems that actually change systems instead of blaming people. |
| 6.8 | [Health Checks and Readiness: Telling the Truth About Whether You're Up](content/hld/part-6-reliability-and-operations/08-health-checks-readiness.md) | Liveness, readiness, startup probes, deep vs shallow health checks, and why bad health checks cause more outages than bad code. |
| 6.9 | [Cost Optimization and FinOps](content/hld/part-6-reliability-and-operations/09-cost-optimization-finops.md) | Apply FinOps to reduce cloud bills without sacrificing reliability: spot instances, reserved capacity, autoscaling, storage tiering, and unit-economics thinking. |
| 6.10 | [Platform Engineering: IDPs, Golden Paths, and DX](content/hld/part-6-reliability-and-operations/10-platform-engineering.md) | Treat the platform as a product: build internal developer platforms with Backstage, golden paths, and DORA/SPACE metrics that move developer productivity. |

</details>

<details>
<summary><a id="hld-part-7"></a><strong>Part 7 · Security at Scale</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Senior/Staff engineers, platform teams, security-adjacent builders.

Security architecture for real systems, not a CISSP crib sheet: AuthN vs AuthZ, OAuth2/OIDC, JWT (and why you probably shouldn't), mTLS, secrets management, DDoS/WAF, compliance (GDPR/DPDP/CCPA), software supply chain, privacy-preserving systems, post-quantum cryptography.

| # | Chapter | What it covers |
|:-:|---|---|
| 7.0 | [Authentication vs Authorization: Identity, Permissions, and Access Models](content/hld/part-7-security-at-scale/00-authn-authz.md) | AuthN vs AuthZ, session vs token auth, and access control models: RBAC, ABAC, ReBAC with examples from SpiceDB, OpenFGA, and AWS IAM. |
| 7.1 | [OAuth 2.0 and OpenID Connect: Delegated Authorization and Identity Done Right](content/hld/part-7-security-at-scale/01-oauth2-oidc.md) | The OAuth 2.0 authorization framework, OIDC identity layer, and the Authorization Code + PKCE flow that is the modern standard for web and mobile. |
| 7.2 | [JWT Deep Dive: Signed Tokens, Claims, and the Revocation Problem](content/hld/part-7-security-at-scale/02-jwt-deep-dive.md) | How JSON Web Tokens work: JWS signing, JWE encryption, claim validation, key rotation, and the trade-offs of stateless auth. |
| 7.3 | [mTLS and Service-to-Service Authentication: SPIFFE, Service Mesh, and Zero Trust](content/hld/part-7-security-at-scale/03-mtls-service-auth.md) | How mutual TLS, SPIFFE/SPIRE, and service meshes like Istio and Linkerd authenticate services without long-lived credentials. |
| 7.4 | [Secrets Management: Vault, KMS, and the End of Secrets in Config Files](content/hld/part-7-security-at-scale/04-secrets-management.md) | Managing API keys, passwords, and certificates with Vault, AWS Secrets Manager, KMS envelope encryption, and dynamic secrets. |
| 7.5 | [DDoS Protection and WAFs: Mitigating Volumetric and Application Attacks](content/hld/part-7-security-at-scale/05-ddos-waf.md) | Defending against L3/L4 and L7 DDoS with Cloudflare, AWS Shield, and WAFs; rate limiting, bot management, and the OWASP Top 10. |
| 7.6 | [Data Residency and Compliance Architecture (GDPR, DPDP, CCPA, Right-to-Erasure)](content/hld/part-7-security-at-scale/06-data-residency-compliance.md) | Designing multi-jurisdictional systems for GDPR, DPDP, CCPA, and LGPD with data classification, regional silos, crypto-shredding, and auditable erasure. |
| 7.7 | [Supply Chain Security: SBOM, SLSA, Sigstore, and Defending Against xz-utils](content/hld/part-7-security-at-scale/07-supply-chain-security.md) | Protecting the software supply chain with SBOMs, SLSA provenance, Sigstore signing, admission policies, and lessons from xz-utils and SolarWinds. |
| 7.8 | [Privacy-Preserving Systems (Differential Privacy, Federated Learning)](content/hld/part-7-security-at-scale/08-privacy-preserving-systems.md) | Design systems that protect user data by construction: differential privacy, federated learning, secure aggregation, and an introduction to homomorphic encryption. |
| 7.9 | [Post-Quantum Cryptography: Migrating to ML-KEM, ML-DSA, and a Crypto-Agile Future](content/hld/part-7-security-at-scale/09-post-quantum-crypto.md) | Why harvest-now-decrypt-later makes PQC urgent, what NIST standardized in 2024, and how to migrate production TLS and long-lived secrets to hybrid post-quantum cryptography. |

</details>

<details>
<summary><a id="hld-part-8"></a><strong>Part 8 · Case Studies</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Interview prep candidates, engineers building adjacent systems, anyone who learns best from worked examples.

End-to-end system designs, each following a consistent structure: requirements (functional + non-functional), back-of-envelope numbers, high-level architecture, data model, deep-dive components, scalability and reliability considerations, and real-world references. Grouped thematically below for easier navigation.

#### Core primitives

The interview classics. One building block per chapter, designed from scratch.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.0 | [Design a URL Shortener (TinyURL / bit.ly)](content/hld/part-8-case-studies/00-url-shortener.md) | Capacity estimation, short-code generation, hot-key caching, and an analytics pipeline that never blocks the redirect. |
| 8.1 | [Design a Pastebin (Paste Sharing Service)](content/hld/part-8-case-studies/01-pastebin.md) | Object storage split, TTL-based expiration pipelines, syntax highlighting placement, and abuse prevention. |
| 8.2 | [Design a Distributed Rate Limiter](content/hld/part-8-case-studies/02-rate-limiter.md) | Algorithm choice, Redis Lua atomicity, two-tier local+global synchronization, and fail-open failure modes. |
| 8.3 | [Design a Distributed Key-Value Store (Dynamo / Cassandra / Riak)](content/hld/part-8-case-studies/03-key-value-store.md) | Design a distributed KV store with consistent hashing, quorum replication, gossip membership, hinted handoff, and Merkle-tree anti-entropy repair. |
| 8.4 | [Design a Notification System (Push, SMS, Email at Scale)](content/hld/part-8-case-studies/04-notification-system.md) | Fan-out architecture, APNs/FCM integration, retry with dead-letter queues, and device-token lifecycle. |
| 8.5 | [Design a Chat System (WhatsApp / Messenger / Signal)](content/hld/part-8-case-studies/05-chat-system.md) | Staff-level design for 1:1 and small-group chat at WhatsApp scale: 500M concurrent connections, message ordering, E2E encryption, and storage model trade-offs. |
| 8.6 | [Design a Social Media Feed (Twitter / Instagram / LinkedIn)](content/hld/part-8-case-studies/06-social-media-feed.md) | Fan-out architecture, hybrid push/pull, ML ranking pipelines, and the celebrity problem at Twitter/X scale. |
| 8.7 | [Design a Photo Sharing Service (Instagram)](content/hld/part-8-case-studies/07-photo-sharing.md) | Design Instagram-scale photo sharing: upload pipeline, transcoding, multi-resolution image serving, CDN with origin shielding, and news feed integration. |
| 8.8 | [Design a Web Crawler (Googlebot-style)](content/hld/part-8-case-studies/08-web-crawler.md) | Design a distributed web crawler with URL frontier, politeness policies, content deduplication, robots.txt compliance, and Bloom-filter-backed URL dedup at billion scale. |
| 8.9 | [Design Search Autocomplete (Typeahead Suggestions)](content/hld/part-8-case-studies/09-search-autocomplete.md) | Design a low-latency autocomplete system with tries, top-K precomputation, real-time trending overlays, and multi-tier caching at Google scale. |
| 8.16 | [Design a Distributed Cache (Memcached / Redis Cluster)](content/hld/part-8-case-studies/16-distributed-cache.md) | Design a Memcached- or Redis-style distributed cache: consistent hashing, eviction, replication, client-side sharding, and hot-key mitigation. |
| 8.25 | [Design a Proximity Service (Nearby Friends / Yelp)](content/hld/part-8-case-studies/25-proximity-service.md) | Design a proximity service for 100M users with 1M concurrent location-sharing sessions: geohash/H3/S2 trade-offs, Redis geosets, bounding-box query fan-out, privacy, and hotspot handling during events. |
| 8.26 | [Design a Real-Time Leaderboard](content/hld/part-8-case-studies/26-leaderboard.md) | Design a real-time leaderboard for 10M players with 100K score updates/sec, tie-breaking, time-windowed views, friend boards, and approximate rank for the tail. |
| 8.27 | [Design a Unique ID Generator (Snowflake, ULID, TSID, UUIDv7)](content/hld/part-8-case-studies/27-unique-id-generator.md) | Design a distributed ID generator producing 10M 64-bit IDs/sec, monotonic-ish ordering, clock-skew resilience, and the four-way trade-off between Snowflake, ULID, TSID, and UUIDv7. |
| 8.29 | [Design a Distributed Job Scheduler (Airflow / Temporal / Distributed Cron)](content/hld/part-8-case-studies/29-job-scheduler.md) | Design a scheduler for 100k registered jobs and 10k executions/sec with exactly-once execution, DAGs up to 10k nodes, late/missed run policies, and graceful scheduler upgrades. |

#### Consumer products

End-user products built from several building blocks.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.10 | [Design a Video Streaming Service (YouTube / Twitch / TikTok)](content/hld/part-8-case-studies/10-video-streaming.md) | Design a UGC video platform from upload through adaptive bitrate streaming: transcode pipeline, HLS/DASH/CMAF packaging, CDN delivery with ISP peering, and live ingest architecture. |
| 8.11 | [Design Netflix (End-to-End)](content/hld/part-8-case-studies/11-netflix.md) | A whole-system walkthrough of Netflix's architecture: microservices, Open Connect CDN, per-title encoding, Cassandra + EVCache, resilience patterns, and chaos engineering. |
| 8.12 | [Design a Ride-Hailing Service (Uber / Lyft)](content/hld/part-8-case-studies/12-ride-hailing.md) | H3 geospatial indexing, real-time location ingest, batched bipartite matching, surge pricing, and trip orchestration. |
| 8.13 | [Design Google Maps (Routing and Tile Rendering)](content/hld/part-8-case-studies/13-google-maps.md) | Design planet-scale mapping: map tile rendering, shortest-path routing with contraction hierarchies, ETA prediction with GNNs, and offline maps. |
| 8.14 | [Design a File Sync Service (Dropbox / Google Drive)](content/hld/part-8-case-studies/14-file-sync.md) | Design a Dropbox-style file sync service: block-level deduplication, delta sync, conflict resolution, versioning, and client-server reconciliation. |
| 8.15 | [Design Collaborative Editing (Google Docs / Figma / Notion)](content/hld/part-8-case-studies/15-collaborative-editing.md) | Staff-level design for real-time collaborative editing at 100K+ concurrent editors: OT vs CRDTs, presence broadcasting, offline sync, and version history. |
| 8.18 | [Design a Ticketing System (BookMyShow / Ticketmaster)](content/hld/part-8-case-studies/18-ticketing-system.md) | Seat locking with Redis SETNX, saga-based payment, virtual waiting rooms, and anti-bot defenses at 500M tickets/year scale. |
| 8.21 | [Design a Food Delivery Service (DoorDash / Swiggy)](content/hld/part-8-case-studies/21-food-delivery.md) | Design a three-sided food delivery marketplace: dispatch with batching and reassignment, composite ETA prediction, and driver-merchant-customer coordination. |
| 8.28 | [Design a Hotel Reservation System (Booking.com / Airbnb)](content/hld/part-8-case-studies/28-hotel-reservation.md) | Staff-level design for hotel reservation: search/booking split, PostgreSQL exclusion constraints for date-range double-booking prevention, Temporal saga orchestration, and CDC-backed availability indexing at 85K QPS. |
| 8.40 | [Design a Dating App (Tinder / Hinge / Bumble)](content/hld/part-8-case-studies/40-dating-app.md) | Design a dating app for 100M MAU handling 1.5B swipes/day with <50 ms card loads: two-tower recommendations, geospatial filtering, mutual-match detection, and safety-at-scale. |
| 8.43 | [Design a Video Conferencing System (Zoom / Google Meet)](content/hld/part-8-case-studies/43-video-conferencing.md) | Design a video conferencing platform for 500K simultaneous meetings and 10M concurrent participants with <150 ms audio and <500 ms video: SFU vs MCU vs P2P, simulcast and SVC, bandwidth estimation, regional media routing, and real-time recording. |
| 8.44 | [Design an Email Service at Gmail Scale (1.8B Users, 300B Messages/Day)](content/hld/part-8-case-studies/44-gmail-scale-email.md) | Design a global email service for 1.8B users and 300B messages/day: SMTP ingress, spam pipeline cascade, per-user sharded search, RFC 5322 threading, and exabyte-scale tiered storage with content-addressed attachment dedup. |
| 8.45 | [Design Live Comments at Scale (FB Live / YouTube Live / Twitch Chat)](content/hld/part-8-case-studies/45-live-comments.md) | Design a live-comment system for 10M concurrent viewers and 100K commenters on one stream: delta-batched fan-out, pre-publish moderation, and the celebrity-stream hotspot. |
| 8.47 | [Design a Fitness Tracking Service (Strava / MapMyRun)](content/hld/part-8-case-studies/47-strava-fitness.md) | Design a fitness tracking service for 195M+ users: GPS ingestion, two-stage segment matching with H3 pre-filter and DTW, Kafka-backed leaderboards, and privacy-safe planetary heatmaps. |

#### Financial systems

Systems where correctness, audit and regulation come first.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.19 | [Design a Payment System (Stripe / PayPal)](content/hld/part-8-case-studies/19-payment-system.md) | Design a payment system with a double-entry ledger, idempotency keys, saga-orchestrated cross-service flows, and the compliance constraints that shape every decision. |
| 8.20 | [Design a Stock Exchange (Matching Engine)](content/hld/part-8-case-studies/20-stock-exchange.md) | Design a deterministic, low-latency matching engine: FIFO order book, price-time priority, multicast market data distribution, and co-location realities. |
| 8.41 | [Design an Online Auction (eBay / Catawiki)](content/hld/part-8-case-studies/41-online-auction.md) | Design an online auction for 100M active listings and 10M concurrent bidders: Redis Lua CAS for atomic bids at 1M/sec peak, proxy bidding, sniping extensions, and WebSocket fan-out. |
| 8.46 | [Design a Fraud Detection System (Stripe Radar / PayPal / Feedzai)](content/hld/part-8-case-studies/46-fraud-detection.md) | Design a real-time fraud detection service scoring millions of events per second under 100 ms p99 with a rules-ML cascade, online/offline feature store, graph ring detection, and analyst feedback loop. |
| 8.54 | [Design a Brokerage Platform (Robinhood / E*TRADE / Interactive Brokers)](content/hld/part-8-case-studies/54-brokerage-trading.md) | Design a retail brokerage for 30M users: order routing, symbol-channel quote fanout, fractional-share aggregation, tax-lot accounting, and seven-year regulatory audit. |

#### AI systems

Systems where inference, retrieval or agent behavior is the hard part.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.17 | [Design a Recommendation System (Netflix / YouTube / TikTok)](content/hld/part-8-case-studies/17-recommendation-system.md) | Design a two-stage recommendation system: candidate generation, ranking, collaborative filtering, content-based features, a feature store, and cold-start handling. |
| 8.30 | [Design ChatGPT (Conversational AI at Scale)](content/hld/part-8-case-studies/30-chatgpt-conversational-ai.md) | Design ChatGPT for 900M weekly users: multi-tenant LLM serving, session-state architecture, streaming SSE, per-user memory, safety, and multi-region deployment. |
| 8.31 | [Design an Enterprise RAG System](content/hld/part-8-case-studies/31-enterprise-rag.md) | Design a multi-tenant enterprise RAG platform for 1k tenants with 10M documents each at 100 QPS/tenant: ingestion, hybrid retrieval, reranking, citation, access-control-aware retrieval, freshness, and tenant isolation. |
| 8.32 | [Design a Coding Agent (Claude Code / GitHub Copilot / Cursor)](content/hld/part-8-case-studies/32-coding-agent.md) | Design a coding agent serving 1M concurrent sessions across autocomplete, chat, and autonomous loop modes with repo indexing, sandboxed tool use, and streaming diff application. |
| 8.33 | [Design Perplexity (AI Search with Citations)](content/hld/part-8-case-studies/33-perplexity-ai-search.md) | Design an AI search engine for 50M MAU, 5k QPS peak, <2 s answer latency with inline citations: query rewriting, source retrieval, citation-grounding, streaming output, freshness, and fact-check post-processing. |
| 8.34 | [Design a Voice Agent (Alexa / Siri-Class Realtime)](content/hld/part-8-case-studies/34-voice-agent.md) | Design a realtime voice agent for 100M devices with 50k concurrent conversations and sub-700 ms turn latency: streaming ASR, LLM turn-taking, streaming TTS, WebRTC transport, and barge-in. |
| 8.35 | [Design a Content Moderation System at Scale](content/hld/part-8-case-studies/35-content-moderation-at-scale.md) | Design moderation for 500M posts/day with <200 ms pre-publish latency, human-in-loop for 0.5% of traffic, multi-modal (text+image+video): classifier cascade, reviewer workflow, appeals, adversarial robustness. |
| 8.36 | [Design a Semantic Cache for LLM Applications](content/hld/part-8-case-studies/36-semantic-cache.md) | Design an embedding-similarity cache for LLM prompts at 10k QPS, 70%+ hit rate, <10 ms lookup: similarity threshold calibration, invalidation on source change, per-tenant isolation, false-positive cost accounting. |
| 8.37 | [Design a Model Router and Gateway (OpenRouter / LiteLLM)](content/hld/part-8-case-studies/37-model-router-gateway.md) | Design a gateway routing 20k QPS across 50+ models and 10 providers with <30 ms routing overhead: cost/latency/quality routing strategies, provider failover, streaming pass-through, per-tenant quotas, cost attribution. |

#### Infrastructure platforms

Platforms other engineers build on.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.22 | [Design a Metrics Pipeline (Prometheus / InfluxDB / Thanos)](content/hld/part-8-case-studies/22-metrics-pipeline.md) | Design a time-series metrics pipeline: high-cardinality ingestion, aggregation across clusters with Thanos or Cortex, alerting, and downsampling for long-term retention. |
| 8.23 | [Design Ad-Click Aggregation (Real-Time Stream Processing)](content/hld/part-8-case-studies/23-ad-click-aggregation.md) | Design an ad-click aggregation system with exactly-once semantics on Kafka + Flink, real-time fraud detection, and low-latency dashboards. |
| 8.24 | [Design a Logging Platform (ELK / Loki / Splunk)](content/hld/part-8-case-studies/24-logging-platform.md) | Design a logging platform: ingestion at scale, index vs. label-based storage (Elastic vs Loki), retention tiering, and full-text search with BM25. |
| 8.38 | [Design a Feature Flag Service (LaunchDarkly / Harness FME / Unleash)](content/hld/part-8-case-studies/38-feature-flag-service.md) | Design a feature flag and experimentation platform for 20T evaluations/day with sub-millisecond SDK-side latency, streaming config distribution, and sub-60s kill-switch propagation. |
| 8.39 | [Design a DNS Service (Cloudflare 1.1.1.1 / Google 8.8.8.8)](content/hld/part-8-case-studies/39-dns-service.md) | Design a public recursive DNS resolver serving trillions of queries/day globally with <20 ms p99 from 300+ anycast POPs: UDP/TCP/DoT/DoH/DoQ, DNSSEC validation, cache design, rate limiting, and DDoS survivability. |
| 8.42 | [Design a Multi-Tenant SaaS Platform](content/hld/part-8-case-studies/42-multi-tenant-saas.md) | Design a multi-tenant SaaS platform serving 50K tenants with per-tenant SLA tiers, metered billing, noisy-neighbor containment, and zero cross-tenant data leakage. |
| 8.48 | [Design an Online Judge (LeetCode / Codeforces / HackerEarth)](content/hld/part-8-case-studies/48-online-judge.md) | Design an online judge for 1M users at 100K submissions/hour peak with <15s verdict p99: Firecracker sandboxes, priority queueing for contests, seccomp + cgroups isolation, and MOSS-style plagiarism detection. |
| 8.49 | [Design a Price Tracking Service (CamelCamelCamel / Honey / Keepa)](content/hld/part-8-case-studies/49-price-tracking.md) | Design a price-tracking service that watches 100M product URLs with priority-driven scraping, diff-based alerting to 10M subscribers, 2-year historical retention, and polite rotation through a proxy pool that retailers actively try to block. |
| 8.50 | [Design an API Gateway at Scale (Kong / AWS API Gateway / Apigee / Envoy)](content/hld/part-8-case-studies/50-api-gateway.md) | Design an API gateway that handles 100K RPS per instance with <5 ms p99 overhead across 10K upstream services: routing trie, local+global rate limiting, mTLS termination, hitless config reload, and circuit breaking. |
| 8.51 | [Design a CI/CD Platform (GitHub Actions / GitLab CI / CircleCI)](content/hld/part-8-case-studies/51-cicd-platform.md) | Design a CI/CD platform for 100K orgs and 10M workflow runs/day: YAML DAG execution, ephemeral runner pools (Firecracker), content-addressed artifacts, dependency caches, secrets injection, and multi-tenant isolation at 40K concurrent runners. |
| 8.52 | [Design an Observability Platform (Datadog / New Relic / Honeycomb)](content/hld/part-8-case-studies/52-observability-platform.md) | Design a unified observability platform for 10M hosts and 1B events/sec: OTLP ingestion across metrics, logs, and traces, cardinality control, trace-log correlation, multi-tenant isolation, and query latency at 100K concurrent analysts. |
| 8.53 | [Design a Search Engine (Google-Scale / Brave Search)](content/hld/part-8-case-studies/53-search-engine.md) | Design a web-scale search engine over 10B documents serving 100K queries/sec at <200 ms p99: sharded inverted index, BM25 + PageRank + neural re-ranking cascade, query understanding, and freshness pipelines. |
| 8.55 | [Design Channel-Scale Chat (Discord / Slack)](content/hld/part-8-case-studies/55-channel-scale-chat.md) | Design channel-scale chat for 100K+ member channels with pub/sub fanout, RBAC on the hot path, presence aggregation, and workspace search. |

</details>

<details>
<summary><a id="hld-part-9"></a><strong>Part 9 · AI & ML System Design</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone building with or around LLMs, agents, or production ML.

Modern AI-systems architecture, treated with the same rigor as Part 3: LLM serving, RAG, vector search, agent architectures, multi-agent orchestration, LLM evaluation, LLMOps, cost optimization, safety, ML fundamentals, feature stores, recommenders, real-time AI, multimodal, and the data infra underneath all of it.

| # | Chapter | What it covers |
|:-:|---|---|
| 9.0 | [LLM Serving Architecture (vLLM, TGI, TensorRT-LLM)](content/hld/part-9-ai-ml-system-design/00-llm-serving-architecture.md) | Design a production LLM inference stack: continuous batching, paged attention, KV-cache management, and multi-tenant GPU scheduling. |
| 9.1 | [RAG Pipelines (Retrieval-Augmented Generation)](content/hld/part-9-ai-ml-system-design/01-rag-pipelines.md) | Design production RAG: chunking, embedding models, hybrid dense-plus-sparse retrieval, reranking, and the eval loops that keep it honest. |
| 9.2 | [Vector Search at Scale (HNSW, IVF-PQ, DiskANN)](content/hld/part-9-ai-ml-system-design/02-vector-search-at-scale.md) | Design billion-scale vector search: HNSW, IVF-PQ, and DiskANN indexes, product quantization, hybrid BM25-vector search, and sharding strategies. |
| 9.3 | [AI Agent Architectures (ReAct, Reflection, Planning, Tool Use, Memory)](content/hld/part-9-ai-ml-system-design/03-ai-agent-architectures.md) | The canonical patterns for turning an LLM into an agent: ReAct's think-act-observe loop, reflection and self-critique, planner-executor decomposition, tool use and function calling, and how agents manage short- and long-term memory. |
| 9.4 | [Multi-Agent Orchestration (LangGraph, OpenAI Agents SDK, AutoGen, Swarm)](content/hld/part-9-ai-ml-system-design/04-multi-agent-orchestration.md) | Composing multiple agents into a reliable system: orchestrator-worker topologies, handoffs and delegation, shared memory, parallel fan-out, and the failure modes of agent graphs. |
| 9.5 | [LLM Evaluation and Observability (Ragas, LangSmith, TruLens, LLM-as-Judge)](content/hld/part-9-ai-ml-system-design/05-llm-evaluation-observability.md) | How to evaluate LLM systems before and after they ship: golden datasets, reference-free metrics, LLM-as-judge, continuous eval pipelines, and the observability stack for production LLMs. |
| 9.6 | [LLMOps and Prompt Engineering (Versioning, Guardrails, Red-Teaming)](content/hld/part-9-ai-ml-system-design/06-llmops-prompt-engineering.md) | The operational side of shipping LLM features: prompt-as-code, versioning, rollback, A/B testing prompts, structured outputs, and red-teaming before launch. |
| 9.7 | [LLM Cost Optimisation (Semantic Cache, Model Routing, Cascading, Prompt Caching)](content/hld/part-9-ai-ml-system-design/07-llm-cost-optimization.md) | The cost-engineering toolbox for production LLMs: semantic caching, model routing, cascade small-then-big, prompt caching (Anthropic, OpenAI), and the unit economics that decide per-request margin. |
| 9.8 | [LLM Safety and Guardrails (OWASP LLM Top 10, Prompt Injection, PII, Jailbreaks)](content/hld/part-9-ai-ml-system-design/08-llm-safety-guardrails.md) | The safety-engineering surface for LLM applications: OWASP LLM Top 10, prompt-injection defence, PII redaction, jailbreak containment, and the defence-in-depth model for public-facing agents. |
| 9.9 | [ML System Design Fundamentals](content/hld/part-9-ai-ml-system-design/09-ml-system-design-fundamentals.md) | The classic ML systems backbone every modern AI product sits on: candidate generation, ranking, two-tower embeddings, offline/online feature parity, and the training-serving skew problem. |
| 9.10 | [Feature Stores and Model Serving (Feast, Tecton, KServe, BentoML, MLflow)](content/hld/part-9-ai-ml-system-design/10-feature-stores-model-serving.md) | The infrastructure that makes ML shippable: online and offline feature stores, the model registry, model servers, shadow deploys, and the production lifecycle around a trained model. |
| 9.11 | [Recommendation Systems Deep Dive (DLRM, Two-Tower, Embedding Retrieval, Cold Start)](content/hld/part-9-ai-ml-system-design/11-recommendation-systems.md) | How modern recommenders actually work end-to-end: candidate gen via ANN on embeddings, DLRM-style ranking, exploration-exploitation, cold-start handling, and the evaluation loop that keeps metrics honest. |
| 9.12 | [Realtime AI and Voice Agents (Streaming Inference, WebRTC, LiveKit, Deepgram)](content/hld/part-9-ai-ml-system-design/12-realtime-ai-voice-agents.md) | Designing sub-second voice agents: streaming ASR, low-latency LLM inference, streaming TTS, WebRTC transport, interruption handling, and the end-to-end latency budget. |
| 9.13 | [Multimodal AI Systems (CLIP, Whisper, LayoutLM, Document AI)](content/hld/part-9-ai-ml-system-design/13-multimodal-ai-systems.md) | Designing systems that ingest images, audio, video, and documents: CLIP-style embeddings for cross-modal retrieval, Whisper pipelines, OCR-plus-layout models, and the storage architecture for unstructured data. |
| 9.14 | [Data Infrastructure for AI (Embedding Pipelines, Chunking, Unstructured ETL, MCP)](content/hld/part-9-ai-ml-system-design/14-data-infrastructure-for-ai.md) | The data plane that feeds AI systems: source connectors, chunking strategies, embedding at scale, metadata schema, freshness, and the Model Context Protocol as a standard interface. |

</details>

<details>
<summary><a id="hld-part-10"></a><strong>Part 10 · Emerging Patterns</strong></summary>

**Level:** Intermediate &nbsp;·&nbsp; **For:** Staff+ engineers and architects thinking past 2026.

Forward-looking topics that sit next to everything else in the book.

| # | Chapter | What it covers |
|:-:|---|---|
| 10.0 | [Green Computing (Carbon-Aware Scheduling, PUE, Sustainable Systems)](content/hld/part-10-emerging-patterns/00-green-computing.md) | Design systems that account for carbon: carbon-aware scheduling, PUE, renewable-energy datacenters, and the Green Software Foundation practices. |

</details>

<details>
<summary><a id="hld-part-11"></a><strong>Part 11 · Interview Framework</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone preparing for or giving system-design interviews.

How to run a 45-minute system-design interview, from both sides of the whiteboard. Compares RESHADED / PEDALS / ADEPT frameworks, teaches requirements scoping, diagramming, trade-off articulation, company-specific flavors, and RFC/design-doc authoring for Staff-level work.

| # | Chapter | What it covers |
|:-:|---|---|
| 11.0 | [Interview Frameworks Compared (RESHADED, PEDALS, ADEPT)](content/hld/part-11-interview-framework/00-frameworks-compared.md) | Compare the major system-design interview frameworks and pick the one you will use in every interview. |
| 11.1 | [Requirements Scoping: Functional, Non-Functional, and MoSCoW](content/hld/part-11-interview-framework/01-requirements-scoping.md) | Master the first five minutes of a system design interview: functional vs non-functional requirements, MoSCoW prioritization, and time-boxing the scope. |
| 11.2 | [Diagramming Skills for System Design Interviews](content/hld/part-11-interview-framework/02-diagramming-skills.md) | Build whiteboard and virtual diagrams that interviewers can read: consistent notation, flow direction, and the tools (Excalidraw, Miro) that the industry prefers. |
| 11.3 | [Trade-off Articulation: Saying 'It Depends' Well](content/hld/part-11-interview-framework/03-trade-off-articulation.md) | Learn to verbalize design trade-offs the way senior engineers do: name the axis, state the dependency, and commit to a choice. |
| 11.4 | [Company-Specific Interview Flavors (Amazon, Google, Meta, Netflix)](content/hld/part-11-interview-framework/04-company-specific-flavors.md) | How the same system design question looks different at Amazon, Google, Meta, and Netflix: leadership principles, scale emphasis, product sense, and simplicity. |
| 11.5 | [Design Doc Authoring: RFCs, ADRs, and the Staff Engineer's Written Output](content/hld/part-11-interview-framework/05-design-doc-authoring.md) | How to write ADRs, design docs, and RFCs that drive alignment, record decisions, and demonstrate Staff+ engineering judgment. |

</details>

### Trade-offs Library

The design questions that come up again and again, each answered on a dedicated page with a decision flowchart, a comparison table, when to pick each side, real-world examples and citations. Chapters across the book link here.

<details>
<summary><strong>Every trade-off page</strong> &nbsp;—&nbsp; consistency, storage, APIs, real-time, scaling, transactions, deployment</summary>

| # | Trade-off | How to decide |
|:-:|---|---|
| 1 | [Strong vs Eventual Consistency](content/hld/trade-offs/01-strong-vs-eventual-consistency.md) | When to pick linearizable consistency, when eventual is enough, and the session-guarantees hybrid that most production systems actually run. |
| 2 | [ACID vs BASE](content/hld/trade-offs/02-acid-vs-base.md) | When ACID transactions earn their coordination cost, when BASE is the only thing that scales, and why most systems run both. |
| 3 | [SQL vs NoSQL](content/hld/trade-offs/03-sql-vs-nosql.md) | When relational wins, when non-relational wins, and why 'SQL does not scale' is almost always wrong in 2026. |
| 4 | [Latency vs Throughput](content/hld/trade-offs/04-latency-vs-throughput.md) | When to optimize for the single request, when to optimize for the aggregate, and why batching has a non-obvious ceiling. |
| 5 | [CAP and PACELC Applied](content/hld/trade-offs/05-cap-and-pacelc.md) | CP or AP under partition, and why PACELC's else-clause (latency vs consistency) is the choice you face on every request. |
| 6 | [Cache Strategies: Cache-Aside vs Write-Through vs Write-Behind](content/hld/trade-offs/06-cache-strategies.md) | The right cache-database coordination pattern: what you gain, what you lose, and why most systems use a hybrid. |
| 7 | [Batch vs Stream Processing](content/hld/trade-offs/07-batch-vs-stream.md) | Discrete job runs vs continuous flow, pinned to the freshness SLO that actually matters. |
| 8 | [Load Balancer vs Reverse Proxy vs API Gateway](content/hld/trade-offs/08-load-balancer-vs-proxy-vs-gateway.md) | Between L4 load balancers, L7 reverse proxies, and API gateways based on your traffic layer, protocol, and policy needs. |
| 9 | [REST vs gRPC vs GraphQL](content/hld/trade-offs/09-rest-vs-grpc-vs-graphql.md) | The right API protocol based on caller identity, caching needs, and payload shape. |
| 10 | [Polling vs Long-Polling vs SSE vs WebSockets vs Webhooks](content/hld/trade-offs/10-polling-vs-websockets.md) | The right real-time pattern. Five options, each right for a different niche; the wrong one means missed updates, wasted bandwidth, or operational pain. |
| 11 | [Rate Limiting Algorithms: Token Bucket vs Sliding Window](content/hld/trade-offs/11-rate-limiting-algorithms.md) | The right rate-limiting algorithm. Token bucket tolerates bursts; sliding window enforces accuracy; the hybrid path layers both. |
| 12 | [Optimistic vs Pessimistic Concurrency Control](content/hld/trade-offs/12-optimistic-vs-pessimistic-locking.md) | Validate-at-commit vs lock-first concurrency. The answer depends on conflict rate, retry cost, and side effects. |
| 13 | [Partitioning Schemes: Range, Hash, Consistent Hash, Directory](content/hld/trade-offs/13-partitioning-schemes.md) | Four canonical partitioning strategies. Pick based on query pattern, rebalance cost, and hot-spot risk. |
| 14 | [B-tree vs LSM-tree Storage](content/hld/trade-offs/14-btree-vs-lsm.md) | Between B-tree and LSM-tree storage engines based on read:write ratio, latency SLOs, and operational complexity. |
| 15 | [Monolith vs Microservices](content/hld/trade-offs/15-monolith-vs-microservices.md) | Architecture choice that mirrors your org chart. Team size and domain stability decide, not traffic. |
| 16 | [Replication Topologies: Leader-Follower, Multi-Leader, Leaderless](content/hld/trade-offs/16-replication-topologies.md) | How writes propagate: single-leader, multi-leader, leaderless, or per-range-leader hybrid. |
| 17 | [Distributed Transactions: 2PC vs Saga vs TCC](content/hld/trade-offs/17-distributed-transactions.md) | Between two-phase commit, saga compensations, and try-confirm-cancel based on isolation needs, transaction duration, and participant control. |
| 18 | [Push vs Pull (Fan-out, Messaging, Feed)](content/hld/trade-offs/18-push-vs-pull.md) | Fundamental data-propagation choice: push front-loads compute on writes, pull back-loads it on reads. The fan-out ratio decides. |
| 19 | [Lambda vs Kappa Architecture](content/hld/trade-offs/19-lambda-vs-kappa.md) | Two pipelines (batch + stream) vs one (stream-only with log replay) for analytics data systems. |
| 20 | [Vertical vs Horizontal Scaling](content/hld/trade-offs/20-vertical-vs-horizontal-scaling.md) | Scaling up a single machine vs scaling out across many. Default: vertical first, horizontal only when measured bottlenecks demand it. |
| 21 | [Normalization vs Denormalization](content/hld/trade-offs/21-normalization-vs-denormalization.md) | Between strict 3NF schemas and redundant pre-joined data, with the hybrid CDC-projection pattern most production systems actually run. |
| 22 | [Single-Region vs Multi-Region Deployment](content/hld/trade-offs/22-single-vs-multi-region.md) | Deployment geography: single-region is the default, multi-region is the most expensive choice you can make, and regional pinning is the hybrid most teams actually need. |

</details>

---

## The DSA Handbook

**Data structures and algorithms, taught pattern by pattern.**

[Website](https://dsa.handbook.academy) · [`content/dsa/`](content/dsa/) · [DSA style rules](STYLE_GUIDE.md#dsa-specific-deviations)

The DSA Handbook builds from Big-O and recursion through linear structures, searching and sorting, and the array-walking patterns, then trees, graphs, dynamic programming and the advanced string algorithms. It finishes with designing data structures to an API contract and with the interview itself: recognizing the pattern, asking the right questions, and narrating your solution.

**How a chapter is built.** Each chapter opens with a cheat-sheet table, explains the structure or pattern in depth, then works through LeetCode problems as prompt cards, each with a worked example, a solution walkthrough and the common mistakes. The Python solution is inline. Java, C++ and Go solutions sit next to the chapter in `lc-NNN/` folders (`sol.py`, `sol.java`, `sol.cpp`, `sol.go`), each with test cases.

### DSA parts at a glance

Pick a part number to jump to its chapters, or open any part below.

| Part | What it covers | Level |
|---|---|---|
| [0](#dsa-part-0) | **Foundations** — Big-O, recursion, bit ops, interview math, language idioms, choosing your language | Beginner |
| [1](#dsa-part-1) | **Linear Data Structures** — arrays, dynamic-array internals, strings, hash maps, stacks, queues, matrices | Beginner to advanced |
| [2](#dsa-part-2) | **Search & Sort** — linear/binary search, comparison & linear-time sorts, heap sort, quickselect | Beginner to intermediate |
| [3](#dsa-part-3) | **Two Pointers, Sliding Window, Prefix Sums** — the array-walking patterns that turn O(n²) into O(n) | Beginner to intermediate |
| [4](#dsa-part-4) | **Stack & Queue Patterns** — monotonic stack/deque, min/max stack, expression parsing, queue-from-stacks | Intermediate |
| [5](#dsa-part-5) | **Linked Lists** — pointer rewiring, reversal, k-group reversal, Floyd's cycle, merging, LRU cache | Beginner to intermediate |
| [6](#dsa-part-6) | **Trees & Heaps** — traversals, Morris, BFS, heaps, BST, AVL/RB, tries, tree DP, segment trees | Beginner to advanced |
| [7](#dsa-part-7) | **Recursion & Backtracking** — recursion patterns, the template, subsets/perms, N-Queens, Sudoku, randomized algos | Intermediate to advanced |
| [8](#dsa-part-8) | **Graphs** — BFS/DFS, components, topo, cycles, bipartite, union-find, Dijkstra, Bellman-Ford, MSTs | Beginner to advanced |
| [9](#dsa-part-9) | **Dynamic Programming** — memo↔tab, 1D/grid/interval/tree/bitmask, knapsack, LCS, edit distance, LIS, palindromes | Intermediate to advanced |
| [10](#dsa-part-10) | **Greedy** — when local choices win, intervals, activity selection, Huffman, jump games | Intermediate |
| [11](#dsa-part-11) | **Bit Manipulation** — the bit-ops cookbook, XOR patterns, bitmask techniques, performance tricks | Intermediate to advanced |
| [12](#dsa-part-12) | **Strings & Pattern Matching** — naive matching, Rabin-Karp, KMP, Z-array, Aho-Corasick, suffix arrays | Intermediate to advanced |
| [13](#dsa-part-13) | **Design the Data Structure** — LRU/LFU, min stacks, hit counter, trie autocomplete, Twitter feed, game state | Intermediate to advanced |
| [14](#dsa-part-14) | **Interview Framework** — pattern recognition, clarifying questions, communicating, complexity, mocks, per-company tracks | Intermediate |

<details>
<summary><a id="dsa-part-0"></a><strong>Part 0 · Foundations</strong></summary>

**Level:** Beginner &nbsp;·&nbsp; **For:** Anyone starting interview prep, or returning after a long pause.

The mental models and language fluency that everything else assumes. Big-O, the recursion mental model, bit-manipulation primer, the math you actually need for interviews, language idioms across Python / Java / C++ / Go, and how to pick which language to interview in.

| # | Chapter | What it covers |
|:-:|---|---|
| 0.0 | [How to use this handbook](content/dsa/part-0-foundations/00-how-to-use.md) | How to read this handbook: who it's for, what to skip, how to pick a language, and the four questions every DSA resource ducks. |
| 0.1 | [Computational complexity and Big-O](content/dsa/part-0-foundations/01-complexity-big-o.md) | Computational complexity, Big-O, and the asymptotic vocabulary every algorithm chapter assumes you have. The five Bachmann-Landau notations. |
| 0.2 | [The recursion mental model](content/dsa/part-0-foundations/02-recursion-mental-model.md) | The mental model for recursion: base case, recursive case, and how to read tree-shaped recursion without losing your place. |
| 0.3 | [Bit manipulation primer](content/dsa/part-0-foundations/03-bit-manipulation-primer.md) | Bit manipulation primer: AND, OR, XOR, NOT, shifts, popcount. The bit-level idioms that show up in interview problems. |
| 0.4 | [Math for interviews](content/dsa/part-0-foundations/04-math-for-interviews.md) | The math you actually need for technical interviews: modular arithmetic, GCD, primality, combinatorics, integer overflow. |
| 0.5 | [Language idioms across Python, Java, C++, Go](content/dsa/part-0-foundations/05-language-idioms.md) | Idiomatic patterns for Python, Java, C++, and Go: collections, iteration, sorting, comparators. The dialect each language wants you to write. |
| 0.6 | [Choosing your interview language](content/dsa/part-0-foundations/06-choosing-your-language.md) | How to pick a language for technical interviews: trade-offs, what each language costs you in problem-solving time, and a decision tree. |

</details>

<details>
<summary><a id="dsa-part-1"></a><strong>Part 1 · Linear Data Structures</strong></summary>

**Level:** Beginner to advanced &nbsp;·&nbsp; **For:** Everyone. These structures show up in most interview problems.

The contiguous-memory and bucket-based data structures: arrays (static / dynamic / multi-dimensional), the amortized-O(1) doubling rule that makes a `vector` work, strings as encoded byte arrays, hash maps and hash sets, the load-factor / collision math behind them, stacks and queues with the call-stack analogy, and matrix manipulation tricks (rotate-in-place, spiral, transpose).

| # | Chapter | What it covers |
|:-:|---|---|
| 1.0 | [Arrays: static, dynamic, multi-dimensional](content/dsa/part-1-linear-data-structures/00-arrays.md) | Arrays: contiguous memory, O(1) indexing, and the operations that differ between fixed-size arrays and dynamic arrays. |
| 1.1 | [Dynamic array internals](content/dsa/part-1-linear-data-structures/01-dynamic-array-internals.md) | How dynamic arrays grow: amortised O(1) append, the doubling trick, capacity vs length, and what each language calls them. |
| 1.2 | [Strings: encoding, immutability, builders](content/dsa/part-1-linear-data-structures/02-strings.md) | Strings as character arrays and beyond: immutability, encoding, concatenation cost, and the per-language trade-offs that catch interviews out. |
| 1.3 | [Hash maps and hash sets](content/dsa/part-1-linear-data-structures/03-hash-maps.md) | Hash maps from first principles: hash functions, buckets, average vs worst-case complexity, and the standard library implementations. |
| 1.4 | [Hash collisions and the load factor](content/dsa/part-1-linear-data-structures/04-hash-collisions.md) | Hash collisions: separate chaining, open addressing, load factor, rehashing, and why hash maps degrade to O(n) under adversarial keys. |
| 1.5 | [Stacks and the call stack analogy](content/dsa/part-1-linear-data-structures/05-stacks.md) | Stacks as data structures and algorithmic primitives: LIFO, function-call stacks, and the interview problems that scream 'stack'. |
| 1.6 | [Queues, deques, and circular buffers](content/dsa/part-1-linear-data-structures/06-queues-deques.md) | Queues and deques: FIFO, double-ended, ring buffers, and the BFS / sliding-window problems where the right primitive is a deque. |
| 1.7 | [Matrix manipulation](content/dsa/part-1-linear-data-structures/07-matrix-manipulation.md) | 2D arrays and matrix manipulation: in-place rotation, transposition, spiral traversal, and indexing without off-by-one bugs. |

</details>

<details>
<summary><a id="dsa-part-2"></a><strong>Part 2 · Search & Sort</strong></summary>

**Level:** Beginner to intermediate &nbsp;·&nbsp; **For:** Every interviewee. Binary search alone shows up again and again.

How to find things and how to order things. Linear search and when it's actually the right answer; the canonical binary search written without off-by-one bugs; the lower_bound / upper_bound / peak / rotated-array variants; the comparison-sort family (insertion, merge, quicksort with the production hybrids like Timsort and Introsort); heap sort and why `n log n` is the comparison-sort lower bound; the linear-time sorts (counting, radix, bucket); and quickselect for the top-k problems.

| # | Chapter | What it covers |
|:-:|---|---|
| 2.0 | [Linear search and what it's good for](content/dsa/part-2-search-sort/00-linear-search.md) | Linear search: when O(n) is the right answer, and the problems where the trick is recognising you don't need anything cleverer. |
| 2.1 | [Binary search: the canonical version](content/dsa/part-2-search-sort/01-binary-search-canonical.md) | Binary search done right: the canonical template, off-by-one pitfalls, and the invariant you need to articulate before writing the loop. |
| 2.2 | [Binary search variants: lower_bound, upper_bound, peaks, and rotated arrays](content/dsa/part-2-search-sort/02-binary-search-variants.md) | Binary search beyond sorted arrays: lower_bound, upper_bound, first-true, last-true, and binary search on the answer space. |
| 2.3 | [Comparison sorts I: insertion sort and merge sort](content/dsa/part-2-search-sort/03-comparison-sorts-1.md) | Insertion, selection, and bubble sort: O(n^2) sorts, when each wins on real input, and the constant-factor lessons that hide inside them. |
| 2.4 | [Comparison sorts II: quicksort, partition, and the production hybrids](content/dsa/part-2-search-sort/04-comparison-sorts-2.md) | Merge sort and quicksort: divide-and-conquer, partitioning, stability, and why production library sorts are hybrid algorithms. |
| 2.5 | [Heap sort and the n log n lower bound](content/dsa/part-2-search-sort/05-heap-sort.md) | Heap sort and the binary heap: heapify, sift-up, sift-down, and why a heap is the right tool for k-way merges and priority queues. |
| 2.6 | [Linear-time sorts: counting, radix, bucket](content/dsa/part-2-search-sort/06-linear-sorts.md) | Counting sort, radix sort, bucket sort: O(n) sorts that beat the comparison-sort lower bound when the input has structure. |
| 2.7 | [Quickselect: linear-time selection](content/dsa/part-2-search-sort/07-quickselect.md) | Quickselect: O(n) average kth-smallest, partitioning, and the problems where you can dodge a full sort by selecting only the part you need. |

</details>

<details>
<summary><a id="dsa-part-3"></a><strong>Part 3 · Two Pointers, Sliding Window, Prefix Sums</strong></summary>

**Level:** Beginner to intermediate &nbsp;·&nbsp; **For:** Anyone whose nested-loop solutions keep timing out.

Three closely related patterns that all amount to "walk the array smarter": opposite-ends two pointers (Container With Most Water, 3Sum), same-direction two pointers, fixed and variable sliding windows, prefix sums and difference arrays, and the prefix-sum + hash-map combo for "subarray sum equals K"-shaped problems.

| # | Chapter | What it covers |
|:-:|---|---|
| 3.0 | [Two pointers: opposite ends](content/dsa/part-3-pointers-window-prefix/00-two-pointers-opposite.md) | Two pointers, opposite ends: the inward sweep, sorted-array invariants, and the canonical 'sum to target' / 'pair under constraint' patterns. |
| 3.1 | [Two pointers: same direction](content/dsa/part-3-pointers-window-prefix/01-two-pointers-same-direction.md) | Two pointers, same direction: fast-slow pointers, in-place filtering, and the array problems that disguise this pattern. |
| 3.2 | [Sliding window: fixed size](content/dsa/part-3-pointers-window-prefix/02-sliding-window-fixed.md) | Fixed-size sliding windows: maintaining a running aggregate in O(1) per step, and the problems whose constraint is window length. |
| 3.3 | [Sliding window: variable size](content/dsa/part-3-pointers-window-prefix/03-sliding-window-variable.md) | Variable-size sliding windows: shrinking when the invariant breaks, and the longest-substring / minimum-window problem family. |
| 3.4 | [Prefix sums and difference arrays](content/dsa/part-3-pointers-window-prefix/04-prefix-sums.md) | Prefix sums: O(1) range-sum queries, 2D extensions, and the subarray-sum problems that simplify once the right precomputation is in place. |
| 3.5 | [The prefix-sum + hash-map combo](content/dsa/part-3-pointers-window-prefix/05-prefix-sum-hash.md) | Prefix sum + hash map: counting subarrays with a target sum, the canonical 'subarray sum equals K' problem family, and modulo extensions. |

</details>

<details>
<summary><a id="dsa-part-4"></a><strong>Part 4 · Stack & Queue Patterns</strong></summary>

**Level:** Intermediate &nbsp;·&nbsp; **For:** Anyone struggling with Next-Greater-Element and sliding-window-maximum problems.

Stack and queue *as algorithmic patterns*, not just data structures. Monotonic stacks (Daily Temperatures, Largest Rectangle in Histogram), monotonic deques (Sliding Window Maximum), min/max stacks (O(1) min query under push/pop), expression parsing (Shunting-Yard / RPN), and the queue-from-stacks amortization argument.

| # | Chapter | What it covers |
|:-:|---|---|
| 4.0 | [Monotonic stack](content/dsa/part-4-stack-queue-patterns/00-monotonic-stack.md) | Push indices, pop while the incoming value violates a monotone order. The data structure designed for the intersection of nearest-greater queries and one-pass linear scans. |
| 4.1 | [Monotonic deque](content/dsa/part-4-stack-queue-patterns/01-monotonic-deque.md) | Pop from both ends to maintain a windowed running max or min in O(1) amortized per slide. The structure that makes sliding-window-extremum problems linear instead of n log k. |
| 4.2 | [Min and max stacks](content/dsa/part-4-stack-queue-patterns/02-min-max-stack.md) | Augment a stack with an O(1) aggregate query by pinning a parallel auxiliary stack to it; scale the technique from running min to lazy bulk-update to frequency tracking. |
| 4.3 | [Expression evaluation and parsing](content/dsa/part-4-stack-queue-patterns/03-expression-evaluation.md) | Stacks suspend operators until their right operand exists. The shunting-yard rhythm and the LeetCode 224/227/772 family where the order characters arrive in is not the order arithmetic should happen. |
| 4.4 | [Queue from stacks](content/dsa/part-4-stack-queue-patterns/04-queue-from-stacks.md) | Implement a queue using only stack primitives. The two-stack lazy-transfer trick, amortized O(1) on every operation, and why the LIFO-from-FIFO inverse has no symmetric construction. |

</details>

<details>
<summary><a id="dsa-part-5"></a><strong>Part 5 · Linked Lists</strong></summary>

**Level:** Beginner to intermediate &nbsp;·&nbsp; **For:** Anyone who's drawn boxes-and-arrows on a whiteboard and gotten lost.

Linked lists are pointer surgery. Sentinel-node patterns, the canonical iterative reversal (and the recursive cousin), reverse-in-groups-of-k, Floyd's tortoise-and-hare cycle detection (and why the cycle-start formula works), merging sorted lists, and the LRU cache as the canonical hash-map + doubly-linked-list combo.

| # | Chapter | What it covers |
|:-:|---|---|
| 5.0 | [Linked list fundamentals: sentinels, pointer rewiring, doubly-linked design](content/dsa/part-5-linked-lists/00-linked-list-fundamentals.md) | Sentinel and dummy nodes erase the boundary branching that special-cases head and tail. The pointer-rewiring discipline and the doubly-linked design every later chapter in Part 5 assumes. |
| 5.1 | [Reversal patterns](content/dsa/part-5-linked-lists/01-reversal-patterns.md) | Reverse a singly-linked list in place with prev, curr, next. The snapshot-then-clobber rule, plus the iterative and recursive forms that show up as a primitive in every later linked-list chapter. |
| 5.2 | [Reverse in groups of k](content/dsa/part-5-linked-lists/02-reverse-in-groups-k.md) | Three mechanical phases stacked on single-list reversal solve LeetCode 25 in O(1) extra memory, with the seam between groups handled cleanly. |
| 5.3 | [Cycle detection (Floyd's tortoise and hare)](content/dsa/part-5-linked-lists/03-cycle-detection.md) | Two pointers, one stepping twice as fast as the other, locate a cycle's entry node in O(n) time and O(1) space. The modular-arithmetic three-line proof of why the second-phase reset works. |
| 5.4 | [Merging linked lists](content/dsa/part-5-linked-lists/04-merging-linked-lists.md) | Merge sorted linked lists in place. The dummy-head trick that erases the first-node special case, two-list and k-list versions, and the heap-based and divide-and-conquer extensions to LC 23. |
| 5.5 | [LRU cache: hash map plus doubly linked list](content/dsa/part-5-linked-lists/05-lru-cache.md) | Build the data structure behind LeetCode 146 from a doubly-linked list and a hash map. O(1) get and put with explicit list management, no shortcut through Python's OrderedDict. |

</details>

<details>
<summary><a id="dsa-part-6"></a><strong>Part 6 · Trees & Heaps</strong></summary>

**Level:** Beginner to advanced &nbsp;·&nbsp; **For:** Anyone past the linear-data-structure phase of prep.

The hierarchical structures and the priority queue. Binary tree fundamentals, the three depth-first traversals (pre/in/post — both recursive and iterative), Morris traversal for O(1) space, level-order BFS, heaps and priority queues (heapify in O(n)), binary search trees, AVL rotations, a red-black overview, tries, the tree-DP primer (post-order with side state), and an introduction to segment trees for range queries.

| # | Chapter | What it covers |
|:-:|---|---|
| 6.0 | [Binary tree fundamentals](content/dsa/part-6-trees-heaps/00-binary-tree-fundamentals.md) | Tree terminology, height vs depth, the two physical representations, and the on-disk vocabulary every later Part 6 chapter assumes you have pinned down. |
| 6.1 | [Tree traversals: pre, in, post](content/dsa/part-6-trees-heaps/01-tree-traversals.md) | One recursive skeleton has three positions for the visit() call. The pre, in, and post placements solve different problem families on the same scaffolding. |
| 6.2 | [Morris traversal: O(1)-space inorder by threading](content/dsa/part-6-trees-heaps/02-morris-traversal.md) | Walk a binary tree in inorder with no recursion stack and no auxiliary memory by threading temporary right-pointers from each subtree's rightmost descendant back to its successor. |
| 6.3 | [Level-order traversal: BFS on trees](content/dsa/part-6-trees-heaps/03-level-order-traversal.md) | BFS on trees, with the level_size = len(queue) snapshot that turns 'visit every node' into 'visit every node grouped by depth' with the boundaries preserved. |
| 6.4 | [Heaps and priority queues](content/dsa/part-6-trees-heaps/04-heaps-priority-queues.md) | Sift-up and sift-down, Floyd's O(n) bottom-up build vs O(n log n) repeated insert, and the language-by-language API for the priority-queue primitive. |
| 6.5 | [Binary search trees](content/dsa/part-6-trees-heaps/05-binary-search-trees.md) | The BST invariant, search/insert/delete operations, and why every shipping standard library uses a balanced variant instead of a plain BST. |
| 6.6 | [AVL trees and rotations](content/dsa/part-6-trees-heaps/06-avl-rotations.md) | Self-balancing BSTs from first principles: the AVL invariant, the four rotation cases, the 1.44 log(n+2) height bound, and why every production ordered map descends from this 1962 paper. |
| 6.7 | [Red-black trees: an overview](content/dsa/part-6-trees-heaps/07-red-black-overview.md) | The balancing scheme behind TreeMap, std::map, and the Linux scheduler. Five invariants, the rotation cases at a high level, and what an interview can reasonably ask about them. |
| 6.8 | [Tries](content/dsa/part-6-trees-heaps/08-tries.md) | Children-map-plus-end-flag nodes give prefix walks in O(L) on query length. The autocomplete and IP-routing problem family where prefix structure is the whole point. |
| 6.9 | [Tree DP primer: post-order with side state](content/dsa/part-6-trees-heaps/09-tree-dp.md) | Post-order helpers thread side state down through arguments, return aggregates up the call stack, and use a global to track diameter-style through-this-node optima. |
| 6.10 | [Segment trees](content/dsa/part-6-trees-heaps/10-segment-tree.md) | O(log n) point updates and O(log n) range queries on the same array. The recursive build and the lazy-propagation extension for range updates. |

</details>

<details>
<summary><a id="dsa-part-7"></a><strong>Part 7 · Recursion & Backtracking</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** Anyone whose subset/permutation/combination solutions feel like guesswork.

Backtracking is just DFS with state-restoration discipline. The recursion patterns (linear, tree, divide-and-conquer); the backtracking template you can adapt to any constraint problem; subsets, combinations, and permutations; N-Queens with pruning; Sudoku with constraint propagation and forward checking; word search on a grid; and Fisher-Yates, reservoir sampling, and rejection sampling for randomized algorithms.

| # | Chapter | What it covers |
|:-:|---|---|
| 7.0 | [Recursion patterns: linear, tree, and divide-and-conquer](content/dsa/part-7-recursion-backtracking/00-recursion-patterns.md) | Three call-tree shapes — linear, tree, divide-and-conquer — and how to read the shape from the recursive case so you know whether you need memoization, an accumulator, or neither. |
| 7.1 | [The backtracking template](content/dsa/part-7-recursion-backtracking/01-backtracking-template.md) | Choose, recurse, unchoose, with prune-on-partial-information as the move that turns exponential search into something that finishes. |
| 7.2 | [Subsets, combinations, permutations](content/dsa/part-7-recursion-backtracking/02-subsets-combinations-permutations.md) | One recursion with three knobs (when to snapshot the path, what to skip, when to allow repeats) covers subsets (LC 78), permutations (LC 46), and combination sum (LC 39). |
| 7.3 | [N-Queens: pruning and constraint propagation](content/dsa/part-7-recursion-backtracking/03-n-queens.md) | Column and diagonal occupancy bitsets give O(1) attack checks. Symmetry pruning and the constraint-propagation idea that generalizes to Sudoku and beyond. |
| 7.4 | [Sudoku solver: constraint propagation and forward checking](content/dsa/part-7-recursion-backtracking/04-sudoku-solver.md) | Row, column, and box bitmasks combined with MRV cell selection and a forward-checking loop solve a 9x9 in milliseconds, despite 4 × 10^38 candidate fillings. |
| 7.5 | [Word search and grid backtracking](content/dsa/part-7-recursion-backtracking/05-word-search.md) | Grid DFS with mark-and-restore: the in-place visited trick that turns a 2D backtracking problem into one clean recursion. |
| 7.6 | [Randomized algorithms: Fisher-Yates, reservoir sampling, rejection sampling](content/dsa/part-7-recursion-backtracking/06-randomized-algorithms.md) | Three randomized recipes — Fisher-Yates shuffle, reservoir sampling, rejection sampling — whose proofs of uniform correctness are the actual lesson, not the code. |

</details>

<details>
<summary><a id="dsa-part-8"></a><strong>Part 8 · Graphs</strong></summary>

**Level:** Beginner to advanced &nbsp;·&nbsp; **For:** Anyone preparing for FAANG-tier interviews — graph problems are the differentiator.

The graph chapters are interview-grade end-to-end. Adjacency-list vs adjacency-matrix representations; BFS and DFS as orthogonal traversal templates; connected components and flood fill (Number of Islands); topological sort via Kahn's queue and via DFS post-order reverse; cycle detection on directed and undirected graphs; bipartite checking; union-find with path compression and union-by-rank; Dijkstra's algorithm; Bellman-Ford and negative cycles; and minimum spanning trees via both Kruskal and Prim.

| # | Chapter | What it covers |
|:-:|---|---|
| 8.0 | [Graph representation](content/dsa/part-8-graphs/00-graph-representation.md) | Three ways to store a graph (adjacency list, adjacency matrix, edge list), the memory math that decides between them, and the default every interview assumes. |
| 8.1 | [Breadth-first search](content/dsa/part-8-graphs/01-bfs.md) | Queue, visited set, and the discipline of never enqueuing the same vertex twice. The shortest-path-on-unweighted-edges algorithm, plus its multi-source and grid variants. |
| 8.2 | [Depth-first search](content/dsa/part-8-graphs/02-dfs.md) | Five lines that visit on entry and recurse on neighbors, plus the customization knobs (entry hook, exit hook, edge classification) every advanced graph algorithm later in Part 8 turns. |
| 8.3 | [Connected components and flood fill](content/dsa/part-8-graphs/03-connected-components.md) | Counting and measuring components in a graph or grid: the outer scan that turns plain BFS or DFS into the algorithm. |
| 8.4 | [Topological sort: Kahn's algorithm](content/dsa/part-8-graphs/04-topological-sort-kahn.md) | Indegree-driven, queue-based, iterative. Kahn's algorithm flags a cycle by failing to consume every vertex. |
| 8.5 | [Topological sort: DFS post-order reverse](content/dsa/part-8-graphs/05-topological-sort-dfs.md) | DFS-based topological sort: three-color recursion, post-order emission, and the algorithms that fall out of the same skeleton — Tarjan's bridges, Hierholzer's Eulerian path, cycle-length detection. |
| 8.6 | [Cycle detection in graphs](content/dsa/part-8-graphs/06-cycle-detection-graphs.md) | Three-state DFS coloring for directed cycles, parent-aware single-state DFS for undirected, and the bug both halves share when the wrong one is used. |
| 8.7 | [Bipartite check](content/dsa/part-8-graphs/07-bipartite-check.md) | Two-color a graph by BFS or DFS. The odd-cycle obstruction, the linear-time check, and the problem family that disguises this question as 'split into two groups'. |
| 8.8 | [Union-Find: parent forests, path compression, and union by rank](content/dsa/part-8-graphs/08-union-find.md) | Parent forests, union by rank, path compression, and the inverse-Ackermann amortized bound. The cycle-detection and connected-components problem family it owns. |
| 8.9 | [Dijkstra's shortest-path algorithm](content/dsa/part-8-graphs/09-dijkstra.md) | Single-source shortest paths on weighted graphs with non-negative edges: the priority-queue mechanics, the lazy-deletion idiom, and the min-max-path and 0-1 BFS specializations. |
| 8.10 | [Bellman-Ford and negative cycles](content/dsa/part-8-graphs/10-bellman-ford.md) | V-1 edge relaxations on every edge, an extra Vth pass to detect negative cycles, and the algorithm that handles the negative-edge case Dijkstra silently mis-reports. |
| 8.11 | [Minimum spanning tree: Kruskal's algorithm](content/dsa/part-8-graphs/11-mst-kruskal.md) | Kruskal's algorithm: sort edges by weight, accept each one whose endpoints sit in different components, halt at n-1 edges. The cycle check is union-find; the cost is the sort. |
| 8.12 | [Minimum spanning trees: Prim's algorithm](content/dsa/part-8-graphs/12-mst-prim.md) | Prim's algorithm grows a minimum spanning tree from a single start vertex by absorbing the cheapest crossing edge. Same MST as Kruskal, different path; better choice on dense and implicit graphs. |

</details>

<details>
<summary><a id="dsa-part-9"></a><strong>Part 9 · Dynamic Programming</strong></summary>

**Level:** Intermediate to advanced &nbsp;·&nbsp; **For:** The part most candidates fear most. Read this if "DP problems just don't click."

The most demanding part of the handbook. Build DP up from recursion (top-down memoization) and re-derive the bottom-up tabulation; 1D-state DPs (Climbing Stairs, House Robber, decision DP); the string-prefix decision DPs (Decode Ways, Word Break); 0/1 and unbounded knapsacks; longest-common-subsequence and edit distance; LIS in O(n²) and the patience-sort O(n log n) variant; palindrome DP; interval DP (matrix chain, burst balloons); grid DP; tree DP; and the bitmask DP family for "all subsets" problems.

| # | Chapter | What it covers |
|:-:|---|---|
| 9.0 | [Dynamic Programming: From Recursion to Memoization](content/dsa/part-9-dynamic-programming/00-dp-recursion-to-memo.md) | When a recursion's call tree carries redundancy, an eight-character cache drops Fibonacci from O(phi^n) to O(n). The systematic move from naive recursion to memoized recursion to bottom-up tabulation. |
| 9.1 | [DP: bottom-up tabulation](content/dsa/part-9-dynamic-programming/01-dp-bottom-up-tabulation.md) | Convert memoized recursion to an iterative table fill: dependency DAG, topological order, loop, array. Plus the rolling-pair O(1) compression. |
| 9.2 | [Dynamic programming on a 1D state](content/dsa/part-9-dynamic-programming/02-dp-1d.md) | 1D-state DP: when the answer at index i depends on a small fixed window of earlier indices. Climbing stairs, house robber, min cost climbing stairs, and the rolling-scalars space collapse. |
| 9.3 | [Decode Ways and Word Break: string-prefix decision DP](content/dsa/part-9-dynamic-programming/03-dp-decode-word-break.md) | Two string-prefix decision DPs whose recurrences look different but run on the same `dp[i]` = OR-over-valid-splits skeleton. LC 91 Decode Ways and LC 139 Word Break. |
| 9.4 | [0/1 knapsack](content/dsa/part-9-dynamic-programming/04-knapsack-01.md) | 0/1 knapsack: take-or-skip per item, the 1D table fill, why the inner loop sweeps right-to-left, and the family of subset-sum reformulations (LC 416, 494, 474, 879, 1049). |
| 9.5 | [Unbounded knapsack: when items can be picked over and over](content/dsa/part-9-dynamic-programming/05-knapsack-unbounded.md) | One inner-loop direction reversed from 0/1 knapsack unlocks the coin-change family. How 'minimum coins', 'count of ways', and 'minimum cost' all fit one recurrence. |
| 9.6 | [Longest common subsequence](content/dsa/part-9-dynamic-programming/06-lcs.md) | The O(n*m) 2D DP for longest common subsequence, parent-pointer recovery for the actual subsequence, and the edit-distance and shortest-common-supersequence variants that live on the same table. |
| 9.7 | [Edit distance](content/dsa/part-9-dynamic-programming/07-edit-distance.md) | Wagner-Fischer's three-way recurrence for the minimum number of insertions, deletions, and replacements that turn one string into another. The canonical 2D string DP. |
| 9.8 | [Longest Increasing Subsequence: the quadratic DP](content/dsa/part-9-dynamic-programming/08-lis-quadratic.md) | Per-index `dp[i]` = max-over-smaller-predecessors gives the O(n^2) LIS. Parent-pointer recovery and the variants (LIS count, LIS with k-tolerance) that stay quadratic. |
| 9.9 | [LIS: patience sort](content/dsa/part-9-dynamic-programming/09-lis-patience-sort.md) | From 9.8's O(n^2) DP to O(n log n): the patience-sort framing, the tails-array invariant, binary search by tail value, and the LC 354 sort-then-LIS reduction. |
| 9.10 | [Palindrome DP](content/dsa/part-9-dynamic-programming/10-palindrome-dp.md) | Filling a 2D table whose recurrence reads `dp[i+1][j-1]` forces a diagonal fill order. The longest-palindromic-substring and min-cuts family that lives on it. |
| 9.11 | [Interval DP: matrix chain and burst balloons](content/dsa/part-9-dynamic-programming/11-interval-dp.md) | State is `dp[l][r]`, and the recurrence picks the LAST operation in the range. Burst Balloons (LC 312) and Matrix Chain Multiplication (LC 1039) are the canonical specimens. |
| 9.12 | [Grid DP: forward fills, backward survives](content/dsa/part-9-dynamic-programming/12-grid-dp.md) | Top-down forward fills (Unique Paths, Min Path Sum) and bottom-up backward survives (Dungeon Game). The direction is picked by whether the constraint applies at start or finish. |
| 9.13 | [Tree DP: states that travel up the call stack](content/dsa/part-9-dynamic-programming/13-tree-dp.md) | Post-order helpers that return more than one number to the parent — (rob, skip), (diameter, depth) 