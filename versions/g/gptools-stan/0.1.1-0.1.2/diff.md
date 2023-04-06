# Comparing `tmp/gptools-stan-0.1.1.tar.gz` & `tmp/gptools-stan-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gptools-stan-0.1.1.tar", last modified: Mon Jan  2 22:54:44 2023, max compression
+gzip compressed data, was "gptools-stan-0.1.2.tar", last modified: Thu Apr  6 18:12:30 2023, max compression
```

## Comparing `gptools-stan-0.1.1.tar` & `gptools-stan-0.1.2.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.596848 gptools-stan-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3433 2023-01-02 22:54:44.596848 gptools-stan-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3327 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.588848 gptools-stan-0.1.1/gptools/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.592848 gptools-stan-0.1.1/gptools/stan/
--rw-r--r--   0 runner    (1001) docker     (123)     2287 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.592848 gptools-stan-0.1.1/gptools/stan/gptools/
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/gptools/fft.stan
--rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/gptools/fft1.stan
--rw-r--r--   0 runner    (1001) docker     (123)    10184 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/gptools/fft2.stan
--rw-r--r--   0 runner    (1001) docker     (123)    20070 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/gptools/graph.stan
--rw-r--r--   0 runner    (1001) docker     (123)    12554 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/gptools/util.stan
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.592848 gptools-stan-0.1.1/gptools/stan/profile/
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/profile/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7388 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/gptools/stan/profile/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.592848 gptools-stan-0.1.1/gptools_stan.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3433 2023-01-02 22:54:44.000000 gptools-stan-0.1.1/gptools_stan.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      548 2023-01-02 22:54:44.000000 gptools-stan-0.1.1/gptools_stan.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-02 22:54:44.000000 gptools-stan-0.1.1/gptools_stan.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-01-02 22:54:44.000000 gptools-stan-0.1.1/gptools_stan.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-01-02 22:54:44.000000 gptools-stan-0.1.1/gptools_stan.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-02 22:54:44.596848 gptools-stan-0.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-02 22:54:44.592848 gptools-stan-0.1.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       90 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      129 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/tests/test_examples.py
--rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/tests/test_profile.py
--rw-r--r--   0 runner    (1001) docker     (123)    20138 2023-01-02 22:33:41.000000 gptools-stan-0.1.1/tests/test_stan_functions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.623878 gptools-stan-0.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     6500 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     6358 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/gptools/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/gptools/stan/
+-rw-r--r--   0 runner    (1001) docker     (123)     2287 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/gptools/stan/gptools/
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/gptools/fft.stan
+-rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/gptools/fft1.stan
+-rw-r--r--   0 runner    (1001) docker     (123)    10184 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/gptools/fft2.stan
+-rw-r--r--   0 runner    (1001) docker     (123)    20070 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/gptools/graph.stan
+-rw-r--r--   0 runner    (1001) docker     (123)    10792 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/gptools/util.stan
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/gptools/stan/profile/
+-rw-r--r--   0 runner    (1001) docker     (123)      809 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/profile/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7398 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/gptools/stan/profile/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/gptools_stan.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     6500 2023-04-06 18:12:30.000000 gptools-stan-0.1.2/gptools_stan.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      548 2023-04-06 18:12:30.000000 gptools-stan-0.1.2/gptools_stan.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:12:30.000000 gptools-stan-0.1.2/gptools_stan.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 18:12:30.000000 gptools-stan-0.1.2/gptools_stan.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 18:12:30.000000 gptools-stan-0.1.2/gptools_stan.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:12:30.623878 gptools-stan-0.1.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1355 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:12:30.619878 gptools-stan-0.1.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      129 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/tests/test_examples.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/tests/test_profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17280 2023-04-06 18:00:16.000000 gptools-stan-0.1.2/tests/test_stan_functions.py
```

### Comparing `gptools-stan-0.1.1/gptools/stan/__init__.py` & `gptools-stan-0.1.2/gptools/stan/__init__.py`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/gptools/stan/gptools/fft1.stan` & `gptools-stan-0.1.2/gptools/stan/gptools/fft1.stan`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/gptools/stan/gptools/fft2.stan` & `gptools-stan-0.1.2/gptools/stan/gptools/fft2.stan`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/gptools/stan/gptools/graph.stan` & `gptools-stan-0.1.2/gptools/stan/gptools/graph.stan`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/gptools/stan/gptools/util.stan` & `gptools-stan-0.1.2/gptools/stan/gptools/util.stan`

 * *Files 13% similar despite different names*

```diff
@@ -210,56 +210,14 @@
 /**
 Assert that two matrices are close. See :stan:func:`is_close` for description of parameters.
 */
 void assert_close(matrix actual, real desired) {
     assert_close(actual, desired, 1e-6, 0);
 }
 
