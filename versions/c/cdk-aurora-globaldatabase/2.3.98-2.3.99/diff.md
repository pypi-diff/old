# Comparing `tmp/cdk-aurora-globaldatabase-2.3.98.tar.gz` & `tmp/cdk-aurora-globaldatabase-2.3.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-aurora-globaldatabase-2.3.98.tar", last modified: Sun Mar 26 00:31:24 2023, max compression
+gzip compressed data, was "cdk-aurora-globaldatabase-2.3.99.tar", last modified: Mon Mar 27 00:28:47 2023, max compression
```

## Comparing `cdk-aurora-globaldatabase-2.3.98.tar` & `cdk-aurora-globaldatabase-2.3.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6927 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 00:31:24.511992 cdk-aurora-globaldatabase-2.3.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/
--rw-r--r--   0 runner    (1001) docker     (123)    58794 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    50640 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/_jsii/cdk-aurora-globaldatabase@2.3.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-26 00:31:12.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 00:31:24.515992 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-26 00:31:24.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-26 00:31:24.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-26 00:31:24.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-03-26 00:31:24.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-03-26 00:31:24.000000 cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 00:28:47.093245 cdk-aurora-globaldatabase-2.3.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-27 00:28:47.089245 cdk-aurora-globaldatabase-2.3.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6927 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-27 00:28:47.093245 cdk-aurora-globaldatabase-2.3.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 00:28:47.089245 cdk-aurora-globaldatabase-2.3.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 00:28:47.089245 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/
+-rw-r--r--   0 runner    (1001) docker     (123)    58794 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 00:28:47.089245 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50641 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/_jsii/cdk-aurora-globaldatabase@2.3.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 00:28:28.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 00:28:47.089245 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     7974 2023-03-27 00:28:47.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-27 00:28:47.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 00:28:47.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-03-27 00:28:47.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-03-27 00:28:47.000000 cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/top_level.txt
```

### Comparing `cdk-aurora-globaldatabase-2.3.98/LICENSE` & `cdk-aurora-globaldatabase-2.3.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-aurora-globaldatabase-2.3.98/PKG-INFO` & `cdk-aurora-globaldatabase-2.3.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-aurora-globaldatabase
-Version: 2.3.98
+Version: 2.3.99
 Summary: cdk-aurora-globaldatabase is an AWS CDK construct library that provides Cross Region Create Global Aurora RDS Databases.
 Home-page: https://github.com/neilkuan/cdk-aurora-globaldatabase.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-aurora-globaldatabase.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdk-aurora-globaldatabase-2.3.98/README.md` & `cdk-aurora-globaldatabase-2.3.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-aurora-globaldatabase-2.3.98/setup.py` & `cdk-aurora-globaldatabase-2.3.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-aurora-globaldatabase",
-    "version": "2.3.98",
+    "version": "2.3.99",
     "description": "cdk-aurora-globaldatabase is an AWS CDK construct library that provides Cross Region Create Global Aurora RDS Databases.",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-aurora-globaldatabase.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_aurora_globaldatabase",
         "cdk_aurora_globaldatabase._jsii"
     ],
     "package_data": {
         "cdk_aurora_globaldatabase._jsii": [
-            "cdk-aurora-globaldatabase@2.3.98.jsii.tgz"
+            "cdk-aurora-globaldatabase@2.3.99.jsii.tgz"
         ],
         "cdk_aurora_globaldatabase": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase/__init__.py` & `cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/PKG-INFO` & `cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-aurora-globaldatabase
-Version: 2.3.98
+Version: 2.3.99
 Summary: cdk-aurora-globaldatabase is an AWS CDK construct library that provides Cross Region Create Global Aurora RDS Databases.
 Home-page: https://github.com/neilkuan/cdk-aurora-globaldatabase.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-aurora-globaldatabase.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdk-aurora-globaldatabase-2.3.98/src/cdk_aurora_globaldatabase.egg-info/SOURCES.txt` & `cdk-aurora-globaldatabase-2.3.99/src/cdk_aurora_globaldatabase.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdk_aurora_globaldatabase/py.typed
 src/cdk_aurora_globaldatabase.egg-info/PKG-INFO
 src/cdk_aurora_globaldatabase.egg-info/SOURCES.txt
 src/cdk_aurora_globaldatabase.egg-info/dependency_links.txt
 src/cdk_aurora_globaldatabase.egg-info/requires.txt
 src/cdk_aurora_globaldatabase.egg-info/top_level.txt
 src/cdk_aurora_globaldatabase/_jsii/__init__.py
-src/cdk_aurora_globaldatabase/_jsii/cdk-aurora-globaldatabase@2.3.98.jsii.tgz
+src/cdk_aurora_globaldatabase/_jsii/cdk-aurora-globaldatabase@2.3.99.jsii.tgz
```

