<p align="center">
  <img src="media/aira_hero.jpeg" width="900" alt="AIRA — An Intelligent Robotic Arm by Nextis">
</p>

<p align="center">
  <a href="https://nextis.tech">
    <img src="https://img.shields.io/badge/Nextis-Website-319795?style=for-the-badge" alt="Nextis">
  </a>
  <a href="https://a360.co/4logosj">
    <img src="https://img.shields.io/badge/Follower%20CAD-319795?style=for-the-badge&logo=autodesk" alt="Follower CAD">
  </a>
  <a href="https://a360.co/4rt2uXv">
    <img src="https://img.shields.io/badge/Leader%20CAD-319795?style=for-the-badge&logo=autodesk" alt="Leader CAD">
  </a>
  <a href="https://github.com/huggingface/lerobot">
    <img src="https://img.shields.io/badge/LeRobot-ff6f61?style=for-the-badge&logo=huggingface" alt="LeRobot">
  </a>
  <a href="https://x.com/robertorobotics">
    <img src="https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x" alt="Twitter">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-319795?style=for-the-badge" alt="License">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-319795?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.nextis.tech/hardware">
    <img src="https://img.shields.io/badge/Hardware-Get_a_Kit_or_Premium_Arm-ff6f61?style=for-the-badge" alt="Hardware">
  </a>
</p>

<h1 align="center">AIRA</h1>
<p align="center"><strong>An Intelligent Robotic Arm</strong></p>
<p align="center"><em>Build it. Plug it in. Train AI.</em></p>
<p align="center">Designed and built by <strong><a href="https://nextis.tech">Nextis</a></strong> · Powered by <a href="https://github.com/huggingface/lerobot">LeRobot</a></p>

---

