# Comparing `tmp/reolink_aio-0.5.8.tar.gz` & `tmp/reolink_aio-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "reolink_aio-0.5.8.tar", last modified: Wed Mar 29 17:58:11 2023, max compression
+gzip compressed data, was "reolink_aio-0.5.9.tar", last modified: Fri Mar 31 15:05:48 2023, max compression
```

## Comparing `reolink_aio-0.5.8.tar` & `reolink_aio-0.5.9.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/
--rw-r--r--   0 runner    (1001) docker     (122)     1069 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     4113 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     3305 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/reolink_aio/
--rw-r--r--   0 runner    (1001) docker     (122)       30 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)   167714 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/api.py
--rw-r--r--   0 runner    (1001) docker     (122)      826 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/enums.py
--rw-r--r--   0 runner    (1001) docker     (122)     1087 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (122)     8014 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/software_version.py
--rw-r--r--   0 runner    (1001) docker     (122)     4713 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/templates.py
--rw-r--r--   0 runner    (1001) docker     (122)      590 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/reolink_aio/typings.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/reolink_aio.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     4113 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      418 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (122)       24 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       12 2023-03-29 17:58:11.000000 reolink_aio-0.5.8/reolink_aio.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1380 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-29 17:58:11.401938 reolink_aio-0.5.8/tests/
--rw-r--r--   0 runner    (1001) docker     (122)    15443 2023-03-29 17:58:01.000000 reolink_aio-0.5.8/tests/test.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-31 15:05:48.760459 reolink_aio-0.5.9/
+-rw-r--r--   0 runner    (1001) docker     (122)     1069 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     4113 2023-03-31 15:05:48.760459 reolink_aio-0.5.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     3305 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-31 15:05:48.756459 reolink_aio-0.5.9/reolink_aio/
+-rw-r--r--   0 runner    (1001) docker     (122)       30 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)   168286 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/api.py
+-rw-r--r--   0 runner    (1001) docker     (122)      826 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/enums.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1087 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8014 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/software_version.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4713 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/templates.py
+-rw-r--r--   0 runner    (1001) docker     (122)      590 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/reolink_aio/typings.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-31 15:05:48.760459 reolink_aio-0.5.9/reolink_aio.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     4113 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      418 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)       24 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       12 2023-03-31 15:05:48.000000 reolink_aio-0.5.9/reolink_aio.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-03-31 15:05:48.760459 reolink_aio-0.5.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1380 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-31 15:05:48.760459 reolink_aio-0.5.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)    15443 2023-03-31 15:05:37.000000 reolink_aio-0.5.9/tests/test.py
```

### Comparing `reolink_aio-0.5.8/LICENSE` & `reolink_aio-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/PKG-INFO` & `reolink_aio-0.5.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: reolink_aio
-Version: 0.5.8
+Version: 0.5.9
 Summary: Reolink NVR/cameras API package
 Home-page: https://github.com/starkillerOG/reolink_aio
 Author: starkillerOG
 Author-email: starkiller.og@gmail.com
 License: MIT
 Platform: any
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `reolink_aio-0.5.8/README.md` & `reolink_aio-0.5.9/README.md`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio/api.py` & `reolink_aio-0.5.9/reolink_aio/api.py`

 * *Files 1% similar despite different names*

```diff
@@ -825,14 +825,17 @@
         if self.api_version("upgrade") >= 2:
             self._capabilities["Host"].append("update")
 
         # Channel capabilities
         for channel in self._channels:
             self._capabilities[channel] = []
 
+            if self.is_nvr and self.api_version("supportAutoTrackStream", channel) > 0:
+                self._capabilities[channel].append("autotrack_stream")
+
             if channel in self._ftp_settings:
                 self._capabilities[channel].append("ftp")
 
             if channel in self._push_settings:
                 self._capabilities[channel].append("push")
 
             if channel in self._recording_settings:
@@ -847,15 +850,15 @@
             if self.api_version("ledControl", channel) > 0 and channel in self._ir_settings:
                 self._capabilities[channel].append("ir_lights")
 
             if self.api_version("powerLed", channel) > 0:
                 # powerLed == statusLed = doorbell_led
                 self._capabilities[channel].append("status_led")  # internal use only
                 self._capabilities[channel].append("power_led")
