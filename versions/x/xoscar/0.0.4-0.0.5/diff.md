# Comparing `tmp/xoscar-0.0.4.tar.gz` & `tmp/xoscar-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xoscar-0.0.4.tar", last modified: Tue Apr  4 09:02:30 2023, max compression
+gzip compressed data, was "xoscar-0.0.5.tar", last modified: Fri Apr  7 06:52:28 2023, max compression
```

## Comparing `xoscar-0.0.4.tar` & `xoscar-0.0.5.tar`

### file list

```diff
@@ -1,91 +1,91 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.863720 xoscar-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)      287 2023-04-04 09:02:00.000000 xoscar-0.0.4/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-04-04 09:02:30.863720 xoscar-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-04-04 09:02:00.000000 xoscar-0.0.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     2693 2023-04-04 09:02:30.863720 xoscar-0.0.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     4264 2023-04-04 09:02:00.000000 xoscar-0.0.4/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    83607 2023-04-04 09:02:00.000000 xoscar-0.0.4/versioneer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.855720 xoscar-0.0.4/xoscar/
--rw-r--r--   0 runner    (1001) docker     (123)     1647 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1157 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/_utils.pxd
--rw-r--r--   0 runner    (1001) docker     (123)     7059 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/_utils.pyx
--rw-r--r--   0 runner    (1001) docker     (123)    23719 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.855720 xoscar-0.0.4/xoscar/aio/
--rw-r--r--   0 runner    (1001) docker     (123)      809 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1313 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/_threads.py
--rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     6311 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/lru.py
--rw-r--r--   0 runner    (1001) docker     (123)     1293 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/aio/parallelism.py
--rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     1850 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backend.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/backends/
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/allocate_strategy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/backends/communication/
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7421 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     7796 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/dummy.py
--rw-r--r--   0 runner    (1001) docker     (123)      723 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)    11733 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/socket.py
--rw-r--r--   0 runner    (1001) docker     (123)    17844 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/ucx.py
--rw-r--r--   0 runner    (1001) docker     (123)     3625 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/communication/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4786 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9040 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     5700 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/core.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/backends/indigen/
--rw-r--r--   0 runner    (1001) docker     (123)      685 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/indigen/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2658 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/indigen/backend.py
--rw-r--r--   0 runner    (1001) docker     (123)      952 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/indigen/driver.py
--rw-r--r--   0 runner    (1001) docker     (123)    12089 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/indigen/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)    16411 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/message.pyx
--rw-r--r--   0 runner    (1001) docker     (123)    55798 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     4841 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/router.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/backends/test/
--rw-r--r--   0 runner    (1001) docker     (123)      682 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/test/backend.py
--rw-r--r--   0 runner    (1001) docker     (123)     4727 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/backends/test/pool.py
--rw-r--r--   0 runner    (1001) docker     (123)     7573 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/batch.py
--rw-r--r--   0 runner    (1001) docker     (123)      765 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/context.pxd
--rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/context.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/core.pxd
--rw-r--r--   0 runner    (1001) docker     (123)    18264 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/core.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     5069 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/debug.py
--rw-r--r--   0 runner    (1001) docker     (123)     1372 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/driver.py
--rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/entrypoints.py
--rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     1147 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/libcpp.pxd
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8854 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/metrics/backends/
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.859720 xoscar-0.0.4/xoscar/metrics/backends/console/
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/console/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2082 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/console/console_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     4446 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/metric.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.863720 xoscar-0.0.4/xoscar/metrics/backends/prometheus/
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/prometheus/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/metrics/backends/prometheus/prometheus_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    20412 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/nvutils.py
--rw-r--r--   0 runner    (1001) docker     (123)     8015 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/profiling.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.863720 xoscar-0.0.4/xoscar/serialization/
--rw-r--r--   0 runner    (1001) docker     (123)      860 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4577 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/aio.py
--rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/arrow.py
--rw-r--r--   0 runner    (1001) docker     (123)      985 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/core.pxd
--rw-r--r--   0 runner    (1001) docker     (123)    29468 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/core.pyx
--rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/cuda.py
--rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/exception.py
--rw-r--r--   0 runner    (1001) docker     (123)     2919 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/numpy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/serialization/scipy.py
--rw-r--r--   0 runner    (1001) docker     (123)    14479 2023-04-04 09:02:00.000000 xoscar-0.0.4/xoscar/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 09:02:30.855720 xoscar-0.0.4/xoscar.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-04-04 09:02:30.000000 xoscar-0.0.4/xoscar.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-04-04 09:02:30.000000 xoscar-0.0.4/xoscar.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 09:02:30.000000 xoscar-0.0.4/xoscar.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 09:02:29.000000 xoscar-0.0.4/xoscar.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      558 2023-04-04 09:02:30.000000 xoscar-0.0.4/xoscar.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-04 09:02:30.000000 xoscar-0.0.4/xoscar.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/
+-rw-r--r--   0 runner    (1001) docker     (123)      287 2023-04-07 06:52:02.000000 xoscar-0.0.5/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-04-07 06:52:28.594642 xoscar-0.0.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-04-07 06:52:02.000000 xoscar-0.0.5/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     2693 2023-04-07 06:52:28.598643 xoscar-0.0.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     4264 2023-04-07 06:52:02.000000 xoscar-0.0.5/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    83607 2023-04-07 06:52:02.000000 xoscar-0.0.5/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.590642 xoscar-0.0.5/xoscar/
+-rw-r--r--   0 runner    (1001) docker     (123)     1647 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1157 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/_utils.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)     7059 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/_utils.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)    23719 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.590642 xoscar-0.0.5/xoscar/aio/
+-rw-r--r--   0 runner    (1001) docker     (123)      809 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1313 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/_threads.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6311 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/lru.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1293 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/aio/parallelism.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4352 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1850 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backend.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.590642 xoscar-0.0.5/xoscar/backends/
+-rw-r--r--   0 runner    (1001) docker     (123)      643 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/allocate_strategy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/backends/communication/
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7421 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7796 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/dummy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      723 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11733 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/socket.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17844 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/ucx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3625 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/communication/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4786 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9040 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5700 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/core.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/backends/indigen/
+-rw-r--r--   0 runner    (1001) docker     (123)      685 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/indigen/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2658 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/indigen/backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)      952 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/indigen/driver.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12089 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/indigen/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16411 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/message.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)    55798 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4841 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/router.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/backends/test/
+-rw-r--r--   0 runner    (1001) docker     (123)      682 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/test/backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4727 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/backends/test/pool.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7573 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/context.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)     7506 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/context.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/core.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)    18264 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/core.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     5069 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1372 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/driver.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/entrypoints.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1147 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/libcpp.pxd
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8854 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/metrics/backends/
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/metrics/backends/console/
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/console/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2082 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/console/console_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4446 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/metric.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/metrics/backends/prometheus/
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/prometheus/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/metrics/backends/prometheus/prometheus_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20412 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/nvutils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8015 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/profiling.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.594642 xoscar-0.0.5/xoscar/serialization/
+-rw-r--r--   0 runner    (1001) docker     (123)      860 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4577 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/aio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/arrow.py
+-rw-r--r--   0 runner    (1001) docker     (123)      985 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/core.pxd
+-rw-r--r--   0 runner    (1001) docker     (123)    29468 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/core.pyx
+-rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/cuda.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/exception.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2919 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/numpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2482 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/serialization/scipy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14321 2023-04-07 06:52:02.000000 xoscar-0.0.5/xoscar/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:52:28.590642 xoscar-0.0.5/xoscar.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-04-07 06:52:28.000000 xoscar-0.0.5/xoscar.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2075 2023-04-07 06:52:28.000000 xoscar-0.0.5/xoscar.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:52:28.000000 xoscar-0.0.5/xoscar.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:52:27.000000 xoscar-0.0.5/xoscar.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      558 2023-04-07 06:52:28.000000 xoscar-0.0.5/xoscar.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 06:52:28.000000 xoscar-0.0.5/xoscar.egg-info/top_level.txt
```

### Comparing `xoscar-0.0.4/PKG-INFO` & `xoscar-0.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xoscar
-Version: 0.0.4
+Version: 0.0.5
 Summary: Python actor framework for heterogeneous computing.
 Home-page: http://github.com/xprobe-inc/xoscar
 Author: Qin Xuye
 Author-email: qinxuye@xprobe.io
 Maintainer: Qin Xuye
 Maintainer-email: qinxuye@xprobe.io
 License: Apache License 2.0
