# Comparing `tmp/functional-cat-0.2.0.tar.gz` & `tmp/functional-cat-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "functional-cat-0.2.0.tar", last modified: Wed Feb  1 21:49:58 2023, max compression
+gzip compressed data, was "functional-cat-0.3.0.tar", last modified: Thu Apr  6 16:17:15 2023, max compression
```

## Comparing `functional-cat-0.2.0.tar` & `functional-cat-0.3.0.tar`

### file list

```diff
@@ -1,88 +1,96 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.184991 functional-cat-0.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-02-01 21:49:47.000000 functional-cat-0.2.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-02-01 21:49:58.184991 functional-cat-0.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-02-01 21:49:47.000000 functional-cat-0.2.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6527 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/data_types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/glip/
--rw-r--r--   0 runner    (1001) docker     (123)      320 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/glip/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2510 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/glip/glip.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/mmcv/
--rw-r--r--   0 runner    (1001) docker     (123)      345 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      391 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/icdar2017.py
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/synthtext.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r18_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r50dcnv2_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnetpp_r50dcnv2_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/drrg_r50_fpn_unet.py
--rw-r--r--   0 runner    (1001) docker     (123)      999 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50dcnv2_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     4504 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem.py
--rw-r--r--   0 runner    (1001) docker     (123)     4525 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem_poly.py
--rw-r--r--   0 runner    (1001) docker     (123)     1421 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r18_fpem_ffm.py
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r50_fpem_ffm.py
--rw-r--r--   0 runner    (1001) docker     (123)     1549 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/psenet_r50_fpnf.py
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/textsnake_r50_fpn_unet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3227 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/dbnet_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     2275 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/drrg_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     4048 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/fcenet_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     1927 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/maskrcnn_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     5668 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/panet_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/psenet_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/textsnake_pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adadelta_18e.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adadelta_5e.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_600e.py
--rw-r--r--   0 runner    (1001) docker     (123)      323 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_12e.py
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_20e.py
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_5e.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_600e.py
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_6e.py
--rw-r--r--   0 runner    (1001) docker     (123)      332 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_100k_iters.py
--rw-r--r--   0 runner    (1001) docker     (123)      329 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_1200e.py
--rw-r--r--   0 runner    (1001) docker     (123)      327 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_1500e.py
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_160e.py
--rw-r--r--   0 runner    (1001) docker     (123)      304 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_600e.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/psenet/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/psenet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1045 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/psenet/psenet_r50_fpnf_600e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     2816 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/mmcv/mmocr.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.180991 functional-cat-0.2.0/functional_cat/funcs/onnx/
--rw-r--r--   0 runner    (1001) docker     (123)      429 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/onnx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4964 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/onnx/tiny_yolov3.py
--rw-r--r--   0 runner    (1001) docker     (123)     9798 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/onnx/yolov4.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.184991 functional-cat-0.2.0/functional_cat/funcs/torchvision/
--rw-r--r--   0 runner    (1001) docker     (123)      557 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/torchvision/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6672 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/funcs/torchvision/detection.py
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     3552 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/io.py
--rw-r--r--   0 runner    (1001) docker     (123)     5919 2023-02-01 21:49:47.000000 functional-cat-0.2.0/functional_cat/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 21:49:58.176991 functional-cat-0.2.0/functional_cat.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-02-01 21:49:58.000000 functional-cat-0.2.0/functional_cat.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4031 2023-02-01 21:49:58.000000 functional-cat-0.2.0/functional_cat.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-01 21:49:58.000000 functional-cat-0.2.0/functional_cat.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 21:49:58.000000 functional-cat-0.2.0/functional_cat.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-02-01 21:49:58.000000 functional-cat-0.2.0/functional_cat.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      856 2023-02-01 21:49:47.000000 functional-cat-0.2.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-01 21:49:58.184991 functional-cat-0.2.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 21:49:47.000000 functional-cat-0.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1054 2023-04-06 16:17:06.000000 functional-cat-0.3.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1753 2023-04-06 16:17:15.193386 functional-cat-0.3.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-04-06 16:17:06.000000 functional-cat-0.3.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6862 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/data_types.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/dlib/
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/dlib/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/dlib/detection.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/glip/
+-rw-r--r--   0 runner    (1001) docker     (123)      320 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/glip/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2874 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/glip/glip.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/mmcv/
+-rw-r--r--   0 runner    (1001) docker     (123)      345 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/default_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      391 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/icdar2017.py
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_datasets/synthtext.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.189386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      728 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r18_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r50dcnv2_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnetpp_r50dcnv2_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/drrg_r50_fpn_unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      999 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50dcnv2_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4504 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4525 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem_poly.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1421 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r18_fpem_ffm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r50_fpem_ffm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1549 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/psenet_r50_fpnf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/textsnake_r50_fpn_unet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.189386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3227 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/dbnet_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2275 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/drrg_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4048 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/fcenet_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1927 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/maskrcnn_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5668 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/panet_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/psenet_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/textsnake_pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.189386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adadelta_18e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adadelta_5e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_600e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      323 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_12e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_20e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_5e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_600e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_adam_step_6e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_100k_iters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      329 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_1200e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      327 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_1500e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_160e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      304 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/schedules/schedule_sgd_600e.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/psenet/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/psenet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1045 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/psenet/psenet_r50_fpnf_600e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2816 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/mmcv/mmocr.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/functional_cat/funcs/onnx/
+-rw-r--r--   0 runner    (1001) docker     (123)      429 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/onnx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4964 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/onnx/tiny_yolov3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9798 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/onnx/yolov4.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/functional_cat/funcs/torchvision/
+-rw-r--r--   0 runner    (1001) docker     (123)      557 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/torchvision/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6672 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/funcs/torchvision/detection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2749 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3552 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6517 2023-04-06 16:17:06.000000 functional-cat-0.3.0/functional_cat/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.185386 functional-cat-0.3.0/functional_cat.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1753 2023-04-06 16:17:15.000000 functional-cat-0.3.0/functional_cat.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4191 2023-04-06 16:17:15.000000 functional-cat-0.3.0/functional_cat.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:17:15.000000 functional-cat-0.3.0/functional_cat.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 16:17:15.000000 functional-cat-0.3.0/functional_cat.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 16:17:15.000000 functional-cat-0.3.0/functional_cat.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      872 2023-04-06 16:17:06.000000 functional-cat-0.3.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 16:17:15.193386 functional-cat-0.3.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-04-06 16:17:06.000000 functional-cat-0.3.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:17:15.193386 functional-cat-0.3.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      925 2023-04-06 16:17:06.000000 functional-cat-0.3.0/tests/test_dlib.py
+-rw-r--r--   0 runner    (1001) docker     (123)      619 2023-04-06 16:17:06.000000 functional-cat-0.3.0/tests/test_mmcv.py
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-04-06 16:17:06.000000 functional-cat-0.3.0/tests/test_onnx.py
+-rw-r--r--   0 runner    (1001) docker     (123)      662 2023-04-06 16:17:06.000000 functional-cat-0.3.0/tests/test_torchvision.py
```

### Comparing `functional-cat-0.2.0/LICENSE` & `functional-cat-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/PKG-INFO` & `functional-cat-0.3.0/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: functional-cat
-Version: 0.2.0
+Version: 0.3.0
 Summary: Catalog of functions
 License: Copyright 2022 Eric O. Korman
         
         Permission is hereby granted, free of charge, to any person obtaining
         a copy of this software and associated documentation files (the
         "Software"), to deal in the Software without restriction, including
         without limitation the rights to use, copy, modify, merge, publish,
