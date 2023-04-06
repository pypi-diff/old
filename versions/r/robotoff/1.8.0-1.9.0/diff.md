# Comparing `tmp/robotoff-1.8.0.tar.gz` & `tmp/robotoff-1.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "robotoff-1.8.0.tar", max compression
+gzip compressed data, was "robotoff-1.9.0.tar", max compression
```

## Comparing `robotoff-1.8.0.tar` & `robotoff-1.9.0.tar`

### file list

```diff
@@ -1,111 +1,111 @@
--rw-r--r--   0        0        0     2468 2022-10-12 09:36:03.788264 robotoff-1.8.0/pyproject.toml
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.788264 robotoff-1.8.0/robotoff/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.788264 robotoff-1.8.0/robotoff/app/__init__.py
--rw-r--r--   0        0        0    46940 2022-10-12 09:36:03.788264 robotoff-1.8.0/robotoff/app/api.py
--rw-r--r--   0        0        0     1363 2022-10-12 09:36:03.788264 robotoff-1.8.0/robotoff/app/auth.py
--rw-r--r--   0        0        0    11985 2022-10-12 09:36:03.788264 robotoff-1.8.0/robotoff/app/core.py
--rw-r--r--   0        0        0     1561 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/app/events.py
--rw-r--r--   0        0        0      286 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/app/middleware.py
--rw-r--r--   0        0        0     2645 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/app/schema.py
--rw-r--r--   0        0        0     4519 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/brands.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/__init__.py
--rw-r--r--   0        0        0     3821 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/annotate.py
--rw-r--r--   0        0        0     1564 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/batch.py
--rw-r--r--   0        0        0     1124 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/file.py
--rw-r--r--   0        0        0     5529 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/insights.py
--rw-r--r--   0        0        0     2230 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/logos.py
--rw-r--r--   0        0        0    11722 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/main.py
--rw-r--r--   0        0        0      711 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/run.py
--rw-r--r--   0        0        0     2811 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/cli/spellcheck.py
--rw-r--r--   0        0        0      124 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/category/__init__.py
--rw-r--r--   0        0        0      852 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/category/dump.py
--rw-r--r--   0        0        0     1891 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/category/match.py
--rw-r--r--   0        0        0     3123 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/category/predict.py
--rw-r--r--   0        0        0     1822 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/category/preprocessing.py
--rw-r--r--   0        0        0     2633 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/export.py
--rw-r--r--   0        0        0     4173 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/index/category_index.json
--rw-r--r--   0        0        0     1080 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/index/product_index.json
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/product/__init__.py
--rw-r--r--   0        0        0     1653 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/elasticsearch/product/dump.py
--rw-r--r--   0        0        0     2209 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/health.py
--rw-r--r--   0        0        0       62 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/_enum.py
--rw-r--r--   0        0        0    15865 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/annotate.py
--rw-r--r--   0        0        0     3989 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/dataclass.py
--rw-r--r--   0        0        0     4914 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/extraction.py
--rw-r--r--   0        0        0    36169 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/importer.py
--rw-r--r--   0        0        0      340 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/normalize.py
--rw-r--r--   0        0        0    10525 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/insights/question.py
--rw-r--r--   0        0        0      145 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/logo_label_type.py
--rw-r--r--   0        0        0    10392 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/logos.py
--rw-r--r--   0        0        0     4653 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/metrics.py
--rw-r--r--   0        0        0    11924 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/models.py
--rw-r--r--   0        0        0      271 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/mongo.py
--rw-r--r--   0        0        0    14703 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/off.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/category/__init__.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/category/neural/__init__.py
--rw-r--r--   0        0        0     5056 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/category/neural/category_classifier.py
--rw-r--r--   0        0        0     1998 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/langid.py
--rw-r--r--   0        0        0       88 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/__init__.py
--rw-r--r--   0        0        0     5979 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/core.py
--rw-r--r--   0        0        0     2453 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/download.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/utils/__init__.py
--rw-r--r--   0        0        0     6527 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/utils/label_map_util.py
--rw-r--r--   0        0        0      724 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/utils/string_int_label_map.proto
--rw-r--r--   0        0        0     5211 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/utils/string_int_label_map_pb2.py
--rw-r--r--   0        0        0    21484 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/object_detection/utils/visualization_utils.py
--rw-r--r--   0        0        0       96 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/__init__.py
--rw-r--r--   0        0        0     3587 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/brand.py
--rw-r--r--   0        0        0     3762 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/category.py
--rw-r--r--   0        0        0     6640 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/core.py
--rw-r--r--   0        0        0    20838 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/dataclass.py
--rw-r--r--   0        0        0     2368 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/expiration_date.py
--rw-r--r--   0        0        0     3508 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/image_flag.py
--rw-r--r--   0        0        0      736 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/image_lang.py
--rw-r--r--   0        0        0     1171 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/image_orientation.py
--rw-r--r--   0        0        0     9677 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/label.py
--rw-r--r--   0        0        0     9977 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/location.py
--rw-r--r--   0        0        0     6511 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/nutrient.py
--rw-r--r--   0        0        0     6914 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/packager_code.py
--rw-r--r--   0        0        0     1547 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/packaging.py
--rw-r--r--   0        0        0     8465 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/product_weight.py
--rw-r--r--   0        0        0     2119 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/store.py
--rw-r--r--   0        0        0     1828 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/trace.py
--rw-r--r--   0        0        0      721 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/ocr/utils.py
--rw-r--r--   0        0        0     1587 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/prediction/types.py
--rw-r--r--   0        0        0    14731 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/products.py
--rw-r--r--   0        0        0    10065 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/scheduler/__init__.py
--rw-r--r--   0        0        0     7489 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/scheduler/latent.py
--rw-r--r--   0        0        0    10506 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/settings.py
--rw-r--r--   0        0        0    11922 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/slack.py
--rw-r--r--   0        0        0     4210 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/spellcheck/__init__.py
--rw-r--r--   0        0        0      748 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/spellcheck/base_spellchecker.py
--rw-r--r--   0        0        0     2809 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/spellcheck/elasticsearch/__init__.py
--rw-r--r--   0        0        0     1602 2022-10-12 09:36:03.792264 robotoff-1.8.0/robotoff/spellcheck/elasticsearch/correction_formatter.py
--rw-r--r--   0        0        0     3095 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/elasticsearch/es_handler.py
--rw-r--r--   0        0        0      188 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/exceptions.py
--rw-r--r--   0        0        0     8340 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/items.py
--rw-r--r--   0        0        0     2057 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/patterns/__init__.py
--rw-r--r--   0        0        0     4778 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/percentages/__init__.py
--rw-r--r--   0        0        0      416 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/utils.py
--rw-r--r--   0        0        0     1568 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/vocabulary/__init__.py
--rw-r--r--   0        0        0     5626 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/spellcheck/vocabulary/utils.py
--rw-r--r--   0        0        0    11309 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/taxonomy.py
--rw-r--r--   0        0        0     4626 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/__init__.py
--rw-r--r--   0        0        0     1219 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/cache.py
--rw-r--r--   0        0        0     1194 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/es.py
--rw-r--r--   0        0        0    26539 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/fold_to_ascii.py
--rw-r--r--   0        0        0      852 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/i18n.py
--rw-r--r--   0        0        0     1488 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/text.py
--rw-r--r--   0        0        0      165 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/utils/types.py
--rw-r--r--   0        0        0        0 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/__init__.py
--rw-r--r--   0        0        0      605 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/client.py
--rw-r--r--   0        0        0     1953 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/listener.py
--rw-r--r--   0        0        0     3487 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/tasks/__init__.py
--rw-r--r--   0        0        0     6279 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/tasks/import_image.py
--rw-r--r--   0        0        0     3500 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/tasks/product_updated.py
--rw-r--r--   0        0        0     4963 2022-10-12 09:36:03.796264 robotoff-1.8.0/robotoff/workers/tasks/update_recycle.py
--rw-r--r--   0        0        0     2118 2022-10-12 09:36:14.752866 robotoff-1.8.0/setup.py
--rw-r--r--   0        0        0     1617 2022-10-12 09:36:14.753283 robotoff-1.8.0/PKG-INFO
+-rw-r--r--   0        0        0     2468 2022-10-17 10:52:08.204024 robotoff-1.9.0/pyproject.toml
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/__init__.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/__init__.py
+-rw-r--r--   0        0        0    47420 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/api.py
+-rw-r--r--   0        0        0     1363 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/auth.py
+-rw-r--r--   0        0        0    11985 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/core.py
+-rw-r--r--   0        0        0     1561 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/events.py
+-rw-r--r--   0        0        0      286 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/middleware.py
+-rw-r--r--   0        0        0     3778 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/app/schema.py
+-rw-r--r--   0        0        0     4519 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/brands.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/__init__.py
+-rw-r--r--   0        0        0     3821 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/annotate.py
+-rw-r--r--   0        0        0     1564 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/batch.py
+-rw-r--r--   0        0        0     1124 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/file.py
+-rw-r--r--   0        0        0     5529 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/insights.py
+-rw-r--r--   0        0        0     2230 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/logos.py
+-rw-r--r--   0        0        0    11722 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/main.py
+-rw-r--r--   0        0        0      711 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/run.py
+-rw-r--r--   0        0        0     2811 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/cli/spellcheck.py
+-rw-r--r--   0        0        0      124 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/__init__.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/category/__init__.py
+-rw-r--r--   0        0        0      852 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/category/dump.py
+-rw-r--r--   0        0        0     1891 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/category/match.py
+-rw-r--r--   0        0        0     3123 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/category/predict.py
+-rw-r--r--   0        0        0     1822 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/category/preprocessing.py
+-rw-r--r--   0        0        0     2633 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/export.py
+-rw-r--r--   0        0        0     4173 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/index/category_index.json
+-rw-r--r--   0        0        0     1080 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/index/product_index.json
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/product/__init__.py
+-rw-r--r--   0        0        0     1653 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/elasticsearch/product/dump.py
+-rw-r--r--   0        0        0     2209 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/health.py
+-rw-r--r--   0        0        0       62 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/__init__.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/_enum.py
+-rw-r--r--   0        0        0    15865 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/annotate.py
+-rw-r--r--   0        0        0     3989 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/dataclass.py
+-rw-r--r--   0        0        0     4914 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/extraction.py
+-rw-r--r--   0        0        0    36169 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/importer.py
+-rw-r--r--   0        0        0      340 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/normalize.py
+-rw-r--r--   0        0        0    12572 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/insights/question.py
+-rw-r--r--   0        0        0      145 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/logo_label_type.py
+-rw-r--r--   0        0        0    10392 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/logos.py
+-rw-r--r--   0        0        0     4653 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/metrics.py
+-rw-r--r--   0        0        0    11924 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/models.py
+-rw-r--r--   0        0        0      271 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/mongo.py
+-rw-r--r--   0        0        0    14703 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/off.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/prediction/__init__.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.204024 robotoff-1.9.0/robotoff/prediction/category/__init__.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/category/neural/__init__.py
+-rw-r--r--   0        0        0     5056 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/category/neural/category_classifier.py
+-rw-r--r--   0        0        0     1998 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/langid.py
+-rw-r--r--   0        0        0       88 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/__init__.py
+-rw-r--r--   0        0        0     5979 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/core.py
+-rw-r--r--   0        0        0     2453 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/download.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/utils/__init__.py
+-rw-r--r--   0        0        0     6543 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/utils/label_map_util.py
+-rw-r--r--   0        0        0      724 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/utils/string_int_label_map.proto
+-rw-r--r--   0        0        0     5226 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/utils/string_int_label_map_pb2.py
+-rw-r--r--   0        0        0    21484 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/object_detection/utils/visualization_utils.py
+-rw-r--r--   0        0        0       96 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/__init__.py
+-rw-r--r--   0        0        0     3587 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/brand.py
+-rw-r--r--   0        0        0     3762 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/category.py
+-rw-r--r--   0        0        0     6640 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/core.py
+-rw-r--r--   0        0        0    20838 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/dataclass.py
+-rw-r--r--   0        0        0     2368 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/expiration_date.py
+-rw-r--r--   0        0        0     3508 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/image_flag.py
+-rw-r--r--   0        0        0      736 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/image_lang.py
+-rw-r--r--   0        0        0     1171 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/image_orientation.py
+-rw-r--r--   0        0        0     9677 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/label.py
+-rw-r--r--   0        0        0     9977 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/location.py
+-rw-r--r--   0        0        0     6511 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/nutrient.py
+-rw-r--r--   0        0        0     6914 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/packager_code.py
+-rw-r--r--   0        0        0     1547 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/packaging.py
+-rw-r--r--   0        0        0     8465 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/product_weight.py
+-rw-r--r--   0        0        0     2119 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/store.py
+-rw-r--r--   0        0        0     1828 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/trace.py
+-rw-r--r--   0        0        0      721 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/ocr/utils.py
+-rw-r--r--   0        0        0     1587 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/prediction/types.py
+-rw-r--r--   0        0        0    14731 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/products.py
+-rw-r--r--   0        0        0    10065 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/scheduler/__init__.py
+-rw-r--r--   0        0        0     7489 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/scheduler/latent.py
+-rw-r--r--   0        0        0    10518 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/settings.py
+-rw-r--r--   0        0        0    11922 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/slack.py
+-rw-r--r--   0        0        0     4210 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/__init__.py
+-rw-r--r--   0        0        0      748 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/base_spellchecker.py
+-rw-r--r--   0        0        0     2809 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/elasticsearch/__init__.py
+-rw-r--r--   0        0        0     1602 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/elasticsearch/correction_formatter.py
+-rw-r--r--   0        0        0     3095 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/elasticsearch/es_handler.py
+-rw-r--r--   0        0        0      188 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/exceptions.py
+-rw-r--r--   0        0        0     8340 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/items.py
+-rw-r--r--   0        0        0     2057 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/patterns/__init__.py
+-rw-r--r--   0        0        0     4778 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/percentages/__init__.py
+-rw-r--r--   0        0        0      416 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/utils.py
+-rw-r--r--   0        0        0     1568 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/vocabulary/__init__.py
+-rw-r--r--   0        0        0     5626 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/spellcheck/vocabulary/utils.py
+-rw-r--r--   0        0        0    12384 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/taxonomy.py
+-rw-r--r--   0        0        0     5575 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/__init__.py
+-rw-r--r--   0        0        0     1218 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/cache.py
+-rw-r--r--   0        0        0     1194 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/es.py
+-rw-r--r--   0        0        0    26539 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/fold_to_ascii.py
+-rw-r--r--   0        0        0      852 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/i18n.py
+-rw-r--r--   0        0        0     1488 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/text.py
+-rw-r--r--   0        0        0      165 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/utils/types.py
+-rw-r--r--   0        0        0        0 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/__init__.py
+-rw-r--r--   0        0        0      605 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/client.py
+-rw-r--r--   0        0        0     1953 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/listener.py
+-rw-r--r--   0        0        0     3487 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/tasks/__init__.py
+-rw-r--r--   0        0        0     6279 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/tasks/import_image.py
+-rw-r--r--   0        0        0     3500 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/tasks/product_updated.py
+-rw-r--r--   0        0        0     4963 2022-10-17 10:52:08.208024 robotoff-1.9.0/robotoff/workers/tasks/update_recycle.py
+-rw-r--r--   0        0        0     2118 2022-10-17 10:52:15.653242 robotoff-1.9.0/setup.py
+-rw-r--r--   0        0        0     1617 2022-10-17 10:52:15.653613 robotoff-1.9.0/PKG-INFO
```

### Comparing `robotoff-1.8.0/pyproject.toml` & `robotoff-1.9.0/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -34,15 +34,15 @@
 line_length = 88
 
 [tool.mypy]
 ignore_missing_imports = true
 
 [tool.poetry]
 name = "robotoff"
