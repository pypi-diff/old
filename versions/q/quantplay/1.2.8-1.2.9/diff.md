# Comparing `tmp/quantplay-1.2.8.tar.gz` & `tmp/quantplay-1.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quantplay-1.2.8.tar", last modified: Tue Mar 14 05:23:27 2023, max compression
+gzip compressed data, was "quantplay-1.2.9.tar", last modified: Tue Mar 14 05:33:14 2023, max compression
```

## Comparing `quantplay-1.2.8.tar` & `quantplay-1.2.9.tar`

### file list

```diff
@@ -1,125 +1,125 @@
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.758303 quantplay-1.2.8/
--rw-r--r--   0 ashok      (502) staff       (20)      662 2023-03-14 05:23:27.758360 quantplay-1.2.8/PKG-INFO
--rw-r--r--   0 ashok      (502) staff       (20)      494 2022-04-17 10:54:24.000000 quantplay-1.2.8/README.md
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.746107 quantplay-1.2.8/quantplay/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.747111 quantplay-1.2.8/quantplay/backtest/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/backtest/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    17260 2023-01-19 02:56:14.000000 quantplay-1.2.8/quantplay/backtest/backtest_trades.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.748850 quantplay-1.2.8/quantplay/broker/
--rw-------   0 ashok      (502) staff       (20)        0 2022-09-14 14:42:56.000000 quantplay-1.2.8/quantplay/broker/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    10902 2023-02-18 12:07:06.000000 quantplay-1.2.8/quantplay/broker/angelone.py
--rw-r--r--   0 ashok      (502) staff       (20)     3738 2022-09-17 04:21:35.000000 quantplay-1.2.8/quantplay/broker/broker_client.py
--rw-r--r--   0 ashok      (502) staff       (20)       87 2022-09-14 14:47:24.000000 quantplay-1.2.8/quantplay/broker/client.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.749129 quantplay-1.2.8/quantplay/broker/finvasia_utils/
--rw-------   0 ashok      (502) staff       (20)        0 2022-12-31 11:10:39.000000 quantplay-1.2.8/quantplay/broker/finvasia_utils/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     2576 2023-02-11 04:10:25.000000 quantplay-1.2.8/quantplay/broker/finvasia_utils/shoonya.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.749368 quantplay-1.2.8/quantplay/broker/generics/
--rw-------   0 ashok      (502) staff       (20)        0 2022-09-16 14:05:50.000000 quantplay-1.2.8/quantplay/broker/generics/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    18638 2023-02-27 07:04:06.000000 quantplay-1.2.8/quantplay/broker/generics/broker.py
--rw-r--r--   0 ashok      (502) staff       (20)     2047 2023-01-22 16:18:04.000000 quantplay-1.2.8/quantplay/broker/kite_utils.py
--rw-r--r--   0 ashok      (502) staff       (20)    31836 2023-02-27 07:02:13.000000 quantplay-1.2.8/quantplay/broker/motilal.py
--rw-r--r--   0 ashok      (502) staff       (20)    16662 2023-03-14 05:22:05.000000 quantplay-1.2.8/quantplay/broker/shoonya.py
--rw-r--r--   0 ashok      (502) staff       (20)     2845 2023-01-30 13:09:52.000000 quantplay-1.2.8/quantplay/broker/symphony.py
--rw-r--r--   0 ashok      (502) staff       (20)    18183 2023-02-27 07:32:47.000000 quantplay-1.2.8/quantplay/broker/zerodha.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.749542 quantplay-1.2.8/quantplay/brokerage/
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.8/quantplay/brokerage/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.749759 quantplay-1.2.8/quantplay/brokerage/angelone/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 06:26:20.000000 quantplay-1.2.8/quantplay/brokerage/angelone/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    10989 2022-08-01 14:56:00.000000 quantplay-1.2.8/quantplay/brokerage/angelone/angel_broker.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.750038 quantplay-1.2.8/quantplay/brokerage/generics/
--rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/brokerage/generics/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    28033 2022-07-12 08:39:40.000000 quantplay-1.2.8/quantplay/brokerage/generics/broker.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.750440 quantplay-1.2.8/quantplay/brokerage/zerodha/
--rw-r--r--   0 ashok      (502) staff       (20)    17401 2022-09-21 18:14:33.000000 quantplay-1.2.8/quantplay/brokerage/zerodha/ZBroker.py
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.8/quantplay/brokerage/zerodha/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.750865 quantplay-1.2.8/quantplay/config/
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.8/quantplay/config/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     1461 2022-06-22 08:09:40.000000 quantplay-1.2.8/quantplay/config/qplay_config.py
--rw-r--r--   0 ashok      (502) staff       (20)     1127 2022-06-15 08:16:17.000000 quantplay-1.2.8/quantplay/create_sample_data.py
--rw-r--r--   0 ashok      (502) staff       (20)     1724 2022-12-19 09:25:50.000000 quantplay-1.2.8/quantplay/data_modify_script.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.751327 quantplay-1.2.8/quantplay/exception/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/exception/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     2162 2022-10-03 07:10:49.000000 quantplay-1.2.8/quantplay/exception/exceptions.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.751633 quantplay-1.2.8/quantplay/executor/
--rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/executor/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     6064 2022-06-28 05:06:04.000000 quantplay-1.2.8/quantplay/executor/strategy_executor.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.751777 quantplay-1.2.8/quantplay/model/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/model/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.752423 quantplay-1.2.8/quantplay/model/exchange/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/model/exchange/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     1472 2022-06-23 07:31:05.000000 quantplay-1.2.8/quantplay/model/exchange/instrument.py
--rw-r--r--   0 ashok      (502) staff       (20)     8628 2023-01-09 04:21:22.000000 quantplay-1.2.8/quantplay/model/exchange/order.py
--rw-r--r--   0 ashok      (502) staff       (20)     3238 2022-07-12 07:44:24.000000 quantplay-1.2.8/quantplay/model/exchange/tick.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.752669 quantplay-1.2.8/quantplay/model/strategy/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/model/strategy/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)      206 2022-04-17 10:54:24.000000 quantplay-1.2.8/quantplay/model/strategy/strategy_response.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.752813 quantplay-1.2.8/quantplay/oms/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-27 04:43:46.000000 quantplay-1.2.8/quantplay/oms/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.753152 quantplay-1.2.8/quantplay/order_execution/
--rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/order_execution/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     2048 2022-04-20 04:11:58.000000 quantplay-1.2.8/quantplay/order_execution/execution_algorithm.py
--rw-r--r--   0 ashok      (502) staff       (20)     1281 2022-04-19 06:42:52.000000 quantplay-1.2.8/quantplay/order_execution/mean_price.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.753525 quantplay-1.2.8/quantplay/reporting/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/reporting/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    10780 2023-01-19 02:56:14.000000 quantplay-1.2.8/quantplay/reporting/strategy_report.py
--rw-r--r--   0 ashok      (502) staff       (20)     1510 2022-06-06 18:04:02.000000 quantplay-1.2.8/quantplay/reporting/visuals.py
--rw-r--r--   0 ashok      (502) staff       (20)      231 2023-01-08 06:14:00.000000 quantplay-1.2.8/quantplay/service.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754046 quantplay-1.2.8/quantplay/services/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/services/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    17986 2023-01-23 02:26:35.000000 quantplay-1.2.8/quantplay/services/market.py
--rw-r--r--   0 ashok      (502) staff       (20)     2798 2023-01-08 06:12:37.000000 quantplay-1.2.8/quantplay/services/tradelens.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754373 quantplay-1.2.8/quantplay/strategies/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:35:41.000000 quantplay-1.2.8/quantplay/strategies/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754473 quantplay-1.2.8/quantplay/strategies/equities/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:48:09.000000 quantplay-1.2.8/quantplay/strategies/equities/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754573 quantplay-1.2.8/quantplay/strategies/equities/intraday/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:48:26.000000 quantplay-1.2.8/quantplay/strategies/equities/intraday/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754673 quantplay-1.2.8/quantplay/strategies/equities/overnight/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:49:47.000000 quantplay-1.2.8/quantplay/strategies/equities/overnight/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754772 quantplay-1.2.8/quantplay/strategies/futures/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-24 08:54:42.000000 quantplay-1.2.8/quantplay/strategies/futures/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754873 quantplay-1.2.8/quantplay/strategies/futures/overnight/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-24 08:54:48.000000 quantplay-1.2.8/quantplay/strategies/futures/overnight/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.754979 quantplay-1.2.8/quantplay/strategies/options/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:35:52.000000 quantplay-1.2.8/quantplay/strategies/options/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.755488 quantplay-1.2.8/quantplay/strategies/options/intraday/
--rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:36:03.000000 quantplay-1.2.8/quantplay/strategies/options/intraday/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)     1958 2022-09-14 18:05:01.000000 quantplay-1.2.8/quantplay/strategies/options/intraday/ladder.py
--rw-r--r--   0 ashok      (502) staff       (20)     2675 2022-06-25 11:41:44.000000 quantplay-1.2.8/quantplay/strategies/options/intraday/musk.py
--rw-r--r--   0 ashok      (502) staff       (20)      403 2022-09-17 07:36:48.000000 quantplay-1.2.8/quantplay/strategies/options/intraday/short_straddle.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.755745 quantplay-1.2.8/quantplay/strategy/
--rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/strategy/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)    11810 2022-10-21 05:19:41.000000 quantplay-1.2.8/quantplay/strategy/base.py
--rw-r--r--   0 ashok      (502) staff       (20)      214 2022-06-28 09:52:29.000000 quantplay-1.2.8/quantplay/strategy_run.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.757047 quantplay-1.2.8/quantplay/utils/
--rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.8/quantplay/utils/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)      723 2022-04-17 10:54:24.000000 quantplay-1.2.8/quantplay/utils/config_util.py
--rw-r--r--   0 ashok      (502) staff       (20)    23741 2022-09-18 09:02:50.000000 quantplay-1.2.8/quantplay/utils/constant.py
--rw-r--r--   0 ashok      (502) staff       (20)     5276 2022-08-22 16:31:03.000000 quantplay-1.2.8/quantplay/utils/data_utils.py
--rw-r--r--   0 ashok      (502) staff       (20)      711 2022-04-17 10:54:24.000000 quantplay-1.2.8/quantplay/utils/exchange.py
--rw-r--r--   0 ashok      (502) staff       (20)      517 2022-12-30 04:31:22.000000 quantplay-1.2.8/quantplay/utils/number_utils.py
--rw-r--r--   0 ashok      (502) staff       (20)      458 2023-01-29 14:04:22.000000 quantplay-1.2.8/quantplay/utils/pickle_utils.py
--rw-r--r--   0 ashok      (502) staff       (20)     1207 2023-01-16 02:41:32.000000 quantplay-1.2.8/quantplay/utils/selenium_utils.py
--rw-r--r--   0 ashok      (502) staff       (20)     4094 2022-04-17 12:50:03.000000 quantplay-1.2.8/quantplay/utils/transaction_utils.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.746865 quantplay-1.2.8/quantplay.egg-info/
--rw-r--r--   0 ashok      (502) staff       (20)      662 2023-03-14 05:23:27.000000 quantplay-1.2.8/quantplay.egg-info/PKG-INFO
--rw-r--r--   0 ashok      (502) staff       (20)     2972 2023-03-14 05:23:27.000000 quantplay-1.2.8/quantplay.egg-info/SOURCES.txt
--rw-r--r--   0 ashok      (502) staff       (20)        1 2023-03-14 05:23:27.000000 quantplay-1.2.8/quantplay.egg-info/dependency_links.txt
--rw-r--r--   0 ashok      (502) staff       (20)      177 2023-03-14 05:23:27.000000 quantplay-1.2.8/quantplay.egg-info/requires.txt
--rw-r--r--   0 ashok      (502) staff       (20)       15 2023-03-14 05:23:27.000000 quantplay-1.2.8/quantplay.egg-info/top_level.txt
--rw-r--r--   0 ashok      (502) staff       (20)       49 2023-03-14 05:23:27.758587 quantplay-1.2.8/setup.cfg
--rw-r--r--   0 ashok      (502) staff       (20)      875 2023-03-14 05:23:24.000000 quantplay-1.2.8/setup.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.757278 quantplay-1.2.8/test/
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-15 16:22:35.000000 quantplay-1.2.8/test/__init__.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.757513 quantplay-1.2.8/test/broker/
--rw-r--r--   0 ashok      (502) staff       (20)        0 2022-12-31 12:18:16.000000 quantplay-1.2.8/test/broker/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)      220 2022-12-31 14:39:54.000000 quantplay-1.2.8/test/broker/finvasia.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.757771 quantplay-1.2.8/test/executor/
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-17 06:24:33.000000 quantplay-1.2.8/test/executor/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)      304 2022-04-17 10:58:40.000000 quantplay-1.2.8/test/executor/strategy_executor.py
-drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:23:27.758176 quantplay-1.2.8/test/strategy/
--rw-------   0 ashok      (502) staff       (20)        0 2022-04-15 16:23:22.000000 quantplay-1.2.8/test/strategy/__init__.py
--rw-r--r--   0 ashok      (502) staff       (20)      292 2022-04-17 10:54:24.000000 quantplay-1.2.8/test/strategy/base.py
--rw-r--r--   0 ashok      (502) staff       (20)     2194 2022-04-20 14:52:19.000000 quantplay-1.2.8/test/strategy/sample_strategy.py
--rw-r--r--   0 ashok      (502) staff       (20)     3302 2022-11-15 06:12:07.000000 quantplay-1.2.8/test/test_motilal.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.387924 quantplay-1.2.9/
+-rw-r--r--   0 ashok      (502) staff       (20)      662 2023-03-14 05:33:14.387984 quantplay-1.2.9/PKG-INFO
+-rw-r--r--   0 ashok      (502) staff       (20)      494 2022-04-17 10:54:24.000000 quantplay-1.2.9/README.md
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.376320 quantplay-1.2.9/quantplay/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.377311 quantplay-1.2.9/quantplay/backtest/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/backtest/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    17260 2023-01-19 02:56:14.000000 quantplay-1.2.9/quantplay/backtest/backtest_trades.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.378998 quantplay-1.2.9/quantplay/broker/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-09-14 14:42:56.000000 quantplay-1.2.9/quantplay/broker/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    10902 2023-02-18 12:07:06.000000 quantplay-1.2.9/quantplay/broker/angelone.py
+-rw-r--r--   0 ashok      (502) staff       (20)     3738 2022-09-17 04:21:35.000000 quantplay-1.2.9/quantplay/broker/broker_client.py
+-rw-r--r--   0 ashok      (502) staff       (20)       87 2022-09-14 14:47:24.000000 quantplay-1.2.9/quantplay/broker/client.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.379281 quantplay-1.2.9/quantplay/broker/finvasia_utils/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-12-31 11:10:39.000000 quantplay-1.2.9/quantplay/broker/finvasia_utils/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2576 2023-02-11 04:10:25.000000 quantplay-1.2.9/quantplay/broker/finvasia_utils/shoonya.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.379531 quantplay-1.2.9/quantplay/broker/generics/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-09-16 14:05:50.000000 quantplay-1.2.9/quantplay/broker/generics/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    18638 2023-02-27 07:04:06.000000 quantplay-1.2.9/quantplay/broker/generics/broker.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2047 2023-01-22 16:18:04.000000 quantplay-1.2.9/quantplay/broker/kite_utils.py
+-rw-r--r--   0 ashok      (502) staff       (20)    31836 2023-02-27 07:02:13.000000 quantplay-1.2.9/quantplay/broker/motilal.py
+-rw-r--r--   0 ashok      (502) staff       (20)    16789 2023-03-14 05:32:26.000000 quantplay-1.2.9/quantplay/broker/shoonya.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2845 2023-01-30 13:09:52.000000 quantplay-1.2.9/quantplay/broker/symphony.py
+-rw-r--r--   0 ashok      (502) staff       (20)    18183 2023-02-27 07:32:47.000000 quantplay-1.2.9/quantplay/broker/zerodha.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.379708 quantplay-1.2.9/quantplay/brokerage/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.9/quantplay/brokerage/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.379908 quantplay-1.2.9/quantplay/brokerage/angelone/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 06:26:20.000000 quantplay-1.2.9/quantplay/brokerage/angelone/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    10989 2022-08-01 14:56:00.000000 quantplay-1.2.9/quantplay/brokerage/angelone/angel_broker.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.380158 quantplay-1.2.9/quantplay/brokerage/generics/
+-rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/brokerage/generics/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    28033 2022-07-12 08:39:40.000000 quantplay-1.2.9/quantplay/brokerage/generics/broker.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.380536 quantplay-1.2.9/quantplay/brokerage/zerodha/
+-rw-r--r--   0 ashok      (502) staff       (20)    17401 2022-09-21 18:14:33.000000 quantplay-1.2.9/quantplay/brokerage/zerodha/ZBroker.py
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.9/quantplay/brokerage/zerodha/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.380730 quantplay-1.2.9/quantplay/config/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-07 17:21:33.000000 quantplay-1.2.9/quantplay/config/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1461 2022-06-22 08:09:40.000000 quantplay-1.2.9/quantplay/config/qplay_config.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1127 2022-06-15 08:16:17.000000 quantplay-1.2.9/quantplay/create_sample_data.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1724 2022-12-19 09:25:50.000000 quantplay-1.2.9/quantplay/data_modify_script.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.380965 quantplay-1.2.9/quantplay/exception/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/exception/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2162 2022-10-03 07:10:49.000000 quantplay-1.2.9/quantplay/exception/exceptions.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.381199 quantplay-1.2.9/quantplay/executor/
+-rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/executor/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     6064 2022-06-28 05:06:04.000000 quantplay-1.2.9/quantplay/executor/strategy_executor.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.381335 quantplay-1.2.9/quantplay/model/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/model/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.381810 quantplay-1.2.9/quantplay/model/exchange/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/model/exchange/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1472 2022-06-23 07:31:05.000000 quantplay-1.2.9/quantplay/model/exchange/instrument.py
+-rw-r--r--   0 ashok      (502) staff       (20)     8628 2023-01-09 04:21:22.000000 quantplay-1.2.9/quantplay/model/exchange/order.py
+-rw-r--r--   0 ashok      (502) staff       (20)     3238 2022-07-12 07:44:24.000000 quantplay-1.2.9/quantplay/model/exchange/tick.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.382051 quantplay-1.2.9/quantplay/model/strategy/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/model/strategy/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)      206 2022-04-17 10:54:24.000000 quantplay-1.2.9/quantplay/model/strategy/strategy_response.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.382187 quantplay-1.2.9/quantplay/oms/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-27 04:43:46.000000 quantplay-1.2.9/quantplay/oms/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.382527 quantplay-1.2.9/quantplay/order_execution/
+-rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/order_execution/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2048 2022-04-20 04:11:58.000000 quantplay-1.2.9/quantplay/order_execution/execution_algorithm.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1281 2022-04-19 06:42:52.000000 quantplay-1.2.9/quantplay/order_execution/mean_price.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.382897 quantplay-1.2.9/quantplay/reporting/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/reporting/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    10780 2023-01-19 02:56:14.000000 quantplay-1.2.9/quantplay/reporting/strategy_report.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1510 2022-06-06 18:04:02.000000 quantplay-1.2.9/quantplay/reporting/visuals.py
+-rw-r--r--   0 ashok      (502) staff       (20)      231 2023-01-08 06:14:00.000000 quantplay-1.2.9/quantplay/service.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.383409 quantplay-1.2.9/quantplay/services/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/services/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    17986 2023-01-23 02:26:35.000000 quantplay-1.2.9/quantplay/services/market.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2798 2023-01-08 06:12:37.000000 quantplay-1.2.9/quantplay/services/tradelens.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.383745 quantplay-1.2.9/quantplay/strategies/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:35:41.000000 quantplay-1.2.9/quantplay/strategies/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.383842 quantplay-1.2.9/quantplay/strategies/equities/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:48:09.000000 quantplay-1.2.9/quantplay/strategies/equities/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.383938 quantplay-1.2.9/quantplay/strategies/equities/intraday/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:48:26.000000 quantplay-1.2.9/quantplay/strategies/equities/intraday/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.384040 quantplay-1.2.9/quantplay/strategies/equities/overnight/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-23 06:49:47.000000 quantplay-1.2.9/quantplay/strategies/equities/overnight/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.384143 quantplay-1.2.9/quantplay/strategies/futures/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-24 08:54:42.000000 quantplay-1.2.9/quantplay/strategies/futures/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.384255 quantplay-1.2.9/quantplay/strategies/futures/overnight/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-24 08:54:48.000000 quantplay-1.2.9/quantplay/strategies/futures/overnight/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.384359 quantplay-1.2.9/quantplay/strategies/options/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:35:52.000000 quantplay-1.2.9/quantplay/strategies/options/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.384870 quantplay-1.2.9/quantplay/strategies/options/intraday/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-06-22 07:36:03.000000 quantplay-1.2.9/quantplay/strategies/options/intraday/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1958 2022-09-14 18:05:01.000000 quantplay-1.2.9/quantplay/strategies/options/intraday/ladder.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2675 2022-06-25 11:41:44.000000 quantplay-1.2.9/quantplay/strategies/options/intraday/musk.py
+-rw-r--r--   0 ashok      (502) staff       (20)      403 2022-09-17 07:36:48.000000 quantplay-1.2.9/quantplay/strategies/options/intraday/short_straddle.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.385114 quantplay-1.2.9/quantplay/strategy/
+-rw-r--r--   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/strategy/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)    11810 2022-10-21 05:19:41.000000 quantplay-1.2.9/quantplay/strategy/base.py
+-rw-r--r--   0 ashok      (502) staff       (20)      214 2022-06-28 09:52:29.000000 quantplay-1.2.9/quantplay/strategy_run.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.386610 quantplay-1.2.9/quantplay/utils/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-03-09 16:36:29.000000 quantplay-1.2.9/quantplay/utils/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)      723 2022-04-17 10:54:24.000000 quantplay-1.2.9/quantplay/utils/config_util.py
+-rw-r--r--   0 ashok      (502) staff       (20)    23741 2022-09-18 09:02:50.000000 quantplay-1.2.9/quantplay/utils/constant.py
+-rw-r--r--   0 ashok      (502) staff       (20)     5276 2022-08-22 16:31:03.000000 quantplay-1.2.9/quantplay/utils/data_utils.py
+-rw-r--r--   0 ashok      (502) staff       (20)      711 2022-04-17 10:54:24.000000 quantplay-1.2.9/quantplay/utils/exchange.py
+-rw-r--r--   0 ashok      (502) staff       (20)      517 2022-12-30 04:31:22.000000 quantplay-1.2.9/quantplay/utils/number_utils.py
+-rw-r--r--   0 ashok      (502) staff       (20)      458 2023-01-29 14:04:22.000000 quantplay-1.2.9/quantplay/utils/pickle_utils.py
+-rw-r--r--   0 ashok      (502) staff       (20)     1207 2023-01-16 02:41:32.000000 quantplay-1.2.9/quantplay/utils/selenium_utils.py
+-rw-r--r--   0 ashok      (502) staff       (20)     4094 2022-04-17 12:50:03.000000 quantplay-1.2.9/quantplay/utils/transaction_utils.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.377079 quantplay-1.2.9/quantplay.egg-info/
+-rw-r--r--   0 ashok      (502) staff       (20)      662 2023-03-14 05:33:14.000000 quantplay-1.2.9/quantplay.egg-info/PKG-INFO
+-rw-r--r--   0 ashok      (502) staff       (20)     2972 2023-03-14 05:33:14.000000 quantplay-1.2.9/quantplay.egg-info/SOURCES.txt
+-rw-r--r--   0 ashok      (502) staff       (20)        1 2023-03-14 05:33:14.000000 quantplay-1.2.9/quantplay.egg-info/dependency_links.txt
+-rw-r--r--   0 ashok      (502) staff       (20)      177 2023-03-14 05:33:14.000000 quantplay-1.2.9/quantplay.egg-info/requires.txt
+-rw-r--r--   0 ashok      (502) staff       (20)       15 2023-03-14 05:33:14.000000 quantplay-1.2.9/quantplay.egg-info/top_level.txt
+-rw-r--r--   0 ashok      (502) staff       (20)       49 2023-03-14 05:33:14.388194 quantplay-1.2.9/setup.cfg
+-rw-r--r--   0 ashok      (502) staff       (20)      875 2023-03-14 05:32:42.000000 quantplay-1.2.9/setup.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.386844 quantplay-1.2.9/test/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-15 16:22:35.000000 quantplay-1.2.9/test/__init__.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.387099 quantplay-1.2.9/test/broker/
+-rw-r--r--   0 ashok      (502) staff       (20)        0 2022-12-31 12:18:16.000000 quantplay-1.2.9/test/broker/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)      220 2022-12-31 14:39:54.000000 quantplay-1.2.9/test/broker/finvasia.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.387368 quantplay-1.2.9/test/executor/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-17 06:24:33.000000 quantplay-1.2.9/test/executor/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)      304 2022-04-17 10:58:40.000000 quantplay-1.2.9/test/executor/strategy_executor.py
+drwxr-xr-x   0 ashok      (502) staff       (20)        0 2023-03-14 05:33:14.387768 quantplay-1.2.9/test/strategy/
+-rw-------   0 ashok      (502) staff       (20)        0 2022-04-15 16:23:22.000000 quantplay-1.2.9/test/strategy/__init__.py
+-rw-r--r--   0 ashok      (502) staff       (20)      292 2022-04-17 10:54:24.000000 quantplay-1.2.9/test/strategy/base.py
+-rw-r--r--   0 ashok      (502) staff       (20)     2194 2022-04-20 14:52:19.000000 quantplay-1.2.9/test/strategy/sample_strategy.py
+-rw-r--r--   0 ashok      (502) staff       (20)     3302 2022-11-15 06:12:07.000000 quantplay-1.2.9/test/test_motilal.py
```

### Comparing `quantplay-1.2.8/PKG-INFO` & `quantplay-1.2.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quantplay
-Version: 1.2.8
+Version: 1.2.9
 Summary: This python package will be stored in AWS CodeArtifact
 Home-page: 
 Author: 
 Author-email: 
 License: MIT
 
 # Quantplay Alpha playground
