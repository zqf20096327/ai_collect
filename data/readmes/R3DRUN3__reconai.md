# reconai  

[![release](https://github.com/R3DRUN3/reconai/actions/workflows/release.yml/badge.svg)](https://github.com/R3DRUN3/reconai/actions/workflows/release.yml) 
![Red Team Badge](https://img.shields.io/badge/Team-Red-red)  ![Blue Team Badge](https://img.shields.io/badge/Team-Blue-blue)  


<img src="./media/logo.png" width="220" alt="reconai Logo">  



## Table of Contents

- [reconai](#reconai)
  - [Table of Contents](#table-of-contents)
  - [Abstract](#abstract)
  - [Why this is *not* an Agentic Offensive Framework](#why-this-is-not-an-agentic-offensive-framework)
  - [Use cases](#use-cases)
  - [Quick start](#quick-start)
  - [API](#api)
    - [API Examples](#api-examples)
  - [Report Example](#report-example)
  - [Configuration](#configuration)


## Abstract  

reconai is a small Kali container with an API and an LLM agent inside.   
You POST a target, the agent runs a handful of authorized tools against the target, and you get back a JSON result with a written report.  

> [!WARNING]  
> **Only scan assets you own or are explicitly authorised to test**.

## Why this is *not* an Agentic Offensive Framework  

AOFs give an LLM a shell, sub-agents, graphs, loops and a mission. reconai gives it a simple **menu**.  

| | AOFs | reconai |
|---|---|---|
| Shell access for the LLM | Yes | **No**. Only allow-listed tools run |
|Complex multi-agent loops and graphs| Yes | **No**. Single agent with limited calls |
| What the LLM controls | Any command | Validated parameters of tools you enabled |
| Exploitation / brute force | Part of the job | **Not possible**. Tools run with non-intrusive flags |
| Scope | "Please stay in scope" | **Enforced in code** on every call, including redirects |
| Goal | Get in | **Look and report** |
| Scan Duration | Hours or Days | **Minutes** |

reconai is much more limited, but also much safer and faster to run than Agentic Offensive Frameworks.  
> [!TIP]  
> **The main rationale behind it is to find low-hanging fruit quickly, at scale, and at minimal cost**.    

## Use cases

- 🔁 **Continuous perimeter checks**: cron or CI posts your domains every night and diffs the reports
- 🤖 **Programmatic lightweight scans**: one HTTP call instead of a pile of tool wrappers
- 🚦 **Triage and Compliance**: "what's actually exposed on this new subdomain?" in minutes
- 📦 **Batch**: submit up to 50 scans at once, they run concurrently
- 🛡️ **Safe automation**: leverage AI capabilities with bounded agency

## Quick start  

reconai works with any OpenAI-compatible API that supports tool calling (OpenAI, Azure Foundry, vLLM, Ollama, LiteLLM...).  
Run the tool via docker:  

```bash
cp .env.example .env     # set reconai_LLM_*, reconai_API_KEY, reconai_TOOLS

docker run -d \
  --name reconai \
  --restart unless-stopped \
  --env-file .env \
  -p 127.0.0.1:9889:9889 \
  --mount type=volume,source=reconai-data,target=/data \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --tmpfs /tmp \
  ghcr.io/r3drun3/reconai:v0.2.0

sleep 3
docker logs reconai 
curl http://localhost:9889/health 
```    

Now go to [API Examples](#api-examples).    


## API

| | | |
|---|---|---|
| `POST` | `/scans` | submit one scan |
| `POST` | `/scans/batch` | submit up to 50 |
| `GET` | `/scans`, `/scans/{id}`, `/scans/{id}/report` | list, result, Markdown report |
| `DELETE` | `/scans/{id}` | cancel |
| `GET` | `/tools`, `/health` | enabled tools, liveness |

### API Examples  

Export API Key and endpoint:  

```bash
export API=http://localhost:9889
export KEY=$(grep ^reconai_API_KEY .env | cut -d= -f2)
```  

Submit a scan:  

```bash
ID=$(curl -s -X POST $API/scans \
  -H "Authorization: Bearer $KEY" -H 'Content-Type: application/json' \
  -d '{
    "targets": ["exampletarget.com"],
    "tools": ["nuclei", "gobuster", "wpscan", "wafw00f", "whatweb", "httpx", "testssl", "curl", "arjun", "katana"],
    "objective": "Light perimeter check: open ports, web technology, exposed files or directories, obvious misconfigurations and vulnerabilities",
    "max_steps": 30,
    "metadata": {"note": "first PoC test"}
  }' | jq -r .scan_id)
echo "scan id: $ID"
```  


Poll the status. It goes queued, then running, then completed or failed:  
```bash
watch -n 5 "curl -s -H 'Authorization: Bearer $KEY' $API/scans/$ID | jq '{status,steps,tools_used,error,runs:[.tool_runs[]|{tool,status,exit_code,duration_s}]}'"
```  

Read the result:  
```bash
# What is actually running (exact commands, status, output)
curl -s -H "Authorization: Bearer $KEY" $API/scans/$ID | jq '.tool_runs[] | {id,tool,status,exit_code,argv,output}'

# Summary and findings
curl -s -H "Authorization: Bearer $KEY" $API/scans/$ID | jq '{status,risk_rating,summary,findings,usage,error}'

# Report as Markdown
curl -s -H "Authorization: Bearer $KEY" $API/scans/$ID/report

# Full JSON saved to a file
curl -s -H "Authorization: Bearer $KEY" $API/scans/$ID > scan-$ID.json
```  

## Report Example  
```txt
# WAPT Assessment — exampletarget.io

## Scope
- Target: `https://exampletarget.io`
- Only the original host was tested. No exploitation or DoS was performed.

## Methodology
1. `httpx` — initial HTTP probe (status, server, technology).
2. `wafw00f` — WAF detection.
3. `whatweb` (aggression 3) — technology fingerprinting.
4. `curl` — manual inspection of responses, headers, and common sensitive paths (`/web.config`, `/elmah.axd`, `/trace.axd`, `/robots.txt`, `/User/Login`).
5. `testssl` — TLS protocols, certificate, headers, ciphers, and vulnerabilities.
6. `nuclei` — exposure, misconfiguration, technology, IIS/ASP.NET, header, and SSL templates.
7. `gobuster` — attempted directory enumeration (failed: TLS verification error on HTTPS; timeout on HTTP).

## Key observations
- The host runs **Microsoft IIS 8.5 / ASP.NET MVC**, with .NET Framework 4.0.30319 and ASP.NET 4.8.4797.0.
- **Every request returns HTTP 500** with a verbose ASP.NET error page. The exception occurs in a global request handler, so the application is unavailable and no application content is reachable.
- **No WAF was detected** by wafw00f’s generic detection.
- TLS: only TLS 1.2/1.3 offered, but the **certificate chain is incomplete** and standard clients fail verification.
- HTTP (port 80) does not respond (connection timeout); only HTTPS is served.

## Findings

### 1. No Web Application Firewall detected — Medium
wafw00f found no WAF in front of the host. The application appears directly exposed to internet traffic without a detected WAF.

[+] Generic Detection results:
[-] No WAF detected by the generic detection

### 2. ASP.NET verbose error messages enabled (customErrors mode=Off) — Medium
Full stack traces are returned to remote clients, disclosing the internal app name, developer username, local source path and line number.

*SupplyNetWebApp.MvcApplication.Application_PreRequestHandlerExecute(Object sender, EventArgs args) in C:\Users\john.doe\source\repos\DemoApp\DemoWebApp\Global.asax.cs:71*
This error page might contain sensitive information because ASP.NET is configured to show verbose error messages using <customErrors mode="Off"/>.


### 3. Application globally unavailable (HTTP 500 on every request) — Medium
`/`, `/User/Login`, `/User/Login?ReturnUrl=%2f` and `/trace.axd` all return the same 500 / `System.ArgumentNullException`. This is an availability problem and blocked deeper application testing.

### 4. TLS certificate chain incomplete — Low

Chain of trust               NOT ok (chain incomplete)
Certificates provided        1
curl: (60) SSL certificate OpenSSL verify result: unable to get local issuer certificate (20)


### 5. Missing HTTP security headers — Low
No HSTS, CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy or cross-origin policies.

### 6. Server/technology version disclosure — Info
`Server: Microsoft-IIS/8.5`, `X-AspNet-Version: 4.0.30319`, `X-Powered-By: ASP.NET` (IIS 8.5 is EOL).

### 7. Obsolete CBC ciphers / LUCKY13 potentially vulnerable — Info

Obsoleted CBC ciphers (AES, ARIA etc.)         offered
LUCKY13 (CVE-2013-0169), experimental     potentially VULNERABLE


## Remediation summary
- Deploy a WAF in blocking mode.
- Set `customErrors mode="RemoteOnly"` and stop returning stack traces.
- Fix the null-reference bug in `Global.asax.cs:71` and add robust exception handling.
- Install the full TLS certificate chain; disable CBC ciphers and prefer AEAD suites.
- Add HSTS and the other missing security headers; suppress version-revealing headers; plan an upgrade off EOL IIS 8.5.

## Limitations
- The application is globally broken (500 on all requests), so no authenticated or functional application testing was possible.
- `gobuster` could not run: HTTPS failed TLS verification and HTTP timed out. Directory/file enumeration was therefore not completed; only a small set of manually chosen paths was checked.
- No WPScan (not WordPress). Nuclei ran only non-intrusive community templates.
- The certificate was inspected with TLS verification bypassed for HTTP response inspection only; the certificate remains untrusted.%     
```


## Configuration

| Variable | Default | |
|---|---|---|
| `reconai_LLM_BASE_URL`, `_API_KEY`, `_MODEL` | OpenAI | your LLM |
| `reconai_API_KEY` | required | bearer key for this API |
| `reconai_TOOLS` | `nuclei,gobuster,wpscan,nmap` | what the agent may use |
| `reconai_SCOPE_ALLOWLIST` | empty | only accept targets inside these domains/CIDRs |
| `reconai_MAX_CONCURRENT_SCANS` | 3 | parallel scans |
| `reconai_MAX_STEPS` | 30 | LLM calls per scan |
| `reconai_TOOL_TIMEOUT` | 600 | seconds per tool run |













