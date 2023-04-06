# Comparing `tmp/unicorn-binance-websocket-api-1.44.1.tar.gz` & `tmp/unicorn-binance-websocket-api-1.45.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "unicorn-binance-websocket-api-1.44.1.tar", last modified: Tue Apr  4 09:13:00 2023, max compression
+gzip compressed data, was "unicorn-binance-websocket-api-1.45.0.tar", last modified: Thu Apr  6 16:02:54 2023, max compression
```

## Comparing `unicorn-binance-websocket-api-1.44.1.tar` & `unicorn-binance-websocket-api-1.45.0.tar`

### file list

```diff
@@ -1,21 +1,22 @@
-drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-04 09:13:00.403397 unicorn-binance-websocket-api-1.44.1/
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)     1215 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.44.1/LICENSE
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    41501 2023-04-04 09:13:00.397772 unicorn-binance-websocket-api-1.44.1/PKG-INFO
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    39620 2023-04-04 09:07:55.000000 unicorn-binance-websocket-api-1.44.1/README.md
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)       38 2023-04-04 09:13:00.407647 unicorn-binance-websocket-api-1.44.1/setup.cfg
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)     4904 2023-04-04 00:02:14.000000 unicorn-binance-websocket-api-1.44.1/setup.py
-drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-04 09:12:59.936179 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)      498 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/__init__.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    25929 2023-04-03 22:20:23.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/connection.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)     2692 2023-04-03 20:23:35.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/connection_settings.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)     2168 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/exceptions.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)   203218 2023-04-04 09:12:28.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/manager.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    14327 2023-04-04 08:52:30.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/restclient.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)     3673 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/restserver.py
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    16355 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/sockets.py
-drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-04 09:13:00.315401 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)    41501 2023-04-04 09:12:57.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/PKG-INFO
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)      643 2023-04-04 09:12:57.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/SOURCES.txt
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)        1 2023-04-04 09:12:57.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/dependency_links.txt
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)      144 2023-04-04 09:12:57.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/requires.txt
--rwxrwxrwx   0 oliver    (1000) oliver    (1000)       30 2023-04-04 09:12:57.000000 unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/top_level.txt
+drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-06 16:02:54.521874 unicorn-binance-websocket-api-1.45.0/
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)     1215 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.45.0/LICENSE
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    41791 2023-04-06 16:02:54.521874 unicorn-binance-websocket-api-1.45.0/PKG-INFO
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    39917 2023-04-06 15:23:39.000000 unicorn-binance-websocket-api-1.45.0/README.md
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)       38 2023-04-06 16:02:54.521874 unicorn-binance-websocket-api-1.45.0/setup.cfg
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)     4904 2023-04-04 00:02:14.000000 unicorn-binance-websocket-api-1.45.0/setup.py
+drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-06 16:02:54.238641 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)      498 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/__init__.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    26452 2023-04-06 12:13:20.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/connection.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)     2874 2023-04-06 10:06:24.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/connection_settings.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)     2168 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/exceptions.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)   208063 2023-04-06 16:01:36.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/manager.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    14327 2023-04-04 08:52:30.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/restclient.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)     3673 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/restserver.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    16355 2023-04-03 15:49:16.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/sockets.py
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    12337 2023-04-06 15:58:46.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/ws_api.py
+drwxrwxrwx   0 oliver    (1000) oliver    (1000)        0 2023-04-06 16:02:54.490175 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)    41791 2023-04-06 16:02:52.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/PKG-INFO
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)      683 2023-04-06 16:02:52.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/SOURCES.txt
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)        1 2023-04-06 16:02:52.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/dependency_links.txt
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)      144 2023-04-06 16:02:52.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/requires.txt
+-rwxrwxrwx   0 oliver    (1000) oliver    (1000)       30 2023-04-06 16:02:52.000000 unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/top_level.txt
```

### Comparing `unicorn-binance-websocket-api-1.44.1/LICENSE` & `unicorn-binance-websocket-api-1.45.0/LICENSE`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/PKG-INFO` & `unicorn-binance-websocket-api-1.45.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: unicorn-binance-websocket-api
-Version: 1.44.1
+Version: 1.45.0
 Summary: An unofficial Python API to use the Binance Websocket API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, jersey, us, jex, dex/chain+testnet) in a easy, fast, flexible, robust and fully-featured way.
 Home-page: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api
 Author: LUCIT Systems and Development
 Author-email: info@lucit.tech
 License: MIT License
 Project-URL: Howto, https://www.lucit.tech/unicorn-binance-websocket-api.html#howto
 Project-URL: Documentation, https://unicorn-binance-websocket-api.docs.lucit.tech
@@ -162,19 +162,22 @@
 [www.binance.com](https://www.binance.com/userCenter/createApi.html), 
 [testnet.binance.vision](https://testnet.binance.vision/), 
 [www.binance.us](https://www.binance.us/userCenter/createApi.html) or 
 [www.jex.com](https://www.jex.com/userCenter/createApi.html) - for the DEX you need a user address from 
 [www.binance.org](https://www.binance.org/en/create) or [testnet.binance.org](https://testnet.binance.org/en/create) 
 and you can [get funds](https://www.binance.vision/tutorials/binance-dex-funding-your-testnet-account) for the testnet.
 
-Be aware that the Binance websocket API just offers to receive data. If you would like to set orders, withdraws and so 
-on, you can use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
+Use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
 
 ### What are the benefits of the UNICORN Binance WebSocket API?
 - Fully managed websockets and 100% auto-reconnect! Also handles maintenance windows!
+
+- Support for [Binance Websocket API](https://developers.binance.com/docs/binance-trading-api/websocket_api), send 
+  requests like create_order, cancel_open_orders and many more directly over websocket!
+
 - [Supported exchanges](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Binance-websocket-endpoint-configuration-overview): 
 
 | Exchange                                                           | Exchange string                       | 
 |--------------------------------------------------------------------|---------------------------------------|
 | [Binance](https://www.binance.com)                                 | `binance.com`                         |
 | [Binance Testnet](https://testnet.binance.vision/)                 | `binance.com-testnet`                 |
 | [Binance Margin](https://www.binance.com)                          | `binance.com-margin`                  |
@@ -263,14 +266,18 @@
 - Also nice to use with the [Jupyter Notebook](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/tree/master/ipynb) :)
 
 - [Monitoring API service](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service) 
 and a [check_command](https://exchange.icinga.com/LUCIT/check_lucit_collector) 
 for [ICINGA](https://exchange.icinga.com/LUCIT/check_lucit_collector)/Nagios 
 [![icinga2-demo](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-websocket-api/master/images/misc/icinga.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service)
 
+- Integration of [test cases](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/actions/workflows/unit-tests.yml) and [examples](#examples).
+
+- Customizable base URL.
+
 - *Socks5 Proxy* support:
   ```
   ubwa = BinanceWebSocketApiManager(exchange="binance.com", socks5_proxy_server="127.0.0.1:9050") 
   ```
   Read the [docs](https://unicorn-binance-websocket-api.docs.lucit.tech/unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager)
   or this [how to](https://medium.com/@oliverzehentleitner/how-to-connect-to-binance-com-websockets-using-python-via-a-socks5-proxy-3c5a3e063f12) 
   for more information or try 
@@ -299,15 +306,15 @@
 [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/requirements.txt).
 
 If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Installation).
 
 ### A wheel and a source file of the latest release with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-websocket-api/)
 `pip install unicorn-binance-websocket-api --upgrade`
 
-### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-fy) via [CONDA-FORGE](https://conda-forge.org).
+### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-binance-websocket-api) via [CONDA-FORGE](https://conda-forge.org).
 `conda install -c conda-forge unicorn-binance-websocket-api`
 
 `conda update -c conda-forge unicorn-binance-websocket-api`
 
 ### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api)
 #### Linux, macOS, ...
 Run in bash:
```

