# rl-trader

**Legacy case study (2021) · Distributed systems + MLOps**

Streaming features and distributed reinforcement-learning training/serving — Kafka, ksqlDB, Ray/RLlib, and Ray Serve. The trading policy is the workload, not the product.

This is **not** a current flagship and is **not** investment advice. Current SA work lives on the [profile](https://github.com/Ryan-Ray-Martin).

Walkthrough: [Deep reinforcement learning for stock trading with Kafka and RLlib](https://ryanraymartin.medium.com/deep-reinforcement-learning-for-stock-trading-with-kafka-and-rllib-d738b9634675)

---

## Problem

A learning agent needed **fresh market features** and **distributed training**, then a way to **serve a policy** without collapsing the pipeline into a laptop notebook. The systems problem was:

1. Ingest a tick/quote stream.
2. Derive features close to the data (stream SQL).
3. Train a policy with a distributed RL runtime.
4. Expose the policy behind an HTTP endpoint.

## Architecture

```
market feed  -->  Kafka  -->  ksqlDB feature queries  -->  Ray / RLlib (PPO or SAC)
                                                              |
                                                              v
                                                         Ray Serve  /trade_stocks
```

| Piece | Role in this repo |
| --- | --- |
| Confluent Kafka + ZooKeeper (`docker-compose.yml`) | Local streaming backbone |
| ksqlDB | Stream-side feature derivation |
| Faust client (`faust_stock.py`) | Python stream processing path |
| Polygon websocket (`websocket_client.py`, `stock_polygon.py`) | Market data ingress |
| Ray RLlib (`ppo_stock_backend.py`, `sac_stock_backend.py`) | Distributed policy training |
| Ray Serve (`deploy_stock_trader.py`) | Policy HTTP endpoint |

Earlier iterations of the same idea (now private): `PPO_Stock_Trader`, `kafka_crypto_trader`, `crypto-rl-trader`, `Trading_Agent`.

## What I would do differently in 2026

- **Lakehouse + feature store** instead of ad-hoc ksql + local files. Treat features as a governed data product.
- **IaC and an env cost sheet.** The 2021 compose file is a laptop lab, not a customer POC.
- **Evals as a gate.** Offline policy quality, latency, and $ per episode — not “the reward curve looked good.”
- **GPU training and a real serving SLO.** Ray on a single box is not the 2026 conversation.
- **No more trading-themed public headlines.** Same systems muscles; customer-shaped workloads (agents, retrieval, lakehouse).

## Disclaimer

Research and education only. Not a trading system. Past results do not predict future results. You are solely responsible for any use of this code.

## License / use

See the repository files. Prefer the Medium post for narrative; prefer the compose file and `deploy_*.py` for the runtime shape.
