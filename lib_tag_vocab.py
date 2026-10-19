# -*- coding: utf-8 -*-
"""场景标签词表库：加载 tag_vocab_v1.json，提供别名映射 / 提名 / topics 归一。

被 s10_tags.py 使用；后续 s8 全量打标也走这里（单一事实源）。
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VOCAB_PATH = ROOT / "tag_vocab_v1.json"

_WS_RE = re.compile(r"\s+")
_SEP_RE = re.compile(r"[-_/.]+")


def normalize(s: str) -> str:
    """标签/topics 归一：casefold + 分隔符折空格 + 压空白。

    'AI Agent' / 'ai-agent' / 'ai_agent' -> 'ai agent'；
    '教程/课程' -> '教程 课程'。
    """
    s = _SEP_RE.sub(" ", str(s))
    s = _WS_RE.sub(" ", s).strip()
    return s.casefold()


@lru_cache(maxsize=1)
def load_vocab(path: str | None = None) -> dict:
    data = json.loads(Path(path or VOCAB_PATH).read_text(encoding="utf-8"))
    tags = data["tags"]
    slugs = [t["slug"] for t in tags]
    if len(slugs) != len(set(slugs)):
        raise ValueError("slug 重复")
    # 别名唯一性：一个别名只能映射一个规范标签（单向，永不回指）
    alias_map: dict[str, str] = {}
    for t in tags:
        for a in t.get("aliases", []):
            k = normalize(a)
            if k in alias_map and alias_map[k] != t["slug"]:
                raise ValueError(f"别名冲突: {a!r} -> {alias_map[k]} 与 {t['slug']}")
            alias_map[k] = t["slug"]
        # 规范名自身也可命中（中文主名 / slug 归一形态）
        alias_map.setdefault(normalize(t["zh"]), t["slug"])
        alias_map.setdefault(normalize(t["slug"]), t["slug"])
    # 排除表：kind -> set(normalized)
    excl: dict[str, set] = {}
    for e in data["exclusions"]:
        excl[e["kind"]] = {normalize(m) for m in e["match"]}
    # 提名关键词：slug -> [归一化子串]
    kw: dict[str, list] = {
        t["slug"]: [normalize(k) for k in t.get("keywords", [])] for t in tags
    }
    data["_by_slug"] = {t["slug"]: t for t in tags}
    data["_alias_map"] = alias_map
    data["_excl_sets"] = excl
    data["_keywords"] = kw
    return data


def classify_free_tag(tag: str) -> tuple[str, str | None]:
    """存量自由标签三分类。

    返回 ("canonical", slug) / ("excluded", kind) / ("unmapped", None)。
    优先级：别名命中 > 排除表 > 未映射（词表缺口信号）。
    """
    v = load_vocab()
    k = normalize(tag)
    if k in v["_alias_map"]:
        return ("canonical", v["_alias_map"][k])
    for kind, s in v["_excl_sets"].items():
        if k in s:
            return ("excluded", kind)
    return ("unmapped", None)


def map_free_tags(tags: list[str]) -> dict:
    """一组自由标签 -> {canonical: 去重排序后的 slug 列表, stats: 三桶计数}"""
    seen: list[str] = []
    stats = {"canonical": 0, "excluded": 0, "unmapped": 0}
    for t in tags:
        kind, val = classify_free_tag(t)
        stats[kind] += 1
        if kind == "canonical" and val not in seen:
            seen.append(val)
    v = load_vocab()
    seen.sort(key=lambda s: (v["_by_slug"][s]["group"], s))
    return {"canonical": seen, "stats": stats}


_CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def _kw_hit(kw: str, blob: str) -> bool:
    """关键词命中：含中文用子串；纯 ASCII 用词边界（防 rag 命中 storage/average、
    quant 命中 quantum/quantization 的裸子串误报）。"""
    if _CJK_RE.search(kw):
        return kw in blob
    return re.search(rf"\b{re.escape(kw)}\b", blob) is not None


def nominate(candidates_text: dict[str, str], max_n: int = 10) -> list[str]:
    """确定性提名：对若干文本源（topics/description/卡片摘要）做关键词命中。

    candidates_text: {源名: 文本}；命中任一关键词即提名该标签
    （文本与关键词都先过 normalize，'claude-code' 与 'claude code' 等价）。
    """
    v = load_vocab()
    blob = normalize(" \n ".join(candidates_text.values()))
    hits = []
    for slug, kws in v["_keywords"].items():
        for k in kws:
            if k and _kw_hit(k, blob):
                hits.append(slug)
                break
    hits.sort(key=lambda s: (v["_by_slug"][s]["group"], s))
    return hits[:max_n]


def normalize_topics(topics: list[str]) -> list[str]:
    """GitHub topics 归一（单复数折衷 + 分隔符折空格），用于二级召回索引与展示。"""
    out = []
    seen = set()
    for t in topics or []:
        k = normalize(t)
        if k.endswith("s") and len(k) > 4:      # agents->agent, embeddings->embedding
            k2 = k[:-1]
        else:
            k2 = k
        for cand in (k, k2):
            if cand and cand not in seen:
                seen.add(cand)
                out.append(cand)
    return out


def validate_density(counter: dict[str, int], threshold: int) -> list[str]:
    """密度门槛检查：返回低于阈值的 slug 列表（应转 facet 不出页面）。"""
    v = load_vocab()
    return sorted(s for s, c in counter.items()
                  if c < threshold and s in v["_by_slug"])


if __name__ == "__main__":
    v = load_vocab()
    n = len(v["tags"])
    print(f"vocab {v['vocab_ver']}: {n} tags, {len(v['groups'])} groups, "
          f"{len(v['_alias_map'])} aliases, "
          f"{sum(len(s) for s in v['_excl_sets'].values())} exclusion patterns")
    for t in v["tags"]:
        assert t["definition"] and t["negatives"], f"四件套缺失: {t['slug']}"
    print("四件套完整性 OK")
