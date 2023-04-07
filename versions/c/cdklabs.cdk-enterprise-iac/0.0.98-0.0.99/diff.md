# Comparing `tmp/cdklabs.cdk-enterprise-iac-0.0.98.tar.gz` & `tmp/cdklabs.cdk-enterprise-iac-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.cdk-enterprise-iac-0.0.98.tar", last modified: Sat Dec  3 00:34:14 2022, max compression
+gzip compressed data, was "cdklabs.cdk-enterprise-iac-0.0.99.tar", last modified: Sun Dec  4 00:33:58 2022, max compression
```

## Comparing `cdklabs.cdk-enterprise-iac-0.0.98.tar` & `cdklabs.cdk-enterprise-iac-0.0.99.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.529137 cdklabs.cdk-enterprise-iac-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      103 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)    71696 2022-12-03 00:34:14.529137 cdklabs.cdk-enterprise-iac-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    70752 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-03 00:34:14.529137 cdklabs.cdk-enterprise-iac-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1800 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.517137 cdklabs.cdk-enterprise-iac-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.517137 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.517137 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/
--rw-r--r--   0 runner    (1001) docker     (123)   143262 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.517137 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      427 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123) 10386789 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/_jsii/cdk-enterprise-iac@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-03 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 00:34:14.517137 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    71696 2022-12-03 00:34:13.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      533 2022-12-03 00:34:14.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-03 00:34:14.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-03 00:34:14.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2022-12-03 00:34:14.000000 cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.570299 cdklabs.cdk-enterprise-iac-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)    71696 2022-12-04 00:33:58.570299 cdklabs.cdk-enterprise-iac-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    70752 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-04 00:33:58.570299 cdklabs.cdk-enterprise-iac-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1800 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.554299 cdklabs.cdk-enterprise-iac-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.554299 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.558299 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/
+-rw-r--r--   0 runner    (1001) docker     (123)   143262 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.558299 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123) 10386790 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/_jsii/cdk-enterprise-iac@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-04 00:33:41.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-04 00:33:58.558299 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    71696 2022-12-04 00:33:57.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      533 2022-12-04 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-04 00:33:57.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-04 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2022-12-04 00:33:58.000000 cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/top_level.txt
```

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/LICENSE` & `cdklabs.cdk-enterprise-iac-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/PKG-INFO` & `cdklabs.cdk-enterprise-iac-0.0.99/PKG-INFO`

 * *Files identical despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-enterprise-iac
-Version: 0.0.98
+Version: 0.0.99
 Summary: @cdklabs/cdk-enterprise-iac
 Home-page: https://github.com/cdklabs/cdk-enterprise-iac.git
 Author: Taylor Ondrey<ondreyt@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-enterprise-iac.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/README.md` & `cdklabs.cdk-enterprise-iac-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/setup.py` & `cdklabs.cdk-enterprise-iac-0.0.99/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.cdk-enterprise-iac",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "@cdklabs/cdk-enterprise-iac",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-enterprise-iac.git",
     "long_description_content_type": "text/markdown",
     "author": "Taylor Ondrey<ondreyt@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdklabs.cdk_enterprise_iac",
         "cdklabs.cdk_enterprise_iac._jsii"
     ],
     "package_data": {
         "cdklabs.cdk_enterprise_iac._jsii": [
-            "cdk-enterprise-iac@0.0.98.jsii.tgz"
+            "cdk-enterprise-iac@0.0.99.jsii.tgz"
         ],
         "cdklabs.cdk_enterprise_iac": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs/cdk_enterprise_iac/__init__.py` & `cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs/cdk_enterprise_iac/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/PKG-INFO` & `cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/PKG-INFO`

 * *Files identical despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-enterprise-iac
-Version: 0.0.98
+Version: 0.0.99
 Summary: @cdklabs/cdk-enterprise-iac
 Home-page: https://github.com/cdklabs/cdk-enterprise-iac.git
 Author: Taylor Ondrey<ondreyt@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-enterprise-iac.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-enterprise-iac-0.0.98/src/cdklabs.cdk_enterprise_iac.egg-info/SOURCES.txt` & `cdklabs.cdk-enterprise-iac-0.0.99/src/cdklabs.cdk_enterprise_iac.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/cdklabs.cdk_enterprise_iac.egg-info/SOURCES.txt
 src/cdklabs.cdk_enterprise_iac.egg-info/dependency_links.txt
 src/cdklabs.cdk_enterprise_iac.egg-info/requires.txt
 src/cdklabs.cdk_enterprise_iac.egg-info/top_level.txt
 src/cdklabs/cdk_enterprise_iac/__init__.py
 src/cdklabs/cdk_enterprise_iac/py.typed
 src/cdklabs/cdk_enterprise_iac/_jsii/__init__.py
-src/cdklabs/cdk_enterprise_iac/_jsii/cdk-enterprise-iac@0.0.98.jsii.tgz
+src/cdklabs/cdk_enterprise_iac/_jsii/cdk-enterprise-iac@0.0.99.jsii.tgz
```

