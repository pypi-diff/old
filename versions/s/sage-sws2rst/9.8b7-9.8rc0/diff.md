# Comparing `tmp/sage-sws2rst-9.8b7.tar.gz` & `tmp/sage-sws2rst-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sage-sws2rst-9.8b7.tar", last modified: Thu Jan 19 06:51:28 2023, max compression
+gzip compressed data, was "sage-sws2rst-9.8rc0.tar", last modified: Sun Jan 29 23:46:55 2023, max compression
```

## Comparing `sage-sws2rst-9.8b7.tar` & `sage-sws2rst-9.8rc0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:28.166531 sage-sws2rst-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-01-19 06:51:28.166531 sage-sws2rst-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      760 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/VERSION.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:28.162531 sage-sws2rst-9.8b7/bin/
--rwxr-xr-x   0 runner    (1001) docker     (123)     6861 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/bin/sage-sws2rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      192 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/check.sh
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:28.162531 sage-sws2rst-9.8b7/sage_sws2rst/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/sage_sws2rst/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15609 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/sage_sws2rst/comments2rst.py
--rw-r--r--   0 runner    (1001) docker     (123)     6046 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/sage_sws2rst/results2rst.py
--rw-r--r--   0 runner    (1001) docker     (123)     6005 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/sage_sws2rst/worksheet2rst.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:28.166531 sage-sws2rst-9.8b7/sage_sws2rst.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-01-19 06:51:27.000000 sage-sws2rst-9.8b7/sage_sws2rst.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-19 06:51:28.000000 sage-sws2rst-9.8b7/sage_sws2rst.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:27.000000 sage-sws2rst-9.8b7/sage_sws2rst.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-01-19 06:51:27.000000 sage-sws2rst-9.8b7/sage_sws2rst.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-01-19 06:51:28.166531 sage-sws2rst-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:28.166531 sage-sws2rst-9.8b7/test/
--rw-r--r--   0 runner    (1001) docker     (123)   281797 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/test/Adding_Pictures_and_screenshots.sws
--rw-r--r--   0 runner    (1001) docker     (123)    30910 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/test/MAT_141_day_25.sws
--rw-r--r--   0 runner    (1001) docker     (123)      282 2023-01-19 06:47:40.000000 sage-sws2rst-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:55.649827 sage-sws2rst-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)       27 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1093 2023-01-29 23:46:55.649827 sage-sws2rst-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      760 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/VERSION.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:55.645827 sage-sws2rst-9.8rc0/bin/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6861 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/bin/sage-sws2rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      192 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/check.sh
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:55.645827 sage-sws2rst-9.8rc0/sage_sws2rst/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/sage_sws2rst/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15609 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/sage_sws2rst/comments2rst.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6046 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/sage_sws2rst/results2rst.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6005 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/sage_sws2rst/worksheet2rst.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:55.645827 sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1093 2023-01-29 23:46:54.000000 sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-29 23:46:55.000000 sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:46:54.000000 sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-01-29 23:46:54.000000 sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-01-29 23:46:55.649827 sage-sws2rst-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:55.649827 sage-sws2rst-9.8rc0/test/
+-rw-r--r--   0 runner    (1001) docker     (123)   281797 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/test/Adding_Pictures_and_screenshots.sws
+-rw-r--r--   0 runner    (1001) docker     (123)    30910 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/test/MAT_141_day_25.sws
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-01-29 23:43:48.000000 sage-sws2rst-9.8rc0/tox.ini
```

### Comparing `sage-sws2rst-9.8b7/PKG-INFO` & `sage-sws2rst-9.8rc0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-sws2rst
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: SageNB worksheet converter
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v3 or later
 Description-Content-Type: text/x-rst
```

### Comparing `sage-sws2rst-9.8b7/README.rst` & `sage-sws2rst-9.8rc0/README.rst`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/bin/sage-sws2rst` & `sage-sws2rst-9.8rc0/bin/sage-sws2rst`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/sage_sws2rst/comments2rst.py` & `sage-sws2rst-9.8rc0/sage_sws2rst/comments2rst.py`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/sage_sws2rst/results2rst.py` & `sage-sws2rst-9.8rc0/sage_sws2rst/results2rst.py`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/sage_sws2rst/worksheet2rst.py` & `sage-sws2rst-9.8rc0/sage_sws2rst/worksheet2rst.py`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/sage_sws2rst.egg-info/PKG-INFO` & `sage-sws2rst-9.8rc0/sage_sws2rst.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-sws2rst
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: SageNB worksheet converter
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v3 or later
 Description-Content-Type: text/x-rst
```

### Comparing `sage-sws2rst-9.8b7/test/Adding_Pictures_and_screenshots.sws` & `sage-sws2rst-9.8rc0/test/Adding_Pictures_and_screenshots.sws`

 * *Files identical despite different names*

### Comparing `sage-sws2rst-9.8b7/test/MAT_141_day_25.sws` & `sage-sws2rst-9.8rc0/test/MAT_141_day_25.sws`

 * *Files identical despite different names*

