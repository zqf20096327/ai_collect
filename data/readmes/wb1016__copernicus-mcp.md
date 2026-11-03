# Copernicus Earth Observation MCP Server

An [MCP](https://modelcontextprotocol.io/) server for Copernicus **Sentinel**
data from the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)
(CDSE): search products and Sentinel-1 SLC bursts, inspect metadata, and
download data with background jobs.

* **Missions**: Sentinel-1, -2, -3, -5P, -6
* **Python**: 3.13+
* **Auth**: token-first (refresh token or access token), password grant as
  fallback

## Features

**Search & discovery**
- Search by point / bounding box / polygon (GeoJSON or WKT), date range, and
  mission-specific filters (product type, processing level, satellite, cloud
  cover, orbit direction, relative orbit, Sentinel-2 tile, S1 mode/swath/
  polarisation, or any catalogue attribute)
- Real server-side filtering (cloud cover and attributes are filtered by the
  API, not silently dropped)
- Recent products, temporal coverage analysis, full product metadata with
  checksums and quicklook URLs

**Sentinel-1 SLC bursts**
- Search bursts by parent product, burst/absolute burst id, subswath,
  polarisation, mode, orbit, datatake, or area + time
- Download bursts as zip via the CDSE on-demand extraction service
  (background job)

**Downloads**
- Background download jobs (products, S1 native archives, quicklooks, bursts)
  with status, progress, speed, and cancellation — no more MCP tool timeouts
  on multi-GB products
- Resumable downloads (HTTP Range), MD5 checksum verification
- Quicklooks download synchronously (small, fast previews)

**File management**
- List / statistics / cleanup of downloaded files, all confined to the
  configured download root (dry-run by default)

## Installation

```bash
git clone <repository-url>
cd copernicus-mcp

uv venv -p 3.13          # or 3.14
uv pip install -e ".[dev]"
```

A free account is required for downloads: <https://dataspace.copernicus.eu/>

## Authentication

Token-based authentication is primary. Configure **one** of:

| Priority | Environment variable | Notes |
|---|---|---|
| 1 | `COPERNICUS_ACCESS_TOKEN` | Static bearer token, used as-is |
| 2 | `COPERNICUS_REFRESH_TOKEN` | **Recommended.** Access tokens are minted and renewed automatically |
| 3 | `COPERNICUS_USERNAME` + `COPERNICUS_PASSWORD` | Password grant (legacy fallback) |

Search works without authentication; downloads require a token.

## Running the server

```bash
copernicus-mcp                          # stdio transport (default)
python -m copernicus_mcp                # equivalent

copernicus-mcp --transport http --host 127.0.0.1 --port 8000
copernicus-mcp --log-level DEBUG --version
```

### MCP client configuration (stdio)

```json
{
  "mcpServers": {
    "copernicus": {
      "command": "copernicus-mcp",
      "env": {
        "COPERNICUS_REFRESH_TOKEN": "<your-refresh-token>"
      }
    }
  }
}
```

## Tools

### Search & discovery

| Tool | Purpose |
|---|---|
| `search_products` | Search Sentinel products (geometry, dates, mission filters, attributes) |
| `get_product_details` | Full metadata, checksums, assets and download URLs for one product (by UUID or name) |
| `get_recent_products` | Most recent products for an area |
| `check_coverage` | Temporal coverage analysis (counts per day/week/month/year) |
| `get_mission_info` | Mission capabilities and supported filters |

### Sentinel-1 SLC bursts

| Tool | Purpose |
|---|---|
| `search_bursts` | Search bursts (parent product, burst ids, swath, polarisation, orbit, area, time) |
| `get_burst_details` | Burst raster metadata (Lines, SamplesPerBurst, ByteOffset, S3Path) |
| `download_burst` | Start background on-demand burst extraction (zip) |

### Downloads

