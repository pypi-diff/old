# Comparing `tmp/nbdev-pytorch-0.0.98.tar.gz` & `tmp/nbdev-pytorch-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-pytorch-0.0.98.tar", last modified: Wed Jun  8 13:37:54 2022, max compression
+gzip compressed data, was "nbdev-pytorch-0.0.99.tar", last modified: Thu Jun  9 01:53:57 2022, max compression
```

## Comparing `nbdev-pytorch-0.0.98.tar` & `nbdev-pytorch-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-08 13:37:54.479774 nbdev-pytorch-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-08 13:18:17.000000 nbdev-pytorch-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-08 13:18:17.000000 nbdev-pytorch-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      817 2022-06-08 13:37:54.479774 nbdev-pytorch-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-08 13:18:17.000000 nbdev-pytorch-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-08 13:37:54.479774 nbdev-pytorch-0.0.98/nbdev_pytorch/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   562738 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-08 13:37:54.479774 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      817 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      386 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       14 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      546 2022-06-08 13:37:54.000000 nbdev-pytorch-0.0.98/settings.ini
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-08 13:37:54.479774 nbdev-pytorch-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-08 13:18:17.000000 nbdev-pytorch-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 01:53:57.639916 nbdev-pytorch-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-09 01:35:55.000000 nbdev-pytorch-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-09 01:35:55.000000 nbdev-pytorch-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      817 2022-06-09 01:53:57.639916 nbdev-pytorch-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-09 01:35:55.000000 nbdev-pytorch-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 01:53:57.639916 nbdev-pytorch-0.0.99/nbdev_pytorch/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   562738 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 01:53:57.639916 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      817 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      386 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       49 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       14 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      546 2022-06-09 01:53:57.000000 nbdev-pytorch-0.0.99/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-09 01:53:57.639916 nbdev-pytorch-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-09 01:35:55.000000 nbdev-pytorch-0.0.99/setup.py
```

### Comparing `nbdev-pytorch-0.0.98/LICENSE` & `nbdev-pytorch-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-pytorch-0.0.98/PKG-INFO` & `nbdev-pytorch-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-pytorch
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for PyTorch
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python pytorch
 Platform: UNKNOWN
```

### Comparing `nbdev-pytorch-0.0.98/nbdev_pytorch/_modidx.py` & `nbdev-pytorch-0.0.99/nbdev_pytorch/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-pytorch-0.0.98/nbdev_pytorch.egg-info/PKG-INFO` & `nbdev-pytorch-0.0.99/nbdev_pytorch.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-pytorch
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for PyTorch
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python pytorch
 Platform: UNKNOWN
```

### Comparing `nbdev-pytorch-0.0.98/settings.ini` & `nbdev-pytorch-0.0.99/settings.ini`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for PyTorch
 keywords = nbdev fastai python pytorch
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
 lib_path = nbdev_pytorch
 nbs_path = .
```

### Comparing `nbdev-pytorch-0.0.98/setup.py` & `nbdev-pytorch-0.0.99/setup.py`

 * *Files identical despite different names*

