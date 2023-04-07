# Comparing `tmp/idun_guardian_client-1.1.0.tar.gz` & `tmp/idun_guardian_client-1.1b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "idun_guardian_client-1.1.0.tar", last modified: Fri Mar 31 15:18:24 2023, max compression
+gzip compressed data, was "idun_guardian_client-1.1b1.tar", last modified: Fri Apr  7 12:31:33 2023, max compression
```

## Comparing `idun_guardian_client-1.1.0.tar` & `idun_guardian_client-1.1b1.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-03-31 15:18:24.367241 idun_guardian_client-1.1.0/
--rw-r--r--   0 waddaben   (501) staff       (20)     8729 2023-03-31 15:18:24.367050 idun_guardian_client-1.1.0/PKG-INFO
--rw-r--r--   0 waddaben   (501) staff       (20)     8164 2023-03-31 15:17:31.000000 idun_guardian_client-1.1.0/README.md
--rw-r--r--   0 waddaben   (501) staff       (20)      864 2023-03-31 15:17:31.000000 idun_guardian_client-1.1.0/pyproject.toml
--rw-r--r--   0 waddaben   (501) staff       (20)       38 2023-03-31 15:18:24.367291 idun_guardian_client-1.1.0/setup.cfg
-drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-03-31 15:18:24.360311 idun_guardian_client-1.1.0/src/
-drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-03-31 15:18:24.364552 idun_guardian_client-1.1.0/src/idun_guardian_client/
--rw-r--r--   0 waddaben   (501) staff       (20)      339 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/__init__.py
--rw-r--r--   0 waddaben   (501) staff       (20)        0 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/__main__.py
--rw-r--r--   0 waddaben   (501) staff       (20)     7083 2023-03-31 15:17:31.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/client.py
--rw-r--r--   0 waddaben   (501) staff       (20)     1797 2023-03-31 15:17:57.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/config.py
--rw-r--r--   0 waddaben   (501) staff       (20)    10983 2023-03-31 15:17:31.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/debug_logs.py
--rw-r--r--   0 waddaben   (501) staff       (20)    18295 2023-03-31 15:17:31.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_api.py
--rw-r--r--   0 waddaben   (501) staff       (20)    31934 2023-03-31 13:04:07.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_bluetooth.py
--rw-r--r--   0 waddaben   (501) staff       (20)     2846 2023-03-24 14:56:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_utils.py
--rw-r--r--   0 waddaben   (501) staff       (20)      191 2023-03-24 14:56:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/mock_utils.py
--rw-r--r--   0 waddaben   (501) staff       (20)      164 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/setup.py
--rw-r--r--   0 waddaben   (501) staff       (20)     1214 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/src/idun_guardian_client/test_producer_consumer.py
-drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-03-31 15:18:24.365743 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/
--rw-r--r--   0 waddaben   (501) staff       (20)     8729 2023-03-31 15:18:24.000000 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/PKG-INFO
--rw-r--r--   0 waddaben   (501) staff       (20)      752 2023-03-31 15:18:24.000000 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/SOURCES.txt
--rw-r--r--   0 waddaben   (501) staff       (20)        1 2023-03-31 15:18:24.000000 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/dependency_links.txt
--rw-r--r--   0 waddaben   (501) staff       (20)      137 2023-03-31 15:18:24.000000 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/requires.txt
--rw-r--r--   0 waddaben   (501) staff       (20)       21 2023-03-31 15:18:24.000000 idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/top_level.txt
-drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-03-31 15:18:24.366719 idun_guardian_client-1.1.0/tests/
--rw-r--r--   0 waddaben   (501) staff       (20)     1940 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/tests/test_ble.py
--rw-r--r--   0 waddaben   (501) staff       (20)     1672 2023-03-24 12:33:16.000000 idun_guardian_client-1.1.0/tests/test_ble_record.py
--rw-r--r--   0 waddaben   (501) staff       (20)     1106 2023-03-22 08:37:21.000000 idun_guardian_client-1.1.0/tests/test_utils.py
+drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-04-07 12:31:33.241931 idun_guardian_client-1.1b1/
+-rw-r--r--   0 waddaben   (501) staff       (20)     8728 2023-04-07 12:31:33.241670 idun_guardian_client-1.1b1/PKG-INFO
+-rw-r--r--   0 waddaben   (501) staff       (20)     8163 2023-04-07 09:22:23.000000 idun_guardian_client-1.1b1/README.md
+-rw-r--r--   0 waddaben   (501) staff       (20)      869 2023-04-07 12:30:57.000000 idun_guardian_client-1.1b1/pyproject.toml
+-rw-r--r--   0 waddaben   (501) staff       (20)       38 2023-04-07 12:31:33.241987 idun_guardian_client-1.1b1/setup.cfg
+drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-04-07 12:31:33.234346 idun_guardian_client-1.1b1/src/
+drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-04-07 12:31:33.239248 idun_guardian_client-1.1b1/src/idun_guardian_client/
+-rw-r--r--   0 waddaben   (501) staff       (20)      339 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/__init__.py
+-rw-r--r--   0 waddaben   (501) staff       (20)        0 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/__main__.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     7083 2023-04-07 11:46:40.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/client.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     1797 2023-04-07 12:29:46.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/config.py
+-rw-r--r--   0 waddaben   (501) staff       (20)    11341 2023-04-07 11:46:38.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/debug_logs.py
+-rw-r--r--   0 waddaben   (501) staff       (20)    19332 2023-04-07 12:28:00.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_api.py
+-rw-r--r--   0 waddaben   (501) staff       (20)    30743 2023-04-07 12:30:04.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_bluetooth.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     2846 2023-04-07 11:46:38.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_utils.py
+-rw-r--r--   0 waddaben   (501) staff       (20)      191 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/mock_utils.py
+-rw-r--r--   0 waddaben   (501) staff       (20)      164 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/setup.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     1214 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/src/idun_guardian_client/test_producer_consumer.py
+drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-04-07 12:31:33.240500 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/
+-rw-r--r--   0 waddaben   (501) staff       (20)     8728 2023-04-07 12:31:33.000000 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/PKG-INFO
+-rw-r--r--   0 waddaben   (501) staff       (20)      752 2023-04-07 12:31:33.000000 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/SOURCES.txt
+-rw-r--r--   0 waddaben   (501) staff       (20)        1 2023-04-07 12:31:33.000000 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/dependency_links.txt
+-rw-r--r--   0 waddaben   (501) staff       (20)      137 2023-04-07 12:31:33.000000 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/requires.txt
+-rw-r--r--   0 waddaben   (501) staff       (20)       21 2023-04-07 12:31:33.000000 idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/top_level.txt
+drwxr-xr-x   0 waddaben   (501) staff       (20)        0 2023-04-07 12:31:33.241330 idun_guardian_client-1.1b1/tests/
+-rw-r--r--   0 waddaben   (501) staff       (20)     1940 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/tests/test_ble.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     1672 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/tests/test_ble_record.py
+-rw-r--r--   0 waddaben   (501) staff       (20)     1106 2023-04-06 15:19:16.000000 idun_guardian_client-1.1b1/tests/test_utils.py
```

### Comparing `idun_guardian_client-1.1.0/PKG-INFO` & `idun_guardian_client-1.1b1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: idun_guardian_client
-Version: 1.1.0
+Version: 1.1b1
 Summary: Python SDK for communication with the IDUN Guardian earbuds and IDUN cloud
 Author-email: IDUN Technologies <contact@iduntechnologies.com>
 Classifier: Development Status :: 1 - Planning
 Classifier: License :: Other/Proprietary License
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.10
@@ -254,11 +254,11 @@
 from idun_guardian_client.igeb_api import GuardianAPI
 
 api = GuardianAPI()
 
 # download recording
 api.download_recording_by_id(
     device_id = "XX-XX-XX-XX-XX-XX",
-    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
+    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
 )
 # The info about th recording can be found in the log file
 ```
```

