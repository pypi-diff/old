# Comparing `tmp/sepal-ui-2.8.0.tar.gz` & `tmp/sepal-ui-2.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sepal-ui-2.8.0.tar", last modified: Mon Apr 18 16:24:12 2022, max compression
+gzip compressed data, was "sepal-ui-2.9.4.tar", last modified: Thu Jun  9 14:15:16 2022, max compression
```

## Comparing `sepal-ui-2.8.0.tar` & `sepal-ui-2.9.4.tar`

### file list

```diff
@@ -1,73 +1,93 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.315887 sepal-ui-2.8.0/
--rw-r--r--   0 runner    (1001) docker     (121)     1069 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)     4304 2022-04-18 16:24:12.315887 sepal-ui-2.8.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3339 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.303887 sepal-ui-2.8.0/sepal_ui/
--rw-r--r--   0 runner    (1001) docker     (121)      379 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/aoi/
--rw-r--r--   0 runner    (1001) docker     (121)       73 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/aoi/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    21385 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/aoi/aoi_model.py
--rw-r--r--   0 runner    (1001) docker     (121)     1996 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/aoi/aoi_tile.py
--rw-r--r--   0 runner    (1001) docker     (121)    14536 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/aoi/aoi_view.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/bin/
--rw-r--r--   0 runner    (1001) docker     (121)     2358 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/activate_venv
--rwxr-xr-x   0 runner    (1001) docker     (121)     6541 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/module_deploy
--rwxr-xr-x   0 runner    (1001) docker     (121)    10110 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/module_factory
--rwxr-xr-x   0 runner    (1001) docker     (121)     1642 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/module_l10n
--rwxr-xr-x   0 runner    (1001) docker     (121)     1471 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/module_theme
--rwxr-xr-x   0 runner    (1001) docker     (121)     3859 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/bin/module_venv
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/frontend/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/frontend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1020 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/frontend/js.py
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/frontend/styles.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/mapping/
--rw-r--r--   0 runner    (1001) docker     (121)       57 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/mapping/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4079 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/mapping/fullscreen_control.py
--rw-r--r--   0 runner    (1001) docker     (121)    27845 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/mapping/mapping.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/message/
--rw-r--r--   0 runner    (1001) docker     (121)      119 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/message/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/message/en/
--rw-r--r--   0 runner    (1001) docker     (121)     6064 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/message/en/locale.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/message/es/
--rw-r--r--   0 runner    (1001) docker     (121)     5760 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/message/es/locale.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/message/fr/
--rw-r--r--   0 runner    (1001) docker     (121)     6724 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/message/fr/locale.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/model/
--rw-r--r--   0 runner    (1001) docker     (121)       25 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2221 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/model/model.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.307887 sepal-ui-2.8.0/sepal_ui/reclassify/
--rw-r--r--   0 runner    (1001) docker     (121)      146 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      445 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/parameters.py
--rw-r--r--   0 runner    (1001) docker     (121)    21176 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_model.py
--rw-r--r--   0 runner    (1001) docker     (121)     3124 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_tile.py
--rw-r--r--   0 runner    (1001) docker     (121)    24543 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_view.py
--rw-r--r--   0 runner    (1001) docker     (121)    21561 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/reclassify/table_view.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.311887 sepal-ui-2.8.0/sepal_ui/scripts/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3172 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/encrypted_key.json
--rw-r--r--   0 runner    (1001) docker     (121)  2492815 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/gadm_database.csv
--rw-r--r--   0 runner    (1001) docker     (121)  1904816 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/gaul_database.csv
--rw-r--r--   0 runner    (1001) docker     (121)     3439 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/gee.py
--rw-r--r--   0 runner    (1001) docker     (121)     5677 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/locale.csv
--rw-r--r--   0 runner    (1001) docker     (121)    16849 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)      426 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/scripts/warning.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.315887 sepal-ui-2.8.0/sepal_ui/sepalwidgets/
--rw-r--r--   0 runner    (1001) docker     (121)      763 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13724 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/alert.py
--rw-r--r--   0 runner    (1001) docker     (121)    23875 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     3498 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/btn.py
--rw-r--r--   0 runner    (1001) docker     (121)    30925 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/inputs.py
--rw-r--r--   0 runner    (1001) docker     (121)     4244 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/sepalwidget.py
--rw-r--r--   0 runner    (1001) docker     (121)     6691 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/tile.py
--rw-r--r--   0 runner    (1001) docker     (121)     4183 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/sepalwidgets/widget.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.315887 sepal-ui-2.8.0/sepal_ui/translator/
--rw-r--r--   0 runner    (1001) docker     (121)       26 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/translator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8939 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/sepal_ui/translator/translator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-04-18 16:24:12.303887 sepal-ui-2.8.0/sepal_ui.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4304 2022-04-18 16:24:12.000000 sepal-ui-2.8.0/sepal_ui.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1603 2022-04-18 16:24:12.000000 sepal-ui-2.8.0/sepal_ui.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-04-18 16:24:12.000000 sepal-ui-2.8.0/sepal_ui.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      453 2022-04-18 16:24:12.000000 sepal-ui-2.8.0/sepal_ui.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-04-18 16:24:12.000000 sepal-ui-2.8.0/sepal_ui.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-04-18 16:24:12.315887 sepal-ui-2.8.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     3375 2022-04-18 16:24:04.000000 sepal-ui-2.8.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.774021 sepal-ui-2.9.4/
+-rw-r--r--   0 runner    (1001) docker     (121)     1069 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)     4430 2022-06-09 14:15:16.774021 sepal-ui-2.9.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3515 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.758020 sepal-ui-2.9.4/sepal_ui/
+-rw-r--r--   0 runner    (1001) docker     (121)      226 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.758020 sepal-ui-2.9.4/sepal_ui/aoi/
+-rw-r--r--   0 runner    (1001) docker     (121)       73 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/aoi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21050 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/aoi/aoi_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1996 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/aoi/aoi_tile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14657 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/aoi/aoi_view.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.758020 sepal-ui-2.9.4/sepal_ui/bin/
+-rw-r--r--   0 runner    (1001) docker     (121)     2791 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/activate_venv.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     6609 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/module_deploy.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    10173 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/module_factory.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1712 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/module_l10n.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1538 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/module_theme.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3926 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/bin/module_venv.py
+-rw-r--r--   0 runner    (1001) docker     (121)      523 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/conf.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.758020 sepal-ui-2.9.4/sepal_ui/frontend/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/frontend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1020 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/frontend/js.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6495 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/frontend/styles.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/mapping/
+-rw-r--r--   0 runner    (1001) docker     (121)      162 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2816 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/basemaps.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1544 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/draw_control.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4089 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/fullscreen_control.py
+-rw-r--r--   0 runner    (1001) docker     (121)      486 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/layer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1072 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/map_btn.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30249 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/sepal_map.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10253 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/mapping/value_inspector.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/
+-rw-r--r--   0 runner    (1001) docker     (121)      119 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/ar-SA/
+-rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/ar-SA/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/en/
+-rw-r--r--   0 runner    (1001) docker     (121)     7565 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/en/locale.json
+-rw-r--r--   0 runner    (1001) docker     (121)      293 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/en/v_inspector.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/es/
+-rw-r--r--   0 runner    (1001) docker     (121)     7692 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/es/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/fr/
+-rw-r--r--   0 runner    (1001) docker     (121)     8358 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/fr/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/pt-PT/
+-rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/pt-PT/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/ru-RU/
+-rw-r--r--   0 runner    (1001) docker     (121)     3233 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/ru-RU/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/message/zh-CN/
+-rw-r--r--   0 runner    (1001) docker     (121)     5971 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/message/zh-CN/locale.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/model/
+-rw-r--r--   0 runner    (1001) docker     (121)       25 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2221 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/model/model.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/planetapi/
+-rw-r--r--   0 runner    (1001) docker     (121)       55 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/planetapi/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4652 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/planetapi/planet_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4270 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/planetapi/planet_view.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.762020 sepal-ui-2.9.4/sepal_ui/reclassify/
+-rw-r--r--   0 runner    (1001) docker     (121)      146 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      445 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/parameters.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21176 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_model.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3124 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_tile.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24544 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_view.py
+-rw-r--r--   0 runner    (1001) docker     (121)    21562 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/reclassify/table_view.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.770020 sepal-ui-2.9.4/sepal_ui/scripts/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3172 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/encrypted_key.json
+-rw-r--r--   0 runner    (1001) docker     (121)  2492815 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/gadm_database.csv
+-rw-r--r--   0 runner    (1001) docker     (121)  1904816 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/gaul_database.csv
+-rw-r--r--   0 runner    (1001) docker     (121)     3439 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/gee.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5677 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/locale.csv
+-rw-r--r--   0 runner    (1001) docker     (121)    19146 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/scripts/warning.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.774021 sepal-ui-2.9.4/sepal_ui/sepalwidgets/
+-rw-r--r--   0 runner    (1001) docker     (121)      817 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11909 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/alert.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23995 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3498 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/btn.py
+-rw-r--r--   0 runner    (1001) docker     (121)    31244 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/inputs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6427 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/sepalwidget.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6691 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/tile.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6007 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/sepalwidgets/widget.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.774021 sepal-ui-2.9.4/sepal_ui/translator/
+-rw-r--r--   0 runner    (1001) docker     (121)       26 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/translator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9661 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/sepal_ui/translator/translator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-09 14:15:16.758020 sepal-ui-2.9.4/sepal_ui.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4430 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2104 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      299 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      408 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        9 2022-06-09 14:15:16.000000 sepal-ui-2.9.4/sepal_ui.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-09 14:15:16.774021 sepal-ui-2.9.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     3558 2022-06-09 14:15:06.000000 sepal-ui-2.9.4/setup.py
```

### Comparing `sepal-ui-2.8.0/LICENSE.txt` & `sepal-ui-2.9.4/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/PKG-INFO` & `sepal-ui-2.9.4/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 Metadata-Version: 2.1
 Name: sepal-ui
-Version: 2.8.0
+Version: 2.9.4
 Summary: Wrapper for ipyvuetify widgets to unify the display of voila dashboards in SEPAL platform
 Home-page: https://github.com/12rambau/sepal_ui
 Author: Pierrick Rambaud
 Author-email: pierrick.rambaud49@gmail.com
 License: MIT
-Download-URL: https://github.com/12rambau/sepal_ui/archive/v_2.8.0.tar.gz
+Download-URL: https://github.com/12rambau/sepal_ui/archive/v_2.9.4.tar.gz
 Keywords: UI,Python,widget,sepal
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: License :: OSI Approved :: MIT License
-Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Python: >=3.6.9
 Description-Content-Type: text/x-rst
 Provides-Extra: dev
 Provides-Extra: test
@@ -28,14 +27,18 @@
 
 Sepal_ui
 --------
 
 .. image:: https://img.shields.io/badge/License-MIT-yellow.svg
     :target: https://opensource.org/licenses/MIT
     :alt: License: MIT
+    
+.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.6467835.svg
+   :target: https://doi.org/10.5281/zenodo.6467835
+   :alt: Citation
 
 .. image:: https://badge.fury.io/py/sepal-ui.svg
     :target: https://badge.fury.io/py/sepal-ui
     :alt: PyPI version
     
 .. image:: https://img.shields.io/pypi/dm/sepal-ui?color=307CC2&logo=python&logoColor=gainsboro  
     :target: https://pypi.org/project/sepal-ui/
@@ -75,21 +78,21 @@
    
 --------------------------------------------------------------------------------
 
 Currently translated in the following languages:
 
 .. csv-table::
 
-    English, Français, Español
+    English, Français, Español, 中国人
 
 You can contribute to the translation effort on our `crowdin project <https://crowdin.com/project/sepal-ui>`__.
 
 --------------------------------------------------------------------------------
 
-:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the SEPAL environment. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
+:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the `SEPAL environment <https://sepal.io/>`__. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
 By using this libraries, you'll ensure a robust and unified interface for your scripts and a easy and complete integration into the SEPAL dashboard of application.
 
 The full documentation is available `here <https://sepal-ui.readthedocs.io/en/latest/>`__ and a demo app can be launched on Heroku following this link: `<https://sepal-ui.herokuapp.com>`__.
 
 We are happy to receive feedback and we welcome any kind of contribution.
 
 .. image:: https://raw.githubusercontent.com/12rambau/sepal_ui/master/docs/source/_image/sepal_ui_screenshot.png
```

### Comparing `sepal-ui-2.8.0/README.rst` & `sepal-ui-2.9.4/README.rst`

 * *Files 4% similar despite different names*

```diff
@@ -2,14 +2,18 @@
 
 Sepal_ui
 --------
 
 .. image:: https://img.shields.io/badge/License-MIT-yellow.svg
     :target: https://opensource.org/licenses/MIT
     :alt: License: MIT
+    
+.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.6467835.svg
+   :target: https://doi.org/10.5281/zenodo.6467835
+   :alt: Citation
 
 .. image:: https://badge.fury.io/py/sepal-ui.svg
     :target: https://badge.fury.io/py/sepal-ui
     :alt: PyPI version
     
 .. image:: https://img.shields.io/pypi/dm/sepal-ui?color=307CC2&logo=python&logoColor=gainsboro  
     :target: https://pypi.org/project/sepal-ui/
@@ -49,21 +53,21 @@
    
 --------------------------------------------------------------------------------
 
 Currently translated in the following languages:
 
 .. csv-table::
 
-    English, Français, Español
+    English, Français, Español, 中国人
 
 You can contribute to the translation effort on our `crowdin project <https://crowdin.com/project/sepal-ui>`__.
 
 --------------------------------------------------------------------------------
 
-:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the SEPAL environment. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
+:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the `SEPAL environment <https://sepal.io/>`__. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
 By using this libraries, you'll ensure a robust and unified interface for your scripts and a easy and complete integration into the SEPAL dashboard of application.
 
 The full documentation is available `here <https://sepal-ui.readthedocs.io/en/latest/>`__ and a demo app can be launched on Heroku following this link: `<https://sepal-ui.herokuapp.com>`__.
 
 We are happy to receive feedback and we welcome any kind of contribution.
 
 .. image:: https://raw.githubusercontent.com/12rambau/sepal_ui/master/docs/source/_image/sepal_ui_screenshot.png
```

### Comparing `sepal-ui-2.8.0/sepal_ui/aoi/aoi_model.py` & `sepal-ui-2.9.4/sepal_ui/aoi/aoi_model.py`

 * *Files 6% similar despite different names*

```diff
@@ -3,15 +3,14 @@
 from traitlets import Any
 from urllib.request import urlretrieve
 import tempfile
 
 import pandas as pd
 import geopandas as gpd
 from ipyleaflet import GeoJSON
-import geemap
 import ee
 
 from sepal_ui import color
 from sepal_ui.frontend.styles import AOI_STYLE
 from sepal_ui.scripts import utils as su
 from sepal_ui.scripts import gee
 from sepal_ui.message import ms
@@ -20,15 +19,16 @@
 __all__ = ["AoiModel"]
 
 
 class AoiModel(Model):
     """
     an Model object dedicated to the sorage and the manipulation of aoi.
     It is meant to be used with the AoiView object (embeded in the AoiTile).
-    By using this you will be able to provide your application with aoi as an ee_object or a gdf, depending if you activated the ee binding or not.
+    By using this you will be able to provide your application with aoi as an ee_object
+    or a gdf, depending if you activated the ee binding or not.
     The class also provide insight on your aoi geometry.
 
     Args:
         gee (bool, optional): wether or not the aoi selector should be using the EarthEngine binding
         vector (str|pathlib.Path, optional): the path to the default vector object
         admin (int, optional): the administrative code of the default selection. Need to be GADM if ee==False and GAUL 2015 if ee==True.
         asset (str, optional): the default asset. Can only work if ee==True
@@ -58,17 +58,18 @@
     ISO = ["GID_0", "ISO 3166-1 alpha-3"]
     "list(str): GADM(0) and GAUL(1) iso codes key"
 
     GADM_BASE_URL = "https://biogeo.ucdavis.edu/data/gadm3.6/gpkg/gadm36_{}_gpkg.zip"
     "str: the base url to download gadm maps"
 
     GADM_ZIP_DIR = Path.home() / "tmp" / "GADM_zip"
-    GADM_ZIP_DIR.mkdir(parents=True, exist_ok=True)
     "pathlib.Path: the zip dir where we download the zips"
 
+    GADM_ZIP_DIR.mkdir(parents=True, exist_ok=True)
+
     GAUL_ASSET = "FAO/GAUL/2015/level{}"
     "str: the GAUL asset name"
 
     ASSET_SUFFIX = "aoi_"
     "str: the suffix to identify the asset in GEE"
 
     # ###########################################################################
@@ -211,15 +212,16 @@
         elif self.asset_name is not None:
             self.set_object("ASSET")
 
         return self
 
     def set_object(self, method=None):
         """
