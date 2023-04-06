# Comparing `tmp/rapidoml-0.1.0.tar.gz` & `tmp/rapidoml-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rapidoml-0.1.0.tar", last modified: Thu Apr  6 19:41:09 2023, max compression
+gzip compressed data, was "rapidoml-0.1.1.tar", last modified: Thu Apr  6 20:00:57 2023, max compression
```

## Comparing `rapidoml-0.1.0.tar` & `rapidoml-0.1.1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:41:09.159863 rapidoml-0.1.0/
--rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 19:03:37.000000 rapidoml-0.1.0/LICENSE
--rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 19:41:09.158971 rapidoml-0.1.0/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)     3436 2023-04-06 19:36:05.000000 rapidoml-0.1.0/README.md
--rw-r--r--   0 fcarva844   (501) staff       (20)      890 2023-04-06 19:35:42.000000 rapidoml-0.1.0/pyproject.toml
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:41:09.149039 rapidoml-0.1.0/rapidoml.egg-info/
--rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 19:41:08.000000 rapidoml-0.1.0/rapidoml.egg-info/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)      292 2023-04-06 19:41:09.000000 rapidoml-0.1.0/rapidoml.egg-info/SOURCES.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 19:41:08.000000 rapidoml-0.1.0/rapidoml.egg-info/dependency_links.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       62 2023-04-06 19:41:08.000000 rapidoml-0.1.0/rapidoml.egg-info/requires.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        6 2023-04-06 19:41:08.000000 rapidoml-0.1.0/rapidoml.egg-info/top_level.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 19:41:09.160168 rapidoml-0.1.0/setup.cfg
--rw-r--r--   0 fcarva844   (501) staff       (20)     1024 2023-04-06 19:35:27.000000 rapidoml-0.1.0/setup.py
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:41:09.152791 rapidoml-0.1.0/tests/
--rw-r--r--   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:22:30.000000 rapidoml-0.1.0/tests/__init__.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      835 2023-04-06 19:39:26.000000 rapidoml-0.1.0/tests/test_datasets.py
--rw-r--r--   0 fcarva844   (501) staff       (20)     1014 2023-04-06 19:39:48.000000 rapidoml-0.1.0/tests/test_preprocessing.py
--rw-r--r--   0 fcarva844   (501) staff       (20)     1525 2023-04-06 19:19:26.000000 rapidoml-0.1.0/tests/test_rapidoml.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.307121 rapidoml-0.1.1/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 19:03:37.000000 rapidoml-0.1.1/LICENSE
+-rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 20:00:57.306719 rapidoml-0.1.1/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)     3436 2023-04-06 19:36:05.000000 rapidoml-0.1.1/README.md
+-rw-r--r--   0 fcarva844   (501) staff       (20)      890 2023-04-06 20:00:00.000000 rapidoml-0.1.1/pyproject.toml
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.302202 rapidoml-0.1.1/rapidoml.egg-info/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    17286 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)      292 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/SOURCES.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/dependency_links.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       62 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/requires.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        6 2023-04-06 20:00:57.000000 rapidoml-0.1.1/rapidoml.egg-info/top_level.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 20:00:57.307247 rapidoml-0.1.1/setup.cfg
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1024 2023-04-06 20:00:19.000000 rapidoml-0.1.1/setup.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 20:00:57.305684 rapidoml-0.1.1/tests/
+-rw-r--r--   0 fcarva844   (501) staff       (20)        0 2023-04-06 19:22:30.000000 rapidoml-0.1.1/tests/__init__.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      835 2023-04-06 19:39:26.000000 rapidoml-0.1.1/tests/test_datasets.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1014 2023-04-06 19:39:48.000000 rapidoml-0.1.1/tests/test_preprocessing.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1531 2023-04-06 19:51:21.000000 rapidoml-0.1.1/tests/test_rapidoml.py
```

### Comparing `rapidoml-0.1.0/LICENSE` & `rapidoml-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.0/PKG-INFO` & `rapidoml-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidoml
-Version: 0.1.0
+Version: 0.1.1
 Summary: RapidoML is a simple Automated Machine Learning (AutoML) library
 Home-page: https://github.com/hipnologo/rapidoml
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `rapidoml-0.1.0/README.md` & `rapidoml-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.0/pyproject.toml` & `rapidoml-0.1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "rapidoml"
-version = "0.1.0"
+version = "0.1.1"
 description = "RapidoML is a simple Automated Machine Learning (AutoML) library"
 authors = [
   { name="Fabio Carvalho", email="hipnologo@gmail.com" },
 ]
 readme = "README.md"
 keywords = ["documentation", "python"]
 classifiers = [
```

### Comparing `rapidoml-0.1.0/rapidoml.egg-info/PKG-INFO` & `rapidoml-0.1.1/rapidoml.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidoml
-Version: 0.1.0
+Version: 0.1.1
 Summary: RapidoML is a simple Automated Machine Learning (AutoML) library
 Home-page: https://github.com/hipnologo/rapidoml
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `rapidoml-0.1.0/setup.py` & `rapidoml-0.1.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name="rapidoml",
-    version="0.1.0",
+    version="0.1.1",
     packages=find_packages(),
     install_requires=[
         "numpy",
         "scikit-learn",
         "tensorflow",
         "keras",
         "xgboost",
```

### Comparing `rapidoml-0.1.0/tests/test_datasets.py` & `rapidoml-0.1.1/tests/test_datasets.py`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.0/tests/test_preprocessing.py` & `rapidoml-0.1.1/tests/test_preprocessing.py`

 * *Files identical despite different names*

### Comparing `rapidoml-0.1.0/tests/test_rapidoml.py` & `rapidoml-0.1.1/tests/test_rapidoml.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,44 +1,44 @@
 import unittest
 import pandas as pd
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import accuracy_score
 
-import flashml
-from flashml.datasets import sample_datasets
+import rapidoml
+from rapidoml.datasets import sample_datasets
 
-class TestFlashML(unittest.TestCase):
+class TestRapidoML(unittest.TestCase):
 
     def test_sample_datasets(self):
         df_train, df_test = sample_datasets('iris')
         self.assertIsInstance(df_train, pd.DataFrame)
         self.assertIsInstance(df_test, pd.DataFrame)
 
     def test_automl_iris(self):
         df_train, df_test = sample_datasets('iris')
         X_train, y_train = df_train.drop('target', axis=1), df_train['target']
         X_test, y_test = df_test.drop('target', axis=1), df_test['target']
         
-        automl = flashml.AutoML()
+        automl = rapidoml.AutoML()
         automl.train(X_train, y_train)
         y_pred = automl.predict(X_test)
         accuracy = accuracy_score(y_test, y_pred)
         
         self.assertGreater(accuracy, 0.8)
 
     def test_automl_save_and_load(self):
         df_train, df_test = sample_datasets('iris')
         X_train, y_train = df_train.drop('target', axis=1), df_train['target']
         X_test, y_test = df_test.drop('target', axis=1), df_test['target']
         
-        automl = flashml.AutoML()
+        automl = rapidoml.AutoML()
         automl.train(X_train, y_train)
         
         automl.save("test_model.pkl")
-        loaded_automl = flashml.AutoML.load("test_model.pkl")
+        loaded_automl = rapidoml.AutoML.load("test_model.pkl")
         y_pred = loaded_automl.predict(X_test)
         accuracy = accuracy_score(y_test, y_pred)
         
         self.assertGreater(accuracy, 0.8)
 
 if __name__ == '__main__':
     unittest.main()
```

