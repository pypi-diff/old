# Comparing `tmp/pyNNRW-0.3.1.tar.gz` & `tmp/pyNNRW-0.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyNNRW-0.3.1.tar", last modified: Fri Oct 14 10:10:00 2022, max compression
+gzip compressed data, was "pyNNRW-0.3.2.tar", last modified: Fri Apr  7 01:48:53 2023, max compression
```

## Comparing `pyNNRW-0.3.1.tar` & `pyNNRW-0.3.2.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxrwx   0        0        0        0 2022-10-14 10:10:00.888346 pyNNRW-0.3.1/
--rw-rw-rw-   0        0        0      214 2022-03-26 07:50:46.000000 pyNNRW-0.3.1/LICENCE
--rw-rw-rw-   0        0        0     4106 2022-10-14 10:10:00.888346 pyNNRW-0.3.1/PKG-INFO
--rw-rw-rw-   0        0        0     3458 2022-05-10 04:41:05.000000 pyNNRW-0.3.1/README.md
--rw-rw-rw-   0        0        0      108 2022-01-07 07:21:30.000000 pyNNRW-0.3.1/pyproject.toml
--rw-rw-rw-   0        0        0      906 2022-10-14 10:10:00.889344 pyNNRW-0.3.1/setup.cfg
-drwxrwxrwx   0        0        0        0 2022-10-14 10:10:00.705546 pyNNRW-0.3.1/src/
-drwxrwxrwx   0        0        0        0 2022-10-14 10:10:00.874779 pyNNRW-0.3.1/src/pyNNRW/
--rw-rw-rw-   0        0        0     2022 2022-10-14 00:56:18.000000 pyNNRW-0.3.1/src/pyNNRW/__init__.py
--rw-rw-rw-   0        0        0      239 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/aerw.py
--rw-rw-rw-   0        0        0      777 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/dtc.py
--rw-rw-rw-   0        0        0    17243 2022-10-14 01:00:40.000000 pyNNRW-0.3.1/src/pyNNRW/elm.py
--rw-rw-rw-   0        0        0      128 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/knn.py
--rw-rw-rw-   0        0        0    12946 2022-09-08 05:18:51.000000 pyNNRW-0.3.1/src/pyNNRW/knnrw.py
--rw-rw-rw-   0        0        0      509 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/lr.py
--rw-rw-rw-   0        0        0     7233 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/mlp.py
--rw-rw-rw-   0        0        0    22081 2022-10-14 09:17:58.000000 pyNNRW-0.3.1/src/pyNNRW/nnrw.py
--rw-rw-rw-   0        0        0     8033 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/rbfnn.py
--rw-rw-rw-   0        0        0     8632 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/rbm.py
--rw-rw-rw-   0        0        0     8104 2022-10-14 01:25:50.000000 pyNNRW-0.3.1/src/pyNNRW/rvfl.py
--rw-rw-rw-   0        0        0     1436 2022-05-20 11:56:20.000000 pyNNRW-0.3.1/src/pyNNRW/wann.py
-drwxrwxrwx   0        0        0        0 2022-10-14 10:10:00.887376 pyNNRW-0.3.1/src/pyNNRW.egg-info/
--rw-rw-rw-   0        0        0     4106 2022-10-14 10:10:00.000000 pyNNRW-0.3.1/src/pyNNRW.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      457 2022-10-14 10:10:00.000000 pyNNRW-0.3.1/src/pyNNRW.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-10-14 10:10:00.000000 pyNNRW-0.3.1/src/pyNNRW.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       30 2022-10-14 10:10:00.000000 pyNNRW-0.3.1/src/pyNNRW.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2022-10-14 10:10:00.000000 pyNNRW-0.3.1/src/pyNNRW.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 01:48:53.660940 pyNNRW-0.3.2/
+-rw-rw-rw-   0        0        0      214 2022-03-26 07:50:46.000000 pyNNRW-0.3.2/LICENCE
+-rw-rw-rw-   0        0        0     4106 2023-04-07 01:48:53.660940 pyNNRW-0.3.2/PKG-INFO
+-rw-rw-rw-   0        0        0     3458 2022-05-10 04:41:05.000000 pyNNRW-0.3.2/README.md
+-rw-rw-rw-   0        0        0      108 2022-01-07 07:21:30.000000 pyNNRW-0.3.2/pyproject.toml
+-rw-rw-rw-   0        0        0      906 2023-04-07 01:48:53.663935 pyNNRW-0.3.2/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 01:48:53.263125 pyNNRW-0.3.2/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 01:48:53.632193 pyNNRW-0.3.2/src/pyNNRW/
+-rw-rw-rw-   0        0        0     2044 2023-04-07 01:47:56.000000 pyNNRW-0.3.2/src/pyNNRW/__init__.py
+-rw-rw-rw-   0        0        0      239 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/aerw.py
+-rw-rw-rw-   0        0        0      777 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/dtc.py
+-rw-rw-rw-   0        0        0    17243 2022-10-14 01:00:40.000000 pyNNRW-0.3.2/src/pyNNRW/elm.py
+-rw-rw-rw-   0        0        0      128 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/knn.py
+-rw-rw-rw-   0        0        0    12946 2022-09-08 05:18:51.000000 pyNNRW-0.3.2/src/pyNNRW/knnrw.py
+-rw-rw-rw-   0        0        0      509 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/lr.py
+-rw-rw-rw-   0        0        0     7233 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/mlp.py
+-rw-rw-rw-   0        0        0    22081 2022-10-14 09:17:58.000000 pyNNRW-0.3.2/src/pyNNRW/nnrw.py
+-rw-rw-rw-   0        0        0     8033 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/rbfnn.py
+-rw-rw-rw-   0        0        0     8632 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/rbm.py
+-rw-rw-rw-   0        0        0     8361 2023-04-07 01:09:38.000000 pyNNRW-0.3.2/src/pyNNRW/rvfl.py
+-rw-rw-rw-   0        0        0     1436 2022-05-20 11:56:20.000000 pyNNRW-0.3.2/src/pyNNRW/wann.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:48:53.658929 pyNNRW-0.3.2/src/pyNNRW.egg-info/
+-rw-rw-rw-   0        0        0     4106 2023-04-07 01:48:53.000000 pyNNRW-0.3.2/src/pyNNRW.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      457 2023-04-07 01:48:53.000000 pyNNRW-0.3.2/src/pyNNRW.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:48:53.000000 pyNNRW-0.3.2/src/pyNNRW.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       30 2023-04-07 01:48:53.000000 pyNNRW-0.3.2/src/pyNNRW.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 01:48:53.000000 pyNNRW-0.3.2/src/pyNNRW.egg-info/top_level.txt
```

### Comparing `pyNNRW-0.3.1/PKG-INFO` & `pyNNRW-0.3.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyNNRW
-Version: 0.3.1
+Version: 0.3.2
 Summary: A Python library for NNRW (neural network with random weights)
 Home-page: https://github.com/zhangys11/pyNNRW
 Author: Yinsheng Zhang (Ph.D.)
 Author-email: oo@zju.edu.cn
 Project-URL: Bug Tracker, https://github.com/zhangys11/pyNNRW/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
