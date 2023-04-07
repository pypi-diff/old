# Comparing `tmp/easy_kline-0.1.0.tar.gz` & `tmp/easy_kline-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "easy_kline-0.1.0.tar", last modified: Thu Apr  6 20:18:38 2023, max compression
+gzip compressed data, was "easy_kline-0.1.1.tar", last modified: Fri Apr  7 07:42:24 2023, max compression
```

## Comparing `easy_kline-0.1.0.tar` & `easy_kline-0.1.1.tar`

### file list

```diff
@@ -1,32 +1,31 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 20:18:38.967581 easy_kline-0.1.0/
--rw-rw-rw-   0        0        0     1079 2023-03-24 09:05:48.000000 easy_kline-0.1.0/LICENSE.txt
--rw-rw-rw-   0        0        0    10158 2023-04-06 20:18:38.967943 easy_kline-0.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     9518 2023-04-06 20:00:06.000000 easy_kline-0.1.0/README.md
--rw-rw-rw-   0        0        0      108 2023-03-24 09:00:12.000000 easy_kline-0.1.0/pyproject.toml
--rw-rw-rw-   0        0        0      847 2023-04-06 20:18:38.967943 easy_kline-0.1.0/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-06 20:18:38.952844 easy_kline-0.1.0/src/
-drwxrwxrwx   0        0        0        0 2023-04-06 20:18:38.964082 easy_kline-0.1.0/src/easy_kline/
--rw-rw-rw-   0        0        0      218 2023-04-01 12:29:09.000000 easy_kline-0.1.0/src/easy_kline/__init__.py
--rw-rw-rw-   0        0        0     1331 2023-04-04 09:46:24.000000 easy_kline-0.1.0/src/easy_kline/binance.py
--rw-rw-rw-   0        0        0     1664 2023-04-04 09:57:13.000000 easy_kline-0.1.0/src/easy_kline/bybit.py
--rw-rw-rw-   0        0        0     1514 2023-03-25 16:50:33.000000 easy_kline-0.1.0/src/easy_kline/bybit_futures.py
--rw-rw-rw-   0        0        0     1359 2023-04-01 23:26:47.000000 easy_kline-0.1.0/src/easy_kline/check_while_loop.py
--rw-rw-rw-   0        0        0      413 2023-03-24 19:53:14.000000 easy_kline-0.1.0/src/easy_kline/datetime_to_timestamp.py
--rw-rw-rw-   0        0        0     2159 2023-04-04 22:08:47.000000 easy_kline-0.1.0/src/easy_kline/errors.py
--rw-rw-rw-   0        0        0    16799 2023-04-06 19:36:22.000000 easy_kline-0.1.0/src/easy_kline/exchange.py
--rw-rw-rw-   0        0        0     8514 2023-04-06 18:03:30.000000 easy_kline-0.1.0/src/easy_kline/get_bar.py
--rw-rw-rw-   0        0        0      673 2023-04-06 17:47:17.000000 easy_kline-0.1.0/src/easy_kline/loading_animation.py
--rw-rw-rw-   0        0        0     1620 2023-04-06 16:59:35.000000 easy_kline-0.1.0/src/easy_kline/oanda.py
--rw-rw-rw-   0        0        0     1578 2023-03-25 22:07:12.000000 easy_kline-0.1.0/src/easy_kline/response_to_json.py
--rw-rw-rw-   0        0        0     4437 2023-04-06 19:56:23.000000 easy_kline-0.1.0/src/easy_kline/stream.py
--rw-rw-rw-   0        0        0        0 2023-04-01 23:55:14.000000 easy_kline-0.1.0/src/easy_kline/test.py
--rw-rw-rw-   0        0        0      549 2023-04-04 22:11:45.000000 easy_kline-0.1.0/src/easy_kline/timeframe_check.py
--rw-rw-rw-   0        0        0      431 2023-03-24 19:19:46.000000 easy_kline-0.1.0/src/easy_kline/timeframe_converter.py
-drwxrwxrwx   0        0        0        0 2023-04-06 20:18:38.966079 easy_kline-0.1.0/src/easy_kline.egg-info/
--rw-rw-rw-   0        0        0    10158 2023-04-06 20:18:38.000000 easy_kline-0.1.0/src/easy_kline.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      726 2023-04-06 20:18:38.000000 easy_kline-0.1.0/src/easy_kline.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 20:18:38.000000 easy_kline-0.1.0/src/easy_kline.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       41 2023-04-06 20:18:38.000000 easy_kline-0.1.0/src/easy_kline.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-06 20:18:38.000000 easy_kline-0.1.0/src/easy_kline.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-06 20:18:38.966079 easy_kline-0.1.0/tests/
--rw-rw-rw-   0        0        0      358 2023-04-06 18:03:54.000000 easy_kline-0.1.0/tests/test.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:42:24.982263 easy_kline-0.1.1/
+-rw-rw-rw-   0        0        0     1079 2023-03-24 09:05:48.000000 easy_kline-0.1.1/LICENSE.txt
+-rw-rw-rw-   0        0        0    10158 2023-04-07 07:42:24.982534 easy_kline-0.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     9518 2023-04-06 20:00:06.000000 easy_kline-0.1.1/README.md
+-rw-rw-rw-   0        0        0      108 2023-03-24 09:00:12.000000 easy_kline-0.1.1/pyproject.toml
+-rw-rw-rw-   0        0        0      847 2023-04-07 07:42:24.982534 easy_kline-0.1.1/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 07:42:24.953245 easy_kline-0.1.1/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 07:42:24.979715 easy_kline-0.1.1/src/easy_kline/
+-rw-rw-rw-   0        0        0      218 2023-04-01 12:29:09.000000 easy_kline-0.1.1/src/easy_kline/__init__.py
+-rw-rw-rw-   0        0        0     1331 2023-04-04 09:46:24.000000 easy_kline-0.1.1/src/easy_kline/binance.py
+-rw-rw-rw-   0        0        0     1666 2023-04-07 07:31:35.000000 easy_kline-0.1.1/src/easy_kline/bybit.py
+-rw-rw-rw-   0        0        0     1359 2023-04-01 23:26:47.000000 easy_kline-0.1.1/src/easy_kline/check_while_loop.py
+-rw-rw-rw-   0        0        0      413 2023-03-24 19:53:14.000000 easy_kline-0.1.1/src/easy_kline/datetime_to_timestamp.py
+-rw-rw-rw-   0        0        0     2159 2023-04-04 22:08:47.000000 easy_kline-0.1.1/src/easy_kline/errors.py
+-rw-rw-rw-   0        0        0    16799 2023-04-06 19:36:22.000000 easy_kline-0.1.1/src/easy_kline/exchange.py
+-rw-rw-rw-   0        0        0     8238 2023-04-07 07:37:08.000000 easy_kline-0.1.1/src/easy_kline/get_bar.py
+-rw-rw-rw-   0        0        0      674 2023-04-07 07:28:40.000000 easy_kline-0.1.1/src/easy_kline/loading_animation.py
+-rw-rw-rw-   0        0        0     1620 2023-04-06 16:59:35.000000 easy_kline-0.1.1/src/easy_kline/oanda.py
+-rw-rw-rw-   0        0        0     1578 2023-03-25 22:07:12.000000 easy_kline-0.1.1/src/easy_kline/response_to_json.py
+-rw-rw-rw-   0        0        0     4437 2023-04-06 19:56:23.000000 easy_kline-0.1.1/src/easy_kline/stream.py
+-rw-rw-rw-   0        0        0        0 2023-04-01 23:55:14.000000 easy_kline-0.1.1/src/easy_kline/test.py
+-rw-rw-rw-   0        0        0      549 2023-04-04 22:11:45.000000 easy_kline-0.1.1/src/easy_kline/timeframe_check.py
+-rw-rw-rw-   0        0        0      431 2023-03-24 19:19:46.000000 easy_kline-0.1.1/src/easy_kline/timeframe_converter.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:42:24.980710 easy_kline-0.1.1/src/easy_kline.egg-info/
+-rw-rw-rw-   0        0        0    10158 2023-04-07 07:42:24.000000 easy_kline-0.1.1/src/easy_kline.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      694 2023-04-07 07:42:24.000000 easy_kline-0.1.1/src/easy_kline.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 07:42:24.000000 easy_kline-0.1.1/src/easy_kline.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       41 2023-04-07 07:42:24.000000 easy_kline-0.1.1/src/easy_kline.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 07:42:24.000000 easy_kline-0.1.1/src/easy_kline.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 07:42:24.981708 easy_kline-0.1.1/tests/
+-rw-rw-rw-   0        0        0      358 2023-04-06 18:03:54.000000 easy_kline-0.1.1/tests/test.py
```

### Comparing `easy_kline-0.1.0/LICENSE.txt` & `easy_kline-0.1.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/PKG-INFO` & `easy_kline-0.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: easy_kline
-Version: 0.1.0
+Version: 0.1.1
 Summary: "Easy_klines" is a Python library that provides a solution to the limitations of exchange APIs in retrieving candlestick data more efficiently and quickly.
 Home-page: https://github.com/mohder79/Easy_klines
 Author: mohder
 Author-email: mohder1379@gmail.com
 Project-URL: Bug Tracker, https://github.com/mohder79/Easy_klines
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `easy_kline-0.1.0/README.md` & `easy_kline-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/setup.cfg` & `easy_kline-0.1.1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2065 6173 795f 6b6c 696e 650d 0a76   = easy_kline..v
-00000020: 6572 7369 6f6e 203d 2030 2e31 2e30 0d0a  ersion = 0.1.0..
+00000020: 6572 7369 6f6e 203d 2030 2e31 2e31 0d0a  ersion = 0.1.1..
 00000030: 6175 7468 6f72 203d 206d 6f68 6465 720d  author = mohder.
 00000040: 0a61 7574 686f 725f 656d 6169 6c20 3d20  .author_email = 
 00000050: 6d6f 6864 6572 3133 3739 4067 6d61 696c  mohder1379@gmail
 00000060: 2e63 6f6d 0d0a 6465 7363 7269 7074 696f  .com..descriptio
 00000070: 6e20 3d20 2245 6173 795f 6b6c 696e 6573  n = "Easy_klines
 00000080: 2220 6973 2061 2050 7974 686f 6e20 6c69  " is a Python li
 00000090: 6272 6172 7920 7468 6174 2070 726f 7669  brary that provi
```

