# Comparing `tmp/crunchstat_summary-2.6.0rc3.tar.gz` & `tmp/crunchstat_summary-2.6.0rc6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was ".upload_dist/crunchstat_summary-2.6.0rc3.tar", last modified: Tue Mar  7 19:02:40 2023, max compression
+gzip compressed data, was ".upload_dist/crunchstat_summary-2.6.0rc6.tar", last modified: Wed Apr  5 20:17:28 2023, max compression
```

## Comparing `crunchstat_summary-2.6.0rc3.tar` & `crunchstat_summary-2.6.0rc6.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      226 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/MANIFEST.in
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      380 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/PKG-INFO
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      130 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/README.rst
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)    34520 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/agpl-3.0.txt
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     2028 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/arvados_version.py
-drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/bin/
--rwxr-xr-x   0 jenkins   (1001) jenkins   (1002)      475 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/bin/crunchstat-summary
-drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      191 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/__init__.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)       25 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/_version.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3720 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/command.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3017 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/dygraphs.js
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     1754 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/dygraphs.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3380 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/reader.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)    30650 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/summarizer.py
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     8454 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/synchronizer.js
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)     2131 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary/webchart.py
-drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      380 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/PKG-INFO
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)      618 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/SOURCES.txt
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)        1 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/dependency_links.txt
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)        1 2021-06-03 18:28:10.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/not-zip-safe
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)       32 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/requires.txt
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)       19 2023-03-07 19:02:39.000000 crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/top_level.txt
--rw-r--r--   0 jenkins   (1001) jenkins   (1002)       38 2023-03-07 19:02:40.000000 crunchstat_summary-2.6.0rc3/setup.cfg
--rwxr-xr-x   0 jenkins   (1001) jenkins   (1002)     1558 2023-03-07 19:02:18.000000 crunchstat_summary-2.6.0rc3/setup.py
+drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      226 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/MANIFEST.in
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      380 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/PKG-INFO
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      130 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/README.rst
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)    34520 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/agpl-3.0.txt
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     2028 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/arvados_version.py
+drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/bin/
+-rwxr-xr-x   0 jenkins   (1001) jenkins   (1002)      475 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/bin/crunchstat-summary
+drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      191 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/__init__.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)       25 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/_version.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3720 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/command.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3017 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/dygraphs.js
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     1754 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/dygraphs.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     3380 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/reader.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)    30650 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/summarizer.py
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     8454 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/synchronizer.js
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)     2131 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary/webchart.py
+drwxr-xr-x   0 jenkins   (1001) jenkins   (1002)        0 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      380 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/PKG-INFO
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)      618 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/SOURCES.txt
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)        1 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/dependency_links.txt
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)        1 2021-06-03 18:28:10.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/not-zip-safe
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)       32 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/requires.txt
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)       19 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/top_level.txt
+-rw-r--r--   0 jenkins   (1001) jenkins   (1002)       38 2023-04-05 20:17:28.000000 crunchstat_summary-2.6.0rc6/setup.cfg
+-rwxr-xr-x   0 jenkins   (1001) jenkins   (1002)     1558 2023-04-05 20:17:08.000000 crunchstat_summary-2.6.0rc6/setup.py
```

### Comparing `crunchstat_summary-2.6.0rc3/agpl-3.0.txt` & `crunchstat_summary-2.6.0rc6/agpl-3.0.txt`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/arvados_version.py` & `crunchstat_summary-2.6.0rc6/arvados_version.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/command.py` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/command.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/dygraphs.js` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/dygraphs.js`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/dygraphs.py` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/dygraphs.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/reader.py` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/reader.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/summarizer.py` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/summarizer.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/synchronizer.js` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/synchronizer.js`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary/webchart.py` & `crunchstat_summary-2.6.0rc6/crunchstat_summary/webchart.py`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/crunchstat_summary.egg-info/SOURCES.txt` & `crunchstat_summary-2.6.0rc6/crunchstat_summary.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `crunchstat_summary-2.6.0rc3/setup.py` & `crunchstat_summary-2.6.0rc6/setup.py`

 * *Files identical despite different names*

