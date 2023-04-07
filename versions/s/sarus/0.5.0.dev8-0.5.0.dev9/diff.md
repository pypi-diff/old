# Comparing `tmp/sarus-0.5.0.dev8.tar.gz` & `tmp/sarus-0.5.0.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sarus-0.5.0.dev8.tar", last modified: Wed Mar 29 13:18:54 2023, max compression
+gzip compressed data, was "sarus-0.5.0.dev9.tar", last modified: Wed Apr  5 07:24:32 2023, max compression
```

## Comparing `sarus-0.5.0.dev8.tar` & `sarus-0.5.0.dev9.tar`

### file list

```diff
@@ -1,99 +1,99 @@
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)       25 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/MANIFEST.in
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1563 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/PKG-INFO
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      663 2021-08-24 10:18:30.000000 sarus-0.5.0.dev8/README.rst
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      100 2021-09-06 19:14:48.000000 sarus-0.5.0.dev8/pyproject.toml
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      549 2023-03-29 13:18:23.000000 sarus-0.5.0.dev8/sarus/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    13051 2023-03-21 15:21:25.000000 sarus-0.5.0.dev8/sarus/config.yaml
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus/context/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/context/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     3069 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/context/local_sdk.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      302 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/context/typing.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    14561 2023-03-28 10:37:22.000000 sarus-0.5.0.dev8/sarus/dataspec_wrapper.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      743 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/debug.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus/imblearn/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      265 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/imblearn/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      578 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/imblearn/over_sampling.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      558 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/imblearn/pipeline.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      556 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/imblearn/under_sampling.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus/legacy/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)       42 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/legacy/__init__.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus/legacy/pandas/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      100 2023-01-27 14:38:46.000000 sarus-0.5.0.dev8/sarus/legacy/pandas/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    16606 2023-01-27 14:38:46.000000 sarus-0.5.0.dev8/sarus/legacy/pandas/dataframe.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.197521 sarus-0.5.0.dev8/sarus/legacy/tensorflow/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      132 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/legacy/tensorflow/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    13194 2022-12-01 13:21:20.000000 sarus-0.5.0.dev8/sarus/legacy/tensorflow/dataset.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    42361 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/legacy/tensorflow/model.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.201521 sarus-0.5.0.dev8/sarus/manager/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/manager/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2994 2023-03-15 13:51:36.000000 sarus-0.5.0.dev8/sarus/manager/arrow_computation.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2738 2023-03-15 13:51:36.000000 sarus-0.5.0.dev8/sarus/manager/cache_scalar_computation.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2486 2023-03-15 13:51:36.000000 sarus-0.5.0.dev8/sarus/manager/caching_computation.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     6003 2023-03-28 10:37:22.000000 sarus-0.5.0.dev8/sarus/manager/dataspec_api.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.201521 sarus-0.5.0.dev8/sarus/manager/ops/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/manager/ops/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      921 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/manager/ops/api.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    23474 2023-03-28 10:37:22.000000 sarus-0.5.0.dev8/sarus/manager/sdk_manager.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2990 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/manager/typing.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2792 2023-03-15 13:51:36.000000 sarus-0.5.0.dev8/sarus/manager/value_computation.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.201521 sarus-0.5.0.dev8/sarus/numpy/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      337 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/numpy/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)       81 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/numpy/random.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      963 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/numpy/scalars.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.205521 sarus-0.5.0.dev8/sarus/pandas/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      197 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/pandas/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      822 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/pandas/core.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     4918 2023-03-21 15:21:25.000000 sarus-0.5.0.dev8/sarus/pandas/dataframe.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      206 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/pandas/io.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.205521 sarus-0.5.0.dev8/sarus/pandas_profiling/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)       81 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/pandas_profiling/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      841 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/pandas_profiling/profile_report.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.205521 sarus-0.5.0.dev8/sarus/plotly/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      108 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/plotly/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      138 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/plotly/express.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    54945 2023-03-28 10:37:22.000000 sarus-0.5.0.dev8/sarus/sarus.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.205521 sarus-0.5.0.dev8/sarus/scripts/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/scripts/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     4618 2023-03-21 15:21:25.000000 sarus-0.5.0.dev8/sarus/scripts/generate_op_list.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.209521 sarus-0.5.0.dev8/sarus/sklearn/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      680 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/sklearn/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     6821 2022-11-25 16:40:07.000000 sarus-0.5.0.dev8/sarus/sklearn/cluster.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      766 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/sklearn/compose.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      833 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/sklearn/decomposition.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    11790 2022-11-25 16:40:07.000000 sarus-0.5.0.dev8/sarus/sklearn/ensemble.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      566 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/sklearn/impute.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      177 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/sklearn/inspection.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      668 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/sklearn/linear_model.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      174 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/sklearn/metrics.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1161 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/sklearn/model_selection.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      558 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/sklearn/pipeline.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1618 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/sklearn/preprocessing.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      613 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/sklearn/svm.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/sarus/skopt/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      223 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/skopt/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      929 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/skopt/searchcv.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/sarus/std/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      154 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/std/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1074 2022-11-29 13:03:29.000000 sarus-0.5.0.dev8/sarus/std/types.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/sarus/storage/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2023-01-27 14:38:46.000000 sarus-0.5.0.dev8/sarus/storage/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     4552 2023-01-27 14:38:46.000000 sarus-0.5.0.dev8/sarus/storage/legacy_local.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/sarus/tensorflow/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/tensorflow/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1676 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/typing.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)    10996 2023-03-21 15:21:25.000000 sarus-0.5.0.dev8/sarus/utils.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1461 2023-03-15 13:51:31.000000 sarus-0.5.0.dev8/sarus/wrapper_factory.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/sarus/xgboost/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      213 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/xgboost/__init__.py
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      774 2022-09-14 12:56:20.000000 sarus-0.5.0.dev8/sarus/xgboost/xgboost.py
-drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-03-29 13:18:54.193521 sarus-0.5.0.dev8/sarus.egg-info/
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     1563 2023-03-29 13:18:53.000000 sarus-0.5.0.dev8/sarus.egg-info/PKG-INFO
--rw-rw-r--   0 vincent   (1000) vincent   (1000)     2000 2023-03-29 13:18:54.000000 sarus-0.5.0.dev8/sarus.egg-info/SOURCES.txt
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        1 2023-03-29 13:18:53.000000 sarus-0.5.0.dev8/sarus.egg-info/dependency_links.txt
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        1 2021-08-30 08:41:07.000000 sarus-0.5.0.dev8/sarus.egg-info/not-zip-safe
--rw-rw-r--   0 vincent   (1000) vincent   (1000)      344 2023-03-29 13:18:53.000000 sarus-0.5.0.dev8/sarus.egg-info/requires.txt
--rw-rw-r--   0 vincent   (1000) vincent   (1000)        6 2023-03-29 13:18:53.000000 sarus-0.5.0.dev8/sarus.egg-info/top_level.txt
--rwxrwxr-x   0 vincent   (1000) vincent   (1000)     1301 2023-03-29 13:18:54.213521 sarus-0.5.0.dev8/setup.cfg
--rwxrwxr-x   0 vincent   (1000) vincent   (1000)      111 2023-03-29 13:18:14.000000 sarus-0.5.0.dev8/setup.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)       25 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/MANIFEST.in
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1563 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/PKG-INFO
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      663 2021-08-24 10:18:30.000000 sarus-0.5.0.dev9/README.rst
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      100 2021-09-06 19:14:48.000000 sarus-0.5.0.dev9/pyproject.toml
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.316826 sarus-0.5.0.dev9/sarus/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      549 2023-04-05 07:24:09.000000 sarus-0.5.0.dev9/sarus/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    13051 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/config.yaml
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus/context/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/context/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     3069 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/context/local_sdk.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      302 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/context/typing.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    14472 2023-04-04 17:16:43.000000 sarus-0.5.0.dev9/sarus/dataspec_wrapper.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      743 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/debug.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus/imblearn/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      265 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/imblearn/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      578 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/imblearn/over_sampling.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      558 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/imblearn/pipeline.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      556 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/imblearn/under_sampling.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus/legacy/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)       42 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/legacy/__init__.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus/legacy/pandas/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      100 2023-01-27 14:38:46.000000 sarus-0.5.0.dev9/sarus/legacy/pandas/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    16606 2023-01-27 14:38:46.000000 sarus-0.5.0.dev9/sarus/legacy/pandas/dataframe.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus/legacy/tensorflow/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      132 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/legacy/tensorflow/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    13194 2022-12-01 13:21:20.000000 sarus-0.5.0.dev9/sarus/legacy/tensorflow/dataset.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    42361 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/legacy/tensorflow/model.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/manager/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/manager/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2994 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/arrow_computation.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2738 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/cache_scalar_computation.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2486 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/caching_computation.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     6003 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/dataspec_api.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/manager/ops/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/manager/ops/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      921 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/ops/api.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    15974 2023-04-04 17:16:43.000000 sarus-0.5.0.dev9/sarus/manager/sdk_manager.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2564 2023-04-04 17:16:43.000000 sarus-0.5.0.dev9/sarus/manager/typing.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2792 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/manager/value_computation.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/numpy/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      337 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/numpy/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)       81 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/numpy/random.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      963 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/numpy/scalars.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/pandas/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      197 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/pandas/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      822 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/pandas/core.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     4918 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/pandas/dataframe.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      206 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/pandas/io.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/pandas_profiling/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)       81 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/pandas_profiling/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      841 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/pandas_profiling/profile_report.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/plotly/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      108 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/plotly/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      138 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/plotly/express.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    55278 2023-04-04 17:16:43.000000 sarus-0.5.0.dev9/sarus/sarus.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.324827 sarus-0.5.0.dev9/sarus/scripts/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/scripts/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     4618 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/scripts/generate_op_list.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/sklearn/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      680 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/sklearn/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     6821 2022-11-25 16:40:07.000000 sarus-0.5.0.dev9/sarus/sklearn/cluster.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      766 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/sklearn/compose.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      833 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/sklearn/decomposition.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    11790 2022-11-25 16:40:07.000000 sarus-0.5.0.dev9/sarus/sklearn/ensemble.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      566 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/sklearn/impute.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      177 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/sklearn/inspection.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      668 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/sklearn/linear_model.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      174 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/sklearn/metrics.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1161 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/sklearn/model_selection.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      558 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/sklearn/pipeline.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1618 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/sklearn/preprocessing.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      613 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/sklearn/svm.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/skopt/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      223 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/skopt/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      929 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/skopt/searchcv.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/std/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      154 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/std/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1074 2022-11-29 13:03:29.000000 sarus-0.5.0.dev9/sarus/std/types.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/storage/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2023-01-27 14:38:46.000000 sarus-0.5.0.dev9/sarus/storage/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     4552 2023-01-27 14:38:46.000000 sarus-0.5.0.dev9/sarus/storage/legacy_local.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/tensorflow/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        0 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/tensorflow/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1676 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/typing.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)    10996 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/utils.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1461 2023-04-04 14:59:28.000000 sarus-0.5.0.dev9/sarus/wrapper_factory.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.328827 sarus-0.5.0.dev9/sarus/xgboost/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      213 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/xgboost/__init__.py
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      774 2022-09-14 12:56:20.000000 sarus-0.5.0.dev9/sarus/xgboost/xgboost.py
+drwxrwxr-x   0 vincent   (1000) vincent   (1000)        0 2023-04-05 07:24:32.320826 sarus-0.5.0.dev9/sarus.egg-info/
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     1563 2023-04-05 07:24:32.000000 sarus-0.5.0.dev9/sarus.egg-info/PKG-INFO
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)     2000 2023-04-05 07:24:32.000000 sarus-0.5.0.dev9/sarus.egg-info/SOURCES.txt
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        1 2023-04-05 07:24:32.000000 sarus-0.5.0.dev9/sarus.egg-info/dependency_links.txt
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        1 2021-08-30 08:41:07.000000 sarus-0.5.0.dev9/sarus.egg-info/not-zip-safe
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)      345 2023-04-05 07:24:32.000000 sarus-0.5.0.dev9/sarus.egg-info/requires.txt
+-rw-rw-r--   0 vincent   (1000) vincent   (1000)        6 2023-04-05 07:24:32.000000 sarus-0.5.0.dev9/sarus.egg-info/top_level.txt
+-rwxrwxr-x   0 vincent   (1000) vincent   (1000)     1302 2023-04-05 07:24:32.332826 sarus-0.5.0.dev9/setup.cfg
+-rwxrwxr-x   0 vincent   (1000) vincent   (1000)      111 2023-04-05 07:23:51.000000 sarus-0.5.0.dev9/setup.py
```

### Comparing `sarus-0.5.0.dev8/PKG-INFO` & `sarus-0.5.0.dev9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sarus
-Version: 0.5.0.dev8
+Version: 0.5.0.dev9
 Summary: Python client for the Sarus Gateway
 Home-page: https://sarus.tech
 Author: Sarus Technologies
 Author-email: contact@sarus.tech
 License: Apache License 2.0
 Keywords: differential privacy,AI,Data privacy
 Platform: UNKNOWN
