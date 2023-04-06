# Comparing `tmp/ultralytics-8.0.8.tar.gz` & `tmp/ultralytics-8.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ultralytics-8.0.8.tar", last modified: Tue Jan 17 22:04:36 2023, max compression
+gzip compressed data, was "ultralytics-8.0.9.tar", last modified: Wed Jan 18 08:36:22 2023, max compression
```

## Comparing `ultralytics-8.0.8.tar` & `ultralytics-8.0.9.tar`

### file list

```diff
@@ -1,140 +1,140 @@
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.216109 ultralytics-8.0.8/
--rw-r--r--   0 glennjocher   (501) staff       (20)     5613 2023-01-17 13:35:22.000000 ultralytics-8.0.8/CONTRIBUTING.md
--rw-r--r--   0 glennjocher   (501) staff       (20)    35149 2023-01-17 13:35:22.000000 ultralytics-8.0.8/LICENSE
--rw-r--r--   0 glennjocher   (501) staff       (20)      140 2023-01-17 13:35:22.000000 ultralytics-8.0.8/MANIFEST.in
--rw-r--r--   0 glennjocher   (501) staff       (20)    24011 2023-01-17 22:04:36.216193 ultralytics-8.0.8/PKG-INFO
--rw-r--r--   0 glennjocher   (501) staff       (20)    22623 2023-01-17 22:00:59.000000 ultralytics-8.0.8/README.md
--rw-r--r--   0 glennjocher   (501) staff       (20)    20431 2023-01-17 22:00:59.000000 ultralytics-8.0.8/README.zh-CN.md
--rw-r--r--   0 glennjocher   (501) staff       (20)     1189 2023-01-17 21:37:01.000000 ultralytics-8.0.8/requirements.txt
--rw-r--r--   0 glennjocher   (501) staff       (20)      702 2023-01-17 22:04:36.216481 ultralytics-8.0.8/setup.cfg
--rw-r--r--   0 glennjocher   (501) staff       (20)     2520 2023-01-17 22:00:59.000000 ultralytics-8.0.8/setup.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.200539 ultralytics-8.0.8/ultralytics/
--rw-r--r--   0 glennjocher   (501) staff       (20)      271 2023-01-17 22:04:24.000000 ultralytics-8.0.8/ultralytics/__init__.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.201877 ultralytics-8.0.8/ultralytics/hub/
--rw-r--r--   0 glennjocher   (501) staff       (20)     5215 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/hub/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2483 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/hub/auth.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     4655 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/hub/session.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     6660 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/hub/utils.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.197780 ultralytics-8.0.8/ultralytics/models/
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.202398 ultralytics-8.0.8/ultralytics/models/v3/
--rw-r--r--   0 glennjocher   (501) staff       (20)     1434 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v3/yolov3-spp.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1135 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v3/yolov3-tiny.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1425 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v3/yolov3.yaml
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.203312 ultralytics-8.0.8/ultralytics/models/v5/
--rw-r--r--   0 glennjocher   (501) staff       (20)     1267 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v5/yolov5l.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v5/yolov5m.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v5/yolov5n.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1270 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v5/yolov5s.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v5/yolov5x.yaml
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.204162 ultralytics-8.0.8/ultralytics/models/v8/
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.204999 ultralytics-8.0.8/ultralytics/models/v8/cls/
--rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8l-cls.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8m-cls.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8n-cls.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8s-cls.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8x-cls.yaml
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.205793 ultralytics-8.0.8/ultralytics/models/v8/seg/
--rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8l-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8m-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1213 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8n-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1213 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8s-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8x-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8l.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8m.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1203 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8n.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1203 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8s.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8x.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1569 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/models/v8/yolov8x6.yaml
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.206610 ultralytics-8.0.8/ultralytics/nn/
--rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/nn/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    20525 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/nn/autobackend.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    11853 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/nn/autoshape.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    18358 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/nn/modules.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    18651 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/nn/tasks.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.206912 ultralytics-8.0.8/ultralytics/yolo/
--rw-r--r--   0 glennjocher   (501) staff       (20)       59 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     3869 2023-01-17 22:00:59.000000 ultralytics-8.0.8/ultralytics/yolo/cli.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.207280 ultralytics-8.0.8/ultralytics/yolo/configs/
--rw-r--r--   0 glennjocher   (501) staff       (20)     1212 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/configs/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     5470 2023-01-17 14:57:21.000000 ultralytics-8.0.8/ultralytics/yolo/configs/default.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     3760 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/configs/hydra_patch.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.208248 ultralytics-8.0.8/ultralytics/yolo/data/
--rw-r--r--   0 glennjocher   (501) staff       (20)      262 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    30711 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/augment.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     8547 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/base.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     4967 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/build.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.208876 ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/
--rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    13173 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/stream_loaders.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    17247 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/v5augmentations.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    55344 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/v5loader.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     9543 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataset.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     1330 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/dataset_wrappers.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.210768 ultralytics-8.0.8/ultralytics/yolo/data/datasets/
--rw-r--r--   0 glennjocher   (501) staff       (20)     2728 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/Argoverse.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1880 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/GlobalWheat2020.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)    18866 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/ImageNet.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     9200 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/Objects365.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     2336 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/SKU-110K.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     3488 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/VOC.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     2966 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/VisDrone.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     2485 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1862 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco128-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1846 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco128.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1797 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco8-seg.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     1777 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco8.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)     5165 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/datasets/xView.yaml
--rw-r--r--   0 glennjocher   (501) staff       (20)    13304 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/data/utils.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.211662 ultralytics-8.0.8/ultralytics/yolo/engine/
--rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    40297 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/exporter.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     9078 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/model.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    13261 2023-01-17 22:00:59.000000 ultralytics-8.0.8/ultralytics/yolo/engine/predictor.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     9580 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/results.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    25807 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/trainer.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     8999 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/engine/validator.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.213313 ultralytics-8.0.8/ultralytics/yolo/utils/
--rw-r--r--   0 glennjocher   (501) staff       (20)    15731 2023-01-17 22:04:24.000000 ultralytics-8.0.8/ultralytics/yolo/utils/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     3010 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/autobatch.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.214119 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/
--rw-r--r--   0 glennjocher   (501) staff       (20)       63 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     3182 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/base.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     1872 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/clearml.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     1596 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/comet.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2584 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/hub.py
--rw-r--r--   0 glennjocher   (501) staff       (20)      723 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/tensorboard.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    10105 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/checks.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2278 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/dist.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     6625 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/downloads.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     3818 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/files.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    11360 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/instance.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2261 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/loss.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    22673 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/metrics.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    28031 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/ops.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    14641 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/plotting.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     9580 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/tal.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    15783 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/utils/torch_utils.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.214240 ultralytics-8.0.8/ultralytics/yolo/v8/
--rw-r--r--   0 glennjocher   (501) staff       (20)      220 2023-01-17 22:00:59.000000 ultralytics-8.0.8/ultralytics/yolo/v8/__init__.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.214876 ultralytics-8.0.8/ultralytics/yolo/v8/classify/
--rw-r--r--   0 glennjocher   (501) staff       (20)      274 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/classify/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2832 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/classify/predict.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     6144 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/classify/train.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     2126 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/classify/val.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.215403 ultralytics-8.0.8/ultralytics/yolo/v8/detect/
--rw-r--r--   0 glennjocher   (501) staff       (20)      175 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/detect/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     3929 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/detect/predict.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     9553 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/detect/train.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    11868 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/detect/val.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.215973 ultralytics-8.0.8/ultralytics/yolo/v8/segment/
--rw-r--r--   0 glennjocher   (501) staff       (20)      184 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/segment/__init__.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     4710 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/segment/predict.py
--rw-r--r--   0 glennjocher   (501) staff       (20)     6948 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/segment/train.py
--rw-r--r--   0 glennjocher   (501) staff       (20)    12343 2023-01-17 13:35:22.000000 ultralytics-8.0.8/ultralytics/yolo/v8/segment/val.py
-drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-17 22:04:36.201298 ultralytics-8.0.8/ultralytics.egg-info/
--rw-r--r--   0 glennjocher   (501) staff       (20)    24011 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/PKG-INFO
--rw-r--r--   0 glennjocher   (501) staff       (20)     4111 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/SOURCES.txt
--rw-r--r--   0 glennjocher   (501) staff       (20)        1 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/dependency_links.txt
--rw-r--r--   0 glennjocher   (501) staff       (20)      103 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/entry_points.txt
--rw-r--r--   0 glennjocher   (501) staff       (20)      372 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/requires.txt
--rw-r--r--   0 glennjocher   (501) staff       (20)       12 2023-01-17 22:04:36.000000 ultralytics-8.0.8/ultralytics.egg-info/top_level.txt
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.378065 ultralytics-8.0.9/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     5613 2023-01-17 13:35:22.000000 ultralytics-8.0.9/CONTRIBUTING.md
+-rw-r--r--   0 glennjocher   (501) staff       (20)    35149 2023-01-17 13:35:22.000000 ultralytics-8.0.9/LICENSE
+-rw-r--r--   0 glennjocher   (501) staff       (20)      140 2023-01-17 13:35:22.000000 ultralytics-8.0.9/MANIFEST.in
+-rw-r--r--   0 glennjocher   (501) staff       (20)    23762 2023-01-18 08:36:22.378177 ultralytics-8.0.9/PKG-INFO
+-rw-r--r--   0 glennjocher   (501) staff       (20)    22374 2023-01-18 08:17:00.000000 ultralytics-8.0.9/README.md
+-rw-r--r--   0 glennjocher   (501) staff       (20)    20431 2023-01-17 22:00:59.000000 ultralytics-8.0.9/README.zh-CN.md
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1189 2023-01-17 21:37:01.000000 ultralytics-8.0.9/requirements.txt
+-rw-r--r--   0 glennjocher   (501) staff       (20)      702 2023-01-18 08:36:22.378608 ultralytics-8.0.9/setup.cfg
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2520 2023-01-17 22:00:59.000000 ultralytics-8.0.9/setup.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.354642 ultralytics-8.0.9/ultralytics/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      299 2023-01-18 08:33:56.000000 ultralytics-8.0.9/ultralytics/__init__.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.356672 ultralytics-8.0.9/ultralytics/hub/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     4465 2023-01-18 07:33:38.000000 ultralytics-8.0.9/ultralytics/hub/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2483 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/hub/auth.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     4655 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/hub/session.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     6660 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/hub/utils.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.350419 ultralytics-8.0.9/ultralytics/models/
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.357623 ultralytics-8.0.9/ultralytics/models/v3/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1434 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v3/yolov3-spp.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1135 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v3/yolov3-tiny.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1425 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v3/yolov3.yaml
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.358685 ultralytics-8.0.9/ultralytics/models/v5/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1267 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v5/yolov5l.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v5/yolov5m.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v5/yolov5n.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1270 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v5/yolov5s.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1269 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v5/yolov5x.yaml
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.360012 ultralytics-8.0.9/ultralytics/models/v8/
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.361106 ultralytics-8.0.9/ultralytics/models/v8/cls/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8l-cls.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8m-cls.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8n-cls.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8s-cls.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)      629 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8x-cls.yaml
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.362256 ultralytics-8.0.9/ultralytics/models/v8/seg/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8l-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8m-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1213 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8n-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1213 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8s-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1209 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8x-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8l.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8m.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1203 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8n.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1203 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8s.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1199 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8x.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1569 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/models/v8/yolov8x6.yaml
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.363349 ultralytics-8.0.9/ultralytics/nn/
+-rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/nn/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    20525 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/nn/autobackend.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    11853 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/nn/autoshape.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    18358 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/nn/modules.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    18651 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/nn/tasks.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.363820 ultralytics-8.0.9/ultralytics/yolo/
+-rw-r--r--   0 glennjocher   (501) staff       (20)       59 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     5956 2023-01-18 08:03:25.000000 ultralytics-8.0.9/ultralytics/yolo/cli.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.364604 ultralytics-8.0.9/ultralytics/yolo/configs/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1212 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/configs/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     5470 2023-01-17 14:57:21.000000 ultralytics-8.0.9/ultralytics/yolo/configs/default.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3760 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/configs/hydra_patch.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.366253 ultralytics-8.0.9/ultralytics/yolo/data/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      262 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    30711 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/augment.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     8547 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/base.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     4967 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/build.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.367178 ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/
+-rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    13173 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/stream_loaders.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    17247 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/v5augmentations.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    55344 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/v5loader.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9605 2023-01-18 07:19:48.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataset.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1330 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/dataset_wrappers.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.370185 ultralytics-8.0.9/ultralytics/yolo/data/datasets/
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2728 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/Argoverse.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1880 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/GlobalWheat2020.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)    18866 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/ImageNet.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9200 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/Objects365.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2336 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/SKU-110K.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3488 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/VOC.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2966 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/VisDrone.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2485 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1862 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco128-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1846 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco128.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1797 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco8-seg.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1777 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco8.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)     5165 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/datasets/xView.yaml
+-rw-r--r--   0 glennjocher   (501) staff       (20)    13304 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/data/utils.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.371597 ultralytics-8.0.9/ultralytics/yolo/engine/
+-rw-r--r--   0 glennjocher   (501) staff       (20)        0 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    40297 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/exporter.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9078 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/model.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    13261 2023-01-17 22:00:59.000000 ultralytics-8.0.9/ultralytics/yolo/engine/predictor.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9580 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/results.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    25807 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/trainer.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     8999 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/engine/validator.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.374329 ultralytics-8.0.9/ultralytics/yolo/utils/
+-rw-r--r--   0 glennjocher   (501) staff       (20)    15731 2023-01-18 08:33:56.000000 ultralytics-8.0.9/ultralytics/yolo/utils/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3010 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/autobatch.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.375451 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/
+-rw-r--r--   0 glennjocher   (501) staff       (20)       63 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3182 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/base.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1872 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/clearml.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     1596 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/comet.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2584 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/hub.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)      723 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/tensorboard.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    10817 2023-01-18 08:21:26.000000 ultralytics-8.0.9/ultralytics/yolo/utils/checks.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2278 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/dist.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     6625 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/downloads.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3818 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/files.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    11360 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/instance.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2261 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/loss.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    22673 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/metrics.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    28031 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/ops.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    14641 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/plotting.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9580 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/tal.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    15783 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/utils/torch_utils.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.375655 ultralytics-8.0.9/ultralytics/yolo/v8/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      220 2023-01-17 22:00:59.000000 ultralytics-8.0.9/ultralytics/yolo/v8/__init__.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.376424 ultralytics-8.0.9/ultralytics/yolo/v8/classify/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      274 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/classify/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2832 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/classify/predict.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     6144 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/classify/train.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     2126 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/classify/val.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.377152 ultralytics-8.0.9/ultralytics/yolo/v8/detect/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      175 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/detect/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     3929 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/detect/predict.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     9553 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/detect/train.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    11868 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/detect/val.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.377898 ultralytics-8.0.9/ultralytics/yolo/v8/segment/
+-rw-r--r--   0 glennjocher   (501) staff       (20)      184 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/segment/__init__.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     4710 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/segment/predict.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)     6948 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/segment/train.py
+-rw-r--r--   0 glennjocher   (501) staff       (20)    12343 2023-01-17 13:35:22.000000 ultralytics-8.0.9/ultralytics/yolo/v8/segment/val.py
+drwxr-xr-x   0 glennjocher   (501) staff       (20)        0 2023-01-18 08:36:22.355654 ultralytics-8.0.9/ultralytics.egg-info/
+-rw-r--r--   0 glennjocher   (501) staff       (20)    23762 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/PKG-INFO
+-rw-r--r--   0 glennjocher   (501) staff       (20)     4111 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/SOURCES.txt
+-rw-r--r--   0 glennjocher   (501) staff       (20)        1 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/dependency_links.txt
+-rw-r--r--   0 glennjocher   (501) staff       (20)      103 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/entry_points.txt
+-rw-r--r--   0 glennjocher   (501) staff       (20)      372 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/requires.txt
+-rw-r--r--   0 glennjocher   (501) staff       (20)       12 2023-01-18 08:36:22.000000 ultralytics-8.0.9/ultralytics.egg-info/top_level.txt
```

### Comparing `ultralytics-8.0.8/CONTRIBUTING.md` & `ultralytics-8.0.9/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/LICENSE` & `ultralytics-8.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/PKG-INFO` & `ultralytics-8.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ultralytics
-Version: 8.0.8
+Version: 8.0.9
 Summary: Ultralytics YOLOv8
 Home-page: https://github.com/ultralytics/ultralytics
 Author: Ultralytics
 Author-email: hello@ultralytics.com
 License: GPL-3.0
 Project-URL: Bug Reports, https://github.com/ultralytics/ultralytics/issues
 Project-URL: Funding, https://ultralytics.com
