# Comparing `tmp/cqepyutils-0.1.8.tar.gz` & `tmp/cqepyutils-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cqepyutils-0.1.8.tar", last modified: Thu Apr  6 03:46:37 2023, max compression
+gzip compressed data, was "cqepyutils-0.1.9.tar", last modified: Thu Apr  6 22:43:54 2023, max compression
```

## Comparing `cqepyutils-0.1.8.tar` & `cqepyutils-0.1.9.tar`

### file list

```diff
@@ -1,27 +1,28 @@
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.308550 cqepyutils-0.1.8/
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.305636 cqepyutils-0.1.8/DBUtils/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     3053 2023-04-06 03:44:45.000000 cqepyutils-0.1.8/DBUtils/DBUtils.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       21 2023-04-05 22:45:36.000000 cqepyutils-0.1.8/DBUtils/__init__.py
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.306102 cqepyutils-0.1.8/FileUtils/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     1519 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/FileUtils/FileUtils.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       23 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/FileUtils/__init__.py
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.306479 cqepyutils-0.1.8/JSONUtils/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     1421 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/JSONUtils/JSONUtils.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)        0 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/JSONUtils/__init__.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     1086 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/LICENSE
--rw-r--r--   0 vaanisridhar   (501) staff       (20)      739 2023-04-06 03:46:37.308369 cqepyutils-0.1.8/PKG-INFO
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.306764 cqepyutils-0.1.8/PandasUtils/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)    10755 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/PandasUtils/PandasUtils.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       26 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/PandasUtils/__init__.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)      108 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/README.md
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.307083 cqepyutils-0.1.8/RFUtils/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     4294 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/RFUtils/RFUtils.py
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       21 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/RFUtils/__init__.py
-drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 03:46:37.308138 cqepyutils-0.1.8/cqepyutils.egg-info/
--rw-r--r--   0 vaanisridhar   (501) staff       (20)      739 2023-04-06 03:46:37.000000 cqepyutils-0.1.8/cqepyutils.egg-info/PKG-INFO
--rw-r--r--   0 vaanisridhar   (501) staff       (20)      414 2023-04-06 03:46:37.000000 cqepyutils-0.1.8/cqepyutils.egg-info/SOURCES.txt
--rw-r--r--   0 vaanisridhar   (501) staff       (20)        1 2023-04-06 03:46:37.000000 cqepyutils-0.1.8/cqepyutils.egg-info/dependency_links.txt
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       68 2023-04-06 03:46:37.000000 cqepyutils-0.1.8/cqepyutils.egg-info/requires.txt
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       48 2023-04-06 03:46:37.000000 cqepyutils-0.1.8/cqepyutils.egg-info/top_level.txt
--rw-r--r--   0 vaanisridhar   (501) staff       (20)       38 2023-04-06 03:46:37.308624 cqepyutils-0.1.8/setup.cfg
--rw-r--r--   0 vaanisridhar   (501) staff       (20)     1180 2023-04-05 22:41:58.000000 cqepyutils-0.1.8/setup.py
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.027130 cqepyutils-0.1.9/
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.024035 cqepyutils-0.1.9/DBUtils/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     3053 2023-04-06 03:44:45.000000 cqepyutils-0.1.9/DBUtils/DBUtils.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     6840 2023-04-06 22:40:12.000000 cqepyutils-0.1.9/DBUtils/Sample.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       21 2023-04-05 22:45:36.000000 cqepyutils-0.1.9/DBUtils/__init__.py
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.024543 cqepyutils-0.1.9/FileUtils/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     1519 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/FileUtils/FileUtils.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       23 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/FileUtils/__init__.py
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.024924 cqepyutils-0.1.9/JSONUtils/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     1421 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/JSONUtils/JSONUtils.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)        0 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/JSONUtils/__init__.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     1086 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/LICENSE
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)      739 2023-04-06 22:43:54.026866 cqepyutils-0.1.9/PKG-INFO
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.025316 cqepyutils-0.1.9/PandasUtils/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)    10755 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/PandasUtils/PandasUtils.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       26 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/PandasUtils/__init__.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)      108 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/README.md
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.025691 cqepyutils-0.1.9/RFUtils/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     4294 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/RFUtils/RFUtils.py
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       21 2023-04-05 22:41:58.000000 cqepyutils-0.1.9/RFUtils/__init__.py
+drwxr-xr-x   0 vaanisridhar   (501) staff       (20)        0 2023-04-06 22:43:54.026535 cqepyutils-0.1.9/cqepyutils.egg-info/
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)      739 2023-04-06 22:43:53.000000 cqepyutils-0.1.9/cqepyutils.egg-info/PKG-INFO
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)      432 2023-04-06 22:43:53.000000 cqepyutils-0.1.9/cqepyutils.egg-info/SOURCES.txt
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)        1 2023-04-06 22:43:53.000000 cqepyutils-0.1.9/cqepyutils.egg-info/dependency_links.txt
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)      108 2023-04-06 22:43:53.000000 cqepyutils-0.1.9/cqepyutils.egg-info/requires.txt
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       48 2023-04-06 22:43:53.000000 cqepyutils-0.1.9/cqepyutils.egg-info/top_level.txt
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)       38 2023-04-06 22:43:54.027210 cqepyutils-0.1.9/setup.cfg
+-rw-r--r--   0 vaanisridhar   (501) staff       (20)     1406 2023-04-06 22:42:45.000000 cqepyutils-0.1.9/setup.py
```

### Comparing `cqepyutils-0.1.8/DBUtils/DBUtils.py` & `cqepyutils-0.1.9/DBUtils/DBUtils.py`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/FileUtils/FileUtils.py` & `cqepyutils-0.1.9/FileUtils/FileUtils.py`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/JSONUtils/JSONUtils.py` & `cqepyutils-0.1.9/JSONUtils/JSONUtils.py`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/LICENSE` & `cqepyutils-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/PKG-INFO` & `cqepyutils-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cqepyutils
-Version: 0.1.8
+Version: 0.1.9
 Summary: Cognitive Quality Engineer - Python Reusable Function Library
 Home-page: https://github.com/cognitiveqe/cqepyutils/
 Author: Sridhar VP
 Author-email: sridharvpmca@gmail.com
 License: MIT
 Keywords: Python Reusable Function Library
 Platform: any
```

