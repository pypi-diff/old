# Comparing `tmp/mlserver-sklearn-1.3.0rc1.tar.gz` & `tmp/mlserver-sklearn-1.3.0rc2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-sklearn-1.3.0rc1.tar", last modified: Thu Apr  6 13:37:29 2023, max compression
+gzip compressed data, was "mlserver-sklearn-1.3.0rc2.tar", last modified: Thu Apr  6 15:39:31 2023, max compression
```

## Comparing `mlserver-sklearn-1.3.0rc1.tar` & `mlserver-sklearn-1.3.0rc2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:29.765463 mlserver-sklearn-1.3.0rc1/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-06 13:37:29.765463 mlserver-sklearn-1.3.0rc1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:29.765463 mlserver-sklearn-1.3.0rc1/mlserver_sklearn/
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4491 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn/sklearn.py
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:29.765463 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-06 13:37:29.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 13:37:29.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:37:29.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 13:37:29.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 13:37:29.000000 mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:37:29.765463 mlserver-sklearn-1.3.0rc1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 13:36:53.000000 mlserver-sklearn-1.3.0rc1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:31.756244 mlserver-sklearn-1.3.0rc2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-06 15:39:31.756244 mlserver-sklearn-1.3.0rc2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:31.756244 mlserver-sklearn-1.3.0rc2/mlserver_sklearn/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4491 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn/sklearn.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:31.756244 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-06 15:39:31.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 15:39:31.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:39:31.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 15:39:31.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 15:39:31.000000 mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:39:31.756244 mlserver-sklearn-1.3.0rc2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 15:38:55.000000 mlserver-sklearn-1.3.0rc2/setup.py
```

### Comparing `mlserver-sklearn-1.3.0rc1/LICENSE` & `mlserver-sklearn-1.3.0rc2/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-sklearn-1.3.0rc1/PKG-INFO` & `mlserver-sklearn-1.3.0rc2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-sklearn
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: Scikit-Learn runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # Scikit-Learn runtime for MLServer
```

### Comparing `mlserver-sklearn-1.3.0rc1/README.md` & `mlserver-sklearn-1.3.0rc2/README.md`

 * *Files identical despite different names*

### Comparing `mlserver-sklearn-1.3.0rc1/mlserver_sklearn/sklearn.py` & `mlserver-sklearn-1.3.0rc2/mlserver_sklearn/sklearn.py`

 * *Files identical despite different names*

### Comparing `mlserver-sklearn-1.3.0rc1/mlserver_sklearn.egg-info/PKG-INFO` & `mlserver-sklearn-1.3.0rc2/mlserver_sklearn.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-sklearn
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: Scikit-Learn runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # Scikit-Learn runtime for MLServer
```

### Comparing `mlserver-sklearn-1.3.0rc1/setup.py` & `mlserver-sklearn-1.3.0rc2/setup.py`

 * *Files identical despite different names*

