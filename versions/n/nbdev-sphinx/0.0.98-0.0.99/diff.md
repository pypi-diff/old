# Comparing `tmp/nbdev-sphinx-0.0.98.tar.gz` & `tmp/nbdev-sphinx-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-sphinx-0.0.98.tar", last modified: Wed Jun  1 13:50:19 2022, max compression
+gzip compressed data, was "nbdev-sphinx-0.0.99.tar", last modified: Thu Jun  2 02:07:19 2022, max compression
```

## Comparing `nbdev-sphinx-0.0.98.tar` & `nbdev-sphinx-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:50:19.959689 nbdev-sphinx-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 13:20:01.000000 nbdev-sphinx-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-01 13:20:01.000000 nbdev-sphinx-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 13:50:19.959689 nbdev-sphinx-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-01 13:20:01.000000 nbdev-sphinx-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:50:19.955689 nbdev-sphinx-0.0.98/nbdev_sphinx/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    48640 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:50:19.959689 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      533 2022-06-01 13:50:19.000000 nbdev-sphinx-0.0.98/settings.ini
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 13:50:19.959689 nbdev-sphinx-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-01 13:20:01.000000 nbdev-sphinx-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:07:19.043294 nbdev-sphinx-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-02 01:35:07.000000 nbdev-sphinx-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-02 01:35:07.000000 nbdev-sphinx-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-02 02:07:19.043294 nbdev-sphinx-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-02 01:35:07.000000 nbdev-sphinx-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:07:19.043294 nbdev-sphinx-0.0.99/nbdev_sphinx/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-02 02:07:18.000000 nbdev-sphinx-0.0.99/nbdev_sphinx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    48640 2022-06-02 02:07:18.000000 nbdev-sphinx-0.0.99/nbdev_sphinx/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-02 02:07:18.000000 nbdev-sphinx-0.0.99/nbdev_sphinx/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-02 02:07:19.043294 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-02 02:07:19.000000 nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      533 2022-06-02 02:07:18.000000 nbdev-sphinx-0.0.99/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-02 02:07:19.043294 nbdev-sphinx-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-02 01:35:07.000000 nbdev-sphinx-0.0.99/setup.py
```

### Comparing `nbdev-sphinx-0.0.98/LICENSE` & `nbdev-sphinx-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-sphinx-0.0.98/PKG-INFO` & `nbdev-sphinx-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-sphinx
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for sphinx
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-sphinx-0.0.98/nbdev_sphinx/_modidx.py` & `nbdev-sphinx-0.0.99/nbdev_sphinx/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-sphinx-0.0.98/nbdev_sphinx.egg-info/PKG-INFO` & `nbdev-sphinx-0.0.99/nbdev_sphinx.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-sphinx
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for sphinx
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-sphinx-0.0.98/settings.ini` & `nbdev-sphinx-0.0.99/settings.ini`

 * *Files 24% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for sphinx
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
 lib_path = nbdev_sphinx
 nbs_path = .
```

### Comparing `nbdev-sphinx-0.0.98/setup.py` & `nbdev-sphinx-0.0.99/setup.py`

 * *Files identical despite different names*

