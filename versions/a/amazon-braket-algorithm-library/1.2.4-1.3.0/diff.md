# Comparing `tmp/amazon-braket-algorithm-library-1.2.4.tar.gz` & `tmp/amazon-braket-algorithm-library-1.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "amazon-braket-algorithm-library-1.2.4.tar", last modified: Thu Mar 23 16:07:24 2023, max compression
+gzip compressed data, was "amazon-braket-algorithm-library-1.3.0.tar", last modified: Thu Apr  6 16:07:20 2023, max compression
```

## Comparing `amazon-braket-algorithm-library-1.2.4.tar` & `amazon-braket-algorithm-library-1.3.0.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.489384 amazon-braket-algorithm-library-1.2.4/
--rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-03-23 16:07:24.489384 amazon-braket-algorithm-library-1.2.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-23 16:07:24.489384 amazon-braket-algorithm-library-1.2.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.473384 amazon-braket-algorithm-library-1.2.4/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.481384 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-03-23 16:07:24.000000 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2286 2023-03-23 16:07:24.000000 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-23 16:07:24.000000 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-23 16:07:24.000000 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-23 16:07:24.000000 amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.473384 amazon-braket-algorithm-library-1.2.4/src/braket/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.481384 amazon-braket-algorithm-library-1.2.4/src/braket/_algos/
--rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/_algos/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.481384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bells_inequality/
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bells_inequality/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4611 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bells_inequality/bells_inequality.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bernstein_vazirani/
--rw-r--r--   0 runner    (1001) docker     (123)      755 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bernstein_vazirani/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3016 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bernstein_vazirani/bernstein_vazirani.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/chsh_inequality/
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/chsh_inequality/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3961 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/chsh_inequality/chsh_inequality.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/deutsch_jozsa/
--rw-r--r--   0 runner    (1001) docker     (123)      749 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/deutsch_jozsa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3470 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/deutsch_jozsa/deutsch_jozsa.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/grovers_search/
--rw-r--r--   0 runner    (1001) docker     (123)      689 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/grovers_search/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5745 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/grovers_search/grovers_search.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12997 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/classical_qmc.py
--rw-r--r--   0 runner    (1001) docker     (123)    19646 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/qc_qmc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_approximate_optimization/
--rw-r--r--   0 runner    (1001) docker     (123)      743 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_approximate_optimization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5414 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_approximate_optimization/quantum_approximate_optimization.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_circuit_born_machine/
--rw-r--r--   0 runner    (1001) docker     (123)      678 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_circuit_born_machine/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8429 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_circuit_born_machine/qcbm.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_fourier_transform/
--rw-r--r--   0 runner    (1001) docker     (123)      678 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_fourier_transform/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5232 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_fourier_transform/quantum_fourier_transform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_phase_estimation/
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_phase_estimation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10830 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_phase_estimation/quantum_phase_estimation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_walk/
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_walk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5033 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_walk/quantum_walk.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.485384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/shors/
--rw-r--r--   0 runner    (1001) docker     (123)      709 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/shors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10435 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/shors/shors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 16:07:24.489384 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/simons/
--rw-r--r--   0 runner    (1001) docker     (123)      736 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/simons/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7007 2023-03-23 16:07:12.000000 amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/simons/simons.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.434817 amazon-braket-algorithm-library-1.3.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.438817 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-04-06 16:07:20.000000 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2286 2023-04-06 16:07:20.000000 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:07:20.000000 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-04-06 16:07:20.000000 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 16:07:20.000000 amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.434817 amazon-braket-algorithm-library-1.3.0/src/braket/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.438817 amazon-braket-algorithm-library-1.3.0/src/braket/_algos/
+-rw-r--r--   0 runner    (1001) docker     (123)      655 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/_algos/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.438817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.438817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.438817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bells_inequality/
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bells_inequality/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4611 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bells_inequality/bells_inequality.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bernstein_vazirani/
+-rw-r--r--   0 runner    (1001) docker     (123)      755 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bernstein_vazirani/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3016 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bernstein_vazirani/bernstein_vazirani.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/chsh_inequality/
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/chsh_inequality/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3961 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/chsh_inequality/chsh_inequality.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/deutsch_jozsa/
+-rw-r--r--   0 runner    (1001) docker     (123)      749 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/deutsch_jozsa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3470 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/deutsch_jozsa/deutsch_jozsa.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/grovers_search/
+-rw-r--r--   0 runner    (1001) docker     (123)      689 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/grovers_search/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5745 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/grovers_search/grovers_search.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12997 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/classical_qmc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19646 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/qc_qmc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_approximate_optimization/
+-rw-r--r--   0 runner    (1001) docker     (123)      743 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_approximate_optimization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5414 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_approximate_optimization/quantum_approximate_optimization.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_circuit_born_machine/
+-rw-r--r--   0 runner    (1001) docker     (123)      678 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_circuit_born_machine/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8429 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_circuit_born_machine/qcbm.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_fourier_transform/
+-rw-r--r--   0 runner    (1001) docker     (123)      678 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_fourier_transform/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5232 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_fourier_transform/quantum_fourier_transform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.442817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_phase_estimation/
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_phase_estimation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10830 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_phase_estimation/quantum_phase_estimation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_walk/
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_walk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5033 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_walk/quantum_walk.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/shors/
+-rw-r--r--   0 runner    (1001) docker     (123)      709 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/shors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10435 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/shors/shors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:07:20.446817 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/simons/
+-rw-r--r--   0 runner    (1001) docker     (123)      736 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/simons/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7007 2023-04-06 16:07:05.000000 amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/simons/simons.py
```

### Comparing `amazon-braket-algorithm-library-1.2.4/LICENSE` & `amazon-braket-algorithm-library-1.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/PKG-INFO` & `amazon-braket-algorithm-library-1.3.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: amazon-braket-algorithm-library
-Version: 1.2.4
+Version: 1.3.0
 Summary: An open source library of quantum computing algorithms implemented on Amazon Braket
 Home-page: https://github.com/aws-samples/amazon-braket-algorithm-library
 Author: Amazon Web Services
 License: Apache License 2.0
 Keywords: Amazon AWS Quantum
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
-Requires-Python: >= 3.7.2
+Requires-Python: >= 3.8.2
 Description-Content-Type: text/markdown
 Provides-Extra: test
 License-File: LICENSE
 License-File: NOTICE
 
 # Amazon Braket Algorithm Library
 The Braket Algorithm Library provides Amazon Braket customers with pre-built implementations of prominent quantum algorithms and experimental workloads as ready-to-run example notebooks.
