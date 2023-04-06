# Comparing `tmp/udata_hydra-2.0.0.dev919.tar.gz` & `tmp/udata_hydra-2.0.0.dev956.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "udata_hydra-2.0.0.dev919.tar", max compression
+gzip compressed data, was "udata_hydra-2.0.0.dev956.tar", max compression
```

## Comparing `udata_hydra-2.0.0.dev919.tar` & `udata_hydra-2.0.0.dev956.tar`

### file list

```diff
@@ -1,35 +1,39 @@
--rw-r--r--   0        0        0     8815 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/README.md
--rw-r--r--   0        0        0     1266 2023-02-01 16:42:03.727985 udata_hydra-2.0.0.dev919/pyproject.toml
--rw-r--r--   0        0        0     1145 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/__init__.py
--rw-r--r--   0        0        0        0 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/analysis/__init__.py
--rw-r--r--   0        0        0     9005 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/analysis/csv.py
--rw-r--r--   0        0        0     9530 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/analysis/resource.py
--rw-r--r--   0        0        0    10921 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/app.py
--rw-r--r--   0        0        0     9058 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/cli.py
--rw-r--r--   0        0        0     1436 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/config_default.toml
--rw-r--r--   0        0        0     1222 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/context.py
--rw-r--r--   0        0        0    12800 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/crawl.py
--rw-r--r--   0        0        0      875 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/logger.py
--rw-r--r--   0        0        0     2125 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/__init__.py
--rw-r--r--   0        0        0      224 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/csv/20221205_initial_up_rev1.sql
--rw-r--r--   0        0        0       63 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/csv/20230130_drop_migrations.sql
--rw-r--r--   0        0        0      756 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221205_initial_up_rev1.sql
--rw-r--r--   0        0        0       96 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221206_rev1_up_rev2.sql
--rw-r--r--   0        0        0       84 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221206_rev2_up_rev3.sql
--rw-r--r--   0        0        0       82 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221208_rev3_up_rev4.sql
--rw-r--r--   0        0        0      120 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221208_rev4_up_rev5.sql
--rw-r--r--   0        0        0      240 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20230119_rev5_up_rev6.sql
--rw-r--r--   0        0        0      156 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20230121_rev6_up_rev7.sql
--rw-r--r--   0        0        0      124 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20230121_rev7_up_rev8.sql
--rw-r--r--   0        0        0       63 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20230130_drop_migrations.sql
--rw-r--r--   0        0        0        0 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/__init__.py
--rw-r--r--   0        0        0      342 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/csv.py
--rw-r--r--   0        0        0     3030 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/db.py
--rw-r--r--   0        0        0     1527 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/file.py
--rw-r--r--   0        0        0     1174 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/http.py
--rw-r--r--   0        0        0      236 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/json.py
--rw-r--r--   0        0        0     1884 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/minio.py
--rw-r--r--   0        0        0      482 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/utils/queue.py
--rw-r--r--   0        0        0      161 2023-02-01 16:40:32.000000 udata_hydra-2.0.0.dev919/udata_hydra/worker.py
--rw-r--r--   0        0        0    10697 1970-01-01 00:00:00.000000 udata_hydra-2.0.0.dev919/setup.py
--rw-r--r--   0        0        0    10222 1970-01-01 00:00:00.000000 udata_hydra-2.0.0.dev919/PKG-INFO
+-rw-r--r--   0        0        0     8815 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/README.md
+-rw-r--r--   0        0        0     1288 2023-02-11 09:03:37.414664 udata_hydra-2.0.0.dev956/pyproject.toml
+-rw-r--r--   0        0        0     1145 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/analysis/__init__.py
+-rw-r--r--   0        0        0    10167 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/analysis/csv.py
+-rw-r--r--   0        0        0      144 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/analysis/errors.py
+-rw-r--r--   0        0        0      694 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/analysis/helpers.py
+-rw-r--r--   0        0        0     9394 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/analysis/resource.py
+-rw-r--r--   0        0        0    10921 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/app.py
+-rw-r--r--   0        0        0     9198 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/cli.py
+-rw-r--r--   0        0        0     1436 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/config_default.toml
+-rw-r--r--   0        0        0     1222 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/context.py
+-rw-r--r--   0        0        0    12819 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/crawl.py
+-rw-r--r--   0        0        0      875 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/logger.py
+-rw-r--r--   0        0        0     2125 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/__init__.py
+-rw-r--r--   0        0        0      224 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/csv/20221205_initial_up_rev1.sql
+-rw-r--r--   0        0        0       63 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/csv/20230130_drop_migrations.sql
+-rw-r--r--   0        0        0      108 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/csv/20230206_datetime_aware.sql
+-rw-r--r--   0        0        0      756 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221205_initial_up_rev1.sql
+-rw-r--r--   0        0        0       96 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221206_rev1_up_rev2.sql
+-rw-r--r--   0        0        0       84 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221206_rev2_up_rev3.sql
+-rw-r--r--   0        0        0       82 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221208_rev3_up_rev4.sql
+-rw-r--r--   0        0        0      120 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221208_rev4_up_rev5.sql
+-rw-r--r--   0        0        0      240 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20230119_rev5_up_rev6.sql
+-rw-r--r--   0        0        0      156 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20230121_rev6_up_rev7.sql
+-rw-r--r--   0        0        0      124 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20230121_rev7_up_rev8.sql
+-rw-r--r--   0        0        0       63 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20230130_drop_migrations.sql
+-rw-r--r--   0        0        0      343 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20230206_datetime_aware.sql
+-rw-r--r--   0        0        0        0 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/__init__.py
+-rw-r--r--   0        0        0      342 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/csv.py
+-rw-r--r--   0        0        0     3030 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/db.py
+-rw-r--r--   0        0        0     1527 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/file.py
+-rw-r--r--   0        0        0      955 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/http.py
+-rw-r--r--   0        0        0      236 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/json.py
+-rw-r--r--   0        0        0     1884 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/minio.py
+-rw-r--r--   0        0        0      482 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/utils/queue.py
+-rw-r--r--   0        0        0      161 2023-02-11 09:01:58.000000 udata_hydra-2.0.0.dev956/udata_hydra/worker.py
+-rw-r--r--   0        0        0    10726 1970-01-01 00:00:00.000000 udata_hydra-2.0.0.dev956/setup.py
+-rw-r--r--   0        0        0    10265 1970-01-01 00:00:00.000000 udata_hydra-2.0.0.dev956/PKG-INFO
```

### Comparing `udata_hydra-2.0.0.dev919/README.md` & `udata_hydra-2.0.0.dev956/README.md`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/pyproject.toml` & `udata_hydra-2.0.0.dev956/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "udata-hydra"
-version = "2.0.0.dev919"
+version = "2.0.0.dev956"
 description = "Async crawler and parsing service for data.gouv.fr"
 authors = ["Opendata Team <opendatateam@data.gouv.fr>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.9"
@@ -13,26 +13,27 @@
 aiohttp = "^3.8.1"
 asyncpg = "^0.27.0"
 boto3 = "^1.21.21"
 humanfriendly = "^10.0"
 marshmallow = "^3.14.1"
 minicli = "^0.5.0"
 progressist = "^0.1.0"
-python-dateutil = "^2.8.2"
 python-magic = "^0.4.25 "
 redis = "^4.1.4"
 sentry-sdk = "^1.11.1"
 aiocontextvars = "^0.2.2"
 coloredlogs = "^15.0.1"
 rq = "^1.11.1"
 toml = "^0.10.2"
-csv-detective = "^0.4.6"
 str2float = "^0.0.9"
 str2bool = "^1.1"
 sqlalchemy = "^1.4.46"
+dateparser = "^1.1.7"
+python-dateutil = "^2.8.2"
+csv-detective = "^0.4.7"
 
 [tool.poetry.group.dev.dependencies]
 flake8-quotes = "^3.3.1"
 flake8 = "^4.0.1"
 gunicorn = "^20.1.0"
 aiohttp-devtools = "^1.0.post0"
 aioresponses = "^0.7.3"
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/__init__.py` & `udata_hydra-2.0.0.dev956/udata_hydra/__init__.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/analysis/csv.py` & `udata_hydra-2.0.0.dev956/udata_hydra/analysis/csv.py`

 * *Files 15% similar despite different names*

