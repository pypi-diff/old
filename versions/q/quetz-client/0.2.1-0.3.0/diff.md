# Comparing `tmp/quetz_client-0.2.1.tar.gz` & `tmp/quetz_client-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quetz_client-0.2.1.tar", last modified: Tue Mar  7 14:54:20 2023, max compression
+gzip compressed data, was "quetz_client-0.3.0.tar", last modified: Thu Apr  6 17:03:19 2023, max compression
```

## Comparing `quetz_client-0.2.1.tar` & `quetz_client-0.3.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 14:54:20.744400 quetz_client-0.2.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-03-07 14:53:39.000000 quetz_client-0.2.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-03-07 14:54:20.748400 quetz_client-0.2.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-03-07 14:53:39.000000 quetz_client-0.2.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-03-07 14:53:51.000000 quetz_client-0.2.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      803 2023-03-07 14:54:20.748400 quetz_client-0.2.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 14:54:20.744400 quetz_client-0.2.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 14:54:20.744400 quetz_client-0.2.1/src/quetz_client/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-07 14:53:39.000000 quetz_client-0.2.1/src/quetz_client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-07 14:53:51.000000 quetz_client-0.2.1/src/quetz_client/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      711 2023-03-07 14:53:39.000000 quetz_client-0.2.1/src/quetz_client/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     5548 2023-03-07 14:53:39.000000 quetz_client-0.2.1/src/quetz_client/client.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 14:54:20.744400 quetz_client-0.2.1/src/quetz_client.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      450 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-03-07 14:54:20.000000 quetz_client-0.2.1/src/quetz_client.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 14:54:20.744400 quetz_client-0.2.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-07 14:53:39.000000 quetz_client-0.2.1/tests/test_both.py
--rw-r--r--   0 runner    (1001) docker     (123)     2182 2023-03-07 14:53:39.000000 quetz_client-0.2.1/tests/test_live.py
--rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-03-07 14:53:39.000000 quetz_client-0.2.1/tests/test_mock.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:03:19.191775 quetz_client-0.3.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-06 17:02:31.000000 quetz_client-0.3.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-04-06 17:03:19.191775 quetz_client-0.3.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-04-06 17:02:31.000000 quetz_client-0.3.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-04-06 17:02:45.000000 quetz_client-0.3.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      803 2023-04-06 17:03:19.191775 quetz_client-0.3.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:03:19.187774 quetz_client-0.3.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:03:19.191775 quetz_client-0.3.0/src/quetz_client/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 17:02:31.000000 quetz_client-0.3.0/src/quetz_client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-06 17:02:45.000000 quetz_client-0.3.0/src/quetz_client/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      922 2023-04-06 17:02:31.000000 quetz_client-0.3.0/src/quetz_client/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5548 2023-04-06 17:02:31.000000 quetz_client-0.3.0/src/quetz_client/client.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:03:19.191775 quetz_client-0.3.0/src/quetz_client.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 17:03:19.000000 quetz_client-0.3.0/src/quetz_client.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:03:19.191775 quetz_client-0.3.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-04-06 17:02:31.000000 quetz_client-0.3.0/tests/test_both.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2182 2023-04-06 17:02:31.000000 quetz_client-0.3.0/tests/test_live.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-04-06 17:02:31.000000 quetz_client-0.3.0/tests/test_mock.py
```

### Comparing `quetz_client-0.2.1/LICENSE` & `quetz_client-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/PKG-INFO` & `quetz_client-0.3.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quetz_client
-Version: 0.2.1
+Version: 0.3.0
 Summary: A Python client to interact with a Quetz server.
 Home-page: https://github.com/mamba-org/quetz-client
 Author: QuantCo, Inc.
 Author-email: noreply@quantco.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `quetz_client-0.2.1/README.md` & `quetz_client-0.3.0/README.md`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/pyproject.toml` & `quetz_client-0.3.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -29,15 +29,15 @@
 check_untyped_defs = true
 
 [tool.pytest.ini_options]
 # This will be pytest's future default.
 addopts = "--import-mode=importlib"
 
 [tool.tbump.version]
-current = "0.2.1"
+current = "0.3.0"
 regex = '''
   (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)
   ((?P<channel>a|b|rc|.dev)(?P<release>\d+))?
 '''
 
 [[tool.tbump.field]]
 name = "channel"
```

### Comparing `quetz_client-0.2.1/setup.cfg` & `quetz_client-0.3.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/src/quetz_client/client.py` & `quetz_client-0.3.0/src/quetz_client/client.py`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/src/quetz_client.egg-info/PKG-INFO` & `quetz_client-0.3.0/src/quetz_client.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quetz-client
-Version: 0.2.1
+Version: 0.3.0
 Summary: A Python client to interact with a Quetz server.
 Home-page: https://github.com/mamba-org/quetz-client
 Author: QuantCo, Inc.
 Author-email: noreply@quantco.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `quetz_client-0.2.1/tests/test_both.py` & `quetz_client-0.3.0/tests/test_both.py`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/tests/test_live.py` & `quetz_client-0.3.0/tests/test_live.py`

 * *Files identical despite different names*

### Comparing `quetz_client-0.2.1/tests/test_mock.py` & `quetz_client-0.3.0/tests/test_mock.py`

 * *Files identical despite different names*

