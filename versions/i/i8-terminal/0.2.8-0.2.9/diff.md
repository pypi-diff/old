# Comparing `tmp/i8-terminal-0.2.8.tar.gz` & `tmp/i8-terminal-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "i8-terminal-0.2.8.tar", last modified: Thu Jun 16 18:04:40 2022, max compression
+gzip compressed data, was "i8-terminal-0.2.9.tar", last modified: Sat Jun 18 08:33:09 2022, max compression
```

## Comparing `i8-terminal-0.2.8.tar` & `i8-terminal-0.2.9.tar`

### file list

```diff
@@ -1,112 +1,113 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.877833 i8-terminal-0.2.8/
--rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      112 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3196 2022-06-16 18:04:40.877833 i8-terminal-0.2.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.865833 i8-terminal-0.2.8/i8_terminal/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.865833 i8-terminal-0.2.8/i8_terminal/app/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6618 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/app/layout.py
--rw-r--r--   0 runner    (1001) docker     (121)     5098 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/app/plot_server.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.865833 i8-terminal-0.2.8/i8_terminal/assets/
--rw-r--r--   0 runner    (1001) docker     (121)     2653 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/assets/favicon.ico
--rw-r--r--   0 runner    (1001) docker     (121)    10071 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/assets/i8t_chart_logo.png
--rw-r--r--   0 runner    (1001) docker     (121)    49202 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/assets/i8t_logo.png
--rw-r--r--   0 runner    (1001) docker     (121)    76185 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/assets/loading.gif
--rw-r--r--   0 runner    (1001) docker     (121)    13983 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/assets/styles.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.865833 i8-terminal-0.2.8/i8_terminal/commands/
--rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.865833 i8-terminal-0.2.8/i8_terminal/commands/company/
--rw-r--r--   0 runner    (1001) docker     (121)      185 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/company/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9590 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/company/company_compare.py
--rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/company/company_search.py
--rw-r--r--   0 runner    (1001) docker     (121)     2776 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/company/compnay_details.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/earnings/
--rw-r--r--   0 runner    (1001) docker     (121)      135 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/earnings/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1967 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     3533 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_plot.py
--rw-r--r--   0 runner    (1001) docker     (121)     1910 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_recent.py
--rw-r--r--   0 runner    (1001) docker     (121)     2739 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_upcoming.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/financials/
--rw-r--r--   0 runner    (1001) docker     (121)      139 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/financials/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     7407 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/financials/financials_compare.py
--rw-r--r--   0 runner    (1001) docker     (121)     1074 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/financials/financials_coverage.py
--rw-r--r--   0 runner    (1001) docker     (121)     4459 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/financials/financials_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     8262 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/financials/financials_plot.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/market/
--rw-r--r--   0 runner    (1001) docker     (121)      123 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/market/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10108 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/market/market_summary.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/metrics/
--rw-r--r--   0 runner    (1001) docker     (121)      133 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1204 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/metrics/metrics_describe.py
--rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/metrics/metrics_plot.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/news/
--rw-r--r--   0 runner    (1001) docker     (121)      130 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/news/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2407 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/news/news_list.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/price/
--rw-r--r--   0 runner    (1001) docker     (121)      149 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/price/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5130 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/price/price_compare.py
--rw-r--r--   0 runner    (1001) docker     (121)     2803 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/price/price_list.py
--rw-r--r--   0 runner    (1001) docker     (121)    10367 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/price/price_plot.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/screen/
--rw-r--r--   0 runner    (1001) docker     (121)      152 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/screen/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      292 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/screen/screen_list.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.869833 i8-terminal-0.2.8/i8_terminal/commands/user/
--rw-r--r--   0 runner    (1001) docker     (121)      107 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/user/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1717 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/user/user_login.py
--rw-r--r--   0 runner    (1001) docker     (121)      428 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/user/user_logout.py
--rw-r--r--   0 runner    (1001) docker     (121)     1843 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/user/webserver.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.873833 i8-terminal-0.2.8/i8_terminal/commands/watchlist/
--rw-r--r--   0 runner    (1001) docker     (121)      135 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1688 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_add.py
--rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_create.py
--rw-r--r--   0 runner    (1001) docker     (121)     2241 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_financials.py
--rw-r--r--   0 runner    (1001) docker     (121)     1330 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_list.py
--rw-r--r--   0 runner    (1001) docker     (121)     2536 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)     1799 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_rm.py
--rw-r--r--   0 runner    (1001) docker     (121)     2207 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_summary.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.873833 i8-terminal-0.2.8/i8_terminal/common/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1729 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)    11753 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/financials.py
--rw-r--r--   0 runner    (1001) docker     (121)     4117 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/formatting.py
--rw-r--r--   0 runner    (1001) docker     (121)     1740 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/layout.py
--rw-r--r--   0 runner    (1001) docker     (121)     4998 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)     3654 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/price.py
--rw-r--r--   0 runner    (1001) docker     (121)     1288 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/stock_info.py
--rw-r--r--   0 runner    (1001) docker     (121)     2885 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/common/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     4564 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/config.py
--rw-r--r--   0 runner    (1001) docker     (121)      966 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/config.yml
--rw-r--r--   0 runner    (1001) docker     (121)       39 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/i8_exception.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.873833 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3196 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3508 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       46 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      242 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-06-16 18:04:40.000000 i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)     5468 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/main.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:40.877833 i8-terminal-0.2.8/i8_terminal/types/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2138 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/auto_complete_choice.py
--rw-r--r--   0 runner    (1001) docker     (121)      705 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/chart_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     1917 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/command_parser.py
--rw-r--r--   0 runner    (1001) docker     (121)     1137 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/fin_identifier_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      914 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/fin_period_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      782 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/fin_statement_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     2222 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/i8_auto_suggest.py
--rw-r--r--   0 runner    (1001) docker     (121)     6929 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/i8_completer.py
--rw-r--r--   0 runner    (1001) docker     (121)     1909 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/indicator_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      750 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/metric_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      685 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/period_type_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      810 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/price_period_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)      592 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/ticker_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     1049 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/user_watchlist_tickers_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     1024 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/types/user_watchlists_param_type.py
--rw-r--r--   0 runner    (1001) docker     (121)     1030 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/i8_terminal/version.txt
--rw-r--r--   0 runner    (1001) docker     (121)      174 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      241 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-16 18:04:40.877833 i8-terminal-0.2.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1380 2022-06-16 18:04:00.000000 i8-terminal-0.2.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.160778 i8-terminal-0.2.9/
+-rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      112 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3196 2022-06-18 08:33:09.160778 i8-terminal-0.2.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2639 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.148778 i8-terminal-0.2.9/i8_terminal/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.148778 i8-terminal-0.2.9/i8_terminal/app/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6618 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/app/layout.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5098 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/app/plot_server.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.148778 i8-terminal-0.2.9/i8_terminal/assets/
+-rw-r--r--   0 runner    (1001) docker     (121)     2653 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/assets/favicon.ico
+-rw-r--r--   0 runner    (1001) docker     (121)    10071 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/assets/i8t_chart_logo.png
+-rw-r--r--   0 runner    (1001) docker     (121)    49202 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/assets/i8t_logo.png
+-rw-r--r--   0 runner    (1001) docker     (121)    76185 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/assets/loading.gif
+-rw-r--r--   0 runner    (1001) docker     (121)    13983 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/assets/styles.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.148778 i8-terminal-0.2.9/i8_terminal/commands/
+-rw-r--r--   0 runner    (1001) docker     (121)      426 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.148778 i8-terminal-0.2.9/i8_terminal/commands/company/
+-rw-r--r--   0 runner    (1001) docker     (121)      185 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/company/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9590 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/company/company_compare.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1279 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/company/company_search.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2776 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/company/compnay_details.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/earnings/
+-rw-r--r--   0 runner    (1001) docker     (121)      135 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/earnings/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1967 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3533 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_plot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1910 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_recent.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2739 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_upcoming.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/financials/
+-rw-r--r--   0 runner    (1001) docker     (121)      139 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/financials/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7407 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/financials/financials_compare.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1074 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/financials/financials_coverage.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4459 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/financials/financials_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8262 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/financials/financials_plot.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/market/
+-rw-r--r--   0 runner    (1001) docker     (121)      123 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/market/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10108 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/market/market_summary.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/metrics/
+-rw-r--r--   0 runner    (1001) docker     (121)      133 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1204 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/metrics/metrics_describe.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/metrics/metrics_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/metrics/metrics_plot.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/news/
+-rw-r--r--   0 runner    (1001) docker     (121)      130 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/news/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2407 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/news/news_list.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/price/
+-rw-r--r--   0 runner    (1001) docker     (121)      149 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/price/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5130 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/price/price_compare.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2803 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/price/price_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10367 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/price/price_plot.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/screen/
+-rw-r--r--   0 runner    (1001) docker     (121)      152 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/screen/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      292 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/screen/screen_list.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.152778 i8-terminal-0.2.9/i8_terminal/commands/user/
+-rw-r--r--   0 runner    (1001) docker     (121)      107 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/user/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1717 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/user/user_login.py
+-rw-r--r--   0 runner    (1001) docker     (121)      428 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/user/user_logout.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1843 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/user/webserver.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.156778 i8-terminal-0.2.9/i8_terminal/commands/watchlist/
+-rw-r--r--   0 runner    (1001) docker     (121)      135 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1688 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_add.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1079 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_create.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2241 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_financials.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1330 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_list.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2536 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1799 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_rm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2207 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_summary.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.156778 i8-terminal-0.2.9/i8_terminal/common/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1729 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11753 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/financials.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4117 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/formatting.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1740 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/layout.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4998 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3654 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/price.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1288 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/stock_info.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2885 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/common/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4564 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/config.py
+-rw-r--r--   0 runner    (1001) docker     (121)      966 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/config.yml
+-rw-r--r--   0 runner    (1001) docker     (121)       39 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/i8_exception.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.156778 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3196 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3553 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       46 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      242 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-06-18 08:33:09.000000 i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)     5468 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/main.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-18 08:33:09.160778 i8-terminal-0.2.9/i8_terminal/types/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2138 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/auto_complete_choice.py
+-rw-r--r--   0 runner    (1001) docker     (121)      705 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/chart_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1917 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/command_parser.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1137 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/fin_identifier_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      914 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/fin_period_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      782 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/fin_statement_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2222 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/i8_auto_suggest.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6929 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/i8_completer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1909 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/indicator_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      750 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/metric_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      685 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/period_type_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      810 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/price_period_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)      592 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/ticker_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1049 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/user_watchlist_tickers_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1024 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/types/user_watchlists_param_type.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1030 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/i8_terminal/version.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      174 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      241 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-18 08:33:09.160778 i8-terminal-0.2.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1380 2022-06-18 08:32:34.000000 i8-terminal-0.2.9/setup.py
```

### Comparing `i8-terminal-0.2.8/LICENSE` & `i8-terminal-0.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/PKG-INFO` & `i8-terminal-0.2.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: i8-terminal
-Version: 0.2.8
+Version: 0.2.9
 Summary: Investor8 CLI
 Home-page: UNKNOWN
 Author: investoreight
 Author-email: info@investoreight.com
 License: MIT
 Project-URL: Homepage, https://i8terminal.io/
 Project-URL: Documentation, https://docs.i8terminal.io/
