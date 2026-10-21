# -*- coding: utf-8 -*-
"""s8_interpret —— AI 解读层 worker（s8_spec.md v2，ver=1 行号指认架构）。

流程：清理(lib_rm_clean) → 提名(lib_nominate) → 窗口 → 提示词(含 few-shot)
   → AIClient(OpenAI 兼容, 环境变量 AI_*) → 解析 → 六道闸 → 规则合成 → 缓存/runlog。

判定权分配（spec §7）：license_risk 元数据权威；model_dep/deploy/hardware/
install_friction 程序组装；maturity 模型判+程序对照（降级不覆盖）；ai_role 模型直判。

用法：
  python s8_interpret.py --selftest                # few-shot 卡过闸自测（不烧 API）
  python s8_interpret.py --dry-run --max-items 5   # 只构建提示词并打印统计（不烧 API）
  python s8_interpret.py --trial 500               # 试批：按 star 降序取 500 条待解读
  python s8_interpret.py --max-items 50            # 增量：sha 变更的全量（star 降序）

缓存两层（spec §17）：state/s8_cache.json（sha→卡片，跨仓同内容共用）
                    state/s8_state.json（fn→sha/状态）
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests

from lib_rm_clean import clean_readme, number_lines, visible_line_limit
from lib_nominate import scan_lines, detect_form
import lib_store
from lib_store import load_pool, atomic_write_json
import lib_card_store as cstore

ROOT = Path(__file__).resolve().parent
READMES = lib_store.READMES      # 只读输入跟 lib_store 的 FACTORY_ROOT 走
CACHE = ROOT / "state" / "s8_cache.json"
ISTATE = ROOT / "state" / "s8_state.json"
LOGDIR = ROOT / "state" / "logs"
FEWSHOT = ROOT / "s8_fewshot.json"

VER = 1                 # 架构代际：1=行号指认
PROMPT_VER = "1.4"      # 1.4：install_friction/deploy 全程序化（去 docker_available/
                         # needs_compile/system_deps/desktop_builds 模型回退，一致闸收尾）
WINDOW_CHARS = 12000    # 可见窗口（清理文）

log = logging.getLogger("s8")

# ============================================================
# 环境与 AI 客户端（自 dbhub interpret.py 移植，协议不变）
# ============================================================

def _load_env():
    f = ROOT / ".env"
    if f.is_file():
        for ln in f.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, _, v = ln.partition("=")
                os.environ.setdefault(k.strip(), v.strip())


class AIClient:
    def __init__(self, deadline: float | None = None):
        _load_env()
        self.key = os.environ.get("AI_API_KEY")
        self.base = (os.environ.get("AI_BASE_URL") or "https://api.deepseek.com").rstrip("/")
        if self.base.endswith("/chat/completions"):
            self.base = self.base.rsplit("/chat/completions", 1)[0]
        self.model = os.environ.get("AI_MODEL") or "deepseek-chat"
        self.deadline = deadline
        if not self.key:
            raise SystemExit("AI_API_KEY 未配置：写入 ai_collect/.env")
        # harness 配置（1.3）：记入卡片 trust.model_harness，换模型后可定位该重审的卡
        self.max_tokens = int(os.environ.get("AI_MAX_TOKENS", "24000"))
        self.seed = os.environ.get("AI_SEED")
        self.thinking_mode = os.environ.get("AI_THINKING", "disabled")
        self.harness = {"model": self.model, "thinking": self.thinking_mode,
                        "max_tokens": self.max_tokens, "seed": self.seed}

    def build_body(self, prompt: str, thinking: dict) -> dict:
        body = {"model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "thinking": thinking,
                "response_format": {"type": "json_object"},
                "temperature": 0, "max_tokens": self.max_tokens}
        if self.seed:
            body["seed"] = int(self.seed)
        return body

    def chat(self, prompt: str, timeout: int = 300) -> dict:
        tk = os.environ.get("AI_THINKING", "disabled")
        thinking = ({"type": "enabled", "budget_tokens": int(tk)} if tk.isdigit()
                    else {"type": tk})
        # harness 工程（1.3）：思考计入 max_tokens 且 GLM 5.x 对 disabled 遵守不稳——
        # 预算必须给足（AI_MAX_TOKENS 默认 24000），否则思考烧穿预算正文为空
        # （dbhub 944 条拒收同根因）。seed 端点接受但不保证复现，聊胜于无。
        attempt = 0
        quota_waits = 0
        t_call = time.time()
        while True:
            try:
                r = requests.post(
                    f"{self.base}/chat/completions",
                    headers={"Authorization": f"Bearer {self.key}"},
                    json=self.build_body(prompt, thinking),
                    timeout=timeout)
            except requests.exceptions.Timeout:
                if attempt >= 2:
                    raise
                attempt += 1
                log.warning("读超时，重试（第 %d 次）", attempt)
                continue
            if r.status_code == 429 and "1113" in r.text:
                quota_waits += 1
                if quota_waits > 33:
                    raise RuntimeError("额度等待超 5.5 小时仍报 1113，放弃本条")
                if self.deadline and time.time() + 600 > self.deadline:
                    raise RuntimeError("额度耗尽，等待将超墙钟预算，本条放弃")
                log.warning("额度耗尽，10 分钟后探测重试（第 %d 次）", quota_waits)
                time.sleep(600)
                continue
            if r.status_code == 429 or r.status_code >= 500:
                if attempt >= 5:
                    raise RuntimeError(f"重试耗尽（最后状态码 {r.status_code}）")
                time.sleep(min(2 ** attempt * 3, 60))
                attempt += 1
                continue
            if r.status_code == 400:
                raise RuntimeError(f"400: {r.text[:150]}")
            r.raise_for_status()
            ch = r.json()["choices"][0]
            msg = ch.get("message") or {}
            return {"content": msg.get("content") or "",
                    "reasoning": msg.get("reasoning_content") or "",
                    "finish": ch.get("finish_reason") or "",
                    "secs": round(time.time() - t_call, 2),
                    "tries": attempt + quota_waits + 1}


# ============================================================
# 中立性：禁词表（dbhub 移植 + AI 域补充）
# ============================================================

_BANNED_CN = [
    "最强", "最快", "颠覆", "必将", "震惊", "碾压", "革命性", "王者",
    "神器", "吊打", "强大", "优秀", "出色", "好用", "漂亮", "完美", "卓越",
    "高效", "高性能", "优雅", "惊艳", "史诗", "炸裂",
    "最先进", "最流行", "最完善", "最强大", "地表最强",
    "顶尖", "顶级", "无可替代", "业界领先", "遥遥领先", "大幅", "显著",
    "优于", "超越", "碾压式", "将会取代", "必将取代", "领先于", "完胜",
]
_BANNED_EN = [
    r"\bbest\b", r"\bfastest\b", r"\bultimate\b", r"\brevolutionar\w+",
    r"\brevolutionize\b", r"\bgreatest\b", r"\bleading\b",
    r"\bunmatched\b", r"\bunrivaled\b", r"\bstate-of-the-art\b",
    r"\bcutting-edge\b", r"\bgame-chang\w*", r"\bworld-class\b",
    r"\bamazing\b", r"\bbeautiful\b", r"\belegant\w*",
    r"\bexcellent\b", r"\bimpressive\b", r"\bstunning\b", r"\bpowerful\b",
    r"\bmust-have\b", r"\boutperforms?\b", r"\bcrushes\b",
    r"\bsuperior\b", r"\bbetter than\b", r"\bwill replace\b", r"\bpoised to\b",
    r"\bincredibly\b", r"\bworld's (?:first|best|fastest)\b", r"#1",
    r"\bblazing\w*\b", r"\bseamless\w*\b",
]
BANNED_RE = re.compile("|".join(_BANNED_CN + _BANNED_EN), re.I)
TEXT_FIELDS = ["one_liner", "review"]


def neutral_violations(facts: dict) -> list[str]:
    hits: list[str] = []

    def scan(txt, path):
        if txt:
            m = BANNED_RE.search(txt)
            if m:
                hits.append(f"{path}:『{m.group(0)}』")

    ident = facts.get("identity") or {}
    scan(ident.get("one_liner"), "one_liner")
    scan(ident.get("review"), "review")
    for h in ident.get("highlights") or []:
        scan(h, "highlights")
    for u in ident.get("use_cases") or []:
        scan(u, "use_cases")
    return hits


def neutral_scrub(facts: dict) -> list[str]:
    """软放行处置：禁词字段置空、违规列表项删除，返回处置记录。"""
    acted: list[str] = []
    ident = facts.setdefault("identity", {})

    def scrub_str(key):
        v = ident.get(key)
        if isinstance(v, str) and v and BANNED_RE.search(v):
            m = BANNED_RE.search(v)
            ident[key] = ""
            acted.append(f"{key}:『{m.group(0) if m else '?'}』置空")

    scrub_str("one_liner")
    scrub_str("review")
    for key in ("highlights", "use_cases"):
        lst = ident.get(key)
        if isinstance(lst, list):
            kept = [it for it in lst if not (isinstance(it, str) and BANNED_RE.search(it))]
            if len(kept) != len(lst):
                acted.append(f"{key} 删条x{len(lst) - len(kept)}")
                ident[key] = kept
    return acted


# ============================================================
# 枚举与别名归一（保守：只收大小写/同义改写）
# ============================================================

AI_ROLE = {"ai-native", "ai-ecosystem", "ai-enhanced", "ai-knowledge"}
MAINTAINER = {"individual", "team", "company", "university", "media"}
CONF = {"high", "mid", "low"}
REL_STD = {"support", "compat", "mention", "none"}       # providers/install/hardware
REL_PROD = {"alternative", "competitor", "mention", "none"}

_ALIAS = {
    "ai_role": {"AI-Native": "ai-native", "AI-native": "ai-native", "native": "ai-native",
                "AI-Ecosystem": "ai-ecosystem", "ecosystem": "ai-ecosystem",
                "AI-Enhanced": "ai-enhanced", "enhanced": "ai-enhanced",
                "AI-Knowledge": "ai-knowledge", "knowledge": "ai-knowledge",
                "清单": "ai-knowledge"},
    "maintainer_type": {"个人": "individual", "团队": "team", "公司": "company",
                        "高校": "university", "大学": "university", "媒体": "media",
                        "Individual": "individual", "Company": "company"},
    "rel": {"Support": "support", "Compat": "compat", "Mention": "mention",
            "None": "none", "Alternative": "alternative", "Competitor": "competitor",
            "used": "mention", "integrated": "support"},
    "confidence": {"High": "high", "Mid": "mid", "Low": "low",
                   "medium": "mid", "高": "high", "中": "mid", "低": "low"},
}


def _extract_enum(val, enum: tuple) -> str | None:
    """模糊救回：模型偶发输出带注释的枚举值（如 'high（证据充分）'、'ai-native 库'），
    从字符串里提取首个合法枚举词。试批拒收帕累托头两名（10+7 条）的根因。"""
    if isinstance(val, str):
        low = val.lower()
        for e in enum:
            if e in low:
                return e
    return None


def normalize_enums(facts: dict) -> int:
    n = 0
    op = facts.setdefault("open", {})
    for key, enum in (("ai_role", tuple(AI_ROLE)), ("maintainer_type", tuple(MAINTAINER))):
        v = op.get(key)
        fixed = _ALIAS.get(key, {}).get(v)
        if fixed and fixed != v:
            op[key] = fixed
            n += 1
        if op.get(key) not in enum and op.get(key) is not None:
            rescued = _extract_enum(op.get(key), enum)
            if rescued:
                op[key] = rescued
                n += 1
            else:
                op[key] = None      # 归一后仍非法 → 置空让校验报违规
    aud = facts.setdefault("audit", {})
    if aud.get("confidence") in _ALIAS["confidence"]:
        aud["confidence"] = _ALIAS["confidence"][aud["confidence"]]
        n += 1
    if aud.get("confidence") not in CONF:
        rescued = _extract_enum(aud.get("confidence"), ("high", "mid", "low"))
        if rescued:
            aud["confidence"] = rescued
            n += 1
    verd = facts.setdefault("verdicts", {})
    for cat in ("providers", "install", "hardware", "products"):
        for v in verd.get(cat) or []:
            if not isinstance(v, dict):        # 模型偶发输出字符串项，归一跳过交校验丢弃
                continue
            r = v.get("rel")
            if r in _ALIAS["rel"]:
                v["rel"] = _ALIAS["rel"][r]
                n += 1
    return n


# ============================================================
# 上下文构建（清理/提名/窗口/提示词）
# ============================================================

def sha_of(raw: str) -> str:
    return hashlib.sha1(raw.encode("utf-8", "ignore")).hexdigest()[:12]


def readme_path(fn: str) -> Path:
    return READMES / (fn.replace("/", "__") + ".md")


def build_context(fn: str, rec: dict) -> dict:
    raw = readme_path(fn).read_text(encoding="utf-8", errors="ignore")
    cleaned = clean_readme(raw)
    numbered = number_lines(cleaned)
    vis_limit = visible_line_limit(numbered, WINDOW_CHARS)
    visible = {no: ln for no, ln in numbered if no <= vis_limit}
    cands = scan_lines(numbered)
    form = detect_form(fn, raw, cleaned)
    # 窗口外标记：候选行不在可见集内的标（窗口外）——模型仍可指认
    cand_lines = {i["line"] for items in cands.values() for i in items}
    return {"fn": fn, "rec": rec, "raw": raw, "cleaned": cleaned,
            "numbered": dict(numbered), "visible": visible, "vis_limit": vis_limit,
            "cands": cands, "cand_lines": cand_lines, "form": form,
            "sha": sha_of(raw), "in_raw_chars": len(raw), "in_clean_chars": len(cleaned)}


NEUTRALITY_CONTRACT = """【中立性契约——违反即拒收】
- 只陈述 README 可验证的事实：它是什么、做什么、给谁用、怎么安装运行
- 禁止：评价词（强大/优秀/perfect…）、绝对词、对比判断（优于/超越）、预测
- 动词用事实性动词：提供/支持/读取/生成/运行；不确定的内容宁可不写"""

SCHEMA_DESC = """输出一个 JSON 对象（只输出 JSON）：
{
 "identity": {"one_liner": "≤30字：给谁+解决什么", "review": "100-150字：做什么+给谁用+关键机制/限制",
              "highlights": ["能力事实 2-4 条"], "use_cases": ["适用场景 2-4 条，用户口吻"]},
 "open": {"scenario_tags_free": ["自由打标 2-5 个"], "domain": "应用领域",
          "target_user": "开发者|科研|企业|消费者", "ai_role": "ai-native|ai-ecosystem|ai-enhanced|ai-knowledge",
          "maintainer_type": "individual|team|company|university|media", "zh_origin_signals": []},
 "verdicts": {
   "providers": [{"term": "候选词", "rel": "support|compat|mention|none", "lines": [行号]}],
   "install":   [{"term": "...", "rel": "support|compat|mention|none", "lines": [行号]}],
   "hardware":  [{"term": "命中片段", "rel": "support|mention|none", "lines": [行号]}],
   "products":  [{"term": "...", "rel": "alternative|competitor|mention|none", "lines": [行号]}],
   "dual_license": {"flag": false, "lines": []},
   "deprecation": {"flag": false, "lines": []}},
 "facts": {"desktop_builds": false, "needs_compile": false, "system_deps": [],
           "docker_available": false,
           "self_declared_early": {"flag": false, "lines": []},
           "paper_url": null, "demo_url": null},
 "audit": {"confidence": "high|mid|low", "evidence_lines": [支撑 ai_role/domain 判断的 1-3 个行号]}
}
裁决规则（按序判定，命中即停）：
ai_role——①清单/数据集/教程/论文集 → ai-knowledge；②用户直接获得模型输出（生成/识别/
  预测/转录/检测）→ ai-native；③帮助开发/运行/接入/管理模型（框架、通用推理运行时、
  API 网关、客户端、评测监控）→ ai-ecosystem；④本体是非 AI 产品、AI 是其中功能
  （去掉 AI 仍可用，如带 AI 助手的启动器）→ ai-enhanced。
  锚例（照此归类）：whisper.cpp/detectree2/stable-baselines3/opencv（模型实现与通用
  ML 库，直接产出识别/预测结果）→ ai-native；gpt_academic/khoj（面向终端用户产出
  AI 内容的应用）→ ai-native；one-api/ollama/vllm/ragas/langchain（接入/运行/评测/
  构建框架）→ ai-ecosystem。