```

### Comparing `sarus-0.5.0.dev8/README.rst` & `sarus-0.5.0.dev9/README.rst`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/__init__.py` & `sarus-0.5.0.dev9/sarus/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,15 +13,15 @@
         std,
         xgboost,
     )
 
     from .sarus import Client, Dataset
     from .utils import eval, eval_policy, floating, integer, length
 
-VERSION = "0.5.0.dev8"
+VERSION = "0.5.0.dev9"
 
 __all__ = [
     "Dataset",
     "Client",
     "length",
     "eval",
     "eval_policy",
```

### Comparing `sarus-0.5.0.dev8/sarus/config.yaml` & `sarus-0.5.0.dev9/sarus/config.yaml`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/context/local_sdk.py` & `sarus-0.5.0.dev9/sarus/context/local_sdk.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/dataspec_wrapper.py` & `sarus-0.5.0.dev9/sarus/dataspec_wrapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -282,23 +282,19 @@
         """Return one of the wrapped DataSpec object."""
         if kind == DataSpecVariant.USER_DEFINED:
             return self._dataspec
         if kind == DataSpecVariant.ALTERNATIVE:
             if self._alt_dataspec:
                 return self._alt_dataspec
             else:
-                return self._dataspec.variant(
-                    kind=st.ConstraintKind.SYNTHETIC, public_context=[]
-                )
+                return self._dataspec.variant(kind=st.ConstraintKind.SYNTHETIC)
         elif kind == DataSpecVariant.SYNTHETIC:
-            return self._dataspec.variant(
-                kind=st.ConstraintKind.SYNTHETIC, public_context=[]
-            )
+            return self._dataspec.variant(kind=st.ConstraintKind.SYNTHETIC)
         elif kind == DataSpecVariant.MOCK:
-            return self._manager.mock(self._dataspec)
+            return self._dataspec.variant(kind=st.ConstraintKind.MOCK)
         else:
             raise ValueError(f"Unknown kind {kind}")
 
     def save(self, path: str) -> None:
         """Save the representation of the sarus object to a file.
 
         Args:
```

### Comparing `sarus-0.5.0.dev8/sarus/debug.py` & `sarus-0.5.0.dev9/sarus/debug.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/imblearn/over_sampling.py` & `sarus-0.5.0.dev9/sarus/imblearn/over_sampling.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/imblearn/pipeline.py` & `sarus-0.5.0.dev9/sarus/imblearn/pipeline.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/imblearn/under_sampling.py` & `sarus-0.5.0.dev9/sarus/imblearn/under_sampling.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/legacy/pandas/dataframe.py` & `sarus-0.5.0.dev9/sarus/legacy/pandas/dataframe.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/legacy/tensorflow/dataset.py` & `sarus-0.5.0.dev9/sarus/legacy/tensorflow/dataset.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/legacy/tensorflow/model.py` & `sarus-0.5.0.dev9/sarus/legacy/tensorflow/model.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/arrow_computation.py` & `sarus-0.5.0.dev9/sarus/manager/arrow_computation.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/cache_scalar_computation.py` & `sarus-0.5.0.dev9/sarus/manager/cache_scalar_computation.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/caching_computation.py` & `sarus-0.5.0.dev9/sarus/manager/caching_computation.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/dataspec_api.py` & `sarus-0.5.0.dev9/sarus/manager/dataspec_api.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/ops/api.py` & `sarus-0.5.0.dev9/sarus/manager/ops/api.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/manager/sdk_manager.py` & `sarus-0.5.0.dev9/sarus/manager/sdk_manager.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,29 +1,25 @@
 import json
 import os
 import tempfile
 import typing as t
 
-import pandas as pd
+import pyarrow as pa
 import requests
 import sarus_data_spec.protobuf as sp
 import sarus_data_spec.status as stt
 import sarus_data_spec.storage.typing as storage_typing
 import sarus_data_spec.typing as st
-from sarus_data_spec import transform as sarus_transform
 from sarus_data_spec.attribute import attach_properties
-from sarus_data_spec.config import WHITELISTED_TRANSFORMS
 from sarus_data_spec.constants import ARROW_TASK, SCALAR_TASK
-from sarus_data_spec.dataset import transformed
 from sarus_data_spec.manager.asyncio.delegating import DelegatingManager
 from sarus_data_spec.manager.base import Base
 from sarus_data_spec.dataspec_validator.privacy_limit import DeltaEpsilonLimit
 from sarus_data_spec.dataspec_validator.typing import DataspecPrivacyPolicy
 from sarus_data_spec.status import Status
-from sarus_data_spec.transform import transform_id
 
 import sarus.manager.dataspec_api as api
 import sarus.manager.ops.api as api_ops
 from sarus.typing import ADMIN_DS, MOCK, PYTHON_TYPE, Client
 
 from .arrow_computation import ToArrowComputationOnServer
 from .cache_scalar_computation import CacheScalarComputationFromServer
@@ -120,14 +116,26 @@
 
     def is_cached(self, dataspec: st.DataSpec) -> bool:
         """Return True if the dataspec is cached locally."""
         return True
 
     def is_delegated(self, dataspec: st.DataSpec) -> bool:
         """Return True if the dataspec is remotely computed."""
+        # `select_sql` transforms are delegated, whether mock or not
+        if dataspec.is_transformed():
+            transform = dataspec.transform()
+            if transform.protobuf().spec.HasField("select_sql"):
+                computation_graph = self.computation_graph(dataspec)
+                referrables = (
+                    list(computation_graph["dataspecs"])
+                    + list(computation_graph["transforms"])
+                    + list(computation_graph["attributes"])
+                )
+                api.push_dataspec_graph(self._client, referrables)
+
         ds, _ = api.get_dataspec(self.client(), dataspec.uuid())
         return ds is not None
 
     def push(self, dataspec: st.DataSpec) -> None:
         """Push a Dataspec's computation graph on the server."""
         computation_graph = self.computation_graph(dataspec)
         referrables = (
@@ -170,240 +178,38 @@
             task_names=[task_name],
         )
         if status_proto is None:
             return None
         else:
             return Status(protobuf=status_proto, store=True)
 
