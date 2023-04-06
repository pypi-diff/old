# Comparing `tmp/slgs1-0.0.1.tar.gz` & `tmp/slgs1-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\slgs1-0.0.1.tar", last modified: Thu Apr  6 08:11:28 2023, max compression
+gzip compressed data, was "dist\slgs1-0.0.2.tar", last modified: Thu Apr  6 09:16:33 2023, max compression
```

## Comparing `slgs1-0.0.1.tar` & `slgs1-0.0.2.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 08:11:28.000000 slgs1-0.0.1/
--rw-rw-rw-   0        0        0     1237 2023-04-06 08:11:28.000000 slgs1-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.1/README.md
--rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.1/license.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 08:11:28.000000 slgs1-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      497 2023-04-06 08:07:27.000000 slgs1-0.0.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1/
--rw-rw-rw-   0        0        0       45 2023-04-06 07:20:58.000000 slgs1-0.0.1/slgs1/__init__.py
--rw-rw-rw-   0        0        0     4372 2023-04-06 07:55:32.000000 slgs1-0.0.1/slgs1/tweet_crawler.py
-drwxrwxrwx   0        0        0        0 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1.egg-info/
--rw-rw-rw-   0        0        0     1237 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      187 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-06 08:11:28.000000 slgs1-0.0.1/slgs1.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 09:16:33.000000 slgs1-0.0.2/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 09:16:33.000000 slgs1-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.2/README.md
+-rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.2/license.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:16:33.000000 slgs1-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      497 2023-04-06 09:12:57.000000 slgs1-0.0.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1/
+-rw-rw-rw-   0        0        0       78 2023-04-06 09:15:26.000000 slgs1-0.0.2/slgs1/__init__.py
+-rw-rw-rw-   0        0        0     4372 2023-04-06 07:55:32.000000 slgs1-0.0.2/slgs1/tweet_crawler.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1.egg-info/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      187 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-06 09:16:33.000000 slgs1-0.0.2/slgs1.egg-info/top_level.txt
```

### Comparing `slgs1-0.0.1/PKG-INFO` & `slgs1-0.0.2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.1
+Version: 0.0.2
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

### Comparing `slgs1-0.0.1/README.md` & `slgs1-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.1/license.txt` & `slgs1-0.0.2/license.txt`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.1/slgs1/tweet_crawler.py` & `slgs1-0.0.2/slgs1/tweet_crawler.py`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.1/slgs1.egg-info/PKG-INFO` & `slgs1-0.0.2/slgs1.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.1
+Version: 0.0.2
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

