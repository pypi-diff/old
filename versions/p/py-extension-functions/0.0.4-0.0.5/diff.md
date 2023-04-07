# Comparing `tmp/py_extension_functions-0.0.4.tar.gz` & `tmp/py_extension_functions-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "py_extension_functions-0.0.4.tar", last modified: Sun Mar 19 10:46:32 2023, max compression
+gzip compressed data, was "py_extension_functions-0.0.5.tar", last modified: Fri Apr  7 04:15:20 2023, max compression
```

## Comparing `py_extension_functions-0.0.4.tar` & `py_extension_functions-0.0.5.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:32.747471 py_extension_functions-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)     2072 2023-03-19 10:46:32.747471 py_extension_functions-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1577 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:32.743471 py_extension_functions-0.0.4/gpp/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/algorithms.py
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/datetimes.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4464 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/geometry.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/loggers.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/networks.py
--rw-r--r--   0 runner    (1001) docker     (123)    11735 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/gpp/texts.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:32.743471 py_extension_functions-0.0.4/py_extension_functions.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2072 2023-03-19 10:46:32.000000 py_extension_functions-0.0.4/py_extension_functions.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      611 2023-03-19 10:46:32.000000 py_extension_functions-0.0.4/py_extension_functions.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-19 10:46:32.000000 py_extension_functions-0.0.4/py_extension_functions.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-03-19 10:46:32.000000 py_extension_functions-0.0.4/py_extension_functions.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-19 10:46:32.000000 py_extension_functions-0.0.4/py_extension_functions.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-03-19 10:46:32.747471 py_extension_functions-0.0.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      913 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 10:46:32.747471 py_extension_functions-0.0.4/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      836 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_algorithms.py
--rw-r--r--   0 runner    (1001) docker     (123)     5224 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_datetimes.py
--rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_django_model_dummy.py
--rw-r--r--   0 runner    (1001) docker     (123)     7601 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_django_model_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_django_task_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    11863 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_geometry.py
--rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-03-19 10:46:22.000000 py_extension_functions-0.0.4/tests/test_texts.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:20.469733 py_extension_functions-0.0.5/
+-rw-r--r--   0 runner    (1001) docker     (123)     2072 2023-04-07 04:15:20.469733 py_extension_functions-0.0.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1577 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:20.465733 py_extension_functions-0.0.5/gpp/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/algorithms.py
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4022 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/datetimes.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4464 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/loggers.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/networks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11735 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/gpp/texts.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:20.469733 py_extension_functions-0.0.5/py_extension_functions.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2072 2023-04-07 04:15:20.000000 py_extension_functions-0.0.5/py_extension_functions.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      611 2023-04-07 04:15:20.000000 py_extension_functions-0.0.5/py_extension_functions.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 04:15:20.000000 py_extension_functions-0.0.5/py_extension_functions.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-07 04:15:20.000000 py_extension_functions-0.0.5/py_extension_functions.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-07 04:15:20.000000 py_extension_functions-0.0.5/py_extension_functions.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-04-07 04:15:20.469733 py_extension_functions-0.0.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      913 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:15:20.469733 py_extension_functions-0.0.5/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      836 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_algorithms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5224 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_datetimes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_django_model_dummy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7601 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_django_model_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_django_task_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11863 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-07 04:15:08.000000 py_extension_functions-0.0.5/tests/test_texts.py
```

### Comparing `py_extension_functions-0.0.4/PKG-INFO` & `py_extension_functions-0.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: py_extension_functions
-Version: 0.0.4
+Version: 0.0.5
 Summary: personally, python extension functions
 Home-page: https://github.com/Gaolious/py_extension_functions
 Author: aJava
 Author-email: gaolious@gmail.com
 License: MIT
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `py_extension_functions-0.0.4/README.md` & `py_extension_functions-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/gpp/algorithms.py` & `py_extension_functions-0.0.5/gpp/algorithms.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/gpp/constants.py` & `py_extension_functions-0.0.5/gpp/constants.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/gpp/datetimes.py` & `py_extension_functions-0.0.5/gpp/datetimes.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/gpp/geometry.py` & `py_extension_functions-0.0.5/gpp/geometry.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/gpp/texts.py` & `py_extension_functions-0.0.5/gpp/texts.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/py_extension_functions.egg-info/PKG-INFO` & `py_extension_functions-0.0.5/py_extension_functions.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: py-extension-functions
-Version: 0.0.4
+Version: 0.0.5
 Summary: personally, python extension functions
 Home-page: https://github.com/Gaolious/py_extension_functions
 Author: aJava
 Author-email: gaolious@gmail.com
 License: MIT
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `py_extension_functions-0.0.4/py_extension_functions.egg-info/SOURCES.txt` & `py_extension_functions-0.0.5/py_extension_functions.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/setup.py` & `py_extension_functions-0.0.5/setup.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_algorithms.py` & `py_extension_functions-0.0.5/tests/test_algorithms.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_datetimes.py` & `py_extension_functions-0.0.5/tests/test_datetimes.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_django_model_dummy.py` & `py_extension_functions-0.0.5/tests/test_django_model_dummy.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_django_model_utils.py` & `py_extension_functions-0.0.5/tests/test_django_model_utils.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_geometry.py` & `py_extension_functions-0.0.5/tests/test_geometry.py`

 * *Files identical despite different names*

### Comparing `py_extension_functions-0.0.4/tests/test_texts.py` & `py_extension_functions-0.0.5/tests/test_texts.py`

 * *Files identical despite different names*

