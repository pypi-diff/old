# Comparing `tmp/hmfs-1.1.5131.tar.gz` & `tmp/hmfs-1.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hmfs-1.1.5131.tar", last modified: Fri Apr  7 03:48:55 2023, max compression
+gzip compressed data, was "dist/hmfs-1.1.6.tar", last modified: Wed Aug 24 12:07:38 2022, max compression
```

## Comparing `hmfs-1.1.5131.tar` & `hmfs-1.1.6.tar`

### file list

```diff
@@ -1,35 +1,1134 @@
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      330 2023-04-07 03:48:55.000000 hmfs-1.1.5131/PKG-INFO
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hamunafs/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        0 2022-10-12 00:41:11.000000 hmfs-1.1.5131/hamunafs/__init__.py
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hamunafs/backends/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      203 2022-08-24 10:45:13.000000 hmfs-1.1.5131/hamunafs/backends/__init__.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      917 2023-02-27 06:26:04.000000 hmfs-1.1.5131/hamunafs/backends/base.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4030 2023-02-27 06:27:51.000000 hmfs-1.1.5131/hamunafs/backends/bk_minio.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4362 2023-02-27 06:27:39.000000 hmfs-1.1.5131/hamunafs/backends/bk_qiniu.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1233 2023-04-07 02:55:40.000000 hmfs-1.1.5131/hamunafs/backends/bk_share.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5747 2023-02-27 06:28:08.000000 hmfs-1.1.5131/hamunafs/backends/bk_wy.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      937 2023-01-31 04:14:05.000000 hmfs-1.1.5131/hamunafs/backends/fetcher.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20512 2023-04-07 03:48:42.000000 hmfs-1.1.5131/hamunafs/client.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      189 2021-11-18 09:55:13.000000 hmfs-1.1.5131/hamunafs/conf.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9389 2023-03-23 03:02:23.000000 hmfs-1.1.5131/hamunafs/server.py
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hamunafs/sqlite/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4895 2021-11-17 08:14:48.000000 hmfs-1.1.5131/hamunafs/sqlite/__init__.py
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hamunafs/utils/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        0 2022-10-12 00:41:11.000000 hmfs-1.1.5131/hamunafs/utils/__init__.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5300 2022-05-20 12:24:19.000000 hmfs-1.1.5131/hamunafs/utils/cachemanager.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4578 2022-10-20 11:01:55.000000 hmfs-1.1.5131/hamunafs/utils/img_compressor.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6528 2022-08-24 11:14:39.000000 hmfs-1.1.5131/hamunafs/utils/minio.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3579 2022-08-24 10:04:27.000000 hmfs-1.1.5131/hamunafs/utils/mqtt.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5226 2023-02-03 04:48:33.000000 hmfs-1.1.5131/hamunafs/utils/nsqmanager.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17182 2023-01-04 13:01:16.000000 hmfs-1.1.5131/hamunafs/utils/redisutil.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      633 2023-01-28 07:26:26.000000 hmfs-1.1.5131/hamunafs/utils/singleton_wrapper.py
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      932 2022-09-03 07:57:02.000000 hmfs-1.1.5131/hamunafs/utils/timeutil.py
-drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      330 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/PKG-INFO
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      753 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/SOURCES.txt
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        1 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/dependency_links.txt
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      146 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/requires.txt
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        9 2023-04-07 03:48:55.000000 hmfs-1.1.5131/hmfs.egg-info/top_level.txt
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)       38 2023-04-07 03:48:55.000000 hmfs-1.1.5131/setup.cfg
--rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      731 2023-04-07 03:48:47.000000 hmfs-1.1.5131/setup.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1209 2022-02-26 02:33:18.000000 hmfs-1.1.6/.qiniu_pythonsdk_hostscache.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      346 2022-08-24 12:07:38.000000 hmfs-1.1.6/PKG-INFO
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      104 2022-01-19 10:09:23.000000 hmfs-1.1.6/build.sh
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)       85 2021-11-07 15:08:42.000000 hmfs-1.1.6/commit.sh
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        2 2022-07-22 08:04:53.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/@plugins_snapshot.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7276 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/__future__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1514 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/__future__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   103046 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_ast.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1528 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_ast.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6609 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_bisect.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1526 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_bisect.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16413 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_csv.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1487 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_csv.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10952 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_dummy_thread.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_dummy_thread.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8446 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_imp.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1519 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_imp.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13536 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_importlib_modulespec.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1524 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_importlib_modulespec.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4774 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_markupbase.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1488 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_markupbase.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1432 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1506 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5150 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_argcomplete.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1619 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_argcomplete.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2334 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1550 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   147562 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/code.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1983 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/code.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16584 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/source.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1683 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_code/source.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1611 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1524 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9624 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/saferepr.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1532 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/saferepr.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14423 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/terminalwriter.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1750 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/terminalwriter.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2490 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/wcwidth.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1537 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_io/wcwidth.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1670 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_version.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1489 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/_version.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11071 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1830 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    53249 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/rewrite.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2252 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/rewrite.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5728 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/truncate.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1590 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/truncate.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19897 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/util.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1757 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/assertion/util.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    42263 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/cacheprovider.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2190 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/cacheprovider.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   104382 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/capture.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1886 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/capture.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    35136 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/compat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1832 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/compat.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    92672 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2733 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    37026 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/argparsing.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1852 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/argparsing.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2542 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1559 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8132 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/findpaths.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1687 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/config/findpaths.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    28384 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/debugging.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2046 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/debugging.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4624 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/deprecated.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1565 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/deprecated.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   150467 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/fixtures.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2357 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/fixtures.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2722 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/freeze_support.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1615 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/freeze_support.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8095 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/helpconfig.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1687 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/helpconfig.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    53725 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/hookspec.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2007 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/hookspec.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    67860 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/logging.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2097 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/logging.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    44210 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/main.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2169 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/main.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    31129 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2122 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    29093 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/expression.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1620 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/expression.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   119483 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/structures.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1983 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/mark/structures.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    23394 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/monkeypatch.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1812 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/monkeypatch.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    46495 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/nodes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2017 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/nodes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25411 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/outcomes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1650 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/outcomes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27228 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pathlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2021 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pathlib.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   156723 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pytester.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2572 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pytester.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3866 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pytester_assertions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1537 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/pytester_assertions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    91593 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/python.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2333 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/python.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    42476 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/python_api.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1992 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/python_api.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27877 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/recwarn.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1711 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/recwarn.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    42487 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/reports.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1922 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/reports.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    41150 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/runner.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2049 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/runner.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12314 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/store.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1483 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/store.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    87981 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/terminal.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2268 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/terminal.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1630 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/timing.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1499 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/timing.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    29774 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/tmpdir.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1860 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/tmpdir.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24080 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/warning_types.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1589 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/warning_types.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11481 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/warnings.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1842 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_pytest/warnings.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5473 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_random.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_random.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11161 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_thread.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1543 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_thread.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3053 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_types.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1496 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_types.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13290 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_warnings.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1497 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_warnings.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    23705 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_weakref.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1536 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_weakref.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    43058 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_weakrefset.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1515 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/_weakrefset.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16916 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/abc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1490 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/abc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   139174 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/argparse.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1510 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/argparse.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    52126 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/array.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1530 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/array.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    95026 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ast.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1543 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ast.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/async_timeout/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13382 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/async_timeout/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1719 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/async_timeout/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10443 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1865 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    84309 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/base_events.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1785 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/base_events.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7055 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/coroutines.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/coroutines.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   164618 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/events.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1785 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/events.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25161 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/futures.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1631 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/futures.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    31007 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/locks.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1604 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/locks.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14274 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/protocols.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1575 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/protocols.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21034 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/queues.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1545 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/queues.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2656 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/runners.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1522 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/runners.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2860 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/selector_events.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1562 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/selector_events.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    38168 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/streams.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1671 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/streams.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24280 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/subprocess.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1722 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/subprocess.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    98509 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/tasks.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1686 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/tasks.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25040 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/transports.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/transports.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17457 2022-06-21 17:17:28.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/unix_events.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1688 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/asyncio/unix_events.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5458 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/atexit.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/atexit.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   258177 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1648 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6213 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/_version_info.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1463 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/_version_info.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7835 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/converters.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1487 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/converters.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9245 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1487 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3251 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/filters.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1481 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/filters.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7379 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/setters.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1481 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/setters.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    39809 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/validators.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1489 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/attr/validators.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13402 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/base64.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/base64.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    46749 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/bdb.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1506 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/bdb.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11334 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/binascii.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1510 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/binascii.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3521 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/bisect.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1507 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/bisect.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    64151 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1539 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2828 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/compat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1593 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/compat.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    54750 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1572 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    63311 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/exception.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1539 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/exception.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7011 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/regioninfo.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/regioninfo.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4959 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1576 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    71723 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/bucket.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1630 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/bucket.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19512 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/bucketlistresultset.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1575 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/bucketlistresultset.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    38765 2021-11-29 11:37:03.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1599 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    64764 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/key.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1512 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/boto/s3/key.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   831058 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/builtins.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1656 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/builtins.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1458 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/certifi.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1472 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/certifi.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    35368 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/cgi.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1543 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/cgi.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18775 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/cmd.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1491 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/cmd.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   115804 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/codecs.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1567 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/codecs.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/collections/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   247997 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/collections/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1597 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/collections/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3612 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/collections/abc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/collections/abc.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1264 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1475 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2860 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1645 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    61498 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1621 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    47736 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/process.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1833 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/process.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20437 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/thread.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1654 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/concurrent/futures/thread.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   111627 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/configparser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1588 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/configparser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    60679 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/contextlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1575 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/contextlib.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27006 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/contextvars.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1515 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/contextvars.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4885 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/copy.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1478 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/copy.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    28655 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/csv.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1562 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/csv.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ctypes/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   113173 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ctypes/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1534 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ctypes/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   113830 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/datetime.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1551 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/datetime.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   156060 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/decimal.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1527 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/decimal.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    47155 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/difflib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1507 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/difflib.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/distutils/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1013 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/distutils/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1479 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/distutils/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8619 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/distutils/util.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1498 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/distutils/util.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    72970 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/doctest.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1548 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/doctest.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5602 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1528 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11881 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/charset.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/charset.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7416 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/contentmanager.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1527 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/contentmanager.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21850 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/errors.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1518 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/errors.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8560 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/header.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1511 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/header.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    53273 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/message.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1602 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/message.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1015 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1477 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3948 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1586 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4632 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/multipart.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1604 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/multipart.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1948 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/nonmultipart.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1521 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/nonmultipart.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3164 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/text.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1579 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/mime/text.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26104 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/policy.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1599 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/email/policy.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    41375 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/enum.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1516 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/enum.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25508 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/errno.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1489 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/errno.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5305 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/fnmatch.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1480 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/fnmatch.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    74824 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/functools.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1573 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/functools.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12958 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/gc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1497 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/gc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16310 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/genericpath.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1546 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/genericpath.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2911 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/getpass.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1478 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/getpass.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    32259 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/gettext.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1566 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/gettext.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7932 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/glob.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1519 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/glob.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2230 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1650 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4648 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1463 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6684 2021-11-29 11:38:15.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/qiniu.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1732 2021-11-29 11:38:15.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/qiniu.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6537 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/yaocdn.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1804 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/backends/yaocdn.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1536 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/conf.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1476 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/conf.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1937 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1767 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12149 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/cachemanager.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1672 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/cachemanager.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9031 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/minio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1794 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/minio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7644 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/mqtt.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1731 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/mqtt.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8534 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/nsqmanager.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1712 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/nsqmanager.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    31073 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/redisutil.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1677 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/redisutil.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3291 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/singleton_wrapper.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1514 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hamunafs/utils/singleton_wrapper.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24319 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hashlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1574 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/hashlib.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3419 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1481 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2267 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/entities.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1506 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/entities.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12749 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/parser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1510 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/html/parser.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18540 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1552 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    64931 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/client.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1633 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/client.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    56922 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/cookiejar.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1585 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/cookiejar.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    28591 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/cookies.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1517 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/cookies.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    36860 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/server.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1610 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/http/server.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6661 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1756 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2611 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1837 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13158 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1552 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19267 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2094 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27651 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/connection_pool.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1945 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/connection_pool.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5939 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1586 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    30326 2022-06-21 17:17:33.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http11.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1915 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http11.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    37459 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http2.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2081 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http2.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    34596 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http_proxy.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2105 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_async/http_proxy.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1040 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1469 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26820 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/anyio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1685 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/anyio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26549 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/asyncio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2031 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/asyncio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9446 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/auto.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1733 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/auto.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20820 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1770 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26381 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/curio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1740 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/curio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20617 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/sync.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1692 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/sync.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25225 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/trio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1640 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_backends/trio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13726 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_bytestreams.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1609 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_bytestreams.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13937 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1545 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_exceptions.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2526 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1828 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11685 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1550 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17451 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2028 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24660 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/connection_pool.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2033 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/connection_pool.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5627 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1583 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26736 2022-06-21 17:17:33.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http11.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1912 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http11.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    32681 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http2.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2042 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http2.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    32783 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http_proxy.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2037 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_sync/http_proxy.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6246 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_threadlock.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1531 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_threadlock.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4044 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_types.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1486 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_types.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1958 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1590 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpcore/_utils.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9367 2022-06-21 17:17:33.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2048 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1709 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/__version__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1491 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/__version__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    68899 2022-06-21 17:17:33.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_api.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1817 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_api.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    37768 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_auth.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1855 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_auth.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   216833 2022-06-21 17:17:33.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_client.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2313 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_client.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25830 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_config.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1732 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_config.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25024 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_content.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1775 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_content.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    54491 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_content_streams.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1833 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_content_streams.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    29120 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_decoders.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1706 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_decoders.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    33731 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1540 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   149885 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_models.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2276 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_models.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20911 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_multipart.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1672 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_multipart.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    62309 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_status_codes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1558 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_status_codes.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1292 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1467 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10389 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/asgi.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1852 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/asgi.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12073 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/urllib3.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1864 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/urllib3.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10611 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/wsgi.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1750 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_transports/wsgi.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20771 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_types.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1612 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_types.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    34475 2022-06-21 17:17:32.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1924 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/httpx/_utils.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17789 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/imp.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1544 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/imp.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5289 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1529 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    41981 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/abc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1626 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/abc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    59102 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/machinery.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1577 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/machinery.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17716 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/util.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1627 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib/util.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    78245 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2225 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5118 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_adapters.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1655 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_adapters.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    22319 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_collections.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1541 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_collections.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5049 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_compat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1570 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_compat.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1762 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_functools.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1552 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_functools.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1746 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_itertools.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1563 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_itertools.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11045 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_meta.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1541 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_meta.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4703 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_text.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1573 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/importlib_metadata/_text.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/iniconfig/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15590 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/iniconfig/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1512 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/iniconfig/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   279358 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/inspect.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1632 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/inspect.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    79830 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/io.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1561 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/io.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   158182 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/itertools.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1558 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/itertools.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14873 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1545 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13729 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/decoder.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/decoder.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9186 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/encoder.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1502 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/json/encoder.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/logging/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   135631 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/logging/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1666 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/logging/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4110 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/marshal.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1478 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/marshal.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27131 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/math.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1547 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/math.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14388 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/mimetypes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1530 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/mimetypes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21573 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/mmap.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/mmap.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    39652 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1968 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27507 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1597 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    86975 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/context.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1825 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/context.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    51130 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/managers.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1666 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/managers.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    45761 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/pool.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1552 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/pool.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15587 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/process.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1539 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/process.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19411 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/queues.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1553 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/queues.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8643 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/spawn.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1535 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/spawn.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21937 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/synchronize.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1600 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/multiprocessing/synchronize.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6948 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/netrc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1507 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/netrc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    72732 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numbers.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numbers.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)  1774653 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2975 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3370 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/_pytesttester.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1982 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/_pytesttester.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1509 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/_version.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1523 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/_version.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14243 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/char.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1493 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/char.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4703 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1550 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5171 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/_inspect.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1516 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/_inspect.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10478 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/py3k.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1712 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/compat/py3k.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      992 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1456 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    23102 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_asarray.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1575 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_asarray.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20610 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_internal.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1516 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_internal.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6621 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_type_aliases.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1561 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_type_aliases.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16658 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_ufunc_config.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1547 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/_ufunc_config.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    66561 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/arrayprint.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1615 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/arrayprint.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   165010 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/einsumfunc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1580 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/einsumfunc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    95980 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/fromnumeric.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1601 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/fromnumeric.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14111 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/function_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1585 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/function_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19671 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/multiarray.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1631 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/multiarray.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    66029 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/numeric.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1575 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/numeric.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    30443 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/numerictypes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1620 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/numerictypes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25170 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/overrides.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1702 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/overrides.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21674 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/shape_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1579 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/shape_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2779 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/umath.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1547 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/core/umath.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3418 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ctypeslib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ctypeslib.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/distutils/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1742 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/distutils/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1482 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/distutils/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    52454 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/distutils/cpuinfo.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1678 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/distutils/cpuinfo.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/fft/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6122 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/fft/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1484 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/fft/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24643 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2127 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8535 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/_version.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1493 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/_version.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1808 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arraypad.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arraypad.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3829 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arraysetops.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1499 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arraysetops.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24947 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arrayterator.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1555 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/arrayterator.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6959 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/format.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1530 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/format.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13098 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/function_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1612 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/function_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    72521 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/index_tricks.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1583 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/index_tricks.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16820 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/mixins.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1489 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/mixins.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5667 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/nanfunctions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1502 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/nanfunctions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12370 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/npyio.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1534 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/npyio.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4316 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/polynomial.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1512 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/polynomial.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3631 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/scimath.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1491 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/scimath.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6903 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/shape_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1607 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/shape_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5491 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/stride_tricks.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1525 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/stride_tricks.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10856 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/twodim_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1536 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/twodim_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4623 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/type_check.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1497 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/type_check.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24240 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/ufunclike.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1533 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/ufunclike.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24974 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1593 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/lib/utils.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/linalg/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7163 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/linalg/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1490 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/linalg/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    28925 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1531 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   129551 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/core.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1534 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/core.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21534 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/extras.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1563 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/ma/extras.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/matrixlib/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2969 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/matrixlib/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1511 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/matrixlib/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3385 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1711 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    23067 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/_polybase.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1510 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/_polybase.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15635 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/chebyshev.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1597 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/chebyshev.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13520 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/hermite.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1593 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/hermite.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13571 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/hermite_e.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1597 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/hermite_e.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13347 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/laguerre.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1595 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/laguerre.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13347 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/legendre.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1595 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/legendre.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12548 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/polynomial.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1599 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/polynomial.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3921 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/polyutils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1509 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/polynomial/polyutils.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9313 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1712 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   378941 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_generator.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1608 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_generator.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12515 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_mt19937.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1614 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_mt19937.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17283 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_pcg64.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_pcg64.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16533 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_philox.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1613 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_philox.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11234 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_sfc64.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1610 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/_sfc64.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    70411 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/bit_generator.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1610 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/bit_generator.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   529009 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/mtrand.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1684 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/random/mtrand.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3554 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/rec.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1490 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/rec.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/testing/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18904 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/testing/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/testing/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    23557 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1882 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3240 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_add_docstring.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1631 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_add_docstring.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18824 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_array_like.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1618 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_array_like.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   232581 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_callable.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1740 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_callable.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    45355 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_char_codes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1546 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_char_codes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    29968 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_dtype_like.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1629 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_dtype_like.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5850 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_extended_precision.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1560 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_extended_precision.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25161 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_generic_alias.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1613 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_generic_alias.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4336 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_nbit.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_nbit.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5946 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_scalars.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1500 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_scalars.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2675 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_shape.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1535 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_shape.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   266830 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_ufunc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1697 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/typing/_ufunc.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2574 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/version.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1507 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/numpy/version.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   141852 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/operator.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1523 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/operator.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6967 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/orjson.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1497 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/orjson.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/os/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   234501 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/os/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1641 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/os/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4687 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/os/path.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1525 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/os/path.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3404 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/__about__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1515 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/__about__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2592 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1533 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6207 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_compat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1554 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_compat.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13910 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_structures.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_structures.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1574 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_typing.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1492 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/_typing.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    31061 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/markers.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1743 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/markers.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    22151 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/requirements.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1729 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/requirements.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    70681 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/specifiers.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1738 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/specifiers.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    61557 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/tags.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1944 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/tags.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4831 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1591 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/utils.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    82421 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/version.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1683 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/packaging/version.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    68873 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pathlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1597 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pathlib.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    84996 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pdb.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1581 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pdb.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    39152 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pickle.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1532 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pickle.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pkg_resources/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   128805 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pkg_resources/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1601 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pkg_resources/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    26935 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pkgutil.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1536 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pkgutil.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    34360 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/platform.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1522 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/platform.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    85632 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/posix.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1561 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/posix.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    67150 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/posixpath.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1565 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/posixpath.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9926 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pprint.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1511 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pprint.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3494 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1563 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    82006 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/error.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1460 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/error.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15773 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/iniconfig.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1509 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/iniconfig.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    44555 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/io.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1521 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/io.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    70339 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/path.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1526 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/path.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11101 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/xml.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1496 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/py/xml.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    95680 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pydoc.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1541 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pydoc.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pytest/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8319 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pytest/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2033 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pytest/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4905 2021-11-29 11:38:14.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pytest/collect.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1679 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/pytest/collect.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25079 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/queue.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1522 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/queue.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    37779 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/random.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1567 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/random.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    83149 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/re.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1535 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/re.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6883 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1608 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   111051 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/client.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1559 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/client.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    48234 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1508 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11264 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1491 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2445 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1497 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/redis/utils.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15905 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/reprlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1515 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/reprlib.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6155 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1682 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    24684 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/adapters.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2085 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/adapters.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10693 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/api.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1566 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/api.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14776 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/auth.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1657 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/auth.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1792 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/compat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1541 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/compat.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18393 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/cookies.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1628 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/cookies.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15989 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1560 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1921 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/hooks.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/hooks.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    59308 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/models.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2083 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/models.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2886 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1502 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10190 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2030 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19996 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/_collections.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1573 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/_collections.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    22063 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1991 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    30180 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/connectionpool.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2188 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/connectionpool.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    28794 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/exceptions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1548 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/exceptions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6088 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/fields.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1620 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/fields.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3203 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/filepost.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1667 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/filepost.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1168 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1534 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/ssl_match_hostname/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2326 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/ssl_match_hostname/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1618 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/packages/ssl_match_hostname/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9677 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/poolmanager.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1593 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/poolmanager.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4415 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/request.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1541 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/request.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19288 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/response.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1840 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/response.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11939 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1880 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2730 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/connection.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1557 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/connection.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1980 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/request.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1551 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/request.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1442 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/response.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1536 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/response.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11996 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/retry.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1676 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/retry.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5519 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/ssl_.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1642 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/ssl_.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7894 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/timeout.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1634 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/timeout.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7401 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/url.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1626 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/packages/urllib3/util/url.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    43337 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/sessions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2044 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/sessions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1628 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/status_codes.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1545 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/status_codes.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    17540 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/structures.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1513 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/structures.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14009 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/utils.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1712 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/requests/utils.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21227 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/select.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1539 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/select.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    67183 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/selectors.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1557 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/selectors.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13837 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/shlex.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/shlex.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    44658 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/shutil.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1537 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/shutil.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    45658 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/signal.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1534 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/signal.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    49997 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1613 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/__init__.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1687 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/BaseHTTPServer.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1523 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/BaseHTTPServer.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1681 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/CGIHTTPServer.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1521 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/CGIHTTPServer.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1699 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/SimpleHTTPServer.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1527 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/SimpleHTTPServer.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6816 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2703 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2007 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/_dummy_thread.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1523 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/_dummy_thread.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1917 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/_thread.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/_thread.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    15350 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/builtins.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1490 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/builtins.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8025 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/cPickle.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1504 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/cPickle.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3629 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/configparser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/configparser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1201 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_base.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1529 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_base.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1246 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_multipart.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1544 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_multipart.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1273 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_nonmultipart.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1553 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_nonmultipart.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1201 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_text.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1529 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/email_mime_text.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1503 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/html_entities.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1523 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/html_entities.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1177 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/html_parser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1517 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/html_parser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9327 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_client.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1517 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_client.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1951 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_cookiejar.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1526 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_cookiejar.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1485 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_cookies.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/http_cookies.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1579 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/queue.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1499 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/queue.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1411 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/reprlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/reprlib.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2915 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/socketserver.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/socketserver.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13379 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1505 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1232 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_commondialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1544 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_commondialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8523 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_constants.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1535 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_constants.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1295 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_dialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1526 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_dialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2762 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_filedialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1538 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_filedialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2774 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_tkfiledialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1542 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_tkfiledialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3609 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_ttk.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1517 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/tkinter_ttk.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1553 2021-11-29 11:37:02.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1706 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1400 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/error.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1521 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/error.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3200 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/parse.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1522 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/parse.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4949 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/request.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1528 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/request.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1205 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/response.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1530 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/response.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1236 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/robotparser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1538 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib/robotparser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1400 2021-11-29 11:37:01.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_error.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_error.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4086 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_parse.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_parse.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1236 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_robotparser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1538 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/six/moves/urllib_robotparser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    90911 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/socket.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1621 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/socket.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    62151 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/socketserver.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1586 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/socketserver.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   169557 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ssl.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/ssl.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20616 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/stat.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1502 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/stat.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16626 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/string.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1532 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/string.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    12517 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/struct.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1524 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/struct.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   140677 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/subprocess.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1588 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/subprocess.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    63496 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/sys.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1612 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/sys.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11894 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/sysconfig.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1488 2021-11-29 11:02:36.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/sysconfig.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   114619 2022-06-21 17:17:18.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tempfile.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1584 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tempfile.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    18675 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/textwrap.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1495 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/textwrap.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    53931 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/threading.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1526 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/threading.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    50442 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/time.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1543 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/time.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   261945 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1561 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4741 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/commondialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1520 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/commondialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21223 2021-11-29 11:36:58.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/constants.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1500 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/constants.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4442 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/dialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1525 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/dialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    27642 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/filedialog.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1565 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/filedialog.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    79317 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/ttk.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1535 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tkinter/ttk.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    13854 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/token.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1509 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/token.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    48728 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tokenize.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1539 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/tokenize.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8363 2021-11-29 11:36:59.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/toml.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1561 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/toml.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    34290 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/traceback.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1545 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/traceback.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   127449 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/types.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1604 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/types.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   409216 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/typing.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1553 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/typing.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    36387 2022-06-21 17:17:17.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/typing_extensions.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1527 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/typing_extensions.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20329 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unicodedata.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1515 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unicodedata.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7604 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1687 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1732 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/async_case.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1555 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/async_case.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   132789 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/case.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1638 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/case.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9265 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/loader.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1620 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/loader.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    19677 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/result.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1569 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/result.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11469 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/runner.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1605 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/runner.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9940 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/signals.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1543 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/signals.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     9168 2021-11-29 11:37:00.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/suite.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1577 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/unittest/suite.meta.json
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1236 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/__init__.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1467 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/__init__.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     7261 2022-06-21 17:17:24.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/error.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1566 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/error.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   123974 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/parse.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1517 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/parse.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)   141119 2022-06-21 17:17:26.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/request.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1685 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/request.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    25277 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/response.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1596 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/response.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    20842 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/robotparser.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1530 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/urllib/robotparser.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    31879 2022-06-21 17:17:23.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/uuid.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1564 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/uuid.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    21560 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/warnings.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1556 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/warnings.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    81071 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/weakref.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1532 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/weakref.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11033 2021-11-29 11:36:57.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/zipimport.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1568 2022-01-16 01:34:45.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/zipimport.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    14389 2022-06-21 17:17:22.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/zlib.data.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1502 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/.mypy_cache/3.7/zlib.meta.json
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)       26 2021-11-07 08:18:04.000000 hmfs-1.1.6/hamunafs/__init__.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/__pycache__/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      186 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/__pycache__/__init__.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      203 2022-02-26 02:33:18.000000 hmfs-1.1.6/hamunafs/__pycache__/__init__.cpython-38.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    11667 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/__pycache__/client.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    10138 2022-02-26 02:33:18.000000 hmfs-1.1.6/hamunafs/__pycache__/client.cpython-38.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      312 2022-08-24 10:24:04.000000 hmfs-1.1.6/hamunafs/__pycache__/conf.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5775 2022-08-24 10:52:11.000000 hmfs-1.1.6/hamunafs/__pycache__/server.cpython-37.pyc
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/backends/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      203 2022-08-24 10:45:13.000000 hmfs-1.1.6/hamunafs/backends/__init__.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      372 2022-08-24 10:51:58.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/__init__.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1396 2022-08-24 10:10:13.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/base.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3902 2022-08-24 10:10:13.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/bk_qiniu.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     2511 2022-01-16 01:34:46.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/qiniu.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3821 2021-11-29 12:05:04.000000 hmfs-1.1.6/hamunafs/backends/__pycache__/yaocdn.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      598 2022-01-16 11:30:53.000000 hmfs-1.1.6/hamunafs/backends/base.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3097 2022-08-24 11:41:08.000000 hmfs-1.1.6/hamunafs/backends/bk_minio.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4300 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/backends/bk_qiniu.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4482 2022-08-24 11:19:59.000000 hmfs-1.1.6/hamunafs/backends/bk_wy.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16741 2022-08-24 12:05:45.000000 hmfs-1.1.6/hamunafs/client.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      189 2021-11-18 09:55:13.000000 hmfs-1.1.6/hamunafs/conf.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     8837 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/server.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/sqlite/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4895 2021-11-17 08:14:48.000000 hmfs-1.1.6/hamunafs/sqlite/__init__.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/sqlite/__pycache__/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     4806 2022-05-21 02:19:54.000000 hmfs-1.1.6/hamunafs/sqlite/__pycache__/__init__.cpython-37.pyc
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/utils/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      202 2021-11-07 14:48:12.000000 hmfs-1.1.6/hamunafs/utils/__init__.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      418 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/__init__.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6103 2022-08-24 10:10:13.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/cachemanager.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5666 2022-08-24 11:18:44.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/minio.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3830 2022-08-24 10:10:12.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/mqtt.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3023 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/nsqmanager.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16971 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/redisutil.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      852 2022-08-24 10:10:11.000000 hmfs-1.1.6/hamunafs/utils/__pycache__/singleton_wrapper.cpython-37.pyc
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     5300 2022-05-20 12:24:19.000000 hmfs-1.1.6/hamunafs/utils/cachemanager.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     6528 2022-08-24 11:14:39.000000 hmfs-1.1.6/hamunafs/utils/minio.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3579 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/utils/mqtt.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     3560 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/utils/nsqmanager.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    16353 2022-08-24 10:04:27.000000 hmfs-1.1.6/hamunafs/utils/redisutil.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      407 2022-08-02 01:13:40.000000 hmfs-1.1.6/hamunafs/utils/singleton_wrapper.py
+drwxrwxr-x   0 superpigy  (1000) superpigy  (1000)        0 2022-08-24 12:07:38.000000 hmfs-1.1.6/hmfs.egg-info/
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      346 2022-08-24 12:07:37.000000 hmfs-1.1.6/hmfs.egg-info/PKG-INFO
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)    55674 2022-08-24 12:07:37.000000 hmfs-1.1.6/hmfs.egg-info/SOURCES.txt
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        1 2022-08-24 12:07:37.000000 hmfs-1.1.6/hmfs.egg-info/dependency_links.txt
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      118 2022-08-24 12:07:37.000000 hmfs-1.1.6/hmfs.egg-info/requires.txt
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)        9 2022-08-24 12:07:37.000000 hmfs-1.1.6/hmfs.egg-info/top_level.txt
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)       38 2022-08-24 12:07:38.000000 hmfs-1.1.6/setup.cfg
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)      694 2022-08-24 12:06:08.000000 hmfs-1.1.6/setup.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)       39 2021-11-17 08:14:48.000000 hmfs-1.1.6/start.py
+-rw-rw-r--   0 superpigy  (1000) superpigy  (1000)     1301 2022-08-24 11:51:13.000000 hmfs-1.1.6/test.py
```

### Comparing `hmfs-1.1.5131/hamunafs/backends/bk_minio.py` & `hmfs-1.1.6/hamunafs/backends/bk_minio.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,9 +1,10 @@
-import os
 import traceback
