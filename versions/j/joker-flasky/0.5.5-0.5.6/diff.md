# Comparing `tmp/joker-flasky-0.5.5.tar.gz` & `tmp/joker-flasky-0.5.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "joker-flasky-0.5.5.tar", last modified: Thu Apr  6 02:20:53 2023, max compression
+gzip compressed data, was "joker-flasky-0.5.6.tar", last modified: Fri Apr  7 02:28:10 2023, max compression
```

## Comparing `joker-flasky-0.5.5.tar` & `joker-flasky-0.5.6.tar`

### file list

```diff
@@ -1,42 +1,42 @@
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.890973 joker-flasky-0.5.5/
--rw-r--r--   0 Hailong    (502) staff       (20)    35149 2018-11-06 12:36:13.000000 joker-flasky-0.5.5/LICENSE
--rw-r--r--   0 Hailong    (502) staff       (20)      106 2022-05-11 15:56:47.000000 joker-flasky-0.5.5/MANIFEST.in
--rw-r--r--   0 Hailong    (502) staff       (20)     1473 2023-04-06 02:20:53.890727 joker-flasky-0.5.5/PKG-INFO
--rw-r--r--   0 Hailong    (502) staff       (20)      986 2022-05-24 12:19:22.000000 joker-flasky-0.5.5/README.md
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.880616 joker-flasky-0.5.5/joker/
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.885527 joker-flasky-0.5.5/joker/flasky/
--rw-r--r--   0 Hailong    (502) staff       (20)       98 2023-04-06 02:18:28.000000 joker-flasky-0.5.5/joker/flasky/__init__.py
--rw-r--r--   0 Hailong    (502) staff       (20)     1315 2022-01-21 14:04:10.000000 joker-flasky-0.5.5/joker/flasky/app.py
--rw-r--r--   0 Hailong    (502) staff       (20)     5275 2022-05-06 15:22:35.000000 joker-flasky-0.5.5/joker/flasky/auth.py
--rw-r--r--   0 Hailong    (502) staff       (20)      919 2022-05-05 06:06:00.000000 joker-flasky-0.5.5/joker/flasky/context.py
--rw-r--r--   0 Hailong    (502) staff       (20)     1524 2021-09-04 07:05:32.000000 joker-flasky-0.5.5/joker/flasky/develop.py
--rw-r--r--   0 Hailong    (502) staff       (20)      699 2022-05-13 10:17:47.000000 joker-flasky-0.5.5/joker/flasky/environ.py
--rw-r--r--   0 Hailong    (502) staff       (20)      384 2022-05-06 15:22:35.000000 joker-flasky-0.5.5/joker/flasky/loggers.py
--rw-r--r--   0 Hailong    (502) staff       (20)     1348 2022-05-11 13:11:04.000000 joker-flasky-0.5.5/joker/flasky/pages.py
--rw-r--r--   0 Hailong    (502) staff       (20)      330 2022-03-04 12:46:49.000000 joker-flasky-0.5.5/joker/flasky/security.py
--rw-r--r--   0 Hailong    (502) staff       (20)      644 2021-09-04 16:31:12.000000 joker-flasky-0.5.5/joker/flasky/serialize.py
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.886638 joker-flasky-0.5.5/joker/flasky/templates/
--rw-r--r--   0 Hailong    (502) staff       (20)     1842 2022-05-24 11:30:42.000000 joker-flasky-0.5.5/joker/flasky/templates/help.html
--rw-r--r--   0 Hailong    (502) staff       (20)     2168 2022-05-11 12:26:38.000000 joker-flasky-0.5.5/joker/flasky/templates/helplist.html
--rw-r--r--   0 Hailong    (502) staff       (20)     1730 2022-05-13 12:40:19.000000 joker-flasky-0.5.5/joker/flasky/templates/login.html
--rw-r--r--   0 Hailong    (502) staff       (20)      583 2022-05-11 15:54:35.000000 joker-flasky-0.5.5/joker/flasky/templates/upload.html
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.887483 joker-flasky-0.5.5/joker/flasky/tools/
--rw-r--r--   0 Hailong    (502) staff       (20)       39 2021-09-04 16:34:51.000000 joker-flasky-0.5.5/joker/flasky/tools/__init__.py
--rw-r--r--   0 Hailong    (502) staff       (20)     1032 2022-05-09 15:09:48.000000 joker-flasky-0.5.5/joker/flasky/tools/docs.py
--rw-r--r--   0 Hailong    (502) staff       (20)     2056 2022-01-21 14:04:37.000000 joker-flasky-0.5.5/joker/flasky/tools/validation.py
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.888207 joker-flasky-0.5.5/joker/flasky/views/
--rw-r--r--   0 Hailong    (502) staff       (20)       39 2021-09-04 10:56:53.000000 joker-flasky-0.5.5/joker/flasky/views/__init__.py
--rw-r--r--   0 Hailong    (502) staff       (20)     2223 2021-12-08 12:08:11.000000 joker-flasky-0.5.5/joker/flasky/views/admin_views.py
--rw-r--r--   0 Hailong    (502) staff       (20)      549 2021-09-19 09:52:20.000000 joker-flasky-0.5.5/joker/flasky/views/ctxmap_views.py
--rw-r--r--   0 Hailong    (502) staff       (20)     9787 2022-05-24 12:15:56.000000 joker-flasky-0.5.5/joker/flasky/viewutils.py
-drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-06 02:20:53.890389 joker-flasky-0.5.5/joker_flasky.egg-info/
--rw-r--r--   0 Hailong    (502) staff       (20)     1473 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/PKG-INFO
--rw-r--r--   0 Hailong    (502) staff       (20)      905 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/SOURCES.txt
--rw-r--r--   0 Hailong    (502) staff       (20)        1 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/dependency_links.txt
--rw-r--r--   0 Hailong    (502) staff       (20)        6 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/namespace_packages.txt
--rw-r--r--   0 Hailong    (502) staff       (20)        1 2022-05-24 12:20:10.000000 joker-flasky-0.5.5/joker_flasky.egg-info/not-zip-safe
--rw-r--r--   0 Hailong    (502) staff       (20)       93 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/requires.txt
--rw-r--r--   0 Hailong    (502) staff       (20)        6 2023-04-06 02:20:53.000000 joker-flasky-0.5.5/joker_flasky.egg-info/top_level.txt
--rw-r--r--   0 Hailong    (502) staff       (20)       92 2023-04-06 02:17:09.000000 joker-flasky-0.5.5/requirements.txt
--rw-r--r--   0 Hailong    (502) staff       (20)       38 2023-04-06 02:20:53.891052 joker-flasky-0.5.5/setup.cfg
--rw-r--r--   0 Hailong    (502) staff       (20)     1688 2022-05-07 13:29:28.000000 joker-flasky-0.5.5/setup.py
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.090242 joker-flasky-0.5.6/
+-rw-r--r--   0 Hailong    (502) staff       (20)    35149 2018-11-06 12:36:13.000000 joker-flasky-0.5.6/LICENSE
+-rw-r--r--   0 Hailong    (502) staff       (20)      106 2022-05-11 15:56:47.000000 joker-flasky-0.5.6/MANIFEST.in
+-rw-r--r--   0 Hailong    (502) staff       (20)     1473 2023-04-07 02:28:10.089861 joker-flasky-0.5.6/PKG-INFO
+-rw-r--r--   0 Hailong    (502) staff       (20)      986 2022-05-24 12:19:22.000000 joker-flasky-0.5.6/README.md
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.069376 joker-flasky-0.5.6/joker/
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.079040 joker-flasky-0.5.6/joker/flasky/
+-rw-r--r--   0 Hailong    (502) staff       (20)       98 2023-04-07 02:27:43.000000 joker-flasky-0.5.6/joker/flasky/__init__.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     1315 2022-01-21 14:04:10.000000 joker-flasky-0.5.6/joker/flasky/app.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     5275 2022-05-06 15:22:35.000000 joker-flasky-0.5.6/joker/flasky/auth.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      919 2022-05-05 06:06:00.000000 joker-flasky-0.5.6/joker/flasky/context.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     1524 2021-09-04 07:05:32.000000 joker-flasky-0.5.6/joker/flasky/develop.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      699 2022-05-13 10:17:47.000000 joker-flasky-0.5.6/joker/flasky/environ.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      384 2022-05-06 15:22:35.000000 joker-flasky-0.5.6/joker/flasky/loggers.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     1348 2022-05-11 13:11:04.000000 joker-flasky-0.5.6/joker/flasky/pages.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      330 2022-03-04 12:46:49.000000 joker-flasky-0.5.6/joker/flasky/security.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      644 2021-09-04 16:31:12.000000 joker-flasky-0.5.6/joker/flasky/serialize.py
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.081884 joker-flasky-0.5.6/joker/flasky/templates/
+-rw-r--r--   0 Hailong    (502) staff       (20)     1842 2022-05-24 11:30:42.000000 joker-flasky-0.5.6/joker/flasky/templates/help.html
+-rw-r--r--   0 Hailong    (502) staff       (20)     2168 2022-05-11 12:26:38.000000 joker-flasky-0.5.6/joker/flasky/templates/helplist.html
+-rw-r--r--   0 Hailong    (502) staff       (20)     1730 2022-05-13 12:40:19.000000 joker-flasky-0.5.6/joker/flasky/templates/login.html
+-rw-r--r--   0 Hailong    (502) staff       (20)      583 2022-05-11 15:54:35.000000 joker-flasky-0.5.6/joker/flasky/templates/upload.html
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.084142 joker-flasky-0.5.6/joker/flasky/tools/
+-rw-r--r--   0 Hailong    (502) staff       (20)       39 2021-09-04 16:34:51.000000 joker-flasky-0.5.6/joker/flasky/tools/__init__.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     1032 2022-05-09 15:09:48.000000 joker-flasky-0.5.6/joker/flasky/tools/docs.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     2056 2022-01-21 14:04:37.000000 joker-flasky-0.5.6/joker/flasky/tools/validation.py
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.086176 joker-flasky-0.5.6/joker/flasky/views/
+-rw-r--r--   0 Hailong    (502) staff       (20)       39 2021-09-04 10:56:53.000000 joker-flasky-0.5.6/joker/flasky/views/__init__.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     2223 2021-12-08 12:08:11.000000 joker-flasky-0.5.6/joker/flasky/views/admin_views.py
+-rw-r--r--   0 Hailong    (502) staff       (20)      549 2021-09-19 09:52:20.000000 joker-flasky-0.5.6/joker/flasky/views/ctxmap_views.py
+-rw-r--r--   0 Hailong    (502) staff       (20)     9787 2022-05-24 12:15:56.000000 joker-flasky-0.5.6/joker/flasky/viewutils.py
+drwxr-xr-x   0 Hailong    (502) staff       (20)        0 2023-04-07 02:28:10.089316 joker-flasky-0.5.6/joker_flasky.egg-info/
+-rw-r--r--   0 Hailong    (502) staff       (20)     1473 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/PKG-INFO
+-rw-r--r--   0 Hailong    (502) staff       (20)      905 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/SOURCES.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)        1 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/dependency_links.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)        6 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/namespace_packages.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)        1 2022-05-24 12:20:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/not-zip-safe
+-rw-r--r--   0 Hailong    (502) staff       (20)       93 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/requires.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)        6 2023-04-07 02:28:10.000000 joker-flasky-0.5.6/joker_flasky.egg-info/top_level.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)       92 2023-04-07 02:24:17.000000 joker-flasky-0.5.6/requirements.txt
+-rw-r--r--   0 Hailong    (502) staff       (20)       38 2023-04-07 02:28:10.090373 joker-flasky-0.5.6/setup.cfg
+-rw-r--r--   0 Hailong    (502) staff       (20)     1688 2022-05-07 13:29:28.000000 joker-flasky-0.5.6/setup.py
```

### Comparing `joker-flasky-0.5.5/LICENSE` & `joker-flasky-0.5.6/LICENSE`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/PKG-INFO` & `joker-flasky-0.5.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: joker-flasky
-Version: 0.5.5
+Version: 0.5.6
 Summary: reusable components for flask-based web development
 License: GNU General Public License (GPL)
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `joker-flasky-0.5.5/README.md` & `joker-flasky-0.5.6/README.md`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/app.py` & `joker-flasky-0.5.6/joker/flasky/app.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/auth.py` & `joker-flasky-0.5.6/joker/flasky/auth.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/context.py` & `joker-flasky-0.5.6/joker/flasky/context.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/develop.py` & `joker-flasky-0.5.6/joker/flasky/develop.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/environ.py` & `joker-flasky-0.5.6/joker/flasky/environ.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/pages.py` & `joker-flasky-0.5.6/joker/flasky/pages.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/serialize.py` & `joker-flasky-0.5.6/joker/flasky/serialize.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/templates/help.html` & `joker-flasky-0.5.6/joker/flasky/templates/help.html`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/templates/helplist.html` & `joker-flasky-0.5.6/joker/flasky/templates/helplist.html`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/templates/login.html` & `joker-flasky-0.5.6/joker/flasky/templates/login.html`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/templates/upload.html` & `joker-flasky-0.5.6/joker/flasky/templates/upload.html`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/tools/docs.py` & `joker-flasky-0.5.6/joker/flasky/tools/docs.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/tools/validation.py` & `joker-flasky-0.5.6/joker/flasky/tools/validation.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/views/admin_views.py` & `joker-flasky-0.5.6/joker/flasky/views/admin_views.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/views/ctxmap_views.py` & `joker-flasky-0.5.6/joker/flasky/views/ctxmap_views.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker/flasky/viewutils.py` & `joker-flasky-0.5.6/joker/flasky/viewutils.py`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/joker_flasky.egg-info/PKG-INFO` & `joker-flasky-0.5.6/joker_flasky.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: joker-flasky
-Version: 0.5.5
+Version: 0.5.6
 Summary: reusable components for flask-based web development
 License: GNU General Public License (GPL)
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `joker-flasky-0.5.5/joker_flasky.egg-info/SOURCES.txt` & `joker-flasky-0.5.6/joker_flasky.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `joker-flasky-0.5.5/setup.py` & `joker-flasky-0.5.6/setup.py`

 * *Files identical despite different names*

