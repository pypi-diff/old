# Comparing `tmp/watchmen_inquiry_kernel-16.4.7.tar.gz` & `tmp/watchmen_inquiry_kernel-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_inquiry_kernel-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_inquiry_kernel-16.4.9.tar", max compression
```

## Comparing `watchmen_inquiry_kernel-16.4.7.tar` & `watchmen_inquiry_kernel-16.4.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/LICENSE
--rw-r--r--   0        0        0     1274 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/pyproject.toml
--rw-r--r--   0        0        0        0 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/__init__.py
--rw-r--r--   0        0        0      112 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/common/__init__.py
--rw-r--r--   0        0        0       47 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/common/exception.py
--rw-r--r--   0        0        0      620 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/common/settings.py
--rw-r--r--   0        0        0       86 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/meta/__init__.py
--rw-r--r--   0        0        0     1404 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/meta/report_service.py
--rw-r--r--   0        0        0     2358 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/meta/subject_service.py
--rw-r--r--   0        0        0       82 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/schema/__init__.py
--rw-r--r--   0        0        0     2178 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/schema/report_schema.py
--rw-r--r--   0        0        0    12544 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/schema/subject_schema.py
--rw-r--r--   0        0        0      104 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/__init__.py
--rw-r--r--   0        0        0     1544 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/report_data_service.py
--rw-r--r--   0        0        0     1228 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/subject_data_service.py
--rw-r--r--   0        0        0    53232 2023-01-18 10:06:03.434851 watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/subject_storage.py
--rw-r--r--   0        0        0     1286 1970-01-01 00:00:00.000000 watchmen_inquiry_kernel-16.4.7/setup.py
--rw-r--r--   0        0        0     1223 1970-01-01 00:00:00.000000 watchmen_inquiry_kernel-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/LICENSE
+-rw-r--r--   0        0        0     1274 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/__init__.py
+-rw-r--r--   0        0        0      112 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/common/__init__.py
+-rw-r--r--   0        0        0       47 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/common/exception.py
+-rw-r--r--   0        0        0      620 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/common/settings.py
+-rw-r--r--   0        0        0       86 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/meta/__init__.py
+-rw-r--r--   0        0        0     1404 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/meta/report_service.py
+-rw-r--r--   0        0        0     2358 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/meta/subject_service.py
+-rw-r--r--   0        0        0       82 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/schema/__init__.py
+-rw-r--r--   0        0        0     2178 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/schema/report_schema.py
+-rw-r--r--   0        0        0    12544 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/schema/subject_schema.py
+-rw-r--r--   0        0        0      104 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/__init__.py
+-rw-r--r--   0        0        0     1544 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/report_data_service.py
+-rw-r--r--   0        0        0     1228 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/subject_data_service.py
+-rw-r--r--   0        0        0    53232 2023-02-23 10:23:45.984775 watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/subject_storage.py
+-rw-r--r--   0        0        0     1286 1970-01-01 00:00:00.000000 watchmen_inquiry_kernel-16.4.9/setup.py
+-rw-r--r--   0        0        0     1223 1970-01-01 00:00:00.000000 watchmen_inquiry_kernel-16.4.9/PKG-INFO
```

### Comparing `watchmen_inquiry_kernel-16.4.7/LICENSE` & `watchmen_inquiry_kernel-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/pyproject.toml` & `watchmen_inquiry_kernel-16.4.9/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 [tool.poetry]
 name = "watchmen-inquiry-kernel"
-version = "16.4.7"
+version = "16.4.9"
 description = ""
 authors = ["botlikes <75356972+botlikes456@users.noreply.github.com>"]
 license = "MIT"
 packages = [
     { include = "watchmen_inquiry_kernel", from = "src" }
 ]
 
 [tool.poetry.dependencies]
 python = "^3.9"
-watchmen-data-kernel = "16.4.7"
-watchmen-inquiry-trino = { version = "16.4.7", optional = true }
-watchmen-storage-mysql = { version = "16.4.7", optional = true }
-watchmen-storage-oracle = { version = "16.4.7", optional = true }
-watchmen-storage-mongodb = { version = "16.4.7", optional = true }
-watchmen-storage-mssql = { version = "16.4.7", optional = true }
-watchmen-storage-postgresql = { version = "16.4.7", optional = true }
-watchmen-storage-oss = { version = "16.4.7", optional = true }
-watchmen-storage-s3 = { version = "16.4.7", optional = true }
+watchmen-data-kernel = "16.4.9"
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

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/common/settings.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/common/settings.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/meta/report_service.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/meta/report_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/meta/subject_service.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/meta/subject_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/schema/report_schema.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/schema/report_schema.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/schema/subject_schema.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/schema/subject_schema.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/report_data_service.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/report_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/subject_data_service.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/subject_data_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/src/watchmen_inquiry_kernel/storage/subject_storage.py` & `watchmen_inquiry_kernel-16.4.9/src/watchmen_inquiry_kernel/storage/subject_storage.py`

 * *Files identical despite different names*

### Comparing `watchmen_inquiry_kernel-16.4.7/setup.py` & `watchmen_inquiry_kernel-16.4.9/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -11,29 +11,29 @@
  'watchmen_inquiry_kernel.schema',
  'watchmen_inquiry_kernel.storage']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['watchmen-data-kernel==16.4.7']
+['watchmen-data-kernel==16.4.9']
 
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
     'name': 'watchmen-inquiry-kernel',
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

### Comparing `watchmen_inquiry_kernel-16.4.7/PKG-INFO` & `watchmen_inquiry_kernel-16.4.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-inquiry-kernel
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
-Requires-Dist: watchmen-data-kernel (==16.4.7)
-Requires-Dist: watchmen-inquiry-trino (==16.4.7) ; extra == "trino"
-Requires-Dist: watchmen-storage-mongodb (==16.4.7) ; extra == "mongodb"
-Requires-Dist: watchmen-storage-mssql (==16.4.7) ; extra == "mssql"
-Requires-Dist: watchmen-storage-mysql (==16.4.7) ; extra == "mysql"
-Requires-Dist: watchmen-storage-oracle (==16.4.7) ; extra == "oracle"
-Requires-Dist: watchmen-storage-oss (==16.4.7) ; extra == "oss"
-Requires-Dist: watchmen-storage-postgresql (==16.4.7) ; extra == "postgresql"
-Requires-Dist: watchmen-storage-s3 (==16.4.7) ; extra == "s3"
+Requires-Dist: watchmen-data-kernel (==16.4.9)
+Requires-Dist: watchmen-inquiry-trino (==16.4.9) ; extra == "trino"
+Requires-Dist: watchmen-storage-mongodb (==16.4.9) ; extra == "mongodb"
+Requires-Dist: watchmen-storage-mssql (==16.4.9) ; extra == "mssql"
+Requires-Dist: watchmen-storage-mysql (==16.4.9) ; extra == "mysql"
+Requires-Dist: watchmen-storage-oracle (==16.4.9) ; extra == "oracle"
+Requires-Dist: watchmen-storage-oss (==16.4.9) ; extra == "oss"
+Requires-Dist: watchmen-storage-postgresql (==16.4.9) ; extra == "postgresql"
+Requires-Dist: watchmen-storage-s3 (==16.4.9) ; extra == "s3"
```

