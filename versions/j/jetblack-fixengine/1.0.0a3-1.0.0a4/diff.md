# Comparing `tmp/jetblack-fixengine-1.0.0a3.tar.gz` & `tmp/jetblack-fixengine-1.0.0a4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jetblack-fixengine-1.0.0a3.tar", max compression
+gzip compressed data, was "jetblack-fixengine-1.0.0a4.tar", max compression
```

## Comparing `jetblack-fixengine-1.0.0a3.tar` & `jetblack-fixengine-1.0.0a4.tar`

### file list

```diff
@@ -1,42 +1,42 @@
--rw-r--r--   0        0        0    11357 2023-03-19 08:07:10.647832 jetblack-fixengine-1.0.0a3/LICENSE
--rw-r--r--   0        0        0     4372 2023-04-02 11:47:49.270385 jetblack-fixengine-1.0.0a3/README.md
--rw-r--r--   0        0        0      359 2023-04-02 10:01:57.381026 jetblack-fixengine-1.0.0a3/jetblack_fixengine/__init__.py
--rw-r--r--   0        0        0      136 2023-04-02 10:46:14.949547 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/__init__.py
--rw-r--r--   0        0        0     7972 2023-04-02 11:07:34.388762 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/acceptor.py
--rw-r--r--   0        0        0     3304 2023-04-02 10:46:26.788149 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/helpers.py
--rw-r--r--   0        0        0     6473 2023-04-02 10:45:01.997468 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/state_machine.py
--rw-r--r--   0        0        0     1757 2023-04-02 10:52:10.219438 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/state_transitions.py
--rw-r--r--   0        0        0      731 2023-04-02 10:50:38.653751 jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/types.py
--rw-r--r--   0        0        0      217 2023-04-02 07:49:31.247277 jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/__init__.py
--rw-r--r--   0        0        0     1232 2023-04-02 07:49:31.247472 jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/state_processor.py
--rw-r--r--   0        0        0     1292 2023-04-02 07:49:31.247618 jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/state_transitions.py
--rw-r--r--   0        0        0     3064 2023-04-02 07:49:31.247760 jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/types.py
--rw-r--r--   0        0        0      225 2023-04-02 10:48:23.639519 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/__init__.py
--rw-r--r--   0        0        0     3169 2023-04-02 10:52:31.884954 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/helpers.py
--rw-r--r--   0        0        0     6100 2023-04-02 11:07:34.344626 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/initiator.py
--rw-r--r--   0        0        0     4890 2023-04-02 10:51:41.615910 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/state_machine.py
--rw-r--r--   0        0        0     1907 2023-04-02 10:52:02.577886 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/state_transitions.py
--rw-r--r--   0        0        0      176 2023-04-02 07:49:31.248601 jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/types.py
--rw-r--r--   0        0        0      158 2023-03-19 08:07:10.650053 jetblack-fixengine-1.0.0a3/jetblack_fixengine/managers/__init__.py
--rw-r--r--   0        0        0     5294 2023-04-02 10:49:54.522343 jetblack-fixengine-1.0.0a3/jetblack_fixengine/managers/initiator_manager.py
--rw-r--r--   0        0        0      132 2023-04-02 10:53:31.600244 jetblack-fixengine-1.0.0a3/jetblack_fixengine/persistence/__init__.py
--rw-r--r--   0        0        0     4438 2023-04-02 10:32:31.244717 jetblack-fixengine-1.0.0a3/jetblack_fixengine/persistence/file_store.py
--rw-r--r--   0        0        0     5967 2023-04-02 10:43:23.846629 jetblack-fixengine-1.0.0a3/jetblack_fixengine/persistence/sql_store.py
--rw-r--r--   0        0        0        0 2023-04-02 07:49:31.249061 jetblack-fixengine-1.0.0a3/jetblack_fixengine/py.typed
--rw-r--r--   0        0        0      629 2023-04-02 11:07:45.608721 jetblack-fixengine-1.0.0a3/jetblack_fixengine/time_provider.py
--rw-r--r--   0        0        0      568 2023-04-02 07:49:31.249427 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/__init__.py
--rw-r--r--   0        0        0     1559 2023-04-02 07:49:31.249786 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_events.py
--rw-r--r--   0        0        0     8197 2023-03-19 15:22:36.371647 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_read_buffer.py
--rw-r--r--   0        0        0     1383 2023-04-02 07:49:31.250207 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_reader_async.py
--rw-r--r--   0        0        0     6326 2023-04-02 07:49:31.250445 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_transport.py
--rw-r--r--   0        0        0     3992 2023-04-02 10:54:32.553624 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_machine.py
--rw-r--r--   0        0        0     1327 2023-04-02 10:55:07.384675 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_processor.py
--rw-r--r--   0        0        0     1785 2023-04-02 10:55:49.604609 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_transitions.py
--rw-r--r--   0        0        0     1161 2023-04-02 07:49:31.251203 jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/types.py
--rw-r--r--   0        0        0     4629 2023-04-02 10:39:42.878453 jetblack-fixengine-1.0.0a3/jetblack_fixengine/types.py
--rw-r--r--   0        0        0        0 2023-03-19 08:07:10.651512 jetblack-fixengine-1.0.0a3/jetblack_fixengine/utils/__init__.py
--rw-r--r--   0        0        0     1091 2023-04-02 10:58:04.048732 jetblack-fixengine-1.0.0a3/jetblack_fixengine/utils/cancellation.py
--rw-r--r--   0        0        0     3099 2023-04-02 11:05:21.329690 jetblack-fixengine-1.0.0a3/jetblack_fixengine/utils/date_utils.py
--rw-r--r--   0        0        0      818 2023-04-02 11:48:01.790514 jetblack-fixengine-1.0.0a3/pyproject.toml
--rw-r--r--   0        0        0     5651 2023-04-02 11:48:36.907628 jetblack-fixengine-1.0.0a3/setup.py
--rw-r--r--   0        0        0     5285 2023-04-02 11:48:36.908106 jetblack-fixengine-1.0.0a3/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-03-19 08:07:10.647832 jetblack-fixengine-1.0.0a4/LICENSE
+-rw-r--r--   0        0        0     4797 2023-04-06 08:13:02.362705 jetblack-fixengine-1.0.0a4/README.md
+-rw-r--r--   0        0        0      370 2023-04-06 08:13:02.363241 jetblack-fixengine-1.0.0a4/jetblack_fixengine/__init__.py
+-rw-r--r--   0        0        0       88 2023-04-06 08:13:02.363414 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/__init__.py
+-rw-r--r--   0        0        0     8030 2023-04-06 08:13:02.363681 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/acceptor.py
+-rw-r--r--   0        0        0     2618 2023-04-06 08:13:02.363870 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/helpers.py
+-rw-r--r--   0        0        0     6585 2023-04-06 08:13:02.364011 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_machine.py
+-rw-r--r--   0        0        0     1757 2023-04-02 10:52:10.219438 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_transitions.py
+-rw-r--r--   0        0        0      727 2023-04-06 08:13:02.364136 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/types.py
+-rw-r--r--   0        0        0      217 2023-04-02 07:49:31.247277 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/__init__.py
+-rw-r--r--   0        0        0     1232 2023-04-02 07:49:31.247472 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_processor.py
+-rw-r--r--   0        0        0     1292 2023-04-02 07:49:31.247618 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_transitions.py
+-rw-r--r--   0        0        0     3064 2023-04-02 07:49:31.247760 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/types.py
+-rw-r--r--   0        0        0      193 2023-04-06 08:13:02.364275 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/__init__.py
+-rw-r--r--   0        0        0     2585 2023-04-06 08:13:02.364454 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/helpers.py
+-rw-r--r--   0        0        0     6158 2023-04-06 08:13:02.364596 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/initiator.py
+-rw-r--r--   0        0        0     4998 2023-04-06 08:13:02.364752 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_machine.py
+-rw-r--r--   0        0        0     1907 2023-04-02 10:52:02.577886 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_transitions.py
+-rw-r--r--   0        0        0      172 2023-04-06 08:13:02.364900 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/types.py
+-rw-r--r--   0        0        0      158 2023-03-19 08:07:10.650053 jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/__init__.py
+-rw-r--r--   0        0        0     5298 2023-04-06 08:13:02.365074 jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/initiator_manager.py
+-rw-r--r--   0        0        0      132 2023-04-02 10:53:31.600244 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/__init__.py
+-rw-r--r--   0        0        0     4438 2023-04-02 10:32:31.244717 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/file_store.py
+-rw-r--r--   0        0        0     5967 2023-04-02 10:43:23.846629 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/sql_store.py
+-rw-r--r--   0        0        0        0 2023-04-02 07:49:31.249061 jetblack-fixengine-1.0.0a4/jetblack_fixengine/py.typed
+-rw-r--r--   0        0        0      629 2023-04-02 11:07:45.608721 jetblack-fixengine-1.0.0a4/jetblack_fixengine/time_provider.py
+-rw-r--r--   0        0        0      568 2023-04-02 07:49:31.249427 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/__init__.py
+-rw-r--r--   0        0        0     1559 2023-04-02 07:49:31.249786 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_events.py
+-rw-r--r--   0        0        0     8197 2023-03-19 15:22:36.371647 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_read_buffer.py
+-rw-r--r--   0        0        0     1383 2023-04-02 07:49:31.250207 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_reader_async.py
+-rw-r--r--   0        0        0     6326 2023-04-02 07:49:31.250445 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_transport.py
+-rw-r--r--   0        0        0     4153 2023-04-06 08:13:02.365244 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_machine.py
+-rw-r--r--   0        0        0     1327 2023-04-02 10:55:07.384675 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_processor.py
+-rw-r--r--   0        0        0     1785 2023-04-02 10:55:49.604609 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_transitions.py
+-rw-r--r--   0        0        0     1161 2023-04-02 07:49:31.251203 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/types.py
+-rw-r--r--   0        0        0     5224 2023-04-06 08:13:02.365382 jetblack-fixengine-1.0.0a4/jetblack_fixengine/types.py
+-rw-r--r--   0        0        0        0 2023-03-19 08:07:10.651512 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/__init__.py
+-rw-r--r--   0        0        0     1091 2023-04-02 10:58:04.048732 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/cancellation.py
+-rw-r--r--   0        0        0     3099 2023-04-02 11:05:21.329690 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/date_utils.py
+-rw-r--r--   0        0        0      818 2023-04-06 08:13:13.312818 jetblack-fixengine-1.0.0a4/pyproject.toml
+-rw-r--r--   0        0        0     6110 2023-04-06 08:17:43.714063 jetblack-fixengine-1.0.0a4/setup.py
+-rw-r--r--   0        0        0     5710 2023-04-06 08:17:43.714558 jetblack-fixengine-1.0.0a4/PKG-INFO
```

### Comparing `jetblack-fixengine-1.0.0a3/LICENSE` & `jetblack-fixengine-1.0.0a4/LICENSE`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/README.md` & `jetblack-fixengine-1.0.0a4/README.md`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # jetblack-fixengine
 
