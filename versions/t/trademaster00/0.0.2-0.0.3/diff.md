# Comparing `tmp/trademaster00-0.0.2.tar.gz` & `tmp/trademaster00-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trademaster00-0.0.2.tar", last modified: Fri Apr  7 11:47:15 2023, max compression
+gzip compressed data, was "trademaster00-0.0.3.tar", last modified: Fri Apr  7 11:52:21 2023, max compression
```

## Comparing `trademaster00-0.0.2.tar` & `trademaster00-0.0.3.tar`

### file list

```diff
@@ -1,9 +1,9 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 11:47:15.591621 trademaster00-0.0.2/
--rw-r--r--   0 root         (0) root         (0)    15927 2023-04-07 11:47:15.591621 trademaster00-0.0.2/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-07 11:47:15.591621 trademaster00-0.0.2/setup.cfg
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 11:47:15.591621 trademaster00-0.0.2/trademaster00.egg-info/
--rw-r--r--   0 root         (0) root         (0)    15927 2023-04-07 11:47:15.000000 trademaster00-0.0.2/trademaster00.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      183 2023-04-07 11:47:15.000000 trademaster00-0.0.2/trademaster00.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 11:47:15.000000 trademaster00-0.0.2/trademaster00.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      151 2023-04-07 11:47:15.000000 trademaster00-0.0.2/trademaster00.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 11:47:15.000000 trademaster00-0.0.2/trademaster00.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 11:52:21.834998 trademaster00-0.0.3/
+-rw-r--r--   0 root         (0) root         (0)    15927 2023-04-07 11:52:21.834998 trademaster00-0.0.3/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-07 11:52:21.834998 trademaster00-0.0.3/setup.cfg
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 11:52:21.833998 trademaster00-0.0.3/trademaster00.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    15927 2023-04-07 11:52:21.000000 trademaster00-0.0.3/trademaster00.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      183 2023-04-07 11:52:21.000000 trademaster00-0.0.3/trademaster00.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 11:52:21.000000 trademaster00-0.0.3/trademaster00.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      146 2023-04-07 11:52:21.000000 trademaster00-0.0.3/trademaster00.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 11:52:21.000000 trademaster00-0.0.3/trademaster00.egg-info/top_level.txt
```

### Comparing `trademaster00-0.0.2/PKG-INFO` & `trademaster00-0.0.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster00
-Version: 0.0.2
+Version: 0.0.3
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `trademaster00-0.0.2/trademaster00.egg-info/PKG-INFO` & `trademaster00-0.0.3/trademaster00.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trademaster00
-Version: 0.0.2
+Version: 0.0.3
 Summary: TradeMaster - A platform for algorithmic trading
 Home-page: https://github.com/TradeMaster-NTU/TradeMaster
 Author: NTU_trademaster
 Author-email: TradeMaster.NTU@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

