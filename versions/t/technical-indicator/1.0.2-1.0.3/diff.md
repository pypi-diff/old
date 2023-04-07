# Comparing `tmp/technical-indicator-1.0.2.tar.gz` & `tmp/technical-indicator-1.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "technical-indicator-1.0.2.tar", last modified: Mon Apr  3 07:12:07 2023, max compression
+gzip compressed data, was "technical-indicator-1.0.3.tar", last modified: Fri Apr  7 09:41:27 2023, max compression
```

## Comparing `technical-indicator-1.0.2.tar` & `technical-indicator-1.0.3.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.869863 technical-indicator-1.0.2/
--rw-rw-rw-   0        0        0    35149 2022-04-03 23:16:50.000000 technical-indicator-1.0.2/LICENSE
--rw-rw-rw-   0        0        0     5603 2023-04-03 07:12:07.870864 technical-indicator-1.0.2/PKG-INFO
--rw-rw-rw-   0        0        0     4540 2023-04-03 07:09:01.000000 technical-indicator-1.0.2/README.md
--rw-rw-rw-   0        0        0     1281 2023-04-03 07:12:07.871864 technical-indicator-1.0.2/setup.cfg
--rw-rw-rw-   0        0        0     1733 2023-03-31 07:25:18.000000 technical-indicator-1.0.2/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.844863 technical-indicator-1.0.2/src/
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.851862 technical-indicator-1.0.2/src/technical_indicator/
--rw-rw-rw-   0        0        0       97 2023-04-03 07:08:05.000000 technical-indicator-1.0.2/src/technical_indicator/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.862862 technical-indicator-1.0.2/src/technical_indicator/momentum/
--rw-rw-rw-   0        0        0      119 2023-03-31 10:55:35.000000 technical-indicator-1.0.2/src/technical_indicator/momentum/__init__.py
--rw-rw-rw-   0        0        0     5277 2023-04-02 18:47:45.000000 technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_macd.py
--rw-rw-rw-   0        0        0     3724 2023-04-02 18:48:29.000000 technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_macd_histogram.py
--rw-rw-rw-   0        0        0        0 2023-03-30 12:24:23.000000 technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_momentum.py
--rw-rw-rw-   0        0        0     3809 2023-04-02 20:33:17.000000 technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_rsi.py
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.864862 technical-indicator-1.0.2/src/technical_indicator/trend/
--rw-rw-rw-   0        0        0       53 2023-04-01 01:54:30.000000 technical-indicator-1.0.2/src/technical_indicator/trend/__init__.py
--rw-rw-rw-   0        0        0     5498 2023-04-03 07:11:55.000000 technical-indicator-1.0.2/src/technical_indicator/trend/calculate_moving_average.py
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.869863 technical-indicator-1.0.2/src/technical_indicator/volume/
--rw-rw-rw-   0        0        0       58 2023-03-30 13:40:40.000000 technical-indicator-1.0.2/src/technical_indicator/volume/__init__.py
--rw-rw-rw-   0        0        0     1065 2023-03-31 05:47:14.000000 technical-indicator-1.0.2/src/technical_indicator/volume/calculate_on_balance_volume.py
--rw-rw-rw-   0        0        0        0 2023-03-30 12:25:02.000000 technical-indicator-1.0.2/src/technical_indicator/volume/calculate_volume_weighted_average_price.py
-drwxrwxrwx   0        0        0        0 2023-04-03 07:12:07.856860 technical-indicator-1.0.2/src/technical_indicator.egg-info/
--rw-rw-rw-   0        0        0     5603 2023-04-03 07:12:07.000000 technical-indicator-1.0.2/src/technical_indicator.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      847 2023-04-03 07:12:07.000000 technical-indicator-1.0.2/src/technical_indicator.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 07:12:07.000000 technical-indicator-1.0.2/src/technical_indicator.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       28 2023-04-03 07:12:07.000000 technical-indicator-1.0.2/src/technical_indicator.egg-info/requires.txt
--rw-rw-rw-   0        0        0       20 2023-04-03 07:12:07.000000 technical-indicator-1.0.2/src/technical_indicator.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.046009 technical-indicator-1.0.3/
+-rw-rw-rw-   0        0        0    35149 2022-04-03 23:16:50.000000 technical-indicator-1.0.3/LICENSE
+-rw-rw-rw-   0        0        0     7279 2023-04-07 09:41:27.047011 technical-indicator-1.0.3/PKG-INFO
+-rw-rw-rw-   0        0        0     6216 2023-04-07 08:32:26.000000 technical-indicator-1.0.3/README.md
+-rw-rw-rw-   0        0        0     1281 2023-04-07 09:41:27.048009 technical-indicator-1.0.3/setup.cfg
+-rw-rw-rw-   0        0        0     1733 2023-03-31 07:25:18.000000 technical-indicator-1.0.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.015005 technical-indicator-1.0.3/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.022004 technical-indicator-1.0.3/src/technical_indicator/
+-rw-rw-rw-   0        0        0       97 2023-04-07 09:41:18.000000 technical-indicator-1.0.3/src/technical_indicator/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.037007 technical-indicator-1.0.3/src/technical_indicator/momentum/
+-rw-rw-rw-   0        0        0      119 2023-03-31 10:55:35.000000 technical-indicator-1.0.3/src/technical_indicator/momentum/__init__.py
+-rw-rw-rw-   0        0        0     5277 2023-04-02 18:47:45.000000 technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_macd.py
+-rw-rw-rw-   0        0        0     3724 2023-04-02 18:48:29.000000 technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_macd_histogram.py
+-rw-rw-rw-   0        0        0        0 2023-03-30 12:24:23.000000 technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_momentum.py
+-rw-rw-rw-   0        0        0     3809 2023-04-02 20:33:17.000000 technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_rsi.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.039008 technical-indicator-1.0.3/src/technical_indicator/trend/
+-rw-rw-rw-   0        0        0       53 2023-04-01 01:54:30.000000 technical-indicator-1.0.3/src/technical_indicator/trend/__init__.py
+-rw-rw-rw-   0        0        0     9434 2023-04-07 08:22:40.000000 technical-indicator-1.0.3/src/technical_indicator/trend/calculate_moving_average.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.046009 technical-indicator-1.0.3/src/technical_indicator/volume/
+-rw-rw-rw-   0        0        0       58 2023-03-30 13:40:40.000000 technical-indicator-1.0.3/src/technical_indicator/volume/__init__.py
+-rw-rw-rw-   0        0        0     1077 2023-04-07 08:32:26.000000 technical-indicator-1.0.3/src/technical_indicator/volume/calculate_on_balance_volume.py
+-rw-rw-rw-   0        0        0        0 2023-03-30 12:25:02.000000 technical-indicator-1.0.3/src/technical_indicator/volume/calculate_volume_weighted_average_price.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:41:27.030005 technical-indicator-1.0.3/src/technical_indicator.egg-info/
+-rw-rw-rw-   0        0        0     7279 2023-04-07 09:41:26.000000 technical-indicator-1.0.3/src/technical_indicator.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      847 2023-04-07 09:41:26.000000 technical-indicator-1.0.3/src/technical_indicator.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:41:26.000000 technical-indicator-1.0.3/src/technical_indicator.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       28 2023-04-07 09:41:26.000000 technical-indicator-1.0.3/src/technical_indicator.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       20 2023-04-07 09:41:26.000000 technical-indicator-1.0.3/src/technical_indicator.egg-info/top_level.txt
```

### Comparing `technical-indicator-1.0.2/LICENSE` & `technical-indicator-1.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/PKG-INFO` & `technical-indicator-1.0.3/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: technical-indicator
-Version: 1.0.2
+Version: 1.0.3
 Summary: Technical Indicator is a Python package for calculating technical indicators from financial time series datasets
 Home-page: https://github.com/nguyentruonglong/technical-indicator
 Author: Nguyen Truong Long
 Author-email: contact@nguyentruonglong.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/nguyentruonglong/technical-indicator/issues
 Platform: UNKNOWN
