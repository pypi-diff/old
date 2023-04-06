# Comparing `tmp/large-image-1.9.1.dev6.tar.gz` & `tmp/large-image-1.9.1.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/large-image-1.9.1.dev6.tar", last modified: Mon Dec 20 21:01:06 2021, max compression
+gzip compressed data, was "dist/large-image-1.9.1.dev8.tar", last modified: Tue Dec 21 17:37:06 2021, max compression
```

## Comparing `large-image-1.9.1.dev6.tar` & `large-image-1.9.1.dev8.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8183 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/README.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/docs/
--rw-r--r--   0 circleci  (3434) circleci  (3434)       55 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/annotations.rst
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2329 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/conf.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4028 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/config_options.rst
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2234 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/development.rst
--rw-r--r--   0 circleci  (3434) circleci  (3434)      688 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/image_conversion.rst
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1202 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/index.rst
--rwxr-xr-x   0 circleci  (3434) circleci  (3434)     1934 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/make_docs.sh
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/docs/static/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      178 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/static/custom.css
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6242 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/tilesource_options.rst
--rw-r--r--   0 circleci  (3434) circleci  (3434)      634 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/docs/upgrade.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1026 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/__init__.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image/cache_util/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2810 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/cache_util/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8118 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/cache_util/cache.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4915 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/cache_util/cachefactory.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6250 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/cache_util/memcache.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1922 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/config.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2284 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/constants.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      487 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/exceptions.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image/tilesource/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6254 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/tilesource/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)   113564 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/tilesource/base.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10578 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/tilesource/tiledict.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    20847 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/large_image/tilesource/utilities.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8183 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      816 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/not-zip-safe
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1362 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       12 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/large_image.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-20 21:01:06.000000 large-image-1.9.1.dev6/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3061 2021-12-20 21:00:58.000000 large-image-1.9.1.dev6/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8183 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/README.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/docs/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       55 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/annotations.rst
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2329 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/conf.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4028 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/config_options.rst
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2234 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/development.rst
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      688 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/image_conversion.rst
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1202 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/index.rst
+-rwxr-xr-x   0 circleci  (3434) circleci  (3434)     1934 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/make_docs.sh
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/docs/static/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      178 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/static/custom.css
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6242 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/tilesource_options.rst
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      634 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/docs/upgrade.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1026 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/__init__.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image/cache_util/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2810 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/cache_util/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8118 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/cache_util/cache.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4915 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/cache_util/cachefactory.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6250 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/cache_util/memcache.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1922 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/config.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2284 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/constants.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      487 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/exceptions.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image/tilesource/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6344 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/tilesource/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)   113564 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/tilesource/base.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10578 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/tilesource/tiledict.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    20847 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/large_image/tilesource/utilities.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8183 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      816 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/not-zip-safe
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1408 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       12 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/large_image.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-21 17:37:06.000000 large-image-1.9.1.dev8/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3116 2021-12-21 17:36:53.000000 large-image-1.9.1.dev8/setup.py
```

### Comparing `large-image-1.9.1.dev6/LICENSE` & `large-image-1.9.1.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/PKG-INFO` & `large-image-1.9.1.dev8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: Python modules to work with large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: large_image
 Platform: UNKNOWN
```

### Comparing `large-image-1.9.1.dev6/README.rst` & `large-image-1.9.1.dev8/README.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/conf.py` & `large-image-1.9.1.dev8/docs/conf.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/config_options.rst` & `large-image-1.9.1.dev8/docs/config_options.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/development.rst` & `large-image-1.9.1.dev8/docs/development.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/image_conversion.rst` & `large-image-1.9.1.dev8/docs/image_conversion.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/index.rst` & `large-image-1.9.1.dev8/docs/index.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/make_docs.sh` & `large-image-1.9.1.dev8/docs/make_docs.sh`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/tilesource_options.rst` & `large-image-1.9.1.dev8/docs/tilesource_options.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/docs/upgrade.rst` & `large-image-1.9.1.dev8/docs/upgrade.rst`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/__init__.py` & `large-image-1.9.1.dev8/large_image/__init__.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/cache_util/__init__.py` & `large-image-1.9.1.dev8/large_image/cache_util/__init__.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/cache_util/cache.py` & `large-image-1.9.1.dev8/large_image/cache_util/cache.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/cache_util/cachefactory.py` & `large-image-1.9.1.dev8/large_image/cache_util/cachefactory.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/cache_util/memcache.py` & `large-image-1.9.1.dev8/large_image/cache_util/memcache.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/config.py` & `large-image-1.9.1.dev8/large_image/config.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/constants.py` & `large-image-1.9.1.dev8/large_image/constants.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/tilesource/__init__.py` & `large-image-1.9.1.dev8/large_image/tilesource/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,9 @@
 import os
 
