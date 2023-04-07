# Comparing `tmp/cdk-common-2.0.98.tar.gz` & `tmp/cdk-common-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-common-2.0.98.tar", last modified: Tue Mar 22 00:18:07 2022, max compression
+gzip compressed data, was "cdk-common-2.0.99.tar", last modified: Wed Mar 23 00:16:37 2022, max compression
```

## Comparing `cdk-common-2.0.98.tar` & `cdk-common-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-22 00:18:07.810060 cdk-common-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-22 00:17:52.000000 cdk-common-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-22 00:17:52.000000 cdk-common-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2672 2022-03-22 00:18:07.810060 cdk-common-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1798 2022-03-22 00:17:52.000000 cdk-common-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-22 00:17:52.000000 cdk-common-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-22 00:18:07.810060 cdk-common-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1650 2022-03-22 00:17:52.000000 cdk-common-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-22 00:18:07.802060 cdk-common-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-22 00:18:07.802060 cdk-common-2.0.98/src/cdk_common/
--rw-r--r--   0 runner    (1001) docker     (121)   164375 2022-03-22 00:17:52.000000 cdk-common-2.0.98/src/cdk_common/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-22 00:18:07.802060 cdk-common-2.0.98/src/cdk_common/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      355 2022-03-22 00:17:52.000000 cdk-common-2.0.98/src/cdk_common/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  3716751 2022-03-22 00:17:52.000000 cdk-common-2.0.98/src/cdk_common/_jsii/cdk-common@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-22 00:17:52.000000 cdk-common-2.0.98/src/cdk_common/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-22 00:18:07.802060 cdk-common-2.0.98/src/cdk_common.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2672 2022-03-22 00:18:07.000000 cdk-common-2.0.98/src/cdk_common.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      374 2022-03-22 00:18:07.000000 cdk-common-2.0.98/src/cdk_common.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-22 00:18:07.000000 cdk-common-2.0.98/src/cdk_common.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-22 00:18:07.000000 cdk-common-2.0.98/src/cdk_common.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       11 2022-03-22 00:18:07.000000 cdk-common-2.0.98/src/cdk_common.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-23 00:16:37.500487 cdk-common-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-23 00:16:26.000000 cdk-common-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-23 00:16:26.000000 cdk-common-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2672 2022-03-23 00:16:37.500487 cdk-common-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1798 2022-03-23 00:16:26.000000 cdk-common-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-23 00:16:26.000000 cdk-common-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-23 00:16:37.500487 cdk-common-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1650 2022-03-23 00:16:26.000000 cdk-common-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-23 00:16:37.492487 cdk-common-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-23 00:16:37.496487 cdk-common-2.0.99/src/cdk_common/
+-rw-r--r--   0 runner    (1001) docker     (121)   164375 2022-03-23 00:16:26.000000 cdk-common-2.0.99/src/cdk_common/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-23 00:16:37.496487 cdk-common-2.0.99/src/cdk_common/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      355 2022-03-23 00:16:26.000000 cdk-common-2.0.99/src/cdk_common/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  3716854 2022-03-23 00:16:26.000000 cdk-common-2.0.99/src/cdk_common/_jsii/cdk-common@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-23 00:16:26.000000 cdk-common-2.0.99/src/cdk_common/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-23 00:16:37.496487 cdk-common-2.0.99/src/cdk_common.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2672 2022-03-23 00:16:37.000000 cdk-common-2.0.99/src/cdk_common.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      374 2022-03-23 00:16:37.000000 cdk-common-2.0.99/src/cdk_common.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-23 00:16:37.000000 cdk-common-2.0.99/src/cdk_common.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-23 00:16:37.000000 cdk-common-2.0.99/src/cdk_common.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       11 2022-03-23 00:16:37.000000 cdk-common-2.0.99/src/cdk_common.egg-info/top_level.txt
```

### Comparing `cdk-common-2.0.98/LICENSE` & `cdk-common-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-common-2.0.98/PKG-INFO` & `cdk-common-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-common
-Version: 2.0.98
+Version: 2.0.99
 Summary: Common AWS CDK librarys.
 Home-page: https://github.com/neilkuan/cdk-common.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-common.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-common-2.0.98/README.md` & `cdk-common-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-common-2.0.98/setup.py` & `cdk-common-2.0.99/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-common",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "Common AWS CDK librarys.",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-common.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_common",
         "cdk_common._jsii"
     ],
     "package_data": {
         "cdk_common._jsii": [
-            "cdk-common@2.0.98.jsii.tgz"
+            "cdk-common@2.0.99.jsii.tgz"
         ],
         "cdk_common": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `cdk-common-2.0.98/src/cdk_common/__init__.py` & `cdk-common-2.0.99/src/cdk_common/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-common-2.0.98/src/cdk_common.egg-info/PKG-INFO` & `cdk-common-2.0.99/src/cdk_common.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-common
-Version: 2.0.98
+Version: 2.0.99
 Summary: Common AWS CDK librarys.
 Home-page: https://github.com/neilkuan/cdk-common.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-common.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