### Comparing `cqepyutils-0.1.8/PandasUtils/PandasUtils.py` & `cqepyutils-0.1.9/PandasUtils/PandasUtils.py`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/RFUtils/RFUtils.py` & `cqepyutils-0.1.9/RFUtils/RFUtils.py`

 * *Files identical despite different names*

### Comparing `cqepyutils-0.1.8/cqepyutils.egg-info/PKG-INFO` & `cqepyutils-0.1.9/cqepyutils.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cqepyutils
-Version: 0.1.8
+Version: 0.1.9
 Summary: Cognitive Quality Engineer - Python Reusable Function Library
 Home-page: https://github.com/cognitiveqe/cqepyutils/
 Author: Sridhar VP
 Author-email: sridharvpmca@gmail.com
 License: MIT
 Keywords: Python Reusable Function Library
 Platform: any
```

### Comparing `cqepyutils-0.1.8/setup.py` & `cqepyutils-0.1.9/setup.py`

 * *Files 20% similar despite different names*

```diff
@@ -30,14 +30,31 @@
     license='MIT',
     packages=setuptools.find_packages(),
     platforms='any',
     classifiers=CLASSIFIERS.splitlines(),
     python_requires='>=3.6',
     install_requires=[
         'pandas',
+        'xlsxwriter',
+        'matplotlib',
         'numpy',
         'requests',
         'robotframework',
         'robotframework-requests',
         'jinja2',
+        'pyyaml',
+        'sqlalchemy',
     ],
 )
+
+# 'logging',
+
+# 'dask',
+# 'base64',
+# 'display',
+# 'difflib',
+# 'time',
+# 'os',
+# 'filecmp',
+# 'fileinput',
+# 'operator',
+# 'create_engine',
```

