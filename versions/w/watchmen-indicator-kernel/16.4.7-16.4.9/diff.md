# Comparing `tmp/watchmen_indicator_kernel-16.4.7.tar.gz` & `tmp/watchmen_indicator_kernel-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_indicator_kernel-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_indicator_kernel-16.4.9.tar", max compression
```

## Comparing `watchmen_indicator_kernel-16.4.7.tar` & `watchmen_indicator_kernel-16.4.9.tar`

### file list

```diff
@@ -1,30 +1,30 @@
--rw-r--r--   0        0        0     1281 2023-01-18 10:06:03.430851 watchmen_indicator_kernel-16.4.7/pyproject.toml
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/__init__.py
--rw-r--r--   0        0        0      109 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/common/__init__.py
--rw-r--r--   0        0        0       49 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/common/exception.py
--rw-r--r--   0        0        0      521 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/common/settings.py
--rw-r--r--   0        0        0      250 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/__init__.py
--rw-r--r--   0        0        0     2163 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/achievement_data_helper.py
--rw-r--r--   0        0        0     3933 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/achievement_data_service.py
--rw-r--r--   0        0        0     1088 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/bucket_helper.py
--rw-r--r--   0        0        0     9526 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/indicator_criteria_service.py
--rw-r--r--   0        0        0     1330 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/indicator_helper.py
--rw-r--r--   0        0        0     2030 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/inspection_data_helper.py
--rw-r--r--   0        0        0     4703 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/inspection_data_service.py
--rw-r--r--   0        0        0     4177 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_base_achievement_data_service.py
--rw-r--r--   0        0        0    11925 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py
--rw-r--r--   0        0        0      786 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_helper.py
--rw-r--r--   0        0        0     5002 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_base_achievement_data_service.py
--rw-r--r--   0        0        0    19431 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py
--rw-r--r--   0        0        0      741 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_helper.py
--rw-r--r--   0        0        0      324 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/__init__.py
--rw-r--r--   0        0        0     3272 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/achievement_service.py
--rw-r--r--   0        0        0     1762 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/achievement_task_service.py
--rw-r--r--   0        0        0     8647 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/bucket_service.py
--rw-r--r--   0        0        0     6603 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/indicator_service.py
--rw-r--r--   0        0        0     2796 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/inspection_service.py
--rw-r--r--   0        0        0     2134 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/objective_analysis_service.py
--rw-r--r--   0        0        0       46 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/plugin/__init__.py
--rw-r--r--   0        0        0      678 2023-01-18 10:06:03.434851 watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/plugin/connector.py
--rw-r--r--   0        0        0     1298 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.7/setup.py
--rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1281 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/__init__.py
+-rw-r--r--   0        0        0      109 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/__init__.py
+-rw-r--r--   0        0        0       49 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/exception.py
+-rw-r--r--   0        0        0      521 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/settings.py
+-rw-r--r--   0        0        0      250 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/__init__.py
+-rw-r--r--   0        0        0     2163 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_helper.py
+-rw-r--r--   0        0        0     3933 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_service.py
+-rw-r--r--   0        0        0     1088 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/bucket_helper.py
+-rw-r--r--   0        0        0     9526 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_criteria_service.py
+-rw-r--r--   0        0        0     1330 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_helper.py
+-rw-r--r--   0        0        0     2030 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_helper.py
+-rw-r--r--   0        0        0     4703 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_service.py
+-rw-r--r--   0        0        0     4177 2023-02-23 10:23:45.980775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_achievement_data_service.py
+-rw-r--r--   0        0        0    11925 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py
+-rw-r--r--   0        0        0      786 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_helper.py
+-rw-r--r--   0        0        0     5002 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_achievement_data_service.py
+-rw-r--r--   0        0        0    19431 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py
+-rw-r--r--   0        0        0      741 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_helper.py
+-rw-r--r--   0        0        0      324 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/__init__.py
+-rw-r--r--   0        0        0     3272 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_service.py
+-rw-r--r--   0        0        0     1762 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_task_service.py
+-rw-r--r--   0        0        0     8647 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/bucket_service.py
+-rw-r--r--   0        0        0     6603 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/indicator_service.py
+-rw-r--r--   0        0        0     2796 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/inspection_service.py
+-rw-r--r--   0        0        0     2134 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/objective_analysis_service.py
+-rw-r--r--   0        0        0       46 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/__init__.py
+-rw-r--r--   0        0        0      678 2023-02-23 10:23:45.984775 watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/connector.py
+-rw-r--r--   0        0        0     1298 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.9/setup.py
+-rw-r--r--   0        0        0     1228 1970-01-01 00:00:00.000000 watchmen_indicator_kernel-16.4.9/PKG-INFO
```

### Comparing `watchmen_indicator_kernel-16.4.7/pyproject.toml` & `watchmen_indicator_kernel-16.4.9/pyproject.toml`

 * *Files 25% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 [tool.poetry]
 name = "watchmen-indicator-kernel"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_indicator_kernel", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-inquiry-kernel = "16.4.7"
-watchmen-inquiry-trino = { version = "16.4.7", optional = true }
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-storage-oss = { version = "16.4.7", optional = true }
-watchmen-storage-s3 = { version = "16.4.7", optional = true }
+watchmen-inquiry-kernel = "16.4.9"
+watchmen-inquiry-trino = { version = "16.4.9", optional = true }
+watchmen-storage-mysql = { version = "16.4.9", optional = true }
+watchmen-storage-oracle = { version = "16.4.9", optional = true }
+watchmen-storage-mongodb = { version = "16.4.9", optional = true }
+watchmen-storage-mssql = { version = "16.4.9", optional = true }
+watchmen-storage-postgresql = { version = "16.4.9", optional = true }
+watchmen-storage-oss = { version = "16.4.9", optional = true }
+watchmen-storage-s3 = { version = "16.4.9", optional = true }
 
 [tool.poetry.dev-dependencies]
 
 [tool.poetry.extras]
 mysql = ["watchmen-storage-mysql"]
 oracle = ["watchmen-storage-oracle"]
 mongodb = ["watchmen-storage-mongodb"]
```

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/common/settings.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/common/settings.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/achievement_data_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/achievement_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/achievement_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/bucket_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/bucket_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/indicator_criteria_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_criteria_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/indicator_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/indicator_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/inspection_data_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/inspection_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/inspection_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_base_achievement_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_achievement_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_base_inspection_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/subject_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/subject_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_base_achievement_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_achievement_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_base_inspection_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/data/topic_helper.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/data/topic_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/achievement_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/achievement_task_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/achievement_task_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/bucket_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/bucket_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/indicator_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/indicator_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/inspection_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/inspection_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/meta/objective_analysis_service.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/meta/objective_analysis_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/src/watchmen_indicator_kernel/plugin/connector.py` & `watchmen_indicator_kernel-16.4.9/src/watchmen_indicator_kernel/plugin/connector.py`

 * *Files identical despite different names*

### Comparing `watchmen_indicator_kernel-16.4.7/setup.py` & `watchmen_indicator_kernel-16.4.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -11,29 +11,29 @@
  'watchmen_indicator_kernel.meta',
  'watchmen_indicator_kernel.plugin']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-inquiry-kernel==16.4.7']
