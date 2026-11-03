# Personal Agent Non-Sleep Deep Rest (NSDR) Protocol Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency NSDR / Yoga Nidra neuro-autonomic state shift modeler, alpha/theta entrainment window projector, and striatal dopamine replenishment estimator.

## Architecture

```mermaid
flowchart TD
    SessionInput[Duration, Baseline & Post Respiratory Rates, Arousal Scores] --> NSDREngine[NSDR Autonomic Engine]
    NSDREngine --> PDRICalc[Parasympathetic Down-Regulation Index: PDRI]
    NSDREngine --> DopamineModeler[Striatal Dopamine Replenishment: Up to +65%]
    NSDREngine --> EEGClass[EEG Depth: Beta to Alpha to Theta Hypnagogia]
    CircadianDemand[Sleep Debt & Cognitive Load] --> Prescriptor[Circadian Timing Prescriptor]
    Prescriptor --> OptimalWindow[10-30 Min Reset Window Without Sleep Inertia]
```

## Quickstart

```python
from client import PersonalAgentNonSleepDeepRestNsdrProtocol

agent = PersonalAgentNonSleepDeepRestNsdrProtocol()
res = agent.evaluate_nsdr_state_shift(session_duration_minutes=20.0, baseline_respiratory_rate_bpm=16.0, post_session_respiratory_rate_bpm=8.0)
print(f"PDRI: {res['parasympathetic_down_regulation_index_pdri']} | Dopamine: {res['striatal_dopamine_replenishment_pct']}")
```
