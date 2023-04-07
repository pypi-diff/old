# Comparing `tmp/NextionEasy-0.2.tar.gz` & `tmp/NextionEasy-0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "NextionEasy-0.2.tar", last modified: Fri Apr  7 13:12:56 2023, max compression
+gzip compressed data, was "NextionEasy-0.3.tar", last modified: Fri Apr  7 13:17:28 2023, max compression
```

## Comparing `NextionEasy-0.2.tar` & `NextionEasy-0.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:12:56.021923 NextionEasy-0.2/
-drwxrwxrwx   0        0        0        0 2023-04-07 13:12:56.012209 NextionEasy-0.2/NextionEasy.egg-info/
--rw-rw-rw-   0        0        0      277 2023-04-07 13:12:55.000000 NextionEasy-0.2/NextionEasy.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      245 2023-04-07 13:12:55.000000 NextionEasy-0.2/NextionEasy.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:12:55.000000 NextionEasy-0.2/NextionEasy.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-07 13:12:55.000000 NextionEasy-0.2/NextionEasy.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       13 2023-04-07 13:12:55.000000 NextionEasy-0.2/NextionEasy.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      277 2023-04-07 13:12:56.022414 NextionEasy-0.2/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-07 13:12:56.012209 NextionEasy-0.2/nextion_easy/
--rw-rw-rw-   0        0        0     2718 2023-04-07 13:12:21.000000 NextionEasy-0.2/nextion_easy/NextionEasy.py
--rw-rw-rw-   0        0        0       36 2023-04-07 12:49:06.000000 NextionEasy-0.2/nextion_easy/__init__.py
--rw-rw-rw-   0        0        0       42 2023-04-07 13:12:56.023598 NextionEasy-0.2/setup.cfg
--rw-rw-rw-   0        0        0      307 2023-04-07 13:12:46.000000 NextionEasy-0.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:17:28.212020 NextionEasy-0.3/
+drwxrwxrwx   0        0        0        0 2023-04-07 13:17:28.212020 NextionEasy-0.3/NextionEasy.egg-info/
+-rw-rw-rw-   0        0        0      277 2023-04-07 13:17:28.000000 NextionEasy-0.3/NextionEasy.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      245 2023-04-07 13:17:28.000000 NextionEasy-0.3/NextionEasy.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:17:28.000000 NextionEasy-0.3/NextionEasy.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-07 13:17:28.000000 NextionEasy-0.3/NextionEasy.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       13 2023-04-07 13:17:28.000000 NextionEasy-0.3/NextionEasy.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      277 2023-04-07 13:17:28.212020 NextionEasy-0.3/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-07 13:17:28.212020 NextionEasy-0.3/nextion_easy/
+-rw-rw-rw-   0        0        0     2718 2023-04-07 13:12:21.000000 NextionEasy-0.3/nextion_easy/NextionEasy.py
+-rw-rw-rw-   0        0        0       37 2023-04-07 13:16:50.000000 NextionEasy-0.3/nextion_easy/__init__.py
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:17:28.212020 NextionEasy-0.3/setup.cfg
+-rw-rw-rw-   0        0        0      307 2023-04-07 13:16:59.000000 NextionEasy-0.3/setup.py
```

### Comparing `NextionEasy-0.2/nextion_easy/NextionEasy.py` & `NextionEasy-0.3/nextion_easy/NextionEasy.py`

 * *Files identical despite different names*

