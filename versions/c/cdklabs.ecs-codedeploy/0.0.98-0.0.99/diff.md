# Comparing `tmp/cdklabs.ecs-codedeploy-0.0.98.tar.gz` & `tmp/cdklabs.ecs-codedeploy-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.ecs-codedeploy-0.0.98.tar", last modified: Sat Mar 18 00:23:15 2023, max compression
+gzip compressed data, was "cdklabs.ecs-codedeploy-0.0.99.tar", last modified: Sun Mar 19 00:25:22 2023, max compression
```

## Comparing `cdklabs.ecs-codedeploy-0.0.98.tar` & `cdklabs.ecs-codedeploy-0.0.99.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)     5802 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4832 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.064743 cdklabs.ecs-codedeploy-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.064743 cdklabs.ecs-codedeploy-0.0.98/src/cdk/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/
--rw-r--r--   0 runner    (1001) docker     (123)   162950 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   766164 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/_jsii/cdk-ecs-codedeploy@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-18 00:23:01.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 00:23:15.068743 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5802 2023-03-18 00:23:15.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      481 2023-03-18 00:23:15.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-18 00:23:15.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-18 00:23:15.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-18 00:23:15.000000 cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.667004 cdklabs.ecs-codedeploy-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)     5802 2023-03-19 00:25:22.667004 cdklabs.ecs-codedeploy-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4832 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-19 00:25:22.667004 cdklabs.ecs-codedeploy-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1864 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.663004 cdklabs.ecs-codedeploy-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.663004 cdklabs.ecs-codedeploy-0.0.99/src/cdk/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.663004 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/
+-rw-r--r--   0 runner    (1001) docker     (123)   162950 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.663004 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   766165 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/_jsii/cdk-ecs-codedeploy@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-19 00:25:07.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 00:25:22.667004 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5802 2023-03-19 00:25:22.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      481 2023-03-19 00:25:22.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-19 00:25:22.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-19 00:25:22.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-03-19 00:25:22.000000 cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/top_level.txt
```

### Comparing `cdklabs.ecs-codedeploy-0.0.98/LICENSE` & `cdklabs.ecs-codedeploy-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.ecs-codedeploy-0.0.98/PKG-INFO` & `cdklabs.ecs-codedeploy-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.ecs-codedeploy
-Version: 0.0.98
+Version: 0.0.99
 Summary: CDK Constructs for performing ECS Deployments with CodeDeploy
 Home-page: https://github.com/cdklabs/cdk-ecs-codedeploy
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-ecs-codedeploy
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdklabs.ecs-codedeploy-0.0.98/README.md` & `cdklabs.ecs-codedeploy-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.ecs-codedeploy-0.0.98/setup.py` & `cdklabs.ecs-codedeploy-0.0.99/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.ecs-codedeploy",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "CDK Constructs for performing ECS Deployments with CodeDeploy",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-ecs-codedeploy",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk.ecs_codedeploy",
         "cdk.ecs_codedeploy._jsii"
     ],
     "package_data": {
         "cdk.ecs_codedeploy._jsii": [
-            "cdk-ecs-codedeploy@0.0.98.jsii.tgz"
+            "cdk-ecs-codedeploy@0.0.99.jsii.tgz"
         ],
         "cdk.ecs_codedeploy": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.ecs-codedeploy-0.0.98/src/cdk/ecs_codedeploy/__init__.py` & `cdklabs.ecs-codedeploy-0.0.99/src/cdk/ecs_codedeploy/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.ecs-codedeploy-0.0.98/src/cdklabs.ecs_codedeploy.egg-info/PKG-INFO` & `cdklabs.ecs-codedeploy-0.0.99/src/cdklabs.ecs_codedeploy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.ecs-codedeploy
-Version: 0.0.98
+Version: 0.0.99
 Summary: CDK Constructs for performing ECS Deployments with CodeDeploy
 Home-page: https://github.com/cdklabs/cdk-ecs-codedeploy
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-ecs-codedeploy
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

