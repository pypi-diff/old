# Comparing `tmp/cdk-events-notify-2.0.98.tar.gz` & `tmp/cdk-events-notify-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-events-notify-2.0.98.tar", last modified: Fri Mar 25 00:14:46 2022, max compression
+gzip compressed data, was "cdk-events-notify-2.0.99.tar", last modified: Sat Mar 26 00:15:28 2022, max compression
```

## Comparing `cdk-events-notify-2.0.98.tar` & `cdk-events-notify-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3972 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3054 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1729 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/src/cdk_events_notify/
--rw-r--r--   0 runner    (1001) docker     (121)     8070 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/src/cdk_events_notify/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/src/cdk_events_notify/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      369 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/src/cdk_events_notify/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    22426 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/src/cdk_events_notify/_jsii/cdk-events-notify@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-25 00:14:30.000000 cdk-events-notify-2.0.98/src/cdk_events_notify/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-25 00:14:46.416468 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3972 2022-03-25 00:14:46.000000 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      444 2022-03-25 00:14:46.000000 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-25 00:14:46.000000 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-25 00:14:46.000000 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-03-25 00:14:46.000000 cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3972 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3054 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1729 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/src/cdk_events_notify/
+-rw-r--r--   0 runner    (1001) docker     (121)     8070 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/src/cdk_events_notify/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/src/cdk_events_notify/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      369 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/src/cdk_events_notify/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22428 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/src/cdk_events_notify/_jsii/cdk-events-notify@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-26 00:15:17.000000 cdk-events-notify-2.0.99/src/cdk_events_notify/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-26 00:15:28.809611 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3972 2022-03-26 00:15:28.000000 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      444 2022-03-26 00:15:28.000000 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-26 00:15:28.000000 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-26 00:15:28.000000 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-03-26 00:15:28.000000 cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/top_level.txt
```

### Comparing `cdk-events-notify-2.0.98/LICENSE` & `cdk-events-notify-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-events-notify-2.0.98/PKG-INFO` & `cdk-events-notify-2.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-events-notify
-Version: 2.0.98
+Version: 2.0.99
 Summary: The Events Notify AWS Construct lib for AWS CDK
 Home-page: https://github.com/neilkuan/cdk-events-notify.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-events-notify.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-events-notify-2.0.98/README.md` & `cdk-events-notify-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-events-notify-2.0.98/setup.py` & `cdk-events-notify-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-events-notify",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "The Events Notify AWS Construct lib for AWS CDK",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdk-events-notify.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_events_notify",
         "cdk_events_notify._jsii"
     ],
     "package_data": {
         "cdk_events_notify._jsii": [
-            "cdk-events-notify@2.0.98.jsii.tgz"
+            "cdk-events-notify@2.0.99.jsii.tgz"
         ],
         "cdk_events_notify": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `cdk-events-notify-2.0.98/src/cdk_events_notify/__init__.py` & `cdk-events-notify-2.0.99/src/cdk_events_notify/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-events-notify-2.0.98/src/cdk_events_notify.egg-info/PKG-INFO` & `cdk-events-notify-2.0.99/src/cdk_events_notify.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-events-notify
-Version: 2.0.98
+Version: 2.0.99
 Summary: The Events Notify AWS Construct lib for AWS CDK
 Home-page: https://github.com/neilkuan/cdk-events-notify.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdk-events-notify.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

