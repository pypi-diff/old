# Comparing `tmp/aws-cdk.cloud-assembly-schema-2.8.0.tar.gz` & `tmp/aws-cdk.cloud-assembly-schema-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/@aws-cdk/cloud-assembly-schema/dist/python/aws-cdk.cloud-assembly-schema-2.8.0.tar", last modified: Thu Jan 13 17:15:12 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/@aws-cdk/cloud-assembly-schema/dist/python/aws-cdk.cloud-assembly-schema-2.9.0.tar", last modified: Wed Jan 26 10:30:18 2022, max compression
```

## Comparing `aws-cdk.cloud-assembly-schema-2.8.0.tar` & `aws-cdk.cloud-assembly-schema-2.9.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     3871 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     3928 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2966 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1723 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/
--rw-r--r--   0 root         (0) root         (0)   153569 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/_jsii/
--rw-r--r--   0 root         (0) root         (0)      351 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)   126700 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/_jsii/cloud-assembly-schema@2.8.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:09.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/
--rw-r--r--   0 root         (0) root         (0)     3928 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      562 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       39 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 17:15:12.000000 aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     3871 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     3928 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2966 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1723 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/
+-rw-r--r--   0 root         (0) root         (0)   153569 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      351 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   126700 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/_jsii/cloud-assembly-schema@2.9.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:14.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 10:30:18.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     3928 2022-01-26 10:30:17.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      562 2022-01-26 10:30:17.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 10:30:17.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       39 2022-01-26 10:30:17.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 10:30:17.000000 aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/top_level.txt
```

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/LICENSE` & `aws-cdk.cloud-assembly-schema-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/NOTICE` & `aws-cdk.cloud-assembly-schema-2.9.0/NOTICE`

 * *Files identical despite different names*

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/PKG-INFO` & `aws-cdk.cloud-assembly-schema-2.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.cloud-assembly-schema
-Version: 2.8.0
+Version: 2.9.0
 Summary: Cloud Assembly Schema
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/README.md` & `aws-cdk.cloud-assembly-schema-2.9.0/README.md`

 * *Files identical despite different names*

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/setup.py` & `aws-cdk.cloud-assembly-schema-2.9.0/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.cloud-assembly-schema",
-    "version": "2.8.0",
+    "version": "2.9.0",
     "description": "Cloud Assembly Schema",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "aws_cdk.cloud_assembly_schema",
         "aws_cdk.cloud_assembly_schema._jsii"
     ],
     "package_data": {
         "aws_cdk.cloud_assembly_schema._jsii": [
-            "cloud-assembly-schema@2.8.0.jsii.tgz"
+            "cloud-assembly-schema@2.9.0.jsii.tgz"
         ],
         "aws_cdk.cloud_assembly_schema": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk/cloud_assembly_schema/__init__.py` & `aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk/cloud_assembly_schema/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/PKG-INFO` & `aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.cloud-assembly-schema
-Version: 2.8.0
+Version: 2.9.0
 Summary: Cloud Assembly Schema
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.cloud-assembly-schema-2.8.0/src/aws_cdk.cloud_assembly_schema.egg-info/SOURCES.txt` & `aws-cdk.cloud-assembly-schema-2.9.0/src/aws_cdk.cloud_assembly_schema.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/aws_cdk.cloud_assembly_schema.egg-info/SOURCES.txt
 src/aws_cdk.cloud_assembly_schema.egg-info/dependency_links.txt
 src/aws_cdk.cloud_assembly_schema.egg-info/requires.txt
 src/aws_cdk.cloud_assembly_schema.egg-info/top_level.txt
 src/aws_cdk/cloud_assembly_schema/__init__.py
 src/aws_cdk/cloud_assembly_schema/py.typed
 src/aws_cdk/cloud_assembly_schema/_jsii/__init__.py
-src/aws_cdk/cloud_assembly_schema/_jsii/cloud-assembly-schema@2.8.0.jsii.tgz
+src/aws_cdk/cloud_assembly_schema/_jsii/cloud-assembly-schema@2.9.0.jsii.tgz
```

