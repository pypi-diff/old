# Comparing `tmp/autogluon.multimodal-0.7.0b20230405.tar.gz` & `tmp/autogluon.multimodal-0.7.0b20230406.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "autogluon.multimodal-0.7.0b20230405.tar", last modified: Wed Apr  5 09:04:33 2023, max compression
+gzip compressed data, was "autogluon.multimodal-0.7.0b20230406.tar", last modified: Thu Apr  6 09:04:11 2023, max compression
```

## Comparing `autogluon.multimodal-0.7.0b20230405.tar` & `autogluon.multimodal-0.7.0b20230406.tar`

### file list

```diff
@@ -1,115 +1,118 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.757135 autogluon.multimodal-0.7.0b20230405/
--rw-r--r--   0 runner    (1001) docker     (123)    12573 2023-04-05 09:04:33.757135 autogluon.multimodal-0.7.0b20230405/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 09:04:33.757135 autogluon.multimodal-0.7.0b20230405/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.745135 autogluon.multimodal-0.7.0b20230405/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.745135 autogluon.multimodal-0.7.0b20230405/src/autogluon/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.749135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/
--rw-r--r--   0 runner    (1001) docker     (123)      245 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7089 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.749135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9729 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/collator.py
--rw-r--r--   0 runner    (1001) docker     (123)     8685 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/datamodule.py
--rw-r--r--   0 runner    (1001) docker     (123)     4312 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)    26476 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/infer_types.py
--rw-r--r--   0 runner    (1001) docker     (123)    10599 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/label_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     7388 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/mixup.py
--rw-r--r--   0 runner    (1001) docker     (123)    30806 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/preprocess_dataframe.py
--rw-r--r--   0 runner    (1001) docker     (123)     3597 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_categorical.py
--rw-r--r--   0 runner    (1001) docker     (123)    14453 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_document.py
--rw-r--r--   0 runner    (1001) docker     (123)    13863 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_image.py
--rw-r--r--   0 runner    (1001) docker     (123)     2560 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_label.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.749135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3073 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/process_mmdet.py
--rw-r--r--   0 runner    (1001) docker     (123)     7000 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/process_mmlab_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3095 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/process_mmocr.py
--rw-r--r--   0 runner    (1001) docker     (123)     6275 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_ner.py
--rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_numerical.py
--rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_text.py
--rw-r--r--   0 runner    (1001) docker     (123)     7005 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/randaug.py
--rw-r--r--   0 runner    (1001) docker     (123)     3610 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/template_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)    25379 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/templates.py
--rw-r--r--   0 runner    (1001) docker     (123)     8404 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/trivial_augmenter.py
--rw-r--r--   0 runner    (1001) docker     (123)    20548 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    85367 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/matcher.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.753135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/
--rw-r--r--   0 runner    (1001) docker     (123)      827 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22571 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/adaptation_layers.py
--rw-r--r--   0 runner    (1001) docker     (123)     4658 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/categorical_mlp.py
--rw-r--r--   0 runner    (1001) docker     (123)    11194 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/categorical_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)     8474 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/clip.py
--rw-r--r--   0 runner    (1001) docker     (123)     7244 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/document_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    27570 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/ft_transformer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.753135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2553 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7327 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_mlp.py
--rw-r--r--   0 runner    (1001) docker     (123)     6378 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_ner.py
--rw-r--r--   0 runner    (1001) docker     (123)     8983 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    11351 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/huggingface_text.py
--rw-r--r--   0 runner    (1001) docker     (123)     4456 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mlp.py
--rw-r--r--   0 runner    (1001) docker     (123)    14422 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mmdet_image.py
--rw-r--r--   0 runner    (1001) docker     (123)     3684 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mmocr_text_detection.py
--rw-r--r--   0 runner    (1001) docker     (123)     3994 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mmocr_text_recognition.py
--rw-r--r--   0 runner    (1001) docker     (123)    10077 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/ner_text.py
--rw-r--r--   0 runner    (1001) docker     (123)     4126 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/numerical_mlp.py
--rw-r--r--   0 runner    (1001) docker     (123)    20906 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/numerical_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    12914 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/t_few.py
--rw-r--r--   0 runner    (1001) docker     (123)    11757 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/timm_image.py
--rw-r--r--   0 runner    (1001) docker     (123)    25891 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.753135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14966 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/deepspeed.py
--rw-r--r--   0 runner    (1001) docker     (123)    20753 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_distiller.py
--rw-r--r--   0 runner    (1001) docker     (123)    17122 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_matcher.py
--rw-r--r--   0 runner    (1001) docker     (123)    12441 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_mmdet.py
--rw-r--r--   0 runner    (1001) docker     (123)    16451 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     8280 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_ner.py
--rw-r--r--   0 runner    (1001) docker     (123)    12454 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/losses.py
--rw-r--r--   0 runner    (1001) docker     (123)     5828 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lr_scheduler.py
--rw-r--r--   0 runner    (1001) docker     (123)    30882 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)   120464 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/predictor.py
--rw-r--r--   0 runner    (1001) docker     (123)    24494 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/presets.py
--rw-r--r--   0 runner    (1001) docker     (123)     6730 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/problem_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     3648 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.757135 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     2717 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5231 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     7766 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/checkpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/cloud_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     3731 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/colormap.py
--rw-r--r--   0 runner    (1001) docker     (123)    29541 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    22137 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/data.py
--rw-r--r--   0 runner    (1001) docker     (123)    10418 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/download.py
--rw-r--r--   0 runner    (1001) docker     (123)     9439 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/environment.py
--rw-r--r--   0 runner    (1001) docker     (123)    11759 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/export.py
--rw-r--r--   0 runner    (1001) docker     (123)     8122 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/few_shot_learning.py
--rw-r--r--   0 runner    (1001) docker     (123)     8302 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/hpo.py
--rw-r--r--   0 runner    (1001) docker     (123)    17759 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/inference.py
--rw-r--r--   0 runner    (1001) docker     (123)    13437 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/label_studio.py
--rw-r--r--   0 runner    (1001) docker     (123)     1816 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/load.py
--rw-r--r--   0 runner    (1001) docker     (123)     4701 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/log.py
--rw-r--r--   0 runner    (1001) docker     (123)    19409 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/map.py
--rw-r--r--   0 runner    (1001) docker     (123)    18206 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/matcher.py
--rw-r--r--   0 runner    (1001) docker     (123)    13569 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     7080 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/misc.py
--rw-r--r--   0 runner    (1001) docker     (123)     6768 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/mmcv.py
--rw-r--r--   0 runner    (1001) docker     (123)    21936 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/nlpaug.py
--rw-r--r--   0 runner    (1001) docker     (123)    50614 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/object_detection.py
--rw-r--r--   0 runner    (1001) docker     (123)    18477 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/object_detection_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     5608 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/onnx.py
--rw-r--r--   0 runner    (1001) docker     (123)     4782 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     3840 2023-04-05 09:03:57.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/save.py
--rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:04:33.745135 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12573 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4687 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/namespace_packages.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 09:04:33.000000 autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.875295 autogluon.multimodal-0.7.0b20230406/
+-rw-r--r--   0 runner    (1001) docker     (123)    12573 2023-04-06 09:04:11.875295 autogluon.multimodal-0.7.0b20230406/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:04:11.875295 autogluon.multimodal-0.7.0b20230406/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3223 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.863296 autogluon.multimodal-0.7.0b20230406/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.863296 autogluon.multimodal-0.7.0b20230406/src/autogluon/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.867296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/
+-rw-r--r--   0 runner    (1001) docker     (123)      245 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7189 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.867296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9729 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/collator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8930 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/datamodule.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4312 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.867296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/dataset_mmlab/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/dataset_mmlab/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29484 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/dataset_mmlab/multi_image_mix_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26476 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/infer_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10599 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/label_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7388 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/mixup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30806 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/preprocess_dataframe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3597 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_categorical.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14453 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_document.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13863 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2758 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_label.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.867296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6568 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/process_mmdet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7000 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/process_mmlab_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3095 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/process_mmocr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6275 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_ner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_numerical.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20340 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_text.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7005 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/randaug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3610 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/template_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25379 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8404 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/trivial_augmenter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21116 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    85367 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/matcher.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.871296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      827 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22571 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/adaptation_layers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4658 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/categorical_mlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11194 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/categorical_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8474 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/clip.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7244 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/document_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27570 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/ft_transformer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.871296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2553 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7327 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_mlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6378 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_ner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8983 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11351 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/huggingface_text.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4456 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24560 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mmdet_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3684 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mmocr_text_detection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3994 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mmocr_text_recognition.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10077 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/ner_text.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4126 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/numerical_mlp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20906 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/numerical_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12914 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/t_few.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11757 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/timm_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25891 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.871296 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14966 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/deepspeed.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20753 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_distiller.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17122 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_matcher.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12441 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_mmdet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16451 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8280 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_ner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12454 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/losses.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5828 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lr_scheduler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30882 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)   121528 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/predictor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24352 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/presets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6730 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/problem_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3648 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.875295 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     2717 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5231 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7766 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/checkpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/cloud_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3731 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/colormap.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29541 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22137 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10418 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/download.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9439 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11759 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8122 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/few_shot_learning.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8302 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/hpo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17759 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/inference.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13437 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/label_studio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1816 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/load.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4701 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19409 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/map.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18206 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/matcher.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13569 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7080 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/misc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6768 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/mmcv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21936 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/nlpaug.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50614 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/object_detection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18477 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/object_detection_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5608 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/onnx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4782 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3840 2023-04-06 09:03:34.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/save.py
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:11.863296 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12573 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4814 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/namespace_packages.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1127 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:04:11.000000 autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/zip-safe
```

### Comparing `autogluon.multimodal-0.7.0b20230405/PKG-INFO` & `autogluon.multimodal-0.7.0b20230406/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: autogluon.multimodal
-Version: 0.7.0b20230405
+Version: 0.7.0b20230406
 Summary: AutoML for Image, Text, and Tabular Data
 Home-page: https://github.com/autogluon/autogluon
 Author: AutoGluon Community
 License: Apache-2.0
 Project-URL: Documentation, https://auto.gluon.ai
 Project-URL: Bug Reports, https://github.com/autogluon/autogluon/issues
 Project-URL: Source, https://github.com/autogluon/autogluon/
