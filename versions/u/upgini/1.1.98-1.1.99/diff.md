# Comparing `tmp/upgini-1.1.98.tar.gz` & `tmp/upgini-1.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/upgini-1.1.98.tar", last modified: Tue Feb 28 16:00:02 2023, max compression
+gzip compressed data, was "dist/upgini-1.1.99.tar", last modified: Fri Mar  3 11:07:10 2023, max compression
```

## Comparing `upgini-1.1.98.tar` & `upgini-1.1.99.tar`

### file list

```diff
@@ -1,63 +1,63 @@
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1514 2021-12-08 19:12:47.000000 upgini-1.1.98/LICENSE
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    46626 2023-02-28 16:00:02.000000 upgini-1.1.98/PKG-INFO
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    39479 2023-02-16 14:54:17.000000 upgini-1.1.98/README.md
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       63 2021-12-08 19:12:47.000000 upgini-1.1.98/pyproject.toml
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       38 2023-02-28 16:00:02.000000 upgini-1.1.98/setup.cfg
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3216 2023-02-28 15:59:54.000000 upgini-1.1.98/setup.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      407 2022-11-25 12:29:54.000000 upgini-1.1.98/src/upgini/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2592 2022-11-25 12:29:54.000000 upgini-1.1.98/src/upgini/ads.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/ads_management/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       50 2023-01-05 17:21:00.000000 upgini-1.1.98/src/upgini/ads_management/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2630 2023-01-06 15:48:24.000000 upgini-1.1.98/src/upgini/ads_management/ads_manager.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/data_source/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-09 12:36:55.000000 upgini-1.1.98/src/upgini/data_source/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     8415 2023-02-21 19:31:19.000000 upgini-1.1.98/src/upgini/data_source/data_source_publisher.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    41712 2023-02-24 15:53:20.000000 upgini-1.1.98/src/upgini/dataset.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      959 2023-01-05 16:59:16.000000 upgini-1.1.98/src/upgini/errors.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)   100378 2023-02-28 15:59:54.000000 upgini-1.1.98/src/upgini/features_enricher.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    35405 2023-02-17 14:13:09.000000 upgini-1.1.98/src/upgini/http.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/mdc/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1152 2022-07-27 18:21:00.000000 upgini-1.1.98/src/upgini/mdc/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1484 2022-07-27 18:21:00.000000 upgini-1.1.98/src/upgini/mdc/context.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     5754 2023-02-17 14:13:09.000000 upgini-1.1.98/src/upgini/metadata.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    13260 2023-01-18 17:48:57.000000 upgini-1.1.98/src/upgini/metrics.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/normalizer/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2021-12-21 13:16:44.000000 upgini-1.1.98/src/upgini/normalizer/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     9930 2022-12-05 12:44:34.000000 upgini-1.1.98/src/upgini/normalizer/phone_normalizer.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/resource_bundle/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     7888 2022-11-25 12:29:54.000000 upgini-1.1.98/src/upgini/resource_bundle/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      622 2022-11-25 12:29:54.000000 upgini-1.1.98/src/upgini/resource_bundle/exceptions.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    19279 2023-02-23 09:03:42.000000 upgini-1.1.98/src/upgini/resource_bundle/strings.properties
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/sampler/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2022-07-08 08:52:11.000000 upgini-1.1.98/src/upgini/sampler/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     6489 2022-07-08 08:52:11.000000 upgini-1.1.98/src/upgini/sampler/base.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4082 2022-07-08 08:52:11.000000 upgini-1.1.98/src/upgini/sampler/random_under_sampler.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    20726 2022-07-08 08:52:11.000000 upgini-1.1.98/src/upgini/sampler/utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    36131 2023-02-22 12:32:49.000000 upgini-1.1.98/src/upgini/search_task.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1149 2023-01-18 17:48:57.000000 upgini-1.1.98/src/upgini/spinner.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini/utils/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2021-12-08 19:13:24.000000 upgini-1.1.98/src/upgini/utils/__init__.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      859 2022-09-04 00:28:46.000000 upgini-1.1.98/src/upgini/utils/base_search_key_detector.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3380 2022-11-25 12:29:54.000000 upgini-1.1.98/src/upgini/utils/blocked_time_series.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     6436 2022-11-23 14:54:48.000000 upgini-1.1.98/src/upgini/utils/country_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2252 2023-01-18 17:48:57.000000 upgini-1.1.98/src/upgini/utils/cv_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4091 2023-01-22 20:14:08.000000 upgini-1.1.98/src/upgini/utils/datetime_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1934 2023-02-07 12:31:28.000000 upgini-1.1.98/src/upgini/utils/display_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3048 2023-02-17 14:13:09.000000 upgini-1.1.98/src/upgini/utils/email_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2190 2023-02-13 21:56:19.000000 upgini-1.1.98/src/upgini/utils/features_validator.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      243 2021-12-08 19:13:24.000000 upgini-1.1.98/src/upgini/utils/format.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      408 2022-11-12 11:53:17.000000 upgini-1.1.98/src/upgini/utils/phone_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      409 2022-11-12 11:53:17.000000 upgini-1.1.98/src/upgini/utils/postal_code_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1370 2023-02-21 19:31:19.000000 upgini-1.1.98/src/upgini/utils/target_utils.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4076 2023-01-05 17:21:00.000000 upgini-1.1.98/src/upgini/utils/track_info.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      228 2022-12-01 07:52:21.000000 upgini-1.1.98/src/upgini/utils/warning_counter.py
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1400 2022-12-09 07:55:43.000000 upgini-1.1.98/src/upgini/version_validator.py
-drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    46626 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/PKG-INFO
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1530 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/SOURCES.txt
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        1 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/dependency_links.txt
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      164 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/requires.txt
--rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        7 2023-02-28 16:00:02.000000 upgini-1.1.98/src/upgini.egg-info/top_level.txt
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1514 2021-12-08 19:12:47.000000 upgini-1.1.99/LICENSE
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    46626 2023-03-03 11:07:10.000000 upgini-1.1.99/PKG-INFO
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    39479 2023-02-16 14:54:17.000000 upgini-1.1.99/README.md
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       63 2021-12-08 19:12:47.000000 upgini-1.1.99/pyproject.toml
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       38 2023-03-03 11:07:10.000000 upgini-1.1.99/setup.cfg
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3216 2023-03-03 11:07:01.000000 upgini-1.1.99/setup.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      407 2022-11-25 12:29:54.000000 upgini-1.1.99/src/upgini/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2592 2022-11-25 12:29:54.000000 upgini-1.1.99/src/upgini/ads.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/ads_management/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)       50 2023-01-05 17:21:00.000000 upgini-1.1.99/src/upgini/ads_management/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2630 2023-01-06 15:48:24.000000 upgini-1.1.99/src/upgini/ads_management/ads_manager.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/data_source/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2023-02-09 12:36:55.000000 upgini-1.1.99/src/upgini/data_source/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     8415 2023-02-21 19:31:19.000000 upgini-1.1.99/src/upgini/data_source/data_source_publisher.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    42110 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/dataset.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      959 2023-01-05 16:59:16.000000 upgini-1.1.99/src/upgini/errors.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)   106004 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/features_enricher.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    35311 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/http.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/mdc/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1152 2022-07-27 18:21:00.000000 upgini-1.1.99/src/upgini/mdc/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1484 2022-07-27 18:21:00.000000 upgini-1.1.99/src/upgini/mdc/context.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     5856 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/metadata.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    13890 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/metrics.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/normalizer/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2021-12-21 13:16:44.000000 upgini-1.1.99/src/upgini/normalizer/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     9930 2022-12-05 12:44:34.000000 upgini-1.1.99/src/upgini/normalizer/phone_normalizer.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/resource_bundle/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     7888 2022-11-25 12:29:54.000000 upgini-1.1.99/src/upgini/resource_bundle/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      622 2022-11-25 12:29:54.000000 upgini-1.1.99/src/upgini/resource_bundle/exceptions.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    19805 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/resource_bundle/strings.properties
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/sampler/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2022-07-08 08:52:11.000000 upgini-1.1.99/src/upgini/sampler/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     6489 2022-07-08 08:52:11.000000 upgini-1.1.99/src/upgini/sampler/base.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4082 2022-07-08 08:52:11.000000 upgini-1.1.99/src/upgini/sampler/random_under_sampler.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    20726 2022-07-08 08:52:11.000000 upgini-1.1.99/src/upgini/sampler/utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    36227 2023-03-03 11:07:01.000000 upgini-1.1.99/src/upgini/search_task.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1149 2023-01-18 17:48:57.000000 upgini-1.1.99/src/upgini/spinner.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini/utils/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        0 2021-12-08 19:13:24.000000 upgini-1.1.99/src/upgini/utils/__init__.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      859 2022-09-04 00:28:46.000000 upgini-1.1.99/src/upgini/utils/base_search_key_detector.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3380 2022-11-25 12:29:54.000000 upgini-1.1.99/src/upgini/utils/blocked_time_series.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     6436 2022-11-23 14:54:48.000000 upgini-1.1.99/src/upgini/utils/country_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2252 2023-01-18 17:48:57.000000 upgini-1.1.99/src/upgini/utils/cv_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4091 2023-01-22 20:14:08.000000 upgini-1.1.99/src/upgini/utils/datetime_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1934 2023-02-07 12:31:28.000000 upgini-1.1.99/src/upgini/utils/display_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     3048 2023-02-17 14:13:09.000000 upgini-1.1.99/src/upgini/utils/email_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     2190 2023-02-13 21:56:19.000000 upgini-1.1.99/src/upgini/utils/features_validator.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      243 2021-12-08 19:13:24.000000 upgini-1.1.99/src/upgini/utils/format.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      408 2022-11-12 11:53:17.000000 upgini-1.1.99/src/upgini/utils/phone_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      409 2022-11-12 11:53:17.000000 upgini-1.1.99/src/upgini/utils/postal_code_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1370 2023-02-21 19:31:19.000000 upgini-1.1.99/src/upgini/utils/target_utils.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     4076 2023-01-05 17:21:00.000000 upgini-1.1.99/src/upgini/utils/track_info.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      228 2022-12-01 07:52:21.000000 upgini-1.1.99/src/upgini/utils/warning_counter.py
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1400 2022-12-09 07:55:43.000000 upgini-1.1.99/src/upgini/version_validator.py
+drwxr-xr-x   0 nikolaytoroptsev   (501) staff       (20)        0 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)    46626 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/PKG-INFO
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)     1530 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/SOURCES.txt
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        1 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/dependency_links.txt
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)      164 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/requires.txt
+-rw-r--r--   0 nikolaytoroptsev   (501) staff       (20)        7 2023-03-03 11:07:10.000000 upgini-1.1.99/src/upgini.egg-info/top_level.txt
```

### Comparing `upgini-1.1.98/LICENSE` & `upgini-1.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/PKG-INFO` & `upgini-1.1.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: upgini
-Version: 1.1.98
+Version: 1.1.99
 Summary: Low-code feature search and enrichment library for machine learning
 Home-page: https://upgini.com/
 Author: Upgini Developers
 Author-email: madewithlove@upgini.com
 License: BSD 3-Clause License
 Project-URL: Bug Reports, https://github.com/upgini/upgini/issues
 Project-URL: Source, https://github.com/upgini/upgini
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: upgini Version: 1.1.98 Summary: Low-code feature
+Metadata-Version: 2.1 Name: upgini Version: 1.1.99 Summary: Low-code feature
 search and enrichment library for machine learning Home-page: https://
 upgini.com/ Author: Upgini Developers Author-email: madewithlove@upgini.com
 License: BSD 3-Clause License Project-URL: Bug Reports, https://github.com/
 upgini/upgini/issues Project-URL: Source, https://github.com/upgini/upgini
 Description:
  ***** Upgini â¢ Free production-ready automated data enrichment library for
                             machine learning *****
