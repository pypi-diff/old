# Comparing `tmp/whatpack.py-0.0.2.1.tar.gz` & `tmp/whatpack.py-0.0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "whatpack.py-0.0.2.1.tar", last modified: Thu Apr  6 12:50:39 2023, max compression
+gzip compressed data, was "whatpack.py-0.0.2.2.tar", last modified: Thu Apr  6 13:14:19 2023, max compression
```

## Comparing `whatpack.py-0.0.2.1.tar` & `whatpack.py-0.0.2.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.644046 whatpack.py-0.0.2.1/
--rw-rw-rw-   0        0        0    11551 2023-04-03 13:57:52.000000 whatpack.py-0.0.2.1/LICENSE
--rw-rw-rw-   0        0        0     4245 2023-04-06 12:50:39.644046 whatpack.py-0.0.2.1/PKG-INFO
--rw-rw-rw-   0        0        0     3333 2023-04-05 09:26:10.000000 whatpack.py-0.0.2.1/README.md
--rw-rw-rw-   0        0        0       42 2023-04-06 12:50:39.644046 whatpack.py-0.0.2.1/setup.cfg
--rw-rw-rw-   0        0        0     2100 2023-04-06 12:49:56.000000 whatpack.py-0.0.2.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.628107 whatpack.py-0.0.2.1/whatpack/
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.628107 whatpack.py-0.0.2.1/whatpack/asyncpy/
--rw-rw-rw-   0        0        0      669 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.1/whatpack/asyncpy/__init__.py
--rw-rw-rw-   0        0        0    12763 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.1/whatpack/asyncpy/whats.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.628107 whatpack.py-0.0.2.1/whatpack/headless/
--rw-rw-rw-   0        0        0      639 2023-03-30 05:47:06.000000 whatpack.py-0.0.2.1/whatpack/headless/__init__.py
--rw-rw-rw-   0        0        0     1416 2023-03-30 05:50:43.000000 whatpack.py-0.0.2.1/whatpack/headless/app.py
--rw-rw-rw-   0        0        0     9715 2023-03-30 05:43:14.000000 whatpack.py-0.0.2.1/whatpack/headless/whats.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.628107 whatpack.py-0.0.2.1/whatpack/sync/
--rw-rw-rw-   0        0        0      669 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.1/whatpack/sync/__init__.py
--rw-rw-rw-   0        0        0    12549 2023-04-06 12:33:52.000000 whatpack.py-0.0.2.1/whatpack/sync/whats.py
-drwxrwxrwx   0        0        0        0 2023-04-06 12:50:39.628107 whatpack.py-0.0.2.1/whatpack.py.egg-info/
--rw-rw-rw-   0        0        0     4245 2023-04-06 12:50:39.000000 whatpack.py-0.0.2.1/whatpack.py.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      386 2023-04-06 12:50:39.000000 whatpack.py-0.0.2.1/whatpack.py.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 12:50:39.000000 whatpack.py-0.0.2.1/whatpack.py.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       91 2023-04-06 12:50:39.000000 whatpack.py-0.0.2.1/whatpack.py.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-06 12:50:39.000000 whatpack.py-0.0.2.1/whatpack.py.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.533001 whatpack.py-0.0.2.2/
+-rw-rw-rw-   0        0        0    11551 2023-04-03 13:57:52.000000 whatpack.py-0.0.2.2/LICENSE
+-rw-rw-rw-   0        0        0     4245 2023-04-06 13:14:19.533001 whatpack.py-0.0.2.2/PKG-INFO
+-rw-rw-rw-   0        0        0     3333 2023-04-05 09:26:10.000000 whatpack.py-0.0.2.2/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 13:14:19.534070 whatpack.py-0.0.2.2/setup.cfg
+-rw-rw-rw-   0        0        0     2126 2023-04-06 12:53:41.000000 whatpack.py-0.0.2.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.518507 whatpack.py-0.0.2.2/whatpack/
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.527497 whatpack.py-0.0.2.2/whatpack/asyncpy/
+-rw-rw-rw-   0        0        0      669 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.2/whatpack/asyncpy/__init__.py
+-rw-rw-rw-   0        0        0    12763 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.2/whatpack/asyncpy/whats.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.530179 whatpack.py-0.0.2.2/whatpack/headless/
+-rw-rw-rw-   0        0        0      639 2023-03-30 05:47:06.000000 whatpack.py-0.0.2.2/whatpack/headless/__init__.py
+-rw-rw-rw-   0        0        0     1416 2023-03-30 05:50:43.000000 whatpack.py-0.0.2.2/whatpack/headless/app.py
+-rw-rw-rw-   0        0        0     9715 2023-03-30 05:43:14.000000 whatpack.py-0.0.2.2/whatpack/headless/whats.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.531970 whatpack.py-0.0.2.2/whatpack/sync/
+-rw-rw-rw-   0        0        0      669 2023-04-06 12:46:07.000000 whatpack.py-0.0.2.2/whatpack/sync/__init__.py
+-rw-rw-rw-   0        0        0    12549 2023-04-06 12:33:52.000000 whatpack.py-0.0.2.2/whatpack/sync/whats.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:19.526582 whatpack.py-0.0.2.2/whatpack.py.egg-info/
+-rw-rw-rw-   0        0        0     4245 2023-04-06 13:14:19.000000 whatpack.py-0.0.2.2/whatpack.py.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      386 2023-04-06 13:14:19.000000 whatpack.py-0.0.2.2/whatpack.py.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 13:14:19.000000 whatpack.py-0.0.2.2/whatpack.py.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       91 2023-04-06 13:14:19.000000 whatpack.py-0.0.2.2/whatpack.py.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 13:14:19.000000 whatpack.py-0.0.2.2/whatpack.py.egg-info/top_level.txt
```

### Comparing `whatpack.py-0.0.2.1/LICENSE` & `whatpack.py-0.0.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/PKG-INFO` & `whatpack.py-0.0.2.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: whatpack.py
-Version: 0.0.2.1
+Version: 0.0.2.2
 Summary: About whatpack.py is a Python package that
 Home-page: https://github.com/SigireddyBalasai/whatpack.py
 Download-URL: https://github.com/SigireddyBalasai/whatpack.py
 Author: SigireddyBalasai
 Author-email: sigireddybalasai@gmail.com
 Maintainer: SigireddyBalasai
 Maintainer-email: SigireddyBalasai@gmail.com
