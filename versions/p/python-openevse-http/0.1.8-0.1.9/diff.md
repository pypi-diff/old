# Comparing `tmp/python-openevse-http-0.1.8.tar.gz` & `tmp/python-openevse-http-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python-openevse-http-0.1.8.tar", last modified: Mon Oct 25 17:13:32 2021, max compression
+gzip compressed data, was "python-openevse-http-0.1.9.tar", last modified: Thu Oct 28 23:13:13 2021, max compression
```

## Comparing `python-openevse-http-0.1.8.tar` & `python-openevse-http-0.1.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-25 17:13:32.714161 python-openevse-http-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (121)      930 2021-10-25 17:13:32.714161 python-openevse-http-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      228 2021-10-25 17:13:27.000000 python-openevse-http-0.1.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-25 17:13:32.710161 python-openevse-http-0.1.8/openevsehttp/
--rw-r--r--   0 runner    (1001) docker     (121)    19330 2021-10-25 17:13:27.000000 python-openevse-http-0.1.8/openevsehttp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      117 2021-10-25 17:13:27.000000 python-openevse-http-0.1.8/openevsehttp/const.py
--rw-r--r--   0 runner    (1001) docker     (121)      252 2021-10-25 17:13:27.000000 python-openevse-http-0.1.8/openevsehttp/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-25 17:13:32.714161 python-openevse-http-0.1.8/python_openevse_http.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      930 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      354 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)        9 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2021-10-25 17:13:32.000000 python-openevse-http-0.1.8/python_openevse_http.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-10-25 17:13:32.718161 python-openevse-http-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1132 2021-10-25 17:13:27.000000 python-openevse-http-0.1.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-28 23:13:13.929793 python-openevse-http-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (121)      930 2021-10-28 23:13:13.929793 python-openevse-http-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      228 2021-10-28 23:13:11.000000 python-openevse-http-0.1.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-28 23:13:13.925793 python-openevse-http-0.1.9/openevsehttp/
+-rw-r--r--   0 runner    (1001) docker     (121)    20421 2021-10-28 23:13:11.000000 python-openevse-http-0.1.9/openevsehttp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      117 2021-10-28 23:13:11.000000 python-openevse-http-0.1.9/openevsehttp/const.py
+-rw-r--r--   0 runner    (1001) docker     (121)      252 2021-10-28 23:13:11.000000 python-openevse-http-0.1.9/openevsehttp/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-28 23:13:13.929793 python-openevse-http-0.1.9/python_openevse_http.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      930 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      354 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       17 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2021-10-28 23:13:13.000000 python-openevse-http-0.1.9/python_openevse_http.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-10-28 23:13:13.929793 python-openevse-http-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1143 2021-10-28 23:13:11.000000 python-openevse-http-0.1.9/setup.py
```

### Comparing `python-openevse-http-0.1.8/PKG-INFO` & `python-openevse-http-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-openevse-http
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python wrapper for OpenEVSE HTTP API
 Home-page: https://github.com/firstof9/python-openevse-http
 Author: firstof9
 Author-email: firstof9@gmail.com
 License: UNKNOWN
 Download-URL: https://github.com/firstof9/python-openevse-http
 Description: # python-openevse-http
```

### Comparing `python-openevse-http-0.1.8/openevsehttp/__init__.py` & `python-openevse-http-0.1.9/openevsehttp/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 """Provide a package for python-openevse-http."""
 from __future__ import annotations
 
 import asyncio
 import datetime
 import logging
-from typing import Optional
+from typing import Any, Callable, Optional
 
-import aiohttp
+import aiohttp  # type: ignore
 import requests  # type: ignore
 
 from .const import MAX_AMPS, MIN_AMPS
 from .exceptions import AuthenticationError, ParseJSONError, HTTPError
 
 _LOGGER = logging.getLogger(__name__)
 
@@ -49,30 +49,20 @@
     def __init__(
         self,
         server,
         callback,
         user=None,
         password=None,
     ):
-        """Initialize a OpenEVSEWebsocket instance.
-        Parameters:
-            server (openevse address):
-                A connected instance.
-            callback (Runnable):
-                Called when interesting events occur. Provides arguments:
-                   msgtype (str): Message type or SIGNAL_* constant
-                   data (str): Current STATE_* or websocket payload contents
-                   error (str): Error message if any or None
-        """
+        """Initialize a OpenEVSEWebsocket instance."""
         self.session = aiohttp.ClientSession()
         self.uri = self._get_uri(server)
-        self._user = (user,)
-        self._password = (password,)
+        self._user = user
+        self._password = password
         self.callback = callback
