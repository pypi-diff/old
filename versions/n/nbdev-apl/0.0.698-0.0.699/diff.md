# Comparing `tmp/nbdev-apl-0.0.698.tar.gz` & `tmp/nbdev-apl-0.0.699.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-apl-0.0.698.tar", last modified: Fri Apr  7 01:42:03 2023, max compression
+gzip compressed data, was "nbdev-apl-0.0.699.tar", last modified: Fri Apr  7 13:18:05 2023, max compression
```

## Comparing `nbdev-apl-0.0.698.tar` & `nbdev-apl-0.0.699.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 01:42:03.052702 nbdev-apl-0.0.698/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 01:30:46.000000 nbdev-apl-0.0.698/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-04-07 01:30:46.000000 nbdev-apl-0.0.698/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      839 2023-04-07 01:42:03.048702 nbdev-apl-0.0.698/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-07 01:30:46.000000 nbdev-apl-0.0.698/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 01:42:03.048702 nbdev-apl-0.0.698/nbdev_apl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 01:42:02.000000 nbdev-apl-0.0.698/nbdev_apl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5828 2023-04-07 01:30:46.000000 nbdev-apl-0.0.698/nbdev_apl/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-07 01:42:02.000000 nbdev-apl-0.0.698/nbdev_apl/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 01:42:03.048702 nbdev-apl-0.0.698/nbdev_apl.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      839 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      346 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 01:42:03.000000 nbdev-apl-0.0.698/nbdev_apl.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-07 01:42:02.000000 nbdev-apl-0.0.698/settings.ini
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 01:42:03.052702 nbdev-apl-0.0.698/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-04-07 01:30:46.000000 nbdev-apl-0.0.698/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:18:05.606760 nbdev-apl-0.0.699/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 13:05:34.000000 nbdev-apl-0.0.699/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2023-04-07 13:05:34.000000 nbdev-apl-0.0.699/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      839 2023-04-07 13:18:05.606760 nbdev-apl-0.0.699/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-07 13:05:34.000000 nbdev-apl-0.0.699/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:18:05.606760 nbdev-apl-0.0.699/nbdev_apl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5828 2023-04-07 13:05:34.000000 nbdev-apl-0.0.699/nbdev_apl/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:18:05.606760 nbdev-apl-0.0.699/nbdev_apl.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      839 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/nbdev_apl.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-07 13:18:05.000000 nbdev-apl-0.0.699/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 13:18:05.606760 nbdev-apl-0.0.699/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2746 2023-04-07 13:05:34.000000 nbdev-apl-0.0.699/setup.py
```

### Comparing `nbdev-apl-0.0.698/LICENSE` & `nbdev-apl-0.0.699/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-apl-0.0.698/PKG-INFO` & `nbdev-apl-0.0.699/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-apl
-Version: 0.0.698
+Version: 0.0.699
 Summary: nbdev docs lookup for numpy
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `nbdev-apl-0.0.698/nbdev_apl/_modidx.py` & `nbdev-apl-0.0.699/nbdev_apl/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-apl-0.0.698/nbdev_apl.egg-info/PKG-INFO` & `nbdev-apl-0.0.699/nbdev_apl.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-apl
-Version: 0.0.698
+Version: 0.0.699
 Summary: nbdev docs lookup for numpy
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `nbdev-apl-0.0.698/settings.ini` & `nbdev-apl-0.0.699/settings.ini`

 * *Files 22% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for numpy
 keywords = nbdev fastai python
 author = Jeremy Howard
 author_email = info@fast.ai
 copyright = fast.ai, inc
 branch = master
-version = 0.0.698
+version = 0.0.699
 min_python = 3.6
 audience = Developers
 language = English
 license = apache2
 status = 2
 lib_path = nbdev_apl
 nbs_path = .
```

### Comparing `nbdev-apl-0.0.698/setup.py` & `nbdev-apl-0.0.699/setup.py`

 * *Files identical despite different names*

