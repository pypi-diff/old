# Comparing `tmp/cdk-lambda-layer-wget-2.0.98.tar.gz` & `tmp/cdk-lambda-layer-wget-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-lambda-layer-wget-2.0.98.tar", last modified: Thu Jun  2 02:19:06 2022, max compression
+gzip compressed data, was "cdk-lambda-layer-wget-2.0.99.tar", last modified: Fri Jun  3 02:02:45 2022, max compression
```

## Comparing `cdk-lambda-layer-wget-2.0.98.tar` & `cdk-lambda-layer-wget-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:19:06.128125 cdk-lambda-layer-wget-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2000 2022-06-02 02:19:06.128125 cdk-lambda-layer-wget-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1072 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-02 02:19:06.128125 cdk-lambda-layer-wget-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1758 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:19:06.120125 cdk-lambda-layer-wget-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:19:06.120125 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/
--rw-r--r--   0 runner    (1001) docker     (121)     1724 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:19:06.124125 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  6011895 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/_jsii/cdk-lambda-layer-wget@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-02 02:18:52.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:19:06.124125 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2000 2022-06-02 02:19:05.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      484 2022-06-02 02:19:06.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-02 02:19:05.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-06-02 02:19:05.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-06-02 02:19:06.000000 cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-03 02:02:45.605113 cdk-lambda-layer-wget-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2000 2022-06-03 02:02:45.601112 cdk-lambda-layer-wget-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1072 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-03 02:02:45.605113 cdk-lambda-layer-wget-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1758 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-03 02:02:45.593112 cdk-lambda-layer-wget-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-03 02:02:45.597113 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/
+-rw-r--r--   0 runner    (1001) docker     (121)     1724 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-03 02:02:45.597113 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  6011898 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/_jsii/cdk-lambda-layer-wget@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-03 02:02:29.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-03 02:02:45.597113 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2000 2022-06-03 02:02:44.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      484 2022-06-03 02:02:45.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-03 02:02:44.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-06-03 02:02:45.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-06-03 02:02:45.000000 cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/top_level.txt
```

### Comparing `cdk-lambda-layer-wget-2.0.98/LICENSE` & `cdk-lambda-layer-wget-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-wget-2.0.98/PKG-INFO` & `cdk-lambda-layer-wget-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-wget
-Version: 2.0.98
+Version: 2.0.99
 Summary: Lambda Layer for wget
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-wget.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-wget.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-lambda-layer-wget-2.0.98/README.md` & `cdk-lambda-layer-wget-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-wget-2.0.98/setup.py` & `cdk-lambda-layer-wget-2.0.99/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-lambda-layer-wget",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "Lambda Layer for wget",
     "license": "Apache-2.0",
     "url": "https://github.com/clarencetw/cdk-lambda-layer-wget.git",
     "long_description_content_type": "text/markdown",
     "author": "clarencetw<mr.lin.clarence@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_lambda_layer_wget",
         "cdk_lambda_layer_wget._jsii"
     ],
     "package_data": {
         "cdk_lambda_layer_wget._jsii": [
-            "cdk-lambda-layer-wget@2.0.98.jsii.tgz"
+            "cdk-lambda-layer-wget@2.0.99.jsii.tgz"
         ],
         "cdk_lambda_layer_wget": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget/__init__.py` & `cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-wget-2.0.98/src/cdk_lambda_layer_wget.egg-info/PKG-INFO` & `cdk-lambda-layer-wget-2.0.99/src/cdk_lambda_layer_wget.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-wget
-Version: 2.0.98
+Version: 2.0.99
 Summary: Lambda Layer for wget
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-wget.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-wget.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