-version = "1.8.0"
+version = "1.9.0"
 description = "Real-time and batch prediction service for Openfoodfacts."
 authors = ["Openfoodfacts Team"]
 license = "GNU Affero General Public License v3"
 
 [tool.poetry.dependencies]
 python = "^3.7"
 requests = "~2.27.1"
```

### Comparing `robotoff-1.8.0/robotoff/app/api.py` & `robotoff-1.9.0/robotoff/app/api.py`

 * *Files 1% similar despite different names*

```diff
@@ -52,15 +52,15 @@
 )
 from robotoff.prediction.category.neural.category_classifier import CategoryClassifier
 from robotoff.prediction.object_detection import ObjectDetectionModelRegistry
 from robotoff.prediction.ocr.dataclass import OCRParsingException
 from robotoff.prediction.types import PredictionType
 from robotoff.products import get_product_dataset_etag
 from robotoff.spellcheck import SPELLCHECKERS, Spellchecker
-from robotoff.taxonomy import TaxonomyType, get_taxonomy, match_unprefixed_value
+from robotoff.taxonomy import TaxonomyType, get_taxonomy, match_taxonomized_value
 from robotoff.utils import get_image_from_url, get_logger, http_session
 from robotoff.utils.es import get_es_client
 from robotoff.utils.i18n import TranslationStore
 from robotoff.utils.text import get_tag
 from robotoff.utils.types import JSONType
 from robotoff.workers.client import send_ipc_event
 
