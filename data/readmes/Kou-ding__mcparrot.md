# MCParrot

<div align="center"><p>
    <a href="https://github.com/Kou-ding/mcparrot/stargazers">
        <img alt="Stars" src="https://img.shields.io/github/stars/Kou-ding/mcparrot?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/Kou-ding/mcparrot/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/Kou-ding/mcparrot?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/Kou-ding/mcparrot/pulse">
        <img alt="Last commit" src="https://img.shields.io/github/last-commit/Kou-ding/mcparrot?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/Kou-ding/mcparrot/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/Kou-ding/mcparrot?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
</div>

<p align="center">
    <img src="static/images/logo.png" width=300 alt="Logo">
</p>

<p align="center">
    <strong>MCParrot</strong>: A File-Centric Penetration Testing Automation Framework Utilizing Specialized Agents. 
</p>

<p align="center">
    <a href="#demo">Demo</a> •
    <a href="#requirements">Requirements</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#features">Features</a> •
    <a href="#disclaimer">Disclaimer</a> •
    <a href="#docs">Docs</a> •
    <a href="#license">License</a>
</p>

---

<a id="demo"></a>

## 🎬 Demo

![mcparrot demo](static/videos/demo.webp)

<a id="requirements"></a>

## 📋 Requirements

- **Operating system**: Linux 🐧
- **API format**: Anthropic
- **Conda**: [Miniforge](https://github.com/conda-forge/miniforge) 🐍 (recommended)
```bash
# Install miniforge
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh

# Initialize conda
conda init "$(basename "$SHELL")"
```

<a id="quick-start"></a>

## 🚀 Quick Start

Quick start guide on running the program:

1. Create the MCParrot Python virtual environment:

```bash
# Choose your preferred python version (e.g. 3.9)
conda create --name mcparrot_venv python=3.9
```

2. Initialize the environment:

```bash
bash init.sh
```
Make sure to add your deepseek API in *.env*. 

> [!note] 
> **Compatibility**:
> The environment initialization script works on `Arch Linux`, some of its derivatives (`CachyOS`, `BlackArch`, `EndeavourOS`, `Artix`, `Manjaro`) and cybersecurity focused Debian-based systems such as `Kali Linux` and `Parrot OS`.

<details>
<summary> <b>📥 Manual Dependency Installation</b> </summary>

If your distribution is not supported you can manually install the following dependencies:

| Tool | Category | Link |
|---|---|---|
| **uv** | 🐍 Python toolchain | [astral-sh/uv](https://github.com/astral-sh/uv) |
| **nmap** | 🔍 Network recon | [nmap.org](https://nmap.org/) |
| **gobuster** | 🌐 Web enumeration | [OJ/gobuster](https://github.com/OJ/gobuster) |
| **hashcat** | 🔓 Password cracking | [hashcat/hashcat](https://github.com/hashcat/hashcat) |
| **sqlmap** | 💉 SQL injection | [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) |
| **metasploit** | 🎯 Exploitation | [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) |
| **termshark** | 🦈 Packet analysis | [gcla/termshark](https://github.com/gcla/termshark) |
| **binwalk** | 🧬 Firmware analysis | [ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| **bubblewrap** | 🛡️ Sandboxing | [containers/bubblewrap](https://github.com/containers/bubblewrap) |

</details>

3. Start the metasploit service:

```bash
msfrpcd -P kali -a 127.0.0.1 -S -f
```

> [!warning] 
> **Security Notice**:
> For enhanced security change the password (*kali*) on both the service run command and the .env file.

4. Run the app
```bash
uv run app.py
```

<a id="features"></a>

## ✨ Features

- **🦅 Hawk Mode (Targeted & Direct)**: A user-driven, **open-ended** task execution mode guided by direct user prompts.
- **🐦‍⬛ Raven Mode (Methodical & Autonomous)**: A **fully autonomous**, multi-agent orchestration mode that requires only a target IP to execute end-to-end.
- **⚙️ Finite State Machine (FSM) Architecture**: The penetration testing workflow is structured into 3 stages: `Reconnaissance`, `Vulnerability Assessment`, and `Exploitation`.
- **💾 Blackboard-Style Memory Management**: The system's memory is split across `message history`, `stage plans` and `summary`, preventing context window saturation.
- **💭 Native Reasoning**: Advanced "thinking" LLMs support with native reasoning capabilities, surpassing traditional Chain-of-Thought prompting for complex cybersecurity logic.
- **⛓️ Jailbreaking**: Carefully engineered system prompts that bypass standard LLM safety filters.
- **🛠️ Cybersecurity MCP servers**: Single-file Python MCP servers.
  - **Nmap**: Network scanning, port discovery and service version detection *(custom made)*.
  - **Gobuster**: Brute-force hidden directory, file and subdomain discovery *(custom made)*.
  - **SQLmap**: Automated detection and exploitation of SQL injection vulnerabilities *(custom made)*.
  - **Sandboxed Terminal**: Secure command execution utilizing `bwrap` (Bubblewrap) and intelligent **output truncation** to prevent context overflow *(heavily modified from [GongRzhe's Project](https://github.com/GongRzhe/terminal-controller-mcp))*.
  - **Hashcat**: GPU-accelerated password cracking *(ported to Linux from [MorDavid's Project](https://github.com/MorDavid/Hashcat-MCP))*.
  - **Metasploit**: Comprehensive penetration testing framework *(used as is from [GH05TCREW's Project](https://github.com/GH05TCREW/MetasploitMCP))*.
- **🎯 Evaluation**: Achieved a **77.4% success rate** on the Cybench Cybersecurity Benchmark and gained root access on **Metasploitable 1 & 2** in a single autonomous pass.

<a id="disclaimer"></a>

## ⚠️ Disclaimer
**FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY.**  
MCParrot is designed for security professionals and researchers to automate penetration testing workflows. Unauthorized use of this framework against targets without prior mutual consent is illegal. The developers assume no liability for any misuse or damage caused by this program.

<a id="docs"></a>

## 📄 Docs

For more information visit the [Project's site](https://kou-ding.github.io/mcparrot/)

<a id="license"></a>

## License

Apache 2.0
