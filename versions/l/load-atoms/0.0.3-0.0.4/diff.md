# Comparing `tmp/load-atoms-0.0.3.tar.gz` & `tmp/load-atoms-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "load-atoms-0.0.3.tar", last modified: Thu Apr  6 10:09:45 2023, max compression
+gzip compressed data, was "load-atoms-0.0.4.tar", last modified: Thu Apr  6 10:24:24 2023, max compression
```

## Comparing `load-atoms-0.0.3.tar` & `load-atoms-0.0.4.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.837371 load-atoms-0.0.3/
--rw-r--r--   0 john       (504) staff       (20)     1069 2023-04-04 12:18:14.000000 load-atoms-0.0.3/LICENSE
--rw-r--r--   0 john       (504) staff       (20)       48 2023-03-07 08:55:19.000000 load-atoms-0.0.3/MANIFEST.in
--rw-r--r--   0 john       (504) staff       (20)     2700 2023-04-06 10:09:45.837217 load-atoms-0.0.3/PKG-INFO
--rw-r--r--   0 john       (504) staff       (20)      905 2023-04-04 12:19:43.000000 load-atoms-0.0.3/README.md
--rw-r--r--   0 john       (504) staff       (20)     1309 2023-04-06 10:09:35.000000 load-atoms-0.0.3/pyproject.toml
--rw-r--r--   0 john       (504) staff       (20)       38 2023-04-06 10:09:45.837414 load-atoms-0.0.3/setup.cfg
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.830909 load-atoms-0.0.3/src/
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.834038 load-atoms-0.0.3/src/load_atoms/
--rw-r--r--   0 john       (504) staff       (20)      127 2023-04-06 10:09:35.000000 load-atoms-0.0.3/src/load_atoms/__init__.py
--rw-r--r--   0 john       (504) staff       (20)     1727 2023-04-05 06:56:03.000000 load-atoms-0.0.3/src/load_atoms/api.py
--rw-r--r--   0 john       (504) staff       (20)     3304 2023-04-05 08:42:48.000000 load-atoms-0.0.3/src/load_atoms/backend.py
--rw-r--r--   0 john       (504) staff       (20)      535 2023-04-05 08:42:48.000000 load-atoms-0.0.3/src/load_atoms/checksums.py
--rw-r--r--   0 john       (504) staff       (20)     2051 2023-04-05 08:42:48.000000 load-atoms-0.0.3/src/load_atoms/database.py
--rw-r--r--   0 john       (504) staff       (20)     3747 2023-04-05 06:56:03.000000 load-atoms-0.0.3/src/load_atoms/dataset.py
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.835744 load-atoms-0.0.3/src/load_atoms/datasets/
--rw-r--r--   0 john       (504) staff       (20)     1040 2023-04-06 09:55:36.000000 load-atoms-0.0.3/src/load_atoms/datasets/C-GAP-17.yaml
--rw-r--r--   0 john       (504) staff       (20)     1166 2023-04-06 09:55:23.000000 load-atoms-0.0.3/src/load_atoms/datasets/C-GAP-20.yaml
--rw-r--r--   0 john       (504) staff       (20)     1356 2023-03-07 08:55:19.000000 load-atoms-0.0.3/src/load_atoms/datasets/QM7.yaml
--rw-r--r--   0 john       (504) staff       (20)     1222 2023-03-07 16:02:25.000000 load-atoms-0.0.3/src/load_atoms/datasets/amorphous-grahpene.yaml
--rw-r--r--   0 john       (504) staff       (20)     1240 2023-02-18 11:49:24.000000 load-atoms-0.0.3/src/load_atoms/manipulations.py
--rw-r--r--   0 john       (504) staff       (20)     1618 2023-04-06 10:09:05.000000 load-atoms-0.0.3/src/load_atoms/util.py
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.834721 load-atoms-0.0.3/src/load_atoms.egg-info/
--rw-r--r--   0 john       (504) staff       (20)     2700 2023-04-06 10:09:45.000000 load-atoms-0.0.3/src/load_atoms.egg-info/PKG-INFO
--rw-r--r--   0 john       (504) staff       (20)      715 2023-04-06 10:09:45.000000 load-atoms-0.0.3/src/load_atoms.egg-info/SOURCES.txt
--rw-r--r--   0 john       (504) staff       (20)        1 2023-04-06 10:09:45.000000 load-atoms-0.0.3/src/load_atoms.egg-info/dependency_links.txt
--rw-r--r--   0 john       (504) staff       (20)      157 2023-04-06 10:09:45.000000 load-atoms-0.0.3/src/load_atoms.egg-info/requires.txt
--rw-r--r--   0 john       (504) staff       (20)       11 2023-04-06 10:09:45.000000 load-atoms-0.0.3/src/load_atoms.egg-info/top_level.txt
-drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:09:45.836996 load-atoms-0.0.3/tests/
--rw-r--r--   0 john       (504) staff       (20)     1581 2023-04-06 09:06:34.000000 load-atoms-0.0.3/tests/test_backend.py
--rw-r--r--   0 john       (504) staff       (20)     1965 2023-04-06 09:14:35.000000 load-atoms-0.0.3/tests/test_database.py
--rw-r--r--   0 john       (504) staff       (20)     2094 2023-04-06 09:14:52.000000 load-atoms-0.0.3/tests/test_dataset.py
--rw-r--r--   0 john       (504) staff       (20)      857 2023-04-05 06:56:03.000000 load-atoms-0.0.3/tests/test_manipulations.py
--rw-r--r--   0 john       (504) staff       (20)      441 2023-04-05 08:42:48.000000 load-atoms-0.0.3/tests/test_util.py
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.068783 load-atoms-0.0.4/
+-rw-r--r--   0 john       (504) staff       (20)     1069 2023-04-04 12:18:14.000000 load-atoms-0.0.4/LICENSE
+-rw-r--r--   0 john       (504) staff       (20)       48 2023-03-07 08:55:19.000000 load-atoms-0.0.4/MANIFEST.in
+-rw-r--r--   0 john       (504) staff       (20)     2700 2023-04-06 10:24:24.068623 load-atoms-0.0.4/PKG-INFO
+-rw-r--r--   0 john       (504) staff       (20)      905 2023-04-04 12:19:43.000000 load-atoms-0.0.4/README.md
+-rw-r--r--   0 john       (504) staff       (20)     1309 2023-04-06 10:24:18.000000 load-atoms-0.0.4/pyproject.toml
+-rw-r--r--   0 john       (504) staff       (20)       38 2023-04-06 10:24:24.068834 load-atoms-0.0.4/setup.cfg
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.061350 load-atoms-0.0.4/src/
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.063603 load-atoms-0.0.4/src/load_atoms/
+-rw-r--r--   0 john       (504) staff       (20)      127 2023-04-06 10:24:18.000000 load-atoms-0.0.4/src/load_atoms/__init__.py
+-rw-r--r--   0 john       (504) staff       (20)     1727 2023-04-05 06:56:03.000000 load-atoms-0.0.4/src/load_atoms/api.py
+-rw-r--r--   0 john       (504) staff       (20)     3304 2023-04-05 08:42:48.000000 load-atoms-0.0.4/src/load_atoms/backend.py
+-rw-r--r--   0 john       (504) staff       (20)      535 2023-04-05 08:42:48.000000 load-atoms-0.0.4/src/load_atoms/checksums.py
+-rw-r--r--   0 john       (504) staff       (20)     2051 2023-04-05 08:42:48.000000 load-atoms-0.0.4/src/load_atoms/database.py
+-rw-r--r--   0 john       (504) staff       (20)     3747 2023-04-05 06:56:03.000000 load-atoms-0.0.4/src/load_atoms/dataset.py
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.066578 load-atoms-0.0.4/src/load_atoms/datasets/
+-rw-r--r--   0 john       (504) staff       (20)     1040 2023-04-06 09:55:36.000000 load-atoms-0.0.4/src/load_atoms/datasets/C-GAP-17.yaml
+-rw-r--r--   0 john       (504) staff       (20)     1166 2023-04-06 10:23:16.000000 load-atoms-0.0.4/src/load_atoms/datasets/C-GAP-20.yaml
+-rw-r--r--   0 john       (504) staff       (20)     1356 2023-03-07 08:55:19.000000 load-atoms-0.0.4/src/load_atoms/datasets/QM7.yaml
+-rw-r--r--   0 john       (504) staff       (20)     1222 2023-03-07 16:02:25.000000 load-atoms-0.0.4/src/load_atoms/datasets/amorphous-grahpene.yaml
+-rw-r--r--   0 john       (504) staff       (20)     1240 2023-02-18 11:49:24.000000 load-atoms-0.0.4/src/load_atoms/manipulations.py
+-rw-r--r--   0 john       (504) staff       (20)     1618 2023-04-06 10:09:05.000000 load-atoms-0.0.4/src/load_atoms/util.py
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.065146 load-atoms-0.0.4/src/load_atoms.egg-info/
+-rw-r--r--   0 john       (504) staff       (20)     2700 2023-04-06 10:24:24.000000 load-atoms-0.0.4/src/load_atoms.egg-info/PKG-INFO
+-rw-r--r--   0 john       (504) staff       (20)      715 2023-04-06 10:24:24.000000 load-atoms-0.0.4/src/load_atoms.egg-info/SOURCES.txt
+-rw-r--r--   0 john       (504) staff       (20)        1 2023-04-06 10:24:24.000000 load-atoms-0.0.4/src/load_atoms.egg-info/dependency_links.txt
+-rw-r--r--   0 john       (504) staff       (20)      157 2023-04-06 10:24:24.000000 load-atoms-0.0.4/src/load_atoms.egg-info/requires.txt
+-rw-r--r--   0 john       (504) staff       (20)       11 2023-04-06 10:24:24.000000 load-atoms-0.0.4/src/load_atoms.egg-info/top_level.txt
+drwxr-xr-x   0 john       (504) staff       (20)        0 2023-04-06 10:24:24.068414 load-atoms-0.0.4/tests/
+-rw-r--r--   0 john       (504) staff       (20)     1581 2023-04-06 09:06:34.000000 load-atoms-0.0.4/tests/test_backend.py
+-rw-r--r--   0 john       (504) staff       (20)     1965 2023-04-06 09:14:35.000000 load-atoms-0.0.4/tests/test_database.py
+-rw-r--r--   0 john       (504) staff       (20)     2094 2023-04-06 09:14:52.000000 load-atoms-0.0.4/tests/test_dataset.py
+-rw-r--r--   0 john       (504) staff       (20)      857 2023-04-05 06:56:03.000000 load-atoms-0.0.4/tests/test_manipulations.py
+-rw-r--r--   0 john       (504) staff       (20)      441 2023-04-05 08:42:48.000000 load-atoms-0.0.4/tests/test_util.py
```

### Comparing `load-atoms-0.0.3/LICENSE` & `load-atoms-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/PKG-INFO` & `load-atoms-0.0.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: load-atoms
-Version: 0.0.3
+Version: 0.0.4
 Summary: Large Open Access Datasets for Atomistic Materials Science (LOAD-AtoMS)
 Author-email: John Gardner <gardner.john97@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 John Gardner
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `load-atoms-0.0.3/README.md` & `load-atoms-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/pyproject.toml` & `load-atoms-0.0.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "load-atoms"
-version = "0.0.3"
+version = "0.0.4"
 description = "Large Open Access Datasets for Atomistic Materials Science (LOAD-AtoMS)"
 readme = "README.md"
 authors = [{ name = "John Gardner", email = "gardner.john97@gmail.com" }]
 license = { file = "LICENSE" }
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
@@ -35,15 +35,15 @@
     "twine",
 ]
 
 [project.urls]
 Homepage = "https://github.com/jla-gardner/load-atoms"
 
 [tool.bumpver]
-current_version = "0.0.3"
+current_version = "0.0.4"
 version_pattern = "MAJOR.MINOR.PATCH"
 commit_message = "Bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 push = false
 
 [tool.bumpver.file_patterns]
```