```

### Comparing `autogluon.multimodal-0.7.0b20230405/setup.py` & `autogluon.multimodal-0.7.0b20230406/setup.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/constants.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/constants.py`

 * *Files 2% similar despite different names*

```diff
@@ -287,7 +287,11 @@
 
 # presets
 DEFAULT = "default"
 HIGH_QUALITY = "high_quality"
 MEDIUM_QUALITY = "medium_quality"
 BEST_QUALITY = "best_quality"
 ALL_MODEL_QUALITIES = [HIGH_QUALITY, MEDIUM_QUALITY, BEST_QUALITY, DEFAULT]
+
+# datasets
+DEFAULT_DATASET = "default_dataset"
+MULTI_IMAGE_MIX_DATASET = "multi_image_mix_dataset"
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/__init__.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/__init__.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/collator.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/collator.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/datamodule.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/datamodule.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 from typing import Dict, List, Optional, Union
 
 import pandas as pd
 from pytorch_lightning import LightningDataModule
-from torch.utils.data import DataLoader
+from torch.utils.data import DataLoader, Dataset
 
-from ..constants import PREDICT, TEST, TRAIN, VALIDATE
+from ..constants import DEFAULT_DATASET, PREDICT, TEST, TRAIN, VALIDATE
 from .dataset import BaseDataset
 from .preprocess_dataframe import MultiModalFeaturePreprocessor
 from .utils import get_collate_fn
 
 
 class BaseDataModule(LightningDataModule):
     """
@@ -22,14 +22,15 @@
     def __init__(
         self,
         df_preprocessor: Union[MultiModalFeaturePreprocessor, List[MultiModalFeaturePreprocessor]],
         data_processors: Union[dict, List[dict]],
         per_gpu_batch_size: int,
         num_workers: int,
         train_data: Optional[pd.DataFrame] = None,
+        train_dataset: Optional[Dataset] = None,
         validate_data: Optional[pd.DataFrame] = None,
         test_data: Optional[pd.DataFrame] = None,
         predict_data: Optional[pd.DataFrame] = None,
         id_mappings: Optional[Union[Dict[str, Dict], Dict[str, pd.Series]]] = None,
         val_use_training_mode: bool = False,
     ):
         """