### Comparing `idun_guardian_client-1.1.0/README.md` & `idun_guardian_client-1.1b1/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -240,11 +240,11 @@
 from idun_guardian_client.igeb_api import GuardianAPI
 
 api = GuardianAPI()
 
 # download recording
 api.download_recording_by_id(
     device_id = "XX-XX-XX-XX-XX-XX",
-    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
+    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
 )
 # The info about th recording can be found in the log file
 ```
```

### Comparing `idun_guardian_client-1.1.0/pyproject.toml` & `idun_guardian_client-1.1b1/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "idun_guardian_client"
-version = "1.1.0"
+version = "1.1.beta.1"
 authors = [
   { name="IDUN Technologies", email="contact@iduntechnologies.com" },
 ]
 description = "Python SDK for communication with the IDUN Guardian earbuds and IDUN cloud"
 readme = "README.md"
 requires-python = ">=3.10"
```

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/client.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/client.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/config.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/config.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/debug_logs.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/debug_logs.py`

 * *Files 2% similar despite different names*

```diff
@@ -78,22 +78,38 @@
     if debug:
         logging.info("[API]: Data queue is not empty, waiting for last timestamp")
 
 
 def log_interrupt_error(error, debug):
     if debug:
         logging.info(
-            "[API]: Interuption in sending data to the cloud: %s",
+            "[API]: Interuption in sending or receiving data to the cloud: %s",
+            error,
+        )
+
+
+def log_error_in_sending_stop(error, debug):
+    if debug:
+        logging.info(
+            "[API]: Error in sending stop signal to the cloud: %s",
+            error,
+        )
+
+
+def log_error_in_sending_stop_ble(error, debug):
+    if debug:
+        logging.info(
+            "[BLE]: Error in loading stop signal to the cloud: %s",
             error,
         )
 
 
 def logging_connection_closed(debug):
     if debug:
-        logging.info("[API]: Websocket client connection closed or asyncio Timeout")
+        logging.info("[API]: Websocket client connection closed")
 
 
 def logging_reconnection(debug):
     if debug:
         logging.info("[API]: Ping successful, connection alive and continue..")
         logging.info("Try to ping websocket successful")
```

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_api.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_api.py`

 * *Files 7% similar despite different names*

```diff
@@ -7,41 +7,28 @@
 import socket
 import datetime
 import asyncio
 from typing import Union
 import requests
 import websockets
 import time
