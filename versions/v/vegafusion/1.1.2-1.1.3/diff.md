# Comparing `tmp/vegafusion-1.1.2.tar.gz` & `tmp/vegafusion-1.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vegafusion-1.1.2.tar", last modified: Thu Mar 30 18:34:14 2023, max compression
+gzip compressed data, was "vegafusion-1.1.3.tar", last modified: Thu Apr  6 18:12:40 2023, max compression
```

## Comparing `vegafusion-1.1.2.tar` & `vegafusion-1.1.3.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 18:34:14.456246 vegafusion-1.1.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1503 2023-03-30 18:32:55.000000 vegafusion-1.1.2/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-03-30 18:34:14.456246 vegafusion-1.1.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      525 2023-03-30 18:32:55.000000 vegafusion-1.1.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-30 18:32:55.000000 vegafusion-1.1.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      987 2023-03-30 18:34:14.456246 vegafusion-1.1.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-30 18:32:55.000000 vegafusion-1.1.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 18:34:14.452246 vegafusion-1.1.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_conext_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    18632 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_input_utc.py
--rw-r--r--   0 runner    (1001) docker     (123)    31525 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_pretransform.py
--rw-r--r--   0 runner    (1001) docker     (123)     3854 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_pretransform_specs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1023 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_row_limit.py
--rw-r--r--   0 runner    (1001) docker     (123)     7874 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_transformed_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     2843 2023-03-30 18:32:55.000000 vegafusion-1.1.2/tests/test_transformer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 18:34:14.456246 vegafusion-1.1.2/vegafusion/
--rw-r--r--   0 runner    (1001) docker     (123)     4014 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      762 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/compilers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 18:34:14.456246 vegafusion-1.1.2/vegafusion/connection/
--rw-r--r--   0 runner    (1001) docker     (123)     4797 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/connection/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8164 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/connection/duckdb.py
--rw-r--r--   0 runner    (1001) docker     (123)      350 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/embed.py
--rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/evaluation.py
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/jupyter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/local_tz.py
--rw-r--r--   0 runner    (1001) docker     (123)     2332 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/renderer.py
--rw-r--r--   0 runner    (1001) docker     (123)    20434 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)     8485 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-03-30 18:32:55.000000 vegafusion-1.1.2/vegafusion/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 18:34:14.456246 vegafusion-1.1.2/vegafusion.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-03-30 18:34:14.000000 vegafusion-1.1.2/vegafusion.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      735 2023-03-30 18:34:14.000000 vegafusion-1.1.2/vegafusion.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 18:34:14.000000 vegafusion-1.1.2/vegafusion.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-30 18:34:14.000000 vegafusion-1.1.2/vegafusion.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-30 18:34:14.000000 vegafusion-1.1.2/vegafusion.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:40.993816 vegafusion-1.1.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1503 2023-04-06 18:11:41.000000 vegafusion-1.1.3/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-04-06 18:12:40.993816 vegafusion-1.1.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-04-06 18:11:41.000000 vegafusion-1.1.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-06 18:11:41.000000 vegafusion-1.1.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      987 2023-04-06 18:12:40.993816 vegafusion-1.1.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:11:41.000000 vegafusion-1.1.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:40.989815 vegafusion-1.1.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_conext_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18632 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_input_utc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31525 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_pretransform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_pretransform_specs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1023 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_row_limit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7874 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_transformed_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2843 2023-04-06 18:11:41.000000 vegafusion-1.1.3/tests/test_transformer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:40.993816 vegafusion-1.1.3/vegafusion/
+-rw-r--r--   0 runner    (1001) docker     (123)     4014 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      762 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/compilers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:40.993816 vegafusion-1.1.3/vegafusion/connection/
+-rw-r--r--   0 runner    (1001) docker     (123)     4797 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/connection/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8344 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/connection/duckdb.py
+-rw-r--r--   0 runner    (1001) docker     (123)      350 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/embed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/evaluation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/jupyter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1318 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/local_tz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2332 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/renderer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20434 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8485 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-06 18:11:41.000000 vegafusion-1.1.3/vegafusion/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:40.993816 vegafusion-1.1.3/vegafusion.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-04-06 18:12:40.000000 vegafusion-1.1.3/vegafusion.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      735 2023-04-06 18:12:40.000000 vegafusion-1.1.3/vegafusion.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:12:40.000000 vegafusion-1.1.3/vegafusion.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 18:12:40.000000 vegafusion-1.1.3/vegafusion.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 18:12:40.000000 vegafusion-1.1.3/vegafusion.egg-info/top_level.txt
```

### Comparing `vegafusion-1.1.2/LICENSE.txt` & `vegafusion-1.1.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/PKG-INFO` & `vegafusion-1.1.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vegafusion
-Version: 1.1.2
+Version: 1.1.3
 Summary: Core tools for using VegaFusion from Python
 License: BSD-3-Clause
 Keywords: vega,altair,vegafusion,arrow
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `vegafusion-1.1.2/README.md` & `vegafusion-1.1.3/README.md`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/setup.cfg` & `vegafusion-1.1.3/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [bdist_wheel]
 universal = 0
 
 [metadata]
 name = vegafusion
 description = Core tools for using VegaFusion from Python
