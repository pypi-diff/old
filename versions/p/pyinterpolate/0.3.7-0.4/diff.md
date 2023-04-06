# Comparing `tmp/pyinterpolate-0.3.7.tar.gz` & `tmp/pyinterpolate-0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyinterpolate-0.3.7.tar", last modified: Thu Feb  9 08:59:27 2023, max compression
+gzip compressed data, was "pyinterpolate-0.4.tar", last modified: Thu Apr  6 10:00:28 2023, max compression
```

## Comparing `pyinterpolate-0.3.7.tar` & `pyinterpolate-0.4.tar`

### file list

```diff
@@ -1,98 +1,109 @@
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.570385 pyinterpolate-0.3.7/
--rw-r--r--   0 szymonos   (504) staff       (20)       42 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/MANIFEST.in
--rw-r--r--   0 szymonos   (504) staff       (20)     9464 2023-02-09 08:59:27.570799 pyinterpolate-0.3.7/PKG-INFO
--rwxr-xr-x   0 szymonos   (504) staff       (20)     8447 2023-02-09 08:37:25.000000 pyinterpolate-0.3.7/README.md
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.525539 pyinterpolate-0.3.7/pyinterpolate/
--rwxr-xr-x   0 szymonos   (504) staff       (20)     1193 2023-02-09 08:37:25.000000 pyinterpolate-0.3.7/pyinterpolate/__init__.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.529452 pyinterpolate-0.3.7/pyinterpolate/distance/
--rw-r--r--   0 szymonos   (504) staff       (20)       80 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/distance/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)    11000 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/distance/distance.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.530463 pyinterpolate-0.3.7/pyinterpolate/idw/
--rw-r--r--   0 szymonos   (504) staff       (20)       60 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/idw/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     3507 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/idw/idw.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.531322 pyinterpolate-0.3.7/pyinterpolate/io/
--rwxr-xr-x   0 szymonos   (504) staff       (20)       70 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/io/__init__.py
--rwxr-xr-x   0 szymonos   (504) staff       (20)     5946 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/io/read_data.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.532220 pyinterpolate-0.3.7/pyinterpolate/kriging/
--rw-r--r--   0 szymonos   (504) staff       (20)      503 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/__init__.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.532585 pyinterpolate-0.3.7/pyinterpolate/kriging/models/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/__init__.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.534503 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/
--rw-r--r--   0 szymonos   (504) staff       (20)      187 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     7712 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/area_to_area_poisson_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)     9806 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/area_to_point_poisson_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)     7405 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/centroid_based_poisson_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)    10644 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/weight.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.535785 pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     6845 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/ordinary_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)     3539 2023-02-06 21:48:30.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/simple_kriging.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.536808 pyinterpolate-0.3.7/pyinterpolate/kriging/models/structures/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2023-02-06 21:48:30.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/structures/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)      687 2023-02-06 21:48:30.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/models/structures/point_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)     6194 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/point_kriging.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.538422 pyinterpolate-0.3.7/pyinterpolate/kriging/utils/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/utils/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     1078 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/utils/kwarnings.py
--rw-r--r--   0 szymonos   (504) staff       (20)     4858 2022-10-31 14:00:40.000000 pyinterpolate-0.3.7/pyinterpolate/kriging/utils/process.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.541268 pyinterpolate-0.3.7/pyinterpolate/pipelines/
--rw-r--r--   0 szymonos   (504) staff       (20)      318 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/pipelines/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)    13437 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/pipelines/block_filtering.py
--rw-r--r--   0 szymonos   (504) staff       (20)     5227 2022-10-21 13:00:35.000000 pyinterpolate-0.3.7/pyinterpolate/pipelines/deconvolution.py
--rw-r--r--   0 szymonos   (504) staff       (20)    12890 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/pipelines/multi_kriging.py
--rw-r--r--   0 szymonos   (504) staff       (20)     2814 2023-01-20 16:18:01.000000 pyinterpolate-0.3.7/pyinterpolate/pipelines/samples.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.543267 pyinterpolate-0.3.7/pyinterpolate/processing/
--rw-r--r--   0 szymonos   (504) staff       (20)       79 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/processing/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     2543 2023-01-21 18:01:23.000000 pyinterpolate-0.3.7/pyinterpolate/processing/checks.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.544811 pyinterpolate-0.3.7/pyinterpolate/processing/preprocessing/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/processing/preprocessing/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)    17173 2023-01-20 23:20:28.000000 pyinterpolate-0.3.7/pyinterpolate/processing/preprocessing/blocks.py
--rw-r--r--   0 szymonos   (504) staff       (20)    36344 2023-02-04 22:34:54.000000 pyinterpolate-0.3.7/pyinterpolate/processing/select_values.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.546813 pyinterpolate-0.3.7/pyinterpolate/processing/transform/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/processing/transform/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     4852 2022-12-25 15:12:44.000000 pyinterpolate-0.3.7/pyinterpolate/processing/transform/statistics.py
--rw-r--r--   0 szymonos   (504) staff       (20)    10485 2023-01-21 16:25:06.000000 pyinterpolate-0.3.7/pyinterpolate/processing/transform/transform.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.548644 pyinterpolate-0.3.7/pyinterpolate/processing/utils/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/processing/utils/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     1802 2022-10-22 08:42:15.000000 pyinterpolate-0.3.7/pyinterpolate/processing/utils/exceptions.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.549459 pyinterpolate-0.3.7/pyinterpolate/variogram/
--rw-r--r--   0 szymonos   (504) staff       (20)      535 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/__init__.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.554923 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/
--rw-r--r--   0 szymonos   (504) staff       (20)     1857 2023-01-28 21:37:06.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)    23617 2023-01-31 22:52:39.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/cloud.py
--rw-r--r--   0 szymonos   (504) staff       (20)    10720 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/covariance.py
--rw-r--r--   0 szymonos   (504) staff       (20)    25377 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/experimental_variogram.py
--rw-r--r--   0 szymonos   (504) staff       (20)    23469 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/semivariance.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.557219 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)    24569 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/aggregated.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.561370 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     1489 2022-10-07 19:36:48.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/avg_block_to_block_semivariances.py
--rw-r--r--   0 szymonos   (504) staff       (20)     4047 2023-01-28 15:31:11.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/avg_inblock_semivariances.py
--rw-r--r--   0 szymonos   (504) staff       (20)     5343 2022-10-07 19:32:56.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/block_to_block_semivariance.py
--rw-r--r--   0 szymonos   (504) staff       (20)     8847 2023-01-28 20:46:13.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/inblock_semivariance.py
--rw-r--r--   0 szymonos   (504) staff       (20)    33508 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/deconvolution.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.563743 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/
--rw-r--r--   0 szymonos   (504) staff       (20)     5340 2023-01-28 21:37:06.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/__init__.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.565278 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/models/
--rw-r--r--   0 szymonos   (504) staff       (20)       31 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/models/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     8319 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/models/variogram_models.py
--rw-r--r--   0 szymonos   (504) staff       (20)    34319 2022-11-02 16:31:10.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/semivariogram.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.567988 pyinterpolate-0.3.7/pyinterpolate/variogram/utils/
--rw-r--r--   0 szymonos   (504) staff       (20)        0 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/utils/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     6340 2022-11-02 16:33:13.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/utils/exceptions.py
--rw-r--r--   0 szymonos   (504) staff       (20)     9500 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/utils/metrics.py
--rw-r--r--   0 szymonos   (504) staff       (20)     2046 2023-01-31 22:52:39.000000 pyinterpolate-0.3.7/pyinterpolate/variogram/utils/plots.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.569831 pyinterpolate-0.3.7/pyinterpolate/viz/
--rw-r--r--   0 szymonos   (504) staff       (20)       55 2023-01-31 22:52:39.000000 pyinterpolate-0.3.7/pyinterpolate/viz/__init__.py
--rw-r--r--   0 szymonos   (504) staff       (20)     5371 2023-01-16 14:22:22.000000 pyinterpolate-0.3.7/pyinterpolate/viz/raster.py
-drwxr-xr-x   0 szymonos   (504) staff       (20)        0 2023-02-09 08:59:27.528443 pyinterpolate-0.3.7/pyinterpolate.egg-info/
--rw-r--r--   0 szymonos   (504) staff       (20)     9464 2023-02-09 08:59:27.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/PKG-INFO
--rw-r--r--   0 szymonos   (504) staff       (20)     3155 2023-02-09 08:59:27.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/SOURCES.txt
--rw-r--r--   0 szymonos   (504) staff       (20)        1 2023-02-09 08:59:27.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/dependency_links.txt
--rw-r--r--   0 szymonos   (504) staff       (20)        1 2023-01-16 14:23:00.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/not-zip-safe
--rw-r--r--   0 szymonos   (504) staff       (20)      904 2023-02-09 08:59:27.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/requires.txt
--rw-r--r--   0 szymonos   (504) staff       (20)       14 2023-02-09 08:59:27.000000 pyinterpolate-0.3.7/pyinterpolate.egg-info/top_level.txt
--rw-r--r--   0 szymonos   (504) staff       (20)       80 2022-10-01 08:48:28.000000 pyinterpolate-0.3.7/pyproject.toml
--rw-r--r--   0 szymonos   (504) staff       (20)     2268 2023-02-09 08:59:27.572306 pyinterpolate-0.3.7/setup.cfg
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.885621 pyinterpolate-0.4/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       42 2021-10-17 13:15:38.000000 pyinterpolate-0.4/MANIFEST.in
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     9656 2023-04-06 10:00:28.885621 pyinterpolate-0.4/PKG-INFO
+-rwxrwxr-x   0 szymon    (1000) szymon    (1000)     8652 2023-04-06 09:25:45.000000 pyinterpolate-0.4/README.md
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/
+-rwxrwxr-x   0 szymon    (1000) szymon    (1000)     1442 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/__init__.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/distance/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      187 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/distance/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     7804 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/distance/clusters.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    11000 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/distance/distance.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     6216 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/distance/gridding.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/idw/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       60 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/idw/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     3507 2022-10-08 09:51:45.000000 pyinterpolate-0.4/pyinterpolate/idw/idw.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/io/
+-rwxrwxr-x   0 szymon    (1000) szymon    (1000)       70 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/io/__init__.py
+-rwxrwxr-x   0 szymon    (1000) szymon    (1000)     5946 2022-10-08 09:51:45.000000 pyinterpolate-0.4/pyinterpolate/io/read_data.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/kriging/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      595 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/__init__.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate/kriging/models/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/__init__.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/kriging/models/block/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      187 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/block/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     7711 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/block/area_to_area_poisson_kriging.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     9806 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/block/area_to_point_poisson_kriging.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     7405 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/block/centroid_based_poisson_kriging.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    10644 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/block/weight.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/kriging/models/indicator/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/indicator/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    13128 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/indicator/indicator_point_kriging.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/kriging/models/point/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/point/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     6965 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/point/ordinary_kriging.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     3766 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/point/simple_kriging.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/kriging/models/structures/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/structures/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      687 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/models/structures/point_kriging.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     7666 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/point_kriging.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/kriging/utils/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/kriging/utils/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     1078 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/utils/kwarnings.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     4870 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/kriging/utils/process.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/pipelines/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      246 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/pipelines/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    13437 2022-10-08 09:51:45.000000 pyinterpolate-0.4/pyinterpolate/pipelines/block_filtering.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     5227 2022-11-05 20:50:31.000000 pyinterpolate-0.4/pyinterpolate/pipelines/deconvolution.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    12890 2022-10-08 09:51:45.000000 pyinterpolate-0.4/pyinterpolate/pipelines/multi_kriging.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/processing/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       79 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/processing/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     2543 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/processing/checks.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/processing/preprocessing/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/processing/preprocessing/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    17173 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/processing/preprocessing/blocks.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    36344 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/processing/select_values.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/processing/transform/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/processing/transform/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     5490 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/processing/transform/statistics.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    11202 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/processing/transform/transform.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/processing/utils/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:15.000000 pyinterpolate-0.4/pyinterpolate/processing/utils/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     1802 2022-11-05 20:50:31.000000 pyinterpolate-0.4/pyinterpolate/processing/utils/exceptions.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/validation/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/validation/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     4079 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/validation/cross_validation.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.877621 pyinterpolate-0.4/pyinterpolate/variogram/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      682 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/__init__.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/empirical/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     1857 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/empirical/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    23322 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/empirical/cloud.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    10720 2022-12-24 08:14:03.000000 pyinterpolate-0.4/pyinterpolate/variogram/empirical/covariance.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    25423 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/empirical/experimental_variogram.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    23469 2022-12-24 08:14:03.000000 pyinterpolate-0.4/pyinterpolate/variogram/empirical/semivariance.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/indicator/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/indicator/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    16462 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/indicator/indicator_variogram.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/regularization/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    24569 2022-12-24 08:14:03.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/aggregated.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     1489 2022-10-09 07:47:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/avg_block_to_block_semivariances.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     4047 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/avg_inblock_semivariances.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     5343 2022-10-09 07:47:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/block_to_block_semivariance.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     8847 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/inblock_semivariance.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    33508 2022-12-24 08:14:03.000000 pyinterpolate-0.4/pyinterpolate/variogram/regularization/deconvolution.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     5340 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/__init__.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.881621 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/models/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       31 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/models/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     8319 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/models/variogram_models.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)    36064 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/semivariogram.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     1140 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/theoretical/spatial_dependency_index.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.885621 pyinterpolate-0.4/pyinterpolate/variogram/utils/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        0 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/utils/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     6340 2022-11-05 20:50:31.000000 pyinterpolate-0.4/pyinterpolate/variogram/utils/exceptions.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     9500 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyinterpolate/variogram/utils/metrics.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     2046 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/variogram/utils/plots.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.885621 pyinterpolate-0.4/pyinterpolate/viz/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       55 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/viz/__init__.py
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     5348 2023-04-06 09:25:45.000000 pyinterpolate-0.4/pyinterpolate/viz/raster.py
+drwxrwxr-x   0 szymon    (1000) szymon    (1000)        0 2023-04-06 10:00:28.873621 pyinterpolate-0.4/pyinterpolate.egg-info/
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     9656 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/PKG-INFO
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     3556 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/SOURCES.txt
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        1 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/dependency_links.txt
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)        1 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/not-zip-safe
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)      884 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/requires.txt
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       14 2023-04-06 10:00:28.000000 pyinterpolate-0.4/pyinterpolate.egg-info/top_level.txt
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)       80 2022-09-07 20:00:16.000000 pyinterpolate-0.4/pyproject.toml
+-rw-rw-r--   0 szymon    (1000) szymon    (1000)     2184 2023-04-06 10:00:28.885621 pyinterpolate-0.4/setup.cfg
```

### Comparing `pyinterpolate-0.3.7/PKG-INFO` & `pyinterpolate-0.4/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: pyinterpolate
-Version: 0.3.7
+Version: 0.4
 Summary: Spatial Interpolation in Python
 Home-page: https://github.com/DataverseLabs/pyinterpolate
