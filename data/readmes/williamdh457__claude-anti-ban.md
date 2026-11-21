# Claude 防封手册 · claude-anti-ban

> **全自动**：你把需求说一次，AI 探测环境、清痕迹、搭节点、配分流、对齐时区、封泄露、建虚拟机、验收、清场，全程只在 7 个必须由人决定的地方问你一次。
> **最后只给你一份文档**，其余中间产物 AI 自己删掉。

<p align="center">
  <a href="https://github.com/williamdh457/claude-anti-ban"><img alt="repo" src="https://img.shields.io/badge/GitHub-claude--anti--ban-black.svg"></a>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="platform" src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows-lightgrey.svg">
  <img alt="mode" src="https://img.shields.io/badge/mode-autopilot-green.svg">
</p>

---

## 一句话原理

大多数人「被封」不是技术不够，而是**画像自相矛盾**：

```
IP 在纽约  ·  系统时区写着 Asia/Shanghai  ·  浏览器语言 zh-CN
DNS 查询从国内发出  ·  WebRTC 泄露真实 IP  ·  出口 IP 一天换三个国家
```

Anthropic 不看你「有没有挂代理」，它看你**像不像一个正常用户**。
所以这个仓库只做一件事：把出口 IP、系统时区、语言、DNS、UDP、设备指纹、支付方式，**全部对齐到同一个地区、同一个身份，并且长期不变**。

---

## 怎么用：发一段话，等一份文档

### 1. 把这段发给你的 AI（Claude Code / Codex / Cursor）

```text
帮我把 Claude 的防封环境整套配好，全自动做完，中间只在必须我选的地方问我。

我的情况：
- 系统：【Windows 11 专业版 / macOS 14】
- 之前：【这个号被封过 / 没被封过】
- 这台电脑：【只登过这一个号 / 登过好几个号】
- 我有 VPS：【有，信息在下面 / 没有，帮我选一家】

如果我有 VPS：
  IP：【203.0.113.10】  端口：【22】  用户：【root】  密码：【粘贴】
  系统：【Ubuntu 22.04】  机房：【美国 纽约】

要求：
1. 先自己探测环境，别问我系统版本、时区、DNS 这些你能查到的
2. 需要我选的，一次问完，每个选项给我代价和推荐
3. 做完给我一份 Word 文档，教我每天怎么用、出问题怎么办
4. 其余中间文件你自己清掉，别留给我
```

### 2. 回答 7 个选择题（一次问完，不知道就选默认）

| # | 问题 | 默认 |
|---|---|---|
| ① | 出口放哪个国家 | 美国 |
| ② | VPS 怎么来 | 有就用有的 |
| ③ | 环境怎么隔离（虚拟机 / 这台电脑 / 混合） | 被封过→虚拟机 |
| ④ | 旧痕迹清到什么程度 | 被封过→清到像新机器 |
| ⑤ | 怎么付款 | Google Play |
| ⑥ | 现有节点留不留 | 全部重建 |
| ⑦ | 文档格式 | Word |

### 3. 拿到 `Claude-使用手册.docx`，照着做

就这一份。里面是：每天开机 5 步、你现在用的是什么、7 件不要做的事、出问题怎么办、被封了怎么申诉、备份怎么恢复、以后想改怎么跟 AI 说。

---

## AI 会自动做完的事

```
P0 探测   系统版本 / 内存 / 磁盘 / 虚拟化 / 时区 / 语言 / IPv6 / DNS / 代理 / 出口 IP
P1 决策   按规则定方案（虚拟机 or 宿主机、时区、语言、分流语义）
P2 清理   备份 → 清旧账号痕迹 → 删的进废纸篓（保护清单永不触碰）
P3 出口   SSH 加固 → 3x-ui → VLESS-Reality → 测速 → 不合格自动换 IP
P4 一致性 时区=出口时区 / 语言 en-US / 关 IPv6 / 客户端 TUN / 白名单式全代理分流
P5 封堵   DNS 三层（客户端 DoH + fake-ip + 走代理）· WebRTC 策略 · NTP 走代理
P6 隔离   Hyper-V 干净虚拟机（可选）+ 检查点 clean-baseline
P7 验收   九项硬门槛，每项要证据，不过就修
P8 文档   渲染唯一一份用户手册（MD + DOCX，自带 lint）
P9 清场   删掉自己所有中间产物
```

