# Comparing `tmp/aib_logging-0.4.tar.gz` & `tmp/aib_logging-0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aib_logging-0.4.tar", last modified: Thu Mar 30 10:18:11 2023, max compression
+gzip compressed data, was "aib_logging-0.5.tar", last modified: Thu Apr  6 08:21:51 2023, max compression
```

## Comparing `aib_logging-0.4.tar` & `aib_logging-0.5.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-30 10:18:11.059750 aib_logging-0.4/
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)     1212 2023-03-28 08:02:11.000000 aib_logging-0.4/LICENSE.txt
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      526 2023-03-30 10:18:11.058750 aib_logging-0.4/PKG-INFO
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       20 2023-03-28 08:02:11.000000 aib_logging-0.4/README.md
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      621 2023-03-30 10:17:14.000000 aib_logging-0.4/pyproject.toml
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       38 2023-03-30 10:18:11.059750 aib_logging-0.4/setup.cfg
-drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-30 10:18:11.056750 aib_logging-0.4/src/
-drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-30 10:18:11.057750 aib_logging-0.4/src/aib_logging/
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-29 01:38:32.000000 aib_logging-0.4/src/aib_logging/__init__.py
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)     1884 2023-03-30 10:16:41.000000 aib_logging-0.4/src/aib_logging/logger.py
-drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-30 10:18:11.058750 aib_logging-0.4/src/aib_logging.egg-info/
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      526 2023-03-30 10:18:11.000000 aib_logging-0.4/src/aib_logging.egg-info/PKG-INFO
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      284 2023-03-30 10:18:11.000000 aib_logging-0.4/src/aib_logging.egg-info/SOURCES.txt
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)        1 2023-03-30 10:18:11.000000 aib_logging-0.4/src/aib_logging.egg-info/dependency_links.txt
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       21 2023-03-30 10:18:11.000000 aib_logging-0.4/src/aib_logging.egg-info/requires.txt
--rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       12 2023-03-30 10:18:11.000000 aib_logging-0.4/src/aib_logging.egg-info/top_level.txt
+drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-04-06 08:21:51.839858 aib_logging-0.5/
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)     1212 2023-03-28 08:02:11.000000 aib_logging-0.5/LICENSE.txt
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      526 2023-04-06 08:21:51.839858 aib_logging-0.5/PKG-INFO
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       20 2023-03-28 08:02:11.000000 aib_logging-0.5/README.md
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      621 2023-04-06 08:18:28.000000 aib_logging-0.5/pyproject.toml
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       38 2023-04-06 08:21:51.839858 aib_logging-0.5/setup.cfg
+drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-04-06 08:21:51.834858 aib_logging-0.5/src/
+drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-04-06 08:21:51.837858 aib_logging-0.5/src/aib_logging/
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-03-29 01:38:32.000000 aib_logging-0.5/src/aib_logging/__init__.py
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)     6515 2023-04-06 08:19:00.000000 aib_logging-0.5/src/aib_logging/logger.py
+drwxr-xr-x   0 akib_shaikh  (1000) akib_shaikh  (1000)        0 2023-04-06 08:21:51.838858 aib_logging-0.5/src/aib_logging.egg-info/
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      526 2023-04-06 08:21:51.000000 aib_logging-0.5/src/aib_logging.egg-info/PKG-INFO
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)      284 2023-04-06 08:21:51.000000 aib_logging-0.5/src/aib_logging.egg-info/SOURCES.txt
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)        1 2023-04-06 08:21:51.000000 aib_logging-0.5/src/aib_logging.egg-info/dependency_links.txt
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       21 2023-04-06 08:21:51.000000 aib_logging-0.5/src/aib_logging.egg-info/requires.txt
+-rw-r--r--   0 akib_shaikh  (1000) akib_shaikh  (1000)       12 2023-04-06 08:21:51.000000 aib_logging-0.5/src/aib_logging.egg-info/top_level.txt
```

### Comparing `aib_logging-0.4/LICENSE.txt` & `aib_logging-0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `aib_logging-0.4/PKG-INFO` & `aib_logging-0.5/src/aib_logging.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: aib_logging
-Version: 0.4
+Name: aib-logging
+Version: 0.5
 Summary: A small example package
 Author-email: akib Shaikh <shaikhakib.k@gmail.com>
 Project-URL: Homepage, https://github.com/pypa/sampleproject
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `aib_logging-0.4/pyproject.toml` & `aib_logging-0.5/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "aib_logging"
-version = "0.4"
+version = "0.5"
 authors = [
   { name="akib Shaikh", email="shaikhakib.k@gmail.com" },
 ]
 description = "A small example package"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `aib_logging-0.4/src/aib_logging.egg-info/PKG-INFO` & `aib_logging-0.5/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: aib-logging
-Version: 0.4
+Name: aib_logging
+Version: 0.5
 Summary: A small example package
 Author-email: akib Shaikh <shaikhakib.k@gmail.com>
 Project-URL: Homepage, https://github.com/pypa/sampleproject
 Project-URL: Bug Tracker, https://github.com/pypa/sampleproject/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

