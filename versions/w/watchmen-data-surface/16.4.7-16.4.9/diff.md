# Comparing `tmp/watchmen_data_surface-16.4.7.tar.gz` & `tmp/watchmen_data_surface-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_data_surface-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_data_surface-16.4.9.tar", max compression
```

## Comparing `watchmen_data_surface-16.4.7.tar` & `watchmen_data_surface-16.4.9.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/LICENSE
--rw-r--r--   0        0        0     1195 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/pyproject.toml
--rw-r--r--   0        0        0       43 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/__init__.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/cache/__init__.py
--rw-r--r--   0        0        0     2237 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/cache/cache_router.py
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/data/__init__.py
--rw-r--r--   0        0        0     9814 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/data/topic_data_router.py
--rw-r--r--   0        0        0      240 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/main.py
--rw-r--r--   0        0        0      462 2023-01-18 10:06:03.430851 watchmen_data_surface-16.4.7/src/watchmen_data_surface/settings.py
--rw-r--r--   0        0        0     1185 1970-01-01 00:00:00.000000 watchmen_data_surface-16.4.7/setup.py
--rw-r--r--   0        0        0     1171 1970-01-01 00:00:00.000000 watchmen_data_surface-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.976775 watchmen_data_surface-16.4.9/LICENSE
+-rw-r--r--   0        0        0     1195 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0       43 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/cache/__init__.py
+-rw-r--r--   0        0        0     2237 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/cache/cache_router.py
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/data/__init__.py
+-rw-r--r--   0        0        0     9814 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/data/topic_data_router.py
+-rw-r--r--   0        0        0      240 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/main.py
+-rw-r--r--   0        0        0      462 2023-02-23 10:23:45.980775 watchmen_data_surface-16.4.9/src/watchmen_data_surface/settings.py
+-rw-r--r--   0        0        0     1185 1970-01-01 00:00:00.000000 watchmen_data_surface-16.4.9/setup.py
+-rw-r--r--   0        0        0     1171 1970-01-01 00:00:00.000000 watchmen_data_surface-16.4.9/PKG-INFO
```

### Comparing `watchmen_data_surface-16.4.7/LICENSE` & `watchmen_data_surface-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_data_surface-16.4.7/pyproject.toml` & `watchmen_data_surface-16.4.9/pyproject.toml`

 * *Files 15% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 [tool.poetry]
 name = "watchmen-data-surface"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_data_surface", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-data-kernel = "16.4.7"
-watchmen-rest = "16.4.7"
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-storage-oss = { version = "16.4.7", optional = true }
-watchmen-storage-s3 = { version = "16.4.7", optional = true }
+watchmen-data-kernel = "16.4.9"
+watchmen-rest = "16.4.9"
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

### Comparing `watchmen_data_surface-16.4.7/src/watchmen_data_surface/cache/cache_router.py` & `watchmen_data_surface-16.4.9/src/watchmen_data_surface/cache/cache_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_data_surface-16.4.7/src/watchmen_data_surface/data/topic_data_router.py` & `watchmen_data_surface-16.4.9/src/watchmen_data_surface/data/topic_data_router.py`

 * *Files identical despite different names*

### Comparing `watchmen_data_surface-16.4.7/setup.py` & `watchmen_data_surface-16.4.9/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -9,28 +9,28 @@
  'watchmen_data_surface.cache',
  'watchmen_data_surface.data']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-data-kernel==16.4.7', 'watchmen-rest==16.4.7']
+['watchmen-data-kernel==16.4.9', 'watchmen-rest==16.4.9']
 
 extras_require = \
-{'mongodb': ['watchmen-storage-mongodb==16.4.7'],
- 'mssql': ['watchmen-storage-mssql==16.4.7'],
- 'mysql': ['watchmen-storage-mysql==16.4.7'],
- 'oracle': ['watchmen-storage-oracle==16.4.7'],
- 'oss': ['watchmen-storage-oss==16.4.7'],
- 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
- 's3': ['watchmen-storage-s3==16.4.7']}
+{'mongodb': ['watchmen-storage-mongodb==16.4.9'],
+ 'mssql': ['watchmen-storage-mssql==16.4.9'],
+ 'mysql': ['watchmen-storage-mysql==16.4.9'],
+ 'oracle': ['watchmen-storage-oracle==16.4.9'],
+ 'oss': ['watchmen-storage-oss==16.4.9'],
+ 'postgresql': ['watchmen-storage-postgresql==16.4.9'],
+ 's3': ['watchmen-storage-s3==16.4.9']}
 
 setup_kwargs = {
     'name': 'watchmen-data-surface',
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

### Comparing `watchmen_data_surface-16.4.7/PKG-INFO` & `watchmen_data_surface-16.4.9/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-data-surface
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
@@ -14,16 +14,16 @@
 Provides-Extra: mongodb
 Provides-Extra: mssql
 Provides-Extra: mysql
 Provides-Extra: oracle
 Provides-Extra: oss
 Provides-Extra: postgresql
 Provides-Extra: s3
-Requires-Dist: watchmen-data-kernel (==16.4.7)
-Requires-Dist: watchmen-rest (==16.4.7)
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.7) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.7) ; extra == "s3"
+Requires-Dist: watchmen-data-kernel (==16.4.9)
+Requires-Dist: watchmen-rest (==16.4.9)
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
```

