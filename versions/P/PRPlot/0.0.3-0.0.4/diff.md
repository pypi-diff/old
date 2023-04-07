# Comparing `tmp/PRPlot-0.0.3.tar.gz` & `tmp/PRPlot-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PRPlot-0.0.3.tar", last modified: Fri Apr  7 01:19:02 2023, max compression
+gzip compressed data, was "PRPlot-0.0.4.tar", last modified: Fri Apr  7 01:28:46 2023, max compression
```

## Comparing `PRPlot-0.0.3.tar` & `PRPlot-0.0.4.tar`

### file list

```diff
@@ -1,15 +1,14 @@
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:19:02.250907 PRPlot-0.0.3/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)    35149 2023-04-06 20:40:07.000000 PRPlot-0.0.3/LICENSE
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 01:19:02.250907 PRPlot-0.0.3/PKG-INFO
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:19:02.226906 PRPlot-0.0.3/PRPlot/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     2432 2023-04-07 00:43:42.000000 PRPlot-0.0.3/PRPlot/PRPlot.py
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      115 2023-04-07 01:18:31.000000 PRPlot-0.0.3/PRPlot/__init__.py
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:19:02.246907 PRPlot-0.0.3/PRPlot.egg-info/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 01:19:01.000000 PRPlot-0.0.3/PRPlot.egg-info/PKG-INFO
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      221 2023-04-07 01:19:01.000000 PRPlot-0.0.3/PRPlot.egg-info/SOURCES.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        1 2023-04-07 01:19:01.000000 PRPlot-0.0.3/PRPlot.egg-info/dependency_links.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)       29 2023-04-07 01:19:01.000000 PRPlot-0.0.3/PRPlot.egg-info/requires.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        7 2023-04-07 01:19:01.000000 PRPlot-0.0.3/PRPlot.egg-info/top_level.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        8 2023-04-06 20:40:07.000000 PRPlot-0.0.3/README.md
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)       38 2023-04-07 01:19:02.258907 PRPlot-0.0.3/setup.cfg
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1589 2023-04-07 01:17:54.000000 PRPlot-0.0.3/setup.py
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:28:46.122260 PRPlot-0.0.4/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)    35149 2023-04-06 20:40:07.000000 PRPlot-0.0.4/LICENSE
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 01:28:46.122260 PRPlot-0.0.4/PKG-INFO
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:28:46.094260 PRPlot-0.0.4/PRPlot/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     2432 2023-04-07 00:43:42.000000 PRPlot-0.0.4/PRPlot/PRPlot.py
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      115 2023-04-07 01:28:17.000000 PRPlot-0.0.4/PRPlot/__init__.py
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 01:28:46.122260 PRPlot-0.0.4/PRPlot.egg-info/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 01:28:45.000000 PRPlot-0.0.4/PRPlot.egg-info/PKG-INFO
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      192 2023-04-07 01:28:45.000000 PRPlot-0.0.4/PRPlot.egg-info/SOURCES.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        1 2023-04-07 01:28:45.000000 PRPlot-0.0.4/PRPlot.egg-info/dependency_links.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        7 2023-04-07 01:28:45.000000 PRPlot-0.0.4/PRPlot.egg-info/top_level.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        8 2023-04-06 20:40:07.000000 PRPlot-0.0.4/README.md
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)       38 2023-04-07 01:28:46.134260 PRPlot-0.0.4/setup.cfg
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1557 2023-04-07 01:28:07.000000 PRPlot-0.0.4/setup.py
```

### Comparing `PRPlot-0.0.3/LICENSE` & `PRPlot-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `PRPlot-0.0.3/PKG-INFO` & `PRPlot-0.0.4/PKG-INFO`

 * *Files 25% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: PRPlot
-Version: 0.0.3
+Version: 0.0.4
 Summary: It is a Python library for build a very nice predict-reference plots. It is an extension of the matplotlib library
 Home-page: https://github.com/89605502155/PRPlot
 Author: Andrey Ferubko
 Author-email: ferubko1999@yandex.ru
 License: GNU General Public License v3.0
-Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.3.zip
+Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.4.zip
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `PRPlot-0.0.3/PRPlot/PRPlot.py` & `PRPlot-0.0.4/PRPlot/PRPlot.py`

 * *Files identical despite different names*

### Comparing `PRPlot-0.0.3/PRPlot.egg-info/PKG-INFO` & `PRPlot-0.0.4/PRPlot.egg-info/PKG-INFO`

 * *Files 25% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: PRPlot
-Version: 0.0.3
+Version: 0.0.4
 Summary: It is a Python library for build a very nice predict-reference plots. It is an extension of the matplotlib library
 Home-page: https://github.com/89605502155/PRPlot
 Author: Andrey Ferubko
 Author-email: ferubko1999@yandex.ru
 License: GNU General Public License v3.0
-Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.3.zip
+Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.4.zip
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `PRPlot-0.0.3/setup.py` & `PRPlot-0.0.4/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from io import open
 from setuptools import setup
 
 
-version = '0.0.3'
+version = '0.0.4'
 
 with open('README.md', encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='PRPlot',
     version=version,
@@ -25,15 +25,15 @@
         version
     ),
     # download_url='https://github.com/89605502155/PRPlot/archive/main.zip',
 
     license='GNU General Public License v3.0',
 
     packages=['PRPlot'],
-    install_requires=['matplotlib.pyplot', 'matplotlib'],
+    #install_requires=[],
 
     classifiers=[
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Operating System :: OS Independent',
         'Intended Audience :: End Users/Desktop',
         'Intended Audience :: Developers',
         'Programming Language :: Python',
```