```

### Comparing `xoscar-0.0.4/pyproject.toml` & `xoscar-0.0.5/pyproject.toml`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/setup.cfg` & `xoscar-0.0.5/setup.cfg`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/setup.py` & `xoscar-0.0.5/setup.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/versioneer.py` & `xoscar-0.0.5/versioneer.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/__init__.py` & `xoscar-0.0.5/xoscar/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/_utils.pxd` & `xoscar-0.0.5/xoscar/_utils.pxd`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/_utils.pyx` & `xoscar-0.0.5/xoscar/_utils.pyx`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/_version.py` & `xoscar-0.0.5/xoscar/_version.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/__init__.py` & `xoscar-0.0.5/xoscar/aio/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/_threads.py` & `xoscar-0.0.5/xoscar/aio/_threads.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/base.py` & `xoscar-0.0.5/xoscar/aio/base.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/file.py` & `xoscar-0.0.5/xoscar/aio/file.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/lru.py` & `xoscar-0.0.5/xoscar/aio/lru.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/aio/parallelism.py` & `xoscar-0.0.5/xoscar/aio/parallelism.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/api.py` & `xoscar-0.0.5/xoscar/api.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backend.py` & `xoscar-0.0.5/xoscar/backend.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/__init__.py` & `xoscar-0.0.5/xoscar/backends/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/allocate_strategy.py` & `xoscar-0.0.5/xoscar/backends/allocate_strategy.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/__init__.py` & `xoscar-0.0.5/xoscar/backends/communication/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/base.py` & `xoscar-0.0.5/xoscar/backends/communication/base.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/core.py` & `xoscar-0.0.5/xoscar/backends/communication/core.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/dummy.py` & `xoscar-0.0.5/xoscar/backends/communication/dummy.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/errors.py` & `xoscar-0.0.5/xoscar/backends/communication/errors.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/socket.py` & `xoscar-0.0.5/xoscar/backends/communication/socket.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/ucx.py` & `xoscar-0.0.5/xoscar/backends/communication/ucx.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/communication/utils.py` & `xoscar-0.0.5/xoscar/backends/communication/utils.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/config.py` & `xoscar-0.0.5/xoscar/backends/config.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/context.py` & `xoscar-0.0.5/xoscar/backends/context.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/core.py` & `xoscar-0.0.5/xoscar/backends/core.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/indigen/__init__.py` & `xoscar-0.0.5/xoscar/backends/indigen/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/indigen/backend.py` & `xoscar-0.0.5/xoscar/backends/indigen/backend.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/indigen/driver.py` & `xoscar-0.0.5/xoscar/backends/indigen/driver.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/indigen/pool.py` & `xoscar-0.0.5/xoscar/backends/indigen/pool.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/message.pyx` & `xoscar-0.0.5/xoscar/backends/message.pyx`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/pool.py` & `xoscar-0.0.5/xoscar/backends/pool.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/router.py` & `xoscar-0.0.5/xoscar/backends/router.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/test/__init__.py` & `xoscar-0.0.5/xoscar/backends/test/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/test/backend.py` & `xoscar-0.0.5/xoscar/backends/test/backend.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/backends/test/pool.py` & `xoscar-0.0.5/xoscar/backends/test/pool.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/batch.py` & `xoscar-0.0.5/xoscar/batch.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/context.pxd` & `xoscar-0.0.5/xoscar/context.pxd`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/context.pyx` & `xoscar-0.0.5/xoscar/context.pyx`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/core.pxd` & `xoscar-0.0.5/xoscar/core.pxd`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/core.pyx` & `xoscar-0.0.5/xoscar/core.pyx`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/debug.py` & `xoscar-0.0.5/xoscar/debug.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/driver.py` & `xoscar-0.0.5/xoscar/driver.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/entrypoints.py` & `xoscar-0.0.5/xoscar/entrypoints.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/errors.py` & `xoscar-0.0.5/xoscar/errors.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/libcpp.pxd` & `xoscar-0.0.5/xoscar/libcpp.pxd`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/__init__.py` & `xoscar-0.0.5/xoscar/metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/api.py` & `xoscar-0.0.5/xoscar/metrics/api.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/__init__.py` & `xoscar-0.0.5/xoscar/metrics/backends/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/console/__init__.py` & `xoscar-0.0.5/xoscar/metrics/backends/console/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/console/console_metric.py` & `xoscar-0.0.5/xoscar/metrics/backends/console/console_metric.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/metric.py` & `xoscar-0.0.5/xoscar/metrics/backends/metric.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/prometheus/__init__.py` & `xoscar-0.0.5/xoscar/metrics/backends/prometheus/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/metrics/backends/prometheus/prometheus_metric.py` & `xoscar-0.0.5/xoscar/metrics/backends/prometheus/prometheus_metric.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/nvutils.py` & `xoscar-0.0.5/xoscar/nvutils.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/profiling.py` & `xoscar-0.0.5/xoscar/profiling.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/__init__.py` & `xoscar-0.0.5/xoscar/serialization/__init__.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/aio.py` & `xoscar-0.0.5/xoscar/serialization/aio.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/arrow.py` & `xoscar-0.0.5/xoscar/serialization/arrow.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/core.pxd` & `xoscar-0.0.5/xoscar/serialization/core.pxd`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/core.pyx` & `xoscar-0.0.5/xoscar/serialization/core.pyx`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/cuda.py` & `xoscar-0.0.5/xoscar/serialization/cuda.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/exception.py` & `xoscar-0.0.5/xoscar/serialization/exception.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/numpy.py` & `xoscar-0.0.5/xoscar/serialization/numpy.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/serialization/scipy.py` & `xoscar-0.0.5/xoscar/serialization/scipy.py`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar/utils.py` & `xoscar-0.0.5/xoscar/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,14 @@
 # limitations under the License.
 
 from __future__ import annotations
 
 import asyncio
 import dataclasses
 import functools
-import getpass
 import importlib
 import inspect
 import io
 import logging
 import os
 import pkgutil
 import random
@@ -443,15 +442,7 @@
                 except ex_type as e:
                     ex = e
                     time.sleep(wait_interval)
             assert ex is not None
             raise ex  # pylint: disable-msg=E0702
 
     return retry_call
-
-
-def get_current_user() -> str:
-    """
-    Get current login user.
-    Compatible for unix and windows.
-    """
-    return getpass.getuser()
```

### Comparing `xoscar-0.0.4/xoscar.egg-info/PKG-INFO` & `xoscar-0.0.5/xoscar.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xoscar
-Version: 0.0.4
+Version: 0.0.5
 Summary: Python actor framework for heterogeneous computing.
 Home-page: http://github.com/xprobe-inc/xoscar
 Author: Qin Xuye
 Author-email: qinxuye@xprobe.io
 Maintainer: Qin Xuye
 Maintainer-email: qinxuye@xprobe.io
 License: Apache License 2.0
```

### Comparing `xoscar-0.0.4/xoscar.egg-info/SOURCES.txt` & `xoscar-0.0.5/xoscar.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `xoscar-0.0.4/xoscar.egg-info/requires.txt` & `xoscar-0.0.5/xoscar.egg-info/requires.txt`

 * *Files identical despite different names*

