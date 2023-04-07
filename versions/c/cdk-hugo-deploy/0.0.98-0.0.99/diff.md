# Comparing `tmp/cdk-hugo-deploy-0.0.98.tar.gz` & `tmp/cdk-hugo-deploy-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-hugo-deploy-0.0.98.tar", last modified: Thu Aug 25 01:48:28 2022, max compression
+gzip compressed data, was "cdk-hugo-deploy-0.0.99.tar", last modified: Fri Aug 26 01:39:46 2022, max compression
```

## Comparing `cdk-hugo-deploy-0.0.98.tar` & `cdk-hugo-deploy-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2873 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1959 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1744 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/
--rw-r--r--   0 runner    (1001) docker     (121)     7839 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      399 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22222 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/_jsii/cdk-hugo-deploy@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-25 01:48:16.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 01:48:28.526343 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2873 2022-08-25 01:48:27.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      424 2022-08-25 01:48:28.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-25 01:48:28.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-08-25 01:48:28.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       16 2022-08-25 01:48:28.000000 cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2873 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1959 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1744 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/
+-rw-r--r--   0 runner    (1001) docker     (121)     7839 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      399 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22221 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/_jsii/cdk-hugo-deploy@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-26 01:39:32.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-26 01:39:46.792340 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2873 2022-08-26 01:39:46.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      424 2022-08-26 01:39:46.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-26 01:39:46.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-08-26 01:39:46.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2022-08-26 01:39:46.000000 cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/top_level.txt
```

### Comparing `cdk-hugo-deploy-0.0.98/LICENSE` & `cdk-hugo-deploy-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-hugo-deploy-0.0.98/PKG-INFO` & `cdk-hugo-deploy-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-hugo-deploy
-Version: 0.0.98
+Version: 0.0.99
 Summary: Deploy Hugo static websites to AWS
 Home-page: https://github.com/maafk/cdk-hugo-deploy.git
 Author: Taylor Ondrey<taylor@taylorondrey.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/maafk/cdk-hugo-deploy.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-hugo-deploy-0.0.98/README.md` & `cdk-hugo-deploy-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-hugo-deploy-0.0.98/setup.py` & `cdk-hugo-deploy-0.0.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-hugo-deploy",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Deploy Hugo static websites to AWS",
     "license": "Apache-2.0",
     "url": "https://github.com/maafk/cdk-hugo-deploy.git",
     "long_description_content_type": "text/markdown",
     "author": "Taylor Ondrey<taylor@taylorondrey.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_hugo_deploy",
         "cdk_hugo_deploy._jsii"
     ],
     "package_data": {
         "cdk_hugo_deploy._jsii": [
-            "cdk-hugo-deploy@0.0.98.jsii.tgz"
+            "cdk-hugo-deploy@0.0.99.jsii.tgz"
         ],
         "cdk_hugo_deploy": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy/__init__.py` & `cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-hugo-deploy-0.0.98/src/cdk_hugo_deploy.egg-info/PKG-INFO` & `cdk-hugo-deploy-0.0.99/src/cdk_hugo_deploy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-hugo-deploy
-Version: 0.0.98
+Version: 0.0.99
 Summary: Deploy Hugo static websites to AWS
 Home-page: https://github.com/maafk/cdk-hugo-deploy.git
 Author: Taylor Ondrey<taylor@taylorondrey.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/maafk/cdk-hugo-deploy.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