@@ -34,101 +34,137 @@
 pip install technical-indicator
 ```
 
 ### Momentum Indicators
 
 #### Relative Strength Index (RSI)
 
-The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of prices and an optional lookback period (default is 14), and call the calculate method:
+The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of close prices and an optional lookback period (default is 14), and call the calculate method:
 
 ```
 from technical_indicator.momentum import RSI
 
 # Example data
 period = 12
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the RSI indicator with the prices and period
-rsi = RSI(prices, period)
+rsi = RSI(close_prices, period)
 
 # Calculate the RSI values
 rsi_values = rsi.calculate_rsi()
 ```
 
 #### Moving Average Convergence Divergence (MACD)
 
-The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
+The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of close prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACD
 
 # Example data
 fast_period = 12
 slow_period = 26
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MACD indicator with the prices and periods
-macd = MACD(prices, fast_period, slow_period)
+macd = MACD(close_prices, fast_period, slow_period)
 
 # Calculate the MACD values
 macd_values = macd.calculate_macd()
 ```
 
 #### MACD Histogram
 
-The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of prices and optional parameters, and call the calculate method:
+The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of close prices and optional parameters, and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACDHistogram
 
 # Example data
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 fast_period = 6
 slow_period = 12
 signal_period = 9
 
 # Initialize the MACD Histogram indicator with the prices and periods
