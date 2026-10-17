
> [!IMPORTANT]
> # 🚫 Archived / Deprecated
>
> **M365 Insider has been superseded by [M365 Release Radar](https://github.com/alexc-MSFT/m365-release-radar).**
>
> M365 Release Radar is a unified, actively‑maintained agent that combines the **Microsoft 365 Roadmap** and **Azure Updates** (now via the Microsoft Release Communications MCP server) with optional, admin‑gated **Message Center** posts — the best of M365 Insider and Message Center Pulse in one place.
>
> 👉 **Please use [alexc-MSFT/m365-release-radar](https://github.com/alexc-MSFT/m365-release-radar) going forward.** This repository is kept for historical reference only and will no longer receive updates.

---

# M365 Insider — Microsoft 365 Roadmap Copilot Agent 🔎

![M365 Insider Agent Screenshot](m365-insider-screenshot.png)

**M365 Insider** is a declarative agent built in the Agents Toolkit for Microsoft 365 Copilot that helps users/administrators query and explore the **Microsoft 365 Roadmap** - surface upcoming features, filter by product/area, and answer roadmap questions quickly and consistently. It leverages adaptive cards to provide consistent formatting in responses.

It uses an API plugin to leverage the Microsoft 365 Roadmap public REST API (https://www.microsoft.com/releasecommunications/api/v1/m365).

It’s designed to be lightweight, web‑grounded, and easy to deploy with the **Microsoft 365 Agents Toolkit** in Visual Studio Code.  

This repository contains basic deployment details for running and publishing the agent in your own Microsoft 365 environment (it assumes a proficient level of knowledge with the Agents Toolkit).


---

## ✨ What it does (current iteration)

- Answers questions about Microsoft 365 Roadmap items. 
- Helps users filter by Products (Teams, Outlook, SharePoint, etc.), Status (Launched, Rolling out), Feature ID and many more.
- Provides quick summaries to support adoption, planning, and release communications.
- Leverages adaptive cards to provide rich information about each roadmap item.

Suggested prompts to try:
- *“What’s coming for Microsoft Teams in the next quarter?”*  
- *“Show roadmap items related to SharePoint admin experiences announced last month.”*  
- *“List features currently in ‘Rolling out’ status for Outlook.”*

![M365 Insider Agent Response Screenshot](m365-insider-response-screenshot.png)

##  Future iterations

Some ideas for future iterations of the agent are as follows:

- Ability to query/retrieve Message Center posts (via Service Communications Graph API).
- Combine relevant MC posts and roadmap items together in responses.
- Ability to 'follow' roadmap items/MC posts for updates - notifications via Adaptive Cards.
- Ability to ask questions about items the user 'follows'.
- Ability to send email/teams summaries of items when prompted.

---

## 🚀 Getting Started

You can deploy directly from VS Code using the **Microsoft 365 Agents Toolkit** (evolution of Teams Toolkit) and publish the agent to your organization or test locally, see [Microsoft 365 Agents Toolkit Overview](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/agents-toolkit-fundamentals).

1. Ensure you have the Agents Toolkit extension for Visual Studio Code installed ([Install Agents Toolkit](https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/install-agents-toolkit?tabs=vscode#install-a-prerelease-version))
2. Clone the [repo](https://github.com/alexc-MSFT/m365-insider.git) to your machine .
3. Open the folder in Visual Studio Code and follow the steps in ([Tutorial: Create declarative agents by using Microsoft 365 Agents Toolkit](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/build-declarative-agents)) to provision the agent.
4. Deploy the agent for all/desired users through the MAC.

---

## 🎨 Customising the Agent

- **Name**: Feel free to change the name of the agent to suit your needs.
- **Instructions**: Refine the agents instructions and responses by editing the instruction.txt file.  
- **Knowledge**: Add public websites or internal knowledge sources to improve coverage.  
- **Actions**: Add additional API plugins as required.

---

## 🤝 Contributing

Contributions are welcome! 

If you'd like to improve the agent, update documentation, suggest new ideas etc. please open an issue or submit a PR.

Open an issue or submit a PR if you’d like to improve prompts, filters, or documentation.

---

## Support

This solution is open-source and community provided with no active community providing support for it. This solution is maintained by both Microsoft employees and community contributors and is not a Microsoft provided solution so there is no SLA or direct support for this from Microsoft. Please report any issues by raising an issue.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