+from typing import Optional
 from dotenv import load_dotenv
 
 from .config import settings
 from .igeb_utils import unpack_from_queue
 from .mock_utils import mock_cloud_package
-from .debug_logs import (
-    log_first_message,
-    log_final_message,
-    logging_connection,
-    logging_break,
-    logging_empty,
-    logging_ping_error,
-    logging_not_empty,
-    log_interrupt_error,
-    logging_connection_closed,
-    logging_reconnection,
-    logging_cloud_termination,
-    logging_gaieerror,
-    logging_cancelled_error,
-    logging_connection_refused,
-    logging_api_completed,
-    logging_connecting_to_cloud,
-    logging_cloud_not_receiving,
-)
+from .debug_logs import *
+
 
 load_dotenv()
 
+FILTER_PACKAGE = "bp_filter_eeg"
+PACKAGE_RECEIPT = "SequenceNumber"
+
 
 class GuardianAPI:
     """Main Guardian API client."""
 
     def __init__(self, debug: bool = True) -> None:
         """Initialize Guardian API client.
 
@@ -65,17 +52,21 @@
         self.decrypted_data_queue: asyncio.Queue = asyncio.Queue(
             maxsize=self.decrypted_buffer_size
         )
         self.initial_receipt_timeout = 15
         self.runtime_receipt_timeout = 1
         self.current_timeout = self.initial_receipt_timeout
         self.initial_bi_directional_timeout = 15
-        self.runtime_bi_directional_timeout = 1
+        self.runtime_bi_directional_timeout = 4
+        self.sending_time_limit = 0.01
         self.bi_directional_timeout = self.initial_bi_directional_timeout
         self.last_saved_time = time.time()
+        self.connected = False
+        self.data_model = GuardianDataModel(None, None, None, None, None, False)
+        self.websocket: Optional[websockets.WebSocketClientProtocol] = None  # type: ignore
 
     async def connect_ws_api(
         self,
         data_queue: asyncio.Queue,
         device_id: str = "deviceMockID",
         recording_id: str = "dummy_recID",
         impedance_measurement: bool = False,
@@ -88,16 +79,30 @@
             recordingID (str, optional): Recording ID. Defaults to "dummy_recID".
 
         Raises:
             Exception: If the websocket connection fails
         """
 
         def reset_data_model():
