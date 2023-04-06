# Comparing `tmp/watchmen_rest_dqc-16.4.7.tar.gz` & `tmp/watchmen_rest_dqc-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_rest_dqc-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_rest_dqc-16.4.9.tar", max compression
```

## Comparing `watchmen_rest_dqc-16.4.7.tar` & `watchmen_rest_dqc-16.4.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/LICENSE
--rw-r--r--   0        0        0     1331 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/pyproject.toml
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/__init__.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/admin/__init__.py
--rw-r--r--   0        0        0     5943 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/admin/catalog_router.py
--rw-r--r--   0        0        0     3051 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/admin/monitor_rules_router.py
--rw-r--r--   0        0        0      861 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/dqc.py
--rw-r--r--   0        0        0      544 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/main.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/monitor/__init__.py
--rw-r--r--   0        0        0     5292 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/monitor/topic_monitor_router.py
--rw-r--r--   0        0        0      106 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/settings.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/topic_profile/__init__.py
--rw-r--r--   0        0        0     1289 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/topic_profile/topic_profile_router.py
--rw-r--r--   0        0        0       80 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/util/__init__.py
--rw-r--r--   0        0        0     2068 2023-01-18 10:06:03.450851 watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/util/trans.py
--rw-r--r--   0        0        0     1264 1970-01-01 00:00:00.000000 watchmen_rest_dqc-16.4.7/setup.py
--rw-r--r--   0        0        0     1240 1970-01-01 00:00:00.000000 watchmen_rest_dqc-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/LICENSE
+-rw-r--r--   0        0        0     1331 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/admin/__init__.py
+-rw-r--r--   0        0        0     5943 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/admin/catalog_router.py
+-rw-r--r--   0        0        0     3051 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/admin/monitor_rules_router.py
+-rw-r--r--   0        0        0      861 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/dqc.py
+-rw-r--r--   0        0        0      544 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/main.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/monitor/__init__.py
+-rw-r--r--   0        0        0     5292 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/monitor/topic_monitor_router.py
+-rw-r--r--   0        0        0      106 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/settings.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/topic_profile/__init__.py
+-rw-r--r--   0        0        0     1289 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/topic_profile/topic_profile_router.py
+-rw-r--r--   0        0        0       80 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/util/__init__.py
+-rw-r--r--   0        0        0     2068 2023-02-23 10:23:46.000775 watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/util/trans.py
+-rw-r--r--   0        0        0     1264 1970-01-01 00:00:00.000000 watchmen_rest_dqc-16.4.9/setup.py
+-rw-r--r--   0        0        0     1240 1970-01-01 00:00:00.000000 watchmen_rest_dqc-16.4.9/PKG-INFO
```

### Comparing `watchmen_rest_dqc-16.4.7/LICENSE` & `watchmen_rest_dqc-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/pyproject.toml` & `watchmen_rest_dqc-16.4.9/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,29 +1,29 @@
 [tool.poetry]
 name = "watchmen-rest-dqc"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_rest_dqc", from = "src" }
 ]
 
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-dqc = "16.4.7"
-watchmen-rest = "16.4.7"
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-storage-oss = { version = "16.4.7", optional = true }
-watchmen-storage-s3 = { version = "16.4.7", optional = true }
+watchmen-dqc = "16.4.9"
+watchmen-rest = "16.4.9"
+watchmen-storage-mysql = { version = "16.4.9", optional = true }
+watchmen-storage-oracle = { version = "16.4.9", optional = true }
+watchmen-storage-mongodb = { version = "16.4.9", optional = true }
+watchmen-storage-mssql = { version = "16.4.9", optional = true }
+watchmen-storage-postgresql = { version = "16.4.9", optional = true }
+watchmen-storage-oss = { version = "16.4.9", optional = true }
+watchmen-storage-s3 = { version = "16.4.9", optional = true }
 boto3 = {version = "^1.24.20", optional = true }
 
 [tool.poetry.dev-dependencies]
 
 [tool.poetry.extras]
 mysql = ["watchmen-storage-mysql"]
 oracle = ["watchmen-storage-oracle"]
```

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/admin/catalog_router.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/admin/catalog_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/admin/monitor_rules_router.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/admin/monitor_rules_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/dqc.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/dqc.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/main.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/main.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/monitor/topic_monitor_router.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/monitor/topic_monitor_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/topic_profile/topic_profile_router.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/topic_profile/topic_profile_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/src/watchmen_rest_dqc/util/trans.py` & `watchmen_rest_dqc-16.4.9/src/watchmen_rest_dqc/util/trans.py`

 * *Files identical despite different names*

### Comparing `watchmen_rest_dqc-16.4.7/setup.py` & `watchmen_rest_dqc-16.4.9/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -11,29 +11,29 @@
  'watchmen_rest_dqc.topic_profile',
  'watchmen_rest_dqc.util']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-dqc==16.4.7', 'watchmen-rest==16.4.7']
+['watchmen-dqc==16.4.9', 'watchmen-rest==16.4.9']
 
 extras_require = \
 {'boto3': ['boto3>=1.24.20,<2.0.0'],
- 'mongodb': ['watchmen-storage-mongodb==16.4.7'],
- 'mssql': ['watchmen-storage-mssql==16.4.7'],
- 'mysql': ['watchmen-storage-mysql==16.4.7'],
- 'oracle': ['watchmen-storage-oracle==16.4.7'],
- 'oss': ['watchmen-storage-oss==16.4.7'],
- 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
- 's3': ['watchmen-storage-s3==16.4.7']}
+ 'mongodb': ['watchmen-storage-mongodb==16.4.9'],
+ 'mssql': ['watchmen-storage-mssql==16.4.9'],
+ 'mysql': ['watchmen-storage-mysql==16.4.9'],
+ 'oracle': ['watchmen-storage-oracle==16.4.9'],
+ 'oss': ['watchmen-storage-oss==16.4.9'],
+ 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
+ 's3': ['watchmen-storage-s3==16.4.9']}
 
 setup_kwargs = {
     'name': 'watchmen-rest-dqc',
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

### Comparing `watchmen_rest_dqc-16.4.7/PKG-INFO` & `watchmen_rest_dqc-16.4.9/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-rest-dqc
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -16,16 +16,16 @@
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
 Requires-Dist: boto3 (>=1.24.20,<2.0.0) ; extra == "boto3"
-Requires-Dist: watchmen-dqc (==16.4.7)
-Requires-Dist: watchmen-rest (==16.4.7)
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.7) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.7) ; extra == "s3"
+Requires-Dist: watchmen-dqc (==16.4.9)
+Requires-Dist: watchmen-rest (==16.4.9)
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
```

