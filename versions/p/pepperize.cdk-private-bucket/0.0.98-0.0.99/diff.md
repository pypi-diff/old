# Comparing `tmp/pepperize.cdk-private-bucket-0.0.98.tar.gz` & `tmp/pepperize.cdk-private-bucket-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-private-bucket-0.0.98.tar", last modified: Tue May  3 10:50:59 2022, max compression
+gzip compressed data, was "pepperize.cdk-private-bucket-0.0.99.tar", last modified: Thu May  5 06:10:47 2022, max compression
```

## Comparing `pepperize.cdk-private-bucket-0.0.98.tar` & `pepperize.cdk-private-bucket-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3037 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2061 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1831 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3037 2022-05-03 10:50:58.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      544 2022-05-03 10:50:58.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-03 10:50:58.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-03 10:50:58.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       29 2022-05-03 10:50:58.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/
--rw-r--r--   0 runner    (1001) docker     (121)    33726 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-03 10:50:59.008199 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      395 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14307 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/_jsii/cdk-private-bucket@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-03 10:50:48.000000 pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-05 06:10:47.876505 pepperize.cdk-private-bucket-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3037 2022-05-05 06:10:47.876505 pepperize.cdk-private-bucket-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2061 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-05 06:10:47.876505 pepperize.cdk-private-bucket-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1831 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-05 06:10:47.872505 pepperize.cdk-private-bucket-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-05 06:10:47.872505 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3037 2022-05-05 06:10:47.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      544 2022-05-05 06:10:47.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-05 06:10:47.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-05 06:10:47.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       29 2022-05-05 06:10:47.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-05 06:10:47.872505 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/
+-rw-r--r--   0 runner    (1001) docker     (121)    33726 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-05 06:10:47.876505 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      395 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14307 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/_jsii/cdk-private-bucket@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-05 06:10:32.000000 pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/py.typed
```

### Comparing `pepperize.cdk-private-bucket-0.0.98/LICENSE` & `pepperize.cdk-private-bucket-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-private-bucket-0.0.98/PKG-INFO` & `pepperize.cdk-private-bucket-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-private-bucket
-Version: 0.0.98
+Version: 0.0.99
 Summary: This project provides a CDK construct for creating private S3 bucket.
 Home-page: https://github.com/pepperize/cdk-private-bucket.git
 Author: Andreas Forster<andreas.forster@pepperize.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-private-bucket.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-private-bucket-0.0.98/README.md` & `pepperize.cdk-private-bucket-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-private-bucket-0.0.98/setup.py` & `pepperize.cdk-private-bucket-0.0.99/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-private-bucket",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "This project provides a CDK construct for creating private S3 bucket.",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-private-bucket.git",
     "long_description_content_type": "text/markdown",
     "author": "Andreas Forster<andreas.forster@pepperize.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_private_bucket",
         "pepperize_cdk_private_bucket._jsii"
     ],
     "package_data": {
         "pepperize_cdk_private_bucket._jsii": [
-            "cdk-private-bucket@0.0.98.jsii.tgz"
+            "cdk-private-bucket@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_private_bucket": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/PKG-INFO` & `pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-private-bucket
-Version: 0.0.98
+Version: 0.0.99
 Summary: This project provides a CDK construct for creating private S3 bucket.
 Home-page: https://github.com/pepperize/cdk-private-bucket.git
 Author: Andreas Forster<andreas.forster@pepperize.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-private-bucket.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-private-bucket-0.0.98/src/pepperize.cdk_private_bucket.egg-info/SOURCES.txt` & `pepperize.cdk-private-bucket-0.0.99/src/pepperize.cdk_private_bucket.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_private_bucket.egg-info/SOURCES.txt
 src/pepperize.cdk_private_bucket.egg-info/dependency_links.txt
 src/pepperize.cdk_private_bucket.egg-info/requires.txt
 src/pepperize.cdk_private_bucket.egg-info/top_level.txt
 src/pepperize_cdk_private_bucket/__init__.py
 src/pepperize_cdk_private_bucket/py.typed
 src/pepperize_cdk_private_bucket/_jsii/__init__.py
-src/pepperize_cdk_private_bucket/_jsii/cdk-private-bucket@0.0.98.jsii.tgz
+src/pepperize_cdk_private_bucket/_jsii/cdk-private-bucket@0.0.99.jsii.tgz
```

### Comparing `pepperize.cdk-private-bucket-0.0.98/src/pepperize_cdk_private_bucket/__init__.py` & `pepperize.cdk-private-bucket-0.0.99/src/pepperize_cdk_private_bucket/__init__.py`

 * *Files identical despite different names*