-            data_model.payload = None
-            data_model.impedance = None
+            self.data_model.payload = None
+            self.data_model.impedance = None
+
+        async def pack_encrypted_queue():
+            if not self.encrypted_data_queue.full():
+                await self.encrypted_data_queue.put(
+                    [self.data_model.deviceTimestamp, self.data_model.payload]
+                )
+            else:
+                await self.encrypted_data_queue.get()
+
+        def pack_decrypted_queue(message):
+            if not self.decrypted_data_queue.full():
+                self.decrypted_data_queue.put_nowait(message[FILTER_PACKAGE])
+            else:
+                self.decrypted_data_queue.get_nowait()
 
         async def unpack_and_load_data():
             """Get data from the queue and pack it into a dataclass"""
             data_valid = False
             reset_data_model()
             package = await data_queue.get()
             (
@@ -106,30 +111,30 @@
                 data,
                 stop,
                 impedance,
             ) = unpack_from_queue(package)
 
             if data is not None:
                 if len(data) == self.base64string_len:
-                    data_model.payload = data
+                    self.data_model.payload = data
                     data_valid = True
 
             if impedance is not None:
                 if isinstance(impedance, int):
-                    data_model.impedance = impedance
+                    self.data_model.impedance = impedance
                     data_valid = True
 
             if device_timestamp is not None:
-                data_model.deviceTimestamp = device_timestamp
+                self.data_model.deviceTimestamp = device_timestamp
 
             if device_id is not None:
-                data_model.deviceID = device_id
+                self.data_model.deviceID = device_id
 
             if stop is not None:
-                data_model.stop = stop
+                self.data_model.stop = stop
                 if stop is True:
                     data_valid = True
 
             return data_valid
 
         async def create_timestamp(debug):
             """Create a timestamp for the data"""
@@ -143,155 +148,178 @@
                 )  # Fetch the timestamp from the BLE package
                 (device_timestamp, _, _, _, _) = unpack_from_queue(package)
             return device_timestamp
 
         async def unpack_and_load_data_termination():
             """Get data from the queue and pack it into a dataclass"""
             logging_cloud_termination(self.debug)
-            data_model.payload = "STOP_CANCELLED"
-            data_model.stop = True
+            self.data_model.payload = "STOP_CANCELLED"
+            self.data_model.stop = True
             device_timestamp = await create_timestamp(self.debug)
             if device_timestamp is not None:
-                data_model.deviceTimestamp = device_timestamp
+                self.data_model.deviceTimestamp = device_timestamp
 
-        async def send_messages(websocket, data_model):
+        async def send_messages():
             while True:
+                if not self.connected:
+                    break
                 if await unpack_and_load_data():
-                    await websocket.send(json.dumps(asdict(data_model)))
-                    if not self.encrypted_data_queue.full():
-                        await self.encrypted_data_queue.put(
-                            [data_model.deviceTimestamp, data_model.payload]
-                        )
-                    else:
-                        await self.encrypted_data_queue.get()
+                    await asyncio.shield(
+                        asyncio.sleep(self.sending_time_limit)
+                    )  # Wait as to not overload the cloud
+                    await asyncio.shield(
+                        self.websocket.send(json.dumps(asdict(self.data_model)))
+                    )
+                    await asyncio.shield(pack_encrypted_queue())
 
-                if data_model.stop:
+                if self.data_model.stop:
                     self.current_timeout = self.initial_receipt_timeout
                     break
 
-        async def receive_messages(websocket):
+        async def receive_messages():
             self.last_saved_time = time.time()
             while True:
 
