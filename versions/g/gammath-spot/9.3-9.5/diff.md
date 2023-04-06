# Comparing `tmp/gammath_spot-9.3.tar.gz` & `tmp/gammath_spot-9.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gammath_spot-9.3.tar", last modified: Tue Feb 28 14:24:09 2023, max compression
+gzip compressed data, was "gammath_spot-9.5.tar", last modified: Tue Mar 14 22:51:24 2023, max compression
```

## Comparing `gammath_spot-9.3.tar` & `gammath_spot-9.5.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-02-28 14:24:09.327993 gammath_spot-9.3/
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    35149 2021-11-18 08:22:38.000000 gammath_spot-9.3/LICENSE.txt
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)       19 2022-11-30 04:05:03.000000 gammath_spot-9.3/MANIFEST.in
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)    11359 2023-02-28 14:24:09.327673 gammath_spot-9.3/PKG-INFO
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10860 2023-02-27 23:42:17.000000 gammath_spot-9.3/README.md
-drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-02-28 14:24:09.323941 gammath_spot-9.3/gammath_spot/
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)      856 2023-01-04 18:55:17.000000 gammath_spot-9.3/gammath_spot/__init__.py
-drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-02-28 14:24:09.327000 gammath_spot-9.3/gammath_spot/data/
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10128 2022-11-30 18:34:05.000000 gammath_spot-9.3/gammath_spot/data/logo.png
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    21366 2023-02-16 16:28:36.000000 gammath_spot-9.3/gammath_spot/gammath_backtesting.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2955 2023-02-09 00:21:27.000000 gammath_spot-9.3/gammath_spot/gammath_bb_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1782 2023-01-26 01:13:54.000000 gammath_spot-9.3/gammath_spot/gammath_beta_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1531 2023-02-09 00:22:04.000000 gammath_spot-9.3/gammath_spot/gammath_get_stcktwts.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2055 2023-02-20 20:28:58.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_calendar.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3955 2023-02-16 23:49:41.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_data.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1775 2023-02-09 00:23:28.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_events_data.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5351 2023-02-20 20:27:54.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_financials.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3516 2023-02-09 00:19:30.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_history.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3121 2023-02-20 20:27:32.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_options_data.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3630 2023-02-20 20:23:22.000000 gammath_spot-9.3/gammath_spot/gammath_get_stocks_summary.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     9803 2023-02-20 17:36:41.000000 gammath_spot-9.3/gammath_spot/gammath_gscores_history.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1848 2023-02-22 00:06:12.000000 gammath_spot-9.3/gammath_spot/gammath_ihp_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1673 2023-02-22 00:07:01.000000 gammath_spot-9.3/gammath_spot/gammath_inshp_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     8607 2023-02-20 17:35:44.000000 gammath_spot-9.3/gammath_spot/gammath_kf_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3964 2023-02-20 17:35:27.000000 gammath_spot-9.3/gammath_spot/gammath_lgstic_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10098 2023-02-20 17:55:40.000000 gammath_spot-9.3/gammath_spot/gammath_lpep.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10140 2023-02-20 17:31:52.000000 gammath_spot-9.3/gammath_spot/gammath_macd_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3762 2023-02-09 00:31:02.000000 gammath_spot-9.3/gammath_spot/gammath_mfi_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1776 2023-01-04 18:55:41.000000 gammath_spot-9.3/gammath_spot/gammath_mi_scores.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2083 2023-01-17 19:50:07.000000 gammath_spot-9.3/gammath_spot/gammath_mtpc.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10747 2023-02-07 18:35:06.000000 gammath_spot-9.3/gammath_spot/gammath_ols_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4300 2023-02-20 17:31:36.000000 gammath_spot-9.3/gammath_spot/gammath_options_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1991 2023-02-22 00:04:56.000000 gammath_spot-9.3/gammath_spot/gammath_pbr_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4208 2023-02-09 00:34:57.000000 gammath_spot-9.3/gammath_spot/gammath_pdp.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3448 2023-02-21 23:33:42.000000 gammath_spot-9.3/gammath_spot/gammath_pe_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1536 2023-02-20 17:30:22.000000 gammath_spot-9.3/gammath_spot/gammath_peg_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     8186 2023-02-20 17:30:05.000000 gammath_spot-9.3/gammath_spot/gammath_price_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5267 2023-02-22 00:03:41.000000 gammath_spot-9.3/gammath_spot/gammath_qbs_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4368 2023-01-26 20:08:56.000000 gammath_spot-9.3/gammath_spot/gammath_reco_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5288 2023-02-20 17:29:33.000000 gammath_spot-9.3/gammath_spot/gammath_rsi_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3361 2023-02-20 17:29:11.000000 gammath_spot-9.3/gammath_spot/gammath_si_charts.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3039 2023-02-09 00:38:47.000000 gammath_spot-9.3/gammath_spot/gammath_stcktwts_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3094 2023-02-07 18:34:58.000000 gammath_spot-9.3/gammath_spot/gammath_stoch_signals.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    25254 2023-02-24 23:47:27.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_analysis.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4291 2023-02-24 17:48:54.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_analyzer_and_scorer.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4265 2023-02-24 17:49:17.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_backtesting.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4121 2023-02-24 17:48:46.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_data_scraper.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4069 2023-02-24 17:49:10.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_gscores_historian.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4302 2023-02-24 17:49:03.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_pep.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4762 2023-02-28 14:03:41.000000 gammath_spot-9.3/gammath_spot/gammath_stocks_screener.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    22577 2023-02-20 17:21:32.000000 gammath_spot-9.3/gammath_spot/gammath_tc.py
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)    17042 2023-02-24 23:47:21.000000 gammath_spot-9.3/gammath_spot/gammath_utils.py
-drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-02-28 14:24:09.326667 gammath_spot-9.3/gammath_spot.egg-info/
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)    11359 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/PKG-INFO
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)     1986 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/SOURCES.txt
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)        1 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/dependency_links.txt
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)      407 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/entry_points.txt
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)        1 2021-11-18 06:07:22.000000 gammath_spot-9.3/gammath_spot.egg-info/not-zip-safe
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)      104 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/requires.txt
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)       13 2023-02-28 14:24:09.000000 gammath_spot-9.3/gammath_spot.egg-info/top_level.txt
--rw-r--r--   0 gammath_mlalgo   (505) staff       (20)       38 2023-02-28 14:24:09.328079 gammath_spot-9.3/setup.cfg
--r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2241 2023-02-28 00:31:28.000000 gammath_spot-9.3/setup.py
+drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-03-14 22:51:24.797389 gammath_spot-9.5/
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    35149 2021-11-18 08:22:38.000000 gammath_spot-9.5/LICENSE.txt
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)       19 2022-11-30 04:05:03.000000 gammath_spot-9.5/MANIFEST.in
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)    11440 2023-03-14 22:51:24.797047 gammath_spot-9.5/PKG-INFO
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10941 2023-03-14 21:35:34.000000 gammath_spot-9.5/README.md
+drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-03-14 22:51:24.792994 gammath_spot-9.5/gammath_spot/
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)      856 2023-01-04 18:55:17.000000 gammath_spot-9.5/gammath_spot/__init__.py
+drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-03-14 22:51:24.796306 gammath_spot-9.5/gammath_spot/data/
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10128 2022-11-30 18:34:05.000000 gammath_spot-9.5/gammath_spot/data/logo.png
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    21366 2023-02-16 16:28:36.000000 gammath_spot-9.5/gammath_spot/gammath_backtesting.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2955 2023-02-09 00:21:27.000000 gammath_spot-9.5/gammath_spot/gammath_bb_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1782 2023-01-26 01:13:54.000000 gammath_spot-9.5/gammath_spot/gammath_beta_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1531 2023-02-09 00:22:04.000000 gammath_spot-9.5/gammath_spot/gammath_get_stcktwts.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2055 2023-02-20 20:28:58.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_calendar.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3955 2023-02-16 23:49:41.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_data.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1775 2023-02-09 00:23:28.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_events_data.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5351 2023-02-20 20:27:54.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_financials.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3516 2023-02-09 00:19:30.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_history.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3121 2023-02-20 20:27:32.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_options_data.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3630 2023-02-20 20:23:22.000000 gammath_spot-9.5/gammath_spot/gammath_get_stocks_summary.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     9803 2023-02-20 17:36:41.000000 gammath_spot-9.5/gammath_spot/gammath_gscores_history.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1848 2023-02-22 00:06:12.000000 gammath_spot-9.5/gammath_spot/gammath_ihp_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1673 2023-02-22 00:07:01.000000 gammath_spot-9.5/gammath_spot/gammath_inshp_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     8607 2023-02-20 17:35:44.000000 gammath_spot-9.5/gammath_spot/gammath_kf_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3964 2023-02-20 17:35:27.000000 gammath_spot-9.5/gammath_spot/gammath_lgstic_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10098 2023-02-20 17:55:40.000000 gammath_spot-9.5/gammath_spot/gammath_lpep.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10140 2023-02-20 17:31:52.000000 gammath_spot-9.5/gammath_spot/gammath_macd_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3762 2023-02-09 00:31:02.000000 gammath_spot-9.5/gammath_spot/gammath_mfi_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1776 2023-01-04 18:55:41.000000 gammath_spot-9.5/gammath_spot/gammath_mi_scores.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2083 2023-01-17 19:50:07.000000 gammath_spot-9.5/gammath_spot/gammath_mtpc.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    10747 2023-02-07 18:35:06.000000 gammath_spot-9.5/gammath_spot/gammath_ols_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4300 2023-02-20 17:31:36.000000 gammath_spot-9.5/gammath_spot/gammath_options_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1991 2023-02-22 00:04:56.000000 gammath_spot-9.5/gammath_spot/gammath_pbr_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4208 2023-02-09 00:34:57.000000 gammath_spot-9.5/gammath_spot/gammath_pdp.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3448 2023-02-21 23:33:42.000000 gammath_spot-9.5/gammath_spot/gammath_pe_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     1536 2023-02-20 17:30:22.000000 gammath_spot-9.5/gammath_spot/gammath_peg_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     8186 2023-02-20 17:30:05.000000 gammath_spot-9.5/gammath_spot/gammath_price_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5267 2023-02-22 00:03:41.000000 gammath_spot-9.5/gammath_spot/gammath_qbs_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4368 2023-01-26 20:08:56.000000 gammath_spot-9.5/gammath_spot/gammath_reco_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5288 2023-02-20 17:29:33.000000 gammath_spot-9.5/gammath_spot/gammath_rsi_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3361 2023-02-20 17:29:11.000000 gammath_spot-9.5/gammath_spot/gammath_si_charts.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3127 2023-03-03 19:40:30.000000 gammath_spot-9.5/gammath_spot/gammath_stcktwts_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     3094 2023-02-07 18:34:58.000000 gammath_spot-9.5/gammath_spot/gammath_stoch_signals.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    25254 2023-02-24 23:47:27.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_analysis.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4615 2023-03-14 21:13:31.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_analyzer_and_scorer.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4513 2023-03-14 21:15:33.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_backtesting.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4371 2023-03-14 21:06:48.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_data_scraper.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4307 2023-03-14 21:14:52.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_gscores_historian.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     4579 2023-03-14 21:14:04.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_pep.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     5041 2023-03-14 21:16:09.000000 gammath_spot-9.5/gammath_spot/gammath_stocks_screener.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    22577 2023-02-20 17:21:32.000000 gammath_spot-9.5/gammath_spot/gammath_tc.py
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)    17628 2023-03-09 22:51:22.000000 gammath_spot-9.5/gammath_spot/gammath_utils.py
+drwxr-xr-x   0 gammath_mlalgo   (505) staff       (20)        0 2023-03-14 22:51:24.795966 gammath_spot-9.5/gammath_spot.egg-info/
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)    11440 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/PKG-INFO
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)     1986 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/SOURCES.txt
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)        1 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/dependency_links.txt
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)      407 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/entry_points.txt
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)        1 2021-11-18 06:07:22.000000 gammath_spot-9.5/gammath_spot.egg-info/not-zip-safe
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)      104 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/requires.txt
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)       13 2023-03-14 22:51:24.000000 gammath_spot-9.5/gammath_spot.egg-info/top_level.txt
+-rw-r--r--   0 gammath_mlalgo   (505) staff       (20)       38 2023-03-14 22:51:24.797482 gammath_spot-9.5/setup.cfg
+-r--r--r--   0 gammath_mlalgo   (505) staff       (20)     2241 2023-03-14 22:29:06.000000 gammath_spot-9.5/setup.py
```

### Comparing `gammath_spot-9.3/LICENSE.txt` & `gammath_spot-9.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/PKG-INFO` & `gammath_spot-9.5/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,7 @@
-Metadata-Version: 2.1
-Name: gammath_spot
-Version: 9.3
-Summary: Stock Price-Opining Tools
-Home-page: https://github.com/salylgw/gammath_spot.git
-Author: Salyl Bhagwat
-Author-email: salylgw@gmail.com
-Classifier: Development Status :: 4 - Beta
-Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Topic :: Office/Business :: Financial :: Investment
-Description-Content-Type: text/markdown
-License-File: LICENSE.txt
-
 
 ![Alt text](https://raw.githubusercontent.com/salylgw/gammath_spot/main/gammath_spot/data/logo.png)
 
 # Gammath™ SPOT
 **S**tock **P**rice-**O**pining **T**ool is a DIY stock technical analysis software. It is used to analyze stocks and compute gScore (Gammath's 'stock analysis score) that indicates the degree to which a stock is trading at a perceived discount or perceived premium. It also provides tools to generate price projection, gScore-history, backtesting and stock screening. Together, these can help in making your own stock-specific buy, sell, hold decisions.
 
 
@@ -80,15 +66,15 @@
  4. Note: You can replace the value for TZ to match your timezone.
 
 
 # HOWTO run these apps
 1. If you installed this software then run: `gammath_scraper sample_watchlist.csv > log_scraper.txt`. See  [sample_watchlist.csv](https://github.com/salylgw/gammath_spot/blob/main/gammath_spot/sample_watchlist.csv). If not installed but just obtained the source code then go to the directory gammath_spot/gammath_spot where all the source files are and run: `python gammath_stocks_data_scraper.py sample_watchlist.csv > log_scraper.txt`.
 1. Above step will save the scraper log in `log_scraper.txt` and save the scraped, formatted data in `tickers` sub-directory. Running the data scraper is essential to be able to use rest of the tools.
 1. If you installed this software then run: `gammath_scorer sample_watchlist.csv > log_scorer.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_analyzer_and_scorer.py sample_watchlist.csv > log_scorer.txt`.
-1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `overall_gscores.csv` in your favorite spreadsheet program or a text editor. In `overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
+1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `<watchlist_name>_overall_gscores.csv` (e.g.: `sample_watchlist_overall_gscores.csv`) in your favorite spreadsheet program or a text editor. In `<watchlist_name>_overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
 1. If you want to generate estimated price projection and have installed this software then run: `gammath_projector sample_watchlist.csv > log_projector.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_pep.py sample_watchlist.csv > log_projector.txt`.
 1. Price projection chart and projections are saved in `tickers/<ticker-symbol>` dir. Chart and projection for S&P500 are saved in `tickers` dir. `<ticker-symbol>_pep.pdf` shows the chart and `<ticker-symbol>_pp.csv` shows the projected values. A sorted list of moving estimated projected 5Y returns are saved in `tickers/MPEP.csv`.
 1. In case you want to generate historical gscores (for correlation, past performance, backtesting etc.) then you can do so by using the gScores historian tool. Please note that this tool takes a long time to run so limit the watchlist for this tool to few selected stocks that you want to zoom into. If you installed this software then run: `gammath_historian sample_watchlist.csv > log_historian.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_gscores_historian.py sample_watchlist.csv > log_historian.txt`.
 1. You can check the `tickers/<ticker-symbol>/<ticker-symbol>_micro_gscores.csv` (for stock history based micro-gScores and corresponding total gScore) and `tickers/<ticker-symbol>/<ticker-symbol>_gscores_charts.pdf` that shows the plotted charts of price, overall stock history based gScore and micro-gScores.
 1. You can do backtesting on provided watchlist. If you installed this software then run: `gammath_backtester sample_watchlist.csv > log_backtester.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_backtesting.py sample_watchlist.csv > log_backtester.txt`. You can update the function locally for implementing your own strategy.
 1. For each stock, it processes (based on a strategy you implement/use) the data collected by scraper app and processes the stock history based gScore/micro-gScores for approximately last 5 years (that were saved from the gscore historian) and saves the backtesting stats in `tickers/<ticker_symbol>/<ticker_symbol>_gtrades_stats.csv`. You can check the backtesting stats to understand if the strategy you use worked historically and then decide whether to use that strategy or not. A sorted list of "Today's Actions" summary associated with default backtested strategy is saved in `tickers/Todays_Actions.csv`.
 1. If you want to screen stocks based on micro-gScores and have installed this software then run: `gammath_screener screener.csv > log_screener.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_screener.py screener.csv > log_screener.txt`. Note that the filtering criteria (micro-gScores values) is specified in `screener.csv` and the results can be found in `tickers/screened_watchlist.csv`.
```

### Comparing `gammath_spot-9.3/README.md` & `gammath_spot-9.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,21 @@
+Metadata-Version: 2.1
+Name: gammath_spot
+Version: 9.5
+Summary: Stock Price-Opining Tools
+Home-page: https://github.com/salylgw/gammath_spot.git
+Author: Salyl Bhagwat
+Author-email: salylgw@gmail.com
+Classifier: Development Status :: 4 - Beta
+Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Topic :: Office/Business :: Financial :: Investment
+Description-Content-Type: text/markdown
+License-File: LICENSE.txt
+
 
 ![Alt text](https://raw.githubusercontent.com/salylgw/gammath_spot/main/gammath_spot/data/logo.png)
 
 # Gammath™ SPOT
 **S**tock **P**rice-**O**pining **T**ool is a DIY stock technical analysis software. It is used to analyze stocks and compute gScore (Gammath's 'stock analysis score) that indicates the degree to which a stock is trading at a perceived discount or perceived premium. It also provides tools to generate price projection, gScore-history, backtesting and stock screening. Together, these can help in making your own stock-specific buy, sell, hold decisions.
 
 
@@ -66,15 +80,15 @@
  4. Note: You can replace the value for TZ to match your timezone.
 
 
 # HOWTO run these apps
 1. If you installed this software then run: `gammath_scraper sample_watchlist.csv > log_scraper.txt`. See  [sample_watchlist.csv](https://github.com/salylgw/gammath_spot/blob/main/gammath_spot/sample_watchlist.csv). If not installed but just obtained the source code then go to the directory gammath_spot/gammath_spot where all the source files are and run: `python gammath_stocks_data_scraper.py sample_watchlist.csv > log_scraper.txt`.
 1. Above step will save the scraper log in `log_scraper.txt` and save the scraped, formatted data in `tickers` sub-directory. Running the data scraper is essential to be able to use rest of the tools.
 1. If you installed this software then run: `gammath_scorer sample_watchlist.csv > log_scorer.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_analyzer_and_scorer.py sample_watchlist.csv > log_scorer.txt`.
-1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `overall_gscores.csv` in your favorite spreadsheet program or a text editor. In `overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
+1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `<watchlist_name>_overall_gscores.csv` (e.g.: `sample_watchlist_overall_gscores.csv`) in your favorite spreadsheet program or a text editor. In `<watchlist_name>_overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
 1. If you want to generate estimated price projection and have installed this software then run: `gammath_projector sample_watchlist.csv > log_projector.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_pep.py sample_watchlist.csv > log_projector.txt`.
 1. Price projection chart and projections are saved in `tickers/<ticker-symbol>` dir. Chart and projection for S&P500 are saved in `tickers` dir. `<ticker-symbol>_pep.pdf` shows the chart and `<ticker-symbol>_pp.csv` shows the projected values. A sorted list of moving estimated projected 5Y returns are saved in `tickers/MPEP.csv`.
 1. In case you want to generate historical gscores (for correlation, past performance, backtesting etc.) then you can do so by using the gScores historian tool. Please note that this tool takes a long time to run so limit the watchlist for this tool to few selected stocks that you want to zoom into. If you installed this software then run: `gammath_historian sample_watchlist.csv > log_historian.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_gscores_historian.py sample_watchlist.csv > log_historian.txt`.
 1. You can check the `tickers/<ticker-symbol>/<ticker-symbol>_micro_gscores.csv` (for stock history based micro-gScores and corresponding total gScore) and `tickers/<ticker-symbol>/<ticker-symbol>_gscores_charts.pdf` that shows the plotted charts of price, overall stock history based gScore and micro-gScores.
 1. You can do backtesting on provided watchlist. If you installed this software then run: `gammath_backtester sample_watchlist.csv > log_backtester.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_backtesting.py sample_watchlist.csv > log_backtester.txt`. You can update the function locally for implementing your own strategy.
 1. For each stock, it processes (based on a strategy you implement/use) the data collected by scraper app and processes the stock history based gScore/micro-gScores for approximately last 5 years (that were saved from the gscore historian) and saves the backtesting stats in `tickers/<ticker_symbol>/<ticker_symbol>_gtrades_stats.csv`. You can check the backtesting stats to understand if the strategy you use worked historically and then decide whether to use that strategy or not. A sorted list of "Today's Actions" summary associated with default backtested strategy is saved in `tickers/Todays_Actions.csv`.
 1. If you want to screen stocks based on micro-gScores and have installed this software then run: `gammath_screener screener.csv > log_screener.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_screener.py screener.csv > log_screener.txt`. Note that the filtering criteria (micro-gScores values) is specified in `screener.csv` and the results can be found in `tickers/screened_watchlist.csv`.
```

### Comparing `gammath_spot-9.3/gammath_spot/__init__.py` & `gammath_spot-9.5/gammath_spot/__init__.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/data/logo.png` & `gammath_spot-9.5/gammath_spot/data/logo.png`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_backtesting.py` & `gammath_spot-9.5/gammath_spot/gammath_backtesting.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_bb_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_bb_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_beta_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_beta_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stcktwts.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stcktwts.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_calendar.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_calendar.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_data.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_data.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_events_data.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_events_data.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_financials.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_financials.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_history.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_history.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_options_data.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_options_data.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_get_stocks_summary.py` & `gammath_spot-9.5/gammath_spot/gammath_get_stocks_summary.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_gscores_history.py` & `gammath_spot-9.5/gammath_spot/gammath_gscores_history.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_ihp_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_ihp_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_inshp_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_inshp_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_kf_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_kf_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_lgstic_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_lgstic_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_lpep.py` & `gammath_spot-9.5/gammath_spot/gammath_lpep.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_macd_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_macd_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_mfi_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_mfi_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_mi_scores.py` & `gammath_spot-9.5/gammath_spot/gammath_mi_scores.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_mtpc.py` & `gammath_spot-9.5/gammath_spot/gammath_mtpc.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_ols_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_ols_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_options_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_options_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_pbr_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_pbr_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_pdp.py` & `gammath_spot-9.5/gammath_spot/gammath_pdp.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_pe_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_pe_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_peg_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_peg_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_price_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_price_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_qbs_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_qbs_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_reco_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_reco_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_rsi_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_rsi_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_si_charts.py` & `gammath_spot-9.5/gammath_spot/gammath_si_charts.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stcktwts_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_stcktwts_signals.py`

 * *Files 4% similar despite different names*

```diff
@@ -59,36 +59,37 @@
         sts_change = 0
         stv_change = 0
 
         if (sentiment_change is not None):
             #Convert to the float type
             sts_change = float(sentiment_change)
             st_tw_sentiment_change = f'sentiment_change: {sentiment_change}'
+            if (sts_change > 0):
+                st_gscore += 2
         else:
             st_string += 'No sentiments change data'
 
         if (volume_change is not None):
             #Convert to the float type
             stv_change = float(volume_change)
             st_tw_volume_change = f'volume_change: {volume_change}'
+            if ((sts_change > 0) and (stv_change > 0)):
+                st_gscore += 3
         else:
             st_string += ' No discussion volume change data'
 
-        #Token score and information logging purpose
-        if ((sts_change > 0) and (stv_change > 0)):
-            st_gscore += 5
-        elif (sts_change > 0):
-            st_gscore += 2
-        else:
-            st_gscore -= 5
-
+        #Check for -ve sentiment
+        if ((sts_change < 0) and (stv_change < 0)):
+            st_gscore = -5
+        elif (sts_change < 0):
+            st_gscore = -2
     except:
         st_string += 'No stocktwits data'
 
-    st_max_score += 5
+    st_max_score = 5
 
     st_grec = f'st_sv_gscore:{st_gscore}/{st_max_score}'
 
     st_signals = f'{st_string},{st_grec}'
 
     return st_gscore, st_max_score, st_signals
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stoch_signals.py` & `gammath_spot-9.5/gammath_spot/gammath_stoch_signals.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_analysis.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_analysis.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_analyzer_and_scorer.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_analyzer_and_scorer.py`

 * *Files 9% similar despite different names*

```diff
@@ -16,107 +16,116 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 import time
 import multiprocessing as mp
+import queue
 try:
     from gammath_spot import gammath_stocks_analysis as gsa
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_stocks_analysis as gsa
     import gammath_utils as gut
 
 import pandas as pd
 import sys
 
-def main():
-    """
-    Main function to analyze and compute score for each stock in the provided watchlist. For each stock, it processes the data collected by scraper app, computes the score and saves score and useful signals in tickers/<ticker_symbol>. List of all gScores is in tickers/overall_gscores.csv
-    """
-
-    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
-    try:
-        #Get the watchlist file from pgm argument
-        sf_name = sys.argv[1]
-    except:
-        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
-        raise ValueError('Missing watch list')
+def run_analyzer_and_scorer(sf_name, info_queue):
 
     #Read the watchlist
     try:
         watch_list = pd.read_csv(sf_name)
     except:
-        print('ERROR: Failed to read watchlist. See watchlist.csv for example')
-        raise ValueError('Watchlist file read failed')
+        print('ERROR: Failed to read watchlist. See sample_watchlist.csv for example')
+        return
 
-    #Set the start method for launching parallel processes
-    #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
-    #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
-    mp.set_start_method('spawn')
+    print('\nStart Time: ', time.strftime('%x %X'), '\n')
 
-    #Get the number of usable CPUs
-    cores_to_use = gut.get_usable_cpu_count()
+    try:
+        #Set the start method for launching parallel processes
+        #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
+        #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
+        mp.set_start_method('spawn')
 
-    print(f'\nAttempting to use {cores_to_use} CPUs\n')
-    print('\nStart Time: ', time.strftime('%x %X'), '\n')
+        #Get the number of usable CPUs
+        cores_to_use = gut.get_usable_cpu_count()
+
+        print(f'\n{cores_to_use} usable CPUs\n')
 
-    proc_handles = []
+        proc_handles = []
 
-    max_tickers = len(watch_list)
+        max_tickers = len(watch_list)
 
-    #Use one process per core so we can run core_to_use number of processes in parallel
-    start_index = 0
-    if (max_tickers > cores_to_use):
-        end_index = cores_to_use
-    else:
-        end_index = max_tickers
+        #Use one process per core so we can run core_to_use number of processes in parallel
+        start_index = 0
+        if (max_tickers > cores_to_use):
+            end_index = cores_to_use
+        else:
+            end_index = max_tickers
 
-    #Instances of GSA class
-    gsa_instances = []
+        #Instances of GSA class
+        gsa_instances = []
 
-    #Create symbols list
-    symbols_list = []
+        #Create symbols list
+        symbols_list = []
 
-    while (max_tickers):
-        for i in range(start_index, end_index):
-            sym = watch_list['Symbol'][i].strip()
-            tsymbol = f'{sym}'
-            symbols_list.append(tsymbol)
-            df_history = pd.DataFrame()
+        while (max_tickers):
+            for i in range(start_index, end_index):
+                sym = watch_list['Symbol'][i].strip()
+                tsymbol = f'{sym}'
+                symbols_list.append(tsymbol)
+                df_history = pd.DataFrame()
 
-            gsa_instances.append(gsa.GSA())
-            proc_handles.append(mp.Process(target=gsa_instances[i].do_stock_analysis_and_compute_score, args=(f'{sym}',df_history,)))
-            proc_handles[i].start()
+                gsa_instances.append(gsa.GSA())
+                proc_handles.append(mp.Process(target=gsa_instances[i].do_stock_analysis_and_compute_score, args=(f'{sym}',df_history,)))
+                proc_handles[i].start()
 
-            max_tickers -= 1
+                max_tickers -= 1
 
-        for i in range(start_index, end_index):
-            proc_handles[i].join()
+            for i in range(start_index, end_index):
+                proc_handles[i].join()
 
-            #Delete the GSA instance
-            gsa_instance = gsa_instances[i]
-            gsa_instances[i] = 0
-            del gsa_instance
+                #Delete the GSA instance
+                gsa_instance = gsa_instances[i]
+                gsa_instances[i] = 0
+                del gsa_instance
 
-            #Running out of resources so need to close handles and release resources
-            proc_handles[i].close()
+                #Running out of resources so need to close handles and release resources
+                proc_handles[i].close()
 
-        if (max_tickers):
-            start_index = end_index
-            if (max_tickers > cores_to_use):
-                end_index += cores_to_use
-            else:
-                end_index += max_tickers
+            if (max_tickers):
+                start_index = end_index
+                if (max_tickers > cores_to_use):
+                    end_index += cores_to_use
+                else:
+                    end_index += max_tickers
 
 
-    #Instantiate GUTILS class
-    gutils = gut.GUTILS()
+        #Instantiate GUTILS class
+        gutils = gut.GUTILS()
 
-    #Aggregate scores and generate a gscores summary
-    gutils.aggregate_scores(symbols_list)
+        #Aggregate scores and generate a gscores summary
+        gutils.aggregate_scores(symbols_list, sf_name.split('.')[0])
+    except:
+        print('ERROR: Analysis and Scoring failed')
 
     print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
+def main():
+    """
+    Main function to analyze and compute score for each stock in the provided watchlist. For each stock, it processes the data collected by scraper app, computes the score and saves score and useful signals in tickers/<ticker_symbol>. List of all gScores is in tickers/<watchlist_name>_overall_gscores.csv
+    """
+
+    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
+    try:
+        #Get the watchlist file from pgm argument
+        sf_name = sys.argv[1]
+
+        run_analyzer_and_scorer(sf_name, None)
+    except:
+        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
+
+
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_backtesting.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_backtesting.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,104 +16,112 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 import time
 import multiprocessing as mp
+import queue
 
 try:
     from gammath_spot import gammath_backtesting as gbt
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_backtesting as gbt
     import gammath_utils as gut
 
 import pandas as pd
 import sys
 
-def main():
-    """
-    Main function to do backtesting on provided watchlist. For each stock, it processes (based on a strategy you implement/use) the data collected by scraper app and processes the stock history based gScore/micro-gScores for approximately last 5 years that from the gscore historian and saves the backtesting stats in respective in tickers/<ticker_symbol>/<ticker_symbol>_bt_stats.csv
-    """
-
-    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
-    try:
-        #Get the watchlist file from pgm argument
-        sf_name = sys.argv[1]
-    except:
-        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
-        raise ValueError('Missing watch list')
-
+def run_backtester(sf_name, info_queue):
     #Read the watchlist
     try:
         watch_list = pd.read_csv(sf_name)
     except:
-        print('ERROR: Failed to read watchlist. See watchlist.csv for example')
-        raise ValueError('Watchlist file read failed')
+        print('ERROR: Failed to read watchlist. See sample_watchlist.csv for example')
+        return
 
-    #Set the start method for launching parallel processes
-    #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
-    #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
-    mp.set_start_method('spawn')
+    print('\nStart Time: ', time.strftime('%x %X'), '\n')
 
-    #Get the number of usable CPUs
-    cores_to_use = gut.get_usable_cpu_count()
+    try:
+        #Set the start method for launching parallel processes
+        #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
+        #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
+        mp.set_start_method('spawn')
+
+        #Get the number of usable CPUs
+        cores_to_use = gut.get_usable_cpu_count()
+
+        print(f'\n{cores_to_use} usable CPUs\n')
+
+        proc_handles = []
+
+        max_tickers = len(watch_list)
+
+        #Use one process per core so we can run core_to_use number of processes in parallel
+        start_index = 0
+        if (max_tickers > cores_to_use):
+            end_index = cores_to_use
+        else:
+            end_index = max_tickers
+
+        #Instances of GBT class
+        gbt_instances = []
+        symbols_list = []
+
+        while (max_tickers):
+            for i in range(start_index, end_index):
+                sym = watch_list['Symbol'][i].strip()
+                tsymbol = f'{sym}'
+                symbols_list.append(tsymbol)
+
+                gbt_instances.append(gbt.GBT())
+                proc_handles.append(mp.Process(target=gbt_instances[i].run_backtest, args=(f'{sym}',)))
+                proc_handles[i].start()
+
+                max_tickers -= 1
+
+            for i in range(start_index, end_index):
+                proc_handles[i].join()
+
+                #Delete the GBT instance
+                gbt_instance = gbt_instances[i]
+                gbt_instances[i] = 0
+                del gbt_instance
+
+                #Running out of resources so need to close handles and release resources
+                proc_handles[i].close()
+
+            if (max_tickers):
+                start_index = end_index
+                if (max_tickers > cores_to_use):
+                    end_index += cores_to_use
+                else:
+                    end_index += max_tickers
 
-    print(f'\nAttempting to use {cores_to_use} CPUs\n')
-    print('\nStart Time: ', time.strftime('%x %X'), '\n')
+        #Instantiate GUTILS class
+        gutils = gut.GUTILS()
 
-    proc_handles = []
+        #Summarize today's actions
+        gutils.summarize_todays_actions(symbols_list)
+    except:
+        print('ERROR: Backtesting failed')
 
-    max_tickers = len(watch_list)
+    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
-    #Use one process per core so we can run core_to_use number of processes in parallel
-    start_index = 0
-    if (max_tickers > cores_to_use):
-        end_index = cores_to_use
-    else:
-        end_index = max_tickers
-
-    #Instances of GBT class
-    gbt_instances = []
-    symbols_list = []
-
-    while (max_tickers):
-        for i in range(start_index, end_index):
-            sym = watch_list['Symbol'][i].strip()
-            tsymbol = f'{sym}'
-            symbols_list.append(tsymbol)
-
-            gbt_instances.append(gbt.GBT())
-            proc_handles.append(mp.Process(target=gbt_instances[i].run_backtest, args=(f'{sym}',)))
-            proc_handles[i].start()
-
-            max_tickers -= 1
-
-        for i in range(start_index, end_index):
-            proc_handles[i].join()
-
-            #Delete the GBT instance
-            gbt_instance = gbt_instances[i]
-            gbt_instances[i] = 0
-            del gbt_instance
-
-            #Running out of resources so need to close handles and release resources
-            proc_handles[i].close()
-
-        if (max_tickers):
-            start_index = end_index
-            if (max_tickers > cores_to_use):
-                end_index += cores_to_use
-            else:
-                end_index += max_tickers
+def main():
+    """
+    Main function to do backtesting on provided watchlist. For each stock, it processes (based on a strategy you implement/use) the data collected by scraper app and processes the stock history based gScore/micro-gScores for approximately last 5 years that from the gscore historian and saves the backtesting stats in respective in tickers/<ticker_symbol>/<ticker_symbol>_bt_stats.csv
+    """
 
-    #Instantiate GUTILS class
-    gutils = gut.GUTILS()
+    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
+    try:
+        #Get the watchlist file from pgm argument
+        sf_name = sys.argv[1]
+        run_backtester(sf_name, None)
+    except:
+        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
 
-    #Summarize today's actions
-    gutils.summarize_todays_actions(symbols_list)
 
-    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_data_scraper.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_data_scraper.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,108 +16,114 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 import time
 import multiprocessing as mp
+import queue
 try:
     from gammath_spot import gammath_get_stocks_data as ggsd
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_get_stocks_data as ggsd
     import gammath_utils as gut
 
 import sys
 import pandas as pd
 
-def main():
-    """
-    Main function to scrape the web and collect data necessary for analyzing and computing gScores for each stock in the provided watchlist. It saves the collected data in tickers/<ticker_symbol> directory.
-    """
-
-    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
-    try:
-        #Get the watchlist file from pgm argument
-        sf_name = sys.argv[1]
-    except:
-        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
-        raise ValueError('Missing watch list')
+def run_scraper(sf_name, info_queue):
 
     #Read the watchlist
     try:
         watch_list = pd.read_csv(sf_name)
     except:
-        print('ERROR: Failed to read watchlist. See watchlist.csv for example')
-        raise ValueError('Watchlist file read failed')
+        print('ERROR: Failed to read watchlist. See sample_watchlist.csv for example')
+        return
 
-    #Set the start method for launching parallel processes
-    #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
-    #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
-    mp.set_start_method('spawn')
+    print('\nStart Time: ', time.strftime('%x %X'), '\n')
 
-    #Get the number of usable CPUs
-    cores_to_use = gut.get_usable_cpu_count()
+    try:
+        #Instantiate GUTILS class
+        gutils = gut.GUTILS()
 
-    print(f'\nAttempting to use {cores_to_use} CPUs\n')
+        #Fetch and save S&P500 list.
+        gutils.get_sp500_list()
 
-    print('\nStart Time: ', time.strftime('%x %X'), '\n')
+        #Fetch S&P500 closing data.
+        gutils.get_sp500_closing_data()
+
+        #Set the start method for launching parallel processes
+        #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
+        #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
+        mp.set_start_method('spawn')
+
+        #Get the number of usable CPUs
+        cores_to_use = gut.get_usable_cpu_count()
+
+        print(f'\n{cores_to_use} usable CPUs\n')
+
+        proc_handles = []
 
-    proc_handles = []
+        max_tickers = len(watch_list)
 
-    max_tickers = len(watch_list)
+        #Instances of GSD class
+        gsd_instances = []
 
-    #Instantiate GUTILS class
-    gutils = gut.GUTILS()
+        #One process per ticker symbol
+        #Run cores_to_use number of processes in parallel
+        start_index = 0
+        if (max_tickers > cores_to_use):
+            end_index = cores_to_use
+        else:
+            end_index = max_tickers
 
-    #Fetch and save S&P500 list.
-    gutils.get_sp500_list()
-
-    #Fetch S&P500 closing data.
-    gutils.get_sp500_closing_data()
-
-    #Instances of GSD class
-    gsd_instances = []
-
-    #One process per ticker symbol
-    #Run cores_to_use number of processes in parallel
-    start_index = 0
-    if (max_tickers > cores_to_use):
-        end_index = cores_to_use
-    else:
-        end_index = max_tickers
-
-    while (max_tickers):
-        for i in range(start_index, end_index):
-            sym = watch_list['Symbol'][i].strip()
-            gsd_instances.append(ggsd.GSD())
-            proc_handles.append(mp.Process(target=gsd_instances[i].get_stocks_data, args=(f'{sym}',)))
-            proc_handles[i].start()
-
-            max_tickers -= 1
-
-        for i in range(start_index, end_index):
-            proc_handles[i].join()
-
-            #Delete the GSD instance
-            gsd_instance = gsd_instances[i]
-            gsd_instances[i] = 0
-            del gsd_instance
-
-            #Running out of resources so need to close handles and release resources
-            proc_handles[i].close()
-
-        if (max_tickers):
-            start_index = end_index
-            if (max_tickers > cores_to_use):
-                end_index += cores_to_use
-            else:
-                end_index += max_tickers
+        while (max_tickers):
+            for i in range(start_index, end_index):
+                sym = watch_list['Symbol'][i].strip()
+                gsd_instances.append(ggsd.GSD())
+                proc_handles.append(mp.Process(target=gsd_instances[i].get_stocks_data, args=(f'{sym}',)))
+                proc_handles[i].start()
 
-    #Aggregate and save PE data
-    gutils.aggregate_pe_data()
+                max_tickers -= 1
+
+            for i in range(start_index, end_index):
+                proc_handles[i].join()
+
+                #Delete the GSD instance
+                gsd_instance = gsd_instances[i]
+                gsd_instances[i] = 0
+                del gsd_instance
+
+                #Running out of resources so need to close handles and release resources
+                proc_handles[i].close()
+
+            if (max_tickers):
+                start_index = end_index
+                if (max_tickers > cores_to_use):
+                    end_index += cores_to_use
+                else:
+                    end_index += max_tickers
+
+        #Aggregate and save PE data
+        gutils.aggregate_pe_data()
+    except:
+        print('ERROR: Data scraping failed')
 
     print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
+def main():
+    """
+    Main function to scrape the web and collect data necessary for analyzing and computing gScores for each stock in the provided watchlist. It saves the collected data in tickers/<ticker_symbol> directory.
+    """
+
+    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
+    try:
+        #Get the watchlist file from pgm argument
+        sf_name = sys.argv[1]
+        run_scraper(sf_name, None)
+    except:
+        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
+
 
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_gscores_historian.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_gscores_historian.py`

 * *Files 5% similar despite different names*

```diff
@@ -16,95 +16,104 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 import time
 import multiprocessing as mp
+import queue
+
 try:
     from gammath_spot import gammath_gscores_history as gsh
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_gscores_history as gsh
     import gammath_utils as gut
 
 import pandas as pd
 import sys
 
+def run_historian(sf_name, info_queue):
+
+    #Read the watchlist
+    try:
+        watch_list = pd.read_csv(sf_name)
+    except:
+        print('ERROR: Failed to read watchlist. See sample_watchlist.csv for example')
+        return
+
+    print('\nStart Time: ', time.strftime('%x %X'), '\n')
+
+    try:
+        #Set the start method for launching parallel processes
+        #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
+        #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
+        mp.set_start_method('spawn')
+
+        #Get the number of usable CPUs
+        cores_to_use = gut.get_usable_cpu_count()
+
+        print(f'\n{cores_to_use} usable CPUs\n')
+
+        proc_handles = []
+
+        max_tickers = len(watch_list)
+
+        #Use one process per core so we can run core_to_use number of processes in parallel
+        start_index = 0
+        if (max_tickers > cores_to_use):
+            end_index = cores_to_use
+        else:
+            end_index = max_tickers
+
+        #Instances of GSH class
+        gsh_instances = []
+
+        while (max_tickers):
+            for i in range(start_index, end_index):
+                sym = watch_list['Symbol'][i].strip()
+                tsymbol = f'{sym}'
+
+                gsh_instances.append(gsh.GSH())
+                proc_handles.append(mp.Process(target=gsh_instances[i].save_gscores_history, args=(f'{sym}',)))
+                proc_handles[i].start()
+
+                max_tickers -= 1
+
+            for i in range(start_index, end_index):
+                proc_handles[i].join()
+
+                #Delete the GSH instance
+                gsh_instance = gsh_instances[i]
+                gsh_instances[i] = 0
+                del gsh_instance
+
+                #Running out of resources so need to close handles and release resources
+                proc_handles[i].close()
+
+            if (max_tickers):
+                start_index = end_index
+                if (max_tickers > cores_to_use):
+                    end_index += cores_to_use
+                else:
+                    end_index += max_tickers
+    except:
+        print('ERROR: gScores history generation failed')
+
+    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
+
 def main():
     """
     Main function to analyze and compute stock history based gScore/micro-gScores for each stock in the provided watchlist. For each stock, it processes the data collected by scraper app, computes the stock history based gScore/micro-gScores for approximately last 5 years and saves respective gScore/micro-gScores in tickers/<ticker_symbol>/<ticker_symbol>_micro_gscores.csv
     """
 
     #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
     try:
         #Get the watchlist file from pgm argument
         sf_name = sys.argv[1]
+        run_historian(sf_name, None)
     except:
         print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
-        raise ValueError('Missing watch list')
 
-    #Read the watchlist
-    try:
-        watch_list = pd.read_csv(sf_name)
-    except:
-        print('ERROR: Failed to read watchlist. See watchlist.csv for example')
-        raise ValueError('Watchlist file read failed')
-
-    #Set the start method for launching parallel processes
-    #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
-    #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
-    mp.set_start_method('spawn')
-
-    #Get the number of usable CPUs
-    cores_to_use = gut.get_usable_cpu_count()
-
-    print(f'\nAttempting to use {cores_to_use} CPUs\n')
-    print('\nStart Time: ', time.strftime('%x %X'), '\n')
-
-    proc_handles = []
-
-    max_tickers = len(watch_list)
-
-    #Use one process per core so we can run core_to_use number of processes in parallel
-    start_index = 0
-    if (max_tickers > cores_to_use):
-        end_index = cores_to_use
-    else:
-        end_index = max_tickers
-
-    #Instances of GSH class
-    gsh_instances = []
-
-    while (max_tickers):
-        for i in range(start_index, end_index):
-            sym = watch_list['Symbol'][i].strip()
-            tsymbol = f'{sym}'
-
-            gsh_instances.append(gsh.GSH())
-            proc_handles.append(mp.Process(target=gsh_instances[i].save_gscores_history, args=(f'{sym}',)))
-            proc_handles[i].start()
-
-            max_tickers -= 1
-
-        for i in range(start_index, end_index):
-            proc_handles[i].join()
-
-            #Delete the GSH instance
-            gsh_instance = gsh_instances[i]
-            gsh_instances[i] = 0
-            del gsh_instance
-
-            #Running out of resources so need to close handles and release resources
-            proc_handles[i].close()
-
-        if (max_tickers):
-            start_index = end_index
-            if (max_tickers > cores_to_use):
-                end_index += cores_to_use
-            else:
-                end_index += max_tickers
-
-    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_pep.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_pep.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,110 +16,117 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 import time
 import multiprocessing as mp
+import queue
 
 try:
     from gammath_spot import gammath_lpep as glpep
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_lpep as glpep
     import gammath_utils as gut
 
 import pandas as pd
 import sys
 import os
 
-def main():
-    """
-    Main function to compute stock's price estimate and price projection. The estimate and projection charts are saved in tickers/<ticker_symbol>/<ticker_symbol>_pep.png. The price projection values are saved in tickers/<ticker_symbol>/<ticker_symbol>_pp.csv.
-    """
-
-    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
-    try:
-        #Get the watchlist file from pgm argument
-        sf_name = sys.argv[1]
-    except:
-        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
-        raise ValueError('Missing watch list')
+def run_projector(sf_name, info_queue):
 
     #Read the watchlist
     try:
         watch_list = pd.read_csv(sf_name)
     except:
-        print('ERROR: Failed to read watchlist. See watchlist.csv for example')
-        raise ValueError('Watchlist file read failed')
-
-    #Set the start method for launching parallel processes
-    #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
-    #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
-    mp.set_start_method('spawn')
-
-    #Get the number of usable CPUs
-    cores_to_use = gut.get_usable_cpu_count()
-
-    print(f'\nAttempting to use {cores_to_use} CPUs\n')
+        print('ERROR: Failed to read watchlist. See sample_watchlist.csv for example')
+        return
 
     print('\nStart Time: ', time.strftime('%x %X'), '\n')
 
-    proc_handles = []
+    try:
+        #Set the start method for launching parallel processes
+        #Python 3.8 onwards 'spawn' is the default method for MacOS and is supported on Linux and Windows
+        #so using it for portability. Spawn method is much slower compared to 'fork' method. If there are no unsafe changes made to this project then on MacOS and Linux this can be changed to use 'fork'
+        mp.set_start_method('spawn')
+
+        #Get the number of usable CPUs
+        cores_to_use = gut.get_usable_cpu_count()
+
+        print(f'\n{cores_to_use} usable CPUs\n')
+
+        proc_handles = []
+
+        max_tickers = len(watch_list)
+
+        #Use one process per core so we can run core_to_use number of processes in parallel
+        start_index = 0
+        if (max_tickers > cores_to_use):
+            end_index = cores_to_use
+        else:
+            end_index = max_tickers
+
+        #Instances of GPEP class
+        gpep_instances = []
+        symbols_list = []
+
+        while (max_tickers):
+            for i in range(start_index, end_index):
+
+                sym = watch_list['Symbol'][i].strip()
+                tsymbol = f'{sym}'
+                symbols_list.append(tsymbol)
+                gpep_instances.append(glpep.GPEP())
+                proc_handles.append(mp.Process(target=gpep_instances[i].get_moving_price_estimated_projection, args=(f'{sym}',)))
+                proc_handles[i].start()
+
+                max_tickers -= 1
+
+            for i in range(start_index, end_index):
+                proc_handles[i].join()
+
+                #Delete the GPEP instance
+                gpep_instance = gpep_instances[i]
+                gpep_instances[i] = 0
+                del gpep_instance
+
+                #Running out of resources so need to close handles and release resources
+                proc_handles[i].close()
+
+            if (max_tickers):
+                start_index = end_index
+                if (max_tickers > cores_to_use):
+                    end_index += cores_to_use
+                else:
+                    end_index += max_tickers
+
+        #Instantiate GUTILS class
+        gutils = gut.GUTILS()
+
+        #Generate 5Y estimated projection for S&P500
+        gpep = glpep.GPEP()
+        gpep.sp500_pep()
 
-    max_tickers = len(watch_list)
+        #Aggregate a sorted list of moving 5Y estimated projected returns
+        gutils.aggregate_peps(symbols_list)
+    except:
+        print('ERROR: Price estimation and projection failed')
 
-    #Use one process per core so we can run core_to_use number of processes in parallel
-    start_index = 0
-    if (max_tickers > cores_to_use):
-        end_index = cores_to_use
-    else:
-        end_index = max_tickers
-
-    #Instances of GPEP class
-    gpep_instances = []
-    symbols_list = []
-
-    while (max_tickers):
-        for i in range(start_index, end_index):
-
-            sym = watch_list['Symbol'][i].strip()
-            tsymbol = f'{sym}'
-            symbols_list.append(tsymbol)
-            gpep_instances.append(glpep.GPEP())
-            proc_handles.append(mp.Process(target=gpep_instances[i].get_moving_price_estimated_projection, args=(f'{sym}',)))
-            proc_handles[i].start()
-
-            max_tickers -= 1
-
-        for i in range(start_index, end_index):
-            proc_handles[i].join()
-
-            #Delete the GPEP instance
-            gpep_instance = gpep_instances[i]
-            gpep_instances[i] = 0
-            del gpep_instance
-
-            #Running out of resources so need to close handles and release resources
-            proc_handles[i].close()
-
-        if (max_tickers):
-            start_index = end_index
-            if (max_tickers > cores_to_use):
-                end_index += cores_to_use
-            else:
-                end_index += max_tickers
-
-    #Instantiate GUTILS class
-    gutils = gut.GUTILS()
-
-    #Generate 5Y estimated projection for S&P500
-    gpep = glpep.GPEP()
-    gpep.sp500_pep()
+    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
-    #Aggregate a sorted list of moving 5Y estimated projected returns
-    gutils.aggregate_peps(symbols_list)
+def main():
+    """
+    Main function to compute stock's price estimate and price projection. The estimate and projection charts are saved in tickers/<ticker_symbol>/<ticker_symbol>_pep.png. The price projection values are saved in tickers/<ticker_symbol>/<ticker_symbol>_pp.csv.
+    """
+
+    #Avoiding to check number of args as if watchlist is not there then there will be an exception anyway
+    try:
+        #Get the watchlist file from pgm argument
+        sf_name = sys.argv[1]
+        run_projector(sf_name, None)
+    except:
+        print('ERROR: Need watch list file name as one argument to this Program. See sample_watchlist.csv')
 
-    print('\nEnd Time: ', time.strftime('%x %X'), '\n')
 
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_stocks_screener.py` & `gammath_spot-9.5/gammath_spot/gammath_stocks_screener.py`

 * *Files 10% similar despite different names*

```diff
@@ -18,31 +18,24 @@
 __author__ = 'Salyl Bhagwat'
 __copyright__ = 'Copyright (c) 2021-2023, Salyl Bhagwat, Gammath Works'
 
 #Stock screener based on micro-gScores
 import sys
 from pathlib import Path
 import pandas as pd
+import queue
 
 try:
     from gammath_spot import gammath_utils as gut
 except:
     import gammath_utils as gut
 
-def main():
-
-    """
-    Main function to screen stocks for buy criteria based on micro-gScores.
-    The screened list is saved in tickers/screened_watchlist.csv.
-    """
 
+def run_screener(sf_name, info_queue):
     try:
-
-        #Get the screening file for buy-criteria from pgm argument
-        sf_name = sys.argv[1]
         df_gscores_screening = pd.read_csv(sf_name)
 
         #extract values for screening
         #-1 means no filtering
         min_price_micro_gscore = df_gscores_screening.Price[0]
         min_rsi_micro_gscore = df_gscores_screening.RSI[0]
         min_bbands_micro_gscore = df_gscores_screening.BBANDS[0]
@@ -107,15 +100,32 @@
                     df_list['sci_gscore'][count] = df_gscores.SCI_gScore[0]
                     df_list['final_gscore'][count] = df_gscores.gScore[0]
                     count += 1
             except:
                 #No action necessary
                 continue
 
-    #Remove unused rows and sort by final_gscore
-    df_list = df_list.truncate(after=(count-1)).sort_values('final_gscore')
+    if (count):
+        #Remove unused rows and sort by final_gscore
+        df_list = df_list.truncate(after=(count-1)).sort_values('final_gscore')
+
+        #Save screened watchlist without the index field
+        df_list.to_csv(p / 'screened_watchlist.csv', index=False)
+
+def main():
+
+    """
+    Main function to screen stocks for buy criteria based on micro-gScores.
+    The screened list is saved in tickers/screened_watchlist.csv.
+    """
+
+    try:
+        #Get the screening file for buy-criteria from pgm argument
+        sf_name = sys.argv[1]
+        run_screener(sf_name, None)
+    except:
+        print('ERROR: Need screener file name as one argument to this Program. See screener.csv')
+
 
-    #Save screened watchlist
-    df_list.to_csv(p / 'screened_watchlist.csv')
 
 if __name__ == '__main__':
     main()
```

### Comparing `gammath_spot-9.3/gammath_spot/gammath_tc.py` & `gammath_spot-9.5/gammath_spot/gammath_tc.py`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/gammath_spot/gammath_utils.py` & `gammath_spot-9.5/gammath_spot/gammath_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,14 +24,15 @@
 import time
 from datetime import date
 from pathlib import Path
 import pandas as pd
 import re
 import pandas_datareader.data as pdd
 import numpy as np
+from glob import glob
 
 #Number of trading days varies across the globe.
 #Some stock exchanges are closed more than US stocks exchanges.
 #As a result, setting the minimum to 239 to accomodate stock exchanges
 #in multiple geographical areas
 MIN_TRADING_DAYS_PER_YEAR = 239
 MIN_TRADING_DAYS_FOR_5_YEARS = (MIN_TRADING_DAYS_PER_YEAR*5)
@@ -112,14 +113,34 @@
         else:
             prices_sigmoid[j] = 0
         j += 1
 
 
     return (prices_sigmoid)
 
+#Get list for watchlists (name and path) in current working dir
+def get_watchlist_list():
+
+    wl_fp_list = []
+
+    #Get all csv file names with path in current working dir
+    fp_list = glob(os.getcwd() + '/*.csv')
+
+    #Extract watchlists (name and paths)
+    for file in fp_list:
+        #Read the file
+        df = pd.read_csv(file)
+        #Check if it has only Symbol column
+        if ((len(df.columns) == 1) and (df.columns[0] == 'Symbol')):
+            #Name with full path
+            wl_fp_list.append(file)
+
+    return wl_fp_list
+
+
 class GUTILS:
 
     def get_sp500_list(self):
 
         sp500_list_url = f'https://en.wikipedia.org/wiki/List_of_S&P_500_companies'
         path = get_tickers_dir()
 
@@ -150,15 +171,15 @@
             sp500 = pd.read_html(sp500_list_url, header=0)[0]
 
             #Save the history for reference and processing
             sp500.to_csv(path / f'SP500_list.csv')
 
         return
 
-    def aggregate_scores(self, symbols_list):
+    def aggregate_scores(self, symbols_list, wl_name):
 
         #Get the watchlist length
         watchlist_len = len(symbols_list)
 
         #Get the tickers dir path
         p = get_tickers_dir()
 
@@ -188,15 +209,15 @@
                     df_b['Note'][i] = ''
 
                 f.close()
                 i += 1
             except:
                 print('\nERROR: Getting stock signals for ', symbol, ': ', sys.exc_info()[0])
 
-        df_b.sort_values('final_gscore').dropna(how='all').to_csv(p / 'overall_gscores.csv', index=False)
+        df_b.sort_values('final_gscore').dropna(how='all').to_csv(p / f'{wl_name}_overall_gscores.csv', index=False)
 
 
     def aggregate_pe_data(self):
 
         path = get_tickers_dir()
         df = pd.read_csv(path / 'SP500_list.csv')
```

### Comparing `gammath_spot-9.3/gammath_spot.egg-info/PKG-INFO` & `gammath_spot-9.5/gammath_spot.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gammath-spot
-Version: 9.3
+Version: 9.5
 Summary: Stock Price-Opining Tools
 Home-page: https://github.com/salylgw/gammath_spot.git
 Author: Salyl Bhagwat
 Author-email: salylgw@gmail.com
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3.8
@@ -80,15 +80,15 @@
  4. Note: You can replace the value for TZ to match your timezone.
 
 
 # HOWTO run these apps
 1. If you installed this software then run: `gammath_scraper sample_watchlist.csv > log_scraper.txt`. See  [sample_watchlist.csv](https://github.com/salylgw/gammath_spot/blob/main/gammath_spot/sample_watchlist.csv). If not installed but just obtained the source code then go to the directory gammath_spot/gammath_spot where all the source files are and run: `python gammath_stocks_data_scraper.py sample_watchlist.csv > log_scraper.txt`.
 1. Above step will save the scraper log in `log_scraper.txt` and save the scraped, formatted data in `tickers` sub-directory. Running the data scraper is essential to be able to use rest of the tools.
 1. If you installed this software then run: `gammath_scorer sample_watchlist.csv > log_scorer.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_analyzer_and_scorer.py sample_watchlist.csv > log_scorer.txt`.
-1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `overall_gscores.csv` in your favorite spreadsheet program or a text editor. In `overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
+1. Above step will save the scorer log in `log_scorer.txt` and all of the Gammath SPOT's analysis and scoring data in `tickers` and `tickers/<ticker-symbol>` sub-directories. Go to `tickers/` sub-directory and open `<watchlist_name>_overall_gscores.csv` (e.g.: `sample_watchlist_overall_gscores.csv`) in your favorite spreadsheet program or a text editor. In `<watchlist_name>_overall_gscores.csv`, you should see stocks from your watchlist arranged in ascending order of gScores. In this file, you'll also see sh_gscore (stock history based gscore) and sci_gscore (current info based gacore) that make up the overall/final gscore. If you are not interested in backtesting or sub-component score then you can ignore it. There is a lot of useful information stored in `tickers/<ticker-symbol>` dir that can be checked for details. `<ticker-symbol>_signal.txt` shows details of the analysis results and `<ticker-symbol>_charts.pdf` shows the plotted charts. This tool also generates current moving estimated support and resistance lines for the stock and saves `<ticker-symbol>_tc.pdf` in `tickers/<ticker-symbol>` dir.
 1. If you want to generate estimated price projection and have installed this software then run: `gammath_projector sample_watchlist.csv > log_projector.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_pep.py sample_watchlist.csv > log_projector.txt`.
 1. Price projection chart and projections are saved in `tickers/<ticker-symbol>` dir. Chart and projection for S&P500 are saved in `tickers` dir. `<ticker-symbol>_pep.pdf` shows the chart and `<ticker-symbol>_pp.csv` shows the projected values. A sorted list of moving estimated projected 5Y returns are saved in `tickers/MPEP.csv`.
 1. In case you want to generate historical gscores (for correlation, past performance, backtesting etc.) then you can do so by using the gScores historian tool. Please note that this tool takes a long time to run so limit the watchlist for this tool to few selected stocks that you want to zoom into. If you installed this software then run: `gammath_historian sample_watchlist.csv > log_historian.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_gscores_historian.py sample_watchlist.csv > log_historian.txt`.
 1. You can check the `tickers/<ticker-symbol>/<ticker-symbol>_micro_gscores.csv` (for stock history based micro-gScores and corresponding total gScore) and `tickers/<ticker-symbol>/<ticker-symbol>_gscores_charts.pdf` that shows the plotted charts of price, overall stock history based gScore and micro-gScores.
 1. You can do backtesting on provided watchlist. If you installed this software then run: `gammath_backtester sample_watchlist.csv > log_backtester.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_backtesting.py sample_watchlist.csv > log_backtester.txt`. You can update the function locally for implementing your own strategy.
 1. For each stock, it processes (based on a strategy you implement/use) the data collected by scraper app and processes the stock history based gScore/micro-gScores for approximately last 5 years (that were saved from the gscore historian) and saves the backtesting stats in `tickers/<ticker_symbol>/<ticker_symbol>_gtrades_stats.csv`. You can check the backtesting stats to understand if the strategy you use worked historically and then decide whether to use that strategy or not. A sorted list of "Today's Actions" summary associated with default backtested strategy is saved in `tickers/Todays_Actions.csv`.
 1. If you want to screen stocks based on micro-gScores and have installed this software then run: `gammath_screener screener.csv > log_screener.txt`. If not installed but just obtained the source code then go to the directory `gammath_spot/gammath_spot/` where all the source files are and run: `python gammath_stocks_screener.py screener.csv > log_screener.txt`. Note that the filtering criteria (micro-gScores values) is specified in `screener.csv` and the results can be found in `tickers/screened_watchlist.csv`.
```

### Comparing `gammath_spot-9.3/gammath_spot.egg-info/SOURCES.txt` & `gammath_spot-9.5/gammath_spot.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gammath_spot-9.3/setup.py` & `gammath_spot-9.5/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 from setuptools import setup
 
 def readme():
     with open('README.md') as f:
         return f.read()
 
 setup(name='gammath_spot',
-      version='9.3',
+      version='9.5',
       description='Stock Price-Opining Tools',
       long_description=readme(),
       long_description_content_type='text/markdown',
       classifiers=['Development Status :: 4 - Beta', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Programming Language :: Python :: 3.8', 'Topic :: Office/Business :: Financial :: Investment'],
       url='https://github.com/salylgw/gammath_spot.git',
       author='Salyl Bhagwat',
       author_email='salylgw@gmail.com',
```