```

### Comparing `quantplay-1.2.8/quantplay/backtest/backtest_trades.py` & `quantplay-1.2.9/quantplay/backtest/backtest_trades.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/angelone.py` & `quantplay-1.2.9/quantplay/broker/angelone.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/broker_client.py` & `quantplay-1.2.9/quantplay/broker/broker_client.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/finvasia_utils/shoonya.py` & `quantplay-1.2.9/quantplay/broker/finvasia_utils/shoonya.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/generics/broker.py` & `quantplay-1.2.9/quantplay/broker/generics/broker.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/kite_utils.py` & `quantplay-1.2.9/quantplay/broker/kite_utils.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/motilal.py` & `quantplay-1.2.9/quantplay/broker/motilal.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/shoonya.py` & `quantplay-1.2.9/quantplay/broker/shoonya.py`

 * *Files 2% similar despite different names*

```diff
@@ -323,15 +323,15 @@
         if positions is None or len(positions) == 0:
             return pd.DataFrame(columns=self.positions_column_list)
 
         positions = pd.DataFrame(positions)
 
         positions.loc[:, 'tradingsymbol'] = positions.tsym
         positions.loc[:, 'ltp'] = positions.lp.astype(float)
-        positions.loc[:, 'pnl'] = positions.rpnl.astype(float)
+        positions.loc[:, 'pnl'] = positions.rpnl.astype(float) + positions.urmtom.astype(float)
 
         if 'dname' not in positions.columns:
             positions.loc[:, 'dname'] = None
 
         positions.loc[:, 'dname'] = positions.dname.str.strip()
         positions.loc[:, 'dname'] = positions.dname.str.strip()
         positions.loc[:, 'option_type'] = np.where("PE" == positions.dname.str[-2:], "PE", np.nan)
