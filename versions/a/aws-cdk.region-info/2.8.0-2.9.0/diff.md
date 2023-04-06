# Comparing `tmp/aws-cdk.region-info-2.8.0.tar.gz` & `tmp/aws-cdk.region-info-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/@aws-cdk/region-info/dist/python/aws-cdk.region-info-2.8.0.tar", last modified: Thu Jan 13 17:15:13 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/@aws-cdk/region-info/dist/python/aws-cdk.region-info-2.9.0.tar", last modified: Wed Jan 26 10:30:18 2022, max compression
```

## Comparing `aws-cdk.region-info-2.8.0.tar` & `aws-cdk.region-info-2.9.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      113 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     4068 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3082 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1697 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/
--rw-r--r--   0 root         (0) root         (0)    23975 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/_jsii/
--rw-r--r--   0 root         (0) root         (0)      318 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)    77218 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/_jsii/region-info@2.8.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:09.000000 aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4068 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      462 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       39 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 17:15:12.000000 aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      113 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     4068 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3082 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1697 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/
+-rw-r--r--   0 root         (0) root         (0)    23975 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      318 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    77441 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/_jsii/region-info@2.9.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:14.000000 aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4068 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      462 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       39 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 10:30:18.000000 aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/top_level.txt
```

### Comparing `aws-cdk.region-info-2.8.0/LICENSE` & `aws-cdk.region-info-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.region-info-2.8.0/PKG-INFO` & `aws-cdk.region-info-2.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.region-info
-Version: 2.8.0
+Version: 2.9.0
 Summary: AWS region information, such as service principal names
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.region-info-2.8.0/README.md` & `aws-cdk.region-info-2.9.0/README.md`

 * *Files identical despite different names*

### Comparing `aws-cdk.region-info-2.8.0/setup.py` & `aws-cdk.region-info-2.9.0/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.region-info",
-    "version": "2.8.0",
+    "version": "2.9.0",
     "description": "AWS region information, such as service principal names",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "aws_cdk.region_info",
         "aws_cdk.region_info._jsii"
     ],
     "package_data": {
         "aws_cdk.region_info._jsii": [
-            "region-info@2.8.0.jsii.tgz"
+            "region-info@2.9.0.jsii.tgz"
         ],
         "aws_cdk.region_info": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `aws-cdk.region-info-2.8.0/src/aws_cdk/region_info/__init__.py` & `aws-cdk.region-info-2.9.0/src/aws_cdk/region_info/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.region-info-2.8.0/src/aws_cdk.region_info.egg-info/PKG-INFO` & `aws-cdk.region-info-2.9.0/src/aws_cdk.region_info.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.region-info
-Version: 2.8.0
+Version: 2.9.0
 Summary: AWS region information, such as service principal names
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

