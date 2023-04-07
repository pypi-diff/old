# Comparing `tmp/bilibili-live-0.8.3.tar.gz` & `tmp/bilibili-live-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bilibili-live-0.8.3.tar", last modified: Fri Jan  6 07:34:14 2023, max compression
+gzip compressed data, was "bilibili-live-0.9.0.tar", last modified: Tue Jan 10 13:44:38 2023, max compression
```

## Comparing `bilibili-live-0.8.3.tar` & `bilibili-live-0.9.0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
--rw-rw-rw-   0        0        0     1091 2022-10-14 12:55:37.353044 bilibili-live-0.8.3/LICENSE
--rw-rw-rw-   0        0        0      637 2023-01-06 07:34:02.248357 bilibili-live-0.8.3/pyproject.toml
--rw-rw-rw-   0        0        0     1724 2022-11-23 08:33:29.073553 bilibili-live-0.8.3/README.md
--rw-rw-rw-   0        0        0       70 2022-10-14 12:55:37.353544 bilibili-live-0.8.3/src/bilibili_live/__init__.py
--rw-rw-rw-   0        0        0      228 2022-10-14 12:55:37.353544 bilibili-live-0.8.3/src/bilibili_live/api/__init__.py
--rw-rw-rw-   0        0        0      560 2022-10-14 12:55:37.354045 bilibili-live-0.8.3/src/bilibili_live/api/generateLoginQRCode.py
--rw-rw-rw-   0        0        0      540 2022-10-14 12:55:37.354045 bilibili-live-0.8.3/src/bilibili_live/api/getDanmuInfo.py
--rw-rw-rw-   0        0        0     1025 2022-10-14 12:55:37.354045 bilibili-live-0.8.3/src/bilibili_live/api/getRoomInfo.py
--rw-rw-rw-   0        0        0      395 2022-10-14 12:55:37.354045 bilibili-live-0.8.3/src/bilibili_live/api/getUserInfo.py
--rw-rw-rw-   0        0        0      571 2022-10-14 12:55:37.354045 bilibili-live-0.8.3/src/bilibili_live/api/pullScanCodeStatus.py
--rw-rw-rw-   0        0        0     4748 2023-01-06 05:56:42.308983 bilibili-live-0.8.3/src/bilibili_live/bilibiliLive.py
--rw-rw-rw-   0        0        0      360 2022-10-14 12:55:37.354544 bilibili-live-0.8.3/src/bilibili_live/events/__init__.py
--rw-rw-rw-   0        0        0     2538 2023-01-06 06:56:15.902863 bilibili-live-0.8.3/src/bilibili_live/events/eventData.py
--rw-rw-rw-   0        0        0     1865 2023-01-05 17:40:08.230368 bilibili-live-0.8.3/src/bilibili_live/events/handler.py
--rw-rw-rw-   0        0        0     1626 2022-10-14 12:55:37.354544 bilibili-live-0.8.3/src/bilibili_live/login.py
--rw-rw-rw-   0        0        0      566 2023-01-06 06:56:15.902863 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/DANMU_MSG_to_Danmu.py
--rw-rw-rw-   0        0        0      766 2023-01-05 17:40:08.230868 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/ENTRY_EFFECT_to_User.py
--rw-rw-rw-   0        0        0      224 2022-12-05 13:57:24.664088 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/GUARD_BUY_to_User.py
--rw-rw-rw-   0        0        0      693 2023-01-06 07:30:34.018270 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/INTERACT_WORD_to_User.py
--rw-rw-rw-   0        0        0      968 2023-01-06 06:56:15.903363 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SEND_GIFT_to_Gift.py
--rw-rw-rw-   0        0        0     1015 2023-01-06 06:56:15.903363 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_JPN_to_SuperChat.py
--rw-rw-rw-   0        0        0      973 2023-01-06 06:56:15.903863 bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_to_SuperChat.py
--rw-rw-rw-   0        0        0       52 2022-10-14 12:55:37.356052 bilibili-live-0.8.3/src/bilibili_live/packageProcess/exceptions.py
--rw-rw-rw-   0        0        0    10689 2023-01-05 17:40:08.231368 bilibili-live-0.8.3/src/bilibili_live/packageProcess/packageProcessor.py
--rw-rw-rw-   0        0        0     3159 2022-10-14 12:55:37.356052 bilibili-live-0.8.3/src/bilibili_live/proto/proto.py
--rw-rw-rw-   0        0        0     1953 2023-01-06 07:34:14.691757 bilibili-live-0.8.3/PKG-INFO
+-rw-rw-rw-   0        0        0     1091 2022-09-05 05:50:45.230337 bilibili-live-0.9.0/LICENSE
+-rw-rw-rw-   0        0        0      637 2023-01-10 13:44:09.047362 bilibili-live-0.9.0/pyproject.toml
+-rw-rw-rw-   0        0        0     1724 2023-01-10 12:10:03.073507 bilibili-live-0.9.0/README.md
+-rw-rw-rw-   0        0        0       70 2022-09-06 07:24:04.218436 bilibili-live-0.9.0/src/bilibili_live/__init__.py
+-rw-rw-rw-   0        0        0      228 2022-09-28 05:37:26.406487 bilibili-live-0.9.0/src/bilibili_live/api/__init__.py
+-rw-rw-rw-   0        0        0      560 2022-09-28 05:37:26.407485 bilibili-live-0.9.0/src/bilibili_live/api/generateLoginQRCode.py
+-rw-rw-rw-   0        0        0      540 2022-09-28 05:37:26.407485 bilibili-live-0.9.0/src/bilibili_live/api/getDanmuInfo.py
+-rw-rw-rw-   0        0        0     1025 2022-09-28 05:37:26.407485 bilibili-live-0.9.0/src/bilibili_live/api/getRoomInfo.py
+-rw-rw-rw-   0        0        0      395 2022-09-28 05:37:26.408484 bilibili-live-0.9.0/src/bilibili_live/api/getUserInfo.py
+-rw-rw-rw-   0        0        0      571 2022-09-28 05:37:26.408484 bilibili-live-0.9.0/src/bilibili_live/api/pullScanCodeStatus.py
+-rw-rw-rw-   0        0        0     5673 2023-01-10 13:43:39.639975 bilibili-live-0.9.0/src/bilibili_live/bilibiliLive.py
+-rw-rw-rw-   0        0        0      360 2022-09-06 10:32:29.002022 bilibili-live-0.9.0/src/bilibili_live/events/__init__.py
+-rw-rw-rw-   0        0        0     2538 2023-01-10 12:10:03.075500 bilibili-live-0.9.0/src/bilibili_live/events/eventData.py
+-rw-rw-rw-   0        0        0     1946 2023-01-10 13:29:40.608714 bilibili-live-0.9.0/src/bilibili_live/events/handler.py
+-rw-rw-rw-   0        0        0     1626 2022-09-28 05:37:26.411484 bilibili-live-0.9.0/src/bilibili_live/login.py
+-rw-rw-rw-   0        0        0      566 2023-01-10 12:10:03.076287 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/DANMU_MSG_to_Danmu.py
+-rw-rw-rw-   0        0        0      766 2023-01-10 12:10:03.077299 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/ENTRY_EFFECT_to_User.py
+-rw-rw-rw-   0        0        0      224 2023-01-10 12:10:03.077299 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/GUARD_BUY_to_User.py
+-rw-rw-rw-   0        0        0      693 2023-01-10 12:10:03.077299 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/INTERACT_WORD_to_User.py
+-rw-rw-rw-   0        0        0      968 2023-01-10 12:10:03.078297 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SEND_GIFT_to_Gift.py
+-rw-rw-rw-   0        0        0     1015 2023-01-10 12:10:03.078297 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_JPN_to_SuperChat.py
+-rw-rw-rw-   0        0        0      973 2023-01-10 12:10:03.079298 bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_to_SuperChat.py
+-rw-rw-rw-   0        0        0       52 2022-09-06 02:37:14.580099 bilibili-live-0.9.0/src/bilibili_live/packageProcess/exceptions.py
+-rw-rw-rw-   0        0        0    10689 2023-01-10 12:10:03.079298 bilibili-live-0.9.0/src/bilibili_live/packageProcess/packageProcessor.py
+-rw-rw-rw-   0        0        0     3159 2022-09-06 06:04:26.243690 bilibili-live-0.9.0/src/bilibili_live/proto/proto.py
+-rw-rw-rw-   0        0        0     1953 2023-01-10 13:44:38.851688 bilibili-live-0.9.0/PKG-INFO
```

### Comparing `bilibili-live-0.8.3/LICENSE` & `bilibili-live-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/pyproject.toml` & `bilibili-live-0.9.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "bilibili-live"
-version = "0.8.3"
+version = "0.9.0"
 description = "哔哩哔哩直播间互动工具"
 authors = [
     { name = "Gedoy", email = "773673499@qq.com" },
 ]
 dependencies = [
     "requests>=2.28.1",
     "websockets>=10.3",
```

### Comparing `bilibili-live-0.8.3/README.md` & `bilibili-live-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/api/generateLoginQRCode.py` & `bilibili-live-0.9.0/src/bilibili_live/api/generateLoginQRCode.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/api/getDanmuInfo.py` & `bilibili-live-0.9.0/src/bilibili_live/api/getDanmuInfo.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/api/getRoomInfo.py` & `bilibili-live-0.9.0/src/bilibili_live/api/getRoomInfo.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/api/pullScanCodeStatus.py` & `bilibili-live-0.9.0/src/bilibili_live/api/pullScanCodeStatus.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/bilibiliLive.py` & `bilibili-live-0.9.0/src/bilibili_live/bilibiliLive.py`

 * *Files 14% similar despite different names*

```diff
@@ -7,61 +7,75 @@
 
 from bilibili_live import api
 
 from .events import Event
 from .events.handler import BilibiliLiveEventHandler
 from .packageProcess.exceptions import PackageConvertException
 from .packageProcess.packageProcessor import PackageProcessor
-from .proto.proto import BilibiliProto, BilibiliProtoException
+from .proto.proto import BilibiliLivePackage, BilibiliProto, BilibiliProtoException
 
 _bilibiliLive = {}
 
+
 class BilibiliLive:
     connected: asyncio.Event
     stop_sig: asyncio.Event
 
     package_queue: Queue
 
-    def __new__(cls, name='defaule'):
+    def __new__(cls, name="defaule"):
         if name in _bilibiliLive:
             return _bilibiliLive[name]
         else:
             obj = object.__new__(cls)
             _bilibiliLive[name] = obj
             return obj
 
     def __init__(self):
         def live_thread_run():
             def handle_thread_run():
                 while True:
                     package = self.package_queue.get()
                     try:
-                        self.handler.onPackage(Event(package=package))
-                        self.processor.process(package)
-                    except BilibiliProtoException as e:
-                        self.handler.onUnpackException(Event(package=package, data=e))
-                        self.handler.onException(e)
+                        if isinstance(package, BilibiliLivePackage):
+                            try:
+                                self.handler.onPackage(Event(package=package))
+                                self.processor.process(package)
+                            except BilibiliProtoException as e:
+                                self.package_queue.put(Event(package=package, data=e))
+                            except Exception as e:
+                                self.package_queue.put(e)
+                        elif isinstance(package, Event):
+                            self.handler.onUnpackException(package)
+                        elif package == "heart":
+                            self.handler.onHeart()
                     except Exception as e:
-                        self.handler.onException(e)
+                        self.package_queue.put(e)
+
+                    try:
+                        if isinstance(package, Exception):
+                            self.handler.onException(package)
+                    except Exception:
+                        ...
 
             handle_thread = Thread(target=handle_thread_run)
             handle_thread.setDaemon(True)
 
             self.loop = asyncio.new_event_loop()
             self.connected = asyncio.Event(loop=self.loop)
             self.stop_sig = asyncio.Event(loop=self.loop)
             self.package_queue = Queue()
-            
+
             handle_thread.start()
             self.loop.run_until_complete(self._start())
 
         self.live_thread = Thread(target=live_thread_run)
         self.live_thread.setDaemon(True)
 
-    def schedule(self, handler, short_id, heart_time = 30):
+    def schedule(self, handler, short_id, heart_time=30):
         self.handler: BilibiliLiveEventHandler = handler(self)
         self.processor: PackageProcessor = PackageProcessor(self.handler)
 
         self.room_info = api.getRoomInfo(short_id)
         self.danmu_info = api.getDanmuServerInfo(self.room_info.room_id)
         self.host = self.danmu_info.host_list[0]
 
@@ -74,24 +88,27 @@
     def stop(self):
         self.stop_sig.set()
 
     async def _check_stop(self):
         await self.stop_sig.wait()
 
     async def _start(self):
-        await self._connect()
-        await asyncio.wait([self._heart(), self._recv(), self._check_stop()], return_when=asyncio.FIRST_COMPLETED)
+        await asyncio.wait(
+            [self._connect(), self._heart(), self._recv(), self._check_stop()], return_when=asyncio.FIRST_COMPLETED
+        )
 
     async def _connect(self):
         while True:
+            if self.connected.is_set():
+                await asyncio.sleep(1)
+                continue
             try:
                 self.websocket = await websockets.connect(f"wss://{self.host.host}:{self.host.wss_port}/sub")
                 await self._auth()
                 self.connected.set()
-                return
             except ConnectionRefusedError:
                 await asyncio.sleep(1)
 
     async def _auth(self):
         auth_proto = BilibiliProto()
         auth_proto.body = json.dumps(
             {
@@ -105,32 +122,36 @@
         )
         auth_proto.op = BilibiliProto.OP_AUTH
         await self.websocket.send(auth_proto.pack())
 
     async def _heart(self):
         while True:
             try:
+                await self.connected.wait()
                 await self.websocket.send(BilibiliProto().pack())
-                self.handler.onHeart()
+                self.package_queue.put("heart")
                 await asyncio.sleep(self.heart_time)
+            except websockets.exceptions.ConnectionClosedError as e:
+                self.package_queue.put(e)
+                await asyncio.sleep(1)
+                self.connected.clear()
             except Exception as e:
-                self.handler.onException(e)
+                self.package_queue.put(e)
 
     async def _recv(self):
         while True:
             try:
                 await self.connected.wait()
                 recv = await self.websocket.recv()
                 packages = BilibiliProto.unpack(recv)
                 for package in packages:
                     self.package_queue.put(package)
-            except websockets.exceptions.ConnectionClosedError:
+            except websockets.exceptions.ConnectionClosedError as e:
+                self.package_queue.put(e)
                 self.connected.clear()
-                await self._connect()
             except BilibiliProtoException as e:
-                self.handler.onException(e)
-                self.handler.onUnpackException(Event(package, data=e))
+                self.package_queue.put(Event(package, data=e))
             except PackageConvertException as e:
-                self.handler.onUnpackException(Event(package, data=e))
+                self.package_queue.put(Event(package, data=e))
             except Exception as e:
-                self.handler.onException(e)
+                self.package_queue.put(e)
                 ...
```

### Comparing `bilibili-live-0.8.3/src/bilibili_live/events/eventData.py` & `bilibili-live-0.9.0/src/bilibili_live/events/eventData.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/events/handler.py` & `bilibili-live-0.9.0/src/bilibili_live/events/handler.py`

 * *Files 2% similar despite different names*

```diff
@@ -51,11 +51,11 @@
     def onSuperChat(self, event: Event[SuperChat]):
         """收到醒目留言，包括日语留言"""
 
     def onUnpackException(self, event: Event[BilibiliProtoException]):
         """解包消息过程出现异常"""
 
     def onException(self, exception: Exception):
-        """出现异常"""
+        """出现异常。其他事件或内部抛出异常将触发，此方法抛出异常将被忽略"""
 
     def onNotProcessPackage(self, event: Event[None]):
         """未处理的包"""
```

### Comparing `bilibili-live-0.8.3/src/bilibili_live/login.py` & `bilibili-live-0.9.0/src/bilibili_live/login.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/DANMU_MSG_to_Danmu.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/DANMU_MSG_to_Danmu.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/ENTRY_EFFECT_to_User.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/ENTRY_EFFECT_to_User.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/INTERACT_WORD_to_User.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/INTERACT_WORD_to_User.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SEND_GIFT_to_Gift.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SEND_GIFT_to_Gift.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_JPN_to_SuperChat.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_JPN_to_SuperChat.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_to_SuperChat.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/convert/SUPER_CHAT_MESSAGE_to_SuperChat.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/packageProcess/packageProcessor.py` & `bilibili-live-0.9.0/src/bilibili_live/packageProcess/packageProcessor.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/src/bilibili_live/proto/proto.py` & `bilibili-live-0.9.0/src/bilibili_live/proto/proto.py`

 * *Files identical despite different names*

### Comparing `bilibili-live-0.8.3/PKG-INFO` & `bilibili-live-0.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bilibili-live
-Version: 0.8.3
+Version: 0.9.0
 Summary: 哔哩哔哩直播间互动工具
 License: MIT
 Author-email: Gedoy <773673499@qq.com>
 Requires-Python: >=3.7
 Project-URL: repository, https://github.com/Gedoy9793/bilibili-live
 Description-Content-Type: text/markdown
```

