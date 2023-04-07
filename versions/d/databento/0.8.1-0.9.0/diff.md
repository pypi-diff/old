# Comparing `tmp/databento-0.8.1.tar.gz` & `tmp/databento-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "databento-0.8.1.tar", last modified: Mon Mar  6 05:11:57 2023, max compression
+gzip compressed data, was "databento-0.9.0.tar", last modified: Fri Mar 10 22:45:15 2023, max compression
```

## Comparing `databento-0.8.1.tar` & `databento-0.9.0.tar`

### file list

```diff
@@ -1,57 +1,57 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.086058 databento-0.8.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-03-06 05:11:33.000000 databento-0.8.1/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (123)     9694 2023-03-06 05:11:33.000000 databento-0.8.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-06 05:11:33.000000 databento-0.8.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-03-06 05:11:57.086058 databento-0.8.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4970 2023-03-06 05:11:33.000000 databento-0.8.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.074058 databento-0.8.1/databento/
--rw-r--r--   0 runner    (1001) docker     (123)     1151 2023-03-06 05:11:33.000000 databento-0.8.1/databento/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.078058 databento-0.8.1/databento/common/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25104 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/bento.py
--rw-r--r--   0 runner    (1001) docker     (123)     8447 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/data.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/deprecated.py
--rw-r--r--   0 runner    (1001) docker     (123)     6403 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)      996 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     5676 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/parsing.py
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/symbology.py
--rw-r--r--   0 runner    (1001) docker     (123)     4082 2023-03-06 05:11:33.000000 databento-0.8.1/databento/common/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.082058 databento-0.8.1/databento/historical/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.082058 databento-0.8.1/databento/historical/api/
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16968 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/api/batch.py
--rw-r--r--   0 runner    (1001) docker     (123)    17607 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/api/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2895 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/api/symbology.py
--rw-r--r--   0 runner    (1001) docker     (123)    13336 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/api/timeseries.py
--rw-r--r--   0 runner    (1001) docker     (123)     2366 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/error.py
--rw-r--r--   0 runner    (1001) docker     (123)     6337 2023-03-06 05:11:33.000000 databento-0.8.1/databento/historical/http.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.082058 databento-0.8.1/databento/live/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:33.000000 databento-0.8.1/databento/live/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-06 05:11:33.000000 databento-0.8.1/databento/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.078058 databento-0.8.1/databento.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-06 05:11:57.000000 databento-0.8.1/databento.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-06 05:11:57.086058 databento-0.8.1/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)     2245 2023-03-06 05:11:33.000000 databento-0.8.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.086058 databento-0.8.1/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:57.086058 databento-0.8.1/tests/data/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 05:11:33.000000 databento-0.8.1/tests/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      963 2023-03-06 05:11:33.000000 databento-0.8.1/tests/data/generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_bento_compression.py
--rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_bento_data_source.py
--rw-r--r--   0 runner    (1001) docker     (123)     4104 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_common_enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     6938 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_common_parsing.py
--rw-r--r--   0 runner    (1001) docker     (123)     3660 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_common_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)     6600 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)    21555 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_bento.py
--rw-r--r--   0 runner    (1001) docker     (123)     5845 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_client.py
--rw-r--r--   0 runner    (1001) docker     (123)      990 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_error.py
--rw-r--r--   0 runner    (1001) docker     (123)    13215 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-03-06 05:11:33.000000 databento-0.8.1/tests/test_historical_timeseries.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.558521 databento-0.9.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1694 2023-03-10 22:44:50.000000 databento-0.9.0/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (123)     9694 2023-03-10 22:44:50.000000 databento-0.9.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-10 22:44:50.000000 databento-0.9.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-03-10 22:45:15.558521 databento-0.9.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4970 2023-03-10 22:44:50.000000 databento-0.9.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.554521 databento-0.9.0/databento/
+-rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-03-10 22:44:50.000000 databento-0.9.0/databento/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.554521 databento-0.9.0/databento/common/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24977 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/bento.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8553 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/deprecated.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6403 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)      996 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5676 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/parsing.py
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/symbology.py
+-rw-r--r--   0 runner    (1001) docker     (123)      907 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/utility.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4948 2023-03-10 22:44:50.000000 databento-0.9.0/databento/common/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.554521 databento-0.9.0/databento/historical/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.558521 databento-0.9.0/databento/historical/api/
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18523 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/api/batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18749 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/api/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2958 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/api/symbology.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13452 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/api/timeseries.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2379 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6337 2023-03-10 22:44:50.000000 databento-0.9.0/databento/historical/http.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.558521 databento-0.9.0/databento/live/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 22:44:50.000000 databento-0.9.0/databento/live/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-10 22:44:50.000000 databento-0.9.0/databento/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.554521 databento-0.9.0/databento.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6238 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-10 22:45:15.000000 databento-0.9.0/databento.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-10 22:45:15.558521 databento-0.9.0/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2245 2023-03-10 22:44:50.000000 databento-0.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.558521 databento-0.9.0/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-10 22:45:15.558521 databento-0.9.0/tests/data/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-10 22:44:50.000000 databento-0.9.0/tests/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      963 2023-03-10 22:44:50.000000 databento-0.9.0/tests/data/generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_bento_compression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1236 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_bento_data_source.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4104 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_common_enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6938 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_common_parsing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4434 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_common_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6733 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23067 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_bento.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5845 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      990 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14220 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5210 2023-03-10 22:44:50.000000 databento-0.9.0/tests/test_historical_timeseries.py
```

### Comparing `databento-0.8.1/CHANGELOG.md` & `databento-0.9.0/CHANGELOG.md`

 * *Files 14% similar despite different names*

```diff
@@ -1,9 +1,15 @@
 # Changelog
 
