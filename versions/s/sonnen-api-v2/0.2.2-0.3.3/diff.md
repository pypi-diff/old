# Comparing `tmp/sonnen-api-v2-0.2.2.tar.gz` & `tmp/sonnen-api-v2-0.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sonnen-api-v2-0.2.2.tar", last modified: Thu Mar 23 13:56:49 2023, max compression
+gzip compressed data, was "sonnen-api-v2-0.3.3.tar", last modified: Wed Apr  5 09:18:04 2023, max compression
```

## Comparing `sonnen-api-v2-0.2.2.tar` & `sonnen-api-v2-0.3.3.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-03-23 13:56:49.833438 sonnen-api-v2-0.2.2/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.2.2/LICENSE
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1492 2023-03-23 13:56:49.833438 sonnen-api-v2-0.2.2/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.2.2/README.md
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-03-23 13:56:49.833438 sonnen-api-v2-0.2.2/setup.cfg
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      895 2023-03-23 13:56:47.000000 sonnen-api-v2-0.2.2/setup.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-03-23 13:56:49.830104 sonnen-api-v2-0.2.2/sonnen_api_v2/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-03-23 13:55:28.000000 sonnen-api-v2-0.2.2/sonnen_api_v2/__init__.py
--rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    13574 2023-03-23 06:35:57.000000 sonnen-api-v2-0.2.2/sonnen_api_v2/sonnen.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-03-23 13:56:49.830104 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1492 2023-03-23 13:56:49.000000 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-03-23 13:56:49.000000 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/SOURCES.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-03-23 13:56:49.000000 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/dependency_links.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       17 2023-03-23 13:56:49.000000 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/requires.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-03-23 13:56:49.000000 sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/top_level.txt
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-03-23 13:56:49.833438 sonnen-api-v2-0.2.2/tests/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.2.2/tests/__init__.py
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.2.2/tests/test_sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/LICENSE
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/README.md
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/setup.cfg
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.3/setup.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/sonnen_api_v2/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-05 09:10:07.000000 sonnen-api-v2-0.3.3/sonnen_api_v2/__init__.py
+-rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    15967 2023-04-04 08:48:06.000000 sonnen-api-v2-0.3.3/sonnen_api_v2/sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/SOURCES.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/dependency_links.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/requires.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/top_level.txt
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/tests/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/tests/__init__.py
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/tests/test_sonnen.py
```

### Comparing `sonnen-api-v2-0.2.2/LICENSE` & `sonnen-api-v2-0.3.3/LICENSE`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.2.2/PKG-INFO` & `sonnen-api-v2-0.3.3/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.2.2
+Version: 0.3.3
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
@@ -23,12 +23,8 @@
         IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
         FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
         AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
         LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
         OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
         SOFTWARE.
         
-Platform: UNKNOWN
 License-File: LICENSE
-
-UNKNOWN
-
```

### Comparing `sonnen-api-v2-0.2.2/setup.py` & `sonnen-api-v2-0.3.3/setup.py`

 * *Files 14% similar despite different names*

```diff
@@ -23,10 +23,11 @@
     packages=find_packages(exclude='tests'),
     url='https://github.com/Katamave/sonnen_api_v2.git',
     license=read_file('LICENSE'),
     author='Vaclav Silhan',
     author_email='katamave@gmail.com',
     description=read_file('README.md'),
     install_requires=[
-        'requests>=2.27.1',
+        'aiohttp>=3.8.4',
+        'requests>=2.27.1'
     ]
 )
```

### Comparing `sonnen-api-v2-0.2.2/sonnen_api_v2/sonnen.py` & `sonnen-api-v2-0.3.3/sonnen_api_v2/sonnen.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,16 @@
 """ SonnenAPI v2 module """
-
+import asyncio
 import functools
 
 import datetime
+from time import time
+import aiohttp
+import logging
+
 import requests
 
 
 def get_item(func):
     """ Decorator for getting json data from Sonnen API """
     @functools.wraps(func)
     def inner(*args):
@@ -51,18 +55,22 @@
     BATTERY_MIN_MODULE_TEMP = 'minimummoduletemperature'
     BATTERY_RSOC = 'relativestateofcharge'
     BATTERY_REMAINING_CAPACITY = 'remainingcapacity'
     BATTERY_SYSTEM_CURRENT = 'systemcurrent'
     BATTERY_SYSTEM_VOLTAGE = 'systemdcvoltage'
 
     # default timeout
-    TIMEOUT = 5
+    TIMEOUT = aiohttp.ClientTimeout(total=5)
 
-    def __init__(self, auth_token: str, ip_address: str) -> None:
+    def __init__(self, auth_token: str,
+                 ip_address: str,
+                 logger: logging.Logger = None) -> None:
+        self._last_updated = None
         self.ip_address = ip_address
+        self.logger = logger
         self.auth_token = auth_token
         self.url = f'http://{ip_address}'
         self.header = {'Auth-Token': self.auth_token}
 
         # read api endpoints
         self.status_api_endpoint = f'{self.url}/api/v2/status'
         self.latest_details_api_endpoint = f'{self.url}/api/v2/latestdata'
@@ -70,74 +78,132 @@
 
         # api data
         self._latest_details_data = {}
         self._status_data = {}
         self._ic_status = {}
         self._battery_status = {}
 
-    def fetch_latest_details(self) -> bool:
-        """Fetches latest details api
-            Returns:
-                True if fetch was successful, else False
-        """
+    def _log_error(self, msg):
+        if self.logger:
+            self.logger.error(msg)
+        else:
+            print(msg)
+
+    def _fetch_data(self, url: str) -> dict:
+        """Fetches data from API endpoint"""
         try:
-            response = requests.get(
-                self.latest_details_api_endpoint,
-                headers=self.header, timeout=self.TIMEOUT
-            )
+            response = requests.get(url, headers=self.header, timeout=self.TIMEOUT.total)
             if response.status_code == 200:
-                self._latest_details_data = response.json()
-                self._ic_status = self._latest_details_data[self.IC_STATUS]
-                return True
-        except requests.ConnectionError as conn_error:
-            print('Connection error to battery system - ', conn_error)
+                data = response.json()
+                return data
+        except ConnectionError as error:
+            self._log_error(f'Connection error to the battery system!')
+            return {}
+
+    def fetch_latest_details(self) -> bool:
+        """Fetches latest details api"""
+        try:
+            self._latest_details_data = self._fetch_data(self.latest_details_api_endpoint)
+            return True
+        except Exception as error:
+            self._log_error(f'Error while data parsing for {self.latest_details_api_endpoint} {error}')
         return False
 
-    def fetch_status(self) -> bool:
-        """Fetches status api
-            Returns:
-                True if fetch was successful, else False
-        """
+    def fetch_status(self):
+        """Fetches status api"""
+        try:
+            self._status_data = self._fetch_data(self.status_api_endpoint)
+            return True
+        except Exception as error:
+            self._log_error(f'Error while data parsing for {self.status_api_endpoint}')
+        return False
+
+    def fetch_battery_status(self):
+        """Fetches battery api endpoint"""
+        try:
+            self._battery_status = self._fetch_data(self.battery_api_endpoint)
+            return True
+        except Exception as error:
+            self._log_error(f'Error while data parsing for {self.battery_api_endpoint}{error}')
+
+    async def _async_fetch_data(self, url: str) -> dict:
+        """Fetches data from the API endpoint with asyncio"""
         try:
-            response = requests.get(
-                self.status_api_endpoint,
+            async with aiohttp.ClientSession(
                 headers=self.header, timeout=self.TIMEOUT
+            ) as session:
+                response = await session.get(url)
+        except aiohttp.ClientError as error:
+            self._log_error(f'Battery: {self.ip_address} is offline!')
+        except asyncio.TimeoutError as error:
+            self._log_error(f'Timeout error while accessing: {url}')
+
+        try:
+            return await response.json()
+        except Exception as error:
+            self._log_error('Error while data parsing')
+            return {}
+
+    async def async_fetch_latest_details(self) -> bool:
+        """Fetches latest details api as coroutine"""
+        try:
+            self._latest_details_data = await self._async_fetch_data(
+                self.latest_details_api_endpoint
             )
-            if response.status_code == 200:
-                self._status_data = response.json()
-                return True
-        except requests.ConnectionError as conn_error:
-            print('Connection error to battery system - ', conn_error)
-        return False
+            self._ic_status = self._latest_details_data[self.IC_STATUS]
+            return True
+        except Exception as error:
+            self._log_error('Error occurred while data parsing')
+            return False
 
-    def fetch_battery_status(self) -> bool:
-        """Fetches battery details api
-            Returns:
-                True if fetch was successful, else False
-        """
+    async def async_fetch_status(self) -> bool:
+        """Fetches status api as coroutine"""
         try:
-            response = requests.get(
-                self.battery_api_endpoint,
-                headers=self.header, timeout=self.TIMEOUT)
-            if response.status_code == 200:
-                self._battery_status = response.json()
-                return True
-        except requests.ConnectionError as conn_err:
-            print('Connection error to battery system - ', conn_err)
+            self._status_data = await self._async_fetch_data(
+                self.latest_details_api_endpoint
+            )
+            return True
+        except Exception as error:
+            self._log_error('Error occurred while data parsing')
+            return False
+
+    async def async_fetch_battery_status(self) -> bool:
+        """Fetches battery details api as coroutine"""
+        try:
+            self._battery_status = await self._async_fetch_data(
+                self.battery_api_endpoint
+            )
+            return True
+        except Exception as err:
+            self._log_error(f'Error ocurred while data parsing')
         return False
 
+    async def async_update(self) -> bool:
+        """Updates data from apis of the sonnenBatterie as coroutine"""
+        success = await self.async_fetch_latest_details()
+        success = success and await self.async_fetch_status()
+        success = success and await self.async_fetch_battery_status()
+        self.last_updated = time()
+        return success
+
     def update(self) -> bool:
-        """Updates data from apis of the sonnenBatterie
-            Returns:
-                True if all updates were successful, else False
-        """
+        """Updates data from apis of the sonnenBatterie"""
         success = self.fetch_latest_details()
         success = success and self.fetch_status()
         success = success and self.fetch_battery_status()
+        self.last_updated = time()
         return success
+    
+    @property
+    def last_updated(self) -> time:
+        return self._last_updated
+
+    @last_updated.setter
+    def last_updated(self, last_updated: time):
+        self._last_updated = last_updated
 
     @get_item
     def consumption(self) -> int:
         """Consumption of the household
             Returns:
                 house consumption in Watt
         """
```

### Comparing `sonnen-api-v2-0.2.2/sonnen_api_v2.egg-info/PKG-INFO` & `sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.2.2
+Version: 0.3.3
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
@@ -23,12 +23,8 @@
         IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
         FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
         AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
         LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
         OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
         SOFTWARE.
         
-Platform: UNKNOWN
 License-File: LICENSE
-
-UNKNOWN
-
```

### Comparing `sonnen-api-v2-0.2.2/tests/test_sonnen.py` & `sonnen-api-v2-0.3.3/tests/test_sonnen.py`

 * *Files identical despite different names*

