# Comparing `tmp/sonnen-api-v2-0.3.3.tar.gz` & `tmp/sonnen-api-v2-0.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sonnen-api-v2-0.3.3.tar", last modified: Wed Apr  5 09:18:04 2023, max compression
+gzip compressed data, was "sonnen-api-v2-0.3.4.tar", last modified: Thu Apr  6 16:05:26 2023, max compression
```

## Comparing `sonnen-api-v2-0.3.3.tar` & `sonnen-api-v2-0.3.4.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/LICENSE
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/README.md
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/setup.cfg
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.3/setup.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/sonnen_api_v2/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-05 09:10:07.000000 sonnen-api-v2-0.3.3/sonnen_api_v2/__init__.py
--rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    15967 2023-04-04 08:48:06.000000 sonnen-api-v2-0.3.3/sonnen_api_v2/sonnen.py
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/PKG-INFO
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/SOURCES.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/dependency_links.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/requires.txt
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-05 09:18:04.000000 sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/top_level.txt
-drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-05 09:18:04.205107 sonnen-api-v2-0.3.3/tests/
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/tests/__init__.py
--rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.3/tests/test_sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1070 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.4/LICENSE
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       46 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.4/README.md
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       79 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/setup.cfg
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      920 2023-04-04 08:51:51.000000 sonnen-api-v2-0.3.4/setup.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/sonnen_api_v2/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       80 2023-04-06 16:05:23.000000 sonnen-api-v2-0.3.4/sonnen_api_v2/__init__.py
+-rwxr-xr-x   0 vaclav    (1000) vaclav    (1000)    16113 2023-04-06 16:00:47.000000 sonnen-api-v2-0.3.4/sonnen_api_v2/sonnen.py
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)     1464 2023-04-06 16:05:26.000000 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/PKG-INFO
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      309 2023-04-06 16:05:26.000000 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/SOURCES.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)        1 2023-04-06 16:05:26.000000 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/dependency_links.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       32 2023-04-06 16:05:26.000000 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/requires.txt
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)       20 2023-04-06 16:05:26.000000 sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/top_level.txt
+drwxr-xr-x   0 vaclav    (1000) vaclav    (1000)        0 2023-04-06 16:05:26.982996 sonnen-api-v2-0.3.4/tests/
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)      125 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.4/tests/__init__.py
+-rw-r--r--   0 vaclav    (1000) vaclav    (1000)    23950 2023-03-18 16:25:33.000000 sonnen-api-v2-0.3.4/tests/test_sonnen.py
```

### Comparing `sonnen-api-v2-0.3.3/LICENSE` & `sonnen-api-v2-0.3.4/LICENSE`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.3/PKG-INFO` & `sonnen-api-v2-0.3.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.3
+Version: 0.3.4
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.3/setup.py` & `sonnen-api-v2-0.3.4/setup.py`

 * *Files identical despite different names*

### Comparing `sonnen-api-v2-0.3.3/sonnen_api_v2/sonnen.py` & `sonnen-api-v2-0.3.4/sonnen_api_v2/sonnen.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,15 +53,15 @@
     BATTERY_MIN_MODULE_CURRENT = 'minimummodulecurrent'
     BATTERY_MIN_MODULE_VOLTAGE = 'minimummoduledcvoltage'
     BATTERY_MIN_MODULE_TEMP = 'minimummoduletemperature'
     BATTERY_RSOC = 'relativestateofcharge'
     BATTERY_REMAINING_CAPACITY = 'remainingcapacity'
     BATTERY_SYSTEM_CURRENT = 'systemcurrent'
     BATTERY_SYSTEM_VOLTAGE = 'systemdcvoltage'
-
+    SYSTEM_STATUS = 'statecorecontrolmodule'
     # default timeout
     TIMEOUT = aiohttp.ClientTimeout(total=5)
 
     def __init__(self, auth_token: str,
                  ip_address: str,
                  logger: logging.Logger = None) -> None:
         self._last_updated = None
@@ -257,14 +257,18 @@
         """Battery modules installed in the system
             Returns:
                 Number of modules
         """
         return self._ic_status[self.MODULES_INSTALLED_KEY]
 
     @get_item
+    def system_status(self) -> str:
+        return self._ic_status[self.SYSTEM_STATUS]
+
+    @get_item
     def u_soc(self) -> int:
         """User state of charge
             Returns:
                 User SoC in percent
         """
         return self._latest_details_data[self.USOC_KEY]
```

### Comparing `sonnen-api-v2-0.3.3/sonnen_api_v2.egg-info/PKG-INFO` & `sonnen-api-v2-0.3.4/sonnen_api_v2.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sonnen-api-v2
-Version: 0.3.3
+Version: 0.3.4
 Summary: # Sonnen API v2
 Home-page: https://github.com/Katamave/sonnen_api_v2.git
 Author: Vaclav Silhan
 Author-email: katamave@gmail.com
 License: MIT License
         
         Copyright (c) 2022 Vaclav Silhan
```

### Comparing `sonnen-api-v2-0.3.3/tests/test_sonnen.py` & `sonnen-api-v2-0.3.4/tests/test_sonnen.py`

 * *Files identical despite different names*

