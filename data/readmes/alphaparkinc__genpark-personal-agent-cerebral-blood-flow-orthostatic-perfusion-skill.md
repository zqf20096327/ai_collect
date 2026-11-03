# Personal Agent Cerebral Blood Flow Orthostatic Perfusion Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Transcranial Doppler (TCD) Middle Cerebral Artery (MCA) velocity modeler, Gosling Pulsatility Index (PI) calculator, and hypocapnic hyperventilation vasoconstriction evaluator.

## Architecture

```mermaid
flowchart TD
    DopplerInput[MCA Systolic Vs, Diastolic Vd, Mean Vm cm/s] --> TCDEngine[Transcranial Doppler Hemodynamics Engine]
    TCDEngine --> PICalc[Gosling Pulsatility Index: PI = Vs - Vd / Vm]
    TCDEngine --> RICalc[Pourcelot Resistive Index: RI = Vs - Vd / Vs]
    PICalc --> ResistanceTier[Downstream Microvascular Resistance Status]
    CO2Input[End-Tidal CO2 mmHg Delta] --> VasoreactivityEngine[Cerebral CO2 Vasoreactivity Modeler]
    VasoreactivityEngine --> VelocityShift[Cerebral Flow Velocity Shift %: -3.0% / mmHg]
    VelocityShift --> SymptomForecast[Prefrontal Oligemia, Dizziness & Panic Mitigation]
```

## Quickstart

```python
from client import PersonalAgentCerebralBloodFlowOrthostaticPerfusion

agent = PersonalAgentCerebralBloodFlowOrthostaticPerfusion()
res = agent.calculate_cerebral_perfusion_and_pulsatility(peak_systolic_velocity_cms=95.0, end_diastolic_velocity_cms=42.0, mean_flow_velocity_cms=60.0)
print(f"PI: {res['gosling_pulsatility_index_pi']} | Status: {res['pulsatility_status_tier']}")
```