-    def mock(self, dataspec: st.DataSpec) -> st.DataSpec:
-        """Returns a MOCK version of a DataSpec.
-
-        This is a kind of compilation used by this manager to infer the
-        DataSpec's type and Python type of an external transform's result.
-        """
-        mock_attribute = dataspec.attribute(name=MOCK)
-        if mock_attribute is None:
-            if dataspec.is_transformed() and not self.is_remote(dataspec):
-                # The mock should have been registered
-                # when applying the transform
-                raise LookupError(
-                    "No Mock DataSpec found for a transformed DataSpec"
-                )
-            else:
-                return self.register_source_mock(dataspec)
-
-        mock_uuid = mock_attribute[MOCK]
-        mock = t.cast(st.DataSpec, self.storage().referrable(mock_uuid))
-        if mock is None:
-            raise LookupError(
-                f"Mock {mock_uuid} for dataspec {dataspec.uuid()} "
-                "not in Storage."
-            )
-        return mock
-
-    def register_source_mock(self, dataspec: st.DataSpec) -> st.DataSpec:
-        """Define what a mock is for source or fetched DataSpecs."""
-        assert not dataspec.is_transformed() or self.is_remote(dataspec)
-
-        if dataspec.prototype() == sp.Scalar:
-            scalar = t.cast(st.Scalar, dataspec)
-            assert scalar.is_model()
-            mock: st.DataSpec = scalar
-
-        elif dataspec.prototype() == sp.Dataset:
-            dataset = t.cast(st.Dataset, dataspec)
-            assert dataset.is_remote()
-
-            # We call transformed() directly specifying the dataspec_type to
-            # avoid going through infer_output_type again
-            syn_variant = dataset.variant(
-                kind=st.ConstraintKind.SYNTHETIC, public_context=[]
-            )
-
-            mock = transformed(
-                sarus_transform.extract(size=self._mock_size),
-                *[syn_variant],
-                dataspec_type=sp.type_name(sp.Dataset),
-            )
-        else:
-            raise TypeError(f"{dataspec.prototype()} not a DataSpec.")
-
-        self.attach_mock(dataspec, mock)
-        return mock
-
-    def attach_mock(self, dataspec: st.DataSpec, mock: st.DataSpec) -> None:
-        """The link between a DataSpec and its MOCK is in an attribute."""
-        attach_properties(dataspec, name=MOCK, properties={MOCK: mock.uuid()})
-
-    def attach_python_type(
-        self, dataspec: st.DataSpec, python_type: str
-    ) -> None:
-        """The Python type is stored in an attribute."""
-        attach_properties(
-            dataspec, name=PYTHON_TYPE, properties={PYTHON_TYPE: python_type}
-        )
-
-    def python_type(self, dataspec: st.DataSpec) -> t.Optional[str]:
+    def python_type(self, dataspec: st.DataSpec) -> str:
         """Return the Python class name of a DataSpec.
 
         This is used to instantiate the correct DataSpecWrapper class.
         """
         python_type_att = dataspec.attribute(name=PYTHON_TYPE)
