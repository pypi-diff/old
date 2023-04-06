# Comparing `tmp/mim_ocr-0.0.8.tar.gz` & `tmp/mim_ocr-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/jsiuta/MIM-OCR/dist/.tmp-7va4hb72/mim_ocr-0.0.8.tar", last modified: Mon Feb 13 12:07:56 2023, max compression
+gzip compressed data, was "/home/bmroczek/mim_ocr/MIM-OCR/dist/.tmp-wc2mpdb9/mim_ocr-0.0.9.tar", last modified: Wed Apr  5 17:19:56 2023, max compression
```

## Comparing `mim_ocr-0.0.8.tar` & `mim_ocr-0.0.9.tar`

### file list

```diff
@@ -1,62 +1,64 @@
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.122077 mim_ocr-0.0.8/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1279 2023-02-10 14:26:26.000000 mim_ocr-0.0.8/LICENSE.txt
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3645 2023-02-13 12:07:56.122077 mim_ocr-0.0.8/PKG-INFO
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3057 2023-02-10 14:26:26.000000 mim_ocr-0.0.8/README.md
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.114077 mim_ocr-0.0.8/mim_ocr/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      804 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/__init__.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.114077 mim_ocr-0.0.8/mim_ocr/backends/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      176 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/backends/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     2830 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/backends/aws_textract.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      732 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/backends/backend.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3501 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/backends/google_vision.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1854 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/backends/tesseract.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/data_model/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       21 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/data_model/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)    14528 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/data_model/box.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     2054 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/data_model/box_functions.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/exceptions/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       55 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/exceptions/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1709 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/exceptions/smooth_job_context.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/heuristics/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      344 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1376 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/basic_features.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1377 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/extract_simple_results.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     2530 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/feature.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     8264 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/fuzzy_matching_keyword_feature.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3094 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/heuristic_analysis.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     8577 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/keyword_feature.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     2020 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/pol_roberta_ner_on_device.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1051 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/heuristics/regex_feature.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/image/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       53 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/image/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1052 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/image/image.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      572 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/image/transformations.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/optional_elements/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/optional_elements/__init__.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/optional_elements/ner_feature/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3029 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/optional_elements/ner_feature/NER_feature.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      285 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/optional_elements/ner_feature/__init__.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/pipeline/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       47 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/pipeline/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     8045 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/pipeline/batch_processing.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     4759 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/pipeline/pipeline.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.118077 mim_ocr-0.0.8/mim_ocr/preprocessing/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       78 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/preprocessing/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     4597 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/preprocessing/deskew.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1320 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/preprocessing/reorient.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.122077 mim_ocr-0.0.8/mim_ocr/utils/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       30 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/utils/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      492 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/utils/class_utils.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     2539 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/utils/notebook_utils.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      215 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/utils/validators.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.122077 mim_ocr-0.0.8/mim_ocr/visualization/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)       72 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/visualization/__init__.py
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)    10565 2023-02-10 14:26:27.000000 mim_ocr-0.0.8/mim_ocr/visualization/visualize_result.py
-drwxrwxr-x   0 jsiuta    (1037) jsiuta    (1041)        0 2023-02-13 12:07:56.114077 mim_ocr-0.0.8/mim_ocr.egg-info/
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     3645 2023-02-13 12:07:56.000000 mim_ocr-0.0.8/mim_ocr.egg-info/PKG-INFO
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1507 2023-02-13 12:07:56.000000 mim_ocr-0.0.8/mim_ocr.egg-info/SOURCES.txt
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)        1 2023-02-13 12:07:56.000000 mim_ocr-0.0.8/mim_ocr.egg-info/dependency_links.txt
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      295 2023-02-13 12:07:56.000000 mim_ocr-0.0.8/mim_ocr.egg-info/requires.txt
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)        8 2023-02-13 12:07:56.000000 mim_ocr-0.0.8/mim_ocr.egg-info/top_level.txt
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)     1627 2023-02-13 11:43:21.000000 mim_ocr-0.0.8/pyproject.toml
--rw-rw-r--   0 jsiuta    (1037) jsiuta    (1041)      172 2023-02-13 12:07:56.122077 mim_ocr-0.0.8/setup.cfg
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.165928 mim_ocr-0.0.9/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1279 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/LICENSE.txt
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3645 2023-04-05 17:19:56.165928 mim_ocr-0.0.9/PKG-INFO
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3057 2023-04-05 17:08:10.000000 mim_ocr-0.0.9/README.md
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.153927 mim_ocr-0.0.9/mim_ocr/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      804 2022-12-28 18:58:01.000000 mim_ocr-0.0.9/mim_ocr/__init__.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.157927 mim_ocr-0.0.9/mim_ocr/backends/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      176 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/backends/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     2830 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/backends/aws_textract.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      732 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/backends/backend.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3501 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/backends/google_vision.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1854 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/backends/tesseract.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.157927 mim_ocr-0.0.9/mim_ocr/data_model/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       21 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/data_model/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)    14548 2023-04-05 17:08:17.000000 mim_ocr-0.0.9/mim_ocr/data_model/box.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     2054 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/data_model/box_functions.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.157927 mim_ocr-0.0.9/mim_ocr/exceptions/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       55 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/exceptions/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1709 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/exceptions/smooth_job_context.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/heuristics/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      344 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/heuristics/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1376 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/heuristics/basic_features.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1377 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/heuristics/extract_simple_results.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     2530 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/heuristics/feature.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     8264 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/heuristics/fuzzy_matching_keyword_feature.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3094 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/heuristics/heuristic_analysis.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     8577 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/heuristics/keyword_feature.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     2020 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/heuristics/pol_roberta_ner_on_device.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1051 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/heuristics/regex_feature.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/image/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       53 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/image/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1052 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/image/image.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      572 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/image/transformations.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/optional_elements/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)        0 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/optional_elements/__init__.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/optional_elements/easy_ocr/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      955 2023-04-05 17:08:17.000000 mim_ocr-0.0.9/mim_ocr/optional_elements/easy_ocr/__init__.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/optional_elements/ner_feature/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3029 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/optional_elements/ner_feature/NER_feature.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      285 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/optional_elements/ner_feature/__init__.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/pipeline/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       47 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/pipeline/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     8045 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/pipeline/batch_processing.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     4759 2023-02-07 13:03:54.000000 mim_ocr-0.0.9/mim_ocr/pipeline/pipeline.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/preprocessing/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       78 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/preprocessing/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     4597 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/preprocessing/deskew.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1320 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/preprocessing/reorient.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.161927 mim_ocr-0.0.9/mim_ocr/utils/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       30 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/utils/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      492 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/utils/class_utils.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     2539 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/utils/notebook_utils.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      215 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/utils/validators.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.165928 mim_ocr-0.0.9/mim_ocr/visualization/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)       72 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/visualization/__init__.py
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)    10565 2022-12-28 18:14:46.000000 mim_ocr-0.0.9/mim_ocr/visualization/visualize_result.py
+drwxrwxr-x   0 bmroczek  (1000) bmroczek  (1000)        0 2023-04-05 17:19:56.153927 mim_ocr-0.0.9/mim_ocr.egg-info/
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     3645 2023-04-05 17:19:56.000000 mim_ocr-0.0.9/mim_ocr.egg-info/PKG-INFO
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1554 2023-04-05 17:19:56.000000 mim_ocr-0.0.9/mim_ocr.egg-info/SOURCES.txt
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)        1 2023-04-05 17:19:56.000000 mim_ocr-0.0.9/mim_ocr.egg-info/dependency_links.txt
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      302 2023-04-05 17:19:56.000000 mim_ocr-0.0.9/mim_ocr.egg-info/requires.txt
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)        8 2023-04-05 17:19:56.000000 mim_ocr-0.0.9/mim_ocr.egg-info/top_level.txt
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)     1676 2023-04-05 17:19:10.000000 mim_ocr-0.0.9/pyproject.toml
+-rw-rw-r--   0 bmroczek  (1000) bmroczek  (1000)      172 2023-04-05 17:19:56.165928 mim_ocr-0.0.9/setup.cfg
```

### Comparing `mim_ocr-0.0.8/LICENSE.txt` & `mim_ocr-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/PKG-INFO` & `mim_ocr-0.0.9/mim_ocr.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: mim_ocr
-Version: 0.0.8
+Name: mim-ocr
+Version: 0.0.9
 Summary: Tool for using different OCR engines and process their results using common data structures.
 Author-email: Barbara Mroczek <barbara.mroczek@mim.ai>
 Project-URL: Homepage, https://github.com/mim-solutions/MIM-OCR
 Project-URL: Bug Tracker, https://github.com/mim-solutions/MIM-OCR/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