```

### Comparing `amazon-braket-algorithm-library-1.2.4/README.md` & `amazon-braket-algorithm-library-1.3.0/README.md`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/setup.py` & `amazon-braket-algorithm-library-1.3.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 with open("src/braket/_algos/_version.py") as f:
     version = f.readlines()[-1].split()[-1].strip("\"'")
 
 setup(
     name="amazon-braket-algorithm-library",
     version=version,
     license="Apache License 2.0",
-    python_requires=">= 3.7.2",
+    python_requires=">= 3.8.2",
     packages=find_namespace_packages(where="src", exclude=("test",)),
     package_dir={"": "src"},
     install_requires=[
         "amazon-braket-sdk>=1.35.1",
         "scipy>=1.5.2",
         "pennylane>=0.29.1",
         "openfermion==1.0.0",
```

### Comparing `amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/PKG-INFO` & `amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: amazon-braket-algorithm-library
-Version: 1.2.4
+Version: 1.3.0
 Summary: An open source library of quantum computing algorithms implemented on Amazon Braket
 Home-page: https://github.com/aws-samples/amazon-braket-algorithm-library
 Author: Amazon Web Services
 License: Apache License 2.0
 Keywords: Amazon AWS Quantum
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python
-Requires-Python: >= 3.7.2
+Requires-Python: >= 3.8.2
 Description-Content-Type: text/markdown
 Provides-Extra: test
 License-File: LICENSE
 License-File: NOTICE
 
 # Amazon Braket Algorithm Library
 The Braket Algorithm Library provides Amazon Braket customers with pre-built implementations of prominent quantum algorithms and experimental workloads as ready-to-run example notebooks.
```

### Comparing `amazon-braket-algorithm-library-1.2.4/src/amazon_braket_algorithm_library.egg-info/SOURCES.txt` & `amazon-braket-algorithm-library-1.3.0/src/amazon_braket_algorithm_library.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/_algos/_version.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/_algos/_version.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,8 +12,8 @@
 # language governing permissions and limitations under the License.
 
 """Version information.
 
 Version number (major.minor.patch[-label])
 """
 
-__version__ = "1.2.4"
+__version__ = "1.3.0"
```

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bells_inequality/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bells_inequality/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bells_inequality/bells_inequality.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bells_inequality/bells_inequality.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bernstein_vazirani/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bernstein_vazirani/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/bernstein_vazirani/bernstein_vazirani.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/bernstein_vazirani/bernstein_vazirani.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/chsh_inequality/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/chsh_inequality/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/chsh_inequality/chsh_inequality.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/chsh_inequality/chsh_inequality.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/deutsch_jozsa/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/deutsch_jozsa/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/deutsch_jozsa/deutsch_jozsa.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/deutsch_jozsa/deutsch_jozsa.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/grovers_search/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/grovers_search/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/grovers_search/grovers_search.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/grovers_search/grovers_search.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/classical_qmc.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/classical_qmc.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/qc_qmc/qc_qmc.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/qc_qmc/qc_qmc.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_approximate_optimization/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_approximate_optimization/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_approximate_optimization/quantum_approximate_optimization.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_approximate_optimization/quantum_approximate_optimization.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_circuit_born_machine/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_circuit_born_machine/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_circuit_born_machine/qcbm.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_circuit_born_machine/qcbm.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_fourier_transform/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_fourier_transform/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_fourier_transform/quantum_fourier_transform.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_fourier_transform/quantum_fourier_transform.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_phase_estimation/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_phase_estimation/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_phase_estimation/quantum_phase_estimation.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_phase_estimation/quantum_phase_estimation.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_walk/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_walk/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/quantum_walk/quantum_walk.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/quantum_walk/quantum_walk.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/shors/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/shors/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/shors/shors.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/shors/shors.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/simons/__init__.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/simons/__init__.py`

 * *Files identical despite different names*

### Comparing `amazon-braket-algorithm-library-1.2.4/src/braket/experimental/algorithms/simons/simons.py` & `amazon-braket-algorithm-library-1.3.0/src/braket/experimental/algorithms/simons/simons.py`

 * *Files identical despite different names*

