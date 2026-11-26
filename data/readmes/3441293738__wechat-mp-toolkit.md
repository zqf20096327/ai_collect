# WeChat MP Toolkit · 微信公众号文章采集与归档工具

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Release](https://img.shields.io/github/v/release/3441293738/wechat-mp-toolkit?color=07c160&label=Release)](https://github.com/3441293738/wechat-mp-toolkit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-07c160.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-5865F2)](#快速开始)

面向个人知识管理与资料归档的 **微信公众号历史文章协议采集、高清图文下载与多模板导出工具**，提供 **Windows 独立桌面版（`.exe` 免安装）** 与 **iOS 玻璃拟态 Web 工作台**。

<p align="center">
  <img src="docs/assets/demo-walkthrough.gif" alt="WeChat MP Toolkit Web 控制台交互演示" width="900">
</p>
<p align="center">
  <sub>交互演示：PAC 协议通道 → 历史分页直采 → iOS 玻璃筛选与日历区间 → 高清图文 / Markdown 切换 → 多模板导出实时预览</sub>
</p>

---

## 核心特性

- **微信同源协议直采（Windows 微信 4.2+）**：免验证码分页拉取公众号历史文章清单、高清排版 HTML、Markdown 与本地图片，支持长 ID 防截断、自动去重与分页完整性审计。
- **PAC 单域名精准分流**：仅将 `mp.weixin.qq.com` 导向本地协议通道，其余站点直连原有代理（如 Clash Verge）或直连网络，停止或退出自动还原系统代理。
- **零凭据落盘安全模型**：`Cookie`、`uin`、`key`、`pass_ticket` 等仅驻留于本机微信内存，绝不写入磁盘、数据库或导出文件。
- **iOS 玻璃拟态 Web 工作台**：支持公众号全部历史采集与单篇文章链接解析、本地高清配图阅读（高清图文 / Markdown / 纯文本切换），以及按公众号、状态、日期区间、关键词和勾选状态实时筛选。
- **多格式 × 多模板导出中心**：支持 6 种导出格式与 6 套模板（含 27 字段自由勾选），导出前实时预览内容效果。

---

## 界面预览

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <strong>iOS 玻璃拟态主工作台 &amp; 高清阅读器</strong><br>
      <sub>PAC 单域名连接状态栏、公众号识别入口与分栏高清图文阅读</sub><br><br>
      <img src="docs/assets/preview-workspace.png" alt="iOS 玻璃拟态主工作台与高清图文阅读器">
    </td>
    <td width="50%" align="center" valign="top">
      <strong>自定义玻璃筛选器 &amp; 日历区间选择器</strong><br>
      <sub>快捷时间预设、起止日期高亮筛选与多选批量补抓正文</sub><br><br>
      <img src="docs/assets/preview-filters.png" alt="自定义 iOS 玻璃筛选器与日历区间选择器">
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <strong>多格式 × 多模板导出中心（含实时预览）</strong><br>
      <sub>6 种文件格式 × 6 套模板（含 27 自定义字段），下载前实时预览</sub><br><br>
      <img src="docs/assets/preview-export-center.png" alt="多格式多模板导出中心与实时预览">
    </td>
    <td width="50%" align="center" valign="top">
      <strong>单文件离线可阅读网页（.html 导出效果）</strong><br>
      <sub>Base64 内嵌高清配图与离线检索，双击即可长期阅读</sub><br><br>
      <img src="docs/assets/preview-offline-reader.png" alt="导出的单文件离线可阅读网页效果">
    </td>
  </tr>
</table>

> 注：以上演示动画与截图均基于合成示例数据录制，不包含任何真实账号凭据或隐私内容。

---

## 快速开始

### 方式一：Windows 桌面版（推荐 · 免安装 Python）

1. 前往 [Releases](https://github.com/3441293738/wechat-mp-toolkit/releases) 下载 `WeChatMPToolkit-win-x64.exe`；
2. **双击运行**即可自动弹出独立桌面应用窗口（归档数据自动保存在同目录 `archive_data/`）；
3. 关闭窗口时自动停止协议通道并还原系统代理。

### 方式二：源码运行（Windows / macOS / Linux）

需 **Python 3.10+**，三步即可启动：

```bash
git clone https://github.com/3441293738/wechat-mp-toolkit.git && cd wechat-mp-toolkit
pip install -r requirements.txt
python run_desktop.py   # 弹出独立桌面窗口（或运行 python run_web.py 在浏览器打开）
```

> **自行打包桌面版 `.exe`（Windows）**：`pip install pyinstaller && python scripts/build_exe.py`，输出单文件 `dist/WeChatMPToolkit.exe`。

### 使用步骤

1. **首次配置临时证书（24 小时有效）**：点击右上角「证书管理」→ 点击 **「一键安装临时证书」**，在弹出的 Windows 安全提示中点「是」即可（仅当前用户，无需管理员权限；也可展开手动直接打开 `.cer` 文件导入）。
2. **开启协议通道**：点击顶部 **「开启微信协议通道」**，自动启用 PAC 单域名分流（需本机电脑版微信 4.2+）。
3. **采集文章**：粘贴目标公众号任意文章链接或 `__biz` → 点击「识别公众号」→ 复制入口链接发到电脑版微信「文件传输助手」点开 → 点击 **「开始协议采集」**。
4. **筛选与导出**：筛选或勾选文章后打开 **「导出中心」**，选择格式与模板并实时预览下载。
5. **用完还原**：点击 **「停止并还原网络」** 或直接关闭桌面窗口，自动恢复原系统代理设置。

---

## 导出格式与模板

| 导出格式 | 说明 |
| --- | --- |
| **Excel (`.xlsx`)** | 4 张结构化工作表（概览、文章明细、分页审计、失败排查），长 ID 强制文本防截断 |
| **CSV (`.csv`)** | UTF-8 BOM 编码，Excel 直接双击无乱码 |
| **Markdown 图文包 (`.zip`)** | 含 `INDEX.md` + 按公众号分目录 `.md`（YAML Frontmatter）+ 本地图片 `images/` |
| **离线可阅读网页 (`.html`)** | 单文件离线阅读器，Base64 内嵌图片，支持全文搜索 |
| **合并纯文本 (`.txt`)** | 按统一结构合并为干净段落文档，便于直接导入大模型 |
| **结构化数据 (`.jsonl`)** | 每行一条 JSON，适配程序入库与 RAG 流水线 |

内置 **6 套模板**：`完整归档模板`、`含正文表格模板`、`精简阅读模板`、`AI 知识库 / RAG 模板`、`运营分析报表模板`、`自定义字段模板（27 字段自由勾选）`。

---

## 安全与免责声明

- **安全边界**（详见 [SECURITY.md](SECURITY.md)）：服务仅监听 `127.0.0.1`；会话凭据仅留存于微信内存永不落盘；临时证书仅限 `mp.weixin.qq.com` 单域名与当前用户存储；退出自动还原系统代理。
- **免责声明**：本项目仅用于技术学习与个人已授权内容的本地离线备份、知识管理研究。请严格遵守相关法律法规及平台服务条款，切勿用于侵权、未授权商业采集或高频恶意抓取，由此产生的一切后果由使用者自行承担。