@@ -618,34 +618,47 @@
     resp.stream_len = fp.tell()
     fp.seek(0)
     resp.stream = fp
 
 
 class ImageLogoResource:
     def on_get(self, req: falcon.Request, resp: falcon.Response):
-        logo_ids: Optional[List[str]] = req.get_param_as_list(
-            "logo_ids", required=False
-        )
+        logo_ids: List[str] = req.get_param_as_list("logo_ids", required=True)
+        logos = []
+        for logo in (
+            LogoAnnotation.select()
+            .join(ImagePrediction)
+            .join(ImageModel)
+            .where(LogoAnnotation.id.in_(logo_ids))
+            .iterator()
+        ):
+            logo_dict = logo.to_dict()
+            image_prediction = logo_dict.pop("image_prediction")
+            logo_dict["image"] = image_prediction["image"]
+            logos.append(logo_dict)
+
+        resp.media = {"logos": logos, "count": len(logos)}
 
-        if logo_ids is not None:
-            self.fetch_logos(logo_ids, resp)
-        else:
-            self.search(req, resp)
 
-    def search(self, req: falcon.Request, resp: falcon.Response):
+class ImageLogoSearchResource:
+    def on_get(self, req: falcon.Request, resp: falcon.Response):
         count: int = req.get_param_as_int(
             "count", min_value=1, max_value=2000, default=25
         )
         type_: Optional[str] = req.get_param("type")
         barcode: Optional[str] = req.get_param("barcode")
         value: Optional[str] = req.get_param("value")
         min_confidence: Optional[float] = req.get_param_as_float("min_confidence")
         random: bool = req.get_param_as_bool("random", default=False)
         server_domain: Optional[str] = req.get_param("server_domain")
