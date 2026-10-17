# Open MHS 🦾

[![PyPI](https://img.shields.io/pypi/v/openmhs)](https://pypi.org/project/openmhs)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/tongriyaotxt/open-mhs)](https://github.com/tongriyaotxt/open-mhs)

> **Open Model Hardware Standard (MHS)** — An open-source implementation of AI agent hardware control, inspired by [Anthropic's Model Hardware Standard](https://www.anthropic.com/news/model-hardware-standard-research-preview).

MHS enables AI agents to **discover, monitor, and safely operate physical devices** through a unified protocol. Think of it as **MCP for the physical world**.

---

## What is MHS?

[Anthropic's MHS](https://www.anthropic.com/news/model-hardware-standard-research-preview) is a research preview standard that lets AI agents control lab equipment, robots, and manufacturing devices. **Open MHS** is the first open-source implementation, making this capability accessible to everyone.

### Key Features

- **Unified Device Interface** — Single protocol for all hardware
- **Cerebellum Layer** — Closed-loop motion skills, reflex arcs, and local forward models: the brain (LLM) supplies intent, the cerebellum handles real-time control
- **Safety-First Design** — Built-in limits and validation, plus reflex arcs that abort motion in one control tick without waiting for the LLM
- **Model Agnostic** — Works with any AI agent framework
- **MCP Compatible** — Expose devices as MCP tools
- **Multi-Transport** — CLI, REST API, and MCP server
- **Broad Hardware Support** — From sensors to robot arms

---

## Supported Hardware

| Category | Devices | Status |
|----------|---------|--------|
| **Sensors** | Temperature, Humidity, Distance, Light, Gas, IMU | ✅ Ready |
| **Cameras** | USB Webcam, IP Camera, Pi Camera | ✅ Ready |
| **Embedded** | Raspberry Pi GPIO, Arduino | ✅ Ready |
| **Smart Home** | MQTT devices, Smart Plugs, Lights | ✅ Ready |
| **Robotics** | Robot Arms, 3D Printers, Microduck biped (intent-level JSON-RPC) | ✅ Ready |
| **Lab Equipment** | Microscopes, Liquid Handlers, Lasers | ✅ Ready |

---

## Quick Start

### Installation

```bash
# Core only
pip install openmhs

# With all hardware support
pip install openmhs[all]

# With MCP and API servers
pip install openmhs[mcp,api]
```

### 1. Control a Device (Python)

```python
import asyncio
from openmhs.adapters.sensors import BME280Driver
from openmhs.core.driver import DriverConfig

async def main():
    # Connect to a temperature sensor
    config = DriverConfig(
        driver_name="bme280",
        connection_params={"device_id": "sensor_001"}
    )
    driver = BME280Driver(config)
    await driver.connect()
    
    # Read temperature
    result = await driver.device.read("temperature")
    print(f"Temperature: {result['value']}°C")

asyncio.run(main())
```

### 2. CLI Usage

```bash
# Setup demo devices
mhs demo

# List devices
mhs discover

# Read from a sensor
mhs read sensor_001 temperature

# Control a robot arm
mhs write arm_001 cartesian_position x=250 y=100 z=300 speed=80

# Check health
mhs status
```

### 3. REST API

```bash
# Start API server
mhs api --port 8000

# List devices
curl http://localhost:8000/devices

# Read sensor
curl -X POST http://localhost:8000/devices/sensor_001/read/temperature

# Control hardware
curl -X POST http://localhost:8000/devices/arm_001/write/joint_position \
  -H "Content-Type: application/json" \
  -d '{"joints": [0, 45, 90, 0, 90, 0], "speed": 50}'
```

### 4. MCP Server

Expose all devices as MCP tools for Claude, ChatGPT, or any MCP client:

```bash
# Stdio mode (for Claude Desktop)
mhs serve --mode stdio

# HTTP mode
mhs serve --mode http
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              Brain: AI Agent (Claude, Kimi, GPT, etc.)       │
│              High-level intent: "grasp the cup"              │
└──────────────────────┬──────────────────────────────────────┘
                       │ MCP / CLI / API (skill calls)
┌──────────────────────▼──────────────────────────────────────┐
│              Cerebellum (openmhs.cerebellum)                 │
│  ┌──────────┐ ┌───────────┐ ┌────────────┐ ┌─────────────┐ │
│  │  Skill   │ │ Control   │ │  Forward   │ │   Reflex    │ │
│  │ Library  │ │ Loop      │ │  Models    │ │   Arcs      │ │
│  │(reach,   │ │(fixed-rate│ │(prediction │ │(abort in 1  │ │
│  │ grasp...)│ │  ticks)   │ │  error)    │ │  tick)      │ │
│  └──────────┘ └───────────┘ └────────────┘ └─────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │ standard read/write capabilities
┌──────────────────────▼──────────────────────────────────────┐
│                  Open MHS Protocol Layer                    │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐ │
│  │  Read   │  │  Write   │  │ Discover │  │ Health Check│ │
│  └─────────┘  └──────────┘  └──────────┘  └─────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │ Unified Driver Interface
┌──────────────────────▼──────────────────────────────────────┐
│                    Hardware Adapters                         │
│  ┌────────┐ ┌────────┐ ┌──────────┐ ┌────────┐ ┌────────┐ │
│  │Sensors │ │ Cameras│ │  Robots  │ │  Lab   │ │ Smart  │ │
│  │        │ │        │ │  Arms    │ │Equipment│ │ Home   │ │
│  └────────┘ └────────┘ └──────────┘ └────────┘ └────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## The Cerebellum Layer

Why not just let the LLM write joint positions? Because end-to-end VLA-style
control is slow, data-hungry, hard to port across embodiments, and has no
safety floor. The cerebellum layer splits the work the way biology does:

- **Skills** — parameterized, closed-loop motor primitives (`reach`, `grasp`,
  ...) that sense and correct every tick
- **Forward models** — small per-skill predictors; prediction error triggers
  online correction (slow down, recover) instead of silent failure
- **Reflex arcs** — threshold rules evaluated every tick that can abort motion
  in one tick (~50 ms), no LLM round-trip required
- **Skill learning** — the brain teaches by demonstration (raw control while
  the cerebellum records); consistent demos are distilled into a DMP-based
  skill that generalizes to goals it never saw
- **Habits** — consolidated skills auto-trigger on familiar requests
  (autonomy: off / suggest / auto); reflexes still outrank habits

```python
import asyncio
from openmhs.cerebellum import Cerebellum, Reflex, SimArmDevice
from openmhs.core.registry import DeviceRegistry

async def main():
    registry = DeviceRegistry()
    arm = SimArmDevice("arm_001")  # or any real device with cartesian_position
    await arm.connect()
    await registry.register(arm)

    cerebellum = Cerebellum(registry, rate_hz=20.0)
    cerebellum.register_defaults()
    cerebellum.add_reflex(Reflex(
        name="obstacle_guard", device_id="arm_001", capability="proximity",
        key="distance", comparator="<", threshold=40.0, action="abort",
    ))

    # The brain issues one call; the cerebellum closes the loop.
    result = await cerebellum.run("grasp", "arm_001", x=400, y=0, z=100)
    print(result.status, result.detail)

asyncio.run(main())
```

Try the full story (disturbance rejection, reflex abort, force-controlled
grasp): `python examples/cerebellum_demo.py`

Watch the cerebellum *learn* (brain teaches 3 demos → skill crystallizes →
new goals work → habits fire with zero brain commands):
`python examples/cerebellum_learning_demo.py`

Skills are also exposed as MCP tools (`mhs_skill_list`, `mhs_skill_run`,
`mhs_skill_stop`) so any MCP-compatible agent can use them directly.

### Biped robots: Microduck adapter

`openmhs.adapters.robots.microduck` wraps [Microduck](https://github.com/pollen-robotics/microduck)
(Pollen Robotics' open-source RL biped) — itself a two-level system where the
robot's 50 Hz policy is the *motor* cerebellum and open-mhs skills
(`walk_to`, `look_at`, `pick_up`) are the *task* cerebellum on top of its
intent-level JSON-RPC API. Ships with a high-fidelity `MockMicroduckServer`
(same protocol, 50 Hz odometry integration, deadman/fallen semantics, 8x8 ToF,
procedural JPEG camera) so everything is reproducible without hardware:

```bash
python examples/microduck_kimi_demo.py   # works with no API key (scripted brain)
# set MOONSHOT_API_KEY to let Moonshot Kimi drive via tool-calling instead
```

---

## Writing a Custom Driver

```python
from openmhs.core.device import BaseDevice, DeviceCapability, DeviceMetadata
from openmhs.core.driver import Driver, DriverConfig, register_driver

class MyDevice(BaseDevice):
    async def connect(self):
        self._set_state(DeviceState.ONLINE)
        return True
    
    async def _do_read(self, capability, **params):
        return {"value": 42}
    
    async def _do_write(self, capability, **params):
        return {"set": params}

@register_driver
class MyDriver(Driver):
    DRIVER_NAME = "my_device"
    SUPPORTED_DEVICES = ["my_device"]
    
    async def connect(self):
        self._device = MyDevice(...)
        return True
```

---

## Project Status

This is an **early alpha** implementation based on publicly available information about Anthropic's MHS. The specification is still in research preview, and this project will evolve as the standard matures.

### Roadmap

- [x] Core protocol implementation
- [x] Device driver framework
- [x] MCP server integration
- [x] REST API
- [x] CLI tool
- [x] Sensor adapters (BME280, HC-SR04, analog)
- [x] Camera adapter
- [x] Robot arm adapter
- [x] 3D printer adapter
- [x] Raspberry Pi GPIO adapter
- [x] Arduino adapter
- [x] MQTT / Smart Home adapter
- [x] Lab equipment adapters (microscope, liquid handler, laser)
- [x] Cerebellum layer: closed-loop skills (reach, grasp)
- [x] Reflex arcs (sub-tick safety aborts)
- [x] Local forward models with prediction-error correction
- [x] Device simulation environment (SimArmDevice with dynamics, disturbances, obstacles)
- [x] Learning cerebellum: demonstration recording → DMP consolidation → habit auto-trigger
- [ ] Real hardware I2C/SPI support
- [ ] Vision-based habit preconditions (scene recognition)
- [ ] Web dashboard
- [ ] G-code streaming
- [ ] Multi-agent orchestration

---

## Contributing

Contributions welcome. Areas we need help:

- New hardware drivers
- Real hardware testing (we only have simulation modes for most devices)
- Documentation and tutorials
- Safety evaluation frameworks

---

## License

MIT License — see [LICENSE](LICENSE) file.

---

## Acknowledgements

Inspired by [Anthropic's Model Hardware Standard](https://www.anthropic.com/news/model-hardware-standard-research-preview) research preview and the [Model Context Protocol](https://modelcontextprotocol.io/).
