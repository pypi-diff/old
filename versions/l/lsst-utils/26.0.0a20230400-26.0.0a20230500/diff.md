# Comparing `tmp/lsst-utils-26.0.0a20230400.tar.gz` & `tmp/lsst-utils-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-utils-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:37 2023, max compression
+gzip compressed data, was "lsst-utils-26.0.0a20230500.tar", last modified: Thu Feb  2 14:05:21 2023, max compression
```

## Comparing `lsst-utils-26.0.0a20230400.tar` & `lsst-utils-26.0.0a20230500.tar`

### file list

```diff
@@ -1,45 +1,45 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      519 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.939856 lsst-utils-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.939856 lsst-utils-26.0.0a20230400/doc/lsst.utils/
--rw-r--r--   0 runner    (1001) docker     (123)     3864 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/doc/lsst.utils/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/doc/lsst.utils/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3390 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.939856 lsst-utils-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.939856 lsst-utils-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)      499 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/python/lsst/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      923 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/_forwarded.py
--rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/_packaging.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/python/lsst/utils/backtrace/
--rw-r--r--   0 runner    (1001) docker     (123)     1015 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/backtrace/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4790 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/classes.py
--rw-r--r--   0 runner    (1001) docker     (123)     3437 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/deprecated.py
--rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/doImport.py
--rw-r--r--   0 runner    (1001) docker     (123)     1792 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/ellipsis.py
--rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/get_caller_name.py
--rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/inheritDoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5703 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/introspection.py
--rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/iteration.py
--rw-r--r--   0 runner    (1001) docker     (123)    14180 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)    19159 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/packages.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    34935 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/threads.py
--rw-r--r--   0 runner    (1001) docker     (123)    17944 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/timer.py
--rw-r--r--   0 runner    (1001) docker     (123)     4607 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/usage.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/version.py
--rw-r--r--   0 runner    (1001) docker     (123)    18090 2023-01-26 09:56:25.000000 lsst-utils-26.0.0a20230400/python/lsst/utils/wrappers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1026 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      158 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:37.000000 lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-01-26 09:56:37.943856 lsst-utils-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.951897 lsst-utils-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.951897 lsst-utils-26.0.0a20230500/doc/lsst.utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     3864 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/doc/lsst.utils/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/doc/lsst.utils/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3391 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.951897 lsst-utils-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.951897 lsst-utils-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)      499 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/python/lsst/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      923 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/_forwarded.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/_packaging.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/python/lsst/utils/backtrace/
+-rw-r--r--   0 runner    (1001) docker     (123)     1015 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/backtrace/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4790 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/classes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3437 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/deprecated.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/doImport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1791 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/ellipsis.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/get_caller_name.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/inheritDoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5703 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/introspection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/iteration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14180 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19159 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/packages.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    34934 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/threads.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17944 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4607 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/usage.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18090 2023-02-02 14:05:07.000000 lsst-utils-26.0.0a20230500/python/lsst/utils/wrappers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1315 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1026 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      158 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:21.000000 lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-02-02 14:05:21.955897 lsst-utils-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-utils-26.0.0a20230400/LICENSE` & `lsst-utils-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/PKG-INFO` & `lsst-utils-26.0.0a20230500/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-utils
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Utility functions from Rubin Observatory Data Management for the Legacy Survey of Space and Time (LSST).
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: BSD 3-Clause License
 Project-URL: Homepage, https://github.com/lsst/utils
 Keywords: lsst
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `lsst-utils-26.0.0a20230400/README.rst` & `lsst-utils-26.0.0a20230500/README.rst`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/doc/lsst.utils/CHANGES.rst` & `lsst-utils-26.0.0a20230500/doc/lsst.utils/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/doc/lsst.utils/index.rst` & `lsst-utils-26.0.0a20230500/doc/lsst.utils/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/pyproject.toml` & `lsst-utils-26.0.0a20230500/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -94,15 +94,15 @@
     [[tool.towncrier.type]]
         directory = "removal"
         name = "An API Removal or Deprecation"
         showcontent = false
 
 [tool.black]
 line-length = 110
-target-version = ["py38"]
+target-version = ["py310"]
 
 [tool.isort]
 profile = "black"
 line_length = 110
 
 [tool.lsst_versions]
 write_to = "python/lsst/utils/version.py"
```

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/__init__.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/_forwarded.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/_forwarded.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/_packaging.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/_packaging.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/backtrace/__init__.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/backtrace/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/classes.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/classes.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/deprecated.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/deprecated.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/doImport.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/doImport.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/ellipsis.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/ellipsis.py`

 * *Files 4% similar despite different names*

```diff
@@ -34,15 +34,14 @@
 from __future__ import annotations
 
 __all__ = ("Ellipsis", "EllipsisType")
 
 from typing import TYPE_CHECKING
 
 if TYPE_CHECKING:
-
     from enum import Enum
 
     class EllipsisType(Enum):
         Ellipsis = "..."
 
     Ellipsis = EllipsisType.Ellipsis
```

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/get_caller_name.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/get_caller_name.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/inheritDoc.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/inheritDoc.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/introspection.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/introspection.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/iteration.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/iteration.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/logging.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/logging.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/packages.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/packages.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/tests.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/tests.py`

 * *Files 0% similar despite different names*

```diff
@@ -623,15 +623,15 @@
     """
     if ignoreNaNs:
         lhsMask = numpy.isnan(lhs)
         rhsMask = numpy.isnan(rhs)
         if not numpy.all(lhsMask == rhsMask):
             testCase.fail(
                 f"lhs has {lhsMask.sum()} NaN values and rhs has {rhsMask.sum()} NaN values, "
-                f"in different locations."
+                "in different locations."
             )
         if numpy.all(lhsMask):
             assert numpy.all(rhsMask), "Should be guaranteed by previous if."
             # All operands are fully NaN (either scalar NaNs or arrays of only
             # NaNs).
             return
         assert not numpy.all(rhsMask), "Should be guaranteed by prevoius two ifs."
```

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/threads.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/threads.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/timer.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/timer.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/usage.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/usage.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst/utils/wrappers.py` & `lsst-utils-26.0.0a20230500/python/lsst/utils/wrappers.py`

 * *Files identical despite different names*

### Comparing `lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/PKG-INFO` & `lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-utils
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Utility functions from Rubin Observatory Data Management for the Legacy Survey of Space and Time (LSST).
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: BSD 3-Clause License
 Project-URL: Homepage, https://github.com/lsst/utils
 Keywords: lsst
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `lsst-utils-26.0.0a20230400/python/lsst_utils.egg-info/SOURCES.txt` & `lsst-utils-26.0.0a20230500/python/lsst_utils.egg-info/SOURCES.txt`

 * *Files identical despite different names*

