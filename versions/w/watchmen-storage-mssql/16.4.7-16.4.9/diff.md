# Comparing `tmp/watchmen_storage_mssql-16.4.7.tar.gz` & `tmp/watchmen_storage_mssql-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_mssql-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_storage_mssql-16.4.9.tar", max compression
```

## Comparing `watchmen_storage_mssql-16.4.7.tar` & `watchmen_storage_mssql-16.4.9.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.454851 watchmen_storage_mssql-16.4.7/LICENSE
--rw-r--r--   0        0        0      460 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      259 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/__init__.py
--rw-r--r--   0        0        0     2294 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/data_source_mssql.py
--rw-r--r--   0        0        0     2450 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/script_builder_mssql.py
--rw-r--r--   0        0        0     7773 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/storage_mssql.py
--rw-r--r--   0        0        0     2085 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/storage_mssql_configuration.py
--rw-r--r--   0        0        0     7971 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/table_creator.py
--rw-r--r--   0        0        0    12465 2023-01-18 10:06:03.458851 watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/where_build.py
--rw-r--r--   0        0        0      738 1970-01-01 00:00:00.000000 watchmen_storage_mssql-16.4.7/setup.py
--rw-r--r--   0        0        0      533 1970-01-01 00:00:00.000000 watchmen_storage_mssql-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.004776 watchmen_storage_mssql-16.4.9/LICENSE
+-rw-r--r--   0        0        0      460 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      259 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/__init__.py
+-rw-r--r--   0        0        0     2294 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/data_source_mssql.py
+-rw-r--r--   0        0        0     2450 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/script_builder_mssql.py
+-rw-r--r--   0        0        0     7773 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/storage_mssql.py
+-rw-r--r--   0        0        0     2085 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/storage_mssql_configuration.py
+-rw-r--r--   0        0        0     7971 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/table_creator.py
+-rw-r--r--   0        0        0    12465 2023-02-23 10:23:46.008776 watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/where_build.py
+-rw-r--r--   0        0        0      738 1970-01-01 00:00:00.000000 watchmen_storage_mssql-16.4.9/setup.py
+-rw-r--r--   0        0        0      533 1970-01-01 00:00:00.000000 watchmen_storage_mssql-16.4.9/PKG-INFO
```

### Comparing `watchmen_storage_mssql-16.4.7/LICENSE` & `watchmen_storage_mssql-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/data_source_mssql.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/data_source_mssql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/script_builder_mssql.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/script_builder_mssql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/storage_mssql.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/storage_mssql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/storage_mssql_configuration.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/storage_mssql_configuration.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/table_creator.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/table_creator.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/src/watchmen_storage_mssql/where_build.py` & `watchmen_storage_mssql-16.4.9/src/watchmen_storage_mssql/where_build.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mssql-16.4.7/setup.py` & `watchmen_storage_mssql-16.4.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 packages = \
 ['watchmen_storage_mssql']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['pyodbc>=4.0.32,<5.0.0', 'watchmen-storage-rds==16.4.7']
+['pyodbc>=4.0.32,<5.0.0', 'watchmen-storage-rds==16.4.9']
 
 setup_kwargs = {
     'name': 'watchmen-storage-mssql',
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

### Comparing `watchmen_storage_mssql-16.4.7/PKG-INFO` & `watchmen_storage_mssql-16.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-mssql
-Version: 16.4.7
+Version: 16.4.9
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
 Requires-Dist: pyodbc (>=4.0.32,<5.0.0)
-Requires-Dist: watchmen-storage-rds (==16.4.7)
+Requires-Dist: watchmen-storage-rds (==16.4.9)
```

