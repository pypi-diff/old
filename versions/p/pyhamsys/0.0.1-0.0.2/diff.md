# Comparing `tmp/pyhamsys-0.0.1.tar.gz` & `tmp/pyhamsys-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyhamsys-0.0.1.tar", last modified: Wed Apr  5 14:54:40 2023, max compression
+gzip compressed data, was "pyhamsys-0.0.2.tar", last modified: Fri Apr  7 08:41:44 2023, max compression
```

## Comparing `pyhamsys-0.0.1.tar` & `pyhamsys-0.0.2.tar`

### file list

```diff
@@ -1,13 +1,15 @@
-drwxr-xr-x   0 cchandre   (501) staff       (20)        0 2023-04-05 14:54:40.421606 pyhamsys-0.0.1/
--rw-r--r--   0 cchandre   (501) staff       (20)     1304 2023-04-05 14:49:59.000000 pyhamsys-0.0.1/LICENSE
--rw-r--r--   0 cchandre   (501) staff       (20)      402 2023-04-05 14:54:40.421368 pyhamsys-0.0.1/PKG-INFO
--rw-r--r--   0 cchandre   (501) staff       (20)       98 2023-04-05 14:49:59.000000 pyhamsys-0.0.1/README.md
-drwxr-xr-x   0 cchandre   (501) staff       (20)        0 2023-04-05 14:54:40.419127 pyhamsys-0.0.1/pyhamsys/
-drwxr-xr-x   0 cchandre   (501) staff       (20)        0 2023-04-05 14:54:40.419233 pyhamsys-0.0.1/pyhamsys/src/
-drwxr-xr-x   0 cchandre   (501) staff       (20)        0 2023-04-05 14:54:40.421069 pyhamsys-0.0.1/pyhamsys/src/pyhamsys.egg-info/
--rw-r--r--   0 cchandre   (501) staff       (20)      402 2023-04-05 14:54:40.000000 pyhamsys-0.0.1/pyhamsys/src/pyhamsys.egg-info/PKG-INFO
--rw-r--r--   0 cchandre   (501) staff       (20)      206 2023-04-05 14:54:40.000000 pyhamsys-0.0.1/pyhamsys/src/pyhamsys.egg-info/SOURCES.txt
--rw-r--r--   0 cchandre   (501) staff       (20)        1 2023-04-05 14:54:40.000000 pyhamsys-0.0.1/pyhamsys/src/pyhamsys.egg-info/dependency_links.txt
--rw-r--r--   0 cchandre   (501) staff       (20)        1 2023-04-05 14:54:40.000000 pyhamsys-0.0.1/pyhamsys/src/pyhamsys.egg-info/top_level.txt
--rw-r--r--   0 cchandre   (501) staff       (20)       38 2023-04-05 14:54:40.421685 pyhamsys-0.0.1/setup.cfg
--rw-r--r--   0 cchandre   (501) staff       (20)      622 2023-04-05 14:51:17.000000 pyhamsys-0.0.1/setup.py
+drwxr-xr-x   0 cchandre   (503) staff       (20)        0 2023-04-07 08:41:44.348867 pyhamsys-0.0.2/
+-rw-r--r--   0 cchandre   (503) staff       (20)     1304 2023-04-07 06:56:17.000000 pyhamsys-0.0.2/LICENSE
+-rw-r--r--   0 cchandre   (503) staff       (20)     4992 2023-04-07 08:41:44.348572 pyhamsys-0.0.2/PKG-INFO
+-rw-r--r--   0 cchandre   (503) staff       (20)     4177 2023-04-07 06:56:17.000000 pyhamsys-0.0.2/README.md
+drwxr-xr-x   0 cchandre   (503) staff       (20)        0 2023-04-07 08:41:44.344852 pyhamsys-0.0.2/pyhamsys/
+drwxr-xr-x   0 cchandre   (503) staff       (20)        0 2023-04-07 08:41:44.346573 pyhamsys-0.0.2/pyhamsys/src/
+drwxr-xr-x   0 cchandre   (503) staff       (20)        0 2023-04-07 08:41:44.348116 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/
+-rw-r--r--   0 cchandre   (503) staff       (20)     4992 2023-04-07 08:41:43.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/PKG-INFO
+-rw-r--r--   0 cchandre   (503) staff       (20)      275 2023-04-07 08:41:44.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/SOURCES.txt
+-rw-r--r--   0 cchandre   (503) staff       (20)        1 2023-04-07 08:41:43.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/dependency_links.txt
+-rw-r--r--   0 cchandre   (503) staff       (20)       12 2023-04-07 08:41:43.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/requires.txt
+-rw-r--r--   0 cchandre   (503) staff       (20)        9 2023-04-07 08:41:43.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.egg-info/top_level.txt
+-rw-r--r--   0 cchandre   (503) staff       (20)    10952 2023-04-07 06:56:17.000000 pyhamsys-0.0.2/pyhamsys/src/pyhamsys.py
+-rw-r--r--   0 cchandre   (503) staff       (20)       38 2023-04-07 08:41:44.348969 pyhamsys-0.0.2/setup.cfg
+-rw-r--r--   0 cchandre   (503) staff       (20)     1129 2023-04-07 08:40:20.000000 pyhamsys-0.0.2/setup.py
```

### Comparing `pyhamsys-0.0.1/LICENSE` & `pyhamsys-0.0.2/LICENSE`

 * *Files identical despite different names*

