# Comparing `tmp/gfagraphs-0.1.8.tar.gz` & `tmp/gfagraphs-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gfagraphs-0.1.8.tar", last modified: Wed Feb 15 16:03:23 2023, max compression
+gzip compressed data, was "gfagraphs-0.1.9.tar", last modified: Wed Feb 15 16:07:34 2023, max compression
```

## Comparing `gfagraphs-0.1.8.tar` & `gfagraphs-0.1.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:03:23.173295 gfagraphs-0.1.8/
--rw-r--r--   0 sidubois (669136) genscale (35005)     1066 2023-02-08 10:12:32.000000 gfagraphs-0.1.8/LICENSE
--rw-r--r--   0 sidubois (669136) genscale (35005)      677 2023-02-15 16:03:23.172294 gfagraphs-0.1.8/PKG-INFO
--rw-r--r--   0 sidubois (669136) genscale (35005)       80 2023-02-15 11:31:37.000000 gfagraphs-0.1.8/README.md
-drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:03:23.150292 gfagraphs-0.1.8/gfagraphs/
--rw-r--r--   0 sidubois (669136) genscale (35005)      136 2023-02-15 13:05:46.000000 gfagraphs-0.1.8/gfagraphs/__init__.py
--rw-r--r--   0 sidubois (669136) genscale (35005)    12170 2023-02-15 16:03:03.000000 gfagraphs-0.1.8/gfagraphs/gfagraphs.py
-drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:03:23.169291 gfagraphs-0.1.8/gfagraphs.egg-info/
--rw-r--r--   0 sidubois (669136) genscale (35005)      677 2023-02-15 16:03:23.000000 gfagraphs-0.1.8/gfagraphs.egg-info/PKG-INFO
--rw-r--r--   0 sidubois (669136) genscale (35005)      282 2023-02-15 16:03:23.000000 gfagraphs-0.1.8/gfagraphs.egg-info/SOURCES.txt
--rw-r--r--   0 sidubois (669136) genscale (35005)        1 2023-02-15 16:03:23.000000 gfagraphs-0.1.8/gfagraphs.egg-info/dependency_links.txt
--rw-r--r--   0 sidubois (669136) genscale (35005)        1 2023-02-15 16:03:22.000000 gfagraphs-0.1.8/gfagraphs.egg-info/not-zip-safe
--rw-r--r--   0 sidubois (669136) genscale (35005)       23 2023-02-15 16:03:23.000000 gfagraphs-0.1.8/gfagraphs.egg-info/requires.txt
--rw-r--r--   0 sidubois (669136) genscale (35005)       10 2023-02-15 16:03:23.000000 gfagraphs-0.1.8/gfagraphs.egg-info/top_level.txt
--rw-r--r--   0 sidubois (669136) genscale (35005)      593 2023-02-15 16:01:53.000000 gfagraphs-0.1.8/pyproject.toml
--rw-r--r--   0 sidubois (669136) genscale (35005)       38 2023-02-15 16:03:23.174295 gfagraphs-0.1.8/setup.cfg
--rw-r--r--   0 sidubois (669136) genscale (35005)      373 2023-02-15 16:01:58.000000 gfagraphs-0.1.8/setup.py
+drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:07:34.783276 gfagraphs-0.1.9/
+-rw-r--r--   0 sidubois (669136) genscale (35005)     1066 2023-02-08 10:12:32.000000 gfagraphs-0.1.9/LICENSE
+-rw-r--r--   0 sidubois (669136) genscale (35005)      677 2023-02-15 16:07:34.782275 gfagraphs-0.1.9/PKG-INFO
+-rw-r--r--   0 sidubois (669136) genscale (35005)       80 2023-02-15 11:31:37.000000 gfagraphs-0.1.9/README.md
+drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:07:34.760274 gfagraphs-0.1.9/gfagraphs/
+-rw-r--r--   0 sidubois (669136) genscale (35005)      136 2023-02-15 13:05:46.000000 gfagraphs-0.1.9/gfagraphs/__init__.py
+-rw-r--r--   0 sidubois (669136) genscale (35005)    12170 2023-02-15 16:03:03.000000 gfagraphs-0.1.9/gfagraphs/gfagraphs.py
+drwxr-xr-x   0 sidubois (669136) genscale (35005)        0 2023-02-15 16:07:34.779274 gfagraphs-0.1.9/gfagraphs.egg-info/
+-rw-r--r--   0 sidubois (669136) genscale (35005)      677 2023-02-15 16:07:34.000000 gfagraphs-0.1.9/gfagraphs.egg-info/PKG-INFO
+-rw-r--r--   0 sidubois (669136) genscale (35005)      282 2023-02-15 16:07:34.000000 gfagraphs-0.1.9/gfagraphs.egg-info/SOURCES.txt
+-rw-r--r--   0 sidubois (669136) genscale (35005)        1 2023-02-15 16:07:34.000000 gfagraphs-0.1.9/gfagraphs.egg-info/dependency_links.txt
+-rw-r--r--   0 sidubois (669136) genscale (35005)        1 2023-02-15 16:03:22.000000 gfagraphs-0.1.9/gfagraphs.egg-info/not-zip-safe
+-rw-r--r--   0 sidubois (669136) genscale (35005)       24 2023-02-15 16:07:34.000000 gfagraphs-0.1.9/gfagraphs.egg-info/requires.txt
+-rw-r--r--   0 sidubois (669136) genscale (35005)       10 2023-02-15 16:07:34.000000 gfagraphs-0.1.9/gfagraphs.egg-info/top_level.txt
+-rw-r--r--   0 sidubois (669136) genscale (35005)      593 2023-02-15 16:07:18.000000 gfagraphs-0.1.9/pyproject.toml
+-rw-r--r--   0 sidubois (669136) genscale (35005)       38 2023-02-15 16:07:34.784275 gfagraphs-0.1.9/setup.cfg
+-rw-r--r--   0 sidubois (669136) genscale (35005)      374 2023-02-15 16:07:13.000000 gfagraphs-0.1.9/setup.py
```

### Comparing `gfagraphs-0.1.8/LICENSE` & `gfagraphs-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `gfagraphs-0.1.8/PKG-INFO` & `gfagraphs-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gfagraphs
-Version: 0.1.8
+Version: 0.1.9
 Summary: Package that packs some utility functions.
 Home-page: https://github.com/Tharos-ux/gfatypes
 Author: Tharos
 Author-email: Tharos <dubois.siegfried@gmail.com>
 License: MIT
 Project-URL: Homepage, https://github.com/Tharos-ux/gfatypes
 Project-URL: Bug Tracker, https://github.com/Tharos-ux/gfatypes/issues
```

### Comparing `gfagraphs-0.1.8/gfagraphs/gfagraphs.py` & `gfagraphs-0.1.9/gfagraphs/gfagraphs.py`

 * *Files identical despite different names*

### Comparing `gfagraphs-0.1.8/gfagraphs.egg-info/PKG-INFO` & `gfagraphs-0.1.9/gfagraphs.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gfagraphs
-Version: 0.1.8
+Version: 0.1.9
 Summary: Package that packs some utility functions.
 Home-page: https://github.com/Tharos-ux/gfatypes
 Author: Tharos
 Author-email: Tharos <dubois.siegfried@gmail.com>
 License: MIT
 Project-URL: Homepage, https://github.com/Tharos-ux/gfatypes
 Project-URL: Bug Tracker, https://github.com/Tharos-ux/gfatypes/issues
```

### Comparing `gfagraphs-0.1.8/pyproject.toml` & `gfagraphs-0.1.9/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "gfagraphs"
-version = "0.1.8"
+version = "0.1.9"
 authors = [
   { name="Tharos", email="dubois.siegfried@gmail.com" },
 ]
 description = "Package that packs some utility functions."
 readme = "README.md"
 requires-python = ">=3.10"
 classifiers = [
```