```

### Comparing `upgini-1.1.98/README.md` & `upgini-1.1.99/README.md`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/setup.py` & `upgini-1.1.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -31,15 +31,15 @@
         req.add_header("Content-Type", "application/json")
         request.urlopen(req)
     except Exception:
         pass
 
 
 here = Path(__file__).parent.resolve()
-version = "1.1.98"
+version = "1.1.99"
 try:
     send_log(f"Start setup PyLib version {version}")
     setup(
         name="upgini",
         version=version,
         description="Low-code feature search and enrichment library for machine learning",
         long_description=(here / "README.md").read_text(encoding="utf-8"),
```

### Comparing `upgini-1.1.98/src/upgini/ads.py` & `upgini-1.1.99/src/upgini/ads.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/ads_management/ads_manager.py` & `upgini-1.1.99/src/upgini/ads_management/ads_manager.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/data_source/data_source_publisher.py` & `upgini-1.1.99/src/upgini/data_source/data_source_publisher.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/dataset.py` & `upgini-1.1.99/src/upgini/dataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -270,15 +270,17 @@
                 def print_dups_sample():
                     print(dups_sample)
                     self.logger.warning(dups_sample)
 
                 do_without_pandas_limits(print_dups_sample)
                 msg = bundle.get("dataset_diff_target_duplicates").format(share_tgt_dedup, num_dup_rows, dups_sample)
                 self.logger.warning(msg)
-                raise ValidationError(msg)
+                print(msg)
+                self.drop_duplicates(subset=unique_columns, keep=False, inplace=True)
+                self.logger.info(f"Dataset shape after clean invalid target duplicates: {self.shape}")
 
     def __convert_bools(self):
         """Convert bool columns True -> 1, False -> 0"""
         # self.logger.info("Converting bool to int")
         for col in self.columns:
             if is_bool(self[col]):
                 self[col] = self[col].astype("Int64")
@@ -805,23 +807,25 @@
         return_scores: bool,
         extract_features: bool,
         accurate_model: Optional[bool] = None,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
         filter_features: Optional[dict] = None,
         runtime_parameters: Optional[RuntimeParameters] = None,
+        metrics_calculation: Optional[bool] = False
     ) -> SearchCustomization:
         # self.logger.info("Constructing search customization")
         search_customization = SearchCustomization(
             extractFeatures=extract_features,
             accurateModel=accurate_model,
             importanceThreshold=importance_threshold,
             maxFeatures=max_features,
             returnScores=return_scores,
             runtimeParameters=runtime_parameters,
+            metricsCalculation=metrics_calculation,
         )
         if filter_features:
             if [
                 key
                 for key in filter_features
                 if key not in {"min_importance", "max_psi", "max_count", "selected_features"}
             ]:
@@ -894,23 +898,27 @@
         self,
         trace_id: str,
         initial_search_task_id: str,
         return_scores: bool = True,
         extract_features: bool = False,
         runtime_parameters: Optional[RuntimeParameters] = None,
         exclude_features_sources: Optional[List[str]] = None,
+        metrics_calculation: bool = False,
         silent_mode: bool = False,
     ) -> SearchTask:
         if self.etalon_def is None:
             self.validate(validate_target=False, silent_mode=silent_mode)
         file_metrics = FileMetrics()
 
         file_metadata = self.__construct_metadata(exclude_features_sources=exclude_features_sources)
         search_customization = self.__construct_search_customization(
-            return_scores, extract_features, runtime_parameters=runtime_parameters
+            return_scores,
+            extract_features,
+            runtime_parameters=runtime_parameters,
+            metrics_calculation=metrics_calculation,
         )
 
         if self.file_upload_id is not None and get_rest_client(self.endpoint, self.api_key).check_uploaded_file_v2(
             trace_id, self.file_upload_id, file_metadata
         ):
             search_task_response = get_rest_client(self.endpoint, self.api_key).validation_search_without_upload_v2(
                 trace_id, self.file_upload_id, initial_search_task_id, file_metadata, file_metrics, search_customization
```

### Comparing `upgini-1.1.98/src/upgini/errors.py` & `upgini-1.1.99/src/upgini/errors.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/features_enricher.py` & `upgini-1.1.99/src/upgini/features_enricher.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,27 +4,32 @@
 import os
 import pickle
 import subprocess
 import tempfile
 import time
 import uuid
 import zlib
-from typing import Any, Callable, Dict, List, Optional, Tuple, Union
+from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
 
 import numpy as np
 import pandas as pd
 from pandas.api.types import is_string_dtype
 from sklearn.base import TransformerMixin
 from sklearn.exceptions import NotFittedError
 from sklearn.model_selection import BaseCrossValidator
 
 from upgini.data_source.data_source_publisher import CommercialSchema
 from upgini.dataset import Dataset
 from upgini.errors import UpginiConnectionError, ValidationError
-from upgini.http import UPGINI_API_KEY, LoggerFactory, get_rest_client
+from upgini.http import (
+    UPGINI_API_KEY,
+    LoggerFactory,
+    get_rest_client,
+    show_status_error,
+)
 from upgini.mdc import MDC
 from upgini.metadata import (
     COUNTRY,
     DEFAULT_INDEX,
     EVAL_SET_INDEX,
     ORIGINAL_INDEX,
     RENAMED_INDEX,
@@ -122,28 +127,34 @@
         shared_datasets: Optional[List[str]] = None,
         runtime_parameters: Optional[RuntimeParameters] = None,
         date_format: Optional[str] = None,
         random_state: int = 42,
         cv: Optional[CVType] = None,
         detect_missing_search_keys: bool = True,
         logs_enabled: bool = True,
+        **kwargs,
     ):
         self.api_key = api_key or os.environ.get(UPGINI_API_KEY)
         try:
             self.rest_client = get_rest_client(endpoint, self.api_key)
         except UpginiConnectionError as e:
             print(e)
             return
 
         if logs_enabled:
             self.logger = LoggerFactory().get_logger(endpoint, self.api_key)
         else:
             self.logger = logging.getLogger()
             self.logger.setLevel("FATAL")
 
+        if len(kwargs) > 0:
+            msg = f"WARNING: Unsupported arguments: {kwargs}"
+            self.logger.warning(msg)
+            print(msg)
+
         validate_version(self.logger)
 
         self.search_keys = search_keys
         self.country_code = country_code
         self.__validate_search_keys(search_keys, search_id)
         self.model_task_type = model_task_type
         self.endpoint = endpoint
@@ -195,36 +206,37 @@
 
         self.passed_features: List[str] = []
         self.feature_names_ = []
         self.feature_importances_ = []
         self.df_with_original_index: Optional[pd.DataFrame] = None
         self.country_added = False
         self.fit_generated_features: List[str] = []
-        self.fit_dropped_features: List[str] = []
+        self.fit_dropped_features: Set[str] = set()
         self.fit_search_keys = search_keys
         self.warning_counter = WarningCounter()
         self.X: Optional[pd.DataFrame] = None
         self.y: Optional[pd.Series] = None
         self.eval_set: Optional[List[Tuple]] = None
         self.autodetected_search_keys: Dict[str, SearchKey] = {}
         self.imbalanced = False
         self.__cached_sampled_datasets: Optional[Tuple[pd.DataFrame, pd.DataFrame, pd.Series, Dict, Dict]] = None
 
     def fit(
         self,
         X: Union[pd.DataFrame, pd.Series, np.ndarray],
         y: Union[pd.Series, np.ndarray, List],
         eval_set: Optional[List[tuple]] = None,
-        *,
+        *args,
         exclude_features_sources: Optional[List[str]] = None,
         calculate_metrics: Optional[bool] = None,
         estimator: Optional[Any] = None,
         scoring: Union[Callable, str, None] = None,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
+        **kwargs,
     ):
         """Fit to data.
 
         Fits transformer to `X` and `y`.
 
         Parameters
         ----------
@@ -252,14 +264,23 @@
         scoring: string or callable, optional (default=None)
             A string or a scorer callable object / function with signature scorer(estimator, X, y).
             If None, the estimator's score method is used.
         """
         trace_id = str(uuid.uuid4())
         start_time = time.time()
         with MDC(trace_id=trace_id):
+            if len(args) > 0:
+                msg = f"WARNING: Unsupported positional arguments: {args}"
+                self.logger.warning(msg)
+                print(msg)
+            if len(kwargs) > 0:
+                msg = f"WARNING: Unsupported named arguments: {kwargs}"
+                self.logger.warning(msg)
+                print(msg)
+
             self.logger.info("Start fit")
 
             try:
                 self.X = X
                 self.y = y
                 checked_eval_set = []
                 for eval_pair in eval_set or []:
@@ -285,34 +306,39 @@
                     " with validation error" if isinstance(e, ValidationError) else ""
                 )
                 self.logger.exception(error_message)
                 if len(e.args) > 0 and (
                     "File doesn't intersect with any ADS" in str(e.args[0]) or "Empty intersection" in str(e.args[0])
                 ):
                     self.__display_slack_community_link(bundle.get("features_info_zero_important_features"))