providers——support=明确接入/专门适配（官方 SDK/专属通道）；compat=配合可用/示例中搭配/
  可选后端；mention=仅列举或对比；none=误命中（如 Minecraft 基岩版命中 bedrock）。
  候选里真实出现的本地运行时（ollama/llama.cpp/vllm）必须表态（compat 或 mention），勿跳过。
install——README 给出的【本产品】安装命令均算 support（pip/docker/git clone 源码/安装包）；
  依赖库或可选组件的安装算 mention。
hardware——support=产品自身硬件要求；mention=其他语境（如被管理对象的配置）。
products——alternative=自称替代该产品；competitor=对比/竞品关系；mention=仅提及。
system_deps 只列【运行本产品必需】的系统级依赖（JDK/GDAL/.NET/CUDA）；标注可选的不算。
dual_license flag=true 仅当声明【本产品】双许可/商业版；他人产品的许可讨论不算。
引证规则（违反即拒收）：lines 只填【行号数字数组】禁止抄原文；行号须在可见范围内，
  或属于候选清单标注（窗口外）的行；evidence_lines 必须指向支撑判断的关键行。
rel=none 或 flag=false 时 lines 可为空。review 必须包含 description 之外的信息。"""


def fmt_candidates(cands: dict, visible: dict) -> str:
    out = []
    for cat, items in cands.items():
        by_term: dict[str, list[int]] = {}
        for i in items:
            by_term.setdefault(i["term"], []).append(i["line"])
        parts = []
        for term, lines in by_term.items():
            marks = ",".join(f"{l}{'(窗外)' if l not in visible else ''}" for l in sorted(lines))
            parts.append(f"{term}[{marks}]")
        out.append(f"{cat}: {'; '.join(parts)}")
    return "\n".join(out) or "（无候选——相应 verdicts 输出空数组）"


def load_fewshot_brief() -> str:
    if not FEWSHOT.is_file():
        return ""
    data = json.loads(FEWSHOT.read_text(encoding="utf-8"))
    parts = []
    for ex in data.get("examples", []):
        f = ex["facts"]
        brief = {"identity": f["identity"], "open": f["open"],
                 "verdicts": f["verdicts"], "audit": f["audit"]}
        parts.append(f"范例 {ex['fn']}：\n{json.dumps(brief, ensure_ascii=False)}")
    return "\n\n".join(parts)


def build_prompt(ctx: dict) -> str:
    rec = ctx["rec"]
    numbered_txt = "\n".join(f"L{no}|{ln}" for no, ln in
                             sorted(ctx["visible"].items(), key=lambda x: int(x[0])))
    fewshot = load_fewshot_brief()
    return f"""你是开源 AI 生态的编目员，为选型目录做中立的结构化编目。
{NEUTRALITY_CONTRACT}