### Comparing `easy_kline-0.1.0/src/easy_kline/binance.py` & `easy_kline-0.1.1/src/easy_kline/binance.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/bybit.py` & `easy_kline-0.1.1/src/easy_kline/bybit.py`

 * *Files 0% similar despite different names*

```diff
@@ -18,14 +18,15 @@
         self.timeframe = time_frame
         self.start_time = start_time
         
         self.retry_count = retry_count
 
         if futures:
             self.futures = 'linear'
+
         else :
             self.futures = 'spot'
 
     # "The Bybit exchange has a different timeframe input compared to the input of my main program."
     def bybit_timeframe(self):
         timeframe = self.timeframe
         bybit_timeframe = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
```

### Comparing `easy_kline-0.1.0/src/easy_kline/bybit_futures.py` & `easy_kline-0.1.1/src/easy_kline/oanda.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,35 +1,36 @@
-
 '''
-This class retrieve data from the bybit API. The class constructor takes four arguments: symbol, time_frame, start_time, and retry_count
-The class has two methods: "bybit_timeframe" and "bybit_data".
-The "bybit_timeframe" method maps the time frame string to the corresponding string used by the bybit API. 
-The "bybit_data" method sends a request to the bybit API using the provided arguments to retrieve candlestick data for the specified symbol and time frame.
+This class retrieve data from the Oanda API. The class constructor takes four arguments: symbol, time_frame, start_time, and retry_count
+The class has two methods: "oanda_timeframe" and "oanda_data".
+The "oanda_timeframe" method maps the time frame string to the corresponding string used by the Oanda API. 
+The "oanda_data" method sends a request to the Oanda API using the provided arguments to retrieve candlestick data for the specified symbol and time frame.
+
 '''