```

### Comparing `pyNNRW-0.3.1/README.md` & `pyNNRW-0.3.2/README.md`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/setup.cfg` & `pyNNRW-0.3.2/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2070 794e 4e52 570d 0a76 6572 7369   = pyNNRW..versi
-00000020: 6f6e 203d 2030 2e33 2e31 0d0a 6175 7468  on = 0.3.1..auth
+00000020: 6f6e 203d 2030 2e33 2e32 0d0a 6175 7468  on = 0.3.2..auth
 00000030: 6f72 203d 2059 696e 7368 656e 6720 5a68  or = Yinsheng Zh
 00000040: 616e 6720 2850 682e 442e 290d 0a61 7574  ang (Ph.D.)..aut
 00000050: 686f 725f 656d 6169 6c20 3d20 6f6f 407a  hor_email = oo@z
 00000060: 6a75 2e65 6475 2e63 6e0d 0a64 6573 6372  ju.edu.cn..descr
 00000070: 6970 7469 6f6e 203d 2041 2050 7974 686f  iption = A Pytho
 00000080: 6e20 6c69 6272 6172 7920 666f 7220 4e4e  n library for NN
 00000090: 5257 2028 6e65 7572 616c 206e 6574 776f  RW (neural netwo
```

### Comparing `pyNNRW-0.3.1/src/pyNNRW/__init__.py` & `pyNNRW-0.3.2/src/pyNNRW/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,13 @@
 
 import importlib.metadata
 __version__ = importlib.metadata.version('pyNNRW')
 
