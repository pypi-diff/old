# Comparing `tmp/qluster-0.0.3.tar.gz` & `tmp/qluster-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "qluster-0.0.3.tar", last modified: Wed Mar 22 14:51:18 2023, max compression
+gzip compressed data, was "qluster-0.0.4.tar", last modified: Fri Apr  7 00:28:23 2023, max compression
```

## Comparing `qluster-0.0.3.tar` & `qluster-0.0.4.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-03-22 14:51:18.183053 qluster-0.0.3/
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)     1070 2023-02-23 15:50:36.000000 qluster-0.0.3/LICENSE
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      327 2023-03-22 14:51:18.183053 qluster-0.0.3/PKG-INFO
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)       57 2023-02-23 15:54:08.000000 qluster-0.0.3/README.md
-drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-03-22 14:51:18.183053 qluster-0.0.3/qluster/
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)     4806 2023-03-22 14:49:46.000000 qluster-0.0.3/qluster/__init__.py
-drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-03-22 14:51:18.183053 qluster-0.0.3/qluster.egg-info/
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      327 2023-03-22 14:51:18.000000 qluster-0.0.3/qluster.egg-info/PKG-INFO
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      200 2023-03-22 14:51:18.000000 qluster-0.0.3/qluster.egg-info/SOURCES.txt
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)        1 2023-03-22 14:51:18.000000 qluster-0.0.3/qluster.egg-info/dependency_links.txt
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)       40 2023-03-22 14:51:18.000000 qluster-0.0.3/qluster.egg-info/requires.txt
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)        8 2023-03-22 14:51:18.000000 qluster-0.0.3/qluster.egg-info/top_level.txt
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)       38 2023-03-22 14:51:18.183053 qluster-0.0.3/setup.cfg
--rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      640 2023-03-22 14:50:24.000000 qluster-0.0.3/setup.py
+drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-04-07 00:28:23.552783 qluster-0.0.4/
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)     1070 2023-02-23 15:50:36.000000 qluster-0.0.4/LICENSE
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      528 2023-04-07 00:28:23.548783 qluster-0.0.4/PKG-INFO
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      258 2023-04-07 00:27:06.000000 qluster-0.0.4/README.md
+drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-04-07 00:28:23.548783 qluster-0.0.4/qluster/
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)     4806 2023-03-22 14:49:46.000000 qluster-0.0.4/qluster/__init__.py
+drwxr-xr-x   0 mdm988   (1344792526) domain users (1344200513)        0 2023-04-07 00:28:23.548783 qluster-0.0.4/qluster.egg-info/
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      528 2023-04-07 00:28:23.000000 qluster-0.0.4/qluster.egg-info/PKG-INFO
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      200 2023-04-07 00:28:23.000000 qluster-0.0.4/qluster.egg-info/SOURCES.txt
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)        1 2023-04-07 00:28:23.000000 qluster-0.0.4/qluster.egg-info/dependency_links.txt
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)       40 2023-04-07 00:28:23.000000 qluster-0.0.4/qluster.egg-info/requires.txt
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)        8 2023-04-07 00:28:23.000000 qluster-0.0.4/qluster.egg-info/top_level.txt
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)       38 2023-04-07 00:28:23.552783 qluster-0.0.4/setup.cfg
+-rw-r--r--   0 mdm988   (1344792526) domain users (1344200513)      640 2023-04-07 00:27:20.000000 qluster-0.0.4/setup.py
```

### Comparing `qluster-0.0.3/LICENSE` & `qluster-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `qluster-0.0.3/qluster/__init__.py` & `qluster-0.0.4/qluster/__init__.py`

 * *Files identical despite different names*

### Comparing `qluster-0.0.3/setup.py` & `qluster-0.0.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from setuptools import setup, find_packages
 
 name = 'qluster'
-version = '0.0.3'
+version = '0.0.4'
 
 with open('README.md' ,'r') as f:
     long_description = f.read().strip()
 
 setup(
     name=name,
     version=version,
```

