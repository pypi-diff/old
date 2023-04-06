# Comparing `tmp/gs_quant-0.9.98.tar.gz` & `tmp/gs_quant-0.9.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/gs_quant-0.9.98.tar", last modified: Mon Mar 27 14:32:13 2023, max compression
+gzip compressed data, was "dist/gs_quant-0.9.99.tar", last modified: Thu Apr  6 10:52:41 2023, max compression
```

## Comparing `gs_quant-0.9.98.tar` & `gs_quant-0.9.99.tar`

### file list

```diff
@@ -1,421 +1,421 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-27 14:31:57.000000 gs_quant-0.9.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-03-27 14:32:13.000000 gs_quant-0.9.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-03-27 14:31:57.000000 gs_quant-0.9.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/common/
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/common/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      667 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/common/enumerators.py
--rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/common/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/core/
--rw-r--r--   0 runner    (1001) docker     (123)      599 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18717 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/core/processor.py
--rw-r--r--   0 runner    (1001) docker     (123)      740 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/core/processor_result.py
--rw-r--r--   0 runner    (1001) docker     (123)     5016 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/core/query_helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/
--rw-r--r--   0 runner    (1001) docker     (123)      722 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3635 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/data_cell.py
--rw-r--r--   0 runner    (1001) docker     (123)     6053 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/data_column.py
--rw-r--r--   0 runner    (1001) docker     (123)     7603 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/data_row.py
--rw-r--r--   0 runner    (1001) docker     (123)    31289 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/datagrid.py
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/serializers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3036 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/datagrid/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/processors/
--rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/analysis_processors.py
--rw-r--r--   0 runner    (1001) docker     (123)    15661 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/econometrics_processors.py
--rw-r--r--   0 runner    (1001) docker     (123)     7837 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/scale_processors.py
--rw-r--r--   0 runner    (1001) docker     (123)     3882 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/special_processors.py
--rw-r--r--   0 runner    (1001) docker     (123)    20346 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/statistics_processors.py
--rw-r--r--   0 runner    (1001) docker     (123)    16176 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/processors/utility_processors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/analytics/workspaces/
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/workspaces/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25146 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/workspaces/components.py
--rw-r--r--   0 runner    (1001) docker     (123)    24692 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/analytics/workspaces/workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/api/
--rw-r--r--   0 runner    (1001) docker     (123)      579 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/data.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/api/fred/
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/fred/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/fred/data.py
--rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/fred/fred_query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/api/gs/
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15995 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/assets.py
--rw-r--r--   0 runner    (1001) docker     (123)     6229 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/backtests.py
--rw-r--r--   0 runner    (1001) docker     (123)     6293 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/base_screener.py
--rw-r--r--   0 runner    (1001) docker     (123)     4196 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/carbon.py
--rw-r--r--   0 runner    (1001) docker     (123)     5510 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/content.py
--rw-r--r--   0 runner    (1001) docker     (123)     2660 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/countries.py
--rw-r--r--   0 runner    (1001) docker     (123)    36633 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/data.py
--rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/data_screen.py
--rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/datagrid.py
--rw-r--r--   0 runner    (1001) docker     (123)     2235 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/esg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3531 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    11394 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/hedges.py
--rw-r--r--   0 runner    (1001) docker     (123)     5835 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/indices.py
--rw-r--r--   0 runner    (1001) docker     (123)     2709 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/monitors.py
--rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2123 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/plots.py
--rw-r--r--   0 runner    (1001) docker     (123)    14356 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/portfolios.py
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/price.py
--rw-r--r--   0 runner    (1001) docker     (123)     9919 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/reports.py
--rw-r--r--   0 runner    (1001) docker     (123)    11988 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/risk.py
--rw-r--r--   0 runner    (1001) docker     (123)     8390 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/risk_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/screens.py
--rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/thematics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/users.py
--rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/gs/workspaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    12505 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/risk.py
--rw-r--r--   0 runner    (1001) docker     (123)     2322 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/api/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/backtests/
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1394 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/action_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     9891 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/actions.py
--rw-r--r--   0 runner    (1001) docker     (123)      863 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/backtest_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)    16746 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/backtest_objects.py
--rw-r--r--   0 runner    (1001) docker     (123)     2007 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/backtest_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     2980 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/data_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     6936 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/data_sources.py
--rw-r--r--   0 runner    (1001) docker     (123)      812 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/decorator.py
--rw-r--r--   0 runner    (1001) docker     (123)    14179 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/equity_vol_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     1248 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/event.py
--rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/execution_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)    39309 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/generic_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     7972 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/order.py
--rw-r--r--   0 runner    (1001) docker     (123)    10071 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/predefined_asset_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/strategy.py
--rw-r--r--   0 runner    (1001) docker     (123)     6766 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/strategy_systematic.py
--rw-r--r--   0 runner    (1001) docker     (123)    18079 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/backtests/triggers.py
--rw-r--r--   0 runner    (1001) docker     (123)    18782 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/config/
--rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      892 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/config/options.py
--rw-r--r--   0 runner    (1001) docker     (123)      587 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/config.ini
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/content/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/content/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/content/reports_and_screens/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/content/reports_and_screens/00_fx/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/content/reports_and_screens/00_fx/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3081 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/content/reports_and_screens/00_fx/vol_screen_app.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/content/reports_and_screens/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4618 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/context_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/data/
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8929 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/coordinate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3962 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/core.py
--rw-r--r--   0 runner    (1001) docker     (123)    15328 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     5796 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/log.py
--rw-r--r--   0 runner    (1001) docker     (123)     1897 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/query.py
--rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/data/stream.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/datetime/
--rw-r--r--   0 runner    (1001) docker     (123)      671 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10979 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/date.py
--rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/gscalendar.py
--rw-r--r--   0 runner    (1001) docker     (123)    11678 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/point.py
--rw-r--r--   0 runner    (1001) docker     (123)     9651 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/relative_date.py
--rw-r--r--   0 runner    (1001) docker     (123)     9136 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/rules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/datetime/time.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/docs/
--rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.business_day_count.html
--rw-r--r--   0 runner    (1001) docker     (123)    11059 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.business_day_offset.html
--rw-r--r--   0 runner    (1001) docker     (123)    11209 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.date_range.html
--rw-r--r--   0 runner    (1001) docker     (123)    10403 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.is_business_day.html
--rw-r--r--   0 runner    (1001) docker     (123)     9984 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.prev_business_date.html
--rw-r--r--   0 runner    (1001) docker     (123)     8161 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.point.point_sort_order.html
--rw-r--r--   0 runner    (1001) docker     (123)    11930 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.abs_.html
--rw-r--r--   0 runner    (1001) docker     (123)    14066 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.add.html
--rw-r--r--   0 runner    (1001) docker     (123)    10248 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.and_.html
--rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.ceil.html
--rw-r--r--   0 runner    (1001) docker     (123)    14106 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.divide.html
--rw-r--r--   0 runner    (1001) docker     (123)    11393 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.exp.html
--rw-r--r--   0 runner    (1001) docker     (123)    13221 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.filter_.html
--rw-r--r--   0 runner    (1001) docker     (123)    11788 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.floor.html
--rw-r--r--   0 runner    (1001) docker     (123)    13898 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.floordiv.html
--rw-r--r--   0 runner    (1001) docker     (123)    11096 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.if_.html
--rw-r--r--   0 runner    (1001) docker     (123)    11416 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.log.html
--rw-r--r--   0 runner    (1001) docker     (123)    14126 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.multiply.html
--rw-r--r--   0 runner    (1001) docker     (123)    10247 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.not_.html
--rw-r--r--   0 runner    (1001) docker     (123)    10249 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.or_.html
--rw-r--r--   0 runner    (1001) docker     (123)    11654 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.power.html
--rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.repeat.html
--rw-r--r--   0 runner    (1001) docker     (123)    11620 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.smooth_spikes.html
--rw-r--r--   0 runner    (1001) docker     (123)    11648 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.sqrt.html
--rw-r--r--   0 runner    (1001) docker     (123)    14183 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.subtract.html
--rw-r--r--   0 runner    (1001) docker     (123)    11852 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.weighted_sum.html
--rw-r--r--   0 runner    (1001) docker     (123)     9329 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.count.html
--rw-r--r--   0 runner    (1001) docker     (123)     9727 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.diff.html
--rw-r--r--   0 runner    (1001) docker     (123)     9322 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.first.html
--rw-r--r--   0 runner    (1001) docker     (123)    10915 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.lag.html
--rw-r--r--   0 runner    (1001) docker     (123)     9362 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.last.html
--rw-r--r--   0 runner    (1001) docker     (123)     9446 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.last_value.html
--rw-r--r--   0 runner    (1001) docker     (123)     3806 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.weighted_sum.html
--rw-r--r--   0 runner    (1001) docker     (123)    10208 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.backtesting.basket.html
--rw-r--r--   0 runner    (1001) docker     (123)    13116 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.align.html
--rw-r--r--   0 runner    (1001) docker     (123)    11783 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.date_range.html
--rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.day.html
--rw-r--r--   0 runner    (1001) docker     (123)    12769 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.interpolate.html
--rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.month.html
--rw-r--r--   0 runner    (1001) docker     (123)    10804 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.prepend.html
--rw-r--r--   0 runner    (1001) docker     (123)    10541 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.quarter.html
--rw-r--r--   0 runner    (1001) docker     (123)    10693 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.union.html
--rw-r--r--   0 runner    (1001) docker     (123)    12057 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.value.html
--rw-r--r--   0 runner    (1001) docker     (123)    10532 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.weekday.html
--rw-r--r--   0 runner    (1001) docker     (123)    10483 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.year.html
--rw-r--r--   0 runner    (1001) docker     (123)    11584 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.annualize.html
--rw-r--r--   0 runner    (1001) docker     (123)    13874 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.beta.html
--rw-r--r--   0 runner    (1001) docker     (123)    10365 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.change.html
--rw-r--r--   0 runner    (1001) docker     (123)    13613 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.correlation.html
--rw-r--r--   0 runner    (1001) docker     (123)    10460 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.excess_returns_.html
--rw-r--r--   0 runner    (1001) docker     (123)    10720 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.index.html
--rw-r--r--   0 runner    (1001) docker     (123)    10995 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.max_drawdown.html
--rw-r--r--   0 runner    (1001) docker     (123)    12717 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.prices.html
--rw-r--r--   0 runner    (1001) docker     (123)    12282 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.returns.html
--rw-r--r--   0 runner    (1001) docker     (123)    12191 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.sharpe_ratio.html
--rw-r--r--   0 runner    (1001) docker     (123)    14325 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.volatility.html
--rw-r--r--   0 runner    (1001) docker     (123)    14645 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.cov.html
--rw-r--r--   0 runner    (1001) docker     (123)    14370 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.exponential_std.html
--rw-r--r--   0 runner    (1001) docker     (123)    12083 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.generate_series.html
--rw-r--r--   0 runner    (1001) docker     (123)    13669 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.max_.html
--rw-r--r--   0 runner    (1001) docker     (123)    14083 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.mean.html
--rw-r--r--   0 runner    (1001) docker     (123)    13491 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.median.html
--rw-r--r--   0 runner    (1001) docker     (123)    13624 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.min_.html
--rw-r--r--   0 runner    (1001) docker     (123)    13107 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.mode.html
--rw-r--r--   0 runner    (1001) docker     (123)    12906 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.percentile.html
--rw-r--r--   0 runner    (1001) docker     (123)    14158 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.percentiles.html
--rw-r--r--   0 runner    (1001) docker     (123)    13132 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.product.html
--rw-r--r--   0 runner    (1001) docker     (123)    13118 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.range_.html
--rw-r--r--   0 runner    (1001) docker     (123)    13766 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.std.html
--rw-r--r--   0 runner    (1001) docker     (123)    13622 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.sum_.html
--rw-r--r--   0 runner    (1001) docker     (123)    13834 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.var.html
--rw-r--r--   0 runner    (1001) docker     (123)    14110 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.winsorize.html
--rw-r--r--   0 runner    (1001) docker     (123)    13566 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.zscores.html
--rw-r--r--   0 runner    (1001) docker     (123)    11992 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.bollinger_bands.html
--rw-r--r--   0 runner    (1001) docker     (123)    11628 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_moving_average.html
--rw-r--r--   0 runner    (1001) docker     (123)    11440 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_spread_volatility.html
--rw-r--r--   0 runner    (1001) docker     (123)    11474 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_volatility.html
--rw-r--r--   0 runner    (1001) docker     (123)    11114 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.moving_average.html
--rw-r--r--   0 runner    (1001) docker     (123)    10863 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.relative_strength_index.html
--rw-r--r--   0 runner    (1001) docker     (123)    11220 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.smoothed_moving_average.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/entities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/entities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20227 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/entities/entitlements.py
--rw-r--r--   0 runner    (1001) docker     (123)    42358 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/entities/entity.py
--rw-r--r--   0 runner    (1001) docker     (123)     8997 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/entities/tree_entity.py
--rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/instrument/
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/instrument/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13457 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/instrument/core.py
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/instrument/overrides.py
--rw-r--r--   0 runner    (1001) docker     (123)     5684 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/json_convertors.py
--rw-r--r--   0 runner    (1001) docker     (123)     1253 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/json_encoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/markets/
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    38713 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/baskets.py
--rw-r--r--   0 runner    (1001) docker     (123)    24889 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     8621 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/factor.py
--rw-r--r--   0 runner    (1001) docker     (123)    41479 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/hedge.py
--rw-r--r--   0 runner    (1001) docker     (123)     8978 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/historical.py
--rw-r--r--   0 runner    (1001) docker     (123)    21287 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/index.py
--rw-r--r--   0 runner    (1001) docker     (123)    19950 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/indices_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9781 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/markets.py
--rw-r--r--   0 runner    (1001) docker     (123)    30382 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/optimizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    25417 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/portfolio.py
--rw-r--r--   0 runner    (1001) docker     (123)    24832 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/portfolio_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    12977 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/portfolio_manager_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    18606 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/position_set.py
--rw-r--r--   0 runner    (1001) docker     (123)    62801 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/report.py
--rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/report_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    16415 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/screens.py
--rw-r--r--   0 runner    (1001) docker     (123)    69212 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/markets/securities.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/models/
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    29605 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/models/epidemiology.py
--rw-r--r--   0 runner    (1001) docker     (123)    96299 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/models/risk_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    18249 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/models/risk_model_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5214 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/priceable.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/quote_reports/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/quote_reports/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2116 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/quote_reports/core.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/risk/
--rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18848 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/measures.py
--rw-r--r--   0 runner    (1001) docker     (123)    14873 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/result_handlers.py
--rw-r--r--   0 runner    (1001) docker     (123)    39628 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/results.py
--rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/scenario_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2606 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/scenarios.py
--rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/risk/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)    21637 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/session.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/target/
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    30269 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/assets.py
--rw-r--r--   0 runner    (1001) docker     (123)    11832 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/assets_screener.py
--rw-r--r--   0 runner    (1001) docker     (123)    30101 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/backtests.py
--rw-r--r--   0 runner    (1001) docker     (123)     3455 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/base_screener.py
--rw-r--r--   0 runner    (1001) docker     (123)    16824 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/charts.py
--rw-r--r--   0 runner    (1001) docker     (123)   241535 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/common.py
--rw-r--r--   0 runner    (1001) docker     (123)    15206 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/content.py
--rw-r--r--   0 runner    (1001) docker     (123)     3177 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/coordinates.py
--rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/countries.py
--rw-r--r--   0 runner    (1001) docker     (123)    36203 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/data.py
--rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/data_screen.py
--rw-r--r--   0 runner    (1001) docker     (123)     4001 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    23131 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/hedge.py
--rw-r--r--   0 runner    (1001) docker     (123)    28594 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/indices.py
--rw-r--r--   0 runner    (1001) docker     (123)   158854 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)    26039 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/measures.py
--rw-r--r--   0 runner    (1001) docker     (123)    15365 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    10446 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/portfolios.py
--rw-r--r--   0 runner    (1001) docker     (123)     6334 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/price.py
--rw-r--r--   0 runner    (1001) docker     (123)    10608 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/reports.py
--rw-r--r--   0 runner    (1001) docker     (123)    37770 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/risk.py
--rw-r--r--   0 runner    (1001) docker     (123)    13042 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/risk_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     3847 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/screens.py
--rw-r--r--   0 runner    (1001) docker     (123)    17024 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/secmaster.py
--rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/trades.py
--rw-r--r--   0 runner    (1001) docker     (123)     9451 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/workflow_quote.py
--rw-r--r--   0 runner    (1001) docker     (123)    19404 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/target/workspaces_markets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/analytics/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/analytics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3827 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/analytics/test_datagrid.py
--rw-r--r--   0 runner    (1001) docker     (123)     5979 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/analytics/test_sorting_and_filtering.py
--rw-r--r--   0 runner    (1001) docker     (123)     5043 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/analytics/test_workspace.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8424 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_assets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4973 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_backtests.py
--rw-r--r--   0 runner    (1001) docker     (123)     7969 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_base_screener.py
--rw-r--r--   0 runner    (1001) docker     (123)     8027 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     7261 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_carbon.py
--rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_content.py
--rw-r--r--   0 runner    (1001) docker     (123)    19594 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     6945 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_data_screen.py
--rw-r--r--   0 runner    (1001) docker     (123)     4956 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_esg.py
--rw-r--r--   0 runner    (1001) docker     (123)     5958 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_fred.py
--rw-r--r--   0 runner    (1001) docker     (123)     3940 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     6159 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_instruments.py
--rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_json.py
--rw-r--r--   0 runner    (1001) docker     (123)     6127 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_monitor.py
--rw-r--r--   0 runner    (1001) docker     (123)    12381 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_portfolios.py
--rw-r--r--   0 runner    (1001) docker     (123)    12054 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_reports.py
--rw-r--r--   0 runner    (1001) docker     (123)     8790 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_risk.py
--rw-r--r--   0 runner    (1001) docker     (123)    30272 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_risk_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_target.py
--rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_thread_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     5394 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/api/test_users.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/backtest/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    34874 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_eq_vol_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     5181 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_flow_vol.py
--rw-r--r--   0 runner    (1001) docker     (123)     8314 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_predefined.py
--rw-r--r--   0 runner    (1001) docker     (123)    20499 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/test_generic_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     4026 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/backtest/test_triggers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/data/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2835 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/data/test_data_coordinate.py
--rw-r--r--   0 runner    (1001) docker     (123)    10512 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/data/test_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/datetime_/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/test_date.py
--rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/test_gscalendar.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/test_point.py
--rw-r--r--   0 runner    (1001) docker     (123)     9802 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/test_relative_date.py
--rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/datetime_/test_time.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/fixtures/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/fixtures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2953 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/fixtures/content.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/markets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12028 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_baskets.py
--rw-r--r--   0 runner    (1001) docker     (123)   180924 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_hedger.py
--rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)    17017 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_portfolio.py
--rw-r--r--   0 runner    (1001) docker     (123)    59098 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_portfolio_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    13426 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_pricing_context.py
--rw-r--r--   0 runner    (1001) docker     (123)    20426 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_report.py
--rw-r--r--   0 runner    (1001) docker     (123)    62477 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/markets/test_securities.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/models/
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6579 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/models/test_epidemiology.py
--rw-r--r--   0 runner    (1001) docker     (123)    25829 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/models/test_risk_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/timeseries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2325 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/test_commod.py
--rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/test_measure_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    19175 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_algebra.py
--rw-r--r--   0 runner    (1001) docker     (123)     6748 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)    18854 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_backtesting.py
--rw-r--r--   0 runner    (1001) docker     (123)    16880 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)    17517 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_econometrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     9989 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)   238167 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures.py
--rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_countries.py
--rw-r--r--   0 runner    (1001) docker     (123)    21519 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_fx_vol.py
--rw-r--r--   0 runner    (1001) docker     (123)    14577 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_inflation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3500 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_portfolios.py
--rw-r--r--   0 runner    (1001) docker     (123)    58601 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_rates.py
--rw-r--r--   0 runner    (1001) docker     (123)    36565 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_reports.py
--rw-r--r--   0 runner    (1001) docker     (123)    10574 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_risk_models.py
--rw-r--r--   0 runner    (1001) docker     (123)    14552 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_xccy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2134 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_rolling.py
--rw-r--r--   0 runner    (1001) docker     (123)    29270 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_statistics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1689 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_tca.py
--rw-r--r--   0 runner    (1001) docker     (123)    10203 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_technicals.py
--rw-r--r--   0 runner    (1001) docker     (123)     5038 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/test_timeseries.py
--rw-r--r--   0 runner    (1001) docker     (123)     2273 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/timeseries/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/test/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/datagrid_test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4310 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/mock_calc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/mock_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     3668 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/mock_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3738 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/test/utils/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/timeseries/
--rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    23911 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/algebra.py
--rw-r--r--   0 runner    (1001) docker     (123)    10328 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/analysis.py
--rw-r--r--   0 runner    (1001) docker     (123)    19527 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/backtesting.py
--rw-r--r--   0 runner    (1001) docker     (123)    20624 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)    26695 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/econometrics.py
--rw-r--r--   0 runner    (1001) docker     (123)    13437 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measure_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)   227330 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures.py
--rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_countries.py
--rw-r--r--   0 runner    (1001) docker     (123)    30098 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_fx_vol.py
--rw-r--r--   0 runner    (1001) docker     (123)     1863 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)    16985 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_inflation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3165 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_portfolios.py
--rw-r--r--   0 runner    (1001) docker     (123)   100015 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_rates.py
--rw-r--r--   0 runner    (1001) docker     (123)    16529 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_reports.py
--rw-r--r--   0 runner    (1001) docker     (123)     8014 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_risk_models.py
--rw-r--r--   0 runner    (1001) docker     (123)    20096 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/measures_xccy.py
--rw-r--r--   0 runner    (1001) docker     (123)    54568 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/statistics.py
--rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/tca.py
--rw-r--r--   0 runner    (1001) docker     (123)    20097 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/timeseries/technicals.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant/tracing/
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/tracing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4504 2023-03-27 14:31:57.000000 gs_quant-0.9.98/gs_quant/tracing/tracing.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    14744 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-27 14:32:13.000000 gs_quant-0.9.98/gs_quant.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-27 14:32:13.000000 gs_quant-0.9.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3531 2023-03-27 14:31:57.000000 gs_quant-0.9.98/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    68673 2023-03-27 14:31:57.000000 gs_quant-0.9.98/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-04-06 10:52:24.000000 gs_quant-0.9.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-04-06 10:52:40.000000 gs_quant-0.9.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-04-06 10:52:24.000000 gs_quant-0.9.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/
+-rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/common/
+-rw-r--r--   0 runner    (1001) docker     (123)      614 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/common/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      667 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/common/enumerators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/common/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/core/
+-rw-r--r--   0 runner    (1001) docker     (123)      599 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18717 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/core/processor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      740 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/core/processor_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5016 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/core/query_helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3635 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/data_cell.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6053 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/data_column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7603 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/data_row.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31289 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/datagrid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/serializers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3036 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/datagrid/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/processors/
+-rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/analysis_processors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15661 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/econometrics_processors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7837 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/scale_processors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3882 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/special_processors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20346 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/statistics_processors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16176 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/processors/utility_processors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/analytics/workspaces/
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/workspaces/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25146 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/workspaces/components.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24692 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/analytics/workspaces/workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/api/
+-rw-r--r--   0 runner    (1001) docker     (123)      579 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/data.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/api/fred/
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/fred/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/fred/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/fred/fred_query.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/api/gs/
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15995 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/assets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6229 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/backtests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6293 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/base_screener.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4196 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/carbon.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5510 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/content.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2660 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/countries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36633 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5810 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/data_screen.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2556 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/datagrid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2235 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/esg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3531 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11394 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/hedges.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5835 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/indices.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2709 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/monitors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2123 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/plots.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14356 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/portfolios.py
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/price.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10081 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11988 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/risk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8390 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/risk_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/screens.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/thematics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/users.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/gs/workspaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12505 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/risk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2322 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/api/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/backtests/
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1394 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/action_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9891 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/actions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      863 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/backtest_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16746 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/backtest_objects.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2007 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/backtest_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2980 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/data_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6936 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/data_sources.py
+-rw-r--r--   0 runner    (1001) docker     (123)      812 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/decorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14179 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/equity_vol_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1248 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/event.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/execution_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39309 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/generic_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7972 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/order.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10071 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/predefined_asset_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1741 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/strategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6766 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/strategy_systematic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18079 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/backtests/triggers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18782 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      585 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      892 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/config/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)      587 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/config.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/content/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/content/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/content/reports_and_screens/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/content/reports_and_screens/00_fx/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/content/reports_and_screens/00_fx/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3081 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/content/reports_and_screens/00_fx/vol_screen_app.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/content/reports_and_screens/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4618 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/context_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/data/
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8929 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/coordinate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3962 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15328 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5796 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1897 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/data/stream.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/datetime/
+-rw-r--r--   0 runner    (1001) docker     (123)      671 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10979 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/gscalendar.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11678 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/point.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9651 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/relative_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9136 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/rules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2681 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/datetime/time.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.business_day_count.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11059 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.business_day_offset.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11209 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.date_range.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10403 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.is_business_day.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9984 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.prev_business_date.html
+-rw-r--r--   0 runner    (1001) docker     (123)     8161 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.point.point_sort_order.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11930 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.abs_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14066 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.add.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10248 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.and_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11754 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.ceil.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14106 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.divide.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11393 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.exp.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13221 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.filter_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11788 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.floor.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13898 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.floordiv.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11096 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.if_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11416 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.log.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14126 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.multiply.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10247 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.not_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10249 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.or_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11654 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.power.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10879 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.repeat.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11620 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.smooth_spikes.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11648 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.sqrt.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14183 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.subtract.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11852 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.weighted_sum.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9329 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.count.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9727 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.diff.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9322 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.first.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10915 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.lag.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9362 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.last.html
+-rw-r--r--   0 runner    (1001) docker     (123)     9446 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.last_value.html
+-rw-r--r--   0 runner    (1001) docker     (123)     3806 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.weighted_sum.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10208 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.backtesting.basket.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13116 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.align.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11783 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.date_range.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.day.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12769 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.interpolate.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10482 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.month.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10804 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.prepend.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10541 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.quarter.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10693 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.union.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12057 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.value.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10532 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.weekday.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10483 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.year.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11584 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.annualize.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13874 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.beta.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10365 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.change.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13613 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.correlation.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10460 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.excess_returns_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10720 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.index.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10995 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.max_drawdown.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12717 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.prices.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12282 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.returns.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12191 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.sharpe_ratio.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14325 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.volatility.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14645 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.cov.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14370 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.exponential_std.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12083 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.generate_series.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13669 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.max_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14083 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.mean.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13491 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.median.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13624 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.min_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13107 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.mode.html
+-rw-r--r--   0 runner    (1001) docker     (123)    12906 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.percentile.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14158 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.percentiles.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13132 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.product.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13118 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.range_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13766 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.std.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13622 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.sum_.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13834 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.var.html
+-rw-r--r--   0 runner    (1001) docker     (123)    14110 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.winsorize.html
+-rw-r--r--   0 runner    (1001) docker     (123)    13566 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.zscores.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11992 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.bollinger_bands.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11628 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_moving_average.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11440 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_spread_volatility.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11474 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_volatility.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11114 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.moving_average.html
+-rw-r--r--   0 runner    (1001) docker     (123)    10863 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.relative_strength_index.html
+-rw-r--r--   0 runner    (1001) docker     (123)    11220 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.smoothed_moving_average.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/entities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/entities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20227 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/entities/entitlements.py
+-rw-r--r--   0 runner    (1001) docker     (123)    42358 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/entities/entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8997 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/entities/tree_entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/instrument/
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/instrument/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13457 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/instrument/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/instrument/overrides.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5684 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/json_convertors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1253 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/json_encoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/markets/
+-rw-r--r--   0 runner    (1001) docker     (123)      728 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38713 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/baskets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24916 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8621 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/factor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    41479 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/hedge.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8978 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/historical.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21287 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19950 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/indices_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9782 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/markets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30382 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25417 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24832 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/portfolio_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12977 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/portfolio_manager_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27816 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/position_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62801 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1836 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/report_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16415 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/screens.py
+-rw-r--r--   0 runner    (1001) docker     (123)    69212 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/markets/securities.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      560 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29605 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/models/epidemiology.py
+-rw-r--r--   0 runner    (1001) docker     (123)    96299 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/models/risk_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18249 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/models/risk_model_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5214 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/priceable.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/quote_reports/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/quote_reports/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2116 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/quote_reports/core.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/risk/
+-rw-r--r--   0 runner    (1001) docker     (123)     1030 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19410 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/measures.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14873 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/result_handlers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39786 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/scenario_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2606 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/scenarios.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/risk/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21637 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/session.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/target/
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30269 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/assets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11832 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/assets_screener.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30101 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/backtests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3455 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/base_screener.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16824 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/charts.py
+-rw-r--r--   0 runner    (1001) docker     (123)   241535 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15206 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/content.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3177 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/coordinates.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3283 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/countries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36279 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/data_screen.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4001 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23131 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/hedge.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28594 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/indices.py
+-rw-r--r--   0 runner    (1001) docker     (123)   158854 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26039 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/measures.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15365 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10446 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/portfolios.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6334 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/price.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10608 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37770 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/risk.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13042 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/risk_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3847 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/screens.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17024 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/secmaster.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11520 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/trades.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9451 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/workflow_quote.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19404 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/target/workspaces_markets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/analytics/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/analytics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3827 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/analytics/test_datagrid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5979 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/analytics/test_sorting_and_filtering.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5043 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/analytics/test_workspace.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8424 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_assets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4973 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_backtests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7969 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_base_screener.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8027 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7261 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_carbon.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3606 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_content.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19594 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6945 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_data_screen.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4956 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_esg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5958 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_fred.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3940 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6159 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1102 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_instruments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6127 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_monitor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12381 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_portfolios.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12054 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8790 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_risk.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30272 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_risk_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_target.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_thread_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5394 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/api/test_users.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/backtest/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34874 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_eq_vol_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5181 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_flow_vol.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8314 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_predefined.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20499 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/test_generic_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4026 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/backtest/test_triggers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/data/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2835 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/data/test_data_coordinate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10512 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/data/test_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/datetime_/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2583 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/test_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/test_gscalendar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/test_point.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9802 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/test_relative_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2973 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/datetime_/test_time.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/fixtures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2953 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/fixtures/content.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/markets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12028 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_baskets.py
+-rw-r--r--   0 runner    (1001) docker     (123)   180924 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_hedger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17017 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_portfolio.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59098 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_portfolio_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13426 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_pricing_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20426 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62477 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/markets/test_securities.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6579 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/models/test_epidemiology.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25829 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/models/test_risk_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/timeseries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2325 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/test_commod.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/test_measure_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19175 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_algebra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6748 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18854 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_backtesting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16880 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17517 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_econometrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9989 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)   238167 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_countries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21519 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_fx_vol.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14577 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_inflation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3500 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_portfolios.py
+-rw-r--r--   0 runner    (1001) docker     (123)    58601 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_rates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36565 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10574 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_risk_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14552 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_xccy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2134 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_rolling.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29270 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_statistics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1689 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_tca.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10203 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_technicals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5038 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/test_timeseries.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2273 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/timeseries/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/test/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/datagrid_test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4310 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/mock_calc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/mock_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3668 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/mock_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3738 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/test/utils/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/timeseries/
+-rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23911 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/algebra.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10328 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19527 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/backtesting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20624 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26695 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/econometrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13437 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2245 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measure_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)   227330 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3179 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_countries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30098 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_fx_vol.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1863 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16985 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_inflation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3165 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_portfolios.py
+-rw-r--r--   0 runner    (1001) docker     (123)   100015 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_rates.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16529 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8014 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_risk_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20096 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/measures_xccy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    54568 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/statistics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/tca.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20097 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/timeseries/technicals.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant/tracing/
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/tracing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4504 2023-04-06 10:52:24.000000 gs_quant-0.9.99/gs_quant/tracing/tracing.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2128 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    14744 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 10:52:40.000000 gs_quant-0.9.99/gs_quant.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-04-06 10:52:40.000000 gs_quant-0.9.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3538 2023-04-06 10:52:24.000000 gs_quant-0.9.99/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68673 2023-04-06 10:52:24.000000 gs_quant-0.9.99/versioneer.py
```

### Comparing `gs_quant-0.9.98/PKG-INFO` & `gs_quant-0.9.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gs_quant
-Version: 0.9.98
+Version: 0.9.99
 Summary: Goldman Sachs Quant
 Home-page: https://marquee.gs.com
 Author: Goldman Sachs
 Author-email: developer@gs.com
 License: http://www.apache.org/licenses/LICENSE-2.0
 Description: # GS Quant