@@ -46,53 +47,60 @@
             one modality of one model. This helps scale up training arbitrary combinations of models.
         per_gpu_batch_size
             Mini-batch size for each GPU.
         num_workers
             Number of workers for Pytorch DataLoader.
         train_data
             Training data.
+        train_dataset
+            Training dataset.
         validate_data
             Validation data.
         test_data
             Test data.
         predict_data
             Prediction data. No labels required in it.
         id_mappings
-             Id-to-content mappings. The contents can be text, image, etc.
-             This is used when the dataframe contains the query/response indexes instead of their contents.
+            Id-to-content mappings. The contents can be text, image, etc.
+            This is used when the dataframe contains the query/response indexes instead of their contents.
         val_use_training_mode
-             whether we are triggering is_training when creating the dataset for validation.
-             This is used when we want to use val_loss as val metric, and thus we'll use data pipeline
-             for training instead of for inference during validation.
+            whether we are triggering is_training when creating the dataset for validation.
+            This is used when we want to use val_loss as val metric, and thus we'll use data pipeline
+            for training instead of for inference during validation.
         """
         super().__init__()
         self.prepare_data_per_node = True
 
         if isinstance(df_preprocessor, MultiModalFeaturePreprocessor):
             df_preprocessor = [df_preprocessor]
         if isinstance(data_processors, dict):
             data_processors = [data_processors]
 
         self.df_preprocessor = df_preprocessor
         self.data_processors = data_processors
         self.per_gpu_batch_size = per_gpu_batch_size
         self.num_workers = num_workers
         self.train_data = train_data
+        self.train_dataset = train_dataset
         self.validate_data = validate_data
         self.test_data = test_data
         self.predict_data = predict_data
         self.id_mappings = id_mappings
         self.val_use_training_mode = val_use_training_mode
 
     def set_dataset(self, split):
-        data_split = getattr(self, f"{split}_data")
         if self.val_use_training_mode:
             is_training = split in [TRAIN, VALIDATE]
         else:
             is_training = split == TRAIN
+
+        if is_training and self.train_dataset is not None:
+            return
+
+        data_split = getattr(self, f"{split}_data")
         dataset = BaseDataset(
             data=data_split,
             preprocessor=self.df_preprocessor,
             processors=self.data_processors,
             id_mappings=self.id_mappings,
             is_training=is_training,
         )
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/dataset.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/dataset.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/infer_types.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/infer_types.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/label_encoder.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/label_encoder.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/mixup.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/mixup.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/preprocess_dataframe.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/preprocess_dataframe.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_categorical.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_categorical.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_document.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_document.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_image.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_image.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_label.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_label.py`

 * *Files 12% similar despite different names*

```diff
@@ -66,25 +66,28 @@
         }
 
     def __call__(
         self,
         labels: Dict[str, Union[int, float]],
         feature_modalities: Dict[str, Union[int, float, list]],
         is_training: bool,
+        load_only: bool = False,  # TODO: refactor mmdet_image and remove this
     ) -> Dict:
         """
         Extract one sample's labels and customize them for a specific model.
 
         Parameters
         ----------
         labels
             Labels of one sample.
         feature_modalities
             The modality of the feature columns.
         is_training
             Whether to do processing in the training mode. This unused flag is for the API compatibility.
