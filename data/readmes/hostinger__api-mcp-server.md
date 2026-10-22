# hostinger-api-mcp

Model Context Protocol (MCP) server for Hostinger API.

## Quick start: Hosted remote server

If you don't want to install or run anything locally, connect directly to Hostinger's hosted MCP server:

```
https://mcp.hostinger.com
```

### Claude Code

```bash
claude mcp add --transport http hostinger https://mcp.hostinger.com
```

This opens a browser window to authorize via OAuth. Once approved, the operations below are reachable through `execute` in your session.

### Other MCP-compatible clients

Add `https://mcp.hostinger.com` as a remote Streamable HTTP MCP server in your client's configuration and complete the OAuth prompt when it appears. Refer to your client's docs for how it exposes "add remote MCP server" / "custom connector" settings.

## Prerequisites
- Node.js version 24 or higher

If you don't have Node.js installed, you can download it from the [official website](https://nodejs.org/en/download/).
Alternatively, you can use a package manager like [Homebrew](https://brew.sh/) (for macOS) or [Chocolatey](https://chocolatey.org/) (for Windows) to install Node.js.

We recommend using [NVM (Node Version Manager)](https://github.com/nvm-sh/nvm) to install and manage installed Node.js versions.
After installing NVM, you can install Node.js with the following command:
```bash
nvm install v24
nvm use v24
```

## Installation

To install the MCP server, run one of the following command, depending on your package manager:

```bash
# Install globally from npm
npm install -g @hostinger/mcp

# Or with yarn
yarn global add @hostinger/mcp

# Or with pnpm
pnpm add -g @hostinger/mcp
```

## Update

To update the MCP server to the latest version, use one of the following commands, depending on your package manager:

```bash
# Update globally from npm
npm update -g @hostinger/mcp

# Or with yarn
yarn global upgrade @hostinger/mcp

# Or with pnpm
pnpm update -g @hostinger/mcp
```

## Binaries

This package installs the following MCP server commands:

- `hostinger-api-mcp` — unified server over every operation (410 total)
- `hostinger-agency-hosting-mcp` — 42 operations for agency-hosting
- `hostinger-agent-readiness-mcp` — 3 operations for agent-readiness
- `hostinger-billing-mcp` — 9 operations for billing
- `hostinger-dns-mcp` — 8 operations for dns
- `hostinger-domains-mcp` — 42 operations for domains
- `hostinger-ecommerce-mcp` — 29 operations for ecommerce
- `hostinger-horizons-mcp` — 6 operations for horizons
- `hostinger-hosting-mcp` — 67 operations for hosting
- `hostinger-mail-mcp` — 38 operations for mail
- `hostinger-reach-mcp` — 62 operations for reach
- `hostinger-vps-mcp` — 67 operations for vps
- `hostinger-wordpress-mcp` — 40 operations for wordpress

Every binary exposes the same three tools; a scoped binary only searches and executes its own group's operations. `hostinger-api-mcp` remains the backwards-compatible default.

## Configuration

The following environment variables can be configured when running the server:
- `DEBUG`: Enable debug logging (true/false) (default: false)
- `HOSTINGER_API_TOKEN`: Your API token, which will be sent in the `Authorization` header. When set, OAuth is bypassed entirely.
- `API_TOKEN`: Deprecated alias for `HOSTINGER_API_TOKEN`. Will be removed in a future version — prefer `HOSTINGER_API_TOKEN`.
- `OAUTH_ISSUER`: OAuth server base URL (default: `https://auth.hostinger.com`). Only used when `HOSTINGER_API_TOKEN` is not set.

## Authentication

The server supports two authentication methods:

### API Token (recommended for CI/scripts)

Set `HOSTINGER_API_TOKEN` in the environment or `.env` file. When present it always takes precedence — no OAuth code runs.

### OAuth 2.0 with PKCE (interactive sign-in)

When `HOSTINGER_API_TOKEN` is not set and the server runs in stdio mode, OAuth 2.0 with PKCE is used automatically on the first authenticated tool call:

1. A dynamic OAuth client is registered with the issuer (RFC 7591) — once per machine.
2. A browser window opens to the authorization page.
3. After sign-in, the server captures the redirect on a local ephemeral port, exchanges the code for tokens, and stores them.
4. Subsequent calls reuse the stored access token; expired tokens are refreshed automatically. If a refresh token is revoked, the browser flow is re-launched.

Credentials are stored at:
- macOS / Linux: `~/.config/hostinger-mcp/credentials.json` (mode 0600)
- Windows: `%APPDATA%\hostinger-mcp\credentials.json`

Credentials are shared across all Hostinger MCP binaries (`hostinger-api-mcp`, `hostinger-vps-mcp`, etc.).

**Manual commands:**

```bash
# Run the OAuth sign-in flow immediately (don't wait for the first tool call)
hostinger-api-mcp --login

# Revoke stored credentials
hostinger-api-mcp --logout
```

**HTTP transport note:** OAuth sign-in is not supported in `--http` mode. Set `HOSTINGER_API_TOKEN` before using `--http`.

## Usage

### JSON configuration for Claude, Cursor, etc.

```json
{
    "mcpServers": {
        "hostinger-api": {
            "command": "hostinger-api-mcp",
            "env": {
                "DEBUG": "false",
                "HOSTINGER_API_TOKEN": "YOUR API TOKEN"
            }
        }
    }
}
```

### Transport Options

The MCP server supports two transport modes:

#### Standard I/O Transport

The server can use standard input / output (stdio) transport (default). This provides local streaming:

#### Streamable HTTP Transport

The server can use HTTP streaming transport. This provides bidirectional streaming over HTTP:

```bash
# Default HTTP transport on localhost:8100
hostinger-api-mcp --http

# Specify custom host and port
hostinger-api-mcp --http --host 0.0.0.0 --port 8150
```

#### Command Line Options

```
Options:
  --http           Use HTTP streaming transport (requires HOSTINGER_API_TOKEN env var)
  --stdio          Use Server-Sent Events transport (default)
  --host {host}    Hostname or IP address to listen on (default: 127.0.0.1)
  --port {port}    Port to bind to (default: 8100)
  --login          Run OAuth sign-in flow and exit
  --logout         Revoke stored OAuth credentials and exit
  --help           Show help message
```

### Using as an MCP Tool Provider

This server implements the Model Context Protocol (MCP) and can be used with any MCP-compatible consumer.

Example of connecting to this server using HTTP streaming transport:

```javascript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

// Create HTTP transport
const transport = new StreamableHTTPClientTransport({
  url: "http://localhost:8100/",
  headers: {
    "Authorization": `Bearer ${process.env.HOSTINGER_API_TOKEN}`
  }
});

// Connect to the MCP server
const client = new Client({
  name: "my-client",
  version: "1.0.0"
}, {
  capabilities: {}
});

await client.connect(transport);

// List available tools
const { tools } = await client.listTools();
console.log("Available tools:", tools);

// Execute an operation
const result = await client.callTool({
  name: "execute",
  arguments: { operation: "billing_catalog_list", params: { category: "DOMAIN" } }
});
console.log("Tool result:", result);
```

## Tools

Every server exposes three tools:

- `search` — find operations by keyword; returns each match with its `inputSchema`.
- `execute` — run one operation: `{ "operation": "<name>", "params": { ... } }`.
- `multi-execute` — run up to 20 operations in order, stopping at the first failure. A params value that is exactly `"$steps.<i>.<path>"` is replaced by that value from an earlier step's result.

## Operations

The operations `search` offers, by binary:

Operations that newer tools replace are hidden from `search`, and not documented, in every binary that also offers the replacing tool. They keep working through `execute` until they are removed.

### `hostinger-agency-hosting-mcp`

#### agency-hosting_deploy-node-static-website

Deploy a node-static Agency Plan (h5g) website from an archive file. WARNING: this overwrites the website's existing contents and cannot be undone — always confirm with the user before proceeding. Use this for Agency Plan websites of type node-static (a Node.js-built static site that requires a build step or a plain simple static site). The tool resolves the website from its domain, uploads the archive to the website's file browser over TUS, and triggers the build-assets process which builds the site and deploys the result to public_html. This operation is synchronous: the build and deployment complete before the tool returns, so the website is live as soon as the tool finishes successfully — there is no separate asynchronous build to wait for or poll. Upload credentials are generated and used internally — do not call a separate upload-url endpoint or upload the archive yourself, this tool does it end-to-end. For plain PHP applications that should be extracted as-is, use agency-hosting_deploy-php-application instead. The website UID is automatically resolved from the domain.

- **Method**: `custom`
- **Path**: `custom`

#### agency-hosting_deploy-php-application

Deploy a PHP (or other non-build) Agency Plan (h5g) website from an archive file. WARNING: this overwrites the website's existing contents and cannot be undone — always confirm with the user before proceeding. Use this for Agency Plan websites where the archive contents should be extracted and served as-is with no build step (e.g., PHP applications). The tool resolves the website from its domain, uploads the archive to the website's file browser over TUS, and triggers the import-archive process which overwrites the website contents with the archive contents. This operation is synchronous: the archive is extracted and deployed before the tool returns, so the website is live as soon as the tool finishes successfully — there is no separate asynchronous build to wait for or poll. Upload credentials are generated and used internally — do not call a separate upload-url endpoint or upload the archive yourself, this tool does it end-to-end. For node-static websites that require a build step, use agency-hosting_deploy-node-static-website instead. The website UID is automatically resolved from the domain.

- **Method**: `custom`
- **Path**: `custom`

#### agency-hosting_datacenters_list

Lists the datacenters available for provisioning a new website on the given Agency Plan
hosting order.

Each datacenter includes a `pinger_url` you can ping from the client to measure round-trip
latency; comparing the results across datacenters lets you pick the nearest one (lowest
ping) before choosing its `code` as the `datacenter_code` when creating a website setup.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/datacenters`

#### agency-hosting_domains_change-website

Changes the primary domain for an Agency Plan website.

Provide the current domain in the path and the new domain in the request body.
Set domain to null to revert to the temporary domain.

- **Method**: `PUT`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{from_domain}`

#### agency-hosting_domains_link-to-website

Links a domain to the specified Agency Plan website so it can serve traffic for that domain.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains`

#### agency-hosting_domains_list

Returns a paginated list of domains associated with Agency Plan websites accessible to the authenticated client.

Use the website_uuids filter to narrow results to specific websites.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/domains`

#### agency-hosting_domains_unlink-from-website

Unlinks a domain from the specified Agency Plan website.

The website stops serving traffic on this domain immediately.

Website files and database are preserved, and any other linked domains remain accessible.

If this is the only domain on the website, unlinking leaves the website without an accessible domain.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{domain}`

#### agency-hosting_files_generate-upload-url

Generate a file browser upload URL with authentication credentials for uploading files
to an Agency Plan website's file storage.

Returns `url`, `auth_key` and `rest_auth_key`. Use these to upload a file to the
website's file storage via the TUS resumable upload protocol (TUS 1.0.0). Send
`X-Auth: {auth_key}` and `X-Auth-Rest: {rest_auth_key}` headers on every request below.

1. Create the upload: `POST` to `{url}/{relative_file_path}?override=true` with headers
   `upload-length: {file size in bytes}` and `upload-offset: 0`. Expect `201 Created`.
2. Upload the file: send the file bytes to the same location (any TUS 1.0.0 client, or
   `PATCH` requests with an `upload-offset` header tracking progress) until complete.

`relative_file_path` is the destination path inside the website's file storage, e.g.
`app.zip`.

Instead of a TUS client, plain `curl` also works:
```
FILE=app.zip
SIZE=$(stat -f%z "$FILE")   # stat -c%s on Linux

curl -i -X POST "{url}/${FILE}?override=true" \
  -H "X-Auth: {auth_key}" \
  -H "X-Auth-Rest: {rest_auth_key}" \
  -H "Tus-Resumable: 1.0.0" \
  -H "Upload-Length: ${SIZE}" \
  -H "Upload-Offset: 0"
# -> 201 Created

curl -i -X PATCH "{url}/${FILE}?override=true" \
  -H "X-Auth: {auth_key}" \
  -H "X-Auth-Rest: {rest_auth_key}" \
  -H "Tus-Resumable: 1.0.0" \
  -H "Content-Type: application/offset+octet-stream" \
  -H "Upload-Offset: 0" \
  --data-binary "@${FILE}"
# -> 204 No Content, Upload-Offset response header equals SIZE when done
```

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/files/upload-urls`

#### agency-hosting_files_import-website-from-archive

Imports an Agency Plan website from an already-uploaded archive.

Upload the archive to the website's root directory via file browser first, then provide its
filename in this request. Website contents are overwritten by the archive contents. Supported
archive types: .zip, .tar, .tar.gz, .tgz.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/files/import-archive`

#### agency-hosting_metrics_list-plan-order-disk-usage

Returns aggregated disk and inode usage for the Agency Plan order over the
selected time frame, plus the plan quotas. Figures cover the whole order
account. Values may be up to one hour stale. CPU, memory, and process usage
are on the resource-usage-metrics endpoint.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/disk-usage-metrics`

#### agency-hosting_orders_list

Returns a paginated list of Agency Plan orders accessible to the authenticated client.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders`

#### agency-hosting_metrics_list-order-resource-usage

Returns aggregated CPU, memory, and process usage for the Agency Plan order
over the selected time frame, plus the plan quotas and a per-website
breakdown. Each website is identified by uid. Suspended and deleted websites
are excluded from both the order totals and the per-website breakdown.
Values may be up to one hour stale. Disk and inode usage are on the
disk-usage-metrics endpoint.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/resource-usage-metrics`

#### agency-hosting_php_list-extensions-for-website

Lists every PHP extension available to an Agency Plan website and whether it is currently enabled.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/extensions`

#### agency-hosting_php_replace-website-extensions

Replaces the set of PHP extensions enabled on an Agency Plan website with the ones provided. Any toggleable extension not in the request is disabled, so call the extensions endpoint first and send the full desired set. Extensions compiled into PHP, reported with the "built-in" state, are always active and are unaffected.

- **Method**: `PUT`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/extensions`

#### agency-hosting_php_list-options-for-website

Lists the php.ini directives that can be configured for an Agency Plan website, each with its default, the value currently in effect, and the values it accepts.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/options`

#### agency-hosting_php_replace-website-options

Replaces the custom php.ini values on an Agency Plan website with the ones provided. Any option not in the request is reset to its default, so call the options endpoint first and send the full desired set. Sending an empty array resets every option to its default.

- **Method**: `PUT`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/options`

#### agency-hosting_php_list-versions-for-order

Lists the PHP versions available to websites created under an Agency Plan order, determined by the server the order is hosted on. Use this before creating a website; for a website that already exists, call the website-scoped versions endpoint instead.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/websites/php-settings/versions`

#### agency-hosting_php_list-versions-for-website

Lists the PHP versions an Agency Plan website can be switched to. The version the website is currently running is returned as settings.php.version by the website details endpoint.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/versions`

#### agency-hosting_php_update-website-version

Switches an Agency Plan website to a different PHP version. Call the available versions endpoint first to see which versions can be selected. The website restarts on the new version, so requests served during the switch may fail and code that is incompatible with the target version will break.

- **Method**: `PATCH`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/php-settings/version`

#### agency-hosting_website-setups_create

Provisions a new website on one of your Agency Plan hosting orders.

Choose the datacenter, stack (`flavor`), and PHP version for the site. Optionally attach
your own `domain` — omit it, set it to `null`, or leave it unavailable and a free
`*.hostingersite.com` subdomain is generated instead — and/or install WordPress by
supplying the `wordpress` details (admin account, site title, and language).

Common setups:
- **Plain PHP site**: `flavor` set to `php-fpm`, with `settings.php.version`; omit
  `wordpress` and `type`.
- **WordPress site**: `flavor` set to the desired WordPress version (e.g. `wp-7.0`), plus
  the `wordpress` block (admin account, title, language).
- **Static/Node.js frontend app**: `flavor` set to `php-fpm` and `type` set to
  `node-static`.

Provisioning runs in the background, so the response returns immediately with a setup UUID
that identifies the job. The new website becomes reachable once provisioning finishes.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/websites/setups`

#### agency-hosting_website-setups_status

Returns the current status of an Agency Plan website setup started via the setups
endpoint.

Poll this endpoint using the `setup_uuid` returned from the provisioning request until
`status` becomes `completed`, at which point `website_uid` identifies the new website.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/orders/{order_id}/websites/setups/{setup_uuid}`

#### agency-hosting_ssl_reinstall-website

Replaces the Let's Encrypt certificate of the domain: the current platform certificate, when
one is recorded, is revoked and removed, then a new setup starts in the background. Returns at
once; `Get website SSL status` reports `installing` while it runs, then `active` or `failed`.

Returns 422 for free subdomains, when a certificate process is recorded for the domain (a
failed setup counts until it is cleaned up), or when the domain hit its limit of three setups
per seven days. Returns 429 when the same domain was requested less than a minute ago, and 403
when the website is suspended or locked, and 404 when the website or the domain does not exist.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/reinstall`

#### agency-hosting_ssl_install-website

Starts a Let's Encrypt certificate setup for the domain and returns at once; the setup runs in
the background. `Get website SSL status` reports `installing` while it runs, then `active` or
`failed`; the `ssl_setup` entry of `List website processes` shows the same progress.

Returns 422 when the domain already has a platform certificate that is not expired, when a
certificate process is recorded for the domain (a failed setup counts until it is cleaned up),
or when the domain hit its limit of three setups per seven days. Returns 429 when the same
domain was requested less than a minute ago, 403 when the website is suspended or locked, and
404 when the website or the domain does not exist.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/setup`

#### agency-hosting_ssl_website-status

Returns the SSL state of one domain of an Agency Plan website: the certificate `status`,
whether the certificate was uploaded by the customer, and when it stops being valid.

`installing` means a certificate setup is running or retrying; the `ssl_setup` entry of
`List website processes` shows the same progress. `active` means a valid certificate is in
place: uploaded by the customer, issued by the platform, or a lifetime certificate bought for
the domain. `failed` means the last setup gave up and no valid certificate is in place.
`expired` means the certificate has run out. `not_installed` means the domain has no
certificate and no setup process. Returns 404 when the website or the domain does not exist.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/status`

#### agency-hosting_ssl_uninstall-website

Removes the platform-issued Let's Encrypt certificate of the domain: the certificate is revoked
and deleted before the response, so the domain is no longer served with a platform certificate
until a new setup completes. Also succeeds when the domain has no platform certificate to
remove. Uploaded (custom) certificates are not affected.

Returns 422 when a certificate process is recorded for the domain (a failed setup counts until
it is cleaned up), 429 when the same domain was requested less than a minute ago, and 403 when
the website is suspended or locked, and 404 when the website or the domain does not exist.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl`

#### agency-hosting_websites_build-nodejs-assets

Builds and deploys a Node.js application for an Agency Plan website from an already-uploaded archive.

Upload the archive to file browser first, then provide its relative path from document root in this request.
Website contents are overwritten by the build result, which is deployed to public_html.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/build-assets`

#### agency-hosting_cache_clear-website

Clears cache for all domains associated with an Agency Plan website, including its preview domain.

This operation clears all cache types for the website.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/cache`

#### agency-hosting_cron-jobs_list-website

Returns a paginated list of cron jobs configured for an Agency Plan website.

Each entry includes the schedule expression and the command executed on that schedule.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/cron-jobs`

#### agency-hosting_cron-jobs_create-website

Creates a cron job for an Agency Plan website from a schedule expression and a command.

Returns the created cron job, including its uuid, which is required to delete the cron job.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/cron-jobs`

#### agency-hosting_cron-jobs_delete-website

Permanently deletes the cron job identified by its uuid from an Agency Plan website.

The operation is idempotent: deleting a cron job that does not exist succeeds without error.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/cron-jobs/{uuid}`

#### agency-hosting_databases_list-website

Returns a paginated list of MySQL databases created for an Agency Plan website.

Each entry includes the database's non-system users.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/databases`

#### agency-hosting_databases_create-website

Creates a MySQL database with a dedicated user for an Agency Plan website.

The database name, username, and password must all be provided by the caller.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/databases`

#### agency-hosting_databases_delete-website

Permanently deletes a MySQL database and all its data from an Agency Plan website, including its users.

The operation is idempotent: deleting a database that does not exist succeeds without error.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/databases/{database_name}`

#### agency-hosting_databases_create-website-user

Creates a user for an existing database on an Agency Plan website.

Each database supports a single non-system user; creating a user for a database that already has one fails.

- **Method**: `POST`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/databases/{database_name}/users`

#### agency-hosting_databases_delete-website-user

Permanently deletes a database user from an Agency Plan website database, revoking all access it had.

The operation is idempotent: deleting a user that does not exist succeeds without error.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/databases/{database_name}/users/{database_user_name}`

#### agency-hosting_websites_get

Retrieves detailed information about a specific Agency Plan website, including configuration,
status, metadata, hosting plan details, and resource quotas.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}`

#### agency-hosting_websites_delete

Permanently deletes an Agency Plan website. Deletion is processed asynchronously: the
website is immediately transitioned to a deleting state and the underlying server
resources are removed in the background.

- **Method**: `DELETE`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}`

#### agency-hosting_websites_list-plan

Retrieve a paginated list of Agency Plan websites (H5G, Builder, and Horizons) accessible to
the authenticated client.

This endpoint returns websites from your hosting accounts as well as
websites from other client hosting accounts that have shared access
with you.

The response shape differs per platform — see the `platform` field on each item.

Use `website_types` to list only websites of a given detected type, e.g. only
WordPress websites (`website_types=wordpress`) or only Node.js websites
(`website_types=nodejs`). Combine with `order_ids`, `states`, or `domain` for more
targeted results.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites`

#### agency-hosting_websites_list-processes

Lists active and recently completed asynchronous processes for an Agency Plan website.

Each process has a unique ID (for tracking), a type, and a status (running, completed, failed).
Poll this endpoint after initiating async operations (SSL setup, backups, cloning) to track progress.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/processes`

#### agency-hosting_wordpress_change-version

Changes the installed WordPress core version on an Agency Plan website to one of the versions available for installation.

- **Method**: `PATCH`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/wordpress/settings/version`

#### agency-hosting_wordpress_settings

Returns the current WordPress settings for an Agency Plan website: installed core version,
LiteSpeed Cache plugin status, object cache status, and maintenance mode status.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/wordpress/settings`

#### agency-hosting_wordpress_list-versions

Lists the WordPress core versions available for installation on an Agency Plan website.

- **Method**: `GET`
- **Path**: `/api/agency-hosting/v1/websites/{website_uid}/wordpress/settings/versions`

### `hostinger-agent-readiness-mcp`

#### agent-readiness_checks_list

List every check an agent readiness scan runs, with its name, category and weight.\n
Use it to show the human-readable name of each `check_id` in a scan's results.

- **Method**: `GET`
- **Path**: `/api/agent-readiness/v1/checks`

#### agent-readiness_scans_run

Start a scan of how ready a public website is for AI agents to discover, read and act on.\n
Scanning is asynchronous: this operation only starts the scan, and the returned scan is usually `pending`
with no results yet. To get the results, poll the `Get agent readiness scan` operation with the same
domain every few seconds until its status is `completed` or `failed`. The scan itself is limited to 60 seconds,
plus any time it waits in the queue. A `failed` scan is not retried; run this operation again.\n
Starting a scan for a domain that already has a pending scan from the last 5 minutes
returns that scan instead of starting a new one.

- **Method**: `POST`
- **Path**: `/api/agent-readiness/v1/scans`

#### agent-readiness_scans_get

Get the latest agent readiness scan of a website.\n
Scans started with the `Run agent readiness scan` operation are asynchronous. While the status is
`pending`, the result fields are null; wait a few seconds and call this operation again until the status is
`completed` or `failed`. A `failed` scan is not retried; run the scan again.\n
A completed scan has a 0-100 score, a letter grade, a score per category, and the result of every
check with the evidence found and how to fix it. Check names are listed by the `List checks` operation.\n
Returns 404 when the domain has never been scanned; use the `Run agent readiness scan` operation first.

- **Method**: `GET`
- **Path**: `/api/agent-readiness/v1/scans/{domain}`

### `hostinger-billing-mcp`

#### billing_catalog_list

Retrieve catalog items available for order.

Prices in catalog items is displayed as cents (without floating point),
e.g: float `17.99` is displayed as integer `1799`.

Use this endpoint to view available services and pricing before placing orders.

- **Method**: `GET`
- **Path**: `/api/billing/v1/catalog`

#### billing_orders_create-purchase

Create a purchase order for any Hostinger product.

This unified endpoint places an order for one or more catalog items and
works across all Hostinger products, leveraging the existing billing
infrastructure. Use the [catalog endpoint](#tag/billing-catalog) to look
up the `item_id` values available for purchase.

If no payment method is provided, your default payment method will be used automatically.

If the response is `202 Accepted`, the payment is still being processed and the order will
complete asynchronously once the payment is confirmed.

This endpoint only places the order. Product-specific provisioning
(e.g. VPS setup or domain registration) is not performed here — once the
order completes, use the relevant product endpoints or
[hPanel](https://hpanel.hostinger.com/) to finalize setup.

Use this endpoint to purchase any product available in the catalog.

- **Method**: `POST`
- **Path**: `/api/billing/v1/orders`

#### billing_payment-methods_set-default

Set the default payment method for your account.

Use this endpoint to configure the primary payment method for future orders.

- **Method**: `POST`
- **Path**: `/api/billing/v1/payment-methods/{paymentMethodId}`

#### billing_payment-methods_delete

Delete a payment method from your account.

Use this endpoint to remove unused payment methods from user accounts.

- **Method**: `DELETE`
- **Path**: `/api/billing/v1/payment-methods/{paymentMethodId}`

#### billing_payment-methods_list

Retrieve available payment methods that can be used for placing new orders.

If you want to add new payment method,
please use [hPanel](https://hpanel.hostinger.com/billing/payment-methods).

Use this endpoint to view available payment options before creating orders.

- **Method**: `GET`
- **Path**: `/api/billing/v1/payment-methods`

#### billing_subscriptions_list

Retrieve a list of all subscriptions associated with your account.

Use this endpoint to monitor active services and billing status.

- **Method**: `GET`
- **Path**: `/api/billing/v1/subscriptions`

#### billing_subscriptions_disable-auto-renewal

Disable auto-renewal for a subscription.

Use this endpoint when disable auto-renewal for a subscription.

- **Method**: `DELETE`
- **Path**: `/api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/disable`

#### billing_subscriptions_enable-auto-renewal

Enable auto-renewal for a subscription.

Use this endpoint when enable auto-renewal for a subscription.

- **Method**: `PATCH`
- **Path**: `/api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/enable`

#### billing_subscriptions_renew

Create a renewal order for an existing Hostinger subscription.

This endpoint places a renewal order for a single subscription, leveraging
the existing billing infrastructure. Use the
[subscriptions endpoint](#tag/billing-subscriptions) to look up the
`subscriptionId` values available for renewal.

If no payment method is provided, your default payment method will be used automatically.

If the response is `202 Accepted`, the payment is still being processed and the renewal will
complete asynchronously once the payment is confirmed.

Use this endpoint to renew any subscription available in your account.

- **Method**: `POST`
- **Path**: `/api/billing/v1/subscriptions/{subscriptionId}/renew`

### `hostinger-dns-mcp`

#### dns_snapshots_get

Retrieve particular DNS snapshot with contents of DNS zone records.

Use this endpoint to view historical DNS configurations for domains.

- **Method**: `GET`
- **Path**: `/api/dns/v1/snapshots/{domain}/{snapshotId}`

#### dns_snapshots_list

Retrieve DNS snapshots for a domain.

Use this endpoint to view available DNS backup points for restoration.

- **Method**: `GET`
- **Path**: `/api/dns/v1/snapshots/{domain}`

#### dns_snapshots_restore

Restore DNS zone to the selected snapshot.

Use this endpoint to revert domain DNS to a previous configuration.

- **Method**: `POST`
- **Path**: `/api/dns/v1/snapshots/{domain}/{snapshotId}/restore`

#### dns_records_list

Retrieve DNS zone records for a specific domain.

Use this endpoint to view current DNS configuration for domain management.

- **Method**: `GET`
- **Path**: `/api/dns/v1/zones/{domain}`

#### dns_records_update

Update DNS records for the selected domain.

Using `overwrite = true` will replace existing records with the provided ones. 
Otherwise existing records will be updated and new records will be added.

Use this endpoint to modify domain DNS configuration.

- **Method**: `PUT`
- **Path**: `/api/dns/v1/zones/{domain}`

#### dns_records_delete

Delete DNS records for the selected domain.

To filter which records to delete, add the `name` of the record and `type` to the filter. 
Multiple filters can be provided with single request.

If you have multiple records with the same name and type, and you want to delete only part of them,
refer to the `Update zone records` endpoint.

Use this endpoint to remove specific DNS records from domains.

- **Method**: `DELETE`
- **Path**: `/api/dns/v1/zones/{domain}`

#### dns_records_reset

Reset DNS zone to the default records.

Use this endpoint to restore domain DNS to original configuration.

- **Method**: `POST`
- **Path**: `/api/dns/v1/zones/{domain}/reset`

#### dns_records_validate

Validate DNS records prior to update for the selected domain.

If the validation is successful, the response will contain `200 Success` code.
If there is validation error, the response will fail with `422 Validation error` code.

Use this endpoint to verify DNS record validity before applying changes.

- **Method**: `POST`
- **Path**: `/api/dns/v1/zones/{domain}/validate`

### `hostinger-domains-mcp`

#### domains_verifications_direct

Retrieve a list of pending and completed domain verifications.

- **Method**: `GET`
- **Path**: `/api/v2/direct/verifications/active`

#### domains_availability_suggest-names-from-description

Suggest available domain names based on a free-text description of your project.

Suggestions are generated by an AI model, so they differ between calls.

Endpoint has rate limit of 90 requests per minute.

Use this endpoint to find a domain name when you only know what the website is about.

- **Method**: `POST`
- **Path**: `/api/domains/v1/availability/alternatives-from-description`

#### domains_availability_suggest-names-from

Suggest available domain names based on a domain name you already have in mind.

Suggestions are generated by an AI model, so they differ between calls.

Endpoint has rate limit of 90 requests per minute.

Use this endpoint when the domain you wanted is taken and you need close alternatives.

- **Method**: `POST`
- **Path**: `/api/domains/v1/availability/alternatives-from-domain`

#### domains_availability_check

Check availability of domain names across multiple TLDs.

Multiple TLDs can be checked at once.
If you want alternative domains with response, provide only one TLD and set `with_alternatives` to `true`.
TLDs should be provided without leading dot (e.g. `com`, `net`, `org`).

Endpoint has rate limit of 90 requests per minute.

Use this endpoint to verify domain availability before purchase.

- **Method**: `POST`
- **Path**: `/api/domains/v1/availability`

#### domains_forwarding_get

Retrieve domain forwarding data.

Use this endpoint to view current redirect configuration for domains.

- **Method**: `GET`
- **Path**: `/api/domains/v1/forwarding/{domain}`

#### domains_forwarding_update

Update domain forwarding configuration.

Use this endpoint to modify existing redirect configuration for domains.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/forwarding/{domain}`

#### domains_forwarding_delete

Delete domain forwarding data.

Use this endpoint to remove redirect configuration from domains.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/forwarding/{domain}`

#### domains_forwarding_create

Create domain forwarding configuration.

Use this endpoint to set up domain redirects to other URLs.

- **Method**: `POST`
- **Path**: `/api/domains/v1/forwarding`

#### domains_whois_pending-irtp-verification

Retrieve a pending IRTP verification for a domain.

Both the old and new registrant must confirm it before the WHOIS change takes effect.

Use this endpoint to check the status of a WHOIS change awaiting registrant confirmation.

- **Method**: `GET`
- **Path**: `/api/domains/v1/irtp/{domain}`

#### domains_whois_cancel-pending-irtp-verification

Cancel a pending IRTP verification.

Use this endpoint to back out of a WHOIS change that is stuck waiting on registrant confirmation,
for example when the confirmation email cannot be received, without waiting out the 5-day expiry.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/irtp/{domain}`

#### domains_move_incoming

Retrieve the incoming move for a specified domain.

Returns 404 when no account is moving this domain to you.

Use this endpoint to check whether a domain addressed to you is still waiting to be accepted.

- **Method**: `GET`
- **Path**: `/api/domains/v1/move/incoming/{domain}`

#### domains_move_accept-incoming

Accept an incoming move for a specified domain.

The provided WHOIS profiles become the contacts of the domain, so they must belong
to your account and satisfy the requirements of the TLD. Only the contact types the
domain actually uses are applied, but all four profile IDs have to be provided.

The move has to still be waiting for your decision, already accepted moves
cannot be accepted again.

Accepting does not complete the move. A confirmation email is sent to the email address of
the new owner contact, and the domain changes hands only after the change is confirmed from it.
Until then the move stays in the `activating` status, which can be followed with the
[incoming move endpoint](#tag/domains-move).

Use this endpoint to take ownership of a domain offered to you.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/move/incoming/{domain}`

#### domains_move_reject-incoming

Reject an incoming move for a specified domain.

The domain stays in the account which initiated the move.
Moves you have already accepted cannot be rejected anymore.

Use this endpoint to decline a domain you do not want to take over.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/move/incoming/{domain}`

#### domains_move_incoming-list

Retrieve all domains other Hostinger accounts are moving to your account.

Moves of every status are returned, including the ones which already completed.

Use this endpoint to find domains waiting for you to accept them.

- **Method**: `GET`
- **Path**: `/api/domains/v1/move/incoming`

#### domains_move_outgoing

Retrieve the outgoing move for a specified domain.

Returns 404 when the domain has no move in progress.

Use this endpoint to track the status of a move you have initiated for a single domain.

- **Method**: `GET`
- **Path**: `/api/domains/v1/move/outgoing/{domain}`

#### domains_move_start-outgoing

Initiate a move of a specified domain to another Hostinger account.

The receiving account has to already exist and accept the move before the domain changes hands.

The domain must be active. The subscription it belongs to is resolved automatically,
and the request is rejected with a 404 status code when the domain has no domain
subscription of its own.

Domains protected by premium protection require an additional verification step,
such requests are rejected with a 428 status code.

Use this endpoint to hand a domain over to another Hostinger user.

- **Method**: `POST`
- **Path**: `/api/domains/v1/move/outgoing/{domain}`

#### domains_move_cancel-outgoing

Cancel an outgoing move for a specified domain.

The move can only be cancelled while the receiving account has not accepted it yet.
The domain stays in your account.

Use this endpoint to withdraw a move you no longer want to complete.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/move/outgoing/{domain}`

#### domains_move_outgoing-list

Retrieve all domains you are moving to other Hostinger accounts.

Only moves which have not completed yet are returned.

Use this endpoint to track moves you have initiated and the accounts they are addressed to.

- **Method**: `GET`
- **Path**: `/api/domains/v1/move/outgoing`

#### domains_portfolio_authorization-code

Retrieve the authorization (EPP) code for a specified domain so it can be transferred
away from Hostinger to another registrar.

Requesting a new code invalidates any code retrieved previously.

Use this endpoint to obtain the code required to transfer a domain to another registrar.

- **Method**: `GET`
- **Path**: `/api/domains/v1/portfolio/{domain}/auth-code`

#### domains_portfolio_claim-free

Claim a free domain available on your account and register it.

Unlike purchasing a domain, this consumes a free domain you already have,
so no payment method is required.

A successful response means the domain is registered. If registration fails, login to
[hPanel](https://hpanel.hostinger.com/) and check domain registration status.

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Some TLDs require `additional_details` to be provided and these will be validated before claiming.

Requests which cannot be fulfilled are rejected with an error code in the response body,
for example `2037` when no free domain is available.

Use this endpoint to register a domain using a free domain from your account.

- **Method**: `POST`
- **Path**: `/api/domains/v1/portfolio/claim`

#### domains_portfolio_enable-lock

Enable domain lock for the domain.

When domain lock is enabled,
the domain cannot be transferred to another registrar without first disabling the lock.

Use this endpoint to secure domains against unauthorized transfers.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/portfolio/{domain}/domain-lock`

#### domains_portfolio_disable-lock

Disable domain lock for the domain.

Domain lock needs to be disabled before transferring the domain to another registrar.

Use this endpoint to prepare domains for transfer to other registrars.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/portfolio/{domain}/domain-lock`

#### domains_portfolio_get

Retrieve detailed information for specified domain.

Use this endpoint to view comprehensive domain configuration and status.

- **Method**: `GET`
- **Path**: `/api/domains/v1/portfolio/{domain}`

#### domains_portfolio_list

Retrieve all domains associated with your account.

Use this endpoint to view user's domain portfolio.

- **Method**: `GET`
- **Path**: `/api/domains/v1/portfolio`

#### domains_portfolio_purchase

Purchase and register a new domain name.

If registration fails, login to [hPanel](https://hpanel.hostinger.com/) and check domain registration status.

If no payment method is provided, your default payment method will be used automatically.

If the response is `202 Accepted`, the payment is still being processed and the domain was
**not** registered. Once the order completes, register the domain from
[hPanel](https://hpanel.hostinger.com/).

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Some TLDs require `additional_details` to be provided and these will be validated before completing purchase.

Use this endpoint to register new domains for users.

- **Method**: `POST`
- **Path**: `/api/domains/v1/portfolio`

#### domains_portfolio_enable-privacy-protection

Enable privacy protection for the domain.

When privacy protection is enabled, domain owner's personal information is hidden from public WHOIS database.

Use this endpoint to protect domain owner's personal information from public view.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/portfolio/{domain}/privacy-protection`

#### domains_portfolio_disable-privacy-protection

Disable privacy protection for the domain.

When privacy protection is disabled, domain owner's personal information is visible in public WHOIS database.

Use this endpoint to make domain owner's information publicly visible.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/portfolio/{domain}/privacy-protection`

#### domains_portfolio_renewal-information

Retrieve renewal information for a specified domain, including its status and current
expiration date.

Use this endpoint to build renewal automation and expiry monitoring for a single domain.

- **Method**: `GET`
- **Path**: `/api/domains/v1/portfolio/{domain}/renewal`

#### domains_portfolio_complete-setup

Register a domain you have already paid for but which has not been set up yet.

Use this endpoint when an order completed without registering the domain, for example when
`Purchase new domain` returned `202 Accepted` and the domain was added to your account without
being registered, or when an earlier setup attempt failed. No new order is placed and no payment
is taken: the subscription you already own is used, for the period you already paid for.

A domain is left awaiting setup when the details needed to register it were missing or invalid
as the order completed. Domains ordered elsewhere can be awaiting setup for the same reason.
Complete the missing information, then call this endpoint. If the order itself has not completed
yet, the domain is not on your account, wait until it appears in `Get domain list`.

If `domain_contacts` is omitted, the default WHOIS profile of that TLD is used for all four
roles. The profile must exist and be complete for the TLD, an incomplete profile is the most
common reason a domain is left awaiting setup. Create one with `Create WHOIS profile`.

Some TLDs require `additional_details`. These are validated before setup, so a missing or
invalid value is rejected without any registration being attempted.

The domain is set up with the default nameservers and without privacy protection. Use
`Update domain nameservers` and `Enable privacy protection` afterwards to change either.

A successful response means the setup request was accepted, not that the domain is already
registered. Poll `Get domain list` for the outcome, the domain appears in `Get domain details`
only once it is registered.

Use this endpoint to finish registering a domain that is awaiting setup on your account.

- **Method**: `POST`
- **Path**: `/api/domains/v1/portfolio/{domain}/setup`

#### domains_portfolio_update-nameservers

Set nameservers for a specified domain.

Be aware, that improper nameserver configuration can lead to the domain being unresolvable or unavailable.

Use this endpoint to configure custom DNS hosting for domains.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/portfolio/{domain}/nameservers`

#### domains_transfer_claim-free

Claim a free domain transfer available on your account and start the transfer.

Unlike purchasing a transfer, this consumes a free domain transfer you already have,
so no payment method is required.

Before making request, unlock the domain at the current registrar and get its authorization
code. The transfer is validated first, so domains which cannot be transferred are rejected
before the free domain transfer is consumed.

A successful response means the transfer has been started. Completion depends on the current
registrar and can be followed with the [transfer list endpoint](#tag/domains-transfer).

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Requests which cannot be fulfilled are rejected with an error code in the response body.

Use this endpoint to transfer a domain using a free domain transfer from your account.

- **Method**: `POST`
- **Path**: `/api/domains/v1/transfers/claim`

#### domains_transfer_get

Retrieve the transfer for a specified domain.

Use this endpoint to track an incoming or outgoing registrar transfer and its status.

- **Method**: `GET`
- **Path**: `/api/domains/v1/transfers/{domain}`

#### domains_transfer_list

Retrieve all domain transfers in your portfolio.

Use this endpoint to monitor incoming and outgoing registrar transfers across your domains.

- **Method**: `GET`
- **Path**: `/api/domains/v1/transfers`

#### domains_transfer_start

Transfer a domain from another registrar to your account.

The transfer runs on a domain transfer service you have already purchased.

Before making request, unlock the domain at the current registrar and get its authorization
code.

A successful response means the transfer has been started. Completion depends on the current
registrar and can be followed with the [transfer list endpoint](#tag/domains-transfer).

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Use this endpoint to bring domains registered elsewhere into your account.

- **Method**: `POST`
- **Path**: `/api/domains/v1/transfers`

#### domains_whois_change-for

Change WHOIS contact profile for a domain.

Repoints the given contact roles to a new WHOIS profile and submits the change to the registry.
The profile currently assigned to those roles is resolved automatically;
the request fails if the given roles are not all on the same profile today.

Changing transfer sensitive fields on the owner contact starts an IRTP verification.

The change is processed asynchronously.

Use this endpoint to move a registered domain onto different contact information.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/whois/change`

#### domains_whois_set-as-default

Set WHOIS contact profile as default.

The default profile is pre-selected for the TLD it belongs to when registering new domains.

Use this endpoint to avoid picking contact information for every registration.

- **Method**: `PUT`
- **Path**: `/api/domains/v1/whois/default/{whoisId}`

#### domains_whois_unset-default

Unset WHOIS contact profile as default.

The profile itself is kept, it is only no longer pre-selected for its TLD.

Use this endpoint to stop reusing contact information for new registrations.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/whois/default/{whoisId}`

#### domains_whois_get

Retrieve a WHOIS contact profile.

Use this endpoint to view domain registration contact information.

- **Method**: `GET`
- **Path**: `/api/domains/v1/whois/{whoisId}`

#### domains_whois_delete

Delete WHOIS contact profile.

Use this endpoint to remove unused contact profiles from account.

- **Method**: `DELETE`
- **Path**: `/api/domains/v1/whois/{whoisId}`

#### domains_whois_list

Retrieve WHOIS contact profiles.

Use this endpoint to view available contact profiles for domain registration.

- **Method**: `GET`
- **Path**: `/api/domains/v1/whois`

#### domains_whois_create

Create WHOIS contact profile.

Use this endpoint to add new contact information for domain registration.

- **Method**: `POST`
- **Path**: `/api/domains/v1/whois`

#### domains_whois_usage

Retrieve domain list where provided WHOIS contact profile is used.

Use this endpoint to view which domains use specific contact profiles.

- **Method**: `GET`
- **Path**: `/api/domains/v1/whois/{whoisId}/usage`

### `hostinger-ecommerce-mcp`

#### ecommerce_discounts_list

List a store's discounts. Filter by free text over code and name, or by disabled state.
Amounts for fixed discounts are integers in the smallest currency unit; percentage
discounts carry a whole-number value between 1 and 100.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/discounts`

#### ecommerce_discounts_create

Create a discount for a store. Fixed discounts take an amount in the smallest currency
unit (e.g. $10 is 1000); percentage discounts take a whole-number value between 1 and 100.
Free-shipping discounts ignore value. Returns the created discount.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/discounts`

#### ecommerce_miscellaneous_custom-storefront-setup-instructions

Retrieve step-by-step setup instructions, formatted as Markdown, for connecting a custom sales
channel to your store and keeping your catalog, orders, shipping and payments in sync through
the Ecommerce API.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/miscellaneous/custom-storefront-instructions`

#### ecommerce_orders_cancel

Cancel the order and optionally email the customer. Returns the updated order summary.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/orders/{order_id}/cancel`

#### ecommerce_orders_fulfil

Create a fulfilment for the order and attach tracking in one call. Omit items to fulfil
every remaining unfulfilled item. Returns the updated order summary.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/orders/{order_id}/fulfill`

#### ecommerce_orders_list-store

List a store's orders newest first as summaries. Filter by status, payment or fulfilment
status, customer email, order number or a free-text query. Amounts are in the smallest
currency unit. Retrieve a single order for its line items, addresses and fulfilments.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/orders`

#### ecommerce_orders_retrieve

Retrieve one order in full: line items (each with the id the fulfil endpoint needs),
addresses, the totals breakdown and fulfilments with tracking. Amounts are in the
smallest currency unit.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/orders/{order_id}`

#### ecommerce_payments_enable-manual-method

Enable a manual payment method so the store can accept orders without an online payment provider.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/payment-methods/manual`

#### ecommerce_payments_create-provider-connect-link

Create an onboarding link for connecting a payment gateway to the store. Returns the gateway
onboarding URL for the merchant to open and a deep-link into the store admin.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/payment-providers/{provider_id}/connect-link`

#### ecommerce_payments_list-store-providers

List a store's payment providers, split into providers already connected to the store and
gateways available to install. Never exposes gateway credentials, secrets, or configuration.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/payment-providers`

#### ecommerce_products_create-image-upload-url

Returns a signed URL to upload a product image to (multipart/form-data POST). Then call the
attach-image endpoint with the returned object_name to scan and attach it to the product.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/images/upload-url`

#### ecommerce_products_delete

Delete a product and its variants from the store. A subscription product with active
subscribers is archived instead of deleted so its data stays available.

- **Method**: `DELETE`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}`

#### ecommerce_products_update

Update a product's name, description, status, SEO settings or collections. Set status to
published to make it buyable, draft to hide it, or archived to retire it. SEO settings (title,
description, slug) left out keep their values. collection_changes adds or removes collections
without touching the others. Variants, prices and inventory are managed through the variant
endpoints, not here. Returns the updated product summary.

- **Method**: `PATCH`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}`

#### ecommerce_products_create-digital

Create a published digital product with a single variant and an optional external download link.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/digital`

#### ecommerce_products_list

List a store's products newest first as lean summaries (name, status, thumbnail, variant
count and price range). Prices are integers in the smallest currency unit and live on
variants. Filter by status, free text or a set of product ids. Use include=variants to
embed each product's variants with prices and inventory, and include=media to embed its media.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products`

#### ecommerce_products_create-physical

Create a published physical product with a single variant priced in the store currency.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/physical`

#### ecommerce_products_upload-and-attach-image

Fetch a raster image (JPEG, PNG, GIF or WebP, max 15MB) from a URL and attach it to a product in a
single call. Image downloads require HTTPS on port 443 without embedded credentials. At most one redirect
is allowed, and its destination must meet the same requirements. Private or reserved network
destinations, unsupported URLs and longer redirect chains are rejected. The image is virus-scanned
and validated by content, then stored on the CDN. Set is_thumbnail to make it the product's primary image.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/images`

#### ecommerce_sales-channels_list

List a store's active sales channels with their full metadata.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/sales-channels`

#### ecommerce_sales-channels_create

Create a sales channel for a store. A "custom" channel is headless: build your own frontend and keep
your catalog, orders, shipping and payments in sync through the Ecommerce API. A "quick-link" channel
is a hosted one-page store whose handle is auto-generated.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/sales-channels`

#### ecommerce_sales-channels_update

Update a custom sales channel. The merchant-facing `name` and the public `url`
(returned as the channel `domain`) can be changed. Pass `null` to clear a value.

- **Method**: `PATCH`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/sales-channels/{sales_channel_id}`

#### ecommerce_shipping_set-store

Set the flat-rate shipping price for a store, creating the shipping zone if it does not exist yet.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/shipping`

#### ecommerce_stores_delete

Soft-delete a store owned by your account.

The underlying store data is preserved; only the store is marked as deleted.

- **Method**: `DELETE`
- **Path**: `/api/ecommerce/v1/stores/{store_id}`

#### ecommerce_stores_list

Retrieve the stores associated with your account.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores`

#### ecommerce_stores_create

Create a new store for your account.

A primary sales channel is created alongside the store.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores`

#### ecommerce_stores_metadata

Get a store's readiness metadata: whether payment methods and shipping are configured,
plus its default currency. Useful to verify prerequisites before building a storefront.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/metadata`

#### ecommerce_product-variants_update-in-batch

Update up to 100 existing variants in place by id — title, SKU, inventory, stock tracking
and prices. Variants omitted from the request are left untouched. Prices replace the variant's
existing prices in full. Returns the updated variants.

- **Method**: `PATCH`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants/batch`

#### ecommerce_product-variants_delete

Delete a single variant from the product.

- **Method**: `DELETE`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants/{variant_id}`

#### ecommerce_product-variants_list

List a product's variants, ordered by rank, with their options, prices and inventory.
Prices are integers in the smallest currency unit and live on variants.

- **Method**: `GET`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants`

#### ecommerce_product-variants_create

Add a variant to a product along one or more option dimensions (e.g. Size, Color). Options
missing from the product are created automatically; provide a value for every option the
product already has. Prices are integers in the smallest currency unit and default to the
store currency. Returns the created variant.

- **Method**: `POST`
- **Path**: `/api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants`

### `hostinger-horizons-mcp`

#### horizons_websites_clone

Clone a Hostinger Horizons website into a new website.\n
Use this tool when the user wants a copy of an existing website, for example to try out
changes without touching the original.\n
This tool returns the ID and URL of the newly created copy.
The original website is left untouched.\n
To edit the copy, use the `Edit website` tool with the returned website ID, or the user can
open the provided website URL in Hostinger Horizons interface.

- **Method**: `POST`
- **Path**: `/api/horizons/v1/websites/{websiteId}/clone`

#### horizons_websites_list

List the Hostinger Horizons websites the user owns.\n
Use this tool when the user asks which websites they have, or when you need a website ID
before editing, publishing or cloning a website.\n
Each website is returned with its ID, status, domain and the URL to open it
in Hostinger Horizons interface.\n
The complete list of websites is returned in a single response - it is not paginated.

- **Method**: `GET`
- **Path**: `/api/horizons/v1/websites`

#### horizons_websites_create

Create new Hostinger Horizons website from the given message.\n
Use this tool when user asks you to create a website, landing page, blog
or any other type of application.\n
This tool initiates the website creation process and returns a website URL and ID.
The generation happens asynchronously.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that Hostinger Horizons is now creating their website and it will be ready in a few minutes
and you should provide the website URL to the user immediately
Do not write code.\n\nTo edit afterwards, use the `Edit website` tool with the returned
website ID, or the user can go to Hostinger Horizons interface in the provided website URL.
If the tool call fails with an error, you should provide a clear explanation of the error
and do not generate code yourself in the chat.
\n
TECHNOLOGY STACK CONSTRAINTS (STRICTLY ENFORCED):\n
The environment is limited to the following technologies.
You MUST NOT use, suggest, or implement any technology outside this list:\n
\n
- Language: JavaScript ONLY.
- Languages like TypeScript, Rust, Python, Java, PHP, etc., are STRICTLY PROHIBITED.\n
- Framework: React.\n
- Navigation: React Router.\n
- Styling: TailwindCSS.\n
- Components: shadcn/ui (built with @radix-ui primitives).\n
- Icons: Lucide React.\n
- Animations: Framer Motion.\n
\n
BACKEND & DATA STORAGE:\n
- Horizons integrated backend is the EXCLUSIVE solution for persistent data storage,
authentication, and database needs.\n
- Local databases (SQLite, MySQL, etc.) are STRICTLY PROHIBITED.\n
- Third-party services (Firebase, AWS Amplify) are allowed ONLY if explicitly requested by the user.\n
\n
MAPS:\n
- OpenStreetMap is the default provider.\n
- Alternative providers (Google Maps, Mapbox) are allowed ONLY if explicitly requested by the user.\n

- **Method**: `POST`
- **Path**: `/api/horizons/v1/websites`

#### horizons_websites_edit

Edit an existing Hostinger Horizons website with a follow-up message.\n
Use this tool when the user wants to change, extend or fix a website that already exists.\n
This tool queues the requested changes and returns the website URL and ID.
The changes are applied asynchronously.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that Hostinger Horizons is now applying the requested changes and they will be ready
in a few minutes, and you should provide the website URL to the user immediately.
Do not write code.\n
If the tool call fails with an error, you should provide a clear explanation of the error
and do not generate code yourself in the chat.

- **Method**: `POST`
- **Path**: `/api/horizons/v1/websites/{websiteId}/messages`

#### horizons_websites_publish

Publish a Hostinger Horizons website so its latest changes go live.\n
Use this tool when the user asks to publish, deploy or make their website live.\n
This tool starts the publish process and returns the URL the website will be live on.
Publishing happens asynchronously and takes a few minutes.\n
Set `is_template` only when the user explicitly asks to share the website as a template:
true adds a "Use template" banner to its published pages that copies the website into the
visitor's own account, and false removes it. Leave it out to keep the current setting.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that the website is being published and you should provide the published URL to the user immediately.

- **Method**: `POST`
- **Path**: `/api/horizons/v1/websites/{websiteId}/publish`

#### horizons_websites_get

Get the link for the user to open their website in Hostinger Horizons interface.\n
Use this tool when the user wants the link to an existing website, or when you need its
website URL before or after editing it.\n
`is_in_progress` is true while changes are being generated or the website is being published;
wait until it is false before publishing. `published_at` is when the website was last published,
`is_template` is whether its published pages show the "Use template" banner, and
`has_ecommerce_store` is whether it has an online store.\n
Websites can be edited with the `Edit website` tool, or by the user in Hostinger Horizons
interface in the provided website URL.

- **Method**: `GET`
- **Path**: `/api/horizons/v1/websites/{websiteId}`

### `hostinger-hosting-mcp`

#### hosting_deploy

Deploy, publish or upload a website to Hostinger web hosting (Shared, Cloud): static HTML, PHP, a nodejs (Node.js) app, a whole WordPress site, or a WordPress plugin or theme, from a local directory, an archive or a GitHub or GitLab repository. It detects what the project is and does the upload, build and Git setup itself: do not call upload or build operations, and do not archive the directory yourself. WARNING: it overwrites the website's contents and cannot be undone; confirm the domain with the user before deploying to a site that already has content. A Node.js build runs on the server: this returns a buildUuid at once, then call hosting_get-deployment until the build state is completed or failed. A plugin or theme goes into the site's WordPress installation, also when WordPress is in a folder of the document root (headless). Static, PHP, plugin and theme deploys are done when this returns; a WordPress site import only starts, and its files are extracted a few minutes later. From Git, pass type (static or nodejs) unless the site already runs a Node.js app or you pass Node.js settings; a static or PHP site deploys the branch now and again on every push; a Node.js site builds the branch now and on every later push, with the settings stored for the site (when none are stored, pass appType and nodeVersion from the project's engines, plus outputDirectory and buildScript if the app has a build step). Git needs GitHub or GitLab connected once in hPanel.

- **Method**: `custom`
- **Path**: `custom`

#### hosting_get-deployment

Check deployment status, build status, build logs and why a build failed (failure analysis) for a website's nodejs (Node.js) deployment: the state of its latest build (or of buildUuid), the end of the build log, the failure analysis when the build failed, and the build settings and Git auto-deployment settings stored for the site. Use it after hosting_deploy starts a Node.js build, and to find out why a deployment failed. Poll until the build state is completed or failed, with growing pauses. The log comes back in full; pass fromLine (the lines count from the previous call) to read only new output. A website without Node.js builds returns build: null with an explanation, because static, PHP, plugin and theme deploys are complete when hosting_deploy returns, and a WordPress site import is ready a few minutes after it starts.

- **Method**: `custom`
- **Path**: `custom`

#### hosting_cache_clear-website

Permanently clears all server-side cache for the website at once. Use it when content was
updated and needs to be visible immediately, or after making major changes.

Also purges the Hostinger CDN cache when CDN is enabled on the website. To purge only the CDN
cache and leave the server cache untouched, use `Purge CDN cache`. For a WordPress
installation living in a subdirectory, pass the directory query parameter to clear its cache.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cache/clear`

#### hosting_cache_toggle-cacheless

Turns development (cacheless) mode on or off, based on the enabled flag. When enabled, nothing
is cached, effectively turning off all caching for the website; use it while actively developing,
testing changes, debugging issues, or when real-time updates must be visible. Disable it after
finishing development work to restore the performance benefits of caching.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cacheless-mode/toggle`

#### hosting_cache_toggle-website

Turns server-side caching for the website on or off, based on the enabled flag. Enable it for
faster page loads, reduced server load, and improved user experience; recommended for production
websites. Disabling may impact performance; to temporarily bypass caching while developing or
debugging, prefer toggling cacheless mode instead.

Does nothing if caching is already in the requested state.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cache/toggle`

#### hosting_cdn_disable

Turns off the Hostinger CDN for the website domain. Once DNS propagation completes, the
website content is served directly from the origin server. Repeating the call is safe; when
CDN is already disabled, it applies the DNS change again.

Returns 422 for platform-managed domains (for example `*.hostingersite.com` and
`*.app-preview.com`), where CDN cannot be disabled, even when CDN is already off. Also returns
422 while the account is being moved to another server (retry after the move finishes), or
when the CDN provider rejects the change. Returns 404 when the domain is not a website on the
account.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cdn/disable`

#### hosting_cdn_enable

Turns on the Hostinger CDN for the website domain, which speeds up page loads and reduces the
load on the server. Works for the main domain, parked domains and subdomains of the account.

Enabling changes the domain's DNS records and usually takes a few seconds. After that, DNS
propagation can take a few more minutes before visitors are served through the CDN.

Repeating the call is safe, for example after a timeout. When CDN is already enabled, it
applies the DNS change again and refreshes the CDN SSL certificate.

Returns 422 when the account is disabled, while the account is being moved to another
server (retry after the move finishes), or when the CDN provider rejects the change.
Returns 404 when the domain is not a website on the account.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cdn/enable`

#### hosting_cdn_purge-cache

Purges the website's content from the Hostinger CDN edge cache only. The origin server cache
is not touched; to clear both, use `Clear website cache`.

Returns 422 when CDN is not enabled on the website. Returns 404 when the domain is not a
website on the account.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cdn/purge`

#### hosting_cdn_status

Returns whether the Hostinger CDN is enabled for the website domain. Works for the main
domain, parked domains and subdomains of the account.

The domain must be the exact website name as listed on the account, without a `www.` prefix.
Returns 404 when the domain is not a website on the account.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/cdn/status`

#### hosting_cron-jobs_list

Returns the list of cron jobs configured for the specified account, including their schedule and command.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/cron-jobs`

#### hosting_cron-jobs_create

Creates a cron job for the specified account from a schedule expression and a command.

Returns the created cron job, including its uid, which is required to delete the cron job or fetch its output.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/cron-jobs`

#### hosting_cron-jobs_delete

Permanently deletes the cron job identified by its uid.

The uid is returned by the list cron jobs endpoint.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/cron-jobs/{uid}`

#### hosting_cron-jobs_output

Returns the output captured from the last execution of the cron job identified by its uid.

The uid is returned by the list cron jobs endpoint.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/cron-jobs/{uid}/output`

#### hosting_databases_change-password

Changes the password for the specified database user.

The database name must be the full name returned by the list databases endpoint.
The password must also be updated in any website configuration that uses this database.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}/change-password`

#### hosting_databases_list

Returns a paginated list of databases for the specified account.

Use the domain and is_assigned filters to find databases assigned to a specific domain.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/databases`

#### hosting_databases_create

Creates a database with a database user and password for the specified account.

The database name and user are automatically prefixed with the account username when needed.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/databases`

#### hosting_databases_delete

Permanently deletes a database and its remote connections.

The database name must be the full name returned by the list databases endpoint.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}`

#### hosting_databases_create-remote-connection

Allows a remote host to connect to the specified database.

Provide an IPv4/IPv6 address, or "%" to allow any host. The database name must be
the full name returned by the list databases endpoint. Database creation is synchronous,
so a 404 here means no database with that name exists under the username, not that it
is still being created.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}/remote-connections`

#### hosting_databases_delete-remote-connection

Permanently removes a remote-access rule, revoking the given host's remote access to the database.

Identify the rule with the required ip query parameter (the IPv4/IPv6 address, or "%",
exactly as returned by the list remote connections endpoint). The database name must be
the full name returned by the list databases endpoint.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}/remote-connections`

#### hosting_databases_list-remote-connections

Returns the remote-access rules for the specified account: the remote hosts
(IPv4/IPv6 addresses, or "%" for any host) allowed to connect to the account databases.

Use the domain filter to only return rules for databases assigned to a specific domain.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/remote-connections`

#### hosting_databases_repair

Repairs corrupted database tables asynchronously.

Use when database errors, crashes, or corruption are reported.
The database name must be the full name returned by the list databases endpoint.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}/repair`

#### hosting_databases_setup-website

Creates a new MySQL database for the website and writes its connection details into the
website's environment variables, then restarts the application. The platform generates the
password (and the database name and user, unless supplied). The password is never returned;
the application reads it from the environment.

Written variables: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` and
`DATABASE_URL` (`mysql://user:password@host:port/name`, user and password percent-encoded).
Existing variables are kept. If the website already has any variable with one of these
names the call fails with 422 and nothing is created; the `Replace Node.js environment
variables` endpoint removes them.

After this call the variables are ordinary environment variables: the
`Replace Node.js environment variables` endpoint changes or removes them like any other.

A restart is enough for apps that read environment variables at process start, such as
Express or NestJS. Frameworks that bake variables into the build output (Next.js,
`NEXT_PUBLIC_*`) see the new values only after a fresh build (`Start Node.js build` endpoint).

A password in the request is ignored; the platform always generates it. The optional `name`
and `user` are identifiers, not secrets.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/databases/setup`

#### hosting_databases_phpmyadmin-link

Returns a direct sign-on link to phpMyAdmin for the specified database.

Use this when a visual database interface is needed for SQL queries, imports, exports, or table management.
The database name must be the full name returned by the list databases endpoint.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/databases/{name}/phpmyadmin-link`

#### hosting_datacenters_list

Retrieve a list of datacenters available for setting up hosting plans
based on available datacenter capacity and hosting plan of your order.
The first item in the list is the best match for your specific order
requirements.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/datacenters`

#### hosting_domains_generate-free-subdomain

Generate a unique free subdomain that can be used for hosting services without purchasing custom domains.
Free subdomains allow you to start using hosting services immediately
and you can always connect a custom domain to your site later.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/domains/free-subdomains`

#### hosting_domains_list-website-parked

Retrieve all parked or alias domains created under the selected website.

Use this endpoint to inspect parked domain configuration for a specific website,
including the parent domain and root directory assigned to each parked domain.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains`

#### hosting_domains_create-website-parked

Create a parked or alias domain for the selected website.

Provide a domain name or IP address to park on the website so it serves the same content
as the parent domain.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains`

#### hosting_domains_delete-website-parked

Delete an existing parked or alias domain from the selected website.

Use this endpoint to remove parked domains that are no longer needed.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains/{parkedDomain}`

#### hosting_domains_list-website-subdomains

Retrieve all subdomains created under the selected website.

Use this endpoint to inspect subdomain configuration for a specific website,
including the parent domain and root directory assigned to each subdomain.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/subdomains`

#### hosting_domains_create-website-subdomain

Create a new subdomain for the selected website.

Provide a subdomain prefix and, optionally, a custom directory or the
website public directory to use as the subdomain root.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/subdomains`

#### hosting_domains_delete-website-subdomain

Delete an existing subdomain from the selected website.

Use this endpoint to remove subdomains that are no longer needed.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/subdomains/{subdomain}`

#### hosting_domains_verify-ownership

Verify ownership of a single domain and return the verification status.

Use this endpoint to check if a domain is accessible for you before using it for new websites.
If the domain is accessible, the response will have `is_accessible: true`.
If not, add the given TXT record to your domain's DNS records and try verifying again.
Keep in mind that it may take up to 10 minutes for new TXT DNS records to propagate.

Skip this verification when using Hostinger's free subdomains (*.hostingersite.com).

- **Method**: `POST`
- **Path**: `/api/hosting/v1/domains/verify-ownership`

#### hosting_files_list-website-and-directories

List files and directories under a website's document root.

Use `directory` to browse a subdirectory relative to the document root. Symlinked entries
are listed but never traversed into or resolved.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/domains/{domain}/files`

#### hosting_files_website-content

Get a single file's content, relative to a website's document root.

Read-only; refuses symlinks, oversized files, non-text file types, and files identified as
containing secrets (e.g. credential files) — none of these are returned by this endpoint.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/domains/{domain}/files/content`

#### hosting_git_delete-auto-deployment-settings

Removes the Git auto-deployment settings of the website. Files already deployed stay on the
website; pushes stop deploying until settings are saved again. Succeeds also when nothing is
configured.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/git/auto-deployments/settings`

#### hosting_git_deploy-website-repository

Clones a Git repository into a directory of the website, or pulls it again. An empty or missing
directory gets a clone of the branch. A directory that already holds this repository and branch is
reset to its last commit and pulled: changes made on the server to files the repository tracks are
discarded, files it does not track stay. A directory that holds other files, including another
repository or another branch of this one, is rejected. `composer install` runs after the clone or
pull when the repository has a `composer.json`.

The call waits for the deployment and returns its log. `is_success` false means Git or composer
failed and the log says why. A second call for the same directory is rejected while the first is
still waiting for the server. If the request times out, the deployment may still finish on the
server; calling again later with the same repository and branch pulls.

Private repositories need an SSH URL and the account's Git SSH key from `Generate Git SSH key`,
added to the repository as a deploy key.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/git/repositories/deploy`

#### hosting_git_list-website-repositories

Lists the Git repositories linked to directories of the website, with
`Deploy website Git repository` or in the Git section of hPanel: clone URL, branch and directory of
each one. A repository whose clone failed stays listed; deploying it again retries the clone. GitHub
and GitLab auto-deployments are not listed here; see `Get Git auto-deployment settings`.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/git/repositories`

#### hosting_git_ssh-public-key

Returns the public SSH key of the hosting account. `Deploy website Git repository` uses this key to
clone and pull over SSH, so a private repository works once the key is added to it as a deploy key
on the Git host. `public_key` is null when the account has no key yet.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/git/ssh-key`

#### hosting_git_generate-ssh-key

Creates the SSH key pair of the hosting account and returns the public key. When the account already
has a key, returns that key unchanged. One key serves every website of the account; add the public
key to a private repository as a deploy key before deploying it.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/git/ssh-key`

#### hosting_headless_submit-build-report

Submits the build report the headless skill writes at the end of a run (including early
stops), so Hostinger can learn where builds get stuck. Send one report per call, with the
report JSON as the request body, unchanged. Only send a report when the user agreed to it.

The report must match report.schema.json v1; an invalid report returns 422 and is not
stored. The report is linked to the authenticated account, so do not add account details
to it.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/headless/agent-reports`

#### hosting_nodejs_build-settings-from-repository

Determine the build settings for a Node.js application from the package.json file of a branch
in a Git repository. Use before starting a Git-source build to find out the auto-detected
settings instead of guessing them.

The repository is read through a Git installation: take `installation_uuid` from
`List Git installations` and `owner` and `repository` from `List Git installation repositories`.

Returns 422 when the installation is not found, the repository or branch is not found, or
the branch has no package.json.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/from-repository`

#### hosting_nodejs_list-environment-variables

Lists the Node.js environment variables currently set for the website. Values are always
masked as `********` and cannot be read back through this API. Use this endpoint to see
which keys are configured or to verify a change, not to read values.

To change variables, use the `Replace Node.js environment variables` endpoint. It replaces
the whole set, so never copy the masked values from this response into that request; send
the full desired set with real values taken from the project `.env` file or the user
prompt instead.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/env`

#### hosting_nodejs_replace-environment-variables

Replaces the website's Node.js environment variables with the ones provided. This is a
full replace: any variable not in the request is deleted, and sending an empty `env_vars`
array deletes every variable. Saving writes the values and restarts the running Node.js
process.

A restart is enough for apps that read environment variables at process start, such as
Express or NestJS. It is not enough for frameworks that bake variables into the build.
Next.js standalone is one of those: build-time values (including `NEXT_PUBLIC_*`) need a
fresh build. After this call, use the `Start Node.js build` endpoint so those apps
pick up the new values.

The `List Node.js environment variables` endpoint returns masked values (`********`), so
never copy values from it into this request. Always send the full desired set with real
values taken from the project `.env` file or the user prompt.

- **Method**: `PUT`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/env`

#### hosting_nodejs_runtime-logs

Returns the Node.js application's runtime console log entries, oldest first, each with
timestamp, level and message. On the first call send `period` (`1h`, `1d`, `1w` or `1m`)
and optionally `levels` and `limit` (1-5000, default 1000); when more entries match than
`limit`, the newest are kept.

To poll for new entries send `total_lines + 1` from the previous response as `from_line`
and omit `period`; `period` and `from_line` cannot be combined. Lines that are not JSON
with a timestamp, level and message are skipped, so `logs` may hold fewer than `limit`
entries while `total_lines` counts every raw line. Entries with a timestamp before
`last_deployed_at` belong to the previous deployment. Returns an empty `logs` list when
the application has not written a log file yet.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/runtime-logs`

#### hosting_nodejs_clear-runtime-logs

Empties the Node.js application's runtime log file. This cannot be undone, so confirm with
the user before calling it. Returns success even when no log file exists yet.

Use it before reproducing a problem so the next `Get Node.js runtime logs` call returns
only fresh entries; start that call with `period` again instead of reusing a `from_line`
from before the clear.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/runtime-logs`

#### hosting_nodejs_restart-application

Restarts the Node.js server process for the website. Does not rebuild or redeploy the
application. Use it to apply environment or configuration changes, or to recover a hung
application.

Only applicable to server-side applications (Express, Next.js, NestJS, etc.). Static
front-end apps (React, Vue, Vite) have no persistent server process, so restarting them
has no effect. Returns success even when the website has no server process to restart.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/server/restart`

#### hosting_nodejs_list-vulnerabilities

Lists known npm package vulnerabilities detected on a Node.js website, enriched with
advisory metadata (severity, CVSS score, CVE, advisory URL). Results are sorted from
the most severe to the least severe, then by publish date (newest first). Use the
`severities` query parameter to filter.

Vulnerabilities with `is_patchable` set to `true` can be auto-fixed via the
`Patch Node.js Vulnerabilities` endpoint, which opens a GitHub pull request with
updated package versions. Auto-fix is only available for websites deployed from a
connected GitHub repository. Vulnerabilities with `is_patching_in_progress` set to
`true` are already included in an open patch pull request; while any patch pull
request is open, new patch requests for this website are rejected until it is merged
or closed.

Data comes from periodic dependency scans, so it may lag behind the latest deployment.
An empty list means the most recent scan found no vulnerabilities; it does not
guarantee the current deployment is vulnerability-free. Available on Business and
Cloud Hosting plans.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities`

#### hosting_nodejs_patch-vulnerabilities

Patches the selected Node.js vulnerabilities by updating the affected package versions
in `package.json` and opening a GitHub pull request in the connected repository. The
customer reviews and merges the pull request; merging triggers the automatic deployment.

Auto-fix is only available for websites deployed from a connected GitHub repository.
Websites deployed from an archive have no auto-fix path and return a 404. The Hostinger
GitHub App needs write access to the repository; without it the request fails with a
403 explaining the missing permission.

Only vulnerabilities with `is_patchable` set to `true` can be patched. Non-patchable
IDs in the selection are skipped; the pull request covers the patchable subset, listed
in `patched_vulnerability_ids`. Selections without any patchable vulnerability are
rejected with a 422. Only one patch pull request can be open at a time per website;
close or merge it before patching again. Available on Business and Cloud Hosting plans.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities/patch`

#### hosting_websites_list-setups

Returns the website setups started in the last 24 hours for the hosting accounts
accessible to the authenticated client, newest first. Narrow the list with the
`order_id`, `subscription_id` or `domain` filters.

Meant for polling right after creating a website or starting a website setup: the
website shows up in the websites list before its server-side setup has finished, and
while the setup is `running` endpoints that operate on that website may respond with
`404` or `409`. Poll this endpoint with the `domain` filter every 10 to 15 seconds and
wait for `status: completed` before uploading files, deploying or creating databases.
`failed` means the setup stopped before finishing or has not reported progress for
over an hour. Setups older than 24 hours are not listed.

`type` is the website type the setup was started with (`wordpress`, `headless_empty`,
`headless_wordpress`, `headless_ecommerce`, `headless_pocketbase`), or `null` for an empty
website.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/onboardings`

#### hosting_websites_start-setup

Starts a website setup on a Web or Cloud hosting order and returns the created setup
right away; the website itself is provisioned asynchronously. Poll the list website
setups endpoint (`hosting_websites_list-setups`) with the `domain` filter every 10 to 15
seconds and wait for `status: completed` before uploading files, deploying or creating
databases.

Omit `type` for an empty website. `type: wordpress` installs WordPress in the website
root with the admin user, email and password from `wordpress`, the domain as the site
title, and `en_US` when `wordpress.language` is omitted. The headless types
(`headless_empty`, `headless_wordpress`, `headless_ecommerce`, `headless_pocketbase`)
create a headless website; `headless_wordpress` additionally installs WordPress into the
`cms` directory of the website root with generated credentials. `headless_empty` installs
nothing: WordPress can be added later through
`POST /api/hosting/v1/accounts/{username}/wordpress/installations`
(`wordpress_installations_install`) with `type: headless`.

Omit `domain` to set the website up on a generated temporary free subdomain. To know the
free subdomain before the call, so a timed-out call can be looked up and retried on the
same domain, generate one through `POST /api/hosting/v1/domains/free-subdomains`
(`hosting_domains_generate-free-subdomain`) and send it as `domain`. It is accepted for
24 hours, only from the client that generated it.

When the order has no hosting account yet, the setup creates one first, in the datacenter
given by `datacenter_code` or the order's default datacenter when it is omitted.
Returns 404 when the order does not exist or is not accessible to the authenticated
client, and 409 with a `Retry-After` header while a setup for the same domain is still
running.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/orders/{order_id}/onboardings`

#### hosting_orders_list

Retrieve a paginated list of orders accessible to the authenticated client.

Only Web and Cloud hosting orders are listed. Agency Plan orders are listed by
`GET /api/agency-hosting/v1/orders`.

This endpoint returns orders of your hosting accounts as well as orders
of other client hosting accounts that have shared access with you.

Use the available query parameters to filter results by order statuses
or specific order IDs for more targeted results.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/orders`

#### hosting_php_reset-extensions

Resets all PHP extensions of the website to their default state.

Use it to recover from extension conflicts or restore the original configuration.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/extensions/reset`

#### hosting_php_get

Returns the full PHP configuration for the website: current version, available versions
(supported and unsupported), enabled/disabled extensions, options with their current value,
default, type and the plan limit (`max`), and conflicting extension groups.

Use it to check the current PHP setup before updating the version, extensions or options.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/details`

#### hosting_php_info

Returns the full phpinfo page (HTML) for the website.

Use it to debug PHP issues or inspect the complete PHP environment of the website.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/php-info`

#### hosting_php_update-extensions

Enables or disables PHP extensions (modules) for the website.

Use the Get PHP details endpoint to check the current extension states before changing them.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/extensions`

#### hosting_php_update-options

Updates PHP options for the website (e.g. `memory_limit`, `max_execution_time`, `upload_max_filesize`).
Only provide the options you want to change, inside the `options` object.

Values above the account plan limit are silently capped to that limit, so the request can succeed
with a smaller applied value. Call the Get PHP details endpoint afterwards to read the applied value.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/options`

#### hosting_php_update-version

Changes the PHP version of the website.

Use the Get PHP details endpoint to see the versions available for the website.

- **Method**: `PATCH`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/php/version`

#### hosting_redirects_list-website

Returns a paginated list of redirects configured for the selected website.

- **Method**: `GET`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/redirects`

#### hosting_redirects_create-website

Creates a redirect from a URL on the selected website to another URL or IP address.

- **Method**: `POST`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/redirects`

#### hosting_redirects_delete-website

Permanently deletes the redirect identified by its source URL.

Pass the `from` value exactly as returned by the list redirects endpoint.

- **Method**: `DELETE`
- **Path**: `/api/hosting/v1/accounts/{username}/websites/{domain}/redirects`

#### hosting_ssl_install

Requests a lifetime SSL certificate for the website. The installation runs in the background;
`Get SSL status` reports `active` or `failed` when it ends. An `active` lifetime certificate
does not block the request: a new installation is requested, which is how a certificate is
reinstalled.

Returns 422 for free subdomains (their certificate is managed by the platform), while an
installation is `installing` or `waiting_for_retry`, when the website's certificate was
revoked (it cannot be reissued), and when an uploaded 