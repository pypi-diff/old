# Comparing `tmp/aioca-1.5.1.tar.gz` & `tmp/aioca-1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/aioca/aioca/dist/tmptor3mz7n/aioca-1.5.1.tar", last modified: Mon Dec  5 14:26:37 2022, max compression
+gzip compressed data, was "/home/runner/work/aioca/aioca/dist/tmpk85jzoav/aioca-1.6.tar", last modified: Thu Apr  6 14:27:37 2023, max compression
```

## Comparing `aioca-1.5.1.tar` & `aioca-1.6.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxr-x   0 runner    (1001) docker     (122)        0 2022-12-05 14:26:37.000000 aioca-1.5.1/
--rw-rw-r--   0 runner    (1001) docker     (122)     3235 2022-12-05 14:26:37.000000 aioca-1.5.1/PKG-INFO
--rw-rw-r--   0 runner    (1001) docker     (122)     2069 2022-12-05 14:25:51.000000 aioca-1.5.1/README.rst
-drwxrwxr-x   0 runner    (1001) docker     (122)        0 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca/
--rw-rw-r--   0 runner    (1001) docker     (122)     2533 2022-12-05 14:25:51.000000 aioca-1.5.1/aioca/__init__.py
--rw-rw-r--   0 runner    (1001) docker     (122)    38776 2022-12-05 14:25:51.000000 aioca-1.5.1/aioca/_catools.py
--rw-rw-r--   0 runner    (1001) docker     (122)     3758 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca/_version_git.py
--rw-rw-r--   0 runner    (1001) docker     (122)     8396 2022-12-05 14:25:51.000000 aioca-1.5.1/aioca/types.py
-drwxrwxr-x   0 runner    (1001) docker     (122)        0 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/
--rw-rw-r--   0 runner    (1001) docker     (122)     3235 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/PKG-INFO
--rw-rw-r--   0 runner    (1001) docker     (122)      261 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/SOURCES.txt
--rw-rw-r--   0 runner    (1001) docker     (122)        1 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/dependency_links.txt
--rw-rw-r--   0 runner    (1001) docker     (122)      216 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/requires.txt
--rw-rw-r--   0 runner    (1001) docker     (122)        6 2022-12-05 14:26:37.000000 aioca-1.5.1/aioca.egg-info/top_level.txt
--rw-rw-r--   0 runner    (1001) docker     (122)      173 2022-12-05 14:25:51.000000 aioca-1.5.1/pyproject.toml
--rw-rw-r--   0 runner    (1001) docker     (122)     1548 2022-12-05 14:26:37.000000 aioca-1.5.1/setup.cfg
--rw-rw-r--   0 runner    (1001) docker     (122)      386 2022-12-05 14:25:51.000000 aioca-1.5.1/setup.py
+drwxrwxr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:27:37.000000 aioca-1.6/
+-rw-rw-r--   0 runner    (1001) docker     (123)     3233 2023-04-06 14:27:37.000000 aioca-1.6/PKG-INFO
+-rw-rw-r--   0 runner    (1001) docker     (123)     2069 2023-04-06 14:26:34.000000 aioca-1.6/README.rst
+drwxrwxr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:27:37.000000 aioca-1.6/aioca/
+-rw-rw-r--   0 runner    (1001) docker     (123)     2533 2023-04-06 14:26:34.000000 aioca-1.6/aioca/__init__.py
+-rw-rw-r--   0 runner    (1001) docker     (123)    39834 2023-04-06 14:26:34.000000 aioca-1.6/aioca/_catools.py
+-rw-rw-r--   0 runner    (1001) docker     (123)     3756 2023-04-06 14:27:37.000000 aioca-1.6/aioca/_version_git.py
+-rw-rw-r--   0 runner    (1001) docker     (123)     8396 2023-04-06 14:26:34.000000 aioca-1.6/aioca/types.py
+drwxrwxr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/
+-rw-rw-r--   0 runner    (1001) docker     (123)     3233 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/PKG-INFO
+-rw-rw-r--   0 runner    (1001) docker     (123)      261 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/SOURCES.txt
+-rw-rw-r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/dependency_links.txt
+-rw-rw-r--   0 runner    (1001) docker     (123)      216 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/requires.txt
+-rw-rw-r--   0 runner    (1001) docker     (123)        6 2023-04-06 14:27:37.000000 aioca-1.6/aioca.egg-info/top_level.txt
+-rw-rw-r--   0 runner    (1001) docker     (123)      173 2023-04-06 14:26:34.000000 aioca-1.6/pyproject.toml
+-rw-rw-r--   0 runner    (1001) docker     (123)     1548 2023-04-06 14:27:37.000000 aioca-1.6/setup.cfg
+-rw-rw-r--   0 runner    (1001) docker     (123)      386 2023-04-06 14:26:34.000000 aioca-1.6/setup.py
```

### Comparing `aioca-1.5.1/PKG-INFO` & `aioca-1.6/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aioca
-Version: 1.5.1
+Version: 1.6
 Summary: Asynchronous Channel Access client for asyncio and Python using libca via ctypes
 Home-page: https://github.com/dls-controls/aioca
 Author: Tom Cobb
 Author-email: tom.cobb@diamond.ac.uk
 License: Apache License 2.0
 Description: aioca
         =====