+
 import requests
-import pandas as pd
 from .datetime_to_timestamp import date_time_to_timestamp
 
 
-class Bybit_F():
-
+class Oanda():
     def __init__(self,  symbol, time_frame, start_time, retry_count: int = 5):
 
         self.symbol = symbol
         self.timeframe = time_frame
         self.start_time = start_time
         self.retry_count = retry_count
 
-    # "The Bybit exchange has a different timeframe input compared to the input of my main program."
-    def bybit_timeframe(self):
+    def oanda_timeframe(self):
         timeframe = self.timeframe
-        bybit_timeframe = {'1m': 1, '3m': 3, '5m': 5, '15m': 15, '30': 30, '1h': 60,
-                           '2h': 120, '4h': 240, '6h': 360, '8h': 480, '12h': 720, '1d': 'D', '1w': 'W'}
+        bybit_timeframe = {'1m': 'M1', '3m': 'M3', '5m': 'M5', '15m': 'M15', '30': 'M30', '1h': 'H1',
+                           '2h': 'H2', '4h': 'H4', '6h': 'H6', '8h': 'H8', '12h': 'H12', '1d': 'D', '1w': 'W'}
         return bybit_timeframe.get(timeframe)
 
-    def bybit_f_data(self):
-
-        url = f'https://api.bybit.com/v5/market/kline?category=linear&symbol={self.symbol}&interval={self.bybit_timeframe()}&start={date_time_to_timestamp(self.start_time)}'
+    def oanda_data(self):
+        API_KEY = '393dc3deec6d2a0f20e328ee40e86595-b3810e7fcb6fafbab913519db3f51b2b'
+        HEADERS = {
+            'Authorization': 'Bearer ' + API_KEY
+        }
 
