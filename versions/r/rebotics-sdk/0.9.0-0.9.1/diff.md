# Comparing `tmp/rebotics_sdk-0.9.0.tar.gz` & `tmp/rebotics_sdk-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/rebotics_sdk-0.9.0.tar", last modified: Tue Mar 23 16:57:51 2021, max compression
+gzip compressed data, was "dist/rebotics_sdk-0.9.1.tar", last modified: Wed Mar 24 09:49:20 2021, max compression
```

## Comparing `rebotics_sdk-0.9.0.tar` & `rebotics_sdk-0.9.1.tar`

### file list

```diff
@@ -1,94 +1,94 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.993173 rebotics_sdk-0.9.0/
--rwxrwxrwx   0 root         (0) root         (0)      162 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/AUTHORS.rst
--rwxrwxrwx   0 root         (0) root         (0)     3593 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/CONTRIBUTING.rst
--rwxrwxrwx   0 root         (0) root         (0)       89 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/HISTORY.rst
--rwxrwxrwx   0 root         (0) root         (0)      262 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/MANIFEST.in
--rwxrwxrwx   0 root         (0) root         (0)     1660 2021-03-23 16:57:50.993173 rebotics_sdk-0.9.0/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)      588 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/README.rst
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:49.953647 rebotics_sdk-0.9.0/docs/
--rwxrwxrwx   0 root         (0) root         (0)      613 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/Makefile
--rwxrwxrwx   0 root         (0) root         (0)       28 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/authors.rst
--rwxrwxrwx   0 root         (0) root         (0)     4888 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/conf.py
--rwxrwxrwx   0 root         (0) root         (0)       33 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/contributing.rst
--rwxrwxrwx   0 root         (0) root         (0)       28 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/history.rst
--rwxrwxrwx   0 root         (0) root         (0)      311 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/index.rst
--rwxrwxrwx   0 root         (0) root         (0)     1186 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/installation.rst
--rwxrwxrwx   0 root         (0) root         (0)      774 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/make.bat
--rwxrwxrwx   0 root         (0) root         (0)       27 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/readme.rst
--rwxrwxrwx   0 root         (0) root         (0)       79 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/docs/usage.rst
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:49.991278 rebotics_sdk-0.9.0/rebotics_sdk/
--rwxrwxrwx   0 root         (0) root         (0)      161 2021-03-23 16:36:32.000000 rebotics_sdk-0.9.0/rebotics_sdk/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.163063 rebotics_sdk-0.9.0/rebotics_sdk/advanced/
--rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/advanced/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     4226 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/advanced/flows.py
--rwxrwxrwx   0 root         (0) root         (0)    12640 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/advanced/packers.py
--rwxrwxrwx   0 root         (0) root         (0)     3328 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/advanced/remote_loaders.py
--rwxrwxrwx   0 root         (0) root         (0)     2380 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/advanced/reverse_planogram.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.322123 rebotics_sdk-0.9.0/rebotics_sdk/cli/
--rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)    24655 2021-03-23 16:36:11.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/admin.py
--rwxrwxrwx   0 root         (0) root         (0)    10190 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/common.py
--rwxrwxrwx   0 root         (0) root         (0)     5818 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     4603 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/renderers.py
--rwxrwxrwx   0 root         (0) root         (0)    33137 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/retailer.py
--rwxrwxrwx   0 root         (0) root         (0)     5080 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/shelf_camera_manager.py
--rwxrwxrwx   0 root         (0) root         (0)     3189 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/tasks.py
--rwxrwxrwx   0 root         (0) root         (0)     5772 2021-03-23 16:36:11.000000 rebotics_sdk-0.9.0/rebotics_sdk/cli/utils.py
--rwxrwxrwx   0 root         (0) root         (0)     1092 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/constants.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.452883 rebotics_sdk-0.9.0/rebotics_sdk/hook/
--rwxrwxrwx   0 root         (0) root         (0)       68 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)      107 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/apps.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.471880 rebotics_sdk-0.9.0/rebotics_sdk/hook/migrations/
--rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/migrations/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)      206 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/serializers.py
--rwxrwxrwx   0 root         (0) root         (0)      214 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/settings.py
--rwxrwxrwx   0 root         (0) root         (0)     2168 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/signals.py
--rwxrwxrwx   0 root         (0) root         (0)       26 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/tests.py
--rwxrwxrwx   0 root         (0) root         (0)      290 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/urls.py
--rwxrwxrwx   0 root         (0) root         (0)      819 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/hook/views.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.617273 rebotics_sdk-0.9.0/rebotics_sdk/notifications/
--rwxrwxrwx   0 root         (0) root         (0)       75 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)      408 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/admin.py
--rwxrwxrwx   0 root         (0) root         (0)      114 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/apps.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.739635 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/
--rwxrwxrwx   0 root         (0) root         (0)     1242 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0001_initial.py
--rwxrwxrwx   0 root         (0) root         (0)     1830 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0002_auto_20190527_0938.py
--rwxrwxrwx   0 root         (0) root         (0)      889 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0003_auto_20190605_0816.py
--rwxrwxrwx   0 root         (0) root         (0)      889 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0003_auto_20190605_0817.py
--rwxrwxrwx   0 root         (0) root         (0)      351 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0004_merge_20190607_1255.py
--rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     2777 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/models.py
--rwxrwxrwx   0 root         (0) root         (0)      360 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/serializers.py
--rwxrwxrwx   0 root         (0) root         (0)     1458 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/tasks.py
--rwxrwxrwx   0 root         (0) root         (0)      196 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/urls.py
--rwxrwxrwx   0 root         (0) root         (0)      484 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/utils.py
--rwxrwxrwx   0 root         (0) root         (0)     1553 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/notifications/views.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.877550 rebotics_sdk-0.9.0/rebotics_sdk/providers/
--rwxrwxrwx   0 root         (0) root         (0)      206 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     5580 2021-03-23 16:36:11.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/admin.py
--rwxrwxrwx   0 root         (0) root         (0)    11228 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/base.py
--rwxrwxrwx   0 root         (0) root         (0)     6549 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/dataset.py
--rwxrwxrwx   0 root         (0) root         (0)     1778 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/facenet.py
--rwxrwxrwx   0 root         (0) root         (0)    17227 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/retailer.py
--rwxrwxrwx   0 root         (0) root         (0)     2962 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/shelf_camera_manager.py
--rwxrwxrwx   0 root         (0) root         (0)     1123 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/rebotics_sdk/providers/utils.py
--rwxrwxrwx   0 root         (0) root         (0)     2952 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.0/rebotics_sdk/utils.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.080319 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/
--rwxrwxrwx   0 root         (0) root         (0)     1660 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)     2438 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/SOURCES.txt
--rwxrwxrwx   0 root         (0) root         (0)        1 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/dependency_links.txt
--rwxrwxrwx   0 root         (0) root         (0)      233 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/entry_points.txt
--rwxrwxrwx   0 root         (0) root         (0)        1 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/not-zip-safe
--rwxrwxrwx   0 root         (0) root         (0)      249 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/requires.txt
--rwxrwxrwx   0 root         (0) root         (0)       13 2021-03-23 16:57:49.000000 rebotics_sdk-0.9.0/rebotics_sdk.egg-info/top_level.txt
--rwxrwxrwx   0 root         (0) root         (0)      537 2021-03-23 16:57:50.998171 rebotics_sdk-0.9.0/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)     2066 2021-03-23 16:36:32.000000 rebotics_sdk-0.9.0/setup.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.903550 rebotics_sdk-0.9.0/tests/
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.934662 rebotics_sdk-0.9.0/tests/db/
-drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-23 16:57:50.974662 rebotics_sdk-0.9.0/tests/db/custom_folder/
--rwxrwxrwx   0 root         (0) root         (0)    13302 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/db/custom_folder/image_1.png
--rwxrwxrwx   0 root         (0) root         (0)    13302 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/db/custom_folder/image_2.png
--rwxrwxrwx   0 root         (0) root         (0)       32 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/db/features.txt
--rwxrwxrwx   0 root         (0) root         (0)       20 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/db/labels.txt
--rwxrwxrwx   0 root         (0) root         (0)     3397 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/test_classification_packing.py
--rwxrwxrwx   0 root         (0) root         (0)     1311 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.0/tests/test_rebotics_sdk.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.890665 rebotics_sdk-0.9.1/
+-rwxrwxrwx   0 root         (0) root         (0)      162 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/AUTHORS.rst
+-rwxrwxrwx   0 root         (0) root         (0)     3593 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/CONTRIBUTING.rst
+-rwxrwxrwx   0 root         (0) root         (0)       89 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/HISTORY.rst
+-rwxrwxrwx   0 root         (0) root         (0)      262 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/MANIFEST.in
+-rwxrwxrwx   0 root         (0) root         (0)     1660 2021-03-24 09:49:22.891666 rebotics_sdk-0.9.1/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)      588 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/README.rst
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:21.621074 rebotics_sdk-0.9.1/docs/
+-rwxrwxrwx   0 root         (0) root         (0)      613 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/Makefile
+-rwxrwxrwx   0 root         (0) root         (0)       28 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/authors.rst
+-rwxrwxrwx   0 root         (0) root         (0)     4888 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/conf.py
+-rwxrwxrwx   0 root         (0) root         (0)       33 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/contributing.rst
+-rwxrwxrwx   0 root         (0) root         (0)       28 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/history.rst
+-rwxrwxrwx   0 root         (0) root         (0)      311 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/index.rst
+-rwxrwxrwx   0 root         (0) root         (0)     1186 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/installation.rst
+-rwxrwxrwx   0 root         (0) root         (0)      774 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/make.bat
+-rwxrwxrwx   0 root         (0) root         (0)       27 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/readme.rst
+-rwxrwxrwx   0 root         (0) root         (0)       79 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/docs/usage.rst
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:21.669191 rebotics_sdk-0.9.1/rebotics_sdk/
+-rwxrwxrwx   0 root         (0) root         (0)      168 2021-03-24 09:33:36.000000 rebotics_sdk-0.9.1/rebotics_sdk/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:21.867855 rebotics_sdk-0.9.1/rebotics_sdk/advanced/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/advanced/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     4226 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/advanced/flows.py
+-rwxrwxrwx   0 root         (0) root         (0)    12640 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/advanced/packers.py
+-rwxrwxrwx   0 root         (0) root         (0)     3328 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/advanced/remote_loaders.py
+-rwxrwxrwx   0 root         (0) root         (0)     2380 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/advanced/reverse_planogram.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.051910 rebotics_sdk-0.9.1/rebotics_sdk/cli/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)    24956 2021-03-24 04:57:21.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/admin.py
+-rwxrwxrwx   0 root         (0) root         (0)    10190 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/common.py
+-rwxrwxrwx   0 root         (0) root         (0)     5818 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/dataset.py
+-rwxrwxrwx   0 root         (0) root         (0)     4603 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/renderers.py
+-rwxrwxrwx   0 root         (0) root         (0)    33137 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/retailer.py
+-rwxrwxrwx   0 root         (0) root         (0)     5080 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/shelf_camera_manager.py
+-rwxrwxrwx   0 root         (0) root         (0)     3189 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/tasks.py
+-rwxrwxrwx   0 root         (0) root         (0)     5772 2021-03-24 04:57:21.000000 rebotics_sdk-0.9.1/rebotics_sdk/cli/utils.py
+-rwxrwxrwx   0 root         (0) root         (0)     1092 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/constants.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.216149 rebotics_sdk-0.9.1/rebotics_sdk/hook/
+-rwxrwxrwx   0 root         (0) root         (0)       68 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)      107 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/apps.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.240149 rebotics_sdk-0.9.1/rebotics_sdk/hook/migrations/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/migrations/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)      206 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/serializers.py
+-rwxrwxrwx   0 root         (0) root         (0)      214 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/settings.py
+-rwxrwxrwx   0 root         (0) root         (0)     2168 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/signals.py
+-rwxrwxrwx   0 root         (0) root         (0)       26 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/tests.py
+-rwxrwxrwx   0 root         (0) root         (0)      290 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/urls.py
+-rwxrwxrwx   0 root         (0) root         (0)      819 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/hook/views.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.423149 rebotics_sdk-0.9.1/rebotics_sdk/notifications/
+-rwxrwxrwx   0 root         (0) root         (0)       75 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)      408 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/admin.py
+-rwxrwxrwx   0 root         (0) root         (0)      114 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/apps.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.573838 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/
+-rwxrwxrwx   0 root         (0) root         (0)     1242 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0001_initial.py
+-rwxrwxrwx   0 root         (0) root         (0)     1830 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0002_auto_20190527_0938.py
+-rwxrwxrwx   0 root         (0) root         (0)      889 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0003_auto_20190605_0816.py
+-rwxrwxrwx   0 root         (0) root         (0)      889 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0003_auto_20190605_0817.py
+-rwxrwxrwx   0 root         (0) root         (0)      351 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0004_merge_20190607_1255.py
+-rwxrwxrwx   0 root         (0) root         (0)        0 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     2777 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/models.py
+-rwxrwxrwx   0 root         (0) root         (0)      360 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/serializers.py
+-rwxrwxrwx   0 root         (0) root         (0)     1458 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/tasks.py
+-rwxrwxrwx   0 root         (0) root         (0)      196 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/urls.py
+-rwxrwxrwx   0 root         (0) root         (0)      484 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/utils.py
+-rwxrwxrwx   0 root         (0) root         (0)     1553 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/notifications/views.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.749584 rebotics_sdk-0.9.1/rebotics_sdk/providers/
+-rwxrwxrwx   0 root         (0) root         (0)      206 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     5580 2021-03-24 04:57:21.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/admin.py
+-rwxrwxrwx   0 root         (0) root         (0)    11228 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/base.py
+-rwxrwxrwx   0 root         (0) root         (0)     6549 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/dataset.py
+-rwxrwxrwx   0 root         (0) root         (0)     1778 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/facenet.py
+-rwxrwxrwx   0 root         (0) root         (0)    17227 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/retailer.py
+-rwxrwxrwx   0 root         (0) root         (0)     2962 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/shelf_camera_manager.py
+-rwxrwxrwx   0 root         (0) root         (0)     1123 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/rebotics_sdk/providers/utils.py
+-rwxrwxrwx   0 root         (0) root         (0)     2952 2021-03-15 12:44:23.000000 rebotics_sdk-0.9.1/rebotics_sdk/utils.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:21.768857 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/
+-rwxrwxrwx   0 root         (0) root         (0)     1660 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)     2438 2021-03-24 09:49:21.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/SOURCES.txt
+-rwxrwxrwx   0 root         (0) root         (0)        1 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/dependency_links.txt
+-rwxrwxrwx   0 root         (0) root         (0)      233 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/entry_points.txt
+-rwxrwxrwx   0 root         (0) root         (0)        1 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/not-zip-safe
+-rwxrwxrwx   0 root         (0) root         (0)      249 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/requires.txt
+-rwxrwxrwx   0 root         (0) root         (0)       13 2021-03-24 09:49:20.000000 rebotics_sdk-0.9.1/rebotics_sdk.egg-info/top_level.txt
+-rwxrwxrwx   0 root         (0) root         (0)      537 2021-03-24 09:49:22.900667 rebotics_sdk-0.9.1/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)     2140 2021-03-24 09:33:36.000000 rebotics_sdk-0.9.1/setup.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.784731 rebotics_sdk-0.9.1/tests/
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.819878 rebotics_sdk-0.9.1/tests/db/
+drwxrwxrwx   0 root         (0) root         (0)        0 2021-03-24 09:49:22.870097 rebotics_sdk-0.9.1/tests/db/custom_folder/
+-rwxrwxrwx   0 root         (0) root         (0)    13302 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/db/custom_folder/image_1.png
+-rwxrwxrwx   0 root         (0) root         (0)    13302 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/db/custom_folder/image_2.png
+-rwxrwxrwx   0 root         (0) root         (0)       32 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/db/features.txt
+-rwxrwxrwx   0 root         (0) root         (0)       20 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/db/labels.txt
+-rwxrwxrwx   0 root         (0) root         (0)     3397 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/test_classification_packing.py
+-rwxrwxrwx   0 root         (0) root         (0)     1311 2020-11-23 08:21:01.000000 rebotics_sdk-0.9.1/tests/test_rebotics_sdk.py
```

### Comparing `rebotics_sdk-0.9.0/CONTRIBUTING.rst` & `rebotics_sdk-0.9.1/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/PKG-INFO` & `rebotics_sdk-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rebotics_sdk
-Version: 0.9.0
+Version: 0.9.1
 Summary: Rebotics SDK for communicating with Rebotic Services, API CLI client.
 Home-page: http://retechlabs.com/rebotics/
 Author: Malik Sulaimanov
 Author-email: malik@retechlabs.com
 License: UNKNOWN
 Description: ============
         rebotics_sdk
