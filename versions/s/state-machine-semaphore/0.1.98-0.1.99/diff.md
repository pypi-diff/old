# Comparing `tmp/state-machine-semaphore-0.1.98.tar.gz` & `tmp/state-machine-semaphore-0.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "state-machine-semaphore-0.1.98.tar", last modified: Thu Nov 17 00:41:47 2022, max compression
+gzip compressed data, was "state-machine-semaphore-0.1.99.tar", last modified: Fri Nov 18 00:48:17 2022, max compression
```

## Comparing `state-machine-semaphore-0.1.98.tar` & `state-machine-semaphore-0.1.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     6151 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     5120 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1901 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/src/state_machine_semaphore/
--rw-r--r--   0 runner    (1001) docker     (121)    18392 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/src/state_machine_semaphore/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      438 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   314231 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore/_jsii/state-machine-semaphore@0.1.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-17 00:41:34.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-17 00:41:47.721512 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     6151 2022-11-17 00:41:47.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      504 2022-11-17 00:41:47.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-17 00:41:47.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-17 00:41:47.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       24 2022-11-17 00:41:47.000000 state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     6151 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     5120 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      236 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1901 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/src/state_machine_semaphore/
+-rw-r--r--   0 runner    (1001) docker     (121)    18392 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/src/state_machine_semaphore/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      438 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   314234 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore/_jsii/state-machine-semaphore@0.1.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-18 00:48:00.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-18 00:48:17.549170 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     6151 2022-11-18 00:48:17.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      504 2022-11-18 00:48:17.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-18 00:48:17.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-11-18 00:48:17.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       24 2022-11-18 00:48:17.000000 state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/top_level.txt
```

### Comparing `state-machine-semaphore-0.1.98/LICENSE` & `state-machine-semaphore-0.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `state-machine-semaphore-0.1.98/PKG-INFO` & `state-machine-semaphore-0.1.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: state-machine-semaphore
-Version: 0.1.98
+Version: 0.1.99
 Summary: Create distributed semaphores using AWS Step Functions and Amazon DynamoDB to control concurrent invocations of contentious work.
 Home-page: https://github.com/dontirun/state-machine-semaphore.git
 Author: Arun Donti<dontirun@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/dontirun/state-machine-semaphore.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `state-machine-semaphore-0.1.98/README.md` & `state-machine-semaphore-0.1.99/README.md`

 * *Files identical despite different names*

### Comparing `state-machine-semaphore-0.1.98/setup.py` & `state-machine-semaphore-0.1.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "state-machine-semaphore",
-    "version": "0.1.98",
+    "version": "0.1.99",
     "description": "Create distributed semaphores using AWS Step Functions and Amazon DynamoDB to control concurrent invocations of contentious work.",
     "license": "Apache-2.0",
     "url": "https://github.com/dontirun/state-machine-semaphore.git",
     "long_description_content_type": "text/markdown",
     "author": "Arun Donti<dontirun@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "state_machine_semaphore",
         "state_machine_semaphore._jsii"
     ],
     "package_data": {
         "state_machine_semaphore._jsii": [
-            "state-machine-semaphore@0.1.98.jsii.tgz"
+            "state-machine-semaphore@0.1.99.jsii.tgz"
         ],
         "state_machine_semaphore": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `state-machine-semaphore-0.1.98/src/state_machine_semaphore/__init__.py` & `state-machine-semaphore-0.1.99/src/state_machine_semaphore/__init__.py`

 * *Files identical despite different names*

### Comparing `state-machine-semaphore-0.1.98/src/state_machine_semaphore.egg-info/PKG-INFO` & `state-machine-semaphore-0.1.99/src/state_machine_semaphore.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: state-machine-semaphore
-Version: 0.1.98
+Version: 0.1.99
 Summary: Create distributed semaphores using AWS Step Functions and Amazon DynamoDB to control concurrent invocations of contentious work.
 Home-page: https://github.com/dontirun/state-machine-semaphore.git
 Author: Arun Donti<dontirun@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/dontirun/state-machine-semaphore.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

