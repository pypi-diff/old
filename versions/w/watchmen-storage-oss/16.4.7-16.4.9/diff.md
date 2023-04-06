# Comparing `tmp/watchmen_storage_oss-16.4.7.tar.gz` & `tmp/watchmen_storage_oss-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_oss-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_storage_oss-16.4.9.tar", max compression
```

## Comparing `watchmen_storage_oss-16.4.7.tar` & `watchmen_storage_oss-16.4.9.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/LICENSE
--rw-r--r--   0        0        0      449 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      112 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/__init__.py
--rw-r--r--   0        0        0     1299 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/data_source_oss.py
--rw-r--r--   0        0        0      495 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/object_defs_oss.py
--rw-r--r--   0        0        0     1657 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/object_storage_service.py
--rw-r--r--   0        0        0     8903 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/storage_oss.py
--rw-r--r--   0        0        0     1836 2023-01-18 10:06:03.462851 watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/storage_oss_configuration.py
--rw-r--r--   0        0        0      721 1970-01-01 00:00:00.000000 watchmen_storage_oss-16.4.7/setup.py
--rw-r--r--   0        0        0      518 1970-01-01 00:00:00.000000 watchmen_storage_oss-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/LICENSE
+-rw-r--r--   0        0        0      449 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      112 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/__init__.py
+-rw-r--r--   0        0        0     1299 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/data_source_oss.py
+-rw-r--r--   0        0        0      495 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/object_defs_oss.py
+-rw-r--r--   0        0        0     1657 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/object_storage_service.py
+-rw-r--r--   0        0        0     8903 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/storage_oss.py
+-rw-r--r--   0        0        0     1836 2023-02-23 10:23:46.012776 watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/storage_oss_configuration.py
+-rw-r--r--   0        0        0      721 1970-01-01 00:00:00.000000 watchmen_storage_oss-16.4.9/setup.py
+-rw-r--r--   0        0        0      518 1970-01-01 00:00:00.000000 watchmen_storage_oss-16.4.9/PKG-INFO
```

### Comparing `watchmen_storage_oss-16.4.7/LICENSE` & `watchmen_storage_oss-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/data_source_oss.py` & `watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/data_source_oss.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/object_storage_service.py` & `watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/object_storage_service.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/storage_oss.py` & `watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/storage_oss.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_oss-16.4.7/src/watchmen_storage_oss/storage_oss_configuration.py` & `watchmen_storage_oss-16.4.9/src/watchmen_storage_oss/storage_oss_configuration.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_oss-16.4.7/setup.py` & `watchmen_storage_oss-16.4.9/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 packages = \
 ['watchmen_storage_oss']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['oss2==2.15.0', 'watchmen-storage==16.4.7']
+['oss2==2.15.0', 'watchmen-storage==16.4.9']
 
 setup_kwargs = {
     'name': 'watchmen-storage-oss',
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

### Comparing `watchmen_storage_oss-16.4.7/PKG-INFO` & `watchmen_storage_oss-16.4.9/PKG-INFO`

 * *Files 22% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-oss
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
 Requires-Dist: oss2 (==2.15.0)
-Requires-Dist: watchmen-storage (==16.4.7)
+Requires-Dist: watchmen-storage (==16.4.9)
```