-version = 1.1.2
+version = 1.1.3
 long_description = file: README.md
 long_description_content_type = text/markdown
 keywords = vega, altair, vegafusion, arrow
 license = BSD-3-Clause
 license_file = LICENSE.txt
 python = "^3.7"
 homepage = "https://vegafusion.io"
@@ -30,14 +30,14 @@
 	altair>=4.2.0
 	pyarrow>=5
 	pandas
 	psutil
 
 [options.extras_require]
 embed = 
-	vegafusion-python-embed==1.1.2
+	vegafusion-python-embed==1.1.3
 	vl-convert-python>=0.7.0
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `vegafusion-1.1.2/tests/test_conext_manager.py` & `vegafusion-1.1.3/tests/test_conext_manager.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/tests/test_input_utc.py` & `vegafusion-1.1.3/tests/test_input_utc.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/tests/test_pretransform.py` & `vegafusion-1.1.3/tests/test_pretransform.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/tests/test_pretransform_specs.py` & `vegafusion-1.1.3/tests/test_pretransform_specs.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,19 @@
 
 
 def load_test_cases():
     cases = []
     for category in ["vegalite", "custom"]:
         category_dir = spec_dir / category
         for file in category_dir.glob("*.vg.json"):
-            cases.append((category, file.name))
+            if file.name not in [
+                # Undefined aggregate column
+                "trellis_area_seattle.vg.json"
+            ]:
+                cases.append((category, file.name))
 
     return cases
 
 
 def maybe_skip(category, name):
     if (category, name) in [
         ("vegalite", "window_cumulative_running_average.vg.json"),
```

### Comparing `vegafusion-1.1.2/tests/test_row_limit.py` & `vegafusion-1.1.3/tests/test_row_limit.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/tests/test_transformed_data.py` & `vegafusion-1.1.3/tests/test_transformed_data.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/tests/test_transformer.py` & `vegafusion-1.1.3/tests/test_transformer.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/__init__.py` & `vegafusion-1.1.3/vegafusion/__init__.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/compilers.py` & `vegafusion-1.1.3/vegafusion/compilers.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/connection/__init__.py` & `vegafusion-1.1.3/vegafusion/connection/__init__.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/connection/duckdb.py` & `vegafusion-1.1.3/vegafusion/connection/duckdb.py`

 * *Files 2% similar despite different names*

```diff
@@ -49,18 +49,23 @@
     elif duckdb_type == "TIMESTAMP WITH TIME ZONE":
         return pa.timestamp("ms", tz="UTC")
     else:
         raise ValueError(f"Unexpected DuckDB type: {duckdb_type}")
 
 
 def duckdb_relation_to_schema(rel: duckdb.DuckDBPyRelation) -> pa.Schema:
-    return pa.schema({
-        col: duckdb_type_name_to_pyarrow_type(type_name)
-        for col, type_name in zip(rel.columns, rel.dtypes)
-    })
+    schema_fields = {}
+    for col, type_name in zip(rel.columns, rel.dtypes):
+        try:
+            type_ = duckdb_type_name_to_pyarrow_type(type_name)
+            schema_fields[col] = type_
+        except ValueError:
+            # Skip columns with unrecognized types
+            pass
+    return pa.schema(schema_fields)
 
 
 class DuckDbConnection(SqlConnection):
     def __init__(self, connection: duckdb.DuckDBPyConnection = None, fallback: bool = True, verbose: bool = False):
         # Validate duckdb version
         if LooseVersion(duckdb.__version__) < LooseVersion("0.7.0"):
             raise ImportError(
```

### Comparing `vegafusion-1.1.2/vegafusion/evaluation.py` & `vegafusion-1.1.3/vegafusion/evaluation.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/local_tz.py` & `vegafusion-1.1.3/vegafusion/local_tz.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/renderer.py` & `vegafusion-1.1.3/vegafusion/renderer.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/runtime.py` & `vegafusion-1.1.3/vegafusion/runtime.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/transformer.py` & `vegafusion-1.1.3/vegafusion/transformer.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion/utils.py` & `vegafusion-1.1.3/vegafusion/utils.py`

 * *Files identical despite different names*

### Comparing `vegafusion-1.1.2/vegafusion.egg-info/PKG-INFO` & `vegafusion-1.1.3/vegafusion.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vegafusion
-Version: 1.1.2
+Version: 1.1.3
 Summary: Core tools for using VegaFusion from Python
 License: BSD-3-Clause
 Keywords: vega,altair,vegafusion,arrow
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `vegafusion-1.1.2/vegafusion.egg-info/SOURCES.txt` & `vegafusion-1.1.3/vegafusion.egg-info/SOURCES.txt`

 * *Files identical despite different names*

