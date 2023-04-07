# Comparing `tmp/seqio-nightly-0.0.8.dev20220906.tar.gz` & `tmp/seqio-nightly-0.0.8.dev20220907.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "seqio-nightly-0.0.8.dev20220906.tar", last modified: Tue Sep  6 07:16:42 2022, max compression
+gzip compressed data, was "seqio-nightly-0.0.8.dev20220907.tar", last modified: Wed Sep  7 07:16:31 2022, max compression
```

## Comparing `seqio-nightly-0.0.8.dev20220906.tar` & `seqio-nightly-0.0.8.dev20220907.tar`

### file list

```diff
@@ -1,80 +1,80 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       36 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)    45696 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    44953 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/
--rw-r--r--   0 runner    (1001) docker     (121)     1095 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14389 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/beam_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    10592 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/beam_utils_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    65780 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/dataset_providers.py
--rw-r--r--   0 runner    (1001) docker     (121)    57471 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/dataset_providers_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    29227 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/evaluation.py
--rw-r--r--   0 runner    (1001) docker     (121)    44383 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/evaluation_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    20157 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/experimental.py
--rw-r--r--   0 runner    (1001) docker     (121)    25091 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/experimental_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    51063 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/feature_converters.py
--rw-r--r--   0 runner    (1001) docker     (121)    37291 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/feature_converters_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    12486 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/helpers.py
--rw-r--r--   0 runner    (1001) docker     (121)    14528 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/helpers_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    17335 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/loggers.py
--rw-r--r--   0 runner    (1001) docker     (121)    22735 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/loggers_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     2285 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)    12633 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/preprocessors.py
--rw-r--r--   0 runner    (1001) docker     (121)    15486 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/preprocessors_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/scripts/
--rw-r--r--   0 runner    (1001) docker     (121)      583 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8962 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/scripts/cache_tasks_main.py
--rw-r--r--   0 runner    (1001) docker     (121)     6629 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/scripts/cache_tasks_test.py
--rw-r--r--   0 runner    (1001) docker     (121)     4134 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/scripts/inspect_tasks_main.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.011722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/bertwordpiece/
--rw-r--r--   0 runner    (1001) docker     (121)     1125 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/bertwordpiece/vocab.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_plaintext_task/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_plaintext_task/COMPLETED
--rw-r--r--   0 runner    (1001) docker     (121)      366 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_plaintext_task/info.train.json
--rwxr-xr-x   0 runner    (1001) docker     (121)      121 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_plaintext_task/stats.train.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/COMPLETED
--rw-r--r--   0 runner    (1001) docker     (121)      400 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/info.train.json
--rwxr-xr-x   0 runner    (1001) docker     (121)      690 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/info.validation.json
--rwxr-xr-x   0 runner    (1001) docker     (121)      166 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/stats.train.json
--rw-r--r--   0 runner    (1001) docker     (121)      167 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/stats.validation.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.015722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/COMPLETED
--rw-r--r--   0 runner    (1001) docker     (121)      822 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/info.train.json
--rwxr-xr-x   0 runner    (1001) docker     (121)     1112 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/info.validation.json
--rwxr-xr-x   0 runner    (1001) docker     (121)      206 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/stats.train.json
--rw-r--r--   0 runner    (1001) docker     (121)      207 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/stats.validation.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/COMPLETED
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/info.train.json
--rw-r--r--   0 runner    (1001) docker     (121)      704 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/info.validation.json
--rw-r--r--   0 runner    (1001) docker     (121)      178 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/stats.train.json
--rw-r--r--   0 runner    (1001) docker     (121)      178 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/stats.validation.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/COMPLETED
--rw-r--r--   0 runner    (1001) docker     (121)      203 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/info.train.json
--rw-r--r--   0 runner    (1001) docker     (121)      493 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/info.validation.json
--rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/stats.train.json
--rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_task/stats.validation.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/seqio/test_data/sentencepiece/
--rwxr-xr-x   0 runner    (1001) docker     (121)   238047 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/sentencepiece/sentencepiece.model
--rwxr-xr-x   0 runner    (1001) docker     (121)      290 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/sentencepiece/sentencepiece.vocab
--rwxr-xr-x   0 runner    (1001) docker     (121)       83 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_data/sentencepiece/tokens.tsv
--rw-r--r--   0 runner    (1001) docker     (121)    42834 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     3745 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/test_utils_test.py
--rw-r--r--   0 runner    (1001) docker     (121)    37657 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    26615 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/utils_test.py
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-09-06 07:16:32.000000 seqio-nightly-0.0.8.dev20220906/seqio/version.py
--rw-r--r--   0 runner    (1001) docker     (121)    31646 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/vocabularies.py
--rw-r--r--   0 runner    (1001) docker     (121)    22053 2022-09-06 07:16:30.000000 seqio-nightly-0.0.8.dev20220906/seqio/vocabularies_test.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    45696 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2458 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       89 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      215 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        6 2022-09-06 07:16:42.000000 seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-06 07:16:42.019722 seqio-nightly-0.0.8.dev20220906/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2420 2022-09-06 07:16:32.000000 seqio-nightly-0.0.8.dev20220906/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       36 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)    45696 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    44953 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.839458 seqio-nightly-0.0.8.dev20220907/seqio/
+-rw-r--r--   0 runner    (1001) docker     (121)     1095 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14389 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/beam_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10592 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/beam_utils_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65780 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/dataset_providers.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57471 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/dataset_providers_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    29227 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/evaluation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    44383 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/evaluation_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20157 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/experimental.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25091 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/experimental_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51063 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/feature_converters.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37291 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/feature_converters_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12486 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14528 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/helpers_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17335 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/loggers.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22735 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/loggers_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2285 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12633 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/preprocessors.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15486 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/preprocessors_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.839458 seqio-nightly-0.0.8.dev20220907/seqio/scripts/
+-rw-r--r--   0 runner    (1001) docker     (121)      583 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8962 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/scripts/cache_tasks_main.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6629 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/scripts/cache_tasks_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4134 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/scripts/inspect_tasks_main.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.835457 seqio-nightly-0.0.8.dev20220907/seqio/test_data/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.839458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/bertwordpiece/
+-rw-r--r--   0 runner    (1001) docker     (121)     1125 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/bertwordpiece/vocab.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.839458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_plaintext_task/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_plaintext_task/COMPLETED
+-rw-r--r--   0 runner    (1001) docker     (121)      366 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_plaintext_task/info.train.json
+-rwxr-xr-x   0 runner    (1001) docker     (121)      121 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_plaintext_task/stats.train.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.839458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/COMPLETED
+-rw-r--r--   0 runner    (1001) docker     (121)      400 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/info.train.json
+-rwxr-xr-x   0 runner    (1001) docker     (121)      690 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/info.validation.json
+-rwxr-xr-x   0 runner    (1001) docker     (121)      166 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/stats.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)      167 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/stats.validation.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/COMPLETED
+-rw-r--r--   0 runner    (1001) docker     (121)      822 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/info.train.json
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1112 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/info.validation.json
+-rwxr-xr-x   0 runner    (1001) docker     (121)      206 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/stats.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)      207 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/stats.validation.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/COMPLETED
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/info.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)      704 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/info.validation.json
+-rw-r--r--   0 runner    (1001) docker     (121)      178 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/stats.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)      178 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/stats.validation.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/COMPLETED
+-rw-r--r--   0 runner    (1001) docker     (121)      203 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/info.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)      493 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/info.validation.json
+-rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/stats.train.json
+-rw-r--r--   0 runner    (1001) docker     (121)       65 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_task/stats.validation.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/seqio/test_data/sentencepiece/
+-rwxr-xr-x   0 runner    (1001) docker     (121)   238047 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/sentencepiece/sentencepiece.model
+-rwxr-xr-x   0 runner    (1001) docker     (121)      290 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/sentencepiece/sentencepiece.vocab
+-rwxr-xr-x   0 runner    (1001) docker     (121)       83 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_data/sentencepiece/tokens.tsv
+-rw-r--r--   0 runner    (1001) docker     (121)    42834 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3745 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/test_utils_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)    37657 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26615 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/utils_test.py
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-09-07 07:16:22.000000 seqio-nightly-0.0.8.dev20220907/seqio/version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31646 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/vocabularies.py
+-rw-r--r--   0 runner    (1001) docker     (121)    22053 2022-09-07 07:16:21.000000 seqio-nightly-0.0.8.dev20220907/seqio/vocabularies_test.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    45696 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2458 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       89 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      215 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        6 2022-09-07 07:16:31.000000 seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-07 07:16:31.843458 seqio-nightly-0.0.8.dev20220907/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2420 2022-09-07 07:16:22.000000 seqio-nightly-0.0.8.dev20220907/setup.py
```

### Comparing `seqio-nightly-0.0.8.dev20220906/LICENSE` & `seqio-nightly-0.0.8.dev20220907/LICENSE`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/PKG-INFO` & `seqio-nightly-0.0.8.dev20220907/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: seqio-nightly
-Version: 0.0.8.dev20220906
+Version: 0.0.8.dev20220907
 Summary: SeqIO: Task-based datasets, preprocessing, and evaluation for sequence models.
 Home-page: https://github.com/google/seqio/tree/nightly
 Author: Google Inc.
 Author-email: no-reply@google.com
 License: Apache 2.0
 Keywords: sequence preprocessing nlp machinelearning
 Classifier: Development Status :: 4 - Beta
```

