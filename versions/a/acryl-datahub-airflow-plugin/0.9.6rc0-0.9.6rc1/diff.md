# Comparing `tmp/acryl-datahub-airflow-plugin-0.9.6rc0.tar.gz` & `tmp/acryl-datahub-airflow-plugin-0.9.6rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "acryl-datahub-airflow-plugin-0.9.6rc0.tar", last modified: Fri Jan 13 23:03:41 2023, max compression
+gzip compressed data, was "acryl-datahub-airflow-plugin-0.9.6rc1.tar", last modified: Fri Jan 13 23:14:19 2023, max compression
```

## Comparing `acryl-datahub-airflow-plugin-0.9.6rc0.tar` & `acryl-datahub-airflow-plugin-0.9.6rc1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:03:41.895008 acryl-datahub-airflow-plugin-0.9.6rc0/
--rw-r--r--   0 runner    (1001) docker     (123)     1472 2023-01-13 23:03:41.895008 acryl-datahub-airflow-plugin-0.9.6rc0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-13 22:58:48.000000 acryl-datahub-airflow-plugin-0.9.6rc0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-13 22:58:48.000000 acryl-datahub-airflow-plugin-0.9.6rc0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      910 2023-01-13 23:03:41.895008 acryl-datahub-airflow-plugin-0.9.6rc0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3634 2023-01-13 22:58:48.000000 acryl-datahub-airflow-plugin-0.9.6rc0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:03:41.891008 acryl-datahub-airflow-plugin-0.9.6rc0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:03:41.895008 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1472 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:00:15.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-13 23:03:41.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:03:41.895008 acryl-datahub-airflow-plugin-0.9.6rc0/src/datahub_airflow_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-13 23:03:35.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/datahub_airflow_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      259 2023-01-13 22:58:48.000000 acryl-datahub-airflow-plugin-0.9.6rc0/src/datahub_airflow_plugin/datahub_plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:14:19.961743 acryl-datahub-airflow-plugin-0.9.6rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1472 2023-01-13 23:14:19.961743 acryl-datahub-airflow-plugin-0.9.6rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-13 23:08:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-01-13 23:08:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      910 2023-01-13 23:14:19.965743 acryl-datahub-airflow-plugin-0.9.6rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3634 2023-01-13 23:08:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:14:19.961743 acryl-datahub-airflow-plugin-0.9.6rc1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:14:19.961743 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1472 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 23:10:01.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-01-13 23:14:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 23:14:19.961743 acryl-datahub-airflow-plugin-0.9.6rc1/src/datahub_airflow_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-01-13 23:14:11.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/datahub_airflow_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-01-13 23:08:19.000000 acryl-datahub-airflow-plugin-0.9.6rc1/src/datahub_airflow_plugin/datahub_plugin.py
```

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/PKG-INFO` & `acryl-datahub-airflow-plugin-0.9.6rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: acryl-datahub-airflow-plugin
-Version: 0.9.6rc0
+Version: 0.9.6rc1
 Summary: Datahub Airflow plugin to capture executions and send to Datahub
 Home-page: https://datahubproject.io/
 License: Apache License 2.0
 Project-URL: Documentation, https://datahubproject.io/docs/
 Project-URL: Source, https://github.com/datahub-project/datahub
 Project-URL: Changelog, https://github.com/datahub-project/datahub/releases
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/setup.cfg` & `acryl-datahub-airflow-plugin-0.9.6rc1/setup.cfg`

 * *Files identical despite different names*

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/setup.py` & `acryl-datahub-airflow-plugin-0.9.6rc1/setup.py`

 * *Files identical despite different names*

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/PKG-INFO` & `acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: acryl-datahub-airflow-plugin
-Version: 0.9.6rc0
+Version: 0.9.6rc1
 Summary: Datahub Airflow plugin to capture executions and send to Datahub
 Home-page: https://datahubproject.io/
 License: Apache License 2.0
 Project-URL: Documentation, https://datahubproject.io/docs/
 Project-URL: Source, https://github.com/datahub-project/datahub
 Project-URL: Changelog, https://github.com/datahub-project/datahub/releases
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/src/acryl_datahub_airflow_plugin.egg-info/SOURCES.txt` & `acryl-datahub-airflow-plugin-0.9.6rc1/src/acryl_datahub_airflow_plugin.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `acryl-datahub-airflow-plugin-0.9.6rc0/src/datahub_airflow_plugin/__init__.py` & `acryl-datahub-airflow-plugin-0.9.6rc1/src/datahub_airflow_plugin/__init__.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # Published at https://pypi.org/project/acryl-datahub/.
 __package_name__ = "acryl-datahub-airflow-plugin"
-__version__ = "0.9.6rc0"
+__version__ = "0.9.6rc1"
 
 
 def is_dev_mode() -> bool:
     return __version__.endswith("dev0")
 
 
 def nice_version_name() -> str:
```

