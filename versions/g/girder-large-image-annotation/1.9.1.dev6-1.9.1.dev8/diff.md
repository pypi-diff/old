# Comparing `tmp/girder-large-image-annotation-1.9.1.dev6.tar.gz` & `tmp/girder-large-image-annotation-1.9.1.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/girder-large-image-annotation-1.9.1.dev6.tar", last modified: Mon Dec 20 21:01:18 2021, max compression
+gzip compressed data, was "dist/girder-large-image-annotation-1.9.1.dev8.tar", last modified: Tue Dec 21 17:37:20 2021, max compression
```

## Comparing `girder-large-image-annotation-1.9.1.dev6.tar` & `girder-large-image-annotation-1.9.1.dev8.tar`

### file list

```diff
@@ -1,100 +1,100 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-20 21:01:17.000000 girder-large-image-annotation-1.9.1.dev6/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)      983 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-20 21:01:17.000000 girder-large-image-annotation-1.9.1.dev6/README.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/docs/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12413 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/docs/annotations.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2865 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      877 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/constants.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    50724 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/annotation.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    21797 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/annotationelement.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/rest/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/rest/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    28125 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/rest/annotation.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1054 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/convert.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6708 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/convertFeatures.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/defaults/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      153 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/defaults/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       98 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/defaults/point.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       98 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/defaults/polyline.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      138 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/defaults/rectangle.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      585 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/common.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      500 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/convert.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/coordinates/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      219 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/coordinates/array.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       92 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/coordinates/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      154 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/coordinates/point.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      209 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/index.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      187 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      489 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/line.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      417 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/point.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      474 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/polygon.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1962 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/rectangle.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      153 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      190 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/point.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      532 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/polyline.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      707 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/rectangle.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      369 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      485 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/rotate.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1049 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/style.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/collections/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      432 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/collections/AnnotationCollection.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      185 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/collections/ElementCollection.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       97 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/collections/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      231 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      327 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/main.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/models/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16120 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/models/AnnotationModel.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      406 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/models/ElementModel.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       82 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/models/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4856 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/package.json
--rw-r--r--   0 circleci  (3434) circleci  (3434)      442 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/routes.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/stylesheets/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      356 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/stylesheets/annotationListWidget.styl
--rw-r--r--   0 circleci  (3434) circleci  (3434)      428 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/stylesheets/itemList.styl
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2124 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/annotationListWidget.pug
--rw-r--r--   0 circleci  (3434) circleci  (3434)       29 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/imageViewerAnnotationList.pug
--rw-r--r--   0 circleci  (3434) circleci  (3434)      915 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/largeImageAnnotationConfig.pug
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8422 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/annotationListWidget.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3206 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/configView.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1235 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerSelectWidget.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2027 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/base.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    25240 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/geojs.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)       52 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      647 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2783 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/itemList.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      983 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4529 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       99 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/entry_points.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/not-zip-safe
--rw-r--r--   0 circleci  (3434) circleci  (3434)       91 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       30 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2263 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/setup.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      529 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/conftest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1910 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/girder_utilities.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    29446 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/test_annotations.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    30066 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/test_annotations_rest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1310 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/test_web_client.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:18.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      237 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/.eslintrc
--rw-r--r--   0 circleci  (3434) circleci  (3434)    15501 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/annotationListSpec.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    19312 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/annotationSpec.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6818 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/geojsAnnotationSpec.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    31188 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/geojsSpec.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      347 2021-12-20 21:00:58.000000 girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/sample_annotation.json
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-21 17:37:19.000000 girder-large-image-annotation-1.9.1.dev8/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      983 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-21 17:37:19.000000 girder-large-image-annotation-1.9.1.dev8/README.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/docs/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12413 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/docs/annotations.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2865 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      877 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/constants.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    50724 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/annotation.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    21797 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/annotationelement.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/rest/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/rest/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    28125 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/rest/annotation.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1054 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/convert.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6708 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/convertFeatures.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/defaults/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      153 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/defaults/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       98 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/defaults/point.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       98 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/defaults/polyline.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      138 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/defaults/rectangle.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      585 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/common.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      500 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/convert.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/coordinates/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      219 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/coordinates/array.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       92 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/coordinates/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      154 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/coordinates/point.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      209 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/index.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      187 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      489 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/line.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      417 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/point.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      474 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/polygon.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1962 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/rectangle.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      153 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      190 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/point.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      532 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/polyline.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      707 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/rectangle.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      369 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      485 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/rotate.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1049 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/style.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/collections/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      432 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/collections/AnnotationCollection.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      185 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/collections/ElementCollection.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       97 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/collections/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      231 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      327 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/main.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/models/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16120 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/models/AnnotationModel.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      406 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/models/ElementModel.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       82 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/models/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4856 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/package.json
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      442 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/routes.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/stylesheets/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      356 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/stylesheets/annotationListWidget.styl
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      428 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/stylesheets/itemList.styl
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2124 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/annotationListWidget.pug
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       29 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/imageViewerAnnotationList.pug
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      915 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/largeImageAnnotationConfig.pug
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8422 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/annotationListWidget.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3206 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/configView.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1235 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerSelectWidget.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2027 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/base.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    25240 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/geojs.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       52 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      647 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2783 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/itemList.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      983 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4529 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       99 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/entry_points.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/not-zip-safe
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       91 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       30 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2263 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      529 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/conftest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1910 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/girder_utilities.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    29446 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/test_annotations.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    30066 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/test_annotations_rest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1310 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/test_web_client.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:20.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      237 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/.eslintrc
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    15501 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/annotationListSpec.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    19312 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/annotationSpec.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6818 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/geojsAnnotationSpec.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    31188 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/geojsSpec.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      347 2021-12-21 17:36:53.000000 girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/sample_annotation.json
```

### Comparing `girder-large-image-annotation-1.9.1.dev6/LICENSE` & `girder-large-image-annotation-1.9.1.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/PKG-INFO` & `girder-large-image-annotation-1.9.1.dev8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: girder-large-image-annotation
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: A Girder plugin to store and display annotations on large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: girder-plugin,large_image
 Platform: UNKNOWN
