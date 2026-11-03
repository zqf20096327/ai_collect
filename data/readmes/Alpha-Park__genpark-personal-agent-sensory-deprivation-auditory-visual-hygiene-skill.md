# Personal Agent Sensory Deprivation Auditory Visual Hygiene Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Sensory Overload Index (SOI) quantifier, thalamocortical sensory gating modeler, and Restricted Environmental Stimulation Therapy (REST) protocol prescriptor.

## Architecture

```mermaid
flowchart TD
    SensoryInput[Screen Time, Decibel Level, Notification Interrupts, Blue Light] --> SOIEngine[Sensory Overload Engine]
    SOIEngine --> AcousticBurden[Acoustic Decibel Logarithmic Burden]
    SOIEngine --> PhotopicBurden[Photopic Irradiance & Retinal Flux]
    SOIEngine --> InterruptBurden[Attentional Task-Switching Latency]
    SOIEngine --> SOIScore[Sensory Overload Index: SOI 0-100]
    SOIScore --> RESTPrescription[Restricted Environmental Stimulation Therapy: REST]
    RESTPrescription --> Regimes[Flotation REST / Chamber REST / Micro Hiatus]
```

## Quickstart

```python
from client import PersonalAgentSensoryDeprivationAuditoryVisualHygiene

agent = PersonalAgentSensoryDeprivationAuditoryVisualHygiene()
res = agent.calculate_sensory_overload_burden(daily_screen_time_hours=8.0, average_ambient_decibels=65.0, daily_notification_interrupts=80)
print(f"SOI: {res['sensory_overload_index_soi']}/100 | Tier: {res['sensory_saturation_tier']}")
```