```

### Comparing `gs_quant-0.9.98/README.md` & `gs_quant-0.9.99/README.md`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/__init__.py` & `gs_quant-0.9.99/gs_quant/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/common/__init__.py` & `gs_quant-0.9.99/gs_quant/analytics/common/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/common/constants.py` & `gs_quant-0.9.99/gs_quant/analytics/common/constants.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/common/enumerators.py` & `gs_quant-0.9.99/gs_quant/analytics/common/enumerators.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/common/helpers.py` & `gs_quant-0.9.99/gs_quant/analytics/common/helpers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/core/__init__.py` & `gs_quant-0.9.99/gs_quant/analytics/core/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/core/processor.py` & `gs_quant-0.9.99/gs_quant/analytics/core/processor.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/core/processor_result.py` & `gs_quant-0.9.99/gs_quant/analytics/core/processor_result.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/core/query_helpers.py` & `gs_quant-0.9.99/gs_quant/analytics/core/query_helpers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/__init__.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/data_cell.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/data_cell.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/data_column.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/data_column.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/data_row.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/data_row.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/datagrid.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/datagrid.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/serializers.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/serializers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/datagrid/utils.py` & `gs_quant-0.9.99/gs_quant/analytics/datagrid/utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/__init__.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/analysis_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/analysis_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/econometrics_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/econometrics_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/scale_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/scale_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/special_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/special_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/statistics_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/statistics_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/processors/utility_processors.py` & `gs_quant-0.9.99/gs_quant/analytics/processors/utility_processors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/workspaces/__init__.py` & `gs_quant-0.9.99/gs_quant/analytics/workspaces/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/workspaces/components.py` & `gs_quant-0.9.99/gs_quant/analytics/workspaces/components.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/analytics/workspaces/workspace.py` & `gs_quant-0.9.99/gs_quant/analytics/workspaces/workspace.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/__init__.py` & `gs_quant-0.9.99/gs_quant/api/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/data.py` & `gs_quant-0.9.99/gs_quant/api/data.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/fred/__init__.py` & `gs_quant-0.9.99/gs_quant/api/fred/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/fred/data.py` & `gs_quant-0.9.99/gs_quant/api/fred/data.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/fred/fred_query.py` & `gs_quant-0.9.99/gs_quant/api/fred/fred_query.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/__init__.py` & `gs_quant-0.9.99/gs_quant/api/gs/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/assets.py` & `gs_quant-0.9.99/gs_quant/api/gs/assets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/backtests.py` & `gs_quant-0.9.99/gs_quant/api/gs/backtests.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/base_screener.py` & `gs_quant-0.9.99/gs_quant/api/gs/base_screener.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/carbon.py` & `gs_quant-0.9.99/gs_quant/api/gs/carbon.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/content.py` & `gs_quant-0.9.99/gs_quant/api/gs/content.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/countries.py` & `gs_quant-0.9.99/gs_quant/api/gs/countries.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/data.py` & `gs_quant-0.9.99/gs_quant/api/gs/data.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/data_screen.py` & `gs_quant-0.9.99/gs_quant/api/gs/data_screen.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/datagrid.py` & `gs_quant-0.9.99/gs_quant/api/gs/datagrid.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/esg.py` & `gs_quant-0.9.99/gs_quant/api/gs/esg.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/groups.py` & `gs_quant-0.9.99/gs_quant/api/gs/groups.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/hedges.py` & `gs_quant-0.9.99/gs_quant/api/gs/hedges.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/indices.py` & `gs_quant-0.9.99/gs_quant/api/gs/indices.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/monitors.py` & `gs_quant-0.9.99/gs_quant/api/gs/monitors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/parser.py` & `gs_quant-0.9.99/gs_quant/api/gs/parser.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/plots.py` & `gs_quant-0.9.99/gs_quant/api/gs/plots.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/portfolios.py` & `gs_quant-0.9.99/gs_quant/api/gs/portfolios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/price.py` & `gs_quant-0.9.99/gs_quant/api/gs/price.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/reports.py` & `gs_quant-0.9.99/gs_quant/api/gs/reports.py`

 * *Files 3% similar despite different names*