-        annotated: bool = req.get_param_as_bool("annotated", default=False)
+        annotated: Optional[bool] = req.get_param_as_bool("annotated")
+
+        where_clauses = []
+        if annotated is not None:
+            where_clauses.append(LogoAnnotation.annotation_value.is_null(not annotated))
 
         where_clauses = [LogoAnnotation.annotation_value.is_null(not annotated)]
         join_image_prediction = False
         join_image_model = False
 
         if server_domain:
             where_clauses.append(ImageModel.server_domain == server_domain)
@@ -690,30 +703,14 @@
 
         for item in items:
             image_prediction = item.pop("image_prediction")
             item["image"] = image_prediction["image"]
 
         resp.media = {"logos": items, "count": query_count}
 
-    def fetch_logos(self, logo_ids: List[str], resp: falcon.Response):
-        logos = []
-        for logo in (
-            LogoAnnotation.select()
-            .join(ImagePrediction)
-            .join(ImageModel)
-            .where(LogoAnnotation.id.in_(logo_ids))
-            .iterator()
-        ):
-            logo_dict = logo.to_dict()
-            image_prediction = logo_dict.pop("image_prediction")
-            logo_dict["image"] = image_prediction["image"]
-            logos.append(logo_dict)
-
-        resp.media = {"logos": logos, "count": len(logos)}
-
 
 class ImageLogoDetailResource:
     def on_get(self, req: falcon.Request, resp: falcon.Response, logo_id: int):
         logo = LogoAnnotation.get_or_none(id=logo_id)
 
         if logo is None:
             resp.status = falcon.HTTP_404
@@ -742,15 +739,15 @@
 
         if value != logo.annotation_value:
             logo.annotation_value = value
 
             if value is not None:
                 value_tag = get_tag(value)
                 logo.annotation_value_tag = value_tag
-                logo.taxonomy_value = match_unprefixed_value(value_tag, type_)
+                logo.taxonomy_value = match_taxonomized_value(value_tag, type_)
             else:
                 logo.annotation_value_tag = None
                 logo.taxonomy_value = None
 
             updated = True
 
         if updated:
@@ -760,39 +757,50 @@
             logo.completed_at = datetime.datetime.utcnow()
             logo.save()
 
         resp.status = falcon.HTTP_204
 
 
 class ImageLogoAnnotateResource:
+    @jsonschema.validate(schema.ANNOTATE_LOGO_SCHEMA)
     def on_post(self, req: falcon.Request, resp: falcon.Response):
         server_domain = req.media.get("server_domain", settings.OFF_SERVER_DOMAIN)
         annotations = req.media["annotations"]
         auth = parse_auth(req)
         username = None if auth is None else auth.get_username()
         completed_at = datetime.datetime.utcnow()
         annotated_logos = []
 
         for annotation in annotations:
             logo_id = annotation["logo_id"]
             type_ = annotation["type"]
             value = annotation["value"] or None
-            logo = LogoAnnotation.get_by_id(logo_id)
+            try:
+                logo = LogoAnnotation.get_by_id(logo_id)
+            except LogoAnnotation.DoesNotExist:
+                raise falcon.HTTPNotFound(description=f"logo {logo_id} not found")
+
             if value is not None:
                 logo.annotation_value = value
                 value_tag = get_tag(value)
                 logo.annotation_value_tag = value_tag
-                logo.taxonomy_value = match_unprefixed_value(value_tag, type_)
+                logo.taxonomy_value = match_taxonomized_value(value_tag, type_)
+            elif type_ in ("brand", "category", "label", "store"):
+                raise falcon.HTTPBadRequest(
+                    description=f"value required for type {type_} (logo {logo_id})"
+                )
 
             logo.annotation_type = type_
             logo.username = username
             logo.completed_at = completed_at
-            logo.save()
             annotated_logos.append(logo)
 