@@ -84,28 +84,34 @@
   </div>
 </div>
 
 ## <div align="center">Ultralytics Live Session</div>
 
 <div align="center">
 
-[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and ease of use make it a top choice for professionals and researchers alike.
+[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into
+the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object
+detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and
+ease of use make it a top choice for professionals and researchers alike.
+
+In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the
+opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared
+with any questions you may have.
 
-In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared with any questions you may have.
-
-To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your notifications!
+To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your
+notifications!
 
 <a align="center" href="https://youtu.be/IPcpYO5ITa8" target="_blank">
 <img width="80%" src="https://user-images.githubusercontent.com/107626595/212887899-e94b006c-5192-40fa-8b24-7b5428e065e8.png"></a>
 </div>
 
 ## <div align="center">Documentation</div>
 
-See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for full
-documentation on training, validation, prediction and deployment.
+See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for
+full documentation on training, validation, prediction and deployment.
 
 <details open>
 <summary>Install</summary>
 
 Pip install the ultralytics package including
 all [requirements.txt](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) in a
 [**3.10>=Python>=3.7**](https://www.python.org/) environment, including
@@ -116,30 +122,26 @@
 ```
 
 </details>
 
 <details open>
 <summary>Usage</summary>
 
+#### CLI
+
 YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo` command:
 
 ```bash
 yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
 ```
 
-`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list
-of available `yolo` [arguments](https://docs.ultralytics.com/config/) in the
-YOLOv8 [Docs](https://docs.ultralytics.com).
+`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8
+[CLI Docs](https://docs.ultralytics.com/cli) for examples.
 
-```bash
-yolo task=detect    mode=train    model=yolov8n.pt        args...
-          classify       predict        yolov8n-cls.yaml  args...
-          segment        val            yolov8n-seg.yaml  args...
-                         export         yolov8n.pt        format=onnx  args...
-```
+#### Python
 
 YOLOv8 may also be used directly in a Python environment, and accepts the
 same [arguments](https://docs.ultralytics.com/config/) as in the CLI example above:
 
 ```python
 from ultralytics import YOLO
 
@@ -151,17 +153,18 @@
 results = model.train(data="coco128.yaml", epochs=3)  # train the model
 results = model.val()  # evaluate model performance on the validation set
 results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
 success = model.export(format="onnx")  # export the model to ONNX format
 ```
 
 [Models](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download automatically from the latest
-Ultralytics [release](https://github.com/ultralytics/assets/releases).
+Ultralytics [release](https://github.com/ultralytics/assets/releases). See
+YOLOv8 [Python Docs](https://docs.ultralytics.com/python) for more examples.
 
-### Known Issues / TODOs
+#### Known Issues / TODOs
 
 We are still working on several parts of YOLOv8! We aim to have these completed soon to bring the YOLOv8 feature set up
 to par with YOLOv5, including export and inference to all the same formats. We are also writing a YOLOv8 paper which we
 will submit to [arxiv.org](https://arxiv.org) once complete.
 
 - [ ] TensorFlow exports
 - [ ] DDP resume
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: ultralytics Version: 8.0.8 Summary: Ultralytics
+Metadata-Version: 2.1 Name: ultralytics Version: 8.0.9 Summary: Ultralytics
 YOLOv8 Home-page: https://github.com/ultralytics/ultralytics Author:
 Ultralytics Author-email: hello@ultralytics.com License: GPL-3.0 Project-URL:
 Bug Reports, https://github.com/ultralytics/ultralytics/issues Project-URL:
 Funding, https://ultralytics.com Project-URL: Source, https://github.com/
 ultralytics/ultralytics Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,YOLOv3,YOLOv5,YOLOv8,HUB,Ultralytics Classifier:
 Intended Audience :: Developers Classifier: Intended Audience :: Science/
@@ -53,40 +53,39 @@
                                  Documentation
 See below for a quickstart installation and usage example, and see the [YOLOv8
 Docs](https://docs.ultralytics.com) for full documentation on training,
 validation, prediction and deployment.  Install Pip install the ultralytics
 package including all [requirements.txt](https://github.com/ultralytics/
 ultralytics/blob/main/requirements.txt) in a [**3.10>=Python>=3.7**](https://
 www.python.org/) environment, including [**PyTorch>=1.7**](https://pytorch.org/
-get-started/locally/). ```bash pip install ultralytics ```   Usage YOLOv8 may
-be used directly in the Command Line Interface (CLI) with a `yolo` command:
-```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/images/
-bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and accepts
-additional arguments, i.e. `imgsz=640`. See a full list of available `yolo`
-[arguments](https://docs.ultralytics.com/config/) in the YOLOv8 [Docs](https://
-docs.ultralytics.com). ```bash yolo task=detect mode=train model=yolov8n.pt
-args... classify predict yolov8n-cls.yaml args... segment val yolov8n-seg.yaml
-args... export yolov8n.pt format=onnx args... ``` YOLOv8 may also be used
-directly in a Python environment, and accepts the same [arguments](https://
-docs.ultralytics.com/config/) as in the CLI example above: ```python from
+get-started/locally/). ```bash pip install ultralytics ```   Usage #### CLI
+YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo`
+command: ```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/
+images/bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and
+accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8 [CLI Docs]
+(https://docs.ultralytics.com/cli) for examples. #### Python YOLOv8 may also be
+used directly in a Python environment, and accepts the same [arguments](https:/
+/docs.ultralytics.com/config/) as in the CLI example above: ```python from
 ultralytics import YOLO # Load a model model = YOLO("yolov8n.yaml") # build a
 new model from scratch model = YOLO("yolov8n.pt") # load a pretrained model
 (recommended for training) # Use the model results = model.train
 (data="coco128.yaml", epochs=3) # train the model results = model.val() #
 evaluate model performance on the validation set results = model("https://
 ultralytics.com/images/bus.jpg") # predict on an image success = model.export
 (format="onnx") # export the model to ONNX format ``` [Models](https://
 github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download
 automatically from the latest Ultralytics [release](https://github.com/
-ultralytics/assets/releases). ### Known Issues / TODOs We are still working on
-several parts of YOLOv8! We aim to have these completed soon to bring the
-YOLOv8 feature set up to par with YOLOv5, including export and inference to all
-the same formats. We are also writing a YOLOv8 paper which we will submit to
-[arxiv.org](https://arxiv.org) once complete. - [ ] TensorFlow exports - [ ]
-DDP resume - [ ] [arxiv.org](https://arxiv.org) paper  ##
+ultralytics/assets/releases). See YOLOv8 [Python Docs](https://
+docs.ultralytics.com/python) for more examples. #### Known Issues / TODOs We
+are still working on several parts of YOLOv8! We aim to have these completed
+soon to bring the YOLOv8 feature set up to par with YOLOv5, including export
+and inference to all the same formats. We are also writing a YOLOv8 paper which
+we will submit to [arxiv.org](https://arxiv.org) once complete. - [ ]
+TensorFlow exports - [ ] DDP resume - [ ] [arxiv.org](https://arxiv.org) paper
+##
                                     Models
 All YOLOv8 pretrained models are available here. Detection and Segmentation
 models are pretrained on the COCO dataset, while Classification models are
 pretrained on the ImageNet dataset. [Models](https://github.com/ultralytics/
 ultralytics/tree/main/ultralytics/models) download automatically from the
 latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on
 first use. Detection See [Detection Docs](https://docs.ultralytics.com/tasks/
```

### Comparing `ultralytics-8.0.8/README.md` & `ultralytics-8.0.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -52,28 +52,34 @@
   </div>
 </div>
 
 ## <div align="center">Ultralytics Live Session</div>
 
 <div align="center">
 
-[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and ease of use make it a top choice for professionals and researchers alike.
+[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into
+the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object
+detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and
+ease of use make it a top choice for professionals and researchers alike.
+
+In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the
+opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared
+with any questions you may have.
 
-In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared with any questions you may have.
-
-To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your notifications!
+To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your
+notifications!
 
 <a align="center" href="https://youtu.be/IPcpYO5ITa8" target="_blank">
 <img width="80%" src="https://user-images.githubusercontent.com/107626595/212887899-e94b006c-5192-40fa-8b24-7b5428e065e8.png"></a>
 </div>
 
 ## <div align="center">Documentation</div>
 
-See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for full
-documentation on training, validation, prediction and deployment.
+See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for
+full documentation on training, validation, prediction and deployment.
 
 <details open>
 <summary>Install</summary>
 
 Pip install the ultralytics package including
 all [requirements.txt](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) in a
 [**3.10>=Python>=3.7**](https://www.python.org/) environment, including
@@ -84,30 +90,26 @@
 ```
 
 </details>
 
 <details open>
 <summary>Usage</summary>
 
+#### CLI
+
 YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo` command:
 
 ```bash
 yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
 ```
 
-`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list
-of available `yolo` [arguments](https://docs.ultralytics.com/config/) in the
-YOLOv8 [Docs](https://docs.ultralytics.com).
+`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8
+[CLI Docs](https://docs.ultralytics.com/cli) for examples.
 
-```bash
-yolo task=detect    mode=train    model=yolov8n.pt        args...
-          classify       predict        yolov8n-cls.yaml  args...
-          segment        val            yolov8n-seg.yaml  args...
-                         export         yolov8n.pt        format=onnx  args...
-```
+#### Python
 
 YOLOv8 may also be used directly in a Python environment, and accepts the
 same [arguments](https://docs.ultralytics.com/config/) as in the CLI example above:
 
 ```python
 from ultralytics import YOLO
 
@@ -119,17 +121,18 @@
 results = model.train(data="coco128.yaml", epochs=3)  # train the model
 results = model.val()  # evaluate model performance on the validation set
 results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
 success = model.export(format="onnx")  # export the model to ONNX format
 ```
 
 [Models](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download automatically from the latest
-Ultralytics [release](https://github.com/ultralytics/assets/releases).
+Ultralytics [release](https://github.com/ultralytics/assets/releases). See
+YOLOv8 [Python Docs](https://docs.ultralytics.com/python) for more examples.
 
-### Known Issues / TODOs
+#### Known Issues / TODOs
 
 We are still working on several parts of YOLOv8! We aim to have these completed soon to bring the YOLOv8 feature set up
 to par with YOLOv5, including export and inference to all the same formats. We are also writing a YOLOv8 paper which we
 will submit to [arxiv.org](https://arxiv.org) once complete.
 
 - [ ] TensorFlow exports
 - [ ] DDP resume
```

#### html2text {}

```diff
@@ -34,40 +34,39 @@
                                  Documentation
 See below for a quickstart installation and usage example, and see the [YOLOv8
 Docs](https://docs.ultralytics.com) for full documentation on training,
 validation, prediction and deployment.  Install Pip install the ultralytics
 package including all [requirements.txt](https://github.com/ultralytics/
 ultralytics/blob/main/requirements.txt) in a [**3.10>=Python>=3.7**](https://
 www.python.org/) environment, including [**PyTorch>=1.7**](https://pytorch.org/
-get-started/locally/). ```bash pip install ultralytics ```   Usage YOLOv8 may
-be used directly in the Command Line Interface (CLI) with a `yolo` command:
-```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/images/
-bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and accepts
-additional arguments, i.e. `imgsz=640`. See a full list of available `yolo`
-[arguments](https://docs.ultralytics.com/config/) in the YOLOv8 [Docs](https://
-docs.ultralytics.com). ```bash yolo task=detect mode=train model=yolov8n.pt
-args... classify predict yolov8n-cls.yaml args... segment val yolov8n-seg.yaml
-args... export yolov8n.pt format=onnx args... ``` YOLOv8 may also be used
-directly in a Python environment, and accepts the same [arguments](https://
-docs.ultralytics.com/config/) as in the CLI example above: ```python from
+get-started/locally/). ```bash pip install ultralytics ```   Usage #### CLI
+YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo`
+command: ```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/
+images/bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and
+accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8 [CLI Docs]
+(https://docs.ultralytics.com/cli) for examples. #### Python YOLOv8 may also be
+used directly in a Python environment, and accepts the same [arguments](https:/
+/docs.ultralytics.com/config/) as in the CLI example above: ```python from
 ultralytics import YOLO # Load a model model = YOLO("yolov8n.yaml") # build a
 new model from scratch model = YOLO("yolov8n.pt") # load a pretrained model
 (recommended for training) # Use the model results = model.train
 (data="coco128.yaml", epochs=3) # train the model results = model.val() #
 evaluate model performance on the validation set results = model("https://
 ultralytics.com/images/bus.jpg") # predict on an image success = model.export
 (format="onnx") # export the model to ONNX format ``` [Models](https://
 github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download
 automatically from the latest Ultralytics [release](https://github.com/
-ultralytics/assets/releases). ### Known Issues / TODOs We are still working on
-several parts of YOLOv8! We aim to have these completed soon to bring the
-YOLOv8 feature set up to par with YOLOv5, including export and inference to all
-the same formats. We are also writing a YOLOv8 paper which we will submit to
-[arxiv.org](https://arxiv.org) once complete. - [ ] TensorFlow exports - [ ]
-DDP resume - [ ] [arxiv.org](https://arxiv.org) paper  ##
+ultralytics/assets/releases). See YOLOv8 [Python Docs](https://
+docs.ultralytics.com/python) for more examples. #### Known Issues / TODOs We
+are still working on several parts of YOLOv8! We aim to have these completed
+soon to bring the YOLOv8 feature set up to par with YOLOv5, including export
+and inference to all the same formats. We are also writing a YOLOv8 paper which
+we will submit to [arxiv.org](https://arxiv.org) once complete. - [ ]
+TensorFlow exports - [ ] DDP resume - [ ] [arxiv.org](https://arxiv.org) paper
+##
                                     Models
 All YOLOv8 pretrained models are available here. Detection and Segmentation
 models are pretrained on the COCO dataset, while Classification models are
 pretrained on the ImageNet dataset. [Models](https://github.com/ultralytics/
 ultralytics/tree/main/ultralytics/models) download automatically from the
 latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on
 first use. Detection See [Detection Docs](https://docs.ultralytics.com/tasks/
```

### Comparing `ultralytics-8.0.8/README.zh-CN.md` & `ultralytics-8.0.9/README.zh-CN.md`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/requirements.txt` & `ultralytics-8.0.9/requirements.txt`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/setup.cfg` & `ultralytics-8.0.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/setup.py` & `ultralytics-8.0.9/setup.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/hub/__init__.py` & `ultralytics-8.0.9/ultralytics/hub/__init__.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,42 +1,18 @@
 # Ultralytics YOLO 🚀, GPL-3.0 license
 
-import os
-import shutil
-
-import psutil
 import requests
-from IPython import display  # to display images and clear console output
 
 from ultralytics.hub.auth import Auth
 from ultralytics.hub.session import HubTrainingSession
 from ultralytics.hub.utils import PREFIX, split_key
-from ultralytics.yolo.utils import LOGGER, emojis, is_colab
-from ultralytics.yolo.utils.torch_utils import select_device
+from ultralytics.yolo.utils import LOGGER, emojis
 from ultralytics.yolo.v8.detect import DetectionTrainer
 
 
-def checks(verbose=True):
-    if is_colab():
-        shutil.rmtree('sample_data', ignore_errors=True)  # remove colab /sample_data directory
-
-    if verbose:
-        # System info
-        gib = 1 << 30  # bytes per GiB
-        ram = psutil.virtual_memory().total
-        total, used, free = shutil.disk_usage("/")
-        display.clear_output()
-        s = f'({os.cpu_count()} CPUs, {ram / gib:.1f} GB RAM, {(total - free) / gib:.1f}/{total / gib:.1f} GB disk)'
-    else:
-        s = ''
-
-    select_device(newline=False)
-    LOGGER.info(f'Setup complete ✅ {s}')
-
-
 def start(key=''):
     # Start training models with Ultralytics HUB. Usage: from src.ultralytics import start; start('API_KEY')
     def request_api_key(attempts=0):
         """Prompt the user to input their API key"""
         import getpass
 
         max_attempts = 3
```

### Comparing `ultralytics-8.0.8/ultralytics/hub/auth.py` & `ultralytics-8.0.9/ultralytics/hub/auth.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/hub/session.py` & `ultralytics-8.0.9/ultralytics/hub/session.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/hub/utils.py` & `ultralytics-8.0.9/ultralytics/hub/utils.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v3/yolov3-spp.yaml` & `ultralytics-8.0.9/ultralytics/models/v3/yolov3-spp.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v3/yolov3-tiny.yaml` & `ultralytics-8.0.9/ultralytics/models/v3/yolov3-tiny.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v3/yolov3.yaml` & `ultralytics-8.0.9/ultralytics/models/v3/yolov3.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v5/yolov5l.yaml` & `ultralytics-8.0.9/ultralytics/models/v5/yolov5l.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v5/yolov5m.yaml` & `ultralytics-8.0.9/ultralytics/models/v5/yolov5m.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v5/yolov5n.yaml` & `ultralytics-8.0.9/ultralytics/models/v5/yolov5n.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v5/yolov5s.yaml` & `ultralytics-8.0.9/ultralytics/models/v5/yolov5s.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v5/yolov5x.yaml` & `ultralytics-8.0.9/ultralytics/models/v5/yolov5x.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8l-cls.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8l-cls.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8m-cls.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8m-cls.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8n-cls.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8n-cls.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8s-cls.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8s-cls.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/cls/yolov8x-cls.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/cls/yolov8x-cls.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8l-seg.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8l-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8m-seg.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8m-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8n-seg.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8n-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8s-seg.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8s-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/seg/yolov8x-seg.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/seg/yolov8x-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8l.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8l.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8m.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8m.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8n.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8n.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8s.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8s.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8x.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8x.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/models/v8/yolov8x6.yaml` & `ultralytics-8.0.9/ultralytics/models/v8/yolov8x6.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/nn/autobackend.py` & `ultralytics-8.0.9/ultralytics/nn/autobackend.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/nn/autoshape.py` & `ultralytics-8.0.9/ultralytics/nn/autoshape.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/nn/modules.py` & `ultralytics-8.0.9/ultralytics/nn/modules.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/nn/tasks.py` & `ultralytics-8.0.9/ultralytics/nn/tasks.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/configs/__init__.py` & `ultralytics-8.0.9/ultralytics/yolo/configs/__init__.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/configs/default.yaml` & `ultralytics-8.0.9/ultralytics/yolo/configs/default.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/configs/hydra_patch.py` & `ultralytics-8.0.9/ultralytics/yolo/configs/hydra_patch.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/augment.py` & `ultralytics-8.0.9/ultralytics/yolo/data/augment.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/base.py` & `ultralytics-8.0.9/ultralytics/yolo/data/base.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/build.py` & `ultralytics-8.0.9/ultralytics/yolo/data/build.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/stream_loaders.py` & `ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/stream_loaders.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/v5augmentations.py` & `ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/v5augmentations.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/dataloaders/v5loader.py` & `ultralytics-8.0.9/ultralytics/yolo/data/dataloaders/v5loader.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/dataset.py` & `ultralytics-8.0.9/ultralytics/yolo/data/dataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -84,14 +84,15 @@
             LOGGER.info("\n".join(msgs))
         if nf == 0:
             LOGGER.warning(f"{self.prefix}WARNING ⚠️ No labels found in {path}. {HELP_URL}")
         x["hash"] = get_hash(self.label_files + self.im_files)
         x["results"] = nf, nm, ne, nc, len(self.im_files)
         x["msgs"] = msgs  # warnings
         x["version"] = self.cache_version  # cache version
+        self.im_files = [lb["im_file"] for lb in x["labels"]]
         try:
             np.save(path, x)  # save cache for next time
             path.with_suffix(".cache.npy").rename(path)  # remove .npy suffix
             LOGGER.info(f"{self.prefix}New cache created: {path}")
         except Exception as e:
             LOGGER.warning(
                 f"{self.prefix}WARNING ⚠️ Cache directory {path.parent} is not writeable: {e}")  # not writeable
```

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/dataset_wrappers.py` & `ultralytics-8.0.9/ultralytics/yolo/data/dataset_wrappers.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/Argoverse.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/Argoverse.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/GlobalWheat2020.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/GlobalWheat2020.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/ImageNet.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/ImageNet.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/Objects365.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/Objects365.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/SKU-110K.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/SKU-110K.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/VOC.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/VOC.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/VisDrone.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/VisDrone.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco128-seg.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco128-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco128.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco128.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco8-seg.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco8-seg.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/coco8.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/coco8.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/datasets/xView.yaml` & `ultralytics-8.0.9/ultralytics/yolo/data/datasets/xView.yaml`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/data/utils.py` & `ultralytics-8.0.9/ultralytics/yolo/data/utils.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/exporter.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/exporter.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/model.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/model.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/predictor.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/predictor.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/results.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/results.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/trainer.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/trainer.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/engine/validator.py` & `ultralytics-8.0.9/ultralytics/yolo/engine/validator.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/__init__.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/autobatch.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/autobatch.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/base.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/base.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/clearml.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/clearml.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/comet.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/comet.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/hub.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/hub.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/callbacks/tensorboard.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/callbacks/tensorboard.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/checks.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/checks.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,29 @@
 # Ultralytics YOLO 🚀, GPL-3.0 license
 
 import glob
 import inspect
 import math
+import os
 import platform
+import shutil
 import urllib
 from pathlib import Path
 from subprocess import check_output
 from typing import Optional
 
 import cv2
 import numpy as np
 import pkg_resources as pkg
+import psutil
 import torch
+from IPython import display
 
 from ultralytics.yolo.utils import (AUTOINSTALL, FONT, LOGGER, ROOT, USER_CONFIG_DIR, TryExcept, colorstr, emojis,
-                                    is_docker, is_jupyter_notebook)
+                                    is_colab, is_docker, is_jupyter_notebook)
 
 
 def is_ascii(s) -> bool:
     """
     Check if a string is composed of only ASCII characters.
 
     Args:
@@ -241,14 +245,34 @@
         return True
     except Exception as e:
         if warn:
             LOGGER.warning(f'WARNING ⚠️ Environment does not support cv2.imshow() or PIL Image.show()\n{e}')
         return False
 
 
+def check_yolo(verbose=True):
+    from ultralytics.yolo.utils.torch_utils import select_device
+
+    if is_colab():
+        shutil.rmtree('sample_data', ignore_errors=True)  # remove colab /sample_data directory
+
+    if verbose:
+        # System info
+        gib = 1 << 30  # bytes per GiB
+        ram = psutil.virtual_memory().total
+        total, used, free = shutil.disk_usage("/")
+        display.clear_output()
+        s = f'({os.cpu_count()} CPUs, {ram / gib:.1f} GB RAM, {(total - free) / gib:.1f}/{total / gib:.1f} GB disk)'
+    else:
+        s = ''
+
+    select_device(newline=False)
+    LOGGER.info(f'Setup complete ✅ {s}')
+
+
 def git_describe(path=ROOT):  # path must be a directory
     # Return human-readable git description, i.e. v5.0-5-g3e25f1e https://git-scm.com/docs/git-describe
     try:
         assert (Path(path) / '.git').is_dir()
         return check_output(f'git -C {path} describe --tags --long --always', shell=True).decode()[:-1]
     except Exception:
         return ''
```

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/dist.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/dist.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/downloads.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/downloads.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/files.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/files.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/instance.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/instance.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/loss.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/loss.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/metrics.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/metrics.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/ops.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/ops.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/plotting.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/plotting.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/tal.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/tal.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/utils/torch_utils.py` & `ultralytics-8.0.9/ultralytics/yolo/utils/torch_utils.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/classify/predict.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/classify/predict.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/classify/train.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/classify/train.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/classify/val.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/classify/val.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/detect/predict.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/detect/predict.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/detect/train.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/detect/train.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/detect/val.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/detect/val.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/segment/predict.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/segment/predict.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/segment/train.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/segment/train.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics/yolo/v8/segment/val.py` & `ultralytics-8.0.9/ultralytics/yolo/v8/segment/val.py`

 * *Files identical despite different names*

### Comparing `ultralytics-8.0.8/ultralytics.egg-info/PKG-INFO` & `ultralytics-8.0.9/ultralytics.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ultralytics
-Version: 8.0.8
+Version: 8.0.9
 Summary: Ultralytics YOLOv8
 Home-page: https://github.com/ultralytics/ultralytics
 Author: Ultralytics
 Author-email: hello@ultralytics.com
 License: GPL-3.0
 Project-URL: Bug Reports, https://github.com/ultralytics/ultralytics/issues
 Project-URL: Funding, https://ultralytics.com
@@ -84,28 +84,34 @@
   </div>
 </div>
 
 ## <div align="center">Ultralytics Live Session</div>
 
 <div align="center">
 
-[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and ease of use make it a top choice for professionals and researchers alike.
+[Ultralytics Live Session 3](https://youtu.be/IPcpYO5ITa8) ✨ is here! Join us on January 24th at 18 CET as we dive into
+the latest advancements in YOLOv8, and demonstrate how to use this cutting-edge, SOTA model to improve your object
+detection, instance segmentation, and image classification projects. See firsthand how YOLOv8's speed, accuracy, and
+ease of use make it a top choice for professionals and researchers alike.
+
+In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the
+opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared
+with any questions you may have.
 
-In addition to learning about the exciting new features and improvements of Ultralytics YOLOv8, you will also have the opportunity to ask questions and interact with our team during the live Q&A session. We encourage you to come prepared with any questions you may have.
-
-To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your notifications!
+To join the webinar, visit our YouTube [Channel](https://www.youtube.com/@Ultralytics/streams) and turn on your
+notifications!
 
 <a align="center" href="https://youtu.be/IPcpYO5ITa8" target="_blank">
 <img width="80%" src="https://user-images.githubusercontent.com/107626595/212887899-e94b006c-5192-40fa-8b24-7b5428e065e8.png"></a>
 </div>
 
 ## <div align="center">Documentation</div>
 
-See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for full
-documentation on training, validation, prediction and deployment.
+See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for
+full documentation on training, validation, prediction and deployment.
 
 <details open>
 <summary>Install</summary>
 
 Pip install the ultralytics package including
 all [requirements.txt](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) in a
 [**3.10>=Python>=3.7**](https://www.python.org/) environment, including
@@ -116,30 +122,26 @@
 ```
 
 </details>
 
 <details open>
 <summary>Usage</summary>
 
+#### CLI
+
 YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo` command:
 
 ```bash
 yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
 ```
 
-`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list
-of available `yolo` [arguments](https://docs.ultralytics.com/config/) in the
-YOLOv8 [Docs](https://docs.ultralytics.com).
+`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8
+[CLI Docs](https://docs.ultralytics.com/cli) for examples.
 
-```bash
-yolo task=detect    mode=train    model=yolov8n.pt        args...
-          classify       predict        yolov8n-cls.yaml  args...
-          segment        val            yolov8n-seg.yaml  args...
-                         export         yolov8n.pt        format=onnx  args...
-```
+#### Python
 
 YOLOv8 may also be used directly in a Python environment, and accepts the
 same [arguments](https://docs.ultralytics.com/config/) as in the CLI example above:
 
 ```python
 from ultralytics import YOLO
 
@@ -151,17 +153,18 @@
 results = model.train(data="coco128.yaml", epochs=3)  # train the model
 results = model.val()  # evaluate model performance on the validation set
 results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
 success = model.export(format="onnx")  # export the model to ONNX format
 ```
 
 [Models](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download automatically from the latest
-Ultralytics [release](https://github.com/ultralytics/assets/releases).
+Ultralytics [release](https://github.com/ultralytics/assets/releases). See
+YOLOv8 [Python Docs](https://docs.ultralytics.com/python) for more examples.
 
-### Known Issues / TODOs
+#### Known Issues / TODOs
 
 We are still working on several parts of YOLOv8! We aim to have these completed soon to bring the YOLOv8 feature set up
 to par with YOLOv5, including export and inference to all the same formats. We are also writing a YOLOv8 paper which we
 will submit to [arxiv.org](https://arxiv.org) once complete.
 
 - [ ] TensorFlow exports
 - [ ] DDP resume
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: ultralytics Version: 8.0.8 Summary: Ultralytics
+Metadata-Version: 2.1 Name: ultralytics Version: 8.0.9 Summary: Ultralytics
 YOLOv8 Home-page: https://github.com/ultralytics/ultralytics Author:
 Ultralytics Author-email: hello@ultralytics.com License: GPL-3.0 Project-URL:
 Bug Reports, https://github.com/ultralytics/ultralytics/issues Project-URL:
 Funding, https://ultralytics.com Project-URL: Source, https://github.com/
 ultralytics/ultralytics Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,YOLOv3,YOLOv5,YOLOv8,HUB,Ultralytics Classifier:
 Intended Audience :: Developers Classifier: Intended Audience :: Science/
@@ -53,40 +53,39 @@
                                  Documentation
 See below for a quickstart installation and usage example, and see the [YOLOv8
 Docs](https://docs.ultralytics.com) for full documentation on training,
 validation, prediction and deployment.  Install Pip install the ultralytics
 package including all [requirements.txt](https://github.com/ultralytics/
 ultralytics/blob/main/requirements.txt) in a [**3.10>=Python>=3.7**](https://
 www.python.org/) environment, including [**PyTorch>=1.7**](https://pytorch.org/
-get-started/locally/). ```bash pip install ultralytics ```   Usage YOLOv8 may
-be used directly in the Command Line Interface (CLI) with a `yolo` command:
-```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/images/
-bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and accepts
-additional arguments, i.e. `imgsz=640`. See a full list of available `yolo`
-[arguments](https://docs.ultralytics.com/config/) in the YOLOv8 [Docs](https://
-docs.ultralytics.com). ```bash yolo task=detect mode=train model=yolov8n.pt
-args... classify predict yolov8n-cls.yaml args... segment val yolov8n-seg.yaml
-args... export yolov8n.pt format=onnx args... ``` YOLOv8 may also be used
-directly in a Python environment, and accepts the same [arguments](https://
-docs.ultralytics.com/config/) as in the CLI example above: ```python from
+get-started/locally/). ```bash pip install ultralytics ```   Usage #### CLI
+YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo`
+command: ```bash yolo predict model=yolov8n.pt source="https://ultralytics.com/
+images/bus.jpg" ``` `yolo` can be used for a variety of tasks and modes and
+accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8 [CLI Docs]
+(https://docs.ultralytics.com/cli) for examples. #### Python YOLOv8 may also be
+used directly in a Python environment, and accepts the same [arguments](https:/
+/docs.ultralytics.com/config/) as in the CLI example above: ```python from
 ultralytics import YOLO # Load a model model = YOLO("yolov8n.yaml") # build a
 new model from scratch model = YOLO("yolov8n.pt") # load a pretrained model
 (recommended for training) # Use the model results = model.train
 (data="coco128.yaml", epochs=3) # train the model results = model.val() #
 evaluate model performance on the validation set results = model("https://
 ultralytics.com/images/bus.jpg") # predict on an image success = model.export
 (format="onnx") # export the model to ONNX format ``` [Models](https://
 github.com/ultralytics/ultralytics/tree/main/ultralytics/models) download
 automatically from the latest Ultralytics [release](https://github.com/
-ultralytics/assets/releases). ### Known Issues / TODOs We are still working on
-several parts of YOLOv8! We aim to have these completed soon to bring the
-YOLOv8 feature set up to par with YOLOv5, including export and inference to all
-the same formats. We are also writing a YOLOv8 paper which we will submit to
-[arxiv.org](https://arxiv.org) once complete. - [ ] TensorFlow exports - [ ]
-DDP resume - [ ] [arxiv.org](https://arxiv.org) paper  ##
+ultralytics/assets/releases). See YOLOv8 [Python Docs](https://
+docs.ultralytics.com/python) for more examples. #### Known Issues / TODOs We
+are still working on several parts of YOLOv8! We aim to have these completed
+soon to bring the YOLOv8 feature set up to par with YOLOv5, including export
+and inference to all the same formats. We are also writing a YOLOv8 paper which
+we will submit to [arxiv.org](https://arxiv.org) once complete. - [ ]
+TensorFlow exports - [ ] DDP resume - [ ] [arxiv.org](https://arxiv.org) paper
+##
                                     Models
 All YOLOv8 pretrained models are available here. Detection and Segmentation
 models are pretrained on the COCO dataset, while Classification models are
 pretrained on the ImageNet dataset. [Models](https://github.com/ultralytics/
 ultralytics/tree/main/ultralytics/models) download automatically from the
 latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on
 first use. Detection See [Detection Docs](https://docs.ultralytics.com/tasks/
```

### Comparing `ultralytics-8.0.8/ultralytics.egg-info/SOURCES.txt` & `ultralytics-8.0.9/ultralytics.egg-info/SOURCES.txt`

 * *Files identical despite different names*