-                message_str = await asyncio.wait_for(
-                    websocket.recv(), timeout=self.current_timeout
+                if not self.connected:
+                    break
+
+                message_str = await asyncio.shield(
+                    asyncio.wait_for(
+                        self.websocket.recv(), timeout=self.current_timeout
+                    )
                 )
 
-                if "bp_filter_eeg" in message_str:
+                if FILTER_PACKAGE in message_str:
                     self.bi_directional_timeout = self.runtime_bi_directional_timeout
                     message = json.loads(message_str)
                     self.last_saved_time = time.time()
-                    if not self.decrypted_data_queue.full():
-                        self.decrypted_data_queue.put_nowait(message["bp_filter_eeg"])
-                    else:
-                        self.decrypted_data_queue.get_nowait()
-                else:
+                    pack_decrypted_queue(message)
+
+                elif PACKAGE_RECEIPT in message_str:
                     self.current_timeout = self.runtime_receipt_timeout
                     if self.first_message_check:
                         self.first_message_check = False
                         log_first_message(
-                            data_model,
+                            self.data_model,
                             message_str,
                             self.debug,
                         )
-                    if data_model.stop:
+                    if self.data_model.stop:
                         log_final_message(
-                            data_model,
+                            self.data_model,
                             message_str,
                             self.debug,
                         )
                         self.final_message_check = True
                         break
 
-                time_without_data = time.time() - self.last_saved_time
-                if (
-                    time_without_data > self.bi_directional_timeout
-                    and not impedance_measurement
-                ):
-                    raise asyncio.TimeoutError
+                bi_directional_timeout(impedance_measurement)
 
-        # initiate flags
-        self.first_message_check = True
-        self.final_message_check = False
-        # Only when starting the code the first time do we want this to be the initial timeout
+        def bi_directional_timeout(impedance_measurement):
+            time_without_data = time.time() - self.last_saved_time
+            if (
+                time_without_data > self.bi_directional_timeout
+                and not impedance_measurement
+            ):
+                raise asyncio.TimeoutError
+
+        def once_initialise_variables():
+            # initiate flags
+            self.first_message_check = True
+            self.final_message_check = False
+            self.data_model = GuardianDataModel(
+                None, device_id, recording_id, None, None, False
+            )
+
+        def on_connection_initialise_variables():
+            self.first_message_check = True
+            self.connected = True
+            self.bi_directional_timeout = self.initial_bi_directional_timeout
+            self.current_timeout = self.initial_receipt_timeout
 
-        # initiate data model
-        data_model = GuardianDataModel(None, device_id, recording_id, None, None, False)
+        async def handle_cancelled_error(error):
+            while True:
+                try:
+                    async with websockets.connect(  # type: ignore
+                        settings.WS_IDENTIFIER
+                    ) as self.websocket:
+                        logging_cancelled_error(error, self.debug)
+                        await unpack_and_load_data_termination()
+                        await self.websocket.send(json.dumps(asdict(self.data_model)))
+                        package_receipt = await self.websocket.recv()
+                        log_final_message(
+                            self.data_model,
+                            package_receipt,
+                            self.debug,
+                        )
+                        self.final_message_check = True
+                        break
+                except Exception as error:
+                    await asyncio.sleep(self.ping_timeout)
+                    log_error_in_sending_stop(error, self.debug)
+                    continue
+
+        once_initialise_variables()
 
         while True:
             logging_connecting_to_cloud(self.debug)
             try:
-                async with websockets.connect(settings.WS_IDENTIFIER) as websocket:  # type: ignore
+                async with websockets.connect(settings.WS_IDENTIFIER) as self.websocket:  # type: ignore
                     try:
-                        self.first_message_check = True
+                        on_connection_initialise_variables()
                         # for the websocket we want to increase to initial timeout each time
-                        self.bi_directional_timeout = (
-                            self.initial_bi_directional_timeout
-                        )
-                        self.current_timeout = self.initial_receipt_timeout
-
                         logging_connection(settings.WS_IDENTIFIER, self.debug)
-                        send_task = asyncio.create_task(
-                            send_messages(websocket, data_model)
-                        )
-                        receive_task = asyncio.create_task(receive_messages(websocket))
+                        send_task = asyncio.create_task(send_messages())
+                        receive_task = asyncio.create_task(receive_messages())
                         await asyncio.gather(send_task, receive_task)
 
                     except (
-                        asyncio.TimeoutError,
                         websockets.exceptions.ConnectionClosed,  # type: ignore
                     ) as error:
-                        log_interrupt_error(error, self.debug)
                         try:
-                            # Wait for the ping timeout before trying to reconnect
-                            # If it is the bi-directional timeout, then we want to
-                            # wait a bit even though we can still send data
-                            await asyncio.sleep(self.ping_timeout)
                             logging_connection_closed(self.debug)
-                            pong = await websocket.ping()
-                            # If the bi-directional timeout is reached, then we
-                            # we will get a pong immediately, if it is the
-                            await asyncio.wait_for(pong, timeout=self.ping_timeout)
+                            self.connected = False
+                            await asyncio.shield(asyncio.sleep(self.ping_timeout))
                             logging_reconnection(self.debug)
                             self.bi_directional_timeout = (
                                 self.initial_bi_directional_timeout
                             )
                             continue
-                        except Exception as error:
-                            logging_ping_error(error, self.ping_timeout, self.debug)
-                            await asyncio.sleep(self.ping_timeout)
+                        except asyncio.CancelledError as error:
+                            await handle_cancelled_error(error)
 
-                    except asyncio.CancelledError as error:
-                        async with websockets.connect(  # type: ignore
-                            settings.WS_IDENTIFIER
-                        ) as websocket:
-                            logging_cancelled_error(error, self.debug)
-                            await unpack_and_load_data_termination()
-
-                            await websocket.send(json.dumps(asdict(data_model)))
-                            package_receipt = await websocket.recv()
-
-                            log_final_message(
-                                data_model,
-                                package_receipt,
-                                self.debug,
+                    except (asyncio.TimeoutError) as error:
+                        try:
+                            log_interrupt_error(error, self.debug)
+                            self.connected = False
+                            await asyncio.shield(asyncio.sleep(self.ping_timeout))
+                            logging_reconnection(self.debug)
+                            self.bi_directional_timeout = (
+                                self.initial_bi_directional_timeout
                             )
-                            self.final_message_check = True
-                            break
+                            continue
+                        except asyncio.CancelledError as error:
+                            await handle_cancelled_error(error)
+
+                    except asyncio.CancelledError as error:
+                        await handle_cancelled_error(error)
 
             except socket.gaierror as error:
                 logging_gaieerror(error, self.retry_time, self.debug)
                 await asyncio.sleep(self.retry_time)
                 continue
 
             except ConnectionRefusedError as error:
                 logging_connection_refused(error, self.retry_time, self.debug)
                 await asyncio.sleep(self.retry_time)
                 continue
 
+            except Exception as error:
+                log_interrupt_error(error, self.debug)
+
             if self.final_message_check:
                 logging_break(self.debug)
                 break
 
         logging_api_completed(self.debug)
 
     def get_recordings_info_all(
```

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_bluetooth.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_bluetooth.py`

 * *Files 6% similar despite different names*

```diff
@@ -8,58 +8,15 @@
 import logging
 import time
 import base64
 import datetime
 from bleak import BleakClient, BleakScanner, exc
 
 from .config import settings
-from .debug_logs import (
-    logging_searching,
-    logging_device_info,
-    logging_device_not_found,
-    logging_device_found,
-    logging_device_address,
-    logging_trying_to_connect,
-    logging_connected,
-    logging_disconnected_recognised,
-    logging_batterylevel,
-    logging_sending_start,
-    logging_subscribing_eeg_notification,
-    logging_subscribing_battery_notification,
-    logging_sending_stop,
-    logging_giving_time_api,
-    logging_sending_stop_device,
-    logging_sending_disconnect,
-    logging_turn_ble_on,
-    logging_recording_successfully_stopped,
-    logging_keyboard_interrupt,
-    logging_turn_led_on,
-    logging_device_lost_give_up,
-    logging_trying_to_connect_again,
-    logging_device_connected_general,
-    logging_recording_started,
-    logging_time_reached,
-    logging_timeout_reached,
-    logging_ble_client_lost,
-    logging_ensuring_ble_disconnected,
-    logging_device_info_uuid,
-    logging_device_info_characteristic,
-    logging_device_description_list,
-    logging_device_connection_failed,
-    logging_reading_battery_level,
-    logging_getting_impedance,
-    logging_starting_impedance_measurement,
-    logging_subscribing_impedance_notification,
-    logging_starting_impedance_measurement_commands,
-    logging_displaying_impedance,
-    logging_stopping_impedance_measurement,
-    logging_ble_complete,
-    loggig_ble_init,
-    logging_batterylevel_int,
-)
+from .debug_logs import *
 
 
 class GuardianBLE:
     """Main Guardian BLE client."""
 
     def __init__(self, address: str = "", debug: bool = True) -> None:
         """Initialize the Guardian BLE client.
@@ -323,18 +280,20 @@
 
             package = {
                 "timestamp": new_time_stamp,
                 "deviceID": mac_id,
                 "data": data_base_64,
                 "stop": False,
             }
+            # print the size of the queue
+            # print(f"                        [BLE]: Queue size: {data_queue.qsize()}")
             if not data_queue.full():
-                await data_queue.put(package)
+                await asyncio.shield(data_queue.put(package))
             else:
-                await data_queue.get()
+                await asyncio.shield(data_queue.get())
 
         async def battery_handler(_, data):
             """Battery handler for the BLE client.
             Args:
                 callback (handler Object): Handler object
                 data (bytes): Battery Level as uint8_t
             """
@@ -637,16 +596,16 @@
         def initialise_timestamps():
             if self.initial_time:
                 self.initial_time = False  # record that this is the initial time
                 self.original_time = time.time()
 
         async def main_loop():
             while self.connection_established is True and self.time_left is True:
-                await asyncio.sleep(
-                    self.ble_delay
+                await asyncio.shield(
+                    asyncio.sleep(self.ble_delay)
                 )  # sleep so that everything can happen
                 remaining_time = record_time - (time.time() - self.original_time)
                 print(f"Time left: {round(remaining_time)}s")
                 if remaining_time <= 0:
                     self.time_left = False
                     logging_time_reached(self.debug, self.original_time)
 
@@ -682,15 +641,15 @@
 
                     logging_recording_started(self.debug)
                     self.try_to_connect_timeout = (
                         self.reconnect_try_amount
                     )  # reset counter
                     # >>>>>>>>>>>>>>>>>>>>> Main loop <<<<<<<<<<<<<<<<<<<<<<<<
                     initialise_timestamps()
-                    await main_loop()
+                    await asyncio.shield(main_loop())
                     # >>>>>>>>>>>>>>>>>>>>> Main loop <<<<<<<<<<<<<<<<<<<<<<<<
                     if not self.time_left:
                         logging_timeout_reached(self.debug)
 
                         if not impedance_measurement:
                             await stop_recording_timeout()
                         else:
```

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/igeb_utils.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/igeb_utils.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client/test_producer_consumer.py` & `idun_guardian_client-1.1b1/src/idun_guardian_client/test_producer_consumer.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/PKG-INFO` & `idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: idun-guardian-client
-Version: 1.1.0
+Version: 1.1b1
 Summary: Python SDK for communication with the IDUN Guardian earbuds and IDUN cloud
 Author-email: IDUN Technologies <contact@iduntechnologies.com>
 Classifier: Development Status :: 1 - Planning
 Classifier: License :: Other/Proprietary License
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.10
@@ -254,11 +254,11 @@
 from idun_guardian_client.igeb_api import GuardianAPI
 
 api = GuardianAPI()
 
 # download recording
 api.download_recording_by_id(
     device_id = "XX-XX-XX-XX-XX-XX",
-    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
+    recording_id = "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
 )
 # The info about th recording can be found in the log file
 ```
```

### Comparing `idun_guardian_client-1.1.0/src/idun_guardian_client.egg-info/SOURCES.txt` & `idun_guardian_client-1.1b1/src/idun_guardian_client.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/tests/test_ble.py` & `idun_guardian_client-1.1b1/tests/test_ble.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/tests/test_ble_record.py` & `idun_guardian_client-1.1b1/tests/test_ble_record.py`

 * *Files identical despite different names*

### Comparing `idun_guardian_client-1.1.0/tests/test_utils.py` & `idun_guardian_client-1.1b1/tests/test_utils.py`

 * *Files identical despite different names*

