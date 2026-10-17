<p align="right">
  <a href="./README.zh.md">中文</a> | English
</p>

<p align="center">
<a href="https://github.com/widget-js/widgets">
  <img width="150" src="https://raw.githubusercontent.com/widget-js/widgets/master/screenshot/logo.png" alt="Widgets - Capable and ergonomic widgets." width="300">
</a>
<br>
桌面组件 - Widget Hub
</p>

<p align="center">
  <img src="https://img.shields.io/badge/QQ%20Group-701784679-EB1923?logo=tencentqq&logoColor=white&sanitize=true" alt="Chat">
  <a href="https://space.bilibili.com/207395767"><img src="https://img.shields.io/badge/-Bilibili-00A1D6?logo=bilibili&logoColor=white" alt="bilibili"></a>
  <a href="https://discord.gg/vwSAaRR8cT"><img src="https://img.shields.io/badge/-Discord-5865F2?logo=discord&logoColor=white" alt="discord"></a>
</p>

![png](screenshot/screenshot.jpg)
![png](https://github.com/rtugeek/stock/raw/master/public/screenshot.png)

## 🔗 Preview All Widgets

https://widget-js.github.io/widgets/#/

![png](screenshot/react.png)


## 🤖 Generate Desktop Widgets with AI

#### 1. Install Software
- AI coding tool (`Claude Code`, `Trae`, `Codex`, etc. — choose any one)
- Node.js
- [WidgetHub Desktop Client](https://github.com/widget-js/widgets/releases)

#### 2. Install Skill
```shell
npx skills@latest add widget-js/skills
```

#### 3. Configure the MCP Server in Your AI Coding Tool
```json
{
  "mcpServers": {
    "widgetjs": {
      "transport": "streamableHttp",
      "url": "http://127.0.0.1:3606/mcp"
    }
  }
}
```

#### 4. Invoke the Skill and Enter a Prompt
```
/widget Generate a stock widget, 4 by 4 in size, where users can select stock codes and the widget displays real-time prices and price changes.
```

![](/screenshot/stock.png)

[📃 Full Documentation](https://widgetjs.cn/guide)
