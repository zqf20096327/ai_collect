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
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
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
    with _PROXY_LOCK:
        if not _PROXY_ALIVE:
            return
        _PROXY_ALIVE = False
        OPENER = urllib.request.build_opener()
        print(f"  [proxy] {PROXY} 连接被拒,本进程降级为直连", flush=True)


def _try_restore_proxy():
    """直连模式下传输被掐时,探测代理是否恢复(30s 内不重复探测)。"""
    global OPENER, _PROXY_ALIVE, _LAST_PROBE
    if not PROXY:
        return False
    with _PROXY_LOCK:
        if _PROXY_ALIVE:
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
                _pace_update(r.headers)
                if want == "raw":
                    return r.headers, body
                try:
                    return r.headers, json.loads(body)
                except json.JSONDecodeError:
                    raise ConnectionError("non-json body (proxy hiccup?)")
        except urllib.error.HTTPError as e:
            hdrs = e.headers
            if e.code == 304:
                _pace_update(hdrs)
                return hdrs, None
            if e.code in (403, 429):
                _pace_update(hdrs)
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


def api_send(method, path, payload=None, accept="application/vnd.github+json",
             extra_headers=None, timeout=30, retries=6):
    """POST/PATCH/PUT/PATCH JSON。与 api_get 同一套重试/换通道逻辑。"""
    url = path if path.startswith("http") else API + path
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    h = _headers(accept, extra_headers)
    if body is not None:
        h["Content-Type"] = "application/json"
    last_err = None
    attempt, iterations = 0, 0
    while attempt < retries and iterations < retries * 4:
        iterations += 1
        req = urllib.request.Request(url, data=body, headers=h, method=method)
        try:
            with OPENER.open(req, timeout=timeout) as r:
                return r.headers, json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            hdrs = e.headers
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
            if e.code >= 500:
                last_err = e
                attempt += 1
                time.sleep(2 * attempt)
                continue
            detail = e.read()[:300] if hasattr(e, "read") else b""
            raise RuntimeError(f"{method} {path} -> {e.code}: {detail!r}") from e
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
    raise last_err if last_err else RuntimeError(f"api_send failed: {method} {path}")


def search_repos(q, max_pages=10, per_page=100, sort="stars", start_page=1,
                 known_total=None, concurrency=5):
    """仓库搜索。返回 (items, total_count)。

    第 1 页串行(拿 total_count 与配额头),余页有界并发:Pacer 闸门按
    30 次/分钟配额把相邻请求的发出时刻至少隔开动态间隔,并发只用于
    重叠网络往返(单页 RTT 5-15s),不提高单位时间请求量,不引入新的
    漏页风险。start_page/known_total 配合探测复用:探测拿了第 1 页后,
    续页从第 2 页开始,首页不重复请求。"""
    SEARCH_PACE.slot()
    h, data = api_get("/search/repositories",
                      {"q": q, "per_page": per_page, "page": start_page,
                       "sort": sort})
    total = known_total if known_total is not None else data.get("total_count", 0)
    items = list(data.get("items", []))
    got = (start_page - 1) * per_page + len(items)
    if len(items) < per_page or (total and got >= total):
        return items, total
    last = min(max_pages, (total + per_page - 1) // per_page)
    pages = list(range(start_page + 1, last + 1))
    if len(pages) > 1 and concurrency > 1:
        with ThreadPoolExecutor(max_workers=concurrency) as ex:
            for batch in ex.map(lambda p: _search_page(q, per_page, sort, p),
                                pages):
                items.extend(batch)
    else:
        for p in pages:
            items.extend(_search_page(q, per_page, sort, p))
    return items, total


def _search_page(q, per_page, sort, page):
    SEARCH_PACE.slot()
    _, data = api_get("/search/repositories",
                      {"q": q, "per_page": per_page, "page": page,
                       "sort": sort})
    return data.get("items", [])


class Pacer:
    """并发限速闸门:按配额响应头动态计算请求间隔;多线程共享时相邻请求
    发出时刻至少间隔 interval,配额见底则睡到重置点。锁内只做时刻计算,
    睡在锁外,不阻塞其它线程预订后续槽位。"""

    def __init__(self, floor: float, cap: float = 6.0, reserve: int = 2):
        self.floor, self.cap, self.reserve = floor, cap, reserve
        self.rem = None            # X-RateLimit-Remaining
        self.reset = 0.0           # X-RateLimit-Reset(epoch 秒)
        self._lock = threading.Lock()
        self._next_at = 0.0

    def update(self, headers):
        try:
            rem = headers.get("X-RateLimit-Remaining")
            if rem is None:
                return
            with self._lock:
                self.rem = int(rem)
                rst = headers.get("X-RateLimit-Reset")
                if rst:
                    self.reset = float(rst)
        except (TypeError, ValueError):
            pass

    def _interval(self):
        if self.rem is None:
            return self.floor
        if self.rem <= self.reserve:
            return max(self.reset - time.time() + 1, self.floor)
        window = max(self.reset - time.time(), 0.0)
        return max(min(window / self.rem, self.cap), self.floor)

    def slot(self):
        """预留下一个请求时刻并等待到点。"""
        with self._lock:
            now = time.time()
            start = max(self._next_at, now) + self._interval()
            self._next_at = start
        wait = start - time.time()
        if wait > 0:
            time.sleep(wait)


SEARCH_PACE = Pacer(2.2)     # 搜索 30 次/分钟
CORE_PACE = Pacer(0.8)       # core 5000 次/时 ≈ 83 次/分钟
_PACERS = {"search": SEARCH_PACE, "core": CORE_PACE}
_PROXY_LOCK = threading.Lock()


def _pace_update(headers):
    """按响应头的资源域把配额信息喂给对应闸门(api_get 每个出口调用)。"""
    res = headers.get("X-RateLimit-Resource") if headers else None
    pacer = _PACERS.get(res)
    if pacer is not None:
        pacer.update(headers)
