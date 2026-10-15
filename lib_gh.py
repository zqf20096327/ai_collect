# -*- coding: utf-8 -*-
"""GitHub 客户端共享库:代理 / token / 限流 / 重试。

所有脚本只通过这里访问 GitHub。瞬时抖动(代理 000)自动重试;
搜索类接口内置 2.2s 节流(30 次/分钟);配额触线睡到重置点。
"""
import http.client
import json
import os
import socket
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
API = "https://api.github.com"


def _stdout_utf8():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _load_env_file():
    env = {}
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def _gh_cli_token():
    try:
        r = subprocess.run(["gh", "auth", "token"], capture_output=True,
                           text=True, timeout=20)
        t = (r.stdout or "").strip()
        return t or None
    except Exception:
        return None


_ENV = _load_env_file()
TOKEN = (_ENV.get("GITHUB_TOKEN") or os.environ.get("GITHUB_TOKEN")
         or _gh_cli_token())
# 优先级:环境变量 > .env > 默认走 Clash。环境变量设空串 = 强制直连(Actions 用)
if "PROXY" in os.environ:
    PROXY = os.environ["PROXY"]
else:
    PROXY = _ENV.get("PROXY", "http://127.0.0.1:7897")

_HANDLERS = []
if PROXY:
    _HANDLERS.append(urllib.request.ProxyHandler(
        {"http": PROXY, "https": PROXY}))
OPENER = urllib.request.build_opener(*_HANDLERS) if _HANDLERS else \
    urllib.request.build_opener()
_PROXY_ALIVE = bool(PROXY)   # 代理连接被拒后自动降级直连;恢复后自动切回
_LAST_PROBE = 0.0


def _proxy_addr():
    u = urllib.parse.urlparse(PROXY)
    return u.hostname or "127.0.0.1", u.port or 7897


def _drop_proxy():
    global OPENER, _PROXY_ALIVE
    _PROXY_ALIVE = False
    OPENER = urllib.request.build_opener()
    print(f"  [proxy] {PROXY} 连接被拒,本进程降级为直连", flush=True)


def _try_restore_proxy():
    """直连模式下传输被掐时,探测代理是否恢复(30s 内不重复探测)。"""
    global OPENER, _PROXY_ALIVE, _LAST_PROBE
    if not PROXY or _PROXY_ALIVE:
        return False
    now = time.time()
    if now - _LAST_PROBE < 30:
        return False
    _LAST_PROBE = now
    try:
        with socket.create_connection(_proxy_addr(), timeout=2):
            pass
    except OSError:
        return False
    OPENER = urllib.request.build_opener(urllib.request.ProxyHandler(
        {"http": PROXY, "https": PROXY}))
    _PROXY_ALIVE = True
    print(f"  [proxy] {PROXY} 恢复可用,切回代理", flush=True)
    return True


def _proxy_broken(e):
    """代理通道坏了的征兆:端口无监听(拒绝)、TLS 被掐(SSLEOF)、连接被重置。"""
    reason = getattr(e, "reason", None)
    for cand in (reason, e):
        if isinstance(cand, (ConnectionRefusedError, ssl.SSLError,
                             ConnectionResetError)):
            return True
    return False


def _headers(accept="application/vnd.github+json", extra=None):
    h = {"Accept": accept, "User-Agent": "ai_collect"}
    if TOKEN:
        h["Authorization"] = "Bearer " + TOKEN
    if extra:
        h.update(extra)
    return h


def _wait_seconds(reset_hdr):
    try:
        return max(int(reset_hdr) - int(time.time()) + 2, 2)
    except (TypeError, ValueError):
        return 60


def api_get(path, params=None, accept="application/vnd.github+json",
            extra_headers=None, timeout=30, retries=6, want="json"):
    """GET,返回 (headers, body)。want="raw" 时 body 为 bytes。
    304 返回 (headers, None)。通道切换/限流等待不消耗重试次数,
    真实失败指数退避;总迭代上限 retries*4 防乒乓死循环。"""
    url = path if path.startswith("http") else API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    last_err = None
    attempt = 0
    iterations = 0
    while attempt < retries and iterations < retries * 4:
        iterations += 1
        req = urllib.request.Request(url, headers=_headers(accept, extra_headers))
        try:
            with OPENER.open(req, timeout=timeout) as r:
                body = r.read()
                if want == "raw":
                    return r.headers, body
                try:
                    return r.headers, json.loads(body)
                except json.JSONDecodeError:
                    raise ConnectionError("non-json body (proxy hiccup?)")
        except urllib.error.HTTPError as e:
            hdrs = e.headers
            if e.code == 304:
                return hdrs, None
            if e.code in (403, 429):
                ra = hdrs.get("Retry-After") if hdrs else None
                if ra:
                    time.sleep(int(ra) + 1)
                    continue
                if hdrs and hdrs.get("X-RateLimit-Remaining") == "0":
                    w = _wait_seconds(hdrs.get("X-RateLimit-Reset"))
                    print(f"  [rate-limit] sleep {int(w)}s", flush=True)
                    time.sleep(min(w, 3600))
                    continue
                raise
            if e.code >= 500:
                last_err = e
                attempt += 1
                time.sleep(2 * attempt)
                continue
            raise
        except (http.client.HTTPException, urllib.error.URLError,
                TimeoutError, ConnectionError, ssl.SSLError, OSError) as e:
            if _PROXY_ALIVE and _proxy_broken(e):
                _drop_proxy()
                time.sleep(2)
                continue
            if _try_restore_proxy():
                continue
            last_err = e
            attempt += 1
            time.sleep(min(3 * attempt, 30))
    raise last_err if last_err else RuntimeError("api_get failed: " + url)


def search_repos(q, max_pages=10, per_page=100, sort="stars", sleep=2.2):
    """仓库搜索。返回 (items, total_count)。内置节流,尊重 1000 条硬上限。
    注意:同一 q 翻页时 page1 会被再次请求(调用方按 id 去重即可)。"""
    items, total = [], None
    page = 1
    while page <= max_pages:
        time.sleep(sleep)  # 30 次/分钟以内
        _, data = api_get("/search/repositories",
                          {"q": q, "per_page": per_page, "page": page,
                           "sort": sort})
        if total is None:
            total = data.get("total_count", 0)
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < per_page or len(items) >= total:
            break
        page += 1
    return items, total or 0
