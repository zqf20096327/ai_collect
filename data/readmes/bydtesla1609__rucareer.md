# RUCareer · 个人经历档案

> Pack your proof. Tell your lore.

RUCareer 是一款面向大学生的 Windows 本地经历管理与 AI 简历生成工具。它不是让 AI 凭空“造人设”，而是把用户真实做过的事、写过的材料和留下的证明收进一个本地包装盒，再针对具体申请目标整理成一条清楚、可信的 storyline。

当前桌面版本：`1.0.0`。默认启动 V8 风格的 RUCareer · 鹿路录桌面 App，界面由 WebView2 承载，资料由本地 Python 服务保存。

## 直接运行桌面版

安装版入口为 `dist/installers/RUCareer-Setup.exe`：选择安装位置、是否创建桌面快捷方式，再安装。程序内置 Python 和 PDF 生成能力；缺少 WebView2 时由安装器联网补齐。升级和卸载仅管理程序文件，个人档案独立保留。当前是未签名体验包，不等同于正式签名发行。

Windows 构建：`build-installer.ps1`。Mac 构建：在真实 Mac 运行 `bash build-macos.sh`，产生拖入 Applications 的 DMG 候选包；正式发行还需 Developer ID 签名、公证和真机验收。不要在 Windows 上伪造 Mac 安装包。下载页源代码独立位于 `download-site/`，发布状态见 `installer/RELEASE-CHECKLIST.md`。

第一次运行时点击“新建文件夹”并选择存放位置，或选择原来的 RUCareer 包装盒。初始界面不再包含虚构示例数据；数量、近期活动和证据情况均根据当前档案计算。

桌面版包括：

- 信息概览及基础信息编辑；专业能力、社会实践、兴趣档案的真实增删改与附件管理。
- 分类再次点击取消筛选、可搜索列表、原始事实和可编辑 AI 草稿分开保存。
- 申请要求、手动/AI 选材、五套内置模板、基础稿/AI 稿、正文编辑、核验和 DOCX/PDF 导出。
- 每日自动备份、手动备份、恢复到新目录、删除前备份和本地回收副本。
- API 请求发送前预览；可选用 Windows DPAPI 保存加密密钥，密钥不进入包装盒。
- 旧包装盒兼容打开、每天检查官方版本、用户主动下载更新。

AI 功能使用您自行填写的 OpenAI 兼容服务和密钥。尚未配置时，本地编辑、附件、基础简历和导出可以正常使用。外部模板导入/解析属于 PRE 的后续阶段，本版提供五套内置模板。

源码运行：`.venv/Scripts/python.exe main.py`。重新打包：`powershell -ExecutionPolicy Bypass -File build-desktop.ps1`。旧 Tk 界面仍可用 `main.py --legacy` 启动，用于兼容回查。

桌面验证：`.venv/Scripts/python.exe -X utf8 -m unittest discover -s tests -v`；`website/qa-desktop.cjs` 会在临时目录跑完整的界面与真实本地服务交互，不操作用户包装盒。

以下保留旧版本的数据格式与开发说明；V8 桌面版的运行入口和密钥保存方式以上述说明为准。

