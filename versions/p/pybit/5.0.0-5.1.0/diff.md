# Comparing `tmp/pybit-5.0.0.tar.gz` & `tmp/pybit-5.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pybit-5.0.0.tar", last modified: Mon Apr  3 15:36:04 2023, max compression
+gzip compressed data, was "pybit-5.1.0.tar", last modified: Thu Apr  6 11:07:14 2023, max compression
```

## Comparing `pybit-5.0.0.tar` & `pybit-5.1.0.tar`

### file list

```diff
@@ -1,46 +1,46 @@
-drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-03 15:36:04.568875 pybit-5.0.0/
--rw-r--r--   0 uk09002ml   (502) staff       (20)    20430 2023-04-03 15:35:39.000000 pybit-5.0.0/CHANGELOG.md
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1217 2022-05-19 15:36:12.000000 pybit-5.0.0/LICENSE
--rw-r--r--   0 uk09002ml   (502) staff       (20)       83 2021-06-17 15:56:06.000000 pybit-5.0.0/MANIFEST.in
--rw-r--r--   0 uk09002ml   (502) staff       (20)     7289 2023-04-03 15:36:04.569828 pybit-5.0.0/PKG-INFO
--rw-r--r--   0 uk09002ml   (502) staff       (20)     5647 2023-04-03 15:35:39.000000 pybit-5.0.0/README.md
-drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-03 15:36:04.486477 pybit-5.0.0/examples/
--rw-r--r--   0 uk09002ml   (502) staff       (20)     6148 2023-04-03 15:33:49.000000 pybit-5.0.0/examples/.DS_Store
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1206 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/direct_session.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1450 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/http_example_explanatory.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      315 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/http_example_quickstart.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1861 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/websocket_example_explanatory.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      258 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/websocket_example_quickstart.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     2313 2023-04-03 15:35:39.000000 pybit-5.0.0/examples/wrapper_class.py
-drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-03 15:36:04.550198 pybit-5.0.0/pybit/
--rw-r--r--   0 uk09002ml   (502) staff       (20)       18 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/__init__.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1964 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_helpers.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)    12518 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_http_manager.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     7591 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_account.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)    13126 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_asset.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     8532 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_market.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     8543 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_position.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     2826 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_spot_leverage_token.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     6113 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_spot_margin_trade.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     8520 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_trade.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     5765 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_v5_user.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)    15535 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/_websocket_stream.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      694 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/account.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1647 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/asset.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1461 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/exceptions.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      856 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/market.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      607 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/position.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      406 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/spot_leverage_token.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      932 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/spot_margin_trade.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      600 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/trade.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)     8680 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/unified_trading.py
--rw-r--r--   0 uk09002ml   (502) staff       (20)      560 2023-04-03 15:35:39.000000 pybit-5.0.0/pybit/user.py
-drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-03 15:36:04.566598 pybit-5.0.0/pybit.egg-info/
--rw-r--r--   0 uk09002ml   (502) staff       (20)     7289 2023-04-03 15:36:04.000000 pybit-5.0.0/pybit.egg-info/PKG-INFO
--rw-r--r--   0 uk09002ml   (502) staff       (20)      926 2023-04-03 15:36:04.000000 pybit-5.0.0/pybit.egg-info/SOURCES.txt
--rw-r--r--   0 uk09002ml   (502) staff       (20)        1 2023-04-03 15:36:04.000000 pybit-5.0.0/pybit.egg-info/dependency_links.txt
--rw-r--r--   0 uk09002ml   (502) staff       (20)        1 2021-07-09 21:25:55.000000 pybit-5.0.0/pybit.egg-info/not-zip-safe
--rw-r--r--   0 uk09002ml   (502) staff       (20)       37 2023-04-03 15:36:04.000000 pybit-5.0.0/pybit.egg-info/requires.txt
--rw-r--r--   0 uk09002ml   (502) staff       (20)        6 2023-04-03 15:36:04.000000 pybit-5.0.0/pybit.egg-info/top_level.txt
--rw-r--r--   0 uk09002ml   (502) staff       (20)      131 2023-04-03 15:36:04.571373 pybit-5.0.0/setup.cfg
--rw-r--r--   0 uk09002ml   (502) staff       (20)     1216 2023-04-03 15:35:39.000000 pybit-5.0.0/setup.py
+drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-06 11:07:14.491958 pybit-5.1.0/
+-rw-r--r--   0 uk09002ml   (502) staff       (20)    20766 2023-04-06 11:06:42.000000 pybit-5.1.0/CHANGELOG.md
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1217 2022-05-19 15:36:12.000000 pybit-5.1.0/LICENSE
+-rw-r--r--   0 uk09002ml   (502) staff       (20)       83 2021-06-17 15:56:06.000000 pybit-5.1.0/MANIFEST.in
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     7944 2023-04-06 11:07:14.492894 pybit-5.1.0/PKG-INFO
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     6294 2023-04-05 16:35:20.000000 pybit-5.1.0/README.md
+drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-06 11:07:14.397335 pybit-5.1.0/examples/
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     6148 2023-04-03 15:36:24.000000 pybit-5.1.0/examples/.DS_Store
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1143 2023-04-06 10:07:37.000000 pybit-5.1.0/examples/direct_session.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1450 2023-04-03 15:35:39.000000 pybit-5.1.0/examples/http_example_explanatory.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      315 2023-04-03 15:35:39.000000 pybit-5.1.0/examples/http_example_quickstart.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1861 2023-04-05 13:48:47.000000 pybit-5.1.0/examples/websocket_example_explanatory.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      258 2023-04-06 10:16:05.000000 pybit-5.1.0/examples/websocket_example_quickstart.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     2256 2023-04-06 10:07:37.000000 pybit-5.1.0/examples/wrapper_class.py
+drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-06 11:07:14.470999 pybit-5.1.0/pybit/
+-rw-r--r--   0 uk09002ml   (502) staff       (20)       18 2023-04-06 11:06:42.000000 pybit-5.1.0/pybit/__init__.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1964 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_helpers.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)    12518 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_http_manager.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     7591 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_account.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)    13126 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_asset.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     8532 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_market.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     8543 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_position.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     2826 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_spot_leverage_token.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     6113 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_spot_margin_trade.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     8520 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_trade.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     5765 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_v5_user.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)    15535 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/_websocket_stream.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      694 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/account.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1647 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/asset.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1461 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/exceptions.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      856 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/market.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      607 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/position.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      406 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/spot_leverage_token.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      932 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/spot_margin_trade.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      600 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/trade.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     8680 2023-04-06 10:22:19.000000 pybit-5.1.0/pybit/unified_trading.py
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      560 2023-04-03 15:35:39.000000 pybit-5.1.0/pybit/user.py
+drwxr-xr-x   0 uk09002ml   (502) staff       (20)        0 2023-04-06 11:07:14.490071 pybit-5.1.0/pybit.egg-info/
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     7944 2023-04-06 11:07:14.000000 pybit-5.1.0/pybit.egg-info/PKG-INFO
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      926 2023-04-06 11:07:14.000000 pybit-5.1.0/pybit.egg-info/SOURCES.txt
+-rw-r--r--   0 uk09002ml   (502) staff       (20)        1 2023-04-06 11:07:14.000000 pybit-5.1.0/pybit.egg-info/dependency_links.txt
+-rw-r--r--   0 uk09002ml   (502) staff       (20)        1 2021-07-09 21:25:55.000000 pybit-5.1.0/pybit.egg-info/not-zip-safe
+-rw-r--r--   0 uk09002ml   (502) staff       (20)       37 2023-04-06 11:07:14.000000 pybit-5.1.0/pybit.egg-info/requires.txt
+-rw-r--r--   0 uk09002ml   (502) staff       (20)        6 2023-04-06 11:07:14.000000 pybit-5.1.0/pybit.egg-info/top_level.txt
+-rw-r--r--   0 uk09002ml   (502) staff       (20)      131 2023-04-06 11:07:14.495136 pybit-5.1.0/setup.cfg
+-rw-r--r--   0 uk09002ml   (502) staff       (20)     1216 2023-04-06 11:06:42.000000 pybit-5.1.0/setup.py
```

### Comparing `pybit-5.0.0/CHANGELOG.md` & `pybit-5.1.0/CHANGELOG.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,26 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
 The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
 and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
 
