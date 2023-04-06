# Comparing `tmp/jetblack-fixengine-1.0.0a4.tar.gz` & `tmp/jetblack-fixengine-1.0.0a5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jetblack-fixengine-1.0.0a4.tar", max compression
+gzip compressed data, was "jetblack-fixengine-1.0.0a5.tar", max compression
```

## Comparing `jetblack-fixengine-1.0.0a4.tar` & `jetblack-fixengine-1.0.0a5.tar`

### file list

```diff
@@ -1,42 +1,42 @@
--rw-r--r--   0        0        0    11357 2023-03-19 08:07:10.647832 jetblack-fixengine-1.0.0a4/LICENSE
--rw-r--r--   0        0        0     4797 2023-04-06 08:13:02.362705 jetblack-fixengine-1.0.0a4/README.md
--rw-r--r--   0        0        0      370 2023-04-06 08:13:02.363241 jetblack-fixengine-1.0.0a4/jetblack_fixengine/__init__.py
--rw-r--r--   0        0        0       88 2023-04-06 08:13:02.363414 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/__init__.py
--rw-r--r--   0        0        0     8030 2023-04-06 08:13:02.363681 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/acceptor.py
--rw-r--r--   0        0        0     2618 2023-04-06 08:13:02.363870 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/helpers.py
--rw-r--r--   0        0        0     6585 2023-04-06 08:13:02.364011 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_machine.py
--rw-r--r--   0        0        0     1757 2023-04-02 10:52:10.219438 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_transitions.py
--rw-r--r--   0        0        0      727 2023-04-06 08:13:02.364136 jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/types.py
--rw-r--r--   0        0        0      217 2023-04-02 07:49:31.247277 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/__init__.py
--rw-r--r--   0        0        0     1232 2023-04-02 07:49:31.247472 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_processor.py
--rw-r--r--   0        0        0     1292 2023-04-02 07:49:31.247618 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_transitions.py
--rw-r--r--   0        0        0     3064 2023-04-02 07:49:31.247760 jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/types.py
--rw-r--r--   0        0        0      193 2023-04-06 08:13:02.364275 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/__init__.py
--rw-r--r--   0        0        0     2585 2023-04-06 08:13:02.364454 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/helpers.py
--rw-r--r--   0        0        0     6158 2023-04-06 08:13:02.364596 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/initiator.py
--rw-r--r--   0        0        0     4998 2023-04-06 08:13:02.364752 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_machine.py
--rw-r--r--   0        0        0     1907 2023-04-02 10:52:02.577886 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_transitions.py
--rw-r--r--   0        0        0      172 2023-04-06 08:13:02.364900 jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/types.py
--rw-r--r--   0        0        0      158 2023-03-19 08:07:10.650053 jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/__init__.py
--rw-r--r--   0        0        0     5298 2023-04-06 08:13:02.365074 jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/initiator_manager.py
--rw-r--r--   0        0        0      132 2023-04-02 10:53:31.600244 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/__init__.py
--rw-r--r--   0        0        0     4438 2023-04-02 10:32:31.244717 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/file_store.py
--rw-r--r--   0        0        0     5967 2023-04-02 10:43:23.846629 jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/sql_store.py
--rw-r--r--   0        0        0        0 2023-04-02 07:49:31.249061 jetblack-fixengine-1.0.0a4/jetblack_fixengine/py.typed
--rw-r--r--   0        0        0      629 2023-04-02 11:07:45.608721 jetblack-fixengine-1.0.0a4/jetblack_fixengine/time_provider.py
--rw-r--r--   0        0        0      568 2023-04-02 07:49:31.249427 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/__init__.py
--rw-r--r--   0        0        0     1559 2023-04-02 07:49:31.249786 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_events.py
--rw-r--r--   0        0        0     8197 2023-03-19 15:22:36.371647 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_read_buffer.py
--rw-r--r--   0        0        0     1383 2023-04-02 07:49:31.250207 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_reader_async.py
--rw-r--r--   0        0        0     6326 2023-04-02 07:49:31.250445 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_transport.py
--rw-r--r--   0        0        0     4153 2023-04-06 08:13:02.365244 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_machine.py
--rw-r--r--   0        0        0     1327 2023-04-02 10:55:07.384675 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_processor.py
--rw-r--r--   0        0        0     1785 2023-04-02 10:55:49.604609 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_transitions.py
--rw-r--r--   0        0        0     1161 2023-04-02 07:49:31.251203 jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/types.py
--rw-r--r--   0        0        0     5224 2023-04-06 08:13:02.365382 jetblack-fixengine-1.0.0a4/jetblack_fixengine/types.py
--rw-r--r--   0        0        0        0 2023-03-19 08:07:10.651512 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/__init__.py
--rw-r--r--   0        0        0     1091 2023-04-02 10:58:04.048732 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/cancellation.py
--rw-r--r--   0        0        0     3099 2023-04-02 11:05:21.329690 jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/date_utils.py
--rw-r--r--   0        0        0      818 2023-04-06 08:13:13.312818 jetblack-fixengine-1.0.0a4/pyproject.toml
--rw-r--r--   0        0        0     6110 2023-04-06 08:17:43.714063 jetblack-fixengine-1.0.0a4/setup.py
--rw-r--r--   0        0        0     5710 2023-04-06 08:17:43.714558 jetblack-fixengine-1.0.0a4/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-03-19 08:07:10.647832 jetblack-fixengine-1.0.0a5/LICENSE
+-rw-r--r--   0        0        0     4403 2023-04-06 09:51:46.854533 jetblack-fixengine-1.0.0a5/README.md
+-rw-r--r--   0        0        0      448 2023-04-06 09:51:46.855181 jetblack-fixengine-1.0.0a5/jetblack_fixengine/__init__.py
+-rw-r--r--   0        0        0      144 2023-04-06 09:51:46.855359 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/__init__.py
+-rw-r--r--   0        0        0     8030 2023-04-06 08:13:02.363681 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/acceptor.py
+-rw-r--r--   0        0        0     2188 2023-04-06 09:51:46.855534 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/helpers.py
+-rw-r--r--   0        0        0     6585 2023-04-06 08:13:02.364011 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/state_machine.py
+-rw-r--r--   0        0        0     1757 2023-04-02 10:52:10.219438 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/state_transitions.py
+-rw-r--r--   0        0        0     2143 2023-04-06 09:51:46.855711 jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/types.py
+-rw-r--r--   0        0        0      217 2023-04-02 07:49:31.247277 jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/__init__.py
+-rw-r--r--   0        0        0     1232 2023-04-02 07:49:31.247472 jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/state_processor.py
+-rw-r--r--   0        0        0     1292 2023-04-02 07:49:31.247618 jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/state_transitions.py
+-rw-r--r--   0        0        0     3064 2023-04-02 07:49:31.247760 jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/types.py
+-rw-r--r--   0        0        0      250 2023-04-06 09:51:46.855880 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/__init__.py
+-rw-r--r--   0        0        0     2386 2023-04-06 09:51:46.856047 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/helpers.py
+-rw-r--r--   0        0        0     6158 2023-04-06 08:13:02.364596 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/initiator.py
+-rw-r--r--   0        0        0     4998 2023-04-06 08:13:02.364752 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/state_machine.py
+-rw-r--r--   0        0        0     1907 2023-04-02 10:52:02.577886 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/state_transitions.py
+-rw-r--r--   0        0        0     1193 2023-04-06 09:51:46.856228 jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/types.py
+-rw-r--r--   0        0        0      158 2023-03-19 08:07:10.650053 jetblack-fixengine-1.0.0a5/jetblack_fixengine/managers/__init__.py
+-rw-r--r--   0        0        0     5298 2023-04-06 08:13:02.365074 jetblack-fixengine-1.0.0a5/jetblack_fixengine/managers/initiator_manager.py
+-rw-r--r--   0        0        0      132 2023-04-02 10:53:31.600244 jetblack-fixengine-1.0.0a5/jetblack_fixengine/persistence/__init__.py
+-rw-r--r--   0        0        0     4438 2023-04-02 10:32:31.244717 jetblack-fixengine-1.0.0a5/jetblack_fixengine/persistence/file_store.py
+-rw-r--r--   0        0        0     5967 2023-04-02 10:43:23.846629 jetblack-fixengine-1.0.0a5/jetblack_fixengine/persistence/sql_store.py
+-rw-r--r--   0        0        0        0 2023-04-02 07:49:31.249061 jetblack-fixengine-1.0.0a5/jetblack_fixengine/py.typed
+-rw-r--r--   0        0        0      629 2023-04-02 11:07:45.608721 jetblack-fixengine-1.0.0a5/jetblack_fixengine/time_provider.py
+-rw-r--r--   0        0        0      568 2023-04-02 07:49:31.249427 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/__init__.py
+-rw-r--r--   0        0        0     1559 2023-04-02 07:49:31.249786 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_events.py
+-rw-r--r--   0        0        0     8197 2023-03-19 15:22:36.371647 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_read_buffer.py
+-rw-r--r--   0        0        0     1383 2023-04-02 07:49:31.250207 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_reader_async.py
+-rw-r--r--   0        0        0     6326 2023-04-02 07:49:31.250445 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_transport.py
+-rw-r--r--   0        0        0     4153 2023-04-06 08:13:02.365244 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_machine.py
+-rw-r--r--   0        0        0     1327 2023-04-02 10:55:07.384675 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_processor.py
+-rw-r--r--   0        0        0     1785 2023-04-02 10:55:49.604609 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_transitions.py
+-rw-r--r--   0        0        0     1161 2023-04-02 07:49:31.251203 jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/types.py
+-rw-r--r--   0        0        0     5224 2023-04-06 08:13:02.365382 jetblack-fixengine-1.0.0a5/jetblack_fixengine/types.py
+-rw-r--r--   0        0        0        0 2023-03-19 08:07:10.651512 jetblack-fixengine-1.0.0a5/jetblack_fixengine/utils/__init__.py
+-rw-r--r--   0        0        0     1091 2023-04-02 10:58:04.048732 jetblack-fixengine-1.0.0a5/jetblack_fixengine/utils/cancellation.py
+-rw-r--r--   0        0        0     3099 2023-04-02 11:05:21.329690 jetblack-fixengine-1.0.0a5/jetblack_fixengine/utils/date_utils.py
+-rw-r--r--   0        0        0      818 2023-04-06 09:52:34.131920 jetblack-fixengine-1.0.0a5/pyproject.toml
+-rw-r--r--   0        0        0     5702 2023-04-06 09:53:33.531630 jetblack-fixengine-1.0.0a5/setup.py
+-rw-r--r--   0        0        0     5316 2023-04-06 09:53:33.532100 jetblack-fixengine-1.0.0a5/PKG-INFO
```

### Comparing `jetblack-fixengine-1.0.0a4/LICENSE` & `jetblack-fixengine-1.0.0a5/LICENSE`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/README.md` & `jetblack-fixengine-1.0.0a5/README.md`

 * *Files 13% similar despite different names*

