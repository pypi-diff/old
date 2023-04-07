# Comparing `tmp/cdk-gitlab-runner-2.1.98.tar.gz` & `tmp/cdk-gitlab-runner-2.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-gitlab-runner-2.1.98.tar", last modified: Tue Jan 24 00:22:40 2023, max compression
+gzip compressed data, was "cdk-gitlab-runner-2.1.99.tar", last modified: Wed Jan 25 00:23:42 2023, max compression
```

## Comparing `cdk-gitlab-runner-2.1.98.tar` & `cdk-gitlab-runner-2.1.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 00:22:40.037652 cdk-gitlab-runner-2.1.98/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-01-24 00:22:40.037652 cdk-gitlab-runner-2.1.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     9159 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-24 00:22:40.037652 cdk-gitlab-runner-2.1.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1818 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 00:22:40.033652 cdk-gitlab-runner-2.1.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 00:22:40.033652 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/
--rw-r--r--   0 runner    (1001) docker     (123)    75161 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 00:22:40.037652 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    64741 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/_jsii/cdk-gitlab-runner@2.1.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-24 00:22:24.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-24 00:22:40.037652 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-01-24 00:22:39.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      444 2023-01-24 00:22:40.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-24 00:22:39.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-24 00:22:39.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-01-24 00:22:39.000000 cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 00:23:42.782946 cdk-gitlab-runner-2.1.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-01-25 00:23:42.782946 cdk-gitlab-runner-2.1.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     9159 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-25 00:23:42.782946 cdk-gitlab-runner-2.1.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1818 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 00:23:42.778946 cdk-gitlab-runner-2.1.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 00:23:42.778946 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/
+-rw-r--r--   0 runner    (1001) docker     (123)    75161 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 00:23:42.778946 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64741 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/_jsii/cdk-gitlab-runner@2.1.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-25 00:23:27.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 00:23:42.778946 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    10137 2023-01-25 00:23:42.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      444 2023-01-25 00:23:42.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-25 00:23:42.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-01-25 00:23:42.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-01-25 00:23:42.000000 cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/top_level.txt
```

### Comparing `cdk-gitlab-runner-2.1.98/LICENSE` & `cdk-gitlab-runner-2.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-gitlab-runner-2.1.98/PKG-INFO` & `cdk-gitlab-runner-2.1.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-gitlab-runner
-Version: 2.1.98
+Version: 2.1.99
 Summary: Use AWS CDK to create a gitlab runner, and use gitlab runner to help you execute your Gitlab pipeline job.
 Home-page: https://github.com/neilkuan/cdk-gitlab-runner.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-gitlab-runner.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-gitlab-runner-2.1.98/README.md` & `cdk-gitlab-runner-2.1.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-gitlab-runner-2.1.98/setup.py` & `cdk-gitlab-runner-2.1.99/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-gitlab-runner",
-    "version": "2.1.98",
+    "version": "2.1.99",
     "description": "Use AWS CDK to create a gitlab runner, and use gitlab runner to help you execute your Gitlab pipeline job.",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-gitlab-runner.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_gitlab_runner",
         "cdk_gitlab_runner._jsii"
     ],
     "package_data": {
         "cdk_gitlab_runner._jsii": [
-            "cdk-gitlab-runner@2.1.98.jsii.tgz"
+            "cdk-gitlab-runner@2.1.99.jsii.tgz"
         ],
         "cdk_gitlab_runner": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner/__init__.py` & `cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-gitlab-runner-2.1.98/src/cdk_gitlab_runner.egg-info/PKG-INFO` & `cdk-gitlab-runner-2.1.99/src/cdk_gitlab_runner.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-gitlab-runner
-Version: 2.1.98
+Version: 2.1.99
 Summary: Use AWS CDK to create a gitlab runner, and use gitlab runner to help you execute your Gitlab pipeline job.
 Home-page: https://github.com/neilkuan/cdk-gitlab-runner.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-gitlab-runner.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

