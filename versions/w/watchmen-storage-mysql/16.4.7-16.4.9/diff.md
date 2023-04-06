# Comparing `tmp/watchmen_storage_mysql-16.4.7.tar.gz` & `tmp/watchmen_storage_mysql-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_mysql-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_storage_mysql-16.4.9.tar", max compression
```

## Comparing `watchmen_storage_mysql-16.4.7.tar` & `watchmen_storage_mysql-16.4.9.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/LICENSE
--rw-r--r--   0        0        0      485 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      258 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/__init__.py
--rw-r--r--   0        0        0     2836 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/data_source_mysql.py
--rw-r--r--   0        0        0     2197 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/script_builder_mysql.py
--rw-r--r--   0        0        0     5301 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/storage_mysql.py
--rw-r--r--   0        0        0     1965 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/storage_mysql_configuration.py
--rw-r--r--   0        0        0     8699 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/table_creator.py
--rw-r--r--   0        0        0    11939 2023-01-18 10:06:03.458851 watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/where_build.py
--rw-r--r--   0        0        0      772 1970-01-01 00:00:00.000000 watchmen_storage_mysql-16.4.7/setup.py
--rw-r--r--   0        0        0      580 1970-01-01 00:00:00.000000 watchmen_storage_mysql-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.008776 watchmen_storage_mysql-16.4.9/LICENSE
+-rw-r--r--   0        0        0      485 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      258 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/__init__.py
+-rw-r--r--   0        0        0     2836 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/data_source_mysql.py
+-rw-r--r--   0        0        0     2197 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/script_builder_mysql.py
+-rw-r--r--   0        0        0     5301 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/storage_mysql.py
+-rw-r--r--   0        0        0     1965 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/storage_mysql_configuration.py
+-rw-r--r--   0        0        0     8699 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/table_creator.py
+-rw-r--r--   0        0        0    11939 2023-02-23 10:23:46.012776 watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/where_build.py
+-rw-r--r--   0        0        0      772 1970-01-01 00:00:00.000000 watchmen_storage_mysql-16.4.9/setup.py
+-rw-r--r--   0        0        0      580 1970-01-01 00:00:00.000000 watchmen_storage_mysql-16.4.9/PKG-INFO
```

### Comparing `watchmen_storage_mysql-16.4.7/LICENSE` & `watchmen_storage_mysql-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/data_source_mysql.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/data_source_mysql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/script_builder_mysql.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/script_builder_mysql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/storage_mysql.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/storage_mysql.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/storage_mysql_configuration.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/storage_mysql_configuration.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/table_creator.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/table_creator.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/src/watchmen_storage_mysql/where_build.py` & `watchmen_storage_mysql-16.4.9/src/watchmen_storage_mysql/where_build.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mysql-16.4.7/setup.py` & `watchmen_storage_mysql-16.4.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,19 +9,19 @@
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
 ['PyMySQL>=1.0.2,<2.0.0',
  'cryptography>=36.0.2,<37.0.0',
- 'watchmen-storage-rds==16.4.7']
+ 'watchmen-storage-rds==16.4.9']
 
 setup_kwargs = {
     'name': 'watchmen-storage-mysql',
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

### Comparing `watchmen_storage_mysql-16.4.7/PKG-INFO` & `watchmen_storage_mysql-16.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-mysql
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
 Requires-Dist: PyMySQL (>=1.0.2,<2.0.0)
 Requires-Dist: cryptography (>=36.0.2,<37.0.0)
-Requires-Dist: watchmen-storage-rds (==16.4.7)
+Requires-Dist: watchmen-storage-rds (==16.4.9)
```