```diff
@@ -60,14 +60,15 @@
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
 from jetblack_fixengine import (
     FileStore,
     start_initiator,
+    InitiatorConfig,
     FIXApplication,
     FIXEngine
 )
 
 LOGGER = logging.getLogger(__name__)
 
 
@@ -92,38 +93,28 @@
             self,
             _message: Mapping[str, Any],
             fix_engine: FIXEngine
     ) -> None:
         LOGGER.info('on_application_message')
 
 
-PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path('store'))
-HOST = '127.0.0.1'
-PORT = 9801
-SENDER_COMP_ID = 'INITIATOR1'
-TARGET_COMP_ID = 'ACCEPTOR'
-LOGON_TIMEOUT = 60
-HEARTBEAT_TIMEOUT = 30
+app = MyInitiator()
+config = InitiatorConfig(
+    '127.0.0.1',
+    9801,
+    load_yaml_protocol(Path('etc') / 'FIX44.yaml'),
+    'INITIATOR1',
+    'ACCEPTOR',
+    FileStore(Path('store'))
+)
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
-    start_initiator(
-        MyInitiator(),
-        HOST,
-        PORT,
-        PROTOCOL,
-        SENDER_COMP_ID,
-        TARGET_COMP_ID,
-        STORE,
-        LOGON_TIMEOUT,
-        HEARTBEAT_TIMEOUT,
-        shutdown_timeout=10
-    )
+    start_initiator(app, config)
 )
 ```
 
 ### Acceptor
 
 The acceptor works in the same way as the initiator. Here is an example:
 