```diff
@@ -100,14 +100,18 @@
         return GsSession.current._get('/reports/{id}/jobs'.format(id=report_id))['results']
 
     @classmethod
     def get_report_job(cls, report_job_id: str) -> dict:
         return GsSession.current._get('/reports/jobs/{report_job_id}'.format(report_job_id=report_job_id))
 
     @classmethod
+    def reschedule_report_job(cls, report_job_id: str):
+        return GsSession.current._post(f'/reports/jobs/{report_job_id}/reschedule', {})
+
+    @classmethod
     def cancel_report_job(cls, report_job_id: str) -> dict:
         return GsSession.current._post('/reports/jobs/{report_job_id}/cancel'.format(report_job_id=report_job_id))
 
     @classmethod
     def update_report_job(cls, report_job_id: str, status: str) -> dict:
         status_body = {
             "status": '{status}'.format(status=status)
```

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/risk.py` & `gs_quant-0.9.99/gs_quant/api/gs/risk.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/risk_models.py` & `gs_quant-0.9.99/gs_quant/api/gs/risk_models.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/screens.py` & `gs_quant-0.9.99/gs_quant/api/gs/screens.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/thematics.py` & `gs_quant-0.9.99/gs_quant/api/gs/thematics.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/users.py` & `gs_quant-0.9.99/gs_quant/api/gs/users.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/gs/workspaces.py` & `gs_quant-0.9.99/gs_quant/api/gs/workspaces.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/risk.py` & `gs_quant-0.9.99/gs_quant/api/risk.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/api/utils.py` & `gs_quant-0.9.99/gs_quant/api/utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/__init__.py` & `gs_quant-0.9.99/gs_quant/backtests/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/action_handler.py` & `gs_quant-0.9.99/gs_quant/backtests/action_handler.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/actions.py` & `gs_quant-0.9.99/gs_quant/backtests/actions.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/backtest_engine.py` & `gs_quant-0.9.99/gs_quant/backtests/backtest_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/backtest_objects.py` & `gs_quant-0.9.99/gs_quant/backtests/backtest_objects.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/backtest_utils.py` & `gs_quant-0.9.99/gs_quant/backtests/backtest_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/core.py` & `gs_quant-0.9.99/gs_quant/backtests/core.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/data_handler.py` & `gs_quant-0.9.99/gs_quant/backtests/data_handler.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/data_sources.py` & `gs_quant-0.9.99/gs_quant/backtests/data_sources.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/decorator.py` & `gs_quant-0.9.99/gs_quant/backtests/decorator.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/equity_vol_engine.py` & `gs_quant-0.9.99/gs_quant/backtests/equity_vol_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/event.py` & `gs_quant-0.9.99/gs_quant/backtests/event.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/execution_engine.py` & `gs_quant-0.9.99/gs_quant/backtests/execution_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/generic_engine.py` & `gs_quant-0.9.99/gs_quant/backtests/generic_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/order.py` & `gs_quant-0.9.99/gs_quant/backtests/order.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/predefined_asset_engine.py` & `gs_quant-0.9.99/gs_quant/backtests/predefined_asset_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/strategy.py` & `gs_quant-0.9.99/gs_quant/backtests/strategy.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/strategy_systematic.py` & `gs_quant-0.9.99/gs_quant/backtests/strategy_systematic.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/backtests/triggers.py` & `gs_quant-0.9.99/gs_quant/backtests/triggers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/base.py` & `gs_quant-0.9.99/gs_quant/base.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/common.py` & `gs_quant-0.9.99/gs_quant/common.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/config/__init__.py` & `gs_quant-0.9.99/gs_quant/config/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/config/options.py` & `gs_quant-0.9.99/gs_quant/config/options.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/config.ini` & `gs_quant-0.9.99/gs_quant/config.ini`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/content/reports_and_screens/00_fx/vol_screen_app.py` & `gs_quant-0.9.99/gs_quant/content/reports_and_screens/00_fx/vol_screen_app.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/context_base.py` & `gs_quant-0.9.99/gs_quant/context_base.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/__init__.py` & `gs_quant-0.9.99/gs_quant/data/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/coordinate.py` & `gs_quant-0.9.99/gs_quant/data/coordinate.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/core.py` & `gs_quant-0.9.99/gs_quant/data/core.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/dataset.py` & `gs_quant-0.9.99/gs_quant/data/dataset.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/fields.py` & `gs_quant-0.9.99/gs_quant/data/fields.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/log.py` & `gs_quant-0.9.99/gs_quant/data/log.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/query.py` & `gs_quant-0.9.99/gs_quant/data/query.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/data/stream.py` & `gs_quant-0.9.99/gs_quant/data/stream.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/__init__.py` & `gs_quant-0.9.99/gs_quant/datetime/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/date.py` & `gs_quant-0.9.99/gs_quant/datetime/date.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/gscalendar.py` & `gs_quant-0.9.99/gs_quant/datetime/gscalendar.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/point.py` & `gs_quant-0.9.99/gs_quant/datetime/point.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/relative_date.py` & `gs_quant-0.9.99/gs_quant/datetime/relative_date.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/rules.py` & `gs_quant-0.9.99/gs_quant/datetime/rules.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/datetime/time.py` & `gs_quant-0.9.99/gs_quant/datetime/time.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.business_day_count.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.business_day_count.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.business_day_offset.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.business_day_offset.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.date_range.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.date_range.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.is_business_day.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.is_business_day.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.date.prev_business_date.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.date.prev_business_date.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.datetime.point.point_sort_order.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.datetime.point.point_sort_order.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.abs_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.abs_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.add.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.add.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.and_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.and_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.ceil.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.ceil.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.divide.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.divide.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.exp.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.exp.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.filter_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.filter_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.floor.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.floor.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.floordiv.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.floordiv.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.if_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.if_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.log.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.log.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.multiply.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.multiply.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.not_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.not_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.or_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.or_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.power.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.power.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.repeat.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.repeat.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.smooth_spikes.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.smooth_spikes.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.sqrt.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.sqrt.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.subtract.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.subtract.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.algebra.weighted_sum.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.algebra.weighted_sum.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.count.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.count.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.diff.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.diff.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.first.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.first.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.lag.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.lag.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.last.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.last.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.last_value.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.last_value.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.analysis.weighted_sum.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.analysis.weighted_sum.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.backtesting.basket.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.backtesting.basket.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.align.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.align.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.date_range.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.date_range.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.day.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.day.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.interpolate.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.interpolate.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.month.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.month.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.prepend.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.prepend.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.quarter.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.quarter.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.union.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.union.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.value.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.value.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.weekday.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.weekday.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.datetime.year.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.datetime.year.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.annualize.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.annualize.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.beta.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.beta.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.change.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.change.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.correlation.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.correlation.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.excess_returns_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.excess_returns_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.index.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.index.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.max_drawdown.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.max_drawdown.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.prices.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.prices.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.returns.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.returns.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.sharpe_ratio.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.sharpe_ratio.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.econometrics.volatility.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.econometrics.volatility.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.cov.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.cov.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.exponential_std.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.exponential_std.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.generate_series.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.generate_series.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.max_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.max_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.mean.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.mean.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.median.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.median.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.min_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.min_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.mode.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.mode.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.percentile.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.percentile.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.percentiles.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.percentiles.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.product.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.product.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.range_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.range_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.std.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.std.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.sum_.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.sum_.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.var.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.var.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.winsorize.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.winsorize.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.statistics.zscores.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.statistics.zscores.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.bollinger_bands.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.bollinger_bands.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_moving_average.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_moving_average.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_spread_volatility.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_spread_volatility.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.exponential_volatility.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.exponential_volatility.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.moving_average.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.moving_average.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.relative_strength_index.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.relative_strength_index.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/docs/gs_quant.timeseries.technicals.smoothed_moving_average.html` & `gs_quant-0.9.99/gs_quant/docs/gs_quant.timeseries.technicals.smoothed_moving_average.html`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/entities/entitlements.py` & `gs_quant-0.9.99/gs_quant/entities/entitlements.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/entities/entity.py` & `gs_quant-0.9.99/gs_quant/entities/entity.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/entities/tree_entity.py` & `gs_quant-0.9.99/gs_quant/entities/tree_entity.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/errors.py` & `gs_quant-0.9.99/gs_quant/errors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/instrument/__init__.py` & `gs_quant-0.9.99/gs_quant/instrument/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/instrument/core.py` & `gs_quant-0.9.99/gs_quant/instrument/core.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/instrument/overrides.py` & `gs_quant-0.9.99/gs_quant/instrument/overrides.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/json_convertors.py` & `gs_quant-0.9.99/gs_quant/json_convertors.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/json_encoder.py` & `gs_quant-0.9.99/gs_quant/json_encoder.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/__init__.py` & `gs_quant-0.9.99/gs_quant/markets/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/baskets.py` & `gs_quant-0.9.99/gs_quant/markets/baskets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/core.py` & `gs_quant-0.9.99/gs_quant/markets/core.py`

 * *Files 1% similar despite different names*

```diff
@@ -99,20 +99,21 @@
         :param is_async: if True, return (a future) immediately. If False, block (defaults to False)
         :param is_batch: use for calculations expected to run longer than 3 mins, to avoid timeouts.
             It can be used with is_async=True|False (defaults to False)
         :param use_cache: store results in the pricing cache (defaults to False)
         :param visible_to_gs: are the contents of risk requests visible to GS (defaults to False)
         :param request_priority: the priority of risk requests
         :param csa_term: the csa under which the calculations are made. Default is local ccy ois index
