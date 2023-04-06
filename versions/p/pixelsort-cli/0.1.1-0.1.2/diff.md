# Comparing `tmp/pixelsort-cli-0.1.1.tar.gz` & `tmp/pixelsort-cli-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pixelsort-cli-0.1.1.tar", last modified: Thu Apr  6 15:05:04 2023, max compression
+gzip compressed data, was "pixelsort-cli-0.1.2.tar", last modified: Thu Apr  6 15:10:06 2023, max compression
```

## Comparing `pixelsort-cli-0.1.1.tar` & `pixelsort-cli-0.1.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/
--rw-r--r--   0 dionysus  (1000) wheel      (998)     1072 2023-04-02 00:49:40.000000 pixelsort-cli-0.1.1/LICENSE
--rw-r--r--   0 dionysus  (1000) wheel      (998)     2049 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/PKG-INFO
--rw-r--r--   0 dionysus  (1000) wheel      (998)     1496 2023-04-06 15:02:57.000000 pixelsort-cli-0.1.1/README.md
--rw-r--r--   0 dionysus  (1000) wheel      (998)      879 2023-04-06 15:03:44.000000 pixelsort-cli-0.1.1/pyproject.toml
--rw-r--r--   0 dionysus  (1000) wheel      (998)       38 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/setup.cfg
--rw-r--r--   0 dionysus  (1000) wheel      (998)       67 2023-04-06 13:11:27.000000 pixelsort-cli-0.1.1/setup.py
-drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:05:04.810326 pixelsort-cli-0.1.1/src/
-drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/src/pixelsort/
--rw-r--r--   0 dionysus  (1000) wheel      (998)       85 2023-04-06 15:01:03.000000 pixelsort-cli-0.1.1/src/pixelsort/__init__.py
--rw-r--r--   0 dionysus  (1000) wheel      (998)       69 2023-04-06 14:55:57.000000 pixelsort-cli-0.1.1/src/pixelsort/__main__.py
--rw-r--r--   0 dionysus  (1000) wheel      (998)     3330 2023-04-06 14:56:40.000000 pixelsort-cli-0.1.1/src/pixelsort/cli.py
--rw-r--r--   0 dionysus  (1000) wheel      (998)      234 2023-04-02 00:47:56.000000 pixelsort-cli-0.1.1/src/pixelsort/direction.py
--rw-r--r--   0 dionysus  (1000) wheel      (998)     4630 2023-04-06 14:55:54.000000 pixelsort-cli-0.1.1/src/pixelsort/image.py
-drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/
--rw-r--r--   0 dionysus  (1000) wheel      (998)     2049 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/PKG-INFO
--rw-r--r--   0 dionysus  (1000) wheel      (998)      431 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/SOURCES.txt
--rw-r--r--   0 dionysus  (1000) wheel      (998)        1 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/dependency_links.txt
--rw-r--r--   0 dionysus  (1000) wheel      (998)       49 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/entry_points.txt
--rw-r--r--   0 dionysus  (1000) wheel      (998)       44 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/requires.txt
--rw-r--r--   0 dionysus  (1000) wheel      (998)       10 2023-04-06 15:05:04.000000 pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/top_level.txt
-drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:05:04.813659 pixelsort-cli-0.1.1/test/
--rw-r--r--   0 dionysus  (1000) wheel      (998)      377 2023-04-06 14:55:49.000000 pixelsort-cli-0.1.1/test/test_image.py
+drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     1072 2023-04-02 00:49:40.000000 pixelsort-cli-0.1.2/LICENSE
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     2049 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/PKG-INFO
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     1496 2023-04-06 15:02:57.000000 pixelsort-cli-0.1.2/README.md
+-rw-r--r--   0 dionysus  (1000) wheel      (998)      879 2023-04-06 15:09:31.000000 pixelsort-cli-0.1.2/pyproject.toml
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       38 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/setup.cfg
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       67 2023-04-06 13:11:27.000000 pixelsort-cli-0.1.2/setup.py
+drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:10:06.613669 pixelsort-cli-0.1.2/src/
+drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/src/pixelsort/
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       85 2023-04-06 15:01:03.000000 pixelsort-cli-0.1.2/src/pixelsort/__init__.py
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       69 2023-04-06 14:55:57.000000 pixelsort-cli-0.1.2/src/pixelsort/__main__.py
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     3330 2023-04-06 14:56:40.000000 pixelsort-cli-0.1.2/src/pixelsort/cli.py
+-rw-r--r--   0 dionysus  (1000) wheel      (998)      234 2023-04-02 00:47:56.000000 pixelsort-cli-0.1.2/src/pixelsort/direction.py
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     4630 2023-04-06 14:55:54.000000 pixelsort-cli-0.1.2/src/pixelsort/image.py
+drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/
+-rw-r--r--   0 dionysus  (1000) wheel      (998)     2049 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/PKG-INFO
+-rw-r--r--   0 dionysus  (1000) wheel      (998)      431 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 dionysus  (1000) wheel      (998)        1 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       49 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/entry_points.txt
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       44 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/requires.txt
+-rw-r--r--   0 dionysus  (1000) wheel      (998)       10 2023-04-06 15:10:06.000000 pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/top_level.txt
+drwxr-xr-x   0 dionysus  (1000) wheel      (998)        0 2023-04-06 15:10:06.617003 pixelsort-cli-0.1.2/test/
+-rw-r--r--   0 dionysus  (1000) wheel      (998)      377 2023-04-06 14:55:49.000000 pixelsort-cli-0.1.2/test/test_image.py
```

### Comparing `pixelsort-cli-0.1.1/LICENSE` & `pixelsort-cli-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pixelsort-cli-0.1.1/PKG-INFO` & `pixelsort-cli-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pixelsort-cli
-Version: 0.1.1
+Version: 0.1.2
 Summary: A Python CLI tool for sorting pixels in images.
 Author-email: Ferdinand Theil <f.p.theil@proton.me>
 Project-URL: Homepage, https://github.com/Blotz/pixelsort-cli
 Project-URL: Bug Tracker, https://github.com/Blotz/pixelsort-cli/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `pixelsort-cli-0.1.1/README.md` & `pixelsort-cli-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `pixelsort-cli-0.1.1/pyproject.toml` & `pixelsort-cli-0.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "pixelsort-cli"
-version = "0.1.1"
+version = "0.1.2"
 authors = [
     {name = "Ferdinand Theil", email = "f.p.theil@proton.me"},
 ]
 description = "A Python CLI tool for sorting pixels in images."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pixelsort-cli-0.1.1/src/pixelsort/cli.py` & `pixelsort-cli-0.1.2/src/pixelsort/cli.py`

 * *Files identical despite different names*

### Comparing `pixelsort-cli-0.1.1/src/pixelsort/image.py` & `pixelsort-cli-0.1.2/src/pixelsort/image.py`

 * *Files identical despite different names*

### Comparing `pixelsort-cli-0.1.1/src/pixelsort_cli.egg-info/PKG-INFO` & `pixelsort-cli-0.1.2/src/pixelsort_cli.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pixelsort-cli
-Version: 0.1.1
+Version: 0.1.2
 Summary: A Python CLI tool for sorting pixels in images.
 Author-email: Ferdinand Theil <f.p.theil@proton.me>
 Project-URL: Homepage, https://github.com/Blotz/pixelsort-cli
 Project-URL: Bug Tracker, https://github.com/Blotz/pixelsort-cli/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