-        if python_type_att is None:
-            return None
-        return python_type_att.properties().get(PYTHON_TYPE)
+        if python_type_att is not None:
+            return python_type_att.properties().get(PYTHON_TYPE)
 
-    def auto_mock(
-        self,
-        python_type: str,
-    ) -> t.Tuple[str, t.Callable[[st.DataSpec], None]]:
-        """Fitted model mocks are handled separately.
-
-        Normally, we would compute the mocks on the mock input data. However,
-        this caused a number of issues (some classes not present in the mocks,
-        fitted mock model having different output shapes,...).
-
-        For a limited number of ops, can set the python output type and set the
-        mock to be the dataspec itself. For this to work, we need the mock and
-        the real value to have the same structure (this works for fitted models
-        and scores). We also need the op to be whitelisted.
-        """
-        # This is because when we call `model.fit`, the model is the first
-        # unnamed arg
-        dataspec_type = sp.type_name(sp.Scalar)
-
-        # Create the callback
-        def attach_info(ds: st.DataSpec) -> None:
-            """Attach the mock to the DataSpec."""
-            self.attach_mock(ds, ds)  # set the mock to be itself
-            self.attach_python_type(ds, python_type)
-
-        # Return the output type
-        return dataspec_type, attach_info
-
-    def infer_output_type(
-        self,
-        transform: st.Transform,
-        *arguments: st.DataSpec,
-        **named_arguments: st.DataSpec,
-    ) -> t.Tuple[str, t.Callable[[st.DataSpec], None]]:
-        """Infer the transform output type: Dataset or Scalar.
-
-        For external transforms, the MOCK value is computed here and the
-        value's Python type is attached to the output DataSpec.
-        """
-        AUTO_MOCK = [
-            # "sklearn.SK_FIT",
-            "sklearn.SK_ROC_AUC_SCORE",
-        ]
-
-        if transform.is_external():
-            tr_id = transform_id(transform)
-            if tr_id in AUTO_MOCK:
-                assert all([op in WHITELISTED_TRANSFORMS for op in AUTO_MOCK])
-                if tr_id == "sklearn.SK_FIT":
-                    non_fitted_model = arguments[0]
-                    # same python class
-                    python_type = str(type(self.value(non_fitted_model)))
-                elif tr_id == "sklearn.SK_ROC_AUC_SCORE":
-                    python_type = str(float)
-                else:
-                    raise ValueError(f"Unknown AUTO_MOCK {python_type}")
-
-                return self.auto_mock(python_type)
-
-            # Get parent DataSpecs mock DataSpecs
-            mock_args = [self.mock(arg) for arg in arguments]
-            named_mock_args = {
-                name: self.mock(arg) for name, arg in named_arguments.items()
-            }
-            # Create a temporary mock that we set as a Scalar
-            temporary_mock = transformed(
-                transform,
-                *mock_args,
-                dataspec_type=sp.type_name(sp.Scalar),
-                dataspec_name="temporary_mock",
-                **named_mock_args,
-            )
-
-            try:
-                mock_value = self.value(temporary_mock)
-            except Exception as e:
-                raise e
-            finally:
-                self.storage().delete(temporary_mock.uuid())
-
-            # Infer output types
-            python_type = str(type(mock_value))
-            dataset_types = [pd.DataFrame]
-            dataspec_type = (
-                sp.type_name(sp.Dataset)
-                if type(mock_value) in dataset_types
-                else sp.type_name(sp.Scalar)
-            )
-
-            mock: st.DataSpec = transformed(
-                transform,
-                *mock_args,
-                dataspec_type=dataspec_type,
-                **named_mock_args,
-            )
-
-            # Create the callback
-            def attach_info(ds: st.DataSpec) -> None:
-                """Attach the mock to the DataSpec."""
-                self.attach_mock(ds, mock)
-                self.attach_python_type(ds, python_type)
-
-            # Return the output type
-            return dataspec_type, attach_info
-
-        elif transform.protobuf().spec.HasField("synthetic"):
-
-            def attach_info(ds: st.DataSpec) -> None:
-                mock = transformed(
-                    sarus_transform.extract(size=self._mock_size),
-                    *[ds],
-                    dataspec_type=sp.type_name(sp.Dataset),
-                )
-                self.attach_mock(ds, mock)
-
-            return sp.type_name(sp.Dataset), attach_info
+        if not dataspec.is_transformed():
+            return str(t.Iterator[pa.RecordBatch])
 