+## 0.8.2 - 2023-03-10
+- Removed `record_count` property from Bento class
+- Fixed bug in `Bento` where invalid metadata would prevent iteration
+- Improved use of the logging module
+- Changed `metadata.get_dataset_condition` response to a list of condition per date
+
 ## 0.8.1 - 2023-03-05
 - Fixed bug in `Bento` iteration where multiple readers were created
 - Added `from_dbn` convenience alias for loading DBN files
 
 ## 0.8.0 - 2023-03-03
 - Integrated DBN encoding `0.3.2`
 - Renamed `timeseries.stream` to `timeseries.get_range`
```

### Comparing `databento-0.8.1/LICENSE` & `databento-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/PKG-INFO` & `databento-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: databento
-Version: 0.8.1
+Version: 0.9.0
 Summary: Official Python client library for Databento
 Home-page: https://github.com/databento/databento-python
 Author: Databento
 Author-email: support@databento.com
 License: Apache License 2.0
 Project-URL: Bug Tracker, https://github.com/databento/databento-python/issues
 Project-URL: Documentation, https://docs.databento.com/
```

### Comparing `databento-0.8.1/README.md` & `databento-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/common/bento.py` & `databento-0.9.0/databento/common/bento.py`

 * *Files 1% similar despite different names*

```diff
@@ -265,16 +265,14 @@
         The metadata for the data.
     nbytes : int
         The size of the data in bytes.
     raw : bytes
         The raw compressed data in bytes.
     reader : IO[bytes]
         A zstd decompression stream.
-    record_count : int
-        The record count.
     schema : Schema
         The data record schema.
     start : pd.Timestamp
         The query start for the data.
     record_size : int
         The binary record size in bytes.
     stype_in : SType
@@ -343,18 +341,25 @@
         self._product_id_index: Dict[
             dt.date,
             Dict[int, str],
         ] = {}
 
     def __iter__(self) -> Generator[np.void, None, None]:
         reader = self.reader
-        for _ in range(self.record_count):
+        while True:
             raw = reader.read(self.record_size)
-            rec = np.frombuffer(raw, dtype=STRUCT_MAP[self.schema])
-            yield rec[0]
+            if raw:
+                rec = np.frombuffer(raw, dtype=STRUCT_MAP[self.schema])
+                yield rec[0]
+            else:
+                break
+
+    def __repr__(self) -> str:
+        name = self.__class__.__name__
+        return f"<{name}(schema={self.schema})>"
 
     def _apply_pretty_ts(self, df: pd.DataFrame) -> pd.DataFrame:
         df.index = pd.to_datetime(df.index, utc=True)
         for column in df.columns:
             if column.startswith("ts_") and "delta" not in column:
                 df[column] = pd.to_datetime(df[column], utc=True)
 
@@ -408,30 +413,28 @@
                 if not date_map:
                     product_id_index[d] = date_map
                 date_map[interval.product_id] = interval.native
 
         return product_id_index
 
     def _prepare_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
+        # Setup column ordering and index
         df.set_index(self._get_index_column(), inplace=True)
-        df.drop(["length", "rtype"], axis=1, inplace=True)
+        df = df.reindex(columns=COLUMNS[self.schema])
+
         if self.schema == Schema.MBO or self.schema in DERIV_SCHEMAS:
             df["flags"] = df["flags"] & 0xFF  # Apply bitmask
             df["side"] = df["side"].str.decode("utf-8")
             df["action"] = df["action"].str.decode("utf-8")
         elif self.schema == Schema.DEFINITION:
             for column in DEFINITION_CHARARRAY_COLUMNS:
                 df[column] = df[column].str.decode("utf-8")
             for column, type_max in DEFINITION_TYPE_MAX_MAP.items():
                 if column in df.columns:
                     df[column] = df[column].where(df[column] != type_max, np.nan)