-        set the object (gdf/featurecollection) based on the model inputs. The method can be manually overwrite
+        set the object (gdf/featurecollection) based on the model inputs. The method can
+        be manually overwritten
 
         Args:
             method (str, optional): a model loading method
 
         Return:
             self
         """
@@ -237,67 +239,63 @@
         elif self.method == "SHAPE":
             self._from_vector(self.vector_json)
         elif self.method == "DRAW":
             self._from_geo_json(self.geo_json)
         elif self.method == "ASSET":
             self._from_asset(self.asset_name)
         else:
-            raise Exception(ms.aoi_sel.no_inputs)
+            raise Exception(ms.aoi_sel.exception.no_inputs)
 
         self.alert.add_msg(ms.aoi_sel.complete, "success")
 
         return self
 
     def _from_asset(self, asset_name):
         """set the ee.FeatureCollection output from an existing asset"""
 
         if not (asset_name["pathname"]):
-            raise Exception("Please select an asset.")
+            raise Exception(ms.aoi_sel.exception.no_asset)
 
         if asset_name["column"] != "ALL":
             if asset_name["value"] is None:
-                raise Exception("Please select a value.")
+                raise Exception(ms.aoi_sel.exception.no_value)
 
+        # set the name
         self.name = Path(asset_name["pathname"]).stem.replace(self.ASSET_SUFFIX, "")
         ee_col = ee.FeatureCollection(asset_name["pathname"])
 
         if asset_name["column"] != "ALL":
 
             column = asset_name["column"]
             value = asset_name["value"]
             ee_col = ee_col.filterMetadata(column, "equals", value)
             self.name = f"{self.name}_{column}_{value}"
 
         # set the feature collection
         self.feature_collection = ee_col
 
         # create a gdf form te feature_collection
-        # cannot be used before geemap 0.8.17 (not released)
-        # self.gdf = geemap.ee_to_geopandas(self.feature_collection)
-        self.gdf = gpd.GeoDataFrame.from_features(
-            self.feature_collection.getInfo()["features"]
-        ).set_crs(epsg=4326)
-
-        # set the name
+        features = self.feature_collection.getInfo()["features"]
+        self.gdf = gpd.GeoDataFrame.from_features(features).set_crs(epsg=4326)
 
         return self
 
     def _from_points(self, point_json):
         """set the object output from a csv json"""
 
         if not all(point_json.values()):
-            raise Exception("All fields are required, please fill them.")
+            raise Exception(ms.aoi_sel.exception.uncomplete)
 
         # cast the pathname to pathlib Path
         point_file = Path(point_json["pathname"])
 
         # check that the columns are well set
         values = [v for v in point_json.values()]
         if not len(values) == len(set(values)):
-            raise Exception(ms.aoi_sel.duplicate_key)
+            raise Exception(ms.aoi_sel.exception.duplicate_key)
 
         # create the gdf
         df = pd.read_csv(point_file, sep=None, engine="python")
         self.gdf = gpd.GeoDataFrame(
             df,
             crs="EPSG:4326",
             geometry=gpd.points_from_xy(
@@ -306,30 +304,30 @@
         )
 
         # set the name
         self.name = point_file.stem
 
         if self.ee:
             # transform the gdf to ee.FeatureCollection
-            self.feature_collection = geemap.geojson_to_ee(self.gdf.__geo_interface__)
+            self.feature_collection = ee.FeatureCollection(self.gdf.__geo_interface__)
 
             # export as a GEE asset
             self.export_to_asset()
 
         return self
 
     def _from_vector(self, vector_json):
         """set the object output from a vector json"""
 
         if not (vector_json["pathname"]):
-            raise Exception("Please select a file.")
+            raise Exception(ms.aoi_sel.exception.no_file)
 
         if vector_json["column"] != "ALL":
             if vector_json["value"] is None:
-                raise Exception("Please select a value.")
+                raise Exception(ms.aoi_sel.exception.no_value)
 
         # cast the pathname to pathlib Path
         vector_file = Path(vector_json["pathname"])
 
         # create the gdf
         self.gdf = gpd.read_file(vector_file).to_crs("EPSG:4326")
 
@@ -339,89 +337,87 @@
         # filter it if necessary
         if vector_json["value"] is not None:
             self.gdf = self.gdf[self.gdf[vector_json["column"]] == vector_json["value"]]
             self.name = f"{self.name}_{vector_json['column']}_{vector_json['value']}"
 
         if self.ee:
             # transform the gdf to ee.FeatureCollection
-            self.feature_collection = geemap.geojson_to_ee(self.gdf.__geo_interface__)
+            self.feature_collection = su.geojson_to_ee(self.gdf.__geo_interface__)
 
             # export as a GEE asset
             self.export_to_asset()
 
         return self
 
     def _from_geo_json(self, geo_json):
         """set the gdf output from a geo_json"""
 
         if not geo_json:
-            raise Exception("Please draw a shape in the map")
+            raise Exception(ms.aoi_sel.exception.no_draw)
 
         # remove the style property from geojson as it's not recognize by geopandas and gee
         for feat in geo_json["features"]:
             if "style" in feat["properties"]:
                 del feat["properties"]["style"]
 
         # create the gdf
         self.gdf = gpd.GeoDataFrame.from_features(geo_json).set_crs(epsg=4326)
 
         # normalize the name
         self.name = su.normalize_str(self.name)
 
         if self.ee:
             # transform the gdf to ee.FeatureCollection
-            self.feature_collection = geemap.geojson_to_ee(self.gdf.__geo_interface__)
+            self.feature_collection = su.geojson_to_ee(self.gdf.__geo_interface__)
 
             # export as a GEE asset
             self.export_to_asset()
         else:
             # save the geojson in downloads
             path = Path("~", "downloads", "aoi").expanduser()
             path.mkdir(
                 exist_ok=True, parents=True
             )  # if nothing have been run the downloads folder doesn't exist
             self.gdf.to_file(path / f"{self.name}.geojson", driver="GeoJSON")
 
         return self
 
     def _from_admin(self, admin):
-        """Set the object according to given an administrative number in the GADM norm. The object will be projected in EPSG:4326"""
+        """Set the object according to given an administrative number in the GADM norm.
+        The object will be projected in EPSG:4326"""
 
         if not admin:
-            raise Exception("Select an administrative layer")
+            raise Exception(ms.aoi_sel.exception.no_admlyr)
 
         # get the admin level corresponding to the given admin code
         df = pd.read_csv(self.FILE[self.ee])
 
         # extract the first element that include this administrative code and set the level accordingly
         is_in = df.filter([self.CODE[self.ee].format(i) for i in range(3)]).isin(
             [admin]
         )
 
         if not is_in.any().any():
-            raise Exception("The code is not in the database")
+            raise Exception(ms.aoi_sel.exception.invalid_code)
         else:
             index = 3 if self.ee else -1
             level = (
                 is_in[~((~is_in).all(axis=1))].idxmax(1).iloc[0][index]
             )  # the character that contains the index
 
         if self.ee:
 
             # get the feature_collection
             self.feature_collection = ee.FeatureCollection(
                 self.GAUL_ASSET.format(level)
             ).filter(ee.Filter.eq(f"ADM{level}_CODE", admin))
 
             # transform it into gdf
-            # cannot be used before geemap 0.8.17 (not released)
-            # self.gdf = geemap.ee_to_geopandas(self.feature_collection)
-            self.gdf = gpd.GeoDataFrame.from_features(
-                self.feature_collection.getInfo()["features"]
-            ).set_crs(epsg=4326)
+            features = self.feature_collection.getInfo()["features"]
+            self.gdf = gpd.GeoDataFrame.from_features(features).set_crs(epsg=4326)
 
         else:
             # save the country iso_code
             iso_3 = admin[:3]
 
             # download the geopackage in a tmp directory
             with tempfile.TemporaryDirectory() as tmp_dir:
@@ -499,15 +495,15 @@
         Retrieve the columns or variables from self excluding geometries and gee index.
 
         Return:
             ([str]): sorted list of column names
         """
 
         if self.gdf is None:
-            raise Exception("You must set the gdf before interacting with it")
+            raise Exception(ms.aoi_sel.exception.no_gdf)
 
         if self.ee:
             aoi_ee = ee.Feature(self.feature_collection.first())
             columns = aoi_ee.propertyNames().getInfo()
             list_ = [
                 col for col in columns if col not in ["system:index", "Shape_Area"]
             ]
@@ -525,15 +521,15 @@
 
         Return:
             ([str]): sorted list of fields value
 
         """
 
         if self.gdf is None:
-            raise Exception("You must set the gdf before interacting with it")
+            raise Exception(ms.aoi_sel.exception.no_gdf)
 
         if self.ee:
             fields = self.feature_collection.distinct(column).aggregate_array(column)
             list_ = fields.getInfo()
         else:
             list_ = self.gdf[column].to_list()
 
@@ -544,15 +540,15 @@
         Select an ee object based on selected column and field.
 
         Return:
             (ee.Feature|GoeSeries): the Feature associated with the query
         """
 
         if self.gdf is None:
-            raise Exception("You must set the gdf before interacting with it")
+            raise Exception(ms.aoi_sel.exception.no_gdf)
 
         if self.ee:
             selected_feature = self.feature_collection.filterMetadata(
                 column, "equals", field
             )
         else:
             selected_feature = self.gdf[self.gdf[column] == field]
@@ -615,15 +611,15 @@
         Converts current geopandas object into ipyleaflet GeoJSON
 
         Return:
             (GeoJSON): the geojson layer of the aoi gdf
         """
 
         if self.gdf is None:
-            raise Exception("You must set the gdf before converting it into GeoJSON")
+            raise Exception(ms.aoi_sel.exception.no_gdf)
 
         # read the data from geojson and add the name as a property of the shape
         # useful when handler are added from ipyleaflet
         data = json.loads(self.gdf.to_json())
         for f in data["features"]:
             f["properties"]["name"] = self.name
```

### Comparing `sepal-ui-2.8.0/sepal_ui/aoi/aoi_tile.py` & `sepal-ui-2.9.4/sepal_ui/aoi/aoi_tile.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/aoi/aoi_view.py` & `sepal-ui-2.9.4/sepal_ui/aoi/aoi_view.py`

 * *Files 2% similar despite different names*

```diff
@@ -275,14 +275,21 @@
         self.w_admin_0 = AdminField(0, gee=gee).get_items().hide()
         self.w_admin_1 = AdminField(1, self.w_admin_0, gee=gee).hide()
         self.w_admin_2 = AdminField(2, self.w_admin_1, gee=gee).hide()
         self.w_vector = sw.VectorField(label=ms.aoi_sel.vector).hide()
         self.w_points = sw.LoadTableField(label=ms.aoi_sel.points).hide()
         if self.map_:
             self.w_draw = sw.TextField(label=ms.aoi_sel.aoi_name).hide()
+
+            # Change model feature name with event
+            def bind_name(change):
+                self.model.name = change["new"]
+
+            self.w_draw.observe(bind_name, "v_model")
+
         if self.ee:
             self.w_asset = sw.VectorField(
                 label=ms.aoi_sel.asset, gee=True, folder=self.folder, types=["TABLE"]
             ).hide()
 
         # group them together with the same key as the select_method object
         self.components = {
@@ -305,16 +312,15 @@
             self.model.bind(self.w_admin_0, "admin")
             .bind(self.w_admin_1, "admin")
             .bind(self.w_admin_2, "admin")
             .bind(self.w_vector, "vector_json")
             .bind(self.w_points, "point_json")
             .bind(self.w_method, "method")
         )
-        if self.map_:
-            self.model.bind(self.w_draw, "name")
+
         if self.ee:
             self.model.bind(self.w_asset, "asset_name")
 
         # add a validation btn
         self.btn = sw.Btn(ms.aoi_sel.btn)
 
         # create the widget
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/activate_venv` & `sepal-ui-2.9.4/sepal_ui/bin/activate_venv.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,22 +1,35 @@
-#!/usr/bin/python3
+"""
+Script to manually activate one of the venv available in the current Jupyter environment.
+
+Application are designed to run on specific venv, created to avoid lib deprecation.
+this script allows the user to easily activate one of the venv have already installed in Jupyter and customize it
+"""
+
 import subprocess
 from pathlib import Path
 import pandas as pd
 from colorama import init, Fore
+import argparse
 
 # init colors for all plateforms
 init()
 
-if __name__ == "__main__":
+parser = argparse.ArgumentParser(description=__doc__, usage="activate_venv")
+
+
+def main():
+
+    # parse agruments
+    parser.parse_args()
 
     print(
         f"{Fore.CYAN} Welcome to the virtual env activation, loading your venvs... \n{Fore.RESET}"
     )
-    
+
     # Get usr venvs
     result = subprocess.run(["jupyter", "kernelspec", "list"], stdout=subprocess.PIPE)
 
     venvs = pd.DataFrame(
         [
             line.split()
             for line in result.stdout.decode("utf-8").splitlines()
@@ -31,15 +44,14 @@
             list(
                 [f"test {el.name}", str(el)]
                 for el in test_venv_path.glob("[!.]*")
                 if el.is_dir()
             )
         )
         venvs = pd.concat([venvs, test_envs])
-    
     venvs = venvs.reset_index(drop=True)
     venvs.columns = ["env name", "path"]
 
     print(f"{Fore.CYAN} You can activate any of the following venvs: \n{Fore.RESET}")
     print(venvs)
 
     valid = False
@@ -52,15 +64,14 @@
             )
         )
 
         if selection not in venvs.index.unique():
             print(f"{Fore.RED}Your selection is not valid {Fore.RESET}")
         else:
             valid = True
-    
     # Activate virtual env
     kernel_path = Path(venvs.iloc[selection]["path"])
     test = "module-venv" in str(kernel_path)
 
     activate_path = "bin/activate" if test else "venv/bin/activate"
     print(f"{Fore.GREEN}Activating: {kernel_path} {Fore.RESET}")
 
@@ -73,8 +84,12 @@
     # The following lines won't be executed because the previous subprocess kill the kernel
 
     # Confirm that we are in the new env
     result = subprocess.run(
         ["echo", "$VIRTUAL_ENV"], shell=True, stdout=subprocess.PIPE
     )
 
-    print(f"The current env is: {result.stdout}")
+    print(f"The current env is: {result.stdout}")
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/module_deploy` & `sepal-ui-2.9.4/sepal_ui/bin/module_deploy.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,14 +20,17 @@
 
 from colorama import init, Fore, Style
 import sepal_ui
 
 # init colors for all plateforms
 init()
 
+# init parser
+parser = argparse.ArgumentParser(description=__doc__, usage="module_deploy")
+
 
 def write_reqs(file):
     """
     write the requirements in the requirements file
 
     Args:
         file (pathlib.Path): the requirements file
@@ -183,19 +186,18 @@
 
     except ValueError:
         pass
 
     return
 
 
-if __name__ == "__main__":
+def main():
 
     # parse agruments
-    p = argparse.ArgumentParser(usage=__doc__)
-    args = p.parse_args()
+    parser.parse_args()
 
     # welcome the user
     print(f"{Fore.YELLOW}sepal-ui module deployment tool{Fore.RESET}")
 
     print("Export the env configuration of your module...")
 
     # check that the local folder is a module folder
