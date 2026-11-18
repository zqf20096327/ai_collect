# 学习通外挂 v10.6 · CX Sign-in Tool

**位置签到一键完成 · AI 一键做题 · 作业自动填写提交**

![平台](https://img.shields.io/static/v1?label=平台&message=Android&color=3DDC84&logo=android&logoColor=white)
![包名](https://img.shields.io/static/v1?label=包名&message=com.cx.signin&color=blue)
![版本](https://img.shields.io/static/v1?label=版本&message=v10.6&color=brightgreen)
![体积](https://img.shields.io/static/v1?label=体积&message=425_KB&color=lightgrey)
![题库](https://img.shields.io/static/v1?label=答题&message=DeepSeek_驱动&color=purple)
![年龄](https://img.shields.io/static/v1?label=使用&message=自担风险&color=critical)
![版本](https://img.shields.io/github/v/release/supermandiao/cx-signin-tool?label=版本&color=blue)
![下载量](https://img.shields.io/github/downloads/supermandiao/cx-signin-tool/total?label=下载量&color=orange)

### ⬇️ [立即下载 v10.6（425 KB）](../../releases/latest)

> **不是修改版学习通，是外挂工具**：独立 App，靠 WebView 加载你自己的学习通登录态，再调 DeepSeek 帮你点签到、填作业。**学习通官方不受影响、也与此无关。**
>
> ⚠️ **使用外挂签到、代做题属于学术不端**：可能被平台风控识别、被学校按校规处理，最重可至记过/取消成绩。**仅限你完全知情下自行承担后果的场景使用。**

---

## 一分钟看懂

| 你可能想知道的 | 答案 |
| --- | --- |
| 要 root 吗 | **不用**，普通安装即可 |
| 要装学习通吗 | 要，登录态共用系统的学习通 |
| 要自己配什么 | 填你自己的 DeepSeek API Key（给 AI 答题用） |
| 能改成绩吗 | 不能，只做签到定位与作业作答填充 |
| 会被发现吗 | 有风险：签到位置、答题速度、提交时间都可能被风控标记 |
| 收费吗 | 免费，仓库内不含任何激活/卡密逻辑 |

## 功能

### 签到

| 类型 | 自动化程度 |
| --- | --- |
| 普通签到 | ✅ 全自动 |
| 位置签到 | ✅ 全自动（没有坐标时自己测距反解老师设的点） |
| 签到码签到 | ✅ 全自动（从活动信息里扒码） |
| 手势签到 | 半自动（九宫格画一遍） |
| 二维码签到 | 半自动（点「扫一下就签」扫一次） |
| 拍照签到 | 半自动（先上传一张照片） |

### 作业 / 考试

| 题型 | answertype | 自动化程度 |
| --- | --- | --- |
| 单选题 | 0 | ✅ 全自动 |
| 多选题 | 1 | ✅ 全自动（支持 BE、AC 这类组合） |
| 填空题 | 2 | ✅ 全自动 |
| 判断题 | 3 | ✅ 全自动 |
| 简答题 | 4 | ✅ 全自动（自动分段） |
| 程序题 | 17 | ✅ 全自动（写进 CodeMirror，可编译运行） |
| 截图题 | — | ❌ 答不了，需自己补图 |

## 三步上手

**签到**：输手机号 + 密码 → 登录 → 打开「自动签到」开关 → 完事，老师发签到 30 秒内自己签掉。

**作业**：填 AI 设置（接口 `https://api.deepseek.com/v1`、模型 `deepseek-chat`、你自己的 `sk-...`）→ 点「检测连通」出现「通了（xxx ms）」→ 进作业页 → 点「一键做题」→ 检查 → 提交。

任何 OpenAI 兼容接口都行，通义千问、智谱、Kimi 改地址和模型名即可。

## 注意事项

- **程序题交了就重做不了**，提交前务必看一眼。
- 签到可以全自动，作业建议人工扫一眼再交。
- 页面缩放已开启，双指可缩放。
- 登录态过期会标红，重新登录一次。
- 完整说明见 [USAGE.md](USAGE.md)。

## 包信息

| 项 | 值 |
| --- | --- |
| 包名 | `com.cx.signin` |
| 版本 | versionName 10.6 |
| 签名 | `CN=ZhanShen`（v1） |
| 体积 | 434,857 字节 |
| 结构 | 单 dex + WebView 前端（`assets/index.html`）+ Leaflet 地图 |
| 权限 | 网络、前台服务、通知、精确定位/粗略定位、相机、开机自启 |
| 外部请求 | `api.deepseek.com`（你的 Key）、`*.chaoxing.com`（你的登录态） |

代码里**没有硬编码的 Key 或后门地址**，API Key 由你在 App 内填写，只存本机。

## 安装

1. 手机装好官方「学习通」并登录（本工具共用它的登录态）。
2. 安装本 App（允许未知来源）。
3. 首次打开按「三步上手」配置。
4. 若要后台自动签到：系统设置里允许自启、允许通知、关掉对它的电池优化，否则会被杀。

## 校验

```
文件：cx-signin-v10.6.apk
大小：434,857 字节
SHA-256：1a63b27b532ce20d16ed4003c40f1136ce22837d8898a146b8cf15467afac145
签名：v1（CN=ZhanShen）
```

```bash
sha256sum cx-signin-v10.6.apk
```

## 已知问题

- 学习通改版会导致选择器失效，签到/答题可能需要等更新。
- AI 答题正确率取决于模型与题目类型，程序题、图表题经常错，**别闭眼提交**。
- 位置签到依赖系统定位权限；部分机型需要开启「模拟位置」或开发者选项。
- 未签名证书自签，部分手机会提示风险；应用商店不会收录。
- 学校若启用行为风控（异常定位、秒答、批量提交），被标记的概率不低。
- 本仓库只分发 APK，不含源码。

## 作者

战神（个人开发），本版界面与说明由作者提供。

## 免责声明

见 [DISCLAIMER.md](DISCLAIMER.md)。要点：**与超星/学习通官方无关；外挂签到与代做题属学术不端，后果自负；不提供任何学术或法律建议；不担保不被发现；责任上限为零。**

---

**English (short)**: An Android helper for Chaoxing/XueXiTong: fake-location check-in and AI-assisted homework filling via your own DeepSeek API key. Not affiliated with Chaoxing. Using it is academic misconduct — you bear all consequences.
