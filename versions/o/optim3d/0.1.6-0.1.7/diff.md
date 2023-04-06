# Comparing `tmp/optim3d-0.1.6.tar.gz` & `tmp/optim3d-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\optim3d-0.1.6.tar", last modified: Thu Apr  6 14:13:20 2023, max compression
+gzip compressed data, was "dist\optim3d-0.1.7.tar", last modified: Thu Apr  6 14:35:25 2023, max compression
```

## Comparing `optim3d-0.1.6.tar` & `optim3d-0.1.7.tar`

### file list

```diff
@@ -1,19 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:13:20.000000 optim3d-0.1.6/
--rw-rw-rw-   0        0        0     1243 2023-04-06 13:43:27.000000 optim3d-0.1.6/COPYING
--rw-rw-rw-   0        0        0     1613 2023-04-06 13:43:27.000000 optim3d-0.1.6/LICENSE
-drwxrwxrwx   0        0        0        0 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d/
-drwxrwxrwx   0        0        0        0 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d/config/
--rw-rw-rw-   0        0        0    20163 2023-04-06 13:43:27.000000 optim3d-0.1.6/optim3d/config/reconstruct.json
--rw-rw-rw-   0        0        0    43428 2023-04-06 13:43:27.000000 optim3d-0.1.6/optim3d/config/reconstruct_.json
--rw-rw-rw-   0        0        0    22145 2023-04-06 13:43:27.000000 optim3d-0.1.6/optim3d/main.py
--rw-rw-rw-   0        0        0        0 2023-04-06 14:11:05.000000 optim3d-0.1.6/optim3d/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/
--rw-rw-rw-   0        0        0        1 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       46 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      360 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      293 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        8 2023-04-06 14:13:20.000000 optim3d-0.1.6/optim3d.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      360 2023-04-06 14:13:20.000000 optim3d-0.1.6/PKG-INFO
--rw-rw-rw-   0        0        0    11580 2023-04-06 13:43:27.000000 optim3d-0.1.6/README.md
--rw-rw-rw-   0        0        0       42 2023-04-06 14:13:20.000000 optim3d-0.1.6/setup.cfg
--rw-rw-rw-   0        0        0      575 2023-04-06 14:13:01.000000 optim3d-0.1.6/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:35:25.000000 optim3d-0.1.7/
+-rw-rw-rw-   0        0        0     1243 2023-04-06 13:43:27.000000 optim3d-0.1.7/COPYING
+-rw-rw-rw-   0        0        0     1613 2023-04-06 13:43:27.000000 optim3d-0.1.7/LICENSE
+drwxrwxrwx   0        0        0        0 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d/
+drwxrwxrwx   0        0        0        0 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d/config/
+-rw-rw-rw-   0        0        0    20163 2023-04-06 13:43:27.000000 optim3d-0.1.7/optim3d/config/reconstruct.json
+-rw-rw-rw-   0        0        0    43428 2023-04-06 13:43:27.000000 optim3d-0.1.7/optim3d/config/reconstruct_.json
+-rw-rw-rw-   0        0        0    22145 2023-04-06 13:43:27.000000 optim3d-0.1.7/optim3d/main.py
+-rw-rw-rw-   0        0        0        0 2023-04-06 14:11:05.000000 optim3d-0.1.7/optim3d/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       46 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      360 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0       59 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/requires.txt
+-rw-rw-rw-   0        0        0      323 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 14:35:25.000000 optim3d-0.1.7/optim3d.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      360 2023-04-06 14:35:25.000000 optim3d-0.1.7/PKG-INFO
+-rw-rw-rw-   0        0        0    11580 2023-04-06 13:43:27.000000 optim3d-0.1.7/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:35:25.000000 optim3d-0.1.7/setup.cfg
+-rw-rw-rw-   0        0        0      703 2023-04-06 14:34:50.000000 optim3d-0.1.7/setup.py
```

### Comparing `optim3d-0.1.6/COPYING` & `optim3d-0.1.7/COPYING`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.6/LICENSE` & `optim3d-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.6/optim3d/config/reconstruct.json` & `optim3d-0.1.7/optim3d/config/reconstruct.json`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.6/optim3d/config/reconstruct_.json` & `optim3d-0.1.7/optim3d/config/reconstruct_.json`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.6/optim3d/main.py` & `optim3d-0.1.7/optim3d/main.py`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.6/README.md` & `optim3d-0.1.7/README.md`

 * *Files identical despite different names*