@@ -28,14 +28,15 @@
 Provides-Extra: torch
 Provides-Extra: onnx
 Provides-Extra: onnx-cpu
 Provides-Extra: onnx-gpu
 Provides-Extra: mmcv
 Provides-Extra: catalog
 Provides-Extra: glip
+Provides-Extra: dlib
 Provides-Extra: test
 License-File: LICENSE
 
 # functional cat
 
 A catalog and Python library of easy-to-use deep learning models.
```

### Comparing `functional-cat-0.2.0/functional_cat/data_types.py` & `functional-cat-0.3.0/functional_cat/data_types.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import math
 from dataclasses import dataclass
-from typing import List, Union
+from typing import Dict, List, Tuple, Union
 
 import numpy as np
 from PIL import Image, ImageDraw, ImageFont
 
 MaskType = List[List[float]]
 ImageInput = List[Image.Image]
 NumberType = Union[float, int]
@@ -182,48 +182,57 @@
 
 
 @dataclass
 class Keypoint:
     class_label: str
     x: float
     y: float
-    score: float
-    visible: bool
+    score: float = None
+    visible: bool = None
 
     def draw_on_image(
         self,
         img: Image.Image,
         inplace: bool = False,
         radius: int = 2,
+        color: Tuple[int, int, int] = (255, 0, 0),
     ) -> Image.Image:
         img = img if inplace else img.copy()
         img_draw = ImageDraw.Draw(img)
         img_draw.ellipse(
             (
                 self.x - radius,
                 self.y - radius,
                 self.x + radius,
                 self.y + radius,
             ),
-            fill=(255, 0, 0),
+            fill=color,
         )
 
         return img
 
 
 @dataclass
 class DetectionWithKeypoints(Detection):
     keypoints: List[Keypoint]
 
     def draw_on_image(
-        self, img: Image.Image, inplace: bool = False
+        self,
+        img: Image.Image,
+        inplace: bool = False,
+        color_map: Dict[str, Tuple[int, int, int]] = None,
     ) -> Image.Image:
         img = super().draw_on_image(img=img, inplace=inplace)
         for keypoint in self.keypoints:
