# Comparing `tmp/broker_grpc_lib-0.2.1.tar.gz` & `tmp/broker_grpc_lib-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "broker_grpc_lib-0.2.1.tar", last modified: Thu Apr  6 07:17:43 2023, max compression
+gzip compressed data, was "broker_grpc_lib-0.3.0.tar", last modified: Thu Apr  6 13:26:19 2023, max compression
```

## Comparing `broker_grpc_lib-0.2.1.tar` & `broker_grpc_lib-0.3.0.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.072974 broker_grpc_lib-0.2.1/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 07:17:43.072773 broker_grpc_lib-0.2.1/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      565 2023-03-31 05:42:06.000000 broker_grpc_lib-0.2.1/README.md
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.068078 broker_grpc_lib-0.2.1/broker_grpc_lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.069612 broker_grpc_lib-0.2.1/broker_grpc_lib/exc/
--rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/exc/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/exc/no_queue_exception.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.070732 broker_grpc_lib-0.2.1/broker_grpc_lib/lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/lib/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/lib/broker_handler.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/lib/grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     5388 2023-04-06 06:01:40.000000 broker_grpc_lib-0.2.1/broker_grpc_lib/lib/rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.069176 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 07:17:43.000000 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-06 07:17:43.000000 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/SOURCES.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-06 07:17:43.000000 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/dependency_links.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-06 07:17:43.000000 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/requires.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-06 07:17:43.000000 broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/top_level.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-06 07:17:43.073033 broker_grpc_lib-0.2.1/setup.cfg
--rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-06 07:17:36.000000 broker_grpc_lib-0.2.1/setup.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.071086 broker_grpc_lib-0.2.1/tests/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.2.1/tests/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.071420 broker_grpc_lib-0.2.1/tests/functional/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.2.1/tests/functional/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.2.1/tests/functional/test_rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.072020 broker_grpc_lib-0.2.1/tests/helpers/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.2.1/tests/helpers/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.2.1/tests/helpers/async_iterator.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:36.000000 broker_grpc_lib-0.2.1/tests/helpers/grpc_stub.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:17:43.072504 broker_grpc_lib-0.2.1/tests/units/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.2.1/tests/units/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.2.1/tests/units/test_grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.2.1/tests/units/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.720518 broker_grpc_lib-0.3.0/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 13:26:19.720354 broker_grpc_lib-0.3.0/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      578 2023-04-06 07:45:45.000000 broker_grpc_lib-0.3.0/README.md
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.715582 broker_grpc_lib-0.3.0/broker_grpc_lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.717040 broker_grpc_lib-0.3.0/broker_grpc_lib/exc/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/exc/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/exc/no_queue_exception.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.718153 broker_grpc_lib-0.3.0/broker_grpc_lib/lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/lib/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/lib/broker_handler.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/lib/grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     5717 2023-04-06 13:26:14.000000 broker_grpc_lib-0.3.0/broker_grpc_lib/lib/rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.716604 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-06 13:26:19.000000 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-06 13:26:19.000000 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-06 13:26:19.000000 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-06 13:26:19.000000 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/requires.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-06 13:26:19.000000 broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/top_level.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-06 13:26:19.720565 broker_grpc_lib-0.3.0/setup.cfg
+-rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-06 13:26:14.000000 broker_grpc_lib-0.3.0/setup.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.718308 broker_grpc_lib-0.3.0/tests/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.3.0/tests/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.718563 broker_grpc_lib-0.3.0/tests/functional/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.3.0/tests/functional/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.3.0/tests/functional/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.719085 broker_grpc_lib-0.3.0/tests/helpers/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.3.0/tests/helpers/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.0/tests/helpers/async_iterator.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 09:03:49.000000 broker_grpc_lib-0.3.0/tests/helpers/grpc_stub.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-06 13:26:19.719843 broker_grpc_lib-0.3.0/tests/units/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.3.0/tests/units/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.3.0/tests/units/test_grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.3.0/tests/units/test_rabbitmq_handler.py
```

### Comparing `broker_grpc_lib-0.2.1/README.md` & `broker_grpc_lib-0.3.0/README.md`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# README #
+# Broker gRPC Library #
 
 This README would normally document whatever steps are necessary to get your application up and running.
 
 ### What is this repository for? ###
 
 * Quick summary
 * Version
```

### Comparing `broker_grpc_lib-0.2.1/broker_grpc_lib/lib/broker_handler.py` & `broker_grpc_lib-0.3.0/broker_grpc_lib/lib/broker_handler.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.2.1/broker_grpc_lib/lib/grpc_client.py` & `broker_grpc_lib-0.3.0/broker_grpc_lib/lib/grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.2.1/broker_grpc_lib/lib/rabbitmq_handler.py` & `broker_grpc_lib-0.3.0/broker_grpc_lib/lib/rabbitmq_handler.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 import aio_pika
 from aio_pika.pool import Pool
 from aio_pika import Channel, Message
 from aio_pika.abc import AbstractRobustConnection
+from aio_pika.exceptions import AMQPConnectionError
 
 from .broker_handler import BaseModel, BrokerHandler, T, RequestType
 from .grpc_client import GRPCClient
 from ..exc.no_queue_exception import NoReadQueueException, NoWriteQueueException
 
 import asyncio
 import signal
 import grpc
 
 from pydantic.error_wrappers import ValidationError
 from typing import Any, Type, Union
 
 import logging
+
 logging.basicConfig(level=logging.INFO)
 
 
 class RabbitMQHandler(BrokerHandler):
 
     def __init__(
             self,
@@ -78,20 +80,27 @@
     async def prepare_handler(self):
         pools = await self.__init_pools()
         queues = await self.__init_queues()
 
         return pools and queues
 
     async def __get_connection(self) -> AbstractRobustConnection:
-        return await aio_pika.connect_robust(
-            host=self._host,
-            login=self._login,
-            password=self._password,
-            port=self._port
-        )
+        try:
+            while True:
+                connection = await aio_pika.connect_robust(
+                    host=self._host,
+                    login=self._login,
+                    password=self._password,
+                    port=self._port
+                )
+
+                return connection
+        except AMQPConnectionError:
+            logging.error("Failed to connect to RabbitMQ. Retrying in 5 sec.")
+            await asyncio.sleep(5)
 
     async def __get_channel(self) -> Channel:
         async with self._connection_pool.acquire() as connection:
             return await connection.channel()
 
     async def start(self):
         if not self._read_queue_name:
```

### Comparing `broker_grpc_lib-0.2.1/broker_grpc_lib.egg-info/SOURCES.txt` & `broker_grpc_lib-0.3.0/broker_grpc_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.2.1/setup.py` & `broker_grpc_lib-0.3.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 
 setup(
     name="broker_grpc_lib",
-    version="0.2.1",
+    version="0.3.0",
     description="Python package for easier use message brokers with gRPC application",
     author="multiadmin_optimus_prime",
     author_email="evgenykond@gmail.com",
     packages=find_packages(),
     install_requires=[
         "pydantic>=1.10.4",
         "aio-pika>=9.0.5",
```

### Comparing `broker_grpc_lib-0.2.1/tests/units/test_grpc_client.py` & `broker_grpc_lib-0.3.0/tests/units/test_grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.2.1/tests/units/test_rabbitmq_handler.py` & `broker_grpc_lib-0.3.0/tests/units/test_rabbitmq_handler.py`

 * *Files identical despite different names*