```

### Comparing `rebotics_sdk-0.9.0/README.rst` & `rebotics_sdk-0.9.1/README.rst`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/docs/Makefile` & `rebotics_sdk-0.9.1/docs/Makefile`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/docs/conf.py` & `rebotics_sdk-0.9.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/docs/installation.rst` & `rebotics_sdk-0.9.1/docs/installation.rst`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/docs/make.bat` & `rebotics_sdk-0.9.1/docs/make.bat`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/advanced/flows.py` & `rebotics_sdk-0.9.1/rebotics_sdk/advanced/flows.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/advanced/packers.py` & `rebotics_sdk-0.9.1/rebotics_sdk/advanced/packers.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/advanced/remote_loaders.py` & `rebotics_sdk-0.9.1/rebotics_sdk/advanced/remote_loaders.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/advanced/reverse_planogram.py` & `rebotics_sdk-0.9.1/rebotics_sdk/advanced/reverse_planogram.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/admin.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/admin.py`

 * *Files 1% similar despite different names*

```diff
@@ -505,15 +505,15 @@
     Make sure that extension is a valid JSON and extension in the admin is set like that
     """
     output = pathlib.Path(output).absolute()
     output.mkdir(parents=True, exist_ok=True)
 
     filepath = output / "definition.json"
 
-    if argument.isidigit():
+    if argument.isdigit():
         backup_id = int(argument)
         rcdb_data = ctx.provider.rcdb.get(backup_id)
         if rcdb_data['extension'] != RCDB.JSON:
             click.echo("extension is not supported")  # but we will try anyway
             # raise click.ClickException("Extension is not supported")
 
         # download to a local folder
@@ -567,72 +567,80 @@
     argument - id of stitching debug data from admin, or json file
     """
     output = pathlib.Path(output).absolute()
     output.mkdir(parents=True, exist_ok=True)
 
     filepath = output / "definition.json"
 
