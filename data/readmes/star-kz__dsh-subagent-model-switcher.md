# DSH-Subagent-Model-Switcher

**子 agent 会话模型切换** —— 给 [DeepSeek Harness](https://github.com/deepseek-ai/DeepSeek-Harness) 子会话输入框补上「模型 + 思考强度」选择器。

`@k-launcher/dsh-subagent-model-switcher` · v1.0.0 · MIT

## 功能

- 仅在子 agent 会话显示，主会话不渲染、不改变官方选择器。
- 可切换模型与思考强度；运行中的子 agent 在后续请求生效。
- 选择按会话保存，重启后仍有效；也可清除覆盖，恢复默认继承。
- 使用插件 Host 端的设置覆盖与 agent 事件，不调用官方会拒绝子会话的 `session/selectModel`。

## 安装

在 DSH 插件管理中安装：

```
github:star-kz/dsh-subagent-model-switcher
```

需要 DSH Web 与 `@deepseek-ai/schemastery`（已在 `peerDependencies` 声明）。

## License

[MIT](LICENSE)：允许自由使用、修改和分发，包括商业用途。
