# AI 福利站 | 免费 AI API

## 服务恢复通知（2026-11-27）

11月26日，本站遭遇机器人批量注册，出现大量异常注册请求。为避免资源被集中占用、保障正常用户使用，我们临时关闭了中转站服务。

11月27日，服务已经恢复，可以重新访问网站并按页面说明使用 API。

给受影响的用户带来不便，抱歉。我们会继续关注异常注册情况，并根据实际情况调整防护措施。

[![AI 福利站](assets/banner.svg)](https://apifuli.com)

[![官网](assets/badge-website.svg)](https://apifuli.com) [![QQ群](assets/badge-qq.svg)](#免费邀请码领取) [![免费使用](assets/badge-free.svg)](#额度和使用规则)

[English](README_EN.md)

分享一下自己搭建的 AI 中转站，主要给有 AI 编程、接口调试和日常学习需求的朋友免费使用。

**网站：[apifuli.com](https://apifuli.com)**

## 额度和使用规则

- 注册送 50 API 额度，属于站内余额。
- GPT 分组倍率为 0.01。
- 每日不限量，签到还可以免费领额度。
- 没有充值入口，不需要付费。

**为什么注册只送 50 额度？** 这不是付费试用，也不是引导以后充值。设置这部分额度，主要是为了减少没有实际需求的随手注册、批量注册和恶意占用资源，把有限的免费资源留给真正需要使用的人。额度用完后也不要求充值。

调用接口会扣除站内额度。可用余额、并发和模型状态以站内实际情况为准。

## 免费邀请码领取

为了防止批量注册和恶意刷量，目前注册需要邀请码。

**QQ群：1131913173**

每天在群里免费发放邀请码，有接入问题也可以在群里问。

## 目前支持的模型

```text
gpt-5.6-luna
gpt-5.6-sol
gpt-5.6-terra
gpt-6-astra
gpt-6-luna
gpt-6-sol
gpt-6.1-sol
gpt-6.2-astra
gpt-6.2-sol
gpt6.2-sol
```

以上是站内的模型调用名称，不代表官方模型名称或已验证的上游身份，实际可用情况以站内为准。

另外，站内已新增 **Gemini 系列大模型**。具体可调用的模型名称和实时状态，请以官网模型列表为准；后续还会根据资源情况陆续增加更多模型。

[GPT 6.2 Sol 单次检测报告](docs/model-tests.md)（本次评分 100%）。

## 怎么使用

完整步骤：[Sub2API 使用教程（CC Switch / Cockpit Tools / Codex）](docs/quickstart.md)

1. 进 QQ 群领取邀请码。
2. 打开 [apifuli.com](https://apifuli.com) 注册。
3. 在「API 密钥」页面创建 Key。
4. 点击「使用密钥」，按站内提供的接入信息配置客户端。

## 交流与反馈

- [GitHub Discussions](https://github.com/zhou2040321-prog/free-ai-api/discussions)：交流使用问题、分享接入经验或讨论建议。
- [GitHub Issues](https://github.com/zhou2040321-prog/free-ai-api/issues)：提交可复现的问题或建议，请选择对应模板。

公开发帖前请移除 API Key、密码、个人信息、私人对话和未脱敏日志。

## 模型需求投票

想讨论新增模型，可以[提交模型需求](https://github.com/zhou2040321-prog/free-ai-api/issues/new?template=model-request.yml)，填写模型名称、用途、需求原因和可能的替代选项。其他人可以在 Issue 下留言或用 👍 表达关注；提交不代表模型已上线或一定会加入。

## 测试反馈

欢迎使用[测试反馈模板](https://github.com/zhou2040321-prog/free-ai-api/issues/new?template=model-test-feedback.yml)分享使用模型、场景、响应速度、稳定性和体验。请勿附上敏感内容；个人反馈不等于官方基准测试或可用性承诺。

## 更新日志

项目资料变更记录见 [CHANGELOG.md](CHANGELOG.md)。

## 使用前请注意

请正常使用，不要批量注册、恶意刷量或倒卖邀请码。

网站目前还没有公开完整的隐私政策，请求内容、模型回复和工具调用记录是否保存、共享或另作他用尚未明确。现阶段请只用自己的非敏感测试数据，不要提交私有代码、个人敏感信息、商业秘密或密钥。

这是第三方中转站，并非模型厂商的官方服务。

如果遇到问题，可以在 QQ 群交流，也可以提 Issue。发帖时记得隐藏 API Key 和私人信息。

觉得有用的话，可以点个 Star 方便以后找到。
