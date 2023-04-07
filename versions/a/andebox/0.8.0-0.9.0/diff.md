# Comparing `tmp/andebox-0.8.0.tar.gz` & `tmp/andebox-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/andebox-0.8.0.tar", last modified: Sun Apr 25 23:55:19 2021, max compression
+gzip compressed data, was "dist/andebox-0.9.0.tar", last modified: Sun Apr 25 23:57:53 2021, max compression
```

## Comparing `andebox-0.8.0.tar` & `andebox-0.9.0.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxr-x   0 az        (1000) az        (1000)        0 2021-04-25 23:55:19.567252 andebox-0.8.0/
--rw-rw-r--   0 az        (1000) az        (1000)     1069 2021-03-24 21:22:13.000000 andebox-0.8.0/LICENSE
--rw-rw-r--   0 az        (1000) az        (1000)       38 2021-03-24 21:17:18.000000 andebox-0.8.0/MANIFEST.in
--rw-rw-r--   0 az        (1000) az        (1000)    11150 2021-04-25 23:55:19.567252 andebox-0.8.0/PKG-INFO
--rw-rw-r--   0 az        (1000) az        (1000)     8567 2021-03-28 00:00:32.000000 andebox-0.8.0/README.md
--rwxrwxr-x   0 az        (1000) az        (1000)    16541 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox
-drwxrwxr-x   0 az        (1000) az        (1000)        0 2021-04-25 23:55:19.567252 andebox-0.8.0/andebox.egg-info/
--rw-rw-r--   0 az        (1000) az        (1000)    11150 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox.egg-info/PKG-INFO
--rw-rw-r--   0 az        (1000) az        (1000)      227 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox.egg-info/SOURCES.txt
--rw-rw-r--   0 az        (1000) az        (1000)        1 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox.egg-info/dependency_links.txt
--rw-rw-r--   0 az        (1000) az        (1000)        7 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox.egg-info/requires.txt
--rw-rw-r--   0 az        (1000) az        (1000)        1 2021-04-25 23:55:19.000000 andebox-0.8.0/andebox.egg-info/top_level.txt
--rw-rw-r--   0 az        (1000) az        (1000)        7 2021-04-10 11:50:20.000000 andebox-0.8.0/requirements.txt
--rw-rw-r--   0 az        (1000) az        (1000)     1446 2021-04-25 23:55:19.567252 andebox-0.8.0/setup.cfg
--rwxrwxr-x   0 az        (1000) az        (1000)      273 2021-04-25 23:55:19.000000 andebox-0.8.0/setup.py
+drwxrwxr-x   0 az        (1000) az        (1000)        0 2021-04-25 23:57:53.773797 andebox-0.9.0/
+-rw-rw-r--   0 az        (1000) az        (1000)     1069 2021-03-24 21:22:13.000000 andebox-0.9.0/LICENSE
+-rw-rw-r--   0 az        (1000) az        (1000)       38 2021-03-24 21:17:18.000000 andebox-0.9.0/MANIFEST.in
+-rw-rw-r--   0 az        (1000) az        (1000)    11150 2021-04-25 23:57:53.773797 andebox-0.9.0/PKG-INFO
+-rw-rw-r--   0 az        (1000) az        (1000)     8567 2021-03-28 00:00:32.000000 andebox-0.9.0/README.md
+-rwxrwxr-x   0 az        (1000) az        (1000)    16541 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox
+drwxrwxr-x   0 az        (1000) az        (1000)        0 2021-04-25 23:57:53.773797 andebox-0.9.0/andebox.egg-info/
+-rw-rw-r--   0 az        (1000) az        (1000)    11150 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox.egg-info/PKG-INFO
+-rw-rw-r--   0 az        (1000) az        (1000)      227 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox.egg-info/SOURCES.txt
+-rw-rw-r--   0 az        (1000) az        (1000)        1 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox.egg-info/dependency_links.txt
+-rw-rw-r--   0 az        (1000) az        (1000)        7 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox.egg-info/requires.txt
+-rw-rw-r--   0 az        (1000) az        (1000)        1 2021-04-25 23:57:53.000000 andebox-0.9.0/andebox.egg-info/top_level.txt
+-rw-rw-r--   0 az        (1000) az        (1000)        7 2021-04-10 11:50:20.000000 andebox-0.9.0/requirements.txt
+-rw-rw-r--   0 az        (1000) az        (1000)     1446 2021-04-25 23:57:53.774797 andebox-0.9.0/setup.cfg
+-rwxrwxr-x   0 az        (1000) az        (1000)      273 2021-04-25 23:57:53.000000 andebox-0.9.0/setup.py
```

### Comparing `andebox-0.8.0/LICENSE` & `andebox-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `andebox-0.8.0/PKG-INFO` & `andebox-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: andebox
-Version: 0.8.0
+Version: 0.9.0
 Summary: Ansible Developer's Box
 Home-page: https://github.com/russoz/andebox
 Author: Alexei Znamensky
 Author-email: russoz@gmail.com
 Maintainer: Alexei Znamensky
 Maintainer-email: russoz@gmail.com
 License: MIT
```

### Comparing `andebox-0.8.0/README.md` & `andebox-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `andebox-0.8.0/andebox` & `andebox-0.9.0/andebox`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 import tempfile
 import signal
 from functools import reduce, partial
 
 from distutils.version import LooseVersion
 
 
-__version__ = '0.8.0'
+__version__ = '0.9.0'
 
 
 PLUGIN_TYPES = ('connection', 'lookup', 'modules', 'doc_fragments', 'module_utils', 'callback', 'inventory')
 
 
 class AndeBox:
     actions = {}
```

### Comparing `andebox-0.8.0/andebox.egg-info/PKG-INFO` & `andebox-0.9.0/andebox.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: andebox
-Version: 0.8.0
+Version: 0.9.0
 Summary: Ansible Developer's Box
 Home-page: https://github.com/russoz/andebox
 Author: Alexei Znamensky
 Author-email: russoz@gmail.com
 Maintainer: Alexei Znamensky
 Maintainer-email: russoz@gmail.com
 License: MIT
```

### Comparing `andebox-0.8.0/setup.cfg` & `andebox-0.9.0/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [bumpversion]
-current_version = 0.8.0
+current_version = 0.9.0
 commit = True
 tag = True
 
 [bumpversion:file:setup.py]
 search = version='{current_version}'
 replace = version='{new_version}'
```

