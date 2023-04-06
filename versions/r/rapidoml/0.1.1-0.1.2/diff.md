# Comparing `tmp/rapidoml-0.1.1.tar.gz` & `tmp/rapidoml-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rapidoml-0.1.1.tar", last modified: Thu Apr  6 20:00:57 2023, max compression
+gzip compressed data, was "rapidoml-0.1.2.tar", last modified: Thu Apr  6 21:21:37 2023, max compression
```

## Comparing `rapidoml-0.1.1.tar` & `rapidoml-0.1.2.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.307121 rapidoml-0.1.1/
--rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 19:03:37.000000 rapidoml-0.1.1/LICENSE
--rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 20:00:57.306719 rapidoml-0.1.1/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)     3436 2023-04-06 19:36:05.000000 rapidoml-0.1.1/README.md
--rw-r--r--   0 fcarva844   (501) staff       (20)      890 2023-04-06 20:00:00.000000 rapidoml-0.1.1/pyproject.toml
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.302202 rapidoml-0.1.1/rapidoml.egg-info/
--rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)      292 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/SOURCES.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/dependency_links.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       62 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/requires.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        6 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/top_level.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 20:00:57.307247 rapidoml-0.1.1/setup.cfg
--rw-r--r--   0 fcarva844   (501) staff       (20)     1024 2023-04-06 20:00:19.000000 rapidoml-0.1.1/setup.py
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.305684 rapidoml-0.1.1/tests/
--rw-r--r--   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:22:30.000000 rapidoml-0.1.1/tests/__init__.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      835 2023-04-06 19:39:26.000000 rapidoml-0.1.1/tests/test_datasets.py
--rw-r--r--   0 fcarva844   (501) staff       (20)     1014 2023-04-06 19:39:48.000000 rapidoml-0.1.1/tests/test_preprocessing.py
--rw-r--r--   0 fcarva844   (501) staff       (20)     1531 2023-04-06 19:51:21.000000 rapidoml-0.1.1/tests/test_rapidoml.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 21:21:37.336117 rapidoml-0.1.2/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 19:03:37.000000 rapidoml-0.1.2/LICENSE
+-rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 21:21:37.335526 rapidoml-0.1.2/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)     3436 2023-04-06 19:36:05.000000 rapidoml-0.1.2/README.md
+-rw-r--r--   0 fcarva844   (501) staff       (20)      890 2023-04-06 21:20:20.000000 rapidoml-0.1.2/pyproject.toml
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 21:21:37.329882 rapidoml-0.1.2/rapidoml.egg-info/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 21:21:37.000000 rapidoml-0.1.2/rapidoml.egg-info/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)      292 2023-04-06 21:21:37.000000 rapidoml-0.1.2/rapidoml.egg-info/SOURCES.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 21:21:37.000000 rapidoml-0.1.2/rapidoml.egg-info/dependency_links.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       62 2023-04-06 21:21:37.000000 rapidoml-0.1.2/rapidoml.egg-info/requires.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        6 2023-04-06 21:21:37.000000 rapidoml-0.1.2/rapidoml.egg-info/top_level.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 21:21:37.336270 rapidoml-0.1.2/setup.cfg
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1024 2023-04-06 21:20:17.000000 rapidoml-0.1.2/setup.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 21:21:37.334595 rapidoml-0.1.2/tests/
+-rw-r--r--   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:22:30.000000 rapidoml-0.1.2/tests/__init__.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1144 2023-04-06 20:40:23.000000 rapidoml-0.1.2/tests/test_datasets.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1007 2023-04-06 20:10:55.000000 rapidoml-0.1.2/tests/test_preprocessing.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      960 2023-04-06 20:48:41.000000 rapidoml-0.1.2/tests/test_rapidoml.py
```

### Comparing `rapidoml-0.1.1/LICENSE` & `rapidoml-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.1/PKG-INFO` & `rapidoml-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidoml
-Version: 0.1.1
+Version: 0.1.2
 Summary: RapidoML is a simple Automated Machine Learning (AutoML) library
 Home-page: https://github.com/hipnologo/rapidoml
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `rapidoml-0.1.1/README.md` & `rapidoml-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.1/pyproject.toml` & `rapidoml-0.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "rapidoml"
-version = "0.1.1"
+version = "0.1.2"
 description = "RapidoML is a simple Automated Machine Learning (AutoML) library"
 authors = [
   { name="Fabio Carvalho", email="hipnologo@gmail.com" },
 ]
 readme = "README.md"
 keywords = ["documentation", "python"]
 classifiers = [
```

### Comparing `rapidoml-0.1.1/rapidoml.egg-info/PKG-INFO` & `rapidoml-0.1.2/rapidoml.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidoml
-Version: 0.1.1
+Version: 0.1.2
 Summary: RapidoML is a simple Automated Machine Learning (AutoML) library
 Home-page: https://github.com/hipnologo/rapidoml
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `rapidoml-0.1.1/setup.py` & `rapidoml-0.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name="rapidoml",
-    version="0.1.1",
+    version="0.1.2",
     packages=find_packages(),
     install_requires=[
         "numpy",
         "scikit-learn",
         "tensorflow",
         "keras",
         "xgboost",
```

### Comparing `rapidoml-0.1.1/tests/test_preprocessing.py` & `rapidoml-0.1.2/tests/test_preprocessing.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import unittest
 import pandas as pd
 import numpy as np
 from rapidoml.preprocessing import preprocess_data
 
+
 class TestPreprocessing(unittest.TestCase):
     def test_preprocess_data_categorical(self):
         data = {'category': ['A', 'B', 'A', 'C']}
         df = pd.DataFrame(data)
         df_processed = preprocess_data(df, categorical_columns=['category'])
         self.assertEqual(df_processed['category'].nunique(), 3)
 
@@ -16,11 +17,11 @@
         df_processed = preprocess_data(df, numerical_columns=['value'])
         self.assertAlmostEqual(np.mean(df_processed['value']), 0.0, delta=1e-6)
 
     def test_preprocess_data_invalid_scaling_method(self):
         data = {'value': [1, 2, 3, 4, 5, 6]}
         df = pd.DataFrame(data)
         with self.assertRaises(ValueError):
-            preprocess_data(df, numerical_columns=['value'], scaling_method='unknown')
+            preprocess_data(df, numerical_columns=['value'], scaler='unknown')
 
 if __name__ == '__main__':
     unittest.main()
```

