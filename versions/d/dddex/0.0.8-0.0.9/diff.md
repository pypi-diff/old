# Comparing `tmp/dddex-0.0.8.tar.gz` & `tmp/dddex-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dddex-0.0.8.tar", last modified: Mon Nov 21 00:01:48 2022, max compression
+gzip compressed data, was "dddex-0.0.9.tar", last modified: Mon Nov 21 00:03:30 2022, max compression
```

## Comparing `dddex-0.0.8.tar` & `dddex-0.0.9.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:01:48.465182 dddex-0.0.8/
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    11337 2022-10-13 15:08:23.000000 dddex-0.0.8/LICENSE
--rw-rw-r--   0 kagu      (1010) kagu      (1010)      111 2022-10-13 15:08:23.000000 dddex-0.0.8/MANIFEST.in
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    17908 2022-11-21 00:01:48.461182 dddex-0.0.8/PKG-INFO
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    17001 2022-11-20 23:43:25.000000 dddex-0.0.8/README.md
-drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:01:48.453182 dddex-0.0.8/dddex/
--rw-rw-r--   0 kagu      (1010) kagu      (1010)        0 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/__init__.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     9137 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/_modidx.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     6274 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/baseClasses.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     6940 2022-11-07 18:12:04.000000 dddex-0.0.8/dddex/basePredictor.py
-drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:01:48.461182 dddex-0.0.8/dddex/datasets/
--rw-rw-r--   0 kagu      (1010) kagu      (1010)   496591 2022-10-21 21:52:52.000000 dddex-0.0.8/dddex/datasets/dataYaz.csv
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    46547 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/levelSetKDEx.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     6275 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/loadData.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    10832 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/utils.py
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     6626 2022-11-20 23:53:10.000000 dddex-0.0.8/dddex/wSAA.py
-drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:01:48.461182 dddex-0.0.8/dddex.egg-info/
-drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:01:48.461182 dddex-0.0.8/dddex.egg-info/.ipynb_checkpoints/
--rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-11-09 20:42:32.000000 dddex-0.0.8/dddex.egg-info/.ipynb_checkpoints/dependency_links-checkpoint.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)      100 2022-11-09 20:42:33.000000 dddex-0.0.8/dddex.egg-info/.ipynb_checkpoints/requires-checkpoint.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)    17908 2022-11-21 00:01:47.000000 dddex-0.0.8/dddex.egg-info/PKG-INFO
--rw-rw-r--   0 kagu      (1010) kagu      (1010)      554 2022-11-21 00:01:48.000000 dddex-0.0.8/dddex.egg-info/SOURCES.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-11-21 00:01:47.000000 dddex-0.0.8/dddex.egg-info/dependency_links.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)       32 2022-11-21 00:01:47.000000 dddex-0.0.8/dddex.egg-info/entry_points.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-10-13 15:24:19.000000 dddex-0.0.8/dddex.egg-info/not-zip-safe
--rw-rw-r--   0 kagu      (1010) kagu      (1010)       95 2022-11-21 00:01:48.000000 dddex-0.0.8/dddex.egg-info/requires.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)        6 2022-11-21 00:01:48.000000 dddex-0.0.8/dddex.egg-info/top_level.txt
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     1115 2022-11-20 23:53:22.000000 dddex-0.0.8/settings.ini
--rw-rw-r--   0 kagu      (1010) kagu      (1010)       38 2022-11-21 00:01:48.465182 dddex-0.0.8/setup.cfg
--rw-rw-r--   0 kagu      (1010) kagu      (1010)     2584 2022-11-11 08:00:53.000000 dddex-0.0.8/setup.py
+drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:03:30.485337 dddex-0.0.9/
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    11337 2022-10-13 15:08:23.000000 dddex-0.0.9/LICENSE
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)      111 2022-10-13 15:08:23.000000 dddex-0.0.9/MANIFEST.in
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    17908 2022-11-21 00:03:30.485337 dddex-0.0.9/PKG-INFO
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    17001 2022-11-20 23:43:25.000000 dddex-0.0.9/README.md
+drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:03:30.481337 dddex-0.0.9/dddex/
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)        0 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/__init__.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     9137 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/_modidx.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     6274 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/baseClasses.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     6940 2022-11-07 18:12:04.000000 dddex-0.0.9/dddex/basePredictor.py
+drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:03:30.485337 dddex-0.0.9/dddex/datasets/
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)   496591 2022-10-21 21:52:52.000000 dddex-0.0.9/dddex/datasets/dataYaz.csv
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    46547 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/levelSetKDEx.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     6275 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/loadData.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    10832 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/utils.py
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     6626 2022-11-20 23:53:10.000000 dddex-0.0.9/dddex/wSAA.py
+drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:03:30.485337 dddex-0.0.9/dddex.egg-info/
+drwxrwxr-x   0 kagu      (1010) kagu      (1010)        0 2022-11-21 00:03:30.485337 dddex-0.0.9/dddex.egg-info/.ipynb_checkpoints/
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-11-09 20:42:32.000000 dddex-0.0.9/dddex.egg-info/.ipynb_checkpoints/dependency_links-checkpoint.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)      100 2022-11-09 20:42:33.000000 dddex-0.0.9/dddex.egg-info/.ipynb_checkpoints/requires-checkpoint.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)    17908 2022-11-21 00:03:29.000000 dddex-0.0.9/dddex.egg-info/PKG-INFO
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)      554 2022-11-21 00:03:30.000000 dddex-0.0.9/dddex.egg-info/SOURCES.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-11-21 00:03:29.000000 dddex-0.0.9/dddex.egg-info/dependency_links.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)       32 2022-11-21 00:03:30.000000 dddex-0.0.9/dddex.egg-info/entry_points.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)        1 2022-10-13 15:24:19.000000 dddex-0.0.9/dddex.egg-info/not-zip-safe
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)       95 2022-11-21 00:03:30.000000 dddex-0.0.9/dddex.egg-info/requires.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)        6 2022-11-21 00:03:30.000000 dddex-0.0.9/dddex.egg-info/top_level.txt
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     1115 2022-11-21 00:03:22.000000 dddex-0.0.9/settings.ini
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)       38 2022-11-21 00:03:30.485337 dddex-0.0.9/setup.cfg
+-rw-rw-r--   0 kagu      (1010) kagu      (1010)     2584 2022-11-11 08:00:53.000000 dddex-0.0.9/setup.py
```

### Comparing `dddex-0.0.8/LICENSE` & `dddex-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/PKG-INFO` & `dddex-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dddex
-Version: 0.0.8
+Version: 0.0.9
 Summary: The package 'data-driven density estimation x' (dddex) turns any standard point forecasting model into an estimator of the underlying conditional density
 Home-page: https://github.com/kaiguender/dddex
 Author: kaiguender
 Author-email: kai.guender@yahoo.de
 License: Apache Software License 2.0
 Keywords: nbdev jupyter notebook python
 Platform: UNKNOWN