+['watchmen-inquiry-kernel==16.4.9']
 
 extras_require = \
-{'mongodb': ['watchmen-storage-mongodb==16.4.7'],
- 'mssql': ['watchmen-storage-mssql==16.4.7'],
- 'mysql': ['watchmen-storage-mysql==16.4.7'],
- 'oracle': ['watchmen-storage-oracle==16.4.7'],
- 'oss': ['watchmen-storage-oss==16.4.7'],
- 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
- 's3': ['watchmen-storage-s3==16.4.7'],
- 'trino': ['watchmen-inquiry-trino==16.4.7']}
+{'mongodb': ['watchmen-storage-mongodb==16.4.9'],
+ 'mssql': ['watchmen-storage-mssql==16.4.9'],
+ 'mysql': ['watchmen-storage-mysql==16.4.9'],
+ 'oracle': ['watchmen-storage-oracle==16.4.9'],
+ 'oss': ['watchmen-storage-oss==16.4.9'],
+ 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
+ 's3': ['watchmen-storage-s3==16.4.9'],
+ 'trino': ['watchmen-inquiry-trino==16.4.9']}
 
 setup_kwargs = {
     'name': 'watchmen-indicator-kernel',
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

### Comparing `watchmen_indicator_kernel-16.4.7/PKG-INFO` & `watchmen_indicator_kernel-16.4.9/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-indicator-kernel
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -15,16 +15,16 @@
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
 Provides-Extra: trino
-Requires-Dist: watchmen-inquiry-kernel (==16.4.7)
-Requires-Dist: watchmen-inquiry-trino (==16.4.7) ; extra == "trino"
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.7) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.7) ; extra == "s3"
+Requires-Dist: watchmen-inquiry-kernel (==16.4.9)
+Requires-Dist: watchmen-inquiry-trino (==16.4.9) ; extra == "trino"
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
```