### Comparing `unicorn-binance-websocket-api-1.44.1/README.md` & `unicorn-binance-websocket-api-1.45.0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -125,19 +125,22 @@
 [www.binance.com](https://www.binance.com/userCenter/createApi.html), 
 [testnet.binance.vision](https://testnet.binance.vision/), 
 [www.binance.us](https://www.binance.us/userCenter/createApi.html) or 
 [www.jex.com](https://www.jex.com/userCenter/createApi.html) - for the DEX you need a user address from 
 [www.binance.org](https://www.binance.org/en/create) or [testnet.binance.org](https://testnet.binance.org/en/create) 
 and you can [get funds](https://www.binance.vision/tutorials/binance-dex-funding-your-testnet-account) for the testnet.
 
-Be aware that the Binance websocket API just offers to receive data. If you would like to set orders, withdraws and so 
-on, you can use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
+Use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
 
 ### What are the benefits of the UNICORN Binance WebSocket API?
 - Fully managed websockets and 100% auto-reconnect! Also handles maintenance windows!
+
+- Support for [Binance Websocket API](https://developers.binance.com/docs/binance-trading-api/websocket_api), send 
+  requests like create_order, cancel_open_orders and many more directly over websocket!
+
 - [Supported exchanges](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Binance-websocket-endpoint-configuration-overview): 
 
 | Exchange                                                           | Exchange string                       | 
 |--------------------------------------------------------------------|---------------------------------------|
 | [Binance](https://www.binance.com)                                 | `binance.com`                         |
 | [Binance Testnet](https://testnet.binance.vision/)                 | `binance.com-testnet`                 |
 | [Binance Margin](https://www.binance.com)                          | `binance.com-margin`                  |
@@ -226,14 +229,18 @@
 - Also nice to use with the [Jupyter Notebook](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/tree/master/ipynb) :)
 
 - [Monitoring API service](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service) 
 and a [check_command](https://exchange.icinga.com/LUCIT/check_lucit_collector) 
 for [ICINGA](https://exchange.icinga.com/LUCIT/check_lucit_collector)/Nagios 
 [![icinga2-demo](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-websocket-api/master/images/misc/icinga.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service)
 
+- Integration of [test cases](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/actions/workflows/unit-tests.yml) and [examples](#examples).
+
+- Customizable base URL.
+
 - *Socks5 Proxy* support:
   ```
   ubwa = BinanceWebSocketApiManager(exchange="binance.com", socks5_proxy_server="127.0.0.1:9050") 
   ```
   Read the [docs](https://unicorn-binance-websocket-api.docs.lucit.tech/unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager)
   or this [how to](https://medium.com/@oliverzehentleitner/how-to-connect-to-binance-com-websockets-using-python-via-a-socks5-proxy-3c5a3e063f12) 
   for more information or try 
@@ -262,15 +269,15 @@
 [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/requirements.txt).
 
 If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Installation).
 
 ### A wheel and a source file of the latest release with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-websocket-api/)
 `pip install unicorn-binance-websocket-api --upgrade`
 
-### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-fy) via [CONDA-FORGE](https://conda-forge.org).
+### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-binance-websocket-api) via [CONDA-FORGE](https://conda-forge.org).
 `conda install -c conda-forge unicorn-binance-websocket-api`
 
 `conda update -c conda-forge unicorn-binance-websocket-api`
 
 ### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api)
 #### Linux, macOS, ...
 Run in bash:
```

### Comparing `unicorn-binance-websocket-api-1.44.1/setup.py` & `unicorn-binance-websocket-api-1.45.0/setup.py`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/connection.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/connection.py`

 * *Files 2% similar despite different names*

```diff
@@ -64,37 +64,41 @@
         self.api_secret = copy.deepcopy(self.manager.stream_list[stream_id]['api_secret'])
         self.ping_interval = copy.deepcopy(self.manager.stream_list[stream_id]['ping_interval'])
         self.ping_timeout = copy.deepcopy(self.manager.stream_list[stream_id]['ping_timeout'])
         self.close_timeout = copy.deepcopy(self.manager.stream_list[stream_id]['close_timeout'])
         self.channels = copy.deepcopy(channels)
         self.markets = copy.deepcopy(markets)
         self.symbols = copy.deepcopy(symbols)
-        self.add_timeout = True if "!userData" in str(str(channels) + str(markets)) else False
+        self.api = copy.deepcopy(self.manager.stream_list[stream_id]['api'])
+        self.add_timeout = True if "!userData" in str(str(channels) + str(markets)) or self.api is True else False
         if self.add_timeout:
             logger.debug(f"BinanceWebSocketApiConnection.receive({str(self.stream_id)}) socket_id="
                          f"{str(self.socket_id)}) - Adding timeout to `websocket.recv()` ")
 
     async def __aenter__(self):
         if self.manager.is_stop_request(self.stream_id):
             self.manager.stream_is_stopping(self.stream_id)
             sys.exit(0)
         uri = self.manager.create_websocket_uri(self.channels,
                                                 self.markets,
                                                 self.stream_id,
                                                 self.api_key,
                                                 self.api_secret,
-                                                symbols=self.symbols)
+                                                symbols=self.symbols,
+                                                api=self.manager.stream_list[self.stream_id]['api'])
         if uri is False:
             # cant get a valid URI, so this stream has to crash
             error_msg = "Probably no internet connection?"
             logger.critical("BinanceWebSocketApiConnection.await._conn.__aenter__(" + str(self.stream_id) + ", " +
                             str(self.channels) + ", " + str(self.markets) + ") - " + " error: 5 - " + str(error_msg))
             self.manager.stream_is_crashing(self.stream_id, str(error_msg))
             self.manager.set_restart_request(self.stream_id)
             sys.exit(1)
+        else:
+            self.manager.stream_list[self.stream_id]['websocket_uri'] = uri
         try:
             if isinstance(uri, dict):
                 # dict = error, string = valid url
                 if uri['code'] == -1102 or \
                         uri['code'] == -2008 or \
                         uri['code'] == -2014 or \
                         uri['code'] == -2015 or \
@@ -149,15 +153,16 @@
             try:
                 host, port = netloc.split(":")
             except ValueError as error_msg:
                 logger.debug(f"'netloc' split error: {netloc} - {error_msg}")
                 host = netloc
                 port = 443
             try:
-                logger.info(f"Connect socks5 proxy to {host}:{port}")
+                logger.info(f"Connect to socks5 proxy {host}:{port} (ssl_verification: "
+                            f"{self.manager.socks5_proxy_ssl_verification})")
                 websocket_socks5_proxy.connect((host, int(port)))
                 websocket_server_hostname = netloc
             except socks.ProxyConnectionError as error_msg:
                 error_msg = f"{error_msg} ({host}:{port})"
                 logger.critical(error_msg)
                 raise Socks5ProxyConnectionError(error_msg)
             except socks.GeneralProxyError as error_msg:
@@ -324,16 +329,20 @@
 
     async def receive(self):
         self.manager.set_heartbeat(self.stream_id)
         if self.manager.is_stop_request(self.stream_id):
             return False
         try:
             if self.add_timeout:
+                if self.api is True:
+                    timeout = 0.1
+                else:
+                    timeout = 1
                 received_data_json = await asyncio.wait_for(self.manager.websocket_list[self.stream_id].recv(),
-                                                            timeout=2.0)
+                                                            timeout=timeout)
             else:
                 received_data_json = await self.manager.websocket_list[self.stream_id].recv()
             if self.manager.is_stop_request(self.stream_id):
                 return False
             try:
                 if self.manager.restart_requests[self.stream_id]['status'] == "restarted":
                     self.manager.increase_reconnect_counter(self.stream_id)
```

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/exceptions.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/exceptions.py`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/manager.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/manager.py`

 * *Files 2% similar despite different names*

```diff
@@ -29,30 +29,32 @@
 # OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
 # ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
 # SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 
-
+from unicorn_binance_websocket_api.connection_settings import CEX_EXCHANGES, DEX_EXCHANGES, CONNECTION_SETTINGS
 from unicorn_binance_websocket_api.exceptions import StreamRecoveryError, UnknownExchange
-from unicorn_binance_websocket_api.sockets import BinanceWebSocketApiSocket
 from unicorn_binance_websocket_api.restclient import BinanceWebSocketApiRestclient
 from unicorn_binance_websocket_api.restserver import BinanceWebSocketApiRestServer
-from unicorn_binance_websocket_api.connection_settings import CEX_EXCHANGES, DEX_EXCHANGES, CONNECTION_SETTINGS
+from unicorn_binance_websocket_api.sockets import BinanceWebSocketApiSocket
+from unicorn_binance_websocket_api.ws_api import BinanceWebSocketApiWsApi
 from cheroot import wsgi
 from collections import deque
 from datetime import datetime
 from flask import Flask, redirect
 from flask_restful import Api
+from operator import itemgetter
 from typing import Literal, Optional, Union
 import asyncio
 import colorama
 import copy
 import logging
+import hmac
 import hashlib
 import os
 import platform
 import psutil
 import re
 import requests
 import ssl
@@ -60,15 +62,14 @@
 import threading
 import time
 import traceback
 import uuid
 import ujson as json
 import websockets
 
-
 logger = logging.getLogger("unicorn_binance_websocket_api")
 
 
 class BinanceWebSocketApiManager(threading.Thread):
     """
     An unofficial Python API to use the Binance Websocket API`s (com+testnet, com-margin+testnet,
     com-isolated_margin+testnet, com-futures+testnet, us, jex, dex/chain+testnet) in a easy, fast, flexible,
@@ -182,14 +183,16 @@
     :type high_performance:  bool
     :param debug: If True the lib adds additional information to logging outputs
     :type debug:  bool
     :param restful_base_uri: Override `restful_base_uri`. Example: `https://127.0.0.1`
     :type restful_base_uri:  str
     :param websocket_base_uri: Override `websocket_base_uri`. Example: `ws://127.0.0.1:8765/`
     :type websocket_base_uri:  str
+    :param websocket_api_base_uri: Override `websocket_api_base_uri`. Example: `ws://127.0.0.1:8765/`
+    :type websocket_api_base_uri:  str
     :param max_subscriptions_per_stream: Override the `max_subscriptions_per_stream` value. Example: 1024
     :type max_subscriptions_per_stream:  int
     :param exchange_type: Override the exchange type. Valid options are: 'cex', 'dex'
     :type exchange_type:  str
     :param socks5_proxy_server: Set this to activate the usage of a socks5 proxy. Example: '127.0.0.1:9050'
     :type socks5_proxy_server:  str
     :param socks5_proxy_user: Set this to activate the usage of a socks5 proxy user. Example: 'alice'
@@ -215,23 +218,24 @@
                  close_timeout_default: int = 1,
                  ping_interval_default: int = 5,
                  ping_timeout_default: int = 10,
                  high_performance: Optional[bool] = False,
                  debug: Optional[bool] = False,
                  restful_base_uri: Optional[str] = None,
                  websocket_base_uri: Optional[str] = None,
+                 websocket_api_base_uri: Optional[str] = None,
                  max_subscriptions_per_stream: Optional[int] = None,
                  exchange_type: Optional[Literal['cex', 'dex']] = None,
                  socks5_proxy_server: Optional[str] = None,
                  socks5_proxy_user: Optional[str] = None,
                  socks5_proxy_pass: Optional[str] = None,
                  socks5_proxy_ssl_verification: Optional[bool] = True,):
         threading.Thread.__init__(self)
         self.name = "unicorn-binance-websocket-api"
-        self.version = "1.44.1"
+        self.version = "1.45.0"
         logger.info(f"New instance of {self.get_user_agent()} on "
                     f"{str(platform.system())} {str(platform.release())} for exchange {exchange} started ...")
         self.debug = debug
         logger.info(f"Debug is {self.debug}")
         if disable_colorama is not True:
             logger.info(f"Initiating `colorama_{colorama.__version__}`")
             colorama.init()
@@ -265,14 +269,15 @@
                         f"Binance-websocket-endpoint-configuration-overview"
             logger.critical(error_msg)
             raise UnknownExchange(error_msg)
 
         self.exchange = exchange
         self.max_subscriptions_per_stream = max_subscriptions_per_stream or CONNECTION_SETTINGS[self.exchange][0]
         self.websocket_base_uri = websocket_base_uri or CONNECTION_SETTINGS[self.exchange][1]
+        self.websocket_api_base_uri = websocket_api_base_uri or CONNECTION_SETTINGS[self.exchange][2]
         self.restful_base_uri = restful_base_uri
         self.exchange_type = exchange_type
         if not self.exchange_type:
             if self.exchange in DEX_EXCHANGES:
                 self.exchange_type = "dex"
             elif self.exchange in CEX_EXCHANGES:
                 self.exchange_type = "cex"
@@ -363,14 +368,15 @@
         self.websocket_list = {}
         self.close_timeout_default = close_timeout_default
         self.ping_interval_default = ping_interval_default
         self.ping_timeout_default = ping_timeout_default
         self.start()
         self.replacement_text = "***SECRET_REMOVED***"
         self.restclient = BinanceWebSocketApiRestclient(self)
+        self.api = BinanceWebSocketApiWsApi(manager=self)
         self.warn_on_update = warn_on_update
         if warn_on_update and self.is_update_available():
             update_msg = f"Release {self.name}_" + self.get_latest_version() + " is available, " \
                          f"please consider updating! (Changelog: " \
                          f"https://unicorn-binance-websocket-api.docs.lucit.tech/CHANGELOG.html)"
             print(update_msg)
             logger.warning(update_msg)
@@ -385,14 +391,15 @@
                                    api_secret=False,
                                    symbols=False,
                                    output=False,
                                    ping_interval=None,
                                    ping_timeout=None,
                                    close_timeout=None,
                                    stream_buffer_maxlen=None,
+                                   api=False,
                                    process_stream_data=None):
         """
         Create a list entry for new streams
 
         :param stream_id: provide a stream_id (only needed for userData Streams (acquiring a listenKey)
         :type stream_id: str
         :param channels: provide the channels to create the URI
@@ -440,14 +447,18 @@
                               This parameter is passed through to the `websockets.client.connect()
                               <https://websockets.readthedocs.io/en/stable/topics/design.html?highlight=close_timeout#closing-handshake>`_
         :type close_timeout: int or None
         :param stream_buffer_maxlen: Set a max len for the `stream_buffer`. Only used in combination with a non generic
                                      `stream_buffer`. The generic `stream_buffer` uses always the value of
                                      `BinanceWebSocketApiManager()`.
         :type stream_buffer_maxlen: int or None
+        :param api: Setting this to `True` activates the creation of a Websocket API stream to send API requests via Websocket.
+                    Needs `api_key` and `api_secret` in combination. This type of stream can not be combined with a UserData
+                    stream or an other public endpoint. (Default is `False`)
+        :type api: bool
         :param process_stream_data: Provide a function/method to process the received webstream data. The function
                             will be called instead of
                             `add_to_stream_buffer() <unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager.add_to_stream_buffer>`_
                             like `process_stream_data(stream_data, stream_buffer_name)` where
                             `stream_data` cointains the raw_stream_data. If not provided, the raw stream_data will
                             get stored in the stream_buffer! `How to read from stream_buffer!
                             <https://unicorn-binance-websocket-api.docs.lucit.tech/README.html#and-4-more-lines-to-print-the-receives>`_
@@ -468,14 +479,15 @@
                                        'stream_label': copy.deepcopy(stream_label),
                                        'stream_buffer_name': copy.deepcopy(stream_buffer_name),
                                        'stream_buffer_maxlen': copy.deepcopy(stream_buffer_maxlen),
                                        'symbols': copy.deepcopy(symbols),
                                        'output': copy.deepcopy(output),
                                        'subscriptions': 0,
                                        'payload': [],
+                                       'api': copy.deepcopy(api),
                                        'api_key': copy.deepcopy(api_key),
                                        'api_secret': copy.deepcopy(api_secret),
                                        'dex_user_address': copy.deepcopy(self.dex_user_address),
                                        'ping_interval': copy.deepcopy(ping_interval),
                                        'ping_timeout': copy.deepcopy(ping_timeout),
                                        'close_timeout': copy.deepcopy(close_timeout),
                                        'status': 'starting',
@@ -494,15 +506,16 @@
                                        'logged_reconnects': [],
                                        'processed_transmitted_total': 0,
                                        'last_static_ping_listen_key': 0,
                                        'listen_key': False,
                                        'listen_key_cache_time':  10 * 60,
                                        'last_received_data_record': None,
                                        'processed_receives_statistic': {},
-                                       'transfer_rate_per_second': {'bytes': {}, 'speed': 0}}
+                                       'transfer_rate_per_second': {'bytes': {}, 'speed': 0},
+                                       'websocket_uri': None}
         logger.info("BinanceWebSocketApiManager._add_stream_to_stream_list(" +
                     str(stream_id) + ", " + str(channels) + ", " + str(markets) + ", " + str(stream_label) + ", "
                     + str(stream_buffer_name) + ", " + str(stream_buffer_maxlen) + ", " + str(symbols) + ")")
 
     def _create_stream_thread(self,
                               loop,
                               stream_id,
@@ -574,14 +587,50 @@
                     self.stream_list[stream_id]['last_stream_signal'] = "DISCONNECT"
             except KeyError as error_msg:
                 logger.debug(f"BinanceWebSocketApiManager._create_stream_thread() stream_id={str(stream_id)} - "
                              f"KeyError `error: 12` - {error_msg}")
             loop.close()
             self.set_socket_is_ready(stream_id)
 
+    def generate_signature(self, api_secret=None, data=None):
+        """
+        Signe the request.
+
+        :param api_secret:
+        :param data:
+
+        :return:
+        """
+        ordered_data = self.order_params(data)
+        query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data])
+        m = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
+        return m.hexdigest()
+
+    @staticmethod
+    def order_params(data):
+        """
+        Convert params to list with signature as last element
+
+        :param data:
+        :return:
+
+        """
+        has_signature = False
+        params = []
+        for key, value in data.items():
+            if key == 'signature':
+                has_signature = True
+            else:
+                params.append((key, value))
+        # sort parameters by key
+        params.sort(key=itemgetter(0))
+        if has_signature:
+            params.append(('signature', data['signature']))
+        return params
+
     def _frequent_checks(self):
         """
         This method gets started as a thread and is doing the frequent checks
         """
         frequent_checks_id = time.time()
         cpu_usage_time = False
         with self.frequent_checks_list_lock:
@@ -702,27 +751,28 @@
             # send keepalive for `!userData` streams every 30 minutes
             if active_stream_list:
                 for stream_id in active_stream_list:
                     if isinstance(active_stream_list[stream_id]['markets'], str):
                         active_stream_list[stream_id]['markets'] = [active_stream_list[stream_id]['markets'], ]
                     if isinstance(active_stream_list[stream_id]['channels'], str):
                         active_stream_list[stream_id]['channels'] = [active_stream_list[stream_id]['channels'], ]
-                    if "!userData" in active_stream_list[stream_id]['markets'] or \
-                            "!userData" in active_stream_list[stream_id]['channels']:
-                        if (active_stream_list[stream_id]['start_time'] +
-                            active_stream_list[stream_id]['listen_key_cache_time']) < time.time() and \
-                                (active_stream_list[stream_id]['last_static_ping_listen_key'] +
-                                 active_stream_list[stream_id]['listen_key_cache_time']) < time.time():
-                            # keep-alive the listenKey
-                            self.restclient.keepalive_listen_key(stream_id)
-                            # set last_static_ping_listen_key
-                            self.stream_list[stream_id]['last_static_ping_listen_key'] = time.time()
-                            self.set_heartbeat(stream_id)
-                            logger.info("BinanceWebSocketApiManager._frequent_checks() - sent listen_key keepalive "
-                                        "ping for stream_id=" + str(stream_id))
+                    if active_stream_list[stream_id]['api'] is False:
+                        if "!userData" in active_stream_list[stream_id]['markets'] or \
+                                "!userData" in active_stream_list[stream_id]['channels']:
+                            if (active_stream_list[stream_id]['start_time'] +
+                                active_stream_list[stream_id]['listen_key_cache_time']) < time.time() and \
+                                    (active_stream_list[stream_id]['last_static_ping_listen_key'] +
+                                     active_stream_list[stream_id]['listen_key_cache_time']) < time.time():
+                                # keep-alive the listenKey
+                                self.restclient.keepalive_listen_key(stream_id)
+                                # set last_static_ping_listen_key
+                                self.stream_list[stream_id]['last_static_ping_listen_key'] = time.time()
+                                self.set_heartbeat(stream_id)
+                                logger.info("BinanceWebSocketApiManager._frequent_checks() - sent listen_key keepalive "
+                                            "ping for stream_id=" + str(stream_id))
         sys.exit(0)
 
     def _handle_task_result(self, task: asyncio.Task) -> None:
         """
         This method is a callback for `loop.create_task()` to retrive the task exception and avoid the `Task exception
         was never retrieved` traceback on stdout:
         https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/issues/261
@@ -890,14 +940,30 @@
         except RuntimeError as error_msg:
             logger.critical("BinanceWebSocketApiManager._start_monitoring_api_thread() - Monitoring API service is "
                             "going down! - Info: " + str(error_msg))
         except OSError as error_msg:
             logger.critical("BinanceWebSocketApiManager._start_monitoring_api_thread() - Monitoring API service is "
                             "going down! - Info: " + str(error_msg))
 
+    def add_payload_to_stream(self, stream_id=None, payload: dict = None):
+        """
+        Add a payload to a stream by `stream_id`.
+
+        :param stream_id: id of a stream
+        :type stream_id: str
+        :param payload: The payload in JSON to add.
+        :type payload: dict
+        :return: bool
+        """
+        if payload is None or stream_id is None:
+            return False
+        else:
+            self.stream_list[stream_id]['payload'].append(payload)
+            return True
+
     def add_to_ringbuffer_error(self, error):
         """
         Add received error messages from websocket endpoints to the error ringbuffer
 
         :param error: The data to add.
         :type error: string
         :return: bool
@@ -1161,26 +1227,27 @@
         logger.info("BinanceWebSocketApiManager.create_payload(" + str(stream_id) + ", "
                     + str(channels) + ", " + str(markets) + ") - Payload: " + str(payload))
         logger.info("BinanceWebSocketApiManager.create_payload(" + str(stream_id) + ", " + str(channels) + ", " +
                     str(markets) + ") finished ...")
         return payload
 
     def create_stream(self,
-                      channels,
-                      markets,
+                      channels=[],
+                      markets=[],
                       stream_label=None,
                       stream_buffer_name=False,
                       api_key=False,
                       api_secret=False,
                       symbols=False,
                       output=False,
                       ping_interval=None,
                       ping_timeout=None,
                       close_timeout=None,
                       stream_buffer_maxlen=None,
+                      api=False,
                       process_stream_data=None):
         """
         Create a websocket stream
 
         If you provide 2 markets and 2 channels, then you are going to create 4 subscriptions (markets * channels).
 
             Example:
@@ -1268,43 +1335,54 @@
                               This parameter is passed through to the `websockets.client.connect()
                               <https://websockets.readthedocs.io/en/stable/topics/design.html?highlight=close_timeout#closing-handshake>`_
         :type close_timeout: int or None
         :param stream_buffer_maxlen: Set a max len for the `stream_buffer`. Only used in combination with a non generic
                                      `stream_buffer`. The generic `stream_buffer` uses always the value of
                                      `BinanceWebSocketApiManager()`.
         :type stream_buffer_maxlen: int or None
+        :param api: Setting this to `True` activates the creation of a Websocket API stream to send API requests via Websocket.
+                    Needs `api_key` and `api_secret` in combination. This type of stream can not be combined with a UserData
+                    stream or an other public endpoint. (Default is `False`)
+        :type api: bool
         :param process_stream_data: Provide a function/method to process the received webstream data (callback). The
                             function will be called instead of
                             `add_to_stream_buffer() <unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager.add_to_stream_buffer>`_
                             like `process_stream_data(stream_data)` where
                             `stream_data` cointains the raw_stream_data. If not provided, the raw stream_data will
                             get stored in the stream_buffer or provided to the global callback function provided during
                             object instantiation! `How to read from stream_buffer!
                             <https://unicorn-binance-websocket-api.docs.lucit.tech/README.html?highlight=pop_stream_data_from_stream_buffer#and-4-more-lines-to-print-the-receives>`_
         :type process_stream_data: function
         :return: stream_id or 'False'
         """
-        # create a stream
-        if isinstance(channels, bool):
-            logger.error(f"BinanceWebSocketApiManager.create_stream(" + str(channels) + ", " + str(markets) + ", "
-                         + str(stream_label) + ", " + str(stream_buffer_name) + ", " + str(symbols) + ", " +
-                         str(stream_buffer_maxlen) + ") - Parameter "
-                         f"`channels` must be str, tuple, list or a set!")
-            return False
-        elif isinstance(markets, bool):
+        # handle Websocket API streams: https://developers.binance.com/docs/binance-trading-api/websocket_api
+        if api is True:
+            if api_key is False or api_secret is False:
+                logger.error(f"BinanceWebSocketApiManager.create_stream(api={api}) - `api_key` and `api_secret` are "
+                             f"mandatory if `api=True`")
+                return False
+        else:
+            # create an ordinary stream
             if isinstance(channels, bool):
                 logger.error(f"BinanceWebSocketApiManager.create_stream(" + str(channels) + ", " + str(markets) + ", "
                              + str(stream_label) + ", " + str(stream_buffer_name) + ", " + str(symbols) + ", " +
                              str(stream_buffer_maxlen) + ") - Parameter "
-                             f"`markets` must be str, tuple, list or a set!")
-            return False
-        if type(channels) is str:
-            channels = [channels]
-        if type(markets) is str:
-            markets = [markets]
+                             f"`channels` must be str, tuple, list or a set!")
+                return False
+            elif isinstance(markets, bool):
+                if isinstance(channels, bool):
+                    logger.error(f"BinanceWebSocketApiManager.create_stream(" + str(channels) + ", " + str(markets) + ", "
+                                 + str(stream_label) + ", " + str(stream_buffer_name) + ", " + str(symbols) + ", " +
+                                 str(stream_buffer_maxlen) + ") - Parameter "
+                                 f"`markets` must be str, tuple, list or a set!")
+                return False
+            if type(channels) is str:
+                channels = [channels]
+            if type(markets) is str:
+                markets = [markets]
         output = output or self.output_default
         close_timeout = close_timeout or self.close_timeout_default
         ping_interval = ping_interval or self.ping_interval_default
         ping_timeout = ping_timeout or self.ping_timeout_default
         stream_id = self.get_new_uuid_id()
         markets_new = []
         if stream_buffer_name is True:
@@ -1321,36 +1399,37 @@
                     if re.match(r'[a-zA-Z0-9]{41,43}', market) is None:
                         markets_new.append(str(market).upper())
                     else:
                         markets_new.append(str(market))
                 elif self.is_exchange_type('cex'):
                     markets_new.append(str(market).lower())
         logger.info("BinanceWebSocketApiManager.create_stream(" + str(channels) + ", " + str(markets_new) + ", "
-                    + str(stream_label) + ", " + str(stream_buffer_name) + ", " + str(symbols) + ") with stream_id="
-                    + str(stream_id))
+                    + str(stream_label) + ", " + str(stream_buffer_name) + ", " + str(symbols) + ", " + str(symbols) +
+                    ", " + str(api) + ") with stream_id=" + str(stream_id))
         self._add_stream_to_stream_list(stream_id,
                                         channels,
                                         markets_new,
                                         stream_label,
                                         stream_buffer_name,
                                         symbols=symbols,
                                         api_key=api_key,
                                         api_secret=api_secret,
                                         output=output,
                                         ping_interval=ping_interval,
                                         ping_timeout=ping_timeout,
                                         close_timeout=close_timeout,
                                         stream_buffer_maxlen=stream_buffer_maxlen,
+                                        api=api,
                                         process_stream_data=process_stream_data)
         try:
             loop = asyncio.new_event_loop()
         except OSError as error_msg:
             logger.critical(f"BinanceWebSocketApiManager.create_stream({str(channels)}, {str(markets_new)}, "
-                            f"{str(stream_label)}, {str(stream_buffer_name)}, {str(symbols)}), {stream_buffer_maxlen} "
-                            f"with stream_id={str(stream_id)} - OSError  - can not create stream - "
+                            f"{str(stream_label)}, {str(stream_buffer_name)}, {str(symbols)}), {stream_buffer_maxlen}, "
+                            f"{api} with stream_id={str(stream_id)} - OSError  - can not create stream - "
                             f"error_msg: {str(error_msg)}")
             return False
         self.event_loops[stream_id] = loop
         self.set_socket_is_not_ready(stream_id)
         thread = threading.Thread(target=self._create_stream_thread,
                                   args=(loop,
                                         stream_id,
@@ -1362,20 +1441,21 @@
                                   name=f"_create_stream_thread:  stream_id={stream_id}, time={time.time()}")
         thread.start()
         self.stream_threads[stream_id] = thread
         while self.socket_is_ready[stream_id] is False and self.high_performance is False:
             # This loop will wait till the thread and the asyncio init is ready. This avoids two possible errors as
             # described here: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/issues/131
             logger.debug(f"BinanceWebSocketApiManager.create_stream({str(channels)}, {str(markets_new)}, "
-                         f"{str(stream_label)}, {str(stream_buffer_name)}, {str(symbols)}, {stream_buffer_maxlen}) "
-                         f"with stream_id={str(stream_id)} - Waiting till new socket and asyncio is ready")
+                         f"{str(stream_label)}, {str(stream_buffer_name)}, {str(symbols)}, {stream_buffer_maxlen}), "
+                         f"{api} with stream_id={str(stream_id)} - Waiting till new socket and asyncio is ready")
             time.sleep(1)
         return stream_id
 
-    def create_websocket_uri(self, channels, markets, stream_id=False, api_key=False, api_secret=False, symbols=False):
+    def create_websocket_uri(self, channels, markets, stream_id=False, api_key=False, api_secret=False, symbols=False,
+                             api=False):
         """
         Create a websocket URI
 
         :param channels: provide the channels to create the URI
         :type channels: str, tuple, list, set
         :param markets: provide the markets to create the URI
         :type markets: str, tuple, list, set
@@ -1384,15 +1464,24 @@
         :param api_key: provide a valid Binance API key
         :type api_key: str
         :param api_secret: provide a valid Binance API secret
         :type api_secret: str
         :param symbols: provide the symbols for isolated_margin user_data streams
         :type symbols: str
         :return: str or False
+        :param api: Setting this to `True` activates the creation of a Websocket API stream to send API requests via Websocket.
+                    Needs `api_key` and `api_secret` in combination. This type of stream can not be combined with a UserData
+                    stream or an other public endpoint. (Default is `False`)
+        :type api: bool
         """
+        if api is True:
+            logger.info("BinanceWebSocketApiManager.create_websocket_uri(" + str(channels) + ", " +
+                        str(markets) + ", " + ", " + str(symbols) + ", " + str(api) + " - Created websocket URI for "
+                        "stream_id=" + str(stream_id) + " is " + self.websocket_api_base_uri)
+            return self.websocket_api_base_uri
         if isinstance(channels, bool):
             logger.error(f"BinanceWebSocketApiManager.create_websocket_uri({str(channels)}, {str(markets)}"
                          f", {str(symbols)}) - error_msg: Parameter `channels` must be str, tuple, list "
                          f"or a set!")
             return False
         elif isinstance(markets, bool):
             logger.error(f"BinanceWebSocketApiManager.create_websocket_uri({str(channels)}, {str(markets)}"
@@ -1700,14 +1789,23 @@
         """
         if self.debug:
             debug_msg = f" - called by {str(traceback.format_stack()[-2]).strip()}"
         else:
             debug_msg = ""
         return debug_msg
 
+    @staticmethod
+    def get_timestamp() -> int:
+        """
+        Get a Binance conform Timestamp.
+
+        :return: int
+        """
+        return int(time.time() * 1000)
+
     def get_used_weight(self):
         """
         Get used_weight, last status_code and the timestamp of the last status update
 
         :return: dict
         """
         return self.binance_api_status
@@ -2991,16 +3089,18 @@
             uptime = self.get_human_uptime(stream_info['processed_receives_statistic']['uptime'])
             print(first_row +
                   " exchange: " + str(self.stream_list[stream_id]['exchange']) + f"{proxy}\r\n" +
                   str(add_string) +
                   " stream_id:", str(stream_id), "\r\n" +
                   str(stream_label_row) +
                   " stream_buffer_maxlen:", str(stream_info['stream_buffer_maxlen']), "\r\n" +
+                  f" api: {self.stream_list[stream_id]['api']}\r\n" +
                   " channels (" + str(len(stream_info['channels'])) + "):", str(stream_info['channels']), "\r\n" +
                   " markets (" + str(len(stream_info['markets'])) + "):", str(stream_info['markets']), "\r\n" +
+                  f" websocket_uri: {self.stream_list[stream_id]['websocket_uri']}\r\n" +
                   str(symbol_row) +
                   " subscriptions: " + str(self.stream_list[stream_id]['subscriptions']) + "\r\n" +
                   str(payload_row) +
                   str(status_row) +
                   str(dex_user_address_row) +
                   f" ping_interval: {ping_interval}\r\n"
                   f" ping_timeout: {ping_timeout}\r\n"
```

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/restclient.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/restclient.py`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/restserver.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/restserver.py`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api/sockets.py` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api/sockets.py`

 * *Files identical despite different names*

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/PKG-INFO` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: unicorn-binance-websocket-api
-Version: 1.44.1
+Version: 1.45.0
 Summary: An unofficial Python API to use the Binance Websocket API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, jersey, us, jex, dex/chain+testnet) in a easy, fast, flexible, robust and fully-featured way.
 Home-page: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api
 Author: LUCIT Systems and Development
 Author-email: info@lucit.tech
 License: MIT License
 Project-URL: Howto, https://www.lucit.tech/unicorn-binance-websocket-api.html#howto
 Project-URL: Documentation, https://unicorn-binance-websocket-api.docs.lucit.tech
@@ -162,19 +162,22 @@
 [www.binance.com](https://www.binance.com/userCenter/createApi.html), 
 [testnet.binance.vision](https://testnet.binance.vision/), 
 [www.binance.us](https://www.binance.us/userCenter/createApi.html) or 
 [www.jex.com](https://www.jex.com/userCenter/createApi.html) - for the DEX you need a user address from 
 [www.binance.org](https://www.binance.org/en/create) or [testnet.binance.org](https://testnet.binance.org/en/create) 
 and you can [get funds](https://www.binance.vision/tutorials/binance-dex-funding-your-testnet-account) for the testnet.
 
-Be aware that the Binance websocket API just offers to receive data. If you would like to set orders, withdraws and so 
-on, you can use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
+Use the [UNICORN Binance REST API](https://www.lucit.tech/unicorn-binance-rest-api.html) in combination. 
 
 ### What are the benefits of the UNICORN Binance WebSocket API?
 - Fully managed websockets and 100% auto-reconnect! Also handles maintenance windows!
+
+- Support for [Binance Websocket API](https://developers.binance.com/docs/binance-trading-api/websocket_api), send 
+  requests like create_order, cancel_open_orders and many more directly over websocket!
+
 - [Supported exchanges](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Binance-websocket-endpoint-configuration-overview): 
 
 | Exchange                                                           | Exchange string                       | 
 |--------------------------------------------------------------------|---------------------------------------|
 | [Binance](https://www.binance.com)                                 | `binance.com`                         |
 | [Binance Testnet](https://testnet.binance.vision/)                 | `binance.com-testnet`                 |
 | [Binance Margin](https://www.binance.com)                          | `binance.com-margin`                  |
@@ -263,14 +266,18 @@
 - Also nice to use with the [Jupyter Notebook](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/tree/master/ipynb) :)
 
 - [Monitoring API service](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service) 
 and a [check_command](https://exchange.icinga.com/LUCIT/check_lucit_collector) 
 for [ICINGA](https://exchange.icinga.com/LUCIT/check_lucit_collector)/Nagios 
 [![icinga2-demo](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-websocket-api/master/images/misc/icinga.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service)
 
+- Integration of [test cases](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/actions/workflows/unit-tests.yml) and [examples](#examples).
+
+- Customizable base URL.
+
 - *Socks5 Proxy* support:
   ```
   ubwa = BinanceWebSocketApiManager(exchange="binance.com", socks5_proxy_server="127.0.0.1:9050") 
   ```
   Read the [docs](https://unicorn-binance-websocket-api.docs.lucit.tech/unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager)
   or this [how to](https://medium.com/@oliverzehentleitner/how-to-connect-to-binance-com-websockets-using-python-via-a-socks5-proxy-3c5a3e063f12) 
   for more information or try 
@@ -299,15 +306,15 @@
 [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/requirements.txt).
 
 If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/Installation).
 
 ### A wheel and a source file of the latest release with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-websocket-api/)
 `pip install unicorn-binance-websocket-api --upgrade`
 
-### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-fy) via [CONDA-FORGE](https://conda-forge.org).
+### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-binance-websocket-api) via [CONDA-FORGE](https://conda-forge.org).
 `conda install -c conda-forge unicorn-binance-websocket-api`
 
 `conda update -c conda-forge unicorn-binance-websocket-api`
 
 ### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api)
 #### Linux, macOS, ...
 Run in bash:
```

### Comparing `unicorn-binance-websocket-api-1.44.1/unicorn_binance_websocket_api.egg-info/SOURCES.txt` & `unicorn-binance-websocket-api-1.45.0/unicorn_binance_websocket_api.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -5,12 +5,13 @@
 unicorn_binance_websocket_api/connection.py
 unicorn_binance_websocket_api/connection_settings.py
 unicorn_binance_websocket_api/exceptions.py
 unicorn_binance_websocket_api/manager.py
 unicorn_binance_websocket_api/restclient.py
 unicorn_binance_websocket_api/restserver.py
 unicorn_binance_websocket_api/sockets.py
+unicorn_binance_websocket_api/ws_api.py
 unicorn_binance_websocket_api.egg-info/PKG-INFO
 unicorn_binance_websocket_api.egg-info/SOURCES.txt
 unicorn_binance_websocket_api.egg-info/dependency_links.txt
 unicorn_binance_websocket_api.egg-info/requires.txt
 unicorn_binance_websocket_api.egg-info/top_level.txt
```

