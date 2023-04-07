# Comparing `tmp/cdklabs.cdk-hyperledger-fabric-network-0.8.98.tar.gz` & `tmp/cdklabs.cdk-hyperledger-fabric-network-0.8.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.cdk-hyperledger-fabric-network-0.8.98.tar", last modified: Sun Nov 13 00:21:21 2022, max compression
+gzip compressed data, was "cdklabs.cdk-hyperledger-fabric-network-0.8.99.tar", last modified: Mon Nov 14 00:20:47 2022, max compression
```

## Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98.tar` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/
--rw-r--r--   0 runner    (1001) docker     (121)      933 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     5428 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     4426 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1939 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.201909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.201909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/
--rw-r--r--   0 runner    (1001) docker     (121)    52657 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      451 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    57762 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/cdk-hyperledger-fabric-network@0.8.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-13 00:21:03.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-13 00:21:21.205909 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     5428 2022-11-13 00:21:20.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      646 2022-11-13 00:21:21.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-13 00:21:20.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-13 00:21:20.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-11-13 00:21:21.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.627077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/
+-rw-r--r--   0 runner    (1001) docker     (121)      933 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     5428 2022-11-14 00:20:47.627077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     4426 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-14 00:20:47.627077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1939 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.623077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.623077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.623077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/
+-rw-r--r--   0 runner    (1001) docker     (121)    52657 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.627077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      451 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57759 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/_jsii/cdk-hyperledger-fabric-network@0.8.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-14 00:20:35.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-14 00:20:47.623077 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     5428 2022-11-14 00:20:47.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      646 2022-11-14 00:20:47.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-14 00:20:47.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-14 00:20:47.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        8 2022-11-14 00:20:47.000000 cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/top_level.txt
```

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/LICENSE` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/PKG-INFO` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-hyperledger-fabric-network
-Version: 0.8.98
+Version: 0.8.99
 Summary: CDK construct to deploy a Hyperledger Fabric network running on Amazon Managed Blockchain
 Home-page: https://github.com/cdklabs/cdk-hyperledger-fabric-network.git
 Author: Amazon Web Services
 License: MIT-0
 Project-URL: Source, https://github.com/cdklabs/cdk-hyperledger-fabric-network.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/README.md` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/setup.py` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.cdk-hyperledger-fabric-network",
-    "version": "0.8.98",
+    "version": "0.8.99",
     "description": "CDK construct to deploy a Hyperledger Fabric network running on Amazon Managed Blockchain",
     "license": "MIT-0",
     "url": "https://github.com/cdklabs/cdk-hyperledger-fabric-network.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdklabs.cdk_hyperledger_fabric_network",
         "cdklabs.cdk_hyperledger_fabric_network._jsii"
     ],
     "package_data": {
         "cdklabs.cdk_hyperledger_fabric_network._jsii": [
-            "cdk-hyperledger-fabric-network@0.8.98.jsii.tgz"
+            "cdk-hyperledger-fabric-network@0.8.99.jsii.tgz"
         ],
         "cdklabs.cdk_hyperledger_fabric_network": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs/cdk_hyperledger_fabric_network/__init__.py` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs/cdk_hyperledger_fabric_network/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/PKG-INFO` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-hyperledger-fabric-network
-Version: 0.8.98
+Version: 0.8.99
 Summary: CDK construct to deploy a Hyperledger Fabric network running on Amazon Managed Blockchain
 Home-page: https://github.com/cdklabs/cdk-hyperledger-fabric-network.git
 Author: Amazon Web Services
 License: MIT-0
 Project-URL: Source, https://github.com/cdklabs/cdk-hyperledger-fabric-network.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdklabs.cdk-hyperledger-fabric-network-0.8.98/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/SOURCES.txt` & `cdklabs.cdk-hyperledger-fabric-network-0.8.99/src/cdklabs.cdk_hyperledger_fabric_network.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdklabs.cdk_hyperledger_fabric_network.egg-info/SOURCES.txt
 src/cdklabs.cdk_hyperledger_fabric_network.egg-info/dependency_links.txt
 src/cdklabs.cdk_hyperledger_fabric_network.egg-info/requires.txt
 src/cdklabs.cdk_hyperledger_fabric_network.egg-info/top_level.txt
 src/cdklabs/cdk_hyperledger_fabric_network/__init__.py
 src/cdklabs/cdk_hyperledger_fabric_network/py.typed
 src/cdklabs/cdk_hyperledger_fabric_network/_jsii/__init__.py
-src/cdklabs/cdk_hyperledger_fabric_network/_jsii/cdk-hyperledger-fabric-network@0.8.98.jsii.tgz
+src/cdklabs/cdk_hyperledger_fabric_network/_jsii/cdk-hyperledger-fabric-network@0.8.99.jsii.tgz
```

