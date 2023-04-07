# Comparing `tmp/pepperize.cdk-organizations-0.7.98.tar.gz` & `tmp/pepperize.cdk-organizations-0.7.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-organizations-0.7.98.tar", last modified: Tue Dec  6 00:38:04 2022, max compression
+gzip compressed data, was "pepperize.cdk-organizations-0.7.99.tar", last modified: Tue Dec  6 00:44:20 2022, max compression
```

## Comparing `pepperize.cdk-organizations-0.7.98.tar` & `pepperize.cdk-organizations-0.7.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    23152 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    22156 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1876 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:38:04.038388 pepperize.cdk-organizations-0.7.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    23152 2022-12-06 00:38:03.000000 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      534 2022-12-06 00:38:04.000000 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 00:38:03.000000 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-06 00:38:03.000000 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-06 00:38:03.000000 pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/
--rw-r--r--   0 runner    (1001) docker     (123)   125194 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:38:04.042388 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      427 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   138418 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/_jsii/cdk-organizations@0.7.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 00:37:44.000000 pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    23152 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    22156 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1876 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    23152 2022-12-06 00:44:20.000000 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2022-12-06 00:44:20.000000 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 00:44:20.000000 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-06 00:44:20.000000 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-06 00:44:20.000000 pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/
+-rw-r--r--   0 runner    (1001) docker     (123)   125194 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 00:44:20.931789 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   138305 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/_jsii/cdk-organizations@0.7.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 00:44:05.000000 pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/py.typed
```

### Comparing `pepperize.cdk-organizations-0.7.98/LICENSE` & `pepperize.cdk-organizations-0.7.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-organizations-0.7.98/PKG-INFO` & `pepperize.cdk-organizations-0.7.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-organizations
-Version: 0.7.98
+Version: 0.7.99
 Summary: Manage AWS organizations, organizational units (OU), accounts and service control policies (SCP).
 Home-page: https://github.com/pepperize/cdk-organizations.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-organizations.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-organizations-0.7.98/README.md` & `pepperize.cdk-organizations-0.7.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-organizations-0.7.98/setup.py` & `pepperize.cdk-organizations-0.7.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-organizations",
-    "version": "0.7.98",
+    "version": "0.7.99",
     "description": "Manage AWS organizations, organizational units (OU), accounts and service control policies (SCP).",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-organizations.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_organizations",
         "pepperize_cdk_organizations._jsii"
     ],
     "package_data": {
         "pepperize_cdk_organizations._jsii": [
-            "cdk-organizations@0.7.98.jsii.tgz"
+            "cdk-organizations@0.7.99.jsii.tgz"
         ],
         "pepperize_cdk_organizations": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/PKG-INFO` & `pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-organizations
-Version: 0.7.98
+Version: 0.7.99
 Summary: Manage AWS organizations, organizational units (OU), accounts and service control policies (SCP).
 Home-page: https://github.com/pepperize/cdk-organizations.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-organizations.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-organizations-0.7.98/src/pepperize.cdk_organizations.egg-info/SOURCES.txt` & `pepperize.cdk-organizations-0.7.99/src/pepperize.cdk_organizations.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_organizations.egg-info/SOURCES.txt
 src/pepperize.cdk_organizations.egg-info/dependency_links.txt
 src/pepperize.cdk_organizations.egg-info/requires.txt
 src/pepperize.cdk_organizations.egg-info/top_level.txt
 src/pepperize_cdk_organizations/__init__.py
 src/pepperize_cdk_organizations/py.typed
 src/pepperize_cdk_organizations/_jsii/__init__.py
-src/pepperize_cdk_organizations/_jsii/cdk-organizations@0.7.98.jsii.tgz
+src/pepperize_cdk_organizations/_jsii/cdk-organizations@0.7.99.jsii.tgz
```

### Comparing `pepperize.cdk-organizations-0.7.98/src/pepperize_cdk_organizations/__init__.py` & `pepperize.cdk-organizations-0.7.99/src/pepperize_cdk_organizations/__init__.py`

 * *Files identical despite different names*