```diff
@@ -8,25 +8,32 @@
 from datetime import datetime
 from typing import Any
 
 import sentry_sdk
 
 from csv_detective.explore_csv import routine as csv_detective_routine
 from progressist import ProgressBar
-from sqlalchemy import MetaData, Table, Column, BigInteger, String, Float, Boolean, Integer
+from sqlalchemy import (
+    MetaData, Table, Column,
+    BigInteger, String, Float, Boolean, Integer, JSON, Date, DateTime,
+)
 from sqlalchemy.dialects.postgresql import asyncpg
 from sqlalchemy.schema import CreateTable
 from str2bool import str2bool
 from str2float import str2float
 
 from udata_hydra import context, config
+from udata_hydra.analysis import helpers
+from udata_hydra.analysis.errors import ParseException
+from udata_hydra.utils import queue
 from udata_hydra.utils.db import (
     get_check, insert_csv_analysis, compute_insert_query,
     update_csv_analysis, get_csv_analysis,
 )
+from udata_hydra.utils.http import send
 from udata_hydra.utils.file import download_resource
 
 
 log = logging.getLogger("udata-hydra")
 
 # Increase CSV field size limit to maximum possible
 # https://stackoverflow.com/a/15063941
@@ -39,63 +46,84 @@
         field_size_limit = int(field_size_limit / 10)
 
 PYTHON_TYPE_TO_PG = {
     "string": String,
     "float": Float,
     "int": BigInteger,
     "bool": Boolean,
+    "json": JSON,
+    "date": Date,
+    "datetime": DateTime,
 }
 
 PYTHON_TYPE_TO_PY = {
     "string": str,
     "float": float,
     "int": int,
     "bool": bool,
+    "json": helpers.to_json,
+    "date": helpers.to_date,
+    "datetime": helpers.to_datetime,
 }
 
 RESERVED_COLS = ("__id", "tableoid", "xmin", "cmin", "xmax", "cmax", "ctid")
 
 
+async def notify_udata(ca_id):
+    """Notify udata of the result of a parsing"""
+    analysis = await get_csv_analysis(ca_id)
+    resource_id = analysis["resource_id"]
+    db = await context.pool()
+    record = await db.fetchrow("SELECT dataset_id FROM catalog WHERE resource_id = $1", resource_id)
+    if record:
+        payload = {
+            "resource_id": resource_id,
+            "dataset_id": record["dataset_id"],
+            "document": {
+                "analysis:parsing:table": analysis["parsing_table"],
+                "analysis:parsing:error": analysis["parsing_error"],
+                "analysis:parsing:created_at": analysis["created_at"].isoformat(),
+            }
+        }
+        queue.enqueue(send, _priority="high", **payload)
+
+
 async def analyse_csv(check_id: int = None, url: str = None, file_path: str = None, debug_insert: bool = False) -> None:
     """Launch csv analysis from a check or an URL (debug), using previsously downloaded file at file_path if any"""
     if not config.CSV_ANALYSIS_ENABLED:
         log.debug("CSV_ANALYSIS_ENABLED turned off, skipping.")
         return
 
     assert any(_ is not None for _ in (check_id, url))
     check = await get_check(check_id) if check_id is not None else {}
     url = check.get("url") or url
 
     headers = json.loads(check.get("headers") or "{}")
     tmp_file = open(file_path, "rb") if file_path else await download_resource(url, headers)
+    table_name = hashlib.md5(url.encode("utf-8")).hexdigest()
 
     try:
-        try:
-            inspection_error = None
-            csv_inspection = await perform_csv_inspection(tmp_file.name)
-        except Exception as e:
-            inspection_error = e
         ca_id = await insert_csv_analysis({
             "resource_id": check.get("resource_id"),
             "url": url,
             "check_id": check_id,
         })
-        if inspection_error:
-            await handle_parse_exception(inspection_error, "csv_detective", analysis_id=ca_id)
-            return
-        table_name = hashlib.md5(url.encode("utf-8")).hexdigest()
-        await csv_to_db(tmp_file.name, csv_inspection, table_name, debug_insert=debug_insert, analysis_id=ca_id)
+        csv_inspection = await perform_csv_inspection(tmp_file.name)
+        await csv_to_db(tmp_file.name, csv_inspection, table_name, debug_insert=debug_insert)
         await update_csv_analysis(ca_id, {
             "parsing_table": table_name,
             "parsing_date": datetime.utcnow(),
         })
         await csv_to_db_index(table_name, csv_inspection, check)
+    except ParseException as e:
+        await handle_parse_exception(e, ca_id, table_name)
     finally:
         tmp_file.close()
         os.remove(tmp_file.name)
+        await notify_udata(ca_id)
 
 
 def generate_dialect(inspection: dict) -> stdcsv.Dialect:
     class CustomDialect(stdcsv.unix_dialect):
         # TODO: it would be nice to have more info from csvdetective to feed the dialect
         # in the meantime we might want to sniff the file a bit
         delimiter = inspection["separator"]
@@ -129,28 +157,23 @@
     compiled = CreateTable(table).compile(dialect=asyncpg.dialect())
     # compiled query will want to write "%% mon pourcent" VARCHAR but will fail when querying "% mon pourcent"
     # also, "% mon pourcent" works well in pg as a column
     # TODO: dirty hack, maybe find an alternative
     return compiled.string.replace("%%", "%")
 
 
-async def csv_to_db(
-    file_path: str, inspection: dict, table_name: str,
-    debug_insert: bool = False, analysis_id: int = None,
-):
+async def csv_to_db(file_path: str, inspection: dict, table_name: str, debug_insert: bool = False):
     """
     Convert a csv file to database table using inspection data. It should (re)create one table:
     - `table_name` with data from `file_path`
 
     :file_path: CSV file path to convert
     :inspection: CSV detective report
     :table_name: used to create tables
     :debug_insert: insert record one by one instead of using postgresql COPY
-    # TODO: we might want to catch the error(s) a step above and get rid of this param
-    :analysis_id: used for reporting errors to the analysis object that lauched conversion
     """
     log.debug(f"Converting from CSV to db for {table_name}")
     dialect = generate_dialect(inspection)
     columns = inspection["columns"]
     # build a `column_name: type` mapping and explicitely rename reserved column names
     columns = {
         f"{c}__hydra_renamed" if c.lower() in RESERVED_COLS else c: v["python_type"]
@@ -176,15 +199,15 @@
         )
         # this use postgresql COPY from an iterator, it's fast but might be difficult to debug
         if not debug_insert:
             # NB: also see copy_to_table for a file source
             try:
                 await db.copy_records_to_table(table_name, records=records, columns=columns.keys())
             except Exception as e:  # I know what I'm doing, pinky swear
-                await handle_parse_exception(e, "copy_records_to_table", analysis_id)
+                raise ParseException("copy_records_to_table") from e
         # this inserts rows from iterator one by one, slow but useful for debugging
         else:
             bar = ProgressBar(total=inspection["total_lines"])
             for r in bar.iter(records):
                 data = {k: v for k, v in zip(columns.keys(), r)}
                 # NB: possible sql injection here, but should not be used in prod
                 q = compute_insert_query(data, table_name, returning="__id")
@@ -196,35 +219,42 @@
     db = await context.pool("csv")
     q = "INSERT INTO tables_index(parsing_table, csv_detective, resource_id, url) VALUES($1, $2, $3, $4)"
     await db.execute(q, table_name, json.dumps(inspection), check.get("resource_id"), check.get("url"))
 
 
 async def perform_csv_inspection(file_path):
     """Launch csv-detective against given file"""
-    return csv_detective_routine(file_path)
+    try:
+        return csv_detective_routine(file_path)
+    except Exception as e:
+        raise ParseException("csv_detective") from e
 
 
 async def delete_table(table_name: str):
     db = await context.pool("csv")
     await db.execute(f'DROP TABLE IF EXISTS "{table_name}"')
     await db.execute("DELETE FROM tables_index WHERE parsing_table = $1", table_name)
 
 
-async def handle_parse_exception(e: Exception, step: str, analysis_id: int) -> None:
-    """Specific parsing_error handling. Enriches sentry w/ context if available,
-       and store error if in a check context"""
+async def handle_parse_exception(e: Exception, analysis_id: int, table_name: str) -> None:
+    """Specific ParsingError handling. Enriches sentry w/ context if available,
+       and store error if in a check context. Also cleanup :table_name: if needed."""
+    db = await context.pool("csv")
+    await db.execute(f'DROP TABLE IF EXISTS "{table_name}"')
     if analysis_id:
         if config.SENTRY_DSN:
             analysis = await get_csv_analysis(analysis_id)
             url = analysis["url"]
             with sentry_sdk.push_scope() as scope:
                 scope.set_extra("analysis_id", analysis_id)
                 scope.set_extra("csv_url", url)
                 scope.set_extra("resource_id", analysis["resource_id"])
                 event_id = sentry_sdk.capture_exception(e)
-        err = f"{step}:sentry:{event_id}" if config.SENTRY_DSN else f"{step}:{str(e)}"
+        # e.__cause__ let us access the "inherited" error of ParseException (raise e from cause)
+        # it's called explicit exception chaining and it's very cool, look it up (PEP 3134)!
+        err = f"{e.step}:sentry:{event_id}" if config.SENTRY_DSN else f"{e.step}:{str(e.__cause__)}"
         q = "UPDATE csv_analysis SET parsing_error = $1 WHERE id = $2"
         db = await context.pool()
         await db.execute(q, err, analysis_id)
         log.error("Parsing error", exc_info=e)
-        return
-    raise e
+    else:
+        raise e
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/analysis/resource.py` & `udata_hydra-2.0.0.dev956/udata_hydra/analysis/resource.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 import os
 
 from datetime import datetime
 from typing import Union
 
 import magic
 
-from dateutil.parser import parse as date_parser, ParserError
+from dateparser import parse as date_parser
 
 from udata_hydra import context
 from udata_hydra.utils import queue
 from udata_hydra.analysis.csv import analyse_csv
 from udata_hydra.utils.csv import detect_csv_from_headers
 from udata_hydra.utils.db import update_check, get_check
 from udata_hydra.utils.file import compute_checksum_from_file, download_resource
@@ -194,23 +194,20 @@
     async with pool.acquire() as connection:
         data = await connection.fetchrow(q, value)
     if not data:
         return
 
     # last modified header check
     if data["last_modified"]:
-        try:
-            # this is GMT so we should be able to safely ignore tz info
-            last_modified_date = date_parser(data["last_modified"], ignoretz=True).isoformat()
+        last_modified_date = date_parser(data["last_modified"])
+        if last_modified_date:
             return {
-                "analysis:last-modified-at": last_modified_date,
+                "analysis:last-modified-at": last_modified_date.isoformat(),
                 "analysis:last-modified-detection": "last-modified-header",
             }
-        except ParserError:
-            pass
 
     # switch to content-length comparison
     if not data["content_length"]:
         return
     q = """
     SELECT
         created_at,
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/app.py` & `udata_hydra-2.0.0.dev956/udata_hydra/app.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/cli.py` & `udata_hydra-2.0.0.dev956/udata_hydra/cli.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import csv
 import os
 
-from datetime import datetime
+from datetime import datetime, timezone
 from pathlib import Path
 from tempfile import NamedTemporaryFile
 
 import aiohttp
 import asyncpg
 
 from humanfriendly import parse_size
@@ -69,15 +69,17 @@
                     )
                     VALUES ($1, $2, $3, $4, FALSE, FALSE)
                     ON CONFLICT (dataset_id, resource_id, url) DO UPDATE SET deleted = FALSE
                 """,
                     row["dataset.id"],
                     row["id"],
                     row["url"],
-                    datetime.fromisoformat(row["harvest.modified_at"]) if row["harvest.modified_at"] else None,
+                    # force timezone info to UTC (catalog data should be in UTC)
+                    datetime.fromisoformat(row["harvest.modified_at"]).replace(tzinfo=timezone.utc)
+                    if row["harvest.modified_at"] else None,
                 )
         log.info("Catalog successfully upserted into DB.")
     except Exception as e:
         raise e
     finally:
         fd.close()
         os.unlink(fd.name)
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/config_default.toml` & `udata_hydra-2.0.0.dev956/udata_hydra/config_default.toml`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/context.py` & `udata_hydra-2.0.0.dev956/udata_hydra/context.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/crawl.py` & `udata_hydra-2.0.0.dev956/udata_hydra/crawl.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import time
 
 from collections import defaultdict
