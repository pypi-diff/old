# Comparing `tmp/aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0.tar.gz` & `tmp/aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/individual-packages/aws-apigatewayv2-authorizers/dist/python/aws-cdk.aws-apigateway", last modified: Thu Jan 13 18:06:06 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/individual-packages/aws-apigatewayv2-authorizers/dist/python/aws-cdk.aws-apigateway", last modified: Wed Jan 26 11:22:21 2022, max compression
```

## Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0.tar` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      113 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    10627 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     9651 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1940 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/
--rw-r--r--   0 root         (0) root         (0)    43110 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/
--rw-r--r--   0 root         (0) root         (0)      483 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)    36862 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/aws-apigatewayv2-authorizers-alpha@2.8.0-alpha.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:06:03.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/
--rw-r--r--   0 root         (0) root         (0)    10627 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      700 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      133 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 18:06:06.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      113 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    10627 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     9651 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1940 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/
+-rw-r--r--   0 root         (0) root         (0)    43110 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      483 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    36953 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/aws-apigatewayv2-authorizers-alpha@2.9.0-alpha.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:18.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    10627 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      700 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      133 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 11:22:21.000000 aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/top_level.txt
```

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/LICENSE` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/PKG-INFO` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-apigatewayv2-authorizers-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: Authorizers for AWS APIGateway V2
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/README.md` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/README.md`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/setup.py` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.aws-apigatewayv2-authorizers-alpha",
-    "version": "2.8.0.a0",
+    "version": "2.9.0.a0",
     "description": "Authorizers for AWS APIGateway V2",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,24 +22,24 @@
     },
     "packages": [
         "aws_cdk.aws_apigatewayv2_authorizers_alpha",
         "aws_cdk.aws_apigatewayv2_authorizers_alpha._jsii"
     ],
     "package_data": {
         "aws_cdk.aws_apigatewayv2_authorizers_alpha._jsii": [
-            "aws-apigatewayv2-authorizers-alpha@2.8.0-alpha.0.jsii.tgz"
+            "aws-apigatewayv2-authorizers-alpha@2.9.0-alpha.0.jsii.tgz"
         ],
         "aws_cdk.aws_apigatewayv2_authorizers_alpha": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "aws-cdk-lib>=2.8.0, <3.0.0",
-        "aws-cdk.aws-apigatewayv2-alpha==2.8.0.a0",
+        "aws-cdk-lib>=2.9.0, <3.0.0",
+        "aws-cdk.aws-apigatewayv2-alpha==2.9.0.a0",
         "constructs>=10.0.0, <11.0.0",
         "jsii>=1.52.1, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
```

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/__init__.py` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk/aws_apigatewayv2_authorizers_alpha/__init__.py`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/PKG-INFO` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-apigatewayv2-authorizers-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: Authorizers for AWS APIGateway V2
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.8.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/SOURCES.txt` & `aws-cdk.aws-apigatewayv2-authorizers-alpha-2.9.0a0/src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/SOURCES.txt
 src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/dependency_links.txt
 src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/requires.txt
 src/aws_cdk.aws_apigatewayv2_authorizers_alpha.egg-info/top_level.txt
 src/aws_cdk/aws_apigatewayv2_authorizers_alpha/__init__.py
 src/aws_cdk/aws_apigatewayv2_authorizers_alpha/py.typed
 src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/__init__.py
-src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/aws-apigatewayv2-authorizers-alpha@2.8.0-alpha.0.jsii.tgz
+src/aws_cdk/aws_apigatewayv2_authorizers_alpha/_jsii/aws-apigatewayv2-authorizers-alpha@2.9.0-alpha.0.jsii.tgz
```

