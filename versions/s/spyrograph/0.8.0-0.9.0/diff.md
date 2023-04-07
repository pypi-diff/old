# Comparing `tmp/spyrograph-0.8.0.tar.gz` & `tmp/spyrograph-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "spyrograph-0.8.0.tar", last modified: Fri Mar 17 01:33:10 2023, max compression
+gzip compressed data, was "spyrograph-0.9.0.tar", last modified: Fri Mar 17 01:50:10 2023, max compression
```

## Comparing `spyrograph-0.8.0.tar` & `spyrograph-0.9.0.tar`

### file list

```diff
@@ -1,11 +1,11 @@
-drwxrwxrwx   0 chris     (1000) chris     (1000)        0 2023-03-17 01:33:10.895048 spyrograph-0.8.0/
--rwxrwxrwx   0 chris     (1000) chris     (1000)     1077 2023-03-12 16:14:46.000000 spyrograph-0.8.0/LICENSE
--rwxrwxrwx   0 chris     (1000) chris     (1000)     3783 2023-03-17 01:33:10.894053 spyrograph-0.8.0/PKG-INFO
--rwxrwxrwx   0 chris     (1000) chris     (1000)     3286 2023-03-16 01:53:00.000000 spyrograph-0.8.0/README.md
--rwxrwxrwx   0 chris     (1000) chris     (1000)       38 2023-03-17 01:33:10.896045 spyrograph-0.8.0/setup.cfg
--rwxrwxrwx   0 chris     (1000) chris     (1000)      700 2023-03-17 01:32:34.000000 spyrograph-0.8.0/setup.py
-drwxrwxrwx   0 chris     (1000) chris     (1000)        0 2023-03-17 01:33:10.892065 spyrograph-0.8.0/spyrograph.egg-info/
--rwxrwxrwx   0 chris     (1000) chris     (1000)     3783 2023-03-17 01:33:10.000000 spyrograph-0.8.0/spyrograph.egg-info/PKG-INFO
--rwxrwxrwx   0 chris     (1000) chris     (1000)      162 2023-03-17 01:33:10.000000 spyrograph-0.8.0/spyrograph.egg-info/SOURCES.txt
--rwxrwxrwx   0 chris     (1000) chris     (1000)        1 2023-03-17 01:33:10.000000 spyrograph-0.8.0/spyrograph.egg-info/dependency_links.txt
--rwxrwxrwx   0 chris     (1000) chris     (1000)        1 2023-03-17 01:33:10.000000 spyrograph-0.8.0/spyrograph.egg-info/top_level.txt
+drwxrwxrwx   0 chris     (1000) chris     (1000)        0 2023-03-17 01:50:10.654963 spyrograph-0.9.0/
+-rwxrwxrwx   0 chris     (1000) chris     (1000)     1077 2023-03-12 16:14:46.000000 spyrograph-0.9.0/LICENSE
+-rwxrwxrwx   0 chris     (1000) chris     (1000)     3783 2023-03-17 01:50:10.652486 spyrograph-0.9.0/PKG-INFO
+-rwxrwxrwx   0 chris     (1000) chris     (1000)     3286 2023-03-16 01:53:00.000000 spyrograph-0.9.0/README.md
+-rwxrwxrwx   0 chris     (1000) chris     (1000)       38 2023-03-17 01:50:10.655063 spyrograph-0.9.0/setup.cfg
+-rwxrwxrwx   0 chris     (1000) chris     (1000)      700 2023-03-17 01:49:42.000000 spyrograph-0.9.0/setup.py
+drwxrwxrwx   0 chris     (1000) chris     (1000)        0 2023-03-17 01:50:10.650808 spyrograph-0.9.0/spyrograph.egg-info/
+-rwxrwxrwx   0 chris     (1000) chris     (1000)     3783 2023-03-17 01:50:10.000000 spyrograph-0.9.0/spyrograph.egg-info/PKG-INFO
+-rwxrwxrwx   0 chris     (1000) chris     (1000)      162 2023-03-17 01:50:10.000000 spyrograph-0.9.0/spyrograph.egg-info/SOURCES.txt
+-rwxrwxrwx   0 chris     (1000) chris     (1000)        1 2023-03-17 01:50:10.000000 spyrograph-0.9.0/spyrograph.egg-info/dependency_links.txt
+-rwxrwxrwx   0 chris     (1000) chris     (1000)        1 2023-03-17 01:50:10.000000 spyrograph-0.9.0/spyrograph.egg-info/top_level.txt
```

### Comparing `spyrograph-0.8.0/LICENSE` & `spyrograph-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `spyrograph-0.8.0/PKG-INFO` & `spyrograph-0.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spyrograph
-Version: 0.8.0
+Version: 0.9.0
 Summary: Library for drawing spirographs in Python
 Home-page: https://github.com/chris-greening/spyrograph
 Author: Chris Greening
 Author-email: chris@christophergreening.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `spyrograph-0.8.0/README.md` & `spyrograph-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `spyrograph-0.8.0/setup.py` & `spyrograph-0.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="spyrograph",
-    version="0.8.0",
+    version="0.9.0",
     author="Chris Greening",
     author_email="chris@christophergreening.com",
     description="Library for drawing spirographs in Python",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/chris-greening/spyrograph",
     packages=[],
```

### Comparing `spyrograph-0.8.0/spyrograph.egg-info/PKG-INFO` & `spyrograph-0.9.0/spyrograph.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spyrograph
-Version: 0.8.0
+Version: 0.9.0
 Summary: Library for drawing spirographs in Python
 Home-page: https://github.com/chris-greening/spyrograph
 Author: Chris Greening
 Author-email: chris@christophergreening.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

