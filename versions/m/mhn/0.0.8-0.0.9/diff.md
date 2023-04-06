# Comparing `tmp/mhn-0.0.8.tar.gz` & `tmp/mhn-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mhn-0.0.8.tar", last modified: Mon Mar  6 18:20:04 2023, max compression
+gzip compressed data, was "mhn-0.0.9.tar", last modified: Sun Mar 19 16:21:44 2023, max compression
```

## Comparing `mhn-0.0.8.tar` & `mhn-0.0.9.tar`

### file list

```diff
@@ -1,42 +1,42 @@
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.394917 mhn-0.0.8/
--rw-rw-rw-   0        0        0     1090 2023-03-04 18:26:12.000000 mhn-0.0.8/LICENSE
--rw-rw-rw-   0        0        0      142 2023-03-06 18:08:27.000000 mhn-0.0.8/MANIFEST.in
--rw-rw-rw-   0        0        0     7385 2023-03-06 18:20:04.393917 mhn-0.0.8/PKG-INFO
--rw-rw-rw-   0        0        0     7130 2023-03-06 18:08:27.000000 mhn-0.0.8/README.md
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.354917 mhn-0.0.8/mhn/
--rw-rw-rw-   0        0        0       90 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/__init__.py
--rw-rw-rw-   0        0        0     2670 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/model.py
--rw-rw-rw-   0        0        0    16950 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/optimizers.py
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.382918 mhn-0.0.8/mhn/original/
--rw-rw-rw-   0        0        0    10481 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/Likelihood.pyx
--rw-rw-rw-   0        0        0      276 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/ModelConstruction.pxd
--rw-rw-rw-   0        0        0     3909 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/ModelConstruction.pyx
--rw-rw-rw-   0        0        0      586 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/PerformanceCriticalCode.pxd
--rw-rw-rw-   0        0        0    11762 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/PerformanceCriticalCode.pyx
--rw-rw-rw-   0        0        0     3797 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/RegularizedOptimization.py
--rw-rw-rw-   0        0        0     2134 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/UtilityFunctions.py
--rw-rw-rw-   0        0        0     1258 2023-03-04 23:19:28.000000 mhn-0.0.8/mhn/original/__init__.py
--rw-rw-rw-   0        0        0    25970 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/cuda_full_state_space.cu
--rw-rw-rw-   0        0        0     8864 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/cuda_inverse_by_substitution.cu
--rw-rw-rw-   0        0        0     1311 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/original/cuda_inverse_by_substitution.cuh
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.390920 mhn-0.0.8/mhn/ssr/
--rw-rw-rw-   0        0        0      313 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/__init__.py
--rw-rw-rw-   0        0        0    36940 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/cuda_state_space_restriction.cu
--rw-rw-rw-   0        0        0    18596 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/matrix_exponential.pyx
--rw-rw-rw-   0        0        0     6846 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/regularized_optimization.py
--rw-rw-rw-   0        0        0      618 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/state_containers.pxd
--rw-rw-rw-   0        0        0     5985 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/state_containers.pyx
--rw-rw-rw-   0        0        0      368 2023-03-04 18:26:12.000000 mhn-0.0.8/mhn/ssr/state_space_restriction.pxd
--rw-rw-rw-   0        0        0    26076 2023-03-04 23:19:28.000000 mhn-0.0.8/mhn/ssr/state_space_restriction.pyx
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.371917 mhn-0.0.8/mhn.egg-info/
--rw-rw-rw-   0        0        0     7385 2023-03-06 18:20:04.000000 mhn-0.0.8/mhn.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      967 2023-03-06 18:20:04.000000 mhn-0.0.8/mhn.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-06 18:20:04.000000 mhn-0.0.8/mhn.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       41 2023-03-06 18:20:04.000000 mhn-0.0.8/mhn.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-03-06 18:20:04.000000 mhn-0.0.8/mhn.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      143 2023-03-06 18:08:27.000000 mhn-0.0.8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-03-06 18:20:04.394917 mhn-0.0.8/setup.cfg
--rw-rw-rw-   0        0        0     6338 2023-03-06 18:08:27.000000 mhn-0.0.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-06 18:20:04.392917 mhn-0.0.8/test/
--rw-rw-rw-   0        0        0     5284 2023-03-04 18:26:12.000000 mhn-0.0.8/test/test_matrix_exponential.py
--rw-rw-rw-   0        0        0     7614 2023-03-04 23:19:28.000000 mhn-0.0.8/test/test_state_space_restriction.py
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:44.077299 mhn-0.0.9/
+-rw-rw-rw-   0        0        0     1090 2023-03-04 18:26:12.000000 mhn-0.0.9/LICENSE
+-rw-rw-rw-   0        0        0      142 2023-03-06 18:08:27.000000 mhn-0.0.9/MANIFEST.in
+-rw-rw-rw-   0        0        0     7531 2023-03-19 16:21:44.077299 mhn-0.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0     7276 2023-03-19 16:20:53.000000 mhn-0.0.9/README.md
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:43.977047 mhn-0.0.9/mhn/
+-rw-rw-rw-   0        0        0       90 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/__init__.py
+-rw-rw-rw-   0        0        0     3059 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/model.py
+-rw-rw-rw-   0        0        0    16950 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/optimizers.py
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:44.039544 mhn-0.0.9/mhn/original/
+-rw-rw-rw-   0        0        0    10481 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/Likelihood.pyx
+-rw-rw-rw-   0        0        0      276 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/ModelConstruction.pxd
+-rw-rw-rw-   0        0        0     3909 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/ModelConstruction.pyx
+-rw-rw-rw-   0        0        0      586 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/PerformanceCriticalCode.pxd
+-rw-rw-rw-   0        0        0    11851 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/original/PerformanceCriticalCode.pyx
+-rw-rw-rw-   0        0        0     4405 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/original/RegularizedOptimization.py
+-rw-rw-rw-   0        0        0     2163 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/original/UtilityFunctions.py
+-rw-rw-rw-   0        0        0     1258 2023-03-04 23:19:28.000000 mhn-0.0.9/mhn/original/__init__.py
+-rw-rw-rw-   0        0        0    26237 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/original/cuda_full_state_space.cu
+-rw-rw-rw-   0        0        0     8864 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/cuda_inverse_by_substitution.cu
+-rw-rw-rw-   0        0        0     1311 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/original/cuda_inverse_by_substitution.cuh
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:44.077299 mhn-0.0.9/mhn/ssr/
+-rw-rw-rw-   0        0        0      313 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/ssr/__init__.py
+-rw-rw-rw-   0        0        0    37215 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/ssr/cuda_state_space_restriction.cu
+-rw-rw-rw-   0        0        0    22496 2023-03-19 16:20:53.000000 mhn-0.0.9/mhn/ssr/matrix_exponential.pyx
+-rw-rw-rw-   0        0        0     6846 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/ssr/regularized_optimization.py
+-rw-rw-rw-   0        0        0      618 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/ssr/state_containers.pxd
+-rw-rw-rw-   0        0        0     5985 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/ssr/state_containers.pyx
+-rw-rw-rw-   0        0        0      368 2023-03-04 18:26:12.000000 mhn-0.0.9/mhn/ssr/state_space_restriction.pxd
+-rw-rw-rw-   0        0        0    26076 2023-03-04 23:19:28.000000 mhn-0.0.9/mhn/ssr/state_space_restriction.pyx
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:43.992672 mhn-0.0.9/mhn.egg-info/
+-rw-rw-rw-   0        0        0     7531 2023-03-19 16:21:43.000000 mhn-0.0.9/mhn.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      967 2023-03-19 16:21:43.000000 mhn-0.0.9/mhn.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-19 16:21:43.000000 mhn-0.0.9/mhn.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       41 2023-03-19 16:21:43.000000 mhn-0.0.9/mhn.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        4 2023-03-19 16:21:43.000000 mhn-0.0.9/mhn.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      143 2023-03-06 18:08:27.000000 mhn-0.0.9/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-03-19 16:21:44.077299 mhn-0.0.9/setup.cfg
+-rw-rw-rw-   0        0        0     6411 2023-03-19 16:20:53.000000 mhn-0.0.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-19 16:21:44.077299 mhn-0.0.9/test/
+-rw-rw-rw-   0        0        0     5284 2023-03-04 18:26:12.000000 mhn-0.0.9/test/test_matrix_exponential.py
+-rw-rw-rw-   0        0        0     7614 2023-03-04 23:19:28.000000 mhn-0.0.9/test/test_state_space_restriction.py
```

### Comparing `mhn-0.0.8/LICENSE` & `mhn-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/PKG-INFO` & `mhn-0.0.9/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,44 +1,48 @@
 Metadata-Version: 2.1
 Name: mhn
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package to train and work with Mutual Hazard Networks
 Author: Stefan Vocht, Kevin Rupp, Y. Linda Hu
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
-# mhn: A Python package to efficiently compute Mutual Hazard Networks
+# *mhn*: A Python package to efficiently compute Mutual Hazard Networks
 
 Mutual Hazard Networks (MHN) were first introduced by [Schill et al. (2019)](https://academic.oup.com/bioinformatics/article/36/1/241/5524604)
 and are used to model cancer progression.  
 This Python package can be used to work with MHNs. It includes functions that were part of the
 original R implementation as well as functions that make use of state-space restriction 
 to make learning a new MHN from cancer data faster and more efficient. Furthermore, it
 also contains functions to work with data for which the samples' ages are known and can
 therefore be considered while learning an MHN (see [Rupp et al. (2021)](https://arxiv.org/abs/2112.10971)).  
 There are optimizer classes for data with known sample ages as well as for data without, which make learning a new MHN possible with
-only a few lines of code.
+only a few lines of code.  
+
+## Documentation
+
+A detailed documentation of the *mhn* package is available [here](https://learnmhn.readthedocs.io/en/latest/index.html).
 
 ## Install the mhn package
 
 You can install the mhn package using pip:
 
 ```bash
-pip3 install mhn
+pip install mhn
 ```
 
 After completing the installation of this package you should be able to import it by calling
 ```python
 import mhn
 ```
 
 If a new version of the mhn package is available, you can upgrade your installation with
 ```bash
-pip3 install --upgrade mhn
+pip install --upgrade mhn
 ```
 
 ## A quick overview
 
 The package contains the original MHN functions implemented in Python. You import them from ``mhn.original``:
 
 ```python
```

### Comparing `mhn-0.0.8/README.md` & `mhn-0.0.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,35 +1,39 @@
-# mhn: A Python package to efficiently compute Mutual Hazard Networks
+# *mhn*: A Python package to efficiently compute Mutual Hazard Networks
 
 Mutual Hazard Networks (MHN) were first introduced by [Schill et al. (2019)](https://academic.oup.com/bioinformatics/article/36/1/241/5524604)
 and are used to model cancer progression.  
 This Python package can be used to work with MHNs. It includes functions that were part of the
 original R implementation as well as functions that make use of state-space restriction 
 to make learning a new MHN from cancer data faster and more efficient. Furthermore, it
 also contains functions to work with data for which the samples' ages are known and can
 therefore be considered while learning an MHN (see [Rupp et al. (2021)](https://arxiv.org/abs/2112.10971)).  
 There are optimizer classes for data with known sample ages as well as for data without, which make learning a new MHN possible with
-only a few lines of code.
+only a few lines of code.  
+
+## Documentation
+
+A detailed documentation of the *mhn* package is available [here](https://learnmhn.readthedocs.io/en/latest/index.html).
 
 ## Install the mhn package
 
 You can install the mhn package using pip:
 
 ```bash
-pip3 install mhn
+pip install mhn
 ```
 
 After completing the installation of this package you should be able to import it by calling
 ```python
 import mhn
 ```
 
 If a new version of the mhn package is available, you can upgrade your installation with
 ```bash
-pip3 install --upgrade mhn
+pip install --upgrade mhn
 ```
 
 ## A quick overview
 
 The package contains the original MHN functions implemented in Python. You import them from ``mhn.original``:
 
 ```python
```

### Comparing `mhn-0.0.8/mhn/model.py` & `mhn-0.0.9/mhn/model.py`

 * *Files 14% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 import numpy as np
 import pandas as pd
 import json
 
 
 class MHN:
     """
-    This class represents the Mutual Hazard Network
+    This class represents the Mutual Hazard Network.
     """
 
     def __init__(self, log_theta: np.array, events: list[str] = None, meta: dict = None):
         """
         :param log_theta: logarithmic values of the theta matrix representing the MHN
         :param events: (optional) list of strings containing the names of the events considered by the MHN
         :param meta: (optional) dictionary containing metadata for the MHN, e.g. parameters used to train the model
@@ -30,40 +30,48 @@
 
     def sample_artificial_data(self, sample_num: int, as_dataframe: bool = False) -> np.ndarray | pd.DataFrame:
         """
         Returns artificial data sampled from this MHN. Random values are generated with numpy, use np.random.seed()
         to make results reproducible.
 
         :param sample_num: number of samples in the generated data
-        :param as_dataframe: if True, the data is returned as a pandas DataFrame
+        :param as_dataframe: if True, the data is returned as a pandas DataFrame, else numpy matrix
+
+        :returns: array or DataFrame with samples as rows and events as columns
         """
         art_data = Likelihood.sample_artificial_data(self.log_theta, sample_num)
         if as_dataframe:
             df = pd.DataFrame(art_data)
             if self.events is not None:
                 df.columns = self.events
             return df
         else:
             return art_data
 
     def save(self, filename: str):
         """
-        Save the MHN file
+        Save the MHN in a CSV file. If metadata is given, it will be stored in a separate JSON file.
+
+        :param filename: name of the CSV file without(!) the '.csv', JSON will be named accordingly
         """
         pd.DataFrame(self.log_theta, columns=self.events,
                      index=self.events).to_csv(f"{filename}.csv")
         if self.meta is not None:
             with open(f"{filename}_meta.json", "x") as file:
                 json.dump(self.meta, file, indent=4)
 
     @classmethod
-    def load(cls, filename: str, events: list[str] = None):
+    def load(cls, filename: str, events: list[str] = None) -> MHN:
         """
-        :param filename: path to the CSV file
+        Load an MHN object from a CSV file.
+
+        :param filename: name of the CSV file without(!) the '.csv'
         :param events: list of strings containing the names of the events considered by the MHN
+
+        :returns: MHN object
         """
         df = pd.read_csv(f"{filename}.csv", index_col=0)
         if events is None and (df.columns != pd.Index([str(x) for x in range(len(df.columns))])).any():
             events = df.columns.to_list()
         try:
             with open(f"{filename}_meta.json", "r") as file:
                 meta = json.load(file)
```

### Comparing `mhn-0.0.8/mhn/optimizers.py` & `mhn-0.0.9/mhn/optimizers.py`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/Likelihood.pyx` & `mhn-0.0.9/mhn/original/Likelihood.pyx`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/ModelConstruction.pyx` & `mhn-0.0.9/mhn/original/ModelConstruction.pyx`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/PerformanceCriticalCode.pxd` & `mhn-0.0.9/mhn/original/PerformanceCriticalCode.pxd`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/PerformanceCriticalCode.pyx` & `mhn-0.0.9/mhn/original/PerformanceCriticalCode.pyx`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 """
 This submodule contains the Cython code equivalent to the original R code in InlineFunctions.R from the original MHN repo
-as well as some functions to solve linear equations involving [I-Q]
+as well as some functions to solve linear equations involving [I-Q].
 """
 # author(s): Stefan Vocht
 
 cimport cython
 import numpy as np
 cimport numpy as np
 
@@ -281,20 +281,20 @@
                 xout[modified_i] += theta_product * exp_theta[j*n + j] * xout_i
             bit_setter <<= 1
     free(exp_theta)
 
 
 cpdef compute_inverse(double[:, :] theta, double[:] dg, double[:] b, double[:] xout, bint transp):
     """
-    Computes the solution for [I - Q] x = b
+    Computes the solution for [I - Q] x = b using forward (and backward) substitution.
 
     :param theta: thetas used to construct Q
     :param dg: vector containing the diagonal values of [I-Q]
     :param b: a double vector
-    :param xout: solution x as double vector
+    :param xout: double vector that will contain the solution after running this function
     :param transp: if True, returns solution for [I - Q]^T x = b
     """
     cdef int n = theta.shape[0]
     if transp:
         _compute_inverse_t(&theta[0, 0], n, &dg[0], &b[0], &xout[0])
     else:
         _compute_inverse(&theta[0, 0], n, &dg[0], &b[0], &xout[0])
```

### Comparing `mhn-0.0.8/mhn/original/RegularizedOptimization.py` & `mhn-0.0.9/mhn/original/RegularizedOptimization.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """
-This submodule implements the RegularizedOptimization.R in python.
+This submodule implements RegularizedOptimization.R in Python.
 
-It contains functions to learn an MHN for a given data distribution and implements the L1 regularization.
+It contains functions to learn an MHN on the *full state-space* for a given data distribution and implements the L1 regularization.
 """
 # author(s): Stefan Vocht
 
 import numpy as np
 from scipy.optimize import minimize
 
 from . import Likelihood
@@ -13,68 +13,80 @@
 
 from typing import Callable
 
 
 def L1(theta: np.ndarray, eps: float = 1e-05) -> float:
     """
     Computes the L1 penalty
+
+    :param theta: the theta matrix representing the MHN
+    :param eps: small epsilon value, mainly there for the derivative
+
+    :returns: the L1 penalty for the given theta matrix
     """
     theta_ = theta.copy()
     np.fill_diagonal(theta_, 0)
     return np.sum(np.sqrt(theta_**2 + eps))
 
 
 def L1_(theta: np.ndarray, eps: float = 1e-05) -> np.ndarray:
     """
     Derivative of the L1 penalty
+
+    :param theta: the theta matrix representing the MHN
+    :param eps: small epsilon value that makes sure that we don't divide by zero
+
+    :returns: the derivative of the L1 penalty
     """
     theta_ = theta.copy()
     np.fill_diagonal(theta_, 0)
     return theta_ / np.sqrt(theta_**2 + eps)
 
 
 def score_reg(theta: np.ndarray, pD: np.ndarray, lam: float, n: int = None, pth_space: np.ndarray = None) -> float:
     """
     Score with L1 - regularization
 
-    :param theta:
+    :param theta: the theta matrix representing the MHN
     :param pD: distribution given by the training data
-    :param lam: tuning parameter for regularization
+    :param lam: tuning parameter lambda for regularization
     :param n: number of columns/rows of theta
-    :param pth_space: opional, with this parameter we can communicate with the gradient function and use pth there again -> performance boost
-    :return:
+    :param pth_space: optional, with this parameter we can communicate with the gradient function and use pth there again -> performance boost
+
+    :returns: the score of the current MHN penalized with the L1 regularization
     """
     n = n or int(np.sqrt(theta.size))
     theta = theta.reshape((n, n))
 
     return -(Likelihood.score(theta, pD, pth_space) - lam * L1(theta))
 
 
 def grad_reg(theta: np.ndarray, pD: np.ndarray, lam: float, n: int = 0, pth_space: np.ndarray = None) -> np.ndarray:
     """
     Gradient with L1 - regularization
 
-    :param theta:
+    :param theta: the theta matrix representing the MHN
     :param pD: distribution given by the training data
-    :param lam: tuning parameter for regularization
+    :param lam: tuning parameter lambda for regularization
     :param n: number of columns/rows of theta
-    :param pth_space: opional, as pth is calculated in the score function anyways, we do not need to calculate it again -> performance boost
-    :return:
+    :param pth_space: optional, as pth is calculated in the score function anyway, we do not need to calculate it again -> performance boost
+
+    :return: the gradient of the L1 - regularized score
     """
     n = n or int(np.sqrt(theta.size))
     theta_ = theta.reshape((n, n))
 
     return -(Likelihood.grad(theta_, pD, pth_space) - lam * L1_(theta_)).flatten()
 
 
 def learn_MHN(pD: np.ndarray, init: np.ndarray = None, lam: float = 0, maxit: int = 5000,
               trace: bool = False, reltol: float = 1e-07, round_result: bool = True,
               callback: Callable = None, score_func: Callable = score_reg, jacobi: Callable = grad_reg) -> np.ndarray:
     """
-    This function is used to train a MHN to a given probability distribution pD
+    This function is used to train an MHN to a given probability distribution pD.
 
     :param pD: probability distribution used to train the new model
     :param init: starting point for the training (initial theta)
     :param lam: tuning parameter lambda for regularization
     :param maxit: maximum number of training iterations
     :param trace: set to True to print convergence messages (see scipy.optimize.minimize)
     :param reltol: Gradient norm must be less than reltol before successful termination (see "gtol" scipy.optimize.minimize)
```

### Comparing `mhn-0.0.8/mhn/original/UtilityFunctions.py` & `mhn-0.0.9/mhn/original/UtilityFunctions.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,35 +1,35 @@
 """
-This submodule implements the UtilityFunctions.R from the original R implementation in Python
+This submodule implements UtilityFunctions.R from the original R implementation in Python.
 
-It contains functions useful for preprocessing data to be used as training data.
+It contains functions useful for preprocessing training data.
 """
 # author(s): Stefan Vocht
 
 import numpy as np
 
 
 def state_to_int(x: np.ndarray) -> int:
     """
-    This function interprets an binary array x as a binary number and returns the corresponding value as an integer
+    This function interprets a binary array x as a binary number and returns the corresponding value as an integer.
 
     :param x: binary array, in the context of the script this is a row of the mutation matrix
     :return: integer number representing the binary array
     """
 
     # reverse list and convert elements to string
     x = map(str, x[::-1])
     return int(''.join(x), 2)
 
 
 def data_to_pD(data: np.ndarray) -> np.ndarray:
     """
-    This function calculates the probability distribution for the different events for a given binary mutation matrix
+    This function calculates the probability distribution for the different events for a given binary mutation matrix.
 
-    :param data: has to be an numpy array/matrix (mutation matrix)
+    :param data: has to be a numpy array/matrix (mutation matrix)
     :return: probability distribution of the different events
     """
 
     n = data.shape[1]
     N = 2**n
 
     # convert data into a list of integers, where each number represents a different event
@@ -41,27 +41,27 @@
 
     return pD
 
 
 def finite_sample(pTh: np.ndarray, k: int) -> np.ndarray:
     """
     Generates a random sample given a probability distribution and returns the probability distribution for this new
-    sample
+    sample.
 
     :param pTh: probability distribution of events (the distribution of a true Theta)
     :param k: number of samples that should be generated
     :return: probability distribution of events from the generated samples
     """
     n = pTh.size
 
     return np.bincount(np.random.choice(n, k, replace=True, p=pTh), minlength=n) / k
 
 
 def KL_div(p: np.ndarray, q: np.ndarray) -> float:
     """
-    Computes the KL-divergence
+    Computes the Kullback–Leibler divergence of two probability distributions.
 
     :param p: probability distribution p
     :param q: probability distribution q
     :return: KL-divergence of p and q
     """
     return p.dot(np.log(p)) - p.dot(np.log(q))
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `mhn-0.0.8/mhn/original/__init__.py` & `mhn-0.0.9/mhn/original/__init__.py`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/cuda_full_state_space.cu` & `mhn-0.0.9/mhn/original/cuda_full_state_space.cu`

 * *Files 2% similar despite different names*

```diff
@@ -19,14 +19,17 @@
 // on Linux this is not needed, so we define DLL_PREFIX depending on which os this code is compiled on
 #ifdef _WIN32
 #define DLL_PREFIX __declspec(dllexport)
 #else
 #define DLL_PREFIX
 #endif
 
+// minimum number of thread blocks used by CUDA
+#define MIN_BLOCK_NUM 32
+
 
 /**
  * we determine the number of blocks and threads used in the CUDA kernels for the current data point with this function
  *
  * @param[out] block_num number of blocks that should be used for the CUDA kernels
  * @param[out] thread_num number of threads that should be used for the CUDA kernels
  * @param[in] n size of the MHN
@@ -37,15 +40,15 @@
     // maximum 256 blocks with 1024 threads
     if (n >= 17) {
         block_num = 256;
         thread_num = 512;
     }
     // define a minimum number of blocks and threads per block
     else if (n < 12) {
-        block_num = 32;
+        block_num = MIN_BLOCK_NUM;
         thread_num = 64;
     }
     else {
         block_num = 1 << (n / 2);
         thread_num = 1 << (n / 2 + (n & 1));
     }
 }
@@ -514,15 +517,20 @@
  * @param[in] pD observed frequency of tumors in data
  * @param[out] grad_out array of size n*n in which the gradient will be stored
  * @param[out] score_out the marginal log-likelihood score is stored at this position
  *
  * @return CUDA error code converted to integer for better interoperability with Cython
 */
 extern "C" int DLL_PREFIX cuda_full_state_space_gradient_score(double *ptheta, int n, double *pD, double *grad_out, double *score_out) {
-    const int nx = 1 << n;
+    
+    int nx = 1 << n;
+    // the arrays have to be at least of size MIN_BLOCK_NUM, else there will be errors when summing over arrays
+    if (nx < MIN_BLOCK_NUM){
+        nx = MIN_BLOCK_NUM;
+    }
 
     double *cuda_grad_out;
     double *cuda_pD, *pth, *q, *tmp1, *tmp2;
     double *cuda_ptheta;
     double *cuda_score;
 
     // allocate memory on the GPU
```

### Comparing `mhn-0.0.8/mhn/original/cuda_inverse_by_substitution.cu` & `mhn-0.0.9/mhn/original/cuda_inverse_by_substitution.cu`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/original/cuda_inverse_by_substitution.cuh` & `mhn-0.0.9/mhn/original/cuda_inverse_by_substitution.cuh`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/ssr/cuda_state_space_restriction.cu` & `mhn-0.0.9/mhn/ssr/cuda_state_space_restriction.cu`

 * *Files 1% similar despite different names*

```diff
@@ -22,14 +22,16 @@
 // on Linux this is not needed, so we define DLL_PREFIX depending on which os this code is compiled on
 #ifdef _WIN32
 #define DLL_PREFIX __declspec(dllexport)
 #else
 #define DLL_PREFIX 
 #endif
 
+// minimum number of thread blocks used by CUDA
+#define MIN_BLOCK_NUM 32
 
 // this struct is used to store states representing up to 32 * STATE_SIZE genes
 // STATE_SIZE must be defined during compilation
 typedef struct {
      uint32_t parts[STATE_SIZE];
 } State;
 
@@ -89,15 +91,15 @@
     // maximum 256 blocks with 1024 threads
     if (mutation_num >= 17) {
         block_num = 256;
         thread_num = 512;
     }
     // minimum 32 * STATE_SIZE threads, else for n = 32 * STATE_SIZE (which is the maximum possible n) not all thetas get loaded in kron_vec
     else if (mutation_num < 12) {
-        block_num = 32;
+        block_num = MIN_BLOCK_NUM;
         thread_num = 64;
     }
     else {
         block_num = 1 << (mutation_num / 2);
         thread_num = 1 << (mutation_num / 2 + (mutation_num & 1));
     }
 }
@@ -721,15 +723,19 @@
 
         // determine the maximum number of mutations present in a single tumor sample
         int max_mutation_num = 0;
         for (int i = 0; i < data_size; i++) {
             if (get_mutation_num(&mutation_data[i]) > max_mutation_num) max_mutation_num = get_mutation_num(&mutation_data[i]);
         }
 
-        const int nx = 1 << max_mutation_num;
+        int nx = 1 << max_mutation_num;
+        // the arrays have to be at least of size MIN_BLOCK_NUM, else there will be errors when summing over arrays
+        if (nx < MIN_BLOCK_NUM){
+            nx = MIN_BLOCK_NUM;
+        }
 
         double *cuda_grad_out, *partial_grad;
         double *p0_pD, *pth, *q, *tmp1, *tmp2;
         double *cuda_ptheta;
         double *cuda_score;
 
         // allocate memory on the GPU
```

### Comparing `mhn-0.0.8/mhn/ssr/matrix_exponential.pyx` & `mhn-0.0.9/mhn/ssr/matrix_exponential.pyx`

 * *Files 10% similar despite different names*

```diff
@@ -4,23 +4,26 @@
 
 (see Rupp et al.(2021): 'Differentiated uniformization: A new method for inferring Markov chains on combinatorial state spaces including stochastic epidemic models')
 """
 # author(s): Kevin Rupp, Stefan Vocht
 
 cimport cython
 
+import warnings
+
 from scipy.linalg.cython_blas cimport dcopy, dscal, daxpy, ddot, dnrm2, dasum
 from libc.stdlib cimport malloc, free
 from libc.math cimport exp, log
 
 from mhn.ssr.state_containers cimport State, StateContainer, StateAgeContainer
 from mhn.ssr.state_space_restriction cimport get_mutation_num, restricted_q_vec, restricted_q_diag
 
 import numpy as np
 cimport numpy as np
+from numpy.math cimport INFINITY
 
 np.import_array()
 
 
 @cython.wraparound(False)
 @cython.boundscheck(False)
 cdef void restricted_derivative_ik(double[:, :] theta_mat, int i, double[:] x_vec, State *state, int mutation_num, int k,
@@ -386,90 +389,161 @@
 
         ewg *= gamma*t/n
 
     free(temp)
     free(temp2)
 
 
-cdef void empirical_distribution(State *current_state, State *former_state, double[:] delta):
+cdef bint compute_diff_state(State *former_state, State *current_state, State *diff_state):
     """
-    Computes the empirical probability distribution used in eq. 13 in Rupp et al.(2021)
+    Find all mutations present in the current state that are not in the former state
+    
+    :param former_state: state of the previous sample
+    :param current_state: state of the current sample
+    :param diff_state: state that contains only the mutations present in current sample that are not in former sample
     
-    :param current_state: state of the current iteration in the score and gradient computation
-    :param former_state: state of the previous iteration in the score and gradient computation
-    :param delta: acts as container which will contain the distribution at the end, size: 2^(mutation_num of current_state)
+    :returns: False, if former_state contains a mutations current_state does not contain -> error
     """
-    cdef int j
-    cdef int nx = delta.shape[0]
-    cdef double zero = 0.
-    cdef int incx = 1
-    cdef current_mutation_num = get_mutation_num(current_state)
-    dscal(&nx, &zero, &delta[0], &incx)
 
-    # will be the index of x_(k-1) in delta
-    cdef int xk_index = (1 << current_mutation_num) - 1
-    cdef bit_setter = 1
-    cdef int state_copy_current = current_state[0].parts[0]
-    cdef int state_copy_former = former_state[0].parts[0]
+    cdef int i
+    cdef int former_state_copy, current_state_copy
 
-    for j in range(32 * STATE_SIZE):
-        if state_copy_current & 1:
-            if not state_copy_former & 1:
-                xk_index &= ~bit_setter
-            bit_setter <<= 1
-        if (j + 1) & 31:
-            state_copy_current >>= 1
-            state_copy_former >>= 1
-        else:
-            state_copy_current = current_state[0].parts[(j+1) >> 5]
-            state_copy_former = former_state[0].parts[(j+1) >> 5]
+    for i in range(STATE_SIZE):
+        former_state_copy = former_state[0].parts[i]
+        current_state_copy = current_state[0].parts[i]
+        # check if there is a mutation in the former state that is not in the current state
+        if (current_state_copy - former_state_copy) != (current_state_copy ^ former_state_copy):
+            return False
+        diff_state[0].parts[i] = (current_state_copy ^ former_state_copy)
+
+    return True
+
+
+cdef compute_modified_theta(double[:, :] theta, double[:, :] modified_theta, State *former_state):
+    """
+    Modifies theta according to the mutations present in the former sample.
+    It sets the base rates of genes that are mutated in the former sample to 0 (this means -inf in log space) and 
+    adds the multiplicative effects of those mutations to the base rates of genes that are not mutated in the previous
+    sample.
+    
+    :param theta: actual theta matrix
+    :param modified_theta: array that will contain the modified theta at the end
+    :param former_state: State object representing the previous sample which is used to compute the modified theta
+    """
+    cdef int n = theta.shape[0]
+    cdef int n_square = n*n
+    cdef int one = 1
+    cdef int i, j
+    cdef int state_copy_i = former_state[0].parts[0]
+    cdef int state_copy_j
+
+    # initialize the modified theta with the actual theta matrix
+    dcopy(&n_square, &theta[0, 0], &one, &modified_theta[0, 0], &one)
+
+    # look for genes that are mutated in the previous sample and modify all base rates accordingly
+    for i in range(n):
+        if state_copy_i & 1:
+            state_copy_j = former_state[0].parts[0]
+            # we want exp(theta_ii) to be 0 if i was mutated in former state
+            modified_theta[i, i] = -INFINITY
+            # all base rates are amplified by i as i is always mutated
+            for j in range(n):
+                if not state_copy_j & 1:
+                    modified_theta[j, j] += theta[j, i]
 
-    delta[xk_index] = 1
+                if (j + 1) & 31:
+                    state_copy_j >>= 1
+                else:
+                    state_copy_j = former_state[0].parts[(j + 1) >> 5]
+
+        if (i + 1) & 31:
+            state_copy_i >>= 1
+        else:
+            state_copy_i = former_state[0].parts[(i + 1) >> 5]
 
 
+@cython.wraparound(False)
+@cython.boundscheck(False)
 cpdef cython_gradient_and_score(double[:, :] theta, StateAgeContainer mutation_data, double eps):
     """
     This function computes the log-likelihood score and its gradient for a given theta and data, where we know the ages
     of the individual samples (see Rupp et al. (2021) eq. (13)-(15))
-    
+
     :param theta: theta matrix representing the MHN
     :param mutation_data: data from which we learn the MHN
     :param eps: accuracy
     :returns: the gradient and the score as a tuple
     """
     cdef int n = theta.shape[0]
     cdef int current_nx
     cdef int data_size = mutation_data.data_size
     cdef int k, i, j
     cdef double t
     cdef double score = 0
+    cdef double diagonal_partial_grad
     cdef np.ndarray[np.double_t, ndim=2] gradient = np.zeros((n, n), dtype=np.double)
+    cdef np.ndarray[np.double_t, ndim=2] modified_theta = np.empty((n, n))
     cdef np.ndarray[np.double_t] pt
     cdef np.ndarray[np.double_t] dp
     cdef np.ndarray[np.double_t] b
-    cdef State *current_state
-    cdef int state_copy
+    cdef State diff_state
+    cdef int state_copy, state_copy_former
 
     for k in range(1, data_size):
-        current_state = &mutation_data.states[k]
-        current_nx = 1 << get_mutation_num(current_state)
-        pt = np.empty(current_nx)
-        dp = np.empty(current_nx)
-        b = np.empty(current_nx)
+        # sample k must always be older than sample k-1
         t = mutation_data.state_ages[k] - mutation_data.state_ages[k-1]
         assert t >= 0
-        empirical_distribution(current_state, &mutation_data.states[k-1], b)
+
+        # get the mutations that are new in the current sample and make sure that no mutation has disappeared
+        if not compute_diff_state(&mutation_data.states[k-1], &mutation_data.states[k], &diff_state):
+            warnings.warn(f"The sample at position {k} contains less mutations than the previous sample")
+            continue
+
+        # as we restrict the state-space to contain only states that are "between" the previous and the current state
+        # this means that we get the score by multiplying exp(Qt) with (1, 0, ..., 0) and taking the last value
+        # (index = current_nx-1) of the resulting vector
+        current_nx = 1 << get_mutation_num(&diff_state)
+        compute_modified_theta(theta, modified_theta, &mutation_data.states[k-1])
+        # For the unlikely case that we have two samples with all genes mutated, the dua algorithm would never be
+        # executed. In that case we need pt to be 1 for the score computation at the end, so we initialize pt with ones.
+        # If the dua function is called even once, then all pt entries are set to zero there anyway, so this init is fine.
+        pt = np.ones(current_nx)
+        dp = np.empty(current_nx)
+        b = np.zeros(current_nx)
+        b[0] = 1
+        state_copy_former = mutation_data.states[k-1].parts[0]
         for i in range(n):
-            state_copy = current_state[0].parts[0]
-            for j in range(n):
-                if state_copy & 1 or i == j:
-                    dua(theta, b, current_state, t, i, j, eps, pt, dp)
-                    gradient[i, j] += dp[current_nx-1] / pt[current_nx-1]
+            # if the gene was mutated in the previous sample, row i of the gradient matrix is zero everywhere
+            if not state_copy_former & 1:
+                state_copy = diff_state.parts[0]
+                # the gradient of theta_ij is non-zero if gene j is mutated in the current sample
+                for j in range(n):
+                    if state_copy & 1 or i == j:
+                        dua(modified_theta, b, &diff_state, t, i, j, eps, pt, dp)
+                        gradient[i, j] += dp[current_nx-1] / pt[current_nx-1]
+                        if i == j:
+                            diagonal_partial_grad = dp[current_nx-1] / pt[current_nx-1]
+
+                    if (j + 1) & 31:
+                        state_copy >>= 1
+                    else:
+                        state_copy = diff_state.parts[(j + 1) >> 5]
+
+                # if gene j was mutated in the previous sample then the gradient of theta_ij is the same as theta_ii
+                state_copy = mutation_data.states[k-1].parts[0]
+                for j in range(n):
+                    if state_copy & 1:
+                        gradient[i, j] += diagonal_partial_grad
+
+                    if (j + 1) & 31:
+                        state_copy >>= 1
+                    else:
+                        state_copy = mutation_data.states[k-1].parts[(j + 1) >> 5]
 
-                if (j + 1) & 31:
-                    state_copy >>= 1
-                else:
-                    state_copy = current_state[0].parts[(j + 1) >> 5]
+            if (i + 1) & 31:
+                state_copy_former >>= 1
+            else:
+                state_copy_former = mutation_data.states[k-1].parts[(i + 1) >> 5]
 
         score += log(pt[current_nx-1])
 
     return gradient, score
```

### Comparing `mhn-0.0.8/mhn/ssr/regularized_optimization.py` & `mhn-0.0.9/mhn/ssr/regularized_optimization.py`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/ssr/state_containers.pxd` & `mhn-0.0.9/mhn/ssr/state_containers.pxd`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/ssr/state_containers.pyx` & `mhn-0.0.9/mhn/ssr/state_containers.pyx`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn/ssr/state_space_restriction.pyx` & `mhn-0.0.9/mhn/ssr/state_space_restriction.pyx`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/mhn.egg-info/PKG-INFO` & `mhn-0.0.9/mhn.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,44 +1,48 @@
 Metadata-Version: 2.1
 Name: mhn
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package to train and work with Mutual Hazard Networks
 Author: Stefan Vocht, Kevin Rupp, Y. Linda Hu
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
-# mhn: A Python package to efficiently compute Mutual Hazard Networks
+# *mhn*: A Python package to efficiently compute Mutual Hazard Networks
 
 Mutual Hazard Networks (MHN) were first introduced by [Schill et al. (2019)](https://academic.oup.com/bioinformatics/article/36/1/241/5524604)
 and are used to model cancer progression.  
 This Python package can be used to work with MHNs. It includes functions that were part of the
 original R implementation as well as functions that make use of state-space restriction 
 to make learning a new MHN from cancer data faster and more efficient. Furthermore, it
 also contains functions to work with data for which the samples' ages are known and can
 therefore be considered while learning an MHN (see [Rupp et al. (2021)](https://arxiv.org/abs/2112.10971)).  
 There are optimizer classes for data with known sample ages as well as for data without, which make learning a new MHN possible with
-only a few lines of code.
+only a few lines of code.  
+
+## Documentation
+
+A detailed documentation of the *mhn* package is available [here](https://learnmhn.readthedocs.io/en/latest/index.html).
 
 ## Install the mhn package
 
 You can install the mhn package using pip:
 
 ```bash
-pip3 install mhn
+pip install mhn
 ```
 
 After completing the installation of this package you should be able to import it by calling
 ```python
 import mhn
 ```
 
 If a new version of the mhn package is available, you can upgrade your installation with
 ```bash
-pip3 install --upgrade mhn
+pip install --upgrade mhn
 ```
 
 ## A quick overview
 
 The package contains the original MHN functions implemented in Python. You import them from ``mhn.original``:
 
 ```python
```

### Comparing `mhn-0.0.8/mhn.egg-info/SOURCES.txt` & `mhn-0.0.9/mhn.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/setup.py` & `mhn-0.0.9/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -133,26 +133,27 @@
 
 # we only want the source code in a source distribution
 if 'sdist' in sys.argv:
     ext_modules = []
 
 setup(
     name="mhn",
-    version="0.0.8",
+    version="0.0.9",
     packages=find_packages(),
     author="Stefan Vocht, Kevin Rupp, Y. Linda Hu",
     description="A package to train and work with Mutual Hazard Networks",
     long_description=long_description,
     long_description_content_type='text/markdown',
     ext_modules=cythonize(ext_modules,
                           annotate=GENERATE_DEBUG_HTML,
                           compile_time_env=dict(
                                                 NVCC_AVAILABLE=nvcc_available,
                                                 STATE_SIZE=STATE_SIZE
-                                                )
+                                                ),
+                          compiler_directives={'embedsignature': True}
                           ),
     include_dirs=[numpy.get_include()],
     include_package_data=True,
     install_requires=[
         'numpy>=1.23.0',
         'scipy>=1.8.0',
         'pandas>=1.5.3'
```

### Comparing `mhn-0.0.8/test/test_matrix_exponential.py` & `mhn-0.0.9/test/test_matrix_exponential.py`

 * *Files identical despite different names*

### Comparing `mhn-0.0.8/test/test_state_space_restriction.py` & `mhn-0.0.9/test/test_state_space_restriction.py`

 * *Files identical despite different names*

