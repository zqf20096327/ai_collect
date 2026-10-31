<div align="center"><img src="docs/logo.gif" width="160" height="160" alt="瞾 — Shuo Zhao" style="border-radius:50%;"/>
</div>

# Aut_Sci_Download

[English](#features) | [中文](#中文说明)

Download academic papers from 8 sources via simple Python CLI scripts. Works standalone or as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill.

## Features

| Source | Auth | Coverage |
|--------|------|----------|
| **Elsevier / ScienceDirect** | API Key (free) | Elsevier journals |
| **Springer Nature** | API Key (free) | Springer/Nature OA articles |
| **IEEE Xplore** | API Key (free) | IEEE/IET journals & conferences |
| **arXiv** | None | Physics, CS, Math preprints |
| **Unpaywall** | Email only | OA versions of any DOI |
| **Semantic Scholar** | None | Cross-database OA PDF aggregation |
| **PubMed Central** | None | Biomedical OA articles |
| **CNKI (知网)** | University account | Chinese journals & theses |

## Quick Start

```bash
git clone https://github.com/ShZhao27208/aut-sci-download.git
cd aut-sci-download
pip install -r requirements.txt
```

Configure API keys (auto-creates `~/.aut-sci-download/.env`):

```bash
cd scripts
python -c "from config import update_config; update_config('elsevier_api_key', 'YOUR_KEY')"
python -c "from config import update_config; update_config('springer_api_key', 'YOUR_KEY')"
python -c "from config import update_config; update_config('unpaywall_email', 'you@university.edu')"
```

Download a paper:

```bash
python elsevier_download.py "10.1016/j.cell.2024.01.029"
python arxiv_download.py "2301.07041"
```

## Usage

All scripts are in the `scripts/` directory. Each accepts a DOI, identifier, or search query.

### Elsevier (DOI: 10.1016/...)

```bash
python elsevier_download.py "10.1016/j.cell.2024.01.029"
python elsevier_download.py --test-key
```
### Springer Nature (DOI: 10.1038/..., 10.1007/...)

```bash
python springer_download.py "10.1038/s41586-024-07487-w"
python springer_download.py --test-key
```

### IEEE Xplore (DOI: 10.1109/...)

```bash
python ieee_download.py "10.1109/ACCESS.2023.1234567"
python ieee_download.py --search "transformer neural network" --limit 5
```

### arXiv (no key needed)

```bash
python arxiv_download.py "2301.07041"
python arxiv_download.py --search "large language model" --limit 5
```

### Unpaywall (any DOI → OA version)

```bash
python unpaywall_download.py "10.1038/s41586-024-07487-w"
```

### Semantic Scholar (DOI or arXiv ID → OA PDF)

```bash
python semantic_scholar_download.py "10.1038/s41586-024-07487-w"
python semantic_scholar_download.py "2301.07041"
python semantic_scholar_download.py --search "CRISPR" --limit 5
```

### PubMed Central (PMCID / PMID / DOI)

```bash
python pubmed_download.py "PMC7654321"
python pubmed_download.py --search "covid vaccine mRNA" --limit 5
```

### CNKI 知网 (FSSO or WebVPN)

```bash
python cnki_download.py set-mode fsso          # Use FSSO (default, recommended)
python cnki_download.py status                 # Show config & login instructions
python cnki_download.py check                  # Verify session cookies
python cnki_download.py search "深度学习" --limit 10
python cnki_download.py download ZGTB202401001 --dbcode CJFD
```

## Configuration

### API Keys (.env)

All secrets are stored in `~/.aut-sci-download/.env` (auto-created on first use):

| Variable | Source | How to get |
|----------|--------|------------|
| `ELSEVIER_API_KEY` | Elsevier | https://dev.elsevier.com/ |
| `SPRINGER_API_KEY` | Springer Nature | https://dev.springernature.com/ |
| `IEEE_API_KEY` | IEEE Xplore | https://developer.ieee.org/ |
| `UNPAYWALL_EMAIL` | Unpaywall | Any valid email |
| `NCBI_API_KEY` | PubMed/NCBI | https://www.ncbi.nlm.nih.gov/account/settings/ |

### General Settings (config.json)

Non-secret settings are stored in `~/.aut-sci-download/config.json`:

```bash
# Set output directory
python -c "from config import update_config; update_config('output_dir', '/path/to/papers')"

# Set HTTP proxy
python -c "from config import update_config; update_config('proxy', 'http://127.0.0.1:7897')"
```

### CNKI Access

CNKI requires a university account. Two access modes are supported:

- **FSSO (default)**: Login at https://fsso.cnki.net via institutional SSO, then export cookies to `~/.aut-sci-download/fsso_cookies.json`
- **WebVPN**: Login at your university's WebVPN portal, export cookies to `~/.aut-sci-download/webvpn_cookies.json`

Use a browser extension like [EditThisCookie](https://www.editthiscookie.com/) to export cookies as JSON.

## Claude Code Integration

This project includes a Claude Code skill definition at `.claude/skills/sci-download.md`. To use it:

1. Clone this repo into your skills directory
2. When you ask Claude Code to "download a paper" or provide a DOI, the skill auto-triggers
3. Claude Code will run the appropriate script and manage configuration for you

## Routing Logic

The skill automatically picks the best source based on your input:

```
DOI 10.1016/...          → Elsevier
DOI 10.1038/... 10.1007/ → Springer Nature
DOI 10.1109/...          → IEEE Xplore
arXiv ID (2301.xxxxx)    → arXiv
PMCID / PMID             → PubMed Central
Chinese keywords / 知网   → CNKI
Other DOIs               → Unpaywall → Semantic Scholar (waterfall)
```

## License

[MIT](LICENSE)

---

# 中文说明

通过 Python CLI 脚本从 8 个数据源下载学术论文 PDF。可独立使用，也可作为 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill 自动调用。

## 支持的数据源

| 数据源 | 认证方式 | 覆盖范围 |
|--------|----------|----------|
| **Elsevier / ScienceDirect** | API Key（免费） | Elsevier 旗下期刊 |
| **Springer Nature** | API Key（免费） | Springer/Nature 开放获取论文 |
| **IEEE Xplore** | API Key（免费） | IEEE/IET 期刊和会议 |
| **arXiv** | 无需 | 物理、计算机、数学预印本 |
| **Unpaywall** | 仅需邮箱 | 任意 DOI 的开放获取版本 |
| **Semantic Scholar** | 无需 | 跨库 OA PDF 聚合 |
| **PubMed Central** | 无需 | 生物医学开放获取论文 |
| **CNKI（知网）** | 高校账号 | 中文期刊、学位论文 |

## 快速开始

```bash
git clone https://github.com/ShZhao27208/aut-sci-download.git
cd aut-sci-download
pip install -r requirements.txt
```

配置 API Key（首次运行自动创建 `~/.aut-sci-download/.env`）：

```bash
cd scripts
python -c "from config import update_config; update_config('elsevier_api_key', '你的KEY')"
python -c "from config import update_config; update_config('springer_api_key', '你的KEY')"
python -c "from config import update_config; update_config('unpaywall_email', 'you@university.edu')"
```

下载论文：

```bash
python elsevier_download.py "10.1016/j.cell.2024.01.029"
python arxiv_download.py "2301.07041"
```

## 各数据源用法

所有脚本在 `scripts/` 目录下，接受 DOI、标识符或搜索关键词。

```bash
# Elsevier（DOI: 10.1016/...）
python elsevier_download.py "10.1016/j.cell.2024.01.029"

# Springer Nature（DOI: 10.1038/..., 10.1007/...）
python springer_download.py "10.1038/s41586-024-07487-w"

# IEEE Xplore（DOI: 10.1109/...）
python ieee_download.py --search "transformer neural network" --limit 5

# arXiv（无需 Key）
python arxiv_download.py "2301.07041"
python arxiv_download.py --search "large language model" --limit 5

# Unpaywall（任意 DOI → 查找 OA 版本）
python unpaywall_download.py "10.1038/s41586-024-07487-w"

# Semantic Scholar（DOI 或 arXiv ID → OA PDF）
python semantic_scholar_download.py "10.1038/s41586-024-07487-w"

# PubMed Central（PMCID / PMID / DOI）
python pubmed_download.py "PMC7654321"
python pubmed_download.py --search "covid vaccine mRNA" --limit 5

# 知网 CNKI（FSSO 或 WebVPN）
python cnki_download.py status                     # 查看配置和登录说明
python cnki_download.py search "深度学习" --limit 10
python cnki_download.py download ZGTB202401001
```

## 配置说明

### API Key（.env 文件）

所有密钥存储在 `~/.aut-sci-download/.env`（首次使用自动创建模板）：

| 变量 | 来源 | 获取方式 |
|------|------|----------|
| `ELSEVIER_API_KEY` | Elsevier | https://dev.elsevier.com/ |
| `SPRINGER_API_KEY` | Springer | https://dev.springernature.com/ |
| `IEEE_API_KEY` | IEEE | https://developer.ieee.org/ |
| `UNPAYWALL_EMAIL` | Unpaywall | 任意有效邮箱 |
| `NCBI_API_KEY` | PubMed | https://www.ncbi.nlm.nih.gov/account/settings/ |

### 通用设置（config.json）

```bash
# 设置下载目录
python -c "from config import update_config; update_config('output_dir', 'D:/papers')"

# 设置代理
python -c "from config import update_config; update_config('proxy', 'http://127.0.0.1:7897')"
```

### 知网访问

知网需要高校账号，支持两种模式：

- **FSSO（默认推荐）**：浏览器打开 https://fsso.cnki.net → 选择机构 → CAS 登录 → 导出 cookie 到 `~/.aut-sci-download/fsso_cookies.json`
- **WebVPN（备选）**：登录学校 WebVPN → 导出 cookie 到 `~/.aut-sci-download/webvpn_cookies.json`

推荐使用 [EditThisCookie](https://www.editthiscookie.com/) 浏览器扩展导出 JSON 格式 cookie。

## 智能路由

根据输入自动选择最佳数据源：

```
DOI 10.1016/...          → Elsevier
DOI 10.1038/... 10.1007/ → Springer Nature
DOI 10.1109/...          → IEEE Xplore
arXiv ID (2301.xxxxx)    → arXiv
PMCID / PMID             → PubMed Central
中文关键词 / 知网         → CNKI
其他 DOI                 → Unpaywall → Semantic Scholar（瀑布式尝试）
```

## Claude Code 集成

本项目包含 Claude Code skill 定义（`.claude/skills/sci-download.md`）：

1. 将本仓库 clone 到你的工作目录
2. 当你对 Claude Code 说"下载论文"或提供 DOI 时，skill 自动触发
3. Claude Code 会自动运行对应脚本并管理配置

## 许可证

[MIT](LICENSE)
