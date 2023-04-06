# Comparing `tmp/cdk-nag-2.9.6.tar.gz` & `tmp/cdk-nag-2.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-nag-2.9.6.tar", last modified: Wed Mar  9 00:21:22 2022, max compression
+gzip compressed data, was "cdk-nag-2.9.7.tar", last modified: Thu Mar 10 00:19:06 2022, max compression
```

## Comparing `cdk-nag-2.9.6.tar` & `cdk-nag-2.9.7.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      105 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/NOTICE
--rw-r--r--   0 runner    (1001) docker     (121)    17054 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    16096 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1697 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/src/cdk_nag/
--rw-r--r--   0 runner    (1001) docker     (121)    45778 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/src/cdk_nag/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/src/cdk_nag/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      347 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/src/cdk_nag/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   644112 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/src/cdk_nag/_jsii/cdk-nag@2.9.6.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-09 00:21:10.000000 cdk-nag-2.9.6/src/cdk_nag/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-09 00:21:22.616062 cdk-nag-2.9.6/src/cdk_nag.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    17054 2022-03-09 00:21:22.000000 cdk-nag-2.9.6/src/cdk_nag.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      350 2022-03-09 00:21:22.000000 cdk-nag-2.9.6/src/cdk_nag.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-09 00:21:22.000000 cdk-nag-2.9.6/src/cdk_nag.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-09 00:21:22.000000 cdk-nag-2.9.6/src/cdk_nag.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-03-09 00:21:22.000000 cdk-nag-2.9.6/src/cdk_nag.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-10 00:19:06.455680 cdk-nag-2.9.7/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      105 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (121)    17054 2022-03-10 00:19:06.455680 cdk-nag-2.9.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    16096 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-10 00:19:06.455680 cdk-nag-2.9.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1697 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-10 00:19:06.451680 cdk-nag-2.9.7/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-10 00:19:06.451680 cdk-nag-2.9.7/src/cdk_nag/
+-rw-r--r--   0 runner    (1001) docker     (121)    45778 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/src/cdk_nag/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-10 00:19:06.455680 cdk-nag-2.9.7/src/cdk_nag/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      347 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/src/cdk_nag/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   644109 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/src/cdk_nag/_jsii/cdk-nag@2.9.7.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-10 00:18:53.000000 cdk-nag-2.9.7/src/cdk_nag/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-10 00:19:06.455680 cdk-nag-2.9.7/src/cdk_nag.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    17054 2022-03-10 00:19:06.000000 cdk-nag-2.9.7/src/cdk_nag.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      350 2022-03-10 00:19:06.000000 cdk-nag-2.9.7/src/cdk_nag.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-10 00:19:06.000000 cdk-nag-2.9.7/src/cdk_nag.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-10 00:19:06.000000 cdk-nag-2.9.7/src/cdk_nag.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        8 2022-03-10 00:19:06.000000 cdk-nag-2.9.7/src/cdk_nag.egg-info/top_level.txt
```

### Comparing `cdk-nag-2.9.6/LICENSE` & `cdk-nag-2.9.7/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-nag-2.9.6/PKG-INFO` & `cdk-nag-2.9.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-nag
-Version: 2.9.6
+Version: 2.9.7
 Summary: Check CDK v2 applications for best practices using a combination on available rule packs.
 Home-page: https://github.com/cdklabs/cdk-nag.git
 Author: Arun Donti<donti@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-nag.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-nag-2.9.6/README.md` & `cdk-nag-2.9.7/README.md`

 * *Files identical despite different names*

### Comparing `cdk-nag-2.9.6/setup.py` & `cdk-nag-2.9.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-nag",
-    "version": "2.9.6",
+    "version": "2.9.7",
     "description": "Check CDK v2 applications for best practices using a combination on available rule packs.",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-nag.git",
     "long_description_content_type": "text/markdown",
     "author": "Arun Donti<donti@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_nag",
         "cdk_nag._jsii"
     ],
     "package_data": {
         "cdk_nag._jsii": [
-            "cdk-nag@2.9.6.jsii.tgz"
+            "cdk-nag@2.9.7.jsii.tgz"
         ],
         "cdk_nag": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `cdk-nag-2.9.6/src/cdk_nag/__init__.py` & `cdk-nag-2.9.7/src/cdk_nag/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-nag-2.9.6/src/cdk_nag.egg-info/PKG-INFO` & `cdk-nag-2.9.7/src/cdk_nag.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-nag
-Version: 2.9.6
+Version: 2.9.7
 Summary: Check CDK v2 applications for best practices using a combination on available rule packs.
 Home-page: https://github.com/cdklabs/cdk-nag.git
 Author: Arun Donti<donti@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-nag.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

