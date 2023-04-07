# Comparing `tmp/pomice-2.4.0.tar.gz` & `tmp/pomice-2.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pomice-2.4.0.tar", last modified: Thu Apr  6 03:01:14 2023, max compression
+gzip compressed data, was "pomice-2.4.1.tar", last modified: Fri Apr  7 00:28:52 2023, max compression
```

## Comparing `pomice-2.4.0.tar` & `pomice-2.4.1.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 03:01:14.653844 pomice-2.4.0/
--rw-rw-rw-   0        0        0    35823 2021-09-25 18:02:32.000000 pomice-2.4.0/LICENSE
--rw-rw-rw-   0        0        0     5445 2023-04-06 03:01:14.652523 pomice-2.4.0/PKG-INFO
--rw-rw-rw-   0        0        0     4680 2023-04-06 02:52:29.000000 pomice-2.4.0/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 03:01:14.623019 pomice-2.4.0/pomice/
--rw-rw-rw-   0        0        0      853 2023-04-06 02:59:42.000000 pomice-2.4.0/pomice/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 03:01:14.649062 pomice-2.4.0/pomice/applemusic/
--rw-rw-rw-   0        0        0      151 2023-03-11 15:22:18.000000 pomice-2.4.0/pomice/applemusic/__init__.py
--rw-rw-rw-   0        0        0     6107 2023-03-27 04:08:42.000000 pomice-2.4.0/pomice/applemusic/client.py
--rw-rw-rw-   0        0        0      321 2023-03-11 15:22:18.000000 pomice-2.4.0/pomice/applemusic/exceptions.py
--rw-rw-rw-   0        0        0     3573 2023-03-11 15:28:02.000000 pomice-2.4.0/pomice/applemusic/objects.py
--rw-rw-rw-   0        0        0     8145 2023-03-27 02:36:38.000000 pomice-2.4.0/pomice/enums.py
--rw-rw-rw-   0        0        0     6038 2023-03-13 23:36:22.000000 pomice-2.4.0/pomice/events.py
--rw-rw-rw-   0        0        0     2746 2023-03-12 15:44:18.000000 pomice-2.4.0/pomice/exceptions.py
--rw-rw-rw-   0        0        0    14832 2023-03-11 15:25:46.000000 pomice-2.4.0/pomice/filters.py
--rw-rw-rw-   0        0        0     5302 2023-04-05 02:18:43.000000 pomice-2.4.0/pomice/objects.py
--rw-rw-rw-   0        0        0    23826 2023-04-06 02:04:37.000000 pomice-2.4.0/pomice/player.py
--rw-rw-rw-   0        0        0    34773 2023-04-06 02:57:31.000000 pomice-2.4.0/pomice/pool.py
--rw-rw-rw-   0        0        0        0 2023-03-10 02:46:40.000000 pomice-2.4.0/pomice/py.typed
--rw-rw-rw-   0        0        0    12184 2023-03-27 02:26:04.000000 pomice-2.4.0/pomice/queue.py
--rw-rw-rw-   0        0        0     1069 2023-03-11 15:22:18.000000 pomice-2.4.0/pomice/routeplanner.py
-drwxrwxrwx   0        0        0        0 2023-04-06 03:01:14.652523 pomice-2.4.0/pomice/spotify/
--rw-rw-rw-   0        0        0      147 2023-03-11 15:22:18.000000 pomice-2.4.0/pomice/spotify/__init__.py
--rw-rw-rw-   0        0        0     6522 2023-03-27 04:08:42.000000 pomice-2.4.0/pomice/spotify/client.py
--rw-rw-rw-   0        0        0      301 2023-03-11 15:22:18.000000 pomice-2.4.0/pomice/spotify/exceptions.py
--rw-rw-rw-   0        0        0     3445 2023-04-05 02:18:43.000000 pomice-2.4.0/pomice/spotify/objects.py
--rw-rw-rw-   0        0        0     8697 2023-03-13 02:58:40.000000 pomice-2.4.0/pomice/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-06 03:01:14.644683 pomice-2.4.0/pomice.egg-info/
--rw-rw-rw-   0        0        0     5445 2023-04-06 03:01:14.000000 pomice-2.4.0/pomice.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      628 2023-04-06 03:01:14.000000 pomice-2.4.0/pomice.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 03:01:14.000000 pomice-2.4.0/pomice.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       43 2023-04-06 03:01:14.000000 pomice-2.4.0/pomice.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-04-06 03:01:14.000000 pomice-2.4.0/pomice.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      369 2023-03-13 23:16:18.000000 pomice-2.4.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 03:01:14.653844 pomice-2.4.0/setup.cfg
--rw-rw-rw-   0        0        0     2192 2023-03-13 23:27:32.000000 pomice-2.4.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 00:28:52.259773 pomice-2.4.1/
+-rw-rw-rw-   0        0        0    35823 2021-09-25 18:02:32.000000 pomice-2.4.1/LICENSE
+-rw-rw-rw-   0        0        0     5445 2023-04-07 00:28:52.259773 pomice-2.4.1/PKG-INFO
+-rw-rw-rw-   0        0        0     4680 2023-04-06 02:52:29.000000 pomice-2.4.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 00:28:52.187768 pomice-2.4.1/pomice/
+-rw-rw-rw-   0        0        0      853 2023-04-07 00:28:12.000000 pomice-2.4.1/pomice/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 00:28:52.235155 pomice-2.4.1/pomice/applemusic/
+-rw-rw-rw-   0        0        0      151 2023-03-11 15:22:18.000000 pomice-2.4.1/pomice/applemusic/__init__.py
+-rw-rw-rw-   0        0        0     6107 2023-03-27 04:08:42.000000 pomice-2.4.1/pomice/applemusic/client.py
+-rw-rw-rw-   0        0        0      321 2023-03-11 15:22:18.000000 pomice-2.4.1/pomice/applemusic/exceptions.py
+-rw-rw-rw-   0        0        0     3573 2023-03-11 15:28:02.000000 pomice-2.4.1/pomice/applemusic/objects.py
+-rw-rw-rw-   0        0        0     8145 2023-03-27 02:36:38.000000 pomice-2.4.1/pomice/enums.py
+-rw-rw-rw-   0        0        0     6038 2023-03-13 23:36:22.000000 pomice-2.4.1/pomice/events.py
+-rw-rw-rw-   0        0        0     2746 2023-03-12 15:44:18.000000 pomice-2.4.1/pomice/exceptions.py
+-rw-rw-rw-   0        0        0    14832 2023-03-11 15:25:46.000000 pomice-2.4.1/pomice/filters.py
+-rw-rw-rw-   0        0        0     5302 2023-04-05 02:18:43.000000 pomice-2.4.1/pomice/objects.py
+-rw-rw-rw-   0        0        0    23531 2023-04-07 00:27:42.000000 pomice-2.4.1/pomice/player.py
+-rw-rw-rw-   0        0        0    34773 2023-04-06 02:57:31.000000 pomice-2.4.1/pomice/pool.py
+-rw-rw-rw-   0        0        0        0 2023-03-10 02:46:40.000000 pomice-2.4.1/pomice/py.typed
+-rw-rw-rw-   0        0        0    12184 2023-03-27 02:26:04.000000 pomice-2.4.1/pomice/queue.py
+-rw-rw-rw-   0        0        0     1069 2023-03-11 15:22:18.000000 pomice-2.4.1/pomice/routeplanner.py
+drwxrwxrwx   0        0        0        0 2023-04-07 00:28:52.257750 pomice-2.4.1/pomice/spotify/
+-rw-rw-rw-   0        0        0      147 2023-03-11 15:22:18.000000 pomice-2.4.1/pomice/spotify/__init__.py
+-rw-rw-rw-   0        0        0     6522 2023-03-27 04:08:42.000000 pomice-2.4.1/pomice/spotify/client.py
+-rw-rw-rw-   0        0        0      301 2023-03-11 15:22:18.000000 pomice-2.4.1/pomice/spotify/exceptions.py
+-rw-rw-rw-   0        0        0     3445 2023-04-05 02:18:43.000000 pomice-2.4.1/pomice/spotify/objects.py
+-rw-rw-rw-   0        0        0     8697 2023-03-13 02:58:40.000000 pomice-2.4.1/pomice/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 00:28:52.207923 pomice-2.4.1/pomice.egg-info/
+-rw-rw-rw-   0        0        0     5445 2023-04-07 00:28:52.000000 pomice-2.4.1/pomice.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      628 2023-04-07 00:28:52.000000 pomice-2.4.1/pomice.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 00:28:52.000000 pomice-2.4.1/pomice.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       43 2023-04-07 00:28:52.000000 pomice-2.4.1/pomice.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 00:28:52.000000 pomice-2.4.1/pomice.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      369 2023-03-13 23:16:18.000000 pomice-2.4.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 00:28:52.259773 pomice-2.4.1/setup.cfg
+-rw-rw-rw-   0        0        0     2192 2023-03-13 23:27:32.000000 pomice-2.4.1/setup.py
```

### Comparing `pomice-2.4.0/LICENSE` & `pomice-2.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/PKG-INFO` & `pomice-2.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pomice
-Version: 2.4.0
+Version: 2.4.1
 Summary: The modern Lavalink wrapper designed for Discord.py
 Home-page: https://github.com/cloudwithax/pomice
 Author: cloudwithax
 License: GPL
 Keywords: pomice,lavalink,discord.py
 Classifier: Framework :: AsyncIO
 Classifier: Operating System :: OS Independent