-        response = requests.get(url)
+        url = f"https://api-fxpractice.oanda.com/v3/instruments/{self.symbol}/candles?price=M&granularity={self.oanda_timeframe()}&from={int(date_time_to_timestamp(self.start_time)/1000)}&count=5000"
+        response = requests.get(url, headers=HEADERS)
 
         return response
```

### Comparing `easy_kline-0.1.0/src/easy_kline/check_while_loop.py` & `easy_kline-0.1.1/src/easy_kline/check_while_loop.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/errors.py` & `easy_kline-0.1.1/src/easy_kline/errors.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/exchange.py` & `easy_kline-0.1.1/src/easy_kline/exchange.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/get_bar.py` & `easy_kline-0.1.1/src/easy_kline/get_bar.py`

 * *Files 8% similar despite different names*

```diff
@@ -81,52 +81,58 @@
         errors(exchange_name, response_data)
         bars = response_to_json(
             exchange_name, response_data)
 
         while True:
             
 
-            last_time = bars['Time'].iloc[-1] # get last time in dataframe
-            time_now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M') # get utc time now
-            timeframe = timeframe_converter(self.timeframe) # return timeframe to minutes
-            time_format = "%Y-%m-%d %H:%M" 
-            difference_in_minutes = (datetime.datetime.strptime(time_now, time_format) - datetime.datetime.strptime(
-                str(last_time), str(time_format))).total_seconds() // 60 # utc time now minus last time in dataframe
-            if difference_in_minutes <= timeframe:  # check if difference_in_minutes < timeframe . its meens we dont have any data and last time in data frame = now time in utc
+            last_time = bars['Time'].iloc[-1]
+            time_now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
+            time = timeframe_converter(self.timeframe)
+            time_format = "%Y-%m-%d %H:%M"
+            time1 = datetime.datetime.strptime(time_now, time_format)
+            time2 = datetime.datetime.strptime(
+                str(last_time), str(time_format))
+
+            difference_in_minutes = (time1 - time2).total_seconds() // 60
+            if difference_in_minutes <= time:
                 break
