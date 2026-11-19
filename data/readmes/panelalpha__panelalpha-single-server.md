<div align="center">

<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset=".github/assets/panelalpha.svg"><img src=".github/assets/panelalpha-light.svg" alt="PanelAlpha Single Server Edition" width="360"></picture></p>

<h1>A hosting panel<br>for your own server.</h1>

<h3>
Sites, domains, backups and staging in your browser. It runs on PanelAlpha Engine.
</h3>

<h3>
<a href="#get-the-panel-running"><b>Get started</b></a> ·
<a href="https://www.panelalpha.com/documentation/single-server-edition"><b>Documentation</b></a> ·
<a href="#talk-to-us-on-discord"><b>Discord</b></a>
</h3>

<p>
<a href="#where-to-find-things">In the panel</a> ·
<a href="#connect-your-ai-assistant">Connect AI</a> ·
<a href="#panelalpha-hub">Hub</a> ·
<a href="#faq">FAQ</a>
</p>

<p>
<b>English</b>
· <a href=".github/readme/README.pl.md">Polski</a>
· <a href=".github/readme/README.de.md">Deutsch</a>
· <a href=".github/readme/README.nl.md">Nederlands</a>
· <a href=".github/readme/README.es.md">Español</a>
· <a href=".github/readme/README.fr.md">Français</a>
· <a href=".github/readme/README.it.md">Italiano</a>
· <a href=".github/readme/README.pt-BR.md">Português</a>
· <a href=".github/readme/README.uk.md">Українська</a>
· <a href=".github/readme/README.ar.md">العربية</a>
· <a href=".github/readme/README.zh-CN.md">简体中文</a>
</p>

<p>
<a href="#step-1-install-the-panel-on-your-vps"><img src="https://img.shields.io/badge/PanelAlpha_Engine-2.3.0+-E65E12" alt="Requires PanelAlpha Engine 2.3.0 or later"></a>
<a href="#step-1-install-the-panel-on-your-vps"><img src="https://img.shields.io/badge/Debian_12%2F13-Ubuntu_22.04%2F24.04%2F26.04-a80030" alt="Supported OS"></a>
<a href="#licence"><img src="https://img.shields.io/badge/license-Apache_2.0-0b7285" alt="Apache 2.0"></a>
<a href="https://discord.gg/9twHWR7xGX"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Join Discord"></a>
</p>

</div>

---

## What is PanelAlpha Single Server Edition?

PanelAlpha Single Server Edition is a web hosting panel you install on your own VPS. You open it in a browser and look after your sites there: WordPress, apps from Git, domains, backups and the rest. PanelAlpha Engine does the hosting underneath, and the panel gives you a screen for it.

The Community edition is for one person and has no project limit. In the panel you can:

- Create a WordPress site, deploy an app from Git or from files, or install a tested app from the PanelAlpha GO! catalog
- Import a WordPress site from another host
- Add domains, with certificates from Let's Encrypt
- Take backups by hand or on a schedule, and restore them
- Keep a staging copy of a site and push it live
- Manage databases, cron jobs, FTP and SFTP accounts and PHP settings
- See visitor statistics, usage and logs
- Connect an AI assistant and manage your projects by chat
- Connect the server to your PanelAlpha Hub account and sign in with it

## How it works

<div align="center"><img src=".github/assets/panelalpha-tour.gif" alt="A tour of the panel: creating a project from PanelAlpha GO!, the project page, staging and Push To Live, and Connect AI" width="800"><br><a href=".github/assets/panelalpha-tour.mp4">Watch the full tour (2.5 min, MP4)</a></div>

The panel is one project on the engine, in its own container. When you create a site, the panel asks the engine API to do it, and the engine gives that site a project of its own. Removing the panel deletes only the panel's project. Your sites keep running.

## Why use the panel

PanelAlpha Engine is run from an AI assistant or from the `pae` command on the server. The panel puts the same work on a screen. You can add a domain, restore a backup or push a staging copy live with a few clicks, and see every site on the server in one list. When you want an assistant to help, you connect it to the panel and it works on the same projects.

## Get the panel running

### Step 1: Install the panel on your VPS

