# Comparing `tmp/Flask Boilerplate Creator-0.0.1.tar.gz` & `tmp/Flask Boilerplate Creator-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Flask Boilerplate Creator-0.0.1.tar", last modified: Fri Apr  7 04:19:42 2023, max compression
+gzip compressed data, was "Flask Boilerplate Creator-0.0.2.tar", last modified: Fri Apr  7 04:25:58 2023, max compression
```

## Comparing `Flask Boilerplate Creator-0.0.1.tar` & `Flask Boilerplate Creator-0.0.2.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 04:19:42.733989 Flask Boilerplate Creator-0.0.1/
-drwxrwxrwx   0        0        0        0 2023-04-07 04:19:42.729018 Flask Boilerplate Creator-0.0.1/Flask_Boilerplate_Creator.egg-info/
--rw-rw-rw-   0        0        0      661 2023-04-07 04:19:42.000000 Flask Boilerplate Creator-0.0.1/Flask_Boilerplate_Creator.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      298 2023-04-07 04:19:42.000000 Flask Boilerplate Creator-0.0.1/Flask_Boilerplate_Creator.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 04:19:42.000000 Flask Boilerplate Creator-0.0.1/Flask_Boilerplate_Creator.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        4 2023-04-07 04:19:42.000000 Flask Boilerplate Creator-0.0.1/Flask_Boilerplate_Creator.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1093 2023-04-07 04:02:55.000000 Flask Boilerplate Creator-0.0.1/LICENSE
--rw-rw-rw-   0        0        0      661 2023-04-07 04:19:42.733989 Flask Boilerplate Creator-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0     1104 2023-04-07 04:10:50.000000 Flask Boilerplate Creator-0.0.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 04:19:42.731995 Flask Boilerplate Creator-0.0.1/flask-boilerplate-creator/
--rw-rw-rw-   0        0        0     8764 2023-04-07 04:12:30.000000 Flask Boilerplate Creator-0.0.1/flask-boilerplate-creator/__init__.py
--rw-rw-rw-   0        0        0       59 2023-04-07 02:54:15.000000 Flask Boilerplate Creator-0.0.1/flask-boilerplate-creator/__main__.py
--rw-rw-rw-   0        0        0       42 2023-04-07 04:19:42.733989 Flask Boilerplate Creator-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      799 2023-04-07 03:47:58.000000 Flask Boilerplate Creator-0.0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 04:25:58.299695 Flask Boilerplate Creator-0.0.2/
+drwxrwxrwx   0        0        0        0 2023-04-07 04:25:58.278428 Flask Boilerplate Creator-0.0.2/Flask_Boilerplate_Creator.egg-info/
+-rw-rw-rw-   0        0        0     1876 2023-04-07 04:25:58.000000 Flask Boilerplate Creator-0.0.2/Flask_Boilerplate_Creator.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      298 2023-04-07 04:25:58.000000 Flask Boilerplate Creator-0.0.2/Flask_Boilerplate_Creator.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 04:25:58.000000 Flask Boilerplate Creator-0.0.2/Flask_Boilerplate_Creator.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        4 2023-04-07 04:25:58.000000 Flask Boilerplate Creator-0.0.2/Flask_Boilerplate_Creator.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1093 2023-04-07 04:02:55.000000 Flask Boilerplate Creator-0.0.2/LICENSE
+-rw-rw-rw-   0        0        0     1876 2023-04-07 04:25:58.292587 Flask Boilerplate Creator-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0     1181 2023-04-07 04:25:06.000000 Flask Boilerplate Creator-0.0.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 04:25:58.289595 Flask Boilerplate Creator-0.0.2/flask-boilerplate-creator/
+-rw-rw-rw-   0        0        0     8764 2023-04-07 04:24:30.000000 Flask Boilerplate Creator-0.0.2/flask-boilerplate-creator/__init__.py
+-rw-rw-rw-   0        0        0       59 2023-04-07 02:54:15.000000 Flask Boilerplate Creator-0.0.2/flask-boilerplate-creator/__main__.py
+-rw-rw-rw-   0        0        0       42 2023-04-07 04:25:58.300704 Flask Boilerplate Creator-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      903 2023-04-07 04:24:22.000000 Flask Boilerplate Creator-0.0.2/setup.py
```

### Comparing `Flask Boilerplate Creator-0.0.1/LICENSE` & `Flask Boilerplate Creator-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `Flask Boilerplate Creator-0.0.1/README.md` & `Flask Boilerplate Creator-0.0.2/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,16 @@
 # Flask Boilerplate Creator
 Create boilerplate for flask web application
 
+Install using pip
+
+```cmd
+> pip install Flask-Boilerplate-Creator
+```
+
 run the Flask-Boilerplate-Creator
 
 ```cmd
 > python -m fbc
 ```
 
 After running above command it will ask for other modules to be installed, if not leave it blank
```

### Comparing `Flask Boilerplate Creator-0.0.1/flask-boilerplate-creator/__init__.py` & `Flask Boilerplate Creator-0.0.2/flask-boilerplate-creator/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 """
 Generate boilerplate structure for flask web app
 
 author: Harkishan Khuva <harkishankhuva.pythonanywhere.com>
 created date: 07/04/2023 IST
-version: 0.0.1
+version: 0.0.2
 """
 
 # :: IMPORTS
 import os
 import sys
 import shutil
 import typing
```

### Comparing `Flask Boilerplate Creator-0.0.1/setup.py` & `Flask Boilerplate Creator-0.0.2/setup.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup
 
 setup(
     name="Flask Boilerplate Creator",
-    version="0.0.1",
+    version="0.0.2",
     description="Create boilerplate structure of flask web application",
     author="Harkishan Khuva",
     author_email="hakitechy@gmail.com",
     license="MIT",
     keywords=["fbc", "flask-boilerplate-creator", "flask boilerplate creator"],
     packages=["fbc"],
     package_dir={
@@ -16,9 +16,11 @@
         "Environment :: Web Environment",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     url="https://github.com/hakiKhuva/flask-boilerplate-creator",
-    python_requires=">=3.8"
+    python_requires=">=3.8",
+    long_description=open("README.md","r").read(),
+    long_description_content_type="text/markdown"
 )
```

