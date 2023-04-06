# Comparing `tmp/fps_terminals-0.0.50.tar.gz` & `tmp/fps_terminals-0.1.2.tar.gz`

## Comparing `fps_terminals-0.0.50.tar` & `fps_terminals-0.1.2.tar`

### file list

```diff
@@ -1,11 +1,12 @@
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/MANIFEST.in
--rw-r--r--   0        0        0       23 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/fps_terminals/__init__.py
--rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/fps_terminals/models.py
--rw-r--r--   0        0        0     2074 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/fps_terminals/routes.py
--rw-r--r--   0        0        0     2351 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/fps_terminals/server.py
--rw-r--r--   0        0        0     1782 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/fps_terminals/win_server.py
--rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/.gitignore
--rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/COPYING.md
--rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/README.md
--rw-r--r--   0        0        0      859 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/pyproject.toml
--rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 fps_terminals-0.0.50/PKG-INFO
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/MANIFEST.in
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/__init__.py
+-rw-r--r--   0        0        0      726 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/main.py
+-rw-r--r--   0        0        0       97 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/models.py
+-rw-r--r--   0        0        0     2442 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/routes.py
+-rw-r--r--   0        0        0     2419 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/server.py
+-rw-r--r--   0        0        0     1850 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/fps_terminals/win_server.py
+-rw-r--r--   0        0        0     6359 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/.gitignore
+-rw-r--r--   0        0        0     2833 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/COPYING.md
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/README.md
+-rw-r--r--   0        0        0      951 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      534 2020-02-02 00:00:00.000000 fps_terminals-0.1.2/PKG-INFO
```

### Comparing `fps_terminals-0.0.50/fps_terminals/server.py` & `fps_terminals-0.1.2/fps_terminals/server.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,27 +3,28 @@
 import os
 import pty
 import shlex
 import struct
 import termios
 
 from fastapi import WebSocketDisconnect
+from jupyverse_api.terminals import TerminalServer
 
 
 def open_terminal(command="bash", columns=80, lines=24):
     pid, fd = pty.fork()
     if pid == 0:
         argv = shlex.split(command)
         env = os.environ.copy()
         env.update(TERM="linux", COLUMNS=str(columns), LINES=str(lines))
         os.execvpe(argv[0], argv, env)
     return fd
 
 
-class TerminalServer:
+class _TerminalServer(TerminalServer):
     def __init__(self):
         self.fd = open_terminal()
         self.p_out = os.fdopen(self.fd, "w+b", 0)
         self.websockets = []
 
     async def serve(self, websocket, permissions):
         self.websocket = websocket
```

### Comparing `fps_terminals-0.0.50/fps_terminals/win_server.py` & `fps_terminals-0.1.2/fps_terminals/win_server.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 import asyncio
 import os
 
+from jupyverse_api.terminals import TerminalServer
 from winpty import PTY  # type: ignore
 
 
 def open_terminal(command="C:\\Windows\\System32\\cmd.exe", columns=80, lines=24):
     env = "\0".join([f"{k}={v}" for k, v in os.environ.items()]) + "\0"
     process = PTY(columns, lines)
     process.spawn(command, env=env)
     return process
 
 
-class TerminalServer:
+class _TerminalServer(TerminalServer):
     def __init__(self):
         self.process = open_terminal()
         self.websockets = []
 
     async def serve(self, websocket):
         self.websocket = websocket
         self.websockets.append(websocket)
```

### Comparing `fps_terminals-0.0.50/.gitignore` & `fps_terminals-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `fps_terminals-0.0.50/COPYING.md` & `fps_terminals-0.1.2/COPYING.md`

 * *Files identical despite different names*

### Comparing `fps_terminals-0.0.50/PKG-INFO` & `fps_terminals-0.1.2/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 Metadata-Version: 2.1
 Name: fps_terminals
-Version: 0.0.50
+Version: 0.1.2
 Summary: An FPS plugin for the terminals API
 Project-URL: Homepage, https://jupyter.org
 Author-email: Jupyter Development Team <jupyter@googlegroups.com>
 License: BSD 3-Clause License
 License-File: COPYING.md
-Keywords: fastapi,jupyter,pluggy,plugins,server
+Keywords: fastapi,jupyter,plugins,server
 Requires-Python: >=3.8
-Requires-Dist: fps-auth-base
-Requires-Dist: fps>=0.0.8
+Requires-Dist: jupyverse-api
 Requires-Dist: pywinpty; platform_system == 'Windows'
 Requires-Dist: websockets
 Description-Content-Type: text/markdown
 
 # fps-terminals
 
 An FPS plugin for the terminals API.
```