+import numpy as np
+import httpx
 from aiohttp_retry import ExponentialRetry, RetryClient
 
 from hamunafs.utils.minio import MinioAgent
 
 from hamunafs.backends.base import BackendBase
 from aiofile import AIOFile, Writer, async_open
 
@@ -12,32 +13,33 @@
         key, secret, domain, default_bucket = cfg['key'], cfg['secret'], cfg['domain'], cfg['default_bucket']
         self.client = MinioAgent(domain, key, secret, secure=False)
         self.domain = domain
         self.default_bucket = default_bucket
     
     def geturl(self, entrypoint):
         bucket, bucket_name = entrypoint.split('/')
-        return 'http://{}/{}/{}_{}'.format(self.domain, self.default_bucket, bucket, bucket_name)
+        return 'http://{}/{}_{}'.format(self.domain, bucket, bucket_name)
 
     def put(self, file, bucket, bucket_name, tmp=True):
         try:
             if tmp:
                 _bucket = 'tmp_file_' + bucket
             else:
                 _bucket = bucket
             b_name = '{}_{}'.format(_bucket, bucket_name)
             print('uploading to {}...'.format(self.domain))
             ret, e = self.client.upload_file(file, self.default_bucket, b_name)
             if ret:
                 print('upload success.')
                 return True, '{}/{}'.format(_bucket, bucket_name)
