# Comparing `tmp/midas-data-util-0.1.4.tar.gz` & `tmp/midas-data-util-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "midas-data-util-0.1.4.tar", last modified: Fri Apr  7 11:19:48 2023, max compression
+gzip compressed data, was "midas-data-util-0.1.5.tar", last modified: Fri Apr  7 11:23:00 2023, max compression
```

## Comparing `midas-data-util-0.1.4.tar` & `midas-data-util-0.1.5.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 11:19:48.172603 midas-data-util-0.1.4/
--rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.4/LICENSE
--rw-rw-rw-   0        0        0      520 2023-04-07 11:19:48.171604 midas-data-util-0.1.4/PKG-INFO
--rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.4/README.md
--rw-rw-rw-   0        0        0      489 2023-04-07 11:18:59.000000 midas-data-util-0.1.4/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 11:19:48.172603 midas-data-util-0.1.4/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 11:19:48.131492 midas-data-util-0.1.4/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 11:19:48.156095 midas-data-util-0.1.4/src/midas/
--rw-rw-rw-   0        0        0     1975 2023-04-07 11:10:36.000000 midas-data-util-0.1.4/src/midas/__init__.py
--rw-rw-rw-   0        0        0     5818 2023-04-07 11:16:15.000000 midas-data-util-0.1.4/src/midas/data_encoder.py
--rw-rw-rw-   0        0        0     5458 2023-04-07 11:16:15.000000 midas-data-util-0.1.4/src/midas/event.py
--rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.4/src/midas/playfab.py
--rw-rw-rw-   0        0        0     7460 2023-04-07 11:18:59.000000 midas-data-util-0.1.4/src/midas/session.py
--rw-rw-rw-   0        0        0     3244 2023-04-07 11:17:45.000000 midas-data-util-0.1.4/src/midas/user.py
-drwxrwxrwx   0        0        0        0 2023-04-07 11:19:48.170633 midas-data-util-0.1.4/src/midas_data_util.egg-info/
--rw-rw-rw-   0        0        0      520 2023-04-07 11:19:48.000000 midas-data-util-0.1.4/src/midas_data_util.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      331 2023-04-07 11:19:48.000000 midas-data-util-0.1.4/src/midas_data_util.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 11:19:48.000000 midas-data-util-0.1.4/src/midas_data_util.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-07 11:19:48.000000 midas-data-util-0.1.4/src/midas_data_util.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 11:23:00.483735 midas-data-util-0.1.5/
+-rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.5/LICENSE
+-rw-rw-rw-   0        0        0      520 2023-04-07 11:23:00.481741 midas-data-util-0.1.5/PKG-INFO
+-rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.5/README.md
+-rw-rw-rw-   0        0        0      489 2023-04-07 11:22:26.000000 midas-data-util-0.1.5/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 11:23:00.483735 midas-data-util-0.1.5/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 11:22:59.715789 midas-data-util-0.1.5/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 11:22:59.920272 midas-data-util-0.1.5/src/midas/
+-rw-rw-rw-   0        0        0     1975 2023-04-07 11:10:36.000000 midas-data-util-0.1.5/src/midas/__init__.py
+-rw-rw-rw-   0        0        0     5818 2023-04-07 11:16:15.000000 midas-data-util-0.1.5/src/midas/data_encoder.py
+-rw-rw-rw-   0        0        0     5458 2023-04-07 11:16:15.000000 midas-data-util-0.1.5/src/midas/event.py
+-rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.5/src/midas/playfab.py
+-rw-rw-rw-   0        0        0     7460 2023-04-07 11:18:59.000000 midas-data-util-0.1.5/src/midas/session.py
+-rw-rw-rw-   0        0        0     3244 2023-04-07 11:17:45.000000 midas-data-util-0.1.5/src/midas/user.py
+drwxrwxrwx   0        0        0        0 2023-04-07 11:23:00.480744 midas-data-util-0.1.5/src/midas_data_util.egg-info/
+-rw-rw-rw-   0        0        0      520 2023-04-07 11:22:59.000000 midas-data-util-0.1.5/src/midas_data_util.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      331 2023-04-07 11:22:59.000000 midas-data-util-0.1.5/src/midas_data_util.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 11:22:59.000000 midas-data-util-0.1.5/src/midas_data_util.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 11:22:59.000000 midas-data-util-0.1.5/src/midas_data_util.egg-info/top_level.txt
```

### Comparing `midas-data-util-0.1.4/LICENSE` & `midas-data-util-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/PKG-INFO` & `midas-data-util-0.1.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.4
+Version: 0.1.5
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `midas-data-util-0.1.4/src/midas/__init__.py` & `midas-data-util-0.1.5/src/midas/__init__.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas/data_encoder.py` & `midas-data-util-0.1.5/src/midas/data_encoder.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas/event.py` & `midas-data-util-0.1.5/src/midas/event.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas/playfab.py` & `midas-data-util-0.1.5/src/midas/playfab.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas/session.py` & `midas-data-util-0.1.5/src/midas/session.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas/user.py` & `midas-data-util-0.1.5/src/midas/user.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.4/src/midas_data_util.egg-info/PKG-INFO` & `midas-data-util-0.1.5/src/midas_data_util.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.4
+Version: 0.1.5
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