-    if argument.isidigit():
+    if argument.isdigit():
         backup_id = int(argument)
-        callback_data = ctx.provider.rcdb.get_core_callback_data(backup_id)
+        callback_data = ctx.provider.get_core_callback_data(backup_id)
         definition = callback_data['data']
 
         ctx.verbose_log("Saving definition locally")
         with open(filepath, 'w') as fp:
-            json.dump(fp, definition)
+            json.dump(definition, fp)
 
     elif uri_validator(argument):
         # argument is a url
         raise click.ClickException("not supported")
     else:
         ctx.verbose_log("Assuming we have a filepath")
         filepath = argument
         try:
             with open(filepath, 'rb') as fp:
                 definition = json.load(fp)
         except:
             raise click.ClickException(f"File is not supported. Please check it at {filepath}")
 
+    if 'data' in definition:
+        definition = definition['data']
+
     if ctx.verbose:
         ctx.format_result(definition['context'])
 
     files_to_load = []  # pair of remote_url to local path
 
     for call_count, call_data in enumerate(definition['calls']):
         call_folder = output / f"call_{call_count}"
         call_folder.mkdir(parents=True, exist_ok=True)
 
         input_data = call_data['input']
 
         stitching_input = {
             **input_data,
             'frame_paths': [],
+            'output_file': str(call_folder),
+            'result_image': str(call_folder / "local_stitching.jpeg"),
         }
 
         del stitching_input['frame_urls']
         del stitching_input['annotated_frames']
 
         # add stitching result image