```

### Comparing `i8-terminal-0.2.8/README.md` & `i8-terminal-0.2.9/README.md`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/app/layout.py` & `i8-terminal-0.2.9/i8_terminal/app/layout.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/app/plot_server.py` & `i8-terminal-0.2.9/i8_terminal/app/plot_server.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/assets/favicon.ico` & `i8-terminal-0.2.9/i8_terminal/assets/favicon.ico`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/assets/i8t_chart_logo.png` & `i8-terminal-0.2.9/i8_terminal/assets/i8t_chart_logo.png`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/assets/i8t_logo.png` & `i8-terminal-0.2.9/i8_terminal/assets/i8t_logo.png`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/assets/loading.gif` & `i8-terminal-0.2.9/i8_terminal/assets/loading.gif`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/assets/styles.css` & `i8-terminal-0.2.9/i8_terminal/assets/styles.css`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/company/company_compare.py` & `i8-terminal-0.2.9/i8_terminal/commands/company/company_compare.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/company/company_search.py` & `i8-terminal-0.2.9/i8_terminal/commands/company/company_search.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/company/compnay_details.py` & `i8-terminal-0.2.9/i8_terminal/commands/company/compnay_details.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_list.py` & `i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_list.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_plot.py` & `i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_plot.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_recent.py` & `i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_recent.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/earnings/earnings_upcoming.py` & `i8-terminal-0.2.9/i8_terminal/commands/earnings/earnings_upcoming.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/financials/financials_compare.py` & `i8-terminal-0.2.9/i8_terminal/commands/financials/financials_compare.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/financials/financials_coverage.py` & `i8-terminal-0.2.9/i8_terminal/commands/financials/financials_coverage.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/financials/financials_list.py` & `i8-terminal-0.2.9/i8_terminal/commands/financials/financials_list.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/financials/financials_plot.py` & `i8-terminal-0.2.9/i8_terminal/commands/financials/financials_plot.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/market/market_summary.py` & `i8-terminal-0.2.9/i8_terminal/commands/market/market_summary.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/metrics/metrics_describe.py` & `i8-terminal-0.2.9/i8_terminal/commands/metrics/metrics_describe.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/metrics/metrics_plot.py` & `i8-terminal-0.2.9/i8_terminal/commands/metrics/metrics_plot.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/news/news_list.py` & `i8-terminal-0.2.9/i8_terminal/commands/news/news_list.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/price/price_compare.py` & `i8-terminal-0.2.9/i8_terminal/commands/price/price_compare.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/price/price_list.py` & `i8-terminal-0.2.9/i8_terminal/commands/price/price_list.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/price/price_plot.py` & `i8-terminal-0.2.9/i8_terminal/commands/price/price_plot.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/user/user_login.py` & `i8-terminal-0.2.9/i8_terminal/commands/user/user_login.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/user/webserver.py` & `i8-terminal-0.2.9/i8_terminal/commands/user/webserver.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_add.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_add.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_create.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_create.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_financials.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_financials.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_list.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_list.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_metrics.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_metrics.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_rm.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_rm.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/commands/watchlist/watchlist_summary.py` & `i8-terminal-0.2.9/i8_terminal/commands/watchlist/watchlist_summary.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/cli.py` & `i8-terminal-0.2.9/i8_terminal/common/cli.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/financials.py` & `i8-terminal-0.2.9/i8_terminal/common/financials.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/formatting.py` & `i8-terminal-0.2.9/i8_terminal/common/formatting.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/layout.py` & `i8-terminal-0.2.9/i8_terminal/common/layout.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/metrics.py` & `i8-terminal-0.2.9/i8_terminal/common/metrics.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/price.py` & `i8-terminal-0.2.9/i8_terminal/common/price.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/stock_info.py` & `i8-terminal-0.2.9/i8_terminal/common/stock_info.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/common/utils.py` & `i8-terminal-0.2.9/i8_terminal/common/utils.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/config.py` & `i8-terminal-0.2.9/i8_terminal/config.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/config.yml` & `i8-terminal-0.2.9/i8_terminal/config.yml`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/PKG-INFO` & `i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: i8-terminal
-Version: 0.2.8
+Version: 0.2.9
 Summary: Investor8 CLI
 Home-page: UNKNOWN
 Author: investoreight
 Author-email: info@investoreight.com
 License: MIT
 Project-URL: Homepage, https://i8terminal.io/
 Project-URL: Documentation, https://docs.i8terminal.io/
```