@@ -133,14 +124,15 @@
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
 from jetblack_fixengine import (
     FileStore,
     start_acceptor,
+    AcceptorConfig,
     FIXApplication,
     FIXEngine
 )
 
 
 LOGGER = logging.getLogger(__name__)
 
@@ -166,36 +158,30 @@
             self,
             _message: Mapping[str, Any],
             _fix_engine: FIXEngine
     ) -> None:
         LOGGER.info('on_application_message')
 
 
-PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path("store"))
-HOST = '0.0.0.0'
-PORT = 9801
-SENDER_COMP_ID = 'ACCEPTOR'
-TARGET_COMP_ID = 'INITIATOR1'
-LOGON_TIMEOUT = 60
-HEARTBEAT_TIMEOUT = 30
-
 logging.basicConfig(level=logging.DEBUG)
 
+app = MyAcceptor()
+config = AcceptorConfig(
+    '0.0.0.0',
+    9801,
+    load_yaml_protocol(Path('etc') / 'FIX44.yaml'),
+    'ACCEPTOR',
+    'INITIATOR1',
+    FileStore(Path("store"))
+)
+
 asyncio.run(
     start_acceptor(
-        MyAcceptor(),
-        HOST,
-        PORT,
-        PROTOCOL,
-        SENDER_COMP_ID,
-        TARGET_COMP_ID,
-        STORE,
-        HEARTBEAT_TIMEOUT,
-        client_shutdown_timeout=10
+        app,
+        config
     )
 )
 ```
 
 Note that throwing the exception `LogonError` from `on_logon` will reject
 the logon request.
```

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/acceptor.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/acceptor.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_machine.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/state_machine.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/acceptor/state_transitions.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/acceptor/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_processor.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/state_processor.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/state_transitions.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/admin/types.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/admin/types.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/helpers.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/helpers.py`

 * *Files 15% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 from ..transports import TransportHandler
 from ..types import Store, FIXApplication
 from ..utils.cancellation import register_cancellation_event
 
 from ..transports import fix_stream_processor,  FixReadBuffer, fix_read_async
 
 from .initiator import InitiatorEngine
+from .types import InitiatorConfig
 
 LOGGER = logging.getLogger(__name__)
 
 InitiatorFactory = Callable[
     [ProtocolMetaData, str, str, Store, int, asyncio.Event],
     TransportHandler
 ]
@@ -61,44 +62,33 @@
         port,
         " over ssl" if ssl else ""
     )
 
 
 async def start_initiator(
         app: FIXApplication,
-        host: str,
-        port: int,
-        protocol: ProtocolMetaData,
-        sender_comp_id: str,
-        target_comp_id: str,
-        store: Store,
-        logon_timeout: int,
-        heartbeat_timeout: int,
-        *,
-        ssl: Optional[SSLContext] = None,
-        shutdown_timeout: float = 10.0,
-        heartbeat_threshold: int = 1
+        config: InitiatorConfig,
 ) -> None:
     cancellation_event = Event()
     loop = asyncio.get_event_loop()
     register_cancellation_event(cancellation_event, loop)
 
     engine = InitiatorEngine(
         app,
-        protocol,
-        sender_comp_id,
-        target_comp_id,
-        store,
-        logon_timeout,
-        heartbeat_timeout,
+        config.protocol,
+        config.sender_comp_id,
+        config.target_comp_id,
+        config.store,
+        config.logon_timeout,
+        config.heartbeat_timeout,
         cancellation_event,
-        heartbeat_threshold=heartbeat_threshold
+        heartbeat_threshold=config.heartbeat_threshold
     )
 
     await initiate(
-        host,
-        port,
+        config.host,
+        config.port,
         engine,
         cancellation_event,
-        ssl=ssl,
-        shutdown_timeout=shutdown_timeout
+        ssl=config.ssl,
+        shutdown_timeout=config.shutdown_timeout
     )
```

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/initiator.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/initiator.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_machine.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/state_machine.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/initiator/state_transitions.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/initiator/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/managers/initiator_manager.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/managers/initiator_manager.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/file_store.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/persistence/file_store.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/persistence/sql_store.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/persistence/sql_store.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/time_provider.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/time_provider.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/__init__.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_events.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_events.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_read_buffer.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_read_buffer.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_reader_async.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_reader_async.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/fix_transport.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/fix_transport.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_machine.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_machine.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_processor.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_processor.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/state_transitions.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/state_transitions.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/transports/types.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/transports/types.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/types.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/types.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/cancellation.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/utils/cancellation.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/jetblack_fixengine/utils/date_utils.py` & `jetblack-fixengine-1.0.0a5/jetblack_fixengine/utils/date_utils.py`

 * *Files identical despite different names*

### Comparing `jetblack-fixengine-1.0.0a4/pyproject.toml` & `jetblack-fixengine-1.0.0a5/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "jetblack-fixengine"
-version = "1.0.0-alpha.4"
+version = "1.0.0-alpha.5"
 description = "A pure Python implementation of the FIX protocol"
 authors = ["Rob Blackbourn <rob.blackbourn@googlemail.com>"]
 license = "Apache-2.0"
 packages = [
     { include = "jetblack_fixengine" }
 ]
 repository = "https://github.com/rob-blackbourn/jetblack-fixengine"