+        for logo in annotated_logos:
+            logo.save()
+
         created = generate_insights_from_annotated_logos(annotated_logos, server_domain)
         resp.media = {"created insights": created}
 
 
 class ImageLogoUpdateResource:
     def on_post(self, req: falcon.Request, resp: falcon.Response):
         """Bulk update logo annotations: change type and value of logos that have specific
@@ -806,15 +814,15 @@
 
         auth = parse_auth(req)
         username = None if auth is None else auth.get_username()
         completed_at = datetime.datetime.utcnow()
 
         target_value_tag = get_tag(target_value)
         source_value_tag = get_tag(source_value)
-        taxonomy_value = match_unprefixed_value(target_value_tag, target_type)
+        taxonomy_value = match_taxonomized_value(target_value_tag, target_type)
 
         query = LogoAnnotation.update(
             {
                 LogoAnnotation.annotation_type: target_type,
                 LogoAnnotation.annotation_value: target_value,
                 LogoAnnotation.annotation_value_tag: target_value_tag,
                 LogoAnnotation.taxonomy_value: taxonomy_value,
@@ -1315,14 +1323,15 @@
 api.add_route("/api/v1/webhook/product", WebhookProductResource())
 api.add_route("/api/v1/images/import", ImageImporterResource())
 api.add_route("/api/v1/images/crop", ImageCropResource())
 api.add_route("/api/v1/images/predictions/import", ImagePredictionImporterResource())
 api.add_route("/api/v1/images/predictions", ImagePredictionFetchResource())
 api.add_route("/api/v1/images/predict", ImagePredictorResource())
 api.add_route("/api/v1/images/logos", ImageLogoResource())
+api.add_route("/api/v1/images/logos/search", ImageLogoSearchResource())
 api.add_route("/api/v1/images/logos/{logo_id:int}", ImageLogoDetailResource())
 api.add_route("/api/v1/images/logos/annotate", ImageLogoAnnotateResource())
 api.add_route("/api/v1/images/logos/update", ImageLogoUpdateResource())
 api.add_route("/api/v1/questions/{barcode}", ProductQuestionsResource())
 api.add_route("/api/v1/questions/random", RandomQuestionsResource())
 api.add_route("/api/v1/questions/popular", PopularQuestionsResource())
 api.add_route("/api/v1/questions/unanswered", UnansweredQuestionCollection())
```

### Comparing `robotoff-1.8.0/robotoff/app/auth.py` & `robotoff-1.9.0/robotoff/app/auth.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/app/core.py` & `robotoff-1.9.0/robotoff/app/core.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/app/events.py` & `robotoff-1.9.0/robotoff/app/events.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/app/schema.py` & `robotoff-1.9.0/robotoff/app/schema.py`

 * *Files 25% similar despite different names*

```diff
@@ -81,7 +81,44 @@
                 },
                 "threshold": {"type": "number"},
             },
             "required": ["product"],
         },
     ],
 }
+
+
+ANNOTATE_LOGO_SCHEMA: JSONType = {
+    "$schema": "http://json-schema.org/draft-07/schema#",
+    "title": "Annotate Logo",
+    "type": "object",
+    "properties": {
+        "annotations": {
+            "type": "array",
+            "items": {
+                "type": "object",
+                "properties": {
+                    "value": {
+                        "type": ["string", "null"],
+                    },
+                    "type": {
+                        "type": "string",
+                        "enum": [
+                            "brand",
+                            "category",
+                            "label",
+                            "no_logo",
+                            "nutritional_label",
+                            "packager_code",
+                            "packaging",
+                            "qr_code",
+                            "store",
+                        ],
+                    },
+                    "logo_id": {"type": "integer"},
+                },
+                "required": ["value", "type", "logo_id"],
+            },
+        },
+    },
+    "required": ["annotations"],
+}
```

### Comparing `robotoff-1.8.0/robotoff/brands.py` & `robotoff-1.9.0/robotoff/brands.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/annotate.py` & `robotoff-1.9.0/robotoff/cli/annotate.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/batch.py` & `robotoff-1.9.0/robotoff/cli/batch.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/file.py` & `robotoff-1.9.0/robotoff/cli/file.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/insights.py` & `robotoff-1.9.0/robotoff/cli/insights.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/logos.py` & `robotoff-1.9.0/robotoff/cli/logos.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/main.py` & `robotoff-1.9.0/robotoff/cli/main.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/run.py` & `robotoff-1.9.0/robotoff/cli/run.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/cli/spellcheck.py` & `robotoff-1.9.0/robotoff/cli/spellcheck.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/category/dump.py` & `robotoff-1.9.0/robotoff/elasticsearch/category/dump.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/category/match.py` & `robotoff-1.9.0/robotoff/elasticsearch/category/match.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/category/predict.py` & `robotoff-1.9.0/robotoff/elasticsearch/category/predict.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/category/preprocessing.py` & `robotoff-1.9.0/robotoff/elasticsearch/category/preprocessing.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/export.py` & `robotoff-1.9.0/robotoff/elasticsearch/export.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/index/category_index.json` & `robotoff-1.9.0/robotoff/elasticsearch/index/category_index.json`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/index/product_index.json` & `robotoff-1.9.0/robotoff/elasticsearch/index/product_index.json`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/elasticsearch/product/dump.py` & `robotoff-1.9.0/robotoff/elasticsearch/product/dump.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/health.py` & `robotoff-1.9.0/robotoff/health.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/insights/annotate.py` & `robotoff-1.9.0/robotoff/insights/annotate.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/insights/dataclass.py` & `robotoff-1.9.0/robotoff/insights/dataclass.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/insights/extraction.py` & `robotoff-1.9.0/robotoff/insights/extraction.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/insights/importer.py` & `robotoff-1.9.0/robotoff/insights/importer.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/insights/question.py` & `robotoff-1.9.0/robotoff/insights/question.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,22 +2,27 @@
 import pathlib
 from typing import Dict, List, Optional
 
 from robotoff import settings
 from robotoff.insights import InsightType
 from robotoff.models import ProductInsight
 from robotoff.mongo import MONGO_CLIENT_CACHE
-from robotoff.off import generate_image_url, get_product
+from robotoff.off import generate_image_url
+from robotoff.products import get_product
 from robotoff.taxonomy import Taxonomy, TaxonomyType, get_taxonomy
 from robotoff.utils import get_logger
 from robotoff.utils.i18n import TranslationStore
 from robotoff.utils.types import JSONType
 
 logger = get_logger(__name__)
 
+DISPLAY_IMAGE_SIZE = 400
+SMALL_IMAGE_SIZE = 200
+THUMB_IMAGE_SIZE = 100
+
 
 LABEL_IMG_BASE_URL = "https://{}/images/lang".format(
     settings.BaseURLProvider().static().get()
 )
 
 LABEL_IMAGES = {
     "en:eu-organic": LABEL_IMG_BASE_URL + "/en/labels/eu-organic.135x90.svg",
@@ -138,36 +143,81 @@
             value_tag=insight.value_tag,
             insight=insight,
             source_image_url=source_image_url,
         )
 
     @staticmethod
     def get_source_image_url(barcode: str) -> Optional[str]:
-        product: Optional[JSONType] = get_product(barcode, fields=["selected_images"])
-
-        if product is None:
-            return None
+        product: Optional[JSONType] = get_product(barcode)
 
-        if "selected_images" not in product:
+        if product is None or "images" not in product:
             return None
 
-        selected_images = product["selected_images"]
+        selected_images = CategoryQuestionFormatter.generate_selected_images(
+            product["images"], barcode
+        )
 
         for key in ("front", "ingredients", "nutrition"):
             if key in selected_images:
                 images = selected_images[key]
 
                 if "display" in images:
                     display_images = list(images["display"].values())
 
                     if display_images:
                         return display_images[0]
 
         return None
 
+    @staticmethod
+    def generate_selected_images(
+        images: JSONType, barcode: str
+    ) -> Dict[str, Dict[str, Dict[str, str]]]:
+        """Generate the same `selected_images` field as returned by Product
+        Opener API.
+
+        :param images: the `images` data of the product
+        :param barcode: the product barcode
+        :return: the `selected_images` data
+        """
+        selected_images: Dict[str, Dict[str, Dict[str, str]]] = {
+            image_type: {}
+            for image_type in ("front", "nutrition", "ingredients", "packaging")
+        }
+
+        for key, image_data in images.items():
+            if (
+                key.startswith("front_")
+                or key.startswith("nutrition_")
+                or key.startswith("ingredients_")
+                or key.startswith("packaging_")
+            ):
+                image_type = key.split("_")[
+                    0
+                ]  # to get image type: `front`, `nutrition`, `ingredients` or `packaging`
+                language = key.split("_")[1]  # splitting to get the language name
+                revision_id = image_data["rev"]  # get revision_id for all languages
+                available_image_sizes = set(
+                    int(size) for size in image_data["sizes"] if size.isdigit()
+                )
+
+                for field_name, image_size in (
+                    ("display", DISPLAY_IMAGE_SIZE),
+                    ("small", SMALL_IMAGE_SIZE),
+                    ("thumb", THUMB_IMAGE_SIZE),
+                ):
+                    if image_size in available_image_sizes:
+                        image_url = generate_image_url(
+                            barcode, f"{key}.{revision_id}.{image_size}"
+                        )
+                        selected_images[image_type].setdefault(field_name, {})
+                        selected_images[image_type][field_name][language] = image_url
+
+        return selected_images
+
 
 class ProductWeightQuestionFormatter(QuestionFormatter):
     question = "Does this weight match the weight displayed on the product?"
 
     def format_question(self, insight: ProductInsight, lang: str) -> Question:
         localized_question = self.translation_store.gettext(lang, self.question)
```

### Comparing `robotoff-1.8.0/robotoff/logos.py` & `robotoff-1.9.0/robotoff/logos.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/metrics.py` & `robotoff-1.9.0/robotoff/metrics.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/models.py` & `robotoff-1.9.0/robotoff/models.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/off.py` & `robotoff-1.9.0/robotoff/off.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/category/neural/category_classifier.py` & `robotoff-1.9.0/robotoff/prediction/category/neural/category_classifier.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/langid.py` & `robotoff-1.9.0/robotoff/prediction/langid.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/core.py` & `robotoff-1.9.0/robotoff/prediction/object_detection/core.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/download.py` & `robotoff-1.9.0/robotoff/prediction/object_detection/download.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/utils/label_map_util.py` & `robotoff-1.9.0/robotoff/prediction/object_detection/utils/label_map_util.py`

 * *Files 1% similar despite different names*

```diff
@@ -137,15 +137,15 @@
     Args:
       path: path to StringIntLabelMap proto text file.
     Returns:
       a StringIntLabelMapProto
     """
     with open(path, "r") as fid:
         label_map_string = fid.read()