| Tool | Purpose |
|---|---|
| `start_download` | Start a background job: `product`, `compressed` (S1 native `$zip`) or `quicklook` |
| `download_quicklook` | Synchronous quicklook download (small preview image) |
| `get_download_status` | Job status, progress %, bytes, speed, output path |
| `list_download_jobs` | All jobs, newest first |
| `cancel_download` | Cancel a queued/running job (partial data kept for resume) |

### File management

| Tool | Purpose |
|---|---|
| `list_downloaded_files` | List files in the download root |
| `get_download_statistics` | Totals and breakdowns by type / mission / month |
| `cleanup_downloads` | Delete old or excess files (dry-run by default) |

### Typical workflow

```
1. search_products(geometry=[2.29, 48.85, 2.30, 48.86], mission="sentinel-2",
                   start_date="2024-06-01", end_date="2024-06-30",
                   max_cloud_cover=20)
2. get_product_details(image_id="<uuid from results>")
3. download_quicklook(image_id="<uuid>")            # fast preview
4. start_download(image_id="<uuid>", kind="product") # background job
5. get_download_status(job_id="<job_id>")
```

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `COPERNICUS_DOWNLOAD_DIR` | `downloads` | Download root (all file access is confined to it) |
| `COPERNICUS_MAX_CONCURRENT_DOWNLOADS` | `3` | Parallel background downloads |
| `COPERNICUS_API_TIMEOUT` | `60` | Catalogue request timeout (seconds) |
| `COPERNICUS_DOWNLOAD_TIMEOUT` | `7200` | Download timeout (seconds) |
| `COPERNICUS_API_BASE` | CDSE catalogue | Override for testing |

## Architecture

```
copernicus_mcp/
├── server.py        # FastMCP wiring + CLI
├── app.py           # service container (built once per process)
├── config.py        # settings from environment
├── auth.py          # token manager (refresh/access token, password)
├── errors.py        # exception hierarchy
├── odata/
│   ├── query.py     # pure query builders (dates, geometry, filters)
│   ├── models.py    # Product / Burst / Asset / Checksum models
│   └── client.py    # async OData client (paging, retries)
├── downloads/
│   ├── manager.py   # streaming, resume, checksums, path confinement
│   ├── jobs.py      # background job manager
│   └── service.py   # executes download jobs
└── tools/           # MCP tool implementations
```

Notes:
- Queries follow the official CDSE OData syntax; see
  [`docs/odata-quickref.md`](docs/odata-quickref.md) and the documentation
  snapshots in [`docs/reference/`](docs/reference/).
- Background jobs are in-memory: they do not survive a server restart
  (partial files stay on disk and are resumed on retry).

## Development

```bash
uv pip install -e ".[dev]"
pytest                 # unit + tool tests (no network; httpx.MockTransport)
ruff check copernicus_mcp tests
```

## Docker

```bash
docker build -t copernicus-mcp .
docker run -i --rm -e COPERNICUS_REFRESH_TOKEN=<token> copernicus-mcp   # stdio
docker run --rm -e COPERNICUS_REFRESH_TOKEN=<token> \
  -v $PWD/downloads:/data/downloads -e COPERNICUS_DOWNLOAD_DIR=/data/downloads \
  copernicus-mcp --transport http --host 0.0.0.0 --port 8000
```

## API notes and limitations

- **Scope**: Sentinel collections only (SENTINEL-1/2/3/5P/6). Other CDSE
  collections (CCM, CLMS, COP-DEM, Landsat, ...) exist in the catalogue but
  are not exposed here.
- **Native archives** (`compressed`): Sentinel-1 RAW/GRD/SLC, one month after
  publication only.
- **Burst downloads** use the CDSE on-demand extraction service and may take a
  while; if the service is unavailable, `get_burst_details` provides the
  `S3Path`/`ByteOffset`/`Lines`/`SamplesPerBurst` values needed for GDAL-based
  extraction (see the Sentinel-1 SLC Bursts documentation).
- Full products can be several GB — prefer quicklooks for previews.

## License

LGPL-3.0-or-later (see [LICENSE](LICENSE)).

## Acknowledgments

- ESA and the Copernicus programme
- The Copernicus Data Space Ecosystem for API access
