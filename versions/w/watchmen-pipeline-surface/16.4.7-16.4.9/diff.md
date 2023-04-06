# Comparing `tmp/watchmen_pipeline_surface-16.4.7.tar.gz` & `tmp/watchmen_pipeline_surface-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_pipeline_surface-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_pipeline_surface-16.4.9.tar", max compression
```

## Comparing `watchmen_pipeline_surface-16.4.7.tar` & `watchmen_pipeline_surface-16.4.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/LICENSE
--rw-r--r--   0        0        0     1456 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      102 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/__init__.py
--rw-r--r--   0        0        0       99 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/__init__.py
--rw-r--r--   0        0        0      854 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/handler.py
--rw-r--r--   0        0        0     1218 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/kafka.py
--rw-r--r--   0        0        0     1689 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/rabbitmq.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/__init__.py
--rw-r--r--   0        0        0     1619 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/monitor_log_router.py
--rw-r--r--   0        0        0     1727 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/pipeline_trigger_router.py
--rw-r--r--   0        0        0     2742 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/topic_snapshot_adhoc_router.py
--rw-r--r--   0        0        0     5996 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/topic_trigger_router.py
--rw-r--r--   0        0        0      370 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/main.py
--rw-r--r--   0        0        0     2850 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/settings.py
--rw-r--r--   0        0        0     1433 2023-01-18 10:06:03.446851 watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/surface.py
--rw-r--r--   0        0        0     1343 1970-01-01 00:00:00.000000 watchmen_pipeline_surface-16.4.7/setup.py
--rw-r--r--   0        0        0     1490 1970-01-01 00:00:00.000000 watchmen_pipeline_surface-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/LICENSE
+-rw-r--r--   0        0        0     1456 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      102 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/__init__.py
+-rw-r--r--   0        0        0       99 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/__init__.py
+-rw-r--r--   0        0        0      854 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/handler.py
+-rw-r--r--   0        0        0     1218 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/kafka.py
+-rw-r--r--   0        0        0     1689 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/rabbitmq.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/__init__.py
+-rw-r--r--   0        0        0     1619 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/monitor_log_router.py
+-rw-r--r--   0        0        0     1727 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/pipeline_trigger_router.py
+-rw-r--r--   0        0        0     2742 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/topic_snapshot_adhoc_router.py
+-rw-r--r--   0        0        0     5996 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/topic_trigger_router.py
+-rw-r--r--   0        0        0      370 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/main.py
+-rw-r--r--   0        0        0     1637 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/settings.py
+-rw-r--r--   0        0        0     1162 2023-02-23 10:23:45.996775 watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/surface.py
+-rw-r--r--   0        0        0     1343 1970-01-01 00:00:00.000000 watchmen_pipeline_surface-16.4.9/setup.py
+-rw-r--r--   0        0        0     1490 1970-01-01 00:00:00.000000 watchmen_pipeline_surface-16.4.9/PKG-INFO
```

### Comparing `watchmen_pipeline_surface-16.4.7/LICENSE` & `watchmen_pipeline_surface-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/pyproject.toml` & `watchmen_pipeline_surface-16.4.9/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 [tool.poetry]
 name = "watchmen-pipeline-surface"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_pipeline_surface", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-pipeline-kernel = "16.4.7"
-watchmen-rest = "16.4.7"
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-collector-kernel = { version = "16.4.7", optional = true }
+watchmen-pipeline-kernel = "16.4.9"
+watchmen-rest = "16.4.9"
+watchmen-storage-mysql = { version = "16.4.9", optional = true }
+watchmen-storage-oracle = { version = "16.4.9", optional = true }
+watchmen-storage-mongodb = { version = "16.4.9", optional = true }
+watchmen-storage-mssql = { version = "16.4.9", optional = true }
+watchmen-storage-postgresql = { version = "16.4.9", optional = true }
+watchmen-collector-kernel = { version = "16.4.9", optional = true }
 kafka-python = { version = "^2.0.2", optional = true }
 aiokafka = { version = "^0.7.2", optional = true }
 aio-pika = { version = "^7.1.2", optional = true }
 requests = { version = "^2.27.1", optional = true }
 
 [tool.poetry.dev-dependencies]
