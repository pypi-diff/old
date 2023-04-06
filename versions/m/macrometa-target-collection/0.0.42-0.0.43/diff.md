# Comparing `tmp/macrometa-target-collection-0.0.42.tar.gz` & `tmp/macrometa-target-collection-0.0.43.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "macrometa-target-collection-0.0.42.tar", last modified: Wed Apr  5 14:12:44 2023, max compression
+gzip compressed data, was "macrometa-target-collection-0.0.43.tar", last modified: Thu Apr  6 09:14:50 2023, max compression
```

## Comparing `macrometa-target-collection-0.0.42.tar` & `macrometa-target-collection-0.0.43.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 14:12:44.802046 macrometa-target-collection-0.0.42/
--rw-r--r--   0 runner    (1001) docker     (123)    10765 2023-04-05 14:12:20.000000 macrometa-target-collection-0.0.42/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-05 14:12:44.802046 macrometa-target-collection-0.0.42/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      331 2023-04-05 14:12:20.000000 macrometa-target-collection-0.0.42/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 14:12:44.802046 macrometa-target-collection-0.0.42/macrometa_target_collection/
--rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-04-05 14:12:20.000000 macrometa-target-collection-0.0.42/macrometa_target_collection/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    11512 2023-04-05 14:12:20.000000 macrometa-target-collection-0.0.42/macrometa_target_collection/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 14:12:44.802046 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-05 14:12:44.000000 macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1611 2023-04-05 14:12:20.000000 macrometa-target-collection-0.0.42/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-05 14:12:44.802046 macrometa-target-collection-0.0.42/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:50.960775 macrometa-target-collection-0.0.43/
+-rw-r--r--   0 runner    (1001) docker     (123)    10765 2023-04-06 09:14:20.000000 macrometa-target-collection-0.0.43/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 09:14:50.960775 macrometa-target-collection-0.0.43/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      331 2023-04-06 09:14:20.000000 macrometa-target-collection-0.0.43/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:50.960775 macrometa-target-collection-0.0.43/macrometa_target_collection/
+-rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-04-06 09:14:20.000000 macrometa-target-collection-0.0.43/macrometa_target_collection/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    12780 2023-04-06 09:14:20.000000 macrometa-target-collection-0.0.43/macrometa_target_collection/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:50.960775 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 09:14:50.000000 macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1611 2023-04-06 09:14:20.000000 macrometa-target-collection-0.0.43/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 09:14:50.960775 macrometa-target-collection-0.0.43/setup.cfg
```

### Comparing `macrometa-target-collection-0.0.42/LICENSE` & `macrometa-target-collection-0.0.43/LICENSE`

 * *Files identical despite different names*

### Comparing `macrometa-target-collection-0.0.42/PKG-INFO` & `macrometa-target-collection-0.0.43/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: macrometa-target-collection
-Version: 0.0.42
+Version: 0.0.43
 Summary: Singer.io target for writing to Macrometa GDN collections
 Author-email: Macrometa <info@macrometa.co>
 License: 
                                          Apache License
                                    Version 2.0, January 2004
                                 https://www.apache.org/licenses/
```

### Comparing `macrometa-target-collection-0.0.42/macrometa_target_collection/__init__.py` & `macrometa-target-collection-0.0.43/macrometa_target_collection/__init__.py`

 * *Files identical despite different names*

### Comparing `macrometa-target-collection-0.0.42/macrometa_target_collection/main.py` & `macrometa-target-collection-0.0.43/macrometa_target_collection/main.py`

 * *Files 6% similar despite different names*

```diff
@@ -3,15 +3,17 @@
 import argparse
 import asyncio
 import hashlib
 import io
 import json
 import os
 import re
+import requests
 import sys
+import time
 from asyncio import AbstractEventLoop
 from datetime import datetime
 from threading import Thread, Lock
 
 import jsonschema
 from adjust_precision_for_schema import adjust_decimal_precision_for_schema
 from c8 import C8Client, DocumentInsertError
@@ -27,19 +29,21 @@
 DEFAULT_MIN_BATCH_FLUSH_TIME_GAP = 60
 
 # Prometheus metrics
 ingested_bytes = Counter('ingested_bytes', 'Total number of bytes ingested', ['region', 'tenant', 'fabric', 'workflow'])
 ingested_documents = Counter('ingested_documents', 'Total number of documents ingested', ['region', 'tenant', 'fabric', 'workflow'])
 ingest_errors = Counter('ingest_errors', 'Total number of errors during ingestion', ['region', 'tenant', 'fabric', 'workflow'])
 ingest_lag = Gauge('ingest_lag', 'Average time lag between data changes in GDN collections and external data sources', ['region', 'tenant', 'fabric', 'workflow'])
+scrape_complete_flag = Counter("scrape_complete_flag", "Flag to check if the last scrape has been completed", ['workflow'])
 
 region_label = os.getenv("GDN_FEDERATION", "NA")
 tenant_label = os.getenv("GDN_TENANT", "NA")
 fabric_label = os.getenv("GDN_FABRIC", "NA")
 workflow_label = os.getenv("WORKFLOW_UUID", "NA")
+metric_service_url = os.getenv("METRIC_SERVICE_API")
 
 # Start the Prometheus HTTP server for exposing metrics
 start_http_server(8000)
 
 class RecordBatch:
     """Class wrapping the record batch in order to make it thread safe."""
 
