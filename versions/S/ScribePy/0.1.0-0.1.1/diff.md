# Comparing `tmp/ScribePy-0.1.0.tar.gz` & `tmp/ScribePy-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ScribePy-0.1.0.tar", last modified: Thu Apr  6 14:29:20 2023, max compression
+gzip compressed data, was "ScribePy-0.1.1.tar", last modified: Thu Apr  6 14:52:48 2023, max compression
```

## Comparing `ScribePy-0.1.0.tar` & `ScribePy-0.1.1.tar`

### file list

```diff
@@ -1,16 +1,19 @@
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:29:20.224113 ScribePy-0.1.0/
--rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 13:47:41.000000 ScribePy-0.1.0/LICENSE
--rw-r--r--   0 fcarva844   (501) staff       (20)      681 2023-04-06 14:29:20.223816 ScribePy-0.1.0/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)     1996 2023-04-06 14:12:48.000000 ScribePy-0.1.0/README.md
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:29:20.220727 ScribePy-0.1.0/ScribePy.egg-info/
--rw-r--r--   0 fcarva844   (501) staff       (20)      681 2023-04-06 14:29:20.000000 ScribePy-0.1.0/ScribePy.egg-info/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)      245 2023-04-06 14:29:20.000000 ScribePy-0.1.0/ScribePy.egg-info/SOURCES.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 14:29:20.000000 ScribePy-0.1.0/ScribePy.egg-info/dependency_links.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       32 2023-04-06 14:29:20.000000 ScribePy-0.1.0/ScribePy.egg-info/requires.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        9 2023-04-06 14:29:20.000000 ScribePy-0.1.0/ScribePy.egg-info/top_level.txt
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:29:20.223152 ScribePy-0.1.0/scribepy/
--rw-r--r--   0 fcarva844   (501) staff       (20)       24 2023-04-06 13:59:46.000000 ScribePy-0.1.0/scribepy/__init__.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      894 2023-04-06 13:59:36.000000 ScribePy-0.1.0/scribepy/scribepy.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      445 2023-04-06 13:59:17.000000 ScribePy-0.1.0/scribepy/utils.py
--rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 14:29:20.224970 ScribePy-0.1.0/setup.cfg
--rw-r--r--   0 fcarva844   (501) staff       (20)      868 2023-04-06 14:25:01.000000 ScribePy-0.1.0/setup.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.987203 ScribePy-0.1.1/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 13:47:41.000000 ScribePy-0.1.1/LICENSE
+-rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 14:52:48.986548 ScribePy-0.1.1/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1996 2023-04-06 14:12:48.000000 ScribePy-0.1.1/README.md
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.981059 ScribePy-0.1.1/ScribePy.egg-info/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)      283 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/SOURCES.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/dependency_links.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       32 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/requires.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        9 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/top_level.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)      868 2023-04-06 14:52:35.000000 ScribePy-0.1.1/pyproject.toml
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.982951 ScribePy-0.1.1/scribepy/
+-rw-r--r--   0 fcarva844   (501) staff       (20)       24 2023-04-06 13:59:46.000000 ScribePy-0.1.1/scribepy/__init__.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      894 2023-04-06 13:59:36.000000 ScribePy-0.1.1/scribepy/scribepy.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      445 2023-04-06 13:59:17.000000 ScribePy-0.1.1/scribepy/utils.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 14:52:48.987319 ScribePy-0.1.1/setup.cfg
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1038 2023-04-06 14:44:00.000000 ScribePy-0.1.1/setup.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.984925 ScribePy-0.1.1/tests/
+-rw-r--r--   0 fcarva844   (501) staff       (20)      359 2023-04-06 14:21:22.000000 ScribePy-0.1.1/tests/test_scribepy.py
```

### Comparing `ScribePy-0.1.0/LICENSE` & `ScribePy-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `ScribePy-0.1.0/README.md` & `ScribePy-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `ScribePy-0.1.0/scribepy/scribepy.py` & `ScribePy-0.1.1/scribepy/scribepy.py`

 * *Files identical despite different names*

### Comparing `ScribePy-0.1.0/setup.py` & `ScribePy-0.1.1/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,22 +1,27 @@
 from setuptools import setup, find_packages
 
+with open("README.md", "r") as fh:
+    long_description = fh.read()
+
 setup(
     name='ScribePy',
-    version='0.1.0',
+    version='0.1.1',
     description='Python library for generating documentation',
+    long_description=long_description,
+    long_description_content_type="text/markdown",
     url='https://github.com/hipnologo/ScribePy',
     author='Fabio Carvalho',
     author_email='hipnologo@gmail.com',
     license='Apache License, Version 2.0',
     packages=find_packages(),
     classifiers=[
-        'Development Status :: 3 - Alpha',
+        'Development Status :: 4 - Beta',
         'Intended Audience :: Developers',
-        'License :: OSI Approved :: MIT License',
+        'License :: OSI Approved :: Apache Software License',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: 3.9',
     ],
     keywords='documentation',
```

