# Comparing `tmp/pepperize.cdk-apigateway-swagger-ui-0.0.97.tar.gz` & `tmp/pepperize.cdk-apigateway-swagger-ui-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-apigateway-swagger-ui-0.0.97.tar", last modified: Tue Nov  8 07:05:55 2022, max compression
+gzip compressed data, was "pepperize.cdk-apigateway-swagger-ui-0.0.99.tar", last modified: Wed Nov  9 06:21:53 2022, max compression
```

## Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97.tar` & `pepperize.cdk-apigateway-swagger-ui-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-08 07:05:55.119082 pepperize.cdk-apigateway-swagger-ui-0.0.97/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3726 2022-11-08 07:05:55.119082 pepperize.cdk-apigateway-swagger-ui-0.0.97/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2759 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-08 07:05:55.119082 pepperize.cdk-apigateway-swagger-ui-0.0.97/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1886 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-08 07:05:55.115082 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-08 07:05:55.115082 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3726 2022-11-08 07:05:54.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      614 2022-11-08 07:05:55.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-08 07:05:54.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      110 2022-11-08 07:05:54.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       36 2022-11-08 07:05:55.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-08 07:05:55.115082 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/
--rw-r--r--   0 runner    (1001) docker     (121)     5424 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-08 07:05:55.115082 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      443 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  3630049 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/_jsii/cdk-apigateway-swagger-ui@0.0.97.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-08 07:05:39.000000 pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-09 06:21:53.958248 pepperize.cdk-apigateway-swagger-ui-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3726 2022-11-09 06:21:53.958248 pepperize.cdk-apigateway-swagger-ui-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2759 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-09 06:21:53.958248 pepperize.cdk-apigateway-swagger-ui-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1886 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-09 06:21:53.950248 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-09 06:21:53.954248 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3726 2022-11-09 06:21:53.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      614 2022-11-09 06:21:53.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-09 06:21:53.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      110 2022-11-09 06:21:53.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       36 2022-11-09 06:21:53.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-09 06:21:53.954248 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/
+-rw-r--r--   0 runner    (1001) docker     (121)     5424 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-09 06:21:53.954248 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      443 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  3630046 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/_jsii/cdk-apigateway-swagger-ui@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-09 06:21:35.000000 pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/py.typed
```

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/LICENSE` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/PKG-INFO` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-apigateway-swagger-ui
-Version: 0.0.97
+Version: 0.0.99
 Summary: Add SwaggerUI to your AWS Apigateway RestApi
 Home-page: https://github.com/pepperize/cdk-apigateway-swagger-ui.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-apigateway-swagger-ui.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/README.md` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/setup.py` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-apigateway-swagger-ui",
-    "version": "0.0.97",
+    "version": "0.0.99",
     "description": "Add SwaggerUI to your AWS Apigateway RestApi",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-apigateway-swagger-ui.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_apigateway_swagger_ui",
         "pepperize_cdk_apigateway_swagger_ui._jsii"
     ],
     "package_data": {
         "pepperize_cdk_apigateway_swagger_ui._jsii": [
-            "cdk-apigateway-swagger-ui@0.0.97.jsii.tgz"
+            "cdk-apigateway-swagger-ui@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_apigateway_swagger_ui": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/PKG-INFO` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-apigateway-swagger-ui
-Version: 0.0.97
+Version: 0.0.99
 Summary: Add SwaggerUI to your AWS Apigateway RestApi
 Home-page: https://github.com/pepperize/cdk-apigateway-swagger-ui.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-apigateway-swagger-ui.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize.cdk_apigateway_swagger_ui.egg-info/SOURCES.txt` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize.cdk_apigateway_swagger_ui.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_apigateway_swagger_ui.egg-info/SOURCES.txt
 src/pepperize.cdk_apigateway_swagger_ui.egg-info/dependency_links.txt
 src/pepperize.cdk_apigateway_swagger_ui.egg-info/requires.txt
 src/pepperize.cdk_apigateway_swagger_ui.egg-info/top_level.txt
 src/pepperize_cdk_apigateway_swagger_ui/__init__.py
 src/pepperize_cdk_apigateway_swagger_ui/py.typed
 src/pepperize_cdk_apigateway_swagger_ui/_jsii/__init__.py
-src/pepperize_cdk_apigateway_swagger_ui/_jsii/cdk-apigateway-swagger-ui@0.0.97.jsii.tgz
+src/pepperize_cdk_apigateway_swagger_ui/_jsii/cdk-apigateway-swagger-ui@0.0.99.jsii.tgz
```

### Comparing `pepperize.cdk-apigateway-swagger-ui-0.0.97/src/pepperize_cdk_apigateway_swagger_ui/__init__.py` & `pepperize.cdk-apigateway-swagger-ui-0.0.99/src/pepperize_cdk_apigateway_swagger_ui/__init__.py`

 * *Files identical despite different names*

