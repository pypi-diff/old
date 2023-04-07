# Comparing `tmp/NextionEasy-0.7.tar.gz` & `tmp/NextionEasy-1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "NextionEasy-0.7.tar", last modified: Fri Apr  7 13:27:30 2023, max compression
+gzip compressed data, was "NextionEasy-1.0.tar", last modified: Fri Apr  7 13:34:04 2023, max compression
```

## Comparing `NextionEasy-0.7.tar` & `NextionEasy-1.0.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:27:30.502711 NextionEasy-0.7/
-drwxrwxrwx   0        0        0        0 2023-04-07 13:27:30.502711 NextionEasy-0.7/NextionEasy.egg-info/
--rw-rw-rw-   0        0        0      277 2023-04-07 13:27:30.000000 NextionEasy-0.7/NextionEasy.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      246 2023-04-07 13:27:30.000000 NextionEasy-0.7/NextionEasy.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:27:30.000000 NextionEasy-0.7/NextionEasy.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-07 13:24:37.000000 NextionEasy-0.7/NextionEasy.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       13 2023-04-07 13:27:30.000000 NextionEasy-0.7/NextionEasy.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      277 2023-04-07 13:27:30.502711 NextionEasy-0.7/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-07 13:27:30.502711 NextionEasy-0.7/nextion_easy/
--rw-rw-rw-   0        0        0       38 2023-04-07 13:27:10.000000 NextionEasy-0.7/nextion_easy/__init__.py
--rw-rw-rw-   0        0        0     2718 2023-04-07 13:12:21.000000 NextionEasy-0.7/nextion_easy/nextion_easy.py
--rw-rw-rw-   0        0        0       42 2023-04-07 13:27:30.502711 NextionEasy-0.7/setup.cfg
--rw-rw-rw-   0        0        0      307 2023-04-07 13:27:21.000000 NextionEasy-0.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:34:04.242458 NextionEasy-1.0/
+drwxrwxrwx   0        0        0        0 2023-04-07 13:34:04.222354 NextionEasy-1.0/NextionEasy/
+-rw-rw-rw-   0        0        0       27 2023-04-07 13:32:36.000000 NextionEasy-1.0/NextionEasy/__init__.py
+-rw-rw-rw-   0        0        0     2718 2023-04-07 13:12:21.000000 NextionEasy-1.0/NextionEasy/nextion_easy.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:34:04.242458 NextionEasy-1.0/NextionEasy.egg-info/
+-rw-rw-rw-   0        0        0      277 2023-04-07 13:34:04.000000 NextionEasy-1.0/NextionEasy.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      244 2023-04-07 13:34:04.000000 NextionEasy-1.0/NextionEasy.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:34:04.000000 NextionEasy-1.0/NextionEasy.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-07 13:34:04.000000 NextionEasy-1.0/NextionEasy.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       12 2023-04-07 13:34:04.000000 NextionEasy-1.0/NextionEasy.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      277 2023-04-07 13:34:04.242458 NextionEasy-1.0/PKG-INFO
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:34:04.242458 NextionEasy-1.0/setup.cfg
+-rw-rw-rw-   0        0        0      306 2023-04-07 13:33:50.000000 NextionEasy-1.0/setup.py
```

### Comparing `NextionEasy-0.7/nextion_easy/nextion_easy.py` & `NextionEasy-1.0/NextionEasy/nextion_easy.py`

 * *Files identical despite different names*

