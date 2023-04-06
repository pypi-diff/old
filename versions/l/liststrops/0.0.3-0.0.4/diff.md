# Comparing `tmp/liststrops-0.0.3.tar.gz` & `tmp/liststrops-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "liststrops-0.0.3.tar", last modified: Thu Apr  6 19:46:14 2023, max compression
+gzip compressed data, was "liststrops-0.0.4.tar", last modified: Thu Apr  6 20:00:16 2023, max compression
```

## Comparing `liststrops-0.0.3.tar` & `liststrops-0.0.4.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 19:46:14.086325 liststrops-0.0.3/
--rw-rw-rw-   0        0        0       98 2023-04-06 19:46:14.083389 liststrops-0.0.3/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-06 19:46:14.045417 liststrops-0.0.3/liststrops/
--rw-rw-rw-   0        0        0        0 2023-04-06 18:56:22.000000 liststrops-0.0.3/liststrops/__init__.py
--rw-rw-rw-   0        0        0      390 2023-04-06 19:07:03.000000 liststrops-0.0.3/liststrops/index.py
-drwxrwxrwx   0        0        0        0 2023-04-06 19:46:14.077751 liststrops-0.0.3/liststrops.egg-info/
--rw-rw-rw-   0        0        0       98 2023-04-06 19:46:13.000000 liststrops-0.0.3/liststrops.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      187 2023-04-06 19:46:13.000000 liststrops-0.0.3/liststrops.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 19:46:13.000000 liststrops-0.0.3/liststrops.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       11 2023-04-06 19:46:13.000000 liststrops-0.0.3/liststrops.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 19:46:14.087332 liststrops-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0      159 2023-04-06 19:45:01.000000 liststrops-0.0.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 20:00:16.356342 liststrops-0.0.4/
+-rw-rw-rw-   0        0        0       98 2023-04-06 20:00:16.352318 liststrops-0.0.4/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 20:00:16.317413 liststrops-0.0.4/liststrops/
+-rw-rw-rw-   0        0        0       20 2023-04-06 19:57:22.000000 liststrops-0.0.4/liststrops/__init__.py
+-rw-rw-rw-   0        0        0      390 2023-04-06 19:56:21.000000 liststrops-0.0.4/liststrops/index.py
+drwxrwxrwx   0        0        0        0 2023-04-06 20:00:16.345337 liststrops-0.0.4/liststrops.egg-info/
+-rw-rw-rw-   0        0        0       98 2023-04-06 20:00:15.000000 liststrops-0.0.4/liststrops.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      187 2023-04-06 20:00:16.000000 liststrops-0.0.4/liststrops.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 20:00:15.000000 liststrops-0.0.4/liststrops.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 20:00:15.000000 liststrops-0.0.4/liststrops.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 20:00:16.356342 liststrops-0.0.4/setup.cfg
+-rw-rw-rw-   0        0        0      159 2023-04-06 19:59:45.000000 liststrops-0.0.4/setup.py
```

