<div align="center">
<img src="./docs/images/icon.svg" alt="icon"/>

<h1 align="center">ChatGPT SDImg Web</h1>

集成部署ChatGPT+SD webUI绘图网页应用。

[演示](https://xsai.online/) / [反馈](https://github.com/chengxs1994/ChatGPT-SDImg-Web/issues)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fchengxs1994%2FChatGPT-SDImg-Web&env=OPENAI_API_KEY&env=CODE&project-name=chatgpt-sdimg-web&repository-name=ChatGPT-SDImg-Web)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/chengxs1994/ChatGPT-SDImg-Web)

</div>

## 项目定位

ChatGPT SDImg Web 是一个面向自托管场景的 AI Web 应用模板，在 ChatGPT 对话能力之外集成 Stable Diffusion WebUI 绘图、用户账号、次数/积分限制、分享和部署配置。项目适合用于学习、二次开发和验证完整 AI 应用的前后端集成方式。

本仓库由 [@chengxs1994](https://github.com/chengxs1994) 维护。欢迎通过 Issue 和 Pull Request 反馈可复现问题、部署经验、安全改进和文档补充。

## 维护状态

- 当前维护重点：依赖安全、部署文档、认证/额度逻辑、OpenAI/Stable Diffusion API 调用链路。
- 问题反馈：请优先使用 [GitHub Issues](https://github.com/chengxs1994/ChatGPT-SDImg-Web/issues)，并提供复现步骤、部署方式、日志和截图。
- 贡献方式：提交 PR 前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)。
- 安全问题：请阅读 [SECURITY.md](./SECURITY.md)，不要在公开 Issue 中粘贴 API Key、Cookie、Token 或生产日志。
- 近期计划：见 [ROADMAP.md](./ROADMAP.md)。

## Security and maintenance

This repository contains security-sensitive surfaces such as OpenAI API keys, user authentication, quota/credit logic, external Stable Diffusion/OpenAI API calls, Docker/Vercel deployment templates, and third-party contributions. Security reviews and maintenance automation should focus on preventing key leakage, auth bypass, unsafe server routes, dependency risks, and deployment misconfiguration.

## 主要功能

- ChatGPT问答
- SD webUI AI绘画
- 用户注册登录，个人中心
- 次数限制，积分充值
- 邀请码，邀请链接分享
- AI二维码

## 本地开发

1. 安装 Node.js 18 和 Yarn。
2. 复制 `.env.template` 并按需配置 `OPENAI_API_KEY`、`CODE`、`BASE_URL` 等环境变量。
3. 执行 `yarn install && yarn dev` 启动本地开发环境。注意：此命令仅用于本地开发，不要用于生产部署。
4. 如果你想本地部署，请先执行 `yarn build`，再使用 `yarn start`，也可以配合 pm2 守护进程。

## 开源计划

- [x] ChatGPT 问答
- [x] SD WebUI AI 绘画
- [x] 用户注册登录
- [x] 个人中心、次数限制、积分充值
- [x] 邀请码、邀请链接分享
- [x] AI 视频生成
- [x] AI 二维码
- [x] 后台功能
- [x] 调用其他平台 API
- [ ] 整理部署安全清单
- [ ] 补充接口和环境变量说明
- [ ] 增加关键业务逻辑的回归测试
- [ ] 定期检查前端、后端和 Docker 依赖风险

<div align="center">

## 效果展示
#### AI二维码，扫码加好友
<div>
<img src="./docs/images/aiewm.jpg" style="width: 45%" />
</div>

![cover](./docs/images/img.jpg)

![cover](./docs/images/img2.jpg)

![cover](./docs/images/user.jpg)

![cover](./docs/images/img3.jpg)

![cover](./docs/images/admin-login.jpg)

![cover](./docs/images/admin1.jpg)

![cover](./docs/images/admin2.jpg)

</div>

## 加入我们
<div>
<img src="./docs/images/wx1.jpg" style="width: 45%" />
<img src="./docs/images/wxg2.jpg" style="width: 45%" />
<img src="./docs/images/qq.jpg" style="width: 45%" />
<img src="./docs/images/qqg.jpg" style="width: 45%" />
</div>

## 最后

### 方便的话，帮忙给项目一个宝贵的star哈，谢谢啦！
