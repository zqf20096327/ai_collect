# Personal Agent Blood Pressure Dipping Hemodynamics Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Ambulatory Blood Pressure Monitoring (ABPM) nocturnal dipping modeler, mean arterial pressure (MAP) calculator, and orthostatic hemodynamic risk evaluator.

## Architecture

```mermaid
flowchart TD
    DayNightBP[Daytime & Nighttime SBP/DBP Means] --> DippingEngine[Nocturnal Dipping Engine]
    DippingEngine --> DippingPct[Dipping %: 1 - Night/Day]
    DippingEngine --> PhenotypeClass[Phenotype: Normal, Extreme, Non-Dipper, Riser]
    DippingEngine --> MAPCalc[Mean Arterial Pressure & Pulse Pressure]
    PosturalBP[Supine & 3-Min Standing BP] --> OrthostaticEngine[Orthostatic Baroreflex Modeler]
    OrthostaticEngine --> OrthoDiag[Normative / Orthostatic Hypotension / Hypertension]
```

## Quickstart

```python
from client import PersonalAgentBloodPressureDippingHemodynamics

agent = PersonalAgentBloodPressureDippingHemodynamics()
res = agent.calculate_nocturnal_bp_dipping_profile(daytime_sbp_mean=125.0, nighttime_sbp_mean=105.0)
print(f"Dipping: {res['systolic_dipping_percentage']} | Phenotype: {res['dipping_phenotype']}")
```