-            img = keypoint.draw_on_image(img)
+            if color_map is not None:
+                img = keypoint.draw_on_image(
+                    img, color=color_map[keypoint.class_label]
+                )
+            else:
+                img = keypoint.draw_on_image(img)
 
         return img
 
 
 def _get_font(font_size: int):
     try:
         font = ImageFont.truetype("arial.ttf", font_size)
```

### Comparing `functional-cat-0.2.0/functional_cat/funcs/glip/glip.py` & `functional-cat-0.3.0/functional_cat/funcs/glip/glip.py`

 * *Files 16% similar despite different names*

```diff
@@ -20,15 +20,15 @@
             md5="2befd9660fe12bb69d02e1716bc9ac34",
         ),
     }
 
     def __init__(
         self,
         model_name: str,
-        class_labels: List[str],
+        class_labels: List[str] = None,
         min_image_size: int = 800,
     ):
         if model_name not in self.MODEL_NAME_TO_WEIGHT.keys():
             raise ValueError(
                 f"model_name must be one of {list(self.MODEL_NAME_TO_WEIGHT.keys())}"
             )
 
@@ -47,29 +47,41 @@
         self._class_labels = class_labels
 
     @property
     def class_labels(self) -> List[str]:
         return self._class_labels
 
     def __call__(
-        self, imgs: ImageInput, score_thres: float
+        self,
+        imgs: ImageInput,
+        score_thres: float,
+        class_labels: List[str] = None,
     ) -> List[List[Detection]]:
+        class_labels = class_labels or self.class_labels
+        if class_labels is None:
+            raise RuntimeError(
+                "`class_labels` must be passed since they were not set when invoking the model."
+            )
         box_lists = self.glip_model(
-            imgs, class_labels=self.class_labels, thresh=score_thres
+            imgs, class_labels=class_labels, thresh=score_thres
         )
         return [
-            self._box_list_to_detections(box_list) for box_list in box_lists
+            self._box_list_to_detections(box_list, class_labels)
+            for box_list in box_lists
         ]
 
-    def _box_list_to_detections(self, box_list: BoxList) -> List[Detection]:
+    @staticmethod
+    def _box_list_to_detections(
+        box_list: BoxList, class_labels: List[str]
+    ) -> List[Detection]:
         bboxes = box_list.bbox.tolist()
         scores = box_list.get_field("scores")
         labels = box_list.get_field("labels")
 
         return [
             Detection(
                 boundary=BoundingPolygon.from_bbox(*bbox),
-                class_label=self.class_labels[label - 1],
+                class_label=class_labels[label - 1],
                 score=score.item(),
             )
             for bbox, score, label in zip(bboxes, scores, labels)
         ]
