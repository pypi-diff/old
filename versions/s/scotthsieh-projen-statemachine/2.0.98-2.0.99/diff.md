# Comparing `tmp/scotthsieh_projen_statemachine-2.0.98.tar.gz` & `tmp/scotthsieh_projen_statemachine-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "scotthsieh_projen_statemachine-2.0.98.tar", last modified: Tue Sep 20 01:51:03 2022, max compression
+gzip compressed data, was "scotthsieh_projen_statemachine-2.0.99.tar", last modified: Wed Sep 21 01:58:40 2022, max compression
```

## Comparing `scotthsieh_projen_statemachine-2.0.98.tar` & `scotthsieh_projen_statemachine-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:51:03.366166 scotthsieh_projen_statemachine-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     8341 2022-09-20 01:51:03.366166 scotthsieh_projen_statemachine-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7347 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-20 01:51:03.366166 scotthsieh_projen_statemachine-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1896 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:51:03.362166 scotthsieh_projen_statemachine-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:51:03.362166 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/
--rw-r--r--   0 runner    (1001) docker     (121)    11695 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:51:03.362166 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      436 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  1486651 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/_jsii/projen-statemachine-example@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 01:50:51.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:51:03.362166 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     8341 2022-09-20 01:51:02.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      571 2022-09-20 01:51:03.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 01:51:02.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-20 01:51:03.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       31 2022-09-20 01:51:03.000000 scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 01:58:40.342409 scotthsieh_projen_statemachine-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     8341 2022-09-21 01:58:40.342409 scotthsieh_projen_statemachine-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     7347 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-21 01:58:40.342409 scotthsieh_projen_statemachine-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1896 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 01:58:40.338409 scotthsieh_projen_statemachine-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 01:58:40.338409 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/
+-rw-r--r--   0 runner    (1001) docker     (121)    11695 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 01:58:40.338409 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  1486651 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/_jsii/projen-statemachine-example@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-21 01:58:23.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 01:58:40.338409 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     8341 2022-09-21 01:58:39.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      571 2022-09-21 01:58:40.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-21 01:58:39.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-21 01:58:40.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       31 2022-09-21 01:58:40.000000 scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/top_level.txt
```

### Comparing `scotthsieh_projen_statemachine-2.0.98/LICENSE` & `scotthsieh_projen_statemachine-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `scotthsieh_projen_statemachine-2.0.98/PKG-INFO` & `scotthsieh_projen_statemachine-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scotthsieh_projen_statemachine
-Version: 2.0.98
+Version: 2.0.99
 Summary: An example construct for deploying to npm, PyPi, Maven, and Nuget with Amazon API Gateway and AWS Step Functions.
 Home-page: https://github.com/HsiehShuJeng/projen-simple.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/projen-simple.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `scotthsieh_projen_statemachine-2.0.98/README.md` & `scotthsieh_projen_statemachine-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `scotthsieh_projen_statemachine-2.0.98/setup.py` & `scotthsieh_projen_statemachine-2.0.99/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "scotthsieh_projen_statemachine",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "An example construct for deploying to npm, PyPi, Maven, and Nuget with Amazon API Gateway and AWS Step Functions.",
     "license": "Apache-2.0",
     "url": "https://github.com/HsiehShuJeng/projen-simple.git",
     "long_description_content_type": "text/markdown",
     "author": "Shu-Jeng Hsieh",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "scotthsieh_projen_statemachine",
         "scotthsieh_projen_statemachine._jsii"
     ],
     "package_data": {
         "scotthsieh_projen_statemachine._jsii": [
-            "projen-statemachine-example@2.0.98.jsii.tgz"
+            "projen-statemachine-example@2.0.99.jsii.tgz"
         ],
         "scotthsieh_projen_statemachine": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine/__init__.py` & `scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine/__init__.py`

 * *Files identical despite different names*

### Comparing `scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/PKG-INFO` & `scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scotthsieh-projen-statemachine
-Version: 2.0.98
+Version: 2.0.99
 Summary: An example construct for deploying to npm, PyPi, Maven, and Nuget with Amazon API Gateway and AWS Step Functions.
 Home-page: https://github.com/HsiehShuJeng/projen-simple.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/projen-simple.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `scotthsieh_projen_statemachine-2.0.98/src/scotthsieh_projen_statemachine.egg-info/SOURCES.txt` & `scotthsieh_projen_statemachine-2.0.99/src/scotthsieh_projen_statemachine.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/scotthsieh_projen_statemachine/py.typed
 src/scotthsieh_projen_statemachine.egg-info/PKG-INFO
 src/scotthsieh_projen_statemachine.egg-info/SOURCES.txt
 src/scotthsieh_projen_statemachine.egg-info/dependency_links.txt
 src/scotthsieh_projen_statemachine.egg-info/requires.txt
 src/scotthsieh_projen_statemachine.egg-info/top_level.txt
 src/scotthsieh_projen_statemachine/_jsii/__init__.py
-src/scotthsieh_projen_statemachine/_jsii/projen-statemachine-example@2.0.98.jsii.tgz
+src/scotthsieh_projen_statemachine/_jsii/projen-statemachine-example@2.0.99.jsii.tgz
```

