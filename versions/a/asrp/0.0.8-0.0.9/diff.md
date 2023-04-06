# Comparing `tmp/asrp-0.0.8.tar.gz` & `tmp/asrp-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/asrp-0.0.8.tar", last modified: Fri Aug 27 07:47:15 2021, max compression
+gzip compressed data, was "dist/asrp-0.0.9.tar", last modified: Mon Nov  1 14:12:30 2021, max compression
```

## Comparing `asrp-0.0.8.tar` & `asrp-0.0.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-08-27 07:47:15.000000 asrp-0.0.8/
--rw-r--r--   0 voidful    (501) staff       (20)     4156 2021-05-06 05:19:19.000000 asrp-0.0.8/.gitignore
--rw-r--r--   0 voidful    (501) staff       (20)    11357 2021-05-06 05:02:16.000000 asrp-0.0.8/LICENSE
--rw-r--r--   0 voidful    (501) staff       (20)     1441 2021-08-27 07:47:15.000000 asrp-0.0.8/PKG-INFO
--rw-r--r--   0 voidful    (501) staff       (20)     1017 2021-07-12 06:34:11.000000 asrp-0.0.8/README.md
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp/
--rw-r--r--   0 voidful    (501) staff       (20)      103 2021-07-12 06:32:31.000000 asrp-0.0.8/asrp/__init__.py
--rw-r--r--   0 voidful    (501) staff       (20)     1937 2021-07-18 07:28:43.000000 asrp-0.0.8/asrp/eval.py
--rw-r--r--   0 voidful    (501) staff       (20)     1853 2021-08-27 07:45:32.000000 asrp-0.0.8/asrp/hubert.py
--rw-r--r--   0 voidful    (501) staff       (20)    23797 2021-05-05 03:14:03.000000 asrp-0.0.8/asrp/preprocessing.py
--rw-r--r--   0 voidful    (501) staff       (20)     4015 2021-07-17 15:02:17.000000 asrp-0.0.8/asrp/test.py
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/
--rw-r--r--   0 voidful    (501) staff       (20)     1441 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/PKG-INFO
--rw-r--r--   0 voidful    (501) staff       (20)      300 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/SOURCES.txt
--rw-r--r--   0 voidful    (501) staff       (20)        1 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/dependency_links.txt
--rw-r--r--   0 voidful    (501) staff       (20)        1 2021-05-18 08:30:31.000000 asrp-0.0.8/asrp.egg-info/not-zip-safe
--rw-r--r--   0 voidful    (501) staff       (20)       52 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/requires.txt
--rw-r--r--   0 voidful    (501) staff       (20)        5 2021-08-27 07:47:15.000000 asrp-0.0.8/asrp.egg-info/top_level.txt
--rw-r--r--   0 voidful    (501) staff       (20)       51 2021-07-17 15:00:53.000000 asrp-0.0.8/requirements.txt
--rw-r--r--   0 voidful    (501) staff       (20)       38 2021-08-27 07:47:15.000000 asrp-0.0.8/setup.cfg
--rw-r--r--   0 voidful    (501) staff       (20)      742 2021-08-27 07:47:04.000000 asrp-0.0.8/setup.py
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-11-01 14:12:30.000000 asrp-0.0.9/
+-rw-r--r--   0 voidful    (501) staff       (20)     4156 2021-05-06 05:19:19.000000 asrp-0.0.9/.gitignore
+-rw-r--r--   0 voidful    (501) staff       (20)    11357 2021-05-06 05:02:16.000000 asrp-0.0.9/LICENSE
+-rw-r--r--   0 voidful    (501) staff       (20)     1441 2021-11-01 14:12:30.000000 asrp-0.0.9/PKG-INFO
+-rw-r--r--   0 voidful    (501) staff       (20)     1017 2021-07-12 06:34:11.000000 asrp-0.0.9/README.md
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp/
+-rw-r--r--   0 voidful    (501) staff       (20)      113 2021-11-01 14:12:17.000000 asrp-0.0.9/asrp/__init__.py
+-rw-r--r--   0 voidful    (501) staff       (20)     1937 2021-07-18 07:28:43.000000 asrp-0.0.9/asrp/eval.py
+-rw-r--r--   0 voidful    (501) staff       (20)     1853 2021-08-28 07:25:59.000000 asrp-0.0.9/asrp/hubert.py
+-rw-r--r--   0 voidful    (501) staff       (20)    23797 2021-05-05 03:14:03.000000 asrp-0.0.9/asrp/preprocessing.py
+-rw-r--r--   0 voidful    (501) staff       (20)     4015 2021-07-17 15:02:17.000000 asrp-0.0.9/asrp/test.py
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/
+-rw-r--r--   0 voidful    (501) staff       (20)     1441 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/PKG-INFO
+-rw-r--r--   0 voidful    (501) staff       (20)      300 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/SOURCES.txt
+-rw-r--r--   0 voidful    (501) staff       (20)        1 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/dependency_links.txt
+-rw-r--r--   0 voidful    (501) staff       (20)        1 2021-05-18 08:30:31.000000 asrp-0.0.9/asrp.egg-info/not-zip-safe
+-rw-r--r--   0 voidful    (501) staff       (20)       52 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/requires.txt
+-rw-r--r--   0 voidful    (501) staff       (20)        5 2021-11-01 14:12:30.000000 asrp-0.0.9/asrp.egg-info/top_level.txt
+-rw-r--r--   0 voidful    (501) staff       (20)       51 2021-07-17 15:00:53.000000 asrp-0.0.9/requirements.txt
+-rw-r--r--   0 voidful    (501) staff       (20)       38 2021-11-01 14:12:30.000000 asrp-0.0.9/setup.cfg
+-rw-r--r--   0 voidful    (501) staff       (20)      742 2021-11-01 14:12:23.000000 asrp-0.0.9/setup.py
```

### Comparing `asrp-0.0.8/.gitignore` & `asrp-0.0.9/.gitignore`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/LICENSE` & `asrp-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/PKG-INFO` & `asrp-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: asrp
-Version: 0.0.8
+Version: 0.0.9
 Summary: UNKNOWN
 Home-page: https://github.com/voidful/asrp
 Author: Voidful
 Author-email: voidful.stack@gmail.com
 License: Apache
 Keywords: asr
 Platform: UNKNOWN
```

### Comparing `asrp-0.0.8/README.md` & `asrp-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/asrp/eval.py` & `asrp-0.0.9/asrp/eval.py`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/asrp/hubert.py` & `asrp-0.0.9/asrp/hubert.py`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/asrp/preprocessing.py` & `asrp-0.0.9/asrp/preprocessing.py`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/asrp/test.py` & `asrp-0.0.9/asrp/test.py`

 * *Files identical despite different names*

### Comparing `asrp-0.0.8/asrp.egg-info/PKG-INFO` & `asrp-0.0.9/asrp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: asrp
-Version: 0.0.8
+Version: 0.0.9
 Summary: UNKNOWN
 Home-page: https://github.com/voidful/asrp
 Author: Voidful
 Author-email: voidful.stack@gmail.com
 License: Apache
 Keywords: asr
 Platform: UNKNOWN
```

### Comparing `asrp-0.0.8/setup.py` & `asrp-0.0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open('requirements.txt') as f:
     required = f.read().splitlines()
 
 setup(
     name='asrp',
-    version='0.0.8',
+    version='0.0.9',
     description='',
     url='https://github.com/voidful/asrp',
     author='Voidful',
     author_email='voidful.stack@gmail.com',
     long_description=open("README.md", encoding="utf8").read(),
     long_description_content_type="text/markdown",
     setup_requires=['setuptools-git'],
```

