# Comparing `tmp/tap-ga4-0.0.8.tar.gz` & `tmp/tap-ga4-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tap-ga4-0.0.8.tar", last modified: Tue Oct 25 20:19:09 2022, max compression
+gzip compressed data, was "tap-ga4-0.0.9.tar", last modified: Tue Oct 25 21:18:58 2022, max compression
```

## Comparing `tap-ga4-0.0.8.tar` & `tap-ga4-0.0.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 20:19:09.823067 tap-ga4-0.0.8/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    34523 2022-08-16 19:49:37.000000 tap-ga4-0.0.8/LICENSE
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       54 2022-10-25 17:36:51.000000 tap-ga4-0.0.8/MANIFEST.in
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      280 2022-10-25 20:19:09.823067 tap-ga4-0.0.8/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       98 2022-08-30 18:41:28.000000 tap-ga4-0.0.8/README.md
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2022-10-25 20:19:09.823067 tap-ga4-0.0.8/setup.cfg
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      786 2022-10-25 20:18:57.000000 tap-ga4-0.0.8/setup.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 20:19:09.823067 tap-ga4-0.0.8/tap_ga4/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1129 2022-10-25 19:36:08.000000 tap-ga4-0.0.8/tap_ga4/__init__.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4659 2022-10-17 18:27:45.000000 tap-ga4-0.0.8/tap_ga4/client.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10213 2022-10-25 20:18:57.000000 tap-ga4-0.0.8/tap_ga4/discover.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   176365 2022-10-18 14:10:50.000000 tap-ga4-0.0.8/tap_ga4/field_exclusions.json
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    19324 2022-10-25 17:36:51.000000 tap-ga4-0.0.8/tap_ga4/reports.py
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10310 2022-10-25 19:36:08.000000 tap-ga4-0.0.8/tap_ga4/sync.py
-drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 20:19:09.823067 tap-ga4-0.0.8/tap_ga4.egg-info/
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      280 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/PKG-INFO
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      349 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/SOURCES.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/dependency_links.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       52 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/entry_points.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      108 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/requires.txt
--rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        8 2022-10-25 20:19:09.000000 tap-ga4-0.0.8/tap_ga4.egg-info/top_level.txt
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 21:18:58.015288 tap-ga4-0.0.9/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    34523 2022-08-16 19:49:37.000000 tap-ga4-0.0.9/LICENSE
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       54 2022-10-25 17:36:51.000000 tap-ga4-0.0.9/MANIFEST.in
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      280 2022-10-25 21:18:58.015288 tap-ga4-0.0.9/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       98 2022-08-30 18:41:28.000000 tap-ga4-0.0.9/README.md
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       38 2022-10-25 21:18:58.015288 tap-ga4-0.0.9/setup.cfg
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      786 2022-10-25 21:18:48.000000 tap-ga4-0.0.9/setup.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 21:18:58.015288 tap-ga4-0.0.9/tap_ga4/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     1129 2022-10-25 19:36:08.000000 tap-ga4-0.0.9/tap_ga4/__init__.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)     4659 2022-10-17 18:27:45.000000 tap-ga4-0.0.9/tap_ga4/client.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10213 2022-10-25 20:18:57.000000 tap-ga4-0.0.9/tap_ga4/discover.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)   176365 2022-10-18 14:10:50.000000 tap-ga4-0.0.9/tap_ga4/field_exclusions.json
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    19324 2022-10-25 17:36:51.000000 tap-ga4-0.0.9/tap_ga4/reports.py
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)    10702 2022-10-25 21:18:48.000000 tap-ga4-0.0.9/tap_ga4/sync.py
+drwxrwxr-x   0 ubuntu    (1000) ubuntu    (1000)        0 2022-10-25 21:18:58.015288 tap-ga4-0.0.9/tap_ga4.egg-info/
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      280 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/PKG-INFO
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      349 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/SOURCES.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        1 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/dependency_links.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)       52 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/entry_points.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)      108 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/requires.txt
+-rw-rw-r--   0 ubuntu    (1000) ubuntu    (1000)        8 2022-10-25 21:18:58.000000 tap-ga4-0.0.9/tap_ga4.egg-info/top_level.txt
```

### Comparing `tap-ga4-0.0.8/LICENSE` & `tap-ga4-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/setup.py` & `tap-ga4-0.0.9/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name="tap-ga4",
-    version="0.0.8",
+    version="0.0.9",
     description="Singer.io tap for extracting data",
     author="Stitch",
     url="http://singer.io",
     classifiers=["Programming Language :: Python :: 3 :: Only"],
     py_modules=["tap_ga4"],
     install_requires=[
         "google-analytics-data==0.14.0",
```

### Comparing `tap-ga4-0.0.8/tap_ga4/__init__.py` & `tap-ga4-0.0.9/tap_ga4/__init__.py`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/tap_ga4/client.py` & `tap-ga4-0.0.9/tap_ga4/client.py`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/tap_ga4/discover.py` & `tap-ga4-0.0.9/tap_ga4/discover.py`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/tap_ga4/field_exclusions.json` & `tap-ga4-0.0.9/tap_ga4/field_exclusions.json`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/tap_ga4/reports.py` & `tap-ga4-0.0.9/tap_ga4/reports.py`

 * *Files identical despite different names*

### Comparing `tap-ga4-0.0.8/tap_ga4/sync.py` & `tap-ga4-0.0.9/tap_ga4/sync.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,13 +1,17 @@
 import hashlib
 import json
 from datetime import datetime, timedelta
 import singer
 from singer import Transformer, get_bookmark, metadata, utils
 from google.analytics.data_v1beta.types import (Metric, Dimension)
+
+from tap_ga4.discover import to_snake_case
+
+
 LOGGER = singer.get_logger()
 
 DEFAULT_CONVERSION_WINDOW = 90
 DEFAULT_REQUEST_WINDOW_SIZE = 7
 
 
 def sort_and_shuffle_streams(currently_syncing, selected_streams):
@@ -63,20 +67,27 @@
     while range_start <= end_date:
         # NB: Subtract 1 from request_window_size because date range in RunReportRequest is inclusive
         range_end = range_start + timedelta(days=request_window_size - 1)
         yield (range_start.strftime("%Y-%m-%d"), min(end_date, range_end).strftime("%Y-%m-%d"))
         range_start = range_end + timedelta(days=1)
 
 
+def transform_headers(dimension_headers, metric_headers):
+    dim_headers = [to_snake_case(dimension) for dimension in dimension_headers]
+    metric_headers = [to_snake_case(metric) for metric in metric_headers]
+    return dim_headers, metric_headers
+
+
 def row_to_record(report, row, dimension_headers, metric_headers):
     """
     Parse a RunReportResponse row into a single Singer record, with added
     runtime info and PK.
     """
     record = {}
+    dimension_headers, metric_headers = transform_headers(dimension_headers, metric_headers)
     dimension_pairs = list(zip(dimension_headers, [dimension.value for dimension in row.dimension_values]))
     record.update(dimension_pairs)
     record.update(zip(metric_headers, [metric.value for metric in row.metric_values]))
     record["property_id"] = report["property_id"]
     record["account_id"] = report["account_id"]
     record["_sdc_record_hash"] = generate_sdc_record_hash(record, dimension_pairs)
     return record
```