```

### Comparing `mim_ocr-0.0.8/README.md` & `mim_ocr-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/__init__.py` & `mim_ocr-0.0.9/mim_ocr/__init__.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/backends/aws_textract.py` & `mim_ocr-0.0.9/mim_ocr/backends/aws_textract.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/backends/backend.py` & `mim_ocr-0.0.9/mim_ocr/backends/backend.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/backends/google_vision.py` & `mim_ocr-0.0.9/mim_ocr/backends/google_vision.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/backends/tesseract.py` & `mim_ocr-0.0.9/mim_ocr/backends/tesseract.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/data_model/box.py` & `mim_ocr-0.0.9/mim_ocr/data_model/box.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,14 +16,15 @@
 class BoxType(Enum):
     ROOT_BOX = 0
     TESSERACT_DOCUMENT = 1
     TESSERACT_PAGE = 2
     TESSERACT_PARAGRAPH = 3
     TESSERACT_LINE = 4
     TESSERACT_WORD = 5
+    EASYOCR_BOX = 6
     GCP_DOCUMENT = 17
     # GCP_BLOCK_PICTURE = 18  # TODO:
     # GCP_BLOCK_RULER = 19  # TODO:
     GCP_BLOCK_TABLE = 20
     GCP_BLOCK_TEXT = 21
     # GCP_BLOCK_UNKNOWN = 22  # TODO:
     # GCP_BLOCK_BARCODE = 23  # TODO:
```

### Comparing `mim_ocr-0.0.8/mim_ocr/data_model/box_functions.py` & `mim_ocr-0.0.9/mim_ocr/data_model/box_functions.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/exceptions/smooth_job_context.py` & `mim_ocr-0.0.9/mim_ocr/exceptions/smooth_job_context.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/basic_features.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/basic_features.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/extract_simple_results.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/extract_simple_results.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/feature.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/feature.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/fuzzy_matching_keyword_feature.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/fuzzy_matching_keyword_feature.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/heuristic_analysis.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/heuristic_analysis.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/keyword_feature.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/keyword_feature.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/pol_roberta_ner_on_device.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/pol_roberta_ner_on_device.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/heuristics/regex_feature.py` & `mim_ocr-0.0.9/mim_ocr/heuristics/regex_feature.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/image/image.py` & `mim_ocr-0.0.9/mim_ocr/image/image.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/image/transformations.py` & `mim_ocr-0.0.9/mim_ocr/image/transformations.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/optional_elements/ner_feature/NER_feature.py` & `mim_ocr-0.0.9/mim_ocr/optional_elements/ner_feature/NER_feature.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/pipeline/batch_processing.py` & `mim_ocr-0.0.9/mim_ocr/pipeline/batch_processing.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/pipeline/pipeline.py` & `mim_ocr-0.0.9/mim_ocr/pipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/preprocessing/deskew.py` & `mim_ocr-0.0.9/mim_ocr/preprocessing/deskew.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/preprocessing/reorient.py` & `mim_ocr-0.0.9/mim_ocr/preprocessing/reorient.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/utils/notebook_utils.py` & `mim_ocr-0.0.9/mim_ocr/utils/notebook_utils.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr/visualization/visualize_result.py` & `mim_ocr-0.0.9/mim_ocr/visualization/visualize_result.py`

 * *Files identical despite different names*

### Comparing `mim_ocr-0.0.8/mim_ocr.egg-info/PKG-INFO` & `mim_ocr-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: mim-ocr
-Version: 0.0.8
+Name: mim_ocr
+Version: 0.0.9
 Summary: Tool for using different OCR engines and process their results using common data structures.
 Author-email: Barbara Mroczek <barbara.mroczek@mim.ai>
 Project-URL: Homepage, https://github.com/mim-solutions/MIM-OCR
 Project-URL: Bug Tracker, https://github.com/mim-solutions/MIM-OCR/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
```

### Comparing `mim_ocr-0.0.8/mim_ocr.egg-info/SOURCES.txt` & `mim_ocr-0.0.9/mim_ocr.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -27,14 +27,15 @@
 mim_ocr/heuristics/keyword_feature.py
 mim_ocr/heuristics/pol_roberta_ner_on_device.py
 mim_ocr/heuristics/regex_feature.py
 mim_ocr/image/__init__.py
 mim_ocr/image/image.py
 mim_ocr/image/transformations.py
 mim_ocr/optional_elements/__init__.py
+mim_ocr/optional_elements/easy_ocr/__init__.py
 mim_ocr/optional_elements/ner_feature/NER_feature.py
 mim_ocr/optional_elements/ner_feature/__init__.py
 mim_ocr/pipeline/__init__.py
 mim_ocr/pipeline/batch_processing.py
 mim_ocr/pipeline/pipeline.py
 mim_ocr/preprocessing/__init__.py
 mim_ocr/preprocessing/deskew.py
```

### Comparing `mim_ocr-0.0.8/pyproject.toml` & `mim_ocr-0.0.9/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "mim_ocr"
-version = "0.0.8"
+version = "0.0.9"
 authors = [
   { name="Barbara Mroczek", email="barbara.mroczek@mim.ai" },
 ]
 description = "Tool for using different OCR engines and process their results using common data structures."
 readme = "README.md"
 requires-python = ">=3.9, <3.11"
 classifiers = [
@@ -22,15 +22,15 @@
     "pdf2image",
     "Pillow==9.0.1",
 
     # from build/requirements.txt
     "boto3",
     "deskew~=0.10.40",
     "google-cloud-storage",
-    "google-cloud-vision",
+    "google-cloud-vision>=3.0.0",
     "hyperscan==0.3.3", # due to https://github.com/darvid/python-hyperscan/issues/50
     "jsonpickle",
     "loguru",
     "omegaconf",
     "openpyxl",
     "pptree",
     "pytesseract~=0.3.8",
@@ -44,14 +44,15 @@
     "mim_ocr",
     "mim_ocr.backends",
     "mim_ocr.data_model",
     "mim_ocr.exceptions",
     "mim_ocr.heuristics",
     "mim_ocr.image",
     "mim_ocr.optional_elements",
+    "mim_ocr.optional_elements.easy_ocr",
     "mim_ocr.optional_elements.ner_feature",
     "mim_ocr.pipeline",
     "mim_ocr.preprocessing",
     "mim_ocr.utils",
     "mim_ocr.visualization",
 ]
```