-from pkg_resources import iter_entry_points
-
 from .. import config
 from ..constants import SourcePriority
 from ..exceptions import (TileGeneralError, TileGeneralException,
                           TileSourceAssetstoreError,
                           TileSourceAssetstoreException, TileSourceError,
                           TileSourceException, TileSourceFileNotFoundError)
 from .base import (TILE_FORMAT_IMAGE, TILE_FORMAT_NUMPY, TILE_FORMAT_PIL,
@@ -47,15 +45,20 @@
     """
     Load all tilesources from entrypoints and add them to the
     AvailableTileSources dictionary.
 
     :param entryPointName: the name of the entry points to load.
     :param sourceDict: a dictionary to populate with the loaded sources.
     """
-    for entryPoint in iter_entry_points(entryPointName):
+    try:
+        from importlib.metadata import entry_points
+    except ImportError:
+        from importlib_metadata import entry_points
+
+    for entryPoint in entry_points()[entryPointName]:
         try:
             sourceClass = entryPoint.load()
             if sourceClass.name and None in sourceClass.extensions:
                 sourceDict[entryPoint.name] = sourceClass
                 config.getConfig('logprint').debug('Loaded tile source %s' % entryPoint.name)
         except Exception:
             config.getConfig('logprint').exception(
```

### Comparing `large-image-1.9.1.dev6/large_image/tilesource/base.py` & `large-image-1.9.1.dev8/large_image/tilesource/base.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/tilesource/tiledict.py` & `large-image-1.9.1.dev8/large_image/tilesource/tiledict.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image/tilesource/utilities.py` & `large-image-1.9.1.dev8/large_image/tilesource/utilities.py`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image.egg-info/PKG-INFO` & `large-image-1.9.1.dev8/large_image.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: large-image
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: Python modules to work with large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: large_image
 Platform: UNKNOWN
```

### Comparing `large-image-1.9.1.dev6/large_image.egg-info/SOURCES.txt` & `large-image-1.9.1.dev8/large_image.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `large-image-1.9.1.dev6/large_image.egg-info/requires.txt` & `large-image-1.9.1.dev8/large_image.egg-info/requires.txt`

 * *Files 6% similar despite different names*

```diff
@@ -1,27 +1,30 @@
 cachetools>=3.0.0
 palettable
 Pillow!=8.3.0,!=8.3.1
 psutil>=4.2.0
 numpy>=1.10.4
 
+[:python_version < "3.8"]
+importlib-metadata
+
 [all]
-large-image-source-ometiff
-large-image-source-gdal
+large-image-source-deepzoom
+large-image-source-nd2
 large-image-source-mapnik
-large-image-source-pil
-large-image-source-openjpeg
 large-image-source-tiff
-large-image-source-deepzoom
+large-image-source-gdal
+large-image-source-ometiff
+large-image-source-openjpeg
+large-image-source-openslide
 large-image-converter
-large-image-source-dummy
-large-image-source-bioformats
 matplotlib
-large-image-source-openslide
-large-image-source-nd2
+large-image-source-bioformats
+large-image-source-pil
+large-image-source-dummy
 large-image-source-test
 
 [all:platform_system != "Windows"]
 pylibmc>=1.5.1
 
 [bioformats]
 large-image-source-bioformats
@@ -61,25 +64,25 @@
 [openslide]
 large-image-source-openslide
 
 [pil]
 large-image-source-pil
 
 [sources]
-large-image-source-ometiff
-large-image-source-gdal
+large-image-source-deepzoom
+large-image-source-nd2
+large-image-source-tiff
 large-image-source-mapnik
-large-image-source-pil
+large-image-source-gdal
+large-image-source-ometiff
 large-image-source-openjpeg
-large-image-source-tiff
-large-image-source-deepzoom
-large-image-source-dummy
-large-image-source-bioformats
 large-image-source-openslide
-large-image-source-nd2
+large-image-source-bioformats
+large-image-source-pil
+large-image-source-dummy
 large-image-source-test
 
 [test]
 large-image-source-test
 
 [tiff]
 large-image-source-tiff
```

### Comparing `large-image-1.9.1.dev6/setup.py` & `large-image-1.9.1.dev8/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -73,14 +73,15 @@
         'palettable',
         # We don't pin the version of Pillow, as anything newer than 3.0
         # probably works, though we'd rather have the latest.  8.3.0 won't
         # save jpeg compressed tiffs properly.
         'Pillow!=8.3.0,!=8.3.1',
         'psutil>=4.2.0',  # technically optional
         'numpy>=1.10.4',
+        'importlib-metadata ; python_version < "3.8"',
     ],
     extras_require=extraReqs,
     include_package_data=True,
     keywords='large_image',
     packages=['large_image'],
     url='https://github.com/girder/large_image',
     python_requires='>=3.6',
```