You need a fresh Debian 12/13 or Ubuntu 22.04/24.04/26.04 server with 2 GB of RAM, `root` access over SSH and a domain pointed at it. **Port 80 must be open to everyone**, because Let's Encrypt uses it.

```bash
curl -fsSL get.panelalpha.com/single-server | sh
```

Every option and the Engine version the panel needs: [Installing the panel](https://www.panelalpha.com/documentation/single-server-edition/getting-started/install).

### Step 2: Sign in

Open `https://panel.example.com`. The setup wizard creates your account, or connects your PanelAlpha Hub account, and opens the panel: [First login](https://www.panelalpha.com/documentation/single-server-edition/getting-started/first-login).

### Step 3: Create your first site

Go to **My Projects**, select **Create First Project** and choose **WordPress**, **Git**, **Files** or **PanelAlpha GO!**. You can also drop a `.zip` or `.tar.gz` archive straight onto the project list: [Create a project](https://www.panelalpha.com/documentation/single-server-edition/projects/create-a-project).

**PanelAlpha GO!** is a catalog of open-source apps that PanelAlpha deployed and tested on PanelAlpha Engine. You pick an app and the panel installs it, with nothing else to fill in. The catalog shows once the panel is connected to [PanelAlpha Hub](#panelalpha-hub).

<div align="center">
<a href="https://www.panelalpha.com/documentation/single-server-edition/projects/create-a-project"><img src="https://skillicons.dev/icons?i=wordpress,php,laravel,nodejs,nextjs,python,docker,git&perline=8" alt="WordPress, PHP, Laravel, Node.js, Next.js, Python, Docker, Git"></a>
<br>
WordPress, or any app the engine can build from a Git repository or a folder of files.
</div>

## Where to find things

Select **Manage** on a project to open it. Its tabs are **Project Details**, **Monitoring**, **Backups**, **Plugins** and **Advanced**. **Plugins** shows only on a WordPress site.

| You want to | In the panel |
|:---|:---|
| Put your own domain on a site | **Advanced > Domains**, then **Add Domain** |
| Take a backup, or back up on a schedule | **Backups** tab. Set up a store once in **Settings > Backups** |
| Try a change before it goes live | **Staging** in the project's top bar, then **Push To Live** |
| Redeploy on every git push | **Advanced > Git**, then **Auto-deploy on push** |
| Move a WordPress site from another host | Create a project, **WordPress**, then **Import Existing WordPress Project** |
| Add a database and a user for it | **Advanced > MySQL Databases** |
| Give someone SFTP access | **Advanced > SFTP Accounts** |
| Run a script on a schedule | **Advanced > Cron Jobs** |
| Change the PHP version or `memory_limit` | **Advanced > Developer Settings** |
| See how many people visit | **Monitoring** tab |

## Everything a site needs, in the panel

- **Domains and HTTPS.** Point your own domain at a site, add more domains and redirects, and give each one a Let's Encrypt certificate. With no domain yet, use a free subdomain when your server offers one. [Domains and SSL](https://www.panelalpha.com/documentation/single-server-edition/looking-after-a-project/domains-and-ssl)
- **Backups you can restore.** Back up by hand or daily, weekly or monthly, to S3, SFTP, FTP, FTPS or a local folder. On a WordPress site you can restore the files and the database separately. [Backups](https://www.panelalpha.com/documentation/single-server-edition/looking-after-a-project/backups)
- **Staging.** Make a copy of a site, try your changes there, then push the files, the full database or selected tables to the live site. A Git project can deploy a branch to staging and leave production alone. [Staging and preview](https://www.panelalpha.com/documentation/single-server-edition/projects/staging-and-preview)
- **Git.** See how many commits behind the site is, redeploy, switch branch and follow the deploy log as it runs. With auto-deploy on, a push to GitHub, GitLab or Bitbucket redeploys the site. [Git](https://www.panelalpha.com/documentation/single-server-edition/projects/git)
- **WordPress.** Sign in to the dashboard without a password, update WordPress and WooCommerce, install plugins and themes by their wordpress.org name, manage WordPress users and turn on automatic updates. [Managing WordPress](https://www.panelalpha.com/documentation/single-server-edition/projects/wordpress)
- **Files, FTP and SFTP.** Edit, upload, zip and unzip files in the file manager, or give a program such as FileZilla an FTP or SFTP account. [Files and access](https://www.panelalpha.com/documentation/single-server-edition/looking-after-a-project/files-and-access)
- **Databases.** Create MySQL databases and users, set their privileges and open phpMyAdmin from the panel. [Databases](https://www.panelalpha.com/documentation/single-server-edition/looking-after-a-project/databases)
- **Statistics and logs.** Visits by country, referrer and device, bandwidth, the CPU, RAM and disk of the whole server, and the PHP and web server logs of each site. [Statistics and logs](https://www.panelalpha.com/documentation/single-server-edition/looking-after-a-project/statistics-and-logs)

## Connect your AI assistant

You connect your assistant from the panel, on the **Connect AI** page in the top menu.

1. Open **Connect AI** and pick your tool under **Your tool**.
2. Under **Generate an MCP token**, select **Create Token**, give it a name such as `Claude on my laptop` and copy it. **The token is shown once.**
3. The next step shows what to put into your tool, with your panel address already filled in. Select **Copy**, paste it into your tool and replace `YOUR_TOKEN` with your token.
4. Follow **Verify the connection** on the same page. In Claude Code, restart it or run `/mcp`.

Then ask in the chat, for example `List my projects.`

<div align="center">

<a href="https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai"><img src="https://github.com/claude.png" width="46" alt="Claude Code"></a>&nbsp;&nbsp;
<a href="https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai"><img src="https://github.com/openai.png" width="46" alt="ChatGPT, Codex"></a>&nbsp;&nbsp;
<a href="https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai"><img src="https://github.com/cursor.png" width="46" alt="Cursor"></a>&nbsp;&nbsp;
<a href="https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai"><img src=".github/assets/windsurf.png" width="46" alt="Windsurf"></a>&nbsp;&nbsp;
<a href="https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai"><img src="https://skillicons.dev/icons?i=vscode" width="46" alt="VS Code"></a>

<sub><b>Claude Code&nbsp; · &nbsp;ChatGPT / Codex&nbsp; · &nbsp;Cursor&nbsp; · &nbsp;Windsurf&nbsp; · &nbsp;VS Code</b></sub>

</div>

Each of these tools has its own page in **Connect AI**, and **Other tool** covers anything else that speaks MCP. The assistant can reach your live and staging projects. It cannot change server-wide settings, change a project's limits, suspend a project or touch the panel's own project. **MCP URL & tokens** lists your tokens and lets you revoke one, and **Activity Log** shows every request: [Connect AI](https://www.panelalpha.com/documentation/single-server-edition/the-panel/connect-ai).

## PanelAlpha Hub

PanelAlpha Hub is your PanelAlpha account at [hub.panelalpha.com](https://hub.panelalpha.com). Connecting the panel to it is free and optional. The panel keeps working on its own either way.

With the panel connected:

- You sign in to the panel with **Sign in with PanelAlpha**, and your Hub account can sign in with GitHub or Google
- One account covers all your servers
- You can install apps from the PanelAlpha GO! catalog
- The Hub shows the status of every site on this server

You connect in one of two places. During the first login, choose **Connect with Hub** on the **Sign in** step of the setup wizard instead of a local account. On a panel that is already set up, open **Settings** and select **Connect to PanelAlpha**. Either way you sign in on PanelAlpha and come straight back to the panel.

While connected, the panel reports to the Hub every five minutes: the name, type and status of each project, the panel's version and its address. **Signing in through PanelAlpha skips the panel's two-factor check.** The Hub sign-in counts as that check.

**Disconnect** in **Settings** removes the server from your account and turns off **Sign in with PanelAlpha**. If PanelAlpha is your only way in, set a password in **My Account** first: [Settings](https://www.panelalpha.com/documentation/single-server-edition/the-panel/settings#panelalpha-hub).

## How your sites are kept apart

Each site is its own project on the engine, with its own files, databases, domains and backups. Sites made from Git or from files run in their own containers, so one broken app does not take the others down.

The panel is a project too. Once its project is protected, neither the panel nor any token can delete, stop or redeploy it. Only `pae` on the server can. Removing the panel leaves every site running.

Your own sign-in can have two-factor authentication, and **Active Devices** lets you sign out a browser you no longer use: [Your account](https://www.panelalpha.com/documentation/single-server-edition/the-panel/your-account).

## When something does not work

Most of what the panel does runs in the background: deploys, backups, staging copies. **Tasks** in the user menu lists each one with its status and how long it took, and shows a dot while one runs. A failed task shows the first line of its error under its name. Select the row to read the full error: [Tasks](https://www.panelalpha.com/documentation/single-server-edition/the-panel/tasks).

For a Git or files site, **Show Logs** opens the deploy log, live or from earlier deploys. **Advanced > Logs** has the PHP and web server logs, and **Advanced > Containers** can start, stop or restart a single service. Each part of the documentation has a Troubleshooting page with the message you see, what it means and what to do: [Troubleshooting](https://www.panelalpha.com/documentation/single-server-edition/troubleshooting/panel-and-account).

## FAQ

<details>
<summary><b>Do I need PanelAlpha Engine?</b></summary>

Yes. The panel is a project on the engine, and every hosting operation goes through the engine API. It needs Engine 2.3.0 or later: [Requirements](https://www.panelalpha.com/documentation/single-server-edition/getting-started/requirements).
</details>

<details>
<summary><b>Can one panel manage several servers?</b></summary>

No. One panel manages the engine it runs on. Managing many engines from one panel is Multi Server, a separate product.
</details>

<details>
<summary><b>What happens to my sites if I remove the panel?</b></summary>

They keep running. Removing the panel deletes its own project and its data: accounts, settings, project labels and the activity log. Each site is a separate project on the engine: [Removing the panel](https://www.panelalpha.com/documentation/single-server-edition/getting-started/removing).
</details>

<details>
<summary><b>Does the panel back itself up?</b></summary>

No. The backups you set up in the panel cover your sites. Back the panel up on the server with `pae project:backup:create`: [Where the panel keeps its data](https://www.panelalpha.com/documentation/single-server-edition/getting-started/removing#backing-up-the-panel).
</details>

<details>
<summary><b>How do I update the panel?</b></summary>

Deploy the new version into the panel's project on the server. There is no update button. Your accounts, settings and sessions stay, and the panel updates its database when it starts: [Updating the panel](https://www.panelalpha.com/documentation/single-server-edition/getting-started/updating).
</details>

<details>
<summary><b>Can I move the panel to another address?</b></summary>

Yes. Point the new domain at the server, then save it as **Application URL** in **Settings**. The panel adds the domain, gets a certificate and moves there. The old address stops answering: [The panel address](https://www.panelalpha.com/documentation/single-server-edition/getting-started/panel-address).
</details>

<details>
<summary><b>Can I bring my WordPress site from another host?</b></summary>

Yes. Create a project, choose **WordPress** and then **Import Existing WordPress Project**. The panel connects with your WordPress admin login or through a plugin you install on the old site. Importing over FTP or SFTP is not available: [Importing a WordPress site](https://www.panelalpha.com/documentation/single-server-edition/projects/importing-wordpress).
</details>

<details>
<summary><b>What can the panel not do yet?</b></summary>

It cannot roll a Git project back to an earlier commit, because it deploys the latest commit of a branch. It has no setting to put a password in front of a whole site. Plugins and themes install by their wordpress.org name, not from a URL.
</details>

<details>
<summary><b>Is it free?</b></summary>

Single Server Community is free, open source under the Apache 2.0 licence and has no project limit. You pay for your server.
</details>

## Talk to us on Discord

[Discord](https://discord.gg/9twHWR7xGX) is the main place to reach the PanelAlpha team. Ask a question, tell us what does not work or show us what you host.

<br><div align="center">
<a href="https://discord.gg/9twHWR7xGX">
<img src=".github/assets/discord-banner.png" alt="Talk to us on Discord, the main place to reach the PanelAlpha team" width="760">
</a>
</div><br>

If you prefer a forum, use [community.panelalpha.com](https://community.panelalpha.com/).

## Security

Report a vulnerability privately, never in a public issue: [manage.panelalpha.com/contact](https://manage.panelalpha.com/contact).

## Licence

PanelAlpha Single Server Edition is open source under the [Apache License 2.0](LICENSE).
