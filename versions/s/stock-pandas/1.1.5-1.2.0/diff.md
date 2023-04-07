# Comparing `tmp/stock-pandas-1.1.5.tar.gz` & `tmp/stock-pandas-1.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "stock-pandas-1.1.5.tar", last modified: Wed Apr  5 13:32:47 2023, max compression
+gzip compressed data, was "stock-pandas-1.2.0.tar", last modified: Fri Apr  7 01:59:37 2023, max compression
```

## Comparing `stock-pandas-1.1.5.tar` & `stock-pandas-1.2.0.tar`

### file list

```diff
@@ -1,59 +1,60 @@
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.497634 stock-pandas-1.1.5/
--rw-r--r--   0 kael       (501) staff       (20)     1070 2020-03-06 12:08:18.000000 stock-pandas-1.1.5/LICENSE
--rw-r--r--   0 kael       (501) staff       (20)    26893 2023-04-05 13:32:47.497792 stock-pandas-1.1.5/PKG-INFO
--rw-r--r--   0 kael       (501) staff       (20)      197 2023-04-05 13:32:47.498290 stock-pandas-1.1.5/setup.cfg
--rw-r--r--   0 kael       (501) staff       (20)     2865 2023-04-05 13:31:50.000000 stock-pandas-1.1.5/setup.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.482041 stock-pandas-1.1.5/stock_pandas/
--rw-r--r--   0 kael       (501) staff       (20)      313 2023-04-05 13:31:37.000000 stock-pandas-1.1.5/stock_pandas/__init__.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.486351 stock-pandas-1.1.5/stock_pandas/commands/
--rw-r--r--   0 kael       (501) staff       (20)      157 2020-03-16 07:15:53.000000 stock-pandas-1.1.5/stock_pandas/commands/__init__.py
--rw-r--r--   0 kael       (501) staff       (20)     1151 2021-02-12 14:59:08.000000 stock-pandas-1.1.5/stock_pandas/commands/base.py
--rw-r--r--   0 kael       (501) staff       (20)     5409 2021-02-13 04:45:02.000000 stock-pandas-1.1.5/stock_pandas/commands/over_bought_or_sold.py
--rw-r--r--   0 kael       (501) staff       (20)     1671 2021-02-12 14:59:57.000000 stock-pandas-1.1.5/stock_pandas/commands/support_and_resistance.py
--rw-r--r--   0 kael       (501) staff       (20)     2691 2021-04-03 12:27:59.000000 stock-pandas-1.1.5/stock_pandas/commands/tools.py
--rw-r--r--   0 kael       (501) staff       (20)     3625 2021-02-14 01:38:18.000000 stock-pandas-1.1.5/stock_pandas/commands/trend_following.py
--rw-r--r--   0 kael       (501) staff       (20)     3665 2021-04-05 09:23:49.000000 stock-pandas-1.1.5/stock_pandas/common.py
--rw-r--r--   0 kael       (501) staff       (20)    10433 2023-04-05 13:25:59.000000 stock-pandas-1.1.5/stock_pandas/dataframe.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.488571 stock-pandas-1.1.5/stock_pandas/directive/
--rw-r--r--   0 kael       (501) staff       (20)      803 2021-04-04 12:17:02.000000 stock-pandas-1.1.5/stock_pandas/directive/__init__.py
--rw-r--r--   0 kael       (501) staff       (20)      463 2021-02-02 13:55:30.000000 stock-pandas-1.1.5/stock_pandas/directive/cache.py
--rw-r--r--   0 kael       (501) staff       (20)     5780 2020-03-28 10:17:57.000000 stock-pandas-1.1.5/stock_pandas/directive/factory.py
--rw-r--r--   0 kael       (501) staff       (20)     1156 2020-03-27 13:53:28.000000 stock-pandas-1.1.5/stock_pandas/directive/operators.py
--rw-r--r--   0 kael       (501) staff       (20)     6143 2020-03-28 11:30:52.000000 stock-pandas-1.1.5/stock_pandas/directive/parser.py
--rw-r--r--   0 kael       (501) staff       (20)     3524 2020-03-27 14:42:28.000000 stock-pandas-1.1.5/stock_pandas/directive/tokenizer.py
--rw-r--r--   0 kael       (501) staff       (20)     2830 2020-03-28 08:53:18.000000 stock-pandas-1.1.5/stock_pandas/directive/types.py
--rw-r--r--   0 kael       (501) staff       (20)     1446 2021-04-05 13:48:13.000000 stock-pandas-1.1.5/stock_pandas/exceptions.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.490464 stock-pandas-1.1.5/stock_pandas/math/
--rw-r--r--   0 kael       (501) staff       (20)        0 2020-03-15 02:07:27.000000 stock-pandas-1.1.5/stock_pandas/math/__init__.py
--rw-r--r--   0 kael       (501) staff       (20)   877379 2023-04-05 13:29:46.000000 stock-pandas-1.1.5/stock_pandas/math/_lib.cpp
--rw-r--r--   0 kael       (501) staff       (20)     1388 2021-01-09 17:19:25.000000 stock-pandas-1.1.5/stock_pandas/math/ma.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.492080 stock-pandas-1.1.5/stock_pandas/meta/
--rw-r--r--   0 kael       (501) staff       (20)      191 2021-04-10 06:13:57.000000 stock-pandas-1.1.5/stock_pandas/meta/__init__.py
--rw-r--r--   0 kael       (501) staff       (20)    17334 2023-04-05 13:12:55.000000 stock-pandas-1.1.5/stock_pandas/meta/cumulator.py
--rw-r--r--   0 kael       (501) staff       (20)     1994 2021-04-06 08:00:21.000000 stock-pandas-1.1.5/stock_pandas/meta/date.py
--rw-r--r--   0 kael       (501) staff       (20)     2397 2021-04-08 10:42:36.000000 stock-pandas-1.1.5/stock_pandas/meta/time_frame.py
--rw-r--r--   0 kael       (501) staff       (20)     4545 2021-04-09 10:42:39.000000 stock-pandas-1.1.5/stock_pandas/meta/utils.py
--rw-r--r--   0 kael       (501) staff       (20)      122 2021-04-08 09:00:06.000000 stock-pandas-1.1.5/stock_pandas/properties.py
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.484221 stock-pandas-1.1.5/stock_pandas.egg-info/
--rw-r--r--   0 kael       (501) staff       (20)    26893 2023-04-05 13:32:47.000000 stock-pandas-1.1.5/stock_pandas.egg-info/PKG-INFO
--rw-r--r--   0 kael       (501) staff       (20)     1417 2023-04-05 13:32:47.000000 stock-pandas-1.1.5/stock_pandas.egg-info/SOURCES.txt
--rw-r--r--   0 kael       (501) staff       (20)        1 2023-04-05 13:32:47.000000 stock-pandas-1.1.5/stock_pandas.egg-info/dependency_links.txt
--rw-r--r--   0 kael       (501) staff       (20)        1 2021-01-21 12:40:51.000000 stock-pandas-1.1.5/stock_pandas.egg-info/not-zip-safe
--rw-r--r--   0 kael       (501) staff       (20)       28 2023-04-05 13:32:47.000000 stock-pandas-1.1.5/stock_pandas.egg-info/requires.txt
--rw-r--r--   0 kael       (501) staff       (20)       13 2023-04-05 13:32:47.000000 stock-pandas-1.1.5/stock_pandas.egg-info/top_level.txt
-drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-05 13:32:47.497350 stock-pandas-1.1.5/test/
--rw-r--r--   0 kael       (501) staff       (20)     3961 2023-04-05 12:51:46.000000 stock-pandas-1.1.5/test/test_append.py
--rw-r--r--   0 kael       (501) staff       (20)     3529 2023-03-09 02:31:22.000000 stock-pandas-1.1.5/test/test_basic.py
--rw-r--r--   0 kael       (501) staff       (20)     1212 2023-04-05 13:13:00.000000 stock-pandas-1.1.5/test/test_column_info.py
--rw-r--r--   0 kael       (501) staff       (20)     3357 2020-08-24 10:52:08.000000 stock-pandas-1.1.5/test/test_commands.py
--rw-r--r--   0 kael       (501) staff       (20)      496 2020-03-27 11:03:52.000000 stock-pandas-1.1.5/test/test_commands_after_append.py
--rw-r--r--   0 kael       (501) staff       (20)     3886 2023-04-05 13:14:34.000000 stock-pandas-1.1.5/test/test_cum_append.py
--rw-r--r--   0 kael       (501) staff       (20)     2333 2021-04-10 06:24:57.000000 stock-pandas-1.1.5/test/test_factory.py
--rw-r--r--   0 kael       (501) staff       (20)      494 2020-03-25 13:57:53.000000 stock-pandas-1.1.5/test/test_indexing.py
--rw-r--r--   0 kael       (501) staff       (20)     1299 2021-02-10 08:33:52.000000 stock-pandas-1.1.5/test/test_manipulate.py
--rw-r--r--   0 kael       (501) staff       (20)     6010 2021-02-14 01:39:03.000000 stock-pandas-1.1.5/test/test_parser.py
--rw-r--r--   0 kael       (501) staff       (20)      698 2021-02-12 16:28:06.000000 stock-pandas-1.1.5/test/test_rolling_calc.py
--rw-r--r--   0 kael       (501) staff       (20)      303 2020-03-22 05:29:07.000000 stock-pandas-1.1.5/test/test_super_methods.py
--rw-r--r--   0 kael       (501) staff       (20)     1039 2021-04-08 10:34:51.000000 stock-pandas-1.1.5/test/test_time_frame.py
--rw-r--r--   0 kael       (501) staff       (20)      881 2020-03-13 14:30:56.000000 stock-pandas-1.1.5/test/test_tokenizer.py
--rw-r--r--   0 kael       (501) staff       (20)     2769 2021-04-09 06:06:41.000000 stock-pandas-1.1.5/test/test_truncated.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.921455 stock-pandas-1.2.0/
+-rw-r--r--   0 kael       (501) staff       (20)     1070 2020-03-06 12:08:18.000000 stock-pandas-1.2.0/LICENSE
+-rw-r--r--   0 kael       (501) staff       (20)    34714 2023-04-07 01:59:37.921674 stock-pandas-1.2.0/PKG-INFO
+-rw-r--r--   0 kael       (501) staff       (20)      197 2023-04-07 01:59:37.922110 stock-pandas-1.2.0/setup.cfg
+-rw-r--r--   0 kael       (501) staff       (20)     2865 2023-04-07 01:48:43.000000 stock-pandas-1.2.0/setup.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.907733 stock-pandas-1.2.0/stock_pandas/
+-rw-r--r--   0 kael       (501) staff       (20)      313 2023-04-05 13:31:37.000000 stock-pandas-1.2.0/stock_pandas/__init__.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.911746 stock-pandas-1.2.0/stock_pandas/commands/
+-rw-r--r--   0 kael       (501) staff       (20)      157 2020-03-16 07:15:53.000000 stock-pandas-1.2.0/stock_pandas/commands/__init__.py
+-rw-r--r--   0 kael       (501) staff       (20)     1151 2021-02-12 14:59:08.000000 stock-pandas-1.2.0/stock_pandas/commands/base.py
+-rw-r--r--   0 kael       (501) staff       (20)     5409 2021-02-13 04:45:02.000000 stock-pandas-1.2.0/stock_pandas/commands/over_bought_or_sold.py
+-rw-r--r--   0 kael       (501) staff       (20)     1671 2021-02-12 14:59:57.000000 stock-pandas-1.2.0/stock_pandas/commands/support_and_resistance.py
+-rw-r--r--   0 kael       (501) staff       (20)     2691 2021-04-03 12:27:59.000000 stock-pandas-1.2.0/stock_pandas/commands/tools.py
+-rw-r--r--   0 kael       (501) staff       (20)     3625 2021-02-14 01:38:18.000000 stock-pandas-1.2.0/stock_pandas/commands/trend_following.py
+-rw-r--r--   0 kael       (501) staff       (20)     3665 2021-04-05 09:23:49.000000 stock-pandas-1.2.0/stock_pandas/common.py
+-rw-r--r--   0 kael       (501) staff       (20)    10692 2023-04-07 01:32:31.000000 stock-pandas-1.2.0/stock_pandas/dataframe.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.914021 stock-pandas-1.2.0/stock_pandas/directive/
+-rw-r--r--   0 kael       (501) staff       (20)      803 2021-04-04 12:17:02.000000 stock-pandas-1.2.0/stock_pandas/directive/__init__.py
+-rw-r--r--   0 kael       (501) staff       (20)      463 2021-02-02 13:55:30.000000 stock-pandas-1.2.0/stock_pandas/directive/cache.py
+-rw-r--r--   0 kael       (501) staff       (20)     5780 2020-03-28 10:17:57.000000 stock-pandas-1.2.0/stock_pandas/directive/factory.py
+-rw-r--r--   0 kael       (501) staff       (20)     1156 2020-03-27 13:53:28.000000 stock-pandas-1.2.0/stock_pandas/directive/operators.py
+-rw-r--r--   0 kael       (501) staff       (20)     6143 2020-03-28 11:30:52.000000 stock-pandas-1.2.0/stock_pandas/directive/parser.py
+-rw-r--r--   0 kael       (501) staff       (20)     3524 2020-03-27 14:42:28.000000 stock-pandas-1.2.0/stock_pandas/directive/tokenizer.py
+-rw-r--r--   0 kael       (501) staff       (20)     2830 2020-03-28 08:53:18.000000 stock-pandas-1.2.0/stock_pandas/directive/types.py
+-rw-r--r--   0 kael       (501) staff       (20)     1446 2021-04-05 13:48:13.000000 stock-pandas-1.2.0/stock_pandas/exceptions.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.915601 stock-pandas-1.2.0/stock_pandas/math/
+-rw-r--r--   0 kael       (501) staff       (20)        0 2020-03-15 02:07:27.000000 stock-pandas-1.2.0/stock_pandas/math/__init__.py
+-rw-r--r--   0 kael       (501) staff       (20)   877379 2023-04-05 13:29:46.000000 stock-pandas-1.2.0/stock_pandas/math/_lib.cpp
+-rw-r--r--   0 kael       (501) staff       (20)     1388 2021-01-09 17:19:25.000000 stock-pandas-1.2.0/stock_pandas/math/ma.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.917090 stock-pandas-1.2.0/stock_pandas/meta/
+-rw-r--r--   0 kael       (501) staff       (20)      191 2021-04-10 06:13:57.000000 stock-pandas-1.2.0/stock_pandas/meta/__init__.py
+-rw-r--r--   0 kael       (501) staff       (20)    17334 2023-04-05 13:12:55.000000 stock-pandas-1.2.0/stock_pandas/meta/cumulator.py
+-rw-r--r--   0 kael       (501) staff       (20)     1994 2021-04-06 08:00:21.000000 stock-pandas-1.2.0/stock_pandas/meta/date.py
+-rw-r--r--   0 kael       (501) staff       (20)     2397 2021-04-08 10:42:36.000000 stock-pandas-1.2.0/stock_pandas/meta/time_frame.py
+-rw-r--r--   0 kael       (501) staff       (20)     4545 2021-04-09 10:42:39.000000 stock-pandas-1.2.0/stock_pandas/meta/utils.py
+-rw-r--r--   0 kael       (501) staff       (20)      122 2021-04-08 09:00:06.000000 stock-pandas-1.2.0/stock_pandas/properties.py
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.909941 stock-pandas-1.2.0/stock_pandas.egg-info/
+-rw-r--r--   0 kael       (501) staff       (20)    34714 2023-04-07 01:59:37.000000 stock-pandas-1.2.0/stock_pandas.egg-info/PKG-INFO
+-rw-r--r--   0 kael       (501) staff       (20)     1438 2023-04-07 01:59:37.000000 stock-pandas-1.2.0/stock_pandas.egg-info/SOURCES.txt
+-rw-r--r--   0 kael       (501) staff       (20)        1 2023-04-07 01:59:37.000000 stock-pandas-1.2.0/stock_pandas.egg-info/dependency_links.txt
+-rw-r--r--   0 kael       (501) staff       (20)        1 2021-01-21 12:40:51.000000 stock-pandas-1.2.0/stock_pandas.egg-info/not-zip-safe
+-rw-r--r--   0 kael       (501) staff       (20)       28 2023-04-07 01:59:37.000000 stock-pandas-1.2.0/stock_pandas.egg-info/requires.txt
+-rw-r--r--   0 kael       (501) staff       (20)       13 2023-04-07 01:59:37.000000 stock-pandas-1.2.0/stock_pandas.egg-info/top_level.txt
+drwxr-xr-x   0 kael       (501) staff       (20)        0 2023-04-07 01:59:37.921229 stock-pandas-1.2.0/test/
+-rw-r--r--   0 kael       (501) staff       (20)     3951 2023-04-07 01:35:06.000000 stock-pandas-1.2.0/test/test_append.py
+-rw-r--r--   0 kael       (501) staff       (20)     3716 2023-04-07 01:58:58.000000 stock-pandas-1.2.0/test/test_basic.py
+-rw-r--r--   0 kael       (501) staff       (20)     1212 2023-04-05 13:13:00.000000 stock-pandas-1.2.0/test/test_column_info.py
+-rw-r--r--   0 kael       (501) staff       (20)     3357 2020-08-24 10:52:08.000000 stock-pandas-1.2.0/test/test_commands.py
+-rw-r--r--   0 kael       (501) staff       (20)      496 2020-03-27 11:03:52.000000 stock-pandas-1.2.0/test/test_commands_after_append.py
+-rw-r--r--   0 kael       (501) staff       (20)     3886 2023-04-05 13:14:34.000000 stock-pandas-1.2.0/test/test_cum_append.py
+-rw-r--r--   0 kael       (501) staff       (20)     2333 2021-04-10 06:24:57.000000 stock-pandas-1.2.0/test/test_factory.py
+-rw-r--r--   0 kael       (501) staff       (20)      521 2023-04-07 01:46:48.000000 stock-pandas-1.2.0/test/test_fulfill.py
+-rw-r--r--   0 kael       (501) staff       (20)      494 2020-03-25 13:57:53.000000 stock-pandas-1.2.0/test/test_indexing.py
+-rw-r--r--   0 kael       (501) staff       (20)     1299 2021-02-10 08:33:52.000000 stock-pandas-1.2.0/test/test_manipulate.py
+-rw-r--r--   0 kael       (501) staff       (20)     6010 2021-02-14 01:39:03.000000 stock-pandas-1.2.0/test/test_parser.py
+-rw-r--r--   0 kael       (501) staff       (20)      698 2021-02-12 16:28:06.000000 stock-pandas-1.2.0/test/test_rolling_calc.py
+-rw-r--r--   0 kael       (501) staff       (20)      303 2020-03-22 05:29:07.000000 stock-pandas-1.2.0/test/test_super_methods.py
+-rw-r--r--   0 kael       (501) staff       (20)     1039 2021-04-08 10:34:51.000000 stock-pandas-1.2.0/test/test_time_frame.py
+-rw-r--r--   0 kael       (501) staff       (20)      881 2020-03-13 14:30:56.000000 stock-pandas-1.2.0/test/test_tokenizer.py
+-rw-r--r--   0 kael       (501) staff       (20)     2769 2021-04-09 06:06:41.000000 stock-pandas-1.2.0/test/test_truncated.py
```

### Comparing `stock-pandas-1.1.5/LICENSE` & `stock-pandas-1.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/setup.py` & `stock-pandas-1.2.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 from setuptools import (
     setup,
     Extension
 )
 
 import numpy as np
 