{SCHEMA_DESC}

【范例（照此口径输出）】
{fewshot}

仓库：{ctx['fn']}
描述：{(rec.get('description') or '')[:300]}
主题标签：{'、'.join((rec.get('topics') or [])[:12])}
--- README 开始（L行号|原文，可见行号 1-{ctx['vis_limit']}）---
{numbered_txt}
--- README 结束 ---

候选清单（只能对这些词表态；标注(窗外)的行不在上方展示但真实存在，可指认）：
{fmt_candidates(ctx['cands'], ctx['visible'])}"""


# ============================================================
# 校验闸门（spec §10）
# ============================================================

def extract_json(rawtxt: str) -> dict | None:
    if not rawtxt:
        return None
    txt = rawtxt.strip()
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", txt, re.S)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def _valid_lines(lines, ctx: dict) -> list[int]:
    """行号合法 = 可见窗口内 ∪ 候选行。返回通过行号（int 化）。"""
    if not isinstance(lines, list) or not lines:
        return []
    good = []
    for x in lines:
        try:
            x = int(x)
        except (TypeError, ValueError):
            continue
        if x in ctx["visible"] or x in ctx["cand_lines"]:
            good.append(x)
    return good


def _vlist(v):
    return v if isinstance(v, list) else []


def validate(facts: dict, ctx: dict) -> tuple[dict | None, list[str], list[str]]:
    """返回 (规整后事实 | None, 硬违规, 软违规)。软违规可重试后软放行。"""
    hard: list[str] = []
    soft: list[str] = []
    if not isinstance(facts, dict):
        return None, ["输出非对象"], []
    ident = facts.get("identity") or {}
    for k in ("one_liner", "review"):
        if not isinstance(ident.get(k), str) or not ident.get(k):
            hard.append(f"identity.{k} 缺失")
    for k in ("highlights", "use_cases"):
        if not isinstance(ident.get(k), list) or not ident.get(k):
            hard.append(f"identity.{k} 缺失")
    op = facts.get("open") or {}
    if op.get("ai_role") not in AI_ROLE:
        hard.append(f"ai_role 非法: {op.get('ai_role')}（合法: {'/'.join(sorted(AI_ROLE))}）")
    mt = op.get("maintainer_type")
    if mt is not None and mt not in MAINTAINER:
        hard.append(f"maintainer_type 非法: {mt}（合法: {'/'.join(sorted(MAINTAINER))} 或 null）")
    aud = facts.get("audit") or {}
    if aud.get("confidence") not in CONF:
        hard.append(f"confidence 非法: {aud.get('confidence')}（合法: {'/'.join(sorted(CONF))}）")

    # 裁决清洗：词表超集丢弃（软）；行号非法丢弃（软）
    verd = facts.setdefault("verdicts", {})
    rel_ok = {"providers": REL_STD, "install": REL_STD,
              "hardware": REL_STD, "products": REL_PROD}
    cand_terms = {cat: {i["term"] for i in _vlist(ctx["cands"].get(cat))}
                  for cat in rel_ok}
    for cat, allowed in rel_ok.items():
        keep = []
        for v in _vlist(verd.get(cat)):
            if not isinstance(v, dict):
                soft.append(f"{cat} 裁决项非对象")
                continue
            term, rel = v.get("term"), v.get("rel")
            if term not in cand_terms[cat]:
                cands_short = "/".join(sorted(cand_terms[cat])[:8])
                soft.append(f"{cat} 词不在候选: {term}（丢弃。本类候选: {cands_short}）")
                continue
            if rel not in allowed:
                hard.append(f"{cat}.{term} rel 非法: {rel}（合法: {'/'.join(sorted(allowed))}）")
                continue
            good = _valid_lines(v.get("lines"), ctx)
            if v.get("rel") not in ("none",) and not good:
                usable = sorted({i.get("line") for i in _vlist(ctx["cands"].get(cat))
                                 if i.get("term") == term and i.get("line") is not None})
                soft.append(f"{cat}.{term} 行号全无效（丢弃。该词可用行号: {usable}）")
                continue
            v["lines"] = good
            keep.append(v)
        verd[cat] = keep
    for flagcat in ("dual_license", "deprecation"):
        d = verd.get(flagcat)
        if not isinstance(d, dict):
            verd[flagcat] = {"flag": False, "lines": []}
            continue
        good = _valid_lines(d.get("lines"), ctx)
        if d.get("flag") and not good:
            soft.append(f"{flagcat} flag=true 但行号无效（降为 false）")
            d["flag"] = False
        d["lines"] = good
    fc = facts.setdefault("facts", {})
    early = fc.get("self_declared_early")
    if isinstance(early, dict):
        good = _valid_lines(early.get("lines"), ctx)
        if early.get("flag") and not good:
            early["flag"] = False
        early["lines"] = good
    ev = _valid_lines(aud.get("evidence_lines"), ctx)
    if not ev:
        vis = sorted(ctx["visible"], key=lambda x: int(x)) if ctx.get("visible") else []
        rng = f"L{vis[0]}-L{vis[-1]}" if vis else "?"
        soft.append(f"evidence_lines 无有效行号（须给支撑 one_liner/domain 判断的行号，"
                    f"可见范围 {rng}；候选清单标(窗外)的行亦可）")
    aud["evidence_lines"] = ev

    soft += neutral_violations(facts)
    if hard:
        return None, hard, soft
    return facts, [], soft


_SOFT_RE = re.compile(r"(行号全无效|词不在候选|flag=true 但行号无效|evidence_lines 无有效"
                      r"|one_liner:『|review:『|highlights 删条|use_cases 删条)")


def info_gain(review: str, desc: str) -> bool:
    """review 须含 description 之外 ≥3 个实义信息点（dbhub 移植）。"""
    if not review:
        return False
    stop = {"这是", "一个", "这个", "可以", "以及", "并且", "该", "此", "它",
            "工具", "项目", "软件", "用于", "支持", "提供", "面向", "基于", "通过",
            "具有", "包括", "等等", "目前", "还是", "都是", "开源", "ai", "llm"}
    dtoks = set(re.findall(r"[a-z0-9\u4e00-\u9fff]{2,}", (desc or "").lower()))
    btoks = set(re.findall(r"[a-z0-9\u4e00-\u9fff]{2,}", review.lower()))
    return len((btoks - dtoks) - stop) >= 3


def xcheck(facts: dict, ctx: dict) -> dict:
    """程序对照：提名有 install 强信号而模型漏报 → 降一级 confidence + 备注（不覆盖）。"""
    notes = {}
    prov_install = {v["term"] for v in _vlist((facts.get("verdicts") or {}).get("install"))
                    if v.get("rel") == "support"}
    nom_install = {i["term"] for i in _vlist(ctx["cands"].get("install"))}
    missing = nom_install - prov_install
    # 只报"强信号"：pypi/npm/docker 才算，source/binary 弱信号不报（口径保守）
    strong = missing & {"pypi", "npm", "docker"}
    if strong:
        notes["install_missing"] = sorted(strong)
    nom_depre = bool(ctx["cands"].get("depre"))
    model_depre = (facts.get("verdicts") or {}).get("deprecation", {}).get("flag")
    if nom_depre and not model_depre:
        notes["depre_hint"] = "提名有弃坑声明而模型未确认"
    if notes:
        aud = facts.setdefault("audit", {})
        aud["confidence"] = {"high": "mid", "mid": "low"}.get(aud.get("confidence"),
                                                             aud.get("confidence"))
        facts["xcheck"] = notes
    return notes


# ============================================================
# 规则合成层（spec §7 判定权分配表）
# ============================================================

_PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC",
               "Unlicense", "0BSD", "MPL-2.0", "MIT-0", "BSL-1.0"}
_VIRAL = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "AGPL-1.0", "SSPL-1.0", "EUPL-1.1", "EUPL-1.2"}
_LOCAL_PROVIDERS = {"ollama", "llama.cpp", "vllm", "local-weights", "cpu-infer"}


def _verdict(facts: dict, cat: str) -> list[dict]:
    return _vlist((facts.get("verdicts") or {}).get(cat))


def _has_rel(facts: dict, cat: str, rels: set) -> bool:
    return any(v.get("rel") in rels for v in _verdict(facts, cat))


def derive_license(facts: dict, rec: dict, ctx: dict) -> str:
    """dual 程序判定（1.2）：元数据为传染许可且提名命中商业许可声明行 → dual。
    取代模型的 dual_license flag——同版双跑 3 次 dual↔viral 摇摆的根因。
    模型 flag 仍记录于 raw_verdicts 供回溯，但不再是判定来源。"""
    spdx = rec.get("license")
    if spdx in _VIRAL and ctx["cands"].get("dual"):
        return "dual"
    if spdx in _PERMISSIVE:
        return "permissive"
    if spdx in _VIRAL:
        return "viral"
    if spdx and spdx != "NOASSERTION":
        return "permissive" if "Apache" in spdx or spdx.startswith("MIT") else "viral"
    # 池缺 license 时的 README 回退：声明式写法（License: MIT / 许可证：AGPL-3.0）。
    # 徽章可能说谎，故留 xcheck 痕迹不静默采用。
    for ln in ctx["visible"].values():
        m = _LIC_FALLBACK.search(ln)
        if m:
            v = m.group(1).upper()
            facts.setdefault("xcheck", {})["license_from_readme"] = m.group(1)
            if "AGPL" in v or "SSPL" in v or v.startswith("GPL") or "EUPL" in v:
                # 传染许可 + 商业许可提名 → dual（同主规则）
                if ctx["cands"].get("dual"):
                    return "dual"
                return "viral"
            return "permissive"
    return "none"


_LIC_FALLBACK = re.compile(
    r"licen[cs]e[：:\s-]*(MIT|Apache[- ]?2\.0|BSD[-\w ]{0,12}|ISC|MPL[- ]?2\.0|"
    r"AGPL[- ]?\d(?:\.\d)?|GPL[- ]?\d(?:\.\d)?|SSPL[- ]?\d?(?:\.\d)?|Unlicense|"
    r"0BSD|BSL[- ]?1\.0)", re.I)


def derive_model_dep(facts: dict) -> str | None:
    provs = _verdict(facts, "providers")
    if any(v.get("term") in _LOCAL_PROVIDERS and v.get("rel") in ("support", "compat")
           for v in provs):
        return "local-ok"
    if any(v.get("rel") == "support" for v in provs):
        return "locked-api"
    return None


def derive_deploy(facts: dict, ctx: dict) -> str | None:
    """1.4 程序化：install 强信号取 提名∪裁决（治 None↔library/desktop 的召回方差；
    source/brew 等弱信号不参与——brew 常是依赖的安装方式）。desktop_builds 模型
    fact 在双跑中摇摆（khoj library↔desktop），1.4 起只认 binary 提名/裁决。"""
    nom = {i["term"] for i in (ctx["cands"].get("install") or [])}
    ver = {v["term"] for v in _verdict(facts, "install") if v.get("rel") == "support"}
    strong = (nom | ver) & {"docker", "pypi", "npm", "cargo", "go", "helm", "binary"}
    if "binary" in strong:
        return "desktop"
    if "docker" in strong:
        return "self-host"
    if strong & {"pypi", "npm", "cargo", "go", "helm"}:
        return "library"
    return None


def derive_hardware(facts: dict) -> str | None:
    for v in _verdict(facts, "hardware"):
        if v.get("rel") != "support":
            continue
        t = (v.get("term") or "").lower()
        if re.search(r"cpu|无需\s*gpu|不需要\s*gpu|no\s+gpu", t):
            return "cpu-ok"
        m = re.search(r"(\d+(?:\.\d+)?)", t)
        if m and re.search(r"vram|显存|gpu", t):
            g = float(m.group(1))
            return "gpu-24g" if g >= 24 else "gpu-8g"
    return None


def derive_install_friction(facts: dict, ctx: dict) -> str | None:
    """1.4 全程序化：docker/compile/sysdep 一律以提名为准。模型 facts
    （docker_available/needs_compile/system_deps）在双跑中摇摆，是 install_friction
    90.9% 的全部拖累，不再作为判定输入；召回由提名词表承担（1.4 已扩充 compile
    词表）。候选行含"可选/optional"的系统依赖不计。"""
    nom_install = {i["term"] for i in (ctx["cands"].get("install") or [])}
    if "docker" in nom_install:
        return "low"
    compile_ = bool(ctx["cands"].get("compile"))
    sysdep_items = [i for i in (ctx["cands"].get("sysdep") or [])
                    if not re.search(r"可选|optional|非必需", i.get("q", ""), re.I)]
    has_sysdep = bool(sysdep_items)
    if compile_ and has_sysdep:
        return "high"
    if compile_ or has_sysdep:
        return "medium"
    return "low"


def derive_maturity(facts: dict) -> str | None:
    """v1 保守版：结构层（releases/CI）未接入前，只做有据可依的判定，其余 null。"""
    fc = facts.get("facts") or {}
    early = (fc.get("self_declared_early") or {}).get("flag")
    if early:
        return "idea"
    if fc.get("paper_url"):
        return "research"
    return None


def backfill_quotes(facts: dict, ctx: dict) -> list[str]:
    numbered = ctx["numbered"]
    out = []
    aud = facts.setdefault("audit", {})
    for l in aud.get("evidence_lines") or []:
        if l in numbered:
            out.append(f"L{l}: {numbered[l][:120]}")
    for cat in ("providers", "install", "hardware", "products"):
        for v in _verdict(facts, cat):
            v["quotes"] = [numbered[l][:120] for l in v.get("lines") or [] if l in numbered]
    dl = (facts.get("verdicts") or {}).get("dual_license")
    if isinstance(dl, dict):
        dl["quotes"] = [numbered[l][:120] for l in dl.get("lines") or [] if l in numbered]
    return out


def derive_card(facts: dict, ctx: dict) -> dict:
    rec = ctx["rec"]
    ident = facts["identity"]
    op = facts.get("open") or {}
    fc = facts.get("facts") or {}
    verd = facts.get("verdicts") or {}
    evidence = backfill_quotes(facts, ctx)
    products = _verdict(facts, "products")
    return {
        "fn": ctx["fn"], "sha": ctx["sha"], "source": "readme",
        "identity": {"one_liner": ident.get("one_liner"), "review": ident.get("review"),
                     "highlights": ident.get("highlights"), "use_cases": ident.get("use_cases")},
        "filters": {"ai_role": op.get("ai_role"),
                    "license_risk": derive_license(facts, rec, ctx),
                    "deploy": derive_deploy(facts, ctx),
                    "model_dep": derive_model_dep(facts),
                    "hardware": derive_hardware(facts),
                    "install_friction": derive_install_friction(facts, ctx),
                    "maturity": derive_maturity(facts)},
        "eval": {"target_user": op.get("target_user"), "paper_url": fc.get("paper_url"),
                 "demo_url": fc.get("demo_url"), "self_declared_early": fc.get("self_declared_early")},
        "links": {"scenario_tags": op.get("scenario_tags_free"), "domain": op.get("domain"),
                  "alternative_to": [v["term"] for v in products if v.get("rel") == "alternative"],
                  "competitors_mentioned": [v["term"] for v in products if v.get("rel") == "competitor"],
                  "ecosystem_compat": [v["term"] for v in _verdict(facts, "providers")
                                       if v.get("rel") in ("support", "compat")]},
        "intel": {"maintainer_type": op.get("maintainer_type"),
                  "zh_origin": bool(op.get("zh_origin_signals")),
                  "zh_origin_signals": op.get("zh_origin_signals")},
        "trust": {"confidence": (facts.get("audit") or {}).get("confidence"),
                  "evidence": evidence, "xcheck": facts.get("xcheck"),
                  "ver": VER, "prompt_ver": PROMPT_VER,
                  "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                  "softened": facts.get("softened")},
        "raw_verdicts": verd,
    }


# ============================================================
# judge：一次解读全流程（两轮尝试 + 软放行）
# ============================================================

def judge(ctx: dict, ai) -> dict:
    """worker 全身防御：任何未预期异常都记为 failed，不杀整批（dbhub 先例）。"""
    t0 = time.time()
    try:
        return _judge(ctx, ai, t0)
    except Exception as e:                                 # noqa: BLE001
        return {"kind": "failed", "fn": ctx["fn"], "sha": ctx["sha"],
                "error": f"{type(e).__name__}: {e}"[:150],
                "t_total_s": round(time.time() - t0, 2), "t_api_s": 0,
                "api_tries": 0, "violations_all": []}


def _judge(ctx: dict, ai, t0: float) -> dict:
    fn, sha = ctx["fn"], ctx["sha"]
    prompt = build_prompt(ctx)
    t_api = 0.0
    api_tries = 0
    violations_all: list[list[str]] = []
    facts = None
    for attempt in (1, 2):
        try:
            out = ai.chat(prompt + ("" if attempt == 1 else
                        f"\n\n【上次输出被拒收，原因：{'；'.join(violations_all[-1] if violations_all else [])}。请修正后重新输出合规 JSON。】"))
        except Exception as e:                                   # noqa: BLE001
            return {"kind": "failed", "fn": fn, "sha": sha, "error": str(e)[:150],
                    "t_total_s": round(time.time() - t0, 2), "t_api_s": t_api,
                    "api_tries": api_tries, "violations_all": violations_all,
                    "prompt_chars": len(prompt)}
        t_api += out.get("secs") or 0
        api_tries += out.get("tries") or 1
        parsed = extract_json(out["content"])
        if parsed is None and out["reasoning"]:
            parsed = extract_json(out["reasoning"])
        if isinstance(parsed, dict):
            normalize_enums(parsed)
        obj, hard, soft = validate(parsed or {}, ctx)
        violations = hard + soft
        if obj is None and out["finish"] == "length":
            violations = ["输出被 max_tokens 截断"] + violations
        violations_all.append(list(violations))
        if obj is None and attempt == 2 and violations and all(_SOFT_RE.search(v) for v in violations):
            soft_rec = neutral_scrub(parsed)                # type: ignore[arg-type]
            obj2, hard2, soft2 = validate(parsed or {}, ctx)   # type: ignore[arg-type]
            if obj2 is not None and not hard2 and not soft2:
                obj = obj2
                obj["softened"] = soft_rec or ["丢坏裁决"]
                violations_all.append([f"[软放行] {'；'.join(obj['softened'])}"])
        if obj is not None:
            facts = obj
            break
    if facts is None:
        return {"kind": "rejected", "fn": fn, "sha": sha,
                "violations": (violations_all[-1] if violations_all else [])[:5],
                "t_total_s": round(time.time() - t0, 2), "t_api_s": t_api,
                "api_tries": api_tries, "violations_all": violations_all,
                "prompt_chars": len(prompt)}
    review = (facts["identity"].get("review") or "")
    review_cleared = False
    if not info_gain(review, ctx["rec"].get("description") or ""):
        facts["identity"]["review"] = ""
        review_cleared = True
    xcheck(facts, ctx)
    card = derive_card(facts, ctx)
    card["trust"]["model_harness"] = getattr(ai, "harness", None)
    return {"kind": "done", "fn": fn, "sha": sha, "card": card,
            "t_total_s": round(time.time() - t0, 2), "t_api_s": t_api,
            "api_tries": api_tries, "violations_all": violations_all,
            "review_cleared": review_cleared, "prompt_chars": len(prompt),
            "in_raw_chars": ctx["in_raw_chars"], "in_clean_chars": ctx["in_clean_chars"],
            "visible_lines": len(ctx["visible"]),
            "cand_terms": sum(len(v) for v in ctx["cands"].values()),
            "cand_lines_out": sum(1 for l in ctx["cand_lines"] if l not in ctx["visible"])}


# ============================================================
# runlog（spec §16，条目级 jsonl）
# ============================================================

def log_item(rec: dict):
    LOGDIR.mkdir(exist_ok=True)
    p = LOGDIR / f"s8_{datetime.now().strftime('%Y%m%d')}.jsonl"
    rec["ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def summarize(results: list[dict]) -> dict:
    done = [r for r in results if r["kind"] == "done"]
    rej = [r for r in results if r["kind"] == "rejected"]
    fail = [r for r in results if r["kind"] == "failed"]
    viol: dict[str, int] = {}
    for r in rej:
        for v in (r.get("violations") or [])[:5]:
            key = str(v).split("（")[0].split(":")[0][:36]
            viol[key] = viol.get(key, 0) + 1
    secs = [r.get("t_total_s") or 0 for r in results]
    return {"n": len(results), "done": len(done), "rejected": len(rej), "failed": len(fail),
            "pass2%": round(len(done) * 100 / len(results), 1) if results else 0,
            "pass1%": round(sum(1 for r in done
                                if len(r.get("violations_all") or []) <= 1) * 100
                            / len(results), 1) if results else 0,
            "t_p50": sorted(secs)[len(secs) // 2] if secs else 0,
            "api_tries_total": sum(r.get("api_tries") or 0 for r in results),
            "t_api_total": round(sum(r.get("t_api_s") or 0 for r in results), 1),
            "reject_reasons": dict(sorted(viol.items(), key=lambda x: -x[1])[:10])}


# ============================================================
# 主流程：选批 / 试批 / 自测 / 干跑
# ============================================================

def load_cache() -> dict:
    """兼容层:一仓一文件存储装配成 {sha: card}(供 compare 抽样等只读场景)。"""
    return {c["sha"]: c for _, c in cstore.iter_cards()}


def load_istate() -> dict:
    return json.loads(ISTATE.read_text(encoding="utf-8")) if ISTATE.is_file() else {"items": {}}


def pool_by_fullname() -> dict:
    """load_pool 按 repo id 键控；解读层按 full_name 取记录。"""
    return {r.get("full_name"): r for r in load_pool().values() if r.get("full_name")}


def pick_pending(pool: dict, limit: int | None, sample: int | None = None) -> list[str]:
    """待解读 = README 在盘 + 在池 + sha 未解读过(去重索引)。
    组内 star 降序;首解读仓(从无卡片)整组排在 sha 变化的重解读仓之前:
    头部仓 README 周更后新 sha 会按星数插回队首,不降级则每批配额大半
    被刷新老卡吃掉(10-21 实测一整批 470 张全是刷新、净增为零);
    sample>0 时改为无放回随机抽样(测试用)。"""
    import random as _random
    seen = cstore.load_sha_index()["sha_to_fn"]
    done_fn = set(seen.values())          # 已有卡片的仓(fn 口径,跨 sha)
    fresh, refresh = [], []
    for p in READMES.glob("*.md"):
        fn = p.stem.replace("__", "/")
        rec = pool.get(fn)
        if not rec or rec.get("archived"):
            continue
        if sha_of(readme_path(fn).read_text(encoding="utf-8", errors="ignore")) in seen:
            continue
        (refresh if fn in done_fn else fresh).append((rec.get("stars") or 0, fn))
    fresh.sort(reverse=True)
    refresh.sort(reverse=True)
    fns = [fn for _, fn in fresh + refresh]
    if sample:
        return _random.Random(11).sample(fns, min(sample, len(fns)))
    return fns[:limit] if limit else fns


def run(args):
    pool = pool_by_fullname()
    todo = pick_pending(pool, args.trial or args.max_items, args.sample)
    if not todo:
        print("无待解读条目")
        return
    print(f"待解读 {len(todo)} 条（首5: {todo[:5]}）" +
          ("（随机抽样）" if args.sample else ""))
    if args.dry_run:
        for fn in todo[:args.max_items or 5]:
            ctx = build_context(fn, pool[fn])
            prompt = build_prompt(ctx)
            print(f"{fn}: raw {ctx['in_raw_chars']}→clean {ctx['in_clean_chars']} "
                  f"({100 - ctx['in_clean_chars'] * 100 // max(ctx['in_raw_chars'], 1)}%), "
                  f"可见 {len(ctx['visible'])}/{len(ctx['numbered'])} 行, "
                  f"候选 {sum(len(v) for v in ctx['cands'].values())} 条"
                  f"（窗外 {sum(1 for l in ctx['cand_lines'] if l not in ctx['visible'])}）, "
                  f"prompt {len(prompt)} 字, form={ctx['form']}")
        return
    # 软墙钟(云端批跑用):AI_WALL_MIN 分钟后不再容忍长等待,快速收尾保住已产卡片
    wall = os.environ.get("AI_WALL_MIN", "")
    ai = AIClient(deadline=time.time() + int(wall) * 60
                  if wall.isdigit() else None)
    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        futs = {}
        for fn in todo:
            ctx = build_context(fn, pool[fn])
            futs[ex.submit(judge, ctx, ai)] = fn
        for fu in as_completed(futs):
            r = fu.result()
            results.append(r)
            log_item({k: v for k, v in r.items() if k != "card"})
            kind = r["kind"]
            print(f"[{len(results)}/{len(todo)}] {kind:<9} {r['fn']} "
                  f"({r.get('t_total_s', 0)}s, tries={r.get('api_tries', 0)})"
                  + (f" violations={r['violations'][:3]}" if kind == "rejected" else ""))
            if kind == "done":
                # 一仓一文件:主线程统一写(与旧"worker 只算不写"纪律一致)
                cstore.write_card(r["card"])
                cstore.register_sha(r["sha"], r["fn"])
    ist = load_istate()
    for r in results:
        ist["items"][r["fn"]] = {"sha": r["sha"], "status": r["kind"],
                                 "at": datetime.now(timezone.utc).strftime("%Y-%m-%d")}
    atomic_write_json(ISTATE, ist)
    summary = {"type": "run_summary", **summarize(results), "wall_s": round(time.time() - t0, 1)}
    log_item(summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))


def selftest():
    """few-shot 卡过闸自测（不烧 API）：验证实现与 s8_fewshot.json 的一致性。"""
    data = json.loads(FEWSHOT.read_text(encoding="utf-8"))
    pool = pool_by_fullname()
    all_ok = True
    for ex in data["examples"]:
        fn = ex["fn"]
        ctx = build_context(fn, pool.get(fn) or {})
        facts = json.loads(json.dumps(ex["facts"]))          # 深拷贝，不污染源文件
        normalize_enums(facts)
        obj, hard, soft = validate(facts, ctx)
        ok = obj is not None and not soft
        all_ok &= bool(ok)
        print(f"\n=== {fn} === {'PASS' if ok else 'FAIL'}")
        if hard:
            print(f"  硬违规: {hard}")
        if soft:
            print(f"  软违规: {soft}")
        card = derive_card(obj or facts, ctx)
        print(f"  filters: {json.dumps(card['filters'], ensure_ascii=False)}")
        print(f"  links.ecosystem_compat: {card['links']['ecosystem_compat']}")
        print(f"  intel: zh_origin={card['intel']['zh_origin']}, "
              f"maintainer={card['intel']['maintainer_type']}")
        print(f"  evidence: {card['trust']['evidence'][:2]}")
        ig = info_gain(card["identity"]["review"], (pool.get(fn) or {}).get("description") or "")
        print(f"  info_gain(review vs desc): {ig}")
    print("\n自测总结:", "全部通过" if all_ok else "存在失败项——检查实现与 fewshot 一致性")


def compare(n: int, seed: int = 7):
    """双跑一致率（spec §10 一致闸）：从缓存抽 N 张重新解读（不写缓存），
    比较六个枚举字段与首次结果的一致率。门槛 ≥98%。"""
    import random as _random
    cache = load_cache()
    pool = pool_by_fullname()
    cards = list(cache.values())
    sample = _random.Random(seed).sample(cards, min(n, len(cards)))
    ai = AIClient()
    fields = ("ai_role", "license_risk", "deploy", "model_dep",
              "hardware", "install_friction")
    agree = {f: 0 for f in fields}
    role_flip = 0
    n_cmp = 0
    t0 = time.time()
    for i, old in enumerate(sample, 1):
        fn = old["fn"]
        rec = pool.get(fn)
        if not rec:
            continue
        r = judge(build_context(fn, rec), ai)
        if r["kind"] != "done":
            print(f"[{i}/{len(sample)}] {fn} 重跑未过闸: {r.get('violations')}")
            continue
        n_cmp += 1
        diffs = [f for f in fields if r["card"]["filters"].get(f) != old["filters"].get(f)]
        if "ai_role" in diffs:
            role_flip += 1
        for f in fields:
            if f not in diffs:
                agree[f] += 1
        flag = "" if not diffs else f" ←分歧{diffs}"
        print(f"[{i}/{len(sample)}] {fn}{flag}")
    print(f"\n双跑对比完成：{n_cmp} 对（{round(time.time() - t0)}s）")
    for f in fields:
        print(f"  {f:<16} 一致率 {agree[f] * 100 / max(n_cmp, 1):.1f}%")
    overall = sum(agree.values()) * 100 / (max(n_cmp, 1) * len(fields))
    print(f"  枚举总体一致率 {overall:.1f}%（门槛 98%）ai_role 翻转 {role_flip}")


def compare_same(n: int, seed: int = 7, workers: int = 4):
    """同版双跑（一致闸的严格口径）：每个样本用当前提示词新鲜解读【两次】，
    比较两次结果的枚举一致率——排除缓存旧版本混入的预期分歧，测纯摇摆。
    1.3 起按样本并发（每样本的两次解读在 worker 内串行），wall 时间 ≈ 1/workers。"""
    import random as _random
    pool = pool_by_fullname()
    cards = list(load_cache().values())
    sample = _random.Random(seed).sample(cards, min(n, len(cards)))
    ai = AIClient()
    fields = ("ai_role", "license_risk", "deploy", "model_dep",
              "hardware", "install_friction")
    agree = {f: 0 for f in fields}
    flips: dict[str, list[str]] = {f: [] for f in fields}
    n_cmp = 0
    t0 = time.time()

    def one(item):
        i, old = item
        fn = old["fn"]
        rec = pool.get(fn)
        if not rec:
            return i, fn, None, None
        r1 = judge(build_context(fn, rec), ai)
        r2 = judge(build_context(fn, rec), ai)
        if r1["kind"] != "done" or r2["kind"] != "done":
            return i, fn, None, (r1.get("violations") or r2.get("violations"))
        diffs = [f for f in fields
                 if r1["card"]["filters"].get(f) != r2["card"]["filters"].get(f)]
        return i, fn, diffs, (r1, r2)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for i, fn, diffs, extra in ex.map(one, list(enumerate(sample, 1))):
            if diffs is None:
                print(f"[{i}/{len(sample)}] {fn} 有一次未过闸: {extra}", flush=True)
                continue
            n_cmp += 1
            if diffs:
                for f in diffs:
                    a, b = extra[0]["card"]["filters"].get(f), extra[1]["card"]["filters"].get(f)
                    flips[f].append(f"{fn}: {a}↔{b}")
            for f in fields:
                if f not in diffs:
                    agree[f] += 1
            print(f"[{i}/{len(sample)}] {fn}{'' if not diffs else f' ←摇摆{diffs}'}", flush=True)
    print(f"\n同版双跑完成：{n_cmp} 对（{round(time.time() - t0)}s，prompt {PROMPT_VER}）")
    for f in fields:
        print(f"  {f:<16} 一致率 {agree[f] * 100 / max(n_cmp, 1):.1f}%")
    overall = sum(agree.values()) * 100 / (max(n_cmp, 1) * len(fields))
    print(f"  枚举总体一致率 {overall:.1f}%（门槛 98%）")
    for f, lst in flips.items():
        if lst:
            print(f"  摇摆明细 {f}: {lst[:5]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trial", type=int, help="试批条数（star 降序）")
    ap.add_argument("--max-items", type=int)
    ap.add_argument("--sample", type=int, help="随机抽样条数（测试/验收用）")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--compare", type=int, help="双跑一致率抽样条数（对比缓存基线）")
    ap.add_argument("--compare-same", type=int, help="同版双跑一致率抽样条数（严格口径）")
    args = ap.parse_args()
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
    if args.selftest:
        selftest()
    elif args.compare_same:
        compare_same(args.compare_same)
    elif args.compare:
        compare(args.compare)
    else:
        run(args)


if __name__ == "__main__":
    main()