-            print('upload failed: {}'.format(e))
+            print('upload failed.')
             return False, e
         except Exception as e:
-            return False, traceback.format_exc()
+            traceback.print_exc()
+            return False, str(e)
     
     async def put_async(self, file, bucket, bucket_name, tmp=True):
         return self.put(file, bucket, bucket_name, tmp)
 
     def put_buffer(self, buffer, bucket, bucket_name):
         try:
             b_name = '{}_{}'.format(bucket, bucket_name)
@@ -53,49 +55,26 @@
 
     def get(self, download_path, bucket, bucket_name, tries=0):
         try:
             if tries >= 3:
                 return False, '下载出错'
             else:
                 url = 'http://{}/{}/{}'.format(self.domain, self.default_bucket, '{}_{}'.format(bucket, bucket_name))
-                print('downloading {} -> {}'.format(url, download_path))
-
-                if os.path.isfile(download_path):
-                    os.remove(download_path)
-
-                self.create_dir_if_not_exists(download_path)
-                path = self.download_file(url, download_path)
-                if path:
-                    return True, download_path
-                return self.get(download_path, bucket, bucket_name, tries+1)
+                with httpx.stream('GET', url) as response:
+                    if response.status_code == 200:
+                        with open(download_path, mode='wb') as f:
+                            for chunk in response.iter_bytes():
+                                f.write(chunk)
+                    else:
+                        raise ValueError()
+                return True, download_path
         except Exception as e:
-            traceback.print_exc()
             if tries >= 3:
                 return False, str(e)
             else:
                 return self.get(download_path, bucket, bucket_name, tries+1)
 
-    async def get_async(self, download_path, bucket, bucket_name, tries=0):
-        try:
-            if tries >= 3:
-                return False, '下载出错'
-            else:
-                url = 'http://{}/{}/{}'.format(self.domain, self.default_bucket, '{}_{}'.format(bucket, bucket_name))
-                print('downloading {} -> {}'.format(url, download_path))
-
-                if os.path.isfile(download_path):
-                    os.remove(download_path)
-
-                self.create_dir_if_not_exists(download_path)
-                path = self.download_file(url, download_path)
-                if path:
-                    return True, download_path
-                return await self.get_async(download_path, bucket, bucket_name, tries+1)
-        except Exception as e:
-            traceback.print_exc()
-            if tries >= 3:
-                return False, str(e)
-            else:
-                return await self.get_async(download_path, bucket, bucket_name, tries+1)
+    async def get_async(self, download_path, bucket, bucket_name):
+        return self.get(download_path, bucket, bucket_name)
```

### Comparing `hmfs-1.1.5131/hamunafs/backends/bk_wy.py` & `hmfs-1.1.6/hamunafs/backends/bk_qiniu.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,46 +1,54 @@
-import os
-import asyncio
+from sqlite3 import DataError
 import traceback
+import httpx
 from aiohttp_retry import ExponentialRetry, RetryClient
+from aiofile import async_open
 
-from nos import Client
-from nos.transport import Transport
+from qiniu import put_file, put_data, Auth, etag
+from qiniu import BucketManager, build_batch_delete
+from qiniu import Zone, set_default
 
 from hamunafs.backends.base import BackendBase
 
-class WYSF(BackendBase):
+class Qiniu(BackendBase):
     def __init__(self, cfg):
         key, secret, domain, default_bucket = cfg['key'], cfg['secret'], cfg['domain'], cfg['default_bucket']
-        self.client = Client(key, secret, Transport)
+        self.auth = Auth(key, secret)
         self.domain = domain
         self.default_bucket = default_bucket
-
+        self.bucket = BucketManager(self.auth)
+    
     def get_token(self, filename):
-        return ''
+        return self.auth.upload_token(self.default_bucket, filename)
     
     def geturl(self, entrypoint):
         bucket, bucket_name = entrypoint.split('/')
         return 'http://{}/{}_{}'.format(self.domain, bucket, bucket_name)
 
     def put(self, file, bucket, bucket_name, tmp=True):
         try:
             if tmp:
                 _bucket = 'tmp_file_' + bucket
             else:
                 _bucket = bucket
             b_name = '{}_{}'.format(_bucket, bucket_name)
-            with open(file, 'rb') as f:
-                resp = self.client.put_object(self.default_bucket, b_name, f)
-            if resp.get('etag', None):
+            print('acquiring upload token....')
+            token = self.auth.upload_token(self.default_bucket, b_name)
+            print('upload token acquired -> {}'.format(token))
+            print('uploading...')
+            ret, info = put_file(token, b_name, file)
+            if ret is not None:
                 print('upload success.')
                 return True, '{}/{}'.format(_bucket, bucket_name)
