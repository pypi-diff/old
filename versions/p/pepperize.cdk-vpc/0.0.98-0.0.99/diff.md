# Comparing `tmp/pepperize.cdk-vpc-0.0.98.tar.gz` & `tmp/pepperize.cdk-vpc-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-vpc-0.0.98.tar", last modified: Mon May  2 16:11:07 2022, max compression
+gzip compressed data, was "pepperize.cdk-vpc-0.0.99.tar", last modified: Wed May  4 15:46:45 2022, max compression
```

## Comparing `pepperize.cdk-vpc-0.0.98.tar` & `pepperize.cdk-vpc-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     4291 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3358 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1733 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4291 2022-05-02 16:11:07.000000 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      434 2022-05-02 16:11:07.000000 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-02 16:11:07.000000 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-02 16:11:07.000000 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-05-02 16:11:07.000000 pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/
--rw-r--r--   0 runner    (1001) docker     (121)    16626 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 16:11:07.716087 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      360 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24732 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/_jsii/cdk-vpc@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-02 16:10:56.000000 pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     4291 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3358 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1733 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4291 2022-05-04 15:46:45.000000 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      434 2022-05-04 15:46:45.000000 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-04 15:46:45.000000 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-04 15:46:45.000000 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-05-04 15:46:45.000000 pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/
+-rw-r--r--   0 runner    (1001) docker     (121)    16626 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-04 15:46:45.833942 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      360 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24732 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/_jsii/cdk-vpc@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-04 15:46:31.000000 pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/py.typed
```

### Comparing `pepperize.cdk-vpc-0.0.98/LICENSE` & `pepperize.cdk-vpc-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-vpc-0.0.98/PKG-INFO` & `pepperize.cdk-vpc-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-vpc
-Version: 0.0.98
+Version: 0.0.99
 Summary: Utility constructs for tagging subnets or creating a cheaper vpc.
 Home-page: https://github.com/pepperize/cdk-vpc.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-vpc.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-vpc-0.0.98/README.md` & `pepperize.cdk-vpc-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-vpc-0.0.98/setup.py` & `pepperize.cdk-vpc-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-vpc",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Utility constructs for tagging subnets or creating a cheaper vpc.",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-vpc.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_vpc",
         "pepperize_cdk_vpc._jsii"
     ],
     "package_data": {
         "pepperize_cdk_vpc._jsii": [
-            "cdk-vpc@0.0.98.jsii.tgz"
+            "cdk-vpc@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_vpc": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `pepperize.cdk-vpc-0.0.98/src/pepperize.cdk_vpc.egg-info/PKG-INFO` & `pepperize.cdk-vpc-0.0.99/src/pepperize.cdk_vpc.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-vpc
-Version: 0.0.98
+Version: 0.0.99
 Summary: Utility constructs for tagging subnets or creating a cheaper vpc.
 Home-page: https://github.com/pepperize/cdk-vpc.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-vpc.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-vpc-0.0.98/src/pepperize_cdk_vpc/__init__.py` & `pepperize.cdk-vpc-0.0.99/src/pepperize_cdk_vpc/__init__.py`

 * *Files identical despite different names*

