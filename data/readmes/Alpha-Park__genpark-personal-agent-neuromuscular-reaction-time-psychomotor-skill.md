# Personal Agent Neuromuscular Reaction Time Psychomotor Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Psychomotor Vigilance Task (PVT) attentional lapse counter, reciprocal speed modeler, and cumulative sleep debt neurobehavioral impairment evaluator.

## Architecture

```mermaid
flowchart TD
    TrialData[Reaction Times ms Array] --> PVTEngine[Dinges PVT Statistical Engine]
    PVTEngine --> FilterFalseStarts[Filter Anticipation False Starts: < 100 ms]
    PVTEngine --> MeanMedian[Mean & Median Reaction Times]
    PVTEngine --> LapseCount[Lapses Counter: Trials >= 500 ms]
    PVTEngine --> ReciprocalSpeed[Reciprocal Speed: 1000 / RT Mean s^-1]
    LapseCount & ReciprocalSpeed --> SleepDebtModeler[Van Dongen Sleep Debt Dose-Response Model]
    SleepDebtModeler --> ImpairmentEquivalence[Impairment Analogy: 0.05% to >= 0.08% BAC Equivalence]
```

## Quickstart

```python
from client import PersonalAgentNeuromuscularReactionTimePsychomotor

agent = PersonalAgentNeuromuscularReactionTimePsychomotor()
res = agent.evaluate_pvt_attentional_performance([230.0, 245.0, 520.0, 240.0, 260.0])
print(f"Mean RT: {res['mean_reaction_time_ms']} ms | Lapses: {res['attentional_lapse_count_500ms']}")
```
