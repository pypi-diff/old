# Comparing `tmp/cdk_emrserverless_with_delta_lake-2.0.98.tar.gz` & `tmp/cdk_emrserverless_with_delta_lake-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk_emrserverless_with_delta_lake-2.0.98.tar", last modified: Fri Aug 26 02:04:44 2022, max compression
+gzip compressed data, was "cdk_emrserverless_with_delta_lake-2.0.99.tar", last modified: Sat Aug 27 02:01:23 2022, max compression
```

## Comparing `cdk_emrserverless_with_delta_lake-2.0.98.tar` & `cdk_emrserverless_with_delta_lake-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 02:04:44.531820 cdk_emrserverless_with_delta_lake-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    13539 2022-08-26 02:04:44.531820 cdk_emrserverless_with_delta_lake-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    12566 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-26 02:04:44.531820 cdk_emrserverless_with_delta_lake-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1894 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 02:04:44.523820 cdk_emrserverless_with_delta_lake-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 02:04:44.523820 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/
--rw-r--r--   0 runner    (1001) docker     (121)    72322 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 02:04:44.527820 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      448 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  3271244 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/_jsii/cdk-emrserverless-with-delta-lake@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-26 02:04:29.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 02:04:44.527820 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    13539 2022-08-26 02:04:43.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      604 2022-08-26 02:04:44.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-26 02:04:43.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      112 2022-08-26 02:04:44.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       34 2022-08-26 02:04:44.000000 cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-27 02:01:23.287517 cdk_emrserverless_with_delta_lake-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    13539 2022-08-27 02:01:23.287517 cdk_emrserverless_with_delta_lake-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    12566 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-27 02:01:23.287517 cdk_emrserverless_with_delta_lake-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1894 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-27 02:01:23.279517 cdk_emrserverless_with_delta_lake-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-27 02:01:23.283517 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/
+-rw-r--r--   0 runner    (1001) docker     (121)    72322 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-27 02:01:23.283517 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      448 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  3271237 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/_jsii/cdk-emrserverless-with-delta-lake@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-27 02:01:11.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-27 02:01:23.283517 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    13539 2022-08-27 02:01:22.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      604 2022-08-27 02:01:23.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-27 02:01:22.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      112 2022-08-27 02:01:23.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       34 2022-08-27 02:01:23.000000 cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/top_level.txt
```

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/LICENSE` & `cdk_emrserverless_with_delta_lake-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/PKG-INFO` & `cdk_emrserverless_with_delta_lake-2.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk_emrserverless_with_delta_lake
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for the quick demo of EMR Serverless.
 Home-page: https://github.com/HsiehShuJeng/cdk-emrserverless-with-delta-lake.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-emrserverless-with-delta-lake.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/README.md` & `cdk_emrserverless_with_delta_lake-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/setup.py` & `cdk_emrserverless_with_delta_lake-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk_emrserverless_with_delta_lake",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "A construct for the quick demo of EMR Serverless.",
     "license": "Apache-2.0",
     "url": "https://github.com/HsiehShuJeng/cdk-emrserverless-with-delta-lake.git",
     "long_description_content_type": "text/markdown",
     "author": "Shu-Jeng Hsieh",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_emrserverless_with_delta_lake",
         "cdk_emrserverless_with_delta_lake._jsii"
     ],
     "package_data": {
         "cdk_emrserverless_with_delta_lake._jsii": [
-            "cdk-emrserverless-with-delta-lake@2.0.98.jsii.tgz"
+            "cdk-emrserverless-with-delta-lake@2.0.99.jsii.tgz"
         ],
         "cdk_emrserverless_with_delta_lake": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake/__init__.py` & `cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/PKG-INFO` & `cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-emrserverless-with-delta-lake
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for the quick demo of EMR Serverless.
 Home-page: https://github.com/HsiehShuJeng/cdk-emrserverless-with-delta-lake.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-emrserverless-with-delta-lake.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk_emrserverless_with_delta_lake-2.0.98/src/cdk_emrserverless_with_delta_lake.egg-info/SOURCES.txt` & `cdk_emrserverless_with_delta_lake-2.0.99/src/cdk_emrserverless_with_delta_lake.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdk_emrserverless_with_delta_lake/py.typed
 src/cdk_emrserverless_with_delta_lake.egg-info/PKG-INFO
 src/cdk_emrserverless_with_delta_lake.egg-info/SOURCES.txt
 src/cdk_emrserverless_with_delta_lake.egg-info/dependency_links.txt
 src/cdk_emrserverless_with_delta_lake.egg-info/requires.txt
 src/cdk_emrserverless_with_delta_lake.egg-info/top_level.txt
 src/cdk_emrserverless_with_delta_lake/_jsii/__init__.py
-src/cdk_emrserverless_with_delta_lake/_jsii/cdk-emrserverless-with-delta-lake@2.0.98.jsii.tgz
+src/cdk_emrserverless_with_delta_lake/_jsii/cdk-emrserverless-with-delta-lake@2.0.99.jsii.tgz
```

