# Comparing `tmp/mlserver-xgboost-1.3.0rc1.tar.gz` & `tmp/mlserver-xgboost-1.3.0rc2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-xgboost-1.3.0rc1.tar", last modified: Thu Apr  6 13:37:46 2023, max compression
+gzip compressed data, was "mlserver-xgboost-1.3.0rc2.tar", last modified: Thu Apr  6 15:39:26 2023, max compression
```

## Comparing `mlserver-xgboost-1.3.0rc1.tar` & `mlserver-xgboost-1.3.0rc2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:46.129348 mlserver-xgboost-1.3.0rc1/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-04-06 13:37:46.129348 mlserver-xgboost-1.3.0rc1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      746 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:46.129348 mlserver-xgboost-1.3.0rc1/mlserver_xgboost/
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost/version.py
--rw-r--r--   0 runner    (1001) docker     (123)     3133 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost/xgboost.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:37:46.129348 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-04-06 13:37:46.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 13:37:46.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:37:46.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 13:37:46.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 13:37:46.000000 mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:37:46.129348 mlserver-xgboost-1.3.0rc1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 13:37:12.000000 mlserver-xgboost-1.3.0rc1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:26.985508 mlserver-xgboost-1.3.0rc2/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-04-06 15:39:26.985508 mlserver-xgboost-1.3.0rc2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      746 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:26.985508 mlserver-xgboost-1.3.0rc2/mlserver_xgboost/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3133 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost/xgboost.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:39:26.985508 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-04-06 15:39:26.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 15:39:26.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:39:26.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 15:39:26.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 15:39:26.000000 mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:39:26.985508 mlserver-xgboost-1.3.0rc2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 15:38:54.000000 mlserver-xgboost-1.3.0rc2/setup.py
```

### Comparing `mlserver-xgboost-1.3.0rc1/LICENSE` & `mlserver-xgboost-1.3.0rc2/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-xgboost-1.3.0rc1/PKG-INFO` & `mlserver-xgboost-1.3.0rc2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-xgboost
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: XGBoost runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # XGBoost runtime for MLServer
```

### Comparing `mlserver-xgboost-1.3.0rc1/README.md` & `mlserver-xgboost-1.3.0rc2/README.md`

 * *Files identical despite different names*

### Comparing `mlserver-xgboost-1.3.0rc1/mlserver_xgboost/xgboost.py` & `mlserver-xgboost-1.3.0rc2/mlserver_xgboost/xgboost.py`

 * *Files identical despite different names*

### Comparing `mlserver-xgboost-1.3.0rc1/mlserver_xgboost.egg-info/PKG-INFO` & `mlserver-xgboost-1.3.0rc2/mlserver_xgboost.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-xgboost
-Version: 1.3.0rc1
+Version: 1.3.0rc2
 Summary: XGBoost runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # XGBoost runtime for MLServer
```

### Comparing `mlserver-xgboost-1.3.0rc1/setup.py` & `mlserver-xgboost-1.3.0rc2/setup.py`

 * *Files identical despite different names*