+                elif isinstance(e, ValidationError):
+                    self._dump_python_libs()
+                    self._show_error(str(e))
                 else:
+                    show_status_error()
                     self._dump_python_libs()
                     self.__display_slack_community_link()
                     raise e
             finally:
                 self.logger.info(f"Fit elapsed time: {time.time() - start_time}")
 
     def fit_transform(
         self,
         X: Union[pd.DataFrame, pd.Series, np.ndarray],
         y: Union[pd.DataFrame, pd.Series, np.ndarray, List],
         eval_set: Optional[List[tuple]] = None,
-        *,
+        *args,
         exclude_features_sources: Optional[List[str]] = None,
         keep_input: bool = True,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
         calculate_metrics: Optional[bool] = None,
         scoring: Union[Callable, str, None] = None,
         estimator: Optional[Any] = None,
+        **kwargs,
     ) -> pd.DataFrame:
         """Fit to data, then transform it.
 
         Fits transformer to `X` and `y` and returns a transformed version of `X`.
         If keep_input is True, then all input columns are copied to the output dataframe.
 
         Parameters
@@ -350,15 +376,25 @@
         X_new: pandas.DataFrame of shape (n_samples, n_features_new)
             Transformed dataframe, enriched with valuable features.
         """
 
         trace_id = str(uuid.uuid4())
         start_time = time.time()
         with MDC(trace_id=trace_id):
+            if len(args) > 0:
+                msg = f"WARNING: Unsupported positional arguments: {args}"
+                self.logger.warning(msg)
+                print(msg)
+            if len(kwargs) > 0:
+                msg = f"WARNING: Unsupported named arguments: {kwargs}"
+                self.logger.warning(msg)
+                print(msg)
+
             self.logger.info("Start fit_transform")
+
             try:
                 self.X = X
                 self.y = y
                 checked_eval_set = []
                 for eval_pair in eval_set or []:
                     if not is_frames_equal(X, eval_pair[0]):
                         checked_eval_set.append(eval_pair)
@@ -386,15 +422,20 @@
                     " with validation error" if isinstance(e, ValidationError) else ""
                 )
                 self.logger.exception(error_message)
                 if len(e.args) > 0 and (
                     "File doesn't intersect with any ADS" in str(e.args[0]) or "Empty intersection" in str(e.args[0])
                 ):
                     self.__display_slack_community_link(bundle.get("features_info_zero_important_features"))
+                    return None
+                elif isinstance(e, ValidationError):
+                    self._dump_python_libs()
+                    self._show_error(str(e))
                 else:
+                    show_status_error()
                     self._dump_python_libs()
                     self.__display_slack_community_link()
                     raise e
             finally:
                 self.logger.info(f"Fit elapsed time: {time.time() - start_time}")
 
             result = self.transform(
@@ -408,21 +449,23 @@
             )
             self.logger.info("Fit_transform finished successfully")
             return result
 
     def transform(
         self,
         X: pd.DataFrame,
-        *,
+        *args,
         exclude_features_sources: Optional[List[str]] = None,
         keep_input: bool = True,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
         trace_id: Optional[str] = None,
+        metrics_calculation: bool = False,
         silent_mode=False,
+        **kwargs,
     ) -> pd.DataFrame:
         """Transform `X`.
 
         Returns a transformed version of `X`.
         If keep_input is True, then all input columns are copied to the output dataframe.
 
         Parameters
@@ -444,14 +487,23 @@
         X_new: pandas.DataFrame of shape (n_samples, n_features_new)
             Transformed dataframe, enriched with valuable features.
         """
 
         trace_id = trace_id or str(uuid.uuid4())
         start_time = time.time()
         with MDC(trace_id=trace_id):
+            if len(args) > 0:
+                msg = f"WARNING: Unsupported positional arguments: {args}"
+                self.logger.warning(msg)
+                print(msg)
+            if len(kwargs) > 0:
+                msg = f"WARNING: Unsupported named arguments: {kwargs}"
+                self.logger.warning(msg)
+                print(msg)
+
             self.logger.info("Start transform")
             try:
                 if self._has_trial_features(exclude_features_sources) and not self.__is_registered:
                     msg = bundle.get("transform_with_trial_features")
                     self.logger.warn(msg)
                     print(msg)
                     return None
@@ -466,14 +518,15 @@
 
                 result = self.__inner_transform(
                     trace_id,
                     X,
                     exclude_features_sources=exclude_features_sources,
                     importance_threshold=importance_threshold,
                     max_features=max_features,
+                    metrics_calculation=metrics_calculation,
                     silent_mode=silent_mode,
                 )
                 self.logger.info("Transform finished successfully")
             except Exception as e:
                 error_message = "Failed on inner transform" + (
                     " with validation error" if isinstance(e, ValidationError) else ""
                 )
@@ -485,45 +538,64 @@
                     return None
                 elif len(e.args) > 0 and (
                     "You have reached the quota limit of trial data usage" in str(e.args[0])
                     or "Current user hasn't access to trial features" in str(e.args[0])
                 ):
                     self.__display_slack_community_link(bundle.get("trial_quota_limit_riched"))
                     return None
-                else:
+                elif isinstance(e, ValidationError):
                     self._dump_python_libs()
-                    self.__display_slack_community_link()
+                    self._show_error(str(e))
+                    return None
+                else:
+                    if not silent_mode:
+                        show_status_error()
+                        self._dump_python_libs()
+                        self.__display_slack_community_link()
                     raise e
             finally:
                 self.logger.info(f"Transform elapsed time: {time.time() - start_time}")
 
             if self.country_added and COUNTRY in result.columns:
                 result = result.drop(columns=COUNTRY)
 
             if keep_input:
                 return result
             else:
                 return result.drop(columns=[c for c in X.columns if c in result.columns])
 
     def calculate_metrics(
         self,
-        *,
+        X: Union[pd.DataFrame, pd.Series, np.ndarray, None] = None,
+        y: Union[pd.DataFrame, pd.Series, np.ndarray, List, None] = None,
+        eval_set: Optional[List[tuple]] = None,
+        *args,
         scoring: Union[Callable, str, None] = None,
         cv: Union[BaseCrossValidator, CVType, None] = None,
         estimator=None,
         exclude_features_sources: Optional[List[str]] = None,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
         trace_id: Optional[str] = None,
         silent: bool = False,
+        **kwargs,
     ) -> Optional[pd.DataFrame]:
         """Calculate metrics
 
         Parameters
         ----------
+        X: pandas.DataFrame of shape (n_samples, n_features), optional (default=None)
+            Input samples. If not passed then X from fit will be used
+
+        y: array-like of shape (n_samples,), optional (default=None)
+            Target values. If X not passed then y from fit will be used
+
+        eval_set: List[tuple], optional (default=None)
+            List of pairs (X, y) for validation. If X not passed then eval_set from fit will be used
+
         scoring: string or callable, optional (default=None)
             A string or a scorer callable object / function with signature scorer(estimator, X, y).
             If None, the estimator's score method is used.
 
         cv: sklearn.model_selection.BaseCrossValidator, optional (default=None)
             Custom cross validator to calculate metric on train.
 
@@ -541,14 +613,23 @@
         metrics: pandas.DataFrame
             Dataframe with metrics calculated on train and validation datasets.
         """
 
         trace_id = trace_id or str(uuid.uuid4())
         start_time = time.time()
         with MDC(trace_id=trace_id):
