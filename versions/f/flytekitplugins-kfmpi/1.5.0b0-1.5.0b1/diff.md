# Comparing `tmp/flytekitplugins-kfmpi-1.5.0b0.tar.gz` & `tmp/flytekitplugins-kfmpi-1.5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flytekitplugins-kfmpi-1.5.0b0.tar", last modified: Tue Mar 21 00:09:51 2023, max compression
+gzip compressed data, was "flytekitplugins-kfmpi-1.5.0b1.tar", last modified: Wed Mar 29 18:58:40 2023, max compression
```

## Comparing `flytekitplugins-kfmpi-1.5.0b0.tar` & `flytekitplugins-kfmpi-1.5.0b1.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/
--rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-21 00:09:29.000000 flytekitplugins-kfmpi-1.5.0b0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins/kfmpi/
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-03-21 00:09:29.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins/kfmpi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4294 2023-03-21 00:09:29.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins/kfmpi/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)       42 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:51.000000 flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-21 00:09:51.704357 flytekitplugins-kfmpi-1.5.0b0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1205 2023-03-21 00:09:46.000000 flytekitplugins-kfmpi-1.5.0b0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/
+-rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-29 18:58:20.000000 flytekitplugins-kfmpi-1.5.0b1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins/kfmpi/
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-03-29 18:58:20.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins/kfmpi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4294 2023-03-29 18:58:20.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins/kfmpi/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:40.000000 flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 18:58:40.116243 flytekitplugins-kfmpi-1.5.0b1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1205 2023-03-29 18:58:35.000000 flytekitplugins-kfmpi-1.5.0b1/setup.py
```

### Comparing `flytekitplugins-kfmpi-1.5.0b0/PKG-INFO` & `flytekitplugins-kfmpi-1.5.0b1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-kfmpi
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: K8s based MPI plugin for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-kfmpi-1.5.0b0/flytekitplugins/kfmpi/task.py` & `flytekitplugins-kfmpi-1.5.0b1/flytekitplugins/kfmpi/task.py`

 * *Files identical despite different names*

### Comparing `flytekitplugins-kfmpi-1.5.0b0/flytekitplugins_kfmpi.egg-info/PKG-INFO` & `flytekitplugins-kfmpi-1.5.0b1/flytekitplugins_kfmpi.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-kfmpi
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: K8s based MPI plugin for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-kfmpi-1.5.0b0/setup.py` & `flytekitplugins-kfmpi-1.5.0b1/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 PLUGIN_NAME = "kfmpi"
 
 microlib_name = f"flytekitplugins-{PLUGIN_NAME}"
 
 plugin_requires = ["flytekit>=1.3.0b2,<2.0.0", "flyteidl>=0.21.4"]
 
-__version__ = "1.5.0b0"
+__version__ = "1.5.0b1"
 
 setup(
     name=microlib_name,
     version=__version__,
     author="flyteorg",
     author_email="admin@flyte.org",
     description="K8s based MPI plugin for flytekit",
```

