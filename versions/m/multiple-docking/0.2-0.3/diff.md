# Comparing `tmp/multiple_docking-0.2.tar.gz` & `tmp/multiple_docking-0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "multiple_docking-0.2.tar", last modified: Thu Apr  6 18:49:55 2023, max compression
+gzip compressed data, was "multiple_docking-0.3.tar", last modified: Thu Apr  6 19:08:36 2023, max compression
```

## Comparing `multiple_docking-0.2.tar` & `multiple_docking-0.3.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 18:49:55.835017 multiple_docking-0.2/
--rw-rw-r--   0 supun     (1000) supun     (1000)      238 2023-04-06 18:49:55.835017 multiple_docking-0.2/PKG-INFO
-drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 18:49:55.835017 multiple_docking-0.2/multiple_docking/
--rw-rw-r--   0 supun     (1000) supun     (1000)        0 2023-04-06 18:13:08.000000 multiple_docking-0.2/multiple_docking/__init__.py
--rw-rw-r--   0 supun     (1000) supun     (1000)     4956 2023-01-30 05:55:24.000000 multiple_docking-0.2/multiple_docking/docking.py
-drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 18:49:55.835017 multiple_docking-0.2/multiple_docking.egg-info/
--rw-rw-r--   0 supun     (1000) supun     (1000)      238 2023-04-06 18:49:55.000000 multiple_docking-0.2/multiple_docking.egg-info/PKG-INFO
--rw-rw-r--   0 supun     (1000) supun     (1000)      225 2023-04-06 18:49:55.000000 multiple_docking-0.2/multiple_docking.egg-info/SOURCES.txt
--rw-rw-r--   0 supun     (1000) supun     (1000)        1 2023-04-06 18:49:55.000000 multiple_docking-0.2/multiple_docking.egg-info/dependency_links.txt
--rw-rw-r--   0 supun     (1000) supun     (1000)       17 2023-04-06 18:49:55.000000 multiple_docking-0.2/multiple_docking.egg-info/top_level.txt
--rw-rw-r--   0 supun     (1000) supun     (1000)       38 2023-04-06 18:49:55.835017 multiple_docking-0.2/setup.cfg
--rw-rw-r--   0 supun     (1000) supun     (1000)      361 2023-04-06 18:47:56.000000 multiple_docking-0.2/setup.py
+drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 19:08:36.751582 multiple_docking-0.3/
+-rw-rw-r--   0 supun     (1000) supun     (1000)      238 2023-04-06 19:08:36.751582 multiple_docking-0.3/PKG-INFO
+drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 19:08:36.751582 multiple_docking-0.3/multiple_docking/
+-rw-rw-r--   0 supun     (1000) supun     (1000)        0 2023-04-06 18:13:08.000000 multiple_docking-0.3/multiple_docking/__init__.py
+-rw-rw-r--   0 supun     (1000) supun     (1000)     4956 2023-01-30 05:55:24.000000 multiple_docking-0.3/multiple_docking/docking.py
+drwxrwxr-x   0 supun     (1000) supun     (1000)        0 2023-04-06 19:08:36.751582 multiple_docking-0.3/multiple_docking.egg-info/
+-rw-rw-r--   0 supun     (1000) supun     (1000)      238 2023-04-06 19:08:36.000000 multiple_docking-0.3/multiple_docking.egg-info/PKG-INFO
+-rw-rw-r--   0 supun     (1000) supun     (1000)      225 2023-04-06 19:08:36.000000 multiple_docking-0.3/multiple_docking.egg-info/SOURCES.txt
+-rw-rw-r--   0 supun     (1000) supun     (1000)        1 2023-04-06 19:08:36.000000 multiple_docking-0.3/multiple_docking.egg-info/dependency_links.txt
+-rw-rw-r--   0 supun     (1000) supun     (1000)       17 2023-04-06 19:08:36.000000 multiple_docking-0.3/multiple_docking.egg-info/top_level.txt
+-rw-rw-r--   0 supun     (1000) supun     (1000)       38 2023-04-06 19:08:36.751582 multiple_docking-0.3/setup.cfg
+-rw-rw-r--   0 supun     (1000) supun     (1000)      361 2023-04-06 19:08:11.000000 multiple_docking-0.3/setup.py
```

### Comparing `multiple_docking-0.2/multiple_docking/docking.py` & `multiple_docking-0.3/multiple_docking/docking.py`

 * *Files identical despite different names*

