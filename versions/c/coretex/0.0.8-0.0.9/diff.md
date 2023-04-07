# Comparing `tmp/coretex-0.0.8.tar.gz` & `tmp/coretex-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "coretex-0.0.8.tar", last modified: Fri Feb 10 09:27:45 2023, max compression
+gzip compressed data, was "coretex-0.0.9.tar", last modified: Tue Feb 14 14:03:55 2023, max compression
```

## Comparing `coretex-0.0.8.tar` & `coretex-0.0.9.tar`

### file list

```diff
@@ -1,149 +1,149 @@
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.013332 coretex-0.0.8/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      805 2023-02-10 09:27:45.009333 coretex-0.0.8/PKG-INFO
--rw-r--r--   0 jenkins    (113) jenkins    (119)       57 2023-02-10 09:27:35.000000 coretex-0.0.8/README.md
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1200 2023-02-10 09:27:35.000000 coretex-0.0.8/pyproject.toml
--rw-r--r--   0 jenkins    (113) jenkins    (119)       38 2023-02-10 09:27:45.013332 coretex-0.0.8/setup.cfg
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.981334 coretex-0.0.8/src/
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.985334 coretex-0.0.8/src/coretex/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       40 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/__init__.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/cache/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       97 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/cache/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     5462 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/cache/cache_module.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/codable/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       67 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/codable/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     6538 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/codable/codable.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      658 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/codable/descriptor.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/context/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       50 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/context/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     3550 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/context/experiment_context.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/coretex/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      139 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/__init__.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/coretex/annotation/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       21 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/annotation/__init__.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex/coretex/annotation/image/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      170 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/annotation/image/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1619 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/annotation/image/bbox.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2524 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/annotation/image/classes_format.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2805 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/annotation/image/coretex_format.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.993333 coretex-0.0.8/src/coretex/coretex/conversion/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       31 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2768 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/base_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      703 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1444 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converter_processor_factory.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.993333 coretex-0.0.8/src/coretex/coretex/conversion/converters/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      385 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     3660 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/city_scape_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     3672 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/coco_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2707 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/create_ml_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     4891 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/human_segmentation_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2566 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/label_me_converter.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.993333 coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       54 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)    10756 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/instance_extractor.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2512 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/pascal_2012_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      964 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/shared.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2961 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/voc_converter.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     4849 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/conversion/converters/yolo_converter.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.997333 coretex-0.0.8/src/coretex/coretex/dataset/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      477 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/__init__.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.997333 coretex-0.0.8/src/coretex/coretex/dataset/custom_dataset/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       95 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/custom_dataset/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)       34 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/custom_dataset/base.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      472 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/custom_dataset/custom_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      310 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/custom_dataset/local_custom_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1893 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/dataset.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.997333 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      154 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1366 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/base.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2285 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/image_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      842 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/local_image_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     8170 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/synthetic_image_generator.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.997333 coretex-0.0.8/src/coretex/coretex/dataset/image_segmentation_dataset/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      141 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_segmentation_dataset/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      455 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_segmentation_dataset/image_segmentation_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      309 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/image_segmentation_dataset/local_image_segmentation_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1420 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/local_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     3737 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/network_dataset.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.997333 coretex-0.0.8/src/coretex/coretex/dataset/object_detection_dataset/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      130 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/object_detection_dataset/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      296 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/object_detection_dataset/local_object_detection_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      447 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/object_detection_dataset/object_detection_dataset.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      329 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/dataset/utils.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.001333 coretex-0.0.8/src/coretex/coretex/experiment/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      103 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/experiment/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     3834 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/experiment/artifact.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     7016 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/experiment/experiment.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1300 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/experiment/status.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.001333 coretex-0.0.8/src/coretex/coretex/item/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      431 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      299 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/any_local_item.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.001333 coretex-0.0.8/src/coretex/coretex/item/custom_item/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       83 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/custom_item/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1053 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/custom_item/custom_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      138 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/custom_item/custom_item_data.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      244 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/custom_item/local_custom_item.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.001333 coretex-0.0.8/src/coretex/coretex/item/image_item/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      131 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_item/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      215 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_item/image_format.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2056 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_item/image_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1611 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_item/image_item_data.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      962 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_item/local_image_item.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.001333 coretex-0.0.8/src/coretex/coretex/item/image_segmentation_item/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      129 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_segmentation_item/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      726 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_segmentation_item/image_segmentation_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      137 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/image_segmentation_item/local_image_segmentation_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1808 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      773 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/local_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2090 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/network_item.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.005333 coretex-0.0.8/src/coretex/coretex/item/object_detection_item/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      121 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/object_detection_item/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      135 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/object_detection_item/local_object_detection_item.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      718 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/item/object_detection_item/object_detection_item.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.005333 coretex-0.0.8/src/coretex/coretex/model/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       25 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/model/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     4606 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/model/model.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.005333 coretex-0.0.8/src/coretex/coretex/project/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      100 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/project/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1911 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/project/base.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1705 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/project/project.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      388 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/project/project_task.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1189 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/coretex/project/workspace.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.005333 coretex-0.0.8/src/coretex/folder_management/
--rw-r--r--   0 jenkins    (113) jenkins    (119)       42 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/folder_management/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2373 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/folder_management/folder_manager.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.005333 coretex-0.0.8/src/coretex/logging/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      486 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/logging/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1257 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/logging/log.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1777 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/logging/log_severity.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     4889 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/logging/logger.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.009333 coretex-0.0.8/src/coretex/networking/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      238 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)    11426 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/network_manager.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     4491 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/network_object.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2258 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/network_response.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      122 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/request_type.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     5459 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/networking/requests_manager.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.009333 coretex-0.0.8/src/coretex/qiime2/
--rw-r--r--   0 jenkins    (113) jenkins    (119)     7678 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/qiime2/__init__.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.009333 coretex-0.0.8/src/coretex/threading/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      110 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/threading/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      306 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/threading/stoppable_thread.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1179 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/threading/threaded_data_processor.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.009333 coretex-0.0.8/src/coretex/utils/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      153 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/utils/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1303 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/utils/console_progress_bar.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)       96 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/utils/date.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2885 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/utils/file.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      258 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/utils/number.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:45.009333 coretex-0.0.8/src/coretex/workspace/
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2126 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/workspace/__init__.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1061 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/workspace/base.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     1567 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/workspace/heartbeat.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)     2529 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/workspace/local.py
--rw-r--r--   0 jenkins    (113) jenkins    (119)      669 2023-02-10 09:27:35.000000 coretex-0.0.8/src/coretex/workspace/remote.py
-drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-10 09:27:44.989334 coretex-0.0.8/src/coretex.egg-info/
--rw-r--r--   0 jenkins    (113) jenkins    (119)      805 2023-02-10 09:27:44.000000 coretex-0.0.8/src/coretex.egg-info/PKG-INFO
--rw-r--r--   0 jenkins    (113) jenkins    (119)     5389 2023-02-10 09:27:44.000000 coretex-0.0.8/src/coretex.egg-info/SOURCES.txt
--rw-r--r--   0 jenkins    (113) jenkins    (119)        1 2023-02-10 09:27:44.000000 coretex-0.0.8/src/coretex.egg-info/dependency_links.txt
--rw-r--r--   0 jenkins    (113) jenkins    (119)      152 2023-02-10 09:27:44.000000 coretex-0.0.8/src/coretex.egg-info/requires.txt
--rw-r--r--   0 jenkins    (113) jenkins    (119)        8 2023-02-10 09:27:44.000000 coretex-0.0.8/src/coretex.egg-info/top_level.txt
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.925225 coretex-0.0.9/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      805 2023-02-14 14:03:55.921226 coretex-0.0.9/PKG-INFO
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       57 2023-02-10 09:27:35.000000 coretex-0.0.9/README.md
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1200 2023-02-14 14:03:49.000000 coretex-0.0.9/pyproject.toml
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       38 2023-02-14 14:03:55.925225 coretex-0.0.9/setup.cfg
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.901227 coretex-0.0.9/src/
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.905227 coretex-0.0.9/src/coretex/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       40 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/__init__.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/cache/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       97 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/cache/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     5462 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/cache/cache_module.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/codable/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       67 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/codable/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     6538 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/codable/codable.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      658 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/codable/descriptor.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/context/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       50 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/context/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     3550 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/context/experiment_context.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/coretex/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      139 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/__init__.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/coretex/annotation/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       21 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/annotation/__init__.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/coretex/annotation/image/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      170 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/annotation/image/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1619 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/annotation/image/bbox.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2524 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/annotation/image/classes_format.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2805 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/annotation/image/coretex_format.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/coretex/conversion/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       31 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2768 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/base_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      703 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1444 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converter_processor_factory.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex/coretex/conversion/converters/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      385 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     3660 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/city_scape_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     3672 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/coco_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2707 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/create_ml_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     4891 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/human_segmentation_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2566 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/label_me_converter.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       54 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)    10756 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/instance_extractor.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2512 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/pascal_2012_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      964 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/shared.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2961 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/voc_converter.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     4849 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/conversion/converters/yolo_converter.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/dataset/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      477 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/__init__.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/dataset/custom_dataset/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       95 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/custom_dataset/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       34 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/custom_dataset/base.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      472 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/custom_dataset/custom_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      310 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/custom_dataset/local_custom_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1893 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/dataset.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      154 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1366 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/base.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2285 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/image_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      842 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/local_image_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     8170 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/synthetic_image_generator.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/dataset/image_segmentation_dataset/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      141 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_segmentation_dataset/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      455 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_segmentation_dataset/image_segmentation_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      309 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/image_segmentation_dataset/local_image_segmentation_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1420 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/local_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     3737 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/network_dataset.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.913226 coretex-0.0.9/src/coretex/coretex/dataset/object_detection_dataset/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      130 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/object_detection_dataset/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      296 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/object_detection_dataset/local_object_detection_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      447 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/object_detection_dataset/object_detection_dataset.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      329 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/dataset/utils.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/experiment/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      103 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/experiment/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     3834 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/experiment/artifact.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     7016 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/experiment/experiment.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1300 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/experiment/status.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/item/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      431 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      299 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/any_local_item.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/item/custom_item/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       83 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/custom_item/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1053 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/custom_item/custom_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      138 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/custom_item/custom_item_data.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      244 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/custom_item/local_custom_item.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/item/image_item/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      131 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_item/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      215 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_item/image_format.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2056 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_item/image_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1611 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_item/image_item_data.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      962 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_item/local_image_item.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/item/image_segmentation_item/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      129 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_segmentation_item/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      726 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_segmentation_item/image_segmentation_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      137 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/image_segmentation_item/local_image_segmentation_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1808 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      773 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/local_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2090 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/network_item.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/item/object_detection_item/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      121 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/object_detection_item/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      135 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/object_detection_item/local_object_detection_item.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      718 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/item/object_detection_item/object_detection_item.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/model/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       25 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/model/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     4606 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/model/model.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.917226 coretex-0.0.9/src/coretex/coretex/project/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      100 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/project/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1911 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/project/base.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1705 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/project/project.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      388 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/project/project_task.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1189 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/coretex/project/workspace.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/folder_management/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       42 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/folder_management/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2373 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/folder_management/folder_manager.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/logging/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      486 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/logging/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1257 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/logging/log.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1777 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/logging/log_severity.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     4889 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/logging/logger.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/networking/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      238 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)    11426 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/network_manager.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     4491 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/network_object.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2258 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/network_response.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      122 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/request_type.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     5459 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/networking/requests_manager.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/qiime2/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     7678 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/qiime2/__init__.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/threading/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      110 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/threading/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      306 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/threading/stoppable_thread.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1179 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/threading/threaded_data_processor.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/utils/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      153 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/utils/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1303 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/utils/console_progress_bar.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)       96 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/utils/date.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2885 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/utils/file.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      258 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/utils/number.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.921226 coretex-0.0.9/src/coretex/workspace/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2126 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/workspace/__init__.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1061 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/workspace/base.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     1567 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/workspace/heartbeat.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     2529 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/workspace/local.py
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      669 2023-02-10 09:27:35.000000 coretex-0.0.9/src/coretex/workspace/remote.py
+drwxr-xr-x   0 jenkins    (113) jenkins    (119)        0 2023-02-14 14:03:55.909226 coretex-0.0.9/src/coretex.egg-info/
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      805 2023-02-14 14:03:55.000000 coretex-0.0.9/src/coretex.egg-info/PKG-INFO
+-rw-r--r--   0 jenkins    (113) jenkins    (119)     5389 2023-02-14 14:03:55.000000 coretex-0.0.9/src/coretex.egg-info/SOURCES.txt
+-rw-r--r--   0 jenkins    (113) jenkins    (119)        1 2023-02-14 14:03:55.000000 coretex-0.0.9/src/coretex.egg-info/dependency_links.txt
+-rw-r--r--   0 jenkins    (113) jenkins    (119)      152 2023-02-14 14:03:55.000000 coretex-0.0.9/src/coretex.egg-info/requires.txt
+-rw-r--r--   0 jenkins    (113) jenkins    (119)        8 2023-02-14 14:03:55.000000 coretex-0.0.9/src/coretex.egg-info/top_level.txt
```

### Comparing `coretex-0.0.8/PKG-INFO` & `coretex-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coretex
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package for AI experiment tracking, infrastructure and dataset management using Coretex.ai platform.
 Author-email: Igor Perić <igor@coretex.ai>
 Maintainer-email: Duško Mirković <dmirkovic@coretex.ai>, Alex Maslennikov <alex@coretex.ai>, Jovica Zarić <jzaric@coretex.ai>, Darko Zarić <dzaric@coretex.ai>, Bogdan Tintor <btintor@coretex.ai>, Igor Perić <igor@coretex.ai>
 Project-URL: Homepage, https://coretex.ai
 Project-URL: Documentation, https://docs.coretex.ai/1.0.0/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `coretex-0.0.8/pyproject.toml` & `coretex-0.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "coretex"
