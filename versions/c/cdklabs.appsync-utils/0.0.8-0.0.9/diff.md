# Comparing `tmp/cdklabs.appsync-utils-0.0.8.tar.gz` & `tmp/cdklabs.appsync-utils-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.appsync-utils-0.0.8.tar", last modified: Thu Feb 23 15:59:33 2023, max compression
+gzip compressed data, was "cdklabs.appsync-utils-0.0.9.tar", last modified: Thu Feb 23 17:08:51 2023, max compression
```

## Comparing `cdklabs.appsync-utils-0.0.8.tar` & `cdklabs.appsync-utils-0.0.9.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    17238 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/src/awscdk/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/
--rw-r--r--   0 runner    (1001) docker     (123)   134850 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    78737 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/_jsii/awscdk-appsync-utils@0.0.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-23 15:59:21.000000 cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 15:59:33.501771 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-02-23 15:59:33.000000 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-23 15:59:33.000000 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-23 15:59:33.000000 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-02-23 15:59:33.000000 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-02-23 15:59:33.000000 cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    17238 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.237581 cdklabs.appsync-utils-0.0.9/src/awscdk/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)   134850 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    78736 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/_jsii/awscdk-appsync-utils@0.0.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-23 17:08:38.000000 cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-23 17:08:51.241582 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-02-23 17:08:51.000000 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-23 17:08:51.000000 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-23 17:08:51.000000 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-02-23 17:08:51.000000 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-02-23 17:08:51.000000 cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/top_level.txt
```

### Comparing `cdklabs.appsync-utils-0.0.8/LICENSE` & `cdklabs.appsync-utils-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.appsync-utils-0.0.8/PKG-INFO` & `cdklabs.appsync-utils-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.appsync-utils
-Version: 0.0.8
+Version: 0.0.9
 Summary: Utilities for creating appsync apis using aws-cdk
 Home-page: https://github.com/cdklabs/awscdk-appsync-utils.git
 Author: Mitchell Valine<mitchellvaline@yahoo.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/awscdk-appsync-utils.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdklabs.appsync-utils-0.0.8/README.md` & `cdklabs.appsync-utils-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.appsync-utils-0.0.8/setup.py` & `cdklabs.appsync-utils-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.appsync-utils",
-    "version": "0.0.8",
+    "version": "0.0.9",
     "description": "Utilities for creating appsync apis using aws-cdk",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/awscdk-appsync-utils.git",
     "long_description_content_type": "text/markdown",
     "author": "Mitchell Valine<mitchellvaline@yahoo.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "awscdk.appsync_utils",
         "awscdk.appsync_utils._jsii"
     ],
     "package_data": {
         "awscdk.appsync_utils._jsii": [
-            "awscdk-appsync-utils@0.0.8.jsii.tgz"
+            "awscdk-appsync-utils@0.0.9.jsii.tgz"
         ],
         "awscdk.appsync_utils": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.appsync-utils-0.0.8/src/awscdk/appsync_utils/__init__.py` & `cdklabs.appsync-utils-0.0.9/src/awscdk/appsync_utils/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.appsync-utils-0.0.8/src/cdklabs.appsync_utils.egg-info/PKG-INFO` & `cdklabs.appsync-utils-0.0.9/src/cdklabs.appsync_utils.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.appsync-utils
-Version: 0.0.8
+Version: 0.0.9
 Summary: Utilities for creating appsync apis using aws-cdk
 Home-page: https://github.com/cdklabs/awscdk-appsync-utils.git
 Author: Mitchell Valine<mitchellvaline@yahoo.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/awscdk-appsync-utils.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

