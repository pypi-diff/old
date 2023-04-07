# Comparing `tmp/conda-store-0.4.8.tar.gz` & `tmp/conda-store-0.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "conda-store-0.4.8.tar", last modified: Thu Aug  4 05:00:45 2022, max compression
+gzip compressed data, was "conda-store-0.4.9.tar", last modified: Wed Aug 10 02:39:14 2022, max compression
```

## Comparing `conda-store-0.4.8.tar` & `conda-store-0.4.9.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 05:00:45.938103 conda-store-0.4.8/
--rw-r--r--   0 runner    (1001) docker     (121)     1457 2022-08-04 05:00:31.000000 conda-store-0.4.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     3472 2022-08-04 05:00:45.938103 conda-store-0.4.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1043 2022-08-04 05:00:31.000000 conda-store-0.4.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 05:00:45.938103 conda-store-0.4.8/conda_store/
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1281 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7066 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/api.py
--rw-r--r--   0 runner    (1001) docker     (121)      857 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/auth.py
--rw-r--r--   0 runner    (1001) docker     (121)    13931 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)       43 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/exception.py
--rw-r--r--   0 runner    (1001) docker     (121)     1355 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/runner.py
--rw-r--r--   0 runner    (1001) docker     (121)     2318 2022-08-04 05:00:31.000000 conda-store-0.4.8/conda_store/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-04 05:00:45.938103 conda-store-0.4.8/conda_store.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3472 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      458 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       58 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      135 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-04 05:00:45.000000 conda-store-0.4.8/conda_store.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)      154 2022-08-04 05:00:31.000000 conda-store-0.4.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)     1391 2022-08-04 05:00:45.938103 conda-store-0.4.8/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-10 02:39:14.107193 conda-store-0.4.9/
+-rw-r--r--   0 runner    (1001) docker     (121)     1457 2022-08-10 02:39:00.000000 conda-store-0.4.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     3472 2022-08-10 02:39:14.107193 conda-store-0.4.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1043 2022-08-10 02:39:00.000000 conda-store-0.4.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-10 02:39:14.107193 conda-store-0.4.9/conda_store/
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1281 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7066 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      857 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/auth.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13931 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)       43 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/exception.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1355 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/runner.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2318 2022-08-10 02:39:00.000000 conda-store-0.4.9/conda_store/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-10 02:39:14.107193 conda-store-0.4.9/conda_store.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3472 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      458 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       58 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      135 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-08-10 02:39:14.000000 conda-store-0.4.9/conda_store.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-10 02:39:13.000000 conda-store-0.4.9/conda_store.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)      154 2022-08-10 02:39:00.000000 conda-store-0.4.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)     1391 2022-08-10 02:39:14.107193 conda-store-0.4.9/setup.cfg
```

### Comparing `conda-store-0.4.8/LICENSE` & `conda-store-0.4.9/LICENSE`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/PKG-INFO` & `conda-store-0.4.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: conda-store
-Version: 0.4.8
+Version: 0.4.9
 Summary: conda-store client
 Home-page: https://github.com/Quansight/conda-store
 Author: Christopher Ostrouchov
 Author-email: chris.ostrouchov@gmail.com
 License: BSD License
 Project-URL: Bug Reports, https://github.com/quansight/conda-store
 Project-URL: Documentation, https://conda-store.readthedocs.io/
```

### Comparing `conda-store-0.4.8/README.md` & `conda-store-0.4.9/README.md`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/__main__.py` & `conda-store-0.4.9/conda_store/__main__.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/api.py` & `conda-store-0.4.9/conda_store/api.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/auth.py` & `conda-store-0.4.9/conda_store/auth.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/cli.py` & `conda-store-0.4.9/conda_store/cli.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/runner.py` & `conda-store-0.4.9/conda_store/runner.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store/utils.py` & `conda-store-0.4.9/conda_store/utils.py`

 * *Files identical despite different names*

### Comparing `conda-store-0.4.8/conda_store.egg-info/PKG-INFO` & `conda-store-0.4.9/conda_store.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: conda-store
-Version: 0.4.8
+Version: 0.4.9
 Summary: conda-store client
 Home-page: https://github.com/Quansight/conda-store
 Author: Christopher Ostrouchov
 Author-email: chris.ostrouchov@gmail.com
 License: BSD License
 Project-URL: Bug Reports, https://github.com/quansight/conda-store
 Project-URL: Documentation, https://conda-store.readthedocs.io/
```

### Comparing `conda-store-0.4.8/setup.cfg` & `conda-store-0.4.9/setup.cfg`

 * *Files identical despite different names*