-__version__ = '1.1.5'
+__version__ = '1.2.0'
 
 
 BUILDING = os.environ.get('STOCK_PANDAS_BUILDING')
 UPLOADING = os.environ.get('STOCK_PANDAS_UPLOADING')
 
 
 def read(*fname) -> str:
```

### Comparing `stock-pandas-1.1.5/stock_pandas/commands/base.py` & `stock-pandas-1.2.0/stock_pandas/commands/base.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/commands/over_bought_or_sold.py` & `stock-pandas-1.2.0/stock_pandas/commands/over_bought_or_sold.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/commands/support_and_resistance.py` & `stock-pandas-1.2.0/stock_pandas/commands/support_and_resistance.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/commands/tools.py` & `stock-pandas-1.2.0/stock_pandas/commands/tools.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/commands/trend_following.py` & `stock-pandas-1.2.0/stock_pandas/commands/trend_following.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/common.py` & `stock-pandas-1.2.0/stock_pandas/common.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/dataframe.py` & `stock-pandas-1.2.0/stock_pandas/dataframe.py`

 * *Files 0% similar despite different names*

```diff
@@ -234,14 +234,26 @@
             size,
             apply,
             fill,
             stride,
             not forward
         )
 
+    def fulfill(self):
+        """
+        Fulfill all the stock columns in the dataframe
+
+        Returns:
+            self
+        """
+        for column in self._stock_columns_info_map.keys():
+            self._fulfill_series(column)
+
+        return self
+
     # --------------------------------------------------------------------
 
     def _map_keys(self, keys) -> List:
         return [
             self._map_single_key(key)
             for key in keys
         ]
