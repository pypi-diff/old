# Comparing `tmp/aws-cdk.cx-api-2.8.0.tar.gz` & `tmp/aws-cdk.cx-api-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/@aws-cdk/cx-api/dist/python/aws-cdk.cx-api-2.8.0.tar", last modified: Thu Jan 13 17:15:20 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/@aws-cdk/cx-api/dist/python/aws-cdk.cx-api-2.9.0.tar", last modified: Wed Jan 26 10:30:25 2022, max compression
```

## Comparing `aws-cdk.cx-api-2.8.0.tar` & `aws-cdk.cx-api-2.9.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2700 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     1251 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      300 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1685 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/
--rw-r--r--   0 root         (0) root         (0)   119177 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/_jsii/
--rw-r--r--   0 root         (0) root         (0)      352 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)   130370 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/_jsii/cx-api@2.8.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:16.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:20.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1251 2022-01-13 17:15:19.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      412 2022-01-13 17:15:19.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:19.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       76 2022-01-13 17:15:19.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 17:15:19.000000 aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2700 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     1251 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      300 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1685 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/
+-rw-r--r--   0 root         (0) root         (0)   119177 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      352 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   131461 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/_jsii/cx-api@2.9.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:21.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1251 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      412 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       76 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 10:30:25.000000 aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/top_level.txt
```

### Comparing `aws-cdk.cx-api-2.8.0/LICENSE` & `aws-cdk.cx-api-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.cx-api-2.8.0/NOTICE` & `aws-cdk.cx-api-2.9.0/NOTICE`

 * *Files identical despite different names*

### Comparing `aws-cdk.cx-api-2.8.0/PKG-INFO` & `aws-cdk.cx-api-2.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.cx-api
-Version: 2.8.0
+Version: 2.9.0
 Summary: Cloud executable protocol
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.cx-api-2.8.0/setup.py` & `aws-cdk.cx-api-2.9.0/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.cx-api",
-    "version": "2.8.0",
+    "version": "2.9.0",
     "description": "Cloud executable protocol",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,23 +22,23 @@
     },
     "packages": [
         "aws_cdk.cx_api",
         "aws_cdk.cx_api._jsii"
     ],
     "package_data": {
         "aws_cdk.cx_api._jsii": [
-            "cx-api@2.8.0.jsii.tgz"
+            "cx-api@2.9.0.jsii.tgz"
         ],
         "aws_cdk.cx_api": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "aws-cdk.cloud-assembly-schema==2.8.0",
+        "aws-cdk.cloud-assembly-schema==2.9.0",
         "jsii>=1.52.1, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
         "Programming Language :: JavaScript",
```

### Comparing `aws-cdk.cx-api-2.8.0/src/aws_cdk/cx_api/__init__.py` & `aws-cdk.cx-api-2.9.0/src/aws_cdk/cx_api/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.cx-api-2.8.0/src/aws_cdk.cx_api.egg-info/PKG-INFO` & `aws-cdk.cx-api-2.9.0/src/aws_cdk.cx_api.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.cx-api
-Version: 2.8.0
+Version: 2.9.0
 Summary: Cloud executable protocol
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

