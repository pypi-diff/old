# Comparing `tmp/sonnen-api-v2-0.3.5.tar.gz` & `tmp/sonnen-api-v2-0.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sonnen-api-v2-0.3.5.tar", last modified: Fri Apr  7 08:43:10 2023, max compression
+gzip compressed data, was "sonnen-api-v2-0.3.6.tar", last modified: Fri Apr  7 12:35:22 2023, max compression
```

## Comparing `sonnen-api-v2-0.3.5.tar` & `sonnen-api-v2-0.3.6.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 08:43:10.688086 sonnen-api-v2-0.3.5/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.5/LICENSE
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 08:43:10.688086 sonnen-api-v2-0.3.5/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.5/README.md
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-07 08:43:10.688086 sonnen-api-v2-0.3.5/setup.cfg
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.5/setup.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 08:43:10.684753 sonnen-api-v2-0.3.5/sonnen_api_v2/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-07 08:42:49.000000 sonnen-api-v2-0.3.5/sonnen_api_v2/__init__.py
--rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    16091 2023-04-07 08:42:49.000000 sonnen-api-v2-0.3.5/sonnen_api_v2/sonnen.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 08:43:10.684753 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 08:43:10.000000 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-07 08:43:10.000000 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/SOURCES.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-07 08:43:10.000000 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/dependency_links.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-07 08:43:10.000000 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/requires.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-07 08:43:10.000000 sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/top_level.txt
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 08:43:10.688086 sonnen-api-v2-0.3.5/tests/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.5/tests/__init__.py
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.5/tests/test_sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.6/LICENSE
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.6/README.md
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/setup.cfg
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.6/setup.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/sonnen_api_v2/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-07 12:35:16.000000 sonnen-api-v2-0.3.6/sonnen_api_v2/__init__.py
+-rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    16100 2023-04-07 12:35:16.000000 sonnen-api-v2-0.3.6/sonnen_api_v2/sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-07 12:35:22.000000 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-07 12:35:22.000000 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/SOURCES.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-07 12:35:22.000000 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/dependency_links.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-07 12:35:22.000000 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/requires.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-07 12:35:22.000000 sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/top_level.txt
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-07 12:35:22.828856 sonnen-api-v2-0.3.6/tests/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.6/tests/__init__.py
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.6/tests/test_sonnen.py
```

### Comparing `sonnen-api-v2-0.3.5/LICENSE` & `sonnen-api-v2-0.3.6/LICENSE`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.5/PKG-INFO` & `sonnen-api-v2-0.3.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.5
+Version: 0.3.6
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.5/setup.py` & `sonnen-api-v2-0.3.6/setup.py`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.5/sonnen_api_v2/sonnen.py` & `sonnen-api-v2-0.3.6/sonnen_api_v2/sonnen.py`

 * *Files 0% similar despite different names*

```diff
@@ -136,15 +136,15 @@
             self._log_error(f'Battery: {self.ip_address} is offline!')
         except asyncio.TimeoutError as error:
             self._log_error(f'Timeout error while accessing: {url}')
 
         try:
             return await response.json()
         except Exception as error:
-            self._log_error('Error while data parsing')
+            self._log_error(f'Error while data parsing {error}')
             return {}
 
     async def async_fetch_latest_details(self) -> bool:
         """Fetches latest details api as coroutine"""
         try:
             self._latest_details_data = await self._async_fetch_data(
                 self.latest_details_api_endpoint
```

### Comparing `sonnen-api-v2-0.3.5/sonnen_api_v2.egg-info/PKG-INFO` & `sonnen-api-v2-0.3.6/sonnen_api_v2.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.5
+Version: 0.3.6
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.5/tests/test_sonnen.py` & `sonnen-api-v2-0.3.6/tests/test_sonnen.py`

 * *Files identical despite different names*