```

### Comparing `jetblack-fixengine-1.0.0a4/setup.py` & `jetblack-fixengine-1.0.0a5/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -19,17 +19,17 @@
  'aiosqlite>=0.18.0,<0.19.0',
  'jetblack-fixparser>=2.4,<3.0',
  'pytz>=2022.7,<2023.0',
  'tzlocal>=4.3,<5.0']
 
 setup_kwargs = {
     'name': 'jetblack-fixengine',
-    'version': '1.0.0a4',
+    'version': '1.0.0a5',
     'description': 'A pure Python implementation of the FIX protocol',
-    'long_description': '# jetblack-fixengine\n\nA pure python asyncio FIX engine.\n\n## Status\n\nThis is work in progress.\n\n## Installation\n\nThe package can be install from the pie store.\n\n```bash\npip install jetblack-fixengine\n```\n\n## Overview\n\nThis project provides a pure Python, asyncio implementation of\na FIX engine, supporting both initiators and acceptors.\n\nThe engine uses the [jetblack-fixparser](https://github.com/rob-blackbourn/jetblack-fixparser)\npackage to present the FIX messages a plain Python objects. For example, a `LOGON` message\ncan be sent as follows:\n\n```python\nawait send_message({\n    \'MsgType\': \'LOGON\',\n    \'MsgSeqNum\': 42,\n    \'SenderCompID\': \'ME\',\n    \'TargetCompID\': \'BANK OF SOMEWHERE\',\n    \'SendingTime\': datetime.now(timezone.utc),\n    \'EncryptMethod\': "NONE",\n    \'HeartBtInt\': 30\n})\n```\n\n### FIX Protocols\n\nThe FIX protocol is a combination of *well known* messages (like `LOGON`)\nand *custom* messages (like an order to buy or sell). The protocol\nhas evolved through a number of different versions providing new features.\n\nBecause of this the protocols are provided by config files. Historically\n`XML` was used. While this is supported, `yaml` is preferred and some\nexample protocols are provided in the\n[etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)\nfolder.\n\nCurrently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.\n\n### Initiators\n\nAn initiator is a class which inherits from `FIXApplication`, and implements a\nfew methods, and has access to `send_message` from the `fix_engine`. Here is an example.\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_initiator,\n    FIXApplication,\n    FIXEngine\n)\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyInitiator(FIXApplication):\n    """An instance of the initiator"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path(\'store\'))\nHOST = \'127.0.0.1\'\nPORT = 9801\nSENDER_COMP_ID = \'INITIATOR1\'\nTARGET_COMP_ID = \'ACCEPTOR\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_initiator(\n        MyInitiator(),\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        LOGON_TIMEOUT,\n        HEARTBEAT_TIMEOUT,\n        shutdown_timeout=10\n    )\n)\n```\n\n### Acceptor\n\nThe acceptor works in the same way as the initiator. Here is an example:\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_acceptor,\n    FIXApplication,\n    FIXEngine\n)\n\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyAcceptor(FIXApplication):\n    """An instance of the acceptor"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nPROTOCOL = load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\')\nSTORE = FileStore(Path("store"))\nHOST = \'0.0.0.0\'\nPORT = 9801\nSENDER_COMP_ID = \'ACCEPTOR\'\nTARGET_COMP_ID = \'INITIATOR1\'\nLOGON_TIMEOUT = 60\nHEARTBEAT_TIMEOUT = 30\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_acceptor(\n        MyAcceptor(),\n        HOST,\n        PORT,\n        PROTOCOL,\n        SENDER_COMP_ID,\n        TARGET_COMP_ID,\n        STORE,\n        HEARTBEAT_TIMEOUT,\n        client_shutdown_timeout=10\n    )\n)\n```\n\nNote that throwing the exception `LogonError` from `on_logon` will reject\nthe logon request.\n\n### Stores\n\nThe engines need to store their state. Two stores are currently provided:\na file store (`FileStore`) and sqlite (`SqlStore`).\n\n## Implementation\n\nThe engines are implemented as state machines. This means they can be\ntested without the need for IO.\n',
+    'long_description': '# jetblack-fixengine\n\nA pure python asyncio FIX engine.\n\n## Status\n\nThis is work in progress.\n\n## Installation\n\nThe package can be install from the pie store.\n\n```bash\npip install jetblack-fixengine\n```\n\n## Overview\n\nThis project provides a pure Python, asyncio implementation of\na FIX engine, supporting both initiators and acceptors.\n\nThe engine uses the [jetblack-fixparser](https://github.com/rob-blackbourn/jetblack-fixparser)\npackage to present the FIX messages a plain Python objects. For example, a `LOGON` message\ncan be sent as follows:\n\n```python\nawait send_message({\n    \'MsgType\': \'LOGON\',\n    \'MsgSeqNum\': 42,\n    \'SenderCompID\': \'ME\',\n    \'TargetCompID\': \'BANK OF SOMEWHERE\',\n    \'SendingTime\': datetime.now(timezone.utc),\n    \'EncryptMethod\': "NONE",\n    \'HeartBtInt\': 30\n})\n```\n\n### FIX Protocols\n\nThe FIX protocol is a combination of *well known* messages (like `LOGON`)\nand *custom* messages (like an order to buy or sell). The protocol\nhas evolved through a number of different versions providing new features.\n\nBecause of this the protocols are provided by config files. Historically\n`XML` was used. While this is supported, `yaml` is preferred and some\nexample protocols are provided in the\n[etc](https://github.com/rob-blackbourn/jetblack-fixengine/tree/master/etc)\nfolder.\n\nCurrently supported versions are 4.0, 4.1, 4.2, 4.3, 4.4.\n\n### Initiators\n\nAn initiator is a class which inherits from `FIXApplication`, and implements a\nfew methods, and has access to `send_message` from the `fix_engine`. Here is an example.\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_initiator,\n    InitiatorConfig,\n    FIXApplication,\n    FIXEngine\n)\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyInitiator(FIXApplication):\n    """An instance of the initiator"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\napp = MyInitiator()\nconfig = InitiatorConfig(\n    \'127.0.0.1\',\n    9801,\n    load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\'),\n    \'INITIATOR1\',\n    \'ACCEPTOR\',\n    FileStore(Path(\'store\'))\n)\n\nlogging.basicConfig(level=logging.DEBUG)\n\nasyncio.run(\n    start_initiator(app, config)\n)\n```\n\n### Acceptor\n\nThe acceptor works in the same way as the initiator. Here is an example:\n\n```python\nimport asyncio\nimport logging\nfrom pathlib import Path\nfrom typing import Mapping, Any\n\nfrom jetblack_fixparser import load_yaml_protocol\nfrom jetblack_fixengine import (\n    FileStore,\n    start_acceptor,\n    AcceptorConfig,\n    FIXApplication,\n    FIXEngine\n)\n\n\nLOGGER = logging.getLogger(__name__)\n\n\nclass MyAcceptor(FIXApplication):\n    """An instance of the acceptor"""\n\n    async def on_logon(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logon\')\n\n    async def on_logout(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_logout\')\n\n    async def on_application_message(\n            self,\n            _message: Mapping[str, Any],\n            _fix_engine: FIXEngine\n    ) -> None:\n        LOGGER.info(\'on_application_message\')\n\n\nlogging.basicConfig(level=logging.DEBUG)\n\napp = MyAcceptor()\nconfig = AcceptorConfig(\n    \'0.0.0.0\',\n    9801,\n    load_yaml_protocol(Path(\'etc\') / \'FIX44.yaml\'),\n    \'ACCEPTOR\',\n    \'INITIATOR1\',\n    FileStore(Path("store"))\n)\n\nasyncio.run(\n    start_acceptor(\n        app,\n        config\n    )\n)\n```\n\nNote that throwing the exception `LogonError` from `on_logon` will reject\nthe logon request.\n\n### Stores\n\nThe engines need to store their state. Two stores are currently provided:\na file store (`FileStore`) and sqlite (`SqlStore`).\n\n## Implementation\n\nThe engines are implemented as state machines. This means they can be\ntested without the need for IO.\n',
     'author': 'Rob Blackbourn',
     'author_email': 'rob.blackbourn@googlemail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/rob-blackbourn/jetblack-fixengine',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `jetblack-fixengine-1.0.0a4/PKG-INFO` & `jetblack-fixengine-1.0.0a5/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jetblack-fixengine
-Version: 1.0.0a4
+Version: 1.0.0a5
 Summary: A pure Python implementation of the FIX protocol
 Home-page: https://github.com/rob-blackbourn/jetblack-fixengine
 License: Apache-2.0
 Keywords: fix,fix-engine
 Author: Rob Blackbourn
 Author-email: rob.blackbourn@googlemail.com
 Requires-Python: >=3.8,<4.0
@@ -83,14 +83,15 @@
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
 from jetblack_fixengine import (
     FileStore,
     start_initiator,
+    InitiatorConfig,
     FIXApplication,
     FIXEngine
 )
 
 LOGGER = logging.getLogger(__name__)
 
 
@@ -115,38 +116,28 @@
             self,
             _message: Mapping[str, Any],
             fix_engine: FIXEngine
     ) -> None:
         LOGGER.info('on_application_message')
 
 
-PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path('store'))
-HOST = '127.0.0.1'
-PORT = 9801
-SENDER_COMP_ID = 'INITIATOR1'
-TARGET_COMP_ID = 'ACCEPTOR'
-LOGON_TIMEOUT = 60
-HEARTBEAT_TIMEOUT = 30
+app = MyInitiator()
+config = InitiatorConfig(
+    '127.0.0.1',
+    9801,
+    load_yaml_protocol(Path('etc') / 'FIX44.yaml'),
+    'INITIATOR1',
+    'ACCEPTOR',
+    FileStore(Path('store'))
+)
 
 logging.basicConfig(level=logging.DEBUG)
 
 asyncio.run(
-    start_initiator(
-        MyInitiator(),
-        HOST,
-        PORT,
-        PROTOCOL,
-        SENDER_COMP_ID,
-        TARGET_COMP_ID,
-        STORE,
-        LOGON_TIMEOUT,
-        HEARTBEAT_TIMEOUT,
-        shutdown_timeout=10
-    )
+    start_initiator(app, config)
 )
 ```
 
 ### Acceptor
 
 The acceptor works in the same way as the initiator. Here is an example:
 
@@ -156,14 +147,15 @@
 from pathlib import Path
 from typing import Mapping, Any
 
 from jetblack_fixparser import load_yaml_protocol
 from jetblack_fixengine import (
     FileStore,
     start_acceptor,
+    AcceptorConfig,
     FIXApplication,
     FIXEngine
 )
 
 
 LOGGER = logging.getLogger(__name__)
 
@@ -189,36 +181,30 @@
             self,
             _message: Mapping[str, Any],
             _fix_engine: FIXEngine
     ) -> None:
         LOGGER.info('on_application_message')
 
 
-PROTOCOL = load_yaml_protocol(Path('etc') / 'FIX44.yaml')
-STORE = FileStore(Path("store"))
-HOST = '0.0.0.0'
-PORT = 9801
-SENDER_COMP_ID = 'ACCEPTOR'
-TARGET_COMP_ID = 'INITIATOR1'
-LOGON_TIMEOUT = 60
-HEARTBEAT_TIMEOUT = 30
-
 logging.basicConfig(level=logging.DEBUG)
 
+app = MyAcceptor()
+config = AcceptorConfig(
+    '0.0.0.0',
+    9801,
+    load_yaml_protocol(Path('etc') / 'FIX44.yaml'),
+    'ACCEPTOR',
+    'INITIATOR1',
+    FileStore(Path("store"))
+)
+
 asyncio.run(
     start_acceptor(
-        MyAcceptor(),
-        HOST,
-        PORT,
-        PROTOCOL,
-        SENDER_COMP_ID,
-        TARGET_COMP_ID,
-        STORE,
-        HEARTBEAT_TIMEOUT,
-        client_shutdown_timeout=10
+        app,
+        config
     )
 )
 ```
 
 Note that throwing the exception `LogonError` from `on_logon` will reject
 the logon request.
```

