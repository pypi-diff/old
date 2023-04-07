# Comparing `tmp/cdk-docker-image-deployment-0.0.98.tar.gz` & `tmp/cdk-docker-image-deployment-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-docker-image-deployment-0.0.98.tar", last modified: Fri Dec  9 00:29:05 2022, max compression
+gzip compressed data, was "cdk-docker-image-deployment-0.0.99.tar", last modified: Sat Dec 10 00:27:57 2022, max compression
```

## Comparing `cdk-docker-image-deployment-0.0.98.tar` & `cdk-docker-image-deployment-0.0.99.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-09 00:29:05.487670 cdk-docker-image-deployment-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)       67 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)     3730 2022-12-09 00:29:05.487670 cdk-docker-image-deployment-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2604 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-09 00:29:05.487670 cdk-docker-image-deployment-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-09 00:29:05.471669 cdk-docker-image-deployment-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-09 00:29:05.475669 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/
--rw-r--r--   0 runner    (1001) docker     (123)    24643 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-09 00:29:05.475669 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      436 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123) 10342583 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/_jsii/cdk-docker-image-deployment@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-09 00:28:52.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-09 00:29:05.475669 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3730 2022-12-09 00:29:04.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      551 2022-12-09 00:29:05.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-09 00:29:04.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-09 00:29:05.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-09 00:29:05.000000 cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-10 00:27:57.904275 cdk-docker-image-deployment-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)     3730 2022-12-10 00:27:57.904275 cdk-docker-image-deployment-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2604 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-10 00:27:57.904275 cdk-docker-image-deployment-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-10 00:27:57.888275 cdk-docker-image-deployment-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-10 00:27:57.888275 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/
+-rw-r--r--   0 runner    (1001) docker     (123)    24643 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-10 00:27:57.892275 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123) 10343247 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/_jsii/cdk-docker-image-deployment@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-10 00:27:39.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-10 00:27:57.892275 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3730 2022-12-10 00:27:57.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2022-12-10 00:27:57.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-10 00:27:57.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-10 00:27:57.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-10 00:27:57.000000 cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/top_level.txt
```

### Comparing `cdk-docker-image-deployment-0.0.98/LICENSE` & `cdk-docker-image-deployment-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-docker-image-deployment-0.0.98/PKG-INFO` & `cdk-docker-image-deployment-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-docker-image-deployment
-Version: 0.0.98
+Version: 0.0.99
 Summary: This module allows you to copy docker image assets to a repository you control. This can be necessary if you want to build a Docker image in one CDK app and consume it in a different app or outside the CDK.
 Home-page: https://github.com/cdklabs/cdk-docker-image-deployment#readme
 Author: Parker Scanlon
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-docker-image-deployment.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-docker-image-deployment-0.0.98/README.md` & `cdk-docker-image-deployment-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-docker-image-deployment-0.0.98/setup.py` & `cdk-docker-image-deployment-0.0.99/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-docker-image-deployment",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "This module allows you to copy docker image assets to a repository you control. This can be necessary if you want to build a Docker image in one CDK app and consume it in a different app or outside the CDK.",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-docker-image-deployment#readme",
     "long_description_content_type": "text/markdown",
     "author": "Parker Scanlon",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_docker_image_deployment",
         "cdk_docker_image_deployment._jsii"
     ],
     "package_data": {
         "cdk_docker_image_deployment._jsii": [
-            "cdk-docker-image-deployment@0.0.98.jsii.tgz"
+            "cdk-docker-image-deployment@0.0.99.jsii.tgz"
         ],
         "cdk_docker_image_deployment": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment/__init__.py` & `cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/PKG-INFO` & `cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-docker-image-deployment
-Version: 0.0.98
+Version: 0.0.99
 Summary: This module allows you to copy docker image assets to a repository you control. This can be necessary if you want to build a Docker image in one CDK app and consume it in a different app or outside the CDK.
 Home-page: https://github.com/cdklabs/cdk-docker-image-deployment#readme
 Author: Parker Scanlon
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-docker-image-deployment.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-docker-image-deployment-0.0.98/src/cdk_docker_image_deployment.egg-info/SOURCES.txt` & `cdk-docker-image-deployment-0.0.99/src/cdk_docker_image_deployment.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/cdk_docker_image_deployment/py.typed
 src/cdk_docker_image_deployment.egg-info/PKG-INFO
 src/cdk_docker_image_deployment.egg-info/SOURCES.txt
 src/cdk_docker_image_deployment.egg-info/dependency_links.txt
 src/cdk_docker_image_deployment.egg-info/requires.txt
 src/cdk_docker_image_deployment.egg-info/top_level.txt
 src/cdk_docker_image_deployment/_jsii/__init__.py
-src/cdk_docker_image_deployment/_jsii/cdk-docker-image-deployment@0.0.98.jsii.tgz
+src/cdk_docker_image_deployment/_jsii/cdk-docker-image-deployment@0.0.99.jsii.tgz
```

