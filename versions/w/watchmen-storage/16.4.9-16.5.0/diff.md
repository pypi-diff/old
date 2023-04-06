# Comparing `tmp/watchmen_storage-16.4.9.tar.gz` & `tmp/watchmen_storage-16.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage-16.4.9.tar", max compression
+gzip compressed data, was "watchmen_storage-16.5.0.tar", max compression
```

## Comparing `watchmen_storage-16.4.9.tar` & `watchmen_storage-16.5.0.tar`

### file list

```diff
@@ -1,18 +1,17 @@
--rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/LICENSE
--rw-r--r--   0        0        0      474 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/pyproject.toml
--rw-r--r--   0        0        0     2196 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/__init__.py
--rw-r--r--   0        0        0     4917 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/competitive_worker_id_generator.py
--rw-r--r--   0        0        0     5549 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/data_source_helper.py
--rw-r--r--   0        0        0     1650 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/free_storage_types.py
--rw-r--r--   0        0        0      211 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/secrets_manager.py
--rw-r--r--   0        0        0      730 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/secrets_manager_aws.py
--rw-r--r--   0        0        0      988 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/settings.py
--rw-r--r--   0        0        0     2750 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/snowflake.py
--rw-r--r--   0        0        0      232 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/snowflake_worker_id_generator.py
--rw-r--r--   0        0        0     7259 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/storage_based_worker_id_generator.py
--rw-r--r--   0        0        0      721 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/storage_exception.py
--rw-r--r--   0        0        0     5884 2023-02-23 10:23:46.016776 watchmen_storage-16.4.9/src/watchmen_storage/storage_spi.py
--rw-r--r--   0        0        0     4610 2023-02-23 10:23:46.020776 watchmen_storage-16.4.9/src/watchmen_storage/storage_types.py
--rw-r--r--   0        0        0      630 2023-02-23 10:23:46.020776 watchmen_storage-16.4.9/src/watchmen_storage/topic_utils.py
--rw-r--r--   0        0        0      695 1970-01-01 00:00:00.000000 watchmen_storage-16.4.9/setup.py
--rw-r--r--   0        0        0      521 1970-01-01 00:00:00.000000 watchmen_storage-16.4.9/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/LICENSE
+-rw-r--r--   0        0        0      472 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/pyproject.toml
+-rw-r--r--   0        0        0     2196 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/__init__.py
+-rw-r--r--   0        0        0     4917 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/competitive_worker_id_generator.py
+-rw-r--r--   0        0        0     5549 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/data_source_helper.py
+-rw-r--r--   0        0        0     1685 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/free_storage_types.py
+-rw-r--r--   0        0        0      211 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/secrets_manager.py
+-rw-r--r--   0        0        0      730 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/secrets_manager_aws.py
+-rw-r--r--   0        0        0      988 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/settings.py
+-rw-r--r--   0        0        0     2750 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/snowflake.py
+-rw-r--r--   0        0        0      232 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/snowflake_worker_id_generator.py
+-rw-r--r--   0        0        0     7259 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/storage_based_worker_id_generator.py
+-rw-r--r--   0        0        0      721 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/storage_exception.py
+-rw-r--r--   0        0        0     5884 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/storage_spi.py
+-rw-r--r--   0        0        0     4645 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/storage_types.py
+-rw-r--r--   0        0        0      630 2023-04-06 09:13:10.428011 watchmen_storage-16.5.0/src/watchmen_storage/topic_utils.py
+-rw-r--r--   0        0        0      521 1970-01-01 00:00:00.000000 watchmen_storage-16.5.0/PKG-INFO
```

### Comparing `watchmen_storage-16.4.9/LICENSE` & `watchmen_storage-16.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/__init__.py` & `watchmen_storage-16.5.0/src/watchmen_storage/__init__.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/competitive_worker_id_generator.py` & `watchmen_storage-16.5.0/src/watchmen_storage/competitive_worker_id_generator.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/data_source_helper.py` & `watchmen_storage-16.5.0/src/watchmen_storage/data_source_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/free_storage_types.py` & `watchmen_storage-16.5.0/src/watchmen_storage/free_storage_types.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 
 from watchmen_model.common import DataModel, Pageable
 from .storage_types import ColumnNameLiteral, EntityCriteria, EntitySortColumn, Literal
 
 
 class FreeAggregateArithmetic(str, Enum):
 	NONE = 'none'
+	DISTINCT_COUNT = 'distinct_count'
 	COUNT = 'count'
 	SUMMARY = 'sum'
 	AVERAGE = 'avg'
 	MAXIMUM = 'max'
 	MINIMUM = 'min'
```

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/secrets_manager_aws.py` & `watchmen_storage-16.5.0/src/watchmen_storage/secrets_manager_aws.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/settings.py` & `watchmen_storage-16.5.0/src/watchmen_storage/settings.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/snowflake.py` & `watchmen_storage-16.5.0/src/watchmen_storage/snowflake.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/storage_based_worker_id_generator.py` & `watchmen_storage-16.5.0/src/watchmen_storage/storage_based_worker_id_generator.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/storage_exception.py` & `watchmen_storage-16.5.0/src/watchmen_storage/storage_exception.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/storage_spi.py` & `watchmen_storage-16.5.0/src/watchmen_storage/storage_spi.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/storage_types.py` & `watchmen_storage-16.5.0/src/watchmen_storage/storage_types.py`

 * *Files 2% similar despite different names*

```diff
@@ -172,14 +172,15 @@
 	columnName: EntityColumnName  # original name
 	alias: Optional[EntityColumnName]  # alias name
 	columnType: Optional[EntityColumnType] = None  # literal column type
 
 
 class EntityColumnAggregateArithmetic(str, Enum):
 	COUNT = 'count',
+	DISTINCT_COUNT = 'distinct_count'
 	SUM = 'sum',
 	AVG = 'avg',
 	MAX = 'max',
 	MIN = 'min'
 
 
 class EntityStraightAggregateColumn(EntityStraightColumn):
```

### Comparing `watchmen_storage-16.4.9/src/watchmen_storage/topic_utils.py` & `watchmen_storage-16.5.0/src/watchmen_storage/topic_utils.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage-16.4.9/PKG-INFO` & `watchmen_storage-16.5.0/PKG-INFO`

 * *Files 27% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage
-Version: 16.4.9
+Version: 16.5.0
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: boto3 (>=1.24.20,<2.0.0)
-Requires-Dist: watchmen-model (==16.4.9)
+Requires-Dist: watchmen-model (==16.5.0)
```