@@ -221,7 +223,11 @@
     freeze_sepal_ui(req_file)
 
     # exit message
     print(f'{Fore.GREEN}The "requirements.txt" file have been updated.{Fore.RESET}')
     print(
         f"{Fore.YELLOW}The tool does not cover every possible configuration so don't forget to check the final file before pushing to release.{Fore.RESET}"
     )
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/module_factory` & `sepal-ui-2.9.4/sepal_ui/bin/module_factory.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,14 +15,17 @@
 import argparse
 
 from colorama import init, Fore
 
 # init colors for all plateforms
 init()
 
+# init parser
+parser = argparse.ArgumentParser(description=__doc__, usage="module_factory")
+
 
 def set_default_readme(folder, module_name, description, url):
     """
     Write a default README.md file and overwrite the existing one.
 
     Args:
         folder (pathlib.Path): the module directory
@@ -180,19 +183,18 @@
     # write everything down again
     with ui.open("w") as f:
         f.write(ui_content)
 
     return
 
 
-if __name__ == "__main__":
+def main():
 
     # parse agruments
-    p = argparse.ArgumentParser(usage=__doc__)
-    args = p.parse_args()
+    parser.parse_args()
 
     # welcome the user
     print(f"{Fore.YELLOW}sepal-ui module factory{Fore.RESET}")
 
     print("Initializing module creation by setting up your module parameters")
     print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
 
@@ -303,22 +305,26 @@
     subprocess.run(["git", "push", "-u", "origin", "master"], cwd=folder)
 
     # create a release branch and push it to the server
     subprocess.run(["git", "checkout", "-b", "release"], cwd=folder)
     subprocess.run(["git", "push", "--set-upstream", "origin", "release"], cwd=folder)
 
     # checkout to master
-    res = subprocess.run(["git", "checkout", "master"], cwd=folder)
+    subprocess.run(["git", "checkout", "master"], cwd=folder)
 
     # exit message
     print(
         f"{Fore.YELLOW}Have a look to the git command executed in the process. if any of them is displaying an error, the final folder may not have been created{Fore.RESET}"
     )
     print(
         f"{Fore.YELLOW}If that's the case, delete the folder in your sepal instance (if there is any) and start the process again or contact us via github issues.{Fore.RESET}"
     )
     print(f"{Fore.GREEN}You created a new module named: {module_name}{Fore.RESET}")
     print(
         f"{Fore.GREEN}You can find its code in {folder} inside your sepal environment.{Fore.RESET}"
     )
     print()
     print("Let's code !")
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/module_l10n` & `sepal-ui-2.9.4/sepal_ui/bin/module_l10n.py`

 * *Files 7% similar despite different names*

```diff
@@ -13,33 +13,35 @@
 import argparse
 
 from sepal_ui.scripts import utils as su
 
 # init colors for all plateforms
 init()
 
+# init the parser
+parser = argparse.ArgumentParser(description=__doc__, usage="module_l10n")
+
 
 def check_locale(locale):
     """
     Check if the locale exist in the country list
 
     Return:
         (bool)
     """
 
     countries = pd.read_csv(Path(__file__).parents[1] / "scripts" / "locale.csv")
 
     return locale in countries.code.values
 
 
-if __name__ == "__main__":
+def main():
 
     # parse agruments
-    p = argparse.ArgumentParser(usage=__doc__)
-    args = p.parse_args()
+    parser.parse_args()
 
     # welcome the user
     print(f"{Fore.YELLOW}sepal-ui localisation script{Fore.RESET}")
 
     # select a language
     is_locale = False
     while is_locale is False:
@@ -56,7 +58,11 @@
     # write the new color code in the config file
     su.set_config_locale(locale)
 
     # display information
     print(
         f'{Fore.GREEN} The provided language code ("{locale}") has been set as default language for all SEPAL applications.{Fore.RESET}'
     )
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/module_theme` & `sepal-ui-2.9.4/sepal_ui/bin/module_theme.py`

 * *Files 12% similar despite different names*

```diff
@@ -12,33 +12,35 @@
 from colorama import init, Fore
 
 from sepal_ui.scripts import utils as su
 
 # init colors for all plateforms
 init()
 
+# init parser
+parser = argparse.ArgumentParser(description=__doc__, usage="module_theme")
+
 
 def check_theme(theme):
     """
     Check if the theme is a legit name
 
     Return:
         (bool)
     """
 
     themes = ["dark", "light"]
 
     return theme in themes
 
 
-if __name__ == "__main__":
+def main():
 
     # parse agruments
-    p = argparse.ArgumentParser(usage=__doc__)
-    args = p.parse_args()
+    parser.parse_args()
 
     # welcome the user
     print(f"{Fore.YELLOW}sepal-ui module theme selection{Fore.RESET}")
 
     # select a language
     is_theme = False
     while is_theme is False:
@@ -55,7 +57,11 @@
     # write the new color code in the config file
     su.set_config_theme(theme)
 
     # display information
     print(
         f'{Fore.GREEN} The provided theme ("{theme}") has been set as default theme for all SEPAL applications.{Fore.RESET}'
     )
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/bin/module_venv` & `sepal-ui-2.9.4/sepal_ui/bin/module_venv.py`

 * *Files 5% similar despite different names*

```diff
@@ -18,19 +18,22 @@
 import argparse
 
 from colorama import init, Fore
 
 # init colors for all plateforms
 init()
 
-if __name__ == "__main__":
+# init parser
+parser = argparse.ArgumentParser(description=__doc__, usage="module_venv")
+
+
+def main():
 
     # read arguments (there should be none)
-    p = argparse.ArgumentParser(usage=__doc__)
-    args = p.parse_args()
+    parser.parse_args()
 
     # welcome the user
     print(f"{Fore.YELLOW}venv creation interface{Fore.RESET}")
 
     # check that the local folder is a module folder
     ui_file = Path.cwd() / "ui.ipynb"
     if not ui_file.is_file():
@@ -109,7 +112,11 @@
 
     entry_point.write_text(json.dumps(data, indent=1))
 
     # display last message to the end user
     print(
         f'{Fore.GREEN}The test venv have been created, it can be found in the kernel list as "{display_name}". It has automatically been added to the entry point of the application: {entry_point.name}.{Fore.RESET}'
     )
+
+
+if __name__ == "__main__":
+    main()
```

### Comparing `sepal-ui-2.8.0/sepal_ui/frontend/js.py` & `sepal-ui-2.9.4/sepal_ui/frontend/js.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/mapping/fullscreen_control.py` & `sepal-ui-2.9.4/sepal_ui/mapping/fullscreen_control.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,106 +1,103 @@
 from ipyleaflet import WidgetControl
 from IPython.display import display
 import ipyvuetify as v
-from ipywidgets import Button, Layout
+
+from sepal_ui.mapping.map_btn import MapBtn
 
 
 class FullScreenControl(WidgetControl):
     """
     A custom Fullscreen Button ready to be embed in a map object.
 
     This button will force the display of the map in fullscreen mode. It should be used instead of the built-in ipyleaflet FullscreenControl if your map is embeding ipyvuetify widgets. I tends to solve the issue raised here: https://github.com/widgetti/ipyvuetify/issues/141. The idea is to fake the fullscreen display by forcing the map container to extend to the full extend of the screen without using a z-index superior to the ipyvuetify overlay.
     simply click on it and the map will automatically expand
 
     .. versionadded:: 2.7.0
 
     Args:
-        kwargs (optional): any availabel arguments from a ipyleaflet WidgetControl
+        m (SepalMap): the map on which the mutated CSS will be applied (Only work with SepalMap as we are querying the _id)
+        kwargs (optional): any available arguments from a ipyleaflet WidgetControl
     """
 
-    ICONS = ["arrows-alt", "compress"]
+    ICONS = ["fas fa-expand", "fas fa-compress"]
     "list: The icons that will be used to toggle between expand and compressed mode"
 
     METHODS = ["embed", "fullscreen"]
     "list: The javascript methods name to be used to switch from expand to compress mode"
 
     zoomed = False
     "bool: the current zoomed level (``True`` for expanded and ``False`` for compressed"
 
     w_btn = None
     "ipywidget.Button: the btn to display on the map"
 
     template = None
     "ipyvuetify.VuetifyTemplate: embeds the 2 javascripts methods to change the rendering of the map"
 
-    def __init__(self, **kwargs):
+    def __init__(self, m, **kwargs):
 
         # create a btn
-        self.w_btn = Button(
-            tooltip="set fullscreen",
-            icon=self.ICONS[self.zoomed],
-            layout=Layout(
-                width="30px", height="30px", line_height="30px", padding="0px"
-            ),
-        )
+        self.w_btn = MapBtn(logo=self.ICONS[self.zoomed])
 
         # overwrite the widget set in the kwargs (if any)
         kwargs["widget"] = self.w_btn
         kwargs["position"] = kwargs.pop("position", "topleft")
         kwargs["transparent_bg"] = True
 
         # create the widget
         super().__init__(**kwargs)
 
         # add javascrip behaviour
-        self.w_btn.on_click(self.toggle_fullscreen)
+        self.w_btn.on_event("click", self.toggle_fullscreen)
 
         # template with js behaviour
         # "jupyter_fullscreen" place tje "leaflet-container element on the front screen
         # and expand it's display to the full screen
         # "jupyter_embed" reset all the changed parameter
         # both trigger the resize event to force the reload of the Tilelayers
         self.template = v.VuetifyTemplate(
             template="""
         <script>
             {methods: {
                 jupyter_fullscreen() {
-                    var element = document.getElementsByClassName("leaflet-container")[0];
+                    var element = document.querySelector(".%s .leaflet-container");
                     element.style.position = "fixed";
                     element.style.width = "100vw";
                     element.style.height = "100vh";
                     element.style.zIndex = 800;
                     element.style.top = 0;
                     element.style.left = 0;
                     window.dispatchEvent(new Event('resize'));
                 },
                 jupyter_embed() {
-                    var element = document.getElementsByClassName("leaflet-container")[0];
+                    var element = document.querySelector(".%s .leaflet-container");
                     element.style.position = "";
                     element.style.width = "";
                     element.style.height = "";
                     element.style.zIndex = "";
                     element.style.top = "";
                     element.style.left = "";
                     window.dispatchEvent(new Event('resize'));
                 }
             }}
         </script>
         """
+            % (m._id, m._id)
         )
         display(self.template)
 
-    def toggle_fullscreen(self, widget):
+    def toggle_fullscreen(self, widget, event, data):
         """
         Toggle the fullscreen state of the map by sending the required javascript method, changing the w_btn icons and the zoomed state of the control.
         """
 
         # change the zoom state
         self.zoomed = not self.zoomed
 
         # change button icon
-        self.w_btn.icon = self.ICONS[self.zoomed]
+        self.w_btn.logo.children = [self.ICONS[self.zoomed]]
 
         # zoom
         self.template.send({"method": self.METHODS[self.zoomed], "args": []})
 
         return
```

### Comparing `sepal-ui-2.8.0/sepal_ui/mapping/mapping.py` & `sepal-ui-2.9.4/sepal_ui/mapping/sepal_map.py`

 * *Files 18% similar despite different names*

```diff
@@ -2,363 +2,250 @@
 import os
 
 if "GDAL_DATA" in list(os.environ.keys()):
     del os.environ["GDAL_DATA"]
 if "PROJ_LIB" in list(os.environ.keys()):
     del os.environ["PROJ_LIB"]
 
-import collections
 from pathlib import Path
 from distutils.util import strtobool
 import warnings
+import math
+import string
+import random
 
-import geemap
 from haversine import haversine
 import numpy as np
 import rioxarray
-import xarray_leaflet  # do not remove: plugin for rioxarray so it is never called but always used
+import xarray_leaflet
 import matplotlib.pyplot as plt
 from matplotlib import colors as mpc
 from matplotlib import colorbar
 import ipywidgets as widgets
-from ipyleaflet import (
-    AttributionControl,
-    DrawControl,
-    LayersControl,
-    LocalTileLayer,
-    ScaleControl,
-    WidgetControl,
-    ZoomControl,
-    GeoJSON,
-)
 from rasterio.crs import CRS
-from traitlets import Bool, link, observe
 import ipyvuetify as v
-import ipyleaflet
+import ipyleaflet as ipl
 import ee
+from deprecated.sphinx import deprecated
 
 import sepal_ui.frontend.styles as styles
 from sepal_ui.scripts import utils as su
 from sepal_ui.scripts.warning import SepalWarning
 from sepal_ui.message import ms
+from sepal_ui.mapping.draw_control import DrawControl
+from sepal_ui.mapping.value_inspector import ValueInspector
+from sepal_ui.mapping.layer import EELayer
+from sepal_ui.mapping.basemaps import basemap_tiles
 
 __all__ = ["SepalMap"]
 
-# call x_array leaflet at least one
+# call x_array leaflet at least once
 # flake8 will complain as it's a pluggin (i.e. never called)
 # We don't want to ignore testing F401
 xarray_leaflet
 
 
-class SepalMap(geemap.Map):
+class SepalMap(ipl.Map):
     """
-    The SepalMap class inherits from geemap.Map. It can thus be initialized with all its parameter.
-    The map will fall back to CartoDB.DarkMatter map that well fits with the rest of the sepal_ui layout.
-    Numerous methods have been added in the class to help you deal with your workflow implementation.
-    It can natively display raster from .tif files and files and ee objects using methods that have the same signature as the GEE JavaScripts console.
+    The SepalMap class inherits from ipyleaflet.Map. It can thus be initialized with all
+    its parameter.
+    The map will fall back to CartoDB.DarkMatter map that well fits with the rest of
+    the sepal_ui layout.
+    Numerous methods have been added in the class to help you deal with your workflow
+    implementation.
+    It can natively display raster from .tif files and files and ee objects using methods
+    that have the same signature as the GEE JavaScripts console.
 
     Args:
         basemaps ['str']: the basemaps used as background in the map. If multiple selection, they will be displayed as layers.
         dc (bool, optional): wether or not the drawing control should be displayed. default to false
         vinspector (bool, optional): Add value inspector to map, useful to inspect pixel values. default to false
         gee (bool, optional): wether or not to use the ee binding. If False none of the earthengine display fonctionalities can be used. default to True