-        files_to_load.append([
-            call_data['image_url'], call_folder / "server_stitched_image.jpeg"
-        ])
+        try:
+            files_to_load.append([
+                call_data['image_url'], call_folder / "server_stitched_image.jpeg"
+            ])
+        except:
+            ctx.verbose_log("No stitching image is available")
 
         mask_od_path = call_folder / "mask_od.json"
-        stitching_input['mask_od'] = mask_od_path
+        stitching_input['mask_od'] = str(mask_od_path)
         files_to_load.append([
             input_data['mask_od_url'], mask_od_path
         ])
 
         # register input files
         frames_folder = call_folder / "frames"
         frames_folder.mkdir(parents=True, exist_ok=True)
 
         for frame_url in input_data['frame_urls']:
             frame_path = frames_folder / get_filename_from_url(frame_url)
-            stitching_input['frame_paths'].append(frame_path)
+            stitching_input['frame_paths'].append(str(frame_path))
             files_to_load.append([
                 frame_url, frame_path
             ])
 
         frames_folder = call_folder / "annotated_frames"
         frames_folder.mkdir(parents=True, exist_ok=True)
```

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/common.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/common.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/dataset.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/dataset.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/renderers.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/renderers.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/retailer.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/retailer.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/shelf_camera_manager.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/shelf_camera_manager.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/tasks.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/tasks.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/cli/utils.py` & `rebotics_sdk-0.9.1/rebotics_sdk/cli/utils.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/constants.py` & `rebotics_sdk-0.9.1/rebotics_sdk/constants.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/hook/signals.py` & `rebotics_sdk-0.9.1/rebotics_sdk/hook/signals.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/hook/views.py` & `rebotics_sdk-0.9.1/rebotics_sdk/hook/views.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0001_initial.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0002_auto_20190527_0938.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0002_auto_20190527_0938.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0003_auto_20190605_0816.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0003_auto_20190605_0816.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/migrations/0003_auto_20190605_0817.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/migrations/0003_auto_20190605_0817.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/models.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/models.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/tasks.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/tasks.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/notifications/views.py` & `rebotics_sdk-0.9.1/rebotics_sdk/notifications/views.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/admin.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/admin.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/base.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/base.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/dataset.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/dataset.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/facenet.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/facenet.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/retailer.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/retailer.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/shelf_camera_manager.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/shelf_camera_manager.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/providers/utils.py` & `rebotics_sdk-0.9.1/rebotics_sdk/providers/utils.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk/utils.py` & `rebotics_sdk-0.9.1/rebotics_sdk/utils.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk.egg-info/PKG-INFO` & `rebotics_sdk-0.9.1/rebotics_sdk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rebotics-sdk
-Version: 0.9.0
+Version: 0.9.1
 Summary: Rebotics SDK for communicating with Rebotic Services, API CLI client.
 Home-page: http://retechlabs.com/rebotics/
 Author: Malik Sulaimanov
 Author-email: malik@retechlabs.com
 License: UNKNOWN
 Description: ============
         rebotics_sdk
```