+            if len(args) > 0:
+                msg = f"WARNING: Unsupported positional arguments: {args}"
+                self.logger.warning(msg)
+                print(msg)
+            if len(kwargs) > 0:
+                msg = f"WARNING: Unsupported named arguments: {kwargs}"
+                self.logger.warning(msg)
+                print(msg)
+
             try:
                 self.logger.info(
                     f"Start calculating metrics\nscoring: {scoring}\n"
                     f"cv: {cv}\n"
                     f"estimator: {estimator}\n"
                     f"importance_threshold: {importance_threshold}\n"
                     f"max_features: {max_features}"
@@ -558,28 +639,25 @@
                     self._search_task is None
                     or self._search_task.initial_max_hit_rate_v2() is None
                     or self.X is None
                     or self.y is None
                 ):
                     raise ValidationError(bundle.get("metrics_unfitted_enricher"))
 
-                if self._has_trial_features(exclude_features_sources) and not self.__is_registered:
-                    msg = bundle.get("metrics_with_trial_features")
-                    self.logger.warn(msg)
-                    print(msg)
-                    return None
+                if X is not None and y is None:
+                    raise ValidationError("X passed without y")
 
                 if self._has_paid_features(exclude_features_sources):
                     msg = bundle.get("metrics_with_paid_features")
                     self.logger.warn(msg)
                     self.__display_slack_community_link(msg)
                     return None
 
                 prepared_data = self._prepare_data_for_metrics(
-                    trace_id, exclude_features_sources, importance_threshold, max_features
+                    trace_id, X, y, eval_set, exclude_features_sources, importance_threshold, max_features
                 )
                 if prepared_data is None:
                     return None
                 (
                     validated_X,
                     fitting_X,
                     y_sorted,
@@ -601,40 +679,42 @@
 
                     _cv = cv or self.cv
                     if not isinstance(_cv, BaseCrossValidator):
                         date_column = self._get_date_column(search_keys)
                         date_series = validated_X[date_column] if date_column is not None else None
                         _cv = CVConfig(_cv, date_series, self.random_state).get_cv()
 
-                    wrapper = EstimatorWrapper.create(estimator, self.logger, model_task_type, _cv, scoring)
+                    wrapper = EstimatorWrapper.create(
+                        estimator, self.logger, model_task_type, _cv, fitting_enriched_X, scoring
+                    )
                     metric = wrapper.metric_name
                     multiplier = wrapper.multiplier
 
                     # 1 If client features are presented - fit and predict with KFold CatBoost model
                     # on etalon features and calculate baseline metric
                     etalon_metric = None
                     baseline_estimator = None
                     if fitting_X.shape[1] > 0:
                         self.logger.info(
                             f"Calculate baseline {metric} on client features: {fitting_X.columns.to_list()}"
                         )
                         baseline_estimator = EstimatorWrapper.create(
-                            estimator, self.logger, model_task_type, _cv, scoring
+                            estimator, self.logger, model_task_type, _cv, fitting_enriched_X, scoring
                         )
                         etalon_metric = baseline_estimator.cross_val_predict(fitting_X, y_sorted)
 
                     # 2 Fit and predict with KFold Catboost model on enriched tds
                     # and calculate final metric (and uplift)
                     enriched_estimator = None
                     if set(fitting_X.columns) != set(fitting_enriched_X.columns):
                         self.logger.info(
                             f"Calculate enriched {metric} on combined features: {fitting_enriched_X.columns.to_list()}"
                         )
                         enriched_estimator = EstimatorWrapper.create(
-                            estimator, self.logger, model_task_type, _cv, scoring
+                            estimator, self.logger, model_task_type, _cv, fitting_enriched_X, scoring
                         )
                         enriched_metric = enriched_estimator.cross_val_predict(fitting_enriched_X, enriched_y_sorted)
                         if etalon_metric is not None:
                             uplift = (enriched_metric - etalon_metric) * multiplier
                         else:
                             uplift = None
                     else:
@@ -653,16 +733,16 @@
                     if uplift is not None:
                         train_metrics[bundle.get("quality_metrics_uplift_header")] = uplift
                     metrics = [train_metrics]
 
                     # 3 If eval_set is presented - fit final model on train enriched data and score each
                     # validation dataset and calculate final metric (and uplift)
                     # max_initial_eval_set_hit_rate = self._search_task.get_max_initial_eval_set_hit_rate_v2()
-                    if self.eval_set is not None:
-                        for idx, _ in enumerate(self.eval_set):
+                    if len(fitting_eval_set_dict) > 0:
+                        for idx in fitting_eval_set_dict.keys():
                             # eval_hit_rate = max_initial_eval_set_hit_rate[idx + 1]
 
                             (
                                 eval_X_sorted,
                                 eval_y_sorted,
                                 enriched_eval_X_sorted,
                                 enriched_eval_y_sorted,
@@ -738,22 +818,26 @@
 
                     return metrics_df
             except Exception as e:
                 error_message = "Failed to calculate metrics" + (
                     " with validation error" if isinstance(e, ValidationError) else ""
                 )
                 self.logger.exception(error_message)
-                self._dump_python_libs()
                 if len(e.args) > 0 and (
                     "You have reached the quota limit of trial data usage" in str(e.args[0])
                     or "Current user hasn't access to trial features" in str(e.args[0])
                 ):
                     self.__display_slack_community_link(bundle.get("trial_quota_limit_riched"))
+                elif isinstance(e, ValidationError):
+                    self._dump_python_libs()
+                    self._show_error(str(e))
                 else:
                     if not silent:
+                        show_status_error()
+                        self._dump_python_libs()
                         self.__display_slack_community_link()
                     raise e
             finally:
                 self.logger.info(f"Calculating metrics elapsed time: {time.time() - start_time}")
 
     def _has_features_with_commercial_schema(
         self, commercial_schema: str, exclude_features_sources: Optional[List[str]]
@@ -789,34 +873,73 @@
             converter = EmailSearchKeyConverter(email_column, hem_column, search_keys, self.logger)
             extended_X = converter.convert(extended_X)
             generated_features.extend(converter.generated_features)
         generated_features = [f for f in generated_features if f in self.fit_generated_features]
 
         return extended_X, search_keys
 
+    def _is_input_same_as_fit(
+        self,
+        X: Union[pd.DataFrame, pd.Series, np.ndarray, None] = None,
+        y: Union[pd.DataFrame, pd.Series, np.ndarray, List, None] = None,
+        eval_set: Optional[List[tuple]] = None,
+    ) -> Tuple:
+        if X is None:
+            return True, self.X, self.y, self.eval_set
+
+        checked_eval_set = []
+        for eval_pair in eval_set or []:
+            if not is_frames_equal(X, eval_pair[0]):
+                checked_eval_set.append(eval_pair)
+
+        if (
+            X is self.X
+            and y is self.y
+            and (
+                (checked_eval_set == [] and self.eval_set == [])
+                or (
+                    len(checked_eval_set) == len(self.eval_set)
+                    and all(
+                        [
+                            eval_x is self_eval_x and eval_y is self_eval_y
+                            for ((eval_x, eval_y), (self_eval_x, self_eval_y)) in zip(checked_eval_set, self.eval_set)
+                        ]
+                    )
+                )
+            )
+        ):
+            return True, self.X, self.y, self.eval_set
+        else:
+            self.logger.info("Passed X, y and eval_set that differs from passed on fit. Transform will be used")
+            return False, X, y, checked_eval_set
+
     def _prepare_data_for_metrics(
         self,
         trace_id: str,
+        X: Union[pd.DataFrame, pd.Series, np.ndarray, None] = None,
+        y: Union[pd.DataFrame, pd.Series, np.ndarray, List, None] = None,
+        eval_set: Optional[List[tuple]] = None,
         exclude_features_sources: Optional[List[str]] = None,
         importance_threshold: Optional[float] = None,
         max_features: Optional[int] = None,
     ):
-        validated_X = self._validate_X(self.X)
-        validated_y = self._validate_y(validated_X, self.y)
+        is_input_same_as_fit, X, y, eval_set = self._is_input_same_as_fit(X, y, eval_set)
+        validated_X = self._validate_X(X)
+        validated_y = self._validate_y(validated_X, y)
 
-        self.__log_debug_information(self.X, self.y, self.eval_set, exclude_features_sources=exclude_features_sources)
+        self.__log_debug_information(X, y, eval_set, exclude_features_sources=exclude_features_sources)
 
         eval_set_sampled_dict = dict()
 
-        if self.__cached_sampled_datasets is not None:
+        if self.__cached_sampled_datasets is not None and is_input_same_as_fit:
             self.logger.info("Cached enriched dataset found - use it")
             X_sampled, y_sampled, enriched_X, eval_set_sampled_dict, search_keys = self.__cached_sampled_datasets
             if exclude_features_sources:
                 enriched_X = enriched_X.drop(columns=[c for c in exclude_features_sources if c in enriched_X.columns])
-        elif not self.imbalanced and not exclude_features_sources:
+        elif not self.imbalanced and not exclude_features_sources and is_input_same_as_fit:
             self.logger.info("Dataset is not imbalanced, so use enriched_X from fit")
             search_keys = self.fit_search_keys
 
             enriched_Xy, enriched_eval_sets = self.__enrich(
                 self.df_with_original_index,
                 self._search_task.get_all_initial_raw_features(trace_id),
             )
@@ -828,37 +951,37 @@
             X_sampled = enriched_Xy[x_columns].copy()
             y_sampled = enriched_Xy[TARGET].copy()
 
             self.logger.info(f"Shape of enriched_X: {enriched_X.shape}")
             self.logger.info(f"Shape of X after sampling: {X_sampled.shape}")
             self.logger.info(f"Shape of y after sampling: {len(y_sampled)}")
 
-            if self.eval_set is not None:
-                if len(enriched_eval_sets) != len(self.eval_set):
+            if eval_set is not None:
+                if len(enriched_eval_sets) != len(eval_set):
                     raise ValidationError(
-                        bundle.get("metrics_eval_set_count_diff").format(len(enriched_eval_sets), len(self.eval_set))
+                        bundle.get("metrics_eval_set_count_diff").format(len(enriched_eval_sets), len(eval_set))
                     )
 
-                for idx in range(len(self.eval_set)):
+                for idx in range(len(eval_set)):
                     enriched_eval_X = enriched_eval_sets[idx + 1].drop(columns=TARGET)
                     eval_X_sampled = enriched_eval_sets[idx + 1][x_columns].copy()
                     eval_y_sampled = enriched_eval_sets[idx + 1][TARGET].copy()
                     eval_set_sampled_dict[idx] = (eval_X_sampled, enriched_eval_X, eval_y_sampled)
 
             self.__cached_sampled_datasets = (X_sampled, y_sampled, enriched_X, eval_set_sampled_dict, search_keys)
         else:
-            self.logger.info("Dataset is imbalanced or exclude_features_sources was passed. Run transform")
+            self.logger.info("Dataset is imbalanced or exclude_features_sources or X was passed. Run transform")
             print(bundle.get("prepare_data_for_metrics"))
-            if self.eval_set is not None:
+            if eval_set is not None:
                 self.logger.info("Transform with eval_set")
                 # concatenate X and eval_set with eval_set_index
                 df_with_eval_set_index = validated_X.copy()
                 df_with_eval_set_index[TARGET] = validated_y
                 df_with_eval_set_index[EVAL_SET_INDEX] = 0
-                for idx, eval_pair in enumerate(self.eval_set):
+                for idx, eval_pair in enumerate(eval_set):
                     eval_x, eval_y = self._validate_eval_set_pair(validated_X, eval_pair)
                     eval_df_with_index = eval_x.copy()
                     eval_df_with_index[TARGET] = eval_y
                     eval_df_with_index[EVAL_SET_INDEX] = idx + 1
                     df_with_eval_set_index = pd.concat([df_with_eval_set_index, eval_df_with_index])
 
                 # downsample if need to eval_set threshold
@@ -873,15 +996,15 @@
                     df_with_eval_set_index[df_with_eval_set_index[EVAL_SET_INDEX] == 0]
                     .copy()
                     .drop(columns=[EVAL_SET_INDEX, TARGET])
                 )
                 X_sampled, search_keys = self._extend_x(X_sampled)
                 y_sampled = df_with_eval_set_index[df_with_eval_set_index[EVAL_SET_INDEX] == 0].copy()[TARGET]
                 eval_set_sampled_dict = dict()
-                for idx in range(len(self.eval_set)):
+                for idx in range(len(eval_set)):
                     eval_x_sampled = (
                         df_with_eval_set_index[df_with_eval_set_index[EVAL_SET_INDEX] == (idx + 1)]
                         .copy()
                         .drop(columns=[EVAL_SET_INDEX, TARGET])
                     )
                     eval_x_sampled, _ = self._extend_x(eval_x_sampled)
                     eval_y_sampled = df_with_eval_set_index[df_with_eval_set_index[EVAL_SET_INDEX] == (idx + 1)].copy()[
@@ -892,22 +1015,23 @@
                 df_with_eval_set_index.drop(columns=TARGET, inplace=True)
 
                 enriched = self.transform(
                     df_with_eval_set_index,
                     exclude_features_sources=exclude_features_sources,
                     silent_mode=True,
                     trace_id=trace_id,
+                    metrics_calculation=True,
                 )
                 if enriched is None:
                     return None
 
                 enriched_X = enriched[enriched[EVAL_SET_INDEX] == 0].copy()
                 enriched_X.drop(columns=EVAL_SET_INDEX, inplace=True)
 
-                for idx in range(len(self.eval_set)):
+                for idx in range(len(eval_set)):
                     enriched_eval_x = enriched[enriched[EVAL_SET_INDEX] == (idx + 1)].copy()
                     enriched_eval_x.drop(columns=EVAL_SET_INDEX, inplace=True)
                     eval_x_sampled, eval_y_sampled = eval_set_sampled_dict[idx]
                     eval_set_sampled_dict[idx] = (eval_x_sampled, enriched_eval_x, eval_y_sampled)
             else:
                 self.logger.info("Transform without eval_set")
                 df = self.X.copy()
@@ -921,23 +1045,29 @@
                 X_sampled = df.copy().drop(columns=TARGET)
                 X_sampled, search_keys = self._extend_x(X_sampled)
                 y_sampled = df.copy()[TARGET]
 
                 df.drop(columns=TARGET, inplace=True)
 
                 enriched_X = self.transform(
-                    df, exclude_features_sources=exclude_features_sources, silent_mode=True, trace_id=trace_id
+                    df,
+                    exclude_features_sources=exclude_features_sources,
+                    silent_mode=True,
+                    trace_id=trace_id,
+                    metrics_calculation=True,
                 )
                 if enriched_X is None:
                     return None
 
             self.__cached_sampled_datasets = (X_sampled, y_sampled, enriched_X, eval_set_sampled_dict, search_keys)
 
         client_features = [
-            c for c in X_sampled.columns.to_list() if c not in (list(search_keys.keys()) + self.fit_dropped_features)
+            c
+            for c in X_sampled.columns.to_list()
+            if c not in (list(search_keys.keys()) + list(self.fit_dropped_features))
         ]
 
         filtered_enriched_features = self.__filtered_enriched_features(
             importance_threshold,
             max_features,
         )
 
@@ -994,32 +1124,30 @@
         self,
         trace_id,
         X: pd.DataFrame,
         *,
         exclude_features_sources: Optional[List[str]] = None,
         importance_threshold: Optional[float],
         max_features: Optional[int],
+        metrics_calculation: bool = False,
         silent_mode: bool = False,
     ) -> pd.DataFrame:
         with MDC(trace_id=trace_id):
             if self._search_task is None:
                 raise NotFittedError(bundle.get("transform_unfitted_enricher"))
 
-            if self.X is not None and not is_frames_same_schema(X, self.X):
-                try:
-                    self.logger.warning(
-                        f"Schema of fitting X:\n{self.X.columns.to_list()}\n"
-                        f"schema of X passed on transform:\n{X.columns.to_list()}"
-                    )
-                except Exception:
-                    pass
-                raise ValidationError(bundle.get("dataset_transform_diff_fit"))
-
             validated_X = self._validate_X(X, is_transform=True)
 
+            columns_to_drop = [c for c in validated_X.columns if c in self.feature_names_]
+            if len(columns_to_drop) > 0:
+                msg = bundle.get("x_contains_enriching_columns").format(columns_to_drop)
+                self.logger.warning(msg)
+                print(msg)
+                validated_X = validated_X.drop(columns=columns_to_drop)
+
             self.__log_debug_information(X, exclude_features_sources=exclude_features_sources)
 
             search_keys = self.search_keys.copy()
             search_keys = self.__prepare_search_keys(validated_X, search_keys, silent_mode=silent_mode)
 
             df = validated_X.copy()
 
@@ -1088,14 +1216,15 @@
                 dataset.ignore_columns = [email_column]
             validation_task = self._search_task.validation(
                 trace_id,
                 dataset,
                 extract_features=True,
                 runtime_parameters=self.runtime_parameters,
                 exclude_features_sources=exclude_features_sources,
+                metrics_calculation=metrics_calculation,
                 silent_mode=silent_mode,
             )
 
             def enrich():
                 res, _ = self.__enrich(
                     df_with_original_index,
                     validation_task.get_all_validation_raw_features(trace_id),
@@ -1175,14 +1304,16 @@
     ):
         self.warning_counter.reset()
         self.df_with_original_index = None
         self.__cached_sampled_datasets = None
         validated_X = self._validate_X(X)
         validated_y = self._validate_y(validated_X, y)
 
+        self._validate_binary_observations(validated_y)
+
         self.__log_debug_information(X, y, eval_set, exclude_features_sources=exclude_features_sources)
 
         self.fit_search_keys = self.search_keys.copy()
         self.fit_search_keys = self.__prepare_search_keys(validated_X, self.fit_search_keys)
 
         df = pd.concat([validated_X, validated_y], axis=1)
 
@@ -1204,14 +1335,15 @@
                 df = pd.concat([df, eval_df])
                 eval_X_by_id[idx + 1] = eval_X
 
         if DEFAULT_INDEX in df.columns:
             msg = bundle.get("unsupported_index_column")
             self.logger.info(msg)
             print(msg)
+            self.fit_dropped_features.add(DEFAULT_INDEX)
             df.drop(columns=DEFAULT_INDEX, inplace=True)
 
         df = self.__add_country_code(df, self.fit_search_keys)
 
         self.fit_generated_features = []
         date_column = self._get_date_column(self.fit_search_keys)
         if date_column is not None:
@@ -1229,19 +1361,20 @@
 
         non_feature_columns = [self.TARGET_NAME, EVAL_SET_INDEX] + list(self.fit_search_keys.keys())
         if email_converted_to_hem:
             non_feature_columns.append(email_column)
 
         features_columns = [c for c in df.columns if c not in non_feature_columns]
 
-        self.fit_dropped_features = FeaturesValidator(self.logger).validate(df, features_columns, self.warning_counter)
-        df = df.drop(columns=self.fit_dropped_features)
+        features_to_drop = FeaturesValidator(self.logger).validate(df, features_columns, self.warning_counter)
+        self.fit_dropped_features.update(features_to_drop)
+        df = df.drop(columns=features_to_drop)
 
         if email_converted_to_hem:
-            self.fit_dropped_features.append(email_column)
+            self.fit_dropped_features.add(email_column)
 
         self.fit_generated_features = [f for f in self.fit_generated_features if f not in self.fit_dropped_features]
 
         meaning_types = {
             **{col: key.value for col, key in self.fit_search_keys.items()},
             **{str(c): FileColumnMeaningType.FEATURE for c in df.columns if c not in non_feature_columns},
         }
@@ -1300,21 +1433,14 @@
         self.__prepare_feature_importances(trace_id, validated_X.columns.to_list() + self.fit_generated_features)
 
         self.__show_selected_features(self.fit_search_keys)
 
         if not self.warning_counter.has_warnings():
             self.__display_slack_community_link(bundle.get("all_ok_community_invite"))
 
-        if self._has_trial_features(exclude_features_sources) and not self.__is_registered:
-            if calculate_metrics is not None and calculate_metrics:
-                msg = bundle.get("metrics_with_trial_features")
-                self.logger.warn(msg)
-                print(msg)
-            return
-
         if self._has_paid_features(exclude_features_sources):
             if calculate_metrics is not None and calculate_metrics:
                 msg = bundle.get("metrics_with_paid_features")
                 self.logger.warn(msg)
                 self.__display_slack_community_link(msg)
             return None
 
@@ -1330,15 +1456,15 @@
         if "HEM" in keys:
             keys.append("EMAIL")
         if "DATE" in keys:
             keys.append("DATETIME")
         search_keys_with_autodetection = {**self.search_keys, **self.autodetected_search_keys}
         return [c for c, v in search_keys_with_autodetection.items() if v.value.value in keys]
 
-    def _validate_X(self, X, is_transform=False) -> Tuple[pd.DataFrame, Dict]:
+    def _validate_X(self, X, is_transform=False) -> pd.DataFrame:
         if _num_samples(X) == 0:
             raise ValidationError(bundle.get("x_is_empty"))
 
         if isinstance(X, pd.DataFrame):
             if isinstance(X.columns, pd.MultiIndex) or isinstance(X.index, pd.MultiIndex):
                 raise ValidationError(bundle.get("x_multiindex_unsupported"))
             validated_X = X.copy()
@@ -1647,15 +1773,15 @@
                     df[self.TARGET_NAME] = np.where(df[self.TARGET_NAME] == uniq_val, np.nan, df[self.TARGET_NAME])
 
         return df
 
     def __add_country_code(self, df: pd.DataFrame, search_keys: Dict[str, SearchKey]) -> pd.DataFrame:
         self.country_added = False
 
-        if self.country_code and SearchKey.COUNTRY not in search_keys.values():
+        if self.country_code is not None and SearchKey.COUNTRY not in search_keys.values():
             self.logger.info(f"Add COUNTRY column with {self.country_code} value")
             df[COUNTRY] = self.country_code
             search_keys[COUNTRY] = SearchKey.COUNTRY
             self.country_added = True
 
         if SearchKey.COUNTRY in search_keys.values():
             country_column = list(search_keys.keys())[list(search_keys.values()).index(SearchKey.COUNTRY)]
@@ -1837,15 +1963,18 @@
                     raise ValidationError(bundle.get("numeric_search_key_not_found").format(column_id, x.shape[1]))
                 column_name = x.columns[column_id]
                 valid_search_keys[column_name] = meaning_type
             else:
                 raise ValidationError(bundle.get("unsupported_search_key_type").format(type(column_id)))
 
             if meaning_type == SearchKey.COUNTRY and self.country_code is not None:
-                raise ValidationError(bundle.get("search_key_country_and_country_code"))
+                msg = bundle.get("search_key_country_and_country_code")
+                self.logger.warning(msg)
+                print(msg)
+                self.country_code = None
 
             if not self.__is_registered and meaning_type in SearchKey.personal_keys():
                 msg = bundle.get("unregistered_with_personal_keys").format(meaning_type)
                 self.logger.warning(msg)
                 if not silent_mode:
                     self.warning_counter.increment()
                     print(msg)
@@ -1916,23 +2045,24 @@
 
             try:
                 from IPython.display import display
 
                 _ = get_ipython()  # type: ignore
 
                 print(Format.GREEN + Format.BOLD + msg + Format.END)
-                if bundle.get("quality_metrics_uplift_header") in metrics.columns:
-                    metrics = metrics.copy()
-                    try:
-                        baseline_header = [c for c in metrics.columns if "Baseline" in c][0]
-                        metrics[bundle.get("quality_metrics_uplift_prc_header")] = (
-                            metrics[bundle.get("quality_metrics_uplift_header")] / metrics[baseline_header] * 100.0
-                        ).round(2)
-                    except Exception:
-                        pass
+                # TODO for roc_auc calculate GINI and GINI %
+                # if bundle.get("quality_metrics_uplift_header") in metrics.columns:
+                #     metrics = metrics.copy()
+                #     try:
+                #         baseline_header = [c for c in metrics.columns if "Baseline" in c][0]
+                #         metrics[bundle.get("quality_metrics_uplift_prc_header")] = (
+                #             metrics[bundle.get("quality_metrics_uplift_header")] / metrics[baseline_header] * 100.0
+                #         ).round(2)
+                #     except Exception:
+                #         pass
                 display(metrics)
             except (ImportError, NameError):
                 print(msg)
                 print(metrics)
 
     def __show_selected_features(self, search_keys: Dict[str, SearchKey]):
         msg = bundle.get("features_info_header").format(len(self.feature_names_), list(search_keys.keys()))
@@ -2032,14 +2162,21 @@
                     )
                     if not silent_mode:
                         print(bundle.get("phone_detected_not_registered"))
                     self.warning_counter.increment()
 
         return search_keys
 
+    def _validate_binary_observations(self, y):
+        task_type = self.model_task_type or define_task(y, self.logger, silent=True)
+        if task_type == ModelTaskType.BINARY and _num_samples(y) < 1000:
+            msg = bundle.get("binary_small_dataset")
+            self.logger.warning(msg)
+            print(msg)
+
     def _dump_python_libs(self):
         try:
             python_version_result = subprocess.run(["python", "-V"], stdout=subprocess.PIPE)
             python_version = python_version_result.stdout.decode("utf-8")
             result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
             libs = result.stdout.decode("utf-8")
             self.logger.warning(f"User python {python_version} libs versions:\n{libs}")
@@ -2051,25 +2188,33 @@
         link_text = link_text or bundle.get("slack_community_text")
         badge = bundle.get("slack_community_bage")
         alt = bundle.get("slack_community_alt")
         try:
             from IPython.display import HTML, display
 
             _ = get_ipython()  # type: ignore
+            self.logger.warning(link_text)
             print(link_text)
             display(
                 HTML(
                     f"""<a href='{slack_community_link}' target='_blank' rel='noopener noreferrer'>
                     <img alt='{alt}' src='{badge}'></a>
                     """
                 )
             )
         except (ImportError, NameError):
             print(f"{link_text} at {slack_community_link}")
 
+    def _show_error(self, msg):
+        try:
+            _ = get_ipython()  # type: ignore
+            print(Format.RED + Format.BOLD + msg + Format.END)
+        except (ImportError, NameError):
+            print(msg)
+
     def dump_input(
         self,
         trace_id: str,
         X: Union[pd.DataFrame, pd.Series],
         y: Union[pd.DataFrame, pd.Series, None] = None,
         eval_set: Union[Tuple, None] = None,
     ):
```

### Comparing `upgini-1.1.98/src/upgini/http.py` & `upgini-1.1.99/src/upgini/http.py`

 * *Files 0% similar despite different names*

```diff
@@ -271,41 +271,28 @@
                 return self._with_unauth_retry(request)
             else:
                 raise e
         except UnauthorizedError:
             self._syncronized_refresh_access_token()
             return request()
         except HttpError as e:
-            self.show_status_error()
             if e.status_code == 429 and try_number == 0:
                 time.sleep(random.randint(1, 10))
                 return self._with_unauth_retry(request, 1)
             elif e.status_code == 400 and "MD5Exception".lower() in e.message.lower() and try_number < 3:
                 print(bundle.get("upload_file_checksum_fail").format(e.message))
                 return self._with_unauth_retry(request, try_number + 1)
             elif e.status_code == 403:
                 raise ValidationError(bundle.get("access_denied"))
             elif "more than one concurrent search request" in e.message.lower():
                 raise ValidationError(bundle.get("concurrent_request"))
             else:
                 raise e
 
     @staticmethod
-    def show_status_error():
-        try:
-            response = requests.get("https://api.github.com/repos/upgini/upgini/contents/error_status.txt")
-            if response.status_code == requests.codes.ok:
-                js = response.json()
-                content = base64.b64decode(js["content"]).decode("utf-8")
-                if len(content) > 0 and not content.isspace():
-                    print(content)
-        except Exception:
-            pass
-
-    @staticmethod
     def meaning_type_by_name(name: str, metadata: FileMetadata) -> Optional[FileColumnMeaningType]:
         for c in metadata.columns:
             if c.name == name:
                 return c.meaningType
         return None
 
     @staticmethod
@@ -857,7 +844,19 @@
             timestamp=True,
         )
         datadog_handler.setFormatter(json_formatter)
         upgini_logger.addHandler(datadog_handler)
         self._loggers[key] = upgini_logger
 
         return upgini_logger
