# Comparing `tmp/python_hilo-2023.3.1.tar.gz` & `tmp/python_hilo-2023.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python_hilo-2023.3.1.tar", max compression
+gzip compressed data, was "python_hilo-2023.4.1.tar", max compression
```

## Comparing `python_hilo-2023.3.1.tar` & `python_hilo-2023.4.1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1082 2023-02-20 01:13:28.118104 python_hilo-2023.3.1/LICENSE
--rw-r--r--   0        0        0     1124 2023-02-20 01:13:28.118273 python_hilo-2023.3.1/README.md
--rw-r--r--   0        0        0      109 2022-03-03 03:33:56.401543 python_hilo-2023.3.1/pyhilo/__init__.py
--rw-r--r--   0        0        0    28825 2023-03-06 23:53:51.346014 python_hilo-2023.3.1/pyhilo/api.py
--rw-r--r--   0        0        0     6957 2023-02-20 01:13:28.119101 python_hilo-2023.3.1/pyhilo/const.py
--rw-r--r--   0        0        0     9103 2022-03-03 03:33:56.402025 python_hilo-2023.3.1/pyhilo/device/__init__.py
--rw-r--r--   0        0        0     1287 2023-02-20 01:13:28.119444 python_hilo-2023.3.1/pyhilo/device/climate.py
--rw-r--r--   0        0        0      930 2023-02-20 01:13:28.119569 python_hilo-2023.3.1/pyhilo/device/light.py
--rw-r--r--   0        0        0      446 2022-03-03 03:33:56.402237 python_hilo-2023.3.1/pyhilo/device/sensor.py
--rw-r--r--   0        0        0      438 2022-03-03 03:33:56.402304 python_hilo-2023.3.1/pyhilo/device/switch.py
--rw-r--r--   0        0        0     3255 2022-03-03 03:33:56.402394 python_hilo-2023.3.1/pyhilo/devices.py
--rw-r--r--   0        0        0     4013 2022-03-03 03:33:56.402480 python_hilo-2023.3.1/pyhilo/event.py
--rw-r--r--   0        0        0     1191 2022-03-03 03:33:56.402554 python_hilo-2023.3.1/pyhilo/exceptions.py
--rw-r--r--   0        0        0     1257 2022-03-03 03:33:56.402675 python_hilo-2023.3.1/pyhilo/util/__init__.py
--rw-r--r--   0        0        0     2988 2023-02-20 01:13:28.119721 python_hilo-2023.3.1/pyhilo/util/state.py
--rw-r--r--   0        0        0    13003 2023-02-20 01:13:28.119881 python_hilo-2023.3.1/pyhilo/websocket.py
--rw-r--r--   0        0        0     3151 2023-03-06 23:54:24.894130 python_hilo-2023.3.1/pyproject.toml
--rw-r--r--   0        0        0     2529 1970-01-01 00:00:00.000000 python_hilo-2023.3.1/PKG-INFO
+-rw-r--r--   0        0        0     1082 2023-02-20 01:13:28.118104 python_hilo-2023.4.1/LICENSE
+-rw-r--r--   0        0        0     1124 2023-02-20 01:13:28.118273 python_hilo-2023.4.1/README.md
+-rw-r--r--   0        0        0      109 2022-03-03 03:33:56.401543 python_hilo-2023.4.1/pyhilo/__init__.py
+-rw-r--r--   0        0        0    28825 2023-03-06 23:53:51.346014 python_hilo-2023.4.1/pyhilo/api.py
+-rw-r--r--   0        0        0     6957 2023-04-07 15:00:18.615552 python_hilo-2023.4.1/pyhilo/const.py
+-rw-r--r--   0        0        0     9103 2022-03-03 03:33:56.402025 python_hilo-2023.4.1/pyhilo/device/__init__.py
+-rw-r--r--   0        0        0     1287 2023-02-20 01:13:28.119444 python_hilo-2023.4.1/pyhilo/device/climate.py
+-rw-r--r--   0        0        0      930 2023-02-20 01:13:28.119569 python_hilo-2023.4.1/pyhilo/device/light.py
+-rw-r--r--   0        0        0      446 2022-03-03 03:33:56.402237 python_hilo-2023.4.1/pyhilo/device/sensor.py
+-rw-r--r--   0        0        0      438 2022-03-03 03:33:56.402304 python_hilo-2023.4.1/pyhilo/device/switch.py
+-rw-r--r--   0        0        0     3824 2023-04-07 15:00:18.615734 python_hilo-2023.4.1/pyhilo/devices.py
+-rw-r--r--   0        0        0     4013 2022-03-03 03:33:56.402480 python_hilo-2023.4.1/pyhilo/event.py
+-rw-r--r--   0        0        0     1191 2022-03-03 03:33:56.402554 python_hilo-2023.4.1/pyhilo/exceptions.py
+-rw-r--r--   0        0        0     1257 2022-03-03 03:33:56.402675 python_hilo-2023.4.1/pyhilo/util/__init__.py
+-rw-r--r--   0        0        0     2988 2023-02-20 01:13:28.119721 python_hilo-2023.4.1/pyhilo/util/state.py
+-rw-r--r--   0        0        0    13003 2023-02-20 01:13:28.119881 python_hilo-2023.4.1/pyhilo/websocket.py
+-rw-r--r--   0        0        0     3151 2023-04-07 15:00:46.570201 python_hilo-2023.4.1/pyproject.toml
+-rw-r--r--   0        0        0     2529 1970-01-01 00:00:00.000000 python_hilo-2023.4.1/PKG-INFO
```

### Comparing `python_hilo-2023.3.1/LICENSE` & `python_hilo-2023.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/README.md` & `python_hilo-2023.4.1/README.md`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/api.py` & `python_hilo-2023.4.1/pyhilo/api.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/const.py` & `python_hilo-2023.4.1/pyhilo/const.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import logging
 import platform
+from typing import Final
+
 import aiohttp
 import homeassistant.core
-from typing import Final
 
 LOG: Final = logging.getLogger(__package__)
 DEFAULT_STATE_FILE: Final = "hilo_state.yaml"
 REQUEST_RETRY: Final = 9
 TIMEOUT: Final = 10
 TOKEN_EXPIRATION_PADDING: Final = 300
 VERIFY: Final = True
@@ -25,15 +26,15 @@
 AUTH_TYPE_PASSWORD: Final = "password"
 AUTH_TYPE_REFRESH: Final = "refresh_token"
 AUTH_RESPONSE_TYPE: Final = "token id_token"
 AUTH_SCOPE: Final = "openid 9870f087-25f8-43b6-9cad-d4b74ce512e1 offline_access"
 SUBSCRIPTION_KEY: Final = "20eeaedcb86945afa3fe792cea89b8bf"
 
 # API constants
-API_HOSTNAME: Final = "apim.hiloenergie.com"
+API_HOSTNAME: Final = "api.hiloenergie.com"
 API_END: Final = "v1/api"
 API_AUTOMATION_ENDPOINT: Final = f"/Automation/{API_END}"
 API_GD_SERVICE_ENDPOINT: Final = f"/GDService/{API_END}"
 API_NOTIFICATIONS_ENDPOINT: Final = "/Notifications"
 API_EVENTS_ENDPOINT: Final = "/Events"
 API_REGISTRATION_ENDPOINT: Final = f"{API_NOTIFICATIONS_ENDPOINT}/Registrations"
```