+## [5.1.0] - 2023-04-06
+### Added
+- HTTP endpoints to the `copy_trading` module
+
+### Modified
+- Docstrings in the `copy_trading` module to make it easier to find the API documentation for reference
+- Example files
+
+### Fixed
+- `ticker_stream` method in the `unified_trading` module, which was subscribing to the wrong WebSocket topic
+
+
 ## [5.0.0] - 2023-04-03
 This version upgrades pybit to Bybit's [version 5 (v5) APIs](https://bybit-exchange.github.io/docs/v5/intro). It supports both [Unified Trading Accounts](https://www.bybit.com/en-US/help-center/s/article/Introduction-to-Bybit-Unified-Trading-Account) (UTA) and non-UTA accounts. Bybit is not expected to develop any more major API versions in the future, so Bybit's v5 API (and subsequently, pybit's 5.0.0) is expected to be supported in the long-term.
 
 See the [examples folder](https://github.com/bybit-exchange/pybit/tree/master/examples) for examples on how to interact with the latest modules.
 
 ### Added
 - Bybit's v5 HTTP and WebSocket APIs in the `unified_trading` module. See what markets All-In-One V5 API supports in the [upgrade guide](https://bybit-exchange.github.io/docs/v5/upgrade-guide).
```

### Comparing `pybit-5.0.0/LICENSE` & `pybit-5.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/PKG-INFO` & `pybit-5.1.0/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 Metadata-Version: 2.1
 Name: pybit
-Version: 5.0.0
+Version: 5.1.0
 Summary: Python3 Bybit HTTP/WebSocket API Connector
 Home-page: https://github.com/bybit-exchange/pybit
 Author: Dexter Dickinson
 Author-email: dexter.dickinson@bybit.com
 License: MIT License
 Description: # pybit
         <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
-        [![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
+        [![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
         <!-- ALL-CONTRIBUTORS-BADGE:END -->
         
         [![Build Status](https://img.shields.io/pypi/pyversions/pybit)](https://www.python.org/downloads/)
         [![Build Status](https://img.shields.io/pypi/v/pybit)](https://pypi.org/project/pybit/)
-        [![Build Status](https://travis-ci.org/verata-veritatis/pybit.svg?branch=master)](https://travis-ci.org/verata-veritatis/pybit)
         ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
         
         Official Python3 API connector for Bybit's HTTP and WebSockets APIs.
         
         ## Table of Contents
         
         - [About](#about)
@@ -91,19 +90,21 @@
         Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
         
         <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
         <!-- prettier-ignore-start -->
         <!-- markdownlint-disable -->
         <table>
           <tr>
-            <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
-             <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=APF20" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=cameronhh" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=tomcru" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
+            <td align="center"><a href="https://github.com/dextertd"><img src="https://avatars.githubusercontent.com/u/54495183?v=4" width="100px;" alt=""/><br /><sub><b>dextertd</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Documentation">📖</a></td>
+            <td align="center"><a href="https://github.com/ervuks"><img src="https://avatars.githubusercontent.com/u/17198438?v=4" width="100px;" alt=""/><br /><sub><b>ervuks</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Documentation">📖</a></td></td>
+            <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
+            <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=APF20" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=cameronhh" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=tomcru" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
           </tr>
         </table>
         
         <!-- markdownlint-enable -->
         <!-- prettier-ignore-end -->
         <!-- ALL-CONTRIBUTORS-LIST:END -->
```

### Comparing `pybit-5.0.0/README.md` & `pybit-5.1.0/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 # pybit
 <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
-[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
+[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
 <!-- ALL-CONTRIBUTORS-BADGE:END -->
 
 [![Build Status](https://img.shields.io/pypi/pyversions/pybit)](https://www.python.org/downloads/)
 [![Build Status](https://img.shields.io/pypi/v/pybit)](https://pypi.org/project/pybit/)
-[![Build Status](https://travis-ci.org/verata-veritatis/pybit.svg?branch=master)](https://travis-ci.org/verata-veritatis/pybit)
 ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
 
 Official Python3 API connector for Bybit's HTTP and WebSockets APIs.
 
 ## Table of Contents
 
 - [About](#about)
@@ -83,19 +82,21 @@
 Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
 
 <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
 <!-- prettier-ignore-start -->
 <!-- markdownlint-disable -->
 <table>
   <tr>
-    <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
-     <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=APF20" title="Code">💻</a></td>
-     <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=cameronhh" title="Code">💻</a></td>
-     <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=tomcru" title="Code">💻</a></td>
-     <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
+    <td align="center"><a href="https://github.com/dextertd"><img src="https://avatars.githubusercontent.com/u/54495183?v=4" width="100px;" alt=""/><br /><sub><b>dextertd</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Documentation">📖</a></td>
+    <td align="center"><a href="https://github.com/ervuks"><img src="https://avatars.githubusercontent.com/u/17198438?v=4" width="100px;" alt=""/><br /><sub><b>ervuks</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Documentation">📖</a></td></td>
+    <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
+    <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=APF20" title="Code">💻</a></td>
+    <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=cameronhh" title="Code">💻</a></td>
+    <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=tomcru" title="Code">💻</a></td>
+    <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
   </tr>
 </table>
 
 <!-- markdownlint-enable -->
 <!-- prettier-ignore-end -->
 <!-- ALL-CONTRIBUTORS-LIST:END -->
```

#### html2text {}

```diff
@@ -1,31 +1,29 @@
-# pybit  [![All Contributors](https://img.shields.io/badge/all_contributors-3-
+# pybit  [![All Contributors](https://img.shields.io/badge/all_contributors-2-
 orange.svg?style=flat-square)](#contributors-)  [![Build Status](https://
 img.shields.io/pypi/pyversions/pybit)](https://www.python.org/downloads/) [!
 [Build Status](https://img.shields.io/pypi/v/pybit)](https://pypi.org/project/
-pybit/) [![Build Status](https://travis-ci.org/verata-veritatis/
-pybit.svg?branch=master)](https://travis-ci.org/verata-veritatis/pybit) !
-[contributions welcome](https://img.shields.io/badge/contributions-welcome-
-brightgreen.svg?style=flat) Official Python3 API connector for Bybit's HTTP and
-WebSockets APIs. ## Table of Contents - [About](#about) - [Development]
-(#development) - [Installation](#installation) - [Usage](#usage) - [Contact]
-(#contact) - [Contributors](#contributors) - [Donations](#donations) ## About
-Put simply, `pybit` (Python + Bybit) is the official lightweight one-stop-shop
-module for the Bybit HTTP and WebSocket APIs. Originally created by [Verata
-Veritatis](https://github.com/verata-veritatis), it's now maintained by Bybit
-employees - however, you're still welcome to contribute! It was designed with
-the following vision in mind: > I was personally never a fan of auto-generated
-connectors that used a mosh-pit of various modules you didn't want (sorry,
-`bravado`) and wanted to build my own Python3-dedicated connector with very
-little external resources. The goal of the connector is to provide traders and
-developers with an easy-to-use high-performing module that has an active issue
-and discussion board leading to consistent improvements. ## Development `pybit`
-is being actively developed, and new Bybit API changes should arrive on `pybit`
-very quickly. `pybit` uses `requests` and `websocket-client` for its methods,
-alongside other built-in modules. Anyone is welcome to branch/fork the
+pybit/) ![contributions welcome](https://img.shields.io/badge/contributions-
+welcome-brightgreen.svg?style=flat) Official Python3 API connector for Bybit's
+HTTP and WebSockets APIs. ## Table of Contents - [About](#about) -
+[Development](#development) - [Installation](#installation) - [Usage](#usage) -
+[Contact](#contact) - [Contributors](#contributors) - [Donations](#donations)
+## About Put simply, `pybit` (Python + Bybit) is the official lightweight one-
+stop-shop module for the Bybit HTTP and WebSocket APIs. Originally created by
+[Verata Veritatis](https://github.com/verata-veritatis), it's now maintained by
+Bybit employees - however, you're still welcome to contribute! It was designed
+with the following vision in mind: > I was personally never a fan of auto-
+generated connectors that used a mosh-pit of various modules you didn't want
+(sorry, `bravado`) and wanted to build my own Python3-dedicated connector with
+very little external resources. The goal of the connector is to provide traders
+and developers with an easy-to-use high-performing module that has an active
+issue and discussion board leading to consistent improvements. ## Development
+`pybit` is being actively developed, and new Bybit API changes should arrive on
+`pybit` very quickly. `pybit` uses `requests` and `websocket-client` for its
+methods, alongside other built-in modules. Anyone is welcome to branch/fork the
 repository and add their own upgrades. If you think you've made substantial
 improvements to the module, submit a pull request and we'll gladly take a look.
 ## Installation `pybit` requires Python 3.9.1 or higher. The module can be
 installed manually or via [PyPI](https://pypi.org/project/pybit/) with `pip`:
 ``` pip install pybit ``` ## Usage You can retrieve a specific market like so:
 ```python from pybit.unified_trading import HTTP ``` Create an HTTP session and
 connect via WebSocket for Inverse on mainnet: ```python session = HTTP
@@ -41,13 +39,15 @@
 the list of endpoints below for more information on available endpoints and
 methods. Usage examples on the `HTTP` methods can be found in the [examples
 folder](https://github.com/bybit-exchange/pybit/tree/master/examples). ##
 Contact You can reach out for support on the [BybitAPI Telegram](https://t.me/
 BybitAPI) group chat. ## Contributors Thanks goes to these wonderful people (
 [emoji key](https://allcontributors.org/docs/en/emoji-key)):
 
-verata-veritatis   APF20   Cameron_Harder-Hutton Tom_Rumpf Todd_Conley
-
-    ð» ð�  ð�        ð»        ð»   ð¤
+                                                               Cameron    Tom      Todd
+    dextertd           ervuks       verata-veritatis   APF20   Harder-   Rumpf    Conley
+                                                                Hutton
+    ð» ð�    ð» ð�    ð» ð�  ð�           ð�  ð¤
+                                                                 ð»
    This project follows the [all-contributors](https://github.com/all-
 contributors/all-contributors) specification. Contributions of any kind
 welcome!
```

### Comparing `pybit-5.0.0/examples/.DS_Store` & `pybit-5.1.0/examples/.DS_Store`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/examples/direct_session.py` & `pybit-5.1.0/examples/direct_session.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 from pybit.unified_trading import HTTP
 
 
-BYBIT_API_KEY = "<account_api_key>"
-BYBIT_API_SECRET = "<account_api_secret>"
-BYBIT_TESTNET_ENDPOINT = "https://api-testnet.bybit.com"
-BYBIT_ENDPOINT = "https://api.bybit.com"
+BYBIT_API_KEY = "api_key"
+BYBIT_API_SECRET = "api_secret"
+TESTNET = True  # True means your API keys were generated on testnet.bybit.com
 
 
 # Create direct HTTP session instance
 
 session = HTTP(
     api_key=BYBIT_API_KEY,
     api_secret=BYBIT_API_SECRET,
-    endpoint=BYBIT_TESTNET_ENDPOINT,
+    testnet=TESTNET,
 )
 
 # Place order
 
 response = session.place_order(
     category="spot",
     symbol="ETHUSDT",
@@ -43,16 +42,16 @@
             orderId=order["orderId"],
         )
 
 
 # Batch cancel orders
 
 orders_to_cancel = [
-    {"category": "linear", "symbol": o["symbol"], "orderId": o["orderId"]}
+    {"category": "option", "symbol": o["symbol"], "orderId": o["orderId"]}
     for o in response["result"]["list"]
-    if o["orderStatus"] == "Untriggered"
+    if o["orderStatus"] == "New"
 ]
 
 response = session.cancel_batch_order(
-    category="linear",
+    category="option",
     request=orders_to_cancel,
 )
```

### Comparing `pybit-5.0.0/examples/http_example_explanatory.py` & `pybit-5.1.0/examples/http_example_explanatory.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/examples/websocket_example_explanatory.py` & `pybit-5.1.0/examples/websocket_example_explanatory.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/examples/wrapper_class.py` & `pybit-5.1.0/examples/wrapper_class.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,27 +1,26 @@
 from pybit.unified_trading import HTTP
 
 
-BYBIT_API_KEY = "<account_api_key>"
-BYBIT_API_SECRET = "<account_api_secret>"
-BYBIT_TESTNET_ENDPOINT = "https://api-testnet.bybit.com"
-BYBIT_ENDPOINT = "https://api.bybit.com"
+BYBIT_API_KEY = "api_key"
+BYBIT_API_SECRET = "api_secret"
+TESTNET = True  # True means your API keys were generated on testnet.bybit.com
 
 
 class BybitWrapper:
     def __init__(
         self,
         api_key: str = None,
         api_secret: str = None,
-        endpoint: str = None,
+        testnet: bool = None,
     ):
         self.instance = HTTP(
             api_key=api_key,
             api_secret=api_secret,
-            endpoint=endpoint,
+            testnet=testnet,
             log_requests=True,
         )
 
     def get_max_leverage(self, category: str, symbol: str):
         """
         Get max leverage for symbol in category
         """
@@ -76,12 +75,12 @@
 
 
 # Initialize wrapper instance
 
 wrapper = BybitWrapper(
     api_key=BYBIT_API_KEY,
     api_secret=BYBIT_API_SECRET,
-    endpoint=BYBIT_TESTNET_ENDPOINT,
+    testnet=TESTNET,
 )
 
 # Actual usage
 response = wrapper.get_realtime_orders(category="linear", symbol="ETHUSDT")
```

### Comparing `pybit-5.0.0/pybit/_helpers.py` & `pybit-5.1.0/pybit/_helpers.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_http_manager.py` & `pybit-5.1.0/pybit/_http_manager.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_account.py` & `pybit-5.1.0/pybit/_v5_account.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_asset.py` & `pybit-5.1.0/pybit/_v5_asset.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_market.py` & `pybit-5.1.0/pybit/_v5_market.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_position.py` & `pybit-5.1.0/pybit/_v5_position.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_spot_leverage_token.py` & `pybit-5.1.0/pybit/_v5_spot_leverage_token.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_spot_margin_trade.py` & `pybit-5.1.0/pybit/_v5_spot_margin_trade.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_trade.py` & `pybit-5.1.0/pybit/_v5_trade.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_v5_user.py` & `pybit-5.1.0/pybit/_v5_user.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/_websocket_stream.py` & `pybit-5.1.0/pybit/_websocket_stream.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/account.py` & `pybit-5.1.0/pybit/account.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/asset.py` & `pybit-5.1.0/pybit/asset.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/exceptions.py` & `pybit-5.1.0/pybit/exceptions.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/market.py` & `pybit-5.1.0/pybit/market.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/position.py` & `pybit-5.1.0/pybit/position.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/spot_margin_trade.py` & `pybit-5.1.0/pybit/spot_margin_trade.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/trade.py` & `pybit-5.1.0/pybit/trade.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/unified_trading.py` & `pybit-5.1.0/pybit/unified_trading.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit/user.py` & `pybit-5.1.0/pybit/user.py`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/pybit.egg-info/PKG-INFO` & `pybit-5.1.0/pybit.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,23 +1,22 @@
 Metadata-Version: 2.1
 Name: pybit
-Version: 5.0.0
+Version: 5.1.0
 Summary: Python3 Bybit HTTP/WebSocket API Connector
 Home-page: https://github.com/bybit-exchange/pybit
 Author: Dexter Dickinson
 Author-email: dexter.dickinson@bybit.com
 License: MIT License
 Description: # pybit
         <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
-        [![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
+        [![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
         <!-- ALL-CONTRIBUTORS-BADGE:END -->
         
         [![Build Status](https://img.shields.io/pypi/pyversions/pybit)](https://www.python.org/downloads/)
         [![Build Status](https://img.shields.io/pypi/v/pybit)](https://pypi.org/project/pybit/)
-        [![Build Status](https://travis-ci.org/verata-veritatis/pybit.svg?branch=master)](https://travis-ci.org/verata-veritatis/pybit)
         ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
         
         Official Python3 API connector for Bybit's HTTP and WebSockets APIs.
         
         ## Table of Contents
         
         - [About](#about)
@@ -91,19 +90,21 @@
         Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
         
         <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
         <!-- prettier-ignore-start -->
         <!-- markdownlint-disable -->
         <table>
           <tr>
-            <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/verata-veritatis/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
-             <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=APF20" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=cameronhh" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/verata-veritatis/pybit/commits?author=tomcru" title="Code">💻</a></td>
-             <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
+            <td align="center"><a href="https://github.com/dextertd"><img src="https://avatars.githubusercontent.com/u/54495183?v=4" width="100px;" alt=""/><br /><sub><b>dextertd</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=dextertd" title="Documentation">📖</a></td>
+            <td align="center"><a href="https://github.com/ervuks"><img src="https://avatars.githubusercontent.com/u/17198438?v=4" width="100px;" alt=""/><br /><sub><b>ervuks</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=ervuks" title="Documentation">📖</a></td></td>
+            <td align="center"><a href="https://github.com/verata-veritatis"><img src="https://avatars0.githubusercontent.com/u/9677388?v=4" width="100px;" alt=""/><br /><sub><b>verata-veritatis</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Code">💻</a> <a href="https://github.com/bybit-exchange/pybit/commits?author=verata-veritatis" title="Documentation">📖</a></td>
+            <td align="center"><a href="https://github.com/APF20"><img src="https://avatars0.githubusercontent.com/u/74583612?v=4" width="100px;" alt=""/><br /><sub><b>APF20</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=APF20" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/cameronhh"><img src="https://avatars0.githubusercontent.com/u/30434979?v=4" width="100px;" alt=""/><br /><sub><b>Cameron Harder-Hutton</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=cameronhh" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/tomcru"><img src="https://avatars0.githubusercontent.com/u/35841182?v=4" width="100px;" alt=""/><br /><sub><b>Tom Rumpf</b></sub></a><br /><a href="https://github.com/bybit-exchange/pybit/commits?author=tomcru" title="Code">💻</a></td>
+            <td align="center"><a href="https://github.com/tconley"><img src="https://avatars1.githubusercontent.com/u/1893207?v=4" width="100px;" alt=""/><br /><sub><b>Todd Conley</b></sub></a><br /><a href="https://github.com/tconley/pybit/commits?author=tconley" title="Ideas">🤔</a></td>
           </tr>
         </table>
         
         <!-- markdownlint-enable -->
         <!-- prettier-ignore-end -->
         <!-- ALL-CONTRIBUTORS-LIST:END -->
```

### Comparing `pybit-5.0.0/pybit.egg-info/SOURCES.txt` & `pybit-5.1.0/pybit.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pybit-5.0.0/setup.py` & `pybit-5.1.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 here = path.abspath(path.dirname(__file__))
 
 with open(path.join(here, "README.md"), encoding="utf-8") as f:
     long_description = f.read()
 
 setup(
     name='pybit',
-    version='5.0.0',
+    version='5.1.0',
     description='Python3 Bybit HTTP/WebSocket API Connector', 
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/bybit-exchange/pybit",
     license="MIT License",
     author="Dexter Dickinson",
     author_email="dexter.dickinson@bybit.com",
```

