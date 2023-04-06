# Comparing `tmp/flytekitplugins-hive-1.5.0b0.tar.gz` & `tmp/flytekitplugins-hive-1.5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flytekitplugins-hive-1.5.0b0.tar", last modified: Tue Mar 21 00:09:50 2023, max compression
+gzip compressed data, was "flytekitplugins-hive-1.5.0b1.tar", last modified: Wed Mar 29 18:58:39 2023, max compression
```

## Comparing `flytekitplugins-hive-1.5.0b0.tar` & `flytekitplugins-hive-1.5.0b1.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      497 2023-03-21 00:09:29.000000 flytekitplugins-hive-1.5.0b0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/flytekitplugins/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/flytekitplugins/hive/
--rw-r--r--   0 runner    (1001) docker     (123)      287 2023-03-21 00:09:29.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins/hive/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5010 2023-03-21 00:09:29.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins/hive/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:50.000000 flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-21 00:09:50.540350 flytekitplugins-hive-1.5.0b0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-21 00:09:46.000000 flytekitplugins-hive-1.5.0b0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:39.096245 flytekitplugins-hive-1.5.0b1/
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-29 18:58:39.092245 flytekitplugins-hive-1.5.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      497 2023-03-29 18:58:20.000000 flytekitplugins-hive-1.5.0b1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:39.092245 flytekitplugins-hive-1.5.0b1/flytekitplugins/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:39.092245 flytekitplugins-hive-1.5.0b1/flytekitplugins/hive/
+-rw-r--r--   0 runner    (1001) docker     (123)      287 2023-03-29 18:58:20.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins/hive/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5010 2023-03-29 18:58:20.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins/hive/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:39.092245 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:39.000000 flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 18:58:39.096245 flytekitplugins-hive-1.5.0b1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-03-29 18:58:34.000000 flytekitplugins-hive-1.5.0b1/setup.py
```

### Comparing `flytekitplugins-hive-1.5.0b0/PKG-INFO` & `flytekitplugins-hive-1.5.0b1/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-hive
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: This package holds Hive plugins for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-hive-1.5.0b0/flytekitplugins/hive/task.py` & `flytekitplugins-hive-1.5.0b1/flytekitplugins/hive/task.py`

 * *Files identical despite different names*

### Comparing `flytekitplugins-hive-1.5.0b0/flytekitplugins_hive.egg-info/PKG-INFO` & `flytekitplugins-hive-1.5.0b1/flytekitplugins_hive.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-hive
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: This package holds Hive plugins for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-hive-1.5.0b0/setup.py` & `flytekitplugins-hive-1.5.0b1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 PLUGIN_NAME = "hive"
 
 microlib_name = f"flytekitplugins-{PLUGIN_NAME}"
 
 plugin_requires = ["flytekit>=1.3.0b2,<2.0.0"]
 
-__version__ = "1.5.0b0"
+__version__ = "1.5.0b1"
 
 setup(
     name=microlib_name,
     version=__version__,
     author="flyteorg",
     author_email="admin@flyte.org",
     description="This package holds Hive plugins for flytekit",
```

