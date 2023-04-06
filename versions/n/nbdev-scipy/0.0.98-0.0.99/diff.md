# Comparing `tmp/nbdev-scipy-0.0.98.tar.gz` & `tmp/nbdev-scipy-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-scipy-0.0.98.tar", last modified: Sat Jun 11 13:34:19 2022, max compression
+gzip compressed data, was "nbdev-scipy-0.0.99.tar", last modified: Sun Jun 12 02:03:07 2022, max compression
```

## Comparing `nbdev-scipy-0.0.98.tar` & `nbdev-scipy-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-11 13:34:19.215900 nbdev-scipy-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-11 13:09:02.000000 nbdev-scipy-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-11 13:09:02.000000 nbdev-scipy-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      805 2022-06-11 13:34:19.215900 nbdev-scipy-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-11 13:09:02.000000 nbdev-scipy-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-11 13:34:19.215900 nbdev-scipy-0.0.98/nbdev_scipy/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   534264 2022-06-11 13:34:18.000000 nbdev-scipy-0.0.98/nbdev_scipy/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-11 13:34:19.215900 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      805 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      366 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       45 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-06-11 13:34:19.000000 nbdev-scipy-0.0.98/nbdev_scipy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      528 2022-06-11 13:34:18.000000 nbdev-scipy-0.0.98/settings.ini
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-11 13:34:19.215900 nbdev-scipy-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-11 13:09:02.000000 nbdev-scipy-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-12 02:03:07.762160 nbdev-scipy-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-12 01:36:44.000000 nbdev-scipy-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-12 01:36:44.000000 nbdev-scipy-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      805 2022-06-12 02:03:07.762160 nbdev-scipy-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-12 01:36:44.000000 nbdev-scipy-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-12 02:03:07.762160 nbdev-scipy-0.0.99/nbdev_scipy/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   534264 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-12 02:03:07.762160 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      805 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      366 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       45 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/nbdev_scipy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      528 2022-06-12 02:03:07.000000 nbdev-scipy-0.0.99/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-12 02:03:07.762160 nbdev-scipy-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-12 01:36:44.000000 nbdev-scipy-0.0.99/setup.py
```

### Comparing `nbdev-scipy-0.0.98/LICENSE` & `nbdev-scipy-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-scipy-0.0.98/PKG-INFO` & `nbdev-scipy-0.0.99/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-scipy
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for scipy
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-scipy-0.0.98/nbdev_scipy/_modidx.py` & `nbdev-scipy-0.0.99/nbdev_scipy/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-scipy-0.0.98/nbdev_scipy.egg-info/PKG-INFO` & `nbdev-scipy-0.0.99/nbdev_scipy.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-scipy
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for scipy
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-scipy-0.0.98/settings.ini` & `nbdev-scipy-0.0.99/settings.ini`

 * *Files 22% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for scipy
 keywords = nbdev fastai python
 author = Jeremy Howard
 author_email = info@fast.ai
 copyright = fast.ai, inc
 branch = master
-version = 0.0.98
+version = 0.0.99
 min_python = 3.6
 audience = Developers
 language = English
 license = apache2
 status = 2
 lib_path = nbdev_scipy
 nbs_path = .
```

### Comparing `nbdev-scipy-0.0.98/setup.py` & `nbdev-scipy-0.0.99/setup.py`

 * *Files identical despite different names*

