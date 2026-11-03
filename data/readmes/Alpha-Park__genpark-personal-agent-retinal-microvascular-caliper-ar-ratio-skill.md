# Personal Agent Retinal Microvascular Caliper AR Ratio Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Central Retinal Arteriolar/Venular Equivalent (CRAE/CRVE) modeler, Arteriolar-to-Venular Ratio (AVR) calculator, and cerebral microangiopathy velocity evaluator.

## Architecture

```mermaid
flowchart TD
    FundusInput[CRAE Microns & CRVE Microns, Age, SBP] --> CaliperEngine[Parr-Hubbard-Knudtson Caliper Engine]
    CaliperEngine --> AVRCalc[Arteriolar-to-Venular Ratio: AVR = CRAE / CRVE]
    CaliperEngine --> ArteriolarNarrowing[Arteriolar Narrowing: Chronic Sclerosis Marker]
    CaliperEngine --> VenularDilation[Venular Widening: Systemic Inflammation Marker]
    AVRCalc --> SMRIScore[Systemic Microangiopathy Risk Index: SMRI]
    AVRCalc & PulsePressure[Pulse Pressure mmHg] --> PulsatilityEngine[Cerebral Microvascular Pulsatility Strain]
    PulsatilityEngine --> EndOrganRisk[Intracranial Penetrating Arteriole Risk Tier]
```

## Quickstart

```python
from client import PersonalAgentRetinalMicrovascularCaliperArRatio

agent = PersonalAgentRetinalMicrovascularCaliperArRatio()
res = agent.calculate_retinal_avr_and_microvascular_risk(crae_microns=154.0, crve_microns=202.0)
print(f"AVR: {res['arteriolar_to_venular_ratio_avr']} | Tier: {res['microvascular_caliber_tier']}")
```
