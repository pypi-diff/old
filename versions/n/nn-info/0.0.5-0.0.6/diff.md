# Comparing `tmp/nn_info-0.0.5.tar.gz` & `tmp/nn_info-0.0.6.tar.gz`

## Comparing `nn_info-0.0.5.tar` & `nn_info-0.0.6.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0   635751 2020-02-02 00:00:00.000000 nn_info-0.0.5/src/.ipynb_checkpoints/examples_notebook-checkpoint.ipynb
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 nn_info-0.0.5/src/nn_info/__init__.py
--rw-r--r--   0        0        0     8665 2020-02-02 00:00:00.000000 nn_info-0.0.5/src/nn_info/estimators.py
--rw-r--r--   0        0        0     4776 2020-02-02 00:00:00.000000 nn_info-0.0.5/src/nn_info/nn_info.py
--rw-r--r--   0        0        0     1059 2020-02-02 00:00:00.000000 nn_info-0.0.5/LICENSE
--rw-r--r--   0        0        0      508 2020-02-02 00:00:00.000000 nn_info-0.0.5/README.md
--rw-r--r--   0        0        0      600 2020-02-02 00:00:00.000000 nn_info-0.0.5/pyproject.toml
--rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 nn_info-0.0.5/PKG-INFO
+-rw-r--r--   0        0        0   635751 2020-02-02 00:00:00.000000 nn_info-0.0.6/src/.ipynb_checkpoints/examples_notebook-checkpoint.ipynb
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 nn_info-0.0.6/src/nn_info/__init__.py
+-rw-r--r--   0        0        0     8665 2020-02-02 00:00:00.000000 nn_info-0.0.6/src/nn_info/estimators.py
+-rw-r--r--   0        0        0     4776 2020-02-02 00:00:00.000000 nn_info-0.0.6/src/nn_info/theory.py
+-rw-r--r--   0        0        0     1059 2020-02-02 00:00:00.000000 nn_info-0.0.6/LICENSE
+-rw-r--r--   0        0        0      508 2020-02-02 00:00:00.000000 nn_info-0.0.6/README.md
+-rw-r--r--   0        0        0      600 2020-02-02 00:00:00.000000 nn_info-0.0.6/pyproject.toml
+-rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 nn_info-0.0.6/PKG-INFO
```

### Comparing `nn_info-0.0.5/src/.ipynb_checkpoints/examples_notebook-checkpoint.ipynb` & `nn_info-0.0.6/src/.ipynb_checkpoints/examples_notebook-checkpoint.ipynb`

 * *Files identical despite different names*

### Comparing `nn_info-0.0.5/src/nn_info/estimators.py` & `nn_info-0.0.6/src/nn_info/estimators.py`

 * *Files identical despite different names*

### Comparing `nn_info-0.0.5/src/nn_info/nn_info.py` & `nn_info-0.0.6/src/nn_info/theory.py`

 * *Files identical despite different names*

### Comparing `nn_info-0.0.5/LICENSE` & `nn_info-0.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `nn_info-0.0.5/pyproject.toml` & `nn_info-0.0.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 [project]
 name = "nn_info"
-version = "0.0.5"
+version = "0.0.6"
 authors = [
   { name="Bettina Schmidt", email="bettina.schmidt@charite.de" },
 ]
 description = "nearest neighbor based estimators for measures of information theory"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `nn_info-0.0.5/PKG-INFO` & `nn_info-0.0.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nn_info
-Version: 0.0.5
+Version: 0.0.6
 Summary: nearest neighbor based estimators for measures of information theory
 Project-URL: Homepage, https://github.com/zuiop11/nn_info
 Project-URL: Bug Tracker, https://github.com/zuiop11/nn_info
 Author-email: Bettina Schmidt <bettina.schmidt@charite.de>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

