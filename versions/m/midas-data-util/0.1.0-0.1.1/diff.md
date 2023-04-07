# Comparing `tmp/midas-data-util-0.1.0.tar.gz` & `tmp/midas-data-util-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "midas-data-util-0.1.0.tar", last modified: Fri Apr  7 08:30:31 2023, max compression
+gzip compressed data, was "midas-data-util-0.1.1.tar", last modified: Fri Apr  7 09:00:02 2023, max compression
```

## Comparing `midas-data-util-0.1.0.tar` & `midas-data-util-0.1.1.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 08:30:31.010396 midas-data-util-0.1.0/
--rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.0/LICENSE
--rw-rw-rw-   0        0        0      457 2023-04-07 08:30:31.009398 midas-data-util-0.1.0/PKG-INFO
--rw-rw-rw-   0        0        0      116 2023-04-07 08:28:09.000000 midas-data-util-0.1.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 08:30:30.996276 midas-data-util-0.1.0/midas_data_util.egg-info/
--rw-rw-rw-   0        0        0      457 2023-04-07 08:30:30.000000 midas-data-util-0.1.0/midas_data_util.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      311 2023-04-07 08:30:30.000000 midas-data-util-0.1.0/midas_data_util.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 08:30:30.000000 midas-data-util-0.1.0/midas_data_util.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       29 2023-04-07 08:30:30.000000 midas-data-util-0.1.0/midas_data_util.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-04-07 08:30:30.000000 midas-data-util-0.1.0/midas_data_util.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 08:30:31.010396 midas-data-util-0.1.0/setup.cfg
--rw-rw-rw-   0        0        0      561 2023-04-07 08:30:26.000000 midas-data-util-0.1.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 08:30:31.007404 midas-data-util-0.1.0/src/
--rw-rw-rw-   0        0        0     2032 2023-04-07 08:19:44.000000 midas-data-util-0.1.0/src/__init__.py
--rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.0/src/data_encoder.py
--rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.0/src/event.py
--rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.0/src/playfab.py
--rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.0/src/session.py
--rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.0/src/user.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.469005 midas-data-util-0.1.1/
+-rw-rw-rw-   0        0        0    11558 2023-04-07 08:14:57.000000 midas-data-util-0.1.1/LICENSE
+-rw-rw-rw-   0        0        0      520 2023-04-07 09:00:02.468018 midas-data-util-0.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0      116 2023-04-07 08:58:48.000000 midas-data-util-0.1.1/README.md
+-rw-rw-rw-   0        0        0      489 2023-04-07 08:58:48.000000 midas-data-util-0.1.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 09:00:02.470004 midas-data-util-0.1.1/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.433155 midas-data-util-0.1.1/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.446883 midas-data-util-0.1.1/src/midas-data-util/
+-rw-rw-rw-   0        0        0     2032 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/__init__.py
+-rw-rw-rw-   0        0        0     5817 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/data_encoder.py
+-rw-rw-rw-   0        0        0     5445 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/event.py
+-rw-rw-rw-   0        0        0     9406 2023-04-03 07:08:38.000000 midas-data-util-0.1.1/src/midas-data-util/playfab.py
+-rw-rw-rw-   0        0        0     7436 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/session.py
+-rw-rw-rw-   0        0        0     3218 2023-04-07 08:19:44.000000 midas-data-util-0.1.1/src/midas-data-util/user.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:00:02.466040 midas-data-util-0.1.1/src/midas_data_util.egg-info/
+-rw-rw-rw-   0        0        0      520 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      391 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       16 2023-04-07 09:00:02.000000 midas-data-util-0.1.1/src/midas_data_util.egg-info/top_level.txt
```

### Comparing `midas-data-util-0.1.0/LICENSE` & `midas-data-util-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/__init__.py` & `midas-data-util-0.1.1/src/midas-data-util/__init__.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/data_encoder.py` & `midas-data-util-0.1.1/src/midas-data-util/data_encoder.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/event.py` & `midas-data-util-0.1.1/src/midas-data-util/event.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/playfab.py` & `midas-data-util-0.1.1/src/midas-data-util/playfab.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/session.py` & `midas-data-util-0.1.1/src/midas-data-util/session.py`

 * *Files identical despite different names*

### Comparing `midas-data-util-0.1.0/src/user.py` & `midas-data-util-0.1.1/src/midas-data-util/user.py`

 * *Files identical despite different names*

