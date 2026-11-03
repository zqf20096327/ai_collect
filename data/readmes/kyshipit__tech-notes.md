**English** | [简体中文](README.zh.md)

<div align="center">

# Technical Notes
<p>
  <a href="#ai">AI</a> ·
  <a href="#quantization">Quantization</a> ·
  <a href="#ros2">ROS2</a> ·
  <a href="#embedded">Embedded</a> ·
  <a href="#iot">IoT</a> ·
  <a href="#tools">Tools</a> ·
  <a href="#scripts">Scripts</a> ·
  <a href="#repos">Repos</a>
</p>
</div>

> Technical notes covering embedded systems, AI, robotics, IoT and other related fields, continuously updated. If you find this useful, please give it a Star ⭐, thanks!


<a id="ai"></a>

## AI

> AI End-to-End | Knowledge System | Agent Architecture

- [AI Knowledge System Construction](en/ai/AI-Knowledge-System-Construction.md)
  <details>
  <summary>ⓘ more info</summary>

  > This document outlines a comprehensive knowledge system for the AI field, encompassing a complete technology stack from underlying mathematics to industrial-grade agents. It covers modules such as the "brain" (large-scale model), memory modules, planning modules, tool invocation, skills, RAG retrieval, model engineering, and agent engineering. The core focus is on building industrial-grade intelligent agents capable of solving real-world problems.

  `tags: #AI #Agent #RAG #LLM #Engineering`

  </details>

- [AI Engineering Implementation](en/ai/AI-Engineering-Implementation.md)
  <details>
  <summary>ⓘ more info</summary>

  > This is a collection of technical notes related to AI engineering implementation, covering modules such as model optimization, quantization, agent architecture, skill systems, and toolchains.

  `tags: #AI #Agent #RAG #LLM #Engineering`

  </details>


<a id="quantization"></a>

## Quantization

> Model Conversion | Quantization Deployment | RKNN | ONNX | NPU Inference

- [RKNPU Model Quantization Deployment Principles Manual](en/deploy/RKNPU-Model-Quantization-Deployment-Principles.md)
  <details>
  <summary>ⓘ more info</summary>

  > From ONNX to NPU instructions, what does the compiler do internally, how are parameters configured, and why?

  `tags: #RKNN #Quantization #ONNX #NPU #Deployment`

  </details>

- [MeloTTS RKNN Quantization Deployment Pitfalls](en/deploy/MeloTTS-RKNN-Quantization-Deployment-Pitfalls.md)
  <details>
  <summary>ⓘ more info</summary>

  > This document records the entire deployment process of PyTorch → ONNX → RKNN, documenting key pitfalls encountered, including dynamic dimensions, pseudo-dynamics, INT8 quantization, and Less operator conflicts. The final solution was: FP16 Encoder + FP16 Decoder (recommended for clear audio quality), and INT8 Decoder (an alternative, smaller in size but with some loss of audio quality).

  `tags: #MeloTTS #RKNN #INT8Quantization #ONNX #RK3588 #NPU`

  </details>


<a id="ros2"></a>

## ROS2

> ROS2 | WSL2 | Cross-machine communication | Fast-DDS

- [Complete Engineering Practice for ROS2 Robot Simulation and Navigation](en/ros/ROS2-Robot-Simulation-and-Navigation-Engineering-Practice.md)
  <details>
  <summary>ⓘ more info</summary>

  > This project builds a ROS2 robot simulation and navigation system from scratch, covering core aspects such as modeling, simulation, and navigation algorithms.

  `tags: #ROS2 #RobotSimulation #Navigation #EngineeringPractice`

  </details>

- [WSL2 ROS2 Cross-Machine Communication Issue](en/ros/WSL2-ROS2-Cross-Machine-Communication.md)
  <details>
  <summary>ⓘ more info</summary>

  > WSL2 Ubuntu 20.04/22.04/24.04 + ROS2 Foxy/Galactic/Humble/Rolling, cross-machine communication fails to discover nodes. After troubleshooting issues with the Fast-DDS multicast discovery mechanism, network interface binding, and environment variable configuration, the final solution was: unified DDS domain ID + forced intra-subnet multicast discovery + specified network interface eth0.

  `tags: #WSL2 #ROS2 #Fast-DDS #CrossMachineCommunication #MulticastDiscovery`

  </details>

