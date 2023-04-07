# Comparing `tmp/botocore-a-la-carte-ds-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-ds-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-ds-1.29.98.tar", last modified: Fri Mar 24 01:24:15 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-ds-1.29.99.tar", last modified: Sat Mar 25 01:22:36 2023, max compression
```

## Comparing `botocore-a-la-carte-ds-1.29.98.tar` & `botocore-a-la-carte-ds-1.29.99.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/
--rw-r--r--   0 runner    (1001) docker     (123)    13114 2023-03-24 01:23:57.000000 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-24 01:23:57.000000 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-03-24 01:23:57.000000 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   199685 2023-03-24 01:23:57.000000 botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/service-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:15.673904 botocore-a-la-carte-ds-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-03-24 01:24:15.000000 botocore-a-la-carte-ds-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.271147 botocore-a-la-carte-ds-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-03-25 01:22:36.271147 botocore-a-la-carte-ds-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.267147 botocore-a-la-carte-ds-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.267147 botocore-a-la-carte-ds-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.267147 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.271147 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/
+-rw-r--r--   0 runner    (1001) docker     (123)    13114 2023-03-25 01:22:12.000000 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-25 01:22:12.000000 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-03-25 01:22:12.000000 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   199685 2023-03-25 01:22:12.000000 botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/service-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:36.271147 botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:22:36.271147 botocore-a-la-carte-ds-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-03-25 01:22:36.000000 botocore-a-la-carte-ds-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-ds-1.29.98/LICENSE.txt` & `botocore-a-la-carte-ds-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ds-1.29.98/PKG-INFO` & `botocore-a-la-carte-ds-1.29.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-ds
-Version: 1.29.98
+Version: 1.29.99
 Summary: ds data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/endpoint-rule-set-1.json` & `botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/paginators-1.json` & `botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ds-1.29.98/botocore/data/ds/2015-04-16/service-2.json` & `botocore-a-la-carte-ds-1.29.99/botocore/data/ds/2015-04-16/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ds-1.29.98/botocore_a_la_carte_ds.egg-info/PKG-INFO` & `botocore-a-la-carte-ds-1.29.99/botocore_a_la_carte_ds.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-ds
-Version: 1.29.98
+Version: 1.29.99
 Summary: ds data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-ds-1.29.98/setup.py` & `botocore-a-la-carte-ds-1.29.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-ds',
-    version="1.29.98",
+    version="1.29.99",
     description='ds data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/ds/*/*.json'],
```

