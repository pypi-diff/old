# Comparing `tmp/broker_grpc_lib-0.3.5.tar.gz` & `tmp/broker_grpc_lib-0.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "broker_grpc_lib-0.3.5.tar", last modified: Thu Apr  6 14:04:10 2023, max compression
+gzip compressed data, was "broker_grpc_lib-0.3.6.tar", last modified: Thu Apr  6 14:09:29 2023, max compression
```

## Comparing `broker_grpc_lib-0.3.5.tar` & `broker_grpc_lib-0.3.6.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.841662 broker_grpc_lib-0.3.5/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 14:04:10.841508 broker_grpc_lib-0.3.5/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      578 2023-04-06 07:45:45.000000 broker_grpc_lib-0.3.5/README.md
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.836712 broker_grpc_lib-0.3.5/broker_grpc_lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.838053 broker_grpc_lib-0.3.5/broker_grpc_lib/exc/
--rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/exc/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/exc/no_queue_exception.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.839114 broker_grpc_lib-0.3.5/broker_grpc_lib/lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/lib/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/lib/broker_handler.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/lib/grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     6234 2023-04-06 14:03:38.000000 broker_grpc_lib-0.3.5/broker_grpc_lib/lib/rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.837626 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 14:04:10.000000 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-06 14:04:10.000000 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/SOURCES.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-06 14:04:10.000000 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/dependency_links.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-06 14:04:10.000000 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/requires.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-06 14:04:10.000000 broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/top_level.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-06 14:04:10.841709 broker_grpc_lib-0.3.5/setup.cfg
--rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-06 14:04:08.000000 broker_grpc_lib-0.3.5/setup.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.839383 broker_grpc_lib-0.3.5/tests/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.3.5/tests/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.839639 broker_grpc_lib-0.3.5/tests/functional/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.3.5/tests/functional/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.3.5/tests/functional/test_rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.840169 broker_grpc_lib-0.3.5/tests/helpers/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.3.5/tests/helpers/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.5/tests/helpers/async_iterator.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 09:03:49.000000 broker_grpc_lib-0.3.5/tests/helpers/grpc_stub.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:04:10.840909 broker_grpc_lib-0.3.5/tests/units/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.3.5/tests/units/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.3.5/tests/units/test_grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.5/tests/units/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.415798 broker_grpc_lib-0.3.6/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 14:09:29.415629 broker_grpc_lib-0.3.6/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      578 2023-04-06 07:45:45.000000 broker_grpc_lib-0.3.6/README.md
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.411178 broker_grpc_lib-0.3.6/broker_grpc_lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.412522 broker_grpc_lib-0.3.6/broker_grpc_lib/exc/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/exc/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/exc/no_queue_exception.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.413504 broker_grpc_lib-0.3.6/broker_grpc_lib/lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/lib/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/lib/broker_handler.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/lib/grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     6025 2023-04-06 14:09:16.000000 broker_grpc_lib-0.3.6/broker_grpc_lib/lib/rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.412086 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 14:09:29.000000 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-06 14:09:29.000000 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-06 14:09:29.000000 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-06 14:09:29.000000 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/requires.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-06 14:09:29.000000 broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/top_level.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-06 14:09:29.415845 broker_grpc_lib-0.3.6/setup.cfg
+-rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-06 14:09:27.000000 broker_grpc_lib-0.3.6/setup.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.413653 broker_grpc_lib-0.3.6/tests/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.3.6/tests/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.413900 broker_grpc_lib-0.3.6/tests/functional/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.3.6/tests/functional/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.3.6/tests/functional/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.414409 broker_grpc_lib-0.3.6/tests/helpers/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.3.6/tests/helpers/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.6/tests/helpers/async_iterator.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 09:03:49.000000 broker_grpc_lib-0.3.6/tests/helpers/grpc_stub.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 14:09:29.415107 broker_grpc_lib-0.3.6/tests/units/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.3.6/tests/units/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.3.6/tests/units/test_grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.6/tests/units/test_rabbitmq_handler.py
```

### Comparing `broker_grpc_lib-0.3.5/README.md` & `broker_grpc_lib-0.3.6/README.md`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.3.5/broker_grpc_lib/lib/broker_handler.py` & `broker_grpc_lib-0.3.6/broker_grpc_lib/lib/broker_handler.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.3.5/broker_grpc_lib/lib/grpc_client.py` & `broker_grpc_lib-0.3.6/broker_grpc_lib/lib/grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.3.5/broker_grpc_lib/lib/rabbitmq_handler.py` & `broker_grpc_lib-0.3.6/broker_grpc_lib/lib/rabbitmq_handler.py`

 * *Files 3% similar despite different names*

```diff
@@ -62,38 +62,31 @@
     async def __init_pools(self) -> bool:
         self._connection_pool = Pool(self.__get_connection, max_size=self._max_connections, loop=self._loop)
         self._channel_pool = Pool(self.__get_channel, max_size=self._max_channels, loop=self._loop)
 
         return True
 
     async def __init_queues(self) -> bool:
-        while True:
-            if not self._channel_pool:
-                logging.error("Channel pool is not initialized yet. Retrying in 5 sec.")
-                await asyncio.sleep(5)
-                continue
-            break
-
         for _ in range(self._max_channels):
             async with self._channel_pool.acquire() as channel:
                 if self._read_queue_name:
                     await channel.declare_queue(self._read_queue_name)
                 if self._write_queue_name:
                     await channel.declare_queue(self._write_queue_name)
                 if self._callback_queue_name:
                     await channel.declare_queue(self._callback_queue_name)
 
         return True
 
     async def prepare_handler(self):
-        pools, queues = False, False
-
         pools = await self.__init_pools()
-        if pools:
-            queues = await self.__init_queues()
+        queues = await self.__init_queues()
+
+        if pools and queues:
+            logging.info("Handler is initialized.")
 
         return pools and queues
 
     async def __get_connection(self) -> AbstractRobustConnection:
         try:
             while True:
                 connection = await aio_pika.connect_robust(
```

### Comparing `broker_grpc_lib-0.3.5/broker_grpc_lib.egg-info/SOURCES.txt` & `broker_grpc_lib-0.3.6/broker_grpc_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.3.5/setup.py` & `broker_grpc_lib-0.3.6/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 
 setup(
     name="broker_grpc_lib",
-    version="0.3.5",
+    version="0.3.6",
     description="Python package for easier use message brokers with gRPC application",
     author="multiadmin_optimus_prime",
     author_email="evgenykond@gmail.com",
     packages=find_packages(),
     install_requires=[
         "pydantic>=1.10.4",
         "aio-pika>=9.0.5",
```

### Comparing `broker_grpc_lib-0.3.5/tests/units/test_grpc_client.py` & `broker_grpc_lib-0.3.6/tests/units/test_grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.3.5/tests/units/test_rabbitmq_handler.py` & `broker_grpc_lib-0.3.6/tests/units/test_rabbitmq_handler.py`

 * *Files identical despite different names*