-        label_map = string_int_label_map_pb2.StringIntLabelMap()
+        label_map = string_int_label_map_pb2.StringIntLabelMap()  # type: ignore
         try:
             text_format.Merge(label_map_string, label_map)
         except text_format.ParseError:
             label_map.ParseFromString(label_map_string)
     _validate_label_map(label_map)
     return label_map
```

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/utils/string_int_label_map.proto` & `robotoff-1.9.0/robotoff/prediction/object_detection/utils/string_int_label_map.proto`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/utils/string_int_label_map_pb2.py` & `robotoff-1.9.0/robotoff/prediction/object_detection/utils/string_int_label_map_pb2.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
 # source: robotoff/ml/object_detection/utils/string_int_label_map.proto
+# type: ignore
 
 import sys
 
 _b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import descriptor_pb2
 from google.protobuf import message as _message
```

### Comparing `robotoff-1.8.0/robotoff/prediction/object_detection/utils/visualization_utils.py` & `robotoff-1.9.0/robotoff/prediction/object_detection/utils/visualization_utils.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/brand.py` & `robotoff-1.9.0/robotoff/prediction/ocr/brand.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/category.py` & `robotoff-1.9.0/robotoff/prediction/ocr/category.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/core.py` & `robotoff-1.9.0/robotoff/prediction/ocr/core.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/dataclass.py` & `robotoff-1.9.0/robotoff/prediction/ocr/dataclass.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/expiration_date.py` & `robotoff-1.9.0/robotoff/prediction/ocr/expiration_date.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/image_flag.py` & `robotoff-1.9.0/robotoff/prediction/ocr/image_flag.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/image_lang.py` & `robotoff-1.9.0/robotoff/prediction/ocr/image_lang.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/image_orientation.py` & `robotoff-1.9.0/robotoff/prediction/ocr/image_orientation.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/label.py` & `robotoff-1.9.0/robotoff/prediction/ocr/label.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/location.py` & `robotoff-1.9.0/robotoff/prediction/ocr/location.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/nutrient.py` & `robotoff-1.9.0/robotoff/prediction/ocr/nutrient.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/packager_code.py` & `robotoff-1.9.0/robotoff/prediction/ocr/packager_code.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/packaging.py` & `robotoff-1.9.0/robotoff/prediction/ocr/packaging.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/product_weight.py` & `robotoff-1.9.0/robotoff/prediction/ocr/product_weight.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/store.py` & `robotoff-1.9.0/robotoff/prediction/ocr/store.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/trace.py` & `robotoff-1.9.0/robotoff/prediction/ocr/trace.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/ocr/utils.py` & `robotoff-1.9.0/robotoff/prediction/ocr/utils.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/prediction/types.py` & `robotoff-1.9.0/robotoff/prediction/types.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/products.py` & `robotoff-1.9.0/robotoff/products.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/scheduler/__init__.py` & `robotoff-1.9.0/robotoff/scheduler/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/scheduler/latent.py` & `robotoff-1.9.0/robotoff/scheduler/latent.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/settings.py` & `robotoff-1.9.0/robotoff/settings.py`

 * *Files 2% similar despite different names*

```diff
@@ -116,18 +116,18 @@
 EVENTS_API_URL = os.environ.get(
     "EVENTS_API_URL", "https://events." + BaseURLProvider().domain
 )
 
 # Taxonomies are huge JSON files that describe many concepts in OFF, in many languages, with synonyms. Those are the full version of taxos.
 
 TAXONOMY_DIR = DATA_DIR / "taxonomies"