-A pure python asyncio FIX engine implemented as a state machine.
+A pure python asyncio FIX engine.
 
 ## Status
 
 This is work in progress.
 
 ## Installation
 
@@ -47,57 +47,73 @@
 [etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)
 folder.
 
 Currently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.
 
 ### Initiators
 
-An initiator is a class which inherits from `Initiator`, and implements a
-few methods, and has access to `send_message`. Here is an example.
+An initiator is a class which inherits from `FIXApplication`, and implements a
+few methods, and has access to `send_message` from the `fix_engine`. Here is an example.
 
 ```python
 import asyncio
 import logging
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
-from jetblack_fixengine import FileStore
-from jetblack_fixengine import start_initiator, Initiator
+from jetblack_fixengine import (
+    FileStore,
+    start_initiator,
+    FIXApplication,
+    FIXEngine
+)
 
 LOGGER = logging.getLogger(__name__)
 
 
-class MyInitiator(Initiator):
+class MyInitiator(FIXApplication):
     """An instance of the initiator"""
 
-    async def on_logon(self, _message: Mapping[str, Any]) -> None:
+    async def on_logon(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logon')
 
-    async def on_logout(self, _message: Mapping[str, Any]) -> None:
+    async def on_logout(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logout')
 
-    async def on_application_message(self, _message: Mapping[str, Any]) -> None:
+    async def on_application_message(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_application_message')
 
 
 PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path("store"))
+STORE = FileStore(Path('store'))
 HOST = '127.0.0.1'
 PORT = 9801
 SENDER_COMP_ID = 'INITIATOR1'
 TARGET_COMP_ID = 'ACCEPTOR'
 LOGON_TIMEOUT = 60
 HEARTBEAT_TIMEOUT = 30
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
     start_initiator(
-        MyInitiator,
+        MyInitiator(),
         HOST,
         PORT,
         PROTOCOL,
         SENDER_COMP_ID,
         TARGET_COMP_ID,
         STORE,
         LOGON_TIMEOUT,
@@ -114,31 +130,47 @@
 ```python
 import asyncio
 import logging
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
-from jetblack_fixengine import FileStore
-from jetblack_fixengine import start_acceptor, Acceptor
+from jetblack_fixengine import (
+    FileStore,
+    start_acceptor,
+    FIXApplication,
+    FIXEngine
+)
 
 
 LOGGER = logging.getLogger(__name__)
 
 
-class MyAcceptor(Acceptor):
+class MyAcceptor(FIXApplication):
     """An instance of the acceptor"""
 