-
-        # Reorder columns
-        df = df.reindex(columns=COLUMNS[self.schema])
-
         return df
 
     def _get_index_column(self) -> str:
         return (
             "ts_event"
             if self.schema
             in (
@@ -600,26 +603,14 @@
             reader = self._data_source.reader
 
         # Seek past the metadata to read records
         reader.seek(self._metadata_length)
         return reader
 
     @property
-    def record_count(self) -> int:
-        """
-        Return the record count.
-
-        Returns
-        -------
-        int
-
-        """
-        return self._metadata["record_count"]
-
-    @property
     def schema(self) -> Schema:
         """
         Return the data record schema.
 
         Returns
         -------
         Schema
```

### Comparing `databento-0.8.1/databento/common/data.py` & `databento-0.9.0/databento/common/data.py`

 * *Files 0% similar despite different names*

```diff
@@ -262,14 +262,17 @@
 ]
 
 STATUS_COLUMNS = [x for x in np.dtype(STATUS_MSG).names or ()]
 STATUS_COLUMNS.remove("ts_recv")  # Index
 
 DEFINITION_COLUMNS = [x for x in np.dtype(DEFINITION_MSG).names or ()]
 DEFINITION_COLUMNS.remove("ts_recv")  # Index
+DEFINITION_COLUMNS.remove("length")
+DEFINITION_COLUMNS.remove("rtype")
+DEFINITION_COLUMNS.remove("dummy")
 
 
 COLUMNS = {
     Schema.MBO: [
         "ts_event",
         "ts_in_delta",
         "publisher_id",
```

### Comparing `databento-0.8.1/databento/common/enums.py` & `databento-0.9.0/databento/common/enums.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/common/metadata.py` & `databento-0.9.0/databento/common/metadata.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/common/parsing.py` & `databento-0.9.0/databento/common/parsing.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/common/symbology.py` & `databento-0.9.0/databento/common/symbology.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/common/validation.py` & `databento-0.9.0/databento/common/validation.py`

 * *Files 11% similar despite different names*

```diff
@@ -139,14 +139,44 @@
     if url_chunks.netloc:
         return urlunsplit(
             components=("https", url_chunks.netloc, url_chunks.path, "", ""),
         )
     return urlunsplit(components=("https", url_chunks.path, "", "", ""))
 
 
+def validate_semantic_string(value: str, param: str) -> str:
+    """
+    Validate whether a string contains a semantic value.
+    A string is considered absent of meaning if:
+        - It is empty.
+        - It contains only whitespace.
+        - It contains unprintable characters.
+
+    Parameters
+    ----------
+    value: str
+        The string to validate.
+    param : str
+        The name of the parameter being validated (for any error message).
+
+    Raises
+    ------
+    ValueError
+        If the string is not meaningful.
+
+    """
+    if not value:
+        raise ValueError(f"The `{param}` cannot be an empty string.")
+    if str.isspace(value):
+        raise ValueError(f"The `{param}` cannot contain only whitepsace.")
+    if not str.isprintable(value):
+        raise ValueError(f"The `{param}` cannot contain unprintable characters.")
+    return value
+
+
 def validate_smart_symbol(symbol: str) -> str:
     """
     Validate whether symbol has a valid smart symbol format.
 
     Parameters
     ----------
     symbol: str
```

### Comparing `databento-0.8.1/databento/historical/api/batch.py` & `databento-0.9.0/databento/historical/api/batch.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from __future__ import annotations
 
+import logging
 import os
 from datetime import date
 from os import PathLike
 from pathlib import Path
 from typing import Any, Dict, List, Optional, Tuple, Union
 
 import aiohttp
@@ -15,31 +16,37 @@
     Delivery,
     Encoding,
     Packaging,
     Schema,
     SplitDuration,
     SType,
 )
-from databento.common.logging import log_error, log_info
 from databento.common.parsing import (
     datetime_to_string,
     optional_datetime_to_string,
     optional_symbols_list_to_string,
     optional_values_list_to_string,
 )
-from databento.common.validation import validate_enum, validate_path
+from databento.common.validation import (
+    validate_enum,
+    validate_path,
+    validate_semantic_string,
+)
 from databento.historical.api import API_VERSION
 from databento.historical.http import (
     BentoHttpAPI,
     check_http_error,
     check_http_error_async,
 )
 from requests.auth import HTTPBasicAuth
 
 
+logger = logging.getLogger(__name__)
+
+
 class BatchHttpAPI(BentoHttpAPI):
     """
     Provides request methods for the batch HTTP API endpoints.
     """
 
     def __init__(self, key: str, gateway: str) -> None:
         super().__init__(key=key, gateway=gateway)
@@ -70,19 +77,19 @@
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code (string identifier) for the request.
         start : pd.Timestamp or date or str or int
             The start datetime of the request time range (inclusive).
             Assumes UTC as timezone unless passed a tz-aware object.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int
             The end datetime of the request time range (exclusive).
             Assumes UTC as timezone unless passed a tz-aware object.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         symbols : List[Union[str, int]] or str
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If more than 1 symbol is specified, the data is merged and sorted by time.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
         encoding : Encoding or str {'dbn', 'csv', 'json'}, default 'dbn'
@@ -114,15 +121,15 @@
         --------
         Calling this method will incur a cost.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start", datetime_to_string(start)),
             ("end", datetime_to_string(end)),
             ("symbols", str(symbols_list)),
             ("schema", str(validate_enum(schema, Schema, "schema"))),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(validate_enum(stype_out, SType, "stype_out"))),
             ("encoding", str(validate_enum(encoding, Encoding, "encoding"))),
@@ -222,15 +229,15 @@
 
     def download(
         self,
         output_dir: Union[PathLike[str], str],
         job_id: str,
         filename_to_download: Optional[str] = None,
         enable_partial_downloads: bool = True,
-    ) -> None:
+    ) -> List[Path]:
         """
         Download a batch job or a specific file to `{output_dir}/{job_id}/`.
 
         Will automatically generate any necessary directories if they do not
         already exist.
 
         Makes one or many `GET /batch/download/{job_id}/{filename}` HTTP request(s).
@@ -243,14 +250,26 @@
             The batch job identifier.
         filename_to_download : str, optional
             The specific file to download.
             If `None` then will download all files for the batch job.
         enable_partial_downloads : bool, default True
             If partially downloaded files will be resumed using range request(s).
 
+        Returns
+        -------
+        List[Path]
+            A list of paths to the downloaded files.
+
+        Raises
+        ------
+        RuntimeError
+            When no files were found for the batch job.
+        ValueError
+            When a file fails to download.
+
         """
         output_dir = validate_path(output_dir, "output_dir")
         self._check_api_key()
 
         params: List[Tuple[str, Optional[str]]] = [
             ("job_id", job_id),
         ]
@@ -258,42 +277,47 @@
         job_files: List[Dict[str, Any]] = self._get(
             url=self._base_url + ".list_files",
             params=params,
             basic_auth=True,
         ).json()
 
         if not job_files:
-            log_error(f"Cannot download batch job {job_id} (no files found).")
-            return
+            logger.error("Cannot download batch job %s (no files found).", job_id)
+            raise RuntimeError(f"no files for batch job {job_id}")
 
         if filename_to_download:
             # A specific file is being requested
             is_file_found = False
             for details in job_files:
                 if details["filename"] == filename_to_download:
                     # Reduce files to download only the single file
                     job_files = [details]
                     is_file_found = True
                     break
             if not is_file_found:
-                log_error(
-                    f"Cannot download batch job {job_id} file "
-                    f"({filename_to_download} not found)",
+                logger.error(
+                    "Cannot download batch job %s file (%s not found)",
+                    job_id,
+                    filename_to_download,
+                )
+                raise ValueError(
+                    f"{filename_to_download} is not a file for batch job {job_id}",
                 )
-                return
 
         # Prepare job directory
         job_dir = Path(output_dir) / job_id
         os.makedirs(job_dir, exist_ok=True)
 
+        file_paths = []
         for details in job_files:
             filename = str(details["filename"])
             output_path = job_dir / filename
-            log_info(
-                f"Downloading batch job file to {output_path} ...",
+            logger.info(
+                "Downloading batch job file to %s ...",
+                output_path,
             )
 
             urls = details.get("urls")
             if not urls:
                 raise ValueError(
                     f"Cannot download {filename}, URLs were not found in manifest.",
                 )
@@ -307,14 +331,17 @@
 
             self._download_file(
                 url=https_url,
                 filesize=int(details["size"]),
                 output_path=output_path,
                 enable_partial_downloads=enable_partial_downloads,
             )
+            file_paths.append(output_path)
+
+        return file_paths
 
     def _download_file(
         self,
         url: str,
         filesize: int,
         output_path: Path,
         enable_partial_downloads: bool,
@@ -330,25 +357,27 @@
             headers=headers,
             auth=HTTPBasicAuth(username=self._key, password=""),
             allow_redirects=True,
             stream=True,
         ) as response:
             check_http_error(response)
 
+            logger.debug("Starting download of file %s", output_path.name)
             with open(output_path, mode=mode) as f:
                 for chunk in response.iter_content():
                     f.write(chunk)
+            logger.debug("Download of %s completed", output_path.name)
 
     async def download_async(
         self,
         output_dir: Union[PathLike[str], str],
         job_id: str,
         filename_to_download: Optional[str] = None,
         enable_partial_downloads: bool = True,
-    ) -> None:
+    ) -> List[Path]:
         """
         Asynchronously download a batch job or a specific file to
         `{output_dir}/{job_id}/`.
 
         Will automatically generate any necessary directories if they do not
         already exist.
 
@@ -362,14 +391,26 @@
             The batch job identifier.
         filename_to_download : str, optional
             The specific file to download.
             If `None` then will download all files for the batch job.
         enable_partial_downloads : bool, default True
             If partially downloaded files will be resumed using range request(s).
 
+        Returns
+        -------
+        List[Path]
+            A list of paths to the downloaded files.
+
+        Raises
+        ------
+        RuntimeError
+            When no files were found for the batch job.
+        ValueError
+            When a file fails to download.
+
         """
         output_dir = validate_path(output_dir, "output_dir")
         self._check_api_key()
 
         params: List[Tuple[str, Optional[str]]] = [
             ("job_id", job_id),
         ]
@@ -377,42 +418,47 @@
         job_files: List[Dict[str, Any]] = await self._get_json_async(
             url=self._base_url + ".list_files",
             params=params,
             basic_auth=True,
         )
 
         if not job_files:
-            log_error(f"Cannot download batch job {job_id} (no files found).")
-            return
+            logger.error("Cannot download batch job %s (no files found).", job_id)
+            raise RuntimeError(f"no files for batch job {job_id}")
 
         if filename_to_download:
             # A specific file is being requested
             is_file_found = False
             for details in job_files:
                 if details["filename"] == filename_to_download:
                     # Reduce files to download only the single file
                     job_files = [details]
                     is_file_found = True
                     break
             if not is_file_found:
-                log_error(
-                    f"Cannot download batch job {job_id} file "
-                    f"({filename_to_download} not found)",
+                logger.error(
+                    "Cannot download batch job %s file (%s not found)",
+                    job_id,
+                    filename_to_download,
+                )
+                raise ValueError(
+                    f"{filename_to_download} is not a file for batch job {job_id}",
                 )
-                return
 
         # Prepare job directory
         job_dir = Path(output_dir) / job_id
         os.makedirs(job_dir, exist_ok=True)
 
+        file_paths = []
         for details in job_files:
             filename = str(details["filename"])
             output_path = job_dir / filename
-            log_info(
-                f"Downloading batch job file to {output_path} ...",
+            logger.info(
+                "Downloading batch job file to %s ...",
+                output_path,
             )
 
             urls = details.get("urls")
             if not urls:
                 raise ValueError(
                     f"Cannot download {filename}, URLs were not found in manifest.",
                 )
@@ -426,14 +472,17 @@
 
             await self._download_file_async(
                 url=https_url,
                 filesize=int(details["size"]),
                 output_path=output_path,
                 enable_partial_downloads=enable_partial_downloads,
             )
+            file_paths.append(output_path)
+
+        return file_paths
 
     async def _download_file_async(
         self,
         url: str,
         filesize: int,
         output_path: Path,
         enable_partial_downloads: bool,
@@ -449,18 +498,20 @@
                 url=url,
                 headers=headers,
                 auth=aiohttp.BasicAuth(login=self._key, password="", encoding="utf-8"),
                 timeout=self.TIMEOUT,
             ) as response:
                 await check_http_error_async(response)
 
+                logger.debug("Starting async download of file %s", output_path.name)
                 with open(output_path, mode=mode) as f:
                     async for chunk in response.content.iter_chunks():
                         data: bytes = chunk[0]
                         f.write(data)
+                logger.debug("Download of %s completed", output_path.name)
 
     def _get_file_download_headers_and_mode(
         self,
         filesize: int,
         output_path: Path,
         enable_partial_downloads: bool,
     ) -> Tuple[Dict[str, str], str]:
```

### Comparing `databento-0.8.1/databento/historical/api/metadata.py` & `databento-0.9.0/databento/historical/api/metadata.py`

 * *Files 10% similar despite different names*

```diff
@@ -5,15 +5,19 @@
 from databento.common.enums import Dataset, Encoding, FeedMode, Schema, SType
 from databento.common.parsing import (
     datetime_to_string,
     optional_date_to_string,
     optional_datetime_to_string,
     optional_symbols_list_to_string,
 )
-from databento.common.validation import validate_enum, validate_maybe_enum
+from databento.common.validation import (
+    validate_enum,
+    validate_maybe_enum,
+    validate_semantic_string,
+)
 from databento.historical.api import API_VERSION
 from databento.historical.http import BentoHttpAPI
 from requests import Response
 
 
 class MetadataHttpAPI(BentoHttpAPI):
     """
@@ -80,41 +84,41 @@
             params=params,
             basic_auth=True,
         )
         return response.json()
 
     def list_schemas(
         self,
-        dataset: Optional[Union[Dataset, str]] = None,
+        dataset: Union[Dataset, str],
         start_date: Optional[Union[date, str]] = None,
         end_date: Optional[Union[date, str]] = None,
     ) -> List[str]:
         """
         Request all available data schemas from Databento.
 
         Makes a `GET /metadata.list_schemas` HTTP request.
 
         Parameters
         ----------
-        dataset : Dataset or str, optional
+        dataset : Dataset or str
             The dataset code (string identifier) for the request.
         start_date : date or str, optional
             The start date (UTC) for the request range.
             If `None` then first date available.
         end_date : date or str, optional
             The end date (UTC) for the request range.
             If `None` then last date available.
 
         Returns
         -------
         List[str]
 
         """
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start_date", optional_date_to_string(start_date)),
             ("end_date", optional_date_to_string(end_date)),
         ]
 
         response: Response = self._get(
             url=self._base_url + ".list_schemas",
             params=params,
@@ -148,15 +152,15 @@
         Returns
         -------
         Dict[str, Dict[str, str]]
             A mapping of dataset to encoding to schema to field to data type.
 
         """
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("schema", validate_maybe_enum(schema, Schema, "schema")),
             ("encoding", validate_maybe_enum(encoding, Encoding, "encoding")),
         ]
 
         response: Response = self._get(
             url=self._base_url + ".list_fields",
             params=params,
@@ -222,34 +226,34 @@
         -------
         float or Dict[str, Any]
             If both `mode` and `schema` are specified, the unit price is returned as a single number.
             Otherwise, return a map of feed mode to schema to unit price.
 
         """
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("mode", validate_maybe_enum(mode, FeedMode, "mode")),
             ("schema", validate_maybe_enum(schema, Schema, "schema")),
         ]
 
         response: Response = self._get(
             url=self._base_url + ".list_unit_prices",
             params=params,
             basic_auth=True,
         )
         return response.json()
 
     def get_dataset_condition(
         self,
         dataset: Union[Dataset, str],
-        start_date: Union[date, str] = None,
-        end_date: Union[date, str] = None,
+        start_date: Optional[Union[date, str]] = None,
+        end_date: Optional[Union[date, str]] = None,
     ) -> Dict[str, Any]:
         """
-        Get the dataset condition from Databento.
+        Get the per date dataset conditions from Databento.
 
         Makes a `GET /metadata.get_dataset_condition` HTTP request.
 
         Use this method to discover data availability and quality.
 
         Parameters
         ----------
@@ -264,26 +268,58 @@
 
         Returns
         -------
         Dict[str, Any]
 
         """
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start_date", optional_date_to_string(start_date)),
             ("end_date", optional_date_to_string(end_date)),
         ]
 
         response: Response = self._get(
             url=self._base_url + ".get_dataset_condition",
             params=params,
             basic_auth=True,
         )
         return response.json()
 
+    def get_dataset_range(
+        self,
+        dataset: Union[Dataset, str],
+    ) -> Dict[str, str]:
+        """
+        Request the available range for the dataset from Databento.
+
+        Makes a GET `/metadata.get_dataset_range` HTTP request.
+
+        Parameters
+        ----------
+        dataset : Dataset or str
+            The dataset code for the request.
+
+        Returns
+        -------
+        Dict[str, str]
+            The available range for the dataset.
+
+        """
+        params: List[Tuple[str, Optional[str]]] = [
+            ("dataset", validate_semantic_string(dataset, "dataset")),
+        ]
+
+        response: Response = self._get(
+            url=self._base_url + ".get_dataset_range",
+            params=params,
+            basic_auth=True,
+        )
+
+        return response.json()
+
     def get_record_count(
         self,
         dataset: Union[Dataset, str],
         start: Union[pd.Timestamp, date, str, int],
         end: Union[pd.Timestamp, date, str, int],
         symbols: Optional[Union[List[str], str]] = None,
         schema: Union[Schema, str] = "trades",
@@ -297,18 +333,18 @@
 
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code for the request.
         start : pd.Timestamp or date or str or int
             The start datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int
             The end datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         symbols : List[Union[str, int]] or str, optional
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
         stype_in : SType or str, default 'native'
             The input symbology type to resolve from.
@@ -320,15 +356,15 @@
         int
             The count of records.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("symbols", symbols_list),
             ("schema", str(validate_enum(schema, Schema, "schema"))),
             ("start", optional_datetime_to_string(start)),
             ("end", optional_datetime_to_string(end)),
             ("stype_in", str(stype_in_valid)),
         ]
 
@@ -362,18 +398,18 @@
 
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code for the request.
         start : pd.Timestamp or date or str or int, optional
             The start datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int, optional
             The end datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         symbols : List[Union[str, int]] or str, optional
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
         stype_in : SType or str, default 'native'
             The input symbology type to resolve from.
@@ -385,15 +421,15 @@
         int
             The size in number of bytes used for billing.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start", datetime_to_string(start)),
             ("end", datetime_to_string(end)),
             ("symbols", symbols_list),
             ("schema", str(validate_enum(schema, Schema, "schema"))),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(SType.PRODUCT_ID)),
         ]
@@ -428,18 +464,18 @@
 
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code for the request.
         start : pd.Timestamp or date or str or int
             The start datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int
             The end datetime for the request range. Assumes UTC as timezone unless otherwise specified.
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         mode : FeedMode or str {'live', 'historical-streaming', 'historical'}, default 'historical-streaming'
             The data feed mode for the request.
         symbols : List[Union[str, int]] or str, optional
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
@@ -453,15 +489,15 @@
         float
             The cost in US Dollars.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         params: List[Tuple[str, str]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start", datetime_to_string(start)),
             ("end", datetime_to_string(end)),
             ("symbols", symbols_list),
             ("schema", str(validate_enum(schema, Schema, "schema"))),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(SType.PRODUCT_ID)),
             ("mode", validate_enum(mode, FeedMode, "mode")),
```

### Comparing `databento-0.8.1/databento/historical/api/symbology.py` & `databento-0.9.0/databento/historical/api/symbology.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from typing import Any, Dict, List, Optional, Tuple, Union
 
 from databento.common.enums import SType
 from databento.common.parsing import (
     datetime_to_date_string,
     optional_symbols_list_to_string,
 )
-from databento.common.validation import validate_enum
+from databento.common.validation import validate_enum, validate_semantic_string
 from databento.historical.api import API_VERSION
 from databento.historical.http import BentoHttpAPI
 from requests import Response
 
 
 class SymbologyHttpAPI(BentoHttpAPI):
     """
@@ -59,15 +59,15 @@
             A result including a map of input symbol to output symbol across a
             date range.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         params: List[Tuple[str, str]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("symbols", symbols_list),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(validate_enum(stype_out, SType, "stype_out"))),
             ("start_date", datetime_to_date_string(start_date)),
             ("end_date", datetime_to_date_string(end_date)),
             ("default_value", default_value),
         ]
```

### Comparing `databento-0.8.1/databento/historical/api/timeseries.py` & `databento-0.9.0/databento/historical/api/timeseries.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from typing import List, Optional, Tuple, Union
 
 import pandas as pd
 from databento.common.bento import Bento
 from databento.common.deprecated import deprecated
 from databento.common.enums import Compression, Dataset, Encoding, Schema, SType
 from databento.common.parsing import datetime_to_string, optional_symbols_list_to_string
-from databento.common.validation import validate_enum
+from databento.common.validation import validate_enum, validate_semantic_string
 from databento.historical.api import API_VERSION
 from databento.historical.error import BentoWarning
 from databento.historical.http import BentoHttpAPI
 
 
 class TimeSeriesHttpAPI(BentoHttpAPI):
     """
@@ -80,18 +80,18 @@
 
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code (string identifier) for the request.
         start : pd.Timestamp or date or str or int
             The start datetime (UTC) of the request time range (inclusive).
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int
             The end datetime (UTC) of the request time range (exclusive).
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         symbols : List[Union[str, int]] or str, optional
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If more than 1 symbol is specified, the data is merged and sorted by time.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
         stype_in : SType or str, default 'native'
@@ -116,15 +116,15 @@
         Calling this method will incur a cost.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         schema_valid = validate_enum(schema, Schema, "schema")
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start", datetime_to_string(start)),
             ("end", datetime_to_string(end)),
             ("symbols", symbols_list),
             ("schema", str(schema_valid)),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(validate_enum(stype_out, SType, "stype_out"))),
             ("encoding", str(Encoding.DBN)),  # Always request dbn
@@ -216,18 +216,18 @@
 
         Parameters
         ----------
         dataset : Dataset or str
             The dataset code (string identifier) for the request.
         start : pd.Timestamp or date or str or int
             The start datetime (UTC) of the request time range (inclusive).
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         end : pd.Timestamp or date or str or int
             The end datetime (UTC) of the request time range (exclusive).
-            If an integer is passed, then this represents nanoseconds since UNIX epoch.
+            If an integer is passed, then this represents nanoseconds since the UNIX epoch.
         symbols : List[Union[str, int]] or str, optional
             The product symbols to filter for. Takes up to 2,000 symbols per request.
             If more than 1 symbol is specified, the data is merged and sorted by time.
             If 'ALL_SYMBOLS' or `None` then will be for **all** symbols.
         schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
             The data record schema for the request.
         stype_in : SType or str, default 'native'
@@ -252,15 +252,15 @@
         Calling this method will incur a cost.
 
         """
         stype_in_valid = validate_enum(stype_in, SType, "stype_in")
         symbols_list = optional_symbols_list_to_string(symbols, stype_in_valid)
         schema_valid = validate_enum(schema, Schema, "schema")
         params: List[Tuple[str, Optional[str]]] = [
-            ("dataset", dataset),
+            ("dataset", validate_semantic_string(dataset, "dataset")),
             ("start", datetime_to_string(start)),
             ("end", datetime_to_string(end)),
             ("symbols", symbols_list),
             ("schema", str(schema_valid)),
             ("stype_in", str(stype_in_valid)),
             ("stype_out", str(validate_enum(stype_out, SType, "stype_out"))),
             ("encoding", str(Encoding.DBN)),  # Always request dbn
```

### Comparing `databento-0.8.1/databento/historical/client.py` & `databento-0.9.0/databento/historical/client.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,19 +1,22 @@
+import logging
 import os
 from typing import Optional, Union
 
 from databento.common.enums import HistoricalGateway
-from databento.common.logging import log_info
 from databento.common.validation import validate_gateway
 from databento.historical.api.batch import BatchHttpAPI
 from databento.historical.api.metadata import MetadataHttpAPI
 from databento.historical.api.symbology import SymbologyHttpAPI
 from databento.historical.api.timeseries import TimeSeriesHttpAPI
 
 
+logger = logging.getLogger(__name__)
+
+
 class Historical:
     """
     Provides a client connection class for requesting historical data and
     metadata from the Databento API servers.
 
     Parameters
     ----------
@@ -50,15 +53,15 @@
 
         self.batch = BatchHttpAPI(key=key, gateway=gateway)
         self.metadata = MetadataHttpAPI(key=key, gateway=gateway)
         self.symbology = SymbologyHttpAPI(key=key, gateway=gateway)
         self.timeseries = TimeSeriesHttpAPI(key=key, gateway=gateway)
 
         # Not logging security sensitive `key`
-        log_info(f"Initialized {type(self).__name__}(gateway={self._gateway})")
+        logger.info("Initialized %s(gateway=%s)", type(self).__name__, self.gateway)
 
     @property
     def key(self) -> str:
         """
         Return the user API key for the client.
 
         Returns
```

### Comparing `databento-0.8.1/databento/historical/error.py` & `databento-0.9.0/databento/historical/error.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento/historical/http.py` & `databento-0.9.0/databento/historical/http.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/databento.egg-info/PKG-INFO` & `databento-0.9.0/databento.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: databento
-Version: 0.8.1
+Version: 0.9.0
 Summary: Official Python client library for Databento
 Home-page: https://github.com/databento/databento-python
 Author: Databento
 Author-email: support@databento.com
 License: Apache License 2.0
 Project-URL: Bug Tracker, https://github.com/databento/databento-python/issues
 Project-URL: Documentation, https://docs.databento.com/
```

### Comparing `databento-0.8.1/databento.egg-info/SOURCES.txt` & `databento-0.9.0/databento.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -13,18 +13,18 @@
 databento.egg-info/requires.txt
 databento.egg-info/top_level.txt
 databento/common/__init__.py
 databento/common/bento.py
 databento/common/data.py
 databento/common/deprecated.py
 databento/common/enums.py
-databento/common/logging.py
 databento/common/metadata.py
 databento/common/parsing.py
 databento/common/symbology.py
+databento/common/utility.py
 databento/common/validation.py
 databento/historical/__init__.py
 databento/historical/client.py
 databento/historical/error.py
 databento/historical/http.py
 databento/historical/api/__init__.py
 databento/historical/api/batch.py
```

### Comparing `databento-0.8.1/setup.py` & `databento-0.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/data/generator.py` & `databento-0.9.0/tests/data/generator.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_bento_compression.py` & `databento-0.9.0/tests/test_bento_compression.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_bento_data_source.py` & `databento-0.9.0/tests/test_bento_data_source.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_common_enums.py` & `databento-0.9.0/tests/test_common_enums.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_common_parsing.py` & `databento-0.9.0/tests/test_common_parsing.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_common_validation.py` & `databento-0.9.0/tests/test_common_validation.py`

 * *Files 13% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 import pytest
 from databento.common.enums import Encoding
 from databento.common.validation import (
     validate_enum,
     validate_gateway,
     validate_maybe_enum,
     validate_path,
+    validate_semantic_string,
     validate_smart_symbol,
 )
 
 
 class TestValidation:
     @pytest.mark.parametrize(
         "value",
@@ -116,7 +117,33 @@
     ) -> None:
         """ """
         if isinstance(expected, str):
             assert validate_smart_symbol(symbol) == expected
         else:
             with pytest.raises(expected):
                 validate_smart_symbol(symbol)
+
+
+@pytest.mark.parametrize(
+    "value,expected",
+    [
+        pytest.param("nick", "nick"),
+        pytest.param("", ValueError, id="empty"),
+        pytest.param(" ", ValueError, id="whitespace"),
+        pytest.param("foo\x00", ValueError, id="unprintable"),
+    ],
+)
+def test_validate_semantic_string(
+    value: str,
+    expected: Union[str, Type[Exception]],
+) -> None:
+    """
+    Test that validate_semantic_string rejects string which are:
+        - empty
+        - whitespace
+        - contain unprintable characters
+    """
+    if isinstance(expected, str):
+        assert validate_semantic_string(value, "unittest") == expected
+    else:
+        with pytest.raises(expected):
+            assert validate_semantic_string(value, "")
```

### Comparing `databento-0.8.1/tests/test_historical_batch.py` & `databento-0.9.0/tests/test_historical_batch.py`

 * *Files 3% similar despite different names*

```diff
@@ -166,19 +166,21 @@
     ) -> None:
         # Arrange
         mocked_get = mocker.patch("requests.get")
         job_id = "GLBX-20220610-5DEFXVTMSM"
         filename = "glbx-mdp3-20220610.mbo.csv.zst"
 
         # Act
-        self.client.batch.download(
-            job_id=job_id,
-            output_dir="my_data",
-            filename_to_download=filename,
-        )
+        with pytest.raises(ValueError):
+            # We expect this to fail since this is not a real batch job.
+            self.client.batch.download(
+                job_id=job_id,
+                output_dir="my_data",
+                filename_to_download=filename,
+            )
 
         # Assert
         call = mocked_get.call_args.kwargs
         assert (
             call["url"]
             == f"https://hist.databento.com/v{db.API_VERSION}/batch.list_files"
         )
```

### Comparing `databento-0.8.1/tests/test_historical_bento.py` & `databento-0.9.0/tests/test_historical_bento.py`

 * *Files 10% similar despite different names*

```diff
@@ -112,15 +112,15 @@
     assert bento.schema == Schema.MBO
     assert bento.symbols == ["ESH1"]
     assert bento.stype_in == SType.NATIVE
     assert bento.stype_out == SType.PRODUCT_ID
     assert bento.start == pd.Timestamp("2020-12-28 13:00:00+0000", tz="UTC")
     assert bento.end == pd.Timestamp("2020-12-29 13:00:00+0000", tz="UTC")
     assert bento.limit == 2
-    assert bento.record_count == 2
+    assert len(bento.to_ndarray()) == 2
     assert bento.mappings == {
         "ESH1": [
             {
                 "symbol": "5482",
                 "start_date": dt.date(2020, 12, 28),
                 "end_date": dt.date(2020, 12, 30),
             },
@@ -243,14 +243,52 @@
     df = data.to_df()
 
     # Assert
     assert list(df.columns) == list(df.columns)
     assert len(df) == 2
 
 
+@pytest.mark.parametrize(
+    "schema",
+    [
+        pytest.param(schema, id=str(schema))
+        for schema in (
+            Schema.MBO,
+            Schema.MBP_1,
+            Schema.MBP_10,
+            Schema.TBBO,
+            Schema.TRADES,
+            Schema.OHLCV_1S,
+            Schema.OHLCV_1M,
+            Schema.OHLCV_1H,
+            Schema.OHLCV_1D,
+            Schema.DEFINITION,
+        )
+    ],
+)
+def test_to_df_drop_columns(
+    schema: Schema,
+) -> None:
+    """
+    Test that rtype, length, and dummy columns are dropped when
+    calling to_df().
+    """
+    # Arrange
+    stub_data = get_test_data(schema=schema)
+    data = Bento.from_bytes(data=stub_data)
+
+    # Act
+    df = data.to_df()
+
+    # Assert
+    assert "length" not in df
+    assert "rtype" not in df
+    assert "dummy" not in df
+
+
 def test_to_df_with_mbo_data_returns_expected_record() -> None:
     # Arrange
     stub_data = get_test_data(schema=Schema.MBO)
     data = Bento.from_bytes(data=stub_data)
 
     # Act
     df = data.to_df(
@@ -401,15 +439,15 @@
     path = get_test_data_path(schema=Schema.MBO)
 
     # Act
     data = databento.from_dbn(path=path)
 
     # Assert
     assert data.schema == Schema.MBO
-    assert data.record_count == 2
+    assert len(data.to_ndarray()) == 2
 
 
 def test_mbo_to_csv_writes_expected_file_to_disk(tmp_path: Path) -> None:
     # Arrange
     test_data_path = get_test_data_path(schema=Schema.MBO)
     data = Bento.from_file(path=test_data_path)
 
@@ -629,14 +667,46 @@
         b'8,"publisher_id":1,"product_id":5482,"action":"A","side":"A","dept'
         b'h":0,"flags":128,"price":3720.5,"size":1,"sequence":1170364,"bid_p'
         b'x_00":3720.25,"ask_px_00":3720.5,"bid_sz_00":24,"ask_sz_00":12,"bi'
         b'd_oq_00":15,"ask_oq_00":10,"symbol":"ESH1"}\n'
     )
 
 
+@pytest.mark.parametrize(
+    "schema",
+    [
+        s
+        for s in Schema
+        if s
+        not in (
+            Schema.OHLCV_1H,
+            Schema.OHLCV_1D,
+            Schema.STATUS,
+            Schema.STATISTICS,
+            Schema.DEFINITION,
+            Schema.GATEWAY_ERROR,
+            Schema.SYMBOL_MAPPING,
+        )
+    ],
+)
+def test_bento_repr(schema: Schema) -> None:
+    """
+    Check that a more meaningful string is returned
+    when calling `repr()` on a Bento.
+    """
+    # Arrange
+    stub_data = get_test_data(schema=schema)
+
+    # Act
+    bento = Bento.from_bytes(data=stub_data)
+
+    # Assert
+    assert repr(bento) == f"<Bento(schema={schema})>"
+
+
 def test_bento_iterable() -> None:
     """
     Tests the Bento iterable implementation to ensure records
     can be accessed by iteration.
     """
     # Arrange
     stub_data = get_test_data(schema=Schema.MBO)
@@ -714,10 +784,10 @@
     dbn_stub_data = (
         zstandard.ZstdDecompressor().stream_reader(get_test_data(schema=schema)).read()
     )
 
     zstd_bento = Bento.from_bytes(zstd_stub_data)
     dbn_bento = Bento.from_bytes(dbn_stub_data)
 
-    assert zstd_bento.record_count == dbn_bento.record_count
+    assert len(zstd_bento.to_ndarray()) == len(dbn_bento.to_ndarray())
     assert zstd_bento.metadata == dbn_bento.metadata
     assert zstd_bento.reader.read() == dbn_bento.reader.read()
```

### Comparing `databento-0.8.1/tests/test_historical_client.py` & `databento-0.9.0/tests/test_historical_client.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_historical_error.py` & `databento-0.9.0/tests/test_historical_error.py`

 * *Files identical despite different names*

### Comparing `databento-0.8.1/tests/test_historical_metadata.py` & `databento-0.9.0/tests/test_historical_metadata.py`

 * *Files 3% similar despite different names*

```diff
@@ -243,14 +243,42 @@
         assert all(
             v in call["headers"]["user-agent"] for v in ("Databento/", "Python/")
         )
         assert call["timeout"] == (100, 100)
         assert isinstance(call["auth"], requests.auth.HTTPBasicAuth)
 
     @pytest.mark.skipif(sys.version_info < (3, 8), reason="incompatible mocking")
+    def test_get_dataset_range_sends_expected_request(
+        self,
+        mocker: MockerFixture,
+    ) -> None:
+        # Arrange
+        mocked_get = mocker.patch("requests.get")
+
+        # Act
+        self.client.metadata.get_dataset_range(dataset="GLBX.MDP3")
+
+        # Assert
+        call = mocked_get.call_args.kwargs
+        assert (
+            call["url"]
+            == f"https://hist.databento.com/v{db.API_VERSION}/metadata.get_dataset_range"  # noqa
+        )
+        assert sorted(call["headers"].keys()) == ["accept", "user-agent"]
+        assert call["headers"]["accept"] == "application/json"
+        assert all(
+            v in call["headers"]["user-agent"] for v in ("Databento/", "Python/")
+        )
+        assert call["params"] == [
+            ("dataset", "GLBX.MDP3"),
+        ]
+        assert call["timeout"] == (100, 100)
+        assert isinstance(call["auth"], requests.auth.HTTPBasicAuth)
+
+    @pytest.mark.skipif(sys.version_info < (3, 8), reason="incompatible mocking")
     def test_get_record_count_sends_expected_request(
         self,
         mocker: MockerFixture,
     ) -> None:
         # Arrange
         mocked_get = mocker.patch("requests.get")
```

### Comparing `databento-0.8.1/tests/test_historical_timeseries.py` & `databento-0.9.0/tests/test_historical_timeseries.py`

 * *Files identical despite different names*