```

### Comparing `girder-large-image-annotation-1.9.1.dev6/README.rst` & `girder-large-image-annotation-1.9.1.dev8/README.rst`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/docs/annotations.rst` & `girder-large-image-annotation-1.9.1.dev8/docs/annotations.rst`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/__init__.py` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/__init__.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/constants.py` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/constants.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/annotation.py` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/annotation.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/models/annotationelement.py` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/models/annotationelement.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/rest/annotation.py` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/rest/annotation.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/convert.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/convert.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/convertFeatures.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/convertFeatures.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/common.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/common.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geojs/types/rectangle.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geojs/types/rectangle.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/polyline.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/polyline.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/geometry/rectangle.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/geometry/rectangle.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/annotations/style.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/annotations/style.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/models/AnnotationModel.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/models/AnnotationModel.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/package.json` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/package.json`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/annotationListWidget.pug` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/annotationListWidget.pug`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/templates/largeImageAnnotationConfig.pug` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/templates/largeImageAnnotationConfig.pug`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/annotationListWidget.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/annotationListWidget.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/configView.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/configView.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerSelectWidget.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerSelectWidget.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/base.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/base.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/imageViewerWidget/geojs.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/imageViewerWidget/geojs.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/index.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/index.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation/web_client/views/itemList.js` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation/web_client/views/itemList.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/PKG-INFO` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: girder-large-image-annotation
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: A Girder plugin to store and display annotations on large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: girder-plugin,large_image
 Platform: UNKNOWN
```

### Comparing `girder-large-image-annotation-1.9.1.dev6/girder_large_image_annotation.egg-info/SOURCES.txt` & `girder-large-image-annotation-1.9.1.dev8/girder_large_image_annotation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/setup.py` & `girder-large-image-annotation-1.9.1.dev8/setup.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/conftest.py` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/conftest.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/girder_utilities.py` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/girder_utilities.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/test_annotations.py` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/test_annotations.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/test_annotations_rest.py` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/test_annotations_rest.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/test_web_client.py` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/test_web_client.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/annotationListSpec.js` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/annotationListSpec.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/annotationSpec.js` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/annotationSpec.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/geojsAnnotationSpec.js` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/geojsAnnotationSpec.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-annotation-1.9.1.dev6/test_annotation/web_client_specs/geojsSpec.js` & `girder-large-image-annotation-1.9.1.dev8/test_annotation/web_client_specs/geojsSpec.js`

 * *Files identical despite different names*

