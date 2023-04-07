# Comparing `tmp/botocore-a-la-carte-autoscaling-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-autoscaling-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-autoscaling-1.29.98.tar", last modified: Fri Mar 24 01:24:08 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-autoscaling-1.29.99.tar", last modified: Sat Mar 25 01:22:26 2023, max compression
```

## Comparing `botocore-a-la-carte-autoscaling-1.29.98.tar` & `botocore-a-la-carte-autoscaling-1.29.99.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      966 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/
--rw-r--r--   0 runner    (1001) docker     (123)    19615 2023-03-24 01:23:57.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    48065 2023-03-24 01:23:57.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1866 2023-03-24 01:23:57.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   356304 2023-03-24 01:23:57.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/service-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      966 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:08.261838 botocore-a-la-carte-autoscaling-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-03-24 01:24:08.000000 botocore-a-la-carte-autoscaling-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      966 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    19615 2023-03-25 01:22:12.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    48065 2023-03-25 01:22:12.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1866 2023-03-25 01:22:12.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   356304 2023-03-25 01:22:12.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/service-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      966 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:22:26.806567 botocore-a-la-carte-autoscaling-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-03-25 01:22:26.000000 botocore-a-la-carte-autoscaling-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/LICENSE.txt` & `botocore-a-la-carte-autoscaling-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/PKG-INFO` & `botocore-a-la-carte-autoscaling-1.29.99/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-autoscaling
-Version: 1.29.98
+Version: 1.29.99
 Summary: autoscaling data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/examples-1.json` & `botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/examples-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/paginators-1.json` & `botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/botocore/data/autoscaling/2011-01-01/service-2.json` & `botocore-a-la-carte-autoscaling-1.29.99/botocore/data/autoscaling/2011-01-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/botocore_a_la_carte_autoscaling.egg-info/PKG-INFO` & `botocore-a-la-carte-autoscaling-1.29.99/botocore_a_la_carte_autoscaling.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-autoscaling
-Version: 1.29.98
+Version: 1.29.99
 Summary: autoscaling data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-autoscaling-1.29.98/setup.py` & `botocore-a-la-carte-autoscaling-1.29.99/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-autoscaling',
-    version="1.29.98",
+    version="1.29.99",
     description='autoscaling data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/autoscaling/*/*.json'],
```