-    async def on_logon(self, _message: Mapping[str, Any]):
+    async def on_logon(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logon')
 
-    async def on_logout(self, _message: Mapping[str, Any]) -> None:
+    async def on_logout(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logout')
 
-    async def on_application_message(self, _message: Mapping[str, Any]) -> None:
+    async def on_application_message(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_application_message')
 
 
 PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
 STORE = FileStore(Path("store"))
 HOST = '0.0.0.0'
 PORT = 9801
@@ -147,15 +179,15 @@
 LOGON_TIMEOUT = 60
 HEARTBEAT_TIMEOUT = 30
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
     start_acceptor(
-        MyAcceptor,
+        MyAcceptor(),
         HOST,
         PORT,
         PROTOCOL,
         SENDER_COMP_ID,
         TARGET_COMP_ID,
         STORE,
         HEARTBEAT_TIMEOUT,
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/acceptor.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/acceptor.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 """An acceptor"""
 
-from abc import ABCMeta
 import asyncio
 from datetime import datetime, time, tzinfo, timezone
 import logging
 from typing import (
     Mapping,
     Any,
     Optional,
@@ -25,27 +24,28 @@
     TransportState,
     TransportEvent,
     TransportMessage,
     TransportStateMachine,
     Send,
     Receive
 )
-from ..types import Store, Session
+from ..types import Store, Session, FIXApplication
 
 from .state_machine import AcceptorAdminStateMachine
-from .types import AbstractAcceptor
+from .types import AbstractAcceptorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 
-class Acceptor(AbstractAcceptor, metaclass=ABCMeta):
+class AcceptorEngine(AbstractAcceptorEngine):
     """The base class for acceptor handlers"""
 
     def __init__(
             self,
+            app: FIXApplication,
             protocol: ProtocolMetaData,
             sender_comp_id: str,
             target_comp_id: str,
             store: Store,
             heartbeat_timeout: int,
             cancellation_event: asyncio.Event,
             *,
@@ -76,19 +76,21 @@
         self._session = self._store.get_session(sender_comp_id, target_comp_id)
         self._send: Optional[Send] = None
         self._receive: Optional[Receive] = None
         self._logout_time: Optional[datetime] = None
 
         self._admin_state_machine = AcceptorAdminStateMachine(
             self,
+            app,
             self.time_provider,
             self.cancellation_event
         )
         self._transport_state_machine = TransportStateMachine(
             self,
+            app,
             self._admin_state_machine,
             self.time_provider
         )
 
     @property
     def session(self) -> Session:
         return self._session
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/helpers.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/helpers.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,69 +1,42 @@
 """Helper functions"""
 
 import asyncio
 from asyncio import StreamReader, StreamWriter, Event
 from datetime import time, tzinfo
 import logging
-from typing import Callable, Optional, Tuple, Type
+from typing import Callable, Optional, Tuple
 from ssl import SSLContext
 
 from jetblack_fixparser.meta_data import ProtocolMetaData
 from jetblack_fixparser.fix_message import SOH
 
 from ..transports import (
     fix_stream_processor,
     FixReadBuffer,
     fix_read_async,
     TransportHandler,
 )
-from ..types import Store
+from ..types import Store, FIXApplication
 from ..utils.cancellation import register_cancellation_event
 
-from .acceptor import Acceptor
+from .acceptor import AcceptorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 ClientFactory = Callable[[], TransportHandler]
 
 AcceptorFactory = Callable[
     [ProtocolMetaData, str, str, Store, int, asyncio.Event],
     TransportHandler
 ]
 
 
-def _create_acceptor(
-        klass: Type[Acceptor],
-        protocol: ProtocolMetaData,
-        sender_comp_id: str,
-        target_comp_id: str,
-        store: Store,
-        heartbeat_timeout: int,
-        cancellation_event: asyncio.Event,
-        *,
-        heartbeat_threshold: int = 1,
-        logon_time_range: Optional[Tuple[time, time]] = None,
-        tz: Optional[tzinfo] = None
-) -> Acceptor:
-    handler = klass(
-        protocol,
-        sender_comp_id,
-        target_comp_id,
-        store,
-        heartbeat_timeout,
-        cancellation_event,
-        heartbeat_threshold=heartbeat_threshold,
-        logon_time_range=logon_time_range,
-        tz=tz
-    )
-    return handler
-
-
 async def start_acceptor(
-        klass: Type[Acceptor],
+        app: FIXApplication,
         host: str,
         port: int,
         protocol: ProtocolMetaData,
         sender_comp_id: str,
         target_comp_id: str,
         store: Store,
         heartbeat_timeout: int,
@@ -84,16 +57,16 @@
 
         read_buffer = FixReadBuffer(
             sep,
             convert_sep_to_soh_for_checksum,
             validate
         )
         buffered_reader = fix_read_async(read_buffer, reader, 1024)
-        handler = _create_acceptor(
-            klass,
+        handler = AcceptorEngine(
+            app,
             protocol,
             sender_comp_id,
             target_comp_id,
             store,
             heartbeat_timeout,
             cancellation_event,
             heartbeat_threshold=heartbeat_threshold,
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/state_machine.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_machine.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,28 +9,29 @@
 from ..admin import (
     AdminState,
     AdminEvent,
     AdminMessage,
     AdminStateProcessor,
 )
 from ..time_provider import TimeProvider
-from ..types import LoginError
+from ..types import LoginError, FIXApplication
 from ..utils.date_utils import wait_for_time_period
 
 from .state_transitions import ACCEPTOR_ADMIN_TRANSITIONS
-from .types import AbstractAcceptor
+from .types import AbstractAcceptorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 
 class AcceptorAdminStateMachine(AdminStateProcessor):
 
     def __init__(
             self,
-            acceptor: AbstractAcceptor,
+            engine: AbstractAcceptorEngine,
+            app: FIXApplication,
             time_provider: TimeProvider,
             cancellation_event: asyncio.Event
     ) -> None:
         super().__init__(
             ACCEPTOR_ADMIN_TRANSITIONS,
             {
                 AdminState.DISCONNECTED: {
@@ -56,102 +57,103 @@
                 },
                 AdminState.REJECT_LOGON: {
                     AdminEvent.SEND_LOGOUT: self._send_logout
                 }
             }
         )
 
-        self.acceptor = acceptor
-        self.time_provider = time_provider
-        self.cancellation_event = cancellation_event
+        self._engine = engine
+        self._app = app
+        self._time_provider = time_provider
+        self._cancellation_event = cancellation_event
         self._test_heartbeat_message: Optional[str] = None
 
     async def _handle_connected(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        if self.acceptor.logon_time_range:
-            start_time, end_time = self.acceptor.logon_time_range
+        if self._engine.logon_time_range:
+            start_time, end_time = self._engine.logon_time_range
             LOGGER.info(
                 "Waiting for logging window between %s and %s",
                 start_time,
                 end_time
             )
-            self.acceptor.logout_time = await wait_for_time_period(
-                self.time_provider.now(self.acceptor.tz or timezone.utc),
+            self._engine.logout_time = await wait_for_time_period(
+                self._time_provider.now(self._engine.tz or timezone.utc),
                 start_time,
                 end_time,
-                self.cancellation_event
+                self._cancellation_event
             )
 
         return None
 
     async def _validate_logon(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         try:
-            await self.acceptor.on_logon(admin_message.fix)
+            await self._app.on_logon(admin_message.fix, self._engine)
             return AdminMessage(AdminEvent.LOGON_ACCEPTED)
         except LoginError:
             LOGGER.info("Logon rejected")
         except:  # pylint: disable=bare-except
             LOGGER.exception("Logon failed")
 
         return AdminMessage(AdminEvent.LOGON_REJECTED)
 
     async def _send_logon(
             self,
             _admin_message: Optional[AdminMessage]
     ) -> Optional[AdminMessage]:
-        await self.acceptor.send_message(
+        await self._engine.send_message(
             'LOGON',
             {
                 'EncryptMethod': 'NONE',
-                'HeartBtInt': self.acceptor.heartbeat_timeout
+                'HeartBtInt': self._engine.heartbeat_timeout
             }
         )
         return None
 
     async def _send_logout(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        await self.acceptor.send_message('LOGOUT')
-        await self.acceptor.on_logout(admin_message.fix)
+        await self._engine.send_message('LOGOUT')
+        await self._app.on_logout(admin_message.fix, self._engine)
         return None
 
     async def _receive_heartbeat(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        await self.acceptor.on_heartbeat(admin_message.fix)
+        await self._app.on_heartbeat(admin_message.fix, self._engine)
         return None
 
     async def _receive_test_request(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         assert 'TestReqID' in admin_message.fix
         test_req_id = admin_message.fix['TestReqID']
-        await self.acceptor.send_message(
+        await self._engine.send_message(
             'TEST_REQUEST',
             {
                 'TestReqID': test_req_id
             }
         )
 
         return AdminMessage(AdminEvent.TEST_REQUEST_SENT)
 
     async def _send_sequence_reset(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        new_seq_no = await self.acceptor.session.get_outgoing_seqnum() + 2
-        await self.acceptor.send_message(
+        new_seq_no = await self._engine.session.get_outgoing_seqnum() + 2
+        await self._engine.send_message(
             'SEQUENCE_RESET',
             {
                 'GapFillFlag': False,
                 'NewSeqNo': new_seq_no
             }
         )
 
@@ -159,31 +161,31 @@
 
     async def _handle_sequence_reset(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         assert 'NewSeqNo' in admin_message.fix
         seqnum = admin_message.fix['NewSeqNo']
-        await self.acceptor.session.set_incoming_seqnum(seqnum)
+        await self._engine.session.set_incoming_seqnum(seqnum)
         return AdminMessage(AdminEvent.INCOMING_SEQNUM_SET)
 
     async def _receive_logout(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        await self.acceptor.on_logout(admin_message.fix)
+        await self._app.on_logout(admin_message.fix, self._engine)
         return None
 
     async def _send_test_heartbeat(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         self._test_heartbeat_message = str(uuid.uuid4())
 
-        await self.acceptor.send_message(
+        await self._engine.send_message(
             'TEST_REQUEST',
             {
                 'TestReqID': self._test_heartbeat_message
             }
         )
         return AdminMessage(AdminEvent.TEST_HEARTBEAT_SENT)
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/state_transitions.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/acceptor/types.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/types.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 """Types"""
 
 from abc import abstractmethod, ABCMeta
 from datetime import datetime, time, tzinfo
 from typing import Optional, Tuple
 
-from ..types import FIXApplication
+from ..types import FIXEngine
 
 
-class AbstractAcceptor(FIXApplication, metaclass=ABCMeta):
+class AbstractAcceptorEngine(FIXEngine, metaclass=ABCMeta):
     """The interface for an acceptor"""
 
     @property
     @abstractmethod
     def logon_time_range(self) -> Optional[Tuple[time, time]]:
         """The logon time range"""
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/state_processor.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_processor.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/state_transitions.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/admin/types.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/types.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/helpers.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/helpers.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 """Helper functions"""
 
 import asyncio
 from asyncio import Event
 import logging
 from ssl import SSLContext
-from typing import Optional, Callable, Type
+from typing import Optional, Callable
 
 from jetblack_fixparser.meta_data import ProtocolMetaData
 from jetblack_fixparser.fix_message import SOH
 
 from ..transports import TransportHandler
-from ..types import Store
+from ..types import Store, FIXApplication
 from ..utils.cancellation import register_cancellation_event
 
 from ..transports import fix_stream_processor,  FixReadBuffer, fix_read_async
 
-from .initiator import Initiator
+from .initiator import InitiatorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 InitiatorFactory = Callable[
     [ProtocolMetaData, str, str, Store, int, asyncio.Event],
     TransportHandler
 ]
@@ -59,41 +59,16 @@
         'disconnected from %s:%s%s',
         host,
         port,
         " over ssl" if ssl else ""
     )
 
 
-def create_initiator(
-        klass: Type[Initiator],
-        protocol: ProtocolMetaData,
-        sender_comp_id: str,
-        target_comp_id: str,
-        store: Store,
-        logon_timeout: int,
-        heartbeat_timeout: int,
-        cancellation_event: asyncio.Event,
-        *,
-        heartbeat_threshold: int = 1
-) -> Initiator:
-    handler = klass(
-        protocol,
-        sender_comp_id,
-        target_comp_id,
-        store,
-        logon_timeout,
-        heartbeat_timeout,
-        cancellation_event,
-        heartbeat_threshold=heartbeat_threshold
-    )
-    return handler
-
-
 async def start_initiator(
-        klass: Type[Initiator],
+        app: FIXApplication,
         host: str,
         port: int,
         protocol: ProtocolMetaData,
         sender_comp_id: str,
         target_comp_id: str,
         store: Store,
         logon_timeout: int,
@@ -103,27 +78,27 @@
         shutdown_timeout: float = 10.0,
         heartbeat_threshold: int = 1
 ) -> None:
     cancellation_event = Event()
     loop = asyncio.get_event_loop()
     register_cancellation_event(cancellation_event, loop)
 
-    handler = create_initiator(
-        klass,
+    engine = InitiatorEngine(
+        app,
         protocol,
         sender_comp_id,
         target_comp_id,
         store,
         logon_timeout,
         heartbeat_timeout,
         cancellation_event,
         heartbeat_threshold=heartbeat_threshold
     )
 
     await initiate(
         host,
         port,
-        handler,
+        engine,
         cancellation_event,
         ssl=ssl,
         shutdown_timeout=shutdown_timeout
     )
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/initiator.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/initiator.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 """An Initiator"""
 
-from abc import ABCMeta
 import asyncio
 from datetime import datetime, timezone
 import logging
 from typing import Mapping, Any, Optional
 
 from jetblack_fixparser.fix_message import FixMessageFactory
 from jetblack_fixparser.meta_data import ProtocolMetaData
@@ -17,27 +16,28 @@
     TransportState,
     TransportEvent,
     TransportMessage,
     TransportStateMachine,
     Send,
     Receive,
 )
-from ..types import Store, Session
+from ..types import Store, Session, FIXApplication
 
 from .state_machine import InitiatorAdminStateMachine
-from .types import AbstractInitiator
+from .types import AbstractInitiatorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 
-class Initiator(AbstractInitiator, metaclass=ABCMeta):
+class InitiatorEngine(AbstractInitiatorEngine):
     """The base class for initiator handlers"""
 
     def __init__(
             self,
+            app: FIXApplication,
             protocol: ProtocolMetaData,
             sender_comp_id: str,
             target_comp_id: str,
             store: Store,
             logon_timeout: int,
             heartbeat_timeout: int,
             cancellation_event: asyncio.Event,
@@ -60,17 +60,19 @@
         self._session = store.get_session(sender_comp_id, target_comp_id)
         self._send: Optional[Send] = None
         self._receive: Optional[Receive] = None
         self._timeout = float(heartbeat_timeout)
 
         self._admin_state_machine = InitiatorAdminStateMachine(
             self,
+            app,
         )
         self._transport_state_machine = TransportStateMachine(
             self,
+            app,
             self._admin_state_machine,
             self._time_provider,
         )
 
         self._stop_event = asyncio.Event()
 
     @property
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/state_machine.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_machine.py`

 * *Files 15% similar despite different names*

```diff
@@ -6,26 +6,28 @@
 
 from ..admin import (
     AdminState,
     AdminEvent,
     AdminMessage,
     AdminStateProcessor,
 )
+from ..types import FIXApplication
 
 from .state_transitions import INITIATOR_ADMIN_TRANSITIONS
-from .types import AbstractInitiator
+from .types import AbstractInitiatorEngine
 
 LOGGER = logging.getLogger(__name__)
 
 
 class InitiatorAdminStateMachine(AdminStateProcessor):
 
     def __init__(
             self,
-            initiator: AbstractInitiator,
+            engine: AbstractInitiatorEngine,
+            app: FIXApplication
     ) -> None:
         super().__init__(
             INITIATOR_ADMIN_TRANSITIONS,
             {
                 AdminState.DISCONNECTED: {
                     AdminEvent.CONNECTED: self._send_logon
                 },
@@ -41,98 +43,99 @@
                     AdminEvent.TEST_HEARTBEAT_REQUIRED: self._send_test_heartbeat,
                 },
                 AdminState.SEND_TEST_HEARTBEAT: {
                     AdminEvent.TEST_REQUEST_SENT: self._validate_test_heartbeat
                 },
             }
         )
-        self.initiator = initiator
+        self._engine = engine
+        self._app = app
         self._test_heartbeat_message: Optional[str] = None
 
     async def _send_logon(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         """Send a logon message"""
-        await self.initiator.send_message(
+        await self._engine.send_message(
             'LOGON',
             {
                 'EncryptMethod': 'NONE',
-                'HeartBtInt': self.initiator.heartbeat_timeout
+                'HeartBtInt': self._engine.heartbeat_timeout
             }
         )
         return AdminMessage(AdminEvent.LOGON_SENT)
 
     async def _logon_received(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        await self.initiator.on_logon(admin_message.fix)
+        await self._app.on_logon(admin_message.fix, self._engine)
         return None
 
     async def _acknowledge_heartbeat(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        await self.initiator.on_heartbeat(admin_message.fix)
+        await self._app.on_heartbeat(admin_message.fix, self._engine)
         return AdminMessage(AdminEvent.HEARTBEAT_ACKNOWLEDGED)
 
     async def _send_test_request(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         assert 'TestReqID' in admin_message.fix, "expected TestReqID"
 
         # Respond to the server with the token it sent.
-        await self.initiator.send_message(
+        await self._engine.send_message(
             'TEST_REQUEST',
             {
                 'TestReqID': admin_message.fix['TestReqID']
             }
         )
         return AdminMessage(AdminEvent.TEST_REQUEST_SENT)
 
     async def _send_sequence_reset(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
-        new_seq_no = await self.initiator.session.get_outgoing_seqnum() + 2
-        await self.initiator.send_message(
+        new_seq_no = await self._engine.session.get_outgoing_seqnum() + 2
+        await self._engine.send_message(
             'SEQUENCE_RESET',
             {
                 'GapFillFlag': False,
                 'NewSeqNo': new_seq_no
             }
         )
         return AdminMessage(AdminEvent.SEQUENCE_RESET_SENT)
 
     async def _reset_incoming_seqnum(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         assert 'NewSeqNo' in admin_message.fix, "expected NewSeqNo"
         seqnum = admin_message.fix['NewSeqNo']
-        await self.initiator.session.set_incoming_seqnum(seqnum)
+        await self._engine.session.set_incoming_seqnum(seqnum)
         return AdminMessage(AdminEvent.SEQUENCE_RESET_SENT)
 
     async def _acknowledge_logout(
             self,
             admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         assert admin_message.fix is not None
-        await self.initiator.on_logout(admin_message.fix)
+        await self._app.on_logout(admin_message.fix, self._engine)
         return AdminMessage(AdminEvent.LOGOUT_ACKNOWLEDGED)
 
     async def _send_test_heartbeat(
             self,
             _admin_message: AdminMessage
     ) -> Optional[AdminMessage]:
         self._test_heartbeat_message = str(uuid.uuid4())
 
-        await self.initiator.send_message(
+        await self._engine.send_message(
             'TEST_REQUEST',
             {
                 'TestReqID': self._test_heartbeat_message
             }
         )
         return AdminMessage(AdminEvent.TEST_HEARTBEAT_SENT)
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/initiator/state_transitions.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/managers/initiator_manager.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/initiator_manager.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,32 +1,32 @@
 """An initiator manager"""
 
 import asyncio
 import calendar
 from datetime import datetime, time, tzinfo
 import logging
 from ssl import SSLContext
-from typing import Callable, Optional, Tuple, Type
+from typing import Callable, Optional, Tuple
 
 from jetblack_fixparser.meta_data import ProtocolMetaData
 
-from ..initiator import Initiator, create_initiator, initiate
-from ..types import Store
+from ..initiator import InitiatorEngine, initiate
+from ..types import Store, FIXApplication
 from ..utils.date_utils import wait_for_day_of_week, wait_for_time_period
 from ..utils.cancellation import register_cancellation_event
 
 LOGGER = logging.getLogger(__name__)
 
 
 class InitiatorManager:
     """A class to manage an initiator lifecycle"""
 
     def __init__(
             self,
-            handler_factory: Callable[[], Initiator],
+            handler_factory: Callable[[], InitiatorEngine],
             host: str,
             port: int,
             cancellation_event: asyncio.Event,
             *,
             ssl: Optional[SSLContext] = None,
             session_dow_range: Optional[Tuple[int, int]] = None,
             session_time_range: Optional[Tuple[time, time]] = None,
@@ -109,15 +109,15 @@
                         return_when=asyncio.FIRST_COMPLETED
                     )
                 except asyncio.TimeoutError:
                     pass
 
 
 def start_initiator_manager(
-        klass: Type[Initiator],
+        app: FIXApplication,
         host: str,
         port: int,
         protocol: ProtocolMetaData,
         sender_comp_id: str,
         target_comp_id: str,
         store: Store,
         logon_timeout: int,
@@ -129,17 +129,17 @@
         shutdown_timeout: float = 10.0,
         heartbeat_threshold: int = 1,
         logon_time_range: Optional[Tuple[time, time]] = None,
         tz: Optional[tzinfo] = None
 ) -> None:
     cancellation_event = asyncio.Event()
 
-    def initiator_factory() -> Initiator:
-        return create_initiator(
-            klass,
+    def initiator_factory() -> InitiatorEngine:
+        return InitiatorEngine(
+            app,
             protocol,
             sender_comp_id,
             target_comp_id,
             store,
             logon_timeout,
             heartbeat_timeout,
             cancellation_event,
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/persistence/file_store.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/file_store.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/persistence/sql_store.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/sql_store.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/time_provider.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/time_provider.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/__init__.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_events.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_events.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_read_buffer.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_read_buffer.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_reader_async.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_reader_async.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/fix_transport.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_transport.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_machine.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_machine.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,24 +15,25 @@
 from .types import (
     TransportState,
     TransportEvent,
     TransportMessage,
 )
 from .state_processor import TransportStateProcessor
 
-from ..types import FIXApplication
+from ..types import FIXEngine, FIXApplication
 
 LOGGER = logging.getLogger(__name__)
 
 
 class TransportStateMachine(TransportStateProcessor):
     """A state machine for the transport layer"""
 
     def __init__(
             self,
+            engine: FIXEngine,
             app: FIXApplication,
             admin_state_machine: AdminStateProcessor,
             time_provider: TimeProvider
     ) -> None:
         super().__init__(
             {
                 TransportState.DISCONNECTED: {
@@ -41,14 +42,15 @@
                 TransportState.CONNECTED: {
                     TransportEvent.FIX_RECEIVED: self._handle_fix,
                     TransportEvent.TIMEOUT_RECEIVED: self._handle_timeout,
                     TransportEvent.DISCONNECT_RECEIVED: self._handle_disconnect
                 }
             }
         )
+        self._engine = engine
         self._app = app
         self._admin_state_machine = admin_state_machine
         self._time_provider = time_provider
         self._last_receive_time_utc = self._time_provider.min(timezone.utc)
 
     async def _handle_connected(
             self,
@@ -60,40 +62,43 @@
         )
         return None
 
     async def _handle_fix(
             self,
             transport_message: TransportMessage
     ) -> Optional[TransportMessage]:
-        await self._app.session.save_message(transport_message.buffer)
+        await self._engine.session.save_message(transport_message.buffer)
 
-        fix_message = self._app.fix_message_factory.decode(
+        fix_message = self._engine.fix_message_factory.decode(
             transport_message.buffer
         )
         LOGGER.info('Received %s', fix_message.message)
 
         msgcat = cast(str, fix_message.meta_data.msgcat)
         if msgcat == 'admin':
             await self._handle_admin_message(fix_message.message)
         else:
-            await self._app.on_application_message(fix_message.message)
+            await self._app.on_application_message(
+                fix_message.message,
+                self._engine
+            )
 
         msg_seq_num: int = cast(int, fix_message.message['MsgSeqNum'])
-        await self._app.session.set_incoming_seqnum(msg_seq_num)
+        await self._engine.session.set_incoming_seqnum(msg_seq_num)
 
         self._last_receive_time_utc = self._time_provider.now(timezone.utc)
 
         return TransportMessage(TransportEvent.FIX_HANDLED)
 
     async def _handle_admin_message(self, message: Mapping[str, Any]) -> None:
         assert 'MsgType' in message
 
         LOGGER.info('admin message: %s', message)
 
-        await self._app.on_admin_message(message)
+        await self._app.on_admin_message(message, self._engine)
 
         await self._admin_state_machine.process(
             AdminMessage(
                 AdminEvent.from_msg_type(message['MsgType']),
                 message
             )
         )
@@ -105,16 +110,16 @@
         if self._admin_state_machine.state != AdminState.AUTHENTICATED:
             raise RuntimeError('Make a state for this')
 
         now_utc = self._time_provider.now(timezone.utc)
         seconds_since_last_receive = (
             now_utc - self._last_receive_time_utc
         ).total_seconds()
-        elapsed = seconds_since_last_receive - self._app.heartbeat_timeout
-        if elapsed > self._app.heartbeat_threshold:
+        elapsed = seconds_since_last_receive - self._engine.heartbeat_timeout
+        if elapsed > self._engine.heartbeat_threshold:
             await self._admin_state_machine.process(
                 AdminMessage(AdminEvent.TEST_HEARTBEAT_REQUIRED)
             )
 
         return TransportMessage(TransportEvent.TIMEOUT_HANDLED)
 
     async def _handle_disconnect(
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_processor.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_processor.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/state_transitions.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/transports/types.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/types.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/types.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/types.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """Types"""
 
 from abc import ABCMeta, abstractmethod
-from typing import Any, Mapping, Optional, Tuple
+from typing import Any, Awaitable, Callable, Mapping, Optional, Tuple
 
 from jetblack_fixparser.fix_message import FixMessageFactory
 
 
 class Session(metaclass=ABCMeta):
     """A FIX session"""
 
@@ -96,15 +96,15 @@
     """An invalid state transition"""
 
 
 class LoginError(Exception):
     """An invalid state transition"""
 
 
-class FIXApplication(metaclass=ABCMeta):
+class FIXEngine(metaclass=ABCMeta):
     """Abstract base class for FIX applications"""
 
     @property
     @abstractmethod
     def session(self) -> Session:
         """The session
 
@@ -127,60 +127,86 @@
         """The heartbeat timeout"""
 
     @property
     @abstractmethod
     def heartbeat_threshold(self) -> int:
         """The heartbeat threshold"""
 
-    async def on_admin_message(self, message: Mapping[str, Any]) -> None:
+    @abstractmethod
+    async def send_message(
+            self,
+            msg_type: str,
+            message: Optional[Mapping[str, Any]] = None
+    ) -> None:
+        """Send a FIX message
+
+        Args:
+            msg_type (str): The message type.
+            message (Optional[Mapping[str, Any]], optional): The message.
+                Defaults to None.
+        """
+
+
+class FIXApplication:
+    """The FIX application"""
+
+    async def on_admin_message(
+            self,
+            message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         """Called when an admin message is received.
 
         Args:
             message (Mapping[str, Any]): The admin message that was sent by the
                 acceptor.
+            fix_engine (FIXEngine): The FIX engine.
         """
 
-    async def on_heartbeat(self, message: Mapping[str, Any]) -> None:
+    async def on_heartbeat(
+            self,
+            message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         """Called when a heartbeat is received.
 
         Args:
             message (Mapping[str, Any]): The message sent by the acceptor.
+            fix_engine (FIXEngine): The FIX engine.
         """
 
-    @abstractmethod
-    async def on_application_message(self, message: Mapping[str, Any]) -> None:
+    async def on_application_message(
+            self,
+            message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         """Called when an application message is received.
 
         Args:
             message (Mapping[str, Any]): The application message sent by the
                 acceptor.
+            fix_engine (FIXEngine): The FIX engine.
         """
 
-    @abstractmethod
-    async def on_logon(self, message: Mapping[str, Any]) -> None:
+    async def on_logon(
+            self,
+            message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         """Called when a logon message is received.
 
         Args:
             message (Mapping[str, Any]): The message sent by the acceptor.
+            fix_engine (FIXEngine): The FIX engine.
         """
 
-    @abstractmethod
-    async def on_logout(self, message: Mapping[str, Any]) -> None:
-        """Called when a logout message is received.
-
-        Args:
-            message (Mapping[str, Any]): The message sent by the acceptor.
-        """
-
-    @abstractmethod
-    async def send_message(
+    async def on_logout(
             self,
-            msg_type: str,
-            message: Optional[Mapping[str, Any]] = None
+            message: Mapping[str, Any],
+            fix_engine: FIXEngine
     ) -> None:
-        """Send a FIX message
+        """Called when a logout message is received.
 
         Args:
-            msg_type (str): The message type.
-            message (Optional[Mapping[str, Any]], optional): The message.
-                Defaults to None.
+            message (Mapping[str, Any]): The message sent by the acceptor.
+            fix_engine (FIXEngine): The FIX engine.
         """
```

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/utils/cancellation.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/cancellation.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/jetblack_fixengine/utils/date_utils.py` & `jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/date_utils.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a3/pyproject.toml` & `jetblack-fixengine-1.0.0a4/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "jetblack-fixengine"
-version = "1.0.0-alpha.3"
+version = "1.0.0-alpha.4"
 description = "A pure Python implementation of the FIX protocol"
 authors = ["Rob Blackbourn <rob.blackbourn@googlemail.com>"]
 license = "Apache-2.0"
 packages = [
     { include = "jetblack_fixengine" }
 ]
 repository = "https://github.com/rob-blackbourn/jetblack-fixengine"
```

### Comparing `jetblack-fixengine-1.0.0a3/setup.py` & `jetblack-fixengine-1.0.0a4/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -19,17 +19,17 @@
  'aiosqlite>=0.18.0,<0.19.0',
  'jetblack-fixparser>=2.4,<3.0',
  'pytz>=2022.7,<2023.0',
  'tzlocal>=4.3,<5.0']
 
 setup_kwargs = {
     'name': 'jetblack-fixengine',
-    'version': '1.0.0a3',
+    'version': '1.0.0a4',
     'description': 'A pure Python implementation of the FIX protocol',
-    'long_description': '# jetblack-fixengine\n\nA pure python asyncio FIX engine implemented as a state machine.\n\n## Status\n\nThis is work in progress.\n\n## Installation\n\nThe package can be install from the pie store.\n\n```bash\npip install jetblack-fixengine\n```\n\n## Overview\n\nThis project provides a pure Python, asyncio implementation of\na FIX engine, supporting both initiators and acceptors.\n\nThe engine uses the [jetblack-fixparser](https://github.com/rob-blackbourn/jetblack-fixparser)\npackage to present the FIX messages a plain Python objects. For example, a `LOGON` message\ncan be sent as follows:\n\n```python\nawait send_message({\n    \'MsgType\': \'LOGON\',\n    \'MsgSeqNum\': 42,\n    \'SenderCompID\': \'ME\',\n    \'TargetCompID\': \'BANK OF SOMEWHERE\',\n    \'SendingTime\': datetime.now(timezone.utc),\n    \'EncryptMethod\': "NONE",\n    \'HeartBtInt\': 30\n})\n```\n\n### FIX Protocols\n\nThe FIX protocol is a combination of *well known* messages (like `LOGON`)\nand *custom* messages (like an order to buy or sell). The protocol\nhas evolved through a number of different versions providing new features.\n\nBecause of this the protocols are provided by config files. Historically\n`XML` was used. While this is supported, `yaml` is preferred and some\nexample protocols are provided in the\n[etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)\nfolder.\n\nCurrently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.\n\n### Initiators\n\nAn initiator is a class which inherits from `Initiator`, and implements a\nfew methods, and has access to `send_message`. Here is an example.\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import FileStore\nfrom jetblack_fixengine import start_initiator, Initiator\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyInitiator(Initiator):\n    """An instance of the initiator"""\n\n    async def on_logon(self, _message: Mapping[str, Any]) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(self, _message: Mapping[str, Any]) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(self, _message: Mapping[str, Any]) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path("store"))\nHOST = \'127.0.0.1\'\nPORT = 9801\nSENDER_COMP_ID = \'INITIATOR1\'\nTARGET_COMP_ID = \'ACCEPTOR\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_initiator(\n        MyInitiator,\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        LOGON_TIMEOUT,\n        HEARTBEAT_TIMEOUT,\n        shutdown_timeout=10\n    )\n)\n```\n\n### Acceptor\n\nThe acceptor works in the same way as the initiator. Here is an example:\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import FileStore\nfrom jetblack_fixengine import start_acceptor, Acceptor\n\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyAcceptor(Acceptor):\n    """An instance of the acceptor"""\n\n    async def on_logon(self, _message: Mapping[str, Any]):\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(self, _message: Mapping[str, Any]) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(self, _message: Mapping[str, Any]) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path("store"))\nHOST = \'0.0.0.0\'\nPORT = 9801\nSENDER_COMP_ID = \'ACCEPTOR\'\nTARGET_COMP_ID = \'INITIATOR1\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_acceptor(\n        MyAcceptor,\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        HEARTBEAT_TIMEOUT,\n        client_shutdown_timeout=10\n    )\n)\n```\n\nNote that throwing the exception `LogonError` from `on_logon` will reject\nthe logon request.\n\n### Stores\n\nThe engines need to store their state. Two stores are currently provided:\na file store (`FileStore`) and sqlite (`SqlStore`).\n\n## Implementation\n\nThe engines are implemented as state machines. This means they can be\ntested without the need for IO.\n',
+    'long_description': '# jetblack-fixengine\n\nA pure python asyncio FIX engine.\n\n## Status\n\nThis is work in progress.\n\n## Installation\n\nThe package can be install from the pie store.\n\n```bash\npip install jetblack-fixengine\n```\n\n## Overview\n\nThis project provides a pure Python, asyncio implementation of\na FIX engine, supporting both initiators and acceptors.\n\nThe engine uses the [jetblack-fixparser](https://github.com/rob-blackbourn/jetblack-fixparser)\npackage to present the FIX messages a plain Python objects. For example, a `LOGON` message\ncan be sent as follows:\n\n```python\nawait send_message({\n    \'MsgType\': \'LOGON\',\n    \'MsgSeqNum\': 42,\n    \'SenderCompID\': \'ME\',\n    \'TargetCompID\': \'BANK OF SOMEWHERE\',\n    \'SendingTime\': datetime.now(timezone.utc),\n    \'EncryptMethod\': "NONE",\n    \'HeartBtInt\': 30\n})\n```\n\n### FIX Protocols\n\nThe FIX protocol is a combination of *well known* messages (like `LOGON`)\nand *custom* messages (like an order to buy or sell). The protocol\nhas evolved through a number of different versions providing new features.\n\nBecause of this the protocols are provided by config files. Historically\n`XML` was used. While this is supported, `yaml` is preferred and some\nexample protocols are provided in the\n[etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)\nfolder.\n\nCurrently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.\n\n### Initiators\n\nAn initiator is a class which inherits from `FIXApplication`, and implements a\nfew methods, and has access to `send_message` from the `fix_engine`. Here is an example.\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_initiator,\n    FIXApplication,\n    FIXEngine\n)\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyInitiator(FIXApplication):\n    """An instance of the initiator"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path(\'store\'))\nHOST = \'127.0.0.1\'\nPORT = 9801\nSENDER_COMP_ID = \'INITIATOR1\'\nTARGET_COMP_ID = \'ACCEPTOR\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_initiator(\n        MyInitiator(),\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        LOGON_TIMEOUT,\n        HEARTBEAT_TIMEOUT,\n        shutdown_timeout=10\n    )\n)\n```\n\n### Acceptor\n\nThe acceptor works in the same way as the initiator. Here is an example:\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_acceptor,\n    FIXApplication,\n    FIXEngine\n)\n\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyAcceptor(FIXApplication):\n    """An instance of the acceptor"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path("store"))\nHOST = \'0.0.0.0\'\nPORT = 9801\nSENDER_COMP_ID = \'ACCEPTOR\'\nTARGET_COMP_ID = \'INITIATOR1\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_acceptor(\n        MyAcceptor(),\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        HEARTBEAT_TIMEOUT,\n        client_shutdown_timeout=10\n    )\n)\n```\n\nNote that throwing the exception `LogonError` from `on_logon` will reject\nthe logon request.\n\n### Stores\n\nThe engines need to store their state. Two stores are currently provided:\na file store (`FileStore`) and sqlite (`SqlStore`).\n\n## Implementation\n\nThe engines are implemented as state machines. This means they can be\ntested without the need for IO.\n',
     'author': 'Rob Blackbourn',
     'author_email': 'rob.blackbourn@googlemail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/rob-blackbourn/jetblack-fixengine',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `jetblack-fixengine-1.0.0a3/PKG-INFO` & `jetblack-fixengine-1.0.0a4/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jetblack-fixengine
-Version: 1.0.0a3
+Version: 1.0.0a4
 Summary: A pure Python implementation of the FIX protocol
 Home-page: https://github.com/rob-blackbourn/jetblack-fixengine
 License: Apache-2.0
 Keywords: fix,fix-engine
 Author: Rob Blackbourn
 Author-email: rob.blackbourn@googlemail.com
 Requires-Python: >=3.8,<4.0
@@ -19,15 +19,15 @@
 Requires-Dist: pytz (>=2022.7,<2023.0)
 Requires-Dist: tzlocal (>=4.3,<5.0)
 Project-URL: Repository, https://github.com/rob-blackbourn/jetblack-fixengine
 Description-Content-Type: text/markdown
 
 # jetblack-fixengine
 
-A pure python asyncio FIX engine implemented as a state machine.
+A pure python asyncio FIX engine.
 
 ## Status
 
 This is work in progress.
 
 ## Installation
 
@@ -70,57 +70,73 @@
 [etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)
 folder.
 
 Currently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.
 
 ### Initiators
 
-An initiator is a class which inherits from `Initiator`, and implements a
-few methods, and has access to `send_message`. Here is an example.
+An initiator is a class which inherits from `FIXApplication`, and implements a
+few methods, and has access to `send_message` from the `fix_engine`. Here is an example.
 
 ```python
 import asyncio
 import logging
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
-from jetblack_fixengine import FileStore
-from jetblack_fixengine import start_initiator, Initiator
+from jetblack_fixengine import (
+    FileStore,
+    start_initiator,
+    FIXApplication,
+    FIXEngine
+)
 
 LOGGER = logging.getLogger(__name__)
 
 
-class MyInitiator(Initiator):
+class MyInitiator(FIXApplication):
     """An instance of the initiator"""
 
-    async def on_logon(self, _message: Mapping[str, Any]) -> None:
+    async def on_logon(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logon')
 
-    async def on_logout(self, _message: Mapping[str, Any]) -> None:
+    async def on_logout(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logout')
 
-    async def on_application_message(self, _message: Mapping[str, Any]) -> None:
+    async def on_application_message(
+            self,
+            _message: Mapping[str, Any],
+            fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_application_message')
 
 
 PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path("store"))
+STORE = FileStore(Path('store'))
 HOST = '127.0.0.1'
 PORT = 9801
 SENDER_COMP_ID = 'INITIATOR1'
 TARGET_COMP_ID = 'ACCEPTOR'
 LOGON_TIMEOUT = 60
 HEARTBEAT_TIMEOUT = 30
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
     start_initiator(
-        MyInitiator,
+        MyInitiator(),
         HOST,
         PORT,
         PROTOCOL,
         SENDER_COMP_ID,
         TARGET_COMP_ID,
         STORE,
         LOGON_TIMEOUT,
@@ -137,31 +153,47 @@
 ```python
 import asyncio
 import logging
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
-from jetblack_fixengine import FileStore
-from jetblack_fixengine import start_acceptor, Acceptor
+from jetblack_fixengine import (
+    FileStore,
+    start_acceptor,
+    FIXApplication,
+    FIXEngine
+)
 
 
 LOGGER = logging.getLogger(__name__)
 
 
-class MyAcceptor(Acceptor):
+class MyAcceptor(FIXApplication):
     """An instance of the acceptor"""
 
-    async def on_logon(self, _message: Mapping[str, Any]):
+    async def on_logon(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logon')
 
-    async def on_logout(self, _message: Mapping[str, Any]) -> None:
+    async def on_logout(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_logout')
 
-    async def on_application_message(self, _message: Mapping[str, Any]) -> None:
+    async def on_application_message(
+            self,
+            _message: Mapping[str, Any],
+            _fix_engine: FIXEngine
+    ) -> None:
         LOGGER.info('on_application_message')
 
 
 PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
 STORE = FileStore(Path("store"))
 HOST = '0.0.0.0'
 PORT = 9801
@@ -170,15 +202,15 @@
 LOGON_TIMEOUT = 60
 HEARTBEAT_TIMEOUT = 30
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
     start_acceptor(
-        MyAcceptor,
+        MyAcceptor(),
         HOST,
         PORT,
         PROTOCOL,
         SENDER_COMP_ID,
         TARGET_COMP_ID,
         STORE,
         HEARTBEAT_TIMEOUT,
```