```

### Comparing `dddex-0.0.8/README.md` & `dddex-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/_modidx.py` & `dddex-0.0.9/dddex/_modidx.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/baseClasses.py` & `dddex-0.0.9/dddex/baseClasses.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/basePredictor.py` & `dddex-0.0.9/dddex/basePredictor.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/datasets/dataYaz.csv` & `dddex-0.0.9/dddex/datasets/dataYaz.csv`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/levelSetKDEx.py` & `dddex-0.0.9/dddex/levelSetKDEx.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/loadData.py` & `dddex-0.0.9/dddex/loadData.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/utils.py` & `dddex-0.0.9/dddex/utils.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex/wSAA.py` & `dddex-0.0.9/dddex/wSAA.py`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/dddex.egg-info/PKG-INFO` & `dddex-0.0.9/dddex.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dddex
-Version: 0.0.8
+Version: 0.0.9
 Summary: The package 'data-driven density estimation x' (dddex) turns any standard point forecasting model into an estimator of the underlying conditional density
 Home-page: https://github.com/kaiguender/dddex
 Author: kaiguender
 Author-email: kai.guender@yahoo.de
 License: Apache Software License 2.0
 Keywords: nbdev jupyter notebook python
 Platform: UNKNOWN
```

### Comparing `dddex-0.0.8/dddex.egg-info/SOURCES.txt` & `dddex-0.0.9/dddex.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dddex-0.0.8/settings.ini` & `dddex-0.0.9/settings.ini`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 [DEFAULT]
 # All sections below are required unless otherwise specified.
 # See https://github.com/fastai/nbdev/blob/master/settings.ini for examples.
 
 ### Python library ###
 repo = dddex
 lib_name = %(repo)s
-version = 0.0.8
+version = 0.0.9
 min_python = 3.7
 license = apache2
 
 ### nbdev ###
 doc_path = _docs
 lib_path = dddex
 nbs_path = nbs
```

### Comparing `dddex-0.0.8/setup.py` & `dddex-0.0.9/setup.py`

 * *Files identical despite different names*