- [Troubleshooting ROS2 Image Stuttering, WiFi QoS, and WSL2 Issues](en/ros/ROS2-Image-Stuttering-WiFi-QoS-and-WSL2-Troubleshooting.md)
  <details>
  <summary>ⓘ more info</summary>

  > On a ROS2 Jazzy + WSL2 Ubuntu 24.04 system, issues included image transmission stuttering, frame drops, and command crashes. Troubleshooting involved checking WiFi packet loss rate, compression settings, asynchronous encoding, and QoS configuration. The solution was ultimately achieved through three measures: ① Enabling compression on the publishing end; ② Moving encoding to a separate thread for asynchronous publishing; ③ Explicitly specifying the BEST_EFFORT QoS on the subscription end.

  `tags: #ROS2 #WiFi #QoS #WSL2 #ImageStuttering #Debugging`

  </details>

- [Cross-Compiling ROS2 Jazzy to RK3588 on x86](en/ros/Cross-Compiling-ROS2-Pitfalls.md)
  <details>
  <summary>ⓘ more info</summary>

  > This document records the configuration of dual sysroots, toolchain files, and CMakeLists to resolve issues such as disabled Python generators, missing system libraries, and link paths.

  `tags: #CrossCompileToolchain #cmake #CMakeLists.txt`

  </details>


<a id="embedded"></a>

## Embedded

> Cross-compilation | Rootfs build | QEMU chroot | Driver porting | Troubleshooting

- [Failed to take /etc/passwd lock: Invalid argument](en/embed/QEMU-Rootfs-Build-Systemd-Lock-Fix.md)
  <details>
  <summary>ⓘ more info</summary>

  > This document documents my experience building an ARM64 Ubuntu 24.04 rootfs root filesystem using x86 VMware-Ubuntu 20.04. It includes solutions to incompatibility errors caused by systemd v254 + OFD locks, summarizing the pitfalls encountered, providing multiple workable repair scripts, and analyzing the underlying principles.

  `tags: #Ubuntu24.04 #systemd #QEMU #ARM64_rootfs`

  </details>

- [RK3588 Ubuntu Porting Camera Display Issue](en/embed/Camera-Display-Troubleshooting.md)
  <details>
  <summary>ⓘ more info</summary>

  > An ATK-DLRK3588 development board with a 5.5-inch MIPI screen experienced camera display issues after porting Ubuntu from Buildroot. Troubleshooting included issues with the DRM display framework, MIPI DSI configuration, and camera driver compatibility.

  `tags: #RK3588 #MIPI #Camera #DRM #Ubuntu24.04`

  </details>

- [RK3588 ES8388 Audio No Sound Issue](en/embed/ES8388-Audio-No-Sound-Troubleshooting.md)
  <details>
  <summary>ⓘ more info</summary>

  > The ES8388 chip's internal OUT1/OUT2 output stage switches are off by default, preventing signals from reaching the speaker. Buildroot enables this automatically via UCM; on Ubuntu, it requires manual enabling via amixer or configuration for automatic startup.

  `tags: #RK3588 #ES8388 #Audio #ALSA #Ubuntu24.04`

  </details>

- [Porting Noble Version Rootfs to RK3588](en/embed/RK3588-Noble-Rootfs-Porting.md)
  <details>
  <summary>ⓘ more info</summary>

  > RK3588 is used to build and port the Ubuntu 24.04 rootfs, supporting QEMU chroot and driver porting.

  `tags: #RK3588 #Ubuntu24.04 #rootfs`

  </details>


<a id="iot"></a>

## IoT

> CAN | Bluetooth | NFC | Other Peripheral Interfaces

- [CAN UDS Vehicle Communication Diagnostic Technology Documentation](en/iot/CAN-UDS-Automotive-Diagnostic-Technical-Guide.md)
  <details>
  <summary>ⓘ more info</summary>

  > CAN bus communication principles, UDS protocol stack, ISO14229/ISO15765 standards, diagnostic service SID, sub-function, negative response code (NRC). Communication flow between vehicle diagnostic tools and ECUs, UDS request/response message format, and parsing of commonly used diagnostic services.

  `tags: #CAN #UDS #ISO14229 #ISO15765 #DiagnosticProtocol`

  </details>

- [Bluetooth Low Energy Communication Principles Explained](en/iot/Bluetooth-Low-Energy-Complete-Communication-Guide.md)
  <details>
  <summary>ⓘ more info</summary>

  > Bluetooth Low Energy communication principles, broadcasting and scanning, connection establishment, link encryption, application authentication, command interaction, and power management. Includes security mechanisms such as RPA/Replay Attack/Whitelist/IRK/CSRK, and power consumption and fault tolerance designs such as Dynamic Interval/OTA A/B Partition.

  `tags: #BLE #Bluetooth #LowPower #CommunicationProtocol #SecurityMechanism`

  </details>

