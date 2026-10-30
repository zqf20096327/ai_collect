# Dynamic DFA Alpha-1 Fractal HRV & Aerobic Threshold Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `compute_dfa_alpha1_aerobic_threshold`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates short-term Detrended Fluctuation Analysis (DFA a1) fractal scaling of RR-intervals, pinpointing the precise aerobic threshold (a1 = 0.75) during endurance exertion.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Autonomic Nonlinear Dynamics)`

## MCP Tool Specification
### `compute_dfa_alpha1_aerobic_threshold`
Parameters:
- `rr_intervals_ms` (list): Series of beat-to-beat RR intervals (ms) during sustained exercise
- `current_power_watts` (float): Current mechanical power output (Watts) or velocity
- `current_heart_rate_bpm` (float): Concurrent heart rate in bpm

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-dynamic-hrv-dfa-alpha1-intensity-fractal-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-dynamic-hrv-dfa-alpha1-intensity-fractal-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
