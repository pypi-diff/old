# Comparing `tmp/midas-data-util-0.1.1.tar.gz` & `tmp/midas-data-util-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "midas-data-util-0.1.1.tar", last modified: Fri Apr  7 09:00:02 2023, max compression
+gzip compressed data, was "midas-data-util-0.1.2.tar", last modified: Fri Apr  7 09:09:29 2023, max compression
```

## Comparing `midas-data-util-0.1.1.tar` & `midas-data-util-0.1.2.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.469005 midas-data-util-0.1.1/
--rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.1/LICENSE
--rw-rw-rw-   0        0        0      520 2023-04-07 09:00:02.468018 midas-data-util-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.1/README.md
--rw-rw-rw-   0        0        0      489 2023-04-07 08:58:48.000000 midas-data-util-0.1.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 09:00:02.470004 midas-data-util-0.1.1/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.433155 midas-data-util-0.1.1/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.446883 midas-data-util-0.1.1/src/midas-data-util/
--rw-rw-rw-   0        0        0     2032 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/__init__.py
--rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/data_encoder.py
--rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/event.py
--rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.1/src/midas-data-util/playfab.py
--rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/session.py
--rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/user.py
-drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.466040 midas-data-util-0.1.1/src/midas_data_util.egg-info/
--rw-rw-rw-   0        0        0      520 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      391 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       16 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.177409 midas-data-util-0.1.2/
+-rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.2/LICENSE
+-rw-rw-rw-   0        0        0      520 2023-04-07 09:09:29.176404 midas-data-util-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.2/README.md
+-rw-rw-rw-   0        0        0      489 2023-04-07 09:08:55.000000 midas-data-util-0.1.2/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 09:09:29.177409 midas-data-util-0.1.2/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.141584 midas-data-util-0.1.2/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.156545 midas-data-util-0.1.2/src/midas/
+-rw-rw-rw-   0        0        0     2032 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/__init__.py
+-rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/data_encoder.py
+-rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/event.py
+-rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.2/src/midas/playfab.py
+-rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/session.py
+-rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.2/src/midas/user.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:09:29.174409 midas-data-util-0.1.2/src/midas_data_util.egg-info/
+-rw-rw-rw-   0        0        0      520 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      331 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 09:09:29.000000 midas-data-util-0.1.2/src/midas_data_util.egg-info/top_level.txt
```

### Comparing `midas-data-util-0.1.1/LICENSE` & `midas-data-util-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/PKG-INFO` & `midas-data-util-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.1
+Version: 0.1.2
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `midas-data-util-0.1.1/src/midas-data-util/__init__.py` & `midas-data-util-0.1.2/src/midas/__init__.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas-data-util/data_encoder.py` & `midas-data-util-0.1.2/src/midas/data_encoder.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas-data-util/event.py` & `midas-data-util-0.1.2/src/midas/event.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas-data-util/playfab.py` & `midas-data-util-0.1.2/src/midas/playfab.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas-data-util/session.py` & `midas-data-util-0.1.2/src/midas/session.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas-data-util/user.py` & `midas-data-util-0.1.2/src/midas/user.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.1/src/midas_data_util.egg-info/PKG-INFO` & `midas-data-util-0.1.2/src/midas_data_util.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: midas-data-util
-Version: 0.1.1
+Version: 0.1.2
 Summary: a package with useful functions for downloading and working with midas generated analytics data
 Author-email: nightcycle <coyer@nightcycle.us>
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

