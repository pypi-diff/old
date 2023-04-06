# Comparing `tmp/watchmen_utilities-16.4.7.tar.gz` & `tmp/watchmen_utilities-16.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "watchmen_utilities-16.4.7.tar", max compression
+gzip compressed data, was "watchmen_utilities-16.4.9.tar", max compression
```

## Comparing `watchmen_utilities-16.4.7.tar` & `watchmen_utilities-16.4.9.tar`

### file list

```diff
@@ -1,11 +1,11 @@
--rw-r--r--   0        0        0      451 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/pyproject.toml
--rw-r--r--   0        0        0     1009 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/__init__.py
--rw-r--r--   0        0        0     5679 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/array_helper.py
--rw-r--r--   0        0        0    20357 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/datetime_helper.py
--rw-r--r--   0        0        0      188 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/json_helper.py
--rw-r--r--   0        0        0     2143 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/logger.py
--rw-r--r--   0        0        0      922 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/numeric_helper.py
--rw-r--r--   0        0        0      352 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/string_helper.py
--rw-r--r--   0        0        0     8884 2023-01-18 10:06:03.470851 watchmen_utilities-16.4.7/src/watchmen_utilities/value_expression.py
--rw-r--r--   0        0        0      735 1970-01-01 00:00:00.000000 watchmen_utilities-16.4.7/setup.py
--rw-r--r--   0        0        0      534 1970-01-01 00:00:00.000000 watchmen_utilities-16.4.7/PKG-INFO
+-rw-r--r--   0        0        0      451 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/pyproject.toml
+-rw-r--r--   0        0        0     1009 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/__init__.py
+-rw-r--r--   0        0        0     5679 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/array_helper.py
+-rw-r--r--   0        0        0    20357 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/datetime_helper.py
+-rw-r--r--   0        0        0      188 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/json_helper.py
+-rw-r--r--   0        0        0     2143 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/logger.py
+-rw-r--r--   0        0        0      922 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/numeric_helper.py
+-rw-r--r--   0        0        0      352 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/string_helper.py
+-rw-r--r--   0        0        0     8884 2023-02-23 10:23:46.020776 watchmen_utilities-16.4.9/src/watchmen_utilities/value_expression.py
+-rw-r--r--   0        0        0      735 1970-01-01 00:00:00.000000 watchmen_utilities-16.4.9/setup.py
+-rw-r--r--   0        0        0      534 1970-01-01 00:00:00.000000 watchmen_utilities-16.4.9/PKG-INFO
```

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/__init__.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/__init__.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/array_helper.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/array_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/datetime_helper.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/datetime_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/logger.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/logger.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/numeric_helper.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/numeric_helper.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/src/watchmen_utilities/value_expression.py` & `watchmen_utilities-16.4.9/src/watchmen_utilities/value_expression.py`

 * *Files identical despite different names*

### Comparing `watchmen_utilities-16.4.7/setup.py` & `watchmen_utilities-16.4.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 {'': ['*']}
 
 install_requires = \
 ['pydantic>=1.9.0,<2.0.0', 'python-json-logger>=2.0.2,<3.0.0']
 
 setup_kwargs = {
     'name': 'watchmen-utilities',
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

### Comparing `watchmen_utilities-16.4.7/PKG-INFO` & `watchmen_utilities-16.4.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: watchmen-utilities
-Version: 16.4.7
+Version: 16.4.9
 Summary: 
 License: MIT
 Author: botlikes
 Author-email: 75356972+botlikes456@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

