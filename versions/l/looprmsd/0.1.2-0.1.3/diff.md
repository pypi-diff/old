# Comparing `tmp/looprmsd-0.1.2.tar.gz` & `tmp/looprmsd-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "looprmsd-0.1.2.tar", last modified: Fri Apr  7 02:39:38 2023, max compression
+gzip compressed data, was "looprmsd-0.1.3.tar", last modified: Fri Apr  7 02:48:36 2023, max compression
```

## Comparing `looprmsd-0.1.2.tar` & `looprmsd-0.1.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:39:38.482119 looprmsd-0.1.2/
--rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.2/LICENCE
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:39:38.482119 looprmsd-0.1.2/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)     1019 2023-04-07 01:55:16.000000 looprmsd-0.1.2/README.md
--rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5187 2023-04-07 01:48:50.000000 looprmsd-0.1.2/loop_rmsd_antibody.py
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:39:38.482119 looprmsd-0.1.2/looprmsd.egg-info/
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:39:38.000000 looprmsd-0.1.2/looprmsd.egg-info/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)      207 2023-04-07 02:39:38.000000 looprmsd-0.1.2/looprmsd.egg-info/SOURCES.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:39:38.000000 looprmsd-0.1.2/looprmsd.egg-info/dependency_links.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       16 2023-04-07 02:39:38.000000 looprmsd-0.1.2/looprmsd.egg-info/requires.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       19 2023-04-07 02:39:38.000000 looprmsd-0.1.2/looprmsd.egg-info/top_level.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 02:39:38.482119 looprmsd-0.1.2/setup.cfg
--rw-r--r--   0 jeffrey   (1014) galux      (500)      403 2023-04-07 02:39:30.000000 looprmsd-0.1.2/setup.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:48:36.710279 looprmsd-0.1.3/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.3/LICENCE
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:48:36.710279 looprmsd-0.1.3/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)     1019 2023-04-07 01:55:16.000000 looprmsd-0.1.3/README.md
+-rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5187 2023-04-07 01:48:50.000000 looprmsd-0.1.3/loop_rmsd_antibody.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:48:36.710279 looprmsd-0.1.3/looprmsd.egg-info/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      207 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/SOURCES.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/dependency_links.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       16 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/requires.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       19 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/top_level.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 02:48:36.710279 looprmsd-0.1.3/setup.cfg
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      411 2023-04-07 02:48:20.000000 looprmsd-0.1.3/setup.py
```

### Comparing `looprmsd-0.1.2/README.md` & `looprmsd-0.1.3/README.md`

 * *Files identical despite different names*

### Comparing `looprmsd-0.1.2/loop_rmsd_antibody.py` & `looprmsd-0.1.3/loop_rmsd_antibody.py`

 * *Files identical despite different names*

