# BoltMCP Installation

BoltMCP installs on any Kubernetes cluster with a single Helm chart.

## Install with Claude

1. Prerequisite: [install Claude Code](https://code.claude.com/docs/) and login

```bash
claude auth login
```

2. Clone this repository

```bash
git clone https://github.com/boltmcp/boltmcp.git
```

3. Move your BoltMCP access key to the `keys` directory

```bash
mv ~/Downloads/my-key.json boltmcp/keys/
```
> Replace `~/Downloads/my-key.json` with the path to your access key file

4. Open Claude Code from inside the `boltmcp` directory

```bash
cd boltmcp && claude
```

5. Invoke the Skill and Claude will walk you through the installation process

```
/install-boltmcp Install BoltMCP on a new cluster
```

> Replace the text after "/install-boltmcp " with any instruction related to installing, updating or uninstalling BoltMCP.

## Install Manually

If you'd prefer to do the installation manually, visit https://install.boltmcp.io and follow the instructions there.