### Comparing `python_hilo-2023.3.1/pyhilo/device/__init__.py` & `python_hilo-2023.4.1/pyhilo/device/__init__.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/device/climate.py` & `python_hilo-2023.4.1/pyhilo/device/climate.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/device/light.py` & `python_hilo-2023.4.1/pyhilo/device/light.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/devices.py` & `python_hilo-2023.4.1/pyhilo/devices.py`

 * *Files 15% similar despite different names*

```diff
@@ -74,18 +74,31 @@
         except KeyError:
             LOG.warning(f"Unknown device type {dev.type}, adding as Sensor")
             device_type = "Sensor"
         dev.__class__ = globals()[device_type]
         return dev
 
     async def update(self) -> None:
-        for device in await self._api.get_devices(self.location_id):
+        fresh_devices = await self._api.get_devices(self.location_id)
+        generated_devices = []
+        for device in fresh_devices:
             LOG.debug(f"Generating device {device}")
             dev = self.generate_device(device)
+            generated_devices.append(dev)
             if dev not in self.devices:
                 self.devices.append(dev)
+        for device in self.devices:
+            if device not in generated_devices:
+                LOG.debug(f"Device unpaired {device}")
+                # Don't do anything with unpaired device for now.
+                # self.devices.remove(device)
+
+    async def update_gateway(self) -> None:
+        gateway = await self._api.get_gateway(self.location_id)
+        LOG.debug(f"Generating device (gateway) {gateway}")
+        self.generate_device(gateway)
 
     async def async_init(self) -> None:
         """Initialize the Hilo "manager" class."""
         LOG.info("Initialising after websocket is connected")
         self.location_id = await self._api.get_location_id()
         await self.update()
```

### Comparing `python_hilo-2023.3.1/pyhilo/event.py` & `python_hilo-2023.4.1/pyhilo/event.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/exceptions.py` & `python_hilo-2023.4.1/pyhilo/exceptions.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/util/__init__.py` & `python_hilo-2023.4.1/pyhilo/util/__init__.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/util/state.py` & `python_hilo-2023.4.1/pyhilo/util/state.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyhilo/websocket.py` & `python_hilo-2023.4.1/pyhilo/websocket.py`

 * *Files identical despite different names*

### Comparing `python_hilo-2023.3.1/pyproject.toml` & `python_hilo-2023.4.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -36,15 +36,15 @@
 warn_unreachable = true
 warn_unused_configs = true
 warn_unused_ignores = true
 exclude = ".venv/.*"
 
 [tool.poetry]
 name = "python-hilo"
-version = "2023.03.01"
+version = "2023.04.01"
 description = "A Python3, async interface to the Hilo API"
 readme = "README.md"
 authors = ["David Vallee Delisle <me@dvd.dev>"]
 maintainers = ["David Vallee Delisle <me@dvd.dev>"]
 license = "MIT"
 repository = "https://github.com/dvd-dev/python-hilo"
 packages = [
@@ -77,15 +77,15 @@
 [tool.poetry.dev-dependencies]
 Sphinx = "^5.3.0"
 aresponses = "^2.1.4"
 asynctest = "^0.13.0"
 pre-commit = "^2.0.1"
 pytest = "^7.2.0"
 pytest-aiohttp = "^1.0.4"
-pytest-cov = "^3.0.0"
+pytest-cov = "^4.0.0"
 sphinx-rtd-theme = "^1.0.0"
 types-pytz = "^2022.7.0"
 
 [tool.pylint.BASIC]
 expected-line-ending-format = "LF"
 
 [tool.pylint."MESSAGES CONTROL"]
```

### Comparing `python_hilo-2023.3.1/PKG-INFO` & `python_hilo-2023.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-hilo
-Version: 2023.3.1
+Version: 2023.4.1
 Summary: A Python3, async interface to the Hilo API
 Home-page: https://github.com/dvd-dev/python-hilo
 License: MIT
 Author: David Vallee Delisle
 Author-email: me@dvd.dev
 Maintainer: David Vallee Delisle
 Maintainer-email: me@dvd.dev
```

