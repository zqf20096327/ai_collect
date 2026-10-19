# -*- coding: utf-8 -*-
"""s8 卡片一仓一文件存储层(v3,2026-10-18)。

取代 s8_cache.json 单大文件:改一卡写一文件(原子),脏追踪免费,坏一文件丢一卡。
去重语义与旧 sha 键控缓存严格等价:同 sha 的新仓直接跳过(pick_pending),
sha→fn 反向表让"这条内容谁先用过"可查。

纪律:
- 只经 write_card() 写(原子 tmp+replace);禁止外部直接改文件再期望索引感知;
- sha 索引是缓存性质的派生物,可由全量卡片重建(rebuild_sha_index)。
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CARDS = ROOT / "state" / "s8_cards"
SHA_INDEX = ROOT / "state" / "s8_sha_index.json"
LEGACY = ROOT / "state" / "s8_cache.json"


def card_path(fn: str) -> Path:
    letter = fn[0].lower()
    return CARDS / letter / (fn.replace("/", "__") + ".json")


def read_card(fn: str) -> dict | None:
    p = card_path(fn)
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def write_card(card: dict) -> Path:
    p = card_path(card["fn"])
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(card, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(p)
    return p


def iter_cards():
    """(fn, card) 生成器,按路径字典序(≈fn 序)。"""
    if not CARDS.is_dir():
        return
    for p in sorted(CARDS.glob("*/*.json")):
        try:
            card = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        fn = (card.get("fn") or p.stem.replace("__", "/"))
        yield fn, card


def all_cards() -> dict:
    return {fn: card for fn, card in iter_cards()}


def load_sha_index() -> dict:
    if SHA_INDEX.is_file():
        try:
            return json.loads(SHA_INDEX.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"sha_to_fn": {}}


def save_sha_index(idx: dict) -> None:
    tmp = SHA_INDEX.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    tmp.replace(SHA_INDEX)


def sha_seen(sha: str) -> str | None:
    """该 README 内容是否已解读过;返回首个使用它的 fn(去重判据)。"""
    return load_sha_index()["sha_to_fn"].get(sha)


def register_sha(sha: str, fn: str) -> dict:
    idx = load_sha_index()
    idx["sha_to_fn"].setdefault(sha, fn)
    save_sha_index(idx)
    return idx


def rebuild_sha_index() -> int:
    idx = {"sha_to_fn": {}}
    for fn, card in iter_cards():
        if card.get("sha"):
            idx["sha_to_fn"].setdefault(card["sha"], fn)
    save_sha_index(idx)
    return len(idx["sha_to_fn"])


def migrate_from_legacy(verify: bool = True) -> dict:
    """一次性迁移:单文件缓存 → 一仓一文件 + sha 索引。
    迁移后旧文件改名为 s8_cache.json.migrated(保留现场,不删)。"""
    if not LEGACY.is_file():
        return {"migrated": 0, "note": "无旧文件"}
    cache = json.loads(LEGACY.read_text(encoding="utf-8"))
    idx = load_sha_index()
    n = 0
    for sha, card in cache.items():
        if not isinstance(card, dict) or not card.get("fn"):
            continue
        write_card(card)
        idx["sha_to_fn"].setdefault(card.get("sha") or sha, card["fn"])
        n += 1
    save_sha_index(idx)
    if verify:
        rebuilt = {c["sha"]: c for _, c in all_cards().items()}
        assert rebuilt == cache, "迁移校验失败:重建结果与原缓存不一致"
    LEGACY.rename(LEGACY.with_suffix(".json.migrated"))
    return {"migrated": n, "verified": verify}


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "rebuild-index":
        print(f"sha 索引重建: {rebuild_sha_index()} 条")
    else:
        print(migrate_from_legacy())
