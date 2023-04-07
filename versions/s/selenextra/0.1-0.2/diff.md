# Comparing `tmp/selenextra-0.1.tar.gz` & `tmp/selenextra-0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "selenextra-0.1.tar", last modified: Fri Apr  7 13:45:54 2023, max compression
+gzip compressed data, was "selenextra-0.2.tar", last modified: Fri Apr  7 13:51:08 2023, max compression
```

## Comparing `selenextra-0.1.tar` & `selenextra-0.2.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:45:54.793976 selenextra-0.1/
--rw-rw-rw-   0        0        0     1097 2023-04-07 13:08:13.000000 selenextra-0.1/LICENSE
--rw-rw-rw-   0        0        0      625 2023-04-07 13:45:54.793976 selenextra-0.1/PKG-INFO
--rw-rw-rw-   0        0        0       57 2023-04-07 13:08:13.000000 selenextra-0.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 13:45:54.788990 selenextra-0.1/selenextra/
--rw-rw-rw-   0        0        0     3740 2023-04-07 13:28:36.000000 selenextra-0.1/selenextra/__init__.py
--rw-rw-rw-   0        0        0       46 2023-04-07 13:08:13.000000 selenextra-0.1/selenextra/exceptions.py
--rw-rw-rw-   0        0        0     1239 2023-04-07 13:08:13.000000 selenextra-0.1/selenextra/patcher.py
--rw-rw-rw-   0        0        0     5149 2023-04-07 13:08:13.000000 selenextra-0.1/selenextra/typer.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:45:54.792980 selenextra-0.1/selenextra.egg-info/
--rw-rw-rw-   0        0        0      625 2023-04-07 13:45:54.000000 selenextra-0.1/selenextra.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      285 2023-04-07 13:45:54.000000 selenextra-0.1/selenextra.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:45:54.000000 selenextra-0.1/selenextra.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       44 2023-04-07 13:45:54.000000 selenextra-0.1/selenextra.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-07 13:45:54.000000 selenextra-0.1/selenextra.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 13:45:54.794974 selenextra-0.1/setup.cfg
--rw-rw-rw-   0        0        0      863 2023-04-07 13:45:40.000000 selenextra-0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:08.525787 selenextra-0.2/
+-rw-rw-rw-   0        0        0    35823 2023-04-07 13:48:48.000000 selenextra-0.2/LICENSE
+-rw-rw-rw-   0        0        0      625 2023-04-07 13:51:08.524789 selenextra-0.2/PKG-INFO
+-rw-rw-rw-   0        0        0       57 2023-04-07 13:48:48.000000 selenextra-0.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:08.518805 selenextra-0.2/selenextra/
+-rw-rw-rw-   0        0        0     3740 2023-04-07 13:48:48.000000 selenextra-0.2/selenextra/__init__.py
+-rw-rw-rw-   0        0        0       46 2023-04-07 13:48:48.000000 selenextra-0.2/selenextra/exceptions.py
+-rw-rw-rw-   0        0        0     1239 2023-04-07 13:48:48.000000 selenextra-0.2/selenextra/patcher.py
+-rw-rw-rw-   0        0        0     5149 2023-04-07 13:48:48.000000 selenextra-0.2/selenextra/typer.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:08.524789 selenextra-0.2/selenextra.egg-info/
+-rw-rw-rw-   0        0        0      625 2023-04-07 13:51:08.000000 selenextra-0.2/selenextra.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      285 2023-04-07 13:51:08.000000 selenextra-0.2/selenextra.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:51:08.000000 selenextra-0.2/selenextra.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       44 2023-04-07 13:51:08.000000 selenextra-0.2/selenextra.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 13:51:08.000000 selenextra-0.2/selenextra.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:51:08.525787 selenextra-0.2/setup.cfg
+-rw-rw-rw-   0        0        0      798 2023-04-07 13:49:28.000000 selenextra-0.2/setup.py
```

### Comparing `selenextra-0.1/PKG-INFO` & `selenextra-0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: selenextra
-Version: 0.1
+Version: 0.2
 Summary: Bringing additional features to Selenium
 Home-page: https://github.com/nguyenvantat1182002/SeleneXtra
 Author: Tat Nguyen Van
 Author-email: nguyenvantat1182002@gmail.com
 License: UNKNOWN
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `selenextra-0.1/selenextra/__init__.py` & `selenextra-0.2/selenextra/__init__.py`

 * *Files identical despite different names*

### Comparing `selenextra-0.1/selenextra/patcher.py` & `selenextra-0.2/selenextra/patcher.py`

 * *Files identical despite different names*

### Comparing `selenextra-0.1/selenextra/typer.py` & `selenextra-0.2/selenextra/typer.py`

 * *Files identical despite different names*

### Comparing `selenextra-0.1/selenextra.egg-info/PKG-INFO` & `selenextra-0.2/selenextra.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: selenextra
-Version: 0.1
+Version: 0.2
 Summary: Bringing additional features to Selenium
 Home-page: https://github.com/nguyenvantat1182002/SeleneXtra
 Author: Tat Nguyen Van
 Author-email: nguyenvantat1182002@gmail.com
 License: UNKNOWN
 Description: UNKNOWN
 Platform: UNKNOWN
```