-version = "0.0.8"
+version = "0.0.9"
 authors = [
   { name="Igor Perić", email="igor@coretex.ai" },
 ]
 maintainers = [
   { name="Duško Mirković", email="dmirkovic@coretex.ai" },
   { name="Alex Maslennikov", email="alex@coretex.ai" },
   { name="Jovica Zarić", email="jzaric@coretex.ai" },
```

### Comparing `coretex-0.0.8/src/coretex/cache/cache_module.py` & `coretex-0.0.9/src/coretex/cache/cache_module.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/codable/codable.py` & `coretex-0.0.9/src/coretex/codable/codable.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/codable/descriptor.py` & `coretex-0.0.9/src/coretex/codable/descriptor.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/context/experiment_context.py` & `coretex-0.0.9/src/coretex/context/experiment_context.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/annotation/image/bbox.py` & `coretex-0.0.9/src/coretex/coretex/annotation/image/bbox.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/annotation/image/classes_format.py` & `coretex-0.0.9/src/coretex/coretex/annotation/image/classes_format.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/annotation/image/coretex_format.py` & `coretex-0.0.9/src/coretex/coretex/annotation/image/coretex_format.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/base_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/base_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converter_processor_factory.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converter_processor_factory.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/city_scape_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/city_scape_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/coco_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/coco_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/create_ml_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/create_ml_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/human_segmentation_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/human_segmentation_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/label_me_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/label_me_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/instance_extractor.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/instance_extractor.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/pascal_2012_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/pascal_2012_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/pascal/shared.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/pascal/shared.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/voc_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/voc_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/conversion/converters/yolo_converter.py` & `coretex-0.0.9/src/coretex/coretex/conversion/converters/yolo_converter.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/dataset.py` & `coretex-0.0.9/src/coretex/coretex/dataset/dataset.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/base.py` & `coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/base.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/image_dataset.py` & `coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/image_dataset.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/local_image_dataset.py` & `coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/local_image_dataset.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/image_dataset/synthetic_image_generator.py` & `coretex-0.0.9/src/coretex/coretex/dataset/image_dataset/synthetic_image_generator.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/local_dataset.py` & `coretex-0.0.9/src/coretex/coretex/dataset/local_dataset.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/dataset/network_dataset.py` & `coretex-0.0.9/src/coretex/coretex/dataset/network_dataset.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/experiment/artifact.py` & `coretex-0.0.9/src/coretex/coretex/experiment/artifact.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/experiment/experiment.py` & `coretex-0.0.9/src/coretex/coretex/experiment/experiment.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/experiment/status.py` & `coretex-0.0.9/src/coretex/coretex/experiment/status.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/custom_item/custom_item.py` & `coretex-0.0.9/src/coretex/coretex/item/custom_item/custom_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/image_item/image_item.py` & `coretex-0.0.9/src/coretex/coretex/item/image_item/image_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/image_item/image_item_data.py` & `coretex-0.0.9/src/coretex/coretex/item/image_item/image_item_data.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/image_item/local_image_item.py` & `coretex-0.0.9/src/coretex/coretex/item/image_item/local_image_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/image_segmentation_item/image_segmentation_item.py` & `coretex-0.0.9/src/coretex/coretex/item/image_segmentation_item/image_segmentation_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/item.py` & `coretex-0.0.9/src/coretex/coretex/item/item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/local_item.py` & `coretex-0.0.9/src/coretex/coretex/item/local_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/network_item.py` & `coretex-0.0.9/src/coretex/coretex/item/network_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/item/object_detection_item/object_detection_item.py` & `coretex-0.0.9/src/coretex/coretex/item/object_detection_item/object_detection_item.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/model/model.py` & `coretex-0.0.9/src/coretex/coretex/model/model.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/project/base.py` & `coretex-0.0.9/src/coretex/coretex/project/base.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/project/project.py` & `coretex-0.0.9/src/coretex/coretex/project/project.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/coretex/project/workspace.py` & `coretex-0.0.9/src/coretex/coretex/project/workspace.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/folder_management/folder_manager.py` & `coretex-0.0.9/src/coretex/folder_management/folder_manager.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/logging/log.py` & `coretex-0.0.9/src/coretex/logging/log.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/logging/log_severity.py` & `coretex-0.0.9/src/coretex/logging/log_severity.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/logging/logger.py` & `coretex-0.0.9/src/coretex/logging/logger.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/networking/network_manager.py` & `coretex-0.0.9/src/coretex/networking/network_manager.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/networking/network_object.py` & `coretex-0.0.9/src/coretex/networking/network_object.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/networking/network_response.py` & `coretex-0.0.9/src/coretex/networking/network_response.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/networking/requests_manager.py` & `coretex-0.0.9/src/coretex/networking/requests_manager.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/qiime2/__init__.py` & `coretex-0.0.9/src/coretex/qiime2/__init__.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/threading/threaded_data_processor.py` & `coretex-0.0.9/src/coretex/threading/threaded_data_processor.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/utils/console_progress_bar.py` & `coretex-0.0.9/src/coretex/utils/console_progress_bar.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/utils/file.py` & `coretex-0.0.9/src/coretex/utils/file.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/workspace/__init__.py` & `coretex-0.0.9/src/coretex/workspace/__init__.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/workspace/base.py` & `coretex-0.0.9/src/coretex/workspace/base.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/workspace/heartbeat.py` & `coretex-0.0.9/src/coretex/workspace/heartbeat.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/workspace/local.py` & `coretex-0.0.9/src/coretex/workspace/local.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex/workspace/remote.py` & `coretex-0.0.9/src/coretex/workspace/remote.py`

 * *Files identical despite different names*

### Comparing `coretex-0.0.8/src/coretex.egg-info/PKG-INFO` & `coretex-0.0.9/src/coretex.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coretex
-Version: 0.0.8
+Version: 0.0.9
 Summary: A package for AI experiment tracking, infrastructure and dataset management using Coretex.ai platform.
 Author-email: Igor Perić <igor@coretex.ai>
 Maintainer-email: Duško Mirković <dmirkovic@coretex.ai>, Alex Maslennikov <alex@coretex.ai>, Jovica Zarić <jzaric@coretex.ai>, Darko Zarić <dzaric@coretex.ai>, Bogdan Tintor <btintor@coretex.ai>, Igor Perić <igor@coretex.ai>
 Project-URL: Homepage, https://coretex.ai
 Project-URL: Documentation, https://docs.coretex.ai/1.0.0/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `coretex-0.0.8/src/coretex.egg-info/SOURCES.txt` & `coretex-0.0.9/src/coretex.egg-info/SOURCES.txt`

 * *Files identical despite different names*