### Comparing `i8-terminal-0.2.8/i8_terminal/i8_terminal.egg-info/SOURCES.txt` & `i8-terminal-0.2.9/i8_terminal/i8_terminal.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -34,14 +34,15 @@
 i8_terminal/commands/financials/financials_coverage.py
 i8_terminal/commands/financials/financials_list.py
 i8_terminal/commands/financials/financials_plot.py
 i8_terminal/commands/market/__init__.py
 i8_terminal/commands/market/market_summary.py
 i8_terminal/commands/metrics/__init__.py
 i8_terminal/commands/metrics/metrics_describe.py
+i8_terminal/commands/metrics/metrics_list.py
 i8_terminal/commands/metrics/metrics_plot.py
 i8_terminal/commands/news/__init__.py
 i8_terminal/commands/news/news_list.py
 i8_terminal/commands/price/__init__.py
 i8_terminal/commands/price/price_compare.py
 i8_terminal/commands/price/price_list.py
 i8_terminal/commands/price/price_plot.py
```

### Comparing `i8-terminal-0.2.8/i8_terminal/main.py` & `i8-terminal-0.2.9/i8_terminal/main.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/auto_complete_choice.py` & `i8-terminal-0.2.9/i8_terminal/types/auto_complete_choice.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/chart_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/chart_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/command_parser.py` & `i8-terminal-0.2.9/i8_terminal/types/command_parser.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/fin_identifier_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/fin_identifier_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/fin_period_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/fin_period_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/fin_statement_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/fin_statement_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/i8_auto_suggest.py` & `i8-terminal-0.2.9/i8_terminal/types/i8_auto_suggest.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/i8_completer.py` & `i8-terminal-0.2.9/i8_terminal/types/i8_completer.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/indicator_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/indicator_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/metric_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/metric_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/period_type_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/period_type_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/price_period_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/price_period_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/ticker_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/ticker_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/user_watchlist_tickers_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/user_watchlist_tickers_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/types/user_watchlists_param_type.py` & `i8-terminal-0.2.9/i8_terminal/types/user_watchlists_param_type.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/i8_terminal/utils.py` & `i8-terminal-0.2.9/i8_terminal/utils.py`

 * *Files identical despite different names*

### Comparing `i8-terminal-0.2.8/setup.py` & `i8-terminal-0.2.9/setup.py`

 * *Files identical despite different names*

