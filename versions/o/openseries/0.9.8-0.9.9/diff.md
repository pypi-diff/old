# Comparing `tmp/openseries-0.9.8.tar.gz` & `tmp/openseries-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "openseries-0.9.8.tar", last modified: Thu Feb  2 20:32:22 2023, max compression
+gzip compressed data, was "openseries-0.9.9.tar", last modified: Sun Feb  5 15:53:45 2023, max compression
```

## Comparing `openseries-0.9.8.tar` & `openseries-0.9.9.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:32:22.574371 openseries-0.9.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-02-02 20:30:23.000000 openseries-0.9.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    40569 2023-02-02 20:32:22.574371 openseries-0.9.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    39570 2023-02-02 20:30:23.000000 openseries-0.9.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:32:22.574371 openseries-0.9.8/openseries/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3756 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/datefixer.py
--rw-r--r--   0 runner    (1001) docker     (123)      516 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)   105140 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/frame.py
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/load_plotly.py
--rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/openseries.json
--rw-r--r--   0 runner    (1001) docker     (123)      177 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/plotly_captor_logo.json
--rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/plotly_layouts.json
--rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/risk.py
--rw-r--r--   0 runner    (1001) docker     (123)    72994 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/series.py
--rw-r--r--   0 runner    (1001) docker     (123)    11245 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/sim_price.py
--rw-r--r--   0 runner    (1001) docker     (123)    15953 2023-02-02 20:30:23.000000 openseries-0.9.8/openseries/stoch_processes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 20:32:22.574371 openseries-0.9.8/openseries.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    40569 2023-02-02 20:32:22.000000 openseries-0.9.8/openseries.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      515 2023-02-02 20:32:22.000000 openseries-0.9.8/openseries.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 20:32:22.000000 openseries-0.9.8/openseries.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-02-02 20:32:22.000000 openseries-0.9.8/openseries.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-02-02 20:32:22.000000 openseries-0.9.8/openseries.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-02-02 20:30:23.000000 openseries-0.9.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-02 20:32:22.574371 openseries-0.9.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-02 20:30:23.000000 openseries-0.9.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 15:53:45.206380 openseries-0.9.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-02-05 15:51:49.000000 openseries-0.9.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    40913 2023-02-05 15:53:45.206380 openseries-0.9.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    39914 2023-02-05 15:51:49.000000 openseries-0.9.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 15:53:45.206380 openseries-0.9.9/openseries/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4358 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/datefixer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      516 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)   108209 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/frame.py
+-rw-r--r--   0 runner    (1001) docker     (123)      617 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/load_plotly.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/openseries.json
+-rw-r--r--   0 runner    (1001) docker     (123)      177 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/plotly_captor_logo.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1348 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/plotly_layouts.json
+-rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/risk.py
+-rw-r--r--   0 runner    (1001) docker     (123)    77815 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/series.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11245 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/sim_price.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15953 2023-02-05 15:51:49.000000 openseries-0.9.9/openseries/stoch_processes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-05 15:53:45.206380 openseries-0.9.9/openseries.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    40913 2023-02-05 15:53:45.000000 openseries-0.9.9/openseries.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      515 2023-02-05 15:53:45.000000 openseries-0.9.9/openseries.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-05 15:53:45.000000 openseries-0.9.9/openseries.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-02-05 15:53:45.000000 openseries-0.9.9/openseries.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-02-05 15:53:45.000000 openseries-0.9.9/openseries.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-02-05 15:51:49.000000 openseries-0.9.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-05 15:53:45.206380 openseries-0.9.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-05 15:51:49.000000 openseries-0.9.9/setup.py
```

### Comparing `openseries-0.9.8/LICENSE` & `openseries-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/PKG-INFO` & `openseries-0.9.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: openseries
-Version: 0.9.8
+Version: 0.9.9
 Summary: Package for simple financial time series analysis.
 Author-email: Martin Karrin <martin.karrin@captor.se>
 License: BSD 3-Clause License
 Project-URL: repository, https://github.com/CaptorAB/OpenSeries
 Keywords: python,python3,plotly,pandas,finance,fintech,data-science,timeseries,timeseries-data,timeseries-analysis,investment,investment-analysis,investing
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.10
@@ -192,34 +192,35 @@
 | `rolling_info_ratio`    | `OpenFrame` | Returns a pandas.DataFrame with the rolling [information ratio](https://www.investopedia.com/terms/i/informationratio.asp) between two series.                    |
 | `rolling_beta`          | `OpenFrame` | Returns a pandas.DataFrame with the rolling [Beta](https://www.investopedia.com/terms/b/beta.asp) of an asset relative a market.                                  |
 | `rolling_corr`          | `OpenFrame` | Calculates and adds a series of rolling [correlations](https://www.investopedia.com/terms/c/correlation.asp) between two other series.                            |
 | `ewma_risk`             | `OpenFrame` | Returns a `pandas.DataFrame` with volatility and correlation based on [Exponentially Weighted Moving Average](https://www.investopedia.com/articles/07/ewma.asp). |
 
 #### In this table are the methods that apply to both the [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) and the [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py) class.
 
-| Method                       | Applies to                    | Description                                                                                                                                            |
-|:-----------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
-| `align_index_to_local_cdays` | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
-| `resample`                   | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
-| `value_nan_handle`           | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
-| `return_nan_handle`          | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
-| `to_cumret`                  | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
-| `value_to_ret`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
-| `value_to_diff`              | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
-| `value_to_log`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
-| `value_ret_calendar_period`  | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
-| `plot_series`                | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
-| `plot_bars`                  | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
-| `drawdown_details`           | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
-| `to_drawdown_series`         | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
-| `rolling_return`             | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
-| `rolling_vol`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
-| `rolling_var_down`           | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
-| `rolling_cvar_down`          | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
-| `calc_range`                 | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
+| Method                             | Applies to                    | Description                                                                                                                                            |
+|:-----------------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
+| `align_index_to_local_cdays`       | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
+| `resample`                         | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
+| `resample_to_business_period_ends` | `OpenTimeSeries`, `OpenFrame` | Resamples the series to month-end dates with monthly, quarterly or annual frequency.                                                                   |
+| `value_nan_handle`                 | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
+| `return_nan_handle`                | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
+| `to_cumret`                        | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
+| `value_to_ret`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
+| `value_to_diff`                    | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
+| `value_to_log`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
+| `value_ret_calendar_period`        | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
+| `plot_series`                      | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
+| `plot_bars`                        | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
+| `drawdown_details`                 | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
+| `to_drawdown_series`               | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
+| `rolling_return`                   | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
+| `rolling_vol`                      | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
+| `rolling_var_down`                 | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
+| `rolling_cvar_down`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
+| `calc_range`                       | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
 
 #### Below are the numeric properties available for individual [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) or on all series in an [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py).
 
 | Attribute               | type                     | Applies to                    | Description                                                                                                                                                                                                             |
 |:------------------------|:-------------------------|:------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | `all_properties`        | `pandas.DataFrame`       | `OpenTimeSeries`, `OpenFrame` | Returns most of the properties in one go.                                                                                                                                                                               |
 | `arithmetic_ret`        | `float`, `pandas.Series` | `OpenTimeSeries`, `OpenFrame` | [Annualized arithmetic mean of returns](https://www.investopedia.com/terms/a/arithmeticmean.asp).                                                                                                                       |
```

### Comparing `openseries-0.9.8/README.md` & `openseries-0.9.9/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -169,34 +169,35 @@
 | `rolling_info_ratio`    | `OpenFrame` | Returns a pandas.DataFrame with the rolling [information ratio](https://www.investopedia.com/terms/i/informationratio.asp) between two series.                    |
 | `rolling_beta`          | `OpenFrame` | Returns a pandas.DataFrame with the rolling [Beta](https://www.investopedia.com/terms/b/beta.asp) of an asset relative a market.                                  |
 | `rolling_corr`          | `OpenFrame` | Calculates and adds a series of rolling [correlations](https://www.investopedia.com/terms/c/correlation.asp) between two other series.                            |
 | `ewma_risk`             | `OpenFrame` | Returns a `pandas.DataFrame` with volatility and correlation based on [Exponentially Weighted Moving Average](https://www.investopedia.com/articles/07/ewma.asp). |
 
 #### In this table are the methods that apply to both the [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) and the [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py) class.
 
-| Method                       | Applies to                    | Description                                                                                                                                            |
-|:-----------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
-| `align_index_to_local_cdays` | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
-| `resample`                   | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
-| `value_nan_handle`           | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
-| `return_nan_handle`          | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
-| `to_cumret`                  | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
-| `value_to_ret`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
-| `value_to_diff`              | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
-| `value_to_log`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
-| `value_ret_calendar_period`  | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
-| `plot_series`                | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
-| `plot_bars`                  | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
-| `drawdown_details`           | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
-| `to_drawdown_series`         | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
-| `rolling_return`             | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
-| `rolling_vol`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
-| `rolling_var_down`           | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
-| `rolling_cvar_down`          | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
-| `calc_range`                 | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
+| Method                             | Applies to                    | Description                                                                                                                                            |
+|:-----------------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
+| `align_index_to_local_cdays`       | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
+| `resample`                         | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
+| `resample_to_business_period_ends` | `OpenTimeSeries`, `OpenFrame` | Resamples the series to month-end dates with monthly, quarterly or annual frequency.                                                                   |
+| `value_nan_handle`                 | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
+| `return_nan_handle`                | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
+| `to_cumret`                        | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
+| `value_to_ret`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
+| `value_to_diff`                    | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
+| `value_to_log`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
+| `value_ret_calendar_period`        | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
+| `plot_series`                      | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
+| `plot_bars`                        | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
+| `drawdown_details`                 | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
+| `to_drawdown_series`               | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
+| `rolling_return`                   | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
+| `rolling_vol`                      | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
+| `rolling_var_down`                 | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
+| `rolling_cvar_down`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
+| `calc_range`                       | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
 
 #### Below are the numeric properties available for individual [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) or on all series in an [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py).
 
 | Attribute               | type                     | Applies to                    | Description                                                                                                                                                                                                             |
 |:------------------------|:-------------------------|:------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | `all_properties`        | `pandas.DataFrame`       | `OpenTimeSeries`, `OpenFrame` | Returns most of the properties in one go.                                                                                                                                                                               |
 | `arithmetic_ret`        | `float`, `pandas.Series` | `OpenTimeSeries`, `OpenFrame` | [Annualized arithmetic mean of returns](https://www.investopedia.com/terms/a/arithmeticmean.asp).                                                                                                                       |
```

### Comparing `openseries-0.9.8/openseries/datefixer.py` & `openseries-0.9.9/openseries/datefixer.py`

 * *Files 22% similar despite different names*

```diff
@@ -63,79 +63,91 @@
         raise Exception(
             f"Unknown date format {str(d)} of type {str(type(d))} encountered"
         )
 
 
 def date_offset_foll(
     raw_date: str | date | datetime | datetime64 | Timestamp,
-    country: str = "SE",
+    calendar: busdaycalendar | None = None,
+    country: str | None = "SE",
     months_offset: int = 12,
     adjust: bool = False,
     following: bool = True,
 ) -> date:
     """Function to offset dates according to a given calendar
 
     Parameters
     ----------
     raw_date: str | date | datetime | datetime64 | Timestamp
         The date to offset from
-    country: str, default: "SE"
-        Numpy busdaycalendar country code
+    calendar: numpy.busdaycalendar | None, default: None
+        Calendar used for date adjustment. If None a calendar object will
+        be set based on the country argument
+    country: str | None, default: None
+        Country code to create a business day calendar
     months_offset: int, default: 12
         Number of months as integer
     adjust: bool, default: False
         Determines if offset should adjust for business days
     following: bool, default: True
         Determines if days should be offset forward (following) or backward
 
     Returns
     -------
     datetime.date
         Off-set date
     """
 
-    calendar = holiday_calendar(country=country)
     raw_date = date_fix(raw_date)
     month_delta = relativedelta(months=months_offset)
 
     if following:
         day_delta = relativedelta(days=1)
     else:
         day_delta = relativedelta(days=-1)
 
     new_date = raw_date + month_delta
 
     if adjust:
+        if calendar is None:
+            calendar = holiday_calendar(country=country)
         while not is_busday(dates=new_date, busdaycal=calendar):
             new_date += day_delta
 
     return new_date
 
 
 def get_previous_business_day_before_today(
-    today: date | None = None, country: str = "SE"
+    today: date | None = None,
+    calendar: busdaycalendar | None = None,
+    country: str = "SE",
 ):
     """Function to bump backwards to find the previous business day before today
 
     Parameters
     ----------
     today: datetime.date, optional
         Manual input of the day from where the previous business day is found
+    calendar: numpy.busdaycalendar | None, default: None
+        Calendar used for date adjustment. If None a calendar object will
+        be set based on the country argument
     country: str, default: "SE"
-        Numpy busdaycalendar country code
-
+        Country code to create a business day calendar
     Returns
     -------
     datetime.date
         The previous Swedish business day
     """
 
     if today is None:
         today = date.today()
 
+    if calendar is None:
+        calendar = holiday_calendar(country=country)
+
     return date_offset_foll(
         today - timedelta(days=1),
-        country=country,
+        calendar=calendar,
         months_offset=0,
         adjust=True,
         following=False,
     )
```

### Comparing `openseries-0.9.8/openseries/exceptions.py` & `openseries-0.9.9/openseries/exceptions.py`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/frame.py` & `openseries-0.9.9/openseries/frame.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from copy import deepcopy
 from datetime import date, timedelta
+from dateutil.relativedelta import relativedelta
 from functools import reduce
 from logging import warning
 from math import ceil
 from numpy import cov, cumprod, log, sqrt, square, zeros
 from os import path
 from pandas import (
     concat,
@@ -214,16 +215,18 @@
         (datetime.date, datetime.date)
             Start and end date of the chosen date range
         """
         earlier, later = None, None
         if months_offset is not None or from_dt is not None or to_dt is not None:
             if months_offset is not None:
                 earlier = date_offset_foll(
-                    self.last_idx,
+                    raw_date=self.last_idx,
                     months_offset=-months_offset,
+                    adjust=False,
+                    following=True,
                 )
                 assert (
                     earlier >= self.first_idx
                 ), "Function calc_range returned earlier date < series start"
                 later = self.last_idx
             else:
                 if from_dt is not None and to_dt is None:
@@ -1893,14 +1896,90 @@
         OpenFrame
             An OpenFrame object
         """
 
         self.tsdf.index = DatetimeIndex(self.tsdf.index)
         self.tsdf = self.tsdf.resample(freq).last()
         self.tsdf.index = [d.date() for d in DatetimeIndex(self.tsdf.index)]
+        for x in self.constituents:
+            x.tsdf.index = DatetimeIndex(x.tsdf.index)
+            x.tsdf = x.tsdf.resample(freq).last()
+            x.tsdf.index = [d.date() for d in DatetimeIndex(x.tsdf.index)]
+
+        return self
+
+    def resample_to_business_period_ends(
+        self: TOpenFrame,
+        freq: Literal["BM", "BQ", "BA"] = "BM",
+        country: str = "SE",
+        convention: Literal["start", "s", "end", "e"] = "end",
+        method: Literal[
+            None, "pad", "ffill", "backfill", "bfill", "nearest"
+        ] = "nearest",
+    ) -> TOpenFrame:
+        """Resamples timeseries frequency to the business calendar
+        month end dates of each period while leaving any stubs
+        in place. Stubs will be aligned to the shortest stub
+
+        Parameters
+        ----------
+        freq: Literal["BM", "BQ", "BA"], default BM
+            The date offset string that sets the resampled frequency
+        country: str | None, default: SE for Sweden
+            Country code to create a business day calendar used for
+            date adjustments
+        convention: Literal["start", "s", "end", "e"], default; end
+            Controls whether to use the start or end of `rule`.
+        method: Literal[None, "pad", "ffill", "backfill", "bfill",
+        "nearest"], default: nearest
+            Controls the method used to align values across columns
+
+        Returns
+        -------
+        OpenFrame
+            An OpenFrame object
+        """
+
+        head = self.tsdf.loc[self.first_indices.max()].copy()
+        head = head.to_frame().T
+        tail = self.tsdf.loc[self.last_indices.min()].copy()
+        tail = tail.to_frame().T
+        self.tsdf.index = DatetimeIndex(self.tsdf.index)
+        self.tsdf = self.tsdf.resample(rule=freq, convention=convention).last()
+        self.tsdf.drop(index=self.tsdf.index[-1], inplace=True)
+        self.tsdf.index = [d.date() for d in DatetimeIndex(self.tsdf.index)]
+
+        if head.index[0] not in self.tsdf.index:
+            self.tsdf = concat([self.tsdf, head])
+
+        if tail.index[0] not in self.tsdf.index:
+            self.tsdf = concat([self.tsdf, tail])
+
+        self.tsdf.sort_index(inplace=True)
+
+        dates = DatetimeIndex(
+            [self.tsdf.index[0]]
+            + [
+                date_offset_foll(
+                    date(d.year, d.month, 1)
+                    + relativedelta(months=1)
+                    - timedelta(days=1),
+                    country=country,
+                    months_offset=0,
+                    adjust=True,
+                    following=False,
+                )
+                for d in self.tsdf.index[1:-1]
+            ]
+            + [self.tsdf.index[-1]]
+        )
+        dates = dates.drop_duplicates()
+        self.tsdf = self.tsdf.reindex([d.date() for d in dates], method=method)
+        for x in self.constituents:
+            x.tsdf = x.tsdf.reindex([d.date() for d in dates], method=method)
         return self
 
     def to_drawdown_series(self: TOpenFrame) -> TOpenFrame:
         """Converts the timeseries into a drawdown series
 
         Returns
         -------
```

### Comparing `openseries-0.9.8/openseries/load_plotly.py` & `openseries-0.9.9/openseries/load_plotly.py`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/openseries.json` & `openseries-0.9.9/openseries/openseries.json`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/plotly_layouts.json` & `openseries-0.9.9/openseries/plotly_layouts.json`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/risk.py` & `openseries-0.9.9/openseries/risk.py`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/series.py` & `openseries-0.9.9/openseries/series.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,17 @@
 from copy import deepcopy
 from datetime import date, datetime, timedelta
+from dateutil.relativedelta import relativedelta
 from json import dump, load
 from jsonschema import Draft7Validator
+from logging import warning
 from math import ceil
 from numpy import array, busdaycalendar, cumprod, insert, log, sqrt, square, zeros
 from os import path
-from pandas import DataFrame, DatetimeIndex, date_range, MultiIndex, Series
+from pandas import concat, DataFrame, DatetimeIndex, date_range, MultiIndex, Series
 from pandas.tseries.offsets import CustomBusinessDay
 from pathlib import Path
 from plotly.graph_objs import Figure, Scatter
 from plotly.offline import plot
 from stdnum import isin as isincode
 from scipy.stats import kurtosis, norm, skew
 from typing import List, Literal, TypedDict, TypeVar
@@ -20,14 +22,50 @@
 from openseries.risk import (
     cvar_down,
     var_down,
     drawdown_series,
     drawdown_details,
 )
 
+
+def strip_duplicates(dates: List[str], values: List[float], warn: bool = True) -> dict:
+    """Function to remove duplicate dates and their values.
+    There is no check done whether the same number of dates
+    and values are given as arguments
+
+    Parameters
+    ----------
+    dates : List[str]
+        Raw dates
+    values : List[float]
+        Raw values
+    warn: bool, default: True
+        Boolean flag indicating if a warning will be made
+        to highlight the duplicate items removed
+
+    Returns
+    -------
+    dict
+        Cleaned dates as dict.keys and values as dict.values
+    """
+    unique_items = {}
+    dupe_log = []
+
+    for dte, valu in zip(dates, values):
+        if dte not in unique_items:
+            unique_items[dte] = valu
+        else:
+            dupe_log.append({dte: valu})
+
+    if warn:
+        warning(f"Duplicate dates and their values removed:\n" f"{dupe_log}")
+
+    return unique_items
+
+
 TOpenTimeSeries = TypeVar("TOpenTimeSeries", bound="OpenTimeSeries")
 
 
 class TimeSerie(TypedDict, total=False):
     """Class to hold the type of input data for the OpenTimeSeries class.
 
     Parameters
@@ -103,29 +141,45 @@
         country: str, default: "SE"
             Country code according to ISO 3166-1 alpha-2
         """
 
         cls.domestic = domestic_ccy
         cls.calendar = holiday_calendar(country=country)
 
-    def __init__(self: TOpenTimeSeries, d: TimeSerie) -> None:
+    def __init__(
+        self: TOpenTimeSeries, d: TimeSerie, remove_duplicates: bool = False
+    ) -> None:
         """Instantiates an object of the class OpenTimeSeries
          The data can have daily frequency, but not more frequent
 
         Parameters
         ----------
         d: TimeSerie
             A subclass of TypedDict with the required and optional parameters
+        remove_duplicates: bool, default: False
+            Determines if duplicate dates and their values will be removed before
+            an object of this class is instantiated
 
         Returns
         -------
         OpenTimeSeries
             Object of the class OpenTimeSeries
         """
 
+        if remove_duplicates:
+            cleaned_items = strip_duplicates(
+                dates=d["dates"], values=d["values"], warn=True
+            )
+            d.update(
+                {
+                    "dates": list(cleaned_items.keys()),
+                    "values": list(cleaned_items.values()),
+                }
+            )
+
         schema_file = path.join(path.dirname(path.abspath(__file__)), "openseries.json")
         with open(file=schema_file, mode="r", encoding="utf-8") as f:
             series_schema = load(f)
 
         Draft7Validator.check_schema(schema=series_schema)
         validator = Draft7Validator(series_schema)
         validator.validate(d)
@@ -166,14 +220,15 @@
     def from_df(
         cls,
         df: DataFrame | Series,
         column_nmbr: int = 0,
         valuetype: str = "Price(Close)",
         baseccy: str = "SEK",
         local_ccy: bool = True,
+        remove_duplicates: bool = False,
     ) -> TOpenTimeSeries:
         """Creates a timeseries from a Pandas DataFrame or Series
 
         Parameters
         ----------
         df: DataFrame | Series
             Pandas DataFrame or Series
@@ -181,14 +236,17 @@
             Using iloc[:, column_nmbr] to pick column
         valuetype : str, default: "Price(Close)"
             Identifies if the series is a series of values or returns
         baseccy : str, default: "SEK"
             The currency of the timeseries
         local_ccy: bool, default: True
             Boolean flag indicating if timeseries is in local currency
+        remove_duplicates: bool, default: False
+            Determines if duplicate dates and their values will be removed before
+            an object of this class is instantiated
 
         Returns
         -------
         OpenTimeSeries
             An OpenTimeSeries object
         """
 
@@ -214,24 +272,25 @@
             local_ccy=local_ccy,
             name=label,
             valuetype=valuetype,
             dates=dates,
             values=values,
         )
 
-        return cls(d=output)
+        return cls(d=output, remove_duplicates=remove_duplicates)
 
     @classmethod
     def from_frame(
         cls,
         frame,
         label: str,
         valuetype: str = "Price(Close)",
         baseccy: str = "SEK",
         local_ccy: bool = True,
+        remove_duplicates: bool = False,
     ) -> TOpenTimeSeries:
         """Creates a timeseries from an openseries.frame.OpenFrame
 
         Parameters
         ----------
         frame: OpenFrame
             openseries.frame.OpenFrame
@@ -239,14 +298,17 @@
             Placeholder for a name of the timeseries
         valuetype : str, default: "Price(Close)"
             Identifies if the series is a series of values or returns
         baseccy : str, default: "SEK"
             The currency of the timeseries
         local_ccy: bool, default: True
             Boolean flag indicating if timeseries is in local currency
+        remove_duplicates: bool, default: False
+            Determines if duplicate dates and their values will be removed before
+            an object of this class is instantiated
 
         Returns
         -------
         OpenTimeSeries
             An OpenTimeSeries object
         """
 
@@ -261,15 +323,15 @@
             local_ccy=local_ccy,
             name=df.name[0],
             valuetype=df.name[1],
             dates=dates,
             values=df.values.tolist(),
         )
 
-        return cls(d=output)
+        return cls(d=output, remove_duplicates=remove_duplicates)
 
     def from_deepcopy(self: TOpenTimeSeries) -> TOpenTimeSeries:
         """Creates a copy of an OpenTimeSeries object
 
         Returns
         -------
         OpenTimeSeries
@@ -285,14 +347,15 @@
         d_range: DatetimeIndex | None = None,
         days: int | None = None,
         end_dt: date | None = None,
         label: str = "Series",
         valuetype: str = "Price(Close)",
         baseccy: str = "SEK",
         local_ccy: bool = True,
+        remove_duplicates: bool = False,
     ) -> TOpenTimeSeries:
         """Creates a timeseries from a series of values accruing with a given fixed rate
 
         Providing a date_range of type Pandas DatetimeIndex takes priority over
         providing a combination of days and an end date.
 
         Parameters
@@ -311,14 +374,17 @@
             Placeholder for a name of the timeseries
         valuetype : str, default: "Price(Close)"
             Identifies if the series is a series of values or returns
         baseccy : str, default: "SEK"
             The currency of the timeseries
         local_ccy: bool, default: True
             Boolean flag indicating if timeseries is in local currency
+        remove_duplicates: bool, default: False
+            Determines if duplicate dates and their values will be removed before
+            an object of this class is instantiated
 
         Returns
         -------
         OpenTimeSeries
             An OpenTimeSeries object
         """
         if d_range is None and all([days, end_dt]):
@@ -339,15 +405,15 @@
             isin="",
             local_ccy=local_ccy,
             valuetype=valuetype,
             dates=d_range,
             values=arr,
         )
 
-        return cls(d=output)
+        return cls(d=output, remove_duplicates=remove_duplicates)
 
     def to_json(
         self: TOpenTimeSeries, filename: str, directory: str | None = None
     ) -> dict:
         """Dumps timeseries data into a json file
 
         The label and tsdf parameters are deleted before the json file is saved
@@ -423,16 +489,18 @@
             Start and end date of the chosen date range
         """
         earlier, later = None, None
         if months_offset is not None or from_dt is not None or to_dt is not None:
             if months_offset is not None:
                 self.setup_class()
                 earlier = date_offset_foll(
-                    self.last_idx,
+                    raw_date=self.last_idx,
                     months_offset=-months_offset,
+                    adjust=False,
+                    following=True,
                 )
                 assert (
                     earlier >= self.first_idx
                 ), "Function calc_range returned earlier date < series start"
                 later = self.last_idx
             else:
                 if from_dt is not None and to_dt is None:
@@ -1785,14 +1853,79 @@
         """
 
         self.tsdf.index = DatetimeIndex(self.tsdf.index)
         self.tsdf = self.tsdf.resample(freq).last()
         self.tsdf.index = [d.date() for d in DatetimeIndex(self.tsdf.index)]
         return self
 
+    def resample_to_business_period_ends(
+        self: TOpenTimeSeries,
+        freq: Literal["BM", "BQ", "BA"] = "BM",
+        convention: Literal["start", "s", "end", "e"] = "end",
+        method: Literal[
+            None, "pad", "ffill", "backfill", "bfill", "nearest"
+        ] = "nearest",
+    ) -> TOpenTimeSeries:
+        """Resamples timeseries frequency to the business calendar
+        month end dates of each period while leaving any stubs
+        in place
+
+        Parameters
+        ----------
+        freq: Literal["BM", "BQ", "BA"], default BM
+            The date offset string that sets the resampled frequency
+        convention: Literal["start", "s", "end", "e"], default; end
+            Controls whether to use the start or end of `rule`.
+        method: Literal[None, "pad", "ffill", "backfill", "bfill",
+        "nearest"], default: nearest
+            Controls the method used to align values across columns
+
+        Returns
+        -------
+        OpenTimeSeries
+            An OpenTimeSeries object
+        """
+
+        head = self.tsdf.iloc[0].copy()
+        head = head.to_frame().T
+        tail = self.tsdf.iloc[-1].copy()
+        tail = tail.to_frame().T
+        self.tsdf.index = DatetimeIndex(self.tsdf.index)
+        self.tsdf = self.tsdf.resample(rule=freq, convention=convention).last()
+        self.tsdf.drop(index=self.tsdf.index[-1], inplace=True)
+        self.tsdf.index = [d.date() for d in DatetimeIndex(self.tsdf.index)]
+
+        if head.index[0] not in self.tsdf.index:
+            self.tsdf = concat([self.tsdf, head])
+
+        if tail.index[0] not in self.tsdf.index:
+            self.tsdf = concat([self.tsdf, tail])
+
+        self.tsdf.sort_index(inplace=True)
+
+        dates = DatetimeIndex(
+            [self.tsdf.index[0]]
+            + [
+                date_offset_foll(
+                    date(d.year, d.month, 1)
+                    + relativedelta(months=1)
+                    - timedelta(days=1),
+                    calendar=self.calendar,
+                    months_offset=0,
+                    adjust=True,
+                    following=False,
+                )
+                for d in self.tsdf.index[1:-1]
+            ]
+            + [self.tsdf.index[-1]]
+        )
+        dates = dates.drop_duplicates()
+        self.tsdf = self.tsdf.reindex([d.date() for d in dates], method=method)
+        return self
+
     def to_drawdown_series(self: TOpenTimeSeries) -> TOpenTimeSeries:
         """Converts the timeseries into a drawdown series
 
         Returns
         -------
         OpenTimeSeries
             An OpenTimeSeries object
```

### Comparing `openseries-0.9.8/openseries/sim_price.py` & `openseries-0.9.9/openseries/sim_price.py`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries/stoch_processes.py` & `openseries-0.9.9/openseries/stoch_processes.py`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/openseries.egg-info/PKG-INFO` & `openseries-0.9.9/openseries.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: openseries
-Version: 0.9.8
+Version: 0.9.9
 Summary: Package for simple financial time series analysis.
 Author-email: Martin Karrin <martin.karrin@captor.se>
 License: BSD 3-Clause License
 Project-URL: repository, https://github.com/CaptorAB/OpenSeries
 Keywords: python,python3,plotly,pandas,finance,fintech,data-science,timeseries,timeseries-data,timeseries-analysis,investment,investment-analysis,investing
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.10
@@ -192,34 +192,35 @@
 | `rolling_info_ratio`    | `OpenFrame` | Returns a pandas.DataFrame with the rolling [information ratio](https://www.investopedia.com/terms/i/informationratio.asp) between two series.                    |
 | `rolling_beta`          | `OpenFrame` | Returns a pandas.DataFrame with the rolling [Beta](https://www.investopedia.com/terms/b/beta.asp) of an asset relative a market.                                  |
 | `rolling_corr`          | `OpenFrame` | Calculates and adds a series of rolling [correlations](https://www.investopedia.com/terms/c/correlation.asp) between two other series.                            |
 | `ewma_risk`             | `OpenFrame` | Returns a `pandas.DataFrame` with volatility and correlation based on [Exponentially Weighted Moving Average](https://www.investopedia.com/articles/07/ewma.asp). |
 
 #### In this table are the methods that apply to both the [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) and the [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py) class.
 
-| Method                       | Applies to                    | Description                                                                                                                                            |
-|:-----------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
-| `align_index_to_local_cdays` | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
-| `resample`                   | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
-| `value_nan_handle`           | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
-| `return_nan_handle`          | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
-| `to_cumret`                  | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
-| `value_to_ret`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
-| `value_to_diff`              | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
-| `value_to_log`               | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
-| `value_ret_calendar_period`  | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
-| `plot_series`                | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
-| `plot_bars`                  | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
-| `drawdown_details`           | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
-| `to_drawdown_series`         | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
-| `rolling_return`             | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
-| `rolling_vol`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
-| `rolling_var_down`           | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
-| `rolling_cvar_down`          | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
-| `calc_range`                 | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
+| Method                             | Applies to                    | Description                                                                                                                                            |
+|:-----------------------------------|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
+| `align_index_to_local_cdays`       | `OpenTimeSeries`, `OpenFrame` | Aligns the series dates to a business calendar. Defaults to Sweden.                                                                                    |
+| `resample`                         | `OpenTimeSeries`, `OpenFrame` | Resamples the series to a specific frequency.                                                                                                          |
+| `resample_to_business_period_ends` | `OpenTimeSeries`, `OpenFrame` | Resamples the series to month-end dates with monthly, quarterly or annual frequency.                                                                   |
+| `value_nan_handle`                 | `OpenTimeSeries`, `OpenFrame` | Fills `Nan` in a value series with the preceding non-Nan value.                                                                                        |
+| `return_nan_handle`                | `OpenTimeSeries`, `OpenFrame` | Replaces `Nan` in a return series with a 0.0 `float`.                                                                                                  |
+| `to_cumret`                        | `OpenTimeSeries`, `OpenFrame` | Converts a return series into a value series and/or resets a value series to be rebased from 1.0.                                                      |
+| `value_to_ret`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a percentage return series.                                                                                               |
+| `value_to_diff`                    | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a series of differences.                                                                                                  |
+| `value_to_log`                     | `OpenTimeSeries`, `OpenFrame` | Converts a value series into a logarithmic return series.                                                                                              |
+| `value_ret_calendar_period`        | `OpenTimeSeries`, `OpenFrame` | Returns the series simple return for a specific calendar period.                                                                                       |
+| `plot_series`                      | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Scatter](https://plotly.com/python/line-and-scatter/) plot of the series in a browser window.                                     |
+| `plot_bars`                        | `OpenTimeSeries`, `OpenFrame` | Opens a HTML [Plotly Bar](https://plotly.com/python/bar-charts/) plot of the series in a browser window.                                               |
+| `drawdown_details`                 | `OpenTimeSeries`, `OpenFrame` | Returns detailed drawdown characteristics.                                                                                                             |
+| `to_drawdown_series`               | `OpenTimeSeries`, `OpenFrame` | Converts the series into drawdown series.                                                                                                              |
+| `rolling_return`                   | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling returns.                                                                                                       |
+| `rolling_vol`                      | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling volatilities.                                                                                                  |
+| `rolling_var_down`                 | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling VaR figures.                                                                                                   |
+| `rolling_cvar_down`                | `OpenTimeSeries`, `OpenFrame` | Returns a pandas.DataFrame with rolling CVaR figures.                                                                                                  |
+| `calc_range`                       | `OpenTimeSeries`, `OpenFrame` | Returns the start and end dates of a range from specific period definitions. Used by the below numeric methods and not meant to be used independently. |
 
 #### Below are the numeric properties available for individual [OpenTimeSeries](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/series.py) or on all series in an [OpenFrame](https://github.com/CaptorAB/OpenSeries/blob/master/openseries/frame.py).
 
 | Attribute               | type                     | Applies to                    | Description                                                                                                                                                                                                             |
 |:------------------------|:-------------------------|:------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | `all_properties`        | `pandas.DataFrame`       | `OpenTimeSeries`, `OpenFrame` | Returns most of the properties in one go.                                                                                                                                                                               |
 | `arithmetic_ret`        | `float`, `pandas.Series` | `OpenTimeSeries`, `OpenFrame` | [Annualized arithmetic mean of returns](https://www.investopedia.com/terms/a/arithmeticmean.asp).                                                                                                                       |
```

### Comparing `openseries-0.9.8/openseries.egg-info/SOURCES.txt` & `openseries-0.9.9/openseries.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `openseries-0.9.8/pyproject.toml` & `openseries-0.9.9/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 exclude = ["tests*"]
 
 [tool.setuptools.package-data]
 openseries = ["*.json", "*.png"]
 
 [project]
 name = "openseries"
-version = "0.9.8"
+version = "0.9.9"
 description = "Package for simple financial time series analysis."
 readme = "README.md"
 license = { text = "BSD 3-Clause License" }
 authors = [
     { name = "Martin Karrin", email = "martin.karrin@captor.se" }
 ]
 requires-python = ">=3.10"
@@ -61,23 +61,24 @@
     "coverage",
     "pytest",
     "pytest-split"
 ]
 dev = [
     "coverage",
     "pytest",
-    "black==22.12.0",
+    "black==23.1.0",
     "flake8==6.0.0",
     "flake8-black"
 ]
 build = [
+    "build",
     "coverage",
     "pytest",
-    "build",
-    "twine"
+    "twine",
+    "wheel"
 ]
 
 [project.urls]
 repository = "https://github.com/CaptorAB/OpenSeries"
 
 [tool.black]
 line-length = 88
```

