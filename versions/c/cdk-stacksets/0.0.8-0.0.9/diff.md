# Comparing `tmp/cdk-stacksets-0.0.8.tar.gz` & `tmp/cdk-stacksets-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-stacksets-0.0.8.tar", last modified: Sun Jan 22 00:16:03 2023, max compression
+gzip compressed data, was "cdk-stacksets-0.0.9.tar", last modified: Mon Jan 23 00:16:09 2023, max compression
```

## Comparing `cdk-stacksets-0.0.8.tar` & `cdk-stacksets-0.0.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    12131 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    11249 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/src/cdk_stacksets/
--rw-r--r--   0 runner    (1001) docker     (123)    83981 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/src/cdk_stacksets/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/src/cdk_stacksets/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/src/cdk_stacksets/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    68656 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/src/cdk_stacksets/_jsii/cdk-stacksets@0.0.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-22 00:15:49.000000 cdk-stacksets-0.0.8/src/cdk_stacksets/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 00:16:03.882442 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12131 2023-01-22 00:16:03.000000 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-22 00:16:03.000000 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-22 00:16:03.000000 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-22 00:16:03.000000 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-01-22 00:16:03.000000 cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    12131 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    11249 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/src/cdk_stacksets/
+-rw-r--r--   0 runner    (1001) docker     (123)    83981 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/src/cdk_stacksets/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/src/cdk_stacksets/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/src/cdk_stacksets/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68654 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/src/cdk_stacksets/_jsii/cdk-stacksets@0.0.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-23 00:15:55.000000 cdk-stacksets-0.0.9/src/cdk_stacksets/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-23 00:16:09.494084 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12131 2023-01-23 00:16:08.000000 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-23 00:16:09.000000 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-23 00:16:09.000000 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-23 00:16:09.000000 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-01-23 00:16:09.000000 cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/top_level.txt
```

### Comparing `cdk-stacksets-0.0.8/LICENSE` & `cdk-stacksets-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-stacksets-0.0.8/PKG-INFO` & `cdk-stacksets-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-stacksets
-Version: 0.0.8
+Version: 0.0.9
 Summary: cdk-stacksets
 Home-page: https://github.com/cdklabs/cdk-stacksets.git
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-stacksets.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-stacksets-0.0.8/README.md` & `cdk-stacksets-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `cdk-stacksets-0.0.8/setup.py` & `cdk-stacksets-0.0.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-stacksets",
-    "version": "0.0.8",
+    "version": "0.0.9",
     "description": "cdk-stacksets",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-stacksets.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services<aws-cdk-dev@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_stacksets",
         "cdk_stacksets._jsii"
     ],
     "package_data": {
         "cdk_stacksets._jsii": [
-            "cdk-stacksets@0.0.8.jsii.tgz"
+            "cdk-stacksets@0.0.9.jsii.tgz"
         ],
         "cdk_stacksets": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-stacksets-0.0.8/src/cdk_stacksets/__init__.py` & `cdk-stacksets-0.0.9/src/cdk_stacksets/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-stacksets-0.0.8/src/cdk_stacksets.egg-info/PKG-INFO` & `cdk-stacksets-0.0.9/src/cdk_stacksets.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-stacksets
-Version: 0.0.8
+Version: 0.0.9
 Summary: cdk-stacksets
 Home-page: https://github.com/cdklabs/cdk-stacksets.git
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-stacksets.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

