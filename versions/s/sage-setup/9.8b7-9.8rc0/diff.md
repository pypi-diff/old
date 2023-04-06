# Comparing `tmp/sage-setup-9.8b7.tar.gz` & `tmp/sage-setup-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sage-setup-9.8b7.tar", last modified: Thu Jan 19 06:51:30 2023, max compression
+gzip compressed data, was "sage-setup-9.8rc0.tar", last modified: Sun Jan 29 23:46:57 2023, max compression
```

## Comparing `sage-setup-9.8b7.tar` & `sage-setup-9.8rc0.tar`

### file list

```diff
@@ -1,52 +1,52 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-01-19 06:51:30.674571 sage-setup-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-19 06:47:40.000000 sage-setup-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sage-setup-9.8b7/VERSION.txt
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-01-19 06:47:40.000000 sage-setup-9.8b7/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup/autogen/
--rw-r--r--   0 runner    (1001) docker     (123)      407 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       42 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)    28790 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/giacpy-mkkeywords.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup/autogen/interpreters/
--rw-r--r--   0 runner    (1001) docker     (123)     8917 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)    39187 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    15724 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/instructions.py
--rw-r--r--   0 runner    (1001) docker     (123)    18579 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/memory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5795 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9412 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/cc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9353 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/cdf.py
--rw-r--r--   0 runner    (1001) docker     (123)     4810 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/element.py
--rw-r--r--   0 runner    (1001) docker     (123)    10467 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/python.py
--rw-r--r--   0 runner    (1001) docker     (123)     6989 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/rdf.py
--rw-r--r--   0 runner    (1001) docker     (123)    10260 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/rr.py
--rw-r--r--   0 runner    (1001) docker     (123)    33583 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/storage.py
--rw-r--r--   0 runner    (1001) docker     (123)     4968 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/autogen/interpreters/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/clean.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup/command/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/command/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11899 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/command/sage_build_cython.py
--rw-r--r--   0 runner    (1001) docker     (123)     8589 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/command/sage_build_ext.py
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/command/sage_build_ext_minimal.py
--rw-r--r--   0 runner    (1001) docker     (123)     4362 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/command/sage_install.py
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/cython_options.py
--rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/excepthook.py
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)    17677 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/find.py
--rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/library_order.py
--rw-r--r--   0 runner    (1001) docker     (123)     4505 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/run_parallel.py
--rw-r--r--   0 runner    (1001) docker     (123)     2220 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/setenv.py
--rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-19 06:47:41.000000 sage-setup-9.8b7/sage_setup/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:30.674571 sage-setup-9.8b7/sage_setup.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-01-19 06:51:29.000000 sage-setup-9.8b7/sage_setup.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-01-19 06:51:30.000000 sage-setup-9.8b7/sage_setup.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:29.000000 sage-setup-9.8b7/sage_setup.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-19 06:51:29.000000 sage-setup-9.8b7/sage_setup.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-19 06:51:29.000000 sage-setup-9.8b7/sage_setup.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-01-19 06:51:30.674571 sage-setup-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-19 06:47:40.000000 sage-setup-9.8b7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)      850 2023-01-19 06:47:40.000000 sage-setup-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/VERSION.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup/autogen/
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28790 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/giacpy-mkkeywords.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup/autogen/interpreters/
+-rw-r--r--   0 runner    (1001) docker     (123)     8917 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39187 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15724 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/instructions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18579 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/memory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5795 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9412 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/cc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9353 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/cdf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4810 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/element.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10467 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/python.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6989 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/rdf.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10260 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/rr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33583 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4968 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/autogen/interpreters/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7313 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/clean.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup/command/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/command/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11899 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/command/sage_build_cython.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8589 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/command/sage_build_ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/command/sage_build_ext_minimal.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4362 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/command/sage_install.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/cython_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/excepthook.py
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17677 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/find.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/library_order.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4505 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/run_parallel.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2220 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/setenv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/sage_setup/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/sage_setup.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-01-29 23:46:57.000000 sage-setup-9.8rc0/sage_setup.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-01-29 23:46:57.000000 sage-setup-9.8rc0/sage_setup.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:46:57.000000 sage-setup-9.8rc0/sage_setup.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-29 23:46:57.000000 sage-setup-9.8rc0/sage_setup.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-29 23:46:57.000000 sage-setup-9.8rc0/sage_setup.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-01-29 23:46:57.909807 sage-setup-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)      850 2023-01-29 23:43:48.000000 sage-setup-9.8rc0/tox.ini
```

### Comparing `sage-setup-9.8b7/PKG-INFO` & `sage-setup-9.8rc0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-setup
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Build system of the Sage library
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sage-setup-9.8b7/sage_setup/autogen/giacpy-mkkeywords.py` & `sage-setup-9.8rc0/sage_setup/autogen/giacpy-mkkeywords.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/__init__.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/__init__.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/generator.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/generator.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/instructions.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/instructions.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/memory.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/memory.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/base.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/base.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/cc.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/cc.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/cdf.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/cdf.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/element.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/element.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/python.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/python.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/rdf.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/rdf.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/specs/rr.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/specs/rr.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/storage.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/storage.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/autogen/interpreters/utils.py` & `sage-setup-9.8rc0/sage_setup/autogen/interpreters/utils.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/clean.py` & `sage-setup-9.8rc0/sage_setup/clean.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/command/sage_build_cython.py` & `sage-setup-9.8rc0/sage_setup/command/sage_build_cython.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/command/sage_build_ext.py` & `sage-setup-9.8rc0/sage_setup/command/sage_build_ext.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/command/sage_build_ext_minimal.py` & `sage-setup-9.8rc0/sage_setup/command/sage_build_ext_minimal.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/command/sage_install.py` & `sage-setup-9.8rc0/sage_setup/command/sage_install.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/cython_options.py` & `sage-setup-9.8rc0/sage_setup/cython_options.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/excepthook.py` & `sage-setup-9.8rc0/sage_setup/excepthook.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/find.py` & `sage-setup-9.8rc0/sage_setup/find.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/library_order.py` & `sage-setup-9.8rc0/sage_setup/library_order.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/run_parallel.py` & `sage-setup-9.8rc0/sage_setup/run_parallel.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/setenv.py` & `sage-setup-9.8rc0/sage_setup/setenv.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup/util.py` & `sage-setup-9.8rc0/sage_setup/util.py`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/sage_setup.egg-info/PKG-INFO` & `sage-setup-9.8rc0/sage_setup.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-setup
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Build system of the Sage library
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sage-setup-9.8b7/sage_setup.egg-info/SOURCES.txt` & `sage-setup-9.8rc0/sage_setup.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/setup.cfg` & `sage-setup-9.8rc0/setup.cfg`

 * *Files identical despite different names*

### Comparing `sage-setup-9.8b7/tox.ini` & `sage-setup-9.8rc0/tox.ini`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 [testenv]
 deps = -rrequirements.txt
 
 setenv =
     # Sage scripts such as sage-runtests like to use $HOME/.sage
     HOME={envdir}
 
-whitelist_externals =
+allowlist_externals =
     bash
 
 commands =
     # Beware of the treacherous non-src layout.
     python -c 'import sys; "" in sys.path and sys.path.remove(""); import sage_setup; import sage_setup.find'
 
 # TODO: Test importing sage_setup.library_order -- when that can handle missing pkgconfig libraries...
```

