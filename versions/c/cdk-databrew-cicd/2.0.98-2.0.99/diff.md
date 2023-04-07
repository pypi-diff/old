# Comparing `tmp/cdk_databrew_cicd-2.0.98.tar.gz` & `tmp/cdk_databrew_cicd-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk_databrew_cicd-2.0.98.tar", last modified: Thu Sep 22 00:50:40 2022, max compression
+gzip compressed data, was "cdk_databrew_cicd-2.0.99.tar", last modified: Fri Sep 23 00:58:00 2022, max compression
```

## Comparing `cdk_databrew_cicd-2.0.98.tar` & `cdk_databrew_cicd-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 00:50:40.107300 cdk_databrew_cicd-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    15129 2022-09-22 00:50:40.107300 cdk_databrew_cicd-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    14210 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-22 00:50:40.107300 cdk_databrew_cicd-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1759 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 00:50:40.103300 cdk_databrew_cicd-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 00:50:40.103300 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/
--rw-r--r--   0 runner    (1001) docker     (121)    56986 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 00:50:40.107300 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      403 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  1424473 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/_jsii/cdk-databrew-cicd@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-22 00:50:27.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-22 00:50:40.107300 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    15129 2022-09-22 00:50:39.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      444 2022-09-22 00:50:40.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-22 00:50:39.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-22 00:50:39.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-09-22 00:50:39.000000 cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-23 00:58:00.492861 cdk_databrew_cicd-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    15129 2022-09-23 00:58:00.488861 cdk_databrew_cicd-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    14210 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-23 00:58:00.492861 cdk_databrew_cicd-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1759 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-23 00:58:00.488861 cdk_databrew_cicd-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-23 00:58:00.488861 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/
+-rw-r--r--   0 runner    (1001) docker     (121)    56986 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-23 00:58:00.488861 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      403 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  1424470 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/_jsii/cdk-databrew-cicd@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-23 00:57:46.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-23 00:58:00.488861 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    15129 2022-09-23 00:57:59.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      444 2022-09-23 00:58:00.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-23 00:57:59.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-09-23 00:58:00.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-09-23 00:58:00.000000 cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/top_level.txt
```

### Comparing `cdk_databrew_cicd-2.0.98/LICENSE` & `cdk_databrew_cicd-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk_databrew_cicd-2.0.98/PKG-INFO` & `cdk_databrew_cicd-2.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk_databrew_cicd
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for AWS Glue DataBrew wtih CICD
 Home-page: https://github.com/HsiehShuJeng/cdk-databrew-cicd.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-databrew-cicd.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk_databrew_cicd-2.0.98/README.md` & `cdk_databrew_cicd-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk_databrew_cicd-2.0.98/setup.py` & `cdk_databrew_cicd-2.0.99/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk_databrew_cicd",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "A construct for AWS Glue DataBrew wtih CICD",
     "license": "Apache-2.0",
     "url": "https://github.com/HsiehShuJeng/cdk-databrew-cicd.git",
     "long_description_content_type": "text/markdown",
     "author": "Shu-Jeng Hsieh",
     "bdist_wheel": {
         "universal": true
@@ -22,25 +22,25 @@
     },
     "packages": [
         "cdk_databrew_cicd",
         "cdk_databrew_cicd._jsii"
     ],
     "package_data": {
         "cdk_databrew_cicd._jsii": [
-            "cdk-databrew-cicd@2.0.98.jsii.tgz"
+            "cdk-databrew-cicd@2.0.99.jsii.tgz"
         ],
         "cdk_databrew_cicd": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
         "aws-cdk-lib>=2.27.0, <3.0.0",
         "constructs>=10.0.5, <11.0.0",
-        "jsii>=1.67.0, <2.0.0",
+        "jsii>=1.68.0, <2.0.0",
         "publication>=0.0.3",
         "typeguard~=2.13.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
         "Programming Language :: JavaScript",
```

### Comparing `cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd/__init__.py` & `cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk_databrew_cicd-2.0.98/src/cdk_databrew_cicd.egg-info/PKG-INFO` & `cdk_databrew_cicd-2.0.99/src/cdk_databrew_cicd.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-databrew-cicd
-Version: 2.0.98
+Version: 2.0.99
 Summary: A construct for AWS Glue DataBrew wtih CICD
 Home-page: https://github.com/HsiehShuJeng/cdk-databrew-cicd.git
 Author: Shu-Jeng Hsieh
 License: Apache-2.0
 Project-URL: Source, https://github.com/HsiehShuJeng/cdk-databrew-cicd.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

