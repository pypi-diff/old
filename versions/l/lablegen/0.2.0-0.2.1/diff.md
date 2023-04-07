# Comparing `tmp/lablegen-0.2.0.tar.gz` & `tmp/lablegen-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lablegen-0.2.0.tar", last modified: Fri Apr  7 03:21:38 2023, max compression
+gzip compressed data, was "lablegen-0.2.1.tar", last modified: Fri Apr  7 03:28:01 2023, max compression
```

## Comparing `lablegen-0.2.0.tar` & `lablegen-0.2.1.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 03:21:38.880990 lablegen-0.2.0/
--rw-rw-rw-   0        0        0    35149 2023-04-07 03:06:15.000000 lablegen-0.2.0/COPYING
--rw-rw-rw-   0        0        0      433 2023-04-07 03:21:38.880990 lablegen-0.2.0/PKG-INFO
--rw-rw-rw-   0        0        0       56 2023-04-07 03:06:15.000000 lablegen-0.2.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 03:21:38.879989 lablegen-0.2.0/lablegen.egg-info/
--rw-rw-rw-   0        0        0      433 2023-04-07 03:21:38.000000 lablegen-0.2.0/lablegen.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      197 2023-04-07 03:21:38.000000 lablegen-0.2.0/lablegen.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 03:21:38.000000 lablegen-0.2.0/lablegen.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       16 2023-04-07 03:21:38.000000 lablegen-0.2.0/lablegen.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-07 03:21:38.000000 lablegen-0.2.0/lablegen.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      858 2023-04-07 03:20:16.000000 lablegen-0.2.0/lablegen.py
--rw-rw-rw-   0        0        0       42 2023-04-07 03:21:38.880990 lablegen-0.2.0/setup.cfg
--rw-rw-rw-   0        0        0      674 2023-04-07 03:14:58.000000 lablegen-0.2.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 03:28:01.966413 lablegen-0.2.1/
+-rw-rw-rw-   0        0        0    35149 2023-04-07 03:06:15.000000 lablegen-0.2.1/COPYING
+-rw-rw-rw-   0        0        0      534 2023-04-07 03:28:01.965885 lablegen-0.2.1/PKG-INFO
+-rw-rw-rw-   0        0        0       56 2023-04-07 03:06:15.000000 lablegen-0.2.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 03:28:01.964858 lablegen-0.2.1/lablegen.egg-info/
+-rw-rw-rw-   0        0        0      534 2023-04-07 03:28:01.000000 lablegen-0.2.1/lablegen.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      197 2023-04-07 03:28:01.000000 lablegen-0.2.1/lablegen.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 03:28:01.000000 lablegen-0.2.1/lablegen.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       16 2023-04-07 03:28:01.000000 lablegen-0.2.1/lablegen.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 03:28:01.000000 lablegen-0.2.1/lablegen.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      801 2023-04-07 03:27:30.000000 lablegen-0.2.1/lablegen.py
+-rw-rw-rw-   0        0        0       42 2023-04-07 03:28:01.966413 lablegen-0.2.1/setup.cfg
+-rw-rw-rw-   0        0        0      869 2023-04-07 03:27:27.000000 lablegen-0.2.1/setup.py
```

### Comparing `lablegen-0.2.0/COPYING` & `lablegen-0.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `lablegen-0.2.0/lablegen.py` & `lablegen-0.2.1/lablegen.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,12 +1,7 @@
-__version__ = "0.2.0"
-__author__ = "Social Mean"
-
-
-
 import pyperclip
 
 def table_generator(dic, clip=False):
     col_count = len(dic)
     row_count = len(dic[list(dic.keys())[0]])
     
     latex_table_str = """\\begin{table}[H]
```

### Comparing `lablegen-0.2.0/setup.py` & `lablegen-0.2.1/setup.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,15 +1,25 @@
+__version__ = "0.2.1"
+__author__ = "Social Mean"
+
+
 from setuptools import setup, find_packages
 import lablegen
+
+with open("README.md", "r") as f:
+  long_description = f.read()
+
 setup(
 	name="lablegen",
-	version=lablegen.__version__,
+	version=__version__,
 	description="Generate LaTeX format table from array data.",
+	long_description=long_description,
+  	long_description_content_type="text/markdown",
 	url="https://github.com/Social-Mean/LableGen",
-	author=lablegen.__author__,
+	author=__author__,
 	author_email="Social_Mean@126.com",
 	license='GNU 3.0',
 	py_modules = [ 'lablegen' ],
 	scripts=['lablegen.py'],
   	classifiers=[
 	  "Programming Language :: Python :: 3",
 	  "License :: OSI Approved :: GNU Affero General Public License v3",
```

