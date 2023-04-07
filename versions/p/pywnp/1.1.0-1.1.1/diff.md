# Comparing `tmp/pywnp-1.1.0.tar.gz` & `tmp/pywnp-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pywnp-1.1.0.tar", last modified: Fri Apr  7 04:47:48 2023, max compression
+gzip compressed data, was "pywnp-1.1.1.tar", last modified: Fri Apr  7 10:53:12 2023, max compression
```

## Comparing `pywnp-1.1.0.tar` & `pywnp-1.1.1.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 04:47:48.950752 pywnp-1.1.0/
--rw-rw-rw-   0        0        0     1060 2023-03-20 18:31:19.000000 pywnp-1.1.0/LICENSE
--rw-rw-rw-   0        0        0     5353 2023-04-07 04:47:48.949755 pywnp-1.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     3627 2023-03-30 12:26:36.000000 pywnp-1.1.0/README.md
--rw-rw-rw-   0        0        0      669 2023-04-07 04:47:27.000000 pywnp-1.1.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 04:47:48.950752 pywnp-1.1.0/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 04:47:48.930726 pywnp-1.1.0/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 04:47:48.933724 pywnp-1.1.0/src/pywnp/
--rw-rw-rw-   0        0        0       27 2023-03-20 19:19:07.000000 pywnp-1.1.0/src/pywnp/__init__.py
--rw-rw-rw-   0        0        0    10528 2023-04-07 04:45:38.000000 pywnp-1.1.0/src/pywnp/pywnp.py
-drwxrwxrwx   0        0        0        0 2023-04-07 04:47:48.948752 pywnp-1.1.0/src/pywnp.egg-info/
--rw-rw-rw-   0        0        0     5353 2023-04-07 04:47:48.000000 pywnp-1.1.0/src/pywnp.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      237 2023-04-07 04:47:48.000000 pywnp-1.1.0/src/pywnp.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 04:47:48.000000 pywnp-1.1.0/src/pywnp.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       11 2023-04-07 04:47:48.000000 pywnp-1.1.0/src/pywnp.egg-info/requires.txt
--rw-rw-rw-   0        0        0        6 2023-04-07 04:47:48.000000 pywnp-1.1.0/src/pywnp.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 10:53:12.688375 pywnp-1.1.1/
+-rw-rw-rw-   0        0        0     1060 2023-03-20 18:31:19.000000 pywnp-1.1.1/LICENSE
+-rw-rw-rw-   0        0        0     5353 2023-04-07 10:53:12.687376 pywnp-1.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3627 2023-03-30 12:26:36.000000 pywnp-1.1.1/README.md
+-rw-rw-rw-   0        0        0      669 2023-04-07 10:52:53.000000 pywnp-1.1.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 10:53:12.688375 pywnp-1.1.1/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 10:53:12.669345 pywnp-1.1.1/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 10:53:12.671860 pywnp-1.1.1/src/pywnp/
+-rw-rw-rw-   0        0        0       27 2023-03-20 19:19:07.000000 pywnp-1.1.1/src/pywnp/__init__.py
+-rw-rw-rw-   0        0        0    10531 2023-04-07 09:23:15.000000 pywnp-1.1.1/src/pywnp/pywnp.py
+drwxrwxrwx   0        0        0        0 2023-04-07 10:53:12.687376 pywnp-1.1.1/src/pywnp.egg-info/
+-rw-rw-rw-   0        0        0     5353 2023-04-07 10:53:12.000000 pywnp-1.1.1/src/pywnp.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      237 2023-04-07 10:53:12.000000 pywnp-1.1.1/src/pywnp.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 10:53:12.000000 pywnp-1.1.1/src/pywnp.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 10:53:12.000000 pywnp-1.1.1/src/pywnp.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 10:53:12.000000 pywnp-1.1.1/src/pywnp.egg-info/top_level.txt
```

### Comparing `pywnp-1.1.0/LICENSE` & `pywnp-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pywnp-1.1.0/PKG-INFO` & `pywnp-1.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pywnp
-Version: 1.1.0
+Version: 1.1.1
 Summary: A python library to communicate with the WebNowPlaying-Redux browser extension
 Author-email: keifufu <keifufu@noonly.net>
 License: Copyright 2023 keifufu
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
         
         The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```

### Comparing `pywnp-1.1.0/README.md` & `pywnp-1.1.1/README.md`

 * *Files identical despite different names*

### Comparing `pywnp-1.1.0/pyproject.toml` & `pywnp-1.1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "pywnp"
-version = "1.1.0"
+version = "1.1.1"
 description = "A python library to communicate with the WebNowPlaying-Redux browser extension"
 authors = [ { name="keifufu", email="keifufu@noonly.net" } ]
 readme = "README.md"
 license = { file = "LICENSE" }
 keywords = [ "webnowplaying", "wnp", "youtube", "spotify", "media", "music" ]
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pywnp-1.1.0/src/pywnp/pywnp.py` & `pywnp-1.1.1/src/pywnp/pywnp.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 import asyncio
 import websockets
 from datetime import datetime
 from threading import Thread
-import time
 import json
 
 class MediaInfo:
   def __init__(self):
     self._Title = ''
     self._State = 'STOPPED'
     self._Volume = 0
@@ -171,16 +170,15 @@
       async def close():
         WNPRedux._server.close()
         await WNPRedux._server.wait_closed()
 
       closed = asyncio.run_coroutine_threadsafe(close(), WNPRedux._loop)
       closed.result(timeout=1.0)
       WNPRedux._loop.stop()
-    except Exception as e:
-      print(e)
+    except: pass
 
   async def _onConnect(websocket):
     WNPRedux._clients.add(websocket)
     WNPRedux.clients = len(WNPRedux._clients)
     websocket.id = str(datetime.now())
     await websocket.send(f'ADAPTER_VERSION {WNPRedux._version};WNPRLIB_REVISION 1')
     try:
@@ -261,14 +259,15 @@
       WNPRedux.clients = len(WNPRedux._clients)
       WNPRedux._recipients.discard(websocket.id)
       for mediaInfo in WNPRedux._mediaInfoDictionary:
         if mediaInfo.WebSocketID == websocket.id:
           WNPRedux._mediaInfoDictionary.remove(mediaInfo)
           break
       WNPRedux._UpdateMediaInfo()
+      await WNPRedux._updateRecipients()
   
   def _UpdateMediaInfo():
     WNPRedux._mediaInfoDictionary = sorted(WNPRedux._mediaInfoDictionary, key=lambda x: x.Timestamp, reverse=True)
     suitableMatch = False
 
     for mediaInfo in WNPRedux._mediaInfoDictionary:
       if mediaInfo.State == 'PLAYING' and mediaInfo.Volume > 0:
```

### Comparing `pywnp-1.1.0/src/pywnp.egg-info/PKG-INFO` & `pywnp-1.1.1/src/pywnp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pywnp
-Version: 1.1.0
+Version: 1.1.1
 Summary: A python library to communicate with the WebNowPlaying-Redux browser extension
 Author-email: keifufu <keifufu@noonly.net>
 License: Copyright 2023 keifufu
         
         Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
         
         The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```