@@ -398,15 +398,17 @@
         pnl = 0
         positions = self.positions()
         if len(positions) > 0:
             pnl = positions.pnl.sum()
 
         if 'marginused' not in margins:
             margins['marginused'] = 0
-        margin_available = float(margins['cash']) - float(margins['marginused'])
+        if 'payin' not in margins:
+            margins['payin'] = 0
+        margin_available = float(margins['cash']) + float(margins['payin']) - float(margins['marginused'])
         response = {
             'margin_used': float(margins['marginused']),
             'total_balance' : float(margins['cash']),
             'margin_available': margin_available,
             'pnl': pnl
         }
         return response
```

### Comparing `quantplay-1.2.8/quantplay/broker/symphony.py` & `quantplay-1.2.9/quantplay/broker/symphony.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/broker/zerodha.py` & `quantplay-1.2.9/quantplay/broker/zerodha.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/brokerage/angelone/angel_broker.py` & `quantplay-1.2.9/quantplay/brokerage/angelone/angel_broker.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/brokerage/generics/broker.py` & `quantplay-1.2.9/quantplay/brokerage/generics/broker.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/brokerage/zerodha/ZBroker.py` & `quantplay-1.2.9/quantplay/brokerage/zerodha/ZBroker.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/config/qplay_config.py` & `quantplay-1.2.9/quantplay/config/qplay_config.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/create_sample_data.py` & `quantplay-1.2.9/quantplay/create_sample_data.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/data_modify_script.py` & `quantplay-1.2.9/quantplay/data_modify_script.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/exception/exceptions.py` & `quantplay-1.2.9/quantplay/exception/exceptions.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/executor/strategy_executor.py` & `quantplay-1.2.9/quantplay/executor/strategy_executor.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/model/exchange/instrument.py` & `quantplay-1.2.9/quantplay/model/exchange/instrument.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/model/exchange/order.py` & `quantplay-1.2.9/quantplay/model/exchange/order.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/model/exchange/tick.py` & `quantplay-1.2.9/quantplay/model/exchange/tick.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/order_execution/execution_algorithm.py` & `quantplay-1.2.9/quantplay/order_execution/execution_algorithm.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/order_execution/mean_price.py` & `quantplay-1.2.9/quantplay/order_execution/mean_price.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/reporting/strategy_report.py` & `quantplay-1.2.9/quantplay/reporting/strategy_report.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/reporting/visuals.py` & `quantplay-1.2.9/quantplay/reporting/visuals.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/services/market.py` & `quantplay-1.2.9/quantplay/services/market.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/services/tradelens.py` & `quantplay-1.2.9/quantplay/services/tradelens.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/strategies/options/intraday/ladder.py` & `quantplay-1.2.9/quantplay/strategies/options/intraday/ladder.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/strategies/options/intraday/musk.py` & `quantplay-1.2.9/quantplay/strategies/options/intraday/musk.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/strategy/base.py` & `quantplay-1.2.9/quantplay/strategy/base.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/config_util.py` & `quantplay-1.2.9/quantplay/utils/config_util.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/constant.py` & `quantplay-1.2.9/quantplay/utils/constant.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/data_utils.py` & `quantplay-1.2.9/quantplay/utils/data_utils.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/exchange.py` & `quantplay-1.2.9/quantplay/utils/exchange.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/number_utils.py` & `quantplay-1.2.9/quantplay/utils/number_utils.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/selenium_utils.py` & `quantplay-1.2.9/quantplay/utils/selenium_utils.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay/utils/transaction_utils.py` & `quantplay-1.2.9/quantplay/utils/transaction_utils.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/quantplay.egg-info/PKG-INFO` & `quantplay-1.2.9/quantplay.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quantplay
-Version: 1.2.8
+Version: 1.2.9
 Summary: This python package will be stored in AWS CodeArtifact
 Home-page: 
 Author: 
 Author-email: 
 License: MIT
 
 # Quantplay Alpha playground
```

### Comparing `quantplay-1.2.8/quantplay.egg-info/SOURCES.txt` & `quantplay-1.2.9/quantplay.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/setup.py` & `quantplay-1.2.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,15 @@
     for line in Path("requirements.txt").read_text().splitlines()
     if is_requirement(line)
 ]
 
 setup(
     name="quantplay",
     long_description=Path("README.md").read_text(),
-    version="1.2.8",
+    version="1.2.9",
     setup_requires=["pytest-runner"],
     install_requires=requirements,
     tests_require=[],
     packages=find_packages(),
     url="",
     license="MIT",
     author="",
```

### Comparing `quantplay-1.2.8/test/strategy/sample_strategy.py` & `quantplay-1.2.9/test/strategy/sample_strategy.py`

 * *Files identical despite different names*

### Comparing `quantplay-1.2.8/test/test_motilal.py` & `quantplay-1.2.9/test/test_motilal.py`

 * *Files identical despite different names*

