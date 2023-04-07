# Comparing `tmp/cdk8s-valheim-0.0.8.tar.gz` & `tmp/cdk8s-valheim-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk8s-valheim-0.0.8.tar", last modified: Tue Mar 28 00:20:35 2023, max compression
+gzip compressed data, was "cdk8s-valheim-0.0.9.tar", last modified: Wed Mar 29 00:19:55 2023, max compression
```

## Comparing `cdk8s-valheim-0.0.8.tar` & `cdk8s-valheim-0.0.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:35.956005 cdk8s-valheim-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-28 00:20:35.956005 cdk8s-valheim-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-28 00:20:35.956005 cdk8s-valheim-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:35.952005 cdk8s-valheim-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:35.952005 cdk8s-valheim-0.0.8/src/cdk8s_valheim/
--rw-r--r--   0 runner    (1001) docker     (123)    74269 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:35.956005 cdk8s-valheim-0.0.8/src/cdk8s_valheim/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    34807 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim/_jsii/cdk8s-valheim@0.0.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 00:20:18.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 00:20:35.956005 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-28 00:20:35.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-28 00:20:35.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 00:20:35.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      128 2023-03-28 00:20:35.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-28 00:20:35.000000 cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:19:55.046563 cdk8s-valheim-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-29 00:19:55.046563 cdk8s-valheim-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 00:19:55.046563 cdk8s-valheim-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:19:55.042563 cdk8s-valheim-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:19:55.042563 cdk8s-valheim-0.0.9/src/cdk8s_valheim/
+-rw-r--r--   0 runner    (1001) docker     (123)    74269 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:19:55.046563 cdk8s-valheim-0.0.9/src/cdk8s_valheim/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34804 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim/_jsii/cdk8s-valheim@0.0.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 00:19:42.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 00:19:55.046563 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-29 00:19:55.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-29 00:19:55.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 00:19:55.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-03-29 00:19:55.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-29 00:19:55.000000 cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/top_level.txt
```

### Comparing `cdk8s-valheim-0.0.8/LICENSE` & `cdk8s-valheim-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk8s-valheim-0.0.8/PKG-INFO` & `cdk8s-valheim-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk8s-valheim
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package that vends a Valheim server chart.
 Home-page: https://github.com/awlsring/cdk8s-valheim.git
 Author: awlsring<mattcanemail@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/awlsring/cdk8s-valheim.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdk8s-valheim-0.0.8/README.md` & `cdk8s-valheim-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `cdk8s-valheim-0.0.8/setup.py` & `cdk8s-valheim-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk8s-valheim",
-    "version": "0.0.8",
+    "version": "0.0.9",
     "description": "A package that vends a Valheim server chart.",
     "license": "Apache-2.0",
     "url": "https://github.com/awlsring/cdk8s-valheim.git",
     "long_description_content_type": "text/markdown",
     "author": "awlsring<mattcanemail@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk8s_valheim",
         "cdk8s_valheim._jsii"
     ],
     "package_data": {
         "cdk8s_valheim._jsii": [
-            "cdk8s-valheim@0.0.8.jsii.tgz"
+            "cdk8s-valheim@0.0.9.jsii.tgz"
         ],
         "cdk8s_valheim": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk8s-valheim-0.0.8/src/cdk8s_valheim/__init__.py` & `cdk8s-valheim-0.0.9/src/cdk8s_valheim/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk8s-valheim-0.0.8/src/cdk8s_valheim.egg-info/PKG-INFO` & `cdk8s-valheim-0.0.9/src/cdk8s_valheim.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk8s-valheim
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package that vends a Valheim server chart.
 Home-page: https://github.com/awlsring/cdk8s-valheim.git
 Author: awlsring<mattcanemail@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/awlsring/cdk8s-valheim.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