**它不会问你**：要不要备份、要不要开 TUN、能不能改时区、是不是生产环境、有没有授权。
**它只会问你**：那 7 个选择题，以及 5 件不可逆的事（删桌面端数据、删钥匙串、改 Play 地区、卸载软件、覆盖现有节点）。

---

## 五条铁律（写在 skill 里，AI 必须遵守）

| # | 铁律 | 为什么 |
|---|---|---|
| 1 | **先测后开** | 每次开机、换节点，先跑检测页再打开 Claude。顺序反了，风控已经记了一笔 |
| 2 | **一致性 > 单点最优** | 美国 IP + 上海时区，比「香港 IP + 香港时区」更危险 |
| 3 | **出口独享且稳定** | 机房 IP 定下来就别换；频繁跳变 = 账号被盗用画像 |
| 4 | **一机一号一环境** | 一个账号只在一个干净环境登录 |
| 5 | **慢就是快** | 新号先免费养 1–3 个月，再 Pro，再 Max |

---

## 仓库结构

```
claude-anti-ban/
├── README.md
├── docs/                            给你看的背景材料（可选读）
│   ├── 00-原理.md                    风控在看什么
│   ├── 01-快速开始.md
│   ├── 02-常见问题.md
│   └── 03-术语表.md
├── skills/
│   └── claude-anti-ban/
│       ├── SKILL.md                 ★ AI 加载的入口：全自动执行规范
│       ├── references/              AI 看的（14 篇）
│       │   ├── 01-vps.md            选商、开机器、搭节点、TUN
│       │   ├── 02-ip-check.md       检测页判读与阈值
│       │   ├── 03a-cleanup-macos.md
│       │   ├── 03b-cleanup-windows.md
│       │   ├── 04-timezone-locale.md
│       │   ├── 05-dns-leak.md
│       │   ├── 06-webrtc-leak.md
│       │   ├── 07-hyperv.md
│       │   ├── 08-payment.md
│       │   ├── 09-routing-rules.md
│       │   ├── 10-troubleshooting.md
│       │   ├── 11-checklist.md
│       │   ├── 12-prompts.md        ★ 你只需要看这一篇
│       │   ├── 13-vm-or-host.md
│       │   ├── 14-autorun.md        ★ 全自动 runbook
│       │   └── 15-user-guide-template.md  ★ 交付文档模板
│       ├── scripts/                 9 个脚本，AI 自己调
│       └── assets/routing/          四套分流规则
└── transcripts/                     两期参考视频的校对字幕
```

**分界线很清楚**：`12-prompts.md` 和最终那份 `Claude-使用手册.docx` 是给你看的；其余全是 AI 看的。

---

## 脚本

| 脚本 | 平台 | 作用 |
|---|---|---|
| `check_env.sh` / `check_env.ps1` | mac/Linux · Win | 环境自检（时区/语言/IPv6/DNS/出口/延迟） |
| `ipcheck.py` | 跨平台 | 多源出口 IP、ASN、hosting 标记、时区比对 |
| `cleanup_traces.sh` / `.ps1` | mac · Win | 痕迹清理（默认 dry-run，删除进废纸篓） |
| `hyperv_setup.ps1` | Win | 检测版本 → 开 Hyper-V → 建交换机 → 建虚拟机 |
| `set_region.ps1` / `set_region.sh` | Win · mac | 时区/区域/语言/关 IPv6 一键设置 |
| `render_user_guide.py` | 跨平台 | **由 state.json 渲染用户手册（MD + DOCX，带 lint）** |
| `finalize.sh` / `finalize.ps1` | mac · Win | **收尾自清理** |

