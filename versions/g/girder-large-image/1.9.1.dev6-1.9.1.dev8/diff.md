# Comparing `tmp/girder-large-image-1.9.1.dev6.tar.gz` & `tmp/girder-large-image-1.9.1.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/girder-large-image-1.9.1.dev6.tar", last modified: Mon Dec 20 21:01:12 2021, max compression
+gzip compressed data, was "dist/girder-large-image-1.9.1.dev8.tar", last modified: Tue Dec 21 17:37:13 2021, max compression
```

## Comparing `girder-large-image-1.9.1.dev6.tar` & `girder-large-image-1.9.1.dev8.tar`

### file list

```diff
@@ -1,73 +1,73 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-20 21:01:11.000000 girder-large-image-1.9.1.dev6/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)      926 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-20 21:01:11.000000 girder-large-image-1.9.1.dev6/README.rst
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12986 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1673 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/constants.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8407 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/girder_tilesource.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3261 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/loadmodelcache.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/models/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/models/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    23845 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/models/image_item.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/rest/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/rest/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    20485 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/rest/large_image_resource.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    61648 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/rest/tiles.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/extra/
--rw-r--r--   0 circleci  (3434) circleci  (3434)       14 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/extra/.gitignore
--rw-r--r--   0 circleci  (3434) circleci  (3434)       57 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      377 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/main.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4969 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/package.json
--rw-r--r--   0 circleci  (3434) circleci  (3434)      399 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/routes.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      235 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/fileList.styl
--rw-r--r--   0 circleci  (3434) circleci  (3434)      648 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/imageViewerSelectWidget.styl
--rw-r--r--   0 circleci  (3434) circleci  (3434)      350 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/itemList.styl
--rw-r--r--   0 circleci  (3434) circleci  (3434)      374 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/itemView.styl
--rw-r--r--   0 circleci  (3434) circleci  (3434)       87 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/largeImageConfig.styl
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      564 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/imageViewerSelectWidget.pug
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3424 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/itemView.pug
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6008 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/largeImageConfig.pug
--rw-r--r--   0 circleci  (3434) circleci  (3434)      478 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/largeImage_fileAction.pug
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6638 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/configView.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2651 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/fileList.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5378 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerSelectWidget.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2049 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/base.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8649 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/geojs.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      272 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2992 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/leaflet.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4527 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/openlayers.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2077 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/openseadragon.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11384 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/setFrameQuad.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4895 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/slideatlas.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      309 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/index.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5014 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemList.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2514 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemView.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      808 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemViewWidget.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)      724 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/girder_large_image/web_client/webpack.helper.js
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      926 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2657 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       67 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/entry_points.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/not-zip-safe
--rw-r--r--   0 circleci  (3434) circleci  (3434)      116 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       19 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/girder_large_image.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2230 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/setup.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/test_girder/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2168 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/conftest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2018 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/girder_utilities.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    16932 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/test_large_image.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    60546 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/test_tiles_rest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      919 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/test_web_client.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-20 21:01:12.000000 girder-large-image-1.9.1.dev6/test_girder/web_client_specs/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      237 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/web_client_specs/.eslintrc
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7267 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/web_client_specs/imageViewerSpec.js
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4170 2021-12-20 21:00:58.000000 girder-large-image-1.9.1.dev6/test_girder/web_client_specs/largeImageSpec.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      578 2021-12-21 17:37:12.000000 girder-large-image-1.9.1.dev8/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      926 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7010 2021-12-21 17:37:12.000000 girder-large-image-1.9.1.dev8/README.rst
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12986 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1673 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/constants.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8407 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/girder_tilesource.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3261 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/loadmodelcache.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/models/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/models/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    23845 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/models/image_item.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/rest/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/rest/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    20485 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/rest/large_image_resource.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    61648 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/rest/tiles.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/extra/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       14 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/extra/.gitignore
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       57 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      377 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/main.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4969 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/package.json
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      399 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/routes.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      235 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/fileList.styl
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      648 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/imageViewerSelectWidget.styl
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      350 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/itemList.styl
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      374 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/itemView.styl
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       87 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/largeImageConfig.styl
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      564 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/imageViewerSelectWidget.pug
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3424 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/itemView.pug
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6008 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/largeImageConfig.pug
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      478 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/largeImage_fileAction.pug
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6638 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/configView.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2651 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/fileList.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5378 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerSelectWidget.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2049 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/base.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8649 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/geojs.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      272 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2992 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/leaflet.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4527 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/openlayers.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2077 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/openseadragon.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11384 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/setFrameQuad.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4895 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/slideatlas.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      309 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/index.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5014 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemList.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2514 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemView.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      808 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemViewWidget.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      724 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/girder_large_image/web_client/webpack.helper.js
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      926 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2657 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       67 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/entry_points.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/not-zip-safe
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      116 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       19 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/girder_large_image.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2230 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/test_girder/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2168 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/conftest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2018 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/girder_utilities.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    16932 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/test_large_image.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    60546 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/test_tiles_rest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      919 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/test_web_client.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-12-21 17:37:13.000000 girder-large-image-1.9.1.dev8/test_girder/web_client_specs/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      237 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/web_client_specs/.eslintrc
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7267 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/web_client_specs/imageViewerSpec.js
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4170 2021-12-21 17:36:53.000000 girder-large-image-1.9.1.dev8/test_girder/web_client_specs/largeImageSpec.js
```

### Comparing `girder-large-image-1.9.1.dev6/LICENSE` & `girder-large-image-1.9.1.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/PKG-INFO` & `girder-large-image-1.9.1.dev8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: girder-large-image
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: A Girder plugin to work with large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: girder-plugin,large_image
 Platform: UNKNOWN
