# Comparing `tmp/tsml-0.0.4.tar.gz` & `tmp/tsml-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tsml-0.0.4.tar", last modified: Mon Mar 27 18:45:51 2023, max compression
+gzip compressed data, was "tsml-0.0.5.tar", last modified: Thu Apr  6 15:04:25 2023, max compression
```

## Comparing `tsml-0.0.4.tar` & `tsml-0.0.5.tar`

### file list

```diff
@@ -1,96 +1,97 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-03-27 18:45:40.000000 tsml-0.0.4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-03-27 18:45:40.000000 tsml-0.0.4/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-03-27 18:45:51.311597 tsml-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-27 18:45:40.000000 tsml-0.0.4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2067 2023-03-27 18:45:40.000000 tsml-0.0.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-27 18:45:51.311597 tsml-0.0.4/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.299597 tsml-0.0.4/tsml/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10672 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/convolution_based/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/convolution_based/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/EqualMinimalJapaneseVowels/
--rw-r--r--   0 runner    (1001) docker     (123)   120661 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)   120799 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TRAIN.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/MinimalChinatown/
--rw-r--r--   0 runner    (1001) docker     (123)     3389 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalChinatown/MinimalChinatown_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)     3381 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalChinatown/MinimalChinatown_TRAIN.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/MinimalGasPrices/
--rw-r--r--   0 runner    (1001) docker     (123)     2709 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)     2711 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TRAIN.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/MinimalJapaneseVowels/
--rw-r--r--   0 runner    (1001) docker     (123)    36247 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)    38758 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TRAIN.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/UnequalMinimalChinatown/
--rw-r--r--   0 runner    (1001) docker     (123)     3309 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TRAIN.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/datasets/UnequalMinimalGasPrices/
--rw-r--r--   0 runner    (1001) docker     (123)     2697 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TEST.ts
--rw-r--r--   0 runner    (1001) docker     (123)     2700 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TRAIN.ts
--rw-r--r--   0 runner    (1001) docker     (123)      580 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24759 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/datasets/_data_io.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/deep_learning/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/deep_learning/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       66 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/deep_learning/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml/dictionary_based/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/dictionary_based/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/distance_based/
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/distance_based/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/dummy/
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/dummy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11180 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/dummy/_dummy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/feature_based/
--rw-r--r--   0 runner    (1001) docker     (123)      217 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/feature_based/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14818 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/feature_based/_catch22_classifier.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/interval_based/
--rw-r--r--   0 runner    (1001) docker     (123)      936 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    41848 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11536 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_cif.py
--rw-r--r--   0 runner    (1001) docker     (123)     5662 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_interval_forest.py
--rw-r--r--   0 runner    (1001) docker     (123)    21635 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_interval_pipelines.py
--rw-r--r--   0 runner    (1001) docker     (123)     5533 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_rise.py
--rw-r--r--   0 runner    (1001) docker     (123)     5772 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_stsf.py
--rw-r--r--   0 runner    (1001) docker     (123)     5307 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/interval_based/_tsf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/shapelet_based/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/shapelet_based/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12784 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/shapelet_based/_stc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.307597 tsml-0.0.4/tsml/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    81457 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/tests/_sklearn_checks.py
--rw-r--r--   0 runner    (1001) docker     (123)     7941 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/tests/estimator_checks.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/tests/test_all_estimators.py
--rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/tests/test_interface.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/tsml/transformations/
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    46093 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_catch22.py
--rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_function_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    34576 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_interval_extraction.py
--rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_periodogram.py
--rw-r--r--   0 runner    (1001) docker     (123)    41527 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_sfa.py
--rw-r--r--   0 runner    (1001) docker     (123)    23960 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_shapelet_transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/transformations/_summary_features.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/tsml/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       46 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2447 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)     4358 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/discovery.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/tsml/utils/numba_functions/
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/numba_functions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5167 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/numba_functions/general.py
--rw-r--r--   0 runner    (1001) docker     (123)    19873 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/numba_functions/stats.py
--rw-r--r--   0 runner    (1001) docker     (123)     7781 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/testing.py
--rw-r--r--   0 runner    (1001) docker     (123)    22204 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/utils/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/tsml/vector/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/vector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15951 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/vector/_cit.py
--rw-r--r--   0 runner    (1001) docker     (123)    18576 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/vector/_rotation_forest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.311597 tsml-0.0.4/tsml/vector/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/vector/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      903 2023-03-27 18:45:40.000000 tsml-0.0.4/tsml/vector/tests/test_rotation_forest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 18:45:51.303597 tsml-0.0.4/tsml.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-03-27 18:45:51.000000 tsml-0.0.4/tsml.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2484 2023-03-27 18:45:51.000000 tsml-0.0.4/tsml.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 18:45:51.000000 tsml-0.0.4/tsml.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-27 18:45:51.000000 tsml-0.0.4/tsml.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-27 18:45:51.000000 tsml-0.0.4/tsml.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.716956 tsml-0.0.5/
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-04-06 15:04:12.000000 tsml-0.0.5/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 15:04:12.000000 tsml-0.0.5/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-04-06 15:04:25.716956 tsml-0.0.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 15:04:12.000000 tsml-0.0.5/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2110 2023-04-06 15:04:12.000000 tsml-0.0.5/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:04:25.716956 tsml-0.0.5/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10672 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml/convolution_based/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/convolution_based/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml/datasets/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml/datasets/EqualMinimalJapaneseVowels/
+-rw-r--r--   0 runner    (1001) docker     (123)   120661 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)   120799 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TRAIN.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml/datasets/MinimalChinatown/
+-rw-r--r--   0 runner    (1001) docker     (123)     3389 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalChinatown/MinimalChinatown_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     3381 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalChinatown/MinimalChinatown_TRAIN.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/datasets/MinimalGasPrices/
+-rw-r--r--   0 runner    (1001) docker     (123)     2709 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     2711 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TRAIN.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/datasets/MinimalJapaneseVowels/
+-rw-r--r--   0 runner    (1001) docker     (123)    36247 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)    38758 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TRAIN.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/datasets/UnequalMinimalChinatown/
+-rw-r--r--   0 runner    (1001) docker     (123)     3309 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     3272 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TRAIN.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/datasets/UnequalMinimalGasPrices/
+-rw-r--r--   0 runner    (1001) docker     (123)     2697 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TEST.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     2700 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TRAIN.ts
+-rw-r--r--   0 runner    (1001) docker     (123)      580 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24759 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/datasets/_data_io.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/deep_learning/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/deep_learning/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       66 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/deep_learning/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/dictionary_based/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/dictionary_based/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/distance_based/
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/distance_based/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/dummy/
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/dummy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11177 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/dummy/_dummy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/feature_based/
+-rw-r--r--   0 runner    (1001) docker     (123)      206 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/feature_based/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15184 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/feature_based/_catch22.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/interval_based/
+-rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45975 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14260 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_cif.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5662 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_interval_forest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21635 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_interval_pipelines.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5479 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_rise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7091 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_stsf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5297 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/interval_based/_tsf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.708956 tsml-0.0.5/tsml/shapelet_based/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/shapelet_based/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12781 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/shapelet_based/_stc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.712956 tsml-0.0.5/tsml/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    81471 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/tests/_sklearn_checks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7690 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/tests/estimator_checks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/tests/test_all_estimators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2601 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/tests/test_interface.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.712956 tsml-0.0.5/tsml/transformations/
+-rw-r--r--   0 runner    (1001) docker     (123)      970 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1421 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_ar_coefficient.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46093 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_catch22.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3204 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_function_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34766 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_interval_extraction.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1844 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_periodogram.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41527 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_sfa.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23960 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_shapelet_transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/transformations/_summary_features.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.712956 tsml-0.0.5/tsml/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2447 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4358 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/discovery.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.712956 tsml-0.0.5/tsml/utils/numba_functions/
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/numba_functions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5898 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/numba_functions/general.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19873 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/numba_functions/stats.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7782 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/testing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22204 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/utils/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.712956 tsml-0.0.5/tsml/vector/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/vector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15951 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/vector/_cit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18576 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/vector/_rotation_forest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.716956 tsml-0.0.5/tsml/vector/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/vector/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      903 2023-04-06 15:04:12.000000 tsml-0.0.5/tsml/vector/tests/test_rotation_forest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:04:25.704956 tsml-0.0.5/tsml.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-04-06 15:04:25.000000 tsml-0.0.5/tsml.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2513 2023-04-06 15:04:25.000000 tsml-0.0.5/tsml.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:04:25.000000 tsml-0.0.5/tsml.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-04-06 15:04:25.000000 tsml-0.0.5/tsml.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 15:04:25.000000 tsml-0.0.5/tsml.egg-info/top_level.txt
```

### Comparing `tsml-0.0.4/LICENSE` & `tsml-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/PKG-INFO` & `tsml-0.0.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tsml
-Version: 0.0.4
+Version: 0.0.5
 Summary: A toolkit for time series machine learning algorithms.
 Author-email: Matthew Middlehurst <m.middlehurst@uea.ac.uk>, Tony Bagnall <ajb@uea.ac.uk>
 License: BSD 3-Clause License
         
         Copyright (c) The Time Series Machine Learning (tsml) developers.
         All rights reserved.
