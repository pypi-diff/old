# Comparing `tmp/typedattr-0.1.8.tar.gz` & `tmp/typedattr-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "typedattr-0.1.8.tar", last modified: Wed Mar 29 15:14:20 2023, max compression
+gzip compressed data, was "typedattr-0.1.9.tar", last modified: Wed Mar 29 15:23:03 2023, max compression
```

## Comparing `typedattr-0.1.8.tar` & `typedattr-0.1.9.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-03-29 15:14:20.585669 typedattr-0.1.8/
--rw-rw-rw-   0        0        0    11336 2023-03-29 13:28:06.000000 typedattr-0.1.8/LICENSE
--rw-rw-rw-   0        0        0     3812 2023-03-29 15:14:20.585102 typedattr-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0     2945 2023-03-29 15:00:43.000000 typedattr-0.1.8/README.md
--rw-rw-rw-   0        0        0     2200 2023-03-29 14:51:05.000000 typedattr-0.1.8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-03-29 15:14:20.585669 typedattr-0.1.8/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-03-29 15:14:20.554990 typedattr-0.1.8/src/
-drwxrwxrwx   0        0        0        0 2023-03-29 15:14:20.565990 typedattr-0.1.8/src/typedattr/
--rw-rw-rw-   0        0        0      121 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/__init__.py
--rw-rw-rw-   0        0        0    11027 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/_typedattr.py
--rw-rw-rw-   0        0        0      243 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/attrutils.py
--rw-rw-rw-   0        0        0     3090 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/cacheutils.py
--rw-rw-rw-   0        0        0     8799 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/objutils.py
--rw-rw-rw-   0        0        0      192 2023-03-29 15:00:43.000000 typedattr-0.1.8/src/typedattr/typeutils.py
-drwxrwxrwx   0        0        0        0 2023-03-29 15:14:20.584093 typedattr-0.1.8/src/typedattr.egg-info/
--rw-rw-rw-   0        0        0     3812 2023-03-29 15:14:20.000000 typedattr-0.1.8/src/typedattr.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      374 2023-03-29 15:14:20.000000 typedattr-0.1.8/src/typedattr.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-29 15:14:20.000000 typedattr-0.1.8/src/typedattr.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       10 2023-03-29 15:14:20.000000 typedattr-0.1.8/src/typedattr.egg-info/top_level.txt
--rw-rw-rw-   0        0        0        2 2023-03-29 14:51:16.000000 typedattr-0.1.8/src/typedattr.egg-info/zip-safe
+drwxrwxrwx   0        0        0        0 2023-03-29 15:23:03.859237 typedattr-0.1.9/
+-rw-rw-rw-   0        0        0    11336 2023-03-29 13:28:06.000000 typedattr-0.1.9/LICENSE
+-rw-rw-rw-   0        0        0     3875 2023-03-29 15:23:03.858238 typedattr-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0     2945 2023-03-29 15:22:14.000000 typedattr-0.1.9/README.md
+-rw-rw-rw-   0        0        0     2268 2023-03-29 15:20:31.000000 typedattr-0.1.9/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-03-29 15:23:03.859237 typedattr-0.1.9/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-03-29 15:23:03.828925 typedattr-0.1.9/src/
+drwxrwxrwx   0        0        0        0 2023-03-29 15:23:03.836937 typedattr-0.1.9/src/typedattr/
+-rw-rw-rw-   0        0        0      121 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/__init__.py
+-rw-rw-rw-   0        0        0    11027 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/_typedattr.py
+-rw-rw-rw-   0        0        0      243 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/attrutils.py
+-rw-rw-rw-   0        0        0     3090 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/cacheutils.py
+-rw-rw-rw-   0        0        0     8799 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/objutils.py
+-rw-rw-rw-   0        0        0      192 2023-03-29 15:22:14.000000 typedattr-0.1.9/src/typedattr/typeutils.py
+drwxrwxrwx   0        0        0        0 2023-03-29 15:23:03.857230 typedattr-0.1.9/src/typedattr.egg-info/
+-rw-rw-rw-   0        0        0     3875 2023-03-29 15:23:03.000000 typedattr-0.1.9/src/typedattr.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      374 2023-03-29 15:23:03.000000 typedattr-0.1.9/src/typedattr.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-29 15:23:03.000000 typedattr-0.1.9/src/typedattr.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       10 2023-03-29 15:23:03.000000 typedattr-0.1.9/src/typedattr.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0        2 2023-03-29 14:51:16.000000 typedattr-0.1.9/src/typedattr.egg-info/zip-safe
```

### Comparing `typedattr-0.1.8/LICENSE` & `typedattr-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `typedattr-0.1.8/PKG-INFO` & `typedattr-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 Metadata-Version: 2.1
 Name: typedattr
-Version: 0.1.8
+Version: 0.1.9
 Summary: Typed conversion of dictionaries to attrs instances
 Author: gingsi
 License: Apache-2.0
+Project-URL: Project-URL, https://github.com/gingsi/typedattr
 Keywords: attrs,typing,dict,attr
 Platform: any
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `typedattr-0.1.8/README.md` & `typedattr-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `typedattr-0.1.8/pyproject.toml` & `typedattr-0.1.9/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -19,14 +19,17 @@
     "Programming Language :: Python :: 3.8",
     "Programming Language :: Python :: 3.9",
     "Operating System :: OS Independent",
     "Topic :: Software Development :: Version Control :: Git"
 ]
 dynamic = ["version"]
 
+[project.urls]
+Project-URL = "https://github.com/gingsi/typedattr"
+
 [tool.setuptools]
 zip-safe = true
 platforms = ["any"]
 include-package-data = false
 
 [tool.setuptools.dynamic]
 version = { attr = "typedattr.__version__" }
```

### Comparing `typedattr-0.1.8/src/typedattr/_typedattr.py` & `typedattr-0.1.9/src/typedattr/_typedattr.py`

 * *Files identical despite different names*

### Comparing `typedattr-0.1.8/src/typedattr/cacheutils.py` & `typedattr-0.1.9/src/typedattr/cacheutils.py`

 * *Files identical despite different names*

### Comparing `typedattr-0.1.8/src/typedattr/objutils.py` & `typedattr-0.1.9/src/typedattr/objutils.py`

 * *Files identical despite different names*

### Comparing `typedattr-0.1.8/src/typedattr.egg-info/PKG-INFO` & `typedattr-0.1.9/src/typedattr.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 Metadata-Version: 2.1
 Name: typedattr
-Version: 0.1.8
+Version: 0.1.9
 Summary: Typed conversion of dictionaries to attrs instances
 Author: gingsi
 License: Apache-2.0
+Project-URL: Project-URL, https://github.com/gingsi/typedattr
 Keywords: attrs,typing,dict,attr
 Platform: any
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.7
```