+            print('upload failed.')
             return False, '上传失败'
         except Exception as e:
-            return False, traceback.format_exc()
+            traceback.print_exc()
+            return False, str(e)
     
     async def put_async(self, file, bucket, bucket_name, tmp=True):
         return self.put(file, bucket, bucket_name, tmp)
 
     def put_buffer(self, buffer, bucket, bucket_name):
         try:
             b_name = '{}_{}'.format(bucket, bucket_name)
@@ -49,102 +57,52 @@
             if ret is not None:
                 return True, '{}/{}'.format(bucket, bucket_name)
             return False, '上传失败'
         except Exception as e:
             return False, str(e)
 
     async def put_buffer_async(self, buffer, bucket, bucket_name):
-        try:
-            b_name = '{}_{}'.format(bucket, bucket_name)
-            bucket = await self.cow.get_bucket(self.default_bucket)
-            ret, info = await bucket.put_data(key=b_name, data=buffer)
-            if ret is not None:
-                return True, '{}/{}'.format(bucket, bucket_name)
-            return False, '上传失败'
-        except Exception as e:
-            return False, str(e)
+        return self.put_buffer(buffer, bucket, bucket_name)
 
     def get(self, download_path, bucket, bucket_name, tries=0):
         try:
             if tries >= 3:
                 return False, '下载出错'
             else:
                 url = 'http://{}/{}'.format(self.domain, '{}_{}'.format(bucket, bucket_name))
-                print('downloading {} -> {}'.format(url, download_path))
-
-                if os.path.isfile(download_path):
-                    os.remove(download_path)
-                self.create_dir_if_not_exists(download_path)
-                path = self.download_file(url, download_path)
-                if path:
-                    return True, download_path
-                return self.get(download_path, bucket, bucket_name, tries+1)
+                print(url)
+                with httpx.stream('GET', url) as response:
+                    if response.status_code == 200:
+                        with open(download_path, mode='wb') as f:
+                            for chunk in response.iter_bytes():
+                                f.write(chunk)
+                    else:
+                        raise ValueError()
+                return True, download_path
         except Exception as e:
-            traceback.print_exc()
             if tries >= 3:
                 return False, str(e)
             else:
                 return self.get(download_path, bucket, bucket_name, tries+1)
 
-    async def get_async(self, download_path, bucket, bucket_name, tries=0):
+    async def get_async(self, download_path, bucket, bucket_name):
         try:
-            if tries >= 3:
-                return False, '下载出错'
-            else:
-                url = 'http://{}/{}'.format(self.domain, '{}_{}'.format(bucket, bucket_name))
-                print('downloading {} -> {}'.format(url, download_path))
-
-                if os.path.isfile(download_path):
-                    os.remove(download_path)
-                self.create_dir_if_not_exists(download_path)
-                path = self.download_file(url, download_path)
-                if path:
-                    return True, download_path
-                return await self.get_async(download_path, bucket, bucket_name, tries+1)
+            url = 'http://{}/{}'.format(self.domain, '{}_{}'.format(bucket, bucket_name))
+            print(url)
+            retry_opts = ExponentialRetry(attempts=3)
+            async with RetryClient(retry_options=retry_opts) as session:
+                async with session.get(url) as response:
+                    if response.status == 200:
+                        async with async_open(download_path, mode='wb') as f:
+                            while True:
+                                chunk = await response.content.read(4096)
+                                if not chunk:
+                                    break
+                                await f.write(chunk)
+                    else:
+                        raise ValueError()
+            return True, download_path
         except Exception as e:
-            traceback.print_exc()
-            if tries >= 3:
-                return False, str(e)
-            else:
-                return await self.get_async(download_path, bucket, bucket_name, tries+1)
-
-    async def cleanup_old_files(self):
-        objects = self.client.list_objects(self.default_bucket, prefix='tmp_file', limit=1000)
-        keys = [object_list.find("Key").text for object_list in objects["response"].findall("Contents")]
-        try:
-            self.client.delete_objects(self.default_bucket, keys, quiet=False)
-        except:
-            pass
-
-        while len(keys) == 1000:
-            print('listing objects...')
-            objects = self.client.list_objects(self.default_bucket, prefix='tmp_file', limit=1000)
-            keys = [object_list.find("Key").text for object_list in objects["response"].findall("Contents")]
-
-            print('deleting objects...')
-            try:
-                self.client.delete_objects(self.default_bucket, keys, quiet=False)
-            except:
-                pass
-        
-        if len(keys) > 0:
-            print('deleting objects...')
-            try:
-                self.client.delete_objects(self.default_bucket, keys, quiet=True)
-            except:
-                pass
-
-        print('all deleting process done')
-
-
-
-if __name__ == '__main__':
-    client = WYSF({
-        'key': '46b5e0508a9641a485c6d3f62078e7ab',
-        'secret': 'fd187963fb8943febc2624e1241081ed',
-        'domain': 'hamuna-images.nos-eastchina1.126.net',
-        'default_bucket': 'hamuna-images'
-    })
-    # asyncio.get_event_loop().run_until_complete(client.cleanup_old_files())
+            return False, str(e)
```

### Comparing `hmfs-1.1.5131/hamunafs/client.py` & `hmfs-1.1.6/hamunafs/client.py`

 * *Files 14% similar despite different names*

```diff
@@ -45,17 +45,17 @@
         #self.cache_path = cache_path
         os.makedirs(cache_path, exist_ok=True)
         self.index_cache = Cache(cache_path)
         
         self.put_topic = 'fs_put'
         self.get_topic = 'fs_get'
 
-        # mqtt_client = MQTTClient('fs_server', 'opush', 'innovation').connect('kafka.ai.hamuna.club', 1883)
-        # mqtt_client.subscribe('fs_backend_update', 2)
-        # mqtt_client.register_on_message_handler(self.__on_mqtt_message)
+        mqtt_client = MQTTClient('fs_server', 'opush', 'innovation').connect('kafka.ai.hamuna.club', 1883)
+        mqtt_client.subscribe('fs_backend_update', 2)
+        mqtt_client.register_on_message_handler(self.__on_mqtt_message)
         
         self.update()
         self._inited = True
 
     
     def __on_mqtt_message(self, client, userdata, msg):
         if msg.topic == 'fs_backend_update':
@@ -95,15 +95,14 @@
         with self.lock:
             keys = [k for k in list(self.backend_pools.keys()) if k not in ignore_prefix]
             if len(keys) > 0:
 
                 selected_ind = int(random.uniform(0, len(keys)))
                 
                 selected_key = keys[selected_ind]
-                print('choosing {} backend'.format(selected_key))
                 return selected_key, self.backend_pools[selected_key]
             else:
                 return None, None
     
     def _get_appropriate_backend(self, url):
         with self.lock:
             prefix, _url = url.split('://')
@@ -162,66 +161,66 @@
         except:
             pass
         self.index_cache.set(key, _val, expire=ttl)
 
     def __put_to_cloud(self, path, bucket, bucket_name, tmp=True, tries=0, ignore_prefix=[]):
         prefix, backend = self._random_pick_backend(ignore_prefix)
         if prefix is None:
-            return False, '尝试过所有Backend都失败'
+            return False, None
         
         ret, e = backend.put(path, bucket, bucket_name, tmp)
         if ret:
             url = '{}://{}'.format(prefix, e)
             return True, url
         else:
-            ignore_prefix.append(prefix)
-            return self.__put_to_cloud(path, bucket, bucket_name, tmp, tries+1, ignore_prefix=ignore_prefix)
+            if tries > 3:
+                return False, None
+            else:
+                ignore_prefix.append(prefix)
+                self.__put_to_cloud(path, bucket, bucket_name, tmp, tries+1, ignore_prefix=ignore_prefix)
             
-    def put_to_cloud(self, path, bucket, bucket_name, tmp=True, refresh=False):
-        if os.path.isfile(path):
-            cache_key = 'cloud_{}_{}'.format(bucket, bucket_name)
-            cache_data = self.get_cache(cache_key, toObj=False) if not refresh else None
-            if cache_data is None:
-                ret, e = self.__put_to_cloud(path, bucket, bucket_name, tmp)
-                if ret:
-                    self.cache(cache_key, e)
+    def put_to_cloud(self, path, bucket, bucket_name, tmp=True):
+        cache_key = 'cloud_{}_{}'.format(bucket, bucket_name)
+        cache_data = self.get_cache(cache_key, toObj=False)
+        if cache_data is None:
+            ret, e = self.__put_to_cloud(path, bucket, bucket_name, tmp)
+            if ret:
+                self.cache(cache_key, e)
 
-                return ret, e
-            else:
-                return True, cache_data
+            return ret, e
         else:
-            return False, '文件不存在'
+            return True, cache_data
 
     async def __put_to_cloud_async(self, path, bucket, bucket_name, tmp=True, tries=0, ignore_prefix=[]):
         prefix, backend = self._random_pick_backend(ignore_prefix)
         if prefix is None:
-            return False, '尝试过所有Backend都失败'
+            return False, None
         
         ret, e = await backend.put_async(path, bucket, bucket_name, tmp)
         if ret:
             url = '{}://{}'.format(prefix, e)
             return True, url
         else:
-            ignore_prefix.append(prefix)
-            return await self.__put_to_cloud_async(path, bucket, bucket_name, tmp, tries+1, ignore_prefix=ignore_prefix)
+            if tries > 3:
+                return False, None
+            else:
+                ignore_prefix.append(prefix)
+                await self.__put_to_cloud_async(path, bucket, bucket_name, tmp, tries+1, ignore_prefix=ignore_prefix)
 
         
     async def put_to_cloud_async(self, path, bucket, bucket_name, tmp=True):