AIRA is a 3D-printable, 7-DoF (6-DoF + 1-DoF Gripper) robotic arm with native integration into [LeRobot](https://github.com/huggingface/lerobot) — Hugging Face's open-source robotics framework. Clone the repo, `pip install`, and you get teleoperation, demonstration recording, and training with ACT, Diffusion Policy, PI0, GR00T N1.5, and every other policy in the LeRobot ecosystem.

> **This is a LeRobot plugin, not a fork.** Your arm stays up to date with the latest LeRobot features automatically.

> **Early Access**: The AIRA plugin is under active development and has not been fully tested by the community yet. Expect rough edges. Contributions, bug reports, and feedback are very welcome.

> **Safety Notice**: AIRA uses high-torque motors (up to 35 Nm peak) that can cause injury or damage if misconfigured. **You must configure and test every motor individually before assembling the arm.** Always keep one hand on the power switch during first tests. You build and operate AIRA entirely at your own risk. See the [Assembly Guide](hardware/ASSEMBLY.md) for the full safety protocol.

## Demo

<p align="center">
  <img src="media/aira_demo.gif" width="700" alt="AIRA Teleoperation Demo">
  <br>
  <em>Teleoperation with the leader arm → autonomous policy execution</em>
</p>

## Interactive 3D CAD Models (Autodesk Fusion 360)

<table align="center">
  <tr>
    <td width="50%" align="center">
      <a href="https://a360.co/4logosj" target="_blank">
        <strong>AIRA — Follower Arm</strong><br>
        <img src="media/cad_preview.png" width="100%" alt="AIRA Follower Arm CAD Preview">
      </a>
      <br><em>Damiao CAN bus motors</em>
    </td>
    <td width="50%" align="center">
      <a href="https://a360.co/4rt2uXv" target="_blank">
        <strong>AIRA — Leader Arm</strong><br>
        <img src="media/cad_leader_preview.png" width="100%" alt="AIRA Leader Arm CAD Preview">
      </a>
      <br><em>Dynamixel XL330 servos</em>
    </td>
  </tr>
</table>

> Click images above for fully interactive 3D viewer · Also available as downloadable STEP files in [`/hardware`](hardware/)

## Features

- **6+1 Degrees of Freedom** — 6-DoF arm plus 1-DoF gripper for full workspace coverage
- **LeRobot Native** — plugin architecture, not a fork. ACT, Diffusion Policy, PI0, GR00T N1.5 out of the box
- **Damiao CAN Bus Motors** — J8009P (20/35 Nm) for the base, J4340P (9/27 Nm) for mid-arm, J4310P (3/12.5 Nm) for wrist and gripper
- **Interactive Setup Wizard** — `aira-setup` walks you through motor-by-motor configuration. No terminal expertise needed
- **MIT Impedance Control** — compliant position tracking on the follower for smooth, safe operation (force feedback planned)
- **3D Printable** — print the frame at home, order a [verified kit](https://www.nextis.tech/hardware), or upgrade to CNC aluminum

## Hardware

| Component | Gear Ratio | Rated / Peak Torque | Rated / Peak Current | Qty | Purpose |
|-----------|-----------|---------------------|---------------------|-----|---------|
| Damiao J8009P | 9:1 | 20 Nm / 35 Nm | 20A / 50A | 2 | Base + Link1 (follower) |
| Damiao J4340P | 40:1 | 9 Nm / 27 Nm | 2.5A / 8A | 2 | Link2 + Link3 (follower) |
| Damiao J4310P | 10:1 | 3 Nm / 12.5 Nm | 2.5A / 7.5A | 3 | Link4 + Link5 + Gripper (follower) |
| Dynamixel XL330-M077 | — | Serial, 0.13 Nm | — | 7 | All joints (leader) |
| USB-CAN adapter | — | e.g. Canable, MKS CANable | — | 1 | CAN bus interface |
| RealSense D405 | — | Depth camera | — | 1 | Wrist camera (optional) |

**Estimated cost**: €2,000–€2,500 / $2,200–$2,750 (full teleop kit including shipping & import duties) · Per-part breakdown in [`hardware/BOM.md`](hardware/BOM.md)

## Quick Start

### 1. Print Parts

> See [`hardware/ASSEMBLY.md`](hardware/ASSEMBLY.md) for print settings and the full parts list.

### 2. Install Software

```bash
git clone https://github.com/robertorobotics/Nextis-AIRA-3D
cd Nextis-AIRA-3D
pip install -e .
```

### 3. Set Up CAN Bus

```bash
sudo aira-setup-can
```

### 4. Configure Motors (BEFORE Assembly)

> **Critical**: Configure each motor individually on the bench before installing it in the arm. See the [Assembly Guide](hardware/ASSEMBLY.md) for the full safety protocol.

```bash
aira-setup
```

The wizard walks you through connecting each motor one by one, setting Slave/Master IDs, and calibrating.

### 5. Assemble the Arm

> Only after all motors are configured and verified. See [`hardware/ASSEMBLY.md`](hardware/ASSEMBLY.md).

### 6. Teleoperate

```bash
lerobot-teleoperate \
  --robot.type=aira_follower \
  --teleop.type=aira_leader
```

### 7. Record Demonstrations

```bash
lerobot-record \
  --robot.type=aira_follower \
  --teleop.type=aira_leader \
  --dataset.repo_id=your-username/pick-and-place \
  --dataset.single_task="pick up the red block"
```

### 8. Train a Policy

```bash
lerobot-train \
  --policy=act \
  --dataset.repo_id=your-username/pick-and-place
```

### 9. Deploy

```bash
lerobot-eval \
  --policy.path=outputs/train/act_pick_and_place/checkpoints/last \
  --robot.type=aira_follower
```

## Architecture

```
lerobot-robot-aira/
├── src/
│   ├── lerobot_robot_aira/           # Main package (robot + motors + CLI)
│   │   ├── motors/
│   │   │   ├── damiao.py             # Damiao CAN bus driver (MIT impedance control)
│   │   │   └── tables.py             # Motor model parameters (J8009P, J4340P, J4310P)
│   │   ├── robots/
│   │   │   └── aira_follower.py      # LeRobot Robot interface → Damiao hardware
│   │   ├── teleoperators/
│   │   │   └── aira_leader.py        # LeRobot Teleoperator → Dynamixel leader arm
│   │   └── cli/
│   │       ├── setup_wizard.py       # aira-setup — interactive motor configuration
│   │       ├── setup_can.py          # aira-setup-can — CAN bus setup
│   │       └── test_motors.py        # aira-test-motors — hardware diagnostics
│   └── lerobot_teleoperator_aira/    # Shim for LeRobot teleoperator discovery
│       └── __init__.py               # Re-exports AiraLeader from main package
├── hardware/                         # STL, STEP, BOM, assembly instructions
├── examples/                         # Step-by-step tutorials
└── tests/
```

## How It Works

AIRA registers with LeRobot's plugin system via `pkgutil` module scanning. LeRobot discovers any installed package named `lerobot_robot_*` (for robots) or `lerobot_teleoperator_*` (for teleoperators). When you run `lerobot-teleoperate --robot.type=aira_follower`, LeRobot finds `lerobot_robot_aira` and `lerobot_teleoperator_aira` automatically — no source code changes needed.

The critical new component is the **Damiao CAN bus driver** (`damiao.py`). LeRobot has built-in Feetech and Dynamixel support, but no CAN bus motors. AIRA adds this. The leader arm reuses LeRobot's built-in Dynamixel driver.

## Troubleshooting

**"No CAN interfaces found"**
> Plug in your USB-CAN adapter and run `sudo aira-setup-can`

**"Motor did not respond"**
> Check power supply voltage, CAN bus wiring, termination resistor

**"Permission denied on CAN bus"**
> Run the setup with `sudo`, or add your user to the `can` group

**Calibration issues**
> Delete `~/.cache/lerobot_robot_aira/calibration/` and re-run `aira-setup`

**"DynamixelMotorsBus connection failed"**
> Check USB port: `ls /dev/ttyUSB* /dev/ttyACM*`

## Acknowledgments

AIRA builds on the work of an incredible open-source community:

- **[LeRobot](https://github.com/huggingface/lerobot)** by Hugging Face — the robotics framework that powers AIRA's software. Every policy, dataset tool, and training recipe just works.
- **[The Robot Learning Company](https://github.com/robot-learning-co)** — gripper design inspiration adapted for AIRA's wrist.
- The open-source robotics community — especially everyone who reached out after the initial launch.

## Contributing

This project is open source (Apache 2.0). Contributions welcome:

- Motor model support (new Damiao models)
- Gripper designs
- Camera mount variants
- Training recipes and pretrained policies
- Bug fixes and documentation

## Get AIRA Hardware

Don't want to source and print everything yourself? We offer two options:

- **Verified Kit** — everything included (3D-printed frame, motors, electronics). Just assemble.
- **Aluminium Premium Arm** — CNC aluminum build, professionally assembled and calibrated. Direct support from Nextis.

Both available at [nextis.tech/hardware](https://www.nextis.tech/hardware).

## License

Apache 2.0 — see [LICENSE](LICENSE).

**Disclaimer**: AIRA is provided as-is, without warranty of any kind. High-torque robotic arms are inherently dangerous. You are solely responsible for safe assembly, configuration, and operation. Nextis and the contributors to this project accept no liability for any damage, injury, or loss resulting from the use of this hardware or software.

---

<p align="center">
  <a href="https://buymeacoffee.com/robertorobotics">
    <img src="https://img.shields.io/badge/Buy_Me_A_Coffee-support_AIRA-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
  </a>
</p>

<p align="center">
  <sub>Built with care by <a href="https://nextis.tech">Nextis</a></sub>
</p>
