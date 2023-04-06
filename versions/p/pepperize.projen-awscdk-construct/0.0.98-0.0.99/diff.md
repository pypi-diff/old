# Comparing `tmp/pepperize.projen-awscdk-construct-0.0.98.tar.gz` & `tmp/pepperize.projen-awscdk-construct-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.projen-awscdk-construct-0.0.98.tar", last modified: Fri Apr 29 08:54:54 2022, max compression
+gzip compressed data, was "pepperize.projen-awscdk-construct-0.0.99.tar", last modified: Mon May  2 08:32:21 2022, max compression
```

## Comparing `pepperize.projen-awscdk-construct-0.0.98.tar` & `pepperize.projen-awscdk-construct-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2977 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1959 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1857 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2977 2022-04-29 08:54:54.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      594 2022-04-29 08:54:54.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-04-29 08:54:54.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       63 2022-04-29 08:54:54.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       34 2022-04-29 08:54:54.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/
--rw-r--r--   0 runner    (1001) docker     (121)    45936 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-29 08:54:54.565989 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7358 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/_jsii/projen-awscdk-construct@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-04-29 08:54:43.000000 pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2977 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1959 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1857 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2977 2022-05-02 08:32:21.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      594 2022-05-02 08:32:21.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-02 08:32:21.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       63 2022-05-02 08:32:21.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       34 2022-05-02 08:32:21.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/
+-rw-r--r--   0 runner    (1001) docker     (121)    45936 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-02 08:32:21.366580 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7357 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/_jsii/projen-awscdk-construct@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-02 08:32:08.000000 pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/py.typed
```

### Comparing `pepperize.projen-awscdk-construct-0.0.98/LICENSE` & `pepperize.projen-awscdk-construct-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.projen-awscdk-construct-0.0.98/PKG-INFO` & `pepperize.projen-awscdk-construct-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.projen-awscdk-construct
-Version: 0.0.98
+Version: 0.0.99
 Summary: This project provides a projen project type providing presets for an AWS CDK construct library project
 Home-page: https://github.com/pepperize/projen-awscdk-construct.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/projen-awscdk-construct.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.projen-awscdk-construct-0.0.98/README.md` & `pepperize.projen-awscdk-construct-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.projen-awscdk-construct-0.0.98/setup.py` & `pepperize.projen-awscdk-construct-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.projen-awscdk-construct",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "This project provides a projen project type providing presets for an AWS CDK construct library project",
     "license": "MIT",
     "url": "https://github.com/pepperize/projen-awscdk-construct.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_projen_awscdk_construct",
         "pepperize_projen_awscdk_construct._jsii"
     ],
     "package_data": {
         "pepperize_projen_awscdk_construct._jsii": [
-            "projen-awscdk-construct@0.0.98.jsii.tgz"
+            "projen-awscdk-construct@0.0.99.jsii.tgz"
         ],
         "pepperize_projen_awscdk_construct": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/PKG-INFO` & `pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.projen-awscdk-construct
-Version: 0.0.98
+Version: 0.0.99
 Summary: This project provides a projen project type providing presets for an AWS CDK construct library project
 Home-page: https://github.com/pepperize/projen-awscdk-construct.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/projen-awscdk-construct.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.projen-awscdk-construct-0.0.98/src/pepperize.projen_awscdk_construct.egg-info/SOURCES.txt` & `pepperize.projen-awscdk-construct-0.0.99/src/pepperize.projen_awscdk_construct.egg-info/SOURCES.txt`

 * *Files 17% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.projen_awscdk_construct.egg-info/SOURCES.txt
 src/pepperize.projen_awscdk_construct.egg-info/dependency_links.txt
 src/pepperize.projen_awscdk_construct.egg-info/requires.txt
 src/pepperize.projen_awscdk_construct.egg-info/top_level.txt
 src/pepperize_projen_awscdk_construct/__init__.py
 src/pepperize_projen_awscdk_construct/py.typed
 src/pepperize_projen_awscdk_construct/_jsii/__init__.py
-src/pepperize_projen_awscdk_construct/_jsii/projen-awscdk-construct@0.0.98.jsii.tgz
+src/pepperize_projen_awscdk_construct/_jsii/projen-awscdk-construct@0.0.99.jsii.tgz
```

### Comparing `pepperize.projen-awscdk-construct-0.0.98/src/pepperize_projen_awscdk_construct/__init__.py` & `pepperize.projen-awscdk-construct-0.0.99/src/pepperize_projen_awscdk_construct/__init__.py`

 * *Files identical despite different names*