```

### Comparing `pomice-2.4.0/README.md` & `pomice-2.4.1/README.md`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/__init__.py` & `pomice-2.4.1/pomice/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 
     raise DiscordPyOutdated(
         "You must have discord.py (v2.0 or greater) to use this library. "
         "Uninstall your current version and install discord.py 2.0 "
         "using 'pip install discord.py'",
     )
 
-__version__ = "2.4.0"
+__version__ = "2.4.1"
 __title__ = "pomice"
 __author__ = "cloudwithax"
 __license__ = "GPL-3.0"
 __copyright__ = "Copyright (c) 2023, cloudwithax"
 
 from .enums import *
 from .events import *
```

### Comparing `pomice-2.4.0/pomice/applemusic/client.py` & `pomice-2.4.1/pomice/applemusic/client.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/applemusic/objects.py` & `pomice-2.4.1/pomice/applemusic/objects.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/enums.py` & `pomice-2.4.1/pomice/enums.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/events.py` & `pomice-2.4.1/pomice/events.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/exceptions.py` & `pomice-2.4.1/pomice/exceptions.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/filters.py` & `pomice-2.4.1/pomice/filters.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/objects.py` & `pomice-2.4.1/pomice/objects.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/player.py` & `pomice-2.4.1/pomice/player.py`

 * *Files 1% similar despite different names*