```

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/__init__.py` & `stock-pandas-1.2.0/stock_pandas/directive/__init__.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/factory.py` & `stock-pandas-1.2.0/stock_pandas/directive/factory.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/operators.py` & `stock-pandas-1.2.0/stock_pandas/directive/operators.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/parser.py` & `stock-pandas-1.2.0/stock_pandas/directive/parser.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/tokenizer.py` & `stock-pandas-1.2.0/stock_pandas/directive/tokenizer.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/directive/types.py` & `stock-pandas-1.2.0/stock_pandas/directive/types.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/exceptions.py` & `stock-pandas-1.2.0/stock_pandas/exceptions.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/math/_lib.cpp` & `stock-pandas-1.2.0/stock_pandas/math/_lib.cpp`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/math/ma.py` & `stock-pandas-1.2.0/stock_pandas/math/ma.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/meta/cumulator.py` & `stock-pandas-1.2.0/stock_pandas/meta/cumulator.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/meta/date.py` & `stock-pandas-1.2.0/stock_pandas/meta/date.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/meta/time_frame.py` & `stock-pandas-1.2.0/stock_pandas/meta/time_frame.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas/meta/utils.py` & `stock-pandas-1.2.0/stock_pandas/meta/utils.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/stock_pandas.egg-info/SOURCES.txt` & `stock-pandas-1.2.0/stock_pandas.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -36,14 +36,15 @@
 test/test_append.py
 test/test_basic.py
 test/test_column_info.py
 test/test_commands.py
 test/test_commands_after_append.py
 test/test_cum_append.py
 test/test_factory.py
