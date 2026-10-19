# -*- coding: utf-8 -*-
"""lib_nominate —— s8 提名层（AI 域版 db_scan，s8_spec.md §5）。

在 LLM 之前对 README 清理文做全文（不截断）正则扫描，产出候选清单：
  {类别: [{term, line, q}]}
可见窗口只影响"模型看多少"，不影响"提名到多少"——支持矩阵深处的行
（窗口外）照样被提名，模型可指认（引证规则允许指认候选清单标注的窗口外行）。

六张词表（+形态检测走文件级判断，不入候选清单）：
  providers  模型供应商 → model_dep / ecosystem_compat 裁决
  install    安装信号   → deploy / install_friction
  hardware   硬件数字   → hardware（只认带数字的原话）
  dual       双许可声明 → license_risk 的 dual 覆盖
  depre      弃坑声明   → maturity 信号（锚定项目主语，裸词全是误报——dbhub 金标实测）
  products   知名产品   → alternative_to / competitors_mentioned

词表设计原则（db_scan 先例）：词边界防短词误命中；同义写法显式列出
（vllm/vLLM、llama.cpp/llama-cpp/gguf）；拿不准的不收——漏提名靠 LLM
自由抽取兜底，误提名浪费裁决预算。

用法：python lib_nominate.py 某文件.md   # 自测提名结果
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

from lib_rm_clean import clean_readme, number_lines

MAX_QUOTES_PER_TERM = 5          # 前 3 条通常在文首；深处的行（窗口外漏判主因）靠后 2 条兜住
QUOTE_MAX = 260

# ---------------- ① providers：模型供应商 ----------------
PROVIDER_VOCAB = {
    "openai":    ["openai", "chatgpt", "gpt-4", "gpt-4o", "gpt-4.1", "gpt-5", "o3", "davinci"],
    "anthropic": ["anthropic", "claude"],
    "deepseek":  ["deepseek"],
    "google":    ["gemini", "vertex ai", "google ai studio", "palm"],
    "groq":      ["groq"],
    "mistral":   ["mistral", "mixtral"],
    "xai":       ["xai", "grok"],
    "cohere":    ["cohere"],
    "together":  ["together.ai", "together ai"],
    "openrouter": ["openrouter"],
    "azure":     ["azure openai", "azure openai"],
    "bedrock":   ["bedrock"],
    "ollama":    ["ollama"],
    "llama.cpp": ["llama.cpp", "llama-cpp", "llamacpp", "gguf"],
    "vllm":      ["vllm"],
    "local-weights": ["hugging face", "huggingface", "hf hub", "transformers",
                      "local model", "local llm", "本地模型", "本地部署模型"],
    "cpu-infer": ["llamafile", "onnxruntime", "openvino"],
}

# ---------------- ② install：安装信号（模式正则，i 大小写不敏感） ----------------
INSTALL_PATTERNS = [
    ("pypi",    r"pip3? install|poetry add|uv (?:add|pip install)|pypi"),
    ("npm",     r"npm (?:i|install|\bintall)|yarn add|pnpm (?:i|add)|npx "),
    ("docker",  r"docker(?:-compose)? (?:run|compose|pull|build)|docker-compose up|dockerfile"),
    ("cargo",   r"cargo install|crates\.io"),
    ("go",      r"go install"),
    ("brew",    r"brew install|homebrew"),
    ("helm",    r"helm (?:install|repo add|chart)"),
    ("binary",  r"download[^\n]{0,60}\.(?:exe|dmg|zip|appimage|deb|pkg|msi)|releases? page"
                r"|\.(?:exe|dmg|appimage|msi|pkg)\b"),   # 1.3：清理已剥 URL，裸扩展名安全（FMCL .exe 表格行教训）
    ("source",  r"git clone|build from source|从源码"),
    ("colab",   r"colab|google colab"),
]

# ---------------- ②b sysdep：系统级依赖（install_friction 程序判定原料，1.3） ----------------
SYSDEP_PATTERNS = [
    ("JDK",    r"(?:java|jdk)\s*\d|openjdk|java\s+\d+\+"),
    ("GDAL",   r"\bgdal\b"),
    (".NET",   r"\.net\s*\d|\bdotnet\b"),
    ("CUDA",   r"\bcuda\b|cu1[12]\d"),
    ("ffmpeg", r"\bffmpeg\b"),
    ("GPU驱动", r"nvidia driver|显卡驱动"),
]

# ---------------- ②c compile：编译步骤信号（1.4 扩充，补偿模型回退移除） ----------------
COMPILE_PATTERNS = [
    r"cmake\s|make install|make -j|\bninja\b|cargo build --release|"
    r"setup\.py build_ext|从源码编译|需要编译|compile from source|"
    r"build-essential|\bg\+\+\s|\bgcc\s|xcodebuild|\bmsbuild\b|编译安装",
]

# ---------------- ③ hardware：硬件数字（term=命中原文片段） ----------------
HARDWARE_PATTERNS = [
    (r"\d+(?:\.\d+)?\s*(?:gb|g|gib|mb|mib)\s*(?:vram|gpu\s+memory|显存)", "vram"),
    (r"(?:vram|gpu\s+memory|显存)[^\n]{0,16}?\d+(?:\.\d+)?\s*(?:gb|g|gib)", "vram"),
    (r"\d+(?:\.\d+)?\s*(?:gb|g|gib)\s*(?:ram|内存|of\s+ram)", "ram"),
    (r"(?:ram|内存)[^\n]{0,16}?\d+(?:\.\d+)?\s*(?:gb|g|gib)", "ram"),
    (r"cpu[- ]only|runs on cpu|无需\s*gpu|不需要\s*gpu|no\s+gpu\s+required", "cpu-ok"),
]

# ---------------- ④ dual：双许可/商业授权声明 ----------------
DUAL_PATTERNS = [
    r"dual[- ]?licen[cs]ed", r"dual[- ]?licen[cs]e",
    r"commercial licen[cs]e", r"enterprise licen[cs]e",
    r"licen[cs]e[^\n]{0,40}commercial", r"commercial[^\n]{0,20}licen[cs]e",
    r"商业授权", r"商业许可", r"企业版授权", r"购买商业",
]

# ---------------- ⑤ depre：弃坑声明（锚定项目主语） ----------------
# dbhub 金标实测：裸 "deprecated" 全是误报（某依赖 deprecated ≠ 项目死）
DEPRE_PATTERNS = [
    r"(?:this|the) (?:project|repo(?:sitory)?|library|package) (?:is |has been |was |is now )?"
    r"(?:deprecated|discontinued|no longer maintained|unmaintained|in maintenance mode|archived)",
    r"no longer (?:maintained|actively developed|under (?:active )?development)",
    r"(?:project|repo) (?:has been )?archived",
    r"停止维护", r"不再维护", r"已归档", r"已停止",
]

# ---------------- ⑥ products：知名商业产品（替代/竞品提名） ----------------
PRODUCT_VOCAB = {
    "Notion AI":     ["notion ai", "notionai"],
    "Midjourney":    ["midjourney"],
    "GitHub Copilot": ["github copilot", "copilot"],
    "Claude Code":   ["claude code"],
    "Cursor":        ["cursor"],
    "ChatGPT":       ["chatgpt"],           # 与 providers.openai 重叠属正常（不同裁决目的）
    "Perplexity":    ["perplexity"],
    "Jasper":        ["jasper"],
    "Stable Diffusion": ["stable diffusion", "sd3"],
    "DALL-E":        ["dall-e", "dall·e", "dalle"],
    "Suno":          ["suno"],
    "Runway":        ["runway"],
    "v0":            ["v0 by vercel", "vercel v0"],
    "Lovable":       ["lovable"],
    "Windsurf":      ["windsurf"],
    "Devin":         ["devin"],
    "Hugging Face":  ["hugging face", "huggingface"],
    "Vercel AI SDK": ["ai sdk"],
    "LangChain":     ["langchain"],
    "Dify":          ["dify"],
    "Coze":          ["coze"],
    "文心一言":       ["文心一言", "ernie"],
    "通义千问":       ["通义千问", "qwen"],
    "Kimi":          ["kimi"],
    "豆包":          ["豆包", "doubao"],
}


def _ascii_pat(term: str) -> re.Pattern:
    """ASCII 词带边界（短词匹配不了带后缀的写法）；中文直接匹配。db_scan 同款。"""
    t = re.escape(term)
    if term.isascii():
        t = r"(?<![a-z0-9])" + t + r"(?![a-z0-9])"
    return re.compile(t)


# 预编译：providers/products 按词条；install/hardware/dual/depre 按模式
_PROVIDERS_C = {prov: _ascii_pat(t) for prov, terms in PROVIDER_VOCAB.items() for t in terms}
_PRODUCTS_C = {prod: _ascii_pat(t) for prod, terms in PRODUCT_VOCAB.items() for t in terms}
_INSTALL_C = [(label, re.compile(pat, re.I)) for label, pat in INSTALL_PATTERNS]
_HARDWARE_C = [(re.compile(pat, re.I), kind) for pat, kind in HARDWARE_PATTERNS]
_DUAL_C = [re.compile(p, re.I) for p in DUAL_PATTERNS]
_DEPRE_C = [re.compile(p, re.I) for p in DEPRE_PATTERNS]
_SYSDEP_C = [(label, re.compile(pat, re.I)) for label, pat in SYSDEP_PATTERNS]
_COMPILE_C = [re.compile(p, re.I) for p in COMPILE_PATTERNS]


def _dedup_quote(q: str) -> str:
    return re.sub(r"\s+", " ", q).strip()[:QUOTE_MAX]


def scan_lines(lines: list[tuple[int, str]]) -> dict:
    """全文扫描清理文行（[(行号, 行文本)]），返回六类候选清单。"""
    out: dict[str, list[dict]] = {k: [] for k in
                                  ("providers", "install", "hardware", "dual", "depre", "products",
                                   "sysdep", "compile")}

    def _add(cat: str, term: str, line: int, q: str):
        if len([c for c in out[cat] if c["term"] == term]) >= MAX_QUOTES_PER_TERM:
            return
        dq = _dedup_quote(q)
        if not any(c["term"] == term and c["q"] == dq for c in out[cat]):
            out[cat].append({"term": term, "line": line, "q": dq})

    for no, ln in lines:
        low = ln.lower()
        # providers
        for prov, pat in _PROVIDERS_C.items():
            if pat.search(low):
                _add("providers", prov, no, ln)
        # install
        for label, pat in _INSTALL_C:
            if pat.search(ln):
                _add("install", label, no, ln)
        # hardware（term=命中片段本身，带数字才算数）
        for pat, kind in _HARDWARE_C:
            m = pat.search(ln)
            if m:
                _add("hardware", m.group(0).strip(), no, ln)
        # dual
        for pat in _DUAL_C:
            if pat.search(ln):
                _add("dual", "dual/commercial", no, ln)
        # depre
        for pat in _DEPRE_C:
            if pat.search(ln):
                _add("depre", "deprecation", no, ln)
        # products
        for prod, pat in _PRODUCTS_C.items():
            if pat.search(low):
                _add("products", prod, no, ln)
        # sysdep / compile（1.3：install_friction 程序判定原料）
        for label, pat in _SYSDEP_C:
            if pat.search(ln):
                _add("sysdep", label, no, ln)
        for pat in _COMPILE_C:
            if pat.search(ln):
                _add("compile", "compile", no, ln)
    return {k: v for k, v in out.items() if v}


def detect_form(fn: str, raw_text: str, cleaned: str) -> str | None:
    """形态检测（分层路由用，不入候选清单）：
    awesome 清单 / 超大表格清单 → C 层规则解析，不烧 LLM。"""
    base = fn.rsplit("/", 1)[-1].rsplit("__", 1)[-1].lower()
    if base.startswith("awesome"):
        return "awesome-name"
    if len(raw_text) > 60_000:
        table_lines = sum(1 for ln in cleaned.split("\n") if ln.strip().startswith("|"))
        total = max(len(cleaned.split("\n")), 1)
        if total > 150 and table_lines / total > 0.25:
            return "huge-table"
    return None


def scan_readme_text(text: str) -> dict:
    """一步到位：清理 → 编号 → 扫描。"""
    return scan_lines(number_lines(clean_readme(text)))


if __name__ == "__main__":   # 自测：python lib_nominate.py 某文件.md
    src = Path(sys.argv[1]).read_text(encoding="utf-8", errors="ignore")
    cleaned = clean_readme(src)
    cands = scan_lines(number_lines(cleaned))
    import json
    print(f"清理 {len(src)} -> {len(cleaned)} 字；提名：")
    print(json.dumps(cands, ensure_ascii=False, indent=1)[:3000])
