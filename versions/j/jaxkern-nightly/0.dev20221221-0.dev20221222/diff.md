# Comparing `tmp/jaxkern-nightly-0.dev20221221.tar.gz` & `tmp/jaxkern-nightly-0.dev20221222.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/jaxkern-nightly-0.dev20221221.tar", last modified: Wed Dec 21 00:04:55 2022, max compression
+gzip compressed data, was "dist/jaxkern-nightly-0.dev20221222.tar", last modified: Thu Dec 22 00:04:43 2022, max compression
```

## Comparing `jaxkern-nightly-0.dev20221221.tar` & `jaxkern-nightly-0.dev20221222.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-21 00:04:55.351562 jaxkern-nightly-0.dev20221221/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      988 2022-12-21 00:04:55.351562 jaxkern-nightly-0.dev20221221/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      436 2022-12-21 00:04:49.000000 jaxkern-nightly-0.dev20221221/README.md
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-21 00:04:55.351562 jaxkern-nightly-0.dev20221221/jaxkern/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      583 2022-12-21 00:04:49.000000 jaxkern-nightly-0.dev20221221/jaxkern/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    23620 2022-12-21 00:04:49.000000 jaxkern-nightly-0.dev20221221/jaxkern/_version.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    36292 2022-12-21 00:04:49.000000 jaxkern-nightly-0.dev20221221/jaxkern/kernels.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-21 00:04:55.351562 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      988 2022-12-21 00:04:55.000000 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      281 2022-12-21 00:04:55.000000 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-12-21 00:04:55.000000 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      164 2022-12-21 00:04:55.000000 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        8 2022-12-21 00:04:55.000000 jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      231 2022-12-21 00:04:55.351562 jaxkern-nightly-0.dev20221221/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1750 2022-12-21 00:04:49.000000 jaxkern-nightly-0.dev20221221/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-22 00:04:43.465968 jaxkern-nightly-0.dev20221222/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      988 2022-12-22 00:04:43.465968 jaxkern-nightly-0.dev20221222/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      436 2022-12-22 00:04:37.000000 jaxkern-nightly-0.dev20221222/README.md
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-22 00:04:43.465968 jaxkern-nightly-0.dev20221222/jaxkern/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      583 2022-12-22 00:04:37.000000 jaxkern-nightly-0.dev20221222/jaxkern/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    23620 2022-12-22 00:04:37.000000 jaxkern-nightly-0.dev20221222/jaxkern/_version.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    36292 2022-12-22 00:04:37.000000 jaxkern-nightly-0.dev20221222/jaxkern/kernels.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-12-22 00:04:43.465968 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      988 2022-12-22 00:04:43.000000 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      281 2022-12-22 00:04:43.000000 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-12-22 00:04:43.000000 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      164 2022-12-22 00:04:43.000000 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        8 2022-12-22 00:04:43.000000 jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      231 2022-12-22 00:04:43.469968 jaxkern-nightly-0.dev20221222/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1750 2022-12-22 00:04:37.000000 jaxkern-nightly-0.dev20221222/setup.py
```

### Comparing `jaxkern-nightly-0.dev20221221/PKG-INFO` & `jaxkern-nightly-0.dev20221222/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jaxkern-nightly
-Version: 0.dev20221221
+Version: 0.dev20221222
 Summary: Kernels in Jax.
 Home-page: UNKNOWN
 Author: Daniel Dodd and Thomas Pinder
 Author-email: tompinder@live.co.uk
 License: LICENSE
 Project-URL: Documentation, https://JaxKern.readthedocs.io/en/latest/
 Project-URL: Source, https://github.com/JaxGaussianProcesses/JaxKern
```

### Comparing `jaxkern-nightly-0.dev20221221/jaxkern/__init__.py` & `jaxkern-nightly-0.dev20221222/jaxkern/__init__.py`

 * *Files identical despite different names*

### Comparing `jaxkern-nightly-0.dev20221221/jaxkern/_version.py` & `jaxkern-nightly-0.dev20221222/jaxkern/_version.py`

 * *Files identical despite different names*

### Comparing `jaxkern-nightly-0.dev20221221/jaxkern/kernels.py` & `jaxkern-nightly-0.dev20221222/jaxkern/kernels.py`

 * *Files identical despite different names*

### Comparing `jaxkern-nightly-0.dev20221221/jaxkern_nightly.egg-info/PKG-INFO` & `jaxkern-nightly-0.dev20221222/jaxkern_nightly.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jaxkern-nightly
-Version: 0.dev20221221
+Version: 0.dev20221222
 Summary: Kernels in Jax.
 Home-page: UNKNOWN
 Author: Daniel Dodd and Thomas Pinder
 Author-email: tompinder@live.co.uk
 License: LICENSE
 Project-URL: Documentation, https://JaxKern.readthedocs.io/en/latest/
 Project-URL: Source, https://github.com/JaxGaussianProcesses/JaxKern
```

### Comparing `jaxkern-nightly-0.dev20221221/setup.py` & `jaxkern-nightly-0.dev20221222/setup.py`

 * *Files identical despite different names*