-macd_histogram = MACDHistogram(prices, fast_period, slow_period, signal_period)
+macd_histogram = MACDHistogram(close_prices, fast_period, slow_period, signal_period)
 
 # Calculate the MACD Histogram values
 macd_histogram_values = macd_histogram.calculate_macd_histogram()
 ```
 
 ### Trend Indicators
 
 #### Simple Moving Average (SMA)
 
-The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the SMA values
 sma_values = ma.calculate_sma()
 ```
 
 #### Exponential Moving Average (EMA)
 
-The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the EMA values
 ema_values = ma.calculate_ema()
 ```
 
+#### Weighted Moving Average (WMA)
+
+The Weighted Moving Average (WMA) is a type of moving average that gives more weight to recent prices while allowing the user to specify the exact weighting of each price in the calculation. To calculate the WMA using this package, initialize an instance of the MovingAverage class with an array of close prices and call the calculate_wma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the WMA value
+wma_value = ma.calculate_wma()
+```
+
+#### Hull Moving Average (HMA)
+
+The Hull Moving Average (HMA) is a type of moving average that aims to reduce the lag and noise of traditional moving averages while maintaining smoothness. To calculate the HMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate_hma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the HMA values
+hma_values = ma.calculate_hma()
+```
+
```

### Comparing `technical-indicator-1.0.2/README.md` & `technical-indicator-1.0.3/README.md`

 * *Files 18% similar despite different names*

```diff
@@ -10,99 +10,135 @@
 pip install technical-indicator
 ```
 
 ### Momentum Indicators
 
 #### Relative Strength Index (RSI)
 
-The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of prices and an optional lookback period (default is 14), and call the calculate method:
+The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of close prices and an optional lookback period (default is 14), and call the calculate method:
 
 ```
 from technical_indicator.momentum import RSI
 
 # Example data
 period = 12
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the RSI indicator with the prices and period
-rsi = RSI(prices, period)
+rsi = RSI(close_prices, period)
 
 # Calculate the RSI values
 rsi_values = rsi.calculate_rsi()
 ```
 
 #### Moving Average Convergence Divergence (MACD)
 