```

### Comparing `tsml-0.0.4/pyproject.toml` & `tsml-0.0.5/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "tsml"
-version = "0.0.4"
+version = "0.0.5"
 description = "A toolkit for time series machine learning algorithms."
 authors = [
     {name = "Matthew Middlehurst", email = "m.middlehurst@uea.ac.uk"},
     {name = "Tony Bagnall", email = "ajb@uea.ac.uk"},
 ]
 readme = "README.md"
 requires-python = ">=3.8,<3.11"
@@ -38,16 +38,17 @@
     "numba>=0.55",
     "numpy>=1.21.0",
     "scikit-learn>=1.0.2",
 ]
 
 [project.optional-dependencies]
 extras = [
-    "pycatch22",
-    "pyfftw"
+    "pycatch22>=0.4.2",
+    "pyfftw>=0.12.0",
+    "statsmodels>=0.12.1",
 ]
 dev = [
     "pre-commit",
     "pytest",
     "pytest-randomly",
     "pytest-timeout",
     "pytest-xdist",
```

### Comparing `tsml-0.0.4/tsml/base.py` & `tsml-0.0.5/tsml/base.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TEST.ts` & `tsml-0.0.5/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/EqualMinimalJapaneseVowels/EqualMinimalJapaneseVowels_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalChinatown/MinimalChinatown_TEST.ts` & `tsml-0.0.5/tsml/datasets/MinimalChinatown/MinimalChinatown_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalChinatown/MinimalChinatown_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/MinimalChinatown/MinimalChinatown_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TEST.ts` & `tsml-0.0.5/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/MinimalGasPrices/MinimalGasPrices_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TEST.ts` & `tsml-0.0.5/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/MinimalJapaneseVowels/MinimalJapaneseVowels_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TEST.ts` & `tsml-0.0.5/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/UnequalMinimalChinatown/UnequalMinimalChinatown_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TEST.ts` & `tsml-0.0.5/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TEST.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TRAIN.ts` & `tsml-0.0.5/tsml/datasets/UnequalMinimalGasPrices/UnequalMinimalGasPrices_TRAIN.ts`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/__init__.py` & `tsml-0.0.5/tsml/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/datasets/_data_io.py` & `tsml-0.0.5/tsml/datasets/_data_io.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/dummy/_dummy.py` & `tsml-0.0.5/tsml/dummy/_dummy.py`

 * *Files 1% similar despite different names*

```diff
@@ -100,15 +100,15 @@
 
         self.classes_ = np.unique(y)
         self.n_classes_ = self.classes_.shape[0]
         self.class_dictionary_ = {}
         for index, classVal in enumerate(self.classes_):
             self.class_dictionary_[classVal] = index
 
-        if len(self.classes_) == 1:
+        if self.n_classes_ == 1:
             return self
 
         self._clf = SklearnDummyClassifier(
             strategy=self.strategy,
             random_state=self.random_state,
             constant=self.constant,
         )
@@ -116,20 +116,20 @@
 
         return self
 
     def predict(self, X) -> np.ndarray:
         """"""
         check_is_fitted(self)
 
+        X = self._validate_data(X=X, reset=False, ensure_min_series_length=1)
+
         # treat case of single class seen in fit
         if self.n_classes_ == 1:
             return np.repeat(list(self.class_dictionary_.keys()), X.shape[0], axis=0)
 
-        X = self._validate_data(X=X, reset=False, ensure_min_series_length=1)
-
         return self._clf.predict(np.zeros(X.shape))
 
     def predict_proba(self, X) -> np.ndarray:
         """"""
         check_is_fitted(self)
 
         # treat case of single class seen in fit
```

### Comparing `tsml-0.0.4/tsml/feature_based/_catch22_classifier.py` & `tsml-0.0.5/tsml/feature_based/_catch22.py`

 * *Files 2% similar despite different names*

```diff
@@ -119,14 +119,17 @@
         self.n_instances_, self.n_dims_, self.series_length_ = X.shape
         self.classes_ = np.unique(y)
         self.n_classes_ = self.classes_.shape[0]
         self.class_dictionary_ = {}
         for index, classVal in enumerate(self.classes_):
             self.class_dictionary_[classVal] = index
 
+        if self.n_classes_ == 1:
+            return self
+
         self._n_jobs = check_n_jobs(self.n_jobs)
 
         self._transformer = Catch22Transformer(
             features=self.features,
             catch24=self.catch24,
             outlier_norm=self.outlier_norm,
             replace_nans=self.replace_nans,
@@ -160,14 +163,18 @@
         Returns
         -------
         y : array-like, shape = [n_instances]
             Predicted class labels.
         """
         check_is_fitted(self)
 
+        # treat case of single class seen in fit
+        if self.n_classes_ == 1:
+            return np.repeat(list(self.class_dictionary_.keys()), X.shape[0], axis=0)
+
         X = self._validate_data(X=X, reset=False)
 
         return self._estimator.predict(self._transformer.transform(X))
 
     def predict_proba(self, X) -> np.ndarray:
         """Predict class probabilities for n instances in X.
 
@@ -179,14 +186,18 @@
         Returns
         -------
         y : array-like, shape = [n_instances, n_classes_]
             Predicted probabilities using the ordering in classes_.
         """
         check_is_fitted(self)
 
+        # treat case of single class seen in fit
+        if self.n_classes_ == 1:
+            return np.repeat([[1]], X.shape[0], axis=0)
+
         X = self._validate_data(X=X, reset=False)
 
         m = getattr(self._estimator, "predict_proba", None)
         if callable(m):
             return self._estimator.predict_proba(self._transformer.transform(X))
         else:
             dists = np.zeros((X.shape[0], self.n_classes_))
```

### Comparing `tsml-0.0.4/tsml/interval_based/__init__.py` & `tsml-0.0.5/tsml/interval_based/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,34 +1,41 @@
 # -*- coding: utf-8 -*-
 """Interval based estimators."""
 
 __all__ = [
     "BaseIntervalForest",
     "CIFClassifier",
     "CIFRegressor",
-    # "DrCIFClassifier",
-    # "DrCIFRegressor",
+    "DrCIFClassifier",
+    "DrCIFRegressor",
     "IntervalForestClassifier",
     "IntervalForestRegressor",
     "RandomIntervalClassifier",
     "RandomIntervalRegressor",
     "SupervisedIntervalClassifier",
-    # "RISEClassifier",
-    # "RISERegressor",
-    # "STSFClassifier",
-    # "RSTSFClassifier",
+    "RISEClassifier",
+    "RISERegressor",
+    "STSFClassifier",
+    "RSTSFClassifier",
     "TSFClassifier",
     "TSFRegressor",
 ]
 
 from tsml.interval_based._base import BaseIntervalForest
-from tsml.interval_based._cif import CIFClassifier, CIFRegressor
+from tsml.interval_based._cif import (
+    CIFClassifier,
+    CIFRegressor,
+    DrCIFClassifier,
+    DrCIFRegressor,
+)
 from tsml.interval_based._interval_forest import (
     IntervalForestClassifier,
     IntervalForestRegressor,
 )
 from tsml.interval_based._interval_pipelines import (
     RandomIntervalClassifier,
     RandomIntervalRegressor,
     SupervisedIntervalClassifier,
 )
+from tsml.interval_based._rise import RISEClassifier, RISERegressor
+from tsml.interval_based._stsf import RSTSFClassifier, STSFClassifier
 from tsml.interval_based._tsf import TSFClassifier, TSFRegressor
```

### Comparing `tsml-0.0.4/tsml/interval_based/_base.py` & `tsml-0.0.5/tsml/interval_based/_base.py`

 * *Files 7% similar despite different names*

```diff
@@ -8,17 +8,23 @@
 import time
 import warnings
 from abc import ABCMeta, abstractmethod
 
 import numpy as np
 from joblib import Parallel
 from sklearn.base import BaseEstimator, is_classifier, is_regressor
-from sklearn.tree import BaseDecisionTree, DecisionTreeClassifier, DecisionTreeRegressor
+from sklearn.tree import (
+    BaseDecisionTree,
+    DecisionTreeClassifier,
+    DecisionTreeRegressor,
+    ExtraTreeClassifier,
+)
 from sklearn.utils import check_random_state
 from sklearn.utils.fixes import delayed
+from sklearn.utils.multiclass import check_classification_targets
 from sklearn.utils.validation import check_is_fitted
 
 from tsml.base import BaseTimeSeriesEstimator, _clone_estimator
 from tsml.transformations._interval_extraction import (
     RandomIntervalTransformer,
     SupervisedIntervalTransformer,
 )
@@ -29,65 +35,86 @@
 
 class BaseIntervalForest(BaseTimeSeriesEstimator, metaclass=ABCMeta):
     """A base class for interval extracting forest estimators.
 
     Allows the implementation of classifiers and regressors along the lines of [1][2][3]
     which extract intervals and create an ensemble from the subsequent features.
 
-        Extension of the CIF algorithm using multple representations. Implementation of the
-    interval based forest making use of the catch22 feature set on randomly selected
-    intervals on the base series, periodogram representation and differences
-    representation described in the HIVE-COTE 2.0 paper Middlehurst et al (2021). [1]_
-
-    Overview: Input "n" series with "d" channels of length "m".
-    For each tree
-        - Sample n_intervals intervals per representation of random position and length
-        - Subsample att_subsample_size catch22 or summary statistic attributes randomly
-        - Randomly select channel for each interval
-        - Calculate attributes for each interval from its representation, concatenate
-          to form new data set
-        - Build decision tree on new data set
-    Ensemble the trees with averaged probability estimates
+    #skipping predict todo
 
     Parameters
     ----------
-    base_estimator : BaseEstimator
-        Base estimator for the ensemble, can be supplied a sklearn BaseEstimator or a
-        string for suggested options.
-    estimator_type : str
-
-        self.interval_selection_method = interval_selection_method
-        self.n_intervals = n_intervals
-        self.min_interval_length = min_interval_length
-        self.max_interval_length = max_interval_length
-        self.interval_features = interval_features
-        self.series_transformers = series_transformers
-        self.att_subsample_size = att_subsample_size
-        self.replace_nan = replace_nan
-
+    base_estimator : BaseEstimator or None, default=None
+        scikit-learn BaseEstimator used to build the interval ensemble. If None, uses a
+        simple decision tree.
     n_estimators : int, default=200
         Number of estimators to build for the ensemble.
-    interval_selection_method :
-
-    n_intervals : int, length 3 list of int or None, default=None
-        Number of intervals to extract per representation per tree as an int for all
-        representations or list for individual settings, if None extracts
-        (4 + (sqrt(representation_length) * sqrt(n_dims)) / 3) intervals.
-    min_interval_length : int or length 3 list of int, default=4
-        Minimum length of an interval per representation as an int for all
-        representations or list for individual settings.
-    max_interval_length : int, length 3 list of int or None, default=None
-        Maximum length of an interval per representation as an int for all
-        representations or list for individual settings, if None set to
-        (representation_length / 2).
-    interval_features :
-
-    series_transformers :
+    interval_selection_method : "random", "supervised" or "random-supervised",
+            default="random"
+        The interval selection transformer to use.
+            - "random" uses a RandomIntervalTransformer.
+            - "supervised" uses a SupervisedIntervalTransformer.
+            - "random-supervised" uses a SupervisedIntervalTransformer with
+                randomised elements.
+
+        Supervised methods can only be used for classification tasks, and require
+        function inputs for interval_features rather than transformers.
+    n_intervals : int, str, list or tuple, default="sqrt"
+        Number of intervals to extract per tree for each series_transformers series.
+
+        An int input will extract that number of intervals from the series, while a str
+        input will return a function of the series length (may differ per
+        series_transformers output) to extract that number of intervals.
+        Valid str inputs are:
+            - "sqrt" : square root of the series length.
+            - "sqrt-div" : sqrt of series length divided by the number
+                of series_transformers.
+
+        A list or tuple of ints and/or strs will extract the number of intervals using
+        the above rules and sum the results for the final n_intervals. i.e. [4, "sqrt"]
+        will extract sqrt(series_length) + 4 intervals.
+
+        Different number of intervals for each series_transformers series can be
+        specified using a nested list or tuple. Any list or tuple input containing
+        another list or tuple must be the same length as the number of
+        series_transformers.
+
+        %todo random vs supervised
+    min_interval_length : int, float, list, or tuple, default=3
+        Minimum length of intervals to extract from series. float inputs take a
+        proportion of the series length to use as the minimum interval length.
+
+        Different minimum interval lengths for each series_transformers series can be
+        specified using a list or tuple. Any list or tuple input must be the same length
+        as the number of series_transformers.
+    max_interval_length : int, float, list, or tuple, default=np.inf
+        Maximum length of intervals to extract from series. float inputs take a
+        proportion of the series length to use as the maximum interval length.
+
+        Different maximum interval lengths for each series_transformers series can be
+        specified using a list or tuple. Any list or tuple input must be the same length
+        as the number of series_transformers.
+
+        Ignored for supervised interval_selection_method inputs.
+    interval_features : TransformerMixin, callable, list, tuple, or None, default=None
+        The features to extract from the intervals using transformers or callable
+        functions. If None, uses the mean, standard deviation, and slope of the series.
+
+        Both transformers and functions should be able to take a 2d np.ndarray input.
+        Functions should output a 1d array (the feature for each series) and
+        transformers should output a 2d array where rows are the features for each
+        series. A list or tuple of transformers and/or functions will extract all
+        features and concatenate the output.
+
+        Different features for each series_transformers series can be specified using a
+        nested list or tuple. Any list or tuple input containing another list or tuple
+        must be the same length as the number of series_transformers.
+    series_transformers : TransformerMixin, list, tuple, or None, default=None
 
-    att_subsample_size : int, default=10
+    att_subsample_size : int or None, default=None
         Number of catch22 or summary statistic attributes to subsample per tree.
     replace_nan :
 
     time_limit_in_minutes : int, default=0
         Time contract to limit build time in minutes, overriding n_estimators.
         Default of 0 means n_estimators is used.
     contract_max_n_estimators : int, default=500
@@ -136,15 +163,15 @@
     .. [2]
     .. [3]
     """
 
     @abstractmethod
     def __init__(
         self,
-        base_estimator,
+        base_estimator=None,
         n_estimators=200,
         interval_selection_method="random",
         n_intervals="sqrt",
         min_interval_length=3,
         max_interval_length=np.inf,
         interval_features=None,
         series_transformers=None,
@@ -179,49 +206,57 @@
     # transformer_feature_names to allow features to be subsampled
     transformer_feature_selection = ["features"]
     transformer_feature_names = ["features_arguments_", "_features_arguments"]
     # an interval_features transformer must contain one of these attribute names to
     # be able to skip transforming features in predict
     transformer_feature_skip = ["transform_features_", "_transform_features"]
 
-    _tags = {
-        "capability:multivariate": True,
-        "capability:train_estimate": True,
-        "capability:contractable": True,
-        "capability:multithreading": True,
-    }
-
     def fit(self, X, y):
         X, y = self._validate_data(X=X, y=y, ensure_min_samples=2)
         X = self._convert_X(X)
 
         self.n_instances_, self.n_dims_, self.series_length_ = X.shape
         if is_classifier(self):
+            check_classification_targets(y)
+
             self.classes_ = np.unique(y)
             self.n_classes_ = self.classes_.shape[0]
             self.class_dictionary_ = {}
             for index, classVal in enumerate(self.classes_):
                 self.class_dictionary_[classVal] = index
 
+            if self.n_classes_ == 1:
+                return self
+
+        self._base_estimator = self.base_estimator
         if self.base_estimator is None:
+            from tsml.interval_based import RSTSFClassifier
+
             # default base_estimators for classification and regression
-            if not hasattr(self, "_base_estimator"):
-                if is_classifier(self):
-                    self._base_estimator = DecisionTreeClassifier(criterion="entropy")
-                elif is_regressor(self):
-                    self._base_estimator = DecisionTreeRegressor(
-                        criterion="absolute_error"
-                    )
-                else:
-                    raise ValueError()  # todo error for invalid self.base_estimator
-            elif not isinstance(self._base_estimator, BaseEstimator):
-                raise ValueError()  # todo error for invalid self.base_estimator
+            if isinstance(self, RSTSFClassifier):
+                self._base_estimator = ExtraTreeClassifier(
+                    criterion="entropy",
+                    class_weight="balanced",
+                    max_features="sqrt",
+                )
+            elif is_classifier(self):
+                self._base_estimator = DecisionTreeClassifier(criterion="entropy")
+            elif is_regressor(self):
+                self._base_estimator = DecisionTreeRegressor(criterion="absolute_error")
+            else:
+                raise ValueError(
+                    f"{self} must be a scikit-learn compatible classifier or "
+                    "regressor."
+                )
         # base_estimator must be an sklearn estimator
         elif not isinstance(self.base_estimator, BaseEstimator):
-            raise ValueError()  # todo error for invalid self.base_estimator
+            raise ValueError(
+                "base_estimator must be a scikit-learn BaseEstimator or None. "
+                f"Found: {self.base_estimator}"
+            )
 
         # use the base series if series_transformers is None
         if self.series_transformers is None or self.series_transformers == []:
             Xt = [X]
             self._series_transformers = [None]
         # clone series_transformers if it is a transformer and transform the input data
         elif is_transformer(self.series_transformers):
@@ -250,42 +285,47 @@
         else:
             raise ValueError()  # todo error for invalid self.series_transformers
 
         # if only a single n_intervals value is passed it must be an int or str
         if isinstance(self.n_intervals, (int, str)):
             n_intervals = [[self.n_intervals]] * len(Xt)
         elif isinstance(self.n_intervals, (list, tuple)):
-            # if only one series_transformer is used, n_intervals can be a list of
-            # multiple n_intervals options to be applied
-            if len(Xt) == 1:
-                for method in self.n_intervals:
-                    if not isinstance(method, (int, str)):
-                        raise ValueError()  # todo error for invalid self.n_intervals
-                n_intervals = [self.n_intervals]
-            # if more than one series_transformer is used, n_intervals must have the
-            # same number of items if it is a list
+            # if input is a list and only contains ints or strs, use the list for all
+            # series in Xt
+            if all(isinstance(item, (int, str)) for item in self.n_intervals):
+                n_intervals = [self.n_intervals] * len(Xt)
+            # other lists must be the same length as Xt
             elif len(self.n_intervals) != len(Xt):
-                raise ValueError()  # todo error for invalid self.n_intervals
+                raise ValueError(
+                    "n_intervals as a list or tuple containing other lists or tuples "
+                    "must be the same length as series_transformers."
+                )
             # list items can be a list of items or a single item for each
             # series_transformer, but each individual item must be an int or str
             else:
                 n_intervals = []
-                for features in self.n_intervals:
-                    if isinstance(features, (list, tuple)):
-                        for method in features:
-                            if not isinstance(method, (int, str)):
-                                raise ValueError()  # todo error for invalid self.n_intervals
-                        n_intervals.append(features)
-                    elif isinstance(features, (int, str)):
-                        n_intervals.append([features])
+                for items in self.n_intervals:
+                    if isinstance(items, (list, tuple)):
+                        if not all(isinstance(item, (int, str)) for item in items):
+                            raise ValueError(
+                                "Individual items in a n_intervals list or tuple must "
+                                f"be an int or str. Input {items} does not contain "
+                                "only ints or strs"
+                            )
+                        n_intervals.append(items)
+                    elif isinstance(items, (int, str)):
+                        n_intervals.append([items])
                     else:
-                        raise ValueError()  # todo error for invalid self.n_intervals
+                        raise ValueError(
+                            "Individual items in a n_intervals list or tuple must be "
+                            f"an int or str. Found: {items}"
+                        )
         # other inputs are invalid
         else:
-            raise ValueError()  # todo error for invalid self.n_intervals
+            raise ValueError(f"Invalid n_intervals input. Found {self.n_intervals}")
 
         # add together the number of intervals for each series_transformer
         # str input must be one of a set valid options
         self._n_intervals = [0] * len(Xt)
         for i, series in enumerate(Xt):
             for method in n_intervals[i]:
                 if isinstance(method, int):
@@ -299,94 +339,113 @@
                     # sqrt of series length divided by the number of series_transformers
                     elif method.lower() == "sqrt-div":
                         self._n_intervals[i] += int(
                             (np.sqrt(series.shape[2]) * np.sqrt(series.shape[1]))
                             / len(Xt)
                         )
                     else:
-                        raise ValueError()  # todo error for invalid self.n_intervals string
+                        raise ValueError(
+                            "Invalid str input for n_intervals. Must be "
+                            f'("sqrt","sqrt-div"). Found {method}'
+                        )
 
         # each series_transformer must have at least 1 interval extracted
         for i, n in enumerate(self._n_intervals):
             if n <= 0:
                 self._n_intervals[i] = 1
 
         self.total_intervals_ = sum(self._n_intervals)
 
         # minimum interval length
         if isinstance(self.min_interval_length, int):
             self._min_interval_length = [self.min_interval_length] * len(Xt)
         # min_interval_length must be at less than one if it is a float (proportion of
-        # total attributed to subsample)
+        # of the series length)
         elif (
             isinstance(self.min_interval_length, float)
             and self.min_interval_length <= 1
         ):
             self._min_interval_length = [
                 int(self.min_interval_length * t.shape[2]) for t in Xt
             ]
         # if the input is a list, it must be the same length as the number of
         # series_transformers
         # list values must be ints or floats. The same checks as above are performed
         elif isinstance(self.min_interval_length, (list, tuple)):
-            if len(self.min_interval_length) == len(Xt):
-                raise ValueError()  # todo error for invalid self.min_interval_length string
+            if len(self.min_interval_length) != len(Xt):
+                raise ValueError(
+                    "min_interval_length as a list or tuple must be the same length "
+                    "as series_transformers."
+                )
 
             self._min_interval_length = []
             for i, length in enumerate(self.min_interval_length):
                 if isinstance(length, float) and length <= 1:
                     self._min_interval_length.append(int(length * Xt[i].shape[2]))
                 elif isinstance(length, int):
                     self._min_interval_length.append(length)
                 else:
-                    raise ValueError()  # todo error for invalid self.min_interval_length string
+                    raise ValueError(
+                        "min_interval_length list items must be int or floats. "
+                        f"Found {length}"
+                    )
         # other inputs are invalid
         else:
-            raise ValueError()  # todo error for invalid self.min_interval_length string
+            raise ValueError(
+                f"Invalid min_interval_length input. Found {self.min_interval_length}"
+            )
 
         # min_interval_length cannot be less than 3 or greater than the series length
         for i, n in enumerate(self._min_interval_length):
             if n > Xt[i].shape[2]:
                 self._min_interval_length[i] = Xt[i].shape[2]
             elif n < 3:
                 self._min_interval_length[i] = 3
 
         # maximum interval length
         if (
             isinstance(self.max_interval_length, int)
             or self.max_interval_length == np.inf
         ):
             self._max_interval_length = [self.max_interval_length] * len(Xt)
-        # max_interval_length must be at less than one if it is a float (proportion of
-        # total attributed to subsample)
+        # max_interval_length must be at less than one if it is a float  (proportion of
+        # of the series length)
         elif (
             isinstance(self.max_interval_length, float)
             and self.max_interval_length <= 1
         ):
             self._max_interval_length = [
                 int(self.max_interval_length * t.shape[2]) for t in Xt
             ]
         # if the input is a list, it must be the same length as the number of
         # series_transformers
         # list values must be ints or floats. The same checks as above are performed
         elif isinstance(self.max_interval_length, (list, tuple)):
-            if len(self.max_interval_length) == len(Xt):
-                raise ValueError()  # todo error for invalid self.max_interval_length string
+            if len(self.max_interval_length) != len(Xt):
+                raise ValueError(
+                    "max_interval_length as a list or tuple must be the same length "
+                    "as series_transformers."
+                )
 
             self._max_interval_length = []
             for i, length in enumerate(self.max_interval_length):
                 if isinstance(length, float) and length <= 1:
                     self._max_interval_length.append(int(length * Xt[i].shape[2]))
                 elif isinstance(length, int):
                     self._max_interval_length.append(length)
                 else:
-                    raise ValueError()  # todo error for invalid self.max_interval_length string
+                    raise ValueError(
+                        "max_interval_length list items must be int or floats. "
+                        f"Found {length}"
+                    )
         # other inputs are invalid
         else:
-            raise ValueError()  # todo error for invalid self.max_interval_length string
+            raise ValueError(
+                f"Invalid max_interval_length input. Found {self.max_interval_length}"
+            )
 
         # max_interval_length cannot be less than min_interval_length or greater than
         # the series length
         for i, n in enumerate(self._max_interval_length):
             if n < self._min_interval_length[i]:
                 self._max_interval_length[i] = self._min_interval_length[i]
             elif n > Xt[i].shape[2]:
@@ -400,58 +459,72 @@
         if is_transformer(self.interval_features):
             self._interval_transformer = [True] * len(Xt)
             self._interval_features = [[self.interval_features]] * len(Xt)
         elif callable(self.interval_features):
             self._interval_function = [True] * len(Xt)
             self._interval_features = [[self.interval_features]] * len(Xt)
         elif isinstance(self.interval_features, (list, tuple)):
-            # if only one series_transformer is used, n_intervals can be a list of
-            # multiple n_intervals options to be applied todo
-            if len(Xt) == 1:
+            # if input is a list and only contains transformers or functions, use the
+            # list for all series in Xt
+            if all(
+                is_transformer(item) or callable(item)
+                for item in self.interval_features
+            ):
                 for i, feature in enumerate(self.interval_features):
                     if is_transformer(feature):
                         self._interval_transformer[0] = True
                     elif callable(feature):
                         self._interval_function[0] = True
-                    else:
-                        raise ValueError()  # todo error for invalid self.interval_features
-                self._interval_features = [self.interval_features]
-            # if more than one series_transformer is used, n_intervals must have the
-            # same number of items if it is a list todo
+                self._interval_features = [self.interval_features] * len(Xt)
+            # other lists must be the same length as Xt
             elif len(self.interval_features) != len(Xt):
-                raise ValueError()  # todo error for invalid self.interval_features
+                raise ValueError(
+                    "interval_features as a list or tuple containing other lists or "
+                    "tuples must be the same length as series_transformers."
+                )
             # list items can be a list of items or a single item for each
-            # series_transformer, but each individual item must be an int or str todo
+            # series_transformer, but each individual item must be a transformer
+            # or function
             else:
                 self._interval_features = []
                 for i, feature in enumerate(self.interval_features):
                     if isinstance(feature, (list, tuple)):
                         for method in feature:
                             if is_transformer(method):
                                 self._interval_transformer[i] = True
                             elif callable(method):
                                 self._interval_function[i] = True
                             else:
-                                raise ValueError()  # todo error for invalid self.interval_features
+                                raise ValueError(
+                                    "Individual items in a interval_features list or "
+                                    "tuple must be a transformer or function. Input "
+                                    f"{feature} does not contain only transformers and "
+                                    f"functions."
+                                )
                         self._interval_features.append(feature)
                     elif is_transformer(feature):
                         self._interval_transformer[i] = True
                         self._interval_features.append([feature])
                     elif callable(feature):
                         self._interval_function[i] = True
                         self._interval_features.append([feature])
                     else:
-                        raise ValueError()  # todo error for invalid self.interval_features
+                        raise ValueError(
+                            "Individual items in a interval_features list or tuple "
+                            f"must be a transformer or function. Found {feature}"
+                        )
         # use basic summary stats by default if None
         elif self.interval_features is None:
             self._interval_function = [True] * len(Xt)
             self._interval_features = [[row_mean, row_std, row_slope]] * len(Xt)
         # other inputs are invalid
         else:
-            raise ValueError()  # todo error for invalid self.interval_features
+            raise ValueError(
+                f"Invalid interval_features input. Found {self.interval_features}"
+            )
 
         # att_subsample_size must be at least one if it is an int
         if isinstance(self.att_subsample_size, int):
             if self.att_subsample_size < 1:
                 raise ValueError()  # todo error for invalid invalid self.att_subsample_size
 
             self._att_subsample_size = [self.att_subsample_size] * len(Xt)
@@ -536,42 +609,51 @@
         if isinstance(self.interval_selection_method, str):
             # SupervisedIntervals cannot currently handle transformers or regression
             if (
                 self.interval_selection_method.lower() == "supervised"
                 or self.interval_selection_method.lower() == "random-supervised"
             ):
                 if any(self._interval_transformer):
-                    raise ValueError()  # todo error for invalid invalid self.interval_selection_method
+                    raise ValueError(
+                        "Supervised interval_selection_method must only have function "
+                        "inputs for interval_features."
+                    )
 
                 if is_regressor(self):
-                    raise ValueError()  # todo error for invalid invalid self.interval_selection_method
+                    raise ValueError(
+                        "Supervised interval_selection_method cannot be used for "
+                        "regression."
+                    )
             # RandomIntervals
             elif not self.interval_selection_method.lower() == "random":
-                raise ValueError()  # todo error for invalid invalid self.interval_selection_method
+                raise ValueError(
+                    'Unknown interval_selection_method, must be one of ("random",'
+                    '"supervised","random-supervised"). '
+                    f"Found: {self.interval_selection_method}"
+                )
         # other inputs are invalid
         else:
-            raise ValueError()  # todo error for invalid self.interval_selection_method
+            raise ValueError(
+                'Unknown interval_selection_method, must be one of ("random",'
+                '"supervised","random-supervised"). '
+                f"Found: {self.interval_selection_method}"
+            )
 
-        # todo int option?
-        # option to replace NaN values must be a valid string
-        if isinstance(self.replace_nan, str):
-            if (
-                not self.replace_nan.lower() == "zero"
-                and not self.replace_nan.lower() == "nan"
-            ):
-                raise ValueError()  # todo error for invalid self.replace_nan
-        # other inputs are invalid except for None
-        elif self.replace_nan is not None:
+        # verify replace_nan is a valid string, number or None
+        if (
+            (not isinstance(self.replace_nan, str) or self.replace_nan.lower() != "nan")
+            and not isinstance(self.replace_nan, (int, float))
+            and self.replace_nan is not None
+        ):
             raise ValueError()  # todo error for invalid self.replace_nan
 
         self._n_jobs = check_n_jobs(self.n_jobs)
         self._efficient_predictions = True  # todo
         self._test_flag = False  # todo
 
-        self._n_estimators = self.n_estimators
         if self.time_limit_in_minutes is not None and self.time_limit_in_minutes > 0:
             time_limit = self.time_limit_in_minutes * 60
             start_time = time.time()
             train_time = 0
 
             self._n_estimators = 0
             self.estimators_ = []
@@ -604,14 +686,16 @@
                 self.estimators_ += estimators
                 self.intervals_ += intervals
                 self.transformed_data_ += transformed_data
 
                 self._n_estimators += self._n_jobs
                 train_time = time.time() - start_time
         else:
+            self._n_estimators = self.n_estimators
+
             fit = Parallel(
                 n_jobs=self._n_jobs,
                 backend=self.parallel_backend,
                 prefer="threads",
             )(
                 delayed(self._fit_estimator)(
                     Xt,
@@ -627,14 +711,16 @@
                 self.transformed_data_,
             ) = zip(*fit)
 
         return self
 
     def predict(self, X):
         if is_regressor(self):
+            check_is_fitted(self)
+
             Xt = self._predict_setup(X)
 
             y_preds = Parallel(
                 n_jobs=self._n_jobs,
                 backend=self.parallel_backend,
                 prefer="threads",
             )(
@@ -645,19 +731,33 @@
                     predict_proba=False,
                 )
                 for i in range(self._n_estimators)
             )
 
             return np.mean(y_preds, axis=0)
         else:
+            check_is_fitted(self)
+
+            # treat case of single class seen in fit
+            if self.n_classes_ == 1:
+                return np.repeat(
+                    list(self.class_dictionary_.keys()), X.shape[0], axis=0
+                )
+
             return np.array(
                 [self.classes_[int(np.argmax(prob))] for prob in self._predict_proba(X)]
             )
 
     def _predict_proba(self, X):
+        check_is_fitted(self)
+
+        # treat case of single class seen in fit
+        if self.n_classes_ == 1:
+            return np.repeat([[1]], X.shape[0], axis=0)
+
         Xt = self._predict_setup(X)
 
         y_probas = Parallel(
             n_jobs=self._n_jobs, backend=self.parallel_backend, prefer="threads"
         )(
             delayed(self._predict_for_estimator)(
                 Xt,
@@ -814,21 +914,26 @@
             intervals.append(selector)
             f = intervals[r].fit_transform(Xt[r], y)
 
             # concatenate the data and save this transforms number of attributes
             transform_data_lengths.append(f.shape[1])
             interval_features = np.hstack((interval_features, f))
 
-        # replace invalid attributes with 0 or np.nan if option is selected
-        if self.replace_nan == "zero":
-            interval_features = np.nan_to_num(interval_features, False, 0, 0, 0)
-        elif self.replace_nan == "nan":
+        if isinstance(self.replace_nan, str) and self.replace_nan.lower() == "nan":
             interval_features = np.nan_to_num(
                 interval_features, False, np.nan, np.nan, np.nan
             )
+        elif isinstance(self.replace_nan, (int, float)):
+            interval_features = np.nan_to_num(
+                interval_features,
+                False,
+                self.replace_nan,
+                self.replace_nan,
+                self.replace_nan,
+            )
 
         # clone and fit the base estimator using the transformed data
         tree = _clone_estimator(self._base_estimator, random_state=rs)
         tree.fit(interval_features, y)
 
         # find the features used in the tree and inform the interval selectors to not
         # transform these features if possible
@@ -872,16 +977,14 @@
         return [
             tree,
             intervals,
             interval_features if self.save_transformed_data else None,
         ]
 
     def _predict_setup(self, X):
-        check_is_fitted(self)
-
         X = self._validate_data(X=X, reset=False)
         X = self._convert_X(X)
 
         n_instances, n_dims, series_length = X.shape
 
         if n_dims != self.n_dims_:
             raise ValueError(
@@ -906,18 +1009,25 @@
     def _predict_for_estimator(self, Xt, estimator, intervals, predict_proba=False):
         interval_features = np.empty((Xt[0].shape[0], 0))
 
         for r in range(len(Xt)):
             f = intervals[r].transform(Xt[r])
             interval_features = np.hstack((interval_features, f))
 
-        if self.replace_nan == "zero":
-            interval_features = np.nan_to_num(interval_features, False, 0, 0, 0)
-        elif self.replace_nan == "nan":
+        if isinstance(self.replace_nan, str) and self.replace_nan.lower() == "nan":
             interval_features = np.nan_to_num(
                 interval_features, False, np.nan, np.nan, np.nan
             )
+        elif isinstance(self.replace_nan, (int, float)):
+            interval_features = np.nan_to_num(
+                interval_features,
+                False,
+                self.replace_nan,
+                self.replace_nan,
+                self.replace_nan,
+            )
 
         if predict_proba:
             return estimator.predict_proba(interval_features)
         else:
             return estimator.predict(interval_features)
+
```

### Comparing `tsml-0.0.4/tsml/interval_based/_cif.py` & `tsml-0.0.5/tsml/interval_based/_cif.py`

 * *Files 26% similar despite different names*

```diff
@@ -4,16 +4,27 @@
 __all__ = ["CIFClassifier", "CIFRegressor", "DrCIFClassifier", "DrCIFRegressor"]
 
 import numpy as np
 from sklearn.base import ClassifierMixin, RegressorMixin
 from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
 
 from tsml.interval_based._base import BaseIntervalForest
-from tsml.transformations._catch22 import Catch22Transformer
-from tsml.utils.numba_functions.stats import row_mean, row_slope, row_std
+from tsml.transformations import FunctionTransformer, PeriodogramTransformer
+from tsml.transformations._catch22 import Catch22Transformer, Catch22WrapperTransformer
+from tsml.utils.numba_functions.general import first_order_differences_3d
+from tsml.utils.numba_functions.stats import (
+    row_iqr,
+    row_mean,
+    row_median,
+    row_numba_max,
+    row_numba_min,
+    row_slope,
+    row_std,
+)
+from tsml.utils.validation import _check_optional_dependency
 from tsml.vector import CITClassifier
 
 
 class CIFClassifier(ClassifierMixin, BaseIntervalForest):
     """TODO."""
 
     def __init__(
@@ -22,26 +33,33 @@
         n_estimators=200,
         n_intervals="sqrt",
         min_interval_length=3,
         max_interval_length=np.inf,
         att_subsample_size=8,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pycatch22=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
+        self.use_pycatch22 = use_pycatch22
+        if use_pycatch22:
+            _check_optional_dependency("pycatch22", "pycatch22", self)
+
         if isinstance(base_estimator, CITClassifier):
             replace_nan = "nan"
         else:
-            replace_nan = "zero"
+            replace_nan = 0
 
         interval_features = [
-            Catch22Transformer(outlier_norm=True),
+            Catch22WrapperTransformer(outlier_norm=True)
+            if use_pycatch22
+            else Catch22Transformer(outlier_norm=True),
             row_mean,
             row_std,
             row_slope,
         ]
 
         super(CIFClassifier, self).__init__(
             base_estimator=base_estimator,
@@ -89,35 +107,47 @@
         """
         return {
             "n_estimators": 2,
             "n_intervals": 2,
             "att_subsample_size": 2,
         }
 
+    def _more_tags(self):
+        return {
+            "optional_dependency": True,
+        }
+
 
 class CIFRegressor(RegressorMixin, BaseIntervalForest):
     """TODO."""
 
     def __init__(
         self,
         base_estimator=None,
         n_estimators=200,
         n_intervals="sqrt",
         min_interval_length=3,
         max_interval_length=np.inf,
         att_subsample_size=8,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pycatch22=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
+        self.use_pycatch22 = use_pycatch22
+        if use_pycatch22:
+            _check_optional_dependency("pycatch22", "pycatch22", self)
+
         interval_features = [
-            Catch22Transformer(outlier_norm=True),
+            Catch22WrapperTransformer(outlier_norm=True)
+            if use_pycatch22
+            else Catch22Transformer(outlier_norm=True),
             row_mean,
             row_std,
             row_slope,
         ]
 
         super(CIFRegressor, self).__init__(
             base_estimator=base_estimator,
@@ -125,15 +155,15 @@
             interval_selection_method="random",
             n_intervals=n_intervals,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
             interval_features=interval_features,
             series_transformers=None,
             att_subsample_size=att_subsample_size,
-            replace_nan="zero",
+            replace_nan=0,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
             n_jobs=n_jobs,
             parallel_backend=parallel_backend,
         )
@@ -162,63 +192,94 @@
         """
         return {
             "n_estimators": 2,
             "n_intervals": 2,
             "att_subsample_size": 2,
         }
 
+    def _more_tags(self):
+        return {
+            "optional_dependency": True,
+        }
+
 
 class DrCIFClassifier(ClassifierMixin, BaseIntervalForest):
     """TODO."""
 
     def __init__(
         self,
         base_estimator=None,
         n_estimators=200,
-        n_intervals=None,
+        n_intervals=(4, "sqrt-div"),
         min_interval_length=3,
         max_interval_length=0.5,
         att_subsample_size=10,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pycatch22=True,
+        use_pyfftw=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
-        # CIT
-        # nans if CIT
+        self.use_pycatch22 = use_pycatch22
+        if use_pycatch22:
+            _check_optional_dependency("pycatch22", "pycatch22", self)
+
+        self.use_pyfftw = use_pyfftw
+        if use_pyfftw:
+            _check_optional_dependency("pyfftw", "pyfftw", self)
 
-        # if n_intervals is None:
-        #     n_intervals =
-        # ((4, "sqrt-div"), (4, "sqrt-div"), (4, "sqrt-div"))
+        if isinstance(base_estimator, CITClassifier):
+            replace_nan = "nan"
+        else:
+            replace_nan = 0
 
-        # interval_features = [Catch22(outlier_norm=True), None, None, None]
+        series_transformers = [
+            None,
+            FunctionTransformer(func=first_order_differences_3d, validate=False),
+            PeriodogramTransformer(use_pyfftw=use_pyfftw),
+        ]
 
-        # check_classification_targets(y)
+        interval_features = [
+            Catch22WrapperTransformer(outlier_norm=True)
+            if use_pycatch22
+            else Catch22Transformer(outlier_norm=True),
+            row_mean,
+            row_std,
+            row_slope,
+            row_median,
+            row_iqr,
+            row_numba_min,
+            row_numba_max,
+        ]
 
         super(DrCIFClassifier, self).__init__(
             base_estimator=base_estimator,
             n_estimators=n_estimators,
             interval_selection_method="random",
             n_intervals=n_intervals,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
-            interval_features=0,
-            series_transformers=0,
+            interval_features=interval_features,
+            series_transformers=series_transformers,
             att_subsample_size=att_subsample_size,
-            replace_nan=0,
+            replace_nan=replace_nan,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
             n_jobs=n_jobs,
             parallel_backend=parallel_backend,
         )
 
+    def predict_proba(self, X):
+        return self._predict_proba(X)
+
     @classmethod
     def get_test_params(cls, parameter_set="default"):
         """Return testing parameter settings for the estimator.
 
         Parameters
         ----------
         parameter_set : str, default="default"
@@ -239,51 +300,76 @@
         """
         return {
             "n_estimators": 2,
             "n_intervals": 2,
             "att_subsample_size": 2,
         }
 
+    def _more_tags(self):
+        return {
+            "optional_dependency": True,
+        }
+
 
 class DrCIFRegressor(RegressorMixin, BaseIntervalForest):
     """TODO."""
 
     def __init__(
         self,
         base_estimator=None,
         n_estimators=200,
-        n_intervals=None,
+        n_intervals=(4, "sqrt-div"),
         min_interval_length=3,
         max_interval_length=0.5,
         att_subsample_size=10,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pycatch22=True,
+        use_pyfftw=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
-        # CIT
-        # nans if CIT
-
-        # if n_intervals is None:
-        #     n_intervals =
-        # ((4, "sqrt-div"), (4, "sqrt-div"), (4, "sqrt-div"))
+        self.use_pycatch22 = use_pycatch22
+        if use_pycatch22:
+            _check_optional_dependency("pycatch22", "pycatch22", self)
+
+        self.use_pyfftw = use_pyfftw
+        if use_pyfftw:
+            _check_optional_dependency("pyfftw", "pyfftw", self)
+
+        series_transformers = [
+            None,
+            FunctionTransformer(func=first_order_differences_3d, validate=False),
+            PeriodogramTransformer(use_pyfftw=True),
+        ]
 
-        # interval_features = [Catch22(outlier_norm=True), None, None, None]
+        interval_features = [
+            Catch22WrapperTransformer(outlier_norm=True)
+            if use_pycatch22
+            else Catch22Transformer(outlier_norm=True),
+            row_mean,
+            row_std,
+            row_slope,
+            row_median,
+            row_iqr,
+            row_numba_min,
+            row_numba_max,
+        ]
 
         super(DrCIFRegressor, self).__init__(
             base_estimator=base_estimator,
             n_estimators=n_estimators,
             interval_selection_method="random",
             n_intervals=n_intervals,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
-            interval_features=0,
-            series_transformers=0,
+            interval_features=interval_features,
+            series_transformers=series_transformers,
             att_subsample_size=att_subsample_size,
             replace_nan=0,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
             n_jobs=n_jobs,
@@ -313,7 +399,12 @@
             `create_test_instance` uses the first (or only) dictionary in `params`.
         """
         return {
             "n_estimators": 2,
             "n_intervals": 2,
             "att_subsample_size": 2,
         }
+
+    def _more_tags(self):
+        return {
+            "optional_dependency": True,
+        }
```

### Comparing `tsml-0.0.4/tsml/interval_based/_interval_forest.py` & `tsml-0.0.5/tsml/interval_based/_interval_forest.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/interval_based/_interval_pipelines.py` & `tsml-0.0.5/tsml/interval_based/_interval_pipelines.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/interval_based/_rise.py` & `tsml-0.0.5/tsml/interval_based/_rise.py`

 * *Files 7% similar despite different names*

```diff
@@ -4,51 +4,50 @@
 __all__ = ["RISEClassifier", "RISERegressor"]
 
 import numpy as np
 from sklearn.base import ClassifierMixin, RegressorMixin
 from sklearn.tree import DecisionTreeClassifier
 
 from tsml.interval_based._base import BaseIntervalForest
+from tsml.transformations import PeriodogramTransformer
 from tsml.vector import CITClassifier
 
 
 class RISEClassifier(ClassifierMixin, BaseIntervalForest):
     """TODO."""
 
     def __init__(
         self,
         base_estimator=None,
         n_estimators=200,
         min_interval_length=3,
         max_interval_length=np.inf,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pyfftw=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
-        if base_estimator is None:
-            base_estimator = DecisionTreeClassifier(criterion="entropy")
+        self.use_pyfftw = use_pyfftw
 
         if isinstance(base_estimator, CITClassifier):
             replace_nan = "nan"
         else:
-            replace_nan = "zero"
-
-        interval_features = []
+            replace_nan = 0
 
         super(RISEClassifier, self).__init__(
             base_estimator=base_estimator,
             n_estimators=n_estimators,
             interval_selection_method="random",
             n_intervals=1,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
-            interval_features=interval_features,
+            interval_features=PeriodogramTransformer(use_pyfftw=use_pyfftw),
             series_transformers=None,
             att_subsample_size=None,
             replace_nan=replace_nan,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
@@ -93,35 +92,33 @@
         self,
         base_estimator=None,
         n_estimators=200,
         min_interval_length=3,
         max_interval_length=np.inf,
         time_limit_in_minutes=None,
         contract_max_n_estimators=500,
+        use_pyfftw=True,
         save_transformed_data=False,
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
-        if base_estimator is None:
-            base_estimator = DecisionTreeClassifier(criterion="entropy")
-
-        interval_features = []
+        self.use_pyfftw = use_pyfftw
 
         super(RISERegressor, self).__init__(
             base_estimator=base_estimator,
             n_estimators=n_estimators,
             interval_selection_method="random",
             n_intervals=1,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
-            interval_features=interval_features,
+            interval_features=PeriodogramTransformer(use_pyfftw=use_pyfftw),
             series_transformers=None,
             att_subsample_size=None,
-            replace_nan="zero",
+            replace_nan=0,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
             n_jobs=n_jobs,
             parallel_backend=parallel_backend,
         )
```

### Comparing `tsml-0.0.4/tsml/interval_based/_tsf.py` & `tsml-0.0.5/tsml/interval_based/_tsf.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
         random_state=None,
         n_jobs=1,
         parallel_backend=None,
     ):
         if isinstance(base_estimator, CITClassifier):
             replace_nan = "nan"
         else:
-            replace_nan = "zero"
+            replace_nan = 0
 
         super(TSFClassifier, self).__init__(
             base_estimator=base_estimator,
             n_estimators=n_estimators,
             interval_selection_method="random",
             n_intervals=n_intervals,
             min_interval_length=min_interval_length,
@@ -105,15 +105,15 @@
             interval_selection_method="random",
             n_intervals=n_intervals,
             min_interval_length=min_interval_length,
             max_interval_length=max_interval_length,
             interval_features=None,
             series_transformers=None,
             att_subsample_size=None,
-            replace_nan="zero",
+            replace_nan=0,
             time_limit_in_minutes=time_limit_in_minutes,
             contract_max_n_estimators=contract_max_n_estimators,
             save_transformed_data=save_transformed_data,
             random_state=random_state,
             n_jobs=n_jobs,
             parallel_backend=parallel_backend,
         )
```

### Comparing `tsml-0.0.4/tsml/shapelet_based/_stc.py` & `tsml-0.0.5/tsml/shapelet_based/_stc.py`

 * *Files 1% similar despite different names*

```diff
@@ -168,15 +168,15 @@
         self.n_instances_, self.n_dims_, self.series_length_ = X.shape
         self.classes_ = np.unique(y)
         self.n_classes_ = self.classes_.shape[0]
         self.class_dictionary_ = {}
         for index, classVal in enumerate(self.classes_):
             self.class_dictionary_[classVal] = index
 
-        if len(self.classes_) == 1:
+        if self.n_classes_ == 1:
             return self
 
         self._n_jobs = check_n_jobs(self.n_jobs)
 
         self._transform_limit_in_minutes = 0
         if self.time_limit_in_minutes > 0:
             # contracting 2/3 transform (with 1/5 of that taken away for final
```

### Comparing `tsml-0.0.4/tsml/tests/_sklearn_checks.py` & `tsml-0.0.5/tsml/tests/_sklearn_checks.py`

 * *Files 0% similar despite different names*

```diff
@@ -1698,15 +1698,14 @@
     """
 
     Modified version of the scikit-learn 1.2.1 function with the name for time series.
     """
     X, y = test_utils.generate_3d_test_data()
 
     tags = _safe_tags(estimator_orig)
-    n_samples = 30
     X = _enforce_estimator_tags_X(estimator_orig, X)
     y = _enforce_estimator_tags_y(estimator_orig, y)
     estimator = clone(estimator_orig)
     set_random_state(estimator)
     # fit
     estimator.fit(X, y)
     y_pred = estimator.predict(X)
@@ -2324,7 +2323,10 @@
 
     tags_keys = set(estimator._get_tags().keys())
     default_tags_keys = set(_DEFAULT_TAGS.keys())
     assert tags_keys.intersection(default_tags_keys) == default_tags_keys, (
         f"{name}._get_tags() is missing entries for the following default tags"
         f": {default_tags_keys - tags_keys.intersection(default_tags_keys)}"
     )
+
+
+# todo add pandas tests again?
```

### Comparing `tsml-0.0.4/tsml/tests/estimator_checks.py` & `tsml-0.0.5/tsml/tests/estimator_checks.py`

 * *Files 4% similar despite different names*

```diff
@@ -20,23 +20,14 @@
 from tsml.utils.validation import is_clusterer, is_transformer
 
 
 def _yield_all_time_series_checks(estimator):
     name = estimator.__class__.__name__
     tags = _safe_tags(estimator)
 
-    if "3darray" not in tags["X_types"]:
-        warnings.warn(
-            "Can't test estimator {} which requires input  of type {}".format(
-                name, tags["X_types"]
-            ),
-            SkipTestWarning,
-        )
-        return
-
     if tags["_skip_test"]:
         warnings.warn(
             f"Explicit SKIP via _skip_test tag for estimator {name}.",
             SkipTestWarning,
         )
         return
```

### Comparing `tsml-0.0.4/tsml/tests/test_interface.py` & `tsml-0.0.5/tsml/tests/test_interface.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/transformations/_catch22.py` & `tsml-0.0.5/tsml/transformations/_catch22.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/transformations/_function_transformer.py` & `tsml-0.0.5/tsml/transformations/_function_transformer.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/transformations/_interval_extraction.py` & `tsml-0.0.5/tsml/transformations/_interval_extraction.py`

 * *Files 2% similar despite different names*

```diff
@@ -360,14 +360,17 @@
                     )
 
                     t = feature.fit_transform(
                         np.expand_dims(X[:, dim, interval_start:interval_end], axis=1),
                         y,
                     )
 
+                    if t.ndim == 3:
+                        t = t.reshape((t.shape[0], t.shape[2]))
+
                     Xt = np.hstack((Xt, t))
                 else:
                     feature.fit(
                         np.expand_dims(X[:, dim, interval_start:interval_end], axis=1),
                         y,
                     )
             elif transform:
@@ -391,14 +394,16 @@
                 return [[0] for _ in range(X.shape[0])]
 
         if is_transformer(feature):
             Xt = feature.transform(
                 np.expand_dims(X[:, dim, interval_start:interval_end], axis=1)
             )
 
+            if Xt.ndim == 3:
+                Xt = Xt.reshape((Xt.shape[0], Xt.shape[2]))
         else:
             Xt = [[f] for f in feature(X[:, dim, interval_start:interval_end])]
 
         return Xt
 
     def set_features_to_transform(self, arr, raise_error=True):
         """Set transform_features to the given array.
@@ -715,15 +720,15 @@
         for i, t in enumerate(transform):
             Xt[:, i] = t
 
         return Xt
 
     def _fit_setup(self, X, y):
         X, y = self._validate_data(
-            X=X, y=y, ensure_min_samples=2, ensure_min_series_length=7
+            X=X, y=y, ensure_min_samples=2, ensure_min_series_length=5
         )
 
         self.intervals_ = []
 
         self.n_instances_, self.n_dims_, self.series_length_ = X.shape
 
         if self.n_instances_ <= 1:
```

### Comparing `tsml-0.0.4/tsml/transformations/_periodogram.py` & `tsml-0.0.5/tsml/transformations/_periodogram.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,54 +1,67 @@
 # -*- coding: utf-8 -*-
 __author__ = ["MatthewMiddlehurst"]
 __all__ = ["PeriodogramTransformer"]
 
+import math
+
 import numpy as np
 from sklearn.base import TransformerMixin
 
 from tsml.base import BaseTimeSeriesEstimator
-from tsml.utils.validation import _check_optional_dependency
+from tsml.utils.validation import _check_optional_dependency, check_n_jobs
 
 
 class PeriodogramTransformer(TransformerMixin, BaseTimeSeriesEstimator):
     def __init__(
         self,
         use_pyfftw=True,
+        pad_series=True,
+        n_jobs=1,
     ):
         self.use_pyfftw = use_pyfftw
+        self.pad_series = pad_series
+        self.n_jobs = n_jobs
+
+        if use_pyfftw:
+            _check_optional_dependency("pyfftw", "pyfftw", self)
 
         super(PeriodogramTransformer, self).__init__()
 
     def fit(self, X, y=None):
         self._validate_data(X=X)
         return self
 
     def transform(self, X, y=None):
         X = self._validate_data(X=X, reset=False)
         X = self._convert_X(X)
 
-        Xt = np.zeros((X.shape[0], X.shape[1], int(X.shape[2] / 2)))
-        if self.use_pyfftw:
-            _check_optional_dependency("pyfftw", "pyfftw", self)
-            import pyfftw
+        threads_to_use = check_n_jobs(self.n_jobs)
 
-            fft_object = pyfftw.builders.fft(X)
-            per_X = np.abs(fft_object)
-            per_X[:, : int(X.shape[2] / 2)]
-        else:
-            X_p = np.zeros(
+        if self.pad_series:
+            zeroes = np.zeros(
                 (
-                    self.n_instances_,
-                    self.n_dims_,
-                    int(
-                        math.pow(2, math.ceil(math.log(self.series_length_, 2)))
-                        - self.series_length_
-                    ),
+                    X.shape[0],
+                    X.shape[1],
+                    int(math.pow(2, math.ceil(math.log(X.shape[2], 2))) - X.shape[2]),
                 )
             )
-            X_p = np.concatenate((X, X_p), axis=2)
-            X_p = np.abs(np.fft.fft(X_p)[:, :, : int(X_p.shape[2] / 2)])
+            X = np.concatenate((X, zeroes), axis=2)
+
+        if self.use_pyfftw:
+            import pyfftw
+
+            old_threads = pyfftw.config.NUM_THREADS
+            pyfftw.config.NUM_THREADS = threads_to_use
+
+            fft_object = pyfftw.builders.fft(X[:, :, :])
+            Xt = np.abs(fft_object())
+            Xt = Xt[:, :, : int(X.shape[2] / 2)]
+
+            pyfftw.config.NUM_THREADS = old_threads
+        else:
+            Xt = np.abs(np.fft.fft(X)[:, :, : int(X.shape[2] / 2)])
 
         return Xt
 
     def _more_tags(self):
-        return {"stateless": True}
+        return {"stateless": True, "optional_dependency": True}
```

### Comparing `tsml-0.0.4/tsml/transformations/_sfa.py` & `tsml-0.0.5/tsml/transformations/_sfa.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/transformations/_shapelet_transform.py` & `tsml-0.0.5/tsml/transformations/_shapelet_transform.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/transformations/_summary_features.py` & `tsml-0.0.5/tsml/transformations/_summary_features.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/utils/_tags.py` & `tsml-0.0.5/tsml/utils/_tags.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/utils/discovery.py` & `tsml-0.0.5/tsml/utils/discovery.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/utils/numba_functions/general.py` & `tsml-0.0.5/tsml/utils/numba_functions/general.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # -*- coding: utf-8 -*-
 """General numba utilities."""
 
 __author__ = ["MatthewMiddlehurst"]
 __all__ = [
     "unique_count",
     "first_order_differences",
-    "row_first_order_differences",
+    "first_order_differences_2d",
     "z_normalise_series",
     "z_normalise_series_2d",
     "z_normalise_series_3d",
 ]
 
 from typing import Tuple
 
@@ -84,38 +84,62 @@
     >>> X = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
     >>> diff = first_order_differences(X)
     """
     return X[1:] - X[:-1]
 
 
 @njit(fastmath=True, cache=True)
-def row_first_order_differences(X: np.ndarray) -> np.ndarray:
+def first_order_differences_2d(X: np.ndarray) -> np.ndarray:
     """Numba first order differences function for a 2d numpy array.
 
     Parameters
     ----------
     X : 2d numpy array
         A 2d numpy array of values
 
     Returns
     -------
     arr : 2d numpy array of shape (X.shape[0], X.shape[1] - 1)
-        The first order differences for axis 0 of the input array
+        The first order differences for axis 1 of the input array
 
     Examples
     --------
     >>> import numpy as np
-    >>> from tsml.utils.numba_functions.general import row_first_order_differences
+    >>> from tsml.utils.numba_functions.general import first_order_differences_2d
     >>> X = np.array([[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [5, 6, 6, 7, 7, 7, 8, 8, 8, 8]])
-    >>> diff = row_first_order_differences(X)
+    >>> diff = first_order_differences_2d(X)
     """
     return X[:, 1:] - X[:, :-1]
 
 
 @njit(fastmath=True, cache=True)
+def first_order_differences_3d(X: np.ndarray) -> np.ndarray:
+    """Numba first order differences function for a 3d numpy array.
+
+    Parameters
+    ----------
+    X : 3d numpy array
+        A 3d numpy array of values
+
+    Returns
+    -------
+    arr : 2d numpy array of shape (X.shape[0], X.shape[1], X.shape[2] - 1)
+        The first order differences for axis 2 of the input array
+
+    Examples
+    --------
+    >>> import numpy as np
+    >>> from tsml.utils.numba_functions.general import first_order_differences_3d
+    >>> X = np.array([[[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [5, 6, 6, 7, 7, 7, 8, 8, 8, 8]]])
+    >>> diff = first_order_differences_3d(X)
+    """
+    return X[:, :, 1:] - X[:, :, :-1]
+
+
+@njit(fastmath=True, cache=True)
 def z_normalise_series(X: np.ndarray) -> np.ndarray:
     """Numba series normalization function for a 1d numpy array.
 
     Parameters
     ----------
     X : 1d numpy array
         A 1d numpy array of values
```

### Comparing `tsml-0.0.4/tsml/utils/numba_functions/stats.py` & `tsml-0.0.5/tsml/utils/numba_functions/stats.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/utils/testing.py` & `tsml-0.0.5/tsml/utils/testing.py`

 * *Files 0% similar despite different names*

```diff
@@ -107,15 +107,15 @@
         "estimator, check", checks_generator(), ids=_get_check_estimator_ids
     )
 
 
 def generate_3d_test_data(
     n_samples: int = 10,
     n_channels: int = 1,
-    series_length: int = 8,
+    series_length: int = 12,
     n_labels: int = 2,
     random_state: Union[int, None] = None,
 ) -> Tuple[np.ndarray, np.ndarray]:
     """Randomly generate 3D data for testing.
 
     Will ensure there is at least one sample per label.
```

### Comparing `tsml-0.0.4/tsml/utils/validation.py` & `tsml-0.0.5/tsml/utils/validation.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/vector/_cit.py` & `tsml-0.0.5/tsml/vector/_cit.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/vector/_rotation_forest.py` & `tsml-0.0.5/tsml/vector/_rotation_forest.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml/vector/tests/test_rotation_forest.py` & `tsml-0.0.5/tsml/vector/tests/test_rotation_forest.py`

 * *Files identical despite different names*

### Comparing `tsml-0.0.4/tsml.egg-info/PKG-INFO` & `tsml-0.0.5/tsml.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tsml
-Version: 0.0.4
+Version: 0.0.5
 Summary: A toolkit for time series machine learning algorithms.
 Author-email: Matthew Middlehurst <m.middlehurst@uea.ac.uk>, Tony Bagnall <ajb@uea.ac.uk>
 License: BSD 3-Clause License
         
         Copyright (c) The Time Series Machine Learning (tsml) developers.
         All rights reserved.
```

### Comparing `tsml-0.0.4/tsml.egg-info/SOURCES.txt` & `tsml-0.0.5/tsml.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 tsml/deep_learning/__init__.py
 tsml/deep_learning/base.py
 tsml/dictionary_based/__init__.py
 tsml/distance_based/__init__.py
 tsml/dummy/__init__.py
 tsml/dummy/_dummy.py
 tsml/feature_based/__init__.py
-tsml/feature_based/_catch22_classifier.py
+tsml/feature_based/_catch22.py
 tsml/interval_based/__init__.py
 tsml/interval_based/_base.py
 tsml/interval_based/_cif.py
 tsml/interval_based/_interval_forest.py
 tsml/interval_based/_interval_pipelines.py
 tsml/interval_based/_rise.py
 tsml/interval_based/_stsf.py
@@ -44,14 +44,15 @@
 tsml/shapelet_based/_stc.py
 tsml/tests/__init__.py
 tsml/tests/_sklearn_checks.py
 tsml/tests/estimator_checks.py
 tsml/tests/test_all_estimators.py
 tsml/tests/test_interface.py
 tsml/transformations/__init__.py
+tsml/transformations/_ar_coefficient.py
 tsml/transformations/_catch22.py
 tsml/transformations/_function_transformer.py
 tsml/transformations/_interval_extraction.py
 tsml/transformations/_periodogram.py
 tsml/transformations/_sfa.py
 tsml/transformations/_shapelet_transform.py
 tsml/transformations/_summary_features.py
```