+        transform = dataspec.transform()
+        if not transform.is_external():
+            type_str = str(t.Iterator[pa.RecordBatch])
         else:
-            # We should attach a python type as Iterator[pa.RecordBatch]
-            # By default, results of non external transforms (e.g. join,
-            # sample) are Datasets and non external transforms are only applied
-            # to Datasets
-            # We also send to the the server the internal mock
-            mock_args = [self.mock(arg) for arg in arguments]
-            named_mock_args = {
-                name: self.mock(arg) for name, arg in named_arguments.items()
-            }
-
-            mock = transformed(
-                transform,
-                *mock_args,
-                dataspec_type=sp.type_name(sp.Dataset),
-                **named_mock_args,
-            )
-
-            def attach_info(ds: st.DataSpec) -> None:
-                self.attach_mock(ds, mock)
-                # self.attach_python_type(ds, Iterator[pa.RecordBatch])
+            ds_args, ds_kwargs = dataspec.parents()
+            mock_value = self.mock_value(transform, *ds_args, **ds_kwargs)
+            type_str = str(type(mock_value))
 
-            if transform.protobuf().spec.HasField("select_sql"):
-                computation_graph = self.computation_graph(mock)
-                referrables = (
-                    list(computation_graph["dataspecs"])
-                    + list(computation_graph["transforms"])
-                    + list(computation_graph["attributes"])
-                )
-                api.push_dataspec_graph(self._client, referrables)
-            return sp.type_name(sp.Dataset), attach_info
+        attach_properties(
+            dataspec, name=PYTHON_TYPE, properties={PYTHON_TYPE: type_str}
+        )
+        return type_str
 
     Edge = t.Tuple[st.DataSpec, st.DataSpec, st.Transform]
 
     def computation_graph(
         self, dataspec: st.DataSpec
     ) -> t.Dict[str, t.Union[st.DataSpec, st.Transform, st.Attribute, Edge]]:
         """Retreive all items necessary to compute a DataSpec.
@@ -483,15 +289,15 @@
         """Delete a DataSpec locally. MOCKs also have to be deleted."""
         would_delete = self.storage().all_referrings(uuid)
         additional_cleanup = []
         for uuid in would_delete:
             item = self.storage().referrable(uuid)
             if item.prototype() in [sp.Dataset, sp.Scalar]:
                 try:
-                    mock = self.mock(item)
+                    mock = item.variant(st.ConstraintKind.MOCK)
                 except Exception:
                     pass
                 else:
                     if mock:
                         additional_cleanup.append(mock)
 
         self.storage().delete(uuid)
```

### Comparing `sarus-0.5.0.dev8/sarus/manager/typing.py` & `sarus-0.5.0.dev9/sarus/manager/typing.py`

 * *Files 4% similar despite different names*

```diff
@@ -25,25 +25,14 @@
     method. This serves two purposes. First, it provides immediate feedback to
     the user in case of erroneous computation. Second, it allows identifying the
     MOCK's value Python type which is then used by the SDK to instantiate the
     correct DataSpecWrapper type (e.g. instantiate a sarus.pandas.DataFrame if
     the value is a pandas.DataFrame).
     """
 