+
+
+def show_status_error():
+    try:
+        response = requests.get("https://api.github.com/repos/upgini/upgini/contents/error_status.txt")
+        if response.status_code == requests.codes.ok:
+            js = response.json()
+            content = base64.b64decode(js["content"]).decode("utf-8")
+            if len(content) > 0 and not content.isspace():
+                print(content)
+    except Exception:
+        pass
```

### Comparing `upgini-1.1.98/src/upgini/mdc/__init__.py` & `upgini-1.1.99/src/upgini/mdc/__init__.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/mdc/context.py` & `upgini-1.1.99/src/upgini/mdc/context.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/metadata.py` & `upgini-1.1.99/src/upgini/metadata.py`

 * *Files 3% similar despite different names*

```diff
@@ -194,24 +194,26 @@
     featuresFilter: Optional[FeaturesFilter]
     extractFeatures: Optional[bool]
     accurateModel: Optional[bool]
     importanceThreshold: Optional[float]
     maxFeatures: Optional[int]
     returnScores: Optional[bool]
     runtimeParameters: Optional[RuntimeParameters]
+    metricsCalculation: Optional[bool]
 
     def __repr__(self):
         return (
             f"Features filter: {self.featuresFilter}, "
             f"extract features: {self.extractFeatures}, "
             f"accurate model: {self.accurateModel}, "
             f"importance threshold: {self.importanceThreshold}, "
             f"max features: {self.maxFeatures}, "
             f"return scores: {self.returnScores}, "
-            f"runtimeParameters: {self.runtimeParameters}"
+            f"runtimeParameters: {self.runtimeParameters}, "
+            f"metricsCalculation: {self.metricsCalculation}"
         )
 
 
 class CVType(Enum):
     k_fold = "k_fold"
     time_series = "time_series"
     blocked_time_series = "blocked_time_series"