```

### Comparing `aioca-1.5.1/README.rst` & `aioca-1.6/README.rst`

 * *Files identical despite different names*

### Comparing `aioca-1.5.1/aioca/__init__.py` & `aioca-1.6/aioca/__init__.py`

 * *Files identical despite different names*

### Comparing `aioca-1.5.1/aioca/_catools.py` & `aioca-1.6/aioca/_catools.py`

 * *Files 6% similar despite different names*

```diff
@@ -30,14 +30,24 @@
 from .types import AugmentedValue, Count, Datatype, Dbe, Format, Timeout
 
 T = TypeVar("T")
 PVs = Union[List[str], Tuple[str, ...]]
 
 DEFAULT_TIMEOUT = 5.0
 
+# patch into epicscorelibs.ca.cadef
+cadef.ca_current_context = cadef.libca.ca_current_context
+cadef.ca_current_context.restype = ctypes.c_void_p
+
+cadef.ca_attach_context = cadef.libca.ca_attach_context
+cadef.ca_attach_context.argtypes = [ctypes.c_void_p]
+cadef.ca_attach_context.errcheck = cadef.expect_ECA_NORMAL
+
+cadef.ca_detach_context = cadef.libca.ca_detach_context
+
 
 class ValueEvent(Generic[T]):
     def __init__(self) -> None:
         self.value: Union[T, Exception] = RuntimeError("No value set")
         self._event = asyncio.Event()
 
     def set(self, value: Union[T, Exception]):
@@ -996,36 +1006,64 @@
 
 
 # ----------------------------------------------------------------------------
 #   CA Context manager
 
 
 class _Context:
-    created = False
+    _ca_available = False
+    _ca_context = None
     _channel_caches: Dict[asyncio.AbstractEventLoop, ChannelCache] = {}
 
     @classmethod
     def purge_channel_caches(cls):
         """Remove cached channel connections. This will close all subscriptions"""
         for channel_cache in cls._channel_caches.values():
             channel_cache.purge()
         cls._channel_caches.clear()
 
     @classmethod
+    def _ensure_context(cls):
+        if not cls._ca_available:
+            if not cadef.ca_current_context():
+                # There is no CA context available for us to use, make one
+                cadef.ca_context_create(1)
+                # EPICS Channel Access event dispatching needs to done with a little
+                # care.  In previous versions the solution was to repeatedly call
+                # ca_pend_event() in polling mode, but this does not appear to be
+                # efficient enough when receiving large amounts of data.  Instead we
+                # enable preemptive Channel Access callbacks, which means we need to
+                # cope with all of our channel access events occuring
+                # asynchronously.
+                cls._ca_context = cadef.ca_current_context()
+            cls._ca_available = True
+            atexit.register(cls._destroy_context)
+
+    @classmethod
+    def _destroy_context(cls):  # pragma: no cover
+        # On exit we do our best to ensure that channel access shuts down cleanly.
+        # We do this by shutting down all channels and clearing the channel access
+        # context: this should reduce the risk of unexpected errors during
+        # application exit.
+        #    One reason that it's rather important to do this properly is that we
+        # can't safely do *any* ca_ calls once ca_context_destroy() is called!
+        cls.purge_channel_caches()
+        if cls._ca_context:
+            # Make sure we are attached to that context
+            cadef.ca_detach_context()
+            cadef.ca_attach_context(cls._ca_context)
+            # Then destroy it
+            cadef.ca_context_destroy()
+            cadef.ca_detach_context()
+            cls._ca_context = None
+        cls._ca_available = False
+
+    @classmethod
     def get_channel_cache(cls):