```bash
# 单独跑一遍体检（不装 skill 也能用）
bash skills/claude-anti-ban/scripts/check_env.sh
python3 skills/claude-anti-ban/scripts/ipcheck.py

# 手动渲染一份用户手册（看看长什么样）
python3 skills/claude-anti-ban/scripts/render_user_guide.py \
  --state state.json --out ./Claude-使用手册 --format both
```

---

## 分流规则（拿来即用）

`skills/claude-anti-ban/assets/routing/`

| 文件 | 引擎 |
|---|---|
| `clash.yaml` | Clash / Mihomo / Stash |
| `singbox-rule-set.json` | sing-box |
| `surge.conf` | Surge / Loon / Quantumult X |
| `domain-list.txt` | 任意工具 |

语义只有一条：**默认全部走代理，白名单例外；Claude 域名最高优先级，加 IP/ASN 兜底 + NTP 走代理。**

---

## 虚拟机还是宿主机？

不替你决定，把利弊摆出来（AI 会按这个问你）：

| | 虚拟机（Hyper-V） | 宿主机 |
|---|---|---|
| 防封 | ★★★★★ | ★★★ |
| 便利 | ★★ | ★★★★★ |
| 性能 | ★★★ | ★★★★★ |
| 可回滚 | ✅ 检查点 | ❌ |
| 首次搭建 | 40–60 min | 20 min |
| 适合 | 被封过 / 长期跑 Code / 内存 ≥16 GB | 只网页聊天 / 机器干净 / 内存 8 GB |

详见 [`13-vm-or-host.md`](skills/claude-anti-ban/references/13-vm-or-host.md)。

---

## 付款路线

```
安卓手机 + 美国网络 + Google Play（地区=美国）+ 国内可外币支付的 Mastercard
   → Claude App → 菜单 → 头像 → 升级 → 走 Play 账单 → 先买 Pro
```

防风要点：**IP 地区 / Play 地区 / 账单地址三者一致**；一张卡只给一个账号；别用虚拟卡、预付卡、接码平台号。

---

## 装进你的 Agent

```bash
git clone https://github.com/williamdh457/claude-anti-ban.git
cd claude-anti-ban

# Claude Code（项目级）
mkdir -p .claude/skills && cp -r skills/claude-anti-ban .claude/skills/

# 用户级
cp -r skills/claude-anti-ban ~/.claude/skills/
```

之后说「用 claude-anti-ban 帮我配环境」即可加载。

---

## 参考与致谢

- 视频《如何长期稳定使用 Claude 订阅，原理 + 实操的手把手教学》— 技术爬爬虾（[字幕校对](transcripts/video-1-claude-stable.md)）
- 视频《为什么我说它是 Windows 平台最好的虚拟机，Hyper-V 虚拟机详细安装教程》— 技术爬爬虾（[字幕校对](transcripts/video-2-hyperv.md)）
- [ip.net.coffee/claude](https://ip.net.coffee/claude/) — IP 纯净度 / DNS / WebRTC / 时区指纹检测
- 清理思路参考 [Pluviobyte/claude-ban-clean](https://github.com/Pluviobyte/claude-ban-clean)、[suyuan2022/suyuan-skill](https://github.com/suyuan2022/suyuan-skill)

## 边界

本仓库是**网络环境与设备一致性**的工程实现：让自用账号的访问环境稳定、可预测。它不改客户端、不伪造身份、不绕过付费。账号是否被限制取决于 Anthropic 的服务条款与风控策略，本仓库不承诺结果，只承诺「做完、验收、说清楚」。

部分风控机制来自社区逆向与公开爆料（截至 2026 年未获官方证实），请当作「值得验证的风险点」。

## License

[MIT](LICENSE)
