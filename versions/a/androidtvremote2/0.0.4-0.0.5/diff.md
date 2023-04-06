# Comparing `tmp/androidtvremote2-0.0.4.tar.gz` & `tmp/androidtvremote2-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "androidtvremote2-0.0.4.tar", last modified: Wed Apr  5 05:47:37 2023, max compression
+gzip compressed data, was "androidtvremote2-0.0.5.tar", last modified: Thu Apr  6 09:34:33 2023, max compression
```

## Comparing `androidtvremote2-0.0.4.tar` & `androidtvremote2-0.0.5.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:47:37.343939 androidtvremote2-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-05 05:47:37.343939 androidtvremote2-0.0.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-05 05:47:37.343939 androidtvremote2-0.0.4/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:47:37.335940 androidtvremote2-0.0.4/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:47:37.339939 androidtvremote2-0.0.4/src/androidtvremote2/
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14359 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/androidtv_remote.py
--rw-r--r--   0 runner    (1001) docker     (123)     3107 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1794 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/certificate_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/const.py
--rw-r--r--   0 runner    (1001) docker     (123)      315 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8318 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/pairing.py
--rw-r--r--   0 runner    (1001) docker     (123)     4186 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/polo_pb2.py
--rw-r--r--   0 runner    (1001) docker     (123)     5968 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/remote.py
--rw-r--r--   0 runner    (1001) docker     (123)    19528 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/src/androidtvremote2/remotemessage_pb2.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:47:37.339939 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-05 05:47:37.000000 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      644 2023-04-05 05:47:37.000000 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 05:47:37.000000 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-04-05 05:47:37.000000 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 05:47:37.000000 androidtvremote2-0.0.4/src/androidtvremote2.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:47:37.339939 androidtvremote2-0.0.4/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-05 05:47:24.000000 androidtvremote2-0.0.4/tests/test_androidtv_remote.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1986 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2483 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:34:33.129868 androidtvremote2-0.0.5/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/src/androidtvremote2/
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14391 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/androidtv_remote.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3107 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1794 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/certificate_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/const.py
+-rw-r--r--   0 runner    (1001) docker     (123)      315 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8318 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/pairing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4186 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/polo_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6806 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/remote.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19528 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/src/androidtvremote2/remotemessage_pb2.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-06 09:34:33.000000 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      644 2023-04-06 09:34:33.000000 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:34:33.000000 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-04-06 09:34:33.000000 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 09:34:33.000000 androidtvremote2-0.0.5/src/androidtvremote2.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:34:33.133868 androidtvremote2-0.0.5/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-06 09:34:23.000000 androidtvremote2-0.0.5/tests/test_androidtv_remote.py
```

### Comparing `androidtvremote2-0.0.4/LICENSE` & `androidtvremote2-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/PKG-INFO` & `androidtvremote2-0.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: androidtvremote2
-Version: 0.0.4
+Version: 0.0.5
 Summary: A Python library for interacting with Android TV using the Android TV Remote protocol v2
 Author-email: tronikos <tronikos@gmail.com>
 License: Apache-2.0
 Project-URL: Homepage, https://github.com/tronikos/androidtvremote2
 Project-URL: Bug Tracker, https://github.com/tronikos/androidtvremote2/issues
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `androidtvremote2-0.0.4/README.md` & `androidtvremote2-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/pyproject.toml` & `androidtvremote2-0.0.5/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "androidtvremote2"
-version = "0.0.4"
+version = "0.0.5"
 license = {text = "Apache-2.0"}
 authors = [
     { name="tronikos", email="tronikos@gmail.com" },
 ]
 description = "A Python library for interacting with Android TV using the Android TV Remote protocol v2"
 readme = "README.md"
 requires-python = ">=3.7"
```

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/androidtv_remote.py` & `androidtvremote2-0.0.5/src/androidtvremote2/androidtv_remote.py`

 * *Files 0% similar despite different names*

```diff
@@ -158,14 +158,15 @@
             ) = await self._loop.create_connection(
                 lambda: RemoteProtocol(
                     on_con_lost,
                     on_remote_started,
                     self._on_is_on_updated,
                     self._on_current_app_updated,
                     self._on_volume_info_updated,
+                    self._loop,
                 ),
                 self.host,
                 self._api_port,
                 ssl=ssl_context,
             )
         except OSError as exc:
             LOGGER.debug(
```

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/base.py` & `androidtvremote2-0.0.5/src/androidtvremote2/base.py`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/certificate_generator.py` & `androidtvremote2-0.0.5/src/androidtvremote2/certificate_generator.py`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/pairing.py` & `androidtvremote2-0.0.5/src/androidtvremote2/pairing.py`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/polo_pb2.py` & `androidtvremote2-0.0.5/src/androidtvremote2/polo_pb2.py`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/remote.py` & `androidtvremote2-0.0.5/src/androidtvremote2/remote.py`

 * *Files 18% similar despite different names*

```diff
@@ -30,33 +30,38 @@
     def __init__(
         self,
         on_con_lost: asyncio.Future,
         on_remote_started: asyncio.Future,
         on_is_on_updated: Callable,
         on_current_app_updated: Callable,
         on_volume_info_updated: Callable,
+        loop: asyncio.AbstractEventLoop,
     ) -> None:
         """Initialize.
 
         :param on_con_lost: callback for when the connection is lost or closed.
         :param on_remote_started: callback for when the Android TV is ready to receive commands.
         :param on_is_on_updated: callback for when is_on is updated.
         :param on_current_app_updated: callback for when current_app is updated.
         :param on_volume_info_updated: callback for when volume_info is updated.
+        :param loop: event loop.
         """
         super().__init__(on_con_lost)
         self._on_remote_started = on_remote_started
         self._on_is_on_updated = on_is_on_updated
         self._on_current_app_updated = on_current_app_updated
         self._on_volume_info_updated = on_volume_info_updated
         self._active_mask = 622
         self.is_on = False
         self.current_app = ""
         self.device_info: dict[str, str] = {}
         self.volume_info: dict[str, str | bool] = {}
+        self._loop = loop
+        self._idle_disconnect_task: asyncio.Task | None = None
+        self._reset_idle_disconnect_task()
 
     def send_key_command(
         self, key_code: int | str, direction: int | str = RemoteDirection.SHORT
     ):
         """Send a key press to Android TV.
 
         This does not block; it buffers the data and arranges for it to be sent out asynchronously.
@@ -84,14 +89,15 @@
         """
         msg = RemoteMessage()
         msg.remote_app_link_launch_request.app_link = app_link
         self._send_message(msg)
 
     def _handle_message(self, raw_msg):
         """Handle a message from the server."""
+        self._reset_idle_disconnect_task()
         msg = RemoteMessage()
         try:
             msg.ParseFromString(raw_msg)
         except DecodeError as exc:
             LOGGER.debug("Couldn't parse as RemoteMessage. %s", exc)
             return
         if LOG_PING_REQUESTS or not msg.HasField("remote_ping_request"):
@@ -139,7 +145,22 @@
         else:
             LOGGER.debug(
                 "Unhandled: %s", text_format.MessageToString(msg, as_one_line=True)
             )
 
         if new_msg != RemoteMessage():
             self._send_message(new_msg, log_send)
+
+    def _reset_idle_disconnect_task(self):
+        if self._idle_disconnect_task is not None:
+            self._idle_disconnect_task.cancel()
+        self._idle_disconnect_task = self._loop.create_task(
+            self._async_idle_disconnect()
+        )
+
+    async def _async_idle_disconnect(self):
+        # Disconnect if there is no message from the server within
+        # 16 seconds. Pings are every 5 seconds. This is similar to
+        # the server behavior that closes connections after 3
+        # unanswered pings.
+        await asyncio.sleep(16)
+        self.transport.close()
```

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2/remotemessage_pb2.py` & `androidtvremote2-0.0.5/src/androidtvremote2/remotemessage_pb2.py`

 * *Files identical despite different names*

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2.egg-info/PKG-INFO` & `androidtvremote2-0.0.5/src/androidtvremote2.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: androidtvremote2
-Version: 0.0.4
+Version: 0.0.5
 Summary: A Python library for interacting with Android TV using the Android TV Remote protocol v2
 Author-email: tronikos <tronikos@gmail.com>
 License: Apache-2.0
 Project-URL: Homepage, https://github.com/tronikos/androidtvremote2
 Project-URL: Bug Tracker, https://github.com/tronikos/androidtvremote2/issues
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `androidtvremote2-0.0.4/src/androidtvremote2.egg-info/SOURCES.txt` & `androidtvremote2-0.0.5/src/androidtvremote2.egg-info/SOURCES.txt`

 * *Files identical despite different names*