```diff
@@ -345,15 +345,15 @@
         self._player_endpoint_uri = f"sessions/{self._node._session_id}/players"
 
         await self._dispatch_voice_update()
         await self._node.send(
             method="PATCH",
             path=self._player_endpoint_uri,
             guild_id=self._guild.id,
-            data=data,
+            data=data or None,
         )
 
         self._log.debug(f"Swapped all players to new node {new_node._identifier}.")
 
     async def get_tracks(
         self,
         query: str,
@@ -570,31 +570,22 @@
             data={"volume": volume},
         )
         self._volume = volume
 
         self._log.debug(f"Player volume has been adjusted to {volume}")
         return self._volume
 
-    async def move_to(self, *, channel: VoiceChannel) -> None:
+    async def move_to(self, channel: VoiceChannel) -> None:
         """Moves the player to a new voice channel."""
 
-        if self.current:
-            data: dict = {"position": self.position, "encodedTrack": self.current.track_id}
-
         await self.guild.change_voice_state(channel=channel)
 
         self.channel = channel
 
         await self._dispatch_voice_update()
-        await self._node.send(
-            method="PATCH",
-            path=self._player_endpoint_uri,
-            guild_id=self._guild.id,
-            data=data,
-        )
 
     async def add_filter(self, _filter: Filter, fast_apply: bool = False) -> Filters:
         """Adds a filter to the player. Takes a pomice.Filter object.
         This will only work if you are using a version of Lavalink that supports filters.
         If you would like for the filter to apply instantly, set the `fast_apply` arg to `True`.
 
         (You must have a song playing in order for `fast_apply` to work.)
```

### Comparing `pomice-2.4.0/pomice/pool.py` & `pomice-2.4.1/pomice/pool.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/queue.py` & `pomice-2.4.1/pomice/queue.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/routeplanner.py` & `pomice-2.4.1/pomice/routeplanner.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/spotify/client.py` & `pomice-2.4.1/pomice/spotify/client.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/spotify/objects.py` & `pomice-2.4.1/pomice/spotify/objects.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice/utils.py` & `pomice-2.4.1/pomice/utils.py`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/pomice.egg-info/PKG-INFO` & `pomice-2.4.1/pomice.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pomice
-Version: 2.4.0
+Version: 2.4.1
 Summary: The modern Lavalink wrapper designed for Discord.py
 Home-page: https://github.com/cloudwithax/pomice
 Author: cloudwithax
 License: GPL
 Keywords: pomice,lavalink,discord.py
 Classifier: Framework :: AsyncIO
 Classifier: Operating System :: OS Independent
```

### Comparing `pomice-2.4.0/pomice.egg-info/SOURCES.txt` & `pomice-2.4.1/pomice.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pomice-2.4.0/setup.py` & `pomice-2.4.1/setup.py`

 * *Files identical despite different names*