-        if os.path.isfile(path):
-            cache_key = 'cloud_{}_{}'.format(bucket, bucket_name)
-            cache_data = await self.get_cache_async(cache_key, toObj=False)
-            if cache_data is None:
-                ret, e = await self.__put_to_cloud_async(path, bucket, bucket_name, tmp)
-                if ret:
-                    await self.cache_async(cache_key, e)
-                return ret, e
-            else:
-                return True, cache_data
+        cache_key = 'cloud_{}_{}'.format(bucket, bucket_name)
+        cache_data = await self.get_cache_async(cache_key, toObj=False)
+        if cache_data is None:
+            ret, e = await self.__put_to_cloud_async(path, bucket, bucket_name, tmp)
+            if ret:
+                await self.cache_async(cache_key, e)
+            return ret, e
         else:
-            return False, '文件不存在'
+            return True, cache_data
     
     def get_from_cloud(self, path, url, force_copy=False, min_size=0):
         file_path = self.index_cache.get(url)
         if file_path is not None and os.path.isfile(file_path) and os.path.getsize(file_path) // 1024 >= min_size:
             print('loading from disk...')
             if force_copy:
                 if file_path == path:
@@ -243,17 +242,17 @@
                 self.index_cache.set(url, e)
                 return True, path
             else:
                 return ret, e
         else:
             return False, '未受支持的Backend'
 
-    async def get_from_cloud_async(self, path, url, force_copy=False, min_size=0, refresh=False):
+    async def get_from_cloud_async(self, path, url, force_copy=False, min_size=0):
         file_path = self.index_cache.get(url)
-        if file_path is not None and os.path.isfile(file_path) and os.path.getsize(file_path) // 1024 >= min_size and not refresh:
+        if file_path is not None and os.path.isfile(file_path) and os.path.getsize(file_path) // 1024 >= min_size:
             print('loading from disk...')
             if force_copy:
                 if file_path == path:
                     return True, path
                 else:
                     os.makedirs(os.path.split(path)[0], exist_ok=True)
                     
@@ -335,16 +334,15 @@
                 if resp['ret']:
                     tmp_url = resp['url']
                     return self.get_from_cloud(path, tmp_url, force_copy, min_size)
         else:
             self.redis.delkey(task_id)
         ret = self.mq.publish(self.get_topic, {
             'bucket': bucket,
-            'bucket_name': bucket_name,
-            'refresh': 'yes' if refresh else 'no'
+            'bucket_name': bucket_name
         })
         if ret:
             t = time.time()
             resp = None
             while True:
                 if time.time() - t >= timeout:
                     break
@@ -356,56 +354,14 @@
                         tmp_url = resp['url']
                         return self.get_from_cloud(path, tmp_url, force_copy, min_size)
                 
                 time.sleep(1/30)
                 
         return False, '获取失败'
 
-    def get_cloud_url(self, path, url, force_copy=False, min_size=0, timeout=60, refresh=False):
-        if '://' in url:
-            bucket, bucket_name = url.split('://')[1].split('/')
-        else:
-            bucket, bucket_name = url.split('/')
-
-        task_id = 'tmp_file_{}_{}'.format(bucket, bucket_name)
-        if not refresh:
-            if '://' in url:
-                return True, url
-            cached_resp = self.redis.get(task_id)
-
-            if cached_resp is not None and len(cached_resp) > 0:
-                resp = json.loads(cached_resp)
-                if resp['ret']:
-                    tmp_url = resp['url']
-                    return True, tmp_url
-        else:
-            self.redis.delkey(task_id)
-        ret = self.mq.publish(self.get_topic, {
-            'bucket': bucket,
-            'bucket_name': bucket_name,
-            'refresh': 'yes' if refresh else 'no'
-        })
-        if ret:
-            t = time.time()
-            resp = None
-            while True:
-                if time.time() - t >= timeout:
-                    break
-                
-                resp = self.redis.get(task_id)
-                if resp is not None and len(resp) > 0:
-                    resp = json.loads(resp)
-                    if resp['ret']:
-                        tmp_url = resp['url']
-                        return True, tmp_url
-                
-                time.sleep(1/30)
-                
-        return False, '获取失败'
-
     async def get_async(self, path, url, force_copy=False, min_size=0, timeout=60, refresh=False):
         if '://' in url:
             bucket, bucket_name = url.split('://')[1].split('/')
         else:
             bucket, bucket_name = url.split('/')
             
         task_id = 'tmp_file_{}_{}'.format(bucket, bucket_name)
@@ -440,72 +396,24 @@
                         break
                     
                     resp = await self.redis.get(task_id)
                     if resp is not None and len(resp) > 0:
                         resp = json.loads(resp)
                         if resp['ret']:
                             tmp_url = resp['url']
-                            return await self.get_from_cloud_async(path, tmp_url, force_copy, min_size, refresh=True)
-                    
-                    await asyncio.sleep(1/30)
-                return False, '超时'
-            else:
-                return False, 'MQ发送失败'
-        except Exception as e:
-            return False, '获取失败'
-    
-    async def get_cloud_url_async(self, path, url, force_copy=False, min_size=0, timeout=60, refresh=False):
-        if '://' in url:
-            bucket, bucket_name = url.split('://')[1].split('/')
-        else:
-            bucket, bucket_name = url.split('/')
-            
-        task_id = 'tmp_file_{}_{}'.format(bucket, bucket_name)
-        if not refresh:
-            if '://' in url:
-                return True, url
-
-            cached_resp = await self.redis.get(task_id)
-
-            if cached_resp is not None and len(cached_resp) > 0:
-                resp = json.loads(cached_resp)
-                if resp['ret']:
-                    tmp_url = resp['url']
-                    return True, tmp_url
-        else:
-            self.redis.delkey(task_id)
-        
-        try:
-            ret = await self.mq.async_publish(self.get_topic, {
-                'bucket': bucket,
-                'bucket_name': bucket_name,
-                'refresh': 'yes' if refresh else 'no'
-            })
-            if ret:
-                t = time.time()
-                resp = None
-                while True:
-                    if time.time() - t >= timeout:
-                        break
-                    
-                    resp = await self.redis.get(task_id)
-                    if resp is not None and len(resp) > 0:
-                        resp = json.loads(resp)
-                        if resp['ret']:
-                            tmp_url = resp['url']
-                            return True, tmp_url
+                            return await self.get_from_cloud_async(path, tmp_url, force_copy, min_size)
                     
                     await asyncio.sleep(1/30)
         except Exception as e:
             return False, '获取失败'
 
     async def get_mq_conn(self):
         return await self.mq.get_mq_conn()
 
