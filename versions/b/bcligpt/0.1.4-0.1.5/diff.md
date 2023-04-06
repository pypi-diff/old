# Comparing `tmp/bcligpt-0.1.4.tar.gz` & `tmp/bcligpt-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bcligpt-0.1.4.tar", last modified: Thu Apr  6 10:12:50 2023, max compression
+gzip compressed data, was "bcligpt-0.1.5.tar", last modified: Thu Apr  6 10:14:18 2023, max compression
```

## Comparing `bcligpt-0.1.4.tar` & `bcligpt-0.1.5.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:12:50.454805 bcligpt-0.1.4/
--rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:12:50.454805 bcligpt-0.1.4/PKG-INFO
--rw-r--r--   0 marco     (1000) marco     (1000)      133 2023-04-03 14:53:27.000000 bcligpt-0.1.4/README.md
--rw-r--r--   0 marco     (1000) marco     (1000)      366 2023-04-06 10:12:46.000000 bcligpt-0.1.4/pyproject.toml
--rw-r--r--   0 marco     (1000) marco     (1000)       38 2023-04-06 10:12:50.454805 bcligpt-0.1.4/setup.cfg
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:12:50.454805 bcligpt-0.1.4/src/
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:12:50.454805 bcligpt-0.1.4/src/bcligpt/
--rw-r--r--   0 marco     (1000) marco     (1000)       48 2023-04-03 15:22:45.000000 bcligpt-0.1.4/src/bcligpt/__init__.py
--rw-r--r--   0 marco     (1000) marco     (1000)     2943 2023-04-06 10:02:30.000000 bcligpt-0.1.4/src/bcligpt/app.py
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:12:50.454805 bcligpt-0.1.4/src/bcligpt.egg-info/
--rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/PKG-INFO
--rw-r--r--   0 marco     (1000) marco     (1000)      279 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/SOURCES.txt
--rw-r--r--   0 marco     (1000) marco     (1000)        1 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/dependency_links.txt
--rw-r--r--   0 marco     (1000) marco     (1000)       42 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/entry_points.txt
--rw-r--r--   0 marco     (1000) marco     (1000)       16 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/requires.txt
--rw-r--r--   0 marco     (1000) marco     (1000)        8 2023-04-06 10:12:50.000000 bcligpt-0.1.4/src/bcligpt.egg-info/top_level.txt
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/
+-rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:14:18.396748 bcligpt-0.1.5/PKG-INFO
+-rw-r--r--   0 marco     (1000) marco     (1000)      133 2023-04-03 14:53:27.000000 bcligpt-0.1.5/README.md
+-rw-r--r--   0 marco     (1000) marco     (1000)      374 2023-04-06 10:14:14.000000 bcligpt-0.1.5/pyproject.toml
+-rw-r--r--   0 marco     (1000) marco     (1000)       38 2023-04-06 10:14:18.396748 bcligpt-0.1.5/setup.cfg
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.392748 bcligpt-0.1.5/src/
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/src/bcligpt/
+-rw-r--r--   0 marco     (1000) marco     (1000)       48 2023-04-03 15:22:45.000000 bcligpt-0.1.5/src/bcligpt/__init__.py
+-rw-r--r--   0 marco     (1000) marco     (1000)     2943 2023-04-06 10:02:30.000000 bcligpt-0.1.5/src/bcligpt/app.py
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/src/bcligpt.egg-info/
+-rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/PKG-INFO
+-rw-r--r--   0 marco     (1000) marco     (1000)      279 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/SOURCES.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)        1 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/dependency_links.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)       42 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/entry_points.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)       21 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/requires.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)        8 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/top_level.txt
```

### Comparing `bcligpt-0.1.4/src/bcligpt/app.py` & `bcligpt-0.1.5/src/bcligpt/app.py`

 * *Files identical despite different names*

