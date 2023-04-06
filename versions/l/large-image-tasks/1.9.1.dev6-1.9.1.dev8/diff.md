# Comparing `tmp/large-image-tasks-1.9.1.dev6.tar.gz` & `tmp/large-image-tasks-1.9.1.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/large-image-tasks-1.9.1.dev6.tar", last modified: Mon Dec 20 21:01:28 2021, max compression
+gzip compressed data, was "dist/large-image-tasks-1.9.1.dev8.tar", last modified: Tue Dec 21 17:37:31 2021, max compression
```

## Comparing `large-image-tasks-1.9.1.dev6.tar` & `large-image-tasks-1.9.1.dev8.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1367 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      521 2021-12-20 21:00:58.000000 large-image-tasks-1.9.1.dev6/README.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      637 2021-12-20 21:00:58.000000 large-image-tasks-1.9.1.dev6/large_image_tasks/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5974 2021-12-20 21:00:58.000000 large-image-tasks-1.9.1.dev6/large_image_tasks/tasks.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1367 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      332 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       79 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/entry_points.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      158 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       18 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-20 21:01:28.000000 large-image-tasks-1.9.1.dev6/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2377 2021-12-20 21:00:58.000000 large-image-tasks-1.9.1.dev6/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1367 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      521 2021-12-21 17:36:53.000000 large-image-tasks-1.9.1.dev8/README.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      637 2021-12-21 17:36:53.000000 large-image-tasks-1.9.1.dev8/large_image_tasks/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5974 2021-12-21 17:36:53.000000 large-image-tasks-1.9.1.dev8/large_image_tasks/tasks.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1367 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      332 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       79 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/entry_points.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      158 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       18 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-21 17:37:31.000000 large-image-tasks-1.9.1.dev8/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2377 2021-12-21 17:36:53.000000 large-image-tasks-1.9.1.dev8/setup.py
```

### Comparing `large-image-tasks-1.9.1.dev6/LICENSE` & `large-image-tasks-1.9.1.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `large-image-tasks-1.9.1.dev6/PKG-INFO` & `large-image-tasks-1.9.1.dev8/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image-tasks
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: Girder Worker tasks for Large Image.
 Home-page: UNKNOWN
 Author: Kitware Inc
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `large-image-tasks-1.9.1.dev6/README.rst` & `large-image-tasks-1.9.1.dev8/README.rst`

 * *Files identical despite different names*

### Comparing `large-image-tasks-1.9.1.dev6/large_image_tasks/__init__.py` & `large-image-tasks-1.9.1.dev8/large_image_tasks/__init__.py`

 * *Files identical despite different names*

### Comparing `large-image-tasks-1.9.1.dev6/large_image_tasks/tasks.py` & `large-image-tasks-1.9.1.dev8/large_image_tasks/tasks.py`

 * *Files identical despite different names*

### Comparing `large-image-tasks-1.9.1.dev6/large_image_tasks.egg-info/PKG-INFO` & `large-image-tasks-1.9.1.dev8/large_image_tasks.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image-tasks
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: Girder Worker tasks for Large Image.
 Home-page: UNKNOWN
 Author: Kitware Inc
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `large-image-tasks-1.9.1.dev6/setup.py` & `large-image-tasks-1.9.1.dev8/setup.py`

 * *Files identical despite different names*