-    def mock(self, dataspec: st.DataSpec) -> st.DataSpec:
-        """Returns a mock version of a DataSpec.
-
-        This is a kind of compilation used by this manager to infer the DataSpec type and Python type of an external transform's result.
-        """
-        ...
-
-    def register_source_mock(self, dataspec: st.DataSpec) -> st.DataSpec:
-        """Define what a mock is for source or fetched DataSpecs."""
-        ...
-
     def python_type(self, dataspec: st.DataSpec) -> t.Optional[str]:
         """Return the Python class name of a DataSpec.
 
         This is used to instantiate the correct DataSpecWrapper class.
         """
 
     def client(self) -> Client:
```

### Comparing `sarus-0.5.0.dev8/sarus/manager/value_computation.py` & `sarus-0.5.0.dev9/sarus/manager/value_computation.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/numpy/scalars.py` & `sarus-0.5.0.dev9/sarus/numpy/scalars.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/pandas/core.py` & `sarus-0.5.0.dev9/sarus/pandas/core.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/pandas/dataframe.py` & `sarus-0.5.0.dev9/sarus/pandas/dataframe.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/pandas_profiling/profile_report.py` & `sarus-0.5.0.dev9/sarus/pandas_profiling/profile_report.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sarus.py` & `sarus-0.5.0.dev9/sarus/sarus.py`

 * *Files 2% similar despite different names*

```diff
@@ -58,15 +58,14 @@
 from sarus.manager.dataspec_api import compile_dataspec, pull_dataspec_graph
 from sarus.manager.typing import SDKManager
 
 with warnings.catch_warnings():
     warnings.simplefilter("ignore")
     import sarus_data_spec.protobuf as sp
     import sarus_data_spec.typing as st
-    from sarus_data_spec.attribute import attach_properties
     from sarus_data_spec.constants import (
         ARROW_TASK,
         CACHE,
         CACHE_PATH,
         SCHEMA_TASK,
     )
     from sarus_data_spec.context import push_global_context
@@ -74,17 +73,23 @@
         deserialize,
         dict_deserialize,
         serialize,
     )
     from sarus_data_spec.dataspec_validator.privacy_limit import (
         DeltaEpsilonLimit,
     )
+    from sarus_data_spec.dataspec_rewriter.simple_rules import (
+        attach_variant,
+    )
     from sarus_data_spec.status import last_statuses, ready
-    from sarus_data_spec.transform import select_sql
-    from sarus_data_spec.variant_constraint import pep_constraint
+    from sarus_data_spec.transform import extract, select_sql
+    from sarus_data_spec.variant_constraint import (
+        mock_constraint,
+        pep_constraint,
+    )
 
     from sarus.context.local_sdk import LocalSDKContext
     from sarus.pandas.dataframe import DataFrame
 
     try:
         import tensorflow as tf
 
@@ -249,14 +254,21 @@
             client.context().storage().referrable(syn_dataset_uuid)
         )
 
         # Update statuses
         dataspec.status(task_names=[ARROW_TASK, SCHEMA_TASK])
         syn_dataset.status(task_names=[ARROW_TASK, SCHEMA_TASK])
 
