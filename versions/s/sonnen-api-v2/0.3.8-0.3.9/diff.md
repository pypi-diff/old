# Comparing `tmp/sonnen-api-v2-0.3.8.tar.gz` & `tmp/sonnen-api-v2-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sonnen-api-v2-0.3.8.tar", last modified: Fri Apr  7 13:04:26 2023, max compression
+gzip compressed data, was "sonnen-api-v2-0.3.9.tar", last modified: Fri Apr  7 13:15:05 2023, max compression
```

## Comparing `sonnen-api-v2-0.3.8.tar` & `sonnen-api-v2-0.3.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.8/LICENSE
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.8/README.md
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/setup.cfg
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.8/setup.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/sonnen_api_v2/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-07 13:04:25.000000 sonnen-api-v2-0.3.8/sonnen_api_v2/__init__.py
--rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    16110 2023-04-07 13:04:25.000000 sonnen-api-v2-0.3.8/sonnen_api_v2/sonnen.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 13:04:26.000000 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-07 13:04:26.000000 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/SOURCES.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-07 13:04:26.000000 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/dependency_links.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-07 13:04:26.000000 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/requires.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-07 13:04:26.000000 sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/top_level.txt
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:04:26.965619 sonnen-api-v2-0.3.8/tests/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.8/tests/__init__.py
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.8/tests/test_sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.9/LICENSE
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.9/README.md
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/setup.cfg
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.9/setup.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/sonnen_api_v2/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-07 13:15:02.000000 sonnen-api-v2-0.3.9/sonnen_api_v2/__init__.py
+-rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    16176 2023-04-07 13:15:02.000000 sonnen-api-v2-0.3.9/sonnen_api_v2/sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 13:15:05.000000 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-07 13:15:05.000000 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/SOURCES.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-07 13:15:05.000000 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/dependency_links.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-07 13:15:05.000000 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/requires.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-07 13:15:05.000000 sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/top_level.txt
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 13:15:05.328988 sonnen-api-v2-0.3.9/tests/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.9/tests/__init__.py
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.9/tests/test_sonnen.py
```

### Comparing `sonnen-api-v2-0.3.8/LICENSE` & `sonnen-api-v2-0.3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.8/PKG-INFO` & `sonnen-api-v2-0.3.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.8
+Version: 0.3.9
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.8/setup.py` & `sonnen-api-v2-0.3.9/setup.py`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.8/sonnen_api_v2/sonnen.py` & `sonnen-api-v2-0.3.9/sonnen_api_v2/sonnen.py`

 * *Files 1% similar despite different names*

```diff
@@ -147,37 +147,37 @@
         try:
             self._latest_details_data = await self._async_fetch_data(
                 self.latest_details_api_endpoint
             )
             self._ic_status = self._latest_details_data[self.IC_STATUS]
             return True
         except Exception as error:
-            self._log_error('Error occurred while data parsing')
+            self._log_error(f'Error occurred while data parsing latest details:{error}')
             return False
 
     async def async_fetch_status(self) -> bool:
         """Fetches status api as coroutine"""
         try:
             self._status_data = await self._async_fetch_data(
                 self.latest_details_api_endpoint
             )
             return True
         except Exception as error:
-            self._log_error('Error occurred while data parsing')
+            self._log_error(f'Error occurred while data parsing status:{error}')
             return False
 
     async def async_fetch_battery_status(self) -> bool:
         """Fetches battery details api as coroutine"""
         try:
             self._battery_status = await self._async_fetch_data(
                 self.battery_api_endpoint
             )
             return True
-        except Exception as err:
-            self._log_error(f'Error ocurred while data parsing')
+        except Exception as error:
+            self._log_error(f'Error occurred while data parsing battery status:{error}')
         return False
 
     async def async_update(self) -> bool:
         """Updates data from apis of the sonnenBatterie as coroutine"""
         success = await self.async_fetch_latest_details()
         success = success and await self.async_fetch_status()
         success = success and await self.async_fetch_battery_status()
```

### Comparing `sonnen-api-v2-0.3.8/sonnen_api_v2.egg-info/PKG-INFO` & `sonnen-api-v2-0.3.9/sonnen_api_v2.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.8
+Version: 0.3.9
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.8/tests/test_sonnen.py` & `sonnen-api-v2-0.3.9/tests/test_sonnen.py`

 * *Files identical despite different names*