-            else:  # get new data 
-                 
-                last_bar_datetime = datetime.datetime.strptime( last_time, '%Y-%m-%d %H:%M')# last time in dataframe
+            else:
+
+                last_bar_datetime = datetime.datetime.strptime(
+                    last_time, '%Y-%m-%d %H:%M')
                 new_time = (
-                    last_bar_datetime + timedelta(minutes=timeframe)).strftime('%Y-%m-%d %H:%M')   # (last time in list + timeframe ) for get new bars
+                    last_bar_datetime + timedelta(minutes=time)).strftime('%Y-%m-%d %H:%M')
                 if new_time == self.start_time:
 
                     break
 
-                self.start_time = new_time  # set new start time for get data
+                self.start_time = new_time
 
-                if exchange_name == 'bybit' or 'binance' :
+                if exchange_name  in ['bybit' , 'binance'] :
                     arguments = self.symbol, self.timeframe, self.start_time , self.futures
                 else :
                     arguments = self.symbol, self.timeframe, self.start_time 
                 exchange = exchanges(*arguments)
                 for i in range(self.retry_count):
                     try:
 
                         sys.stdout.write("\033[K")
                         loading_animation(
-                            f'Fetching a new bar of data for {self.symbol} at {self.start_time}', 2)
+                            f'Fetching {self.symbol} new bar for {self.start_time}', 2)
 
                         response_data = exchange.bybit_data() if exchange_name == 'bybit' else exchange.binance_data(
                         ) if exchange_name == 'binance' else exchange.oanda_data() if exchange_name == 'oanda' else None
 
                         if str(response_data) == '(<Response [200]>, 0)' or '<Response [200]>':
                             sys.stdout.write("\033[K")
                             sys.stdout.write('\r')
 
+                            break  # if successful, exit the loop
+
                     except requests.exceptions.RequestException:
                         loading_animation(
                             'Request failed: "Encountered network error"  Retrying in 5 seconds')
                         sys.stdout.write("\033[K")
                         sys.stdout.write('\r')
 
                         if i == self.retry_count - 1:
```

### Comparing `easy_kline-0.1.0/src/easy_kline/loading_animation.py` & `easy_kline-0.1.1/src/easy_kline/loading_animation.py`

 * *Files 14% similar despite different names*

```diff
@@ -11,10 +11,10 @@
     start_time = time.time()  # start time
 
     while time.time() - start_time < time_loading:  # time condition
         for char in chars:
             # Print the current character
             space = ' ' * 15
             sys.stdout.write(
-                f'\r {text}  {char}{space}')
+                f'\r {text}  {char} {space}')
             time.sleep(0.1)  # Wait for a short amount of time
     time.sleep(1)  # Wait for a short amount of time
```

### Comparing `easy_kline-0.1.0/src/easy_kline/response_to_json.py` & `easy_kline-0.1.1/src/easy_kline/response_to_json.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/stream.py` & `easy_kline-0.1.1/src/easy_kline/stream.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline/timeframe_check.py` & `easy_kline-0.1.1/src/easy_kline/timeframe_check.py`

 * *Files identical despite different names*

### Comparing `easy_kline-0.1.0/src/easy_kline.egg-info/PKG-INFO` & `easy_kline-0.1.1/src/easy_kline.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: easy-kline
-Version: 0.1.0
+Version: 0.1.1
 Summary: "Easy_klines" is a Python library that provides a solution to the limitations of exchange APIs in retrieving candlestick data more efficiently and quickly.
 Home-page: https://github.com/mohder79/Easy_klines
 Author: mohder
 Author-email: mohder1379@gmail.com
 Project-URL: Bug Tracker, https://github.com/mohder79/Easy_klines
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `easy_kline-0.1.0/src/easy_kline.egg-info/SOURCES.txt` & `easy_kline-0.1.1/src/easy_kline.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 LICENSE.txt
 README.md
 pyproject.toml
 setup.cfg
 src/easy_kline/__init__.py
 src/easy_kline/binance.py
 src/easy_kline/bybit.py
-src/easy_kline/bybit_futures.py
 src/easy_kline/check_while_loop.py
 src/easy_kline/datetime_to_timestamp.py
 src/easy_kline/errors.py
 src/easy_kline/exchange.py
 src/easy_kline/get_bar.py
 src/easy_kline/loading_animation.py
 src/easy_kline/oanda.py
```

