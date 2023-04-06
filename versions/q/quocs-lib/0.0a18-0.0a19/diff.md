# Comparing `tmp/quocs-lib-0.0a18.tar.gz` & `tmp/quocs-lib-0.0a19.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quocs-lib-0.0a18.tar", last modified: Thu Mar 31 10:43:16 2022, max compression
+gzip compressed data, was "quocs-lib-0.0a19.tar", last modified: Thu Mar 31 10:51:54 2022, max compression
```

## Comparing `quocs-lib-0.0a18.tar` & `quocs-lib-0.0a19.tar`

### file list

```diff
@@ -1,99 +1,99 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.094236 quocs-lib-0.0a18/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     1722 2022-03-31 10:43:16.094236 quocs-lib-0.0a18/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1152 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/README.md
--rw-r--r--   0 runner    (1001) docker     (121)       85 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      719 2022-03-31 10:43:16.094236 quocs-lib-0.0a18/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      806 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocs_lib.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     1722 2022-03-31 10:43:15.000000 quocs-lib-0.0a18/src/quocs_lib.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3176 2022-03-31 10:43:15.000000 quocs-lib-0.0a18/src/quocs_lib.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-31 10:43:15.000000 quocs-lib-0.0a18/src/quocs_lib.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-03-31 10:43:15.000000 quocs-lib-0.0a18/src/quocs_lib.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-03-31 10:43:15.000000 quocs-lib-0.0a18/src/quocs_lib.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/
--rw-r--r--   0 runner    (1001) docker     (121)    10530 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/Controls.py
--rw-r--r--   0 runner    (1001) docker     (121)     2463 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/Optimizer.py
--rw-r--r--   0 runner    (1001) docker     (121)      107 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/communication/
--rw-r--r--   0 runner    (1001) docker     (121)     8933 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/communication/AllInOneCommunication.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/communication/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/figureofmeritevaluation/
--rw-r--r--   0 runner    (1001) docker     (121)     1122 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/figureofmeritevaluation/AbstractFom.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/figureofmeritevaluation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/
--rw-r--r--   0 runner    (1001) docker     (121)     9541 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/CMAES.py
--rw-r--r--   0 runner    (1001) docker     (121)     1716 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/DirectSearchMethod.py
--rw-r--r--   0 runner    (1001) docker     (121)     7311 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/GradientFreeTemplate.py
--rw-r--r--   0 runner    (1001) docker     (121)     7277 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/NelderMead.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/gradientfreemethods/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/handleexit/
--rw-r--r--   0 runner    (1001) docker     (121)      913 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/handleexit/AbstractHandleExit.py
--rw-r--r--   0 runner    (1001) docker     (121)      939 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/handleexit/HandleExit.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/handleexit/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.086236 quocs-lib-0.0a18/src/quocslib/noiseprocesses/
--rw-r--r--   0 runner    (1001) docker     (121)      118 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/noiseprocesses/noiseprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)     1317 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/noiseprocesses/ornsteinuhlenbeckprocess.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/
--rw-r--r--   0 runner    (1001) docker     (121)     4056 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/OneQubitProblem.py
--rw-r--r--   0 runner    (1001) docker     (121)     3376 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/OneQubitProblem_2fields.py
--rw-r--r--   0 runner    (1001) docker     (121)     2012 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/RosenbrockProblem.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1703 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/su2.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/
--rw-r--r--   0 runner    (1001) docker     (121)     7008 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/ADAlgorithm.py
--rw-r--r--   0 runner    (1001) docker     (121)     6258 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/AlgorithmTemplate.py
--rw-r--r--   0 runner    (1001) docker     (121)     5896 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/DirectSearchAlgorithm.py
--rw-r--r--   0 runner    (1001) docker     (121)     9271 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/GRAPEAlgorithm.py
--rw-r--r--   0 runner    (1001) docker     (121)     7819 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/OptimizationAlgorithm.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9706 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/dCRABAlgorithm.py
--rw-r--r--   0 runner    (1001) docker     (121)    21654 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/dCRABNoisyAlgorithm.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/parameters/
--rw-r--r--   0 runner    (1001) docker     (121)     3904 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/parameters/BaseParameter.py
--rw-r--r--   0 runner    (1001) docker     (121)     1058 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/parameters/Parameter.py
--rw-r--r--   0 runner    (1001) docker     (121)     3651 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/parameters/TimeParameter.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/parameters/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/pulses/
--rw-r--r--   0 runner    (1001) docker     (121)    14269 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/BasePulse.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/pulses/basis/
--rw-r--r--   0 runner    (1001) docker     (121)     3020 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/Chebyshev.py
--rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/ChoppedBasis.py
--rw-r--r--   0 runner    (1001) docker     (121)     3728 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/DummyBasis.py
--rw-r--r--   0 runner    (1001) docker     (121)     2907 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/Fourier.py
--rw-r--r--   0 runner    (1001) docker     (121)     3028 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/PiecewiseBasis.py
--rw-r--r--   0 runner    (1001) docker     (121)     3551 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/Sigmoid.py
--rw-r--r--   0 runner    (1001) docker     (121)     4233 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/basis/Walsh.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/pulses/superparameter/
--rw-r--r--   0 runner    (1001) docker     (121)     1291 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/superparameter/SuperParameterDistribution.py
--rw-r--r--   0 runner    (1001) docker     (121)     2043 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/pulses/superparameter/Uniform.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/stoppingcriteria/
--rw-r--r--   0 runner    (1001) docker     (121)     2283 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/stoppingcriteria/CMAESStoppingCriteria.py
--rw-r--r--   0 runner    (1001) docker     (121)     2230 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/stoppingcriteria/NelderMeadStoppingCriteria.py
--rw-r--r--   0 runner    (1001) docker     (121)     2402 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/stoppingcriteria/StoppingCriteria.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/stoppingcriteria/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/timeevolution/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/timeevolution/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1878 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/timeevolution/piecewise_integrator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.090236 quocs-lib-0.0a18/src/quocslib/tools/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4374 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/tools/linearalgebra.py
--rw-r--r--   0 runner    (1001) docker     (121)     2450 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/tools/logger.py
--rw-r--r--   0 runner    (1001) docker     (121)     1095 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/tools/pulsetools.py
--rw-r--r--   0 runner    (1001) docker     (121)     2543 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/tools/randomgenerator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:43:16.094236 quocs-lib-0.0a18/src/quocslib/utils/
--rw-r--r--   0 runner    (1001) docker     (121)     1775 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/AbstractDump.py
--rw-r--r--   0 runner    (1001) docker     (121)     1687 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/AbstractFoM.py
--rw-r--r--   0 runner    (1001) docker     (121)     1213 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/AbstractHandleExit.py
--rw-r--r--   0 runner    (1001) docker     (121)     3048 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/BestDump.py
--rw-r--r--   0 runner    (1001) docker     (121)     1099 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/DummyDump.py
--rw-r--r--   0 runner    (1001) docker     (121)     6770 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/FilesUpdateFom.py
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3601 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/dynamicimport.py
--rw-r--r--   0 runner    (1001) docker     (121)     2104 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/inputoutput.py
--rw-r--r--   0 runner    (1001) docker     (121)     2456 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/logger.py
--rw-r--r--   0 runner    (1001) docker     (121)     2368 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/map_dictionary.json
--rw-r--r--   0 runner    (1001) docker     (121)     2668 2022-03-31 10:43:06.000000 quocs-lib-0.0a18/src/quocslib/utils/test_BestDump.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     1722 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1152 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)       85 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      719 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      806 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.348300 quocs-lib-0.0a19/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.352300 quocs-lib-0.0a19/src/quocs_lib.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     1722 2022-03-31 10:51:54.000000 quocs-lib-0.0a19/src/quocs_lib.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3176 2022-03-31 10:51:54.000000 quocs-lib-0.0a19/src/quocs_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-31 10:51:54.000000 quocs-lib-0.0a19/src/quocs_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-03-31 10:51:54.000000 quocs-lib-0.0a19/src/quocs_lib.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        9 2022-03-31 10:51:54.000000 quocs-lib-0.0a19/src/quocs_lib.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.352300 quocs-lib-0.0a19/src/quocslib/
+-rw-r--r--   0 runner    (1001) docker     (121)    10530 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/Controls.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2463 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/Optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (121)      107 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.352300 quocs-lib-0.0a19/src/quocslib/communication/
+-rw-r--r--   0 runner    (1001) docker     (121)     8933 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/communication/AllInOneCommunication.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/communication/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.352300 quocs-lib-0.0a19/src/quocslib/figureofmeritevaluation/
+-rw-r--r--   0 runner    (1001) docker     (121)     1122 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/figureofmeritevaluation/AbstractFom.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/figureofmeritevaluation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/
+-rw-r--r--   0 runner    (1001) docker     (121)     9541 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/CMAES.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1716 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/DirectSearchMethod.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7311 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/GradientFreeTemplate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7277 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/NelderMead.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/gradientfreemethods/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/handleexit/
+-rw-r--r--   0 runner    (1001) docker     (121)      913 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/handleexit/AbstractHandleExit.py
+-rw-r--r--   0 runner    (1001) docker     (121)      939 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/handleexit/HandleExit.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/handleexit/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/noiseprocesses/
+-rw-r--r--   0 runner    (1001) docker     (121)      118 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/noiseprocesses/noiseprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1317 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/noiseprocesses/ornsteinuhlenbeckprocess.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/
+-rw-r--r--   0 runner    (1001) docker     (121)     4056 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/OneQubitProblem.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3376 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/OneQubitProblem_2fields.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2012 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/RosenbrockProblem.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1703 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/su2.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/
+-rw-r--r--   0 runner    (1001) docker     (121)     7008 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/ADAlgorithm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6258 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/AlgorithmTemplate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5896 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/DirectSearchAlgorithm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9271 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/GRAPEAlgorithm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7819 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/OptimizationAlgorithm.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9706 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/dCRABAlgorithm.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21654 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/dCRABNoisyAlgorithm.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/parameters/
+-rw-r--r--   0 runner    (1001) docker     (121)     3904 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/parameters/BaseParameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1058 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/parameters/Parameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3651 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/parameters/TimeParameter.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/parameters/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.356300 quocs-lib-0.0a19/src/quocslib/pulses/
+-rw-r--r--   0 runner    (1001) docker     (121)    14269 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/BasePulse.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/pulses/basis/
+-rw-r--r--   0 runner    (1001) docker     (121)     3020 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/Chebyshev.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2528 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/ChoppedBasis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3728 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/DummyBasis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2907 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/Fourier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3028 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/PiecewiseBasis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3551 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/Sigmoid.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4233 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/basis/Walsh.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/pulses/superparameter/
+-rw-r--r--   0 runner    (1001) docker     (121)     1291 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/superparameter/SuperParameterDistribution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2043 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/pulses/superparameter/Uniform.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/stoppingcriteria/
+-rw-r--r--   0 runner    (1001) docker     (121)     2283 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/stoppingcriteria/CMAESStoppingCriteria.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2230 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/stoppingcriteria/NelderMeadStoppingCriteria.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2402 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/stoppingcriteria/StoppingCriteria.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/stoppingcriteria/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/timeevolution/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/timeevolution/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1878 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/timeevolution/piecewise_integrator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/tools/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4374 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/tools/linearalgebra.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2450 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/tools/logger.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1095 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/tools/pulsetools.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2543 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/tools/randomgenerator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-31 10:51:54.360300 quocs-lib-0.0a19/src/quocslib/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)     1775 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/AbstractDump.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1687 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/AbstractFoM.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1213 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/AbstractHandleExit.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3048 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/BestDump.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1099 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/DummyDump.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6770 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/FilesUpdateFom.py
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3601 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/dynamicimport.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2104 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/inputoutput.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2456 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/logger.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2368 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/map_dictionary.json
+-rw-r--r--   0 runner    (1001) docker     (121)     2702 2022-03-31 10:51:44.000000 quocs-lib-0.0a19/src/quocslib/utils/test_BestDump.py
```

### Comparing `quocs-lib-0.0a18/LICENSE` & `quocs-lib-0.0a19/LICENSE`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/PKG-INFO` & `quocs-lib-0.0a19/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quocs-lib
-Version: 0.0a18
+Version: 0.0a19
 Summary: QuOCS (Quantum Optimal Control Suite) library
 Home-page: https://github.com/Quantum-OCS/QuOCS
 Author: QuOCS Team
 Author-email: quantum.optimal.cs@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/Quantum-OCS/QuOCS/issues
 Platform: UNKNOWN
```

