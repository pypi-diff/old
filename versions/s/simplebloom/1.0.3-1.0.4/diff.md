# Comparing `tmp/simplebloom-1.0.3.tar.gz` & `tmp/simplebloom-1.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "simplebloom-1.0.3.tar", last modified: Mon Oct 11 11:20:37 2021, max compression
+gzip compressed data, was "simplebloom-1.0.4.tar", last modified: Thu Apr  6 18:27:13 2023, max compression
```

## Comparing `simplebloom-1.0.3.tar` & `simplebloom-1.0.4.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-10-11 11:20:37.343664 simplebloom-1.0.3/
--rw-rw-rw-   0 root         (0) root         (0)     1138 2021-10-11 11:20:35.000000 simplebloom-1.0.3/LICENSE
--rw-rw-rw-   0 root         (0) root         (0)       70 2021-10-11 11:20:35.000000 simplebloom-1.0.3/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     4432 2021-10-11 11:20:37.342664 simplebloom-1.0.3/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     3551 2021-10-11 11:20:35.000000 simplebloom-1.0.3/README.rst
--rw-rw-rw-   0 root         (0) root         (0)      117 2021-10-11 11:20:35.000000 simplebloom-1.0.3/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2021-10-11 11:20:37.343664 simplebloom-1.0.3/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     4102 2021-10-11 11:20:35.000000 simplebloom-1.0.3/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-10-11 11:20:37.340664 simplebloom-1.0.3/simplebloom/
--rw-rw-rw-   0 root         (0) root         (0)       96 2021-10-11 11:20:35.000000 simplebloom-1.0.3/simplebloom/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      401 2021-10-11 11:20:35.000000 simplebloom-1.0.3/simplebloom/_bswap.h
--rw-rw-rw-   0 root         (0) root         (0)   176152 2021-10-11 11:20:35.000000 simplebloom-1.0.3/simplebloom/_cbloom.c
--rw-rw-rw-   0 root         (0) root         (0)     1290 2021-10-11 11:20:35.000000 simplebloom-1.0.3/simplebloom/_pybloom.py
--rw-rw-rw-   0 root         (0) root         (0)     5098 2021-10-11 11:20:35.000000 simplebloom-1.0.3/simplebloom/bloom.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-10-11 11:20:37.342664 simplebloom-1.0.3/simplebloom.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4432 2021-10-11 11:20:37.000000 simplebloom-1.0.3/simplebloom.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      340 2021-10-11 11:20:37.000000 simplebloom-1.0.3/simplebloom.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-10-11 11:20:37.000000 simplebloom-1.0.3/simplebloom.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-10-11 11:20:37.000000 simplebloom-1.0.3/simplebloom.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)       12 2021-10-11 11:20:37.000000 simplebloom-1.0.3/simplebloom.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:27:13.920073 simplebloom-1.0.4/
+-rw-rw-rw-   0 root         (0) root         (0)     1138 2023-04-06 18:27:09.000000 simplebloom-1.0.4/LICENSE
+-rw-rw-rw-   0 root         (0) root         (0)       70 2023-04-06 18:27:09.000000 simplebloom-1.0.4/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     4393 2023-04-06 18:27:13.920073 simplebloom-1.0.4/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     3551 2023-04-06 18:27:09.000000 simplebloom-1.0.4/README.rst
+-rw-rw-rw-   0 root         (0) root         (0)      117 2023-04-06 18:27:09.000000 simplebloom-1.0.4/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 18:27:13.920073 simplebloom-1.0.4/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     4102 2023-04-06 18:27:09.000000 simplebloom-1.0.4/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:27:13.918073 simplebloom-1.0.4/simplebloom/
+-rw-rw-rw-   0 root         (0) root         (0)       96 2023-04-06 18:27:09.000000 simplebloom-1.0.4/simplebloom/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      401 2023-04-06 18:27:09.000000 simplebloom-1.0.4/simplebloom/_bswap.h
+-rw-rw-rw-   0 root         (0) root         (0)   176152 2023-04-06 18:27:09.000000 simplebloom-1.0.4/simplebloom/_cbloom.c
+-rw-rw-rw-   0 root         (0) root         (0)     1290 2023-04-06 18:27:09.000000 simplebloom-1.0.4/simplebloom/_pybloom.py
+-rw-rw-rw-   0 root         (0) root         (0)     5098 2023-04-06 18:27:09.000000 simplebloom-1.0.4/simplebloom/bloom.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:27:13.919073 simplebloom-1.0.4/simplebloom.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4393 2023-04-06 18:27:13.000000 simplebloom-1.0.4/simplebloom.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      340 2023-04-06 18:27:13.000000 simplebloom-1.0.4/simplebloom.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 18:27:13.000000 simplebloom-1.0.4/simplebloom.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 18:27:13.000000 simplebloom-1.0.4/simplebloom.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       12 2023-04-06 18:27:13.000000 simplebloom-1.0.4/simplebloom.egg-info/top_level.txt
```

### Comparing `simplebloom-1.0.3/LICENSE` & `simplebloom-1.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/PKG-INFO` & `simplebloom-1.0.4/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,18 @@
 Metadata-Version: 2.1
 Name: simplebloom
-Version: 1.0.3
+Version: 1.0.4
 Summary: A dumb but fast bloom filter.
-Home-page: UNKNOWN
 Author: Joachim Folz
 Author-email: joachim.folz@dfki.de
 License: MIT
 Project-URL: Documentation, https://gitlab.com/jfolz/simplebloom/blob/master/README.rst
 Project-URL: Source, https://gitlab.com/jfolz/simplebloom
 Project-URL: Tracker, https://gitlab.com/jfolz/simplebloom/issues
 Keywords: bloom filter bloomfilter
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Science/Research
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
@@ -171,9 +169,7 @@
 
 
 Developing
 ----------
 
 Extension code is generated by Cython.
 Install Cython to make and build changes to the extension.
-
-
```

### Comparing `simplebloom-1.0.3/README.rst` & `simplebloom-1.0.4/README.rst`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/setup.py` & `simplebloom-1.0.4/setup.py`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/simplebloom/_cbloom.c` & `simplebloom-1.0.4/simplebloom/_cbloom.c`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/simplebloom/_pybloom.py` & `simplebloom-1.0.4/simplebloom/_pybloom.py`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/simplebloom/bloom.py` & `simplebloom-1.0.4/simplebloom/bloom.py`

 * *Files identical despite different names*

### Comparing `simplebloom-1.0.3/simplebloom.egg-info/PKG-INFO` & `simplebloom-1.0.4/simplebloom.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,18 @@
 Metadata-Version: 2.1
 Name: simplebloom
-Version: 1.0.3
+Version: 1.0.4
 Summary: A dumb but fast bloom filter.
-Home-page: UNKNOWN
 Author: Joachim Folz
 Author-email: joachim.folz@dfki.de
 License: MIT
 Project-URL: Documentation, https://gitlab.com/jfolz/simplebloom/blob/master/README.rst
 Project-URL: Source, https://gitlab.com/jfolz/simplebloom
 Project-URL: Tracker, https://gitlab.com/jfolz/simplebloom/issues
 Keywords: bloom filter bloomfilter
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Science/Research
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
@@ -171,9 +169,7 @@
 
 
 Developing
 ----------
 
 Extension code is generated by Cython.
 Install Cython to make and build changes to the extension.
-
-
```

