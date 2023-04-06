# Comparing `tmp/macrometa-target-collection-0.0.45.tar.gz` & `tmp/macrometa-target-collection-0.0.46.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "macrometa-target-collection-0.0.45.tar", last modified: Thu Apr  6 11:49:41 2023, max compression
+gzip compressed data, was "macrometa-target-collection-0.0.46.tar", last modified: Thu Apr  6 13:18:50 2023, max compression
```

## Comparing `macrometa-target-collection-0.0.45.tar` & `macrometa-target-collection-0.0.46.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:41.086388 macrometa-target-collection-0.0.45/
--rw-r--r--   0 runner    (1001) docker     (123)    10765 2023-04-06 11:49:11.000000 macrometa-target-collection-0.0.45/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 11:49:41.086388 macrometa-target-collection-0.0.45/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      331 2023-04-06 11:49:11.000000 macrometa-target-collection-0.0.45/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:41.086388 macrometa-target-collection-0.0.45/macrometa_target_collection/
--rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-04-06 11:49:11.000000 macrometa-target-collection-0.0.45/macrometa_target_collection/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    12890 2023-04-06 11:49:11.000000 macrometa-target-collection-0.0.45/macrometa_target_collection/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:41.086388 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 11:49:41.000000 macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1611 2023-04-06 11:49:11.000000 macrometa-target-collection-0.0.45/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 11:49:41.086388 macrometa-target-collection-0.0.45/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:18:50.541711 macrometa-target-collection-0.0.46/
+-rw-r--r--   0 runner    (1001) docker     (123)    10765 2023-04-06 13:18:24.000000 macrometa-target-collection-0.0.46/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 13:18:50.541711 macrometa-target-collection-0.0.46/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      331 2023-04-06 13:18:24.000000 macrometa-target-collection-0.0.46/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:18:50.541711 macrometa-target-collection-0.0.46/macrometa_target_collection/
+-rw-r--r--   0 runner    (1001) docker     (123)     3751 2023-04-06 13:18:24.000000 macrometa-target-collection-0.0.46/macrometa_target_collection/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    12936 2023-04-06 13:18:24.000000 macrometa-target-collection-0.0.46/macrometa_target_collection/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:18:50.541711 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    13259 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 13:18:50.000000 macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1611 2023-04-06 13:18:24.000000 macrometa-target-collection-0.0.46/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 13:18:50.541711 macrometa-target-collection-0.0.46/setup.cfg
```

### Comparing `macrometa-target-collection-0.0.45/LICENSE` & `macrometa-target-collection-0.0.46/LICENSE`

 * *Files identical despite different names*

### Comparing `macrometa-target-collection-0.0.45/PKG-INFO` & `macrometa-target-collection-0.0.46/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: macrometa-target-collection
-Version: 0.0.45
+Version: 0.0.46
 Summary: Singer.io target for writing to Macrometa GDN collections
 Author-email: Macrometa <info@macrometa.co>
 License: 
                                          Apache License
                                    Version 2.0, January 2004
                                 https://www.apache.org/licenses/
```

### Comparing `macrometa-target-collection-0.0.45/macrometa_target_collection/__init__.py` & `macrometa-target-collection-0.0.46/macrometa_target_collection/__init__.py`

 * *Files identical despite different names*

### Comparing `macrometa-target-collection-0.0.45/macrometa_target_collection/main.py` & `macrometa-target-collection-0.0.46/macrometa_target_collection/main.py`

 * *Files 2% similar despite different names*

```diff
@@ -90,26 +90,26 @@
             if type(r) is DocumentInsertError:
                 to_update.append(to_insert[i])
             else:
                 # Update ingested_documents and ingested_bytes metrics
                 ingested_documents.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
                 ingested_bytes.labels(region_label, tenant_label, fabric_label, workflow_label).inc(len(json.dumps(r)))
                 # Update ingest_lag metric
-                diff = datetime.now() - datetime.fromisoformat(to_insert[i]["time_extracted"])
+                diff = datetime.utcnow() - datetime.strptime(to_insert[i]["time_extracted"], "%Y-%m-%dT%H:%M:%S.%fZ")
                 ingest_lag.labels(region_label, tenant_label, fabric_label, workflow_label).set(diff.total_seconds())
 
         if len(to_update) > 0:
             for i, r in enumerate(collection.update_many(to_update)):
                 if type(r) is DocumentInsertError:
                     # Increment ingest_errors metric
                     ingest_errors.labels(region_label, tenant_label, fabric_label, workflow_label).inc()
                     print(f'Failed to insert/update record: {to_update[i]}. {r}')
                 else:
                     # Update ingest_lag metric
-                    diff = datetime.now() - datetime.fromisoformat(to_update[i]["time_extracted"])
+                    diff = datetime.utcnow() - datetime.strptime(to_update[i]["time_extracted"], "%Y-%m-%dT%H:%M:%S.%fZ")
                     ingest_lag.labels(region_label, tenant_label, fabric_label, workflow_label).set(diff.total_seconds())
         record_batch.last_executed_time = datetime.now()
 
 
 def try_delete(collection: StandardCollection, _key: str):
     try:
         collection.delete(_key)
```

### Comparing `macrometa-target-collection-0.0.45/macrometa_target_collection.egg-info/PKG-INFO` & `macrometa-target-collection-0.0.46/macrometa_target_collection.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: macrometa-target-collection
-Version: 0.0.45
+Version: 0.0.46
 Summary: Singer.io target for writing to Macrometa GDN collections
 Author-email: Macrometa <info@macrometa.co>
 License: 
                                          Apache License
                                    Version 2.0, January 2004
                                 https://www.apache.org/licenses/
```

### Comparing `macrometa-target-collection-0.0.45/pyproject.toml` & `macrometa-target-collection-0.0.46/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "macrometa-target-collection"
-version = "0.0.45"
+version = "0.0.46"
 authors = [
     { name = "Macrometa", email = "info@macrometa.co" },
 ]
 description = "Singer.io target for writing to Macrometa GDN collections"
 readme = "README.md"
 license = { file = "LICENSE" }
 requires-python = ">=3.7"
```