-        kwargs (optional): any parameter from a geemap.Map. if set, 'ee_initialize' will be overwritten.
+        kwargs (optional): any parameter from a ipyleaflet.Map. if set, 'ee_initialize' will be overwritten.
     """
 
-    # ############################################################################
-    # ###                              Map parameters                          ###
-    # ############################################################################
+    # ##########################################################################
+    # ###                              Map parameters                        ###
+    # ##########################################################################
 
     ee = True
-    "bool: either the map will use geempa binding or not"
+    "bool: either the map will use ee binding or not"
 
-    vinspector = Bool(False).tag(sync=True)
-    "bool: either or not the datainspector is available"
-
-    loaded_rasters = {}
-    "dict: the list of loaded rasters"
+    v_inspector = None
+    "mapping.ValueInspector: the value inspector of the map"
 
     dc = None
     "ipyleaflet.DrawingControl: the drawing control of the map"
 
-    def __init__(self, basemaps=[], dc=False, vinspector=False, gee=True, **kwargs):
+    _id = None
+    "str: a unique 6 letters str to identify the map in the DOM"
 
-        self.world_copy_jump = True
+    def __init__(self, basemaps=[], dc=False, vinspector=False, gee=True, **kwargs):
 
         # set the default parameters
-        kwargs["ee_initialize"] = False  # we do it ourselves
-        kwargs["add_google_map"] = kwargs.pop("add_google_map", False)
         kwargs["center"] = kwargs.pop("center", [0, 0])
         kwargs["zoom"] = kwargs.pop("zoom", 2)
+        kwargs["basemap"] = {}
+        kwargs["zoom_control"] = False
+        kwargs["attribution_control"] = False
+        kwargs["scroll_wheel_zoom"] = True
+        kwargs["world_copy_jump"] = kwargs.pop("world_copy_jump", True)
 
         # Init the map
         super().__init__(**kwargs)
 
         # init ee
         self.ee = gee
-        if gee:
-            su.init_ee()
+        not gee or su.init_ee()
 
         # add the basemaps
         self.clear_layers()
-        if len(basemaps):
-            [self.add_basemap(basemap) for basemap in set(basemaps)]
-        else:
-            default_basemap = (
-                "CartoDB.DarkMatter" if v.theme.dark is True else "CartoDB.Positron"
-            )
-            self.add_basemap(default_basemap)
+        default_basemap = (
+            "CartoDB.DarkMatter" if v.theme.dark is True else "CartoDB.Positron"
+        )
+        basemaps = basemaps or [default_basemap]
+        [self.add_basemap(basemap) for basemap in set(basemaps)]
 
         # add the base controls
-        self.clear_controls()
-        self.add_control(ZoomControl(position="topright"))
-        self.add_control(LayersControl(position="topright"))
-        self.add_control(AttributionControl(position="bottomleft"))
-        self.add_control(ScaleControl(position="bottomleft", imperial=False))
-
-        # change the prefix
-        for control in self.controls:
-            if type(control) == AttributionControl:
-                control.prefix = "SEPAL"
+        self.add_control(ipl.ZoomControl(position="topright"))
+        self.add_control(ipl.LayersControl(position="topright"))
+        self.add_control(ipl.AttributionControl(position="bottomleft", prefix="SEPAL"))
+        self.add_control(ipl.ScaleControl(position="bottomleft", imperial=False))
 
         # specific drawing control
-        self.set_drawing_controls(dc)
-
-        # Add value inspector
-        self.w_vinspector = widgets.Checkbox(
-            value=False,
-            description="Inspect values",
-            indent=False,
-            layout=widgets.Layout(width="18ex"),
-        )
-
-        if vinspector:
-            self.add_control(
-                WidgetControl(widget=self.w_vinspector, position="topright")
-            )
-
-            link((self.w_vinspector, "value"), (self, "vinspector"))
-
-        # Create output space for raster interaction
-        self.output_r = widgets.Output(layout={"border": "1px solid black"})
-        self.output_control_r = WidgetControl(
-            widget=self.output_r, position="bottomright"
-        )
-        self.add_control(self.output_control_r)
-
-        # define interaction with rasters
-        self.on_interaction(self._raster_interaction)
-
-    @observe("vinspector")
-    def _change_cursor(self, change):
-        """Method to be called when vinspector trait changes"""
-
-        if self.vinspector:
-            self.default_style = {"cursor": "crosshair"}
-        else:
-            self.default_style = {"cursor": "grab"}
-
-        return
-
-    def _raster_interaction(self, **kwargs):
-        """Define a behavior when ispector checked and map clicked"""
-
-        if kwargs.get("type") == "click" and self.vinspector:
-            latlon = kwargs.get("coordinates")
-            self.default_style = {"cursor": "wait"}
-
-            local_rasters = [
-                lr.name for lr in self.layers if isinstance(lr, LocalTileLayer)
-            ]
-
-            if local_rasters:
-
-                with self.output_r:
-                    self.output_r.clear_output(wait=True)
-
-                    for lr_name in local_rasters:
-
-                        lr = self.loaded_rasters[lr_name]
-                        lat, lon = latlon
-
-                        # Verify if the selected latlon is the image bounds
-                        if any(
-                            [
-                                lat < lr.bottom,
-                                lat > lr.top,
-                                lon < lr.left,
-                                lon > lr.right,
-                            ]
-                        ):
-                            print("Location out of raster bounds")
-                        else:
-                            # row in pixel coordinates
-                            y = int(((lr.top - lat) / abs(lr.y_res)))
-
-                            # column in pixel coordinates
-                            x = int(((lon - lr.left) / abs(lr.x_res)))
-
-                            # get height and width
-                            h, w = lr.data.shape
-                            value = lr.data[y][x]
-                            print(f"{lr_name}")
-                            print(f"Lat: {round(lat,4)}, Lon: {round(lon,4)}")
-                            print(f"x:{x}, y:{y}")
-                            print(f"Pixel value: {value}")
-            else:
-                with self.output_r:
-                    self.output_r.clear_output()
-
-            self.default_style = {"cursor": "crosshair"}
+        self.dc = DrawControl(self)
+        not dc or self.add_control(self.dc)
 
-            return
-
-    def set_drawing_controls(self, add=False):
-        """
-        Create a drawing control for the map.
-        It will be possible to draw rectangles, circles and polygons.
-
-        Args:
-            add (bool): either to add the dc to the object attribute or not
+        # specific v_inspector
+        self.v_inspector = ValueInspector(self)
+        not vinspector or self.add_control(self.v_inspector)
+
+        # create a proxy ID to the element
+        # this id should be unique and will be used by mutators to identify this map
+        self._id = "".join(random.choice(string.ascii_lowercase) for i in range(6))
+        self.add_class(self._id)
 
-        return:
-            self
+    @deprecated(version="2.8.0", reason="the local_layer stored list has been dropped")
+    def _remove_local_raster(self, local_layer):
         """
+        Remove local layer from memory.
 
-        color = v.theme.themes.dark.info
-
-        dc = DrawControl(
-            edit=False,
-            marker={},
-            circlemarker={},
-            polyline={},
-            rectangle={"shapeOptions": {"color": color}},
-            circle={"shapeOptions": {"color": color}},
-            polygon={"shapeOptions": {"color": color}},
-        )
-
-        self.dc = dc if add else None
+        .. danger::
 
-        return self
-
-    def _remove_local_raster(self, local_layer):
-        """
-        Remove local layer from memory
+            Does nothing now.
 
         Args:
-            local_layer (str | geemap.layer): The local layer to remove or its name
+            local_layer (str | ipyleaflet.TileLayer): The local layer to remove or its name
 
         Return:
             self
         """
-        name = local_layer if type(local_layer) == str else local_layer.name
-
-        if name in self.loaded_rasters.keys():
-            self.loaded_rasters.pop(name)
 
         return self
 
+    @deprecated(version="2.8.0", reason="use remove_layer(-1) instead")
     def remove_last_layer(self, local=False):
         """
         Remove last added layer from Map
 
         Args:
             local (boolean): Specify True to only remove local last layers, otherwise will remove every last layer.
 
         Return:
             self
         """
-        if len(self.layers) > 1:
+        self.remove_layer(-1)
 
-            last_layer = self.layers[-1]
+        return self
 
-            if local:
-                local_rasters = [
-                    lr for lr in self.layers if isinstance(lr, LocalTileLayer)
-                ]
-                if local_rasters:
-                    last_layer = local_rasters[-1]
-                    self.remove_layer(last_layer)
-
-                    # If last layer is local_layer, remove it from memory
-                    if isinstance(last_layer, LocalTileLayer):
-                        self._remove_local_raster(last_layer)
-            else:
-                self.remove_layer(last_layer)
+    def set_center(self, lon, lat, zoom=None):
+        """
+        Centers the map view at a given coordinates with the given zoom level.
 
-                # If last layer is local_layer, remove it from memory
-                if isinstance(last_layer, LocalTileLayer):
-                    self._remove_local_raster(last_layer)
+        Args:
+            lon (float): The longitude of the center, in degrees.
+            lat	(float): The latitude of the center, in degrees.
+            zoom (int|optional): The zoom level, from 1 to 24. Defaults to None.
+        """
 
-        return self
+        self.center = [lat, lon]
+        self.zoom = self.zoom if zoom is None else zoom
+
+        return
 
     @su.need_ee
-    def zoom_ee_object(self, ee_geometry, zoom_out=1):
+    def zoom_ee_object(self, item, zoom_out=1):
         """
         Get the proper zoom to the given ee geometry.
 
         Args:
-            ee_geometry (ee.Geometry): the geometry to zoom on
+            item (ee.ComputedObject): the geometry to zoom on
             zoom_out (int) (optional): Zoom out the bounding zoom
 
         Return:
             self
         """
 
-        # center the image
-        self.centerObject(ee_geometry)
+        # type check the given object
+        ee_geometry = item if isinstance(item, ee.Geometry) else item.geometry()
 
         # extract bounds from ee_object
-        ee_bounds = ee_geometry.bounds().coordinates()
-        coords = ee_bounds.get(0).getInfo()
+        coords = ee_geometry.bounds().coordinates().get(0).getInfo()
 
-        # Get (x, y) of the 4 cardinal points
-        bl, br, tr, tl, _ = coords
+        # zoom on these bounds
+        return self.zoom_bounds((*coords[0], *coords[2]), zoom_out)
 
-        # Get (x, y) of the 4 cardinal points
-        min_lon, min_lat = bl
-        max_lon, max_lat = tr
+    def zoom_raster(self, layer, zoom_out=1):
+        """
+        Adapt the zoom to the given LocalLayer. The localLayer need to come from the add_raster method to embed the image name
 
-        # zoom on these bounds
-        self.zoom_bounds([min_lon, min_lat, max_lon, max_lat], zoom_out)
+        Args:
+            layer (LocalTileLayer): the localTile layer to zoom on. it needs to embed the "raster" member
+            zoom_out (int) (optional): Zoom out the bounding zoom
 
-        return self
+        Return:
+            self
+        """
+
+        da = rioxarray.open_rasterio(layer.raster, masked=True)
+
+        # unproject if necessary
+        epsg_4326 = "EPSG:4326"
+        if da.rio.crs != CRS.from_string(epsg_4326):
+            da = da.rio.reproject(epsg_4326)
+
+        return self.zoom_bounds(da.rio.bounds(), zoom_out)
 
     def zoom_bounds(self, bounds, zoom_out=1):
         """
         Adapt the zoom to the given bounds. and center the image.
 
         Args:
-            bounds ([coordinates]): coordinates corners as minx, miny, maxx, maxy
+            bounds ([coordinates]): coordinates corners as minx, miny, maxx, maxy in EPSG:4326
             zoom_out (int) (optional): Zoom out the bounding zoom
 
         Return:
             self
         """
 
         minx, miny, maxx, maxy = bounds
 
         # Center map to the centroid of the layer(s)
         self.center = [(maxy - miny) / 2 + miny, (maxx - minx) / 2 + minx]
 
-        tl = (minx, maxy)
-        bl = (minx, miny)
-        tr = (maxx, maxy)
-        br = (maxx, miny)
+        # create the tuples for each corner
+        tl, br, bl, tr = (minx, maxy), (maxx, miny), (minx, miny), (maxx, maxy)
 
+        # find zoom level to display the biggest diagonal (in km)
+        lg, zoom = 40075, 1  # number of displayed km at zoom 1
         maxsize = max(haversine(tl, br), haversine(bl, tr))
-
-        lg = 40075  # number of displayed km at zoom 1
-        zoom = 1
         while lg > maxsize:
-            zoom += 1
-            lg /= 2
+            (zoom, lg) = (zoom + 1, lg / 2)
 
-        if zoom_out > zoom:
-            zoom_out = zoom - 1
+        zoom_out = (zoom - 1) if zoom_out > zoom else zoom_out
 
         self.zoom = zoom - zoom_out
 
         return self
 
     def add_raster(
         self,
@@ -367,64 +254,61 @@
         layer_name="Layer_" + su.random_string(),
         colormap=plt.cm.inferno,
         x_dim="x",
         y_dim="y",
         opacity=1.0,
         fit_bounds=True,
         get_base_url=lambda _: "https://sepal.io/api/sandbox/jupyter",
-        colorbar_position="bottomright",
+        colorbar_position=False,
     ):
         """
         Adds a local raster dataset to the map.
 
         Args:
             image (str | pathlib.Path): The image file path.
             bands (int or list, optional): The image bands to use. It can be either a number (e.g., 1) or a list (e.g., [3, 2, 1]). Defaults to None.
-            layer_name (str, optional): The layer name to use for the raster. Defaults to None.
+            layer_name (str, optional): The layer name to use for the raster. Defaults to None. If a layer is already using this name 3 random letter will be added
             colormap (str, optional): The name of the colormap to use for the raster, such as 'gray' and 'terrain'. More can be found at https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html. Defaults to None.
             x_dim (str, optional): The x dimension. Defaults to 'x'.
             y_dim (str, optional): The y dimension. Defaults to 'y'.
             opacity (float, optional): the opacity of the layer, default 1.0.
             fit_bounds (bool, optional): Wether or not we should fit the map to the image bounds. Default to True.
             get_base_url (callable, optional): A function taking the window URL and returning the base URL to use. It's design to work in the SEPAL environment, you only need to change it if you want to work outside of our platform. See xarray-leaflet lib for more details.
-            colorbar_position (str, optional): The position of the colorbar (default to "bottomright"). set to False to remove it.
+            colorbar_position (str, optional): The position of the colorbar. By default set to False to remove it.
+
+        Return:
+            (LocalTileLayer) the local tile layer embeding the raster member (to be used with other tools of sepal-ui)
         """
 
-        if type(image) == str:
-            image = Path(image)
+        # force cast to Path
+        image = Path(image)
 
         if not image.is_file():
             raise Exception(ms.mapping.no_image)
 
         # check inputs
-        if layer_name in self.loaded_rasters.keys():
+        if layer_name in [layer.name for layer in self.layers]:
             layer_name = layer_name + su.random_string()
 
         if isinstance(colormap, str):
             colormap = plt.cm.get_cmap(name=colormap)
 
         da = rioxarray.open_rasterio(image, masked=True)
 
-        # The dataset can be too big to hold in memory, so we will chunk it into smaller pieces.
-        # That will also improve performances as the generation of a tile can be done in parallel using Dask.
+        # The dataset can be too big to hold in memory, so we will chunk it into smaller
+        # pieces.
+        # That will also improve performances as the generation of a tile can be done
+        # in parallel using Dask.
         da = da.chunk((1000, 1000))
 
         # unproject if necessary
         epsg_4326 = "EPSG:4326"
         if da.rio.crs != CRS.from_string(epsg_4326):
             da = da.rio.reproject(epsg_4326)
 
-        # Create a named tuple with raster bounds and resolution
-        local_raster = collections.namedtuple(
-            "LocalRaster",
-            ("name", "left", "bottom", "right", "top", "x_res", "y_res", "data"),
-        )(layer_name, *da.rio.bounds(), *da.rio.resolution(), da.data[0])
-
-        self.loaded_rasters[layer_name] = local_raster
-
         multi_band = False
         if len(da.band) > 1 and type(bands) != int:
             multi_band = True
             if not bands:
                 bands = [3, 2, 1]
         elif len(da.band) == 1:
             bands = 1
@@ -437,58 +321,43 @@
 
         kwargs = {
             "m": self,
             "x_dim": x_dim,
             "y_dim": y_dim,
             "fit_bounds": fit_bounds,
             "get_base_url": get_base_url,
-            # 'colorbar_position': colorbar_position, # will be uncoment when the colobared version of xarray-leaflet will be released
+            "colorbar_position": colorbar_position,
             "rgb_dim": "band" if multi_band else None,
             "colormap": None if multi_band else colormap,
         }
 
         # display the layer on the map
         layer = da.leaflet.plot(**kwargs)
-
         layer.name = layer_name
-
         layer.opacity = opacity if abs(opacity) <= 1.0 else 1.0
 
-        return
+        # add the da to the layer as an extra member for the v_inspector
+        layer.raster = str(image)
 
+        return layer
+
+    @deprecated(version="2.8.0", reason="use dc methods instead")
     def show_dc(self):
         """
         show the drawing control on the map
-
-        Return:
-            self
         """
-
-        if self.dc:
-            self.dc.clear()
-
-            if self.dc not in self.controls:
-                self.add_control(self.dc)
-
+        self.dc.show()
         return self
 
+    @deprecated(version="2.8.0", reason="use dc methods instead")
     def hide_dc(self):
         """
         hide the drawing control of the map
-
-        Return:
-            self
         """
-
-        if self.dc:
-            self.dc.clear()
-
-            if self.dc in self.controls:
-                self.remove_control(self.dc)
-
+        self.dc.hide()
         return self
 
     def add_colorbar(
         self,
         colors,
         cmap="viridis",
         vmin=0,
@@ -515,15 +384,14 @@
             height (str, optional): The height of the colormap widget. Defaults to "45px".
             position (str, optional): The position for the colormap widget. Defaults to "bottomright".
             layer_name (str, optional): Layer name of the colorbar to be associated with. Defaults to None.
             kwargs (any): any other argument of the colorbar object from matplotlib
         """
 
         width, height = 6.0, 0.4
