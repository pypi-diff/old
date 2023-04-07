# Comparing `tmp/tflite-model-maker-nightly-0.4.3.dev202304050507.tar.gz` & `tmp/tflite-model-maker-nightly-0.4.3.dev202304060508.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tflite-model-maker-nightly-0.4.3.dev202304050507.tar", last modified: Wed Apr  5 05:07:27 2023, max compression
+gzip compressed data, was "dist/tflite-model-maker-nightly-0.4.3.dev202304060508.tar", last modified: Thu Apr  6 05:08:44 2023, max compression
```

## Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507.tar` & `tflite-model-maker-nightly-0.4.3.dev202304060508.tar`

### file list

```diff
@@ -1,421 +1,421 @@
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4494 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/PKG-INFO
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       38 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/setup.cfg
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4567 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/setup.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      722 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      730 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      673 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/cli/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/cli/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4255 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/cli/cli.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      731 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2418 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/api_gen.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9856 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/api_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1269 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/deprecated_api.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8038 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/golden_api.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4764 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/golden_api_doc.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2824 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/include.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2072 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/compat.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15006 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/audio_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1334 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/data_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7311 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4180 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/image_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6248 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/image_searcher_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2459 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/metadata_loader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15144 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14165 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1865 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_config.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    11908 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6126 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_testutil.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3750 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/searcher_dataloader.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      566 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/annotations.json
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1019 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/test_annotations.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      898 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/train_annotations.json
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      420 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v1.1.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1654 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v2.0.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      421 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v1.1.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1654 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v2.0.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14998 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/text_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4854 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/text_searcher_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1031 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/export_format.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1092 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/file_util.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/optimization/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/optimization/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2213 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/optimization/warmup.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5964 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/audio_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5384 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/classification_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7258 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/configs.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9301 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/custom_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3856 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/hub_loader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14127 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/image_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8529 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/image_preprocessing.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8129 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writer_for_image_classifier.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9295 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/metadata_writer_for_bert.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6448 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5309 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5928 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/metadata_writer.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6098 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4563 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    23901 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/audio_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5557 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/image_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    23482 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/object_detector_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1916 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/recommendation_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    43235 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/text_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1781 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12268 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12155 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/object_detector.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10179 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/question_answer.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10005 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/recommendation.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14665 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/searcher.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1960 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/average_word_vec_metadata.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2394 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_classifier_metadata.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2575 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_qa_metadata.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3127 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientdet_lite0_metadata.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1904 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientnet_lite0_metadata.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1282 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/mobilenet_v3_small_100_224_embedder_scann.json
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9596 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/text_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8241 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/train_image_classifier_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5663 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/test_util.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1856 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/ondevice_scann_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9289 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/scann_converter.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6869 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/audio_classification_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7862 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/custom_model_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2613 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/image_classification_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2829 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/question_answer_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5356 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/recommendation_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3078 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/text_classification_demo.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    66601 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/autoaugment.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4635 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/gridmask.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8379 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/mosaic.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    25566 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/autoaugment.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3149 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/backbone_factory.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    11729 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8045 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_lite_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    28272 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10376 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/preprocessing.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8679 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/train_backbone.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10868 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/coco_metric.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20312 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataloader.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    13974 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_coco_tfrecord.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10955 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_pascal_tfrecord.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4826 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/inspect_tfrecords.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4854 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/label_map_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3421 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/tfrecord_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    25881 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/det_model_fn.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20185 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/efficientdet_arch.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15189 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/hparams_config.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    26693 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/inference.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7478 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/iou_utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10488 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/anchors.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    37455 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/efficientdet_keras.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6057 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8245 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval_tflite.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6187 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/fpn_configs.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4371 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    16554 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7986 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/inspector.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3513 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/label_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    24393 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/postprocess.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3467 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/segmentation.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1815 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/tfmot.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12262 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    35736 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9515 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/util_keras.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3366 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/wbf.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15394 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/main.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20632 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/model_inspect.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8364 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/nms_np.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9084 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/argmax_matcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4914 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_coder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6749 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_list.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4011 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8842 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/matcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    17782 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/preprocessor.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4530 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/region_similarity_calculator.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2361 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/shape_utils.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    13987 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/target_assigner.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7305 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/tf_example_decoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3311 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/run_tflite.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3175 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/tensorrt.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    27904 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      835 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    17848 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/shape_utils.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12354 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/standard_fields.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2177 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/static_shape.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    48880 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/vis_utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12297 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/input_config_pb2.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1429 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/model_config.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    18041 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/example_generation_movielens.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10017 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/context_encoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2397 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/dotproduct_similarity.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10743 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/input_pipeline.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3194 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/label_encoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3290 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/losses.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5388 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/metrics.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4109 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12480 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model_launcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2842 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2396 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/audio_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1485 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/audio_classifier/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/config/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/config/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/image_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2090 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/image_classifier/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/model_spec/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1363 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/model_spec/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/object_detector/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1818 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/object_detector/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      786 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/cli/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      794 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/cli/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      802 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/cli/cli.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      796 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      804 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      820 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/api_gen.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/api_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      834 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/deprecated_api.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      834 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/golden_api_doc.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      820 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/include.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      810 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/compat.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/audio_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/data_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/image_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/image_searcher_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/metadata_loader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/object_detector_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/object_detector_dataloader_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_config.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_testutil.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/searcher_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/text_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      866 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/text_searcher_dataloader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      824 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/export_format.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/file_util.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/optimization/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/optimization/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/optimization/warmup.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      806 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/audio_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/classification_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/configs.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      832 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/custom_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/hub_loader.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/image_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/image_preprocessing.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writer_for_image_classifier.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/metadata_writer_for_bert.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      972 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      964 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/metadata_writer.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      944 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/audio_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/image_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/object_detector_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/recommendation_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/text_spec.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/object_detector.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/question_answer.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/recommendation.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      824 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/searcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/text_classifier.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/train_image_classifier_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/test_util.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      808 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/ondevice_scann_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/scann_converter.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      796 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/audio_classification_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      832 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/custom_model_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/image_classification_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/question_answer_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/recommendation_demo.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/text_classification_demo.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      844 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/autoaugment.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/gridmask.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/mosaic.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      878 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/autoaugment.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/backbone_factory.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      906 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_lite_builder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      892 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/preprocessing.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      884 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/train_backbone.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/coco_metric.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataloader.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      852 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      894 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_coco_tfrecord.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      898 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_pascal_tfrecord.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/inspect_tfrecords.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/label_map_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/tfrecord_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/det_model_fn.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/efficientdet_arch.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      866 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/hparams_config.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/inference.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/iou_utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/anchors.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/efficientdet_keras.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/eval.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/eval_tflite.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/fpn_configs.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/infer.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/infer_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/inspector.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/label_util.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/postprocess.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      874 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/segmentation.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/tfmot.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/train.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/train_lib.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/util_keras.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/wbf.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/main.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/model_inspect.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/nms_np.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/argmax_matcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      890 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_coder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_list.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      914 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/matcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/preprocessor.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      928 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/region_similarity_calculator.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      894 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/shape_utils.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      902 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/target_assigner.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      908 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/tf_example_decoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/run_tflite.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/tensorrt.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/shape_utils.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/standard_fields.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/static_shape.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      876 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/vis_utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/input_config_pb2.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/model_config.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/data/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/data/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      914 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/data/example_generation_movielens.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/__init__.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      890 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/context_encoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      902 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/dotproduct_similarity.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/input_pipeline.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/label_encoder.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/losses.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      874 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/metrics.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      918 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model_launcher.py
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/utils.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/question_answer/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1481 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/question_answer/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1320 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/spec/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3035 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/spec/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/searcher/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1686 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/searcher/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/text_classifier/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1480 2023-04-05 04:42:45.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/text_classifier/__init__.py
-drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-05 05:07:27.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4494 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/PKG-INFO
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    26115 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/SOURCES.txt
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)        1 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/dependency_links.txt
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       78 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/entry_points.txt
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      562 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/requires.txt
--rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       39 2023-04-05 05:07:26.000000 tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/top_level.txt
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4494 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/PKG-INFO
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       38 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/setup.cfg
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4567 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/setup.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      722 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      730 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      673 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/cli/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/cli/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4255 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/cli/cli.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      731 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2418 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/api_gen.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9856 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/api_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1269 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/deprecated_api.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8038 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/golden_api.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4764 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/golden_api_doc.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2824 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/include.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2072 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/compat.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15006 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/audio_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1334 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/data_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7311 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4180 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/image_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6248 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/image_searcher_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2459 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/metadata_loader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15144 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14165 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1865 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_config.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    11908 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6126 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_testutil.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3750 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/searcher_dataloader.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      566 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/annotations.json
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1019 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/test_annotations.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      898 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/train_annotations.json
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      420 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v1.1.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1654 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v2.0.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      421 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v1.1.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1654 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v2.0.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14998 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/text_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4854 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/text_searcher_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1031 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/export_format.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1092 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/file_util.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/optimization/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/optimization/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2213 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/optimization/warmup.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5964 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/audio_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5384 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/classification_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7258 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/configs.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9301 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/custom_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3856 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/hub_loader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14127 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/image_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8529 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/image_preprocessing.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8129 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writer_for_image_classifier.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9295 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/metadata_writer_for_bert.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6448 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5309 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5928 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/metadata_writer.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6098 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4563 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    23901 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/audio_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5557 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/image_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    23482 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/object_detector_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1916 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/recommendation_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    43235 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/text_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1781 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12268 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12155 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/object_detector.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10179 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/question_answer.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10005 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/recommendation.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    14665 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/searcher.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1960 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/average_word_vec_metadata.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2394 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_classifier_metadata.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2575 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_qa_metadata.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3127 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientdet_lite0_metadata.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1904 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientnet_lite0_metadata.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1282 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/mobilenet_v3_small_100_224_embedder_scann.json
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9596 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/text_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8241 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/train_image_classifier_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5663 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/test_util.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1856 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/ondevice_scann_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9289 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/scann_converter.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      608 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6869 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/audio_classification_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7862 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/custom_model_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2613 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/image_classification_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2829 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/question_answer_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5356 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/recommendation_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3078 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/text_classification_demo.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    66601 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/autoaugment.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4635 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/gridmask.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8379 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/mosaic.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    25566 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/autoaugment.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3149 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/backbone_factory.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    11729 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8045 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_lite_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    28272 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10376 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/preprocessing.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8679 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/train_backbone.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10868 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/coco_metric.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20312 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataloader.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    13974 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_coco_tfrecord.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10955 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_pascal_tfrecord.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4826 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/inspect_tfrecords.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4854 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/label_map_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3421 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/tfrecord_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    25881 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/det_model_fn.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20185 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/efficientdet_arch.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15189 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/hparams_config.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    26693 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/inference.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7478 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/iou_utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10488 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/anchors.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    37455 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/efficientdet_keras.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6057 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8245 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval_tflite.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6187 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/fpn_configs.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4371 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    16554 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7986 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/inspector.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3513 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/label_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    24393 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/postprocess.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3467 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/segmentation.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1815 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/tfmot.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12262 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    35736 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9515 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/util_keras.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3366 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/wbf.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    15394 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/main.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    20632 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/model_inspect.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8364 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/nms_np.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      682 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     9084 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/argmax_matcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4914 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_coder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     6749 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_list.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4011 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     8842 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/matcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    17782 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/preprocessor.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4530 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/region_similarity_calculator.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2361 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/shape_utils.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    13987 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/target_assigner.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     7305 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/tf_example_decoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3311 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/run_tflite.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3175 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/tensorrt.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    27904 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      835 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    17848 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/shape_utils.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12354 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/standard_fields.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2177 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/static_shape.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    48880 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/vis_utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12297 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/input_config_pb2.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1429 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/model_config.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    18041 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/example_generation_movielens.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      630 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10017 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/context_encoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2397 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/dotproduct_similarity.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    10743 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/input_pipeline.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3194 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/label_encoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3290 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/losses.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     5388 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/metrics.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4109 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    12480 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model_launcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2842 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2396 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/audio_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1485 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/audio_classifier/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/config/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/config/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/image_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     2090 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/image_classifier/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/model_spec/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1363 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/model_spec/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/object_detector/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1818 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/object_detector/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      786 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/cli/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      794 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/cli/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      802 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/cli/cli.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      796 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      804 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      820 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/api_gen.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/api_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      834 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/deprecated_api.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      834 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/golden_api_doc.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      820 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/include.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      810 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/compat.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/audio_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/data_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/image_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/image_searcher_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/metadata_loader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/object_detector_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/object_detector_dataloader_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_config.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_testutil.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/searcher_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/text_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      866 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/text_searcher_dataloader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      824 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/export_format.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/file_util.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/optimization/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/optimization/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/optimization/warmup.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      806 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/audio_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/classification_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      822 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/configs.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      832 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/custom_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/hub_loader.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/image_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/image_preprocessing.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writer_for_image_classifier.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/metadata_writer_for_bert.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      972 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      964 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/metadata_writer.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      944 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/audio_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/image_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/object_detector_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/recommendation_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/text_spec.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      828 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/object_detector.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/question_answer.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/recommendation.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      824 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/searcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/text_classifier.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/train_image_classifier_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      816 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/test_util.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      808 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/ondevice_scann_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      840 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/scann_converter.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      796 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/audio_classification_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      832 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/custom_model_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/image_classification_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      838 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/question_answer_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/recommendation_demo.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/text_classification_demo.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      836 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      844 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/autoaugment.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/gridmask.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/mosaic.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      878 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/autoaugment.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/backbone_factory.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      906 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_lite_builder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      892 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/preprocessing.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      884 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/train_backbone.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/coco_metric.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataloader.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      852 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      894 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_coco_tfrecord.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      898 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_pascal_tfrecord.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/inspect_tfrecords.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/label_map_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/tfrecord_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/det_model_fn.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/efficientdet_arch.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      866 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/hparams_config.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/inference.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/iou_utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/anchors.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/efficientdet_keras.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/eval.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/eval_tflite.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/fpn_configs.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/infer.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/infer_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/inspector.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/label_util.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/postprocess.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      874 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/segmentation.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/tfmot.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      860 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/train.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      868 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/train_lib.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/util_keras.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/wbf.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      846 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/main.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      864 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/model_inspect.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      850 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/nms_np.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/argmax_matcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      890 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_coder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_list.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      914 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/matcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/preprocessor.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      928 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/region_similarity_calculator.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      894 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/shape_utils.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      902 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/target_assigner.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      908 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/tf_example_decoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/run_tflite.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      854 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/tensorrt.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      848 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      880 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/shape_utils.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/standard_fields.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      882 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/static_shape.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      876 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/vis_utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      862 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      896 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/input_config_pb2.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/model_config.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/data/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      856 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/data/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      914 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/data/example_generation_movielens.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      858 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/__init__.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      890 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/context_encoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      902 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/dotproduct_similarity.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      888 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/input_pipeline.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      886 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/label_encoder.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      872 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/losses.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      874 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/metrics.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      900 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      918 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model_launcher.py
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      870 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/utils.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/question_answer/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1481 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/question_answer/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1320 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/spec/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     3035 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/spec/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/searcher/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1686 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/searcher/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/text_classifier/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     1480 2023-04-06 04:42:46.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/text_classifier/__init__.py
+drwxrwsr-x   0 kbuilder  (1015) kokoro    (1037)        0 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)     4494 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/PKG-INFO
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)    26115 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/SOURCES.txt
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)        1 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/dependency_links.txt
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       78 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/entry_points.txt
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)      562 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/requires.txt
+-rw-rw-r--   0 kbuilder  (1015) kokoro    (1037)       39 2023-04-06 05:08:44.000000 tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/top_level.txt
```

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/PKG-INFO` & `tflite-model-maker-nightly-0.4.3.dev202304060508/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tflite-model-maker-nightly
-Version: 0.4.3.dev202304050507
+Version: 0.4.3.dev202304060508
 Summary: TFLite Model Maker: a model customization library for on-device applications.
 Home-page: http://github.com/tensorflow/examples
 Download-URL: https://github.com/tensorflow/examples/tags
 Author: Google LLC
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tensorflow,lite,model customization,transfer learning
```

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/setup.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/setup.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/cli/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/cli/cli.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/cli/cli.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/api_gen.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/api_gen.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/api_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/api_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/deprecated_api.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/deprecated_api.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/golden_api.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/golden_api.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/golden_api_doc.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/golden_api_doc.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/api/include.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/api/include.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/compat.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/compat.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/audio_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/audio_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/data_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/data_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/image_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/image_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/image_searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/image_searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/metadata_loader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/metadata_loader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/object_detector_dataloader_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_testutil.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/recommendation_testutil.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/annotations.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/annotations.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/test_annotations.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/test_annotations.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/train_annotations.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/object_detection_csv/json_files/train_annotations.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v2.0.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/dev-v2.0.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v2.0.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/testdata/squad_testdata/train-v2.0.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/text_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/text_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/data_util/text_searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/data_util/text_searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/export_format.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/export_format.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/file_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/file_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/optimization/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/optimization/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/optimization/warmup.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/optimization/warmup.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/audio_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/audio_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/classification_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/classification_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/configs.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/configs.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/custom_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/custom_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/hub_loader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/hub_loader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/image_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/image_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/image_preprocessing.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/image_preprocessing.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writer_for_image_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writer_for_image_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/metadata_writer_for_bert.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/metadata_writer_for_bert.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/metadata_writer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/metadata_writer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/audio_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/audio_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/image_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/image_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/object_detector_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/object_detector_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/recommendation_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/recommendation_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/text_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/text_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_spec/util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_spec/util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/model_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/model_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/object_detector.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/object_detector.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/question_answer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/question_answer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/recommendation.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/recommendation.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/searcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/searcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/average_word_vec_metadata.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/average_word_vec_metadata.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_classifier_metadata.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_classifier_metadata.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_qa_metadata.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/bert_qa_metadata.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientdet_lite0_metadata.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientdet_lite0_metadata.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientnet_lite0_metadata.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/efficientnet_lite0_metadata.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/testdata/mobilenet_v3_small_100_224_embedder_scann.json` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/testdata/mobilenet_v3_small_100_224_embedder_scann.json`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/task/train_image_classifier_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/task/train_image_classifier_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/test_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/test_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/ondevice_scann_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/ondevice_scann_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/core/utils/scann_converter.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/core/utils/scann_converter.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/audio_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/audio_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/custom_model_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/custom_model_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/image_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/image_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/question_answer_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/question_answer_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/recommendation_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/recommendation_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/demo/text_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/demo/text_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/autoaugment.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/autoaugment.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/gridmask.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/gridmask.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/mosaic.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/aug/mosaic.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/autoaugment.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/autoaugment.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/backbone_factory.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/backbone_factory.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_lite_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_lite_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/efficientnet_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/preprocessing.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/preprocessing.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/train_backbone.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/backbone/train_backbone.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/coco_metric.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/coco_metric.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_coco_tfrecord.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_coco_tfrecord.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_pascal_tfrecord.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/create_pascal_tfrecord.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/inspect_tfrecords.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/inspect_tfrecords.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/label_map_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/label_map_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/tfrecord_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/dataset/tfrecord_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/det_model_fn.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/det_model_fn.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/efficientdet_arch.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/efficientdet_arch.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/hparams_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/hparams_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/inference.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/inference.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/iou_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/iou_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/anchors.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/anchors.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/efficientdet_keras.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/efficientdet_keras.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval_tflite.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/eval_tflite.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/fpn_configs.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/fpn_configs.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/infer_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/inspector.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/inspector.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/label_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/label_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/postprocess.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/postprocess.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/segmentation.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/segmentation.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/tfmot.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/tfmot.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/train_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/util_keras.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/util_keras.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/wbf.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/keras/wbf.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/main.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/main.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/model_inspect.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/model_inspect.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/nms_np.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/nms_np.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/argmax_matcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/argmax_matcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_coder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_coder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_list.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/box_list.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/matcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/matcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/preprocessor.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/preprocessor.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/region_similarity_calculator.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/region_similarity_calculator.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/shape_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/shape_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/target_assigner.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/target_assigner.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/tf_example_decoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/object_detection/tf_example_decoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/run_tflite.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/run_tflite.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/tensorrt.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/tensorrt.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/shape_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/shape_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/standard_fields.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/standard_fields.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/static_shape.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/static_shape.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/vis_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/efficientdet/visualize/vis_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/input_config_pb2.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/input_config_pb2.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/model_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/configs/model_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/example_generation_movielens.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/data/example_generation_movielens.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/context_encoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/context_encoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/dotproduct_similarity.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/dotproduct_similarity.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/input_pipeline.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/input_pipeline.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/label_encoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/label_encoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/losses.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/losses.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/metrics.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/metrics.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model_launcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/recommendation_model_launcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tensorflow_examples/lite/model_maker/third_party/recommendation/ml/model/utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -56,8 +56,8 @@
 # https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker
 # pylint: disable=g-bad-import-order
 from tensorflow_examples.lite.model_maker.core.data_util.image_dataloader import ImageClassifierDataLoader
 from tensorflow_examples.lite.model_maker.core.export_format import ExportFormat
 from tensorflow_examples.lite.model_maker.core.task import configs
 # pylint: enable=g-bad-import-order
 
-__version__ = '0.4.3.dev202304050507'
+__version__ = '0.4.3.dev202304060508'
```

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/audio_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/audio_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/config/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/config/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/image_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/image_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/model_spec/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/model_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/object_detector/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/object_detector/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/cli/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/cli/cli.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/cli/cli.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/api_gen.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/api_gen.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/api_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/api_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/deprecated_api.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/deprecated_api.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/golden_api_doc.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/golden_api_doc.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/api/include.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/api/include.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/compat.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/compat.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/audio_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/audio_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/data_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/data_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/image_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/image_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/image_searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/image_searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/metadata_loader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/metadata_loader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/object_detector_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/object_detector_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/object_detector_dataloader_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/object_detector_dataloader_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/recommendation_testutil.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/recommendation_testutil.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/text_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/text_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/data_util/text_searcher_dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/data_util/text_searcher_dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/export_format.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/export_format.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/file_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/file_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/optimization/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/optimization/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/optimization/warmup.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/optimization/warmup.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/audio_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/audio_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/classification_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/classification_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/configs.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/configs.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/custom_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/custom_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/hub_loader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/hub_loader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/image_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/image_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/image_preprocessing.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/image_preprocessing.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writer_for_image_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writer_for_image_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/metadata_writer_for_bert.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/metadata_writer_for_bert.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/question_answerer/metadata_writer_for_bert_question_answerer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/bert/text_classifier/metadata_writer_for_bert_text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/metadata_writer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/metadata_writer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/metadata_writers/text_classifier/metadata_writer_for_text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/audio_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/audio_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/image_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/image_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/object_detector_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/object_detector_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/recommendation_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/recommendation_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/text_spec.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/text_spec.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_spec/util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_spec/util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/model_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/model_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/object_detector.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/object_detector.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/question_answer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/question_answer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/recommendation.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/recommendation.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/searcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/searcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/text_classifier.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/text_classifier.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/task/train_image_classifier_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/task/train_image_classifier_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/test_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/test_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/ondevice_scann_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/ondevice_scann_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/core/utils/scann_converter.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/core/utils/scann_converter.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/audio_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/audio_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/custom_model_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/custom_model_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/image_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/image_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/question_answer_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/question_answer_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/recommendation_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/recommendation_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/demo/text_classification_demo.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/demo/text_classification_demo.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/autoaugment.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/autoaugment.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/gridmask.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/gridmask.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/aug/mosaic.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/aug/mosaic.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/autoaugment.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/autoaugment.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/backbone_factory.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/backbone_factory.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_lite_builder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_lite_builder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/efficientnet_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/preprocessing.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/preprocessing.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/backbone/train_backbone.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/backbone/train_backbone.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/coco_metric.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/coco_metric.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataloader.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataloader.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_coco_tfrecord.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_coco_tfrecord.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_pascal_tfrecord.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/create_pascal_tfrecord.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/inspect_tfrecords.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/inspect_tfrecords.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/label_map_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/label_map_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/dataset/tfrecord_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/dataset/tfrecord_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/det_model_fn.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/det_model_fn.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/efficientdet_arch.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/efficientdet_arch.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/hparams_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/hparams_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/inference.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/inference.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/iou_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/iou_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/anchors.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/anchors.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/efficientdet_keras.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/efficientdet_keras.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/eval.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/eval.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/eval_tflite.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/eval_tflite.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/fpn_configs.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/fpn_configs.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/infer.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/infer.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/infer_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/infer_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/inspector.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/inspector.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/label_util.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/label_util.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/postprocess.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/postprocess.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/segmentation.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/segmentation.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/tfmot.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/tfmot.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/train.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/train.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/train_lib.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/train_lib.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/util_keras.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/util_keras.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/keras/wbf.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/keras/wbf.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/main.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/main.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/model_inspect.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/model_inspect.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/nms_np.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/nms_np.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/argmax_matcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/argmax_matcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_coder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_coder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_list.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/box_list.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/faster_rcnn_box_coder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/matcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/matcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/preprocessor.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/preprocessor.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/region_similarity_calculator.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/region_similarity_calculator.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/shape_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/shape_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/target_assigner.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/target_assigner.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/object_detection/tf_example_decoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/object_detection/tf_example_decoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/run_tflite.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/run_tflite.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/tensorrt.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/tensorrt.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/shape_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/shape_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/standard_fields.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/standard_fields.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/static_shape.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/static_shape.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/efficientdet/visualize/vis_utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/efficientdet/visualize/vis_utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/input_config_pb2.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/input_config_pb2.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/configs/model_config.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/configs/model_config.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/data/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/data/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/data/example_generation_movielens.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/data/example_generation_movielens.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/context_encoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/context_encoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/dotproduct_similarity.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/dotproduct_similarity.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/input_pipeline.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/input_pipeline.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/label_encoder.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/label_encoder.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/losses.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/losses.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/metrics.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/metrics.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model_launcher.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/recommendation_model_launcher.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/python/third_party/recommendation/ml/model/utils.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/python/third_party/recommendation/ml/model/utils.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/question_answer/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/question_answer/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/recommendation/spec/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/recommendation/spec/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/searcher/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/searcher/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker/text_classifier/__init__.py` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker/text_classifier/__init__.py`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/PKG-INFO` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tflite-model-maker-nightly
-Version: 0.4.3.dev202304050507
+Version: 0.4.3.dev202304060508
 Summary: TFLite Model Maker: a model customization library for on-device applications.
 Home-page: http://github.com/tensorflow/examples
 Download-URL: https://github.com/tensorflow/examples/tags
 Author: Google LLC
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tensorflow,lite,model customization,transfer learning
```

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/SOURCES.txt` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tflite-model-maker-nightly-0.4.3.dev202304050507/src/tflite_model_maker_nightly.egg-info/requires.txt` & `tflite-model-maker-nightly-0.4.3.dev202304060508/src/tflite_model_maker_nightly.egg-info/requires.txt`

 * *Files identical despite different names*