```

### Comparing `whatpack.py-0.0.2.1/README.md` & `whatpack.py-0.0.2.2/README.md`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/setup.py` & `whatpack.py-0.0.2.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,33 +1,33 @@
 """THis is the setup.py file for whatpack.py"""
 import os
 from distutils.core import setup
-
+import pathlib
 dir_path = os.path.dirname(os.path.realpath(__file__))
 
 
 def readme_str() -> str:
     """This will return the readme file"""
     with open(r"README.md") as file:
         readme = file.read()
         return readme
 
 
 def reqs():
     """This will return the requirements file"""
     print(dir_path)
-    with open((dir_path + "//requirements.txt"), "r", encoding="UTF-8") as file:
+    with open((pathlib.Path(dir_path) / "requirements.txt"), "r", encoding="UTF-8") as file:
         requirements = [line.strip() for line in file]
         return requirements
 
 
 setup(
     name="whatpack.py",
     packages=['whatpack', 'whatpack.asyncpy', 'whatpack.sync', 'whatpack.headless'],
-    version="0.0.2.1",
+    version="0.0.2.2",
     maintainer="SigireddyBalasai",
     maintainer_email="SigireddyBalasai@gmail.com",
     setup_requires=['setuptools_scm'],
     use_scm_version=True,
     license="MIT",
     description="""About whatpack.py is a Python package that
     allows you to automate WhatsApp and YouTube tasks in an asynchronous
```

### Comparing `whatpack.py-0.0.2.1/whatpack/asyncpy/__init__.py` & `whatpack.py-0.0.2.2/whatpack/asyncpy/__init__.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/asyncpy/whats.py` & `whatpack.py-0.0.2.2/whatpack/asyncpy/whats.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/headless/__init__.py` & `whatpack.py-0.0.2.2/whatpack/headless/__init__.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/headless/app.py` & `whatpack.py-0.0.2.2/whatpack/headless/app.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/headless/whats.py` & `whatpack.py-0.0.2.2/whatpack/headless/whats.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/sync/__init__.py` & `whatpack.py-0.0.2.2/whatpack/sync/__init__.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack/sync/whats.py` & `whatpack.py-0.0.2.2/whatpack/sync/whats.py`

 * *Files identical despite different names*

### Comparing `whatpack.py-0.0.2.1/whatpack.py.egg-info/PKG-INFO` & `whatpack.py-0.0.2.2/whatpack.py.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: whatpack.py
-Version: 0.0.2.1
+Version: 0.0.2.2
 Summary: About whatpack.py is a Python package that
 Home-page: https://github.com/SigireddyBalasai/whatpack.py
 Download-URL: https://github.com/SigireddyBalasai/whatpack.py
 Author: SigireddyBalasai
 Author-email: sigireddybalasai@gmail.com
 Maintainer: SigireddyBalasai
 Maintainer-email: SigireddyBalasai@gmail.com
```

