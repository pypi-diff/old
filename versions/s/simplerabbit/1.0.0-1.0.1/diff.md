# Comparing `tmp/simplerabbit-1.0.0.tar.gz` & `tmp/simplerabbit-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "simplerabbit-1.0.0.tar", last modified: Fri Apr  7 03:02:49 2023, max compression
+gzip compressed data, was "simplerabbit-1.0.1.tar", last modified: Fri Apr  7 03:08:10 2023, max compression
```

## Comparing `simplerabbit-1.0.0.tar` & `simplerabbit-1.0.1.tar`

### file list

```diff
@@ -1,11 +1,11 @@
-drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 03:02:49.210728 simplerabbit-1.0.0/
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      430 2023-04-07 03:02:49.210728 simplerabbit-1.0.0/PKG-INFO
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)     1100 2023-04-06 03:29:42.000000 simplerabbit-1.0.0/README.md
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       38 2023-04-07 03:02:49.210728 simplerabbit-1.0.0/setup.cfg
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      533 2023-04-07 03:02:20.000000 simplerabbit-1.0.0/setup.py
-drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 03:02:49.210728 simplerabbit-1.0.0/simplerabbit.egg-info/
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      430 2023-04-07 03:02:49.000000 simplerabbit-1.0.0/simplerabbit.egg-info/PKG-INFO
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      197 2023-04-07 03:02:49.000000 simplerabbit-1.0.0/simplerabbit.egg-info/SOURCES.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 03:02:49.000000 simplerabbit-1.0.0/simplerabbit.egg-info/dependency_links.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       12 2023-04-07 03:02:49.000000 simplerabbit-1.0.0/simplerabbit.egg-info/requires.txt
--rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 03:02:49.000000 simplerabbit-1.0.0/simplerabbit.egg-info/top_level.txt
+drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 03:08:10.953737 simplerabbit-1.0.1/
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      430 2023-04-07 03:08:10.953737 simplerabbit-1.0.1/PKG-INFO
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)     1100 2023-04-06 03:29:42.000000 simplerabbit-1.0.1/README.md
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       38 2023-04-07 03:08:10.953737 simplerabbit-1.0.1/setup.cfg
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      533 2023-04-07 03:07:43.000000 simplerabbit-1.0.1/setup.py
+drwxrwxr-x   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        0 2023-04-07 03:08:10.953737 simplerabbit-1.0.1/simplerabbit.egg-info/
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      430 2023-04-07 03:08:10.000000 simplerabbit-1.0.1/simplerabbit.egg-info/PKG-INFO
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)      197 2023-04-07 03:08:10.000000 simplerabbit-1.0.1/simplerabbit.egg-info/SOURCES.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 03:08:10.000000 simplerabbit-1.0.1/simplerabbit.egg-info/dependency_links.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)       12 2023-04-07 03:08:10.000000 simplerabbit-1.0.1/simplerabbit.egg-info/requires.txt
+-rw-rw-r--   0 AATSTestAdmin  (1000) AATSTestAdmin  (1000)        1 2023-04-07 03:08:10.000000 simplerabbit-1.0.1/simplerabbit.egg-info/top_level.txt
```

### Comparing `simplerabbit-1.0.0/README.md` & `simplerabbit-1.0.1/README.md`

 * *Files identical despite different names*

### Comparing `simplerabbit-1.0.0/setup.py` & `simplerabbit-1.0.1/setup.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name='simplerabbit',
-    version='1.0.0',
+    version='1.0.1',
     author='Phuong Do',
     author_email='phdo@energidanmark.dk',
     description='A Python library for sending and receiving messages using RabbitMQ',
     packages=find_packages(),
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
```