-    async def put_from_cloud_async(self, url, bucket, bucket_name, timeout=120, file_ttl=-1):
+    async def put_from_cloud_async(self, url, bucket, bucket_name, timeout=10, file_ttl=-1):
         # save to cache
         task_id = 'tmp_file_{}_{}'.format(bucket, bucket_name)
         try:
             ret = await self.mq.async_publish(self.put_topic, {
                 'url': url,
                 'bucket': bucket,
                 'bucket_name': bucket_name,
@@ -528,27 +436,22 @@
                     
                     await asyncio.sleep(1/30)
             return False, '上传出错'
         except Exception as e:
             return False, str(e)
         
     
-    async def put_async(self, path, bucket, bucket_name, timeout=60, file_ttl=-1):
+    async def put_async(self, path, bucket, bucket_name, timeout=10, file_ttl=-1):
         ret, e = await self.put_to_cloud_async(path, bucket, bucket_name)
         if ret:
             ret, e = await self.put_from_cloud_async(e, bucket, bucket_name, timeout, file_ttl)
         return ret, e
     
     def geturl(self, entrypoint):
         prefix, bucket_info = entrypoint.split('://')
         if prefix in self.backend_pools:
             backend = self.backend_pools[prefix]
             return backend.geturl(bucket_info)
         else:
             return entrypoint
-
-    async def cleanup_cloud(self):
-        for k, backend in self.backend_pools.items():
-            print('cleanup {} files'.format(k))
-            await backend.cleanup_old_files()
```

### Comparing `hmfs-1.1.5131/hamunafs/server.py` & `hmfs-1.1.6/hamunafs/server.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,24 +1,21 @@
-from genericpath import isfile
 import traceback
 from function_scheduling_distributed_framework import fsdf_background_scheduler, task_deco, patch_frame_config, get_publisher, BrokerEnum
 from function_scheduling_distributed_framework.consumers.base_consumer import ExceptionForRequeue
 from hamunafs.utils.cachemanager import CacheManager
 from hamunafs.utils.minio import MinioAgent
 from hamunafs.client import Client
 
 import asyncio
 import time
 import os
 import argparse
-import shutil
 
 from hamunafs.utils.nsqmanager import MQManager
 from hamunafs.sqlite import DB
-from hamunafs.utils.timeutil import is_time_in_range
 
 def get_opts():
     parser = argparse.ArgumentParser()
     parser.add_argument('--host', type=str, default='127.0.0.1')
     parser.add_argument('--port', type=str, default='9000')
     parser.add_argument('--acs-key', type=str, default='hmcz')
     parser.add_argument('--acs-secret', type=str, default='1987yang')
@@ -58,14 +55,16 @@
 }
 
     
 minio = MinioAgent('{}:{}'.format(opt.host, opt.port), opt.acs_key, opt.acs_secret, secure=False, location=opt.location)
 
 cache_engine = CacheManager(opt.redis_host, opt.redis_pass, opt.redis_port, opt.redis_db, local_cache=None)
 
+
+
 patch_frame_config(
     NSQD_TCP_ADDRESSES=['{}:{}'.format(
         broker_cfg['host'], broker_cfg['port'])],
     NSQD_HTTP_CLIENT_HOST=broker_cfg['host'],
     NSQD_HTTP_CLIENT_PORT=broker_cfg['http_port']
 )
 
@@ -73,32 +72,33 @@
 
 @task_deco('fs_put', function_timeout=20, concurrent_mode=4, broker_kind=BrokerEnum.NSQ, specify_async_loop=asyncio.get_event_loop())
 async def file_transfer_put(url, bucket, bucket_name, ttl):
     key = 'file_transfer_put_{}_{}'.format(bucket, bucket_name)
     if await cache_engine.get_cache_async(key, return_obj=False) is not None:
         return
     
-    with cache_engine.lock(key, ttl=30) as lock:
+    with cache_engine.lock(key, ttl=10) as lock:
         if lock:
             try:
                 if await cache_engine.get_cache_async(key, return_obj=False) is not None:
                     return
                 
                 file_path = os.path.join(cache_path, '{}_{}'.format(bucket, bucket_name))
+                # print('downloading file from cloud....')
                 ret, e = await hmfs_client.get_from_cloud_async(file_path, url)
 
                 if ret:
-                    print('cloud downloaded. start uploading...')
+                    # print('cloud downloaded. start uploading...')
                     ret, e = minio.upload_file(e, bucket, bucket_name)
                     if ret:
                         cache_engine.cache('tmp_file_{}_{}'.format(bucket, bucket_name), {
                             'ret': True, 
                             'url': url
-                        }, expired=24 * 60 * 60)
-                        print('upload success!!')
+                        }, expired=60)
+                        # print('upload success!!')
                         
                         if ttl != -1:
                             expired_time = time.time() + ttl * 24 * 60 * 60
                             sqlite_db.iud('insert into ttl_files(bucket, bucket_name, expired) values (?, ?, ?)', (bucket, bucket_name, expired_time))
                         
                     else:
                         cache_engine.cache('tmp_file_{}_{}'.format(bucket, bucket_name), {
@@ -120,16 +120,16 @@
         else:
             cache_engine.cache('tmp_file_{}_{}'.format(bucket, bucket_name), {
                         'ret': False,
                         'err': '锁超时'
                     }, expired=60)
 
 
-def put_to_cloud(task_id, file_path, bucket, bucket_name, refresh=False, tries=0):
-    ret, e = hmfs_client.put_to_cloud(file_path, bucket, bucket_name, refresh=refresh)
+def put_to_cloud(task_id, file_path, bucket, bucket_name, tries=0):
+    ret, e = hmfs_client.put_to_cloud(file_path, bucket, bucket_name)
     if ret:
         print('fget -> uploaded to cloud')
         cache_engine.cache(task_id, {
             'ret': True,
             'url': e
         }, expired=60 * 60 * 24 * 1)
     else:
@@ -137,15 +137,15 @@
             print('fget -> failed uploading to cloud')
             cache_engine.cache(task_id, {
                 'ret': False, 
                 'err': e
             }, expired=60)
         else:
             print('fget -> retry put to cloud') 
-            put_to_cloud(task_id, file_path, bucket, bucket_name, refresh=refresh, tries=tries+1)
+            put_to_cloud(task_id, file_path, bucket, bucket_name, tries+1)
 
 @task_deco('fs_get', function_timeout=60, concurrent_mode=4, broker_kind=BrokerEnum.NSQ)
 async def file_transfer_get(bucket, bucket_name, refresh='no'):
     try:
         task_id = 'tmp_file_{}_{}'.format(bucket, bucket_name)
         file_path = os.path.join(cache_path, '{}_{}'.format(bucket, bucket_name))
         if not os.path.isfile(file_path):
@@ -159,15 +159,15 @@
                 cache_engine.cache(task_id, {
                     'ret': False, 
                     'err': e.message
                 }, expired=60)
                 return
         
 
-        put_to_cloud(task_id, file_path, bucket, bucket_name, refresh=refresh=='yes')
+        put_to_cloud(task_id, file_path, bucket, bucket_name)
     except Exception as e:
         traceback.print_exc()
     
 
 # @task_deco('file_transfer_del', function_timeout=60, concurrent_mode=4, broker_kind=BrokerEnum.NSQ)
 # async def file_transfer_del(bucket, bucket_name):
 #     key = 'del_file_{}_{}'.format(bucket, bucket_name)
@@ -202,31 +202,22 @@
     
 async def extra_tasks():
     while True:
         try:
             affected_records = await ttl_cleanup()
             if affected_records > 0:
                 print('data cleaned')
-
-            if is_time_in_range('02:00', '04:00'):
-                if cache_engine.get_cache('hmfs_cleanup'):
-                    continue
-                await hmfs_client.cleanup_cloud()
-                cache_engine.cache('hmfs_cleanup', 1, expired=7200)
-
-                shutil.rmtree(cache_path, ignore_errors=True)
-                os.mkdir(cache_path)
         except:
             traceback.print_exc()
         finally:
             await asyncio.sleep(30)
 
 def run():
     file_transfer_get.consume()
     file_transfer_put.consume()
-    # file_transfer_del.consume()
+    # # file_transfer_del.consume()
 
     # asyncio.get_event_loop().run_until_complete(file_transfer_put('qiniu://tmp_file_test/test.jpg', 'test', 'test.jpg', -1))
     
     loop = asyncio.new_event_loop()
     loop.run_until_complete(extra_tasks())
-    # asyncio.get_event_loop().run_until_complete(hmfs_client.cleanup_cloud())
+
```

### Comparing `hmfs-1.1.5131/hamunafs/sqlite/__init__.py` & `hmfs-1.1.6/hamunafs/sqlite/__init__.py`

 * *Files identical despite different names*

### Comparing `hmfs-1.1.5131/hamunafs/utils/cachemanager.py` & `hmfs-1.1.6/hamunafs/utils/cachemanager.py`

 * *Files identical despite different names*

### Comparing `hmfs-1.1.5131/hamunafs/utils/minio.py` & `hmfs-1.1.6/hamunafs/utils/minio.py`

 * *Files identical despite different names*

### Comparing `hmfs-1.1.5131/hamunafs/utils/mqtt.py` & `hmfs-1.1.6/hamunafs/utils/mqtt.py`

 * *Files identical despite different names*

### Comparing `hmfs-1.1.5131/hamunafs/utils/nsqmanager.py` & `hmfs-1.1.6/hamunafs/utils/nsqmanager.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,13 +1,11 @@
 
 import traceback
-from gnsq import Producer
+from gnsq import Producer, Consumer, Message, NsqdHTTPClient
 from ansq import open_connection
-from ansq.tcp.connection import ConnectionStatus
-from ansq.tcp.exceptions import ConnectionClosedError
 import asyncio
 import orjson
 import time
 
 from hamunafs.utils.singleton_wrapper import Singleton
 
 
@@ -19,103 +17,56 @@
         self.port = port
         self.async_mq = async_mq
         self.inited = False
         if init:
             self._init()
         self._inited = True
 
-        self.connection_locker = asyncio.Lock()
-    
     def _init(self):
-        self.addr = '{}:{}'.format(self.host, self.port)
-        self.producer = Producer(nsqd_tcp_addresses=[self.addr])
-        self.producer.start()
-
-    async def _init_async(self):
         if self.async_mq:
-            self.mq = await open_connection(self.host, self.port)
-
-    def close(self):
-        if not self.async_mq:
-            self.close_producer()
-
-    async def close_async(self):
-        try:
-            if self.async_mq:
-                await self.mq.close()
-                del self.mq
-        except:
-            traceback.print_exc()
+            self.mq = asyncio.get_event_loop().run_until_complete(open_connection(self.host, self.port))
+        else:
+            self.addr = '{}:{}'.format(self.host, self.port)
+            self.producer = Producer(nsqd_tcp_addresses=[self.addr])
+            self.producer.start()
+        self.inited = True
 
-    async def get_mq_conn(self, tries=0):
-        async with self.connection_locker:
-            if not hasattr(self, 'mq') or self.mq.status.is_closed:
-                await self._init_async()
-                await asyncio.sleep(0.1)
-            else:
-                if not self.mq.status.is_connected:
-                    is_timeout = False
-                    t = time.time()
-                    while self.mq.status.is_reconnecting:
-                        if time.time() - t > 5:
-                            is_timeout = True
-                            break
-                    
-                    if self.mq.status.is_connected:
-                        return self.mq
-                    
-                    if is_timeout:
-                        await self.close_async()
-                        return None
+    async def get_mq_conn(self):
+        if not hasattr(self, 'mq'):
+            self.mq = await open_connection(self.host, self.port)
         
-        return self.mq
+        if not self.mq.is_connected:
+            del self.mq
+            return await self.get_mq_conn()
+        else:
+            return self.mq
             
     def _encode_message(self, message):
         if isinstance(message, str):
             message = message.encode('utf-8')
         else:
             message = orjson.dumps(message)
         return message
-
-    def close_producer(self):
-        try:
-            self.producer.close()
-        except:
-            pass
-
-    def restart_producer(self):
-        try:
-            self.close_producer()
-            del self.producer
-        except:
-            pass
-        finally:
-            self._init()
             
     def publish(self, topic, message, multi=False):
         try:
-            if not self.producer.is_running:
-                self.producer.close()
-                time.sleep(0.5)
-                self._init()
-                
             if multi and isinstance(message, list):
                 message = list(map(self._encode_message, message))
             else:
                 message = self._encode_message(message)
             
             if multi:
                 pub_func = self.producer.multipublish
             else:
                 pub_func = self.producer.publish
             
             ret = pub_func(topic, message).decode()
         except Exception as e:
             traceback.print_exc()
-            ret = 'ERR'
+            ret = False
         max_t = 5
         t = 0
         while ret != 'OK' and t < max_t: 
             try:
                 ret = pub_func(topic, message).decode()
             except:
                 ret = 'ERR'
@@ -123,49 +74,40 @@
                 time.sleep(1)
             t += 1
         ret = ret == 'OK'
         if ret:
             print('nsq publish success!')
         return ret
 
-    async def __mq_pub(self, topic, message, mq=None, tries=0):
-        if tries > 5:
-            return False
-        if mq is None:
-            mq = await self.get_mq_conn()
-        try:
-            if mq is None:
-                return await self.__mq_pub(topic, message, None, tries+1)
-                
-            resp = await mq.pub(topic, message)
-            return resp.is_ok
-        except:
-            traceback.print_exc()
-            await self.close_async()
-            return await self.__mq_pub(topic, message, None, tries+1)
-
-
     async def async_publish(self, topic, message, mq=None):
         try:
             if isinstance(message, str):
                 message = message.encode('utf-8')
             elif isinstance(message, bytes):
                 pass
             else:
                 message = orjson.dumps(message)
+            print('publishing')
 
-            ret = await self.__mq_pub(topic, message)
-            if ret:
-                print('published')
-            else:
-                print('publish failed')
+            if mq is None:
+                mq = await self.get_mq_conn()
+
+            ret = (await mq.pub(topic, message)).is_ok
+            max_t = 5
+            t = 0
+            while not ret and t < max_t: 
+                try:
+                    ret = (await mq.pub(topic, message)).is_ok
+                except:
+                    ret = False
+                t += 1
             return ret
         except Exception as e:
             print(traceback.print_exc())
-            return False
+            ret = False
 
 if __name__ == "__main__":
     manager = MQManager('kafka.ai.hamuna.club', 34150, async_mq=True)
     
     loop = asyncio.get_event_loop()
     loop.run_until_complete(manager._init_async())
```

### Comparing `hmfs-1.1.5131/hamunafs/utils/redisutil.py` & `hmfs-1.1.6/hamunafs/utils/redisutil.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-import asyncio
 import traceback
 import redis
 import time
 import threading
 
 
 from redis.exceptions import LockError 
@@ -14,15 +13,14 @@
             return
         self.host = host
         self.password = password
         self.port = port
         self.db = db
         self.locker = threading.Lock()
         self.connection_lost = True
-        self.stopped = False
         
         self._make_conn()
         self._inited = True
         
     def _background_heartbeat(self):
         print('开始心跳')
         if hasattr(self, 'heartbeat_thread'):
@@ -32,36 +30,30 @@
             
         self.heartbeat_thread = threading.Thread(target=self._ping, args=())
         self.heartbeat_thread.daemon = True
         self.heartbeat_thread.start()
         # self._ping()
         
     def _ping(self):
-        while not self.connection_lost or not self.stopped:
+        while not self.connection_lost:
             if self.set('ping', 'ok', expired=30):
                 print('pinged')
             else:
                 self.connection_lost = True
                 print('连接丢失')
-                break
                 
             time.sleep(30)
             
     def __release_conn(self):
         if hasattr(self, 'conn'):
             print('释放连接')
-            self.conn.close()
-            self.connection_lost = True
-            
             del self.conn
     
     def _make_conn(self):
         try:
-            if self.stopped:
-                return
             self.__release_conn()
             print('创建新连接')
             pool = redis.ConnectionPool(
                 host=self.host, password=self.password, port=self.port, db=self.db, decode_responses=True, socket_timeout=60, socket_connect_timeout=30, socket_keepalive=True, retry_on_timeout=True)
             self.conn = redis.StrictRedis(connection_pool=pool)
             # self.conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db, password=self.password, decode_responses=True, socket_connect_timeout=1, socket_timeout=1)
             if self.conn.ping():
@@ -91,15 +83,15 @@
         if conn is None:
             with self.locker:
                 conn = self.__get_connection(pipeline, transaction)
                 if conn is None:
                     while not self._make_conn():
                         time.sleep(0.1)
                     
-                    conn = self.__get_connection(pipeline, transaction)
+                    conn = self.conn
            
         return conn
 
     def lock(self, lock_id, ttl=60, tries=0):
         try:
             conn = self._get_connection()
             print('获取锁 -> {}'.format(lock_id))
@@ -268,24 +260,14 @@
         conn = self._get_connection()
         return conn.zcount(z_name, score_min, score_max)
 
     def zscore(self, z_name, key):
         conn = self._get_connection()
         return conn.zscore(z_name, key)
 
-    def close(self):
-        try:
-            self.__release_conn()
-            self.stopped = True
-            if self.heartbeat_thread.isAlive:
-                self.heartbeat_thread.join()
-        except Exception as e:
-            traceback.print_exc()
-        
-
 try:
     from redis import asyncio as coredis
 except:
     pass
 
 class XRedisAsync(Singleton):
     def __init__(self, host, password, port, db=0):
@@ -294,24 +276,19 @@
         self.host = host
         self.password = password
         self.port = port
         self.db = db
         self.locker = threading.Lock()
         pool = coredis.ConnectionPool(host=self.host, password=self.password, port=self.port, db=self.db, decode_responses=True, socket_keepalive=True, retry_on_timeout=True)
         self.conn = coredis.StrictRedis(connection_pool=pool)
-
-    async def _ping(self):
-        ret = await self.conn.ping()
-        if ret:
-            print('pinged')
             
     async def __release_conn(self):
         if hasattr(self, 'conn'):
             print('释放连接')
-            await self.conn.close()
+            await self.conn.quit()
             del self.conn
     
     async def _make_conn(self):
         try:
             await self.__release_conn()
             print('创建新连接')
             pool = coredis.ConnectionPool(host=self.host, password=self.password, port=self.port, db=self.db, decode_responses=True, socket_keepalive=True, retry_on_timeout=True)
@@ -327,52 +304,52 @@
             return False
             
     def __get_connection(self):
         if hasattr(self, 'conn'):
             return self.conn
         return None
 
-    async def _get_connection(self, pipeline=False, transaction=True):
+    async def _get_connection(self, pipeline=False, transaction=False):
         conn = self.__get_connection()
         
         if conn is None:
             with self.locker:
                 ret = await self._make_conn()
                 return await self._get_connection(pipeline, transaction)
         
         if pipeline:
-            return conn.pipeline(transaction)
+            return await conn.pipeline(transaction)
         else:
             return conn
 
     async def lock(self, lock_id, ttl=60, tries=0):
         try:
             conn = await self._get_connection()
             print('获取锁 -> {}'.format(lock_id))
             return conn.lock('lock_' + lock_id, blocking_timeout=10, timeout=ttl)
         except LockError as error:
             print(str(error))
             return None
         except Exception as e:
             if tries < 3:
-                await asyncio.sleep(0.1)
+                time.sleep(0.1)
                 return await self.lock(lock_id, ttl, tries + 1)
             else:
                 traceback.print_exc()
 
     async def set(self, key, val, expired=None, tries=0):
         conn = await self._get_connection()
         try:
             await conn.set(key, val)
             if expired is not None:
                 await conn.expire(key, expired)
             return True
         except Exception as e:
             if tries < 3:
-                await asyncio.sleep(0.1)
+                time.sleep(0.1)
                 await self.set(key, val, expired, tries + 1)
             else:
                 traceback.print_exc()
         return False
 
     async def set_expire_time(self, key, expired):
         conn = await self._get_connection()
@@ -492,17 +469,15 @@
     
     async def get_hmget(self, hashname, keys):
         conn = await self._get_connection()
         return await conn.hmget(hashname, keys)
     
     async def zadd(self, z_name, member, val):
         conn = await self._get_connection()
-        return await conn.zadd(z_name, {
-            member: val
-        })
+        return await conn.zadd(z_name, val, member)
     
     async def zrem(self, z_name, member):
         conn = await self._get_connection()
         return await conn.zrem(z_name, member)
         
     async def zrange(self, z_name, score_min, score_max):
         conn = await self._get_connection()
@@ -511,13 +486,7 @@
     async def zcount(self, z_name, score_min, score_max):
         conn = await self._get_connection()
         return await conn.zcount(z_name, score_min, score_max)
 
     async def zscore(self, z_name, key):
         conn = await self._get_connection()
         return await conn.zscore(z_name, key)
-
-    async def close(self):
-        try:
-            await self.__release_conn()
-        except:
-            traceback.print_exc()
```

### Comparing `hmfs-1.1.5131/setup.py` & `hmfs-1.1.6/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 from setuptools import setup, find_packages
 
 setup(
     name='hmfs',
-    version='1.1.5131',
+    version='1.1.6',
     packages=find_packages(),
     license="MIT",
     description='Distributed filesystem for Hamuna AI',
     long_description='Distributed filesystem for Hamuna AI with multiple third party middleware transfer points',
     long_description_content_type="text/plain",
     author='O.Push',
     author_email='opush.developer@outlook.com',
     url='https://www.hamuna.club',
     package_dir={'': '.'},
-    install_requires=['minio', 'redis==4.3.4', 'paho-mqtt', 'gnsq', 'ansq', 'qiniu', 'boto', 'diskcache',
-                      'httpx', 'aiofile', 'aiohttp', 'aiohttp_retry', 'aiobotocore', 'nos-python3-sdk', 'async_exit_stack', 'wget']
+    install_requires=['minio', 'redis', 'paho-mqtt', 'gnsq', 'aonsq', 'qiniu', 'boto', 'diskcache',
+                      'httpx', 'aiofile', 'aiohttp', 'aiohttp_retry', 'aiobotocore', 'nos-python3-sdk']
 )
```

