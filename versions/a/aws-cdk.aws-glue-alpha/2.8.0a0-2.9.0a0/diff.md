# Comparing `tmp/aws-cdk.aws-glue-alpha-2.8.0a0.tar.gz` & `tmp/aws-cdk.aws-glue-alpha-2.9.0a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/individual-packages/aws-glue/dist/python/aws-cdk.aws-glue-alpha-2.8.0a0.tar", last modified: Thu Jan 13 18:05:52 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/individual-packages/aws-glue/dist/python/aws-cdk.aws-glue-alpha-2.9.0a0.tar", last modified: Wed Jan 26 11:22:06 2022, max compression
```

## Comparing `aws-cdk.aws-glue-alpha-2.8.0a0.tar` & `aws-cdk.aws-glue-alpha-2.9.0a0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      113 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    18455 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    17493 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1774 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/
--rw-r--r--   0 root         (0) root         (0)   304051 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/_jsii/
--rw-r--r--   0 root         (0) root         (0)      399 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)   128193 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/_jsii/aws-glue-alpha@2.8.0-alpha.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:47.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/
--rw-r--r--   0 root         (0) root         (0)    18455 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      500 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       92 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 18:05:52.000000 aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      113 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    18455 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    17493 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1774 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/
+-rw-r--r--   0 root         (0) root         (0)   304051 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      399 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   128286 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/_jsii/aws-glue-alpha@2.9.0-alpha.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:01.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    18455 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      500 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       92 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 11:22:06.000000 aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/top_level.txt
```

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/LICENSE` & `aws-cdk.aws-glue-alpha-2.9.0a0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/PKG-INFO` & `aws-cdk.aws-glue-alpha-2.9.0a0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-glue-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: The CDK Construct Library for AWS::Glue
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/README.md` & `aws-cdk.aws-glue-alpha-2.9.0a0/README.md`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/setup.py` & `aws-cdk.aws-glue-alpha-2.9.0a0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.aws-glue-alpha",
-    "version": "2.8.0.a0",
+    "version": "2.9.0.a0",
     "description": "The CDK Construct Library for AWS::Glue",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,23 +22,23 @@
     },
     "packages": [
         "aws_cdk.aws_glue_alpha",
         "aws_cdk.aws_glue_alpha._jsii"
     ],
     "package_data": {
         "aws_cdk.aws_glue_alpha._jsii": [
-            "aws-glue-alpha@2.8.0-alpha.0.jsii.tgz"
+            "aws-glue-alpha@2.9.0-alpha.0.jsii.tgz"
         ],
         "aws_cdk.aws_glue_alpha": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "aws-cdk-lib>=2.8.0, <3.0.0",
+        "aws-cdk-lib>=2.9.0, <3.0.0",
         "constructs>=10.0.0, <11.0.0",
         "jsii>=1.52.1, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
```

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk/aws_glue_alpha/__init__.py` & `aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk/aws_glue_alpha/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-glue-alpha-2.8.0a0/src/aws_cdk.aws_glue_alpha.egg-info/PKG-INFO` & `aws-cdk.aws-glue-alpha-2.9.0a0/src/aws_cdk.aws_glue_alpha.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-glue-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: The CDK Construct Library for AWS::Glue
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

