# Comparing `tmp/pepperize.cdk-ssm-parameters-cross-region-0.0.98.tar.gz` & `tmp/pepperize.cdk-ssm-parameters-cross-region-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-ssm-parameters-cross-region-0.0.98.tar", last modified: Thu Oct 20 12:44:28 2022, max compression
+gzip compressed data, was "pepperize.cdk-ssm-parameters-cross-region-0.0.99.tar", last modified: Thu Oct 20 12:48:51 2022, max compression
```

## Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98.tar` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3381 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1944 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:44:28.914947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-10-20 12:44:28.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      674 2022-10-20 12:44:28.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-20 12:44:28.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      110 2022-10-20 12:44:28.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       42 2022-10-20 12:44:28.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/
--rw-r--r--   0 runner    (1001) docker     (121)    27936 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:44:28.918947 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      455 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    28364 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/cdk-ssm-parameters-cross-region@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-20 12:44:14.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3381 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1944 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4376 2022-10-20 12:48:50.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      674 2022-10-20 12:48:50.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-20 12:48:50.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      110 2022-10-20 12:48:50.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       42 2022-10-20 12:48:50.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/
+-rw-r--r--   0 runner    (1001) docker     (121)    27936 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-20 12:48:51.015817 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      455 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28365 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/_jsii/cdk-ssm-parameters-cross-region@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-20 12:48:36.000000 pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/py.typed
```

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/LICENSE` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/PKG-INFO` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-ssm-parameters-cross-region
-Version: 0.0.98
+Version: 0.0.99
 Summary: Store, read and lookup AWS SSM Parameters cross-region
 Home-page: https://github.com/pepperize/cdk-ssm-parameters-cross-region.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-ssm-parameters-cross-region.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/README.md` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/setup.py` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-ssm-parameters-cross-region",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Store, read and lookup AWS SSM Parameters cross-region",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-ssm-parameters-cross-region.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_ssm_parameters_cross_region",
         "pepperize_cdk_ssm_parameters_cross_region._jsii"
     ],
     "package_data": {
         "pepperize_cdk_ssm_parameters_cross_region._jsii": [
-            "cdk-ssm-parameters-cross-region@0.0.98.jsii.tgz"
+            "cdk-ssm-parameters-cross-region@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_ssm_parameters_cross_region": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/PKG-INFO` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-ssm-parameters-cross-region
-Version: 0.0.98
+Version: 0.0.99
 Summary: Store, read and lookup AWS SSM Parameters cross-region
 Home-page: https://github.com/pepperize/cdk-ssm-parameters-cross-region.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-ssm-parameters-cross-region.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/SOURCES.txt` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize.cdk_ssm_parameters_cross_region.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_ssm_parameters_cross_region.egg-info/SOURCES.txt
 src/pepperize.cdk_ssm_parameters_cross_region.egg-info/dependency_links.txt
 src/pepperize.cdk_ssm_parameters_cross_region.egg-info/requires.txt
 src/pepperize.cdk_ssm_parameters_cross_region.egg-info/top_level.txt
 src/pepperize_cdk_ssm_parameters_cross_region/__init__.py
 src/pepperize_cdk_ssm_parameters_cross_region/py.typed
 src/pepperize_cdk_ssm_parameters_cross_region/_jsii/__init__.py
-src/pepperize_cdk_ssm_parameters_cross_region/_jsii/cdk-ssm-parameters-cross-region@0.0.98.jsii.tgz
+src/pepperize_cdk_ssm_parameters_cross_region/_jsii/cdk-ssm-parameters-cross-region@0.0.99.jsii.tgz
```

### Comparing `pepperize.cdk-ssm-parameters-cross-region-0.0.98/src/pepperize_cdk_ssm_parameters_cross_region/__init__.py` & `pepperize.cdk-ssm-parameters-cross-region-0.0.99/src/pepperize_cdk_ssm_parameters_cross_region/__init__.py`

 * *Files identical despite different names*