```

### Comparing `girder-large-image-1.9.1.dev6/README.rst` & `girder-large-image-1.9.1.dev8/README.rst`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/__init__.py` & `girder-large-image-1.9.1.dev8/girder_large_image/__init__.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/constants.py` & `girder-large-image-1.9.1.dev8/girder_large_image/constants.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/girder_tilesource.py` & `girder-large-image-1.9.1.dev8/girder_large_image/girder_tilesource.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/loadmodelcache.py` & `girder-large-image-1.9.1.dev8/girder_large_image/loadmodelcache.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/models/image_item.py` & `girder-large-image-1.9.1.dev8/girder_large_image/models/image_item.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/rest/large_image_resource.py` & `girder-large-image-1.9.1.dev8/girder_large_image/rest/large_image_resource.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/rest/tiles.py` & `girder-large-image-1.9.1.dev8/girder_large_image/rest/tiles.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/package.json` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/package.json`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/stylesheets/imageViewerSelectWidget.styl` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/stylesheets/imageViewerSelectWidget.styl`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/imageViewerSelectWidget.pug` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/imageViewerSelectWidget.pug`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/itemView.pug` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/itemView.pug`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/templates/largeImageConfig.pug` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/templates/largeImageConfig.pug`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/configView.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/configView.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/fileList.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/fileList.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerSelectWidget.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerSelectWidget.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/base.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/base.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/geojs.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/geojs.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/leaflet.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/leaflet.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/openlayers.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/openlayers.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/openseadragon.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/openseadragon.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/setFrameQuad.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/setFrameQuad.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/imageViewerWidget/slideatlas.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/imageViewerWidget/slideatlas.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemList.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemList.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemView.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemView.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/views/itemViewWidget.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/views/itemViewWidget.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image/web_client/webpack.helper.js` & `girder-large-image-1.9.1.dev8/girder_large_image/web_client/webpack.helper.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image.egg-info/PKG-INFO` & `girder-large-image-1.9.1.dev8/girder_large_image.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: girder-large-image
-Version: 1.9.1.dev6
+Version: 1.9.1.dev8
 Summary: A Girder plugin to work with large, multiresolution images.
 Home-page: https://github.com/girder/large_image
 Author: Kitware, Inc.
 Author-email: kitware@kitware.com
 License: Apache Software License 2.0
 Keywords: girder-plugin,large_image
 Platform: UNKNOWN
```

### Comparing `girder-large-image-1.9.1.dev6/girder_large_image.egg-info/SOURCES.txt` & `girder-large-image-1.9.1.dev8/girder_large_image.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/setup.py` & `girder-large-image-1.9.1.dev8/setup.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/conftest.py` & `girder-large-image-1.9.1.dev8/test_girder/conftest.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/girder_utilities.py` & `girder-large-image-1.9.1.dev8/test_girder/girder_utilities.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/test_large_image.py` & `girder-large-image-1.9.1.dev8/test_girder/test_large_image.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/test_tiles_rest.py` & `girder-large-image-1.9.1.dev8/test_girder/test_tiles_rest.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/test_web_client.py` & `girder-large-image-1.9.1.dev8/test_girder/test_web_client.py`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/web_client_specs/imageViewerSpec.js` & `girder-large-image-1.9.1.dev8/test_girder/web_client_specs/imageViewerSpec.js`

 * *Files identical despite different names*

### Comparing `girder-large-image-1.9.1.dev6/test_girder/web_client_specs/largeImageSpec.js` & `girder-large-image-1.9.1.dev8/test_girder/web_client_specs/largeImageSpec.js`

 * *Files identical despite different names*

