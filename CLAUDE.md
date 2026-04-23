# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A PySpark learning series ("PySpark - Zero to Hero") with 27 numbered Jupyter notebooks progressing from basics to advanced topics. Source for the YouTube playlist at `https://youtube.com/playlist?list=PL2IsFZBGM_IHCl9zhRVC1EXTomkEp_1zm`.

## Environment setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/). Python 3.12, PySpark 4.1, and delta-spark 4.2 are pinned in `pyproject.toml`.

```bash
make install       # create .venv and install all dependencies
make kernel        # register the "PySpark (spark-plug)" Jupyter kernel (run once)
```

## Running notebooks

```bash
make lab                          # launch JupyterLab (select the "PySpark (spark-plug)" kernel)
make run nb=01_spark_session.ipynb  # execute a notebook in-place non-interactively
```

## Execution environments

Notebooks target one of three environments — check the `SparkSession` at the top of each notebook:

| Environment | `master` value | Data paths | Notes |
|---|---|---|---|
| **Local** | `local[*]` | relative `data/output/...` | Runs anywhere with PySpark installed |
| **Docker cluster** | `spark://<host>:7077` | `/data/input/`, `/data/output/` | Use `docker compose up` from `pyspark-cluster-with-jupyter` in the `subhamkharwal/docker-images` repo |
| **Databricks** | (none — uses cluster attach) | `/data/input/`, `/data/output/` | Notebooks 23+ use `dbutils`, `display()`, and `%sql` — must run on Databricks |

### Docker cluster setup (notebooks 12, 18–27)

1. Clone `https://github.com/subhamkharwal/docker-images`
2. `cd pyspark-cluster-with-jupyter && docker compose up`
3. Get the Jupyter token from the JupyterLab container logs and open `http://localhost:8888`
4. Place all input files under `/data/` — this path is volume-mounted across master, workers, and history server

## Notebook curriculum

| Range | Topics |
|---|---|
| 01–11 | SparkSession, DataFrame transformations, reading/writing CSV/JSON/Parquet/ORC |
| 12–14 | Cluster architecture, DAG, execution plan |
| 15–17 | Shuffles, caching, broadcast/accumulator variables |
| 18–21 | Join optimization, dynamic allocation, skewness & spillage, AQE |
| 22 | Spark SQL |
| 23–25 | Delta Lake (CRUD, time travel, VACUUM, OPTIMIZE, Z-ordering) |
| 26 | Concurrent jobs with `concurrent.futures.ThreadPoolExecutor` |
| 27 | Memory management and OOM debugging (`spark_oom_files.7z` has supporting data) |

## Sample datasets

`datasets/` contains the local copies of input files referenced throughout the notebooks:

- `emp.csv`, `emp_new.csv` — employee records used in early transformation notebooks
- `sales.csv`, `new_sales.csv`, `sales_data.parquet`, `sales_data.orc` — sales data used in read/write and Delta Lake notebooks
- `cities.csv` — used in notebook 26 (concurrent tasks)
- `order_singleline.json`, `order_multiline.json` — JSON format examples
- `sales_total_parquet/`, `sales_total_orc/` — pre-partitioned multi-file output examples

When running on the Docker cluster or Databricks, copy these files to `/data/input/` so the cluster workers can access them.

## Delta Lake notes

Notebooks 23–25 use Delta Lake. `delta-spark` is included in the project dependencies. For local execution, the SparkSession must be configured with the Delta extensions:

```python
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

spark = configure_spark_with_delta_pip(
    SparkSession.builder
    .appName("Delta")
    .master("local[*]")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
).getOrCreate()
```

The original notebook cells use Databricks-specific APIs (`dbutils`, `display()`, `%sql`) and will not run locally as-is.