-            if self.api_version("supportDoorbellLight", channel) > 0:
+            if self.api_version("supportDoorbellLight", channel) > 0 or self.is_doorbell(channel):
                 # powerLed == statusLed = doorbell_led
                 self._capabilities[channel].append("status_led")  # internal use only
                 self._capabilities[channel].append("doorbell_led")
 
             if self.api_version("GetWhiteLed") > 0 and (
                 self.api_version("floodLight", channel) > 0 or self.api_version("supportFLswitch", channel) > 0 or self.api_version("supportFLBrightness", channel) > 0
             ):
@@ -863,15 +866,17 @@
                 self._capabilities[channel].append("floodLight")
 
             if self.api_version("GetAudioCfg") > 0:
                 self._capabilities[channel].append("volume")
                 if self.api_version("supportVisitorLoudspeaker", channel) > 0:
                     self._capabilities[channel].append("doorbell_button_sound")
 
-            if self.is_doorbell(channel) and self.api_version("GetAudioFileList") > 0 and self.api_version("GetAutoReply") > 0:
+            if (self.api_version("supportAudioFileList", channel) > 0 and self.api_version("supportAutoReply", channel) > 0) or (
+                not self.is_nvr and self.api_version("supportAudioFileList") > 0 and self.api_version("supportAutoReply") > 0
+            ):
                 self._capabilities[channel].append("quick_reply")
 
             if channel in self._audio_alarm_settings:
                 self._capabilities[channel].append("siren")
 
             if self.audio_record(channel) is not None:
                 self._capabilities[channel].append("audio")
@@ -1223,19 +1228,18 @@
                 {"cmd": "GetAiState", "action": 0, "param": {"channel": channel}},  # to capture AI capabilities
                 {"cmd": "GetEvents", "action": 0, "param": {"channel": channel}},
                 {"cmd": "GetWhiteLed", "action": 0, "param": {"channel": channel}},
                 {"cmd": "GetIsp", "action": 0, "param": {"channel": channel}},
                 {"cmd": "GetIrLights", "action": 0, "param": {"channel": channel}},
                 {"cmd": "GetAudioCfg", "action": 0, "param": {"channel": channel}},
             ]
-            if self.is_doorbell(channel):
-                ch_body.append({"cmd": "GetAudioFileList", "action": 0, "param": {"channel": channel}})
-                ch_body.append({"cmd": "GetAutoReply", "action": 0, "param": {"channel": channel}})
             # one time values
             ch_body.append({"cmd": "GetOsd", "action": 0, "param": {"channel": channel}})
+            if self.supported(channel, "quick_reply"):
+                ch_body.append({"cmd": "GetAudioFileList", "action": 0, "param": {"channel": channel}})
             # checking range
             if self.supported(channel, "zoom_basic"):
                 ch_body.append({"cmd": "GetZoomFocus", "action": 1, "param": {"channel": channel}})
             if self.supported(channel, "pan_tilt") and self.api_version("ptzPreset", channel) >= 1:
                 ch_body.append({"cmd": "GetPtzPreset", "action": 0, "param": {"channel": channel}})
                 ch_body.append({"cmd": "GetPtzGuard", "action": 0, "param": {"channel": channel}})
             if self.supported(channel, "auto_track"):
@@ -1272,16 +1276,14 @@
                     return 1
             return 0
 
         self._api_version["GetEvents"] = check_command_exists("GetEvents")
         self._api_version["GetWhiteLed"] = check_command_exists("GetWhiteLed")
         self._api_version["GetAudioCfg"] = check_command_exists("GetAudioCfg")
         self._api_version["GetPtzGuard"] = check_command_exists("GetPtzGuard")
-        self._api_version["GetAudioFileList"] = check_command_exists("GetAudioFileList")
-        self._api_version["GetAutoReply"] = check_command_exists("GetAutoReply")
         if self.api_version("scheduleVersion") >= 1:
             self._api_version["GetEmail"] = check_command_exists("GetEmailV20")
             self._api_version["GetPush"] = check_command_exists("GetPushV20")
             self._api_version["GetFtp"] = check_command_exists("GetFtpV20")
             self._api_version["GetRec"] = check_command_exists("GetRecV20")
             self._api_version["GetAudioAlarm"] = check_command_exists("GetAudioAlarmV20")
             self._api_version["GetMdAlarm"] = check_command_exists("GetMdAlarm")
