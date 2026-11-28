# [pgvector](https://github.com/pgvector/pgvector) binary compile, Microsoft Windows x64, PostgreSQL

[![GitHub all releases](https://img.shields.io/github/downloads/andreiramani/pgvector_pgsql_windows/total)](https://github.com/andreiramani/pgvector_pgsql_windows/releases)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/andreiramani/pgvector_pgsql_windows)](https://github.com/andreiramani/pgvector_pgsql_windows/releases/latest)

> [!NOTE]
> **Unofficial release**

See the [latest releases](https://github.com/andreiramani/pgvector_pgsql_windows/releases/latest) for available versions and read the [wiki](https://github.com/andreiramani/pgvector_pgsql_windows/wiki).

## How to's (v0.8.x)

​	Check `readme.txt` inside the archive.

## Upgrading

Extract the latest version (check `readme.txt` inside the zip release). Then in each database you want to upgrade, run:

```sql
ALTER EXTENSION vector UPDATE;
```

You can check the version in the current database with:

```sql
SELECT extversion FROM pg_extension WHERE extname = 'vector';
```

<details>
<summary><b>How to's (v0.7.3, v0.7.4)</b></summary>

1. Extract the zip file to `[pg_installed folder]\share\extension\`.
2. Activate the extension:

   ```sql
   CREATE EXTENSION vector;
   ```

   [![Screenshot made with Navicat Premium](img/01-create_extension.jpg)](https://www.navicat.com/en/products/navicat-premium)

3. Run this query to check if the extension is enabled (`t`):

   ```sql
   SELECT extname, extrelocatable, extversion FROM pg_extension WHERE extname = 'vector';
   ```

   [![Screenshot made with Navicat Premium](img/02-check_extension.jpg)](https://www.navicat.com/en/products/navicat-premium)

</details>

---

**Contributor compiler:** [vjivandro](https://github.com/vjivandro) (v0.7.3, v0.7.4), [andreiramani](https://github.com/andreiramani) (v0.8.0 - v0.8.7)

[![Star History Chart](https://api.star-history.com/chart?repos=andreiramani/pgvector_pgsql_windows&type=date&legend=bottom-right)](https://www.star-history.com/?repos=andreiramani%2Fpgvector_pgsql_windows&type=date&legend=bottom-right)
