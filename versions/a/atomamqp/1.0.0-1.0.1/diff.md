# Comparing `tmp/atomamqp-1.0.0.tar.gz` & `tmp/atomamqp-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "atomamqp-1.0.0.tar", last modified: Fri Apr  7 02:54:54 2023, max compression
+gzip compressed data, was "atomamqp-1.0.1.tar", last modified: Fri Apr  7 02:59:19 2023, max compression
```

## Comparing `atomamqp-1.0.0.tar` & `atomamqp-1.0.1.tar`

### file list

```diff
@@ -1,11 +1,11 @@
-drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 02:54:54.834291 atomamqp-1.0.0/
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      426 2023-04-07 02:54:54.830291 atomamqp-1.0.0/PKG-INFO
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)     1100 2023-04-06 03:29:42.000000 atomamqp-1.0.0/README.md
-drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 02:54:54.830291 atomamqp-1.0.0/atomamqp.egg-info/
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      426 2023-04-07 02:54:54.000000 atomamqp-1.0.0/atomamqp.egg-info/PKG-INFO
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      177 2023-04-07 02:54:54.000000 atomamqp-1.0.0/atomamqp.egg-info/SOURCES.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 02:54:54.000000 atomamqp-1.0.0/atomamqp.egg-info/dependency_links.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       12 2023-04-07 02:54:54.000000 atomamqp-1.0.0/atomamqp.egg-info/requires.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 02:54:54.000000 atomamqp-1.0.0/atomamqp.egg-info/top_level.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       38 2023-04-07 02:54:54.834291 atomamqp-1.0.0/setup.cfg
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      529 2023-04-07 02:54:36.000000 atomamqp-1.0.0/setup.py
+drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 02:59:19.052762 atomamqp-1.0.1/
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      426 2023-04-07 02:59:19.052762 atomamqp-1.0.1/PKG-INFO
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)     1100 2023-04-06 03:29:42.000000 atomamqp-1.0.1/README.md
+drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 02:59:19.048762 atomamqp-1.0.1/atomamqp.egg-info/
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      426 2023-04-07 02:59:19.000000 atomamqp-1.0.1/atomamqp.egg-info/PKG-INFO
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      177 2023-04-07 02:59:19.000000 atomamqp-1.0.1/atomamqp.egg-info/SOURCES.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 02:59:19.000000 atomamqp-1.0.1/atomamqp.egg-info/dependency_links.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       12 2023-04-07 02:59:19.000000 atomamqp-1.0.1/atomamqp.egg-info/requires.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 02:59:19.000000 atomamqp-1.0.1/atomamqp.egg-info/top_level.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       38 2023-04-07 02:59:19.052762 atomamqp-1.0.1/setup.cfg
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      529 2023-04-07 02:59:07.000000 atomamqp-1.0.1/setup.py
```

### Comparing `atomamqp-1.0.0/README.md` & `atomamqp-1.0.1/README.md`

 * *Files identical despite different names*