-        self.subscriptions = ["message"]
         self._state = None
         self.failed_attempts = 0
         self._error_reason = None
 
     @property
     def state(self):
         """Return the current state."""
@@ -85,82 +75,49 @@
         _LOGGER.debug("Websocket %s", value)
         self.callback(SIGNAL_CONNECTION_STATE, value, self._error_reason)
         self._error_reason = None
 
     @staticmethod
     def _get_uri(server):
         """Generate the websocket URI."""
-        return server._url("/:/ws").replace("http", "ws")
+        return server[: server.rfind("/")].replace("http", "ws") + "/ws"
 
     async def running(self):
         """Open a persistent websocket connection and act on events."""
         self.state = STATE_STARTING
+        auth = None
+
+        if self._user and self._password:
+            auth = aiohttp.BasicAuth(self._user, self._password)
 
         try:
-            if self._user and self._password:
-                async with self.session.ws_connect(
-                    self.uri,
-                    heartbeat=15,
-                    auth=aiohttp.BasicAuth(self._user, self._password),
-                ) as ws_client:
-                    self.state = STATE_CONNECTED
-                    self.failed_attempts = 0
-
-                    async for message in ws_client:
-                        if self.state == STATE_STOPPED:
-                            break
-
-                        if message.type == aiohttp.WSMsgType.TEXT:
-                            msg = message.json()
-                            msgtype = msg["type"]
-
-                            if msgtype not in self.subscriptions:
-                                _LOGGER.debug("Ignoring: %s", msg)
-                                continue
-
-                            else:
-                                self.callback(msgtype, msg, None)
-
-                        elif message.type == aiohttp.WSMsgType.CLOSED:
-                            _LOGGER.warning("AIOHTTP websocket connection closed")
-                            break
-
-                        elif message.type == aiohttp.WSMsgType.ERROR:
-                            _LOGGER.error("AIOHTTP websocket error")
-                            break
-            else:
-                async with self.session.ws_connect(
-                    self.uri,
-                    heartbeat=15,
-                ) as ws_client:
-                    self.state = STATE_CONNECTED
-                    self.failed_attempts = 0
-
-                    async for message in ws_client:
-                        if self.state == STATE_STOPPED:
-                            break
-
-                        if message.type == aiohttp.WSMsgType.TEXT:
-                            msg = message.json()
-                            msgtype = msg["type"]
-
-                            if msgtype not in self.subscriptions:
-                                _LOGGER.debug("Ignoring: %s", msg)
-                                continue
-
-                            else:
-                                self.callback(msgtype, msg, None)
-
-                        elif message.type == aiohttp.WSMsgType.CLOSED:
-                            _LOGGER.warning("AIOHTTP websocket connection closed")
-                            break
-
-                        elif message.type == aiohttp.WSMsgType.ERROR:
-                            _LOGGER.error("AIOHTTP websocket error")
-                            break
+            async with self.session.ws_connect(
+                self.uri,
+                heartbeat=15,
+                auth=auth,
+            ) as ws_client:
+                self.state = STATE_CONNECTED
+                self.failed_attempts = 0
+
+                async for message in ws_client:
+                    if self.state == STATE_STOPPED:
+                        break
+
+                    if message.type == aiohttp.WSMsgType.TEXT:
+                        msg = message.json()
+                        msgtype = "data"
+                        self.callback(msgtype, msg, None)
+
+                    elif message.type == aiohttp.WSMsgType.CLOSED:
+                        _LOGGER.warning("Websocket connection closed")
+                        break
+
+                    elif message.type == aiohttp.WSMsgType.ERROR:
+                        _LOGGER.error("Websocket error")
+                        break
 
         except aiohttp.ClientResponseError as error:
             if error.code == 401:
                 _LOGGER.error("Credentials rejected: %s", error)
                 self._error_reason = ERROR_AUTH_FAILURE
             else:
                 _LOGGER.error("Unexpected response received: %s", error)
@@ -187,15 +144,15 @@
                 self.state = STATE_STOPPED
         else:
             if self.state != STATE_STOPPED:
                 self.state = STATE_DISCONNECTED
                 await asyncio.sleep(5)
 
     async def listen(self):
-        """Close the listening websocket."""
+        """Start the listening websocket."""
         self.failed_attempts = 0
         while self.state != STATE_STOPPED:
             await self.running()
 
     def close(self):
         """Close the listening websocket."""
         self.state = STATE_STOPPED
