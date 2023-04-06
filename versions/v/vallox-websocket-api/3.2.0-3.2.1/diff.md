# Comparing `tmp/vallox_websocket_api-3.2.0.tar.gz` & `tmp/vallox_websocket_api-3.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vallox_websocket_api-3.2.0.tar", last modified: Thu Apr  6 18:52:58 2023, max compression
+gzip compressed data, was "vallox_websocket_api-3.2.1.tar", last modified: Thu Apr  6 20:19:21 2023, max compression
```

## Comparing `vallox_websocket_api-3.2.0.tar` & `vallox_websocket_api-3.2.1.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)     7651 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    33640 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    32687 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      542 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     6173 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_client.py
--rw-r--r--   0 runner    (1001) docker     (123)      867 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_fetch_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4336 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_messages.py
--rw-r--r--   0 runner    (1001) docker     (123)      779 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_set_temperature.py
--rw-r--r--   0 runner    (1001) docker     (123)     1689 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_vallox_fan_speed.py
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_vallox_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_vallox_next_filter_change.py
--rw-r--r--   0 runner    (1001) docker     (123)     5312 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_vallox_profile.py
--rw-r--r--   0 runner    (1001) docker     (123)     4391 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/tests/test_vallox_temperatures.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/vallox_websocket_api/
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11360 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/client.py
--rw-r--r--   0 runner    (1001) docker     (123)    71638 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2479 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/messages.py
--rw-r--r--   0 runner    (1001) docker     (123)     9933 2023-04-06 18:52:47.000000 vallox_websocket_api-3.2.0/vallox_websocket_api/vallox.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:52:58.207112 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    33640 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:52:58.000000 vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:19:21.174334 vallox_websocket_api-3.2.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     7651 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    33640 2023-04-06 20:19:21.174334 vallox_websocket_api-3.2.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    32687 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      542 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 20:19:21.178334 vallox_websocket_api-3.2.1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:19:21.174334 vallox_websocket_api-3.2.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     6173 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      867 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_fetch_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4336 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_messages.py
+-rw-r--r--   0 runner    (1001) docker     (123)      779 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_set_temperature.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1689 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_vallox_fan_speed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_vallox_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_vallox_next_filter_change.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5312 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_vallox_profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4391 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/tests/test_vallox_temperatures.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:19:21.174334 vallox_websocket_api-3.2.1/vallox_websocket_api/
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11360 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    71638 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2479 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/messages.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9933 2023-04-06 20:19:08.000000 vallox_websocket_api-3.2.1/vallox_websocket_api/vallox.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:19:21.174334 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    33640 2023-04-06 20:19:21.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-04-06 20:19:21.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:19:21.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       46 2023-04-06 20:19:21.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-06 20:19:21.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:19:20.000000 vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/zip-safe
```

### Comparing `vallox_websocket_api-3.2.0/LICENSE.txt` & `vallox_websocket_api-3.2.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/PKG-INFO` & `vallox_websocket_api-3.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vallox_websocket_api
-Version: 3.2.0
+Version: 3.2.1
 Summary: Vallox WebSocket API
 Home-page: https://github.com/yozik04/vallox_websocket_api
 Author: Jevgeni Kiski
 Author-email: yozik04@gmail.com
 License: LGPL 3
 Project-URL: Bug Tracker, https://github.com/yozik04/vallox_websocket_api/issues
 Keywords: vallox api
```

### Comparing `vallox_websocket_api-3.2.0/README.md` & `vallox_websocket_api-3.2.1/README.md`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/pyproject.toml` & `vallox_websocket_api-3.2.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/setup.cfg` & `vallox_websocket_api-3.2.1/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
 [options]
 zip_safe = True
 include_package_data = True
 packages = 
 	vallox_websocket_api
 python_requires = >=3.6.0, <4
 install_requires = 
-	websockets >= 11.0.1, < 12.0
+	websockets >= 9.1, < 12.0
 	construct >= 2.9.0, < 3.0.0
 tests_require = 
 	pytest
 	pytest-asyncio
 
 [flake8]
 exclude = .venv,.git,.tox,docs,venv,bin,lib,deps,build
```

### Comparing `vallox_websocket_api-3.2.0/tests/test_client.py` & `vallox_websocket_api-3.2.1/tests/test_client.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_fetch_logs.py` & `vallox_websocket_api-3.2.1/tests/test_fetch_logs.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_messages.py` & `vallox_websocket_api-3.2.1/tests/test_messages.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_set_temperature.py` & `vallox_websocket_api-3.2.1/tests/test_set_temperature.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_vallox_fan_speed.py` & `vallox_websocket_api-3.2.1/tests/test_vallox_fan_speed.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_vallox_info.py` & `vallox_websocket_api-3.2.1/tests/test_vallox_info.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_vallox_next_filter_change.py` & `vallox_websocket_api-3.2.1/tests/test_vallox_next_filter_change.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_vallox_profile.py` & `vallox_websocket_api-3.2.1/tests/test_vallox_profile.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/tests/test_vallox_temperatures.py` & `vallox_websocket_api-3.2.1/tests/test_vallox_temperatures.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api/__init__.py` & `vallox_websocket_api-3.2.1/vallox_websocket_api/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,8 +20,8 @@
     "PROFILE_TO_SET_TEMPERATURE_METRIC_MAP",
     "ValloxException",
     "ValloxInvalidInputException",
     "ValloxApiException",
     "ValloxWebsocketException",
 ]
 
-__version__ = "3.2.0"
+__version__ = "3.2.1"
```

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api/client.py` & `vallox_websocket_api-3.2.1/vallox_websocket_api/client.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api/constants.py` & `vallox_websocket_api-3.2.1/vallox_websocket_api/constants.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api/messages.py` & `vallox_websocket_api-3.2.1/vallox_websocket_api/messages.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api/vallox.py` & `vallox_websocket_api-3.2.1/vallox_websocket_api/vallox.py`

 * *Files identical despite different names*

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/PKG-INFO` & `vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vallox-websocket-api
-Version: 3.2.0
+Version: 3.2.1
 Summary: Vallox WebSocket API
 Home-page: https://github.com/yozik04/vallox_websocket_api
 Author: Jevgeni Kiski
 Author-email: yozik04@gmail.com
 License: LGPL 3
 Project-URL: Bug Tracker, https://github.com/yozik04/vallox_websocket_api/issues
 Keywords: vallox api
```

### Comparing `vallox_websocket_api-3.2.0/vallox_websocket_api.egg-info/SOURCES.txt` & `vallox_websocket_api-3.2.1/vallox_websocket_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