+        load_only
+            Whether to only load the data. Other processing steps may happen in dataset.__getitem__.
 
         Returns
         -------
         A dictionary containing one sample's processed label.
         """
         return self.process_one_sample(labels)
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/process_mmdet.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/process_mmocr.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,17 +17,17 @@
 from ..utils import is_rois_input
 from .process_mmlab_base import MMLabProcessor
 
 logger = logging.getLogger(__name__)
 ImageFile.LOAD_TRUNCATED_IMAGES = True
 
 
-class MMDetProcessor(MMLabProcessor):
+class MMOcrProcessor(MMLabProcessor):
     """
-    Prepare rois data for mmdetection models.
+    Prepare data for mmocr models.
     """
 
     def __init__(
         self,
         model: nn.Module,
         max_img_num_per_col: Optional[int] = 1,
         missing_value_strategy: Optional[str] = "zero",
@@ -45,19 +45,19 @@
             - skip
                 Skip this sample
             -zero
                 Use an image with zero pixels.
         requires_column_info
             Whether to require feature column information in dataloader.
         """
-        from ...utils import CollateMMDet
+        from ...utils import CollateMMOcr
 
         super().__init__(
             model=model,
-            collate_func=CollateMMDet,
+            collate_func=CollateMMOcr,
             max_img_num_per_col=max_img_num_per_col,
             missing_value_strategy=missing_value_strategy,
             requires_column_info=requires_column_info,
         )
 
     def process_one_sample(
         self,
@@ -76,14 +76,15 @@
         is_training
             Whether to process images in the training mode.
 
         Returns
         -------
         A dictionary containing one sample's images and their number.
         """
+        # TODO: modify for MMOCR
         mm_data = dict(img_prefix=None, bbox_fields=[])
         ret = {}
 
         for per_col_name, per_col_content in image_paths.items():
             if is_rois_input(per_col_content):
                 rois = np.array(per_col_content)
                 mm_data["ann_info"] = dict(bboxes=rois[:, :4], labels=rois[:, 4])
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_mmlab/process_mmlab_base.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_mmlab/process_mmlab_base.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_ner.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_ner.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_numerical.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_numerical.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/process_text.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/process_text.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/randaug.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/randaug.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/template_engine.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/template_engine.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/templates.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/templates.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/trivial_augmenter.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/trivial_augmenter.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/data/utils.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/data/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
     IMAGENET_DEFAULT_STD,
     IMAGENET_INCEPTION_MEAN,
     IMAGENET_INCEPTION_STD,
 )
 from tokenizers import pre_tokenizers
 from torchvision import transforms
 
-from ..constants import CLIP_IMAGE_MEAN, CLIP_IMAGE_STD, IDENTIFIER, IMAGE, MMLAB_MODELS
+from ..constants import CLIP_IMAGE_MEAN, CLIP_IMAGE_STD, IDENTIFIER, IMAGE, MMDET_IMAGE, MMLAB_MODELS
 from .collator import DictCollator
 from .preprocess_dataframe import MultiModalFeaturePreprocessor
 
 try:
     from torchvision.transforms import InterpolationMode
 
     BICUBIC = InterpolationMode.BICUBIC
@@ -146,39 +146,54 @@
     assert len(set(lengths)) == 1  # make sure each modality has the same sample num
     sample_num = lengths[0]
 
     return modality_features, modality_types, sample_num
 
 
 def apply_data_processor(
-    per_sample_features: Dict, data_processors: Dict, feature_modalities: Dict, is_training: bool
+    per_sample_features: Dict,
+    data_processors: Dict,
+    feature_modalities: Dict,
+    is_training: bool,
+    load_only=False,
 ):
     """
     Process one sample's features.
 
     Parameters
     ----------
     per_sample_features
         Modality features of one sample.
     data_processors
         A dict of data processors.
     is_training
         Whether is training.
+    load_only
+        Whether to only load the data. Other processing steps may happen in dataset.__getitem__.
 
     Returns
     -------
     The processed features of one sample.
     """
     sample_features = {}
     for per_modality, per_modality_processors in data_processors.items():
         for per_model_processor in per_modality_processors:
             if per_modality in per_sample_features and per_sample_features[per_modality]:
                 sample_features.update(
                     per_model_processor(
-                        per_sample_features[per_modality], feature_modalities[per_modality], is_training=is_training
+                        per_sample_features[per_modality],
+                        feature_modalities[per_modality],
+                        is_training=is_training,
+                        load_only=load_only,
+                    )
+                    if per_model_processor.prefix.lower().startswith(MMDET_IMAGE)
+                    else per_model_processor(
+                        per_sample_features[per_modality],
+                        feature_modalities[per_modality],
+                        is_training=is_training,
                     )
                 )
 
     return sample_features
 
 
 def get_per_sample_features(
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/matcher.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/matcher.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/__init__.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/__init__.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/adaptation_layers.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/adaptation_layers.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/categorical_mlp.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/categorical_mlp.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/categorical_transformer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/categorical_transformer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/clip.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/clip.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/document_transformer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/document_transformer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/ft_transformer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/ft_transformer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/base.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/base.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_mlp.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_mlp.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_ner.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_ner.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/fusion/fusion_transformer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/fusion/fusion_transformer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/huggingface_text.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/huggingface_text.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mlp.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mlp.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mmocr_text_detection.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mmocr_text_detection.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/mmocr_text_recognition.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/mmocr_text_recognition.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/ner_text.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/ner_text.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/numerical_mlp.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/numerical_mlp.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/numerical_transformer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/numerical_transformer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/t_few.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/t_few.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/timm_image.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/timm_image.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/models/utils.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/models/utils.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/deepspeed.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/deepspeed.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_distiller.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_distiller.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_matcher.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_matcher.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_mmdet.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_mmdet.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_module.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_module.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lit_ner.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lit_ner.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/losses.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/losses.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/lr_scheduler.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/optimization/utils.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/optimization/utils.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/predictor.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/predictor.py`

 * *Files 0% similar despite different names*

```diff
@@ -56,14 +56,15 @@
     LAST_CHECKPOINT,
     LOGITS,
     MAP,
     MASKS,
     MAX,
     MIN,
     MODEL_CHECKPOINT,
+    MULTI_IMAGE_MIX_DATASET,
     MULTICLASS,
     NER,
     NER_RET,
     NUMERICAL,
     OBJECT_DETECTION,
     OCR_TEXT_DETECTION,
     OCR_TEXT_RECOGNITION,
@@ -78,14 +79,15 @@
     XYWH,
     Y_PRED,
     Y_PRED_PROB,
     Y_TRUE,
     ZERO_SHOT_IMAGE_CLASSIFICATION,
 )
 from .data.datamodule import BaseDataModule
+from .data.dataset_mmlab import MultiImageMixDataset
 from .data.infer_types import (
     infer_column_types,
     infer_label_column_type_by_problem_type,
     infer_problem_type_output_shape,
     infer_rois_column_type,
     is_image_column,
 )
@@ -1227,24 +1229,48 @@
 
         if teacher_df_preprocessor is not None:
             df_preprocessor = [df_preprocessor, teacher_df_preprocessor]
         if teacher_data_processors is not None:
             data_processors = [data_processors, teacher_data_processors]
 
         val_use_training_mode = (self._problem_type == OBJECT_DETECTION) and (validation_metric_name != MAP)
+        train_dataset = None
+        if (
+            self._problem_type == OBJECT_DETECTION
+            and self._model.config is not None
+            and MULTI_IMAGE_MIX_DATASET in self._model.config
+        ):
+            train_dataset = MultiImageMixDataset(
+                data=train_df,
+                preprocessor=[df_preprocessor],
+                processors=[data_processors],
+                model_config=self._model.config,
+                id_mappings=None,
+                is_training=True,
+            )
+            train_dm = BaseDataModule(
+                df_preprocessor=df_preprocessor,
+                data_processors=data_processors,
+                per_gpu_batch_size=config.env.per_gpu_batch_size,
+                num_workers=config.env.num_workers,
+                train_dataset=train_dataset,
+                validate_data=val_df,
+                val_use_training_mode=val_use_training_mode,
+            )
+        else:
+            train_dm = BaseDataModule(
+                df_preprocessor=df_preprocessor,
+                data_processors=data_processors,
+                per_gpu_batch_size=config.env.per_gpu_batch_size,
+                num_workers=config.env.num_workers,
+                train_data=train_df,
+                validate_data=val_df,
+                val_use_training_mode=val_use_training_mode,
+            )
 
-        train_dm = BaseDataModule(
-            df_preprocessor=df_preprocessor,
-            data_processors=data_processors,
-            per_gpu_batch_size=config.env.per_gpu_batch_size,
-            num_workers=config.env.num_workers,
-            train_data=train_df,
-            validate_data=val_df,
-            val_use_training_mode=val_use_training_mode,
-        )
         optimization_kwargs = dict(
             optim_type=config.optimization.optim_type,
             lr_choice=config.optimization.lr_choice,
             lr_schedule=config.optimization.lr_schedule,
             lr=config.optimization.learning_rate,
             lr_decay=config.optimization.lr_decay,
             end_lr=config.optimization.end_lr,
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/presets.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/presets.py`

 * *Files 1% similar despite different names*

```diff
@@ -316,15 +316,15 @@
         "env.precision": 32,
         "env.strategy": "ddp",
         "env.auto_select_gpus": False,  # Have to turn off for detection!
         "env.num_gpus": -1,
         "env.per_gpu_batch_size": 8,  # Works on 8G GPU
         "env.num_workers": 2,
         "optimization.learning_rate": 1e-4,
-        "optimization.lr_decay": 0.90,
+        "optimization.lr_decay": 0.9,
         "optimization.lr_mult": 100,
         "optimization.lr_choice": "two_stages",
         "optimization.top_k": 1,
         "optimization.top_k_average_method": "best",
         "optimization.warmup_steps": 0.0,
         "optimization.patience": 10,
         "optimization.val_metric": "map",
@@ -339,40 +339,37 @@
         hyperparameters.update(default_tunable_hyperparameters)
         hyperparameter_tune_kwargs.update(default_hyperparameter_tune_kwargs)
 
     if presets == MEDIUM_QUALITY:
         hyperparameters.update(
             {
                 "optimization.max_epochs": 30,
-                "optimization.lr_decay": 0.95,
                 "optimization.patience": 3,
                 "optimization.val_check_interval": 1.0,
                 "optimization.check_val_every_n_epoch": 3,
             }
         )
     elif presets in [DEFAULT, HIGH_QUALITY]:
         hyperparameters.update(
             {
                 "model.mmdet_image.checkpoint_name": "yolox_l_8x8_300e_coco",
                 "env.per_gpu_batch_size": 2,  # Works on 8G GPU
                 "optimization.learning_rate": 5e-5,
-                "optimization.lr_decay": 0.95,
                 "optimization.patience": 3,
                 "optimization.max_epochs": 50,
                 "optimization.val_check_interval": 1.0,
                 "optimization.check_val_every_n_epoch": 3,
             }
         )
     elif presets == BEST_QUALITY:
         hyperparameters.update(
             {
                 "model.mmdet_image.checkpoint_name": "yolox_x_8x8_300e_coco",
                 "env.per_gpu_batch_size": 1,  # Works on 8G GPU
                 "optimization.learning_rate": 1e-5,
-                "optimization.lr_decay": 0.95,
                 "optimization.patience": 20,
                 "optimization.max_epochs": 50,
             }
         )
     else:
         raise ValueError(f"Unknown preset type: {presets}")
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/problem_types.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/problem_types.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/registry.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/registry.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/__init__.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/cache.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/cache.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/checkpoint.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/checkpoint.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/cloud_io.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/cloud_io.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/colormap.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/colormap.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/config.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/config.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/data.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/data.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/download.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/download.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/environment.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/environment.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/export.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/export.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/few_shot_learning.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/few_shot_learning.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/hpo.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/hpo.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/inference.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/inference.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/label_studio.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/label_studio.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/load.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/load.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/log.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/log.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/map.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/map.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/matcher.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/matcher.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/metric.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/metric.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/misc.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/misc.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/mmcv.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/mmcv.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/model.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/model.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/nlpaug.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/nlpaug.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/object_detection.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/object_detection.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/object_detection_visualizer.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/object_detection_visualizer.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/onnx.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/onnx.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/pipeline.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/pipeline.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon/multimodal/utils/save.py` & `autogluon.multimodal-0.7.0b20230406/src/autogluon/multimodal/utils/save.py`

 * *Files identical despite different names*

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/PKG-INFO` & `autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: autogluon.multimodal
-Version: 0.7.0b20230405
+Version: 0.7.0b20230406
 Summary: AutoML for Image, Text, and Tabular Data
 Home-page: https://github.com/autogluon/autogluon
 Author: AutoGluon Community
 License: Apache-2.0
 Project-URL: Documentation, https://auto.gluon.ai
 Project-URL: Bug Reports, https://github.com/autogluon/autogluon/issues
 Project-URL: Source, https://github.com/autogluon/autogluon/
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/SOURCES.txt` & `autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -31,14 +31,16 @@
 src/autogluon/multimodal/data/process_numerical.py
 src/autogluon/multimodal/data/process_text.py
 src/autogluon/multimodal/data/randaug.py
 src/autogluon/multimodal/data/template_engine.py
 src/autogluon/multimodal/data/templates.py
 src/autogluon/multimodal/data/trivial_augmenter.py
 src/autogluon/multimodal/data/utils.py
+src/autogluon/multimodal/data/dataset_mmlab/__init__.py
+src/autogluon/multimodal/data/dataset_mmlab/multi_image_mix_dataset.py
 src/autogluon/multimodal/data/process_mmlab/__init__.py
 src/autogluon/multimodal/data/process_mmlab/process_mmdet.py
 src/autogluon/multimodal/data/process_mmlab/process_mmlab_base.py
 src/autogluon/multimodal/data/process_mmlab/process_mmocr.py
 src/autogluon/multimodal/models/__init__.py
 src/autogluon/multimodal/models/adaptation_layers.py
 src/autogluon/multimodal/models/categorical_mlp.py
```

### Comparing `autogluon.multimodal-0.7.0b20230405/src/autogluon.multimodal.egg-info/requires.txt` & `autogluon.multimodal-0.7.0b20230406/src/autogluon.multimodal.egg-info/requires.txt`

 * *Files 11% similar despite different names*

```diff
@@ -18,17 +18,17 @@
 pytorch-lightning<1.10.0,>=1.9.0
 text-unidecode<1.4,>=1.3
 torchmetrics<0.12.0,>=0.11.0
 transformers<4.27.0,>=4.23.0
 nptyping<2.5.0,>=1.4.4
 omegaconf<2.3.0,>=2.1.1
 sentencepiece<0.2.0,>=0.1.95
-autogluon.core[raytune]==0.7.0b20230405
-autogluon.features==0.7.0b20230405
-autogluon.common==0.7.0b20230405
+autogluon.core[raytune]==0.7.0b20230406
+autogluon.features==0.7.0b20230406
+autogluon.common==0.7.0b20230406
 pytorch-metric-learning<2.0,>=1.3.0
 nlpaug<1.2.0,>=1.1.10
 nltk<4.0.0,>=3.4.5
 openmim<0.4.0,>0.1.5
 defusedxml<0.7.2,>=0.7.1
 jinja2<3.2,>=3.0.3
 tensorboard<3,>=2.9
```

