# Comparing `tmp/ypy_websocket-0.8.4.tar.gz` & `tmp/ypy_websocket-0.9.0.tar.gz`

## Comparing `ypy_websocket-0.8.4.tar` & `ypy_websocket-0.9.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1096 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/conftest.py
--rw-r--r--   0        0        0       76 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/package.json
--rw-r--r--   0        0        0     2322 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/test_ypy_yjs.py
--rw-r--r--   0        0        0     3007 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/test_ystore.py
--rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/yjs_client_0.js
--rw-r--r--   0        0        0      871 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/tests/yjs_client_1.js
--rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/__init__.py
--rw-r--r--   0        0        0     2313 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/awareness.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/py.typed
--rw-r--r--   0        0        0     1273 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/websocket_provider.py
--rw-r--r--   0        0        0     6051 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/websocket_server.py
--rw-r--r--   0        0        0    10586 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/ystore.py
--rw-r--r--   0        0        0     4020 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/ypy_websocket/yutils.py
--rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/.gitignore
--rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/LICENSE
--rw-r--r--   0        0        0     1874 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/README.md
--rw-r--r--   0        0        0     1060 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/pyproject.toml
--rw-r--r--   0        0        0     2539 2020-02-02 00:00:00.000000 ypy_websocket-0.8.4/PKG-INFO
+-rw-r--r--   0        0        0     1096 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/conftest.py
+-rw-r--r--   0        0        0       76 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/package.json
+-rw-r--r--   0        0        0     2322 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/test_ypy_yjs.py
+-rw-r--r--   0        0        0     3007 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/test_ystore.py
+-rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/yjs_client_0.js
+-rw-r--r--   0        0        0      871 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/tests/yjs_client_1.js
+-rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/__init__.py
+-rw-r--r--   0        0        0     2313 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/awareness.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/py.typed
+-rw-r--r--   0        0        0     1273 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/websocket_provider.py
+-rw-r--r--   0        0        0     6051 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/websocket_server.py
+-rw-r--r--   0        0        0    10544 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/ystore.py
+-rw-r--r--   0        0        0     4012 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/ypy_websocket/yutils.py
+-rw-r--r--   0        0        0     1884 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/.gitignore
+-rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/LICENSE
+-rw-r--r--   0        0        0     1874 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/README.md
+-rw-r--r--   0        0        0     1649 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/pyproject.toml
+-rw-r--r--   0        0        0     4394 2020-02-02 00:00:00.000000 ypy_websocket-0.9.0/PKG-INFO
```

### Comparing `ypy_websocket-0.8.4/tests/conftest.py` & `ypy_websocket-0.9.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/tests/test_ypy_yjs.py` & `ypy_websocket-0.9.0/tests/test_ypy_yjs.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/tests/test_ystore.py` & `ypy_websocket-0.9.0/tests/test_ystore.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/tests/yjs_client_0.js` & `ypy_websocket-0.9.0/tests/yjs_client_0.js`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/tests/yjs_client_1.js` & `ypy_websocket-0.9.0/tests/yjs_client_1.js`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/ypy_websocket/awareness.py` & `ypy_websocket-0.9.0/ypy_websocket/awareness.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/ypy_websocket/websocket_provider.py` & `ypy_websocket-0.9.0/ypy_websocket/websocket_provider.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/ypy_websocket/websocket_server.py` & `ypy_websocket-0.9.0/ypy_websocket/websocket_server.py`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/ypy_websocket/ystore.py` & `ypy_websocket-0.9.0/ypy_websocket/ystore.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,17 +3,16 @@
 import struct
 import tempfile
 import time
 from abc import ABC, abstractmethod
 from pathlib import Path
 from typing import AsyncIterator, Callable, Optional, Tuple
 
-import aiofiles  # type: ignore
-import aiofiles.os  # type: ignore
-import aiosqlite  # type: ignore
+import aiosqlite
+import anyio
 import y_py as Y
 
 from .yutils import Decoder, get_new_path, write_var_uint
 
 
 class YDocNotFound(Exception):
     pass
@@ -59,48 +58,48 @@
     def __init__(self, path: str, metadata_callback: Optional[Callable] = None, log=None):
         self.path = path
         self.metadata_callback = metadata_callback
         self.log = log or logging.getLogger(__name__)
         self.lock = asyncio.Lock()
 
     async def check_version(self) -> int:
-        if not await aiofiles.os.path.exists(self.path):
+        if not await anyio.Path(self.path).exists():
             version_mismatch = True
         else:
             version_mismatch = False
             move_file = False
-            async with aiofiles.open(self.path, "rb") as f:
+            async with await anyio.open_file(self.path, "rb") as f:
                 header = await f.read(8)
                 if header == b"VERSION:":
                     version = int(await f.readline())
                     if version == self.version:
                         offset = await f.tell()
                     else:
                         version_mismatch = True
                 else:
                     version_mismatch = True
                 if version_mismatch:
                     move_file = True
             if move_file:
                 new_path = await get_new_path(self.path)
                 self.log.warning(f"YStore version mismatch, moving {self.path} to {new_path}")
-                await aiofiles.os.rename(self.path, new_path)
+                await anyio.Path(self.path).rename(new_path)
         if version_mismatch:
-            async with aiofiles.open(self.path, "wb") as f:
+            async with await anyio.open_file(self.path, "wb") as f:
                 version_bytes = f"VERSION:{self.version}\n".encode()
                 await f.write(version_bytes)
                 offset = len(version_bytes)
         return offset
 
     async def read(self) -> AsyncIterator[Tuple[bytes, bytes, float]]:  # type: ignore
         async with self.lock:
-            if not await aiofiles.os.path.exists(self.path):
+            if not await anyio.Path(self.path).exists():
                 raise YDocNotFound
             offset = await self.check_version()
-            async with aiofiles.open(self.path, "rb") as f:
+            async with await anyio.open_file(self.path, "rb") as f:
                 await f.seek(offset)
                 data = await f.read()
                 if not data:
                     raise YDocNotFound
         i = 0
         for d in Decoder(data).read_messages():
             if i == 0:
@@ -111,17 +110,17 @@
                 timestamp = struct.unpack("<d", d)[0]
                 yield update, metadata, timestamp
             i = (i + 1) % 3
 
     async def write(self, data: bytes) -> None:
         parent = Path(self.path).parent
         async with self.lock:
-            await aiofiles.os.makedirs(parent, exist_ok=True)
+            await anyio.Path(parent).mkdir(parents=True, exist_ok=True)
             await self.check_version()
-            async with aiofiles.open(self.path, "ab") as f:
+            async with await anyio.open_file(self.path, "ab") as f:
                 data_len = write_var_uint(len(data))
                 await f.write(data_len + data)
                 metadata = await self.get_metadata()
                 metadata_len = write_var_uint(len(metadata))
                 await f.write(metadata_len + metadata)
                 timestamp = struct.pack("<d", time.time())
                 timestamp_len = write_var_uint(len(timestamp))
@@ -179,15 +178,15 @@
         self.log = log or logging.getLogger(__name__)
         self.lock = asyncio.Lock()
         self.db_initialized = asyncio.create_task(self.init_db())
 
     async def init_db(self):
         create_db = False
         move_db = False
-        if not await aiofiles.os.path.exists(self.db_path):
+        if not await anyio.Path(self.db_path).exists():
             create_db = True
         else:
             async with self.lock:
                 async with aiosqlite.connect(self.db_path) as db:
                     cursor = await db.execute(
                         "SELECT count(name) FROM sqlite_master WHERE type='table' and name='yupdates'"
                     )
@@ -199,15 +198,15 @@
                             move_db = True
                             create_db = True
                     else:
                         create_db = True
         if move_db:
             new_path = await get_new_path(self.db_path)
             self.log.warning(f"YStore version mismatch, moving {self.db_path} to {new_path}")
-            await aiofiles.os.rename(self.db_path, new_path)
+            await anyio.Path(self.db_path).rename(new_path)
         if create_db:
             async with self.lock:
                 async with aiosqlite.connect(self.db_path) as db:
                     await db.execute(
                         "CREATE TABLE yupdates (path TEXT NOT NULL, yupdate BLOB, metadata BLOB, timestamp REAL NOT NULL)"
                     )
                     await db.execute(
```