### Comparing `quocs-lib-0.0a18/README.md` & `quocs-lib-0.0a19/README.md`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/setup.cfg` & `quocs-lib-0.0a19/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = quocs-lib
-version = 0.0a18
+version = 0.0a19
 author = QuOCS Team
 author_email = quantum.optimal.cs@gmail.com
 description = QuOCS (Quantum Optimal Control Suite) library
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/Quantum-OCS/QuOCS
 project_urls =
```

### Comparing `quocs-lib-0.0a18/setup.py` & `quocs-lib-0.0a19/setup.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocs_lib.egg-info/PKG-INFO` & `quocs-lib-0.0a19/src/quocs_lib.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quocs-lib
-Version: 0.0a18
+Version: 0.0a19
 Summary: QuOCS (Quantum Optimal Control Suite) library
 Home-page: https://github.com/Quantum-OCS/QuOCS
 Author: QuOCS Team
 Author-email: quantum.optimal.cs@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/Quantum-OCS/QuOCS/issues
 Platform: UNKNOWN
```

### Comparing `quocs-lib-0.0a18/src/quocs_lib.egg-info/SOURCES.txt` & `quocs-lib-0.0a19/src/quocs_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/Controls.py` & `quocs-lib-0.0a19/src/quocslib/Controls.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/Optimizer.py` & `quocs-lib-0.0a19/src/quocslib/Optimizer.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/communication/AllInOneCommunication.py` & `quocs-lib-0.0a19/src/quocslib/communication/AllInOneCommunication.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/figureofmeritevaluation/AbstractFom.py` & `quocs-lib-0.0a19/src/quocslib/figureofmeritevaluation/AbstractFom.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/gradientfreemethods/CMAES.py` & `quocs-lib-0.0a19/src/quocslib/gradientfreemethods/CMAES.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/gradientfreemethods/DirectSearchMethod.py` & `quocs-lib-0.0a19/src/quocslib/gradientfreemethods/DirectSearchMethod.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/gradientfreemethods/GradientFreeTemplate.py` & `quocs-lib-0.0a19/src/quocslib/gradientfreemethods/GradientFreeTemplate.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/gradientfreemethods/NelderMead.py` & `quocs-lib-0.0a19/src/quocslib/gradientfreemethods/NelderMead.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/handleexit/AbstractHandleExit.py` & `quocs-lib-0.0a19/src/quocslib/handleexit/AbstractHandleExit.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/handleexit/HandleExit.py` & `quocs-lib-0.0a19/src/quocslib/handleexit/HandleExit.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/noiseprocesses/ornsteinuhlenbeckprocess.py` & `quocs-lib-0.0a19/src/quocslib/noiseprocesses/ornsteinuhlenbeckprocess.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/OneQubitProblem.py` & `quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/OneQubitProblem.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/OneQubitProblem_2fields.py` & `quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/OneQubitProblem_2fields.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/RosenbrockProblem.py` & `quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/RosenbrockProblem.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimalcontrolproblems/su2.py` & `quocs-lib-0.0a19/src/quocslib/optimalcontrolproblems/su2.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/ADAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/ADAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/AlgorithmTemplate.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/AlgorithmTemplate.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/DirectSearchAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/DirectSearchAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/GRAPEAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/GRAPEAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/OptimizationAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/OptimizationAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/dCRABAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/dCRABAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/optimizationalgorithms/dCRABNoisyAlgorithm.py` & `quocs-lib-0.0a19/src/quocslib/optimizationalgorithms/dCRABNoisyAlgorithm.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/parameters/BaseParameter.py` & `quocs-lib-0.0a19/src/quocslib/parameters/BaseParameter.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/parameters/Parameter.py` & `quocs-lib-0.0a19/src/quocslib/parameters/Parameter.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/parameters/TimeParameter.py` & `quocs-lib-0.0a19/src/quocslib/parameters/TimeParameter.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/BasePulse.py` & `quocs-lib-0.0a19/src/quocslib/pulses/BasePulse.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/Chebyshev.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/Chebyshev.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/ChoppedBasis.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/ChoppedBasis.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/DummyBasis.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/DummyBasis.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/Fourier.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/Fourier.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/PiecewiseBasis.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/PiecewiseBasis.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/Sigmoid.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/Sigmoid.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/basis/Walsh.py` & `quocs-lib-0.0a19/src/quocslib/pulses/basis/Walsh.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/superparameter/SuperParameterDistribution.py` & `quocs-lib-0.0a19/src/quocslib/pulses/superparameter/SuperParameterDistribution.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/pulses/superparameter/Uniform.py` & `quocs-lib-0.0a19/src/quocslib/pulses/superparameter/Uniform.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/stoppingcriteria/CMAESStoppingCriteria.py` & `quocs-lib-0.0a19/src/quocslib/stoppingcriteria/CMAESStoppingCriteria.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/stoppingcriteria/NelderMeadStoppingCriteria.py` & `quocs-lib-0.0a19/src/quocslib/stoppingcriteria/NelderMeadStoppingCriteria.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/stoppingcriteria/StoppingCriteria.py` & `quocs-lib-0.0a19/src/quocslib/stoppingcriteria/StoppingCriteria.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/timeevolution/piecewise_integrator.py` & `quocs-lib-0.0a19/src/quocslib/timeevolution/piecewise_integrator.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/tools/linearalgebra.py` & `quocs-lib-0.0a19/src/quocslib/tools/linearalgebra.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/tools/logger.py` & `quocs-lib-0.0a19/src/quocslib/tools/logger.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/tools/pulsetools.py` & `quocs-lib-0.0a19/src/quocslib/tools/pulsetools.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/tools/randomgenerator.py` & `quocs-lib-0.0a19/src/quocslib/tools/randomgenerator.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/AbstractDump.py` & `quocs-lib-0.0a19/src/quocslib/utils/AbstractDump.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/AbstractFoM.py` & `quocs-lib-0.0a19/src/quocslib/utils/AbstractFoM.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/AbstractHandleExit.py` & `quocs-lib-0.0a19/src/quocslib/utils/AbstractHandleExit.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/BestDump.py` & `quocs-lib-0.0a19/src/quocslib/utils/BestDump.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/DummyDump.py` & `quocs-lib-0.0a19/src/quocslib/utils/DummyDump.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/FilesUpdateFom.py` & `quocs-lib-0.0a19/src/quocslib/utils/FilesUpdateFom.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/dynamicimport.py` & `quocs-lib-0.0a19/src/quocslib/utils/dynamicimport.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/inputoutput.py` & `quocs-lib-0.0a19/src/quocslib/utils/inputoutput.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/logger.py` & `quocs-lib-0.0a19/src/quocslib/utils/logger.py`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/map_dictionary.json` & `quocs-lib-0.0a19/src/quocslib/utils/map_dictionary.json`

 * *Files identical despite different names*

### Comparing `quocs-lib-0.0a18/src/quocslib/utils/test_BestDump.py` & `quocs-lib-0.0a19/src/quocslib/utils/test_BestDump.py`

 * *Files 2% similar despite different names*

```diff
@@ -36,14 +36,15 @@
 
     outfile_path = os.path.join(dump_obj.best_controls_path, "000_best_controls.npz")
     controls = np.load(outfile_path)
     # print(controls.files)
     assert (controls["pulse1"] == test_pulse).all()
     assert (controls["time_grid1"] == test_timegrid).all()
     assert (controls["parameter1"] == test_params).all()
+    os.chmod(outfile_path, 0o777)
     os.remove(outfile_path)
 
 
 def test_dump_controls_NO_record():
 
     folder = os.path.dirname(os.path.realpath(__file__))
     dump_obj = BestDump(folder, "111")
```

