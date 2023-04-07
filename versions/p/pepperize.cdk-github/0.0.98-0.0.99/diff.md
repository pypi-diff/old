# Comparing `tmp/pepperize.cdk-github-0.0.98.tar.gz` & `tmp/pepperize.cdk-github-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-github-0.0.98.tar", last modified: Mon Dec 12 23:35:11 2022, max compression
+gzip compressed data, was "pepperize.cdk-github-0.0.99.tar", last modified: Mon Dec 12 23:38:59 2022, max compression
```

## Comparing `pepperize.cdk-github-0.0.98.tar` & `pepperize.cdk-github-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     9366 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8288 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1923 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     9366 2022-12-12 23:35:10.000000 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      464 2022-12-12 23:35:11.000000 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-12 23:35:10.000000 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-12 23:35:11.000000 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2022-12-12 23:35:11.000000 pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/
--rw-r--r--   0 runner    (1001) docker     (123)    29924 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:35:11.352002 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      400 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   379285 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/_jsii/cdk-github@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-12 23:34:58.000000 pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     9366 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8288 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1923 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     9366 2022-12-12 23:38:59.000000 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      464 2022-12-12 23:38:59.000000 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-12 23:38:59.000000 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-12 23:38:59.000000 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2022-12-12 23:38:59.000000 pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/
+-rw-r--r--   0 runner    (1001) docker     (123)    29924 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-12 23:38:59.903064 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   379283 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/_jsii/cdk-github@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-12 23:38:47.000000 pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/py.typed
```

### Comparing `pepperize.cdk-github-0.0.98/LICENSE` & `pepperize.cdk-github-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-github-0.0.98/PKG-INFO` & `pepperize.cdk-github-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-github
-Version: 0.0.98
+Version: 0.0.99
 Summary: Manage GitHub resources like repositories, teams, members, integrations and workflows with the AWS CDK as Custom Resources in CloudFormation with [cdk-github](https://github.com/pepperize/cdk-github).
 Home-page: https://github.com/pepperize/cdk-github.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-github.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-github-0.0.98/README.md` & `pepperize.cdk-github-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-github-0.0.98/setup.py` & `pepperize.cdk-github-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-github",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Manage GitHub resources like repositories, teams, members, integrations and workflows with the AWS CDK as Custom Resources in CloudFormation with [cdk-github](https://github.com/pepperize/cdk-github).",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-github.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_github",
         "pepperize_cdk_github._jsii"
     ],
     "package_data": {
         "pepperize_cdk_github._jsii": [
-            "cdk-github@0.0.98.jsii.tgz"
+            "cdk-github@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_github": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-github-0.0.98/src/pepperize.cdk_github.egg-info/PKG-INFO` & `pepperize.cdk-github-0.0.99/src/pepperize.cdk_github.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-github
-Version: 0.0.98
+Version: 0.0.99
 Summary: Manage GitHub resources like repositories, teams, members, integrations and workflows with the AWS CDK as Custom Resources in CloudFormation with [cdk-github](https://github.com/pepperize/cdk-github).
 Home-page: https://github.com/pepperize/cdk-github.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-github.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-github-0.0.98/src/pepperize_cdk_github/__init__.py` & `pepperize.cdk-github-0.0.99/src/pepperize_cdk_github/__init__.py`

 * *Files identical despite different names*

