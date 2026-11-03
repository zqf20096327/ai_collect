# Personal Agent Nocturnal Core Body Temperature Min Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency circadian core body temperature (CBT) nadir modeler, distal-to-proximal vasodilation heat dump calculator, and phase response curve inflection timing scheduler.

## Architecture

```mermaid
flowchart TD
    WakeInput[Habitual Wake Time & Peak/Nadir CBT Celsius] --> CBTEngine[Circadian Thermoregulatory Modeler]
    CBTEngine --> TMinCalc[Circadian Temperature Nadir T_min: ~1.75h Pre-Wake]
    CBTEngine --> TAmpCalc[Circadian Thermal Amplitude & Entrainment Status]
    TMinCalc --> PRCBoundary[PRC Boundary: Pre-Nadir Light Delays vs Post-Nadir Advances]
    BedtimeInput[Target Bedtime] --> HeatDumpEngine[Distal Vasodilation Heat-Dump Prescriptor]
    HeatDumpEngine --> ImmersionWindow[40.0-42.5 C Warm Immersion Window @ T-90 Min]
```

## Quickstart

```python
from client import PersonalAgentNocturnalCoreBodyTemperatureMin

agent = PersonalAgentNocturnalCoreBodyTemperatureMin()
res = agent.model_circadian_temperature_curve(habitual_wake_time_24h=7.0, evening_peak_cbt_celsius=37.2, nocturnal_nadir_cbt_celsius=36.3)
print(f"T_min Nadir: {res['projected_t_min_nadir_time']} | Amplitude: {res['circadian_temperature_amplitude_celsius']} C")
```