-        :param market_data_location: the location for sourcing market data ('NYC', 'LDN' or 'HKG' (defaults to LDN)
         :param timeout: the timeout for batch operations
+        :param market: a Market object
         :param show_progress: add a progress bar (tqdm)
         :param use_server_cache: cache query results on the GS servers
         :param market_behaviour: the behaviour to build the curve for pricing ('ContraintsBased' or 'Calibrated'
             (defaults to ContraintsBased))
+        :param set_parameters_only: if true don't stop embedded pricing contexts submitting their jobs.
 
         **Examples**
 
         To change the market data location of the default context:
 
         >>> from gs_quant.markets import PricingContext
         >>>
```

### Comparing `gs_quant-0.9.98/gs_quant/markets/factor.py` & `gs_quant-0.9.99/gs_quant/markets/factor.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/hedge.py` & `gs_quant-0.9.99/gs_quant/markets/hedge.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/historical.py` & `gs_quant-0.9.99/gs_quant/markets/historical.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/index.py` & `gs_quant-0.9.99/gs_quant/markets/index.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/indices_utils.py` & `gs_quant-0.9.99/gs_quant/markets/indices_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/markets.py` & `gs_quant-0.9.99/gs_quant/markets/markets.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,24 +10,25 @@
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 """
 import datetime as dt
+import re
+from typing import Mapping, Optional, Tuple, Union
+
 from gs_quant.base import Market, RiskKey
 from gs_quant.common import PricingLocation
 from gs_quant.datetime.date import prev_business_date
 from gs_quant.target.common import CloseMarket as _CloseMarket, LiveMarket as _LiveMarket, \
     OverlayMarket as _OverlayMarket, RelativeMarket as _RelativeMarket, TimestampedMarket as _TimestampedMarket, \
     RefMarket as _RefMarket
 from gs_quant.target.data import MarketDataCoordinate as __MarketDataCoordinate, \
     MarketDataCoordinateValue as __MarketDataCoordinateValue
-import re
-from typing import Mapping, Optional, Tuple, Union
 
 
 def historical_risk_key(risk_key: RiskKey) -> RiskKey:
     market = LocationOnlyMarket(risk_key.market.location)
     return RiskKey(risk_key.provider, None, market, risk_key.params, risk_key.scenario, risk_key.risk_measure)
```

### Comparing `gs_quant-0.9.98/gs_quant/markets/optimizer.py` & `gs_quant-0.9.99/gs_quant/markets/optimizer.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/portfolio.py` & `gs_quant-0.9.99/gs_quant/markets/portfolio.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/portfolio_manager.py` & `gs_quant-0.9.99/gs_quant/markets/portfolio_manager.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/portfolio_manager_utils.py` & `gs_quant-0.9.99/gs_quant/markets/portfolio_manager_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/report.py` & `gs_quant-0.9.99/gs_quant/markets/report.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/report_utils.py` & `gs_quant-0.9.99/gs_quant/markets/report_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/screens.py` & `gs_quant-0.9.99/gs_quant/markets/screens.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/markets/securities.py` & `gs_quant-0.9.99/gs_quant/markets/securities.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/models/__init__.py` & `gs_quant-0.9.99/gs_quant/models/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/models/epidemiology.py` & `gs_quant-0.9.99/gs_quant/models/epidemiology.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/models/risk_model.py` & `gs_quant-0.9.99/gs_quant/models/risk_model.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/models/risk_model_utils.py` & `gs_quant-0.9.99/gs_quant/models/risk_model_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/priceable.py` & `gs_quant-0.9.99/gs_quant/priceable.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/quote_reports/core.py` & `gs_quant-0.9.99/gs_quant/quote_reports/core.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/__init__.py` & `gs_quant-0.9.99/gs_quant/risk/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/core.py` & `gs_quant-0.9.99/gs_quant/risk/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 under the License.
 """
 import datetime as dt
 import itertools
 from abc import ABCMeta, abstractmethod
 from concurrent.futures import Future
 from copy import copy
-from dataclasses import dataclass
+from dataclasses import dataclass, fields
 from typing import Iterable, Optional, Tuple, Union, Dict
 
 import pandas as pd
 from dataclasses_json import dataclass_json
 
 import gs_quant
 from gs_quant.base import RiskKey
@@ -342,15 +342,27 @@
             show_na = options.show_na
 
             return [{**extra_dict, 'value': None}] if show_na else []
 
         return [dict(item, **{**extra_dict}) for item in self.raw_value.to_dict('records')]
 
     def copy_with_resultinfo(self, deep=True):
-        return DataFrameWithInfo(self.raw_value.copy(deep=deep), risk_key=self.risk_key, unit=self.unit, error=self.error, request_id=self.request_id)
+        return DataFrameWithInfo(self.raw_value.copy(deep=deep), risk_key=self.risk_key, unit=self.unit,
+                                 error=self.error, request_id=self.request_id)
+
+    def filter_by_coord(self, coordinate):
+        from gs_quant.markets import MarketDataCoordinate
+        df = self.copy_with_resultinfo()
+        for att in [i.name for i in fields(MarketDataCoordinate)]:
+            if getattr(coordinate, att) is not None:
+                if isinstance(getattr(coordinate, att), str):
+                    df = df[getattr(df, att) == getattr(coordinate, att)]
+                else:
+                    df = df[getattr(df, att).isin(getattr(coordinate, att))]
+        return df
 
 
 @dataclass_json
 @dataclass
 class MQVSValidationTarget:
     env: Optional[str] = None
     operator: Optional[str] = None
@@ -543,12 +555,12 @@
     """
     Combine two risk keys (key_1, key_2) into a new RiskKey
 
     :type key_1: RiskKey
     :type key_2: RiskKey
     """
 
-    def get_field_value(field_name: str): getattr(key_1, field_name) \
-        if getattr(key_1, field_name) == getattr(key_2, field_name) else None
+    def get_field_value(field_name: str):
+        return getattr(key_1, field_name) if getattr(key_1, field_name) == getattr(key_2, field_name) else None
 
     return RiskKey(get_field_value("provider"), get_field_value("date"), get_field_value("market"),
                    get_field_value("params"), get_field_value("scenario"), get_field_value("risk_measure"))
```

### Comparing `gs_quant-0.9.98/gs_quant/risk/measures.py` & `gs_quant-0.9.99/gs_quant/risk/measures.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/result_handlers.py` & `gs_quant-0.9.99/gs_quant/risk/result_handlers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/results.py` & `gs_quant-0.9.99/gs_quant/risk/results.py`

 * *Files 0% similar despite different names*

```diff
@@ -760,18 +760,22 @@
         if risk_transformation is None:
             return self
         elif len(self.__risk_measures) > 1:
             return MultipleRiskMeasureResult(self.portfolio,
                                              ((r, self[r].transform(risk_transformation)) for r in
                                               self.__risk_measures))
         elif len(self.__risk_measures) == 1:
-            transformed_future = PricingFuture()
-            transformed_future.set_result(risk_transformation.apply(self.__results()))
-            transformed_future.done()
-            return PortfolioRiskResult(self.portfolio, self.risk_measures, (transformed_future,))
+            flattened_results = risk_transformation.apply(self.__results())
+            futures = []
+            for result in flattened_results:
+                transformed_future = PricingFuture()
+                transformed_future.set_result(result)
+                transformed_future.done()
+                futures.append(transformed_future)
+            return PortfolioRiskResult(self.portfolio, self.risk_measures, futures)
         else:
             return self
 
     def aggregate(self, allow_mismatch_risk_keys=False) -> Union[float, pd.DataFrame, pd.Series,
                                                                  MultipleRiskMeasureResult]:
         if len(self.__risk_measures) > 1:
             return MultipleRiskMeasureResult(self.portfolio, ((r, self[r].aggregate()) for r in self.__risk_measures))
```

### Comparing `gs_quant-0.9.98/gs_quant/risk/scenario_utils.py` & `gs_quant-0.9.99/gs_quant/risk/scenario_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/scenarios.py` & `gs_quant-0.9.99/gs_quant/risk/scenarios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/risk/transform.py` & `gs_quant-0.9.99/gs_quant/risk/transform.py`

 * *Files 9% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 specific language governing permissions and limitations
 under the License.
 """
 
 from abc import ABC, abstractmethod
 from typing import Generic, Callable, Sequence, Any, TypeVar, Iterable, Union
 
-from gs_quant.risk.core import ResultType, DataFrameWithInfo, SeriesWithInfo, FloatWithInfo, combine_risk_key
+from gs_quant.risk.core import ResultType, DataFrameWithInfo, SeriesWithInfo, FloatWithInfo
 
 _InputT = TypeVar('_InputT')
 _ResultT = TypeVar('_ResultT')
 
 
 class Transformer(ABC, Generic[_InputT, _ResultT]):
     @abstractmethod
@@ -34,36 +34,46 @@
         self.__fn = fn
 
     def apply(self, data: ResultType, *args, **kwargs) -> ResultType:
         return self.__fn(data, *args, **kwargs)
 
 
 class ResultWithInfoAggregator(Transformer[Iterable[ResultType], FloatWithInfo]):
-    def __init__(self, risk_col: str = 'value'):
+    def __init__(self, risk_col: str = 'value', filter_coord=None):
         self.__risk_col = risk_col
+        self.__filter_coord = filter_coord
 
     def apply(self, results: Iterable[Union[float, FloatWithInfo, SeriesWithInfo, DataFrameWithInfo]],
-              *args, **kwargs) -> FloatWithInfo:
-        val = 0
+              *args, **kwargs) -> Iterable[Union[float, FloatWithInfo]]:
         risk_key = None
-        units = set()
+        flattened_results = set()
 
         for result in results:
             if isinstance(result, float):
-                val += result
-            elif isinstance(result, (FloatWithInfo, SeriesWithInfo, DataFrameWithInfo)):
+                flattened_results.add(result)
+            else:
                 if isinstance(result, FloatWithInfo):
-                    val += result.raw_value
+                    val = result.raw_value
+                elif isinstance(result, SeriesWithInfo):
+                    val = getattr(result, self.risk_col).sum()
+                elif isinstance(result, DataFrameWithInfo):
+                    if self.filter_coord is not None:
+                        df = result.filter_by_coord(self.filter_coord)
+                        val = getattr(df, self.risk_col).sum()
+                    else:
+                        val = getattr(result, self.risk_col).sum()
                 else:
-                    val += getattr(result, self.risk_col).sum()
-                risk_key = result.risk_key if risk_key is None else combine_risk_key(risk_key, result.risk_key)
-                units.add(result.unit)
-            else:
-                raise ValueError(f'Aggregation of {type(result).__name__} not currently supported')
+                    raise ValueError(f'Aggregation of {type(result).__name__} not currently supported')
+                risk_key = result.risk_key
+                unit = result.unit
+                error = result.error
+                flattened_results.add(FloatWithInfo(value=val, risk_key=risk_key, unit=unit, error=error))
 
-        if len(units) != 1:
-            raise ValueError(f'Aggregation of {len(units)} units not currently supported. 1 unit expected.')
-        return FloatWithInfo(value=val, risk_key=risk_key, unit=(list(units))[0])
+        return flattened_results
 
     @property
     def risk_col(self):
         return self.__risk_col
+
+    @property
+    def filter_coord(self):
+        return self.__filter_coord
```

### Comparing `gs_quant-0.9.98/gs_quant/session.py` & `gs_quant-0.9.99/gs_quant/session.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/__init__.py` & `gs_quant-0.9.99/gs_quant/target/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/assets.py` & `gs_quant-0.9.99/gs_quant/target/assets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/assets_screener.py` & `gs_quant-0.9.99/gs_quant/target/assets_screener.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/backtests.py` & `gs_quant-0.9.99/gs_quant/target/backtests.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/base_screener.py` & `gs_quant-0.9.99/gs_quant/target/base_screener.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/charts.py` & `gs_quant-0.9.99/gs_quant/target/charts.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/common.py` & `gs_quant-0.9.99/gs_quant/target/common.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/content.py` & `gs_quant-0.9.99/gs_quant/target/content.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/coordinates.py` & `gs_quant-0.9.99/gs_quant/target/coordinates.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/countries.py` & `gs_quant-0.9.99/gs_quant/target/countries.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/data.py` & `gs_quant-0.9.99/gs_quant/target/data.py`

 * *Files 0% similar despite different names*

```diff
@@ -469,14 +469,15 @@
     times: Optional[Tuple[datetime.datetime, ...]] = field(default=None, metadata=field_metadata)
     delay: Optional[int] = field(default=None, metadata=field_metadata)
     intervals: Optional[int] = field(default=None, metadata=field_metadata)
     samples: Optional[int] = field(default=None, metadata=field_metadata)
     limit: Optional[int] = field(default=None, metadata=field_metadata)
     polling_interval: Optional[int] = field(default=None, metadata=field_metadata)
     grouped: Optional[bool] = field(default=None, metadata=field_metadata)
+    group_by: Optional[bool] = field(default=None, metadata=field_metadata)
     fields: Optional[Tuple[Union[DictBase, str], ...]] = field(default=None, metadata=field_metadata)
     restrict_fields: Optional[bool] = field(default=False, metadata=field_metadata)
     entity_filter: Optional[FieldFilterMapDataQuery] = field(default=None, metadata=field_metadata)
     interval: Optional[str] = field(default=None, metadata=field_metadata)
     distinct_consecutive: Optional[bool] = field(default=False, metadata=field_metadata)
     time_filter: Optional[TimeFilter] = field(default=None, metadata=field_metadata)
     use_field_alias: Optional[bool] = field(default=False, metadata=field_metadata)
```

### Comparing `gs_quant-0.9.98/gs_quant/target/data_screen.py` & `gs_quant-0.9.99/gs_quant/target/data_screen.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/groups.py` & `gs_quant-0.9.99/gs_quant/target/groups.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/hedge.py` & `gs_quant-0.9.99/gs_quant/target/hedge.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/indices.py` & `gs_quant-0.9.99/gs_quant/target/indices.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/instrument.py` & `gs_quant-0.9.99/gs_quant/target/instrument.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/measures.py` & `gs_quant-0.9.99/gs_quant/target/measures.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/monitor.py` & `gs_quant-0.9.99/gs_quant/target/monitor.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/portfolios.py` & `gs_quant-0.9.99/gs_quant/target/portfolios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/price.py` & `gs_quant-0.9.99/gs_quant/target/price.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/reports.py` & `gs_quant-0.9.99/gs_quant/target/reports.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/risk.py` & `gs_quant-0.9.99/gs_quant/target/risk.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/risk_models.py` & `gs_quant-0.9.99/gs_quant/target/risk_models.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/screens.py` & `gs_quant-0.9.99/gs_quant/target/screens.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/secmaster.py` & `gs_quant-0.9.99/gs_quant/target/secmaster.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/trades.py` & `gs_quant-0.9.99/gs_quant/target/trades.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/workflow_quote.py` & `gs_quant-0.9.99/gs_quant/target/workflow_quote.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/target/workspaces_markets.py` & `gs_quant-0.9.99/gs_quant/target/workspaces_markets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/analytics/test_datagrid.py` & `gs_quant-0.9.99/gs_quant/test/analytics/test_datagrid.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/analytics/test_sorting_and_filtering.py` & `gs_quant-0.9.99/gs_quant/test/analytics/test_sorting_and_filtering.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/analytics/test_workspace.py` & `gs_quant-0.9.99/gs_quant/test/analytics/test_workspace.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_assets.py` & `gs_quant-0.9.99/gs_quant/test/api/test_assets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_backtests.py` & `gs_quant-0.9.99/gs_quant/test/api/test_backtests.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_base_screener.py` & `gs_quant-0.9.99/gs_quant/test/api/test_base_screener.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_cache.py` & `gs_quant-0.9.99/gs_quant/test/api/test_cache.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_carbon.py` & `gs_quant-0.9.99/gs_quant/test/api/test_carbon.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_content.py` & `gs_quant-0.9.99/gs_quant/test/api/test_content.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_data.py` & `gs_quant-0.9.99/gs_quant/test/api/test_data.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_data_screen.py` & `gs_quant-0.9.99/gs_quant/test/api/test_data_screen.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_esg.py` & `gs_quant-0.9.99/gs_quant/test/api/test_esg.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_fred.py` & `gs_quant-0.9.99/gs_quant/test/api/test_fred.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_groups.py` & `gs_quant-0.9.99/gs_quant/test/api/test_groups.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_index.py` & `gs_quant-0.9.99/gs_quant/test/api/test_index.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_instruments.py` & `gs_quant-0.9.99/gs_quant/test/api/test_instruments.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_json.py` & `gs_quant-0.9.99/gs_quant/test/api/test_json.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_monitor.py` & `gs_quant-0.9.99/gs_quant/test/api/test_monitor.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_portfolios.py` & `gs_quant-0.9.99/gs_quant/test/api/test_portfolios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_reports.py` & `gs_quant-0.9.99/gs_quant/test/api/test_reports.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_risk.py` & `gs_quant-0.9.99/gs_quant/test/api/test_risk.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_risk_models.py` & `gs_quant-0.9.99/gs_quant/test/api/test_risk_models.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_target.py` & `gs_quant-0.9.99/gs_quant/test/api/test_target.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_thread_manager.py` & `gs_quant-0.9.99/gs_quant/test/api/test_thread_manager.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/api/test_users.py` & `gs_quant-0.9.99/gs_quant/test/api/test_users.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_eq_vol_engine.py` & `gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_eq_vol_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_flow_vol.py` & `gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_flow_vol.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/backtest/test_backtest_predefined.py` & `gs_quant-0.9.99/gs_quant/test/backtest/test_backtest_predefined.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/backtest/test_generic_engine.py` & `gs_quant-0.9.99/gs_quant/test/backtest/test_generic_engine.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/backtest/test_triggers.py` & `gs_quant-0.9.99/gs_quant/test/backtest/test_triggers.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/data/test_data_coordinate.py` & `gs_quant-0.9.99/gs_quant/test/data/test_data_coordinate.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/data/test_dataset.py` & `gs_quant-0.9.99/gs_quant/test/data/test_dataset.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/datetime_/test_date.py` & `gs_quant-0.9.99/gs_quant/test/datetime_/test_date.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/datetime_/test_gscalendar.py` & `gs_quant-0.9.99/gs_quant/test/datetime_/test_gscalendar.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/datetime_/test_point.py` & `gs_quant-0.9.99/gs_quant/test/datetime_/test_point.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/datetime_/test_relative_date.py` & `gs_quant-0.9.99/gs_quant/test/datetime_/test_relative_date.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/datetime_/test_time.py` & `gs_quant-0.9.99/gs_quant/test/datetime_/test_time.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/fixtures/content.py` & `gs_quant-0.9.99/gs_quant/test/fixtures/content.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_baskets.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_baskets.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_hedger.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_hedger.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_instrument.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_instrument.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_portfolio.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_portfolio.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_portfolio_manager.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_portfolio_manager.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_pricing_context.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_pricing_context.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_report.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_report.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/markets/test_securities.py` & `gs_quant-0.9.99/gs_quant/test/markets/test_securities.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/models/__init__.py` & `gs_quant-0.9.99/gs_quant/test/models/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/models/test_epidemiology.py` & `gs_quant-0.9.99/gs_quant/test/models/test_epidemiology.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/models/test_risk_model.py` & `gs_quant-0.9.99/gs_quant/test/models/test_risk_model.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/test_base.py` & `gs_quant-0.9.99/gs_quant/test/test_base.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/test_commod.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/test_commod.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/multi_measure/test_measure_registry.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/multi_measure/test_measure_registry.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_algebra.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_algebra.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_analysis.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_analysis.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_backtesting.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_backtesting.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_datetime.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_datetime.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_econometrics.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_econometrics.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_helper.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_helper.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_countries.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_countries.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_fx_vol.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_fx_vol.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_inflation.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_inflation.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_portfolios.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_portfolios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_rates.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_rates.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_reports.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_reports.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_risk_models.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_risk_models.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_measures_xccy.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_measures_xccy.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_rolling.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_rolling.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_statistics.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_statistics.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_tca.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_tca.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_technicals.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_technicals.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/test_timeseries.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/test_timeseries.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/timeseries/utils.py` & `gs_quant-0.9.99/gs_quant/test/timeseries/utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/utils/datagrid_test_utils.py` & `gs_quant-0.9.99/gs_quant/test/utils/datagrid_test_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/utils/mock_calc.py` & `gs_quant-0.9.99/gs_quant/test/utils/mock_calc.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/utils/mock_data.py` & `gs_quant-0.9.99/gs_quant/test/utils/mock_data.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/utils/mock_request.py` & `gs_quant-0.9.99/gs_quant/test/utils/mock_request.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/test/utils/test_utils.py` & `gs_quant-0.9.99/gs_quant/test/utils/test_utils.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/__init__.py` & `gs_quant-0.9.99/gs_quant/timeseries/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/algebra.py` & `gs_quant-0.9.99/gs_quant/timeseries/algebra.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/analysis.py` & `gs_quant-0.9.99/gs_quant/timeseries/analysis.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/backtesting.py` & `gs_quant-0.9.99/gs_quant/timeseries/backtesting.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/datetime.py` & `gs_quant-0.9.99/gs_quant/timeseries/datetime.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/econometrics.py` & `gs_quant-0.9.99/gs_quant/timeseries/econometrics.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/helper.py` & `gs_quant-0.9.99/gs_quant/timeseries/helper.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measure_registry.py` & `gs_quant-0.9.99/gs_quant/timeseries/measure_registry.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_countries.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_countries.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_fx_vol.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_fx_vol.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_helper.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_helper.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_inflation.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_inflation.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_portfolios.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_portfolios.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_rates.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_rates.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_reports.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_reports.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_risk_models.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_risk_models.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/measures_xccy.py` & `gs_quant-0.9.99/gs_quant/timeseries/measures_xccy.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/statistics.py` & `gs_quant-0.9.99/gs_quant/timeseries/statistics.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/tca.py` & `gs_quant-0.9.99/gs_quant/timeseries/tca.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/timeseries/technicals.py` & `gs_quant-0.9.99/gs_quant/timeseries/technicals.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/tracing/__init__.py` & `gs_quant-0.9.99/gs_quant/tracing/__init__.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant/tracing/tracing.py` & `gs_quant-0.9.99/gs_quant/tracing/tracing.py`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant.egg-info/PKG-INFO` & `gs_quant-0.9.99/gs_quant.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gs-quant
-Version: 0.9.98
+Version: 0.9.99
 Summary: Goldman Sachs Quant
 Home-page: https://marquee.gs.com
 Author: Goldman Sachs
 Author-email: developer@gs.com
 License: http://www.apache.org/licenses/LICENSE-2.0
 Description: # GS Quant
```

### Comparing `gs_quant-0.9.98/gs_quant.egg-info/SOURCES.txt` & `gs_quant-0.9.99/gs_quant.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gs_quant-0.9.98/gs_quant.egg-info/requires.txt` & `gs_quant-0.9.99/gs_quant.egg-info/requires.txt`

 * *Files 3% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 funcsigs
 inflection
 lmfit<=1.0.2
 more_itertools
 msgpack
 nest-asyncio
 opentracing
-pandas>1.0.0
+pandas<2.0.0,>1.0.0
 pydash
 python-dateutil>=2.7.0
 requests
 tqdm
 websockets
 
 [:python_version < "3.7"]
```

### Comparing `gs_quant-0.9.98/setup.py` & `gs_quant-0.9.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -64,15 +64,15 @@
         "funcsigs",
         "inflection",
         "lmfit<=1.0.2",  # version 1.0.3 requires a newer version of pip (21.3 works, but 18.1 doesn't)
         "more_itertools",
         "msgpack",
         "nest-asyncio",
         "opentracing",
-        "pandas>1.0.0",
+        "pandas>1.0.0,<2.0.0",
         "pydash",
         "python-dateutil>=2.7.0",
         "requests",
         "scipy>=1.2.0;python_version>'3.8'",
         "scipy>=1.2.0,<1.6.0;python_version<'3.7'",
         "scipy>=1.2.0,<1.8.0;python_version<'3.8'",
         "statsmodels<=0.12.2;python_version<'3.7'",
```

### Comparing `gs_quant-0.9.98/versioneer.py` & `gs_quant-0.9.99/versioneer.py`

 * *Files identical despite different names*

