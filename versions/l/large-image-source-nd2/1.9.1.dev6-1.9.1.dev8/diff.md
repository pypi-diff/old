# Comparing `tmp/large-image-source-nd2-1.9.1.dev6.tar.gz` & `tmp/large-image-source-nd2-1.9.1.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/large-image-source-nd2-1.9.1.dev6.tar", last modified: Mon Dec 20 21:01:55 2021, max compression
+gzip compressed data, was "dist/large-image-source-nd2-1.9.1.dev8.tar", last modified: Tue Dec 21 17:38:02 2021, max compression
```

## Comparing `large-image-source-nd2-1.9.1.dev6.tar` & `large-image-source-nd2-1.9.1.dev8.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)      909 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/README.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13706 2021-12-20 21:00:58.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1298 2021-12-20 21:00:58.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2/girder_source.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      909 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      380 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      161 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/entry_points.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      102 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       23 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-20 21:01:55.000000 large-image-source-nd2-1.9.1.dev6/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2196 2021-12-20 21:00:58.000000 large-image-source-nd2-1.9.1.dev6/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-21 17:38:01.000000 large-image-source-nd2-1.9.1.dev8/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      909 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-21 17:38:01.000000 large-image-source-nd2-1.9.1.dev8/README.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13706 2021-12-21 17:36:53.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1298 2021-12-21 17:36:53.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2/girder_source.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      909 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      380 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      161 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/entry_points.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      102 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       23 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-21 17:38:02.000000 large-image-source-nd2-1.9.1.dev8/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2196 2021-12-21 17:36:53.000000 large-image-source-nd2-1.9.1.dev8/setup.py
```

### Comparing `large-image-source-nd2-1.9.1.dev6/LICENSE` & `large-image-source-nd2-1.9.1.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `large-image-source-nd2-1.9.1.dev6/PKG-INFO` & `large-image-source-nd2-1.9.1.dev8/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image-source-nd2
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: An nd2 (NIS Elements) tilesource for large_image.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: large_image,tile source
 Platform: UNKNOWN
```

### Comparing `large-image-source-nd2-1.9.1.dev6/README.rst` & `large-image-source-nd2-1.9.1.dev8/README.rst`

 * *Files identical despite different names*

### Comparing `large-image-source-nd2-1.9.1.dev6/large_image_source_nd2/__init__.py` & `large-image-source-nd2-1.9.1.dev8/large_image_source_nd2/__init__.py`

 * *Files identical despite different names*

### Comparing `large-image-source-nd2-1.9.1.dev6/large_image_source_nd2/girder_source.py` & `large-image-source-nd2-1.9.1.dev8/large_image_source_nd2/girder_source.py`

 * *Files identical despite different names*

### Comparing `large-image-source-nd2-1.9.1.dev6/large_image_source_nd2.egg-info/PKG-INFO` & `large-image-source-nd2-1.9.1.dev8/large_image_source_nd2.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image-source-nd2
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: An nd2 (NIS Elements) tilesource for large_image.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: large_image,tile source
 Platform: UNKNOWN
```

### Comparing `large-image-source-nd2-1.9.1.dev6/setup.py` & `large-image-source-nd2-1.9.1.dev8/setup.py`

 * *Files identical despite different names*