+test/test_fulfill.py
 test/test_indexing.py
 test/test_manipulate.py
 test/test_parser.py
 test/test_rolling_calc.py
 test/test_super_methods.py
 test/test_time_frame.py
 test/test_tokenizer.py
```

### Comparing `stock-pandas-1.1.5/test/test_append.py` & `stock-pandas-1.2.0/test/test_append.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,21 +7,19 @@
 )
 
 from stock_pandas import (
     StockDataFrame
 )
 
 from .common import (
-    get_tencent
+    get_tencent,
+    TIME_KEY
 )
 
 
-TIME_KEY = 'time_key'
-
-
 @pytest.fixture
 def tencent() -> DataFrame:
     return get_tencent(stock=False)
 
 
 def check_append(head, new, ctor_twice=False):
     stock = StockDataFrame(head, date_col=TIME_KEY, copy=True)
```

### Comparing `stock-pandas-1.1.5/test/test_basic.py` & `stock-pandas-1.2.0/test/test_basic.py`

 * *Files 3% similar despite different names*

```diff
@@ -48,14 +48,23 @@
 
     stock.alias('close', 'Close')
 
     # get_column should apply alias
     stock.get_column('close')
 
 
+def test_copy(stock):
+    stock['ma:2']
+
+    def ma_size(stock):
+        return stock._stock_columns_info_map.get('ma:2,close').size
+
+    assert ma_size(stock) == ma_size(stock.copy())
+
+
 def test_astype(stock):
     stock = stock.astype({
         'open': 'float',
         'close': 'float'
     })
 
     assert isinstance(stock, StockDataFrame)
```

### Comparing `stock-pandas-1.1.5/test/test_column_info.py` & `stock-pandas-1.2.0/test/test_column_info.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_commands.py` & `stock-pandas-1.2.0/test/test_commands.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_cum_append.py` & `stock-pandas-1.2.0/test/test_cum_append.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_factory.py` & `stock-pandas-1.2.0/test/test_factory.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_manipulate.py` & `stock-pandas-1.2.0/test/test_manipulate.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_parser.py` & `stock-pandas-1.2.0/test/test_parser.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_rolling_calc.py` & `stock-pandas-1.2.0/test/test_rolling_calc.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_time_frame.py` & `stock-pandas-1.2.0/test/test_time_frame.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_tokenizer.py` & `stock-pandas-1.2.0/test/test_tokenizer.py`

 * *Files identical despite different names*

### Comparing `stock-pandas-1.1.5/test/test_truncated.py` & `stock-pandas-1.2.0/test/test_truncated.py`

 * *Files identical despite different names*

