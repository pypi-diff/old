# Comparing `tmp/cdk_lambda_subminute-2.0.98.tar.gz` & `tmp/cdk_lambda_subminute-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk_lambda_subminute-2.0.98.tar", last modified: Mon Sep 19 01:58:44 2022, max compression
+gzip compressed data, was "cdk_lambda_subminute-2.0.99.tar", last modified: Tue Sep 20 01:50:50 2022, max compression
```

## Comparing `cdk_lambda_subminute-2.0.98.tar` & `cdk_lambda_subminute-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-19 01:58:44.668490 cdk_lambda_subminute-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    13792 2022-09-19 01:58:44.664489 cdk_lambda_subminute-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    12806 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-19 01:58:44.668490 cdk_lambda_subminute-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1841 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-19 01:58:44.664489 cdk_lambda_subminute-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-19 01:58:44.664489 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/
--rw-r--r--   0 runner    (1001) docker     (121)    28658 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-19 01:58:44.664489 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      422 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   132763 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/_jsii/cdk-lambda-subminute@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-19 01:58:27.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-19 01:58:44.664489 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    13792 2022-09-19 01:58:43.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      474 2022-09-19 01:58:44.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-19 01:58:44.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-19 01:58:44.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-09-19 01:58:44.000000 cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    13792 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    12806 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1841 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/
+-rw-r--r--   0 runner    (1001) docker     (121)    28658 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      422 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   132764 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/_jsii/cdk-lambda-subminute@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 01:50:38.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 01:50:50.164944 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    13792 2022-09-20 01:50:49.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      474 2022-09-20 01:50:50.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 01:50:49.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-20 01:50:50.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-09-20 01:50:50.000000 cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/top_level.txt
```

### Comparing `cdk_lambda_subminute-2.0.98/LICENSE` & `cdk_lambda_subminute-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk_lambda_subminute-2.0.98/PKG-INFO` & `cdk_lambda_subminute-2.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk_lambda_subminute
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for deploying a Lambda function that can be invoked every time unit less than one minute.
 Home-page: https://github.com/HsiehShuJeng/cdk-lambda-subminute.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-lambda-subminute.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk_lambda_subminute-2.0.98/README.md` & `cdk_lambda_subminute-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk_lambda_subminute-2.0.98/setup.py` & `cdk_lambda_subminute-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk_lambda_subminute",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "A construct for deploying a Lambda function that can be invoked every time unit less than one minute.",
     "license": "Apache-2.0",
     "url": "https://github.com/HsiehShuJeng/cdk-lambda-subminute.git",
     "long_description_content_type": "text/markdown",
     "author": "Shu-Jeng Hsieh",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_lambda_subminute",
         "cdk_lambda_subminute._jsii"
     ],
     "package_data": {
         "cdk_lambda_subminute._jsii": [
-            "cdk-lambda-subminute@2.0.98.jsii.tgz"
+            "cdk-lambda-subminute@2.0.99.jsii.tgz"
         ],
         "cdk_lambda_subminute": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute/__init__.py` & `cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk_lambda_subminute-2.0.98/src/cdk_lambda_subminute.egg-info/PKG-INFO` & `cdk_lambda_subminute-2.0.99/src/cdk_lambda_subminute.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-subminute
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for deploying a Lambda function that can be invoked every time unit less than one minute.
 Home-page: https://github.com/HsiehShuJeng/cdk-lambda-subminute.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-lambda-subminute.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

