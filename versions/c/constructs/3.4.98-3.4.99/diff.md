# Comparing `tmp/constructs-3.4.98.tar.gz` & `tmp/constructs-3.4.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "constructs-3.4.98.tar", last modified: Sat Sep 17 00:22:06 2022, max compression
+gzip compressed data, was "constructs-3.4.99.tar", last modified: Sun Sep 18 00:21:23 2022, max compression
```

## Comparing `constructs-3.4.98.tar` & `constructs-3.4.99.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-17 00:22:06.367047 constructs-3.4.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-17 00:21:54.000000 constructs-3.4.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-17 00:21:54.000000 constructs-3.4.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)       72 2022-09-17 00:21:54.000000 constructs-3.4.98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-09-17 00:22:06.367047 constructs-3.4.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1621 2022-09-17 00:21:54.000000 constructs-3.4.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-17 00:21:54.000000 constructs-3.4.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-17 00:22:06.367047 constructs-3.4.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1613 2022-09-17 00:21:54.000000 constructs-3.4.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-17 00:22:06.367047 constructs-3.4.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-17 00:22:06.367047 constructs-3.4.98/src/constructs/
--rw-r--r--   0 runner    (1001) docker     (121)    40767 2022-09-17 00:21:54.000000 constructs-3.4.98/src/constructs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-17 00:22:06.367047 constructs-3.4.98/src/constructs/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      343 2022-09-17 00:21:54.000000 constructs-3.4.98/src/constructs/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    52956 2022-09-17 00:21:54.000000 constructs-3.4.98/src/constructs/_jsii/constructs@3.4.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-17 00:21:54.000000 constructs-3.4.98/src/constructs/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-17 00:22:06.367047 constructs-3.4.98/src/constructs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-09-17 00:22:05.000000 constructs-3.4.98/src/constructs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      381 2022-09-17 00:22:06.000000 constructs-3.4.98/src/constructs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-17 00:22:05.000000 constructs-3.4.98/src/constructs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       57 2022-09-17 00:22:06.000000 constructs-3.4.98/src/constructs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       11 2022-09-17 00:22:06.000000 constructs-3.4.98/src/constructs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-18 00:21:23.868094 constructs-3.4.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-18 00:21:11.000000 constructs-3.4.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-18 00:21:11.000000 constructs-3.4.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)       72 2022-09-18 00:21:11.000000 constructs-3.4.99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-09-18 00:21:23.868094 constructs-3.4.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1621 2022-09-18 00:21:11.000000 constructs-3.4.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-18 00:21:11.000000 constructs-3.4.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-18 00:21:23.868094 constructs-3.4.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1613 2022-09-18 00:21:11.000000 constructs-3.4.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-18 00:21:23.864094 constructs-3.4.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-18 00:21:23.868094 constructs-3.4.99/src/constructs/
+-rw-r--r--   0 runner    (1001) docker     (121)    40767 2022-09-18 00:21:11.000000 constructs-3.4.99/src/constructs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-18 00:21:23.868094 constructs-3.4.99/src/constructs/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      343 2022-09-18 00:21:11.000000 constructs-3.4.99/src/constructs/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    52953 2022-09-18 00:21:11.000000 constructs-3.4.99/src/constructs/_jsii/constructs@3.4.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-18 00:21:11.000000 constructs-3.4.99/src/constructs/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-18 00:21:23.868094 constructs-3.4.99/src/constructs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-09-18 00:21:23.000000 constructs-3.4.99/src/constructs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      381 2022-09-18 00:21:23.000000 constructs-3.4.99/src/constructs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-18 00:21:23.000000 constructs-3.4.99/src/constructs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       57 2022-09-18 00:21:23.000000 constructs-3.4.99/src/constructs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       11 2022-09-18 00:21:23.000000 constructs-3.4.99/src/constructs.egg-info/top_level.txt
```

### Comparing `constructs-3.4.98/LICENSE` & `constructs-3.4.99/LICENSE`

 * *Files identical despite different names*

### Comparing `constructs-3.4.98/PKG-INFO` & `constructs-3.4.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: constructs
-Version: 3.4.98
+Version: 3.4.99
 Summary: A programming model for composable configuration
 Home-page: https://github.com/aws/constructs
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/constructs.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `constructs-3.4.98/README.md` & `constructs-3.4.99/README.md`

 * *Files identical despite different names*

### Comparing `constructs-3.4.98/setup.py` & `constructs-3.4.99/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "constructs",
-    "version": "3.4.98",
+    "version": "3.4.99",
     "description": "A programming model for composable configuration",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/constructs",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "constructs",
         "constructs._jsii"
     ],
     "package_data": {
         "constructs._jsii": [
-            "constructs@3.4.98.jsii.tgz"
+            "constructs@3.4.99.jsii.tgz"
         ],
         "constructs": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `constructs-3.4.98/src/constructs/__init__.py` & `constructs-3.4.99/src/constructs/__init__.py`

 * *Files identical despite different names*

### Comparing `constructs-3.4.98/src/constructs.egg-info/PKG-INFO` & `constructs-3.4.99/src/constructs.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: constructs
-Version: 3.4.98
+Version: 3.4.99
 Summary: A programming model for composable configuration
 Home-page: https://github.com/aws/constructs
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/constructs.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

