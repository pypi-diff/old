# Comparing `tmp/aws-cdk.asset-node-proxy-agent-v5-2.0.98.tar.gz` & `tmp/aws-cdk.asset-node-proxy-agent-v5-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aws-cdk.asset-node-proxy-agent-v5-2.0.98.tar", last modified: Tue Mar 28 00:20:31 2023, max compression
+gzip compressed data, was "aws-cdk.asset-node-proxy-agent-v5-2.0.99.tar", last modified: Wed Mar 29 00:22:48 2023, max compression
```

## Comparing `aws-cdk.asset-node-proxy-agent-v5-2.0.98.tar` & `aws-cdk.asset-node-proxy-agent-v5-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       68 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1730 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk/asset_node_proxy_agent_v5/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)  1320294 2023-03-28 00:20:20.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/asset-node-proxy-agent-v5@2.0.98.jsii.tgz
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:31.404527 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-28 00:20:31.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-03-28 00:20:31.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 00:20:31.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-28 00:20:31.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-03-28 00:20:31.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.604247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-29 00:22:48.604247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       68 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 00:22:48.604247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1730 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.600247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.600247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.600247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk/asset_node_proxy_agent_v5/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.604247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)  1320562 2023-03-29 00:22:36.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk/asset_node_proxy_agent_v5/_jsii/asset-node-proxy-agent-v5@2.0.99.jsii.tgz
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:22:48.604247 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-29 00:22:48.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-03-29 00:22:48.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 00:22:48.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-29 00:22:48.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-03-29 00:22:48.000000 aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/top_level.txt
```

### Comparing `aws-cdk.asset-node-proxy-agent-v5-2.0.98/LICENSE` & `aws-cdk.asset-node-proxy-agent-v5-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.asset-node-proxy-agent-v5-2.0.98/PKG-INFO` & `aws-cdk.asset-node-proxy-agent-v5-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.asset-node-proxy-agent-v5
-Version: 2.0.98
+Version: 2.0.99
 Summary: @aws-cdk/asset-node-proxy-agent-v5
 Home-page: https://github.com/cdklabs/awscdk-asset-node-proxy-agent#readme
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/awscdk-asset-node-proxy-agent.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `aws-cdk.asset-node-proxy-agent-v5-2.0.98/setup.py` & `aws-cdk.asset-node-proxy-agent-v5-2.0.99/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.asset-node-proxy-agent-v5",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "@aws-cdk/asset-node-proxy-agent-v5",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/awscdk-asset-node-proxy-agent#readme",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services<aws-cdk-dev@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -21,15 +21,15 @@
         "": "src"
     },
     "packages": [
         "aws_cdk.asset_node_proxy_agent_v5._jsii"
     ],
     "package_data": {
         "aws_cdk.asset_node_proxy_agent_v5._jsii": [
-            "asset-node-proxy-agent-v5@2.0.98.jsii.tgz"
+            "asset-node-proxy-agent-v5@2.0.99.jsii.tgz"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
         "jsii>=1.79.0, <2.0.0",
         "publication>=0.0.3",
         "typeguard~=2.13.3"
```

### Comparing `aws-cdk.asset-node-proxy-agent-v5-2.0.98/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/PKG-INFO` & `aws-cdk.asset-node-proxy-agent-v5-2.0.99/src/aws_cdk.asset_node_proxy_agent_v5.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.asset-node-proxy-agent-v5
-Version: 2.0.98
+Version: 2.0.99
 Summary: @aws-cdk/asset-node-proxy-agent-v5
 Home-page: https://github.com/cdklabs/awscdk-asset-node-proxy-agent#readme
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/awscdk-asset-node-proxy-agent.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

