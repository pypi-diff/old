# Comparing `tmp/opshive_tools-0.1.1.tar.gz` & `tmp/opshive_tools-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "opshive_tools-0.1.1.tar", last modified: Fri Apr  7 10:13:15 2023, max compression
+gzip compressed data, was "opshive_tools-0.1.2.tar", last modified: Fri Apr  7 10:54:00 2023, max compression
```

## Comparing `opshive_tools-0.1.1.tar` & `opshive_tools-0.1.2.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxr-xr-x   0 opshive   (1000) opshive   (1001)        0 2023-04-07 10:13:15.163740 opshive_tools-0.1.1/
--rw-r--r--   0 opshive   (1000) opshive   (1001)       57 2023-04-07 10:13:15.163740 opshive_tools-0.1.1/PKG-INFO
--rw-r--r--   0 opshive   (1000) opshive   (1001)      182 2023-04-07 08:22:33.000000 opshive_tools-0.1.1/README.md
-drwxr-xr-x   0 opshive   (1000) opshive   (1001)        0 2023-04-07 10:13:15.160406 opshive_tools-0.1.1/opshive_tools.egg-info/
--rw-r--r--   0 opshive   (1000) opshive   (1001)       57 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/PKG-INFO
--rw-r--r--   0 opshive   (1000) opshive   (1001)      242 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/SOURCES.txt
--rw-r--r--   0 opshive   (1000) opshive   (1001)        1 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/dependency_links.txt
--rw-r--r--   0 opshive   (1000) opshive   (1001)       63 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/entry_points.txt
--rw-r--r--   0 opshive   (1000) opshive   (1001)       17 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/requires.txt
--rw-r--r--   0 opshive   (1000) opshive   (1001)        1 2023-04-07 10:13:15.000000 opshive_tools-0.1.1/opshive_tools.egg-info/top_level.txt
--rw-r--r--   0 opshive   (1000) opshive   (1001)       38 2023-04-07 10:13:15.163740 opshive_tools-0.1.1/setup.cfg
--rw-r--r--   0 opshive   (1000) opshive   (1001)      321 2023-04-07 08:18:35.000000 opshive_tools-0.1.1/setup.py
+drwxr-xr-x   0 opshive   (1000) opshive   (1001)        0 2023-04-07 10:54:00.028147 opshive_tools-0.1.2/
+-rw-r--r--   0 opshive   (1000) opshive   (1001)       57 2023-04-07 10:54:00.028147 opshive_tools-0.1.2/PKG-INFO
+-rw-r--r--   0 opshive   (1000) opshive   (1001)      182 2023-04-07 08:22:33.000000 opshive_tools-0.1.2/README.md
+drwxr-xr-x   0 opshive   (1000) opshive   (1001)        0 2023-04-07 10:54:00.028147 opshive_tools-0.1.2/opshive_tools.egg-info/
+-rw-r--r--   0 opshive   (1000) opshive   (1001)       57 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/PKG-INFO
+-rw-r--r--   0 opshive   (1000) opshive   (1001)      242 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 opshive   (1000) opshive   (1001)        1 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 opshive   (1000) opshive   (1001)       63 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/entry_points.txt
+-rw-r--r--   0 opshive   (1000) opshive   (1001)       17 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/requires.txt
+-rw-r--r--   0 opshive   (1000) opshive   (1001)        1 2023-04-07 10:53:59.000000 opshive_tools-0.1.2/opshive_tools.egg-info/top_level.txt
+-rw-r--r--   0 opshive   (1000) opshive   (1001)       38 2023-04-07 10:54:00.028147 opshive_tools-0.1.2/setup.cfg
+-rw-r--r--   0 opshive   (1000) opshive   (1001)      321 2023-04-07 10:53:45.000000 opshive_tools-0.1.2/setup.py
```