@@ -1539,21 +1541,36 @@
             raise NoDataError(f"Host: {self._host}:{self._port}: error obtaining update progress response") from err
 
         if json_data[0]["code"] != 0:
             return False
 
         return json_data[0]["value"]["Status"]["Persent"]
 
-    async def get_snapshot(self, channel: int) -> bytes | None:
+    async def get_snapshot(self, channel: int, stream: Optional[str] = None) -> bytes | None:
         """Get the still image."""
         if channel not in self._stream_channels:
             return None
 
+        if stream is None:
+            stream = "main"
+
         param: dict[str, Any] = {"cmd": "Snap", "channel": channel}
 
+        if stream.startswith("autotrack_"):
+            param["iLogicChannel"] = 1
+            stream = stream.removeprefix("autotrack_")
+
+        if stream.startswith("snapshots_"):
+            stream = stream.removeprefix("snapshots_")
+
+        if stream not in ["main", "sub"]:
+            stream = "main"
+
+        param["snapType"] = stream
+
         body: reolink_json = [{}]
         response = await self.send(body, param, expected_response_type="image/jpeg")
         if response is None or response == b"":
             _LOGGER.error(
                 "Host: %s:%s: error obtaining still image response for channel %s.",
                 self._host,
                 self._port,
@@ -1583,15 +1600,15 @@
         if channel not in self._stream_channels:
             return None
 
         if stream is None:
             stream = self._stream
 
         stream_type = None
-        if stream == "sub":
+        if stream in ["sub", "autotrack_sub"]:
             stream_type = 1
         else:
             stream_type = 0
         if self._rtmp_auth_method == DEFAULT_RTMP_AUTH_METHOD:
             password = parse.quote(self._password)
             return f"rtmp://{self._host}:{self._rtmp_port}/bcs/channel{channel}_{stream}.bcs?channel={channel}&stream={stream_type}&user={self._username}&password={password}"
 
@@ -1649,22 +1666,22 @@
             await self.login()
         except LoginError:
             return None
 
         if stream is None:
             stream = self._stream
 
-        if stream not in ["main", "sub", "ext"]:
+        if stream not in ["main", "sub", "ext", "autotrack_sub"]:
             return None
         if self.protocol == "rtmp":
             return self.get_rtmp_stream_source(channel, stream)
+        if self.protocol == "flv" or stream == "autotrack_sub":
+            return self.get_flv_stream_source(channel, stream)
         if self.protocol == "rtsp":
             return await self.get_rtsp_stream_source(channel, stream)
-        if self.protocol == "flv":
-            return self.get_flv_stream_source(channel, stream)
         return None
 
     async def get_vod_source(
         self,
         channel: int,
         filename: str,
         stream: Optional[str] = None,
```

### Comparing `reolink_aio-0.5.8/reolink_aio/enums.py` & `reolink_aio-0.5.9/reolink_aio/enums.py`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio/exceptions.py` & `reolink_aio-0.5.9/reolink_aio/exceptions.py`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio/software_version.py` & `reolink_aio-0.5.9/reolink_aio/software_version.py`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio/templates.py` & `reolink_aio-0.5.9/reolink_aio/templates.py`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio/typings.py` & `reolink_aio-0.5.9/reolink_aio/typings.py`

 * *Files identical despite different names*

### Comparing `reolink_aio-0.5.8/reolink_aio.egg-info/PKG-INFO` & `reolink_aio-0.5.9/reolink_aio.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: reolink-aio
-Version: 0.5.8
+Version: 0.5.9
 Summary: Reolink NVR/cameras API package
 Home-page: https://github.com/starkillerOG/reolink_aio
 Author: starkillerOG
 Author-email: starkiller.og@gmail.com
 License: MIT
 Platform: any
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `reolink_aio-0.5.8/setup.py` & `reolink_aio-0.5.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 # The directory containing this file
 HERE = pathlib.Path(__file__).parent
 
 # The text of the README file
 README = (HERE / "README.md").read_text()
 
 setup(name='reolink_aio',
-      version='0.5.8',
+      version='0.5.9',
       description='Reolink NVR/cameras API package',
       long_description=README,
       long_description_content_type="text/markdown",
       url='https://github.com/starkillerOG/reolink_aio',
       author='starkillerOG',
       author_email='starkiller.og@gmail.com',
       license='MIT',
```

### Comparing `reolink_aio-0.5.8/tests/test.py` & `reolink_aio-0.5.9/tests/test.py`

 * *Files identical despite different names*