```

### Comparing `upgini-1.1.98/src/upgini/metrics.py` & `upgini-1.1.99/src/upgini/metrics.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,43 +1,47 @@
 import logging
 from typing import Callable, List, Tuple, Union
 
 import numpy as np
 import pandas as pd
 from catboost import CatBoostClassifier, CatBoostRegressor
+from lightgbm import LGBMClassifier
 from numpy import log1p
 from pandas.api.types import is_numeric_dtype
 from sklearn.metrics import SCORERS, check_scoring, get_scorer, make_scorer
 from sklearn.metrics._regression import (
     _check_reg_targets,
     check_consistent_length,
     mean_squared_error,
 )
-from sklearn.model_selection import (
-    BaseCrossValidator,
-    cross_validate,
-)
+from sklearn.model_selection import BaseCrossValidator, cross_validate
 
 from upgini.errors import ValidationError
 from upgini.metadata import ModelTaskType
 from upgini.resource_bundle import bundle
 from upgini.utils.target_utils import correct_string_target
 
+DEFAULT_RANDOM_STATE = 42
+
 CATBOOST_PARAMS = {
     "iterations": 250,
     "learning_rate": 0.05,
     "min_child_samples": 10,
     "max_depth": 5,
     "early_stopping_rounds": 20,
     "one_hot_max_size": 100,
     "verbose": False,
-    "random_state": 42,
+    "random_state": DEFAULT_RANDOM_STATE,
     "allow_writing_files": False,
 }
 