### Comparing `load-atoms-0.0.3/src/load_atoms/api.py` & `load-atoms-0.0.4/src/load_atoms/api.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/backend.py` & `load-atoms-0.0.4/src/load_atoms/backend.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/checksums.py` & `load-atoms-0.0.4/src/load_atoms/checksums.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/database.py` & `load-atoms-0.0.4/src/load_atoms/database.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/dataset.py` & `load-atoms-0.0.4/src/load_atoms/dataset.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/datasets/C-GAP-17.yaml` & `load-atoms-0.0.4/src/load_atoms/datasets/C-GAP-17.yaml`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/datasets/C-GAP-20.yaml` & `load-atoms-0.0.4/src/load_atoms/datasets/C-GAP-20.yaml`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 name: C-GAP-20
 files:
-    C-GAP-20.extxyz: 3dca8e9f9707
+    C-GAP-20.extxyz: 1b4152e17aa2
 description: |
     Complete dataset and labels used for training both the C-GAP-20
     and C-GAP-20-U models. 
     For details, see here https://doi.org/10.17863/CAM.54529 
     and https://doi.org/10.17863/CAM.82086
 citation: |
     @article{Rowe-20-07,
```

### Comparing `load-atoms-0.0.3/src/load_atoms/datasets/QM7.yaml` & `load-atoms-0.0.4/src/load_atoms/datasets/QM7.yaml`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/datasets/amorphous-grahpene.yaml` & `load-atoms-0.0.4/src/load_atoms/datasets/amorphous-grahpene.yaml`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/manipulations.py` & `load-atoms-0.0.4/src/load_atoms/manipulations.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms/util.py` & `load-atoms-0.0.4/src/load_atoms/util.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/src/load_atoms.egg-info/PKG-INFO` & `load-atoms-0.0.4/src/load_atoms.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: load-atoms
-Version: 0.0.3
+Version: 0.0.4
 Summary: Large Open Access Datasets for Atomistic Materials Science (LOAD-AtoMS)
 Author-email: John Gardner <gardner.john97@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 John Gardner
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `load-atoms-0.0.3/src/load_atoms.egg-info/SOURCES.txt` & `load-atoms-0.0.4/src/load_atoms.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/tests/test_backend.py` & `load-atoms-0.0.4/tests/test_backend.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/tests/test_database.py` & `load-atoms-0.0.4/tests/test_database.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/tests/test_dataset.py` & `load-atoms-0.0.4/tests/test_dataset.py`

 * *Files identical despite different names*

### Comparing `load-atoms-0.0.3/tests/test_manipulations.py` & `load-atoms-0.0.4/tests/test_manipulations.py`

 * *Files identical despite different names*

