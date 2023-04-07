# Comparing `tmp/cdklabs.cdk-ethereum-node-0.0.98.tar.gz` & `tmp/cdklabs.cdk-ethereum-node-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.cdk-ethereum-node-0.0.98.tar", last modified: Sat Feb  4 00:24:29 2023, max compression
+gzip compressed data, was "cdklabs.cdk-ethereum-node-0.0.99.tar", last modified: Sun Feb  5 00:24:57 2023, max compression
```

## Comparing `cdklabs.cdk-ethereum-node-0.0.98.tar` & `cdklabs.cdk-ethereum-node-0.0.99.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)      933 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4105 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1823 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/
--rw-r--r--   0 runner    (1001) docker     (123)    11551 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19424 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/_jsii/cdk-ethereum-node@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-04 00:24:16.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-04 00:24:29.406276 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-02-04 00:24:28.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      516 2023-02-04 00:24:29.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-04 00:24:28.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-02-04 00:24:29.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-02-04 00:24:29.000000 cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.982340 cdklabs.cdk-ethereum-node-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)      933 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-02-05 00:24:57.982340 cdklabs.cdk-ethereum-node-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4105 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-05 00:24:57.982340 cdklabs.cdk-ethereum-node-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1823 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.978340 cdklabs.cdk-ethereum-node-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.978340 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.982340 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/
+-rw-r--r--   0 runner    (1001) docker     (123)    11551 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.982340 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19424 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/_jsii/cdk-ethereum-node@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-05 00:24:43.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 00:24:57.978340 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5056 2023-02-05 00:24:57.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      516 2023-02-05 00:24:57.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-05 00:24:57.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-02-05 00:24:57.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-02-05 00:24:57.000000 cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/top_level.txt
```

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/LICENSE` & `cdklabs.cdk-ethereum-node-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/PKG-INFO` & `cdklabs.cdk-ethereum-node-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-ethereum-node
-Version: 0.0.98
+Version: 0.0.99
 Summary: CDK construct to deploy an Ethereum node running on Amazon Managed Blockchain
 Home-page: https://github.com/cdklabs/cdk-ethereum-node.git
 Author: Amazon Web Services
 License: MIT-0
 Project-URL: Source, https://github.com/cdklabs/cdk-ethereum-node.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/README.md` & `cdklabs.cdk-ethereum-node-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/setup.py` & `cdklabs.cdk-ethereum-node-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.cdk-ethereum-node",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "CDK construct to deploy an Ethereum node running on Amazon Managed Blockchain",
     "license": "MIT-0",
     "url": "https://github.com/cdklabs/cdk-ethereum-node.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdklabs.cdk_ethereum_node",
         "cdklabs.cdk_ethereum_node._jsii"
     ],
     "package_data": {
         "cdklabs.cdk_ethereum_node._jsii": [
-            "cdk-ethereum-node@0.0.98.jsii.tgz"
+            "cdk-ethereum-node@0.0.99.jsii.tgz"
         ],
         "cdklabs.cdk_ethereum_node": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs/cdk_ethereum_node/__init__.py` & `cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs/cdk_ethereum_node/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/PKG-INFO` & `cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-ethereum-node
-Version: 0.0.98
+Version: 0.0.99
 Summary: CDK construct to deploy an Ethereum node running on Amazon Managed Blockchain
 Home-page: https://github.com/cdklabs/cdk-ethereum-node.git
 Author: Amazon Web Services
 License: MIT-0
 Project-URL: Source, https://github.com/cdklabs/cdk-ethereum-node.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-ethereum-node-0.0.98/src/cdklabs.cdk_ethereum_node.egg-info/SOURCES.txt` & `cdklabs.cdk-ethereum-node-0.0.99/src/cdklabs.cdk_ethereum_node.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdklabs.cdk_ethereum_node.egg-info/SOURCES.txt
 src/cdklabs.cdk_ethereum_node.egg-info/dependency_links.txt
 src/cdklabs.cdk_ethereum_node.egg-info/requires.txt
 src/cdklabs.cdk_ethereum_node.egg-info/top_level.txt
 src/cdklabs/cdk_ethereum_node/__init__.py
 src/cdklabs/cdk_ethereum_node/py.typed
 src/cdklabs/cdk_ethereum_node/_jsii/__init__.py
-src/cdklabs/cdk_ethereum_node/_jsii/cdk-ethereum-node@0.0.98.jsii.tgz
+src/cdklabs/cdk_ethereum_node/_jsii/cdk-ethereum-node@0.0.99.jsii.tgz
```