-        if not cls.created:
-            # EPICS Channel Access event dispatching needs to done with a little
-            # care.  In previous versions the solution was to repeatedly call
-            # ca_pend_event() in polling mode, but this does not appear to be
-            # efficient enough when receiving large amounts of data.  Instead we
-            # enable preemptive Channel Access callbacks, which means we need to
-            # cope with all of our channel access events occuring
-            # asynchronously.
-            cadef.ca_context_create(1)
-            cls.created = True
+        cls._ensure_context()
         loop = asyncio.get_event_loop()
         try:
             channel_cache = cls._channel_caches[loop]
         except KeyError:
             # Channel from new event loop. Don't support multiple event loops, so
             # clear out all the old channels
             cls.purge_channel_caches()
@@ -1039,28 +1077,14 @@
 
 def get_channel(pv: str) -> Channel:
     channel_cache = _Context.get_channel_cache()
     channel = channel_cache.get_channel(pv)
     return channel
 
 
-@atexit.register
-def _catools_atexit():  # pragma: no cover
-    # On exit we do our best to ensure that channel access shuts down cleanly.
-    # We do this by shutting down all channels and clearing the channel access
-    # context: this should reduce the risk of unexpected errors during
-    # application exit.
-    #    One reason that it's rather important to do this properly is that we
-    # can't safely do *any* ca_ calls once ca_context_destroy() is called!
-    purge_channel_caches()
-    if _Context.created:
-        cadef.ca_flush_io()
-        cadef.ca_context_destroy()
-
-
 # Another delicacy arising from relying on asynchronous CA event dispatching is
 # that we need to manually flush IO events such as caget commands.  To ensure
 # that large blocks of channel access activity really are aggregated we used to
 # ensure that ca_flush_io() is only called once in any scheduling cycle, but now
 # we just call it every time
 _flush_io = cadef.ca_flush_io
```

### Comparing `aioca-1.5.1/aioca/_version_git.py` & `aioca-1.6/aioca/_version_git.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 # versiongit-0.6 (https://github.com/dls-controls/versiongit)
 import os
 import re
 import sys
 from subprocess import STDOUT, CalledProcessError, check_output
 
 # These will be filled in if git archive is run or by setup.py cmdclasses
-GIT_REFS = 'tag: 1.5.1'
-GIT_SHA1 = '82f881a'
+GIT_REFS = 'tag: 1.6'
+GIT_SHA1 = 'a5500d0'
 
 
 def get_version_from_git(path=None):
     """Try to parse version from git describe, fallback to git archive tags"""
     tag, plus, suffix = "0", "untagged", ""
     if not GIT_SHA1.startswith("$"):
         # git archive or the cmdclasses below have filled in these strings
```

### Comparing `aioca-1.5.1/aioca/types.py` & `aioca-1.6/aioca/types.py`

 * *Files identical despite different names*

### Comparing `aioca-1.5.1/aioca.egg-info/PKG-INFO` & `aioca-1.6/aioca.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aioca
-Version: 1.5.1
+Version: 1.6
 Summary: Asynchronous Channel Access client for asyncio and Python using libca via ctypes
 Home-page: https://github.com/dls-controls/aioca
 Author: Tom Cobb
 Author-email: tom.cobb@diamond.ac.uk
 License: Apache License 2.0
 Description: aioca
         =====
```

### Comparing `aioca-1.5.1/setup.cfg` & `aioca-1.6/setup.cfg`

 * *Files identical despite different names*

