# -*- coding: utf-8 -*-
"""enrich_cache 分片存取层(移植自 dbhub enrich_store,10-09 分片方案)。

桶名 = sha256(key) 前 2 位 → state/enrich_cache_shards/<xx>.json,256 桶。
4 万仓的全量信号 ~8MB:整文件重写会让 git 每晚传一个整 blob,分片后
只写脏桶(~32KB/桶),git 只传变化的桶。

注意:值是"原地合并"语义(collect_dims 的 sig.update),dict 子类的脏桶
追踪看不见原地改——采集每个目标前必须显式 touch(fn),忘掉即静默丢数据。
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARD_DIR = ROOT / "state" / "enrich_cache_shards"


def _bucket(key: str) -> str:
    # 对 key 整体做 sha 再取前 2 位:统一走哈希防前缀类 key 挤爆个别桶
    return hashlib.sha256(key.encode()).hexdigest()[:2]


def _write_shard(bucket: str, entries: dict) -> None:
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    p = SHARD_DIR / f"{bucket}.json"
    tmp = SHARD_DIR / f"{bucket}.tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(entries, ensure_ascii=False, indent=1))
    tmp.replace(p)


def load_cache() -> dict:
    data: dict = {}
    if SHARD_DIR.is_dir():
        for p in sorted(SHARD_DIR.glob("*.json")):
            shard = json.loads(p.read_text(encoding="utf-8"))
            if not isinstance(shard, dict):
                raise RuntimeError(f"分片格式损坏(非 dict): {p}")
            data.update(shard)
    return data


def save_cache_all(cache: dict) -> int:
    """全量落盘(拆分/清理类工具用):重写全部桶,清掉已无键的桶文件。"""
    buckets: dict[str, dict] = {}
    for k, v in cache.items():
        buckets.setdefault(_bucket(k), {})[k] = v
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    for p in SHARD_DIR.glob("*.json"):
        if p.stem not in buckets:
            p.unlink()
    for b, entries in buckets.items():
        _write_shard(b, entries)
    return len(buckets)


class EnrichCacheStore(dict):
    """dict 兼容的分片缓存:改哪个桶,flush() 只重写哪个桶(checkpoint 用)。

    值字段是原地 update 语义(collect_dims 的 sig.update),__setitem__
    追踪不到——原地改前必须显式 touch(fn)。
    """

    def __init__(self):
        super().__init__(load_cache())
        self._dirty: set[str] = set()

    def touch(self, key) -> None:
        self._dirty.add(_bucket(key))

    def __setitem__(self, key, value):
        self._dirty.add(_bucket(key))
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self._dirty.add(_bucket(key))
        super().__delitem__(key)

    def update(self, *args, **kwargs):     # dict 原生 update 绕过 __setitem__
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
        return self[key]

    def pop(self, key, *default):
        if key in self:
            self._dirty.add(_bucket(key))
        return super().pop(key, *default)

    def flush(self) -> int:
        """脏桶落盘;桶被清空则删该桶文件。返回本次写入的桶数。"""
        if not self._dirty:
            return 0
        grouped: dict[str, dict] = {}
        for k, v in self.items():           # 单趟全扫分组
            b = _bucket(k)
            if b in self._dirty:
                grouped.setdefault(b, {})[k] = v
        for b in sorted(self._dirty):
            entries = grouped.get(b)
            if entries:
                _write_shard(b, entries)
            else:
                p = SHARD_DIR / f"{b}.json"
                if p.is_file():
                    p.unlink()
        n = len(self._dirty)
        self._dirty.clear()
        return n
