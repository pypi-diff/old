# Comparing `tmp/cdk-secret-manager-wrapper-layer-2.0.98.tar.gz` & `tmp/cdk-secret-manager-wrapper-layer-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-secret-manager-wrapper-layer-2.0.98.tar", last modified: Sun Nov  6 00:34:42 2022, max compression
+gzip compressed data, was "cdk-secret-manager-wrapper-layer-2.0.99.tar", last modified: Mon Nov  7 00:33:33 2022, max compression
```

## Comparing `cdk-secret-manager-wrapper-layer-2.0.98.tar` & `cdk-secret-manager-wrapper-layer-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3326 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2377 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1864 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/
--rw-r--r--   0 runner    (1001) docker     (121)     4180 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      446 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    26572 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/_jsii/cdk-secret-manager-wrapper-layer@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-06 00:34:27.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-06 00:34:42.473105 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3326 2022-11-06 00:34:41.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      594 2022-11-06 00:34:42.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-06 00:34:41.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-06 00:34:42.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       33 2022-11-06 00:34:42.000000 cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3326 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2377 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1864 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/
+-rw-r--r--   0 runner    (1001) docker     (121)     4180 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      446 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26571 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/_jsii/cdk-secret-manager-wrapper-layer@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-07 00:33:17.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 00:33:33.480777 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3326 2022-11-07 00:33:32.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      594 2022-11-07 00:33:33.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-07 00:33:33.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-07 00:33:33.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       33 2022-11-07 00:33:33.000000 cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/top_level.txt
```

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/LICENSE` & `cdk-secret-manager-wrapper-layer-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/PKG-INFO` & `cdk-secret-manager-wrapper-layer-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-secret-manager-wrapper-layer
-Version: 2.0.98
+Version: 2.0.99
 Summary: cdk-secret-manager-wrapper-layer
 Home-page: https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/README.md` & `cdk-secret-manager-wrapper-layer-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/setup.py` & `cdk-secret-manager-wrapper-layer-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-secret-manager-wrapper-layer",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "cdk-secret-manager-wrapper-layer",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_secret_manager_wrapper_layer",
         "cdk_secret_manager_wrapper_layer._jsii"
     ],
     "package_data": {
         "cdk_secret_manager_wrapper_layer._jsii": [
-            "cdk-secret-manager-wrapper-layer@2.0.98.jsii.tgz"
+            "cdk-secret-manager-wrapper-layer@2.0.99.jsii.tgz"
         ],
         "cdk_secret_manager_wrapper_layer": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer/__init__.py` & `cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/PKG-INFO` & `cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-secret-manager-wrapper-layer
-Version: 2.0.98
+Version: 2.0.99
 Summary: cdk-secret-manager-wrapper-layer
 Home-page: https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-secret-manager-wrapper-layer.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-secret-manager-wrapper-layer-2.0.98/src/cdk_secret_manager_wrapper_layer.egg-info/SOURCES.txt` & `cdk-secret-manager-wrapper-layer-2.0.99/src/cdk_secret_manager_wrapper_layer.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdk_secret_manager_wrapper_layer/py.typed
 src/cdk_secret_manager_wrapper_layer.egg-info/PKG-INFO
 src/cdk_secret_manager_wrapper_layer.egg-info/SOURCES.txt
 src/cdk_secret_manager_wrapper_layer.egg-info/dependency_links.txt
 src/cdk_secret_manager_wrapper_layer.egg-info/requires.txt
 src/cdk_secret_manager_wrapper_layer.egg-info/top_level.txt
 src/cdk_secret_manager_wrapper_layer/_jsii/__init__.py
-src/cdk_secret_manager_wrapper_layer/_jsii/cdk-secret-manager-wrapper-layer@2.0.98.jsii.tgz
+src/cdk_secret_manager_wrapper_layer/_jsii/cdk-secret-manager-wrapper-layer@2.0.99.jsii.tgz
```