+LIGHTGBM_PARAMS = {
+    "random_state": DEFAULT_RANDOM_STATE,
+}
+
 N_FOLDS = 5
 BLOCKED_TS_TEST_SIZE = 0.2
 
 
 class EstimatorWrapper:
     def __init__(
         self,
@@ -114,27 +118,31 @@
 
     @staticmethod
     def create(
         estimator,
         logger: logging.Logger,
         target_type: ModelTaskType,
         cv: BaseCrossValidator,
+        X: pd.DataFrame,
         scoring: Union[Callable, str, None] = None,
     ) -> "EstimatorWrapper":
         scorer, metric_name, multiplier = _get_scorer(target_type, scoring)
         kwargs = {
             "scorer": scorer,
             "metric_name": metric_name,
             "multiplier": multiplier,
             "cv": cv,
             "target_type": target_type,
         }
         if estimator is None:
             if target_type in [ModelTaskType.MULTICLASS, ModelTaskType.BINARY]:
-                estimator = CatBoostWrapper(CatBoostClassifier(**CATBOOST_PARAMS), **kwargs)
+                if target_type == ModelTaskType.MULTICLASS and _is_too_many_categorical_values(X):
+                    estimator = LightGBMWrapper(LGBMClassifier(**LIGHTGBM_PARAMS), **kwargs)
+                else:
+                    estimator = CatBoostWrapper(CatBoostClassifier(**CATBOOST_PARAMS), **kwargs)
             elif target_type == ModelTaskType.REGRESSION:
                 estimator = CatBoostWrapper(CatBoostRegressor(**CATBOOST_PARAMS), **kwargs)
             else:
                 raise Exception(bundle.get("metrics_unsupported_target_type").format(target_type))
         else:
             kwargs["estimator"] = estimator
             if isinstance(estimator, CatBoostClassifier) or isinstance(estimator, CatBoostRegressor):
@@ -356,7 +364,15 @@
     return mean_squared_error(
         log1p(y_true),
         log1p(y_pred.clip(0)),
         sample_weight=sample_weight,
         multioutput=multioutput,
         squared=squared,
     )
+
+
+def _is_too_many_categorical_values(X: pd.DataFrame) -> bool:
+    many_values_features_count = 0
+    for f in _get_cat_features(X):
+        if X[f].nunique() > 100:
+            many_values_features_count += 1
+    return many_values_features_count >= 2
```

### Comparing `upgini-1.1.98/src/upgini/normalizer/phone_normalizer.py` & `upgini-1.1.99/src/upgini/normalizer/phone_normalizer.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/resource_bundle/__init__.py` & `upgini-1.1.99/src/upgini/resource_bundle/__init__.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/resource_bundle/exceptions.py` & `upgini-1.1.99/src/upgini/resource_bundle/exceptions.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/resource_bundle/strings.properties` & `upgini-1.1.99/src/upgini/resource_bundle/strings.properties`

 * *Files 2% similar despite different names*

```diff
@@ -34,15 +34,15 @@
 failed_search_by_task_id=Failed to retrieve the specified search results
 metrics_unfitted_enricher=Call fit method before calling calculate_metrics
 metrics_empty_enriched_features=Metrics calculation isn't possible after restart. Please call fit method again
 metrics_eval_set_count_diff=Different number of eval_set datasets for fit and calculation metrics: fit: {}, calculation metrics: {}.
 features_unfitted_enricher=Call fit method or pass search_id before calling get_features_info
 transform_unfitted_enricher=Call fit method or pass search_id before calling transform method
 features_wasnt_returned=Search engine crashed on this request. But we already know that and on the way to fix it :-)
-returned_features_same_as_passed=Columns set for transform method should be the same as for fit method, please check input dataframe.\nThese columns are different: {}
+returned_features_same_as_passed=Columns in X contain names same as features to enrich: {}. Drop them and try again
 missing_eval_set_for_enrichment=Eval_set index {} from enriched result not found in original eval_set
 missing_features_meta=Internal error, there's no metadata. But we already know that and on the way to fix it :-)
 search_task_failed_status=Oh! Server did something wrong, please retry with new search request
 no_one_provider_respond=No data sources found for specified set of a search keys. Try with another set of keys or different time period
 all_providers_failed=All search tasks in the request have failed
 all_providers_failed_with_error=All search tasks in the request have failed: {}.
 search_timed_out=Search request timed out
@@ -65,29 +65,30 @@
 search_key_differ_from_fit=With search_id passed as a parameter, search_keys should same as for fit call\nSee docs https://github.com/upgini/upgini#61-reuse-completed-search-for-enrichment-without-fit-run
 empty_search_keys=At least one column with a search key required\nSee docs https://github.com/upgini/upgini#3--choose-one-or-multiple-columns-as-a-search-keys
 date_and_datetime_simultanious=DATE and DATETIME search keys cannot be used simultaneously. Choose one to keep
 email_and_hem_simultanious=EMAIL and HEM search keys cannot be used simultaneously. Choose one to keep
 postal_code_without_country=COUNTRY search key required if POSTAL_CODE is present
 multiple_search_key=Search key {} passed multiple times
 unregistered_only_personal_keys=Api_key from profile.upgini.com required for EMAIL/HEM, PHONE NUMBER or IPv4 search keys\nSee docs https://github.com/upgini/upgini#-open-up-all-capabilities-of-upgini
