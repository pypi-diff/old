# Comparing `tmp/libtukaan-mac-0.1.2.tar.gz` & `tmp/libtukaan-mac-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "libtukaan-mac-0.1.2.tar", last modified: Tue Aug 30 21:42:17 2022, max compression
+gzip compressed data, was "libtukaan-mac-0.1.3.tar", last modified: Thu Apr  6 13:08:53 2023, max compression
```

## Comparing `libtukaan-mac-0.1.2.tar` & `libtukaan-mac-0.1.3.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxr-xr-x   0 runner     (501) staff       (20)        0 2022-08-30 21:42:17.732050 libtukaan-mac-0.1.2/
--rw-r--r--   0 runner     (501) staff       (20)      423 2022-08-30 21:42:17.731573 libtukaan-mac-0.1.2/PKG-INFO
-drwxr-xr-x   0 runner     (501) staff       (20)        0 2022-08-30 21:42:17.728621 libtukaan-mac-0.1.2/libtukaan/
--rw-r--r--   0 runner     (501) staff       (20)       25 2022-08-30 21:42:05.000000 libtukaan-mac-0.1.2/libtukaan/__init__.py
-drwxr-xr-x   0 runner     (501) staff       (20)        0 2022-08-30 21:42:17.729111 libtukaan-mac-0.1.2/libtukaan/mac/
--rw-r--r--   0 runner     (501) staff       (20)    49992 2022-08-30 21:42:05.000000 libtukaan-mac-0.1.2/libtukaan/mac/libserif_x64.dylib
--rw-r--r--   0 runner     (501) staff       (20)     1576 2022-08-30 21:42:05.000000 libtukaan-mac-0.1.2/libtukaan/serif.py
-drwxr-xr-x   0 runner     (501) staff       (20)        0 2022-08-30 21:42:17.730938 libtukaan-mac-0.1.2/libtukaan_mac.egg-info/
--rw-r--r--   0 runner     (501) staff       (20)      423 2022-08-30 21:42:17.000000 libtukaan-mac-0.1.2/libtukaan_mac.egg-info/PKG-INFO
--rw-r--r--   0 runner     (501) staff       (20)      230 2022-08-30 21:42:17.000000 libtukaan-mac-0.1.2/libtukaan_mac.egg-info/SOURCES.txt
--rw-r--r--   0 runner     (501) staff       (20)        1 2022-08-30 21:42:17.000000 libtukaan-mac-0.1.2/libtukaan_mac.egg-info/dependency_links.txt
--rw-r--r--   0 runner     (501) staff       (20)       10 2022-08-30 21:42:17.000000 libtukaan-mac-0.1.2/libtukaan_mac.egg-info/top_level.txt
--rw-r--r--   0 runner     (501) staff       (20)       38 2022-08-30 21:42:17.732173 libtukaan-mac-0.1.2/setup.cfg
--rw-r--r--   0 runner     (501) staff       (20)      658 2022-08-30 21:42:05.000000 libtukaan-mac-0.1.2/setup.py
+drwxr-xr-x   0 runner     (501) staff       (20)        0 2023-04-06 13:08:53.953196 libtukaan-mac-0.1.3/
+-rw-r--r--   0 runner     (501) staff       (20)      423 2023-04-06 13:08:53.952806 libtukaan-mac-0.1.3/PKG-INFO
+drwxr-xr-x   0 runner     (501) staff       (20)        0 2023-04-06 13:08:53.949673 libtukaan-mac-0.1.3/libtukaan/
+-rw-r--r--   0 runner     (501) staff       (20)       25 2023-04-06 13:08:42.000000 libtukaan-mac-0.1.3/libtukaan/__init__.py
+drwxr-xr-x   0 runner     (501) staff       (20)        0 2023-04-06 13:08:53.950126 libtukaan-mac-0.1.3/libtukaan/mac/
+-rw-r--r--   0 runner     (501) staff       (20)    49992 2023-04-06 13:08:42.000000 libtukaan-mac-0.1.3/libtukaan/mac/libserif_x64.dylib
+-rw-r--r--   0 runner     (501) staff       (20)     1612 2023-04-06 13:08:42.000000 libtukaan-mac-0.1.3/libtukaan/serif.py
+drwxr-xr-x   0 runner     (501) staff       (20)        0 2023-04-06 13:08:53.952223 libtukaan-mac-0.1.3/libtukaan_mac.egg-info/
+-rw-r--r--   0 runner     (501) staff       (20)      423 2023-04-06 13:08:53.000000 libtukaan-mac-0.1.3/libtukaan_mac.egg-info/PKG-INFO
+-rw-r--r--   0 runner     (501) staff       (20)      230 2023-04-06 13:08:53.000000 libtukaan-mac-0.1.3/libtukaan_mac.egg-info/SOURCES.txt
+-rw-r--r--   0 runner     (501) staff       (20)        1 2023-04-06 13:08:53.000000 libtukaan-mac-0.1.3/libtukaan_mac.egg-info/dependency_links.txt
+-rw-r--r--   0 runner     (501) staff       (20)       10 2023-04-06 13:08:53.000000 libtukaan-mac-0.1.3/libtukaan_mac.egg-info/top_level.txt
+-rw-r--r--   0 runner     (501) staff       (20)       38 2023-04-06 13:08:53.953314 libtukaan-mac-0.1.3/setup.cfg
+-rw-r--r--   0 runner     (501) staff       (20)      658 2023-04-06 13:08:42.000000 libtukaan-mac-0.1.3/setup.py
```

### Comparing `libtukaan-mac-0.1.2/libtukaan/mac/libserif_x64.dylib` & `libtukaan-mac-0.1.3/libtukaan/mac/libserif_x64.dylib`

 * *Files identical despite different names*

### Comparing `libtukaan-mac-0.1.2/libtukaan/serif.py` & `libtukaan-mac-0.1.3/libtukaan/serif.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+from __future__ import annotations
+
 import sys
 from pathlib import Path
 
 from tukaan._tcl import Tcl
 
 
 class Serif:
```

### Comparing `libtukaan-mac-0.1.2/setup.py` & `libtukaan-mac-0.1.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from setuptools import setup
 
 platform = {"darwin": "mac", "win32": "win"}.get(sys.platform, "unix")
 
 
 setup(
     name=f"libtukaan-{platform}",
-    version="0.1.2",
+    version="0.1.3",
     license="MIT",
     author="rdbende",
     author_email="rdbende@gmail.com",
     description="Binary extensions for Tukaan",
     url="https://tukaan.github.io",
     project_urls={
         "Documentation": "https://tukaan.github.io/docs",
```