### Comparing `seqio-nightly-0.0.8.dev20220906/README.md` & `seqio-nightly-0.0.8.dev20220907/README.md`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/__init__.py` & `seqio-nightly-0.0.8.dev20220907/seqio/__init__.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/beam_utils.py` & `seqio-nightly-0.0.8.dev20220907/seqio/beam_utils.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/beam_utils_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/beam_utils_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/dataset_providers.py` & `seqio-nightly-0.0.8.dev20220907/seqio/dataset_providers.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/dataset_providers_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/dataset_providers_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/evaluation.py` & `seqio-nightly-0.0.8.dev20220907/seqio/evaluation.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/evaluation_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/evaluation_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/experimental.py` & `seqio-nightly-0.0.8.dev20220907/seqio/experimental.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/experimental_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/experimental_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/feature_converters.py` & `seqio-nightly-0.0.8.dev20220907/seqio/feature_converters.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/feature_converters_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/feature_converters_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/helpers.py` & `seqio-nightly-0.0.8.dev20220907/seqio/helpers.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/helpers_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/helpers_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/loggers.py` & `seqio-nightly-0.0.8.dev20220907/seqio/loggers.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/loggers_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/loggers_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/metrics.py` & `seqio-nightly-0.0.8.dev20220907/seqio/metrics.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/preprocessors.py` & `seqio-nightly-0.0.8.dev20220907/seqio/preprocessors.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/preprocessors_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/preprocessors_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/scripts/__init__.py` & `seqio-nightly-0.0.8.dev20220907/seqio/scripts/__init__.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/scripts/cache_tasks_main.py` & `seqio-nightly-0.0.8.dev20220907/seqio/scripts/cache_tasks_main.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/scripts/cache_tasks_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/scripts/cache_tasks_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/scripts/inspect_tasks_main.py` & `seqio-nightly-0.0.8.dev20220907/seqio/scripts/inspect_tasks_main.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/bertwordpiece/vocab.txt` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/bertwordpiece/vocab.txt`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task/info.validation.json` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task/info.validation.json`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/info.train.json` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/info.train.json`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_task_with_provenance/info.validation.json` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_task_with_provenance/info.validation.json`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/cached_untokenized_ndfeatures_task/info.validation.json` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/cached_untokenized_ndfeatures_task/info.validation.json`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_data/sentencepiece/sentencepiece.model` & `seqio-nightly-0.0.8.dev20220907/seqio/test_data/sentencepiece/sentencepiece.model`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_utils.py` & `seqio-nightly-0.0.8.dev20220907/seqio/test_utils.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/test_utils_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/test_utils_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/utils.py` & `seqio-nightly-0.0.8.dev20220907/seqio/utils.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/utils_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/utils_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/version.py` & `seqio-nightly-0.0.8.dev20220907/seqio/version.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,8 +13,8 @@
 # limitations under the License.
 
 r"""Separate file for storing the current version of SeqIO.
 
 Stored in a separate file so that setup.py can reference the version without
 pulling in all the dependencies in __init__.py.
 """
-__version__ = '0.0.8.dev20220906'
+__version__ = '0.0.8.dev20220907'
```

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/vocabularies.py` & `seqio-nightly-0.0.8.dev20220907/seqio/vocabularies.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio/vocabularies_test.py` & `seqio-nightly-0.0.8.dev20220907/seqio/vocabularies_test.py`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/PKG-INFO` & `seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: seqio-nightly
-Version: 0.0.8.dev20220906
+Version: 0.0.8.dev20220907
 Summary: SeqIO: Task-based datasets, preprocessing, and evaluation for sequence models.
 Home-page: https://github.com/google/seqio/tree/nightly
 Author: Google Inc.
 Author-email: no-reply@google.com
 License: Apache 2.0
 Keywords: sequence preprocessing nlp machinelearning
 Classifier: Development Status :: 4 - Beta
```

### Comparing `seqio-nightly-0.0.8.dev20220906/seqio_nightly.egg-info/SOURCES.txt` & `seqio-nightly-0.0.8.dev20220907/seqio_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `seqio-nightly-0.0.8.dev20220906/setup.py` & `seqio-nightly-0.0.8.dev20220907/setup.py`

 * *Files identical despite different names*