```

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r18_fpnc.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r18_fpnc.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r50dcnv2_fpnc.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnet_r50dcnv2_fpnc.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnetpp_r50dcnv2_fpnc.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/dbnetpp_r50dcnv2_fpnc.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/drrg_r50_fpn_unet.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/drrg_r50_fpn_unet.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50_fpn.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50_fpn.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50dcnv2_fpn.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/fcenet_r50dcnv2_fpn.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem_poly.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/ocr_mask_rcnn_r50_fpn_ohem_poly.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r18_fpem_ffm.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r18_fpem_ffm.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r50_fpem_ffm.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/panet_r50_fpem_ffm.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/psenet_r50_fpnf.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/psenet_r50_fpnf.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_models/textsnake_r50_fpn_unet.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_models/textsnake_r50_fpn_unet.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/dbnet_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/dbnet_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/drrg_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/drrg_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/fcenet_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/fcenet_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/maskrcnn_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/maskrcnn_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/panet_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/panet_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/psenet_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/psenet_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/textsnake_pipeline.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/_base_/det_pipelines/textsnake_pipeline.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/configs/textdet/psenet/psenet_r50_fpnf_600e_icdar2015.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/configs/textdet/psenet/psenet_r50_fpnf_600e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/mmcv/mmocr.py` & `functional-cat-0.3.0/functional_cat/funcs/mmcv/mmocr.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/onnx/tiny_yolov3.py` & `functional-cat-0.3.0/functional_cat/funcs/onnx/tiny_yolov3.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/onnx/yolov4.py` & `functional-cat-0.3.0/functional_cat/funcs/onnx/yolov4.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/torchvision/__init__.py` & `functional-cat-0.3.0/functional_cat/funcs/torchvision/__init__.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/funcs/torchvision/detection.py` & `functional-cat-0.3.0/functional_cat/funcs/torchvision/detection.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/interfaces.py` & `functional-cat-0.3.0/functional_cat/interfaces.py`

 * *Files 19% similar despite different names*

```diff
@@ -9,14 +9,39 @@
     DetectionWithKeypoints,
     ImageInput,
     InstanceSegmentation,
 )
 
 __all__ = ["ObjectDetector", "InstanceSegmentationModel", "KeyPointDetector"]
 
+colors = [
+    "#e6194b",
+    "#3cb44b",
+    "#ffe119",
+    "#4363d8",
+    "#f58231",
+    "#911eb4",
+    "#46f0f0",
+    "#f032e6",
+    "#bcf60c",
+    "#fabebe",
+    "#008080",
+    "#e6beff",
+    "#9a6324",
+    "#fffac8",
+    "#800000",
+    "#aaffc3",
+    "#808000",
+    "#ffd8b1",
+    "#000075",
+    "#808080",
+    "#ffffff",
+    "#000000",
+]
+
 
 class Task(Enum):
     OBJECT_DETECTION = "Object Detection"
     INSTANCE_SEGMENTATION = "Instance Segmentation"
     KEYPOINT_DETECTION = "KeyPoint Detection"
 
 
@@ -36,18 +61,18 @@
     def __call__(
         self, imgs: ImageInput, score_thres: float
     ) -> List[List[Detection]]:
         pass
 
     @staticmethod
     def draw_output_on_img(
-        img: Image.Image, dets: List[Detection]
+        img: Image.Image, dets: List[Detection], **kwargs
     ) -> Image.Image:
         for i, det in enumerate(dets):
-            img = det.draw_on_image(img, inplace=i != 0)
+            img = det.draw_on_image(img, inplace=i != 0, **kwargs)
         return img
 
 
 class InstanceSegmentationModel(ObjectDetector):
     task = Task.INSTANCE_SEGMENTATION
 
     @abstractmethod
@@ -77,7 +102,13 @@
     def __call__(self, imgs: ImageInput) -> List[List[DetectionWithKeypoints]]:
         pass
 
     @property
     @abstractmethod
     def key_point_labels(self) -> List[str]:
         pass
+
+    def draw_output_on_img(
+        self, img: Image.Image, dets: List[DetectionWithKeypoints]
+    ) -> Image.Image:
+        color_map = {k: colors[i] for i, k in enumerate(self.key_point_labels)}
+        return super().draw_output_on_img(img, dets, color_map=color_map)
```

### Comparing `functional-cat-0.2.0/functional_cat/io.py` & `functional-cat-0.3.0/functional_cat/io.py`

 * *Files identical despite different names*

### Comparing `functional-cat-0.2.0/functional_cat/registry.py` & `functional-cat-0.3.0/functional_cat/registry.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 from functional_cat.interfaces import Task
 
 
 class Framework(Enum):
     PYTORCH = "PyTorch"
     ONNX = "ONNX"
     MMCV = "MMCV"
+    DLIB = "dlib"
 
 
 @dataclass
 class ModelMeta:
     name: str
     class_: type
     constructor_args: dict
@@ -170,7 +171,27 @@
             cpu_support=False,
             gpu_support=True,
             example_img=example_img,
             colab_link="https://colab.research.google.com/drive/1GKMq4Z-7tD3cNWubWCqMuQ81D-nAFIaD",
         )
         for name in ["GLIP-T", "GLIP-L"]
     ]