### Comparing `ypy_websocket-0.8.4/ypy_websocket/yutils.py` & `ypy_websocket-0.9.0/ypy_websocket/yutils.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import asyncio
 from enum import IntEnum
 from pathlib import Path
 from typing import Optional
 
-import aiofiles.os  # type: ignore
+import anyio
 import y_py as Y
 
 
 class YMessageType(IntEnum):
     SYNC = 0
     AWARENESS = 1
 
@@ -140,14 +140,14 @@
 
 
 async def get_new_path(path: str) -> str:
     p = Path(path)
     ext = p.suffix
     p_noext = p.with_suffix("")
     i = 1
-    dir_list = await aiofiles.os.listdir()
+    dir_list = [p async for p in anyio.Path().iterdir()]
     while True:
         new_path = f"{p_noext}({i}){ext}"
         if new_path not in dir_list:
             break
         i += 1
     return str(new_path)
```

### Comparing `ypy_websocket-0.8.4/.gitignore` & `ypy_websocket-0.9.0/.gitignore`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/LICENSE` & `ypy_websocket-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/README.md` & `ypy_websocket-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `ypy_websocket-0.8.4/pyproject.toml` & `ypy_websocket-0.9.0/pyproject.toml`

 * *Files 24% similar despite different names*

```diff
@@ -2,40 +2,55 @@
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "ypy-websocket"
 dynamic = ["version"]
 description = "WebSocket connector for Ypy"
+license = { file = "LICENSE" }
 readme = "README.md"
 requires-python = ">=3.7"
 authors = [
     { name = "David Brochart", email = "david.brochart@gmail.com" },
 ]
 keywords = [
     "websocket",
     "yjs",
 ]
+classifiers = [
+    "Development Status :: 4 - Beta",
+    "Intended Audience :: Developers",
+    "License :: OSI Approved :: MIT License",
+    "Programming Language :: Python",
+    "Programming Language :: Python :: 3.7",
+    "Programming Language :: Python :: 3.8",
+    "Programming Language :: Python :: 3.9",
+    "Programming Language :: Python :: 3.10",
+    "Programming Language :: Python :: 3.11",
+]
 dependencies = [
-    "aiofiles >=22.1.0,<23",
-    "aiosqlite >=0.17.0,<1",
+    "anyio >=3.6.2,<4",
+    "aiosqlite >=0.18.0,<1",
     "y-py >=0.6.0,<0.7.0",
 ]
 
 [project.optional-dependencies]
 test = [
     "mypy",
     "pre-commit",
     "pytest",
     "pytest-asyncio",
     "websockets >=10.0",
 ]
 
 [project.urls]
 Homepage = "https://github.com/y-crdt/ypy-websocket"
+Source = "https://github.com/y-crdt/ypy-websocket"
+Issues = "https://github.com/y-crdt/ypy-websocket/issues"
+Pypi = "https://pypi.org/project/ypy-websocket"
 
 [tool.hatch.version]
 path = "ypy_websocket/__init__.py"
 
 [tool.hatch.build.targets.sdist]
 include = [
     "/ypy_websocket",
```