### Comparing `rebotics_sdk-0.9.0/rebotics_sdk.egg-info/SOURCES.txt` & `rebotics_sdk-0.9.1/rebotics_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/setup.cfg` & `rebotics_sdk-0.9.1/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [bumpversion]
-current_version = 0.9.0
+current_version = 0.9.1
 commit = False
 tag = False
 
 [bumpversion:file:setup.py]
 search = version='{current_version}'
 replace = version='{new_version}'
```

### Comparing `rebotics_sdk-0.9.0/setup.py` & `rebotics_sdk-0.9.1/setup.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,74 +1,74 @@
-#!/usr/bin/env python
-# -*- coding: utf-8 -*-
-
-"""The setup script."""
-
-from setuptools import setup, find_packages
-
-with open('README.rst') as readme_file:
-    readme = readme_file.read()
-
-with open('HISTORY.rst') as history_file:
-    history = history_file.read()
-
-test_requirements = ['pytest', ]
-
-setup(
-    author="Malik Sulaimanov",
-    author_email='malik@retechlabs.com',
-    classifiers=[
-        'Development Status :: 2 - Pre-Alpha',
-        'Intended Audience :: Developers',
-        'Natural Language :: English',
-        'Programming Language :: Python :: 3.6',
-        'Programming Language :: Python :: 3.7',
-        'Programming Language :: Python :: 3.8',
-        'Programming Language :: Python :: 3.9',
-    ],
-    description="Rebotics SDK for communicating with Rebotic Services, API CLI client.",
-    entry_points={
-        'console_scripts': [
-            'admin=rebotics_sdk.cli.admin:api',
-            'dataset=rebotics_sdk.cli.dataset:api',
-            'retailer=rebotics_sdk.cli.retailer:api',
-            'camera_manager=rebotics_sdk.cli.shelf_camera_manager:api',
-            'rebotics=rebotics_sdk.cli.common:main',
-        ],
-    },
-    long_description=readme + '\n\n' + history,
-    include_package_data=True,
-    keywords='rebotics_sdk',
-    name='rebotics_sdk',
-    packages=find_packages(),
-    test_suite='tests',
-    url='http://retechlabs.com/rebotics/',
-    version='0.9.0',
-    zip_safe=False,
-    install_requires=[
-        'requests>=2.21.0',
-        'requests[socks]',
-        'requests-toolbelt>=0.9.1',
-        'six>=1.12.0',
-        'more-itertools',
-        'tqdm',
-    ],
-    tests_require=test_requirements,
-    extras_require={
-        'hook': [
-            'django',
-            'djangorestframework'
-        ],
-        'shell': [
-            'ipython>=7.5.0,<8',
-            'pandas',
-            'pytz',
-            'ptable',
-            'python-dateutil',
-            'humanize',
-            'PySocks!=1.5.7,>=1.5.6',
-            'xlrd>=1.2.0',
-            'click>=7.0',
-            'pyyaml',
-        ]
-    }
-)
+#!/usr/bin/env python
+# -*- coding: utf-8 -*-
+
+"""The setup script."""
+
+from setuptools import setup, find_packages
+
+with open('README.rst') as readme_file:
+    readme = readme_file.read()
+
+with open('HISTORY.rst') as history_file:
+    history = history_file.read()
+
+test_requirements = ['pytest', ]
+
+setup(
+    author="Malik Sulaimanov",
+    author_email='malik@retechlabs.com',
+    classifiers=[
+        'Development Status :: 2 - Pre-Alpha',
+        'Intended Audience :: Developers',
+        'Natural Language :: English',
+        'Programming Language :: Python :: 3.6',
+        'Programming Language :: Python :: 3.7',
+        'Programming Language :: Python :: 3.8',
+        'Programming Language :: Python :: 3.9',
+    ],
+    description="Rebotics SDK for communicating with Rebotic Services, API CLI client.",
+    entry_points={
+        'console_scripts': [
+            'admin=rebotics_sdk.cli.admin:api',
+            'dataset=rebotics_sdk.cli.dataset:api',
+            'retailer=rebotics_sdk.cli.retailer:api',
+            'camera_manager=rebotics_sdk.cli.shelf_camera_manager:api',
+            'rebotics=rebotics_sdk.cli.common:main',
+        ],
+    },
+    long_description=readme + '\n\n' + history,
+    include_package_data=True,
+    keywords='rebotics_sdk',
+    name='rebotics_sdk',
+    packages=find_packages(),
+    test_suite='tests',
+    url='http://retechlabs.com/rebotics/',
+    version='0.9.1',
+    zip_safe=False,
+    install_requires=[
+        'requests>=2.21.0',
+        'requests[socks]',
+        'requests-toolbelt>=0.9.1',
+        'six>=1.12.0',
+        'more-itertools',
+        'tqdm',
+    ],
+    tests_require=test_requirements,
+    extras_require={
+        'hook': [
+            'django',
+            'djangorestframework'
+        ],
+        'shell': [
+            'ipython>=7.5.0,<8',
+            'pandas',
+            'pytz',
+            'ptable',
+            'python-dateutil',
+            'humanize',
+            'PySocks!=1.5.7,>=1.5.6',
+            'xlrd>=1.2.0',
+            'click>=7.0',
+            'pyyaml',
+        ]
+    }
+)
```

### Comparing `rebotics_sdk-0.9.0/tests/db/custom_folder/image_1.png` & `rebotics_sdk-0.9.1/tests/db/custom_folder/image_1.png`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/tests/db/custom_folder/image_2.png` & `rebotics_sdk-0.9.1/tests/db/custom_folder/image_2.png`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/tests/test_classification_packing.py` & `rebotics_sdk-0.9.1/tests/test_classification_packing.py`

 * *Files identical despite different names*

### Comparing `rebotics_sdk-0.9.0/tests/test_rebotics_sdk.py` & `rebotics_sdk-0.9.1/tests/test_rebotics_sdk.py`

 * *Files identical despite different names*