- [NFC Technology Principles and Car Key Applications](en/iot/NFC-Technology-and-Car-Key-Applications.md)
  <details>
  <summary>ⓘ more info</summary>

  > This course provides a systematic explanation of NFC technology principles (13.56MHz, electromagnetic induction, load modulation, and three operating modes). It covers the general hardware architecture of automotive NFC key systems (antenna/RF controller/MCU/HSM/CAN bus). The course also explains automotive diagnostic communication protocols (ISO 14229 UDS and ISO 15765-2 transport layer), including four frame types, secure access mechanisms, and routine control format parsing.

  `tags: #NFC #NearFieldCommunication #DigitalKey #ISO15765-2`

  </details>


<a id="tools"></a>

## Tools

> Debugging Tools | Disassembler | Reverse Engineering

- [ELF Static Reverse Engineering](en/tools/ELF-Static-Reverse-Engineering-Analysis.md)
  <details>
  <summary>ⓘ more info</summary>

  > ELF file structure, ELF header, section table, symbol table, relocation table, dynamic link table. Static analysis workflow: strings → Ghidra decompilation → radare2 advanced analysis → reconstruct source code.

  `tags: #ELF #StaticAnalysis #ReverseEngineering #Ghidra #radare2`

  </details>

- [GDB Dynamic Debugging Guide](en/tools/GDB-Dynamic-Debugging-Guide.md)
  <details>
  <summary>ⓘ more info</summary>

  > GDB command cheat sheet, quick debugging process, memory check, conditional breakpoints, user-defined commands.

  `tags: #GDB #Debugging #DynamicAnalysis #Breakpoints`

  </details>

- [Common Git Operations and Security Practices](en/tools/Git-Common-Operations-and-Security-Practices.md)
  <details>
  <summary>ⓘ more info</summary>

  > Git common operations, branch management, conflict resolution, and security practices.

  `tags: #Git #VersionControl #SecurityPractices`

  </details>


<a id="scripts"></a>

## Scripts

> Project-aided build scripts and environment configuration

- [configure-rootfs.sh](scripts/configure-rootfs.sh)
  <details>
  <summary>ⓘ more info</summary>

  > Build and packaging script for Ubuntu 20.04/24.04 rootfs targeting RK3588. It supports automatic installation of the rkaiq camera engine deb package extracted from the Buildroot target directory.

  `tags: #RK3588 #Ubuntu #rootfs #PackagingScript`

  </details>

- [configure-bashrc](scripts/configure-bashrc)
  <details>
  <summary>ⓘ more info</summary>

  > Bash environment configuration file: intelligent PATH management, locale, history, and shell behavior optimization.

  `tags: #bash #shell #EnvironmentConfiguration`

  </details>

- [configure-vimrc](scripts/configure-vimrc)
  <details>
  <summary>ⓘ more info</summary>

  > Minimal Vim configuration without plugins, retains commonly used shortcuts and supports Linux/WSL clipboard.

  `tags: #vim #EditorConfiguration`

  </details>


<a id="repos"></a>

## Repos

> Open source project links

- [eai-rk3588](https://github.com/kyshipit/eai-rk3588)
  <details>
  <summary>ⓘ more info</summary>

  > A plug-in-based edge inference platform for RK3588, with multi-threaded pipeline, RKNN adapter, RKLLM runtime, and coordinator-driven multi-slot scheduling.

  </details>

- [MeloTTS](https://github.com/kyshipit/MeloTTS)
  <details>
  <summary>ⓘ more info</summary>

  > MeloTTS ONNX export + RKNN deployment on RK3588, INT8 quantization practice.

  </details>

- [ros-robot](https://github.com/kyshipit/ros-robot)
  <details>
  <summary>ⓘ more info</summary>

  > A scalable edge AI robot platform based on ROS2, with built-in YOLO detection, SCRFD face detection, local RKLLM, and TTS voice output.

  </details>

<p align="right">(<a href="#technical-notes">Back to top</a>)</p>

## License

The notes are in [CC BY-SA 4.0](LICENSE-CC-BY-SA) format, and the code/scripts are licensed under [the MIT License](LICENSE-MIT).
