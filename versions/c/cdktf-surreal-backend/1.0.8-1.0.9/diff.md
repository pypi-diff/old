# Comparing `tmp/cdktf-surreal-backend-1.0.8.tar.gz` & `tmp/cdktf-surreal-backend-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdktf-surreal-backend-1.0.8.tar", last modified: Mon Jan 30 01:07:30 2023, max compression
+gzip compressed data, was "cdktf-surreal-backend-1.0.9.tar", last modified: Tue Jan 31 01:14:28 2023, max compression
```

## Comparing `cdktf-surreal-backend-1.0.8.tar` & `cdktf-surreal-backend-1.0.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 01:07:30.438377 cdktf-surreal-backend-1.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-01-30 01:07:30.438377 cdktf-surreal-backend-1.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 01:07:30.438377 cdktf-surreal-backend-1.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1822 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 01:07:30.434377 cdktf-surreal-backend-1.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 01:07:30.434377 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/
--rw-r--r--   0 runner    (1001) docker     (123)     7404 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 01:07:30.434377 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      430 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11060 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/_jsii/cdktf-surreal-backend@1.0.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 01:07:16.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 01:07:30.438377 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-01-30 01:07:29.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-30 01:07:30.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 01:07:29.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-30 01:07:30.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-01-30 01:07:30.000000 cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1822 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/
+-rw-r--r--   0 runner    (1001) docker     (123)     7404 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      430 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11054 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/_jsii/cdktf-surreal-backend@1.0.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-31 01:14:09.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 01:14:28.484941 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2222 2023-01-31 01:14:27.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-01-31 01:14:28.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-31 01:14:27.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-31 01:14:28.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-01-31 01:14:28.000000 cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/top_level.txt
```

### Comparing `cdktf-surreal-backend-1.0.8/LICENSE` & `cdktf-surreal-backend-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdktf-surreal-backend-1.0.8/PKG-INFO` & `cdktf-surreal-backend-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-surreal-backend
-Version: 1.0.8
+Version: 1.0.9
 Summary: A package that vends a construct to setup the surreal backend in CDKTF
 Home-page: https://github.com/awlsring/cdktf-surreal-backend.git
 Author: awlsring<mattcanemail@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/awlsring/cdktf-surreal-backend.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdktf-surreal-backend-1.0.8/README.md` & `cdktf-surreal-backend-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `cdktf-surreal-backend-1.0.8/setup.py` & `cdktf-surreal-backend-1.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdktf-surreal-backend",
-    "version": "1.0.8",
+    "version": "1.0.9",
     "description": "A package that vends a construct to setup the surreal backend in CDKTF",
     "license": "Apache-2.0",
     "url": "https://github.com/awlsring/cdktf-surreal-backend.git",
     "long_description_content_type": "text/markdown",
     "author": "awlsring<mattcanemail@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdktf_surreal-backend",
         "cdktf_surreal-backend._jsii"
     ],
     "package_data": {
         "cdktf_surreal-backend._jsii": [
-            "cdktf-surreal-backend@1.0.8.jsii.tgz"
+            "cdktf-surreal-backend@1.0.9.jsii.tgz"
         ],
         "cdktf_surreal-backend": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdktf-surreal-backend-1.0.8/src/cdktf_surreal-backend/__init__.py` & `cdktf-surreal-backend-1.0.9/src/cdktf_surreal-backend/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-surreal-backend-1.0.8/src/cdktf_surreal_backend.egg-info/PKG-INFO` & `cdktf-surreal-backend-1.0.9/src/cdktf_surreal_backend.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-surreal-backend
-Version: 1.0.8
+Version: 1.0.9
 Summary: A package that vends a construct to setup the surreal backend in CDKTF
 Home-page: https://github.com/awlsring/cdktf-surreal-backend.git
 Author: awlsring<mattcanemail@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/awlsring/cdktf-surreal-backend.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

