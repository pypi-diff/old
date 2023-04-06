# Comparing `tmp/watchmen_storage_mongodb-16.4.7.tar.gz` & `tmp/watchmen_storage_mongodb-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_storage_mongodb-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_storage_mongodb-16.4.9.tar", max compression
```

## Comparing `watchmen_storage_mongodb-16.4.7.tar` & `watchmen_storage_mongodb-16.4.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
--rw-r--r--   0        0        0     1061 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/LICENSE
--rw-r--r--   0        0        0      460 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/pyproject.toml
--rw-r--r--   0        0        0      210 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/__init__.py
--rw-r--r--   0        0        0      703 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/codes_options.py
--rw-r--r--   0        0        0     1308 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/data_source_mongo.py
--rw-r--r--   0        0        0     2540 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_defs_helper.py
--rw-r--r--   0        0        0    16846 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_defs_mongo.py
--rw-r--r--   0        0        0     2541 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_mongo.py
--rw-r--r--   0        0        0     5220 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/engine_mongo.py
--rw-r--r--   0        0        0      509 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/sort_build.py
--rw-r--r--   0        0        0    21084 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/storage_mongo.py
--rw-r--r--   0        0        0     1899 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/storage_mongo_configuration.py
--rw-r--r--   0        0        0    11657 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/topic_document_generate.py
--rw-r--r--   0        0        0    24666 2023-01-18 10:06:03.454851 watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/where_build.py
--rw-r--r--   0        0        0      738 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.7/setup.py
--rw-r--r--   0        0        0      531 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1061 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/LICENSE
+-rw-r--r--   0        0        0      460 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0      210 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/__init__.py
+-rw-r--r--   0        0        0      703 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/codes_options.py
+-rw-r--r--   0        0        0     1308 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/data_source_mongo.py
+-rw-r--r--   0        0        0     2540 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_helper.py
+-rw-r--r--   0        0        0    16846 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_mongo.py
+-rw-r--r--   0        0        0     2541 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_mongo.py
+-rw-r--r--   0        0        0     5220 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/engine_mongo.py
+-rw-r--r--   0        0        0      509 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/sort_build.py
+-rw-r--r--   0        0        0    21084 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo.py
+-rw-r--r--   0        0        0     1899 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo_configuration.py
+-rw-r--r--   0        0        0    11657 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/topic_document_generate.py
+-rw-r--r--   0        0        0    24666 2023-02-23 10:23:46.004776 watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/where_build.py
+-rw-r--r--   0        0        0      738 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.9/setup.py
+-rw-r--r--   0        0        0      531 1970-01-01 00:00:00.000000 watchmen_storage_mongodb-16.4.9/PKG-INFO
```

### Comparing `watchmen_storage_mongodb-16.4.7/LICENSE` & `watchmen_storage_mongodb-16.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/codes_options.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/codes_options.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/data_source_mongo.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/data_source_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_defs_helper.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_defs_mongo.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_defs_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/document_mongo.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/document_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/engine_mongo.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/engine_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/storage_mongo.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/storage_mongo_configuration.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/storage_mongo_configuration.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/topic_document_generate.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/topic_document_generate.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/src/watchmen_storage_mongodb/where_build.py` & `watchmen_storage_mongodb-16.4.9/src/watchmen_storage_mongodb/where_build.py`

 * *Files identical despite different names*

### Comparing `watchmen_storage_mongodb-16.4.7/setup.py` & `watchmen_storage_mongodb-16.4.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,19 +7,19 @@
 packages = \
 ['watchmen_storage_mongodb']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['pymongo>=4.1.0,<5.0.0', 'watchmen-storage==16.4.7']
+['pymongo>=4.1.0,<5.0.0', 'watchmen-storage==16.4.9']
 
 setup_kwargs = {
     'name': 'watchmen-storage-mongodb',
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

### Comparing `watchmen_storage_mongodb-16.4.7/PKG-INFO` & `watchmen_storage_mongodb-16.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: watchmen-storage-mongodb
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
 Requires-Dist: pymongo (>=4.1.0,<5.0.0)
-Requires-Dist: watchmen-storage (==16.4.7)
+Requires-Dist: watchmen-storage (==16.4.9)
```

