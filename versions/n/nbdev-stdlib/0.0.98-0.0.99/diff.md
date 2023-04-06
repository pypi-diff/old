# Comparing `tmp/nbdev-stdlib-0.0.98.tar.gz` & `tmp/nbdev-stdlib-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-stdlib-0.0.98.tar", last modified: Wed Jun  1 01:38:08 2022, max compression
+gzip compressed data, was "nbdev-stdlib-0.0.99.tar", last modified: Wed Jun  1 13:21:11 2022, max compression
```

## Comparing `nbdev-stdlib-0.0.98.tar` & `nbdev-stdlib-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 01:38:08.088410 nbdev-stdlib-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 01:37:00.000000 nbdev-stdlib-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-01 01:37:00.000000 nbdev-stdlib-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      828 2022-06-01 01:38:08.088410 nbdev-stdlib-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-01 01:37:00.000000 nbdev-stdlib-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 01:38:08.088410 nbdev-stdlib-0.0.98/nbdev_stdlib/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 01:38:07.000000 nbdev-stdlib-0.0.98/nbdev_stdlib/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   793442 2022-06-01 01:38:07.000000 nbdev-stdlib-0.0.98/nbdev_stdlib/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-01 01:38:07.000000 nbdev-stdlib-0.0.98/nbdev_stdlib/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 01:38:08.088410 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      828 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-01 01:38:08.000000 nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      554 2022-06-01 01:38:07.000000 nbdev-stdlib-0.0.98/settings.ini
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 01:38:08.088410 nbdev-stdlib-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-01 01:37:00.000000 nbdev-stdlib-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:21:11.789912 nbdev-stdlib-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 13:20:01.000000 nbdev-stdlib-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-01 13:20:01.000000 nbdev-stdlib-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      828 2022-06-01 13:21:11.789912 nbdev-stdlib-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-01 13:20:01.000000 nbdev-stdlib-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:21:11.789912 nbdev-stdlib-0.0.99/nbdev_stdlib/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   793442 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:21:11.789912 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      828 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      554 2022-06-01 13:21:11.000000 nbdev-stdlib-0.0.99/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 13:21:11.789912 nbdev-stdlib-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-01 13:20:01.000000 nbdev-stdlib-0.0.99/setup.py
```

### Comparing `nbdev-stdlib-0.0.98/LICENSE` & `nbdev-stdlib-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-stdlib-0.0.98/PKG-INFO` & `nbdev-stdlib-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-stdlib
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for the python standard library
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-stdlib-0.0.98/nbdev_stdlib/_modidx.py` & `nbdev-stdlib-0.0.99/nbdev_stdlib/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-stdlib-0.0.98/nbdev_stdlib.egg-info/PKG-INFO` & `nbdev-stdlib-0.0.99/nbdev_stdlib.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-stdlib
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for the python standard library
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-stdlib-0.0.98/settings.ini` & `nbdev-stdlib-0.0.99/settings.ini`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for the python standard library
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
 lib_path = nbdev_stdlib
 nbs_path = .
```

### Comparing `nbdev-stdlib-0.0.98/setup.py` & `nbdev-stdlib-0.0.99/setup.py`

 * *Files identical despite different names*