@@ -204,65 +161,141 @@
 class OpenEVSE:
     """Represent an OpenEVSE charger."""
 
     def __init__(self, host: str, user: str = None, pwd: str = None) -> None:
         """Connect to an OpenEVSE charger equipped with wifi or ethernet."""
         self._user = user
         self._pwd = pwd
-        self._url = f"http://{host}"
-        self._status = None
-        self._config = None
+        self.url = f"http://{host}/"
+        self._status: dict = {}
+        self._config: dict = {}
         self._override = None
+        self._ws_listening = False
+        self.websocket: Optional[OpenEVSEWebsocket] = None
+        self.callback: Optional[Callable] = None
+        self._loop = None
 
-    def send_command(self, command: str) -> tuple | None:
+    async def send_command(self, command: str) -> tuple | None:
         """Send a RAPI command to the charger and parses the response."""
-        url = f"{self._url}/r"
+        auth = None
+        url = f"{self.url}r"
         data = {"json": 1, "rapi": command}
 
+        if self._user and self._pwd:
+            auth = aiohttp.BasicAuth(self._user, self._pwd)
+
         _LOGGER.debug("Posting data: %s to %s", command, url)
-        if self._user is not None:
-            value = requests.post(url, data=data, auth=(self._user, self._pwd))
-        else:
-            value = requests.post(url, data=data)
+        async with aiohttp.ClientSession() as session:
+            async with session.post(url, data=data, auth=auth) as resp:
+                if resp.status == 400:
+                    _LOGGER.debug("JSON error: %s", await resp.text())
+                    raise ParseJSONError
+                if resp.status == 401:
+                    _LOGGER.debug("Authentication error: %s", await resp)
+                    raise AuthenticationError
+
+                value = await resp.json()
+
+                if "ret" not in value:
+                    return False, ""
+                return value["cmd"], value["ret"]
 
-        if value.status_code == 400:
-            _LOGGER.debug("JSON error: %s", value.text)
-            raise ParseJSONError
-        if value.status_code == 401:
-            _LOGGER.debug("Authentication error: %s", value)
-            raise AuthenticationError
+    async def update(self) -> None:
+        """Update the values."""
+        auth = None
+        urls = [f"{self.url}config"]
 
-        if "ret" not in value.json():
-            return False, ""
-        resp = value.json()
-        return resp["cmd"], resp["ret"]
+        if self._user and self._pwd:
+            auth = aiohttp.BasicAuth(self._user, self._pwd)
 
-    def update(self) -> None:
-        """Update the values."""
-        urls = [f"{self._url}/status", f"{self._url}/config"]
+        if not self._ws_listening:
+            urls = [f"{self.url}status", f"{self.url}config"]
 
-        for url in urls:
-            _LOGGER.debug("Updating data from %s", url)
-            if self._user is not None:
-                value = requests.get(url, auth=(self._user, self._pwd))
-            else:
-                value = requests.get(url)
+        async with aiohttp.ClientSession() as session:
+            for url in urls:
+                _LOGGER.debug("Updating data from %s", url)
+                async with session.get(url, auth=auth) as resp:
+                    if resp.status == 401:
+                        _LOGGER.debug("Authentication error: %s", resp)
+                        raise AuthenticationError
+
+                    if "/status" in url:
+                        self._status = await resp.json()
+                        _LOGGER.debug("Status update: %s", self._status)
+                    else:
+                        self._config = await resp.json()
+                        _LOGGER.debug("Config update: %s", self._config)
+
+        if not self.websocket:
+            # Start Websocket listening
+            self.websocket = OpenEVSEWebsocket(
+                self.url, self._update_status, self._user, self._pwd
+            )
+            if not self._ws_listening:
+                self._start_listening()
 
-            if value.status_code == 401:
-                _LOGGER.debug("Authentication error: %s", value)
-                raise AuthenticationError
+    def _start_listening(self):
+        """Start the websocket listener."""
+        try:
+            _LOGGER.debug("Attempting to find running loop...")
+            self._loop = asyncio.get_running_loop()
+        except RuntimeError:
+            self._loop = asyncio.get_event_loop()
+            _LOGGER.debug("Using new event loop...")
+
+        if not self._ws_listening:
+            self._loop.create_task(self.websocket.listen())
+            pending = asyncio.all_tasks()
+            self._ws_listening = True
+            self._loop.run_until_complete(asyncio.gather(*pending))
+
+    def _update_status(self, msgtype, data, error):
+        """Update data from websocket listener."""
+        if msgtype == SIGNAL_CONNECTION_STATE:
+            if data == STATE_CONNECTED:
+                _LOGGER.debug("Websocket to %s successful", self.url)
+                self._ws_listening = True
+            elif data == STATE_DISCONNECTED:
+                _LOGGER.debug(
+                    "Websocket to %s disconnected, retrying",
+                    self.url,
+                )
+                self._ws_listening = False
+            # Stopped websockets without errors are expected during shutdown
+            # and ignored
+            elif data == STATE_STOPPED and error:
+                _LOGGER.error(
+                    "Websocket to %s failed, aborting [Error: %s]",
+                    self.url,
+                    error,
+                )
+                self._ws_listening = False
 
