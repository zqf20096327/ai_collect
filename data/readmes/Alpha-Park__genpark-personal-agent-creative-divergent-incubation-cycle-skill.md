# Personal Agent Creative Divergent Incubation Cycle Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Graham Wallas 4-stage creativity modeler, cognitive impasse fixation detector, Default Mode Network (DMN) spreading activation calculator, and incubation scheduler.

## Architecture

```mermaid
flowchart TD
    FocusSession[Continuous Focus Minutes & Impasse Friction] --> FixationAuditor[Cognitive Fixation Auditor]
    FixationAuditor --> WallasStage[Wallas Creativity Stage: Preparation vs Incubation Mandate]
    FixationAuditor --> DMNPotential[Default Mode Network Spreading Activation Potential]
    BreakWindow[Available Break Window Minutes] --> IncubationScheduler[Subconscious Incubation Scheduler]
    IncubationScheduler --> LowDemandActivity[Walking / Hydrotherapy Protocol & Insight Capture]
```

## Quickstart

```python
from client import PersonalAgentCreativeDivergentIncubation

agent = PersonalAgentCreativeDivergentIncubation()
res = agent.evaluate_incubation_necessity(focus_duration_continuous_minutes=100.0, impasse_friction_score=8.0)
print(f"Fixation Index: {res['cognitive_fixation_index']} | Stage: {res['wallas_creative_stage']}")
```
