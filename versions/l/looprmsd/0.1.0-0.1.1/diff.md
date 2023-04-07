# Comparing `tmp/looprmsd-0.1.0.tar.gz` & `tmp/looprmsd-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "looprmsd-0.1.0.tar", last modified: Fri Apr  7 02:02:17 2023, max compression
+gzip compressed data, was "looprmsd-0.1.1.tar", last modified: Fri Apr  7 02:37:17 2023, max compression
```

## Comparing `looprmsd-0.1.0.tar` & `looprmsd-0.1.1.tar`

### file list

```diff
@@ -1,12 +1,13 @@
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:02:17.009796 looprmsd-0.1.0/
--rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.0/LICENCE
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:02:17.009796 looprmsd-0.1.0/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)     1019 2023-04-07 01:55:16.000000 looprmsd-0.1.0/README.md
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:02:17.009796 looprmsd-0.1.0/looprmsd.egg-info/
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:02:17.000000 looprmsd-0.1.0/looprmsd.egg-info/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)      185 2023-04-07 02:02:17.000000 looprmsd-0.1.0/looprmsd.egg-info/SOURCES.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:02:17.000000 looprmsd-0.1.0/looprmsd.egg-info/dependency_links.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       16 2023-04-07 02:02:17.000000 looprmsd-0.1.0/looprmsd.egg-info/requires.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:02:17.000000 looprmsd-0.1.0/looprmsd.egg-info/top_level.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 02:02:17.009796 looprmsd-0.1.0/setup.cfg
--rw-r--r--   0 jeffrey   (1014) galux      (500)      362 2023-04-07 02:02:00.000000 looprmsd-0.1.0/setup.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:37:17.232382 looprmsd-0.1.1/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.1/LICENCE
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:37:17.232382 looprmsd-0.1.1/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)     1019 2023-04-07 01:55:16.000000 looprmsd-0.1.1/README.md
+-rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5187 2023-04-07 01:48:50.000000 looprmsd-0.1.1/loop_rmsd_antibody.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:37:17.232382 looprmsd-0.1.1/looprmsd.egg-info/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:37:17.000000 looprmsd-0.1.1/looprmsd.egg-info/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      207 2023-04-07 02:37:17.000000 looprmsd-0.1.1/looprmsd.egg-info/SOURCES.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:37:17.000000 looprmsd-0.1.1/looprmsd.egg-info/dependency_links.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       16 2023-04-07 02:37:17.000000 looprmsd-0.1.1/looprmsd.egg-info/requires.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       19 2023-04-07 02:37:17.000000 looprmsd-0.1.1/looprmsd.egg-info/top_level.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 02:37:17.232382 looprmsd-0.1.1/setup.cfg
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      403 2023-04-07 02:36:25.000000 looprmsd-0.1.1/setup.py
```

### Comparing `looprmsd-0.1.0/README.md` & `looprmsd-0.1.1/README.md`

 * *Files identical despite different names*

