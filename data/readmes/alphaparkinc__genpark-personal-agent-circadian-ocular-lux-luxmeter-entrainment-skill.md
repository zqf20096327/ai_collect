# Personal Agent Circadian Ocular Luxmeter Entrainment Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency CIE S 026 melanopic equivalent daylight illuminance (melanopic EDI) quantifier, intrinsically photosensitive retinal ganglion cell (ipRGC) modeler, and solar zeitgeber scheduler.

## Architecture

```mermaid
flowchart TD
    LuxInput[Photopic Lux & Light Source Spectrum] --> EDIEngine[CIE S 026 Melanopic Engine]
    EDIEngine --> MAFMultiplier[Melanopic Action Factor: 0.08x to 1.10x]
    MAFMultiplier --> MelanopicEDI[Melanopic Equivalent Daylight Illuminance: EDI Lux]
    MelanopicEDI & ExposureTime[Duration & Time Post-Waking] --> PRCEngine[Circadian Phase Response Curve Modeler]
    PRCEngine --> PhaseShift[Phase Advance / Delay Prediction in Hours]
    PRCEngine --> SCNEntrainment[Suprachiasmatic Nucleus Master Clock Reset]
```

## Quickstart

```python
from client import PersonalAgentCircadianOcularLuxLuxmeterEntrainment

agent = PersonalAgentCircadianOcularLuxLuxmeterEntrainment()
res = agent.calculate_melanopic_edi_and_circadian_drive(photopic_lux=15000.0, light_source_spectrum="direct_sunlight")
print(f"Melanopic EDI: {res['melanopic_equivalent_daylight_illuminance_edi']} lux | PRC: {res['circadian_phase_shift_trajectory']}")
```