-The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
+The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of close prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACD
 
 # Example data
 fast_period = 12
 slow_period = 26
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MACD indicator with the prices and periods
-macd = MACD(prices, fast_period, slow_period)
+macd = MACD(close_prices, fast_period, slow_period)
 
 # Calculate the MACD values
 macd_values = macd.calculate_macd()
 ```
 
 #### MACD Histogram
 
-The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of prices and optional parameters, and call the calculate method:
+The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of close prices and optional parameters, and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACDHistogram
 
 # Example data
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 fast_period = 6
 slow_period = 12
 signal_period = 9
 
 # Initialize the MACD Histogram indicator with the prices and periods
-macd_histogram = MACDHistogram(prices, fast_period, slow_period, signal_period)
+macd_histogram = MACDHistogram(close_prices, fast_period, slow_period, signal_period)
 
 # Calculate the MACD Histogram values
 macd_histogram_values = macd_histogram.calculate_macd_histogram()
 ```
 
 ### Trend Indicators
 
 #### Simple Moving Average (SMA)
 
-The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the SMA values
 sma_values = ma.calculate_sma()
 ```
 
 #### Exponential Moving Average (EMA)
 
-The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the EMA values
 ema_values = ma.calculate_ema()
 ```
+
+#### Weighted Moving Average (WMA)
+
+The Weighted Moving Average (WMA) is a type of moving average that gives more weight to recent prices while allowing the user to specify the exact weighting of each price in the calculation. To calculate the WMA using this package, initialize an instance of the MovingAverage class with an array of close prices and call the calculate_wma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the WMA value
+wma_value = ma.calculate_wma()
+```
+
+#### Hull Moving Average (HMA)
+
+The Hull Moving Average (HMA) is a type of moving average that aims to reduce the lag and noise of traditional moving averages while maintaining smoothness. To calculate the HMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate_hma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the HMA values
+hma_values = ma.calculate_hma()
+```
```

### Comparing `technical-indicator-1.0.2/setup.cfg` & `technical-indicator-1.0.3/setup.cfg`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/setup.py` & `technical-indicator-1.0.3/setup.py`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_macd.py` & `technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_macd.py`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_macd_histogram.py` & `technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_macd_histogram.py`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/src/technical_indicator/momentum/calculate_rsi.py` & `technical-indicator-1.0.3/src/technical_indicator/momentum/calculate_rsi.py`

 * *Files identical despite different names*

### Comparing `technical-indicator-1.0.2/src/technical_indicator/volume/calculate_on_balance_volume.py` & `technical-indicator-1.0.3/src/technical_indicator/volume/calculate_on_balance_volume.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,24 +4,24 @@
 class OnBalanceVolume:
 
     def __init__(self, prices=[], volumes=[]):
         """
         Initializes an instance of the On Balance Volume (OBV) class.
 
         Args:
-            prices (np.ndarray): Array of prices.
+            prices (np.ndarray): array of close prices.
             volumes (np.ndarray): Array of volumes.
         """
         self.prices = np.asarray(prices)
         self.volumes = np.asarray(volumes)
         self.obv = np.zeros_like(prices)
 
     def calculate(self):
         """
-        Calculates the OBV indicator for the initialized array of prices and volumes.
+        Calculates the OBV indicator for the initialized array of close prices and volumes.
 
         Returns:
             np.ndarray: Array of OBV values.
         """
         prev_obv = 0
         for i in range(1, len(self.prices)):
             if self.prices[i] > self.prices[i - 1]:
```

### Comparing `technical-indicator-1.0.2/src/technical_indicator.egg-info/PKG-INFO` & `technical-indicator-1.0.3/src/technical_indicator.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: technical-indicator
-Version: 1.0.2
+Version: 1.0.3
 Summary: Technical Indicator is a Python package for calculating technical indicators from financial time series datasets
 Home-page: https://github.com/nguyentruonglong/technical-indicator
 Author: Nguyen Truong Long
 Author-email: contact@nguyentruonglong.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/nguyentruonglong/technical-indicator/issues
 Platform: UNKNOWN