-
         alpha = 1
 
         if colors is not None:
 
             # transform colors in hex colors
             hexcodes = [su.to_colors(c) for c in colors]
 
@@ -538,17 +406,16 @@
 
         elif cmap is not None:
 
             cmap = plt.get_cmap(cmap)
             norm = mpc.Normalize(vmin=vmin, vmax=vmax)
 
         else:
-            raise ValueError(
-                'cmap keyword or "palette" key in vis_params must be provided.'
-            )
+            msg = '"cmap" keyword or "colors" key must be provided.'
+            raise ValueError(msg)
 
         style = "dark_background" if v.theme.dark is True else "classic"
 
         with plt.style.context(style):
             fig, ax = plt.subplots(figsize=(width, height))
             cb = colorbar.ColorbarBase(
                 ax,
@@ -561,49 +428,44 @@
 
             # cosmetic improvement
             cb.outline.set_visible(False)  # remove border of the color bar
             ax.tick_params(size=0)  # remove ticks
             fig.patch.set_alpha(0.0)  # remove bg of the fig
             ax.patch.set_alpha(0.0)  # remove bg of the ax
 
-        if layer_name:
-            cb.set_label(layer_name)
+        not layer_name or cb.set_label(layer_name)
 
         output = widgets.Output()
-        colormap_ctrl = ipyleaflet.WidgetControl(
+        colormap_ctrl = ipl.WidgetControl(
             widget=output,
             position=position,
             transparent_bg=True,
         )
         with output:
             output.clear_output()
             plt.show()
 
-        self.colorbar = colormap_ctrl
-        if layer_name in self.ee_layer_names:
-            if "colorbar" in self.ee_layer_dict[layer_name]:
-                self.remove_control(self.ee_layer_dict[layer_name]["colorbar"])
-            self.ee_layer_dict[layer_name]["colorbar"] = colormap_ctrl
-
         self.add_control(colormap_ctrl)
 
         return
 
-    def addLayer(
+    def add_ee_Layer(
         self,
         ee_object,
         vis_params={},
         name=None,
         shown=True,
         opacity=1.0,
         viz_name=False,
     ):
         """
-        Override the addLayer method from geemap to read the guess the vizaulization parameters the same way as in SEPAL recipes.
-        If the vizparams are empty and vizualization metadata exist, SepalMap will use them automatically.
+        Copy the addLayer method from geemap to read and guess the vizaulization
+        parameters the same way as in SEPAL recipes.
+        If the vizparams are empty and vizualization metadata exist, SepalMap will use
+        them automatically.
 
         Args:
             ee_object (ee.Object): the ee OBject to draw on the map
             vis_params (dict, optional): the visualization parameters set as in GEE
             name (str, optional): the name of the layer
             shown (bool, optional): either to show the layer or not, default to true (it is bugged in ipyleaflet)
             opacity (float, optional): the opcity of the layer from 0 to 1, default to 1.
@@ -691,35 +553,100 @@
                     )
                     asset = asset.addBands(asset.expression(exp), [band], True)
 
                 # set the arguments
                 ee_object = asset.select(vis_params["bands"]).hsvToRgb()
                 vis_params["bands"] = ["red", "green", "blue"]
 
-        # call the function using the replacing the empty viz params with the new one.
-        super().addLayer(ee_object, vis_params, name, shown, opacity)
+        # create the layer based on these new values
+        image = None
+
+        if name is None:
+            layer_count = len(self.layers)
+            name = "Layer " + str(layer_count + 1)
+
+        # check the type of the ee object and raise an error if it's not recognized
+        if not isinstance(
+            ee_object,
+            (
+                ee.Image,
+                ee.ImageCollection,
+                ee.FeatureCollection,
+                ee.Feature,
+                ee.Geometry,
+            ),
+        ):
+            raise AttributeError(
+                "\n\nThe image argument in 'addLayer' function must be an instance of "
+                "one of ee.Image, ee.Geometry, ee.Feature or ee.FeatureCollection."
+            )
+
+        # force cast to featureCollection if needed
+        if isinstance(
+            ee_object,
+            (
+                ee.geometry.Geometry,
+                ee.feature.Feature,
+                ee.featurecollection.FeatureCollection,
+            ),
+        ):
+
+            features = ee.FeatureCollection(ee_object)
+
+            width = vis_params.pop("width", 2)
+            color = vis_params.pop("color", "000000")
+
+            const_image = ee.Image.constant(0.5)
+            image_fill = features.style(fillColor=color).updateMask(const_image)
+            image_outline = features.style(
+                color=color, fillColor="00000000", width=width
+            )
+
+            image = image_fill.blend(image_outline)
+            obj = features
+
+        # use directly the ee object if Image
+        elif isinstance(ee_object, ee.image.Image):
+            image = obj = ee_object
+
+        # use mosaicing if the ee_object is a ImageCollection
+        elif isinstance(ee_object, ee.imagecollection.ImageCollection):
+            image = obj = ee_object.mosaic()
+
+        # create the colored image
+        map_id_dict = ee.Image(image).getMapId(vis_params)
+        tile_layer = EELayer(
+            ee_object=obj,
+            url=map_id_dict["tile_fetcher"].url_format,
+            attribution="Google Earth Engine",
+            name=name,
+            opacity=opacity,
+            visible=shown,
+            max_zoom=24,
+        )
+
+        self.add_layer(tile_layer)
 
         return
 
     @staticmethod
     def get_basemap_list():
         """
         This function is intending for development use
         It give the list of all the available basemaps for SepalMap object
-
         Return:
             ([str]): the list of the basemap names
         """
 
-        return [k for k in geemap.ee_basemaps.keys()]
+        return [k for k in basemap_tiles.keys()]
 
     @staticmethod
     def get_viz_params(image):
         """
-        Return the vizual parmaeters that are set in the metadata of the image
+        Return the vizual parameters that are set in the metadata of the image
 
         Args:
             image (ee.Image): the image to analyse
 
         Return:
             (dict): the dictionnary of the find properties
         """
@@ -774,32 +701,141 @@
                 # if no "type" is provided guess it from the different parameters gathered
                 if len(props[i]["bands"]) == 1:
                     props[i]["type"] = "continuous"
                 elif len(props[i]["bands"]) == 3:
                     props[i]["type"] = "rgb"
                 else:
                     warnings.warn(
-                        "the embed viz properties are incomplete or badly set, please review our documentation",
+                        "the embed viz properties are incomplete or badly set, "
+                        "please review our documentation",
                         SepalWarning,
                     )
                     props = {}
 
         return props
 
+    def remove_layer(self, key, base=False, none_ok=False):
+        """
+        Remove a layer based on a key. The key can be, a Layer object, the name of a
+        layer or the index in the layer list
+
+        Args:
+            key (Layer, int, str): the key to find the layer to delete
+            base (bool, optional): either the basemaps should be included in the search or not. default t false
+            none_ok (bool, optional): if True the function will not raise error if no layer is found. Default to False
+        """
+
+        layer = self.find_layer(key, base, none_ok)
+
+        # catch if the layer doesn't exist
+        if layer is None:
+            raise ipl.LayerException(f"layer not on map: {key}")
+
+        super().remove_layer(layer)
+
+        return
+
+    def remove_all(self, base=False):
+        """
+        Remove all the layers from the maps.
+        If base is set to True, the basemaps are removed as well
+
+        Args:
+            base (bool, optional): wether or not the basemaps should be removed, default to False
+        """
+        # filter out the basemaps if base == False
+        layers = self.layers if base else [lyr for lyr in self.layers if not lyr.base]
+
+        # remove them using the layer objects as keys
+        [self.remove_layer(layer, base) for layer in layers]
+
+        return
+
     def add_layer(self, layer, hover=False):
-        """Add layer and use a default style for the GeoJSON inputs
+        """
+        Add layer and use a default style for the GeoJSON inputs.
+        Remove existing layer if already on the map.
 
+        layer (ipyleaflet.Layer): any layer type from ipyleaflet
         hover (bool): whether to use the default hover style or not.
+        """
+
+        # remove existing layer before addition
+        existing_layer = self.find_layer(layer.name, none_ok=True)
+        not existing_layer or self.remove_layer(existing_layer)
+
+        # apply default coloring for geoJson
+        if isinstance(layer, ipl.GeoJSON):
+            layer.style = layer.style or styles.layer_style
+            hover_style = styles.layer_hover_style if hover else layer.hover_style
+            layer.hover_style = layer.hover_style or hover_style
 
+        super().add_layer(layer)
+
+        return
+
+    def add_basemap(self, basemap="HYBRID"):
         """
+        Adds a basemap to the map.
 
-        if isinstance(layer, GeoJSON):
+        Args:
+            basemap (str, optional): Can be one of string from basemaps. Defaults to 'HYBRID'.
+        """
+        if basemap not in basemap_tiles.keys():
+            keys = "\n".join(basemap_tiles.keys())
+            msg = f"Basemap can only be one of the following:\n{keys}"
+            raise ValueError(msg)
 
-            if not layer.style:
-                layer.style = styles.layer_style
+        self.add_layer(basemap_tiles[basemap])
 
-            if hover and not layer.hover_style:
-                layer.hover_style = styles.layer_hover_style
+        return
 
-        super().add_layer(layer)
+    def get_scale(self):
+        """
+        Returns the approximate pixel scale of the current map view, in meters.
+        Reference: https://blogs.bing.com/maps/2006/02/25/map-control-zoom-levels-gt-resolution
 
-        return self
+        Returns:
+            (float): Map resolution in meters.
+        """
+
+        return 156543.04 * math.cos(0) / math.pow(2, self.zoom)
+
+    def find_layer(self, key, base=False, none_ok=False):
+        """
+        Search a layer by name or index
+
+        Args:
+            key (Layer, str, int): the layer name, index or directly the layer
+            base (bool, optional): either the basemaps should be included in the search or not. default to false
+            none_ok (bool, optional): if True the function will not raise error if no layer is found. Default to False
+
+        Return:
+            (TileLLayerayer): the first layer using the same name or index else None
+        """
+
+        # filter the layers
+        layers = self.layers if base else [lyr for lyr in self.layers if not lyr.base]
+
+        if isinstance(key, str):
+            layer = next((lyr for lyr in layers if lyr.name == key), None)
+        elif isinstance(key, int):
+            size = len(layers)
+            layer = layers[key] if -size <= key < size else None
+        elif isinstance(key, ipl.Layer):
+            layer = next((lyr for lyr in layers if lyr == key), None)
+        else:
+            raise ValueError(f"key must be a int or a str, {type(key)} given")
+
+        if layer is None and none_ok is False:
+            raise ValueError(f"no layer corresponding to {key} on the map")
+
+        return layer
+
+    # ##########################################################################
+    # ###                overwrite geemap calls                              ###
+    # ##########################################################################
+
+    setCenter = set_center
+    centerObject = zoom_ee_object
+    addLayer = add_ee_Layer
+    getScale = get_scale
```

### Comparing `sepal-ui-2.8.0/sepal_ui/message/en/locale.json` & `sepal-ui-2.9.4/sepal_ui/message/en/locale.json`

 * *Files 17% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8662561576354679%*

 * *Differences: {"'aoi_sel'": "{'exception': OrderedDict([('no_inputs', 'Please provide fully qualified inputs "*

 * *              "before validating your AOI'), ('no_asset', 'Please select an asset.'), ('no_value', "*

 * *              "'Please select a value.'), ('uncomplete', 'All fields are required, please fill "*

 * *              "them.'), ('no_file', 'Please select a file.'), ('duplicate_key', 'A key is "*

 * *              'duplicated in your selection. Please select different columns for your latitude, '*

 * *              "longitude an […]*

```diff
@@ -12,22 +12,32 @@
         "asset_already_exist": "The asset was already existing you can continue to use it. It's also available at :{}",
         "asset_created": "The asset has been created under the name : {}",
         "btn": "Select AOI",
         "check_if_asset": "Check carefully that your string is an assetId",
         "complete": "The AOI has been selected",
         "custom": "Custom geometries",
         "draw": "Drawn shapes",
-        "duplicate_key": "A key is duplicated in your selection. Please select different columns for your latitude, longitude and Id parameters",
+        "exception": {
+            "duplicate_key": "A key is duplicated in your selection. Please select different columns for your latitude, longitude and Id parameters",
+            "invalid_code": "The code is not in the database",
+            "no_admlyr": "Select an administrative layer",
+            "no_asset": "Please select an asset.",
+            "no_draw": "Please draw a shape in the map",
+            "no_file": "Please select a file.",
+            "no_gdf": "You must set the gdf before interacting with it",
+            "no_inputs": "Please provide fully qualified inputs before validating your AOI",
+            "no_value": "Please select a value.",
+            "uncomplete": "All fields are required, please fill them."
+        },
         "file_pattern": "aoi_{}",
         "geojson_to_ee": "Convert your .csv file into a ee_object",
         "method": "AOI selection method",
         "name_used": "The name was already in used, change it or delete the previous asset in your GEE acount",
         "no_asset": "No Asset has been provided",
         "no_country": "No Country has been selected",
-        "no_inputs": "Provided fully qualified inputs before validating your AOI",
         "no_selection": "No selection method has been picked up",
         "no_shape": "No shape has been drawn on the map",
         "not_available": "This function is not yet available",
         "points": "Point file",
         "shape_drawn": "A shape has been drawn",
         "shp_error": "An error occured with provided .shp file",
         "title": "Select Area Of Interest (AOI)",
@@ -43,14 +53,36 @@
     "locale": {
         "change": "The locale \"{0}\" will now be used as default language in SEPAL apps. Please restart the current application to take this change into account. Note that if \"{0}\" is not avalaible in another application, SEPAL will fallback to the closest possible language",
         "fallback": "The \"{0}\" locale is not available for this application. We will be using \"{1}\" instead. Please report to the maintainer if you want to add \"{0}\" to the suported languages."
     },
     "mapping": {
         "no_image": "The image file does not exist."
     },
+    "planet": {
+        "exception": {
+            "empty": "Please fill the required field(s).",
+            "format": "Please check the format of your inputs.",
+            "invalid": "Invalid email or password",
+            "nosubs": "Your credentials do not have any valid planet subscription."
+        },
+        "status": {
+            "offilne": "Not connected",
+            "online": "Connected"
+        },
+        "widget": {
+            "apikey": "Planet API key",
+            "method": {
+                "api_key": "Planet API key",
+                "credentials": "Credentials",
+                "label": "Login method"
+            },
+            "password": "Planet password",
+            "username": "Planet username"
+        }
+    },
     "rec": {
         "rec": {
             "btn": "Reclassify",
             "export": {
                 "0": {
                     "0": "The Vector has been created and added to your SEPAL Folder: {}",
                     "1": "The Image has been created and added to your SEPAL folder: {}"
@@ -164,12 +196,35 @@
             },
             "wrong_type": "The type of the selected asset ({}) does not match authorized asset type ({})."
         },
         "banner": {
             "close": "close",
             "next": "next ({} more)"
         },
+        "fileinput": {
+            "label": "search file",
+            "placeholder": "Selected file"
+        },
         "load_table": {
             "too_small": "The provided file have less than 3 columns. Please provide a complete point file with at least ID, lattitude and longitude columns."
+        },
+        "navdrawer": {
+            "bug": "Bug report",
+            "code": "Source code",
+            "wiki": "Wiki"
+        },
+        "table": {
+            "column": {
+                "id": "id",
+                "lat": "latitude",
+                "lng": "longitude"
+            },
+            "label": "Table file"
+        },
+        "vector": {
+            "all": "Use all features",
+            "column": "column",
+            "label": "Vector file",
+            "value": "value"
         }
     }
 }
```

### Comparing `sepal-ui-2.8.0/sepal_ui/message/es/locale.json` & `sepal-ui-2.9.4/sepal_ui/message/es/locale.json`

 * *Files 17% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8320821360153257%*

 * *Differences: {"'aoi_sel'": "{'administrative': 'Límites administrativos', 'adm': {'1': 'Nivel administrativo "*

 * *              "1', '2': 'Nivel administrativo 2'}, 'draw': 'Dibujar figura(s) en el mapa', "*

 * *              "'aoi_name': 'Crea un nombre para tu AOI', 'btn': 'Usar selección', 'complete': 'El "*

 * *              "AOI ha sido seleccionada', 'no_selection': 'No has elegido ningún método de "*

 * *              "selección', 'no_country': 'No has seleccionado ningún país', 'exception': "*

 * *              "OrderedDict([('no_inpu […]*

```diff
@@ -1,34 +1,44 @@
 {
     "aoi_sel": {
         "adm": {
             "0": "Pa\u00eds/Provincia",
-            "1": "Nivel de administraci\u00f3n 1",
-            "2": "Nivel de administraci\u00f3n 2"
+            "1": "Nivel administrativo 1",
+            "2": "Nivel administrativo 2"
         },
-        "administrative": "Definiciones administrativas",
+        "administrative": "L\u00edmites administrativos",
         "aoi_message": "haga clic en \"seleccionar estas opciones\" para validar su AOI.",
-        "aoi_name": "Seleccionar un nombre de AOI",
+        "aoi_name": "Crea un nombre para tu AOI",
         "asset": "Nombre del asset",
         "asset_already_exist": "El Asset ya existe, puede seguir utiliz\u00e1ndolo. Est\u00e1 disponible en :{}",
         "asset_created": "El Asset ya ha sido creado bajo el nombre: {}",
-        "btn": "Seleccione estas entradas",
+        "btn": "Usar selecci\u00f3n",
         "check_if_asset": "Compruebe que su cadena es un assetId",
-        "complete": "La AOI ha sido seleccionada",
+        "complete": "El AOI ha sido seleccionada",
         "custom": "Geometr\u00edas personalizadas",
-        "draw": "Figuras dibujadas",
-        "duplicate_key": "Hay una llave duplicada en su selecci\u00f3n. Por favor, seleccione diferentes columnas para los par\u00e1metros de latitud, longitud e identificaci\u00f3n",
+        "draw": "Dibujar figura(s) en el mapa",
+        "exception": {
+            "duplicate_key": "",
+            "invalid_code": "",
+            "no_admlyr": "",
+            "no_asset": "",
+            "no_draw": "",
+            "no_file": "",
+            "no_gdf": "",
+            "no_inputs": "",
+            "no_value": "",
+            "uncomplete": ""
+        },
         "file_pattern": "aoi_{}",
         "geojson_to_ee": "Convierta su archivo .csv en un objeto de Google Earth Engine",
         "method": "M\u00e9todo de selecci\u00f3n de AOI",
         "name_used": "El nombre ya est\u00e1 en uso, c\u00e1mbielo o borre el archivo anterior en su cuenta de GEE",
         "no_asset": "No se ha seleccionado ning\u00fan Asset",
-        "no_country": "No se ha seleccionado ning\u00fan pa\u00eds",
-        "no_inputs": "Proporcione entradas completas antes de validar su AOI",
-        "no_selection": "No se ha recogido ning\u00fan m\u00e9todo de selecci\u00f3n",
+        "no_country": "No has seleccionado ning\u00fan pa\u00eds",
+        "no_selection": "No has elegido ning\u00fan m\u00e9todo de selecci\u00f3n",
         "no_shape": "No se ha dibujado ninguna forma en el mapa",
         "not_available": "Esta funci\u00f3n a\u00fan no est\u00e1 disponible",
         "points": "Archivo de puntos",
         "shape_drawn": "Se ha dibujado una figura",
         "shp_error": "Ocurri\u00f3 un error con el shapefile seleccionado",
         "title": "Seleccionar \u00e1rea de inter\u00e9s (AOI)",
         "vector": "Archivo vectorial"
@@ -37,31 +47,53 @@
         "p": {
             "0": "La FAO declina toda responsabilidad respecto de los errores o deficiencias en la base de datos o los programas, o en la documentaci\u00f3n que la acompa\u00f1a a \u00e9stos, el mantenimiento y el mejoramiento del programa, as\u00ed como por cualquier da\u00f1o que pueda derivarse de ellos.",
             "1": "Asimismo, la FAO no se considerar\u00e1 responsable de la actualizaci\u00f3n de los datos y no asume ning\u00fan tipo de responsabilidad respecto de los errores u omisiones en los datos proporcionados.",
             "2": "No obstante, se ruega a los usuarios que informen de los errores o deficiencias que hallen en este producto de la FAO."
         }
     },
     "locale": {
-        "change": "",
-        "fallback": ""
+        "change": "La configuraci\u00f3n regional \"{0}\" ser\u00e1 usada como idioma predeterminado en las aplicaciones de SEPAL. Por favor, reinicia la aplicaci\u00f3n actual para aplicar los cambios. Ten en cuenta que si \"{0}\" no est\u00e1 disponible en otra aplicaci\u00f3n, SEPAL usar\u00e1 el idioma m\u00e1s cercano posible.",
+        "fallback": "La configuraci\u00f3n regional \"{0}\" no est\u00e1 disponible para esta aplicaci\u00f3n. En su lugar usaremos \"{1}\". Por favor, informa al mantenedor de la aplicaci\u00f3n si deseas a\u00f1adir \"{0}\" a los idiomas soportados."
     },
     "mapping": {
         "no_image": "El archivo de imagen no existe"
     },
+    "planet": {
+        "exception": {
+            "empty": "Por favor completa todos los campos",
+            "format": "Por favor verifica el formato de tus entradas",
+            "invalid": "Correo electr\u00f3nico o contrase\u00f1a inv\u00e1lidos",
+            "nosubs": "Tus credenciales no tienen asociada ninguna suscripci\u00f3n v\u00e1lida de Planet."
+        },
+        "status": {
+            "offilne": "Desconectado",
+            "online": "Conectado"
+        },
+        "widget": {
+            "apikey": "API key",
+            "method": {
+                "api_key": "API key",
+                "credentials": "Credenciales",
+                "label": "M\u00e9todo de inicio de sesi\u00f3n"
+            },
+            "password": "Contrase\u00f1a",
+            "username": "Nombre de usuario"
+        }
+    },
     "rec": {
         "rec": {
             "btn": "Reclasificar",
             "export": {
                 "0": {
-                    "0": "",
-                    "1": ""
+                    "0": "El vector ha sido creado y a\u00f1adido a tu cuenta de SEPAL: {}",
+                    "1": "La imagen ha sido creada y a\u00f1adida a tu cuenta de SEPAL: {}"
                 },
                 "1": {
-                    "0": "",
-                    "1": ""
+                    "0": "El FeatureCollection ha sido exportado a GEE como {}. Utiliza la interfaz del editor de c\u00f3digo para seguir el proceso de exportaci\u00f3n.",
+                    "1": "La imagen ha sido exportada a GEE como {}. Utiliza la interfaz del editor de c\u00f3digo para seguir el proceso de exportaci\u00f3n."
                 }
             },
             "headers": {
                 "0": "Clase originale",
                 "1": "Clase de destino"
             },
             "input": {
@@ -162,14 +194,37 @@
                 "3": "Algoritmo",
                 "4": "Directorio"
             },
             "wrong_type": "El tipo del asset seleccionado: ({}), no coincide con ninguno de los tipos permitidos por el widget: ({})."
         },
         "banner": {
             "close": "cerrar",
-            "next": ""
+            "next": "siguiente ({} m\u00e1s)"
+        },
+        "fileinput": {
+            "label": "buscar archivos",
+            "placeholder": "Archivo seleccionado"
         },
         "load_table": {
-            "too_small": "El archivo indicado tiene menos de 3 columnas. Por favor, indique un archivo de puntos completo con al menos las columnas de ID, latitud y longitud."
+            "too_small": "El archivo ingresado contiene menos de 3 columnas. Por favor, selecciona un archivo de puntos completo con al menos las columnas de ID, latitud y longitud."
+        },
+        "navdrawer": {
+            "bug": "Reportar error",
+            "code": "C\u00f3digo fuente",
+            "wiki": "Wiki"
+        },
+        "table": {
+            "column": {
+                "id": "id",
+                "lat": "latitud",
+                "lng": "longitud"
+            },
+            "label": "Tabla de archivos"
+        },
+        "vector": {
+            "all": "Usar todos los features",
+            "column": "columna",
+            "label": "Archivo vectorial",
+            "value": "Valor"
         }
     }
 }
```

### Comparing `sepal-ui-2.8.0/sepal_ui/message/fr/locale.json` & `sepal-ui-2.9.4/sepal_ui/message/fr/locale.json`

 * *Files 18% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8662561576354679%*

 * *Differences: {"'aoi_sel'": "{'exception': OrderedDict([('no_inputs', 'Merci de fournir des entrées entièrement "*

 * *              "définies avant de valider votre AOI'), ('no_asset', 'Veuillez sélectionner un asset "*

 * *              "Earthengine.'), ('no_value', 'Veuillez sélectionner une valeur.'), ('uncomplete', "*

 * *              "'Tous les champs sont obligatoires, merci de les remplir.'), ('no_file', 'Veuillez "*

 * *              'sélectionner un fichier.\'), (\'duplicate_key\', "Une clef est dupliquée dans votre '*

 * *            […]*

```diff
@@ -12,22 +12,32 @@
         "asset_already_exist": "L'asset existe d\u00e9j\u00e0, vous pouvez continuer de l'utiliser. Il est disponible ici : {}",
         "asset_created": "L'asset a \u00e9t\u00e9 cr\u00e9\u00e9e sous le nom : {}",
         "btn": "Selectionner cet AOI",
         "check_if_asset": "Verifier attentivement que vous avez utiliser une asset ID valide",
         "complete": "L'AOI a \u00e9t\u00e9 selectionn\u00e9e",
         "custom": "G\u00e9ometries personnalis\u00e9es",
         "draw": "Dessiner une forme",
-        "duplicate_key": "Une clef est dupliqu\u00e9e dans votre selection. Veuillez selectionner des colonnes diff\u00e9rentes pour la latitude, la longitude et l'identifiant",
+        "exception": {
+            "duplicate_key": "Une clef est dupliqu\u00e9e dans votre selection. Veuillez selectionner des colonnes diff\u00e9rentes pour la latitude, la longitude et l'id",
+            "invalid_code": "Le code administratif n'est pas dans la base de donn\u00e9es.",
+            "no_admlyr": "S\u00e9lectionnez une couche administrative",
+            "no_asset": "Veuillez s\u00e9lectionner un asset Earthengine.",
+            "no_draw": "Veuillez dessiner une forme sur la carte",
+            "no_file": "Veuillez s\u00e9lectionner un fichier.",
+            "no_gdf": "Vous devez d\u00e9finir le gdf avant d'interagir avec celui-ci",
+            "no_inputs": "Merci de fournir des entr\u00e9es enti\u00e8rement d\u00e9finies avant de valider votre AOI",
+            "no_value": "Veuillez s\u00e9lectionner une valeur.",
+            "uncomplete": "Tous les champs sont obligatoires, merci de les remplir."
+        },
         "file_pattern": "aoi_{}",
         "geojson_to_ee": "Convertir votre fichier .csv en object Google Earth Engine",
         "method": "Methode de selection d'AOI",
         "name_used": "L'asset est d\u00e9j\u00e0 utilis\u00e9, vous pouvez changer le nom de fichier ou supprimer celui d\u00e9j\u00e0 pr\u00e9sent de votre compte GEE",
         "no_asset": "Aucun asset n'a \u00e9t\u00e9 renseign\u00e9",
         "no_country": "Aucun pays selectionn\u00e9",
-        "no_inputs": "Fournir des entr\u00e9es enti\u00e8rement qualifi\u00e9es avant de valider votre AOI",
         "no_selection": "Aucune methode de selection n'a \u00e9t\u00e9 choisie",
         "no_shape": "Aucune figure n'a \u00e9t\u00e9 dessin\u00e9 sur la carte",
         "not_available": "Cette fonction n'est pas encore disponible",
         "points": "Fichier de point",
         "shape_drawn": "Une forme a \u00e9t\u00e9 dessin\u00e9e",
         "shp_error": "Une erreur est survenue avec le fichier .shp utilis\u00e9",
         "title": "Selectionner la zone d'inter\u00eat (AOI)",
@@ -43,14 +53,36 @@
     "locale": {
         "change": "La locale \"{0}\" sera maintenant utilis\u00e9e comme langue par d\u00e9faut dans les applications SEPAL. Veuillez red\u00e9marrer l'application actuelle pour tenir compte de cette modification. Notez que si \u00ab{0}\u00bb n'est pas disponible dans une autre application, SEPAL se repliera sur la langue la plus proche possible",
         "fallback": "La locale \"{0}\" n'est pas disponible pour cette application. Nous allons utiliser \"{1}\" sera utiliser \u00e0 la place. Veuillez le signaler au developeurs si vous voulez ajouter \"{0}\" aux langues suport\u00e9es."
     },
     "mapping": {
         "no_image": "Le fichier image n'existe pas."
     },
+    "planet": {
+        "exception": {
+            "empty": "Veuillez renseigner tous les champs obligatoires.",
+            "format": "Merci de v\u00e9rifier le format de vos donn\u00e9es.",
+            "invalid": "Email ou mot de passe invalide",
+            "nosubs": "Vos identifiants n'ont pas d'abonnement PlanetLab valide."
+        },
+        "status": {
+            "offilne": "Non connect\u00e9",
+            "online": "Connect\u00e9"
+        },
+        "widget": {
+            "apikey": "Cl\u00e9 API PlanetLab",
+            "method": {
+                "api_key": "Cl\u00e9 API PlanetLab",
+                "credentials": "Identifiants",
+                "label": "M\u00e9thode d'acc\u00e8s"
+            },
+            "password": "Mot de passe PlanetLab",
+            "username": "Nom d'utilisateur PlanetLab"
+        }
+    },
     "rec": {
         "rec": {
             "btn": "Reclassifer",
             "export": {
                 "0": {
                     "0": "Le Vecteur a \u00e9t\u00e9 cr\u00e9\u00e9 et ajout\u00e9 \u00e0 votre dossier SEPAL: {}",
                     "1": "L'Image a \u00e9t\u00e9 cr\u00e9\u00e9 et ajout\u00e9 \u00e0 votre dossier SEPAL: {}"
@@ -164,12 +196,35 @@
             },
             "wrong_type": "Le type de l'asset selection\u00e9 ({}) ne correspond pas aux type autoris\u00e9s par le widget ({})."
         },
         "banner": {
             "close": "fermer",
             "next": "suivant ({} de plus)"
         },
+        "fileinput": {
+            "label": "chercher un fichier",
+            "placeholder": "Fichier s\u00e9lectionn\u00e9"
+        },
         "load_table": {
             "too_small": "Le fichier fourni comporte moins de 3 colonnes. Veuillez fournir un fichier de points complet avec au moins les colonnes ID, lattitude et longitude."
+        },
+        "navdrawer": {
+            "bug": "Signaler un Bug",
+            "code": "Code source",
+            "wiki": "Wiki"
+        },
+        "table": {
+            "column": {
+                "id": "Id",
+                "lat": "latitude",
+                "lng": "longitude"
+            },
+            "label": "Fichier de tableau"
+        },
+        "vector": {
+            "all": "Utiliser toutes les features",
+            "column": "colonne",
+            "label": "Fichier de vecteur",
+            "value": "valeur"
         }
     }
 }
```

### Comparing `sepal-ui-2.8.0/sepal_ui/model/model.py` & `sepal-ui-2.9.4/sepal_ui/model/model.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_model.py` & `sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_model.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_tile.py` & `sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_tile.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/reclassify/reclassify_view.py` & `sepal-ui-2.9.4/sepal_ui/reclassify/reclassify_view.py`

 * *Files 0% similar despite different names*

```diff
@@ -294,15 +294,15 @@
 
         return self
 
 
 class ReclassifyView(sw.Card):
     """
     Stand-alone Card object allowing the user to reclassify a input file. the input can be of any type (vector or raster) and from any source (local or GEE).
-    The user need to provide a destination classification file (table) in the following format : 3 headless columns: 'code', 'desc', 'color'. Once all the old class have been attributed to their new class the file can be exported in the source format to local memory or GEE. the output is also savec in memory for further use in the app. It can be used as a tile in a sepal_ui app. The id_ of the tile is set to "reclassify_tile"
+    The user need to provide a destination classification file (table) in the following format : 3 headless columns: 'code', 'desc', 'color'. Once all the old class have been attributed to their new class the file can be exported in the source format to local memory or GEE. the output is also savec in memory for further use in the app. It can be used as a tile in a sepal_ui app. The id\_ of the tile is set to "reclassify_tile"
 
     Args:
         model (ReclassifyModel): the reclassify model to manipulate the
             classification dataset. default to a new one
         class_path (str,optional): Folder path containing already existing
             classes. Default to ~/
         out_path (str,optional): the folder to save the created classifications.
```

### Comparing `sepal-ui-2.8.0/sepal_ui/reclassify/table_view.py` & `sepal-ui-2.9.4/sepal_ui/reclassify/table_view.py`

 * *Files 0% similar despite different names*

```diff
@@ -527,15 +527,15 @@
         self.v_model = False
 
         return
 
 
 class TableView(sw.Card):
     """
-    Stand-alone Card object allowing the user to build custom class table. The user can start from an existing table or start from scratch. It gives the oportunity to change: the value, the class name and the color. It can be used as a tile in a sepal_ui app. The id_ of the tile is set to "classification_tile"
+    Stand-alone Card object allowing the user to build custom class table. The user can start from an existing table or start from scratch. It gives the oportunity to change: the value, the class name and the color. It can be used as a tile in a sepal_ui app. The id\_ of the tile is set to "classification_tile"
 
     Args:
         class_path (str|optional): Folder path containing already existing classes. Default to ~/
         out_path (str|optional): the folder to save the created classifications. default to ~/downloads
     """
 
     title = None
```

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/encrypted_key.json` & `sepal-ui-2.9.4/sepal_ui/scripts/encrypted_key.json`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/gadm_database.csv` & `sepal-ui-2.9.4/sepal_ui/scripts/gadm_database.csv`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/gaul_database.csv` & `sepal-ui-2.9.4/sepal_ui/scripts/gaul_database.csv`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/gee.py` & `sepal-ui-2.9.4/sepal_ui/scripts/gee.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/locale.csv` & `sepal-ui-2.9.4/sepal_ui/scripts/locale.csv`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/scripts/utils.py` & `sepal-ui-2.9.4/sepal_ui/scripts/utils.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,29 +1,27 @@
+from configparser import ConfigParser
 import os
 from pathlib import Path
 from urllib.parse import urlparse
 import string
 import random
 import math
 import re
 import warnings
 from unidecode import unidecode
 from functools import wraps
 from itertools import product
-from configparser import ConfigParser
 
 import ee
 from cryptography.fernet import Fernet
 from matplotlib import colors as c
-from deprecated.sphinx import deprecated, versionadded
+from deprecated.sphinx import versionadded, deprecated
 
 import sepal_ui
-
-from sepal_ui import config_file
-from sepal_ui.frontend.styles import TYPES
+from sepal_ui.conf import config_file, config
 from .warning import SepalWarning
 
 
 def hide_component(widget):
     """
     hide a vuetify based component
 
@@ -83,43 +81,25 @@
     # but I don't really understand how it works
     # so here is an ugly fix only compatible with SEPAL
     link = f"https://sepal.io/api/sandbox/jupyter/files/{download_path}"
 
     return link
 
 
-@deprecated(
-    version="2.5.4",
-    reason="This function makes no sense outside of create_download_link. It will be removed in the next minor version",
-)
-def is_absolute(url):
-    """
-    Check if the given URL is an absolute or relative path
-
-    Args:
-        url (str): the URL to test
-
-    Return:
-        (bool): True if absolute else False
-    """
-    return bool(urlparse(str(url)).netloc)
-
-
 def random_string(string_length=3):
     """
     Generates a random string of fixed length.
 
     Args:
         string_length (int, optional): Fixed length. Defaults to 3.
 
     Return:
         (str): A random string
     """
 
-    # random.seed(1001)
     letters = string.ascii_lowercase
 
     return "".join(random.choice(letters) for i in range(string_length))
 
 
 def get_file_size(filename):
     """
@@ -492,14 +472,41 @@
         string = "_".join(split[:-1]) + f"_{int(end)+1}"
     else:
         string += "_1"
 
     return string
 
 
+def set_config(key, value, section="sepal-ui"):
+    """
+    Set the provided value to the given key for the given section in the sepal-ui config
+    file
+
+    Args:
+        key (str): key configuration name
+        value (str): value to be referenced by the configuration key
+        section (str, optional): configuration section, defaults to sepal-ui.
+    """
+
+    # set the section if needed
+    if "sepal-ui" not in config.sections():
+        config.add_section(section)
+
+    # set the value
+    config.set("sepal-ui", key, value)
+
+    # save back the file
+    config.write(config_file.open("w"))
+
+    return
+
+
+@deprecated(
+    version="2.9.1", reason="This function will be removed in favor of set_config()"
+)
 @versionadded(version="2.7.0")
 def set_config_locale(locale):
     """
     Set the provided local in the sepal-ui config file
 
     Args:
         locale (str): a locale name in IETF BCP 47 (no verifications are performed)
@@ -520,14 +527,17 @@
 
     # save back the file
     config.write(config_file.open("w"))
 
     return
 
 
+@deprecated(
+    version="2.9.1", reason="This function will be removed in favor of set_config()"
+)
 @versionadded(version="2.7.0")
 def set_config_theme(theme):
     """
     Set the provided theme in the sepal-ui config file
 
     Args:
         theme (str): a theme name (currently supporting "dark" and "light")
@@ -551,26 +561,73 @@
 
     return
 
 
 @versionadded(version="2.7.1")
 def set_type(color):
     """
-    Return a pre-defined material colors based on the requested type_ parameter. If the parameter is not a predifined color,
+    Return a pre-defined material colors based on the requested type\_ parameter. If the parameter is not a predifined color,
     fallback to "info" and will raise a warning. the colors can only be selected from ["primary", "secondary", "accent", "error", "info", "success", "warning", "anchor"]
 
     Args:
         color (str): the requested color
 
     Returns:
         (str): a pre-defined material color
 
     """
+    from sepal_ui.frontend.styles import TYPES
 
     if color not in TYPES:
         warnings.warn(
             f'the selected color "{color}" is not a pre-defined material color. It should be one from [{", ".join(TYPES)}]',
             SepalWarning,
         )
         color = TYPES[0]
 
     return color
+
+
+@versionadded(version="2.8.0")
+def geojson_to_ee(geo_json, geodesic=False, encoding="utf-8"):
+    """
+    Transform a geojson object into a featureCollection or a Geometry
+    No sanity check is performed on the initial geo_json. It must respect the
+    `__geo_interface__ <https://gist.github.com/sgillies/2217756>`__.
+
+    Args:
+        geo_json (dict): a geo_json dictionnary
+        geodesic (bool, optional): Whether line segments should be interpreted as spherical geodesics. If false, indicates that line segments should be interpreted as planar lines in the specified CRS. If absent, defaults to True if the CRS is geographic (including the default EPSG:4326), or to False if the CRS is projected. Defaults to False.
+        encoding (str, optional): The encoding of characters. Defaults to "utf-8".
+
+    Returns:
+        (ee.FeatureCollection): the created featurecollection
+    """
+
+    # from a featureCollection
+    if geo_json["type"] == "FeatureCollection":
+        for feature in geo_json["features"]:
+            if feature["geometry"]["type"] != "Point":
+                feature["geometry"]["geodesic"] = geodesic
+        features = ee.FeatureCollection(geo_json)
+        return features
+
+    # from a single feature
+    elif geo_json["type"] == "Feature":
+        geom = None
+        # Checks whether it is a point
+        if geo_json["geometry"]["type"] == "Point":
+            coordinates = geo_json["geometry"]["coordinates"]
+            longitude = coordinates[0]
+            latitude = coordinates[1]
+            geom = ee.Geometry.Point(longitude, latitude)
+        # for every other geometry simply create a geometry
+        else:
+            geom = ee.Geometry(geo_json["geometry"], "", geodesic)
+
+        return geom
+
+    # some error handling because we are fancy
+    else:
+        raise ValueError("Could not convert the geojson to ee.Geometry()")
+
+    return
```

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/__init__.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/__init__.py`

 * *Files 16% similar despite different names*

```diff
@@ -27,7 +27,8 @@
 # import and/or overwrite with our customized widgets
 from sepal_ui.sepalwidgets.widget import *
 from sepal_ui.sepalwidgets.alert import *
 from sepal_ui.sepalwidgets.btn import *
 from sepal_ui.sepalwidgets.app import *
 from sepal_ui.sepalwidgets.tile import *
 from sepal_ui.sepalwidgets.inputs import *
+from sepal_ui.sepalwidgets.sepalwidget import Tooltip
```

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/alert.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/alert.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 from datetime import datetime
 
 from ipywidgets import jslink
 import ipyvuetify as v
-from deprecated.sphinx import deprecated
 from traitlets import Unicode, observe, directional_link, Bool
 
 from sepal_ui.sepalwidgets.sepalwidget import SepalWidget
 from sepal_ui.scripts.utils import set_type
 from sepal_ui.frontend.styles import TYPES
 from sepal_ui.message import ms
 
@@ -16,19 +15,19 @@
 class Divider(v.Divider, SepalWidget):
     """
     A custom Divider with the ability to dynamically change color
     Whenever the type\_ trait is modified, the divider class will change accordingly
 
     Args:
         class\_ (str, optional): the initial color of the divider
-        kwargs (optional): any parameter from a v.Divider. if set, 'class_' will be overwritten.
+        kwargs (optional): any parameter from a v.Divider. if set, 'class\_' will be overwritten.
     """
 
     type_ = Unicode("").tag(sync=True)
-    "str: Added type_ trait to specify the current color of the divider"
+    "str: Added type\_ trait to specify the current color of the divider"
 
     def __init__(self, class_="", **kwargs):
         kwargs["class_"] = class_
         super().__init__(**kwargs)
 
     @observe("type_")
     def add_class_type(self, change):
@@ -222,59 +221,14 @@
         """
 
         self.children = [""]
         self.hide()
 
         return self
 
-    @deprecated(version="2.1.0", reason="use a Model object instead")
-    def bind(self, widget, obj, attribute, msg=None, verbose=True, secret=False):
-        """
-        Bind the attribute to the widget and display it in the alert.
-        The binded input need to have an active `v_model` trait.
-        After the binding, whenever the `v_model` of the input is changed, the io attribute is changed accordingly.
-        The value can also be displayed in the alert with a custom message with the following format = `[custom message] + [v_model]`
-
-        Args:
-            widget (v.XX): an ipyvuetify input element with an activated `v_model` trait
-            obj (io): any io object
-            attribute (str): the name of the attribute in io object
-            msg (str, optionnal): the output message displayed before the variable
-            verbose (bool, optional): wheter the variable should be displayed to the user
-            secret (bool, optional): either if the variable is secret or not. If true only "*" will be shown in the output
-
-        Return:
-            self
-        """
-        if not msg:
-            msg = "The selected variable is: "
-
-        def _on_change(change, obj=obj, attribute=attribute, msg=msg):
-
-            # if the key doesn't exist the getattr function will raise an AttributeError
-            getattr(obj, attribute)
-
-            # change the obj value
-            setattr(obj, attribute, change["new"])
-
-            # add the message if needed
-            if secret:
-                msg += "*" * len(str(change["new"]))
-            else:
-                msg += str(change["new"])
-
-            if verbose:
-                self.add_msg(msg)
-
-            return
-
-        widget.observe(_on_change, "v_model")
-
-        return self
-
     def check_input(self, input_, msg=None):
         """
         Check if the inpupt value is initialized.
         If not return false and display an error message else return True
 
         Args:
             input\_ (any): the input to check
```

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/app.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/app.py`

 * *Files 1% similar despite different names*

```diff
@@ -251,21 +251,27 @@
 
     def __init__(self, items=[], code=None, wiki=None, issue=None, **kwargs):
 
         self.items = items
 
         code_link = []
         if code:
-            item_code = DrawerItem("Source code", icon="far fa-file-code", href=code)
+            item_code = DrawerItem(
+                ms.widgets.navdrawer.code, icon="far fa-file-code", href=code
+            )
             code_link.append(item_code)
         if wiki:
-            item_wiki = DrawerItem("Wiki", icon="fas fa-book-open", href=wiki)
+            item_wiki = DrawerItem(
+                ms.widgets.navdrawer.wiki, icon="fas fa-book-open", href=wiki
+            )
             code_link.append(item_wiki)
         if issue:
-            item_bug = DrawerItem("Bug report", icon="fas fa-bug", href=issue)
+            item_bug = DrawerItem(
+                ms.widgets.navdrawer.bug, icon="fas fa-bug", href=issue
+            )
             code_link.append(item_bug)
 
         children = [
             v.List(dense=True, children=self.items),
             v.Divider(),
             v.List(dense=True, children=code_link),
         ]
@@ -460,15 +466,15 @@
             for i in items:
                 if name == i._metadata["card_id"]:
                     i.input_value = True
 
         return self
 
     @versionadded(version="2.4.1", reason="New end user interaction method")
-    @versionchanged(version="2.7.1", reason="new id_ and persistent parameters")
+    @versionchanged(version="2.7.1", reason="new id\_ and persistent parameters")
     def add_banner(self, msg="", type_="info", id_=None, persistent=True, **kwargs):
         """
         Display an snackbar object on top of the app to communicate development information to end user (release date, known issues, beta version). The alert is dissmisable and prominent.
 
         Args:
             *args: all required sw.Banner arguments.
             **kwargs: any arguments of the sw.Banner constructor. if set, 'children' will be overwritten.
@@ -667,15 +673,15 @@
         self.btn.children = [
             v.Html(tag="img", attributes=attr, class_="mr-1"),
             loc.code,
         ]
         self.btn.color = "info"
 
         # change the paramater file
-        su.set_config_locale(loc.code)
+        su.set_config("locale", loc.code)
 
         return
 
 
 class ThemeSelect(v.Btn, SepalWidget):
     """
     A theme selector for sepal-ui based application.
@@ -694,15 +700,15 @@
 
     theme = "dark"
     "str: the current theme of the widget (default to dark)"
 
     def __init__(self, **kwargs):
 
         # get the current theme name
-        self.theme = sepal_ui.get_theme(sepal_ui.config_file)
+        self.theme = sepal_ui.get_theme()
 
         # set the btn parameters
         kwargs["x_small"] = kwargs.pop("x_small", True)
         kwargs["fab"] = kwargs.pop("fab", True)
         kwargs["class_"] = kwargs.pop("class_", "ml-2")
         kwargs["children"] = [v.Icon(children=[self.THEME_ICONS[self.theme]])]
         kwargs["v_model"] = self.theme
@@ -723,13 +729,13 @@
         self.theme = next(t for t in theme_cycle)
 
         # change icon
         self.color = "info"
         self.children[0].children = [self.THEME_ICONS[self.theme]]
 
         # change the paramater file
-        su.set_config_theme(self.theme)
+        su.set_config("theme", self.theme)
 
         # trigger other events by changing v_model
         self.v_model = self.theme
 
         return
```

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/btn.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/btn.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/inputs.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/inputs.py`

 * *Files 2% similar despite different names*

```diff
@@ -193,28 +193,31 @@
     v_model = Unicode(None, allow_none=True).tag(sync=True)
     "str: the v_model of the input"
 
     def __init__(
         self,
         extentions=[],
         folder=Path.home(),
-        label="search file",
+        label=ms.widgets.fileinput.label,
         v_model=None,
         clearable=False,
         **kwargs,
     ):
 
         if type(folder) == str:
             folder = Path(folder)
 
         self.extentions = extentions
         self.folder = folder
 
         self.selected_file = v.TextField(
-            readonly=True, label="Selected file", class_="ml-5 mt-5", v_model=None
+            readonly=True,
+            label=ms.widgets.fileinput.placeholder,
+            class_="ml-5 mt-5",
+            v_model=None,
         )
 
         self.loading = v.ProgressLinear(
             indeterminate=False,
             background_color=color.menu,
             color=COMPONENTS["PROGRESS_BAR"]["color"][v.theme.dark],
         )
@@ -465,26 +468,35 @@
         "pathname": None,
         "id_column": None,
         "lat_column": None,
         "lng_column": None,
     }
     "dict: The default v_model structure {'pathname': xx, 'id_column': xx, 'lat_column': xx, 'lng_column': xx}"
 
-    def __init__(self, label="Table file", **kwargs):
+    def __init__(self, label=ms.widgets.table.label, **kwargs):
 
         self.fileInput = FileInput([".csv", ".txt"], label=label)
 
         self.IdSelect = v.Select(
-            _metadata={"name": "id_column"}, items=[], label="Id", v_model=None
+            _metadata={"name": "id_column"},
+            items=[],
+            label=ms.widgets.table.column.id,
+            v_model=None,
         )
         self.LngSelect = v.Select(
-            _metadata={"name": "lng_column"}, items=[], label="Longitude", v_model=None
+            _metadata={"name": "lng_column"},
+            items=[],
+            label=ms.widgets.table.column.lng,
+            v_model=None,
         )
         self.LatSelect = v.Select(
-            _metadata={"name": "lat_column"}, items=[], label="Latitude", v_model=None
+            _metadata={"name": "lat_column"},
+            items=[],
+            label=ms.widgets.table.column.lat,
+            v_model=None,
         )
 
         # set default parameters
         kwargs["v_model"] = self.default_v_model  # format of v_model is fixed
         kwargs["children"] = [
             self.fileInput,
             self.IdSelect,
@@ -712,15 +724,15 @@
 
             self.valid = self.error_messages is None
             self.error = self.error_messages is not None
 
         return
 
     @su.switch("loading", "disabled")
-    def _get_items(self, change=None):
+    def _get_items(self, *args):
 
         # get the list of user asset
         raw_assets = gee.get_assets(self.folder)
 
         assets = {
             k: sorted([e["id"] for e in raw_assets if e["type"] == k])
             for k in self.types
@@ -881,40 +893,43 @@
             "column": None,
             "value": None,
         }
     )
     "Traitlet: The json saved v_model shaped as {'pathname': xx, 'column': xx, 'value': xx}"
 
     column_base_items = [
-        {"text": "Use all features", "value": "ALL"},
+        {"text": ms.widgets.vector.all, "value": "ALL"},
         {"divider": True},
     ]
     "list: the column compulsory selector (ALL)"
 
     feature_collection = None
     "ee.FeatureCollection: the selected featureCollection"
 
-    def __init__(self, label="vector_file", gee=False, **kwargs):
+    def __init__(self, label=ms.widgets.vector.label, gee=False, **kwargs):
 
         # set the 3 wigets
         if not gee:
             self.w_file = FileInput([".shp", ".geojson", ".gpkg", ".kml"], label=label)
         else:
             # Don't care about 'types' arg. It will only work with tables.
             asset_select_kwargs = {"folder": kwargs.pop("folder", None)}
             self.w_file = AssetSelect(types=["TABLE"], **asset_select_kwargs)
 
         self.w_column = v.Select(
             _metadata={"name": "column"},
             items=self.column_base_items,
-            label="Column",
+            label=ms.widgets.vector.column,
             v_model="ALL",
         )
         self.w_value = v.Select(
-            _metadata={"name": "value"}, items=[], label="Value", v_model=None
+            _metadata={"name": "value"},
+            items=[],
+            label=ms.widgets.vector.value,
+            v_model=None,
         )
         su.hide_component(self.w_value)
 
         # create the Col Field
         kwargs["children"] = [self.w_file, self.w_column, self.w_value]
 
         super().__init__(**kwargs)
```

### Comparing `sepal-ui-2.8.0/sepal_ui/sepalwidgets/tile.py` & `sepal-ui-2.9.4/sepal_ui/sepalwidgets/tile.py`

 * *Files identical despite different names*

### Comparing `sepal-ui-2.8.0/sepal_ui/translator/translator.py` & `sepal-ui-2.9.4/sepal_ui/translator/translator.py`

 * *Files 4% similar despite different names*

```diff
@@ -162,15 +162,16 @@
 
     @classmethod
     def sanitize(cls, d):
         """
         Identify numbered dictionnaries embeded in the dict and transform them into lists
 
         This function is an helper to prevent deprecation after the introduction of pontoon for translation.
-        The user is now force to use keys even for numbered lists. SimpleNamespace doesn't support integer indexing so this function will transform back this "numbered" dictionnary (with integer keys) into lists.
+        The user is now force to use keys even for numbered lists. SimpleNamespace doesn't support integer indexing
+        so this function will transform back this "numbered" dictionnary (with integer keys) into lists.
 
         Args:
             d (dict): the dictionnary to sanitize
 
         Return:
             (dict): the sanitized dictionnary
         """
@@ -248,22 +249,46 @@
 
     @versionadded(version="2.7.0")
     @classmethod
     def merge_dict(cls, folder):
         """
         gather all the .json file in the provided l10n folder as 1 single json dict
 
-        the json dict will be sanitysed and the key will be used as if they were coming from 1 single file. be careful with duplication
+        the json dict will be sanitysed and the key will be used as if they were coming from 1 single file.
+        be careful with duplication. empty string keys will be removed.
 
         Args:
             folder (pathlib.path)
 
         Return:
             (dict): the json dict with all the keys
 
         """
 
         final_json = {}
         for f in folder.glob("*.json"):
-            final_json = {**final_json, **cls.sanitize(json.loads(f.read_text()))}
+            tmp_dict = cls.delete_empty(json.loads(f.read_text()))
+            final_json = {**final_json, **cls.sanitize(tmp_dict)}
 
         return final_json
+
+    @versionadded(version="2.8.1")
+    @classmethod
+    def delete_empty(cls, d):
+        """
+        Remove empty strings ("") recursively from the dictionaries. This is to prevent untranslated strings from
+        Crowdin to be uploaded. The dictionnary must only embed dictionnaries and no lists.
+
+        Args:
+            d (dict): the dictionnary to sanitize
+
+        Return:
+            (dict): the sanitized dictionnary
+
+        """
+        for k, v in list(d.items()):
+            if isinstance(v, dict):
+                cls.delete_empty(v)
+            elif v == "":
+                del d[k]
+
+        return d
```

### Comparing `sepal-ui-2.8.0/sepal_ui.egg-info/PKG-INFO` & `sepal-ui-2.9.4/sepal_ui.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 Metadata-Version: 2.1
 Name: sepal-ui
-Version: 2.8.0
+Version: 2.9.4
 Summary: Wrapper for ipyvuetify widgets to unify the display of voila dashboards in SEPAL platform
 Home-page: https://github.com/12rambau/sepal_ui
 Author: Pierrick Rambaud
 Author-email: pierrick.rambaud49@gmail.com
 License: MIT
-Download-URL: https://github.com/12rambau/sepal_ui/archive/v_2.8.0.tar.gz
+Download-URL: https://github.com/12rambau/sepal_ui/archive/v_2.9.4.tar.gz
 Keywords: UI,Python,widget,sepal
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
 Classifier: License :: OSI Approved :: MIT License
-Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Python: >=3.6.9
 Description-Content-Type: text/x-rst
 Provides-Extra: dev
 Provides-Extra: test
@@ -28,14 +27,18 @@
 
 Sepal_ui
 --------
 
 .. image:: https://img.shields.io/badge/License-MIT-yellow.svg
     :target: https://opensource.org/licenses/MIT
     :alt: License: MIT
+    
+.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.6467835.svg
+   :target: https://doi.org/10.5281/zenodo.6467835
+   :alt: Citation
 
 .. image:: https://badge.fury.io/py/sepal-ui.svg
     :target: https://badge.fury.io/py/sepal-ui
     :alt: PyPI version
     
 .. image:: https://img.shields.io/pypi/dm/sepal-ui?color=307CC2&logo=python&logoColor=gainsboro  
     :target: https://pypi.org/project/sepal-ui/
@@ -75,21 +78,21 @@
    
 --------------------------------------------------------------------------------
 
 Currently translated in the following languages:
 
 .. csv-table::
 
-    English, Français, Español
+    English, Français, Español, 中国人
 
 You can contribute to the translation effort on our `crowdin project <https://crowdin.com/project/sepal-ui>`__.
 
 --------------------------------------------------------------------------------
 
-:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the SEPAL environment. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
+:code:`sepal_ui` is a lib designed to create elegant python based dashboard in the `SEPAL environment <https://sepal.io/>`__. It is designed on top of the amazing `ipyvuetify <https://ipyvuetify.readthedocs.io/en/latest/introduction.html>`_ library and will help developer to easily create interface for their workflows. 
 By using this libraries, you'll ensure a robust and unified interface for your scripts and a easy and complete integration into the SEPAL dashboard of application.
 
 The full documentation is available `here <https://sepal-ui.readthedocs.io/en/latest/>`__ and a demo app can be launched on Heroku following this link: `<https://sepal-ui.herokuapp.com>`__.
 
 We are happy to receive feedback and we welcome any kind of contribution.
 
 .. image:: https://raw.githubusercontent.com/12rambau/sepal_ui/master/docs/source/_image/sepal_ui_screenshot.png
```

### Comparing `sepal-ui-2.8.0/sepal_ui.egg-info/SOURCES.txt` & `sepal-ui-2.9.4/sepal_ui.egg-info/SOURCES.txt`

 * *Files 19% similar despite different names*

```diff
@@ -1,38 +1,53 @@
 LICENSE.txt
 README.rst
 setup.py
 sepal_ui/__init__.py
+sepal_ui/conf.py
 sepal_ui.egg-info/PKG-INFO
 sepal_ui.egg-info/SOURCES.txt
 sepal_ui.egg-info/dependency_links.txt
+sepal_ui.egg-info/entry_points.txt
 sepal_ui.egg-info/requires.txt
 sepal_ui.egg-info/top_level.txt
 sepal_ui/aoi/__init__.py
 sepal_ui/aoi/aoi_model.py
 sepal_ui/aoi/aoi_tile.py
 sepal_ui/aoi/aoi_view.py
-sepal_ui/bin/activate_venv
-sepal_ui/bin/module_deploy
-sepal_ui/bin/module_factory
-sepal_ui/bin/module_l10n
-sepal_ui/bin/module_theme
-sepal_ui/bin/module_venv
+sepal_ui/bin/activate_venv.py
+sepal_ui/bin/module_deploy.py
+sepal_ui/bin/module_factory.py
+sepal_ui/bin/module_l10n.py
+sepal_ui/bin/module_theme.py
+sepal_ui/bin/module_venv.py
 sepal_ui/frontend/__init__.py
 sepal_ui/frontend/js.py
 sepal_ui/frontend/styles.py
 sepal_ui/mapping/__init__.py
+sepal_ui/mapping/basemaps.py
+sepal_ui/mapping/draw_control.py
 sepal_ui/mapping/fullscreen_control.py
-sepal_ui/mapping/mapping.py
+sepal_ui/mapping/layer.py
+sepal_ui/mapping/map_btn.py
+sepal_ui/mapping/sepal_map.py
+sepal_ui/mapping/value_inspector.py
 sepal_ui/message/__init__.py
+sepal_ui/message/ar-SA/locale.json
 sepal_ui/message/en/locale.json
+sepal_ui/message/en/v_inspector.json
 sepal_ui/message/es/locale.json
 sepal_ui/message/fr/locale.json
+sepal_ui/message/pt-PT/locale.json
+sepal_ui/message/ru-RU/locale.json
+sepal_ui/message/zh-CN/locale.json
 sepal_ui/model/__init__.py
 sepal_ui/model/model.py
+sepal_ui/planetapi/__init__.py
+sepal_ui/planetapi/planet_model.py
+sepal_ui/planetapi/planet_view.py
 sepal_ui/reclassify/__init__.py
 sepal_ui/reclassify/parameters.py
 sepal_ui/reclassify/reclassify_model.py
 sepal_ui/reclassify/reclassify_tile.py
 sepal_ui/reclassify/reclassify_view.py
 sepal_ui/reclassify/table_view.py
 sepal_ui/scripts/__init__.py
```

### Comparing `sepal-ui-2.8.0/setup.py` & `sepal-ui-2.9.4/setup.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup
 from setuptools.command.develop import develop
 from subprocess import check_call
 
-version = "2.8.0"
+version = "2.9.4"
 
 DESCRIPTION = "Wrapper for ipyvuetify widgets to unify the display of voila dashboards in SEPAL platform"
 LONG_DESCRIPTION = open("README.rst").read()
 
 
 class DevelopCmd(develop):
     def run(self):
@@ -29,83 +29,90 @@
     "download_url": f"https://github.com/12rambau/sepal_ui/archive/v_{version}.tar.gz",
     "keywords": ["UI", "Python", "widget", "sepal"],
     "python_requires": ">=3.6.9",
     "install_requires": [
         "haversine",
         "ipyvue>=1.7.0",  # this is the version with the class manager
         "ipyvuetify",  # it will work anyway as the widgets are build on the fly
-        "geemap==0.8.9",
         "earthengine-api",
         "markdown",
         "xarray_leaflet",
         "shapely",
         "geopandas",
         "pandas",
         "deepdiff",
         "colorama",
         "Deprecated",
         "Unidecode",
         "natsort",
         "pipreqs",
         "cryptography",
+        "python-box",
+        "xyzservices",
+        "planet",
+        "pyyaml",
+        "dask",
     ],
     "extras_require": {
         "dev": [
             "pre-commit",
         ],
         "test": [
             "coverage",
             "pytest",
         ],
         "doc": [
-            "jupyter-sphinx @ git+https://github.com/jupyter/jupyter-sphinx.git",
-            "pydata-sphinx-theme @ git+https://github.com/pydata/pydata-sphinx-theme.git",
+            "jupyter-sphinx",
+            "pydata-sphinx-theme==0.9.0",
             "sphinx-notfound-page",
             "Sphinx",
             "sphinxcontrib-spelling",
             "sphinx-copybutton",
             "pandoc",
             "m2r2",
+            "sphinxcontrib-autoprogram",
         ],
     },
     "packages": [
         "sepal_ui",
         "sepal_ui.scripts",
         "sepal_ui.frontend",
         "sepal_ui.sepalwidgets",
         "sepal_ui.aoi",
         "sepal_ui.message",
         "sepal_ui.mapping",
         "sepal_ui.translator",
         "sepal_ui.model",
         "sepal_ui.reclassify",
+        "sepal_ui.planetapi",
     ],
     "package_data": {
         "sepal_ui": [
             "scripts/*.csv",
             "scripts/*.md",
             "scripts/*.json",
             "message/**/*.json",
             "bin/*",
         ]
     },
-    "scripts": [
-        "sepal_ui/bin/module_deploy",
-        "sepal_ui/bin/module_factory",
-        "sepal_ui/bin/module_l10n",
-        "sepal_ui/bin/module_theme",
-        "sepal_ui/bin/module_venv",
-        "sepal_ui/bin/activate_venv",
-    ],
+    "entry_points": {
+        "console_scripts": [
+            "module_deploy = sepal_ui.bin.module_deploy:main",
+            "module_factory = sepal_ui.bin.module_factory:main",
+            "module_l10n = sepal_ui.bin.module_l10n:main",
+            "module_theme = sepal_ui.bin.module_theme:main",
+            "module_venv = sepal_ui.bin.module_venv:main",
+            "activate_venv = sepal_ui.bin.activate_venv:main",
+        ]
+    },
     "classifiers": [
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "Topic :: Software Development :: Build Tools",
         "License :: OSI Approved :: MIT License",
-        "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
     ],
     "cmdclass": {
         "develop": DevelopCmd,
     },
```