@@ -85,23 +89,26 @@
         for i, r in enumerate(collection.insert_many(to_insert)):
             if type(r) is DocumentInsertError:
                 to_update.append(to_insert[i])
             else:
                 # Update ingested_documents and ingested_bytes metrics
                 ingested_documents.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
                 ingested_bytes.labels(region_label, tenant_label, fabric_label, workflow_label).inc(len(json.dumps(r)))
+                # Update ingest_lag metric
+                ingest_lag.labels(region_label, tenant_label, fabric_label, workflow_label).set((datetime.now() - to_insert[i].time_extracted).total_seconds())
 
         if len(to_update) > 0:
             for i, r in enumerate(collection.update_many(to_update)):
                 if type(r) is DocumentInsertError:
                     # Increment ingest_errors metric
                     ingest_errors.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
                     print(f'Failed to insert/update record: {to_update[i]}. {r}')
-        # Update ingest_lag metric
-        ingest_lag.labels(region_label, tenant_label, fabric_label, workflow_label).set((datetime.now() - record_batch.last_executed_time).total_seconds())
+                else:
+                    # Update ingest_lag metric
+                    ingest_lag.labels(region_label, tenant_label, fabric_label, workflow_label).set((datetime.now() - to_update[i].time_extracted).total_seconds())
         record_batch.last_executed_time = datetime.now()
 
 
 def try_delete(collection: StandardCollection, _key: str):
     try:
         collection.delete(_key)
     except Exception as e:
@@ -139,14 +146,18 @@
                 # Increment ingest_errors metric
                 ingest_errors.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
                 logger.error(f"Failed parsing the json schema for stream: {stream}.")
                 raise e
 
             try:
                 rec = o['record']
+                if o["time_extracted"]:
+                    rec["time_extracted"] = o["time_extracted"]
+                else:
+                    rec["time_extracted"] = record_batch.last_executed_time
                 try:
                     kps = key_properties.get(stream)
                     _key = None
                     # Appending _ to keys inorder for preserving values of reserved keys in source data
                     reserved_keys = ['_key', '_id', '_rev']
 
                     if kps:
@@ -205,14 +216,15 @@
             validators[stream] = Draft4Validator((o['schema']))
             key_properties[stream] = o['key_properties']
         else:
             # Increment ingest_errors metric
             ingest_errors.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
             logger.warning("Unknown message type {} in message {}".format(o['type'], o))
 
+    scrape_complete_flag.labels(workflow_label).inc()
     return state
 
 
 def setup_batch_task(collection: StandardCollection, record_batch: RecordBatch) -> AbstractEventLoop:
     event_loop = asyncio.new_event_loop()
     Thread(target=start_background_loop, args=(event_loop,), daemon=True).start()
     asyncio.run_coroutine_threadsafe(process_batch(collection, record_batch), event_loop)
@@ -249,24 +261,40 @@
     client = C8Client(
         protocol='https',
         host=region,
         port=443,
         apikey=apikey,
         geofabric=fabric
     )
+
     if not client.has_collection(target_collection):
         client.create_collection(name=target_collection)
+
     collection = client.get_collection(target_collection)
     record_batch = RecordBatch(config)
     event_loop = setup_batch_task(collection, record_batch)
     input_messages = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
     state = persist_messages(collection, input_messages, record_batch)
+
     # There can still be records in the `record_batch` which is not processed,
     # So, we have to force process it one last time before the workflow terminates.
     try_upsert(collection, record_batch, force=True)
     emit_state(state)
     event_loop.stop()
     logger.info("Exiting normally...")
 
 
+def is_scrape_complete(prometheus_url, metric_name, filter):
+    response = requests.get(f"{prometheus_url}/query", params={"query": f"{metric_name}{{{filter}}}"})
+    if response.status_code == 200:
+        json_data = response.json()
+        if json_data["data"]["result"] and len(json_data["data"]["result"]) > 0:
+            return True
+    return False
+
+
 if __name__ == '__main__':
     main()
+
+    # Wait for Prometheus to scrape the metrics
+    while not is_scrape_complete(metric_service_url, f"{scrape_complete_flag._name}_total", f"workflow=\"{workflow_label}\""):
+        time.sleep(15)
```

### Comparing `macrometa-target-collection-0.0.42/macrometa_target_collection.egg-info/PKG-INFO` & `macrometa-target-collection-0.0.43/macrometa_target_collection.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: macrometa-target-collection
-Version: 0.0.42
+Version: 0.0.43
 Summary: Singer.io target for writing to Macrometa GDN collections
 Author-email: Macrometa <info@macrometa.co>
 License: 
                                          Apache License
                                    Version 2.0, January 2004
                                 https://www.apache.org/licenses/
```

### Comparing `macrometa-target-collection-0.0.42/pyproject.toml` & `macrometa-target-collection-0.0.43/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "macrometa-target-collection"
-version = "0.0.42"
+version = "0.0.43"
 authors = [
     { name = "Macrometa", email = "info@macrometa.co" },
 ]
 description = "Singer.io target for writing to Macrometa GDN collections"
 readme = "README.md"
 license = { file = "LICENSE" }
 requires-python = ">=3.7"
```