-Download-URL: https://github.com/DataverseLabs/pyinterpolate/archive/v0.3.tar.gz
+Download-URL: https://github.com/DataverseLabs/pyinterpolate/archive/
 Author: Szymon Moliński
 Author-email: simon@dataverselabs.com
 License: BSD 3-clause
 Project-URL: Documentation, https://readthedocs.org/projects/pyinterpolate/
 Project-URL: Source, https://github.com/DataverseLabs/pyinterpolate
 Project-URL: Tracker, https://github.com/DataverseLabs/pyinterpolate/issues
 Classifier: Development Status :: 4 - Beta
@@ -19,19 +19,19 @@
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown; charset=UTF-8
 
 ![status](https://joss.theoj.org/papers/3f87f562264c4e5174d9e6ed6d8812aa/status.svg) ![License](https://img.shields.io/github/license/szymon-datalions/pyinterpolate) ![Documentation Status](https://readthedocs.org/projects/pyinterpolate/badge/?version=latest) [![CodeFactor](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate/badge)](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate)
 
-![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov03.jpg?raw=true  "Pyinterpolate logo")
+![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov04.jpg?raw=true  "Pyinterpolate logo")
 
 # Pyinterpolate
 
-**version 0.3.7** - *Kyiv*
+**version 0.4** - *Kharkiv*
 
 ---
 
 Pyinterpolate is the Python library for **spatial statistics**. The package provides access to spatial statistics tools used in various studies. This package helps you **interpolate spatial data** with the *Kriging* technique.
 
 If you’re:
 
@@ -208,15 +208,15 @@
 * scipy
 * shapely
 * fiona
 * rtree
 * prettytable
 * pandas
 * dask
-* requests
+* dbscan
 
 You may check a specific version of requirements in the `setup.cfg` file.
 
 ## Package structure
 
 High level overview:
 
@@ -227,10 +227,14 @@
     - [x] `kriging` - Ordinary Kriging, Simple Kriging, Poisson Kriging: centroid based, area-to-area, area-to-point,
     - [x] `pipelines` - a complex functions to smooth a block data, download sample data, compare different kriging techniques, and filter blocks,
     - [x] `processing` - core data structures of the package: `Blocks` and `PointSupport`, and additional functions used for internal processes,
     - [x] `variogram` - experimental variogram, theoretical variogram, variogram point cloud, semivariogram regularization & deconvolution,
     - [x] `viz` - interpolation of smooth surfaces from points into rasters.
  - [x] `tutorials` - tutorials (Basic, Intermediate and Advanced).
 
+## Datasets
+
+Datasets and scripts to download spatial data from external API's are available in a dedicated package: **[pyinterpolate-datasets](https://pypi.org/project/pyinterpolate-datasets/2023.0.0/)**
+
 ## API documentation
 
 https://pyinterpolate.readthedocs.io/en/latest/
```

### Comparing `pyinterpolate-0.3.7/README.md` & `pyinterpolate-0.4/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 ![status](https://joss.theoj.org/papers/3f87f562264c4e5174d9e6ed6d8812aa/status.svg) ![License](https://img.shields.io/github/license/szymon-datalions/pyinterpolate) ![Documentation Status](https://readthedocs.org/projects/pyinterpolate/badge/?version=latest) [![CodeFactor](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate/badge)](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate)
 
-![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov03.jpg?raw=true  "Pyinterpolate logo")
+![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov04.jpg?raw=true  "Pyinterpolate logo")
 
 # Pyinterpolate
 
-**version 0.3.7** - *Kyiv*
+**version 0.4** - *Kharkiv*
 
 ---
 
 Pyinterpolate is the Python library for **spatial statistics**. The package provides access to spatial statistics tools used in various studies. This package helps you **interpolate spatial data** with the *Kriging* technique.
 
 If you’re:
 
@@ -185,15 +185,15 @@
 * scipy
 * shapely
 * fiona
 * rtree
 * prettytable
 * pandas
 * dask
-* requests
+* dbscan
 
 You may check a specific version of requirements in the `setup.cfg` file.
 
 ## Package structure
 
 High level overview:
 
@@ -204,10 +204,14 @@
     - [x] `kriging` - Ordinary Kriging, Simple Kriging, Poisson Kriging: centroid based, area-to-area, area-to-point,
     - [x] `pipelines` - a complex functions to smooth a block data, download sample data, compare different kriging techniques, and filter blocks,
     - [x] `processing` - core data structures of the package: `Blocks` and `PointSupport`, and additional functions used for internal processes,
     - [x] `variogram` - experimental variogram, theoretical variogram, variogram point cloud, semivariogram regularization & deconvolution,
     - [x] `viz` - interpolation of smooth surfaces from points into rasters.
  - [x] `tutorials` - tutorials (Basic, Intermediate and Advanced).
 
+## Datasets
+
+Datasets and scripts to download spatial data from external API's are available in a dedicated package: **[pyinterpolate-datasets](https://pypi.org/project/pyinterpolate-datasets/2023.0.0/)**
+
 ## API documentation
 
 https://pyinterpolate.readthedocs.io/en/latest/
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/__init__.py` & `pyinterpolate-0.4/pyinterpolate/__init__.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,41 +1,45 @@
 # Distance
 from pyinterpolate.distance import calc_point_to_point_distance, calc_block_to_block_distance
+from pyinterpolate.distance import aggregate_cluster, ClusterDetector
+from pyinterpolate.distance import create_grid, points_to_grid
 
 # IDW
 from pyinterpolate.idw import inverse_distance_weighting
 
 # I/O
 from pyinterpolate.io import read_block, read_csv, read_txt
 
 # Kriging
 # Point
 from pyinterpolate.kriging import kriging, ordinary_kriging, simple_kriging
 # Block
 from pyinterpolate.kriging import centroid_poisson_kriging, area_to_area_pk, area_to_point_pk
+# Indicator
+from pyinterpolate.kriging import IndicatorKriging
 
 # Pipelines
 # Excluded: multi_kriging (BlockToBlockKrigingComparison)
 # PK
 from pyinterpolate.pipelines import BlockFilter, smooth_blocks
-# Data
-from pyinterpolate.pipelines import download_air_quality_poland
 
 # Processing
 from pyinterpolate.processing import Blocks, PointSupport
 
 # Variogram
 # Experimental
 from pyinterpolate.variogram import build_experimental_variogram, build_variogram_point_cloud, ExperimentalVariogram, \
     VariogramCloud
 # Theoretical
 from pyinterpolate.variogram import build_theoretical_variogram, TheoreticalVariogram
 # Blocks
 from pyinterpolate.variogram import AggregatedVariogram
 # Deconvolution
 from pyinterpolate.variogram import Deconvolution
+# Indicator
+from pyinterpolate.variogram import IndicatorVariogramData, ExperimentalIndicatorVariogram, IndicatorVariograms
 
 # Viz
 from pyinterpolate.viz import interpolate_raster
 
 
 __version__ = "0.3.7"
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/distance/distance.py` & `pyinterpolate-0.4/pyinterpolate/distance/distance.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/idw/idw.py` & `pyinterpolate-0.4/pyinterpolate/idw/idw.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/io/read_data.py` & `pyinterpolate-0.4/pyinterpolate/io/read_data.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/area_to_area_poisson_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/block/area_to_area_poisson_kriging.py`

 * *Files 1% similar despite different names*

```diff
@@ -182,15 +182,14 @@
             logging.debug(f'Prediction below 0 for area {u_idx}')
         if raise_when_negative_prediction:
             raise ValueError(f'Predicted value is {zhat} and it should not be lower than 0. Check your sampling '
                              f'grid, samples, number of neighbors or semivariogram model type.')
 
     sigmasq = np.matmul(w.T, k_ones)
 
-
     distances_within_unknown_block = get_distances_within_unknown(unknown_block_point_support)
     semivariance_within_unknown = b2b_semivariance.calculate_average_semivariance({
         u_idx: distances_within_unknown_block
     })[u_idx]
 
     covariance_within_unknown = sem_to_cov([semivariance_within_unknown], sill)[0]
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/area_to_point_poisson_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/block/area_to_point_poisson_kriging.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/centroid_based_poisson_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/block/centroid_based_poisson_kriging.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/block/weight.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/block/weight.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/ordinary_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/point/ordinary_kriging.py`

 * *Files 2% similar despite different names*

```diff
@@ -82,16 +82,17 @@
     p_ones_row = np.ones((1, predicted_with_ones_col.shape[1]))
     p_ones_row[0][-1] = 0.
     weights = np.r_[predicted_with_ones_col, p_ones_row]
 
     try:
         output_weights = solve_weights(weights, k, allow_approximate_solutions)
     except np.linalg.LinAlgError as _:
-        msg = 'Singular matrix in Kriging system detected, check if you have duplicated coordinates ' \
-              'in the ``known_locations`` variable.'
+        msg = "Singular matrix in Kriging system detected, check if you have duplicated coordinates " \
+              "in the ``known_locations`` variable. If your data doesn't have duplicates then set " \
+              "``allow_approximate_solutions`` parameter to ``True``."
         raise RuntimeError(msg)
 
     zhat = dataset[:, -2].dot(output_weights[:-1])
 
     sigma = np.matmul(output_weights.T, k)
 
     if sigma < 0:
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/point/simple_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/point/simple_kriging.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,22 +1,20 @@
 """
 Perform point simple kriging.
 
 Authors
 -------
 1. Szymon Moliński | @SimonMolinsky
 
-TODO
-----
-* log k, predicted, dataset
 """
 # Python core
 from typing import List, Union, Tuple
 
 # Core calculation and data visualization
+import logging
 import numpy as np
 
 # Pyinterpolate
 from pyinterpolate.kriging.utils.process import get_predictions, solve_weights
 from pyinterpolate.variogram import TheoreticalVariogram
 
 
@@ -71,21 +69,22 @@
         ``[predicted value, variance error, longitude (x), latitude (y)]``
 
     Raises
     ------
     RunetimeError
         Singularity matrix in a Kriging system.
     """
-
+    logging.info("SIMPLE KRIGING | Operation starts")
     k, predicted, dataset = get_predictions(theoretical_model,
                                             known_locations,
                                             unknown_location,
                                             neighbors_range,
                                             no_neighbors,
                                             use_all_neighbors_in_range)
+    logging.info("SIMPLE KRIGING | Weights are prepared")
 
     try:
         output_weights = solve_weights(predicted, k, allow_approximate_solutions)
     except np.linalg.LinAlgError as _:
         msg = 'Singular matrix in Kriging system detected, check if you have duplicated coordinates ' \
               'in the ``known_locations`` variable.'
         raise RuntimeError(msg)
@@ -93,10 +92,12 @@
     r = dataset[:, -2] - process_mean
     zhat = r.dot(output_weights)
     zhat = zhat + process_mean
 
     sigma = np.matmul(output_weights.T, k)
 
     if sigma < 0:
+        logging.info("SIMPLE KRIGING | Variance error lower than zero, NaN is returned")
         return [zhat, np.nan, unknown_location[0], unknown_location[1]]
 
+    logging.info("SIMPLE KRIGING | Process ends")
     return [zhat, sigma, unknown_location[0], unknown_location[1]]
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/models/structures/point_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/models/structures/point_kriging.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/point_kriging.py` & `pyinterpolate-0.4/pyinterpolate/kriging/point_kriging.py`

 * *Files 22% similar despite different names*

```diff
@@ -27,15 +27,16 @@
             points: Union[np.ndarray, List, Tuple],
             how: str = 'ok',
             neighbors_range: Union[float, None] = None,
             no_neighbors: int = 4,
             use_all_neighbors_in_range=False,
             sk_mean: Union[float, None] = None,
             allow_approx_solutions=False,
-            number_of_workers: int = 1) -> np.ndarray:
+            number_of_workers: int = 1,
+            show_progress_bar: bool = True) -> np.ndarray:
     """Function manages Ordinary Kriging and Simple Kriging predictions.
 
     Parameters
     ----------
     observations : numpy array
         Known points and their values.
 
@@ -71,14 +72,17 @@
         if you don't know what are you doing. This parameter can be useful when you have clusters in your dataset,
         that can lead to singular or near-singular matrix creation.
 
     number_of_workers : int, default=1
         How many processing units can be used for predictions. Increase it only for a very large number of
         interpolated points (~10k+).
 
+    show_progress_bar : bool, default=True
+        Show progress bar of predictions.
+
     Returns
     -------
     : numpy array
         Predictions ``[predicted value, variance error, longitude (x), latitude (y)]``
     """
 
     # Check model type
@@ -102,38 +106,65 @@
     else:
         model = models[how]
 
     results = []
 
     if number_of_workers == 1:
         # Don't use dask
-        for point in tqdm(points):
-            prediction = [np.nan, np.nan, np.nan, np.nan]
-            if how == 'ok':
-                prediction = model(
-                    theoretical_model,
-                    observations,
-                    point,
-                    neighbors_range=neighbors_range,
-                    no_neighbors=no_neighbors,
-                    use_all_neighbors_in_range=use_all_neighbors_in_range,
-                    allow_approximate_solutions=allow_approx_solutions
-                )
-            elif how == 'sk':
-                prediction = model(
-                    theoretical_model,
-                    observations,
-                    point,
-                    sk_mean,
-                    neighbors_range=neighbors_range,
-                    no_neighbors=no_neighbors,
-                    use_all_neighbors_in_range=use_all_neighbors_in_range,
-                    allow_approximate_solutions=allow_approx_solutions
-                )
-            results.append(prediction)
+
+        if show_progress_bar:
+            for point in tqdm(points):
+                prediction = [np.nan, np.nan, np.nan, np.nan]
+                if how == 'ok':
+                    prediction = model(
+                        theoretical_model,
+                        observations,
+                        point,
+                        neighbors_range=neighbors_range,
+                        no_neighbors=no_neighbors,
+                        use_all_neighbors_in_range=use_all_neighbors_in_range,
+                        allow_approximate_solutions=allow_approx_solutions
+                    )
+                elif how == 'sk':
+                    prediction = model(
+                        theoretical_model,
+                        observations,
+                        point,
+                        sk_mean,
+                        neighbors_range=neighbors_range,
+                        no_neighbors=no_neighbors,
+                        use_all_neighbors_in_range=use_all_neighbors_in_range,
+                        allow_approximate_solutions=allow_approx_solutions
+                    )
+                results.append(prediction)
+        else:
+            for point in points:
+                    prediction = [np.nan, np.nan, np.nan, np.nan]
+                    if how == 'ok':
+                        prediction = model(
+                            theoretical_model,
+                            observations,
+                            point,
+                            neighbors_range=neighbors_range,
+                            no_neighbors=no_neighbors,
+                            use_all_neighbors_in_range=use_all_neighbors_in_range,
+                            allow_approximate_solutions=allow_approx_solutions
+                        )
+                    elif how == 'sk':
+                        prediction = model(
+                            theoretical_model,
+                            observations,
+                            point,
+                            sk_mean,
+                            neighbors_range=neighbors_range,
+                            no_neighbors=no_neighbors,
+                            use_all_neighbors_in_range=use_all_neighbors_in_range,
+                            allow_approximate_solutions=allow_approx_solutions
+                        )
+                    results.append(prediction)
         predictions = np.array(results)
     else:
         # Use dask
         for point in points:
             prediction = [np.nan, np.nan, np.nan, np.nan]
             if how == 'ok':
                 prediction = dask.delayed(model)(
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/utils/kwarnings.py` & `pyinterpolate-0.4/pyinterpolate/kriging/utils/kwarnings.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/kriging/utils/process.py` & `pyinterpolate-0.4/pyinterpolate/kriging/utils/process.py`

 * *Files 0% similar despite different names*

```diff
@@ -118,13 +118,13 @@
     except np.linalg.LinAlgError as linalgerr:
         if np.mean(weights) == 0 or np.mean(k) == 0:
             warnings.warn(ZerosMatrixWarning().__str__())
             solved = np.zeros(len(k))
         else:
             if allow_lsa:
                 warnings.warn(LeastSquaresApproximationWarning().__str__())
-                solved = np.linalg.lstsq(weights, k)
+                solved = np.linalg.lstsq(weights, k, rcond=None)
                 solved = solved[0]
             else:
                 raise linalgerr
 
     return solved
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/pipelines/block_filtering.py` & `pyinterpolate-0.4/pyinterpolate/pipelines/block_filtering.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/pipelines/deconvolution.py` & `pyinterpolate-0.4/pyinterpolate/pipelines/deconvolution.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/pipelines/multi_kriging.py` & `pyinterpolate-0.4/pyinterpolate/pipelines/multi_kriging.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/checks.py` & `pyinterpolate-0.4/pyinterpolate/processing/checks.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/preprocessing/blocks.py` & `pyinterpolate-0.4/pyinterpolate/processing/preprocessing/blocks.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/select_values.py` & `pyinterpolate-0.4/pyinterpolate/processing/select_values.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/transform/statistics.py` & `pyinterpolate-0.4/pyinterpolate/processing/transform/statistics.py`

 * *Files 5% similar despite different names*

```diff
@@ -84,14 +84,41 @@
         raise ValueError(f'The parameter z_upper must be a float greater than zero.')
 
     outliers = stats.zscore(dataset)
     mask = (outliers > z_upper) | (outliers < z_lower)
     return mask
 
 
+def select_variogram_thresholds(ds: Iterable,
+                                n_thresh: int) -> List[float]:
+    """
+    Function selects ``n_thresh`` thresholds of a sample dataset from its histogram, it divides histogram based on
+    the n-quantiles.
+
+    Parameters
+    ----------
+    ds : Iterable
+        Data values used for interpolation.
+
+    n_thresh : int
+        The number of thresholds.
+
+    Returns
+    -------
+    thresholds : List
+        Thresholds used for indicator Kriging.
+    """
+
+    quantiles = np.linspace(0, 1, n_thresh+1)
+
+    thresholds = [np.quantile(ds, q=q) for q in quantiles[1:]]
+
+    return thresholds
+
+
 def remove_outliers(data: Union[Iterable, Dict],
                     method='zscore',
                     z_lower_limit=-3,
                     z_upper_limit=3,
                     iqr_lower_limit=1.5,
                     iqr_upper_limit=1.5) -> Union[List, Dict]:
     """
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/transform/transform.py` & `pyinterpolate-0.4/pyinterpolate/processing/transform/transform.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 """
 Data transforming functions.
 
 Authors
 -------
 1. Szymon Moliński | @SimonMolinsky
 """
-from typing import Dict, Union
+from typing import Dict, Union, List
 
 import geopandas as gpd
 import numpy as np
 import pandas as pd
 
 from pyinterpolate.processing.preprocessing.blocks import PointSupport, Blocks
 
@@ -66,14 +66,47 @@
     d = {}
     for _id in block_df[idx_col].unique():
         d[_id] = block_df[block_df[idx_col] == _id][[x_col, y_col, value_col]].values
 
     return d
 
 
+def code_indicators(ds: np.ndarray, thresholds: List) -> np.ndarray:
+    """
+    Function transforms kriging values into a vector of their indicators.
+
+    Parameters
+    ----------
+    ds : numpy array
+        Kriging dataset [lon, lat, value]
+
+    thresholds : List
+        The list of possible thresholds.
+
+    Returns
+    -------
+    ids : numpy array
+        [lon, lat, bin value for thresh 0, ..., bin value for thresh n].
+
+    """
+
+    ids = []
+    thresh_arr = np.array(thresholds)
+
+    for row in ds:
+        _r = [row[0], row[1]]
+        _val = row[2]
+        _indicators = _val <= thresh_arr
+        _r.extend(_indicators.astype(int))
+        ids.append(_r)
+
+    ids = np.array(ids)
+    return ids
+
+
 def get_areal_centroids_from_agg(
         aggregated_data: Union[Blocks, gpd.GeoDataFrame, pd.DataFrame, np.ndarray]) -> np.ndarray:
     """
 
     Parameters
     ----------
     aggregated_data : Union[Blocks, gpd.GeoDataFrame, pd.DataFrame, np.ndarray]
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/processing/utils/exceptions.py` & `pyinterpolate-0.4/pyinterpolate/processing/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/__init__.py` & `pyinterpolate-0.4/pyinterpolate/variogram/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,6 +1,8 @@
 from pyinterpolate.variogram.empirical.experimental_variogram import build_experimental_variogram, ExperimentalVariogram
 from pyinterpolate.variogram.empirical.cloud import build_variogram_point_cloud
 from pyinterpolate.variogram.empirical import VariogramCloud
 from pyinterpolate.variogram.theoretical.semivariogram import build_theoretical_variogram, TheoreticalVariogram
 from pyinterpolate.variogram.regularization.aggregated import AggregatedVariogram
 from pyinterpolate.variogram.regularization.deconvolution import Deconvolution
+from pyinterpolate.variogram.indicator.indicator_variogram import IndicatorVariogramData,\
+    ExperimentalIndicatorVariogram, IndicatorVariograms
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/__init__.py` & `pyinterpolate-0.4/pyinterpolate/variogram/empirical/__init__.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/cloud.py` & `pyinterpolate-0.4/pyinterpolate/variogram/empirical/cloud.py`

 * *Files 2% similar despite different names*

```diff
@@ -158,17 +158,14 @@
 
     step_size : float
         The distance between lags within each points are included in the calculations.
 
     max_range : float
         The maximum range of analysis.
 
-    weights : numpy array or None, optional, default=None
-        Weights assigned to points, index of weight must be the same as index of point.
-
     direction : float (in range [0, 360]), default=None
         Direction of semivariogram, values from 0 to 360 degrees:
         - 0 or 180: is E-W,
         - 90 or 270 is N-S,
         - 45 or 225 is NE-SW,
         - 135 or 315 is NW-SE.
 
@@ -222,17 +219,14 @@
 
     step_size : float
         The distance between lags within each points are included in the calculations.
 
     max_range : float
         The maximum range of analysis.
 
-    weights : numpy array or None, optional, default=None
-        Weights assigned to points, index of weight must be the same as index of point.
-
     direction : float (in range [0, 360]), optional, default=None
         Direction of semivariogram, values from 0 to 360 degrees:
 
         - 0 or 180: is E-W,
         - 90 or 270 is N-S,
         - 45 or 225 is NE-SW,
         - 135 or 315 is NW-SE.
@@ -479,15 +473,14 @@
         elif kind == 'violin':
             self._violin_plot()
         else:
             msg = f'Plot kind {kind} is not available. Use "scatter", "box" or "violin" instead.'
             raise KeyError(msg)
         return True
 
-
     def remove_outliers(self, method='zscore',
                         z_lower_limit=-3,
                         z_upper_limit=3,
                         iqr_lower_limit=1.5,
                         iqr_upper_limit=1.5,
                         inplace=False):
         """
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/covariance.py` & `pyinterpolate-0.4/pyinterpolate/variogram/empirical/covariance.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/experimental_variogram.py` & `pyinterpolate-0.4/pyinterpolate/variogram/empirical/experimental_variogram.py`

 * *Files 0% similar despite different names*

```diff
@@ -333,14 +333,17 @@
     +-----+--------------------+---------------------+--------------------+
     | lag |    semivariance    |      covariance     |    var_cov_diff    |
     +-----+--------------------+---------------------+--------------------+
     | 1.0 |       4.625        | -0.5434027777777798 | 4.791923487836951  |
     | 2.0 | 5.2272727272727275 | -0.7954545454545454 | 5.0439752555137165 |
     | 3.0 |        6.0         | -1.2599999999999958 | 5.508520710059168  |
     +-----+--------------------+---------------------+--------------------+
+
+    # TODO
+    * calculate variance ALWAYS
     """
 
     def __init__(self,
                  input_array: Union[np.ndarray, list, tuple],
                  step_size: float,
                  max_range: float,
                  weights=None,
@@ -362,15 +365,15 @@
         self.experimental_semivariance_array = None
         self.experimental_covariance_array = None
         self.lags = None
         self.experimental_semivariances = None
         self.experimental_covariances = None
         self.variance_covariances_diff = None
         self.points_per_lag = None
-        self.variance = 0
+        self.variance = 0.0
 
         self.step = step_size
         self.mx_rng = max_range
         self.weights = weights
         self.direct = direction
         self.tol = tolerance
         self.method = method
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/empirical/semivariance.py` & `pyinterpolate-0.4/pyinterpolate/variogram/empirical/semivariance.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/aggregated.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/aggregated.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/avg_block_to_block_semivariances.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/avg_block_to_block_semivariances.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/avg_inblock_semivariances.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/avg_inblock_semivariances.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/block_to_block_semivariance.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/block_to_block_semivariance.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/block/inblock_semivariance.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/block/inblock_semivariance.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/regularization/deconvolution.py` & `pyinterpolate-0.4/pyinterpolate/variogram/regularization/deconvolution.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/__init__.py` & `pyinterpolate-0.4/pyinterpolate/variogram/theoretical/__init__.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/models/variogram_models.py` & `pyinterpolate-0.4/pyinterpolate/variogram/theoretical/models/variogram_models.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/theoretical/semivariogram.py` & `pyinterpolate-0.4/pyinterpolate/variogram/theoretical/semivariogram.py`

 * *Files 3% similar despite different names*

```diff
@@ -24,14 +24,16 @@
 from pyinterpolate.variogram.theoretical.models import circular_model, cubic_model, linear_model, exponential_model, \
     gaussian_model, spherical_model, power_model
 from pyinterpolate.variogram.empirical.experimental_variogram import ExperimentalVariogram
 from pyinterpolate.variogram.utils.metrics import forecast_bias, root_mean_squared_error, \
     symmetric_mean_absolute_percentage_error, mean_absolute_error, weighted_root_mean_squared_error
 from pyinterpolate.variogram.utils.exceptions import validate_selected_errors, check_ranges, check_sills
 
+from pyinterpolate.variogram.theoretical.spatial_dependency_index import calculate_spatial_dependence_index
+
 
 class TheoreticalVariogram:
     """Theoretical model of a spatial dissimilarity.
 
     Parameters
     ----------
     model_params : Dict, default=None
@@ -86,14 +88,27 @@
     bias : float, default=0
         Forecast Bias of the modeled variogram vs experimental points. Large positive value means that the estimated
         model underestimates values. A large negative value means that model overestimates predictions.
 
     smape : float, default=0
         Symmetric Mean Absolute Percentage Error of the prediction - values from 0 to 100%.
 
+    spatial_dependency_ratio : float, default = None
+        The ratio of nugget vs sill multiplied by 100. Levels from 0 to 25 indicate strong spatial dependency,
+        from 25 to 75 moderate spatial dependency, from 75 to 95 weak spatial dependency, and above process is
+        considered to be not spatially-depended.
+
+    spatial_dependency_strength : str, default = "Unknown"
+        Descriptive indicator of spatial dependency strength based on the ``spatial_dependency_level``. It could be:
+          * ``unknown`` if ratio is ``None``,
+          * ``strong`` if ratio is below 25,
+          * ``moderate`` if ratio is between 25 and 75,
+          * ``weak`` if ratio is between 75 and 95,
+          * ``no spatial dependency`` if ratio is greater than 95.
+
     are_params : bool
         Check if model parameters were given during initialization.
 
     Methods
     -------
     fit()
         Fits experimental variogram data into theoretical model.
@@ -178,21 +193,25 @@
         self.sill = 0.
 
         self.direction = None
 
         if self.are_params:
             self._set_model_parameters(model_params)
 
-        # Errror
+        # Error
         self.deviation_weighting = None
         self.rmse = 0.
         self.bias = 0.
         self.smape = 0.
         self.mae = 0.
 
+        # Spatial dependency
+        self.spatial_dependency_ratio = None
+        self.spatial_dependency_strength = 'Unknown'
+
     # Core functions
 
     def fit(self,
             experimental_variogram: Union[ExperimentalVariogram, np.ndarray],
             model_type: str,
             sill: float,
             rang: float,
@@ -294,20 +313,23 @@
 
         if update_attrs:
             attrs_to_update = {
                 'fitted_model': _theoretical_values,
                 'model_type': model_type,
                 'nugget': nugget,
                 'sill': sill,
-                'rang': rang
+                'range': rang
             }
             attrs_to_update.update(_error)
 
             self._update_attributes(**attrs_to_update)
 
+        # Update spatial dependency
+        self._update_spatial_dependency()
+
         return _theoretical_values, _error
 
     def autofit(self,
                 experimental_variogram: Union[ExperimentalVariogram, np.ndarray],
                 model_types: Union[str, list] = 'all',
                 nugget=0,
                 rang=None,
@@ -411,15 +433,15 @@
         -------
         model_attributes : Dict
             Attributes dict:
 
             >>> {
             ...     'model_type': model_name,
             ...     'sill': model_sill,
-            ...     'rang': model_range,
+            ...     'range': model_range,
             ...     'nugget': model_nugget,
             ...     'error_type': type_of_error_metrics,
             ...     'error value': error_value
             ... }
 
         Warns
         -----
@@ -508,15 +530,15 @@
         err_val = np.inf
 
         # Initlize parameters
         optimal_parameters = {
             'model_type': '',
             'nugget': 0,
             'sill': 0,
-            'rang': 0
+            'range': 0
         }
 
         for _mtype in mtypes:
             for _rang in min_max_ranges:
                 for _sill in min_max_sill:
                     # Create model
                     _mdl_fn = self.variogram_models[_mtype]
@@ -532,21 +554,24 @@
 
                     # Check if model is better than the previous
                     if _err[error_estimator] < err_val:
                         err_val = _err[error_estimator]
                         optimal_parameters['model_type'] = _mtype
                         optimal_parameters['nugget'] = nugget
                         optimal_parameters['sill'] = _sill
-                        optimal_parameters['rang'] = _rang
+                        optimal_parameters['range'] = _rang
                         optimal_parameters['fitted_model'] = _fitted_model
                         optimal_parameters.update(_err)
 
         if auto_update_attributes:
             self._update_attributes(**optimal_parameters)
 
+        # Update spatial dependency
+        self._update_spatial_dependency()
+
         if return_params:
             return optimal_parameters
 
     def predict(self, distances: np.ndarray) -> np.ndarray:
         """
         Method returns a semivariance per distance.
 
@@ -688,14 +713,25 @@
         # Get SMAPE
         if smape:
             _smape = symmetric_mean_absolute_percentage_error(fitted_values, _real_values)
             model_error['smape'] = _smape
 
         return model_error
 
+    def _update_spatial_dependency(self):
+        """
+        Method updates spatial dependency of a fitted variogram.
+        """
+        if self.nugget > 0:
+            index_ratio, index_strength = calculate_spatial_dependence_index(
+                self.nugget, self.sill
+            )
+            self.spatial_dependency_ratio = index_ratio
+            self.spatial_dependency_strength = index_strength
+
     # I/O
 
     def to_dict(self) -> dict:
         """Method exports the theoretical variogram parameters to a dictionary.
 
         Returns
         -------
@@ -719,15 +755,15 @@
             'range': self.rang,
             'nugget': self.nugget,
             'direction': self.direction
         }
 
         return modeled_parameters
 
-    def from_dict(self, parameters: dict) -> None:
+    def from_dict(self, parameters: dict):
         """Method updates model with a given set of parameters.
 
         Parameters
         ----------
         parameters : Dict
             Dictionary with model's: ``'name', 'nugget', 'sill', 'range', 'direction'``.
         """
@@ -778,21 +814,23 @@
             return 'Theoretical model is not calculated yet. Use fit() or autofit() methods to build or find a model ' \
                    'or import model with from_dict() or from_json() methods.'
         else:
             title = '* Selected model: ' + f'{self.name}'.capitalize() + ' model'
             msg_nugget = f'* Nugget: {self.nugget}'
             msg_sill = f'* Sill: {self.sill}'
             msg_range = f'* Range: {self.rang}'
+            msg_spatial_dependency = f'* Spatial Dependency Strength is {self.spatial_dependency_strength}'
             mean_bias_msg = f'* Mean Bias: {self.bias}'
             mean_rmse_msg = f'* Mean RMSE: {self.rmse}'
             error_weighting = f'* Error-lag weighting method: {self.deviation_weighting}'
 
-            text_list = [title, msg_nugget, msg_sill, msg_range, mean_bias_msg, mean_rmse_msg, error_weighting]
+            text_list = [title, msg_nugget, msg_sill, msg_range, msg_spatial_dependency,
+                         mean_bias_msg, mean_rmse_msg, error_weighting]
 
-            header = '\n'.join(text_list) + '\n' + '\n'
+            header = '\n'.join(text_list) + '\n\n'
 
             if self.experimental_array is not None:
                 # Build pretty table
                 pretty_table = PrettyTable()
                 pretty_table.field_names = ["lag", "theoretical", "experimental", "bias (y-y')"]
 
                 records = []
@@ -801,15 +839,15 @@
                     experimental_semivar = record[1]
                     theoretical_semivar = self.fitted_model[idx][1]
                     bias = experimental_semivar - theoretical_semivar
                     records.append([lag, theoretical_semivar, experimental_semivar, bias])
 
                 pretty_table.add_rows(records)
 
-                msg = header + pretty_table.get_string()
+                msg = header + '\n' + pretty_table.get_string()
                 return msg
             else:
                 return header
 
     def __repr__(self):
         cname = 'TheoreticalVariogram'
         input_params = f'empirical_variogram={self.experimental_variogram},experimental_array={self.experimental_array}'
@@ -860,25 +898,25 @@
                     mtypes.append(mdl)
         return mtypes
 
     def _update_attributes(self,
                            fitted_model=None,
                            model_type=None,
                            nugget=None,
-                           rang=None,
+                           range=None,
                            sill=None,
                            rmse=None,
                            bias=None,
                            mae=None,
                            smape=None):
         # Model parameters
         self.fitted_model = fitted_model
         self.name = model_type
         self.nugget = nugget
-        self.rang = rang
+        self.rang = range
         self.sill = sill
 
         # Dynamic parameters
         self.rmse = rmse
         self.bias = bias
         self.smape = smape
         self.mae = mae
@@ -899,16 +937,15 @@
             msg = f'Defined error {err_name} not exists. Use one of {list(err_dict.keys())} instead.'
             raise KeyError(msg)
 
     @staticmethod
     def __print_autofit_info(model_type: str, nugget: float, sill: float, rang: float, err_type: str, err_value: float):
         msg_core = f'Model {model_type},\n' \
                    f'Model Parameters - nugget: {nugget:.2f}, sill: {sill:.4f}, range: {rang:.4f},\n' \
-                   f'Model Error {err_type}: {err_value}' \
-                   f'\n'
+                   f'Model Error {err_type}: {err_value}\n'
         print(msg_core)
 
     def _fit_model(self, model_fn: Callable, nugget: float, sill: float, rang: float) -> np.array:
         """Method fits selected model into baseline lags.
 
         Parameters
         ----------
@@ -946,14 +983,15 @@
 
     def _set_model_parameters(self, model_params: dict):
         self.nugget = float(model_params['nugget'])
         self.rang = float(model_params['range'])
         self.sill = float(model_params['sill'])
         self.name = model_params['name']
         self.direction = self._set_direction(model_params)
+        self._update_spatial_dependency()
 
 
 def build_theoretical_variogram(experimental_variogram: ExperimentalVariogram,
                                 model_type: str,
                                 sill: float,
                                 rang: float,
                                 nugget: float = 0.,
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/utils/exceptions.py` & `pyinterpolate-0.4/pyinterpolate/variogram/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/utils/metrics.py` & `pyinterpolate-0.4/pyinterpolate/variogram/utils/metrics.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/variogram/utils/plots.py` & `pyinterpolate-0.4/pyinterpolate/variogram/utils/plots.py`

 * *Files identical despite different names*

### Comparing `pyinterpolate-0.3.7/pyinterpolate/viz/raster.py` & `pyinterpolate-0.4/pyinterpolate/viz/raster.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,20 +6,20 @@
 1. Szymon Moliński | @SimonMolinsky
 """
 from typing import Dict
 
 import numpy as np
 
 from pyinterpolate.distance.distance import calc_point_to_point_distance
+from pyinterpolate.kriging.point_kriging import kriging
 from pyinterpolate.variogram.empirical.experimental_variogram import build_experimental_variogram
 from pyinterpolate.variogram.theoretical.semivariogram import TheoreticalVariogram
-from pyinterpolate.kriging.point_kriging import kriging
 
 
-def _set_dims(xs, ys, dmax):
+def set_dimensions(xs, ys, dmax):
     """
     Function sets dimensions of the output array.
 
     Parameters
     ----------
     xs : numpy array
          X coordinates.
@@ -119,15 +119,15 @@
     """
 
     # Set dimension
 
     if isinstance(data, list):
         data = np.array(data)
 
-    x_coords, y_coords, props = _set_dims(data[:, 0], data[:, 1], dim)
+    x_coords, y_coords, props = set_dimensions(data[:, 0], data[:, 1], dim)
 
     # Calculate semivariance if not provided
 
     if semivariogram_model is None:
         distances = calc_point_to_point_distance(data[:, :-1])
 
         maximum_range = np.max(distances)
@@ -153,16 +153,15 @@
             coords = np.array([_x, _y])
             interpolation_points.append(coords)
 
     k = kriging(observations=data,
                 theoretical_model=ts,
                 points=interpolation_points,
                 how='ok',
-                no_neighbors=number_of_neighbors,
-                err_to_nan=True)
+                no_neighbors=number_of_neighbors)
 
     kriged_matrix = k[:, 0].reshape((len(y_coords), len(x_coords)))
     kriged_errors = k[:, 1].reshape((len(y_coords), len(x_coords)))
 
     raster_dict = {
         'result': kriged_matrix,
         'error': kriged_errors,
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate.egg-info/PKG-INFO` & `pyinterpolate-0.4/pyinterpolate.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: pyinterpolate
-Version: 0.3.7
+Version: 0.4
 Summary: Spatial Interpolation in Python
 Home-page: https://github.com/DataverseLabs/pyinterpolate
-Download-URL: https://github.com/DataverseLabs/pyinterpolate/archive/v0.3.tar.gz
+Download-URL: https://github.com/DataverseLabs/pyinterpolate/archive/
 Author: Szymon Moliński
 Author-email: simon@dataverselabs.com
 License: BSD 3-clause
 Project-URL: Documentation, https://readthedocs.org/projects/pyinterpolate/
 Project-URL: Source, https://github.com/DataverseLabs/pyinterpolate
 Project-URL: Tracker, https://github.com/DataverseLabs/pyinterpolate/issues
 Classifier: Development Status :: 4 - Beta
@@ -19,19 +19,19 @@
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown; charset=UTF-8
 
 ![status](https://joss.theoj.org/papers/3f87f562264c4e5174d9e6ed6d8812aa/status.svg) ![License](https://img.shields.io/github/license/szymon-datalions/pyinterpolate) ![Documentation Status](https://readthedocs.org/projects/pyinterpolate/badge/?version=latest) [![CodeFactor](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate/badge)](https://www.codefactor.io/repository/github/dataverselabs/pyinterpolate)
 
-![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov03.jpg?raw=true  "Pyinterpolate logo")
+![Pyinterpolate](https://github.com/DataverseLabs/pyinterpolate/blob/main/logov04.jpg?raw=true  "Pyinterpolate logo")
 
 # Pyinterpolate
 
-**version 0.3.7** - *Kyiv*
+**version 0.4** - *Kharkiv*
 
 ---
 
 Pyinterpolate is the Python library for **spatial statistics**. The package provides access to spatial statistics tools used in various studies. This package helps you **interpolate spatial data** with the *Kriging* technique.
 
 If you’re:
 
@@ -208,15 +208,15 @@
 * scipy
 * shapely
 * fiona
 * rtree
 * prettytable
 * pandas
 * dask
-* requests
+* dbscan
 
 You may check a specific version of requirements in the `setup.cfg` file.
 
 ## Package structure
 
 High level overview:
 
@@ -227,10 +227,14 @@
     - [x] `kriging` - Ordinary Kriging, Simple Kriging, Poisson Kriging: centroid based, area-to-area, area-to-point,
     - [x] `pipelines` - a complex functions to smooth a block data, download sample data, compare different kriging techniques, and filter blocks,
     - [x] `processing` - core data structures of the package: `Blocks` and `PointSupport`, and additional functions used for internal processes,
     - [x] `variogram` - experimental variogram, theoretical variogram, variogram point cloud, semivariogram regularization & deconvolution,
     - [x] `viz` - interpolation of smooth surfaces from points into rasters.
  - [x] `tutorials` - tutorials (Basic, Intermediate and Advanced).
 
+## Datasets
+
+Datasets and scripts to download spatial data from external API's are available in a dedicated package: **[pyinterpolate-datasets](https://pypi.org/project/pyinterpolate-datasets/2023.0.0/)**
+
 ## API documentation
 
 https://pyinterpolate.readthedocs.io/en/latest/
```

### Comparing `pyinterpolate-0.3.7/pyinterpolate.egg-info/SOURCES.txt` & `pyinterpolate-0.4/pyinterpolate.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -6,66 +6,74 @@
 pyinterpolate.egg-info/PKG-INFO
 pyinterpolate.egg-info/SOURCES.txt
 pyinterpolate.egg-info/dependency_links.txt
 pyinterpolate.egg-info/not-zip-safe
 pyinterpolate.egg-info/requires.txt
 pyinterpolate.egg-info/top_level.txt
 pyinterpolate/distance/__init__.py
+pyinterpolate/distance/clusters.py
 pyinterpolate/distance/distance.py
+pyinterpolate/distance/gridding.py
 pyinterpolate/idw/__init__.py
 pyinterpolate/idw/idw.py
 pyinterpolate/io/__init__.py
 pyinterpolate/io/read_data.py
 pyinterpolate/kriging/__init__.py
 pyinterpolate/kriging/point_kriging.py
 pyinterpolate/kriging/models/__init__.py
 pyinterpolate/kriging/models/block/__init__.py
 pyinterpolate/kriging/models/block/area_to_area_poisson_kriging.py
 pyinterpolate/kriging/models/block/area_to_point_poisson_kriging.py
 pyinterpolate/kriging/models/block/centroid_based_poisson_kriging.py
 pyinterpolate/kriging/models/block/weight.py
+pyinterpolate/kriging/models/indicator/__init__.py
+pyinterpolate/kriging/models/indicator/indicator_point_kriging.py
 pyinterpolate/kriging/models/point/__init__.py
 pyinterpolate/kriging/models/point/ordinary_kriging.py
 pyinterpolate/kriging/models/point/simple_kriging.py
 pyinterpolate/kriging/models/structures/__init__.py
 pyinterpolate/kriging/models/structures/point_kriging.py
 pyinterpolate/kriging/utils/__init__.py
 pyinterpolate/kriging/utils/kwarnings.py
 pyinterpolate/kriging/utils/process.py
 pyinterpolate/pipelines/__init__.py
 pyinterpolate/pipelines/block_filtering.py
 pyinterpolate/pipelines/deconvolution.py
 pyinterpolate/pipelines/multi_kriging.py
-pyinterpolate/pipelines/samples.py
 pyinterpolate/processing/__init__.py
 pyinterpolate/processing/checks.py
 pyinterpolate/processing/select_values.py
 pyinterpolate/processing/preprocessing/__init__.py
 pyinterpolate/processing/preprocessing/blocks.py
 pyinterpolate/processing/transform/__init__.py
 pyinterpolate/processing/transform/statistics.py
 pyinterpolate/processing/transform/transform.py
 pyinterpolate/processing/utils/__init__.py
 pyinterpolate/processing/utils/exceptions.py
+pyinterpolate/validation/__init__.py
+pyinterpolate/validation/cross_validation.py
 pyinterpolate/variogram/__init__.py
 pyinterpolate/variogram/empirical/__init__.py
 pyinterpolate/variogram/empirical/cloud.py
 pyinterpolate/variogram/empirical/covariance.py
 pyinterpolate/variogram/empirical/experimental_variogram.py
 pyinterpolate/variogram/empirical/semivariance.py
+pyinterpolate/variogram/indicator/__init__.py
+pyinterpolate/variogram/indicator/indicator_variogram.py
 pyinterpolate/variogram/regularization/__init__.py
 pyinterpolate/variogram/regularization/aggregated.py
 pyinterpolate/variogram/regularization/deconvolution.py
 pyinterpolate/variogram/regularization/block/__init__.py
 pyinterpolate/variogram/regularization/block/avg_block_to_block_semivariances.py
 pyinterpolate/variogram/regularization/block/avg_inblock_semivariances.py
 pyinterpolate/variogram/regularization/block/block_to_block_semivariance.py
 pyinterpolate/variogram/regularization/block/inblock_semivariance.py
 pyinterpolate/variogram/theoretical/__init__.py
 pyinterpolate/variogram/theoretical/semivariogram.py
+pyinterpolate/variogram/theoretical/spatial_dependency_index.py
 pyinterpolate/variogram/theoretical/models/__init__.py
 pyinterpolate/variogram/theoretical/models/variogram_models.py
 pyinterpolate/variogram/utils/__init__.py
 pyinterpolate/variogram/utils/exceptions.py
 pyinterpolate/variogram/utils/metrics.py
 pyinterpolate/variogram/utils/plots.py
 pyinterpolate/viz/__init__.py
```

### Comparing `pyinterpolate-0.3.7/setup.cfg` & `pyinterpolate-0.4/setup.cfg`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 [metadata]
 name = pyinterpolate
 description = Spatial Interpolation in Python
 long_description = file: README.md
 long_description_content_type = text/markdown; charset=UTF-8
-version = 0.3.7
+version = 0.4
 url = https://github.com/DataverseLabs/pyinterpolate
-download_url = https://github.com/DataverseLabs/pyinterpolate/archive/v0.3.tar.gz
+download_url = https://github.com/DataverseLabs/pyinterpolate/archive/
 author = Szymon Moliński
 author_email = simon@dataverselabs.com
 license = BSD 3-clause
 classifiers = 
 	Development Status :: 4 - Beta
 	Intended Audience :: Science/Research
 	Topic :: Scientific/Engineering :: GIS
@@ -25,40 +25,39 @@
 
 [options]
 zip_safe = False
 include_package_data = True
 packages = find:
 python_requires = >=3.7
 install_requires = 
-	tqdm==4.64.0; python_version<='3.9'
-	tqdm>=4.64; python_version>'3.9'
-	descartes==1.1.0
-	prettytable>=3.3.0
-	pandas>=1.4.3; python_version>='3.10'
-	pandas==1.4.3; python_version<='3.9'
-	pandas==1.3.5; python_version=='3.7'
+	dask==2022.2.1; python_version=='3.8' and sys_platform=='darwin'
+	dask==2023.3.2; python_version>='3.9' and sys_platform=='darwin'
+	dask==2023.3.2; python_version>='3.8' and sys_platform=='linux'
+	dask>=2023.3.2; python_version>='3.8' and sys_platform=='windows'
+	dask==2021.10.0; python_version=='3.7'
+	descartes
+	geopandas>=0.12.2; python_version>='3.8'
+	geopandas==0.10.2; python_version=='3.7'
+	hdbscan
+	matplotlib>=3.6
 	numpy>=1.23; python_version>='3.10'
-	numpy==1.23.0; python_version>='3.10' and sys_platform=='windows'
 	numpy==1.21.2; python_version<='3.9'
 	numpy==1.21.6; python_version=='3.7' and sys_platform=='linux'
 	numpy==1.21.5; python_version=='3.7' and sys_platform=='darwin'
+	pandas>=1.4.3; python_version>='3.9'
+	pandas==1.4.3; python_version=='3.8'
+	pandas==1.3.5; python_version=='3.7'
+	prettytable>=3.3.0
+	pyogrio
+	rtree>=1.0.0
+	shapely>=2.0.1
 	scipy>=1.9.0; python_version>='3.8'
 	scipy==1.7.3; python_version=='3.7'
-	matplotlib>=3.6
-	dask==2022.2.1; python_version=='3.8' and sys_platform=='darwin'
-	dask==2022.8.0; python_version>='3.9' and sys_platform=='darwin'
-	dask==2022.8.0; python_version>='3.8' and sys_platform=='linux'
-	dask>=2022.8.0; python_version>='3.8' and sys_platform=='windows'
-	dask==2021.10.0; python_version=='3.7'
-	requests
-	pyogrio
-	rtree==1.0.0
-	shapely<2
-	geopandas>=0.11.1; python_version>='3.8'
-	geopandas==0.10.2; python_version=='3.7'
+	tqdm>=4.64; python_version>'3.9'
+	tqdm==4.64.0; python_version<='3.9'
 
 [options.packages.find]
 exclude = 
 	tests*
 	tutorials*
 	new_concepts*
 	sample_data*
```