-from datetime import datetime, timedelta
+from datetime import datetime, timedelta, timezone
 from typing import Tuple
 from urllib.parse import urlparse
 
 import aiohttp
 import asyncio
 
 from humanfriendly import parse_timespan
@@ -100,15 +100,15 @@
     return await insert_check(check_data), is_first_check
 
 
 async def is_backoff(domain) -> Tuple[bool, str]:
     backoff = False, ""
     no_backoff = [f"'{d}'" for d in config.NO_BACKOFF_DOMAINS]
     no_backoff = f"({','.join(no_backoff)})"
-    since = datetime.utcnow() - timedelta(seconds=config.BACKOFF_PERIOD)
+    since = datetime.now(timezone.utc) - timedelta(seconds=config.BACKOFF_PERIOD)
     pool = await context.pool()
     async with pool.acquire() as connection:
         # check if we trigger BACKOFF_NB_REQ for BACKOFF_PERIOD on this domain
         res = await connection.fetchrow(
             f"""
             SELECT COUNT(*) FROM checks
             WHERE domain = $1
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/logger.py` & `udata_hydra-2.0.0.dev956/udata_hydra/logger.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/migrations/__init__.py` & `udata_hydra-2.0.0.dev956/udata_hydra/migrations/__init__.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/migrations/main/20221205_initial_up_rev1.sql` & `udata_hydra-2.0.0.dev956/udata_hydra/migrations/main/20221205_initial_up_rev1.sql`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/utils/db.py` & `udata_hydra-2.0.0.dev956/udata_hydra/utils/db.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/utils/file.py` & `udata_hydra-2.0.0.dev956/udata_hydra/utils/file.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/utils/http.py` & `udata_hydra-2.0.0.dev956/udata_hydra/utils/http.py`

 * *Files 14% similar despite different names*

```diff
@@ -5,18 +5,14 @@
 
 from udata_hydra import config
 
 log = logging.getLogger("udata-hydra")
 
 
 async def send(dataset_id: str, resource_id: str, document: dict) -> None:
-    # Extras in udata can't be None
-    # FIXME: we will need to send None values
-    # cf https://github.com/etalab/data.gouv.fr/issues/1001
-    document = {k: document[k] for k in document if document[k] is not None}
     log.debug(f"Sending payload to udata {dataset_id}/{resource_id}: {json.dumps(document, indent=4)}")
 
     if not config.WEBHOOK_ENABLED:
         log.debug("Webhook disabled, skipping send")
         return
 
     if not config.UDATA_URI or not config.UDATA_URI_API_KEY:
```

### Comparing `udata_hydra-2.0.0.dev919/udata_hydra/utils/minio.py` & `udata_hydra-2.0.0.dev956/udata_hydra/utils/minio.py`

 * *Files identical despite different names*

### Comparing `udata_hydra-2.0.0.dev919/setup.py` & `udata_hydra-2.0.0.dev956/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,16 @@
 install_requires = \
 ['aiocontextvars>=0.2.2,<0.3.0',
  'aiohttp>=3.8.1,<4.0.0',
  'asyncpg>=0.27.0,<0.28.0',
  'boto3>=1.21.21,<2.0.0',
  'cchardet>=2.1.7,<3.0.0',
  'coloredlogs>=15.0.1,<16.0.0',
- 'csv-detective>=0.4.6,<0.5.0',
+ 'csv-detective>=0.4.7,<0.5.0',
+ 'dateparser>=1.1.7,<2.0.0',
  'humanfriendly>=10.0,<11.0',
  'marshmallow>=3.14.1,<4.0.0',
  'minicli>=0.5.0,<0.6.0',
  'pandas>=1.3.3,<2.0.0',
  'progressist>=0.1.0,<0.2.0',
  'python-dateutil>=2.8.2,<3.0.0',
  'python-magic>=0.4.25,<0.5.0',
@@ -36,15 +37,15 @@
 entry_points = \
 {'console_scripts': ['udata-hydra = udata_hydra.cli:run',
                      'udata-hydra-app = udata_hydra.app:run',
                      'udata-hydra-crawl = udata_hydra.crawl:run']}
 
 setup_kwargs = {
     'name': 'udata-hydra',
-    'version': '2.0.0.dev919',
+    'version': '2.0.0.dev956',
     'description': 'Async crawler and parsing service for data.gouv.fr',
     'long_description': '# udata-hydra 🦀\n\n`udata-hydra` is an async metadata crawler for [data.gouv.fr](https://www.data.gouv.fr).\n\nURLs are crawled via _aiohttp_, catalog and crawled metadata are stored in a _PostgreSQL_ database.\n\nSince it\'s called _hydra_, it also has mythical powers embedded:\n- analyse remote resource metadata over time to detect changes in the smartest way possible\n- if the remote resource is a CSV, convert it to a PostgreSQL table, ready for APIfication\n- send crawl and analysis info to a udata instance\n\n## CLI\n\n### Create database structure\n\nInstall udata-hydra dependencies and cli.\n`poetry install`\n\n`poetry run udata-hydra migrate`\n\n### Load (UPSERT) latest catalog version from data.gouv.fr\n\n`udata-hydra load-catalog`\n\n## Crawler\n\n`udata-hydra-crawl`\n\nIt will crawl (forever) the catalog according to config set in `config.py`.\n\n`BATCH_SIZE` URLs are queued at each loop run.\n\nThe crawler will start with URLs never checked and then proceed with URLs crawled before `SINCE` interval. It will then wait until something changes (catalog or time).\n\nThere\'s a by-domain backoff mecanism. The crawler will wait when, for a given domain in a given batch, `BACKOFF_NB_REQ` is exceeded in a period of `BACKOFF_PERIOD` seconds. It will retry until the backoff is lifted.\n\nIf an URL matches one of the `EXCLUDED_PATTERNS`, it will never be checked.\n\n## Worker\n\nA job queuing system is used to process long-running tasks. Launch the worker with the following command:\n\n`poetry run rq worker -c udata_hydra.worker`\n\nMonitor worker status:\n\n`poetry run rq info -c udata_hydra.worker --interval 1`\n\n## CSV conversion to database\n\nConverted CSV tables will be stored in the database specified via `config.DATABASE_URL_CSV`. For tests it\'s same database as for the catalog. Locally, `docker compose` will launch two distinct database containers.\n\n## API\n\n### Run\n\n```\npoetry install\npoetry run adev runserver udata_hydra/app.py\n```\n\n### Get latest check\n\nWorks with `?url={url}` and `?resource_id={resource_id}`.\n\n```\n$ curl -s "http://localhost:8000/api/checks/latest/?url=http://opendata-sig.saintdenis.re/datasets/661e19974bcc48849bbff7c9637c5c28_1.csv" | json_pp\n{\n   "status" : 200,\n   "catalog_id" : 64148,\n   "deleted" : false,\n   "error" : null,\n   "created_at" : "2021-02-06T12:19:08.203055",\n   "response_time" : 0.830198049545288,\n   "url" : "http://opendata-sig.saintdenis.re/datasets/661e19974bcc48849bbff7c9637c5c28_1.csv",\n   "domain" : "opendata-sig.saintdenis.re",\n   "timeout" : false,\n   "id" : 114750,\n   "dataset_id" : "5c34944606e3e73d4a551889",\n   "resource_id" : "b3678c59-5b35-43ad-9379-fce29e5b56fe",\n   "headers" : {\n      "content-disposition" : "attachment; filename=\\"xn--Dlimitation_des_cantons-bcc.csv\\"",\n      "server" : "openresty",\n      "x-amz-meta-cachetime" : "191",\n      "last-modified" : "Wed, 29 Apr 2020 02:19:04 GMT",\n      "content-encoding" : "gzip",\n      "content-type" : "text/csv",\n      "cache-control" : "must-revalidate",\n      "etag" : "\\"20415964703d9ccc4815d7126aa3a6d8\\"",\n      "content-length" : "207",\n      "date" : "Sat, 06 Feb 2021 12:19:08 GMT",\n      "x-amz-meta-contentlastmodified" : "2018-11-19T09:38:28.490Z",\n      "connection" : "keep-alive",\n      "vary" : "Accept-Encoding"\n   }\n}\n```\n\n### Get all checks for an URL or resource\n\nWorks with `?url={url}` and `?resource_id={resource_id}`.\n\n```\n$ curl -s "http://localhost:8000/api/checks/all/?url=http://www.drees.sante.gouv.fr/IMG/xls/er864.xls" | json_pp\n[\n   {\n      "domain" : "www.drees.sante.gouv.fr",\n      "dataset_id" : "53d6eadba3a72954d9dd62f5",\n      "timeout" : false,\n      "deleted" : false,\n      "response_time" : null,\n      "error" : "Cannot connect to host www.drees.sante.gouv.fr:443 ssl:True [SSLCertVerificationError: (1, \\"[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for \'www.drees.sante.gouv.fr\'. (_ssl.c:1122)\\")]",\n      "catalog_id" : 232112,\n      "url" : "http://www.drees.sante.gouv.fr/IMG/xls/er864.xls",\n      "headers" : {},\n      "id" : 165107,\n      "created_at" : "2021-02-06T14:32:47.675854",\n      "resource_id" : "93dfd449-9d26-4bb0-a6a9-ee49b1b8a4d7",\n      "status" : null\n   },\n   {\n      "timeout" : false,\n      "deleted" : false,\n      "response_time" : null,\n      "error" : "Cannot connect to host www.drees.sante.gouv.fr:443 ssl:True [SSLCertVerificationError: (1, \\"[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for \'www.drees.sante.gouv.fr\'. (_ssl.c:1122)\\")]",\n      "domain" : "www.drees.sante.gouv.fr",\n      "dataset_id" : "53d6eadba3a72954d9dd62f5",\n      "created_at" : "2020-12-24T17:06:58.158125",\n      "resource_id" : "93dfd449-9d26-4bb0-a6a9-ee49b1b8a4d7",\n      "status" : null,\n      "catalog_id" : 232112,\n      "url" : "http://www.drees.sante.gouv.fr/IMG/xls/er864.xls",\n      "headers" : {},\n      "id" : 65092\n   }\n]\n```\n\n### Get crawling status\n\n```\n$ curl -s "http://localhost:8000/api/status/crawler/" | json_pp\n{\n   "fresh_checks_percentage" : 0.4,\n   "pending_checks" : 142153,\n   "total" : 142687,\n   "fresh_checks" : 534,\n   "checks_percentage" : 0.4\n}\n```\n\n### Get worker status\n\n```\n$ curl -s "http://localhost:8000/api/status/worker/" | json_pp\n{\n   "queued" : {\n      "default" : 0,\n      "high" : 825,\n      "low" : 655\n   }\n}\n```\n\n### Get crawling stats\n\n```\n$ curl -s "http://localhost:8000/api/stats/" | json_pp\n{\n   "status" : [\n      {\n         "count" : 525,\n         "percentage" : 98.3,\n         "label" : "ok"\n      },\n      {\n         "label" : "error",\n         "percentage" : 1.3,\n         "count" : 7\n      },\n      {\n         "label" : "timeout",\n         "percentage" : 0.4,\n         "count" : 2\n      }\n   ],\n   "status_codes" : [\n      {\n         "code" : 200,\n         "count" : 413,\n         "percentage" : 78.7\n      },\n      {\n         "code" : 501,\n         "percentage" : 12.4,\n         "count" : 65\n      },\n      {\n         "percentage" : 6.1,\n         "count" : 32,\n         "code" : 404\n      },\n      {\n         "code" : 500,\n         "percentage" : 2.7,\n         "count" : 14\n      },\n      {\n         "code" : 502,\n         "count" : 1,\n         "percentage" : 0.2\n      }\n   ]\n}\n```\n\n## Using Webhook integration\n\n** Set the config values**\n\nCreate a `config.toml` where your service and commands are launched, or specify a path to a TOML file via the `HYDRA_SETTINGS` environment variable. `config.toml` or equivalent will override values from `udata_hydra/config_default.toml`, lookup there for values that can/need to be defined.\n\n```toml\nUDATA_URI = "https://dev.local:7000/api/2"\nUDATA_URI_API_KEY = "example.api.key"\nSENTRY_DSN = "https://{my-sentry-dsn}"\n```\n\nThe webhook integration sends HTTP messages to `udata` when resources are analyzed or checked to fill resources extras.\n\nRegarding analysis, there is a phase called "change detection". It will try to guess if a resource has been modified based on different criterions:\n- harvest modified date in catalog\n- content-length and last-modified headers\n- checksum comparison over time\n\nThe payload should look something like:\n\n```json\n{\n   "analysis:filesize": 91661,\n   "analysis:mime-type": "application/zip",\n   "analysis:checksum": "bef1de04601dedaf2d127418759b16915ba083be",\n   "analysis:last-modified-at": "2022-11-27T23:00:54.762000",\n   "analysis:last-modified-detection": "harvest-resource-metadata",\n}\n```\n\n## Development\n\n### docker-compose\n\nMultiple docker-compose files are provided:\n- a minimal `docker-compose.yml` with two PostgreSQL containers (one for catalog and metadata, the other for converted CSV to database)\n- `docker-compose.broker.yml` adds a Redis broker\n- `docker-compose.test.yml` launches a test DB, needed to run tests\n\nNB: you can launch compose from multiple files like this: `docker-compose -f docker-compose.yml -f docker-compose.test.yml up`\n\n### Logging & Debugging\n\nThe log level can be adjusted using the environment variable LOG_LEVEL.\nFor example, to set the log level to `DEBUG` when initializing the database, use `LOG_LEVEL="DEBUG" udata-hydra init_db `.\n\n### Writing a migration\n\n1. Add a file named `migrations/{YYYYMMDD}_{description}.sql` and write the SQL you need to perform migration.\n2. `udata-hydra migrate` will migrate the database as needeed.\n\n## Deployment\n\n3 services need to be deployed for the full stack to run:\n- worker\n- api / app\n- crawler\n\nRefer to each section to learn how to launch them. The only differences from dev to prod are:\n- use `HYDRA_SETTINGS` env var to point to your custom `config.toml`\n- use `HYDRA_APP_SOCKET_PATH` to configure where aiohttp should listen to a [reverse proxy connection (eg nginx)](https://docs.aiohttp.org/en/stable/deployment.html#nginx-configuration) and use `udata-hydra-app` to launch the app server\n',
     'author': 'Opendata Team',
     'author_email': 'opendatateam@data.gouv.fr',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `udata_hydra-2.0.0.dev919/PKG-INFO` & `udata_hydra-2.0.0.dev956/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: udata-hydra
-Version: 2.0.0.dev919
+Version: 2.0.0.dev956
 Summary: Async crawler and parsing service for data.gouv.fr
 License: MIT
 Author: Opendata Team
 Author-email: opendatateam@data.gouv.fr
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -13,15 +13,16 @@
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: aiocontextvars (>=0.2.2,<0.3.0)
 Requires-Dist: aiohttp (>=3.8.1,<4.0.0)
 Requires-Dist: asyncpg (>=0.27.0,<0.28.0)
 Requires-Dist: boto3 (>=1.21.21,<2.0.0)
 Requires-Dist: cchardet (>=2.1.7,<3.0.0)
 Requires-Dist: coloredlogs (>=15.0.1,<16.0.0)
-Requires-Dist: csv-detective (>=0.4.6,<0.5.0)
+Requires-Dist: csv-detective (>=0.4.7,<0.5.0)
+Requires-Dist: dateparser (>=1.1.7,<2.0.0)
 Requires-Dist: humanfriendly (>=10.0,<11.0)
 Requires-Dist: marshmallow (>=3.14.1,<4.0.0)
 Requires-Dist: minicli (>=0.5.0,<0.6.0)
 Requires-Dist: pandas (>=1.3.3,<2.0.0)
 Requires-Dist: progressist (>=0.1.0,<0.2.0)
 Requires-Dist: python-dateutil (>=2.8.2,<3.0.0)
 Requires-Dist: python-magic (>=0.4.25,<0.5.0)
```