@@ -34,101 +34,137 @@
 pip install technical-indicator
 ```
 
 ### Momentum Indicators
 
 #### Relative Strength Index (RSI)
 
-The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of prices and an optional lookback period (default is 14), and call the calculate method:
+The RSI measures the ratio of upward price movements to downward price movements over a given period of time. To calculate the RSI using this package, initialize an instance of the RSI class with an array of close prices and an optional lookback period (default is 14), and call the calculate method:
 
 ```
 from technical_indicator.momentum import RSI
 
 # Example data
 period = 12
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the RSI indicator with the prices and period
-rsi = RSI(prices, period)
+rsi = RSI(close_prices, period)
 
 # Calculate the RSI values
 rsi_values = rsi.calculate_rsi()
 ```
 
 #### Moving Average Convergence Divergence (MACD)
 
-The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
+The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. To calculate the MACD using this package, initialize an instance of the MACD class with an array of close prices and optional fast and slow lookback periods (default are 12 and 26, respectively), and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACD
 
 # Example data
 fast_period = 12
 slow_period = 26
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MACD indicator with the prices and periods
-macd = MACD(prices, fast_period, slow_period)
+macd = MACD(close_prices, fast_period, slow_period)
 
 # Calculate the MACD values
 macd_values = macd.calculate_macd()
 ```
 
 #### MACD Histogram
 
-The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of prices and optional parameters, and call the calculate method:
+The MACD (Moving Average Convergence Divergence) Histogram is a momentum indicator that shows the difference between the MACD line and the signal line. It is derived from the MACD line and is used to identify potential trend reversals. To calculate the MACD Histogram using this package, import the MACDHistogram class from the momentum module, initialize an instance with an array of close prices and optional parameters, and call the calculate method:
 
 ```
 from technical_indicator.momentum import MACDHistogram
 
 # Example data
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 fast_period = 6
 slow_period = 12
 signal_period = 9
 
 # Initialize the MACD Histogram indicator with the prices and periods
-macd_histogram = MACDHistogram(prices, fast_period, slow_period, signal_period)
+macd_histogram = MACDHistogram(close_prices, fast_period, slow_period, signal_period)
 
 # Calculate the MACD Histogram values
 macd_histogram_values = macd_histogram.calculate_macd_histogram()
 ```
 
 ### Trend Indicators
 
 #### Simple Moving Average (SMA)
 
-The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Simple Moving Average (SMA) is a widely used technical indicator that represents the average closing price of a security over a specified period of time. To calculate the SMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the SMA values
 sma_values = ma.calculate_sma()
 ```
 
 #### Exponential Moving Average (EMA)
 
-The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of prices and an optional lookback period (default is 9), and call the calculate method:
+The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent prices. To calculate the EMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate method:
 
 ```
 from technical_indicator.trend import MovingAverage
 
 # Example data
 period = 20
-prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17, 18, 14, 20, 18]
 
 # Initialize the MovingAverage instance with the prices and period
-ma = MovingAverage(prices, period)
+ma = MovingAverage(close_prices, period)
 
 # Calculate the EMA values
 ema_values = ma.calculate_ema()
 ```
 
+#### Weighted Moving Average (WMA)
+
+The Weighted Moving Average (WMA) is a type of moving average that gives more weight to recent prices while allowing the user to specify the exact weighting of each price in the calculation. To calculate the WMA using this package, initialize an instance of the MovingAverage class with an array of close prices and call the calculate_wma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the WMA value
+wma_value = ma.calculate_wma()
+```
+
+#### Hull Moving Average (HMA)
+
+The Hull Moving Average (HMA) is a type of moving average that aims to reduce the lag and noise of traditional moving averages while maintaining smoothness. To calculate the HMA using this package, initialize an instance of the MovingAverage class with an array of close prices and an optional lookback period (default is 9), and call the calculate_hma method:
+
+```
+from technical_indicator.trend import MovingAverage
+
+# Example data
+period = 20
+close_prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 17, 16, 18, 20, 18, 16, 17, 15, 17, 19, 20, 16, 17 , 18, 14, 20, 18]
+
+# Initialize the MovingAverage instance with the prices and period
+ma = MovingAverage(close_prices, period)
+
+# Calculate the HMA values
+hma_values = ma.calculate_hma()
+```
+
```

### Comparing `technical-indicator-1.0.2/src/technical_indicator.egg-info/SOURCES.txt` & `technical-indicator-1.0.3/src/technical_indicator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