-search_key_not_found=Key `{}` from search_keys was not found in X dataframe: {}
+search_key_not_found=Column `{}` from search_keys was not found in X dataframe: {}
 numeric_search_key_not_found=Index {} in search_keys is out of bounds for {} columns of X dataframe
 unsupported_search_key_type=Unsupported type of key in search_keys: {}
-search_key_country_and_country_code=SearchKey.COUNTRY and country_code cannot be used simultaneously
+search_key_country_and_country_code=WARNING: SearchKey.COUNTRY and country_code parameter were passed simultaniously. Parameter country_code will be ignored
 empty_search_key=Search key {} is empty. Please fill values or remove this search key
 single_constant_search_key=WARNING: Constant value detected for the {} search key in the X dataframe: {}.\nThat search key will add constant features for different y values.\nPlease add extra search keys with non constant values, like the COUNTRY, POSTAL_CODE, DATE, PHONE NUMBER, EMAIL/HEM or IPv4
 unsupported_index_column=WARNING: Your column with name `index` was dropped because it's reserved name is booked for system needs.
 date_string_without_format=Date column `{}` has string type, but date_format is not specified. Convert column to datetime type or pass date_format
     # X and y validation
 unsupported_x_type=Unsupported type of X: {}. Use pandas.DataFrame, pandas.Series or numpy.ndarray or list
 x_contains_dup_columns=X contains duplicate column names. Please rename or drop duplicates
+x_contains_enriching_columns=WARNING: X contains column names that match the names of features from external data sources. They will be dropped from the dataframe before the enrichment: {}
 unsupported_y_type=Unsupported type of y: {}. Use pandas.DataFrame, pandas.Series, numpy.ndarray or list
 y_is_constant=y is a constant. Relevant feature search requires a non-constant y
 x_and_y_diff_size=X and y has different size: {}, {}.
-x_non_unique_index=Index of X is non unique. Use reset_index
+x_non_unique_index=Index of X is non unique. Use X.reset_index(drop=True)
 x_and_y_diff_index=Indexes of X and y are different. Correct input dataframes
 y_invalid_dimension_dataframe=y should be one column dataframe
 y_invalid_dimension_array=y should be one dimension array
 x_multiindex_unsupported=Multi index in X is not supported
 y_multiindex_unsupported=Multi index in y is not supported
 x_is_empty=X is empty
 y_is_empty=y is empty
@@ -117,15 +118,15 @@
     # Dataset validation
 dataset_too_few_rows=X size should be at least {} rows after validation
 dataset_too_many_rows_registered=X rows limit for transform is {}. Please sample X
 dataset_too_many_rows_unregistered=For unregistered users total rows limit for X + eval_set is {}. Please register on profile.upgini.com
 dataset_empty_column_names=Some column names are empty. Add names please
 dataset_too_long_column_name=Column {} is too long: {} characters. Remove this column or trim length to 50 characters
 dataset_full_duplicates=WARNING: {:.5f}% of the rows are fully duplicated
-dataset_diff_target_duplicates={:.4f}% of rows ({}) in X and eval_set are duplicates with different y values. Please check dataframes
+dataset_diff_target_duplicates=WARNING: {:.4f}% of rows ({}) in X and eval_set are duplicates with different y values. These rows will be deleted as incorrect
 duplicates_sample=Duplicates sample:
 dataset_drop_old_dates=WARNING: We don't have data before '2000-01-01' and removed all earlier records from the search dataset
 dataset_all_dates_old=There is empty train dataset after removing data before '2000-01-01'
 dataset_invalid_target_type=Unexpected dtype of target for binary task type: {}. Expected int or bool
 dataset_invalid_binary_target=Binary task type should contain only 2 target values, but {} found
 dataset_invalid_multiclass_target=Unexpected dtype of target for multiclass task type: {}. Expected int, str or category
 dataset_invalid_regression_target=Unexpected dtype of target for regression task type: {}. Expected float
@@ -138,14 +139,15 @@
 dataset_constant_target=y contains only one distinct value
 dataset_empty_target=y contains only NaN or incorrect values.
 dataset_unsupported_string_target=Unsupported string data type for target in y
 dataset_invalid_column_type=Unsupported data type of column {}: {}
 dataset_invalid_filter=Unknown field in filter_features. Should be {'min_importance', 'max_psi', 'max_count', 'selected_features'}.
 dataset_too_big_file=Too big size of dataframe X for processing. Please reduce number of rows or columns
 dataset_transform_diff_fit=You try to enrich dataset that column names are different from the train dataset column names that you used on the fit stage. Please make the column names the same as in the train dataset and restart.
+binary_small_dataset=The least populated class in Target contains less than 1000 rows.\nSmall numbers of observations may negatively affect the number of selected features and quality of your ML model.\nUpgini recommends you increase the number of observations in the least populated class.
     # Metrics validation
 metrics_msle_negative_target=Mean Squared Logarithmic Error cannot be used when y contain negative values
 metrics_unsupported_target_type=Unsupported type of target in y: {}
 metrics_invalid_scoring={} is not a valid scoring value. Use {} to get valid options
     # Timeseries validation
 timeseries_invalid_split_type=The number of folds must be of Integral type. {} of type {} was passed
 timeseries_invalid_split_count=Cross-validation requires at least one train/test split with n_splits=2 or more, got n_splits={}
```

### Comparing `upgini-1.1.98/src/upgini/sampler/base.py` & `upgini-1.1.99/src/upgini/sampler/base.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/sampler/random_under_sampler.py` & `upgini-1.1.99/src/upgini/sampler/random_under_sampler.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/sampler/utils.py` & `upgini-1.1.99/src/upgini/sampler/utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/search_task.py` & `upgini-1.1.99/src/upgini/search_task.py`

 * *Files 0% similar despite different names*

```diff
@@ -172,23 +172,25 @@
     def validation(
         self,
         trace_id: str,
         validation_dataset: "dataset.Dataset",
         extract_features: bool = False,
         runtime_parameters: Optional[RuntimeParameters] = None,
         exclude_features_sources: Optional[List[str]] = None,
+        metrics_calculation: bool = False,
         silent_mode: bool = False,
     ) -> "SearchTask":
         return validation_dataset.validation(
             trace_id,
             self.search_task_id,
             return_scores=True,
             extract_features=extract_features,
             runtime_parameters=runtime_parameters,
             exclude_features_sources=exclude_features_sources,
+            metrics_calculation=metrics_calculation,
             silent_mode=silent_mode,
         )
 
     def _check_finished_initial_search(self) -> List[ProviderTaskSummary]:
         if self.summary is None or len(self.summary.initial_important_providers) == 0:
             raise RuntimeError(bundle.get("search_not_started"))
         return self.summary.initial_important_providers
```

### Comparing `upgini-1.1.98/src/upgini/spinner.py` & `upgini-1.1.99/src/upgini/spinner.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/base_search_key_detector.py` & `upgini-1.1.99/src/upgini/utils/base_search_key_detector.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/blocked_time_series.py` & `upgini-1.1.99/src/upgini/utils/blocked_time_series.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/country_utils.py` & `upgini-1.1.99/src/upgini/utils/country_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/cv_utils.py` & `upgini-1.1.99/src/upgini/utils/cv_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/datetime_utils.py` & `upgini-1.1.99/src/upgini/utils/datetime_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/display_utils.py` & `upgini-1.1.99/src/upgini/utils/display_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/email_utils.py` & `upgini-1.1.99/src/upgini/utils/email_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/features_validator.py` & `upgini-1.1.99/src/upgini/utils/features_validator.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/target_utils.py` & `upgini-1.1.99/src/upgini/utils/target_utils.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/utils/track_info.py` & `upgini-1.1.99/src/upgini/utils/track_info.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini/version_validator.py` & `upgini-1.1.99/src/upgini/version_validator.py`

 * *Files identical despite different names*

### Comparing `upgini-1.1.98/src/upgini.egg-info/PKG-INFO` & `upgini-1.1.99/src/upgini.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: upgini
-Version: 1.1.98
+Version: 1.1.99
 Summary: Low-code feature search and enrichment library for machine learning
 Home-page: https://upgini.com/
 Author: Upgini Developers
 Author-email: madewithlove@upgini.com
 License: BSD 3-Clause License
 Project-URL: Bug Reports, https://github.com/upgini/upgini/issues
 Project-URL: Source, https://github.com/upgini/upgini
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: upgini Version: 1.1.98 Summary: Low-code feature
+Metadata-Version: 2.1 Name: upgini Version: 1.1.99 Summary: Low-code feature
 search and enrichment library for machine learning Home-page: https://
 upgini.com/ Author: Upgini Developers Author-email: madewithlove@upgini.com
 License: BSD 3-Clause License Project-URL: Bug Reports, https://github.com/
 upgini/upgini/issues Project-URL: Source, https://github.com/upgini/upgini
 Description:
  ***** Upgini â¢ Free production-ready automated data enrichment library for
                             machine learning *****
```

### Comparing `upgini-1.1.98/src/upgini.egg-info/SOURCES.txt` & `upgini-1.1.99/src/upgini.egg-info/SOURCES.txt`

 * *Files identical despite different names*