-/**
-Ravel a matrix in the same order as numpy.
-*/
-vector ravel(matrix y) {
-    return to_vector(y');
-}
-
-/**
-Ravel a two-dimensional real array in the same order as numpy.
-*/
-array [] real ravel(array [,] real y) {
-    return to_array_1d(y);
-}
-
-/**
-Ravel a two-dimensional integer array in the same order as numpy.
-*/
-array [] int ravel(array [,] int y) {
-    return to_array_1d(y);
-}
-
-/**
-Reshape a vector in the same order as numpy.
-*/
-matrix reshape(vector y, int n, int m) {
-    return to_matrix(y, m, n)';
-}
-
-/**
-Reshape a vector in the same order as numpy.
-*/
-matrix reshape(row_vector y, int n, int m) {
-    return to_matrix(y, m, n)';
-}
-
-/**
-Reshape a matrix in the same order as numpy.
-*/
-matrix reshape(matrix y, int n, int m) {
-    return to_matrix(y', m, n)';
-}
-
 // Complex vectors ---------------------------------------------------------------------------------
 
 /**
 Assert that two vectors are close. See :stan:func:`is_close` for description of parameters.
 */
 void assert_close(complex_vector actual, complex_vector desired, real rtol, real atol) {
     int n = size(desired);
@@ -290,59 +248,17 @@
 Assert that two vectors are close. See :stan:func:`is_close` for description of parameters.
 */
 void assert_close(complex_vector actual, complex desired) {
     assert_close(actual, desired, 1e-6, 0);
 }
 
 
-/**
-Assert that all elements of a complex vector are finite.
-
-:param: Vector to check.
-*/
-void assert_finite(complex_vector x) {
-    int n = size(x);
-    for (i in 1:n) {
-        if (!is_finite(x[i])) {
-            reject(x[i], " at index ", i, " is not finite");
-        }
-    }
-}
-
 // Real Fourier transforms -------------------------------------------------------------------------
 
 /**
-Evaluate the complex conjugate.
-*/
-complex conjugate(complex x) {
-    return get_real(x) - 1.0i * get_imag(x);
-}
-
-/**
-Evaluate the complex conjugate.
-*/
-complex_vector conjugate(complex_vector x) {
-    return get_real(x) - 1.0i * get_imag(x);
-}
-
-/**
-Evaluate the complex conjugate.
-*/
-complex_row_vector conjugate(complex_row_vector x) {
-    return get_real(x) - 1.0i * get_imag(x);
-}
-
-/**
-Evaluate the complex conjugate.
-*/
-complex_matrix conjugate(complex_matrix x) {
-    return get_real(x) - 1.0i * get_imag(x);
-}
-
-/**
 Compute the one-dimensional discrete Fourier transform for real input.
 
 :param y: Real signal with :code:`n` elements to transform.
 :returns: Truncated vector of Fourier coefficients with :code:`n %/% 2 + 1` elements.
 */
 complex_vector rfft(vector y) {
     return fft(y)[:size(y) %/% 2 + 1];
@@ -356,15 +272,15 @@
     complex_vector[n] result;
     int nrfft = n %/% 2 + 1;
     if (size(y) != nrfft) {
         reject("expected complex vector with ", nrfft, " elements but got ", size(y));
     }
     int ncomplex = (n - 1) %/% 2;
     result[:nrfft] = y;
-    result[nrfft + 1:n] = conjugate(reverse(y[2:1 + ncomplex]));
+    result[nrfft + 1:n] = conj(reverse(y[2:1 + ncomplex]));
     return result;
 }
 
 /**
 Compute the one-dimensional inverse discrete Fourier transform for real output.
 
 :param z: Truncated vector of Fourier coefficents with :code:`n %/% 2 + 1` elements.
@@ -400,29 +316,23 @@
     int n = rows(z);
     complex_matrix[n, m] x;
     int mrfft = m %/% 2 + 1;
     int mcomplex = (m - 1) %/% 2;
     x[:, 1:mrfft] = z[:, 1:mrfft];
     // Fill redundant values.
     for (i in 1:n) {
-        x[i, mrfft + 1:m] = conjugate(reverse(z[i, 2:1 + mcomplex]));
+        x[i, mrfft + 1:m] = conj(reverse(z[i, 2:1 + mcomplex]));
     }
     // Reverse the order to account for negative frequencies.
     for (i in mrfft + 1:mrfft + mcomplex) {
         x[2:, i] = reverse(x[2:, i]);
     }
     return get_real(inv_fft2(x));
 }
 
-// Containers --------------------------------------------------------------------------------------
-
-matrix zeros_matrix(int m, int n) {
-    return rep_matrix(0, m, n);
-}
-
 // Conditional location and scale parameters for multivariate normal distributions -----------------
 
 /**
 Evaluate the conditional location and scale parameter of a univariate normal random variable given
 correlated observations from a multivariate normal distribution.
 
 :param y: Observation to condition on.
```

### Comparing `gptools-stan-0.1.1/gptools/stan/profile/__init__.py` & `gptools-stan-0.1.2/gptools/stan/profile/__init__.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 import cmdstanpy
 import logging
 import numpy as np
 
 
-SIZES = 16 * 2 ** np.arange(9)
+SIZES = 16 * 2 ** np.arange(11)
+FOURIER_ONLY_SIZE_THRESHOLD = 16 * 2 ** 9
 LOG10_NOISE_SCALES = np.linspace(-1, 1, 7)
 PARAMETERIZATIONS = ["graph_centered", "graph_non_centered", "fourier_centered",
                      "fourier_non_centered", "standard_centered", "standard_non_centered"]
 
 # Make cmdstanpy less verbose.
 cmdstanpy_logger = cmdstanpy.utils.get_logger()
 for handler in cmdstanpy_logger.handlers:
```

### Comparing `gptools-stan-0.1.1/gptools/stan/profile/__main__.py` & `gptools-stan-0.1.2/gptools/stan/profile/__main__.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 import argparse
 from gptools.stan import compile_model
 from gptools.util import Timer
-from gptools.util.kernels import ExpQuadKernel, DiagonalKernel
+from gptools.util.fft import transform_irfft
+from gptools.util.kernels import ExpQuadKernel
 from gptools.util.graph import lattice_predecessors, predecessors_to_edge_index
 from gptools.util.timeout import call_with_timeout
 import numpy as np
 import pathlib
 import pickle
 import tabulate
-from scipy import stats
 from tqdm import tqdm
 from typing import Optional
 from . import PARAMETERIZATIONS, sample_and_load_fit
 
 
 def __main__(args: Optional[list[str]] = None) -> None:
     parser = argparse.ArgumentParser()
@@ -52,40 +52,39 @@
 
     # Prepare the results container.
     result = {"args": vars(args)}
 
     np.random.seed(args.seed)
     i = 0
 
-    # Prepare the distribution outside the loop because matrix inversion can take a while.
-    # Generate data from a Gaussian process with normal observation noise.
-    X = np.arange(args.n)[:, None]
-    kernel = ExpQuadKernel(args.sigma, args.length_scale) + DiagonalKernel(args.epsilon)
-    cov = kernel.evaluate(X)
-    dist = stats.multivariate_normal(np.zeros(args.n), cov)
+    # We draw samples with Fourier methods because generating the training data can be the main
+    # bottleneck if the sample size is large.
+    kernel = ExpQuadKernel(args.sigma, args.length_scale, args.n)
+    cov_rfft = kernel.evaluate_rfft(args.n) + args.epsilon
 
     with Timer() as total_timer, tqdm() as progress:
         while (args.max_chains == -1 or i < args.max_chains) \
                 and (args.timeout is None or total_timer.duration < args.timeout):
 
             # Sample the Gaussian process.
-            eta = dist.rvs()
+            z = np.random.normal(0, 1, args.n)
+            eta = transform_irfft(z, np.zeros_like(z), cov_rfft=cov_rfft)
             y = np.random.normal(eta, args.noise_scale)
 
             # Construct the nearest-neighbor graph.
             predecessors = lattice_predecessors((args.n,), args.num_parents)
             edge_index = predecessors_to_edge_index(predecessors)
 
             # Sample observed points and fit the model.
             num_observed = np.random.binomial(args.n, args.train_frac)
             observed_idx = np.random.choice(args.n, size=num_observed, replace=False) + 1
             data = {
                 "n": args.n,
                 "num_dims": 1,
-                "X": X,
+                "X": np.arange(args.n)[:, None],
                 "y": y,
                 "sigma": args.sigma,
                 "length_scale": args.length_scale,
                 "epsilon": args.epsilon,
                 "num_edges": edge_index.shape[1],
                 "edge_index": edge_index,
                 "noise_scale": args.noise_scale,
```

### Comparing `gptools-stan-0.1.1/gptools_stan.egg-info/SOURCES.txt` & `gptools-stan-0.1.2/gptools_stan.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/setup.py` & `gptools-stan-0.1.2/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,22 +1,23 @@
 import re
 from setuptools import find_namespace_packages, setup
 
 with open("README.rst") as fp:
     long_description = fp.read()
-long_description = re.sub(r".. (literalinclude|testsetup|toctree)::", "..", long_description)
+long_description = re.sub(r".. (literalinclude|testsetup|toctree)::", "..\n    comment",
+                          long_description)
 long_description = re.sub(".. doctest::", ".. code-block::", long_description)
 long_description = re.sub(":(doc|class|func|ref):", ":code:", long_description)
 
 setup(
     name="gptools-stan",
     long_description=long_description,
     long_description_content_type="text/x-rst",
     packages=find_namespace_packages(),
-    version="0.1.1",
+    version="0.1.2",
     install_requires=[
         # Required because of a bug in how complex numbers are handled (see
         # https://github.com/stan-dev/cmdstanpy/pull/612).
         "cmdstanpy>=1.0.7",
         "gptools-util",
         "numpy",
     ],
```

### Comparing `gptools-stan-0.1.1/tests/test_profile.py` & `gptools-stan-0.1.2/tests/test_profile.py`

 * *Files identical despite different names*

### Comparing `gptools-stan-0.1.1/tests/test_stan_functions.py` & `gptools-stan-0.1.2/tests/test_stan_functions.py`

 * *Files 9% similar despite different names*

```diff
@@ -277,91 +277,14 @@
         "arg_values": {"n_": n, "m_": m, "y": y, "loc": loc, "cov_rfft2": cov_rfft2},
         "result_type": "real",
         "includes": ["gptools/util.stan", "gptools/fft1.stan", "gptools/fft2.stan"],
         "desired": [stats.multivariate_normal(loc.ravel(), cov).logpdf(y.ravel()),
                     fft.evaluate_log_prob_rfft2(y, loc, cov_rfft2=cov_rfft2)],
     })
 
-    # Using `to_vector` is different from numpy's `ravel` in terms of ordering ...
-    add_configuration({
-        "stan_function": "to_vector",
-        "arg_types": {"n_": "int", "m_": "int", "y": "matrix[n_, m_]"},
-        "arg_values": {"n_": n, "m_": m, "y": y},
-        "result_type": "vector[n_ * m_]",
-        "includes": ["gptools/util.stan"],
-        "desired": y.T.ravel(),
-    })
-
-    # ... but `to_array_1d` has the same ordering as numpy's `ravel`.
-    add_configuration({
-        "stan_function": "to_array_1d",
-        "arg_types": {"n_": "int", "m_": "int", "y": "array [n_, m_] real"},
-        "arg_values": {"n_": n, "m_": m, "y": y},
-        "result_type": "array [n_ * m_] real",
-        "includes": ["gptools/util.stan"],
-        "desired": y.ravel(),
-    })
-
-    # Linearising matrices and arrays using a common `ravel` function.
-    add_configuration({
-        "stan_function": "ravel",
-        "arg_types": {"n_": "int", "m_": "int", "y": "matrix[n_, m_]"},
-        "arg_values": {"n_": n, "m_": m, "y": y},
-        "result_type": "vector[n_ * m_]",
-        "includes": ["gptools/util.stan"],
-        "desired": y.ravel(),
-        "suffix": "vector",
-    })
-    add_configuration({
-        "stan_function": "ravel",
-        "arg_types": {"n_": "int", "m_": "int", "y": "array [n_, m_] real"},
-        "arg_values": {"n_": n, "m_": m, "y": y},
-        "result_type": "array [n_ * m_] real",
-        "includes": ["gptools/util.stan"],
-        "desired": y.ravel(),
-        "suffix": "array",
-    })
-
-    # Reshaping vectors and matrices.
-    add_configuration({
-        "stan_function": "reshape",
-        "arg_types": {"n": "int", "m": "int", "y": "matrix[n, m]"},
-        "arg_values": {"y": y, "m": m, "n": n},
-        "result_type": "matrix[m, n]",
-        "includes": ["gptools/util.stan"],
-        "desired": y.reshape((m, n)),
-        "suffix": "matrix",
-    })
-    add_configuration({
-        "stan_function": "reshape",
-        "arg_types": {"n": "int", "m": "int", "y": "vector[n * m]"},
-        "arg_values": {"y": y.ravel(), "m": m, "n": n},
-        "result_type": "matrix[m, n]",
-        "includes": ["gptools/util.stan"],
-        "desired": y.reshape((m, n)),
-        "suffix": "vector",
-    })
-    add_configuration({
-        "stan_function": "reshape",
-        "arg_types": {"n": "int", "m": "int", "y": "row_vector[n * m]"},
-        "arg_values": {"y": y.ravel(), "m": m, "n": n},
-        "result_type": "matrix[m, n]",
-        "includes": ["gptools/util.stan"],
-        "desired": y.reshape((m, n)),
-        "suffix": "row_vector",
-    })
-    add_configuration({
-        "stan_function": "zeros_matrix",
-        "arg_types": {"m": "int", "n": "int"},
-        "arg_values": {"m": m, "n": n},
-        "result_type": "matrix[m, n]",
-        "includes": ["gptools/util.stan"],
-        "desired": np.zeros((m, n)),
-    })
-
 for m in [7, 8]:
     sigma = np.random.gamma(10, 0.1)
     length_scale = np.random.gamma(10, 0.1)
     period = np.random.gamma(100, 0.1)
     add_configuration({
         "stan_function": "gp_periodic_exp_quad_cov_rfft",
         "arg_types": {"m": "int", "sigma": "real", "length_scale": "real", "period": "real"},
```

