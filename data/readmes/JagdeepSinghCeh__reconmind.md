# 🔱 ReconMind — AI-Powered Bug Bounty Agent

<div align="center">

![ReconMind Banner](https://img.shields.io/badge/ReconMind-AI%20Bug%20Bounty%20Agent-brightgreen?style=for-the-badge&logo=shield&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/encrypticle/reconmind?style=flat-square&color=yellow)](https://github.com/encrypticle/reconmind/stargazers)
[![YouTube](https://img.shields.io/badge/YouTube-Encrypticle-red?style=flat-square&logo=youtube)](https://youtube.com/@encrypticle)
[![Instagram](https://img.shields.io/badge/Instagram-encrypticle-E4405F?style=flat-square&logo=instagram)](https://instagram.com/encrypticle)

**An autonomous, LLM-orchestrated bug bounty hunting agent built for serious hunters.**  
Chains Recon → Enum → Scan → Fuzz → AI Analysis → Report — fully automated.

[🚀 Quick Start](#-quick-start) • [📖 Usage](#-usage) • [💬 Discord](https://discord.com/invite/RR42FjT4) • [📺 YouTube](https://youtube.com/@encrypticle)

</div>

---

> ⭐ **If this tool helps you find bugs — star this repo and [subscribe to Encrypticle](https://youtube.com/@encrypticle) if you haven't already! Every star helps the community discover this tool.**

---

## 🧠 What is ReconMind?

ReconMind is an AI-powered bug bounty agent that thinks and hunts like a **senior penetration tester**. Instead of just running tools, it uses an LLM brain (Claude / Llama / Groq) to make decisions at every step — selecting targets, chaining findings, filtering false positives, and generating platform-ready reports.

```
Target Domain
     │
     ▼
┌──────────────────────────────────────────────────────┐
│                 RECONMIND PIPELINE                    │
│                                                      │
│  RECON → ENUM → SCAN → FUZZ → ANALYZE → REPORT      │
│                                                      │
│  🧠 AI Brain decides what to test next at each step  │
└──────────────────────────────────────────────────────┘
     │
     ▼
HackerOne / Bugcrowd / Intigriti Ready Reports
```

### 🎯 What makes it different?

- **Domain-only by default** — no noisy subdomain scan unless you want it (`--subdomain`)
- **Full OWASP Top 10** coverage with `--thorough` flag
- **AI decides what to scan next** — not just blindly running tools
- **Attack chain identification** — combines low findings into critical impact
- **False positive filtering** — AI validates each finding before reporting
- **100% Free to use** — works with Ollama (local), Groq (free API), or Anthropic (paid)
- **Platform-ready reports** — HackerOne, Bugcrowd, Intigriti format

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/encrypticle/reconmind.git
cd reconmind

# 2. Install everything (tools + dependencies)
chmod +x setup.sh
./setup.sh

# 3. Start Ollama (free local LLM — no API key needed)
ollama serve &
ollama pull llama3.1:8b

# 4. Hunt!
python3 reconmind.py --target example.com
```

---

## 📋 Requirements

### System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| OS | Ubuntu 22.04 / Parrot OS | **Kali Linux** |
| Python | 3.9 | 3.11+ |
| RAM | 4GB | 8GB+ (16GB for local Ollama) |
| Disk | 10GB | 20GB |
| Go | 1.21+ | Latest |

### Python Dependencies

```txt
pyyaml>=6.0
rich>=13.7
click>=8.1
httpx>=0.27
aiohttp>=3.9
aiofiles>=23.2
anthropic>=0.40.0
ollama>=0.3.0
groq>=0.11.0
beautifulsoup4>=4.12
tldextract>=5.1
dnspython>=2.6
jinja2>=3.1
tenacity>=8.2
```

Install all:
```bash
pip3 install -r requirements.txt --break-system-packages
```

### External Security Tools

| Tool | Purpose | Install |
|------|---------|---------|
| subfinder | Subdomain enumeration | `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| httpx | HTTP probing + tech detect | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| nuclei | Vulnerability scanning | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| naabu | Port scanning | `go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest` |
| katana | Web crawling | `go install github.com/projectdiscovery/katana/cmd/katana@latest` |
| ffuf | Directory fuzzing | `go install github.com/ffuf/ffuf/v2@latest` |
| dalfox | XSS detection | `go install github.com/hahwul/dalfox/v2@latest` |
| gau | Historical URLs | `go install github.com/lc/gau/v2/cmd/gau@latest` |
| waybackurls | Wayback Machine URLs | `go install github.com/tomnomnom/waybackurls@latest` |
| gf | Grep patterns | `go install github.com/tomnomnom/gf@latest` |
| amass | Deep subdomain enum | `sudo apt install amass` |
| sqlmap | SQL injection | `sudo apt install sqlmap` |
| nikto | Web server scanner | `sudo apt install nikto` |
| whatweb | Technology fingerprint | `sudo apt install whatweb` |

> 💡 **Just run `./setup.sh` — it installs everything automatically.**

---

## 🔧 Installation (Step by Step)

### Step 1 — Clone & Install

```bash
git clone https://github.com/encrypticle/reconmind.git
cd reconmind
chmod +x setup.sh
./setup.sh
```

### Step 2 — Configure LLM

```bash
cp configs/config.example.yaml configs/config.yaml
nano configs/config.yaml
```

### Step 3 — Get Your API Keys

#### 🆓 Groq (Free — Best for beginners)

1. Go to **[console.groq.com](https://console.groq.com)**
2. Sign up → **API Keys** → **Create API Key**
3. Copy the key starting with `gsk_...`
4. Add to `configs/config.yaml`:

```yaml
llm:
  default: groq
  groq:
    enabled: true
    api_key: "gsk_your_key_here"
```

#### 🖥️ Ollama (Free — No internet, runs locally)

```bash
# Install
curl -fsSL https://ollama.ai/install.sh | sh

# Start the service
ollama serve &

# Pull a model (choose based on your RAM)
ollama pull llama3.1:8b      # Needs 8GB RAM  — good balance
ollama pull llama3.1:70b     # Needs 32GB RAM — better quality
ollama pull mistral-nemo     # Needs 4GB RAM  — lightweight
```

Add to config:
```yaml
llm:
  default: ollama
  ollama:
    enabled: true
    base_url: "http://localhost:11434"
    model: "llama3.1:8b"
```

#### 💎 Anthropic Claude (Paid — Highest quality)

1. Go to **[console.anthropic.com](https://console.anthropic.com)**
2. Add billing → minimum $5 credits
3. **API Keys** → **Create Key**
4. Add to config:

```yaml
llm:
  default: anthropic
  anthropic:
    enabled: true
    api_key: "sk-ant-your_key_here"
```

> 💡 **Pro tip:** Use **Groq** for daily hunting (free), switch to **Anthropic** for final reports on high-severity findings.

### Step 4 — Verify Everything is Ready

```bash
python3 reconmind.py --check-tools
```

---

## 🚀 Usage

### Basic Commands

```bash
# Scan a domain (domain-only — fast, clean)
python3 reconmind.py --target example.com

# With subdomain enumeration
python3 reconmind.py --target example.com --subdomain

# Deep OWASP Top 10 testing
python3 reconmind.py --target example.com --thorough

# Full nuclear hunt
python3 reconmind.py --target example.com --subdomain --thorough

# Specify LLM backend
python3 reconmind.py --target example.com --llm groq
python3 reconmind.py --target example.com --llm anthropic
python3 reconmind.py --target example.com --llm ollama

# Custom project name (organizes output folder)
python3 reconmind.py --target example.com --project h1_hunt_jan2025

# Specific phases only
python3 reconmind.py --target example.com --phases recon,scan,report

# Multiple targets from file
python3 reconmind.py --targets targets.txt

# Resume interrupted scan
python3 reconmind.py --target example.com --resume
```

### Hunting Profiles

```bash
python3 reconmind.py --target example.com --profile quick        # Fast: recon+scan+report
python3 reconmind.py --target example.com --profile deep         # Everything + validate
python3 reconmind.py --target api.example.com --profile api      # API-focused hunt
python3 reconmind.py --target example.com --profile cloud        # Cloud misconfigs
python3 reconmind.py --target example.com --profile mobile_api   # Mobile backend
```

### All Flags Reference

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--target` | `-t` | — | Target domain |
| `--targets` | `-T` | — | File with list of targets |
| `--project` | `-P` | domain name | Project name for output folder |
| `--subdomain` | | off | Enable subdomain enumeration |
| `--thorough` | | off | Deep OWASP Top 10 testing |
| `--llm` | `-l` | config default | ollama / anthropic / groq |
| `--profile` | | default | Hunting profile |
| `--phases` | `-p` | all | Specific phases to run |
| `--scope` | `-s` | standard | narrow / standard / wide |
| `--resume` | `-r` | off | Resume from checkpoint |
| `--output` | `-o` | ./output | Custom output directory |
| `--check-tools` | | — | Show installed tools status |

---

## 🔍 OWASP Top 10 Coverage (`--thorough`)

| # | Category | What ReconMind Tests |
|---|----------|---------------------|
| A01 | Broken Access Control | IDOR detection, HTTP method tampering, forced browsing, 403 bypass via headers |
| A02 | Cryptographic Failures | HTTP without TLS, sensitive data in URLs, missing HSTS |
| A03 | Injection | SQLi (error/blind/time-based/boolean), XSS (reflected/DOM), SSTI, LFI, Command Injection, XXE, XPath |
| A04 | Insecure Design | AI-driven business logic analysis, rate limiting gaps, race conditions |
| A05 | Security Misconfiguration | .env, .git, debug endpoints, Actuator, Swagger, phpinfo, directory listing |
| A06 | Outdated Components | Technology fingerprinting + nuclei CVE matching |
| A07 | Auth Failures | Insecure cookies (Secure/HttpOnly/SameSite), session management |
| A08 | Integrity Failures | Missing SRI on external scripts, deserialization indicators |
| A09 | Logging Exposure | Exposed log files, stack traces, verbose error messages |
| A10 | SSRF | URL parameter probing, AWS/GCP metadata endpoints, internal host access |
| ➕ | Response Manipulation | JSON boolean flip, 403 bypass, header injection |

---

## 📁 Output Structure

```
./output/
└── your_project/
    └── 20250429_143022/
        ├── recon/
        │   ├── subdomains.txt       ← All discovered subdomains
        │   ├── urls.txt             ← Historical URLs
        │   ├── js_files.txt         ← JavaScript files
        │   └── params.txt           ← Parameterized URLs
        ├── enum/
        │   ├── live_hosts.txt       ← Confirmed live hosts
        │   ├── httpx_results.json   ← Tech stack, status codes
        │   └── ports.json           ← Open ports per host
        ├── scan/
        │   ├── nuclei_results.json  ← Raw nuclei findings
        │   ├── all_vulnerabilities.json
        │   └── attack_chains.json   ← AI-identified chains
        ├── fuzz/
        │   └── fuzz_results.json    ← XSS, SQLi, LFI results
        ├── analyze/
        │   └── final_analysis.json  ← AI analysis + prioritization
        └── report/
            ├── EXECUTIVE_SUMMARY.md     ← 👈 Start here
            ├── vuln_1_xss.md            ← HackerOne-ready report
            ├── vuln_2_sqli.md
            └── chain_1_ssrf_rce.md      ← Attack chain report
```

---

## 🧠 LLM Backend Comparison

| Backend | Cost | Speed | Quality | Best For |
|---------|------|-------|---------|----------|
| Ollama | 🆓 Free | 🐢 Slow (CPU) | ⭐⭐⭐ | Offline use, testing |
| Groq | 🆓 Free | ⚡ Fast | ⭐⭐⭐⭐ | Daily hunting |
| Anthropic | 💰 ~$0.01/hunt | 🚀 Fast | ⭐⭐⭐⭐⭐ | Final reports, critical analysis |

---

## 🧪 Test on Intentionally Vulnerable Sites

**Practice legally before hunting real programs:**

```bash
# Acunetix test site (SQLi, XSS, LFI and more)
python3 reconmind.py --target testphp.vulnweb.com --thorough

# OWASP WebGoat (run locally)
python3 reconmind.py --target localhost:8080 --thorough

# HackTheBox / TryHackMe targets (use VPN)
python3 reconmind.py --target 10.10.x.x --thorough
```

---

## ⚠️ Legal Disclaimer

> This tool is for **authorized security testing only**. Always ensure you have **explicit written permission** before testing any target. The author is not responsible for any misuse or damage caused by this tool.
> 
> Only hunt on programs where you are authorized — HackerOne, Bugcrowd, Intigriti, or private programs you have permission for.

---

## 👨‍💻 About the Creator

<div align="center">

**Jagdeep Singh**  
Cybersecurity Educator | Active Bug Bounty Hunter

🏆 CEH | CRTP | PWPA  
🐛 Active on HackerOne • Bugcrowd • Intigriti  
🎯 Top 4% on TryHackMe  
📺 Teaching cybersecurity in Hinglish for Indian beginners

</div>

### 🤝 Connect & Follow

<div align="center">

[![YouTube](https://img.shields.io/badge/YouTube-Subscribe%20Now-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@encrypticle)
[![Instagram](https://img.shields.io/badge/Instagram-%40encrypticle-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/encrypticle)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Encrypticle-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/company/encrypticle)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/RR42FjT4)
[![Website](https://img.shields.io/badge/Website-encrypticle.com-556B2F?style=for-the-badge&logo=firefox&logoColor=white)](https://encrypticle.com)

</div>

---

## ⭐ Support This Project

This tool is free and open source. If it helped you:

- ⭐ **Star this repo** — helps others in the community discover it
- 📺 **[Subscribe to Encrypticle](https://youtube.com/@encrypticle)** — free cybersecurity content in Hinglish
- 🐛 **Share your findings** — join our [Discord](https://discord.com/invite/RR42FjT4) and show what you found
- 🔄 **Share this repo** — help more Indian hunters get access to proper tools

---

## 🤝 Contributing

PRs are welcome! If you find a bug or want to add a feature:

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'Add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute with attribution.

---

<div align="center">

**Built with ❤️ by [Jagdeep Singh](https://instagram.com/encrypticle)**  
**For the Indian cybersecurity community 🇮🇳**

*Decode. Discover. Defend.*

</div>