```

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/handler.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/handler.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/kafka.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/kafka.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/connectors/rabbitmq.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/connectors/rabbitmq.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/monitor_log_router.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/monitor_log_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/pipeline_trigger_router.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/pipeline_trigger_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/topic_snapshot_adhoc_router.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/topic_snapshot_adhoc_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/data/topic_trigger_router.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/data/topic_trigger_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_pipeline_surface-16.4.7/src/watchmen_pipeline_surface/surface.py` & `watchmen_pipeline_surface-16.4.9/src/watchmen_pipeline_surface/surface.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from watchmen_pipeline_kernel.boot import init_prebuilt_external_writers, init_topic_snapshot_jobs
 from .connectors import init_kafka, init_rabbitmq
 from .settings import ask_kafka_connector_enabled, ask_kafka_connector_settings, ask_rabbitmq_connector_enabled, \
-	ask_rabbitmq_connector_settings, ask_s3_connector_enabled, ask_s3_connector_settings
+	ask_rabbitmq_connector_settings
 
 
 class PipelineSurface:
 	def __init__(self):
 		pass
 
 	# noinspection PyMethodMayBeStatic
@@ -14,23 +14,17 @@
 			init_kafka(ask_kafka_connector_settings())
 
 	# noinspection PyMethodMayBeStatic
 	def init_rabbitmq_connector(self) -> None:
 		if ask_rabbitmq_connector_enabled():
 			init_rabbitmq(ask_rabbitmq_connector_settings())
 
-	def init_s3_connector(self) -> None:
-		if ask_s3_connector_enabled():
-			from watchmen_collector_kernel.connector import init_s3_collector
-			init_s3_collector(ask_s3_connector_settings())
-
 	def init_connectors(self) -> None:
 		self.init_kafka_connector()
 		self.init_rabbitmq_connector()
-		self.init_s3_connector()
 
 	# noinspection PyMethodMayBeStatic
 	def init_external_writers(self) -> None:
 		init_prebuilt_external_writers()
 
 	# noinspection PyMethodMayBeStatic
 	def init_topic_snapshot_jobs(self) -> None:
```

### Comparing `watchmen_pipeline_surface-16.4.7/setup.py` & `watchmen_pipeline_surface-16.4.9/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -9,30 +9,30 @@
  'watchmen_pipeline_surface.connectors',
  'watchmen_pipeline_surface.data']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-pipeline-kernel==16.4.7', 'watchmen-rest==16.4.7']
+['watchmen-pipeline-kernel==16.4.9', 'watchmen-rest==16.4.9']
 
 extras_require = \
-{'collector': ['watchmen-collector-kernel==16.4.7'],
+{'collector': ['watchmen-collector-kernel==16.4.9'],
  'kafka': ['kafka-python>=2.0.2,<3.0.0', 'aiokafka>=0.7.2,<0.8.0'],
- 'mongodb': ['watchmen-storage-mongodb==16.4.7'],
- 'mssql': ['watchmen-storage-mssql==16.4.7'],
- 'mysql': ['watchmen-storage-mysql==16.4.7'],
- 'oracle': ['watchmen-storage-oracle==16.4.7'],
- 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
+ 'mongodb': ['watchmen-storage-mongodb==16.4.9'],
+ 'mssql': ['watchmen-storage-mssql==16.4.9'],
+ 'mysql': ['watchmen-storage-mysql==16.4.9'],
+ 'oracle': ['watchmen-storage-oracle==16.4.9'],
+ 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
  'rabbitmq': ['aio-pika>=7.1.2,<8.0.0'],
  'standard-ext-writer': ['requests>=2.27.1,<3.0.0']}
 
 setup_kwargs = {
     'name': 'watchmen-pipeline-surface',
-    'version': '16.4.7',
+    'version': '16.4.9',
     'description': '',
     'long_description': 'None',
     'author': 'botlikes',
     'author_email': '75356972+botlikes456@users.noreply.github.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `watchmen_pipeline_surface-16.4.7/PKG-INFO` & `watchmen_pipeline_surface-16.4.9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-pipeline-surface
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -21,15 +21,15 @@
 Provides-Extra: postgresql
 Provides-Extra: rabbitmq
 Provides-Extra: standard-ext-writer
 Requires-Dist: aio-pika (>=7.1.2,<8.0.0) ; extra == "rabbitmq"
 Requires-Dist: aiokafka (>=0.7.2,<0.8.0) ; extra == "kafka"
 Requires-Dist: kafka-python (>=2.0.2,<3.0.0) ; extra == "kafka"
 Requires-Dist: requests (>=2.27.1,<3.0.0) ; extra == "standard-ext-writer"
-Requires-Dist: watchmen-collector-kernel (==16.4.7) ; extra == "collector"
-Requires-Dist: watchmen-pipeline-kernel (==16.4.7)
-Requires-Dist: watchmen-rest (==16.4.7)
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
+Requires-Dist: watchmen-collector-kernel (==16.4.9) ; extra == "collector"
+Requires-Dist: watchmen-pipeline-kernel (==16.4.9)
+Requires-Dist: watchmen-rest (==16.4.9)
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
```

