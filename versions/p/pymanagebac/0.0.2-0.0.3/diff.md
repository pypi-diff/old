# Comparing `tmp/pymanagebac-0.0.2.tar.gz` & `tmp/pymanagebac-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pymanagebac-0.0.2.tar", last modified: Tue Apr  4 20:12:55 2023, max compression
+gzip compressed data, was "pymanagebac-0.0.3.tar", last modified: Thu Apr  6 17:54:49 2023, max compression
```

## Comparing `pymanagebac-0.0.2.tar` & `pymanagebac-0.0.3.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-04 20:12:55.034097 pymanagebac-0.0.2/
--rw-r--r--   0 moik      (1000) moik      (1000)    35149 2023-03-28 19:37:03.000000 pymanagebac-0.0.2/LICENCE
--rw-r--r--   0 moik      (1000) moik      (1000)      864 2023-04-04 20:12:55.034097 pymanagebac-0.0.2/PKG-INFO
--rw-r--r--   0 moik      (1000) moik      (1000)      317 2023-03-28 19:37:03.000000 pymanagebac-0.0.2/README.md
-drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-04 20:12:55.034097 pymanagebac-0.0.2/pymanagebac.egg-info/
--rw-r--r--   0 moik      (1000) moik      (1000)      864 2023-04-04 20:12:54.000000 pymanagebac-0.0.2/pymanagebac.egg-info/PKG-INFO
--rw-r--r--   0 moik      (1000) moik      (1000)      235 2023-04-04 20:12:55.000000 pymanagebac-0.0.2/pymanagebac.egg-info/SOURCES.txt
--rw-r--r--   0 moik      (1000) moik      (1000)        1 2023-04-04 20:12:54.000000 pymanagebac-0.0.2/pymanagebac.egg-info/dependency_links.txt
--rw-r--r--   0 moik      (1000) moik      (1000)       13 2023-04-04 20:12:54.000000 pymanagebac-0.0.2/pymanagebac.egg-info/requires.txt
--rw-r--r--   0 moik      (1000) moik      (1000)        4 2023-04-04 20:12:54.000000 pymanagebac-0.0.2/pymanagebac.egg-info/top_level.txt
--rw-r--r--   0 moik      (1000) moik      (1000)       38 2023-04-04 20:12:55.034097 pymanagebac-0.0.2/setup.cfg
--rw-r--r--   0 moik      (1000) moik      (1000)     1170 2023-04-04 20:11:12.000000 pymanagebac-0.0.2/setup.py
-drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-04 20:12:55.034097 pymanagebac-0.0.2/src/
--rw-r--r--   0 moik      (1000) moik      (1000)       65 2023-04-04 19:44:47.000000 pymanagebac-0.0.2/src/__init__.py
--rw-r--r--   0 moik      (1000) moik      (1000)    13648 2023-04-04 19:44:47.000000 pymanagebac-0.0.2/src/pymanagebac.py
+drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-06 17:54:49.107278 pymanagebac-0.0.3/
+-rw-r--r--   0 moik      (1000) moik      (1000)    35149 2023-03-28 19:37:03.000000 pymanagebac-0.0.3/LICENCE
+-rw-r--r--   0 moik      (1000) moik      (1000)      864 2023-04-06 17:54:49.107278 pymanagebac-0.0.3/PKG-INFO
+-rw-r--r--   0 moik      (1000) moik      (1000)      505 2023-04-06 12:22:32.000000 pymanagebac-0.0.3/README.md
+drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-06 17:54:49.105944 pymanagebac-0.0.3/pymanagebac.egg-info/
+-rw-r--r--   0 moik      (1000) moik      (1000)      864 2023-04-06 17:54:49.000000 pymanagebac-0.0.3/pymanagebac.egg-info/PKG-INFO
+-rw-r--r--   0 moik      (1000) moik      (1000)      235 2023-04-06 17:54:49.000000 pymanagebac-0.0.3/pymanagebac.egg-info/SOURCES.txt
+-rw-r--r--   0 moik      (1000) moik      (1000)        1 2023-04-06 17:54:49.000000 pymanagebac-0.0.3/pymanagebac.egg-info/dependency_links.txt
+-rw-r--r--   0 moik      (1000) moik      (1000)       13 2023-04-06 17:54:49.000000 pymanagebac-0.0.3/pymanagebac.egg-info/requires.txt
+-rw-r--r--   0 moik      (1000) moik      (1000)        4 2023-04-06 17:54:49.000000 pymanagebac-0.0.3/pymanagebac.egg-info/top_level.txt
+-rw-r--r--   0 moik      (1000) moik      (1000)       38 2023-04-06 17:54:49.107278 pymanagebac-0.0.3/setup.cfg
+-rw-r--r--   0 moik      (1000) moik      (1000)     1170 2023-04-06 17:54:24.000000 pymanagebac-0.0.3/setup.py
+drwxr-xr-x   0 moik      (1000) moik      (1000)        0 2023-04-06 17:54:49.105944 pymanagebac-0.0.3/src/
+-rw-r--r--   0 moik      (1000) moik      (1000)       65 2023-04-04 19:44:47.000000 pymanagebac-0.0.3/src/__init__.py
+-rw-r--r--   0 moik      (1000) moik      (1000)    13577 2023-04-04 20:15:28.000000 pymanagebac-0.0.3/src/pymanagebac.py
```

### Comparing `pymanagebac-0.0.2/LICENCE` & `pymanagebac-0.0.3/LICENCE`

 * *Files identical despite different names*

### Comparing `pymanagebac-0.0.2/PKG-INFO` & `pymanagebac-0.0.3/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymanagebac
-Version: 0.0.2
+Version: 0.0.3
 Summary: A python module for interacting with Managebac using selenium.
 Home-page: https://github.com/supermikea/pymanagebac
 Author: Mike Wiegman Avila
 Author-email: mike12wiegman@gmail.com
 License: gplv3
 Keywords: managebac,selenium,api,scraping
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pymanagebac-0.0.2/pymanagebac.egg-info/PKG-INFO` & `pymanagebac-0.0.3/pymanagebac.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pymanagebac
-Version: 0.0.2
+Version: 0.0.3
 Summary: A python module for interacting with Managebac using selenium.
 Home-page: https://github.com/supermikea/pymanagebac
 Author: Mike Wiegman Avila
 Author-email: mike12wiegman@gmail.com
 License: gplv3
 Keywords: managebac,selenium,api,scraping
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pymanagebac-0.0.2/setup.py` & `pymanagebac-0.0.3/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from setuptools import setup, find_packages
 
-VERSION = '0.0.2'
+VERSION = '0.0.3'
 DESCRIPTION = 'A python module for interacting with Managebac using selenium.'
 LONG_DESCRIPTION = """
 pymanagebac is a python module for interacting with Managebac using selenium.
 
 this is a scraper that you can login using your student credentials.
 you can get your soon tasks from the managebac website.
 you can get your grades from the managebac website.
```

### Comparing `pymanagebac-0.0.2/src/pymanagebac.py` & `pymanagebac-0.0.3/src/pymanagebac.py`

 * *Files 0% similar despite different names*

```diff
@@ -293,15 +293,14 @@
                 parts.pop(0)
                 parts.pop(-1)
                 temp = (parts[0][:-5])
 
                 temp_max_grades.append(temp)
                 temp_grades.append(temp)
 
-            # TODO if this happens, add a dictionary for easier access
             # check if grade has criterion (basically always)
             if "<div class=\"cell criterion-grade\">" in item or criterion:
                 if not criterion:
                     criterion = True
                     continue
                 criterion = False
                 part = item[:-1]
```