-            if "/status" in url:
-                self._status = value.json()
-            else:
-                self._config = value.json()
+        elif msgtype == "data":
+            _LOGGER.debug("ws_data: %s", data)
+            self._status.update(data)
+
+            if self.callback is not None:
+                self.callback()
+
+    def ws_disconnect(self) -> None:
+        """Disconnect the websocket listener."""
+        assert self.websocket
+        self.websocket.close()
+        self._ws_listening = False
+
+    @property
+    def ws_state(self) -> Any:
+        """Return the status of the websocket listener."""
+        assert self.websocket
+        return self.websocket.state
 
     def get_override(self) -> None:
         """Get the manual override status."""
-        url = f"{self._url}/overrride"
+        url = f"{self.url}/overrride"
 
         _LOGGER.debug("Geting data from %s", url)
         if self._user is not None:
             value = requests.get(url, auth=(self._user, self._pwd))
         else:
             value = requests.get(url)
 
@@ -278,15 +311,15 @@
         charge_current: int,
         max_current: int,
         energy_limit: int,
         time_limit: int,
         auto_release: bool = True,
     ) -> str:
         """Set the manual override status."""
-        url = f"{self._url}/overrride"
+        url = f"{self.url}/overrride"
 
         if state not in ["active", "disabled"]:
             raise ValueError
 
         data = {
             "state": state,
             "charge_current": charge_current,
@@ -306,15 +339,15 @@
             _LOGGER.debug("Authentication error: %s", value)
             raise AuthenticationError
 
         return value["msg"]
 
     def toggle_override(self) -> None:
         """Toggle the manual override status."""
-        url = f"{self._url}/overrride"
+        url = f"{self.url}/overrride"
 
         _LOGGER.debug("Toggling manual override %s", url)
         if self._user is not None:
             value = requests.patch(url, auth=(self._user, self._pwd))
         else:
             value = requests.patch(url)
 
@@ -324,15 +357,15 @@
 
         if value.status_code != 200:
             _LOGGER.error("Problem handling request: %s", value)
             raise HTTPError
 
     def clear_override(self) -> None:
         """Clear the manual override status."""
-        url = f"{self._url}/overrride"
+        url = f"{self.url}/overrride"
 
         _LOGGER.debug("Clearing manual overrride %s", url)
         if self._user is not None:
             value = requests.delete(url, auth=(self._user, self._pwd))
         else:
             value = requests.delete(url)
```

### Comparing `python-openevse-http-0.1.8/python_openevse_http.egg-info/PKG-INFO` & `python-openevse-http-0.1.9/python_openevse_http.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-openevse-http
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python wrapper for OpenEVSE HTTP API
 Home-page: https://github.com/firstof9/python-openevse-http
 Author: firstof9
 Author-email: firstof9@gmail.com
 License: UNKNOWN
 Download-URL: https://github.com/firstof9/python-openevse-http
 Description: # python-openevse-http
```

### Comparing `python-openevse-http-0.1.8/setup.py` & `python-openevse-http-0.1.9/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 """Setup module for python-openevse-http."""
 from pathlib import Path
 
 from setuptools import find_packages, setup
 
 PROJECT_DIR = Path(__file__).parent.resolve()
 README_FILE = PROJECT_DIR / "README.md"
-VERSION = "0.1.8"
+VERSION = "0.1.9"
 
 
 setup(
     name="python-openevse-http",
     version=VERSION,
     url="https://github.com/firstof9/python-openevse-http",
     download_url="https://github.com/firstof9/python-openevse-http",
     author="firstof9",
     author_email="firstof9@gmail.com",
     description="Python wrapper for OpenEVSE HTTP API",
     long_description=README_FILE.read_text(encoding="utf-8"),
     long_description_content_type="text/markdown",
     packages=find_packages(exclude=["test.*", "tests"]),
     python_requires=">=3.8",
-    install_requires=["requests"],
+    install_requires=["aiohttp", "requests"],
     entry_points={},
     include_package_data=True,
     zip_safe=False,
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Natural Language :: English",
```

