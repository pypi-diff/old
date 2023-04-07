# Comparing `tmp/autogluon.eda-0.7.0b20230406.tar.gz` & `tmp/autogluon.eda-0.7.0b20230407.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "autogluon.eda-0.7.0b20230406.tar", last modified: Thu Apr  6 09:04:32 2023, max compression
+gzip compressed data, was "autogluon.eda-0.7.0b20230407.tar", last modified: Fri Apr  7 09:04:37 2023, max compression
```

## Comparing `autogluon.eda-0.7.0b20230406.tar` & `autogluon.eda-0.7.0b20230407.tar`

### file list

```diff
@@ -1,46 +1,46 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/
--rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-06 09:04:32.859128 autogluon.eda-0.7.0b20230406/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2328 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.851128 autogluon.eda-0.7.0b20230406/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/eda/
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/
--rw-r--r--   0 runner    (1001) docker     (123)      539 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11219 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    20850 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     5029 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/explain.py
--rw-r--r--   0 runner    (1001) docker     (123)    23617 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/interaction.py
--rw-r--r--   0 runner    (1001) docker     (123)     1462 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/missing.py
--rw-r--r--   0 runner    (1001) docker     (123)    10719 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/model.py
--rw-r--r--   0 runner    (1001) docker     (123)    12132 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/shift.py
--rw-r--r--   0 runner    (1001) docker     (123)     4564 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/transform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/eda/auto/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/auto/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    61305 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/auto/simple.py
--rw-r--r--   0 runner    (1001) docker     (123)     4052 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/state.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/eda/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/utils/defaults.py
--rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/
--rw-r--r--   0 runner    (1001) docker     (123)      827 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11954 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     4161 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/explain.py
--rw-r--r--   0 runner    (1001) docker     (123)    24169 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/interaction.py
--rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/jupyter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5130 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/layouts.py
--rw-r--r--   0 runner    (1001) docker     (123)     4857 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/missing.py
--rw-r--r--   0 runner    (1001) docker     (123)    11369 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-04-06 09:03:34.000000 autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/shift.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:32.855128 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:04:32.000000 autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.460568 autogluon.eda-0.7.0b20230407/
+-rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-04-07 09:04:37.460568 autogluon.eda-0.7.0b20230407/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1263 2023-04-07 09:04:37.460568 autogluon.eda-0.7.0b20230407/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2328 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon/eda/
+-rw-r--r--   0 runner    (1001) docker     (123)      125 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11219 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20850 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5029 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/explain.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23617 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/interaction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1462 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/missing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10719 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12132 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/shift.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4564 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/transform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon/eda/auto/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/auto/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61305 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/auto/simple.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4052 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/state.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon/eda/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      614 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/utils/defaults.py
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.460568 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/
+-rw-r--r--   0 runner    (1001) docker     (123)      827 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11954 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4161 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/explain.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24169 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/interaction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/jupyter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5130 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/layouts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4857 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/missing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11369 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-04-07 09:03:45.000000 autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/shift.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:04:37.456568 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:04:37.000000 autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/zip-safe
```

### Comparing `autogluon.eda-0.7.0b20230406/PKG-INFO` & `autogluon.eda-0.7.0b20230407/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: autogluon.eda
-Version: 0.7.0b20230406
+Version: 0.7.0b20230407
 Summary: AutoML for Image, Text, and Tabular Data
 Home-page: https://github.com/autogluon/autogluon
 Author: AutoGluon Community
 License: Apache-2.0
 Project-URL: Documentation, https://auto.gluon.ai
 Project-URL: Bug Reports, https://github.com/autogluon/autogluon/issues
 Project-URL: Source, https://github.com/autogluon/autogluon/
```

### Comparing `autogluon.eda-0.7.0b20230406/setup.cfg` & `autogluon.eda-0.7.0b20230407/setup.cfg`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/setup.py` & `autogluon.eda-0.7.0b20230407/setup.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/__init__.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/__init__.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/base.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/base.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/dataset.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/dataset.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/explain.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/explain.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/interaction.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/interaction.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/missing.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/missing.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/model.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/model.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/shift.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/shift.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/analysis/transform.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/analysis/transform.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/auto/simple.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/auto/simple.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/state.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/state.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/utils/defaults.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/utils/defaults.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/__init__.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/__init__.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/base.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/base.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/dataset.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/dataset.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/explain.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/explain.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/interaction.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/interaction.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/jupyter.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/jupyter.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/layouts.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/layouts.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/missing.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/missing.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/model.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/model.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon/eda/visualization/shift.py` & `autogluon.eda-0.7.0b20230407/src/autogluon/eda/visualization/shift.py`

 * *Files identical despite different names*

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/PKG-INFO` & `autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: autogluon.eda
-Version: 0.7.0b20230406
+Version: 0.7.0b20230407
 Summary: AutoML for Image, Text, and Tabular Data
 Home-page: https://github.com/autogluon/autogluon
 Author: AutoGluon Community
 License: Apache-2.0
 Project-URL: Documentation, https://auto.gluon.ai
 Project-URL: Bug Reports, https://github.com/autogluon/autogluon/issues
 Project-URL: Source, https://github.com/autogluon/autogluon/
```

### Comparing `autogluon.eda-0.7.0b20230406/src/autogluon.eda.egg-info/SOURCES.txt` & `autogluon.eda-0.7.0b20230407/src/autogluon.eda.egg-info/SOURCES.txt`

 * *Files identical despite different names*