-TAXONOMY_CATEGORY_PATH = TAXONOMY_DIR / "categories.full.json"
-TAXONOMY_INGREDIENT_PATH = TAXONOMY_DIR / "ingredients.full.json"
-TAXONOMY_LABEL_PATH = TAXONOMY_DIR / "labels.full.json"
-TAXONOMY_BRAND_PATH = TAXONOMY_DIR / "brands.full.json"
+TAXONOMY_CATEGORY_PATH = TAXONOMY_DIR / "categories.full.json.gz"
+TAXONOMY_INGREDIENT_PATH = TAXONOMY_DIR / "ingredients.full.json.gz"
+TAXONOMY_LABEL_PATH = TAXONOMY_DIR / "labels.full.json.gz"
+TAXONOMY_BRAND_PATH = TAXONOMY_DIR / "brands.full.json.gz"
 INGREDIENTS_FR_PATH = TAXONOMY_DIR / "ingredients_fr.txt"
 INGREDIENT_TOKENS_PATH = TAXONOMY_DIR / "ingredients_tokens.txt"
 FR_TOKENS_PATH = TAXONOMY_DIR / "fr_tokens_lower.gz"
 
 # Spellchecking parameters. Wauplin and Raphael are the experts.
 
 SPELLCHECK_DIR = DATA_DIR / "spellcheck"
```

### Comparing `robotoff-1.8.0/robotoff/slack.py` & `robotoff-1.9.0/robotoff/slack.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/__init__.py` & `robotoff-1.9.0/robotoff/spellcheck/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/base_spellchecker.py` & `robotoff-1.9.0/robotoff/spellcheck/base_spellchecker.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/elasticsearch/__init__.py` & `robotoff-1.9.0/robotoff/spellcheck/elasticsearch/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/elasticsearch/correction_formatter.py` & `robotoff-1.9.0/robotoff/spellcheck/elasticsearch/correction_formatter.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/elasticsearch/es_handler.py` & `robotoff-1.9.0/robotoff/spellcheck/elasticsearch/es_handler.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/items.py` & `robotoff-1.9.0/robotoff/spellcheck/items.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/patterns/__init__.py` & `robotoff-1.9.0/robotoff/spellcheck/patterns/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/percentages/__init__.py` & `robotoff-1.9.0/robotoff/spellcheck/percentages/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/vocabulary/__init__.py` & `robotoff-1.9.0/robotoff/spellcheck/vocabulary/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/spellcheck/vocabulary/utils.py` & `robotoff-1.9.0/robotoff/spellcheck/vocabulary/utils.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/taxonomy.py` & `robotoff-1.9.0/robotoff/taxonomy.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 import collections
 import functools
 import pathlib
 from enum import Enum
 from typing import Any, Dict, Iterable, List, Optional, Set, Union
 
-import orjson
 import requests
 
 from robotoff import settings
-from robotoff.utils import get_logger, http_session
+from robotoff.utils import get_logger, http_session, load_json
 from robotoff.utils.cache import CachedStore
 from robotoff.utils.types import JSONType
 
 try:
     import networkx
 except ImportError:
     networkx = None
@@ -226,17 +225,15 @@
             parents = [taxonomy[ref] for ref in key_data.get("parents", [])]
             node.add_parents(parents)
 
         return taxonomy
 
     @classmethod
     def from_json(cls, file_path: Union[str, pathlib.Path]):
-        with open(str(file_path), "rb") as f:
-            data = orjson.loads(f.read())
-            return cls.from_dict(data)
+        return cls.from_dict(load_json(file_path, compressed=True))  # type: ignore
 
     def to_graph(self):
         """Generate a networkx.DiGraph from the taxonomy."""
         graph = networkx.DiGraph()
         graph.add_nodes_from((x.id for x in self.iter_nodes()))
 
         for node in self.iter_nodes():
@@ -301,36 +298,40 @@
 
 TAXONOMY_STORES: Dict[str, CachedStore] = {
     TaxonomyType.category.name: CachedStore(
         functools.partial(
             fetch_taxonomy,
             url=settings.TAXONOMY_CATEGORY_URL,
             fallback_path=settings.TAXONOMY_CATEGORY_PATH,
-        )
+        ),
+        expiration_interval=720,
     ),
     TaxonomyType.ingredient.name: CachedStore(
         functools.partial(
             fetch_taxonomy,
             url=settings.TAXONOMY_INGREDIENT_URL,
             fallback_path=settings.TAXONOMY_INGREDIENT_PATH,
-        )
+        ),
+        expiration_interval=720,
     ),
     TaxonomyType.label.name: CachedStore(
         functools.partial(
             fetch_taxonomy,
             url=settings.TAXONOMY_LABEL_URL,
             fallback_path=settings.TAXONOMY_LABEL_PATH,
-        )
+        ),
+        expiration_interval=720,
     ),
     TaxonomyType.brand.name: CachedStore(
         functools.partial(
             fetch_taxonomy,
             url=settings.TAXONOMY_BRAND_URL,
             fallback_path=settings.TAXONOMY_BRAND_PATH,
-        )
+        ),
+        expiration_interval=720,
     ),
 }
 
 
 def get_taxonomy(taxonomy_type: str, offline: bool = False) -> Taxonomy:
     """Returned the requested Taxonomy."""
     taxonomy_store = TAXONOMY_STORES.get(taxonomy_type)