+        # Create mock
+        mock_dataset: st.Dataset = extract(size=dataspec.manager()._mock_size)(
+            syn_dataset
+        )
+        mock_constraint(mock_dataset)
+        attach_variant(dataspec, mock_dataset, st.ConstraintKind.MOCK)
+
         # TODO fetch the PEP token from the API
         # (it is lazily computed on the server)
         h = hashlib.md5()
         h.update(dataspec.protobuf().SerializeToString())
         pep_token = h.hexdigest()
         pep_constraint(
             dataspec=dataspec,
@@ -1185,15 +1197,15 @@
         factory = self.context().factory()
         storage = self.context().storage()
         # Two passes to have all the correct referrings
         refs = [factory.create(deserialize(ref)) for ref in refs]
         _ = [storage.store(ref) for ref in refs]
 
         user_ds = self.context().storage().referrable(user_defined)
-        mock_ds = self.context().manager().mock(user_ds)
+        mock_ds = user_ds.variant(st.ConstraintKind.MOCK)
 
         # loading the cache of the mock (only for the dataspec we load)
         with tarfile.open(path, mode="r") as tar:
             tar_filenames = tar.getnames()
             for filename in tar_filenames:
                 if f"{mock_ds.uuid()}" in filename:
                     cache_dir = self.context().manager().parquet_dir()
@@ -1208,17 +1220,17 @@
         return self.context().wrapper_factory().create(user_ds)
 
     def _oidc_login(self):
         oidc_login_url = f"{self.base_url}/oidc_login?headless=true"
         try:
             from IPython.display import Javascript, clear_output
 
-            display(
+            display(  # noqa: F821
                 Javascript(f'window.open("{oidc_login_url}");')
-            )  # noqa: F821
+            )
             display(clear_output())  # noqa: F821
         except Exception:
             webbrowser.open(oidc_login_url)
         token = getpass.getpass(
             "Logging in via google.\nYou will be redirected to a login page "
             "where you will obtain a token to paste below.\nIf you are not "
             f"redirected automatically, you can visit {oidc_login_url}\n"
```

### Comparing `sarus-0.5.0.dev8/sarus/scripts/generate_op_list.py` & `sarus-0.5.0.dev9/sarus/scripts/generate_op_list.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/__init__.py` & `sarus-0.5.0.dev9/sarus/sklearn/__init__.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/cluster.py` & `sarus-0.5.0.dev9/sarus/sklearn/cluster.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/compose.py` & `sarus-0.5.0.dev9/sarus/sklearn/compose.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/decomposition.py` & `sarus-0.5.0.dev9/sarus/sklearn/decomposition.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/ensemble.py` & `sarus-0.5.0.dev9/sarus/sklearn/ensemble.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/impute.py` & `sarus-0.5.0.dev9/sarus/sklearn/impute.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/linear_model.py` & `sarus-0.5.0.dev9/sarus/sklearn/linear_model.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/model_selection.py` & `sarus-0.5.0.dev9/sarus/sklearn/model_selection.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/pipeline.py` & `sarus-0.5.0.dev9/sarus/sklearn/pipeline.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/preprocessing.py` & `sarus-0.5.0.dev9/sarus/sklearn/preprocessing.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/sklearn/svm.py` & `sarus-0.5.0.dev9/sarus/sklearn/svm.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/skopt/searchcv.py` & `sarus-0.5.0.dev9/sarus/skopt/searchcv.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/std/types.py` & `sarus-0.5.0.dev9/sarus/std/types.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/storage/legacy_local.py` & `sarus-0.5.0.dev9/sarus/storage/legacy_local.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/typing.py` & `sarus-0.5.0.dev9/sarus/typing.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/utils.py` & `sarus-0.5.0.dev9/sarus/utils.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/wrapper_factory.py` & `sarus-0.5.0.dev9/sarus/wrapper_factory.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus/xgboost/xgboost.py` & `sarus-0.5.0.dev9/sarus/xgboost/xgboost.py`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/sarus.egg-info/PKG-INFO` & `sarus-0.5.0.dev9/sarus.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sarus
-Version: 0.5.0.dev8
+Version: 0.5.0.dev9
 Summary: Python client for the Sarus Gateway
 Home-page: https://sarus.tech
 Author: Sarus Technologies
 Author-email: contact@sarus.tech
 License: Apache License 2.0
 Keywords: differential privacy,AI,Data privacy
 Platform: UNKNOWN
```

### Comparing `sarus-0.5.0.dev8/sarus.egg-info/SOURCES.txt` & `sarus-0.5.0.dev9/sarus.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sarus-0.5.0.dev8/setup.cfg` & `sarus-0.5.0.dev9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 
 [options]
 zip_safe = False
 python_requires = >=3.7, <3.11
 packages = find:
 include_package_data = True
 install_requires = 
-	sarus_data_spec_public==2.9.2
+	sarus_data_spec_public==2.11.1
 	matplotlib>=3.1
 	cloudpickle>=1.2, <2.1
 
 [options.extras_require]
 sklearn = 
 	scikit-learn==1.1.1
 	scipy==1.9.0
```

