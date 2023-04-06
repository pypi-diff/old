# Comparing `tmp/jianglab-0.1.tar.gz` & `tmp/jianglab-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jianglab-0.1.tar", last modified: Thu Apr  6 20:48:43 2023, max compression
+gzip compressed data, was "jianglab-0.1.1.tar", last modified: Thu Apr  6 21:41:53 2023, max compression
```

## Comparing `jianglab-0.1.tar` & `jianglab-0.1.1.tar`

### file list

```diff
@@ -1,10 +1,11 @@
-drwxr-xr-x   0 zhengjiang   (501) staff       (20)        0 2023-04-06 20:48:43.383643 jianglab-0.1/
--rw-r--r--   0 zhengjiang   (501) staff       (20)      544 2023-04-06 20:48:43.383308 jianglab-0.1/PKG-INFO
-drwxr-xr-x   0 zhengjiang   (501) staff       (20)        0 2023-04-06 20:48:43.382860 jianglab-0.1/jianglab.egg-info/
--rw-r--r--   0 zhengjiang   (501) staff       (20)      544 2023-04-06 20:48:43.000000 jianglab-0.1/jianglab.egg-info/PKG-INFO
--rw-r--r--   0 zhengjiang   (501) staff       (20)      167 2023-04-06 20:48:43.000000 jianglab-0.1/jianglab.egg-info/SOURCES.txt
--rw-r--r--   0 zhengjiang   (501) staff       (20)        1 2023-04-06 20:48:43.000000 jianglab-0.1/jianglab.egg-info/dependency_links.txt
--rw-r--r--   0 zhengjiang   (501) staff       (20)       24 2023-04-06 20:48:43.000000 jianglab-0.1/jianglab.egg-info/requires.txt
--rw-r--r--   0 zhengjiang   (501) staff       (20)        1 2023-04-06 20:48:43.000000 jianglab-0.1/jianglab.egg-info/top_level.txt
--rw-r--r--   0 zhengjiang   (501) staff       (20)       38 2023-04-06 20:48:43.383771 jianglab-0.1/setup.cfg
--rw-r--r--   0 zhengjiang   (501) staff       (20)      754 2023-04-06 20:48:15.000000 jianglab-0.1/setup.py
+drwxr-xr-x   0 zhengjiang   (501) staff       (20)        0 2023-04-06 21:41:53.129237 jianglab-0.1.1/
+-rw-r--r--   0 zhengjiang   (501) staff       (20)      542 2023-04-06 21:41:53.128909 jianglab-0.1.1/PKG-INFO
+-rw-r--r--   0 zhengjiang   (501) staff       (20)        0 2023-04-06 20:59:21.000000 jianglab-0.1.1/README.md
+drwxr-xr-x   0 zhengjiang   (501) staff       (20)        0 2023-04-06 21:41:53.128389 jianglab-0.1.1/jianglab.egg-info/
+-rw-r--r--   0 zhengjiang   (501) staff       (20)      542 2023-04-06 21:41:53.000000 jianglab-0.1.1/jianglab.egg-info/PKG-INFO
+-rw-r--r--   0 zhengjiang   (501) staff       (20)      177 2023-04-06 21:41:53.000000 jianglab-0.1.1/jianglab.egg-info/SOURCES.txt
+-rw-r--r--   0 zhengjiang   (501) staff       (20)        1 2023-04-06 21:41:53.000000 jianglab-0.1.1/jianglab.egg-info/dependency_links.txt
+-rw-r--r--   0 zhengjiang   (501) staff       (20)       24 2023-04-06 21:41:53.000000 jianglab-0.1.1/jianglab.egg-info/requires.txt
+-rw-r--r--   0 zhengjiang   (501) staff       (20)        1 2023-04-06 21:41:53.000000 jianglab-0.1.1/jianglab.egg-info/top_level.txt
+-rw-r--r--   0 zhengjiang   (501) staff       (20)       38 2023-04-06 21:41:53.129366 jianglab-0.1.1/setup.cfg
+-rw-r--r--   0 zhengjiang   (501) staff       (20)      752 2023-04-06 21:40:55.000000 jianglab-0.1.1/setup.py
```

### Comparing `jianglab-0.1/setup.py` & `jianglab-0.1.1/setup.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 from setuptools import setup, find_packages
 
 setup(
     name='jianglab',
-    version='0.1',
+    version='0.1.1',
     packages=find_packages(),
     install_requires=[
         "numpy",
         "pandas",
         "matplotlib",
     ],
     author = "Jiang Zheng",
     author_email = "zjiang314@gmail.com",
     description = "A package for Jiang lab",
-    url = "https://github.com/jiang_lab_retina/common_functions",
+    url = "https://github.com/jiang-lab-retina/jianglab.git",
     classifiers=[
         "Development Status :: 3 - Alpha",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
```

