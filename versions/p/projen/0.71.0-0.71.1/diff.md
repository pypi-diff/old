# Comparing `tmp/projen-0.71.0.tar.gz` & `tmp/projen-0.71.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "projen-0.71.0.tar", last modified: Thu Apr  6 16:10:07 2023, max compression
+gzip compressed data, was "projen-0.71.1.tar", last modified: Fri Apr  7 00:48:24 2023, max compression
```

## Comparing `projen-0.71.0.tar` & `projen-0.71.1.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.451689 projen-0.71.0/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 16:09:55.000000 projen-0.71.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 16:09:55.000000 projen-0.71.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-06 16:10:07.451689 projen-0.71.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    54524 2023-04-06 16:09:55.000000 projen-0.71.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-06 16:09:55.000000 projen-0.71.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 16:10:07.451689 projen-0.71.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-06 16:09:55.000000 projen-0.71.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.435689 projen-0.71.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.439689 projen-0.71.0/src/projen/
--rw-r--r--   0 runner    (1001) docker     (123)   579961 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.439689 projen-0.71.0/src/projen/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/_jsii/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.443689 projen-0.71.0/src/projen/_jsii/bin/
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/_jsii/bin/projen
--rw-r--r--   0 runner    (1001) docker     (123)  3348765 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/_jsii/projen@0.71.0.jsii.tgz
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.443689 projen-0.71.0/src/projen/awscdk/
--rw-r--r--   0 runner    (1001) docker     (123)  1031705 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/awscdk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.443689 projen-0.71.0/src/projen/build/
--rw-r--r--   0 runner    (1001) docker     (123)    39873 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/build/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.443689 projen-0.71.0/src/projen/cdk/
--rw-r--r--   0 runner    (1001) docker     (123)   475192 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/cdk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/cdk8s/
--rw-r--r--   0 runner    (1001) docker     (123)   568763 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/cdk8s/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/cdktf/
--rw-r--r--   0 runner    (1001) docker     (123)   210426 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/cdktf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/circleci/
--rw-r--r--   0 runner    (1001) docker     (123)    75837 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/circleci/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/github/
--rw-r--r--   0 runner    (1001) docker     (123)   275214 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/github/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)   235582 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/github/workflows/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/gitlab/
--rw-r--r--   0 runner    (1001) docker     (123)   192753 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/gitlab/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/java/
--rw-r--r--   0 runner    (1001) docker     (123)   174928 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/java/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/javascript/
--rw-r--r--   0 runner    (1001) docker     (123)   585936 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/javascript/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/python/
--rw-r--r--   0 runner    (1001) docker     (123)   187110 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/python/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/release/
--rw-r--r--   0 runner    (1001) docker     (123)   246151 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/release/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.447689 projen-0.71.0/src/projen/typescript/
--rw-r--r--   0 runner    (1001) docker     (123)   423064 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/typescript/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.451689 projen-0.71.0/src/projen/vscode/
--rw-r--r--   0 runner    (1001) docker     (123)    54316 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/vscode/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.451689 projen-0.71.0/src/projen/web/
--rw-r--r--   0 runner    (1001) docker     (123)   745214 2023-04-06 16:09:55.000000 projen-0.71.0/src/projen/web/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:10:07.439689 projen-0.71.0/src/projen.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-06 16:10:07.000000 projen-0.71.0/src/projen.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-06 16:10:07.000000 projen-0.71.0/src/projen.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:10:07.000000 projen-0.71.0/src/projen.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 16:10:07.000000 projen-0.71.0/src/projen.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 16:10:07.000000 projen-0.71.0/src/projen.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.835705 projen-0.71.1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-07 00:48:12.000000 projen-0.71.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 00:48:12.000000 projen-0.71.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 00:48:24.835705 projen-0.71.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    54524 2023-04-07 00:48:12.000000 projen-0.71.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-07 00:48:12.000000 projen-0.71.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 00:48:24.835705 projen-0.71.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-07 00:48:12.000000 projen-0.71.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.819705 projen-0.71.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.823705 projen-0.71.1/src/projen/
+-rw-r--r--   0 runner    (1001) docker     (123)   579961 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.823705 projen-0.71.1/src/projen/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/_jsii/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/_jsii/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/_jsii/bin/projen
+-rw-r--r--   0 runner    (1001) docker     (123)  3348778 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/_jsii/projen@0.71.1.jsii.tgz
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/awscdk/
+-rw-r--r--   0 runner    (1001) docker     (123)  1031705 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/awscdk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/build/
+-rw-r--r--   0 runner    (1001) docker     (123)    39873 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/build/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/cdk/
+-rw-r--r--   0 runner    (1001) docker     (123)   475192 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/cdk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/cdk8s/
+-rw-r--r--   0 runner    (1001) docker     (123)   568763 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/cdk8s/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/cdktf/
+-rw-r--r--   0 runner    (1001) docker     (123)   210426 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/cdktf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/circleci/
+-rw-r--r--   0 runner    (1001) docker     (123)    75837 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/circleci/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.827705 projen-0.71.1/src/projen/github/
+-rw-r--r--   0 runner    (1001) docker     (123)   275214 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/github/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)   235582 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/github/workflows/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/gitlab/
+-rw-r--r--   0 runner    (1001) docker     (123)   192753 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/gitlab/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/java/
+-rw-r--r--   0 runner    (1001) docker     (123)   174928 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/java/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/javascript/
+-rw-r--r--   0 runner    (1001) docker     (123)   585936 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/javascript/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/python/
+-rw-r--r--   0 runner    (1001) docker     (123)   187110 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/python/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/release/
+-rw-r--r--   0 runner    (1001) docker     (123)   246151 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/release/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/typescript/
+-rw-r--r--   0 runner    (1001) docker     (123)   423064 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/typescript/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/vscode/
+-rw-r--r--   0 runner    (1001) docker     (123)    54316 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/vscode/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.831705 projen-0.71.1/src/projen/web/
+-rw-r--r--   0 runner    (1001) docker     (123)   745214 2023-04-07 00:48:12.000000 projen-0.71.1/src/projen/web/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:48:24.823705 projen-0.71.1/src/projen.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 00:48:24.000000 projen-0.71.1/src/projen.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-07 00:48:24.000000 projen-0.71.1/src/projen.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:48:24.000000 projen-0.71.1/src/projen.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-07 00:48:24.000000 projen-0.71.1/src/projen.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 00:48:24.000000 projen-0.71.1/src/projen.egg-info/top_level.txt
```

### Comparing `projen-0.71.0/LICENSE` & `projen-0.71.1/LICENSE`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/PKG-INFO` & `projen-0.71.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: projen
-Version: 0.71.0
+Version: 0.71.1
 Summary: CDK for software projects
 Home-page: https://github.com/projen/projen.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/projen/projen.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `projen-0.71.0/README.md` & `projen-0.71.1/README.md`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/setup.py` & `projen-0.71.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "projen",
-    "version": "0.71.0",
+    "version": "0.71.1",
     "description": "CDK for software projects",
     "license": "Apache-2.0",
     "url": "https://github.com/projen/projen.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -38,15 +38,15 @@
         "projen.release",
         "projen.typescript",
         "projen.vscode",
         "projen.web"
     ],
     "package_data": {
         "projen._jsii": [
-            "projen@0.71.0.jsii.tgz"
+            "projen@0.71.1.jsii.tgz"
         ],
         "projen": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `projen-0.71.0/src/projen/__init__.py` & `projen-0.71.1/src/projen/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/awscdk/__init__.py` & `projen-0.71.1/src/projen/awscdk/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/build/__init__.py` & `projen-0.71.1/src/projen/build/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/cdk/__init__.py` & `projen-0.71.1/src/projen/cdk/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/cdk8s/__init__.py` & `projen-0.71.1/src/projen/cdk8s/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/cdktf/__init__.py` & `projen-0.71.1/src/projen/cdktf/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/circleci/__init__.py` & `projen-0.71.1/src/projen/circleci/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/github/__init__.py` & `projen-0.71.1/src/projen/github/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/github/workflows/__init__.py` & `projen-0.71.1/src/projen/github/workflows/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/gitlab/__init__.py` & `projen-0.71.1/src/projen/gitlab/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/java/__init__.py` & `projen-0.71.1/src/projen/java/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/javascript/__init__.py` & `projen-0.71.1/src/projen/javascript/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/python/__init__.py` & `projen-0.71.1/src/projen/python/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/release/__init__.py` & `projen-0.71.1/src/projen/release/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/typescript/__init__.py` & `projen-0.71.1/src/projen/typescript/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/vscode/__init__.py` & `projen-0.71.1/src/projen/vscode/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen/web/__init__.py` & `projen-0.71.1/src/projen/web/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.0/src/projen.egg-info/PKG-INFO` & `projen-0.71.1/src/projen.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: projen
-Version: 0.71.0
+Version: 0.71.1
 Summary: CDK for software projects
 Home-page: https://github.com/projen/projen.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/projen/projen.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `projen-0.71.0/src/projen.egg-info/SOURCES.txt` & `projen-0.71.1/src/projen.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 src/projen/py.typed
 src/projen.egg-info/PKG-INFO
 src/projen.egg-info/SOURCES.txt
 src/projen.egg-info/dependency_links.txt
 src/projen.egg-info/requires.txt
 src/projen.egg-info/top_level.txt
 src/projen/_jsii/__init__.py
-src/projen/_jsii/projen@0.71.0.jsii.tgz
+src/projen/_jsii/projen@0.71.1.jsii.tgz
 src/projen/_jsii/bin/projen
 src/projen/awscdk/__init__.py
 src/projen/build/__init__.py
 src/projen/cdk/__init__.py
 src/projen/cdk8s/__init__.py
 src/projen/cdktf/__init__.py
 src/projen/circleci/__init__.py
```