不想安装 Python，可以从 [GitHub Releases](https://github.com/bydtesla1609/rucareer/releases) 下载 Windows 预览版 `RUCareer.exe`。当前安装包尚未购买代码签名证书，Windows 可能显示来源提醒；请只从本仓库 Release 页面下载并核对随 Release 提供的 SHA-256。

## 现在能做什么

- 在用户指定的本地文件夹中创建包装盒，无需注册或登录。
- 以五个档案页签整理基础信息、科创经历、社会实践、兴趣爱好和简历生成。
- 保存姓名、学校、学号、联系方式、绩点、专业、排名和兴趣爱好等基础信息。
- 按科研、项目、竞赛、实习、社会实践、志愿服务、实践项目、国际校际交流等分类记录经历；每条经历只选一个分类。
- 每条经历拥有独立文件夹，可附加 TXT、Markdown、CSV、JSON、DOCX、PDF 等材料。
- 用户填写自己的 OpenAI 兼容 API 地址、模型和 API Key，让 AI 结合原始叙述与附件生成“AI 叙述”。
- 针对岗位、研究生项目、交流活动等要求生成分析报告，并由 AI 初选经历；用户可以随时增删。
- 使用基础模板或 AI 生成简历正文，继续手动编辑后导出 DOCX、PDF。
- 每日最多自动创建一次本地备份并保留最近 7 份，也可以随时手动备份；恢复时始终创建新包装盒，不覆盖当前数据。
- 每日自动检查一次官方 GitHub Release。发现新版本后可以立即打开下载页、稍后提醒或忽略该版本，绝不强制更新。
- 正确适配 Windows 高 DPI 显示缩放；“界面大小”可以在 90%–150% 之间调整，`Ctrl++` / `Ctrl+-` 缩放，`Ctrl+0` 恢复推荐大小。

AI 只能润色和提炼已有事实。提示词明确禁止虚构数字、职责、奖项与结果；缺失信息应显示为 `【待补充】`。最终内容仍需用户核验。

## Windows 快速运行

需要 Python 3.12 或更高版本。

```powershell
git clone https://github.com/bydtesla1609/rucareer.git
cd rucareer
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

脚本会在仓库内创建 `.venv`、安装两个文档读取/导出依赖，然后启动桌面应用。

也可以手动运行：

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

仓库自带一个无真实个人信息的示例盒子：`examples/demo-box`。启动后选择“打开包装盒”即可查看；点击“新建包装盒”可以先填写名称、再选择存放位置，由应用自动创建完整目录。

## 创建 Windows EXE

```powershell
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

完成后得到 `dist/RUCareer.exe`。构建脚本使用 PyInstaller，只影响本地虚拟环境；构建产物不会提交到 Git。

`build.ps1` 只用于本地开发构建。正式公开发布必须使用代码签名证书：

```powershell
$env:RUCAREER_CERT_THUMBPRINT = "证书指纹"
powershell -ExecutionPolicy Bypass -File .\build-release.ps1
```

`build-release.ps1` 会拒绝无证书或无 `signtool.exe` 的构建，签名并复核 `RUCareer.exe`，随后生成 `dist/SHA256SUMS.txt`。证书本身不存放在仓库中。

## 本地数据长什么样

RUCareer 不把经历锁进在线账号。包装盒本身就是一个普通文件夹：

```text
我的包装盒/
├─ rucareer-index.json
├─ profile.json
├─ experiences/
│  └─ <经历 ID>/
│     ├─ experience.json
│     └─ attachments/
├─ applications/
└─ exports/
```

这些文件可以直接复制和备份。首版不提供本地加密，因此请像保护其他个人资料一样保护包装盒所在文件夹。

新建档案使用 RUCareer 索引。旧版的 `lorecase.json`、格式标记和备份目录继续兼容读取，不批量改动已有资料。应用源码模块与 GitHub 仓库统一命名为 `rucareer`。

## 官网与代码仓库

App 源码（`rucareer/`）、桌面界面（`website/`）、安装器（`installer/`）和官网（`download-site/`）共用 [rucareer 仓库](https://github.com/bydtesla1609/rucareer)。Cloudflare 的构建根目录设为 `download-site`；具体命令和授权边界见 [官网发布说明](download-site/README.md)。个人档案、密钥、安装包和本地备份不提交到 Git。

自动备份存放在包装盒旁边的 `<包装盒名称> - RUCareer备份` 文件夹中，而不是包装盒内部。升级前会额外创建不参与日常清理的备份。应用内的“备份与恢复”可以查看位置、立即备份和恢复；恢复结果使用新文件夹，避免覆盖当前数据。

API Key 不会写入包装盒、设置文件或 Git 仓库，只存在于当前应用运行期间；退出后需要重新填写，也可以通过 `OPENAI_API_KEY` 环境变量提供。

## AI 服务

打开应用右上角的“AI 设置”，填写：

- OpenAI 兼容 API 地址，例如 `https://api.openai.com/v1`
- 模型名称
- 你自己的 API Key

基础资料、经历管理、基础简历和文件导出都不依赖 AI。只有点击 AI 叙述、需求分析或 AI 生成简历时，相关文本与可读取附件内容才会发往用户配置的服务。

发送前，RUCareer 会让用户决定经历润色时是否包含附件文字，以及生成简历时是否包含基础资料。取消操作不会发送内容。

## 更新说明

- 自动更新检查只访问本仓库的 GitHub Release 接口，不上传包装盒或个人资料。
- 应用不会后台下载或强制安装版本；用户决定是否打开官方发布页。
- 打开更新页前，如果当前已有包装盒，RUCareer 会先创建升级前备份。
- 新版本打开旧格式包装盒时，会先备份再迁移；来自更高格式版本的包装盒会要求先更新应用。

## 导出说明

- DOCX 由 `python-docx` 生成。
- PDF 通过 Windows 自带的 Microsoft Edge 无界面打印生成；如果未找到 Edge，RUCareer 会保留可手动打印的 HTML。

## 验证

```powershell
python -m unittest discover -s tests -v
python -m compileall -q rucareer main.py
```

自动检查覆盖包装盒创建、资料与经历往返保存、附件读取、AI 分析结果过滤、基础简历、HTML 转义、DOCX 导出和申请任务保存。

## 已确认但尚未进入首版

- 多套复杂模板及模板创作、导入、收藏和删除。
- Canva 登录授权、往返导航、再次打开设计及导出结果同步。
- macOS 分发与签名。
- 平台托管 AI、用户账号、云同步和多人共享。

这些能力不会先搭空壳；当前主线稳定并经真实用户验证后再加入。

## 隐私边界

- RUCareer 不要求产品账号，也不默认上传整个包装盒。
- 学号、电话、微信等敏感字段只有在用户主动用于生成内容时才会进入相应 AI 请求。
- 附件只在用户主动点击某条经历的“AI 美化叙述”时读取。
- 导出前请检查 AI 生成文字，确保每一项事实都能由原始材料支持。

## 项目状态

RUCareer 目前是公开的早期 MVP。欢迎通过 Issue 提交能够复现的问题，但请勿上传真实简历、证件、API Key 或包含隐私的包装盒。

## RUCareer 保存与 AI 辅助更新（2026-09-08）

新版 Windows 入口为 `dist/save-ai-update/RUCareer/RUCareer.exe`，分发包为 `dist/RUCareer-v1.0.0-save-ai-update-Windows.zip`。请先保存并关闭旧窗口，再打开新版；这次没有覆盖正在运行的旧程序。

- 首次自动显示聚光灯分步引导，支持上一步、下一步和跳过；完成或跳过后不再自动播放。
- “使用指引”入口仅保留在左下角，可重播同一套九步介绍，自动依次展示五个栏目。简历指引已删除多余的发送提醒。
- 切换时暂存原页面节点，结束或跳过后恢复原页面和弹窗；不提交表单、覆盖草稿、上传附件或调用 AI。
- 选中导航项的文字居中；软件图标统一为鹿角与档案页标志，Windows 11 原生窗口标题栏和边框同步使用品牌色。
- 常见问题补充了 API Key 获取与配置、模型和基础地址、密钥保护及错误排查。
- 保存增加临时文件落盘后原子替换、旧表单版本检测、失败时保留输入及持久提示。Ctrl+S 优先保存当前弹窗。
- 三个记录栏目及简历任务的 AI 输出先保存为可编辑、可重开的本地待采用草稿。确认采用后才替换原稿，采用前备份；检测到资料变化则保留草稿供对照。
- 界面专项验收：`node website/qa-guide.cjs`、`node website/qa-persistence.cjs`；完整验收范围见 `DESKTOP-ACCEPTANCE.md`。AI 流程使用模拟返回，不使用真实密钥或发起付费请求。
