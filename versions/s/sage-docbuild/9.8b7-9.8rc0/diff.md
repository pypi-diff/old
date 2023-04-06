# Comparing `tmp/sage-docbuild-9.8b7.tar.gz` & `tmp/sage-docbuild-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sage-docbuild-9.8b7.tar", last modified: Thu Jan 19 06:51:29 2023, max compression
+gzip compressed data, was "sage-docbuild-9.8rc0.tar", last modified: Sun Jan 29 23:46:56 2023, max compression
```

## Comparing `sage-docbuild-9.8b7.tar` & `sage-docbuild-9.8rc0.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:29.410551 sage-docbuild-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)       20 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-01-19 06:51:29.410551 sage-docbuild-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/VERSION.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:29.406551 sage-docbuild-9.8b7/sage_docbuild/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21202 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      757 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/build_options.py
--rw-r--r--   0 runner    (1001) docker     (123)    51454 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/builders.py
--rw-r--r--   0 runner    (1001) docker     (123)    38070 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/conf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:29.410551 sage-docbuild-9.8b7/sage_docbuild/ext/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/ext/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/ext/inventory_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)    12737 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/ext/multidocs.py
--rw-r--r--   0 runner    (1001) docker     (123)   121165 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/ext/sage_autodoc.py
--rw-r--r--   0 runner    (1001) docker     (123)    13441 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/sphinxbuild.py
--rw-r--r--   0 runner    (1001) docker     (123)    13278 2023-01-19 06:47:41.000000 sage-docbuild-9.8b7/sage_docbuild/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:29.406551 sage-docbuild-9.8b7/sage_docbuild.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-01-19 06:51:28.000000 sage-docbuild-9.8b7/sage_docbuild.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      579 2023-01-19 06:51:29.000000 sage-docbuild-9.8b7/sage_docbuild.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:28.000000 sage-docbuild-9.8b7/sage_docbuild.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-01-19 06:51:28.000000 sage-docbuild-9.8b7/sage_docbuild.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-01-19 06:51:28.000000 sage-docbuild-9.8b7/sage_docbuild.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-01-19 06:51:29.410551 sage-docbuild-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)      546 2023-01-19 06:47:40.000000 sage-docbuild-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)       20 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/VERSION.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/sage_docbuild/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21202 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      757 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/build_options.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51454 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/builders.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38070 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/conf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/sage_docbuild/ext/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/ext/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/ext/inventory_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12737 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/ext/multidocs.py
+-rw-r--r--   0 runner    (1001) docker     (123)   121165 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/ext/sage_autodoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13441 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/sphinxbuild.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13278 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/sage_docbuild/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/sage_docbuild.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-01-29 23:46:55.000000 sage-docbuild-9.8rc0/sage_docbuild.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      579 2023-01-29 23:46:56.000000 sage-docbuild-9.8rc0/sage_docbuild.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:46:55.000000 sage-docbuild-9.8rc0/sage_docbuild.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-01-29 23:46:55.000000 sage-docbuild-9.8rc0/sage_docbuild.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-01-29 23:46:55.000000 sage-docbuild-9.8rc0/sage_docbuild.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-01-29 23:46:56.765817 sage-docbuild-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)      546 2023-01-29 23:43:48.000000 sage-docbuild-9.8rc0/tox.ini
```

### Comparing `sage-docbuild-9.8b7/PKG-INFO` & `sage-docbuild-9.8rc0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-docbuild
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Build system of the Sage documentation
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sage-docbuild-9.8b7/README.rst` & `sage-docbuild-9.8rc0/README.rst`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/__main__.py` & `sage-docbuild-9.8rc0/sage_docbuild/__main__.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/build_options.py` & `sage-docbuild-9.8rc0/sage_docbuild/build_options.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/builders.py` & `sage-docbuild-9.8rc0/sage_docbuild/builders.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/conf.py` & `sage-docbuild-9.8rc0/sage_docbuild/conf.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/ext/inventory_builder.py` & `sage-docbuild-9.8rc0/sage_docbuild/ext/inventory_builder.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/ext/multidocs.py` & `sage-docbuild-9.8rc0/sage_docbuild/ext/multidocs.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/ext/sage_autodoc.py` & `sage-docbuild-9.8rc0/sage_docbuild/ext/sage_autodoc.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/sphinxbuild.py` & `sage-docbuild-9.8rc0/sage_docbuild/sphinxbuild.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild/utils.py` & `sage-docbuild-9.8rc0/sage_docbuild/utils.py`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/sage_docbuild.egg-info/PKG-INFO` & `sage-docbuild-9.8rc0/sage_docbuild.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sage-docbuild
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: Build system of the Sage documentation
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sage-docbuild-9.8b7/sage_docbuild.egg-info/SOURCES.txt` & `sage-docbuild-9.8rc0/sage_docbuild.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/setup.cfg` & `sage-docbuild-9.8rc0/setup.cfg`

 * *Files identical despite different names*

### Comparing `sage-docbuild-9.8b7/tox.ini` & `sage-docbuild-9.8rc0/tox.ini`

 * *Files 24% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 [testenv]
 deps = -rrequirements.txt
 
 setenv =
     # Sage scripts like to use $HOME/.sage
     HOME={envdir}
 
-whitelist_externals =
+allowlist_externals =
     bash
 
 commands =
     # Beware of the treacherous non-src layout.
     #python -c 'import sys; "" in sys.path and sys.path.remove(""); import sage_docbuild'
 
 # TODO: Add tests after adding the dependency on sagelib to
```

