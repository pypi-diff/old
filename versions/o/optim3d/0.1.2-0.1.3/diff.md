# Comparing `tmp/optim3d-0.1.2.tar.gz` & `tmp/optim3d-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\optim3d-0.1.2.tar", last modified: Thu Apr  6 13:58:46 2023, max compression
+gzip compressed data, was "dist\optim3d-0.1.3.tar", last modified: Thu Apr  6 14:06:07 2023, max compression
```

## Comparing `optim3d-0.1.2.tar` & `optim3d-0.1.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 13:58:46.000000 optim3d-0.1.2/
--rw-rw-rw-   0        0        0     1243 2023-04-06 13:43:27.000000 optim3d-0.1.2/COPYING
--rw-rw-rw-   0        0        0     1613 2023-04-06 13:43:27.000000 optim3d-0.1.2/LICENSE
-drwxrwxrwx   0        0        0        0 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/
--rw-rw-rw-   0        0        0        1 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       46 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0      360 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      192 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 13:58:46.000000 optim3d-0.1.2/optim3d.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      360 2023-04-06 13:58:46.000000 optim3d-0.1.2/PKG-INFO
--rw-rw-rw-   0        0        0    11580 2023-04-06 13:43:27.000000 optim3d-0.1.2/README.md
--rw-rw-rw-   0        0        0       42 2023-04-06 13:58:46.000000 optim3d-0.1.2/setup.cfg
--rw-rw-rw-   0        0        0      478 2023-04-06 13:58:14.000000 optim3d-0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:06:07.000000 optim3d-0.1.3/
+-rw-rw-rw-   0        0        0     1243 2023-04-06 13:43:27.000000 optim3d-0.1.3/COPYING
+-rw-rw-rw-   0        0        0     1613 2023-04-06 13:43:27.000000 optim3d-0.1.3/LICENSE
+drwxrwxrwx   0        0        0        0 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       46 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0      360 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      192 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:06:07.000000 optim3d-0.1.3/optim3d.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      360 2023-04-06 14:06:07.000000 optim3d-0.1.3/PKG-INFO
+-rw-rw-rw-   0        0        0    11580 2023-04-06 13:43:27.000000 optim3d-0.1.3/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:06:07.000000 optim3d-0.1.3/setup.cfg
+-rw-rw-rw-   0        0        0      549 2023-04-06 14:05:51.000000 optim3d-0.1.3/setup.py
```

### Comparing `optim3d-0.1.2/COPYING` & `optim3d-0.1.3/COPYING`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.2/LICENSE` & `optim3d-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `optim3d-0.1.2/README.md` & `optim3d-0.1.3/README.md`

 * *Files identical despite different names*