+import numpy as np
+
 def to_categorical(y, num_classes=None, dtype="float32"):
     """
     This function is copied from keras.
 
     Converts a class vector (integers) to binary class matrix.
 
     E.g. for use with `categorical_crossentropy`.
```

### Comparing `pyNNRW-0.3.1/src/pyNNRW/dtc.py` & `pyNNRW-0.3.2/src/pyNNRW/dtc.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/elm.py` & `pyNNRW-0.3.2/src/pyNNRW/elm.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/knnrw.py` & `pyNNRW-0.3.2/src/pyNNRW/knnrw.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/mlp.py` & `pyNNRW-0.3.2/src/pyNNRW/mlp.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/nnrw.py` & `pyNNRW-0.3.2/src/pyNNRW/nnrw.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/rbfnn.py` & `pyNNRW-0.3.2/src/pyNNRW/rbfnn.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/rbm.py` & `pyNNRW-0.3.2/src/pyNNRW/rbm.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW/rvfl.py` & `pyNNRW-0.3.2/src/pyNNRW/rvfl.py`

 * *Files 9% similar despite different names*

```diff
@@ -158,32 +158,38 @@
     '''
     def __init__(self, n_hidden_nodes = 20, activation = 'sigmoid'):
 
         self.n_hidden_nodes = n_hidden_nodes
         self.activation = activation
 
     def fit(self, X, y):     
-        self.model = RVFL(hidden_nodes=self.n_hidden_nodes, 
-                random_type="uniform", 
-                activation_name=self.activation, 
+        self.model = RVFL(hidden_nodes=self.n_hidden_nodes,
+                random_type="uniform",
+                activation_name=self.activation,
                 type="classification")
         self.model.fit(X, y)        
         self.classes_ = np.unique(y) # self.classes_ = np.array(list(set(y)))
 
         '''
         n_features_in_ is the number of features that an estimator expects.
         In most cases, the n_features_in_ attribute exists only once fit has been called, but there are exceptions.
         '''
         self.n_features_in_ = X.shape[1]
 
     def predict(self, X):
         return self.model.predict(X)
 
     def predict_proba(self, X):
-        return self.model.predict_proba(X)    
+        return self.model.predict_proba(X)  
+
+    def evaluate(self, X, y, metrics=['loss', 'accuracy', 'precision', 'recall']):
+        '''
+        Return loss, accuracy, precision, recall by default
+        '''
+        return self.model.evaluate(X, y, metrics=metrics)
 
 class RVFLClassifierCV():
 
     def __init__(self, hparams = {'n_hidden_nodes': [1, 10], 'activation': ['sigmoid', 'tanh', 'sin'] }):        
         '''
         parameters  
         ----------
@@ -202,12 +208,12 @@
 
     def predict_proba(self, X):
         return self.clf.predict_proba(X)
 
     def predict(self, X):
         return self.clf.predict(X)
 
-def create_rvfl_instance(L):
-    return RVFLClassifier(L)
+def create_rvfl_instance(L, activation = 'sigmoid'):
+    return RVFLClassifier(L, activation)
 
 def create_rvflcv_instance():
     return RVFLClassifierCV()
```

### Comparing `pyNNRW-0.3.1/src/pyNNRW/wann.py` & `pyNNRW-0.3.2/src/pyNNRW/wann.py`

 * *Files identical despite different names*

### Comparing `pyNNRW-0.3.1/src/pyNNRW.egg-info/PKG-INFO` & `pyNNRW-0.3.2/src/pyNNRW.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyNNRW
-Version: 0.3.1
+Version: 0.3.2
 Summary: A Python library for NNRW (neural network with random weights)
 Home-page: https://github.com/zhangys11/pyNNRW
 Author: Yinsheng Zhang (Ph.D.)
 Author-email: oo@zju.edu.cn
 Project-URL: Bug Tracker, https://github.com/zhangys11/pyNNRW/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
```

