# Comparing `tmp/scikit-hep-5.1.0.tar.gz` & `tmp/scikit-hep-5.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "scikit-hep-5.1.0.tar", last modified: Mon Apr  3 08:46:02 2023, max compression
+gzip compressed data, was "scikit-hep-5.1.1.tar", last modified: Thu Apr  6 16:23:28 2023, max compression
```

## Comparing `scikit-hep-5.1.0.tar` & `scikit-hep-5.1.1.tar`

### file list

```diff
@@ -1,38 +1,38 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.524890 scikit-hep-5.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/.zenodo.json
--rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5226 2023-04-03 08:46:02.524890 scikit-hep-5.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4111 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)      418 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.520890 scikit-hep-5.1.0/scikit_hep.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5226 2023-04-03 08:46:02.000000 scikit-hep-5.1.0/scikit_hep.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-03 08:46:02.000000 scikit-hep-5.1.0/scikit_hep.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 08:46:02.000000 scikit-hep-5.1.0/scikit_hep.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-03 08:46:02.000000 scikit-hep-5.1.0/scikit_hep.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-03 08:46:02.000000 scikit-hep-5.1.0/scikit_hep.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-04-03 08:46:02.524890 scikit-hep-5.1.0/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)      393 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.520890 scikit-hep-5.1.0/skhep/
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.520890 scikit-hep-5.1.0/skhep/math/
--rw-r--r--   0 runner    (1001) docker     (123)      515 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    23635 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/geometry.py
--rw-r--r--   0 runner    (1001) docker     (123)     3995 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/isclose.py
--rw-r--r--   0 runner    (1001) docker     (123)     4650 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/kinematics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/numeric.py
--rw-r--r--   0 runner    (1001) docker     (123)    34867 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/math/vectors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.520890 scikit-hep-5.1.0/skhep/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      167 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2252 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/utils/_show_versions.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/skhep/utils/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.520890 scikit-hep-5.1.0/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.524890 scikit-hep-5.1.0/tests/math/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/tests/math/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6995 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/tests/math/test_geometry.py
--rw-r--r--   0 runner    (1001) docker     (123)     1538 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/tests/math/test_kinematics.py
--rw-r--r--   0 runner    (1001) docker     (123)    17470 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/tests/math/test_vectors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 08:46:02.524890 scikit-hep-5.1.0/tests/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-03 08:45:53.000000 scikit-hep-5.1.0/tests/utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/.zenodo.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5226 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4111 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      418 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.837278 scikit-hep-5.1.1/scikit_hep.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5226 2023-04-06 16:23:28.000000 scikit-hep-5.1.1/scikit_hep.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-06 16:23:28.000000 scikit-hep-5.1.1/scikit_hep.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:23:28.000000 scikit-hep-5.1.1/scikit_hep.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-06 16:23:28.000000 scikit-hep-5.1.1/scikit_hep.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 16:23:28.000000 scikit-hep-5.1.1/scikit_hep.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)      393 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/skhep/
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/skhep/math/
+-rw-r--r--   0 runner    (1001) docker     (123)      515 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    23635 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3995 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/isclose.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4650 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/kinematics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/numeric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34867 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/math/vectors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/skhep/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      167 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2252 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/utils/_show_versions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/skhep/utils/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.837278 scikit-hep-5.1.1/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/tests/math/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/tests/math/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6995 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/tests/math/test_geometry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1538 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/tests/math/test_kinematics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17470 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/tests/math/test_vectors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:23:28.841278 scikit-hep-5.1.1/tests/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 16:23:16.000000 scikit-hep-5.1.1/tests/utils/__init__.py
```

### Comparing `scikit-hep-5.1.0/.zenodo.json` & `scikit-hep-5.1.1/.zenodo.json`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/LICENSE` & `scikit-hep-5.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/PKG-INFO` & `scikit-hep-5.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scikit-hep
-Version: 5.1.0
+Version: 5.1.1
 Summary: Metapackage of Scikit-HEP project libraries for Particle Physics.
 Home-page: https://github.com/scikit-hep/scikit-hep/
 Author: the scikit-hep admins
 Author-email: scikit-hep-admins@googlegroups.com
 License: BSD 3-Clause License
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
```

### Comparing `scikit-hep-5.1.0/README.rst` & `scikit-hep-5.1.1/README.rst`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/scikit_hep.egg-info/PKG-INFO` & `scikit-hep-5.1.1/scikit_hep.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scikit-hep
-Version: 5.1.0
+Version: 5.1.1
 Summary: Metapackage of Scikit-HEP project libraries for Particle Physics.
 Home-page: https://github.com/scikit-hep/scikit-hep/
 Author: the scikit-hep admins
 Author-email: scikit-hep-admins@googlegroups.com
 License: BSD 3-Clause License
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
```

### Comparing `scikit-hep-5.1.0/scikit_hep.egg-info/SOURCES.txt` & `scikit-hep-5.1.1/scikit_hep.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/setup.cfg` & `scikit-hep-5.1.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/__init__.py` & `scikit-hep-5.1.1/skhep/__init__.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/__init__.py` & `scikit-hep-5.1.1/skhep/math/__init__.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/geometry.py` & `scikit-hep-5.1.1/skhep/math/geometry.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/isclose.py` & `scikit-hep-5.1.1/skhep/math/isclose.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/kinematics.py` & `scikit-hep-5.1.1/skhep/math/kinematics.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/numeric.py` & `scikit-hep-5.1.1/skhep/math/numeric.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/math/vectors.py` & `scikit-hep-5.1.1/skhep/math/vectors.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/utils/_show_versions.py` & `scikit-hep-5.1.1/skhep/utils/_show_versions.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/skhep/utils/exceptions.py` & `scikit-hep-5.1.1/skhep/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/tests/math/test_geometry.py` & `scikit-hep-5.1.1/tests/math/test_geometry.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/tests/math/test_kinematics.py` & `scikit-hep-5.1.1/tests/math/test_kinematics.py`

 * *Files identical despite different names*

### Comparing `scikit-hep-5.1.0/tests/math/test_vectors.py` & `scikit-hep-5.1.1/tests/math/test_vectors.py`

 * *Files identical despite different names*

