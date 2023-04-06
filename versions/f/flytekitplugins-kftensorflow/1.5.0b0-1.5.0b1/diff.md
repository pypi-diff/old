# Comparing `tmp/flytekitplugins-kftensorflow-1.5.0b0.tar.gz` & `tmp/flytekitplugins-kftensorflow-1.5.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flytekitplugins-kftensorflow-1.5.0b0.tar", last modified: Tue Mar 21 00:09:52 2023, max compression
+gzip compressed data, was "flytekitplugins-kftensorflow-1.5.0b1.tar", last modified: Wed Mar 29 18:58:40 2023, max compression
```

## Comparing `flytekitplugins-kftensorflow-1.5.0b0.tar` & `flytekitplugins-kftensorflow-1.5.0b1.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:52.472361 flytekitplugins-kftensorflow-1.5.0b0/
--rw-r--r--   0 runner    (1001) docker     (123)      804 2023-03-21 00:09:52.472361 flytekitplugins-kftensorflow-1.5.0b0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-21 00:09:29.000000 flytekitplugins-kftensorflow-1.5.0b0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:52.468361 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:52.472361 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-21 00:09:29.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-03-21 00:09:29.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-03-21 00:09:29.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-21 00:09:52.472361 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      804 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-21 00:09:52.000000 flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-21 00:09:52.472361 flytekitplugins-kftensorflow-1.5.0b0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-03-21 00:09:46.000000 flytekitplugins-kftensorflow-1.5.0b0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.796242 flytekitplugins-kftensorflow-1.5.0b1/
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-03-29 18:58:40.792242 flytekitplugins-kftensorflow-1.5.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-29 18:58:20.000000 flytekitplugins-kftensorflow-1.5.0b1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.792242 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.792242 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-03-29 18:58:20.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-03-29 18:58:20.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-03-29 18:58:20.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 18:58:40.792242 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-29 18:58:40.000000 flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 18:58:40.796242 flytekitplugins-kftensorflow-1.5.0b1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-03-29 18:58:35.000000 flytekitplugins-kftensorflow-1.5.0b1/setup.py
```

### Comparing `flytekitplugins-kftensorflow-1.5.0b0/PKG-INFO` & `flytekitplugins-kftensorflow-1.5.0b1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-kftensorflow
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: K8s based Tensorflow plugin for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/models.py` & `flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/models.py`

 * *Files identical despite different names*

### Comparing `flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins/kftensorflow/task.py` & `flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins/kftensorflow/task.py`

 * *Files identical despite different names*

### Comparing `flytekitplugins-kftensorflow-1.5.0b0/flytekitplugins_kftensorflow.egg-info/PKG-INFO` & `flytekitplugins-kftensorflow-1.5.0b1/flytekitplugins_kftensorflow.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flytekitplugins-kftensorflow
-Version: 1.5.0b0
+Version: 1.5.0b1
 Summary: K8s based Tensorflow plugin for flytekit
 Author: flyteorg
 Author-email: admin@flyte.org
 License: apache2
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `flytekitplugins-kftensorflow-1.5.0b0/setup.py` & `flytekitplugins-kftensorflow-1.5.0b1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 PLUGIN_NAME = "kftensorflow"
 
 microlib_name = f"flytekitplugins-{PLUGIN_NAME}"
 
 # TODO: Requirements are missing, add them back in later.
 plugin_requires = ["flytekit>=1.3.0b2,<2.0.0"]
 
-__version__ = "1.5.0b0"
+__version__ = "1.5.0b1"
 
 setup(
     name=microlib_name,
     version=__version__,
     author="flyteorg",
     author_email="admin@flyte.org",
     description="K8s based Tensorflow plugin for flytekit",
```