@@ -371,14 +372,41 @@
             taxonomy_type=TaxonomyType.brand.name,
         )
     ),
 }
 
 
 def match_unprefixed_value(value_tag: str, taxonomy_type: str) -> Optional[str]:
+    """From an unprefixed `value_tag`, return the taxonomized value in the
+    taxonomy (if any) or return None if no match was found.
+
+    Currently this only works for labels and brands:
+    - for label, from unprefixed `value_tag` (ex: en-organic), we return the
+    prefixed label (ex: en:eu-organic)
+    - for brand, we return the correctly capitalize brand name
+    (ex: carrefour-bio -> Carrefour Bio), as Product Opener does not have a
+    brand taxonomy so far
+    """
     unprefixed_mapping_cache = UNPREFIXED_MAPPING_STORE.get(taxonomy_type)
 
     if unprefixed_mapping_cache is None:
         return None
 
     unprefixed_mapping = unprefixed_mapping_cache.get()
     return unprefixed_mapping.get(value_tag)
+
+
+def match_taxonomized_value(value_tag: str, taxonomy_type: str) -> Optional[str]:
+    """Return the taxonomized value of a `value_tag` (if any) or return
+    None if no match was found.
+
+    Currently it only works for brand and label.
+    """
+    if taxonomy_type not in (TaxonomyType.brand.name, TaxonomyType.label.name):
+        return None
+
+    taxonomy = get_taxonomy(taxonomy_type)
+
+    if value_tag in taxonomy:
+        return value_tag
+
+    return match_unprefixed_value(value_tag, taxonomy_type)
```

### Comparing `robotoff-1.8.0/robotoff/utils/__init__.py` & `robotoff-1.9.0/robotoff/utils/__init__.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import gzip
 import logging
 import os
 import pathlib
 import sys
 from io import BytesIO
-from typing import Any, Callable, Dict, Iterable, Optional, Union
+from typing import Any, Callable, Dict, Iterable, List, Optional, Union
 
 import orjson
 import PIL
 import requests
 from PIL import Image
 
 from robotoff import settings
@@ -67,14 +67,46 @@
 def jsonl_iter_fp(fp) -> Iterable[Dict]:
     for line in fp:
         line = line.strip("\n")
         if line:
             yield orjson.loads(line)
 
 
+def load_json(
+    path: Union[str, pathlib.Path], compressed: bool = False
+) -> Union[Dict, List]:
+    """Load a JSON file.
+
+    :param path: the path of the file
+    :param: compressed: if True, use gzip to decompress the file
+    :return: the unserialized JSON
+    """
+    if compressed:
+        with gzip.open(str(path), "rb") as f:
+            return orjson.loads(f.read())
+    else:
+        with open(str(path), "rb") as f:
+            return orjson.loads(f.read())
+
+
+def dump_json(path: Union[str, pathlib.Path], item: Any, compressed: bool = False):
+    """Dump an object in a JSON file.
+
+    :param path: the path of the file
+    :param item: the item to serialize
+    :param: compressed: if True, use gzip to compress the file
+    """
+    if compressed:
+        with gzip.open(str(path), "wb") as f:
+            f.write(orjson.dumps(item))
+    else:
+        with open(str(path), "wb") as f:
+            f.write(orjson.dumps(item))
+
+
 def dump_jsonl(
     filepath: Union[str, pathlib.Path],
     json_iter: Iterable[Any],
 ) -> int:
     count = 0
     open_fn = get_open_fn(filepath)
```

### Comparing `robotoff-1.8.0/robotoff/utils/cache.py` & `robotoff-1.9.0/robotoff/utils/cache.py`

 * *Files 8% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 
     def get(self, **kwargs):
         if self.store is None or (
             self.expiration_timedelta is not None
             and datetime.datetime.utcnow() >= self.expires_after
         ):
             if self.store is not None:
-                logger.info("ProductStore expired, reloading...")
+                logger.info("CachedStore expired, reloading...")
 
             if self.expiration_timedelta is not None:
                 self.expires_after = (
                     datetime.datetime.utcnow() + self.expiration_timedelta
                 )
             self.store = self.fetch_func(**kwargs)
```

### Comparing `robotoff-1.8.0/robotoff/utils/es.py` & `robotoff-1.9.0/robotoff/utils/es.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/utils/fold_to_ascii.py` & `robotoff-1.9.0/robotoff/utils/fold_to_ascii.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/utils/i18n.py` & `robotoff-1.9.0/robotoff/utils/i18n.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/utils/text.py` & `robotoff-1.9.0/robotoff/utils/text.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/client.py` & `robotoff-1.9.0/robotoff/workers/client.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/listener.py` & `robotoff-1.9.0/robotoff/workers/listener.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/tasks/__init__.py` & `robotoff-1.9.0/robotoff/workers/tasks/__init__.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/tasks/import_image.py` & `robotoff-1.9.0/robotoff/workers/tasks/import_image.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/tasks/product_updated.py` & `robotoff-1.9.0/robotoff/workers/tasks/product_updated.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/robotoff/workers/tasks/update_recycle.py` & `robotoff-1.9.0/robotoff/workers/tasks/update_recycle.py`

 * *Files identical despite different names*

### Comparing `robotoff-1.8.0/setup.py` & `robotoff-1.9.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -57,15 +57,15 @@
  'typer>=0.3.2,<0.4.0']
 
 entry_points = \
 {'console_scripts': ['robotoff-cli = robotoff.cli.main:main']}
 
 setup_kwargs = {
     'name': 'robotoff',
-    'version': '1.8.0',
+    'version': '1.9.0',
     'description': 'Real-time and batch prediction service for Openfoodfacts.',
     'long_description': None,
     'author': 'Openfoodfacts Team',
     'author_email': None,
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `robotoff-1.8.0/PKG-INFO` & `robotoff-1.9.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: robotoff
-Version: 1.8.0
+Version: 1.9.0
 Summary: Real-time and batch prediction service for Openfoodfacts.
 License: GNU Affero General Public License v3
 Author: Openfoodfacts Team
 Requires-Python: >=3.7,<4.0
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
```

