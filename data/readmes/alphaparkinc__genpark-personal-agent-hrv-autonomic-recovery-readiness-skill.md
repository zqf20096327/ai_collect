# Personal Agent HRV Autonomic Recovery Readiness Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Heart Rate Variability (HRV) RMSSD/lnRMSSD autonomic nervous system balance evaluator, 30-day rolling baseline corridor tracker, and daily cognitive/physical capacity allocation engine.

## Architecture

```mermaid
flowchart TD
    HRVInput[Morning / Nocturnal RMSSD & Resting HR] --> TransEngine[Natural Log Transformation: lnRMSSD]
    TransEngine --> BaselineCorridor[30-Day Rolling Baseline Corridor: Mean & SD]
    BaselineCorridor --> ZScoreEval[Autonomic Z-Score & State Classification]
    ZScoreEval --> ReadinessScore[Daily Readiness Score: 0 - 100]
    ReadinessScore --> CapacityAlloc[Cognitive Deep Work & Physical Strain Allocation]
```

## Quickstart

```python
from client import PersonalAgentHrvAutonomicRecoveryReadiness

agent = PersonalAgentHrvAutonomicRecoveryReadiness()
res = agent.evaluate_daily_readiness(rmssd_ms=58.0, resting_hr_bpm=54.0)
print(f"Readiness Score: {res['daily_readiness_score']} | State: {res['autonomic_state']}")
```