+
+
+def create_dlib_model_metas(
+    example_img: Image.Image = None,
+) -> List[ModelMeta]:
+    from functional_cat.funcs.dlib import DLibFaceDetector
+
+    return [
+        ModelMeta(
+            name="cnn_face_detection_model_v1",
+            class_=DLibFaceDetector,
+            constructor_args={},
+            description="cnn_face_detection_model_v1 from dlib",
+            framework=Framework.DLIB,
+            install_snippet="pip install functional-cat[dlib]",
+            cpu_support=True,
+            gpu_support=True,
+            example_img=example_img,
+        )
+    ]
```

### Comparing `functional-cat-0.2.0/functional_cat.egg-info/PKG-INFO` & `functional-cat-0.3.0/functional_cat.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: functional-cat
-Version: 0.2.0
+Version: 0.3.0
 Summary: Catalog of functions
 License: Copyright 2022 Eric O. Korman
         
         Permission is hereby granted, free of charge, to any person obtaining
         a copy of this software and associated documentation files (the
         "Software"), to deal in the Software without restriction, including
         without limitation the rights to use, copy, modify, merge, publish,
@@ -28,14 +28,15 @@
 Provides-Extra: torch
 Provides-Extra: onnx
 Provides-Extra: onnx-cpu
 Provides-Extra: onnx-gpu
 Provides-Extra: mmcv
 Provides-Extra: catalog
 Provides-Extra: glip
+Provides-Extra: dlib
 Provides-Extra: test
 License-File: LICENSE
 
 # functional cat
 
 A catalog and Python library of easy-to-use deep learning models.
```

### Comparing `functional-cat-0.2.0/functional_cat.egg-info/SOURCES.txt` & `functional-cat-0.3.0/functional_cat.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -9,14 +9,16 @@
 functional_cat/registry.py
 functional_cat.egg-info/PKG-INFO
 functional_cat.egg-info/SOURCES.txt
 functional_cat.egg-info/dependency_links.txt
 functional_cat.egg-info/requires.txt
 functional_cat.egg-info/top_level.txt
 functional_cat/funcs/__init__.py
+functional_cat/funcs/dlib/__init__.py
+functional_cat/funcs/dlib/detection.py
 functional_cat/funcs/glip/__init__.py
 functional_cat/funcs/glip/glip.py
 functional_cat/funcs/mmcv/__init__.py
 functional_cat/funcs/mmcv/mmocr.py
 functional_cat/funcs/mmcv/configs/__init__.py
 functional_cat/funcs/mmcv/configs/_base_/__init__.py
 functional_cat/funcs/mmcv/configs/_base_/default_runtime.py
@@ -63,8 +65,12 @@
 functional_cat/funcs/mmcv/configs/textdet/__init__.py
 functional_cat/funcs/mmcv/configs/textdet/psenet/__init__.py
 functional_cat/funcs/mmcv/configs/textdet/psenet/psenet_r50_fpnf_600e_icdar2015.py
 functional_cat/funcs/onnx/__init__.py
 functional_cat/funcs/onnx/tiny_yolov3.py
 functional_cat/funcs/onnx/yolov4.py
 functional_cat/funcs/torchvision/__init__.py
-functional_cat/funcs/torchvision/detection.py
+functional_cat/funcs/torchvision/detection.py
+tests/test_dlib.py
+tests/test_mmcv.py
+tests/test_onnx.py
+tests/test_torchvision.py
```

### Comparing `functional-cat-0.2.0/pyproject.toml` & `functional-cat-0.3.0/pyproject.toml`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "functional-cat"
-version = "0.2.0"
+version = "0.3.0"
 description = "Catalog of functions"
 readme = "README.md"
 requires-python = ">=3.7"
 license = {file = "LICENSE"}
 dependencies = ["requests", "Pillow >= 9.1.0", "tqdm", "numpy >= 1.23"]
 
 [build-system]
@@ -18,14 +18,15 @@
 ]
 onnx = ["onnxruntime >= 1.11", "scipy"]
 onnx-cpu = ["onnxruntime >= 1.11"]
 onnx-gpu = ["onnxruntime-gpu >= 1.11"]
 mmcv = [] # this is installed separately
 catalog = ["boto3", "python-dotenv"]
 glip = ["glip-object-detection"]
+dlib = ["dlib"]
 test = ["pytest"]
 
 [tool.black]
 line-length = 79
 
 [tool.isort]
 line_length = 79
```

